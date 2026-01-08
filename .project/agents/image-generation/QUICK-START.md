# Quick Start Guide: Image Generation Workflow

> **Purpose**: Step-by-step guide for creating content with proper workflow order  
> **Version**: 1.0.0  
> **Created**: 2026-01-08  
> **Audience**: Developers and content creators

## Overview

This guide walks you through creating new content (presentations, comics, diagrams) following the **correct workflow order** learned from PR #36 and PR #38.

**Key Rule**: Always generate images BEFORE creating final documents.

## Workflow Order

```
Phase 1-2: Storyboard → Phase 3: Prompts → Phase 4: Images → Phase 5: Documents
```

## Step-by-Step Guide

### Step 0: Setup (One-time)

```bash
# Install pre-commit hook (optional but recommended)
cp .project/agents/image-generation/pre-commit-hook.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Verify environment variables
env | grep AI_FOUNDRY
# Should show: AI_FOUNDRY_API_KEY, AI_FOUNDRY_ENDPOINT, GPT_IMAGE_1DOT5_ENDPOINT_URL
```

### Step 1-2: Create Storyboard (Content Planning)

**Time**: 30-60 minutes  
**Goal**: Define what you want to create

**Actions**:
1. Create content directory structure
2. Write storyboard file describing each scene/slide/panel

**Example** (presentation):
```bash
# Create directory
mkdir -p renders/by-domain/formal-sciences/.../my-presentation
cd renders/by-domain/formal-sciences/.../my-presentation

# Create storyboard
nano storyboard.yaml
```

**storyboard.yaml**:
```yaml
title: "Introduction to Category Theory"
subtitle: "A Developer's Guide"
slides:
  - id: 1
    title: "What is Category Theory?"
    description: "Overview slide with abstract mathematical diagrams"
    educational_goal: "Introduce basic concepts"
    
  - id: 2
    title: "Objects and Morphisms"
    description: "Diagram showing objects connected by arrows"
    educational_goal: "Explain fundamental building blocks"
    visual_direction: "Arrows point LEFT TO RIGHT showing composition"
```

**Validation**:
```bash
# Check storyboard exists
ls -lh storyboard.yaml

# Preview structure
cat storyboard.yaml
```

### Step 3: Write Complete Prompts (SUPER EXPLICIT)

**Time**: 1-3 hours  
**Goal**: Write 8K-20K character prompts for each image, NO placeholders

**Actions**:
1. Create prompts directory
2. Write ONE complete prompt per image
3. Include ALL details explicitly

**Example**:
```bash
mkdir -p prompts
nano prompts/slide-01-what-is-category-theory.txt
```

