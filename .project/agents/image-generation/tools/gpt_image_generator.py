#!/usr/bin/env python3
"""
GPT Image 1.5 Generator for WorldSMEGraphs
===========================================

A robust async image generation tool using Azure AI Foundry's GPT Image 1.5 model.

Features:
- **PARALLEL GENERATION**: Generate multiple images concurrently up to rate limits
- **LINEAR BACKOFF**: Smart linear backoff (not geometric) when hitting rate limits
- **RATE LIMIT TRACKING**: Tracks observed limits in repository for optimization
- **SUPER EXPLICIT PROMPTS**: Comprehensive prompt enhancement based on best practices
- Async generation with polling for long-running operations
- Multiple variation support
- Automatic source control tracking
- High-quality output at maximum supported resolutions

Environment Variables Required:
- AI_FOUNDRY_API_KEY: API key for Azure AI Foundry
- AI_FOUNDRY_ENDPOINT: Base endpoint URL for Azure AI Foundry
- GPT_IMAGE_1DOT5_ENDPOINT_URL: Specific endpoint for GPT Image 1.5

Supported Resolutions (GPT Image 1.5):
- 1024x1024 (square) - default
- 1024x1536 (portrait) - 2:3 tall
- 1536x1024 (landscape) - 3:2 wide

Usage:
    python gpt_image_generator.py --prompt "Your prompt" --output image.png
    python gpt_image_generator.py --prompt "Your prompt" --aspect landscape --variations 3
    python gpt_image_generator.py --prompt-file prompts.txt --output-dir ./images/
    python gpt_image_generator.py --prompt-file prompts.txt --parallel 5  # Parallel generation

Author: WorldSMEGraphs Image Generation Agent
Version: 2.0.0  # Major upgrade with parallel generation and linear backoff
Created: 2026-01-04
Updated: 2026-01-04
"""

import os
import sys
import json
import time
import base64
import asyncio
import argparse
import hashlib
import subprocess
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import urllib.request
import urllib.error
import urllib.parse
import random

# Try to import yaml for config loading (optional dependency)
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# =============================================================================
# CONSTANTS
# =============================================================================

# Path to rate limits file (relative to this script)
RATE_LIMITS_FILE = Path(__file__).parent.parent / "rate-limits.yaml"

# Prompt length threshold for structured enhancement (chars)
PROMPT_LENGTH_THRESHOLD = 200

# Maximum number of rate limit events to track in history
RATE_LIMIT_HISTORY_SIZE = 10

# =============================================================================
# RATE LIMIT TRACKING
# =============================================================================

@dataclass
class RateLimitConfig:
    """Rate limit configuration loaded from repository."""
    requests_per_minute_safe: int = 40
    concurrent_requests_safe: int = 5
    backoff_type: str = "linear"
    base_delay_seconds: float = 5.0
    linear_increment_seconds: float = 5.0
    max_delay_seconds: float = 60.0
    max_retries: int = 5
    push_limits_probability: float = 0.1
    
    @classmethod
    def load_from_yaml(cls) -> "RateLimitConfig":
        """Load rate limit config from YAML file if available."""
        config = cls()
        if not YAML_AVAILABLE:
            return config  # Use defaults if yaml not available
        try:
            if RATE_LIMITS_FILE.exists():
                with open(RATE_LIMITS_FILE) as f:
                    data = yaml.safe_load(f)
                    if data:
                        api_limits = data.get("api_limits", {})
                        backoff = data.get("backoff", {})
                        config.requests_per_minute_safe = api_limits.get("requests_per_minute", {}).get("safe_target", 40)
                        config.concurrent_requests_safe = api_limits.get("concurrent_requests", {}).get("safe_target", 5)
                        config.backoff_type = backoff.get("type", "linear")
                        config.base_delay_seconds = backoff.get("base_delay_seconds", 5.0)
                        config.linear_increment_seconds = backoff.get("linear_increment_seconds", 5.0)
                        config.max_delay_seconds = backoff.get("max_delay_seconds", 60.0)
                        config.max_retries = backoff.get("max_retries", 5)
                        config.push_limits_probability = backoff.get("push_limits_probability", 0.1)
        except Exception:
            pass  # Use defaults if YAML loading fails
        return config


def calculate_linear_backoff(retry_count: int, config: RateLimitConfig) -> float:
    """Calculate linear backoff delay (not exponential per requirements)."""
    delay = config.base_delay_seconds + (retry_count * config.linear_increment_seconds)
    return min(delay, config.max_delay_seconds)


def should_push_limits(config: RateLimitConfig) -> bool:
    """Occasionally push beyond safe limits to test actual boundaries."""
    return random.random() < config.push_limits_probability


# =============================================================================
# CONFIGURATION
# =============================================================================

