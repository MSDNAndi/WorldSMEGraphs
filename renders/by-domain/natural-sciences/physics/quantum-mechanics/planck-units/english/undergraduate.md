# Planck Units: Natural Units from Fundamental Constants

## Abstract

Planck units constitute a natural system of units derived solely from fundamental physical constants: the reduced Planck constant (ℏ), gravitational constant (G), speed of light (c), Boltzmann constant (k_B), and elementary charge (e). This document provides a rigorous introduction to Planck units, their mathematical derivation, physical significance, and applications in modern theoretical physics, suitable for undergraduate physics students.

## 1. Introduction: Why Natural Units?

In standard SI units, the choice of meter, kilogram, and second is anthropocentric—based on human-scale phenomena. In contrast, natural unit systems emerge from the fundamental constants that govern physical law.

**Advantages of Natural Units**:
1. Simplification of equations (many factors of ℏ, c, G drop out)
2. Dimensionless ratios reveal physical significance
3. Invariant under changes in human measurement conventions
4. Highlight regimes where different physics dominates

Planck units specifically represent the scales where quantum mechanics, special relativity, and general relativity all become important simultaneously—the quantum gravity regime.

## 2. Fundamental Constants (CODATA 2018 Values)

| Constant | Symbol | Value | Uncertainty | Status |
|----------|--------|-------|-------------|--------|
| Speed of light | c | 299,792,458 m/s | 0 | Exact (by definition) |
| Gravitational constant | G | 6.67430(15)×10⁻¹¹ m³/(kg·s²) | 2.2×10⁻⁵ | Measured |
| Reduced Planck constant | ℏ | 1.054571817×10⁻³⁴ J·s | 0 | Exact (by definition) |
| Boltzmann constant | k_B | 1.380649×10⁻²³ J/K | 0 | Exact (by definition) |
| Elementary charge | e | 1.602176634×10⁻¹⁹ C | 0 | Exact (by definition) |

**Note**: All uncertainty in Planck units derives from uncertainty in G, which has relative uncertainty ~10⁻⁵.

## 3. Derivation of Base Planck Units

### 3.1 Dimensional Analysis Approach

Planck units can be derived through dimensional analysis. Consider three fundamental constants:
- [ℏ] = ML²T⁻¹ (action)
- [G] = M⁻¹L³T⁻² (gravitational constant)
- [c] = LT⁻¹ (velocity)

To construct a unit of length from these, we seek:
ℓ_P = ℏᵃ Gᵇ cᶜ

Where [ℓ_P] = L. This gives:
L = (ML²T⁻¹)ᵃ (M⁻¹L³T⁻²)ᵇ (LT⁻¹)ᶜ
L = Mᵃ⁻ᵇ L²ᵃ⁺³ᵇ⁺ᶜ T⁻ᵃ⁻²ᵇ⁻ᶜ

Matching exponents:
- Mass: a - b = 0 → a = b
- Time: -a - 2b - c = 0 → c = -a - 2b = -3a
- Length: 2a + 3b + c = 1 → 2a + 3a - 3a = 1 → a = 1/2

Therefore: a = b = 1/2, c = -3/2

**Planck Length**:
ℓ_P = √(ℏG/c³) = 1.616255(18) × 10⁻³⁵ m

Similarly, for time: t_P = ℓ_P/c = √(ℏG/c⁵) = 5.391247(60) × 10⁻⁴⁴ s

For mass: m_P = √(ℏc/G) = 2.176434(24) × 10⁻⁸ kg

### 3.2 Physical Motivation: Compton Wavelength = Schwarzschild Radius

A more physically motivated derivation equates two fundamental length scales:

**Compton wavelength** (quantum mechanics):
λ_C = ℏ/(mc)

This is the length scale where relativistic quantum effects become important for a particle of mass m.

**Schwarzschild radius** (general relativity):
r_S = 2Gm/c²

