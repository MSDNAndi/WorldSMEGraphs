# Quick Start Guide: Adding Ontology Identifiers to AKUs

**For**: Knowledge graph creators, AKU developers, and AI agents  
**Purpose**: Step-by-step instructions for adding semantic links  
**Time**: ~5 minutes per AKU

---

## Quick Reference Card

### What You Need
1. **Concept name** (e.g., "Net Present Value")
2. **Domain context** (e.g., "economics/finance")
3. **Annotation templates** (see `aku-semantic-annotations.json`)
4. **Your AKU JSON file**

### Where to Add
Add `semantic_links` at the same level as `metadata` and `classification`:

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "economics:finance:npv:001",
  "metadata": { ... },
  "classification": { ... },
  "semantic_links": {
    "exact_matches": [...],
    "skos_preferred_label": {...}
  },
  "content": { ... }
}
```

---

## Step-by-Step Instructions

### Step 1: Identify Your Concept

Determine which financial concept your AKU represents:
- Net Present Value (NPV)
- Present Value (PV)
- Discount Rate
- Cash Flow
- Discount Factor
- Time Value of Money
- Investment Decision
- Capital Budgeting

### Step 2: Copy the Appropriate Template

Open `aku-semantic-annotations.json` and copy the `semantic_links` object for your concept.

**Example for NPV:**
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

### Step 3: Paste into Your AKU

Insert the `semantic_links` object into your AKU JSON structure:

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "economics:finance:npv:net-present-value:001",
  "metadata": {
    "version": "2.0.0",
    "created": "2025-12-27T20:00:00.000Z",
    "contributors": ["terminology-agent"],
    "status": "validated"
  },
  "classification": {
    "domain_path": "economics/bwl/finance/valuation/npv",
    "type": "definition",
    "difficulty": "intermediate"
  },
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
  "content": {
    "definition": "The present value of expected cash flows minus the initial investment..."
  }
}
```

### Step 4: Validate JSON Syntax

Use a JSON validator to ensure proper formatting:

```bash
# Using Python
python -m json.tool your-aku.json

# Using jq
jq . your-aku.json

# Using Node.js
node -e "JSON.parse(require('fs').readFileSync('your-aku.json'))"
```

### Step 5: Verify URIs (Optional but Recommended)

Check that the ontology URIs are correct:

```bash
# Check Wikidata
curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q1054308.json" | jq '.entities.Q1054308.labels.en.value'
# Should return: "net present value"

# Check DBpedia (HTTP 200 = exists)
curl -s -o /dev/null -w "%{http_code}" "http://dbpedia.org/resource/Net_present_value"
# Should return: 200
```

---

## Common Patterns

### Pattern 1: Core Financial Concept (Most Common)

Use for: NPV, PV, Cash Flow, Capital Budgeting

```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/...",
    "http://dbpedia.org/resource/...",
    "http://www.wikidata.org/entity/Q..."
  ],
  "related_matches": [
    "http://www.wikidata.org/entity/Q..."  // Related concepts
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q...",
  "skos_preferred_label": {
    "en": "...",
    "de": "...",
    "es": "...",
    "fr": "..."
  }
}
```

### Pattern 2: Ambiguous Terms (Requires Care)

Use for: Discount Rate (multiple meanings)

```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate"
  ],
  "close_matches": [
    "http://www.wikidata.org/entity/Q899651"  // DCF-specific
  ],
  "broad_matches": [
    "http://dbpedia.org/resource/Discount_rate",  // General term
    "http://www.wikidata.org/entity/Q1226339"     // Includes central bank rate
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q1226339",
  "skos_definition": {
    "en": "The interest rate used to discount future cash flows...",
    "scope_note": "In NPV context, specifically refers to DCF discount rate"
  }
}
```

### Pattern 3: Concepts Without FIBO

Use for: Investment Decision (not strongly defined in FIBO)

```json
"semantic_links": {
  "close_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/InvestmentDecision"
  ],
  "broad_matches": [
    "http://dbpedia.org/resource/Investment_management",
    "http://www.wikidata.org/entity/Q2345678"
  ],
  "related_matches": [
    "http://www.wikidata.org/entity/Q1054308"  // NPV as decision criterion
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q2345678"
}
```

---

## Match Type Decision Guide

### Use `exact_matches` when:
- ✅ Concept definitions are identical
- ✅ Scope is the same
- ✅ URIs point to the same semantic concept
- ✅ Terms are fully interchangeable

**Example**: FIBO NetPresentValue ≡ Wikidata Q1054308 ≡ DBpedia Net_present_value

### Use `close_matches` when:
- ✅ Concepts are highly similar
- ✅ Minor differences in scope or emphasis
- ✅ Generally interchangeable in practice
- ⚠️ Not identical in formal reasoning

**Example**: FIBO DiscountFactor ≈ DBpedia Discounting (broader article)

### Use `broad_matches` when:
- ✅ Target concept is broader/more general
- ✅ Source is a specific case of target
- ⚠️ Cannot always substitute
- ⚠️ Target includes additional meanings

**Example**: NPV Discount Rate → General Discount Rate (includes monetary policy meaning)

### Use `related_matches` when:
- ✅ Concepts are related but distinct
- ⚠️ Not substitutable
- ✅ Useful for navigation and discovery

**Example**: NPV ⟷ IRR (both are capital budgeting methods)

---

## Troubleshooting

### Problem: JSON Syntax Error

**Symptom**: Parser fails, invalid JSON
**Solution**: 
- Check for missing commas between objects
- Verify all brackets/braces match
- Ensure quotes are properly closed
- Use a JSON linter

