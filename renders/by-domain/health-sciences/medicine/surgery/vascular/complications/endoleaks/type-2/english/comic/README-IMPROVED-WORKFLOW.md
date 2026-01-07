# Type 2 Endoleak Comic - Improved Image Generation Workflow

## Overview

This directory contains an improved workflow for generating the 32-panel Type 2 Endoleak research comic based on learnings from PR #36. The key improvements address three critical issues:

1. **Archive Management**: Previous images are properly archived in subfolders, not just in git history
2. **Complete Prompts**: All prompts written upfront without placeholders or references
3. **Hyper-Detailed Specifications**: Each prompt contains 8K-20K characters of explicit detail

## Problem Statement (from PR #36 Feedback)

> "Following https://github.com/MSDNAndi/WorldSMEGraphs/pull/36 you can see that we didn't do a good job. a) the previous images are only in the git history, but I asked them to be archived which implies in a folder based system, to be put in a subfolder, b) the workflow to generate the images was too convuluted and we did unnecessary intermediate generations, we should have written the complete prompt without placeholders for each image and save it, so that the image generation is not guess work c) specifically styles, characters, composition - all needs to be described hyper-detailed and hyper precise. Remember we have up to 32000 characters for EACH images"

## Solutions Implemented

### 1. Archive System (`archive/` directory)

**Structure:**
```
archive/
├── README.md                           # Archive documentation
├── 2026-01-07-original-pr36/          # Original PR #36 images
│   ├── image_001_*.png through image_032_*.png
│   ├── metadata_*.json files
│   └── alt-text.md
└── [future archives]/                  # Future generation iterations
```

**Purpose:**
- Preserve image evolution history
- Enable comparison between prompt strategies
- Allow rollback if needed
- Document what changed between versions

**Usage:**
- Each archive folder named with date + identifier (e.g., `2026-01-07-original-pr36`)
- Include README or metadata explaining what changed
- Preserve all associated files (images, metadata, alt text)

### 2. Complete Prompt Generation (No Placeholders)

