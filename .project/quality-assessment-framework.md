# Comprehensive Quality Assessment Framework for AKUs

> **Version**: 1.0.0
> **Created**: 2026-01-08T16:45:00.000Z
> **Last Updated**: 2026-01-08T16:45:00.000Z
> **Status**: Active

## Executive Summary

This framework defines a comprehensive, multi-dimensional quality assessment system for Atomic Knowledge Units (AKUs) in WorldSMEGraphs. It encompasses all aspects of quality verification including fact-checking, ontology compliance, reference validation, third-party verification, web search verification, and dependency tracking.

## Table of Contents

1. [Quality Dimensions](#1-quality-dimensions)
2. [Assessment Levels](#2-assessment-levels)
3. [Quality Metrics](#3-quality-metrics)
4. [Assessment Workflow](#4-assessment-workflow)
5. [Reassessment Process](#5-reassessment-process)
6. [Quality Tracking](#6-quality-tracking)
7. [Tools and Automation](#7-tools-and-automation)
8. [Agent Integration](#8-agent-integration)
9. [Quality Thresholds](#9-quality-thresholds)
10. [Continuous Improvement](#10-continuous-improvement)

---

## 1. Quality Dimensions

### 1.1 Factual Accuracy (FA)
Ensures all factual claims in the AKU are correct and verifiable.

**Criteria:**
- All statements verified against authoritative sources
- Mathematical formulas verified for correctness
- Numerical values checked for accuracy
- Historical facts validated
- No outdated or deprecated information

**Verification Methods:**
- Cross-reference with peer-reviewed literature
- Mathematical proof verification
- Comparison with authoritative textbooks
- Expert review

**Score Range:** 0.0 - 1.0
- 0.95-1.0: All facts verified with multiple authoritative sources
- 0.85-0.94: Most facts verified, minor gaps
- 0.70-0.84: Some verification gaps or minor inaccuracies
- 0.50-0.69: Significant verification needed
- <0.50: Major accuracy concerns

### 1.2 Ontology Compliance (OC)
Validates adherence to domain ontologies and global hierarchy.

**Criteria:**
- Correct domain_path placement in global hierarchy
- Proper use of SKOS relationships
- Valid JSON-LD context references
- Alignment with external ontologies (SNOMED, FIBO, etc.)
- Cross-domain references properly structured

**Verification Methods:**
- Automated schema validation
- Domain path verification against global-hierarchy.yaml
- Cross-domain link validation
- External ontology mapping verification

**Score Range:** 0.0 - 1.0
- 0.95-1.0: Full ontology compliance
- 0.85-0.94: Minor ontology issues
- 0.70-0.84: Some structural improvements needed
- 0.50-0.69: Significant ontology problems
- <0.50: Major restructuring required

### 1.3 Reference Quality (RQ)
Assesses the quality and completeness of source citations.

**Criteria:**
- All significant claims have citations
- Sources are authoritative and current
- Citations are complete (DOI, ISBN, pages, etc.)
- Source diversity (multiple independent sources)
- Recency of sources (within appropriate timeframe)

**Verification Methods:**
- Citation completeness check
- Source credibility assessment
- DOI/ISBN verification
- Publication date validation

**Score Range:** 0.0 - 1.0
- 0.95-1.0: All claims cited with authoritative, recent sources
- 0.85-0.94: Good coverage with minor gaps
- 0.70-0.84: Adequate but improvable
- 0.50-0.69: Significant citation gaps
- <0.50: Poor source coverage

### 1.4 Third-Party Verification (TPV)
Independent validation by external reviewers or systems.

**Criteria:**
- Verified by domain expert (human or AI agent)
- Cross-checked against authoritative databases
- Validated by independent fact-checking
- Reviewed by peer-review agent

**Verification Methods:**
- Domain expert review
- Peer-review agent validation
- External database cross-reference
- Contrarian agent review

**Score Range:** 0.0 - 1.0
- 0.95-1.0: Multiple independent verifications
- 0.85-0.94: At least one independent verification
- 0.70-0.84: Partial independent verification
- 0.50-0.69: Limited external validation
- <0.50: No independent verification

### 1.5 Web Search Verification (WSV)
Validation through web search and online resources.

**Criteria:**
- Claims verified through multiple web sources
- Wikipedia/encyclopedic sources consulted
- Academic databases searched
- No contradictory authoritative web content
- Current online consensus reflected

**Verification Methods:**
- Structured web search queries
- Academic database search
- Wikipedia cross-reference (as starting point)
- News/current events verification

**Score Range:** 0.0 - 1.0
- 0.95-1.0: Comprehensive web verification
- 0.85-0.94: Good web source coverage
- 0.70-0.84: Adequate web verification
- 0.50-0.69: Limited web verification
- <0.50: No web verification performed

### 1.6 Dependency Completeness (DC)
Ensures all required supporting AKUs exist and are properly linked.

**Criteria:**
- All prerequisite AKUs exist
- Related AKUs are identified and linked
- No broken references
- Cross-domain dependencies satisfied
- Broader/narrower relationships complete

**Verification Methods:**
- Reference resolution check
- Prerequisite existence verification
- Cross-domain link validation
- Relationship completeness analysis

**Score Range:** 0.0 - 1.0
- 0.95-1.0: All dependencies satisfied
- 0.85-0.94: Most dependencies satisfied
- 0.70-0.84: Some missing dependencies
- 0.50-0.69: Significant gaps
- <0.50: Critical dependencies missing

### 1.7 Content Completeness (CC)
Assesses whether the AKU fully covers its topic.

**Criteria:**
- All required sections present
- Content depth appropriate for classification
- Explanations clear and comprehensive
- Examples provided where appropriate
- Edge cases addressed

**Verification Methods:**
- Schema completeness check
- Domain-specific content requirements
- Pedagogical completeness assessment
- Contrarian review for gaps

**Score Range:** 0.0 - 1.0
- 0.95-1.0: Comprehensive coverage
- 0.85-0.94: Good coverage with minor gaps
- 0.70-0.84: Adequate but improvable
- 0.50-0.69: Significant content gaps
- <0.50: Major incompleteness

### 1.8 Technical Quality (TQ)
Validates technical aspects of the AKU.

**Criteria:**
- Valid JSON syntax
- Proper schema compliance
- Valid timestamps (ISO 8601)
- Executable code works correctly
- No malformed content

**Verification Methods:**
- JSON validation
- Schema validation
- Code execution testing
- Timestamp format verification

**Score Range:** 0.0 - 1.0
- 0.95-1.0: Perfect technical quality
- 0.85-0.94: Minor technical issues
- 0.70-0.84: Some technical problems
- 0.50-0.69: Significant technical issues
- <0.50: Major technical problems

---

## 2. Assessment Levels

### 2.1 Quick Assessment
**Purpose:** Fast validation for initial drafts
**Duration:** 2-5 minutes per AKU
**Dimensions Checked:** TQ, CC (basic)
**When to Use:**
- Initial AKU creation
- Minor edits
- Bulk processing

### 2.2 Standard Assessment
**Purpose:** Comprehensive validation for publication-ready AKUs
**Duration:** 15-30 minutes per AKU
**Dimensions Checked:** FA, OC, RQ, CC, TQ
**When to Use:**
- Pre-publication review
- Regular quality audits
- Pilot completion

### 2.3 Comprehensive Assessment
**Purpose:** Deep verification for critical content
**Duration:** 1-2 hours per AKU
**Dimensions Checked:** All 8 dimensions
**When to Use:**
- Medical/safety-critical content
- Foundational AKUs
- Quality concerns identified
- Post-error correction

### 2.4 Peer Review Assessment
**Purpose:** Multi-agent/expert review
**Duration:** 2-4 hours per AKU
**Dimensions Checked:** All dimensions + expert opinions
**When to Use:**
- High-visibility content
- Disputed content
- New domain onboarding
- Quality disputes

---

## 3. Quality Metrics

### 3.1 Composite Quality Score (CQS)
The overall quality score, calculated as weighted average:

```
CQS = (FA × 0.20) + (OC × 0.10) + (RQ × 0.15) + (TPV × 0.15) + 
      (WSV × 0.10) + (DC × 0.10) + (CC × 0.15) + (TQ × 0.05)
```

**Weights Explanation:**
- **Factual Accuracy (0.20):** Most important - content must be correct
- **Content Completeness (0.15):** Full coverage essential
- **Reference Quality (0.15):** Proper sourcing critical
- **Third-Party Verification (0.15):** Independent validation adds credibility
- **Ontology Compliance (0.10):** Structural integrity important
- **Dependency Completeness (0.10):** Relationship quality matters
- **Web Search Verification (0.10):** Additional validation layer
- **Technical Quality (0.05):** Basic requirement, usually automated

### 3.2 Quality Grades

| Grade | CQS Range | Status | Publication Ready |
|-------|-----------|--------|-------------------|
| A+ | 0.95-1.00 | Excellent | Yes - Featured |
| A  | 0.90-0.94 | Very Good | Yes |
| B+ | 0.85-0.89 | Good | Yes |
| B  | 0.80-0.84 | Satisfactory | Yes - Minor improvements suggested |
| C+ | 0.75-0.79 | Acceptable | Conditional - Improvements required |
| C  | 0.70-0.74 | Needs Work | No - Improvements mandatory |
| D  | 0.60-0.69 | Poor | No - Significant rework needed |
| F  | <0.60 | Failing | No - Major revision or rejection |

### 3.3 Domain-Specific Adjustments

Different domains may have adjusted weights:

**Medical Domain:**
- FA: 0.30 (increased - patient safety)
- TPV: 0.20 (increased - clinical validation)
- TQ: 0.05 (standard)

**Mathematical Domain:**
- FA: 0.25 (increased - proof accuracy)
- TQ: 0.10 (increased - executable code)
- CC: 0.20 (increased - derivations)

**Economics Domain:**
- RQ: 0.20 (increased - data sourcing)
- WSV: 0.15 (increased - current data)

---

## 4. Assessment Workflow

### 4.1 Initial Assessment (New AKU)

```
1. CREATION
   └─→ Author creates AKU
       └─→ Run Quick Assessment
           ├─→ PASS → Proceed to Standard Assessment
           └─→ FAIL → Return for corrections

2. STANDARD ASSESSMENT
   └─→ Run automated validations (TQ, OC, DC)
       └─→ Run content analysis (FA, CC, RQ)
           └─→ Calculate initial CQS
               ├─→ CQS ≥ 0.80 → Mark for publication
               ├─→ CQS 0.70-0.79 → Request improvements
               └─→ CQS < 0.70 → Return for rework

3. FINAL REVIEW
   └─→ Human/agent review
       └─→ Approve or request changes
           └─→ Update status to "validated" or "published"
```

### 4.2 Reassessment Workflow

```
1. TRIGGER
   ├─→ Scheduled reassessment
   ├─→ Source update detected
   ├─→ Error reported
   ├─→ Domain changes
   └─→ Manual request

2. REASSESSMENT
   └─→ Run Comprehensive Assessment
       └─→ Compare with previous scores
           └─→ Generate change report
               ├─→ IMPROVED → Update scores, optionally upgrade grade
               ├─→ UNCHANGED → Confirm validity
               └─→ DEGRADED → Flag for review

3. REMEDIATION (if needed)
   └─→ Identify degradation causes
       └─→ Apply corrections
           └─→ Re-run assessment
               └─→ Update tracking database
```

### 4.3 Continuous Monitoring

```
1. DAILY CHECKS
   ├─→ Broken link detection
   ├─→ External source updates
   └─→ Schema compliance

2. WEEKLY AUDITS
   ├─→ Random sample assessment
   ├─→ Domain-specific quality checks
   └─→ Cross-domain consistency

3. MONTHLY REVIEWS
   ├─→ Quality trend analysis
   ├─→ Low-scoring AKU identification
   ├─→ Agent performance evaluation
   └─→ Framework effectiveness review
```

---

## 5. Reassessment Process

### 5.1 Reassessment Triggers

| Trigger | Priority | Reassessment Level |
|---------|----------|-------------------|
| Error report | High | Comprehensive |
| Source update (major) | High | Standard |
| Scheduled (>6 months) | Medium | Standard |
| Domain ontology change | Medium | OC-focused |
| New related AKU created | Low | DC-focused |
| Minor source update | Low | Quick |

### 5.2 Reassessment Tracking

Each AKU maintains reassessment history:

```json
{
  "reassessment_history": [
    {
      "date": "2026-01-08T16:45:00.000Z",
      "trigger": "scheduled",
      "level": "standard",
      "assessor": "quality-agent",
      "previous_cqs": 0.85,
      "new_cqs": 0.87,
      "changes": ["Updated references", "Added cross-domain link"],
      "status": "improved"
    }
  ]
}
```

### 5.3 Reassessment Prioritization

Priority calculation:

```
Priority Score = (1 - CQS) × Importance_Weight × Time_Factor × Trigger_Weight

Where:
- Importance_Weight: critical=1.0, high=0.8, medium=0.6, low=0.4
- Time_Factor: months since last assessment / 12 (max 2.0)
- Trigger_Weight: error=2.0, source_update=1.5, scheduled=1.0, new_link=0.5
```

---

## 6. Quality Tracking

### 6.1 Quality Database Structure

Location: `.project/tracking/quality-scores.yaml`

```yaml
akus:
  aku-001-npv-definition:
    current_assessment:
      date: "2026-01-08T16:45:00.000Z"
      level: comprehensive
      assessor: quality-agent
      cqs: 0.92
      grade: A
      dimension_scores:
        factual_accuracy: 0.95
        ontology_compliance: 0.90
        reference_quality: 0.92
        third_party_verification: 0.88
        web_search_verification: 0.90
        dependency_completeness: 0.95
        content_completeness: 0.93
        technical_quality: 1.00
      issues: []
      recommendations:
        - "Consider adding more recent sources (2023+)"
    assessment_history:
      - date: "2025-12-27T14:00:00.000Z"
        cqs: 0.88
        grade: B+
    next_scheduled_assessment: "2026-07-08"
    reassessment_count: 1
    
summary:
  total_akus: 658
  assessed_akus: 50
  average_cqs: 0.84
  grade_distribution:
    "A+": 5
    "A": 15
    "B+": 12
    "B": 10
    "C+": 5
    "C": 2
    "D": 1
    "F": 0
  domain_averages:
    formal-sciences: 0.86
    natural-sciences: 0.82
    social-sciences: 0.85
    health-sciences: 0.83
  last_updated: "2026-01-08T16:45:00.000Z"
```

### 6.2 Quality Reports

#### Daily Report
- AKUs assessed today
- Issues identified
- Scores updated
- Upcoming reassessments

#### Weekly Report
- Quality trends
- Domain comparison
- Agent performance
- Top/bottom performers

#### Monthly Report
- Comprehensive quality analysis
- Improvement recommendations
- Framework effectiveness
- Resource allocation suggestions

### 6.3 Quality Dashboard Metrics

Key metrics to track:

1. **Overall Quality Score**: Average CQS across all AKUs
2. **Assessment Coverage**: % of AKUs with current assessment
3. **Quality Distribution**: Grade distribution chart
4. **Domain Health**: Per-domain quality averages
5. **Issue Backlog**: Open quality issues
6. **Reassessment Queue**: Pending reassessments
7. **Trend Analysis**: Quality over time
8. **Agent Effectiveness**: Per-agent quality impact

---

## 7. Tools and Automation

### 7.1 Primary Quality Assessment Tool

**Location:** `.project/agents/quality-assurance/tools/comprehensive_quality_assessment.py`

**Capabilities:**
- Multi-dimensional scoring
- Automated fact-checking integration
- Ontology validation
- Reference verification
- Web search integration
- Dependency analysis
- Quality tracking updates
- Report generation

**Usage:**
```bash
# Assess single AKU
python comprehensive_quality_assessment.py path/to/aku.json

# Batch assessment
python comprehensive_quality_assessment.py --directory path/to/akus/

# Domain assessment
python comprehensive_quality_assessment.py --domain health-sciences

# Reassessment mode
python comprehensive_quality_assessment.py path/to/aku.json --reassess

# Generate report
python comprehensive_quality_assessment.py --report weekly
```

### 7.2 Supporting Tools

| Tool | Purpose | Location |
|------|---------|----------|
| validate_aku_v2.py | Technical validation | .project/agents/quality-assurance/tools/ |
| validate_ontology.py | Ontology compliance | .project/agents/quality-assurance/tools/ |
| validate_uris.py | Reference validation | .project/agents/quality-assurance/tools/ |
| discover_cross_domain.py | Dependency analysis | .project/agents/quality-assurance/tools/ |

### 7.3 Automation Integration

**CI/CD Integration:**
- Pre-commit: Quick Assessment
- Pull Request: Standard Assessment
- Merge: Update quality tracking
- Scheduled: Weekly comprehensive assessment

**GitHub Actions Workflow:**
```yaml
name: Quality Assessment
on:
  push:
    paths: ['domain/**/*.json', '.project/pilot/**/*.json']
  schedule:
    - cron: '0 3 * * 0'  # Weekly at 3am Sunday

jobs:
  assess-quality:
    runs-on: ubuntu-latest
    steps:
      - name: Run Quality Assessment
        run: python comprehensive_quality_assessment.py --changed-only
```

---

## 8. Agent Integration

### 8.1 Agent Responsibilities

| Agent | Quality Role | Dimensions |
|-------|--------------|------------|
| @fact-checking | Factual verification | FA, WSV |
| @verification | Overall validation | All |
| @ontology | Structural compliance | OC |
| @peer-review | Independent review | TPV |
| @citation | Reference quality | RQ |
| @contrarian | Gap identification | CC, DC |
| @quality | Quality orchestration | All |

### 8.2 Multi-Agent Assessment Flow

```
1. @quality initiates assessment
   │
   ├─→ @ontology validates OC
   │   └─→ Returns OC score + issues
   │
   ├─→ @fact-checking validates FA
   │   └─→ Returns FA score + issues
   │
   ├─→ @citation validates RQ
   │   └─→ Returns RQ score + issues
   │
   ├─→ @peer-review provides TPV
   │   └─→ Returns TPV score + review
   │
   └─→ @contrarian identifies gaps
       └─→ Returns CC/DC issues
   │
   └─→ @quality aggregates results
       └─→ Calculates CQS, generates report
```

### 8.3 Agent Invocation Examples

```
@quality Perform comprehensive assessment of domain/health-sciences/medicine/surgery/vascular/pathology/mesenteric-ischemia/aku-001-ami-definition.json

@fact-checking Verify all medical claims in aku-039-atypical-presentations.json using peer-reviewed sources from last 10 years

@ontology Validate cross-domain references in domain/formal-sciences/computer-science/functional-programming/

@contrarian Review NPV pilot AKUs for completeness gaps and missing dependencies
```

---

## 9. Quality Thresholds

### 9.1 Publication Thresholds

| Content Type | Minimum CQS | Required Dimensions |
|--------------|-------------|---------------------|
| Medical/Clinical | 0.90 | FA ≥ 0.95, TPV ≥ 0.85 |
| Mathematical/Formal | 0.85 | FA ≥ 0.90, TQ ≥ 0.90 |
| Economic/Financial | 0.85 | FA ≥ 0.85, RQ ≥ 0.85 |
| General Science | 0.80 | FA ≥ 0.85 |
| Educational | 0.80 | CC ≥ 0.85 |

### 9.2 Flagging Thresholds

| Condition | Action |
|-----------|--------|
| Any dimension < 0.50 | Block publication, require immediate fix |
| CQS < 0.70 | Require major revision |
| FA < 0.80 | Flag for fact-checking |
| TPV = 0 | Require independent verification |
| DC < 0.70 | Identify missing dependencies |

### 9.3 Excellence Thresholds

| Condition | Recognition |
|-----------|-------------|
| CQS ≥ 0.95 | Feature as exemplar |
| All dimensions ≥ 0.90 | Highlight as comprehensive |
| TPV ≥ 0.95 | Mark as peer-reviewed |
| FA = 1.00 | Mark as verified |

---

## 10. Continuous Improvement

### 10.1 Framework Review Cycle

- **Monthly:** Review threshold effectiveness
- **Quarterly:** Adjust weights based on outcomes
- **Annually:** Major framework revision

### 10.2 Improvement Tracking

Track and incorporate:
- False positive/negative patterns
- Agent performance data
- User feedback
- Domain expert input
- Tool effectiveness metrics

### 10.3 Evolution Roadmap

**Phase 1 (Current):** Manual + automated hybrid
**Phase 2 (Q2 2026):** Full automation with human override
**Phase 3 (Q3 2026):** ML-enhanced quality prediction
**Phase 4 (Q4 2026):** Proactive quality management

---

## Appendix A: Missing AKU Dependencies Template

When identifying missing supportive AKUs:

```yaml
missing_dependencies:
  for_aku: aku-001-npv-definition
  identified_by: comprehensive_quality_assessment
  date: "2026-01-08T16:45:00.000Z"
  missing:
    - id: time-value-of-money
      type: definition
      priority: critical
      reason: "Referenced as prerequisite but does not exist"
      suggested_domain_path: "social-sciences/economics/finance/fundamentals"
      
    - id: opportunity-cost-concept
      type: theory
      priority: high
      reason: "Implicit dependency for discount rate understanding"
      suggested_domain_path: "social-sciences/economics/microeconomics/fundamentals"
```

---

## Appendix B: Quality Assessment Checklist

### Quick Assessment Checklist
- [ ] Valid JSON syntax
- [ ] All required fields present
- [ ] Valid timestamps
- [ ] Classification complete
- [ ] Content non-empty

### Standard Assessment Checklist
- [ ] All Quick Assessment items
- [ ] Domain path valid
- [ ] At least 2 sources cited
- [ ] Relationships defined
- [ ] No broken references
- [ ] Content matches difficulty level
- [ ] Explanations adequate

### Comprehensive Assessment Checklist
- [ ] All Standard Assessment items
- [ ] All facts verified against sources
- [ ] External ontology alignment checked
- [ ] Independent verification obtained
- [ ] Web search verification performed
- [ ] All dependencies exist
- [ ] Executable code tested
- [ ] Pedagogical elements complete
- [ ] Contrarian review performed

---

## Related Documents

- [AKU Validation Tools](../agents/quality-assurance/tools/README.md)
- [Ontology Integration Specification](research/ontology-integration-specification.md)
- [Knowledge Format Specification](knowledge-format-v2.md)
- [Agent KPIs](../.github/copilot/agent-kpis.md)

---

**Document Maintainer:** @quality agent  
**Review Schedule:** Monthly  
**Last Review:** 2026-01-08
