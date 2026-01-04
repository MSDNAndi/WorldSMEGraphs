# Cross-Domain Knowledge Linking: A Visual Guide

> **Purpose**: Understand how knowledge concepts connect across different domains using the native domain principle and cross-domain references.

## Table of Contents
1. [Core Concept](#core-concept)
2. [The Native Domain Principle](#the-native-domain-principle)
3. [Visual Examples](#visual-examples)
4. [Implementation Patterns](#implementation-patterns)
5. [Real-World Cases](#real-world-cases)
6. [Best Practices](#best-practices)

---

## Core Concept

### What is Cross-Domain Linking?

**Cross-domain linking** connects knowledge concepts across different academic and professional domains while maintaining clear ownership and avoiding duplication.

### The Problem It Solves

**Without Cross-Domain Linking**:
```
Math Domain              CS Domain
┌──────────────┐        ┌──────────────┐
│ Monad        │        │ Monad        │  ← Duplicate!
│ (definition) │        │ (definition) │
│              │        │              │
└──────────────┘        └──────────────┘
```

**With Cross-Domain Linking**:
```
Math Domain (Native)     CS Domain (Application)
┌──────────────┐        ┌──────────────┐
│ Monad        │◄───────│ Monad Usage  │
│ (definition) │ refers │ (application)│
│ NATIVE       │   to   │ APPLIES      │
└──────────────┘        └──────────────┘
```

### Key Benefits

1. ✅ **Single Source of Truth**: One authoritative definition
2. ✅ **Avoid Duplication**: Don't copy concepts
3. ✅ **Clear Attribution**: Know where concepts originated
4. ✅ **Easy Updates**: Change once, applies everywhere
5. ✅ **Rich Context**: See how concepts are used across fields

---

## The Native Domain Principle

### Definition

> **Native Domain**: The academic or professional field where a concept **originated** and has its authoritative definition.

### Rules

1. **Every concept has ONE native domain**
   - Where it was first discovered/invented
   - Where experts define it authoritatively

2. **Native domain owns the definition**
   - Marked with `isNativeDomain: true`
   - Contains complete, rigorous definition
   - May list application domains

3. **Application domains link to native**
   - Marked with `isApplicationDomain: true`
   - Include `cross_domain_references`
   - Describe application-specific usage
   - Do NOT duplicate native definition

### Decision Flowchart

```
For concept X:

1. Where did X originate?
   ├─ Mathematics → Native: Formal Sciences / Mathematics
   ├─ Physics Law → Native: Natural Sciences / Physics
   ├─ Economic Theory → Native: Social Sciences / Economics
   └─ Medical Diagnosis → Native: Health Sciences / Medicine

2. Am I in the native domain?
   ├─ YES → Set isNativeDomain: true
   │         Add complete definition
   │         List application domains
   │
   └─ NO  → Set isApplicationDomain: true
             Add cross_domain_references
             Describe application-specific usage
```

---

## Visual Examples

### Example 1: Category Theory

Category theory originated in **mathematics** but is widely used in **computer science**.

#### Native Domain (Mathematics)

```
Location: formal-sciences/mathematics/pure-mathematics/category-theory/

┌────────────────────────────────────────┐
│  Category Theory (NATIVE)              │
│                                        │
│  isNativeDomain: true                  │
│                                        │
│  Content:                              │
│  • Complete mathematical definition    │
│  • Rigorous axioms and laws           │
│  • Universal properties                │
│  • Morphisms and composition          │
│                                        │
│  cross_domain_applications:            │
│  • Functional programming              │
│  • Type theory                         │
│  • Abstract algebra                    │
└────────────────────────────────────────┘
```

#### Application Domain (Computer Science)

```
Location: science/computer-science/functional-theory/

┌────────────────────────────────────────┐
│  Functors, Monads (APPLICATION)        │
│                                        │
│  isApplicationDomain: true             │
│  isNativeDomain: false                 │
│                                        │
│  cross_domain_references: ───────┐     │
│    @id: "wsmg:formal-sciences/   │     │
│           mathematics/...monad"  │     │
│    sourceDomain: math            │     │
│    relationship: applies         │     │
│                                  │     │
│  Content:                        │     │
│  • Programming usage             │     │
│  • Code examples                 │     │
│  • Practical applications        │     │
└──────────────────────────────────┼─────┘
                                   │
                         ┌─────────┘
                         ▼
              Points to math definition
              (doesn't duplicate it)
```

#### Visual Relationship

```
Mathematics (Native)              Computer Science (Application)
━━━━━━━━━━━━━━━━━━━━             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────┐              ┌─────────────────┐
│ Category Theory │              │ Functors        │
│                 │              │                 │
│ Definition:     │◄─────────────┤ Usage:          │
│  A category C   │    refers    │  map :: (a→b)   │
│  consists of... │     to       │  → f a → f b    │
│                 │              │                 │
│ Monad:          │              │ Monad:          │
│  T: C → C       │◄─────────────┤  bind :: m a    │
│  η: Id → T      │              │  → (a → m b)    │
│  μ: T² → T      │              │  → m b          │
└─────────────────┘              └─────────────────┘
      ▲                                  │
      │                                  │
      │ cross_domain_applications        │ cross_domain_references
      │                                  │
      └──────────────────────────────────┘
               bidirectional awareness
```

### Example 2: Statistical Methods

Statistics originated in **mathematics** but is used across ALL domains.

```
Mathematics (Native)           → Social Sciences (Application)
                               → Natural Sciences (Application)
                               → Health Sciences (Application)

┌──────────────────┐          ┌──────────────────┐
│ Statistics       │          │ Clinical Trials  │
│                  │◄─────────│ Statistical      │
│ p-value:         │  refers  │ Analysis         │
│  Probability of  │   to     │                  │
│  observing data  │          │ Uses: p-value,   │
│  given H₀ true   │          │ confidence       │
│                  │          │ intervals, etc.  │
└──────────────────┘          └──────────────────┘
        ▲                              
        │ cross_domain_references      
        │ from: economics, medicine,   
        │       psychology, biology... 
        │                              
```

### Example 3: Thermodynamics

Thermodynamics is a **physics law** (natural sciences) applied in engineering.

```
Physics (Native)               Engineering (Application)
━━━━━━━━━━━━━━━━              ━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────────┐          ┌──────────────────┐
│ Laws of          │          │ Engine Design    │
│ Thermodynamics   │          │                  │
│                  │◄─────────│ Applies:         │
│ 1st Law:         │          │  • Carnot cycle  │
│  ΔU = Q - W      │          │  • Efficiency    │
│                  │          │  • Heat transfer │
│ 2nd Law:         │          │                  │
│  ΔS ≥ 0          │          │ Practical:       │
│                  │          │  • ICE design    │
│ 3rd Law:         │          │  • HVAC systems  │
│  S → 0 as T → 0  │          │  • Refrigeration │
└──────────────────┘          └──────────────────┘
```

---

## Implementation Patterns

### Pattern 1: Native Domain AKU

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
  
  "metadata": {
    "version": "2.0.0",
    "created": "2024-01-15T10:00:00.000Z",
    "modified": "2026-01-04T14:30:00.000Z"
  },
  
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "type": "definition",
    "isNativeDomain": true,
    "isApplicationDomain": false
  },
  
  "content": {
    "primary_definition": {
      "statement": "A monad T on a category C consists of...",
      "formal_notation": "T: C → C, η: Id → T, μ: T² → T"
    }
  },
  
  "cross_domain_applications": {
    "functional_programming": "Structures effectful computations",
    "type_theory": "Models computational effects",
    "abstract_algebra": "Monoid in endofunctor category"
  }
}
```

**Key Fields**:
- `isNativeDomain: true` ← Marks as authoritative source
- `cross_domain_applications` ← Lists where it's used
- Complete, rigorous definition in `content`

### Pattern 2: Application Domain AKU

```json
{
  "@context": "aku-v2",
  "@type": "concept",
  "@id": "wsmg:computer-science/functional-programming/monad-usage",
  
  "metadata": {
    "version": "2.0.0",
    "modified": "2026-01-04T14:45:00.000Z"
  },
  
  "classification": {
    "domain_path": "science/computer-science/functional-theory/monads",
    "type": "concept",
    "isNativeDomain": false,
    "isApplicationDomain": true
  },
  
  "content": {
    "application_specific": {
      "context": "Functional programming languages",
      "usage": "Monads structure sequential computations..."
    }
  },
  
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
      "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
      "relationship": "applies",
      "applicationContext": "Monads in FP apply mathematical monad concept to structure effectful computations"
    }]
  }
}
```

**Key Fields**:
- `isApplicationDomain: true` ← Marks as application
- `isNativeDomain: false` ← Not the authoritative source
- `cross_domain_references` ← Links to native definition
- Application-specific content (not duplicate definition)

### Pattern 3: Relationship Types

```json
"cross_domain_references": {
  "applies": [...]       // Uses concept from native domain
  "extends": [...]       // Builds upon native concept
  "requires": [...]      // Prerequisite from another domain
  "related_to": [...]    // Loosely related concept
}
```

---

## Real-World Cases

### Case 1: Category Theory Migration

**Problem**: Category theory AKUs were in computer science, but category theory is mathematics.

**Solution Applied**:
1. **Moved category theory to mathematics** (native domain)
2. **Marked as native**: `isNativeDomain: true`
3. **Updated functional programming AKUs**: Added `cross_domain_references`
4. **Result**: Clear ownership, no duplication

**Before**:
```
science/computer-science/functional-theory/category-theory/  ← WRONG
science/computer-science/functional-theory/monads/
```

**After**:
```
formal-sciences/mathematics/pure-mathematics/category-theory/  ← NATIVE
  └─ isNativeDomain: true
  
science/computer-science/functional-theory/monads/  ← APPLICATION
  └─ cross_domain_references → mathematics
```

### Case 2: Physics in Multiple Contexts

**Scenario**: Planck units (physics) used in cosmology, quantum mechanics, and string theory.

**Implementation**:
```
Native Domain: natural-sciences/physics/quantum-mechanics/planck-units/
  isNativeDomain: true
  cross_domain_applications:
    - Cosmology: Big Bang epoch analysis
    - Quantum Gravity: Fundamental limits
    - String Theory: Planck scale phenomena
    - Black Hole Physics: Hawking radiation

Application Domains:
  - Cosmology AKUs link back to Planck units
  - String theory AKUs link back to Planck units
  - Each describes their specific usage
  - None duplicate the native definition
```

### Case 3: Medical Statistics

**Scenario**: Statistical methods (math) used in clinical trials (medicine).

**Implementation**:
```
Native: formal-sciences/mathematics/statistics/
  - Statistical tests defined rigorously
  - p-values, confidence intervals
  - Hypothesis testing framework

Application: health-sciences/medicine/clinical-research/
  - Links to native statistical definitions
  - Describes medical context
  - Clinical interpretation
  - Regulatory requirements
```

---

## Best Practices

### DO ✅

1. **Identify Native Domain First**
   ```
   Ask: "Where did this concept originate?"
   Not: "Where do I use it?"
   ```

2. **Link, Don't Duplicate**
   ```json
   // GOOD: Application domain
   {
     "cross_domain_references": {
       "applies": [{
         "@id": "wsmg:path/to/native/concept"
       }]
     }
   }
   ```
   
   ```json
   // BAD: Duplicating native definition
   {
     "content": {
       "definition": "A monad is..."  // Don't copy!
     }
   }
   ```

3. **Use Proper @id Format**
   ```
   ✅ "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad"
   ❌ "monad"
   ❌ "../../../mathematics/monad"
   ```

4. **Specify Relationship Type**
   ```json
   {
     "relationship": "applies",  // or "extends", "requires", etc.
     "applicationContext": "Describes specific usage"
   }
   ```

5. **Maintain Bidirectional Awareness**
   ```
   Native Domain:
     cross_domain_applications: ["FP", "Type Theory"]
   
   Application Domain:
     cross_domain_references → Native Domain
   ```

### DON'T ❌

1. **Don't Place by Usage**
   ```
   ❌ Category theory in CS (because CS uses it)
   ✅ Category theory in Math (where it originated)
   ```

2. **Don't Duplicate Definitions**
   ```
   ❌ Full monad definition in both math and CS
   ✅ Definition in math, application details in CS
   ```

3. **Don't Forget Flags**
   ```json
   // ❌ Missing
   {
     "classification": {}
   }
   
   // ✅ Complete
   {
     "classification": {
       "isNativeDomain": true,
       "isApplicationDomain": false
     }
   }
   ```

4. **Don't Use Relative Paths**
   ```json
   // ❌ BAD
   "@id": "../../../math/monad"
   
   // ✅ GOOD
   "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad"
   ```

5. **Don't Skip Application Context**
   ```json
   // ❌ Incomplete
   {
     "cross_domain_references": {
       "applies": [{
         "@id": "wsmg:path/to/concept"
       }]
     }
   }
   
   // ✅ Complete
   {
     "cross_domain_references": {
       "applies": [{
         "@id": "wsmg:path/to/concept",
         "relationship": "applies",
         "applicationContext": "Describes how concept is used in this domain"
       }]
     }
   }
   ```

---

## Validation

### Check Native Domain

```bash
python domain/_ontology/tools/validate_cross_domain.py \
  formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-002-category-definition.json
```

**Expected Output**:
```
✓ ct-002-category-definition.json
  Classification: Native Domain ✓
  isNativeDomain: true ✓
```

### Check Application Domain

```bash
python domain/_ontology/tools/validate_cross_domain.py \
  science/computer-science/functional-theory/monads/akus/md-001-monad-definition.json
```

**Expected Output**:
```
✓ md-001-monad-definition.json
  Classification: Application Domain ✓
  isApplicationDomain: true ✓
  isNativeDomain: false ✓
  Cross-domain references: Present ✓
    → formal-sciences/mathematics/pure-mathematics/category-theory/monad
  Reference validity: ✓ Path exists
```

---

## Summary

### Key Principles

1. **Native Domain Ownership**: Every concept has ONE authoritative source
2. **Application Domains Link**: Others reference, don't duplicate
3. **Clear Attribution**: Know where concepts originated
4. **Rich Context**: Document cross-domain usage

### Benefits

- ✅ Eliminates duplication
- ✅ Single source of truth
- ✅ Clear concept ownership
- ✅ Easy maintenance
- ✅ Rich interdisciplinary connections

### Quick Reference

| Aspect | Native Domain | Application Domain |
|--------|--------------|-------------------|
| **Flag** | `isNativeDomain: true` | `isApplicationDomain: true` |
| **Content** | Complete definition | Application-specific usage |
| **Cross-refs** | `cross_domain_applications` (list) | `cross_domain_references` (links) |
| **Purpose** | Authoritative source | Practical application |
| **Example** | Math defines "monad" | CS applies "monad" in FP |

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**See Also**: 
- `DOMAIN-COMPARISON-MATRIX.md` - Domain characteristics
- `MIGRATION-GUIDE.md` - Migration patterns
- `TOOLS-DOCUMENTATION.md` - Validation tools

