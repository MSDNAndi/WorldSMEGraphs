# Example AKU with Semantic Annotations - Explanation

**File**: `example-npv-definition-with-semantic-annotations.json`  
**Purpose**: Demonstrate best practices for semantic annotation in AKUs  
**Domain**: economics/bwl/finance/valuation/npv

---

## Overview

This example AKU demonstrates how to properly integrate ontology identifiers and semantic annotations into a complete, production-ready Atomic Knowledge Unit (AKU). It serves as a template for creating semantically-rich knowledge units.

---

## Key Features Demonstrated

### 1. Complete Semantic Links Section

```json
"semantic_links": {
  "exact_matches": [...],
  "close_matches": [],
  "broad_matches": [],
  "related_matches": [...],
  "skos_concept": "...",
  "skos_preferred_label": {...},
  "skos_alt_label": {...},
  "skos_definition": {...},
  "skos_scope_note": {...}
}
```

**Placement**: At the same level as `metadata`, `classification`, and `content`

**Purpose**: 
- Links to authoritative ontologies (FIBO, Wikidata, DBpedia)
- Provides multilingual support
- Enables knowledge graph integration
- Facilitates semantic reasoning

### 2. SKOS Compliance

The example follows SKOS (Simple Knowledge Organization System) standards:

- **skos:exactMatch**: Semantically identical concepts
- **skos:closeMatch**: Highly similar concepts
- **skos:broadMatch**: More general concepts
- **skos:relatedMatch**: Related but distinct concepts
- **skos:prefLabel**: Preferred term in each language
- **skos:altLabel**: Alternative terms and synonyms
- **skos:definition**: Formal definition with source citation
- **skos:scopeNote**: Usage context and clarifications

### 3. Multilingual Labels

Includes 8 languages:
- English (en)
- German (de)
- Spanish (es)
- French (fr)
- Italian (it)
- Portuguese (pt)
- Chinese (zh)
- Japanese (ja)

**Best Practice**: Include minimum 4 languages (en, de, es, fr) for European markets. Add more based on target audience.

### 4. Related Concept Linking

The `related_matches` array connects NPV to:
- Internal Rate of Return (IRR)
- Present Value (PV)
- Capital Budgeting
- Discounted Cash Flow (DCF)

**Purpose**: Enables "see also" functionality and knowledge graph traversal.

### 5. Component-Level Semantic Links

Each component references its own Wikidata entity:

```json
{
  "name": "Cash Flows (CF_t)",
  "semantic_link": "http://www.wikidata.org/entity/Q223557",
  ...
}
```

**Benefit**: Enables fine-grained semantic understanding and cross-referencing.

---

## Section-by-Section Breakdown

### Metadata Section

```json
"metadata": {
  "version": "2.0.0",
  "created": "2025-12-27T20:29:00.000Z",
  "contributors": ["terminology-agent"],
  "status": "example",
  "purpose": "Demonstrate proper use of semantic annotations",
  "tags": ["npv", "valuation", "semantic-annotation"]
}
```

**Key Points**:
- Version 2.0.0 indicates inclusion of semantic links
- ISO 8601 timestamps with UTC
- Clear purpose statement
- Descriptive tags for discoverability

### Classification Section

```json
"classification": {
  "domain_path": "economics/bwl/finance/valuation/npv",
  "type": "definition",
  "difficulty": "intermediate",
  "importance": "foundational",
  "prerequisites": [...],
  "learning_objectives": [...]
}
```

**Key Points**:
- Domain path matches directory structure
- Type indicates this is a definition AKU
- Prerequisites enable dependency management
- Learning objectives support educational rendering

### Semantic Links Section (CRITICAL)

This is the focus of the example. See detailed breakdown below.

### Content Section

```json
"content": {
  "definition": {
    "primary": "...",
    "technical": "...",
    "simple": "..."
  },
  "formula": {...},
  "decision_rule": {...},
  "components": [...],
  "example_calculation": {...},
  "advantages": [...],
  "limitations": [...],
  "applications": [...],
  "related_concepts": [...],
  "references": [...]
}
```

**Key Points**:
- Multiple definition levels for different audiences
- Complete formula with notation
- Worked example with step-by-step calculation
- Related concepts link back to semantic_links

---

## Semantic Links Deep Dive

### Exact Matches

```json
"exact_matches": [
  "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
  "http://dbpedia.org/resource/Net_present_value",
  "http://www.wikidata.org/entity/Q1054308"
]
```

**Interpretation**: NPV concept in this AKU is semantically identical to:
1. FIBO's NetPresentValue (financial industry standard)
2. DBpedia's Net_present_value (Wikipedia-derived)
3. Wikidata's Q1054308 (universal knowledge base)

**Use Case**: Automated fact-checking, cross-reference verification, ontology alignment

### Related Matches

