# Comprehensive Ontology Integration Specification for WorldSMEGraphs

**Version**: 1.0  
**Date**: 2025-12-27  
**Status**: Technical Specification  
**Authors**: @ontology, @semantic-harmonization, @standards

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Design Principles](#design-principles)
3. [Ontology Architecture](#ontology-architecture)
4. [JSON-LD Context Structure](#json-ld-context-structure)
5. [SKOS Integration](#skos-integration)
6. [Domain-Specific Ontologies](#domain-specific-ontologies)
7. [Cross-Domain Linking](#cross-domain-linking)
8. [Dynamic Domain Discovery](#dynamic-domain-discovery)
9. [Concrete Examples](#concrete-examples)
10. [Migration Strategy](#migration-strategy)
11. [Validation Requirements](#validation-requirements)
12. [Implementation Roadmap](#implementation-roadmap)

---

## Executive Summary

### Purpose
This specification defines a comprehensive ontology integration system for WorldSMEGraphs that:
- Enables semantic interoperability across all knowledge domains
- Links to established ontology standards (SKOS, SNOMED CT, FIBO, etc.)
- Supports dynamic discovery and integration of new subject domains
- Maintains backward compatibility with existing AKU format
- Provides clear migration path from current structure

### Key Features
1. **Multi-Ontology Support**: Integrates Schema.org, SKOS, SNOMED CT, FIBO, DBpedia, and extensible for new ontologies
2. **Flexible Relationships**: SKOS-based concept relationships with domain-specific extensions
3. **External Linking**: Standard mechanisms for linking to external knowledge bases
4. **Domain Agnostic**: Works for medicine, economics, science, and unanticipated domains
5. **Annotation System**: Comprehensive cross-referencing and provenance tracking

### Research Foundation
This specification builds on:
- PR #11 ontology research findings
- `.project/research/ontology-and-numbering-analysis.md`
- Current AKU format v2.0 specification
- W3C Semantic Web standards (RDF, OWL, SKOS, JSON-LD)

---

## Design Principles

### 1. Standards-First Approach
**Principle**: Use established W3C and industry standards before creating custom solutions.

**Rationale**: 
- Ensures interoperability with external systems
- Leverages existing tools and validators
- Reduces reinvention and maintenance burden
- Enables semantic web integration

**Standards Adopted**:
- **JSON-LD**: For structured data with semantic context
- **SKOS**: For concept relationships and taxonomies
- **RDF/RDFS**: For basic resource description
- **OWL**: For formal ontology axioms (when needed)
- **Schema.org**: For general-purpose vocabulary
- **Dublin Core**: For metadata elements

### 2. Progressive Enhancement
**Principle**: Start simple, add complexity only where needed.

**Levels of Semantic Richness**:
1. **Basic**: Schema.org types + simple relationships
2. **Enhanced**: SKOS concept relationships + domain paths
3. **Advanced**: Domain ontology alignment (SNOMED, FIBO)
4. **Expert**: Formal axioms, inference rules, constraints

**Implementation**: Each AKU can exist at any level; upgrade as needed.

### 3. Domain Flexibility
**Principle**: System must work for known and unknown domains.

**Approach**:
- Core vocabulary is domain-agnostic
- Domain-specific terms added via extensible namespaces
- Auto-discovery of domain-specific ontologies
- Fallback to general-purpose ontologies

### 4. Human-AI Collaboration
**Principle**: Design for both machine processing and human comprehension.

**Implementation**:
- JSON-LD provides both: compact for humans, expanded for machines
- Multiple serialization formats (JSON-LD, Turtle, RDF/XML)
- Human-readable labels alongside URIs
- Clear documentation and examples

---

## Ontology Architecture

### Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Upper Ontology (Foundational Concepts)       │
│  - BFO (Basic Formal Ontology) for scientific domains  │
│  - DOLCE for general knowledge                          │
│  - Schema.org Thing as root                             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Layer 2: Mid-Level Ontologies (Cross-Domain)          │
│  - SKOS for concept organization                        │
│  - Dublin Core for metadata                             │
│  - FOAF for provenance and attribution                  │
│  - PROV-O for provenance tracking                       │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Layer 3: Domain-Specific Ontologies                   │
│  - Medical: SNOMED CT, MeSH, ICD-11                    │
│  - Economics: FIBO, DBpedia Economics                   │
│  - Science: ChEBI, UniProt, NASA SWEET                  │
│  - Custom: WorldSMEGraphs domain extensions             │
└─────────────────────────────────────────────────────────┘
```

### Namespace Registry

All ontologies are registered with standard prefixes:

```json
{
  "prefixes": {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "https://schema.org/",
    "dc": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "prov": "http://www.w3.org/ns/prov#",
    
    "snomed": "http://snomed.info/id/",
    "mesh": "http://id.nlm.nih.gov/mesh/",
    "icd11": "http://id.who.int/icd/entity/",
    "fibo": "https://spec.edmcouncil.org/fibo/ontology/",
    "dbpedia": "http://dbpedia.org/resource/",
    "dbpedia-owl": "http://dbpedia.org/ontology/",
    
    "wsmg": "https://worldsmegraphs.org/vocab/",
    "wsmg-med": "https://worldsmegraphs.org/vocab/medicine/",
    "wsmg-econ": "https://worldsmegraphs.org/vocab/economics/",
    "wsmg-sci": "https://worldsmegraphs.org/vocab/science/"
  }
}
```

### Ontology Selection Matrix

| Domain | Primary Ontology | Secondary | Tertiary |
|--------|------------------|-----------|----------|
| **Medicine** | SNOMED CT | MeSH | ICD-11 |
| **Economics** | FIBO | DBpedia Economics | Schema.org |
| **Biology** | UniProt | GO | ChEBI |
| **Chemistry** | ChEBI | PubChem | - |
| **Physics** | NASA SWEET | DBpedia | - |
| **Mathematics** | DBpedia Math | Schema.org | - |
| **General** | Schema.org | SKOS | Dublin Core |

---

## JSON-LD Context Structure

### Context Hierarchy

WorldSMEGraphs uses a **layered context** approach:

1. **Base Context**: Core Schema.org + SKOS
2. **Domain Context**: Domain-specific ontologies
3. **Local Context**: AKU-specific terms

### Base Context Definition

Create: `/domain/_contexts/base.jsonld`

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dc": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "wsmg": "https://worldsmegraphs.org/vocab/",
    
    "broader": {"@id": "skos:broader", "@type": "@id"},
    "narrower": {"@id": "skos:narrower", "@type": "@id"},
    "related": {"@id": "skos:related", "@type": "@id"},
    "exactMatch": {"@id": "skos:exactMatch", "@type": "@id"},
    "closeMatch": {"@id": "skos:closeMatch", "@type": "@id"},
    "relatedMatch": {"@id": "skos:relatedMatch", "@type": "@id"},
    "broadMatch": {"@id": "skos:broadMatch", "@type": "@id"},
    "narrowMatch": {"@id": "skos:narrowMatch", "@type": "@id"},
    
    "prefLabel": {"@id": "skos:prefLabel"},
    "altLabel": {"@id": "skos:altLabel"},
    "hiddenLabel": {"@id": "skos:hiddenLabel"},
    "definition": {"@id": "skos:definition"},
    "notation": {"@id": "skos:notation"},
    
    "sameAs": {"@id": "owl:sameAs", "@type": "@id"},
    "equivalentClass": {"@id": "owl:equivalentClass", "@type": "@id"},
    "equivalentProperty": {"@id": "owl:equivalentProperty", "@type": "@id"},
    
    "creator": {"@id": "dc:creator"},
    "created": {"@id": "dc:created", "@type": "http://www.w3.org/2001/XMLSchema#dateTime"},
    "modified": {"@id": "dc:modified", "@type": "http://www.w3.org/2001/XMLSchema#dateTime"},
    "source": {"@id": "dc:source", "@type": "@id"},
    
    "wasGeneratedBy": {"@id": "prov:wasGeneratedBy", "@type": "@id"},
    "wasDerivedFrom": {"@id": "prov:wasDerivedFrom", "@type": "@id"},
    "wasAttributedTo": {"@id": "prov:wasAttributedTo", "@type": "@id"}
  }
}
```

### Domain-Specific Contexts

#### Medical Context

Create: `/domain/_contexts/medicine.jsonld`

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    {
      "snomed": "http://snomed.info/id/",
      "mesh": "http://id.nlm.nih.gov/mesh/",
      "icd11": "http://id.who.int/icd/entity/",
      "umls": "http://linkedlifedata.com/resource/umls/id/",
      "rxnorm": "http://purl.bioontology.org/ontology/RXNORM/",
      
      "medicalCode": {"@id": "schema:medicalCode"},
      "codingSystem": {"@id": "schema:codingSystem"},
      "medicalEntity": {"@id": "schema:MedicalEntity", "@type": "@id"},
      "medicalCondition": {"@id": "schema:MedicalCondition", "@type": "@id"},
      "medicalProcedure": {"@id": "schema:MedicalProcedure", "@type": "@id"},
      "drug": {"@id": "schema:Drug", "@type": "@id"},
      
      "anatomicalStructure": {"@id": "schema:anatomicalStructure", "@type": "@id"},
      "associatedAnatomy": {"@id": "schema:associatedAnatomy", "@type": "@id"},
      "bodyLocation": {"@id": "schema:bodyLocation"},
      
      "snomedConcept": {"@id": "snomed:", "@type": "@id"},
      "meshHeading": {"@id": "mesh:", "@type": "@id"},
      "icd11Code": {"@id": "icd11:", "@type": "@id"}
    }
  ]
}
```

#### Economics/Finance Context

Create: `/domain/_contexts/economics.jsonld`

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    {
      "fibo": "https://spec.edmcouncil.org/fibo/ontology/",
      "fibo-fnd": "https://spec.edmcouncil.org/fibo/ontology/FND/",
      "fibo-be": "https://spec.edmcouncil.org/fibo/ontology/BE/",
      "fibo-fbc": "https://spec.edmcouncil.org/fibo/ontology/FBC/",
      "dbpedia-econ": "http://dbpedia.org/resource/Category:Economics/",
      
      "financialProduct": {"@id": "fibo-fbc:FinancialProduct", "@type": "@id"},
      "monetaryAmount": {"@id": "schema:MonetaryAmount"},
      "currency": {"@id": "schema:currency"},
      "price": {"@id": "schema:price"},
      "value": {"@id": "schema:value"},
      
      "interestRate": {"@id": "fibo:hasInterestRate"},
      "discountRate": {"@id": "wsmg-econ:discountRate"},
      "returnOnInvestment": {"@id": "wsmg-econ:returnOnInvestment"},
      "netPresentValue": {"@id": "wsmg-econ:netPresentValue"},
      
      "fiboEntity": {"@id": "fibo:", "@type": "@id"}
    }
  ]
}
```

#### Science Context

Create: `/domain/_contexts/science.jsonld`

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    {
      "qudt": "http://qudt.org/schema/qudt/",
      "unit": "http://qudt.org/vocab/unit/",
      "dbpedia-sci": "http://dbpedia.org/resource/Category:Science/",
      "chebi": "http://purl.obolibrary.org/obo/CHEBI_",
      "go": "http://purl.obolibrary.org/obo/GO_",
      
      "quantity": {"@id": "qudt:Quantity"},
      "unit": {"@id": "qudt:unit", "@type": "@id"},
      "value": {"@id": "qudt:value"},
      "quantityKind": {"@id": "qudt:quantityKind", "@type": "@id"},
      
      "formula": {"@id": "wsmg-sci:formula"},
      "equation": {"@id": "wsmg-sci:equation"},
      "variable": {"@id": "wsmg-sci:variable"},
      "constant": {"@id": "wsmg-sci:constant"}
    }
  ]
}
```

### Context Loading Strategy

AKUs reference contexts in order of specificity:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld",
    {
      "customTerm": "https://worldsmegraphs.org/vocab/custom#term"
    }
  ]
}
```

**Processing Order**:
1. Load base context (Schema.org + SKOS)
2. Load domain context (domain-specific ontologies)
3. Apply local context (AKU-specific overrides)

**Conflict Resolution**: Later contexts override earlier ones.

---

## SKOS Integration

### SKOS Vocabulary Mapping

SKOS provides standardized relationship vocabulary:

| SKOS Property | Usage in WorldSMEGraphs | Example |
|---------------|-------------------------|---------|
| `skos:broader` | More general concept | PV → Financial Concept |
| `skos:narrower` | More specific concept | NPV → PV |
| `skos:related` | Associated concept | NPV ↔ IRR |
| `skos:exactMatch` | Same concept, different ontology | WSMG concept = FIBO concept |
| `skos:closeMatch` | Similar concept | WSMG ≈ DBpedia |
| `skos:prefLabel` | Preferred term | "Net Present Value" |
| `skos:altLabel` | Alternative term | "NPV", "Present Worth" |
| `skos:definition` | Formal definition | "PV is..." |
| `skos:notation` | Code/identifier | "NPV-001" |

### Relationship Vocabulary Enhancement

**Current relationships** in AKUs:
- `prerequisites`
- `enables`
- `related_to`
- `inverse_of`

**Enhanced with SKOS**:

```json
{
  "relationships": {
    "hierarchical": {
      "broader": ["wsmg-econ:financial-concept", "wsmg-econ:valuation-method"],
      "narrower": ["wsmg-econ:npv-calculation", "wsmg-econ:npv-interpretation"],
      "broaderTransitive": ["wsmg-econ:economics"],
      "narrowerTransitive": ["wsmg-econ:npv-sensitivity-analysis"]
    },
    "associative": {
      "related": ["wsmg-econ:irr", "wsmg-econ:payback-period"],
      "relatedMatch": ["fibo:NetPresentValue", "dbpedia:Net_present_value"]
    },
    "pedagogical": {
      "prerequisites": ["wsmg-econ:time-value-money", "wsmg-econ:discount-rate"],
      "enables": ["wsmg-econ:capital-budgeting", "wsmg-econ:project-evaluation"],
      "inverse": "wsmg-econ:future-value"
    },
    "logical": {
      "isPartOf": ["wsmg-econ:dcf-analysis"],
      "hasPart": ["wsmg-econ:cash-flow-projection", "wsmg-econ:discounting"],
      "requires": ["wsmg-econ:discount-rate-determination"]
    }
  }
}
```

### Concept Scheme Definition

Define WorldSMEGraphs as a SKOS Concept Scheme:

```json
{
  "@context": "https://worldsmegraphs.org/contexts/base.jsonld",
  "@id": "wsmg:ConceptScheme",
  "@type": "skos:ConceptScheme",
  "dc:title": {
    "@language": "en",
    "@value": "WorldSMEGraphs Knowledge Organization System"
  },
  "dc:description": "Comprehensive knowledge representation system for subject matter expertise",
  "dc:creator": "WorldSMEGraphs Project",
  "dc:created": "2025-12-27",
  "dc:modified": "2025-12-27",
  "skos:hasTopConcept": [
    "wsmg:Medicine",
    "wsmg:Economics",
    "wsmg:Science",
    "wsmg:Technology",
    "wsmg:Humanities"
  ]
}
```

---

## Domain-Specific Ontologies

### Medical Domain Integration

#### SNOMED CT Integration

**Mapping Strategy**:
- Identify SNOMED CT concept ID for medical entities
- Use `skos:exactMatch` for precise alignments
- Use `skos:closeMatch` for approximate alignments

**Example - Type 2 Endoleak**:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld"
  ],
  "@id": "wsmg-med:type2-endoleak",
  "@type": ["schema:MedicalCondition", "skos:Concept"],
  
  "skos:prefLabel": {
    "@language": "en",
    "@value": "Type 2 Endoleak"
  },
  "skos:altLabel": [
    "Type II Endoleak",
    "Retrograde Flow Endoleak"
  ],
  "skos:definition": "Persistent flow in the aneurysm sac due to retrograde blood flow from collateral vessels",
  
  "skos:exactMatch": "snomed:449567000",
  "skos:closeMatch": "mesh:D000078862",
  "skos:relatedMatch": "icd11:BD50",
  
  "skos:broader": "wsmg-med:endoleak",
  "skos:narrower": [
    "wsmg-med:type2a-endoleak-lumbar",
    "wsmg-med:type2b-endoleak-ima"
  ],
  "skos:related": [
    "wsmg-med:evar-procedure",
    "wsmg-med:aortic-aneurysm"
  ],
  
  "schema:medicalCode": [
    {
      "@type": "MedicalCode",
      "schema:codeValue": "449567000",
      "schema:codingSystem": "SNOMED CT"
    },
    {
      "@type": "MedicalCode",
      "schema:codeValue": "D000078862",
      "schema:codingSystem": "MeSH"
    }
  ],
  
  "schema:associatedAnatomy": {
    "@id": "snomed:15825003",
    "schema:name": "Aorta"
  }
}
```

#### MeSH Integration

**Usage**: Primarily for literature references and research context

```json
{
  "provenance": {
    "sources": [
      {
        "@type": "ScholarlyArticle",
        "dc:title": "Management of Type 2 Endoleaks",
        "schema:about": [
          {
            "@id": "mesh:D000078862",
            "mesh:prefLabel": "Endoleak"
          },
          {
            "@id": "mesh:D057510",
            "mesh:prefLabel": "Endovascular Procedures"
          }
        ]
      }
    ]
  }
}
```

### Economics/Finance Domain Integration

#### FIBO Integration

**Example - Net Present Value**:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  "@id": "wsmg-econ:net-present-value",
  "@type": ["skos:Concept", "wsmg-econ:ValuationMethod"],
  
  "skos:prefLabel": {
    "@language": "en",
    "@value": "Net Present Value"
  },
  "skos:altLabel": ["NPV", "Present Worth", "Net Present Worth"],
  "skos:definition": "Sum of present values of incoming and outgoing cash flows over a period of time",
  
  "skos:exactMatch": "fibo-fnd:NetPresentValue",
  "skos:closeMatch": [
    "dbpedia:Net_present_value",
    "http://www.wikidata.org/entity/Q338801"
  ],
  
  "skos:broader": [
    "wsmg-econ:discounted-cash-flow",
    "wsmg-econ:valuation-method"
  ],
  "skos:narrower": [
    "wsmg-econ:npv-calculation",
    "wsmg-econ:npv-rule"
  ],
  "skos:related": [
    "wsmg-econ:internal-rate-return",
    "wsmg-econ:profitability-index"
  ],
  
  "wsmg:formula": {
    "@type": "MathematicalExpression",
    "latex": "NPV = \\sum_{t=0}^{T} \\frac{C_t}{(1+r)^t}",
    "variables": [
      {
        "symbol": "C_t",
        "definition": "Cash flow at time t",
        "unit": "currency"
      },
      {
        "symbol": "r",
        "definition": "Discount rate",
        "unit": "percentage"
      },
      {
        "symbol": "T",
        "definition": "Number of time periods",
        "unit": "time"
      }
    ]
  }
}
```

### Science Domain Integration

#### Physics Example with QUDT Units

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/science.jsonld"
  ],
  "@id": "wsmg-sci:newtons-second-law",
  "@type": ["skos:Concept", "wsmg-sci:PhysicalLaw"],
  
  "skos:prefLabel": "Newton's Second Law of Motion",
  "skos:altLabel": ["F=ma", "Law of Acceleration"],
  "skos:definition": "The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass",
  
  "skos:closeMatch": "dbpedia:Newton's_laws_of_motion#Second_law",
  
  "wsmg:formula": {
    "@type": "PhysicalEquation",
    "latex": "\\vec{F} = m\\vec{a}",
    "variables": [
      {
        "symbol": "F",
        "definition": "Net force",
        "quantityKind": "qudt:Force",
        "unit": "unit:N"
      },
      {
        "symbol": "m",
        "definition": "Mass",
        "quantityKind": "qudt:Mass",
        "unit": "unit:KG"
      },
      {
        "symbol": "a",
        "definition": "Acceleration",
        "quantityKind": "qudt:Acceleration",
        "unit": "unit:M-PER-SEC2"
      }
    ]
  }
}
```

---

## Cross-Domain Linking

### Linking Patterns

#### 1. Exact Equivalence (`owl:sameAs`)

**Use when**: Two URIs refer to the exact same real-world entity

```json
{
  "@id": "wsmg-med:diabetes-mellitus",
  "owl:sameAs": [
    "snomed:73211009",
    "dbpedia:Diabetes_mellitus"
  ]
}
```

#### 2. Concept Matching (`skos:exactMatch`, `skos:closeMatch`)

**Use when**: Concepts are equivalent or similar across ontologies

```json
{
  "@id": "wsmg-econ:npv",
  "skos:exactMatch": "fibo:NetPresentValue",
  "skos:closeMatch": [
    "dbpedia:Net_present_value",
    "http://www.wikidata.org/entity/Q338801"
  ]
}
```

#### 3. Broad/Narrow Matching (`skos:broadMatch`, `skos:narrowMatch`)

**Use when**: Hierarchical relationships exist across ontologies

```json
{
  "@id": "wsmg-med:type2-endoleak",
  "skos:broadMatch": "snomed:233985008",
  "skos:narrowMatch": [
    "wsmg-med:type2a-lumbar",
    "wsmg-med:type2b-ima"
  ]
}
```

#### 4. Related Matching (`skos:relatedMatch`)

**Use when**: Concepts are associated but not hierarchically related

```json
{
  "@id": "wsmg-econ:npv",
  "skos:relatedMatch": [
    "fibo:InternalRateOfReturn",
    "fibo:PaybackPeriod"
  ]
}
```

### Cross-Domain Dependencies

When concepts from different domains relate:

```json
{
  "@id": "wsmg-med:cost-effectiveness-analysis",
  "@type": ["skos:Concept", "schema:MedicalEntity"],
  
  "skos:broader": [
    "wsmg-med:health-economics",
    "wsmg-econ:economic-evaluation"
  ],
  
  "wsmg:requiresConcepts": [
    {
      "@id": "wsmg-econ:npv",
      "domain": "economics",
      "rationale": "Required for calculating present value of health outcomes"
    },
    {
      "@id": "wsmg-med:quality-adjusted-life-years",
      "domain": "medicine",
      "rationale": "Health outcome measure"
    }
  ],
  
  "wsmg:bridges": ["medicine", "economics"]
}
```

---

## Dynamic Domain Discovery

### Auto-Discovery System

For unanticipated domains, implement auto-discovery:

#### Step 1: Domain Detection

```python
def detect_domain(aku_data: dict) -> DomainInfo:
    """
    Detect domain from AKU content using:
    1. domain_path classification
    2. Content analysis (keywords, entities)
    3. External ontology lookup
    """
    domain_path = aku_data.get("classification", {}).get("domain_path", "")
    top_level = domain_path.split("/")[0] if domain_path else "unknown"
    
    # Check if domain is known
    if top_level in KNOWN_DOMAINS:
        return KNOWN_DOMAINS[top_level]
    
    # Auto-discover
    return auto_discover_domain(aku_data)

def auto_discover_domain(aku_data: dict) -> DomainInfo:
    """
    Auto-discover domain using:
    1. LOV (Linked Open Vocabularies) API
    2. BioPortal API (for life sciences)
    3. DBpedia Spotlight (for general knowledge)
    """
    text = extract_text(aku_data)
    
    # Query LOV API
    lov_result = query_lov(text)
    if lov_result:
        return create_domain_info(lov_result)
    
    # Query BioPortal
    bioportal_result = query_bioportal(text)
    if bioportal_result:
        return create_domain_info(bioportal_result)
    
    # Fallback to DBpedia
    dbpedia_result = query_dbpedia_spotlight(text)
    return create_domain_info(dbpedia_result)
```

#### Step 2: Ontology Selection

```python
DOMAIN_ONTOLOGY_MAP = {
    "medicine": ["snomed", "mesh", "icd11", "umls"],
    "economics": ["fibo", "dbpedia-econ"],
    "biology": ["uniprot", "go", "chebi"],
    "chemistry": ["chebi", "pubchem"],
    "physics": ["sweet", "dbpedia"],
    "mathematics": ["dbpedia-math", "mathworld"],
    # Auto-discover for unknown domains
    "unknown": ["schema.org", "dbpedia", "skos"]
}

def select_ontologies(domain: str) -> List[str]:
    """Select appropriate ontologies for domain."""
    return DOMAIN_ONTOLOGY_MAP.get(domain, DOMAIN_ONTOLOGY_MAP["unknown"])
```

#### Step 3: Context Generation

```python
def generate_context(domain: str, ontologies: List[str]) -> dict:
    """Generate JSON-LD context for domain."""
    context = {
        "@context": [
            "https://worldsmegraphs.org/contexts/base.jsonld"
        ]
    }
    
    # Add domain-specific context if exists
    domain_context_url = f"https://worldsmegraphs.org/contexts/{domain}.jsonld"
    if context_exists(domain_context_url):
        context["@context"].append(domain_context_url)
    
    # Add ontology namespaces
    ontology_ns = {}
    for ont in ontologies:
        ontology_ns[ont] = ONTOLOGY_NAMESPACES[ont]
    
    context["@context"].append(ontology_ns)
    
    return context
```

### Domain Registry

Maintain a registry of discovered domains:

```json
{
  "@context": "https://worldsmegraphs.org/contexts/base.jsonld",
  "@id": "wsmg:DomainRegistry",
  "@type": "skos:ConceptScheme",
  
  "domains": [
    {
      "@id": "wsmg:medicine",
      "prefLabel": "Medicine",
      "status": "established",
      "ontologies": ["snomed", "mesh", "icd11"],
      "contextURL": "https://worldsmegraphs.org/contexts/medicine.jsonld",
      "akuCount": 15000
    },
    {
      "@id": "wsmg:economics",
      "prefLabel": "Economics",
      "status": "established",
      "ontologies": ["fibo", "dbpedia-econ"],
      "contextURL": "https://worldsmegraphs.org/contexts/economics.jsonld",
      "akuCount": 8000
    },
    {
      "@id": "wsmg:marine-biology",
      "prefLabel": "Marine Biology",
      "status": "emerging",
      "discoveredDate": "2025-12-15",
      "ontologies": ["uniprot", "go", "envo"],
      "contextURL": "https://worldsmegraphs.org/contexts/marine-biology.jsonld",
      "akuCount": 50
    }
  ]
}
```

---

## Annotation and Cross-Referencing System

### Provenance Tracking with PROV-O

Track full lineage of knowledge:

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    {
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "wsmg-econ:npv-aku-001",
  "@type": ["EducationalResource", "prov:Entity"],
  
  "prov:wasGeneratedBy": {
    "@id": "wsmg:extraction-activity-12345",
    "@type": "prov:Activity",
    "prov:startedAtTime": "2025-12-27T10:00:00Z",
    "prov:endedAtTime": "2025-12-27T10:15:00Z",
    "prov:wasAssociatedWith": {
      "@id": "wsmg-agent:paper-miner",
      "@type": "prov:Agent",
      "prov:actedOnBehalfOf": "wsmg-agent:coordinator"
    },
    "prov:used": {
      "@id": "isbn:978-0073382333",
      "@type": "schema:Book",
      "schema:name": "Corporate Finance",
      "schema:author": ["Brealey", "Myers", "Allen"]
    }
  },
  
  "prov:wasDerivedFrom": [
    {
      "@id": "isbn:978-0073382333#page-18",
      "@type": "schema:Chapter",
      "schema:pagination": "18-22"
    }
  ],
  
  "prov:wasAttributedTo": [
    {
      "@id": "wsmg-agent:finance-expert",
      "@type": "prov:Agent",
      "prov:actedOnBehalfOf": "wsmg:domain-expert-team"
    }
  ],
  
  "prov:wasRevisionOf": {
    "@id": "wsmg-econ:npv-aku-001-v1",
    "dc:modified": "2025-12-20"
  }
}
```

### Citation and References

Use Schema.org citation properties enhanced with Dublin Core:

```json
{
  "provenance": {
    "sources": [
      {
        "@type": "ScholarlyArticle",
        "@id": "doi:10.1016/j.jfineco.2020.01.001",
        "schema:name": "Modern Applications of NPV in Capital Budgeting",
        "schema:author": [
          {"@type": "Person", "schema:name": "Jane Smith"},
          {"@type": "Person", "schema:name": "John Doe"}
        ],
        "schema:datePublished": "2020",
        "schema:isPartOf": {
          "@type": "Periodical",
          "schema:name": "Journal of Financial Economics",
          "schema:volumeNumber": "135",
          "schema:issueNumber": "2"
        },
        "dc:bibliographicCitation": "Smith, J., & Doe, J. (2020). Modern Applications of NPV in Capital Budgeting. Journal of Financial Economics, 135(2), 300-320."
      },
      {
        "@type": "Book",
        "@id": "isbn:978-0073382333",
        "schema:name": "Principles of Corporate Finance",
        "schema:author": ["Richard Brealey", "Stewart Myers", "Franklin Allen"],
        "schema:datePublished": "2019",
        "schema:publisher": "McGraw-Hill Education",
        "schema:bookEdition": "13th",
        "dc:bibliographicCitation": "Brealey, R., Myers, S., & Allen, F. (2019). Principles of Corporate Finance (13th ed.). McGraw-Hill Education."
      }
    ]
  }
}
```

### Cross-References Between AKUs

```json
{
  "relationships": {
    "pedagogical": {
      "prerequisites": [
        {
          "@id": "wsmg-econ:time-value-money",
          "@type": "EducationalResource",
          "relationship": "requires-understanding-of",
          "strength": "essential"
        },
        {
          "@id": "wsmg-econ:discount-rate",
          "@type": "EducationalResource",
          "relationship": "requires-knowledge-of",
          "strength": "critical"
        }
      ],
      "enables": [
        {
          "@id": "wsmg-econ:capital-budgeting",
          "@type": "EducationalResource",
          "relationship": "enables-understanding-of",
          "strength": "foundational"
        }
      ]
    },
    "semantic": {
      "skos:broader": "wsmg-econ:discounted-cash-flow",
      "skos:narrower": ["wsmg-econ:npv-calculation", "wsmg-econ:npv-interpretation"],
      "skos:related": ["wsmg-econ:irr", "wsmg-econ:payback-period"]
    },
    "external": {
      "skos:exactMatch": "fibo:NetPresentValue",
      "skos:closeMatch": [
        "dbpedia:Net_present_value",
        "wikidata:Q338801"
      ]
    }
  }
}
```

### Annotation Vocabulary

Define custom annotation properties:

```json
{
  "@context": "https://worldsmegraphs.org/contexts/base.jsonld",
  "@id": "wsmg:AnnotationVocabulary",
  "@type": "owl:Ontology",
  
  "properties": [
    {
      "@id": "wsmg:confidence",
      "@type": "owl:DatatypeProperty",
      "rdfs:label": "confidence level",
      "rdfs:comment": "Confidence score for AKU content (0.0-1.0)",
      "rdfs:range": "xsd:decimal"
    },
    {
      "@id": "wsmg:validationStatus",
      "@type": "owl:DatatypeProperty",
      "rdfs:label": "validation status",
      "rdfs:comment": "Status of AKU validation",
      "rdfs:range": {
        "@type": "rdfs:Datatype",
        "owl:oneOf": ["draft", "validated", "peer-reviewed", "published"]
      }
    },
    {
      "@id": "wsmg:difficulty",
      "@type": "owl:DatatypeProperty",
      "rdfs:label": "difficulty level",
      "rdfs:comment": "Cognitive difficulty level",
      "rdfs:range": {
        "@type": "rdfs:Datatype",
        "owl:oneOf": ["beginner", "intermediate", "advanced", "expert"]
      }
    },
    {
      "@id": "wsmg:importance",
      "@type": "owl:DatatypeProperty",
      "rdfs:label": "importance level",
      "rdfs:comment": "Importance in domain knowledge",
      "rdfs:range": {
        "@type": "rdfs:Datatype",
        "owl:oneOf": ["foundational", "core", "advanced", "specialized"]
      }
    }
  ]
}
```

---

## Concrete Examples

### Example 1: Medical Domain - Type 2 Endoleak (Complete AKU)

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld"
  ],
  "@id": "wsmg-med:type2-endoleak-def-001",
  "@type": ["schema:MedicalCondition", "EducationalResource", "skos:Concept"],
  
  "metadata": {
    "version": "2.0.0",
    "dc:created": "2025-12-27T10:00:00.000Z",
    "dc:modified": "2025-12-27T15:00:00.000Z",
    "dc:creator": ["wsmg-agent:medical-expert", "wsmg-agent:vascular-specialist"],
    "wsmg:confidence": 0.98,
    "wsmg:validationStatus": "peer-reviewed"
  },
  
  "classification": {
    "domain_path": "medicine/surgery/vascular/complications/endoleaks/type-2",
    "type": "definition",
    "wsmg:difficulty": "advanced",
    "wsmg:importance": "core"
  },
  
  "skos:prefLabel": {
    "@language": "en",
    "@value": "Type 2 Endoleak"
  },
  "skos:altLabel": ["Type II Endoleak", "Retrograde Flow Endoleak", "Branch Vessel Endoleak"],
  "skos:definition": "Persistent blood flow within aneurysm sac following EVAR, resulting from retrograde filling through patent aortic branch vessels (lumbar arteries, inferior mesenteric artery)",
  "skos:notation": "T2EL",
  
  "content": {
    "statement": {
      "text": "Type 2 endoleak is the most common complication following endovascular aneurysm repair (EVAR), characterized by retrograde blood flow into the aneurysm sac through patent branch vessels.",
      "formal": "T2EL := retrograde_flow(branch_vessels → aneurysm_sac) ∧ post_EVAR"
    },
    "explanation": {
      "intuition": "Imagine sealing a water balloon but leaving small tubes attached. Even though the main opening is sealed, water can still flow back through those tubes. That's similar to how Type 2 endoleaks work.",
      "clinical_significance": "Most Type 2 endoleaks are benign and self-limiting. However, persistent Type 2 endoleaks with sac expansion require intervention."
    }
  },
  
  "relationships": {
    "hierarchical": {
      "skos:broader": [
        "wsmg-med:endoleak",
        "wsmg-med:evar-complications"
      ],
      "skos:narrower": [
        "wsmg-med:type2a-lumbar-endoleak",
        "wsmg-med:type2b-ima-endoleak",
        "wsmg-med:complex-type2-endoleak"
      ]
    },
    "associative": {
      "skos:related": [
        "wsmg-med:evar-procedure",
        "wsmg-med:abdominal-aortic-aneurysm",
        "wsmg-med:endoleak-classification"
      ]
    },
    "pedagogical": {
      "prerequisites": [
        "wsmg-med:vascular-anatomy",
        "wsmg-med:evar-basics",
        "wsmg-med:aneurysm-pathophysiology"
      ],
      "enables": [
        "wsmg-med:endoleak-diagnosis",
        "wsmg-med:endoleak-management",
        "wsmg-med:post-evar-surveillance"
      ]
    },
    "external": {
      "owl:sameAs": [
        "snomed:449567000",
        "umls:C2828396"
      ],
      "skos:exactMatch": "snomed:449567000",
      "skos:closeMatch": [
        "mesh:D000078862",
        "icd11:BD50.2"
      ],
      "skos:relatedMatch": [
        "snomed:233985008",
        "dbpedia:Endoleak"
      ]
    }
  },
  
  "schema:medicalCode": [
    {
      "@type": "MedicalCode",
      "schema:codeValue": "449567000",
      "schema:codingSystem": "SNOMED CT",
      "schema:codingSystemVersion": "International Edition 2024"
    },
    {
      "@type": "MedicalCode",
      "schema:codeValue": "D000078862",
      "schema:codingSystem": "MeSH"
    }
  ],
  
  "schema:associatedAnatomy": [
    {
      "@id": "snomed:15825003",
      "schema:name": "Aorta",
      "skos:prefLabel": "Abdominal Aorta"
    },
    {
      "@id": "snomed:181347005",
      "schema:name": "Lumbar arteries"
    }
  ],
  
  "provenance": {
    "prov:wasGeneratedBy": {
      "@id": "wsmg:extraction-med-12345",
      "@type": "prov:Activity",
      "prov:startedAtTime": "2025-12-27T09:00:00Z",
      "prov:wasAssociatedWith": "wsmg-agent:medical-literature-miner"
    },
    "dc:source": [
      {
        "@type": "ScholarlyArticle",
        "@id": "doi:10.1016/j.jvs.2018.01.051",
        "schema:name": "Management of Type 2 Endoleaks After EVAR",
        "schema:author": ["White GH", "Yu W", "May J"]
      }
    ]
  },
  
  "pedagogical": {
    "target_audiences": ["vascular-surgery-residents", "interventional-radiologists"],
    "learning_objectives": [
      "Define Type 2 endoleak",
      "Identify anatomical sources",
      "Explain clinical significance",
      "Describe diagnostic approach"
    ],
    "estimated_time_minutes": 15
  }
}
```

### Example 2: Economics Domain - NPV (Complete AKU)

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  "@id": "wsmg-econ:npv-definition-001",
  "@type": ["EducationalResource", "skos:Concept", "wsmg-econ:FinancialConcept"],
  
  "metadata": {
    "version": "2.0.0",
    "dc:created": "2025-12-27T00:00:00.000Z",
    "dc:modified": "2025-12-27T15:00:00.000Z",
    "dc:creator": ["wsmg-agent:finance-expert", "wsmg-agent:economics-researcher"],
    "wsmg:confidence": 0.99,
    "wsmg:validationStatus": "validated"
  },
  
  "classification": {
    "domain_path": "economics/bwl/finance/valuation/npv",
    "type": "definition",
    "wsmg:difficulty": "intermediate",
    "wsmg:importance": "foundational"
  },
  
  "skos:prefLabel": {
    "@language": "en",
    "@value": "Net Present Value"
  },
  "skos:altLabel": ["NPV", "Present Worth", "Net Present Worth", "Nettogegenwartswert"],
  "skos:definition": "The difference between the present value of cash inflows and the present value of cash outflows over a period of time, used in capital budgeting to analyze the profitability of a projected investment or project",
  "skos:notation": "NPV",
  
  "content": {
    "statement": {
      "text": "Net Present Value (NPV) is the sum of the present values of incoming and outgoing cash flows over a period of time, discounted at a specified rate of return.",
      "formal": "NPV = Σ(t=0 to T) [C_t / (1+r)^t] where C_t is net cash flow at time t, r is discount rate, T is number of periods"
    },
    "explanation": {
      "intuition": "If a project costs $100,000 today and will generate $120,000 in one year, is it worthwhile? NPV answers this by calculating what those future cash flows are worth today.",
      "key_insight": "NPV > 0 means the investment adds value; NPV < 0 means it destroys value; NPV = 0 means breakeven."
    }
  },
  
  "relationships": {
    "hierarchical": {
      "skos:broader": [
        "wsmg-econ:discounted-cash-flow",
        "wsmg-econ:capital-budgeting-methods",
        "wsmg-econ:investment-valuation"
      ],
      "skos:narrower": [
        "wsmg-econ:npv-calculation",
        "wsmg-econ:npv-decision-rule",
        "wsmg-econ:npv-sensitivity-analysis"
      ]
    },
    "associative": {
      "skos:related": [
        "wsmg-econ:internal-rate-return",
        "wsmg-econ:payback-period",
        "wsmg-econ:profitability-index"
      ]
    },
    "pedagogical": {
      "prerequisites": [
        "wsmg-econ:time-value-money",
        "wsmg-econ:present-value",
        "wsmg-econ:discount-rate"
      ],
      "enables": [
        "wsmg-econ:capital-budgeting",
        "wsmg-econ:project-selection",
        "wsmg-econ:investment-appraisal"
      ]
    },
    "external": {
      "skos:exactMatch": "fibo-fnd:NetPresentValue",
      "skos:closeMatch": [
        "dbpedia:Net_present_value",
        "wikidata:Q338801"
      ]
    }
  },
  
  "representations": {
    "latex": "NPV = \\sum_{t=0}^{T} \\frac{C_t}{(1+r)^t}",
    "python": {
      "code": "def npv(rate, cash_flows):\n    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))",
      "test_cases": [
        {
          "input": {"rate": 0.10, "cash_flows": [-100, 50, 50, 50]},
          "expected": 24.34
        }
      ]
    }
  },
  
  "wsmg:formula": {
    "@type": "MathematicalExpression",
    "latex": "NPV = \\sum_{t=0}^{T} \\frac{C_t}{(1+r)^t}",
    "variables": [
      {
        "symbol": "C_t",
        "definition": "Net cash flow at time t",
        "unit": "currency",
        "skos:related": "wsmg-econ:cash-flow"
      },
      {
        "symbol": "r",
        "definition": "Discount rate (required rate of return)",
        "unit": "percentage",
        "skos:related": "wsmg-econ:discount-rate"
      },
      {
        "symbol": "T",
        "definition": "Number of time periods",
        "unit": "time_periods"
      }
    ]
  },
  
  "provenance": {
    "prov:wasDerivedFrom": [
      {
        "@type": "Book",
        "@id": "isbn:978-0073382333",
        "schema:name": "Principles of Corporate Finance",
        "schema:author": ["Brealey", "Myers", "Allen"],
        "schema:bookEdition": "13th",
        "schema:pagination": "18-25"
      }
    ],
    "dc:source": [
      {
        "@type": "ScholarlyArticle",
        "@id": "doi:10.1111/j.1540-6261.1972.tb00971.x",
        "schema:name": "Capital Budgeting and the Capital Asset Pricing Model",
        "schema:author": ["Rubinstein ME"]
      }
    ]
  },
  
  "pedagogical": {
    "target_audiences": ["undergraduate-finance", "mba-students", "finance-practitioners"],
    "learning_objectives": [
      "Calculate NPV given cash flows and discount rate",
      "Interpret NPV results for investment decisions",
      "Explain relationship between NPV and value creation"
    ],
    "estimated_time_minutes": 20,
    "common_errors": [
      "Using nominal vs real cash flows incorrectly",
      "Mismatching discount rate with cash flow type",
      "Forgetting initial investment (t=0) is typically negative"
    ]
  }
}
```

### Example 3: Science Domain - Newton's Second Law

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/science.jsonld"
  ],
  "@id": "wsmg-sci:newtons-second-law-001",
  "@type": ["EducationalResource", "skos:Concept", "wsmg-sci:PhysicalLaw"],
  
  "metadata": {
    "version": "2.0.0",
    "dc:created": "2025-12-27T00:00:00.000Z",
    "dc:modified": "2025-12-27T15:00:00.000Z",
    "dc:creator": ["wsmg-agent:physics-expert"],
    "wsmg:confidence": 1.0,
    "wsmg:validationStatus": "validated"
  },
  
  "classification": {
    "domain_path": "science/physics/mechanics/dynamics/force-laws",
    "type": "definition",
    "wsmg:difficulty": "intermediate",
    "wsmg:importance": "foundational"
  },
  
  "skos:prefLabel": "Newton's Second Law of Motion",
  "skos:altLabel": ["F=ma", "Law of Acceleration", "Second Law of Motion"],
  "skos:definition": "The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass",
  "skos:notation": "N2L",
  
  "content": {
    "statement": {
      "text": "The net force acting on an object is equal to the mass of the object multiplied by its acceleration.",
      "formal": "∑F = ma, where F is net force, m is mass, a is acceleration"
    },
    "explanation": {
      "intuition": "Pushing a shopping cart: the harder you push (more force), the faster it accelerates. A full cart (more mass) accelerates less than an empty one with the same push.",
      "key_insight": "This law quantifies how forces cause changes in motion and establishes the fundamental relationship between force, mass, and acceleration."
    }
  },
  
  "relationships": {
    "hierarchical": {
      "skos:broader": [
        "wsmg-sci:newtons-laws-motion",
        "wsmg-sci:classical-mechanics"
      ],
      "skos:narrower": [
        "wsmg-sci:linear-motion-f-equals-ma",
        "wsmg-sci:rotational-analog-tau-equals-i-alpha"
      ]
    },
    "associative": {
      "skos:related": [
        "wsmg-sci:newtons-first-law",
        "wsmg-sci:newtons-third-law",
        "wsmg-sci:momentum"
      ]
    },
    "pedagogical": {
      "prerequisites": [
        "wsmg-sci:force-concept",
        "wsmg-sci:mass-concept",
        "wsmg-sci:acceleration"
      ],
      "enables": [
        "wsmg-sci:dynamics-problems",
        "wsmg-sci:free-body-diagrams",
        "wsmg-sci:orbital-mechanics"
      ]
    },
    "external": {
      "skos:closeMatch": [
        "dbpedia:Newton's_laws_of_motion",
        "wikidata:Q11412"
      ]
    }
  },
  
  "wsmg:formula": {
    "@type": "PhysicalEquation",
    "latex": "\\sum \\vec{F} = m\\vec{a}",
    "variables": [
      {
        "symbol": "F",
        "definition": "Net force (vector sum of all forces)",
        "qudt:quantityKind": "qudt:Force",
        "qudt:unit": "unit:N",
        "si_unit": "newton (N = kg⋅m/s²)"
      },
      {
        "symbol": "m",
        "definition": "Mass of object",
        "qudt:quantityKind": "qudt:Mass",
        "qudt:unit": "unit:KG",
        "si_unit": "kilogram (kg)"
      },
      {
        "symbol": "a",
        "definition": "Acceleration of object",
        "qudt:quantityKind": "qudt:Acceleration",
        "qudt:unit": "unit:M-PER-SEC2",
        "si_unit": "meters per second squared (m/s²)"
      }
    ],
    "dimensional_analysis": "[M][L][T]⁻² = [M] × [L][T]⁻²"
  },
  
  "representations": {
    "latex": "\\sum \\vec{F} = m\\vec{a}",
    "python": {
      "code": "def force(mass, acceleration):\n    return mass * acceleration",
      "test_cases": [
        {"input": {"mass": 10, "acceleration": 2}, "expected": 20}
      ]
    }
  },
  
  "provenance": {
    "dc:source": [
      {
        "@type": "Book",
        "schema:name": "Philosophiæ Naturalis Principia Mathematica",
        "schema:author": "Isaac Newton",
        "schema:datePublished": "1687"
      }
    ]
  },
  
  "pedagogical": {
    "target_audiences": ["high-school-physics", "introductory-university"],
    "learning_objectives": [
      "State Newton's Second Law",
      "Calculate force given mass and acceleration",
      "Solve dynamics problems using F=ma"
    ],
    "estimated_time_minutes": 30
  }
}
```

### Example 4: Cross-Domain - Medical Cost-Effectiveness Analysis

```json
{
  "@context": [
    "https://worldsmegraphs.org/contexts/base.jsonld",
    "https://worldsmegraphs.org/contexts/medicine.jsonld",
    "https://worldsmegraphs.org/contexts/economics.jsonld"
  ],
  "@id": "wsmg-med:cost-effectiveness-analysis-001",
  "@type": ["EducationalResource", "skos:Concept", "schema:MedicalEntity"],
  
  "classification": {
    "domain_path": "medicine/health-economics/economic-evaluation",
    "type": "definition",
    "wsmg:difficulty": "advanced",
    "wsmg:importance": "core",
    "wsmg:crossDomain": ["medicine", "economics"]
  },
  
  "skos:prefLabel": "Cost-Effectiveness Analysis",
  "skos:altLabel": ["CEA", "Health Economic Evaluation"],
  "skos:definition": "Economic analysis comparing relative costs and outcomes (effects) of different courses of action in healthcare",
  
  "relationships": {
    "hierarchical": {
      "skos:broader": [
        "wsmg-med:health-economics",
        "wsmg-econ:economic-evaluation"
      ]
    },
    "cross_domain": {
      "wsmg:requiresConcepts": [
        {
          "@id": "wsmg-econ:npv",
          "domain": "economics",
          "usage": "Discounting future health costs and benefits"
        },
        {
          "@id": "wsmg-med:quality-adjusted-life-years",
          "domain": "medicine",
          "usage": "Measuring health outcomes"
        }
      ],
      "wsmg:integrates": ["medicine", "economics"]
    },
    "external": {
      "skos:closeMatch": [
        "mesh:D003362",
        "fibo:CostBenefitAnalysis"
      ]
    }
  },
  
  "wsmg:formula": {
    "@type": "MathematicalExpression",
    "latex": "ICER = \\frac{C_1 - C_0}{E_1 - E_0}",
    "variables": [
      {
        "symbol": "ICER",
        "definition": "Incremental Cost-Effectiveness Ratio",
        "domain": "health-economics"
      },
      {
        "symbol": "C_1, C_0",
        "definition": "Costs of intervention vs comparator",
        "uses_concept": "wsmg-econ:npv"
      },
      {
        "symbol": "E_1, E_0",
        "definition": "Effects of intervention vs comparator",
        "uses_concept": "wsmg-med:qaly"
      }
    ]
  }
}
```

---

## Migration Strategy

### Phase 1: Add Ontology Support (Weeks 1-2)

**Goal**: Introduce ontology features without breaking existing AKUs

**Actions**:
1. Create `/domain/_contexts/` directory with base and domain contexts
2. Update AKU schema to support `@context` arrays
3. Add optional `relationships.external` section for ontology mappings
4. No changes required to existing AKUs (backward compatible)

**Validation**:
- Existing AKUs still validate with old schema
- New AKUs can optionally use ontology features
- JSON-LD processor can expand both formats

**Example Migration Script**:
```python
def add_ontology_support(aku: dict) -> dict:
    """Add ontology support to existing AKU."""
    # Convert single context to array
    if "@context" in aku and isinstance(aku["@context"], str):
        domain = detect_domain(aku)
        aku["@context"] = [
            "https://worldsmegraphs.org/contexts/base.jsonld",
            f"https://worldsmegraphs.org/contexts/{domain}.jsonld"
        ]
    
    # Add SKOS relationships section (optional)
    if "relationships" in aku:
        aku["relationships"]["hierarchical"] = {
            "skos:broader": [],
            "skos:narrower": [],
            "skos:related": []
        }
    
    return aku
