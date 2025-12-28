#!/usr/bin/env python3
"""
Ontology Version Tracker

Tracks which versions of ontologies are used in AKUs and helps detect
when ontology codes might be deprecated due to version updates.

Usage:
    python track_ontology_versions.py --add snomed 2024-09-01
    python track_ontology_versions.py --check path/to/aku.json
    python track_ontology_versions.py --report
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

VERSION_TRACKING_FILE = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/ontology-versions.json")

class OntologyVersionTracker:
    """Tracks ontology versions used in the knowledge base."""
    
    KNOWN_ONTOLOGIES = {
        'snomed': {
            'name': 'SNOMED CT International Edition',
            'update_frequency': 'Biannual (March, September)',
            'url': 'https://www.snomed.org/snomed-ct/releases',
            'deprecation_risk': 'Medium - codes can be made inactive'
        },
        'mesh': {
            'name': 'Medical Subject Headings (MeSH)',
            'update_frequency': 'Annual (December)',
            'url': 'https://www.nlm.nih.gov/mesh/introduction.html',
            'deprecation_risk': 'Low - descriptors rarely deprecated'
        },
        'icd11': {
            'name': 'International Classification of Diseases 11th Revision',
            'update_frequency': 'Annual updates',
            'url': 'https://icd.who.int/',
            'deprecation_risk': 'Low - WHO maintains backward compatibility'
        },
        'fibo': {
            'name': 'Financial Industry Business Ontology',
            'update_frequency': 'Quarterly releases',
            'url': 'https://spec.edmcouncil.org/fibo/',
            'deprecation_risk': 'Low - stable OMG standard'
        },
        'wikidata': {
            'name': 'Wikidata',
            'update_frequency': 'Continuous',
            'url': 'https://www.wikidata.org/',
            'deprecation_risk': 'Very Low - entity IDs are permanent'
        },
        'dbpedia': {
            'name': 'DBpedia',
            'update_frequency': 'Periodic (follows Wikipedia)',
            'url': 'https://www.dbpedia.org/',
            'deprecation_risk': 'Low - resources maintained'
        },
        'qudt': {
            'name': 'Quantities, Units, Dimensions and Types',
            'update_frequency': 'Periodic',
            'url': 'http://www.qudt.org/',
            'deprecation_risk': 'Low - stable standard'
        },
        'chebi': {
            'name': 'Chemical Entities of Biological Interest',
            'update_frequency': 'Monthly',
            'url': 'https://www.ebi.ac.uk/chebi/',
            'deprecation_risk': 'Low - EBI maintained'
        },
        'go': {
            'name': 'Gene Ontology',
            'update_frequency': 'Continuous',
            'url': 'http://geneontology.org/',
            'deprecation_risk': 'Low - terms marked obsolete but retained'
        }
    }
    
    def __init__(self):
        self.versions = self.load_versions()
    
    def load_versions(self) -> Dict:
        """Load version tracking data."""
        if VERSION_TRACKING_FILE.exists():
            with open(VERSION_TRACKING_FILE, 'r') as f:
                return json.load(f)
        else:
            return {
                'last_updated': datetime.utcnow().isoformat() + 'Z',
                'ontologies': {},
                'aku_metadata': {}
            }
    
    def save_versions(self):
        """Save version tracking data."""
        self.versions['last_updated'] = datetime.utcnow().isoformat() + 'Z'
        
        VERSION_TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(VERSION_TRACKING_FILE, 'w') as f:
            json.dump(self.versions, f, indent=2)
        
        print(f"✅ Version tracking saved to {VERSION_TRACKING_FILE}")
    
    def add_ontology_version(self, ontology: str, version: str, release_date: Optional[str] = None):
        """Add or update an ontology version."""
        if ontology not in self.KNOWN_ONTOLOGIES:
            print(f"⚠️  Warning: {ontology} is not a known ontology")
        
        if 'ontologies' not in self.versions:
            self.versions['ontologies'] = {}
        
        self.versions['ontologies'][ontology] = {
            'version': version,
            'release_date': release_date or datetime.utcnow().isoformat() + 'Z',
            'recorded_date': datetime.utcnow().isoformat() + 'Z',
            'name': self.KNOWN_ONTOLOGIES.get(ontology, {}).get('name', ontology)
        }
        
        self.save_versions()
        print(f"✅ Added {ontology} version {version}")
    
    def check_aku_ontology_usage(self, aku_path: Path) -> Dict:
        """Check which ontologies an AKU uses and record metadata."""
        try:
            with open(aku_path, 'r') as f:
                aku = json.load(f)
            
            ontologies_used = set()
            codes_found = []
            
            # Extract ontology usage
            for field in ['owl:sameAs', 'skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch']:
                if field in aku:
                    uris = aku[field] if isinstance(aku[field], list) else [aku[field]]
                    for uri in uris:
                        if isinstance(uri, str):
                            for ont_key, ont_info in self.KNOWN_ONTOLOGIES.items():
                                if ont_info.get('url', '') in uri or ont_key in uri.lower():
                                    ontologies_used.add(ont_key)
                                    codes_found.append({
                                        'ontology': ont_key,
                                        'uri': uri,
                                        'field': field
                                    })
            
            # Check medicalCode
            if 'medicalCode' in aku:
                for code in aku['medicalCode']:
                    if isinstance(code, dict):
                        system = code.get('codingSystem', '').lower()
                        if 'snomed' in system:
                            ontologies_used.add('snomed')
                            codes_found.append({
                                'ontology': 'snomed',
                                'code': code.get('codeValue'),
                                'field': 'medicalCode'
                            })
                        elif 'mesh' in system:
                            ontologies_used.add('mesh')
                            codes_found.append({
                                'ontology': 'mesh',
                                'code': code.get('codeValue'),
                                'field': 'medicalCode'
                            })
            
            # Record AKU metadata
            aku_id = aku.get('@id', aku_path.stem)
            timestamp = aku.get('metadata', {}).get('last_updated', datetime.utcnow().isoformat() + 'Z')
            
            if 'aku_metadata' not in self.versions:
                self.versions['aku_metadata'] = {}
            
            self.versions['aku_metadata'][aku_id] = {
                'file': str(aku_path),
                'last_updated': timestamp,
                'ontologies_used': list(ontologies_used),
                'code_count': len(codes_found),
                'checked_date': datetime.utcnow().isoformat() + 'Z'
            }
            
            return {
                'status': 'success',
                'ontologies_used': list(ontologies_used),
                'codes_found': codes_found
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def generate_report(self) -> str:
        """Generate a version tracking report."""
        report = []
        report.append("=" * 80)
        report.append("ONTOLOGY VERSION TRACKING REPORT")
        report.append("=" * 80)
        report.append(f"\nLast Updated: {self.versions.get('last_updated', 'Never')}\n")
        
        # Ontology versions
        report.append("\n📚 ONTOLOGY VERSIONS")
        report.append("-" * 80)
        
        if self.versions.get('ontologies'):
            for ont_key, ont_data in self.versions['ontologies'].items():
                ont_info = self.KNOWN_ONTOLOGIES.get(ont_key, {})
                report.append(f"\n{ont_data.get('name', ont_key)}:")
                report.append(f"  Version: {ont_data.get('version', 'Unknown')}")
                report.append(f"  Release Date: {ont_data.get('release_date', 'Unknown')}")
                report.append(f"  Recorded: {ont_data.get('recorded_date', 'Unknown')}")
                if ont_info:
                    report.append(f"  Update Frequency: {ont_info.get('update_frequency', 'Unknown')}")
                    report.append(f"  Deprecation Risk: {ont_info.get('deprecation_risk', 'Unknown')}")
        else:
            report.append("\n⚠️  No ontology versions recorded yet.")
            report.append("   Use: python track_ontology_versions.py --add <ontology> <version>")
        
        # AKU usage statistics
        report.append("\n\n📊 AKU ONTOLOGY USAGE")
        report.append("-" * 80)
        
        if self.versions.get('aku_metadata'):
            total_akus = len(self.versions['aku_metadata'])
            report.append(f"\nTotal AKUs tracked: {total_akus}")
            
            # Count by ontology
            ont_usage = {}
            for aku_data in self.versions['aku_metadata'].values():
                for ont in aku_data.get('ontologies_used', []):
                    ont_usage[ont] = ont_usage.get(ont, 0) + 1
            
            report.append("\nOntology usage:")
            for ont, count in sorted(ont_usage.items(), key=lambda x: x[1], reverse=True):
                ont_name = self.KNOWN_ONTOLOGIES.get(ont, {}).get('name', ont)
                percentage = (count / total_akus) * 100
                report.append(f"  {ont_name}: {count} AKUs ({percentage:.1f}%)")
        else:
            report.append("\n⚠️  No AKU metadata recorded yet.")
        
        # Recommendations
        report.append("\n\n💡 RECOMMENDATIONS")
        report.append("-" * 80)
        
        if not self.versions.get('ontologies'):
            report.append("\n1. Record current ontology versions you're using")
            report.append("2. Check ontology release notes for breaking changes")
            report.append("3. Set reminders for ontology update cycles")
        else:
            report.append("\n1. Regularly check for ontology updates")
            report.append("2. Review deprecation notices from ontology maintainers")
            report.append("3. Test URI validity after major version updates")
            report.append("4. Document any code migrations in AKU provenance")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)
    
    def list_known_ontologies(self):
        """List all known ontologies with details."""
        print("\n📚 KNOWN ONTOLOGIES")
        print("=" * 80)
        
        for ont_key, ont_info in self.KNOWN_ONTOLOGIES.items():
            print(f"\n{ont_key.upper()}: {ont_info['name']}")
            print(f"  Update Frequency: {ont_info['update_frequency']}")
            print(f"  Deprecation Risk: {ont_info['deprecation_risk']}")
            print(f"  URL: {ont_info['url']}")


def main():
    parser = argparse.ArgumentParser(description='Track ontology versions used in knowledge base')
    parser.add_argument('--add', nargs=2, metavar=('ONTOLOGY', 'VERSION'),
                       help='Add ontology version (e.g., --add snomed 2024-09-01)')
    parser.add_argument('--check', metavar='PATH',
                       help='Check which ontologies an AKU uses')
    parser.add_argument('--check-all', action='store_true',
                       help='Check all AKUs and record metadata')
    parser.add_argument('--report', action='store_true',
                       help='Generate version tracking report')
    parser.add_argument('--list', action='store_true',
                       help='List known ontologies')
    
    args = parser.parse_args()
    
    tracker = OntologyVersionTracker()
    
    if args.add:
        ontology, version = args.add
        tracker.add_ontology_version(ontology, version)
    
    elif args.check:
        aku_path = Path(args.check)
        result = tracker.check_aku_ontology_usage(aku_path)
        if result['status'] == 'success':
            print(f"\n✅ {aku_path.name}")
            print(f"Ontologies used: {', '.join(result['ontologies_used']) or 'None'}")
            print(f"Codes found: {len(result['codes_found'])}")
            tracker.save_versions()
        else:
            print(f"\n❌ Error checking {aku_path.name}: {result.get('error')}")
    
    elif args.check_all:
        base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs")
        aku_files = []
        for pattern in ["domain/**/*.json", ".project/pilot/**/*.json"]:
            aku_files.extend(base_dir.glob(pattern))
        
        print(f"Checking {len(aku_files)} AKUs...")
        for aku_file in aku_files:
            tracker.check_aku_ontology_usage(aku_file)
        
        tracker.save_versions()
        print(f"\n✅ Checked {len(aku_files)} AKUs")
    
    elif args.report:
        report = tracker.generate_report()
        print(report)
    
    elif args.list:
        tracker.list_known_ontologies()
    
    else:
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
