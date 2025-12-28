#!/usr/bin/env python3
"""
Cross-Domain Relationship Discovery

Automatically discovers potential relationships between concepts across different
domains (medical/economics/science). For example, medical procedures that have
economic implications, or scientific concepts used in medical contexts.

Usage:
    python discover_cross_domain.py --analyze
    python discover_cross_domain.py --suggest path/to/aku.json
    python discover_cross_domain.py --report
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class CrossDomainDiscovery:
    """Discovers relationships across knowledge domains."""
    
    # Known cross-domain patterns
    CROSS_DOMAIN_KEYWORDS = {
        'medical_to_economics': {
            'keywords': ['cost', 'price', 'payment', 'reimbursement', 'insurance', 
                        'budget', 'economic', 'financial', 'value', 'investment'],
            'description': 'Medical concepts with economic implications'
        },
        'medical_to_science': {
            'keywords': ['chemical', 'molecule', 'compound', 'reaction', 'measurement',
                        'physics', 'biology', 'biochemistry', 'pharmacology'],
            'description': 'Medical concepts based on scientific principles'
        },
        'economics_to_medical': {
            'keywords': ['health', 'medical', 'hospital', 'patient', 'treatment',
                        'procedure', 'diagnosis', 'clinical', 'healthcare'],
            'description': 'Economic concepts applied to healthcare'
        },
        'science_to_medical': {
            'keywords': ['diagnostic', 'therapeutic', 'clinical', 'patient', 'disease',
                        'medical', 'health', 'treatment'],
            'description': 'Scientific concepts used in medical practice'
        }
    }
    
    def __init__(self):
        self.akus_by_domain = defaultdict(list)
        self.cross_domain_suggestions = []
    
    def detect_domain(self, aku: Dict) -> str:
        """Detect which domain an AKU belongs to."""
        domain_path = aku.get('classification', {}).get('domain_path', '')
        
        if 'medicine' in domain_path or 'medical' in domain_path:
            return 'medical'
        elif 'economics' in domain_path or 'finance' in domain_path:
            return 'economics'
        elif 'science' in domain_path or 'physics' in domain_path or 'chemistry' in domain_path:
            return 'science'
        
        return 'unknown'
    
    def extract_text_content(self, aku: Dict) -> str:
        """Extract all text content from an AKU for analysis."""
        text_parts = []
        
        # Extract from content
        if 'content' in aku:
            content = aku['content']
            if isinstance(content, dict):
                if 'statement' in content:
                    stmt = content['statement']
                    if isinstance(stmt, dict):
                        text_parts.append(stmt.get('text', ''))
                        text_parts.append(stmt.get('formal', ''))
                    elif isinstance(stmt, str):
                        text_parts.append(stmt)
                
                if 'explanation' in content:
                    exp = content['explanation']
                    if isinstance(exp, dict):
                        for key, value in exp.items():
                            if isinstance(value, str):
                                text_parts.append(value)
                            elif isinstance(value, list):
                                text_parts.extend([str(v) for v in value])
        
        # Extract from definitions glossary
        if 'definitions_glossary' in aku.get('content', {}):
            glossary = aku['content']['definitions_glossary']
            if isinstance(glossary, dict):
                text_parts.extend(glossary.values())
        
        # Extract from labels
        text_parts.append(aku.get('skos:prefLabel', ''))
        text_parts.append(aku.get('skos:definition', ''))
        
        return ' '.join(text_parts).lower()
    
    def find_cross_domain_connections(self, aku: Dict, aku_id: str, domain: str) -> List[Dict]:
        """Find potential cross-domain connections for an AKU."""
        suggestions = []
        text_content = self.extract_text_content(aku)
        
        # Check each cross-domain pattern
        for pattern_key, pattern_info in self.CROSS_DOMAIN_KEYWORDS.items():
            # Only check relevant patterns for this domain
            source_domain, target_domain = pattern_key.split('_to_')
            if source_domain != domain:
                continue
            
            # Count keyword matches
            matches = []
            for keyword in pattern_info['keywords']:
                if keyword in text_content:
                    matches.append(keyword)
            
            if matches:
                suggestions.append({
                    'aku_id': aku_id,
                    'source_domain': source_domain,
                    'target_domain': target_domain,
                    'description': pattern_info['description'],
                    'matched_keywords': matches,
                    'confidence': min(len(matches) / 3, 1.0)  # Confidence based on matches
                })
        
        return suggestions
    
    def analyze_repository(self) -> Dict:
        """Analyze entire repository for cross-domain relationships."""
        base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs")
        aku_files = []
        
        for pattern in ["domain/**/*.json", ".project/pilot/**/*.json"]:
            aku_files.extend(base_dir.glob(pattern))
        
        print(f"🔍 Analyzing {len(aku_files)} AKUs for cross-domain relationships...\n")
        
        # Analyze each AKU
        for aku_file in aku_files:
            try:
                with open(aku_file, 'r') as f:
                    aku = json.load(f)
                
                domain = self.detect_domain(aku)
                aku_id = aku.get('@id', aku_file.stem)
                
                self.akus_by_domain[domain].append({
                    'id': aku_id,
                    'file': str(aku_file),
                    'aku': aku
                })
                
                # Find cross-domain connections
                suggestions = self.find_cross_domain_connections(aku, aku_id, domain)
                self.cross_domain_suggestions.extend(suggestions)
            
            except Exception as e:
                print(f"⚠️  Error analyzing {aku_file.name}: {e}")
        
        return {
            'total_akus': len(aku_files),
            'by_domain': {d: len(akus) for d, akus in self.akus_by_domain.items()},
            'cross_domain_suggestions': len(self.cross_domain_suggestions)
        }
    
    def generate_report(self) -> str:
        """Generate cross-domain discovery report."""
        report = []
        report.append("=" * 80)
        report.append("CROSS-DOMAIN RELATIONSHIP DISCOVERY REPORT")
        report.append("=" * 80)
        
        # Domain distribution
        report.append("\n📊 DOMAIN DISTRIBUTION")
        report.append("-" * 80)
        for domain, akus in sorted(self.akus_by_domain.items()):
            report.append(f"  {domain.capitalize()}: {len(akus)} AKUs")
        
        # Cross-domain suggestions
        report.append("\n\n🔗 CROSS-DOMAIN CONNECTION SUGGESTIONS")
        report.append("-" * 80)
        
        if self.cross_domain_suggestions:
            # Group by target domain
            by_target = defaultdict(list)
            for sugg in self.cross_domain_suggestions:
                by_target[f"{sugg['source_domain']}→{sugg['target_domain']}"].append(sugg)
            
            for connection_type, suggestions in sorted(by_target.items()):
                report.append(f"\n{connection_type.upper()} ({len(suggestions)} potential connections)")
                
                # Show top suggestions by confidence
                top_suggestions = sorted(suggestions, key=lambda x: x['confidence'], reverse=True)[:5]
                for sugg in top_suggestions:
                    report.append(f"\n  AKU: {sugg['aku_id']}")
                    report.append(f"  Confidence: {sugg['confidence']:.0%}")
                    report.append(f"  Matched keywords: {', '.join(sugg['matched_keywords'][:5])}")
                    report.append(f"  Suggestion: {sugg['description']}")
                
                if len(suggestions) > 5:
                    report.append(f"\n  ... and {len(suggestions) - 5} more suggestions")
        else:
            report.append("\nNo cross-domain connections detected.")
            report.append("This may indicate:")
            report.append("  - Domains are currently independent")
            report.append("  - Keyword patterns need refinement")
            report.append("  - More AKUs needed for pattern detection")
        
        # Recommendations
        report.append("\n\n💡 RECOMMENDATIONS")
        report.append("-" * 80)
        report.append("\n1. Review high-confidence suggestions for potential links")
        report.append("2. Add cross-domain relationships where appropriate")
        report.append("3. Consider creating bridge AKUs for strong connections")
        report.append("4. Document domain boundaries and interfaces")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)
    
    def suggest_connections_for_aku(self, aku_path: Path) -> List[Dict]:
        """Suggest cross-domain connections for a specific AKU."""
        try:
            with open(aku_path, 'r') as f:
                aku = json.load(f)
            
            domain = self.detect_domain(aku)
            aku_id = aku.get('@id', aku_path.stem)
            
            suggestions = self.find_cross_domain_connections(aku, aku_id, domain)
            
            return suggestions
        
        except Exception as e:
            print(f"❌ Error: {e}")
            return []


def main():
    parser = argparse.ArgumentParser(description='Discover cross-domain relationships')
    parser.add_argument('--analyze', action='store_true', 
                       help='Analyze entire repository')
    parser.add_argument('--suggest', metavar='PATH',
                       help='Suggest connections for specific AKU')
    parser.add_argument('--report', action='store_true',
                       help='Generate cross-domain report')
    
    args = parser.parse_args()
    
    discovery = CrossDomainDiscovery()
    
    if args.analyze or args.report:
        stats = discovery.analyze_repository()
        print(f"\n✅ Analysis complete")
        print(f"   Total AKUs: {stats['total_akus']}")
        print(f"   Cross-domain suggestions: {stats['cross_domain_suggestions']}")
        
        if args.report:
            report = discovery.generate_report()
            print("\n" + report)
    
    elif args.suggest:
        aku_path = Path(args.suggest)
        suggestions = discovery.suggest_connections_for_aku(aku_path)
        
        if suggestions:
            print(f"\n🔗 Cross-domain suggestions for {aku_path.name}:")
            for sugg in suggestions:
                print(f"\n  → {sugg['source_domain']} to {sugg['target_domain']}")
                print(f"    Confidence: {sugg['confidence']:.0%}")
                print(f"    Keywords: {', '.join(sugg['matched_keywords'][:5])}")
                print(f"    Suggestion: {sugg['description']}")
        else:
            print(f"\nℹ️  No cross-domain connections detected for {aku_path.name}")
    
    else:
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
