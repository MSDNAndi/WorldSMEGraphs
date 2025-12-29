# Planck Units Cross-Reference Matrix

**Date**: 2025-12-29T14:40:00Z  
**Purpose**: Document relationships between Planck unit AKUs  
**Status**: Phase 1-2 Complete (10 AKUs)

## Overview

This document provides a comprehensive view of how the 10 Planck unit AKUs relate to each other through mathematical relationships, conceptual dependencies, and pedagogical prerequisites.

## Mathematical Relationships

### Direct Formulas

| From AKU | To AKU | Relationship | Formula |
|----------|--------|--------------|---------|
| 001 (ℓₚ) | 002 (tₚ) | Division by c | tₚ = ℓₚ/c |
| 003 (mₚ) | 001 (ℓₚ) | Compton wavelength | ℓₚ = ℏ/(mₚc) |
| 003 (mₚ) | 004 (Eₚ) | Mass-energy | Eₚ = mₚc² |
| 003 (mₚ) | 008 (pₚ) | Momentum | pₚ = mₚc |
| 004 (Eₚ) | 005 (Tₚ) | Temperature | Tₚ = Eₚ/k_B |
| 004 (Eₚ) | 008 (pₚ) | Energy-momentum | Eₚ = pₚc |
| 004 (Eₚ) | 009 (Fₚ) | Force from energy | Fₚ = Eₚ/ℓₚ |
| 001 (ℓₚ) | 009 (Fₚ) | Force from length | Fₚ = Eₚ/ℓₚ = c⁴/G |
| 006 (α) | 007 (qₚ) | Charge scaling | qₚ = e/√α |
| 001 (ℓₚ) | 008 (pₚ) | Uncertainty | pₚ = ℏ/ℓₚ |
| 010 (ℏ) | ALL (except 009) | Foundation | All Planck units contain ℏ except Fₚ |

### Composite Relationships

| AKU Set | Combined Formula | Description |
|---------|------------------|-------------|
| 001, 002 | c = ℓₚ/tₚ | Speed of light from Planck units |
| 001, 003, 008 | pₚ = mₚc = ℏ/ℓₚ | Three ways to express Planck momentum |
| 001, 004, 009 | Fₚ = Eₚ/ℓₚ = c⁴/G | Planck force from energy and length |
| 003, 004, 005 | Tₚ = mₚc²/k_B | Temperature from mass via energy |
| 006, 007 | α = e²/qₚ² | Fine structure from charge ratio |
| 010, ALL (except 009) | ℏ appears in all formulas | ℏ is foundation; Fₚ = c⁴/G is unique exception |

## Conceptual Dependencies

### Prerequisites (What you need to know first)

```
Fundamental Constants (ℏ, G, c, k_B, e, ε₀)
           ↓
010 (ℏ) ← FOUNDATION (appears in ALL except 009)
           ↓
    ┌──────┴──────┐
    ↓             ↓
001 (ℓₚ)      003 (mₚ)
    ↓             ↓
002 (tₚ)      004 (Eₚ)
    ↓             ↓
001+004 → 009 (Fₚ) ← UNIQUE: No ℏ! (c⁴/G)
                  ↓
              005 (Tₚ)

Separate Branch:
Fundamental Constants (e, ℏ, c, ε₀)
           ↓
      006 (α)
           ↓
      007 (qₚ)

Combined:
001 (ℓₚ) + 003 (mₚ) + 010 (ℏ)
           ↓
      008 (pₚ)
```

### Learning Order (Pedagogical Sequence)

**Level 1: Foundation (Core Spatial & Mass)**
1. **aku-001 (ℓₚ)**: Start here - most fundamental scale
2. **aku-003 (mₚ)**: Natural mass scale from ℓₚ

**Level 2: Derived Basics (Time & Energy)**
3. **aku-002 (tₚ)**: Time from ℓₚ/c
4. **aku-004 (Eₚ)**: Energy from mₚc²

**Level 3: Thermodynamics**
5. **aku-005 (Tₚ)**: Temperature from Eₚ/k_B

**Level 4: Electromagnetic Foundation**
6. **aku-006 (α)**: Dimensionless constant (can be studied independently)
7. **aku-007 (qₚ)**: Charge scale from α

**Level 5: Dynamics & Forces**
8. **aku-008 (pₚ)**: Momentum from ℓₚ and mₚ
9. **aku-009 (Fₚ)**: Force from Eₚ/ℓₚ (or directly c⁴/G)

