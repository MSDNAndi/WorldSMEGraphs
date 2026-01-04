# Domain Migration Checklist Template

> **Purpose**: Step-by-step checklist for migrating content to the new domain hierarchy following the native domain principle.

## Pre-Migration Planning

### 1. Identify Content Domain
- [ ] Determine the **native domain** (where concept originated)
- [ ] Verify against `domain/_ontology/global-hierarchy.yaml`
- [ ] Check if this is a native or application domain
- [ ] Document rationale for placement

**Questions to Answer**:
- Where did this concept originate historically?
- Which field claims this as foundational knowledge?
- Is this applying someone else's concept?

**Example**:
- ✅ **Category Theory** → Mathematics (originated there)
- ❌ **Category Theory** → Computer Science (applies it, doesn't own it)

### 2. Review Current Structure
- [ ] List all AKUs to be migrated
- [ ] Document current paths
- [ ] Identify dependencies and cross-references
- [ ] Note any special files (terminology, examples, etc.)

**Inventory Template**:
```
Source: science/computer-science/functional-theory/category-theory/
Target: formal-sciences/mathematics/pure-mathematics/category-theory/
AKUs: 8 files
Dependencies: Functional programming (19 AKUs need cross-refs)
```

### 3. Check Global Hierarchy
- [ ] Verify target path exists in `global-hierarchy.yaml`
- [ ] Confirm subdomain structure
- [ ] Identify required intermediate directories
- [ ] Check for naming conflicts

**Validation**:
```bash
grep -A 10 "formal-sciences" domain/_ontology/global-hierarchy.yaml
```

---

## Migration Preparation

### 4. Create Target Structure
- [ ] Create domain root if needed (e.g., `formal-sciences/`)
- [ ] Create subdomain directories
- [ ] Create `akus/` subdirectory for AKUs
- [ ] Create `.renders/` subdirectory for human content
- [ ] Preserve any existing subdirectory structure

**Command**:
```bash
mkdir -p formal-sciences/mathematics/pure-mathematics/category-theory/akus
mkdir -p formal-sciences/mathematics/pure-mathematics/category-theory/.renders
```

### 5. Backup Current State
- [ ] Document current git commit hash
- [ ] Create backup branch if desired
- [ ] Take inventory of files to migrate
- [ ] Document any manual changes needed

**Commands**:
```bash
git log -1 --oneline  # Note current commit
git branch backup-before-migration  # Optional safety branch
```

---

## Migration Execution

### 6. Run Migration Script (Dry Run)
- [ ] Use `migrate_domain.py` with `--dry-run` flag
- [ ] Review planned changes carefully
- [ ] Check for any warnings or errors
- [ ] Verify all files will be migrated

**Command**:
```bash
python domain/_ontology/tools/migrate_domain.py \
  --source "science/computer-science/functional-theory/category-theory" \
  --target "formal-sciences/mathematics/pure-mathematics/category-theory" \
  --dry-run
```

**Review Checklist**:
- [ ] Source files identified correctly?
- [ ] Target paths correct?
- [ ] Subdirectories preserved?
- [ ] All AKUs included?
- [ ] No unintended files included?

### 7. Execute Migration
- [ ] Run migration script without `--dry-run`
- [ ] Monitor for errors
- [ ] Verify files copied correctly
- [ ] Check that updates were made to AKUs

**Command**:
```bash
python domain/_ontology/tools/migrate_domain.py \
  --source "science/computer-science/functional-theory/category-theory" \
  --target "formal-sciences/mathematics/pure-mathematics/category-theory"
```

**Expected Changes**:
- [ ] `classification.domain_path` updated in all AKUs
- [ ] `isNativeDomain` set correctly
- [ ] `modified` timestamps updated
- [ ] Files physically moved to new location

---

## Post-Migration Validation

### 8. Validate Migrated AKUs
- [ ] Run AKU validator on migrated files
- [ ] Check for structural errors
- [ ] Verify all required fields present
- [ ] Confirm domain_path correctness

**Commands**:
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-001-historical-origins.json

# Validate all in directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory formal-sciences/mathematics/pure-mathematics/category-theory/akus/
```

**Expected Results**:
- [ ] All AKUs pass validation
- [ ] Minor warnings acceptable (see TROUBLESHOOTING.md)
- [ ] No critical errors

### 9. Validate Cross-Domain Links
- [ ] Run cross-domain validator
- [ ] Verify `isNativeDomain` flag correct
- [ ] Check `cross_domain_applications` if native
- [ ] Verify all paths point to existing files

**Commands**:
```bash
# Check single AKU
python domain/_ontology/tools/validate_cross_domain.py \
  formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-002-category-definition.json

# Check directory
python domain/_ontology/tools/validate_cross_domain.py \
  --directory formal-sciences/mathematics/pure-mathematics/category-theory/akus/
```

### 10. Test Migration Tools
- [ ] Verify migration script still works
- [ ] Test on sample AKU if needed
- [ ] Confirm no regressions introduced
- [ ] Document any issues found

---

## Cross-Domain Reference Updates

### 11. Identify Application Domains
- [ ] List all domains that apply this concept
- [ ] Find AKUs in application domains
- [ ] Document needed cross-references
- [ ] Plan update strategy

**Example**:
- Native: Category theory in mathematics
- Applications: Functional programming, type theory
- Action: Update FP AKUs with cross-references

### 12. Update Application Domain AKUs
- [ ] Add `cross_domain_references` section
- [ ] Include proper `@id` fields
- [ ] Specify relationship type
- [ ] Add application context
- [ ] Set `isApplicationDomain: true`

**Script**:
```bash
python domain/_ontology/tools/update_fp_cross_domain.py \
  --source "science/computer-science/functional-theory"
```

**Required Fields**:
```json
{
  "classification": {
    "isApplicationDomain": true,
    "isNativeDomain": false
  },
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
      "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
      "relationship": "applies",
      "applicationContext": "Describes usage in application domain"
    }]
  }
}
```

### 13. Validate Cross-References
- [ ] Check all `@id` fields resolve
- [ ] Verify paths exist
- [ ] Test relationship descriptions
- [ ] Confirm bidirectional awareness (if applicable)

---

## Documentation Updates

### 14. Create/Update README
- [ ] Create README.md in new domain directory
- [ ] Document content overview
- [ ] Explain domain purpose
- [ ] List subdisciplines
- [ ] Provide navigation guidance
- [ ] Add contributing guidelines

**Template Sections**:
```markdown
# [Domain Name]

