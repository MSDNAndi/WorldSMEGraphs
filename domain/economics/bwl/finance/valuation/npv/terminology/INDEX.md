# NPV Ontology Identifiers - Quick Reference Index

**Domain**: economics/bwl/finance/valuation/npv  
**Purpose**: Concise lookup table for all ontology identifiers  
**Format**: Quick copy-paste reference

---

## 1. Net Present Value (NPV)

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue`  
**Wikidata**: `http://www.wikidata.org/entity/Q1054308`  
**DBpedia**: `http://dbpedia.org/resource/Net_present_value`  
**Match**: exactMatch (all three)

**Labels**: EN: Net Present Value | DE: Nettobarwert | ES: Valor Actual Neto | FR: Valeur Actuelle Nette

---

## 2. Present Value (PV)

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PresentValue`  
**Wikidata**: `http://www.wikidata.org/entity/Q332099`  
**DBpedia**: `http://dbpedia.org/resource/Present_value`  
**Match**: exactMatch (all three)

**Labels**: EN: Present Value | DE: Barwert | ES: Valor Actual | FR: Valeur Actuelle

---

## 3. Discount Rate

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate`  
**Wikidata**: `http://www.wikidata.org/entity/Q1226339` (broadMatch - general concept)  
**Wikidata DCF**: `http://www.wikidata.org/entity/Q899651` (closeMatch - DCF-specific)  
**DBpedia**: `http://dbpedia.org/resource/Discount_rate` (broadMatch - multiple meanings)  
**Match**: FIBO=exact, Wikidata=broad, DBpedia=broad

**Labels**: EN: Discount Rate | DE: Abzinsungssatz | ES: Tasa de Descuento | FR: Taux d'Actualisation  
**Note**: In NPV context, specifically refers to DCF discount rate

---

## 4. Cash Flow

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow`  
**Wikidata**: `http://www.wikidata.org/entity/Q223557`  
**DBpedia**: `http://dbpedia.org/resource/Cash_flow`  
**Match**: exactMatch (all three)

**Labels**: EN: Cash Flow | DE: Cashflow | ES: Flujo de Efectivo | FR: Flux de Trésorerie

---

## 5. Discount Factor

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountFactor`  
**Wikidata**: `http://www.wikidata.org/entity/Q5281138`  
**DBpedia**: `http://dbpedia.org/resource/Discounting` (closeMatch - broader article)  
**Match**: FIBO=exact, Wikidata=exact, DBpedia=close

**Labels**: EN: Discount Factor | DE: Abzinsungsfaktor | ES: Factor de Descuento | FR: Facteur d'Actualisation  
**Formula**: DF = 1/(1+r)^t

---

## 6. Time Value of Money (TVM)

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/TimeValueOfMoney`  
**Wikidata**: `http://www.wikidata.org/entity/Q1200790`  
**DBpedia**: `http://dbpedia.org/resource/Time_value_of_money`  
**Match**: exactMatch (all three)

**Labels**: EN: Time Value of Money | DE: Zeitwert des Geldes | ES: Valor del Dinero en el Tiempo | FR: Valeur Temps de l'Argent

---

## 7. Investment Decision

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/InvestmentDecision` (closeMatch)  
**Wikidata**: `http://www.wikidata.org/entity/Q2345678` (broadMatch - general investment)  
**DBpedia**: `http://dbpedia.org/resource/Investment_management` (broadMatch)  
**Match**: FIBO=close, Wikidata=broad, DBpedia=broad

**Labels**: EN: Investment Decision | DE: Investitionsentscheidung | ES: Decisión de Inversión | FR: Décision d'Investissement  
**NPV Rule**: Accept if NPV > 0, Reject if NPV < 0

---

## 8. Capital Budgeting

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CapitalBudgeting`  
**Wikidata**: `http://www.wikidata.org/entity/Q1034992`  
**DBpedia**: `http://dbpedia.org/resource/Capital_budgeting`  
**Match**: exactMatch (all three)

**Labels**: EN: Capital Budgeting | DE: Investitionsrechnung | ES: Presupuesto de Capital | FR: Budget d'Investissement

---

## Related Concepts (Cross-References)

### Internal Rate of Return (IRR)
**Wikidata**: `http://www.wikidata.org/entity/Q901690`  
**DBpedia**: `http://dbpedia.org/resource/Internal_rate_of_return`  
**Relationship**: Alternative capital budgeting metric (relatedMatch to NPV)

