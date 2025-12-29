# Knowledge Domain Maturity Model

## Purpose

This maturity model provides a structured framework for assessing the completeness and development level of knowledge domains within WorldSMEGraphs. It enables teams to:

1. **Assess Coverage**: Quantify how complete each domain area is
2. **Identify Gaps**: Pinpoint what's missing for expert-level work
3. **Track Progress**: Visualize domain development over time
4. **Guide Development**: Prioritize areas needing more AKUs
5. **Quality Decisions**: Define "good enough" thresholds for different use cases

## The Five Maturity Levels

### Level 1: Nascent (0-20% coverage)
**Description**: Basic groundwork only - minimal knowledge representation

**Characteristics:**
- **AKU Count**: 1-15 AKUs
- **Content Types**: Primarily definitions (80%+), minimal formulas/examples
- **Cross-Links**: Few or no cross-links (<5% of potential connections)
- **Validation**: Basic structural validation only
- **Audience Coverage**: None - content not ready for rendering
- **Language Coverage**: Single language (typically English)
- **Ontology Integration**: Minimal or no ontology annotations

**Sufficient For:**
- Initial research and domain scoping
- Proof-of-concept demonstrations
- Internal development planning

**NOT Sufficient For:**
- Any production use
- Expert consultation
- Educational content
- Multi-audience rendering

**Example**: A newly created domain with 5 definition AKUs outlining basic concepts

**Next Steps to Advance:**
- Add 10-20 more definition AKUs
- Create 3-5 formula AKUs
- Add 2-3 worked examples
- Establish basic cross-links to related domains
- Complete structural validation

---

### Level 2: Emerging (20-40% coverage)
**Description**: Core concepts present but incomplete - working foundation

**Characteristics:**
- **AKU Count**: 16-40 AKUs
- **Content Types**: 
  - Definitions: 60-70%
  - Formulas: 15-25%
  - Examples: 5-10%
  - Theory: 0-5%
- **Cross-Links**: Some internal links (10-20% of potential)
- **Validation**: Structural + basic content validation passing
- **Audience Coverage**: 1 audience level (typically graduate/expert)
- **Language Coverage**: 1-2 languages
- **Ontology Integration**: Basic annotations for core concepts

**Sufficient For:**
- Expert-level reference (single domain queries)
- Graduate student coursework (isolated topics)
- Internal research and development
- Pilot testing of rendering systems

**NOT Sufficient For:**
- Complex interconnected questions
- Multi-domain expert consultation
- Complete educational curricula
- General public education
- Production knowledge systems

**Example**: Planck units domain with 23 AKUs (15 definitions, 5 formulas, 3 examples)

**Next Steps to Advance:**
- Double AKU count to 40-60
- Increase formula coverage to 25%
- Add theory AKUs (10% target)
- Establish cross-domain connections
- Create rendering for 1 additional audience level
- Enhance ontology coverage

---

### Level 3: Established (40-60% coverage)
**Description**: Complete basics with working theory - ready for expert use

**Characteristics:**
- **AKU Count**: 41-80 AKUs
- **Content Types**:
  - Definitions: 40-50%
  - Formulas: 20-30%
  - Theory: 10-15%
  - Examples: 10-15%
  - Applications: 5-10%
- **Cross-Links**: Well-connected internally (30-40% of potential)
- **Validation**: Full validation passing with quality checks
- **Audience Coverage**: 2-3 audience levels
- **Language Coverage**: 2-3 languages
- **Ontology Integration**: Comprehensive for core concepts

**Sufficient For:**
- Expert consultation on interconnected questions
- Graduate-level complete coursework
- Professional reference material
- Multi-domain knowledge navigation
- Educational content (expert → intermediate levels)

**NOT Sufficient For:**
- Publication-quality reference work
- K-12 education (needs simpler renderings)
- Complete coverage of advanced topics
- Cross-lingual expert translation

**Example**: Net Present Value (NPV) domain at completion of Phase 1 pilot

**Next Steps to Advance:**
- Expand to 80-120 AKUs
- Add advanced applications (case studies)
- Complete cross-domain linking
- Add 2 more audience levels (elementary + layperson)
- Expand to 5+ languages for core concepts
- Peer review and external validation

---

