#!/usr/bin/env python3
"""
GPT Image 1.5 Generator for WorldSMEGraphs
===========================================

A robust async image generation tool using Azure AI Foundry's GPT Image 1.5 model.

Features:
- Async generation with polling for long-running operations
- Automatic retry logic with exponential backoff
- Multiple variation support
- Automatic source control tracking
- High-quality output at maximum supported resolutions

Environment Variables Required:
- AI_FOUNDRY_API_KEY: API key for Azure AI Foundry
- AI_FOUNDRY_ENDPOINT: Base endpoint URL for Azure AI Foundry
- GPT_IMAGE_1DOT5_ENDPOINT_URL: Specific endpoint for GPT Image 1.5

Supported Resolutions (GPT Image 1.5):
- 1024x1024 (square) - default
- 1024x1792 (portrait) 
- 1792x1024 (landscape)
- 1536x1024 (wide landscape - 3:2)
- 1024x1536 (tall portrait - 2:3)

Usage:
    python gpt_image_generator.py --prompt "Your prompt" --output image.png
    python gpt_image_generator.py --prompt "Your prompt" --aspect landscape --variations 3
    python gpt_image_generator.py --prompt-file prompts.txt --output-dir ./images/

Author: WorldSMEGraphs Image Generation Agent
Version: 1.0.0
Created: 2026-01-04
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
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import urllib.request
import urllib.error
import urllib.parse

# =============================================================================
# CONFIGURATION
# =============================================================================

class AspectRatio(Enum):
    """Supported aspect ratios with their resolutions."""
    SQUARE = ("1024x1024", 1024, 1024)
    PORTRAIT = ("1024x1792", 1024, 1792)
    LANDSCAPE = ("1792x1024", 1792, 1024)
    WIDE = ("1536x1024", 1536, 1024)
    TALL = ("1024x1536", 1024, 1536)
    
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
    """Image quality settings."""
    STANDARD = "standard"
    HD = "hd"
    HIGH = "high"  # Alias for HD


@dataclass
class GenerationConfig:
    """Configuration for image generation."""
    prompt: str
    aspect_ratio: AspectRatio = AspectRatio.LANDSCAPE
    quality: Quality = Quality.HD
    n_variations: int = 1
    output_dir: Path = field(default_factory=lambda: Path("./generated_images"))
    output_prefix: str = "image"
    response_format: str = "b64_json"  # or "url"
    style: str = "vivid"  # or "natural"
    
    # Retry configuration
    max_retries: int = 3
    retry_delay_base: float = 2.0  # Exponential backoff base
    timeout_seconds: int = 120
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


# =============================================================================
# PROMPTING BEST PRACTICES (Based on GPT Image 1.5 Prompting Guide)
# =============================================================================

PROMPT_GUIDELINES = """
GPT Image 1.5 Prompting Best Practices:
========================================

1. BE SPECIFIC AND DETAILED
   - Include subject, setting, lighting, mood, style
   - Bad: "a cat"
   - Good: "A fluffy orange tabby cat sitting on a windowsill, soft afternoon 
           sunlight streaming through, cozy home interior, photorealistic"

2. SPECIFY VISUAL STYLE
   - Photography: "photorealistic", "35mm film", "cinematic"
   - Illustration: "digital illustration", "watercolor", "vector art"
   - Technical: "technical diagram", "infographic", "flowchart"

3. DESCRIBE COMPOSITION
   - Camera angle: "bird's eye view", "low angle", "close-up", "wide shot"
   - Layout: "centered composition", "rule of thirds", "symmetrical"

4. INCLUDE LIGHTING
   - "soft diffused lighting", "dramatic shadows", "golden hour"
   - "studio lighting", "natural daylight", "neon lights"

5. AVOID NEGATIVES
   - Instead of "no people", describe what you DO want
   - The model handles positive instructions better

6. FOR DIAGRAMS/INFOGRAPHICS
   - Specify: colors, layout, typography style, icon style
   - Include: "clean lines", "minimal design", "professional"
   - Avoid: text in images (use overlays instead)

