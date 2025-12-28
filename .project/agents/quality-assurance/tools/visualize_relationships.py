#!/usr/bin/env python3
"""
SKOS Relationship Visualizer

Creates text-based and Mermaid diagram visualizations of SKOS relationships
in AKUs, showing broader/narrower/related concept hierarchies.

Usage:
    python visualize_relationships.py path/to/aku.json
    python visualize_relationships.py --directory path/to/akus/
    python visualize_relationships.py --graph-all
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class RelationshipVisualizer:
    """Visualizes SKOS relationships in AKUs."""
    
    def __init__(self):
        self.akus = {}
        self.relationships = defaultdict(lambda: {'broader': [], 'narrower': [], 'related': []})
    
    def load_aku(self, aku_path: Path) -> Dict:
        """Load an AKU from file."""
        with open(aku_path, 'r') as f:
            return json.load(f)
    
    def extract_relationships(self, aku: Dict, aku_id: str):
        """Extract SKOS relationships from an AKU."""
        relationships = aku.get('relationships', {})
        
        # Extract broader concepts
        if 'skos:broader' in relationships:
            broader = relationships['skos:broader']
            if isinstance(broader, list):
                for item in broader:
                    if isinstance(item, dict) and '@id' in item:
                        target_id = item['@id'].replace('wsmg:', '').replace('wsmg-econ:', '').replace('wsmg-med:', '')
                        self.relationships[aku_id]['broader'].append(target_id)
        
        # Extract narrower concepts
        if 'skos:narrower' in relationships:
            narrower = relationships['skos:narrower']
            if isinstance(narrower, list):
                for item in narrower:
                    if isinstance(item, dict) and '@id' in item:
                        target_id = item['@id'].replace('wsmg:', '').replace('wsmg-econ:', '').replace('wsmg-med:', '')
                        self.relationships[aku_id]['narrower'].append(target_id)
        
        # Extract related concepts
        if 'skos:related' in relationships:
            related = relationships['skos:related']
            if isinstance(related, list):
                for item in related:
                    if isinstance(item, dict) and '@id' in item:
                        target_id = item['@id'].replace('wsmg:', '').replace('wsmg-econ:', '').replace('wsmg-med:', '')
                        self.relationships[aku_id]['related'].append(target_id)
    
    def generate_tree_view(self, aku_id: str, aku: Dict) -> str:
        """Generate ASCII tree view of relationships."""
        lines = []
        label = aku.get('skos:prefLabel', aku_id)
        
        lines.append(f"\n{'='*70}")
        lines.append(f"CONCEPT: {label}")
        lines.append(f"ID: {aku_id}")
        lines.append(f"{'='*70}")
        
        rels = self.relationships[aku_id]
        
        # Broader (parent) concepts
        if rels['broader']:
            lines.append("\n📈 BROADER CONCEPTS (Parents):")
            for broader_id in rels['broader']:
                lines.append(f"  ↑ {broader_id}")
        
        # Current concept
        lines.append(f"\n🎯 CURRENT: {label}")
        
        # Narrower (child) concepts
        if rels['narrower']:
            lines.append("\n📉 NARROWER CONCEPTS (Children):")
            for narrower_id in rels['narrower']:
                lines.append(f"  ↓ {narrower_id}")
        
        # Related concepts
        if rels['related']:
            lines.append("\n🔗 RELATED CONCEPTS (Siblings/Associates):")
            for related_id in rels['related']:
                lines.append(f"  ↔ {related_id}")
        
        # External ontology links
        external_links = []
        for field in ['skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch']:
            if field in aku:
                matches = aku[field] if isinstance(aku[field], list) else [aku[field]]
                external_links.extend(matches)
        
        if external_links:
            lines.append("\n🌐 EXTERNAL ONTOLOGY LINKS:")
            for link in external_links[:3]:  # Show first 3
                if 'snomed' in link:
                    lines.append(f"  → SNOMED CT: {link}")
                elif 'fibo' in link:
                    lines.append(f"  → FIBO: {link}")
                elif 'wikidata' in link:
                    lines.append(f"  → Wikidata: {link}")
                elif 'dbpedia' in link:
                    lines.append(f"  → DBpedia: {link}")
                else:
                    lines.append(f"  → {link}")
            
            if len(external_links) > 3:
                lines.append(f"  ... and {len(external_links) - 3} more")
        
        lines.append(f"\n{'='*70}\n")
        
        return '\n'.join(lines)
    
    def generate_mermaid_diagram(self, aku_id: str, aku: Dict) -> str:
        """Generate Mermaid flowchart diagram."""
        lines = []
        label = aku.get('skos:prefLabel', aku_id).replace('"', "'")
        
        lines.append("```mermaid")
        lines.append("graph TD")
        lines.append(f"    %% SKOS Concept Hierarchy for: {label}")
        
        # Current node (highlighted)
        safe_id = aku_id.replace('-', '_').replace(':', '_')
        lines.append(f"    {safe_id}[\"{label}\"]")
        lines.append(f"    style {safe_id} fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff")
        
        rels = self.relationships[aku_id]
        
        # Broader concepts
        for broader_id in rels['broader']:
            safe_broader = broader_id.replace('-', '_').replace(':', '_')
            broader_label = broader_id.replace('-', ' ').title()
            lines.append(f"    {safe_broader}[\"{broader_label}\"]")
            lines.append(f"    {safe_broader} -->|skos:broader| {safe_id}")
            lines.append(f"    style {safe_broader} fill:#2196F3,stroke:#1976D2,stroke-width:2px,color:#fff")
        
        # Narrower concepts
        for narrower_id in rels['narrower']:
            safe_narrower = narrower_id.replace('-', '_').replace(':', '_')
            narrower_label = narrower_id.replace('-', ' ').title()
            lines.append(f"    {safe_narrower}[\"{narrower_label}\"]")
            lines.append(f"    {safe_id} -->|skos:narrower| {safe_narrower}")
            lines.append(f"    style {safe_narrower} fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#fff")
        
        # Related concepts
        for related_id in rels['related']:
            safe_related = related_id.replace('-', '_').replace(':', '_')
            related_label = related_id.replace('-', ' ').title()
            lines.append(f"    {safe_related}[\"{related_label}\"]")
            lines.append(f"    {safe_id} -.->|skos:related| {safe_related}")
            lines.append(f"    style {safe_related} fill:#9C27B0,stroke:#7B1FA2,stroke-width:2px,color:#fff")
        
        lines.append("```")
        
        return '\n'.join(lines)
    
    def generate_domain_graph(self, domain_name: str, akus: List[Dict]) -> str:
        """Generate domain-wide Mermaid graph."""
        lines = []
        lines.append(f"```mermaid")
        lines.append("graph TB")
        lines.append(f"    %% {domain_name.upper()} Domain Concept Map")
        
        # Create nodes for all AKUs
        for aku in akus[:10]:  # Limit to 10 for readability
            aku_id = aku.get('@id', 'unknown')
            label = aku.get('skos:prefLabel', aku_id)
            safe_id = aku_id.replace('-', '_').replace(':', '_')
            
            # Determine node type
            classification = aku.get('classification', {})
            aku_type = classification.get('type', 'concept')
            
            if aku_type == 'definition':
                shape = f"{safe_id}[[\"{label}\"]"
                color = "fill:#4CAF50"
            elif aku_type == 'formula':
                shape = f"{safe_id}{{\"{label}\"}}"
                color = "fill:#2196F3"
            elif aku_type == 'example':
                shape = f"{safe_id}(\"{label}\")"
                color = "fill:#FF9800"
            else:
                shape = f"{safe_id}[\"{label}\"]"
                color = "fill:#9C27B0"
            
            lines.append(f"    {shape}")
            lines.append(f"    style {safe_id} {color},stroke:#333,stroke-width:2px")
        
        # Add relationships
        for aku in akus[:10]:
            aku_id = aku.get('@id', 'unknown')
            safe_id = aku_id.replace('-', '_').replace(':', '_')
            
            rels = aku.get('relationships', {})
            
            if 'skos:broader' in rels:
                broader_list = rels['skos:broader']
                if isinstance(broader_list, list):
                    for item in broader_list[:2]:  # Limit connections
                        if isinstance(item, dict) and '@id' in item:
                            target = item['@id'].replace('wsmg:', '').replace('wsmg-econ:', '').replace('-', '_').replace(':', '_')
                            lines.append(f"    {safe_id} --> {target}")
        
        if len(akus) > 10:
            lines.append(f"    more[\"... and {len(akus) - 10} more concepts\"]")
            lines.append("    style more fill:#ddd,stroke:#999,stroke-dasharray: 5 5")
        
        lines.append("```")
        
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Visualize SKOS relationships in AKUs')
    parser.add_argument('path', nargs='?', help='Path to AKU file')
    parser.add_argument('--directory', '-d', help='Visualize all AKUs in directory')
    parser.add_argument('--graph-all', action='store_true', help='Create domain graphs')
    parser.add_argument('--output', '-o', help='Output file for visualization')
    
    args = parser.parse_args()
    
    visualizer = RelationshipVisualizer()
    
    if args.path:
        # Single AKU visualization
        aku_path = Path(args.path)
        aku = visualizer.load_aku(aku_path)
        aku_id = aku.get('@id', aku_path.stem)
        
        visualizer.extract_relationships(aku, aku_id)
        
        # Generate visualizations
        tree_view = visualizer.generate_tree_view(aku_id, aku)
        mermaid_diagram = visualizer.generate_mermaid_diagram(aku_id, aku)
        
        output = f"{tree_view}\n\n{mermaid_diagram}"
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"✅ Visualization saved to {args.output}")
        else:
            print(output)
    
    elif args.directory or args.graph_all:
        # Multiple AKUs or domain graph
        if args.graph_all:
            base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs")
            domains = {
                'NPV/Finance': list(base_dir.glob(".project/pilot/npv-finance/akus/**/*.json")),
                'Medical': list(base_dir.glob("domain/medicine/**/*.json"))
            }
        else:
            dir_path = Path(args.directory)
            domains = {'Custom': list(dir_path.glob("**/*.json"))}
        
        output_lines = []
        
        for domain_name, aku_files in domains.items():
            if not aku_files:
                continue
            
            print(f"\n📊 Processing {domain_name} domain ({len(aku_files)} AKUs)...")
            
            akus = []
            for aku_file in aku_files:
                if 'ENHANCED' in aku_file.name:
                    continue
                try:
                    aku = visualizer.load_aku(aku_file)
                    akus.append(aku)
                    aku_id = aku.get('@id', aku_file.stem)
                    visualizer.extract_relationships(aku, aku_id)
                except Exception as e:
                    print(f"⚠️  Skipping {aku_file.name}: {e}")
            
            # Generate domain graph
            domain_graph = visualizer.generate_domain_graph(domain_name, akus)
            output_lines.append(f"\n## {domain_name} Domain\n")
            output_lines.append(domain_graph)
        
        output = '\n'.join(output_lines)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"\n✅ Visualization saved to {args.output}")
        else:
            print(output)
    
    else:
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
