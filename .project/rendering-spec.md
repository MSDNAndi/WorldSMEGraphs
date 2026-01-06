# Rendering System Specification

> **Version**: 1.0  
> **Status**: Draft  
> **Last Updated**: 2025-12-26  
> **Owner**: Rendering Agent

## Overview
The rendering system transforms language-agnostic knowledge graphs into human-readable content tailored for specific languages, audiences, and formats.

## Design Goals

### 1. Audience Appropriateness
Content must match the cognitive level and background of the target audience.

### 2. Language Flexibility
Support multiple natural languages without modifying source graphs.

### 3. Format Versatility
Generate content in various formats: Markdown, PDF, LaTeX, DOCX, HTML.

### 4. Consistency
Renderings accurately represent knowledge graph content.

### 5. Maintainability
Easy to update renderings when graphs change.

## Architecture

### Components

```
Knowledge Graph (source)
        ↓
Rendering Engine
        ↓
    Templates
        ↓
   Formatters
        ↓
Output Files (renders/)
```

### Data Flow

1. **Parse** knowledge graph
2. **Select** template for target audience/language
3. **Map** UIDs to localized content
4. **Generate** human-readable text
5. **Format** for output medium
6. **Validate** against quality criteria
7. **Output** to `renders/by-domain/[domain-path]/[language]/[audience].[format]`

## Directory Structure

```
domain/[topic]/
├── knowledge.graph           # Source
└── schema.json              # Schema

renders/by-domain/[topic]/   # Outputs
    ├── english/
    │   ├── 4-year-old.md
    │   ├── elementary-school.md
    │   ├── middle-school.md
    │   ├── high-school.md
    │   ├── adult-limited-reading.md
    │   ├── adult.md
    │   └── graduate.md
    ├── german/
    │   ├── grundschule.md      # Elementary
    │   ├── hochschule.md       # University
    │   └── erwachsene.md       # Adults
    ├── spanish/
    │   └── escuela-primaria.md
    └── [other-languages]/
```

## Audience Levels

### 1. Toddler (2-3 years)
**Characteristics**:
- Very limited vocabulary (100-500 words)
- Concrete thinking only
- Short attention span
- Visual learning

**Guidelines**:
- Use 2-4 word sentences
- Describe with pictures/visuals
- Use repetition
- Focus on concrete, physical concepts
- Include interactive elements

**Example**:
```markdown
# Big and Small

This is big: 🐘
This is small: 🐭

You are bigger than a mouse!
```

### 2. 4-Year-Old
**Characteristics**:
- Vocabulary: 1,000-2,000 words
- Beginning abstract thinking
- Curious, asks "why"
- Learning through play

**Guidelines**:
- Use 5-8 word sentences
- Explain with simple analogies
- Answer "why" questions
- Include examples from daily life
- Use colorful language

**Example**:
```markdown
# What is a Number?

A number tells us "how many."

You have 2 hands. ✋✋
You have 5 fingers on each hand. ✋

Count your fingers: 1, 2, 3, 4, 5!
```

### 3. Elementary School (6-11 years)
**Characteristics**:
- Growing vocabulary
- Developing logical thinking
- Learning to read fluently
- Interested in how things work

**Guidelines**:
- Use grade-appropriate vocabulary
- Explain concepts step-by-step
- Include practice examples
- Use diagrams and illustrations
- Make connections to everyday life

**Example**:
```markdown
# Variables in Algebra

A variable is like a box that can hold different numbers.

We often use letters like x, y, or z for variables.

Example: If x = 5, then x + 3 = 8

Try it: If y = 7, what is y + 2?
```

### 4. Middle School (12-14 years)
**Characteristics**:
- Abstract thinking developing
- Can handle more complexity
- Questioning and analyzing
- Building on prior knowledge

**Guidelines**:
- Introduce formal terminology
- Show multiple perspectives
- Include problem-solving exercises
- Connect to real-world applications
- Challenge with moderate complexity