```

### Phase 2: External Linking (Weeks 3-4)

**Goal**: Link AKUs to external ontologies (SNOMED, FIBO, etc.)

**Actions**:
1. Identify mappable concepts in each domain
2. Use ontology lookup services (BioPortal, LOV, Wikidata SPARQL)
3. Add `skos:exactMatch`, `skos:closeMatch` to AKUs
4. Create domain-specific mapping guidelines

**Tools**:
- **BioPortal Annotator**: Auto-detect medical concepts → SNOMED/MeSH
- **LOV (Linked Open Vocabularies)**: Discover ontologies
- **Wikidata SPARQL**: Find Wikidata entities
- **FIBO Navigator**: Map financial concepts

**Example Mapping Process**:
```python
def find_ontology_mappings(aku: dict) -> List[str]:
    """Find external ontology matches for AKU concept."""
    concept_text = aku["content"]["statement"]["text"]
    domain = aku["classification"]["domain_path"].split("/")[0]
    
    mappings = []
    
    if domain == "medicine":
        # Query BioPortal
        snomed_id = bioportal_annotate(concept_text, ontology="SNOMEDCT")
        if snomed_id:
            mappings.append(f"snomed:{snomed_id}")
        
        mesh_id = bioportal_annotate(concept_text, ontology="MESH")
        if mesh_id:
            mappings.append(f"mesh:{mesh_id}")
    
    elif domain == "economics":
        # Query FIBO
        fibo_match = query_fibo_sparql(concept_text)
        if fibo_match:
            mappings.append(fibo_match)
    
    # Always try Wikidata
    wikidata_id = query_wikidata(concept_text)
    if wikidata_id:
        mappings.append(f"wikidata:{wikidata_id}")
    
    return mappings
