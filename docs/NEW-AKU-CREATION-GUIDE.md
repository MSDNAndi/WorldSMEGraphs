# Creating New AKUs with Ontology Annotations

**Version**: 1.0  
**Date**: 2025-12-27  
**Status**: Production Ready  
**Purpose**: Instructions for creating new AKUs with proper ontology annotations from the start

---

## Quick Start

**IMPORTANT**: All new AKUs MUST include ontology annotations from creation. Do not create AKUs without proper ontology research.

### Step-by-Step Process

1. **Choose the appropriate template** for your domain
2. **Research ontology codes** before writing content
3. **Fill in the template** with researched codes
4. **Validate** before committing
5. **Timestamp** is automatically set during creation

---

## Available Templates

### Medical Domain
**Template**: `docs/templates/medical-aku-ontology-template.json`

**Use for**: Medical conditions, procedures, tests, devices, clinical concepts

**Required Ontologies**:
- SNOMED CT (primary)
- MeSH (secondary)
- ICD-11 (for diseases)
- UMLS (optional)

### Economics/Finance Domain
**Template**: `docs/templates/economics-aku-ontology-template.json`

**Use for**: Financial concepts, economic theories, business concepts

**Required Ontologies**:
- FIBO (primary)
- DBpedia (secondary)
- Wikidata (multilingual)

### Science Domain
**Template**: `docs/templates/science-aku-ontology-template.json`

**Use for**: Physics, chemistry, biology, mathematics concepts

**Required Ontologies**:
- QUDT (for units/quantities)
- ChEBI (for chemicals)
- Gene Ontology (for biology)

---

## Detailed Instructions

### Phase 1: Research BEFORE Creation

#### Step 1.1: Identify Your Concept
Before creating the AKU, clearly define:
- Primary concept name
- Domain and subdomain
- Related concepts

#### Step 1.2: Research Ontology Codes

**Medical Domain**:
```bash
# Use SNOMED CT Browser: https://browser.ihtsdotools.org/
# Search for your concept
# Note the code (e.g., 449567000 for "Type II endoleak")
# Verify it's active, not retired
# Find broader/narrower concepts in hierarchy

# Cross-reference with MeSH: https://meshb.nlm.nih.gov/
# Note descriptor (e.g., D000078862 for "Endoleak")

# Check ICD-11: https://icd.who.int/browse11
# Note entity code if applicable
```

**Economics/Finance Domain**:
```bash
# Use FIBO Navigator: https://spec.edmcouncil.org/fibo/
# Navigate hierarchy to find your concept
# Note full URI (e.g., .../FBC/DebtAndEquities/Debt/NetPresentValue)

# Cross-reference with DBpedia: https://dbpedia.org/
# Search and note resource URL

# Find Wikidata entity: https://www.wikidata.org/
# Note Q-number (e.g., Q1054308 for "net present value")
```

**Science Domain**:
```bash
# Use appropriate ontology browser for subdomain
# QUDT: http://www.qudt.org/
# ChEBI: https://www.ebi.ac.uk/chebi/
# Gene Ontology: http://geneontology.org/
```

#### Step 1.3: Document Your Research

Create a quick reference note:
```
Concept: Net Present Value
FIBO: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue
DBpedia: http://dbpedia.org/resource/Net_present_value
Wikidata: Q1054308
Match types: All exactMatch
```

### Phase 2: Create AKU from Template

#### Step 2.1: Copy Template

```bash
# For medical
cp docs/templates/medical-aku-ontology-template.json \
   domain/medicine/YOUR/PATH/akus/CATEGORY/aku-NNN-concept-name.json

# For economics
cp docs/templates/economics-aku-ontology-template.json \
   domain/economics/YOUR/PATH/akus/CATEGORY/aku-NNN-concept-name.json

# For science
cp docs/templates/science-aku-ontology-template.json \
   domain/science/YOUR/PATH/akus/CATEGORY/aku-NNN-concept-name.json
```

#### Step 2.2: Fill in Metadata

**CRITICAL**: Set proper timestamps using ISO 8601 format with UTC timezone:

```json
"metadata": {
  "version": "1.0.0",
  "created": "2025-12-27T22:32:00.000Z",
  "last_updated": "2025-12-27T22:32:00.000Z",
  "contributors": [
    "your-name-or-agent-name",
    "terminology-agent"
  ],
  "confidence": 0.95,
  "status": "ontology-enhanced"
}
```

**Timestamp Format**:
- Format: `YYYY-MM-DDTHH:MM:SS.000Z`
- Always use UTC (Z suffix)
- Include milliseconds (.000)
- Use 24-hour time

