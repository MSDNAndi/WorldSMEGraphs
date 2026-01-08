# Quality Assurance Tools

**Purpose**: Validation and quality checking tools for WorldSMEGraphs content  
**Location**: `.project/agents/quality-assurance/tools/`  
**Maintained By**: Quality Assurance Agent

## Overview

This directory contains tools for validating, analyzing, and ensuring quality of AKUs (Atomic Knowledge Units) and their relationships within the WorldSMEGraphs system.

## Available Tools

### 1. validate_aku_v2.py (Recommended)

**Purpose**: Domain-aware AKU validator with flexible schema

**Usage**:
```bash
# Single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/

# Specific domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine path/to/aku.json

# Verbose output
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json --verbose
```

**Features**:
- Auto-detects domain from classification.domain_path
- Domain-specific validation rules (medicine, math, economics, science)
- Recognizes new hierarchy (formal-sciences, natural-sciences, etc.)
- Flexible schema based on content type
- Detailed error reporting with suggestions

**Validated Domains**:
- formal-sciences → math/science rules
- natural-sciences → science rules
- social-sciences → economics rules
- health-sciences → medicine rules
- Legacy: math, medicine, economics, science (backward compatible)

### 2. validate_aku.py (Legacy)

**Purpose**: Math-focused AKU validator

**Usage**:
```bash
python .project/agents/quality-assurance/tools/validate_aku.py path/to/aku.json
python .project/agents/quality-assurance/tools/validate_aku.py --directory path/to/akus/
python .project/agents/quality-assurance/tools/validate_aku.py --pilot npv
```

**Note**: Use `validate_aku_v2.py` for new work. This validator is maintained for legacy compatibility.

### 3. visualize_relationships.py

**Purpose**: Creates visualizations of SKOS relationships in AKUs

**Usage**:
```bash
# Single AKU
python .project/agents/quality-assurance/tools/visualize_relationships.py path/to/aku.json

# Directory
python .project/agents/quality-assurance/tools/visualize_relationships.py --directory path/to/akus/

# All domains
python .project/agents/quality-assurance/tools/visualize_relationships.py --graph-all
```

**Features**:
- Text-based relationship trees
- Mermaid diagram output
- Shows broader/narrower/related concepts
- Detects bidirectional relationships
- Identifies orphaned concepts

**Output Formats**:
- Console text tree
- Mermaid flowchart syntax (for documentation)

### 4. batch_processor.py

**Purpose**: Process multiple AKUs in batch

**Usage**:
```bash
python .project/agents/quality-assurance/tools/batch_processor.py \
  --directory path/to/akus/ \
  --operation validate
```

**Operations**:
- validate: Run validation on all AKUs
- check-ontology: Verify ontology compliance
- generate-report: Create quality report

**Features**:
- Parallel processing
- Progress tracking
- Aggregate statistics
- Error summary

### 5. discover_cross_domain.py

**Purpose**: Discover potential cross-domain relationships

**Usage**:
```bash
python .project/agents/quality-assurance/tools/discover_cross_domain.py \
  --source path/to/akus/ \
  --threshold 0.7
```

**Features**:
- Semantic similarity analysis
- Suggests cross-domain links
- Confidence scores
- Export to JSON for review

### 6. validate_ontology.py

**Purpose**: Validates ontology structure and consistency

**Usage**:
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py \
  --ontology domain/_ontology/global-hierarchy.yaml
```

**Checks**:
- Hierarchy consistency
- No circular dependencies
- Valid domain paths
- Proper classification

### 7. validate_uris.py

**Purpose**: Validates URI references in AKUs

**Usage**:
```bash
python .project/agents/quality-assurance/tools/validate_uris.py path/to/aku.json
```

**Features**:
- Checks @id format
- Validates context URIs
- Verifies external ontology links
- Checks for dead links

### 8. migrate_to_ontology.py

**Purpose**: Migrates AKUs to use formal ontology references

**Usage**:
```bash
python .project/agents/quality-assurance/tools/migrate_to_ontology.py \
  --aku path/to/aku.json \
  --ontology domain/_ontology/global-hierarchy.yaml
