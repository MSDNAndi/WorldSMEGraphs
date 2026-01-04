#!/usr/bin/env python3
"""
General-Purpose Domain Migration Script

This script migrates AKUs from legacy domain paths to the new global hierarchy.

Usage:
    python migrate_domain.py --source science/physics --target natural-sciences/physics
    python migrate_domain.py --source economics --target social-sciences/economics
    python migrate_domain.py --source medicine --target health-sciences/medicine
"""

import json
import sys
import os
import argparse
from pathlib import Path
from datetime import datetime, timezone
import shutil

def get_utc_timestamp():
    """Get current UTC timestamp in ISO 8601 format with milliseconds"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def migrate_aku(aku_path, old_domain_path, new_domain_path):
    """
    Migrate a single AKU from old to new domain path
    
    Args:
        aku_path: Path to the AKU file
        old_domain_path: Old domain path (e.g., "science/physics")
        new_domain_path: New domain path (e.g., "natural-sciences/physics")
        
    Returns:
        tuple: (success: bool, message: str, updated_aku: dict or None)
    """
    try:
        with open(aku_path, 'r', encoding='utf-8') as f:
            aku = json.load(f)
        
        # Get the AKU ID for messaging
        aku_id = aku.get('@id', 'unknown')
        
        # Update classification.domain_path if it contains old path
        if 'classification' in aku and 'domain_path' in aku['classification']:
            current_path = aku['classification']['domain_path']
            
            # Replace old domain path with new domain path
            if current_path.startswith(old_domain_path):
                # Preserve any subdirectory structure after the base path
                remainder = current_path[len(old_domain_path):].lstrip('/')
                new_full_path = new_domain_path
                if remainder:
                    new_full_path = f"{new_domain_path}/{remainder}"
                
                aku['classification']['domain_path'] = new_full_path
                
                # Mark as native domain (these are being migrated to their proper home)
                if 'isNativeDomain' not in aku['classification']:
                    aku['classification']['isNativeDomain'] = True
                
                # Update modified timestamp
                if 'metadata' not in aku:
                    aku['metadata'] = {}
                aku['metadata']['modified'] = get_utc_timestamp()
                
                message = f"✅ Migrated {aku_id}: {current_path} -> {new_full_path}"
                return True, message, aku
            else:
                message = f"⚠️  Skipped {aku_id}: path doesn't match source ({current_path})"
                return True, message, None
        else:
            message = f"⚠️  Skipped {aku_id}: no classification.domain_path"
            return True, message, None
        
    except Exception as e:
        return False, f"❌ Error migrating {aku_path}: {str(e)}", None

def main():
    """Main migration function"""
    parser = argparse.ArgumentParser(
        description='Migrate domain AKUs to new global hierarchy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Migrate physics
  python migrate_domain.py --source science/physics --target natural-sciences/physics
  
  # Migrate economics
  python migrate_domain.py --source economics --target social-sciences/economics
  
  # Migrate medicine
  python migrate_domain.py --source medicine --target health-sciences/medicine
  
  # Dry run (don't write files)
  python migrate_domain.py --source science/physics --target natural-sciences/physics --dry-run
        """
    )
    parser.add_argument('--source', required=True, help='Source domain path (e.g., science/physics)')
    parser.add_argument('--target', required=True, help='Target domain path (e.g., natural-sciences/physics)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing files')
    
    args = parser.parse_args()
    
    # Define paths
    repo_root = Path(__file__).parent.parent.parent.parent
    source_dir = repo_root / "domain" / args.source
    target_dir = repo_root / "domain" / args.target
    
    print("=" * 70)
    print("Domain Migration Script")
    print("=" * 70)
    print(f"\nSource: {source_dir}")
    print(f"Target: {target_dir}")
    print(f"Mode: {'DRY RUN (no files written)' if args.dry_run else 'LIVE (files will be written)'}")
    print()
    
    # Check source exists
    if not source_dir.exists():
        print(f"❌ Source directory does not exist: {source_dir}")
        return 1
    
    # Ensure target directory exists (in non-dry-run mode)
    if not args.dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files (AKUs) in source
    aku_files = list(source_dir.rglob("*.json"))
    
    if not aku_files:
        print("❌ No AKU files found in source directory!")
        return 1
    
    print(f"Found {len(aku_files)} AKU files to process\n")
    
    # Track statistics
    success_count = 0
    skipped_count = 0
    failed_count = 0
    migrated_files = []
    
    # Process each AKU
    for aku_file in aku_files:
        success, message, updated_aku = migrate_aku(aku_file, args.source, args.target)
        print(message)
        
        if success and updated_aku:
            # Calculate relative path from source
            rel_path = aku_file.relative_to(source_dir)
            new_file = target_dir / rel_path
            
            if not args.dry_run:
                # Ensure parent directory exists
                new_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Write to new location
                with open(new_file, 'w', encoding='utf-8') as f:
                    json.dump(updated_aku, f, indent=2, ensure_ascii=False)
                    f.write('\n')
            
            migrated_files.append((aku_file, new_file))
            success_count += 1
        elif success and not updated_aku:
            skipped_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 70)
    print("Migration Summary")
    print("=" * 70)
    print(f"✅ Successfully migrated: {success_count}")
    print(f"⚠️  Skipped (no changes needed): {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    
    if args.dry_run:
        print("\n⚠️  DRY RUN MODE - No files were actually written")
        print("Run without --dry-run to perform actual migration")
    else:
        print(f"\n📁 New location: {target_dir}")
        print("\nNext steps:")
        print("1. Review migrated AKUs in new location")
        print("2. Run validation: python domain/_ontology/tools/validate_cross_domain.py --directory <target>")
        print("3. Copy/move other files (README, concept-index.yaml, etc.) if needed")
        print("4. Update cross-references in other AKUs")
        print("5. Delete old source directory after verification")
    
    return 0 if failed_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
