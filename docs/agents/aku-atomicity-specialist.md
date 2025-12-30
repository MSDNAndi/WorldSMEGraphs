# AKU Atomicity Specialist Agent

**Created**: 2025-12-29  
**Version**: 1.0  
**Agent File**: `.github/agents/aku-atomicity-specialist.agent.md`  
**Lines**: 521  
**Category**: Knowledge Organization

## Overview

The AKU Atomicity Specialist is a specialized agent designed to analyze, manage, and correct the granularity of Atomic Knowledge Units (AKUs) in the WorldSMEGraphs system. It ensures that each AKU contains exactly one indivisible concept, performing surgical transformations when atomicity violations are detected.

## Problem Statement

Knowledge units in educational systems often suffer from granularity issues:

1. **Over-bundling**: Multiple concepts inappropriately combined in a single AKU
2. **Under-specification**: Fragments too small to be independently useful
3. **Pedagogical Misalignment**: Concept boundaries that don't match learning flow
4. **Domain Variation**: Different fields define "atomic" differently

These issues reduce learning effectiveness, limit reusability, and complicate assessment design.

## Solution

The AKU Atomicity Specialist provides:

### Analysis Capabilities
- Detects over-bundled AKUs (multiple concepts in one unit)
- Identifies under-specified fragments (incomplete concepts)
- Maps natural concept boundaries within knowledge units
- Assesses pedagogical coherence of current granularity
- Generates detailed atomicity reports with recommendations

### Transformation Operations
- **Split**: Decompose over-bundled AKUs into atomic units
- **Merge**: Combine under-specified fragments into coherent AKUs
- **Recombine**: Reorganize AKU boundaries for better learning flow
- **Rebalance**: Adjust granularity across related AKU sets

### Quality Assurance
- Validates atomicity of transformed AKUs
- Ensures relationships are preserved during transformations
- Verifies JSON schema compliance
- Confirms prerequisites remain valid
- Maintains metadata integrity

## Core Philosophy

An Atomic Knowledge Unit (AKU) is the smallest piece of knowledge that:

1. **Can stand alone** and be understood (given stated prerequisites)
2. **Teaches exactly one concept** - not zero, not multiple
3. **Cannot be meaningfully divided** without losing coherence
4. **Can be independently** learned, tested, and referenced

## Domain-Specific Atomicity Rules

### Mathematics
- ✅ **Atomic**: One theorem, one proof, one formula, one worked example
- ❌ **Non-Atomic**: Theorem + proof in same AKU (should be 2 separate)
- ✅ **Atomic**: Multiple equivalent formulas for same concept (keep together)

### Medicine
- ✅ **Atomic**: One disease, one symptom cluster, one diagnostic criterion
- ❌ **Non-Atomic**: Disease definition + symptoms + diagnosis + treatment (split into 4)
- ✅ **Atomic**: Multiple imaging findings for one pathology (keep together)

### Economics/Finance
- ✅ **Atomic**: One financial concept, one formula, one decision rule
- ❌ **Non-Atomic**: NPV definition + formula + example (split into 3)
- ✅ **Atomic**: Formula with notation guide (keep together for usability)

### Science (General)
- ✅ **Atomic**: One principle, one law, one experiment, one observation
- ❌ **Non-Atomic**: Multiple experiments for same principle (split per experiment)
- ✅ **Atomic**: Principle + mathematical formulation (keep if inseparable)

## Usage Examples

### Analyze for Violations
```bash
@aku-atomicity-specialist Analyze domain/economics/bwl/finance/valuation/npv/akus/ 
for over-bundled AKUs. Look for: (1) AKUs teaching multiple concepts, (2) Mixed 
definition + formula + example in single AKU, (3) Multi-step calculations in one unit.
Report violations with split recommendations.
```

### Split Over-bundled AKU
```bash
@aku-atomicity-specialist Split aku-npv-complete.json - it contains: NPV definition, 
formula, decision rule, advantages, limitations, and worked example. Target: 6 atomic 
AKUs (1=definition, 2=formula, 3=decision-rule, 4=advantages, 5=limitations, 
6=example). Preserve all semantic links to FIBO/Wikidata. Maintain prerequisite chain.
```

### Merge Under-specified Fragments
```bash
@aku-atomicity-specialist Merge these 4 under-specified fragments: 
[aku-discount-rate-symbol.json, aku-discount-rate-unit.json, 
aku-discount-rate-range.json, aku-discount-rate-notation.json] into single cohesive 
"Discount Rate Notation" AKU. These fragments are too small to be independently useful.
```

