#!/usr/bin/env python3
"""
AKU Atomicity Analyzer

Analyzes Atomic Knowledge Units (AKUs) to detect atomicity violations.
Identifies over-bundled AKUs (multiple concepts) and under-specified fragments.

Usage:
    python analyze_atomicity.py path/to/aku.json
    python analyze_atomicity.py --directory path/to/akus/
    python analyze_atomicity.py --domain economics/finance/npv

Self-contained with standard library only.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re


class AtomicityAnalyzer:
    """Analyzes AKU atomicity and identifies granularity issues."""
    
    # Indicators of multiple concepts (over-bundling)
    OVER_BUNDLED_INDICATORS = [
        "definition",
        "formula",
        "example",
        "advantages",
        "limitations",
        "applications",
        "procedure",
        "symptoms",
        "diagnosis",
        "treatment",
        "theorem",
        "proof",
        "derivation"
    ]
    
    # Indicators of under-specification (too small)
    UNDER_SPECIFIED_INDICATORS = [
        "symbol",
        "notation",
        "unit",
        "abbreviation",
        "acronym"
    ]
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.issues = []
        
    def analyze_aku(self, aku_path: Path) -> Dict:
        """Analyze a single AKU for atomicity."""
        self.issues = []
        
        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Analyzing Atomicity: {aku_path.name}")
            print(f"{'='*60}")
        
        # Load AKU
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except Exception as e:
            return {
                "status": "error",
                "error": f"Failed to load AKU: {e}",
                "file": str(aku_path)
            }
        
        # Analyze structure
        concept_count = self._count_concepts(aku)
        is_fragment = self._is_fragment(aku)
        
        # Determine atomicity status
        if concept_count > 1:
            status = "over_bundled"
            recommendation = "SPLIT"
            rationale = f"Contains {concept_count} distinct concepts - should be split into atomic units"
        elif is_fragment:
            status = "under_specified"
            recommendation = "MERGE"
            rationale = "Fragment too small to be independently useful - consider merging with related content"
        elif concept_count == 1:
            status = "atomic"
            recommendation = "KEEP"
            rationale = "Appears to contain exactly one concept - atomicity looks good"
        else:
            status = "unclear"
            recommendation = "REVIEW"
            rationale = "Unable to clearly determine concept count - manual review recommended"
        
        # Extract detected concepts
        concepts = self._extract_concepts(aku)
        
        # Calculate atomicity score (1.0 = perfectly atomic)
        atomicity_score = self._calculate_atomicity_score(concept_count, is_fragment)
        
        report = {
            "file": str(aku_path),
            "aku_id": aku.get("@id", "unknown"),
            "status": status,
            "concept_count": concept_count,
            "is_fragment": is_fragment,
            "atomicity_score": atomicity_score,
            "recommendation": recommendation,
            "rationale": rationale,
            "detected_concepts": concepts,
            "content_keys": list(aku.get("content", {}).keys()) if "content" in aku else [],
        }
        
        if self.verbose:
            self._print_report(report)
        
        return report
    
    def _count_concepts(self, aku: Dict) -> int:
        """Count distinct concepts in the AKU."""
        content = aku.get("content", {})
        if not content:
            return 0
        
        concept_indicators = 0
        
        # Check for multiple major sections
        for indicator in self.OVER_BUNDLED_INDICATORS:
            if indicator in content:
                concept_indicators += 1
        
        # Special cases that suggest multiple concepts
        if "definition" in content and "formula" in content:
            # Definition + formula might be two concepts
            concept_indicators += 1
        
        if "example_calculation" in content or "worked_example" in content:
            # Worked examples are often separate concepts
            concept_indicators += 1
        
        # Count decision rules, procedures, etc.
        if "decision_rule" in content:
            concept_indicators += 1
        
        if "procedure" in content or "steps" in content:
            concept_indicators += 1
        
        # If very few indicators, likely one concept
        if concept_indicators <= 1:
            return 1
        
        # If many indicators, likely over-bundled
        return concept_indicators
    
    def _is_fragment(self, aku: Dict) -> bool:
        """Check if AKU is an under-specified fragment."""
        content = aku.get("content", {})
        if not content:
            return True
        
        # Check for fragment indicators in content keys
        content_keys = list(content.keys())
        fragment_count = sum(1 for indicator in self.UNDER_SPECIFIED_INDICATORS 
                           if any(indicator in key.lower() for key in content_keys))
        
        # Check content size
        content_str = json.dumps(content)
        if len(content_str) < 200:  # Very small content
            return True
        
        # If primarily notation/symbols, likely a fragment
        if fragment_count > 0 and len(content_keys) <= 2:
            return True
        
        return False
    
    def _extract_concepts(self, aku: Dict) -> List[Dict]:
        """Extract detected concepts from the AKU."""
        content = aku.get("content", {})
        concepts = []
        
        for key, value in content.items():
            # Check if this is a major concept section
            if key in self.OVER_BUNDLED_INDICATORS:
                concepts.append({
                    "name": key.replace("_", " ").title(),
                    "type": key,
                    "size_estimate": len(json.dumps(value))
                })
        
        return concepts
    
    def _calculate_atomicity_score(self, concept_count: int, is_fragment: bool) -> float:
        """Calculate atomicity score (1.0 = perfectly atomic)."""
        if is_fragment:
            return 0.3  # Under-specified
        
        if concept_count == 1:
            return 1.0  # Perfect atomicity
        elif concept_count == 2:
            return 0.7  # Slightly over-bundled
        elif concept_count <= 4:
            return 0.5  # Moderately over-bundled
        else:
            return 0.3  # Severely over-bundled
    
    def _print_report(self, report: Dict):
        """Print atomicity analysis report."""
        print(f"\nStatus: {report['status'].upper()}")
        print(f"Recommendation: {report['recommendation']}")
        print(f"Atomicity Score: {report['atomicity_score']:.2f} / 1.0")
        print(f"Concept Count: {report['concept_count']}")
        print(f"Is Fragment: {report['is_fragment']}")
        print(f"\nRationale: {report['rationale']}")
        
        if report['detected_concepts']:
            print(f"\nDetected Concepts:")
            for i, concept in enumerate(report['detected_concepts'], 1):
                print(f"  {i}. {concept['name']} ({concept['size_estimate']} bytes)")
        
        print(f"\nContent Keys: {', '.join(report['content_keys'])}")
    
    def analyze_directory(self, directory: Path) -> List[Dict]:
        """Analyze all AKUs in a directory."""
        aku_files = list(directory.glob("**/*.json"))
        # Filter out schema files
        aku_files = [f for f in aku_files if "schema" not in f.name.lower()]
        
        print(f"\nAnalyzing {len(aku_files)} AKUs in {directory}")
        print(f"{'='*60}\n")
        
        reports = []
        for aku_file in aku_files:
            report = self.analyze_aku(aku_file)
            reports.append(report)
        
        # Summary
        self._print_summary(reports)
        
        return reports
    
    def _print_summary(self, reports: List[Dict]):
        """Print summary of atomicity analysis."""
        total = len(reports)
        atomic = sum(1 for r in reports if r['status'] == 'atomic')
        over_bundled = sum(1 for r in reports if r['status'] == 'over_bundled')
        under_specified = sum(1 for r in reports if r['status'] == 'under_specified')
        unclear = sum(1 for r in reports if r['status'] == 'unclear')
        errors = sum(1 for r in reports if r['status'] == 'error')
        
        avg_score = sum(r.get('atomicity_score', 0) for r in reports if 'atomicity_score' in r) / total if total > 0 else 0
        
        print(f"\n{'='*60}")
        print("ATOMICITY ANALYSIS SUMMARY")
        print(f"{'='*60}")
        print(f"Total AKUs Analyzed: {total}")
        print(f"  ✅ Atomic (1 concept): {atomic} ({atomic/total*100:.1f}%)")
        print(f"  🔴 Over-bundled (>1 concept): {over_bundled} ({over_bundled/total*100:.1f}%)")
        print(f"  🟡 Under-specified (fragment): {under_specified} ({under_specified/total*100:.1f}%)")
        print(f"  ⚪ Unclear: {unclear} ({unclear/total*100:.1f}%)")
        if errors > 0:
            print(f"  ❌ Errors: {errors}")
        print(f"\nAverage Atomicity Score: {avg_score:.2f} / 1.0")
        
        # Recommendations
        if over_bundled > 0:
            print(f"\n⚠️  SPLIT RECOMMENDATIONS:")
            for report in reports:
                if report['status'] == 'over_bundled':
                    print(f"   - {Path(report['file']).name} ({report['concept_count']} concepts)")
        
        if under_specified > 0:
            print(f"\n⚠️  MERGE RECOMMENDATIONS:")
            for report in reports:
                if report['status'] == 'under_specified':
                    print(f"   - {Path(report['file']).name} (fragment)")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Analyze AKU atomicity to detect over-bundled or under-specified units"
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to AKU file or directory to analyze"
    )
    parser.add_argument(
        "--directory",
        help="Analyze all AKUs in directory"
    )
    parser.add_argument(
        "--domain",
        help="Analyze all AKUs in domain path (e.g., economics/finance/npv)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output with detailed analysis"
    )
    
    args = parser.parse_args()
    
    analyzer = AtomicityAnalyzer(verbose=args.verbose)
    
    if args.domain:
        # Construct path from domain
        domain_path = Path("domain") / args.domain
        if not domain_path.exists():
            print(f"Error: Domain path not found: {domain_path}")
            sys.exit(1)
        analyzer.analyze_directory(domain_path)
    elif args.directory:
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {dir_path}")
            sys.exit(1)
        analyzer.analyze_directory(dir_path)
    elif args.path:
        aku_path = Path(args.path)
        if not aku_path.exists():
            print(f"Error: File not found: {aku_path}")
            sys.exit(1)
        
        if aku_path.is_dir():
            analyzer.analyze_directory(aku_path)
        else:
            report = analyzer.analyze_aku(aku_path)
            if report['status'] == 'error':
                print(f"Error: {report['error']}")
                sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
