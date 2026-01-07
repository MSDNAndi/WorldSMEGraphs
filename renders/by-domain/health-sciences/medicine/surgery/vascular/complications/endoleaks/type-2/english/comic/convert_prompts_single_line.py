#!/usr/bin/env python3
"""
Convert multi-line panel prompts to single-line format for image generator.
Each panel's complete prompt becomes a single line.
"""

import re
from pathlib import Path

def convert_to_single_line(input_file: Path, output_file: Path):
    """Convert multi-line prompts to single-line format."""
    with input_file.open('r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by panel markers
    panels = re.split(r'={5,}\s+PANEL\s+\d+:', content)
    
    # Remove empty first element if present
    if panels and not panels[0].strip():
        panels = panels[1:]
    
    single_line_prompts = []
    
    for idx, panel in enumerate(panels, 1):
        # Clean up the panel content
        lines = panel.strip().split('\n')
        
        # Remove section headers (lines starting with ===)
        cleaned_lines = []
        for line in lines:
            # Skip section headers and empty lines
            if line.strip().startswith('==='):
                continue
            if not line.strip():
                continue
            cleaned_lines.append(line.strip())
        
        # Join into single line, space-separated
        single_line = ' '.join(cleaned_lines)
        
        # Add to output
        if single_line:
            single_line_prompts.append(single_line)
    
    # Write output
    with output_file.open('w', encoding='utf-8') as f:
        for prompt in single_line_prompts:
            f.write(prompt + '\n')
    
    print(f"✓ Converted {len(single_line_prompts)} panel prompts")
    print(f"✓ Output written to: {output_file}")
    
    # Show statistics
    total_chars = sum(len(p) for p in single_line_prompts)
    avg_chars = total_chars / len(single_line_prompts) if single_line_prompts else 0
    print(f"✓ Total characters: {total_chars:,} ({avg_chars:,.0f} avg per panel)")

if __name__ == '__main__':
    comic_dir = Path(__file__).parent
    input_file = comic_dir / 'gpt-prompts-v2-detailed-all-panels.txt'
    output_file = comic_dir / 'gpt-prompts-v2-single-line.txt'
    
    convert_to_single_line(input_file, output_file)
