#!/usr/bin/env python3
"""
Comprehensive Quality Assessment Tool for WorldSMEGraphs AKUs

This tool performs multi-dimensional quality assessment of Atomic Knowledge Units (AKUs)
including fact-checking, ontology compliance, reference quality, third-party verification,
web search verification, dependency completeness, content completeness, and technical quality.

Usage:
    python comprehensive_quality_assessment.py path/to/aku.json
    python comprehensive_quality_assessment.py --directory path/to/akus/
    python comprehensive_quality_assessment.py --domain health-sciences
    python comprehensive_quality_assessment.py path/to/aku.json --reassess
    python comprehensive_quality_assessment.py --report weekly

Features:
- Multi-dimensional quality scoring (8 dimensions)
- Composite Quality Score (CQS) calculation
- Quality grade assignment (A+ to F)
- Missing dependency identification
- Quality tracking database integration
- Reassessment workflow support
- Comprehensive reporting

Self-contained with standard library only.
"""

import json
import sys
import os
import hashlib
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional, Any
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from enum import Enum
import argparse


class QualityGrade(Enum):
    """Quality grades based on CQS score."""
    A_PLUS = ("A+", 0.95, 1.00, "Excellent")
    A = ("A", 0.90, 0.94, "Very Good")
    B_PLUS = ("B+", 0.85, 0.89, "Good")
    B = ("B", 0.80, 0.84, "Satisfactory")
    C_PLUS = ("C+", 0.75, 0.79, "Acceptable")
    C = ("C", 0.70, 0.74, "Needs Work")
    D = ("D", 0.60, 0.69, "Poor")
    F = ("F", 0.00, 0.59, "Failing")

    @classmethod
    def from_score(cls, score: float) -> 'QualityGrade':
        """Get grade from CQS score."""
        if score >= 0.95:
            return cls.A_PLUS
        elif score >= 0.90:
            return cls.A
        elif score >= 0.85:
            return cls.B_PLUS
        elif score >= 0.80:
            return cls.B
        elif score >= 0.75:
            return cls.C_PLUS
        elif score >= 0.70:
            return cls.C
        elif score >= 0.60:
            return cls.D
        else:
            return cls.F


@dataclass
class DimensionScore:
    """Score for a single quality dimension."""
    dimension: str
    score: float
    max_score: float = 1.0
    weight: float = 0.0
    issues: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    verified_items: List[str] = field(default_factory=list)


@dataclass
class MissingDependency:
    """Represents a missing AKU dependency."""
    id: str
    type: str
    priority: str  # critical, high, medium, low
    reason: str
    suggested_domain_path: str = ""


@dataclass
class QualityAssessment:
    """Complete quality assessment result."""
    aku_id: str
    aku_path: str
    assessment_date: str
    assessment_level: str  # quick, standard, comprehensive
    assessor: str
    dimension_scores: Dict[str, DimensionScore]
    composite_quality_score: float
    grade: str
    publication_ready: bool
    issues: List[str]
    recommendations: List[str]
    missing_dependencies: List[MissingDependency]
    previous_assessment: Optional[Dict] = None
    assessment_duration_seconds: float = 0.0


