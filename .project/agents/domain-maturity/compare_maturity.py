#!/usr/bin/env python3
"""
Domain Maturity Comparison Tool

Compare maturity between two points in time to track progress.

Usage:
    python compare_maturity.py --domain <domain-path>
    python compare_maturity.py --domain <domain-path> --baseline 2025-12-01
    python compare_maturity.py --all --since 2025-12-01

Self-contained, uses standard library only.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import argparse


def load_history(history_file: Path) -> list:
    """Load maturity history."""
    if not history_file.exists():
        return []
    
    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def filter_history(history: list, domain: str = None, since: str = None) -> list:
    """Filter history by domain and date."""
    filtered = history
    
    if domain:
        filtered = [h for h in filtered if h.get("domain_path") == domain]
    
    if since:
        since_date = datetime.fromisoformat(since.replace('Z', '+00:00'))
        filtered = [h for h in filtered 
                   if datetime.fromisoformat(h.get("scan_date", "").replace('Z', '+00:00')) >= since_date]
    
    return filtered


def compare_reports(old: dict, new: dict) -> dict:
    """Compare two maturity reports and calculate changes."""
    
    comparison = {
        "domain": new.get("domain_path"),
        "old_date": old.get("scan_date"),
        "new_date": new.get("scan_date"),
        "changes": {}
    }
    
    # Level change
    old_level = old.get("maturity_level", 0)
    new_level = new.get("maturity_level", 0)
    comparison["changes"]["maturity_level"] = {
        "old": old_level,
        "new": new_level,
        "delta": new_level - old_level,
        "improved": new_level > old_level
    }
    
    # Completeness change
    old_completeness = old.get("completeness_percentage", 0)
    new_completeness = new.get("completeness_percentage", 0)
    comparison["changes"]["completeness"] = {
        "old": old_completeness,
        "new": new_completeness,
        "delta": round(new_completeness - old_completeness, 1),
        "improved": new_completeness > old_completeness
    }
    
    # AKU count change
    old_count = old.get("aku_counts", {}).get("total", 0)
    new_count = new.get("aku_counts", {}).get("total", 0)
    comparison["changes"]["aku_count"] = {
        "old": old_count,
        "new": new_count,
        "delta": new_count - old_count,
        "improved": new_count > old_count
    }
    
    # Validation rate change
    old_validation = old.get("validation", {}).get("pass_rate_pct", 0)
    new_validation = new.get("validation", {}).get("pass_rate_pct", 0)
    comparison["changes"]["validation_rate"] = {
        "old": old_validation,
        "new": new_validation,
        "delta": round(new_validation - old_validation, 1),
        "improved": new_validation >= old_validation
    }
    
    # Cross-link change
    old_links = old.get("cross_links", {}).get("total", 0)
    new_links = new.get("cross_links", {}).get("total", 0)
    comparison["changes"]["cross_links"] = {
        "old": old_links,
        "new": new_links,
        "delta": new_links - old_links,
        "improved": new_links > old_links
    }
    
    # Overall improvement
    improvements = sum(1 for change in comparison["changes"].values() 
                      if change.get("improved", False))
    comparison["overall_improvement"] = improvements >= 3  # Majority improved
    
    return comparison


def format_comparison(comparison: dict) -> str:
    """Format comparison as human-readable text."""
    
    output = []
    output.append("=" * 70)
    output.append(f"MATURITY COMPARISON: {comparison['domain']}")
    output.append("=" * 70)
    output.append("")
    output.append(f"Baseline: {comparison['old_date'][:10]}")
    output.append(f"Current:  {comparison['new_date'][:10]}")
    output.append("")
    
    changes = comparison["changes"]
    
    # Maturity level
    level = changes["maturity_level"]
    arrow = "📈" if level["improved"] else "➡️"
    output.append(f"{arrow} Maturity Level: {level['old']} → {level['new']} ({level['delta']:+d})")
    
    # Completeness
    comp = changes["completeness"]
    arrow = "📈" if comp["improved"] else "📉" if comp["delta"] < 0 else "➡️"
    output.append(f"{arrow} Completeness: {comp['old']:.1f}% → {comp['new']:.1f}% ({comp['delta']:+.1f}%)")
    
    # AKU count
    aku = changes["aku_count"]
    arrow = "📈" if aku["improved"] else "➡️"
    output.append(f"{arrow} AKU Count: {aku['old']} → {aku['new']} ({aku['delta']:+d})")
    
    # Validation
    val = changes["validation_rate"]
    arrow = "✅" if val["improved"] else "⚠️" if val["delta"] < 0 else "➡️"
    output.append(f"{arrow} Validation: {val['old']:.1f}% → {val['new']:.1f}% ({val['delta']:+.1f}%)")
    
    # Cross-links
    links = changes["cross_links"]
    arrow = "🔗" if links["improved"] else "➡️"
    output.append(f"{arrow} Cross-Links: {links['old']} → {links['new']} ({links['delta']:+d})")
    
    output.append("")
    
    if comparison["overall_improvement"]:
        output.append("✅ Overall Assessment: IMPROVED")
    else:
        output.append("⚠️ Overall Assessment: No significant improvement")
    
    output.append("=" * 70)
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Compare domain maturity between two points in time"
    )
    parser.add_argument(
        "--domain",
        help="Domain path to compare"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Compare all domains"
    )
    parser.add_argument(
        "--baseline",
        help="Baseline date (ISO format: YYYY-MM-DD or full timestamp)"
    )
    parser.add_argument(
        "--since",
        help="Show progress since date (ISO format: YYYY-MM-DD)"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )
    
    args = parser.parse_args()
    
    # Find repository root
    repo_root = Path(__file__).resolve().parents[3]
    history_file = repo_root / ".project" / "agents" / "domain-maturity" / "maturity_history.json"
    
    # Load history
    history = load_history(history_file)
    
    if not history:
        print("No historical data found. Run tracker with --save-history first.", file=sys.stderr)
        sys.exit(1)
    
    # Filter history
    if args.domain:
        domain_history = [h for h in history if h.get("domain_path") == args.domain]
        
        if len(domain_history) < 2:
            print(f"Not enough historical data for {args.domain}. Need at least 2 data points.", file=sys.stderr)
            sys.exit(1)
        
        # Get baseline and current
        if args.baseline:
            baseline_date = args.baseline
            baseline = None
            for h in domain_history:
                if h.get("scan_date", "").startswith(baseline_date):
                    baseline = h
                    break
            
            if not baseline:
                print(f"No data found for baseline date: {baseline_date}", file=sys.stderr)
                sys.exit(1)
        else:
            baseline = domain_history[0]
        
        current = domain_history[-1]
        
        # Compare
        comparison = compare_reports(baseline, current)
        
        if args.format == "json":
            print(json.dumps(comparison, indent=2))
        else:
            print(format_comparison(comparison))
    
    elif args.all:
        # Compare all domains
        if args.since:
            filtered = filter_history(history, since=args.since)
        else:
            filtered = history
        
        # Group by domain
        by_domain = {}
        for entry in filtered:
            domain = entry.get("domain_path")
            if domain not in by_domain:
                by_domain[domain] = []
            by_domain[domain].append(entry)
        
        # Compare each domain
        comparisons = []
        for domain, domain_history in by_domain.items():
            if len(domain_history) >= 2:
                baseline = domain_history[0]
                current = domain_history[-1]
                comparison = compare_reports(baseline, current)
                comparisons.append(comparison)
        
        if args.format == "json":
            print(json.dumps(comparisons, indent=2))
        else:
            for comparison in comparisons:
                print(format_comparison(comparison))
                print("\n")
    
    else:
        print("ERROR: Must specify --domain or --all", file=sys.stderr)
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
