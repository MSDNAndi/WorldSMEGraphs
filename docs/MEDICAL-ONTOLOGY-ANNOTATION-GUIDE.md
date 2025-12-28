# Medical Ontology Annotation Guide for WorldSMEGraphs

**Version**: 1.0  
**Date**: 2025-12-27  
**Author**: @terminology agent  
**Purpose**: Guide for annotating medical AKUs with standard ontology identifiers

---

## Table of Contents
- [Overview](#overview)
- [Required Ontology Standards](#required-ontology-standards)
- [Annotation Workflow](#annotation-workflow)
- [JSON-LD Structure](#json-ld-structure)
- [Finding Ontology Codes](#finding-ontology-codes)
- [Match Types Explained](#match-types-explained)
- [Domain-Specific Guidelines](#domain-specific-guidelines)
- [Validation](#validation)
- [Common Patterns](#common-patterns)
- [Examples](#examples)

---

## Overview

Medical AKUs in WorldSMEGraphs must be annotated with standard medical ontology identifiers to:
- Enable semantic interoperability with external medical knowledge bases
- Support EHR (Electronic Health Record) integration
- Facilitate literature search and indexing
- Enable clinical decision support systems
- Support administrative and billing systems

### Key Principles
1. **Use multiple ontologies**: SNOMED CT (clinical), MeSH (literature), ICD-11 (administrative)
2. **Specify match types**: exactMatch, closeMatch, broadMatch
3. **Validate against authoritative sources**: Official browsers and terminology servers
4. **Document confidence**: Include validation metadata
5. **Update regularly**: Medical terminologies evolve

---

## Required Ontology Standards

### 1. SNOMED CT (Primary for Clinical Use)
**Authority**: SNOMED International  
**Use for**: Clinical documentation, EHR systems, precise medical terminology  
**Browser**: https://browser.ihtsdotools.org/  
**Format**: `http://snomed.info/id/XXXXXXX` (7-8 digit code)

**Strengths**:
- Most granular clinical terminology
- Hierarchical relationships
- Covers all medical domains
- International standard

**Example**: Type 2 endoleak → `http://snomed.info/id/449567000`

### 2. MeSH (Medical Subject Headings)
**Authority**: U.S. National Library of Medicine  
**Use for**: Literature indexing, PubMed searches, bibliographic work  
**Browser**: https://meshb.nlm.nih.gov/  
**Format**: `http://id.nlm.nih.gov/mesh/DXXXXXX` (Descriptor ID)

**Strengths**:
- Optimized for literature search
- Tree structure for browsing
- Updated annually
- Gold standard for MEDLINE

**Example**: Endoleak → `http://id.nlm.nih.gov/mesh/D000078862`

### 3. ICD-11 (International Classification of Diseases)
**Authority**: World Health Organization  
**Use for**: Administrative, billing, epidemiology, statistics  
**Browser**: https://icd.who.int/browse11/  
**Format**: `http://id.who.int/icd/entity/XXXXXXXXX` (Numeric entity ID)

**Strengths**:
- International standard for health statistics
- Required for billing in many countries
- WHO maintained
- Structured hierarchically

**Example**: Abdominal aortic aneurysm → `http://id.who.int/icd/entity/2132508894`

### 4. UMLS (Unified Medical Language System) - Optional but Recommended
**Authority**: U.S. National Library of Medicine  
**Use for**: Cross-ontology mapping, semantic interoperability  
**Browser**: https://uts.nlm.nih.gov/  
**Format**: `http://linkedlifedata.com/resource/umls/id/CXXXXXXX` (CUI)

**Strengths**:
- Integrates 200+ terminologies
- Unified concept identifiers
- Cross-reference mapping
- Semantic networks

**Example**: Type II Endoleak → `http://linkedlifedata.com/resource/umls/id/C3549542`

---

## Annotation Workflow

### Step 1: Identify Medical Concepts
Extract all medical concepts from AKU content:
- Primary condition/procedure
- Related conditions
- Anatomical structures
- Procedures
- Devices
- Medications (if applicable)

### Step 2: Research Ontology Codes
For each concept, search:
1. **SNOMED CT Browser**: Most precise clinical codes
2. **MeSH Browser**: Literature indexing
3. **ICD-11 Browser**: Administrative codes
4. **UMLS Metathesaurus**: Unified concepts and mappings

### Step 3: Determine Match Types
- **exactMatch**: Concept is identical
- **closeMatch**: Very similar, minor differences
- **broadMatch**: Target is more general/broader
- **narrowMatch**: Target is more specific (rarely used)

### Step 4: Structure Annotations
Add to AKU JSON-LD:
```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/medicine.jsonld"
  ],
  "@type": ["EducationalResource", "MedicalEntity"],
  
  "relationships": {
    "exactMatch": ["snomed:XXXXXXX", "umls:CXXXXXXX"],
    "broadMatch": ["mesh:DXXXXXX"],
    "closeMatch": ["icd11:ENTITY_ID"]
  },
  
  "medicalCode": [
    {
      "@type": "MedicalCode",
      "codingSystem": "SNOMED-CT",
      "codeValue": "XXXXXXX",
      "uri": "http://snomed.info/id/XXXXXXX",
      "description": "Full name from SNOMED"
    }
  ]
}
```

### Step 5: Validate
- Check codes in official browsers
- Verify URIs are correctly formatted
- Ensure match types are appropriate
- Validate JSON-LD structure
- Run domain validation tool

### Step 6: Document
- Update metadata with terminology-agent contributor
- Add validation timestamp
- Document confidence level
- Note any ambiguities or limitations

---

## JSON-LD Structure

### Complete Annotation Template

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/medicine.jsonld"
  ],
  "@type": ["EducationalResource", "MedicalEntity", "MedicalCondition"],
  "@id": "wsmg-med:concept-identifier",
  
  "metadata": {
    "version": "2.0.0",
    "created": "2025-XX-XXT00:00:00.000Z",
    "last_updated": "2025-XX-XXT00:00:00.000Z",
    "contributors": [
      "original-author",
      "terminology-agent"
    ],
    "confidence": 0.98,
    "status": "enhanced"
  },
  
  "relationships": {
    "broader": [
      {
        "@id": "wsmg-med:parent-concept",
        "@type": "skos:Concept",
        "label": "Parent Concept Name"
      }
    ],
    "narrower": [
      {
        "@id": "wsmg-med:child-concept",
        "@type": "skos:Concept",
        "label": "Child Concept Name"
      }
    ],
    "related": [
      {
        "@id": "wsmg-med:related-concept",
        "@type": "skos:Concept",
        "label": "Related Concept Name"
      }
    ],
    "exactMatch": [
      "snomed:XXXXXXX",
      "umls:CXXXXXXX"
    ],
    "broadMatch": [
      "snomed:PARENT_CODE",
      "mesh:DXXXXXX"
    ],
    "closeMatch": [
      "icd11:ENTITY_ID"
    ]
  },
  
  "medicalCode": [
    {
      "@type": "MedicalCode",
      "codingSystem": "SNOMED-CT",
      "codeValue": "XXXXXXX",
      "uri": "http://snomed.info/id/XXXXXXX",
      "description": "Fully specified name",
      "preferred": true
    },
    {
      "@type": "MedicalCode",
      "codingSystem": "MeSH",
      "codeValue": "DXXXXXX",
      "uri": "http://id.nlm.nih.gov/mesh/DXXXXXX",
      "description": "MeSH heading",
      "note": "Optional note about usage"
    },
    {
      "@type": "MedicalCode",
      "codingSystem": "ICD-11",
      "codeValue": "XX00.0",
      "uri": "http://id.who.int/icd/entity/XXXXXXXXX",
      "description": "ICD-11 title",
      "note": "May require extension code"
    },
    {
      "@type": "MedicalCode",
      "codingSystem": "UMLS",
      "codeValue": "CXXXXXXX",
      "uri": "http://linkedlifedata.com/resource/umls/id/CXXXXXXX",
      "description": "UMLS preferred term"
    }
  ],
  
  "anatomicalStructure": [
    {
      "@type": "AnatomicalStructure",
      "name": "Structure name",
      "snomedCode": "XXXXXXX",
      "uri": "http://snomed.info/id/XXXXXXX",
      "role": "affected_structure"
    }
  ],
  
  "terminology_metadata": {
    "validation_agent": "terminology",
    "validation_date": "2025-XX-XXT00:00:00.000Z",
    "ontology_version": "1.0",
    "sources_validated": [
      "SNOMED CT International Edition",
      "MeSH 2025",
      "ICD-11 2024",
      "UMLS Metathesaurus"
    ],
    "confidence": 0.98
  }
}
```

---

## Finding Ontology Codes

### SNOMED CT Search Strategy

1. **Go to**: https://browser.ihtsdotools.org/
2. **Search by**: Condition name, procedure, anatomy
3. **Look for**:
   - Fully Specified Name (FSN)
   - Concept ID (7-8 digits)
   - Active status
   - Appropriate semantic tag (disorder, procedure, body structure)

**Example Search**: "endoleak"
- Results: Multiple concepts
- Select: "Type II endoleak (disorder)" - 449567000
- Verify: Active status, correct hierarchy

### MeSH Search Strategy

1. **Go to**: https://meshb.nlm.nih.gov/
2. **Search by**: Medical term
3. **Look for**:
   - Descriptor ID (D + 6 digits)
   - MeSH Heading
   - Tree Numbers (for hierarchy)
   - Year introduced

**Example Search**: "Endoleak"
- Result: D000078862
- Introduced: 2019
- Tree: C14.907.055.239.075

### ICD-11 Search Strategy

1. **Go to**: https://icd.who.int/browse11/
2. **Search by**: Condition or procedure
3. **Look for**:
   - Code (alphanumeric)
   - Entity ID (numeric URI component)
   - Title
   - Parent categories

**Example Search**: "Abdominal aortic aneurysm"
- Code: BB40.00
- Entity: 2132508894
- URI: http://id.who.int/icd/entity/2132508894

---

## Match Types Explained

### exactMatch ✅
**Definition**: The concept is semantically identical across ontologies.

**Use when**:
- Same clinical entity
- Same scope and definition
- Same level of specificity
- Interchangeable in context

**Examples**:
- Type 2 endoleak = SNOMED 449567000 (exactMatch)
- Abdominal aortic aneurysm = SNOMED 233985008 = MeSH D017544 (exactMatch)

### closeMatch ⚠️
**Definition**: Concepts are highly similar but have minor differences in scope or specificity.

**Use when**:
- Similar but not identical meaning
- Different levels of specificity
- Contextual differences
- Requires qualification or extension

**Examples**:
- Retrograde flow ≈ SNOMED 255539007 (closeMatch - qualifier, not standalone)
- Type 2 endoleak ≈ ICD-11 MH84.Z (closeMatch - requires extension)

### broadMatch 📚
**Definition**: Target concept is more general/broader than source concept.

**Use when**:
- Linking to parent concepts
- General categories
- Broader clinical domains
- Less specific terminology

**Examples**:
- Type 2 endoleak → Endoleak (general) SNOMED 445080003 (broadMatch)
- Type 2 endoleak → Postoperative complications MeSH D011183 (broadMatch)

### narrowMatch 🔍 (Rare)
**Definition**: Target concept is more specific than source concept.

**Use when**:
- Subtypes or variants
- More specific classifications

**Example**:
- Endoleak (general) → Type 2a endoleak (narrowMatch)

---

## Domain-Specific Guidelines

### Cardiovascular Medicine
**Key Ontologies**: SNOMED CT, MeSH, ICD-11  
**Focus Areas**: Conditions, procedures, anatomy, devices

**Common Codes**:
- Cardiovascular diseases: ICD-11 BA00-BE2Z
- Heart structures: SNOMED anatomical hierarchy
- Cardiac procedures: SNOMED procedure concepts

### Surgery
**Key Ontologies**: SNOMED CT (primary), MeSH, ICD-11  
**Focus Areas**: Procedures, complications, devices

**Common Patterns**:
- Procedure codes from SNOMED
- Complication codes from ICD-11 MH section
- Device codes from SNOMED or MeSH

### Oncology
**Key Ontologies**: SNOMED CT, ICD-O-3, MeSH, ICD-11  
**Focus Areas**: Tumor types, staging, treatments

**Additional Standards**:
- ICD-O-3 for morphology
- TNM staging system
- Cancer-specific terminologies

### Pharmacology
**Key Ontologies**: RxNorm, ATC, SNOMED CT, MeSH  
**Focus Areas**: Medications, ingredients, formulations

**Additional Standards**:
- RxNorm for drug naming
- ATC classification
- DrugBank identifiers

---

## Validation

### Automated Validation
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate all medical AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine

# Validate specific directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/medicine/
```

### Manual Validation Checklist

- [ ] All URIs are correctly formatted
- [ ] Codes verified in official browsers
- [ ] Match types are appropriate
- [ ] @context includes base.jsonld and medicine.jsonld
- [ ] @type includes EducationalResource
- [ ] medicalCode section present for primary concepts
- [ ] Metadata updated with terminology-agent
- [ ] Confidence level documented
- [ ] Validation timestamp current

---

## Common Patterns

### Pattern 1: Medical Condition
```json
{
  "@type": ["EducationalResource", "MedicalEntity", "MedicalCondition"],
  "relationships": {
    "exactMatch": ["snomed:CONDITION_CODE"],
    "broadMatch": ["mesh:DISEASE_CATEGORY"]
  },
  "medicalCode": [
    {"codingSystem": "SNOMED-CT", "codeValue": "..."},
    {"codingSystem": "ICD-11", "codeValue": "..."}
  ]
}
```

### Pattern 2: Medical Procedure
```json
{
  "@type": ["EducationalResource", "MedicalEntity", "MedicalProcedure"],
  "relationships": {
    "exactMatch": ["snomed:PROCEDURE_CODE"],
    "broadMatch": ["mesh:PROCEDURE_CATEGORY"]
  },
  "medicalCode": [
    {"codingSystem": "SNOMED-CT", "codeValue": "..."}
  ]
}
```

### Pattern 3: Anatomical Structure
```json
{
  "anatomicalStructure": [
    {
      "@type": "AnatomicalStructure",
      "name": "Structure name",
      "snomedCode": "XXXXXXX",
      "uri": "http://snomed.info/id/XXXXXXX"
    }
  ]
}
```

### Pattern 4: Complication
```json
{
  "@type": ["EducationalResource", "MedicalEntity", "MedicalCondition"],
  "possibleComplication": {
    "@id": "wsmg-med:parent-condition",
    "name": "Parent condition"
  },
  "relationships": {
    "exactMatch": ["snomed:COMPLICATION_CODE"],
    "broadMatch": ["icd11:COMPLICATION_CATEGORY"]
  }
}
```

---

## Examples

See complete examples in:
- `/domain/medicine/surgery/vascular/complications/endoleaks/type-2/terminology/EXAMPLE-enhanced-aku.json`
- `/domain/medicine/surgery/vascular/complications/endoleaks/type-2/akus/definitions/aku-001-type2-endoleak-definition.json`

---

## References

### Official Resources
- **SNOMED CT**: https://www.snomed.org/
- **MeSH**: https://www.nlm.nih.gov/mesh/
- **ICD-11**: https://icd.who.int/
- **UMLS**: https://www.nlm.nih.gov/research/umls/

### WorldSMEGraphs Documentation
- Ontology Quick Start: `/docs/ONTOLOGY-QUICKSTART.md`
- Medical Context: `/domain/_contexts/medicine.jsonld`
- Base Context: `/domain/_contexts/base.jsonld`
- Terminology Agent: `/.github/agents/terminology.agent.md`

---

**Version**: 1.0  
**Last Updated**: 2025-12-27  
**Maintained by**: @terminology agent  
**Status**: Active