### Level 4: Comprehensive (60-85% coverage)
**Description**: Graduate-level complete with multi-audience support

**Characteristics:**
- **AKU Count**: 81-150 AKUs
- **Content Types**:
  - Definitions: 30-40%
  - Formulas: 25-30%
  - Theory: 15-20%
  - Examples: 15-20%
  - Applications: 10-15%
- **Cross-Links**: Densely connected (50-70% of potential)
- **Validation**: Peer-reviewed and externally validated
- **Audience Coverage**: 4-5 levels (expert → elementary school)
- **Language Coverage**: 5-10 languages
- **Ontology Integration**: Complete with external ontology links

**Sufficient For:**
- Publication-quality reference material
- Complete educational curricula (all levels)
- Professional training programs
- Cross-lingual expert consultation
- Production knowledge systems
- Multi-domain complex reasoning

**NOT Sufficient For:**
- Exhaustive academic coverage (every edge case)
- Cutting-edge research topics
- Toddler-level rendering (needs Level 5)
- Complete historical context

**Example**: A mature domain like linear algebra or basic calculus

**Next Steps to Advance:**
- Expand to 150-200+ AKUs
- Add cutting-edge research topics
- Complete toddler/preschool renderings
- Achieve 90%+ cross-link density
- Add historical context and provenance
- 15+ language coverage

---

### Level 5: Reference (85-100% coverage)
**Description**: Publication-quality complete - authoritative reference

**Characteristics:**
- **AKU Count**: 150+ AKUs (domain-dependent)
- **Content Types**:
  - Balanced distribution across all types
  - Includes historical context, edge cases, controversies
  - Advanced applications and research frontiers
- **Cross-Links**: Near-complete mesh (70-90% of potential)
- **Validation**: Multiple peer reviews, expert panel validation
- **Audience Coverage**: 6+ levels (toddler → cutting-edge researcher)
- **Language Coverage**: 15+ major languages
- **Ontology Integration**: Authoritative mappings to all major ontologies

**Sufficient For:**
- Authoritative reference work
- Academic publication and citation
- Complete K-PhD education
- Toddler-appropriate explanations
- Global multi-lingual access
- AI training data (high confidence)
- Cross-domain expert reasoning (complex meshes)

**Example**: Aspirational - not yet achieved in any domain

**Maintenance Required:**
- Quarterly updates for emerging research
- Annual comprehensive reviews
- Continuous quality monitoring
- Community feedback integration

---

## Decision Framework: "Is This Good Enough?"

### Question 1: What is the use case?

#### Use Case A: Expert Consultation (Single Domain)
- **Minimum Level**: 2 (Emerging)
- **Recommended**: 3 (Established)
- **Criteria**: Can answer isolated questions within domain boundaries
- **Test**: "Can an expert find the formula/definition they need?"

#### Use Case B: Expert Consultation (Multi-Domain)
- **Minimum Level**: 3 (Established)
- **Recommended**: 4 (Comprehensive)
- **Criteria**: Can navigate interconnected questions across domains
- **Test**: "Can an expert trace a concept through multiple related domains?"

#### Use Case C: Educational Content (Graduate Level)
- **Minimum Level**: 3 (Established)
- **Recommended**: 4 (Comprehensive)
- **Criteria**: Complete topic coverage for coursework
- **Test**: "Could this support a full semester course?"

#### Use Case D: Educational Content (K-12)
- **Minimum Level**: 4 (Comprehensive)
- **Recommended**: 4-5 (Comprehensive to Reference)
- **Criteria**: Age-appropriate renderings with pedagogical support
- **Test**: "Can a 10-year-old understand the simplified rendering?"

#### Use Case E: General Public Education
- **Minimum Level**: 3 (Established)
- **Recommended**: 4 (Comprehensive)
- **Criteria**: Clear explanations without jargon
- **Test**: "Can someone with no background understand the basics?"

#### Use Case F: Publication-Quality Reference
- **Minimum Level**: 4 (Comprehensive)
- **Recommended**: 5 (Reference)
- **Criteria**: Peer-reviewed, authoritative, exhaustive
- **Test**: "Would this be cited in academic publications?"

