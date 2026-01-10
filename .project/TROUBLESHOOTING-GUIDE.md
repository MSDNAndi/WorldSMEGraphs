# AKU Quality Troubleshooting Guide
## Common Issues and Solutions

**Quick diagnostics for AKU quality problems** | Version 1.0.0 | 2026-01-10

---

## 🔍 Quick Diagnosis

Run validation and check the CQS score:
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json --level comprehensive
```

---

## Common Problems by CQS Score Range

### CQS < 0.40 (Severe Issues)

**Most Likely Causes**:
1. Missing required fields
2. No sources or broken source format
3. Missing ontology links
4. No verification information

**Quick Fixes**:
```bash
# Run automated improvement
python /tmp/universal_improve.py path/to/aku.json

# Validate again
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json
```

---

### CQS 0.40-0.59 (Major Issues)

**Typical Problems**:
- Incomplete sources (missing year, ISBN, DOI)
- Generic content ("fundamental concept...")
- Empty or minimal glossary
- No examples

**Solution Checklist**:
- [ ] Add year field to all sources
- [ ] Add ISBN to textbook sources
- [ ] Add DOI to journal sources
- [ ] Create 4-8 term glossary
- [ ] Add at least 1 concrete example with context
- [ ] Update domain_path to full taxonomy

---

### CQS 0.60-0.69 (D Grade - Minimal)

**Minor Issues**:
- Could use more sources (have 2, need 4+)
- Could use more examples (have 1, need 3+)
- Missing historical context
- Basic explanations need expansion

**Upgrade Path to C (0.70+)**:
1. Add 2 more authoritative sources
2. Add 2-3 more examples
3. Expand technical_details section
4. Add historical context (optional but helpful)

---

### CQS 0.70-0.79 (C Grade - Good)

**Enhancement Opportunities**:
- Add mathematical formulations (STEM)
- Add policy implications (economics/social)
- Add pedagogical content
- Cross-link to other domains

**Upgrade Path to B (0.80+)**:
1. Add 2 more sources (reach 6 total)
2. Add mathematical formulation section
3. Add common_misconceptions
4. Add cross-domain links

---

## Problem-Specific Solutions

### Problem: "No sources in provenance"

**Cause**: Missing "sources" field or using old "citations" field

**Solution**:
```json
{
  "provenance": {
    "sources": [    // Must be "sources" not "citations"
      {
        "source": "Full citation here",
        "type": "textbook",
        "year": 2021,      // Required
        "isbn": "978-XXX", // For books
        "relevance": "Why this source is cited"
      }
    ]
  }
}
```

---

### Problem: "Missing prerequisite AKU: [ID]"

**Cause**: Referenced AKU doesn't exist yet

**Solutions**:

**Option 1** - Remove broken reference:
```json
{
  "relationships": {
    "prerequisites": []  // Remove non-existent IDs
  }
}
```

**Option 2** - Create the missing AKU:
```bash
# Use template to create prerequisite
cp .project/templates/economics-template.json \
   domain/path/to/missing-aku.json
# Fill it out
```

**Option 3** - Fix the ID if you know correct one:
```json
{
  "relationships": {
    "prerequisites": ["correct-id-here"]
  }
}
```

---

### Problem: "Invalid domain_path"

**Cause**: Using old taxonomy without top-level category

**Solution**: Add proper prefix

| Old (Wrong) | New (Correct) |
|-------------|---------------|
| economics/macro | social-sciences/economics/macroeconomics |
| mathematics/algebra | formal-sciences/mathematics/algebra |
| physics/mechanics | natural-sciences/physics/mechanics |
| medicine/cardiology | health-sciences/medicine/cardiology |
| electrical/circuits | engineering/electrical/circuits |

---

### Problem: "Content completeness score low"

**Cause**: Missing key content sections

**Required Sections Checklist**:
- [ ] title
- [ ] definition (50-200 words, not just 2-3 words)
- [ ] definitions_glossary (4-8 terms)
- [ ] key_points (3-7 items)
- [ ] examples (1-4 with description and context)
- [ ] statement (one-sentence summary)
- [ ] explanation.intuition
- [ ] explanation.key_insight
- [ ] explanation.technical_details

---

### Problem: "Ontology compliance score low"

**Cause**: Missing ontology links

**Required Fields**:

**Top level**:
```json
{
  "owl:sameAs": "http://dbpedia.org/resource/Concept_Name",
  "skos:exactMatch": "http://www.wikidata.org/entity/QXXXXX"
}
```

**In relationships**:
```json
{
  "relationships": {
    "skos:broader": [
      "http://dbpedia.org/resource/Broader_Category"
    ],
    "skos:related": [
      "http://dbpedia.org/resource/Related_Concept"
    ]
  }
}
```

**Finding the correct links**:
1. Search DBpedia: https://dbpedia.org/
2. Search Wikidata: https://www.wikidata.org/
3. Use concept name, replace spaces with underscores
4. Get the Q-number from Wikidata (e.g., Q188790 for Inflation)

---

### Problem: "Reference quality score low"

**Causes and Fixes**:

**Missing years**:
```json
// Bad
{"source": "Mankiw (2021)...", "type": "textbook"}

