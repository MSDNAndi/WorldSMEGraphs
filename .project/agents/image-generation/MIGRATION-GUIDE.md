# Migration Guide: Applying Workflow Enforcement to Existing Projects

> **Purpose**: Guide for updating existing presentations/comics to comply with proper workflow order  
> **Version**: 1.0.0  
> **Created**: 2026-01-08  
> **Audience**: Project maintainers, content creators

## Overview

This guide helps you update existing content projects (presentations, comics, diagrams) to comply with the workflow enforcement system implemented based on PR #36 and PR #38 learnings.

## When to Use This Guide

Use this guide if you have:
- Existing presentations (PPTX/PDF) created before workflow enforcement
- Comics or visual content generated with old workflow
- Documents that may violate the correct phase order
- Content with placeholder prompts or missing storyboards

## Prerequisites

- Workflow enforcement tools installed (see QUICK-START.md)
- Existing project directory with content
- Understanding of correct workflow order:
  ```
  Phase 1-2: Storyboard → Phase 3: Prompts → Phase 4: Images → Phase 5: Documents
  ```

## Step-by-Step Migration

### Step 1: Assess Current State

**Goal**: Understand what's missing and what needs updating

```bash
# Navigate to your project
cd renders/by-domain/.../your-project/

# Run workflow validation
python .project/agents/image-generation/tools/validate_workflow.py .

# Review output - note violations
```

**Common violations**:
- ❌ No storyboard (Phase 1-2)
- ❌ No prompts directory or prompts with placeholders (Phase 3)
- ❌ Missing images (Phase 4)
- ❌ Documents exist but images don't (Phase 5 violation)

### Step 2: Archive Current Version

**Goal**: Preserve existing work before making changes

```bash
# Create archive directory
mkdir -p archive/$(date +%Y-%m-%d)-pre-workflow-migration

# Move current files to archive
# (Adjust based on what you have)
mv *.pptx *.pdf archive/$(date +%Y-%m-%d)-pre-workflow-migration/ 2>/dev/null || true
mv images/ archive/$(date +%Y-%m-%d)-pre-workflow-migration/ 2>/dev/null || true
mv prompts/ archive/$(date +%Y-%m-%d)-pre-workflow-migration/ 2>/dev/null || true

# Create archive README
cat > archive/$(date +%Y-%m-%d)-pre-workflow-migration/README.md << 'EOL'
# Pre-Workflow Migration Archive

## What This Was
Original version before applying workflow enforcement.

## Why Archived
Migrating to comply with proper workflow order:
- Storyboard → Prompts → Images → Documents

## Contents
- Previous presentation files
- Original images (if any)
- Original prompts (if any)

## Migration Date
$(date +%Y-%m-%d)

## Can Be Restored
Yes - files preserved for reference
EOL
```

### Step 3: Create Missing Storyboard (Phase 1-2)

**Goal**: Document what the content is meant to convey

If you don't have a storyboard, create one based on existing content:

```bash
# Create storyboard file
nano storyboard.yaml
```

**storyboard.yaml template**:
```yaml
presentation:
  title: "Your Presentation Title"
  subtitle: "Your Subtitle"
  author: "Author Name"
  theme: "professional"

slides:
  - id: 1
    title: "Slide 1 Title"
    type: title
    educational_goal: "What this slide teaches"
    visual_description: |
      Describe what the image should show.
      Be specific about layout, elements, directions.
      
  - id: 2
    title: "Slide 2 Title"
    type: content
    educational_goal: "Learning objective"
    visual_description: |
      Complete visual description.
      Include directions (LEFT TO RIGHT, etc.)
```

**Tips for reverse-engineering from existing slides**:
1. Look at existing slides/images
2. Write down what each one shows
3. Document the educational intent
4. Describe visual elements explicitly

**Validate storyboard**:
```bash
# Check phase 1-2
python .project/agents/image-generation/tools/validate_workflow.py .
# Should now show ✅ Phase 1-2: Storyboard
```

### Step 4: Create Complete Prompts (Phase 3)

**Goal**: Write 8K-20K character prompts for each image, NO placeholders

```bash
# Create prompts directory
mkdir -p prompts

# For each slide/panel, create a complete prompt
nano prompts/slide-01-title.txt
```

**If you have old prompts with placeholders**:

1. Review old prompts (if in archive)
2. Expand each placeholder into complete description
3. Be super explicit about:
   - Directions (LEFT TO RIGHT, clockwise, etc.)
   - Colors (hex codes like #0078D4)
   - Sizes (pixel measurements)
   - Positions (exact coordinates or percentages)
   - Layout and composition

**Example - expanding a placeholder prompt**:

❌ **OLD (with placeholders)**:
```
Apply STYLE BASE.
Show functor concept.
Use professional style.
```

✅ **NEW (complete)**:
```
Create a technical illustration showing functor transformation in functional programming.

SCENE COMPOSITION:
The image shows a transformation process flowing from LEFT to RIGHT across the canvas.

On the LEFT side (at 15% from left edge), place an input container:
- Rounded rectangle (200px wide, 400px tall)
- Color: Light blue (#E3F2FD) with 3px border in Microsoft Blue (#0078D4)
- Inside: Three circles stacked vertically...

[Continue with 8,000-20,000 characters of explicit detail]

DIRECTIONAL SPECIFICATIONS:
- Main flow: LEFT TO RIGHT (input to output)
- Transformation occurs in center
- Arrows point from source TO destination (arrowheads on target end)

COLOR PALETTE:
- Input: #E3F2FD (light blue)
- Transform: #8661C5 (Visual Studio purple)
- Output: #F3E5F5 (light purple)
- Background: #FFFFFF (white)

[... more explicit details ...]
```

**Validate prompts**:
```bash
# Check all prompts
python .project/agents/image-generation/tools/validate_prompts.py prompts/ --verbose

# Fix any issues (placeholders, too short, etc.)

# Re-validate workflow
python .project/agents/image-generation/tools/validate_workflow.py .
# Should show ✅ Phase 3: Prompts (no placeholders)
```

### Step 5: Regenerate Images (Phase 4)

**Goal**: Generate new images using complete prompts

```bash
# Create images directory
mkdir -p images

# Generate all images (parallel for efficiency)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/slide-01-title.txt \
  --output-dir images/ \
  --aspect landscape \
  --quality high \
  --output-prefix slide_01

# Repeat for each slide, or use batch file
# For batch generation:
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all-slides.txt \
  --output-dir images/ \
  --aspect landscape \
  --quality high \
  --parallel 5 \
  --enhance
```

**Review generated images**:
1. Open each image
2. Verify it matches prompt intention
3. Check directions are correct (LEFT TO RIGHT, etc.)
4. Ensure quality is acceptable
5. Regenerate if needed with improved prompt

**Validate images**:
```bash
# Check workflow
python .project/agents/image-generation/tools/validate_workflow.py .
# Should show ✅ Phase 4: Images
```

### Step 6: Regenerate Final Documents (Phase 5)

**Goal**: Create new documents using pre-generated images

**CRITICAL**: Workflow validation MUST pass before this step!

```bash
# FIRST: Validate workflow
python .project/agents/image-generation/tools/validate_workflow.py .

# Should show:
# ✅ Phase 1-2: Storyboard
# ✅ Phase 3: Prompts (no placeholders)
# ✅ Phase 4: Images
# ✅ Ready for Phase 5

# If validation passes, generate documents
python .project/agents/image-generation/tools/presentation_generator.py \
  --slides storyboard.yaml \
  --image-dir images/ \
  --output your-presentation

# For comics
python renders/.../comic/build_gpt_pdf.py \
  --input-dir images/ \
  --output your-comic.pdf
```

**What happens**:
- Tool validates images exist (BLOCKS if missing)
- Creates PPTX with images inserted
- Creates PDF version
- Saves to specified output

### Step 7: Final Validation

**Goal**: Confirm everything is correct

```bash
# Full workflow validation
python .project/agents/image-generation/tools/validate_workflow.py .

# Should show all phases passing:
# ✅ Phase 1-2: Storyboard
# ✅ Phase 3: Prompts (no placeholders)
# ✅ Phase 4: Images
# ✅ Phase 5: Documents (created after images)
# ✅ Phase 6: Archive

# Check output files
ls -lh *.pptx *.pdf

# Review quality
# - Open presentation/document
# - Check all images present
# - Verify layout correct
# - Test navigation
```

### Step 8: Clean Up and Document

**Goal**: Update project README and commit

```bash
# Update project README
cat > README.md << 'EOL'
# Your Project Title

> **Status**: ✅ Workflow-compliant  
> **Last Updated**: $(date +%Y-%m-%d)  
> **Migrated**: $(date +%Y-%m-%d)

## Workflow Status

- [x] Phase 1-2: Storyboard created
- [x] Phase 3: Complete prompts (no placeholders)
- [x] Phase 4: Images generated
- [x] Phase 5: Final documents created
- [x] Phase 6: Pre-migration version archived

## Files

- **storyboard.yaml** - Content structure
- **prompts/** - Complete image prompts (8K-20K chars each)
- **images/** - Generated images
- **your-presentation.pptx** - Final PowerPoint
- **your-presentation.pdf** - PDF version
- **archive/** - Previous versions

## Migration Notes

Migrated from pre-workflow version on $(date +%Y-%m-%d).
Now complies with proper workflow order.

See: `.project/agents/image-generation/WORKFLOW-ENFORCEMENT.md`
EOL

# Commit changes
git add .
git commit -m "Migrate: Applied workflow enforcement to [project name]

- Created storyboard documenting content
- Expanded placeholders to complete prompts (8K+ chars each)
- Regenerated all images from complete prompts
- Recreated documents using pre-generated images
- Archived pre-migration version
- Now complies with workflow order"
```

## Special Cases

### Case 1: Already Have Good Images

If your existing images are high quality and don't need regeneration:

```bash
# Keep existing images
mv archive/$(date +%Y-%m-%d)-pre-workflow-migration/images/ ./

# BUT: Create prompts that DESCRIBE those images
# This documents what was intended
# Write complete prompts (8K-20K chars) describing existing images

# Then validation will pass
python .project/agents/image-generation/tools/validate_workflow.py .
```

### Case 2: Missing Source Information

If you don't know what prompts were used:

```bash
# Reverse-engineer prompts from existing images
# Look at each image and write detailed description

# For each image, create prompt describing what you SEE:
nano prompts/slide-01.txt

# Write:
# - What elements are in the image
# - What colors are used
# - What directions/orientations
# - Layout and composition
# - Style characteristics

# Make it 8K-20K characters by being super explicit
```

### Case 3: Batch Migration of Multiple Projects

If you have many projects to migrate:

```bash
# Create migration script
cat > migrate_all.sh << 'EOL'
#!/bin/bash
for project in $(find renders/by-domain -name "*.pptx" -o -name "*.pdf" | xargs dirname | sort -u); do
    echo "Migrating: $project"
    cd "$project"
    
    # Run workflow validation
    python .project/agents/image-generation/tools/validate_workflow.py . > validation.txt 2>&1
    
    if grep -q "WORKFLOW VIOLATIONS" validation.txt; then
        echo "  ❌ Needs migration"
        # Add to migration queue
        echo "$project" >> /tmp/migration_queue.txt
    else
        echo "  ✅ Already compliant"
    fi
    
    cd - > /dev/null
done

echo ""
echo "Projects needing migration:"
cat /tmp/migration_queue.txt
EOL

chmod +x migrate_all.sh
./migrate_all.sh
```

## Troubleshooting

### "No storyboard found"
**Solution**: Create storyboard.yaml based on existing content. Review slides and document what each shows.

### "Prompts contain placeholders"
**Solution**: Expand each placeholder into complete description. Remove "TODO", "Apply STYLE BASE", etc. Write full 8K-20K character descriptions.

### "Prompts too short"
**Solution**: Add more explicit detail:
- Specify exact colors (hex codes)
- Describe orientations (LEFT TO RIGHT, clockwise)
- Give measurements (pixels, percentages)
- Define composition and layout
- Describe lighting and style

### "Images directory does not exist"
**Solution**: Generate images before trying to create documents. Run Phase 4 first.

### "Cannot generate document: images missing"
**Solution**: This is working as intended! Generate all images before creating final documents. This is the whole point of workflow enforcement.

## Validation Checklist

After migration, verify:

- [ ] Storyboard exists and describes content
- [ ] Prompts directory has complete prompts (no placeholders)
- [ ] Each prompt is 5K+ characters (target 8K-20K)
- [ ] All prompts super explicit (directions, colors, sizes)
- [ ] Images directory has all required images
- [ ] Images match prompt descriptions
- [ ] Final documents reference pre-generated images
- [ ] Pre-migration version archived with README
- [ ] Project README updated with workflow status
- [ ] Workflow validation passes completely

## Benefits After Migration

Once migrated, your project will have:

1. **Documentation**: Storyboard explains intent
2. **Reproducibility**: Complete prompts can regenerate images
3. **Quality**: Super explicit prompts produce better results
4. **Compliance**: Follows correct workflow order
5. **History**: Archived versions preserved
6. **Validation**: Tools ensure ongoing compliance

## Getting Help

If stuck during migration:

1. **Read comprehensive guide**: `.project/agents/image-generation/WORKFLOW-ENFORCEMENT.md`
2. **Check quick start**: `.project/agents/image-generation/QUICK-START.md`
3. **Run validation**: See specific error messages with guidance
4. **Review examples**: Check example projects that follow workflow
5. **Study PR #36 and PR #38**: See real-world workflow improvements

## Next Steps After Migration

Once migrated:

1. Install pre-commit hook to prevent future violations
2. Document migration in project README
3. Share learnings with team
4. Apply workflow to new projects from start
5. Consider automating validation in CI/CD

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-08 | Initial migration guide |

## See Also

- **WORKFLOW-ENFORCEMENT.md** - Complete workflow guide
- **QUICK-START.md** - Guide for new projects
- **tools/README.md** - Tool reference
- **PR #36** - Original workflow issues
- **PR #38** - Workflow improvements