class AspectRatio(Enum):
    """Supported aspect ratios with their resolutions for GPT Image 1.5."""
    SQUARE = ("1024x1024", 1024, 1024)
    PORTRAIT = ("1024x1536", 1024, 1536)  # 2:3 tall
    LANDSCAPE = ("1536x1024", 1536, 1024)  # 3:2 wide
    AUTO = ("auto", 0, 0)  # Model decides
    
    @property
    def size(self) -> str:
        return self.value[0]
    
    @property
    def width(self) -> int:
        return self.value[1]
    
    @property
    def height(self) -> int:
        return self.value[2]


class Quality(Enum):
    """Image quality settings for GPT Image models."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    AUTO = "auto"  # Default - model selects best quality


@dataclass
class GenerationConfig:
    """Configuration for image generation."""
    prompt: str
    aspect_ratio: AspectRatio = AspectRatio.LANDSCAPE
    quality: Quality = Quality.HIGH
    n_variations: int = 1
    output_dir: Path = field(default_factory=lambda: Path("./generated_images"))
    output_prefix: str = "image"
    output_format: str = "png"  # png, jpeg, or webp
    background: str = "auto"  # auto, transparent, or opaque
    
    # Retry configuration - now uses LINEAR backoff
    max_retries: int = 5  # Increased for linear backoff
    retry_delay_base: float = 5.0  # Base delay for linear backoff
    retry_delay_increment: float = 5.0  # Linear increment per retry
    timeout_seconds: int = 180  # GPT image models can take time
    poll_interval: float = 5.0
    
    # Source control
    add_to_git: bool = True
    
    def __post_init__(self):
        self.output_dir = Path(self.output_dir)


@dataclass 
class GenerationResult:
    """Result of an image generation operation."""
    success: bool
    file_paths: List[Path] = field(default_factory=list)
    error_message: Optional[str] = None
    prompt_used: str = ""
    generation_time_seconds: float = 0.0
    retries_used: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    rate_limited: bool = False  # Track if we hit rate limits
    content_safety_modified: bool = False  # Track if prompt was modified for safety


class ContentSafetyError(Exception):
    """Exception raised when content safety blocks an image generation."""
    def __init__(self, message: str, code: str = ""):
        self.message = message
        self.code = code
        super().__init__(f"Content Safety Error: {message}")


class ContentSafetyHandler:
    """
    Handles content safety errors by modifying prompts.
    
    When the image generation API rejects a prompt due to content safety,
    this handler analyzes the error and modifies the prompt to be compliant.
    """
    
    # Keywords that might trigger content safety
    SENSITIVE_KEYWORDS = {
        "death", "kill", "blood", "violence", "weapon", "gun", "knife",
        "adult", "nude", "explicit", "sexy", "provocative",
        "drug", "cocaine", "heroin", "marijuana",
        "hate", "racist", "discrimination",
        "political", "election", "president", "government",
    }
    
    # Safe replacements for technical concepts
    SAFE_REPLACEMENTS = {
        "death": "transition",
        "kill": "terminate gracefully",
        "blood": "energy flow",
        "attack": "challenge",
        "crash": "unexpected stop",
        "destroy": "clean up",
        "explode": "expand rapidly",
        "injection": "insertion",
        "execute": "run",
        "daemon": "background service",
        "master": "primary",
        "slave": "replica",
        "kill signal": "stop signal",
        "killer feature": "standout feature",
    }
    
    @classmethod
    def sanitize_prompt(cls, prompt: str) -> str:
        """Pre-emptively sanitize a prompt before sending to the API."""
        result = prompt
        for old, new in cls.SAFE_REPLACEMENTS.items():
            if old.lower() in result.lower():
                # Case-insensitive replacement using pre-imported re module
                pattern = re.compile(re.escape(old), re.IGNORECASE)
                result = pattern.sub(new, result)
        return result
    
    @classmethod
    def modify_for_safety(cls, original_prompt: str, error_message: str) -> str:
        """
        Modify a prompt that was rejected for content safety.
        
        Args:
            original_prompt: The prompt that was rejected
            error_message: The error message from the API
            
        Returns:
            Modified prompt that should be safer
        """
        # Apply sanitization
        modified = cls.sanitize_prompt(original_prompt)
        
        # Add explicit safety constraints
        safety_suffix = """

