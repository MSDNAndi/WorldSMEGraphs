#!/usr/bin/env python3
"""
Workflow Phase Order Validation
================================

Validates that content generation follows the correct workflow order:
1. Storyboard exists (Phase 1-2)
2. Complete prompts exist (Phase 3)
3. Images generated (Phase 4)
4. Final documents only created after images (Phase 5)

This ensures the proper order learned from PR #36 and PR #38:
- Storyboard → Prompts → Images → Documents

Author: WorldSMEGraphs Image Generation Specialist
Version: 1.0.0
Created: 2026-01-08
"""

import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Result of workflow validation."""
    phase: str
    passed: bool
    errors: List[str]
    warnings: List[str]

def validate_phase_1_2_storyboard(content_dir: Path) -> ValidationResult:
    """Validate Phase 1-2: Storyboard existence and completeness."""
    errors = []
    warnings = []
    
    # Check for storyboard file (multiple formats acceptable)
    storyboard_files = [
        content_dir / "storyboard.yaml",
        content_dir / "storyboard.json",
        content_dir / "storyboard.md",
        content_dir / "comic-storyboard.md",
        content_dir / "presentation-storyboard.yaml"
    ]
    
    storyboard_exists = any(f.exists() for f in storyboard_files)
    
    if not storyboard_exists:
        errors.append(
            "No storyboard file found. Expected one of:\n"
            "  - storyboard.yaml/json/md\n"
            "  - comic-storyboard.md\n"
            "  - presentation-storyboard.yaml"
        )
    else:
        # Found storyboard, check it's not empty
        for f in storyboard_files:
            if f.exists():
                size = f.stat().st_size
                if size < 100:
                    warnings.append(f"Storyboard {f.name} seems very small ({size} bytes)")
                break
    
    passed = len(errors) == 0
    return ValidationResult("Phase 1-2: Storyboard", passed, errors, warnings)

def validate_phase_3_prompts(content_dir: Path) -> ValidationResult:
    """Validate Phase 3: Complete prompts without placeholders."""
    errors = []
    warnings = []
    
    # Check for prompts directory or prompt files
    prompts_dir = content_dir / "prompts"
    prompt_files = list(content_dir.glob("*prompts*.txt"))
    
    if not prompts_dir.exists() and not prompt_files:
        errors.append(
            "No prompts directory or prompt files found.\n"
            "Expected: prompts/ directory or files like gpt-prompts.txt"
        )
        return ValidationResult("Phase 3: Prompts", False, errors, warnings)
    
    # Check prompts if they exist
    all_prompts = []
    if prompts_dir.exists():
        all_prompts.extend(prompts_dir.glob("*.txt"))
    all_prompts.extend(prompt_files)
    
    if not all_prompts:
        errors.append("Prompts directory/files exist but no .txt files found")
    
    # Validate each prompt
    placeholder_keywords = [
        "PLACEHOLDER", "TODO", "TBD", "FIXME",
        "Apply STYLE BASE", "[insert", "[add", "[describe"
    ]
    
    for prompt_file in all_prompts:
        try:
            content = prompt_file.read_text(encoding='utf-8')
            
            # Check length (should be substantial)
            if len(content) < 1000:
                warnings.append(
                    f"{prompt_file.name}: Only {len(content)} characters "
                    f"(recommend 5K+, target 8K-20K)"
                )
            
            # Check for placeholders
            for keyword in placeholder_keywords:
                if keyword.lower() in content.lower():
                    errors.append(
                        f"{prompt_file.name}: Contains placeholder '{keyword}'\n"
                        f"  Prompts must be complete and self-contained"
                    )
                    break
            
            # Check for external references
            external_refs = [
                "see style guide", "refer to", "as described in",
                "use the style from", "apply the style"
            ]
            for ref in external_refs:
                if ref.lower() in content.lower():
                    warnings.append(
                        f"{prompt_file.name}: May contain external reference '{ref}'\n"
                        f"  Prompts should be self-contained"
                    )
                    break
                    
        except Exception as e:
            errors.append(f"{prompt_file.name}: Error reading file: {e}")
    
    passed = len(errors) == 0
    return ValidationResult("Phase 3: Prompts", passed, errors, warnings)

def validate_phase_4_images(content_dir: Path) -> ValidationResult:
    """Validate Phase 4: Images generated and present."""
    errors = []
    warnings = []
    
    # Check for images directory
    images_dir = content_dir / "images"
    if not images_dir.exists():
        # Also check for panels-gpt, panels-gpt-v2 (comic naming)
        alt_dirs = [
            content_dir / "panels-gpt",
            content_dir / "panels-gpt-v2"
        ]
        if any(d.exists() for d in alt_dirs):
            images_dir = next(d for d in alt_dirs if d.exists())
        else:
            errors.append(
                "No images directory found.\n"
                "Expected: images/ or panels-gpt/ or panels-gpt-v2/"
            )
            return ValidationResult("Phase 4: Images", False, errors, warnings)
    
    # Check for image files
    image_files = list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg"))
    
    if not image_files:
        errors.append(f"Images directory exists but no image files found in {images_dir}")
    else:
        # Check for metadata files
        metadata_files = list(images_dir.glob("metadata_*.json"))
        if len(metadata_files) < len(image_files) * 0.5:
            warnings.append(
                f"Only {len(metadata_files)} metadata files for {len(image_files)} images.\n"
                f"  Recommend creating metadata for all images"
            )
    
    passed = len(errors) == 0
    return ValidationResult("Phase 4: Images", passed, errors, warnings)

def validate_phase_5_documents(content_dir: Path, images_exist: bool) -> ValidationResult:
    """Validate Phase 5: Documents created only after images exist."""
    errors = []
    warnings = []
    
    # Check for final document files
    doc_files = (
        list(content_dir.glob("*.pptx")) +
        list(content_dir.glob("*.pdf")) +
        list(content_dir.glob("*.html"))
    )
    
    if doc_files and not images_exist:
        errors.append(
            f"Found {len(doc_files)} final document(s) but no images.\n"
            f"Documents:\n" +
            "\n".join(f"  - {d.name}" for d in doc_files[:5]) +
            "\n\n❌ CRITICAL VIOLATION: You MUST generate images (Phase 4) "
            "BEFORE creating documents (Phase 5).\n"
            "See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
        )
    
    if doc_files and images_exist:
        # Documents exist with images - this is correct
        pass
    
    passed = len(errors) == 0
    return ValidationResult("Phase 5: Documents", passed, errors, warnings)

def validate_archive_structure(content_dir: Path) -> ValidationResult:
    """Validate Phase 6: Archive structure for previous versions."""
    errors = []
    warnings = []
    
    archive_dir = content_dir / "archive"
    
    if not archive_dir.exists():
        # Archive is optional if this is first version
        warnings.append(
            "No archive/ directory found.\n"
            "  Create archive/ before replacing with new versions"
        )
    else:
        # Check archive structure
        archive_folders = [d for d in archive_dir.iterdir() if d.is_dir()]
        
        if not archive_folders:
            warnings.append("archive/ directory exists but is empty")
        else:
            # Check each archive has README
            for folder in archive_folders:
                readme = folder / "README.md"
                if not readme.exists():
                    warnings.append(
                        f"Archive {folder.name} missing README.md\n"
                        f"  Document what changed and why it was archived"
                    )
    
    passed = len(errors) == 0
    return ValidationResult("Phase 6: Archive", passed, errors, warnings)

def validate_workflow(content_dir: Path, verbose: bool = False) -> Tuple[bool, List[ValidationResult]]:
    """
    Validate complete workflow order for a content directory.
    
    Args:
        content_dir: Path to content directory to validate
        verbose: Show detailed output
        
    Returns:
        (all_passed, results): Overall pass/fail and detailed results
    """
    results = []
    
    # Phase 1-2: Storyboard
    result_12 = validate_phase_1_2_storyboard(content_dir)
    results.append(result_12)
    
    # Phase 3: Prompts
    result_3 = validate_phase_3_prompts(content_dir)
    results.append(result_3)
    
    # Phase 4: Images
    result_4 = validate_phase_4_images(content_dir)
    results.append(result_4)
    
    # Phase 5: Documents (check against Phase 4)
    result_5 = validate_phase_5_documents(content_dir, result_4.passed)
    results.append(result_5)
    
    # Phase 6: Archive
    result_6 = validate_archive_structure(content_dir)
    results.append(result_6)
    
    all_passed = all(r.passed for r in results)
    
    return all_passed, results

def print_results(results: List[ValidationResult], verbose: bool = False):
    """Print validation results in human-readable format."""
    print("\n" + "="*70)
    print("WORKFLOW VALIDATION RESULTS")
    print("="*70)
    
    for result in results:
        status = "✅ PASS" if result.passed else "❌ FAIL"
        print(f"\n{status} - {result.phase}")
        
        if result.errors:
            print("\n  Errors:")
            for error in result.errors:
                print(f"    ❌ {error}")
        
        if verbose and result.warnings:
            print("\n  Warnings:")
            for warning in result.warnings:
                print(f"    ⚠️  {warning}")
    
    print("\n" + "="*70)
    
    all_passed = all(r.passed for r in results)
    if all_passed:
        print("✅ WORKFLOW ORDER IS CORRECT")
        print("\nAll phases completed in proper order:")
        print("  1-2. Storyboard created")
        print("  3. Complete prompts written")
        print("  4. Images generated")
        print("  5. Documents created (after images)")
        print("  6. Archive structure ready")
    else:
        print("❌ WORKFLOW VIOLATIONS FOUND")
        print("\nCorrect order:")
        print("  1-2. Create storyboard (content planning)")
        print("  3. Write complete prompts (no placeholders)")
        print("  4. Generate images using prompts")
        print("  5. Create final documents referencing images")
        print("  6. Archive previous versions before replacing")
        print("\nSee: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md")
    
    print("="*70 + "\n")

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate workflow phase order for content generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate current directory
  python validate_workflow.py
  
  # Validate specific content directory
  python validate_workflow.py renders/by-domain/.../presentations/
  
  # Verbose output with warnings
  python validate_workflow.py --verbose
  
  # Check multiple directories
  find renders/ -name "comic" -type d -exec python validate_workflow.py {} \\;
        """
    )
    
    parser.add_argument(
        "content_dir",
        nargs="?",
        default=".",
        help="Content directory to validate (default: current directory)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show warnings in addition to errors"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    
    args = parser.parse_args()
    
    content_dir = Path(args.content_dir).resolve()
    
    if not content_dir.exists():
        print(f"❌ ERROR: Directory does not exist: {content_dir}", file=sys.stderr)
        sys.exit(1)
    
    if not content_dir.is_dir():
        print(f"❌ ERROR: Not a directory: {content_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Validating workflow order: {content_dir}")
    
    all_passed, results = validate_workflow(content_dir, args.verbose)
    
    if args.json:
        # Output JSON for programmatic use
        output = {
            "content_dir": str(content_dir),
            "all_passed": all_passed,
            "results": [
                {
                    "phase": r.phase,
                    "passed": r.passed,
                    "errors": r.errors,
                    "warnings": r.warnings
                }
                for r in results
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        # Human-readable output
        print_results(results, args.verbose)
    
    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
