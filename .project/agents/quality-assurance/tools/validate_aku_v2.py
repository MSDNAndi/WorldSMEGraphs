"""
Domain-Aware AKU Validator

Validates Atomic Knowledge Units (AKUs) across multiple domains with domain-specific rules.
Follows guidance from @verification and @ontology agents for validation best practices.

Usage:
    python validate_aku_v2.py path/to/aku.json
    python validate_aku_v2.py --directory path/to/akus/
    python validate_aku_v2.py --domain medicine  # Validate all medical AKUs

Features:
- Domain-specific validation rules (math, medicine, economics, etc.)
- Auto-detection of domain from classification.domain_path
- Flexible schema validation based on content type
- Detailed error reporting with suggestions

Self-contained with standard library only.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
from datetime import datetime
import re

# Core required keys for ALL AKUs (domain-agnostic)
CORE_REQUIRED_KEYS = ["@context", "@type", "@id", "metadata", "classification", "content"]

# Metadata required fields
METADATA_REQUIRED = ["version", "created", "contributors", "confidence", "status"]

# Classification required fields
CLASSIFICATION_REQUIRED = ["domain_path", "type", "difficulty", "importance"]

# Domain-specific required keys
DOMAIN_REQUIREMENTS = {
    "math": ["representations", "variables", "relationships", "provenance"],
    "medicine": ["clinical_features", "relationships", "provenance"],
    "economics": ["economic_concepts", "relationships", "provenance"],
    "science": ["scientific_principles", "relationships", "provenance"],
}

# Optional keys that may appear
OPTIONAL_KEYS = [
    "pedagogical", "rendering_hints", "examples", "applications",
    "imaging_characteristics", "diagnostic_criteria", "treatment_options",
    "formulas", "equations", "proofs", "derivations"
]


class DomainAwareAKUValidator:
    """Validator for Atomic Knowledge Units with domain-specific rules."""
    
    def __init__(self, verbose: bool = False):
        self.errors = []
        self.warnings = []
        self.info = []
        self.verbose = verbose
    
    def validate_aku(self, aku_path: Path) -> Tuple[bool, Dict]:
        """Validate a single AKU file with domain-specific rules."""
        self.errors = []
        self.warnings = []
        self.info = []
        
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Validating: {aku_path.name}")
            print(f"{'='*60}")
        
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
        
        # Detect domain
        domain = self._detect_domain(aku)
        self.info.append(f"Detected domain: {domain}")
        
        # Structural validation (domain-agnostic)
        self._validate_core_structure(aku)
        
        # Domain-specific validation
        if domain in DOMAIN_REQUIREMENTS:
            self._validate_domain_specific(aku, domain)
        else:
            self.warnings.append(f"Unknown domain '{domain}' - using generic validation")
        
        # Content validation
        self._validate_content(aku, domain)
        
        # Metadata validation
        self._validate_metadata(aku)
        
        # ID and reference validation
        self._validate_ids(aku)
        
        # Relationship validation
        if "relationships" in aku:
            self._validate_relationships(aku["relationships"])
        
        # Provenance validation
        if "provenance" in aku:
            self._validate_provenance(aku["provenance"])
        
        is_valid = len(self.errors) == 0
        return is_valid, self._create_report(aku_path)
    
    def _detect_domain(self, aku: Dict) -> str:
        """Detect domain from classification.domain_path."""
        if "classification" in aku and "domain_path" in aku["classification"]:
            path = aku["classification"]["domain_path"]
            # Extract top-level domain (e.g., "medicine" from "medicine/surgery/vascular")
            parts = path.split('/')
            return parts[0] if parts else "unknown"
        return "unknown"
    
    def _validate_core_structure(self, aku: Dict):
        """Validate core AKU structure (domain-agnostic)."""
        # Check core keys
        for key in CORE_REQUIRED_KEYS:
            if key not in aku:
                self.errors.append(f"Missing required core key: {key}")
        
        # Check metadata structure
        if "metadata" in aku:
            for key in METADATA_REQUIRED:
                if key not in aku["metadata"]:
                    self.errors.append(f"Missing metadata.{key}")
            
            # Validate confidence range
            if "confidence" in aku["metadata"]:
                conf = aku["metadata"]["confidence"]
                if not isinstance(conf, (int, float)) or not (0 <= conf <= 1):
                    self.errors.append(f"metadata.confidence must be 0-1, got {conf}")
            
            # Validate timestamp format
            if "created" in aku["metadata"]:
                self._validate_timestamp(aku["metadata"]["created"], "metadata.created")
        
        # Check classification structure
        if "classification" in aku:
            for key in CLASSIFICATION_REQUIRED:
                if key not in aku["classification"]:
                    self.errors.append(f"Missing classification.{key}")
            
            # Validate difficulty level
            if "difficulty" in aku["classification"]:
                valid_difficulties = ["beginner", "elementary", "intermediate", "advanced", "expert"]
                if aku["classification"]["difficulty"] not in valid_difficulties:
                    self.warnings.append(
                        f"classification.difficulty should be one of {valid_difficulties}"
                    )
            
            # Validate importance level
            if "importance" in aku["classification"]:
                valid_importance = ["low", "medium", "high", "critical", "foundational"]
                if aku["classification"]["importance"] not in valid_importance:
                    self.warnings.append(
                        f"classification.importance should be one of {valid_importance}"
                    )
    
    def _validate_domain_specific(self, aku: Dict, domain: str):
        """Validate domain-specific required fields."""
        required_keys = DOMAIN_REQUIREMENTS.get(domain, [])
        
        for key in required_keys:
            if key not in aku:
                # Check if it's really required or if alternatives exist
                if key == "representations" and domain == "math":
                    # For math, representations is critical
                    self.errors.append(f"Missing required key for {domain} domain: {key}")
                elif key == "clinical_features" and domain == "medicine":
                    # For medicine, clinical_features is expected
                    if "content" in aku and isinstance(aku["content"], dict):
                        # Check if content has clinical information
                        if not any(k in aku["content"] for k in ["clinical_context", "clinical_significance"]):
                            self.warnings.append(
                                f"Missing {key} - consider adding clinical information"
                            )
                elif key == "economic_concepts" and domain == "economics":
                    self.warnings.append(f"Missing {key} - consider adding for {domain} domain")
                else:
                    self.warnings.append(f"Missing recommended key for {domain} domain: {key}")
    
    def _validate_content(self, aku: Dict, domain: str):
        """Validate content structure based on domain."""
        if "content" not in aku:
            return  # Already flagged in core validation
        
        content = aku["content"]
        
        if not isinstance(content, dict):
            self.errors.append("content must be a dictionary/object")
            return
        
        # Domain-specific content validation
        if domain == "medicine":
            self._validate_medical_content(content)
        elif domain == "math":
            self._validate_math_content(content)
        elif domain == "economics":
            self._validate_economics_content(content)
        
        # Check for explanation quality
        if "explanation" in content:
            exp = content["explanation"]
            if isinstance(exp, dict):
                if "intuition" in exp and len(exp["intuition"]) < 20:
                    self.warnings.append("explanation.intuition is too short (< 20 chars)")
                if "key_insight" in exp and len(exp["key_insight"]) < 20:
                    self.warnings.append("explanation.key_insight is too short (< 20 chars)")
    
    def _validate_medical_content(self, content: Dict):
        """Validate medical-specific content."""
        # Check for statement
        if "statement" not in content:
            self.warnings.append("Medical AKUs should have content.statement")
        
        # Check for definitions glossary
        if "definitions_glossary" not in content:
            self.info.append("Consider adding definitions_glossary for medical terms")
        
        # Check for explanation
        if "explanation" not in content:
            self.warnings.append("Medical AKUs should include explanation for different audiences")
    
    def _validate_math_content(self, content: Dict):
        """Validate mathematics-specific content."""
        # Math AKUs should have formal representation
        if "statement" not in content and "definition" not in content:
            self.warnings.append("Math AKUs should have content.statement or content.definition")
    
    def _validate_economics_content(self, content: Dict):
        """Validate economics-specific content."""
        # Economics AKUs should have clear definition
        if "statement" not in content and "definition" not in content:
            self.warnings.append("Economics AKUs should have clear statement or definition")
    
    def _validate_metadata(self, aku: Dict):
        """Validate metadata fields."""
        if "metadata" not in aku:
            return
        
        metadata = aku["metadata"]
        
        # Validate version format (semver)
        if "version" in metadata:
            version = metadata["version"]
            if not re.match(r'^\d+\.\d+\.\d+$', version):
                self.warnings.append(f"version should follow semver format (e.g., '1.0.0'), got '{version}'")
        
        # Validate contributors is array
        if "contributors" in metadata:
            if not isinstance(metadata["contributors"], list):
                self.errors.append("metadata.contributors must be an array")
            elif len(metadata["contributors"]) == 0:
                self.warnings.append("metadata.contributors is empty")
        
        # Validate status
        if "status" in metadata:
            valid_statuses = ["draft", "review", "validated", "published", "archived"]
            if metadata["status"] not in valid_statuses:
                self.warnings.append(
                    f"metadata.status should be one of {valid_statuses}, got '{metadata['status']}'"
                )
    
    def _validate_timestamp(self, timestamp: str, field_name: str):
        """Validate ISO 8601 timestamp format."""
        try:
            # Try to parse as ISO 8601
            datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            self.warnings.append(f"{field_name} should be ISO 8601 format (e.g., '2025-12-27T14:55:00.000Z')")
    
    def _validate_ids(self, aku: Dict):
        """Validate ID formats and consistency."""
        # Check @id format
        if "@id" in aku:
            aku_id = aku["@id"]
            if not isinstance(aku_id, str) or len(aku_id) == 0:
                self.errors.append("@id must be a non-empty string")
            
            # Check if it follows recommended format
            if "/" in aku_id or "\\" in aku_id:
                self.warnings.append("@id contains path separators - consider using colon notation")
        
        # Check aku_id in classification
        if "classification" in aku and "aku_id" in aku["classification"]:
            local_id = aku["classification"]["aku_id"]
            if not isinstance(local_id, str):
                self.errors.append("classification.aku_id must be a string")
    
    def _validate_relationships(self, relationships: Dict):
        """Validate relationships structure."""
        if not isinstance(relationships, dict):
            self.errors.append("relationships must be a dictionary/object")
            return
        
        # Check for common relationship types
        common_types = ["prerequisites", "related", "applications", "broader", "narrower", "seeAlso"]
        found_types = [key for key in relationships.keys() if key in common_types]
        
        if len(found_types) == 0:
            self.info.append(f"No standard relationship types found. Consider using: {common_types}")
        
        # Validate relationship arrays
        for key, value in relationships.items():
            if not isinstance(value, list):
                self.warnings.append(f"relationships.{key} should be an array")
    
    def _validate_provenance(self, provenance: Dict):
        """Validate provenance information."""
        if not isinstance(provenance, dict):
            self.errors.append("provenance must be a dictionary/object")
            return
        
        # Check for sources
        if "sources" not in provenance:
            self.warnings.append("provenance should include sources")
        else:
            sources = provenance["sources"]
            if not isinstance(sources, list):
                self.errors.append("provenance.sources must be an array")
            elif len(sources) == 0:
                self.warnings.append("provenance.sources is empty - add source references")
    
    def _create_report(self, aku_path: Path) -> Dict:
        """Create validation report."""
        return {
            "file": str(aku_path),
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "info_count": len(self.info)
        }
    
    def print_report(self, report: Dict):
        """Print validation report."""
        print(f"\nFile: {report['file']}")
        print(f"Status: {'✅ VALID' if report['valid'] else '❌ INVALID'}")
        
        if report['errors']:
            print(f"\n❌ Errors ({report['error_count']}):")
            for error in report['errors']:
                print(f"   - {error}")
        
        if report['warnings']:
            print(f"\n⚠️  Warnings ({report['warning_count']}):")
            for warning in report['warnings']:
                print(f"   - {warning}")
        
        if self.verbose and report['info']:
            print(f"\nℹ️  Info ({report['info_count']}):")
            for info in report['info']:
                print(f"   - {info}")


def validate_directory(directory: Path, domain: str = None, verbose: bool = False) -> Tuple[int, int]:
    """Validate all AKU files in a directory."""
    validator = DomainAwareAKUValidator(verbose=verbose)
    
    # Find all JSON files
    if domain:
        pattern = f"domain/{domain}/**/*.json"
        aku_files = list(Path(".").glob(pattern))
    else:
        aku_files = list(directory.glob("**/*.json"))
    
    if not aku_files:
        print(f"No JSON files found in {directory}")
        return 0, 0
    
    print(f"\n{'='*60}")
    print(f"Validating {len(aku_files)} AKU files")
    print(f"{'='*60}")
    
    valid_count = 0
    invalid_count = 0
    
    for aku_file in sorted(aku_files):
        # Skip schema files
        if "schema.json" in aku_file.name:
            continue
        
        is_valid, report = validator.validate_aku(aku_file)
        
        if verbose or not is_valid:
            validator.print_report(report)
        
        if is_valid:
            valid_count += 1
        else:
            invalid_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✅ Valid: {valid_count}")
    print(f"  ❌ Invalid: {invalid_count}")
    print(f"  Total: {valid_count + invalid_count}")
    print(f"{'='*60}")
    
    return valid_count, invalid_count


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate Atomic Knowledge Units (AKUs) with domain-specific rules"
    )
    parser.add_argument("path", nargs="?", help="Path to AKU file or directory")
    parser.add_argument("--directory", "-d", help="Validate all AKUs in directory")
    parser.add_argument("--domain", help="Validate all AKUs in specific domain (e.g., 'medicine')")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if args.domain:
        domain_path = Path(f"domain/{args.domain}")
        if not domain_path.exists():
            print(f"Error: Domain directory not found: {domain_path}")
            sys.exit(1)
        valid, invalid = validate_directory(domain_path, args.domain, args.verbose)
        sys.exit(0 if invalid == 0 else 1)
    
    elif args.directory:
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {dir_path}")
            sys.exit(1)
        valid, invalid = validate_directory(dir_path, verbose=args.verbose)
        sys.exit(0 if invalid == 0 else 1)
    
    elif args.path:
        aku_path = Path(args.path)
        if not aku_path.exists():
            print(f"Error: File not found: {aku_path}")
            sys.exit(1)
        
        if aku_path.is_dir():
            valid, invalid = validate_directory(aku_path, verbose=args.verbose)
            sys.exit(0 if invalid == 0 else 1)
        else:
            validator = DomainAwareAKUValidator(verbose=args.verbose)
            is_valid, report = validator.validate_aku(aku_path)
            validator.print_report(report)
            sys.exit(0 if is_valid else 1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
