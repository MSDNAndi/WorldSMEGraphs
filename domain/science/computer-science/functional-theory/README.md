# Functional Theory Knowledge Domain

## Overview

This domain contains comprehensive, atomic knowledge units (AKUs) covering the mathematical foundations of functional programming: **category theory**, **functors**, **monoids**, and **monads**.

**Purpose**: Provide a rigorous, language-agnostic knowledge foundation for a technical presentation on functional theory, suitable for rendering to multiple audience levels.

## ⚠️ Important: Ontology Note

> **Native Domain vs Application Domain**
> 
> Per the [Global Domain Hierarchy](../../../_ontology/global-hierarchy.yaml), category theory, 
> functors, monoids, and monads are **mathematically native** concepts that belong in:
> `formal-sciences/mathematics/pure-mathematics/category-theory/`
> 
> This domain (`functional-theory`) contains **APPLICATION AKUs** that explain how these 
> mathematical concepts are **used in functional programming**. The AKUs here provide 
> programming-specific context, code examples, and practical applications.
> 
> **Migration Status**: See Issue #3 for the plan to properly separate native mathematical 
> definitions from programming applications with cross-domain linking.

## Placement and Cross-Domain Alignment

- **Current Location**: `science/computer-science/functional-theory/`
- **Global Hierarchy Path**: `formal-sciences/computer-science/programming-paradigms/functional-programming`
- **Native Math Location**: `formal-sciences/mathematics/pure-mathematics/category-theory/`

### Cross-Domain Linking Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                    MATHEMATICS (Native Domain)                   │
│  formal-sciences/mathematics/pure-mathematics/category-theory/  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ • Category definitions                                      ││
│  │ • Functor theorems                                          ││
│  │ • Monad axioms                                              ││
│  │ • Mathematical proofs                                       ││
│  └─────────────────────────────────────────────────────────────┘│
└───────────────────────────┬─────────────────────────────────────┘
                            │ uses/applies
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              COMPUTER SCIENCE (Application Domain)              │
│  formal-sciences/computer-science/programming-paradigms/fp/     │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ • Programming examples (Haskell, Scala, etc.)               ││
│  │ • Practical applications (error handling, async)            ││
│  │ • Code patterns and idioms                                  ││
│  │ • Cross-domain LINKS to math definitions                    ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

## Domain Structure

```
functional-theory/
├── category-theory/     # 8 AKUs - Foundations
│   └── akus/
├── functors/            # 6 AKUs - Structure-preserving maps
│   └── akus/
├── monoids/             # 5 AKUs - Algebraic aggregation
│   └── akus/
├── monads/              # 8 AKUs - Effectful composition
│   └── akus/
├── concept-index.yaml   # Complete relationship graph
└── README.md           # This file
```

## Rendered Presentations

This domain has been rendered into multiple formats:

| File | Description | Lines |
|------|-------------|-------|
| `technical-presentation.md` | 60-minute talk with jokes | 918 |
| `undergraduate-guide.md` | CS student learning guide | ~600 |
| `quick-reference.md` | Cheat sheet / reference card | ~350 |
| `advanced-research.md` | Graduate/researcher guide | ~700 |
| `powerpoint-visualization.md` | **NEW** Visual diagrams & slides | 1,390 |

## Content Coverage

### Category Theory (8 AKUs)
Foundation of the entire domain - objects, morphisms, composition, and laws.

- **ct-001**: Historical origins (Eilenberg & Mac Lane, 1945)
- **ct-002**: Category definition (objects, morphisms, composition, identity)
- **ct-003**: Morphisms (arrows, structure preservation)
- **ct-004**: Composition operation (chaining morphisms)
- **ct-005**: Identity morphisms (neutral elements)
- **ct-006**: Category laws (associativity, identity)
- **ct-007**: Examples of categories (Set, Grp, Top, Poset, Vect, etc.)
- **ct-008**: Universal properties (products, limits, abstract characterization)

### Functors (6 AKUs)
Mappings between categories that preserve structure.

- **fn-001**: Functor definition (structure-preserving maps between categories)
- **fn-002**: Functor laws (identity and composition preservation)
- **fn-003**: Mathematical examples (power set, free groups, forgetful, homology)
- **fn-004**: Programming perspective (map operation, type constructors)
- **fn-005**: Language implementations (Haskell, Scala, JavaScript, Rust, Python)
- **fn-006**: Endofunctors (functors from category to itself - foundation for monads)

### Monoids (5 AKUs)
Algebraic structures with associative operations and identity.

