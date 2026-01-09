# Agent Segmentation Strategy

> **Version**: 1.0.0  
> **Created**: 2026-01-09  
> **Status**: Planning  
> **Purpose**: Future-proof agent organization for scaling

## Overview

As WorldSMEGraphs grows, the agent ecosystem will need to be organized for maintainability. This document outlines strategies for segmenting agents into logical groups as the project scales.

## Current State

- **Total Agents**: 61
- **Location**: `.github/agents/`
- **Format**: `.agent.md` files with YAML frontmatter
- **Categories**: 11 functional categories

## Scaling Thresholds

| Agent Count | Recommended Action |
|-------------|-------------------|
| 1-100 | Single directory with categories in README |
| 100-250 | Subdirectory organization by category |
| 250-500 | Domain-specific subdirectories |
| 500+ | Multi-repository architecture |

---

## Phase 1: Category Subdirectories (100+ agents)

### When to Implement
- Agent count exceeds 100
- Frequent confusion about which agent to use
- Category-specific updates become common

### Proposed Structure

```
.github/agents/
├── core/
│   ├── coordinator.agent.md
│   ├── recruiter.agent.md
│   └── quality.agent.md
├── extraction/
│   ├── paper-miner.agent.md
│   ├── textbook-parser.agent.md
│   ├── video-transcriber.agent.md
│   ├── definition-extractor.agent.md
│   ├── formula-extractor.agent.md
│   ├── example-extractor.agent.md
│   ├── citation-extractor.agent.md
│   ├── relationship-extractor.agent.md
│   └── web-scraper.agent.md
├── organization/
│   ├── ontology.agent.md
│   ├── graph-database.agent.md
│   ├── semantic-harmonization.agent.md
│   ├── terminology.agent.md
│   ├── merger.agent.md
│   ├── conflict-resolution.agent.md
│   ├── provenance-tracking.agent.md
│   └── aku-atomicity-specialist.agent.md
├── quality-assurance/
│   ├── fact-checking.agent.md
│   ├── peer-review.agent.md
│   ├── verification.agent.md
│   ├── citation.agent.md
│   └── database-query.agent.md
├── rendering/
│   ├── rendering-agent.agent.md
│   ├── visualization.agent.md
│   ├── localization.agent.md
│   ├── accessibility.agent.md
│   └── image-generation.agent.md
├── pedagogy/
│   ├── pedagogy.agent.md
│   ├── educational-path.agent.md
│   ├── assessment-creation.agent.md
│   ├── user-testing.agent.md
│   └── meta-learning.agent.md
├── audience-advocates/
│   ├── academic-audience-advocate.agent.md
│   ├── student-audience-advocate.agent.md
│   ├── professional-audience-advocate.agent.md
│   ├── diverse-learner-advocate.agent.md
│   └── curious-public-advocate.agent.md
├── domain-experts/
│   ├── generic-domain-empathy.agent.md
│   ├── math-expert.agent.md
│   ├── legal-copyright.agent.md
│   └── standards.agent.md
├── infrastructure/
│   ├── software-architecture.agent.md
│   ├── devops.agent.md
│   ├── implementation.agent.md
│   ├── research-monitoring.agent.md
│   ├── community-manager.agent.md
│   ├── deprecation.agent.md
│   └── data-integration.agent.md
├── special/
│   ├── contrarian.agent.md
│   ├── contrarian-agent.agent.md
│   ├── multi-lingual-validation.agent.md
│   ├── documentation-agent.agent.md
│   ├── code-review-agent.agent.md
│   ├── file-organization-agent.agent.md
│   ├── knowledge-graph-agent.agent.md
│   ├── research.agent.md
│   ├── example-generation.agent.md
│   └── domain-expert-template.agent.md
└── README.md
```

### Migration Steps

1. Create subdirectories
2. Move agent files to appropriate directories
3. Update all cross-references
4. Update validation scripts to scan subdirectories
5. Update documentation
6. Test agent loading

### Backward Compatibility

- Ensure GitHub Copilot scans subdirectories
- Consider symlinks if flat structure required
- Update `@agent-name` invocations if needed

---

## Phase 2: Domain-Specific Subdirectories (250+ agents)

### When to Implement
- Significant domain-specific agents emerge
- Different teams work on different domains
- Domain-specific validation rules needed

### Proposed Structure

