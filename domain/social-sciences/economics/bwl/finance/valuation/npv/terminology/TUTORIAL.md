# Tutorial: Adding Semantic Annotations to Your NPV AKU

**Estimated Time**: 10 minutes  
**Difficulty**: Beginner  
**Prerequisites**: Basic JSON knowledge

---

## Learning Objectives

By the end of this tutorial, you will be able to:
- ✅ Find the right ontology identifiers for your concept
- ✅ Copy and paste semantic annotations into your AKU
- ✅ Validate your semantic annotations
- ✅ Understand match types and when to use them
- ✅ Add multilingual labels correctly

---

## Tutorial Overview

We'll walk through adding semantic annotations to a simple NPV definition AKU step by step.

**What we're building**: A minimal but complete AKU with proper semantic annotations.

---

## Step 1: Start with Your Basic AKU (2 minutes)

Let's say you have this basic NPV definition AKU:

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "economics:finance:npv:tutorial-example",
  "metadata": {
    "version": "1.0.0",
    "created": "2025-12-27T20:40:00.000Z",
    "status": "draft"
  },
  "classification": {
    "domain_path": "economics/bwl/finance/valuation/npv",
    "type": "definition",
    "difficulty": "intermediate"
  },
  "content": {
    "definition": {
      "primary": "Net Present Value (NPV) is the sum of discounted cash flows minus the initial investment."
    }
  }
}
```

**Notice**: No semantic annotations yet! Let's add them.

---

## Step 2: Find Your Concept (1 minute)

Our AKU is about "Net Present Value (NPV)".

**Quick lookup**: Open `terminology/INDEX.md` and search for "Net Present Value".

You'll find:
```markdown
## 1. Net Present Value (NPV)

**FIBO**: `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue`  
**Wikidata**: `http://www.wikidata.org/entity/Q1054308`  
**DBpedia**: `http://dbpedia.org/resource/Net_present_value`  
**Match**: exactMatch (all three)
```

Great! We have 3 URIs and they're all exact matches.

---

## Step 3: Copy the Template (1 minute)

Open `terminology/aku-semantic-annotations.json` and find the "net_present_value" section.

You'll see:
```json
"net_present_value": {
  "concept": "Net Present Value (NPV)",
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
      "http://dbpedia.org/resource/Internal_rate_of_return",
      "http://www.wikidata.org/entity/Q332099",
      "http://dbpedia.org/resource/Present_value"
    ],
    "skos_concept": "http://www.wikidata.org/entity/Q1054308",
    "skos_preferred_label": {
      "en": "Net Present Value",
      "de": "Nettobarwert",
      "es": "Valor Actual Neto",
      "fr": "Valeur Actuelle Nette",
      "it": "Valore Attuale Netto",
      "pt": "Valor Presente Líquido",
      "zh": "净现值",
      "ja": "正味現在価値"
    },
    "skos_alt_label": {
      "en": ["NPV", "net present worth"],
      "de": ["Kapitalwert", "NBW"],
      "es": ["VAN", "VPN"],
      "fr": ["VAN"]
    },
    "skos_definition": {
      "en": "The present value of expected cash flows minus the initial investment cost...",
      "source": "FIBO, Wikidata Q1054308"
    }
  }
}
```

**Copy the entire `semantic_links` object** (not the wrapper).

---

## Step 4: Paste Into Your AKU (1 minute)

Add the `semantic_links` section at the **same level** as `metadata`, `classification`, and `content`:

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "economics:finance:npv:tutorial-example",
  "metadata": {
    "version": "1.0.0",
    "created": "2025-12-27T20:40:00.000Z",
    "status": "draft"
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
    "related_matches": [
      "http://www.wikidata.org/entity/Q901690",
      "http://dbpedia.org/resource/Internal_rate_of_return",
      "http://www.wikidata.org/entity/Q332099",
      "http://dbpedia.org/resource/Present_value"
    ],
    "skos_concept": "http://www.wikidata.org/entity/Q1054308",
    "skos_preferred_label": {
      "en": "Net Present Value",
      "de": "Nettobarwert",
      "es": "Valor Actual Neto",
      "fr": "Valeur Actuelle Nette",
      "it": "Valore Attuale Netto",
      "pt": "Valor Presente Líquido",
      "zh": "净现值",
      "ja": "正味現在価値"
    },
    "skos_alt_label": {
      "en": ["NPV", "net present worth"],
      "de": ["Kapitalwert", "NBW"],
      "es": ["VAN", "VPN"],
      "fr": ["VAN"]
    },
    "skos_definition": {
      "en": "The present value of expected cash flows minus the initial investment cost, used to evaluate the profitability of an investment or project",
      "source": "FIBO, Wikidata Q1054308"
    }
  },
  "content": {
    "definition": {
      "primary": "Net Present Value (NPV) is the sum of discounted cash flows minus the initial investment."
    }
  }
}
```

