# Type 2 Endoleak Comic Redesign: Implementation Checklist

**Version**: 1.0  
**Date**: 2026-01-07  
**Purpose**: Step-by-step guide to implement pedagogical narrative enhancements

---

## Overview

This checklist helps you apply the narrative redesign from:
- `narrative-redesign-pedagogy.md` (strategy and principles)
- `dialogue-enhanced.md` (panel-by-panel implementation)

**Goal**: Transform linear fact-delivery comic → emotionally engaging learning journey

**Estimated Time**: 2-4 weeks for full implementation (depending on whether you regenerate images)

---

## Phase 1: Dialogue Updates (High Priority)
*Can be done WITHOUT regenerating images*

### Step 1.1: Update `storyboard.json`
- [ ] **Panel 1-2**: Replace dialogue with overconfident tone (establish false confidence)
- [ ] **Panel 3-5**: Add confusion moments, questioning dialogue (learning through struggle)
- [ ] **Panel 6**: Add "we need help" moment (modeling asking for mentorship)
- [ ] **Panel 9**: Replace with Socratic questions from Dr. Erben (scaffolding thinking)
- [ ] **Panel 14-16**: Add innovation spark language (transition to research creation)
- [ ] **Panel 17**: Add feasibility reality check (innovation vs. execution)
- [ ] **Panel 23**: Add vulnerability ("I'm nervous!") (authentic research emotions)
- [ ] **Panel 25**: Deepen ethics dialogue (values, not checkbox)
- [ ] **Panel 30**: Add growth reflection with Dr. Erben (mentor validates transformation)
- [ ] **Panel 31**: Emphasize patient impact emotionally (research = lives)
- [ ] **Panel 32**: Add inspirational call-to-action to reader (invitation)

**How to do it**:
1. Open `storyboard.json`
2. For each panel, replace `dialogue` array with enhanced version from `dialogue-enhanced.md`
3. Keep speaker names and structure identical
4. Test by running `export_dialogue.py` to regenerate `dialogue.md`

**Verification**:
```bash
python export_dialogue.py
diff dialogue.md dialogue-enhanced.md  # Should match key emotional beats
```

---

### Step 1.2: Add Interactive Elements
- [ ] **Panel 1**: Add thought bubble: "Have YOU ever felt overconfident?"
- [ ] **Panel 3**: Add question: "What OTHER paths could blood take?"
- [ ] **Panel 5**: Add decision prompt: "How would YOU decide?"
- [ ] **Panel 7**: Add visual challenge: "Can YOU spot the difference?"
- [ ] **Panel 8**: Add hypothesis prompt: "Which vessel would YOU suspect?"
- [ ] **Panel 9**: Add reflection: "What would YOU ask Dr. Erben?"
- [ ] **Panel 14**: Add brainstorm: "What else would YOU measure?"
- [ ] **Panel 15**: Add methodology: "How would YOU test this?"
- [ ] **Panel 19**: Add communication: "How would YOU explain this?"
- [ ] **Panel 23**: Add hypothesis creation: "What would YOUR hypothesis be?"
- [ ] **Panel 28**: Add teaching challenge: "Can YOU explain it now?"
- [ ] **Panel 29**: Add vision: "What technology would YOU invent?"
- [ ] **Panel 32**: Add inspiration: "What mystery would YOU investigate?"

**How to add**:
1. In `storyboard.json`, add new dialogue object with `"speaker": "Reader Prompt"`
2. In image prompts (if regenerating), specify thought bubble/question box style
3. Alternatively, add as text overlay in PDF generation script

---

## Phase 2: Visual Enhancements (Medium Priority)
*Requires updating visual_prompt in storyboard.json; may or may not need image regeneration*

### Step 2.1: Character Expression Updates
Update `visual_prompt` field in `storyboard.json` for emotion:

- [ ] **Panel 1-2**: Add "overconfident smirks," "casual body language"
- [ ] **Panel 3**: Add "furrowed brows," "confused expressions," "scratching head"
- [ ] **Panel 4**: Add "lightbulb over Camila," "aha face"
- [ ] **Panel 5**: Add "serious expressions," "concerned faces" (tone shift)
- [ ] **Panel 6**: Add "overwhelmed posture," "hands on head," "sweat drops"
- [ ] **Panel 7**: Add "excited pointing," "magnifying glass," "discovery expressions"
- [ ] **Panel 9**: Add "leaning forward engaged," "note-taking," "Dr. Erben warm smile"
- [ ] **Panel 14**: Add "LARGE lightbulb," "jumping/excited gestures"
- [ ] **Panel 17**: Add "concerned expressions," "question marks overhead"
- [ ] **Panel 23**: Add "nervous expressions," "coffee cups" (working session)
- [ ] **Panel 25**: Add "serious reflective faces," "protective stance around consent"
- [ ] **Panel 30**: Add "proud posture," "high-five moment," "transformation montage"
- [ ] **Panel 31**: Add "tears of joy," "hug," "celebration balloons"
- [ ] **Panel 32**: Add "triumphant but humble," "open door with new interns"

