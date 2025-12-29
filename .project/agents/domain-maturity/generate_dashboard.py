#!/usr/bin/env python3
"""
Domain Maturity Dashboard Generator

Creates ASCII art visual dashboard showing maturity status of all domains.

Usage:
    python generate_dashboard.py
    python generate_dashboard.py --format html > dashboard.html
    python generate_dashboard.py --domains economics medicine

Self-contained, uses standard library only.
"""

import sys
import json
from pathlib import Path
from typing import List, Dict
import argparse


def create_progress_bar(percentage: float, width: int = 50) -> str:
    """Create ASCII art progress bar."""
    filled = int(width * percentage / 100)
    empty = width - filled
    bar = "█" * filled + "░" * empty
    return f"[{bar}] {percentage:.1f}%"


def get_level_emoji(level: int) -> str:
    """Get emoji for maturity level."""
    emojis = {
        1: "🌱",  # Nascent - seedling
        2: "🌿",  # Emerging - herb
        3: "🌳",  # Established - tree
        4: "🏛️",   # Comprehensive - classical building
        5: "💎"   # Reference - gem
    }
    return emojis.get(level, "❓")


def generate_ascii_dashboard(reports: List[Dict]) -> str:
    """Generate ASCII art dashboard."""
    
    lines = []
    lines.append("╔" + "═" * 78 + "╗")
    lines.append("║" + " KNOWLEDGE DOMAIN MATURITY DASHBOARD ".center(78) + "║")
    lines.append("╠" + "═" * 78 + "╣")
    lines.append("║" + "".center(78) + "║")
    
    # Summary statistics
    total_domains = len(reports)
    total_akus = sum(r["aku_counts"]["total"] for r in reports)
    avg_maturity = sum(r["maturity_level"] for r in reports) / total_domains if total_domains > 0 else 0
    
    lines.append("║  " + f"Total Domains: {total_domains}".ljust(76) + "║")
    lines.append("║  " + f"Total AKUs: {total_akus}".ljust(76) + "║")
    lines.append("║  " + f"Average Maturity Level: {avg_maturity:.1f}".ljust(76) + "║")
    lines.append("║" + "".center(78) + "║")
    lines.append("╠" + "═" * 78 + "╣")
    
    # Sort by maturity level (descending)
    sorted_reports = sorted(reports, key=lambda r: (r["maturity_level"], r["completeness_percentage"]), reverse=True)
    
    # Display each domain
    for report in sorted_reports:
        domain = report["domain_path"]
        level = report["maturity_level"]
        level_name = report["maturity_name"]
        completeness = report["completeness_percentage"]
        aku_count = report["aku_counts"]["total"]
        emoji = get_level_emoji(level)
        
        # Domain header
        lines.append("║" + "".center(78) + "║")
        domain_line = f"  {emoji} {domain}"
        lines.append("║" + domain_line.ljust(78) + "║")
        
        # Maturity level
        level_line = f"     Level {level}: {level_name}"
        lines.append("║" + level_line.ljust(78) + "║")
        
        # Progress bar
        bar = create_progress_bar(completeness, width=50)
        bar_line = f"     {bar}"
        lines.append("║" + bar_line.ljust(78) + "║")
        
        # AKU count
        target = report["aku_counts"]["target"]
        aku_line = f"     AKUs: {aku_count}/{target}"
        lines.append("║" + aku_line.ljust(78) + "║")
        
        # Distribution
        dist = report["type_distribution"]
        def_pct = dist.get("definitions", 0)
        form_pct = dist.get("formulas", 0)
        theory_pct = dist.get("theory", 0)
        ex_pct = dist.get("examples", 0)
        dist_line = f"     Dist: Def {def_pct:.0f}% | Form {form_pct:.0f}% | Theory {theory_pct:.0f}% | Ex {ex_pct:.0f}%"
        lines.append("║" + dist_line.ljust(78) + "║")
        
        # Top gap if any
        gaps = report.get("gaps", [])
        if gaps:
            gap_text = gaps[0]
            if len(gap_text) > 60:
                gap_text = gap_text[:57] + "..."
            gap_line = f"     ⚠ {gap_text}"
            lines.append("║" + gap_line.ljust(78) + "║")
    
    lines.append("║" + "".center(78) + "║")
    lines.append("╚" + "═" * 78 + "╝")
    lines.append("")
    lines.append("Legend:")
    lines.append("  🌱 Level 1: Nascent (0-20% complete)")
    lines.append("  🌿 Level 2: Emerging (20-40% complete)")
    lines.append("  🌳 Level 3: Established (40-60% complete)")
    lines.append("  🏛️  Level 4: Comprehensive (60-85% complete)")
    lines.append("  💎 Level 5: Reference (85-100% complete)")
    lines.append("")
    
    return "\n".join(lines)


