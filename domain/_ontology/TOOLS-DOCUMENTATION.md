# Migration Tools Documentation

> **Purpose**: Comprehensive documentation for all migration tools in WorldSMEGraphs, including usage examples, options, and best practices.

## Available Tools

### Overview Table

| Tool | Purpose | Complexity | Use Case |
|------|---------|------------|----------|
| `migrate_domain.py` | General-purpose migration | ★★☆☆☆ | Any domain migration |
| `migrate_category_theory.py` | Category theory specific | ★★★☆☆ | Category theory → Math |
| `update_fp_cross_domain.py` | Cross-domain references | ★★★☆☆ | Add cross-refs to FP AKUs |
| `validate_aku_v2.py` | AKU validation | ★☆☆☆☆ | Validate AKU structure |
| `validate_cross_domain.py` | Cross-domain validation | ★★☆☆☆ | Validate cross-refs |

---

## Tool 1: migrate_domain.py

### Description
General-purpose migration tool for moving content from legacy to new hierarchy. Automatically updates `classification.domain_path`, sets `isNativeDomain`, and updates timestamps.

### Location
```
domain/_ontology/tools/migrate_domain.py
```

### Basic Usage
```bash
python domain/_ontology/tools/migrate_domain.py \
  --source "old/path" \
  --target "new/path"
```

### Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--source` | Yes | Source directory path | `science/physics` |
| `--target` | Yes | Target directory path | `natural-sciences/physics` |
| `--dry-run` | No | Preview without changes | Flag only |

### Examples

#### Example 1: Simple Domain Migration
```bash
# Migrate physics content
python domain/_ontology/tools/migrate_domain.py \
  --source "science/physics" \
  --target "natural-sciences/physics"
```

**What it does**:
1. Copies all AKUs from source to target
2. Preserves subdirectory structure
3. Updates `classification.domain_path` in each AKU
4. Sets `isNativeDomain: true`
5. Updates `modified` timestamp

**Output**:
```
=== Domain Migration Tool ===
Source: science/physics/
Target: natural-sciences/physics/

Found 138 AKU files to migrate

Processing: science/physics/quantum-mechanics/planck-units/akus/theory/aku-t01-holographic-principle.json
  Updated domain_path: natural-sciences/physics/quantum-mechanics/planck-units
  Set isNativeDomain: true
  Updated modified timestamp
✓ Migrated to: natural-sciences/physics/quantum-mechanics/planck-units/akus/theory/aku-t01-holographic-principle.json

[... 137 more files ...]

=== Migration Summary ===
Total files processed: 138
Successfully migrated: 136
Skipped (no domain_path): 2
Success rate: 99.5%
```

#### Example 2: Dry Run First (Recommended)
```bash
# Preview migration without making changes
python domain/_ontology/tools/migrate_domain.py \
  --source "medicine" \
  --target "health-sciences/medicine" \
  --dry-run
```

**What it does**:
1. Scans source directory
2. Shows what WOULD be migrated
3. Reports any issues
4. **Does NOT modify files**

**Output**:
```
=== Dry Run Mode - No Changes Will Be Made ===
Source: medicine/
Target: health-sciences/medicine/

Would migrate 67 AKU files:

Would create: health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/akus/definitions/aku-001-type2-endoleak-definition.json
  Current domain_path: medicine/surgery/vascular/complications/endoleaks/type-2
  New domain_path: health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2

[... more files ...]

Would skip 3 files (missing classification.domain_path):
  - medicine/surgery/vascular/complications/endoleaks/type-2/terminology/EXAMPLE-enhanced-aku.json

=== Dry Run Summary ===
Would migrate: 64
Would skip: 3
Estimated success rate: 95.5%

Run without --dry-run to execute migration.
```

#### Example 3: Economics Migration (With Known Issues)
```bash
# Attempt to migrate economics content
python domain/_ontology/tools/migrate_domain.py \
  --source "economics" \
  --target "social-sciences/economics" \
  --dry-run
```

