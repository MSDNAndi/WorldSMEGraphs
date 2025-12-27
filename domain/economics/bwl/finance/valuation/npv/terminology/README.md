# NPV Terminology and Ontology References

**Domain**: `economics/bwl/finance/valuation/npv`  
**Purpose**: Standardized terminology, ontology identifiers, and semantic annotations for Net Present Value concepts  
**Maintained by**: @terminology agent

---

## Overview

This directory contains comprehensive terminology management resources for NPV (Net Present Value) and related financial concepts in the WorldSMEGraphs knowledge system.

### What's Included

1. **Ontology Identifiers** - Authoritative references from FIBO, Wikidata, and DBpedia
2. **Semantic Annotations** - Ready-to-use JSON snippets for AKUs
3. **Validation References** - Tools and checklists for quality assurance
4. **Quick Start Guide** - Step-by-step instructions for implementation

---

## Files in This Directory

### 📘 ONTOLOGY-IDENTIFIERS.md
**Comprehensive reference document**

Contains verified ontology identifiers for 8 core NPV concepts:
- Net Present Value (NPV)
- Present Value (PV)
- Discount Rate
- Cash Flow
- Discount Factor
- Time Value of Money
- Investment Decision
- Capital Budgeting

**Features**:
- FIBO URIs with module paths
- Wikidata Q-numbers with multilingual labels
- DBpedia resource URIs
- Match type classifications (exact, close, broad, related)
- Cross-reference matrix
- SKOS annotation format examples
- Usage guidelines for each ontology

**Best for**: Understanding the full ontology landscape, researching new concepts

---

### 📄 aku-semantic-annotations.json
**Ready-to-use JSON templates**

Pre-formatted `semantic_links` objects for direct copy-paste into AKUs.

**Features**:
- Complete annotations for all 8 core concepts
- Multilingual labels (en, de, es, fr, it, pt, zh, ja)
- Proper match type categorization
- SKOS-compliant structure
- Integration examples

**Best for**: Quick implementation, ensuring consistent formatting

**Usage**:
```bash
# View available annotations
jq '.annotations | keys' aku-semantic-annotations.json

# Extract specific concept annotation
jq '.annotations.net_present_value.semantic_links' aku-semantic-annotations.json
```

---

### ✅ validation-reference.md
**Quality assurance guide**

Validation tools and error checking for ontology identifiers.

**Features**:
- FIBO URI pattern validation
- Wikidata Q-number registry
- DBpedia resource validation
- Common errors and corrections
- Match type decision tree
- Multilingual label verification
- SPARQL queries for validation
- Python validation script

**Best for**: Verifying correctness, troubleshooting issues, quality control

---

### 🚀 QUICK-START-GUIDE.md
**Step-by-step implementation instructions**

Practical guide for adding semantic links to AKUs in 5 minutes.

**Features**:
- Clear step-by-step workflow
- Common patterns and examples
- Before/after comparisons
- Troubleshooting section
- Quality checklist
- Integration guidelines

**Best for**: First-time users, quick reference, hands-on implementation

---

## Quick Reference

### For AKU Developers

**Adding semantic links to your AKU:**

1. Identify your concept (e.g., "Net Present Value")
2. Open `aku-semantic-annotations.json`
3. Copy the appropriate `semantic_links` object
4. Paste into your AKU at the same level as `metadata`
5. Validate JSON syntax
6. Done!

**Example**:
```json
{
  "@context": "aku-v2",
  "@id": "economics:finance:npv:001",
  "metadata": { ... },
  "semantic_links": {
    "exact_matches": [
      "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
      "http://dbpedia.org/resource/Net_present_value",
      "http://www.wikidata.org/entity/Q1054308"
    ],
    "skos_concept": "http://www.wikidata.org/entity/Q1054308",
    "skos_preferred_label": {
      "en": "Net Present Value",
      "de": "Nettobarwert",
      "es": "Valor Actual Neto",
      "fr": "Valeur Actuelle Nette"
    }
  },
  "content": { ... }
}
```

---

### For Terminology Agents

**Validating terminology consistency:**

1. Check concept definitions against authoritative sources
2. Verify ontology URIs using `validation-reference.md`
3. Ensure match types are correctly classified
4. Validate multilingual labels (minimum: en, de, es, fr)
5. Cross-reference related concepts
6. Document any ambiguities

**Tools**:
```bash
# Validate Wikidata entity
curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q1054308.json" | \
  jq '.entities.Q1054308.labels.en.value'

# Check DBpedia resource
curl -s -o /dev/null -w "%{http_code}" \
  "http://dbpedia.org/resource/Net_present_value"
```