// Good
{"source": "Mankiw (2021)...", "type": "textbook", "year": 2021}
```

**Missing ISBN/DOI**:
```json
// Textbook - needs ISBN
{"source": "...", "type": "textbook", "year": 2021, "isbn": "978-XXXXX"}

// Journal - needs DOI
{"source": "...", "type": "journal", "year": 2023, "doi": "10.XXXX/XXX"}
```

**Wrong source type**:
```json
// Change "reference" to actual type
{"type": "reference"}  // Bad
{"type": "textbook"}   // Good
```

---

### Problem: "Factual accuracy score low"

**Causes**:
1. Low confidence score in metadata
2. No verification information
3. Sources don't support claims

**Solutions**:

**Increase confidence** (if justified):
```json
{
  "metadata": {
    "confidence": 0.95  // vs 0.85
  }
}
```

**Add verification**:
```json
{
  "provenance": {
    "verification_status": "verified",
    "last_verified": "2026-01-10T15:00:00.000Z",
    "verification_notes": "Verified against sources X, Y, Z"
  }
}
```

**Add multiple sources**:
- 2 sources → 0.60 accuracy
- 4 sources → 0.70 accuracy
- 6 sources → 0.80 accuracy

---

### Problem: "Third-party verification score low"

**Cause**: Requires comprehensive assessment level

**Solution**: This is expected for standard assessment. To improve:

1. Run comprehensive assessment:
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json --level comprehensive
```

2. Actually get expert review (real solution):
- Submit to domain expert
- Document their review
- Update metadata

---

### Problem: JSON Validation Errors

**Common JSON Mistakes**:

**Missing comma**:
```json
// Bad
{
  "field1": "value1"
  "field2": "value2"
}

// Good
{
  "field1": "value1",
  "field2": "value2"
}
```

**Trailing comma** (some validators reject):
```json
// Problematic
{
  "field": "value",
}

// Safe
{
  "field": "value"
}
```

**Unquoted keys**:
```json
// Bad
{title: "value"}

// Good
{"title": "value"}
```

**Check syntax**:
```bash
python -m json.tool path/to/aku.json
# If it prints formatted JSON, syntax is valid
# If it shows error, fix the line mentioned
```

---

## Validation Workflow

### Step 1: Basic Validation
```bash
# Check if JSON is valid
python -m json.tool domain/path/to/aku.json > /dev/null
echo $?  # Should print 0 if valid
```

### Step 2: Schema Validation
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  domain/path/to/aku.json --verbose
```

### Step 3: Quality Assessment
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  domain/path/to/aku.json --level comprehensive --verbose
```

### Step 4: Fix Issues
- Read error messages carefully
- Fix one issue at a time
- Re-validate after each fix

### Step 5: Iterate
- Repeat steps 3-4 until CQS ≥ 0.60
- Aim for 0.70+ if possible
- 0.80+ for important AKUs

---

## Getting Help

### Check Documentation
1. `.project/AKU-QUALITY-STANDARDS.md` - Complete standards
2. `.project/QUICK-REFERENCE-CARD.md` - One-page guide
3. `.project/templates/` - Working examples

### Review Examples
Look at high-quality AKUs:
- `domain/social-sciences/economics/macroeconomics/akus/macro-001-gdp.json` (CQS 0.65)
- `domain/formal-sciences/mathematics/category-theory/akus/ct-003-morphisms.json` (CQS 0.68)

### Common Patterns
- Copy structure from template
- Copy source format from high-quality AKUs
- Copy ontology links pattern from similar concepts

---

## Automated Fixes

For batch improvements:
```bash
# Fix a single AKU
python /tmp/universal_improve.py path/to/aku.json

# Fix all AKUs in a directory
for file in domain/path/akus/*.json; do
    python /tmp/universal_improve.py "$file"
done

# Then validate all
for file in domain/path/akus/*.json; do
    echo "Checking $file"
    python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
      "$file" | grep "GRADE"
done
```

---

## Prevention

### Using Templates
Always start with a template:
```bash
cp .project/templates/economics-template.json domain/path/to/new-aku.json
```

This prevents most common mistakes:
- ✅ Correct structure
- ✅ All required fields
- ✅ Proper source format
- ✅ Ontology links
- ✅ Verification structure

### Pre-Commit Checks
Before committing, always:
```bash
# 1. Validate syntax
python -m json.tool new-aku.json > /dev/null

# 2. Check quality
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  new-aku.json

# 3. Ensure CQS ≥ 0.60
# Only commit if validation passes
```

---

## Quick Reference

| Problem | Quick Fix Command |
|---------|-------------------|
| Invalid JSON | `python -m json.tool file.json` |
| Low quality | `python /tmp/universal_improve.py file.json` |
| Check score | `python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py file.json` |
| Validate structure | `python .project/agents/quality-assurance/tools/validate_aku_v2.py file.json` |

---

**Need more help?** See:
- AKU-QUALITY-STANDARDS.md (complete guide)
- QUICK-REFERENCE-CARD.md (one-page summary)
- templates/ (working examples)
