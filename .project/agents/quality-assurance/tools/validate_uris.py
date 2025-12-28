#!/usr/bin/env python3
"""
Ontology URI Validator

Validates that external ontology URIs referenced in AKUs are actually accessible
and return valid responses. Checks SNOMED CT, MeSH, FIBO, Wikidata, etc.

Usage:
    python validate_uris.py path/to/aku.json
    python validate_uris.py --directory path/to/akus/
    python validate_uris.py --all
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time

class URIValidator:
    """Validates ontology URIs in AKUs."""
    
    # Known ontology patterns and their expected behaviors
    ONTOLOGY_PATTERNS = {
        'snomed': {
            'pattern': 'http://snomed.info/id/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302, 303]
        },
        'mesh': {
            'pattern': 'http://id.nlm.nih.gov/mesh/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302]
        },
        'icd11': {
            'pattern': 'http://id.who.int/icd/entity/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302]
        },
        'fibo': {
            'pattern': 'https://spec.edmcouncil.org/fibo/ontology/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302]
        },
        'dbpedia': {
            'pattern': 'http://dbpedia.org/resource/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302, 303]
        },
        'wikidata': {
            'pattern': 'http://www.wikidata.org/entity/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302, 303]
        },
        'qudt': {
            'pattern': 'http://qudt.org/vocab/',
            'check_method': 'head',
            'timeout': 10,
            'expected_status': [200, 301, 302]
        }
    }
    
    def __init__(self, verbose: bool = False, cache: bool = True):
        self.verbose = verbose
        self.cache = cache
        self.uri_cache = {}
        self.stats = {
            'checked': 0,
            'valid': 0,
            'invalid': 0,
            'skipped': 0,
            'cached': 0
        }
    
    def validate_uri(self, uri: str) -> Tuple[bool, str]:
        """
        Validate a single URI.
        
        Returns:
            Tuple of (is_valid, message)
        """
        # Check cache
        if self.cache and uri in self.uri_cache:
            self.stats['cached'] += 1
            return self.uri_cache[uri]
        
        # Determine ontology type
        ontology_info = None
        for name, info in self.ONTOLOGY_PATTERNS.items():
            if uri.startswith(info['pattern']):
                ontology_info = info
                break
        
        if not ontology_info:
            result = (True, "Unknown ontology, skipping validation")
            self.stats['skipped'] += 1
            if self.cache:
                self.uri_cache[uri] = result
            return result
        
        # Validate URI
        try:
            req = Request(uri, method='HEAD')
            req.add_header('User-Agent', 'WorldSMEGraphs-URI-Validator/1.0')
            req.add_header('Accept', 'text/html,application/json,application/ld+json')
            
            with urlopen(req, timeout=ontology_info['timeout']) as response:
                status = response.getcode()
                if status in ontology_info['expected_status']:
                    result = (True, f"Valid ({status})")
                    self.stats['valid'] += 1
                else:
                    result = (False, f"Unexpected status {status}")
                    self.stats['invalid'] += 1
        
        except HTTPError as e:
            result = (False, f"HTTP Error {e.code}")
            self.stats['invalid'] += 1
        except URLError as e:
            result = (False, f"URL Error: {e.reason}")
            self.stats['invalid'] += 1
        except Exception as e:
            result = (False, f"Error: {str(e)}")
            self.stats['invalid'] += 1
        
        self.stats['checked'] += 1
        
        if self.cache:
            self.uri_cache[uri] = result
        
        # Rate limiting
        time.sleep(0.1)
        
        return result
    
    def extract_uris_from_aku(self, aku: Dict) -> List[str]:
        """Extract all ontology URIs from an AKU."""
        uris = []
        
        # Check owl:sameAs
        if 'owl:sameAs' in aku:
            uri = aku['owl:sameAs']
            if isinstance(uri, str):
                uris.append(uri)
        
        # Check SKOS match properties
        for match_type in ['skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch', 'skos:narrowMatch']:
            if match_type in aku:
                matches = aku[match_type]
                if isinstance(matches, list):
                    uris.extend([m for m in matches if isinstance(m, str)])
                elif isinstance(matches, str):
                    uris.append(matches)
        
        # Check medicalCode
        if 'medicalCode' in aku:
            for code in aku['medicalCode']:
                if isinstance(code, dict) and 'uri' in code:
                    uris.append(code['uri'])
        
        return uris
    
    def validate_aku(self, aku_path: Path) -> Dict:
        """Validate all URIs in an AKU."""
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
            
            uris = self.extract_uris_from_aku(aku)
            
            if not uris:
                return {
                    'file': aku_path.name,
                    'status': 'no_uris',
                    'uris': []
                }
            
            uri_results = []
            for uri in uris:
                is_valid, message = self.validate_uri(uri)
                uri_results.append({
                    'uri': uri,
                    'valid': is_valid,
                    'message': message
                })
                
                if self.verbose:
                    status = "✅" if is_valid else "❌"
                    print(f"  {status} {uri}: {message}")
            
            all_valid = all(r['valid'] for r in uri_results)
            
            return {
                'file': aku_path.name,
                'status': 'valid' if all_valid else 'invalid',
                'uris': uri_results
            }
        
        except Exception as e:
            return {
                'file': aku_path.name,
                'status': 'error',
                'error': str(e),
                'uris': []
            }
    
    def print_summary(self):
        """Print validation summary."""
        print(f"\n{'='*70}")
        print("URI VALIDATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total URIs checked: {self.stats['checked']}")
        print(f"✅ Valid: {self.stats['valid']}")
        print(f"❌ Invalid: {self.stats['invalid']}")
        print(f"⏭️  Skipped (unknown ontology): {self.stats['skipped']}")
        if self.cache:
            print(f"💾 Cached hits: {self.stats['cached']}")
        
        if self.stats['checked'] > 0:
            success_rate = (self.stats['valid'] / self.stats['checked']) * 100
            print(f"\nSuccess rate: {success_rate:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Validate ontology URIs in AKUs')
    parser.add_argument('path', nargs='?', help='Path to AKU file or directory')
    parser.add_argument('--directory', '-d', help='Validate all AKUs in directory')
    parser.add_argument('--all', action='store_true', help='Validate all AKUs in repository')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--no-cache', action='store_true', help='Disable URI caching')
    
    args = parser.parse_args()
    
    validator = URIValidator(verbose=args.verbose, cache=not args.no_cache)
    
    # Determine files to validate
    aku_files = []
    
    if args.all:
        base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs")
        for pattern in ["domain/**/*.json", ".project/pilot/**/*.json"]:
            aku_files.extend(base_dir.glob(pattern))
    elif args.directory:
        dir_path = Path(args.directory)
        aku_files = list(dir_path.glob("**/*.json"))
    elif args.path:
        path = Path(args.path)
        if path.is_dir():
            aku_files = list(path.glob("**/*.json"))
        else:
            aku_files = [path]
    else:
        parser.print_help()
        return 1
    
    if not aku_files:
        print("No AKU files found")
        return 1
    
    print(f"Validating URIs in {len(aku_files)} AKU(s)...\n")
    
    results = []
    for aku_file in aku_files:
        if args.verbose:
            print(f"\n{aku_file.name}:")
        result = validator.validate_aku(aku_file)
        results.append(result)
        
        if not args.verbose:
            if result['status'] == 'valid':
                print(f"✅ {aku_file.name}")
            elif result['status'] == 'invalid':
                print(f"❌ {aku_file.name}")
            elif result['status'] == 'no_uris':
                print(f"⏭️  {aku_file.name} (no URIs)")
            else:
                print(f"⚠️  {aku_file.name} ({result.get('error', 'unknown error')})")
    
    validator.print_summary()
    
    # Return error code if any invalid
    invalid_count = sum(1 for r in results if r['status'] == 'invalid')
    return 1 if invalid_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