```json
"related_matches": [
  "http://www.wikidata.org/entity/Q901690",    // IRR
  "http://dbpedia.org/resource/Internal_rate_of_return",
  "http://www.wikidata.org/entity/Q332099",     // Present Value
  "http://dbpedia.org/resource/Present_value",
  "http://www.wikidata.org/entity/Q1034992",    // Capital Budgeting
  "http://dbpedia.org/resource/Capital_budgeting",
  "http://www.wikidata.org/entity/Q899651",     // DCF
  "http://dbpedia.org/resource/Discounted_cash_flow"
]
```

**Interpretation**: NPV is related to but distinct from these concepts.

**Use Case**: 
- Generate "see also" links
- Build knowledge graph edges
- Suggest related learning materials
- Enable exploratory navigation

### SKOS Concept

```json
"skos_concept": "http://www.wikidata.org/entity/Q1054308"
```

**Purpose**: Primary identifier for this concept in the knowledge graph.

**Why Wikidata**: 
- Universal knowledge base
- Excellent multilingual support
- Stable identifiers
- Community-maintained
- Free and open

### Preferred Labels

```json
"skos_preferred_label": {
  "en": "Net Present Value",
  "de": "Nettobarwert",
  "es": "Valor Actual Neto",
  "fr": "Valeur Actuelle Nette",
  "it": "Valore Attuale Netto",
  "pt": "Valor Presente Líquido",
  "zh": "净现值",
  "ja": "正味現在価値"
}
```

**Usage**: 
- Automatic translation in multilingual rendering
- User interface labels
- Search indexing
- Citation generation

### Alternative Labels

```json
"skos_alt_label": {
  "en": ["NPV", "net present worth"],
  "de": ["Kapitalwert", "NBW"],
  "es": ["VAN", "VPN"],
  "fr": ["VAN"]
}
```

**Usage**:
- Search expansion (find AKUs by acronym)
- Synonym matching
- Regional variations
- Common abbreviations

### Definition with Source

```json
"skos_definition": {
  "en": "The present value of expected cash flows minus the initial investment cost, used to evaluate the profitability of an investment or project",
  "source": "FIBO FBC/DebtAndEquities/Debt, Wikidata Q1054308"
}
```

**Purpose**: Provides authoritative definition with citation.

### Scope Note

```json
"skos_scope_note": {
  "en": "NPV is a primary method in capital budgeting for evaluating long-term investments. A positive NPV indicates the investment is expected to add value to the firm."
}
```

**Purpose**: Clarifies usage context and prevents misunderstanding.

---

## Integration with Content

### Component Linking

Notice how formula components reference semantic links:

```json
"components": [
  {
    "name": "Cash Flows (CF_t)",
    "semantic_link": "http://www.wikidata.org/entity/Q223557",
    ...
  },
  {
    "name": "Discount Rate (r)",
    "semantic_link": "http://www.wikidata.org/entity/Q1226339",
    ...
  }
]
```

**Benefit**: Fine-grained semantic understanding. Each formula variable is linked to its own concept.

### Related Concepts Referencing

```json
"related_concepts": [
  {
    "name": "Internal Rate of Return (IRR)",
    "semantic_link": "http://www.wikidata.org/entity/Q901690",
    ...
  }
]
```

**Benefit**: Consistent linking throughout AKU. Same semantic_link used in both places.

---

## Usage Patterns

### For AKU Developers

**Copy the semantic_links structure:**

1. Identify your concept (e.g., "Discount Rate")
2. Open `aku-semantic-annotations.json`
3. Find your concept's annotation
4. Copy the `semantic_links` object
5. Paste into your AKU at top level
6. Adjust related_matches if needed

**Minimal version** (if tight on space):
```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/...",
    "http://www.wikidata.org/entity/Q..."
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q..."
}
```

**Full version** (recommended):
Include all match types, labels, definitions, and scope notes as shown in the example.

### For Knowledge Graph Builders

**Use semantic_links to:**
1. Create nodes: `@id` → internal identifier, `skos_concept` → external identifier
2. Create edges: `related_matches` → relationship links
3. Label nodes: `skos_preferred_label` → display names
4. Validate: `exact_matches` → cross-reference with external ontologies

**Example Graph Structure**:
```
(NPV Node)
  ├─ internal_id: economics:finance:npv:net-present-value:example-001
  ├─ external_id: http://www.wikidata.org/entity/Q1054308
  ├─ label_en: "Net Present Value"
  ├─ label_de: "Nettobarwert"
  ├─ exact_match: [FIBO, DBpedia, Wikidata]
  └─ related_to:
       ├─ IRR (Q901690)
       ├─ PV (Q332099)
       └─ Capital Budgeting (Q1034992)
```

### For Rendering Engines

