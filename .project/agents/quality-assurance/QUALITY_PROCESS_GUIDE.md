# Quality Assurance Process Guide

## Overview

This document describes the comprehensive quality review, assessment, and correction process for Atomic Knowledge Units (AKUs) in WorldSMEGraphs. The process encompasses all aspects of quality including fact-checking, ontology validation, reference verification, third-party verification, web search verification, and tracking of supportive AKUs.

## Quality Dimensions

The quality assessment system evaluates AKUs across **8 key dimensions**:

### 1. Structural Integrity (10%)
- Validates JSON schema compliance
- Checks required fields presence
- Verifies field data types
- Ensures proper nesting and formatting

### 2. Content Quality (20%)
- Evaluates statement clarity and precision
- Checks explanation comprehensiveness
- Validates examples for accuracy
- Assesses vocabulary definitions

### 3. Fact Accuracy (20%)
- Cross-references claims with authoritative sources
- Verifies numerical data and statistics
- Checks formula correctness
- Validates historical facts

### 4. Ontological Consistency (15%)
- Validates domain_path alignment with global hierarchy
- Checks relationship integrity
- Verifies cross-domain links
- Ensures classification accuracy

### 5. Reference Quality (10%)
- Validates citation formats
- Checks source accessibility
- Verifies publication details
- Assesses source authority

### 6. Relationship Integrity (10%)
- Validates requires/enables chains
- Checks for circular dependencies
- Verifies related_to connections
- Assesses cross-domain links

### 7. Pedagogical Effectiveness (10%)
- Evaluates learning objectives clarity
- Checks prerequisite accuracy
- Assesses example quality
- Validates difficulty progression

### 8. Temporal Currency (5%)
- Checks content recency
- Validates external reference freshness
- Assesses knowledge currency
- Monitors for outdated information

## Quality Scoring System

### Composite Quality Score (CQS)
```
CQS = Σ(dimension_weight × dimension_score)
```

Where each dimension score is 0.0-1.0 and weights sum to 1.0.

### Grade Scale

| Grade | CQS Range | Description |
|-------|-----------|-------------|
| A+    | 0.95-1.00 | Exceptional quality |
| A     | 0.90-0.94 | Excellent |
| A-    | 0.85-0.89 | Very Good |
| B+    | 0.80-0.84 | Good |
| B     | 0.75-0.79 | Above Average |
| B-    | 0.70-0.74 | Satisfactory Plus |
| C+    | 0.65-0.69 | Satisfactory |
| C     | 0.60-0.64 | Acceptable |
| C-    | 0.55-0.59 | Marginal |
| D     | 0.40-0.54 | Below Standard |
| F     | 0.00-0.39 | Failing |

## Assessment Tools

### 1. Comprehensive Quality Assessment Tool
**Location:** `.project/agents/quality-assurance/tools/comprehensive_quality_assessment.py`

```bash
# Assess single AKU
python comprehensive_quality_assessment.py path/to/aku.json

# Assess directory
python comprehensive_quality_assessment.py --directory path/to/akus/

# Verbose output with recommendations
python comprehensive_quality_assessment.py path/to/aku.json --verbose

# Output to JSON
python comprehensive_quality_assessment.py path/to/aku.json --output-format json
```

### 2. Reassessment Tool
**Location:** `.project/agents/quality-assurance/tools/reassessment_tool.py`

```bash
# Generate reassessment report
python reassessment_tool.py --report

# Show priority queue
python reassessment_tool.py --priority-queue

# View quality history for an AKU
python reassessment_tool.py --history aku-001-npv-definition

# Run scheduled reassessments
python reassessment_tool.py --schedule --max 10
```

### 3. Domain-Aware Validator
**Location:** `.project/agents/quality-assurance/tools/validate_aku_v2.py`

```bash
# Validate single AKU
python validate_aku_v2.py path/to/aku.json

# Validate by domain
python validate_aku_v2.py --domain economics

# Verbose mode
python validate_aku_v2.py path/to/aku.json --verbose
```

## Assessment Workflow

### Phase 1: Initial Assessment
1. **Structural Validation**
   - Run schema validator
   - Check required fields
   - Verify JSON integrity

2. **Content Analysis**
   - Evaluate statement quality
   - Check explanation depth
   - Assess example coverage

3. **Fact Verification**
   - Cross-reference with sources
   - Verify calculations
   - Check citations

### Phase 2: Deep Assessment
4. **Ontological Review**
   - Validate domain path
   - Check relationship graph
   - Verify cross-domain links

5. **Reference Audit**
   - Verify source accessibility
   - Check citation accuracy
   - Assess source authority

6. **Relationship Analysis**
   - Map dependency graph
   - Identify missing links
   - Check for orphans

### Phase 3: Quality Synthesis
7. **Score Calculation**
   - Compute dimension scores
   - Calculate CQS
   - Determine grade

8. **Recommendation Generation**
   - Identify improvement areas
   - Suggest corrections
   - Prioritize fixes

## Reassessment Process

### Trigger Conditions

Reassessment is triggered by:

1. **Scheduled Interval**
   - Grade A: Every 180 days
   - Grade B: Every 90 days
   - Grade C: Every 45 days
   - Grade D: Every 14 days
   - Grade F: Every 7 days

2. **Content Change**
   - Any modification to AKU content
   - Significant structural changes
   - Reference updates

3. **Dependency Update**
   - Related AKUs modified
   - Upstream dependencies changed
   - Cross-domain links updated