7. FOR PRESENTATIONS
   - Use: "presentation slide background", "clean corporate style"
   - Specify: color palette, mood (professional, creative, technical)
"""


def enhance_prompt(base_prompt: str, style_hints: Optional[str] = None) -> str:
    """
    Enhance a prompt with best practices for better results.
    
    Args:
        base_prompt: The user's original prompt
        style_hints: Optional style guidance (e.g., "technical", "fun", "professional")
    
    Returns:
        Enhanced prompt with quality improvements
    """
    enhancements = []
    
    # Check if prompt lacks quality specifiers
    quality_keywords = ["high quality", "detailed", "professional", "hd", "4k"]
    if not any(kw in base_prompt.lower() for kw in quality_keywords):
        enhancements.append("high quality")
    
    # Check if prompt lacks style specifiers
    style_keywords = ["style", "illustration", "photo", "render", "drawing"]
    if not any(kw in base_prompt.lower() for kw in style_keywords):
        if style_hints == "technical":
            enhancements.append("clean technical illustration style")
        elif style_hints == "fun":
            enhancements.append("vibrant colorful illustration style")
        elif style_hints == "professional":
            enhancements.append("professional corporate style")
    
    # Check if prompt lacks lighting
    lighting_keywords = ["lighting", "light", "shadows", "bright", "dark"]
    if not any(kw in base_prompt.lower() for kw in lighting_keywords):
        enhancements.append("well-lit")
    
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
    - Async image generation with polling
    - Retry logic with exponential backoff
    - Response parsing and image saving
    """
    
    def __init__(self):
        self.api_key = os.environ.get("AI_FOUNDRY_API_KEY")
        self.endpoint = os.environ.get("AI_FOUNDRY_ENDPOINT")
        self.image_endpoint = os.environ.get("GPT_IMAGE_1DOT5_ENDPOINT_URL")
        
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
        """Build the API request."""
        url = self.image_endpoint
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "api-key": self.api_key,  # Azure-specific header
        }
        
        payload = {
            "model": "gpt-image-1.5",
            "prompt": config.prompt,
            "n": config.n_variations,
            "size": config.aspect_ratio.size,
            "quality": config.quality.value if config.quality != Quality.HIGH else "hd",
            "response_format": config.response_format,
            "style": config.style,
        }
        
        return url, json.dumps(payload).encode("utf-8"), headers
    
    async def generate_image(self, config: GenerationConfig) -> GenerationResult:
        """
        Generate image(s) with retry logic and polling.
        
        Args:
            config: Generation configuration
            
        Returns:
            GenerationResult with success status and file paths
        """
        start_time = time.time()
        retries = 0
        last_error = None
        
        while retries <= config.max_retries:
            try:
                result = await self._attempt_generation(config)
                result.generation_time_seconds = time.time() - start_time
                result.retries_used = retries
                return result
                
            except Exception as e:
                last_error = str(e)
                retries += 1
                
                if retries <= config.max_retries:
                    delay = config.retry_delay_base ** retries
                    print(f"Retry {retries}/{config.max_retries} after {delay:.1f}s: {e}")
                    await asyncio.sleep(delay)
        
        return GenerationResult(
            success=False,
            error_message=f"Failed after {config.max_retries} retries: {last_error}",
            prompt_used=config.prompt,
            generation_time_seconds=time.time() - start_time,
            retries_used=retries
        )
    
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
            raise Exception(response["error"].get("message", "Unknown API error"))
        
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
        
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        prompt_hash = hashlib.md5(config.prompt.encode()).hexdigest()[:8]
        
        for i, image_data in enumerate(images):
            suffix = f"_v{i+1}" if len(images) > 1 else ""
            filename = f"{config.output_prefix}_{timestamp}_{prompt_hash}{suffix}.png"
            filepath = config.output_dir / filename
            
            if config.response_format == "b64_json":
                # Decode base64 image
                image_bytes = base64.b64decode(image_data.get("b64_json", ""))
            else:
                # Download from URL
                url = image_data.get("url", "")
                with urllib.request.urlopen(url) as resp:
                    image_bytes = resp.read()
            
            # Save image
            with open(filepath, "wb") as f:
                f.write(image_bytes)
            
            print(f"Saved: {filepath}")
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
                "generated_at": datetime.utcnow().isoformat() + "Z",
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
                       choices=["square", "portrait", "landscape", "wide", "tall"],
                       help="Aspect ratio (default: landscape)")
    parser.add_argument("--quality", "-q", type=str, default="hd",
                       choices=["standard", "hd"],
                       help="Image quality (default: hd)")
    parser.add_argument("--variations", "-n", type=int, default=1,
                       help="Number of variations to generate (default: 1)")
    parser.add_argument("--style", "-s", type=str, default="vivid",
                       choices=["vivid", "natural"],
                       help="Image style (default: vivid)")
    
    # Enhancement options
    parser.add_argument("--enhance", "-e", action="store_true",
                       help="Enhance prompt with best practices")
    parser.add_argument("--style-hint", type=str, default=None,
                       choices=["technical", "fun", "professional"],
                       help="Style hint for prompt enhancement")
    
    # Retry options
    parser.add_argument("--max-retries", type=int, default=3,
                       help="Maximum retry attempts (default: 3)")
    parser.add_argument("--timeout", type=int, default=120,
                       help="Request timeout in seconds (default: 120)")
    
    # Git options
    parser.add_argument("--no-git", action="store_true",
                       help="Don't add generated images to git")
    
    # Utility options
    parser.add_argument("--guidelines", action="store_true",
                       help="Print prompting guidelines and exit")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be generated without making API calls")
    
    return parser


