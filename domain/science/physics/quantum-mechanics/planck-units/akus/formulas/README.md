# Planck Units Formula AKUs

This directory contains formula-based Atomic Knowledge Units (AKUs) that provide practical skills and theoretical frameworks for understanding Planck units.

## Contents

### Priority 1: Critical Gap Fillers

These AKUs address the most important knowledge gaps identified in the Planck units domain:

1. **aku-f01-dimensional-analysis.json** - Systematic method for deriving any Planck unit
   - Type: Formula/Method
   - Focus: Step-by-step dimensional analysis technique
   - Includes: Complete worked examples for ℓₚ, tₚ, mₚ
   - Pedagogical value: Teaches essential physics skill applicable across all domains

2. **aku-f02-natural-units-system.json** - Natural units (ℏ = c = G = k_B = 1)
   - Type: Formula/System
   - Focus: Working in Planck units, conversion formulas
   - Includes: Practical examples, equation simplifications
   - Pedagogical value: Essential for reading modern physics papers

3. **aku-f03-bekenstein-hawking-entropy.json** - Black hole entropy formula
   - Type: Formula
   - Focus: S_BH = k_B·A/(4ℓₚ²) and holographic principle
   - Includes: Hawking temperature, radiation, information paradox
   - Pedagogical value: Shows deep QM + GR + thermodynamics unification

4. **aku-f04-natural-units-philosophy.json** - Why Planck units matter
   - Type: Theory/Conceptual
   - Focus: Philosophical motivation, dimensionless vs dimensional constants
   - Includes: Fine structure constant, Planck's prescience (1899)
   - Pedagogical value: Provides "why we care" motivation

5. **aku-f05-quantum-gravity-regime.json** - When quantum gravity matters
   - Type: Theory
   - Focus: Defining quantum gravity regime (r_s ~ λ_C)
   - Includes: Examples where QG matters vs doesn't matter
   - Pedagogical value: Shows scope and limitations of theories

## Knowledge Integration

These formula AKUs complement the 12 definition AKUs by providing:

- **Practical Skills**: How to derive Planck units (f01), work in natural units (f02)
- **Theoretical Framework**: When QG applies (f05), why these scales matter (f04)
- **Deep Connections**: Black hole thermodynamics linking QM, GR, thermodynamics (f03)

## Target Audience

- Physics graduate students
- Theoretical physics researchers
- Advanced undergraduates with QM and GR background

## Validation

All AKUs in this directory have been validated using:
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/science/physics/quantum-mechanics/planck-units/akus/formulas/
```

Status: ✅ All 5 AKUs valid (validated 2025-12-29)

## Cross-References

### Prerequisites
- All 12 definition AKUs (especially aku-001 through aku-005)
- Basic quantum mechanics
- Basic general relativity
- Dimensional analysis fundamentals

### Related Topics
- Quantum gravity theories (string theory, loop quantum gravity)
- Black hole physics
- Early universe cosmology
- High-energy physics

## Next Steps

Potential future additions:
- Examples AKU showing complete problem-solving workflows
- Applications AKU for cosmology and particle physics
- Connections AKU linking to other physics domains