### 5. High School (15-18 years)
**Characteristics**:
- Advanced abstract thinking
- Preparing for specialization
- Critical thinking skills
- Can handle formal proofs

**Guidelines**:
- Use technical vocabulary
- Present formal definitions
- Include proofs and derivations
- Show advanced applications
- Prepare for college-level work

### 6. Adult (General)
**Characteristics**:
- Varied educational backgrounds
- Life experience
- Practical focus
- Self-directed learning

**Guidelines**:
- Clear, efficient explanations
- Focus on practical applications
- Assume general knowledge
- Minimize jargon with explanations
- Respect reader's time

### 7. Adult (Limited Reading Comprehension)
**Characteristics**:
- Reading below high school level
- May have knowledge but struggle with text
- Need clear, simple language
- Benefit from visual aids

**Guidelines**:
- Use short sentences (10-15 words)
- Simple vocabulary
- Clear structure with headings
- Bullet points and lists
- Visual aids and examples
- Define technical terms immediately

**Example**:
```markdown
# What is Inflation?

Inflation means prices go up over time.

Example:
- 10 years ago: Coffee costs $2
- Today: Coffee costs $3

The same coffee costs more now. That is inflation.

Why does this happen?
- More money is printed
- More people want the same things
- Things cost more to make
```

### 8. Graduate/Expert
**Characteristics**:
- Advanced education in field
- Seeking depth and rigor
- Comfortable with technical language
- Interested in research and theory

**Guidelines**:
- Use formal academic language
- Include citations and references
- Present current research
- Show mathematical rigor
- Discuss open questions
- Connect to advanced topics

## Language Localization

### Content Mapping File
Each language has a mapping file:

`renders/by-domain/[domain-path]/[language]/mappings.json`:
```json
{
  "algebra:variable": {
    "term": "variable",
    "article": "a",
    "plural": "variables",
    "description": "a symbol representing a number",
    "examples": ["x", "y", "z"]
  },
  "algebra:equation": {
    "term": "equation",
    "article": "an",
    "plural": "equations",
    "description": "a mathematical statement of equality"
  }
}
```

### Translation Guidelines
1. Translate concepts, not words literally
2. Use culturally appropriate examples
3. Adapt idioms and metaphors
4. Maintain technical accuracy
5. Consult domain experts for specialized terms

## Output Formats

### Markdown (.md)
**Primary format** for web and documentation.

**Features**:
- Headers, lists, tables
- Code blocks for examples
- Links and cross-references
- Images and diagrams
- Widely supported

**Use Cases**:
- Online documentation
- Quick reference
- GitHub/GitLab display
- Easy editing

### PDF
For print and distribution.

**Features**:
- Professional formatting
- Pagination
- Table of contents
- Consistent appearance

**Generation**: Markdown → Pandoc → PDF

**Use Cases**:
- Textbooks
- Print materials
- Official documents
- Distribution

### LaTeX/TeX
For academic and mathematical content.

**Features**:
- Superior math typesetting
- Academic formatting
- Bibliography management
- High-quality output

**Use Cases**:
- Research papers
- Textbooks
- Mathematical proofs
- Scientific publishing

### DOCX
For collaborative editing.

**Features**:
- Microsoft Word format
- Track changes
- Comments
- Wide compatibility

**Use Cases**:
- Collaborative review
- Corporate environments
- Educational institutions
- Easy editing by non-technical users

### HTML
For web applications.

**Features**:
- Interactive elements
- Styling with CSS
- JavaScript integration
- Accessibility features

**Use Cases**:
- Web applications
- Interactive learning
- Online courses
- Dynamic content

## Quality Criteria

### Accuracy
- Content matches knowledge graph
- No information added or lost
- Technical correctness verified
- Examples are correct

### Appropriateness
- Language matches audience level
- Complexity is appropriate
- Cultural sensitivity maintained
- Examples relevant to audience

### Clarity
- Easy to understand
- Logical flow
- Clear explanations
- Unambiguous language