async def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.guidelines:
        print(PROMPT_GUIDELINES)
        return 0
    
    # Collect prompts
    prompts = []
    if args.prompt:
        prompts.append(args.prompt)
    elif args.prompt_file:
        with open(args.prompt_file) as f:
            prompts = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    # Enhance prompts if requested
    if args.enhance:
        prompts = [enhance_prompt(p, args.style_hint) for p in prompts]
    
    # Map aspect ratio
    aspect_map = {
        "square": AspectRatio.SQUARE,
        "portrait": AspectRatio.PORTRAIT,
        "landscape": AspectRatio.LANDSCAPE,
        "wide": AspectRatio.WIDE,
        "tall": AspectRatio.TALL,
    }
    
    # Map quality
    quality_map = {
        "standard": Quality.STANDARD,
        "hd": Quality.HD,
    }
    
    if args.dry_run:
        print("DRY RUN - Would generate the following:")
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}] Prompt: {prompt}")
            print(f"    Aspect: {args.aspect} ({aspect_map[args.aspect].size})")
            print(f"    Quality: {args.quality}")
            print(f"    Variations: {args.variations}")
            print(f"    Style: {args.style}")
            print(f"    Output dir: {args.output_dir}")
        return 0
    
    # Initialize client
    try:
        client = GPTImageClient()
    except EnvironmentError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    # Generate images
    all_results = []
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{'='*60}")
        print(f"Generating {i}/{len(prompts)}: {prompt[:50]}...")
        print(f"{'='*60}")
        
        config = GenerationConfig(
            prompt=prompt,
            aspect_ratio=aspect_map[args.aspect],
            quality=quality_map[args.quality],
            n_variations=args.variations,
            output_dir=args.output_dir,
            output_prefix=args.output.stem if args.output else "image",
            style=args.style,
            max_retries=args.max_retries,
            timeout_seconds=args.timeout,
            add_to_git=not args.no_git,
        )
        
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
    
    # Summary
    successful = sum(1 for r in all_results if r.success)
    print(f"\n{'='*60}")
    print(f"Summary: {successful}/{len(all_results)} prompts succeeded")
    print(f"{'='*60}")
    
    return 0 if all(r.success for r in all_results) else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
