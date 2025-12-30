# WorldSMEGraphs Project Structure

> **Last Updated**: 2025-12-29  
> **Maintained By**: File Organization Agent, Implementation Agent  
> **Review Frequency**: After every significant structure change

## Overview
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. All data is stored in files, enabling version control, portability, and collaborative editing.

## Top-Level Structure

```
WorldSMEGraphs/
├── .github/                  # GitHub configuration and Copilot agents
│   ├── agents/              # GitHub Copilot custom agent definitions (.agent.md)
│   │   ├── recruiter.agent.md        # Format gatekeeper agent
│   │   ├── coordinator.agent.md       # Workflow orchestration agent
│   │   └── [52 other agents].agent.md # Specialized domain agents
│   ├── copilot/             # Copilot configuration
│   │   ├── agents/          # Legacy agent utilities
│   │   └── agent-kpis.md   # Agent performance tracking
│   ├── workflows/           # GitHub Actions workflows
│   └── copilot-instructions.md  # Main Copilot instructions
│
├── .project/                # Project metadata and documentation
│   ├── structure.md         # This file - project organization
│   ├── roadmap.md          # Project roadmap and planning
│   ├── knowledge-format.md  # Knowledge graph format specification
│   ├── rendering-spec.md    # Rendering system specification
│   └── work-continuation.md # Work session guide (50-minute sessions)
│
├── domain/                  # Knowledge domain hierarchies
│   ├── science/            # Science domains
│   │   ├── math/
│   │   │   ├── algebra/
│   │   │   │   ├── knowledge.graph        # Language-agnostic representation
│   │   │   │   ├── schema.json           # Graph schema definition
│   │   │   │   └── .renders/             # Human-readable renderings
│   │   │   │       ├── english/
│   │   │   │       │   ├── elementary-school.md
│   │   │   │       │   ├── high-school.md
│   │   │   │       │   ├── graduate.md
│   │   │   │       │   └── 4-year-old.md
│   │   │   │       └── german/
│   │   │   │           ├── grundschule.md
│   │   │   │           └── hochschule.md
│   │   │   ├── number-theory/
│   │   │   │   └── primes/                # Prime Numbers ✓ Complete (10 AKUs)
│   │   │   │       ├── concept-index.yaml
│   │   │   │       ├── README.md
│   │   │   │       ├── akus/
│   │   │   │       │   ├── definitions/     (1 AKU)
│   │   │   │       │   ├── theory/          (3 AKUs)
│   │   │   │       │   ├── formulas/        (1 AKU)
│   │   │   │       │   └── applications/    (5 AKUs)
│   │   │   │       └── .renders/
│   │   │   │           └── english/         (to be created)
│   │   │   ├── geometry/
│   │   │   └── calculus/
│   │   ├── physics/
│   │   └── chemistry/
│   │
│   ├── economics/          # Economics domains
│   │   ├── macroeconomics/
│   │   │   ├── knowledge.graph
│   │   │   └── .renders/
│   │   │       └── english/
│   │   │           ├── adult-limited-reading.md
│   │   │           └── graduate.md
│   │   └── microeconomics/
│   │
│   ├── medicine/           # Medical domains ✓ NEW
│   │   └── surgery/
│   │       └── vascular/
│   │           ├── procedures/
│   │           │   └── evar/              # EVAR procedure (placeholder)
│   │           ├── pathology/
│   │           │   └── aaa/               # Abdominal Aortic Aneurysm (placeholder)
│   │           └── complications/
│   │               └── endoleaks/
│   │                   └── type-2/        # Type 2 Endoleak ✓ Complete (5 AKUs)
│   │                       ├── concept-index.yaml
│   │                       ├── akus/
│   │                       │   ├── definitions/     (2 AKUs)
│   │                       │   ├── pathophysiology/ (1 AKU)
│   │                       │   ├── diagnosis/       (1 AKU)
│   │                       │   ├── management/      (1 AKU)
│   │                       │   └── clinical/        (1 AKU)
│   │                       └── .renders/
│   │                           └── english/
│   │                               └── medical-student-guide.md
│   │
│   └── [other-domains]/    # Additional domain hierarchies
│
├── docs/                   # General project documentation
│   ├── README.md          # Main documentation
│   ├── CONTRIBUTING.md    # Contribution guidelines
│   └── getting-started.md # Quick start guide
│
└── TODO                    # Task tracking file

```

## Directory Purposes

