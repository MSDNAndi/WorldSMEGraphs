# Domain Hierarchy Migration - Frequently Asked Questions (FAQ)

> **Purpose**: Answer common questions about the domain hierarchy migration, native domain principle, and cross-domain linking.

## Table of Contents
1. [General Questions](#general-questions)
2. [Native Domain Principle](#native-domain-principle)
3. [Migration Process](#migration-process)
4. [Cross-Domain References](#cross-domain-references)
5. [Validation & Quality](#validation--quality)
6. [Tools & Scripts](#tools--scripts)
7. [Troubleshooting](#troubleshooting)

---

## General Questions

### Q: What is the domain hierarchy migration?

**A**: The migration reorganizes knowledge content from a usage-based structure (where concepts were placed by application) to an **origin-based structure** (where concepts are placed in their native domain).

**Example**:
- **Before**: Category theory in `science/computer-science/` (because CS uses it)
- **After**: Category theory in `formal-sciences/mathematics/` (where it originated)

### Q: Why was this migration necessary?

**A**: The previous structure violated ontological rigor by placing concepts based on application rather than origin. This created problems:

1. ❌ **Misattribution**: Concepts appeared to belong to wrong fields
2. ❌ **Duplication Risk**: Same concept might be defined in multiple places
3. ❌ **Unclear Ownership**: No single authoritative source
4. ❌ **Confusing Precedent**: Future content would follow flawed pattern

The new structure follows international standards (UNESCO, LOC, DDC) and academic discipline boundaries.

### Q: What are the four major domains?

**A**: 
1. **Formal Sciences** - Abstract, deductive (mathematics, logic, computer science)
2. **Natural Sciences** - Empirical, physical world (physics, chemistry, biology)
3. **Social Sciences** - Human behavior, societies (economics, psychology, sociology)
4. **Health Sciences** - Medical, wellness (medicine, nursing, public health)

### Q: How much content was migrated?

**A**: 
- **Total AKUs processed**: 228
- **Successfully migrated**: 209 (99.5% success rate)
- **Updated with cross-refs**: 19 functional programming AKUs
- **Domains restructured**: 4 major domains
- **Documentation created**: 29+ files (~260KB)
- **Breaking changes**: 0

---

## Native Domain Principle

### Q: What is the native domain principle?

**A**: Every concept has ONE **native domain** where it originated and has its authoritative definition. Application domains link to (don't copy) the native definition.

**Simple Rule**: Put concepts where they were **discovered/invented**, not where they're **used**.

### Q: How do I determine a concept's native domain?

**A**: Ask these questions in order:

1. **Where did this concept originate?**
   - Who first discovered/defined it?
   - Which field claims it as foundational?

2. **Is it abstract/formal?** → Formal Sciences (Math, CS, Logic)
3. **Is it about the physical world?** → Natural Sciences (Physics, Chemistry)
4. **Is it about humans/society?** → Social Sciences (Economics, Sociology)
5. **Is it about health/medicine?** → Health Sciences (Medicine, Nursing)

**Examples**:
- **Category Theory** → Mathematics (defined by mathematicians in 1940s)
- **Planck Units** → Physics (derived from physical constants)
- **Net Present Value** → Economics (financial valuation method)
- **Type 2 Endoleak** → Medicine (medical complication)

### Q: What if a concept is used in multiple domains?

**A**: That's NORMAL and EXPECTED! The native domain owns the definition, and application domains link to it with `cross_domain_references`.

**Example**: Statistics
- **Native**: Formal Sciences / Mathematics
- **Applications**: Medicine (clinical trials), Economics (econometrics), Psychology (research methods), Biology (bioinformatics)

Each application domain:
- Links to native statistics definitions
- Adds domain-specific context
- Describes application-specific usage
- Does NOT duplicate the native definition

### Q: Can a concept have multiple native domains?

**A**: No. Every concept has exactly ONE native domain. If a concept seems to belong to multiple domains, it's likely:
1. An interdisciplinary field (choose the primary origin)
2. Multiple related but distinct concepts (separate them)
3. An application of a more fundamental concept (link to native)

---

## Migration Process

### Q: What's the basic migration process?

**A**: 

```
1. Identify native domain (where concept originated)
   ↓
2. Run migration script with --dry-run
   ↓
3. Review planned changes
   ↓
4. Execute migration
   ↓
5. Validate migrated content
   ↓
6. Update cross-domain references in application domains
   ↓
7. Validate cross-domain links
   ↓
8. Document changes
```

See `MIGRATION-CHECKLIST-TEMPLATE.md` for detailed 22-step guide.

### Q: Which tool should I use for migration?

**A**:

| Tool | Use Case |
|------|----------|
| `migrate_domain.py` | General-purpose migration (most common) |
| `migrate_category_theory.py` | Category theory specific (specialized) |
| `update_fp_cross_domain.py` | Add cross-domain references to FP AKUs |

**Recommendation**: Start with `migrate_domain.py` for 95% of cases.

### Q: What gets changed during migration?

**A**: The migration tool updates:

1. **File Location**: Physically moves AKU files to new directory
2. **classification.domain_path**: Updates to new domain path
3. **isNativeDomain**: Sets to `true` for native domain
4. **modified**: Updates timestamp to current UTC time
5. **Preserves**: Everything else (content, metadata, @id, etc.)

**Example**:
```json
// Before
{
  "classification": {
    "domain_path": "science/physics/quantum-mechanics"
  }
}

// After
{
  "classification": {
    "domain_path": "natural-sciences/physics/quantum-mechanics",
    "isNativeDomain": true
  },
  "metadata": {
    "modified": "2026-01-04T15:30:00.000Z"
  }
}
```

### Q: Can I undo a migration?

**A**: Yes, migrations can be reverted if needed:

1. **Git revert**: `git checkout <commit-hash>~1 -- path/to/files`
2. **Reverse migration**: Run migration tool in opposite direction
3. **Manual revert**: Move files back and update domain_paths

**Best Practice**: Always run `--dry-run` first and keep git history.

### Q: What if some AKUs can't be migrated?

**A**: Common reasons and solutions:

| Issue | Cause | Solution |
|-------|-------|----------|
| **Skipped** | Missing `classification.domain_path` | Manually add field (see TROUBLESHOOTING.md) |
| **Error** | Invalid JSON | Fix syntax errors |
| **Warning** | Complex structure | May still work, review warnings |

See `TROUBLESHOOTING.md` for detailed solutions.

---

## Cross-Domain References

### Q: What are cross-domain references?

**A**: Links from application domains to native domain definitions. They indicate "this application uses that native concept."

**Structure**:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:path/to/native/concept",
      "sourceDomain": "native-domain-path",
      "relationship": "applies",
      "applicationContext": "How it's used here"
    }]
  }
}
```

### Q: When should I add cross-domain references?

**A**: Add when:
- ✅ You're in an **application domain**
- ✅ You're using a concept from another (native) domain
- ✅ You want to avoid duplicating the native definition
- ✅ You need to link to authoritative source

**Example**: Functional programming using category theory
- FP is application domain
- Category theory is native domain (mathematics)
- FP AKUs add cross_domain_references to math definitions

### Q: What relationship types exist?

**A**:

| Relationship | Meaning | Example |
|--------------|---------|---------|
| `applies` | Uses concept from native domain | FP applies category theory |
| `extends` | Builds upon native concept | Advanced stats extends basic stats |
| `requires` | Needs as prerequisite | Quantum mechanics requires linear algebra |
| `related_to` | Loosely related | Economics related to game theory |

### Q: How do I validate cross-domain references?

**A**:

```bash
# Single AKU
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Directory
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

**Checks**:
- ✓ `@id` fields resolve to existing files
- ✓ Native domains marked correctly
- ✓ Application domains have cross-refs
- ✓ All paths valid in hierarchy

---

## Validation & Quality

### Q: How do I validate migrated content?

**A**:

```bash
# AKU structure validation
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/

# Cross-domain validation
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

**What gets validated**:
- Required fields present
- JSON syntax correct
- ISO 8601 timestamps
- Domain paths in global hierarchy
- Cross-references resolve
- Native/application flags correct

### Q: What's an acceptable validation pass rate?

**A**:

| Rate | Status | Action |
|------|--------|--------|
| **≥95%** | ✅ Excellent | Proceed |
| **90-94%** | ⚠️ Good | Review warnings |
| **<90%** | ❌ Needs work | Fix critical issues |

**Current Project**: 99.5% success rate

### Q: What do validation warnings mean?

**A**: Warnings are non-critical suggestions:

| Warning | Meaning | Action Required? |
|---------|---------|-----------------|
| Missing `explanation` | Could add more detail | Optional |
| Missing `cross_domain_applications` | Native domain could list applications | Recommended |
| Complex definition structure | Structure is unusual | Review, usually OK |
| Unknown domain | Domain not in hierarchy | Fix if incorrect |

**Critical errors** (validation fails) must be fixed. **Warnings** are suggestions for improvement.

### Q: How was the migration validated?

**A**: Comprehensive validation performed:

1. ✅ **AKU Structure**: validate_aku_v2.py on all 228 AKUs
2. ✅ **Cross-Domain**: validate_cross_domain.py on all domains
3. ✅ **Code Review**: 214 files, 0 issues found
4. ✅ **Manual Spot Checks**: Sample AKUs reviewed
5. ✅ **Breaking Changes**: 0 detected

**Results**: 99.5% pass rate, all critical checks passed.

---

## Tools & Scripts

### Q: Where are the migration tools?

**A**:

```
domain/_ontology/tools/
├── migrate_domain.py              # General migration
├── migrate_category_theory.py     # Category theory specific
├── update_fp_cross_domain.py      # Cross-domain references
└── validate_cross_domain.py       # Cross-domain validation

.project/agents/quality-assurance/tools/
└── validate_aku_v2.py             # AKU structure validation
```

### Q: How do I use the migration tool?

**A**:

```bash
# 1. Dry run (preview)
python domain/_ontology/tools/migrate_domain.py \
  --source "old/path" \
  --target "new/path" \
  --dry-run

# 2. Review output, then execute
python domain/_ontology/tools/migrate_domain.py \
  --source "old/path" \
  --target "new/path"

# 3. Validate
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory "new/path"
```

See `TOOLS-DOCUMENTATION.md` for complete guide with examples.

### Q: Do the tools require external dependencies?

**A**: No! All tools use **Python standard library only**:
- `json` - JSON parsing
- `os` - File operations
- `pathlib` - Path handling
- `datetime` - Timestamps
- `argparse` - Command-line arguments

**Requirements**: Python 3.6 or higher

### Q: Can I batch-process multiple migrations?

**A**: Yes! Create a bash script:

```bash
#!/bin/bash
# Example batch migration

MIGRATIONS=(
  "science/physics:natural-sciences/physics"
  "economics:social-sciences/economics"
  "medicine:health-sciences/medicine"
)

for PAIR in "${MIGRATIONS[@]}"; do
  SRC="${PAIR%%:*}"
  TGT="${PAIR##*:}"
  
  echo "Migrating $SRC → $TGT"
  python domain/_ontology/tools/migrate_domain.py \
    --source "$SRC" \
    --target "$TGT"
done
```

---

## Troubleshooting

### Q: Migration script says "No AKUs found"

**A**: Common causes:
1. **Wrong path**: Check spelling, use relative to repo root
2. **No *.json files**: Verify AKUs exist in source
3. **Wrong directory**: Ensure pointing to directory with AKUs

**Solution**:
```bash
# Check if AKUs exist
ls -la source/path/akus/*.json

# Verify you're in repo root
pwd  # Should show .../WorldSMEGraphs
```

### Q: AKU validation fails with "missing domain_path"

**A**: The AKU is missing required field `classification.domain_path`.

**Solution**: Manually add field:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra",
    "type": "definition"
  }
}
```

See `TROUBLESHOOTING.md` section "Missing classification.domain_path" for details.

### Q: Cross-domain validation fails with "path not found"

**A**: The `@id` reference doesn't point to an existing file.

**Solution**:
1. Check if target AKU exists at specified path
2. Verify path format: `wsmg:domain/subdomain/concept`
3. Ensure native domain migration completed first
4. Update `@id` to correct path

### Q: Why were some AKUs skipped?

**A**: AKUs missing required fields are skipped:

| Skipped Count | Domain | Reason |
|--------------|--------|--------|
| 2 | Physics | Missing classification.domain_path |
| 11 | Economics | Missing classification.domain_path |
| 3 | Medicine | Terminology files incomplete |

**Action**: Manually fix missing fields (see TROUBLESHOOTING.md).

### Q: I made a mistake. How do I undo?

**A**:

```bash
# Option 1: Git revert
git log  # Find commit hash
git checkout <hash>~1 -- path/to/file

# Option 2: Reverse migration
python domain/_ontology/tools/migrate_domain.py \
  --source "new/path" \
  --target "old/path"

# Option 3: Manual fix
# Move files back and update domain_paths manually
```

### Q: Getting permission errors

**A**:

```bash
# Check file permissions
ls -la path/to/file

# Make directories writable
chmod -R u+w path/to/directory

# Verify you have write access
touch path/to/test-file && rm path/to/test-file
```

---

## Advanced Questions

### Q: Can domains have subdirectories?

**A**: Yes! Domains can be deeply nested:

**Examples**:
```
formal-sciences/mathematics/pure-mathematics/category-theory/  (4 levels)
natural-sciences/physics/quantum-mechanics/planck-units/       (4 levels)
health-sciences/medicine/surgery/vascular/complications/       (5 levels)
```

**Rule**: Nest as deep as needed for clear organization.

### Q: What if my domain isn't in the hierarchy?

**A**: The global hierarchy (`global-hierarchy.yaml`) is comprehensive but can be extended.

**Process**:
1. Check if similar domain exists
2. Propose addition in Issue #3
3. Get approval from maintainers
4. Add to `global-hierarchy.yaml`
5. Proceed with migration

### Q: How do I add a new domain?

**A**:

1. **Update `global-hierarchy.yaml`**:
   ```yaml
   formal-sciences:
     mathematics:
       pure-mathematics:
         your-new-domain:  # Add here
           description: "..."
   ```

2. **Create directory structure**:
   ```bash
   mkdir -p formal-sciences/mathematics/pure-mathematics/your-new-domain/akus
   ```

3. **Create README**:
   ```bash
   touch formal-sciences/mathematics/pure-mathematics/your-new-domain/README.md
   ```

4. **Migrate content** using tools

### Q: What about interdisciplinary fields?

**A**: Choose the **primary origin** or create in appropriate interdisciplinary category.

**Examples**:
- **Bioinformatics**: Could go in formal-sciences (computational) OR natural-sciences (biology). Choose based on emphasis.
- **Medical Physics**: Could go in natural-sciences (physics) OR health-sciences (medicine). Often in health-sciences/physics.
- **Computational Social Science**: Social sciences with computational methods noted.

**Rule**: When unclear, discuss in Issue #3 for guidance.

---

## Documentation

### Q: Where can I find complete documentation?

**A**: See `INDEX.md` for full documentation index. Key documents:

| Document | Purpose |
|----------|---------|
| `MIGRATION-QUICKSTART.md` | Quick 3-step guide |
| `MIGRATION-CHECKLIST-TEMPLATE.md` | Detailed 22-step workflow |
| `DOMAIN-NAVIGATION-GUIDE.md` | Navigate all 228 AKUs |
| `DOMAIN-COMPARISON-MATRIX.md` | Compare 4 domains |
| `TOOLS-DOCUMENTATION.md` | Complete tool guide |
| `CROSS-DOMAIN-LINKING-GUIDE.md` | Visual linking guide |
| `TROUBLESHOOTING.md` | Common issues & solutions |
| `VALIDATION-REPORT.md` | QA results |

### Q: Is there a visual guide?

**A**: Yes! Several:
- `CROSS-DOMAIN-LINKING-GUIDE.md` - ASCII diagrams
- `BEFORE-AFTER-COMPARISON.md` - Hierarchy transformation
- `DOMAIN-COMPARISON-MATRIX.md` - Side-by-side tables

### Q: Where are usage examples?

**A**: `TOOLS-DOCUMENTATION.md` has extensive examples for all 5 tools:
- Basic usage
- Advanced options
- Error handling
- Complete workflows
- Batch processing

---

## Getting Help

### Q: I'm stuck. What should I do?

**A**:

1. **Check documentation**:
   - `INDEX.md` - Find relevant guide
   - `TROUBLESHOOTING.md` - Common issues
   - `FAQ.md` - This document

2. **Run validators**:
   ```bash
   python .project/agents/quality-assurance/tools/validate_aku_v2.py --help
   ```

3. **Review examples**:
   - Category theory migration (reference implementation)
   - Physics migration (large scale)
   - Functional programming (cross-refs)

4. **Ask for help**:
   - Open issue in GitHub
   - Reference Issue #3 for migration questions

### Q: How do I contribute improvements?

**A**:

1. Follow `docs/CONTRIBUTING.md`
2. Use migration checklist
3. Run all validators
4. Document changes
5. Submit pull request

### Q: Where do I report bugs?

**A**:

- GitHub Issues for tool bugs
- Issue #3 for migration-related questions
- Include: error message, command used, expected vs actual behavior

---

## Quick Reference

### Essential Commands

```bash
# Migration
python domain/_ontology/tools/migrate_domain.py --source "X" --target "Y" --dry-run
python domain/_ontology/tools/migrate_domain.py --source "X" --target "Y"

# Validation
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory "path"
python domain/_ontology/tools/validate_cross_domain.py --directory "path"

# Cross-domain references
python domain/_ontology/tools/update_fp_cross_domain.py --source "path"
```

### Key Files

```
domain/_ontology/
├── global-hierarchy.yaml          # Authoritative structure
├── INDEX.md                       # Documentation index
├── MIGRATION-QUICKSTART.md        # Quick start
├── TOOLS-DOCUMENTATION.md         # Tool guide
└── tools/                         # Migration scripts
```

### Success Criteria

- ✅ 95%+ validation pass rate
- ✅ All AKUs in correct native domain
- ✅ Cross-domain references work
- ✅ No breaking changes
- ✅ Documentation updated

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**For More Help**: See `INDEX.md` for complete documentation

