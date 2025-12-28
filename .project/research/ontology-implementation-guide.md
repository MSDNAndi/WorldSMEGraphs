# Ontology Integration Implementation Guide

**Date**: 2025-12-27  
**Purpose**: Quick-start guide for implementing ontology integration  
**Related**: [Ontology Integration Specification](./ontology-integration-specification.md)

---

## Quick Start

### For Developers

**1. Update existing AKU with ontology support:**

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  "@id": "wsmg-econ:my-concept",
  "@type": ["schema:EducationalResource", "skos:Concept"],
  
  "skos:prefLabel": "My Concept",
  "skos:altLabel": ["Alternative Name"],
  "skos:definition": "Clear definition here",
  
  "relationships": {
    "hierarchical": {
      "skos:broader": ["wsmg-econ:parent-concept"],
      "skos:narrower": ["wsmg-econ:child-concept"]
    },
    "associative": {
      "skos:related": ["wsmg-econ:related-concept"]
    },
    "external": {
      "skos:exactMatch": "fibo:ExternalConcept",
      "skos:closeMatch": ["dbpedia:Related_Topic"]
    }
  }
}
```

**2. Validate ontology compliance:**

```bash
python .project/agents/quality-assurance/tools/validate_ontology.py path/to/aku.json --verbose
```

**3. Check integration:**
- ✅ Has @context with domain-specific context
- ✅ Has skos:prefLabel
- ✅ Has skos:definition or content.statement
- ✅ Has hierarchical relationships (broader/narrower)
- ✅ Has external ontology mappings when applicable
- ✅ Domain-specific ontology (SNOMED for medicine, FIBO for economics)

### For Agent Developers

**Use @ontology agent for complex ontology tasks:**

```
@ontology Design JSON-LD context for new domain: marine-biology. 
Include relevant ontologies: UniProt, GO, ENVO. Map key concepts 
to external ontologies. Create example AKU with full ontology integration.
```

**Use @semantic-harmonization for consistency:**

```
@semantic-harmonization Review economics AKUs for consistent SKOS 
relationships. Identify missing broader/narrower links. Suggest 
alignments with FIBO ontology.
```

---

## Context Files

### Location
```
domain/_contexts/
├── base.jsonld          # Core vocabulary (Schema.org, SKOS, DC, PROV)
├── medicine.jsonld      # Medical ontologies (SNOMED, MeSH, ICD-11)
├── economics.jsonld     # Economics/finance (FIBO)
├── science.jsonld       # Science domains (QUDT, ChEBI)
└── README.md           # Context documentation
```

### Usage in AKUs

**Single domain:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld"
  ]
}
```

**Multiple domains:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ]
}
```

**Custom terms:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/science.jsonld",
    {
      "myTerm": "https://worldsmegraphs.org/vocab/custom#myTerm"
    }
  ]
}
```

---

## SKOS Relationships

### Hierarchical

**Broader (more general):**
```json
"skos:broader": [
  "wsmg-econ:financial-concept",
  "wsmg-econ:valuation-method"
]
```

**Narrower (more specific):**
```json
"skos:narrower": [
  "wsmg-econ:npv-calculation",
  "wsmg-econ:npv-interpretation"
]
```

### Associative

**Related (associated concepts):**
```json
"skos:related": [
  "wsmg-econ:irr",
  "wsmg-econ:payback-period"
]
```

### External Mappings

**Exact match (same concept):**
```json
"skos:exactMatch": [
  "fibo:NetPresentValue",
  "wikidata:Q338801"
]
```

**Close match (similar concept):**
```json
"skos:closeMatch": [
  "dbpedia:Net_present_value"
]
```

**Same as (identical entity):**
```json
"owl:sameAs": [
  "http://www.wikidata.org/entity/Q338801"
]
```

---

## Domain-Specific Ontologies

### Medicine

**Required elements:**
- SNOMED CT concept ID when available
- MeSH heading for literature context
- ICD-11 code for conditions
- Schema.org medical types

**Example:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld"
  ],
  "@type": ["schema:MedicalCondition", "skos:Concept"],
  
  "skos:exactMatch": "snomed:449567000",
  "skos:closeMatch": "mesh:D000078862",
  
  "schema:medicalCode": [
    {
      "@type": "MedicalCode",
      "schema:codeValue": "449567000",
      "schema:codingSystem": "SNOMED CT"
    }
  ]
}
```

### Economics/Finance

**Required elements:**
- FIBO concept mapping when available
- Wikidata entity for general concepts
- DBpedia for encyclopedic knowledge

**Example:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  "@type": ["skos:Concept", "wsmg-econ:FinancialConcept"],
  
  "skos:exactMatch": "fibo:NetPresentValue",
  "skos:closeMatch": [
    "dbpedia:Net_present_value",
    "wikidata:Q338801"
  ]
}
```

### Science

**Required elements:**
- QUDT units for quantities
- Domain-specific ontologies (ChEBI, GO, etc.)
- DBpedia for general scientific concepts

**Example:**
```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/science.jsonld"
  ],
  "@type": ["skos:Concept", "wsmg-sci:PhysicalLaw"],
  
  "wsmg:formula": {
    "variables": [
      {
        "symbol": "F",
        "qudt:quantityKind": "qudt:Force",
        "qudt:unit": "unit:N"
      }
    ]
  }
}
```

---

## Migration Checklist

### For Existing AKUs

