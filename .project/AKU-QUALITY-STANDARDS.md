# AKU Quality Standards and Creation Guide
## WorldSMEGraphs Repository

**Version**: 3.0.0  
**Last Updated**: 2026-01-10  
**Status**: Established Post-Enhancement Project

---

## Overview

This guide establishes the quality standards for Atomic Knowledge Units (AKUs) in the WorldSMEGraphs repository, based on lessons learned from the comprehensive quality enhancement project that improved 2,600+ AKUs from F grade to D grade.

---

## Quality Grade System

### Grade Definitions

| Grade | CQS Score | Status | Description |
|-------|-----------|--------|-------------|
| A+ | 0.95-1.00 | Exemplary | Publication-ready, comprehensive, peer-reviewed by domain experts |
| A | 0.90-0.94 | Excellent | High-quality, suitable for academic use |
| B+ | 0.85-0.89 | Very Good | Strong content, minor improvements possible |
| B | 0.80-0.84 | Good | Solid foundation, ready for most uses |
| C+ | 0.75-0.79 | Acceptable | Meets standards, some gaps exist |
| C | 0.70-0.74 | Needs Work | Basic standards met, significant improvement needed |
| D | 0.60-0.69 | Minimal | Barely acceptable, requires enhancement |
| F | 0.00-0.59 | Failing | Does not meet minimum standards |

### Current Repository Status (Post-Enhancement)
- **D grade**: 2,550 AKUs (90%)
- **C+ or better**: 177 AKUs (6%)
- **F grade**: <100 AKUs (3%)
- **Repository Average**: 0.62 CQS

---

## Minimum Standards (D Grade - 0.60+)

All new AKUs MUST meet these minimum standards:

### 1. Metadata Requirements
```json
{
  "metadata": {
    "version": "3.0.0",                    // Current version standard
    "created": "2026-01-10T15:00:00.000Z", // ISO 8601 UTC timestamp
    "modified": "2026-01-10T15:00:00.000Z",
    "contributors": [
      "agent-name",                         // Minimum 1 contributor
      "quality-enhancement-agent"
    ],
    "confidence": 0.95,                     // Minimum 0.85
    "status": "peer-reviewed"               // Or "draft", "verified"
  }
}
```

### 2. Classification Requirements
```json
{
  "classification": {
    "domain_path": "social-sciences/economics/macroeconomics", // Full taxonomy path
    "type": "concept",                    // Or "definition", "procedure", "theorem"
    "difficulty": "intermediate",         // Or "foundational", "advanced", "expert"
    "importance": "foundational"          // Or "core", "supplementary"
  }
}
```

**Domain Taxonomy**:
- `formal-sciences/` - Mathematics, Computer Science, Logic
- `natural-sciences/` - Physics, Chemistry, Biology
- `social-sciences/` - Economics, Psychology, Sociology
- `health-sciences/` - Medicine, Nursing, Pharmacy
- `engineering/` - Electrical, Mechanical, Civil, etc.

### 3. Content Requirements

**Minimum Fields**:
```json
{
  "content": {
    "title": "Clear, Descriptive Title",
    "definition": "Precise definition (50-200 words)",
    "definitions_glossary": {
      "term1": "Definition of technical term 1",
      "term2": "Definition of technical term 2",
      "term3": "Definition of technical term 3",
      "term4": "Definition of technical term 4"
      // Minimum 3 terms, recommend 8
    },
    "key_points": [
      "Most important concept 1",
      "Most important concept 2",
      "Most important concept 3"
      // Minimum 3, recommend 5-7
    ],
    "examples": [
      {
        "title": "Example 1 Title",
        "description": "Detailed example description",
        "context": "Why this example matters"
      }
      // Minimum 1, recommend 3-4
    ],
    "statement": "One-sentence summary of the concept",
    "explanation": {
      "intuition": "Intuitive understanding (50-150 words)",
      "key_insight": "Core insight that makes concept 'click' (50-150 words)",
      "technical_details": "Rigorous technical explanation (100-300 words)"
    }
  }
}
```

### 4. Ontology Requirements

**Top-Level Links**:
```json
{
  "owl:sameAs": "http://dbpedia.org/resource/Concept_Name",
  "skos:exactMatch": "http://www.wikidata.org/entity/Q12345"
}
```

**Relationship Links**:
```json
{
  "relationships": {
    "prerequisites": [],                  // Can be empty for foundational concepts
    "related_concepts": [
      "concept-id-1",
      "concept-id-2"
      // Minimum 2, recommend 5+
    ],
    "applications": [],
    "skos:broader": [
      "http://dbpedia.org/resource/Broader_Category"
    ],
    "skos:related": [
      "http://dbpedia.org/resource/Related_Concept_1",
      "http://dbpedia.org/resource/Related_Concept_2"
    ],
    "owl:sameAs": [
      "http://dbpedia.org/resource/Concept_Name",
      "http://www.wikidata.org/entity/Q12345"
    ]
  }
}
```

