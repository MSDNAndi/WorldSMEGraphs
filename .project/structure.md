# WorldSMEGraphs Project Structure

> **Last Updated**: 2026-01-04  
> **Maintained By**: File Organization Agent, Implementation Agent  
> **Review Frequency**: After every significant structure change

## Overview
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. All data is stored in files, enabling version control, portability, and collaborative editing.

## ✅ Migration Status (2026-01-04 - COMPLETE at 18:50 UTC)

**Migration COMPLETE!** ✅ All domains successfully transitioned to global hierarchy per `domain/_ontology/global-hierarchy.yaml`

### Final Results ✅
- **Category Theory (27 AKUs)**: Migrated all components (8 ct + 6 functors + 8 monads + 5 monoids)
  - FROM: `science/computer-science/functional-theory/` → TO: `formal-sciences/mathematics/pure-mathematics/category-theory/`
- **Mathematics (21 AKUs)**: Migrated geometry and number-theory content
  - FROM: `science/math/` → TO: `formal-sciences/mathematics/pure-mathematics/`
- **Physics (138 AKUs)**: Complete migration including 2 metadata files
  - FROM: `science/physics/` → TO: `natural-sciences/physics/`
- **Economics (12 AKUs)**: Complete migration including 11 schema files + 1 terminology
  - FROM: `economics/` → TO: `social-sciences/economics/`
- **Medicine (68 AKUs)**: Complete migration including 3 terminology files
  - FROM: `medicine/` → TO: `health-sciences/medicine/`

**Total Files Processed**: 293 total (40 newly migrated + 253 verified duplicates)
- **New migrations**: 40 files (category theory + math)
- **Missing files added**: 16 files (metadata, terminology, schema)
- **Duplicates removed**: 293 files from old locations
- **Legacy directories removed**: 3 (science, economics, medicine)

### Final Statistics
- **formal-sciences**: 48 JSON files
- **natural-sciences**: 138 JSON files
- **social-sciences**: 12 JSON files
- **health-sciences**: 68 JSON files
- **Total**: 266 JSON files (256 AKUs + 10 schema/metadata)

### Migration Tools ✅
- `domain/_ontology/tools/migrate_category_theory.py` - Category theory migration
- `domain/_ontology/tools/update_fp_cross_domain.py` - FP cross-domain refs
- `domain/_ontology/tools/migrate_domain.py` - General-purpose migration

**See**: `.project/tracking/migration-pr30-completion-report.md` for complete details  
**Issue**: #3 in `.project/issues.md` marked COMPLETE

## Current Hierarchy Structure (post-migration)

```
domain/
├── _contexts/                 # JSON-LD semantic vocabularies
├── _ontology/                 # Global hierarchy and tools
│   ├── README.md
│   ├── global-hierarchy.yaml  # Authoritative source
│   └── tools/
│       ├── migrate_domain.py
│       └── validate_cross_domain.py
│
├── formal-sciences/          # ✅ COMPLETE - Abstract/formal sciences
│   ├── mathematics/
│   │   └── pure-mathematics/
│   │       ├── category-theory/     # ✅ 27 AKUs (ct, functors, monads, monoids)
│   │       │   ├── akus/
│   │       │   ├── functors/
│   │       │   ├── monads/
│   │       │   ├── monoids/
│   │       │   └── README.md
│   │       ├── geometry/            # ✅ 5 AKUs (golden-ratio)
│   │       │   └── golden-ratio/
│   │       └── number-theory/       # ✅ 16 AKUs (7 subdirectories)
│   │           ├── primes/
│   │           ├── fibonacci/
│   │           ├── perfect-numbers/
│   │           ├── mersenne-primes/
│   │           ├── composite-numbers/
│   │           ├── amicable-numbers/
│   │           └── fermat-primes/
│   └── computer-science/
│       └── programming-paradigms/
│           └── functional-programming/  # ✅ 19 AKUs with cross-domain refs
│
├── natural-sciences/         # ✅ COMPLETE - Empirical sciences  
│   └── physics/              # ✅ 138 AKUs
│       ├── atomic-physics/
│       ├── cosmology/
│       ├── general-relativity/
│       ├── particle-physics/
│       ├── measurement-limits/
│       │   ├── minimum-measurable-quantities/
│       │   └── theoretical-minimum-limits/
│       └── quantum-mechanics/
│           └── planck-units/
│
├── social-sciences/          # ✅ COMPLETE - Human society
│   └── economics/            # ✅ 12 AKUs + schema files
│       └── bwl/
│           ├── finance/valuation/npv/
│           ├── accounting/
│           ├── entrepreneurship/
│           ├── marketing/
│           ├── strategy/
│           ├── organization/
│           ├── human-resources/
│           ├── controlling/
│           └── operations/
│
└── health-sciences/          # ✅ ACTIVE - Health and medicine
    └── medicine/             # ✅ 598+ AKUs + terminology
        └── surgery/vascular/
            ├── anatomy/akus/{collaterals,variants}/
            ├── complications/akus/              # Endoleak, migration, pseudoaneurysm, etc.
            ├── diagnostics/akus/{imaging,noninvasive,physical-exam}/
            ├── dialysis-access/akus/            # AVF, maturation, steal, DRIL
            ├── foundations/                     # Foundational concepts
            ├── pathology/
            │   ├── aortic/
            │   ├── cerebrovascular/akus/        # Carotid, stroke, TIA
            │   ├── congenital/akus/
            │   ├── genetic-disorders/akus/      # FMD, HHT, Marfan, etc.
            │   ├── lymphatic/akus/
            │   ├── mesenteric/akus/
            │   ├── rare-syndromes/akus/         # TOS, Leriche, entrapment
            │   ├── renal-artery/akus/
            │   ├── trauma/regional/akus/
            │   ├── upper-extremity/akus/
            │   ├── vascular-malformations/akus/
            │   └── venous/akus/{chronic,physiology,procedures,superficial}/
            ├── pharmacology/akus/{anticoagulation,antiplatelet,claudication}/
            ├── procedures/akus/{bypass,carotid,endovascular,access,techniques}/
            ├── terminology/
            └── wound-care/akus/
```

