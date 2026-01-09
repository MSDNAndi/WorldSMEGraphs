# Comic Story Creation Workflow

> **Critical Rule**: Write the STORY first, decide PANELS later.
> 
> **Version**: 1.0.0  
> **Created**: 2026-01-09  
> **Updated from**: PR #42 feedback on wrong workflow order
> **Purpose**: Enforce story-first approach for educational comics

## Problem Statement

From PR #42 feedback, we identified a workflow issue:

**Previous (WRONG) Approach:**
1. Story Idea (with panels already defined)
2. Narrative written per-panel
3. Storyboard 
4. Prompts
5. Images

**Issue**: Panels were decided too early, constraining the storytelling.

**Correct Approach:**
1. Story Idea (theme, characters, goals - NO panels)
2. Full Narrative (complete flowing story - NO panel structure)
3. Panel Planning (decide how to break story into panels)
4. Storyboard (map narrative to panels)
5. Prompts
6. Images

## The Correct Comic Workflow

### Phase 1: Story Concept
**Input**: Medical topic, educational objectives, target audience
**Output**: Story concept document WITHOUT panel assignments

**File**: `story-development/01-story-idea.md`

**Contents**:
```markdown
# [Topic] - Story Concept

## Educational Objectives
- What medical knowledge to teach
- What skills to develop
- What attitudes to foster

## Character Specifications
- Main characters (doctor, patient, family)
- Physical descriptions
- Personality traits
- Cultural background (if relevant)

## Story Hook
- Opening dramatic moment
- Central conflict/challenge
- Why reader should care

## Thematic Elements
- Medical themes (e.g., time-critical decisions)
- Human themes (e.g., trust, communication)
- Cultural elements (e.g., language barriers)

## Story Arc (HIGH LEVEL ONLY)
### Act 1: Setup
- What happens to establish the situation

### Act 2: Confrontation
- The main challenge/procedure/journey

### Act 3: Resolution
- The outcome and aftermath

## Style Notes
- Visual style inspiration
- Color palette
- Tone (dramatic, educational, heartwarming)
```

**CRITICAL**: No panel numbers, no panel counts, no panel assignments at this stage.

**Validation**: ✅ Story concept is complete without panel references

---

### Phase 2: Full Narrative Writing
**Input**: Story concept
**Output**: Complete prose narrative WITHOUT panel structure

**File**: `story-development/02-narrative.md`

**Contents**:
```markdown
# [Topic] - Full Narrative

## Prologue (Optional)
[Scene-setting prose]

## The Story

[Write the complete story as flowing narrative prose.
Use scene breaks (---) when the setting or time changes significantly.
Include all dialogue, descriptions, and educational content.
Write as if this were a short story or novella.
DO NOT reference panels or visual frames.]

### Scene 1: [Title]
[Narrative prose describing what happens...]

### Scene 2: [Title]  
[Continue the story...]

[etc.]

## Educational Insights (Post-Story Notes)
- Key medical concepts covered
- Decision points illustrated
- Procedural steps shown
```

**Word Count Target**: 8,000-15,000 words for a 30-40 panel comic

**CRITICAL**: Write as flowing narrative. Scenes are logical story divisions, NOT panels.

**Validation**: 
- ✅ Complete story with beginning, middle, end
- ✅ All educational content included
- ✅ NO panel references
- ✅ Flows naturally as prose

---

### Phase 3: Panel Planning
**Input**: Complete narrative
**Output**: Decision document on how to break story into panels

**File**: `story-development/03-panel-planning.md`

