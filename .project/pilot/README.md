# Pilot Projects

This directory contains pilot implementations to validate the WorldSMEGraphs approach before scaling.

## Current Pilots

### 1. NPV Finance Pilot (`npv-finance/`)

**Status:** In Progress  
**Start Date:** 2025-12-27  
**Objective:** Demonstrate complete knowledge representation for Net Present Value (NPV) concept

**Scope:**
- 50 Atomic Knowledge Units (AKUs)
- Complete theoretical foundations
- Mathematical formulations with LaTeX + executable code
- Worked examples (10+)
- Cross-references to related concepts
- Multi-audience renderings (academic, student, professional)

**Success Criteria:**
- All 50 AKUs validated by domain expert persona
- Error rate <2%
- Rendering time <100ms per AKU
- User validation with 5+ test subjects
- Quality score >0.95

**Structure:**
```
npv-finance/
├── plan.md                    # Detailed project plan
├── akus/                      # 50 Atomic Knowledge Units
│   ├── definitions/
│   ├── formulas/
│   ├── examples/
│   └── applications/
├── personas/                  # Domain expert specifications
│   └── finance-valuation-expert-v1.yaml
├── metrics/                   # Tracking data
│   ├── extraction_success.csv
│   ├── validation_errors.csv
│   └── performance.csv
├── renderings/               # Test renderings
│   ├── academic.md
│   ├── student.md
│   └── professional.md
└── README.md                 # Pilot-specific documentation
```

## Pilot Guidelines

### Creating a New Pilot

1. **Propose:** Submit pilot proposal in `.project/pilot/proposals/`
2. **Approve:** Coordinator reviews for alignment with goals
3. **Create Directory:** `mkdir .project/pilot/[pilot-name]`
4. **Document:** Create plan.md with objectives, scope, success criteria
5. **Execute:** Implement following structure guidelines
6. **Validate:** Run validation tools, collect metrics
7. **Report:** Document findings in final-report.md

### Directory Structure Rules

- **Hierarchical:** No flat 100-file directories
- **Discoverable:** Clear README.md at each level
- **Balanced:** Aim for 5-20 items per directory
- **Logical:** Group by type (definitions, formulas, examples)

### Integration with Main System

Successful pilots graduate to main knowledge graph:
```
.project/pilot/npv-finance/ → domain/economics/bwl/finance/valuation/npv/
```

## Pilot Pipeline

**Stage 1: Planning** → Define scope, success criteria  
**Stage 2: Implementation** → Create AKUs, personas, tools  
**Stage 3: Validation** → Domain expert review, user testing  
**Stage 4: Metrics** → Track quality, performance, usability  
**Stage 5: Graduation** → Move to main knowledge graph if successful  
**Stage 6: Retrospective** → Document lessons learned

## Current Status

- **npv-finance:** Planning/Implementation (Day 1)
- **[Future Pilot 2]:** TBD
- **[Future Pilot 3]:** TBD