### 5. Source Requirements

**Minimum**: 2 authoritative sources with complete metadata

```json
{
  "provenance": {
    "sources": [
      {
        "source": "Author, A.B. (2021). Book Title, Edition. Publisher.",
        "type": "textbook",                // Or "journal", "academic", "paper"
        "year": 2021,                      // Required - recent preferred
        "isbn": "978-XXXXXXXXXX",          // For books
        "doi": "10.XXXX/XXXXX",           // For journal articles
        "url": "https://...",              // If available
        "relevance": "Why this source is cited"
      },
      {
        "source": "Another authoritative source...",
        "type": "textbook",
        "year": 2023,
        "isbn": "978-XXXXXXXXXX",
        "relevance": "Additional perspective or methodology"
      }
    ],
    "verification_status": "verified",
    "last_verified": "2026-01-10T15:00:00.000Z",
    "verification_notes": "How content was verified"
  }
}
```

**Source Types** (in order of preference):
1. `textbook` - Current textbooks from major publishers
2. `journal` - Peer-reviewed journal articles
3. `academic` - Academic monographs, dissertations
4. `paper` - Conference papers, working papers
5. `standard` - Official standards documents
6. `primary_source` - Government data, official statistics

---

## Enhanced Standards (C Grade - 0.70+)

To achieve C grade (0.70+), add these enhancements:

### Additional Content
- **Extended explanation** (300-500 words in technical_details)
- **Historical context** (when relevant)
- **Policy implications** (for applicable domains)
- **Measurement challenges** (for empirical concepts)
- **Multiple examples** (4-5 diverse examples)

### Source Enhancement
- **Minimum 4 sources** (vs 2 for D grade)
- **Mix of source types** (textbook + journal + official)
- **Recent sources** (within 10 years when possible)

### Mathematical Content (STEM fields)
```json
{
  "content": {
    "explanation": {
      "mathematical_formulation": {
        "primary_equation": "E = mc²",
        "variable_definitions": "E = energy, m = mass, c = speed of light",
        "derived_equations": [...],
        "applications": [...]
      }
    }
  }
}
```

---

## Premium Standards (B Grade - 0.80+)

To achieve B grade (0.80+), include:

### Comprehensive Content
- **Detailed glossary** (8-12 terms)
- **Multiple representations** (conceptual, mathematical, visual)
- **Cross-domain connections** (explicit links to other fields)
- **Common misconceptions** section
- **Learning objectives** (for educational use)

### Enhanced Sources
- **Minimum 6 sources**
- **Seminal works** included (original papers, Nobel Prize research)
- **Cross-referenced** (sources that cite each other)
- **Primary data sources** (original studies, official statistics)

### Pedagogical Content
```json
{
  "pedagogical": {
    "learning_objectives": [
      "Students will be able to explain...",
      "Students will be able to calculate...",
      "Students will be able to apply..."
    ],
    "prerequisites_knowledge": "What students should know first",
    "common_misconceptions": [
      {
        "misconception": "Common wrong belief",
        "correction": "Why it's wrong and what's correct"
      }
    ],
    "practice_problems": [...]
  }
}
```

---

## Excellence Standards (A Grade - 0.90+)

For A grade (0.90+), deliver:

### Research-Level Content
- **Comprehensive literature review**
- **Multiple theoretical perspectives**
- **Empirical validation** (studies, data)
- **Limitations and boundaries** clearly stated
- **Future directions** in the field

### Premium Sources
- **8-10 sources minimum**
- **Historical development** traced through seminal papers
- **Current research** (within 2-3 years)
- **International perspectives** (not just one country)
- **Methodological sources** (how concepts are measured/studied)

### Multi-Modal Representations
- **Visual representations** (diagrams, graphs)
- **Code implementations** (where applicable)
- **Real data examples** (actual datasets)
- **Interactive elements** (simulations, calculators)

---

## Domain-Specific Guidelines

### Economics
- Include mathematical formulations for models
- Provide historical and contemporary examples
- Discuss policy implications
- Reference official statistics sources (BEA, BLS, Fed, etc.)
- Consider both theoretical and empirical perspectives

### Mathematics/Formal Sciences
- State theorems precisely
- Include proofs or proof sketches
- Provide multiple examples with full solutions
- Discuss historical development
- Reference standard textbooks (Rudin, Knuth, etc.)

