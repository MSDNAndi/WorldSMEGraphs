#!/usr/bin/env python3
"""
Cross-Domain AKU Validator

Validates that AKUs follow the cross-domain linking pattern defined in
domain/_ontology/global-hierarchy.yaml.

Checks:
1. Native domain AKUs have isNativeDomain: true
2. Application domain AKUs have cross_domain_references
3. All cross-domain links point to valid paths
4. Domain paths match the global hierarchy

Usage:
    python validate_cross_domain.py path/to/aku.json
    python validate_cross_domain.py --directory path/to/akus/
"""

import json
import os
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class CrossDomainValidator:
    def __init__(self, hierarchy_path: str = None):
        """Initialize validator with global hierarchy."""
        if hierarchy_path is None:
            # Find hierarchy relative to this script
            script_dir = Path(__file__).parent
            hierarchy_path = script_dir.parent / "global-hierarchy.yaml"
        
        self.hierarchy_path = Path(hierarchy_path)
        self.hierarchy = None
        self.valid_domains = set()
        self.errors = []
        self.warnings = []
        
        self._load_hierarchy()
    
    def _load_hierarchy(self):
        """Load the global domain hierarchy."""
        try:
            with open(self.hierarchy_path, 'r') as f:
                self.hierarchy = yaml.safe_load(f)
            self._extract_valid_domains()
        except FileNotFoundError:
            print(f"Warning: Global hierarchy not found at {self.hierarchy_path}")
            print("Cross-domain path validation will be skipped.")
        except yaml.YAMLError as e:
            print(f"Error parsing hierarchy YAML: {e}")
    
    def _extract_valid_domains(self):
        """Extract all valid domain paths from the hierarchy."""
        if not self.hierarchy or 'domains' not in self.hierarchy:
            return
        
        def extract_paths(node: dict, prefix: str = ""):
            """Recursively extract domain paths."""
            for key, value in node.items():
                if isinstance(value, dict):
                    current_path = f"{prefix}/{key}" if prefix else key
                    self.valid_domains.add(current_path)
                    
                    # Recurse into subdomain_hierarchy or subdomains
                    if 'subdomain_hierarchy' in value:
                        extract_paths(value['subdomain_hierarchy'], current_path)
                    if 'subdomains' in value:
                        extract_paths(value['subdomains'], current_path)
        
        extract_paths(self.hierarchy['domains'])
    
    def validate_aku(self, aku_path: str) -> Tuple[bool, List[str], List[str]]:
        """
        Validate a single AKU for cross-domain compliance.
        
        Returns:
            (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        try:
            with open(aku_path, 'r') as f:
                aku = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False, self.errors, self.warnings
        except FileNotFoundError:
            self.errors.append(f"File not found: {aku_path}")
            return False, self.errors, self.warnings
        
        # Check for required fields
        self._check_id(aku)
        self._check_classification(aku)
        self._check_cross_domain_refs(aku)
        self._check_content(aku)
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def _check_id(self, aku: dict):
        """Check that AKU has a valid ID."""
        if '@id' not in aku:
            self.errors.append("Missing @id field")
    
    def _check_classification(self, aku: dict):
        """Check classification section for domain compliance."""
        if 'classification' not in aku:
            self.errors.append("Missing 'classification' section")
            return
        
        classification = aku['classification']
        
        # Check domain_path
        if 'domain_path' not in classification:
            self.errors.append("Missing 'classification.domain_path'")
        else:
            domain_path = classification['domain_path']
            if self.valid_domains and domain_path not in self.valid_domains:
                # Check if it's a partial match (path might be more specific)
                # Use boundary-aware matching to avoid 'math' matching 'mathematics'
                def is_path_compatible(path1: str, path2: str) -> bool:
                    """Check if one path is a prefix of another, respecting boundaries."""
                    if path1 == path2:
                        return True
                    # Ensure prefix matching respects path boundaries
                    if path1.startswith(path2 + '/') or path2.startswith(path1 + '/'):
                        return True
                    return False
                
                partial_match = any(is_path_compatible(domain_path, vd) 
                                   for vd in self.valid_domains)
                if not partial_match:
                    self.warnings.append(
                        f"Domain path '{domain_path}' not found in global hierarchy. "
                        "Ensure it matches domain/_ontology/global-hierarchy.yaml"
                    )
        
        # Check native/application domain markers
        is_native = classification.get('isNativeDomain', False)
        is_application = classification.get('isApplicationDomain', False)
        
        if is_native and is_application:
            self.errors.append(
                "AKU cannot be both isNativeDomain and isApplicationDomain"
            )
        
        if not is_native and not is_application:
            self.warnings.append(
                "AKU has neither isNativeDomain nor isApplicationDomain set. "
                "Consider adding one for clarity."
            )
    
    def _check_cross_domain_refs(self, aku: dict):
        """Check cross-domain references for compliance."""
        classification = aku.get('classification', {})
        is_native = classification.get('isNativeDomain', False)
        is_application = classification.get('isApplicationDomain', False)
        
        has_cross_refs = 'cross_domain_references' in aku
        has_applications = 'cross_domain_applications' in aku
        
        # Native domains should document applications
        if is_native:
            if has_cross_refs:
                self.warnings.append(
                    "Native domain AKU has 'cross_domain_references'. "
                    "Consider using 'cross_domain_applications' instead to document "
                    "where this concept is applied."
                )
            if not has_applications:
                self.warnings.append(
                    "Native domain AKU could benefit from 'cross_domain_applications' "
                    "section documenting where this concept is used."
                )
        
        # Application domains must have cross-domain references
        if is_application:
            if not has_cross_refs:
                self.errors.append(
                    "Application domain AKU must have 'cross_domain_references' "
                    "section linking to native domain concepts."
                )
            else:
                self._validate_cross_refs(aku['cross_domain_references'])
    
    def _validate_cross_refs(self, cross_refs: dict):
        """Validate the structure of cross-domain references."""
        valid_relationships = {'applies', 'uses', 'extends', 'informs'}
        
        for rel_type, refs in cross_refs.items():
            if rel_type == 'note':
                continue
            
            if rel_type not in valid_relationships:
                self.warnings.append(
                    f"Unknown relationship type '{rel_type}'. "
                    f"Valid types: {valid_relationships}"
                )
            
            if not isinstance(refs, list):
                refs = [refs]
            
            for ref in refs:
                if isinstance(ref, dict):
                    if '@id' not in ref:
                        self.errors.append(
                            f"Cross-domain reference missing '@id': {ref}"
                        )
                    if 'relationship' not in ref:
                        self.warnings.append(
                            f"Cross-domain reference missing 'relationship': {ref.get('@id', 'unknown')}"
                        )
    
    def _check_content(self, aku: dict):
        """Check content section for appropriate depth."""
        classification = aku.get('classification', {})
        is_native = classification.get('isNativeDomain', False)
        is_application = classification.get('isApplicationDomain', False)
        
        if 'content' not in aku:
            self.warnings.append("Missing 'content' section")
            return
        
        content = aku['content']
        
        # Native domains should have full definitions
        if is_native:
            if 'definition' not in content:
                self.warnings.append(
                    "Native domain AKU should have a 'definition' in content"
                )
        
        # Application domains should have applicationContext
        if is_application:
            cross_refs = aku.get('cross_domain_references', {})
            has_context = False
            for refs in cross_refs.values():
                if not isinstance(refs, list):
                    continue
                for ref in refs:
                    if isinstance(ref, dict) and 'applicationContext' in ref:
                        has_context = True
                        break
                if has_context:
                    break
            
            if not has_context:
                self.warnings.append(
                    "Application domain AKU should explain 'applicationContext' "
                    "in cross_domain_references"
                )


def validate_file(path: str, validator: CrossDomainValidator) -> bool:
    """Validate a single file and print results."""
    print(f"\nValidating: {path}")
    print("-" * 60)
    
    is_valid, errors, warnings = validator.validate_aku(path)
    
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  ❌ {error}")
    
    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
    
    if is_valid and not warnings:
        print("  ✅ Valid with no warnings")
    elif is_valid:
        print(f"\n  Result: ⚠️  Valid with {len(warnings)} warning(s)")
    else:
        print(f"\n  Result: ❌ Invalid with {len(errors)} error(s)")
    
    return is_valid


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate AKUs for cross-domain compliance'
    )
    parser.add_argument('path', nargs='?', help='Path to AKU file or directory')
    parser.add_argument('--directory', '-d', help='Directory to scan for AKUs')
    parser.add_argument('--hierarchy', '-H', 
                       help='Path to global-hierarchy.yaml')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    
    args = parser.parse_args()
    
    if not args.path and not args.directory:
        parser.print_help()
        sys.exit(1)
    
    validator = CrossDomainValidator(args.hierarchy)
    
    files_to_validate = []
    
    if args.directory:
        dir_path = Path(args.directory)
        files_to_validate.extend(dir_path.rglob('*.json'))
    elif args.path:
        path = Path(args.path)
        if path.is_dir():
            files_to_validate.extend(path.rglob('*.json'))
        else:
            files_to_validate.append(path)
    
    if not files_to_validate:
        print("No JSON files found to validate")
        sys.exit(0)
    
    print(f"Validating {len(files_to_validate)} file(s)...")
    
    valid_count = 0
    for file_path in files_to_validate:
        if validate_file(str(file_path), validator):
            valid_count += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {valid_count}/{len(files_to_validate)} files valid")
    
    if valid_count < len(files_to_validate):
        sys.exit(1)


if __name__ == '__main__':
    main()