Additional Constraints:
- Create family-friendly, professional artwork only
- Use abstract, geometric representations where appropriate
- Clean, corporate presentation style
- No controversial, violent, or adult imagery
- Suitable for business and educational contexts
"""
        
        return modified + safety_suffix
    
    @classmethod
    def log_for_manual_review(cls, original_prompt: str, error_message: str, 
                              auto_modified: str, log_path: Path = None) -> Path:
        """
        Log a prompt that needs manual inspection by a human or custom agent.
        
        Content safety issues often require human judgment to fix properly.
        This method logs the problematic prompt for later review.
        
        Args:
            original_prompt: The prompt that was rejected
            error_message: The error message from the API
            auto_modified: The automatically modified version (may still need work)
            log_path: Optional path to log file. Defaults to 'content-safety-review.yaml'
            
        Returns:
            Path to the log file
        """
        if log_path is None:
            log_path = Path(".project/agents/image-generation/content-safety-review.yaml")
        
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing log or create new
        existing_entries = []
        if log_path.exists():
            with open(log_path, 'r') as f:
                data = yaml.safe_load(f) or {}
                existing_entries = data.get('pending_review', [])
        
        # Create entry for review
        from datetime import datetime, timezone
        entry = {
            'id': f"safety-{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}",
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'status': 'pending_review',
            'original_prompt': original_prompt,
            'error_message': error_message,
            'auto_modified_prompt': auto_modified,
            'reviewer_notes': '',
            'final_prompt': '',
            'resolution': ''  # Options: 'fixed', 'skip', 'escalate'
        }
        
        existing_entries.append(entry)
        
        # Save log
        with open(log_path, 'w') as f:
            yaml.dump({
                'description': 'Prompts requiring manual review for content safety issues',
                'instructions': '''
Review each entry and either:
1. Edit 'final_prompt' with a safe version, set resolution to 'fixed'
2. Set resolution to 'skip' if the image should be omitted
3. Set resolution to 'escalate' if unsure and need expert help
''',
                'pending_review': existing_entries
            }, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        print(f"⚠️  Logged prompt for manual review: {log_path}")
        return log_path
    
    @classmethod
    def get_pending_reviews(cls, log_path: Path = None) -> list:
        """Get prompts pending manual review."""
        if log_path is None:
            log_path = Path(".project/agents/image-generation/content-safety-review.yaml")
        
        if not log_path.exists():
            return []
        
        with open(log_path, 'r') as f:
            data = yaml.safe_load(f) or {}
        
        return [e for e in data.get('pending_review', []) if e.get('status') == 'pending_review']


# =============================================================================
# PROMPTING BEST PRACTICES (Based on GPT Image 1.5 Prompting Guide)
# From: https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-1.5-prompting_guide.ipynb
# =============================================================================

PROMPT_GUIDELINES = """
GPT Image 1.5 Prompting Best Practices (Comprehensive Guide)
=============================================================

KEY PRINCIPLES FROM OPENAI COOKBOOK:
1. BE SUPER EXPLICIT - The model has world knowledge but needs explicit instructions
   for domain-specific accuracy (e.g., blood flow direction, arrow orientations)
2. USE STRUCTURED PROMPTS - Organize with sections: Scene, Style, Constraints, etc.
3. SEPARATE INVARIANTS - Clearly state what should NOT change
4. ITERATE SMALL - Make small changes, restate invariants on every iteration

PROMPT STRUCTURE TEMPLATE:
--------------------------
```
Create [TYPE OF IMAGE].

Scene:
[Detailed scene description with specific elements, positions, and relationships]

Style:
[Visual style, lighting, mood, technique - be specific]

Technical Details:
[Colors, materials, textures - be explicit about directions, orientations]

Constraints:
- [What to avoid or exclude]
- Original artwork only
- No watermarks/logos

[Optional] Include ONLY this text: "[exact text if needed]"
```

BEING SUPER EXPLICIT (Critical for accuracy):
- BAD: "blood vessels with blood flow"
- GOOD: "blood vessels showing red oxygenated blood flowing FROM the heart 
         through arteries (arrows pointing outward from center), and blue 
         deoxygenated blood flowing TOWARD the heart through veins 
         (arrows pointing inward toward center)"

- BAD: "morphism arrows in category theory"  
- GOOD: "morphism arrows connecting objects, all arrows pointing LEFT TO RIGHT
         to indicate composition direction, with arrow heads on the RIGHT side
         of each connection, demonstrating f: A → B composition"

VISUAL STYLE SPECIFICATIONS:
- Photography: "photorealistic", "35mm film", "cinematic", "studio photography"
- Illustration: "digital illustration", "watercolor", "vector art", "hand-painted"
- Technical: "technical diagram", "infographic", "flowchart", "schematic"
- Corporate: "clean corporate style", "professional presentation", "minimal design"

COMPOSITION SPECIFICATIONS:
- Camera angle: "bird's eye view", "isometric", "low angle", "close-up", "wide shot"
- Layout: "centered composition", "rule of thirds", "symmetrical", "asymmetrical"
- Depth: "shallow depth of field", "deep focus", "bokeh background"

LIGHTING SPECIFICATIONS:
- "soft diffused lighting", "dramatic shadows", "golden hour", "blue hour"
- "studio lighting with soft boxes", "natural daylight through windows"
- "rim lighting", "backlit", "silhouette", "high key", "low key"

TEXTURE & MATERIAL SPECIFICATIONS:
- "realistic textures", "smooth gradients", "glossy finish", "matte surface"
- "paper texture", "fabric texture", "metallic sheen", "glass transparency"

