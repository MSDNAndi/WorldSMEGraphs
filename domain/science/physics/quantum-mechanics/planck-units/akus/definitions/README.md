# Planck Units Definition AKUs

This directory contains 5 authoritative definition AKUs for Planck units, extracted from NIST CODATA 2018 and peer-reviewed physics literature.

## Created AKUs

### 1. **aku-001-planck-length-definition.json**
- **Value**: 1.616255(18) × 10⁻³⁵ m
- **Formula**: ℓₚ = √(ℏG/c³)
- **Significance**: Smallest meaningful length in physics; quantum gravity scale
- **Prerequisites**: Quantum mechanics, general relativity, fundamental constants

### 2. **aku-002-planck-time-definition.json**
- **Value**: 5.391247(60) × 10⁻⁴⁴ s
- **Formula**: tₚ = √(ℏG/c⁵) = ℓₚ/c
- **Significance**: Shortest time interval with physical meaning; light travel time across Planck length
- **Cosmological Context**: Planck epoch (0 < t < tₚ) in early universe

### 3. **aku-003-planck-mass-definition.json**
- **Value**: 2.176434(24) × 10⁻⁸ kg ≈ 21.76 μg
- **Formula**: mₚ = √(ℏc/G)
- **Significance**: Mass scale where quantum mechanics and gravity become equally important
- **Unique Property**: Macroscopic (unlike other Planck units); Compton wavelength = Schwarzschild radius

### 4. **aku-004-planck-energy-definition.json**
- **Value**: 1.956082(22) × 10⁹ J ≈ 1.220910(14) × 10¹⁹ GeV
- **Formula**: Eₚ = mₚc² = √(ℏc⁵/G)
- **Significance**: Energy scale where quantum gravity and all forces unify
- **Comparison**: 10¹⁵ times larger than LHC collision energy

### 5. **aku-005-planck-temperature-definition.json**
- **Value**: 1.416784(16) × 10³² K
- **Formula**: Tₚ = Eₚ/k_B = mₚc²/k_B = √(ℏc⁵/(Gk_B²))
- **Significance**: Highest temperature with physical meaning; early universe at Planck epoch
- **Comparison**: 10²¹ times hotter than a supernova

## Data Quality

- **Source**: NIST CODATA 2018 (authoritative reference)
- **Confidence**: 0.98 (highly reliable)
- **Status**: validated
- **Uncertainty**: All values have relative uncertainty ~1.1 × 10⁻⁵ (arising solely from G measurement)

## Format Compliance

All AKUs follow the standard format with:
- `@context`: base.jsonld + science.jsonld
- `@type`: EducationalResource + ScientificConcept
- Complete metadata with UTC timestamps
- Classification with domain_path: "science/physics/quantum-mechanics/planck-units"
- Comprehensive content sections (statement, explanation, glossary)
- SKOS annotations for ontology integration
- Provenance with NIST CODATA 2018 citation
- Pedagogical information (target audience, learning objectives, insights)
- Rendering hints for multi-format output

## Validation Status

All 5 AKUs validated successfully with `.project/agents/quality-assurance/tools/validate_aku_v2.py`:
- ✅ Structure compliant
- ✅ All required fields present
- ✅ Numerical values match NIST CODATA 2018
- ✅ Cross-references consistent
- ⚠️  Minor: "scientific_principles" field recommended but not required

## Relationships Between AKUs

1. **Planck Length (001)** ← foundational spatial scale
2. **Planck Time (002)** = Planck Length / c
3. **Planck Mass (003)** → Compton wavelength = Planck Length
4. **Planck Energy (004)** = Planck Mass × c²
5. **Planck Temperature (005)** = Planck Energy / k_B

## Target Audience

- Physics graduate students
- Physics researchers
- Advanced undergraduates
- Theoretical physicists

## Estimated Study Time

15-20 minutes per AKU (75-100 minutes total for all 5)

## External References

All AKUs link to external ontologies:
- **Wikidata**: Q499294 (Planck length), Q568726 (Planck time), Q830175 (Planck mass), Q1387955 (Planck energy), Q898892 (Planck temperature)
- **DBpedia**: Corresponding resources
- **QUDT**: Quantity kinds (Length, Time, Mass, Energy, Temperature)

## Creation Details

- **Created**: 2025-12-29T03:14:51.064Z
- **Agent**: definition-extractor-agent
- **Method**: NLP pattern recognition with expert validation
- **Research Source**: `/tmp/planck-research/planck_units_structured_data.json`

---

**Note**: These AKUs represent authoritative, peer-reviewed knowledge suitable for inclusion in physics knowledge bases, educational systems, and semantic web applications.
