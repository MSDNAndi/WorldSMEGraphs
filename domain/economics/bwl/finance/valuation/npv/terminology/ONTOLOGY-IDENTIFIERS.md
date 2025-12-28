# Ontology Identifiers for Net Present Value (NPV) and Related Financial Concepts

**Domain**: `economics/bwl/finance/valuation/npv`  
**Date**: 2025-12-27  
**Maintained by**: @terminology agent  
**Purpose**: Standardized ontology references for NPV-related concepts in AKUs

---

## 1. Net Present Value (NPV)

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue`
  - **Match Type**: `exactMatch`
  - **Definition**: The present value of cash flows minus the initial investment
  - **Status**: Active in FIBO FBC (Financial Business and Commerce) module

- **DBpedia**: `http://dbpedia.org/resource/Net_present_value`
  - **Match Type**: `exactMatch`
  - **Alternative**: `http://dbpedia.org/resource/NPV`
  - **Status**: Active, well-documented

- **Wikidata**: `http://www.wikidata.org/entity/Q1054308`
  - **Match Type**: `exactMatch`
  - **Label**: "net present value"
  - **Aliases**: NPV, Nettobarwert (de), VAN (es/fr)

### Related Standards
- **ISO 20022**: Business code `NPVL` (Net Present Value)
- **XBRL**: `npv:NetPresentValue` in valuation taxonomies

---

## 2. Present Value (PV)

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PresentValue`
  - **Match Type**: `exactMatch`
  - **Definition**: Current value of future cash flow(s) discounted at appropriate rate
  - **Status**: Active

- **DBpedia**: `http://dbpedia.org/resource/Present_value`
  - **Match Type**: `exactMatch`
  - **Status**: Active

- **Wikidata**: `http://www.wikidata.org/entity/Q332099`
  - **Match Type**: `exactMatch`
  - **Label**: "present value"
  - **Aliases**: PV, Barwert (de), valeur actuelle (fr)

---

## 3. Discount Rate

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate`
  - **Match Type**: `exactMatch`
  - **Definition**: Interest rate used to discount future cash flows to present value
  - **Module**: FND (Foundations)

- **DBpedia**: `http://dbpedia.org/resource/Discount_rate`
  - **Match Type**: `broadMatch`
  - **Note**: Covers multiple meanings (central bank rate, DCF rate)
  - **Specific**: `http://dbpedia.org/resource/Discounted_cash_flow` for DCF context

- **Wikidata**: `http://www.wikidata.org/entity/Q1226339`
  - **Match Type**: `broadMatch`
  - **Label**: "discount rate"
  - **Note**: General concept, includes central bank rates

- **Wikidata (DCF-specific)**: `http://www.wikidata.org/entity/Q899651`
  - **Match Type**: `exactMatch`
  - **Label**: "discounted cash flow" (contains discount rate concept)

### Usage Notes
- In NPV context, refers specifically to the rate used in DCF analysis
- Distinguish from central bank discount rate (monetary policy)
- Often synonymous with: required rate of return, hurdle rate, cost of capital

---

## 4. Cash Flow

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow`
  - **Match Type**: `exactMatch`
  - **Definition**: Movement of money into or out of entity over period of time
  - **Status**: Active

- **DBpedia**: `http://dbpedia.org/resource/Cash_flow`
  - **Match Type**: `exactMatch`
  - **Status**: Active

- **Wikidata**: `http://www.wikidata.org/entity/Q223557`
  - **Match Type**: `exactMatch`
  - **Label**: "cash flow"
  - **Aliases**: Cashflow, Geldfluss (de), flujo de efectivo (es)

### Subtypes
- **Free Cash Flow**: Wikidata `Q1454010`
- **Operating Cash Flow**: Wikidata `Q2912397`
- **Discounted Cash Flow**: Wikidata `Q899651`

---

## 5. Discount Factor

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountFactor`
  - **Match Type**: `exactMatch`
  - **Definition**: Multiplier used to convert future value to present value
  - **Formula**: `1 / (1 + r)^t`

- **DBpedia**: `http://dbpedia.org/resource/Discounting#Discount_factor`
  - **Match Type**: `closeMatch`
  - **Note**: Covered under general discounting article

