# Formal Sciences

> **Domain Path**: `formal-sciences/`  
> **UNESCO Code**: 05 (partial - formal aspects of natural sciences)  
> **Library of Congress**: QA, BC  
> **Version**: 1.0.0  
> **Created**: 2026-01-04

## Overview

The Formal Sciences are disciplines that study abstract structures and formal systems using deductive methodology. Unlike empirical sciences, formal sciences do not depend on observation of the physical world; instead, they use logic and mathematics to derive conclusions from axioms and definitions.

## Why Separate from Natural Sciences?

Formal sciences are distinguished from natural sciences by their methodology and subject matter:

1. **Methodology**: Deductive reasoning from axioms, not empirical observation
2. **Subject Matter**: Abstract structures, not physical phenomena  
3. **Truth Criteria**: Logical consistency, not empirical verification
4. **Applications**: Provide tools and frameworks for all other sciences

## Subdomain Structure

### Mathematics

**Path**: `formal-sciences/mathematics/`  
**Coverage**: All branches of mathematics

#### Pure Mathematics
Study of mathematics for its own sake, developing abstract theories and structures.

**Subdomains**:
- **Category Theory** (`pure-mathematics/category-theory/`) ✅ 8 AKUs
  - Objects, morphisms, composition
  - Foundational framework for mathematics
  - Native domain for functors, monads
- **Algebra** (`pure-mathematics/algebra/`)
  - Linear algebra, abstract algebra
  - Groups, rings, fields, modules
  - Native domain for monoids, semigroups
- **Analysis** (`pure-mathematics/analysis/`)
  - Calculus, real analysis, functional analysis
- **Topology** (`pure-mathematics/topology/`)
  - Point-set topology, algebraic topology
- **Number Theory** (`pure-mathematics/number-theory/`)
  - Primes, diophantine equations
- **Geometry** (`pure-mathematics/geometry/`)
  - Euclidean, non-Euclidean, algebraic geometry
- **Logic** (`pure-mathematics/logic/`)
  - Mathematical logic, proof theory, type theory

#### Applied Mathematics
Mathematics applied to solve real-world problems.

**Subdomains**:
- **Numerical Analysis**
- **Probability Theory**
- **Statistics**
- **Operations Research**
- **Mathematical Physics**
- **Mathematical Economics**

### Computer Science

**Path**: `formal-sciences/computer-science/`  
**Coverage**: Theoretical and applied computing

#### Theoretical Computer Science
- **Automata Theory**
- **Computational Complexity**
- **Type Theory** - Uses category theory concepts
- **Algorithms**

#### Programming Paradigms
- **Functional Programming** (`programming-paradigms/functional-programming/`)
  - **Application domain** for category theory concepts
  - Links to mathematical definitions in pure mathematics
  - Contains programming-specific context and code examples
- **Object-Oriented Programming**
- **Imperative Programming**
- **Logic Programming**

#### Software Engineering
- Architecture, design patterns, testing, DevOps

#### Artificial Intelligence
- **Machine Learning** - Uses linear algebra, statistics, probability
- **Natural Language Processing**
- **Computer Vision**

#### Data Structures and Databases
- Trees, graphs, hash tables
- Relational and NoSQL databases

#### Systems
- Operating systems, distributed systems, networking

## Cross-Domain Applications

Formal sciences provide foundational tools for all other domains:

### Natural Sciences
- **Physics**: Uses calculus, differential equations, linear algebra
- **Chemistry**: Uses quantum mechanics (linear algebra), thermodynamics
- **Biology**: Uses statistics, probability, computational methods

### Social Sciences
- **Economics**: Uses mathematical economics, optimization, game theory
- **Psychology**: Uses statistics for research
- **Sociology**: Uses network analysis, statistical methods

### Engineering
- **All Branches**: Use calculus, linear algebra, numerical methods
- **Computer Engineering**: Direct application of CS theory

### Health Sciences
- **Medicine**: Uses statistics (epidemiology, clinical trials)
- **Bioinformatics**: Uses algorithms, machine learning

## Native Domain Principle

