#!/usr/bin/env python3
"""
AKU Ontology Migration Script

Migrates existing AKU files to include ontology integration:
- Adds proper @context with domain-specific contexts
- Adds SKOS labels and definitions
- Converts legacy relationships to SKOS format
- Suggests external ontology mappings

Usage:
    python migrate_to_ontology.py path/to/aku.json
    python migrate_to_ontology.py --directory path/to/akus/
    python migrate_to_ontology.py --domain economics --dry-run
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class OntologyMigrator:
    """Migrates AKUs to ontology-enhanced format."""
    
    # Domain to context mapping
    DOMAIN_CONTEXTS = {
        "medicine": "medicine.jsonld",
        "economics": "economics.jsonld",
        "science": "science.jsonld",
        "math": "science.jsonld",
        "physics": "science.jsonld",
        "chemistry": "science.jsonld",
        "biology": "science.jsonld",
    }
    
    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.stats = {
            "processed": 0,
            "migrated": 0,
            "skipped": 0,
            "errors": 0
        }
    
    def migrate_aku(self, aku_path: Path) -> bool:
        """
        Migrate a single AKU file to ontology format.
        
        Args:
            aku_path: Path to AKU JSON file
            
        Returns:
            True if migrated, False if skipped or error
        """
        self.stats["processed"] += 1
        
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except Exception as e:
            print(f"❌ Error reading {aku_path}: {e}")
            self.stats["errors"] += 1
            return False
        
        # Check if already migrated
        if self._is_already_migrated(aku):
            if self.verbose:
                print(f"⏭️  Skipping {aku_path.name} (already has ontology support)")
            self.stats["skipped"] += 1
            return False
        
        # Perform migration
        migrated_aku = self._migrate_aku_content(aku)
        
        # Save or print
        if self.dry_run:
            print(f"\n{'='*70}")
            print(f"DRY RUN: {aku_path.name}")
            print(f"{'='*70}")
            print(json.dumps(migrated_aku, indent=2))
            print()
        else:
            # Write back to file
            with open(aku_path, 'w', encoding='utf-8') as f:
                json.dump(migrated_aku, f, indent=2, ensure_ascii=False)
            
            if self.verbose:
                print(f"✅ Migrated {aku_path.name}")
        
        self.stats["migrated"] += 1
        return True
    
    def _is_already_migrated(self, aku: Dict) -> bool:
        """Check if AKU already has ontology support."""
        # Check for SKOS properties
        has_skos_labels = any(key in aku for key in ["skos:prefLabel", "prefLabel"])
        
        # Check for enhanced context
        if "@context" in aku:
            context = aku["@context"]
            if isinstance(context, list):
                # Check if includes base.jsonld or domain contexts
                context_str = str(context)
                if "base.jsonld" in context_str or any(
                    ctx in context_str for ctx in ["medicine.jsonld", "economics.jsonld", "science.jsonld"]
                ):
                    return True
        
        return has_skos_labels
    
    def _migrate_aku_content(self, aku: Dict) -> Dict:
        """Apply ontology enhancements to AKU."""
        # 1. Update @context
        aku = self._update_context(aku)
        
        # 2. Add/update @id
        aku = self._update_id(aku)
        
        # 3. Add/update @type
        aku = self._update_type(aku)
        
        # 4. Add SKOS labels
        aku = self._add_skos_labels(aku)
        
        # 5. Convert relationships to SKOS
        aku = self._convert_relationships(aku)
        
        # 6. Add provenance metadata
        aku = self._add_provenance(aku)
        
        return aku
    
    def _update_context(self, aku: Dict) -> Dict:
        """Update @context to include domain-specific context."""
        domain = self._detect_domain(aku)
        domain_context = self.DOMAIN_CONTEXTS.get(domain, "base.jsonld")
        
        new_context = [
            "https://worldsmegraphs.org/contexts/base.jsonld",
            f"https://worldsmegraphs.org/contexts/{domain_context}"
        ]
        
        # Preserve local context if exists
        if "@context" in aku:
            old_context = aku["@context"]
            if isinstance(old_context, dict):
                new_context.append(old_context)
        
        aku["@context"] = new_context
        return aku
    
    def _update_id(self, aku: Dict) -> Dict:
        """Update @id to follow ontology naming convention."""
        if "@id" not in aku:
            # Generate ID from classification
            domain = self._detect_domain(aku)
            concept = self._extract_concept_name(aku)
            aku_id_num = aku.get("classification", {}).get("aku_id", "001")
            
            aku["@id"] = f"wsmg-{domain}:{concept}-{aku_id_num}"
        
        return aku
    
    def _update_type(self, aku: Dict) -> Dict:
        """Update @type to include SKOS concept."""
        current_type = aku.get("@type", "schema:EducationalResource")
        
        if isinstance(current_type, str):
            types = [current_type]
        else:
            types = list(current_type)
        
        # Add skos:Concept if not present
        if "skos:Concept" not in types and "Concept" not in types:
            types.append("skos:Concept")
        
        aku["@type"] = types
        return aku
    
    def _add_skos_labels(self, aku: Dict) -> Dict:
        """Add SKOS labeling properties."""
        # Extract from content if available
        content = aku.get("content", {})
        statement = content.get("statement", {})
        
        # Add prefLabel if not exists
        if "skos:prefLabel" not in aku and "prefLabel" not in aku:
            # Try to extract from various sources
            label = (
                statement.get("text", "").split(".")[0] if statement.get("text") else
                aku.get("name", "") or
                aku.get("title", "") or
                "Unnamed Concept"
            )
            
            if label and label != "Unnamed Concept":
                aku["skos:prefLabel"] = {
                    "@language": "en",
                    "@value": label[:100]  # Limit length
                }
        
        # Add definition if not exists
        if "skos:definition" not in aku and "definition" not in aku:
            definition = statement.get("text", "") or content.get("description", "")
            if definition:
                aku["skos:definition"] = definition
        
        # Add notation if available
        aku_id = aku.get("classification", {}).get("aku_id")
        if aku_id and "skos:notation" not in aku:
            aku["skos:notation"] = aku_id
        
        return aku
    
    def _convert_relationships(self, aku: Dict) -> Dict:
        """Convert legacy relationships to SKOS format."""
        if "relationships" not in aku:
            aku["relationships"] = {}
        
        relationships = aku["relationships"]
        
        # Convert prerequisites to broader (more general concepts)
        if "prerequisites" in relationships:
            if "hierarchical" not in relationships:
                relationships["hierarchical"] = {}
            relationships["hierarchical"]["skos:broader"] = relationships["prerequisites"]
        
        # Convert enables to narrower (more specific concepts)
        if "enables" in relationships:
            if "hierarchical" not in relationships:
                relationships["hierarchical"] = {}
            relationships["hierarchical"]["skos:narrower"] = relationships["enables"]
        
        # Convert related_to to skos:related
        if "related_to" in relationships:
            if "associative" not in relationships:
                relationships["associative"] = {}
            relationships["associative"]["skos:related"] = relationships["related_to"]
        
        # Add placeholder for external mappings
        if "external" not in relationships:
            relationships["external"] = {
                "skos:exactMatch": [],
                "skos:closeMatch": [],
                "comment": "TODO: Add external ontology mappings"
            }
        
        return aku
    
    def _add_provenance(self, aku: Dict) -> Dict:
        """Add provenance tracking."""
        if "provenance" not in aku:
            aku["provenance"] = {}
        
        provenance = aku["provenance"]
        
        # Add migration activity
        if "prov:wasRevisionOf" not in provenance:
            old_id = aku.get("@id", "unknown")
            provenance["prov:wasRevisionOf"] = {
                "@id": f"{old_id}-v1",
                "dc:modified": datetime.utcnow().isoformat() + "Z",
                "comment": "Migrated to ontology-enhanced format"
            }
        
        return aku
    
    def _detect_domain(self, aku: Dict) -> str:
        """Detect domain from AKU classification."""
        if "classification" in aku and "domain_path" in aku["classification"]:
            domain_path = aku["classification"]["domain_path"]
            return domain_path.split("/")[0] if "/" in domain_path else domain_path
        return "general"
    
    def _extract_concept_name(self, aku: Dict) -> str:
        """Extract concept name from AKU."""
        # Try various sources
        if "@id" in aku:
            return aku["@id"].split(":")[-1].split("-")[0]
        
        if "content" in aku and "statement" in aku["content"]:
            statement = aku["content"]["statement"]
            # Handle both string and object formats
            if isinstance(statement, str):
                text = statement
            elif isinstance(statement, dict):
                text = statement.get("text", "")
            else:
                text = ""
            
            if text:
                # Take first few words
                words = text.split()[:3]
                return "-".join(w.lower() for w in words if w.isalnum())[:30]
        
        return "concept"
    
    def print_summary(self):
        """Print migration summary."""
        print(f"\n{'='*70}")
        print("MIGRATION SUMMARY")
        print(f"{'='*70}")
        print(f"Processed: {self.stats['processed']}")
        print(f"✅ Migrated: {self.stats['migrated']}")
        print(f"⏭️  Skipped: {self.stats['skipped']}")
        print(f"❌ Errors: {self.stats['errors']}")
        
        if self.dry_run:
            print(f"\n💡 This was a DRY RUN - no files were modified")
        else:
            print(f"\n✅ Files have been updated")


def main():
    parser = argparse.ArgumentParser(
        description="Migrate AKUs to ontology-enhanced format"
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to AKU file or directory"
    )
    parser.add_argument(
        "--directory",
        "-d",
        help="Migrate all AKUs in directory"
    )
    parser.add_argument(
        "--domain",
        help="Migrate all AKUs in domain (e.g., medicine, economics)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    migrator = OntologyMigrator(dry_run=args.dry_run, verbose=args.verbose)
    
    # Determine what to migrate
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
        # Migrate directory
        dir_path = Path(args.directory)
        if dir_path.exists():
            aku_files = list(dir_path.rglob("*.json"))
        else:
            print(f"❌ Directory not found: {args.directory}")
            return 1
    elif args.path:
        # Migrate single file or directory
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
    
    # Migrate all files
    print(f"\nMigrating {len(aku_files)} AKU(s)...")
    if args.dry_run:
        print("(DRY RUN - no files will be modified)\n")
    
    for aku_file in aku_files:
        migrator.migrate_aku(aku_file)
    
    migrator.print_summary()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
