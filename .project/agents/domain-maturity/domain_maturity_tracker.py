#!/usr/bin/env python3
"""
Domain Maturity Tracker

Scans knowledge domains and calculates maturity level based on AKU count,
type distribution, cross-link density, validation status, and other metrics.

Usage:
    # Scan single domain
    python domain_maturity_tracker.py --domain science/physics/quantum-mechanics/planck-units
    
    # Scan all domains
    python domain_maturity_tracker.py --all
    
    # Show historical progress
    python domain_maturity_tracker.py --domain economics/finance/valuation/npv --history
    
    # Set target maturity level
    python domain_maturity_tracker.py --domain science/physics/quantum-mechanics/planck-units --target-level 3
    
    # Output JSON format
    python domain_maturity_tracker.py --domain economics/finance --format json

Self-contained, uses standard library only.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timezone
from collections import defaultdict
import argparse


# Target distribution by maturity level (in percentages)
TARGET_DISTRIBUTIONS = {
    1: {"definitions": 80, "formulas": 15, "theory": 0, "examples": 5, "applications": 0},
    2: {"definitions": 65, "formulas": 20, "theory": 5, "examples": 10, "applications": 0},
    3: {"definitions": 45, "formulas": 25, "theory": 12, "examples": 12, "applications": 6},
    4: {"definitions": 35, "formulas": 27, "theory": 17, "examples": 17, "applications": 12},
    5: {"definitions": 30, "formulas": 25, "theory": 20, "examples": 15, "applications": 10},
}

# Maturity level thresholds (by completeness percentage)
MATURITY_LEVELS = {
    1: {"name": "Nascent", "min": 0, "max": 20, "aku_range": (1, 15)},
    2: {"name": "Emerging", "min": 20, "max": 40, "aku_range": (16, 40)},
    3: {"name": "Established", "min": 40, "max": 60, "aku_range": (41, 80)},
    4: {"name": "Comprehensive", "min": 60, "max": 85, "aku_range": (81, 150)},
    5: {"name": "Reference", "min": 85, "max": 100, "aku_range": (150, 999)},
}


class DomainMaturityTracker:
    """Tracks maturity and completeness of knowledge domains."""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.domain_root = repo_root / "domain"
        self.history_file = repo_root / ".project" / "agents" / "domain-maturity" / "maturity_history.json"
        
    def scan_domain(self, domain_path: str) -> Dict:
        """Scan a domain directory and calculate maturity metrics."""
        
        domain_dir = self.domain_root / domain_path
        if not domain_dir.exists():
            return {"error": f"Domain not found: {domain_path}"}
        
        # Find AKU directory
        aku_dir = domain_dir / "akus"
        if not aku_dir.exists():
            return {"error": f"No akus directory found in {domain_path}"}
        
        # Count AKUs by type
        aku_counts = self._count_akus_by_type(aku_dir)
        total_akus = sum(aku_counts.values())
        
        if total_akus == 0:
            return {"error": f"No AKUs found in {domain_path}"}
        
        # Calculate type distribution
        distribution = {
            aku_type: (count / total_akus * 100) if total_akus > 0 else 0
            for aku_type, count in aku_counts.items()
        }
        
        # Count cross-links
        cross_links = self._count_cross_links(aku_dir)
        
        # Estimate target AKU count
        target_count = self._estimate_target_count(total_akus, domain_path)
        
        # Calculate completeness percentage
        completeness = (total_akus / target_count * 100) if target_count > 0 else 0
        
        # Determine maturity level
        maturity_level = self._calculate_maturity_level(completeness, total_akus, distribution)
        
        # Calculate type distribution score
        distribution_score = self._calculate_distribution_score(distribution, maturity_level)
        
        # Identify gaps
        gaps = self._identify_gaps(aku_counts, distribution, maturity_level, target_count)
        
        # Validate AKUs (count passing validation)
        validation_stats = self._validate_akus(aku_dir)
        
        # Load completeness metadata if exists
        metadata_file = domain_dir / "COMPLETENESS_METADATA.yaml"
        metadata = self._load_metadata(metadata_file) if metadata_file.exists() else {}
        
        # Compile report
        report = {
            "domain_path": domain_path,
            "scan_date": datetime.now(timezone.utc).isoformat(),
            "maturity_level": maturity_level,
            "maturity_name": MATURITY_LEVELS[maturity_level]["name"],
            "completeness_percentage": round(completeness, 1),
            "aku_counts": {
                "total": total_akus,
                "by_type": aku_counts,
                "target": target_count
            },
            "type_distribution": {k: round(v, 1) for k, v in distribution.items()},
            "distribution_score": round(distribution_score, 2),
            "cross_links": cross_links,
            "validation": validation_stats,
            "gaps": gaps,
            "metadata": metadata
        }
        
        return report
    
    def _count_akus_by_type(self, aku_dir: Path) -> Dict[str, int]:
        """Count AKUs by type (definitions, formulas, theory, examples, applications)."""
        counts = defaultdict(int)
        
        # Standard subdirectories
        type_dirs = {
            "definitions": aku_dir / "definitions",
            "formulas": aku_dir / "formulas",
            "theory": aku_dir / "theory",
            "examples": aku_dir / "examples",
            "applications": aku_dir / "applications",
        }
        
        for aku_type, type_dir in type_dirs.items():
            if type_dir.exists():
                json_files = list(type_dir.glob("*.json"))
                counts[aku_type] = len(json_files)
        
        # Check for other subdirectories
        for subdir in aku_dir.iterdir():
            if subdir.is_dir() and subdir.name not in type_dirs:
                json_files = list(subdir.glob("*.json"))
                counts[subdir.name] = len(json_files)
        
        return dict(counts)
    
    def _count_cross_links(self, aku_dir: Path) -> Dict:
        """Count internal and external cross-links in AKUs."""
        internal_links = 0
        external_links = 0
        total_akus = 0
        
        for json_file in aku_dir.rglob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    aku = json.load(f)
                    total_akus += 1
                    
                    # Check relationships section
                    if "relationships" in aku:
                        rels = aku["relationships"]
                        if isinstance(rels, dict):
                            # Count links
                            for rel_type in ["related_to", "prerequisite_for", "derived_from", "applied_in"]:
                                if rel_type in rels:
                                    links = rels[rel_type]
                                    if isinstance(links, list):
                                        for link in links:
                                            if isinstance(link, str):
                                                # Heuristic: external if contains different domain
                                                if "/" in link and link.count("/") >= 3:
                                                    external_links += 1
                                                else:
                                                    internal_links += 1
            except (json.JSONDecodeError, IOError):
                continue
        
        # Estimate potential links (very rough heuristic)
        potential_internal = total_akus * (total_akus - 1) // 2 if total_akus > 1 else 0
        potential_external = total_akus * 10  # Assume 10 potential external links per AKU
        
        internal_density = (internal_links / potential_internal * 100) if potential_internal > 0 else 0
        external_density = (external_links / potential_external * 100) if potential_external > 0 else 0
        
        return {
            "internal": internal_links,
            "external": external_links,
            "total": internal_links + external_links,
            "internal_density_pct": round(internal_density, 1),
            "external_density_pct": round(external_density, 1),
            "potential_internal": potential_internal,
            "potential_external": potential_external
        }
    
    def _estimate_target_count(self, current_count: int, domain_path: str) -> int:
        """Estimate target AKU count for domain completion."""
        
        # If we have metadata with explicit target, use it
        domain_dir = self.domain_root / domain_path
        metadata_file = domain_dir / "COMPLETENESS_METADATA.yaml"
        if metadata_file.exists():
            metadata = self._load_metadata(metadata_file)
            if "target_aku_count" in metadata:
                return metadata["target_aku_count"]
        
        # Heuristic: estimate based on current count and maturity patterns
        # This is a rough estimation that should be overridden by manual assessment
        
        if current_count <= 15:
            # Nascent - assume targeting Emerging (40 AKUs)
            return 40
        elif current_count <= 40:
            # Emerging - assume targeting Established (80 AKUs)
            return 80
        elif current_count <= 80:
            # Established - assume targeting Comprehensive (150 AKUs)
            return 150
        else:
            # Comprehensive or beyond - assume targeting Reference (2x current)
            return current_count * 2
    
    def _calculate_maturity_level(self, completeness: float, aku_count: int, distribution: Dict) -> int:
        """Calculate maturity level based on multiple factors."""
        
        # Primary factor: completeness percentage
        level_by_completeness = 1
        for level, data in MATURITY_LEVELS.items():
            if data["min"] <= completeness < data["max"]:
                level_by_completeness = level
                break
            elif completeness >= data["max"]:
                level_by_completeness = level
        
        # Secondary factor: AKU count ranges
        level_by_count = 1
        for level, data in MATURITY_LEVELS.items():
            min_aku, max_aku = data["aku_range"]
            if min_aku <= aku_count <= max_aku:
                level_by_count = level
                break
            elif aku_count > max_aku:
                level_by_count = level
        
        # Tertiary factor: type distribution (are we balanced?)
        has_theory = distribution.get("theory", 0) > 0
        has_examples = distribution.get("examples", 0) > 0
        has_applications = distribution.get("applications", 0) > 0
        
        # Penalize if missing critical types for claimed level
        distribution_penalty = 0
        if level_by_completeness >= 3 and not has_theory:
            distribution_penalty = 1  # Can't be Established without theory
        if level_by_completeness >= 4 and not has_applications:
            distribution_penalty = max(distribution_penalty, 1)
        
        # Final level: minimum of factors, with penalty
        final_level = min(level_by_completeness, level_by_count) - distribution_penalty
        return max(1, min(5, final_level))
    
    def _calculate_distribution_score(self, actual: Dict, level: int) -> float:
        """Calculate how well type distribution matches target for maturity level."""
        
        target = TARGET_DISTRIBUTIONS[level]
        
        # Normalize actual distribution to include all types
        actual_normalized = {
            "definitions": actual.get("definitions", 0),
            "formulas": actual.get("formulas", 0),
            "theory": actual.get("theory", 0),
            "examples": actual.get("examples", 0),
            "applications": actual.get("applications", 0),
        }
        
        # Calculate absolute differences
        total_diff = sum(abs(actual_normalized[k] - target[k]) for k in target.keys())
        
        # Score: 1 - (total_diff / 200)  [max diff is 200 if completely opposite]
        score = 1 - (total_diff / 200)
        return max(0, min(1, score))
    
    def _identify_gaps(self, counts: Dict, distribution: Dict, level: int, target: int) -> List[str]:
        """Identify critical gaps and recommendations."""
        
        gaps = []
        current_total = sum(counts.values())
        
        # Gap 1: Missing AKUs to reach target
        missing_akus = target - current_total
        if missing_akus > 0:
            gaps.append(f"{missing_akus} more AKUs needed to reach target ({target})")
        
        # Gap 2: Missing critical types for maturity level
        if level >= 3 and counts.get("theory", 0) == 0:
            target_theory = int(current_total * TARGET_DISTRIBUTIONS[level]["theory"] / 100)
            gaps.append(f"{max(1, target_theory)} theory AKUs needed for Level {level}")
        
        if level >= 4 and counts.get("applications", 0) == 0:
            target_apps = int(current_total * TARGET_DISTRIBUTIONS[level]["applications"] / 100)
            gaps.append(f"{max(1, target_apps)} application AKUs needed for Level {level}")
        
        # Gap 3: Type imbalance
        target_dist = TARGET_DISTRIBUTIONS[level]
        for aku_type, target_pct in target_dist.items():
            actual_pct = distribution.get(aku_type, 0)
            diff = target_pct - actual_pct
            
            if diff > 15:  # Significantly under target
                needed = int(current_total * diff / 100)
                gaps.append(f"{needed} more {aku_type} AKUs to balance distribution")
            elif diff < -15:  # Significantly over target
                excess = int(current_total * abs(diff) / 100)
                gaps.append(f"{excess} {aku_type} AKUs could be redistributed to other types")
        
        # Gap 4: Specific recommendations based on patterns
        if counts.get("definitions", 0) > current_total * 0.7:
            gaps.append("Over-emphasis on definitions; add more formulas and examples")
        
        if counts.get("examples", 0) < current_total * 0.05:
            gaps.append("Very few examples; add worked examples to improve understanding")
        
        return gaps
    
    def _validate_akus(self, aku_dir: Path) -> Dict:
        """Quick validation check - just count parseable JSON files."""
        
        total = 0
        valid = 0
        invalid = []
        
        for json_file in aku_dir.rglob("*.json"):
            total += 1
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    json.load(f)
                    valid += 1
            except (json.JSONDecodeError, IOError) as e:
                invalid.append(json_file.name)
        
        pass_rate = (valid / total * 100) if total > 0 else 0
        
        return {
            "total_akus": total,
            "valid_json": valid,
            "invalid_json": len(invalid),
            "pass_rate_pct": round(pass_rate, 1),
            "invalid_files": invalid[:5]  # Show first 5
        }
    
    def _load_metadata(self, metadata_file: Path) -> Dict:
        """Load YAML metadata (simple parsing without PyYAML dependency)."""
        
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            metadata = {}
            current_key = None
            current_list = None
            
            for line in lines:
                line = line.rstrip()
                
                # Skip empty lines and comments
                if not line or line.strip().startswith("#"):
                    continue
                
                # Key-value pairs
                if ":" in line and not line.startswith(" "):
                    if current_list is not None:
                        metadata[current_key] = current_list
                        current_list = None
                    
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    
                    if not value or value == "":
                        # Start of nested structure or list
                        current_key = key
                    else:
                        # Simple key-value
                        metadata[key] = self._parse_value(value)
                
                # List items
                elif line.strip().startswith("-"):
                    if current_list is None:
                        current_list = []
                    item = line.strip()[1:].strip()
                    if item.startswith('"') and item.endswith('"'):
                        item = item[1:-1]
                    current_list.append(item)
            
            # Don't forget last list
            if current_list is not None:
                metadata[current_key] = current_list
            
            return metadata
        
        except Exception as e:
            return {"error": f"Failed to parse metadata: {e}"}
    
    def _parse_value(self, value: str):
        """Parse YAML value to appropriate Python type."""
        
        value = value.strip()
        
        # Remove quotes
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        
        # Boolean
        if value.lower() in ["true", "yes"]:
            return True
        if value.lower() in ["false", "no"]:
            return False
        
        # Number
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            pass
        
        # Percentage
        if value.endswith("%"):
            try:
                return float(value[:-1])
            except ValueError:
                pass
        
        # String
        return value
    
    def save_history(self, report: Dict):
        """Save maturity report to history log."""
        
        history = []
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except (json.JSONDecodeError, IOError):
                history = []
        
        # Add this report
        history.append(report)
        
        # Save
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
    
    def get_history(self, domain_path: str) -> List[Dict]:
        """Get historical maturity data for a domain."""
        
        if not self.history_file.exists():
            return []
        
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
            
            # Filter to this domain
            return [h for h in history if h.get("domain_path") == domain_path]
        except (json.JSONDecodeError, IOError):
            return []
    
    def scan_all_domains(self) -> List[Dict]:
        """Scan all domains in repository."""
        
        reports = []
        
        # Walk domain directory
        for domain_dir in self.domain_root.rglob("akus"):
            # Get relative path from domain root
            rel_path = domain_dir.parent.relative_to(self.domain_root)
            domain_path = str(rel_path)
            
            # Scan this domain
            report = self.scan_domain(domain_path)
            if "error" not in report:
                reports.append(report)
        
        # Sort by maturity level (descending)
        reports.sort(key=lambda r: r["maturity_level"], reverse=True)
        
        return reports


def format_report_text(report: Dict) -> str:
    """Format maturity report as human-readable text."""
    
    if "error" in report:
        return f"ERROR: {report['error']}"
    
    output = []
    output.append("=" * 70)
    output.append(f"DOMAIN MATURITY REPORT: {report['domain_path']}")
    output.append("=" * 70)
    output.append("")
    
    # Maturity level
    level = report["maturity_level"]
    level_name = report["maturity_name"]
    completeness = report["completeness_percentage"]
    output.append(f"Maturity Level: {level} - {level_name} ({completeness}% complete)")
    output.append("")
    
    # AKU counts
    counts = report["aku_counts"]
    output.append(f"AKU Count: {counts['total']} / {counts['target']} (target)")
    output.append("")
    output.append("By Type:")
    for aku_type, count in counts["by_type"].items():
        pct = report["type_distribution"].get(aku_type, 0)
        output.append(f"  - {aku_type.capitalize()}: {count} ({pct}%)")
    output.append("")
    
    # Distribution score
    dist_score = report["distribution_score"]
    output.append(f"Type Distribution Score: {dist_score:.2f} (1.0 = perfect balance)")
    output.append("")
    
    # Cross-links
    links = report["cross_links"]
    output.append(f"Cross-Links:")
    output.append(f"  - Internal: {links['internal']} ({links['internal_density_pct']}% density)")
    output.append(f"  - External: {links['external']} ({links['external_density_pct']}% density)")
    output.append(f"  - Total: {links['total']}")
    output.append("")
    
    # Validation
    validation = report["validation"]
    output.append(f"Validation: {validation['valid_json']}/{validation['total_akus']} pass ({validation['pass_rate_pct']}%)")
    if validation["invalid_files"]:
        output.append(f"  Invalid files: {', '.join(validation['invalid_files'])}")
    output.append("")
    
    # Gaps
    gaps = report["gaps"]
    if gaps:
        output.append("Critical Gaps & Recommendations:")
        for i, gap in enumerate(gaps, 1):
            output.append(f"  {i}. {gap}")
        output.append("")
    
    # Sufficiency assessment
    output.append("Sufficient For:")
    if level >= 2:
        output.append("  ✓ Expert-level reference (single domain queries)")
    if level >= 3:
        output.append("  ✓ Graduate student coursework (isolated topics)")
        output.append("  ✓ Expert consultation on interconnected questions")
    if level >= 4:
        output.append("  ✓ Complete educational curricula (multiple levels)")
        output.append("  ✓ Publication-quality reference material")
    if level >= 5:
        output.append("  ✓ Authoritative reference work")
        output.append("  ✓ Multi-lingual expert translation (15+ languages)")
    output.append("")
    
    output.append("NOT Sufficient For:")
    if level < 5:
        output.append("  ✗ Authoritative reference work")
    if level < 4:
        output.append("  ✗ Publication-quality reference")
        output.append("  ✗ Complete K-12 curriculum")
    if level < 3:
        output.append("  ✗ Expert consultation on interconnected questions")
        output.append("  ✗ Graduate-level complete coursework")
    if level < 2:
        output.append("  ✗ Any production use")
        output.append("  ✗ Educational content")
    output.append("")
    
    # Next steps
    if level < 5:
        next_level = level + 1
        next_name = MATURITY_LEVELS[next_level]["name"]
        output.append(f"Next Steps to Reach Level {next_level} ({next_name}):")
        
        if gaps:
            for gap in gaps[:3]:  # Top 3 priorities
                output.append(f"  • {gap}")
        
        if level == 1:
            output.append("  • Add 10-20 more definition AKUs")
            output.append("  • Create 3-5 formula AKUs")
            output.append("  • Add 2-3 worked examples")
        elif level == 2:
            output.append("  • Add theory AKUs (target 10% of total)")
            output.append("  • Establish cross-domain connections")
            output.append("  • Create rendering for 1 additional audience level")
        elif level == 3:
            output.append("  • Expand to 80-120 AKUs")
            output.append("  • Add application case studies")
            output.append("  • Complete cross-domain linking")
            output.append("  • Add 2 more audience levels")
        elif level == 4:
            output.append("  • Expand to 150-200+ AKUs")
            output.append("  • Add cutting-edge research topics")
            output.append("  • Complete toddler-level renderings")
            output.append("  • Achieve 90%+ cross-link density")
    
    output.append("")
    output.append(f"Report generated: {report['scan_date']}")
    output.append("=" * 70)
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Track maturity and completeness of knowledge domains"
    )
    parser.add_argument(
        "--domain",
        help="Domain path to scan (e.g., science/physics/quantum-mechanics/planck-units)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan all domains in repository"
    )
    parser.add_argument(
        "--history",
        action="store_true",
        help="Show historical progress for domain"
    )
    parser.add_argument(
        "--target-level",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="Show what's needed to reach target maturity level"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--save-history",
        action="store_true",
        help="Save scan results to history log"
    )
    
    args = parser.parse_args()
    
    # Find repository root
    repo_root = Path(__file__).resolve().parents[3]
    
    tracker = DomainMaturityTracker(repo_root)
    
    # Scan all domains
    if args.all:
        reports = tracker.scan_all_domains()
        
        if args.format == "json":
            print(json.dumps(reports, indent=2))
        else:
            print(f"\nFound {len(reports)} domains with AKUs\n")
            for report in reports:
                print(format_report_text(report))
                print("\n")
        
        return
    
    # Show history
    if args.history:
        if not args.domain:
            print("ERROR: --history requires --domain", file=sys.stderr)
            sys.exit(1)
        
        history = tracker.get_history(args.domain)
        
        if not history:
            print(f"No historical data found for {args.domain}")
            return
        
        if args.format == "json":
            print(json.dumps(history, indent=2))
        else:
            print(f"\nHistorical Progress for {args.domain}")
            print("=" * 70)
            for entry in history:
                date = entry["scan_date"][:10]
                level = entry["maturity_level"]
                level_name = entry["maturity_name"]
                total = entry["aku_counts"]["total"]
                completeness = entry["completeness_percentage"]
                print(f"{date}: Level {level} ({level_name}) - {total} AKUs ({completeness}%)")
            print("")
        
        return
    
    # Scan single domain
    if not args.domain:
        print("ERROR: Must specify --domain or --all", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    report = tracker.scan_domain(args.domain)
    
    if "error" in report:
        print(f"ERROR: {report['error']}", file=sys.stderr)
        sys.exit(1)
    
    # Save to history if requested
    if args.save_history:
        tracker.save_history(report)
        print(f"Saved to history: {tracker.history_file}")
    
    # Output report
    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(format_report_text(report))
    
    # Show target level analysis if requested
    if args.target_level:
        current_level = report["maturity_level"]
        target = args.target_level
        
        if target <= current_level:
            print(f"\n✓ Already at or above Level {target}")
        else:
            print(f"\nTo reach Level {target} ({MATURITY_LEVELS[target]['name']}):")
            print("=" * 70)
            
            # Calculate what's needed
            current_count = report["aku_counts"]["total"]
            target_range = MATURITY_LEVELS[target]["aku_range"]
            target_min = target_range[0]
            
            if current_count < target_min:
                needed = target_min - current_count
                print(f"• Add at least {needed} more AKUs (target: {target_min}+)")
            
            # Type distribution needed
            target_dist = TARGET_DISTRIBUTIONS[target]
            current_dist = report["type_distribution"]
            
            print(f"• Target type distribution for Level {target}:")
            for aku_type, target_pct in target_dist.items():
                current_pct = current_dist.get(aku_type, 0)
                diff = target_pct - current_pct
                status = "✓" if abs(diff) < 5 else "✗"
                print(f"  {status} {aku_type.capitalize()}: {target_pct}% (currently {current_pct:.1f}%)")
            
            # Level-specific requirements
            if target >= 3 and report["aku_counts"]["by_type"].get("theory", 0) == 0:
                print("• Add theory AKUs (critical for Level 3+)")
            
            if target >= 4 and report["aku_counts"]["by_type"].get("applications", 0) == 0:
                print("• Add application AKUs (critical for Level 4+)")
            
            print("")


if __name__ == "__main__":
    main()
