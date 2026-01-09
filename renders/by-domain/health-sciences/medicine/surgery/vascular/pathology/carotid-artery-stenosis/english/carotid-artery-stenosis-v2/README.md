# Carotid Artery Stenosis Story - Version 2

## Overview

**The Silent Warning**: Dr. Yuna Erben's Carotid Endarterectomy Story

This is the comprehensive Version 2 of the carotid artery stenosis educational comic, featuring updated character representation and separated workflow development.

## Character Update - Dr. Yuna Erben

### Key Character Attributes
- **Ethnicity**: Korean-American
- **Physical Appearance**: Petite (approximately 5 feet tall), 40s
- **Distinctive Features**: Expressive rectangular black-framed glasses
- **Hair**: Straight black hair in practical low ponytail
- **Languages**: Multilingual
  - Spanish (Venezuelan dialect - grew up in Caracas, Venezuela)
  - English (fluent)
  - German (fluent)
  - Korean (fluent)
- **Professional**: Vascular surgeon specializing in cerebrovascular disease
- **Personality**: Warm, culturally sensitive, technically brilliant, dedicated

### Cultural Background
Dr. Erben grew up in Caracas, Venezuela until age 15, giving her native-level fluency in Spanish with Venezuelan inflections. This background allows her to connect deeply with Latino patients and build trust through shared cultural understanding.

## Story Synopsis

Carmen Rodriguez, a 67-year-old Venezuelan immigrant, presents to the emergency department after experiencing transient ischemic attack (TIA) symptoms. Dr. Yuna Erben, connecting with Carmen through their shared Venezuelan Spanish, diagnoses severe (85%) carotid artery stenosis and guides her through the decision-making process for carotid endarterectomy surgery.

The story follows Carmen's complete journey:
- **Act 1** (Panels 1-12): TIA recognition, diagnosis, building trust, patient education
- **Act 2** (Panels 13-20): Surgical preparation, informed consent, pre-operative planning
- **Act 3** (Panels 21-32): The surgical procedure in detail
- **Act 4** (Panels 33-40): Recovery, prevention education, long-term success

## Educational Objectives

### Medical Knowledge
1. **TIA Recognition**: FAST acronym (Face, Arms, Speech, Time)
2. **Carotid Stenosis Pathophysiology**: Atherosclerotic plaque formation and embolization
3. **Diagnostic Workup**: Carotid duplex ultrasound, CT angiography
4. **NASCET Criteria**: >70% stenosis with symptoms = surgical candidate
5. **Treatment Options**: Medical management vs. surgical intervention
6. **Surgical Technique**: Step-by-step carotid endarterectomy with patch angioplasty
7. **Perioperative Care**: Neuromonitoring, blood pressure management
8. **Stroke Prevention**: Long-term management (medications + lifestyle)

### Cultural Competence
1. **Language**: Importance of communicating in patient's native language
2. **Trust-Building**: Cultural connections facilitate medical care
3. **Family-Centered Care**: Involving family in decision-making
4. **Health Literacy**: Using visual aids and analogies accessible across language barriers

## Story Development Workflow

This V2 version follows a separated workflow (different from V1):

### Phase 1: Story Idea (Completed)
- Character specifications
- Story hook and concept
- Educational goals
- Story arc outline (40 panels)

### Phase 2: Story Telling (Completed)
- Full narrative prose (44KB)
- Detailed scene descriptions
- Character development
- Dialogue (Spanish and English)
- Medical accuracy

### Phase 3: Storyboard (Completed)
- 40-panel detailed storyboard (JSON format)
- Scene descriptions for each panel
- Character lists per panel
- Key visual elements
- Educational focus per panel
- Emotional tone guidance

### Phase 4: Prompts (Completed)
- Super-explicit prompts for image generation
- 40 individual prompt files (avg 5,522 characters each)
- Total: 220KB of prompts
- Specifications include:
  - Hex color codes
  - Precise positioning (LEFT/RIGHT explicit)
  - Character appearance consistency
  - Dora the Explorer cartoon style
  - Educational elements
  - Spanish dialogue with English subtitles

### Phase 5: Images (In Progress)
- Generate 40 images using GPT Image 1.5
- Landscape orientation: 1536×1024 pixels
- Dora the Explorer cartoon style:
  - Thick black outlines (3-4px)
  - Flat bright colors, no gradients
  - Expressive faces with large eyes
  - Educational clarity over realism

### Phase 6: Documentation (Pending)
- Comprehensive README
- Usage guidelines
- Educational application suggestions

## Technical Specifications