```

**Features**:
- Adds proper ontology references
- Updates domain classification
- Adds SKOS relationships
- Preserves existing content

### 9. track_ontology_versions.py

**Purpose**: Tracks changes to ontology structure over time

**Usage**:
```bash
python .project/agents/quality-assurance/tools/track_ontology_versions.py \
  --ontology domain/_ontology/global-hierarchy.yaml \
  --output .project/tracking/ontology-changes.log
```

**Features**:
- Detects structural changes
- Version comparison
- Change impact analysis
- Migration recommendations

## Common Workflows

### Workflow 1: Validate New AKU

```bash
# 1. Validate structure
python .project/agents/quality-assurance/tools/validate_aku_v2.py new-aku.json --verbose

# 2. Check cross-domain links
python domain/_ontology/tools/validate_cross_domain.py new-aku.json

# 3. Visualize relationships
python .project/agents/quality-assurance/tools/visualize_relationships.py new-aku.json
```

### Workflow 2: Domain Quality Check

```bash
# 1. Validate all AKUs
python .project/agents/quality-assurance/tools/batch_processor.py \
  --directory domain/formal-sciences/mathematics/ \
  --operation validate

# 2. Check ontology compliance
python .project/agents/quality-assurance/tools/validate_ontology.py \
  --ontology domain/_ontology/global-hierarchy.yaml

# 3. Discover missing cross-domain links
python .project/agents/quality-assurance/tools/discover_cross_domain.py \
  --source domain/formal-sciences/mathematics/
```

### Workflow 3: Migration Quality Assurance

```bash
# After migrating domain:

# 1. Validate all migrated AKUs
python .project/agents/quality-assurance/tools/batch_processor.py \
  --directory domain/new-location/ \
  --operation validate

# 2. Check URIs are correct
python .project/agents/quality-assurance/tools/validate_uris.py \
  domain/new-location/sample-aku.json

# 3. Verify relationships preserved
python .project/agents/quality-assurance/tools/visualize_relationships.py \
  --directory domain/new-location/
```

## Quality Standards

All AKUs must pass these checks:

1. **Structure**: Valid JSON with required fields
2. **Metadata**: Complete version, timestamps, contributors
3. **Classification**: Valid domain_path, type, difficulty
4. **Content**: Domain-appropriate required fields
5. **Relationships**: Valid SKOS relationships
6. **IDs**: Proper @id format and uniqueness
7. **URIs**: Valid context and ontology references

## Tool Development

### Adding New Tools

When creating new QA tools:

1. **Follow Pattern**: Use existing tools as templates
2. **Command Line**: Use argparse with --help
3. **Validation First**: Never modify without validating
4. **Detailed Output**: Clear error messages and suggestions
5. **Documentation**: Add to this README

### Testing Tools

Before using on production:

1. Test on sample data
2. Verify error handling
3. Check edge cases
4. Document limitations
5. Add usage examples

## Related Documentation

- **Migration Guide**: `.project/docs/domain-migration-guide.md`
- **Ontology Tools**: `domain/_ontology/tools/README.md`
- **Structure**: `.project/structure.md`
- **Format Spec**: `.project/knowledge-format.md`

## Troubleshooting

### Problem: Validation Fails with "Unknown Domain"

**Solution**: Update DOMAIN_REQUIREMENTS in validate_aku_v2.py to include your domain.

### Problem: Cross-Domain Links Not Found

**Solution**: Ensure target AKU exists and path is correct. Use `find` to verify.

### Problem: Batch Processor Slow

**Solution**: Reduce parallelism or process smaller batches.

### 10. comprehensive_quality_assessment.py (NEW)

**Purpose**: Multi-dimensional quality assessment with scoring and tracking

**Usage**:
```bash
# Single AKU - standard assessment
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py path/to/aku.json

