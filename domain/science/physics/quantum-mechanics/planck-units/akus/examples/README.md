# Planck Units Example AKUs

This directory contains worked example AKUs demonstrating practical applications of Planck units concepts and formulas.

## Contents

### Practical Problem-Solving Examples

1. **aku-e01-converting-particle-energy.json** - Unit conversion: GeV⁻² to m²
   - Type: Example
   - Focus: Converting particle physics cross-section from natural units to SI
   - Skills: Using ℏc ≈ 197 MeV·fm, dimensional analysis
   - Difficulty: Intermediate
   - Time: ~15 minutes

2. **aku-e02-black-hole-properties.json** - Complete black hole calculation
   - Type: Example
   - Focus: Calculate r_s, A, S_BH, T_H, τ_evap for primordial black hole
   - Skills: Schwarzschild geometry, Bekenstein-Hawking formulas, numerical calculation
   - Difficulty: Advanced
   - Time: ~45 minutes

3. **aku-e03-deriving-planck-energy.json** - Dimensional analysis derivation
   - Type: Example
   - Focus: Derive Eₚ = √(ℏc⁵/G) from first principles
   - Skills: Systematic dimensional analysis, solving linear systems
   - Difficulty: Intermediate
   - Time: ~20 minutes

## Pedagogical Value

These examples serve multiple learning objectives:

### Skills Development
- **Unit Conversions**: Natural units ↔ SI (e01)
- **Dimensional Analysis**: Systematic derivation method (e03)
- **Numerical Calculation**: Multi-step physics problems (e02)
- **Formula Application**: Using Planck-scale formulas (all)

### Concept Reinforcement
- Natural units make theory easier, SI for experiments (e01)
- Black hole thermodynamics unifies QM, GR, thermodynamics (e02)
- Dimensional analysis alone determines Planck scales (e03)

### Problem-Solving Strategies
- Step-by-step systematic approach
- Verification through dimensional analysis
- Multiple solution methods shown
- Physical interpretation emphasized

## Integration with Other AKUs

### Prerequisites
Students should complete these before working examples:
- **Formula AKUs** (f01-f05): Provides theoretical foundation
- **Definition AKUs** (001-012): Defines quantities used
- Basic QM and GR background

### Learning Path
1. Study definitions (aku-001 through aku-012)
2. Learn methods (aku-f01 dimensional analysis, aku-f02 natural units)
3. Practice with examples (this directory)
4. Apply to research problems

## Target Audience

- Physics graduate students
- Advanced undergraduates with QM and GR
- Researchers needing practical skills

## Validation

All AKUs validated:
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/science/physics/quantum-mechanics/planck-units/akus/examples/
```

Status: ✅ All 3 AKUs valid (validated 2025-12-29)

## Future Additions

Potential examples to add:
- Cosmic string energy density calculation
- Planck epoch early universe conditions
- String theory characteristic scales
- Quantum foam spacetime fluctuations
- Gravitational wave frequency conversions
