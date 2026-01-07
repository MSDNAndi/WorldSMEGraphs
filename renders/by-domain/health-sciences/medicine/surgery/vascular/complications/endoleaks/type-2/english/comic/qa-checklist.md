# QA Checklist — Type 2 Endoleak Comic

- [ ] Follow regeneration steps in `runbook.md` if assets were refreshed.
- [ ] `python validate_comic.py` reports ✅ and counts 32 prompts/images/map entries/alt-text.
- [ ] `check_env.py` shows required image-generation secrets are present.
- [ ] Open `panels-gpt/image_001_20260107_013733_e1ae2fc8.png` to verify speech bubble legibility.
- [ ] Capture a screenshot of the sample panel above for UI review as needed.
- [ ] Open `type2-endoleak-comic-gpt.pdf` to confirm 6-panel layout order is correct.
- [ ] Open `type2-endoleak-comic-gpt-featured.pdf` to confirm panel 15 (microbubble tracker) is enlarged and correctly placed.
- [ ] `panel-map.json` lists 32 entries and marks panel 15 as `featured: true`.
- [ ] `alt-text.md` contains 32 numbered descriptions and mentions featured panel.