# Directory assessment
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py --directory path/to/akus/

# Domain assessment
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py --domain health-sciences

# Comprehensive assessment (all 8 dimensions)
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py path/to/aku.json --level comprehensive

# Reassessment mode
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py path/to/aku.json --reassess

# Export results to JSON
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py --directory path/to/akus/ --output results.json
```

**Features**:
- **8 Quality Dimensions**:
  1. Factual Accuracy (FA) - Verification of claims
  2. Ontology Compliance (OC) - SKOS, JSON-LD, hierarchy
  3. Reference Quality (RQ) - Source citations
  4. Third-Party Verification (TPV) - Independent validation
  5. Web Search Verification (WSV) - External links
  6. Dependency Completeness (DC) - Required AKUs exist
  7. Content Completeness (CC) - All sections present
  8. Technical Quality (TQ) - Valid JSON, timestamps

- **Composite Quality Score (CQS)**: Weighted average of all dimensions
- **Grades**: A+ to F based on CQS thresholds
- **Domain-Specific Weights**: Medical content weighted toward accuracy
- **Missing Dependencies**: Identifies AKUs that need to be created
- **Publication Readiness**: Checks domain-specific thresholds

**Assessment Levels**:
- `quick`: Technical + content (2-5 min)
- `standard`: + ontology, references, dependencies (15-30 min)
- `comprehensive`: All 8 dimensions (1-2 hours)

**Output Example**:
```
GRADE: B+ (CQS: 0.8725)
Publication Ready: ✅ Yes

DIMENSION SCORES:
  factual_accuracy              [████████░░] 0.84
  ontology_compliance           [██████████] 1.00
  reference_quality             [█████████░] 0.91
  ...
```

**Related Framework**: See `.project/quality-assessment-framework.md` for full specification.

## Quality Assessment Workflow

### Complete Quality Review Process

The comprehensive quality assessment framework enables multi-stage review:

```
1. CREATION → Quick Assessment
   └─→ Pass: Proceed to Standard Assessment
   └─→ Fail: Return for corrections

2. STANDARD ASSESSMENT
   └─→ CQS ≥ 0.80: Mark for publication review
   └─→ CQS 0.70-0.79: Request improvements
   └─→ CQS < 0.70: Return for rework

3. COMPREHENSIVE REVIEW (for critical content)
   └─→ All 8 dimensions assessed
   └─→ Third-party verification
   └─→ Web search validation
   └─→ Missing dependencies identified

4. PUBLICATION
   └─→ Domain-specific thresholds met
   └─→ Grade B+ or better
   └─→ No critical issues
```

### Reassessment Triggers

AKUs are reassessed when:
- Error reported (High priority)
- Source updated (High priority)
- 6+ months since assessment (Medium priority)
- Domain ontology changed (Medium priority)
- New related AKU created (Low priority)

### Quality Tracking

All assessment results are stored in:
- `.project/tracking/quality-scores.yaml` - Score database
- Each AKU tracks: current score, history, next assessment date

### Workflow Commands

```bash
# 1. Quick validation before commit
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/new-aku.json --level quick

# 2. Standard assessment for PR review
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  --directory path/to/changed-akus/ --level standard

# 3. Comprehensive review for publication
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/critical-aku.json --level comprehensive --verbose

# 4. Domain-wide quality check
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  --domain health-sciences --output domain-quality-report.json
```

## Version History

- **v3.0** (2026-01-08): Added comprehensive_quality_assessment.py with 8-dimension scoring
- **v2.0** (2026-01-04): Enhanced validate_aku_v2.py for new hierarchy
- **v1.5** (2026-01-04): Updated visualize_relationships.py with new paths
- **v1.0** (2025-12-27): Initial tool suite

---

**Last Updated**: 2026-01-08  
**Status**: Active and maintained  
**Contact**: @quality-agent for questions
