# Economics & Finance Ontology Quick Reference

**Version**: 1.0  
**Date**: 2025-12-27  
**For**: Economics and finance AKU annotation  
**See Also**: docs/ONTOLOGY-QUICKSTART.md (general guide)

---

## Overview

This guide provides ontology standards and URIs for annotating economics and finance AKUs. Follow the pattern established by the ENHANCED present value AKU.

---

## Key Ontology Standards for Economics

### 1. FIBO (Financial Industry Business Ontology)
**Authority**: EDM Council  
**Use for**: Financial concepts, instruments, markets, organizations  
**Browser**: https://spec.edmcouncil.org/fibo/  
**Format**: `fibo:ConceptName`  
**Example**: `fibo:PresentValue`, `fibo:NetPresentValue`

### 2. DBpedia
**Authority**: DBpedia Association  
**Use for**: General knowledge concepts, cross-domain linking  
**Browser**: https://dbpedia.org/  
**Format**: `dbr:Concept_name` or full URI `http://dbpedia.org/resource/Concept_name`  
**Example**: `dbr:Present_value`, `dbr:Net_present_value`

### 3. Wikidata
**Authority**: Wikimedia Foundation  
**Use for**: Universal concepts, multilingual support  
**Browser**: https://www.wikidata.org/  
**Format**: `wd:QXXXXXX` or full URI `http://www.wikidata.org/entity/QXXXXXX`  
**Example**: `wd:Q1053298` (Present Value)

### 4. Schema.org
**Authority**: Schema.org community  
**Use for**: Structured data on the web  
**Browser**: https://schema.org/  
**Format**: `schema:ConceptName`  
**Example**: `schema:MonetaryAmount`, `schema:FinancialProduct`

---

## Common Economics/Finance Concepts

### Net Present Value (NPV)
```json
{
  "skos:prefLabel": "Net Present Value",
  "skos:altLabel": ["NPV"],
  "skos:exactMatch": [
    "fibo:NetPresentValue",
    "http://www.wikidata.org/entity/Q1632881"
  ],
  "skos:closeMatch": [
    "dbr:Net_present_value"
  ]
}
```

### Present Value (PV)
```json
{
  "skos:prefLabel": "Present Value",
  "skos:altLabel": ["PV", "Discounted Value"],
  "skos:exactMatch": [
    "fibo:PresentValue",
    "http://www.wikidata.org/entity/Q1053298"
  ],
  "skos:closeMatch": [
    "dbr:Present_value"
  ]
}
```

### Discount Rate
```json
{
  "skos:prefLabel": "Discount Rate",
  "skos:altLabel": ["Required Rate of Return", "Hurdle Rate"],
  "skos:exactMatch": [
    "fibo:DiscountRate",
    "http://www.wikidata.org/entity/Q1227960"
  ],
  "skos:closeMatch": [
    "dbr:Discount_rate"
  ]
}
```

### Cash Flow
```json
{
  "skos:prefLabel": "Cash Flow",
  "skos:exactMatch": [
    "fibo:CashFlow",
    "http://www.wikidata.org/entity/Q913824"
  ],
  "skos:closeMatch": [
    "dbr:Cash_flow"
  ]
}
```

### Internal Rate of Return (IRR)
```json
{
  "skos:prefLabel": "Internal Rate of Return",
  "skos:altLabel": ["IRR"],
  "skos:exactMatch": [
    "fibo:InternalRateOfReturn",
    "http://www.wikidata.org/entity/Q899729"
  ],
  "skos:closeMatch": [
    "dbr:Internal_rate_of_return"
  ]
}
```

### Time Value of Money
```json
{
  "skos:prefLabel": "Time Value of Money",
  "skos:exactMatch": [
    "http://www.wikidata.org/entity/Q1141506"
  ],
  "skos:broader": [
    "fibo:TimeValue"
  ],
  "skos:closeMatch": [
    "dbr:Time_value_of_money"
  ]
}
```

---

## AKU Structure Template

### Minimal Economics Ontology Annotation

```json
{
  "@context": [
    "file://domain/_contexts/base.jsonld",
    "file://domain/_contexts/economics.jsonld"
  ],
  "@id": "wsmg-econ:concept-identifier",
  "@type": ["schema:EducationalResource", "skos:Concept"],
  
  "skos:prefLabel": {
    "@language": "en",
    "@value": "Concept Name"
  },
  "skos:altLabel": ["Synonym 1", "Abbreviation"],
  "skos:definition": "Clear definition of the concept",
  "skos:notation": "ABBR",
  
  "relationships": {
    "skos:broader": [
      {
        "@id": "wsmg-econ:parent-concept",
        "@type": "skos:Concept"
      }
    ],
    "skos:related": [
      {
        "@id": "wsmg-econ:related-concept",
        "@type": "skos:Concept"
      }
    ],
    "skos:exactMatch": [
      "fibo:ConceptName",
      "http://www.wikidata.org/entity/QXXXXXX"
    ],
    "skos:closeMatch": [
      "dbr:Concept_name"
    ]
  }
}
```

