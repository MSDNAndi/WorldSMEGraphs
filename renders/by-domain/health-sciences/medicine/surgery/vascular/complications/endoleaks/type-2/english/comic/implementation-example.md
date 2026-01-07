# Implementation Example: Updating storyboard.json

**Purpose**: Step-by-step guide showing HOW to apply enhanced dialogue to storyboard.json  
**Date**: 2026-01-07  
**For**: Developers, comic editors

---

## Overview

This document shows the EXACT steps to update `storyboard.json` with enhanced dialogue from the narrative redesign. Includes before/after JSON examples and validation steps.

---

## Prerequisites

1. **Backup current file**:
   ```bash
   cp storyboard.json storyboard.json.backup
   ```

2. **Required files**:
   - `storyboard.json` (current)
   - `dialogue-enhanced.md` (enhanced dialogue source)
   - JSON editor (VSCode, vim, or preferred editor)

3. **Optional tools**:
   - `export_dialogue.py` (to verify changes)
   - `validate_comic.py` (to check structure)

---

## Step-by-Step: Panel 1 Update

### Step 1: View Current Panel 1

**Current storyboard.json** (Panel 1):
```json
{
  "panel": 1,
  "title": "Clinic Courtyard Kickoff",
  "setting": "Bright hospital courtyard with river-like path and arrow markers like a map",
  "visual_prompt": "Three cheerful Latin American research interns in colorful explorer outfits outside Mayo Clinic Jacksonville, holding clipboards; Dora-style bold outlines, speech bubbles, playful arrows pointing toward the aorta diagram.",
  "dialogue": [
    {
      "speaker": "Camila",
      "text": "Hola! Ready to map Type 2 endoleaks?"
    },
    {
      "speaker": "Camilo",
      "text": "Sí, let's explore the hidden flow paths!"
    },
    {
      "speaker": "Diego",
      "text": "Dr. Erben wants clear visuals and data."
    }
  ]
}
```

**Problems**:
- Generic enthusiasm
- No personality
- No emotional hook
- Missing interactive element

---

### Step 2: Apply Enhanced Dialogue

**Enhanced storyboard.json** (Panel 1):
```json
{
  "panel": 1,
  "title": "Clinic Courtyard Kickoff",
  "setting": "Bright hospital courtyard with river-like path and arrow markers like a map",
  "visual_prompt": "Three cheerful Latin American research interns in colorful explorer outfits outside Mayo Clinic Jacksonville, holding clipboards; Dora-style bold outlines; characters have overconfident smirks; Dr. Erben visible in background with complex diagram (foreshadowing); playful arrows pointing toward simple aorta sketch on their clipboards.",
  "dialogue": [
    {
      "speaker": "Camila",
      "text": "Hola! Type 2 endoleaks? We've read the papers—esto es fácil!"
    },
    {
      "speaker": "Camilo",
      "text": "¡Sí! Just map the vessels and we're done by lunch, right?"
    },
    {
      "speaker": "Diego",
      "text": "Dr. Erben said this is 'more complex than it seems'... but how hard can it be?"
    },
    {
      "speaker": "Reader Prompt",
      "text": "Have YOU ever felt confident about something before really understanding it? 🤔"
    }
  ]
}
```

