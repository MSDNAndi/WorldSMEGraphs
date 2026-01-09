#!/usr/bin/env python3
"""
Create markdown and HTML viewers for all V2 stories
"""

import json
from pathlib import Path

STORIES = [
    {
        "name": "Carotid Artery Stenosis",
        "dir": "carotid-artery-stenosis-v2",
        "panels": 40
    },
    {
        "name": "Acute Limb Ischemia", 
        "dir": "acute-limb-ischemia-v2",
        "panels": 35
    },
    {
        "name": "Diabetic Foot Bypass",
        "dir": "diabetic-foot-bypass-v2",
        "panels": 35
    },
    {
        "name": "Varicose Veins",
        "dir": "varicose-veins-v2",
        "panels": 32
    }
]

def create_markdown_viewer(story_dir, story_name, num_panels):
    """Create 6-panel-per-page markdown viewer"""
    storyboard_file = story_dir / "story-development" / "03-storyboard.json"
    
    # Load storyboard
    with open(storyboard_file, 'r') as f:
        storyboard = json.load(f)
    
    panels = storyboard['panels']
    pages = (len(panels) + 5) // 6
    
    md_content = f'''# {story_name} - Educational Comic Story

**Character**: Dr. Young Erben (Korean, petite, 40s, multilingual vascular surgeon)  
**Total Panels**: {num_panels}

---

'''
    
    for page in range(pages):
        md_content += f'## Page {page + 1}\n\n'
        start_idx = page * 6
        end_idx = min(start_idx + 6, len(panels))
        
        for i in range(start_idx, end_idx):
            panel = panels[i]
            panel_num = panel['panel_number']
            
            md_content += f'### Panel {panel_num}: {panel["title"]}\n\n'
            md_content += f'**Scene**: {panel.get("scene", "N/A")}\n\n'
            
            if panel.get('dialogue'):
                md_content += f'**Dialogue**: {panel["dialogue"]}\n\n'
            
            md_content += f'**Educational Focus**: {panel.get("educational_focus", "N/A")}\n\n'
            md_content += '---\n\n'
    
    # Save
    output_file = story_dir / "comic" / "COMIC-VIEW.md"
    with open(output_file, 'w') as f:
        f.write(md_content)
    
    print(f"✓ Created markdown viewer: {output_file.name}")
    return output_file

def create_html_viewer(story_dir, story_name, num_panels):
    """Create interactive HTML viewer"""
    storyboard_file = story_dir / "story-development" / "03-storyboard.json"
    
    with open(storyboard_file, 'r') as f:
        storyboard = json.load(f)
    
    panels = storyboard['panels']
    pages = (len(panels) + 5) // 6
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{story_name} - Educational Comic</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .nav-buttons {{
            text-align: center;
            margin: 20px 0;
        }}
        .nav-buttons button {{
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
        }}
        .nav-buttons button:hover {{
            background-color: #2980b9;
        }}
        .nav-buttons button:disabled {{
            background-color: #95a5a6;
            cursor: not-allowed;
        }}
        .page {{
            display: none;
        }}
        .page.active {{
            display: block;
        }}
        .panel-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .panel-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .panel-card h3 {{
            color: #34495e;
            margin-top: 0;
        }}
        .panel-card p {{
            margin: 8px 0;
            color: #555;
        }}
        .panel-card strong {{
            color: #2c3e50;
        }}
        .info-box {{
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <h1>{story_name}</h1>
    <div class="info-box">
        <strong>Character:</strong> Dr. Young Erben (Korean, petite, 40s, multilingual vascular surgeon)<br>
        <strong>Total Panels:</strong> {num_panels}<br>
        <strong>Pages:</strong> {pages}
    </div>

'''
    
    for page in range(pages):
        html_content += f'    <div class="page" id="page{page + 1}">\n'
        html_content += f'        <h2>Page {page + 1} of {pages}</h2>\n'
        html_content += '        <div class="panel-grid">\n'
        
        start_idx = page * 6
        end_idx = min(start_idx + 6, len(panels))
        
        for i in range(start_idx, end_idx):
            panel = panels[i]
            panel_num = panel['panel_number']
            
            html_content += '            <div class="panel-card">\n'
            html_content += f'                <h3>Panel {panel_num}: {panel["title"]}</h3>\n'
            html_content += f'                <p><strong>Scene:</strong> {panel.get("scene", "N/A")}</p>\n'
            
            if panel.get('dialogue'):
                html_content += f'                <p><strong>Dialogue:</strong> {panel["dialogue"]}</p>\n'
            
            html_content += f'                <p><strong>Focus:</strong> {panel.get("educational_focus", "N/A")}</p>\n'
            html_content += '            </div>\n'
        
        html_content += '        </div>\n'
        html_content += '    </div>\n\n'
    
    html_content += '''
    <div class="nav-buttons">
        <button id="prevBtn" onclick="changePage(-1)">Previous</button>
        <span id="pageInfo"></span>
        <button id="nextBtn" onclick="changePage(1)">Next</button>
    </div>

    <script>
        let currentPage = 1;
        const totalPages = ''' + str(pages) + ''';

        function showPage(n) {
            const pages = document.querySelectorAll('.page');
            if (n > totalPages) currentPage = totalPages;
            if (n < 1) currentPage = 1;
            
            pages.forEach(page => page.classList.remove('active'));
            document.getElementById('page' + currentPage).classList.add('active');
            
            document.getElementById('prevBtn').disabled = (currentPage === 1);
            document.getElementById('nextBtn').disabled = (currentPage === totalPages);
            document.getElementById('pageInfo').textContent = `Page ${currentPage} of ${totalPages}`;
        }

        function changePage(n) {
            currentPage += n;
            showPage(currentPage);
        }

        // Show first page on load
        showPage(1);
    </script>
</body>
</html>'''
    
    output_file = story_dir / "comic" / "comic-viewer.html"
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created HTML viewer: {output_file.name}")
    return output_file

def main():
    base_dir = Path("renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english")
    
    for story in STORIES:
        print(f"\n{'='*60}")
        print(f"Creating viewers for: {story['name']}")
        print(f"{'='*60}")
        
        story_dir = base_dir / story['dir']
        
        try:
            # Create markdown viewer
            create_markdown_viewer(story_dir, story['name'], story['panels'])
            
            # Create HTML viewer
            create_html_viewer(story_dir, story['name'], story['panels'])
            
        except Exception as e:
            print(f"✗ Error for {story['name']}: {str(e)}")
    
    print(f"\n{'='*60}")
    print("All viewers created!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