**Done!** You've added semantic annotations.

---

## Step 5: Validate (2 minutes)

Save your AKU as `tutorial-npv-aku.json` and validate it:

```bash
# Validate JSON syntax
python3 -m json.tool tutorial-npv-aku.json

# Validate semantic annotations
python3 terminology/validate_npv_ontology.py tutorial-npv-aku.json --verbose
```

**Expected output:**
```
======================================================================
Validating: tutorial-npv-aku.json
======================================================================

ℹ Info:
  ℹ Includes optional languages: it, pt, zh, ja
  ℹ Aligned with reference concepts: net_present_value

✓ PASSED
```

**If you see errors**: Check that JSON is valid (commas, brackets) and URIs are correct.

---

## Step 6: Understand What You Added (3 minutes)

Let's break down what each part does:

### exact_matches
```json
"exact_matches": [
  "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
  "http://dbpedia.org/resource/Net_present_value",
  "http://www.wikidata.org/entity/Q1054308"
]
```
**Purpose**: Links to authoritative ontologies. These say "our NPV concept is **exactly the same** as these external concepts."

**Uses**:
- Automated fact-checking
- Cross-reference validation
- Integration with external systems

### related_matches
```json
"related_matches": [
  "http://www.wikidata.org/entity/Q901690",      // IRR
  "http://www.wikidata.org/entity/Q332099"       // Present Value
]
```
**Purpose**: Links to related but distinct concepts.

**Uses**:
- "See also" links
- Knowledge graph navigation
- Suggested reading

### skos_concept
```json
"skos_concept": "http://www.wikidata.org/entity/Q1054308"
```
**Purpose**: The **primary** identifier for this concept in knowledge graphs.

**Why Wikidata**: Best multilingual support, stable, universal.

### skos_preferred_label
```json
"skos_preferred_label": {
  "en": "Net Present Value",
  "de": "Nettobarwert",
  "es": "Valor Actual Neto",
  "fr": "Valeur Actuelle Nette"
}
```
**Purpose**: Official term in each language.

**Uses**:
- Multilingual rendering
- User interface labels
- Search indexing
- Citations

### skos_alt_label
```json
"skos_alt_label": {
  "en": ["NPV", "net present worth"],
  "de": ["Kapitalwert", "NBW"]
}
```
**Purpose**: Alternative terms and abbreviations.

**Uses**:
- Search expansion (find by "NPV" or "VAN")
- Synonym matching
- Regional variations

### skos_definition
```json
"skos_definition": {
  "en": "The present value of expected cash flows minus...",
  "source": "FIBO, Wikidata Q1054308"
}
```
**Purpose**: Authoritative definition with citation.

**Uses**:
- Tooltips
- Help text
- Citation generation
- Quality validation

---

## Common Scenarios

### Scenario 1: Minimal Annotation (Just Identifiers)

If you're short on space, use this minimal version:

```json
"semantic_links": {
  "exact_matches": [
    "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
    "http://www.wikidata.org/entity/Q1054308"
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q1054308"
}
```

**Still valid!** But less useful for multilingual and knowledge graph purposes.

### Scenario 2: Your Concept Isn't in the Templates

1. Search for it in `terminology/INDEX.md`
2. If not found, do your own research:
   - Search Wikidata: https://www.wikidata.org/
   - Search DBpedia: http://dbpedia.org/
   - Search FIBO: https://spec.edmcouncil.org/fibo/
