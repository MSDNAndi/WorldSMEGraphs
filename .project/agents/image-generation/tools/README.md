# GPT Image 1.5 Generation Tool

> **Version**: 2.1.0  
> **Created**: 2026-01-04  
> **Updated**: 2026-01-09  
> **Author**: WorldSMEGraphs Image Generation Agent

A robust Python tool for generating images using GPT Image 1.5 via Azure AI Foundry.

## Features (v2.1)

- ✅ **PARALLEL Generation**: Generate multiple images concurrently (respects rate limits)
- ✅ **LINEAR Backoff**: Smart linear backoff (not exponential) when rate limited
- ✅ **Rate Limit Tracking**: Observed limits stored in `rate-limits.yaml`
- ✅ **Super Explicit Prompts**: Comprehensive prompt enhancement based on OpenAI guide
- ✅ **Async Generation**: Handles long-running operations gracefully with polling
- ✅ **Automatic Retry**: Linear backoff retry logic for reliability
- ✅ **Multiple Variations**: Generate multiple image variations in one call
- ✅ **Auto Git Tracking**: Automatically adds generated images to source control
- ✅ **Comprehensive Logging**: Detailed output for debugging and monitoring
- ✅ **Multi-Panel Prompt Parsing** (NEW in v2.1): Automatic parsing of `=== PANEL XX ===` delimiters

## What's New in v2.1 (PR #42 Fixes)

### Multi-Panel Prompt File Support

The tool now automatically detects and parses multi-panel prompt files:

**Format**:
```text
=== PANEL 01: First Scene ===

[Your complete 8K+ character prompt here]
All the details, colors, positioning...

=== PANEL 02: Second Scene ===

[Your complete 8K+ character prompt here]
...
```

**Benefits**:
- Each panel's prompt can be multi-line (8K-20K characters)
- Panel numbers are extracted for proper output file naming (`image_001_*`, `image_002_*`, etc.)
- No need to split prompts into separate files for each panel

**Usage**:
```bash
python gpt_image_generator.py --prompt-file prompts-all-panels.txt --output-dir panels/ --parallel 5
```

**Detection**: The tool auto-detects the format based on `=== PANEL XX ===` pattern. Falls back to single-line prompts if no delimiters found.

## Prerequisites

### Environment Variables

The following GitHub environment secrets must be configured:

| Secret Name | Description |
|-------------|-------------|
| `AI_FOUNDRY_API_KEY` | API key for Azure AI Foundry |
| `AI_FOUNDRY_ENDPOINT` | Base endpoint URL for Azure AI Foundry |
| `GPT_IMAGE_1DOT5_ENDPOINT_URL` | Specific endpoint for GPT Image 1.5 model |

### Python Requirements

- Python 3.8+
- Standard library only (no external dependencies)
- Optional: PyYAML for rate limit config loading

## Usage

### Basic Usage

```bash
# Generate a single image
python gpt_image_generator.py --prompt "A beautiful sunset over mountains"

# Generate with specific aspect ratio
python gpt_image_generator.py --prompt "Technical diagram" --aspect landscape

# Generate multiple variations
python gpt_image_generator.py --prompt "Abstract art" --variations 3

# Generate from a file of prompts
python gpt_image_generator.py --prompt-file prompts.txt --output-dir ./images/
```

### PARALLEL Generation (NEW in v2.0)

```bash
# Generate multiple images IN PARALLEL (recommended for batches)
python gpt_image_generator.py --prompt-file prompts.txt --parallel 5

# Force sequential generation
python gpt_image_generator.py --prompt-file prompts.txt --sequential
```

### Rate Limit Management

```bash
# Show current rate limit configuration
python gpt_image_generator.py --show-rate-limits

# Show comprehensive prompting guidelines
python gpt_image_generator.py --guidelines
```

### Command Line Options

```
Required (one of):
  --prompt, -p          Image generation prompt
  --prompt-file, -f     File containing prompts (one per line)

Output Options:
  --output, -o          Output file path or prefix
  --output-dir, -d      Output directory (default: ./generated_images)

Generation Options:
  --aspect, -a          Aspect ratio: square|portrait|landscape|auto
  --quality, -q         Image quality: low|medium|high|auto
  --variations, -n      Number of variations (default: 1)
  --format              Output format: png|jpeg|webp

PARALLEL Options (NEW):
  --parallel            Max concurrent requests (default: from rate-limits.yaml)
  --sequential          Force sequential generation (one at a time)

Enhancement Options:
  --enhance, -e         Enhance prompt with best practices (RECOMMENDED)
  --style-hint          Style hint: technical|fun|professional|scientific

Reliability Options:
  --max-retries         Maximum retry attempts with LINEAR backoff (default: 5)
  --timeout             Request timeout in seconds (default: 180)

Other Options:
  --no-git              Don't add generated images to git
  --guidelines          Print comprehensive prompting guidelines and exit
  --show-rate-limits    Show current rate limit configuration
  --dry-run             Show what would be generated without API calls
```

## Supported Resolutions

GPT Image 1.5 supports the following resolutions:

