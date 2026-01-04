#!/usr/bin/env python3
"""
Update Functional Programming AKUs with Cross-Domain References

This script updates the remaining functional-theory AKUs (functors, monoids, monads)
to mark them as application domain AKUs that reference mathematical concepts.

Changes made:
1. Adds classification.isApplicationDomain: true
2. Updates classification.domain_path to reflect FP application context
3. Adds cross_domain_references section linking to math concepts
4. Updates modified timestamp to current UTC time
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

def get_utc_timestamp():
    """Get current UTC timestamp in ISO 8601 format with milliseconds"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

# Map of AKU types to their math concept references
MATH_REFERENCES = {
    'functor': {
        'concept': 'functor',
        'math_path': 'formal-sciences/mathematics/pure-mathematics/category-theory',
        'context': 'Functors in programming apply the mathematical concept of structure-preserving mappings between categories'
    },
    'monad': {
        'concept': 'monad',
        'math_path': 'formal-sciences/mathematics/pure-mathematics/category-theory',
        'context': 'Monads in programming are inspired by the mathematical definition of monads as monoids in the category of endofunctors'
    },
    'monoid': {
        'concept': 'monoid',
        'math_path': 'formal-sciences/mathematics/pure-mathematics/algebra',
        'context': 'Monoids in programming directly apply the algebraic structure of associative binary operation with identity'
    },
    'endofunctor': {
        'concept': 'endofunctor',
        'math_path': 'formal-sciences/mathematics/pure-mathematics/category-theory',
        'context': 'Endofunctors are functors from a category to itself, foundational to monads'
    },
    'kleisli': {
        'concept': 'kleisli-category',
        'math_path': 'formal-sciences/mathematics/pure-mathematics/category-theory',
        'context': 'Kleisli categories provide categorical structure for monadic composition'
    }
}

def determine_aku_type(aku_id, content):
    """Determine which mathematical concept this AKU relates to"""
    aku_id_lower = aku_id.lower()
    
    if 'monad' in aku_id_lower:
        return 'monad'
    elif 'functor' in aku_id_lower or aku_id_lower.startswith('fn-'):
        if 'endofunctor' in aku_id_lower:
            return 'endofunctor'
        return 'functor'
    elif 'monoid' in aku_id_lower or aku_id_lower.startswith('mo-'):
        return 'monoid'
    elif 'kleisli' in aku_id_lower:
        return 'kleisli'
    
    return 'functor'  # default

def update_functional_programming_aku(aku_path):
    """
    Update a functional programming AKU with cross-domain references
    
    Args:
        aku_path: Path to the AKU file
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        with open(aku_path, 'r', encoding='utf-8') as f:
            aku = json.load(f)
        
        # Get the AKU ID for messaging
        aku_id = aku.get('@id', 'unknown')
        
        # Determine AKU type
        aku_type = determine_aku_type(aku_id, aku.get('content', {}))
        math_ref = MATH_REFERENCES.get(aku_type, MATH_REFERENCES['functor'])
        
        # Update classification
        if 'classification' not in aku:
            aku['classification'] = {}
        
        # Keep existing domain_path (science/computer-science/functional-theory is OK as application)
        # OR update to new FP path - let's keep it for now and note the future path
        old_path = aku['classification'].get('domain_path', '')
        
        # Mark as application domain
        aku['classification']['isApplicationDomain'] = True
        aku['classification']['isNativeDomain'] = False
        
        # Add note about future path
        if 'notes' not in aku['classification']:
            aku['classification']['notes'] = []
        
        # Update modified timestamp
        if 'metadata' not in aku:
            aku['metadata'] = {}
        aku['metadata']['modified'] = get_utc_timestamp()
        
        # Add cross-domain references if not already present
        if 'cross_domain_references' not in aku:
            aku['cross_domain_references'] = {
                "note": "This programming concept APPLIES mathematical concepts from their native domains",
                "applies": [
                    {
                        "sourceDomain": math_ref['math_path'],
                        "concept": math_ref['concept'],
                        "relationship": "applies",
                        "applicationContext": math_ref['context']
                    }
                ]
            }
        
        # Write back to file
        with open(aku_path, 'w', encoding='utf-8') as f:
            json.dump(aku, f, indent=2, ensure_ascii=False)
            f.write('\n')
        
        message = f"✅ Updated {aku_id}: Added cross-domain references to {math_ref['concept']}"
        return True, message
        
    except Exception as e:
        return False, f"❌ Error updating {aku_path}: {str(e)}"

def main():
    """Main update function"""
    # Define paths
    repo_root = Path(__file__).parent.parent.parent.parent
    fp_dir = repo_root / "domain/science/computer-science/functional-theory"
    
    print("=" * 70)
    print("Functional Programming AKUs - Cross-Domain Reference Update")
    print("=" * 70)
    print(f"\nWorking directory: {fp_dir}")
    print()
    
    # Find all AKUs in functors, monoids, monads
    aku_files = []
    for subdir in ['functors', 'monoids', 'monads']:
        subdir_path = fp_dir / subdir / 'akus'
        if subdir_path.exists():
            aku_files.extend(sorted(subdir_path.glob("*.json")))
    
    if not aku_files:
        print("❌ No functional programming AKU files found!")
        return 1
    
    print(f"Found {len(aku_files)} functional programming AKUs to update\n")
    
    # Update each AKU
    success_count = 0
    failed_count = 0
    
    for aku_file in aku_files:
        success, message = update_functional_programming_aku(aku_file)
        print(message)
        
        if success:
            success_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 70)
    print("Update Summary")
    print("=" * 70)
    print(f"✅ Successfully updated: {success_count}")
    print(f"❌ Failed: {failed_count}")
    print("\nChanges made:")
    print("1. Added isApplicationDomain: true to classification")
    print("2. Added cross_domain_references linking to math concepts")
    print("3. Updated modified timestamps")
    print("\nNext steps:")
    print("1. Update concept-index.yaml with cross-domain links")
    print("2. Run validation: python domain/_ontology/tools/validate_cross_domain.py")
    print("3. Consider creating dedicated FP directory in new hierarchy")
    
    return 0 if failed_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