**Output (showing issues)**:
```
=== Dry Run Mode ===
Found 12 AKU files

Would migrate 1 file:
  ✓ economics/bwl/finance/valuation/npv/akus/examples/example-npv-definition-with-semantic-annotations.json

Would skip 11 files (missing classification.domain_path):
  ⚠️ economics/bwl/finance/valuation/npv/akus/example-npv-definition.json
  ⚠️ economics/bwl/finance/valuation/npv/akus/npv-001-definition.json
  [... 9 more ...]

ACTION REQUIRED: Fix missing domain_path in 11 AKUs before migration
See TROUBLESHOOTING.md for guidance
```

### Error Handling

#### Error: Source Directory Not Found
```
Error: Source directory 'invalid/path' does not exist
```
**Solution**: Check path spelling, ensure you're in repository root

#### Error: Target Already Exists
```
Error: Target directory 'natural-sciences/physics' already exists
```
**Solution**: Use different target or manually merge if intentional

#### Warning: Files Skipped
```
Warning: Skipped 2 files missing classification.domain_path
```
**Solution**: See `TROUBLESHOOTING.md` section "Missing classification.domain_path"

### Best Practices

1. **Always dry-run first**:
   ```bash
   # Preview
   python migrate_domain.py --source "X" --target "Y" --dry-run
   # If looks good, execute
   python migrate_domain.py --source "X" --target "Y"
   ```

2. **Backup first** (optional but recommended):
   ```bash
   git branch backup-before-migration
   git log -1 --oneline  # Note commit hash
   ```

3. **Validate after**:
   ```bash
   python .project/agents/quality-assurance/tools/validate_aku_v2.py \
     --directory "new/path"
   ```

4. **Check cross-domain references** if native domain:
   ```bash
   python domain/_ontology/tools/validate_cross_domain.py \
     --directory "new/path"
   ```

---

## Tool 2: migrate_category_theory.py

### Description
Specialized tool for migrating category theory content from computer science to mathematics. More sophisticated than general tool - handles mathematical concepts moving to native domain.

### Location
```
domain/_ontology/tools/migrate_category_theory.py
```

### Basic Usage
```bash
python domain/_ontology/tools/migrate_category_theory.py
```

**Note**: Paths are hardcoded for category theory migration. No arguments needed.

### What It Does Specifically

1. **Migrates 8 AKUs**:
   ```
   FROM: science/computer-science/functional-theory/category-theory/
   TO:   formal-sciences/mathematics/pure-mathematics/category-theory/
   ```

2. **Updates Classification**:
   - Sets `isNativeDomain: true`
   - Updates `domain_path`
   - Adds `cross_domain_applications` field

3. **Updates Identifiers**:
   - Changes `@id`: `aku:functional-theory:*` → `aku:math:category-theory:*`
   - Preserves all other fields

4. **Creates README**:
   - Generates comprehensive README in new location
   - Documents native domain status
   - Lists cross-domain applications

### Example Run

```bash
python domain/_ontology/tools/migrate_category_theory.py
```

**Output**:
```
=== Category Theory Migration Tool ===
Migrating 8 category theory AKUs from CS to Mathematics

Source: science/computer-science/functional-theory/category-theory/
Target: formal-sciences/mathematics/pure-mathematics/category-theory/

✓ Created target directory
✓ Migrating ct-001-historical-origins.json
  - Updated domain_path
  - Set isNativeDomain: true
  - Changed @id prefix: aku:functional-theory → aku:math
  - Added cross_domain_applications

[... 7 more files ...]

✓ Created comprehensive README.md

=== Migration Complete ===
Migrated: 8/8 AKUs
Success rate: 100%
New location: formal-sciences/mathematics/pure-mathematics/category-theory/
```

### When to Use

Use this tool when:
- ✅ Migrating category theory specifically
- ✅ Want automated `@id` updates
- ✅ Need cross-domain applications added
- ✅ Want README auto-generated

Use general `migrate_domain.py` instead when:
- ❌ Migrating other content
- ❌ Don't need `@id` updates
- ❌ Want more control over process