```

### Phase 3: SKOS Relationships (Weeks 5-6)

**Goal**: Establish SKOS concept hierarchies across all AKUs

**Actions**:
1. Analyze existing `relationships.prerequisites` → map to `skos:broader`
2. Analyze `relationships.enables` → map to `skos:narrower`
3. Analyze `relationships.related_to` → map to `skos:related`
4. Build domain taxonomies
5. Validate transitivity and consistency

**Mapping Logic**:
```python
def convert_to_skos_relationships(old_relationships: dict) -> dict:
    """Convert legacy relationships to SKOS."""
    skos_rel = {
        "hierarchical": {},
        "associative": {}
    }
    
    # Prerequisites often indicate broader concepts
    # (you need to know X before learning Y, so X is broader)
    if "prerequisites" in old_relationships:
        skos_rel["hierarchical"]["skos:broader"] = old_relationships["prerequisites"]
    
    # Enables often indicates narrower concepts
    # (learning Y enables understanding Z, so Z is narrower)
    if "enables" in old_relationships:
        skos_rel["hierarchical"]["skos:narrower"] = old_relationships["enables"]
    
    # Related_to maps directly to skos:related
    if "related_to" in old_relationships:
        skos_rel["associative"]["skos:related"] = old_relationships["related_to"]
    
    return skos_rel
