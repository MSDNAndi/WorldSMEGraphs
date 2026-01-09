#!/usr/bin/env python3
"""
Prompt Completeness Validation
===============================

Validates that image generation prompts are complete and self-contained
according to the standards learned from PR #36, PR #38, and PR #42.

Checks for:
- Sufficient length (target 8K-20K characters)
- No placeholder text
- No external references
- Super explicit directions and specifications
- Multi-panel prompt file support (=== PANEL XX === delimiters)

Author: WorldSMEGraphs Image Generation Specialist
Version: 1.1.0
Created: 2026-01-08
Updated: 2026-01-09 (Added multi-panel prompt file validation)
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

# Import shared constants
try:
    from workflow_constants import (
        PLACEHOLDER_KEYWORDS,
        EXTERNAL_REFERENCE_PATTERNS,
        MIN_LENGTH,
        RECOMMENDED_LENGTH,
        TARGET_MIN_LENGTH,
        TARGET_MAX_LENGTH,
        EXPLICIT_INDICATORS,
        PANEL_DELIMITER_DETECT,
        PANEL_DELIMITER_SPLIT,
    )
except ImportError:
    # Fallback if constants file not available
    PLACEHOLDER_KEYWORDS = [
        "PLACEHOLDER", "TODO", "TBD", "FIXME", "XXX",
        "[insert", "[add", "[describe", "[fill in",
        "Apply STYLE BASE", "Use style from", "See style guide",
    ]
    EXTERNAL_REFERENCE_PATTERNS = [
        r"refer to\s+\w+", r"see\s+(the\s+)?style\s+guide",
        r"as described in", r"use\s+the\s+style\s+from",
    ]
    MIN_LENGTH = 1000
    RECOMMENDED_LENGTH = 5000
    TARGET_MIN_LENGTH = 8000
    TARGET_MAX_LENGTH = 20000
    EXPLICIT_INDICATORS = ["LEFT TO RIGHT", "clockwise", r"#[0-9A-Fa-f]{6}", r"\d+\s*px"]
    PANEL_DELIMITER_DETECT = r'(?:^|\n)={3,}.*PANEL\s*\d+'
    PANEL_DELIMITER_SPLIT = r'(?:^|\n)={3,}\s*PANEL\s*(\d+).*?(?:={3,})?\s*(?:\n|$)'

@dataclass
class PromptIssue:
    """An issue found in a prompt."""
    severity: str  # 'error' or 'warning'
    category: str
    message: str
    line_number: int = 0

@dataclass
class PromptValidation:
    """Results of validating a single prompt."""
    filename: str
    length: int
    passed: bool
    errors: List[PromptIssue]
    warnings: List[PromptIssue]
    score: float  # 0-100 quality score

def validate_prompt_length(content: str) -> Tuple[List[PromptIssue], List[PromptIssue]]:
    """Validate prompt length against standards."""
    errors = []
    warnings = []
    length = len(content)
    
    if length < MIN_LENGTH:
        errors.append(PromptIssue(
            severity='error',
            category='length',
            message=f"Prompt too short: {length} characters (minimum: {MIN_LENGTH})"
        ))
    elif length < RECOMMENDED_LENGTH:
        warnings.append(PromptIssue(
            severity='warning',
            category='length',
            message=f"Prompt shorter than recommended: {length} chars (recommend: {RECOMMENDED_LENGTH}+)"
        ))
    elif length < TARGET_MIN_LENGTH:
        warnings.append(PromptIssue(
            severity='warning',
            category='length',
            message=f"Prompt below target: {length} chars (target: {TARGET_MIN_LENGTH}-{TARGET_MAX_LENGTH})"
        ))
    
    if length > TARGET_MAX_LENGTH * 1.5:
        warnings.append(PromptIssue(
            severity='warning',
            category='length',
            message=f"Prompt very long: {length} chars (may be overly detailed)"
        ))
    
    return errors, warnings

def validate_no_placeholders(content: str) -> List[PromptIssue]:
    """Check for placeholder text that indicates incomplete prompts."""
    errors = []
    
    for keyword in PLACEHOLDER_KEYWORDS:
        # Case-insensitive search
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = list(pattern.finditer(content))
        
        for match in matches:
            # Find line number
            line_num = content[:match.start()].count('\n') + 1
            errors.append(PromptIssue(
                severity='error',
                category='placeholder',
                message=f"Contains placeholder '{keyword}' - prompt must be complete",
                line_number=line_num
            ))
    
    return errors

def validate_no_external_references(content: str) -> List[PromptIssue]:
    """Check for external references that make prompts not self-contained."""
    warnings = []
    
    for pattern_str in EXTERNAL_REFERENCE_PATTERNS:
        pattern = re.compile(pattern_str, re.IGNORECASE)
        matches = list(pattern.finditer(content))
        
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            warnings.append(PromptIssue(
                severity='warning',
                category='external_reference',
                message=f"Possible external reference: '{match.group()}' - prompts should be self-contained",
                line_number=line_num
            ))
    
    return warnings

def validate_explicit_detail(content: str) -> Tuple[List[PromptIssue], int]:
    """Check for super explicit directions and specifications."""
    warnings = []
    score = 0
    
    # Count explicit indicators
    for indicator in EXPLICIT_INDICATORS:
        if isinstance(indicator, str) and indicator.isupper():
            # Exact match for uppercase indicators
            if indicator in content:
                score += 10
        else:
            # Regex pattern
            pattern = re.compile(indicator, re.IGNORECASE)
            matches = len(list(pattern.finditer(content)))
            score += min(matches * 5, 20)  # Cap per indicator
    
    # Check for color specifications
    hex_colors = re.findall(r"#[0-9A-Fa-f]{6}", content)
    if len(hex_colors) >= 3:
        score += 15
    elif len(hex_colors) >= 1:
        score += 5
    else:
        warnings.append(PromptIssue(
            severity='warning',
            category='explicit_detail',
            message="No hex color codes found - specify exact colors (e.g., #3498DB)"
        ))
    
    # Check for measurements
    pixel_measures = len(re.findall(r"\d+\s*px", content))
    if pixel_measures >= 5:
        score += 10
    elif pixel_measures >= 1:
        score += 5
    else:
        warnings.append(PromptIssue(
            severity='warning',
            category='explicit_detail',
            message="Few pixel measurements found - be more explicit about sizes"
        ))
    
    # Check for directional language
    directional_terms = [
        "left to right", "right to left", "top to bottom", "bottom to top",
        "clockwise", "counterclockwise", "flowing", "pointing"
    ]
    direction_count = sum(1 for term in directional_terms if term.lower() in content.lower())
    if direction_count >= 3:
        score += 15
    elif direction_count >= 1:
        score += 5
    else:
        warnings.append(PromptIssue(
            severity='warning',
            category='explicit_detail',
            message="Few directional specifications - be super explicit about orientations"
        ))
    
    # Cap score at 100
    score = min(score, 100)
    
    return warnings, score

def validate_sections(content: str) -> List[PromptIssue]:
    """Check for recommended prompt structure with sections."""
    warnings = []
    
    recommended_sections = [
        ("SCENE", ["scene", "composition", "layout"]),
        ("STYLE", ["style", "visual style", "art style"]),
        ("COLOR", ["color", "palette", "colors"]),
        ("CONSTRAINTS", ["constraint", "no text", "no people"]),
    ]
    
    content_lower = content.lower()
    
    for section_name, keywords in recommended_sections:
        if not any(keyword in content_lower for keyword in keywords):
            warnings.append(PromptIssue(
                severity='warning',
                category='structure',
                message=f"Missing {section_name} section - consider adding explicit section"
            ))
    
    return warnings

def parse_multi_panel_prompts(content: str) -> List[Tuple[int, str]]:
    """
    Parse a multi-panel prompt file using === PANEL XX === delimiters.
    Returns list of (panel_number, prompt_content) tuples.
    
    Added in v1.1.0 (PR #42) to properly validate multi-panel prompt files.
    Uses shared constants from workflow_constants.py.
    """
    # Check for panel delimiters using shared constant
    if not re.search(PANEL_DELIMITER_DETECT, content, re.IGNORECASE):
        return []  # Not a multi-panel file
    
    # Split on panel delimiters using shared constant
    sections = re.split(PANEL_DELIMITER_SPLIT, content, flags=re.IGNORECASE)
    
    # Process pairs of (panel_number, content)
    panels = []
    for i in range(1, len(sections) - 1, 2):
        panel_num_str = sections[i]
        prompt_text = sections[i + 1].strip() if i + 1 < len(sections) else ""
        
        if panel_num_str and prompt_text:
            panel_num = int(panel_num_str)
            panels.append((panel_num, prompt_text))
    
    return panels

def validate_multi_panel_file(filepath: Path) -> List[PromptValidation]:
    """
    Validate a multi-panel prompt file.
    Returns a list of PromptValidation results, one per panel.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [PromptValidation(
            filename=filepath.name,
            length=0,
            passed=False,
            errors=[PromptIssue('error', 'file', f"Cannot read file: {e}")],
            warnings=[],
            score=0
        )]
    
    panels = parse_multi_panel_prompts(content)
    
    if not panels:
        # Not a multi-panel file, return empty list
        return []
    
    results = []
    for panel_num, prompt_text in panels:
        errors = []
        warnings = []
        
        # Validate length
        length_errors, length_warnings = validate_prompt_length(prompt_text)
        errors.extend(length_errors)
        warnings.extend(length_warnings)
        
        # Check for placeholders
        placeholder_errors = validate_no_placeholders(prompt_text)
        errors.extend(placeholder_errors)
        
        # Check for external references
        external_warnings = validate_no_external_references(prompt_text)
        warnings.extend(external_warnings)
        
        # Check for explicit detail
        detail_warnings, explicitness_score = validate_explicit_detail(prompt_text)
        warnings.extend(detail_warnings)
        
        # Check for recommended structure
        structure_warnings = validate_sections(prompt_text)
        warnings.extend(structure_warnings)
        
        # Calculate overall score
        length_score = min(len(prompt_text) / TARGET_MIN_LENGTH * 50, 50)
        quality_score = (explicitness_score / 100) * 50
        total_score = length_score + quality_score
        
        # Deduct for errors
        total_score -= len(errors) * 10
        total_score = max(0, min(100, total_score))
        
        passed = len(errors) == 0
        
        results.append(PromptValidation(
            filename=f"{filepath.name} → Panel {panel_num:02d}",
            length=len(prompt_text),
            passed=passed,
            errors=errors,
            warnings=warnings,
            score=total_score
        ))
    
    return results

def validate_prompt_file(filepath: Path) -> PromptValidation:
    """Validate a single prompt file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return PromptValidation(
            filename=filepath.name,
            length=0,
            passed=False,
            errors=[PromptIssue('error', 'file', f"Cannot read file: {e}")],
            warnings=[],
            score=0
        )
    
    errors = []
    warnings = []
    
    # Validate length
    length_errors, length_warnings = validate_prompt_length(content)
    errors.extend(length_errors)
    warnings.extend(length_warnings)
    
    # Check for placeholders
    placeholder_errors = validate_no_placeholders(content)
    errors.extend(placeholder_errors)
    
    # Check for external references
    external_warnings = validate_no_external_references(content)
    warnings.extend(external_warnings)
    
    # Check for explicit detail
    detail_warnings, explicitness_score = validate_explicit_detail(content)
    warnings.extend(detail_warnings)
    
    # Check for recommended structure
    structure_warnings = validate_sections(content)
    warnings.extend(structure_warnings)
    
    # Calculate overall score
    length_score = min(len(content) / TARGET_MIN_LENGTH * 50, 50)
    quality_score = (explicitness_score / 100) * 50
    total_score = length_score + quality_score
    
    # Deduct for errors
    total_score -= len(errors) * 10
    total_score = max(0, min(100, total_score))
    
    passed = len(errors) == 0
    
    return PromptValidation(
        filename=filepath.name,
        length=len(content),
        passed=passed,
        errors=errors,
        warnings=warnings,
        score=total_score
    )

def print_validation_result(result: PromptValidation, verbose: bool = False):
    """Print validation result for a single prompt."""
    status = "✅ PASS" if result.passed else "❌ FAIL"
    score_emoji = "🟢" if result.score >= 80 else "🟡" if result.score >= 60 else "🔴"
    
    print(f"\n{status} {score_emoji} {result.filename}")
    print(f"  Length: {result.length:,} characters")
    print(f"  Quality Score: {result.score:.0f}/100")
    
    if result.errors:
        print(f"\n  Errors ({len(result.errors)}):")
        for error in result.errors:
            line_info = f" (line {error.line_number})" if error.line_number else ""
            print(f"    ❌ [{error.category}]{line_info} {error.message}")
    
    if verbose and result.warnings:
        print(f"\n  Warnings ({len(result.warnings)}):")
        for warning in result.warnings[:5]:  # Limit to first 5
            line_info = f" (line {warning.line_number})" if warning.line_number else ""
            print(f"    ⚠️  [{warning.category}]{line_info} {warning.message}")
        if len(result.warnings) > 5:
            print(f"    ... and {len(result.warnings) - 5} more warnings")

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate image generation prompt completeness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Prompt Quality Standards (from PR #36 and PR #38):
- Length: 8,000-20,000 characters (target)
- No placeholders or external references
- Super explicit directions (LEFT TO RIGHT, hex colors, pixel sizes)
- Self-contained complete descriptions

Examples:
  # Validate single prompt
  python validate_prompts.py prompts/slide-01.txt
  
  # Validate all prompts in directory
  python validate_prompts.py prompts/
  
  # Verbose output with all warnings
  python validate_prompts.py prompts/ --verbose
  
  # Validate prompt file pattern
  python validate_prompts.py gpt-prompts*.txt
        """
    )
    
    parser.add_argument(
        "paths",
        nargs="+",
        help="Prompt file(s) or directory to validate"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show all warnings"
    )
    
    parser.add_argument(
        "--min-score",
        type=float,
        default=60.0,
        help="Minimum quality score to pass (0-100, default: 60)"
    )
    
    args = parser.parse_args()
    
    # Collect all prompt files
    prompt_files = []
    for path_str in args.paths:
        path = Path(path_str)
        if path.is_file():
            prompt_files.append(path)
        elif path.is_dir():
            prompt_files.extend(path.glob("*.txt"))
        else:
            print(f"⚠️  Warning: {path} does not exist", file=sys.stderr)
    
    if not prompt_files:
        print("❌ No prompt files found", file=sys.stderr)
        sys.exit(1)
    
    print("="*70)
    print(f"VALIDATING {len(prompt_files)} PROMPT FILE(S)")
    print("="*70)
    
    results = []
    for prompt_file in sorted(prompt_files):
        # First, check if it's a multi-panel file
        multi_panel_results = validate_multi_panel_file(prompt_file)
        
        if multi_panel_results:
            # Multi-panel file: validate each panel separately
            print(f"\n📁 Multi-panel file detected: {prompt_file.name} ({len(multi_panel_results)} panels)")
            for result in multi_panel_results:
                results.append(result)
                print_validation_result(result, args.verbose)
        else:
            # Single prompt file
            result = validate_prompt_file(prompt_file)
            results.append(result)
            print_validation_result(result, args.verbose)
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]
    low_score = [r for r in results if r.score < args.min_score]
    
    avg_length = sum(r.length for r in results) / len(results)
    avg_score = sum(r.score for r in results) / len(results)
    
    print(f"\nTotal files: {len(results)}")
    print(f"Passed: {len(passed)} ✅")
    print(f"Failed: {len(failed)} ❌")
    print(f"Below min score ({args.min_score}): {len(low_score)} 🔴")
    print(f"\nAverage length: {avg_length:,.0f} characters")
    print(f"Average quality score: {avg_score:.0f}/100")
    
    if failed:
        print("\n❌ FAILED FILES:")
        for result in failed:
            print(f"  - {result.filename} ({len(result.errors)} errors)")
    
    if low_score:
        print(f"\n🔴 LOW QUALITY SCORES (<{args.min_score}):")
        for result in low_score:
            print(f"  - {result.filename} (score: {result.score:.0f})")
    
    print("\n" + "="*70)
    
    if failed or low_score:
        print("\n❌ VALIDATION FAILED")
        print("\nImprove prompts by:")
        print("  1. Adding more explicit detail (directions, colors, sizes)")
        print("  2. Removing placeholders and external references")
        print("  3. Increasing length with complete descriptions")
        print("  4. Using structured sections (SCENE, STYLE, COLOR, CONSTRAINTS)")
        print("\nSee: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md")
    else:
        print("\n✅ ALL PROMPTS VALIDATED")
        print("\nPrompts are:")
        print("  ✅ Complete and self-contained")
        print("  ✅ Super explicit with details")
        print("  ✅ Ready for image generation")
    
    print("="*70 + "\n")
    
    sys.exit(0 if (not failed and not low_score) else 1)

if __name__ == "__main__":
    main()
