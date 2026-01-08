# Changelog

All notable changes to the WorldSMEGraphs project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Image Generation Workflow Enforcement** (2026-01-08) - v0.3.1
  - Comprehensive workflow enforcement system (64KB documentation + 29KB code)
  - Documentation:
    - `WORKFLOW-ENFORCEMENT.md` (20KB) - Complete phase-by-phase guide
    - `QUICK-START.md` (16KB) - Step-by-step tutorial
    - `tools/README.md` - Updated with workflow tools reference
  - Validation tools:
    - `validate_workflow.py` (13KB) - Phase order validation
    - `validate_prompts.py` (15KB) - Prompt quality checking
    - `workflow_constants.py` (1KB) - Shared validation constants
    - `pre-commit-hook.sh` (5KB) - Git hook enforcement
  - Generator updates with blocking validation:
    - `presentation_generator.py` - validate_images_exist() function
    - `build_gpt_pdf.py` - Workflow enforcement
  - Example project: Category Theory presentation storyboard
  - Enforces correct order: Storyboard → Prompts → Images → Documents
  - Ensures complete prompts (8K-20K chars, no placeholders)
  - Based on lessons learned from PR #36 and PR #38
- **Centralized Renders Infrastructure** (2026-01-06)
  - New `renders/` directory at repository root
  - `renders/by-domain/` organization (255 files)
  - `renders/_metadata/` with comprehensive documentation (75KB+)
  - Automation tools:
    - `generate_render_index.py` - Renders cataloging
    - `generate_aku_usage_matrix.py` - AKU-render tracking (658 AKUs)
    - `render_quality_linter.py` - Quality validation (8 checks)
    - `create_render.sh` - Interactive render creation
  - CI/CD validation workflow (`.github/workflows/validate-renders.yml`)
  - Audience profiles (8 definitions with guidelines)
  - Developer guide (13KB comprehensive reference)
  - Migration log and validation reports
  - Project completion summary
- Comprehensive domain migration guide (`.project/docs/domain-migration-guide.md`)
- Ontology tools README documentation (`domain/_ontology/tools/README.md`)
- Post-migration validation report (`.project/tracking/post-migration-validation-report.md`)
- Session work summary template (`.project/tracking/session-work-summary-2026-01-04.md`)

### Changed
- **Image Generation Agent** - Updated to v3.0 with workflow enforcement capabilities
- **Project Documentation** - Updated README.md to v0.3.1, added workflow links
- **Structure Documentation** - Added image generation workflow section
- **Improvements Tracking** - Added IMP-010 (completed), IMP-011/012 (proposed)
- **Renders Migration** - Extracted all `.renders/` content to centralized `renders/`
  - Updated 23 documentation files with new render paths
  - Updated 4 agent configurations
  - Updated rendering specification workflows
  - Updated examples in all guides
- Updated all path references from old to new hierarchy across codebase
- Enhanced `validate_aku_v2.py` to recognize new domain paths
- Updated agent file examples to use new hierarchy paths
- Updated CONTRIBUTING.md examples with new paths

### Removed
- All `.renders/` subdirectories from domain hierarchy (6 directories)
- Legacy render path references in documentation

### Fixed
- **Code Review Issues** (2026-01-08):
  - Consolidated placeholder keywords into shared constants
  - Improved docstrings explaining blocking behavior
  - Eliminated code duplication between validators
- Completed incomplete PR #30 migration
- Removed duplicate content (293 files from old locations)
- Fixed inconsistent path references in documentation

## [0.2.0] - 2026-01-04

### Added
- **Global Domain Hierarchy** - Ontologically rigorous taxonomy
  - 4 top-level domains: formal-sciences, natural-sciences, social-sciences, health-sciences
  - Based on UNESCO/LOC/DDC/MSC/ACM standards
  - Native domain placement principle established
  - Cross-domain linking patterns defined
- **Migration Tools**
  - `migrate_domain.py` - General migration script
  - `migrate_category_theory.py` - Category theory specialist
  - `update_fp_cross_domain.py` - Functional programming linker
  - `validate_cross_domain.py` - Cross-domain validator
