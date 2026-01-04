# GPT Image 1.5 Generation Tool

> **Version**: 1.0.0  
> **Created**: 2026-01-04  
> **Author**: WorldSMEGraphs Image Generation Agent

A robust Python tool for generating images using GPT Image 1.5 via Azure AI Foundry.

## Features

- ✅ **Async Generation**: Handles long-running operations gracefully with polling
- ✅ **Automatic Retry**: Exponential backoff retry logic for reliability
- ✅ **Multiple Variations**: Generate multiple image variations in one call
- ✅ **Auto Git Tracking**: Automatically adds generated images to source control
- ✅ **Prompt Enhancement**: Built-in prompt optimization for better results
- ✅ **Comprehensive Logging**: Detailed output for debugging and monitoring

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

### Command Line Options

```
Required (one of):
  --prompt, -p          Image generation prompt
  --prompt-file, -f     File containing prompts (one per line)

Output Options:
  --output, -o          Output file path or prefix
  --output-dir, -d      Output directory (default: ./generated_images)

Generation Options:
  --aspect, -a          Aspect ratio: square|portrait|landscape|wide|tall
  --quality, -q         Image quality: standard|hd
  --variations, -n      Number of variations (default: 1)
  --style, -s           Image style: vivid|natural

Enhancement Options:
  --enhance, -e         Enhance prompt with best practices
  --style-hint          Style hint: technical|fun|professional

Reliability Options:
  --max-retries         Maximum retry attempts (default: 3)
  --timeout             Request timeout in seconds (default: 120)

Other Options:
  --no-git              Don't add generated images to git
  --guidelines          Print prompting guidelines and exit
  --dry-run             Show what would be generated without API calls
```

## Supported Resolutions

GPT Image 1.5 supports the following resolutions:

| Aspect Ratio | Resolution | Use Case |
|--------------|------------|----------|
| `square` | 1024×1024 | Social media, icons |
| `portrait` | 1024×1792 | Phone wallpapers, stories |
| `landscape` | 1792×1024 | Presentations, banners |
| `wide` | 1536×1024 | Wide banners (3:2) |
| `tall` | 1024×1536 | Tall graphics (2:3) |

## Prompting Best Practices

### 1. Be Specific and Detailed

```
# Bad
"a cat"

# Good
"A fluffy orange tabby cat sitting on a windowsill, soft afternoon 
sunlight streaming through, cozy home interior, photorealistic"
```

### 2. Specify Visual Style

- **Photography**: "photorealistic", "35mm film", "cinematic"
- **Illustration**: "digital illustration", "watercolor", "vector art"
- **Technical**: "technical diagram", "infographic", "flowchart"

### 3. Describe Composition

- **Camera angle**: "bird's eye view", "low angle", "close-up"
- **Layout**: "centered composition", "rule of thirds", "symmetrical"

### 4. Include Lighting

- "soft diffused lighting", "dramatic shadows", "golden hour"
- "studio lighting", "natural daylight", "neon lights"

### 5. Avoid Negatives

Instead of "no people", describe what you DO want.

### 6. For Technical Diagrams

```
"Clean technical illustration showing [concept], minimal design, 
professional corporate color palette (blues and grays), 
clean lines, no text, suitable for presentation slide"
```

### 7. For Presentation Slides

```
"Abstract background suitable for presentation slide, 
[color palette] gradient, subtle geometric patterns, 
professional corporate style, clean and modern"
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

## Error Handling

The tool handles common errors:

| Error | Handling |
|-------|----------|
| Rate limiting | Exponential backoff retry |
| Timeout | Retry with same request |
| Network errors | Retry with backoff |
| Invalid prompt | Return error message |
| Missing secrets | Clear error message listing missing vars |

## Integration with WorldSMEGraphs

### In Workflows

```yaml
- name: Generate Presentation Images
  env:
    AI_FOUNDRY_API_KEY: ${{ secrets.AI_FOUNDRY_API_KEY }}
    AI_FOUNDRY_ENDPOINT: ${{ secrets.AI_FOUNDRY_ENDPOINT }}
    GPT_IMAGE_1DOT5_ENDPOINT_URL: ${{ secrets.GPT_IMAGE_1DOT5_ENDPOINT_URL }}
  run: |
    python .project/agents/image-generation/tools/gpt_image_generator.py \
      --prompt-file presentation_prompts.txt \
      --output-dir ./domain/presentations/images/ \
      --aspect landscape \
      --quality hd
```

### In Python Scripts

```python
import asyncio
from gpt_image_generator import GPTImageClient, GenerationConfig, AspectRatio, Quality

async def generate_presentation_image():
    client = GPTImageClient()
    
    config = GenerationConfig(
        prompt="Abstract technology background with neural network visualization",
        aspect_ratio=AspectRatio.LANDSCAPE,
        quality=Quality.HD,
        n_variations=2,
        output_dir=Path("./images"),
        add_to_git=True
    )
    
    result = await client.generate_image(config)
    
    if result.success:
        print(f"Generated: {result.file_paths}")
    else:
        print(f"Error: {result.error_message}")

asyncio.run(generate_presentation_image())
```

## Troubleshooting

### "Missing environment variables" error

Ensure all three secrets are configured in your GitHub environment.

### "HTTP 429" (Rate Limited)

The tool will automatically retry with exponential backoff. If it persists, wait a few minutes.

### "Timeout" errors

Increase the `--timeout` value. Image generation can take up to 60 seconds.

### Images look different than expected

1. Use `--enhance` flag to apply best practices
2. Be more specific in your prompt
3. Try `--style natural` for more realistic results

## Related Resources

- [OpenAI Image Generation Documentation](https://platform.openai.com/docs/api-reference/images)
- [GPT Image 1.5 Prompting Guide](https://cookbook.openai.com/examples/multimodal/image-gen-1.5-prompting_guide)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-04 | Initial release |
