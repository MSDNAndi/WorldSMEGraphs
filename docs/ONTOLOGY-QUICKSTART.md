# Ontology Integration Quick Start Guide

**Version**: 1.0  
**Date**: 2025-12-27  
**For**: Contributors and Developers

---

## Overview

WorldSMEGraphs now uses standard W3C ontologies to enable semantic interoperability. This guide helps you quickly understand and use the ontology system.

## What Changed?

### Before (Simple Relationships)
```json
{
  "relationships": {
    "prerequisites": ["time-value-of-money"],
    "enables": ["npv-calculation"],
    "related_to": ["future-value"]
  }
}
```

### After (SKOS Ontology)
```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/economics.jsonld"
  ],
  "relationships": {
    "broader": ["wsmg:time-value-of-money"],
    "narrower": ["wsmg:npv-calculation"],
    "related": ["wsmg:future-value"],
    "exactMatch": ["fibo:PresentValue", "dbr:Present_value"]
  }
}
```

## Quick Reference

### SKOS Relationship Types

| Old Term | New Term | Meaning |
|----------|----------|---------|
| `prerequisites` | `broader` | More general concept this builds on |
| `enables` | `narrower` | More specific concept this leads to |
| `related_to` | `related` | Related concept (not hierarchical) |
| - | `exactMatch` | Exactly same concept in external ontology |
| - | `closeMatch` | Very similar concept in external ontology |

### Context Files

Use these in your `@context` array:

- **Base** (always include): `file://domain/_contexts/base.jsonld`
- **Medicine**: `file://domain/_contexts/medicine.jsonld` 
- **Economics**: `file://domain/_contexts/economics.jsonld`
- **Science**: `file://domain/_contexts/science.jsonld`

## Step-by-Step: Convert an AKU

### Step 1: Add Context

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/economics.jsonld"
  ],
  "@type": "EducationalResource"
}
```

### Step 2: Convert Relationships

**Before:**
```json
"relationships": {
  "prerequisites": ["compound-interest"],
  "enables": ["npv-calculation"],
  "related_to": ["future-value"]
}
```

**After:**
```json
"relationships": {
  "broader": {
    "@id": "wsmg:compound-interest",
    "@type": "skos:Concept"
  },
  "narrower": {
    "@id": "wsmg:npv-calculation", 
    "@type": "skos:Concept"
  },
  "related": {
    "@id": "wsmg:future-value",
    "@type": "skos:Concept"
  }
}
```

### Step 3: Add External Links (Optional)

Link to standard ontologies:

```json
"relationships": {
  "exactMatch": [
    "fibo:PresentValue",
    "dbr:Present_value"
  ],
  "broadMatch": [
    "fibo:TimeValue"
  ]
}
```

### Step 4: Validate

```bash
python .project/agents/quality-assurance/tools/validate_ontology.py your-aku.json
```

## Domain-Specific Examples

### Medicine Example

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/medicine.jsonld"
  ],
  "@type": ["MedicalEntity", "MedicalCondition"],
  "@id": "wsmg:type2-endoleak",
  "relationships": {
    "broader": {
      "@id": "wsmg:endoleak",
      "@type": "skos:Concept"
    },
    "exactMatch": [
      "snomed:449567000",
      "mesh:D000078862"
    ]
  }
}
```

### Economics Example

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/economics.jsonld"
  ],
  "@type": "EducationalResource",
  "@id": "wsmg:present-value",
  "relationships": {
    "broader": {
      "@id": "wsmg:time-value-of-money",
      "@type": "skos:Concept"
    },
    "exactMatch": [
      "fibo:PresentValue",
      "dbr:Present_value"
    ]
  }
}
```

### Science Example

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/science.jsonld"
  ],
  "@type": "EducationalResource",
  "@id": "wsmg:photosynthesis",
  "relationships": {
    "broader": {
      "@id": "wsmg:cellular-metabolism",
      "@type": "skos:Concept"
    },
    "related": {
      "@id": "wsmg:chlorophyll",
      "@type": "skos:Concept"
    },
    "exactMatch": [
      "go:0015979",
      "mesh:D010788"
    ]
  }
}
```

## Finding External Ontology URIs

### Medicine
- **SNOMED CT**: https://browser.ihtsdotools.org/
- **MeSH**: https://meshb.nlm.nih.gov/
- **ICD-11**: https://icd.who.int/browse11

### Economics/Finance
- **FIBO**: https://spec.edmcouncil.org/fibo/
- **DBpedia**: https://dbpedia.org/

### Science
- **Gene Ontology**: http://geneontology.org/
- **ChEBI**: https://www.ebi.ac.uk/chebi/
- **QUDT**: http://www.qudt.org/

### General
- **Schema.org**: https://schema.org/
- **DBpedia**: https://wiki.dbpedia.org/
- **Wikidata**: https://www.wikidata.org/

## Automated Migration

Use the migration tool to convert existing AKUs:

```bash
# Convert single AKU
python .project/agents/quality-assurance/tools/migrate_to_ontology.py input.json output.json

# Convert entire directory
python .project/agents/quality-assurance/tools/migrate_to_ontology.py \
  --directory .project/pilot/npv-finance/akus/definitions/ \
  --output-dir .project/pilot/npv-finance/akus/definitions-enhanced/
```

## Validation

### Validate Single AKU
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py aku.json
```

### Validate Directory
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py \
  --directory .project/pilot/npv-finance/akus/
```

### Validate by Domain
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py \
  --domain medicine
```

## Common Issues

### Issue: Context file not found
**Error**: `Cannot resolve context file`  
**Fix**: Use relative path from repository root: `file://domain/_contexts/base.jsonld`

### Issue: Invalid SKOS relationship
**Error**: `Invalid relationship type`  
**Fix**: Use only: `broader`, `narrower`, `related`, `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`

### Issue: Missing @type on relationships
**Warning**: `Relationship should have @type: skos:Concept`  
**Fix**: Add `"@type": "skos:Concept"` to relationship objects

## Benefits of Using Ontologies

1. **Interoperability**: Link to external knowledge bases (Wikipedia, medical databases, etc.)
2. **Discovery**: Users can find related content across domains
3. **Validation**: Machine-readable semantics enable automated consistency checking
4. **Standards**: Industry-standard vocabularies ensure clarity
5. **Future-Proof**: Extensible system for new domains

## Need Help?

- **Full Specification**: `.project/research/ontology-integration-specification.md`
- **Implementation Guide**: `.project/research/ontology-implementation-guide.md`
- **Context Documentation**: `domain/_contexts/README.md`
- **Examples**: `.project/pilot/npv-finance/akus/definitions/aku-003-present-value-concept-ENHANCED.json`

---

**Last Updated**: 2025-12-27  
**Status**: Ready for use
