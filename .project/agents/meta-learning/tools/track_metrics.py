"""
Meta-Learning Agent: Metrics Tracker

Tracks extraction success rates, validation errors, and performance metrics
to detect when domain-specific SME agents are needed.

Usage:
    python track_metrics.py --domain economics/bwl/finance --concept npv
    python track_metrics.py --report  # Generate report

Self-contained script with inline dependencies.
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import sys

# Configuration
STORAGE_DIR = Path(__file__).parent.parent / "storage" / "metrics"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# Detection thresholds (from dynamic SME framework)
THRESHOLDS = {
    "volume": 1000,  # AKUs
    "error_rate": 0.05,  # 5%
    "validation_time_multiplier": 2.0,  # 2x average
    "correction_rate": 0.30,  # 30%
    "demand": 3,  # user requests
}


class MetricsTracker:
    """Track metrics for dynamic SME agent detection."""
    
    def __init__(self, storage_dir: Path = STORAGE_DIR):
        self.storage_dir = storage_dir
        self.metrics_file = storage_dir / "domain_metrics.csv"
        self._ensure_metrics_file()
    
    def _ensure_metrics_file(self):
        """Create metrics file if it doesn't exist."""
        if not self.metrics_file.exists():
            with open(self.metrics_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'domain', 'concept', 'aku_count',
                    'success_rate', 'error_rate', 'validation_time_sec',
                    'correction_rate', 'agent_type'
                ])
    
    def record_validation(
        self,
        domain: str,
        concept: str,
        aku_count: int,
        success_rate: float,
        error_rate: float,
        validation_time: float,
        correction_rate: float,
        agent_type: str = "persona"
    ):
        """Record a validation event."""
        with open(self.metrics_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                domain,
                concept,
                aku_count,
                success_rate,
                error_rate,
                validation_time,
                correction_rate,
                agent_type
            ])
        
        print(f"✓ Recorded metrics for {domain}/{concept}")
        
        # Check thresholds
        self._check_thresholds(domain, concept, aku_count, error_rate, 
                               validation_time, correction_rate)
    
    def _check_thresholds(
        self,
        domain: str,
        concept: str,
        aku_count: int,
        error_rate: float,
        validation_time: float,
        correction_rate: float
    ):
        """Check if thresholds are exceeded."""
        triggers = []
        
        if aku_count > THRESHOLDS["volume"]:
            triggers.append(f"Volume threshold exceeded: {aku_count} > {THRESHOLDS['volume']}")
        
        if error_rate > THRESHOLDS["error_rate"]:
            triggers.append(f"Error rate threshold exceeded: {error_rate:.2%} > {THRESHOLDS['error_rate']:.2%}")
        
        if correction_rate > THRESHOLDS["correction_rate"]:
            triggers.append(f"Correction rate threshold exceeded: {correction_rate:.2%} > {THRESHOLDS['correction_rate']:.2%}")
        
        if triggers:
            print(f"\n⚠ THRESHOLD ALERT for {domain}/{concept}:")
            for trigger in triggers:
                print(f"  • {trigger}")
            print(f"  → Consider provisioning specialized SME agent")
            
            # Log alert
            alert_file = self.storage_dir / "threshold_alerts.log"
            with open(alert_file, 'a') as f:
                f.write(f"{datetime.now().isoformat()} | {domain}/{concept}\n")
                for trigger in triggers:
                    f.write(f"  {trigger}\n")
                f.write("\n")
    
    def get_domain_stats(self, domain: str) -> Dict:
        """Get aggregated statistics for a domain."""
        stats = {
            "total_validations": 0,
            "avg_success_rate": 0.0,
            "avg_error_rate": 0.0,
            "avg_validation_time": 0.0,
            "avg_correction_rate": 0.0,
            "total_akus": 0,
        }
        
        if not self.metrics_file.exists():
            return stats
        
        validations = []
        with open(self.metrics_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['domain'] == domain:
                    validations.append(row)
        
        if not validations:
            return stats
        
        stats["total_validations"] = len(validations)
        stats["avg_success_rate"] = sum(float(v['success_rate']) for v in validations) / len(validations)
        stats["avg_error_rate"] = sum(float(v['error_rate']) for v in validations) / len(validations)
        stats["avg_validation_time"] = sum(float(v['validation_time_sec']) for v in validations) / len(validations)
        stats["avg_correction_rate"] = sum(float(v['correction_rate']) for v in validations) / len(validations)
        stats["total_akus"] = sum(int(v['aku_count']) for v in validations)
        
        return stats
    
    def generate_report(self):
        """Generate metrics report."""
        if not self.metrics_file.exists():
            print("No metrics data available")
            return
        
        # Load all data
        domains = {}
        with open(self.metrics_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                domain = row['domain']
                if domain not in domains:
                    domains[domain] = []
                domains[domain].append(row)
        
        # Print report
        print("\n" + "="*60)
        print("META-LEARNING AGENT: METRICS REPORT")
        print("="*60)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for domain, validations in sorted(domains.items()):
            stats = self.get_domain_stats(domain)
            
            print(f"Domain: {domain}")
            print(f"  Validations: {stats['total_validations']}")
            print(f"  Total AKUs: {stats['total_akus']}")
            print(f"  Avg Success Rate: {stats['avg_success_rate']:.2%}")
            print(f"  Avg Error Rate: {stats['avg_error_rate']:.2%}")
            print(f"  Avg Validation Time: {stats['avg_validation_time']:.2f}s")
            print(f"  Avg Correction Rate: {stats['avg_correction_rate']:.2%}")
            
            # Recommendation
            if stats['avg_error_rate'] > THRESHOLDS['error_rate']:
                print(f"  ⚠ RECOMMENDATION: Provision specialized SME agent")
            elif stats['total_akus'] > THRESHOLDS['volume']:
                print(f"  → RECOMMENDATION: Monitor for specialist need")
            else:
                print(f"  ✓ Generic Domain Empathy Agent adequate")
            
            print()


def main():
    """Main entry point."""
    tracker = MetricsTracker()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--report':
        tracker.generate_report()
        return
    
    # Example usage for NPV pilot
    if len(sys.argv) > 1 and sys.argv[1] == '--npv-pilot':
        tracker.record_validation(
            domain="economics/bwl/finance",
            concept="npv",
            aku_count=10,  # First batch
            success_rate=0.95,
            error_rate=0.02,
            validation_time=5.5,
            correction_rate=0.05,
            agent_type="persona:finance-valuation-expert-v1"
        )
        return
    
    print("Usage:")
    print("  python track_metrics.py --npv-pilot    # Record NPV pilot metrics")
    print("  python track_metrics.py --report       # Generate metrics report")


if __name__ == "__main__":
    main()
