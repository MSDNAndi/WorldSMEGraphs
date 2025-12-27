# WorldSMEGraphs

> A file-based, language-agnostic knowledge representation system for subject matter expert domains

## Overview

WorldSMEGraphs is a comprehensive system for creating, storing, and rendering interconnected knowledge graphs across multiple subject matter expert domains. The system enables:

- **Language-Agnostic Knowledge Representation**: Core knowledge stored independent of natural language
- **Multi-Audience Rendering**: Generate content for audiences from toddlers to graduate students
- **Multi-Lingual Support**: Render the same knowledge in any language
- **Multiple Output Formats**: Markdown, PDF, LaTeX, DOCX, and more
- **Cross-Domain Linking**: Connect related concepts across different subject areas
- **File-Based Architecture**: Everything in version control, no external databases needed

## Quick Start

### Understanding the Structure

```
domain/
├── science/
│   └── math/
│       └── algebra/
│           ├── knowledge.graph        # Language-agnostic representation
│           └── .renders/             # Human-readable versions
│               ├── english/
│               │   ├── elementary-school.md
│               │   ├── graduate.md
│               │   └── 4-year-old.md
│               └── german/
│                   └── grundschule.md
└── economics/
    └── macroeconomics/
        └── ...
```

### Core Concepts

1. **Knowledge Graphs**: Language-agnostic representations of domain knowledge in `knowledge.graph` files
2. **Renderings**: Human-readable versions tailored for specific languages and audiences
3. **Cross-Links**: Connections between related concepts across domains
4. **Domains**: Hierarchical organization by subject matter (science, economics, etc.)

## Features

### 🌐 Language-Agnostic Core
Knowledge is stored in a structured, language-independent format that can be rendered into any natural language without modifying the source.

### 👥 Audience-Adaptive Content
Generate appropriate content for:
- Toddlers (2-3 years)
- Young children (4 years)
- Elementary school students
- Middle school students
- High school students
- Adults (general and limited reading)
- Graduate students and experts

### 🔗 Interconnected Knowledge
Create unidirectional or bidirectional links between concepts, enabling:
- Prerequisite relationships
- Specialization hierarchies
- Cross-domain connections
- Analogies between fields

### 📊 Multiple Output Formats
Generate content in:
- **Markdown** for web and documentation
- **PDF** for print and distribution
- **LaTeX/TeX** for academic publishing
- **DOCX** for collaborative editing
- **HTML** for interactive applications

### 🤖 AI-Powered Agents
60 specialized GitHub Copilot agents in `.github/agents/`:
- **Core Infrastructure**: Coordinator, Recruiter (format gatekeeper), Quality
- **Content Creation**: Parsers, miners, extractors for textbooks, papers, videos
- **Knowledge Organization**: Ontology, semantic harmonization, terminology
- **Quality Assurance**: Validation, verification, peer review
- **Rendering & Presentation**: Multi-audience rendering, visualization, accessibility
- **Pedagogy & Learning**: Learning design, assessment creation
- **Domain Expertise**: Generic domain empathy, math expert, legal, standards
- And 40+ more specialized agents

## Project Structure

See [Project Structure Documentation](.project/structure.md) for complete details.

```
.
├── .github/
│   ├── agents/                # 60 Copilot custom agents (.agent.md)
│   ├── copilot/              # Copilot configuration
│   └── copilot-instructions.md
├── .project/
│   ├── structure.md          # Project organization
│   ├── roadmap.md           # Development roadmap
│   ├── knowledge-format.md   # Graph format spec
│   └── rendering-spec.md     # Rendering system spec
├── domain/                   # Knowledge domain hierarchies
│   ├── science/
│   ├── economics/
│   └── [other domains]/
└── docs/                     # General documentation
```

## Getting Started

### For Contributors

1. **Read the Documentation**
   - [Contributing Guidelines](docs/CONTRIBUTING.md)
   - [Project Structure](.project/structure.md)
   - [Knowledge Format Specification](.project/knowledge-format.md)
   - [Rendering Specification](.project/rendering-spec.md)

2. **Understand the Agents**
   - Review [Copilot Instructions](.github/copilot-instructions.md)
   - Check available [Agent Configurations](.github/copilot/agents/)

3. **Choose Your Contribution**
   - Create new knowledge graphs
   - Add renderings for existing graphs
   - Translate to new languages
   - Improve documentation
   - Enhance tooling

