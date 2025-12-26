# WorldSMEGraphs Project Structure

> **Last Updated**: 2025-12-26  
> **Maintained By**: File Organization Agent  
> **Review Frequency**: After every significant structure change

## Overview
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. All data is stored in files, enabling version control, portability, and collaborative editing.

## Top-Level Structure

```
WorldSMEGraphs/
├── .github/                  # GitHub configuration and Copilot agents
│   ├── copilot/             # Copilot agent configurations
│   │   ├── agents/          # Individual agent definitions
│   │   └── agent-kpis.md   # Agent performance tracking
│   ├── workflows/           # GitHub Actions workflows
│   └── copilot-instructions.md  # Main Copilot instructions
│
├── .project/                # Project metadata and documentation
│   ├── structure.md         # This file - project organization
│   ├── roadmap.md          # Project roadmap and planning
│   ├── knowledge-format.md  # Knowledge graph format specification
│   └── rendering-spec.md    # Rendering system specification
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
- **copilot/**: Copilot Coding Agent infrastructure
  - **agents/**: Individual agent definitions and instructions
  - **agent-kpis.md**: Performance tracking for all agents
- **workflows/**: GitHub Actions for CI/CD and automation
- **copilot-instructions.md**: Main instructions for Copilot

### `.project/`
Project metadata and specifications:
- **structure.md**: This file, describing project organization
- **roadmap.md**: Project goals, milestones, and planning
- **knowledge-format.md**: Specification for knowledge graph format
- **rendering-spec.md**: Guidelines for rendering system

### `domain/`
Knowledge domain hierarchies organized by subject matter:
- **Structure**: `domain/[category]/[subcategory]/[topic]/`
- **Required Files**:
  - `knowledge.graph`: Language-agnostic knowledge representation
  - `schema.json`: Schema definition for the graph
  - `.renders/`: Directory for human-readable renderings
- **Rendering Structure**: `.renders/[language]/[audience-level].[format]`

### `docs/`
General documentation accessible to all users:
- README, contributing guidelines, tutorials, etc.

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
- [Knowledge Format Specification](knowledge-format.md)
- [Rendering Specification](rendering-spec.md)
- [Project Roadmap](roadmap.md)
