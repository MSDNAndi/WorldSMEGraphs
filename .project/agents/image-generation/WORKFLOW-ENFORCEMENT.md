# Image Generation Workflow Enforcement

> **Critical Rule**: Visual assets MUST be created BEFORE final render documents.
> 
> **Version**: 1.0.0  
> **Created**: 2026-01-08  
> **Purpose**: Enforce correct workflow order learned from PR #36 and PR #38

## Problem Statement

From PR #36 feedback and PR #38 improvements, we identified three critical issues:

1. **Archive Management**: Previous images only in git history, not in subfolders
2. **Incomplete Prompts**: Used placeholders and external references instead of complete self-contained prompts
3. **Wrong Order**: Generated images during or after document creation instead of before

## The Correct Workflow Order

### Phase 1: Content Planning
**Input**: Educational objectives, domain knowledge, target audience
**Output**: Content structure and learning flow

**Steps**:
1. Define learning objectives
2. Identify key concepts to visualize
3. Determine narrative flow
4. Create content outline

**Validation**: ✅ Content outline reviewed and approved

---

### Phase 2: Storyboard Creation
**Input**: Content outline
**Output**: Complete storyboard with scene descriptions

**Steps**:
1. Break content into scenes/slides/panels
2. Describe each visual scene in detail
3. Define transitions and flow
4. Document educational purpose of each visual
5. Create storyboard file (JSON, YAML, or Markdown)

**Validation**: ✅ Storyboard file exists and is complete

**Example**:
```yaml
# presentation-storyboard.yaml
slides:
  - id: 1
    title: "Introduction to Functors"
    visual_description: |
      A transformation diagram showing input shapes morphing into output shapes,
      with arrows pointing LEFT TO RIGHT indicating the transformation direction.
    educational_purpose: "Illustrate the mapping concept"
    
  - id: 2
    title: "Functor Laws"
    visual_description: |
      Side-by-side comparison showing correct vs incorrect functor behavior...
```

---

### Phase 3: Prompt Engineering (SUPER EXPLICIT)
**Input**: Storyboard
**Output**: Complete, self-contained prompts for each image (8K-20K characters each)

**Steps**:
1. For each scene in storyboard, write COMPLETE prompt
2. Include ALL details explicitly (no placeholders, no external references)
3. Specify exact colors with hex codes
4. Describe orientations explicitly (LEFT TO RIGHT, clockwise, etc.)
5. Define composition, lighting, style completely
6. Save prompts to file (one file per scene or batch file)

**Requirements**:
- ❌ NO placeholders ("Apply STYLE BASE", "Use style from...")
- ❌ NO external references ("See style guide...")
- ❌ NO assumptions about what AI "knows"
- ✅ COMPLETE self-contained descriptions
- ✅ 8,000-20,000 characters per prompt
- ✅ Super explicit about directions and positions

**Validation**: 
- ✅ Prompt file(s) exist
- ✅ Each prompt is self-contained
- ✅ No placeholder text or external references
- ✅ Prompts meet minimum length requirements (suggest 5K+ chars)

**Tools**:
- `.project/agents/image-generation/tools/validate_prompts.py` (to be created)
- Manual review against checklist