**Use semantic_links to:**
1. **Multilingual rendering**: Use `skos_preferred_label[language]`
2. **Synonyms**: Include `skos_alt_label` in search
3. **Definitions**: Pull `skos_definition` for tooltips
4. **Related links**: Generate "see also" from `related_matches`
5. **Citations**: Link to FIBO, Wikipedia (via DBpedia), Wikidata

**Example Rendering**:
```html
<h1>
  <span lang="en">Net Present Value</span>
  <span class="abbr">(NPV)</span>
  <a href="http://www.wikidata.org/entity/Q1054308" class="external">ⓘ</a>
</h1>

<div class="definition">
  <p>The present value of expected cash flows minus...</p>
  <cite>Source: FIBO, Wikidata Q1054308</cite>
</div>

<div class="related">
  <h2>See Also</h2>
  <ul>
    <li><a href="...">Internal Rate of Return</a></li>
    <li><a href="...">Present Value</a></li>
    <li><a href="...">Capital Budgeting</a></li>
  </ul>
</div>
```

---

## Validation

The example includes a validation section:

```json
"validation": {
  "fact_checked": true,
  "formula_verified": true,
  "calculation_verified": true,
  "ontology_aligned": true,
  "sources_cited": true,
  "last_validated": "2025-12-27T20:29:00.000Z"
}
```

**Purpose**: Track quality assurance status.

**Ontology Alignment**: Confirms semantic_links match authoritative sources.

---

## Best Practices Demonstrated

### ✅ DO

1. **Include all three ontologies** (FIBO, Wikidata, DBpedia) when available
2. **Use exactMatch accurately** - only for truly identical concepts
3. **Provide multilingual labels** - minimum 4 languages
4. **Cite sources** in skos_definition
5. **Link related concepts** for knowledge graph navigation
6. **Add scope notes** for potentially ambiguous terms
7. **Validate JSON syntax** before committing
8. **Version your AKU** when adding semantic links (bump to 2.0)

### ❌ DON'T

1. **Don't use exactMatch loosely** - be precise
2. **Don't forget to update timestamps** when modifying
3. **Don't omit FIBO** for financial concepts
4. **Don't mix up Q-numbers** - verify against Wikidata
5. **Don't skip validation section** - track QA status
6. **Don't forget component-level links** - enables fine-grained understanding
7. **Don't ignore multilingual** - critical for global reach
8. **Don't leave empty match arrays** - remove them if unused

---

## Testing the Example

### Validate JSON
```bash
python3 -m json.tool example-npv-definition-with-semantic-annotations.json
```

### Check Semantic Links
```bash
# Extract and verify exact matches
jq '.semantic_links.exact_matches[]' example-npv-definition-with-semantic-annotations.json

# Test Wikidata link
curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q1054308.json" | \
  jq '.entities.Q1054308.labels.en.value'
```

### Extract Labels
```bash
# Get all multilingual labels
jq '.semantic_links.skos_preferred_label' example-npv-definition-with-semantic-annotations.json
```

---

## Extending the Example

### Add More Languages

```json
"skos_preferred_label": {
  "en": "Net Present Value",
  "de": "Nettobarwert",
  "es": "Valor Actual Neto",
  "fr": "Valeur Actuelle Nette",
  "ru": "Чистая приведённая стоимость",  // Russian
  "ar": "صافي القيمة الحالية",            // Arabic
  "hi": "शुद्ध वर्तमान मूल्य"            // Hindi
}
```

### Add Industry-Specific Scope Notes

```json
"skos_scope_note": {
  "en": "NPV is a primary method in capital budgeting...",
  "en_real_estate": "In real estate, NPV accounts for purchase price, rental income, expenses, and terminal sale value",
  "en_pharmaceutical": "In pharma, NPV must account for lengthy R&D timelines, regulatory approval risks, and patent expiration"
}
```

### Add Related Standards

```json
"semantic_links": {
  ...
  "related_standards": [
    {
      "name": "ISO 20022",
      "code": "NPVL",
      "description": "Business code for Net Present Value"
    },
    {
      "name": "XBRL Taxonomy",
      "element": "npv:NetPresentValue"
    }
  ]
}
```

---

## Summary

This example demonstrates:
- ✅ Complete semantic annotation with FIBO, Wikidata, DBpedia
- ✅ SKOS-compliant structure
- ✅ Multilingual support (8 languages)
- ✅ Component-level semantic links
- ✅ Related concept linking
- ✅ Proper match type classification
- ✅ Source citation
- ✅ Scope notes for clarity
- ✅ Integration with content sections
- ✅ Validation tracking

**Use this as your template** for creating high-quality, semantically-rich AKUs in the WorldSMEGraphs system.

---

**Document Type**: Example Explanation  
**Version**: 1.0  
**Created**: 2025-12-27T20:30:00Z  
**Maintained by**: @terminology agent  
**Status**: Active