```

### Phase 4: Validation and Consistency (Weeks 7-8)

**Goal**: Ensure ontological consistency across entire knowledge base

**Actions**:
1. Implement ontology validator
2. Check for circular dependencies
3. Verify external URIs resolve
4. Validate SKOS constraints (e.g., broader/narrower symmetry)
5. Generate consistency reports

**Validation Checks**:
```python
def validate_ontology_consistency(aku: dict) -> List[str]:
    """Validate ontological consistency of AKU."""
    errors = []
    
    # Check 1: Broader/narrower symmetry
    if "skos:broader" in aku and "skos:narrower" in aku:
        broader = set(aku["skos:broader"])
        narrower = set(aku["skos:narrower"])
        if broader & narrower:
            errors.append("Concept cannot be both broader and narrower")
    
    # Check 2: No circular dependencies
    if has_circular_dependency(aku["@id"], aku.get("skos:broader", [])):
        errors.append("Circular dependency detected in broader chain")
    
    # Check 3: External URIs resolve
    for match_type in ["exactMatch", "closeMatch", "relatedMatch"]:
        for uri in aku.get(f"skos:{match_type}", []):
            if not uri_resolves(uri):
                errors.append(f"URI does not resolve: {uri}")
    
    # Check 4: Domain-specific validation
    domain = aku["classification"]["domain_path"].split("/")[0]
    if domain == "medicine":
        errors.extend(validate_medical_ontology(aku))
    elif domain == "economics":
        errors.extend(validate_economics_ontology(aku))
    
    return errors
