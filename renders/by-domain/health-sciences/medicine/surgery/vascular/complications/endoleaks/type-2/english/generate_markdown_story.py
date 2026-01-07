#!/usr/bin/env python3
"""
Generate markdown story format from storyboard JSON.
Creates full narrative text suitable for reading.
"""

import json
import sys
from pathlib import Path

def generate_markdown_story(storyboard_path, output_path):
    """Generate readable markdown story from storyboard."""
    
    with open(storyboard_path, 'r') as f:
        storyboard = json.load(f)
    
    story_title = storyboard.get('title', 'Vascular Surgery Adventure')
    synopsis = storyboard.get('synopsis', '')
    characters = storyboard.get('characters', [])
    teaching_points = storyboard.get('teaching_points', [])
    panels = storyboard.get('panels', [])
    
    # Build markdown content
    md_content = f"""# {story_title}

## Synopsis
{synopsis}

## Characters
"""
    
    for char in characters:
        md_content += f"- **{char.get('name', '')}**: {char.get('description', '')}\n"
    
    md_content += f"""

## Key Learning Points
"""
    
    for i, point in enumerate(teaching_points, 1):
        md_content += f"{i}. {point}\n"
    
    md_content += f"""

---

## The Story

"""
    
    # Add panels
    current_act = None
    for i, panel in enumerate(panels, 1):
        act = panel.get('act', 1)
        if act != current_act:
            current_act = act
            act_titles = {
                1: "Act 1: Discovery",
                2: "Act 2: Investigation", 
                3: "Act 3: Action",
                4: "Act 4: Resolution"
            }
            md_content += f"\n### {act_titles.get(act, f'Act {act}')}\n\n"
        
        md_content += f"**Panel {i}: {panel.get('title', 'Scene')}**\n\n"
        
        # Setting
        setting = panel.get('setting', '')
        if setting:
            md_content += f"*Setting: {setting}*\n\n"
        
        # Action/Description
        action = panel.get('action', '')
        if action:
            md_content += f"{action}\n\n"
        
        # Dialogue
        dialogue = panel.get('dialogue', '')
        if dialogue:
            md_content += f"{dialogue}\n\n"
        
        # Teaching point for this panel
        teaching = panel.get('teaching_point', '')
        if teaching:
            md_content += f"📚 *Teaching Point: {teaching}*\n\n"
        
        md_content += "---\n\n"
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(md_content)
    
    print(f"Generated markdown story: {output_path}")
    print(f"Total panels: {len(panels)}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python generate_markdown_story.py <storyboard.json> <output.md>")
        sys.exit(1)
    
    storyboard_path = sys.argv[1]
    output_path = sys.argv[2]
    
    generate_markdown_story(storyboard_path, output_path)