This is the gravitational radius—if an object's radius is smaller than r_S, it forms a black hole.

Setting λ_C = r_S:
ℏ/(mc) = 2Gm/c²

Solving for m:
m² = ℏc/(2G)

m_P = √(ℏc/G) ≈ 2.18 × 10⁻⁸ kg (dropping numerical factor)

The Planck length is then:
ℓ_P = ℏ/(m_P c) = √(ℏG/c³)

**Physical Interpretation**: At the Planck mass, quantum mechanical spread (Compton wavelength) equals gravitational size (Schwarzschild radius). This is where quantum mechanics and general relativity must be treated on equal footing.

## 4. Complete System of Planck Units

### 4.1 Base Units

| Unit | Symbol | Formula | Value | Dimensions |
|------|--------|---------|-------|-----------|
| Length | ℓ_P | √(ℏG/c³) | 1.616×10⁻³⁵ m | L |
| Time | t_P | √(ℏG/c⁵) | 5.391×10⁻⁴⁴ s | T |
| Mass | m_P | √(ℏc/G) | 2.176×10⁻⁸ kg | M |
| Temperature | T_P | √(ℏc⁵/Gk_B²) | 1.417×10³² K | Θ |
| Charge | q_P | √(4πε₀ℏc) | 1.876×10⁻¹⁸ C | Q |

### 4.2 Derived Units

| Unit | Formula | Value |
|------|---------|-------|
| Energy | E_P = m_P c² | 1.956×10⁹ J ≈ 1.22×10¹⁹ GeV |
| Force | F_P = E_P/ℓ_P | 1.21×10⁴⁴ N |
| Power | P_P = E_P/t_P | 3.63×10⁵² W |
| Density | ρ_P = m_P/ℓ_P³ | 5.16×10⁹⁶ kg/m³ |
| Momentum | p_P = m_P c | 6.525 kg·m/s |

### 4.3 Dimensionless Constants

Several fundamental coupling constants become order unity in Planck units:

**Gravitational fine structure constant**:
α_G = Gm_P²/(ℏc) ≈ 1

This shows that at the Planck mass, gravitational coupling is "strong" (order unity) rather than the usual weak gravitational force.

**Fine structure constant** (electromagnetic):
α ≈ 1/137

This remains dimensionless and doesn't depend on unit choice. It's approximately 137 times weaker than the Planck-scale gravitational interaction.

## 5. Physical Significance and Applications

### 5.1 Planck Scale as Quantum Gravity Regime

The Planck scale defines where quantum field theory and general relativity cannot be treated independently.

**Energy-Time Uncertainty**:
From the Heisenberg uncertainty principle:
ΔE Δt ≥ ℏ/2

At Planck time intervals (Δt ~ t_P), energy fluctuations are:
ΔE ~ ℏ/t_P = ℏc⁵/(ℏG) = c⁵/G √(ℏG/c⁵) = c⁴√(ℏ/G) ≈ E_P

These energy fluctuations are sufficient to curve spacetime significantly, requiring quantum gravity.

**Gravitational Self-Energy**:
The gravitational self-energy of a Planck mass within a Planck length is:
E_grav ~ Gm_P²/ℓ_P = G(ℏc/G)/(√(ℏG/c³)) = √(ℏc⁵/G) = E_P

Thus the gravitational binding energy equals the rest mass energy—strong gravity regime.

### 5.2 Limits on Measurement

**Wigner 1957 / Salecker-Wigner 1958 Argument**:

To measure a distance δx with precision requires a "clock" of mass m_clock such that:
δx ≥ ℏ/(m_clock c)   (Compton wavelength)

But this clock's gravitational field perturbs spacetime over scale:
r_g ~ Gm_clock/c²   (Schwarzschild radius)

For the measurement to not be dominated by gravitational perturbation:
δx > Gm_clock/c²

Combining these:
δx² ≥ (ℏ/(m_clock c))(Gm_clock/c²) = ℏG/c³ = ℓ_P²