**Legacy directories (`science/`, `economics/`, `medicine/`) have been removed.**

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
│   ├── _ontology/          # Global domain taxonomy and ontology
│   │   ├── README.md              # Design documentation
│   │   ├── global-hierarchy.yaml  # Authoritative domain hierarchy
│   │   └── tools/
│   │       ├── migrate_domain.py          # Migration utility
│   │       └── validate_cross_domain.py   # Cross-domain link validator
│   │
│   ├── formal-sciences/    # Abstract sciences (mathematics, CS, logic)
│   │   └── (see "Current Hierarchy Structure" section above for details)
│   │
│   ├── natural-sciences/   # Empirical sciences (physics, chemistry, biology)
│   │   └── (see "Current Hierarchy Structure" section above for details)
│   │
│   ├── social-sciences/    # Social sciences (economics, psychology, sociology)
│   │   └── (see "Current Hierarchy Structure" section above for details)
│   │
│   └── health-sciences/    # Health sciences (medicine, nursing, pharmacy)
│       └── (see "Current Hierarchy Structure" section above for details)
│
├── renders/                 # Centralized rendered content (NEW - 2026-01-06)
│   ├── _metadata/          # Metadata and tracking
│   │   ├── README.md      # Renders documentation
│   │   └── migration-log.md # Migration history
│   ├── by-domain/          # Organized by source domain (primary organization)
│   ├── by-language/        # Organized by language
│   └── by-audience/        # Organized by target audience
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
  - `COMPLETENESS_METADATA.yaml`: Domain maturity tracking metadata (OPTIONAL but recommended)
- **Note**: Rendered content is stored in the centralized `renders/` directory

### `renders/`
Centralized repository for all rendered, human-readable content:
- **Structure**: Multiple organizational views (by-domain, by-language, by-audience)
- **Primary Organization**: `renders/by-domain/[domain-path]/[language]/[content-file]`
- **See**: `renders/README.md` for complete documentation
- **Migration**: All content migrated from domain `.renders/` subdirectories on 2026-01-06

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
- **Location**: `renders/by-domain/[domain-path]/[language]/`

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
- **Knowledge**: Language-agnostic in `.graph` files within `domain/`
- **Renderings**: Language and audience-specific in centralized `renders/` directory
- **Metadata**: Schemas and configuration separate from content
- **Infrastructure**: GitHub and project config in dotfiles

### 5. Consistent Structure
Each domain topic follows the same pattern:
```
domain/[topic]/
├── knowledge.graph
└── schema.json

renders/by-domain/[topic]/
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
4. Add renderings to `renders/by-domain/[category]/[subcategory]/[topic]/[language]/`
5. Update this structure document
6. Create domain-specific README if needed

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

**Last Updated**: 2026-01-04T18:55:00.000Z  
**Major Changes**: 
- **2026-01-04 18:50 UTC**: ✅ MIGRATION COMPLETE - All domains migrated to global hierarchy
  - Completed migration of 40 files (category theory components + math content)
  - Added 16 missing files (metadata, terminology, schema)
  - Removed 3 legacy directories (science, economics, medicine)
  - Total: 293 files processed (40 new + 253 removed duplicates)
- 2026-01-04 14:41 UTC: Added physics migration (136 AKUs → natural-sciences/physics/)
- 2026-01-04 14:41 UTC: Added economics migration (1 AKU → social-sciences/economics/)
- 2026-01-04 14:41 UTC: Added medicine migration (64 AKUs → health-sciences/medicine/)
- 2026-01-04: Added global domain hierarchy (`domain/_ontology/global-hierarchy.yaml`) with rigorous taxonomy based on UNESCO/LOC/DDC
- 2026-01-04: Added cross-domain relationship vocabulary (`domain/_contexts/cross-domain.jsonld`)
- 2026-01-04: Established native domain placement principle - category theory belongs to mathematics, not computer-science
- 2025-12-30: Added mesenteric ischemia domain with 29 AKUs and rendered book chapter (25-30 pages)
- 2025-12-30: Added prime numbers domain with 10 AKUs and cross-domain connections
- 2025-12-27: Added medicine domain with vascular surgery Type 2 endoleak (5 AKUs complete)
- 2025-12-27: Updated agent infrastructure section for .agent.md format migration
- 2025-12-26: Initial structure documentation
