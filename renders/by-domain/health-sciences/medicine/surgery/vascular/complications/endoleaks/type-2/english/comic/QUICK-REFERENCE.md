# Quick Reference Card - Comic Generation Workflow v2

## 🚀 Generate Images (Most Common Task)

```bash
cd renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic

# Standard generation (all 32 panels)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2 \
  --aspect landscape --quality high --parallel 4 --enhance

# Duration: ~12-15 minutes
```

## 📖 Key Documents (Read These First)

| Priority | File | Purpose | Time |
|----------|------|---------|------|
| 🥇 | `PROJECT-SUMMARY.md` | Complete overview | 5 min |
| 🥈 | `README-IMPROVED-WORKFLOW.md` | Detailed workflow | 10 min |
| 🥉 | `BEFORE-AFTER-COMPARISON.md` | See improvements | 8 min |

## 🎨 Apply Narrative Improvements

```bash
# 1. Review enhanced dialogue
less dialogue-enhanced.md

# 2. Update storyboard with improvements
nano storyboard.json

# 3. Regenerate prompts
python generate_detailed_prompts.py

# 4. Generate images
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2-narrative \
  --aspect landscape --quality high --parallel 4 --enhance
```

## 📦 Build PDF

```bash
# Standard (6 panels/page)
python build_gpt_pdf.py --input-dir panels-gpt-v2

# Featured panel (Panel 15 large)
python build_gpt_pdf.py --input-dir panels-gpt-v2 --feature-panel 15
```

## 🔍 Validate Output

```bash
# Check all components
python validate_comic.py --version v2

# Expected output:
# ✅ Prompts: 32 (valid)
# ✅ Images: 32
# ✅ PDF present
# ✅ All checks passed
```

## 📊 Prompt Specs Quick Reference

**Average per panel:** 10,421 characters  
**Range:** 8,000 - 20,000 characters  
**Total file:** 333 KB (all 32 panels)  
**Placeholders:** ZERO  

**Each prompt contains:**
1. Style Foundation (1,500-2,000 chars)
2. Character Specs (2,000-3,000 chars EACH)
3. Scene Composition (1,500-2,000 chars)
4. Visual Elements (1,000-1,500 chars)
5. Speech Bubbles (1,500-2,000 chars)
6. Lighting (800-1,000 chars)
7. Color Palette (500-800 chars)
8. Technical Specs (400-600 chars)

## 🎯 Character Consistency Checks

**Camila:**
- Teal vest/shorts #20B2AA
- Purple backpack #9370DB
- Sunflower patch RIGHT chest
- Braid LEFT shoulder
- Skin #D4A574

**Camilo:**
- Green vest #3CB371
- Orange backpack #FFA500
- Topo map patch RIGHT chest
- Khaki pants #C3B091
- Skin #C19A6B

**Diego:**
- Orange vest #FF8C00
- Green backpack #90EE90
- Compass patch RIGHT chest
- Navy pants #000080
- Skin #B8956A
- Glasses (black frames)

## ⚡ Common Commands

```bash
# Check environment
env | grep AI_FOUNDRY

# Regenerate single panel
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "[paste panel prompt]" \
  --output-dir panels-gpt-v2 \
  --filename image_012_regenerated.png

# Compare with original
diff gpt-prompts.txt gpt-prompts-v2-detailed-all-panels.txt

# Archive new version
mkdir -p archive/2026-01-XX-description
cp -r panels-gpt-v2 archive/2026-01-XX-description/
```

## 🐛 Troubleshooting

**No images generated?**
→ Check `env | grep AI_FOUNDRY` for API keys

**Inconsistent characters?**
→ Verify using `gpt-prompts-v2-detailed-all-panels.txt` (not old file)

**Text not readable?**
→ Increase `--quality high` flag was used

**Wrong colors?**
→ Check hex codes in prompts match specifications

**Placeholders in prompts?**
→ You're using old file; use `gpt-prompts-v2-detailed-all-panels.txt`

## 📁 Directory Structure

```
comic/
├── PROJECT-SUMMARY.md                      ⭐ Start here
├── README-IMPROVED-WORKFLOW.md             📖 Full guide
├── BEFORE-AFTER-COMPARISON.md              📊 Metrics
├── NARRATIVE-INTEGRATION-GUIDE.md          🎭 Story improvements
├── PROMPT-ENGINEERING-GUIDE.md             🛠️ Methodology
│
├── gpt-prompts-v2-detailed-all-panels.txt  ⚙️ USE THIS
├── generate_detailed_prompts.py            🔧 Generator script
│
├── storyboard.json                         📝 Source of truth
├── panels-gpt-v2/                          🖼️ New images (after generation)
├── archive/                                📦 Previous versions
│   └── 2026-01-07-original-pr36/
└── [other files...]
```

## 🎓 Key Improvements

| What | Before | After |
|------|--------|-------|
| Prompt length | 1.5-3K | 8-20K chars |
| Placeholders | Yes | Zero |
| Character specs | Varies | Identical all panels |
| Colors | Names | Hex codes |
| Archive | Git only | Folders + docs |

## ⏱️ Time Estimates

| Task | Duration |
|------|----------|
| Read summary | 5 min |
| Generate images | 12-15 min |
| Build PDF | 2 min |
| Validate | 1 min |
| **Total (quick)** | **~20 min** |
| | |
| Apply narrative | +2 hours |
| Full integration | +1-2 weeks |

## 💡 Quick Wins

**60% impact in 1 hour:**
1. Update Panel 1, 14, 31 dialogue
2. Regenerate prompts
3. Generate images
4. Build PDF

## 📞 Getting Help

**Workflow questions?** → `README-IMPROVED-WORKFLOW.md`  
**Prompt questions?** → `PROMPT-ENGINEERING-GUIDE.md`  
**Story questions?** → `NARRATIVE-INTEGRATION-GUIDE.md`  
**Metrics/ROI?** → `BEFORE-AFTER-COMPARISON.md`

---

**Version:** 2.0  
**Status:** Ready to use  
**Last Updated:** 2026-01-07

**Copy-paste this for quick image generation:**
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2 \
  --aspect landscape --quality high --parallel 4 --enhance
```
