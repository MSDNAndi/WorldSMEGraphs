# Renders Workflow Guide

**For**: Content creators and contributors  
**Purpose**: Step-by-step workflows for common render tasks  
**Last Updated**: 2026-01-06

---

## Table of Contents

1. [Creating Your First Render](#creating-your-first-render)
2. [Updating Existing Renders](#updating-existing-renders)
3. [Translating Renders](#translating-renders)
4. [Quality Assurance](#quality-assurance)
5. [Batch Operations](#batch-operations)
6. [Troubleshooting](#troubleshooting)

---

## Creating Your First Render

### Prerequisites

- Knowledge of the source domain
- Understanding of target audience
- Familiarity with audience profiles (`renders/_metadata/audience-profiles.yaml`)

### Step-by-Step

#### 1. Choose Source Content

Find the domain AKUs you want to render:

```bash
ls domain/natural-sciences/physics/quantum-mechanics/planck-units/akus/
```

Read the AKUs to understand the content:

```bash
cat domain/natural-sciences/physics/quantum-mechanics/planck-units/akus/aku-001-*.json
```

#### 2. Select Audience

Choose from defined audiences:
- `preschool`, `elementary-school`, `middle-school`, `high-school`
- `undergraduate`, `graduate`, `adult-limited-reading`, `professional`

Review guidelines:
```bash
grep -A20 "elementary-school:" renders/_metadata/audience-profiles.yaml
```

#### 3. Create Render (Automated)

Use the helper script:

```bash
bash renders/_metadata/tools/create_render.sh \
  natural-sciences/physics/quantum-mechanics/planck-units \
  english \
  elementary-school
```

This will:
- ✅ Create directory structure
- ✅ Generate template file
- ✅ Update render index
- ✅ Update AKU usage matrix
- ✅ Provide next steps

#### 4. Write Content

Edit the generated file:

```bash
vim renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
```

**Guidelines**:
- Use simple, age-appropriate language
- Define technical terms
- Include examples
- Add visuals if helpful
- Cite source AKUs

**Example Structure**:

```markdown
# Planck Units - Elementary School

> **For**: Grades 1-5  
> **Reading Level**: 3rd-4th grade  
> **Time**: 10 minutes

## What Are They?

[Simple explanation in 2-3 sentences]

## Why Do We Care?

[Practical importance in child-friendly terms]

## Key Ideas

### Idea 1: [Concept Name]

[Explanation with concrete examples]

### Idea 2: [Concept Name]

[Explanation with concrete examples]

## Try This!

[Interactive activity or thought experiment]

## Learn More

[Links to related topics or next steps]

---

**Source**: domain/natural-sciences/physics/quantum-mechanics/planck-units/  
**Last Updated**: 2026-01-06
```

#### 5. Check Quality

Run the linter:

```bash
python renders/_metadata/tools/render_quality_linter.py \
  renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
```

Address any issues or warnings.

#### 6. Commit

```bash
git add renders/
git commit -m "Add elementary school render for Planck units"
git push
```

---

## Updating Existing Renders

### When to Update

- Source AKUs changed
- Errors or inaccuracies found
- Improve clarity or examples
- Update outdated information

### Workflow

#### 1. Check AKU Usage

Find which renders use specific AKUs:

```bash
grep -A5 "aku-planck-length-001" renders/_metadata/aku-usage-matrix.yaml
```

#### 2. Update Render

Edit the file:

```bash
vim renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/undergraduate.md
```

#### 3. Update Metadata

If file has frontmatter, update the date:

```yaml
---
updated: "2026-01-06"
version: "1.1.0"
---
```

#### 4. Re-run Quality Checks

```bash
python renders/_metadata/tools/render_quality_linter.py [file]
```

#### 5. Regenerate Indexes

```bash
python renders/_metadata/tools/generate_render_index.py
python renders/_metadata/tools/generate_aku_usage_matrix.py
```

#### 6. Commit

```bash
git add renders/
git commit -m "Update [audience] render for [topic]: [brief description]"
```

---

## Translating Renders

### Prerequisites

- Fluency in target language
- Understanding of source content
- Knowledge of cultural adaptations needed

### Workflow

#### 1. Choose Source Render

```bash
cat renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
```

#### 2. Create Target Language Directory

```bash
mkdir -p renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/german
```

#### 3. Translate Content

Create new file:

```bash
touch renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/german/grundschule.md
```

**Translation Guidelines**:
- Maintain audience level (don't simplify/complicate)
- Adapt examples for cultural relevance
- Use appropriate terminology
- Keep same structure when possible
- Cite same source AKUs

#### 4. Quality Check

```bash
python renders/_metadata/tools/render_quality_linter.py \
  renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/german/grundschule.md
```

#### 5. Update Indexes

```bash
python renders/_metadata/tools/generate_render_index.py
```

#### 6. Commit

```bash
git add renders/
git commit -m "Add German translation of elementary school Planck units render"
```

---

## Quality Assurance

### Pre-Commit Checklist

- [ ] Content accurate (matches source AKUs)
- [ ] Appropriate for target audience
- [ ] Reading level matches guidelines
- [ ] All images have alt text
- [ ] Links use descriptive text
- [ ] No spelling or grammar errors
- [ ] Proper heading hierarchy
- [ ] Metadata complete (if using frontmatter)
- [ ] Linter passes with no issues
- [ ] Indexes updated

### Running Full QA

```bash
# 1. Lint content
python renders/_metadata/tools/render_quality_linter.py renders/by-domain/[path]/

# 2. Regenerate indexes
python renders/_metadata/tools/generate_render_index.py
python renders/_metadata/tools/generate_aku_usage_matrix.py

# 3. Check validation
bash .github/scripts/validate-structure.sh  # if it exists

# 4. Review changes
git status
git diff
```

---

## Batch Operations

### Creating Multiple Renders

Use shell loops:

```bash
for audience in elementary-school middle-school high-school; do
  bash renders/_metadata/tools/create_render.sh \
    natural-sciences/physics/quantum-mechanics/planck-units \
    english \
    $audience
done
```

### Updating Multiple Languages

```bash
# After updating English version, create reminders for translations
for lang in german french spanish; do
  echo "TODO: Update $lang translation of [topic]" >> /tmp/translation-tasks.txt
done
```

### Batch Quality Checks

```bash
# Check all renders in a domain
python renders/_metadata/tools/render_quality_linter.py \
  renders/by-domain/natural-sciences/physics/
```

---

## Troubleshooting

### Issue: Linter Reports Many Warnings

**Common Causes**:
- Sentences too long
- Missing alt text
- Poor link text

**Solutions**:
1. Break long sentences (aim for < 20 words for most audiences)
2. Add descriptive alt text: `![Student conducting experiment](diagram.png)`
3. Use descriptive links: "View the tutorial" not "click here"

### Issue: Can't Find Source AKUs

**Steps**:
1. Check domain path exists:
   ```bash
   ls domain/natural-sciences/physics/quantum-mechanics/planck-units/
   ```

2. Look for akus/ subdirectory:
   ```bash
   ls domain/natural-sciences/physics/quantum-mechanics/planck-units/akus/
   ```

3. If missing, check if AKUs are in parent directory or different location

### Issue: Render Index Out of Date

**Solution**:
```bash
python renders/_metadata/tools/generate_render_index.py
git add renders/_metadata/render-index.yaml
git commit -m "Update render index"
```

### Issue: Unclear Target Audience

**Steps**:
1. Read audience profiles:
   ```bash
   cat renders/_metadata/audience-profiles.yaml
   ```

2. Review examples:
   ```bash
   find renders -name "elementary-school.md" | head -3 | xargs cat
   ```

3. Consult DEVELOPER_GUIDE.md

---

## Quick Reference

### Common Commands

```bash
# Create render
bash renders/_metadata/tools/create_render.sh [domain] [lang] [audience]

# Check quality
python renders/_metadata/tools/render_quality_linter.py [file-or-dir]

# Update indexes
python renders/_metadata/tools/generate_render_index.py
python renders/_metadata/tools/generate_aku_usage_matrix.py

# Find renders
find renders/by-domain -name "*.md"
find renders/by-domain -path "*/english/*"

# Count renders
find renders/by-domain -type f | wc -l
```

### File Locations

- **Tools**: `renders/_metadata/tools/`
- **Documentation**: `renders/_metadata/`
- **Audience Profiles**: `renders/_metadata/audience-profiles.yaml`
- **Render Index**: `renders/_metadata/render-index.yaml`
- **AKU Usage**: `renders/_metadata/aku-usage-matrix.yaml`

---

## Getting Help

- **Developer Guide**: `renders/_metadata/DEVELOPER_GUIDE.md` (comprehensive)
- **Tools Documentation**: `renders/_metadata/tools/README.md`
- **Recommendations**: `renders/_metadata/RECOMMENDATIONS.md`
- **GitHub Issues**: Create issue with `[renders]` tag

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Maintained By**: Pedagogy Agent, Rendering Agent
