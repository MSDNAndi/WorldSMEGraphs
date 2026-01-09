#!/usr/bin/env python3
"""
Initialize a new comic project with the correct story-first workflow structure.

This tool creates the proper directory structure and template files for
creating educational comics following the story-first workflow documented
in COMIC-STORY-WORKFLOW.md.

Usage:
    python init_comic_project.py --name "Story Name" --topic "Medical Topic" --character "Dr. Name"
    
Example:
    python init_comic_project.py \
        --name "deep-vein-thrombosis-v1" \
        --topic "Deep Vein Thrombosis" \
        --character "Dr. Young Erben"
"""

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def create_story_idea_template(name: str, topic: str, character: str) -> str:
    """Create a story idea template following the correct workflow."""
    return f'''# {topic} - Story Concept

> **IMPORTANT**: Do NOT define panel counts or panel assignments at this stage.
> Write the story FIRST, decide panels LATER.
> 
> See: `.project/agents/image-generation/COMIC-STORY-WORKFLOW.md`

## Educational Objectives

### Medical Learning Goals
- [ ] Define primary learning objective
- [ ] Define secondary learning objectives
- [ ] Define procedural skills to teach (if applicable)
- [ ] Define prevention/follow-up education

### Cultural/Human Elements
- [ ] Define patient communication themes
- [ ] Define cultural sensitivity elements
- [ ] Define emotional/trust-building moments

## Character Specification

**Main Character: {character}**
- **Ethnicity**: [e.g., Korean]
- **Physical Description**: [e.g., Petite, 40s, expressive rectangular glasses]
- **Languages**: [e.g., Spanish, English, German, Korean]
- **Specialty**: [e.g., Vascular Surgery]
- **Background**: [Brief background story]

**Patient: [Name]**
- **Age**: [Age]
- **Background**: [Cultural/social background]
- **Presenting Condition**: [What brings them to care]
- **Character Arc**: [How they change through the story]

## Story Hook

[Write a compelling opening that draws readers in. What is the dramatic moment?
What creates urgency or emotional connection?]

## Thematic Elements

### Medical Themes
- [List key medical concepts]

### Human Themes
- [Trust, communication, fear, hope, etc.]

### Cultural Elements
- [Language, family dynamics, healthcare access, etc.]

## Story Arc (HIGH LEVEL ONLY)

> **Note**: Do NOT define panel numbers here. Just outline the story beats.

### Act 1: [Title - e.g., Recognition]
- [Story beat 1]
- [Story beat 2]
- [Story beat 3]

### Act 2: [Title - e.g., Preparation]
- [Story beat 1]
- [Story beat 2]
- [Story beat 3]

### Act 3: [Title - e.g., Treatment/Procedure]
- [Story beat 1]
- [Story beat 2]
- [Story beat 3]

### Act 4: [Title - e.g., Recovery/Prevention]
- [Story beat 1]
- [Story beat 2]
- [Story beat 3]

## Medical Accuracy Notes

- [Key medical facts that must be accurate]
- [Evidence-based sources to reference]
- [Common misconceptions to address]

## Style Notes

- **Visual Style**: Dora the Explorer cartoon (thick black outlines, flat colors)
- **Color Palette**: [Define key colors]
- **Tone**: [Educational, dramatic, heartwarming, etc.]
- **Language**: [Bilingual elements, if any]

---

**Status**: Story Concept Complete  
**Next Step**: Write full narrative in `02-narrative.md`  
**Created**: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')}
'''


def create_narrative_template(topic: str) -> str:
    """Create a narrative template for flowing prose."""
    return f'''# {topic} - Full Narrative

> **IMPORTANT**: Write this as flowing prose WITHOUT panel references.
> Use scene breaks (---) for major setting/time changes.
> Panel decisions come AFTER this story is complete.
> 
> See: `.project/agents/image-generation/COMIC-STORY-WORKFLOW.md`

## The Story

[Write the complete story as flowing narrative prose. Include:
- All dialogue (with language indicators if multilingual)
- Scene descriptions
- Character emotions and internal thoughts
- Educational content woven naturally into the narrative
- Clear scene transitions

Target length: 8,000-15,000 words for a 30-40 panel comic.]

### Scene 1: [Scene Title]

[Write scene 1 as flowing prose...]

---

### Scene 2: [Scene Title]

[Continue the story...]

---

### Scene 3: [Scene Title]

[Continue the story...]

---

[Add more scenes as needed...]

---

## Educational Content Notes

[After writing the story, note the key educational moments:]

- **Concept 1**: [Where in the story this appears]
- **Concept 2**: [Where in the story this appears]
- **Procedure details**: [Where these are taught]
- **Prevention education**: [Where this appears]

---

**Status**: Narrative In Progress  
**Next Step**: Complete narrative, then create `03-panel-planning.md`  
**Word Count**: [Update as you write]
'''