**prompts/slide-01-what-is-category-theory.txt** (example - should be much longer):
```text
Create a professional technical illustration for a presentation slide about category theory.

SCENE COMPOSITION:
The image shows an abstract mathematical concept visualization.
Background: Dark navy blue (#1A1A2E) with subtle noise texture (5% opacity).

Three geometric objects arranged in a triangle formation:
- Object A: Circle (diameter 120px, solid #3498DB blue) positioned at LEFT side (x=20%, y=30%)
- Object B: Square (120x120px, solid #E74C3C red) positioned at RIGHT side (x=80%, y=30%)  
- Object C: Triangle (equilateral, 120px sides, solid #2ECC71 green) at BOTTOM (x=50%, y=70%)

CONNECTION ARROWS:
- Arrow from A to B: Curved bezier, flows LEFT TO RIGHT, 6px thick, white (#FFFFFF) 80% opacity
  Start point: right edge of circle A (x=20%+60px, y=30%)
  End point: left edge of square B (x=80%-60px, y=30%)
  Arrowhead on RIGHT end (pointing TO square B)
  
- Arrow from B to C: Curved bezier, flows TOP-RIGHT TO BOTTOM-CENTER, 6px thick, white 80%
  Start point: bottom edge of square B
  End point: top-right edge of triangle C
  Arrowhead on end (pointing TO triangle C)
  
- Arrow from A to C: Curved bezier, flows TOP-LEFT TO BOTTOM-CENTER, 6px thick, white 80%
  Start point: bottom edge of circle A
  End point: top-left edge of triangle C
  Arrowhead on end (pointing TO triangle C)

COMPOSITION ANNOTATION:
In the CENTER of the triangle formed by the three objects (x=50%, y=45%), show:
- Dotted curved arrow forming a partial circle, suggesting composition
- Arrow flows CLOCKWISE from arrow A→B, around to B→C, completing at A→C
- Dotted line: 3px thick, dashed (10px dash, 5px gap), yellow (#F1C40F) 70% opacity
- This represents the composition property: A→C can be derived from A→B and B→C

LABELS (Text Elements):
- "A" label: White text, 24px sans-serif bold, positioned above circle A
- "B" label: White text, 24px sans-serif bold, positioned above square B
- "C" label: White text, 24px sans-serif bold, positioned below triangle C
- "f" label: White text, 18px italic, positioned ABOVE arrow A→B
- "g" label: White text, 18px italic, positioned RIGHT of arrow B→C
- "g∘f" label: White text, 18px italic, positioned LEFT of arrow A→C
- "composition" annotation: Yellow text (#F1C40F), 16px italic, positioned center

STYLE:
Clean vector illustration, modern mathematical textbook aesthetic.
Solid colors with smooth gradients for depth (no textures except background).
Professional presentation quality, suitable for academic or developer conference.
Minimalist design focusing on clarity of concept.

LIGHTING:
Soft ambient light from top-left (135° angle).
Subtle glow effect around each object (8px blur, 30% opacity matching object color).
No harsh shadows, maintain clean diagram aesthetic.

TECHNICAL SPECIFICATIONS:
- Aspect ratio: 16:9 (landscape orientation)
- Resolution: 1536x1024 pixels
- Color space: sRGB
- Format: PNG with transparency support (though background is solid)

CONSTRAINTS:
- NO additional text beyond specified labels
- NO human figures or faces
- NO copyrighted symbols or logos
- Original artwork only, not derivative
- Family-friendly, G-rated content
- Professional academic presentation quality

EDUCATIONAL PURPOSE:
This diagram illustrates the fundamental concept of category theory: objects (A, B, C)
connected by morphisms (f, g) with the composition property (g∘f). The visual shows
that you can compose morphisms (go from A to B via f, then B to C via g) to get a
direct morphism from A to C (g∘f). This is the essence of categorical composition.

The triangle layout emphasizes that all three morphisms are related, and the dotted
composition arrow shows the "derived" nature of the A→C path.

DIRECTIONAL SPECIFICATIONS (SUPER EXPLICIT):
- All morphism arrows point from SOURCE to TARGET (arrowheads on target end)
- Primary flow is LEFT TO RIGHT (A to B)
- Secondary flows converge TOWARD BOTTOM (to C)
- Composition flow is CLOCKWISE around center
- Reading order: Start at A (left), move to B (right), conclude at C (bottom)

COLOR PALETTE RATIONALE:
- Blue (#3498DB): Primary, represents starting object
- Red (#E74C3C): Secondary, represents intermediate object
- Green (#2ECC71): Tertiary, represents final object
- Yellow (#F1C40F): Composition, highlights derived morphism
- White: Connections and labels, maintains clarity
- Dark navy: Professional background, high contrast

[... Continue with more explicit detail to reach 8,000-20,000 characters total ...]
```

**Validation**:
```bash
# Validate all prompts
python .project/agents/image-generation/tools/validate_prompts.py prompts/ --verbose

# Check for issues
# - Should be 8K-20K characters each
# - No "TODO", "PLACEHOLDER", "Apply STYLE BASE"
# - Super explicit about directions
```

### Step 4: Generate Images (PARALLEL)

**Time**: 5-30 minutes (depending on number of images and rate limits)  
**Goal**: Generate ALL images before creating ANY documents

**Actions**:
1. Create images output directory
2. Run image generator on all prompts
3. Review generated images

