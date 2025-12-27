# Ontology Systems & AKU Numbering Analysis

**Date**: 2025-12-27  
**Purpose**: Research standardized ontologies and analyze AKU numbering sustainability  
**Status**: Research Complete

---

## Executive Summary

### Key Findings:
1. **Project Structure Scalability**: Current structure will face issues beyond ~10,000 AKUs
2. **Standard Ontologies Exist**: Multiple mature systems available (DBpedia, Schema.org, DOLCE, BFO, SUMO)
3. **AKU Numbering Issues**: Current sequential numbering (001-999) is not sustainable at scale
4. **Recommended Approach**: Hierarchical UUID-based system with semantic paths

---

## 1. Project Structure Scalability Analysis

### Current Approach
```
domain/
├── medicine/surgery/vascular/complications/endoleaks/type-2/
│   └── akus/
│       ├── definitions/
│       │   ├── aku-001-type2-endoleak-definition.json
│       │   └── aku-002-endoleak-classification.json
│       ├── diagnosis/
│       │   └── aku-005-cta-imaging-findings.json
```

### Problems at Scale

#### Problem 1: Deep Nesting
- **Current**: Up to 8-10 levels deep
- **Issue**: File system limitations (255 char path limit)
- **Impact**: Cannot go deeper for specialized topics

#### Problem 2: Single File Approach
- **Current**: Each AKU is a separate JSON file
- **Issue**: 100,000 AKUs = 100,000 files in one repo
- **Impact**: Git performance degrades, file system stress

#### Problem 3: No Clear Boundary
- **Question**: When does a leaf topic become too large?
- **Current**: No defined split criteria
- **Impact**: Inconsistent organization

### Proposed Solutions

#### Solution A: Hybrid Storage (RECOMMENDED)
```
domain/
├── index/
│   ├── medicine.index.json       # All medicine AKUs indexed here
│   └── economics.index.json      # All economics AKUs indexed here
├── content/
│   ├── medicine/
│   │   ├── batch-0000.jsonl     # First 1000 AKUs (JSONL format)
│   │   ├── batch-0001.jsonl     # Next 1000 AKUs
│   │   └── batch-0002.jsonl
│   └── economics/
│       └── batch-0000.jsonl
└── structure/
    └── medicine/
        └── surgery/vascular/... # Directory structure for browsing
```

**Benefits**:
- Index files enable O(1) lookup
- JSONL files batch AKUs (1000 per file)
- Directory structure preserved for human navigation
- Git handles ~1000 files well (vs 100,000)

#### Solution B: Database-Backed with File Sync
```
- SQLite database for primary storage
- JSON files auto-generated for Git
- Best of both: queryable + version controlled
```

#### Solution C: Monorepo Split
```
WorldSMEGraphs/
├── core/              # This repo - infrastructure
├── medicine/          # Separate repo
├── economics/        # Separate repo
└── index/            # Cross-repo index
```

---

## 2. Standardized Ontology Systems Research

### Overview
Multiple mature ontology systems exist for knowledge representation:

### 2.1 Upper Ontologies (Meta-Level)

#### DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering)
- **URL**: http://www.loa.istc.cnr.it/dolce/
- **Scope**: General-purpose upper ontology
- **Key Concepts**: Objects, Events, Qualities, Abstracts
- **Status**: Well-established (2002+), widely used
- **Alignment**: Good for our multi-domain approach

#### BFO (Basic Formal Ontology)
- **URL**: https://basic-formal-ontology.org/
- **Scope**: Top-level ontology for scientific research
- **Key Concepts**: Continuants, Occurrents, Universals, Particulars
- **Status**: ISO standard (ISO/IEC 21838)
- **Alignment**: Excellent for scientific domains

#### SUMO (Suggested Upper Merged Ontology)
- **URL**: https://www.ontologyportal.org/
- **Scope**: Comprehensive formal ontology
- **Key Concepts**: 1000+ terms, 4000+ axioms
- **Status**: Open source, large community
- **Alignment**: Comprehensive but may be too formal

### 2.2 Domain-Specific Ontologies

#### Schema.org
- **URL**: https://schema.org/
- **Scope**: Web markup, general knowledge
- **Key Concepts**: Thing → MedicalEntity, Course, Article, etc.
- **Status**: Industry standard (Google, Microsoft, Yahoo, Yandex)
- **Current Use**: Already using in AKUs (`@context: "https://schema.org/"`)
- **Alignment**: ✅ PERFECT - already adopted

