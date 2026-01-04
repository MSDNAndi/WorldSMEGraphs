# Domain Directory

> **Purpose**: Root directory for all subject matter expert knowledge domains
> **Last Updated**: 2026-01-04

## Overview
This directory contains hierarchically organized knowledge graphs for various subject matter expert domains. Each domain follows a consistent structure to enable cross-linking and systematic knowledge representation.

## 🆕 Global Domain Hierarchy

The authoritative domain taxonomy is defined in [`_ontology/global-hierarchy.yaml`](_ontology/global-hierarchy.yaml).

**Key Principles**:
1. **Native Domain Placement**: Concepts belong to their ORIGIN domain, not application domains
2. **Single Source of Truth**: AKUs created only in native domain; others link to them
3. **Cross-Domain Linking**: Applications reference native concepts, don't copy them

**Top-Level Domains**:
- `formal-sciences/` - Mathematics, Computer Science, Logic
- `natural-sciences/` - Physics, Chemistry, Biology, Earth Sciences
- `social-sciences/` - Economics, Psychology, Sociology
- `health-sciences/` - Medicine, Nursing, Pharmacy
- `engineering/` - Mechanical, Electrical, Civil
- `humanities/` - Philosophy, History, Linguistics
- `arts/` - Visual Arts, Music, Design
- `interdisciplinary/` - Cognitive Science, Data Science

See [`_ontology/README.md`](_ontology/README.md) for design documentation.

## Domain Organization

### Hierarchical Structure
```
domain/
├── _ontology/            # Global domain taxonomy (NEW)
│   ├── global-hierarchy.yaml  # Authoritative hierarchy
│   ├── README.md              # Design documentation
│   ├── examples/              # Cross-domain linking examples
│   └── tools/                 # Validation tools
├── _contexts/            # JSON-LD context files
│   ├── base.jsonld           # Core vocabulary
│   ├── cross-domain.jsonld   # Cross-domain vocabulary (NEW)
│   └── [domain].jsonld       # Domain-specific vocabularies
├── [category]/           # Major category (science, economics, etc.)
│   ├── [discipline]/     # Specific discipline within category
│   │   ├── [topic]/      # Specific topic within discipline
│   │   │   ├── knowledge.graph      # Core knowledge representation
│   │   │   ├── schema.json          # Schema definition
│   │   │   ├── README.md            # Topic documentation
│   │   │   └── .renders/            # Human-readable renderings
│   │   │       └── [language]/[audience].[format]
│   │   └── README.md     # Discipline documentation
│   └── README.md         # Category documentation
└── README.md             # This file
```

## Current Domains

### Science
**Status**: Planned  
**Subdisciplines**: Mathematics, Physics, Chemistry, Biology

**Priority Topics**:
- Mathematics: Algebra, Geometry, Calculus
- Physics: Mechanics, Thermodynamics, Electromagnetism
- Chemistry: Atomic Structure, Chemical Bonding, Reactions
- Biology: Cell Biology, Genetics, Evolution

### Economics  
**Status**: Planned  
**Subdisciplines**: Macroeconomics, Microeconomics, Behavioral Economics

**Priority Topics**:
- Macroeconomics: GDP, Inflation, Monetary Policy
- Microeconomics: Supply & Demand, Market Structures
- Behavioral Economics: Decision Making, Cognitive Biases

### Humanities
**Status**: Future  
**Subdisciplines**: History, Philosophy, Literature

### Technology
**Status**: Future  
**Subdisciplines**: Computer Science, Engineering

## Creating a New Domain

### 1. Determine Hierarchy
Identify where the domain fits:
- Major category (science, economics, etc.)
- Discipline within category
- Topic within discipline

### 2. Create Directory Structure
```bash
mkdir -p domain/[category]/[discipline]/[topic]
mkdir -p domain/[category]/[discipline]/[topic]/.renders
```

### 3. Create Core Files

#### knowledge.graph
Language-agnostic knowledge representation. See [Knowledge Format Specification](../.project/knowledge-format.md).