## Overview
## Content Structure
## Navigation
## Cross-Domain Relationships
## Contributing
## Validation
## References
```

### 15. Update Project Documentation
- [ ] Update `.project/structure.md` with new paths
- [ ] Update `MIGRATION-SUMMARY.md` with status
- [ ] Add entry to `VALIDATION-REPORT.md`
- [ ] Update domain root README if needed
- [ ] Document in session log

**Files to Update**:
- `.project/structure.md` - Current structure
- `domain/_ontology/MIGRATION-SUMMARY.md` - Migration record
- `domain/_ontology/VALIDATION-REPORT.md` - QA results
- `domain/[domain-root]/README.md` - Domain overview

### 16. Update Migration Status
- [ ] Mark migration complete in tracking docs
- [ ] Update statistics (AKU counts, success rate)
- [ ] Note any pending work
- [ ] Document lessons learned

---

## Quality Assurance

### 17. Code Review
- [ ] Review all changes systematically
- [ ] Check for unintended modifications
- [ ] Verify file permissions preserved
- [ ] Confirm no accidental deletions

**Review Areas**:
- [ ] AKU structure and content
- [ ] File paths and naming
- [ ] Cross-references accuracy
- [ ] Documentation completeness

### 18. Regression Testing
- [ ] Test migration tools still work
- [ ] Verify validators function correctly
- [ ] Check that existing content unaffected
- [ ] Confirm no breaking changes

**Test Commands**:
```bash
# Test migration tool
python domain/_ontology/tools/migrate_domain.py --help

# Test validators
python .project/agents/quality-assurance/tools/validate_aku_v2.py --help
python domain/_ontology/tools/validate_cross_domain.py --help
```

### 19. Peer Review (if applicable)
- [ ] Request agent review
- [ ] Address feedback
- [ ] Make necessary adjustments
- [ ] Document changes

---

## Finalization

### 20. Commit Changes
- [ ] Stage all migrated files
- [ ] Use descriptive commit message
- [ ] Include co-author tags if applicable
- [ ] Reference related issues

**Commit Message Template**:
```
Progress report: Migrated [domain] content to new hierarchy ([N] AKUs)

