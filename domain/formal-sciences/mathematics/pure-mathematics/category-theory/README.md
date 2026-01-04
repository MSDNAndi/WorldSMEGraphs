# Category Theory

> **Domain Path**: `formal-sciences/mathematics/pure-mathematics/category-theory`  
> **Native Domain**: ✅ Yes (This is the authoritative location)  
> **Version**: 1.0.0  
> **Last Updated**: 2026-01-04

## Overview

Category theory is a branch of pure mathematics that provides a unified framework for studying mathematical structures and their relationships. Developed by Samuel Eilenberg and Saunders Mac Lane in 1945 for algebraic topology, it has become fundamental to modern mathematics and has found important applications in computer science, physics, and logic.

## What is Category Theory?

Category theory studies abstract structures by focusing on **relationships** (morphisms) rather than internal properties of objects. A category consists of:

1. **Objects**: Mathematical entities (sets, groups, spaces, types, etc.)
2. **Morphisms**: Structure-preserving maps between objects (functions, homomorphisms, etc.)
3. **Composition**: A way to combine morphisms
4. **Identity**: A neutral morphism for each object

The power of category theory lies in its ability to reveal deep connections between seemingly disparate areas of mathematics through common patterns.

## Content in This Directory

### Atomic Knowledge Units (AKUs)

This directory contains **8 foundational AKUs** covering:

- **ct-001**: Historical Origins - Eilenberg, Mac Lane, and the birth of category theory
- **ct-002**: Category Definition - Objects, morphisms, composition, identity
- **ct-003**: Morphisms (Arrows) - Structure-preserving maps
- **ct-004**: Composition Operation - Chaining morphisms
- **ct-005**: Identity Morphisms - Neutral elements
- **ct-006**: Category Axioms and Laws - Associativity and identity laws
- **ct-007**: Examples of Categories - Set, Grp, Top, Vect, and more
- **ct-008**: Universal Properties - Characterizing objects by their relationships

### Why This Location?

Per the **Global Domain Hierarchy** (`domain/_ontology/global-hierarchy.yaml`), category theory belongs in pure mathematics because:

1. **Native Domain**: Developed as pure mathematics for algebraic topology
2. **Mathematical Nature**: Studies abstract mathematical structures
3. **Foundational**: Provides unifying language for mathematics
4. **Origin**: Created by mathematicians (Eilenberg, Mac Lane) for mathematics

Even though category theory is heavily used in:
- Computer Science (functional programming, type theory)
- Physics (quantum mechanics, topological quantum field theory)
- Logic (categorical logic, topos theory)

...it remains fundamentally mathematical in nature.

## Cross-Domain Applications

Category theory has profound applications across multiple domains:

### Computer Science

**Location**: `formal-sciences/computer-science/`

- **Functional Programming**: Monads, functors, and composition patterns
- **Type Theory**: Categorical semantics of types
- **Programming Languages**: Haskell, Scala, and type systems

See: `formal-sciences/computer-science/programming-paradigms/functional-programming/`

### Physics

**Location**: `natural-sciences/physics/`

- **Quantum Mechanics**: Monoidal categories and quantum computing
- **Topological Quantum Field Theory**: Categories and topology
- **String Theory**: Higher category theory

### Logic

**Location**: `formal-sciences/mathematics/pure-mathematics/logic/`

- **Categorical Logic**: Semantics for logical systems
- **Topos Theory**: Generalized set theory
- **Proof Theory**: Curry-Howard correspondence

## Key Concepts

### Core Abstractions

1. **Categories**: Collections of objects and morphisms with composition
2. **Functors**: Structure-preserving maps between categories
3. **Natural Transformations**: Morphisms between functors
4. **Limits and Colimits**: Universal constructions
5. **Adjunctions**: Deep connections between categories
6. **Monads**: Monoids in the category of endofunctors

### Mathematical Examples

- **Set**: Category of sets and functions
- **Grp**: Category of groups and homomorphisms
- **Top**: Category of topological spaces and continuous maps
- **Vect**: Category of vector spaces and linear maps
- **Poset**: Partially ordered sets as categories

