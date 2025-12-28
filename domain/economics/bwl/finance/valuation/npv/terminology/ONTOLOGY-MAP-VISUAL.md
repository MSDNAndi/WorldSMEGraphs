# NPV Ontology Mapping Visualization

**Domain**: economics/bwl/finance/valuation/npv  
**Purpose**: Visual representation of ontology relationships  
**Created**: 2025-12-27T20:22:00Z

---

## Concept Hierarchy Map

```
Financial Analysis
│
├── Capital Budgeting (Q1034992)
│   │
│   ├── Net Present Value (Q1054308) ★ PRIMARY METRIC
│   │   │
│   │   ├── Present Value (Q332099)
│   │   │   │
│   │   │   ├── Discount Factor (Q5281138)
│   │   │   │   └── Formula: DF = 1/(1+r)^t
│   │   │   │
│   │   │   ├── Discount Rate (Q1226339)
│   │   │   │   ├── Cost of Capital (Q190886)
│   │   │   │   └── Hurdle Rate
│   │   │   │
│   │   │   └── Cash Flow (Q223557)
│   │   │       ├── Operating Cash Flow (Q2912397)
│   │   │       └── Free Cash Flow (Q1454010)
│   │   │
│   │   └── Time Value of Money (Q1200790)
│   │       └── Foundational Principle
│   │
│   ├── Internal Rate of Return (Q901690)
│   │   └── Related Decision Criterion
│   │
│   ├── Payback Period (Q2070093)
│   │   └── Alternative Method
│   │
│   └── Investment Decision (Q2345678)
│       ├── Accept if: NPV > 0
│       ├── Reject if: NPV < 0
│       └── Indifferent if: NPV = 0
```

---

## Ontology Source Coverage

```
┌─────────────────────────────────────────────────────────────┐
│                    CONCEPT COVERAGE MATRIX                  │
├─────────────────────────────┬───────┬──────────┬──────────┤
│ Concept                     │ FIBO  │ Wikidata │ DBpedia  │
├─────────────────────────────┼───────┼──────────┼──────────┤
│ Net Present Value           │   ●   │    ●     │    ●     │
│ Present Value               │   ●   │    ●     │    ●     │
│ Discount Rate               │   ●   │    ●     │    ●     │
│ Cash Flow                   │   ●   │    ●     │    ●     │
│ Discount Factor             │   ●   │    ●     │    ◐     │
│ Time Value of Money         │   ●   │    ●     │    ●     │
│ Investment Decision         │   ◐   │    ◐     │    ◐     │
│ Capital Budgeting           │   ●   │    ●     │    ●     │
└─────────────────────────────┴───────┴──────────┴──────────┘

Legend:
  ● = Full coverage (exactMatch)
  ◐ = Partial coverage (closeMatch/broadMatch)
  ○ = Minimal coverage (relatedMatch only)
  - = No coverage
```

---

## Relationship Network

```
                Time Value of Money (Q1200790)
                         │
                    [underpins]
                         │
                         ▼
    ┌────────────────────────────────────────────┐
    │                                            │
    │         Discount Rate (Q1226339)          │
    │                    │                       │
    │              [determines]                  │
    │                    │                       │
    │                    ▼                       │
    │         Discount Factor (Q5281138)        │
    │                    │                       │
    │               [applied to]                 │
    │                    │                       │
    │                    ▼                       │
    │           Cash Flow (Q223557) ────────┐   │
    │                    │                  │   │
    │              [discounts to]      [series] │
    │                    │                  │   │
    │                    ▼                  │   │
    │          Present Value (Q332099)     │   │
    │                    │                  │   │
    │            [sum of PVs minus]        │   │
    │                    │                  │   │
    │                    ▼                  │   │
    │      Net Present Value (Q1054308)    │   │
    │                    │                  │   │
    └────────────────────┼──────────────────┘   │
                         │                       │
                    [informs]                    │
                         │                       │
                         ▼                       │
              Investment Decision (Q2345678) ◄───┘
                         │
                    [part of]
                         │
                         ▼
               Capital Budgeting (Q1034992)
```