4. **External Trigger**
   - New authoritative source available
   - Known error reported
   - Domain knowledge updated

5. **User Feedback**
   - Error report received
   - Improvement suggestion
   - Accuracy question raised

### Priority Queue

AKUs are prioritized for reassessment based on:

| Factor | Weight | Description |
|--------|--------|-------------|
| Grade Score | 40% | Lower grades = higher priority |
| Time Since Assessment | 20% | Longer time = higher priority |
| Content Importance | 20% | Critical content = higher priority |
| Dependency Count | 10% | More dependents = higher priority |
| User Feedback | 10% | Feedback = higher priority |

### Priority Score Calculation
```
Priority = 0.4 × (1 - grade_score) +
           0.2 × min(days_since / 180, 1.0) +
           0.2 × importance_score +
           0.1 × min(dependents / 10, 1.0) +
           0.1 × feedback_score
```

## Correction Workflow

### For Grade D or F AKUs

1. **Immediate Triage**
   - Identify critical errors
   - Assess impact scope
   - Determine correction urgency

2. **Root Cause Analysis**
   - Identify why quality is low
   - Check for systematic issues
   - Review creation process

3. **Correction Planning**
   - Define specific fixes needed
   - Estimate correction effort
   - Assign to appropriate agent

4. **Implementation**
   - Apply corrections
   - Update metadata
   - Document changes

5. **Re-assessment**
   - Run full assessment
   - Verify improvements
   - Confirm grade improvement

### For Grade C AKUs

1. **Improvement Analysis**
   - Identify weakest dimensions
   - Prioritize improvements
   - Plan enhancements

2. **Targeted Improvements**
   - Address specific gaps
   - Enhance documentation
   - Improve examples

3. **Verification**
   - Re-assess after changes
   - Confirm improvement
   - Update tracking

## Quality Tracking

### Tracking Database
**Location:** `.project/tracking/quality-scores.yaml`

The tracking database stores:
- Current assessment results
- Assessment history (last 10)
- Quality trend data
- Improvement recommendations

### Quality Metrics

Key metrics tracked:

1. **Grade Distribution**
   - Count of AKUs per grade
   - Trend over time
   - Domain breakdown

2. **Average CQS**
   - Overall average
   - By domain
   - By AKU type

3. **Improvement Rate**
   - AKUs improving grade
   - Average improvement time
   - Intervention effectiveness

4. **Coverage Metrics**
   - Assessed vs unassessed
   - Assessment currency
   - Reassessment backlog

## Verification Types

### 1. Fact-Checking Verification
- Cross-reference with textbooks
- Verify with academic papers
- Check against authoritative websites
- Validate mathematical correctness

### 2. Ontology Verification
- Validate domain_path against global-hierarchy.yaml
- Check relationship consistency
- Verify cross-domain link validity
- Ensure classification accuracy

### 3. Reference Verification
- Confirm source existence
- Verify citation accuracy
- Check source accessibility
- Validate publication details

### 4. Third-Party Verification
- Independent expert review
- Peer review process
- Domain specialist validation
- External audit

### 5. Web Search Verification
- Verify claims against web sources
- Check for contradicting information
- Validate currency of information
- Cross-reference multiple sources

### 6. Supportive AKU Verification
- Check for missing prerequisite AKUs
- Identify needed related AKUs
- Validate dependency completeness
- Ensure learning path coherence

## Agent Integration

### Quality Agent
**File:** `.github/agents/quality.agent.md`

The Quality Agent orchestrates the assessment process:
- Coordinates dimension evaluators
- Synthesizes quality scores
- Generates recommendations
- Manages reassessment queue

### Fact-Checking Agent
**File:** `.github/agents/fact-checking.agent.md`

Specialized for accuracy verification:
- Cross-references authoritative sources
- Validates numerical claims
- Checks formula correctness
- Verifies historical accuracy

### Peer Review Agent
**File:** `.github/agents/peer-review.agent.md`

Provides academic-style review:
- Content rigor assessment
- Methodology evaluation
- Citation quality review
- Improvement suggestions

### Verification Agent
**File:** `.github/agents/verification.agent.md`

Handles multi-source verification:
- Web search verification
- Third-party validation
- Reference checking
- Consistency validation

## Best Practices

### For AKU Authors

1. **Before Creating**
   - Review related existing AKUs
   - Verify prerequisite AKUs exist
   - Check ontology for correct placement

2. **During Creation**
   - Use authoritative sources
   - Include complete citations
   - Add comprehensive examples
   - Define all specialized terms

3. **After Creation**
   - Run validation tools
   - Request peer review
   - Check relationship integrity
   - Document assumptions

### For Reviewers

1. **Assessment Focus**
   - Check factual accuracy first
   - Verify source quality
   - Assess pedagogical effectiveness
   - Validate relationships

2. **Feedback Style**
   - Be specific about issues
   - Suggest concrete improvements
   - Reference authoritative sources
   - Prioritize critical fixes

## Continuous Improvement

### Monthly Review
- Analyze grade distribution trends
- Identify systematic issues
- Update assessment criteria
- Refine priority weights

### Quarterly Audit
- Full reassessment of sample AKUs
- Cross-domain consistency check
- Reference validity verification
- Process effectiveness review

### Annual Calibration
- Update dimension weights
- Revise grade thresholds
- Refresh verification sources
- Enhance assessment tools

---

**Last Updated:** 2026-01-08
**Version:** 1.0.0