**Example**:
```bash
# Create images directory
mkdir -p images

# Generate all images (PARALLEL for efficiency)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/slide-01-what-is-category-theory.txt \
  --output-dir images/ \
  --aspect landscape \
  --quality high \
  --output-prefix slide_01 \
  --enhance

# For multiple prompts in one file (recommended)
# Create all-prompts.txt with prompts separated by "---"
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all-slides.txt \
  --output-dir images/ \
  --aspect landscape \
  --quality high \
  --parallel 5 \
  --enhance
```

**Review Images**:
```bash
# List generated images
ls -lh images/

# View images (use your preferred image viewer)
# Check that images match prompts
# Verify directions are correct (LEFT TO RIGHT, etc.)
```

**Validation**:
```bash
# Validate workflow at this point
python .project/agents/image-generation/tools/validate_workflow.py .

# Should show:
# ✅ Phase 1-2: Storyboard
# ✅ Phase 3: Prompts
# ✅ Phase 4: Images
# Note: Phase 5 (Documents) not yet created - that's correct!
```

### Step 5: Create Final Documents

**Time**: 10-30 minutes  
**Goal**: Create PPTX, PDF, HTML using pre-generated images

**Prerequisites Check** (CRITICAL):
```bash
# Verify all images exist
ls -1 images/*.png | wc -l
# Should match number of slides/panels expected

# Run workflow validation
python .project/agents/image-generation/tools/validate_workflow.py .
# Must pass before proceeding
```

**Generate Documents**:
```bash
# For presentations
python .project/agents/image-generation/tools/presentation_generator.py \
  --slides storyboard.yaml \
  --image-dir images/ \
  --output my-presentation

# For comics (if using comic structure)
python renders/.../comic/build_gpt_pdf.py \
  --input-dir images/ \
  --output my-comic.pdf
```

**What Happens**:
- Tool validates images exist (BLOCKS if missing)
- Creates PPTX with images inserted
- Creates PDF version
- Saves to specified output path

**Validation**:
```bash
# Check output files
ls -lh my-presentation.pptx my-presentation.pdf

# Open and review
# - All images present?
# - Layout correct?
# - Quality acceptable?
```

### Step 6: Archive (When Updating)

**Time**: 5-10 minutes  
**Goal**: Archive previous versions before replacing

**Only needed when** updating existing content with new version.

**Actions**:
```bash
# Create archive directory structure
mkdir -p archive/2026-01-08-initial-version

# Move previous version to archive
mv images/ archive/2026-01-08-initial-version/
mv prompts/ archive/2026-01-08-initial-version/
mv my-presentation.pptx archive/2026-01-08-initial-version/
mv my-presentation.pdf archive/2026-01-08-initial-version/

# Create archive README
nano archive/2026-01-08-initial-version/README.md
```

**archive/.../README.md**:
```markdown
# Archive: 2026-01-08 Initial Version

## What This Was
First version of "Introduction to Category Theory" presentation.

## Why Archived
Replaced by improved version with:
- Better narrative flow
- More explicit diagrams
- Enhanced color consistency

## Contents
- images/ - 10 slide images
- prompts/ - Complete prompts used
- my-presentation.pptx - PowerPoint file
- my-presentation.pdf - PDF version

## Restoration
Can be restored using archived prompts:
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all-slides.txt \
  --output-dir images-restored/
```

## Date: 2026-01-08
## Replaced By: Current version in parent directory
```

## Final Validation

Before committing:
```bash
# Full workflow validation
python .project/agents/image-generation/tools/validate_workflow.py .

# Should show all phases passing:
# ✅ Phase 1-2: Storyboard
# ✅ Phase 3: Prompts (no placeholders)
# ✅ Phase 4: Images
# ✅ Phase 5: Documents (created after images)
# ✅ Phase 6: Archive (if applicable)