def create_panel_planning_template(topic: str) -> str:
    """Create a panel planning template."""
    return f'''# {topic} - Panel Planning

> **Create this AFTER completing the full narrative.**
> This is where panel decisions are made.
> 
> See: `.project/agents/image-generation/COMIC-STORY-WORKFLOW.md`

## Overall Strategy

**Target Panel Count**: [Estimate based on story length and complexity]

**Pacing Philosophy**: 
- [Dense action scenes vs. breathing room for emotional moments]
- [How many panels per page for reading flow]

**Key Moments Requiring Full Panels**:
- [List climactic or educational moments that need their own panel]

## Scene-to-Panel Mapping

### Scene 1: [Scene Title from narrative]

**Narrative Excerpt**: From "[first quote]" to "[last quote]"

**Proposed Panels**: [Number]

**Panel Breakdown**:
1. **Panel [X]**: [What this panel captures]
   - **Visual**: [Key visual elements]
   - **Dialogue**: [Any dialogue in this panel]
   - **Educational Focus**: [What viewers learn]

2. **Panel [X+1]**: [Next panel]
   - **Visual**: [Elements]
   - **Dialogue**: [Dialogue]
   - **Educational Focus**: [Learning]

[Continue for each panel in this scene...]

---

### Scene 2: [Scene Title]

[Repeat the structure above for each scene...]

---

## Panel Count Summary

| Act | Panel Range | Count |
|-----|-------------|-------|
| Act 1 | 1 - [X] | [N] |
| Act 2 | [X+1] - [Y] | [M] |
| Act 3 | [Y+1] - [Z] | [P] |
| Act 4 | [Z+1] - [End] | [Q] |
| **Total** | 1 - [End] | **[Total]** |

## Review Checklist

- [ ] Every panel serves a narrative or educational purpose
- [ ] No scenes are under-represented
- [ ] Key educational moments have sufficient visual space
- [ ] Pacing feels appropriate for target audience
- [ ] Panel count is sustainable for image generation

---

**Status**: Panel Planning Complete  
**Next Step**: Create `04-storyboard.json`
'''


def create_readme_template(name: str, topic: str, character: str) -> str:
    """Create a README template."""
    return f'''# {topic} - Educational Comic

## Overview

**Topic**: {topic}  
**Format**: Educational Comic  
**Target Audience**: [Medical students, patients, general public, etc.]

**Main Character**: {character}

## Status

🔴 **In Development** - Story Phase

## Workflow Progress

Following the story-first workflow from `COMIC-STORY-WORKFLOW.md`:

- [ ] 1. Story Concept (01-story-idea.md)
- [ ] 2. Full Narrative (02-narrative.md) - NO panel references
- [ ] 3. Panel Planning (03-panel-planning.md) - Decide panels AFTER story
- [ ] 4. Storyboard (04-storyboard.json)
- [ ] 5. Prompts (comic/individual-prompts/)
- [ ] 6. Images (comic/panels-gpt/)
- [ ] 7. Viewing Files (6-panel-grid-view.md, etc.)

## Educational Objectives

[Copy from story idea when complete]

## Technical Details

- **Style**: Dora the Explorer cartoon (thick black outlines, flat colors)
- **Image Size**: 1536×1024 (landscape)
- **Image Format**: PNG

## Files Structure

```
{name}/
├── README.md (this file)
├── story-development/
│   ├── 01-story-idea.md (story concept - NO panels)
│   ├── 02-narrative.md (flowing prose - NO panels)
│   ├── 03-panel-planning.md (panel decisions AFTER story)
│   └── 04-storyboard.json (panel-by-panel breakdown)
└── comic/
    ├── individual-prompts/ (one file per panel)
    ├── prompts-all-panels.txt (concatenated)
    ├── panels-gpt/ (generated images)
    └── viewing files (*.md)
```

## License

For educational use.

---

**Created**: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')}  
**Workflow**: Story-first approach (COMIC-STORY-WORKFLOW.md)
'''


def init_project(output_dir: str, name: str, topic: str, character: str) -> None:
    """Initialize a new comic project with proper structure."""
    
    base_path = Path(output_dir) / name
    story_dev_path = base_path / "story-development"
    comic_path = base_path / "comic"
    prompts_path = comic_path / "individual-prompts"
    panels_path = comic_path / "panels-gpt"
    
    # Create directories
    story_dev_path.mkdir(parents=True, exist_ok=True)
    prompts_path.mkdir(parents=True, exist_ok=True)
    panels_path.mkdir(parents=True, exist_ok=True)
    
    # Create template files
    files = [
        (base_path / "README.md", create_readme_template(name, topic, character)),
        (story_dev_path / "01-story-idea.md", create_story_idea_template(name, topic, character)),
        (story_dev_path / "02-narrative.md", create_narrative_template(topic)),
        (story_dev_path / "03-panel-planning.md", create_panel_planning_template(topic)),
    ]
    
    for filepath, content in files:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created: {filepath}")
    
    # Create .gitkeep files for empty directories
    for path in [prompts_path, panels_path]:
        gitkeep = path / ".gitkeep"
        gitkeep.touch()
        print(f"✓ Created: {gitkeep}")
    
    print()
    print("=" * 60)
    print(f"✅ Comic project initialized: {base_path}")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Edit story-development/01-story-idea.md - Define story concept (NO panels)")
    print("2. Edit story-development/02-narrative.md - Write full prose story (NO panels)")
    print("3. Edit story-development/03-panel-planning.md - Plan panels AFTER story")
    print("4. Create 04-storyboard.json - Map narrative to panels")
    print("5. Generate individual-prompts/ files")
    print("6. Run image generation")
    print()
    print("See: .project/agents/image-generation/COMIC-STORY-WORKFLOW.md")


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new comic project with story-first workflow structure"
    )
    parser.add_argument(
        "--output-dir", "-d",
        default=".",
        help="Output directory for the project (default: current directory)"
    )
    parser.add_argument(
        "--name", "-n",
        required=True,
        help="Project name (e.g., 'deep-vein-thrombosis-v1')"
    )
    parser.add_argument(
        "--topic", "-t",
        required=True,
        help="Medical/educational topic (e.g., 'Deep Vein Thrombosis')"
    )
    parser.add_argument(
        "--character", "-c",
        default="Dr. Young Erben",
        help="Main character name (default: 'Dr. Young Erben')"
    )
    
    args = parser.parse_args()
    
    init_project(args.output_dir, args.name, args.topic, args.character)


if __name__ == "__main__":
    main()