---

## Tool 3: update_fp_cross_domain.py

### Description
Updates functional programming AKUs with cross-domain references linking to native mathematics definitions. Sets application domain flags.

### Location
```
domain/_ontology/tools/update_fp_cross_domain.py
```

### Basic Usage
```bash
python domain/_ontology/tools/update_fp_cross_domain.py \
  --source "science/computer-science/functional-theory"
```

### Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--source` | Yes | FP source directory | `science/computer-science/functional-theory` |

### What It Does

1. **Updates 19 FP AKUs** (6 functors, 5 monoids, 8 monads)

2. **Adds Classification Flags**:
   ```json
   {
     "classification": {
       "isApplicationDomain": true,
       "isNativeDomain": false
     }
   }
   ```

3. **Adds Cross-Domain References**:
   - Functors → link to math category theory
   - Monoids → link to math algebra
   - Monads → link to math category theory

4. **Updates Timestamps**:
   - Sets `modified` to current UTC time

### Example Run

```bash
python domain/_ontology/tools/update_fp_cross_domain.py \
  --source "science/computer-science/functional-theory"
```

**Output**:
```
=== Functional Programming Cross-Domain Reference Updater ===

Processing Functors (6 AKUs)...
✓ fn-001-functor-definition.json
  - Set isApplicationDomain: true
  - Added cross_domain_references to category theory
  - Updated timestamp

[... 5 more functors ...]

Processing Monoids (5 AKUs)...
✓ mo-001-monoid-definition.json
  - Set isApplicationDomain: true
  - Added cross_domain_references to algebra
  - Updated timestamp

[... 4 more monoids ...]

Processing Monads (8 AKUs)...
✓ md-001-monad-definition.json
  - Set isApplicationDomain: true
  - Added cross_domain_references to category theory
  - Updated timestamp

[... 7 more monads ...]

=== Update Complete ===
Total AKUs updated: 19
  Functors: 6
  Monoids: 5
  Monads: 8
Success rate: 100%
```

### Cross-Domain Reference Format

The tool adds references like this:

```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
      "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
      "relationship": "applies",
      "applicationContext": "Monads in FP structure effectful computations using mathematical foundation"
    }]
  }
}
```

### When to Use

Use this tool when:
- ✅ Linking application domains to native domains
- ✅ After native domain migration is complete
- ✅ Want automated cross-reference addition
- ✅ Need consistent reference format

---

## Tool 4: validate_aku_v2.py

### Description
Domain-aware AKU validator that checks structure, required fields, and domain-specific requirements.

### Location
```
.project/agents/quality-assurance/tools/validate_aku_v2.py
```

### Basic Usage
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/

# Validate entire domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine
```

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `<file>` | Single AKU file | `aku-001.json` |
| `--directory` | Directory of AKUs | `--directory domain/natural-sciences/physics/` |
| `--domain` | Domain name | `--domain medicine` |
| `--verbose` | Detailed output | Flag only |

### Examples

#### Example 1: Validate Single AKU
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-001-historical-origins.json
```

**Output (Success)**:
```
✓ formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-001-historical-origins.json
  Domain: formal-sciences/mathematics/pure-mathematics/category-theory
  Type: concept
  Required fields: ✓ All present
  Timestamps: ✓ Valid ISO 8601 format
  Classification: ✓ Valid domain_path
```

**Output (With Warnings)**:
```
⚠ formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-002-category-definition.json
  Domain: formal-sciences/mathematics/pure-mathematics/category-theory
  Type: definition
  Required fields: ✓ All present
  Warnings:
    - Missing 'explanation' in content.primary_definition
    - Consider adding 'cross_domain_applications' (native domain)
```

#### Example 2: Validate Entire Directory
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory natural-sciences/physics/quantum-mechanics/planck-units/akus/
```

**Output**:
```
Validating 102 AKU files...

