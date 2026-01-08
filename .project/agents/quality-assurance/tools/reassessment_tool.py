#!/usr/bin/env python3
"""
Reassessment Tool for AKU Quality Tracking

This tool manages the reassessment process for AKUs, including:
- Triggering reassessments based on schedule or criteria
- Tracking quality score history
- Managing priority queues for improvement
- Generating reassessment reports

Usage:
    python reassessment_tool.py --schedule          # Run scheduled reassessments
    python reassessment_tool.py --aku <path>        # Reassess specific AKU
    python reassessment_tool.py --priority-queue    # Show priority queue
    python reassessment_tool.py --history <aku_id>  # Show quality history
    python reassessment_tool.py --report            # Generate reassessment report
"""

import json
import yaml
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import hashlib
import re


class ReassessmentTool:
    """Manages AKU reassessment process and quality tracking."""
    
    def __init__(self, project_root: str = None):
        """Initialize the reassessment tool."""
        if project_root is None:
            project_root = Path(__file__).parent.parent.parent.parent.parent
        self.project_root = Path(project_root)
        self.tracking_dir = self.project_root / ".project" / "tracking"
        self.quality_scores_file = self.tracking_dir / "quality-scores.yaml"
        self.reassessment_log_file = self.tracking_dir / "reassessment-log.yaml"
        
        # Reassessment configuration
        self.config = {
            "scheduled_intervals": {
                "grade_A": 180,  # Days between reassessments
                "grade_B": 90,
                "grade_C": 45,
                "grade_D": 14,
                "grade_F": 7
            },
            "trigger_thresholds": {
                "content_change_significant": 0.3,  # 30% change triggers reassessment
                "dependency_update_max_age": 30,    # Days after dependency update
                "external_reference_check": 90      # Days to recheck external refs
            },
            "priority_weights": {
                "grade_score": 0.4,
                "time_since_assessment": 0.2,
                "content_importance": 0.2,
                "dependency_count": 0.1,
                "user_feedback": 0.1
            }
        }
    
    def load_quality_scores(self) -> Dict:
        """Load quality scores from tracking file."""
        if not self.quality_scores_file.exists():
            return {"version": "1.0.0", "last_updated": None, "akus": {}}
        
        with open(self.quality_scores_file) as f:
            return yaml.safe_load(f) or {"version": "1.0.0", "akus": {}}
    
    def save_quality_scores(self, scores: Dict) -> None:
        """Save quality scores to tracking file."""
        self.tracking_dir.mkdir(parents=True, exist_ok=True)
        scores["last_updated"] = datetime.now(timezone.utc).isoformat() + "Z"
        
        with open(self.quality_scores_file, 'w') as f:
            yaml.dump(scores, f, default_flow_style=False, sort_keys=False)
    
    def load_reassessment_log(self) -> Dict:
        """Load reassessment log."""
        if not self.reassessment_log_file.exists():
            return {"assessments": [], "summary": {}}
        
        with open(self.reassessment_log_file) as f:
            return yaml.safe_load(f) or {"assessments": [], "summary": {}}
    
    def save_reassessment_log(self, log: Dict) -> None:
        """Save reassessment log."""
        self.tracking_dir.mkdir(parents=True, exist_ok=True)
        
        with open(self.reassessment_log_file, 'w') as f:
            yaml.dump(log, f, default_flow_style=False, sort_keys=False)
    
    def calculate_content_hash(self, aku_path: Path) -> str:
        """Calculate hash of AKU content for change detection."""
        with open(aku_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    
    def check_reassessment_triggers(self, aku_path: Path, aku_data: Dict, 
                                   last_assessment: Optional[Dict]) -> List[str]:
        """
        Check if any reassessment triggers are met.
        
        Returns list of trigger reasons.
        """
        triggers = []
        now = datetime.now(timezone.utc)
        
        # 1. Scheduled reassessment check
        if last_assessment:
            last_date = datetime.fromisoformat(
                last_assessment.get("date", "2020-01-01").replace("Z", "")
            )
            grade = last_assessment.get("grade", "C")
            
            # Map grade to letter for interval lookup
            grade_key = f"grade_{grade[0].upper()}"
            interval = self.config["scheduled_intervals"].get(grade_key, 90)
            
            if (now - last_date).days >= interval:
                triggers.append(f"Scheduled: {interval} days since last assessment")
        else:
            triggers.append("Initial: No previous assessment found")
        
        # 2. Content change detection
        if last_assessment and last_assessment.get("content_hash"):
            current_hash = self.calculate_content_hash(aku_path)
            if current_hash != last_assessment["content_hash"]:
                triggers.append("Content: AKU content has been modified")
        
        # 3. External reference age check
        provenance = aku_data.get("provenance", {})
        sources = provenance.get("sources", [])
        for source in sources:
            if source.get("type") in ["website", "api", "database"]:
                triggers.append("External: Has external references requiring verification")
                break
        
        # 4. Dependency update check
        relationships = aku_data.get("relationships", {})
        requires = relationships.get("requires", [])
        if requires:
            # Check if any dependencies have been updated recently
            # This would require cross-referencing with other AKUs
            pass  # Placeholder for dependency tracking
        
        # 5. User feedback trigger
        # This would integrate with a feedback system
        
        return triggers
    
    def calculate_priority_score(self, aku_id: str, aku_data: Dict, 
                                 last_assessment: Optional[Dict]) -> float:
        """
        Calculate priority score for reassessment queue.
        
        Higher score = higher priority.
        Returns score between 0.0 and 1.0.
        """
        score = 0.0
        weights = self.config["priority_weights"]
        
        # 1. Grade-based priority (lower grades = higher priority)
        if last_assessment:
            grade = last_assessment.get("grade", "C")
            grade_scores = {"A+": 0.0, "A": 0.1, "A-": 0.2, 
                           "B+": 0.3, "B": 0.4, "B-": 0.5,
                           "C+": 0.6, "C": 0.7, "C-": 0.8,
                           "D": 0.9, "F": 1.0}
            score += grade_scores.get(grade, 0.5) * weights["grade_score"]
        else:
            score += 1.0 * weights["grade_score"]  # No assessment = highest priority
        
        # 2. Time since last assessment
        if last_assessment:
            last_date = datetime.fromisoformat(
                last_assessment.get("date", "2020-01-01").replace("Z", "")
            )
            days_ago = (datetime.now(timezone.utc) - last_date).days
            time_score = min(days_ago / 180, 1.0)  # Max out at 180 days
            score += time_score * weights["time_since_assessment"]
        else:
            score += 1.0 * weights["time_since_assessment"]
        
        # 3. Content importance
        importance = aku_data.get("classification", {}).get("importance", "medium")
        importance_scores = {"critical": 1.0, "high": 0.75, "medium": 0.5, "low": 0.25}
        score += importance_scores.get(importance, 0.5) * weights["content_importance"]
        
        # 4. Dependency count (more dependencies = more important to keep accurate)
        relationships = aku_data.get("relationships", {})
        enables = relationships.get("enables", [])
        dep_score = min(len(enables) / 10, 1.0)  # Max out at 10 dependents
        score += dep_score * weights["dependency_count"]
        
        # 5. User feedback placeholder
        score += 0.0 * weights["user_feedback"]  # Would integrate with feedback system
        
        return round(score, 3)
    
    def get_priority_queue(self) -> List[Dict]:
        """
        Generate priority queue of AKUs needing reassessment.
        
        Returns sorted list of AKUs by priority score.
        """
        scores = self.load_quality_scores()
        queue = []
        
        # Find all AKUs in the pilot
        pilot_dir = self.project_root / ".project" / "pilot" / "npv-finance" / "akus"
        
        for aku_file in pilot_dir.rglob("*.json"):
            try:
                with open(aku_file) as f:
                    aku_data = json.load(f)
                
                aku_id = aku_data.get("@id", aku_file.stem)
                last_assessment = scores.get("akus", {}).get(aku_id)
                
                # Check triggers
                triggers = self.check_reassessment_triggers(aku_file, aku_data, last_assessment)
                
                if triggers:
                    priority = self.calculate_priority_score(aku_id, aku_data, last_assessment)
                    
                    queue.append({
                        "aku_id": aku_id,
                        "path": str(aku_file.relative_to(self.project_root)),
                        "priority_score": priority,
                        "triggers": triggers,
                        "last_assessment": last_assessment.get("date") if last_assessment else None,
                        "last_grade": last_assessment.get("grade") if last_assessment else None
                    })
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Warning: Could not process {aku_file}: {e}")
        
        # Sort by priority score (descending)
        queue.sort(key=lambda x: x["priority_score"], reverse=True)
        
        return queue
    
    def record_assessment(self, aku_id: str, aku_path: Path, 
                         assessment_result: Dict) -> None:
        """Record an assessment result in the quality tracking system."""
        scores = self.load_quality_scores()
        log = self.load_reassessment_log()
        
        # Update quality scores
        if "akus" not in scores:
            scores["akus"] = {}
        
        # Add history tracking
        if aku_id not in scores["akus"]:
            scores["akus"][aku_id] = {"history": []}
        
        aku_record = scores["akus"][aku_id]
        
        # Add current assessment to history
        if "history" not in aku_record:
            aku_record["history"] = []
        
        current_assessment = {
            "date": datetime.now(timezone.utc).isoformat() + "Z",
            "grade": assessment_result.get("grade", "C"),
            "cqs": assessment_result.get("cqs", 0.0),
            "content_hash": self.calculate_content_hash(aku_path),
            "dimension_scores": assessment_result.get("dimension_scores", {})
        }
        
        aku_record["history"].append(current_assessment)
        
        # Keep only last 10 assessments in history
        if len(aku_record["history"]) > 10:
            aku_record["history"] = aku_record["history"][-10:]
        
        # Update current assessment
        aku_record["current"] = current_assessment
        aku_record["assessment_count"] = len(aku_record["history"])
        
        # Update log
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
            "aku_id": aku_id,
            "path": str(aku_path),
            "grade": assessment_result.get("grade"),
            "cqs": assessment_result.get("cqs"),
            "action": "assessment"
        }
        log["assessments"].append(log_entry)
        
        # Save updates
        self.save_quality_scores(scores)
        self.save_reassessment_log(log)
    
    def get_quality_history(self, aku_id: str) -> List[Dict]:
        """Get assessment history for a specific AKU."""
        scores = self.load_quality_scores()
        aku_record = scores.get("akus", {}).get(aku_id, {})
        return aku_record.get("history", [])
    
    def generate_report(self) -> str:
        """Generate reassessment report."""
        scores = self.load_quality_scores()
        queue = self.get_priority_queue()
        
        report = []
        report.append("=" * 60)
        report.append("AKU Reassessment Report")
        report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}Z")
        report.append("=" * 60)
        
        # Summary statistics
        akus = scores.get("akus", {})
        total_akus = len(akus)
        
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "unassessed": 0}
        for aku_id, record in akus.items():
            current = record.get("current", {})
            grade = current.get("grade", "unassessed")
            if grade and grade[0].upper() in grade_counts:
                grade_counts[grade[0].upper()] += 1
            else:
                grade_counts["unassessed"] += 1
        
        report.append("\n📊 GRADE DISTRIBUTION")
        report.append("-" * 40)
        for grade, count in sorted(grade_counts.items()):
            bar = "█" * count
            report.append(f"  {grade}: {count:3d} {bar}")
        
        # Priority queue summary
        report.append("\n⚡ PRIORITY QUEUE (Top 10)")
        report.append("-" * 40)
        for i, item in enumerate(queue[:10], 1):
            report.append(f"  {i}. {item['aku_id']}")
            report.append(f"     Priority: {item['priority_score']:.3f}")
            report.append(f"     Last Grade: {item['last_grade'] or 'N/A'}")
            report.append(f"     Triggers: {', '.join(item['triggers'][:2])}")
        
        # Reassessment schedule
        report.append("\n📅 REASSESSMENT SCHEDULE")
        report.append("-" * 40)
        for grade, days in self.config["scheduled_intervals"].items():
            report.append(f"  {grade}: Every {days} days")
        
        # Action items
        report.append("\n✅ RECOMMENDED ACTIONS")
        report.append("-" * 40)
        
        urgent = [q for q in queue if q["priority_score"] >= 0.7]
        moderate = [q for q in queue if 0.4 <= q["priority_score"] < 0.7]
        low = [q for q in queue if q["priority_score"] < 0.4]
        
        report.append(f"  🔴 Urgent ({len(urgent)} AKUs): Reassess within 7 days")
        report.append(f"  🟡 Moderate ({len(moderate)} AKUs): Reassess within 30 days")
        report.append(f"  🟢 Low ({len(low)} AKUs): Reassess at scheduled interval")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)
    
    def run_scheduled_reassessments(self, max_assessments: int = 10) -> List[Dict]:
        """
        Run scheduled reassessments for top priority AKUs.
        
        Returns list of assessment results.
        """
        queue = self.get_priority_queue()
        results = []
        
        for item in queue[:max_assessments]:
            aku_path = self.project_root / item["path"]
            
            try:
                with open(aku_path) as f:
                    aku_data = json.load(f)
                
                # Run comprehensive assessment
                # This would integrate with comprehensive_quality_assessment.py
                print(f"Assessing: {item['aku_id']}")
                
                # Placeholder assessment result
                result = {
                    "aku_id": item["aku_id"],
                    "path": item["path"],
                    "status": "pending",
                    "triggers": item["triggers"]
                }
                
                results.append(result)
                
            except Exception as e:
                results.append({
                    "aku_id": item["aku_id"],
                    "status": "error",
                    "error": str(e)
                })
        
        return results