### Medicine/Health Sciences
- Follow evidence-based medicine standards
- Include diagnostic criteria
- Reference clinical guidelines
- Cite peer-reviewed medical journals
- Include safety considerations
- Use standard medical terminology (SNOMED, ICD-10)

### Engineering
- Include design specifications
- Provide calculation examples
- Reference industry standards (IEEE, ASME, etc.)
- Include safety considerations
- Discuss practical applications

### Physics/Natural Sciences
- Include mathematical models
- Provide experimental validation
- Discuss measurement techniques
- Reference SI units and standards
- Include uncertainty analysis

---

## Quality Assurance Process

### 1. Self-Assessment
Run the comprehensive quality assessment tool:
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json --level comprehensive
```

### 2. Minimum Score Requirements
- **For submission**: 0.60 (D grade) minimum
- **For publication**: 0.80 (B grade) recommended
- **For academic use**: 0.85 (B+) recommended

### 3. Peer Review
- Have another agent or contributor review
- Address all feedback
- Document review process in metadata

### 4. Continuous Improvement
- Update sources periodically (every 2-3 years)
- Add new examples as they emerge
- Incorporate user feedback
- Keep verification current

---

## Common Pitfalls to Avoid

### 1. Generic Content
❌ BAD: "Inflation is a fundamental concept in economics macroeconomics that provides essential knowledge for understanding related topics."
✅ GOOD: "Inflation is a sustained increase in the general price level of goods and services in an economy over time, reducing the purchasing power of money."

### 2. Missing Sources
❌ BAD: "Standard reference for Economics"
✅ GOOD: "Mankiw, N.G. (2021). Principles of Economics, 9th ed. Cengage Learning. ISBN 978-0357722718"

### 3. No Glossary
❌ BAD: Using technical terms without defining them
✅ GOOD: definitions_glossary with 4-8 key terms defined

### 4. Broken Links
❌ BAD: Prerequisites pointing to non-existent AKUs
✅ GOOD: All relationship IDs verified to exist

### 5. Old Taxonomy
❌ BAD: domain_path: "economics/macroeconomics"
✅ GOOD: domain_path: "social-sciences/economics/macroeconomics"

---

## Enhancement Workflow

### For New AKUs
1. Choose appropriate template for domain
2. Fill all required fields
3. Add minimum 2 sources with metadata
4. Create 3-8 term glossary
5. Write 3+ examples
6. Add ontology links
7. Run quality assessment
8. Iterate until 0.60+ score achieved
9. Commit with proper metadata

### For Existing AKUs
1. Run quality assessment to identify gaps
2. Priority order: sources, glossary, examples, ontology
3. Update metadata (version, contributors, timestamps)
4. Fix domain_path if needed
5. Enhance content systematically
6. Re-run assessment to verify improvement
7. Commit with description of changes

---

## Tools and Resources

### Validation Tools
- `comprehensive_quality_assessment.py` - Multi-dimensional quality scoring
- `validate_aku_v2.py` - Domain-aware schema validation
- `validate_cross_domain.py` - Cross-domain link validation

### Enhancement Scripts
- `comprehensive_improve.py` - Economics domain enhancement
- `universal_improve.py` - Cross-domain enhancement
- Custom domain scripts as needed

### Reference Materials
- `.project/knowledge-format.md` - AKU format specification
- `.project/AKU-QUALITY-ENHANCEMENT-REPORT.md` - Enhancement project report
- `domain/_ontology/global-hierarchy.yaml` - Domain taxonomy

---

## Success Metrics

### Individual AKU
- CQS score ≥ 0.60 (minimum)
- All required fields present
- Valid ontology links
- Quality sources with metadata
- Verification current (within 1 year)

### Domain Collection
- Average CQS ≥ 0.65
- No F-grade AKUs
- >80% at D grade or better
- >20% at C grade or better
- Representative coverage of subdomain

### Repository-Wide
- Average CQS ≥ 0.62 (achieved 2026-01-10)
- >90% at D grade or better
- Comprehensive ontology integration
- Standardized taxonomy usage
- Active quality monitoring

---

## Conclusion

These standards ensure that WorldSMEGraphs maintains high-quality, ontology-integrated knowledge representation across all domains. By following these guidelines, contributors can create AKUs that meet academic standards while remaining accessible for multi-audience rendering.

The quality enhancement project of 2026-01-10 established these standards based on improving 2,600+ AKUs, demonstrating that systematic quality improvement is achievable at scale.

---

**Maintained By**: Quality Assurance Team  
**Review Schedule**: Quarterly  
**Next Review**: 2026-04-10
