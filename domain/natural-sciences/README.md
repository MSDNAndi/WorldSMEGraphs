# Natural Sciences

> **Domain Path**: `natural-sciences/`  
> **UNESCO Code**: 05 (Natural Sciences, Mathematics, and Statistics)  
> **Library of Congress**: Q (Science)  
> **Version**: 1.0.0  
> **Created**: 2026-01-04

## Overview

The Natural Sciences are empirical sciences that study the natural world through observation and experimentation. Unlike formal sciences (which use deductive reasoning from axioms), natural sciences rely on the scientific method: hypothesis, experimentation, observation, and conclusion.

## What are Natural Sciences?

Natural sciences study:
- **Physical phenomena**: Matter, energy, forces, space, time
- **Living organisms**: Life, evolution, ecosystems, biological processes  
- **Earth systems**: Geology, atmosphere, oceans, climate
- **Celestial objects**: Stars, galaxies, cosmology

**Key Methodology**: Empirical observation + experimentation + peer review

## Subdomain Structure

### Physics

**Path**: `natural-sciences/physics/`  
**Coverage**: All branches of physics

**Content (136 AKUs migrated 2026-01-04)**:
- **Measurement Limits** - Theoretical and practical measurement boundaries
  - Minimum measurable quantities (18 AKUs)
  - Theoretical minimum limits (12 AKUs)
- **Quantum Mechanics** - Physics at atomic and subatomic scales
  - Planck units and quantum scales (74 AKUs)
- **Cosmology** - Study of the universe's origin and evolution (2 AKUs)
- **General Relativity** - Spacetime and gravity (1 AKU)
- **Particle Physics** - Fundamental particles and forces (2 AKUs)
- **Atomic Physics** - Structure and behavior of atoms (1 AKU)

### Chemistry

**Path**: `natural-sciences/chemistry/`  
**Status**: ⏳ Pending migration from `science/chemistry/`

**Planned Coverage**:
- General Chemistry
- Organic Chemistry
- Inorganic Chemistry
- Physical Chemistry
- Biochemistry

### Biology

**Path**: `natural-sciences/biology/`  
**Status**: ⏳ Pending migration from `science/biology/`

**Planned Coverage**:
- Molecular Biology
- Cell Biology
- Genetics
- Evolution
- Ecology
- Physiology

### Earth Sciences

**Path**: `natural-sciences/earth-sciences/`  
**Status**: ⏳ Pending migration

**Planned Coverage**:
- Geology
- Meteorology
- Oceanography

### Astronomy

**Path**: `natural-sciences/astronomy/`  
**Status**: ⏳ Pending migration

**Planned Coverage**:
- Stellar Astronomy
- Planetary Science
- Galactic Astronomy
- Cosmology

## Cross-Domain Applications

Natural sciences provide empirical foundations for many other domains:

### Engineering
- **All Branches**: Apply physics, chemistry, and materials science
- **Example**: Chemical engineering applies physical chemistry and thermodynamics

### Health Sciences
- **Medicine**: Applies biology, chemistry, and physiology
- **Pharmacy**: Applies chemistry and biochemistry
- **Example**: Drug development uses organic chemistry and molecular biology

### Formal Sciences
- **Mathematics**: Provides theoretical frameworks (e.g., mathematical physics)
- **Computer Science**: Physics inspires quantum computing

### Social Sciences
- **Environmental Studies**: Integrates ecology, geology, climatology
- **Psychology**: Draws on neuroscience and biological processes

## Native Domain Principle

Natural sciences concepts belong here even when applied extensively elsewhere:

| Concept | Native Domain | Application Domains |
|---------|---------------|---------------------|
| Quantum Mechanics | Physics | Chemistry (QM chemistry), CS (quantum computing) |
| Thermodynamics | Physics | Chemistry (chemical thermodynamics), Engineering |
| Evolution | Biology | Social Sciences (evolutionary psychology) |
| Plate Tectonics | Earth Sciences | Engineering (seismology) |

## Migration Status

**Created**: 2026-01-04  
**Status**: Initial structure with physics migrated

### Migrated Content
- ✅ **Physics** (136/138 AKUs) migrated from `science/physics/`
  - All AKUs marked as native domain
  - Domain paths updated to `natural-sciences/physics/*`
  - Timestamps updated to 2026-01-04

### Pending Migrations
- ⏳ Chemistry content from `science/chemistry/`
- ⏳ Biology content from `science/biology/`
- ⏳ Earth sciences content (if exists)

## Content Statistics

**Current AKUs**: 136 (physics)  
**Pending Migrations**: Chemistry, Biology, Earth Sciences  
**Target**: Comprehensive coverage of all natural sciences

## Directory Structure

```
natural-sciences/
├── physics/                       ✅ 136 AKUs migrated
│   ├── measurement-limits/
│   │   ├── minimum-measurable-quantities/    (18 AKUs)
│   │   └── theoretical-minimum-limits/       (12 AKUs)
│   ├── quantum-mechanics/
│   │   └── planck-units/                     (74 AKUs)
│   ├── cosmology/                            (2 AKUs)
│   ├── general-relativity/                   (1 AKU)
│   ├── particle-physics/                     (2 AKUs)
│   └── atomic-physics/                       (1 AKU)
│
├── chemistry/                     ⏳ Pending
│   ├── general-chemistry/
│   ├── organic-chemistry/
│   ├── inorganic-chemistry/
│   ├── physical-chemistry/
│   └── biochemistry/
│
├── biology/                       ⏳ Pending
│   ├── molecular-biology/
│   ├── cell-biology/
│   ├── genetics/
│   ├── evolution/
│   ├── ecology/
│   └── physiology/
│
├── earth-sciences/                ⏳ Pending
│   ├── geology/
│   ├── meteorology/
│   └── oceanography/
│
└── astronomy/                     ⏳ Pending
    ├── stellar-astronomy/
    ├── planetary-science/
    └── cosmology/
```

## References

### Classification Standards
- UNESCO ISCED-F 2013: Field 05 (Natural Sciences, Mathematics, and Statistics)
- Library of Congress Classification (Q: Science)
- Dewey Decimal Classification (500: Natural Sciences and Mathematics)

### Foundational Documents
- `domain/_ontology/global-hierarchy.yaml` - Authoritative taxonomy
- `domain/_ontology/README.md` - Design principles
- `domain/_ontology/MIGRATION-GUIDE.md` - Migration patterns
- `domain/_contexts/science.jsonld` - Scientific vocabulary

## Contributing

When adding content to natural sciences:

1. **Verify Empirical Nature**: Ensure concept is based on observation/experimentation
2. **Check Existing Structure**: Use established subdomain paths
3. **Mark Domain Status**: Set `isNativeDomain: true` for native concepts
4. **Follow Scientific Method**: Content should reflect empirical evidence
5. **Follow AKU Format**: Use AKU v2.0 specification
6. **Validate**: Run validation tools before committing

## Validation

```bash
# Validate physics AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/natural-sciences/physics/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/natural-sciences/physics/
```

## Related Domains

- **Formal Sciences** (`formal-sciences/`) - Mathematics, Computer Science (provide tools)
- **Engineering** (`engineering/`) - Applied natural sciences
- **Health Sciences** (`health-sciences/`) - Apply biology, chemistry, physics to medicine

---

**Authoritative Source**: This directory hierarchy follows the global ontology defined in `domain/_ontology/global-hierarchy.yaml`

**Questions?** See `domain/_ontology/README.md` for design principles and migration guidance.