```
.github/agents/
├── core/                    # Core infrastructure agents
├── general/                 # General-purpose agents
│   ├── extraction/
│   ├── organization/
│   ├── quality-assurance/
│   ├── rendering/
│   └── pedagogy/
└── domains/                 # Domain-specific agents
    ├── medicine/
    │   ├── medical-terminology.agent.md
    │   ├── clinical-validation.agent.md
    │   └── icd-coding.agent.md
    ├── economics/
    │   ├── economic-modeling.agent.md
    │   ├── financial-analysis.agent.md
    │   └── market-research.agent.md
    ├── physics/
    │   ├── physics-formula.agent.md
    │   └── experiment-design.agent.md
    ├── mathematics/
    │   ├── theorem-prover.agent.md
    │   └── mathematical-notation.agent.md
    └── computer-science/
        ├── algorithm-analysis.agent.md
        └── code-verification.agent.md
```

---

## Phase 3: Multi-Repository Architecture (500+ agents)

### When to Implement
- Agent count exceeds 500
- Domain teams need independent development
- Different release cycles for domains
- Performance concerns with single repository

### Repository Structure

```
# Main repository (core agents + registry)
MSDNAndi/WorldSMEGraphs
  ├── .github/agents/
  │   ├── core/              # Core agents only
  │   └── registry.yaml      # Agent registry manifest
  └── ...

# Domain-specific agent repositories
MSDNAndi/WorldSMEGraphs-agents-medicine
  ├── .github/agents/
  │   ├── medical-terminology.agent.md
  │   ├── clinical-validation.agent.md
  │   └── ...
  └── README.md

MSDNAndi/WorldSMEGraphs-agents-economics
  ├── .github/agents/
  │   └── ...
  └── README.md

MSDNAndi/WorldSMEGraphs-agents-physics
  └── ...

MSDNAndi/WorldSMEGraphs-agents-mathematics
  └── ...

MSDNAndi/WorldSMEGraphs-agents-computer-science
  └── ...
```

### Registry Manifest

```yaml
# registry.yaml
version: "1.0"
repositories:
  - name: core
    location: local
    path: .github/agents/core/
    agents:
      - coordinator
      - recruiter
      - quality
  
  - name: medicine
    location: github
    repo: MSDNAndi/WorldSMEGraphs-agents-medicine
    branch: main
    agents:
      - medical-terminology
      - clinical-validation
      - icd-coding
  
  - name: economics
    location: github
    repo: MSDNAndi/WorldSMEGraphs-agents-economics
    branch: main
    agents:
      - economic-modeling
      - financial-analysis
```

### Synchronization Strategy

1. **Git Submodules**: Link domain repos as submodules
2. **CI/CD Integration**: Automated sync on releases
3. **Version Pinning**: Pin to specific versions
4. **Fallback**: Core agents always available

---

## Implementation Guidelines

### Agent Naming Conventions

| Level | Convention | Example |
|-------|------------|---------|
| Core | Simple descriptive | `coordinator` |
| Category | Function-focused | `paper-miner` |
| Domain | Domain-prefixed | `medical-terminology` |

### Cross-Reference Updates

When moving agents:
1. Search for all `@agent-name` references
2. Update agent documentation cross-references
3. Update README agent lists
4. Run validation scripts

### Validation Script Updates

The validation scripts will need updates for subdirectory scanning:

```bash
# Updated pattern for subdirectories
for agent_file in "$AGENTS_DIR"/**/*.agent.md; do
    ...
done
```

### Testing Checklist

- [ ] All agents load correctly
- [ ] `@agent-name` invocation works
- [ ] Cross-references resolve
- [ ] Validation scripts pass
- [ ] Documentation is accurate

---

## Metrics for Decision Making

Track these metrics to decide when to advance phases:

| Metric | Threshold | Action |
|--------|-----------|--------|
| Agent count | 100+ | Start Phase 1 |
| Average time to find agent | >30 seconds | Consider reorganization |
| Agent category size | 20+ in one category | Split category |
| Domain-specific agents | 10+ per domain | Start Phase 2 |
| Repository size | >100MB | Consider Phase 3 |

---

## Related Documents

- [AGENTS-GUIDE.md](./AGENTS-GUIDE.md) - Main agent documentation
- [Agent README](../../.github/agents/README.md) - Agent list
- [Project Structure](../../.project/structure.md) - Overall structure

---

*Last Updated: 2026-01-09*