**How to get current timestamp**:
```bash
# Command line
date -u +"%Y-%m-%dT%H:%M:%S.000Z"

# Python
from datetime import datetime
datetime.utcnow().isoformat() + "Z"
```

#### Step 2.3: Add SKOS Properties

```json
"skos:prefLabel": "Your Concept Name",
"skos:notation": "aku-001-concept-name",
"skos:definition": "Clear, concise definition of the concept",
"skos:altLabel": ["Alternative Name 1", "Abbreviation", "Foreign Name"]
```

#### Step 2.4: Add External Ontology Links

**Medical Example**:
```json
"owl:sameAs": "http://snomed.info/id/449567000",
"skos:exactMatch": [
  "http://snomed.info/id/449567000"
],
"skos:broadMatch": [
  "http://id.nlm.nih.gov/mesh/D000078862"
],
"skos:closeMatch": [
  "http://id.who.int/icd/entity/1573326799"
],

"medicalCode": [
  {
    "@type": "MedicalCode",
    "codingSystem": "SNOMED-CT",
    "codeValue": "449567000",
    "uri": "http://snomed.info/id/449567000",
    "description": "Type II endoleak (disorder)",
    "preferred": true
  },
  {
    "@type": "MedicalCode",
    "codingSystem": "MeSH",
    "codeValue": "D000078862",
    "uri": "http://id.nlm.nih.gov/mesh/D000078862",
    "description": "Endoleak"
  }
]
```

**Economics Example**:
```json
"owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
"skos:exactMatch": [
  "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
  "http://dbpedia.org/resource/Net_present_value",
  "http://www.wikidata.org/entity/Q1054308"
]
```

#### Step 2.5: Add SKOS Relationships

```json
"relationships": {
  "skos:broader": [
    {
      "@id": "wsmg:parent-concept",
      "@type": "skos:Concept",
      "label": "Parent Concept Name"
    }
  ],
  "skos:narrower": [
    {
      "@id": "wsmg:child-concept",
      "@type": "skos:Concept",
      "label": "Child Concept Name"
    }
  ],
  "skos:related": [
    {
      "@id": "wsmg:related-concept",
      "@type": "skos:Concept",
      "label": "Related Concept Name"
    }
  ]
}
```

#### Step 2.6: Add Provenance

```json
"provenance": {
  "dc:creator": ["your-name", "terminology-agent"],
  "dc:created": "2025-12-27T22:32:00.000Z",
  "dc:modified": "2025-12-27T22:32:00.000Z",
  "prov:wasDerivedFrom": [
    {
      "@type": "ScholarlyArticle",
      "dc:title": "Source Title",
      "dc:bibliographicCitation": "Full citation",
      "dc:source": "https://doi.org/..."
    }
  ],
  "prov:wasGeneratedBy": {
    "@type": "Activity",
    "label": "Ontology-enhanced AKU creation",
    "prov:startedAtTime": "2025-12-27T22:30:00.000Z",
    "prov:endedAtTime": "2025-12-27T22:32:00.000Z"
  }
}
```

### Phase 3: Validation

#### Step 3.1: JSON Structure Validation

```bash
python -m json.tool your-aku.json > /dev/null
# Should show no errors
```

#### Step 3.2: Ontology Compliance Validation

```bash
python .project/agents/quality-assurance/tools/validate_ontology.py your-aku.json
# Should show 100% pass
```

#### Step 3.3: Manual Checklist

- [ ] Timestamp in ISO 8601 format with UTC (Z suffix)
- [ ] `created` and `last_updated` fields present
- [ ] SKOS properties (prefLabel, definition, notation) present
- [ ] External ontology links researched and verified
- [ ] Match types appropriate (exactMatch/closeMatch/broadMatch)
- [ ] SKOS relationships use proper format with @id and @type
- [ ] Provenance includes creator and timestamps
- [ ] All external URIs tested and valid

---

## Timestamp Management

### Why Timestamps Matter

1. **Change Detection**: Identify when AKUs were last modified
2. **Versioning**: Track evolution of knowledge
3. **Audit Trail**: Maintain provenance
4. **Synchronization**: Coordinate distributed updates

### Timestamp Fields

Every AKU MUST have:

```json
"metadata": {
  "created": "2025-12-27T22:32:00.000Z",
  "last_updated": "2025-12-27T22:32:00.000Z"
}
```

Additional provenance timestamps:

```json
"provenance": {
  "dc:created": "2025-12-27T22:32:00.000Z",
  "dc:modified": "2025-12-27T22:32:00.000Z"
}
```

### Updating Timestamps

When modifying an existing AKU:

1. **DO NOT change** `metadata.created` - preserve original
2. **DO update** `metadata.last_updated` to current UTC time
3. **DO update** `provenance.dc:modified` to current UTC time
4. **DO add** to `metadata.contributors` if you're a new contributor

