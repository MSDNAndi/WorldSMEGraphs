# Archive - Type 2 Endoleak Comic Image Generations

This directory contains archived versions of generated comic images from various iterations.

## Purpose

As we refine prompts and regenerate images, we archive previous versions here to:
- Maintain a history of image evolution
- Allow comparison between prompt strategies
- Preserve work for future reference
- Avoid losing previous generations to git history only

## Archive Structure

Each subdirectory represents a generation batch:

### 2026-01-07-original-pr36
- **Date**: Original from PR #36 (generated ~2026-01-06)
- **Prompt Style**: Short-form, STYLE BASE reference pattern
- **Issue**: Prompts were too brief, used placeholder references, lacked hyper-detailed specifications
- **Contents**: 
  - 32 GPT-generated images (image_001-032, 032xxx timestamps) in root
  - 32 placeholder images (panel-01 through panel-32) in panels-placeholder/
  - Associated metadata JSON files
  - Alt-text documentation
- **Total**: 64 images + metadata
- **Characteristics**: 
  - GPT images: Prompts ~200-400 words each, used "Apply STYLE BASE" shorthand
  - Placeholder images: Python-generated simple colored backgrounds with text

## Current Working Images (Not Archived)

The parent `comic/` directory contains active/current versions:
- **panels-gpt-v2/** - Latest generation (051xxx timestamps) using hyper-detailed prompts (8-20K chars each)
- **type2-endoleak-comic-gpt.pdf** - Compiled PDF from v2 images
- **type2-endoleak-comic-gpt-featured.pdf** - Featured version

## Next Iterations

Future archives should include:
- Timestamp/version identifier in folder name
- README or metadata file explaining what changed
- Comparison notes (what worked, what didn't)
- Prompt file used for generation

---

**Last Updated**: 2026-01-07 (removed duplicate 03-56-panels-gpt archive, consolidated to original-pr36)