- Migrated [N] AKUs from [source] → [target]
- Updated domain_path and classification
- Added cross-domain references to [application domains]
- Created comprehensive README
- Validated all content (X/Y pass rate)

Addresses: #[issue-number]
```

### 21. Push and Verify
- [ ] Push changes to remote
- [ ] Verify all files uploaded
- [ ] Check CI/CD if applicable
- [ ] Confirm no merge conflicts

### 22. Post-Migration Cleanup (Future)
- [ ] Mark legacy paths as deprecated
- [ ] Add migration notices in legacy locations
- [ ] Plan eventual removal of old structure
- [ ] Document deprecation timeline

**Note**: Do NOT delete legacy paths immediately. Allow transition period.

---

## Troubleshooting

### Common Issues

#### Issue: Migration script fails
**Symptoms**: Script errors, no files migrated
**Solutions**:
1. Check source path exists and is correct
2. Verify target path doesn't already exist
3. Ensure write permissions
4. Check for special characters in paths
5. See `TROUBLESHOOTING.md` for details

#### Issue: Validation fails after migration
**Symptoms**: AKUs marked invalid
**Solutions**:
1. Check `classification.domain_path` format
2. Verify all required fields present
3. Confirm domain path in global hierarchy
4. Check for syntax errors in JSON
5. Review `VALIDATION-REPORT.md` for patterns

#### Issue: Cross-references broken
**Symptoms**: `@id` fields don't resolve
**Solutions**:
1. Verify target AKU exists at specified path
2. Check path format (wsmg: prefix, slashes)
3. Confirm sourceDomain accurate
4. Update after native domain migration
5. Use cross-domain validator

#### Issue: AKU missing classification.domain_path
**Symptoms**: Skipped during migration
**Solutions**:
1. Manually add `classification.domain_path` field
2. Determine correct domain from content
3. Use template from valid AKU
4. Re-run migration script
5. See manual fix guide in `TROUBLESHOOTING.md`

---

## Success Criteria

### Migration Complete When:
- [x] All AKUs migrated to correct domain
- [x] 95%+ validation pass rate
- [x] Cross-domain references properly linked
- [x] Documentation created/updated
- [x] No breaking changes introduced
- [x] Code review passed
- [x] Changes committed and pushed

### Quality Metrics:
- **Target Success Rate**: ≥95%
- **Validation**: All critical checks pass
- **Cross-Refs**: 100% resolve correctly
- **Documentation**: Comprehensive and accurate
- **Breaking Changes**: 0

---

## Reference Materials

### Key Documents
- `domain/_ontology/global-hierarchy.yaml` - Authoritative structure
- `domain/_ontology/MIGRATION-GUIDE.md` - Detailed migration guide
- `domain/_ontology/MIGRATION-QUICKSTART.md` - Quick start guide
- `domain/_ontology/TROUBLESHOOTING.md` - Common issues
- `domain/_ontology/INDEX.md` - Documentation index

### Tools
- `migrate_domain.py` - General-purpose migration
- `migrate_category_theory.py` - Specialized migration
- `update_fp_cross_domain.py` - Cross-reference updater
- `validate_aku_v2.py` - AKU validator
- `validate_cross_domain.py` - Cross-domain validator

### Examples
- Category theory migration (8 AKUs) - Reference implementation
- Functional programming updates (19 AKUs) - Cross-ref example
- Physics migration (136 AKUs) - Large-scale example

---

## Checklist Summary

**Quick Reference** - Mark each phase complete:

- [ ] Pre-Migration Planning (Steps 1-3)
- [ ] Migration Preparation (Steps 4-5)
- [ ] Migration Execution (Steps 6-7)
- [ ] Post-Migration Validation (Steps 8-10)
- [ ] Cross-Domain References (Steps 11-13)
- [ ] Documentation Updates (Steps 14-16)
- [ ] Quality Assurance (Steps 17-19)
- [ ] Finalization (Steps 20-22)

**Estimated Time**: 2-4 hours for small migration, 1-2 days for large migration

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Status**: Comprehensive template based on successful migrations