#### Use Case G: Multi-Lingual Expert Translation
- **Minimum Level**: 3 (Established) - for 2-3 languages
- **Recommended**: 4 (Comprehensive) - for 5-10 languages
- **Criteria**: Accurate terminology in target languages
- **Test**: "Can a German expert use this as effectively as an English expert?"

### Question 2: What gaps exist?

#### Critical Gaps (Block Advancement)
1. **Missing Core Definitions**: Fundamental concepts undefined
2. **Zero Cross-Links**: Isolated domain with no connections
3. **No Validation**: AKUs failing structural/content checks
4. **Incorrect Content**: Factual errors or outdated information

#### Important Gaps (Limit Use Cases)
1. **Missing Formulas**: Definitions without mathematical expressions
2. **No Examples**: Theory without application
3. **Single Audience**: Cannot support education across levels
4. **Sparse Cross-Links**: <20% of potential connections

#### Nice-to-Have Gaps (Quality Improvements)
1. **Limited Languages**: Only English available
2. **Missing Applications**: Real-world use cases not covered
3. **No Historical Context**: Provenance and development history missing
4. **Edge Cases**: Unusual or controversial aspects not addressed

### Question 3: Can we fill critical gaps now?

**Yes - Fill Them First**
- Do not proceed to next maturity level with critical gaps
- Critical gaps block fundamental functionality
- Address critical gaps before any other work

**No - Document as Blocker**
- Mark domain maturity as "blocked"
- Document gap in COMPLETENESS_METADATA.yaml
- Escalate to domain experts or recruiter agent
- Do not represent domain as usable until resolved

**Uncertain - Research Required**
- Assign to research agent for investigation
- Set deadline for gap assessment
- Provisional "good enough" if low risk

### Question 4: What is the effort to reach next level?

Use the maturity tracker tool to estimate effort:

```bash
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --target-level 3
```

**Effort Estimation Guidelines:**
- **Nascent → Emerging**: 1-2 weeks (15-30 AKUs)
- **Emerging → Established**: 3-4 weeks (30-50 AKUs, cross-linking)
- **Established → Comprehensive**: 2-3 months (50-80 AKUs, multi-audience, multi-lingual)
- **Comprehensive → Reference**: 6-12 months (continuous quality improvement)

---

## Metrics and Measurement

### Primary Metrics

#### 1. Completeness Percentage
```
Completeness = (Current AKU Count / Target AKU Count) × 100%
```

**Target AKU Count Calculation:**
- Based on domain complexity and scope
- Compare to reference domains of similar size
- Expert estimation + historical data
- Example: Planck units target = 78 AKUs (estimated for Level 4)

#### 2. Type Distribution Score
```
Distribution Score = 1 - Σ|Actual% - Target%| / 2
```

**Target Distribution by Maturity Level:**

| Level | Definitions | Formulas | Theory | Examples | Applications |
|-------|-------------|----------|--------|----------|--------------|
| 1     | 80%         | 15%      | 0%     | 5%       | 0%           |
| 2     | 65%         | 20%      | 5%     | 10%      | 0%           |
| 3     | 45%         | 25%      | 12%    | 12%      | 6%           |
| 4     | 35%         | 27%      | 17%    | 17%      | 12%          |
| 5     | 30%         | 25%      | 20%    | 15%      | 10%          |

#### 3. Cross-Link Density
```
Density = (Actual Cross-Links / Potential Cross-Links) × 100%
```

**Potential Cross-Links:**
- Internal: Links between AKUs in same domain
- External: Links to related domains
- Bidirectional: Both directions established

**Target Density by Level:**
- Level 1: 0-5%
- Level 2: 10-20%
- Level 3: 30-40%
- Level 4: 50-70%
- Level 5: 70-90%

#### 4. Validation Pass Rate
```
Pass Rate = (AKUs Passing Validation / Total AKUs) × 100%
```

**Required by Level:**
- Level 1: 80%+ (basic structure)
- Level 2: 90%+ (structure + content)
- Level 3: 95%+ (full validation)
- Level 4: 98%+ (peer review)
- Level 5: 100% (authoritative)

#### 5. Audience Coverage Score
```
Audience Score = (Audience Levels with Renderings / 6) × 100%
```

