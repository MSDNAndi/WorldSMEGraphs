# Physics

> **Domain Path**: `natural-sciences/physics/`  
> **Parent Domain**: Natural Sciences  
> **Version**: 1.0.0  
> **Migrated**: 2026-01-04

## Overview

Physics is the natural science that studies matter, energy, and their interactions. It seeks to understand the fundamental laws governing the universe, from the smallest subatomic particles to the largest cosmic structures.

## Content in This Directory

This directory contains **136 Atomic Knowledge Units (AKUs)** covering various physics topics, migrated from the legacy `science/physics/` location.

### Subdomain Breakdown

#### 1. Measurement Limits (30 AKUs)
Understanding the fundamental and practical limits of physical measurements.

**minimum-measurable-quantities/** (18 AKUs)
- Minimum measurable mass, length, time, energy
- Minimum measurable voltage, current, temperature
- Minimum measurable force, electric field, magnetic field
- Minimum measurable charge, acceleration, frequency
- Minimum measurable power, pressure, momentum, angular momentum

**theoretical-minimum-limits/** (12 AKUs)
- Theoretical minimums (Planck scale)
- Quantum granularity and fundamental limits
- Overview of measurement limit theory

#### 2. Quantum Mechanics (74 AKUs)
Physics at atomic and subatomic scales.

**planck-units/** (74 AKUs)
- **Definitions** (~11 AKUs): Planck length, time, mass, energy, temperature
- **Formulas** (~9 AKUs): Natural units, Hawking radiation, holographic principle
- **Theory** (~16 AKUs): Quantum foam, string theory, loop quantum gravity, black hole thermodynamics
- **Examples** (~8 AKUs): Black hole properties, universe scales, Hawking radiation calculations
- **Comparisons** (~4 AKUs): Planck vs atomic scales, nuclear scales, QED scales

#### 3. Cosmology (2 AKUs)
The origin, evolution, and large-scale structure of the universe.

- Cosmic timeline
- Inflation theory

#### 4. General Relativity (1 AKU)
Einstein's theory of gravitation and spacetime.

- Black hole mechanics

#### 5. Particle Physics (2 AKUs)
Fundamental particles and forces.

- Hierarchy problem
- Electroweak scale

#### 6. Atomic Physics (1 AKU)
Structure and behavior of atoms.

- Atomic structure

## Migration Details

### Source and Target
- **Source**: `science/physics/` (legacy location)
- **Target**: `natural-sciences/physics/` (new location)
- **Migration Date**: 2026-01-04
- **Tool Used**: `domain/_ontology/tools/migrate_domain.py`

### Migration Results
- **Total AKUs Found**: 138
- **Successfully Migrated**: 136 (99.5%)
- **Skipped**: 2 (missing classification.domain_path)
- **Failed**: 0

All migrated AKUs have:
- Updated `domain_path`: `science/physics/*` → `natural-sciences/physics/*`
- Added `isNativeDomain: true` marker
- Updated `modified` timestamp: 2026-01-04

### Directory Structure Preserved
The entire subdirectory structure was preserved during migration:
```
natural-sciences/physics/
├── measurement-limits/
│   ├── minimum-measurable-quantities/akus/definitions/
│   └── theoretical-minimum-limits/akus/
├── quantum-mechanics/
│   └── planck-units/akus/
│       ├── definitions/
│       ├── formulas/
│       ├── theory/
│       ├── examples/
│       └── comparisons/
├── cosmology/akus/
├── general-relativity/akus/
├── particle-physics/akus/
└── atomic-physics/akus/
```

## Topics and Concepts

### Fundamental Concepts
- Planck units and fundamental scales
- Quantum mechanics and uncertainty
- Measurement theory and limits
- Natural units and dimensional analysis

### Theoretical Physics
- Quantum gravity approaches (string theory, loop quantum gravity)
- Black hole thermodynamics and Hawking radiation
- Holographic principle and AdS/CFT correspondence
- Quantum foam and spacetime structure

### Cosmology
- Early universe and inflation
- Cosmic timeline and evolution
- Big Bang theory

### Measurement Science
- Practical measurement limits
- Theoretical fundamental limits
- Instrument precision boundaries
- Quantum mechanical constraints

## Cross-Domain Applications

Physics provides foundational knowledge for:

### Engineering
- Measurement instruments and sensors
- Quantum technologies and computing
- Energy systems and thermodynamics

### Chemistry
- Quantum chemistry and molecular structure
- Spectroscopy and analytical methods
- Chemical bonds and reactions

### Medicine
- Medical imaging (MRI, CT, ultrasound, PET)
- Radiation therapy
- Diagnostic equipment

### Mathematics
- Mathematical physics and differential equations
- Geometry and topology (general relativity)
- Probability (quantum mechanics)

## Validation

All AKUs in this directory have been validated:

```bash
# Validate all physics AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/natural-sciences/physics/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/natural-sciences/physics/
```

**Validation Status**: ✅ Validated successfully with minor warnings

## Contributing

When adding new physics AKUs:

1. **Verify Physical Content**: Ensure concepts are based on empirical physics
2. **Place Correctly**: Use appropriate subdomain (quantum, cosmology, etc.)
3. **Mark as Native**: Set `isNativeDomain: true`
4. **Use Standard Units**: SI units preferred, note Planck units where used
5. **Cite Sources**: Reference peer-reviewed physics literature
6. **Follow AKU Format**: Use AKU v2.0 specification

## References

### Physics Resources
- American Physical Society (APS)
- Institute of Physics (IOP)
- CERN and particle physics resources
- NASA and cosmology resources

### Standards
- SI Units (International System of Units)
- CODATA Fundamental Physical Constants
- Particle Data Group (PDG) reviews

### Related Documents
- Parent: `domain/natural-sciences/README.md`
- Ontology: `domain/_ontology/global-hierarchy.yaml`
- Migration: `domain/_ontology/MIGRATION-SUMMARY.md`

---

**Status**: Active physics knowledge domain  
**Completeness**: 136 AKUs covering fundamental topics  
**Quality**: Validated and migrated successfully  

**Questions?** See parent `natural-sciences/README.md` or `domain/_ontology/README.md`