#### DBpedia Ontology
- **URL**: https://www.dbpedia.org/resources/ontology/
- **Scope**: General knowledge from Wikipedia
- **Key Concepts**: 685 classes, 2,795 properties
- **Status**: Mature, multilingual
- **Alignment**: Good for linking to external knowledge

#### Medical Ontologies

**SNOMED CT** (Systematized Nomenclature of Medicine - Clinical Terms)
- **URL**: https://www.snomed.org/
- **Scope**: Clinical terminology (390,000+ concepts)
- **Status**: International standard
- **Licensing**: Free for many uses
- **Alignment**: ✅ EXCELLENT for medical domains

**MeSH** (Medical Subject Headings)
- **URL**: https://www.nlm.nih.gov/mesh/
- **Scope**: Biomedical literature indexing
- **Status**: NLM standard, freely available
- **Alignment**: Good for research/literature

**ICD-11** (International Classification of Diseases)
- **URL**: https://icd.who.int/
- **Scope**: Disease classification
- **Status**: WHO standard
- **Alignment**: Essential for medical conditions

#### Economics Ontologies

**FIBO** (Financial Industry Business Ontology)
- **URL**: https://spec.edmcouncil.org/fibo/
- **Scope**: Financial services, business concepts
- **Status**: OMG standard
- **Alignment**: ✅ EXCELLENT for economics/finance domains

### 2.3 Linking Ontologies

#### SKOS (Simple Knowledge Organization System)
- **URL**: https://www.w3.org/2004/02/skos/
- **Scope**: Thesauri, taxonomies, classification schemes
- **Key Concepts**: Concepts, Collections, Relationships
- **Status**: W3C Recommendation
- **Alignment**: ✅ PERFECT for linking our concepts

### 2.4 Recommended Integration Strategy

```json
{
  "@context": [
    "https://schema.org/",
    "http://www.w3.org/2004/02/skos/core#",
    {
      "@vocab": "https://worldsmegraphs.org/vocab/",
      "snomed": "http://snomed.info/id/",
      "mesh": "http://id.nlm.nih.gov/mesh/",
      "fibo": "https://spec.edmcouncil.org/fibo/ontology/"
    }
  ],
  "@type": "MedicalEntity",
  "@id": "medicine:vascular:endoleak:type2:001",
  "sameAs": [
    "snomed:449567000",
    "mesh:D000078862"
  ],
  "broader": "medicine:vascular:endoleak",
  "narrower": ["medicine:vascular:endoleak:type2:lumbar-source"],
  "related": ["medicine:vascular:evar", "medicine:vascular:aneurysm"]
}
```

**Benefits**:
- Interoperable with existing systems
- Can link to external knowledge bases
- Standard vocabularies for relationships
- Machine-readable semantics

---

## 3. AKU Numbering System Analysis

### Current System Problems

#### Problem 1: Local Sequential Numbering
```
domain/medicine/.../type-2/akus/definitions/aku-001-...
domain/medicine/.../type-2/akus/definitions/aku-002-...
domain/economics/bwl/finance/akus/definitions/aku-001-...  # COLLISION!
```

**Issues**:
- Number "001" used in multiple places
- No global uniqueness
- Cannot reference across domains easily
- Merge conflicts when multiple contributors

#### Problem 2: No Semantic Meaning
- "001" tells you nothing about the content
- Order is arbitrary
- Renumbering breaks references

#### Problem 3: Limited Range
- 001-999 = max 999 AKUs per category
- What happens at 1000?
- Need to restructure or add digits

#### Problem 4: Manual Management
- Humans must track next available number
- Risk of duplicates
- No automatic assignment

### Alternative Numbering Systems

#### Option A: Hierarchical Dot Notation (Like Dewey Decimal)
```
medicine.surgery.vascular.001
medicine.surgery.vascular.complications.001
medicine.surgery.vascular.complications.endoleaks.001
```

**Pros**: Semantic hierarchy, sortable
**Cons**: Still arbitrary numbers, limited range per level

#### Option B: UUID-Based
```
aku:550e8400-e29b-41d4-a716-446655440000
```

**Pros**: Globally unique, no collisions, auto-generated
**Cons**: Not human-readable, not semantic

#### Option C: Semantic Path-Based (RECOMMENDED)
```
medicine:surgery:vascular:complications:endoleak:type2:definition:retrograde-flow
```

**Pros**: 
- Globally unique (full path)
- Self-describing
- Hierarchical
- Human-readable
- Can generate from structure

**Cons**: Longer strings