**Critical Concept**: Formal sciences concepts belong to their **native** domain, even when heavily used elsewhere.

### Example: Category Theory
- **Native Domain**: `formal-sciences/mathematics/pure-mathematics/category-theory/`
- **Application Domains**: 
  - Computer Science (functional programming, type theory)
  - Physics (quantum mechanics, topological quantum field theory)
  - Logic (categorical logic)

**Pattern**:
- Mathematical definitions → Live in mathematics
- Programming applications → Live in CS, **link to** mathematics
- Physics applications → Live in physics, **link to** mathematics

See: `domain/_ontology/global-hierarchy.yaml` for complete taxonomy

## Migration Status

**Created**: 2026-01-04  
**Status**: Initial structure established

### Migrated Content
- ✅ Category Theory (8 AKUs) from `science/computer-science/functional-theory/category-theory/`
  - All AKUs marked as native domain
  - Cross-domain applications documented
  - Comprehensive README created

### Pending Migrations
- ⏳ Remaining mathematics content from `science/math/`
- ⏳ Other computer science content from `science/computer-science/`

## Content Statistics

**Current AKUs**: 8 (category theory)  
**Pending Migrations**: ~100+ mathematics and CS AKUs  
**Target**: Comprehensive coverage of formal sciences

## Directory Structure

```
formal-sciences/
├── mathematics/
│   ├── pure-mathematics/
│   │   ├── category-theory/          ✅ 8 AKUs
│   │   │   ├── akus/
│   │   │   └── README.md
│   │   ├── algebra/                  ⏳ Pending
│   │   ├── analysis/                 ⏳ Pending
│   │   ├── topology/                 ⏳ Pending
│   │   ├── number-theory/            ⏳ Pending
│   │   ├── geometry/                 ⏳ Pending
│   │   └── logic/                    ⏳ Pending
│   └── applied-mathematics/
│       ├── numerical-analysis/
│       ├── probability-theory/
│       ├── statistics/
│       └── operations-research/
│
└── computer-science/
    ├── theoretical-computer-science/
    │   ├── automata-theory/
    │   ├── computational-complexity/
    │   ├── type-theory/
    │   └── algorithms/
    ├── programming-paradigms/
    │   ├── functional-programming/   ⏳ Future home for FP
    │   ├── object-oriented-programming/
    │   └── logic-programming/
    ├── artificial-intelligence/
    │   ├── machine-learning/
    │   └── natural-language-processing/
    └── systems/
        ├── operating-systems/
        └── distributed-systems/
```

## References

### Classification Standards
- UNESCO ISCED-F 2013: International Standard Classification of Education - Fields
- Library of Congress Classification (QA: Mathematics, BC: Logic)
- Dewey Decimal Classification (510: Mathematics, 004: Computer Science)
- Mathematics Subject Classification (MSC 2020)
- ACM Computing Classification System

### Foundational Documents
- `domain/_ontology/global-hierarchy.yaml` - Authoritative taxonomy
- `domain/_ontology/README.md` - Design principles
- `domain/_ontology/MIGRATION-GUIDE.md` - Migration patterns
- `domain/_contexts/cross-domain.jsonld` - Cross-domain vocabulary

## Contributing

When adding content to formal sciences:

1. **Verify Native Domain**: Ensure concept belongs to formal sciences
2. **Check Existing Structure**: Use established subdomain paths
3. **Mark Domain Status**: Set `isNativeDomain: true` for native concepts
4. **Document Applications**: Use `cross_domain_applications` for usage in other domains
5. **Follow AKU Format**: Use AKU v2.0 specification
6. **Validate**: Run validation tools before committing

## Validation

```bash
# Validate category theory AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/
```

## Related Domains

- **Natural Sciences** (`natural-sciences/`) - Empirical study of physical world
- **Social Sciences** (`social-sciences/`) - Study of human society and behavior
- **Engineering** (`engineering/`) - Applied sciences for practical problems

---

**Authoritative Source**: This directory hierarchy follows the global ontology defined in `domain/_ontology/global-hierarchy.yaml`

**Questions?** See `domain/_ontology/README.md` for design principles and migration guidance.
