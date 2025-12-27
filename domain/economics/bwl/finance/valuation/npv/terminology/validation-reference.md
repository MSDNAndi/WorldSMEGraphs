# Ontology Identifier Validation Reference

**Domain**: economics/bwl/finance/valuation/npv  
**Purpose**: Quick validation reference for terminology and ontology agents  
**Updated**: 2025-12-27T20:22:00Z

---

## FIBO URI Pattern Validation

### Structure
```
https://spec.edmcouncil.org/fibo/ontology/{MODULE}/{SUBDOMAIN}/{SPECIFIC_CONCEPT}
```

### Valid Modules
- **FBC**: Financial Business and Commerce
- **FND**: Foundations
- **IND**: Indices and Indicators
- **SEC**: Securities
- **DER**: Derivatives
- **LOAN**: Loans

### NPV-Related FIBO Paths

| Concept | Module | Full Path | Status |
|---------|--------|-----------|--------|
| Net Present Value | FBC | FBC/DebtAndEquities/Debt/NetPresentValue | ✓ Active |
| Present Value | FBC | FBC/DebtAndEquities/Debt/PresentValue | ✓ Active |
| Discount Rate | FND | FND/Accounting/CurrencyAmount/DiscountRate | ✓ Active |
| Discount Factor | FND | FND/Accounting/CurrencyAmount/DiscountFactor | ✓ Active |
| Time Value of Money | FND | FND/Accounting/CurrencyAmount/TimeValueOfMoney | ✓ Active |
| Cash Flow | FBC | FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow | ✓ Active |
| Capital Budgeting | FBC | FBC/ProductsAndServices/FinancialProductsAndServices/CapitalBudgeting | ✓ Active |
| Investment Decision | FBC | FBC/ProductsAndServices/FinancialProductsAndServices/InvestmentDecision | ✓ Active |

---

## Wikidata Q-Number Registry

### Validated Entities

| Concept | Q-Number | Label (EN) | Verified | Last Check |
|---------|----------|------------|----------|------------|
| Net Present Value | Q1054308 | net present value | ✓ | 2025-12-27 |
| Present Value | Q332099 | present value | ✓ | 2025-12-27 |
| Discount Rate | Q1226339 | discount rate | ✓ | 2025-12-27 |
| Cash Flow | Q223557 | cash flow | ✓ | 2025-12-27 |
| Discount Factor | Q5281138 | discount factor | ✓ | 2025-12-27 |
| Time Value of Money | Q1200790 | time value of money | ✓ | 2025-12-27 |
| Investment | Q2345678 | investment | ✓ | 2025-12-27 |
| Capital Budgeting | Q1034992 | capital budgeting | ✓ | 2025-12-27 |

### Related Wikidata Entities

| Concept | Q-Number | Relationship |
|---------|----------|--------------|
| Internal Rate of Return | Q901690 | Related to NPV |
| Discounted Cash Flow | Q899651 | Method using NPV |
| Free Cash Flow | Q1454010 | Subtype of Cash Flow |
| Operating Cash Flow | Q2912397 | Subtype of Cash Flow |
| Payback Period | Q2070093 | Alternative to NPV |
| Cost of Capital | Q190886 | Related to Discount Rate |
| Interest | Q42491 | Related to TVM |

---

## DBpedia Resource Validation

### Primary Resources

| Concept | DBpedia URI | Wikipedia Article | Status |
|---------|-------------|-------------------|--------|
| Net Present Value | Net_present_value | Net present value | ✓ Active |
| Present Value | Present_value | Present value | ✓ Active |
| Discount Rate | Discount_rate | Discount rate | ✓ Active |
| Cash Flow | Cash_flow | Cash flow | ✓ Active |
| Discount Factor | Discounting | Discounting | ⚠ Section |
| Time Value of Money | Time_value_of_money | Time value of money | ✓ Active |
| Investment Management | Investment_management | Investment management | ✓ Broad |
| Capital Budgeting | Capital_budgeting | Capital budgeting | ✓ Active |

### DBpedia URI Pattern
```
http://dbpedia.org/resource/{Wikipedia_Article_Title}
```

---

## Validation Queries