---

## Finding Ontology URIs

### FIBO
1. Go to: https://spec.edmcouncil.org/fibo/ontology/
2. Browse or search for concept
3. Find appropriate module (FND, IND, BE, etc.)
4. Use format: `fibo:ConceptName`

**Common FIBO Modules**:
- `fibo-fnd-` Foundation (dates, amounts, agreements)
- `fibo-ind-` Indicators (rates, indices)
- `fibo-fbc-` Financial Business and Commerce

### Wikidata
1. Go to: https://www.wikidata.org/
2. Search for concept
3. Find Q-number (e.g., Q1053298)
4. Use URI: `http://www.wikidata.org/entity/QXXXXXX`

### DBpedia
1. Go to: https://dbpedia.org/
2. Search for concept
3. Use format: `dbr:Concept_name` (underscores for spaces)
4. Or full URI: `http://dbpedia.org/resource/Concept_name`

---

## Match Types

### exactMatch ✅
Use when concepts are semantically identical:
- NPV in FIBO = NPV in Wikidata
- Present Value definition matches exactly

### closeMatch ⚠️
Use when concepts are similar but may differ in scope or emphasis:
- DBpedia articles (may have broader or narrower scope)
- Related but not perfectly identical concepts

### broadMatch 📚
Use when linking to parent/broader concepts:
- NPV → Time Value of Money
- Discount Rate → Interest Rate

---

## Common Wikidata Q-Numbers for Finance

| Concept | Wikidata Q-Number | URI |
|---------|-------------------|-----|
| Net Present Value | Q1632881 | http://www.wikidata.org/entity/Q1632881 |
| Present Value | Q1053298 | http://www.wikidata.org/entity/Q1053298 |
| Discount Rate | Q1227960 | http://www.wikidata.org/entity/Q1227960 |
| Cash Flow | Q913824 | http://www.wikidata.org/entity/Q913824 |
| Internal Rate of Return | Q899729 | http://www.wikidata.org/entity/Q899729 |
| Time Value of Money | Q1141506 | http://www.wikidata.org/entity/Q1141506 |
| Discounted Cash Flow | Q1227266 | http://www.wikidata.org/entity/Q1227266 |
| Cost of Capital | Q1136774 | http://www.wikidata.org/entity/Q1136774 |
| Payback Period | Q897239 | http://www.wikidata.org/entity/Q897239 |
| Profitability Index | Q2108948 | http://www.wikidata.org/entity/Q2108948 |

---

## Example: Complete NPV AKU Annotation

See: `.project/pilot/npv-finance/akus/definitions/aku-003-present-value-concept-ENHANCED.json`

Key elements:
- SKOS properties (prefLabel, altLabel, definition)
- exactMatch to FIBO and Wikidata
- closeMatch to DBpedia
- Hierarchical relationships (broader, narrower, related)
- Provenance information

---

## Best Practices

1. **Always use FIBO** for financial concepts when available
2. **Add Wikidata** for multilingual support and cross-domain linking
3. **Include DBpedia** for general knowledge integration
4. **Use SKOS properties** (prefLabel, altLabel, definition, notation)
5. **Document relationships** (broader, narrower, related)
6. **Validate URIs** - check that they resolve correctly
7. **Consider audience** - link to appropriate level of detail

---

## Validation

### Check URIs Resolve
```bash
# FIBO
curl -I https://spec.edmcouncil.org/fibo/ontology/

# Wikidata  
curl -I https://www.wikidata.org/entity/Q1053298

# DBpedia
curl -I http://dbpedia.org/resource/Present_value
```

### Validate JSON-LD
```bash
python .project/agents/quality-assurance/tools/validate_ontology.py aku.json
```

---

## Related Documentation

- **General Ontology Guide**: docs/ONTOLOGY-QUICKSTART.md
- **Medical Ontology Guide**: docs/MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md
- **Economics Context**: domain/_contexts/economics.jsonld
- **ENHANCED Example**: .project/pilot/npv-finance/akus/definitions/aku-003-present-value-concept-ENHANCED.json

---

## Additional Economics Ontologies (Advanced)

### XBRL (eXtensible Business Reporting Language)
- **Use for**: Financial reporting, accounting standards
- **URL**: https://www.xbrl.org/

### UN/CEFACT
- **Use for**: Trade facilitation, business processes
- **URL**: https://unece.org/trade/uncefact

### OECD Statistics
- **Use for**: Economic indicators, statistics
- **URL**: https://stats.oecd.org/

---

**Last Updated**: 2025-12-27  
**Maintained by**: @terminology agent  
**Status**: Active