### Problem: Wrong Ontology URI

**Symptom**: 404 error when checking URI
**Solution**:
- Verify against `ONTOLOGY-IDENTIFIERS.md`
- Check for typos in Q-numbers (Wikidata)
- Ensure correct FIBO module path
- Use underscore not hyphen in DBpedia

### Problem: Multilingual Labels Missing

**Symptom**: Only English label present
**Solution**:
- Copy full label set from `aku-semantic-annotations.json`
- Minimum: en, de, es, fr
- Extended: it, pt, zh, ja
- Verify labels match Wikidata

### Problem: Uncertain About Match Type

**Symptom**: Don't know if exactMatch or closeMatch
**Solution**:
- Read definitions from both ontologies
- If definitions are identical → exactMatch
- If minor differences → closeMatch
- If significantly different scope → broadMatch
- When in doubt, use closeMatch

---

## Quality Checklist

Before finalizing your AKU, verify:

- [ ] `semantic_links` section present
- [ ] At least one `exact_matches` entry
- [ ] FIBO URI included (if concept exists in FIBO)
- [ ] Wikidata Q-number included
- [ ] `skos_concept` points to primary identifier (usually Wikidata)
- [ ] `skos_preferred_label` has at least 4 languages (en, de, es, fr)
- [ ] Match types are appropriate
- [ ] All URIs are syntactically correct
- [ ] JSON is valid (no syntax errors)
- [ ] Related concepts linked in `related_matches`

---

## Advanced: Adding Custom Concepts

If your concept is **not** in the provided templates:

### 1. Research Ontology Identifiers

```bash
# Search Wikidata
https://www.wikidata.org/w/index.php?search=your+concept

# Search DBpedia
http://lookup.dbpedia.org/api/search?QueryString=your+concept

# Search FIBO (manual)
https://spec.edmcouncil.org/fibo/
```

### 2. Verify Match Quality

- Read the full definitions
- Check scope and usage
- Classify match type appropriately
- Document any ambiguities

### 3. Follow Template Structure

```json
"semantic_links": {
  "exact_matches": [
    // Only truly identical concepts
  ],
  "close_matches": [
    // Highly similar, minor differences
  ],
  "broad_matches": [
    // Target is broader than source
  ],
  "related_matches": [
    // Related but distinct concepts
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q...",
  "skos_preferred_label": {
    "en": "...",
    "de": "...",
    "es": "...",
    "fr": "..."
  },
  "skos_definition": {
    "en": "...",
    "source": "...",
    "scope_note": "..." // If needed for clarity
  }
}
```

---

## Examples: Before and After

### Before (No Semantic Links)

```json
{
  "@context": "aku-v2",
  "@id": "economics:finance:npv:001",
  "metadata": {
    "version": "1.0.0",
    "created": "2025-12-20T10:00:00.000Z"
  },
  "content": {
    "definition": "NPV is the sum of discounted cash flows..."
  }
}
```

### After (With Semantic Links)

```json
{
  "@context": "aku-v2",
  "@id": "economics:finance:npv:001",
  "metadata": {
    "version": "2.0.0",
    "created": "2025-12-20T10:00:00.000Z",
    "updated": "2025-12-27T20:22:00.000Z"
  },
  "semantic_links": {
    "exact_matches": [
      "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
      "http://dbpedia.org/resource/Net_present_value",
      "http://www.wikidata.org/entity/Q1054308"
    ],
    "related_matches": [
      "http://www.wikidata.org/entity/Q901690"
    ],
    "skos_concept": "http://www.wikidata.org/entity/Q1054308",
    "skos_preferred_label": {
      "en": "Net Present Value",
      "de": "Nettobarwert",
      "es": "Valor Actual Neto",
      "fr": "Valeur Actuelle Nette"
    }
  },
  "content": {
    "definition": "NPV is the sum of discounted cash flows..."
  }
}
```

---

## Integration with Other Systems

### For Knowledge Graphs
- Use `skos_concept` as the primary node identifier
- Link nodes via `related_matches`
- Traverse hierarchies via FIBO structure

### For Multilingual Rendering
- Use `skos_preferred_label` for translations
- Fall back to `skos_alt_label` for synonyms
- Include `skos_definition` for context

### For Search and Discovery
- Index all URIs in `exact_matches`, `close_matches`, `broad_matches`
- Use `related_matches` for "see also" suggestions
- Leverage Wikidata for related concept exploration

---

## Getting Help

### Resources
- **Full Reference**: `ONTOLOGY-IDENTIFIERS.md`
- **Validation Guide**: `validation-reference.md`
- **JSON Templates**: `aku-semantic-annotations.json`

### Contact
- **Agent**: @terminology
- **Related Agents**: @semantic-harmonization, @ontology, @verification

### Common Questions

**Q: Do I need all three ontologies (FIBO, DBpedia, Wikidata)?**  
A: Ideally yes. FIBO is primary for finance, Wikidata for multilingual support, DBpedia for Wikipedia integration.

**Q: What if my concept doesn't exist in FIBO?**  
A: Use Wikidata and DBpedia. Leave FIBO out or use `close_matches`/`broad_matches` for nearest FIBO concept.

**Q: How many related_matches should I include?**  
A: 2-5 is typical. Include the most directly related concepts (e.g., NPV → IRR, Payback Period).

**Q: Can I use multiple skos_concept identifiers?**  
A: No, use a single primary identifier (typically Wikidata). Others go in appropriate match arrays.

---

**Version**: 1.0  
**Created**: 2025-12-27T20:22:00Z  
**Maintained by**: @terminology agent  
**Status**: Active
