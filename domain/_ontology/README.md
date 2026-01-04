# Global Domain Hierarchy - Design Documentation

> **Version**: 1.0.0  
> **Created**: 2026-01-04  
> **Author**: ontology-agent  
> **Status**: Approved for implementation

## Overview

This document explains the design decisions behind the WorldSMEGraphs Global Domain Hierarchy, a comprehensive taxonomy for organizing all knowledge in the system.

## Problem Statement

Previous implementations (PRs #23, #24) placed category theory under `science/computer-science/functional-theory/` because it was being used for a functional programming presentation. This approach:

1. **Sacrificed ontological rigor** for pedagogical convenience
2. **Conflated origin with application** - treating where something is used as where it belongs
3. **Created precedent** for misplacing other foundational concepts
4. **Made cross-domain linking unclear** - where do concepts really live?

The user specifically stated:
> "We need a truly global domain hierarchy first and cannot sacrifice it to pedagogical goals. We have to accomplish those goals differently."

## Design Principles

### 1. Native Domain Placement

**Principle**: Every concept belongs to exactly one NATIVE domain - the field where it was originally developed.

**Rationale**: 
- Category theory was developed by Eilenberg and Mac Lane in 1945 for algebraic topology
- It is fundamentally mathematics, not computer science
- Being used in CS/physics doesn't change its mathematical nature

**Implementation**:
- Category theory → `formal-sciences/mathematics/pure-mathematics/category-theory/`
- Linear algebra → `formal-sciences/mathematics/pure-mathematics/algebra/linear-algebra/`
- Even if 95% of linear algebra usage is in ML, it's still math

### 2. Single Source of Truth

**Principle**: AKUs are created ONLY in the native domain. Other domains LINK to these AKUs.

**Rationale**:
- Avoids content duplication
- Ensures consistency
- Makes updates propagate automatically
- Clarifies authoritative sources

**Implementation**:
```yaml
# In functional programming AKU
cross_domain_references:
  uses:
    - "@id": "wsmg:math/category-theory/monad-definition"
      relationship: "applies"
      context: "Functional programming uses monads to structure effects"
```

### 3. Cross-Domain Linking, Not Copying

**Principle**: Applications create semantic links to source concepts, not copies of content.

**Rationale**:
- Maintains integrity
- Enables rich semantic web
- Supports multiple viewpoints on same concept
- Allows domain-specific context without duplication

**Implementation**:
- Native AKU: Full mathematical definition
- Application AKU: Programming context + link to math definition

## Taxonomy Sources

The hierarchy draws from established knowledge classification systems:

| System | Coverage | Used For |
|--------|----------|----------|
| UNESCO ISCED-F 2013 | Education fields | Top-level categories |
| Library of Congress | All knowledge | General structure |
| Dewey Decimal | All knowledge | Cross-reference |
| MSC 2020 | Mathematics | Math subdomain |
| ACM CCS | Computing | CS subdomain |

## Top-Level Domains

### 1. Formal Sciences
Abstract structures and formal systems using deductive methodology.

**Includes**: Mathematics, Computer Science, Logic
**Why separate**: Uses different methodology (deduction) than empirical sciences

### 2. Natural Sciences
Empirical study of the physical world.

**Includes**: Physics, Chemistry, Biology, Earth Sciences, Astronomy
**Why here**: Share empirical, observational methodology

### 3. Social Sciences
Study of human society and behavior.

**Includes**: Economics, Psychology, Sociology, Political Science
**Why separate**: Different subject matter (humans) and methods

### 4. Health Sciences
Sciences concerned with human health and healthcare.

**Includes**: Medicine, Nursing, Pharmacy, Public Health
**Why separate**: Practical orientation toward health outcomes

### 5. Engineering
Application of science to practical problems.

**Includes**: Mechanical, Electrical, Civil, Chemical, Biomedical
**Why separate**: Applied orientation with practical outcomes

### 6. Humanities
Study of human culture and experience.

**Includes**: Philosophy, History, Linguistics, Literature
**Why separate**: Interpretive methods, focus on meaning

### 7. Arts
Creative expression and aesthetic experience.

**Includes**: Visual Arts, Performing Arts, Music, Design
**Why separate**: Creative and aesthetic focus

### 8. Interdisciplinary
Fields that inherently span multiple domains.

**Includes**: Cognitive Science, Bioinformatics, Data Science
**Why exists**: Some fields cannot be cleanly assigned

## Category Theory: The Test Case

### Current Location (Wrong)
```
domain/
└── science/
    └── computer-science/
        └── functional-theory/
            └── category-theory/  ← WRONG
```

### Correct Location
```
domain/
└── formal-sciences/
    └── mathematics/
        └── pure-mathematics/
            └── category-theory/  ← CORRECT
```

### Cross-Linking Pattern
```
domain/
├── formal-sciences/
│   ├── mathematics/
│   │   └── pure-mathematics/
│   │       └── category-theory/
│   │           └── akus/
│   │               ├── monad-definition.json      ← NATIVE AKU
│   │               ├── functor-definition.json    ← NATIVE AKU
│   │               └── ...
│   │
│   └── computer-science/
│       └── programming-paradigms/
│           └── functional-programming/
│               └── akus/
│                   ├── monad-in-programming.json  ← APPLICATION AKU
│                   │   └── links to: monad-definition.json
│                   └── functor-map-operation.json ← APPLICATION AKU
│                       └── links to: functor-definition.json
```

### Example: Native vs Application AKU

**Native AKU (Mathematics)**:
```json
{
  "@id": "wsmg:math/category-theory/monad-definition",
  "@type": ["MathematicalConcept", "skos:Concept"],
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory"
  },
  "content": {
    "core": {
      "definition": "A monad on a category C is a triple (T, η, μ)...",
      "notation": {
        "T": "endofunctor T: C → C",
        "η": "unit natural transformation η: 1_C → T",
        "μ": "multiplication natural transformation μ: T² → T"
      }
    }
  }
}
```

**Application AKU (Functional Programming)**:
```json
{
  "@id": "wsmg:cs/fp/monad-in-programming",
  "@type": ["ProgrammingConcept", "skos:Concept"],
  "classification": {
    "domain_path": "formal-sciences/computer-science/programming-paradigms/functional-programming"
  },
  "cross_domain_references": {
    "uses": [
      {
        "@id": "wsmg:math/category-theory/monad-definition",
        "relationship": "applies",
        "context": "Monads structure effectful computations"
      }
    ]
  },
  "content": {
    "core": {
      "explanation": "In functional programming, a monad is a design pattern...",
      "code_examples": {
        "haskell": "class Monad m where...",
        "scala": "trait Monad[F[_]]..."
      }
    }
  }
}
```

## Migration Recommendations

### Phase 1: Create New Structure
1. Create `domain/formal-sciences/` directory tree
2. Create `domain/natural-sciences/` for physics, chemistry, biology
3. Create `domain/social-sciences/economics/` 
4. Create `domain/health-sciences/medicine/`

### Phase 2: Migrate Content
1. Move category theory AKUs to mathematics
2. Update functional-theory to link to, not contain, category theory
3. Move medicine content to health-sciences
4. Move economics content to social-sciences

### Phase 3: Update References
1. Update all cross-domain links
2. Update concept-index.yaml files
3. Update JSON-LD contexts

### Phase 4: Deprecate Old Paths
1. Add deprecation notices
2. Create redirects if needed
3. Remove old directories after verification

## Relationship to Existing Content

### Current `domain/science/`
Maps to multiple new locations:
- `science/math/` → `formal-sciences/mathematics/`
- `science/physics/` → `natural-sciences/physics/`
- `science/computer-science/` → `formal-sciences/computer-science/`

### Current `domain/economics/`
Maps to:
- `economics/` → `social-sciences/economics/`

### Current `domain/medicine/`
Maps to:
- `medicine/` → `health-sciences/medicine/`

## Validation

The hierarchy includes validation rules to ensure:

1. **Single native domain**: Every concept has exactly one native domain
2. **Valid cross-references**: All links point to existing AKUs
3. **No duplication**: Concepts exist in only one location
4. **Proper linking**: Application domains link, not copy

## Future Considerations

### Extensibility
- New domains added at appropriate level
- Hierarchy supports arbitrary depth
- Cross-domain patterns scale

### Versioning
- Hierarchy version tracked
- Migration paths documented
- Backwards compatibility considered

### Tooling
- Validation scripts for hierarchy compliance
- Migration tools for content moves
- Link checking utilities

## Appendix: Cross-Domain Relationship Types

| Type | Direction | Description | Example |
|------|-----------|-------------|---------|
| `applies` | app → native | Applies concepts | FP applies category theory |
| `uses` | app → native | Uses as foundation | ML uses linear algebra |
| `extends` | app → native | Extends concepts | Type theory extends category theory |
| `informs` | bidirectional | Mutual influence | Physics ↔ Mathematics |

## References

1. Eilenberg, S., & Mac Lane, S. (1945). General theory of natural equivalences. *Transactions of the American Mathematical Society*, 58(2), 231-294.

2. UNESCO Institute for Statistics. (2015). *International Standard Classification of Education: Fields of Education and Training 2013 (ISCED-F 2013)*.

3. Library of Congress. *Library of Congress Classification*. https://www.loc.gov/catdir/cpso/lcc.html

4. OCLC. *Dewey Decimal Classification*. https://www.oclc.org/dewey.en.html

5. American Mathematical Society. *Mathematics Subject Classification 2020*. https://mathscinet.ams.org/mathscinet/msc/msc2020.html

6. ACM. *Computing Classification System*. https://dl.acm.org/ccs

## Related Documents

- [Global Domain Hierarchy](global-hierarchy.yaml) - Authoritative taxonomy
- [Migration Guide](MIGRATION-GUIDE.md) - How to migrate existing AKUs
- [Cross-Domain Examples](examples/) - Example AKUs demonstrating patterns
- [Validation Tool](tools/validate_cross_domain.py) - AKU validator
- [Cross-Domain Context](../_contexts/cross-domain.jsonld) - JSON-LD vocabulary

---

**Document Status**: This document is the authoritative design specification for the WorldSMEGraphs global domain hierarchy.