### For Users

1. **Browse Domains**: Navigate the `domain/` directory to find topics of interest
2. **Select Rendering**: Choose a rendering appropriate for your audience and language
3. **Follow Cross-Links**: Explore related concepts across domains
4. **Suggest Improvements**: Open issues for corrections or enhancements

## Key Documents

### For Understanding the System
- **[Copilot Instructions](.github/copilot-instructions.md)**: How AI agents work with this project
- **[Project Structure](.project/structure.md)**: Organization and file layout
- **[Roadmap](.project/roadmap.md)**: Project goals and timeline

### For Technical Details
- **[Knowledge Format](.project/knowledge-format.md)**: How knowledge graphs are structured
- **[Rendering Specification](.project/rendering-spec.md)**: How renderings are generated
- **[Ontology Integration](docs/ONTOLOGY-QUICKSTART.md)**: Quick start guide for using standard ontologies (NEW!)
- **[Ontology Specification](.project/research/ontology-integration-specification.md)**: Complete technical specification

### For Contributors
- **[Contributing Guidelines](docs/CONTRIBUTING.md)**: How to contribute
- **[Ontology Quick Start](docs/ONTOLOGY-QUICKSTART.md)**: How to use SKOS, SNOMED, FIBO and other ontologies
- **[Agent Configurations](.github/copilot/agents/)**: Specialized agent instructions
- **[Agent KPIs](.github/copilot/agent-kpis.md)**: Agent performance tracking

## Architecture

### Knowledge Representation
Knowledge is stored in JSON-based `knowledge.graph` files with:
- **Nodes**: Concepts, operations, properties, examples
- **Edges**: Relationships between nodes (contains, requires, uses, etc.)
- **Cross-Links**: References to concepts in other domains
- **Metadata**: Domain, versioning, authors, tags

### Rendering System
The rendering engine:
1. Parses knowledge graphs
2. Selects appropriate templates
3. Maps UIDs to localized content
4. Generates human-readable text
5. Formats for output medium
6. Validates quality

### Agent System
Specialized AI agents handle:
- **Knowledge Graph Agent**: Creates and maintains graphs
- **Documentation Agent**: Manages documentation
- **Code Review Agent**: Ensures quality
- **Contrarian Agent**: Provides critical feedback
- **Rendering Agent**: Generates human-readable content
- **Domain Experts**: Validate subject-specific accuracy

## Current Status

**Phase**: Foundation (In Progress)

### Completed ✅
- Agent infrastructure setup
- Project structure definition
- Knowledge format specification
- Rendering system specification
- Core documentation

### In Progress 🚧
- Pilot domain implementation
- Rendering automation
- Quality validation tools

### Planned 📋
- Multi-domain expansion
- Visualization tools
- API development
- Community building

See the [Roadmap](.project/roadmap.md) for details.

## Examples

### Knowledge Graph (Simplified)
```json
{
  "nodes": {
    "n1": {
      "type": "concept",
      "uid": "algebra:variable",
      "properties": {"abstract": true}
    }
  },
  "edges": [
    {
      "from": "n2",
      "to": "n1",
      "type": "contains"
    }
  ]
}
```

### Rendering (Elementary School)
```markdown
# Variables

A variable is like a box that can hold different numbers.
We use letters like x, y, or z for variables.

Example: If x = 5, then x + 3 = 8
```

### Rendering (Graduate)
```markdown
# Algebraic Variables

A variable is a symbolic representation of an element in a mathematical
set, typically denoted by letters from the Latin or Greek alphabets.
Variables serve as placeholders in algebraic expressions and equations...
```

## Technology

- **Storage**: File-based (JSON, Markdown)
- **Version Control**: Git
- **AI Agents**: GitHub Copilot
- **Rendering**: Pandoc, LaTeX, Markdown
- **Validation**: JSON Schema, readability metrics

## Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for:
- How to create knowledge graphs
- Rendering guidelines
- Coding standards
- Review process
- Community guidelines

## License

[To be determined]

## Contact

[To be determined]

## Acknowledgments

Inspired by best practices in:
- Knowledge representation systems
- Semantic web technologies
- Educational content design
- Multi-lingual documentation
- AI-assisted development

---

**Note**: This project is in active development. Structure and specifications may evolve based on implementation experience.