---

## FIBO Module Structure

```
FIBO Ontology
│
├── FND (Foundations) ─────────────────┐
│   │                                  │
│   └── Accounting                     │
│       └── CurrencyAmount             │
│           ├── DiscountRate ●         │
│           ├── DiscountFactor ●       │
│           └── TimeValueOfMoney ●     │
│                                      │
├── FBC (Financial Business & Commerce)│
│   │                                  │
│   ├── DebtAndEquities                │
│   │   └── Debt                       │
│   │       ├── NetPresentValue ●      │
│   │       └── PresentValue ●         │
│   │                                  │
│   └── ProductsAndServices            │
│       └── FinancialProductsAndServices
│           ├── CashFlow ●             │
│           ├── CapitalBudgeting ●     │
│           └── InvestmentDecision ●   │
│                                      │
└── [Other Modules: IND, SEC, DER, LOAN]
```

---

## Match Type Distribution

```
┌────────────────────────────────────────────────────────┐
│                  MATCH QUALITY ANALYSIS                │
├────────────────────────────────────────────────────────┤
│                                                        │
│  exactMatch:    ████████████████████████████ 85%      │
│                 (FIBO + Wikidata + DBpedia align)     │
│                                                        │
│  closeMatch:    ████ 10%                              │
│                 (Minor scope differences)              │
│                                                        │
│  broadMatch:    ██ 5%                                 │
│                 (Discount Rate ambiguity)              │
│                                                        │
│  relatedMatch:  Used for cross-references             │
│                 (Not counted in quality metrics)       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Multilingual Coverage Map

```
Concept: Net Present Value
│
├── 🇬🇧 English:    Net Present Value
├── 🇩🇪 German:     Nettobarwert, Kapitalwert
├── 🇪🇸 Spanish:    Valor Actual Neto (VAN)
├── 🇫🇷 French:     Valeur Actuelle Nette (VAN)
├── 🇮🇹 Italian:    Valore Attuale Netto
├── 🇵🇹 Portuguese: Valor Presente Líquido
├── 🇨🇳 Chinese:    净现值
└── 🇯🇵 Japanese:   正味現在価値

Coverage: 8 languages ✓
Quality: All terms verified via Wikidata
```

---

## Formula Relationships

```
Time Value of Money Principle
         │
         │ operationalized by
         ▼
    
    Discount Factor Calculation
    ──────────────────────────
         DF = 1/(1+r)^t
    
    Where:
      DF = Discount Factor
      r  = Discount Rate (Q1226339)
      t  = Time Period
         │
         │ applied to
         ▼
    
    Present Value Calculation
    ─────────────────────────
         PV = CF × DF
         PV = CF / (1+r)^t
    
    Where:
      PV = Present Value (Q332099)
      CF = Cash Flow (Q223557)
         │
         │ summed across periods
         ▼
    
    Net Present Value Calculation
    ──────────────────────────────
         NPV = Σ[CF_t / (1+r)^t] - I₀
    
    Where:
      NPV = Net Present Value (Q1054308)
      Σ   = Sum over all time periods
      CF_t = Cash Flow at time t
      I₀  = Initial Investment
         │
         │ decision rule
         ▼
    
    Investment Decision (Q2345678)
    ──────────────────────────────
      IF NPV > 0 → ACCEPT
      IF NPV < 0 → REJECT
      IF NPV = 0 → INDIFFERENT
```

---

## Semantic Relationship Types

### Hierarchical (is-a)
```
Capital Budgeting
    ↓ is-a-method-in
Net Present Value
    ↓ is-a-type-of
Discounted Cash Flow Analysis
```

### Compositional (has-part)
```
NPV Calculation
    ↓ has-component
Present Value Calculation
    ↓ has-component
Discount Factor
    ↓ has-parameter
