# Image Generation Workflow - Frequently Asked Questions (FAQ)

> **Purpose**: Answer common questions about workflow enforcement  
> **Version**: 1.0.0  
> **Created**: 2026-01-08  
> **Related**: WORKFLOW-ENFORCEMENT.md, QUICK-START.md, MIGRATION-GUIDE.md

## Table of Contents
- [General Questions](#general-questions)
- [Workflow Order](#workflow-order)
- [Prompts](#prompts)
- [Images](#images)
- [Documents](#documents)
- [Validation](#validation)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## General Questions

### Q: Why is workflow order important?

**A**: Workflow order ensures quality and reproducibility:

1. **Quality**: Complete prompts (Phase 3) before images (Phase 4) ensures you know exactly what you want
2. **Reproducibility**: With complete prompts, you can regenerate images if needed
3. **Efficiency**: Generating all images before documents avoids back-and-forth
4. **Documentation**: Storyboard and prompts document intent for future maintainers
5. **Avoiding mistakes**: Learned from PR #36 where convoluted workflow led to issues

### Q: What if I just want to quickly test something?

**A**: For quick tests, you can:
1. Create minimal storyboard (just what you need)
2. Write quick prompt (still complete, but shorter - aim for 2K-5K chars)
3. Generate ONE image
4. If it works, expand to full project

But even for tests, follow the order: storyboard → prompt → image → document.

### Q: Do I need to use this workflow for all content?

**A**: Use it for:
- ✅ Presentations (PPTX, PDF)
- ✅ Comics and visual stories
- ✅ Diagrams with generated images
- ✅ Any content using GPT Image 1.5

Don't need it for:
- ❌ Text-only markdown files
- ❌ Mermaid/ASCII diagrams (different tool)
- ❌ External images (not generated)

### Q: Is this workflow mandatory?

**A**: Yes for new projects. Validation is enforced:
- Pre-commit hooks block violations
- Generators refuse to run without images
- CI/CD (future) will validate on PRs

For existing projects, see MIGRATION-GUIDE.md.

---

## Workflow Order

### Q: Can I skip the storyboard?

**A**: No. The storyboard (Phase 1-2) is essential because:
1. Documents your intent
2. Helps you think through content before coding
3. Required by validation tools
4. Serves as project documentation
5. Minimal effort (can be simple YAML)

### Q: Can I create the document first and add images later?

**A**: No. This is exactly what we're preventing. The workflow must be:
```
Storyboard → Prompts → Images → Documents
```

Creating documents first leads to:
- ❌ Placeholder prompts
- ❌ Rushed image generation
- ❌ Poor quality results
- ❌ No documentation of intent

### Q: What if I already have the images?

**A**: That's fine! But you still need:
1. Storyboard documenting what the content conveys
2. Prompts DESCRIBING the images you have (for documentation)
3. Then create documents using those images

The prompts document what was intended, enabling future regeneration.

---

## Prompts

### Q: Why do prompts need to be 8K-20K characters?

**A**: Complete descriptions ensure:
1. **Precision**: No ambiguity about what you want
2. **Reproducibility**: Can regenerate exact image
3. **Quality**: More detail = better results
4. **Documentation**: Others understand your intent
5. **No guesswork**: AI knows exactly what to create

### Q: What does "super explicit" mean?

**A**: Super explicit means:

**✅ GOOD (explicit)**:
```
Arrow flows from LEFT TO RIGHT, starting at x=20% and ending at x=80%.
Arrowhead on the RIGHT end (pointing toward target).
Arrow color: Microsoft Blue (#0078D4), 6 pixels thick.
```

**❌ BAD (vague)**:
```
Arrow pointing to the result.
Use blue color.
```

### Q: Can I use "Apply STYLE BASE" or similar references?

**A**: No. These are placeholders. Instead:
1. Describe the complete style in EVERY prompt
2. Copy-paste style description if repeating
3. Be self-contained (no external references)

**Example**: Instead of "Apply STYLE BASE", write:
```
STYLE:
Clean vector illustration with modern tech aesthetic.
Solid colors with subtle gradients (no textures).
Flat design with 2px shadows (20% opacity black, 2px offset).
Professional Microsoft color palette.
Minimalist approach focusing on clarity.
```

### Q: How do I write such long prompts efficiently?

**A**: Strategies:

1. **Templates**: Create prompt template with sections (SCENE, STYLE, COLORS, etc.)
2. **Copy-paste**: Reuse style descriptions across prompts
3. **Scripts**: Use Python script to generate prompts from structured data
4. **Incremental**: Start with 2K chars, expand to 5K, then 8K+
5. **Think once, write fully**: Better to spend time on prompts than regenerating images

### Q: Can I use a shared style guide?

**A**: Not as an external reference. Instead:
1. Create style guide document
2. Copy-paste relevant sections into each prompt
3. Each prompt must be self-contained

This ensures prompts are portable and reproducible without external dependencies.

---

## Images

### Q: Do I have to generate ALL images before creating ANY documents?

**A**: Yes. This is the core rule:
- ✅ Generate ALL images (Phase 4)
- ✅ Validate they exist
- ✅ THEN create documents (Phase 5)

Creating any document before all images exist violates workflow.

### Q: What if one image fails to generate?

**A**: Handle the failure, then continue:
1. Review the error message
2. Fix the prompt (usually content safety issue)
3. Regenerate that specific image
4. Verify all images present
5. Then proceed to documents

### Q: Can I use placeholder images temporarily?

**A**: No. Placeholders defeat the purpose. Instead:
1. Generate actual images
2. If image doesn't meet expectations, regenerate with better prompt
3. Keep iterating until satisfied
4. Then create documents with final images

### Q: How do I regenerate one image without redoing all?

**A**: Easy:
```bash
# Regenerate specific image
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/slide-05-diagram.txt \
  --output-dir images/ \
  --aspect landscape \
  --quality high \
  --output-prefix slide_05

# Replaces old slide_05_*.png with new version
```

---

## Documents

### Q: Why can't I create documents and images at the same time?

**A**: Creating them simultaneously leads to:
1. **Rushed decisions**: Pressure to move fast
2. **Placeholder prompts**: Don't take time for complete descriptions
3. **Poor quality**: Images generated with insufficient detail
4. **No documentation**: No record of what was intended
5. **Hard to improve**: Can't easily regenerate

Sequential process ensures quality at each step.

### Q: What if my document generator doesn't check for images?

**A**: Update it! Add validation:

```python
from pathlib import Path

def validate_images_exist(slides, images_dir):
    """BLOCKING: Images must exist before document generation."""
    if not Path(images_dir).exists():
        raise ValueError(
            f"Images directory doesn't exist: {images_dir}\n"
            f"Generate images BEFORE creating documents.\n"
            f"See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
        )
    
    # Check each required image
    missing = []
    for slide in slides:
        if slide.image_file:
            path = Path(images_dir) / slide.image_file
            if not path.exists():
                missing.append(str(path))
    
    if missing:
        raise FileNotFoundError(
            f"Cannot create document: {len(missing)} images missing.\n"
            f"Missing: {', '.join(missing)}\n"
            f"Generate images first!"
        )

# Call this BEFORE starting document generation
validate_images_exist(slides, "images/")
```

### Q: Can I skip validation if I know images exist?

**A**: Don't skip validation. It's fast and catches mistakes:
- Typos in image filenames
- Missing images you forgot about
- Moved/deleted images
- Provides clear error messages

Run validation, fix any issues, then proceed.

---

## Validation

### Q: How do I validate my project?

**A**: Run validation tools:

```bash
# Check complete workflow
python .project/agents/image-generation/tools/validate_workflow.py .

# Check prompt quality
python .project/agents/image-generation/tools/validate_prompts.py prompts/

# Expected output:
# ✅ Phase 1-2: Storyboard
# ✅ Phase 3: Prompts (no placeholders)
# ✅ Phase 4: Images
# ✅ Phase 5: Documents (created after images)
# ✅ Phase 6: Archive
```

### Q: What if validation fails?

**A**: Read the error messages - they tell you exactly what to fix:

**Example error**:
```
❌ Phase 3: Prompts
  Contains placeholder 'TODO' - prompt must be complete
```

**Fix**: Edit prompt, remove TODO, add complete description.

Then re-validate.

### Q: Can I bypass validation temporarily?

**A**: For Git commits, use `--no-verify`:
```bash
git commit --no-verify -m "WIP: Draft work"
```

But this is **NOT RECOMMENDED**. Better to fix issues than bypass checks.

### Q: How often should I validate?

**A**: Validate:
- ✅ After completing each phase
- ✅ Before generating images
- ✅ Before creating documents  
- ✅ Before committing

Validation is fast (<1 second) - run it liberally.

---

## Troubleshooting

### Q: Error: "No storyboard found"

**A**: Create a storyboard file:
```yaml
# storyboard.yaml
presentation:
  title: "Your Title"
slides:
  - id: 1
    title: "Slide 1"
    visual_description: "What the image shows..."
```

See QUICK-START.md for complete template.

### Q: Error: "Prompts contain placeholders"

**A**: Edit prompts and remove:
- "TODO", "PLACEHOLDER", "TBD"
- "Apply STYLE BASE"
- "[insert...]", "[add...]"

Replace with complete descriptions.

### Q: Error: "Prompt too short"

**A**: Expand prompt with explicit details:
- Add color specifications (hex codes)
- Describe orientations (LEFT TO RIGHT, clockwise)
- Give measurements (pixels, percentages)
- Define composition thoroughly
- Describe lighting and style

Target 8K-20K characters.

### Q: Error: "Images directory does not exist"

**A**: This means you're trying to create documents before images. 

**Fix**: Generate images first!
```bash
mkdir images
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all.txt \
  --output-dir images/ \
  --parallel 5
```

### Q: Error: "Cannot generate document: X images missing"

**A**: This is CORRECT behavior! It's blocking you from violating workflow.

**Fix**:
1. Check which images are missing
2. Generate those images
3. Verify all images present
4. Then create document

### Q: Validation passes but images look wrong

**A**: Validation checks workflow order, not image quality. To fix quality:
1. Review the image
2. Identify what's wrong
3. Improve the prompt (be more explicit)
4. Regenerate that image
5. Review again
6. Iterate until satisfied

---

## Best Practices

### Q: What's the best way to organize prompts?

**A**: Structure:
```
your-project/
├── storyboard.yaml          # Content structure
├── prompts/                 # All prompts
│   ├── slide-01-title.txt   # One file per image
│   ├── slide-02-intro.txt
│   └── ...
├── images/                  # Generated images
└── README.md                # Project documentation
```

### Q: Should I version control images?

**A**: Yes, but consider:
- **Small projects**: Commit images directly
- **Large projects**: Use Git LFS
- **Always commit**: Prompts and metadata (reproducibility)

### Q: How do I handle style changes across all images?

**A**: Update prompts and regenerate:
1. Update style section in all prompts (can script this)
2. Regenerate all images
3. Archive old version first
4. Update documents

This is why complete prompts are important - easy to regenerate.

### Q: Can I parallelize image generation?

**A**: Yes! Use `--parallel`:
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all.txt \
  --output-dir images/ \
  --parallel 5
```

Respects rate limits automatically.

### Q: What's the best prompt length?

**A**: Target range:
- **Minimum**: 5,000 characters
- **Target**: 8,000-20,000 characters
- **Maximum**: No hard limit, but 20K+ may be excessive

Quality matters more than length. Be explicit, not verbose.

### Q: How do I share projects with others?

**A**: Include everything:
```bash
# Project should have:
- storyboard.yaml      # What it is
- prompts/             # How to recreate
- images/              # Generated assets
- *.pptx, *.pdf        # Final outputs
- README.md            # Documentation

# Others can:
1. Review storyboard to understand intent
2. Review prompts to see specifications
3. Use images as-is
4. Regenerate images if needed (from prompts)
```

### Q: What if requirements change mid-project?

**A**: Follow workflow for changes:
1. Update storyboard with new requirements
2. Update affected prompts
3. Regenerate affected images
4. Archive old version
5. Regenerate documents with new images

This is manageable because you have complete prompts.

---

## Examples

### Q: Can you show a complete workflow example?

**A**: Yes! See:
```
renders/by-domain/.../functional-programming/presentations/professional-category-theory/
```

This example has:
- ✅ storyboard.yaml - Content structure
- ✅ README.md - Workflow instructions
- ✅ Shows Phase 1-2 complete
- ✅ Documents next steps

### Q: Where can I see good prompt examples?

**A**: Check PR #38:
```
renders/.../endoleaks/type-2/english/comic/gpt-prompts-v2-detailed-all-panels.txt
```

These are 8K-20K character prompts with:
- Complete scene descriptions
- Super explicit directions
- Hex color codes
- Pixel measurements
- No placeholders

### Q: Are there templates I can use?

**A**: Yes:

**Storyboard template**: See QUICK-START.md section "Step 1-2"

**Prompt template**: Structure your prompts like:
```
[TITLE]

SCENE COMPOSITION:
[Describe layout, LEFT TO RIGHT flow, positions]

ELEMENTS:
[List all elements with exact specifications]

STYLE:
[Complete style description]

COLORS:
[Hex codes for all colors]

LIGHTING:
[Light sources, shadows]

CONSTRAINTS:
[What to avoid, requirements]
```

---

## Getting More Help

### Q: Where can I find more information?

**A**: Documentation:
1. **QUICK-START.md** - Step-by-step for new projects
2. **WORKFLOW-ENFORCEMENT.md** - Complete 20KB guide
3. **MIGRATION-GUIDE.md** - Update existing projects
4. **tools/README.md** - Tool reference

### Q: What if I'm still stuck?

**A**: Debugging process:
1. Read error message carefully
2. Check relevant section in docs
3. Review example projects
4. Validate each phase individually
5. Ask for help with specific error

### Q: Can I suggest improvements to the workflow?

**A**: Yes! Proposed improvements go in:
```
.project/improvements.md
```

See IMP-011 (CI/CD integration) and IMP-012 (interactive tutorial) for examples.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.0 | 2026-01-09 | Added troubleshooting for PR #42 issues (panel numbering, multi-line prompts) |
| 1.0.0 | 2026-01-08 | Initial FAQ based on common questions |

---

## Troubleshooting New Issues (PR #42)

### Q: All my images are numbered `image_001_*` instead of `image_001`, `image_002`, etc.

**A**: The generation script didn't include the `--output` parameter with panel numbers.

**Fix for existing images**: Run viewing file generator (uses timestamp ordering as fallback):
```bash
python tools/generate_viewing_files.py
```

**Fix for future generation**: Update your script to include panel numbering:
```bash
# WRONG - all images get image_001 prefix
python gpt_image_generator.py --prompt "$prompt_content" --output-dir panels/

# CORRECT - each image gets proper panel number
python gpt_image_generator.py --prompt "$prompt_content" --output "image_${panel_num}" --output-dir panels/
```

### Q: My viewing files only show "Panel 1" even though I have many images

**A**: This happens when all images have the same `image_001` prefix. The viewing file generator now handles this by using timestamp ordering.

**Fix**: Regenerate viewing files:
```bash
python renders/.../tools/generate_viewing_files.py
```

### Q: How do I use multi-line prompts (8K+ characters) from a file?

**A**: Use `=== PANEL XX ===` delimiters in your prompts file:

```text
=== PANEL 01: First Scene ===

[Your complete 8K+ character prompt here]
All the details, colors, positioning...

=== PANEL 02: Second Scene ===

[Your complete 8K+ character prompt here]
...
```

Then run:
```bash
python gpt_image_generator.py --prompt-file prompts-all-panels.txt --output-dir panels/ --parallel 5
```

The generator auto-detects the delimiter format and extracts each panel's prompt correctly.

### Q: How should I structure my story for a comic?

**A**: Use the story-first workflow (COMIC-STORY-WORKFLOW.md):

1. **Story Idea**: Define characters, educational goals, story hook - NO panels yet
2. **Full Narrative**: Write complete flowing prose story - NO panel references
3. **Panel Planning**: Decide how to break story into panels AFTER story is written
4. **Storyboard**: Map narrative sections to specific panels
5. **Prompts**: Write detailed prompts for each panel
6. **Images**: Generate images with proper numbering

**Common Mistake**: Defining "Story Arc (35 Panels)" in the Story Idea phase locks you into a structure before the story is written.

---

## See Also

- **COMIC-STORY-WORKFLOW.md** - Story-first approach for comics (11KB)
- **WORKFLOW-ENFORCEMENT.md** - Complete guide (20KB)
- **QUICK-START.md** - Tutorial (16KB)
- **MIGRATION-GUIDE.md** - Existing projects (14KB)
- **tools/README.md** - Tool reference
- **PR #36** - Original lessons learned
- **PR #38** - Workflow improvements
- **PR #42** - Comic fixes and story-first workflow
