# Content Creation Guide for WorldSMEGraphs

> **Purpose**: Comprehensive guide for creating high-quality knowledge content  
> **Audience**: Contributors, domain experts, content creators  
> **Last Updated**: 2026-01-04

## Table of Contents

1. [Overview](#overview)
2. [Content Types](#content-types)
3. [Creating AKUs](#creating-akus)
4. [Writing for Different Audiences](#writing-for-different-audiences)
5. [Quality Standards](#quality-standards)
6. [Visual Content](#visual-content)
7. [Cross-Domain Linking](#cross-domain-linking)
8. [Workflow](#workflow)
9. [Tools and Resources](#tools-and-resources)
10. [Examples](#examples)

---

## Overview

WorldSMEGraphs is a knowledge representation system where content is stored as Atomic Knowledge Units (AKUs) - structured, self-contained pieces of knowledge that can be rendered for different audiences and languages.

### Core Principles

1. **Atomic**: Each AKU contains one complete, self-contained concept
2. **Structured**: Follow consistent JSON schema (aku-v2)
3. **Multi-Audience**: Content for toddlers through experts
4. **Language-Agnostic**: Core structure independent of language
5. **Interconnected**: Cross-references to related concepts
6. **Validated**: All content must pass quality checks

---

## Content Types

### 1. Definitions
**Purpose**: Explain what something is

```json
{
  "@type": "definition",
  "content": {
    "definition": {
      "primary": "Clear, standard definition",
      "technical": "Precise, field-specific definition",
      "simple": "Explanation for beginners"
    }
  }
}
```

**When to use**: Introducing new terms, concepts, or objects

**Examples**:
- What is a variable (mathematics)
- What is photosynthesis (biology)
- What is Net Present Value (economics)

### 2. Theorems
**Purpose**: State and prove mathematical or logical propositions

```json
{
  "@type": "theorem",
  "content": {
    "statement": "Formal theorem statement",
    "proof_methods": ["method1", "method2"],
    "applications": [...]
  }
}
```

**When to use**: Mathematical theorems, laws of physics, logical propositions

**Examples**:
- Pythagorean Theorem
- Newton's Laws
- Central Limit Theorem

### 3. Formulas
**Purpose**: Mathematical or scientific relationships

```json
{
  "@type": "formula",
  "content": {
    "formula": {
      "standard": "E = mc²",
      "latex": "E = mc^2",
      "notation": {
        "E": "Energy",
        "m": "Mass",
        "c": "Speed of light"
      }
    }
  }
}
```

**When to use**: Mathematical equations, physical laws, chemical formulas

**Examples**:
- Einstein's Mass-Energy Equivalence
- Quadratic Formula
- Ideal Gas Law

### 4. Procedures
**Purpose**: Step-by-step instructions

```json
{
  "@type": "procedure",
  "content": {
    "steps": [
      {"step": 1, "action": "...", "details": "..."},
      {"step": 2, "action": "...", "details": "..."}
    ],
    "prerequisites": [...],
    "tools_required": [...]
  }
}
```

**When to use**: Algorithms, techniques, methods, processes

**Examples**:
- How to solve a quadratic equation
- Steps for cell division
- Algorithm for binary search

### 5. Examples
**Purpose**: Concrete instances demonstrating concepts

```json
{
  "@type": "example",
  "content": {
    "scenario": "Description of example",
    "demonstration": "Step-by-step walkthrough",
    "conclusion": "What this shows"
  }
}
```

**When to use**: Illustrating abstract concepts, showing applications

**Examples**:
- Calculating NPV for a project
- Applying Pythagorean theorem
- Sample chemical reaction

### 6. Concepts
**Purpose**: Abstract ideas that tie together definitions, theorems, and examples

```json
{
  "@type": "concept",
  "content": {
    "overview": "High-level explanation",
    "components": ["part1", "part2"],
    "relationships": [...],
    "significance": "Why this matters"
  }
}
```

**When to use**: Big ideas that encompass multiple definitions/theorems

**Examples**:
- The concept of "function" in mathematics
- The concept of "evolution" in biology
- The concept of "value" in economics

---

## Creating AKUs

### Step 1: Choose the Right Domain Path

Domain paths follow the UNESCO/LOC/DDC taxonomy:

```
formal-sciences/
  mathematics/
    pure-mathematics/
      algebra/
      geometry/
      category-theory/
    applied-mathematics/

natural-sciences/
  physics/
  chemistry/
  biology/

social-sciences/
  economics/
  psychology/
  sociology/

health-sciences/
  medicine/
  public-health/
```

**Rule**: Place content in its NATIVE domain (origin), not application domain (usage)

**Example**:
- ✅ Category theory → `formal-sciences/mathematics/pure-mathematics/category-theory/`
- ❌ Category theory → `formal-sciences/computer-science/` (even though CS uses it)

### Step 2: Create the AKU Structure

Minimum required fields:

```json
{
  "@context": "aku-v2",
  "@type": "definition|theorem|formula|procedure|example|concept",
  "@id": "domain:subdomain:topic:specific-id",
  
  "metadata": {
    "version": "2.0.0",
    "created": "2026-01-04T17:15:00.000Z",
    "updated": "2026-01-04T17:15:00.000Z",
    "contributors": ["your-name-or-agent"],
    "confidence": 0.95,
    "status": "draft|review|validated|published",
    "tags": ["tag1", "tag2"]
  },
  
  "classification": {
    "domain_path": "formal-sciences/mathematics/...",
    "type": "definition",
    "difficulty": "beginner|intermediate|advanced|expert",
    "importance": "foundational|important|supplementary",
    "isNativeDomain": true,
    "prerequisites": ["prerequisite-aku-ids"],
    "learning_objectives": ["objective1", "objective2"]
  },
  
  "content": {
    // Content structure depends on @type
  }
}
```

### Step 3: Write Content for Multiple Audiences

Always provide at least three levels:

```json
"definition": {
  "simple": "For children or complete beginners",
  "primary": "For undergraduate-level understanding",
  "technical": "For graduate-level or expert understanding"
}
```

**Guidelines**:

**Simple Level** (Ages 5-12, General Public):
- Use everyday language
- Avoid jargon
- Short sentences
- Concrete examples
- Analogies to familiar things

**Primary Level** (Undergraduates, Educated Readers):
- Standard terminology
- Clear explanations
- Some technical detail
- Proper context
- Academic but accessible

**Technical Level** (Graduate Students, Professionals):
- Precise terminology
- Full technical detail
- Mathematical rigor
- Field-specific notation
- Citations and references

### Step 4: Add Cross-References

If your content uses concepts from OTHER domains:

```json
"cross_domain_references": {
  "applies": [
    {
      "@id": "wsmg:formal-sciences/mathematics/.../concept",
      "sourceDomain": "formal-sciences/mathematics/...",
      "relationship": "applies",
      "applicationContext": "How this applies here"
    }
  ]
}
```

If your content has applications in OTHER domains:

```json
"cross_domain_applications": {
  "used_in": [
    {
      "domain": "formal-sciences/computer-science/...",
      "context": "How it's used there",
      "examples": ["example1", "example2"]
    }
  ]
}
```

### Step 5: Add Semantic Links

Link to external ontologies for interoperability:

```json
"semantic_links": {
  "exact_matches": [
    "http://www.wikidata.org/entity/Q123456",
    "http://dbpedia.org/resource/Concept"
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q123456",
  "skos_preferred_label": {
    "en": "English Name",
    "de": "German Name",
    "es": "Spanish Name"
  }
}
```

### Step 6: Validate

```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate cross-domain references
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json
```

---

## Writing for Different Audiences

### Toddler (Ages 2-4)
- **Length**: 1-2 sentences maximum
- **Vocabulary**: Most common 500 words
- **Style**: Simple, playful
- **Focus**: Concrete, tangible things

**Example** (What is a circle):
> "A circle is round like a ball! It goes all the way around."

### Child (Ages 5-8)
- **Length**: 2-4 sentences
- **Vocabulary**: Grade 1-3 reading level
- **Style**: Engaging, relatable
- **Focus**: Observable phenomena

**Example** (What is a circle):
> "A circle is a shape that is perfectly round. If you draw a dot and walk the same distance all around it, you make a circle! Wheels, plates, and coins are circles."

### Pre-teen (Ages 9-12)
- **Length**: 1 paragraph
- **Vocabulary**: Grade 4-6 reading level
- **Style**: Clear, educational
- **Focus**: Beginning abstractions

**Example** (What is a circle):
> "A circle is a shape where every point on the edge is the same distance from the center. This distance is called the radius. You can draw a circle with a compass by keeping the point in one place and rotating the pencil around it. Circles are everywhere in nature and technology because they can spin smoothly."

### High School (Ages 13-18)
- **Length**: 1-2 paragraphs
- **Vocabulary**: High school level
- **Style**: Academic but accessible
- **Focus**: Formal definitions, properties

**Example** (What is a circle):
> "A circle is the set of all points in a plane that are equidistant from a fixed point called the center. The constant distance is called the radius (r). A circle can be defined by the equation (x-h)² + (y-k)² = r², where (h,k) is the center. Key properties include having infinite lines of symmetry through the center, a constant curvature, and a circumference of 2πr."

### Undergraduate
- **Length**: 2-3 paragraphs
- **Vocabulary**: Academic terminology
- **Style**: Textbook-like
- **Focus**: Rigorous definitions, theorems, proofs

**Example** (What is a circle):
> "A circle is formally defined as the locus of points in a Euclidean plane equidistant from a fixed point called the center. In Cartesian coordinates, a circle with center (h,k) and radius r satisfies (x-h)² + (y-k)² = r². In polar coordinates, a circle centered at the origin has the simple form r = constant.
>
> Circles possess unique properties: they maximize area for a given perimeter, have constant curvature 1/r, and exhibit infinite rotational symmetry. The circle is a special case of an ellipse where both foci coincide, and can be generalized to n-dimensional spheres in higher dimensions."

### Graduate/Professional
- **Length**: Multiple paragraphs
- **Vocabulary**: Field-specific terminology
- **Style**: Research paper level
- **Focus**: Advanced theory, applications, current research

**Example** (What is a circle):
> "In differential geometry, a circle in ℝ² can be characterized as a simple closed curve with constant curvature κ = 1/r. More generally, circles are geodesics on the 2-sphere S², embedding naturally into discussions of Riemannian manifolds with constant sectional curvature.
>
> The circle group S¹ plays a fundamental role in topology and algebra. As a topological space, S¹ is compact, connected, and serves as the simplest example of a non-trivial manifold. Algebraically, it forms a Lie group under complex multiplication when viewed as {z ∈ ℂ : |z| = 1}, making it central to representation theory and harmonic analysis.
>
> In complex analysis, the unit circle |z| = 1 bounds the unit disk and appears in Cauchy's integral formulas, conformal mappings, and the study of analytic functions. The Riemann sphere compactification relates circles to lines via stereographic projection, fundamental to M öbius transformations and the study of holomorphic dynamics."

---

## Quality Standards

### Accuracy
✅ **DO**:
- Cite authoritative sources
- Verify all facts and formulas
- Use peer-reviewed references
- Include multiple perspectives when applicable

❌ **DON'T**:
- Make unsupported claims
- Use outdated information
- Rely on single sources
- Present opinions as facts

### Clarity
✅ **DO**:
- Use precise terminology
- Define terms before using them
- Provide examples
- Break complex ideas into steps

❌ **DON'T**:
- Use unnecessary jargon
- Assume prior knowledge
- Skip logical steps
- Use ambiguous language

### Completeness
✅ **DO**:
- Cover all essential aspects
- Include prerequisites
- Provide context
- Link to related concepts

❌ **DON'T**:
- Leave gaps in explanation
- Omit important details
- Ignore common misconceptions
- Forget practical applications

### Consistency
✅ **DO**:
- Follow naming conventions
- Use standard notation
- Match field conventions
- Align with taxonomy

❌ **DON'T**:
- Invent new terminology
- Use inconsistent notation
- Contradict other AKUs
- Misclassify content

---

## Visual Content

### When to Create Visuals

**Always create for**:
- Complex processes (flowcharts, diagrams)
- Spatial relationships (geometry, anatomy)
- Data patterns (graphs, charts)
- Sequences (timelines, algorithms)

**Consider creating for**:
- Abstract concepts (metaphorical diagrams)
- Comparisons (side-by-side tables)
- Hierarchies (tree diagrams)
- Relationships (network graphs)

### Types of Visuals

1. **ASCII Diagrams** (in markdown)
   - Simple flowcharts
   - Basic relationships
   - Quick sketches

2. **SVG Graphics**
   - Scalable illustrations
   - Mathematical diagrams
   - Interactive elements

3. **Images**
   - Photographs (real-world examples)
   - Rendered graphics
   - Medical/scientific imagery

4. **Interactive Elements**
   - Manipulable diagrams
   - Animations
   - Simulations

### Creating Visual Guides

See example in `renders/by-domain/formal-sciences/computer-science/programming-paradigms/functional-programming/functional-programming-visual-guide.md`

**Structure**:
1. Overview diagram
2. Component breakdowns
3. Step-by-step illustrations
4. Real-world examples
5. Practice exercises

---

## Cross-Domain Linking

### Native Domain Principle

**Rule**: Concepts belong to their ORIGIN field, not where they're USED

**Example - Category Theory**:
- **Native Domain**: `formal-sciences/mathematics/pure-mathematics/category-theory/`
- **Application Domains**: Computer science (functional programming), physics (quantum mechanics)

**AKU in Native Domain** (mathematics):
```json
{
  "@id": "math:category-theory:monad",
  "classification": {
    "domain_path": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "isNativeDomain": true
  },
  "cross_domain_applications": {
    "used_in": [
      {
        "domain": "formal-sciences/computer-science/programming-paradigms/functional",
        "context": "Monads structure effectful computations in functional programming",
        "examples": ["Maybe monad", "IO monad", "List monad"]
      }
    ]
  }
}
```

**AKU in Application Domain** (computer science):
```json
{
  "@id": "cs:functional-programming:monad-usage",
  "classification": {
    "domain_path": "formal-sciences/computer-science/...",
    "isApplicationDomain": true,
    "isNativeDomain": false
  },
  "cross_domain_references": {
    "applies": [
      {
        "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
        "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
        "relationship": "applies",
        "applicationContext": "We use the mathematical concept of monads to handle side effects"
      }
    ]
  }
}
```

---

## Workflow

### 1. Research Phase
- [ ] Gather authoritative sources
- [ ] Review existing related AKUs
- [ ] Identify domain placement
- [ ] List prerequisites
- [ ] Plan content structure

### 2. Creation Phase
- [ ] Create AKU file with template
- [ ] Write content for all audience levels
- [ ] Add formulas/examples if applicable
- [ ] Include cross-references
- [ ] Add semantic links
- [ ] Write for multiple languages (if multilingual)

### 3. Validation Phase
- [ ] Run structure validator
- [ ] Check cross-domain links
- [ ] Verify all facts and formulas
- [ ] Review with domain expert
- [ ] Test readability at each level

### 4. Integration Phase
- [ ] Add to appropriate directory
- [ ] Update related AKUs with links
- [ ] Create renders if needed
- [ ] Update indexes
- [ ] Document in concept-index.yaml

### 5. Review Phase
- [ ] Self-review checklist
- [ ] Peer review (if available)
- [ ] Agent review (quality, fact-checking)
- [ ] Address all feedback
- [ ] Final validation

---

## Tools and Resources

### Creation Tools
- **Python**: See `docs/tutorials/PYTHON-AKU-TUTORIAL.md`
- **Migration Scripts**: `domain/_ontology/tools/`
- **Validators**: `.project/agents/quality-assurance/tools/`

### Documentation
- **Domain Navigation**: `domain/_ontology/DOMAIN-NAVIGATION-GUIDE.md`
- **FAQ**: `domain/_ontology/FAQ.md`
- **Migration Guide**: `domain/_ontology/MIGRATION-QUICKSTART.md`
- **Tools Docs**: `domain/_ontology/TOOLS-DOCUMENTATION.md`

### Standards and References
- **Global Hierarchy**: `domain/_ontology/global-hierarchy.yaml`
- **AKU Format Spec**: `docs/aku-format-v2.md` (if exists)
- **UNESCO Taxonomy**: http://vocabularies.unesco.org/browser/thesaurus/en/
- **Library of Congress**: https://www.loc.gov/aba/cataloging/classification/

---

## Examples

### Example 1: Simple Definition AKU

See: `domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-002-category-definition.json`

### Example 2: Formula with Multiple Audiences

See: `domain/social-sciences/economics/bwl/finance/valuation/npv/akus/examples/example-npv-definition-with-semantic-annotations.json`

### Example 3: Cross-Domain Application

See: Functional programming AKUs in `domain/science/computer-science/functional-theory/`

---

## Quick Checklist

Before submitting content:

**Structure**:
- [ ] Follows aku-v2 schema
- [ ] Has all required fields (@context, @type, @id, metadata, classification, content)
- [ ] Proper domain_path set
- [ ] isNativeDomain correctly set

**Content Quality**:
- [ ] Written for multiple audience levels
- [ ] Facts verified from authoritative sources
- [ ] Formulas checked and notation explained
- [ ] Examples clear and correct
- [ ] No typos or grammatical errors

**Integration**:
- [ ] Prerequisites listed
- [ ] Learning objectives stated
- [ ] Cross-references added (if applicable)
- [ ] Semantic links included (if applicable)
- [ ] Tags relevant and complete

**Validation**:
- [ ] Passes `validate_aku_v2.py`
- [ ] Passes `validate_cross_domain.py` (if has cross-refs)
- [ ] Reviewed by domain expert (if possible)
- [ ] Ready for publication

---

## Getting Help

- **Questions**: See FAQ at `domain/_ontology/FAQ.md`
- **New Contributors**: Start with `domain/_ontology/NEW-CONTRIBUTOR-TUTORIAL.md`
- **Technical Issues**: Check `domain/_ontology/TROUBLESHOOTING.md`
- **Community**: Check project README for communication channels

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintainer**: WorldSMEGraphs Team