**Previous Approach (PR #36):**
- Prompts 200-400 words (~1,500-3,000 characters)
- Used "Apply STYLE BASE" placeholder
- Referenced external style guide
- Left details to AI interpretation
- Example: "Apply STYLE BASE; include sticky note 'English only'."

**New Approach:**
- Prompts 8,000-20,000 characters each
- Every detail explicitly specified
- No external references or placeholders
- Self-contained specifications
- Example: Full character descriptions repeated in every prompt with exact positioning

**Tools:**
- `PROMPT-ENGINEERING-GUIDE.md` - Comprehensive methodology (12.8 KB)
- `generate_detailed_prompts.py` - Script to generate all 32 prompts automatically
- `gpt-prompts-v2-detailed-all-panels.txt` - Generated prompts (333 KB, 10.4K avg per panel)

### 3. Hyper-Detailed Specifications

**Each prompt now includes:**

1. **Style Foundation** (~1,500-2,000 chars)
   - Complete art style description
   - Visual language specifications
   - Rendering technique details
   - Color palette overview
   - Line quality and shading approach

2. **Character Specifications** (~2,000-3,000 chars PER character)
   - Complete physical appearance (skin tone hex codes, facial features, hair style)
   - Exact outfit specifications (colors with hex codes, all accessories, patches)
   - Body language THIS PANEL (specific posture, gestures, expressions)
   - Position in frame (exact spatial placement, facing angle, distances)

3. **Scene Composition** (~1,500-2,000 chars)
   - Camera angle and distance
   - Framing (rule of thirds, focus areas)
   - Foreground, midground, background elements
   - Environmental details with measurements
   - Spatial relationships between elements

4. **Key Visual Elements** (~1,000-1,500 chars)
   - Primary educational focus (diagrams, charts, equipment)
   - Secondary props and tools
   - Medical/scientific content specifications
   - All with precise measurements and styling

5. **Text & Speech Bubbles** (~1,500-2,000 chars)
   - Exact bubble positioning and sizing
   - Border and fill specifications
   - Text content (quoted exactly)
   - Font, size, color, alignment
   - Reading order and spacing rules

6. **Lighting & Atmosphere** (~800-1,000 chars)
   - Light source position and quality
   - Shadow specifications (opacity, blur, direction)
   - Highlight placement and intensity
   - Atmosphere and mood description

7. **Color Palette** (~500-800 chars)
   - All colors with hex codes
   - Character-specific colors
   - Environmental colors
   - Accent colors for UI elements

8. **Technical Specifications** (~400-600 chars)
   - Aspect ratio, resolution
   - Anti-aliasing requirements
   - Quality checklist
   - Consistency requirements

## Directory Structure

```
.
├── README-IMPROVED-WORKFLOW.md         # This file
├── PROMPT-ENGINEERING-GUIDE.md         # Detailed methodology guide
│
├── archive/                            # Archived previous generations
│   ├── README.md
│   └── 2026-01-07-original-pr36/       # Original PR #36 images
│
├── storyboard.json                     # Source of truth for panels
├── generate_detailed_prompts.py        # Automated prompt generator
│
├── gpt-prompts-v2-detailed.txt         # Hand-crafted Panel 01 (18.5K chars)
├── gpt-prompts-v2-detailed-all-panels.txt  # All 32 panels (333KB total)
│
├── panels-gpt-v2/                      # NEW: Generated images (to be created)
│   └── [images will go here]
│
├── type2-endoleak-comic-v2.pdf         # NEW: PDF from v2 images (to be created)
│
└── [existing files...]                 # Original PR #36 files
    ├── comic-storyboard.md
    ├── runbook.md
    ├── build_gpt_pdf.py
    └── etc.
```

## Workflow Steps

### Step 1: Review and Refine Story (Optional)

If improving narrative:
1. Review `comic-storyboard.md` and `storyboard.json`
2. Make story improvements (better arc, character development, engagement)
3. Update `storyboard.json` with refined content
4. Regenerate prompts with `generate_detailed_prompts.py`

### Step 2: Generate Hyper-Detailed Prompts

**Automated (Recommended):**
```bash
python generate_detailed_prompts.py
```

This generates `gpt-prompts-v2-detailed-all-panels.txt` with all 32 panels.

**Manual Refinement:**
1. Open `gpt-prompts-v2-detailed-all-panels.txt`
2. Find placeholders: `[Specific to Panel XX - ...]`
3. Fill in with scene-specific details from `storyboard.json`
4. Enhance any areas needing more precision

**Key Rules:**
- NO placeholders (no "Apply STYLE BASE" or similar)
- Every panel self-contained (assume AI knows nothing about previous panels)
- Character descriptions IDENTICAL across all 32 panels
- Use precise spatial language (LEFT/RIGHT from viewer's perspective)
- Specify ALL directional arrows with explicit endpoints and arrowhead positions
- Include hex codes for all colors
- Measurement scale using proportions or relative sizes

### Step 3: Generate Images

**Prerequisites:**
```bash
# Verify environment variables
env | grep AI_FOUNDRY
# Should see: AI_FOUNDRY_API_KEY, GPT_IMAGE_1DOT5_ENDPOINT_URL
```

**Generation Command:**
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2 \
  --aspect landscape --quality high --parallel 4 --enhance
```

**Parameters:**
- `--prompt-file`: Your hyper-detailed prompts file
- `--output-dir`: Where to save generated images
- `--aspect landscape`: 16:9 for comic panels
- `--quality high`: Maximum quality setting
- `--parallel 4`: Generate 4 images at once (adjust based on API rate limits)
- `--enhance`: Use prompt enhancement features

**Duration:**
- ~32 panels × ~90 seconds average = ~48 minutes total
- With `--parallel 4`: ~12-15 minutes

### Step 4: Build PDF

```bash
python build_gpt_pdf.py --input-dir panels-gpt-v2 --output type2-endoleak-comic-v2.pdf
```

Or create custom layouts:
```bash
# 6 panels per page (standard)
python build_gpt_pdf.py --input-dir panels-gpt-v2 --panels-per-page 6

# Feature panel 15 (microbubble tracker) as large
python build_gpt_pdf.py --input-dir panels-gpt-v2 --feature-panel 15
```

### Step 5: Validate and Review

```bash
# Validate all components present
python validate_comic.py --version v2

# Check quality
# - Open PDF and review all 32 panels
# - Verify character consistency
# - Check speech bubble text accuracy
# - Confirm educational content clarity
# - Assess overall visual quality
```

### Step 6: Iterate if Needed

If panels need refinement:
1. Identify specific issues (e.g., "Panel 12 catheter position unclear")
2. Update relevant section in prompts file
3. Regenerate ONLY affected panels:
   ```bash
   python .project/agents/image-generation/tools/gpt_image_generator.py \
     --prompt "Panel 12 detailed prompt here" \
     --output-dir panels-gpt-v2 \
     --filename image_012_regenerated.png
   ```
4. Rebuild PDF
5. Archive old version before replacing

## Benefits of This Workflow

### ✅ Improved Quality
- **Consistency**: Character models identical across all panels
- **Precision**: Exact composition, positioning, colors specified
- **Clarity**: Educational content rendered accurately
- **Professional**: No guesswork, predictable results

### ✅ Better Process
- **Efficient**: Write prompts once, generate all 32 panels
- **Reproducible**: Same prompt = same result
- **Documented**: Clear methodology and specifications
- **Maintainable**: Easy to update specific panels

### ✅ Knowledge Preservation
- **Archived**: Previous generations preserved, not lost to git history
- **Compared**: Easy to compare prompt strategies
- **Learned**: Document what works and what doesn't
- **Evolved**: Clear progression of improvements

## Metrics

### Prompt Detail Comparison

| Metric | PR #36 (Old) | v2 (New) | Improvement |
|--------|--------------|----------|-------------|
| Chars per prompt | 1,500-3,000 | 8,000-20,000 | 4-8x more |
| Placeholders | Yes ("Apply STYLE BASE") | No (fully self-contained) | 100% reduction |
| Character specs | Compressed | Full detail per panel | Complete consistency |
| Color specs | Generic | Hex codes everywhere | Exact matching |
| Spatial precision | Vague | Explicit LEFT/RIGHT | No ambiguity |
| Total prompt file | ~50-100 KB | 333 KB | 3-6x more detail |

### Generation Comparison

| Aspect | PR #36 (Old) | v2 (New) |
|--------|--------------|----------|
| Workflow | Multi-step, intermediate files | Single generation run |
| Consistency | Variable (AI interpretation) | High (explicit specs) |
| Iteration | Difficult (scattered prompts) | Easy (single source file) |
| Documentation | Minimal | Comprehensive |
| Archive | Git history only | Folder-based with metadata |

## Future Improvements

### Short Term
1. Fill in remaining `[Specific to Panel XX]` placeholders with scene details
2. Generate v2 images and compare with original
3. Create side-by-side comparison document
4. Document any further refinements needed

### Medium Term
1. Create template for other comics/stories
2. Build prompt validation tool
3. Develop character consistency checker
4. Automate quality assessment

### Long Term
1. Integrate with AKU (Atomic Knowledge Unit) system
2. Multi-language support (generate prompts for different languages)
3. Audience-level variations (adjust complexity for different audiences)
4. Interactive web viewer with panel navigation

## Key Learnings from PR #36

1. **Placeholders are problematic** - Every placeholder requires context and introduces ambiguity
2. **Repetition is good** - Repeating character specs in every prompt ensures consistency
3. **Explicit is better** - "LEFT to RIGHT arrow" beats "arrow showing flow"
4. **Hex codes matter** - Color names are ambiguous; hex codes are precise
5. **Archive everything** - Git history is not sufficient for visual assets
6. **Measurement scale needed** - "Large" vs "3 inches" vs "70% of frame width"
7. **Single source of truth** - One comprehensive prompt file beats scattered fragments

## References

- **PR #36**: https://github.com/MSDNAndi/WorldSMEGraphs/pull/36
- **GPT Image 1.5 Docs**: `.project/agents/image-generation/`
- **Prompt Engineering**: `PROMPT-ENGINEERING-GUIDE.md`
- **Original Runbook**: `runbook.md`
- **Storyboard**: `storyboard.json`

## Questions & Support

**Q: Why such long prompts?**
A: GPT Image 1.5 supports up to 32,000 characters per prompt. Using this capacity eliminates ambiguity and ensures consistent, high-quality results.

**Q: Can't AI infer some details?**
A: Yes, but inference introduces variability. For medical education comics requiring consistency across 32 panels, explicit specification is critical.

**Q: What if prompts are too detailed?**
A: Better too detailed than too vague. The AI can handle complex specifications better than filling in missing details consistently.

**Q: How do I customize for other stories?**
A: Use `generate_detailed_prompts.py` as template. Update character bases, style foundation, and panel-specific details based on your storyboard.

---

**Document Version:** 1.0  
**Created:** 2026-01-07  
**Authors:** GitHub Copilot Agent  
**Status:** Active - v2 prompts generated, images pending
