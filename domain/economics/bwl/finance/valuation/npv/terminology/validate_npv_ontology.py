#!/usr/bin/env python3
"""
NPV Ontology Identifier Validator

Validates semantic_links sections in AKUs against the NPV ontology reference.
Checks URI formats, match types, multilingual labels, and SKOS compliance.

Usage:
    python3 validate_npv_ontology.py path/to/aku.json
    python3 validate_npv_ontology.py --directory path/to/akus/
    python3 validate_npv_ontology.py --help

Requirements: Python 3.6+ (standard library only)
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Reference ontology identifiers for NPV domain
REFERENCE_ONTOLOGY = {
    "net_present_value": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
        "wikidata": "http://www.wikidata.org/entity/Q1054308",
        "dbpedia": "http://dbpedia.org/resource/Net_present_value"
    },
    "present_value": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PresentValue",
        "wikidata": "http://www.wikidata.org/entity/Q332099",
        "dbpedia": "http://dbpedia.org/resource/Present_value"
    },
    "discount_rate": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate",
        "wikidata": "http://www.wikidata.org/entity/Q1226339",
        "dbpedia": "http://dbpedia.org/resource/Discount_rate"
    },
    "cash_flow": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow",
        "wikidata": "http://www.wikidata.org/entity/Q223557",
        "dbpedia": "http://dbpedia.org/resource/Cash_flow"
    },
    "discount_factor": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountFactor",
        "wikidata": "http://www.wikidata.org/entity/Q5281138",
        "dbpedia": "http://dbpedia.org/resource/Discounting"
    },
    "time_value_of_money": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/TimeValueOfMoney",
        "wikidata": "http://www.wikidata.org/entity/Q1200790",
        "dbpedia": "http://dbpedia.org/resource/Time_value_of_money"
    },
    "capital_budgeting": {
        "fibo": "https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CapitalBudgeting",
        "wikidata": "http://www.wikidata.org/entity/Q1034992",
        "dbpedia": "http://dbpedia.org/resource/Capital_budgeting"
    }
}

# Required languages
REQUIRED_LANGUAGES = ["en", "de", "es", "fr"]
OPTIONAL_LANGUAGES = ["it", "pt", "zh", "ja", "ru", "ar"]

# Valid match types
VALID_MATCH_TYPES = ["exact_matches", "close_matches", "broad_matches", "related_matches"]

class OntologyValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_aku(self, aku_path: Path) -> Tuple[bool, List[str], List[str], List[str]]:
        """Validate an AKU file for ontology compliance."""
        self.errors = []
        self.warnings = []
        self.info = []
        
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False, self.errors, self.warnings, self.info
        except Exception as e:
            self.errors.append(f"Error reading file: {e}")
            return False, self.errors, self.warnings, self.info
            
        # Check if semantic_links exists
        if "semantic_links" not in aku:
            self.warnings.append("No semantic_links section found")
            return True, self.errors, self.warnings, self.info
            
        semantic_links = aku["semantic_links"]
        
        # Validate structure
        self._validate_structure(semantic_links)
        
        # Validate URIs
        self._validate_uris(semantic_links)
        
        # Validate match types
        self._validate_match_types(semantic_links)
        
        # Validate SKOS elements
        self._validate_skos(semantic_links)
        
        # Validate multilingual labels
        self._validate_multilingual(semantic_links)
        
        # Check against reference ontology
        self._check_reference_alignment(semantic_links)
        
        success = len(self.errors) == 0
        return success, self.errors, self.warnings, self.info
        
    def _validate_structure(self, semantic_links: Dict):
        """Validate basic structure of semantic_links."""
        recommended_fields = ["exact_matches", "skos_concept", "skos_preferred_label"]
        
        for field in recommended_fields:
            if field not in semantic_links:
                self.warnings.append(f"Missing recommended field: {field}")
                
    def _validate_uris(self, semantic_links: Dict):
        """Validate URI formats."""
        fibo_pattern = r"^https://spec\.edmcouncil\.org/fibo/ontology/[A-Z]+/.+"
        wikidata_pattern = r"^http://www\.wikidata\.org/entity/Q\d+$"
        dbpedia_pattern = r"^http://dbpedia\.org/resource/.+$"
        
        for match_type in VALID_MATCH_TYPES:
            if match_type in semantic_links:
                for uri in semantic_links[match_type]:
                    if "fibo" in uri:
                        if not re.match(fibo_pattern, uri):
                            self.errors.append(f"Invalid FIBO URI format: {uri}")
                    elif "wikidata" in uri:
                        if not re.match(wikidata_pattern, uri):
                            self.errors.append(f"Invalid Wikidata URI format: {uri}")
                    elif "dbpedia" in uri:
                        if not re.match(dbpedia_pattern, uri):
                            self.errors.append(f"Invalid DBpedia URI format: {uri}")
                        # Check for common mistakes
                        if "-" in uri.split("/")[-1]:
                            self.warnings.append(f"DBpedia URI contains hyphen (should be underscore): {uri}")
                            
    def _validate_match_types(self, semantic_links: Dict):
        """Validate match type arrays."""
        for match_type in VALID_MATCH_TYPES:
            if match_type in semantic_links:
                matches = semantic_links[match_type]
                if not isinstance(matches, list):
                    self.errors.append(f"{match_type} must be an array")
                elif len(matches) == 0:
                    self.warnings.append(f"{match_type} is empty (consider removing)")
                    
    def _validate_skos(self, semantic_links: Dict):
        """Validate SKOS elements."""
        # Check skos_concept
        if "skos_concept" in semantic_links:
            concept = semantic_links["skos_concept"]
            if not isinstance(concept, str):
                self.errors.append("skos_concept must be a string")
            elif not concept.startswith("http"):
                self.errors.append(f"skos_concept should be a URI: {concept}")
        else:
            self.warnings.append("Missing skos_concept (recommended for primary identifier)")
            
        # Check skos_preferred_label
        if "skos_preferred_label" not in semantic_links:
            self.warnings.append("Missing skos_preferred_label (required for multilingual support)")
        else:
            labels = semantic_links["skos_preferred_label"]
            if not isinstance(labels, dict):
                self.errors.append("skos_preferred_label must be an object")
                
        # Check skos_definition
        if "skos_definition" in semantic_links:
            definition = semantic_links["skos_definition"]
            if isinstance(definition, dict):
                if "source" not in definition:
                    self.warnings.append("skos_definition should include source citation")
            elif not isinstance(definition, str):
                self.errors.append("skos_definition must be string or object")
                
    def _validate_multilingual(self, semantic_links: Dict):
        """Validate multilingual labels."""
        if "skos_preferred_label" not in semantic_links:
            return
            
        labels = semantic_links["skos_preferred_label"]
        if not isinstance(labels, dict):
            return
            
        # Check required languages
        for lang in REQUIRED_LANGUAGES:
            if lang not in labels:
                self.warnings.append(f"Missing required language: {lang}")
            elif not labels[lang] or not labels[lang].strip():
                self.errors.append(f"Empty label for language: {lang}")
                
        # Check for extra languages (positive note)
        extra_langs = [lang for lang in labels.keys() if lang not in REQUIRED_LANGUAGES]
        if extra_langs:
            self.info.append(f"Includes optional languages: {', '.join(extra_langs)}")
            
    def _check_reference_alignment(self, semantic_links: Dict):
        """Check if URIs align with reference ontology."""
        if "exact_matches" not in semantic_links:
            return
            
        found_concepts = []
        for uri in semantic_links["exact_matches"]:
            for concept_name, refs in REFERENCE_ONTOLOGY.items():
                if uri in refs.values():
                    found_concepts.append(concept_name)
                    break
                    
        if found_concepts:
            self.info.append(f"Aligned with reference concepts: {', '.join(set(found_concepts))}")
        else:
            self.info.append("No alignment with NPV reference ontology (may be valid for other domains)")

def validate_directory(directory: Path) -> Dict:
    """Validate all JSON files in a directory."""
    validator = OntologyValidator()
    results = {}
    
    json_files = list(directory.rglob("*.json"))
    
    for json_file in json_files:
        success, errors, warnings, info = validator.validate_aku(json_file)
        results[str(json_file)] = {
            "success": success,
            "errors": errors,
            "warnings": warnings,
            "info": info
        }
        
    return results

def print_results(results: Dict, verbose: bool = False):
    """Print validation results."""
    total = len(results)
    passed = sum(1 for r in results.values() if r["success"])
    failed = total - passed
    
    print(f"\n{'='*70}")
    print(f"Validation Results: {passed}/{total} passed")
    print(f"{'='*70}\n")
    
    for file_path, result in results.items():
        status = "✓ PASS" if result["success"] else "✗ FAIL"
        print(f"{status}: {Path(file_path).name}")
        
        if result["errors"]:
            print(f"  Errors ({len(result['errors'])}):")
            for error in result["errors"]:
                print(f"    ✗ {error}")
                
        if result["warnings"] and verbose:
            print(f"  Warnings ({len(result['warnings'])}):")
            for warning in result["warnings"]:
                print(f"    ⚠ {warning}")
                
        if result["info"] and verbose:
            print(f"  Info ({len(result['info'])}):")
            for info in result["info"]:
                print(f"    ℹ {info}")
                
        print()
        
    # Summary
    total_errors = sum(len(r["errors"]) for r in results.values())
    total_warnings = sum(len(r["warnings"]) for r in results.values())
    
    print(f"{'='*70}")
    print(f"Total: {total_errors} errors, {total_warnings} warnings")
    print(f"{'='*70}\n")
    
    return failed == 0

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate NPV ontology identifiers in AKUs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate single file
  python3 validate_npv_ontology.py aku.json
  
  # Validate directory
  python3 validate_npv_ontology.py --directory path/to/akus/
  
  # Verbose output
  python3 validate_npv_ontology.py --verbose aku.json
        """
    )
    
    parser.add_argument("file", nargs="?", help="AKU JSON file to validate")
    parser.add_argument("--directory", "-d", help="Directory containing AKU files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if not args.file and not args.directory:
        parser.print_help()
        sys.exit(1)
        
    validator = OntologyValidator()
    
    if args.directory:
        # Validate directory
        directory = Path(args.directory)
        if not directory.exists():
            print(f"Error: Directory not found: {directory}")
            sys.exit(1)
            
        results = validate_directory(directory)
        success = print_results(results, args.verbose)
        sys.exit(0 if success else 1)
    else:
        # Validate single file
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
            
        success, errors, warnings, info = validator.validate_aku(file_path)
        
        print(f"\n{'='*70}")
        print(f"Validating: {file_path.name}")
        print(f"{'='*70}\n")
        
        if errors:
            print(f"✗ FAILED with {len(errors)} error(s):")
            for error in errors:
                print(f"  ✗ {error}")
            print()
            
        if warnings:
            print(f"⚠ {len(warnings)} warning(s):")
            for warning in warnings:
                print(f"  ⚠ {warning}")
            print()
            
        if info and args.verbose:
            print(f"ℹ Info:")
            for i in info:
                print(f"  ℹ {i}")
            print()
            
        if success:
            print("✓ PASSED\n")
        else:
            print("✗ FAILED\n")
            
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
