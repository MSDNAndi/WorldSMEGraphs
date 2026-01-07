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

## Outputs
- Images: `.../panels-gpt/image_*.png`
- PDF: `.../type2-endoleak-comic-gpt.pdf`
- Panel map: `.../panel-map.json` (includes alt text)
- Alt text: `.../panels-gpt/alt-text.md`
- Dialogue script: `.../dialogue.md`
