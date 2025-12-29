# AKU Atomicity Specialist

**Agent**: `.github/agents/aku-atomicity-specialist.agent.md`  
**Created**: 2025-12-29  
**Status**: Active  
**Category**: Knowledge Organization

## Overview

The AKU Atomicity Specialist is a specialized agent that ensures Atomic Knowledge Units (AKUs) maintain true atomicity - each containing exactly one indivisible concept. It detects granularity violations and performs surgical transformations to optimize knowledge decomposition.

## Directory Structure

```
.project/agents/atomicity-specialist/
├── README.md                    # This file
├── tools/
│   ├── README.md               # Tool documentation
│   └── analyze_atomicity.py    # Atomicity analysis tool
└── examples/
    └── splitting-over-bundled-aku.md  # Split example
```

## Quick Start

### Analyze a Single AKU
```bash
python tools/analyze_atomicity.py path/to/aku.json --verbose
```

### Analyze a Domain
```bash
python tools/analyze_atomicity.py --domain economics/bwl/finance/valuation/npv
```

### Invoke the Agent
```bash
@aku-atomicity-specialist Analyze domain/economics/finance/ for atomicity 
violations. Provide split/merge recommendations prioritized by learning impact.
```

## Core Concepts

### What is Atomic?

An Atomic Knowledge Unit (AKU) is the smallest piece of knowledge that:
1. **Can stand alone** - Understood independently (given prerequisites)
2. **Teaches one concept** - Not zero, not multiple
3. **Cannot be divided** - Further subdivision loses coherence
4. **Can be independently** - Learned, tested, referenced

### Atomicity Violations

**Over-Bundled** (multiple concepts):
- NPV definition + formula + example in one AKU
- Disease definition + symptoms + diagnosis + treatment
- Theorem + proof + corollaries

**Under-Specified** (incomplete concepts):
- Just a symbol notation
- Only abbreviation definition
- Fragment without context

## Domain-Specific Rules

### Mathematics
- ✅ Atomic: One theorem, one proof, one formula
- ❌ Non-Atomic: Theorem + proof together

### Medicine
- ✅ Atomic: One disease, one symptom cluster
- ❌ Non-Atomic: Disease + symptoms + diagnosis + treatment

### Economics/Finance
- ✅ Atomic: One concept, one formula, one decision rule
- ❌ Non-Atomic: NPV definition + formula + example

### Science
- ✅ Atomic: One principle, one law, one experiment
- ❌ Non-Atomic: Multiple experiments for same principle

## Available Resources

### Agent Specification
- **File**: `.github/agents/aku-atomicity-specialist.agent.md`
- **Lines**: 521 (comprehensive)
- **Format**: GitHub Copilot custom agent format
- **Content**: Responsibilities, expertise, workflows, examples

### Documentation
- **File**: `docs/agents/aku-atomicity-specialist.md`
- **Content**: Overview, usage examples, success criteria, benefits

### Tools
- **Analyzer**: `tools/analyze_atomicity.py`
- **Documentation**: `tools/README.md`
- **Features**: Detection, scoring, recommendations

### Examples
- **Split Example**: `examples/splitting-over-bundled-aku.md`
- **Demonstrates**: 8-concept AKU → 8 atomic AKUs

## Transformation Operations

### Split (Over-bundled → Atomic)
```bash
@aku-atomicity-specialist Split aku-npv-complete.json containing 
definition + formula + example into 3 atomic AKUs. Preserve semantic 
links and update prerequisites.
```

### Merge (Fragments → Atomic)
```bash
@aku-atomicity-specialist Merge symbol/notation fragments in discount-rate/ 
into single cohesive "Discount Rate Notation" AKU.
```

### Recombine (Reorganize boundaries)
```bash
@aku-atomicity-specialist Recombine NPV learning path - reorganize AKU 
boundaries to improve pedagogical flow while maintaining atomicity.
```

## Success Metrics

### Atomicity Validation
- Each AKU teaches exactly **one** concept
- Can be understood independently
- Cannot be meaningfully subdivided
- Appropriate granularity for audience

### Quality Assurance
- All relationships preserved
- Semantic links maintained
- Prerequisites valid
- Schema validation passes
- Metadata complete

### Pedagogical Impact
- Learning flow improved
- Cognitive load optimized
- Assessment more granular
- Reusability enhanced

## Integration with Other Agents

### Primary Collaborators
- **verification**: Validates transformed AKUs
- **pedagogy**: Confirms optimal granularity
- **ontology**: Maintains semantic links
- **quality**: Reviews transformation quality
- **knowledge-graph-agent**: Updates relationships

### Workflow Integration
1. **Content Creation** → Extract AKUs from sources
2. **Atomicity Analysis** → Detect violations
3. **Transformation** → Split/merge as needed
4. **Validation** → Verify quality
5. **Integration** → Update knowledge graph

## Performance Expectations

### Analysis
- Single AKU: 5-10 minutes
- Domain (50 AKUs): 45-60 minutes
- Report generation: 15 minutes

### Transformation
- Simple split (2-3 concepts): 30-45 minutes
- Complex split (5-6 concepts): 60-90 minutes
- Merge (2-3 fragments): 20-30 minutes
- Recombination (10+ AKUs): 2-3 hours

## Quality Standards

All transformations must:
- Preserve all knowledge (no information loss)
- Maintain relationship integrity
- Pass schema validation
- Document provenance
- Archive originals

## Usage Patterns

### Domain Audit
```bash
# 1. Run atomicity analysis
python tools/analyze_atomicity.py --domain economics/finance/npv

# 2. Review violations
# 3. Prioritize by impact
# 4. Transform high-priority AKUs
# 5. Validate results
# 6. Update documentation
```

### Continuous Quality
```bash
# Add to CI/CD pipeline
python tools/analyze_atomicity.py --directory domain/ > atomicity-report.txt
# Fail build if average score < 0.80
```

### Learning Path Optimization
```bash
# 1. Analyze learning path AKUs
# 2. Identify pedagogical misalignments
# 3. Recombine boundaries
# 4. Validate learning flow
# 5. Test with learners
```

## Future Enhancements

### Planned Features
1. Machine learning models for detection
2. Automatic split plan generation
3. Relationship visualization
4. Batch processing capabilities
5. CI/CD integration
6. Learning analytics integration
7. Multi-lingual atomicity rules
8. Domain-specific heuristics

## Contributing

To improve the atomicity specialist:

1. **Add Domain Rules**: Update detection heuristics
2. **Improve Scoring**: Refine atomicity calculations
3. **Create Examples**: Document transformation patterns
4. **Test Cases**: Validate on diverse domains
5. **Tool Enhancements**: Add features to analyzer

## References

- **Cognitive Load Theory**: Optimal chunk size for learning
- **Learning Science**: How concepts should be decomposed
- **Instructional Design**: Granularity for effectiveness
- **Bloom's Taxonomy**: Complexity and learning objectives
- **Schema Theory**: Building knowledge incrementally

## Support

- **Agent Issues**: Consult `@quality` or `@coordinator`
- **Tool Bugs**: Create issue in `.project/issues.md`
- **Enhancement Ideas**: Add to `.project/improvements.md`
- **Questions**: Ask `@recruiter` for agent ecosystem guidance

---

**Maintained by**: Agent Recruiter  
**Last Updated**: 2025-12-29  
**Version**: 1.0  
**Status**: Production Ready