**Contents**:
```markdown
# [Topic] - Panel Planning

## Overall Strategy
- Target panel count: [estimate based on story complexity]
- Pacing philosophy: [dense action vs. breathing room]
- Key moments requiring their own panel

## Scene-to-Panel Mapping

### Scene 1: [Scene Title from narrative]
**Narrative excerpt to cover**: "From [start quote] to [end quote]"
**Proposed panels**: 3
**Reasoning**: 
- Panel 1: Establish setting and characters
- Panel 2: Key dramatic moment  
- Panel 3: Transition

### Scene 2: [Title]
**Narrative excerpt**: "..."
**Proposed panels**: 4
**Reasoning**: [explanation]

[Continue for all scenes]

## Panel Count Summary
- Act 1: X panels
- Act 2: Y panels  
- Act 3: Z panels
- **Total**: N panels

## Review Questions
- Does every panel serve a purpose?
- Are any scenes under/over-represented?
- Is pacing appropriate for audience?
- Are key educational moments given sufficient visual space?
```

**Validation**: 
- ✅ All narrative content is mapped to panels
- ✅ No narrative content is orphaned
- ✅ Panel assignments are justified

---

### Phase 4: Storyboard Creation
**Input**: Panel planning + Complete narrative
**Output**: Structured storyboard with scene descriptions per panel

**File**: `story-development/04-storyboard.json`

**Contents**:
```json
{
  "comic_title": "[Title]",
  "version": "1.0",
  "total_panels": 35,
  "acts": [
    {
      "act_number": 1,
      "act_title": "Recognition",
      "panels": [
        {
          "panel_number": 1,
          "panel_title": "The 3 AM Call",
          "narrative_reference": "Scene 1, paragraphs 1-2",
          "scene_description": "Dr. Erben's bedroom, phone ringing...",
          "characters_present": ["Dr. Erben"],
          "key_visual_elements": ["phone", "clock showing 3:02 AM", "darkness"],
          "dialogue": ["Phone: *RING*", "Dr. Erben: 'Dr. Erben speaking...'"],
          "educational_focus": "Emergency response - on-call 24/7",
          "emotional_tone": "Alert, immediate response"
        }
      ]
    }
  ]
}
```

**Validation**:
- ✅ Every panel has complete scene description
- ✅ Dialogue extracted from narrative
- ✅ Educational focus defined per panel

---

### Phase 5: Prompt Engineering
**Input**: Storyboard
**Output**: Super-explicit prompts for each panel

**Files**: 
- `comic/prompts-all-panels.txt` (concatenated)
- `comic/individual-prompts/panel_01.txt` through `panel_XX.txt`

**Prompt Structure**:
```text
=== PANEL [NN]: [Panel Title] ===

[Complete, self-contained prompt with ALL details]

STYLE REQUIREMENTS:
[Full style description - no external references]

CHARACTER DESCRIPTIONS:
[Full description of each character - every time]

SCENE DESCRIPTION:
[What happens in this panel]

KEY VISUAL ELEMENTS:
[List of must-include elements with positions]

DIALOGUE:
[All dialogue to include as text bubbles]

COLOR PALETTE:
[Hex codes for all colors]

COMPOSITION:
[Layout, positioning, orientation specifics]

CRITICAL CONSTRAINTS:
[What must be in/out of the panel]
```

**Validation**:
- ✅ Each prompt is self-contained (8K+ characters)
- ✅ No external references or placeholders
- ✅ Super explicit about directions and positions

---

### Phase 6: Image Generation
**Input**: Individual prompts
**Output**: Generated images with proper panel numbering

**Script Template**:
```bash
#!/bin/bash
for i in $(seq 1 [TOTAL_PANELS]); do
    panel_num=$(printf "%02d" $i)
    prompt_file="individual-prompts/panel_${panel_num}.txt"
    
    python gpt_image_generator.py \
        --prompt "$(cat $prompt_file)" \
        --output "image_${panel_num}" \  # CRITICAL: Include panel number
        --aspect landscape \
        --quality high \
        --output-dir panels-gpt
done
```

**CRITICAL**: Always use `--output image_XX` to ensure proper panel numbering.

**Validation**:
- ✅ Images named `image_001_*.png`, `image_002_*.png`, etc.
- ✅ One image per panel number
- ✅ Total image count matches panel count

---

