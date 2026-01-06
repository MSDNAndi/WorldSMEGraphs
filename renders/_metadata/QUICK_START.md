# Renders Quick Start

**Get started with renders in 5 minutes**

---

## What Are Renders?

Renders are **human-readable** versions of language-agnostic knowledge graphs (AKUs), tailored for specific:
- **Languages**: English, German, French, etc.
- **Audiences**: Preschool → Graduate level
- **Formats**: Markdown, PDF, PPTX, etc.

**Example**: A physics AKU about Planck units might have renders for elementary school kids, high school students, and graduate researchers - all from the same source content.

---

## Directory Structure

```
renders/
├── by-domain/              ← START HERE
│   └── [domain-path]/
│       └── [language]/
│           └── [audience].md
└── _metadata/              ← Documentation & tools
    ├── DEVELOPER_GUIDE.md
    ├── WORKFLOW_GUIDE.md
    └── tools/
```

---

## Creating Your First Render (3 Steps)

### 1. Use the Helper Script

```bash
bash renders/_metadata/tools/create_render.sh \
  natural-sciences/physics/quantum-mechanics/planck-units \
  english \
  elementary-school
```

This creates:
- ✅ Directory structure
- ✅ Template file
- ✅ Updated indexes

### 2. Edit the File

```bash
vim renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
```

Write content appropriate for your audience. See `renders/_metadata/audience-profiles.yaml` for guidelines.

### 3. Commit

```bash
git add renders/
git commit -m "Add elementary school render for Planck units"
git push
```

**Done!** 🎉

---

## Essential Commands

```bash
# Create render
bash renders/_metadata/tools/create_render.sh [domain] [lang] [audience]

# Check quality
python renders/_metadata/tools/render_quality_linter.py [file]

# Update indexes (automatically done by create_render.sh)
python renders/_metadata/tools/generate_render_index.py

# Find existing renders
find renders/by-domain -name "*.md"
```

---

## Audience Levels

Choose one:
- `preschool` (ages 3-5)
- `elementary-school` (grades 1-5)
- `middle-school` (grades 6-8)
- `high-school` (grades 9-12)
- `undergraduate` (college)
- `graduate` (advanced/professional)
- `adult-limited-reading` (adults, 6-8th grade reading level)
- `professional` (expert practitioners)

Full definitions: `renders/_metadata/audience-profiles.yaml`

---

## Quality Checklist

Before committing, ensure your render has:
- [ ] Appropriate reading level for audience
- [ ] Clear, accurate content
- [ ] Proper grammar and spelling
- [ ] Images with alt text (if any)
- [ ] Descriptive link text (not "click here")
- [ ] Citation to source AKUs

Run linter to check:
```bash
python renders/_metadata/tools/render_quality_linter.py [your-file]
```

---

## Example Render Structure

```markdown
# Topic Name - Audience Level

> **For**: [Audience description]  
> **Reading Level**: [Grade level]  
> **Time**: [Estimated reading time]

## What Is It?

[Simple introduction in 2-3 sentences]

## Why Does It Matter?

[Practical importance]

## Key Concepts

### Concept 1: [Name]

[Explanation with examples]

### Concept 2: [Name]

[Explanation with examples]

## Learn More

[Links to related topics]

---

**Source**: domain/[path-to-source-akus]/  
**Last Updated**: YYYY-MM-DD
```

---

## Need More Help?

📚 **Full Guides**:
- `renders/_metadata/DEVELOPER_GUIDE.md` (14KB, comprehensive)
- `renders/_metadata/WORKFLOW_GUIDE.md` (9KB, step-by-step)
- `renders/_metadata/INDEX.md` (navigation to all docs)

🛠️ **Tools**:
- `renders/_metadata/tools/README.md` (tool documentation)

📋 **Standards**:
- `renders/_metadata/audience-profiles.yaml` (audience requirements)

💬 **Questions**:
- Create GitHub issue with `[renders]` tag
- Check `renders/README.md` for overview

---

## Tips for Success

✅ **DO**:
- Read audience profiles before writing
- Use the helper script (saves time)
- Run the linter (catches issues early)
- Look at existing renders for examples
- Keep it simple and focused

❌ **DON'T**:
- Skip quality checks
- Use jargon without explaining it
- Forget image alt text
- Make assumptions about audience knowledge
- Copy-paste without adapting

---

## Common Mistakes

**Issue**: "I can't find the source AKUs"
- **Solution**: Check `domain/[path]/akus/` or `domain/[path]/` directly

**Issue**: "Linter reports warnings"
- **Solution**: Usually sentence length or missing alt text - easy to fix

**Issue**: "Don't know which audience to choose"
- **Solution**: Read `audience-profiles.yaml` - it has detailed descriptions

---

## What's Next?

After creating renders:
1. ✅ **Translate**: Create renders in other languages
2. ✅ **Expand**: Create renders for different audiences
3. ✅ **Improve**: Update existing renders based on feedback

See `renders/_metadata/RECOMMENDATIONS.md` for project roadmap.

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Time to Read**: 3 minutes  
**Next**: Read DEVELOPER_GUIDE.md for details