- **Domain Content**
  - Category theory (27 AKUs): category-theory, functors, monads, monoids
  - Mathematics (21 AKUs): geometry, number-theory
  - Physics (138 AKUs): atomic, quantum, cosmology, relativity
  - Medicine (68 AKUs): vascular surgery, mesenteric ischemia
  - Economics (12 AKUs): BWL, finance, NPV
- **Documentation**
  - Domain READMEs for all 4 top-level domains
  - Migration completion report
  - Validation report
  - Structure documentation updates

### Changed
- **Migrated 266 AKUs** to new hierarchy (100% success rate)
- Reorganized all domain content per global hierarchy
- Updated classification.domain_path in all AKUs
- Enhanced validators for new domain structure

### Removed
- Old domain directories: `domain/science/`, `domain/economics/`, `domain/medicine/`
- 293 duplicate files from legacy locations
- Outdated path references (90,729 lines removed)

### Fixed
- Domain organizational compliance with international standards
- Cross-domain linking patterns (native vs application domains)
- Validator domain recognition for new hierarchy
- Path consistency across all documentation

## [0.1.0] - 2025-12-27

### Added
- **Agent Infrastructure**
  - 61 specialized GitHub Copilot agents
  - `.agent.md` format standard (180-line minimum)
  - Agent performance tracking (KPIs)
  - Recruiter agent as format gatekeeper
- **Project Structure**
  - `.project/` metadata directory
  - `domain/` knowledge hierarchy
  - `docs/` general documentation
  - `.github/agents/` agent definitions
- **Knowledge Format**
  - AKU (Atomic Knowledge Unit) specification
  - JSON-LD contexts (base, medicine, economics, science)
  - SKOS integration framework
  - Rendering system specification
- **Quality Assurance**
  - AKU validators (v1 and v2)
  - Relationship visualizer
  - Maturity tracking system
  - Code review processes
- **Initial Content**
  - Medicine: Vascular surgery, Type 2 endoleak (5 AKUs)
  - Medicine: Mesenteric ischemia (29 AKUs)
  - Mathematics: Prime numbers (10 AKUs)
  - Physics: Planck units (extensive)
  - Economics: NPV pilot content

### Documentation
- Project README with vision and structure
- CONTRIBUTING guide for contributors
- Getting started guide
- Agent KPI tracking documentation
- Knowledge format specification
- Rendering specification

## [0.0.1] - 2025-12-26

### Added
- Initial project setup
- Basic repository structure
- Core documentation framework
- GitHub Copilot integration setup

---

## Release Notes

### Version 0.2.0 Highlights

**Major Milestone**: Complete alignment with global domain hierarchy

This release represents a significant architectural improvement, transitioning from a simple flat structure to an ontologically rigorous hierarchical taxonomy based on international academic standards. All 266 AKUs have been successfully migrated with zero data loss, and the project now follows professional knowledge organization principles.

**Key Achievements**:
- ✅ 100% migration success rate (266 AKUs)
- ✅ Zero data loss
- ✅ Removed 90,729 lines of duplicate content
- ✅ 14 commits with comprehensive documentation
- ✅ All validators updated and functional
- ✅ Complete documentation coverage

**Impact**: The project is now positioned for scalable growth with a solid organizational foundation that supports cross-domain knowledge linking and multi-lingual, multi-audience rendering.

### Version 0.1.0 Highlights

**Foundation Phase**: Established core infrastructure

This release established the foundational infrastructure for WorldSMEGraphs, including the agent system, quality assurance processes, and initial pilot content across multiple domains.

**Key Features**:
- 61 specialized AI agents for content creation and review
- Comprehensive validation and quality assurance tools
- Initial multi-domain content (medicine, mathematics, physics, economics)
- Knowledge format specification with JSON-LD and SKOS integration

---

## Versioning Strategy

- **Major version** (X.0.0): Significant architectural changes, breaking changes
- **Minor version** (0.X.0): New features, content additions, non-breaking changes
- **Patch version** (0.0.X): Bug fixes, documentation updates, minor corrections

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on how to contribute to this project.

## License

[License information to be added]

---

**Maintained By**: WorldSMEGraphs Core Team  
**Last Updated**: 2026-01-04
