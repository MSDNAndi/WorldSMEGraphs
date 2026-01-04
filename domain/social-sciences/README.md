# Social Sciences

> **Domain Path**: `social-sciences/`  
> **UNESCO Code**: 03 (Social Sciences, Journalism, and Information)  
> **Library of Congress**: H (Social Sciences)  
> **Version**: 1.0.0  
> **Created**: 2026-01-04

## Overview

The Social Sciences study human society, behavior, institutions, and relationships. These sciences use both quantitative and qualitative methods to understand social phenomena, cultural practices, economic systems, and political structures.

## What are Social Sciences?

Social sciences examine:
- **Human behavior**: Individual and group psychology
- **Social structures**: Organizations, institutions, hierarchies
- **Economic systems**: Production, distribution, consumption
- **Political systems**: Government, policy, power relations
- **Cultural phenomena**: Beliefs, practices, communication

**Key Methodology**: Empirical observation + statistical analysis + qualitative research + theory building

## Subdomain Structure

### Economics

**Path**: `social-sciences/economics/`  
**Coverage**: All branches of economics

**Content (1 AKU migrated 2026-01-04)**:
- **Business Administration (BWL)** - German business administration
  - Finance/Valuation (1 AKU on Net Present Value)

**Note**: Most economics AKUs (11) are missing `classification.domain_path` and need fixing.

**Planned Coverage**:
- **Microeconomics**: Individual agents and markets
  - Supply and demand, consumer theory, producer theory
- **Macroeconomics**: Economy-wide phenomena
  - GDP, inflation, unemployment, monetary policy
- **Financial Economics**: Resource allocation over time
  - Asset pricing, corporate finance, investments, NPV, IRR, WACC
- **Econometrics**: Statistical methods in economics
- **Behavioral Economics**: Psychology and economics

### Psychology

**Path**: `social-sciences/psychology/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Cognitive Psychology
- Developmental Psychology
- Social Psychology
- Clinical Psychology

### Sociology

**Path**: `social-sciences/sociology/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Social Structure
- Social Stratification
- Institutions
- Social Movements

### Political Science

**Path**: `social-sciences/political-science/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Political Theory
- Comparative Politics
- International Relations
- Public Policy

### Anthropology

**Path**: `social-sciences/anthropology/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Cultural Anthropology
- Physical Anthropology
- Archaeology
- Linguistics

## Cross-Domain Applications

Social sciences draw from and contribute to other domains:

### From Formal Sciences
- **Mathematics**: Statistical methods, game theory, optimization
- **Computer Science**: Data science, computational social science, network analysis

### From Natural Sciences
- **Biology**: Evolutionary psychology, neuroscience
- **Chemistry**: Behavioral effects of substances

### To Health Sciences
- **Public Health**: Social determinants of health
- **Clinical Psychology**: Mental health treatment

### To Engineering
- **Systems Engineering**: Human factors, user experience
- **Urban Planning**: Social impact assessment

## Native Domain Principle

Social science concepts belong here even when applied elsewhere:

| Concept | Native Domain | Application Domains |
|---------|---------------|---------------------|
| Game Theory | Economics | CS (algorithmic game theory), Biology (evolution) |
| Social Networks | Sociology | CS (network analysis), Engineering (communication) |
| Behavioral Economics | Economics | Marketing, Policy Design |
| Supply & Demand | Economics | Engineering (resource allocation) |

## Migration Status

**Created**: 2026-01-04  
**Status**: Initial structure with partial economics migration

### Migrated Content
- ✅ **Economics** (1/12 AKUs) migrated from `economics/`
  - Only 1 AKU had proper classification.domain_path
  - 11 AKUs skipped (missing domain_path - need fixing)

### Issues to Resolve
- 🔴 **Economics AKUs missing classification**: 11 AKUs need domain_path added
  - Location: `economics/bwl/` subdirectories
  - Action needed: Update AKUs to include classification.domain_path

### Pending Migrations
- ⏳ Fix remaining economics AKUs (11)
- ⏳ Create psychology content
- ⏳ Create sociology content
- ⏳ Create political science content
- ⏳ Create anthropology content

## Content Statistics

**Current AKUs**: 1 (economics/finance)  
**Pending Fix**: 11 economics AKUs  
**Pending Creation**: Psychology, Sociology, Political Science, Anthropology  
**Target**: Comprehensive coverage of all social sciences

## Directory Structure

```
social-sciences/
├── economics/                     ✅ 1 AKU migrated, 11 pending fix
│   ├── microeconomics/            ⏳ Future
│   ├── macroeconomics/            ⏳ Future
│   ├── financial-economics/       ⏳ Future
│   ├── econometrics/              ⏳ Future
│   ├── behavioral-economics/      ⏳ Future
│   └── bwl/                       ✅ Partial (1 AKU)
│       └── finance/
│           └── valuation/
│               └── npv/
│
├── psychology/                    ⏳ Pending
│   ├── cognitive-psychology/
│   ├── developmental-psychology/
│   ├── social-psychology/
│   └── clinical-psychology/
│
├── sociology/                     ⏳ Pending
│   ├── social-structure/
│   ├── social-stratification/
│   └── institutions/
│
├── political-science/             ⏳ Pending
│   ├── political-theory/
│   ├── comparative-politics/
│   └── international-relations/
│
└── anthropology/                  ⏳ Pending
    ├── cultural-anthropology/
    ├── physical-anthropology/
    └── archaeology/
```

## References

### Classification Standards
- UNESCO ISCED-F 2013: Field 03 (Social Sciences, Journalism, and Information)
- Library of Congress Classification (H: Social Sciences)
- Dewey Decimal Classification (300: Social Sciences)

### Foundational Documents
- `domain/_ontology/global-hierarchy.yaml` - Authoritative taxonomy
- `domain/_ontology/README.md` - Design principles
- `domain/_contexts/economics.jsonld` - Economics vocabulary
- Financial Industry Business Ontology (FIBO) - Finance concepts

## Contributing

When adding content to social sciences:

1. **Verify Social Nature**: Ensure concept studies human society/behavior
2. **Check Existing Structure**: Use established subdomain paths
3. **Mark Domain Status**: Set `isNativeDomain: true` for native concepts
4. **Consider Ethics**: Social science research has ethical implications
5. **Follow AKU Format**: Use AKU v2.0 specification
6. **Validate**: Run validation tools before committing

## Validation

```bash
# Validate economics AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/social-sciences/economics/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/social-sciences/economics/
```

## Related Domains

- **Formal Sciences** (`formal-sciences/`) - Mathematics provides statistical tools
- **Natural Sciences** (`natural-sciences/`) - Psychology draws from neuroscience
- **Health Sciences** (`health-sciences/`) - Public health and clinical psychology overlap
- **Humanities** (`humanities/`) - Philosophy, history overlap with social sciences

---

**Authoritative Source**: This directory hierarchy follows the global ontology defined in `domain/_ontology/global-hierarchy.yaml`

**Questions?** See `domain/_ontology/README.md` for design principles and migration guidance.
