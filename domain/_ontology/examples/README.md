# Cross-Domain AKU Examples

This directory contains example AKUs that demonstrate the correct pattern for cross-domain knowledge organization.

## The Pattern

WorldSMEGraphs follows the **native domain placement** principle:

1. **Concepts belong to their origin domain** - where they were developed
2. **Applications LINK to native concepts** - they don't duplicate content
3. **One source of truth** - modifications happen in the native domain

## Example Files

### 1. `native-domain-aku-example.json`

**What it is**: A mathematical AKU for "Monad" in its native domain (category theory).

**Key features**:
- `isNativeDomain: true` - This is the authoritative location
- Full mathematical definition with notation and coherence conditions
- `cross_domain_applications` section that documents where this concept is applied
- External mappings to Wikidata, nLab, etc.

**Location in hierarchy**:
```
formal-sciences/mathematics/pure-mathematics/category-theory/
```

### 2. `application-domain-aku-example.json`

**What it is**: A programming AKU for "Monad in Functional Programming" that APPLIES the mathematical concept.

**Key features**:
- `isNativeDomain: false` and `isApplicationDomain: true`
- `cross_domain_references.applies` with link to math definition
- Programming-specific content (code examples, common monads)
- Clear attribution to the mathematical source

**Location in hierarchy**:
```
formal-sciences/computer-science/programming-paradigms/functional-programming/
```

### 3. `application-domain-health-example.json` (NEW)

**What it is**: A practical health guidance AKU for "Conference Cognitive Optimization" that APPLIES concepts from multiple scientific domains.

**Key features**:
- `isNativeDomain: false` and `isApplicationDomain: true`
- `cross_domain_references.applies` with links to 7 native domain AKUs
- Practical guidance synthesized from neurology, psychology, pharmacology, and public health
- Clear attribution to authoritative scientific sources

**Location in hierarchy**:
```
health-sciences/preventive-medicine/travel-health/
```

**Linked native domain AKUs**:
- `health-sciences/medicine/neurology/neuro-051` - Dehydration and cognitive impairment
- `health-sciences/medicine/neurology/neuro-052` - Circadian rhythm and jet lag
- `health-sciences/medicine/neurology/neuro-053` - Sleep architecture and napping
- `social-sciences/psychology/psych-001` - Decision fatigue
- `social-sciences/psychology/psych-003` - FOMO
- `health-sciences/pharmacy/pharm-002` - Caffeine pharmacokinetics
- `health-sciences/public-health/ph-001` - Sedentary behavior risks

## The Relationship

```
┌─────────────────────────────────────────────────────────────┐
│  MATHEMATICS (Native Domain)                                 │
│  formal-sciences/mathematics/pure-mathematics/category-theory│
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ monad-definition.json                                   │ │
│  │ - Full mathematical definition                          │ │
│  │ - Notation: (T, η, μ)                                   │ │
│  │ - Coherence conditions                                  │ │
│  │ - Mathematical examples                                 │ │
│  │ - isNativeDomain: true                                  │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │ applies
                            │
┌─────────────────────────────────────────────────────────────┐
│  COMPUTER SCIENCE (Application Domain)                      │
│  formal-sciences/computer-science/programming-paradigms/fp   │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ monad-in-programming.json                               │ │
│  │ - Programming interpretation                            │ │
│  │ - Code examples (Haskell, Scala, JS)                    │ │
│  │ - Common monads (Maybe, IO, State)                      │ │
│  │ - cross_domain_references.applies: monad-definition     │ │
│  │ - isApplicationDomain: true                             │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Key Properties

### In Native Domain AKUs

```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "isNativeDomain": true
  },
  "cross_domain_applications": {
    "applications": [
      {
        "domain": "formal-sciences/computer-science/programming-paradigms/functional-programming",
        "context": "Monads structure effectful computations"
      }
    ]
  }
}
```

### In Application Domain AKUs

```json
{
  "classification": {
    "domain_path": "formal-sciences/computer-science/programming-paradigms/functional-programming",
    "isNativeDomain": false,
    "isApplicationDomain": true
  },
  "cross_domain_references": {
    "applies": [
      {
        "@id": "wsmg:math/category-theory/monad-definition",
        "relationship": "applies",
        "applicationContext": "Programming interpretation of mathematical monad"
      }
    ]
  }
}
```

## Relationship Types

| Type | Direction | Description | Example |
|------|-----------|-------------|---------|
| `applies` | app → native | Applies concepts practically | FP applies category theory |
| `uses` | app → native | Uses as tools/foundations | ML uses linear algebra |
| `extends` | app → native | Extends with domain-specific structure | Type theory extends category theory |
| `informs` | bidirectional | Mutual influence | Physics ↔ Mathematics |

## Benefits

1. **Single source of truth** - Updates to math propagate everywhere
2. **Clear attribution** - Origin of concepts is always clear
3. **No duplication** - Content exists in one place
4. **Rich linking** - Applications connect to foundations
5. **Ontological integrity** - Concepts are in their proper place

## Anti-Patterns to Avoid

### ❌ Copying Content

Don't copy the mathematical definition into the programming AKU:

```json
// WRONG
{
  "@id": "wsmg:cs/fp/monad",
  "definition": "A monad on a category C is a triple (T, η, μ)..."  // Copied from math!
}
```

### ❌ Placing Concepts in Application Domains

Don't put concepts where they're used instead of where they're from:

```
// WRONG
computer-science/functional-programming/category-theory/monad/

// CORRECT
mathematics/pure-mathematics/category-theory/monad/
```

### ❌ Bidirectional Content

Don't put full content in both locations:

```json
// WRONG: Two full definitions
math/monad.json:  { "definition": "Full math definition..." }
cs/monad.json:    { "definition": "Full CS definition..." }

// CORRECT: One native, one linking
math/monad.json:  { "definition": "Full math definition...", "isNativeDomain": true }
cs/monad.json:    { "applies": "math/monad", "applicationContext": "..." }
```

## Validation

AKUs should be validated to ensure:

1. Every AKU has exactly one `domain_path`
2. `isNativeDomain: true` AKUs have full definitions
3. `isApplicationDomain: true` AKUs have `cross_domain_references`
4. All cross-domain links point to valid AKUs
5. No duplicate concepts across domains

## See Also

- [Global Domain Hierarchy](../global-hierarchy.yaml)
- [Cross-Domain JSON-LD Context](../../_contexts/cross-domain.jsonld)
- [Design Documentation](../README.md)
