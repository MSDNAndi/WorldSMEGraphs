# Ontology System Enhancement Tools

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Production Ready

---

## Overview

This document describes the advanced tools created to enhance and maintain the ontology integration system in WorldSMEGraphs. These tools address key operational needs identified after the initial ontology migration.

---

## Tool Suite

### 1. URI Validator (`validate_uris.py`)

**Purpose**: Validate that external ontology URIs are accessible and return valid responses.

**Why it matters**: Ontology services can change, URLs can break, and codes can be deprecated. Regular validation ensures our links remain functional.

**Features**:
- HTTP HEAD requests to check accessibility without downloading full content
- Support for 7+ major ontologies (SNOMED CT, MeSH, ICD-11, FIBO, DBpedia, Wikidata, QUDT)
- URI caching to avoid redundant checks
- Rate limiting to be respectful of ontology servers
- Detailed reporting with success rates

**Usage**:
```bash
# Validate all AKUs in repository
python .project/agents/quality-assurance/tools/validate_uris.py --all --verbose

# Validate specific directory
python .project/agents/quality-assurance/tools/validate_uris.py --directory domain/health-sciences/medicine/

# Validate single AKU
python .project/agents/quality-assurance/tools/validate_uris.py path/to/aku.json
```

**Output Example**:
```
Validating URIs in 16 AKU(s)...

✅ aku-001-npv-definition.json
✅ aku-002-npv-basic-formula.json
⏭️  aku-003-present-value-concept.json (no URIs)

======================================================================
URI VALIDATION SUMMARY
======================================================================
Total URIs checked: 45
✅ Valid: 43
❌ Invalid: 2
⏭️  Skipped (unknown ontology): 0
💾 Cached hits: 12

Success rate: 95.6%
```

**When to use**:
- Before major releases
- After ontology version updates
- Monthly maintenance checks
- When adding new ontology links

---

### 2. Ontology Version Tracker (`track_ontology_versions.py`)

**Purpose**: Track which versions of ontologies are used and monitor for updates/deprecations.

**Why it matters**: Ontologies update regularly (SNOMED CT twice yearly, MeSH annually, etc.). Tracking versions helps identify when codes might be deprecated and migration is needed.

**Features**:
- Record ontology versions with release dates
- Track which AKUs use which ontologies
- Generate usage reports across knowledge base
- Monitor deprecation risk levels
- Provide update frequency information

**Usage**:
```bash
# Record ontology version
python .project/agents/quality-assurance/tools/track_ontology_versions.py --add snomed 2024-09-01

# Check which ontologies an AKU uses
python .project/agents/quality-assurance/tools/track_ontology_versions.py --check path/to/aku.json

# Check all AKUs and build metadata
python .project/agents/quality-assurance/tools/track_ontology_versions.py --check-all

# Generate version tracking report
python .project/agents/quality-assurance/tools/track_ontology_versions.py --report

# List known ontologies
python .project/agents/quality-assurance/tools/track_ontology_versions.py --list
```

**Output Example**:
```
================================================================================
ONTOLOGY VERSION TRACKING REPORT
================================================================================

Last Updated: 2025-12-28T01:15:00.000Z

📚 ONTOLOGY VERSIONS
--------------------------------------------------------------------------------

SNOMED CT International Edition:
  Version: 2024-09-01
  Release Date: 2024-09-01
  Recorded: 2025-12-27T22:00:00.000Z
  Update Frequency: Biannual (March, September)
  Deprecation Risk: Medium - codes can be made inactive

📊 AKU ONTOLOGY USAGE
--------------------------------------------------------------------------------

Total AKUs tracked: 16

Ontology usage:
  SNOMED CT International Edition: 8 AKUs (50.0%)
  FIBO: 8 AKUs (50.0%)
  Wikidata: 8 AKUs (50.0%)
  MeSH: 8 AKUs (50.0%)
```

**Storage**: Versions tracked in `.project/ontology-versions.json`

**When to use**:
- When starting to use a new ontology
- After ontology releases (quarterly/annually)
- Before major knowledge base updates
- For audit and compliance documentation

---

### 3. Batch Processor (`batch_processor.py`)

**Purpose**: Process multiple AKUs at once with progress reporting and error recovery.

**Why it matters**: Manual one-by-one processing is time-consuming and error-prone. Batch processing enables efficient operations across the entire knowledge base.

**Features**:
- Validate multiple AKUs in batch
- Create backups before operations
- Progress reporting with status indicators
- Error collection and summary
- Dry-run mode to preview changes

**Usage**:
```bash
# Validate all AKUs in a directory
python .project/agents/quality-assurance/tools/batch_processor.py \
    --validate --directory domain/health-sciences/medicine/ --verbose

# Validate entire repository
python .project/agents/quality-assurance/tools/batch_processor.py \
    --validate --all

# Dry run (no actual changes)
python .project/agents/quality-assurance/tools/batch_processor.py \
    --validate --all --dry-run
```

**Output Example**:
```
🔍 Validating 16 AKUs...

  [1/16] ✅ aku-001-type2-endoleak-definition.json
  [2/16] ❌ aku-002-endoleak-classification.json
      - Missing skos:prefLabel
      - Missing metadata.last_updated

======================================================================
BATCH PROCESSING SUMMARY
======================================================================
Total files: 16
✅ Success: 14
❌ Failed: 2
⏭️  Skipped: 0

❌ ERRORS (2):

  File: aku-002-endoleak-classification.json
    - Missing skos:prefLabel
    - Missing metadata.last_updated

📦 Backup location: /tmp/aku_backup_20251228_011500

Success rate: 87.5%
```

**When to use**:
- Before committing bulk changes
- Regular quality checks
- Migration operations
- After automated enhancements

---