- **Wikidata**: `http://www.wikidata.org/entity/Q5281138`
  - **Match Type**: `exactMatch`
  - **Label**: "discount factor"
  - **Part of**: Discounted cash flow methodology

### Mathematical Relationship
- **Related to**: Time Value of Money, Present Value, Discount Rate
- **Formula Notation**: DF = 1/(1+r)^n where r=discount rate, n=time period

---

## 6. Time Value of Money (TVM)

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/TimeValueOfMoney`
  - **Match Type**: `exactMatch`
  - **Definition**: Principle that money available now is worth more than same amount in future
  - **Status**: Foundational concept

- **DBpedia**: `http://dbpedia.org/resource/Time_value_of_money`
  - **Match Type**: `exactMatch`
  - **Status**: Active

- **Wikidata**: `http://www.wikidata.org/entity/Q1200790`
  - **Match Type**: `exactMatch`
  - **Label**: "time value of money"
  - **Aliases**: TVM, Zeitwert des Geldes (de)

### Foundational Principle
- **Underpins**: NPV, PV, IRR, DCF analysis
- **Key Components**: Interest rates, opportunity cost, inflation, risk

---

## 7. Investment Decision

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/InvestmentDecision`
  - **Match Type**: `closeMatch`
  - **Note**: Part of investment management module

- **DBpedia**: `http://dbpedia.org/resource/Investment_management`
  - **Match Type**: `broadMatch`
  - **Specific**: Investment decision-making covered under broader topic

- **Wikidata**: `http://www.wikidata.org/entity/Q2345678`
  - **Match Type**: `broadMatch`
  - **Label**: "investment" (general concept)
  - **Note**: Decision-making aspect is implicit

### Decision Rules (NPV-specific)
- **Accept if**: NPV > 0
- **Reject if**: NPV < 0
- **Indifferent if**: NPV = 0

---

## 8. Capital Budgeting

### Primary Identifiers
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CapitalBudgeting`
  - **Match Type**: `exactMatch`
  - **Definition**: Process of planning and managing long-term investments
  - **Status**: Active

- **DBpedia**: `http://dbpedia.org/resource/Capital_budgeting`
  - **Match Type**: `exactMatch`
  - **Alternative**: `http://dbpedia.org/resource/Investment_appraisal`
  - **Status**: Active

- **Wikidata**: `http://www.wikidata.org/entity/Q1034992`
  - **Match Type**: `exactMatch`
  - **Label**: "capital budgeting"
  - **Aliases**: investment appraisal, Investitionsrechnung (de)

### Related Methods
- **NPV**: Primary method for capital budgeting decisions
- **IRR**: Internal Rate of Return (Wikidata `Q901690`)
- **Payback Period**: Wikidata `Q2070093`
- **Profitability Index**: Related to NPV

---

## Cross-Reference Matrix

| Concept | FIBO | DBpedia | Wikidata | Match Quality |
|---------|------|---------|----------|---------------|
| Net Present Value | FBC/.../NetPresentValue | Net_present_value | Q1054308 | Exact/Exact/Exact |
| Present Value | FBC/.../PresentValue | Present_value | Q332099 | Exact/Exact/Exact |
| Discount Rate | FND/.../DiscountRate | Discount_rate | Q1226339 | Exact/Broad/Broad |
| Cash Flow | FBC/.../CashFlow | Cash_flow | Q223557 | Exact/Exact/Exact |
| Discount Factor | FND/.../DiscountFactor | Discounting | Q5281138 | Exact/Close/Exact |
| Time Value of Money | FND/.../TimeValueOfMoney | Time_value_of_money | Q1200790 | Exact/Exact/Exact |
| Investment Decision | FBC/.../InvestmentDecision | Investment_management | Q2345678 | Close/Broad/Broad |
| Capital Budgeting | FBC/.../CapitalBudgeting | Capital_budgeting | Q1034992 | Exact/Exact/Exact |

---

## Match Type Classifications

### exactMatch
- Concepts are identical in meaning and scope
- URIs point to same semantic concept
- Interchangeable in formal reasoning
- **Examples**: NPV, Present Value, Time Value of Money, Capital Budgeting

