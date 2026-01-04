# Migration Troubleshooting Guide

> **Purpose**: Solutions for common migration issues  
> **Version**: 1.0.0  
> **Date**: 2026-01-04

## Common Issues and Solutions

### Issue 1: AKUs Missing classification.domain_path

**Symptom**:
```
⚠️  Skipped unknown: no classification.domain_path
```

**Cause**: AKU JSON file lacks the required `classification.domain_path` field

**Impact**: Cannot be automatically migrated

**Solution**:

1. **Locate the problematic AKU**:
   ```bash
   # AKU will be in the source directory but not migrated
   find domain/SOURCE_PATH -name "*.json" -type f
   ```

2. **Add classification section**:
   ```json
   {
     "@context": "...",
     "@type": "...",
     "@id": "...",
     "metadata": { ... },
     
     "classification": {
       "domain_path": "appropriate/domain/path/here",
       "type": "definition|formula|example|theorem|procedure",
       "difficulty": "beginner|intermediate|advanced|expert",
       "importance": "foundational|important|specialized|peripheral",
       "maturity": "draft|stable|validated|deprecated"
     },
     
     "content": { ... }
   }
   ```

3. **Determine correct domain_path**:
   - Consult `domain/_ontology/global-hierarchy.yaml`
   - Follow native domain principle (origin, not application)
   - Use hierarchical path: `domain/subdomain/topic`

4. **Re-run migration**:
   ```bash
   python domain/_ontology/tools/migrate_domain.py \
     --source OLD_PATH \
     --target NEW_PATH
   ```

**Affected in Current Migration**:
- Economics: 11 AKUs (in `economics/bwl/` subdirectories)
- Medicine: 3 AKUs (terminology files in vascular surgery)
- Physics: 2 AKUs (investigation needed)

---

### Issue 2: Domain Path Not in Global Hierarchy

**Symptom**:
```
⚠️  Domain path 'X' not found in global hierarchy
```

**Cause**: The domain_path doesn't match any path in `global-hierarchy.yaml`

**Impact**: Warning only - validation proceeds with generic rules

**Solution**:

**Option A - Update AKU** (if path is wrong):
1. Check `domain/_ontology/global-hierarchy.yaml` for correct path
2. Update AKU's `classification.domain_path`
3. Re-run migration

**Option B - Update Hierarchy** (if path is correct):
1. Add the path to `global-hierarchy.yaml`
2. Follow existing hierarchy structure
3. Commit the updated hierarchy file

**Option C - Accept Warning** (legacy paths):
- If using legacy paths temporarily, warning is expected
- Will resolve when content migrated to new paths
- No action needed if migration planned

**Current Example**:
- Functional programming AKUs use `science/computer-science/functional-theory/*`
- This is legacy path, not in new hierarchy
- ✅ Acceptable - migration to `formal-sciences/computer-science/` planned

---

### Issue 3: Migration Tool Says "No AKUs Found"

**Symptom**:
```
❌ No AKU files found in source directory!
```

**Cause**: No `.json` files in source directory, or source path incorrect

**Solution**:

1. **Verify source path exists**:
   ```bash
   ls -la domain/SOURCE_PATH/
   ```

2. **Check for JSON files**:
   ```bash
   find domain/SOURCE_PATH -name "*.json" -type f
   ```

3. **Common mistakes**:
   - Typo in source path
   - Missing `domain/` prefix
   - AKUs in subdirectories (tool searches recursively, should work)
   - Hidden files or directories

4. **Debug**:
   ```bash
   # List all JSON files
   find domain/SOURCE_PATH -name "*.json" -type f -ls
   
   # Check specific subdirectory
   ls -R domain/SOURCE_PATH/
   ```

---

### Issue 4: Validation Fails After Migration

**Symptom**:
```
❌ Invalid with N error(s)
```

**Cause**: Migrated AKU has structural or content issues

**Solution**:

1. **Review error message**:
   ```bash
   python domain/_ontology/tools/validate_cross_domain.py \
     PATH/TO/AKU.json --verbose
   ```

2. **Common validation errors**:

   **Missing @id field**:
   ```json
   {
     "@id": "wsmg:domain/subdomain/topic/concept-id"
   }
   ```

   **Missing cross_domain_references @id**:
   ```json
   "cross_domain_references": {
     "applies": [{
       "@id": "wsmg:path/to/concept",  // ← Must be present
       "sourceDomain": "...",
       "relationship": "applies"
     }]
   }
   ```

   **Invalid JSON**:
   - Check for missing commas
   - Check for trailing commas in last element
   - Validate JSON syntax online

3. **Re-validate after fix**:
   ```bash
   python domain/_ontology/tools/validate_cross_domain.py PATH/TO/AKU.json
   ```

---

### Issue 5: "Unknown domain" Warning

**Symptom**:
```
⚠️  Unknown domain 'health-sciences' - using generic validation
```

**Cause**: Validator doesn't have domain-specific rules for this domain

**Impact**: Warning only - validation uses generic rules and still works

**Solution**:

