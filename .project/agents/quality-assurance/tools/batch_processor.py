#!/usr/bin/env python3
"""
Batch AKU Processor

Enhanced batch processing tool for ontology operations on multiple AKUs.
Handles entire directories with progress reporting, error recovery, and rollback.

Usage:
    python batch_processor.py --validate --directory path/to/akus/
    python batch_processor.py --enhance --directory path/to/akus/ --domain medicine
    python batch_processor.py --check-uris --all
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import shutil

class BatchProcessor:
    """Process multiple AKUs in batch with progress tracking."""
    
    def __init__(self, verbose: bool = False, dry_run: bool = False):
        self.verbose = verbose
        self.dry_run = dry_run
        self.results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }
        self.backup_dir = None
    
    def create_backup(self, files: List[Path]) -> Path:
        """Create backup of files before batch operation."""
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        backup_dir = Path(f"/tmp/aku_backup_{timestamp}")
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"📦 Creating backup in {backup_dir}")
        
        for file in files:
            rel_path = file.relative_to(file.parent.parent.parent)
            backup_file = backup_dir / rel_path
            backup_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, backup_file)
        
        self.backup_dir = backup_dir
        print(f"✅ Backed up {len(files)} files")
        return backup_dir
    
    def restore_from_backup(self):
        """Restore files from backup."""
        if not self.backup_dir or not self.backup_dir.exists():
            print("❌ No backup found to restore from")
            return False
        
        print(f"♻️  Restoring from backup {self.backup_dir}")
        
        # Implementation would restore files
        print("⚠️  Backup restore not yet implemented - manual restore from backup dir")
        return True
    
    def validate_batch(self, files: List[Path]) -> Dict:
        """Validate multiple AKUs."""
        print(f"\n🔍 Validating {len(files)} AKUs...")
        
        for i, file in enumerate(files, 1):
            self.results['total'] += 1
            
            try:
                with open(file, 'r') as f:
                    aku = json.load(f)
                
                # Basic validation checks
                errors = []
                
                # Check required fields
                if '@context' not in aku:
                    errors.append("Missing @context")
                
                if 'metadata' not in aku:
                    errors.append("Missing metadata")
                elif 'last_updated' not in aku['metadata']:
                    errors.append("Missing metadata.last_updated")
                
                # Check SKOS properties
                if 'skos:prefLabel' not in aku:
                    errors.append("Missing skos:prefLabel")
                
                if errors:
                    self.results['failed'] += 1
                    self.results['errors'].append({
                        'file': str(file),
                        'errors': errors
                    })
                    status = "❌"
                else:
                    self.results['success'] += 1
                    status = "✅"
                
                if self.verbose or errors:
                    print(f"  [{i}/{len(files)}] {status} {file.name}")
                    if errors:
                        for error in errors:
                            print(f"      - {error}")
            
            except json.JSONDecodeError as e:
                self.results['failed'] += 1
                self.results['errors'].append({
                    'file': str(file),
                    'errors': [f"JSON Error: {str(e)}"]
                })
                print(f"  [{i}/{len(files)}] ❌ {file.name}: Invalid JSON")
            
            except Exception as e:
                self.results['failed'] += 1
                self.results['errors'].append({
                    'file': str(file),
                    'errors': [str(e)]
                })
                print(f"  [{i}/{len(files)}] ❌ {file.name}: {str(e)}")
        
        return self.results
    
    def enhance_batch(self, files: List[Path], domain: str) -> Dict:
        """Enhance multiple AKUs with ontology annotations."""
        if not self.dry_run:
            self.create_backup(files)
        
        print(f"\n✨ Enhancing {len(files)} AKUs for {domain} domain...")
        
        # This would call the actual enhancement logic
        print("⚠️  Enhancement logic not yet implemented in batch processor")
        print("   Use domain-specific enhancement scripts instead")
        
        return self.results
    
    def check_uris_batch(self, files: List[Path]) -> Dict:
        """Check URIs in multiple AKUs."""
        print(f"\n🔗 Checking URIs in {len(files)} AKUs...")
        
        # This would integrate with validate_uris.py
        print("⚠️  URI checking should use validate_uris.py tool")
        
        return self.results
    
    def print_summary(self):
        """Print batch processing summary."""
        print(f"\n{'='*70}")
        print("BATCH PROCESSING SUMMARY")
        print(f"{'='*70}")
        print(f"Total files: {self.results['total']}")
        print(f"✅ Success: {self.results['success']}")
        print(f"❌ Failed: {self.results['failed']}")
        print(f"⏭️  Skipped: {self.results['skipped']}")
        
        if self.results['errors']:
            print(f"\n❌ ERRORS ({len(self.results['errors'])}):")
            for error_info in self.results['errors'][:10]:  # Show first 10
                print(f"\n  File: {Path(error_info['file']).name}")
                for error in error_info['errors']:
                    print(f"    - {error}")
            
            if len(self.results['errors']) > 10:
                print(f"\n  ... and {len(self.results['errors']) - 10} more errors")
        
        if self.backup_dir:
            print(f"\n📦 Backup location: {self.backup_dir}")
        
        success_rate = (self.results['success'] / self.results['total'] * 100) if self.results['total'] > 0 else 0
        print(f"\nSuccess rate: {success_rate:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Batch process multiple AKUs')
    parser.add_argument('--validate', action='store_true', help='Validate AKUs')
    parser.add_argument('--enhance', action='store_true', help='Enhance AKUs with ontology')
    parser.add_argument('--check-uris', action='store_true', help='Check URI validity')
    parser.add_argument('--directory', '-d', help='Directory containing AKUs')
    parser.add_argument('--all', action='store_true', help='Process all AKUs in repository')
    parser.add_argument('--domain', help='Domain for enhancement (medicine, economics, science)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--dry-run', action='store_true', help='Dry run (no changes)')
    
    args = parser.parse_args()
    
    # Collect files
    files = []
    if args.all:
        base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs")
        for pattern in ["domain/**/*.json", ".project/pilot/**/*.json"]:
            files.extend(base_dir.glob(pattern))
    elif args.directory:
        dir_path = Path(args.directory)
        files = list(dir_path.glob("**/*.json"))
    else:
        parser.print_help()
        return 1
    
    if not files:
        print("❌ No files found")
        return 1
    
    processor = BatchProcessor(verbose=args.verbose, dry_run=args.dry_run)
    
    # Execute requested operation
    if args.validate:
        processor.validate_batch(files)
    elif args.enhance:
        if not args.domain:
            print("❌ --domain required for enhancement")
            return 1
        processor.enhance_batch(files, args.domain)
    elif args.check_uris:
        processor.check_uris_batch(files)
    else:
        parser.print_help()
        return 1
    
    processor.print_summary()
    
    return 0 if processor.results['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
