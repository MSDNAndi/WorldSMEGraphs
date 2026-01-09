#!/usr/bin/env python3
"""
Generate viewing markdown files for comic directories.
Creates: 6-panel grid view, continuous story view, pictures-only view.
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple

def find_comic_directories(base_path: str) -> List[Path]:
    """Find all comic directories with panels-gpt folders."""
    comic_dirs = []
    base = Path(base_path)
    
    for comic_dir in base.rglob("comic"):
        panels_dir = comic_dir / "panels-gpt"
        if panels_dir.exists() and panels_dir.is_dir():
            # Check if there are images
            images = list(panels_dir.glob("image_*.png"))
            if images:
                comic_dirs.append(comic_dir)
    
    return comic_dirs

def get_panel_images(panels_dir: Path) -> List[Tuple[int, Path]]:
    """Get sorted list of panel images with their numbers.
    
    This function handles two scenarios:
    1. Properly numbered images: image_001_*, image_002_*, etc.
    2. Broken numbering (all image_001_*): Use timestamp ordering
    
    Returns list of (panel_number, path) tuples.
    """
    images = []
    for img in panels_dir.glob("image_*.png"):
        match = re.match(r'image_(\d+)_(\d{8}_\d{6})_([a-f0-9]+)', img.name)
        if match:
            panel_num = int(match.group(1))
            timestamp = match.group(2)
            images.append((panel_num, timestamp, img))
    
    # Check if all images have the same panel number (broken numbering)
    panel_nums = set(p[0] for p in images)
    
    if len(panel_nums) == 1 and len(images) > 1:
        # All images have the same panel number - use timestamp ordering
        # This happens when image generator was called without --output
        print(f"  Note: All images numbered as panel {list(panel_nums)[0]}, using timestamp order")
        
        # Sort by timestamp
        images.sort(key=lambda x: x[1])
        
        # Group by unique hash to avoid duplicates, take first of each timestamp
        seen_hashes = set()
        unique_images = []
        panel_counter = 1
        for _, timestamp, path in images:
            # Extract hash from filename
            hash_match = re.match(r'image_\d+_\d+_\d+_([a-f0-9]+)', path.name)
            img_hash = hash_match.group(1) if hash_match else path.name
            
            if img_hash not in seen_hashes:
                seen_hashes.add(img_hash)
                unique_images.append((panel_counter, path))
                panel_counter += 1
        
        return unique_images
    
    # Normal case: properly numbered images
    # Sort by panel number and take the first occurrence of each
    images.sort(key=lambda x: x[0])
    
    # Deduplicate - keep first instance of each panel number
    seen = set()
    unique_images = []
    for num, timestamp, path in images:
        if num not in seen:
            seen.add(num)
            unique_images.append((num, path))
    
    return unique_images

def read_storyboard(comic_dir: Path) -> Dict:
    """Read storyboard.json if it exists."""
    storyboard_file = comic_dir / "storyboard.json"
    if storyboard_file.exists():
        try:
            with open(storyboard_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def read_readme(comic_dir: Path) -> Tuple[str, str]:
    """Extract title and description from README.md."""
    readme_file = comic_dir / "README.md"
    title = "Medical Educational Comic"
    description = ""
    
    if readme_file.exists():
        try:
            with open(readme_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if lines:
                    # First line after # is usually the title
                    for line in lines[:10]:
                        if line.startswith('# '):
                            title = line[2:].strip()
                            break
                # Get a short description
                for line in lines[1:20]:
                    if line.strip() and not line.startswith('#') and not line.startswith('**'):
                        description = line.strip()
                        if len(description) > 200:
                            description = description[:197] + "..."
                        break
        except:
            pass
    
    return title, description

def generate_6_panel_grid(comic_dir: Path, images: List[Tuple[int, Path]], title: str) -> str:
    """Generate 6-panel grid view markdown."""
    rel_path = "panels-gpt"
    
    content = [
        f"# {title}",
        "",
        "## 6-Panel Grid View",
        "",
        "This view shows 6 panels at a time in a 2x3 grid format for easy reading.",
        "",
    ]
    
    # Group into pages of 6
    for page_num, i in enumerate(range(0, len(images), 6), 1):
        page_images = images[i:i+6]
        content.append(f"## Page {page_num}")
        content.append("")
        
        # Create 2x3 grid
        for row in range(0, len(page_images), 3):
            row_images = page_images[row:row+3]
            
            # Panel numbers
            panel_line = " | ".join([f"**Panel {num}**" for num, _ in row_images])
            content.append("| " + panel_line + " |")
            
            # Separator
            content.append("| " + " | ".join(["---"] * len(row_images)) + " |")
            
            # Images
            img_line = " | ".join([f"![Panel {num}]({rel_path}/{path.name})" for num, path in row_images])
            content.append("| " + img_line + " |")
            content.append("")
        
        content.append("---")
        content.append("")
    
    return "\n".join(content)

def generate_continuous_story(comic_dir: Path, images: List[Tuple[int, Path]], title: str, storyboard: Dict) -> str:
    """Generate continuous story view with dialogue."""
    rel_path = "panels-gpt"
    
    content = [
        f"# {title}",
        "",
        "## Continuous Story View",
        "",
        "Read through the complete story from beginning to end with all panels in sequence.",
        "",
        "---",
        "",
    ]
    
    for num, path in images:
        content.append(f"### Panel {num}")
        content.append("")
        content.append(f"![Panel {num}]({rel_path}/{path.name})")
        content.append("")
        
        # Try to add dialogue from storyboard if available
        if storyboard and 'panels' in storyboard:
            for panel in storyboard['panels']:
                if panel.get('panel') == num or panel.get('panel_number') == num:
                    if 'dialogue' in panel and panel['dialogue']:
                        content.append(f"**Dialogue**: {panel['dialogue']}")
                        content.append("")
                    if 'caption' in panel and panel['caption']:
                        content.append(f"**Caption**: {panel['caption']}")
                        content.append("")
                    break
        
        content.append("---")
        content.append("")
    
    return "\n".join(content)

def generate_pictures_only(comic_dir: Path, images: List[Tuple[int, Path]], title: str) -> str:
    """Generate pictures-only view (no text, just images)."""
    rel_path = "panels-gpt"
    
    content = [
        f"# {title}",
        "",
        "## Pictures Only View",
        "",
        "Pure visual storytelling - all panels without text or dialogue.",
        "",
        "---",
        "",
    ]
    
    for num, path in images:
        content.append(f"![Panel {num}]({rel_path}/{path.name})")
        content.append("")
    
    return "\n".join(content)

def process_comic_directory(comic_dir: Path):
    """Process a single comic directory and generate all viewing files."""
    panels_dir = comic_dir / "panels-gpt"
    images = get_panel_images(panels_dir)
    
    if not images:
        print(f"No images found in {comic_dir}")
        return
    
    print(f"Processing {comic_dir} ({len(images)} panels)...")
    
    title, description = read_readme(comic_dir)
    storyboard = read_storyboard(comic_dir)
    
    # Generate 6-panel grid view
    grid_content = generate_6_panel_grid(comic_dir, images, title)
    grid_file = comic_dir / "6-panel-grid-view.md"
    with open(grid_file, 'w', encoding='utf-8') as f:
        f.write(grid_content)
    print(f"  Created: {grid_file.name}")
    
    # Generate continuous story view
    story_content = generate_continuous_story(comic_dir, images, title, storyboard)
    story_file = comic_dir / "continuous-story-view.md"
    with open(story_file, 'w', encoding='utf-8') as f:
        f.write(story_content)
    print(f"  Created: {story_file.name}")
    
    # Generate pictures-only view
    pictures_content = generate_pictures_only(comic_dir, images, title)
    pictures_file = comic_dir / "pictures-only-view.md"
    with open(pictures_file, 'w', encoding='utf-8') as f:
        f.write(pictures_content)
    print(f"  Created: {pictures_file.name}")

def main():
    base_path = "/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/renders/by-domain/health-sciences/medicine/surgery/vascular"
    
    print(f"Searching for comic directories under {base_path}...")
    comic_dirs = find_comic_directories(base_path)
    
    print(f"\nFound {len(comic_dirs)} comic directories")
    print("=" * 60)
    
    for comic_dir in sorted(comic_dirs):
        try:
            process_comic_directory(comic_dir)
        except Exception as e:
            print(f"Error processing {comic_dir}: {e}")
    
    print("\n" + "=" * 60)
    print(f"Completed processing {len(comic_dirs)} comic directories")

if __name__ == "__main__":
    main()