Example:
```json
"metadata": {
  "created": "2025-12-27T10:00:00.000Z",  // KEEP ORIGINAL
  "last_updated": "2025-12-27T22:32:00.000Z",  // UPDATE TO NOW
  "contributors": [
    "original-creator",
    "your-name"  // ADD YOURSELF
  ]
}
```

### Automated Timestamp Detection

Query for recently updated AKUs:

```bash
# Find AKUs updated in last 24 hours
find domain -name "*.json" -type f -exec grep -l "2025-12-27" {} \;

# Find AKUs by last_updated timestamp
grep -r "last_updated.*2025-12-27" domain/ --include="*.json"
```

---

## Common Patterns

### Pattern 1: Definition AKU

```json
{
  "@context": [...],
  "@type": "EducationalResource",
  "@id": "wsmg:concept-name",
  "skos:prefLabel": "Concept Name",
  "skos:definition": "Clear definition",
  "owl:sameAs": "http://ontology.org/...",
  "skos:exactMatch": ["http://ontology.org/..."],
  "metadata": {
    "created": "2025-12-27T22:32:00.000Z",
    "last_updated": "2025-12-27T22:32:00.000Z"
  }
}
```

### Pattern 2: Formula AKU

```json
{
  "@context": [...],
  "@type": "EducationalResource",
  "@id": "wsmg:formula-name",
  "skos:prefLabel": "Formula Name",
  "content": {
    "statement": "Formula description",
    "mathematical_representations": {...}
  },
  "skos:broader": [...],
  "metadata": {
    "created": "2025-12-27T22:32:00.000Z",
    "last_updated": "2025-12-27T22:32:00.000Z"
  }
}
```

### Pattern 3: Procedure AKU

```json
{
  "@context": [...],
  "@type": ["EducationalResource", "MedicalProcedure"],
  "@id": "wsmg:procedure-name",
  "skos:prefLabel": "Procedure Name",
  "medicalCode": [...],
  "relationships": {...},
  "metadata": {
    "created": "2025-12-27T22:32:00.000Z",
    "last_updated": "2025-12-27T22:32:00.000Z"
  }
}
```

---

## Quality Standards

### Minimum Requirements

Every new AKU MUST have:

1. ✅ Proper @context with base and domain contexts
2. ✅ SKOS properties (prefLabel, definition, notation)
3. ✅ At least one external ontology link
4. ✅ Appropriate match type classification
5. ✅ ISO 8601 timestamps in UTC
6. ✅ Valid JSON structure
7. ✅ Provenance with creator attribution

### Excellence Standards

For high-quality AKUs, include:

1. ⭐ Multiple ontology links (primary + secondary)
2. ⭐ Multilingual labels via Wikidata
3. ⭐ Complete SKOS relationship graph
4. ⭐ Detailed provenance with sources
5. ⭐ Examples and use cases
6. ⭐ Cross-domain relationships

---

## Troubleshooting

### Issue: Can't find ontology code

**Solution**: 
- Try synonyms and alternative terms
- Navigate from broader concepts
- Check if concept is language-specific
- Use closeMatch or broadMatch for nearest concept

### Issue: Timestamp format error

**Solution**:
```bash
# Correct format
"2025-12-27T22:32:00.000Z"

# Common errors to avoid
"2025-12-27"  # Missing time
"2025-12-27T22:32:00"  # Missing timezone
"2025-12-27T22:32:00+00:00"  # Wrong timezone format (use Z)
"12/27/2025"  # Wrong date format
```

### Issue: Validation fails

**Solution**:
1. Check JSON syntax first
2. Verify @context array present
3. Ensure all SKOS properties have correct format
4. Verify timestamps are ISO 8601 with Z suffix
5. Check all relationship objects have @type: "skos:Concept"

---

## Support Resources

### Documentation
- **This Guide**: `docs/NEW-AKU-CREATION-GUIDE.md`
- **Migration Guide**: `docs/COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md`
- **Quick Start**: `docs/ONTOLOGY-QUICKSTART.md`

### Templates
- **Medical**: `docs/templates/medical-aku-ontology-template.json`
- **Economics**: `docs/templates/economics-aku-ontology-template.json`
- **Science**: `docs/templates/science-aku-ontology-template.json`

### Tools
- **Validator**: `.project/agents/quality-assurance/tools/validate_ontology.py`
- **Enhancement**: `.project/enhance_npv_akus.py` (example for automation)

### Getting Help
1. Review templates in `docs/templates/`
2. Check examples in enhanced AKUs
3. Consult domain-specific guides
4. Use @terminology agent for research

---

**Last Updated**: 2025-12-27  
**Version**: 1.0  
**Status**: Production Ready