**Conclusion**: The Planck length represents a fundamental limit on spatial measurement precision, regardless of technology.

### 5.3 Cosmological Applications

**Planck Epoch** (0 < t < t_P):
The earliest period in cosmic history where quantum gravitational effects dominated. Current physics cannot describe this epoch.

**Initial Conditions**:
- Temperature: T ~ T_P = 10³² K
- Density: ρ ~ ρ_P = 10⁹⁶ kg/m³
- Scale factor: a ~ ℓ_P = 10⁻³⁵ m

**Inflationary Cosmology**:
Many inflation models involve scalar fields with potentials V(φ) characterized by energy scales near (but below) the Planck energy. The Planck scale provides an upper bound on inflation energy scales.

**Observable Consequences**:
The Planck satellite (ESA) measured CMB anisotropies, providing constraints on physics near (but not at) Planck scales through primordial gravitational waves and scalar perturbations.

### 5.4 Black Hole Physics

**Hawking Temperature**:
A black hole of mass M has temperature:
T_H = ℏc³/(8πGMk_B) = (m_P/M)(T_P/8π)

For a Planck-mass black hole (M = m_P):
T_H ~ T_P

Such black holes evaporate almost instantaneously via Hawking radiation.

**Bekenstein-Hawking Entropy**:
S_BH = (k_B c³/4ℏG) A = (k_B/4) (A/ℓ_P²)

The entropy is proportional to area measured in Planck units, suggesting spacetime has Planck-scale degrees of freedom.

**Information Paradox**:
Understanding information loss/preservation in black holes requires quantum gravity—physics at the Planck scale near the horizon.

## 6. Quantum Gravity Theories and Planck Scale

### 6.1 String Theory

String theory proposes that fundamental objects are not point particles but one-dimensional strings with length:
l_s ~ ℓ_P

Different vibration modes of these Planck-length strings correspond to different particles. The theory requires extra spatial dimensions compactified at scales ~10-100 ℓ_P.

**Key Prediction**: At energies E ~ E_P, string excitations become important, resolving ultraviolet divergences present in quantum field theory.

### 6.2 Loop Quantum Gravity

Loop quantum gravity quantizes spacetime geometry itself. Area and volume operators have discrete spectra with minimum values:
A_min ~ ℓ_P²
V_min ~ ℓ_P³

This leads to a discrete "quantum geometry" where spacetime has granular structure at the Planck scale.

**Spin Networks**: At Planck scales, space is described by spin networks—graphs with edges carrying SU(2) representations, with edge lengths ~ ℓ_P.

### 6.3 Causal Set Theory

Proposes spacetime is fundamentally discrete, composed of Planck-scale events with causal relations. The discreteness scale is set by:
n ~ 1/ℓ_P⁴   (events per unit 4-volume)

### 6.4 Experimental Prospects

Direct observation of Planck-scale physics is beyond current technology:

**Particle Accelerators**: 
- LHC: ~10¹³ eV
- Planck scale: ~10¹⁹ GeV = 10²⁸ eV
- Gap: 15 orders of magnitude

**Indirect Tests**:
- Planck-scale Lorentz violation (extremely constrained)
- Quantum gravity phenomenology in cosmic rays
- Gravitational wave observations (LIGO/Virgo)
- CMB physics (Planck satellite)

## 7. Mathematical Framework: Natural Units

In theoretical calculations, physicists often use Planck units as the natural scale, setting:
ℏ = G = c = k_B = 1

**Benefits**:
1. Equations become simpler
2. Physical scales are measured relative to Planck scale
3. Dimensionless ratios reveal physics

**Example - Einstein Field Equations**:

Standard form:
R_μν - (1/2)g_μν R = (8πG/c⁴) T_μν

In Planck units (G = c = 1):
R_μν - (1/2)g_μν R = 8π T_μν

**Conversion Back to SI**:

Any dimensionful quantity Q can be expressed as:
Q = (numerical factor) × ℏᵃ Gᵇ cᶜ k_B^d

where exponents are determined by dimensional analysis.

## 8. Summary and Conclusions

**Key Points**:

1. Planck units emerge naturally from fundamental constants and define the quantum gravity scale
2. At Planck scales, quantum mechanics and general relativity are equally important
3. The Planck length represents a fundamental limit on spatial measurement
4. Planck units are essential for cosmology (early universe), black hole physics, and quantum gravity theories
5. Current technology cannot probe Planck scales directly, but they provide crucial theoretical guidance

**Scaling Context**:

| Scale | Length | Example |
|-------|--------|---------|
| Planck | 10⁻³⁵ m | Quantum gravity regime |
| Nuclear | 10⁻¹⁵ m | Proton radius |
| Atomic | 10⁻¹⁰ m | Hydrogen atom |
| Macroscopic | 10⁰ m | Human scale |
| Astronomical | 10²⁶ m | Observable universe |

The Planck scale is 20 orders of magnitude below atomic scales—far beyond direct experimental access.

**Open Questions**:

1. Is spacetime discrete or continuous at Planck scales?
2. What is the correct theory of quantum gravity?
3. What happened during the Planck epoch?
4. How is information preserved in black hole evaporation?
5. Are there additional spatial dimensions at Planck scales?

## 9. Further Reading

**Textbooks**:
- Carroll, S. (2019). *Spacetime and Geometry*. Cambridge University Press.
- Weinberg, S. (2008). *Cosmology*. Oxford University Press.
- Peskin, M. & Schroeder, D. (1995). *An Introduction to Quantum Field Theory*. Westview Press.

**Seminal Papers**:
- Planck, M. (1899). "Über irreversible Strahlungsvorgänge"
- Garay, L. J. (1995). "Quantum gravity and minimum length". Int. J. Mod. Phys. A 10, 145.
- Amelino-Camelia, G. (2013). "Quantum-Spacetime Phenomenology". Living Rev. Relativ. 16, 5.

**Review Articles**:
- Wüthrich, C. (2019). "Are Black Holes about Information?" Philosophy of Physics (Oxford Handbooks)
- Rovelli, C. & Vidotto, F. (2015). *Covariant Loop Quantum Gravity*. Cambridge.

## Appendices

### A. Derivation of All Base Planck Units

Using dimensional analysis with [ℏ] = ML²T⁻¹, [G] = M⁻¹L³T⁻², [c] = LT⁻¹, [k_B] = ML²T⁻²Θ⁻¹:

**Length**: ℓ_P = ℏ^(1/2) G^(1/2) c^(-3/2)

**Time**: t_P = ℏ^(1/2) G^(1/2) c^(-5/2)

**Mass**: m_P = ℏ^(1/2) G^(-1/2) c^(1/2)

**Temperature**: T_P = ℏ^(1/2) G^(-1/2) c^(5/2) k_B^(-1)

**Charge**: q_P = (4πε₀ℏc)^(1/2) = e/√α ≈ 11.7e

### B. Problem Sets

**Problem 1**: Show that the Schwarzschild radius of a Planck mass equals √2 times the Planck length.

**Problem 2**: Calculate the lifetime of a Planck-mass black hole using the Hawking evaporation formula.

**Problem 3**: Estimate the number of Planck times since the Big Bang.

**Problem 4**: Derive the Planck energy from the Planck mass.

---

**Level**: Undergraduate (Years 2-4)  
**Prerequisites**: Classical mechanics, special relativity, quantum mechanics, thermodynamics  
**Recommended Background**: Some exposure to general relativity and quantum field theory helpful  
**Reading Time**: 20-25 minutes  
**Problem Set**: 4 problems (answers in AKU technical files)

---

*This document provides an undergraduate-level introduction to Planck units. For graduate-level treatment, consult the technical AKU files which include full derivations, advanced applications, and connections to modern research.*
