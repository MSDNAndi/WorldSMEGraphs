"""
Quality Assurance Agent: AKU Validator

Validates Atomic Knowledge Units (AKUs) for completeness, accuracy, and format compliance.

Usage:
    python validate_aku.py path/to/aku.json
    python validate_aku.py --directory path/to/akus/  # Validate all in directory
    python validate_aku.py --pilot npv  # Validate NPV pilot AKUs

Self-contained with standard library only.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

# Required top-level keys in AKU
REQUIRED_KEYS = [
    "@context", "@type", "@id", "metadata", "classification",
    "content", "representations", "variables", "relationships",
    "provenance", "pedagogical", "rendering_hints"
]

# Metadata required fields
METADATA_REQUIRED = ["version", "created", "contributors", "confidence", "status"]

# Classification required fields
CLASSIFICATION_REQUIRED = ["domain_path", "type", "difficulty", "importance", "aku_id"]


class AKUValidator:
    """Validator for Atomic Knowledge Units."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
    
    def validate_aku(self, aku_path: Path) -> Tuple[bool, Dict]:
        """Validate a single AKU file."""
        self.errors = []
        self.warnings = []
        self.info = []
        
        # Load JSON
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False, self._create_report(aku_path)
        except Exception as e:
            self.errors.append(f"Failed to load file: {e}")
            return False, self._create_report(aku_path)
        
        # Structural validation
        self._validate_structure(aku)
        
        # Content validation
        self._validate_content(aku)
        
        # Formula validation
        self._validate_formulas(aku)
        
        # Relationship validation
        self._validate_relationships(aku)
        
        # Provenance validation
        self._validate_provenance(aku)
        
        # Pedagogical validation
        self._validate_pedagogical(aku)
        
        is_valid = len(self.errors) == 0
        return is_valid, self._create_report(aku_path)
    
    def _validate_structure(self, aku: Dict):
        """Validate AKU structure."""
        # Check top-level keys
        for key in REQUIRED_KEYS:
            if key not in aku:
                self.errors.append(f"Missing required key: {key}")
        
        # Check metadata
        if "metadata" in aku:
            for key in METADATA_REQUIRED:
                if key not in aku["metadata"]:
                    self.errors.append(f"Missing metadata.{key}")
            
            # Check confidence range
            if "confidence" in aku["metadata"]:
                conf = aku["metadata"]["confidence"]
                if not (0 <= conf <= 1):
                    self.errors.append(f"Confidence must be 0-1, got {conf}")
        
        # Check classification
        if "classification" in aku:
            for key in CLASSIFICATION_REQUIRED:
                if key not in aku["classification"]:
                    self.errors.append(f"Missing classification.{key}")
    
    def _validate_content(self, aku: Dict):
        """Validate content section."""
        if "content" not in aku:
            return
        
        content = aku["content"]
        
        # Check statement
        if "statement" not in content:
            self.errors.append("Missing content.statement")
        elif "text" not in content["statement"]:
            self.errors.append("Missing content.statement.text")
        
        # Check explanation
        if "explanation" not in content:
            self.warnings.append("Missing content.explanation (recommended)")
        else:
            explanation = content["explanation"]
            if "intuition" not in explanation:
                self.warnings.append("Missing content.explanation.intuition")
            if "key_insight" not in explanation:
                self.warnings.append("Missing content.explanation.key_insight")
    
    def _validate_formulas(self, aku: Dict):
        """Validate formulas if present."""
        if "representations" not in aku:
            return
        
        reps = aku["representations"]
        
        # Check for executable code
        if "latex" in reps and "python" not in reps:
            self.warnings.append("LaTeX formula present but no Python code")
        
        # Validate Python code structure
        if "python" in reps:
            if isinstance(reps["python"], dict):
                if "code" not in reps["python"]:
                    self.errors.append("Python representation missing 'code' field")
                if "test_cases" not in reps["python"]:
                    self.warnings.append("Python code missing test_cases")
            else:
                self.warnings.append("Python should be dict with 'code' and 'test_cases'")
    
    def _validate_relationships(self, aku: Dict):
        """Validate relationships."""
        if "relationships" not in aku:
            return
        
        rels = aku["relationships"]
        
        # Check for key relationship types
        if "prerequisites" not in rels:
            self.info.append("No prerequisites specified")
        
        if "enables" not in rels:
            self.info.append("No 'enables' relationships specified")
        
        # Warn if no relationships at all
        if all(not rels.get(key) for key in ["prerequisites", "enables", "related_to"]):
            self.warnings.append("AKU has no relationships to other concepts")
    
    def _validate_provenance(self, aku: Dict):
        """Validate provenance."""
        if "provenance" not in aku:
            return
        
        prov = aku["provenance"]
        
        if "sources" not in prov or not prov["sources"]:
            self.errors.append("No sources provided in provenance")
        else:
            for i, source in enumerate(prov["sources"]):
                if "type" not in source:
                    self.errors.append(f"Source {i}: missing 'type'")
                if "title" not in source:
                    self.errors.append(f"Source {i}: missing 'title'")
        
        if "validation_method" not in prov:
            self.warnings.append("No validation_method specified in provenance")
    
    def _validate_pedagogical(self, aku: Dict):
        """Validate pedagogical section."""
        if "pedagogical" not in aku:
            return
        
        ped = aku["pedagogical"]
        
        if "target_audiences" not in ped:
            self.warnings.append("No target_audiences specified")
        
        if "learning_objectives" not in ped:
            self.warnings.append("No learning_objectives specified")
        
        if "common_errors" not in ped:
            self.info.append("No common_errors specified (helpful for students)")
    
    def _create_report(self, aku_path: Path) -> Dict:
        """Create validation report."""
        return {
            "file": str(aku_path),
            "timestamp": datetime.now().isoformat(),
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "summary": {
                "total_errors": len(self.errors),
                "total_warnings": len(self.warnings),
                "total_info": len(self.info)
            }
        }
    
    def print_report(self, report: Dict):
        """Print validation report to console."""
        print(f"\n{'='*60}")
        print(f"AKU VALIDATION REPORT")
        print(f"{'='*60}")
        print(f"File: {report['file']}")
        print(f"Status: {'✓ VALID' if report['valid'] else '✗ INVALID'}")
        print(f"Timestamp: {report['timestamp']}\n")
        
        if report['errors']:
            print(f"ERRORS ({len(report['errors'])}):")
            for error in report['errors']:
                print(f"  ✗ {error}")
            print()
        
        if report['warnings']:
            print(f"WARNINGS ({len(report['warnings'])}):")
            for warning in report['warnings']:
                print(f"  ⚠ {warning}")
            print()
        
        if report['info']:
            print(f"INFO ({len(report['info'])}):")
            for info in report['info']:
                print(f"  ℹ {info}")
            print()
        
        print(f"{'='*60}\n")