#### schema.json
Schema definition for the knowledge graph.

#### README.md (optional)
Domain-specific documentation, guidelines, or notes.

### 4. Add Initial Renderings
Create at least one rendering to validate the knowledge graph.

```bash
mkdir -p domain/[category]/[discipline]/[topic]/.renders/english
# Create rendering file
```

### 5. Update Documentation
- Add domain to this README
- Update project structure documentation
- Create category/discipline READMEs if needed

## Domain Guidelines

### Naming Conventions
- Use lowercase for directory names
- Use hyphens for multi-word names
- Be descriptive but concise
- Follow hierarchy: broad → specific

Examples:
- `science/math/algebra`
- `economics/macroeconomics/monetary-policy`
- `science/physics/classical-mechanics`

### Knowledge Graph Requirements
Each topic must have:
1. Valid `knowledge.graph` file
2. Corresponding `schema.json`
3. At least one rendering
4. Cross-links to related topics (when applicable)

### Cross-Linking Guidelines
- Link to prerequisite topics
- Connect related concepts across domains
- Establish hierarchical relationships
- Document bidirectional links appropriately

### Quality Standards
- **Accuracy**: Factually correct information
- **Completeness**: All key concepts covered
- **Consistency**: No contradictions with other domains
- **Clarity**: Clear relationships and structure
- **Maintainability**: Easy to update and extend

## Domain Status Tracking

### Completed Domains
*None yet - project in foundation phase*

### In Progress
*None yet*

### Planned
- science/math/algebra
- economics/macroeconomics

### Future Considerations
- humanities/history
- technology/computer-science
- arts/music-theory
- social-sciences/psychology

## Contributing to Domains

### Process
1. Choose a domain to develop
2. Research thoroughly using authoritative sources
3. Design knowledge graph structure
4. Create `knowledge.graph` and `schema.json`
5. Add initial renderings
6. Validate with domain experts
7. Submit for review

### Required Expertise
- Subject matter expertise in the domain
- Understanding of knowledge representation
- Ability to identify key concepts and relationships
- Writing skills for renderings

### Review Process
1. Technical review (format compliance)
2. Domain expert review (accuracy)
3. Cross-link validation
4. Documentation review
5. Final approval

## Domain Maintenance

### Regular Updates
- Incorporate new research/discoveries
- Fix inaccuracies
- Add new renderings
- Update cross-links
- Improve clarity

### Version Control
All changes tracked in Git:
- Clear commit messages
- Reference sources for factual updates
- Document breaking changes
- Tag major versions

### Quality Monitoring
- Regular accuracy reviews
- User feedback incorporation
- Cross-link validation
- Consistency checks

## Cross-Domain Collaboration

### Coordination
When domains intersect:
1. Establish clear cross-links
2. Coordinate with other domain maintainers
3. Ensure consistent terminology
4. Document relationships

### Example Intersections
- Math & Physics: Mathematical models in physics
- Economics & Math: Mathematical economics
- Biology & Chemistry: Biochemistry
- Psychology & Economics: Behavioral economics

## Tools and Automation

### Planned Tools
- Knowledge graph validator
- Rendering generator
- Cross-link checker
- Quality metrics calculator
- Domain visualizer

### Current Status
All tools are planned for future development.

## Getting Help

### For Domain Creation
- Review [Knowledge Format Specification](../.project/knowledge-format.md)
- Study existing domain examples
- Consult @knowledge-graph-agent
- Request domain expert review

### For Technical Issues
- Check [Project Structure](../.project/structure.md)
- Review [Contributing Guidelines](../docs/CONTRIBUTING.md)
- Use @file-organization-agent for structure questions
- Open an issue for persistent problems

## Related Documents
- [Knowledge Format Specification](../.project/knowledge-format.md)
- [Rendering Specification](../.project/rendering-spec.md)
- [Project Structure](../.project/structure.md)
- [Contributing Guidelines](../docs/CONTRIBUTING.md)

---

**Status**: This is a living document. Update it as domains are added or guidelines evolve.