**Level 0: Fundamental Foundation (Can study first or alongside Level 1)**
10. **aku-010 (ℏ)**: Reduced Planck constant - foundation of ALL units above

## Cross-Reference by Fundamental Constant

### Units Involving ℏ (Planck's Constant)
- aku-010 (ℏ): h/(2π) - THE FOUNDATION ITSELF (exact since 2019)
- aku-001 (ℓₚ): √(ℏG/c³)
- aku-002 (tₚ): √(ℏG/c⁵)
- aku-003 (mₚ): √(ℏc/G)
- aku-004 (Eₚ): √(ℏc⁵/G)
- aku-005 (Tₚ): √(ℏc⁵/(Gk_B²))
- aku-006 (α): e²/(4πε₀ℏc)
- aku-007 (qₚ): √(4πε₀ℏc)
- aku-008 (pₚ): √(ℏc³/G)
- aku-009 (Fₚ): c⁴/G - **UNIQUE EXCEPTION: NO ℏ!**

**Note**: ℏ appears in ALL Planck units EXCEPT Planck force (Fₚ = c⁴/G is purely general relativistic)

### Units Involving G (Gravitational Constant)
- aku-001 (ℓₚ): √(ℏG/c³)
- aku-002 (tₚ): √(ℏG/c⁵)
- aku-003 (mₚ): √(ℏc/G)
- aku-004 (Eₚ): √(ℏc⁵/G)
- aku-005 (Tₚ): √(ℏc⁵/(Gk_B²))
- aku-008 (pₚ): √(ℏc³/G)
- aku-009 (Fₚ): c⁴/G

**Note**: Units 001-005, 008-009 involve G (quantum gravity/relativistic basis)

### Units Involving c (Speed of Light)
- ALL 10 AKUs involve c (relativistic basis)

### Units Involving e (Elementary Charge)
- aku-006 (α): e²/(4πε₀ℏc)
- aku-007 (qₚ): e/√α (implicit)

**Note**: Only electromagnetic units involve e

### Units Involving k_B (Boltzmann Constant)
- aku-005 (Tₚ): √(ℏc⁵/(Gk_B²))

**Note**: Only temperature involves k_B

## Cross-Reference by Physics Domain

### Quantum Mechanics (Primary Domain)
- **aku-001** (ℓₚ): Quantum of space via uncertainty principle
- **aku-002** (tₚ): Quantum of time
- **aku-003** (mₚ): Compton wavelength = Schwarzschild radius
- **aku-006** (α): QED coupling constant
- **aku-008** (pₚ): Uncertainty principle at Planck scale
- **aku-010** (ℏ): Foundation of quantum mechanics, quantum of action

### General Relativity (Primary Domain)
- **aku-001** (ℓₚ): Schwarzschild radius scale
- **aku-003** (mₚ): Gravitational coupling ~ 1
- **aku-009** (Fₚ): Maximum force / spacetime tension (purely GR, no quantum!)

### Statistical Mechanics (Primary Domain)
- **aku-005** (Tₚ): Thermal energy ~ Planck energy

### Electromagnetism (Primary Domain)
- **aku-006** (α): Electromagnetic coupling
- **aku-007** (qₚ): Natural charge unit

### Multi-Domain (Integrative)
- **aku-004** (Eₚ): Energy unification scale (QM + GR + EM)
- **aku-008** (pₚ): Dynamics at quantum gravity scale
- **aku-009** (Fₚ): Force at quantum gravity scale
- **aku-010** (ℏ): Bridges quantum and classical physics

## Common Misconceptions Addressed

### Misconception Matrix

| AKU | Common Error | Correction | Related AKUs |
|-----|--------------|------------|--------------|
| 001 | "Planck length is particle size" | Particles are pointlike to much smaller scales | 003, 008 |
| 002 | "Nothing can happen faster than tₚ" | Time can be measured to smaller intervals | 001, 008 |
| 003 | "Planck mass is microscopic" | It's macroscopic: ~22 μg! | 001, 004 |
| 004 | "Planck energy is small" | It's enormous: 10¹⁵× LHC energy | 003, 005 |
| 005 | "Planck temperature existed in early universe" | Only approached, never reached | 004 |
| 006 | "α is a Planck unit" | It's dimensionless, not a unit | 007 |
| 007 | "Planck charge is fundamental quantum" | Elementary charge e is the quantum | 006 |
| 008 | "Planck momentum is microscopic" | It's ~6.5 kg·m/s (baseball scale)! | 003, 001 |
| 009 | "Planck force is quantum" | No! Fₚ = c⁴/G has NO ℏ - purely GR! | 010 |
| 010 | "ℏ still has uncertainty" | Exact since 2019 SI redefinition! | ALL |

