# Runbook — Type 2 Endoleak Comic Assets

## Prereqs
- Env vars: `AI_FOUNDRY_API_KEY`, `AI_FOUNDRY_ENDPOINT`, `GPT_IMAGE_1DOT5_ENDPOINT_URL` (verify with `env | grep AI_FOUNDRY`).
- Python 3.10+, Pillow installed (`pip install pillow`).

## Generate Images
```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/gpt-prompts.txt \
  --output-dir renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic/panels-gpt \
  --aspect landscape --quality high --parallel 4 --enhance --no-git
```

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
- PDF (5/page with featured panel 15 large): `.../type2-endoleak-comic-gpt-featured.pdf`
- Panel map: `.../panel-map.json` (includes alt text)
- Alt text: `.../panels-gpt/alt-text.md`
- Dialogue script: `.../dialogue.md`
- Validation: `python renders/.../comic/validate_comic.py`
