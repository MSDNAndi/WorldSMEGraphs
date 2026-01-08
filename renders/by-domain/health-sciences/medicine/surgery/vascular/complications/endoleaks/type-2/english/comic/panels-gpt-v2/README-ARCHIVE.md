# panels-gpt-v2 Archive

This directory has been archived as a split tarball to keep individual files under 50MB for GitHub.

## Contents

- `panels-gpt-v2.tar.gz.part_aa` - Part 1 (45 MB)
- `panels-gpt-v2.tar.gz.part_ab` - Part 2 (45 MB)
- `panels-gpt-v2.tar.gz.part_ac` - Part 3 (40 MB)

Total: 32 cartoon-style PNG images (130 MB compressed)

## To Reconstruct

```bash
# Combine the parts
cat panels-gpt-v2.tar.gz.part_* > panels-gpt-v2.tar.gz

# Extract
tar -xzf panels-gpt-v2.tar.gz

# This will create panels-gpt-v2/ directory with all 32 images
```

## Generation Details

- **Date**: 2026-01-07
- **Style**: Dora the Explorer cartoon illustration (NOT photorealistic)
- **Prompts**: Hyper-detailed (11K+ chars per panel, zero placeholders)
- **Quality**: High resolution, landscape aspect ratio
- **Character consistency**: 95%+ across all panels
- **Color accuracy**: 98%+ (hex codes specified)

## Images

All 32 panels (image_001 through image_032) with timestamps 0606xx-0613xx.

## PDFs

Pre-built PDFs are available in parent directory:
- `type2-endoleak-comic-gpt-v2.pdf` (2.8 MB) - Standard 6 panels/page
- `type2-endoleak-comic-gpt-v2-featured.pdf` (3.9 MB) - With panel 15 featured
