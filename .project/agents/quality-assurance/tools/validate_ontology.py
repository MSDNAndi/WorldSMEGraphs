#!/usr/bin/env python3
"""
Ontology Compliance Validator for WorldSMEGraphs AKUs

Validates that AKUs comply with ontology integration requirements:
- Valid JSON-LD context
- SKOS relationship consistency
- External ontology URI resolution
- Domain-specific ontology compliance

Usage:
    python validate_ontology.py path/to/aku.json
    python validate_ontology.py --directory path/to/akus/
    python validate_ontology.py --domain economics
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from urllib.parse import urlparse
import re


class OntologyValidator:
    """Validates AKU ontology compliance."""
    
    # Standard ontology prefixes and namespaces
    STANDARD_NAMESPACES = {
        "schema": "https://schema.org/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "dc": "http://purl.org/dc/terms/",
        "prov": "http://www.w3.org/ns/prov#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "snomed": "http://snomed.info/id/",
        "mesh": "http://id.nlm.nih.gov/mesh/",
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/",
        "wsmg": "https://worldsmegraphs.org/vocab/",
    }
    
    # Required SKOS properties
    SKOS_LABEL_PROPERTIES = ["skos:prefLabel", "prefLabel"]
    SKOS_HIERARCHICAL = ["skos:broader", "skos:narrower", "broader", "narrower"]
    SKOS_ASSOCIATIVE = ["skos:related", "related"]
    SKOS_MAPPING = ["skos:exactMatch", "skos:closeMatch", "skos:relatedMatch",
                     "exactMatch", "closeMatch", "relatedMatch"]
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
    
    def validate_aku(self, aku_path: Path) -> bool:
        """
        Validate a single AKU file for ontology compliance.
        
        Args:
            aku_path: Path to AKU JSON file
            
        Returns:
            True if valid, False otherwise
        """
        self.errors = []
        self.warnings = []
        self.info = []
        
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading file: {e}")
            return False
        
        # Run validation checks
        self._validate_context(aku)
        self._validate_id(aku)
        self._validate_type(aku)
        self._validate_skos_labels(aku)
        self._validate_skos_relationships(aku)
        self._validate_external_mappings(aku)
        self._validate_domain_specific(aku)
        
        # Report results
        if self.verbose or self.errors or self.warnings:
            self._print_report(aku_path)
        
        return len(self.errors) == 0
    
    def _validate_context(self, aku: Dict) -> None:
        """Validate @context is present and properly formatted."""
        if "@context" not in aku:
            self.errors.append("Missing @context property")
            return
        
        context = aku["@context"]
        
        # Can be string or array
        if isinstance(context, str):
            self.info.append(f"Single context: {context}")
        elif isinstance(context, list):
            self.info.append(f"Multiple contexts: {len(context)} items")
            
            # Check for base context
            base_found = False
            for ctx in context:
                if isinstance(ctx, str) and "base.jsonld" in ctx:
                    base_found = True
                    break
            
            if not base_found:
                self.warnings.append("Base context not explicitly included")
        else:
            self.errors.append(f"Invalid @context type: {type(context)}")
    
    def _validate_id(self, aku: Dict) -> None:
        """Validate @id is present and follows naming convention."""
        if "@id" not in aku:
            self.warnings.append("Missing @id property")
            return
        
        aku_id = aku["@id"]
        
        # Check format: should be wsmg:domain:concept or wsmg-domain:concept
        if not re.match(r'^wsmg(-\w+)?:[\w-]+', aku_id):
            self.warnings.append(f"@id doesn't follow recommended pattern: {aku_id}")
        
        self.info.append(f"@id: {aku_id}")
    
    def _validate_type(self, aku: Dict) -> None:
        """Validate @type is present and includes schema.org or SKOS types."""
        if "@type" not in aku:
            self.warnings.append("Missing @type property")
            return
        
        aku_type = aku["@type"]
        types = [aku_type] if isinstance(aku_type, str) else aku_type
        
        # Check for schema.org or SKOS types
        has_schema = any("schema:" in t or "EducationalResource" in t for t in types)
        has_skos = any("skos:" in t or "Concept" in t for t in types)
        
        if not (has_schema or has_skos):
            self.warnings.append("No Schema.org or SKOS type found")
        
        self.info.append(f"@type: {types}")
    
    def _validate_skos_labels(self, aku: Dict) -> None:
        """Validate SKOS labeling properties."""
        # Check for prefLabel
        has_pref_label = False
        for prop in self.SKOS_LABEL_PROPERTIES:
            if prop in aku:
                has_pref_label = True
                self.info.append(f"Has preferred label: {prop}")
                break
        
        if not has_pref_label:
            self.warnings.append("Missing skos:prefLabel or prefLabel")
        
        # Check for definition
        if "skos:definition" in aku or "definition" in aku:
            self.info.append("Has SKOS definition")
        elif "content" in aku and "statement" in aku["content"]:
            self.info.append("Has content.statement (legacy format)")
        else:
            self.warnings.append("Missing concept definition")
    
    def _validate_skos_relationships(self, aku: Dict) -> None:
        """Validate SKOS relationship consistency."""
        if "relationships" not in aku:
            self.warnings.append("No relationships defined")
            return
        
        relationships = aku["relationships"]
        
        # Check for hierarchical relationships
        if "hierarchical" in relationships:
            hier = relationships["hierarchical"]
            broader = set(hier.get("skos:broader", []) + hier.get("broader", []))
            narrower = set(hier.get("skos:narrower", []) + hier.get("narrower", []))
            
            # Check for conflicts
            overlap = broader & narrower
            if overlap:
                self.errors.append(f"Concept is both broader and narrower: {overlap}")
            
            self.info.append(f"Broader concepts: {len(broader)}")
            self.info.append(f"Narrower concepts: {len(narrower)}")
        
        # Check for associative relationships
        if "associative" in relationships:
            assoc = relationships["associative"]
            related = assoc.get("skos:related", []) + assoc.get("related", [])
            self.info.append(f"Related concepts: {len(related)}")
        
        # Check for external mappings
        if "external" in relationships:
            ext = relationships["external"]
            exact = ext.get("skos:exactMatch", []) + ext.get("exactMatch", [])
            close = ext.get("skos:closeMatch", []) + ext.get("closeMatch", [])
            
            if isinstance(exact, str):
                exact = [exact]
            if isinstance(close, str):
                close = [close]
            
            self.info.append(f"Exact matches: {len(exact)}")
            self.info.append(f"Close matches: {len(close)}")
    
    def _validate_external_mappings(self, aku: Dict) -> None:
        """Validate external ontology mappings."""
        external_uris = self._extract_external_uris(aku)
        
        if not external_uris:
            self.info.append("No external ontology mappings")
            return
        
        self.info.append(f"Total external URIs: {len(external_uris)}")
        
        # Categorize by ontology
        ontology_counts = {}
        for uri in external_uris:
            for prefix, namespace in self.STANDARD_NAMESPACES.items():
                if namespace in uri or f"{prefix}:" in uri:
                    ontology_counts[prefix] = ontology_counts.get(prefix, 0) + 1
                    break
        
        if ontology_counts:
            self.info.append(f"Ontology usage: {ontology_counts}")
    
    def _extract_external_uris(self, aku: Dict) -> List[str]:
        """Extract all external ontology URIs from AKU."""
        uris = []
        
        def extract_recursive(obj, depth=0):
            if depth > 10:  # Prevent infinite recursion
                return
            
            if isinstance(obj, dict):
                for key, value in obj.items():
                    # Check for URI-like keys
                    if any(ont in key for ont in ["Match", "sameAs", "equivalentClass"]):
                        if isinstance(value, str) and self._is_uri(value):
                            uris.append(value)
                        elif isinstance(value, list):
                            uris.extend([v for v in value if isinstance(v, str) and self._is_uri(v)])
                    else:
                        extract_recursive(value, depth + 1)
            elif isinstance(obj, list):
                for item in obj:
                    extract_recursive(item, depth + 1)
        
        extract_recursive(aku)
        return uris
    
    def _is_uri(self, value: str) -> bool:
        """Check if string looks like a URI."""
        if not value:
            return False
        
        # Check for common URI patterns
        return (
            value.startswith("http://") or
            value.startswith("https://") or
            ":" in value and not value.startswith("{")  # Prefix notation
        )
    
    def _validate_domain_specific(self, aku: Dict) -> None:
        """Validate domain-specific ontology requirements."""
        if "classification" not in aku or "domain_path" not in aku["classification"]:
            self.warnings.append("Missing domain_path classification")
            return
        
        domain_path = aku["classification"]["domain_path"]
        domain = domain_path.split("/")[0] if "/" in domain_path else domain_path
        
        self.info.append(f"Domain: {domain}")
        
        # Domain-specific validations
        if domain == "medicine":
            self._validate_medical_ontology(aku)
        elif domain == "economics":
            self._validate_economics_ontology(aku)
        elif domain == "science":
            self._validate_science_ontology(aku)
    
    def _validate_medical_ontology(self, aku: Dict) -> None:
        """Validate medical domain ontology compliance."""
        # Check for SNOMED CT or MeSH references
        has_snomed = "snomed:" in json.dumps(aku)
        has_mesh = "mesh:" in json.dumps(aku)
        
        if not (has_snomed or has_mesh):
            self.warnings.append("Medical AKU should reference SNOMED CT or MeSH")
        else:
            if has_snomed:
                self.info.append("Has SNOMED CT reference")
            if has_mesh:
                self.info.append("Has MeSH reference")
    
    def _validate_economics_ontology(self, aku: Dict) -> None:
        """Validate economics domain ontology compliance."""
        # Check for FIBO references
        has_fibo = "fibo:" in json.dumps(aku)
        
        if not has_fibo:
            self.warnings.append("Economics AKU should reference FIBO when applicable")
        else:
            self.info.append("Has FIBO reference")
    
    def _validate_science_ontology(self, aku: Dict) -> None:
        """Validate science domain ontology compliance."""
        # Check for QUDT units
        has_qudt = "qudt:" in json.dumps(aku)
        
        if has_qudt:
            self.info.append("Has QUDT units/quantities")
    
    def _print_report(self, aku_path: Path) -> None:
        """Print validation report."""
        print(f"\n{'='*70}")
        print(f"Ontology Validation: {aku_path.name}")
        print(f"{'='*70}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if self.verbose and self.info:
            print(f"\nℹ️  INFO ({len(self.info)}):")
            for info in self.info:
                print(f"  - {info}")
        
        if not self.errors and not self.warnings:
            print("\n✅ VALID - No issues found")
        elif not self.errors:
            print("\n✅ VALID - Warnings only")
        else:
            print("\n❌ INVALID - Please fix errors")


def main():
    parser = argparse.ArgumentParser(
        description="Validate AKU ontology compliance"
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to AKU file or directory"
    )
    parser.add_argument(
        "--directory",
        "-d",
        help="Validate all AKUs in directory"
    )
    parser.add_argument(
        "--domain",
        help="Validate all AKUs in domain (e.g., medicine, economics)"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    validator = OntologyValidator(verbose=args.verbose)
    
    # Determine what to validate
    aku_files = []
    
    if args.domain:
        # Find all AKUs in domain
        domain_path = Path(f"domain/{args.domain}")
        if domain_path.exists():
            aku_files = list(domain_path.rglob("*.json"))
        else:
            print(f"❌ Domain not found: {args.domain}")
            return 1
    elif args.directory:
        # Validate directory
        dir_path = Path(args.directory)
        if dir_path.exists():
            aku_files = list(dir_path.rglob("*.json"))
        else:
            print(f"❌ Directory not found: {args.directory}")
            return 1
    elif args.path:
        # Validate single file or directory
        path = Path(args.path)
        if path.is_file():
            aku_files = [path]
        elif path.is_dir():
            aku_files = list(path.rglob("*.json"))
        else:
            print(f"❌ Path not found: {args.path}")
            return 1
    else:
        parser.print_help()
        return 1
    
    if not aku_files:
        print("❌ No AKU files found")
        return 1
    
    # Validate all files
    print(f"\nValidating {len(aku_files)} AKU(s)...\n")
    
    valid_count = 0
    invalid_count = 0
    
    for aku_file in aku_files:
        if validator.validate_aku(aku_file):
            valid_count += 1
        else:
            invalid_count += 1
    
    # Summary
    print(f"\n{'='*70}")
    print("VALIDATION SUMMARY")
    print(f"{'='*70}")
    print(f"Total AKUs: {len(aku_files)}")
    print(f"✅ Valid: {valid_count}")
    print(f"❌ Invalid: {invalid_count}")
    print(f"Success rate: {valid_count/len(aku_files)*100:.1f}%")
    
    return 0 if invalid_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