**Short-term**: Accept the warning
- Generic validation is sufficient for most cases
- AKUs will still validate correctly
- No blocking issue

**Long-term**: Add domain-specific rules
1. Edit `.project/agents/quality-assurance/tools/validate_aku_v2.py`
2. Add domain to DOMAIN_RULES dictionary
3. Define domain-specific validation logic
4. Test with sample AKUs

**Not Urgent**: Generic validation is adequate

---

### Issue 6: Dry-Run vs. Actual Run Discrepancy

**Symptom**: Dry-run shows different results than actual run

**Cause**: File system state changed between runs (rare)

**Solution**:

1. **Always re-run dry-run immediately before actual**:
   ```bash
   # Run these back-to-back
   migrate_domain.py --source X --target Y --dry-run
   migrate_domain.py --source X --target Y
   ```

2. **Check for concurrent modifications**:
   - Ensure no one else is modifying files
   - Check git status for uncommitted changes

3. **If discrepancy occurs**:
   - Trust the actual run (it reads files fresh)
   - Dry-run is preview only
   - Validate results regardless

---

### Issue 7: Git Merge Conflicts After Migration

**Symptom**: Merge conflicts when pulling/merging migration branch

**Cause**: Someone else modified same files in different branch

**Solution**:

1. **For new files** (most migrated AKUs):
   - Accept both versions (they're in different locations)
   - No conflict should occur

2. **For modified files** (updated domain_paths):
   - Review both changes carefully
   - If migration is correct, accept migration version
   - If other change is important, manually integrate

3. **Prevention**:
   - Communicate before large migrations
   - Use feature branches
   - Migrate frequently to avoid large conflicts

---

### Issue 8: Performance - Migration Takes Too Long

**Symptom**: migrate_domain.py takes minutes for hundreds of AKUs

**Cause**: Normal - tool processes each AKU individually

**Solution**:

**For Current Tool**:
- Expected: ~1 second per AKU
- 100 AKUs = ~1.5 minutes
- Be patient for large migrations

**Optimization Options** (future):
- Parallel processing (use multiprocessing)
- Batch file operations
- Skip validation in migration tool (validate separately)

**Workaround**:
- Run dry-run first (faster, no writes)
- Migrate subdirectories separately
- Use `time` command to measure actual duration

---

### Issue 9: Wrong Domain Path After Migration

**Symptom**: Migrated AKU has incorrect or unexpected domain_path

**Cause**: Original AKU's domain_path didn't start with source path

**Explanation**: Tool does string replacement:
- Looks for domain_path starting with `--source` value
- Replaces with `--target` value
- If source path doesn't match, no replacement occurs

**Solution**:

1. **Check original AKU**:
   ```bash
   git show HEAD~1:path/to/original/aku.json | grep domain_path
   ```

2. **Verify source path matches**:
   - Source: `science/physics`
   - AKU path: `science/physics/quantum/...` ✅
   - AKU path: `physics/quantum/...` ❌ (no "science/" prefix)

3. **Fix**:
   - Update original AKU to have correct base path
   - Or adjust --source parameter to match actual path
   - Re-run migration

---

### Issue 10: Need to Undo Migration

**Symptom**: Migration went to wrong location or had errors

**Solution**:

**Option A - Delete and Re-migrate**:
```bash
# Remove incorrectly migrated content
rm -rf domain/TARGET_PATH/

# Re-run migration with correct parameters
python domain/_ontology/tools/migrate_domain.py \
  --source CORRECT_SOURCE \
  --target CORRECT_TARGET
```

**Option B - Git Reset** (if not pushed):
```bash
# Undo last commit
git reset --soft HEAD~1

# Review changes
git status

# Re-do migration correctly
```

**Option C - Manual Fix**:
- Edit domain_paths in migrated AKUs
- Move files to correct locations
- Update timestamps

**Best Practice**: Always use --dry-run first!

---

## Prevention Checklist

Before migrating:
- [ ] Run dry-run first
- [ ] Review dry-run output carefully
- [ ] Check global-hierarchy.yaml for correct target path
- [ ] Verify source path contains JSON files
- [ ] Check sample AKU has classification.domain_path
- [ ] Have backup or committed clean state

During migration:
- [ ] Monitor output for errors
- [ ] Note any skipped files
- [ ] Check success count matches expectations

After migration:
- [ ] Validate migrated AKUs
- [ ] Review a few sample files manually
- [ ] Run git status to see what changed
- [ ] Commit with clear message
- [ ] Update documentation

---

## Getting Help

If stuck:
1. Check this troubleshooting guide
2. Review migration examples in MIGRATION-SUMMARY.md
3. Consult MIGRATION-QUICKSTART.md
4. Review validation errors carefully
5. Check domain/_ontology/INDEX.md for related docs

Still stuck?
- Add to `.project/issues.md`
- Document the problem clearly
- Include error messages and context

---

**Document Version**: 1.0.0  
**Last Updated**: 2026-01-04  
**Based on**: Real issues encountered during 228-AKU migration
