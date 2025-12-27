# JSON-LD Context Files for WorldSMEGraphs

This directory contains JSON-LD context files that define the semantic vocabulary used across WorldSMEGraphs knowledge representation system.

## Overview

These context files enable semantic interoperability by:
- Mapping short property names to full URIs
- Integrating with standard ontologies (Schema.org, SKOS, SNOMED CT, FIBO, etc.)
- Providing domain-specific vocabularies
- Supporting linked data and semantic web standards

## Context Files

### `base.jsonld`
**Purpose**: Core vocabulary used by all AKUs

**Includes**:
- Schema.org base vocabulary
- SKOS (Simple Knowledge Organization System) for concept relationships
- Dublin Core Terms for metadata
- PROV-O for provenance tracking
- OWL for ontology axioms
- RDF/RDFS base vocabularies

**Usage**: Automatically included in all domain contexts

### `medicine.jsonld`
**Purpose**: Medical and healthcare domain vocabulary

**Includes**:
- SNOMED CT integration
- MeSH (Medical Subject Headings)
- ICD-11 classification
- UMLS (Unified Medical Language System)
- RxNorm for medications
- Schema.org medical types

**Usage**: For medical, clinical, and healthcare AKUs

### `economics.jsonld`
**Purpose**: Economics and finance domain vocabulary

**Includes**:
- FIBO (Financial Industry Business Ontology)
- DBpedia economics categories
- Schema.org financial types
- Custom economics terminology

**Usage**: For economics, finance, and business AKUs

### `science.jsonld`
**Purpose**: Scientific domains vocabulary

**Includes**:
- QUDT (Quantities, Units, Dimensions, and Types)
- ChEBI (Chemical Entities of Biological Interest)
- Gene Ontology
- NASA SWEET (Semantic Web for Earth and Environmental Terminology)
- Physics and chemistry vocabularies

**Usage**: For physics, chemistry, biology, and other science AKUs

## How to Use

### In AKU Files

Reference contexts in the `@context` property at the top of each AKU:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld"
  ],
  "@id": "wsmg-med:type2-endoleak-001",
  "@type": ["schema:MedicalCondition", "skos:Concept"],
  ...
}
```

### Multiple Domains

For cross-domain AKUs, include multiple contexts:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  ...
}
```

### Custom Terms

Add local context for AKU-specific terms:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/science.jsonld",
    {
      "myCustomTerm": "https://worldsmegraphs.org/vocab/custom#term"
    }
  ],
  ...
}
```

## Context Resolution

### Development
During development, contexts resolve to local files:
```
base.jsonld → domain/_contexts/base.jsonld
```

### Production
In production, contexts resolve to stable URLs:
```
https://worldsmegraphs.org/contexts/base.jsonld
```

## Adding New Domain Contexts

To add a new domain context:

1. **Create context file**: `new-domain.jsonld`
2. **Include base context**: Always extend `base.jsonld`
3. **Add domain ontologies**: Include relevant standard ontologies
4. **Define custom terms**: Add domain-specific vocabulary
5. **Document usage**: Update this README
6. **Test validation**: Ensure JSON-LD validity

**Template**:
```json
{
  "@context": [
    "base.jsonld",
    {
      "domain-prefix": "https://domain-ontology.org/",
      "customTerm": {
        "@id": "wsmg-domain:customTerm",
        "@type": "@id"
      }
    }
  ]
}
```

## Validation

Validate context files using:

```bash
# JSON-LD validation
jsonld validate context-file.jsonld

# Or use online playground
# https://json-ld.org/playground/
```

## Standard Ontologies Reference

| Ontology | Prefix | Namespace | Used In |
|----------|--------|-----------|---------|
| Schema.org | schema | https://schema.org/ | base |
| SKOS | skos | http://www.w3.org/2004/02/skos/core# | base |
| Dublin Core | dc | http://purl.org/dc/terms/ | base |
| PROV-O | prov | http://www.w3.org/ns/prov# | base |
| OWL | owl | http://www.w3.org/2002/07/owl# | base |
| SNOMED CT | snomed | http://snomed.info/id/ | medicine |
| MeSH | mesh | http://id.nlm.nih.gov/mesh/ | medicine |
| ICD-11 | icd11 | http://id.who.int/icd/entity/ | medicine |
| FIBO | fibo | https://spec.edmcouncil.org/fibo/ontology/ | economics |
| QUDT | qudt | http://qudt.org/schema/qudt/ | science |
| ChEBI | chebi | http://purl.obolibrary.org/obo/CHEBI_ | science |

## Versioning

Context files follow semantic versioning:
- Major version: Breaking changes to vocabulary
- Minor version: New terms added (backward compatible)
- Patch version: Documentation or minor corrections

Current version: **1.0.0** (2025-12-27)

## Related Documentation

- [Ontology Integration Specification](../../.project/research/ontology-integration-specification.md)
- [Knowledge Format v2](../../.project/knowledge-format-v2.md)
- [AKU Schema](../../.project/aku-schema.json)

## Maintenance

**Owner**: @ontology, @semantic-harmonization  
**Review Schedule**: Quarterly  
**Last Updated**: 2025-12-27  
**Next Review**: 2026-03-27