**Example**:
```text
# prompt-slide-01.txt

Create a technical illustration showing the concept of functor transformation.

SCENE COMPOSITION:
The image shows a transformation process flowing from LEFT to RIGHT across the canvas.
On the LEFT side (approximately 20% from left edge), place 3 geometric input shapes:
- Circle (diameter 80 pixels, filled with #3498DB blue, centered at x=15%, y=30%)
- Square (80x80 pixels, filled with #E74C3C red, centered at x=15%, y=50%)
- Triangle (equilateral, 80 pixel sides, filled with #2ECC71 green, centered at x=15%, y=70%)

In the CENTER (40-60% from left edge), show a transformation functor represented as:
- A rectangular box with rounded corners (200x400 pixels)
- Filled with semi-transparent gradient (#9B59B6 to #8E44AD, left to right)
- White border 3 pixels thick
- Inside the box: abstract code-like patterns (lines and dots, not actual text)

On the RIGHT side (approximately 80% from left edge), show transformed outputs:
- Transformed circle: Pentagon shape (diameter 90px, #5DADE2 light blue, x=85%, y=30%)
- Transformed square: Hexagon (90px across, #EC7063 light red, x=85%, y=50%)  
- Transformed triangle: Octagon (90px, #58D68D light green, x=85%, y=70%)

CONNECTION ARROWS:
Draw 3 flowing arrows connecting inputs to functor and functor to outputs:
- Each arrow is curved (smooth bezier), 5 pixels thick, white color with 80% opacity
- Arrow 1: from input circle TO functor box (points RIGHT, arrowhead on right end)
- Arrow 2: from input square TO functor box (points RIGHT)
- Arrow 3: from input triangle TO functor box (points RIGHT)
- Arrow 4: from functor box TO output pentagon (points RIGHT)
- Arrow 5: from functor box TO output hexagon (points RIGHT)
- Arrow 6: from functor box TO output octagon (points RIGHT)
All arrows point from LEFT TO RIGHT showing transformation flow direction.

STYLE:
Clean vector illustration style, modern tech aesthetic, professional but friendly.
Solid colors with subtle gradients, no textures.
Flat design with subtle shadows for depth (2px offset, 20% opacity black).

BACKGROUND:
Dark navy blue (#1A1A2E) solid color with subtle noise texture (5% opacity).

LIGHTING:
Soft ambient lighting from top-left (135° angle), no harsh shadows.
Slight glow effect around transformed shapes (10px blur, 30% opacity matching shape color).

COLOR PALETTE:
- Primary: #3498DB (blue)
- Secondary: #E74C3C (red)  
- Tertiary: #2ECC71 (green)
- Accent: #9B59B6 (purple)
- Background: #1A1A2E (dark navy)
- Text/Details: #FFFFFF (white)

CONSTRAINTS:
- NO text labels or annotations (will be added as overlay)
- NO human figures or faces
- NO copyrighted elements
- Original artwork only
- Landscape orientation (1536x1024 pixels)
- Professional presentation quality
- Family-friendly G-rated content

PURPOSE:
This image illustrates the concept of functors in functional programming - a structure-preserving
transformation that maps elements from one category to another while maintaining relationships.
The transformation functor in the center represents the mapping function.

[... Continue with more details totaling 8K-20K characters ...]
```

---

### Phase 4: Image Generation (PARALLEL)
**Input**: Complete prompts from Phase 3
**Output**: Generated images (.png files)

**Steps**:
1. Verify all prompts are complete (no placeholders)
2. Review prompts for super-explicit directions
3. Generate images using GPT Image 1.5
4. Use PARALLEL generation for efficiency
5. Save images with descriptive filenames
6. Create metadata files for each image
7. Review generated images for quality

**Tools**:
```bash
# Parallel generation (recommended)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all-slides.txt \
  --output-dir renders/.../images/ \
  --aspect landscape \
  --quality high \
  --parallel 5 \
  --enhance

# Single image
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "$(cat prompts/slide-01.txt)" \
  --output-dir renders/.../images/ \
  --aspect landscape \
  --quality high
```

**Validation**:
- ✅ All images generated successfully
- ✅ Image quality meets standards
- ✅ Images match prompt intentions
- ✅ All images saved with metadata
- ✅ Images archived properly

**Output Structure**:
```
renders/by-domain/{domain}/images/
├── slide_01_functors_20260108_123456_abc123.png
├── metadata_20260108_123456_abc123.json
├── slide_02_monads_20260108_123457_def456.png
├── metadata_20260108_123457_def456.json
└── ... (all images)
```

---

### Phase 5: Document Generation (FINAL)
**Input**: Generated images from Phase 4, content from Phase 1-2
**Output**: Final render documents (PDF, PPTX, HTML, Markdown)