### 4. Cross-Domain Discovery (`discover_cross_domain.py`)

**Purpose**: Automatically discover potential relationships between concepts across different domains.

**Why it matters**: Medical, economic, and scientific concepts often interrelate (e.g., medical procedures have costs, scientific principles underpin medical treatments). Automated discovery helps identify these connections.

**Features**:
- Keyword-based pattern matching
- Confidence scoring
- Domain distribution analysis
- Suggestion generation with reasoning
- Customizable pattern library

**Usage**:
```bash
# Analyze entire repository for cross-domain relationships
python .project/agents/quality-assurance/tools/discover_cross_domain.py --analyze --report

# Get suggestions for a specific AKU
python .project/agents/quality-assurance/tools/discover_cross_domain.py --suggest path/to/aku.json
```

**Output Example**:
```
================================================================================
CROSS-DOMAIN RELATIONSHIP DISCOVERY REPORT
================================================================================

📊 DOMAIN DISTRIBUTION
--------------------------------------------------------------------------------
  Medical: 8 AKUs
  Economics: 8 AKUs

🔗 CROSS-DOMAIN CONNECTION SUGGESTIONS
--------------------------------------------------------------------------------

MEDICAL→ECONOMICS (3 potential connections)

  AKU: aku-009-treatment-algorithm
  Confidence: 67%
  Matched keywords: cost, payment, value
  Suggestion: Medical concepts with economic implications

💡 RECOMMENDATIONS
--------------------------------------------------------------------------------

1. Review high-confidence suggestions for potential links
2. Add cross-domain relationships where appropriate
3. Consider creating bridge AKUs for strong connections
4. Document domain boundaries and interfaces
```

**When to use**:
- When expanding the knowledge base
- After adding new domains
- To identify research opportunities
- For knowledge graph visualization planning

---

## Maintenance Workflows

### Monthly Maintenance

```bash
# 1. Validate all URIs
python .project/agents/quality-assurance/tools/validate_uris.py --all

# 2. Check for invalid URIs and investigate
# 3. Update ontology versions if new releases
python .project/agents/quality-assurance/tools/track_ontology_versions.py --add snomed 2024-09-01

# 4. Generate version tracking report
python .project/agents/quality-assurance/tools/track_ontology_versions.py --report
```

### Quarterly Review

```bash
# 1. Validate all AKUs
python .project/agents/quality-assurance/tools/batch_processor.py --validate --all

# 2. Check cross-domain connections
python .project/agents/quality-assurance/tools/discover_cross_domain.py --analyze --report

# 3. Review and act on suggestions
```

### Before Major Release

```bash
# 1. Full URI validation
python .project/agents/quality-assurance/tools/validate_uris.py --all --verbose

# 2. Batch validation
python .project/agents/quality-assurance/tools/batch_processor.py --validate --all

# 3. Version tracking check
python .project/agents/quality-assurance/tools/track_ontology_versions.py --check-all
python .project/agents/quality-assurance/tools/track_ontology_versions.py --report

# 4. Review cross-domain suggestions
python .project/agents/quality-assurance/tools/discover_cross_domain.py --analyze --report
```

---

## Integration with Existing Tools

These new tools complement the existing validation infrastructure:

**Existing Tools**:
- `validate_aku.py` - Basic AKU structure validation
- `validate_aku_v2.py` - Domain-aware validation
- `validate_ontology.py` - Ontology compliance checking
- `migrate_to_ontology.py` - AKU migration tool

**New Tools**:
- `validate_uris.py` - External URI validation
- `track_ontology_versions.py` - Version tracking
- `batch_processor.py` - Batch operations
- `discover_cross_domain.py` - Relationship discovery

**Recommended Workflow**:
1. Create AKU using template (existing guide)
2. Validate structure (`validate_aku_v2.py`)
3. Validate ontology compliance (`validate_ontology.py`)
4. Validate URIs (`validate_uris.py`)
5. Record in version tracker (`track_ontology_versions.py --check`)
6. Check cross-domain connections (`discover_cross_domain.py --suggest`)

---

## Future Enhancements

### Not Yet Implemented (Future Work)

**Relationship Visualization**:
- Generate graph diagrams of SKOS hierarchies
- Visualize cross-domain connections
- Interactive exploration tools

**Ontology Lookup API**:
- Cached ontology queries
- Local mirror for common lookups
- Integration with ontology browsers

**Deprecation Detection**:
- Automated checking against ontology release notes
- Notification system for deprecated codes
- Migration path suggestions

**CI/CD Integration** (deferred per user request):
- GitHub Actions workflows
- Automated validation on commits
- PR quality gates

---

## Troubleshooting

### URI Validation Timeouts

**Problem**: URI checks timing out or failing

**Solutions**:
- Increase timeout in `ONTOLOGY_PATTERNS` dict
- Check network connectivity
- Verify ontology service is operational
- Use caching to reduce repeated checks

### Version Tracking Not Saving

**Problem**: Changes not persisted to `.project/ontology-versions.json`

**Solutions**:
- Check file permissions
- Ensure `.project/` directory exists
- Verify JSON format if file exists

### Cross-Domain False Positives

**Problem**: Too many incorrect suggestions

**Solutions**:
- Adjust keyword patterns in `CROSS_DOMAIN_KEYWORDS`
- Increase confidence threshold
- Add domain-specific exclusion patterns

---

## Tool Dependencies

All tools use **Python standard library only** - no external dependencies required:
- `json` - JSON parsing
- `pathlib` - File system operations
- `urllib` - HTTP requests (for URI validation)
- `argparse` - Command-line interface
- `datetime` - Timestamps

This ensures tools work in any Python 3.7+ environment without installation complications.

---

**Last Updated**: 2025-12-28  
**Version**: 1.0  
**Status**: Production Ready