### Domain Audit
```bash
@aku-atomicity-specialist Audit entire NPV pilot 
(domain/economics/bwl/finance/valuation/npv/) for atomicity violations. Provide: 
(1) List of over-bundled AKUs with concept count, (2) Under-specified fragments, 
(3) Recommended splits/merges, (4) Priority ranking by learning impact.
```

### Recombine for Pedagogy
```bash
@aku-atomicity-specialist Recombine NPV learning path - current atomicity is 
technically correct but pedagogically suboptimal. Components scattered: formula (AKU-5), 
notation (AKU-12), worked example (AKU-18). Reorganize so learners encounter 
definition→formula→example as coherent sequence within 3 consecutive AKUs.
```

## Success Criteria

### Atomicity Validation
- ✅ Each AKU teaches exactly **one** concept
- ✅ AKU can be understood independently (given prerequisites)
- ✅ Cannot be meaningfully subdivided without losing coherence
- ✅ Concept boundaries align with domain conventions
- ✅ Appropriate granularity for target audience

### Transformation Quality
- ✅ All relationships preserved or correctly updated
- ✅ Semantic links (FIBO, Wikidata) maintained
- ✅ Prerequisite chains remain valid and acyclic
- ✅ No orphaned references or broken cross-links
- ✅ JSON schema validation passes

### Metadata Integrity
- ✅ UTC timestamps updated correctly
- ✅ Provenance documented (transformation history)
- ✅ Contributors list includes atomicity-specialist
- ✅ Version numbers incremented appropriately
- ✅ Status reflects transformation state

### Pedagogical Improvement
- ✅ Learning flow improved
- ✅ Reusability enhanced
- ✅ Testing/assessment more granular
- ✅ Cognitive load optimized

## Related Agents

### Primary Collaborators
- **verification**: Validates transformed AKUs meet quality standards
- **pedagogy**: Confirms granularity appropriate for learning sequences
- **ontology**: Ensures semantic links preserved correctly
- **quality**: Reviews transformation quality before finalization
- **knowledge-graph-agent**: Updates graph relationships after transformations

### Provides Input To
- **rendering-agent**: Benefits from atomic units for flexible rendering
- **assessment-creation**: Uses atomic units for precise testing
- **educational-path**: Leverages atomic units for learning path construction
- **terminology**: Relies on atomic definitions for glossaries

### Receives Input From
- **paper-miner**: May extract over-bundled concepts requiring splitting
- **textbook-parser**: Often produces non-atomic units needing refinement
- **coordinator**: Assigns atomicity audits and transformations
- **contrarian-agent**: Challenges atomicity decisions for improvement

## Performance Expectations

### Analysis Operations
- **Single AKU Analysis**: 5-10 minutes
- **Domain Audit (50 AKUs)**: 45-60 minutes
- **Atomicity Report Generation**: 15 minutes

### Transformation Operations
- **Simple Split** (2-3 concepts): 30-45 minutes
- **Complex Split** (5-6 concepts): 60-90 minutes
- **Simple Merge** (2-3 fragments): 20-30 minutes
- **Complex Recombination** (10+ AKUs): 2-3 hours

### Validation Operations
- **Post-Split Validation**: 15-20 minutes
- **Schema Validation**: 5 minutes per AKU
- **Relationship Integrity Check**: 10-15 minutes per domain

## Benefits to WorldSMEGraphs

### Learning Effectiveness
- Concepts taught at optimal granularity
- Reduced cognitive load for learners
- Clearer learning objectives per unit
- More effective assessment design

### System Quality
- Improved knowledge reusability
- More flexible rendering options
- Better cross-referencing granularity
- Cleaner prerequisite chains

### Maintenance
- Easier to update individual concepts
- Reduced risk of conflicting information
- Better provenance tracking
- Simpler validation processes

### Scalability
- Atomic units easier to compose
- More flexible learning path construction
- Better multi-lingual rendering
- Improved audience adaptation

## Version History

- **v1.0** (2025-12-29): Initial creation as specialized atomicity management agent
  - 521 lines of comprehensive specifications
  - Domain-specific atomicity rules for math, medicine, economics, science
  - Split, merge, recombine transformation operations
  - Detailed quality criteria and success metrics
  - Integration with verification, pedagogy, and ontology agents

## Completed Audits

### Mesenteric Ischemia Domain (2025-12-30)
- **Domain**: `medicine/surgery/vascular/pathology/mesenteric-ischemia`
- **Result**: ✅ 100% pass (29/29 AKUs atomic)
- **Key Validation**: All 6 surgical dilemma AKUs represent exactly ONE discrete clinical decision
- **Report**: `.project/audits/mesenteric-ischemia-atomicity-audit.md`

---

**Last Updated**: 2025-12-30  
**Maintained by**: Agent Recruiter  
**Status**: Active