### `.github/`
GitHub-specific configuration including:
- **agents/**: GitHub Copilot custom agent definitions (.agent.md format)
  - All 53 agents in standardized format
  - **recruiter.agent.md**: Format gatekeeper and ecosystem curator
  - **coordinator.agent.md**: Multi-agent workflow orchestrator
  - Location per GitHub Copilot standards: `.github/agents/`
- **copilot/**: Copilot configuration
  - **agents/**: Legacy agent utilities and scripts
  - **agent-kpis.md**: Performance tracking for all agents
- **workflows/**: GitHub Actions for CI/CD and automation
- **copilot-instructions.md**: Main instructions for Copilot

### `.project/`
Project metadata and specifications:
- **structure.md**: This file, describing project organization
- **roadmap.md**: Project goals, milestones, and planning
- **knowledge-format.md**: Specification for knowledge graph format
- **knowledge-maturity-model.md**: Domain maturity assessment framework (NEW)
- **rendering-spec.md**: Guidelines for rendering system
- **agents/domain-maturity/**: Domain completeness tracking system
  - **domain_maturity_tracker.py**: Core assessment tool
  - **generate_dashboard.py**: Visual dashboard generator
  - **maturity_history.json**: Historical tracking data
  - **README.md**: System documentation

### `domain/`
Knowledge domain hierarchies organized by subject matter:
- **Structure**: `domain/[category]/[subcategory]/[topic]/`
- **Required Files**:
  - `knowledge.graph`: Language-agnostic knowledge representation
  - `schema.json`: Schema definition for the graph
  - `.renders/`: Directory for human-readable renderings
  - `COMPLETENESS_METADATA.yaml`: Domain maturity tracking metadata (OPTIONAL but recommended)
- **Rendering Structure**: `.renders/[language]/[audience-level].[format]`

### `docs/`
General documentation accessible to all users:
- **CONTRIBUTING.md**: Contribution guidelines and workflows
- **knowledge-maturity-tracking.md**: Comprehensive guide to domain maturity tracking (NEW)
- Additional documentation files as needed

## File Naming Conventions

### Knowledge Graphs
- **Format**: `knowledge.graph`
- **Location**: In the specific topic directory
- **Always accompanied by**: `schema.json`

### Renderings
- **Format**: `[audience-level].[format]`
- **Examples**: 
  - `elementary-school.md`
  - `graduate.pdf`
  - `adult-limited-reading.md`
  - `4-year-old.md`
- **Location**: `.renders/[language]/`

### Documentation
- **Use kebab-case**: `getting-started.md`, `knowledge-format.md`
- **Descriptive names**: Clear purpose from filename
- **Markdown default**: Use `.md` unless other format required

### GitHub Copilot Agents
- **Format**: `[agent-name].agent.md`
- **Location**: `.github/agents/`
- **Naming**: kebab-case for agent names
- **Examples**:
  - `recruiter.agent.md` - Format gatekeeper
  - `coordinator.agent.md` - Workflow orchestration
  - `paper-miner.agent.md` - Research paper extraction

### Schemas
- **Format**: `schema.json`
- **Location**: Same directory as corresponding `knowledge.graph`

## Organization Principles

### 1. Hierarchy by Subject Matter
Organize domains hierarchically from broad to specific:
- Level 1: Major category (science, economics, humanities)
- Level 2: Discipline (math, physics, macroeconomics)
- Level 3: Topic (algebra, mechanics, monetary-policy)

### 2. Separation of Concerns
- **Knowledge**: Language-agnostic in `.graph` files
- **Renderings**: Language and audience-specific in `.renders/`
- **Metadata**: Schemas and configuration separate from content
- **Infrastructure**: GitHub and project config in dotfiles

### 3. Consistent Structure
Each domain topic follows the same pattern:
```
[topic]/
├── knowledge.graph
├── schema.json
└── .renders/
    └── [language]/
        └── [audience].[format]
```

### 4. File-Based Everything
- No external databases required
- All data in version control
- Portable and collaborative
- Easy to backup and distribute

## Excluded from Repository

Listed in `.gitignore`:
- Build artifacts
- Temporary files (`/tmp`)
- IDE-specific files
- OS-specific files (`.DS_Store`, `Thumbs.db`)
- Generated files (unless explicitly needed)
- Node modules or dependency directories
- Compiled binaries

## Adding New Domains

1. Create directory structure: `domain/[category]/[subcategory]/[topic]/`
2. Add `knowledge.graph` file with content
3. Add `schema.json` with graph schema
4. Create `.renders/` directory
5. Add initial renderings for at least one language/audience
6. Update this structure document
7. Create domain-specific README if needed

## Adding New Agents

1. Create agent file: `.github/agents/[agent-name].agent.md`
2. Follow GitHub Copilot custom agent format
3. Include all required sections:
   - Purpose
   - Responsibilities
   - Expertise
   - Input Requirements
   - Output Format
   - Usage Examples
   - Success Criteria
   - Related Agents
4. Have recruiter agent review for format compliance
5. Update agent README if adding to new category
6. Test agent invocation with examples

## Maintenance Guidelines

### Regular Reviews
- **Weekly**: Check for misplaced files
- **Monthly**: Identify redundancies
- **Quarterly**: Review and optimize structure

### When to Refactor
- Duplicate information across multiple files
- Deep nesting (>5 levels)
- Unclear organization
- Difficulty finding files
- Related content in separate locations

### Documentation Updates
- Update this file after structural changes
- Keep README synchronized with actual structure
- Document reasons for significant reorganizations
- Maintain changelog of structure changes

## See Also
- [Copilot Instructions](../.github/copilot-instructions.md)
- [Agent Directory](../.github/agents/)
- [Agent Performance Tracking](../.github/copilot/agent-kpis.md)
- [Knowledge Format Specification](knowledge-format.md)
- [Rendering Specification](rendering-spec.md)
- [Project Roadmap](roadmap.md)

---

**Last Updated**: 2025-12-30  
**Major Changes**: 
- 2025-12-30: Added prime numbers domain with 10 AKUs and cross-domain connections
- 2025-12-27: Added medicine domain with vascular surgery Type 2 endoleak (5 AKUs complete)
- 2025-12-27: Updated agent infrastructure section for .agent.md format migration
- 2025-12-26: Initial structure documentation