**How to update**:
1. Open `storyboard.json`
2. Append emotional cues to `visual_prompt` field
3. If regenerating images: use `gpt_image_generator.py` with updated prompts
4. If NOT regenerating: document for future version

---

### Step 2.2: Visual Metaphors & Storytelling Elements
Add to `visual_prompt` field:

- [ ] **Panel 2**: Add "Dr. Erben's complex diagram visible in background (ignored)"
- [ ] **Panel 4**: Add "pressure gradient arrows with HIGH→LOW labels"
- [ ] **Panel 8**: Add "upstream tracing visualization (river metaphor)"
- [ ] **Panel 12**: Add "catheter as snake navigating maze"
- [ ] **Panel 13**: Add "danger zone highlighted around nerve roots (yellow caution)"
- [ ] **Panel 14**: Add "Known vs Unknown columns on whiteboard"
- [ ] **Panel 24**: Add "coffee cups multiplying (time passage humor)"
- [ ] **Panel 27**: Add "'Preliminary' watermark across graph"
- [ ] **Panel 29**: Add "timeline: Today → 5yrs → 10yrs" with tech evolution
- [ ] **Panel 30**: Add "Panel 1 vs Panel 30 faces comparison" (transformation)

---

## Phase 3: Story Structure Verification (Essential)

### Step 3.1: 8-Beat Story Spine Check
Verify each panel maps to correct story beat:

- [ ] **Panels 1-2**: Beat 1 - Ordinary World (overconfident start) ✓
- [ ] **Panels 3-5**: Beat 2 - Call to Adventure (complexity confrontation) ✓
- [ ] **Panels 6-8**: Beat 3 - Refusal (overwhelmed, seeking help) ✓
- [ ] **Panel 9**: Beat 4 - Meeting Mentor (Dr. Erben scaffolds) ✓
- [ ] **Panels 10-16**: Beat 5 - Crossing Threshold (clinical + research challenges) ✓
- [ ] **Panels 17-24**: Beat 6 - Tests & Challenges (reality checks) ✓
- [ ] **Panels 25-28**: Beat 7 - Inmost Cave (ethics, data, consolidation) ✓
- [ ] **Panels 29-32**: Beat 8 - Return with Elixir (transformation, impact, inspiration) ✓

**How to verify**:
Read through updated `storyboard.json` and check:
- Does each section have the right emotional tone?
- Are challenges present in Beats 3, 6, 7?
- Is transformation visible in Beat 8?

---

### Step 3.2: Emotional Arc Check
Plot emotional energy across panels:

| Panel Range | Target Emotion | Check |
|-------------|----------------|-------|
| 1-2 | High (overconfident) | [ ] |
| 3-5 | Med-High (curious, worried) | [ ] |
| 6-8 | Med (overwhelmed → discovery) | [ ] |
| 9 | High (validated) | [ ] |
| 10-13 | Med-High (problem-solving) | [ ] |
| 14-16 | High (innovation breakthrough) ⚡ | [ ] |
| 17-19 | Med (reality check) | [ ] |
| 20-22 | Med-High (application) | [ ] |
| 23-24 | Med (nervous anticipation) | [ ] |
| 25-26 | Med-Low (ethical sobering) | [ ] |
| 27-28 | Med-High (cautious optimism) | [ ] |
| 29 | High (visionary) | [ ] |
| 30-31 | High (proud, emotional) 🎉 | [ ] |
| 32 | High (inspired) | [ ] |

**Verification**: Read dialogue aloud—does emotional energy match target?

---

## Phase 4: Character Development Check

### Step 4.1: Verify Character Arcs
Each character should show growth:

**Camila (The Questioner)**
- [ ] **Start** (P1-2): Dismissive of complexity ✓
- [ ] **Challenge** (P3-4): Realizes she doesn't understand ✓
- [ ] **Growth** (P9, 14): Asks deeper "why" questions ✓
- [ ] **Mastery** (P28, 30): Teaches others to question ✓
- [ ] **Signature Moment** (P4): "¡Momento! Pressure gradients!" ✓

