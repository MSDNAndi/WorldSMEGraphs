# Visualization Style Guide for WorldSMEGraphs

> **Purpose**: Standards and best practices for creating visual content  
> **Audience**: Content creators, designers, educators  
> **Last Updated**: 2026-01-04

## Table of Contents

1. [Introduction](#introduction)
2. [Visual Types](#visual-types)
3. [Design Principles](#design-principles)
4. [Color Guidelines](#color-guidelines)
5. [Typography](#typography)
6. [Diagram Standards](#diagram-standards)
7. [Tools and Workflows](#tools-and-workflows)
8. [Accessibility](#accessibility)
9. [Examples](#examples)
10. [Quick Reference](#quick-reference)

---

## Introduction

Visual content is essential for making complex knowledge accessible. This guide ensures consistency, quality, and accessibility across all visual materials in WorldSMEGraphs.

### Goals of Visualization

1. **Clarity**: Make complex concepts understandable
2. **Consistency**: Maintain visual language across domains
3. **Accessibility**: Work for all users, including those with disabilities
4. **Scalability**: Look good at all sizes and resolutions
5. **Multilingual**: Support text in multiple languages

---

## Visual Types

### 1. Concept Diagrams

**Purpose**: Show relationships between ideas

**When to use**:
- Hierarchies (taxonomies, classifications)
- Networks (relationships, dependencies)
- Processes (workflows, algorithms)
- Comparisons (similarities, differences)

**Best practices**:
- Keep it simple (max 7-10 elements per diagram)
- Use consistent shapes for consistent meanings
- Clear labels in plain language
- Directional arrows for flow/causation

**Example Use Cases**:
- Domain hierarchy visualization
- Cross-domain linking diagrams
- Concept relationship maps
- Knowledge graph structures

### 2. Mathematical Diagrams

**Purpose**: Illustrate mathematical concepts

**When to use**:
- Geometric proofs
- Function graphs
- Coordinate systems
- Vector operations

**Best practices**:
- Precise measurements
- Clear axis labels
- Standard notation
- Grid lines when helpful

**Example Use Cases**:
- Pythagorean theorem illustration
- Function transformation demonstrations
- Coordinate plane examples
- Geometric constructions

### 3. Scientific Illustrations

**Purpose**: Show scientific phenomena or structures

**When to use**:
- Anatomical structures
- Chemical processes
- Physical systems
- Biological mechanisms

**Best practices**:
- Anatomical accuracy
- Clear labeling
- Appropriate detail level for audience
- Color coding for different elements

**Example Use Cases**:
- Type 2 endoleak anatomy
- Chemical reaction diagrams
- Cell structure illustrations
- Physics experiment setups

### 4. Process Flowcharts

**Purpose**: Show step-by-step procedures

**When to use**:
- Algorithms
- Decision trees
- Workflows
- Troubleshooting guides

**Best practices**:
- Standard flowchart symbols
- Top-to-bottom or left-to-right flow
- Clear decision points
- Numbered steps

**Example Use Cases**:
- AKU creation workflow
- Migration decision tree
- Validation process
- Content review steps

### 5. Data Visualizations

**Purpose**: Present data patterns and trends

**When to use**:
- Statistical data
- Comparisons
- Trends over time
- Distribution patterns

**Best practices**:
- Choose right chart type
- Clear axes and labels
- Minimal decoration
- Accessible colors

**Example Use Cases**:
- AKU statistics by domain
- Migration success rates
- Content difficulty distribution
- Knowledge maturity tracking

### 6. Infographics

**Purpose**: Quick visual summaries

**When to use**:
- Quick references
- Key facts
- Process overviews
- Comparison sheets

**Best practices**:
- One main message
- Mix text and visuals
- Visual hierarchy
- Scannable layout

**Example Use Cases**:
- AKU format overview
- Domain structure summary
- Quick start guides
- Cheat sheets

---

## Design Principles

### 1. Simplicity

**Keep it minimal**:
- Remove unnecessary elements
- One concept per diagram when possible
- White space is your friend
- Clear visual hierarchy

**Example**:
```
❌ TOO COMPLEX:
[Box with 15 interconnected concepts, multiple colors, busy background]

✅ JUST RIGHT:
[Box with 5 key concepts, clear connections, clean background]
```

### 2. Consistency

**Maintain standards**:
- Same shapes mean same things
- Consistent color usage
- Uniform typography
- Standard spacing

**Shape Conventions**:
- **Rectangle**: Process/action
- **Diamond**: Decision point
- **Circle/Ellipse**: Start/end point
- **Rounded rectangle**: Data/content
- **Cloud**: External system/reference

### 3. Hierarchy

**Guide the eye**:
- Most important elements largest/boldest
- Use position (top-left = start)
- Size variation for emphasis
- Color for categorization

**Visual Weight**:
1. **Primary**: Main concept (largest, darkest, or most colorful)
2. **Secondary**: Supporting concepts (medium size/color)
3. **Tertiary**: Details (smallest, lightest)

### 4. Balance

**Distribute visual weight**:
- Symmetrical or asymmetrical balance
- Even distribution of elements
- Avoid cramped or empty areas
- Centered or aligned layouts

### 5. Proximity

**Group related elements**:
- Close = related
- White space = separation
- Boxes for strong grouping
- Background colors for subtle grouping

---

## Color Guidelines

### Primary Color Palette

**Domain Colors** (for domain-specific content):

```
Formal Sciences:     #3498db (Blue)
Natural Sciences:    #27ae60 (Green)
Social Sciences:     #e67e22 (Orange)
Health Sciences:     #e74c3c (Red)
```

**Functional Colors** (for diagrams):

```
Process/Action:      #34495e (Dark Gray)
Decision:            #f39c12 (Amber)
Success/Valid:       #2ecc71 (Green)
Error/Invalid:       #e74c3c (Red)
Warning:             #f39c12 (Orange)
Info:                #3498db (Blue)
Neutral:             #95a5a6 (Gray)
```

**Semantic Colors** (for meaning):

```
Native Domain:       #9b59b6 (Purple)
Application Domain:  #1abc9c (Teal)
Cross-Domain Link:   #e67e22 (Orange)
```

### Color Usage Rules

**DO**:
- ✅ Use domain colors consistently
- ✅ Ensure sufficient contrast (WCAG AA minimum)
- ✅ Test in grayscale
- ✅ Provide color-blind safe alternatives

**DON'T**:
- ❌ Use red-green only distinctions
- ❌ Use color as sole indicator
- ❌ Mix too many colors (max 5-6 per diagram)
- ❌ Use vibrant backgrounds

### Accessibility Colors

**Color-blind safe palette**:

```
Safe Blue:    #0173B2  (distinguishable)
Safe Orange:  #DE8F05  (distinguishable)
Safe Green:   #029E73  (distinguishable)
Safe Yellow:  #ECE133  (distinguishable)
Safe Purple:  #CC78BC  (distinguishable)
Safe Brown:   #CA9161  (distinguishable)
```

**Contrast Requirements**:
- Text on background: 4.5:1 minimum (normal text)
- Large text on background: 3:1 minimum
- UI components: 3:1 minimum

---

## Typography

### Font Choices

**Recommended Fonts**:

**For Diagrams**:
- **Primary**: Arial, Helvetica (sans-serif, highly legible)
- **Alternative**: Open Sans, Roboto

**For Mathematical Content**:
- **Primary**: Computer Modern, Latin Modern (LaTeX-style)
- **Alternative**: STIX, Cambria Math

**For Code**:
- **Primary**: Consolas, Monaco
- **Alternative**: Source Code Pro, Fira Code

### Font Sizes

**Minimum sizes** (for readability):

```
Diagram Labels:  14pt minimum
Body Text:       12pt minimum
Captions:        10pt minimum
Footnotes:       9pt minimum (rarely use)
```

**Recommended Hierarchy**:

```
Title/Heading:   24-32pt, Bold
Subheading:      18-24pt, Semi-bold
Body:            14-16pt, Regular
Labels:          12-14pt, Regular
Small Text:      10-12pt, Regular
```

### Text Guidelines

**DO**:
- ✅ Use title case for headings
- ✅ Use sentence case for labels
- ✅ Left-align text blocks
- ✅ Keep line length reasonable (45-75 characters)

**DON'T**:
- ❌ Use all caps for long text
- ❌ Use italic for body text
- ❌ Mix too many fonts (max 2-3)
- ❌ Use decorative fonts

---

## Diagram Standards

### Flowcharts

**Standard Symbols**:

```
START/END:     ⬭ (Rounded rectangle)
PROCESS:       ▭ (Rectangle)
DECISION:      ⬥ (Diamond)
INPUT/OUTPUT:  ▱ (Parallelogram)
CONNECTOR:     ● (Circle)
```

**Layout**:
- Top to bottom OR left to right
- Consistent arrow direction
- No crossing lines when possible
- Clear spacing between elements

**Example ASCII**:

```
    ┌─────────┐
    │  START  │
    └────┬────┘
         │
    ┌────▼────┐
    │ Process │
    └────┬────┘
         │
    ┌────▼────┐
    │Decision?│◄──┐
    └┬───────┬┘   │
     │ Yes   │ No │
     ▼       └────┘
  ┌─────┐
  │ END │
  └─────┘
```

### Network Diagrams

**Node Types**:
- **Circular nodes**: Concepts, entities
- **Square nodes**: Processes, actions
- **Diamond nodes**: Decision points

**Connection Types**:
- **Solid arrow**: Direct relationship
- **Dashed arrow**: Indirect/weak relationship
- **Bidirectional**: Two-way relationship
- **Labeled**: Specify relationship type

### Tree Diagrams

**Structure**:
- Root at top
- Branches downward
- Consistent spacing
- Aligned levels

**Example**:

```
             Root
            /    \
       Branch1  Branch2
       /    \      |
    Leaf1  Leaf2 Leaf3
```

---

## Tools and Workflows

### Recommended Tools

**For Diagrams**:
1. **draw.io** (diagrams.net) - Free, open-source
2. **Inkscape** - Vector graphics, free
3. **Adobe Illustrator** - Professional (if available)
4. **Figma** - Collaborative, free tier

**For Mathematical Diagrams**:
1. **GeoGebra** - Interactive math
2. **Desmos** - Function plotting
3. **TikZ** (LaTeX) - Precise, programmable
4. **Matplotlib** (Python) - Programmatic

**For Scientific Illustrations**:
1. **BioRender** - Biological diagrams
2. **ChemDraw** - Chemical structures
3. **Blender** - 3D rendering
4. **Medical illustration software** - Domain-specific

**For ASCII Diagrams**:
1. **asciiflow.com** - Online ASCII diagram editor
2. **MonoDraw** (Mac) - ASCII art tool
3. **Plain text** - For simple diagrams

### Workflow

**Step 1: Plan**
- [ ] Define purpose and audience
- [ ] List key elements to show
- [ ] Choose appropriate diagram type
- [ ] Sketch rough layout

**Step 2: Create**
- [ ] Use appropriate tool
- [ ] Follow style guidelines
- [ ] Keep it simple
- [ ] Save source files

**Step 3: Refine**
- [ ] Check clarity
- [ ] Verify accuracy
- [ ] Test readability
- [ ] Get feedback

**Step 4: Export**
- [ ] SVG for scalability (preferred)
- [ ] PNG for compatibility (min 300dpi)
- [ ] Include source files
- [ ] Add alt text descriptions

**Step 5: Integrate**
- [ ] Place in appropriate renders/by-domain/[domain-path]/images/ directory
- [ ] Reference in AKU or documentation
- [ ] Update visual index
- [ ] Document in commit message

---

## Accessibility

### WCAG Guidelines

**Level A** (Minimum):
- Text alternatives for non-text content
- Captions for audio
- Logical structure

**Level AA** (Target):
- Color contrast 4.5:1 (text)
- Color contrast 3:1 (UI)
- Resizable text
- Multiple ways to navigate

**Level AAA** (Ideal):
- Color contrast 7:1
- No images of text
- Extensive alternatives

### Making Diagrams Accessible

**Always provide**:
1. **Alt text**: Concise description (125 chars max)
2. **Long description**: Detailed explanation
3. **Text alternative**: List or table form
4. **Semantic markup**: Proper HTML/SVG structure

**Example Alt Text**:

```
❌ BAD: "Diagram showing relationships"
✅ GOOD: "Flow diagram: AKU creation workflow with 5 steps from research to validation"
```

**Color Accessibility**:
- Don't rely on color alone
- Use patterns or shapes too
- Test with color-blind simulators
- Provide high-contrast version

**Text Accessibility**:
- Minimum 14pt font size
- High contrast text
- No italics in diagrams
- Clear, simple language

---

## Examples

### Example 1: Simple Concept Diagram

**ASCII Version** (for markdown):

```
    Native Domain          Application Domain
    ═════════════         ══════════════════
         
   ┌──────────────┐          ┌──────────────┐
   │   Category   │──────────│  Functional  │
   │    Theory    │ applies  │ Programming  │
   │ (Mathematics)│────────→ │    (CS)      │
   └──────────────┘          └──────────────┘
         
     isNativeDomain:        cross_domain_references:
          true                     applies
```

### Example 2: Process Flowchart

```
START
  │
  ▼
┌────────────────────┐
│  Create AKU file   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Add content for   │
│  all audiences     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Validate AKU     │
└─────────┬──────────┘
          │
    ┌─────▼─────┐
    │  Valid?   │
    └─┬───────┬─┘
      │ Yes   │ No
      │       └─────┐
      ▼             │
   ┌──────┐    ┌────▼────┐
   │ Save │    │   Fix   │
   └──────┘    │  errors │
                └────┬────┘
                     │
                     └──────────┘
```

### Example 3: Hierarchy Tree

```
WorldSMEGraphs Knowledge
        │
        ├── Formal Sciences
        │   ├── Mathematics
        │   │   ├── Pure Mathematics
        │   │   │   ├── Algebra
        │   │   │   ├── Geometry
        │   │   │   └── Category Theory
        │   │   └── Applied Mathematics
        │   └── Computer Science
        │
        ├── Natural Sciences
        │   ├── Physics
        │   ├── Chemistry
        │   └── Biology
        │
        ├── Social Sciences
        │   ├── Economics
        │   ├── Psychology
        │   └── Sociology
        │
        └── Health Sciences
            ├── Medicine
            └── Public Health
```

---

## Quick Reference

### Color Quick Reference

```
Domain Colors:
  Formal:  #3498db (Blue)
  Natural: #27ae60 (Green)
  Social:  #e67e22 (Orange)
  Health:  #e74c3c (Red)

Status Colors:
  Success: #2ecc71 (Green)
  Error:   #e74c3c (Red)
  Warning: #f39c12 (Orange)
  Info:    #3498db (Blue)
```

### Font Size Quick Reference

```
Title:      24-32pt, Bold
Heading:    18-24pt, Semi-bold
Body:       14-16pt, Regular
Labels:     12-14pt, Regular
Small:      10-12pt, Regular
```

### Checklist Before Publishing

Visual Quality:
- [ ] Clear and simple
- [ ] Consistent with style guide
- [ ] Proper colors and contrast
- [ ] Readable fonts and sizes
- [ ] No spelling errors

Accessibility:
- [ ] Alt text provided
- [ ] Long description provided
- [ ] Color-blind safe
- [ ] Sufficient contrast
- [ ] Keyboard navigable (if interactive)

Technical:
- [ ] SVG format (preferred) or high-res PNG
- [ ] Source files saved
- [ ] Optimized file size
- [ ] Proper file naming
- [ ] Documented in index

---

## Additional Resources

- **WCAG Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/
- **Color Contrast Checker**: https://webaim.org/resources/contrastchecker/
- **Color-blind Simulator**: https://www.color-blindness.com/coblis-color-blindness-simulator/
- **ASCII Art Generator**: https://asciiflow.com/

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintainer**: WorldSMEGraphs Team