AVOIDING COMMON MISTAKES:
1. ❌ Using negative instructions ("no people") 
   ✓ Instead, describe what you DO want
2. ❌ Vague style descriptions ("nice", "good")
   ✓ Use specific style terms ("photorealistic", "watercolor illustration")
3. ❌ Assuming the model knows specific orientations
   ✓ Explicitly state directions (left-to-right, clockwise, etc.)
4. ❌ Requesting text in images (often renders poorly)
   ✓ Use overlays or keep text minimal and specify font style
5. ❌ Overly complex prompts without structure
   ✓ Use sections with clear headers

FOR TECHNICAL/SCIENTIFIC DIAGRAMS:
- ALWAYS specify:
  - Arrow directions and what they represent
  - Color coding and its meaning
  - Relative positions and relationships
  - Label placements (even if using overlays later)
  - Scale relationships between elements

FOR PRESENTATION SLIDES:
```
Create a presentation slide background for [TOPIC].

Visual Elements:
[Specific abstract elements that convey the concept]

Color Palette:
[Exact colors or color scheme, e.g., "Microsoft Azure blue (#0078D4) 
with purple accents (#8661C5)"]

Style:
Professional corporate presentation, clean modern design,
subtle geometric patterns, suitable for developer conference,
no text elements, high quality.

Mood:
[Professional, innovative, technical, warm, etc.]
```

CONSISTENCY ACROSS MULTIPLE IMAGES:
When generating a series, use "Character Consistency" sections:
```
Character/Element Consistency:
- Same [color palette/proportions/style] as previous images
- Maintain [specific visual elements]
- Do not redesign the [element]
```
"""


def enhance_prompt(base_prompt: str, style_hints: Optional[str] = None, 
                   domain_hints: Optional[Dict[str, str]] = None) -> str:
    """
    Enhance a prompt with best practices for better results.
    
    Based on the OpenAI GPT Image 1.5 Prompting Guide, this function
    ensures prompts are SUPER EXPLICIT to minimize generation errors.
    
    Args:
        base_prompt: The user's original prompt
        style_hints: Optional style guidance (e.g., "technical", "fun", "professional")
        domain_hints: Optional domain-specific hints for explicit specifications
                     e.g., {"arrows": "left-to-right", "flow": "clockwise"}
    
    Returns:
        Enhanced prompt with quality improvements and explicit specifications
    """
    enhancements = []
    
    # Check if prompt lacks quality specifiers
    quality_keywords = ["high quality", "detailed", "professional", "hd", "4k", "high-end"]
    if not any(kw in base_prompt.lower() for kw in quality_keywords):
        enhancements.append("high quality")
    
    # Check if prompt lacks style specifiers
    style_keywords = ["style", "illustration", "photo", "render", "drawing", "realistic"]
    if not any(kw in base_prompt.lower() for kw in style_keywords):
        if style_hints == "technical":
            enhancements.append("clean technical illustration style with precise lines")
        elif style_hints == "fun":
            enhancements.append("vibrant colorful illustration style")
        elif style_hints == "professional":
            enhancements.append("professional corporate style, clean and modern")
        elif style_hints == "scientific":
            enhancements.append("scientific illustration style with accurate proportions")
    
    # Check if prompt lacks lighting
    lighting_keywords = ["lighting", "light", "shadows", "bright", "dark", "lit"]
    if not any(kw in base_prompt.lower() for kw in lighting_keywords):
        enhancements.append("soft professional lighting")
    
    # Check if prompt lacks composition hints
    composition_keywords = ["composition", "centered", "layout", "angle", "view"]
    if not any(kw in base_prompt.lower() for kw in composition_keywords):
        enhancements.append("well-composed")
    
    # Add domain-specific explicit hints
    if domain_hints:
        for key, value in domain_hints.items():
            enhancements.append(f"{key}: {value}")
    
    # Build enhanced prompt with structure if it's short
    if len(base_prompt) < PROMPT_LENGTH_THRESHOLD:
        # Add structured format for short prompts
        structured_prompt = f"""
{base_prompt}

Style: {', '.join(enhancements) if enhancements else 'professional, clean'}