| Aspect Ratio | Resolution | Use Case |
|--------------|------------|----------|
| `square` | 1024×1024 | Social media, icons |
| `portrait` | 1024×1536 | Phone wallpapers, stories (2:3) |
| `landscape` | 1536×1024 | Presentations, banners (3:2) |

## Prompting Best Practices

### BE SUPER EXPLICIT

The model has world knowledge but needs **explicit instructions** for domain-specific accuracy.

❌ **BAD - VAGUE:**
```
blood vessels with blood flow
```

✅ **GOOD - SUPER EXPLICIT:**
```
blood vessels showing red oxygenated blood flowing FROM the heart 
through arteries (arrows pointing AWAY from center), and blue 
deoxygenated blood flowing TOWARD the heart through veins 
(arrows pointing TOWARD center)
```

### Use Structured Prompts

```
Create [TYPE OF IMAGE].

Scene:
[Detailed description with explicit positions and directions]

Style:
[Visual style, lighting, mood - be specific]

Constraints:
- Original artwork only
- No watermarks or logos
```

### Specify Visual Style

- **Photography**: "photorealistic", "35mm film", "cinematic"
- **Illustration**: "digital illustration", "watercolor", "vector art"
- **Technical**: "technical diagram", "infographic", "flowchart"
- **Corporate**: "clean corporate style", "professional presentation"

## Rate Limit Configuration

Rate limits are configured in `../rate-limits.yaml`:

```yaml
backoff:
  type: "linear"              # NOT exponential
  base_delay_seconds: 5       # Initial delay
  linear_increment_seconds: 5 # Delay increase per retry
  max_delay_seconds: 60       # Cap on delay
  max_retries: 5

api_limits:
  concurrent_requests:
    safe_target: 5            # Max parallel requests
```

## Output Files

The tool generates:

1. **Image files**: `{prefix}_{timestamp}_{hash}_v{n}.png`
2. **Metadata files**: `metadata_{timestamp}_{hash}.json`

Metadata includes:
- Original prompt
- Generation settings
- Timestamp
- API response data
- Rate limit events (if any)

## Error Handling

The tool handles common errors:

| Error | Handling |
|-------|----------|
| Rate limiting (429) | LINEAR backoff retry (not exponential) |
| Timeout | Retry with same request |
| Network errors | Retry with backoff |
| Invalid prompt | Return error message |
| Missing secrets | Clear error message listing missing vars |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-09 | Multi-panel prompt parsing (`=== PANEL XX ===` delimiters), panel number extraction for output naming |
| 2.0.0 | 2026-01-04 | PARALLEL generation, LINEAR backoff, rate tracking, super explicit prompts |
| 1.0.0 | 2026-01-04 | Initial release |

---

## Workflow Enforcement Tools (v1.0.0)

> **Added**: 2026-01-08  
> **Purpose**: Enforce correct workflow order for image generation and content creation  
> **Based on**: PR #36 and PR #38 learnings

### New Tools for Workflow Validation

#### 1. validate_workflow.py
**Size**: 13KB  
**Purpose**: Validate phase order and completeness

Checks that content follows correct workflow:
- ✅ Storyboard exists (Phase 1-2)
- ✅ Prompts complete (Phase 3)
- ✅ Images generated (Phase 4)
- ✅ Documents only after images (Phase 5)

```bash
# Validate current directory
python validate_workflow.py

# Validate specific directory
python validate_workflow.py renders/by-domain/.../presentations/

# Verbose with warnings
python validate_workflow.py --verbose

# JSON output
python validate_workflow.py --json
```

#### 2. validate_prompts.py
**Size**: 15KB  
**Purpose**: Validate prompt quality

Checks prompt completeness:
- ✅ Length (target 8K-20K chars)
- ✅ No placeholders
- ✅ No external references
- ✅ Super explicit details

```bash
# Validate prompts
python validate_prompts.py prompts/

# With quality threshold
python validate_prompts.py prompts/ --min-score 70
```

#### 3. pre-commit-hook.sh
**Size**: 5KB  
**Purpose**: Prevent workflow violations in commits

Install:
```bash
cp pre-commit-hook.sh ../../../.git/hooks/pre-commit
chmod +x ../../../.git/hooks/pre-commit
```

### Workflow Documentation

See [WORKFLOW-ENFORCEMENT.md](../WORKFLOW-ENFORCEMENT.md) (20KB) for complete guide including:
- Phase-by-phase workflow
- Validation requirements
- Archive management
- Common mistakes
- Examples and checklists

### Correct Workflow Order

**Phase 1-2**: Storyboard → **Phase 3**: Prompts → **Phase 4**: Images → **Phase 5**: Documents

**Critical Rule**: Images MUST be generated BEFORE creating final documents (PDF, PPTX, HTML).

### Quick Reference

| Task | Tool |
|------|------|
| Generate images | gpt_image_generator.py |
| Validate workflow | validate_workflow.py |
| Validate prompts | validate_prompts.py |
| Prevent bad commits | pre-commit-hook.sh |
| Create presentations | presentation_generator.py (updated with validation) |
| Read full guide | WORKFLOW-ENFORCEMENT.md |