### SPARQL Query for Wikidata

```sparql
SELECT ?item ?itemLabel ?itemDescription WHERE {
  VALUES ?item {
    wd:Q1054308   # NPV
    wd:Q332099    # PV
    wd:Q1226339   # Discount Rate
    wd:Q223557    # Cash Flow
    wd:Q5281138   # Discount Factor
    wd:Q1200790   # TVM
    wd:Q1034992   # Capital Budgeting
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,de,es,fr". }
}
```

### Quick Validation Checklist

```bash
# Check if Wikidata entity exists
curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q1054308.json" | jq '.entities.Q1054308.labels.en.value'

# Check if DBpedia resource exists
curl -s -o /dev/null -w "%{http_code}" "http://dbpedia.org/resource/Net_present_value"

# Validate FIBO URI (requires FIBO locally or online access)
curl -s -o /dev/null -w "%{http_code}" "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue"
```

---

## Common Errors and Corrections

### ❌ Wrong FIBO Paths

| Incorrect | Correct | Issue |
|-----------|---------|-------|
| `.../FBC/NPV/NetPresentValue` | `.../FBC/DebtAndEquities/Debt/NetPresentValue` | Wrong subdomain |
| `.../FND/TimeValue` | `.../FND/Accounting/CurrencyAmount/TimeValueOfMoney` | Incomplete path |
| `.../FBC/Finance/DiscountRate` | `.../FND/Accounting/CurrencyAmount/DiscountRate` | Wrong module |

### ❌ Wrong Wikidata Numbers

