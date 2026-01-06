# Renders Directory

This directory contains all rendered, human-readable content generated from the knowledge graphs in the `domain/` directory.

## Purpose

The `renders/` directory centralizes all rendered content that was previously distributed in `.renders/` subdirectories throughout the domain hierarchy. This refactoring enables:

- **Centralized Management**: All rendered content in one location
- **Multi-domain Content**: Easier to create content that spans multiple domains
- **Better Tracking**: Clear references between AKUs and their renderings
- **Flexible Organization**: Multiple views of the same content (by domain, language, audience, format)

## Structure

```
renders/
├── _metadata/                  # Metadata and tracking information
│   ├── README.md              # This file
│   ├── render-index.yaml      # Master index of all renders
│   └── migration-log.md       # History of content migration
│
├── by-domain/                 # Organized by source domain
│   ├── formal-sciences/
│   ├── natural-sciences/
│   ├── social-sciences/
│   └── health-sciences/
│
├── by-language/               # Organized by language
│   ├── english/
│   ├── german/
│   └── [other languages]/
│
└── by-audience/               # Organized by target audience
    ├── elementary-school/
    ├── graduate/
    ├── adult-limited-reading/
    └── [other audiences]/
```

## Organization Principles

### By Domain
Maintains the domain hierarchy structure for easy navigation from source AKUs to their renders.

Path format: `renders/by-domain/[domain-path]/[language]/[content-file]`

Example: `renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/adult-limited-reading.md`

### By Language
Groups all content by language for localization and translation workflows.

Path format: `renders/by-language/[language]/[domain-path]/[content-file]`

Example: `renders/by-language/english/natural-sciences/physics/quantum-mechanics/planck-units/adult-limited-reading.md`

### By Audience
Groups content by target audience level for curriculum development.

Path format: `renders/by-audience/[audience]/[domain]/[content-file]`

Example: `renders/by-audience/adult-limited-reading/physics/planck-units.md`

## Migration from .renders/

All content from `domain/**/.renders/` directories has been migrated to this centralized structure. The primary organization is **by-domain** to maintain the connection to source AKUs.

See `_metadata/migration-log.md` for details of the migration.

## Adding New Renders

When creating new rendered content:

1. **Primary Location**: Place in `renders/by-domain/[domain-path]/[language]/`
2. **Naming**: Use descriptive names indicating audience level or purpose
3. **Metadata**: Consider adding YAML frontmatter with:
   - Source AKU references
   - Target audience
   - Language
   - Last updated timestamp
4. **Cross-references**: Update AKU files if needed to reference the render

## Relationship to Domain Structure

- **Domain AKUs**: Remain in `domain/` hierarchy (NOT touched by this refactoring)
- **Rendered Content**: Now in `renders/` hierarchy (moved from `.renders/` subdirectories)
- **References**: AKUs may reference their renders; renders should reference source AKUs

## See Also

- `.project/rendering-spec.md` - Rendering system specification
- `.project/proposals/rendering-architecture-v2.md` - Architecture proposal
- `domain/_ontology/global-hierarchy.yaml` - Domain taxonomy

---

**Created**: 2026-01-06
**Migration Date**: 2026-01-06
**Status**: Active
