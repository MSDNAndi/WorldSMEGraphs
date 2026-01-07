# Runbook — Type 2 Endoleak Comic Assets

## 🆕 V2 WORKFLOW (Recommended) - Improved Post-PR #36

**📖 See full documentation:**
- **Quick Start**: `QUICK-REFERENCE.md` (copy-paste commands)
- **Overview**: `PROJECT-SUMMARY.md` (complete summary)
- **Detailed Guide**: `README-IMPROVED-WORKFLOW.md` (comprehensive)

**Key improvements**: Hyper-detailed prompts (8-20K chars each), zero placeholders, archived versions, better Dora-style story.

### Generate Images (V2)
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2 \
  --aspect landscape --quality high --parallel 4 --enhance
```

### Optional: Apply Narrative Improvements First
```bash
# 1. Review improved story (30 min)
less NARRATIVE-INTEGRATION-GUIDE.md

# 2. Update storyboard.json (60 min)
nano storyboard.json

# 3. Regenerate prompts (5 min)
python generate_detailed_prompts.py

# 4. Generate images with improvements
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts-v2-detailed-all-panels.txt \
  --output-dir panels-gpt-v2-narrative \
  --aspect landscape --quality high --parallel 4 --enhance
```

---

## 📦 Original V1 Workflow (PR #36)

### Prereqs
- Env vars: `AI_FOUNDRY_API_KEY`, `AI_FOUNDRY_ENDPOINT`, `GPT_IMAGE_1DOT5_ENDPOINT_URL` (verify with `env | grep AI_FOUNDRY`).
- Python 3.10+, Pillow installed (`pip install pillow`).
- Quick check: `python renders/.../comic/check_env.py`

### Generate Images (V1 - Original)
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file gpt-prompts.txt \
  --output-dir panels-gpt \
  --aspect landscape --quality high --parallel 4 --enhance --no-git
```

**Note**: V1 prompts archived in `archive/2026-01-07-original-pr36/`. Use V2 for better quality.

## Build PDF (6 panels/page)
```bash
python renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/build_gpt_pdf.py
```

## Refresh Maps & Dialogue
```bash
python renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/refresh_panel_map.py
python renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/export_dialogue.py
```

## Clean Metadata (optional, removes base64 payloads)
```bash
python - <<'PY'
import json, pathlib
base = pathlib.Path("renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/panels-gpt")
for path in base.glob("metadata_*.json"):
    data = json.load(open(path))
    if "response" in data:
        data["response_summary"] = {k: data["response"].get(k) for k in ("status", "created", "model") if k in data["response"]}
        data.pop("response")
        json.dump(data, open(path, "w"), indent=2)
        print("trimmed", path.name)
PY
```

## Outputs
- Images: `.../panels-gpt/image_*.png`
- PDF (6/page): `.../type2-endoleak-comic-gpt.pdf`
- PDF (5/page with featured panel 15 large - microbubble tracker): `.../type2-endoleak-comic-gpt-featured.pdf`
- Panel map: `.../panel-map.json` (includes alt text)
- Alt text: `.../panels-gpt/alt-text.md`
- Dialogue script: `.../dialogue.md`
- Validation: `python renders/.../comic/validate_comic.py`
  - Expected: `Prompts: 32 (valid format: 32)`, `Images: 32`, `Map entries: 32`, `Alt text entries: 32`, PDFs present, ✅ OK.
- QA: see `qa-checklist.md`.
