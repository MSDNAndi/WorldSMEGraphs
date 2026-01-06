#!/usr/bin/env python3
"""
AKU Usage Matrix Generator

Creates a matrix showing which renders use which AKUs.
This helps track:
- Which AKUs are rendered (coverage)
- Which renders depend on which AKUs (impact analysis)
- Orphaned renders (renders with no valid AKU references)

Usage:
    python generate_aku_usage_matrix.py
"""

import os
import json
import yaml
import re
from collections import defaultdict
from datetime import datetime

def find_aku_files(domain_root):
    """Find all AKU JSON files in domain hierarchy."""
    aku_files = []
    
    for root, dirs, files in os.walk(domain_root):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            if filename.endswith('.json') and ('aku' in filename.lower() or 'akus' in root):
                filepath = os.path.join(root, filename)
                # Extract AKU ID from file
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        aku_id = data.get('@id') or data.get('id') or filename
                        domain_path = os.path.relpath(os.path.dirname(filepath), domain_root)
                        aku_files.append({
                            'id': aku_id,
                            'path': filepath,
                            'domain_path': domain_path,
                            'filename': filename
                        })
                except (json.JSONDecodeError, IOError):
                    pass  # Skip invalid files
    
    return aku_files

def extract_aku_references(render_file):
    """Extract AKU references from a render file."""
    references = set()
    
    try:
        with open(render_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            # Look for common AKU reference patterns
            # Pattern 1: aku-xxx-yyy-zzz
            pattern1 = r'\baku-[\w\-]+\b'
            references.update(re.findall(pattern1, content, re.IGNORECASE))
            
            # Pattern 2: domain/path/to/akus/file.json
            pattern2 = r'domain/[^\s\)]+/akus/[^\s\)]+\.json'
            references.update(re.findall(pattern2, content))
            
            # Pattern 3: AKU IDs in metadata blocks
            if content.startswith('---'):
                # YAML frontmatter
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        metadata = yaml.safe_load(parts[1])
                        if isinstance(metadata, dict):
                            # Look for aku_ids or source_akus fields
                            if 'aku_ids' in metadata:
                                refs = metadata['aku_ids']
                                if isinstance(refs, list):
                                    references.update(refs)
                            if 'source' in metadata and isinstance(metadata['source'], dict):
                                if 'aku_ids' in metadata['source']:
                                    refs = metadata['source']['aku_ids']
                                    if isinstance(refs, list):
                                        references.update(refs)
                    except yaml.YAMLError:
                        pass  # Ignore invalid YAML in frontmatter
    
    except IOError:
        pass  # Skip files that cannot be read
    
    return list(references)

def scan_render_aku_usage(renders_root):
    """Scan renders for AKU references."""
    by_domain_path = os.path.join(renders_root, 'by-domain')
    
    if not os.path.exists(by_domain_path):
        return []
    
    render_usage = []
    
    for root, dirs, files in os.walk(by_domain_path):
        for filename in files:
            # Only scan text-based files
            if filename.endswith(('.md', '.html', '.txt')):
                filepath = os.path.join(root, filename)
                aku_refs = extract_aku_references(filepath)
                
                if aku_refs:
                    relative_path = os.path.relpath(filepath, renders_root)
                    render_usage.append({
                        'render_path': relative_path,
                        'render_file': filename,
                        'aku_references': aku_refs,
                        'reference_count': len(aku_refs)
                    })
    
    return render_usage

def generate_aku_usage_matrix(repo_root):
    """Generate AKU usage matrix."""
    domain_root = os.path.join(repo_root, 'domain')
    renders_root = os.path.join(repo_root, 'renders')
    
    print("Finding AKUs...")
    akus = find_aku_files(domain_root)
    print(f"Found {len(akus)} AKU files")
    
    print("\nScanning renders for AKU references...")
    render_usage = scan_render_aku_usage(renders_root)
    print(f"Found {len(render_usage)} renders with AKU references")
    
    # Build matrix
    aku_to_renders = defaultdict(list)
    render_to_akus = {}
    
    for usage in render_usage:
        render_path = usage['render_path']
        render_to_akus[render_path] = usage['aku_references']
        
        for aku_ref in usage['aku_references']:
            aku_to_renders[aku_ref].append(render_path)
    
    # Calculate statistics
    total_akus = len(akus)
    total_renders = len(render_usage)
    akus_with_renders = len(aku_to_renders)
    renders_with_akus = len(render_to_akus)
    
    coverage_pct = (akus_with_renders / total_akus * 100) if total_akus > 0 else 0
    
    # Build output data
    matrix_data = {
        'metadata': {
            'generated': datetime.utcnow().isoformat() + 'Z',
            'version': '1.0.0'
        },
        'statistics': {
            'total_akus': total_akus,
            'total_renders_scanned': total_renders,
            'akus_with_renders': akus_with_renders,
            'renders_with_aku_references': renders_with_akus,
            'coverage_percentage': round(coverage_pct, 2)
        },
        'aku_to_renders': {k: sorted(v) for k, v in sorted(aku_to_renders.items())},
        'render_to_akus': {k: sorted(v) for k, v in sorted(render_to_akus.items())}
    }
    
    # Write output
    output_path = os.path.join(renders_root, '_metadata', 'aku-usage-matrix.yaml')
    with open(output_path, 'w') as f:
        yaml.dump(matrix_data, f, default_flow_style=False, sort_keys=False)
    
    # Print summary
    print("\n" + "="*70)
    print("AKU Usage Matrix Generation Complete")
    print("="*70)
    print(f"Total AKUs: {total_akus}")
    print(f"AKUs with renders: {akus_with_renders} ({coverage_pct:.1f}%)")
    print(f"Total renders scanned: {total_renders}")
    print(f"Renders with AKU refs: {renders_with_akus}")
    print(f"\nTop 10 most referenced AKUs:")
    top_akus = sorted(aku_to_renders.items(), key=lambda x: len(x[1]), reverse=True)[:10]
    for aku, renders in top_akus:
        print(f"  {aku}: {len(renders)} renders")
    print(f"\nOutput: {output_path}")
    print("="*70)
    
    return matrix_data

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
    generate_aku_usage_matrix(repo_root)