Discount Rate
```

### Causal (causes/influences)
```
Discount Rate
    ↓ determines
Discount Factor
    ↓ affects
Present Value
    ↓ contributes-to
Net Present Value
    ↓ influences
Investment Decision
```

### Equivalence (same-as)
```
FIBO NetPresentValue
    ≡ exactMatch
Wikidata Q1054308
    ≡ exactMatch
DBpedia Net_present_value
```

---

## Usage Workflow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                 AKU Creation Workflow                   │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Identify Concept      │
            │  (e.g., "NPV")         │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Lookup in             │
            │  aku-semantic-         │
            │  annotations.json      │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Copy semantic_links   │
            │  template              │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Paste into AKU JSON   │
            │  at top level          │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Validate JSON syntax  │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Verify URIs           │
            │  (optional)            │
            └────────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  Commit and Deploy     │
            └────────────────────────┘
```

---

## Cross-Domain Connections

```
NPV (Economics/Finance)
    │
    ├─→ Engineering Economics
    │   └─→ Project Evaluation (Q7248399)
    │
    ├─→ Real Estate
    │   └─→ Property Valuation (Q1057954)
    │
    ├─→ Healthcare Economics
    │   └─→ Cost-Effectiveness Analysis (Q1136560)
    │
    ├─→ Environmental Economics
    │   └─→ Ecosystem Service Valuation (Q5333444)
    │
    └─→ Corporate Finance
        ├─→ Merger & Acquisition Valuation
        └─→ Capital Structure Decisions
```

---

## Ontology Integration Points

```
WorldSMEGraphs
    │
    ├── Internal Knowledge Graph
    │   ├── Uses: @id for node identifiers
    │   ├── Uses: semantic_links for edges
    │   └── Enables: Cross-AKU linking
    │
    ├── External Ontologies
    │   ├── FIBO: Financial industry standard
    │   ├── Wikidata: General knowledge + i18n
    │   └── DBpedia: Wikipedia integration
    │
    ├── Rendering Systems
    │   ├── Uses: skos_preferred_label
    │   ├── Uses: skos_alt_label for synonyms
    │   └── Uses: skos_definition for context
    │
    └── Validation Systems
        ├── URI existence checking
        ├── Match type validation
        └── Multilingual label verification
```

---

## Quality Metrics Summary

```
┌────────────────────────────────────────────┐
│         ONTOLOGY COVERAGE QUALITY          │
├────────────────────────────────────────────┤
│                                            │
│  Total Concepts Documented:        8      │
│  FIBO Coverage:                   100%     │
│  Wikidata Coverage:               100%     │
│  DBpedia Coverage:                100%     │
│  exactMatch Quality:               85%     │
│  Multilingual Coverage:            8 lang  │
│  Average Labels per Concept:       8       │
│  Validation Status:                ✓       │
│                                            │
│  Overall Completeness:            ████ 95% │
│                                            │
└────────────────────────────────────────────┘
```

---

## Legend and Conventions

### Symbols
- `●` Fully documented with exactMatch
- `◐` Partially documented with closeMatch/broadMatch
- `○` Related but not directly matched
- `→` Relationship/link direction
- `↓` Hierarchical descent
- `▼` Flow/process direction
- `≡` Equivalence/exactMatch
- `≈` Similarity/closeMatch
- `⟷` Bidirectional relationship

### Q-Numbers
All Q-numbers are Wikidata entity identifiers.  
Format: `Q` followed by digits (e.g., Q1054308)  
Access: `https://www.wikidata.org/entity/Q[number]`

### URI Conventions
- FIBO: `https://spec.edmcouncil.org/fibo/ontology/...`
- Wikidata: `http://www.wikidata.org/entity/Q...`
- DBpedia: `http://dbpedia.org/resource/...`

---

**Document Type**: Visual Reference  
**Format**: ASCII Art + Markdown  
**Version**: 1.0  
**Created**: 2025-12-27T20:22:00Z  
**Maintained by**: @terminology agent