**Prerequisites** (ENFORCED):
- ✅ All images exist and are validated
- ✅ Images are properly named and located
- ✅ Metadata files are present
- ✅ Image quality review completed

**Steps**:
1. **VALIDATE** that all required images exist (BLOCKING)
2. Assemble document structure
3. Insert pre-generated images
4. Add text content
5. Apply formatting and styling
6. Generate final output files

**Tools**:
```bash
# For presentations
python .project/agents/image-generation/tools/presentation_generator.py \
  --slides presentation-content.yaml \
  --images-dir renders/.../images/ \
  --output presentation.pptx

# The tool MUST check that all required images exist before proceeding
```

**Validation Enforcement**:
```python
# In presentation_generator.py or similar tools
def validate_images_exist(slides, images_dir):
    """
    BLOCKING validation: All images must exist before document generation.
    Raises FileNotFoundError if any image is missing.
    """
    missing = []
    for slide in slides:
        image_path = Path(images_dir) / slide['image_file']
        if not image_path.exists():
            missing.append(str(image_path))
    
    if missing:
        raise FileNotFoundError(
            f"Cannot generate document: {len(missing)} images missing.\n"
            f"You must generate images BEFORE creating final documents.\n"
            f"Missing files:\n" + "\n".join(missing)
        )
    
    return True
```

**Output Structure**:
```
renders/by-domain/{domain}/
├── images/                          # Phase 4 output (REQUIRED FIRST)
│   ├── slide_01_*.png
│   ├── slide_02_*.png
│   └── ...
├── presentation.pptx                # Phase 5 output (REQUIRES images)
├── presentation.pdf                 # Phase 5 output (REQUIRES images)
└── presentation-notes.md            # Phase 5 output (REQUIRES images)
```

---

## Phase 6: Archive Management
**Input**: New version of rendered content
**Output**: Properly archived previous versions

**Steps**:
1. Before overwriting, move previous version to archive/
2. Create dated archive folder (YYYY-MM-DD-description)
3. Move all related files (images, metadata, documents)
4. Create archive README documenting what changed
5. Update main README referencing archive

**Archive Structure**:
```
renders/by-domain/{domain}/archive/
├── README.md                        # Index of all archives
├── 2026-01-04-original-version/    # First version
│   ├── README.md                   # What this version was
│   ├── images/
│   ├── presentation.pptx
│   └── presentation.pdf
├── 2026-01-08-improved-prompts/    # Improved version
│   ├── README.md
│   ├── images/
│   ├── prompts/                    # Include prompts used
│   ├── presentation.pptx
│   └── presentation.pdf
└── ... (future versions)
```

**Archive README Template**:
```markdown
# Archive: 2026-01-08 Improved Prompts Version

## What Changed
- Rewrote all prompts to be super explicit (8K-20K chars each)
- Improved directional specifications
- Added explicit color palette with hex codes
- Removed all placeholder text

## Why Archived
Replaced by version with better narrative flow and improved visual consistency.

## Files Included
- 32 slide images (.png)
- 32 metadata files (.json)
- Complete prompt set (prompts/)
- Final presentation files (.pptx, .pdf)

## Can Be Restored
Yes - all prompts included, can regenerate if needed.

## Date: 2026-01-08
## Replaced by: 2026-01-15-final-version/
```

---

## Workflow Enforcement Mechanisms

### 1. Validation Scripts