**What Changed**:
1. ✅ Added overconfidence to Camila's dialogue ("esto es fácil!")
2. ✅ Added dismissive attitude to Camilo ("done by lunch")
3. ✅ Added foreshadowing via Diego (Dr. Erben's warning)
4. ✅ Added interactive reader prompt (4th dialogue entry)
5. ✅ Enhanced visual_prompt (overconfident smirks, complex diagram in background)

---

### Step 3: Verify JSON Structure

**Check**:
```bash
# Validate JSON syntax
python -m json.tool storyboard.json > /dev/null && echo "✅ Valid JSON" || echo "❌ Invalid JSON"

# Check panel 1 specifically
python -c "import json; data = json.load(open('storyboard.json')); print(f'Panel 1 dialogue entries: {len(data[0][\"dialogue\"])}')"
# Expected output: Panel 1 dialogue entries: 4
```

**Expected**: 4 dialogue entries (3 characters + 1 reader prompt)

---

## Step-by-Step: Panel 3 Update (Confusion Moment)

### Current vs Enhanced

**BEFORE**:
```json
{
  "panel": 3,
  "title": "Define Type 2",
  "setting": "Close-up of aneurysm diagram with incoming and outgoing arrows",
  "visual_prompt": "Aorta cutaway, aneurysm sac, small lumbar artery feeding retrograde flow; bright labels and dotted arrows.",
  "dialogue": [
    {
      "speaker": "Camilo",
      "text": "Type 2 = retrograde inflow from branches."
    },
    {
      "speaker": "Camila",
      "text": "Not a leak at the seal, sino colaterales."
    }
  ]
}
```

**AFTER**:
```json
{
  "panel": 3,
  "title": "Define Type 2",
  "setting": "Close-up of aneurysm diagram with incoming and outgoing arrows",
  "visual_prompt": "Aorta cutaway, aneurysm sac, multiple small lumbar arteries with dotted arrows showing bidirectional flow; bright labels BUT characters look confused; characters lean in, squinting at diagram, pointing at different vessels.",
  "dialogue": [
    {
      "speaker": "Camilo",
      "text": "Wait... it's NOT a seal leak? I thought endoleaks were stent failures..."
    },
    {
      "speaker": "Camila",
      "text": "Retrograde inflow? From which direction? There are so many branches!"
    },
    {
      "speaker": "Diego",
      "text": "The stent works FINE but blood finds another way?! How is that possible?"
    },
    {
      "speaker": "Reader Prompt",
      "text": "Reader, what OTHER paths could blood take? Think about it! 🔍"
    }
  ]
}
```

**What Changed**:
1. ✅ Transformed statements → questions (learning through confusion)
2. ✅ Added misconception challenge ("I thought endoleaks were stent failures")
3. ✅ Showed complexity ("so many branches!")
4. ✅ Added emotional reaction ("How is that possible?!")
5. ✅ Added reader engagement prompt
6. ✅ Enhanced visual_prompt (confusion expressions, multiple vessels)

---

## Batch Update Script (Optional)

If updating many panels, use Python script:

**update_dialogue.py**:
```python
#!/usr/bin/env python3
"""
Batch update storyboard.json with enhanced dialogue.
"""
import json
from pathlib import Path

# Enhanced dialogue mapping (panel_num -> new_dialogue)
ENHANCEMENTS = {
    1: {
        "dialogue": [
            {"speaker": "Camila", "text": "Hola! Type 2 endoleaks? We've read the papers—esto es fácil!"},
            {"speaker": "Camilo", "text": "¡Sí! Just map the vessels and we're done by lunch, right?"},
            {"speaker": "Diego", "text": "Dr. Erben said this is 'more complex than it seems'... but how hard can it be?"},
            {"speaker": "Reader Prompt", "text": "Have YOU ever felt confident about something before really understanding it? 🤔"}
        ],
        "visual_prompt_additions": "; characters have overconfident smirks; Dr. Erben visible in background with complex diagram (foreshadowing)"
    },
    3: {
        "dialogue": [
            {"speaker": "Camilo", "text": "Wait... it's NOT a seal leak? I thought endoleaks were stent failures..."},
            {"speaker": "Camila", "text": "Retrograde inflow? From which direction? There are so many branches!"},
            {"speaker": "Diego", "text": "The stent works FINE but blood finds another way?! How is that possible?"},
            {"speaker": "Reader Prompt", "text": "Reader, what OTHER paths could blood take? Think about it! 🔍"}
        ],
        "visual_prompt_additions": "; multiple lumbar arteries; characters look confused, leaning in, squinting"
    },
    # Add more panels as needed
}

def update_storyboard(input_path: str, output_path: str, backup: bool = True):
    """Update storyboard.json with enhanced dialogue."""
    
    # Load current storyboard
    with open(input_path, 'r', encoding='utf-8') as f:
        storyboard = json.load(f)
    
    # Backup if requested
    if backup:
        backup_path = Path(input_path).with_suffix('.json.backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(storyboard, f, indent=2, ensure_ascii=False)
        print(f"✅ Backup created: {backup_path}")
    
    # Apply enhancements
    panels_updated = 0
    for panel_data in storyboard:
        panel_num = panel_data['panel']
        if panel_num in ENHANCEMENTS:
            enhancement = ENHANCEMENTS[panel_num]
            
            # Update dialogue
            panel_data['dialogue'] = enhancement['dialogue']
            
            # Append to visual_prompt if specified
            if 'visual_prompt_additions' in enhancement:
                panel_data['visual_prompt'] += enhancement['visual_prompt_additions']
            
            panels_updated += 1
            print(f"✅ Updated Panel {panel_num}: {panel_data['title']}")
    
    # Save updated storyboard
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(storyboard, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Updated {panels_updated} panels")
    print(f"✅ Saved to: {output_path}")

if __name__ == '__main__':
    update_storyboard('storyboard.json', 'storyboard.json', backup=True)
```

**Usage**:
```bash
python update_dialogue.py
# Creates storyboard.json.backup and updates storyboard.json
```

---

## Quick Start: 6 Critical Panels (2-Hour Implementation)

### Priority Panel Updates

**Time**: ~20 minutes per panel × 6 panels = 2 hours

1. **Panel 1** (Opening hook)
   - Add overconfidence
   - Add reader prompt
   - Time: 15 min

2. **Panel 3** (First confusion)
   - Transform statements → questions
   - Add misconception
   - Add reader prompt
   - Time: 20 min

3. **Panel 9** (Mentor interaction)
   - Replace directives → Socratic questions
   - Add scaffolding dialogue
   - Time: 25 min (longest)

4. **Panel 14-15** (Innovation breakthrough)
   - Add "Known vs Unknown" transition
   - Enhance excitement
   - Time: 20 min

5. **Panel 23** (Vulnerability)
   - Add "I'm nervous!" moment
   - Add team support
   - Time: 15 min

6. **Panel 32** (Inspirational ending)
   - Add call-to-action
   - Add reader invitation
   - Time: 15 min

**Total**: ~110 minutes (1.8 hours) for maximum impact

---

## Validation After Updates

### 1. JSON Structure Check
```bash
# Validate JSON syntax
python -m json.tool storyboard.json > /dev/null && echo "✅ Valid JSON"

# Check panel count (should be 32)
python -c "import json; print(f'Panels: {len(json.load(open(\"storyboard.json\")))}')"
```

### 2. Dialogue Consistency Check
```bash
# Export updated dialogue
python export_dialogue.py

# Verify changes
diff dialogue.md dialogue-enhanced.md

# Should show fewer differences if updates applied correctly
```

### 3. Visual Prompt Check
```bash
# Check that visual_prompt was enhanced (not just dialogue)
grep -c "overconfident" storyboard.json
# Expected: At least 1 (Panel 1)

grep -c "confused" storyboard.json
# Expected: At least 1 (Panel 3)
```

### 4. Interactive Prompts Check
```bash
# Count reader prompts
python -c "
import json
count = 0
for panel in json.load(open('storyboard.json')):
    for d in panel['dialogue']:
        if d['speaker'] == 'Reader Prompt':
            count += 1
print(f'Reader prompts: {count}')
"
# Expected: At least 6 for quick start (13 for full implementation)
```

---

## Testing the Updated Comic

### 1. Regenerate Dialogue Export
```bash
python export_dialogue.py
# Creates updated dialogue.md
```

### 2. Regenerate PDF (if images unchanged)
```bash
python build_gpt_pdf.py
# Creates updated PDF with new dialogue
```

### 3. Visual Verification
- Open `type2-endoleak-comic-gpt.pdf`
- Check Panel 1: Overconfident dialogue visible?
- Check Panel 3: Confusion dialogue visible?
- Check Panel 9: Socratic questions visible?

### 4. Readability Test
- Read Panels 1-9 aloud
- Does dialogue sound natural?
- Are emotional beats clear?
- Do interactive prompts make sense?

---

## Common Pitfalls & Solutions

### Pitfall 1: JSON Syntax Errors
**Symptom**: Script fails with "JSONDecodeError"  
**Cause**: Missing comma, unclosed quote, or bracket  
**Solution**:
```bash
# Find syntax errors
python -m json.tool storyboard.json
# Will pinpoint line with error
```

### Pitfall 2: Unicode/Emoji Issues
**Symptom**: Emoji (🤔, 🔍) don't display correctly  
**Cause**: File encoding not UTF-8  
**Solution**:
```bash
# Ensure UTF-8 encoding when saving
# In Python: json.dump(..., ensure_ascii=False)
# In editor: Set encoding to UTF-8
```

### Pitfall 3: Lost Original Content
**Symptom**: Want to revert changes  
**Cause**: Didn't create backup  
**Solution**:
```bash
# Restore from backup
cp storyboard.json.backup storyboard.json

# Or from git (if committed earlier)
git restore storyboard.json
```

### Pitfall 4: Dialogue Too Long for Bubble
**Symptom**: Text overflows speech bubble in generated images  
**Cause**: Enhanced dialogue is longer  
**Solution**:
- Check maximum characters per bubble (typically ~100-120)
- Split long dialogue into 2 bubbles if needed
- Adjust font size in generation settings

### Pitfall 5: Interactive Prompts Not Rendering
**Symptom**: Reader prompts not visible in PDF  
**Cause**: Build script doesn't handle "Reader Prompt" speaker  
**Solution**:
```bash
# Update build_gpt_pdf.py to style reader prompts differently
# e.g., thought bubble instead of speech bubble
# or separate text box below panel
```

---

## Full Implementation Checklist

Use this checklist for complete 32-panel update:

### Preparation
- [ ] Read `dialogue-enhanced.md` completely
- [ ] Read `before-after-comparison.md` for philosophy
- [ ] Backup `storyboard.json` → `storyboard.json.backup`
- [ ] Test validation scripts work

### Critical Panels (Priority 1)
- [ ] Panel 1: Overconfident opening
- [ ] Panel 3: First confusion
- [ ] Panel 9: Socratic mentorship
- [ ] Panel 14-15: Innovation breakthrough
- [ ] Panel 23: Vulnerability
- [ ] Panel 32: Inspirational call-to-action

### Act 1 (Panels 1-8)
- [ ] Panel 1: ✅ (see above)
- [ ] Panel 2: Goal map with foreshadowing
- [ ] Panel 3: ✅ (see above)
- [ ] Panel 4: Camila's lightbulb moment
- [ ] Panel 5: Stakes become clear
- [ ] Panel 6: Overwhelmed, need help
- [ ] Panel 7: Visual comparison discovery
- [ ] Panel 8: Applying new understanding

### Act 2 (Panels 9-16)
- [ ] Panel 9: ✅ (see above)
- [ ] Panel 10: Understanding observation
- [ ] Panel 11: Intervention criteria
- [ ] Panel 12: Transarterial challenge
- [ ] Panel 13: Translumbar solution
- [ ] Panel 14: ✅ (see above)
- [ ] Panel 15: ✅ (see above)
- [ ] Panel 16: Clinical application

### Act 3 (Panels 17-24)
- [ ] Panel 17: Feasibility reality check
- [ ] Panel 18: Literature analysis
- [ ] Panel 19: Patient empathy
- [ ] Panel 20: Appreciating rigor
- [ ] Panel 21: Observing expertise
- [ ] Panel 22: Long-term perspective
- [ ] Panel 23: ✅ (see above)
- [ ] Panel 24: Sample size patience

### Act 4 (Panels 25-32)
- [ ] Panel 25: Ethics foundation
- [ ] Panel 26: Data integrity
- [ ] Panel 27: Preliminary results
- [ ] Panel 28: Teaching consolidation
- [ ] Panel 29: Future vision
- [ ] Panel 30: Mentor validation
- [ ] Panel 31: Patient impact (emotional climax)
- [ ] Panel 32: ✅ (see above)

### Validation
- [ ] JSON syntax valid
- [ ] 32 panels present
- [ ] All panels have 3-4 dialogue entries
- [ ] 13 reader prompts present (or 6 for quick start)
- [ ] Visual prompts enhanced
- [ ] Regenerate dialogue.md
- [ ] Read aloud test (sounds natural?)
- [ ] Regenerate PDF
- [ ] Visual check in PDF

### Testing
- [ ] Share with 2-3 colleagues for feedback
- [ ] Test with 1-2 target audience (research interns)
- [ ] Collect feedback on emotional engagement
- [ ] Iterate on any unclear dialogue

---

## After Implementation: Next Steps

### 1. User Testing
- Recruit 5-10 research interns
- Pre-test knowledge (Type 2 endoleak quiz)
- Have them read enhanced comic
- Post-test knowledge + engagement survey
- Iterate based on feedback

### 2. Visual Enhancements (Optional)
- If regenerating images: update `gpt-prompts.txt` with enhanced visual_prompt content
- Regenerate images: `python gpt_image_generator.py --prompt-file gpt-prompts.txt`
- Rebuild PDF: `python build_gpt_pdf.py`

### 3. Distribution
- Upload enhanced PDF to appropriate channels
- Update documentation with "enhanced" version label
- Archive original version for comparison

### 4. Metrics Tracking
- Track downloads/views
- Collect qualitative feedback
- Measure impact on research intern engagement
- Document lessons learned

---

## Support Resources

**Documentation**:
- `dialogue-enhanced.md` - Complete enhanced dialogue
- `before-after-comparison.md` - Philosophy and examples
- `implementation-checklist.md` - Project management guide
- `emotional-arc-guide.md` - Emotional journey visualization

**Tools**:
- `export_dialogue.py` - Export dialogue to markdown
- `validate_comic.py` - Validate structure
- `build_gpt_pdf.py` - Generate PDF
- `update_dialogue.py` - (Created above) Batch update script

**Getting Help**:
- Review companion documents in this directory
- Consult `.github/agents/pedagogy.agent.md`
- Test incrementally (don't update all 32 panels at once!)

---

**Version**: 1.0  
**Date**: 2026-01-07  
**Author**: @pedagogy agent  
**Tested**: Example panels verified with JSON validator
