# Ontology and Domain Hierarchy - Glossary

**Purpose**: Comprehensive glossary of terms used throughout the WorldSMEGraphs ontology and domain hierarchy documentation.

---

## Core Concepts

### AKU (Atomic Knowledge Unit)
A self-contained, language-agnostic unit of knowledge representing a single concept, formula, definition, or principle. AKUs are the fundamental building blocks of the knowledge graph.

### Native Domain
The academic or scientific field where a concept originated and is fundamentally defined. For example, category theory's native domain is mathematics, even though it's applied in computer science.

### Application Domain
A field that applies concepts from other native domains. For example, functional programming (computer science) applies category theory (mathematics).

### Cross-Domain Reference
A structured link from an application domain AKU to a native domain AKU, documenting how the native concept is applied in the application context.

### Domain Path
A hierarchical identifier specifying an AKU's location in the knowledge taxonomy (e.g., `formal-sciences/mathematics/pure-mathematics/category-theory`).

---

## Domain Classifications

### Formal Sciences
Academic disciplines that study abstract structures and logical systems. Includes mathematics, logic, computer science theory, statistics, and information theory.

### Natural Sciences
Empirical sciences studying natural phenomena through observation and experiment. Includes physics, chemistry, biology, earth sciences, and astronomy.

### Social Sciences
Disciplines studying human behavior, societies, and social relationships. Includes economics, sociology, psychology, political science, and anthropology.

### Health Sciences
Applied sciences focused on health, medicine, and healthcare. Includes medicine, nursing, public health, pharmacy, and medical technology.

---

## Ontological Principles

### Ontological Rigor
The discipline of placing concepts in their proper categorical location based on fundamental nature rather than practical application.

### Single Source of Truth
Each concept should have exactly one authoritative definition in its native domain, with all other references linking back to it.

### Hierarchical Organization
Knowledge organized in taxonomic hierarchies from general domains to specific subdomains and individual concepts.

---

## Migration Terms

### Legacy Structure
The previous organization where concepts were placed by application usage (e.g., category theory under computer-science).

### New Hierarchy
The ontologically-rigorous organization where concepts are placed in their native domains (e.g., category theory under mathematics).

### Migration Success Rate
Percentage of AKUs successfully migrated with all required fields updated correctly.

### Cross-Domain Migration
The process of updating application domain AKUs to reference native domain concepts after migration.

---

## Technical Terms

### @id Field
A unique identifier for an AKU in JSON-LD format (e.g., `aku:math:category-theory:monad`).

### domain_path Field
Classification field specifying an AKU's location in the hierarchy (e.g., `formal-sciences/mathematics/pure-mathematics/category-theory`).

### isNativeDomain
Boolean flag indicating whether an AKU belongs to a concept's native domain (true) or application domain (false).

### isApplicationDomain
Boolean flag indicating whether an AKU represents an application of concepts from other domains.

### cross_domain_applications
Array documenting how a native domain concept is applied in other fields.

### cross_domain_references
Structured links from application domains to native domain definitions.

---

## Standards and Taxonomies

### UNESCO Classification
International Standard Nomenclature for Fields of Science and Technology used as reference for domain organization.

### Library of Congress (LOC)
Classification system used for organizing knowledge domains.

### Dewey Decimal Classification (DDC)
Library classification system providing hierarchical domain structure.

### ISO Standards
International standards relevant to domain-specific content (e.g., ISO 80000 for physics).

---

## Validation Terms

### AKU Validation
Process of checking AKUs for required fields, correct structure, and proper formatting.

### Cross-Domain Validation
Verification that cross-domain references point to valid native domain AKUs.

### Schema Compliance
Ensuring AKUs conform to the defined JSON schema for their content type.

---

## Documentation Terms

### Render
A human-readable representation of knowledge graph content, typically in markdown, PDF, or presentation format.

### Visual Guide
Educational documentation with diagrams, flowcharts, and visual explanations.

### Migration Checklist
Step-by-step procedure for migrating content from legacy to new hierarchy.

### Troubleshooting Guide
Documentation of common issues and their solutions.

---

## Project Management

### Phase
A major stage in project development (e.g., Phase 1: Foundation, Phase 2: Content Creation).

### Milestone
A significant achievement or completion point in the project timeline.

### KPI (Key Performance Indicator)
Measurable metric used to evaluate project success (e.g., validation pass rate, migration success rate).

---

## Content Types

### Definition AKU
An AKU that defines a concept or term.

### Formula AKU
An AKU containing a mathematical or scientific formula.

### Example AKU
An AKU providing a practical example or application of a concept.

### Relationship AKU
An AKU documenting connections between concepts.

---

## Quality Metrics

### Validation Pass Rate
Percentage of AKUs that pass all validation checks.

### Documentation Coverage
Extent to which all aspects of the system are documented.

### Cross-Reference Integrity
Measure of whether all cross-domain references point to valid targets.

---

## Related Resources

- **Global Hierarchy**: `domain/_ontology/global-hierarchy.yaml`
- **Migration Guide**: `domain/_ontology/MIGRATION-GUIDE.md`
- **FAQ**: `domain/_ontology/FAQ.md`
- **Index**: `domain/_ontology/INDEX.md`

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintained By**: WorldSMEGraphs Project Team