---

### For Knowledge Graph Creators

**Building semantic relationships:**

1. Use `skos_concept` as primary node identifier
2. Link related concepts via `related_matches`
3. Implement hierarchies using FIBO structure
4. Enable multilingual navigation via `skos_preferred_label`
5. Leverage match types for reasoning

**SPARQL Query Example**:
```sparql
SELECT ?concept ?label WHERE {
  VALUES ?concept {
    wd:Q1054308   # NPV
    wd:Q332099    # PV
    wd:Q901690    # IRR
  }
  ?concept rdfs:label ?label.
  FILTER(LANG(?label) = "en")
}
```

---

## Ontology Sources

### 1. FIBO (Primary for Financial Concepts)
- **URL**: https://spec.edmcouncil.org/fibo/
- **Authority**: EDM Council (financial industry standard)
- **License**: MIT
- **Coverage**: Comprehensive financial/business ontology
- **Update Frequency**: Quarterly releases

**When to use**: Always preferred for core financial and business concepts

### 2. Wikidata (Primary for Cross-Reference)
- **URL**: https://www.wikidata.org/
- **Authority**: Wikimedia Foundation community
- **License**: CC0 (Public Domain)
- **Coverage**: Universal knowledge base with multilingual support
- **Update Frequency**: Continuous (community-driven)

**When to use**: Essential for multilingual labels and general knowledge linking

### 3. DBpedia (Secondary for General Knowledge)
- **URL**: https://dbpedia.org/
- **Authority**: DBpedia Association (derived from Wikipedia)
- **License**: CC BY-SA 3.0, GFDL
- **Coverage**: Structured data from Wikipedia
- **Update Frequency**: Annual releases

**When to use**: Useful for natural language context and Wikipedia integration

---

## Concepts Covered

| Concept | FIBO | Wikidata | DBpedia | Translations |
|---------|------|----------|---------|--------------|
| Net Present Value | ✓ | Q1054308 | ✓ | 8 languages |
| Present Value | ✓ | Q332099 | ✓ | 8 languages |
| Discount Rate | ✓ | Q1226339 | ✓ | 8 languages |
| Cash Flow | ✓ | Q223557 | ✓ | 8 languages |
| Discount Factor | ✓ | Q5281138 | ✓ | 8 languages |
| Time Value of Money | ✓ | Q1200790 | ✓ | 8 languages |
| Investment Decision | ✓ | Q2345678 | ✓ | 8 languages |
| Capital Budgeting | ✓ | Q1034992 | ✓ | 8 languages |

**Languages**: English (en), German (de), Spanish (es), French (fr), Italian (it), Portuguese (pt), Chinese (zh), Japanese (ja)

---

## Match Type System

### exactMatch
Concepts are semantically identical and fully interchangeable.

**Example**: FIBO NetPresentValue ≡ Wikidata Q1054308

### closeMatch
Highly similar concepts with minor differences in scope.

**Example**: FIBO DiscountFactor ≈ DBpedia Discounting (broader article)

### broadMatch
Target concept is broader/more general than source.

**Example**: NPV Discount Rate → General Discount Rate (includes central bank rate)

### relatedMatch
Related but distinct concepts, useful for navigation.

**Example**: NPV ⟷ IRR (both are capital budgeting methods)

---

## Validation Workflow

```
1. Identify Concept
   ↓
2. Research Ontology IDs
   ├─ Check FIBO
   ├─ Check Wikidata
   └─ Check DBpedia
   ↓
3. Classify Match Types
   ├─ exactMatch?
   ├─ closeMatch?
   ├─ broadMatch?
   └─ relatedMatch?
   ↓
4. Extract Multilingual Labels
   ├─ Minimum: en, de, es, fr
   └─ Extended: it, pt, zh, ja
   ↓
5. Create Semantic Links Object
   ├─ exact_matches: [...]
   ├─ close_matches: [...]
   ├─ broad_matches: [...]
   ├─ related_matches: [...]
   ├─ skos_concept: "..."
   └─ skos_preferred_label: {...}
   ↓
6. Validate JSON Syntax
   ↓
7. Verify URIs (optional)
   ↓
8. Add to AKU
   ↓
9. Update AKU Version
```

---

## Common Use Cases

### Use Case 1: Creating New NPV AKU
1. Read `QUICK-START-GUIDE.md` (steps 1-5)
2. Copy template from `aku-semantic-annotations.json`
3. Paste into AKU JSON structure
4. Validate using `validation-reference.md` checklist

