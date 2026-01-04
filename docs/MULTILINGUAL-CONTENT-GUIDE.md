# Multilingual Content Guide for WorldSMEGraphs

> **Purpose**: Guidelines for creating and managing content in multiple languages  
> **Audience**: Content creators, translators, localization specialists  
> **Last Updated**: 2026-01-04

## Table of Contents

1. [Introduction](#introduction)
2. [Language-Agnostic Core](#language-agnostic-core)
3. [Rendering for Languages](#rendering-for-languages)
4. [Translation Standards](#translation-standards)
5. [Cultural Adaptation](#cultural-adaptation)
6. [Language-Specific Considerations](#language-specific-considerations)
7. [Tools and Workflow](#tools-and-workflow)
8. [Quality Assurance](#quality-assurance)
9. [Examples](#examples)
10. [Resources](#resources)

---

## Introduction

WorldSMEGraphs uses a language-agnostic core with language-specific renders. This approach ensures:

1. **Single Source of Truth**: Core knowledge independent of language
2. **Scalability**: Easy to add new languages
3. **Consistency**: Same structure across all languages
4. **Efficiency**: Translate once, render for all audiences

### Architecture Overview

```
Core AKU (language-agnostic)
    ├── classification (domain, type, difficulty)
    ├── metadata (version, status, contributors)
    ├── structure (relationships, prerequisites)
    └── semantic_links (ontology references)
        │
        └── .renders/
            ├── english/
            │   ├── toddler.md
            │   ├── child.md
            │   ├── elementary-school.md
            │   ├── high-school.md
            │   └── graduate.md
            ├── spanish/
            │   ├── niño-pequeño.md
            │   ├── niño.md
            │   └── universidad.md
            ├── german/
            │   ├── kleinkind.md
            │   └── hochschule.md
            └── chinese/
                ├── 幼儿.md
                └── 大学.md
```

---

## Language-Agnostic Core

### What Goes in the Core AKU

**Include** (language-independent):
- Classification (domain_path, type, difficulty)
- Metadata (version, timestamps, status)
- Structure (prerequisites, relationships)
- Semantic links (@id, ontology URIs)
- Mathematical notation (LaTeX, symbolic)
- Cross-domain references
- Validation status

**Example Core Section**:

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "math:geometry:pythagorean-theorem",
  "classification": {
    "domain_path": "formal-sciences/mathematics/geometry",
    "type": "theorem",
    "difficulty": "intermediate",
    "importance": "foundational"
  },
  "semantic_links": {
    "exact_matches": [
      "http://www.wikidata.org/entity/Q11518",
      "http://dbpedia.org/resource/Pythagorean_theorem"
    ],
    "skos_preferred_label": {
      "en": "Pythagorean Theorem",
      "de": "Satz des Pythagoras",
      "es": "Teorema de Pitágoras",
      "fr": "Théorème de Pythagore",
      "zh": "勾股定理",
      "ja": "ピタゴラスの定理",
      "ar": "مبرهنة فيثاغورس",
      "ru": "Теорема Пифагора"
    }
  }
}
```

### What Goes in Renders

**Include** (language-specific):
- Full text explanations
- Examples with natural language
- Cultural context
- Analogies and metaphors
- Region-specific applications
- Local measurement systems

---

## Rendering for Languages

### Directory Structure

```
domain/formal-sciences/mathematics/geometry/
├── pythagorean-theorem.json          # Core AKU (language-agnostic)
└── .renders/
    ├── english/
    │   ├── toddler.md                 # Ages 2-4
    │   ├── child.md                   # Ages 5-8
    │   ├── pre-teen.md                # Ages 9-12
    │   ├── high-school.md             # Ages 13-18
    │   ├── undergraduate.md           # University
    │   └── graduate.md                # Advanced
    ├── spanish/
    │   ├── niño-pequeño.md
    │   ├── niño.md
    │   ├── adolescente.md
    │   ├── bachillerato.md
    │   ├── universidad.md
    │   └── postgrado.md
    ├── german/
    │   ├── kleinkind.md
    │   ├── kind.md
    │   ├── gymnasium.md
    │   └── hochschule.md
    ├── french/
    │   ├── tout-petit.md
    │   ├── enfant.md
    │   ├── collège.md
    │   └── université.md
    ├── chinese/
    │   ├── 幼儿.md
    │   ├── 儿童.md
    │   ├── 中学.md
    │   └── 大学.md
    └── japanese/
        ├── 幼児.md
        ├── 子供.md
        ├── 中学生.md
        └── 大学.md
```

### Naming Conventions

**Language Codes** (ISO 639-1):
- `english/` (en)
- `spanish/` (es)
- `french/` (fr)
- `german/` (de)
- `italian/` (it)
- `portuguese/` (pt)
- `chinese/` (zh)
- `japanese/` (ja)
- `korean/` (ko)
- `arabic/` (ar)
- `russian/` (ru)
- `hindi/` (hi)

**Audience Level Files**:
Use native language terms for audience levels, not English translations.

**English**:
- `toddler.md`, `child.md`, `pre-teen.md`, `high-school.md`, `undergraduate.md`, `graduate.md`

**Spanish**:
- `niño-pequeño.md`, `niño.md`, `preadolescente.md`, `bachillerato.md`, `universidad.md`, `postgrado.md`

**German**:
- `kleinkind.md`, `kind.md`, `jugendlicher.md`, `gymnasium.md`, `hochschule.md`, `promotion.md`

**Chinese** (simplified):
- `幼儿.md` (yòu'ér), `儿童.md` (értóng), `少年.md` (shàonián), `中学.md` (zhōngxué), `大学.md` (dàxué), `研究生.md` (yánjiūshēng)

---

## Translation Standards

### Quality Levels

**Level 1: Machine Translation + Review**
- Use automated translation
- Human review for accuracy
- Fix obvious errors
- Good for initial coverage

**Level 2: Professional Translation**
- Native speaker translator
- Domain expert review
- Cultural adaptation
- Standard for published content

**Level 3: Localization**
- Full cultural adaptation
- Local examples and contexts
- Region-specific terminology
- Gold standard for target markets

### Translation Process

**Step 1: Prepare Source**
- [ ] Finalize English version
- [ ] Mark terminology for consistency
- [ ] Note cultural references
- [ ] Identify idioms to adapt

**Step 2: Translate**
- [ ] Use translation memory
- [ ] Maintain terminology glossary
- [ ] Preserve formatting
- [ ] Keep technical terms consistent

**Step 3: Review**
- [ ] Native speaker review
- [ ] Domain expert check
- [ ] Cultural appropriateness
- [ ] Technical accuracy

**Step 4: Test**
- [ ] Readability test at target level
- [ ] Cultural sensitivity check
- [ ] Technical term verification
- [ ] Format/layout check

**Step 5: Publish**
- [ ] Add to .renders/ directory
- [ ] Update language index
- [ ] Document contributors
- [ ] Mark review status

### Terminology Management

**Create Glossary**:

```json
{
  "term": "Atomic Knowledge Unit",
  "translations": {
    "es": "Unidad de Conocimiento Atómico",
    "de": "Atomare Wissenseinheit",
    "fr": "Unité de Connaissance Atomique",
    "zh": "原子知识单元",
    "ja": "原子的知識単位"
  },
  "context": "Core structural element of knowledge graph",
  "usage_notes": "Always capitalize in formal documents"
}
```

**Maintain Consistency**:
- Use same translation for same term
- Document exceptions
- Update glossary regularly
- Share across translators

---

## Cultural Adaptation

### Localizing Examples

**Original (English)**:
> "Imagine you have a football field that is 100 yards long..."

**Adapted (Metric Countries)**:
> "Imagine you have a football pitch that is 90 meters long..."

**Adapted (Asian Context)**:
> "Imagine you have a rice field that is 100 meters long..."

### Cultural References

**General Principle**: Use culturally appropriate examples

**Examples**:

**Food**:
- English: "slicing a pizza into 8 pieces"
- Chinese: "cutting a moon cake into 8 pieces"
- Indian: "dividing a roti into 8 parts"

**Sports**:
- US: "baseball diamond"
- Europe: "football pitch"
- Cricket nations: "cricket oval"

**Currency**:
- US: "dollars and cents"
- Europe: "euros and cents"
- Japan: "yen"
- Use local currency symbols

**Measurements**:
- US: Imperial (feet, miles, pounds)
- Most others: Metric (meters, kilometers, kilograms)
- Always provide both when critical

### Sensitive Topics

**Be aware of**:
- Religious references
- Political examples
- Gender roles
- Historical events
- Social norms

**Guidelines**:
- Use neutral examples
- Avoid controversial topics
- Respect cultural values
- When in doubt, generalize

---

## Language-Specific Considerations

### Right-to-Left Languages (Arabic, Hebrew)

**Technical Considerations**:
- Mirror layouts where appropriate
- Don't mirror mathematical notation
- Proper text direction in diagrams
- Test rendering carefully

**Example**:
```html
<div dir="rtl" lang="ar">
  النظرية: في المثلث القائم، مربع الوتر يساوي مجموع مربعي الضلعين الآخرين
</div>
```

### Character Sets (Chinese, Japanese, Korean)

**Considerations**:
- Use Unicode (UTF-8)
- Simplified vs Traditional Chinese
- Kanji vs Hiragana balance (Japanese)
- Hanja usage (Korean - mostly avoided now)

**Font Requirements**:
- CJK font support essential
- Proper line height (taller than Latin)
- Character spacing
- Mixed script handling

### Formal vs Informal (Many Languages)

**German**:
- "Sie" (formal) vs "du" (informal)
- Use formal for undergraduate+
- Informal for children

**Spanish**:
- "usted" (formal) vs "tú" (informal)
- Regional variations (vosotros in Spain)

**French**:
- "vous" (formal) vs "tu" (informal)

**Japanese**:
- Multiple politeness levels
- Choose appropriate for audience

### Gendered Language

**Spanish/French/German**:
- Default to neutral when possible
- Use inclusive language
- "All students" not "he/she"

**Example (Spanish)**:
❌ "El estudiante debe..." (masculine default)
✅ "Los estudiantes deben..." (plural neutral)
✅ "El/la estudiante debe..." (explicit inclusion)

---

## Tools and Workflow

### Translation Tools

**Translation Memory**:
- **OmegaT** - Free, open-source
- **Trados** - Professional standard
- **Memsource** - Cloud-based

**Machine Translation**:
- **DeepL** - High quality, context-aware
- **Google Translate** - Wide language support
- **Microsoft Translator** - Good for technical

**Terminology Management**:
- **Termbase** files
- Custom glossaries
- Shared terminology databases

### Workflow Automation

**Using Python**:

```python
import json
from pathlib import Path

def create_render_template(aku_id, language, audience_level):
    """Create a template for translators."""
    return f"""# {aku_id} - {audience_level.title()}

## Definition

[TRANSLATE: Provide definition at {audience_level} level]

## Explanation

[TRANSLATE: Detailed explanation appropriate for {audience_level}]

## Examples

[ADAPT: Use culturally appropriate examples for {language}]

## Practice

[TRANSLATE: Practice questions or exercises]

---

**Translation Notes**:
- Target audience: {audience_level}
- Language: {language}
- Maintain {audience_level}-appropriate vocabulary
- Adapt examples to local context
"""

# Generate templates for translators
template = create_render_template(
    "math:geometry:pythagorean",
    "Spanish",
    "high-school"
)
print(template)
```

### Quality Assurance Tools

**Validation**:
```bash
# Check encoding
file -i path/to/file.md

# Check language detection
python -c "from langdetect import detect; print(detect(open('file.md').read()))"

# Spell check
aspell -l es check spanish-file.md
```

---

## Quality Assurance

### Review Checklist

**Technical Accuracy**:
- [ ] Facts correct in target language
- [ ] Formulas unchanged (or properly adapted)
- [ ] Technical terms consistent
- [ ] Numbers and units correct

**Language Quality**:
- [ ] Grammar correct
- [ ] Natural phrasing
- [ ] Appropriate register (formal/informal)
- [ ] No machine translation artifacts

**Cultural Appropriateness**:
- [ ] Examples culturally relevant
- [ ] No offensive content
- [ ] Measurements localized
- [ ] Currency adapted

**Formatting**:
- [ ] Markdown correct
- [ ] Links working
- [ ] Images display correctly
- [ ] Math notation renders

**Completeness**:
- [ ] All sections translated
- [ ] Metadata updated
- [ ] Attribution present
- [ ] Review status marked

---

## Examples

### Example 1: Simple Concept (Pythagorean Theorem)

**English (High School)**:
```markdown
# Pythagorean Theorem

## Definition
In a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides.

## Formula
a² + b² = c²

Where:
- a and b are the legs of the triangle
- c is the hypotenuse (longest side)

## Example
If a triangle has legs of 3 and 4 units:
- 3² + 4² = c²
- 9 + 16 = c²
- 25 = c²
- c = 5
```

**Spanish (Bachillerato)**:
```markdown
# Teorema de Pitágoras

## Definición
En un triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los otros dos lados.

## Fórmula
a² + b² = c²

Donde:
- a y b son los catetos del triángulo
- c es la hipotenusa (lado más largo)

## Ejemplo
Si un triángulo tiene catetos de 3 y 4 unidades:
- 3² + 4² = c²
- 9 + 16 = c²
- 25 = c²
- c = 5
```

**Chinese (中学)**:
```markdown
# 勾股定理

## 定义
在直角三角形中，斜边的平方等于两直角边的平方和。

## 公式
a² + b² = c²

其中：
- a 和 b 是直角三角形的两条直角边
- c 是斜边（最长的边）

## 例子
如果一个三角形的直角边长度为 3 和 4 单位：
- 3² + 4² = c²
- 9 + 16 = c²
- 25 = c²
- c = 5
```

### Example 2: Cultural Adaptation

**Original (US Context)**:
> "If you drive 60 miles per hour for 2 hours, how far do you travel?"

**Adapted (Metric)**:
> "If you drive 100 kilometers per hour for 2 hours, how far do you travel?"

**Adapted (Non-driving culture)**:
> "If a train travels 100 kilometers per hour for 2 hours, how far does it go?"

---

## Resources

### Standards

- **ISO 639**: Language codes
- **ISO 3166**: Country codes
- **Unicode**: Character encoding
- **CLDR**: Locale data

### Translation Communities

- **Translatewiki.net**: Open translation platform
- **Crowdin**: Collaborative translation
- **Weblate**: Free software translation

### Style Guides

- **Microsoft Language Portal**: Terminology
- **Google Developer Style Guide**: Technical writing
- **W3C Internationalization**: Web standards

### Testing Tools

- **BrowserStack**: Multi-language testing
- **Language Tool**: Grammar checking (many languages)
- **Pseudolocalization**: Test for i18n issues

---

##  Quick Checklist

Before Publishing Translation:

**Content**:
- [ ] All text translated
- [ ] Technical terms consistent
- [ ] Examples culturally adapted
- [ ] Numbers/units localized

**Quality**:
- [ ] Native speaker reviewed
- [ ] Grammar checked
- [ ] Readability appropriate
- [ ] No machine translation artifacts

**Technical**:
- [ ] UTF-8 encoding
- [ ] Markdown valid
- [ ] Links working
- [ ] Math renders correctly

**Metadata**:
- [ ] Language code correct
- [ ] Translator credited
- [ ] Review date recorded
- [ ] Status marked

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintainer**: WorldSMEGraphs Team