def generate_html_dashboard(reports: List[Dict]) -> str:
    """Generate HTML dashboard."""
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Knowledge Domain Maturity Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            margin: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 30px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }
        .summary {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .summary-stat {
            display: inline-block;
            margin: 0 20px;
            font-size: 1.1em;
        }
        .domain-card {
            background: #f8f9fa;
            border-left: 5px solid #667eea;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .domain-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .domain-card.level-1 { border-left-color: #ff6b6b; }
        .domain-card.level-2 { border-left-color: #feca57; }
        .domain-card.level-3 { border-left-color: #48dbfb; }
        .domain-card.level-4 { border-left-color: #1dd1a1; }
        .domain-card.level-5 { border-left-color: #9b59b6; }
        .domain-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .domain-name {
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }
        .level-badge {
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        .level-badge.level-1 { background: #ff6b6b; }
        .level-badge.level-2 { background: #feca57; color: #333; }
        .level-badge.level-3 { background: #48dbfb; }
        .level-badge.level-4 { background: #1dd1a1; }
        .level-badge.level-5 { background: #9b59b6; }
        .progress-bar {
            width: 100%;
            height: 25px;
            background: #e0e0e0;
            border-radius: 12px;
            overflow: hidden;
            margin: 15px 0;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 10px;
            color: white;
            font-weight: bold;
            font-size: 0.9em;
            transition: width 1s ease-in-out;
        }
        .stats {
            display: flex;
            justify-content: space-between;
            margin-top: 15px;
            font-size: 0.9em;
            color: #666;
        }
        .stat-item {
            flex: 1;
        }
        .gap {
            margin-top: 10px;
            padding: 10px;
            background: #fff3cd;
            border-left: 3px solid #ffc107;
            border-radius: 4px;
            font-size: 0.9em;
        }
        .legend {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .legend h3 {
            margin-top: 0;
        }
        .legend-item {
            display: inline-block;
            margin: 5px 15px 5px 0;
        }
        .legend-color {
            display: inline-block;
            width: 20px;
            height: 20px;
            border-radius: 3px;
            margin-right: 8px;
            vertical-align: middle;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Knowledge Domain Maturity Dashboard</h1>
"""
    
    # Summary
    total_domains = len(reports)
    total_akus = sum(r["aku_counts"]["total"] for r in reports)
    avg_maturity = sum(r["maturity_level"] for r in reports) / total_domains if total_domains > 0 else 0
    
    html += f"""
        <div class="summary">
            <div class="summary-stat"><strong>{total_domains}</strong> Domains</div>
            <div class="summary-stat"><strong>{total_akus}</strong> Total AKUs</div>
            <div class="summary-stat"><strong>{avg_maturity:.1f}</strong> Avg Maturity Level</div>
        </div>
"""
    
    # Sort by maturity level (descending)
    sorted_reports = sorted(reports, key=lambda r: (r["maturity_level"], r["completeness_percentage"]), reverse=True)
    
    # Domain cards
    for report in sorted_reports:
        domain = report["domain_path"]
        level = report["maturity_level"]
        level_name = report["maturity_name"]
        completeness = report["completeness_percentage"]
        aku_count = report["aku_counts"]["total"]
        target = report["aku_counts"]["target"]
        dist = report["type_distribution"]
        gaps = report.get("gaps", [])
        
        html += f"""
        <div class="domain-card level-{level}">
            <div class="domain-header">
                <div class="domain-name">{domain}</div>
                <div class="level-badge level-{level}">Level {level}: {level_name}</div>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {completeness}%">{completeness:.1f}%</div>
            </div>
            <div class="stats">
                <div class="stat-item"><strong>AKUs:</strong> {aku_count}/{target}</div>
                <div class="stat-item"><strong>Definitions:</strong> {dist.get('definitions', 0):.0f}%</div>
                <div class="stat-item"><strong>Formulas:</strong> {dist.get('formulas', 0):.0f}%</div>
                <div class="stat-item"><strong>Theory:</strong> {dist.get('theory', 0):.0f}%</div>
                <div class="stat-item"><strong>Examples:</strong> {dist.get('examples', 0):.0f}%</div>
            </div>
"""
        
        if gaps:
            html += f"""
            <div class="gap">⚠️ <strong>Top Priority:</strong> {gaps[0]}</div>
"""
        
        html += """
        </div>
"""
    
    # Legend
    html += """
        <div class="legend">
            <h3>Maturity Levels</h3>
            <div class="legend-item">
                <span class="legend-color" style="background: #ff6b6b;"></span>
                <strong>Level 1 - Nascent:</strong> 0-20% complete (basic groundwork)
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background: #feca57;"></span>
                <strong>Level 2 - Emerging:</strong> 20-40% complete (core concepts present)
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background: #48dbfb;"></span>
                <strong>Level 3 - Established:</strong> 40-60% complete (ready for expert use)
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background: #1dd1a1;"></span>
                <strong>Level 4 - Comprehensive:</strong> 60-85% complete (graduate-level complete)
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background: #9b59b6;"></span>
                <strong>Level 5 - Reference:</strong> 85-100% complete (publication-quality)
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    return html


def main():
    parser = argparse.ArgumentParser(
        description="Generate visual dashboard of domain maturity"
    )
    parser.add_argument(
        "--format",
        choices=["ascii", "html"],
        default="ascii",
        help="Output format (default: ascii)"
    )
    parser.add_argument(
        "--domains",
        nargs="+",
        help="Specific domains to include (default: all)"
    )
    
    args = parser.parse_args()
    
    # Find repository root
    repo_root = Path(__file__).resolve().parents[3]
    
    # Import tracker to scan domains
    sys.path.insert(0, str(Path(__file__).parent))
    from domain_maturity_tracker import DomainMaturityTracker
    
    tracker = DomainMaturityTracker(repo_root)
    
    # Scan domains
    if args.domains:
        reports = []
        for domain in args.domains:
            report = tracker.scan_domain(domain)
            if "error" not in report:
                reports.append(report)
    else:
        reports = tracker.scan_all_domains()
    
    if not reports:
        print("No domains found to display", file=sys.stderr)
        sys.exit(1)
    
    # Generate dashboard
    if args.format == "html":
        dashboard = generate_html_dashboard(reports)
    else:
        dashboard = generate_ascii_dashboard(reports)
    
    print(dashboard)


if __name__ == "__main__":
    main()
