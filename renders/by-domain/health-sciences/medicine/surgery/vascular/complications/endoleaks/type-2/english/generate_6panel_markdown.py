#!/usr/bin/env python3
"""
Generate markdown 6-panel-per-page layout.
Creates visual grid showing story flow.
"""

import json
import sys
from pathlib import Path

def generate_6panel_markdown(image_dir, storyboard_path, output_path):
    """Generate 6-panel grid layout in markdown."""
    
    with open(storyboard_path, 'r') as f:
        storyboard = json.load(f)
    
    story_title = storyboard.get('title', 'Vascular Surgery Adventure')
    panels = storyboard.get('panels', [])
    
    # Build markdown content
    md_content = f"""# {story_title} - 6-Panel Layout

*Visual grid format showing story flow*

---

"""
    
    # Create tables with 3 columns (3 panels per row, 2 rows per "page")
    for page_num in range(0, len(panels), 6):
        page_panels = panels[page_num:page_num+6]
        
        if len(page_panels) == 0:
            break
        
        md_content += f"\n## Page {page_num//6 + 1}\n\n"
        
        # First row (panels 1-3 of this page)
        md_content += "| Panel " + str(page_num+1) if len(page_panels) > 0 else ""
        if len(page_panels) > 1:
            md_content += " | Panel " + str(page_num+2)
        if len(page_panels) > 2:
            md_content += " | Panel " + str(page_num+3)
        md_content += " |\n"
        
        md_content += "|" + "---------|" * min(3, len(page_panels)) + "\n"
        
        # Images row
        md_content += "|"
        for i in range(min(3, len(page_panels))):
            panel_num = page_num + i + 1
            img_path = Path(image_dir) / f"image_{panel_num:03d}.png"
            if img_path.exists():
                md_content += f" ![Panel {panel_num}]({img_path}) |"
            else:
                md_content += f" *[Panel {panel_num} image]*  |"
        md_content += "\n"
        
        # Captions row
        md_content += "|"
        for i in range(min(3, len(page_panels))):
            panel = page_panels[i]
            title = panel.get('title', '')
            dialogue_short = panel.get('dialogue', '')[:50] + "..." if len(panel.get('dialogue', '')) > 50 else panel.get('dialogue', '')
            md_content += f" **{title}**<br>{dialogue_short} |"
        md_content += "\n\n"
        
        # Second row if there are panels 4-6
        if len(page_panels) > 3:
            md_content += "| Panel " + str(page_num+4)
            if len(page_panels) > 4:
                md_content += " | Panel " + str(page_num+5)
            if len(page_panels) > 5:
                md_content += " | Panel " + str(page_num+6)
            md_content += " |\n"
            
            md_content += "|" + "---------|" * min(3, len(page_panels)-3) + "\n"
            
            # Images row
            md_content += "|"
            for i in range(3, min(6, len(page_panels))):
                panel_num = page_num + i + 1
                img_path = Path(image_dir) / f"image_{panel_num:03d}.png"
                if img_path.exists():
                    md_content += f" ![Panel {panel_num}]({img_path}) |"
                else:
                    md_content += f" *[Panel {panel_num} image]* |"
            md_content += "\n"
            
            # Captions row
            md_content += "|"
            for i in range(3, min(6, len(page_panels))):
                panel = page_panels[i]
                title = panel.get('title', '')
                dialogue_short = panel.get('dialogue', '')[:50] + "..." if len(panel.get('dialogue', '')) > 50 else panel.get('dialogue', '')
                md_content += f" **{title}**<br>{dialogue_short} |"
            md_content += "\n"
        
        md_content += "\n---\n\n"
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(md_content)
    
    print(f"Generated 6-panel markdown layout: {output_path}")
    print(f"Total pages: {(len(panels) + 5) // 6}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python generate_6panel_markdown.py <image_dir> <storyboard.json> <output.md>")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    storyboard_path = sys.argv[2]
    output_path = sys.argv[3]
    
    generate_6panel_markdown(image_dir, storyboard_path, output_path)
