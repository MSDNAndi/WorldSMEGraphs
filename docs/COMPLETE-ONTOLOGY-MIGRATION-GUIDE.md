# Complete Knowledge Base Ontology Migration Guide

**Version**: 1.0  
**Date**: 2025-12-27  
**Status**: Production Ready  
**For**: Contributors enhancing AKUs with ontology annotations

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Process](#step-by-step-process)
4. [Domain-Specific Instructions](#domain-specific-instructions)
5. [Quality Checklist](#quality-checklist)
6. [Troubleshooting](#troubleshooting)
7. [Examples](#examples)

---

## Overview

This guide explains the complete process for migrating existing AKUs to the new ontology system with proper research and annotations. The migration ensures semantic interoperability with standard ontologies (SNOMED CT, MeSH, ICD-11, FIBO, etc.).

### What Gets Enhanced

Each AKU receives:
1. **Updated @context** - References to domain-specific JSON-LD contexts
2. **SKOS properties** - Human-readable labels, definitions, notations
3. **SKOS relationships** - Structured concept hierarchies (broader/narrower/related)
4. **External ontology links** - URIs to authoritative ontologies with match types
5. **PROV-O provenance** - Enhanced metadata tracking

---

## Prerequisites

### Required Knowledge
- Understanding of the domain being annotated
- Familiarity with JSON-LD format
- Access to ontology browsers (see resources below)

### Required Files
- Domain-specific context files in `domain/_contexts/`
- Ontology research documentation
- Validation tools in `.project/agents/quality-assurance/tools/`

### Resources
- **SNOMED CT Browser**: https://browser.ihtsdotools.org/
- **MeSH Browser**: https://meshb.nlm.nih.gov/
- **ICD-11 Browser**: https://icd.who.int/browse11
- **FIBO Navigator**: https://spec.edmcouncil.org/fibo/
- **DBpedia**: https://dbpedia.org/
- **Wikidata**: https://www.wikidata.org/

---

## Step-by-Step Process

### Phase 1: Terminology Research (CRITICAL)

**DO NOT SKIP THIS STEP** - This is where the value comes from.

#### 1.1 Identify Core Concepts

For each AKU, identify the primary concept:
- Read the AKU content thoroughly
- Extract the main concept being defined or explained
- List related concepts mentioned

Example for NPV AKU:
- Primary: Net Present Value
- Related: Present Value, Discount Rate, Cash Flow, Time Value of Money

#### 1.2 Research Standard Ontologies

For each concept, search in relevant ontologies:

**Medical Domain:**
1. Search SNOMED CT Browser for the concept
2. Verify the code is active and matches exactly
3. Find broader/narrower concepts in hierarchy
4. Search MeSH for descriptor
5. Check ICD-11 for disease classifications

**Economics/Finance Domain:**
1. Search FIBO ontology for financial concepts
2. Check DBpedia for general knowledge link
3. Find Wikidata entity with multilingual labels

**Science Domain:**
1. Search QUDT for units and quantities
2. Check ChEBI for chemical entities
3. Use Gene Ontology for biological concepts

#### 1.3 Classify Match Types

For each ontology link, determine the match type:

- **`exactMatch`**: Concept is identical
  - Example: NPV in FIBO exactly matches our NPV concept
  
- **`closeMatch`**: Concepts are very similar but not identical
  - Example: Discount factor as part of general discounting article
  
- **`broadMatch`**: External concept is broader/more general
  - Example: "Endoleak" (general) is broader than "Type 2 Endoleak"
  
- **`narrowMatch`**: External concept is narrower/more specific
  - Example: "Free Cash Flow" is narrower than general "Cash Flow"

#### 1.4 Document Research

Create a terminology reference document:

```markdown
# Ontology Identifiers for [Concept]

## SNOMED CT
- **URI**: http://snomed.info/id/449567000
- **FSN**: Type II endoleak (disorder)
- **Match Type**: exactMatch
- **Status**: Active

## MeSH
- **URI**: http://id.nlm.nih.gov/mesh/D000078862
- **Descriptor**: Endoleak
- **Match Type**: broadMatch

## Wikidata
- **URI**: http://www.wikidata.org/entity/Q1054308
- **Label**: "net present value"
- **Match Type**: exactMatch
```

### Phase 2: Apply Enhancements

#### 2.1 Update @context

Change from:
```json
"@context": "https://schema.org/"
```

To:
```json
"@context": [
  "file://domain/_contexts/base.jsonld",
  "file://domain/_contexts/medicine.jsonld"
]
```

Or for economics:
```json
"@context": [
  "file://domain/_contexts/base.jsonld",
  "file://domain/_contexts/economics.jsonld"
]
```

#### 2.2 Add SKOS Properties

Add after `@id`:

```json
"skos:prefLabel": "Type II Endoleak",
"skos:notation": "aku-001-type2-endoleak-definition",
"skos:definition": "Complication following EVAR characterized by retrograde blood flow...",
"skos:altLabel": ["Type 2 Endoleak", "T2EL"]
```

#### 2.3 Add External Ontology Links

Add at root level:

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
]
```

#### 2.4 Convert Relationships

**Before:**
```json
"relationships": {
  "prerequisites": ["abdominal-aortic-aneurysm", "evar-procedure"],
  "enables": ["endoleak-management"],
  "related_to": ["type1-endoleak", "type3-endoleak"]
}
```

**After (keep both for backward compatibility):**
```json
"relationships": {
  "prerequisites": ["abdominal-aortic-aneurysm", "evar-procedure"],
  "skos:broader": [
    {
      "@id": "wsmg:abdominal-aortic-aneurysm",
      "@type": "skos:Concept"
    },
    {
      "@id": "wsmg:evar-procedure",
      "@type": "skos:Concept"
    }
  ],
  "enables": ["endoleak-management"],
  "skos:narrower": [
    {
      "@id": "wsmg:endoleak-management",
      "@type": "skos:Concept"
    }
  ],
  "related_to": ["type1-endoleak"],
  "skos:related": [
    {
      "@id": "wsmg:type1-endoleak",
      "@type": "skos:Concept"
    }
  ]
}
```

#### 2.5 Enhance Provenance

Add PROV-O properties:

```json
"provenance": {
  "sources": [...],
  "dc:creator": ["original-agent", "ontology-enhancement-agent"],
  "dc:modified": "2025-12-27T22:00:00.000Z",
  "prov:wasDerivedFrom": [
    {
      "dc:title": "Society for Vascular Surgery guidelines",
      "dc:bibliographicCitation": "SVS Practice Guidelines 2018"
    }
  ]
}
```

#### 2.6 Update Metadata

```json
"metadata": {
  "version": "1.0.0",
  "status": "ontology-enhanced",
  "last_updated": "2025-12-27T22:00:00.000Z",
  "contributors": [
    "original-agent",
    "terminology-agent",
    "ontology-enhancement-agent"
  ]
}
```

### Phase 3: Validation

#### 3.1 JSON Structure Validation

```bash
python -m json.tool path/to/aku.json > /dev/null
```

Should show no errors.

#### 3.2 Ontology Compliance Validation

```bash
python .project/agents/quality-assurance/tools/validate_ontology.py path/to/aku.json
```

Should show 100% pass rate.

#### 3.3 Manual Review

Check:
- [ ] All external URIs are valid (no typos)
- [ ] Match types are appropriate
- [ ] SKOS relationships make logical sense
- [ ] All required fields present
- [ ] Timestamps are current and in ISO 8601 format

---

## Domain-Specific Instructions

### Medical Domain

**Primary Ontologies**: SNOMED CT, MeSH, ICD-11

**Special Considerations**:
- Always search SNOMED CT first (most comprehensive)
- Use FSN (Fully Specified Name) to verify correct concept
- Check if concept is active, not retired
- MeSH often provides only broadMatch (less granular than SNOMED)
- ICD-11 for diseases and complications

**Example Workflow**:
1. Search "Type 2 endoleak" in SNOMED CT Browser
2. Find code 449567000, verify FSN matches
3. Navigate hierarchy to find broader concept (Endoleak: 445080003)
4. Search MeSH for "endoleak", find D000078862
5. Check ICD-11 for complication codes

### Economics/Finance Domain

**Primary Ontologies**: FIBO, DBpedia, Wikidata

**Special Considerations**:
- FIBO is most authoritative for financial concepts
- Use DBpedia for general business concepts not in FIBO
- Wikidata provides multilingual labels (very useful)
- ISO 20022 codes for standard business transactions

**Example Workflow**:
1. Navigate FIBO ontology structure
2. Search for concept in FBC (Financial Business and Commerce) module
3. Cross-reference with DBpedia article
4. Find Wikidata entity for multilingual support
5. Document all three for comprehensive linking

### Science Domain

**Primary Ontologies**: QUDT, ChEBI, Gene Ontology

**Special Considerations**:
- QUDT for units, quantities, dimensions
- ChEBI for chemical entities (molecular structures)
- Gene Ontology for biological processes
- Use Schema.org for general scientific concepts

---

## Quality Checklist

Before finalizing each AKU enhancement:

- [ ] **Research Complete**: All concepts researched in relevant ontologies
- [ ] **URIs Validated**: All external links tested and working
- [ ] **Match Types Correct**: exactMatch/closeMatch/broadMatch applied appropriately
- [ ] **SKOS Properties Present**: prefLabel, definition, notation added
- [ ] **Relationships Converted**: Prerequisites→broader, enables→narrower, related_to→related
- [ ] **Provenance Enhanced**: PROV-O properties added
- [ ] **Metadata Updated**: Status, timestamp, contributors updated
- [ ] **JSON Valid**: File parses without errors
- [ ] **Ontology Validator Passes**: 100% validation success
- [ ] **Documentation Updated**: Terminology reference document complete

---

## Troubleshooting

### Issue: Cannot find ontology code

**Solution**: 
1. Try alternate search terms (synonyms, abbreviations)
2. Navigate hierarchy from broader concepts
3. Check if concept is language-specific (use English terms)
4. Ask domain expert or use closeMatch/broadMatch for nearest concept

### Issue: Multiple matching codes

**Solution**:
1. Read definitions carefully - choose most specific match
2. Use FSN in SNOMED to disambiguate
3. Check hierarchy placement
4. Document all matches if genuinely equivalent

### Issue: Ontology URL format unclear

**Solution**:
- **SNOMED CT**: `http://snomed.info/id/XXXXXXX` (7-9 digit code)
- **MeSH**: `http://id.nlm.nih.gov/mesh/DXXXXXX` (D + 6 digits)
- **ICD-11**: `http://id.who.int/icd/entity/XXXXXXXXX` (numeric code)
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/MODULE/SubModule/Concept`
- **DBpedia**: `http://dbpedia.org/resource/Article_Title`
- **Wikidata**: `http://www.wikidata.org/entity/QXXXXXX` (Q + digits)

### Issue: Validation fails

**Solution**:
1. Check JSON syntax first (`python -m json.tool`)
2. Verify all required SKOS properties present
3. Ensure @context array has both base and domain contexts
4. Check timestamps are ISO 8601 format with Z suffix
5. Verify all relationship objects have @type: "skos:Concept"

---

## Examples

### Complete Medical AKU Example

See: `domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/akus/definitions/aku-001-type2-endoleak-definition.json`

Key features:
- SNOMED CT exactMatch (449567000)
- MeSH broadMatch (D000078862)
- ICD-11 closeMatch (MH84.Z)
- Complete SKOS properties
- PROV-O provenance
- Both legacy and SKOS relationships

### Complete Economics AKU Example

See: `.project/pilot/npv-finance/akus/definitions/aku-001-npv-definition.json`

Key features:
- FIBO exactMatch
- DBpedia exactMatch  
- Wikidata exactMatch with multilingual labels
- SKOS alternative labels (NPV, Nettobarwert, VAN)
- Complete SKOS relationships
- PROV-O provenance

---

## Automation Tools

### Available Scripts

1. **Enhancement Script**: `.project/enhance_npv_akus.py`
   - Applies ontology annotations based on predefined mappings
   - Use as template for other domains

2. **Validation Script**: `.project/agents/quality-assurance/tools/validate_ontology.py`
   - Validates ontology compliance
   - Domain-aware checking

3. **Migration Script**: `.project/agents/quality-assurance/tools/migrate_to_ontology.py`
   - Handles structural conversions
   - Best used after research phase

### When to Use Automation

**Use automation for**:
- Structural changes (@context, basic SKOS properties)
- Batch relationship conversions
- Provenance updates

**DO NOT use automation for**:
- Ontology research (requires human judgment)
- Match type classification (requires domain expertise)
- External URI discovery (must be validated)

---

## Support

### Documentation
- **Main Spec**: `.project/research/ontology-integration-specification.md`
- **Quick Start**: `docs/ONTOLOGY-QUICKSTART.md`
- **Medical Guide**: `docs/MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md`
- **This Guide**: `docs/COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md`

### Getting Help
1. Review terminology documentation in `domain/{domain}/terminology/`
2. Check examples in enhanced AKUs
3. Consult domain experts for complex concepts
4. Use @terminology agent for research assistance

---

**Last Updated**: 2025-12-27  
**Version**: 1.0  
**Status**: Production Ready