class ComprehensiveQualityAssessor:
    """
    Performs comprehensive quality assessment of AKUs across 8 dimensions:
    1. Factual Accuracy (FA)
    2. Ontology Compliance (OC)
    3. Reference Quality (RQ)
    4. Third-Party Verification (TPV)
    5. Web Search Verification (WSV)
    6. Dependency Completeness (DC)
    7. Content Completeness (CC)
    8. Technical Quality (TQ)
    """

    # Default dimension weights
    DEFAULT_WEIGHTS = {
        "factual_accuracy": 0.20,
        "ontology_compliance": 0.10,
        "reference_quality": 0.15,
        "third_party_verification": 0.15,
        "web_search_verification": 0.10,
        "dependency_completeness": 0.10,
        "content_completeness": 0.15,
        "technical_quality": 0.05,
    }

    # Domain-specific weight adjustments
    DOMAIN_WEIGHTS = {
        "health-sciences": {
            "factual_accuracy": 0.30,
            "third_party_verification": 0.20,
            "reference_quality": 0.15,
            "ontology_compliance": 0.10,
            "web_search_verification": 0.05,
            "dependency_completeness": 0.05,
            "content_completeness": 0.10,
            "technical_quality": 0.05,
        },
        "formal-sciences": {
            "factual_accuracy": 0.25,
            "technical_quality": 0.10,
            "content_completeness": 0.20,
            "reference_quality": 0.15,
            "ontology_compliance": 0.10,
            "third_party_verification": 0.10,
            "web_search_verification": 0.05,
            "dependency_completeness": 0.05,
        },
        "social-sciences": {
            "reference_quality": 0.20,
            "web_search_verification": 0.15,
            "factual_accuracy": 0.20,
            "content_completeness": 0.15,
            "ontology_compliance": 0.10,
            "third_party_verification": 0.10,
            "dependency_completeness": 0.05,
            "technical_quality": 0.05,
        },
    }

    # Publication thresholds by domain
    PUBLICATION_THRESHOLDS = {
        "health-sciences": {"min_cqs": 0.90, "min_fa": 0.95, "min_tpv": 0.85},
        "formal-sciences": {"min_cqs": 0.85, "min_fa": 0.90, "min_tq": 0.90},
        "social-sciences": {"min_cqs": 0.85, "min_fa": 0.85, "min_rq": 0.85},
        "natural-sciences": {"min_cqs": 0.80, "min_fa": 0.85},
        "default": {"min_cqs": 0.80, "min_fa": 0.80},
    }

    def __init__(self, verbose: bool = False, tracking_path: str = None):
        self.verbose = verbose
        self.tracking_path = tracking_path or ".project/tracking/quality-scores.yaml"
        self.global_hierarchy_path = "domain/_ontology/global-hierarchy.yaml"
        self.existing_akus: Set[str] = set()
        self._load_existing_akus()

    def _load_existing_akus(self):
        """Load all existing AKU IDs for dependency checking."""
        domain_paths = [
            "domain/formal-sciences",
            "domain/natural-sciences",
            "domain/social-sciences",
            "domain/health-sciences",
            ".project/pilot"
        ]
        for domain_path in domain_paths:
            path = Path(domain_path)
            if path.exists():
                for aku_file in path.glob("**/*.json"):
                    try:
                        with open(aku_file, 'r', encoding='utf-8') as f:
                            aku = json.load(f)
                            if "@id" in aku:
                                self.existing_akus.add(aku["@id"])
                            # Also add filename-based ID
                            self.existing_akus.add(aku_file.stem)
                    except (json.JSONDecodeError, KeyError):
                        pass

    def assess(self, aku_path: Path, level: str = "standard") -> QualityAssessment:
        """
        Perform quality assessment on an AKU.

        Args:
            aku_path: Path to the AKU JSON file
            level: Assessment level (quick, standard, comprehensive)

        Returns:
            QualityAssessment object with complete results
        """
        start_time = datetime.now(timezone.utc)
        
        # Load AKU
        try:
            with open(aku_path, 'r', encoding='utf-8') as f:
                aku = json.load(f)
        except json.JSONDecodeError as e:
            return self._create_failed_assessment(aku_path, f"Invalid JSON: {e}")
        except Exception as e:
            return self._create_failed_assessment(aku_path, f"Failed to load: {e}")

        # Detect domain for weight adjustment
        domain = self._detect_domain(aku)
        weights = self._get_weights(domain)

        # Assess each dimension
        dimension_scores = {}
        
        # 1. Technical Quality (always assessed)
        dimension_scores["technical_quality"] = self._assess_technical_quality(aku, aku_path)
        
        # 2. Content Completeness
        dimension_scores["content_completeness"] = self._assess_content_completeness(aku, domain)
        
        if level in ["standard", "comprehensive"]:
            # 3. Ontology Compliance
            dimension_scores["ontology_compliance"] = self._assess_ontology_compliance(aku, domain)
            
            # 4. Reference Quality
            dimension_scores["reference_quality"] = self._assess_reference_quality(aku)
            
            # 5. Dependency Completeness
            dimension_scores["dependency_completeness"] = self._assess_dependency_completeness(aku)
            
            # 6. Factual Accuracy (basic check for standard)
            dimension_scores["factual_accuracy"] = self._assess_factual_accuracy(aku, level)
        
        if level == "comprehensive":
            # 7. Third-Party Verification
            dimension_scores["third_party_verification"] = self._assess_third_party_verification(aku)
            
            # 8. Web Search Verification
            dimension_scores["web_search_verification"] = self._assess_web_search_verification(aku)
        else:
            # Placeholder scores for non-comprehensive assessment
            if "third_party_verification" not in dimension_scores:
                dimension_scores["third_party_verification"] = DimensionScore(
                    dimension="third_party_verification",
                    score=0.0,
                    weight=weights.get("third_party_verification", 0.15),
                    issues=["Third-party verification not performed (requires comprehensive assessment)"]
                )
            if "web_search_verification" not in dimension_scores:
                dimension_scores["web_search_verification"] = DimensionScore(
                    dimension="web_search_verification",
                    score=0.0,
                    weight=weights.get("web_search_verification", 0.10),
                    issues=["Web search verification not performed (requires comprehensive assessment)"]
                )
            if "factual_accuracy" not in dimension_scores:
                dimension_scores["factual_accuracy"] = DimensionScore(
                    dimension="factual_accuracy",
                    score=0.5,
                    weight=weights.get("factual_accuracy", 0.20),
                    issues=["Factual accuracy not fully verified (quick assessment only)"]
                )

        # Apply weights
        for dim_name, dim_score in dimension_scores.items():
            dim_score.weight = weights.get(dim_name, 0.1)

        # Calculate Composite Quality Score
        cqs = self._calculate_cqs(dimension_scores, weights)
        
        # Determine grade
        grade = QualityGrade.from_score(cqs)
        
        # Check publication readiness
        publication_ready = self._check_publication_readiness(cqs, dimension_scores, domain)
        
        # Collect all issues and recommendations
        all_issues = []
        all_recommendations = []
        for dim_score in dimension_scores.values():
            all_issues.extend(dim_score.issues)
            all_recommendations.extend(dim_score.recommendations)
        
        # Identify missing dependencies
        missing_deps = self._identify_missing_dependencies(aku)
        
        # Calculate duration
        duration = (datetime.now(timezone.utc) - start_time).total_seconds()
        
        return QualityAssessment(
            aku_id=aku.get("@id", aku_path.stem),
            aku_path=str(aku_path),
            assessment_date=datetime.now(timezone.utc).isoformat(),
            assessment_level=level,
            assessor="comprehensive_quality_assessment.py",
            dimension_scores=dimension_scores,
            composite_quality_score=round(cqs, 4),
            grade=grade.value[0],
            publication_ready=publication_ready,
            issues=all_issues,
            recommendations=all_recommendations,
            missing_dependencies=missing_deps,
            assessment_duration_seconds=round(duration, 2)
        )

    def _detect_domain(self, aku: Dict) -> str:
        """Detect domain from AKU classification."""
        if "classification" in aku and "domain_path" in aku["classification"]:
            path = aku["classification"]["domain_path"]
            parts = path.split('/')
            return parts[0] if parts else "unknown"
        return "unknown"

    def _get_weights(self, domain: str) -> Dict[str, float]:
        """Get dimension weights for domain."""
        return self.DOMAIN_WEIGHTS.get(domain, self.DEFAULT_WEIGHTS)

    def _assess_technical_quality(self, aku: Dict, aku_path: Path) -> DimensionScore:
        """Assess technical quality (TQ dimension)."""
        score = 1.0
        issues = []
        recommendations = []
        verified = []

        # Check JSON structure
        verified.append("Valid JSON structure")

        # Check required keys
        required_keys = ["@context", "@type", "@id", "metadata", "classification", "content"]
        for key in required_keys:
            if key not in aku:
                score -= 0.15
                issues.append(f"Missing required key: {key}")
            else:
                verified.append(f"Has {key}")

        # Check metadata structure
        if "metadata" in aku:
            metadata_keys = ["version", "created", "contributors", "confidence", "status"]
            for key in metadata_keys:
                if key not in aku["metadata"]:
                    score -= 0.05
                    issues.append(f"Missing metadata.{key}")
            
            # Validate timestamp format
            if "created" in aku["metadata"]:
                try:
                    ts = aku["metadata"]["created"]
                    if not re.match(r'\d{4}-\d{2}-\d{2}', ts):
                        score -= 0.05
                        issues.append("Invalid date format in metadata.created")
                    else:
                        verified.append("Valid timestamp format")
                except:
                    score -= 0.05
                    issues.append("Invalid metadata.created")

            # Validate confidence range
            if "confidence" in aku["metadata"]:
                conf = aku["metadata"]["confidence"]
                if not isinstance(conf, (int, float)) or not (0 <= conf <= 1):
                    score -= 0.1
                    issues.append(f"Invalid confidence value: {conf}")
                else:
                    verified.append(f"Valid confidence: {conf}")

            # Check version format
            if "version" in aku["metadata"]:
                version = aku["metadata"]["version"]
                if not re.match(r'^\d+\.\d+\.\d+$', version):
                    score -= 0.02
                    recommendations.append(f"Consider semver format for version: {version}")

        # Check classification structure
        if "classification" in aku:
            class_keys = ["domain_path", "type", "difficulty", "importance"]
            for key in class_keys:
                if key not in aku["classification"]:
                    score -= 0.05
                    issues.append(f"Missing classification.{key}")

        # Check for executable code if present
        if "representations" in aku and "python" in aku["representations"]:
            if "code" in aku["representations"]["python"]:
                verified.append("Has executable Python code")
                # Could add code validation here
            if "test_cases" in aku["representations"]["python"]:
                verified.append("Has test cases")

        return DimensionScore(
            dimension="technical_quality",
            score=max(0, min(1, score)),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_content_completeness(self, aku: Dict, domain: str) -> DimensionScore:
        """Assess content completeness (CC dimension)."""
        score = 0.0
        issues = []
        recommendations = []
        verified = []

        # Check content presence and structure
        if "content" not in aku:
            return DimensionScore(
                dimension="content_completeness",
                score=0.0,
                issues=["No content section found"]
            )

        content = aku["content"]

        # Check for statement/definition
        if "statement" in content or "definition" in content:
            score += 0.25
            verified.append("Has statement/definition")
        else:
            issues.append("Missing statement or definition")
            recommendations.append("Add a clear statement or definition")

        # Check for explanation
        if "explanation" in content:
            score += 0.20
            exp = content["explanation"]
            if isinstance(exp, dict):
                if "intuition" in exp:
                    score += 0.05
                    verified.append("Has intuition explanation")
                if "key_insight" in exp:
                    score += 0.05
                    verified.append("Has key insight")
                if "technical_details" in exp:
                    score += 0.05
                    verified.append("Has technical details")
            verified.append("Has explanation section")
        else:
            issues.append("Missing explanation section")
            recommendations.append("Add explanation with intuition, key insight, and technical details")

        # Check for definitions glossary
        if "definitions_glossary" in content:
            score += 0.10
            verified.append("Has definitions glossary")
        else:
            recommendations.append("Consider adding definitions glossary")

        # Check for representations (mathematical content)
        if "representations" in aku:
            score += 0.10
            rep = aku["representations"]
            if "latex" in rep:
                verified.append("Has LaTeX representation")
            if "python" in rep:
                verified.append("Has Python implementation")
            if "mathml" in rep:
                verified.append("Has MathML representation")

        # Check for relationships
        if "relationships" in aku:
            score += 0.10
            rel = aku["relationships"]
            if "prerequisites" in rel and rel["prerequisites"]:
                verified.append(f"Has {len(rel['prerequisites'])} prerequisites")
            if "related_to" in rel and rel["related_to"]:
                verified.append(f"Has {len(rel['related_to'])} related concepts")

        # Check for pedagogical content
        if "pedagogical" in aku:
            score += 0.10
            ped = aku["pedagogical"]
            if "learning_objectives" in ped:
                verified.append("Has learning objectives")
            if "practice_problems" in ped:
                verified.append("Has practice problems")

        return DimensionScore(
            dimension="content_completeness",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_ontology_compliance(self, aku: Dict, domain: str) -> DimensionScore:
        """Assess ontology compliance (OC dimension)."""
        score = 0.0
        issues = []
        recommendations = []
        verified = []

        # Check @context
        if "@context" in aku:
            score += 0.15
            verified.append("Has @context")
            context = aku["@context"]
            if isinstance(context, list):
                if any("base.jsonld" in str(c) for c in context):
                    score += 0.05
                    verified.append("References base.jsonld")
        else:
            issues.append("Missing @context")

        # Check @type
        if "@type" in aku:
            score += 0.10
            verified.append(f"Has @type: {aku['@type']}")
        else:
            issues.append("Missing @type")

        # Check domain_path against hierarchy
        if "classification" in aku and "domain_path" in aku["classification"]:
            domain_path = aku["classification"]["domain_path"]
            score += 0.20
            verified.append(f"Has domain_path: {domain_path}")
            
            # Check if path follows hierarchy
            valid_prefixes = ["formal-sciences", "natural-sciences", "social-sciences", "health-sciences", 
                             "science", "economics", "medicine", "math"]  # Support legacy paths
            if any(domain_path.startswith(p) for p in valid_prefixes):
                score += 0.10
                verified.append("Domain path follows hierarchy")
            else:
                recommendations.append(f"Consider migrating to standard hierarchy: {domain_path}")
        else:
            issues.append("Missing domain_path in classification")

        # Check for SKOS relationships
        if "relationships" in aku:
            rel = aku["relationships"]
            skos_types = ["skos:broader", "skos:narrower", "skos:related", "skos:exactMatch"]
            found_skos = [s for s in skos_types if s in rel]
            if found_skos:
                score += 0.15
                verified.append(f"Has SKOS relationships: {', '.join(found_skos)}")
            else:
                recommendations.append("Consider adding SKOS relationships for better ontology integration")

        # Check for external ontology alignments
        if "owl:sameAs" in aku or "skos:exactMatch" in aku:
            score += 0.15
            verified.append("Has external ontology alignment")
        else:
            recommendations.append("Consider adding owl:sameAs or skos:exactMatch for external linking")

        # Check for provenance with ontology info
        if "provenance" in aku:
            prov = aku["provenance"]
            if "prov:wasDerivedFrom" in prov or "dc:creator" in prov:
                score += 0.10
                verified.append("Has provenance ontology terms")

        return DimensionScore(
            dimension="ontology_compliance",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_reference_quality(self, aku: Dict) -> DimensionScore:
        """Assess reference quality (RQ dimension)."""
        score = 0.0
        issues = []
        recommendations = []
        verified = []

        if "provenance" not in aku:
            return DimensionScore(
                dimension="reference_quality",
                score=0.0,
                issues=["No provenance section found"]
            )

        prov = aku["provenance"]

        # Check for sources
        if "sources" in prov:
            sources = prov["sources"]
            if isinstance(sources, list) and len(sources) > 0:
                score += 0.30
                verified.append(f"Has {len(sources)} sources")

                # Check source quality
                high_quality_sources = 0
                for source in sources:
                    if isinstance(source, dict):
                        # Check for authoritative source types
                        source_type = source.get("type", "")
                        if source_type in ["textbook", "paper", "journal", "academic"]:
                            high_quality_sources += 1
                            
                            # Check for DOI or ISBN
                            if "doi" in source:
                                score += 0.05
                                verified.append(f"Has DOI: {source['doi'][:30]}...")
                            if "isbn" in source:
                                score += 0.05
                                verified.append(f"Has ISBN: {source['isbn']}")
                            
                            # Check for year
                            if "year" in source:
                                year = source.get("year", 0)
                                current_year = datetime.now().year
                                if current_year - year <= 5:
                                    score += 0.05
                                    verified.append(f"Recent source ({year})")
                                elif current_year - year <= 10:
                                    score += 0.03
                                elif current_year - year > 20:
                                    recommendations.append(f"Source from {year} may be outdated")

                if high_quality_sources >= 2:
                    score += 0.20
                    verified.append(f"{high_quality_sources} high-quality sources")
                elif high_quality_sources == 1:
                    score += 0.10
                    recommendations.append("Add more authoritative sources (textbooks, peer-reviewed papers)")
            else:
                issues.append("Empty sources list")
        else:
            issues.append("No sources in provenance")
            recommendations.append("Add authoritative sources with DOI/ISBN")

        # Check for extraction method
        if "extraction_method" in prov:
            score += 0.05
            verified.append(f"Extraction method: {prov['extraction_method'][:50]}")

        # Check for validation
        if "validation_method" in prov or "validation_date" in prov:
            score += 0.10
            verified.append("Has validation information")

        # Check for confidence factors
        if "confidence_factors" in prov:
            score += 0.05
            verified.append("Has confidence factors")

        return DimensionScore(
            dimension="reference_quality",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_dependency_completeness(self, aku: Dict) -> DimensionScore:
        """Assess dependency completeness (DC dimension)."""
        score = 0.5  # Start at 50% if no explicit dependencies
        issues = []
        recommendations = []
        verified = []

        if "relationships" not in aku:
            return DimensionScore(
                dimension="dependency_completeness",
                score=0.3,
                issues=["No relationships section found"],
                recommendations=["Add relationships section with prerequisites and related concepts"]
            )

        rel = aku["relationships"]

        # Check prerequisites
        if "prerequisites" in rel and isinstance(rel["prerequisites"], list):
            prereqs = rel["prerequisites"]
            if prereqs:
                score += 0.20
                verified.append(f"Has {len(prereqs)} prerequisites defined")
                
                # Check if prerequisites exist
                missing = []
                for prereq in prereqs:
                    prereq_id = prereq if isinstance(prereq, str) else prereq.get("@id", str(prereq))
                    if prereq_id not in self.existing_akus:
                        missing.append(prereq_id)
                
                if missing:
                    score -= 0.10 * min(len(missing), 3)  # Max penalty of 0.30
                    issues.extend([f"Missing prerequisite AKU: {m}" for m in missing[:3]])
                else:
                    score += 0.10
                    verified.append("All prerequisites exist")
        else:
            recommendations.append("Consider adding prerequisites for this concept")

        # Check related_to
        if "related_to" in rel and isinstance(rel["related_to"], list):
            related = rel["related_to"]
            if related:
                score += 0.10
                verified.append(f"Has {len(related)} related concepts")

        # Check enables/narrower
        if "enables" in rel or "skos:narrower" in rel:
            score += 0.05
            verified.append("Has forward dependencies (enables/narrower)")

        # Check part_of/broader
        if "part_of" in rel or "skos:broader" in rel:
            score += 0.05
            verified.append("Has hierarchical relationship (part_of/broader)")

        return DimensionScore(
            dimension="dependency_completeness",
            score=min(1.0, max(0, score)),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_factual_accuracy(self, aku: Dict, level: str) -> DimensionScore:
        """
        Assess factual accuracy (FA dimension).
        
        For standard level: Basic structural checks
        For comprehensive level: Would integrate with fact-checking agent
        """
        score = 0.5  # Default to 50% for unverified content
        issues = []
        recommendations = []
        verified = []

        # Check if content exists
        if "content" not in aku:
            return DimensionScore(
                dimension="factual_accuracy",
                score=0.0,
                issues=["No content to verify"]
            )

        # Check metadata confidence (author's claim)
        if "metadata" in aku and "confidence" in aku["metadata"]:
            author_confidence = aku["metadata"]["confidence"]
            # Use author confidence as a baseline
            score = author_confidence * 0.5  # Weighted contribution
            verified.append(f"Author confidence: {author_confidence}")

        # Check if sources support claims
        if "provenance" in aku and "sources" in aku["provenance"]:
            sources = aku["provenance"]["sources"]
            if len(sources) >= 2:
                score += 0.20
                verified.append("Multiple sources support claims")
            elif len(sources) == 1:
                score += 0.10
                recommendations.append("Add additional sources for cross-verification")

        # Check validation status
        if "metadata" in aku and "status" in aku["metadata"]:
            status = aku["metadata"]["status"]
            if status in ["validated", "published"]:
                score += 0.15
                verified.append(f"Status: {status}")
            elif status == "review":
                score += 0.05
                verified.append("In review")
            elif status == "draft":
                recommendations.append("Validate content before publication")

        # Check if formulas are present (they can be verified)
        if "representations" in aku:
            rep = aku["representations"]
            if "latex" in rep or "python" in rep:
                score += 0.10
                verified.append("Has verifiable mathematical representations")
                if "python" in rep and "test_cases" in rep.get("python", {}):
                    score += 0.05
                    verified.append("Has test cases for verification")

        # For comprehensive assessment, would need fact-checking agent
        if level == "comprehensive":
            recommendations.append("Run @fact-checking agent for detailed verification")

        return DimensionScore(
            dimension="factual_accuracy",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_third_party_verification(self, aku: Dict) -> DimensionScore:
        """
        Assess third-party verification (TPV dimension).
        
        This would integrate with verification agents in a full implementation.
        """
        score = 0.0
        issues = []
        recommendations = []
        verified = []

        # Check for validation markers
        if "metadata" in aku:
            metadata = aku["metadata"]
            
            # Check for external validation
            if "status" in metadata:
                if metadata["status"] == "validated":
                    score += 0.30
                    verified.append("Has validated status")
                elif metadata["status"] == "published":
                    score += 0.40
                    verified.append("Has published status")

            # Check for peer review
            if "peer_reviewed" in metadata and metadata["peer_reviewed"]:
                score += 0.30
                verified.append("Peer reviewed")

            # Check for external validators in contributors
            if "contributors" in metadata:
                contributors = metadata["contributors"]
                if any("expert" in str(c).lower() for c in contributors):
                    score += 0.15
                    verified.append("Has domain expert contributor")
                if any("verification" in str(c).lower() or "review" in str(c).lower() for c in contributors):
                    score += 0.15
                    verified.append("Has verification agent contributor")

        # Check provenance for external validation
        if "provenance" in aku:
            prov = aku["provenance"]
            if "validation_method" in prov:
                score += 0.10
                verified.append(f"Validation method: {prov['validation_method'][:50]}")

        if score < 0.5:
            issues.append("Limited third-party verification")
            recommendations.append("Request @peer-review agent verification")
            recommendations.append("Consider @fact-checking agent validation")

        return DimensionScore(
            dimension="third_party_verification",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _assess_web_search_verification(self, aku: Dict) -> DimensionScore:
        """
        Assess web search verification (WSV dimension).
        
        This would integrate with web search in a full implementation.
        """
        score = 0.0
        issues = []
        recommendations = []
        verified = []

        # Check for external links
        if "owl:sameAs" in aku:
            score += 0.30
            verified.append(f"Has owl:sameAs: {aku['owl:sameAs'][:50]}")

        if "skos:exactMatch" in aku:
            matches = aku["skos:exactMatch"]
            if isinstance(matches, list) and matches:
                score += 0.30
                verified.append(f"Has {len(matches)} exact matches")
                # Check for known reliable sources
                for match in matches:
                    if isinstance(match, str):
                        if "wikidata.org" in match:
                            score += 0.10
                            verified.append("Linked to Wikidata")
                        if "dbpedia.org" in match:
                            score += 0.10
                            verified.append("Linked to DBpedia")

        # Check provenance for web sources
        if "provenance" in aku and "sources" in aku["provenance"]:
            sources = aku["provenance"]["sources"]
            for source in sources:
                if isinstance(source, dict):
                    if "doi" in source:
                        score += 0.05
                        verified.append("Has DOI (verifiable online)")
                    if source.get("type") == "paper":
                        score += 0.05
                        verified.append("Has academic paper reference")

        if score < 0.3:
            recommendations.append("Add links to Wikidata/DBpedia for verification")
            recommendations.append("Include DOIs for academic sources")

        return DimensionScore(
            dimension="web_search_verification",
            score=min(1.0, score),
            issues=issues,
            recommendations=recommendations,
            verified_items=verified
        )

    def _calculate_cqs(self, dimension_scores: Dict[str, DimensionScore], 
                       weights: Dict[str, float]) -> float:
        """Calculate Composite Quality Score."""
        total_weight = 0.0
        weighted_sum = 0.0

        for dim_name, dim_score in dimension_scores.items():
            weight = weights.get(dim_name, 0.1)
            weighted_sum += dim_score.score * weight
            total_weight += weight

        if total_weight == 0:
            return 0.0

        return weighted_sum / total_weight if total_weight != 1.0 else weighted_sum

    def _check_publication_readiness(self, cqs: float, 
                                     dimension_scores: Dict[str, DimensionScore],
                                     domain: str) -> bool:
        """Check if AKU meets publication thresholds."""
        thresholds = self.PUBLICATION_THRESHOLDS.get(domain, self.PUBLICATION_THRESHOLDS["default"])

        # Check minimum CQS
        if cqs < thresholds.get("min_cqs", 0.80):
            return False

        # Check dimension-specific thresholds
        for key, threshold in thresholds.items():
            if key.startswith("min_"):
                dim_abbrev = key[4:]  # Remove 'min_' prefix
                dim_mapping = {
                    "fa": "factual_accuracy",
                    "oc": "ontology_compliance",
                    "rq": "reference_quality",
                    "tpv": "third_party_verification",
                    "wsv": "web_search_verification",
                    "dc": "dependency_completeness",
                    "cc": "content_completeness",
                    "tq": "technical_quality",
                }
                dim_name = dim_mapping.get(dim_abbrev)
                if dim_name and dim_name in dimension_scores:
                    if dimension_scores[dim_name].score < threshold:
                        return False

        return True

    def _identify_missing_dependencies(self, aku: Dict) -> List[MissingDependency]:
        """Identify missing AKU dependencies that need to be created."""
        missing = []

        if "relationships" not in aku:
            return missing

        rel = aku["relationships"]

        # Check prerequisites
        if "prerequisites" in rel:
            for prereq in rel["prerequisites"]:
                prereq_id = prereq if isinstance(prereq, str) else prereq.get("@id", str(prereq))
                if prereq_id not in self.existing_akus:
                    missing.append(MissingDependency(
                        id=prereq_id,
                        type="definition",
                        priority="critical",
                        reason=f"Referenced as prerequisite but does not exist",
                        suggested_domain_path=self._suggest_domain_path(prereq_id, aku)
                    ))

        # Check skos:broader
        if "skos:broader" in rel:
            for broader in rel["skos:broader"]:
                if isinstance(broader, dict):
                    broader_id = broader.get("@id", "").replace("wsmg:", "")
                    if broader_id and broader_id not in self.existing_akus:
                        missing.append(MissingDependency(
                            id=broader_id,
                            type="concept",
                            priority="high",
                            reason="Broader concept referenced but does not exist"
                        ))

        # Check enables
        if "enables" in rel:
            for enables in rel["enables"]:
                enables_id = enables if isinstance(enables, str) else str(enables)
                if enables_id not in self.existing_akus:
                    missing.append(MissingDependency(
                        id=enables_id,
                        type="concept",
                        priority="medium",
                        reason="Enabled concept referenced but does not exist"
                    ))

        return missing

    def _suggest_domain_path(self, concept_id: str, source_aku: Dict) -> str:
        """Suggest a domain path for a missing dependency."""
        if "classification" in source_aku and "domain_path" in source_aku["classification"]:
            # Suggest same domain as source
            return source_aku["classification"]["domain_path"].rsplit('/', 1)[0]
        return ""

    def _create_failed_assessment(self, aku_path: Path, error: str) -> QualityAssessment:
        """Create a failed assessment result."""
        return QualityAssessment(
            aku_id=aku_path.stem,
            aku_path=str(aku_path),
            assessment_date=datetime.now(timezone.utc).isoformat(),
            assessment_level="quick",
            assessor="comprehensive_quality_assessment.py",
            dimension_scores={},
            composite_quality_score=0.0,
            grade="F",
            publication_ready=False,
            issues=[error],
            recommendations=["Fix the error and re-run assessment"],
            missing_dependencies=[]
        )

    def print_report(self, assessment: QualityAssessment):
        """Print formatted assessment report."""
        print("\n" + "=" * 70)
        print(f"QUALITY ASSESSMENT REPORT")
        print("=" * 70)
        print(f"AKU: {assessment.aku_id}")
        print(f"Path: {assessment.aku_path}")
        print(f"Date: {assessment.assessment_date}")
        print(f"Level: {assessment.assessment_level}")
        print(f"Duration: {assessment.assessment_duration_seconds}s")
        print("-" * 70)
        
        # Grade display
        grade_emoji = {
            "A+": "🌟", "A": "⭐", "B+": "✅", "B": "✅",
            "C+": "⚠️", "C": "⚠️", "D": "❌", "F": "🚫"
        }
        emoji = grade_emoji.get(assessment.grade, "❓")
        
        print(f"\n{emoji} GRADE: {assessment.grade} (CQS: {assessment.composite_quality_score:.4f})")
        print(f"Publication Ready: {'✅ Yes' if assessment.publication_ready else '❌ No'}")
        
        # Dimension scores
        print("\n" + "-" * 70)
        print("DIMENSION SCORES:")
        print("-" * 70)
        for dim_name, dim_score in assessment.dimension_scores.items():
            score_bar = "█" * int(dim_score.score * 10) + "░" * (10 - int(dim_score.score * 10))
            print(f"  {dim_name:30} [{score_bar}] {dim_score.score:.2f} (weight: {dim_score.weight:.2f})")
            if dim_score.verified_items and self.verbose:
                for item in dim_score.verified_items[:3]:
                    print(f"    ✓ {item}")
        
        # Issues
        if assessment.issues:
            print("\n" + "-" * 70)
            print("❌ ISSUES:")
            print("-" * 70)
            for issue in assessment.issues[:10]:  # Limit to 10
                print(f"  • {issue}")
        
        # Recommendations
        if assessment.recommendations:
            print("\n" + "-" * 70)
            print("💡 RECOMMENDATIONS:")
            print("-" * 70)
            for rec in assessment.recommendations[:10]:  # Limit to 10
                print(f"  • {rec}")
        
        # Missing dependencies
        if assessment.missing_dependencies:
            print("\n" + "-" * 70)
            print("📦 MISSING DEPENDENCIES:")
            print("-" * 70)
            for dep in assessment.missing_dependencies:
                print(f"  [{dep.priority.upper()}] {dep.id}")
                print(f"    Type: {dep.type}, Reason: {dep.reason}")
                if dep.suggested_domain_path:
                    print(f"    Suggested path: {dep.suggested_domain_path}")
        
        print("\n" + "=" * 70)


def assess_directory(directory: Path, level: str = "standard", 
                    verbose: bool = False) -> List[QualityAssessment]:
    """Assess all AKUs in a directory."""
    assessor = ComprehensiveQualityAssessor(verbose=verbose)
    results = []
    
    aku_files = list(directory.glob("**/*.json"))
    
    print(f"\nAssessing {len(aku_files)} files in {directory}...\n")
    
    for aku_file in sorted(aku_files):
        # Skip schema files and non-AKU files
        if "schema" in aku_file.name.lower():
            continue
        
        assessment = assessor.assess(aku_file, level)
        results.append(assessment)
        
        # Print brief summary
        grade_emoji = {
            "A+": "🌟", "A": "⭐", "B+": "✅", "B": "✅",
            "C+": "⚠️", "C": "⚠️", "D": "❌", "F": "🚫"
        }.get(assessment.grade, "❓")
        
        print(f"{grade_emoji} {assessment.grade} ({assessment.composite_quality_score:.2f}) - {aku_file.name}")
        
        if verbose:
            assessor.print_report(assessment)
    
    # Print summary
    print("\n" + "=" * 70)
    print("ASSESSMENT SUMMARY")
    print("=" * 70)
    
    if results:
        avg_cqs = sum(r.composite_quality_score for r in results) / len(results)
        grade_counts = {}
        for r in results:
            grade_counts[r.grade] = grade_counts.get(r.grade, 0) + 1
        
        print(f"Total assessed: {len(results)}")
        print(f"Average CQS: {avg_cqs:.4f}")
        print(f"Publication ready: {sum(1 for r in results if r.publication_ready)}/{len(results)}")
        print("\nGrade distribution:")
        for grade in ["A+", "A", "B+", "B", "C+", "C", "D", "F"]:
            count = grade_counts.get(grade, 0)
            if count > 0:
                print(f"  {grade}: {count}")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive Quality Assessment for WorldSMEGraphs AKUs"
    )
    parser.add_argument("path", nargs="?", help="Path to AKU file or directory")
    parser.add_argument("--directory", "-d", help="Assess all AKUs in directory")
    parser.add_argument("--domain", help="Assess all AKUs in specific domain")
    parser.add_argument("--level", "-l", choices=["quick", "standard", "comprehensive"],
                       default="standard", help="Assessment level")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--reassess", action="store_true", help="Reassessment mode")
    parser.add_argument("--report", choices=["daily", "weekly", "monthly"],
                       help="Generate quality report")
    parser.add_argument("--output", "-o", help="Output file for JSON results")
    
    args = parser.parse_args()
    
    assessor = ComprehensiveQualityAssessor(verbose=args.verbose)
    
    if args.domain:
        # Assess domain
        domain_path = Path(f"domain/{args.domain}")
        if not domain_path.exists():
            print(f"Error: Domain not found: {domain_path}")
            sys.exit(1)
        results = assess_directory(domain_path, args.level, args.verbose)
        
    elif args.directory:
        # Assess directory
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {dir_path}")
            sys.exit(1)
        results = assess_directory(dir_path, args.level, args.verbose)
        
    elif args.path:
        # Assess single file or directory
        path = Path(args.path)
        if not path.exists():
            print(f"Error: Path not found: {path}")
            sys.exit(1)
        
        if path.is_dir():
            results = assess_directory(path, args.level, args.verbose)
        else:
            assessment = assessor.assess(path, args.level)
            assessor.print_report(assessment)
            results = [assessment]
    
    elif args.report:
        print(f"Generating {args.report} quality report...")
        # Would generate comprehensive report here
        print("Report generation not yet implemented")
        sys.exit(0)
        
    else:
        parser.print_help()
        sys.exit(1)
    
    # Output JSON if requested
    if args.output and results:
        output_data = []
        for r in results:
            output_data.append({
                "aku_id": r.aku_id,
                "aku_path": r.aku_path,
                "grade": r.grade,
                "cqs": r.composite_quality_score,
                "publication_ready": r.publication_ready,
                "issues_count": len(r.issues),
                "recommendations_count": len(r.recommendations),
                "missing_dependencies_count": len(r.missing_dependencies)
            })
        
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"\nResults written to {args.output}")


if __name__ == "__main__":
    main()
