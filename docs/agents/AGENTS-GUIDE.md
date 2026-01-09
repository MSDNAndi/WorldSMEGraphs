# WorldSMEGraphs Agent System Guide

> **Version**: 2.0.0  
> **Updated**: 2026-01-09  
> **Total Agents**: 61  
> **Location**: `.github/agents/`

## Table of Contents

1. [Overview](#overview)
2. [Agent File Format](#agent-file-format)
3. [Agent Categories](#agent-categories)
4. [How Agents Are Loaded](#how-agents-are-loaded)
5. [Invoking Agents](#invoking-agents)
6. [Agent Collaboration Patterns](#agent-collaboration-patterns)
7. [Creating New Agents](#creating-new-agents)
8. [Agent Segmentation Strategy](#agent-segmentation-strategy)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Overview

WorldSMEGraphs uses 61 specialized GitHub Copilot custom agents to create, manage, and enhance its knowledge representation system. These agents work together to:

- Extract knowledge from various sources (textbooks, papers, videos)
- Organize and structure knowledge into atomic units
- Validate and verify accuracy
- Render content for different audiences and languages
- Maintain quality and consistency

### Key Features

- **Language-agnostic knowledge representation**
- **Multi-audience rendering** (toddlers to experts)
- **Multi-lingual support**
- **File-based architecture** (no external databases)
- **Cross-domain knowledge linking**

---

## Agent File Format

### File Structure

All agent files follow the GitHub Copilot custom agent format:

```markdown
---
name: agent-name
description: Brief description of agent capabilities
tools:
- '*'
infer: true
---

# Agent Title

[Detailed agent description and instructions]

## Responsibilities
- Responsibility 1
- Responsibility 2

## Expertise
- Area 1
- Area 2

## Input Requirements
### Required
- Field 1
- Field 2

### Optional
- Field 1

## Output Format
- Output specification

## Usage Examples
```
@agent-name Do something specific
```

## Related Agents
- @other-agent
```

### Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Agent identifier (used for @invocation) |
| `description` | string | Brief capability description |
| `tools` | array | Tool permissions (`'*'` = all tools) |
| `infer` | boolean | Allow inference (`true` recommended) |

### File Naming Convention

```
{agent-name}.agent.md
```

Examples:
- `coordinator.agent.md`
- `paper-miner.agent.md`
- `fact-checking.agent.md`

### Minimum Requirements

- **180 lines minimum** for comprehensive specifications
- Proper YAML frontmatter with all required fields
- Detailed usage examples (50-75+)
- Clear input/output formats
- Cross-references to related agents

---

## Agent Categories

### Core Infrastructure (3 agents)

| Agent | Purpose |
|-------|---------|
| `coordinator` | Multi-agent workflow orchestration, task delegation |
| `recruiter` | Agent ecosystem management, capability matching |
| `quality` | Comprehensive QA procedures, validation |

### Content Creation & Extraction (9 agents)

| Agent | Purpose |
|-------|---------|
| `textbook-parser` | Extract content from textbooks |
| `paper-miner` | Extract from research papers |
| `video-transcriber` | Transcribe educational videos |
| `definition-extractor` | Extract formal definitions |
| `formula-extractor` | Extract mathematical formulas |
| `example-extractor` | Extract worked examples |
| `citation-extractor` | Extract and format citations |
| `relationship-extractor` | Extract conceptual relationships |
| `web-scraper` | Scrape educational web content |

### Knowledge Organization (8 agents)

| Agent | Purpose |
|-------|---------|
| `ontology` | Design ontologies and taxonomies |
| `graph-database` | Graph database architecture |
| `semantic-harmonization` | Resolve semantic conflicts |
| `terminology` | Manage domain terminology |
| `merger` | Merge duplicate AKUs |
| `conflict-resolution` | Resolve conflicting information |
| `provenance-tracking` | Track content lineage |
| `aku-atomicity-specialist` | Manage AKU granularity |

### Quality Assurance (5 agents)

| Agent | Purpose |
|-------|---------|
| `fact-checking` | Verify factual accuracy |
| `peer-review` | Multi-dimensional quality review |
| `verification` | Formal verification, proof checking |
| `citation` | Citation validation |
| `database-query` | Query external databases |

### Rendering & Presentation (5 agents)

| Agent | Purpose |
|-------|---------|
| `rendering-agent` | Transform AKUs for audiences |
| `visualization` | Create visual representations |
| `localization` | Adapt for languages/cultures |
| `accessibility` | Ensure WCAG compliance |
| `image-generation` | Generate images via GPT Image 1.5 |

### Pedagogy & Learning (5 agents)

| Agent | Purpose |
|-------|---------|
| `pedagogy` | Learning science, instructional design |
| `educational-path` | Curriculum design, prerequisites |
| `assessment-creation` | Create Bloom's taxonomy assessments |
| `user-testing` | User research, usability testing |
| `meta-learning` | Learning analytics, adaptive systems |

### Audience Advocates (5 agents)

| Agent | Purpose |
|-------|---------|
| `academic-audience-advocate` | Academic rigor, research standards |
| `student-audience-advocate` | Student learning needs |
| `professional-audience-advocate` | Professional practitioner needs |
| `diverse-learner-advocate` | Accessibility, diverse learning styles |
| `curious-public-advocate` | General public accessibility |

### Domain Expertise (4 agents)

| Agent | Purpose |
|-------|---------|
| `generic-domain-empathy` | Understand any domain, create personas |
| `math-expert` | Mathematical verification |
| `legal-copyright` | IP law, fair use, licensing |
| `standards` | Technical standards compliance |

### Technical Infrastructure (7 agents)

| Agent | Purpose |
|-------|---------|
| `software-architecture` | Architecture patterns, scalability |
| `devops` | CI/CD pipelines, automation |
| `implementation` | Feasibility assessment, planning |
| `research-monitoring` | Track research advances |
| `community-manager` | Community engagement |
| `deprecation` | Manage outdated content |
| `data-integration` | Integrate data from sources |

### Special Purpose (4 agents)

| Agent | Purpose |
|-------|---------|
| `contrarian` | Challenge assumptions, identify weaknesses |
| `contrarian-agent` | Alternate contrarian implementation |
| `multi-lingual-validation` | Validate translations |
| `documentation-agent` | Create and maintain documentation |

### Other Agents

| Agent | Purpose |
|-------|---------|
| `code-review-agent` | Code quality review |
| `file-organization-agent` | File structure management |
| `knowledge-graph-agent` | Knowledge graph creation |
| `research` | Research tasks |
| `example-generation` | Generate examples |
| `domain-expert-template` | Template for domain experts |

---

## How Agents Are Loaded

### GitHub Copilot Custom Agent Loading

GitHub Copilot loads custom agents from `.github/agents/*.agent.md` files. The loading process:

1. **Discovery**: Scans `.github/agents/` for `.agent.md` files
2. **Parsing**: Reads YAML frontmatter for agent metadata
3. **Registration**: Registers agent name for `@` invocation
4. **Instruction Loading**: Loads markdown content as agent instructions

### Critical Requirements

1. **File must start with `---`** (YAML frontmatter delimiter)
2. **`name:` field is required** (used for `@agent-name` invocation)
3. **`description:` field is required** (shown in agent list)
4. **Frontmatter must end with `---`**

### Common Loading Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Missing frontmatter | Agent not recognized | Add `---` delimited YAML block |
| Missing `name:` field | Agent can't be invoked | Add `name:` to frontmatter |
| Invalid YAML | Parsing errors | Validate YAML syntax |
| File not `.agent.md` | Not discovered | Rename to `.agent.md` |

### Verification Script

```bash
# Check all agents have valid frontmatter
bash .github/scripts/check-agent-lengths.sh
```

---

## Invoking Agents

### Basic Syntax

```
@agent-name [specific request with context]
```

### Examples

**Content Extraction:**
```
@textbook-parser Extract Chapters 1-3 from Corporate Finance 13e, domain: finance

@paper-miner Extract methodology from arXiv:2103.12345

@video-transcriber Process MIT 18.06 Linear Algebra Lecture 10
```

**Validation:**
```
@fact-checking Verify statistics in economics AKUs against Federal Reserve data

@peer-review Comprehensive review: NPV module (20 AKUs)

@verification Formal proof check: Nash equilibrium theorem
```

**Organization:**
```
@ontology Design ontology for finance domain: valuation, risk, markets

@merger Merge 3 NPV AKUs, keep all unique examples

@aku-atomicity-specialist Analyze NPV directory for over-bundled AKUs
```

**Rendering:**
```
@rendering-agent Create elementary school rendering of algebra AKUs

@localization Adapt economics content for Japanese business culture

@accessibility Ensure WCAG AA compliance for mathematics content
```

### Best Practices

1. **Be Specific**: Provide clear objectives and success criteria
2. **Include Context**: Give relevant background information
3. **Set Expectations**: Specify format, depth, timeline
4. **Reference Files**: Point to specific files or resources
5. **Define Success**: State how to measure completion

---

## Agent Collaboration Patterns

### Pattern 1: Extract → Validate → Organize → Review

**Use Case**: Creating AKUs from textbook sources

```
textbook-parser → definition-extractor → fact-checking → ontology → peer-review
```

### Pattern 2: Research → Mine → Verify → Integrate

**Use Case**: Incorporating research papers

```
database-query → paper-miner → verification → data-integration → quality
```

### Pattern 3: Design → Render → Adapt → Test

**Use Case**: Multi-audience renderings

```
pedagogy → rendering-agent → localization → accessibility → user-testing
```

### Pattern 4: Create → Critique → Improve → Validate

**Use Case**: Ensuring highest quality output

```
[primary agent] → contrarian → peer-review → quality
```

---

## Creating New Agents

### When to Create a New Agent

- Recurring need for specialized expertise
- Existing agents can't be adapted
- Clear, distinct responsibilities
- Measurable success criteria

### Steps

1. **Use the template**: Copy `domain-expert-template.agent.md`
2. **Define clear responsibilities**: What tasks will it handle?
3. **Set quality criteria**: How to measure success?
4. **Add comprehensive examples**: 50-75+ usage examples
5. **Cross-reference related agents**: Who does it work with?
6. **Test thoroughly**: Run sample tasks

### Template Structure

```markdown
---
name: new-agent
description: Clear description of capabilities
tools:
- '*'
infer: true
---

# Agent: New Agent Name

[Comprehensive description]

## Responsibilities
- [List all responsibilities]

## Expertise
- [List expertise areas]

## Input Requirements
### Required
- [Required inputs]

### Optional
- [Optional inputs]

## Output Format
- [Expected outputs]

## Workflows
[Typical workflow steps]

## Usage Examples
[50-75+ examples]

## Success Criteria
- [Measurable criteria]

## Related Agents
- [Cross-references]
```

---

## Agent Segmentation Strategy

As the agent ecosystem grows, segmentation becomes necessary. Here's the recommended strategy for future organization:

### Current Structure (61 agents)

```
.github/agents/
├── coordinator.agent.md
├── paper-miner.agent.md
├── [57 more agents]
└── README.md
```

### Phase 1: Category Subdirectories (100+ agents)

When reaching 100+ agents, organize by category:

```
.github/agents/
├── core/
│   ├── coordinator.agent.md
│   ├── recruiter.agent.md
│   └── quality.agent.md
├── extraction/
│   ├── paper-miner.agent.md
│   ├── textbook-parser.agent.md
│   └── ...
├── organization/
│   ├── ontology.agent.md
│   ├── merger.agent.md
│   └── ...
├── quality-assurance/
│   ├── fact-checking.agent.md
│   ├── verification.agent.md
│   └── ...
├── rendering/
│   ├── rendering-agent.agent.md
│   ├── visualization.agent.md
│   └── ...
└── README.md
```

### Phase 2: Domain-Specific Repositories (500+ agents)

For domain-specific agents, create separate repositories:

```
# Main repository
MSDNAndi/WorldSMEGraphs
  └── .github/agents/  (core agents only)

# Domain-specific repositories
MSDNAndi/WorldSMEGraphs-agents-medicine
MSDNAndi/WorldSMEGraphs-agents-economics
MSDNAndi/WorldSMEGraphs-agents-physics
MSDNAndi/WorldSMEGraphs-agents-mathematics
```

### Phase 3: Agent Registry (1000+ agents)

Create a centralized registry:

```
.github/agents/
├── registry.yaml          # Agent registry manifest
├── core/                   # Core agents always present
└── domains/               # Domain configs (load on demand)
    ├── medicine.yaml
    ├── economics.yaml
    └── physics.yaml
```

### Migration Guidelines

1. **Maintain backward compatibility**: Keep agent names consistent
2. **Update cross-references**: Fix related agent references
3. **Version carefully**: Use semantic versioning for agent changes
4. **Document migrations**: Track all organizational changes
5. **Test thoroughly**: Verify agents work after reorganization

---

## Best Practices

### Agent Invocation

✅ **DO:**
```
@rendering-agent Create an elementary school English rendering 
of domain/formal-sciences/mathematics/algebra/knowledge.graph 
focusing on variables and equations
```

❌ **DON'T:**
```
@rendering-agent Create a rendering
```

### Agent Development

✅ **DO:**
- Write 180+ lines of comprehensive specifications
- Include 50-75+ usage examples
- Define clear input/output formats
- Cross-reference related agents
- Maintain YAML frontmatter

❌ **DON'T:**
- Create placeholder agents with minimal content
- Skip frontmatter requirements
- Duplicate functionality across agents
- Forget to update related documentation

### Quality Assurance

✅ **DO:**
- Use `@contrarian` to critique agent output
- Run `@peer-review` for quality checks
- Track agent performance via KPIs
- Iterate based on feedback

❌ **DON'T:**
- Blindly accept agent suggestions
- Skip validation steps
- Ignore performance metrics
- Forget to document issues

---

## Troubleshooting

### Agent Not Recognized

**Symptom**: `@agent-name` doesn't invoke the agent

**Solutions**:
1. Check file exists: `.github/agents/agent-name.agent.md`
2. Verify frontmatter starts with `---`
3. Confirm `name:` field matches invocation name
4. Ensure file extension is `.agent.md`

### Agent Returns Unexpected Results

**Symptom**: Agent doesn't follow instructions

**Solutions**:
1. Provide more specific context
2. Check agent's documented expertise areas
3. Review input requirements in agent file
4. Try a different, more specialized agent

### Validation Script Fails

**Symptom**: `check-agent-lengths.sh` reports failures

**Solutions**:
1. Add more content to meet 180-line minimum
2. Include more usage examples
3. Expand input/output documentation
4. Add detailed workflows

### Frontmatter Parsing Errors

**Symptom**: Agent loads but with wrong metadata

**Solutions**:
1. Validate YAML syntax (indentation, colons)
2. Ensure no tabs in YAML (use spaces)
3. Quote strings with special characters
4. Close frontmatter with `---`

---

## Related Documentation

- [Agent README](.github/agents/README.md) - Quick reference
- [Agent KPIs](.github/copilot/agent-kpis.md) - Performance tracking
- [Copilot Instructions](.github/copilot-instructions.md) - Main instructions
- [Contributing Guide](docs/CONTRIBUTING.md) - Contribution guidelines

---

## Appendix: Full Agent List

| # | Agent Name | Category | Lines |
|---|------------|----------|-------|
| 1 | coordinator | Core | 300 |
| 2 | recruiter | Core | 451 |
| 3 | quality | Core | 296 |
| 4 | textbook-parser | Extraction | 224 |
| 5 | paper-miner | Extraction | 200 |
| 6 | video-transcriber | Extraction | 227 |
| 7 | definition-extractor | Extraction | 189 |
| 8 | formula-extractor | Extraction | 195 |
| 9 | example-extractor | Extraction | 193 |
| 10 | citation-extractor | Extraction | 193 |
| 11 | relationship-extractor | Extraction | 203 |
| 12 | web-scraper | Extraction | 192 |
| ... | (See .github/agents/README.md for complete list) | ... | ... |

---

*Last updated: 2026-01-09*