```

### Phase 5: Full Deployment (Weeks 9-10)

**Goal**: All AKUs using comprehensive ontology integration

**Actions**:
1. Migrate all existing AKUs to ontology-enhanced format
2. Update documentation
3. Train agents on ontology usage
4. Deploy validation as CI check
5. Enable semantic search and reasoning

**Success Metrics**:
- 100% of AKUs have valid `@context`
- 80%+ of AKUs have external ontology mappings
- 90%+ of AKUs have SKOS relationships
- Zero ontology consistency errors
- Semantic search operational

---

## Validation Requirements

### 1. Schema Validation

**JSON Schema for Ontology-Enhanced AKU**:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WorldSMEGraphs AKU v2.1 with Ontology Support",
  "type": "object",
  "required": ["@context", "@id", "@type", "metadata", "classification", "content"],
  "properties": {
    "@context": {
      "oneOf": [
        {"type": "string"},
        {"type": "array", "items": {"oneOf": [{"type": "string"}, {"type": "object"}]}}
      ]
    },
    "@id": {
      "type": "string",
      "pattern": "^wsmg(-[a-z]+)?:[a-z0-9-]+$"
    },
    "@type": {
      "oneOf": [
        {"type": "string"},
        {"type": "array", "items": {"type": "string"}}
      ]
    },
    "relationships": {
      "type": "object",
      "properties": {
        "hierarchical": {
          "type": "object",
          "properties": {
            "skos:broader": {"type": "array", "items": {"type": "string"}},
            "skos:narrower": {"type": "array", "items": {"type": "string"}},
            "skos:related": {"type": "array", "items": {"type": "string"}}
          }
        },
        "external": {
          "type": "object",
          "properties": {
            "skos:exactMatch": {"oneOf": [{"type": "string"}, {"type": "array"}]},
            "skos:closeMatch": {"type": "array", "items": {"type": "string"}},
            "owl:sameAs": {"type": "array", "items": {"type": "string"}}
          }
        }
      }
    }
  }
}
```

