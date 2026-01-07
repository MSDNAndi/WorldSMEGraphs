---
source: domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2
audience: research-interns
language: english (with spanish cues)
panels: 32
style: dora-inspired, explorer tone, speech-bubble only
---

# Type 2 Endoleak Research Comic — Structured Storyboard

## Goals
- Keep the story self-explanatory through speech bubbles only.
- Embed scientific rigor: sac growth thresholds, source-vessel mapping, imaging phases, and embolization options.
- Highlight novel ideas: CEUS microbubble persistence, dual-phase CTA overlay, sac pressure probe.
- Maintain the Dora-style exploration vibe without copying characters.

## Story Spine (8 beats)
1. **Mission Brief** — Meet the trio, set the 30+ panel target.
2. **Define the Leak** — Retrograde collateral inflow vs seal failure.
3. **Risk Signal** — Sac growth >5 mm or diameter >60 mm triggers action.
4. **See the Flow** — CTA arterial + delayed, source-vessel hunt.
5. **Choose the Route** — Observation vs embolization; transarterial vs translumbar.
6. **Novel Research** — Microbubble timing, CTA overlay, pressure probe.
7. **Protocol Build** — Sample size, IRB, data capture, outcome tracking.
8. **Payoff** — Successful case, poster with Dr. Erben, and future paper.

## Panel List (concise)
1. Courtyard kickoff  
2. Goal map  
3. Define Type 2  
4. Flow mechanism  
5. Risk signal (sac growth)  
6. Imaging plan (arterial + delayed)  
7. CTA frames comparison  
8. Source vessel hunt  
9. Check-in with Dr. Erben  
10. Observation path  
11. Intervention path  
12. Transarterial route  
13. Translumbar route  
14. Novel idea spark (microbubbles)  
15. Microbubble tracker (wash-in/out)  
16. Dual-phase CTA overlay  
17. Pressure monitoring probe  
18. Outcome data wall  
19. Patient counseling  
20. Sterile prep  
21. Coil deployment  
22. Post-procedure CTA  
23. Pilot study draft  
24. Sample size debate  
25. Ethics reminder (IRB, bilingual consent)  
26. Data capture (REDCap)  
27. Result teaser (correlation)  
28. Teaching moment (3 steps)  
29. Future tech dream (AR guidance)  
30. Wrap-up with Dr. Erben  
31. Patient success follow-up  
32. Future paper and sharing

## Visual & Prompt Notes
- Bright pastel backgrounds, bold outlines, playful arrows like a map.
- Speech bubbles carry all explanations; no side narration.
- Clear labels on sac growth thresholds, imaging phases, and vessels.
- Characters: Camilo (Colombia), Diego (Colombia), Camila (Ecuador), plus Dr. Young Erben cameo.
- Science anchors: retrograde collateral inflow, delayed blush, sac growth ≥5 mm trigger, embolization options, follow-up cadence.

## Narration Tone (compelling + scientific)
- Explorer energy (“¡Vamos!”) paired with precise thresholds and imaging phase names.
- Each research insight voiced in-character (no omniscient narrator).
- Humor via map arrows, stickers, and lightbulb “aha” beats; rigor via sac diameter numbers and CTA phase callouts.
- Bilingual touches (English/Spanish) to keep voice authentic to the characters.

## Files
- `storyboard.json` — authoritative panel data (titles, prompts, dialogue).
- `gpt-prompts.txt` — explicit prompts for GPT Image 1.5 (one per panel).
- `panels-gpt/` — GPT-generated panels from `.project/agents/image-generation/tools/gpt_image_generator.py`.
- `build_gpt_pdf.py` — assembles GPT panels into `type2-endoleak-comic-gpt.pdf` (6 panels/page).
- `comic-fluid.md` — fluid reading format embedding GPT panels.
- `generate_comic.py` / `panels/` — prior placeholder render path retained for fallback.

## Generation Notes
- Secrets available: `AI_FOUNDRY_API_KEY`, `AI_FOUNDRY_ENDPOINT`, `GPT_IMAGE_1DOT5_ENDPOINT_URL` (verified via environment).
- Generation command used:
  ```
  python .project/agents/image-generation/tools/gpt_image_generator.py \
    --prompt-file gpt-prompts.txt \
    --output-dir panels-gpt \
    --aspect landscape --quality high --parallel 4 --enhance
  ```
- PDF assembly:
  ```
  python build_gpt_pdf.py
  ```
