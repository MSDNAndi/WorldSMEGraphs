# Domain Migration Guide

**Purpose**: Guide for migrating domains to the WorldSMEGraphs global hierarchy  
**Audience**: Project maintainers, contributors, and agents  
**Last Updated**: 2026-01-04

## Overview

This guide documents the process for migrating domain content to comply with the global domain hierarchy defined in `domain/_ontology/global-hierarchy.yaml`. Use this as a reference for future migrations or domain reorganizations.

## Prerequisites

Before starting a migration:

1. **Review Global Hierarchy**
   - Read `domain/_ontology/global-hierarchy.yaml`
   - Understand the native domain principle
   - Identify correct placement for your content

2. **Backup Current State**
   - Create a git branch for migration work
   - Document current file locations
   - Count files to verify nothing is lost

3. **Available Tools**
   - `domain/_ontology/tools/migrate_domain.py` - General migration script
   - `domain/_ontology/tools/validate_cross_domain.py` - Link validator
   - `.project/agents/quality-assurance/tools/validate_aku_v2.py` - AKU validator

## Migration Process

### Phase 1: Analysis

1. **Inventory Current Content**
   ```bash
   # Count files in old location
   find domain/old-path -name "*.json" -type f | wc -l
   
   # List all subdirectories
   find domain/old-path -type d
   ```

2. **Determine Target Location**
   - Consult `global-hierarchy.yaml` for correct path
   - Apply native domain principle: place concepts in their origin field
   - Examples:
     - Category theory → `formal-sciences/mathematics/pure-mathematics/category-theory/`
     - Economics → `social-sciences/economics/`
     - Medicine → `health-sciences/medicine/`

3. **Check for Duplicates**
   - Verify if content already exists in new location
   - Compare file contents to confirm duplication
   - Document which files are duplicates vs. need migration

### Phase 2: Preparation

1. **Create Target Directories**
   ```bash
   mkdir -p domain/target-path/subdirs/
   ```

2. **Document Migration Plan**
   - List all files to migrate
   - Note any that need special handling
   - Identify files that will be removed (duplicates)

3. **Identify Missing Files**
   - Check for metadata files (`.metadata.json`)
   - Check for schema files (`schema.json`)
   - Check for terminology files
   - Document files that need to be created in new location

### Phase 3: Migration

1. **Migrate Files to New Location**
   ```bash
   # For entire directories
   cp -r domain/old-path/subdir domain/new-path/subdir
   
   # For individual files
   cp domain/old-path/file.json domain/new-path/file.json
   ```

2. **Add Missing Files**
   - Copy any files that were in old location but missing in new
   - Maintain directory structure within new hierarchy

3. **Verify File Counts**
   ```bash
   # Count in old location
   OLD_COUNT=$(find domain/old-path -name "*.json" | wc -l)
   
   # Count in new location  
   NEW_COUNT=$(find domain/new-path -name "*.json" | wc -l)
   
   # Should match if complete migration
   echo "Old: $OLD_COUNT, New: $NEW_COUNT"
   ```

### Phase 4: Validation

1. **Validate Migrated AKUs**
   ```bash
   # Validate sample from each subdirectory
   python .project/agents/quality-assurance/tools/validate_aku_v2.py \
     domain/new-path/subdir/file.json
   ```

2. **Check Cross-Domain Links**
   ```bash
   # Validate cross-domain references
   python domain/_ontology/tools/validate_cross_domain.py \
     domain/new-path/subdir/file.json
   ```

3. **Verify Directory Structure**
   ```bash
   # View new structure
   tree -L 4 -d domain/new-path/
   ```

### Phase 5: Cleanup

1. **Remove Old Directories**
   ```bash
   # ONLY after verification complete
   rm -rf domain/old-path
   ```

2. **Update Documentation**
   - `.project/structure.md` - Update hierarchy diagram
   - `README.md` - Update any path references
   - Domain-specific READMEs if needed

3. **Update Path References**
   - Check Python scripts for hardcoded paths
   - Check Markdown files for old links
   - Check workflow files

### Phase 6: Git Operations

1. **Stage Changes**
   ```bash
   git add -A
   ```

2. **Review Staged Changes**
   ```bash
   # Should show renames (R) not deletions + additions
   git status --short
   ```

3. **Commit with Clear Message**
   ```bash
   git commit -m "Progress report: Migrate [domain] to new hierarchy

   - Migrated X files from old-path to new-path
   - Added Y missing files
   - Removed Z duplicate files
   - Removed old directory
   
   Session: Nm NNs, continuing..."
   ```

## Best Practices

### During Migration

1. **Preserve Structure**: Maintain subdirectory organization within new location
2. **Check Duplicates**: Always verify files don't already exist
3. **Document Decisions**: Note why files were placed in specific locations
4. **Test Incrementally**: Validate as you migrate, not at the end
5. **Use Git Properly**: Let git detect renames by copying then deleting

### After Migration

1. **Run Full Validation**: Test sample from every subdirectory
2. **Update All Docs**: Don't leave references to old paths
3. **Check Cross-References**: Ensure AKUs don't reference old paths
4. **Clean Working Directory**: No untracked files left behind

### Common Mistakes to Avoid

1. **Don't Delete First**: Always copy to new location, verify, then delete old
2. **Don't Forget Metadata**: Include .metadata.json, schema.json, terminology files
3. **Don't Skip Validation**: Always validate before removing old files
4. **Don't Leave Duplicates**: Remove old location after verification
5. **Don't Forget Documentation**: Update structure.md, README.md, etc.

## Checklist

Use this checklist for any migration:

- [ ] Reviewed global-hierarchy.yaml
- [ ] Identified correct target location
- [ ] Counted files in old location
- [ ] Checked for existing content in new location
- [ ] Documented migration plan
- [ ] Created target directories
- [ ] Migrated files to new location
- [ ] Added any missing files
- [ ] Verified file counts match
- [ ] Validated sample AKUs
- [ ] Checked cross-domain links
- [ ] Removed old directories
- [ ] Updated structure.md
- [ ] Updated README.md
- [ ] Updated path references in code
- [ ] Updated validators if needed
- [ ] Committed with clear message
- [ ] Created migration report

## Resources

- **Global Hierarchy**: `domain/_ontology/global-hierarchy.yaml`
- **Structure Docs**: `.project/structure.md`
- **Migration Example**: `.project/tracking/migration-pr30-completion-report.md`
- **Validation Report**: `.project/tracking/post-migration-validation-report.md`

---

**Version**: 1.0.0  
**Created**: 2026-01-04  
**Based On**: PR #30 Migration Completion  
**Maintained By**: File Organization Agent, Ontology Agent