### Visual Style
- **Inspiration**: Dora the Explorer cartoon aesthetic
- **Outlines**: Thick black (3-4px, #000000)
- **Colors**: Flat, bright, saturated - NO gradients or shadows
- **Character Eyes**: Large and expressive (30% of face height)
- **Orientation**: Landscape 1536×1024 (3:2 aspect ratio)
- **Backgrounds**: Simple, often white or solid colors
- **Typography**: Sans-serif, horizontal text only

### Character Consistency
Dr. Erben's appearance is IDENTICAL across all 40 panels:
- Same teal scrubs (#008B8B) in non-surgical scenes
- Same surgical attire (light green gown #90EE90) in OR scenes
- Same rectangular black glasses in EVERY panel
- Same black ponytail hairstyle
- Same petite stature (notably shorter than other adults)
- Same East Asian facial features

### Medical Accuracy
All medical content vetted for accuracy:
- Anatomical terminology correct
- Surgical technique reflects current best practices
- NASCET criteria accurately represented
- Evidence-based treatment algorithms (NASCET, CREST trials)
- Realistic complication monitoring

## File Structure

```
carotid-artery-stenosis-v2/
├── story-development/
│   ├── 01-story-idea.md (6KB)
│   ├── 02-narrative.md (44KB)
│   ├── 03-storyboard.json (31KB)
│   └── generate_storyboard.py
├── comic/
│   ├── generate_prompts.py
│   ├── prompts-all-panels.txt (220KB combined)
│   ├── individual-prompts/
│   │   ├── panel_01.txt through panel_40.txt
│   └── panels-gpt/ (generated images)
│       └── image_XXX_*.png (40 images)
└── README.md (this file)
```

## Usage Guidelines

### For Medical Education
- **Target Audiences**: Medical students, residents, patients, families
- **Learning Objectives**: Stroke prevention, surgical decision-making, patient education
- **Format Options**: Digital viewing, printed comic, presentation slides, video animation

### For Patient Education
- **Accessible Language**: Visual storytelling transcends language barriers
- **Cultural Relevance**: Representation matters - diverse patients see themselves
- **Informed Consent**: Realistic surgical expectations
- **Prevention Emphasis**: Long-term lifestyle changes

### For Cultural Competency Training
- **Language**: Demonstrating value of multilingual healthcare providers
- **Trust**: How cultural connections improve medical outcomes
- **Family**: Involving family in Hispanic healthcare culture
- **Respect**: Dr. Erben's humble expertise despite accomplishments

## Differences from Version 1

| Aspect | Version 1 | Version 2 |
|--------|-----------|-----------|
| **Workflow** | Combined | Separated (Idea → Telling → Storyboard) |
| **Dr. Erben Ethnicity** | Unspecified | Explicitly Korean-American |
| **Physical Description** | Basic | Detailed (petite, glasses, ponytail) |
| **Languages** | English focus | Multilingual (Spanish/English/German/Korean) |
| **Cultural Background** | Minimal | Venezuelan upbringing emphasized |
| **Panel Count** | 32 panels | 40 panels (story-driven expansion) |
| **Narrative Depth** | Moderate | Deep (44KB prose) |
| **Patient Connection** | Standard | Cultural/linguistic bond through Spanish |
| **Story Length Approach** | Fixed limit | Story-driven (expanded to serve narrative) |

## Educational Applications

### Medical School Curriculum
- **Year 1-2**: Cardiovascular pathophysiology, stroke mechanisms
- **Year 3-4**: Clinical decision-making, surgical indications
- **Residency**: Surgical technique, perioperative management

### Patient Materials
- Waiting room education
- Pre-operative teaching
- Post-operative care instructions
- Stroke prevention programs

### Community Health
- Public health campaigns
- Community center education
- Senior center stroke awareness
- Multi-lingual health literacy

## Contact and Attribution

**Story Development**: AI-assisted medical education content creation  
**Medical Accuracy**: Based on current vascular surgery guidelines  
**Cultural Consultation**: Venezuelan Spanish dialogue, Korean-American representation  
**Visual Style**: Dora the Explorer inspired educational cartoon aesthetic  

## Version History

- **V1**: Original 32-panel version (generic character representation)
- **V2**: Updated 40-panel version with Dr. Yuna Erben character, separated workflow, deeper narrative

---

## Workflow Note

> **Important**: This comic was created using an **older workflow** where panels were defined in the Story Idea phase and narrative was written per-panel.
>
> **For new comics**, use the **story-first workflow** documented in:
> `.project/agents/image-generation/COMIC-STORY-WORKFLOW.md`
>
> **Correct workflow**:
> 1. Story Idea (NO panels yet)
> 2. Full Narrative (flowing prose, NO panel references)
> 3. Panel Planning (decide panels AFTER story is written)
> 4. Storyboard
> 5. Prompts
> 6. Images

---

**Target Completion**: All 40 images + comprehensive documentation  
**Educational Impact**: Accessible, culturally relevant stroke prevention education  
**Innovation**: Separated workflow emphasizes storytelling before visualization