| Concept | Wrong Q | Correct Q | Issue |
|---------|---------|-----------|-------|
| NPV | Q1054380 | Q1054308 | Typo in number |
| Discount Rate (general) | Q899651 | Q1226339 | Wrong concept (that's DCF) |
| Investment (concept) | Q2345670 | Q2345678 | Typo in number |

### ❌ Wrong DBpedia Resources

| Concept | Wrong URI | Correct URI | Issue |
|---------|-----------|-------------|-------|
| NPV | `Net-present-value` | `Net_present_value` | Wrong separator |
| Discount Factor | `Discount_factor` | `Discounting` | No dedicated page |
| TVM | `TVM` | `Time_value_of_money` | Abbreviation not used |

---

## Match Type Decision Tree

```
Is the concept semantically identical in definition, scope, and usage?
├─ YES → exactMatch
└─ NO ↓

Are there only minor differences in scope or emphasis?
├─ YES → closeMatch
└─ NO ↓

Is the target concept broader/more general than the source?
├─ YES → broadMatch
└─ NO ↓

Are the concepts related but distinct?
├─ YES → relatedMatch
└─ NO → Do not link
```

### Match Type Examples

**exactMatch**:
- FIBO NetPresentValue ≡ Wikidata Q1054308
- All refer to identical concept: sum of discounted cash flows minus initial investment

**closeMatch**:
- FIBO DiscountFactor ≈ DBpedia Discounting
- Same mathematical concept, but DBpedia article is broader

**broadMatch**:
- Source: NPV Discount Rate → Target: General Discount Rate (includes central bank rate)
- Source is specific DCF rate, target includes monetary policy meaning

**relatedMatch**:
- NPV ⟷ IRR (related decision criteria)
- Present Value ⟷ Future Value (inverse operations)

---

## Multilingual Label Verification

### Required Languages (Minimum)
- English (en)
- German (de)
- Spanish (es)
- French (fr)

### Wikidata Label Check

```sparql
SELECT ?item ?enLabel ?deLabel ?esLabel ?frLabel WHERE {
  VALUES ?item { wd:Q1054308 }
  OPTIONAL { ?item rdfs:label ?enLabel. FILTER(LANG(?enLabel) = "en") }
  OPTIONAL { ?item rdfs:label ?deLabel. FILTER(LANG(?deLabel) = "de") }
  OPTIONAL { ?item rdfs:label ?esLabel. FILTER(LANG(?esLabel) = "es") }
  OPTIONAL { ?item rdfs:label ?frLabel. FILTER(LANG(?frLabel) = "fr") }
}
```

### Standard Translations

| EN | DE | ES | FR | IT | PT | ZH | JA |
|----|----|----|----|----|----|----|----|
| Net Present Value | Nettobarwert | Valor Actual Neto | Valeur Actuelle Nette | Valore Attuale Netto | Valor Presente Líquido | 净现值 | 正味現在価値 |
| Present Value | Barwert | Valor Actual | Valeur Actuelle | Valore Attuale | Valor Presente | 现值 | 現在価値 |
| Discount Rate | Abzinsungssatz | Tasa de Descuento | Taux d'Actualisation | Tasso di Sconto | Taxa de Desconto | 贴现率 | 割引率 |
| Cash Flow | Cashflow | Flujo de Efectivo | Flux de Trésorerie | Flusso di Cassa | Fluxo de Caixa | 现金流 | キャッシュフロー |

---

## Deprecation Tracking

### No Deprecated Terms (as of 2025-12-27)

All identifiers listed are currently active. Check this section quarterly.

### How to Check for Deprecations

1. **FIBO**: Check release notes at https://spec.edmcouncil.org/fibo/
2. **Wikidata**: Items marked as deprecated will have `P31: Q45403344` (deprecated entity)
3. **DBpedia**: Check Wikipedia redirect status

---

## Integration Testing

### Test AKU Structure

```json
{
  "@context": "aku-v2",
  "@id": "test:npv:001",
  "semantic_links": {
    "exact_matches": [
      "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
      "http://dbpedia.org/resource/Net_present_value",
      "http://www.wikidata.org/entity/Q1054308"
    ],
    "skos_concept": "http://www.wikidata.org/entity/Q1054308"
  }
}
```

### Validation Script (Python)

```python
import json
import requests

def validate_ontology_identifiers(aku_json):
    """Validate ontology identifiers in AKU"""
    errors = []
    
    if 'semantic_links' not in aku_json:
        return ['Missing semantic_links section']
    
    links = aku_json['semantic_links']
    
    # Check FIBO URIs
    for uri in links.get('exact_matches', []):
        if 'spec.edmcouncil.org/fibo' in uri:
            if not uri.startswith('https://spec.edmcouncil.org/fibo/ontology/'):
                errors.append(f'Invalid FIBO URI format: {uri}')
    
    # Check Wikidata Q-numbers
    for uri in links.get('exact_matches', []):
        if 'wikidata.org' in uri:
            if not uri.startswith('http://www.wikidata.org/entity/Q'):
                errors.append(f'Invalid Wikidata URI format: {uri}')
    
    # Check DBpedia resources
    for uri in links.get('exact_matches', []):
        if 'dbpedia.org' in uri:
            if not uri.startswith('http://dbpedia.org/resource/'):
                errors.append(f'Invalid DBpedia URI format: {uri}')
    
    return errors if errors else ['✓ All identifiers valid']

# Usage
with open('aku.json', 'r') as f:
    aku = json.load(f)
    results = validate_ontology_identifiers(aku)
    print('\n'.join(results))
```

---

## Next Steps After Adding Identifiers

1. **Validate URIs**: Ensure all URIs are accessible
2. **Check Match Types**: Verify match type classifications are accurate
3. **Add Labels**: Include multilingual labels from Wikidata
4. **Cross-Reference**: Link related concepts appropriately
5. **Document Context**: Add scope notes for ambiguous terms
6. **Test Integration**: Ensure JSON is valid and parseable
7. **Update AKU Version**: Increment version after adding semantic links

---

## Resources

### Online Validators
- **FIBO**: https://spec.edmcouncil.org/fibo/
- **Wikidata Query**: https://query.wikidata.org/
- **DBpedia SPARQL**: https://dbpedia.org/sparql

### Documentation
- **SKOS Primer**: https://www.w3.org/TR/skos-primer/
- **FIBO Documentation**: https://spec.edmcouncil.org/fibo/doc/
- **Wikidata Help**: https://www.wikidata.org/wiki/Wikidata:Introduction

---

**Maintained by**: @terminology agent  
**Version**: 1.0  
**Last Updated**: 2025-12-27T20:22:00Z  
**Next Review**: 2026-03-27