### 2. SKOS Consistency Validation

**Rules**:
1. **S9**: `skos:exactMatch` is transitive and symmetric
2. **S44**: No `skos:related` cycles
3. Hierarchical integrity: No concept is both broader and narrower
4. Circular dependency detection in broader/narrower chains

**Validator Implementation**:
```python
def validate_skos_consistency(aku: dict, knowledge_base: dict) -> List[str]:
    """Validate SKOS consistency rules."""
    errors = []
    
    # S9: exactMatch transitivity
    if "skos:exactMatch" in aku:
        for match in aku["skos:exactMatch"]:
            if not verify_exact_match_transitive(aku["@id"], match, knowledge_base):
                errors.append(f"exactMatch transitivity violated: {match}")
    
    # S44: No skos:related cycles
    if "skos:related" in aku:
        for related in aku["skos:related"]:
            if creates_cycle(aku["@id"], related, "skos:related", knowledge_base):
                errors.append(f"skos:related cycle detected: {related}")
    
    # Hierarchical integrity
    broader = set(aku.get("skos:broader", []))
    narrower = set(aku.get("skos:narrower", []))
    if broader & narrower:
        errors.append("Concept cannot be both broader and narrower than same concept")
    
    return errors
```

### 3. Domain-Specific Validation

#### Medical Domain