- [ ] Add @context array with base + domain contexts
- [ ] Add @id with wsmg prefix
- [ ] Add @type including skos:Concept
- [ ] Add skos:prefLabel (can copy from existing name/title)
- [ ] Add skos:altLabel for alternative terms
- [ ] Add skos:definition (can copy from content.statement)
- [ ] Convert relationships.prerequisites → skos:broader
- [ ] Convert relationships.enables → skos:narrower
- [ ] Convert relationships.related_to → skos:related
- [ ] Add external mappings (skos:exactMatch, closeMatch)
- [ ] Add domain-specific ontology references
- [ ] Add provenance with prov: properties
- [ ] Validate with validate_ontology.py

### For New AKUs

- [ ] Start with enhanced template (see examples)
- [ ] Use domain-specific context
- [ ] Include all SKOS properties from start
- [ ] Research external ontology mappings
- [ ] Add rich provenance tracking
- [ ] Validate before committing

---

## Validation

### Command-Line Validation

**Single file:**
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py aku.json --verbose
```

**Directory:**
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py --directory path/to/akus/ --verbose
```

**Domain:**
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py --domain economics --verbose
```

### Validation Checks

The validator checks for:
- ✅ Valid @context (base + domain)
- ✅ Proper @id format
- ✅ @type includes Schema.org or SKOS types
- ✅ SKOS labels (prefLabel, altLabel, definition)
- ✅ SKOS relationship consistency
- ✅ External ontology mappings
- ✅ Domain-specific requirements

### Common Issues and Fixes

**Issue: Missing @context**
```json
// ❌ Wrong
{
  "@context": "https://schema.org/"
}

// ✅ Fixed
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ]
}
```

**Issue: Missing SKOS labels**
```json
// ❌ Wrong
{
  "content": {
    "statement": {"text": "Definition here"}
  }
}

// ✅ Fixed
{
  "skos:prefLabel": "Concept Name",
  "skos:definition": "Definition here",
  "content": {
    "statement": {"text": "Definition here"}
  }
}
```

**Issue: No external mappings**
```json
// ❌ Missing external links
{
  "relationships": {
    "pedagogical": {"prerequisites": [...]}
  }
}

// ✅ Added external mappings
{
  "relationships": {
    "pedagogical": {"prerequisites": [...]},
    "external": {
      "skos:exactMatch": "fibo:ConceptName",
      "skos:closeMatch": ["dbpedia:Concept", "wikidata:Q12345"]
    }
  }
}
```

---

## Finding External Ontology Mappings

### Medical Domain

**SNOMED CT:**
1. Visit: https://browser.ihtsdotools.org/
2. Search for medical concept
3. Copy concept ID (e.g., 449567000)
4. Use as: `"snomed:449567000"`

**MeSH:**
1. Visit: https://meshb.nlm.nih.gov/
2. Search for medical subject
3. Copy MeSH ID (e.g., D000078862)
4. Use as: `"mesh:D000078862"`

### Economics Domain

**FIBO:**
1. Visit: https://spec.edmcouncil.org/fibo/ontology/
2. Browse or search for financial concept
3. Copy full URI or use prefix notation
4. Use as: `"fibo:NetPresentValue"`

**Wikidata:**
1. Visit: https://www.wikidata.org/
2. Search for concept
3. Copy Q-number (e.g., Q338801)
4. Use as: `"wikidata:Q338801"`

### Science Domain

**QUDT Units:**
1. Visit: http://www.qudt.org/
2. Browse units or quantity kinds
3. Use standard QUDT notation
4. Example: `"unit:N"` for Newton

**ChEBI:**
1. Visit: https://www.ebi.ac.uk/chebi/
2. Search for chemical compound
3. Copy ChEBI ID
4. Use as: `"chebi:CHEBI_15377"`

---

## Resources

### Documentation
- [Ontology Integration Specification](./ontology-integration-specification.md) - Complete technical spec
- [Knowledge Format v2](../knowledge-format-v2.md) - AKU format documentation
- [Context README](../../domain/_contexts/README.md) - Context file documentation

### Tools
- **Validator**: `.project/agents/quality-assurance/tools/validate_ontology.py`
- **JSON-LD Playground**: https://json-ld.org/playground/
- **RDF Validator**: https://www.w3.org/RDF/Validator/

### Ontology Browsers
- **SNOMED CT**: https://browser.ihtsdotools.org/
- **MeSH**: https://meshb.nlm.nih.gov/
- **FIBO**: https://spec.edmcouncil.org/fibo/
- **Wikidata**: https://www.wikidata.org/
- **BioPortal**: https://bioportal.bioontology.org/
- **LOV**: https://lov.linkeddata.es/dataset/lov/

### W3C Standards
- **SKOS**: https://www.w3.org/2004/02/skos/
- **JSON-LD**: https://www.w3.org/TR/json-ld11/
- **PROV-O**: https://www.w3.org/TR/prov-o/
- **OWL**: https://www.w3.org/OWL/

---

## Examples

### Complete Examples

**Medicine**: See `.project/research/ontology-integration-specification.md` Example 1
**Economics**: See `.project/pilot/npv-finance/akus/definitions/aku-003-present-value-concept-ENHANCED.json`
**Science**: See `.project/research/ontology-integration-specification.md` Example 3
**Cross-Domain**: See `.project/research/ontology-integration-specification.md` Example 4

---

## Getting Help

**For ontology design questions:**
```
@ontology [Your question about ontology design]
```

**For semantic consistency:**
```
@semantic-harmonization [Your question about terminology/relationships]
```

**For standards compliance:**
```
@standards [Your question about W3C/ISO standards]
```

---

**Last Updated**: 2025-12-27  
**Version**: 1.0  
**Maintained By**: @ontology, @semantic-harmonization
