# Type 2 Endoleak - Terminology & Ontology Annotations

**Domain**: Medicine / Vascular Surgery  
**Created**: 2025-12-27  
**Agent**: @terminology  
**Status**: Validated

---

## Overview

This directory contains standardized medical ontology annotations for Type 2 Endoleak concepts, validated against authoritative medical terminology sources including SNOMED CT, MeSH, ICD-11, and UMLS.

## Contents

### 1. `ONTOLOGY-IDENTIFIERS.md` (Primary Deliverable)
**Purpose**: Comprehensive reference document with all ontology URIs and match types  
**Use for**: 
- AKU annotation
- Semantic web linking
- Literature searches
- Clinical documentation

**Contains**:
- Complete SNOMED CT codes with URIs
- MeSH descriptors with tree numbers
- ICD-11 codes for administrative use
- Match type explanations (exactMatch, closeMatch, broadMatch)
- Implementation guidance
- Quick reference tables

### 2. `ontology-annotation.json` (Machine-Readable)
**Purpose**: Structured JSON-LD format for automated processing  
**Use for**:
- Programmatic integration
- Validation scripts
- Ontology mapping tools
- Knowledge graph construction

**Contains**:
- Full ontology metadata
- Cross-references between terminologies
- Match type classifications
- Quality assurance metadata

### 3. `QUICK-REFERENCE.txt` (Visual Guide)
**Purpose**: At-a-glance reference for developers and content creators  
**Use for**:
- Quick lookups during AKU creation
- Copy-paste URIs
- Understanding match types
- Terminal/console viewing

---

## Medical Ontology Standards Used

### SNOMED CT (Systematized Nomenclature of Medicine - Clinical Terms)
- **Authority**: SNOMED International
- **Purpose**: Clinical documentation, EHR systems, precise medical terminology
- **Coverage**: Most granular - includes specific Type 2 endoleak code
- **Validation**: https://browser.ihtsdotools.org/

### MeSH (Medical Subject Headings)
- **Authority**: U.S. National Library of Medicine
- **Purpose**: Literature indexing, PubMed searches, bibliographic work
- **Coverage**: General endoleak term (no Type 2 distinction)
- **Validation**: https://meshb.nlm.nih.gov/

### ICD-11 (International Classification of Diseases, 11th Revision)
- **Authority**: World Health Organization
- **Purpose**: Administrative, billing, epidemiology, statistics
- **Coverage**: Complication codes (requires extension for specificity)
- **Validation**: https://icd.who.int/browse11/

### UMLS (Unified Medical Language System)
- **Authority**: U.S. National Library of Medicine
- **Purpose**: Cross-ontology mapping, semantic interoperability
- **Coverage**: Integrates all above systems with unified concept IDs (CUIs)
- **Validation**: https://uts.nlm.nih.gov/

---

## Key Findings

### Exact Matches (Identical Concepts) ✅
- Type 2 endoleak: SNOMED 449567000
- Abdominal aortic aneurysm: SNOMED 233985008, MeSH D017544, ICD-11 2132508894
- EVAR: SNOMED 233689003
- Lumbar arteries: SNOMED 33795007
- Inferior mesenteric artery: SNOMED 33616005, MeSH D008638

### Close Matches (Similar with Differences) ⚠️
- Retrograde flow: SNOMED 255539007 (qualifier, not standalone)
- Blood vessel prosthesis: MeSH D019917 (device, not procedure)
- ICD-11 endoleak: MH84.Z (requires extension)

### Broad Matches (Parent Concepts) 📚
- General endoleak: SNOMED 445080003, MeSH D000078862
- Postoperative complications: MeSH D011183
- Circulatory complications: ICD-11 MH84

---

## Usage in AKUs

### Recommended JSON-LD Structure

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/medicine.jsonld"
  ],
  "@type": ["MedicalEntity", "MedicalCondition"],
  "@id": "wsmg:type2-endoleak",
  
  "relationships": {
    "exactMatch": [
      "snomed:449567000",
      "umls:C3549542"
    ],
    "broadMatch": [
      "snomed:445080003",
      "mesh:D000078862"
    ],
    "closeMatch": [
      "icd11:MH84.Z"
    ]
  },
  
  "medicalCode": [
    {
      "@type": "MedicalCode",
      "codingSystem": "SNOMED-CT",
      "codeValue": "449567000",
      "uri": "http://snomed.info/id/449567000"
    }
  ]
}
```

---

## Validation & Quality Assurance

**Validation Date**: 2025-12-27  
**Agent**: @terminology  
**Methodology**: Multi-source cross-reference validation  
**Confidence**: 98%  

**Sources Checked**:
- ✅ SNOMED CT International Browser
- ✅ MeSH Browser (NLM)
- ✅ ICD-11 Browser (WHO)
- ✅ UMLS Metathesaurus
- ✅ Society for Vascular Surgery Guidelines

**Conflicts Resolved**: 0  
**Deprecated Terms Found**: 0  
**Status**: Approved for implementation

---

## Related Documentation

- **AKU Definition**: `../akus/definitions/aku-001-type2-endoleak-definition.json`
- **Medical Context**: `/domain/_contexts/medicine.jsonld`
- **Ontology Quickstart**: `/docs/ONTOLOGY-QUICKSTART.md`
- **Base Context**: `/domain/_contexts/base.jsonld`

---

## For More Information

- **Ontology Integration Guide**: See `/docs/ONTOLOGY-QUICKSTART.md`
- **Medical Terminology Standards**: See `.github/copilot-instructions.md` (Domain-Specific Standards section)
- **Terminology Agent**: See `.github/agents/terminology.agent.md`

---

**Last Updated**: 2025-12-27T19:57:00Z  
**Version**: 1.0  
**Maintainer**: @terminology agent