### Use Case 2: Validating Existing Terminology
1. Open `validation-reference.md`
2. Run SPARQL queries against Wikidata
3. Verify FIBO URIs match documented paths
4. Check multilingual labels for completeness
5. Confirm match types are appropriate

### Use Case 3: Researching New Financial Concept
1. Start with `ONTOLOGY-IDENTIFIERS.md` as template
2. Search FIBO, Wikidata, DBpedia for concept
3. Document URIs and match types
4. Extract multilingual labels from Wikidata
5. Create new entry in `aku-semantic-annotations.json`
6. Update this README with new concept

### Use Case 4: Multilingual Rendering
1. Extract `skos_preferred_label` from annotation
2. Use for audience-appropriate language rendering
3. Fall back to `skos_alt_label` for synonyms
4. Include `skos_definition` for context

---

## Best Practices

### ✅ Do

- **Always include FIBO** if concept exists in FIBO ontology
- **Always include Wikidata** for multilingual support
- **Specify match types accurately** using the decision tree
- **Include minimum 4 languages** (en, de, es, fr)
- **Cross-reference related concepts** in `related_matches`
- **Validate JSON syntax** before committing
- **Document ambiguities** with `scope_note`
- **Version AKUs** when adding semantic links

### ❌ Don't

- **Don't use exactMatch loosely** - only for truly identical concepts
- **Don't mix up Q-numbers** - verify against Wikidata
- **Don't use hyphens in DBpedia URIs** - use underscores
- **Don't omit FIBO** for financial concepts - it's the industry standard
- **Don't skip validation** - broken URIs undermine trust
- **Don't forget scope notes** for ambiguous terms

---

## Maintenance

### Update Schedule
- **Quarterly**: Check FIBO releases for updates
- **Monthly**: Verify Wikidata Q-numbers still active
- **Annually**: Review DBpedia for URI changes

### Version Control
- **Current Version**: 1.0
- **Last Updated**: 2025-12-27T20:22:00Z
- **Next Review**: 2026-03-27

### Adding New Concepts

1. Research ontology identifiers thoroughly
2. Add to `ONTOLOGY-IDENTIFIERS.md` with full documentation
3. Create JSON template in `aku-semantic-annotations.json`
4. Update validation reference if needed
5. Add to "Concepts Covered" table in this README
6. Increment version number

---

## Related Agents

- **@terminology** - Terminology management and validation (primary)
- **@semantic-harmonization** - Cross-domain concept alignment
- **@ontology** - Ontology structure and relationships
- **@multi-lingual-validation** - Translation verification
- **@verification** - Definition validation
- **@quality** - Overall quality assessment

---

## Integration Points

### With AKU System
- Semantic links added to AKU JSON at top level
- Used for knowledge graph construction
- Enables cross-AKU relationship mapping

### With Rendering System
- Multilingual labels support audience-appropriate rendering
- Definitions provide context for explanations
- Related concepts enable "see also" suggestions

### With Validation System
- Ontology URIs enable automated fact-checking
- Match types support semantic reasoning
- SKOS compliance ensures interoperability

---

## Troubleshooting

### Issue: Cannot Find FIBO URI
**Solution**: Check `.../ONTOLOGY-IDENTIFIERS.md` for correct module path. If concept doesn't exist in FIBO, use Wikidata/DBpedia only.

### Issue: Wikidata Q-Number Changed
**Solution**: Use Wikidata redirect resolver. Update all references. Document change in maintenance log.

### Issue: DBpedia Resource 404
**Solution**: Check for Wikipedia redirects. Use canonical article title with underscores. May need to use broader/related concept.

### Issue: Uncertain Match Type
**Solution**: When in doubt, use `closeMatch` instead of `exactMatch`. Add `scope_note` to document uncertainty.

---

## Quick Links

- [FIBO Specification](https://spec.edmcouncil.org/fibo/)
- [Wikidata Query Service](https://query.wikidata.org/)
- [DBpedia Lookup](http://lookup.dbpedia.org/)
- [SKOS Specification](https://www.w3.org/TR/skos-reference/)

---

## Contact

**Maintained by**: @terminology agent  
**For questions**: Invoke `@terminology` with your query  
**For updates**: Submit PR with documentation changes

---

**Version**: 1.0  
**Created**: 2025-12-27T20:22:00Z  
**Status**: Active  
**License**: Consistent with WorldSMEGraphs project license