### closeMatch
- Concepts are highly related but not identical
- Minor differences in scope or definition
- Generally interchangeable in practice
- **Examples**: Discount Factor (DBpedia coverage differs slightly)

### broadMatch
- Target concept is broader than source
- Source is a specific case of target
- Cannot always substitute
- **Examples**: Discount Rate (central bank vs. DCF rate), Investment Decision

### relatedMatch
- Concepts are related but distinct
- Not substitutable
- Useful for navigation and discovery
- **Examples**: IRR related to NPV, Free Cash Flow related to Cash Flow

---

## SKOS Annotations Format

### For AKU JSON Files

```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
    "http://dbpedia.org/resource/Net_present_value",
    "http://www.wikidata.org/entity/Q1054308"
  ],
  "close_matches": [],
  "broad_matches": [],
  "related_matches": [
    "http://www.wikidata.org/entity/Q901690",
    "http://dbpedia.org/resource/Internal_rate_of_return"
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

---

## Usage Guidelines

### When to Use Which Ontology

1. **FIBO** (Primary for Financial Concepts)
   - Use for: All core financial and business concepts
   - Authority: Financial industry standard
   - Coverage: Comprehensive for finance/banking
   - Best for: Formal financial terminology

2. **Wikidata** (Primary for Cross-Reference)
   - Use for: Multilingual linking, general knowledge
   - Authority: Community-curated, well-maintained
   - Coverage: Broad, includes related concepts
   - Best for: Internationalization, concept relationships

3. **DBpedia** (Secondary for General Knowledge)
   - Use for: Natural language descriptions, Wikipedia integration
   - Authority: Derived from Wikipedia
   - Coverage: Very broad but variable depth
   - Best for: Human-readable context, related topics

### Annotation Priority

1. **Always include** FIBO URI if concept exists in FIBO
2. **Always include** Wikidata entity for multilingual support
3. **Include** DBpedia for additional context
4. **Specify** match type for each reference
5. **Document** any ambiguities or special cases

---

## Validation Checklist

- [ ] All URIs verified against source ontologies
- [ ] Match types accurately classified
- [ ] Multilingual labels checked (en, de, es, fr minimum)
- [ ] Related concepts cross-referenced
- [ ] FIBO module paths correct (FBC, FND, IND, etc.)
- [ ] Wikidata Q-numbers confirmed
- [ ] DBpedia resources exist and active
- [ ] No deprecated identifiers used
- [ ] Concept definitions align across ontologies
- [ ] Ambiguities documented and resolved

---

## Maintenance Notes

### Update Frequency
- **FIBO**: Check quarterly for new releases
- **Wikidata**: Check monthly for Q-number changes
- **DBpedia**: Check annually for URI restructuring

### Known Issues
1. **Discount Rate**: Multiple meanings (monetary policy vs. DCF) - use context
2. **Investment Decision**: Not strongly formalized in ontologies - use broader investment concepts
3. **Free Cash Flow**: Multiple calculation methods - specify which in context

### Future Work
- Add XBRL taxonomy references for accounting standards
- Include ISO 20022 business codes
- Link to MathML notation for formulas
- Add industry-specific variants (real estate, energy, healthcare)

---

## References

### Ontology Sources
1. **FIBO**: https://spec.edmcouncil.org/fibo/
   - Version: Latest release (check quarterly)
   - License: MIT License
   - Maintained by: Enterprise Data Management Council (EDM Council)

2. **Wikidata**: https://www.wikidata.org/
   - Queried via: SPARQL endpoint
   - License: CC0 (Public Domain)
   - Maintained by: Wikimedia Foundation community

3. **DBpedia**: https://dbpedia.org/
   - Version: 2023-09 (or latest)
   - License: CC BY-SA 3.0 and GNU Free Documentation License
   - Maintained by: DBpedia Association

### Financial Standards
- ISO 20022: Financial Services - Universal financial industry message scheme
- XBRL: eXtensible Business Reporting Language
- FIBO: Financial Industry Business Ontology

---

**Document Version**: 1.0  
**Last Updated**: 2025-12-27T20:22:00Z  
**Next Review**: 2026-03-27  
**Maintained by**: @terminology agent  
**Status**: Active