✓ theory/aku-t01-holographic-principle.json
✓ theory/aku-t02-planck-epoch-cosmology.json
✓ theory/aku-t03-fundamental-limits-smallest-units.json
[... 99 more files ...]

=== Validation Summary ===
Total files: 102
Passed: 102
Failed: 0
Warnings: 8 (non-critical)
Success rate: 100%

Common warnings:
  - 5 files missing 'cross_domain_applications'
  - 3 files have complex definition structures
```

#### Example 3: Validate by Domain
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine
```

**Output**:
```
Scanning health-sciences/medicine/ domain...
Found 64 AKUs

Validating medicine AKUs...
✓ surgery/vascular/complications/endoleaks/type-2/akus/definitions/aku-001-type2-endoleak-definition.json
✓ surgery/vascular/complications/endoleaks/type-2/akus/definitions/aku-002-endoleak-classification.json
[... 62 more files ...]

=== Domain Validation: medicine ===
Total AKUs: 64
Valid: 64
Invalid: 0
Warnings: 2 (terminology files)
Domain-specific checks: ✓ Passed
```

### Validation Checks

The validator checks:

1. **Required Fields**:
   - `@context`, `@type`, `@id`
   - `metadata` (version, created, modified)
   - `classification` (domain_path, type)
   - `content`

2. **Format Validation**:
   - JSON syntax
   - ISO 8601 timestamps
   - Valid domain paths

3. **Domain-Specific Rules**:
   - Medicine: Clinical terminology
   - Mathematics: Formula notation
   - Physics: Units and measurements
   - Economics: Statistical data

4. **Cross-Domain Compliance**:
   - Native domains should have `isNativeDomain: true`
   - Application domains should have cross-refs
   - All `@id` refs should be valid

---

## Tool 5: validate_cross_domain.py

### Description
Validates cross-domain references and native/application domain markers.

### Location
```
domain/_ontology/tools/validate_cross_domain.py
```

### Basic Usage
```bash
# Validate single AKU
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Validate directory
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `<file>` | Single AKU file | `aku-001.json` |
| `--directory` | Directory of AKUs | `--directory domain/formal-sciences/` |

### Examples

#### Example 1: Validate Native Domain AKU
```bash
python domain/_ontology/tools/validate_cross_domain.py \
  formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-002-category-definition.json
```

**Output (Success)**:
```
✓ ct-002-category-definition.json
  Classification: Native Domain ✓
  isNativeDomain: true ✓
  Domain path matches hierarchy: ✓
  Recommendations:
    - Consider adding 'cross_domain_applications' to document usage in other fields
```

#### Example 2: Validate Application Domain AKU
```bash
python domain/_ontology/tools/validate_cross_domain.py \
  science/computer-science/functional-theory/monads/akus/md-001-monad-definition.json
```

**Output (Success)**:
```
✓ md-001-monad-definition.json
  Classification: Application Domain ✓
  isApplicationDomain: true ✓
  isNativeDomain: false ✓
  Cross-domain references: Present ✓
    → formal-sciences/mathematics/pure-mathematics/category-theory/monad
  Reference validity: ✓ Path exists
```

**Output (Issues)**:
```
✗ md-001-monad-definition.json
  Classification: Application Domain
  isApplicationDomain: true ✓
  isNativeDomain: false ✓
  Cross-domain references: ✗ MISSING
  
ERROR: Application domain AKU must include cross_domain_references
Add reference to native domain definition
```

#### Example 3: Validate Directory
```bash
python domain/_ontology/tools/validate_cross_domain.py \
  --directory science/computer-science/functional-theory/
```

**Output**:
```
Validating 19 AKUs in application domain...

Functors:
✓ fn-001-functor-definition.json
✓ fn-002-functor-laws.json
[... 4 more ...]

Monoids:
✓ mo-001-monoid-definition.json
[... 4 more ...]

Monads:
✓ md-001-monad-definition.json
[... 7 more ...]

