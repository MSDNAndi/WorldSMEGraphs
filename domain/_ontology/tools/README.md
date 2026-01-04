# Domain Ontology Tools

**Purpose**: Migration and validation tools for the WorldSMEGraphs domain hierarchy  
**Location**: `domain/_ontology/tools/`  
**Maintained By**: Ontology Agent, File Organization Agent

## Overview

This directory contains tools for migrating content to and validating compliance with the global domain hierarchy defined in `domain/_ontology/global-hierarchy.yaml`.

## Available Tools

### 1. migrate_domain.py

**Purpose**: General-purpose domain migration script

**Usage**:
```bash
python domain/_ontology/tools/migrate_domain.py \
  --source domain/old-path \
  --target domain/new-path \
  --verify
```

**Features**:
- Migrates AKUs between domain locations
- Updates domain_path in classification
- Preserves all metadata and content
- Validates migrated files
- Generates migration report

**Use Cases**:
- Moving content to comply with global hierarchy
- Reorganizing domain structure
- Bulk migrations with verification

**Output**: Migration report with statistics and any errors

### 2. migrate_category_theory.py

**Purpose**: Specialized migration for category theory AKUs

**Usage**:
```bash
python domain/_ontology/tools/migrate_category_theory.py
```

**Features**:
- Migrates category theory from CS to mathematics
- Adds `isNativeDomain: true` flag
- Updates @id references
- Adds cross_domain_applications section
- Updates timestamps

**Background**:
Category theory is fundamentally mathematical, not computer science.
This tool migrates it to `formal-sciences/mathematics/pure-mathematics/category-theory/`
per the native domain placement principle.

**Status**: Completed - used in PR #30 migration

### 3. update_fp_cross_domain.py

**Purpose**: Updates functional programming AKUs with cross-domain references

**Usage**:
```bash
python domain/_ontology/tools/update_fp_cross_domain.py
```

**Features**:
- Adds `isApplicationDomain: true` flag
- Creates cross_domain_references section
- Links to native math concepts (functors, monads, monoids)
- Updates timestamps

**Background**:
Functional programming APPLIES category theory concepts.
This tool creates proper cross-domain links to mathematics.

**Status**: Completed - used in PR #30 migration

### 4. validate_cross_domain.py

**Purpose**: Validates cross-domain links and references

**Usage**:
```bash
# Single AKU
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Directory
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/

# Verbose output
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json --verbose
```

**Features**:
- Validates cross_domain_references structure
- Checks that native domain AKUs have `isNativeDomain: true`
- Checks that application domain AKUs have proper links
- Verifies referenced paths exist
- Validates domain_path alignment with global hierarchy

**Use Cases**:
- Verifying cross-domain linking patterns
- Validating migrations
- Checking new AKU compliance

**Output**: Validation report with errors and warnings

## Global Domain Hierarchy

All tools use the authoritative hierarchy defined in:
```
domain/_ontology/global-hierarchy.yaml
```

### Key Principles

1. **Native Domain Placement**: Concepts belong to their origin field
   - Category theory → mathematics (not computer science)
   - Economics concepts → social sciences
   - Medical concepts → health sciences

2. **Cross-Domain Linking**: Applications link to native definitions
   - Functional programming → links to category theory
   - Econometrics → links to statistics
   - Medical imaging → links to physics

3. **Single Source of Truth**: One authoritative location per concept
   - Native domain contains full definition
   - Application domains contain context + links

## Migration Workflow

Standard process using these tools:

1. **Analysis**
   ```bash
   # Count files to migrate
   find domain/old-path -name "*.json" | wc -l
   ```

2. **Migration**
   ```bash
   # Migrate content
   python domain/_ontology/tools/migrate_domain.py \
     --source domain/old-path \
     --target domain/new-path
   ```

3. **Validation**
   ```bash
   # Validate cross-domain links
   python domain/_ontology/tools/validate_cross_domain.py \
     --directory domain/new-path
   ```

4. **Verification**
   ```bash
   # Verify AKU validity
   python .project/agents/quality-assurance/tools/validate_aku_v2.py \
     domain/new-path/file.json
   ```

## Examples

### Example 1: Migrate Domain

```bash
# Migrate economics content
python domain/_ontology/tools/migrate_domain.py \
  --source domain/economics \
  --target domain/social-sciences/economics \
  --verify
```

### Example 2: Validate Cross-Domain Links

```bash
# Validate functional programming links to math
python domain/_ontology/tools/validate_cross_domain.py \
  domain/formal-sciences/computer-science/programming-paradigms/functional-programming/
```

### Example 3: Check Single AKU

```bash
# Validate one AKU
python domain/_ontology/tools/validate_cross_domain.py \
  domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-001-historical-origins.json \
  --verbose
```

## Common Issues

### Issue: Domain Path Mismatch

**Problem**: AKU domain_path doesn't match global hierarchy

**Solution**:
1. Check `global-hierarchy.yaml` for correct path
2. Update domain_path in AKU classification
3. Re-run validation

### Issue: Missing Cross-Domain References

**Problem**: Application domain AKU doesn't link to native concept

**Solution**:
1. Add cross_domain_references section
2. Link to native domain AKU @id
3. Specify relationship type (uses/applies/extends)

### Issue: Duplicate Concepts

**Problem**: Same concept in multiple domains

**Solution**:
1. Identify native domain (origin of concept)
2. Keep full definition in native domain
3. Replace copies with cross-domain links

## Related Documentation

- **Global Hierarchy**: `domain/_ontology/global-hierarchy.yaml`
- **Migration Guide**: `.project/docs/domain-migration-guide.md`
- **Migration Report**: `.project/tracking/migration-pr30-completion-report.md`
- **Validation Report**: `.project/tracking/post-migration-validation-report.md`

## Tool Development

### Adding New Tools

When creating new ontology tools:

1. **Follow Naming**: `[action]_[target].py`
2. **Add Docstring**: Comprehensive module documentation
3. **Command Line Interface**: Use argparse with clear help
4. **Validation**: Always validate before modifying files
5. **Reporting**: Generate detailed operation reports
6. **Error Handling**: Graceful failures with clear messages

### Testing Tools

Before using on production data:

1. Test on sample AKUs
2. Verify no data loss
3. Check all edge cases
4. Document any limitations
5. Add to this README

## Version History

- **v1.0** (2026-01-04): Initial tools created for PR #30 migration
  - migrate_domain.py
  - migrate_category_theory.py  
  - update_fp_cross_domain.py
  - validate_cross_domain.py

## Contact

For questions about these tools:
- Use `@ontology-agent` for ontology questions
- Use `@file-organization-agent` for migration questions
- Refer to `.project/docs/domain-migration-guide.md` for detailed process

---

**Last Updated**: 2026-01-04  
**Status**: Active (all tools functional)  
**Maintenance**: Ontology Agent, File Organization Agent
