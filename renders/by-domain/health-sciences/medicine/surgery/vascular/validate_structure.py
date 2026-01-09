#!/usr/bin/env python3
"""
Validate vascular surgery render structure.

This script validates that:
1. All comic directories have the three required viewing files
2. All image references in viewing files are valid
3. Directory structure aligns with ontology
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Set

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_viewing_files(comic_dir: Path) -> Tuple[bool, List[str]]:
    """Check if all three viewing files exist."""
    required_files = [
        '6-panel-grid-view.md',
        'continuous-story-view.md',
        'pictures-only-view.md'
    ]
    
    issues = []
    for file in required_files:
        file_path = comic_dir / file
        if not file_path.exists():
            issues.append(f"Missing: {file}")
    
    return len(issues) == 0, issues

def check_image_references(viewing_file: Path, comic_dir: Path) -> Tuple[bool, List[str]]:
    """Check if all image references in viewing file are valid."""
    if not viewing_file.exists():
        return False, [f"File does not exist: {viewing_file}"]
    
    issues = []
    
    try:
        with open(viewing_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references: ![...](path)
        img_pattern = r'!\[.*?\]\((.*?)\)'
        matches = re.findall(img_pattern, content)
        
        for img_path in matches:
            # Resolve relative path
            full_path = (viewing_file.parent / img_path).resolve()
            if not full_path.exists():
                issues.append(f"Broken image link: {img_path}")
    
    except Exception as e:
        issues.append(f"Error reading file: {e}")
    
    return len(issues) == 0, issues

def check_directory_structure(base_path: Path) -> Tuple[bool, List[str]]:
    """Check if directory structure matches ontology."""
    issues = []
    
    # Required top-level categories
    required_dirs = ['procedures', 'pathology', 'complications']
    
    for dir_name in required_dirs:
        dir_path = base_path / dir_name
        if not dir_path.exists():
            issues.append(f"Missing required directory: {dir_name}")
    
    # Check for misplaced comics (should not be any comics directly under vascular/)
    for item in base_path.iterdir():
        if item.is_dir() and item.name not in required_dirs + ['english', '.git']:
            # Check if it contains comics
            comics = list(item.rglob('comic'))
            if comics:
                issues.append(f"Comics found in unexpected location: {item.name}")
    
    return len(issues) == 0, issues

def find_all_comics(base_path: Path) -> List[Path]:
    """Find all comic directories."""
    comics = []
    for comic_dir in base_path.rglob('comic'):
        if comic_dir.is_dir():
            # Check if it has panels-gpt
            if (comic_dir / 'panels-gpt').exists():
                comics.append(comic_dir)
    return comics

def main():
    base_path = Path('/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/renders/by-domain/health-sciences/medicine/surgery/vascular')
    
    print(f"{BLUE}=== Vascular Surgery Render Structure Validation ==={RESET}\n")
    
    # Check directory structure
    print(f"{BLUE}1. Checking directory structure...{RESET}")
    struct_ok, struct_issues = check_directory_structure(base_path)
    if struct_ok:
        print(f"   {GREEN}✓ Directory structure is correct{RESET}")
    else:
        print(f"   {RED}✗ Directory structure issues:{RESET}")
        for issue in struct_issues:
            print(f"     - {issue}")
    print()
    
    # Find all comics
    print(f"{BLUE}2. Finding comic directories...{RESET}")
    comics = find_all_comics(base_path)
    print(f"   Found {len(comics)} comic directories")
    print()
    
    # Check each comic
    print(f"{BLUE}3. Validating comics...{RESET}")
    
    total_issues = 0
    comics_ok = 0
    comics_with_issues = 0
    
    for comic_dir in sorted(comics):
        relative_path = comic_dir.relative_to(base_path)
        
        # Check viewing files
        viewing_ok, viewing_issues = check_viewing_files(comic_dir)
        
        # Check image references in viewing files
        img_issues = []
        for viewing_file in ['6-panel-grid-view.md', 'continuous-story-view.md', 'pictures-only-view.md']:
            file_path = comic_dir / viewing_file
            if file_path.exists():
                ok, issues = check_image_references(file_path, comic_dir)
                img_issues.extend(issues)
        
        all_issues = viewing_issues + img_issues
        
        if not all_issues:
            comics_ok += 1
            print(f"   {GREEN}✓{RESET} {relative_path}")
        else:
            comics_with_issues += 1
            total_issues += len(all_issues)
            print(f"   {RED}✗{RESET} {relative_path}")
            for issue in all_issues:
                print(f"     {YELLOW}- {issue}{RESET}")
    
    print()
    
    # Summary
    print(f"{BLUE}=== Summary ==={RESET}")
    print(f"Comics validated: {len(comics)}")
    print(f"{GREEN}Comics OK: {comics_ok}{RESET}")
    if comics_with_issues > 0:
        print(f"{RED}Comics with issues: {comics_with_issues}{RESET}")
        print(f"{RED}Total issues found: {total_issues}{RESET}")
    else:
        print(f"{GREEN}All comics validated successfully! ✓{RESET}")
    
    print()
    
    # Exit code
    if total_issues > 0 or not struct_ok:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