```python
def validate_medical_ontology(aku: dict) -> List[str]:
    """Validate medical domain ontology compliance."""
    errors = []
    
    # Must have at least one medical code
    if "schema:medicalCode" not in aku:
        errors.append("Medical AKU must have medicalCode")
    
    # SNOMED CT code validation
    if "snomed:" in str(aku):
        snomed_codes = extract_snomed_codes(aku)
        for code in snomed_codes:
            if not validate_snomed_code(code):
                errors.append(f"Invalid SNOMED CT code: {code}")
    
    # Anatomical structure validation
    if "schema:associatedAnatomy" in aku:
        anatomy = aku["schema:associatedAnatomy"]
        if not validate_anatomy_reference(anatomy):
            errors.append("Invalid anatomical structure reference")
    
    return errors
```

#### Economics Domain

```python
def validate_economics_ontology(aku: dict) -> List[str]:
    """Validate economics domain ontology compliance."""
    errors = []
    
    # Financial concepts should link to FIBO when possible
    if "financial" in aku.get("classification", {}).get("domain_path", "").lower():
        if not any("fibo:" in str(v) for v in aku.get("relationships", {}).values()):
            errors.append("Warning: Financial concept without FIBO reference")
    
    # Formulas should have proper units
    if "wsmg:formula" in aku:
        formula = aku["wsmg:formula"]
        if "variables" in formula:
            for var in formula["variables"]:
                if "unit" not in var and var.get("symbol") not in ["t", "T", "n"]:
                    errors.append(f"Variable {var['symbol']} missing unit")
    
    return errors
```

### 4. URI Resolution Validation

```python
def validate_external_uris(aku: dict) -> List[str]:
    """Validate that external ontology URIs resolve."""
    errors = []
    
    uri_fields = [
        "owl:sameAs",
        "skos:exactMatch",
        "skos:closeMatch",
        "skos:relatedMatch"
    ]
    
    for field in uri_fields:
        uris = extract_uris(aku, field)
        for uri in uris:
            if not uri_resolves(uri):
                errors.append(f"URI does not resolve: {uri}")
            elif not uri_returns_rdf(uri):
                errors.append(f"URI does not return RDF: {uri}")
    
    return errors
```