**Camilo (The Systematizer)**
- [ ] **Start** (P1-2): Wants simple answers, impatient ✓
- [ ] **Challenge** (P17, 24): Discovers patience required ✓
- [ ] **Growth** (P23): Designs rigorous protocol ✓
- [ ] **Mastery** (P26, 28): Values methodology deeply ✓
- [ ] **Signature Moment** (P23): "I'm nervous!" (vulnerability) ✓

**Diego (The Humanist)**
- [ ] **Start** (P1-2): Data-focused, clinical ✓
- [ ] **Challenge** (P19): Realizes patients are people ✓
- [ ] **Growth** (P20-22): Balances rigor with empathy ✓
- [ ] **Mastery** (P31): "Every data point has a face" ✓
- [ ] **Signature Moment** (P31): Emotional patient connection ✓

**Dr. Erben (The Mentor)**
- [ ] Asks questions, doesn't give answers (Socratic) ✓
- [ ] Validates struggle as part of learning ✓
- [ ] Introduces next challenge (Type 3) showing growth ✓

---

## Phase 5: Pedagogical Quality Check

### Step 5.1: Bloom's Taxonomy Progression
Verify learning moves through levels:

- [ ] **Remember** (P3-5): Define Type 2, recall criteria ✓
- [ ] **Understand** (P6-8): Explain mechanism, compare phases ✓
- [ ] **Apply** (P10-13): Choose intervention based on scenarios ✓
- [ ] **Analyze** (P14-18): Identify gaps, critique data ✓
- [ ] **Evaluate** (P19-27): Judge ethics, assess results ✓
- [ ] **Create** (P14-16, 23-24, 29): Design studies, envision future ✓

**Verification**: Can a reader demonstrate each level after reading?

---

### Step 5.2: Interactive Engagement Check
Count interactive prompts (target: 10+):

1. [ ] Panel 1: Overconfidence reflection
2. [ ] Panel 3: Alternative paths brainstorm
3. [ ] Panel 5: Decision-making
4. [ ] Panel 7: Visual comparison challenge
5. [ ] Panel 8: Vessel identification
6. [ ] Panel 9: Question formulation
7. [ ] Panel 14: Innovation brainstorm
8. [ ] Panel 15: Methodology design
9. [ ] Panel 19: Communication skill
10. [ ] Panel 23: Hypothesis creation
11. [ ] Panel 27: Sample size critique
12. [ ] Panel 28: Teaching challenge
13. [ ] Panel 29: Technology vision
14. [ ] Panel 32: Research inspiration

**Target**: 10+ prompts ✅ (14 prompts implemented)

---

## Phase 6: Technical Accuracy Check
Ensure scientific rigor maintained:

### Clinical Accuracy
- [ ] Type 2 definition correct (retrograde collateral flow) ✓
- [ ] CTA protocol accurate (arterial + delayed phases) ✓
- [ ] Sac growth threshold (>5mm) evidence-based ✓
- [ ] Embolization techniques accurate (coils, Onyx) ✓
- [ ] Routes correct (transarterial, translumbar) ✓
- [ ] Follow-up intervals realistic (6wk, 6mo, 1yr, 2yr) ✓

### Research Methods
- [ ] Hypothesis format correct ✓
- [ ] Power calculation realistic (n=34, 80%, α=0.05) ✓
- [ ] IRB/ethics accurate ✓
- [ ] Data management (REDCap) appropriate ✓
- [ ] Timeline realistic (18-24 months) ✓

### Novel Research Elements
- [ ] CEUS microbubble concept plausible ✓
- [ ] Pressure monitoring feasible (with caveats noted) ✓
- [ ] Image fusion realistic ✓

**Verification**: Have domain expert (vascular surgeon) review

---

## Phase 7: User Testing (Recommended)

### Step 7.1: Pilot Testing
Test with 5-10 research interns:

**Pre-Comic Assessment**
- [ ] Quiz: Type 2 endoleak mechanism (baseline)
- [ ] Survey: Confidence in research skills (1-10)
- [ ] Survey: Interest in vascular surgery (1-10)

**Post-Comic Assessment**
- [ ] Quiz: Type 2 endoleak mechanism (improvement?)
- [ ] Survey: Confidence in research skills (1-10, change?)
- [ ] Survey: Interest in vascular surgery (1-10, change?)
- [ ] Survey: Emotional engagement (did you care about characters?)
- [ ] Survey: Inspiration (would you consider research?)

