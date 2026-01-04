# Quick Start Guide: Domain Migration

> **For**: Future developers migrating content to new hierarchy  
> **Version**: 1.0.0  
> **Date**: 2026-01-04

## Overview

This guide helps you migrate domain content from legacy locations to the new global hierarchy following the established patterns.

## Prerequisites

✅ Familiarity with:
- Project structure (`domain/_ontology/global-hierarchy.yaml`)
- AKU v2.0 format
- Native domain principle

✅ Tools installed:
- Python 3.x (no external dependencies needed)
- Git

✅ Knowledge of:
- Source domain location
- Target domain path (check global-hierarchy.yaml)

## Quick Start (3 Steps)

### Step 1: Dry Run
Preview the migration without writing files:

```bash
cd /home/runner/work/WorldSMEGraphs/WorldSMEGraphs

python domain/_ontology/tools/migrate_domain.py \
  --source science/chemistry \
  --target natural-sciences/chemistry \
  --dry-run
```

Review the output to ensure:
- Correct number of AKUs found
- Domain paths will update correctly
- No unexpected failures

### Step 2: Execute Migration
Run the actual migration:

```bash
python domain/_ontology/tools/migrate_domain.py \
  --source science/chemistry \
  --target natural-sciences/chemistry
```

The script will:
- ✅ Create target directories
- ✅ Update domain_path in classification
- ✅ Add isNativeDomain: true
- ✅ Update modified timestamps
- ✅ Copy files to new location

### Step 3: Validate
Validate the migrated content:

```bash
# Validate structure and cross-references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/natural-sciences/chemistry/

# Domain-aware validation
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --domain chemistry \
  --directory domain/natural-sciences/chemistry/
```

## Common Migration Scenarios

### Scenario 1: Simple Domain Migration
**Use Case**: Migrating a complete domain (e.g., chemistry)

```bash
# Dry run first
python domain/_ontology/tools/migrate_domain.py \
  --source science/chemistry \
  --target natural-sciences/chemistry \
  --dry-run

# Execute
python domain/_ontology/tools/migrate_domain.py \
  --source science/chemistry \
  --target natural-sciences/chemistry
```

### Scenario 2: Subdomain Migration
**Use Case**: Migrating a specific subdomain (e.g., algebra)

```bash
python domain/_ontology/tools/migrate_domain.py \
  --source science/math/algebra \
  --target formal-sciences/mathematics/pure-mathematics/algebra
```

### Scenario 3: Reorganizing Content
**Use Case**: Moving content to different organization

```bash
python domain/_ontology/tools/migrate_domain.py \
  --source old/path/biology \
  --target natural-sciences/biology
```

## Migration Checklist

Before migration:
- [ ] Check global-hierarchy.yaml for correct target path
- [ ] Run dry-run to preview changes
- [ ] Verify AKU count matches expectations
- [ ] Check for data quality issues (missing classification)

During migration:
- [ ] Monitor output for errors
- [ ] Note any skipped files
- [ ] Verify success count

After migration:
- [ ] Validate migrated AKUs
- [ ] Create README in new location
- [ ] Update parent README with content
- [ ] Update structure.md
- [ ] Update Issue #3 or create new tracking issue
- [ ] Commit changes with clear message

## Handling Common Issues

### Issue: AKUs Missing classification.domain_path

**Error**: `⚠️ Skipped unknown: no classification.domain_path`

**Solution**: Manually add classification section:
```json
{
  "classification": {
    "domain_path": "appropriate/path/here",
    "type": "definition",
    "difficulty": "intermediate",
    "importance": "foundational"
  }
}
```

### Issue: Wrong Domain Path After Migration

**Error**: Domain path doesn't match expected pattern

**Solution**: Check that source path matches beginning of current domain_path in AKUs. The migration tool does string replacement.

### Issue: Some AKUs Not Found

**Error**: Fewer AKUs than expected

**Solution**: 
1. Check if AKUs are in subdirectories
2. Verify .json file extension
3. Look for hidden files or directories

## Best Practices