3. Document your findings in a similar format
4. Consider contributing back to the terminology database

### Scenario 3: Unsure About Match Type

**Use this decision tree:**

```
Is the concept EXACTLY the same in meaning, scope, and usage?
├─ YES → Use exactMatch
└─ NO ↓

Are there only MINOR differences in scope or emphasis?
├─ YES → Use closeMatch
└─ NO ↓

Is the target concept BROADER/more general than yours?
├─ YES → Use broadMatch
└─ NO ↓

Are the concepts RELATED but distinct?
├─ YES → Use relatedMatch
└─ NO → Don't link
```

**When in doubt**: Use `closeMatch` instead of `exactMatch`.

---

## Practice Exercise

Try adding semantic annotations for "Present Value" yourself:

1. Start with this skeleton:
```json
{
  "@context": "aku-v2",
  "@id": "economics:finance:present-value:practice",
  "metadata": { "version": "1.0.0" },
  "classification": { "domain_path": "economics/bwl/finance/valuation" },
  "content": {
    "definition": {
      "primary": "Present Value is the current value of a future sum of money."
    }
  }
}
```

2. Look up "Present Value" in `terminology/INDEX.md`
3. Copy the template from `terminology/aku-semantic-annotations.json`
4. Paste it in
5. Validate with the Python script

**Solution**: Check `akus/examples/example-npv-definition-with-semantic-annotations.json` - it has Present Value links in `related_matches`.

---

## Troubleshooting

### Error: "Invalid JSON"
**Cause**: Missing comma, bracket, or quote  
**Fix**: Use `python3 -m json.tool your-aku.json` to find the error

### Error: "Invalid FIBO URI format"
**Cause**: Typo in FIBO URI  
**Fix**: Copy exactly from `terminology/INDEX.md` or `aku-semantic-annotations.json`

### Error: "Invalid Wikidata URI format"
**Cause**: Wrong Q-number or format  
**Fix**: Verify at https://www.wikidata.org/entity/Q1054308 (example)

### Warning: "Missing required language: de"
**Cause**: German label not included  
**Fix**: Add all 4 required languages (en, de, es, fr) at minimum

---

## Next Steps

### Beginner
- ✅ Complete this tutorial
- [ ] Add annotations to your own AKUs
- [ ] Try the practice exercise
- [ ] Validate with the Python script

### Intermediate
- [ ] Read `terminology/ONTOLOGY-IDENTIFIERS.md` for deep understanding
- [ ] Explore match type classifications
- [ ] Add component-level semantic links
- [ ] Create related concept networks

### Advanced
- [ ] Study `terminology/RESEARCH-METHODOLOGY.md`
- [ ] Contribute new concept annotations
- [ ] Build custom validators
- [ ] Integrate with knowledge graph systems

---

## Resources

### Essential
- `terminology/INDEX.md` - Quick URI lookup
- `terminology/aku-semantic-annotations.json` - Copy-paste templates
- `terminology/QUICK-START-GUIDE.md` - Comprehensive guide

### Reference
- `terminology/ONTOLOGY-IDENTIFIERS.md` - Complete documentation
- `terminology/validation-reference.md` - QA guidelines
- `akus/examples/example-npv-definition-with-semantic-annotations.json` - Full example

### Tools
- `terminology/validate_npv_ontology.py` - Validation script
- `python3 -m json.tool` - JSON syntax validator
- `jq` - JSON query tool (optional)

---

## Success Checklist

After completing this tutorial, you should be able to:

- [x] Locate ontology identifiers in documentation
- [x] Copy semantic_links templates
- [x] Paste them correctly into AKUs
- [x] Validate JSON syntax
- [x] Validate semantic annotations
- [x] Understand match types
- [x] Add multilingual labels
- [x] Troubleshoot common errors

**Congratulations!** You can now add semantic annotations to NPV AKUs. 🎉

---

## Feedback

Found an issue with this tutorial? Have suggestions?
- Contact: @terminology agent
- File: Issue in `.project/issues.md`

---

**Tutorial Version**: 1.0  
**Last Updated**: 2025-12-27  
**Estimated Time**: 10 minutes  
**Difficulty**: Beginner ⭐