Constraints:
- Original artwork only
- No watermarks or logos
"""
        return structured_prompt.strip()
    
    # For longer prompts, just append enhancements
    if enhancements:
        return f"{base_prompt}, {', '.join(enhancements)}"
    return base_prompt


# =============================================================================
# API CLIENT
# =============================================================================

class GPTImageClient:
    """
    Async client for GPT Image 1.5 via Azure AI Foundry.
    
    Handles:
    - Authentication with Azure AI Foundry
    - PARALLEL image generation (up to rate limits)
    - LINEAR backoff retry logic (not exponential)
    - Rate limit tracking and intelligent throttling
    - Response parsing and image saving
    """
    
    def __init__(self):
        self.api_key = os.environ.get("AI_FOUNDRY_API_KEY")
        self.endpoint = os.environ.get("AI_FOUNDRY_ENDPOINT")
        self.image_endpoint = os.environ.get("GPT_IMAGE_1DOT5_ENDPOINT_URL")
        
        # Load rate limit configuration
        self.rate_config = RateLimitConfig.load_from_yaml()
        
        # Track concurrent requests
        self._active_requests = 0
        self._request_lock = asyncio.Lock()
        
        # Rate limit tracking
        self._rate_limit_events = []
        
        # Validate environment
        missing = []
        if not self.api_key:
            missing.append("AI_FOUNDRY_API_KEY")
        if not self.endpoint:
            missing.append("AI_FOUNDRY_ENDPOINT")
        if not self.image_endpoint:
            missing.append("GPT_IMAGE_1DOT5_ENDPOINT_URL")
        
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}\n"
                "Please set these secrets in your GitHub environment."
            )
    
    def _build_request(self, config: GenerationConfig) -> Tuple[str, bytes, Dict[str, str]]:
        """Build the API request according to OpenAI GPT Image 1.5 API spec."""
        # Use the specific endpoint or default to OpenAI
        url = self.image_endpoint or "https://api.openai.com/v1/images/generations"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        
        # Add Azure-specific header if using Azure endpoint
        if self.endpoint and "azure" in self.endpoint.lower():
            headers["api-key"] = self.api_key
        
        # Build payload according to GPT Image 1.5 API spec
        payload = {
            "model": "gpt-image-1.5",
            "prompt": config.prompt,
            "n": config.n_variations,
            "size": config.aspect_ratio.size,
            "quality": config.quality.value,
            "output_format": config.output_format,
            "background": config.background,
        }
        
        return url, json.dumps(payload).encode("utf-8"), headers
    
    async def generate_images_parallel(self, configs: List[GenerationConfig], 
                                        max_concurrent: Optional[int] = None) -> List[GenerationResult]:
        """
        Generate multiple images in PARALLEL up to rate limits.
        
        This is the preferred method for batch generation. It respects rate limits
        and uses intelligent linear backoff when limits are hit.
        
        Args:
            configs: List of generation configurations
            max_concurrent: Max concurrent requests (default: from rate_config)
            
        Returns:
            List of GenerationResults in same order as configs
        """
        if max_concurrent is None:
            # Optionally push limits sometimes
            if should_push_limits(self.rate_config):
                max_concurrent = self.rate_config.concurrent_requests_safe + 2
                print(f"🚀 Pushing limits: trying {max_concurrent} concurrent requests")
            else:
                max_concurrent = self.rate_config.concurrent_requests_safe
        
        # Create semaphore to limit concurrency
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def generate_with_semaphore(config: GenerationConfig, index: int) -> Tuple[int, GenerationResult]:
            async with semaphore:
                print(f"  [{index+1}/{len(configs)}] Starting: {config.prompt[:50]}...")
                try:
                    result = await self.generate_image(config)
                    return index, result
                except Exception as e:
                    # Wrap any exception in a failed GenerationResult
                    return index, GenerationResult(
                        success=False,
                        error_message=str(e),
                        prompt_used=config.prompt
                    )
        
        # Launch all tasks concurrently (semaphore limits actual concurrency)
        tasks = [
            generate_with_semaphore(config, i) 
            for i, config in enumerate(configs)
        ]
        
        print(f"\n🎨 Generating {len(configs)} images in parallel (max {max_concurrent} concurrent)...")
        
        # Wait for all to complete - exceptions are now wrapped in GenerationResult
        indexed_results = await asyncio.gather(*tasks)
        
        # Sort results back to original order (all items are now (index, result) tuples)
        results = [None] * len(configs)
        for index, result in indexed_results:
            results[index] = result
        
        # Summary
        successful = sum(1 for r in results if r and r.success)
        rate_limited = sum(1 for r in results if r and r.rate_limited)
        print(f"\n✅ Completed: {successful}/{len(configs)} successful")
        if rate_limited:
            print(f"⚠️  Rate limited: {rate_limited} requests (handled with backoff)")
        
        return results
    
    async def generate_image(self, config: GenerationConfig) -> GenerationResult:
        """
        Generate image(s) with LINEAR backoff retry logic.
        
        Uses linear backoff (not exponential) as per requirements for
        a more gradual and predictable retry pattern.
        
        Also handles content safety errors by modifying prompts automatically.
        
        Args:
            config: Generation configuration
            
        Returns:
            GenerationResult with success status and file paths
        """
        start_time = time.time()
        retries = 0
        last_error = None
        rate_limited = False
        content_safety_modified = False
        current_prompt = config.prompt
        
        while retries <= self.rate_config.max_retries:
            try:
                async with self._request_lock:
                    self._active_requests += 1
                
                try:
                    # Update config with current prompt (may have been modified for safety)
                    modified_config = GenerationConfig(
                        prompt=current_prompt,
                        aspect_ratio=config.aspect_ratio,
                        quality=config.quality,
                        n_variations=config.n_variations,
                        output_dir=config.output_dir,
                        output_prefix=config.output_prefix,
                        output_format=config.output_format,
                        background=config.background,
                        max_retries=config.max_retries,
                        retry_delay_base=config.retry_delay_base,
                        retry_delay_increment=config.retry_delay_increment,
                        timeout_seconds=config.timeout_seconds,
                        poll_interval=config.poll_interval,
                        add_to_git=config.add_to_git
                    )
                    result = await self._attempt_generation(modified_config)
                    result.generation_time_seconds = time.time() - start_time
                    result.retries_used = retries
                    result.rate_limited = rate_limited
                    result.content_safety_modified = content_safety_modified
                    return result
                finally:
                    async with self._request_lock:
                        self._active_requests -= 1
            
            except ContentSafetyError as e:
                # Content safety error - try to modify prompt and retry
                print(f"  ⚠️  Content safety issue: {e.message[:100]}...")
                retries += 1
                content_safety_modified = True
                current_prompt = ContentSafetyHandler.modify_for_safety(current_prompt, str(e))
                print(f"  🔄 Modified prompt for safety, retrying...")
                # Short delay before retry
                await asyncio.sleep(2)
                    
            except Exception as e:
                last_error = str(e)
                retries += 1
                
                # Check if rate limited
                is_rate_limit = "429" in str(e) or "rate" in str(e).lower()
                if is_rate_limit:
                    rate_limited = True
                    self._record_rate_limit_event(str(e))
                
                if retries <= self.rate_config.max_retries:
                    # LINEAR backoff (not exponential)
                    delay = calculate_linear_backoff(retries, self.rate_config)
                    print(f"  ⏳ Retry {retries}/{self.rate_config.max_retries} after {delay:.1f}s: {e}")
                    await asyncio.sleep(delay)
        
        return GenerationResult(
            success=False,
            error_message=f"Failed after {self.rate_config.max_retries} retries: {last_error}",
            prompt_used=current_prompt,
            generation_time_seconds=time.time() - start_time,
            retries_used=retries,
            rate_limited=rate_limited,
            content_safety_modified=content_safety_modified
        )
    
    def _record_rate_limit_event(self, error_message: str):
        """Record a rate limit event for tracking."""
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "concurrent_at_time": self._active_requests,
            "message": error_message[:200]  # Truncate long messages
        }
        self._rate_limit_events.append(event)
        
        # Keep only last N events (defined by constant)
        if len(self._rate_limit_events) > RATE_LIMIT_HISTORY_SIZE:
            self._rate_limit_events = self._rate_limit_events[-RATE_LIMIT_HISTORY_SIZE:]
    
    async def _attempt_generation(self, config: GenerationConfig) -> GenerationResult:
        """Single generation attempt."""
        url, data, headers = self._build_request(config)
        
        # Make async request (using sync urllib in thread for simplicity)
        loop = asyncio.get_event_loop()
        response_data = await loop.run_in_executor(
            None, 
            self._sync_request, 
            url, data, headers, config.timeout_seconds
        )
        
        # Parse response
        response = json.loads(response_data)
        
        if "error" in response:
            error_msg = response["error"].get("message", "Unknown API error")
            error_code = response["error"].get("code", "")
            # Check for content safety issues
            if any(term in error_msg.lower() for term in ["content", "safety", "policy", "moderation", "rejected"]):
                raise ContentSafetyError(error_msg, error_code)
            raise Exception(error_msg)
        
        # Handle async generation with polling if needed
        if "id" in response and "status" in response:
            # This is an async operation, poll for completion
            response = await self._poll_for_completion(
                response["id"], 
                config.poll_interval,
                config.timeout_seconds
            )
        
        # Extract and save images
        file_paths = await self._save_images(response, config)
        
        return GenerationResult(
            success=True,
            file_paths=file_paths,
            prompt_used=config.prompt,
            metadata=response
        )
    
    def _sync_request(self, url: str, data: bytes, headers: Dict[str, str], 
                      timeout: int) -> str:
        """Synchronous HTTP request."""
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            raise Exception(f"HTTP {e.code}: {error_body}")
    
    async def _poll_for_completion(self, operation_id: str, poll_interval: float,
                                    timeout: int) -> Dict[str, Any]:
        """Poll for async operation completion."""
        status_url = f"{self.endpoint}/operations/{operation_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "api-key": self.api_key,
        }
        
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            loop = asyncio.get_event_loop()
            
            req = urllib.request.Request(status_url, headers=headers)
            response_data = await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
            )
            
            response = json.loads(response_data)
            status = response.get("status", "unknown")
            
            if status == "succeeded":
                return response.get("result", response)
            elif status in ("failed", "cancelled"):
                raise Exception(f"Operation {status}: {response.get('error', 'Unknown error')}")
            
            print(f"Generation in progress... ({status})")
            await asyncio.sleep(poll_interval)
        
        raise TimeoutError(f"Operation timed out after {timeout} seconds")
    
    async def _save_images(self, response: Dict[str, Any], 
                           config: GenerationConfig) -> List[Path]:
        """Save generated images to disk and optionally add to git."""
        config.output_dir.mkdir(parents=True, exist_ok=True)
        
        saved_paths = []
        images = response.get("data", [])
        
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        prompt_hash = hashlib.md5(config.prompt.encode()).hexdigest()[:8]
        
        # Determine file extension from output format
        ext = config.output_format if config.output_format in ["png", "jpeg", "webp"] else "png"
        
        for i, image_data in enumerate(images):
            suffix = f"_v{i+1}" if len(images) > 1 else ""
            filename = f"{config.output_prefix}_{timestamp}_{prompt_hash}{suffix}.{ext}"
            filepath = config.output_dir / filename
            
            # GPT Image models return base64-encoded images directly
            b64_data = image_data.get("b64_json", "")
            if b64_data:
                image_bytes = base64.b64decode(b64_data)
            else:
                # Fallback: try URL if available (for dall-e models)
                url = image_data.get("url", "")
                if url:
                    with urllib.request.urlopen(url) as resp:
                        image_bytes = resp.read()
                else:
                    print(f"Warning: No image data found for image {i+1}")
                    continue
            
            # Save image
            with open(filepath, "wb") as f:
                f.write(image_bytes)
            
            print(f"✓ Saved: {filepath} ({len(image_bytes)} bytes)")
            saved_paths.append(filepath)
            
            # Add to git if requested
            if config.add_to_git:
                try:
                    subprocess.run(
                        ["git", "add", str(filepath)],
                        check=True,
                        capture_output=True,
                        cwd=str(config.output_dir.parent)
                    )
                    print(f"Added to git: {filepath}")
                except subprocess.CalledProcessError as e:
                    print(f"Warning: Could not add to git: {e}")
        
        # Save metadata
        metadata_path = config.output_dir / f"metadata_{timestamp}_{prompt_hash}.json"
        with open(metadata_path, "w") as f:
            json.dump({
                "prompt": config.prompt,
                "aspect_ratio": config.aspect_ratio.name,
                "quality": config.quality.value,
                "n_variations": config.n_variations,
                "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "files": [str(p) for p in saved_paths],
                "response": response
            }, f, indent=2)
        
        return saved_paths


# =============================================================================
# CLI INTERFACE
# =============================================================================

def create_parser() -> argparse.ArgumentParser:
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate images using GPT Image 1.5 via Azure AI Foundry",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=PROMPT_GUIDELINES
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--prompt", "-p", type=str, help="Image generation prompt")
    input_group.add_argument("--prompt-file", "-f", type=Path, 
                             help="File containing prompts (one per line)")
    
    # Output options
    parser.add_argument("--output", "-o", type=Path, default=None,
                       help="Output file path (single image) or prefix (multiple)")
    parser.add_argument("--output-dir", "-d", type=Path, 
                       default=Path("./generated_images"),
                       help="Output directory (default: ./generated_images)")
    
    # Generation options
    parser.add_argument("--aspect", "-a", type=str, default="landscape",
                       choices=["square", "portrait", "landscape", "auto"],
                       help="Aspect ratio (default: landscape)")
    parser.add_argument("--quality", "-q", type=str, default="high",
                       choices=["low", "medium", "high", "auto"],
                       help="Image quality (default: high)")
    parser.add_argument("--variations", "-n", type=int, default=1,
                       help="Number of variations to generate (default: 1)")
    parser.add_argument("--format", type=str, default="png",
                       choices=["png", "jpeg", "webp"],
                       help="Output image format (default: png)")
    parser.add_argument("--background", type=str, default="auto",
                       choices=["auto", "transparent", "opaque"],
                       help="Background type (default: auto)")
    
    # PARALLEL GENERATION options (NEW)
    parser.add_argument("--parallel", type=int, default=None,
                       help="Max concurrent requests for parallel generation (default: from rate-limits.yaml)")
    parser.add_argument("--sequential", action="store_true",
                       help="Force sequential generation (one at a time)")
    
    # Enhancement options
    parser.add_argument("--enhance", "-e", action="store_true",
                       help="Enhance prompt with best practices (RECOMMENDED)")
    parser.add_argument("--style-hint", type=str, default=None,
                       choices=["technical", "fun", "professional", "scientific"],
                       help="Style hint for prompt enhancement")
    
    # Retry options (LINEAR backoff)
    parser.add_argument("--max-retries", type=int, default=5,
                       help="Maximum retry attempts with LINEAR backoff (default: 5)")
    parser.add_argument("--timeout", type=int, default=180,
                       help="Request timeout in seconds (default: 180)")
    
    # Git options
    parser.add_argument("--no-git", action="store_true",
                       help="Don't add generated images to git")
    
    # Utility options
    parser.add_argument("--guidelines", action="store_true",
                       help="Print comprehensive prompting guidelines and exit")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be generated without making API calls")
    parser.add_argument("--show-rate-limits", action="store_true",
                       help="Show current rate limit configuration and exit")
    
    return parser


async def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.guidelines:
        print(PROMPT_GUIDELINES)
        return 0
    
    if args.show_rate_limits:
        config = RateLimitConfig.load_from_yaml()
        print("Current Rate Limit Configuration:")
        print(f"  Requests/min (safe): {config.requests_per_minute_safe}")
        print(f"  Concurrent (safe):   {config.concurrent_requests_safe}")
        print(f"  Backoff type:        {config.backoff_type}")
        print(f"  Base delay:          {config.base_delay_seconds}s")
        print(f"  Linear increment:    {config.linear_increment_seconds}s")
        print(f"  Max delay:           {config.max_delay_seconds}s")
        print(f"  Max retries:         {config.max_retries}")
        print(f"  Push limits prob:    {config.push_limits_probability*100:.0f}%")
        return 0
    
    # Collect prompts
    prompts = []
    if args.prompt:
        prompts.append(args.prompt)
    elif args.prompt_file:
        with open(args.prompt_file) as f:
            prompts = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    # Enhance prompts if requested (RECOMMENDED for best results)
    if args.enhance:
        print("🔧 Enhancing prompts with best practices...")
        prompts = [enhance_prompt(p, args.style_hint) for p in prompts]
    
    # Map aspect ratio
    aspect_map = {
        "square": AspectRatio.SQUARE,
        "portrait": AspectRatio.PORTRAIT,
        "landscape": AspectRatio.LANDSCAPE,
        "auto": AspectRatio.AUTO,
    }
    
    # Map quality
    quality_map = {
        "low": Quality.LOW,
        "medium": Quality.MEDIUM,
        "high": Quality.HIGH,
        "auto": Quality.AUTO,
    }
    
    if args.dry_run:
        print("DRY RUN - Would generate the following:")
        mode = "sequential" if args.sequential else f"parallel (max {args.parallel or 'auto'})"
        print(f"Mode: {mode}")
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}] Prompt: {prompt[:100]}...")
            print(f"    Aspect: {args.aspect} ({aspect_map[args.aspect].size})")
            print(f"    Quality: {args.quality}")
            print(f"    Variations: {args.variations}")
            print(f"    Format: {args.format}")
            print(f"    Background: {args.background}")
            print(f"    Output dir: {args.output_dir}")
        return 0
    
    # Initialize client
    try:
        client = GPTImageClient()
    except EnvironmentError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    # Build configs for all prompts
    configs = []
    for i, prompt in enumerate(prompts):
        config = GenerationConfig(
            prompt=prompt,
            aspect_ratio=aspect_map[args.aspect],
            quality=quality_map[args.quality],
            n_variations=args.variations,
            output_dir=args.output_dir,
            output_prefix=Path(args.output).stem if args.output else f"image_{i+1:03d}",
            output_format=args.format,
            background=args.background,
            max_retries=args.max_retries,
            timeout_seconds=args.timeout,
            add_to_git=not args.no_git,
        )
        configs.append(config)
    
    # Choose generation mode
    if args.sequential or len(configs) == 1:
        # Sequential generation (one at a time)
        print(f"\n🎨 Generating {len(configs)} images sequentially...")
        all_results = []
        for i, config in enumerate(configs, 1):
            print(f"\n{'='*60}")
            print(f"[{i}/{len(configs)}] {config.prompt[:50]}...")
            print(f"{'='*60}")
            
            result = await client.generate_image(config)
            all_results.append(result)
            
            if result.success:
                print(f"\n✓ Success! Generated {len(result.file_paths)} image(s)")
                print(f"  Time: {result.generation_time_seconds:.1f}s")
                print(f"  Retries: {result.retries_used}")
                for path in result.file_paths:
                    print(f"  File: {path}")
            else:
                print(f"\n✗ Failed: {result.error_message}")
    else:
        # PARALLEL generation (recommended for multiple images)
        all_results = await client.generate_images_parallel(configs, max_concurrent=args.parallel)
        
        # Print individual results
        for i, result in enumerate(all_results, 1):
            if result.success:
                print(f"  [{i}] ✓ {', '.join(str(p) for p in result.file_paths)}")
            else:
                print(f"  [{i}] ✗ {result.error_message}")
    
    # Summary
    successful = sum(1 for r in all_results if r.success)
    print(f"\n{'='*60}")
    print(f"Summary: {successful}/{len(all_results)} prompts succeeded")
    print(f"{'='*60}")
    
    return 0 if all(r.success for r in all_results) else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