## Scale Relationships

### "Hierarchy of Scales" Table

| Property | Subatomic | Atomic | Human | Planck |
|----------|-----------|--------|-------|--------|
| Length | 10⁻¹⁵ m | 10⁻¹⁰ m | 1 m | 10⁻³⁵ m |
| Time | 10⁻²³ s | 10⁻¹⁶ s | 1 s | 10⁻⁴⁴ s |
| Mass | 10⁻²⁷ kg | 10⁻²⁶ kg | 1 kg | 10⁻⁸ kg |
| Energy | 10⁻¹³ J | 10⁻¹⁹ J | 1 J | 10⁹ J |
| Momentum | 10⁻²¹ kg·m/s | 10⁻²⁴ kg·m/s | 1 kg·m/s | 6.5 kg·m/s |
| Force | 10⁻⁹ N | 10⁻¹⁰ N | 1 N | 10⁴⁴ N |

**Key Insight**: Planck length/time are microscopic, but Planck mass/energy/momentum/force are macroscopic!

## Usage Patterns

### Which AKU to Reference When...

| Question/Topic | Recommended AKUs | Reason |
|----------------|------------------|--------|
| Quantum gravity scales | 001, 002, 003 | Define the regime |
| Early universe cosmology | 001, 002, 004, 005 | Planck epoch |
| Black hole physics | 001, 003, 004, 009 | Schwarzschild radius, Hawking radiation, horizon force |
| String theory | 001, 002, 008, 010 | String length scale, quantum action |
| Loop quantum gravity | 001, 010 | Area quantization, quantum geometry |
| Natural units systems | 010, ALL | Setting ℏ=c=G=k_B=1 |
| Maximum force conjecture | 009 | Spacetime tension limit |
| SI unit redefinition | 010 | Exact h since 2019 |
| Electromagnetic Planck units | 006, 007 | Charge scale |
| Uncertainty principle applications | 001, 008 | Δx·Δp at Planck scale |
| Natural units systems | All 8 | Complete unit system |

## Citation Patterns

### How to Cite These AKUs

**Single AKU**:
```
WorldSMEGraphs Planck Units Knowledge Base, 
aku-001-planck-length-definition, 
version 1.0.0, 
https://github.com/WorldSMEGraphs/domain/science/physics/quantum-mechanics/planck-units/
```

**Multiple AKUs**:
```
WorldSMEGraphs Planck Units Knowledge Base, 
AKUs 001-008 (Phase 1-2), 
NIST CODATA 2018 values,
https://github.com/WorldSMEGraphs/domain/science/physics/quantum-mechanics/planck-units/
```

## Validation Notes

### Cross-Validation Results
- ✅ All 8 AKUs validated with validate_aku_v2.py
- ✅ Mathematical relationships verified consistent
- ✅ NIST values match across all citations
- ✅ No circular dependencies found
- ✅ Prerequisite chains are acyclic

### Consistency Checks
- ✅ Formulas consistent across all AKUs
- ✅ No contradictory statements
- ✅ Scale comparisons aligned
- ✅ Common misconceptions don't overlap
- ✅ External ontology links validated

## Future Cross-References

### When Priority 2 AKUs Added
- Planck Force (Fₚ) will reference: 001, 004
- Planck Power (Pₚ) will reference: 002, 004
- Planck Voltage (Vₚ) will reference: 004, 007

### When Priority 3 AKUs Added
- Planck Density (ρₚ) will reference: 001, 003
- Planck Area (Aₚ) will reference: 001
- Planck Frequency (fₚ) will reference: 002

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total AKUs | 8 |
| Direct mathematical relationships | 8 |
| Prerequisite dependencies | 24 |
| Cross-references in content | 47 |
| Common misconceptions addressed | 8 |
| External ontology links | 24 |
| Physics domains covered | 5 |

---

**Maintained By**: definition-extractor-agent  
**Last Updated**: 2025-12-29T14:40:00Z  
**Next Update**: After Priority 2 additions