## Learning Path

### For Mathematicians
1. Start with ct-001 (Historical Origins)
2. Master ct-002 through ct-006 (Foundations)
3. Study ct-007 (Examples) to see concrete instances
4. Explore ct-008 (Universal Properties) for deeper understanding

### For Programmers
While this directory contains the **mathematical definitions**, programmers should also explore:
- `formal-sciences/computer-science/programming-paradigms/functional-programming/` for programming applications
- Start with concrete examples (map, filter, compose)
- Connect back to mathematical foundations when ready

## Prerequisites

- **Mathematics**: Abstract algebra (groups, rings), set theory
- **Maturity**: Graduate-level mathematical thinking
- **Comfort**: Working with abstract definitions and proofs

## References

### Foundational Papers
- Eilenberg, S., & Mac Lane, S. (1945). "General Theory of Natural Equivalences." *Transactions of the American Mathematical Society*, 58(2), 231-294.

### Standard Textbooks
- Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.
- Awodey, S. (2010). *Category Theory* (2nd ed.). Oxford University Press.
- Leinster, T. (2014). *Basic Category Theory*. Cambridge University Press.

### Online Resources
- nLab: https://ncatlab.org/nlab/show/category+theory
- Category Theory for Programmers: https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/

## Related Domains

### Within Mathematics
- **Algebra**: `formal-sciences/mathematics/pure-mathematics/algebra/`
- **Topology**: `formal-sciences/mathematics/pure-mathematics/topology/`
- **Logic**: `formal-sciences/mathematics/pure-mathematics/logic/`

### Applications
- **Functional Programming**: `formal-sciences/computer-science/programming-paradigms/functional-programming/`
- **Type Theory**: `formal-sciences/computer-science/type-theory/`
- **Quantum Physics**: `natural-sciences/physics/quantum-physics/`

## Ontology Notes

### Native Domain Status

This directory contains the **native, authoritative definitions** of category theory concepts. All other domains that use category theory should:

1. **Link to these AKUs** via `cross_domain_references`
2. **Not duplicate** mathematical content
3. **Provide application context** in their own domains
4. **Use relationship types**: `applies`, `uses`, `extends`

Example from functional programming:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "aku:math:category-theory:monad-definition",
      "relationship": "applies",
      "context": "Monads structure effectful computations in FP"
    }]
  }
}
```

### Migration History

- **2026-01-04**: Category theory AKUs migrated from `science/computer-science/functional-theory/category-theory/` to this location
- **Reason**: Ontological rigor - concepts belong to their native domain of origin
- **Impact**: Establishes clear separation between mathematical definitions and programming applications

See: `domain/_ontology/MIGRATION-GUIDE.md` for details

## Validation

To validate AKUs in this directory:

```bash
# Validate all category theory AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/
```

## Contributing

When adding new category theory AKUs:

1. **Follow AKU v2.0 format** (see `.project/knowledge-format.md`)
2. **Use mathematical rigor** - this is pure mathematics
3. **Mark as native domain**: `isNativeDomain: true`
4. **Document applications**: Use `cross_domain_applications` section
5. **Provide examples**: Both mathematical and (if relevant) computational
6. **Include prerequisites**: Reference earlier AKUs as needed
7. **Update this README**: Keep the AKU list current

## Status

- **AKUs**: 8 foundational concepts (complete)
- **Validation**: All AKUs validated ✅
- **Cross-Links**: Documented in `cross_domain_applications`
- **Maturity**: Stable
- **Coverage**: Core foundations established

## Future Work

Potential expansions:
- Functors and natural transformations (currently in functional-theory)
- Limits and colimits
- Adjunctions
- Monads (mathematical definition)
- Kan extensions
- Enriched categories
- Higher category theory

---

**Authoritative Source**: This is the canonical location for category theory in WorldSMEGraphs. All references to category theory concepts should point here.

**Questions?** See `domain/_ontology/README.md` for ontology design principles.
