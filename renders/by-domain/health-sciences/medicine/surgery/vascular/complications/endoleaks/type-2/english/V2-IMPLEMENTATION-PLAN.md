# Version 2 Stories - Implementation Plan
## Updated Character & Workflow

### Character Update: Dr. Erben

**Original (V1)**: Generic attending vascular surgeon  
**Updated (V2)**: 
- **Ethnicity**: Korean
- **Physical**: Petite, in her 40s, wears expressive glasses
- **Languages**: Spanish (grew up in Venezuela), English, German, Korean
- **Background**: Venezuelan upbringing, multilingual, brings diverse cultural perspectives

### Workflow Changes

**V1 Workflow** (Combined):
- Storyboard → Prompts → Images → Docs

**V2 Workflow** (Separated):
1. **Story Idea** - Core concept, educational goals, emotional arc, target length
2. **Story Telling** - Detailed narrative prose with full dialogue and scenes
3. **Storyboard** - Panel-by-panel breakdown with visual specifications
4. **Prompts** - Super-explicit technical specifications for image generation
5. **Images** - Generate with GPT Image 1.5
6. **Documentation** - Compile final materials

### Story Length Requirements

**V1**: Fixed panels (carotid: 32, others: 8)  
**V2**: Story-driven length, minimum 30 panels, can expand as needed for narrative

**Key Principle**: "It's not 'oh, I must add another image' but rather 'we have to make the story more elaborate'"

### Implementation Approach

#### For Each Story:
1. Create `/story-name-v2/` directory alongside existing
2. Within that, create `/story-development/` subdirectory for workflow phases
3. Develop in phases:
   - `01-story-idea.md` - High-level concept
   - `02-story-telling.md` - Full narrative with dialogue
   - `03-storyboard.json` - Detailed panel specs
   - `04-prompts/` - Individual prompt files
   - `05-comic/panels-gpt/` - Generated images
4. Create comprehensive README documenting the v2 approach

### Stories to Create (V2 Versions)

1. **Carotid Artery Stenosis V2** - Expand to 35+ panels
2. **Acute Limb Ischemia V2** - Expand to 30+ panels  
3. **Diabetic Foot Bypass V2** - Expand to 30+ panels
4. **Varicose Veins V2** - Expand to 30+ panels

All will feature updated Dr. Erben character throughout.

### Directory Structure

```
renders/.../endoleaks/type-2/english/
├── carotid-artery-stenosis/ (v1 - preserved)
├── carotid-artery-stenosis-v2/
│   ├── story-development/
│   │   ├── 01-story-idea.md
│   │   ├── 02-story-telling.md
│   │   ├── 03-storyboard.json
│   │   ├── 04-prompts/
│   │   │   ├── panel_01.txt
│   │   │   ├── panel_02.txt
│   │   │   └── ... (35+ files)
│   │   └── README.md
│   └── comic/
│       ├── README.md
│       ├── panels-gpt/ (images)
│       └── metadata/
├── acute-limb-ischemia/ (v1 - preserved)
├── acute-limb-ischemia-v2/
│   └── (similar structure)
├── diabetic-foot-bypass/ (v1 - preserved)
├── diabetic-foot-bypass-v2/
│   └── (similar structure)
├── varicose-veins/ (v1 - preserved)
└── varicose-veins-v2/
    └── (similar structure)
```

### Character Consistency Requirements

All V2 images must show:
- Dr. Erben as petite Korean woman
- Expressive glasses (distinctive feature)
- Professional attire (scrubs/white coat)
- Age ~40s
- Confident but approachable demeanor

Prompts must specify:
- Ethnicity explicitly (Korean)
- Physical build (petite, approximately 5'2")
- Glasses style (expressive, slightly oversized frames)
- Hair (shoulder-length, dark, professional style)
- Facial features (consistent with Korean ethnicity)

### Next Steps

1. ✅ Create this implementation plan
2. Create story idea for carotid v2
3. Write full narrative for carotid v2
4. Develop storyboard for carotid v2
5. Generate prompts for carotid v2
6. Generate images for carotid v2
7. Repeat for other 3 stories
8. Create v2 overview documentation

**Status**: Implementation plan complete. Ready to proceed with carotid v2 story development.