### 5. Comprehensive Validation Pipeline

```python
def validate_aku_ontology(aku_path: str) -> ValidationReport:
    """Comprehensive ontology validation for AKU."""
    aku = load_json(aku_path)
    knowledge_base = load_knowledge_base()
    
    report = ValidationReport()
    
    # Schema validation
    report.add_errors(validate_json_schema(aku))
    
    # SKOS consistency
    report.add_errors(validate_skos_consistency(aku, knowledge_base))
    
    # Domain-specific validation
    domain = aku["classification"]["domain_path"].split("/")[0]
    if domain == "medicine":
        report.add_errors(validate_medical_ontology(aku))
    elif domain == "economics":
        report.add_errors(validate_economics_ontology(aku))
    elif domain == "science":
        report.add_errors(validate_science_ontology(aku))
    
    # URI resolution
    report.add_errors(validate_external_uris(aku))
    
    # JSON-LD validity
    report.add_errors(validate_jsonld(aku))
    
    return report
```

---

## Implementation Roadmap

### Immediate (Weeks 1-2)

**Priority 1: Foundation**
- [ ] Create `/domain/_contexts/` directory structure
- [ ] Implement base.jsonld context
- [ ] Implement medicine.jsonld context
- [ ] Implement economics.jsonld context
- [ ] Implement science.jsonld context
- [ ] Update AKU JSON schema with ontology support
- [ ] Create migration utilities

**Priority 2: Validation**
- [ ] Implement JSON-LD validator
- [ ] Implement SKOS consistency checker
- [ ] Create validation test suite
- [ ] Integrate validation into CI/CD

### Short Term (Weeks 3-6)

**Priority 1: External Linking**
- [ ] Integrate BioPortal API for medical concepts
- [ ] Integrate FIBO Navigator for economics concepts
- [ ] Implement Wikidata SPARQL queries
- [ ] Create ontology mapping tools
- [ ] Add external mappings to 50+ existing AKUs

**Priority 2: SKOS Enhancement**
- [ ] Convert existing relationships to SKOS
- [ ] Build domain taxonomies
- [ ] Implement broader/narrower/related analysis
- [ ] Generate concept schemes for each domain

### Medium Term (Weeks 7-12)

**Priority 1: Full Migration**
- [ ] Migrate all existing AKUs to ontology format
- [ ] Generate comprehensive ontology documentation
- [ ] Create domain-specific ontology guides
- [ ] Train agents on ontology usage patterns

**Priority 2: Advanced Features**
- [ ] Implement semantic search
- [ ] Add reasoning capabilities (infer implicit relationships)
- [ ] Create ontology visualization tools
- [ ] Build cross-domain query interface

### Long Term (Months 4-6)

**Priority 1: Ecosystem Integration**
- [ ] Publish contexts to production URIs
- [ ] Register WorldSMEGraphs in LOV (Linked Open Vocabularies)
- [ ] Integrate with external knowledge graphs (Wikidata, DBpedia)
- [ ] Implement federated SPARQL endpoint

**Priority 2: Community and Standards**
- [ ] Publish ontology specification as W3C Community Report
- [ ] Create ontology governance framework
- [ ] Establish ontology review board
- [ ] Build ontology contribution guidelines

---

## Appendices

### Appendix A: Ontology Namespace Registry

| Prefix | Namespace URI | Status | Used For |
|--------|---------------|--------|----------|
| `schema` | https://schema.org/ | Official | Base vocabulary |
| `skos` | http://www.w3.org/2004/02/skos/core# | W3C Rec | Concept organization |
| `dc` | http://purl.org/dc/terms/ | DCMI | Metadata |
| `owl` | http://www.w3.org/2002/07/owl# | W3C Rec | Ontology axioms |
| `rdf` | http://www.w3.org/1999/02/22-rdf-syntax-ns# | W3C Rec | RDF vocabulary |
| `rdfs` | http://www.w3.org/2000/01/rdf-schema# | W3C Rec | Schema vocabulary |
| `prov` | http://www.w3.org/ns/prov# | W3C Rec | Provenance |
| `snomed` | http://snomed.info/id/ | Official | Medical terminology |
| `mesh` | http://id.nlm.nih.gov/mesh/ | Official | Medical subjects |
| `fibo` | https://spec.edmcouncil.org/fibo/ontology/ | OMG Std | Finance ontology |
| `dbpedia` | http://dbpedia.org/resource/ | Official | General knowledge |
| `wikidata` | http://www.wikidata.org/entity/ | Official | Structured data |
| `qudt` | http://qudt.org/schema/qudt/ | Official | Quantities/units |
| `wsmg` | https://worldsmegraphs.org/vocab/ | Project | Custom vocabulary |

### Appendix B: SKOS Relationship Quick Reference

| Property | Meaning | Example | Inverse |
|----------|---------|---------|---------|
| `skos:broader` | More general | NPV → Financial Concept | `skos:narrower` |
| `skos:narrower` | More specific | NPV → NPV Calculation | `skos:broader` |
| `skos:related` | Associated | NPV ↔ IRR | symmetric |
| `skos:exactMatch` | Identical concept | WSMG:NPV = FIBO:NPV | symmetric |
| `skos:closeMatch` | Similar concept | WSMG:NPV ≈ DBpedia:NPV | symmetric |
| `skos:broadMatch` | More general (cross-ontology) | - | `skos:narrowMatch` |
| `skos:narrowMatch` | More specific (cross-ontology) | - | `skos:broadMatch` |
| `skos:relatedMatch` | Related (cross-ontology) | - | symmetric |

### Appendix C: Domain-Specific Ontology Resources

#### Medical Domain
- **SNOMED CT Browser**: https://browser.ihtsdotools.org/
- **MeSH Browser**: https://meshb.nlm.nih.gov/
- **ICD-11 Browser**: https://icd.who.int/browse11/
- **BioPortal**: https://bioportal.bioontology.org/
- **UMLS**: https://www.nlm.nih.gov/research/umls/

#### Economics/Finance Domain
- **FIBO Ontology**: https://spec.edmcouncil.org/fibo/
- **FIBO Navigator**: https://spec.edmcouncil.org/fibo/ontology/
- **Wikidata Economics**: https://www.wikidata.org/wiki/Wikidata:WikiProject_Economics

#### Science Domain
- **QUDT**: http://www.qudt.org/
- **ChEBI**: https://www.ebi.ac.uk/chebi/
- **Gene Ontology**: http://geneontology.org/
- **UniProt**: https://www.uniprot.org/
- **NASA SWEET**: http://sweetontology.net/

#### General
- **Schema.org**: https://schema.org/
- **DBpedia**: https://www.dbpedia.org/
- **Wikidata**: https://www.wikidata.org/
- **LOV**: https://lov.linkeddata.es/dataset/lov/
- **Linked Open Vocabularies**: https://lov.linkeddata.es/dataset/lov/

### Appendix D: Validation Tools

#### JSON-LD Tools
- **JSON-LD Playground**: https://json-ld.org/playground/
- **RDF Validator**: https://www.w3.org/RDF/Validator/
- **SHACL Playground**: https://shacl.org/playground/

#### Ontology Validators
- **Protégé**: https://protege.stanford.edu/
- **OOPS!**: http://oops.linkeddata.es/
- **RDFUnit**: http://aksw.org/Projects/RDFUnit.html

#### Python Libraries
```bash
pip install rdflib  # RDF processing
pip install pyshacl  # SHACL validation
pip install jsonschema  # JSON Schema validation
```

---

## Summary

This specification provides a comprehensive framework for integrating standard ontologies into WorldSMEGraphs:

**Key Achievements**:
1. ✅ Multi-layered ontology architecture (upper, mid-level, domain-specific)
2. ✅ JSON-LD context system for all major domains
3. ✅ SKOS integration for concept relationships
4. ✅ External ontology linking (SNOMED, FIBO, etc.)
5. ✅ Dynamic domain discovery system
6. ✅ Comprehensive validation framework
7. ✅ Clear migration path from current format
8. ✅ Concrete examples for medicine, economics, science
9. ✅ Cross-domain integration patterns
10. ✅ Implementation roadmap with timeline

**Next Steps**:
1. Review and approve this specification
2. Begin Phase 1 implementation (context creation)
3. Update validation tools
4. Migrate pilot AKUs to demonstrate approach
5. Train agents on ontology usage

**Success Metrics**:
- All domains have defined ontology integration
- 80%+ external ontology coverage
- Zero ontology consistency errors
- Semantic interoperability achieved
- Standards compliance verified

---

**Document Version**: 1.0  
**Last Updated**: 2025-12-27  
**Next Review**: 2026-01-27  
**Maintained By**: @ontology, @semantic-harmonization, @standards