### 1. Always Dry-Run First
```bash
# Good
migrate_domain.py --source X --target Y --dry-run  # Preview first
migrate_domain.py --source X --target Y            # Then execute

# Bad  
migrate_domain.py --source X --target Y            # Execute without preview
```

### 2. Migrate in Logical Order
1. Formal sciences first (mathematics, computer science)
2. Natural sciences second (physics, chemistry, biology)
3. Social sciences third (economics, psychology, sociology)
4. Health sciences fourth (medicine, nursing, pharmacy)

### 3. Validate Immediately
```bash
# Good - validate right after migration
migrate_domain.py --source X --target Y
validate_cross_domain.py --directory domain/Y/

# Bad - migrate many domains then validate
migrate_domain.py --source X1 --target Y1
migrate_domain.py --source X2 --target Y2
migrate_domain.py --source X3 --target Y3
validate_cross_domain.py --directory domain/Y1/  # Too late to catch issues
```

### 4. Document As You Go
Create README.md in each new domain directory:
- Overview of content
- Migration details
- Statistics
- Contributing guidelines

## Advanced Usage

### Custom Script for Batch Migration

```bash
#!/bin/bash
# batch_migrate.sh

DOMAINS=(
  "science/chemistry:natural-sciences/chemistry"
  "science/biology:natural-sciences/biology"  
  "science/geology:natural-sciences/earth-sciences/geology"
)

for domain in "${DOMAINS[@]}"; do
  SOURCE="${domain%:*}"
  TARGET="${domain#*:}"
  
  echo "Migrating $SOURCE -> $TARGET"
  python domain/_ontology/tools/migrate_domain.py \
    --source "$SOURCE" \
    --target "$TARGET"
done
```

### Validation Summary Script

```bash
#!/bin/bash
# validate_all.sh

DOMAINS=(
  "domain/formal-sciences/mathematics"
  "domain/natural-sciences/physics"
  "domain/social-sciences/economics"
  "domain/health-sciences/medicine"
)

for domain in "${DOMAINS[@]}"; do
  echo "Validating $domain"
  python domain/_ontology/tools/validate_cross_domain.py \
    --directory "$domain"
done
```

## Reference

### Migration Tool Options
```
--source SOURCE      Source domain path (required)
--target TARGET      Target domain path (required)
--dry-run           Preview changes without writing (optional)
```

### Validation Tool Options
```
--directory DIR      Validate all AKUs in directory (optional)
--hierarchy FILE     Path to global-hierarchy.yaml (optional)
--verbose           Show detailed output (optional)
path                Single AKU file to validate (optional)
```

## Examples from This Project

### Successfully Completed Migrations

1. **Category Theory** (specialized script)
   ```bash
   python domain/_ontology/tools/migrate_category_theory.py
   # Result: 8/8 migrated
   ```

2. **Physics**
   ```bash
   python domain/_ontology/tools/migrate_domain.py \
     --source science/physics \
     --target natural-sciences/physics
   # Result: 136/138 migrated (99.5%)
   ```

3. **Medicine**
   ```bash
   python domain/_ontology/tools/migrate_domain.py \
     --source medicine \
     --target health-sciences/medicine
   # Result: 64/67 migrated (95.5%)
   ```

## Getting Help

- **Global Hierarchy**: See `domain/_ontology/global-hierarchy.yaml`
- **Migration Guide**: See `domain/_ontology/MIGRATION-GUIDE.md`
- **Validation Report**: See `domain/_ontology/VALIDATION-REPORT.md`
- **Migration Summary**: See `domain/_ontology/MIGRATION-SUMMARY.md`

## Success Criteria

✅ Migration Successful When:
- All (or 95%+) AKUs migrated
- Validation passes
- README created
- Documentation updated
- Changes committed

---

**Quick Reference Card**:
```bash
# 1. Dry run
migrate_domain.py --source OLD --target NEW --dry-run

# 2. Execute
migrate_domain.py --source OLD --target NEW

# 3. Validate
validate_cross_domain.py --directory domain/NEW/

# 4. Document
# Create README.md in domain/NEW/

# 5. Commit
git add . && git commit -m "Migrated OLD to NEW"
```

**Ready to migrate? Follow the 3 steps above!**