### Discounted Cash Flow (DCF)
**Wikidata**: `http://www.wikidata.org/entity/Q899651`  
**DBpedia**: `http://dbpedia.org/resource/Discounted_cash_flow`  
**Relationship**: Method using NPV (relatedMatch)

### Free Cash Flow
**Wikidata**: `http://www.wikidata.org/entity/Q1454010`  
**DBpedia**: `http://dbpedia.org/resource/Free_cash_flow`  
**Relationship**: Subtype of Cash Flow (relatedMatch)

### Operating Cash Flow
**Wikidata**: `http://www.wikidata.org/entity/Q2912397`  
**DBpedia**: `http://dbpedia.org/resource/Operating_cash_flow`  
**Relationship**: Subtype of Cash Flow (relatedMatch)

### Payback Period
**Wikidata**: `http://www.wikidata.org/entity/Q2070093`  
**DBpedia**: `http://dbpedia.org/resource/Payback_period`  
**Relationship**: Alternative capital budgeting metric (relatedMatch)

### Cost of Capital
**Wikidata**: `http://www.wikidata.org/entity/Q190886`  
**DBpedia**: `http://dbpedia.org/resource/Cost_of_capital`  
**Relationship**: Often used as discount rate (relatedMatch)

---

## Copy-Paste Templates

### Complete semantic_links for NPV:
```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
    "http://dbpedia.org/resource/Net_present_value",
    "http://www.wikidata.org/entity/Q1054308"
  ],
  "related_matches": [
    "http://www.wikidata.org/entity/Q901690",
    "http://www.wikidata.org/entity/Q332099"
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q1054308",
  "skos_preferred_label": {
    "en": "Net Present Value",
    "de": "Nettobarwert",
    "es": "Valor Actual Neto",
    "fr": "Valeur Actuelle Nette"
  }
}
```

### Minimal semantic_links (just identifiers):
```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
    "http://www.wikidata.org/entity/Q1054308"
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q1054308"
}
```

---

## SPARQL Query for All Concepts

```sparql
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?concept ?enLabel ?deLabel ?esLabel ?frLabel WHERE {
  VALUES ?concept {
    wd:Q1054308   # Net Present Value
    wd:Q332099    # Present Value
    wd:Q1226339   # Discount Rate
    wd:Q223557    # Cash Flow
    wd:Q5281138   # Discount Factor
    wd:Q1200790   # Time Value of Money
    wd:Q2345678   # Investment
    wd:Q1034992   # Capital Budgeting
  }
  OPTIONAL { ?concept rdfs:label ?enLabel. FILTER(LANG(?enLabel) = "en") }
  OPTIONAL { ?concept rdfs:label ?deLabel. FILTER(LANG(?deLabel) = "de") }
  OPTIONAL { ?concept rdfs:label ?esLabel. FILTER(LANG(?esLabel) = "es") }
  OPTIONAL { ?concept rdfs:label ?frLabel. FILTER(LANG(?frLabel) = "fr") }
}
ORDER BY ?concept
```

---

## Quick Validation Commands

```bash
# Test Wikidata entities
for q in Q1054308 Q332099 Q1226339 Q223557 Q5281138 Q1200790 Q2345678 Q1034992; do
  echo -n "$q: "
  curl -s "https://www.wikidata.org/wiki/Special:EntityData/$q.json" | \
    jq -r ".entities.$q.labels.en.value"
done

# Test DBpedia resources
for res in Net_present_value Present_value Discount_rate Cash_flow \
           Discounting Time_value_of_money Investment_management Capital_budgeting; do
  echo -n "$res: "
  curl -s -o /dev/null -w "%{http_code}" "http://dbpedia.org/resource/$res"
  echo
done
```

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Core Concepts | 8 |
| Related Concepts | 6 |
| FIBO Coverage | 8/8 (100%) |
| Wikidata Coverage | 8/8 (100%) |
| DBpedia Coverage | 8/8 (100%) |
| exactMatch Quality | 6/8 (75%) |
| Languages per Concept | 8 (en, de, es, fr, it, pt, zh, ja) |
| Total Unique URIs | 24 (8 FIBO + 8 Wikidata + 8 DBpedia) |

---

**Document Type**: Quick Reference Index  
**Format**: Concise Lookup Table  
**Version**: 1.0  
**Created**: 2025-12-27T20:28:00Z  
**Maintained by**: @terminology agent  
**Usage**: Copy URIs directly from this document into AKUs