### Completeness
- All key concepts covered
- Sufficient detail for audience
- Examples provided
- Context given

### Consistency
- Terminology used consistently
- Style matches other renderings
- Cross-references work
- Format is uniform

## Rendering Templates

### Template Structure

```markdown
---
source: [graph-path]
language: [language]
audience: [level]
version: 1.0
generated: [date]
---

# [Localized Title]

[Introduction appropriate for audience]

## [Concept 1]
[Explanation using audience-appropriate language]

### Examples
[Relevant examples for audience]

### Try It Yourself
[Practice problems if appropriate]

## [Concept 2]
...

## Related Topics
- [Cross-links to other rendered topics]

## Learn More
- [Suggestions for next topics]
```

### Template Selection

Rendering engine selects template based on:
1. Target audience level
2. Domain (some domains need specialized templates)
3. Output format
4. Language (some languages need different structures)

## Automation

### Automated Rendering Pipeline

```bash
# Command line tool (planned)
render --graph domain/formal-sciences/mathematics/pure-mathematics/algebra/knowledge.graph \
       --language english \
       --audience elementary-school \
       --format markdown \
       --output renders/by-domain/formal-sciences/mathematics/pure-mathematics/algebra/english/
```

### CI/CD Integration
- Auto-generate renderings on graph changes
- Validate rendering quality
- Check for broken cross-references
- Verify readability scores

## Validation

### Automated Checks
- [ ] All UIDs from graph are rendered
- [ ] Cross-links are valid
- [ ] Readability score matches target audience
- [ ] No broken links or references
- [ ] Format is valid
- [ ] Metadata is complete

### Manual Review
- [ ] Accuracy verified by domain expert
- [ ] Appropriateness confirmed for audience
- [ ] Examples are helpful and correct
- [ ] Language is natural and clear
- [ ] Cultural sensitivity checked

## Readability Metrics

### Tools
- Flesch Reading Ease
- Flesch-Kincaid Grade Level
- SMOG Index
- Coleman-Liau Index

### Target Scores by Audience

| Audience | Flesch-Kincaid Grade |
|----------|---------------------|
| 4-year-old | < 1.0 |
| Elementary | 2.0 - 5.0 |
| Middle School | 6.0 - 8.0 |
| High School | 9.0 - 12.0 |
| Adult (Limited) | 6.0 - 8.0 |
| Adult | 8.0 - 12.0 |
| Graduate | 13.0+ |

## Visualization Support

### Future Enhancement
Renderings may include:
- Concept maps
- Graphs and charts
- Animated explanations
- Interactive diagrams
- Video explanations

### Planned Tools
- Mermaid for diagrams
- D3.js for interactive visualizations
- Manim for mathematical animations
- TikZ for LaTeX graphics

## Best Practices

### For Rendering Agents
1. Always validate against source graph
2. Use appropriate templates
3. Test readability scores
4. Get expert review for technical content
5. Consider cultural context
6. Maintain consistency with existing renderings

### For Manual Editors
1. Follow audience guidelines strictly
2. Use mapping files for terminology
3. Include metadata in frontmatter
4. Cross-link to related topics
5. Provide examples at appropriate level
6. Test with target audience when possible

## Examples

### Complete Rendering Example
See: `examples/sample-rendering.md` (to be created)

## Future Enhancements

### Planned Features
1. **Adaptive Rendering**: Adjust to reader's demonstrated comprehension
2. **Interactive Mode**: Embedded exercises and immediate feedback
3. **Multimedia Integration**: Audio explanations, video demonstrations
4. **Personalization**: Customize examples to reader's interests
5. **Accessibility**: Screen reader optimization, alternative text
6. **Collaborative Review**: In-line suggestions and improvements

## References

- Readability formulas and standards
- Pedagogical best practices
- Writing for different audiences
- Technical writing guidelines
- Accessibility standards (WCAG)

---

**Status**: This specification is in draft form and will be refined based on pilot implementation feedback.
