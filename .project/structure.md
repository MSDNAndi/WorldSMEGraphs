# WorldSMEGraphs Project Structure

> **Last Updated**: 2026-01-04  
> **Maintained By**: File Organization Agent, Implementation Agent  
> **Review Frequency**: After every significant structure change

## Overview
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. All data is stored in files, enabling version control, portability, and collaborative editing.

## 🚧 Migration Status (2026-01-04)

**Active Migration**: Transitioning from legacy structure to global hierarchy per `domain/_ontology/global-hierarchy.yaml`

### Completed ✅
- **Category Theory (8 AKUs)**: Migrated from `science/computer-science/functional-theory/category-theory/` → `formal-sciences/mathematics/pure-mathematics/category-theory/`
- **Functional Programming AKUs (19 AKUs)**: Updated with `isApplicationDomain: true` and `cross_domain_references`
- **New hierarchy directories created**: formal-sciences, natural-sciences, social-sciences, health-sciences

### In Progress 🔄
- **Documentation updates**: Updating structure.md, README files
- **Validation**: Running cross-domain validators on migrated content

### Pending ⏳
- **Physics (138 AKUs)**: To migrate from `science/physics/` → `natural-sciences/physics/`
- **Economics (12 AKUs)**: To migrate from `economics/` → `social-sciences/economics/`
- **Medicine (67 AKUs)**: To migrate from `medicine/` → `health-sciences/medicine/`
- **Mathematics**: Remaining math content in `science/math/` → `formal-sciences/mathematics/`
- **Computer Science**: Other CS content → `formal-sciences/computer-science/`

### Migration Tools
- `domain/_ontology/tools/migrate_category_theory.py` - Category theory migration (completed)
- `domain/_ontology/tools/update_fp_cross_domain.py` - FP cross-domain refs (completed)
- Future: General-purpose domain migration script for remaining content

See: Issue #3 in `.project/issues.md` for detailed migration plan

## New Hierarchy Structure (per global-hierarchy.yaml)

```
domain/
├── _contexts/                 # JSON-LD semantic vocabularies
├── _ontology/                 # Global hierarchy and tools
│
├── formal-sciences/          # ✓ NEW - Abstract/formal sciences
│   ├── mathematics/
│   │   └── pure-mathematics/
│   │       └── category-theory/     # ✓ MIGRATED (8 AKUs)
│   │           ├── akus/
│   │           └── README.md
│   └── computer-science/
│       └── programming-paradigms/
│           └── functional-programming/  # Future FP home
│
├── natural-sciences/         # ✓ NEW - Empirical sciences
│   ├── physics/              # To migrate from science/physics/ (138 AKUs)
│   ├── chemistry/
│   └── biology/
│
├── social-sciences/          # ✓ NEW - Human society
│   └── economics/            # To migrate from economics/ (12 AKUs)
│
├── health-sciences/          # ✓ NEW - Health and medicine
│   └── medicine/             # To migrate from medicine/ (67 AKUs)
│
├── science/                  # 🔄 LEGACY - Being phased out
│   ├── math/                 # To migrate to formal-sciences/mathematics/
│   ├── computer-science/
│   │   └── functional-theory/   # FP app AKUs (19, updated with cross-refs)
│   └── physics/              # To migrate to natural-sciences/physics/
│
├── economics/                # 🔄 LEGACY - Being phased out
└── medicine/                 # 🔄 LEGACY - Being phased out
```

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
│   ├── _contexts/          # JSON-LD context files for semantic vocabulary
│   │   ├── README.md              # Context file documentation
│   │   ├── base.jsonld            # Core vocabulary (Schema.org, SKOS, DC)
│   │   ├── medicine.jsonld        # Medical domain vocabulary (SNOMED CT, MeSH)
│   │   ├── economics.jsonld       # Economics domain vocabulary (FIBO)
│   │   ├── science.jsonld         # Science domain vocabulary (QUDT, ChEBI)
│   │   └── cross-domain.jsonld    # Cross-domain relationship vocabulary ✓ NEW
│   │
│   ├── _ontology/          # Global domain taxonomy and ontology ✓ NEW
│   │   ├── README.md              # Design documentation
│   │   └── global-hierarchy.yaml  # Authoritative domain hierarchy
│   │
│   ├── science/            # Science domains (to be migrated to formal-sciences/natural-sciences)
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
│   │   ├── computer-science/
│   │   │   └── functional-theory/         # FP concepts (27 AKUs) - to be refactored
│   │   │       ├── concept-index.yaml     # NOTE: Category theory to migrate to
│   │   │       ├── README.md              # formal-sciences/mathematics/pure-mathematics/category-theory
│   │   │       ├── category-theory/       # 8 AKUs (⚠️ migration pending per global-hierarchy.yaml)
│   │   │       ├── functors/              # 6 AKUs
│   │   │       ├── monoids/               # 5 AKUs
│   │   │       └── monads/                # 8 AKUs
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
│   │           │   ├── aaa/               # Abdominal Aortic Aneurysm (placeholder)
│   │           │   └── mesenteric-ischemia/  # Mesenteric Ischemia ✓ Complete (29 AKUs)
│   │           │       ├── concept-index.yaml
│   │           │       ├── README.md
│   │           │       ├── akus/
│   │           │       │   ├── definitions/        (4 AKUs)
│   │           │       │   ├── epidemiology/       (1 AKU)
│   │           │       │   ├── pathophysiology/    (4 AKUs)
│   │           │       │   ├── diagnosis/          (3 AKUs)
│   │           │       │   ├── imaging/            (2 AKUs)
│   │           │       │   ├── treatment/          (6 AKUs)
│   │           │       │   ├── surgical-dilemmas/  (6 AKUs)
│   │           │       │   ├── outcomes/           (2 AKUs)
│   │           │       │   └── follow-up/          (1 AKU)
│   │           │       └── .renders/
│   │           │           └── english/
│   │           │               └── book-chapter-surgical-dilemmas.md  # 25-30 page chapter
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

