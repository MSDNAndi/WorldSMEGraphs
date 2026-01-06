#!/usr/bin/env python3
"""
Render Index Generator

Scans the renders/ directory and generates render-index.yaml

Usage:
    python generate_render_index.py
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import hashlib

def get_file_hash(filepath):
    """Calculate MD5 hash of file."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def get_file_info(filepath):
    """Extract basic file information."""
    stat = os.stat(filepath)
    return {
        'size_bytes': stat.st_size,
        'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
        'hash': get_file_hash(filepath)
    }

def parse_domain_path(render_path, renders_root):
    """Extract domain path from render file path."""
    relative = os.path.relpath(render_path, os.path.join(renders_root, 'by-domain'))
    parts = Path(relative).parts
    
    languages = {'english', 'german', 'french', 'spanish', 'chinese', 'japanese'}
    
    for i, part in enumerate(parts):
        if part.lower() in languages:
            domain_path = '/'.join(parts[:i])
            language = part
            filename = '/'.join(parts[i+1:])
            return domain_path, language, filename
    
    if len(parts) > 1:
        return '/'.join(parts[:-1]), 'unknown', parts[-1]
    return 'unknown', 'unknown', parts[-1] if parts else 'unknown'

def scan_renders_directory(renders_root):
    """Scan renders directory and build index."""
    by_domain_path = os.path.join(renders_root, 'by-domain')
    
    renders = []
    stats = {
        'total_files': 0,
        'by_language': defaultdict(int),
        'by_domain': defaultdict(int),
        'by_extension': defaultdict(int),
        'total_size_mb': 0
    }
    
    for root, dirs, files in os.walk(by_domain_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_info = get_file_info(filepath)
            
            domain_path, language, rel_filename = parse_domain_path(filepath, renders_root)
            ext = Path(filename).suffix.lower()
            
            render_entry = {
                'id': f"render-{hashlib.md5(filepath.encode()).hexdigest()[:12]}",
                'path': os.path.relpath(filepath, renders_root),
                'filename': filename,
                'domain_path': domain_path,
                'language': language,
                'extension': ext,
                'size_bytes': file_info['size_bytes']
            }
            
            renders.append(render_entry)
            
            stats['total_files'] += 1
            stats['by_language'][language] += 1
            stats['by_domain'][domain_path] += 1
            stats['by_extension'][ext] += 1
            stats['total_size_mb'] += file_info['size_bytes'] / (1024 * 1024)
    
    return {
        'renders': renders,
        'statistics': {
            'total_files': stats['total_files'],
            'total_size_mb': round(stats['total_size_mb'], 2),
            'by_language': dict(stats['by_language']),
            'by_domain': dict(stats['by_domain']),
            'by_extension': dict(stats['by_extension'])
        }
    }

def generate_render_index(renders_root):
    """Generate render index YAML file."""
    print("Scanning renders directory...")
    index_data = scan_renders_directory(renders_root)
    
    index_data['metadata'] = {
        'generated': datetime.utcnow().isoformat() + 'Z',
        'version': '1.0.0'
    }
    
    index_data['renders'].sort(key=lambda r: (r['domain_path'], r['language'], r['filename']))
    
    output_path = os.path.join(renders_root, '_metadata', 'render-index.yaml')
    
    with open(output_path, 'w') as f:
        yaml.dump(index_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"Generated: {output_path}")
    print(f"Total: {index_data['statistics']['total_files']} files")
    return index_data

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    renders_root = os.path.dirname(os.path.dirname(script_dir))
    generate_render_index(renders_root)
