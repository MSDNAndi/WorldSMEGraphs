# Domain Hierarchy Maintenance - Best Practices Guide

> **Purpose**: Guidelines for maintaining the domain hierarchy over time, ensuring consistency, quality, and adherence to the native domain principle.

## Table of Contents
1. [Core Maintenance Principles](#core-maintenance-principles)
2. [Adding New Content](#adding-new-content)
3. [Updating Existing Content](#updating-existing-content)
4. [Quality Assurance](#quality-assurance)
5. [Documentation Standards](#documentation-standards)
6. [Periodic Reviews](#periodic-reviews)
7. [Common Mistakes to Avoid](#common-mistakes-to-avoid)

---

## Core Maintenance Principles

### Principle 1: Preserve Native Domain Placement

**Rule**: Once a concept is placed in its native domain, it stays there permanently (unless the original placement was incorrect).

**Why**: Native domain reflects where concept originated historically, which doesn't change.

**Example**:
- ✅ Category theory stays in mathematics (originated there in 1940s)
- ❌ Don't move to computer science because "CS uses it more"

### Principle 2: Single Source of Truth

**Rule**: Every concept has exactly ONE authoritative definition in its native domain.

**Why**: Prevents duplication, inconsistency, and maintenance burden.

**Implementation**:
```
Native Domain (ONE place):
  └─ Complete, authoritative definition

Application Domains (MANY places):
  └─ Links to native + application-specific usage
```

### Principle 3: Cross-Domain Links, Not Copies

**Rule**: Application domains link to native definitions, never copy them.

**Why**: Copying creates maintenance burden and risks inconsistency.

**Pattern**:
```json
// Application domain AKU
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:path/to/native/definition"
    }]
  }
}
```

### Principle 4: Consistent Taxonomy

**Rule**: Follow `global-hierarchy.yaml` strictly for domain organization.

**Why**: Maintains consistency with international standards (UNESCO, LOC, DDC).

**Check**: Before adding content, verify path exists in global hierarchy.

---

## Adding New Content

### Step 1: Determine Native Domain

**Questions to Ask**:
1. Where did this concept originate?
2. Which field claims it as foundational knowledge?
3. Who are the authoritative experts?

**Flowchart**:
```
Is it abstract/formal? → Formal Sciences
Is it about physical world? → Natural Sciences
Is it about humans/society? → Social Sciences
Is it about health/medicine? → Health Sciences
```

### Step 2: Check Global Hierarchy

```bash
# Verify domain path exists
grep -A 5 "your-domain" domain/_ontology/global-hierarchy.yaml
```

**If not found**: Propose addition in Issue #3 before proceeding.

### Step 3: Create AKU with Proper Fields

**Required Fields**:
```json
{
  "@context": "aku-v2",
  "@type": "definition|concept|theorem|formula",
  "@id": "wsmg:domain/subdomain/concept-name",
  
  "metadata": {
    "version": "2.0.0",
    "created": "2026-01-04T15:00:00.000Z",
    "modified": "2026-01-04T15:00:00.000Z",
    "contributors": ["agent-name"],
    "confidence": 0.95,
    "status": "validated"
  },
  
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra",
    "type": "definition",
    "difficulty": "intermediate",
    "importance": "foundational",
    "isNativeDomain": true,       // if native
    "isApplicationDomain": false   // if native
  },
  
  "content": {
    // Your content here
  }
}
```

### Step 4: Validate Before Committing

```bash
# Validate structure
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  path/to/new-aku.json

# If application domain, validate cross-refs
python domain/_ontology/tools/validate_cross_domain.py \
  path/to/new-aku.json
```

### Step 5: Document Addition

- Update domain README with new content count
- Add to concept index if exists
- Note in commit message: "Added [concept] to [native domain]"

---

## Updating Existing Content

### When to Update

**Update Required**:
- ✅ Correcting factual errors
- ✅ Adding missing information
- ✅ Improving clarity
- ✅ Fixing validation errors

**Update NOT Required** (avoid churn):
- ❌ Minor wording changes
- ❌ Formatting preferences
- ❌ Style-only changes

### Update Procedure

1. **Load Current AKU**:
   ```bash
   cat path/to/aku.json
   ```

2. **Make Changes**:
   - Edit content as needed
   - Update `modified` timestamp to current UTC
   - Increment `version` if major change
   - Add yourself to `contributors` if significant

3. **Validate Changes**:
   ```bash
   python .project/agents/quality-assurance/tools/validate_aku_v2.py \
     path/to/aku.json
   ```

4. **Document Changes**:
   - Commit message: "Updated [concept]: [brief description of changes]"
   - If major change, note in domain README changelog

### Fields to Always Update

When modifying an AKU, **always update**:
- `metadata.modified` → Current UTC timestamp
- `metadata.contributors` → Add yourself if significant
- `metadata.version` → Increment if major (1.0.0 → 2.0.0) or minor (1.0.0 → 1.1.0)

**Example**:
```json
{
  "metadata": {
    "version": "2.1.0",  // Was 2.0.0
    "modified": "2026-01-04T15:45:00.000Z",  // Updated
    "contributors": ["original-agent", "you"]  // Added yourself
  }
}
```

---

## Quality Assurance

### Regular Validation

**Frequency**: Before every commit that modifies AKUs

**Commands**:
```bash
# Validate modified AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory path/to/domain/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory path/to/domain/
```

### Quality Metrics

| Metric | Target | Action if Below |
|--------|--------|----------------|
| Validation Pass Rate | ≥95% | Fix critical errors |
| Cross-Ref Validity | 100% | Update broken links |
| Required Fields | 100% | Add missing fields |
| Timestamp Format | 100% | Fix to ISO 8601 |

### Quality Checklist

Before committing changes:
- [ ] All AKUs validate successfully
- [ ] Cross-domain references resolve
- [ ] Timestamps in ISO 8601 format
- [ ] Domain paths match global hierarchy
- [ ] Native/application flags correct
- [ ] Documentation updated
- [ ] Commit message descriptive

---

## Documentation Standards

### Domain READMEs

**Required Sections**:
```markdown
# Domain Name

## Overview
Brief description of domain

## Content Structure
Subdomain organization

## Current Content
- Total AKUs: X
- Subdomains: A, B, C
- Status: Active/Complete/Partial

## Navigation
How to find content

## Cross-Domain Relationships
Where this domain connects

## Contributing
Guidelines for additions

## Validation
How to validate content

## References
Standards, sources
```

### Keeping READMEs Current

**Update Triggers**:
- New AKUs added → Update content count
- Subdomain created → Update structure section
- Cross-domain links added → Update relationships
- Migration completed → Update status

**Frequency**: With every significant change (10+ AKUs)

### Migration Documentation

**Always Document**:
- What was migrated
- From where to where
- How many AKUs
- Success rate
- Any issues encountered
- Validation results

**Location**: `MIGRATION-SUMMARY.md` (append new migrations)

---

## Periodic Reviews

### Monthly Review

**Checklist**:
- [ ] Run validation on all domains
- [ ] Check for broken cross-domain references
- [ ] Review any validation warnings
- [ ] Update domain statistics
- [ ] Check README currency
- [ ] Verify global hierarchy alignment

**Command**:
```bash
# Validate all domains
for DOMAIN in formal-sciences natural-sciences social-sciences health-sciences; do
  echo "Validating $DOMAIN..."
  python .project/agents/quality-assurance/tools/validate_aku_v2.py \
    --directory domain/$DOMAIN/
done
```

### Quarterly Review

**In-Depth Analysis**:
1. **Content Audit**:
   - Count AKUs per domain
   - Identify gaps
   - Plan additions

2. **Quality Check**:
   - Sample AKUs for manual review
   - Check consistency across domains
   - Verify native domain placements

3. **Documentation Review**:
   - Update outdated READMEs
   - Refresh statistics
   - Add new examples

4. **Tool Maintenance**:
   - Test migration scripts
   - Update validation rules if needed
   - Improve error messages

### Annual Review

**Strategic Assessment**:
1. **Taxonomy Review**:
   - Is global hierarchy still appropriate?
   - New domains needed?
   - Restructuring required?

2. **Standards Alignment**:
   - Check UNESCO/LOC/DDC updates
   - Align with latest standards
   - Document any changes

3. **Process Improvement**:
   - Review migration success rates
   - Identify pain points
   - Update procedures

---

## Common Mistakes to Avoid

### Mistake 1: Placement by Usage

**❌ Wrong**:
```
"We use monads extensively in our FP course, 
 so let's put them in computer-science/"
```

**✅ Correct**:
```
"Monads originated in mathematics (category theory),
 so they belong in formal-sciences/mathematics/.
 We'll add cross-references from our FP AKUs."
```

**Rule**: Origin determines placement, not usage frequency.

### Mistake 2: Duplicating Definitions

**❌ Wrong**:
```json
// Math domain
{
  "content": {
    "definition": "A monad is..."
  }
}

// CS domain  
{
  "content": {
    "definition": "A monad is..."  // Copied!
  }
}
```

**✅ Correct**:
```json
// Math domain (native)
{
  "content": {
    "definition": "A monad is..."
  },
  "classification": {
    "isNativeDomain": true
  }
}

// CS domain (application)
{
  "content": {
    "usage": "In FP, monads structure..."
  },
  "classification": {
    "isApplicationDomain": true
  },
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/.../monad"
    }]
  }
}
```

### Mistake 3: Forgetting to Update Timestamps

**❌ Wrong**:
```json
{
  "metadata": {
    "modified": "2025-01-01T10:00:00.000Z"  // Old!
  },
  "content": {
    "definition": "Updated definition..."  // But modified not updated
  }
}
```

**✅ Correct**:
```json
{
  "metadata": {
    "modified": "2026-01-04T15:45:00.000Z"  // Current UTC
  },
  "content": {
    "definition": "Updated definition..."
  }
}
```

### Mistake 4: Breaking Cross-Domain References

**❌ Wrong**:
```
1. Move native domain AKU to new location
2. Forget to update cross_domain_references in application domains
3. Result: Broken links!
```

**✅ Correct**:
```
1. Move native domain AKU
2. Update all cross_domain_references in application domains
3. Validate with validate_cross_domain.py
4. Verify all links resolve
```

### Mistake 5: Ignoring Validation Errors

**❌ Wrong**:
```
Validator shows errors → "I'll fix them later" → Commit anyway
```

**✅ Correct**:
```
Validator shows errors → Fix immediately → Validate again → Then commit
```

**Rule**: Never commit with validation errors (warnings OK if documented).

### Mistake 6: Missing Native Domain Flags

**❌ Wrong**:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra"
    // Missing isNativeDomain flag!
  }
}
```

**✅ Correct**:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra",
    "isNativeDomain": true,
    "isApplicationDomain": false
  }
}
```

### Mistake 7: Relative Paths in @id

**❌ Wrong**:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "../../../mathematics/monad"  // Fragile!
    }]
  }
}
```

**✅ Correct**:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad"
    }]
  }
}
```

---

## Emergency Procedures

### If Native Domain Placement Was Wrong

**Scenario**: Concept was placed in wrong native domain.

**Procedure**:
1. **Confirm Error**:
   - Research concept's origin
   - Consult domain experts
   - Check authoritative sources

2. **Plan Migration**:
   - Identify correct native domain
   - List all affected AKUs
   - Identify application domains with references

3. **Execute Migration**:
   ```bash
   python domain/_ontology/tools/migrate_domain.py \
     --source "wrong/domain" \
     --target "correct/domain"
   ```

4. **Update References**:
   - Fix all cross_domain_references
   - Update documentation
   - Validate thoroughly

5. **Document Correction**:
   - Note in MIGRATION-SUMMARY.md
   - Explain reasoning
   - Add to lessons learned

### If Cross-Domain References Break

**Symptoms**: Validation fails, links don't resolve

**Fix**:
1. **Identify Broken Links**:
   ```bash
   python domain/_ontology/tools/validate_cross_domain.py --directory path/
   ```

2. **Find Current Location**:
   ```bash
   find domain/ -name "*concept-name*.json"
   ```

3. **Update References**:
   - Edit AKUs with broken references
   - Update `@id` fields to correct paths
   - Update `modified` timestamp

4. **Validate**:
   ```bash
   python domain/_ontology/tools/validate_cross_domain.py --directory path/
   ```

---

## Best Practices Summary

### DO ✅

1. **Place by Origin**, not usage
2. **Link**, don't duplicate
3. **Validate** before committing
4. **Update timestamps** when modifying
5. **Document** all migrations
6. **Follow** global hierarchy
7. **Use proper @id format** (wsmg: prefix)
8. **Keep** READMEs current
9. **Run** periodic reviews
10. **Test** before deploying

### DON'T ❌

1. **Don't** place by usage frequency
2. **Don't** copy native definitions
3. **Don't** commit with validation errors
4. **Don't** forget timestamps
5. **Don't** use relative paths in @id
6. **Don't** break cross-domain references
7. **Don't** skip validation
8. **Don't** ignore warnings without reason
9. **Don't** forget native domain flags
10. **Don't** make changes without documenting

---

## Tools for Maintenance

### Regular Use

| Tool | When to Use | Frequency |
|------|------------|-----------|
| `validate_aku_v2.py` | After any AKU changes | Every commit |
| `validate_cross_domain.py` | After migrations or updates | Weekly |
| `migrate_domain.py` | When reorganizing | As needed |

### Automation Opportunities

**Pre-commit Hook** (optional):
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Validate all modified AKUs
for FILE in $(git diff --cached --name-only | grep '\.json$'); do
  python .project/agents/quality-assurance/tools/validate_aku_v2.py "$FILE"
  if [ $? -ne 0 ]; then
    echo "Validation failed for $FILE"
    exit 1
  fi
done
```

**CI/CD Integration**:
```yaml
# .github/workflows/validate.yml
name: Validate AKUs
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate AKUs
        run: |
          python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/
```

---

## Success Metrics

### Key Performance Indicators

| Metric | Target | Current |
|--------|--------|---------|
| Validation Pass Rate | ≥95% | 99.5% ✅ |
| Cross-Ref Validity | 100% | 100% ✅ |
| Native Domain Compliance | 100% | 100% ✅ |
| Documentation Currency | ≥90% | 100% ✅ |
| Monthly Review Completion | 100% | N/A (new) |

### Quality Goals

- **Zero** validation errors in commits
- **<1%** broken cross-domain references
- **100%** native domain placements correct
- **<7 days** from change to documentation update
- **Monthly** validation sweep completed

---

## Getting Help

### Resources

- **Documentation**: See INDEX.md for all guides
- **FAQ**: Check FAQ.md for common questions
- **Troubleshooting**: TROUBLESHOOTING.md for issues
- **Examples**: Review successful migrations

### Support

- **Issues**: GitHub Issues for problems
- **Questions**: Issue #3 for migration questions
- **Improvements**: Pull requests welcome

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintained By**: Development Team  
**Review Frequency**: Quarterly

