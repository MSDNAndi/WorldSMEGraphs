# Contributing to WorldSMEGraphs

Thank you for your interest in contributing to WorldSMEGraphs! This guide will help you get started.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Creating Knowledge Graphs](#creating-knowledge-graphs)
- [Creating Renderings](#creating-renderings)
- [Code Review Process](#code-review-process)
- [Style Guidelines](#style-guidelines)
- [Agent Collaboration](#agent-collaboration)

## Code of Conduct

### Our Standards
- Be respectful and inclusive
- Focus on what's best for the project
- Accept constructive criticism gracefully
- Show empathy towards others
- Collaborate openly

### Unacceptable Behavior
- Harassment or discriminatory language
- Personal attacks
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## How Can I Contribute?

### 1. Create Knowledge Graphs
Design and implement language-agnostic knowledge graphs for new domains or topics.

**Skills Needed**: Subject matter expertise, understanding of knowledge representation

**See**: [Knowledge Format Specification](../.project/knowledge-format.md)

### 2. Add Renderings
Generate human-readable content from existing knowledge graphs for different audiences and languages.

**Skills Needed**: Writing, translation, educational content design

**See**: [Rendering Specification](../.project/rendering-spec.md)

### 3. Improve Documentation
Enhance project documentation, fix errors, add examples, or improve clarity.

**Skills Needed**: Technical writing, clarity of communication

### 4. Develop Tooling
Create tools for graph validation, rendering automation, or quality assurance.

**Skills Needed**: Programming, software development

### 5. Review Content
Validate accuracy, appropriateness, and quality of knowledge graphs and renderings.

**Skills Needed**: Subject expertise, attention to detail

### 6. Translate Content
Translate renderings into new languages or improve existing translations.

**Skills Needed**: Multi-lingual proficiency, cultural awareness

## Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/MSDNAndi/WorldSMEGraphs.git
cd WorldSMEGraphs
```

### 2. Read Key Documentation
- [README.md](../README.md)
- [Project Structure](../.project/structure.md)
- [Copilot Instructions](../.github/copilot-instructions.md)
- [Knowledge Format](../.project/knowledge-format.md)
- [Rendering Spec](../.project/rendering-spec.md)

### 3. Explore Existing Content
Browse `domain/` directory to understand existing knowledge graphs and renderings.

### 4. Choose a Task
- Check open issues
- Review the [Roadmap](../.project/roadmap.md)
- Propose new domains or improvements

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

Use branch naming convention:
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `refactor/` for code improvements

### 2. Make Changes
Follow the guidelines for your type of contribution (see below).

### 3. Self-Review
- Run validation checks
- Review your changes
- Ensure consistency with existing content
- Check for redundancies

### 4. Request Agent Review
Use specialized agents for review:
```
@code-review-agent Review my changes to ensure quality
@documentation-agent Check for contradictions with existing docs
@contrarian-agent Challenge my approach and identify weaknesses
```

### 5. Commit Changes
```bash
git add .
git commit -m "Brief description of changes"
```

**Commit Message Guidelines**:
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Provide detailed description in body if needed
- Reference issue numbers when applicable

### 6. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Create a pull request with:
- Clear title and description
- Reference to related issues
- Summary of changes
- Any special considerations

## Creating Knowledge Graphs

### Process

1. **Research the Domain**
   - Gather authoritative sources
   - Identify core concepts
   - Understand relationships
   - Note prerequisites

2. **Design the Graph Structure**
   - List main concepts (nodes)
   - Define relationships (edges)
   - Identify cross-links to other domains
   - Plan hierarchies

3. **Create the Files**

Create directory:
```bash
mkdir -p domain/[category]/[subcategory]/[topic]
```

Create `knowledge.graph`:
```json
{
  "version": "1.0",
  "domain": "[category]/[subcategory]/[topic]",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "metadata": {
    "title": "Topic Title",
    "description": "Brief description",
    "authors": ["your-id"],
    "tags": ["tag1", "tag2"]
  },
  "nodes": { ... },
  "edges": [ ... ],
  "cross_links": [ ... ]
}
```

Create `schema.json`:
```json
{
  "version": "1.0",
  "graph": "knowledge.graph",
  "node_types": ["concept", "operation", "property"],
  "edge_types": ["contains", "requires", "uses"]
}
```

4. **Validate**
   - All nodes referenced in edges exist
   - UIDs follow naming conventions
   - Cross-links target valid domains
   - Schema matches graph structure

5. **Document**
   - Add README in domain directory if needed
   - Update project structure documentation
   - Note any design decisions

### Quality Criteria

- **Completeness**: All key concepts covered
- **Accuracy**: Factually correct
- **Consistency**: No contradictions
- **Clarity**: Clear relationships
- **Linkability**: Cross-links where appropriate

## Creating Renderings

### Process

1. **Select Source Graph**
   - Choose existing `knowledge.graph`
   - Understand its structure
   - Review schema and metadata

2. **Choose Target Audience and Language**
   - Identify audience level
   - Select language
   - Review audience guidelines in [Rendering Spec](../.project/rendering-spec.md)

3. **Create Rendering File**

Path: `domain/[...]/[topic]/.renders/[language]/[audience].[format]`

Example: `domain/formal-sciences/mathematics/pure-mathematics/algebra/.renders/english/elementary-school.md`

4. **Write Content**

Use template structure:
```markdown
---
source: [graph-path]
language: english
audience: elementary-school
version: 1.0
generated: 2025-12-26
---

# [Title]

[Introduction]

## [Concept 1]
[Explanation]

### Examples
[Examples]

## Related Topics
- [Cross-links]
```

5. **Match Audience Level**
   - Use appropriate vocabulary
   - Adjust complexity
   - Include relevant examples
   - Follow guidelines for target audience

6. **Validate**
   - Check readability score
   - Verify all UIDs from graph are covered
   - Test cross-links
   - Review for accuracy

### Quality Criteria

- **Accuracy**: Matches source graph
- **Appropriateness**: Fits audience level
- **Clarity**: Easy to understand
- **Completeness**: No key concepts missing
- **Consistency**: Uniform style

## Code Review Process

### Before Submitting PR

1. **Self-Review**
   - Read through all changes
   - Check for errors or typos
   - Verify consistency
   - Test any tools or scripts

2. **Agent Review** (Mandatory)
   ```
   @code-review-agent Review all changes for quality and standards
   @documentation-agent Check documentation consistency
   ```

3. **Address Feedback**
   - Fix issues identified
   - Re-review if significant changes made
   - Iterate until clean

### During PR Review

- Respond to comments promptly
- Be open to suggestions
- Explain your reasoning when needed
- Make requested changes or discuss alternatives
- Mark conversations as resolved when addressed

### Review Focus Areas

Reviewers will check:
- Adherence to specifications
- Quality and accuracy
- Consistency with existing content
- Documentation completeness
- No redundancies introduced
- Proper file organization

## Style Guidelines

### File Naming
- Use lowercase
- Use hyphens for multi-word names
- Be descriptive: `elementary-school.md` not `es.md`
- Consistent extensions: `.md`, `.json`, `.graph`

### Markdown Style
- Use ATX-style headers (`#` not underlines)
- One blank line between sections
- Use fenced code blocks with language tags
- Keep lines under 100 characters when possible
- Use numbered lists when order matters, bullets otherwise

### JSON Style
- Use 2-space indentation
- Include trailing commas where allowed
- Use double quotes for strings
- Keep consistent field ordering

### Writing Style
- Use clear, concise language
- Define terms before using them
- Use active voice
- Be consistent with terminology
- Avoid jargon unless necessary

## Agent Collaboration

### Using Copilot Agents

This project uses specialized AI agents. Leverage them:

**Knowledge Graph Agent**:
```
@knowledge-graph-agent Create a knowledge graph for domain/natural-sciences/chemistry/atoms
covering protons, neutrons, electrons, and their relationships.
```

**Rendering Agent**:
```
@rendering-agent Generate an elementary school rendering of 
domain/formal-sciences/mathematics/pure-mathematics/algebra/knowledge.graph in English.
```

**Documentation Agent**:
```
@documentation-agent Review docs/CONTRIBUTING.md for contradictions
with other documentation.
```

**Contrarian Agent**:
```
@contrarian-agent Critique the proposed knowledge graph structure for
economics/macroeconomics. What are the weaknesses?
```

### Agent Best Practices

1. Be specific in requests
2. Provide context and constraints
3. Review agent output carefully
4. Iterate if needed
5. Learn from agent suggestions

## Questions?

- Check existing documentation first
- Search issues for similar questions
- Open a new issue with the `question` label
- Be specific about what you're trying to accomplish

## Recognition

Contributors will be:
- Listed in knowledge graph metadata
- Acknowledged in project documentation
- Credited for significant contributions

Thank you for contributing to WorldSMEGraphs! 🚀