def main():
    """Main entry point for reassessment tool."""
    import argparse
    
    parser = argparse.ArgumentParser(description="AKU Reassessment Tool")
    parser.add_argument("--schedule", action="store_true",
                       help="Run scheduled reassessments")
    parser.add_argument("--aku", type=str,
                       help="Reassess specific AKU by path")
    parser.add_argument("--priority-queue", action="store_true",
                       help="Show priority queue")
    parser.add_argument("--history", type=str,
                       help="Show quality history for AKU ID")
    parser.add_argument("--report", action="store_true",
                       help="Generate reassessment report")
    parser.add_argument("--max", type=int, default=10,
                       help="Maximum assessments to run (default: 10)")
    
    args = parser.parse_args()
    
    tool = ReassessmentTool()
    
    if args.report:
        print(tool.generate_report())
    
    elif args.priority_queue:
        queue = tool.get_priority_queue()
        print(f"Priority Queue ({len(queue)} AKUs needing reassessment):\n")
        for i, item in enumerate(queue[:20], 1):
            print(f"{i:2d}. {item['aku_id']}")
            print(f"    Priority: {item['priority_score']:.3f} | "
                  f"Last: {item['last_grade'] or 'N/A'} | "
                  f"Triggers: {len(item['triggers'])}")
    
    elif args.history:
        history = tool.get_quality_history(args.history)
        if history:
            print(f"Quality History for {args.history}:\n")
            for entry in history:
                print(f"  {entry['date']}: Grade {entry['grade']} (CQS: {entry['cqs']:.2f})")
        else:
            print(f"No history found for {args.history}")
    
    elif args.schedule:
        results = tool.run_scheduled_reassessments(max_assessments=args.max)
        print(f"Processed {len(results)} reassessments")
        for r in results:
            print(f"  {r['aku_id']}: {r['status']}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
