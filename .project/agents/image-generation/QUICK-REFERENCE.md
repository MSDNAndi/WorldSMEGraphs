# Image Generation Workflow - Quick Reference Card

> **Version**: 1.0.0  
> **Print**: 2 pages max (optimized for quick lookup)  
> **Audience**: All users

## ⚡ TL;DR

```
Storyboard → Prompts → Images → Documents
```

**Never** create documents before images exist!

---

## 📋 Workflow Checklist

```
□ Phase 1-2: Create storyboard.yaml
□ Phase 3: Write complete prompts (8K-20K chars, NO placeholders)
□ Phase 4: Generate ALL images
□ Phase 5: Validate workflow passes
□ Phase 6: Create final documents
```

---

## 🚀 Quick Start Commands

```bash
# Validate workflow
python .project/agents/image-generation/tools/validate_workflow.py .

# Validate prompts
python .project/agents/image-generation/tools/validate_prompts.py prompts/

# Generate images (parallel)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts/all.txt --output-dir images/ --parallel 5

# Create presentation (images must exist!)
python .project/agents/image-generation/tools/presentation_generator.py \
  --slides storyboard.yaml --image-dir images/

# Install pre-commit hook
cp .project/agents/image-generation/pre-commit-hook.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

## 📖 Documentation Quick Links

| I Want To... | Read This |
|--------------|-----------|
| Start new project | [QUICK-START.md](./QUICK-START.md) (16KB) |
| Update existing | [MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md) (14KB) |
| Answer question | [FAQ.md](./FAQ.md) (15KB) |
| Understand system | [WORKFLOW-ENFORCEMENT.md](./WORKFLOW-ENFORCEMENT.md) (20KB) |
| Use tools | [tools/README.md](./tools/README.md) (5KB) |
| Navigate docs | [INDEX.md](./INDEX.md) (10KB) |

---

## ⚠️ Common Mistakes

| ❌ Wrong | ✅ Correct |
|---------|-----------|
| Create docs first | Create images first |
| Use "TODO" in prompts | Write complete prompt |
| 500-char prompts | 8,000-20,000 char prompts |
| Vague ("use blue") | Explicit ("Microsoft Blue #0078D4") |
| Generate during build | Generate before build |
| "Apply STYLE BASE" | Copy full style description |

---

## 🔧 Troubleshooting

| Error | Fix |
|-------|-----|
| "No storyboard found" | Create storyboard.yaml |
| "Contains placeholders" | Remove TODO, PLACEHOLDER, etc. |
| "Prompt too short" | Expand to 8K-20K characters |
| "Images missing" | Generate images first! |
| "Validation fails" | Read error, it tells you how to fix |

---

## 📝 Prompt Template

```
[TITLE OF IMAGE]

SCENE COMPOSITION:
[Layout, LEFT TO RIGHT flow, element positions with x%/y%]

ELEMENTS:
- Element 1: [Position, size in pixels, color #RRGGBB]
- Element 2: [Position, size, color]

STYLE:
- [Complete style description]
- [Professional/fun/academic]
- [Flat/gradient/textured]

COLORS:
- Primary: #RRGGBB
- Secondary: #RRGGBB
- Background: #RRGGBB

DIRECTIONS (SUPER EXPLICIT):
- Arrow 1: Flows LEFT TO RIGHT from x=20% to x=80%
- Arrow 2: Points clockwise from top to right

LIGHTING:
- [Light source position]
- [Shadow details]

CONSTRAINTS:
- NO text in image
- Family-friendly
- 16:9 aspect ratio
- Original artwork only

[Continue until 8,000-20,000 characters...]
```

---

## 🎯 Phase Requirements

### Phase 1-2: Storyboard
- **Format**: YAML or Markdown
- **Contains**: Title, slides/panels, educational goals
- **Time**: 30-60 minutes

### Phase 3: Prompts
- **Length**: 8,000-20,000 characters EACH
- **No**: TODO, PLACEHOLDER, "Apply STYLE BASE"
- **Yes**: Hex colors, pixel sizes, explicit directions
- **Time**: 1-3 hours

### Phase 4: Images
- **Generate**: ALL images before ANY documents
- **Parallel**: Use --parallel 5 for efficiency
- **Review**: Check each image matches intent
- **Time**: 5-30 minutes

### Phase 5: Documents
- **Prerequisite**: ALL images exist
- **Validate**: Run validate_workflow.py first
- **Create**: PPTX, PDF, HTML
- **Time**: 10-30 minutes

---

## 🛠️ Tool Reference

| Tool | Purpose | Key Flag |
|------|---------|----------|
| validate_workflow.py | Check phase order | --verbose |
| validate_prompts.py | Check quality | --min-score 70 |
| gpt_image_generator.py | Create images | --parallel 5 |
| presentation_generator.py | Create slides | --image-dir |
| pre-commit-hook.sh | Block bad commits | (auto) |

---

## 📊 Quality Targets

| Metric | Target | Why |
|--------|--------|-----|
| Prompt length | 8K-20K chars | Complete specifications |
| Placeholders | 0 | Self-contained |
| Images first | 100% | Correct workflow |
| Validation | Pass | Quality assurance |

---

## 🔑 Key Principles

1. **Order Matters**: Images BEFORE documents
2. **Complete Prompts**: NO placeholders
3. **Super Explicit**: Directions, colors, sizes
4. **Validate Early**: Check at each phase
5. **Archive Versions**: Dated subfolders

---

## 💡 Pro Tips

- **Time Investment**: 60% prompts, 30% images, 10% docs
- **Parallel Generation**: Use --parallel 5 (respects rate limits)
- **Prompt Reuse**: Copy style sections between prompts
- **Version Control**: Git for code, subfolders for archives
- **Error Messages**: Read them - they guide you to fixes

---

## 🆘 Emergency Contacts

- **New Project**: Read [QUICK-START.md](./QUICK-START.md)
- **Existing Project**: Read [MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md)
- **Questions**: Search [FAQ.md](./FAQ.md)
- **Problems**: Run validators, read error messages
- **Navigation**: Start at [INDEX.md](./INDEX.md)

---

## 📈 Success Criteria

You're doing it right if:
- ✅ Storyboard exists
- ✅ Prompts are 8K-20K chars
- ✅ No placeholders in prompts
- ✅ All images generated first
- ✅ Validation passes
- ✅ Documents created after images

---

## ⚡ One-Liner Summary

> "Create storyboard, write complete prompts (8K-20K chars, super explicit), generate ALL images, THEN build documents."

---

**Quick Reference Card v1.0.0**  
**Created**: 2026-01-08  
**For**: Image Generation Workflow Enforcement v0.3.1

**Print this card and keep it visible while working!**
