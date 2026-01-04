#!/usr/bin/env python3
"""
Migrate Category Theory AKUs from Computer Science to Mathematics

This script migrates category theory AKUs from their incorrect location in
science/computer-science/functional-theory/category-theory/ to the correct
native mathematics location: formal-sciences/mathematics/pure-mathematics/category-theory/

Per the global hierarchy (domain/_ontology/global-hierarchy.yaml), category theory
is a mathematical discipline, not a computer science one.

Changes made:
1. Updates classification.domain_path to formal-sciences/mathematics/pure-mathematics/category-theory
2. Adds classification.isNativeDomain: true
3. Updates @id to reflect new path
4. Adds cross_domain_applications section documenting FP usage
5. Updates modified timestamp to current UTC time
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

def get_utc_timestamp():
    """Get current UTC timestamp in ISO 8601 format with milliseconds"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def migrate_category_theory_aku(aku_path):
    """
    Migrate a single category theory AKU from CS to Math
    
    Args:
        aku_path: Path to the AKU file
        
    Returns:
        tuple: (success: bool, message: str, updated_aku: dict or None)
    """
    try:
        with open(aku_path, 'r', encoding='utf-8') as f:
            aku = json.load(f)
        
        # Get the AKU ID for messaging
        aku_id = aku.get('@id', 'unknown')
        
        # Update classification.domain_path
        if 'classification' not in aku:
            aku['classification'] = {}
        
        old_path = aku['classification'].get('domain_path', '')
        new_path = 'formal-sciences/mathematics/pure-mathematics/category-theory'
        aku['classification']['domain_path'] = new_path
        
        # Mark as native domain
        aku['classification']['isNativeDomain'] = True
        
        # Update @id to reflect new path
        old_id = aku.get('@id', '')
        # Convert: aku:functional-theory:category-theory:... -> aku:math:category-theory:...
        if old_id.startswith('aku:functional-theory:category-theory:'):
            new_id = old_id.replace('aku:functional-theory:category-theory:', 'aku:math:category-theory:')
            aku['@id'] = new_id
        
        # Update modified timestamp
        if 'metadata' not in aku:
            aku['metadata'] = {}
        aku['metadata']['modified'] = get_utc_timestamp()
        
        # Add cross-domain applications section
        aku['cross_domain_applications'] = {
            "note": "This mathematical concept is APPLIED in other domains",
            "applications": [
                {
                    "domain": "formal-sciences/computer-science/programming-paradigms/functional-programming",
                    "context": "Category theory provides the theoretical foundation for functional programming, including composition, functors, and monads",
                    "relationship": "applies"
                },
                {
                    "domain": "formal-sciences/computer-science/type-theory",
                    "context": "Type theory uses categorical semantics, especially cartesian closed categories",
                    "relationship": "uses"
                }
            ]
        }
        
        message = f"✅ Migrated {aku_id}: {old_path} -> {new_path}"
        return True, message, aku
        
    except Exception as e:
        return False, f"❌ Error migrating {aku_path}: {str(e)}", None

def main():
    """Main migration function"""
    # Define paths
    repo_root = Path(__file__).parent.parent.parent.parent
    old_dir = repo_root / "domain/science/computer-science/functional-theory/category-theory/akus"
    new_dir = repo_root / "domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus"
    
    print("=" * 70)
    print("Category Theory Migration: Computer Science → Mathematics")
    print("=" * 70)
    print(f"\nSource: {old_dir}")
    print(f"Target: {new_dir}")
    print()
    
    # Ensure new directory exists
    new_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all category theory AKUs
    aku_files = sorted(old_dir.glob("ct-*.json"))
    
    if not aku_files:
        print("❌ No category theory AKU files found!")
        return 1
    
    print(f"Found {len(aku_files)} category theory AKUs to migrate\n")
    
    # Migrate each AKU
    success_count = 0
    failed_count = 0
    
    for aku_file in aku_files:
        success, message, updated_aku = migrate_category_theory_aku(aku_file)
        print(message)
        
        if success and updated_aku:
            # Write to new location
            new_file = new_dir / aku_file.name
            with open(new_file, 'w', encoding='utf-8') as f:
                json.dump(updated_aku, f, indent=2, ensure_ascii=False)
                f.write('\n')
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 70)
    print("Migration Summary")
    print("=" * 70)
    print(f"✅ Successfully migrated: {success_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"📁 New location: {new_dir}")
    print("\nNext steps:")
    print("1. Review migrated AKUs in new location")
    print("2. Update functional-theory AKUs with cross_domain_references")
    print("3. Update concept-index.yaml files")
    print("4. Run validation: python domain/_ontology/tools/validate_cross_domain.py")
    print("5. Delete old category-theory directory after verification")
    
    return 0 if failed_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