**Check Prerequisites** (`validate_workflow.py`):
```python
#!/usr/bin/env python3
"""
Workflow validation: Ensure correct phase order.
"""

def validate_workflow(content_dir):
    """Validate that workflow phases completed in correct order."""
    errors = []
    
    # Phase 1-2: Storyboard must exist
    storyboard = content_dir / "storyboard.yaml"
    if not storyboard.exists():
        errors.append("Phase 1-2: No storyboard found")
    
    # Phase 3: Prompts must exist
    prompts_dir = content_dir / "prompts"
    if not prompts_dir.exists():
        errors.append("Phase 3: No prompts directory found")
    else:
        # Check prompts are complete
        for prompt_file in prompts_dir.glob("*.txt"):
            content = prompt_file.read_text()
            if len(content) < 2000:
                errors.append(f"Phase 3: Prompt {prompt_file.name} too short")
            if "PLACEHOLDER" in content or "TODO" in content:
                errors.append(f"Phase 3: Prompt {prompt_file.name} has placeholders")
    
    # Phase 4: Images must exist
    images_dir = content_dir / "images"
    if not images_dir.exists():
        errors.append("Phase 4: No images directory found")
    else:
        png_count = len(list(images_dir.glob("*.png")))
        if png_count == 0:
            errors.append("Phase 4: No images generated")
    
    # Phase 5: Final documents should reference existing images only
    for doc in content_dir.glob("*.pptx"):
        # Check that this doc doesn't exist without images
        if not images_dir.exists() or len(list(images_dir.glob("*.png"))) == 0:
            errors.append(f"Phase 5: Document {doc.name} created without images")
    
    return errors

if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    content_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate_workflow(content_dir)
    
    if errors:
        print("❌ WORKFLOW VIOLATIONS FOUND:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Workflow order is correct")
        sys.exit(0)
```

### 2. Generator Tool Updates

Update all document generators to REQUIRE images:

```python
# In presentation_generator.py, build_gpt_pdf.py, etc.

def generate_document(config, images_dir, output_file):
    """Generate final document."""
    
    # BLOCKING CHECK: Images must exist
    if not Path(images_dir).exists():
        raise ValueError(
            f"Images directory does not exist: {images_dir}\n"
            f"You MUST generate images (Phase 4) BEFORE creating documents (Phase 5).\n"
            f"See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
        )
    
    required_images = extract_required_images(config)
    missing = [img for img in required_images if not (Path(images_dir) / img).exists()]
    
    if missing:
        raise FileNotFoundError(
            f"Cannot generate {output_file}: {len(missing)} images missing.\n"
            f"Missing images:\n" + "\n".join(f"  - {m}" for m in missing) + "\n"
            f"Generate images first using:\n"
            f"  python .project/agents/image-generation/tools/gpt_image_generator.py ..."
        )
    
    # Proceed with generation only if all images exist
    ...
```

### 3. Pre-commit Hooks

Add Git pre-commit hook to check workflow order:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check if any final documents are being committed without images
echo "Checking workflow order..."

for pptx in $(git diff --cached --name-only | grep '\.pptx$\|\.pdf$'); do
    dir=$(dirname "$pptx")
    images_dir="$dir/images"
    
    if [ ! -d "$images_dir" ] || [ -z "$(ls -A $images_dir/*.png 2>/dev/null)" ]; then
        echo "❌ ERROR: Committing $pptx without images in $images_dir"
        echo "   You must generate images BEFORE creating final documents."
        echo "   See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
        exit 1
    fi
done

echo "✅ Workflow order check passed"
```

### 4. Documentation Requirements

Every content directory MUST include:

1. **README.md** - Overview and workflow status
2. **storyboard.yaml/json/md** - Content structure (Phase 2)
3. **prompts/** - Complete image prompts (Phase 3)
4. **images/** - Generated images (Phase 4)
5. **archive/** - Previous versions (Phase 6)

**Template README.md**:
```markdown
# [Content Title]

## Workflow Status

- [x] Phase 1-2: Content planning and storyboard
- [x] Phase 3: Complete prompts created (no placeholders)
- [x] Phase 4: Images generated and validated
- [x] Phase 5: Final documents created
- [x] Phase 6: Previous versions archived

## Files

