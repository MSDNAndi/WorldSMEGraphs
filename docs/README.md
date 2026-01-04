# Documentation Index

> **Last Updated**: 2026-01-04T17:21:00Z

Welcome to the WorldSMEGraphs documentation! This directory contains comprehensive guides for contributors, developers, and users.

## ⭐ New Comprehensive Guides (2026-01-04)

- **[CONTENT-CREATION-GUIDE.md](CONTENT-CREATION-GUIDE.md)** - Complete content creation handbook (19KB)
  - All 6 AKU types with examples
  - Writing for 7 audience levels (toddler → professional)
  - Quality standards and workflow
  - Cross-domain linking patterns

- **[VISUALIZATION-STYLE-GUIDE.md](VISUALIZATION-STYLE-GUIDE.md)** - Visual content standards (16KB)
  - 6 visual types (diagrams, flowcharts, infographics)
  - WCAG accessibility guidelines (A, AA, AAA)
  - Color palettes and typography
  - ASCII diagram templates

- **[MULTILINGUAL-CONTENT-GUIDE.md](MULTILINGUAL-CONTENT-GUIDE.md)** - Internationalization guide (16KB)
  - Language-agnostic architecture
  - Translation standards (3 quality levels)
  - Cultural adaptation guidelines
  - Support for 10+ languages

- **[API-DOCUMENTATION-GUIDE.md](API-DOCUMENTATION-GUIDE.md)** - API design and usage (18KB)
  - Complete AKU JSON Schema (v2.0)
  - REST API and GraphQL schemas
  - Query patterns and examples
  - Python and JavaScript SDKs

- **[tutorials/PYTHON-AKU-TUTORIAL.md](tutorials/PYTHON-AKU-TUTORIAL.md)** - Python developer guide
  - Reading and creating AKUs
  - Validation and batch processing
  - Best practices and patterns

## Quick Start Guides

### For Contributors

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project
  - Code of conduct
  - Development workflow
  - Pull request process
  - Quality standards

- **[NEW-AKU-CREATION-GUIDE.md](NEW-AKU-CREATION-GUIDE.md)** - Step-by-step guide to creating new AKUs
  - AKU structure and format
  - Best practices
  - Validation requirements
  - Examples

### For Developers

- **[CI-CD.md](CI-CD.md)** - Continuous Integration and Deployment pipeline ⭐ NEW
  - Active workflows documentation
  - Validation scripts
  - Python tools with usage examples
  - Workflow development guide
  - Best practices and troubleshooting

## Specialized Guides

### Ontology Integration

The project uses standard ontologies (Schema.org, SKOS, SNOMED CT, FIBO) for knowledge representation.

- **[ONTOLOGY-QUICKSTART.md](ONTOLOGY-QUICKSTART.md)** - Quick introduction to ontology concepts
  - Why ontologies matter
  - Key concepts
  - Quick examples

- **[COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md](COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md)** - Comprehensive migration guide
  - Phase-by-phase implementation
  - Migration strategy
  - Tools and automation

- **[ONTOLOGY-TOOLS-GUIDE.md](ONTOLOGY-TOOLS-GUIDE.md)** - How to use ontology validation and migration tools
  - Validation tool usage
  - Migration tool usage
  - Troubleshooting

### Domain-Specific Guides

#### Medical Domain

- **[MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md](MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md)** - Medical knowledge annotation
  - SNOMED CT integration
  - Medical terminology standards
  - Clinical coding examples
  - Anatomical and physiological concepts

#### Economics Domain

- **[ECONOMICS-ONTOLOGY-QUICK-REFERENCE.md](ECONOMICS-ONTOLOGY-QUICK-REFERENCE.md)** - Economics knowledge annotation
  - FIBO integration
  - Financial concepts
  - Economic indicators
  - Valuation and analysis

### Visualization and Rendering

- **[VISUALIZATION-EXAMPLES.md](VISUALIZATION-EXAMPLES.md)** - Knowledge graph visualization
  - Mermaid diagrams
  - Network visualizations
  - Hierarchy trees
  - Examples from multiple domains

### Quality and Maturity

- **[knowledge-maturity-tracking.md](knowledge-maturity-tracking.md)** - Domain maturity tracking system
  - 5-level maturity framework
  - Completeness metrics
  - Quality indicators
  - Gap analysis

## Agent Documentation

The `agents/` subdirectory contains detailed documentation for specialized AI agents:

- **[agents/](agents/)** - Individual agent specifications and usage guides
  - Knowledge graph agent
  - AKU atomicity specialist
  - Domain expert templates
  - And 60+ other specialized agents

## Templates