=== Cross-Domain Validation Summary ===
Total AKUs: 19
Valid: 19
Invalid: 0
Missing cross-refs: 0
Broken refs: 0
Success rate: 100%
```

---

## Workflow Integration

### Complete Migration Workflow

```bash
# 1. Dry run migration
python domain/_ontology/tools/migrate_domain.py \
  --source "science/physics" \
  --target "natural-sciences/physics" \
  --dry-run

# 2. Execute migration
python domain/_ontology/tools/migrate_domain.py \
  --source "science/physics" \
  --target "natural-sciences/physics"

# 3. Validate migrated content
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory natural-sciences/physics/

# 4. Validate cross-domain compliance
python domain/_ontology/tools/validate_cross_domain.py \
  --directory natural-sciences/physics/

# 5. If application domain needs updating
python domain/_ontology/tools/update_fp_cross_domain.py \
  --source "science/computer-science/functional-theory"

# 6. Final validation
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --domain computer-science
```

### Batch Processing Script Example

```bash
#!/bin/bash
# batch-migrate.sh - Migrate multiple domains

DOMAINS=(
  "science/physics:natural-sciences/physics"
  "economics:social-sciences/economics"
  "medicine:health-sciences/medicine"
)

for DOMAIN_PAIR in "${DOMAINS[@]}"; do
  SRC="${DOMAIN_PAIR%%:*}"
  TGT="${DOMAIN_PAIR##*:}"
  
  echo "=== Migrating $SRC → $TGT ==="
  
  # Dry run
  python domain/_ontology/tools/migrate_domain.py \
    --source "$SRC" \
    --target "$TGT" \
    --dry-run
  
  # Prompt for confirmation
  read -p "Proceed with migration? (y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Execute
    python domain/_ontology/tools/migrate_domain.py \
      --source "$SRC" \
      --target "$TGT"
    
    # Validate
    python .project/agents/quality-assurance/tools/validate_aku_v2.py \
      --directory "$TGT"
  fi
done
```

---

## Troubleshooting

### Common Issues

See `TROUBLESHOOTING.md` for detailed solutions to:
1. Missing classification.domain_path
2. Domain path not in global hierarchy
3. No AKUs found
4. Validation failures
5. Cross-domain reference errors

### Quick Fixes

**Issue**: Import error
```
ModuleNotFoundError: No module named 'json'
```
**Solution**: Tools use Python standard library only, ensure Python 3.6+

**Issue**: Permission denied
```
PermissionError: [Errno 13] Permission denied
```
**Solution**: Check file permissions, run from repository root

**Issue**: Path not found
```
Error: Source directory not found
```
**Solution**: Use paths relative to repository root, check spelling

---

## Development

### Adding New Migration Tool

Template for new tool:

```python
#!/usr/bin/env python3
"""
Tool Name: my_migration_tool.py
Purpose: Describe what this tool does
"""

import json
import os
from pathlib import Path
from datetime import datetime

def migrate_content(source, target):
    """Main migration logic"""
    # Implementation
    pass

def validate_paths(source, target):
    """Validate source and target paths"""
    # Implementation
    pass

if __name__ == "__main__":
    # Argument parsing
    # Main logic
    pass
```

### Testing Tools

```bash
# Test on sample data first
mkdir -p /tmp/test-migration/source/subdir
cp sample.json /tmp/test-migration/source/subdir/

python domain/_ontology/tools/migrate_domain.py \
  --source "/tmp/test-migration/source" \
  --target "/tmp/test-migration/target"

# Verify results
ls -R /tmp/test-migration/target
cat /tmp/test-migration/target/subdir/sample.json
```

---

## Best Practices Summary

1. ✅ **Always dry-run first**
2. ✅ **Validate after migration**
3. ✅ **Check cross-domain references**
4. ✅ **Document your changes**
5. ✅ **Test on samples first**
6. ✅ **Backup important data**
7. ✅ **Follow native domain principle**
8. ✅ **Use appropriate tool for task**
9. ✅ **Read tool output carefully**
10. ✅ **Report issues in TROUBLESHOOTING.md**

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Status**: Comprehensive - all tools documented