- **storyboard.yaml** - Content structure and scene descriptions
- **prompts/** - Complete image generation prompts (8K-20K chars each)
- **images/** - Generated images (.png + metadata .json)
- **presentation.pptx** - Final PowerPoint presentation
- **presentation.pdf** - PDF version
- **archive/** - Previous versions with READMEs

## Last Updated
2026-01-08

## Generated With
GPT Image 1.5 via Azure AI Foundry
```

---

## Common Mistakes to Avoid

### ❌ WRONG: Generate images while creating document
```python
# DON'T DO THIS
def create_presentation(slides):
    for slide in slides:
        image = generate_image(slide.prompt)  # ❌ Generating during doc creation
        add_to_presentation(slide, image)
    save_presentation()
```

### ✅ CORRECT: Require pre-generated images
```python
# DO THIS
def create_presentation(slides, images_dir):
    validate_images_exist(slides, images_dir)  # ✅ Check first (BLOCKING)
    
    for slide in slides:
        image_path = Path(images_dir) / slide.image_file
        add_to_presentation(slide, image_path)
    save_presentation()
```

### ❌ WRONG: Use placeholder prompts
```text
Create an image for slide 3.
Apply STYLE BASE.
Show functors concept.
```

### ✅ CORRECT: Complete self-contained prompts
```text
Create a technical illustration showing functor transformation.

SCENE: The composition shows a transformation flowing from LEFT to RIGHT.
On the LEFT (at x=20% from left edge): Three input shapes arranged vertically:
- Circle (80px diameter, #3498DB blue, centered at y=30%)
- Square (80x80px, #E74C3C red, centered at y=50%)
- Triangle (80px sides, #2ECC71 green, centered at y=70%)

[... 8,000 more characters of explicit detail ...]
```

---

## Checklist for Each New Content Project

### Before Starting
- [ ] Read this workflow enforcement guide
- [ ] Understand the phase requirements
- [ ] Set up directory structure

### Phase 1-2: Planning
- [ ] Define learning objectives
- [ ] Create content outline
- [ ] Write complete storyboard
- [ ] Review storyboard for completeness

### Phase 3: Prompts
- [ ] Write complete prompts for each image
- [ ] Each prompt 5K+ characters (target 8K-20K)
- [ ] No placeholders or external references
- [ ] Super explicit about directions and positions
- [ ] Include exact color codes (hex)
- [ ] Specify composition, lighting, style
- [ ] Save prompts to files
- [ ] Review prompts against checklist

### Phase 4: Images
- [ ] Verify prompts are complete
- [ ] Generate images using GPT Image 1.5
- [ ] Use parallel generation for efficiency
- [ ] Review image quality
- [ ] Check images match prompts
- [ ] Save metadata files
- [ ] All images in images/ directory

### Phase 5: Documents
- [ ] **VALIDATE** all images exist (REQUIRED)
- [ ] Run workflow validation script
- [ ] Generate documents referencing images
- [ ] Review final output quality
- [ ] Test all links and references

### Phase 6: Archive
- [ ] Create dated archive folder if replacing
- [ ] Move previous version to archive
- [ ] Create archive README
- [ ] Update main README

### Final
- [ ] Run complete validation
- [ ] Commit all files
- [ ] Document lessons learned

---

## Tools and Resources

### Validation
- `.project/agents/image-generation/tools/validate_workflow.py` - Phase order validation
- `.project/agents/image-generation/tools/validate_prompts.py` - Prompt completeness check

### Generation
- `.project/agents/image-generation/tools/gpt_image_generator.py` - Image generation
- `.project/agents/image-generation/tools/presentation_generator.py` - Document generation

### Documentation
- `.project/agents/image-generation/WORKFLOW-ENFORCEMENT.md` - This guide
- `.project/agents/image-generation/image-prompt-engineering-guide.md` - Prompt writing
- `.github/agents/image-generation.agent.md` - Agent configuration

### Examples
- `renders/.../comic/README-IMPROVED-WORKFLOW.md` - PR #38 comic workflow
- `renders/.../comic/PROMPT-ENGINEERING-GUIDE.md` - Detailed prompt examples

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-08 | Initial workflow enforcement guide based on PR #36/#38 learnings |

## See Also

- PR #36: Original comic generation with lessons learned
- PR #38: Improved workflow with hyper-detailed prompts
- `.github/agents/image-generation.agent.md` - Agent capabilities
