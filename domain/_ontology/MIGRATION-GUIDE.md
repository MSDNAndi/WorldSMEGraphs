# Cross-Domain Migration Guide

This guide explains how to migrate existing AKUs to follow the cross-domain linking pattern established in the global domain hierarchy.

## Overview

The migration involves two key changes:

1. **Moving native concepts to their origin domain**
2. **Converting application references to cross-domain links**

## Migration Steps

### Step 1: Identify Native vs Application Domains

Ask: "Where was this concept originally developed?"

| Concept | Native Domain | Application Domains |
|---------|---------------|---------------------|
| Category Theory | `formal-sciences/mathematics/pure-mathematics/category-theory` | CS, Physics |
| Linear Algebra | `formal-sciences/mathematics/pure-mathematics/algebra/linear-algebra` | ML, Physics, Economics |
| Calculus | `formal-sciences/mathematics/pure-mathematics/analysis/calculus` | Physics, Engineering, Economics |
| Probability | `formal-sciences/mathematics/applied-mathematics/probability-theory` | Statistics, ML, Finance |

### Step 2: Add Domain Markers

Add classification fields to indicate native or application status:

**For Native Domain AKUs:**
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "isNativeDomain": true,
    "type": "definition",
    "difficulty": "graduate"
  }
}
```

**For Application Domain AKUs:**
```json
{
  "classification": {
    "domain_path": "formal-sciences/computer-science/programming-paradigms/functional-programming",
    "isNativeDomain": false,
    "isApplicationDomain": true,
    "type": "concept",
    "difficulty": "intermediate"
  }
}
```

### Step 3: Add Cross-Domain References (Application AKUs)

For AKUs that apply concepts from other domains, add the `cross_domain_references` section:

```json
{
  "cross_domain_references": {
    "applies": [
      {
        "@id": "wsmg:math/category-theory/monad-definition",
        "relationship": "applies",
        "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
        "applicationContext": "Monads structure effectful computations in functional programming"
      }
    ],
    "uses": [
      {
        "@id": "wsmg:math/algebra/monoid-definition",
        "relationship": "uses",
        "applicationContext": "Monoids provide algebraic structure for aggregation operations"
      }
    ]
  }
}
```

### Step 4: Add Cross-Domain Applications (Native AKUs)

For native AKUs, document where the concept is applied:

```json
{
  "cross_domain_applications": {
    "note": "This section documents where this mathematical concept is APPLIED",
    "applications": [
      {
        "domain": "formal-sciences/computer-science/programming-paradigms/functional-programming",
        "context": "Monads structure effectful computations in functional programming",
        "related_akus": ["wsmg:cs/fp/monad-in-programming"]
      },
      {
        "domain": "formal-sciences/computer-science/type-theory",
        "context": "Monads provide semantics for computational effects",
        "related_akus": ["wsmg:cs/type-theory/computational-effects"]
      }
    ]
  }
}
```

## Category Theory Migration Example

### Before (Current Structure)

```
domain/
└── science/
    └── computer-science/
        └── functional-theory/
            └── category-theory/
                └── akus/
                    └── ct-001-category-definition.json  ← Wrong location!
```

### After (Correct Structure)

```
domain/
├── formal-sciences/
│   ├── mathematics/
│   │   └── pure-mathematics/
│   │       └── category-theory/
│   │           └── akus/
│   │               └── ct-001-category-definition.json  ← Native (CORRECT)
│   │
│   └── computer-science/
│       └── programming-paradigms/
│           └── functional-programming/
│               └── akus/
│                   └── fp-category-theory-applications.json  ← Application (CORRECT)
```

### File Changes

**Original AKU (in wrong location):**
```json
{
  "@id": "wsmg:cs/functional-theory/category-definition",
  "classification": {
    "domain_path": "science/computer-science/functional-theory"
  },
  "content": {
    "definition": "A category consists of objects and morphisms..."
  }
}
```

**Step 1: Move to Mathematics (Native)**
```json
{
  "@id": "wsmg:math/category-theory/category-definition",
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "isNativeDomain": true
  },
  "content": {
    "definition": "A category consists of objects and morphisms..."
  },
  "cross_domain_applications": {
    "applications": [
      {
        "domain": "formal-sciences/computer-science/programming-paradigms/functional-programming",
        "context": "Categories provide theoretical foundation for type systems and composition"
      }
    ]
  }
}
```

**Step 2: Create Application AKU for Functional Programming**
```json
{
  "@id": "wsmg:cs/fp/category-theory-in-programming",
  "classification": {
    "domain_path": "formal-sciences/computer-science/programming-paradigms/functional-programming",
    "isApplicationDomain": true
  },
  "cross_domain_references": {
    "applies": [
      {
        "@id": "wsmg:math/category-theory/category-definition",
        "relationship": "applies",
        "applicationContext": "Categories model types and functions in programming"
      }
    ]
  },
  "content": {
    "explanation": "In programming, categories appear as type systems...",
    "code_examples": { }
  }
}
```

## Relationship Types

| Type | Direction | When to Use | Example |
|------|-----------|-------------|---------|
| `applies` | app → native | Applying theoretical concepts practically | FP uses monads from math |
| `uses` | app → native | Using as tool/foundation | ML uses linear algebra |
| `extends` | app → native | Extending with domain-specific structure | Type theory extends category theory |
| `informs` | bidirectional | Mutual influence | Physics ↔ Mathematics |

## Validation

After migration, validate AKUs with:

```bash
# Validate single file
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Validate directory
python domain/_ontology/tools/validate_cross_domain.py --directory domain/formal-sciences/
```

Expected output for correct AKUs:
```
✅ Valid with no warnings
```

## Common Mistakes

### ❌ Duplicating Content

Don't copy the native definition to the application AKU:
```json
// WRONG - duplication
{
  "@id": "wsmg:cs/fp/monad",
  "definition": "A monad is a triple (T, η, μ)..."  // Copied from math!
}
```

### ❌ Mixing Native and Application

Don't mark the same AKU as both:
```json
// WRONG - contradictory
{
  "isNativeDomain": true,
  "isApplicationDomain": true
}
```

### ❌ Missing Application Context

Always explain how the concept is applied:
```json
// WRONG - no context
{
  "cross_domain_references": {
    "uses": [{ "@id": "wsmg:math/algebra/monoid" }]  // Why? How?
  }
}

// RIGHT - with context
{
  "cross_domain_references": {
    "uses": [{
      "@id": "wsmg:math/algebra/monoid",
      "applicationContext": "Monoids enable generic fold operations"
    }]
  }
}
```

## See Also

- [Global Domain Hierarchy](global-hierarchy.yaml)
- [Cross-Domain JSON-LD Context](../_contexts/cross-domain.jsonld)
- [Native Domain Example](examples/native-domain-aku-example.json)
- [Application Domain Example](examples/application-domain-aku-example.json)
- [Issue #3: Category Theory Migration](../../.project/issues.md)
