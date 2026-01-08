#!/usr/bin/env python3
"""
Generate HTML comic with styled layout.
Creates interactive web page with embedded CSS.
"""

import json
import sys
from pathlib import Path
import base64

def generate_html_comic(storyboard_path, image_dir, output_path):
    """Generate styled HTML comic."""
    
    with open(storyboard_path, 'r') as f:
        storyboard = json.load(f)
    
    story_title = storyboard.get('title', 'Vascular Surgery Adventure')
    synopsis = storyboard.get('synopsis', '')
    characters = storyboard.get('characters', [])
    panels = storyboard.get('panels', [])
    
    # Build HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{story_title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Comic Sans MS', 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        h1 {{
            font-size: 3em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .synopsis {{
            font-size: 1.2em;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .characters {{
            background: #f8f9fa;
            padding: 30px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }}
        
        .character {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            flex: 0 1 200px;
        }}
        
        .character h3 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .comic-grid {{
            padding: 40px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }}
        
        .panel {{
            background: white;
            border: 4px solid #333;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .panel:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        }}
        
        .panel-header {{
            background: #333;
            color: white;
            padding: 10px;
            font-weight: bold;
            text-align: center;
        }}
        
        .panel-image {{
            width: 100%;
            height: auto;
            display: block;
        }}
        
        .panel-caption {{
            padding: 15px;
            background: #f8f9fa;
            min-height: 80px;
        }}
        
        .panel-dialogue {{
            font-style: italic;
            margin-bottom: 10px;
            color: #555;
        }}
        
        .panel-teaching {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin-top: 10px;
            font-size: 0.9em;
        }}
        
        footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        .act-divider {{
            grid-column: 1 / -1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            border-radius: 10px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{story_title}</h1>
            <div class="synopsis">{synopsis}</div>
        </header>
        
        <div class="characters">
"""
    
    # Add characters
    for char in characters:
        html_content += f"""
            <div class="character">
                <h3>{char.get('name', '')}</h3>
                <p>{char.get('description', '')}</p>
            </div>
"""
    
    html_content += """
        </div>
        
        <div class="comic-grid">
"""
    
    # Add panels with act dividers
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
            html_content += f"""
            <div class="act-divider">
                {act_titles.get(act, f'Act {act}')}
            </div>
"""
        
        img_path = Path(image_dir) / f"image_{i:03d}.png"
        img_src = f"panels-gpt/image_{i:03d}.png" if img_path.exists() else "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23ddd' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' text-anchor='middle' fill='%23999'%3EPanel {i}%3C/text%3E%3C/svg%3E"
        
        html_content += f"""
            <div class="panel">
                <div class="panel-header">Panel {i}: {panel.get('title', 'Scene')}</div>
                <img src="{img_src}" alt="Panel {i}" class="panel-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'400\\' height=\\'300\\'%3E%3Crect fill=\\'%23ddd\\' width=\\'400\\' height=\\'300\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' fill=\\'%23999\\'%3EPanel {i}%3C/text%3E%3C/svg%3E'">
                <div class="panel-caption">
                    <div class="panel-dialogue">{panel.get('dialogue', '')}</div>
"""
        
        if panel.get('teaching_point'):
            html_content += f"""
                    <div class="panel-teaching">
                        📚 {panel.get('teaching_point', '')}
                    </div>
"""
        
        html_content += """
                </div>
            </div>
"""
    
    html_content += """
        </div>
        
        <footer>
            <p>&copy; 2026 Vascular Surgery Educational Comics | Dora-Inspired Medical Education</p>
        </footer>
    </div>
</body>
</html>
"""
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(html_content)
    
    print(f"Generated HTML comic: {output_path}")
    print(f"Total panels: {len(panels)}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python generate_html_comic.py <storyboard.json> <image_dir> <output.html>")
        sys.exit(1)
    
    storyboard_path = sys.argv[1]
    image_dir = sys.argv[2]
    output_path = sys.argv[3]
    
    generate_html_comic(storyboard_path, image_dir, output_path)