### Phase 7: Viewing File Generation
**Input**: Generated images
**Output**: Viewing markdown files

**Files**:
- `comic/6-panel-grid-view.md`
- `comic/continuous-story-view.md`
- `comic/pictures-only-view.md`

**Tool**: `python tools/generate_viewing_files.py`

**Validation**:
- ✅ All panels included in viewing files
- ✅ Correct ordering (handles broken numbering via timestamps)

---

## File Structure Template

```
[topic]-v2/
├── README.md                    # Overview and status
├── story-development/
│   ├── 01-story-idea.md         # Concept WITHOUT panels
│   ├── 02-narrative.md          # Full prose story
│   ├── 03-panel-planning.md     # Panel decisions
│   ├── 04-storyboard.json       # Panel-by-panel breakdown
│   └── generate_storyboard.py   # Helper script
├── comic/
│   ├── individual-prompts/
│   │   ├── panel_01.txt
│   │   ├── panel_02.txt
│   │   └── ...
│   ├── prompts-all-panels.txt
│   ├── panels-gpt/
│   │   ├── image_001_*.png
│   │   ├── image_002_*.png
│   │   └── ...
│   ├── 6-panel-grid-view.md
│   ├── continuous-story-view.md
│   ├── pictures-only-view.md
│   ├── COMIC-VIEW.md
│   └── generate_all_images.sh
└── SESSION-NOTES.md             # Development notes
```

---

## Differences from Old Workflow

| Aspect | Old (Wrong) | New (Correct) |
|--------|-------------|---------------|
| **Story Idea** | Included "Story Arc (35 Panels)" | Just high-level acts, no panels |
| **Narrative** | Written per-panel: "### Panel 1:" | Flowing prose with scene breaks |
| **Panel Decision** | Embedded in story concept | Separate planning phase AFTER story |
| **Storyboard** | First panel reference | Third phase, informed by complete story |
| **Flexibility** | Locked in early | Adjustable based on story needs |

---

## Common Mistakes to Avoid

### ❌ WRONG: Defining Panels in Story Idea
```markdown
## Story Arc (35 Panels)
### Act 1: Emergency Recognition (Panels 1-10)
1. 3 AM phone call - Dr. Erben awakened
2. Racing to hospital
```

### ✅ CORRECT: High-Level Story Beats Only
```markdown
## Story Arc (High Level)
### Act 1: Emergency Recognition
- The emergency call in the middle of the night
- Rush to the hospital
- First assessment of the patient
```

### ❌ WRONG: Writing Narrative Per-Panel
```markdown
### Panel 1: The 3 AM Call
The phone's shrill ring pierced the darkness...

### Panel 2: Racing to Hospital  
Dr. Erben's car cut through the empty streets...
```

### ✅ CORRECT: Flowing Prose Narrative
```markdown
## The Story

The phone's shrill ring pierced the darkness of Dr. Erben's bedroom. 
She reached for her glasses on the nightstand, her eyes focusing on 
the clock: 3:02 AM. "Dr. Erben," she answered, her voice alert...

Her car cut through the empty pre-dawn streets. The dashboard clock 
glowed 3:11 AM. Her mind raced through the differential: Embolus 
versus thrombosis? Probably embolus at this age if he has AFib...
```

---

## Workflow Enforcement Checklist

Before generating images, verify:

- [ ] `02-narrative.md` exists and contains flowing prose
- [ ] `02-narrative.md` does NOT contain panel references
- [ ] `03-panel-planning.md` exists with justified panel assignments
- [ ] `04-storyboard.json` maps narrative to panels completely
- [ ] Individual prompts are self-contained (8K+ chars each)
- [ ] Generation script uses `--output image_XX` for proper naming

---

## See Also

- `WORKFLOW-ENFORCEMENT.md` - General image workflow
- `image-prompt-engineering-guide.md` - Prompt writing best practices
- `QUICK-START.md` - Getting started guide
- `tools/generate_viewing_files.py` - Viewing file generator