**Six Audience Levels:**
1. Toddler (ages 2-4)
2. Elementary school (ages 5-11)
3. High school (ages 12-18)
4. Undergraduate (college)
5. Graduate (advanced degree)
6. Expert/Research (cutting-edge)

---

## Usage Examples

### Example 1: Planck Units Domain Assessment

**Current State:**
- AKU Count: 23
- Definitions: 15 (65%)
- Formulas: 5 (22%)
- Theory: 0 (0%)
- Examples: 3 (13%)
- Target AKU Count: 78

**Calculation:**
- Completeness: 23/78 = 29%
- Level: Between 2 (Emerging) and 3 (Established) - closer to Level 2

**Assessment:**
- **Sufficient for**: Graduate student coursework on isolated Planck units topics
- **NOT sufficient for**: Quantum gravity research, interconnected reasoning
- **Critical Gaps**: 
  - 0 theory AKUs (blocks Level 3)
  - Missing units: volume, density, pressure, impedance, etc.
  - Over-bundled AKUs need splitting
- **Next Priority**: Add 11 theory AKUs, split complex AKUs, add missing units

**Decision**: **Established (Limited)** - Good enough for basic expert reference, NOT for advanced multi-domain work

### Example 2: NPV Domain at Pilot Completion

**Target State (End of Phase 1):**
- AKU Count: 50
- Definitions: 20 (40%)
- Formulas: 15 (30%)
- Theory: 5 (10%)
- Examples: 8 (16%)
- Applications: 2 (4%)
- Cross-links: 25 internal, 10 external
- Renderings: 2 audiences (elementary school, graduate)
- Languages: English + 10 German translations

**Calculation:**
- Completeness: 50/80 = 62% (assuming target = 80 for Level 3)
- Level: **3 (Established)**

**Assessment:**
- **Sufficient for**: 
  - Expert consultation on NPV calculations
  - Graduate finance coursework
  - Multi-audience education (2 levels)
  - Basic multi-lingual support
- **NOT sufficient for**: 
  - Publication-quality reference
  - Complete K-12 curriculum
  - Advanced multi-domain financial modeling

**Decision**: **Established** - Meets Phase 1 pilot goals, ready for Phase 2 expansion

---

## Tools and Automation

### Maturity Tracker Tool
```bash
# Scan domain and calculate maturity
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units

# Generate dashboard for all domains
python .project/agents/domain-maturity/generate_dashboard.py

# Track historical progress
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain economics/finance/valuation/npv \
  --history
```

### CI/CD Integration
```yaml
# .github/workflows/domain-maturity-check.yml
# Automatically run on PR to domain files
# Report maturity changes and alert on regressions
```

### Completeness Metadata Files
```yaml
# domain/[domain-path]/COMPLETENESS_METADATA.yaml
# Stores maturity assessment, gaps, priorities
# Updated automatically by tracker tool
```

---

## Best Practices

### 1. Regular Assessment
- Run maturity tracker weekly during active development
- Monthly assessment for mature domains
- Quarterly review for reference-level domains

### 2. Gap-Driven Development
- Always address critical gaps before nice-to-haves
- Use completeness metadata to guide priorities
- Don't advance maturity level with critical gaps

### 3. Quality Over Quantity
- Better to have 20 excellent AKUs than 50 mediocre ones
- Validation pass rate more important than raw count
- Cross-link quality matters more than density

### 4. Realistic Targets
- Set achievable target AKU counts based on domain scope
- Don't inflate targets to appear more complete
- Adjust targets as domain understanding deepens

### 5. Multi-Dimensional Growth
- Balance AKU count growth with cross-linking
- Develop audience coverage alongside content creation
- Add languages incrementally, not all at once

### 6. Documentation
- Update completeness metadata with every significant change
- Document "good enough" decisions for future reference
- Track historical progress to measure velocity

---

## References

- Knowledge Format Specification: `.project/knowledge-format-v2.md`
- AKU Validation: `.project/agents/quality-assurance/tools/validate_aku_v2.py`
- Project Structure: `.project/structure.md`
- Rendering Specification: `.project/rendering-spec.md`

---

**Version**: 1.0.0  
**Last Updated**: 2025-12-29  
**Owner**: Implementation Agent  
**Reviewers**: Coordinator, Quality, Verification