The `templates/` subdirectory contains reusable templates for common tasks:

- AKU templates by type (definition, formula, example, theory)
- Domain structure templates
- Metadata templates
- Rendering templates

## Documentation by Task

### Creating Content

1. Start with **[CONTENT-CREATION-GUIDE.md](CONTENT-CREATION-GUIDE.md)** - comprehensive handbook ⭐ NEW
2. Review [NEW-AKU-CREATION-GUIDE.md](NEW-AKU-CREATION-GUIDE.md) for step-by-step walkthrough
3. Check domain-specific guides ([Medical](MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md) or [Economics](ECONOMICS-ONTOLOGY-QUICK-REFERENCE.md))
4. Review [MULTILINGUAL-CONTENT-GUIDE.md](MULTILINGUAL-CONTENT-GUIDE.md) for multi-language content ⭐ NEW
5. Use [VISUALIZATION-STYLE-GUIDE.md](VISUALIZATION-STYLE-GUIDE.md) for visual content ⭐ NEW
6. Use templates from `templates/` directory

### Developing with APIs

1. Read **[API-DOCUMENTATION-GUIDE.md](API-DOCUMENTATION-GUIDE.md)** for complete API reference ⭐ NEW
2. Use **[tutorials/PYTHON-AKU-TUTORIAL.md](tutorials/PYTHON-AKU-TUTORIAL.md)** for Python development ⭐ NEW
3. Check REST and GraphQL schemas
4. Review SDK examples (Python, JavaScript/TypeScript)

### Setting Up Development Environment

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Review [CI-CD.md](CI-CD.md) for workflow understanding
3. Test locally using scripts documented in CI-CD guide
4. Follow pull request guidelines

### Working with Ontologies

1. Start with [ONTOLOGY-QUICKSTART.md](ONTOLOGY-QUICKSTART.md)
2. Read domain-specific guide for your area
3. Use [ONTOLOGY-TOOLS-GUIDE.md](ONTOLOGY-TOOLS-GUIDE.md) for validation
4. Reference [COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md](COMPLETE-ONTOLOGY-MIGRATION-GUIDE.md) for migration

### Visualizing Knowledge

1. Check [VISUALIZATION-EXAMPLES.md](VISUALIZATION-EXAMPLES.md) for examples
2. Use Mermaid for diagrams
3. Follow visualization best practices

### Tracking Quality

1. Review [knowledge-maturity-tracking.md](knowledge-maturity-tracking.md)
2. Use maturity tracking tools (documented in [CI-CD.md](CI-CD.md))
3. Monitor validation rates
4. Address identified gaps

## Documentation Standards

### Markdown Style

- Use ATX-style headers (`#` not underlines)
- One blank line between sections
- Fenced code blocks with language tags
- Keep lines under 100 characters when possible

### File Naming

- Use UPPERCASE for major guides: `CONTRIBUTING.md`, `CI-CD.md`
- Use lowercase-with-hyphens for specific topics: `knowledge-maturity-tracking.md`
- Use descriptive names: `MEDICAL-ONTOLOGY-ANNOTATION-GUIDE.md` not `med-guide.md`

### Content Guidelines

- Start with purpose and audience
- Include table of contents for long documents
- Provide examples for complex concepts
- Link to related documentation
- Keep "Last Updated" timestamps current
- Use active voice and clear language

## Getting Help

1. Check documentation in this directory
2. Review [CONTRIBUTING.md](CONTRIBUTING.md) for project guidelines
3. Consult `.github/copilot-instructions.md` for Copilot usage
4. Check `.project/issues.md` for known issues
5. Contact repository maintainers

## Related Documentation

### In Repository Root

- [README.md](../README.md) - Project overview and quick start
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) - GitHub Copilot configuration
- [.github/workflows/README.md](../.github/workflows/README.md) - Workflow-specific documentation

### In Project Directory

- [.project/structure.md](../.project/structure.md) - File organization
- [.project/roadmap.md](../.project/roadmap.md) - Project roadmap
- [.project/issues.md](../.project/issues.md) - Open issues tracking
- [.project/improvements.md](../.project/improvements.md) - Enhancement ideas

## Contributing to Documentation

Documentation improvements are always welcome! When updating documentation:

1. Keep existing structure and style
2. Update "Last Updated" timestamp
3. Test all code examples
4. Check all links work
5. Update this index if adding new docs
6. Follow markdown standards above

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

**Maintained By**: Documentation Team  
**Review Schedule**: Monthly  
**Last Major Update**: 2026-01-04 (Added 5 comprehensive guides: Content Creation, Visualization, Multilingual, API, Python Tutorial)