**Qualitative Feedback**
- [ ] What panel resonated most? Why?
- [ ] What was confusing?
- [ ] Did you feel the characters' journey?
- [ ] Did interactive prompts engage you?
- [ ] Would you recommend to others?

---

### Step 7.2: Iterate Based on Feedback
- [ ] Identify panels with low comprehension → clarify
- [ ] Identify emotional beats that didn't land → revise
- [ ] Test interactive prompts → adjust if unclear
- [ ] A/B test different dialogue options for key panels

---

## Phase 8: Final Polish

### Step 8.1: Consistency Check
- [ ] Character voices consistent (Camila's Spanish, Diego's empathy)
- [ ] Spanish/English code-switching natural
- [ ] Terminology consistent across panels
- [ ] Visual style consistent
- [ ] Emotional progression smooth (no jarring jumps)

### Step 8.2: Accessibility
- [ ] Alt text for all images (in `panel-map.json`)
- [ ] High contrast for readability
- [ ] Font size adequate (especially in speech bubbles)
- [ ] Color-blind friendly color scheme
- [ ] Screen reader compatible PDF

### Step 8.3: Distribution Formats
- [ ] PDF (6 panels/page) - `build_gpt_pdf.py` ✓
- [ ] PDF (featured layout with key panels emphasized)
- [ ] Web-friendly (HTML with embedded images)
- [ ] Print-friendly (high-res)
- [ ] Mobile-optimized (vertical scroll)

---

## Timeline Estimate

| Phase | Tasks | Time | Priority |
|-------|-------|------|----------|
| 1 | Dialogue updates | 2-3 days | **HIGH** |
| 2 | Visual enhancements | 3-5 days | Medium |
| 3 | Story structure verification | 1 day | **HIGH** |
| 4 | Character development check | 1 day | **HIGH** |
| 5 | Pedagogical quality check | 1 day | **HIGH** |
| 6 | Technical accuracy check | 2 days | **HIGH** |
| 7 | User testing | 1-2 weeks | Medium |
| 8 | Final polish | 2-3 days | Medium |

**Total**: 2-4 weeks (depending on image regeneration)

---

## Quick Start (Minimum Viable Enhancement)

**If you only have 2 days**, prioritize these changes:

### Day 1: Critical Dialogue Updates
- [ ] Panel 1-2: Overconfident tone
- [ ] Panel 3-5: Confusion moments
- [ ] Panel 9: Socratic mentoring
- [ ] Panel 14-15: Innovation breakthrough
- [ ] Panel 23: Vulnerability
- [ ] Panel 31-32: Impact + inspiration

### Day 2: Interactive Elements + Character Arc
- [ ] Add 5 key interactive prompts (P1, P7, P23, P28, P32)
- [ ] Verify character signature moments present
- [ ] Check 8-beat structure
- [ ] Export new `dialogue.md`
- [ ] Regenerate PDF with `build_gpt_pdf.py`

**Result**: 60-70% of impact with 10% of time investment

---

## Success Criteria

Your enhanced comic is ready when:

✅ **Readers care** about the characters (emotional investment)  
✅ **Readers understand** Type 2 endoleaks (learning objectives met)  
✅ **Readers engage** with interactive prompts (active participation)  
✅ **Readers feel inspired** to consider research (motivation)  
✅ **Experts approve** technical accuracy (scientific rigor)  
✅ **Characters grow** visibly from panel 1 to 32 (transformation)  
✅ **Story flows** with clear beginning, middle, end (8-beat structure)  

---

## Resources

- **Strategy Document**: `narrative-redesign-pedagogy.md` (39KB, comprehensive)
- **Implementation Guide**: `dialogue-enhanced.md` (48KB, panel-by-panel)
- **This Checklist**: `implementation-checklist.md` (you are here)
- **Current Files**: 
  - `storyboard.json` (authoritative panel data)
  - `dialogue.md` (current dialogue)
  - `gpt-prompts.txt` (image generation prompts)
  - `panels-gpt/` (generated images)

---

## Support

Questions? Check the pedagogy agent for guidance:
- `.github/agents/pedagogy.agent.md` - Full agent specifications
- `@pedagogy` - Invoke for specific questions

---

**Version**: 1.0  
**Created**: 2026-01-07  
**Author**: @pedagogy agent  
**Next Review**: After Phase 7 user testing