#### Option D: Hybrid: Semantic Path + Short Hash
```
medicine:vascular:endoleak-type2:def-001
or
med:vasc:endo2:7f3a91
```

**Pros**: Compact, unique, somewhat readable
**Cons**: Hash part is opaque

### Recommended Solution: Semantic URI Pattern

```
{domain}:{path}:{concept}:{uuid}

Examples:
medicine:vascular:complications:endoleak-type2:def:a7f3c891
economics:bwl:finance:npv:formula:e91bc3f7
science:math:algebra:linear-equations:example:12d9a4c3
```

**Format**:
- **Domain**: Top-level category (medicine, economics, science)
- **Path**: Hierarchical path (colon-separated)
- **Concept**: Specific concept (kebab-case)
- **UUID**: Short hash (8 chars) for uniqueness

**Benefits**:
1. ✅ Globally unique (path + hash)
2. ✅ Human-readable (semantic path)
3. ✅ Automatically generated (path from file location, hash computed)
4. ✅ Collision-resistant (8-char hash = 16^8 = 4.3 billion possibilities)
5. ✅ Sortable and filterable
6. ✅ References work across domains
7. ✅ No manual number management

**Implementation**:
```python
import hashlib
from pathlib import Path

def generate_aku_id(file_path: Path, concept_name: str) -> str:
    """Generate semantic AKU ID from file path."""
    # Extract domain path
    parts = file_path.relative_to("domain").parts[:-2]  # Remove /akus/category
    domain_path = ":".join(parts)
    
    # Generate short hash from full path + concept for uniqueness
    full_id = f"{domain_path}:{concept_name}"
    hash_obj = hashlib.sha256(full_id.encode())
    short_hash = hash_obj.hexdigest()[:8]
    
    return f"{domain_path}:{concept_name}:{short_hash}"

# Example usage:
path = Path("domain/medicine/surgery/vascular/complications/endoleaks/type-2/akus/definitions")
concept = "type2-endoleak-definition"
aku_id = generate_aku_id(path, concept)
# Result: "medicine:surgery:vascular:complications:endoleaks:type-2:type2-endoleak-definition:7f3a91c8"
```

---

## 4. Migration Strategy

### Phase 1: Maintain Backward Compatibility
- Keep current numbering for existing AKUs
- Add new field: `"canonical_id": "medicine:vascular:..."`
- Both IDs work during transition

### Phase 2: Implement Auto-Generation
- Script to generate canonical IDs
- Update validation to require canonical_id
- Deprecate old aku_id field

### Phase 3: Adopt Standard Ontologies
- Add SKOS relationships (broader, narrower, related)
- Link to SNOMED, MeSH, FIBO where applicable
- Use Schema.org types consistently

### Phase 4: Structure Optimization
- Move to hybrid storage (index + batched content)
- Implement cross-references
- Add search index

---

## 5. Recommendations Summary

### Immediate Actions (This PR)
1. ✅ Document these findings
2. ✅ Create issue for AKU ID migration
3. ✅ Add canonical_id field to AKU schema

### Short Term (Next Month)
1. Implement semantic ID generation script
2. Add validation for canonical IDs
3. Update documentation with new ID format
4. Begin using SKOS relationships

### Medium Term (2-3 Months)
1. Migrate existing AKUs to new ID format
2. Implement hybrid storage for scalability
3. Add ontology alignment (SNOMED, FIBO, etc.)
4. Create cross-domain index

### Long Term (6+ Months)
1. Consider repository splitting for large domains
2. Implement database backing with file sync
3. Build query interface
4. Add visualization tools

---

## 6. Agent Recommendations

For implementing these changes, utilize these agents:

- **@ontology**: For ontology alignment and SKOS relationships
- **@semantic-harmonization**: For consistent terminology
- **@relationship-extractor**: For identifying broader/narrower/related concepts
- **@database-query**: For implementing search/query capabilities
- **@file-organization-agent**: For structure migration
- **@verification**: For validating ID uniqueness and consistency
- **@standards**: For ensuring compliance with W3C/ISO standards

---

## References

1. DOLCE: http://www.loa.istc.cnr.it/dolce/
2. BFO: https://basic-formal-ontology.org/
3. Schema.org: https://schema.org/
4. SKOS: https://www.w3.org/2004/02/skos/
5. SNOMED CT: https://www.snomed.org/
6. FIBO: https://spec.edmcouncil.org/fibo/
7. DBpedia: https://www.dbpedia.org/
8. MeSH: https://www.nlm.nih.gov/mesh/

---

**Last Updated**: 2025-12-27  
**Next Review**: 2026-01-27