- **mo-001**: Monoid definition (set, operation, identity element)
- **mo-002**: Monoid laws (associativity, identity)
- **mo-003**: Examples (addition, multiplication, concatenation, composition)
- **mo-004**: Monoids in programming (type classes, generic aggregation)
- **mo-005**: Reduce/fold operations (foundation of MapReduce)

### Monads (8 AKUs)
Endofunctors with unit and join for composing effectful computations.

- **md-001**: Monad definition (endofunctor, unit/return, join/bind)
- **md-002**: Monad laws (left/right identity, associativity)
- **md-003**: Why monads matter (composing effects, Kleisli arrows)
- **md-004**: Kleisli category (category of effectful computations)
- **md-005**: Common examples (Maybe, List, IO, State, Reader, Writer, Either)
- **md-006**: Language implementations (do-notation, for-comprehension, async/await)
- **md-007**: Monad tutorial fallacy (pedagogy and learning)
- **md-008**: Monads as monoids (connection to algebraic structures)

## Key Insights

### The Grand Unification
This domain reveals deep connections:
- **Categories** provide the foundational structure (objects + morphisms)
- **Functors** are morphisms between categories
- **Monoids** are simple algebraic structures (operation + identity)
- **Monads** are monoids in the category of endofunctors

### Cross-Domain Links
- **Mathematics**: Abstract algebra, topology, set theory, logic
- **Computer Science**: Type theory, functional programming, error handling, async programming
- **Practical Applications**: MapReduce, effect systems, compositional programming

## Quality Metrics

- **Total AKUs**: 27
- **Validation Status**: ✅ All 27 valid
- **Language Agnostic**: Yes
- **Scientifically Rigorous**: Yes
- **Code Examples**: Haskell, Scala, JavaScript, Python, Rust, C#, Swift
- **Cross-References**: 150+ concept links
- **Provenance**: Peer-reviewed sources (Mac Lane, Awodey, Moggi, Wadler)

## Learning Paths

### For Beginners
Start with concrete examples, build to abstraction:
1. Monoids (most concrete - addition, concatenation)
2. Functors in programming (map operation)
3. Monad examples (Maybe, List, Promise)
4. Category theory foundations

### For Mathematicians
Start with theory, build to applications:
1. Category theory foundations
2. Functors as category morphisms
3. Universal properties
4. Monads as categorical structures

### For Programmers
Start with practical use, build to understanding:
1. Map operations (functors)
2. Reduce/fold (monoids)
3. Promise chains, async/await (monads)
4. Theoretical foundations

## Usage

### Validation
```bash
# Validate all AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/science/computer-science/functional-theory/

# Validate specific subdomain
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/science/computer-science/functional-theory/monads/akus/
```

### Rendering
AKUs are language-agnostic and ready for rendering to multiple formats and audience levels:
- Elementary school (simplified analogies)
- High school (concrete examples)
- Undergraduate (mathematical rigor)
- Graduate (full category theory)
- Expert (research-level insights)

### Integration
Use `concept-index.yaml` for:
- Navigation and discovery
- Prerequisite tracking
- Learning path generation
- Cross-domain exploration
- Visualization generation

## Contributing

When adding new AKUs:
1. Maintain atomicity (one concept per AKU)
2. Follow the JSON-LD schema
3. Include proper metadata (timestamps, contributors, confidence)
4. Establish relationships (prerequisites, enables, related_to)
5. Provide cross-domain links
6. Add provenance (sources, citations)
7. Validate with `validate_aku_v2.py`
8. Update `concept-index.yaml`

## References

### Primary Sources
- Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.
- Awodey, S. (2010). *Category Theory* (2nd ed.). Oxford University Press.
- Moggi, E. (1991). Notions of computation and monads. *Information and Computation*, 93(1), 55-92.
- Wadler, P. (1992). The essence of functional programming. *POPL '92*.

### Online Resources
- nLab: https://ncatlab.org/nlab/
- Haskell Wiki: https://wiki.haskell.org/
- Scala Cats: https://typelevel.org/cats/

## Metadata

- **Created**: 2026-01-03T23:36:18.481Z
- **Version**: 1.0.0
- **Status**: Complete
- **Contributors**: knowledge-graph-agent
- **Domain Path**: science/computer-science/functional-theory
- **License**: Knowledge commons (educational use)

---

**Note for Presenters**: This knowledge base is designed for a fun, hour-long technical presentation. The entertainment happens at rendering time - the AKUs themselves are rigorous and language-agnostic. Use the learning paths and concept index to tailor the presentation to your audience.