### 1. Native Domain Placement (NEW)
Concepts belong to their NATIVE domain (origin), not application domains:
- **Category Theory** → `formal-sciences/mathematics/pure-mathematics/category-theory/` (not under computer-science)
- **Linear Algebra** → `formal-sciences/mathematics/pure-mathematics/algebra/linear-algebra/` (even if used 95% in ML)
- Applications create LINKS to source concepts, not copies

See `domain/_ontology/global-hierarchy.yaml` for the authoritative domain taxonomy.

### 2. Hierarchy by Subject Matter
Organize domains hierarchically from broad to specific:
- Level 1: Top-level domain (formal-sciences, natural-sciences, social-sciences, health-sciences, engineering, humanities, arts)
- Level 2: Discipline (mathematics, physics, economics, medicine)
- Level 3: Subdiscipline (pure-mathematics, applied-mathematics, vascular-surgery)
- Level 4+: Specific topics (category-theory, linear-algebra, endoleaks)

### 3. Cross-Domain Linking
- Applications link to native concepts using `crossDomainReferences`
- Use relationship types: `uses`, `applies`, `extends`, `informs`
- See `domain/_contexts/cross-domain.jsonld` for vocabulary

### 4. Separation of Concerns
- **Knowledge**: Language-agnostic in `.graph` files
- **Renderings**: Language and audience-specific in `.renders/`
- **Metadata**: Schemas and configuration separate from content
- **Infrastructure**: GitHub and project config in dotfiles

### 5. Consistent Structure
Each domain topic follows the same pattern:
```
[topic]/
├── knowledge.graph
├── schema.json
└── .renders/
    └── [language]/
        └── [audience].[format]
```

### 6. File-Based Everything
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
- [Global Domain Hierarchy](../domain/_ontology/global-hierarchy.yaml) ✓ NEW
- [Cross-Domain Context](../domain/_contexts/cross-domain.jsonld) ✓ NEW

---

**Last Updated**: 2026-01-04  
**Major Changes**: 
- 2026-01-04: Added global domain hierarchy (`domain/_ontology/global-hierarchy.yaml`) with rigorous taxonomy based on UNESCO/LOC/DDC
- 2026-01-04: Added cross-domain relationship vocabulary (`domain/_contexts/cross-domain.jsonld`)
- 2026-01-04: Established native domain placement principle - category theory belongs to mathematics, not computer-science
- 2026-01-04: Added functional-theory domain under science/computer-science (category theory, functors, monoids, monads) - ⚠️ migration pending
- 2025-12-30: Added mesenteric ischemia domain with 29 AKUs and rendered book chapter (25-30 pages)
- 2025-12-30: Added prime numbers domain with 10 AKUs and cross-domain connections
- 2025-12-27: Added medicine domain with vascular surgery Type 2 endoleak (5 AKUs complete)
- 2025-12-27: Updated agent infrastructure section for .agent.md format migration
- 2025-12-26: Initial structure documentation