# Commit with descriptive message
git add .
git commit -m "Add: Introduction to Category Theory presentation (workflow compliant)"
```

## Troubleshooting

### "Images directory does not exist"
**Problem**: Trying to create document before generating images  
**Fix**: Generate images first (Step 4)

### "Contains placeholder 'TODO'"
**Problem**: Prompts not complete  
**Fix**: Rewrite prompts without placeholders (Step 3)

### "Prompt too short: X characters"
**Problem**: Prompt lacks sufficient detail  
**Fix**: Add explicit specifications (target 8K-20K chars)

### Image doesn't match intention
**Problem**: Prompt not explicit enough about directions/details  
**Fix**: 
1. Rewrite prompt with SUPER EXPLICIT directions
2. Regenerate that specific image
3. Review before creating final document

### Pre-commit hook blocks commit
**Problem**: Workflow validation detected violation  
**Fix**: Follow error message guidance
- Generate missing images
- Fix incomplete prompts
- Archive before replacing

## Common Mistakes

### ❌ WRONG: Generate images while creating document
```python
# DON'T DO THIS
for slide in slides:
    image = generate_image(slide.prompt)  # Generating during doc creation
    add_to_document(slide, image)
save_document()
```

### ✅ CORRECT: Generate ALL images first, then create document
```bash
# Step 1: Generate all images
python gpt_image_generator.py --prompt-file all-prompts.txt --output-dir images/

# Step 2: Validate images exist
python validate_workflow.py .

# Step 3: Create document using pre-generated images
python presentation_generator.py --slides slides.yaml --image-dir images/
```

## Time Estimates

| Phase | Typical Time | What Takes Long |
|-------|--------------|-----------------|
| 1-2. Storyboard | 30-60 min | Thinking through content |
| 3. Prompts | 1-3 hours | Writing explicit detail |
| 4. Images | 5-30 min | API calls, rate limits |
| 5. Documents | 10-30 min | Assembly, formatting |
| 6. Archive | 5-10 min | Organization |
| **Total** | **2-5 hours** | Mostly prompt writing |

**Tip**: Most time is in writing quality prompts. Invest time here for better results.

## Checklist

Use this checklist for every new content project:

```markdown
## Content Creation Checklist

- [ ] Step 1-2: Storyboard
  - [ ] Created content directory
  - [ ] Wrote storyboard file
  - [ ] Defined educational goals
  - [ ] Specified visual directions
  
- [ ] Step 3: Complete Prompts
  - [ ] Created prompts directory
  - [ ] Wrote ONE complete prompt per image
  - [ ] Each prompt 8K-20K characters
  - [ ] NO placeholders (TODO, PLACEHOLDER, etc.)
  - [ ] Super explicit directions (LEFT TO RIGHT, hex colors, px sizes)
  - [ ] Ran validate_prompts.py - all passed
  
- [ ] Step 4: Generate Images
  - [ ] Created images directory
  - [ ] Generated ALL images
  - [ ] Reviewed image quality
  - [ ] Verified images match prompts
  - [ ] Ran validate_workflow.py - Phase 4 passed
  
- [ ] Step 5: Create Documents
  - [ ] Ran validate_workflow.py BEFORE starting
  - [ ] Generated PPTX/PDF/HTML
  - [ ] Reviewed final output
  - [ ] Quality acceptable
  
- [ ] Step 6: Archive (if updating)
  - [ ] Created dated archive folder
  - [ ] Moved old version to archive
  - [ ] Created archive README
  - [ ] Documented what changed
  
- [ ] Final Validation
  - [ ] Ran validate_workflow.py - all phases passed
  - [ ] Committed with descriptive message
  - [ ] Pushed to repository
```

## Next Steps

After creating your content:
1. Review [WORKFLOW-ENFORCEMENT.md](./WORKFLOW-ENFORCEMENT.md) for deeper understanding
2. Check [image-generation.agent.md](../../.github/agents/image-generation.agent.md) for advanced features
3. Read [image-prompt-engineering-guide.md](./image-prompt-engineering-guide.md) for prompt tips
4. Study PR #36 and PR #38 for real-world examples

## Support

Questions? Check:
1. This quick start guide
2. WORKFLOW-ENFORCEMENT.md (comprehensive)
3. tools/README.md (tool reference)
4. Validation tool error messages (they guide you)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-08 | Initial quick start guide |