def validate_directory(directory: Path):
    """Validate all JSON files in a directory."""
    validator = AKUValidator()
    results = []
    
    json_files = list(directory.rglob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in {directory}")
        return
    
    print(f"Found {len(json_files)} AKU files to validate\n")
    
    for json_file in json_files:
        is_valid, report = validator.validate_aku(json_file)
        results.append(report)
        
        # Print brief result
        status = "✓" if is_valid else "✗"
        errors = report['summary']['total_errors']
        warnings = report['summary']['total_warnings']
        print(f"{status} {json_file.name:50} Errors: {errors:2} Warnings: {warnings:2}")
    
    # Print summary
    total = len(results)
    valid = sum(1 for r in results if r['valid'])
    invalid = total - valid
    total_errors = sum(r['summary']['total_errors'] for r in results)
    total_warnings = sum(r['summary']['total_warnings'] for r in results)
    
    print(f"\n{'='*60}")
    print(f"VALIDATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total AKUs: {total}")
    print(f"Valid: {valid}")
    print(f"Invalid: {invalid}")
    print(f"Total Errors: {total_errors}")
    print(f"Total Warnings: {total_warnings}")
    print(f"{'='*60}\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python validate_aku.py path/to/aku.json")
        print("  python validate_aku.py --directory path/to/akus/")
        print("  python validate_aku.py --pilot npv")
        return
    
    arg = sys.argv[1]
    
    if arg == "--pilot" and len(sys.argv) > 2:
        pilot_name = sys.argv[2]
        pilot_dir = Path(__file__).parent.parent.parent / "pilot" / f"{pilot_name}-finance" / "akus"
        if pilot_dir.exists():
            validate_directory(pilot_dir)
        else:
            print(f"Pilot directory not found: {pilot_dir}")
    elif arg == "--directory" and len(sys.argv) > 2:
        directory = Path(sys.argv[2])
        if directory.exists():
            validate_directory(directory)
        else:
            print(f"Directory not found: {directory}")
    else:
        aku_path = Path(arg)
        if aku_path.exists():
            validator = AKUValidator()
            is_valid, report = validator.validate_aku(aku_path)
            validator.print_report(report)
        else:
            print(f"File not found: {aku_path}")


if __name__ == "__main__":
    main()
