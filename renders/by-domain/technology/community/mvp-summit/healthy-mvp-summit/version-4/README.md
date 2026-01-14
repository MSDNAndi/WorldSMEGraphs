# Version 4: Campus Wisdom

## A Walk Through Wellness at the Microsoft MVP Summit

**Created:** 2026-01-13  
**Status:** Story Development Complete, Ready for Image Generation  
**Panels:** 48  
**Style:** 1950s American Comic Book

---

## Overview

Version 4 takes a unique approach compared to the first three versions:

| Feature | Version 4 | Versions 1-3 |
|---------|-----------|--------------|
| **Focus** | All 10 AKU topics | Broader wellness themes |
| **Structure** | Walking tour narrative | Multi-day/event-based |
| **Character Descriptions** | Exact photo-based | Original artistic |
| **Setting** | Campus → downtown bar | Full conference experience |
| **Ending** | Sparkling water toast | Varies |

---

## Story Concept

Two technology veterans—old friends reuniting at the Summit—walk the beautiful Microsoft campus sharing wisdom about conference wellness. Their friendship and mutual care naturally weave educational content into an entertaining narrative.

### Key Differentiators

1. **AKU-Aligned Content**: Every scene directly maps to one of the 10 conference wellness AKUs
2. **Accurate Character Visuals**: Uses exact descriptions from actual photographs
3. **No Alcohol Consumption**: Bar scene shows only sparkling water with lime
4. **Walking Tour Structure**: Organic flow through campus to evening in Bellevue
5. **Friendship Focus**: Emphasizes genuine relationship over just information

---

## Educational Topics (10 AKUs)

| Scene | AKU | Topic |
|-------|-----|-------|
| Scene 2 | cw-001 | Hydration & Cognitive Performance |
| Scene 3 | cw-002 | Jet Lag & Circadian Disruption |
| Scene 4 | cw-003 | Decision Fatigue |
| Scene 5 | cw-009 | FOMO Anxiety Management |
| Scene 6 | cw-007 | Eye Strain & 20-20-20 Rule |
| Scene 7 | cw-006 | Sitting Health Risks & Movement |
| Scene 8 | cw-004 | Social Energy Management |
| Scene 9 | cw-005 | Power Nap Science |
| Scene 10 | cw-008 | Alcohol Moderation |
| Scene 2 | cw-010 | Caffeine Strategic Timing |

---

## Character Specifications

### Andreas Erben

> Caucasian male in his late 40s to early 50s, with short thinning sandy-blonde/light brown hair that is receding at the temples and thin on top. He wears prominent rectangular dark-framed glasses with thick black plastic frames. He has a clean-shaven face with an oval-rectangular face shape, light grey-blue eyes, and a warm genuine smile. Fair complexion with natural smile lines. Wearing a dark charcoal grey vest over a light blue button-down shirt with a conference lanyard.

**Role:** Experienced conference veteran who shares wellness wisdom through friendly conversation.

### Marco Casalaina

> Caucasian male in his mid-40s to early 50s, completely bald with a smooth shaved head - this is his most distinctive feature. He has no glasses, a clean-shaven face with a slightly rounded/oval face shape, and friendly blue-grey eyes. He has a warm, genuine smile showing teeth, with a fair complexion. Wearing a dark navy blue blazer over a white open-collar dress shirt.

**Role:** Curious listener learning through the conversation, representing typical conference attendee.

---

## Files

### Story Development

| File | Purpose | Status |
|------|---------|--------|
| `story-development/01-story-idea.md` | Complete story outline with themes, arc, scenes | ✅ Complete |
| `story-development/02-narrative.md` | Full prose narrative (~2,450 words) | ✅ Complete |
| `story-development/03-panel-planning.md` | 48-panel scene-by-scene breakdown | ✅ Complete |

### Comic Generation

| File | Purpose | Status |
|------|---------|--------|
| `comic/prompts-single-line.txt` | 48 image generation prompts | ✅ Complete |
| `comic/panels-gpt/` | Generated images | ⏳ Pending |
| `comic/continuous-story-view.md` | Images with dialogue | ⏳ Pending |
| `comic/pictures-only-view.md` | Images gallery | ⏳ Pending |

---

## Next Steps

1. **Image Generation**: Run `prompts-single-line.txt` through GPT Image 1.5
2. **Quality Review**: Check character consistency across panels
3. **View Creation**: Create continuous-story-view.md and pictures-only-view.md
4. **Final Review**: Ensure educational content is clear and engaging

---

## Image Generation Command

```bash
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file renders/by-domain/technology/community/mvp-summit/healthy-mvp-summit/version-4/comic/prompts-single-line.txt \
  --output-dir renders/by-domain/technology/community/mvp-summit/healthy-mvp-summit/version-4/comic/panels-gpt \
  --parallel 8 \
  --aspect landscape \
  --quality high
```

---

## Technical Notes

### Panel Aspect Ratios
- **Landscape (16:9)**: 1792 × 1024 pixels for wide shots
- **Square (1:1)**: 1024 × 1024 pixels for close-ups

### Style Consistency
- 1950s American comic book style throughout
- Bold black outlines
- Ben-Day dot shading
- Flat colors with limited palette
- Classic speech bubbles with tails

### Key Visual Requirements
- **Andreas**: ALWAYS show rectangular dark-framed glasses, thinning sandy-blonde hair
- **Marco**: ALWAYS show completely bald shaved head, no glasses
- **Both**: Clean-shaven, friendly expressions

---

*Version 4 developed as part of Issue #47*
