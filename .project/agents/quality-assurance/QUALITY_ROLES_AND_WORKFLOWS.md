# Quality Roles and Workflows

## Overview

This document defines **WHO does WHAT** in the quality review process. It specifies:
- The type of expert needed for each task
- The tools required
- The knowledge prerequisites
- The workflow triggers and outputs

---

## Quality Roles

### 1. Domain Subject Matter Expert (SME)

**Who**: Medical doctor, PhD researcher, or certified professional in the specific domain

**What They Do**:
- Create new AKUs from original knowledge
- Review content accuracy for their specialty area
- Validate clinical relevance and correctness
- Identify missing prerequisite knowledge
- Approve final content before publication

**Tools They Use**:
- Text editor for AKU creation
- Reference management (Zotero, Mendeley)
- Domain-specific resources (UpToDate, PubMed)

**Knowledge Required**:
- Board certification or equivalent in specialty
- Current clinical practice (within 5 years)
- Understanding of educational standards for the domain
- Familiarity with AKU JSON format (training provided)

**Trigger**: New AKU creation, content accuracy questions, annual recertification review

**Output**: Validated AKU content, accuracy sign-off, correction requests

---

### 2. Ontology Specialist

**Who**: Information scientist, knowledge engineer, or librarian with taxonomy experience

**What They Do**:
- Validate AKU placement in domain hierarchy
- Check classification.domain_path accuracy
- Verify cross-domain links are valid
- Ensure terminology consistency
- Review relationship integrity (requires/enables)

**Tools They Use**:
- `domain/_ontology/global-hierarchy.yaml` - Master taxonomy reference
- `python domain/_ontology/tools/validate_cross_domain.py` - Link validation
- `python .project/agents/quality-assurance/tools/validate_ontology.py` - Ontology compliance
- Graph visualization tools (optional)

**Knowledge Required**:
- Understanding of ontology principles (SKOS, OWL basics)
- Familiarity with WorldSMEGraphs domain hierarchy
- Knowledge of cross-domain linking patterns
- JSON-LD context understanding

**Trigger**: New AKU creation, domain reorganization, cross-domain link addition

**Output**: Ontology validation report, reclassification recommendations

---

### 3. Fact-Checker

**Who**: Research librarian, medical editor, or trained verification specialist

**What They Do**:
- Verify claims against authoritative sources
- Check citation accuracy and accessibility
- Validate numerical data and statistics
- Confirm formulas and calculations
- Flag unsupported or questionable claims

**Tools They Use**:
- `python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py --dimension fact_accuracy`
- PubMed, Google Scholar for literature search
- Authoritative source databases (SNOMED-CT, ICD-10)
- Citation verification tools

**Knowledge Required**:
- Research methodology training
- Understanding of evidence hierarchies
- Familiarity with domain literature sources
- Critical appraisal skills

**Trigger**: New AKU creation, external error report, scheduled reassessment

**Output**: Fact-check report with citations, accuracy score, error list

---

### 4. Reference Librarian

**Who**: Medical librarian, citation specialist, or research assistant

**What They Do**:
- Validate citation format compliance
- Verify source accessibility (URLs, DOIs)
- Check publication dates and author accuracy
- Assess source authority and reliability
- Identify missing references for claims

**Tools They Use**:
- CrossRef DOI resolver
- PubMed for citation verification
- Web archive (Wayback Machine) for dead links
- Citation format checkers

**Knowledge Required**:
- Citation style standards (APA, Vancouver)
- Understanding of academic publishing
- Source evaluation skills
- Database search proficiency

**Trigger**: New AKU creation, reference decay check (quarterly)

**Output**: Reference validation report, dead link list, format corrections

---

### 5. Pedagogy Reviewer

**Who**: Education specialist, curriculum developer, or instructional designer

**What They Do**:
- Evaluate learning objectives clarity
- Check prerequisite accuracy and completeness
- Assess difficulty level appropriateness
- Review example quality and relevance
- Validate learning progression

**Tools They Use**:
- Learning objective taxonomies (Bloom's)
- Prerequisite mapping tools
- Readability calculators
- Example quality rubrics

**Knowledge Required**:
- Instructional design principles
- Learning theory (constructivism, cognitive load)
- Assessment design
- Audience analysis skills

**Trigger**: New AKU creation, audience rendering request, curriculum mapping

**Output**: Pedagogy assessment, learning path recommendations, example improvements

---

### 6. Third-Party Verifier

**Who**: External consultant, independent reviewer, or peer institution expert

**What They Do**:
- Independent content validation
- Cross-institutional comparison
- Bias detection and mitigation
- Competing interpretation review
- Final quality sign-off for high-stakes content

**Tools They Use**:
- Independent reference sources
- Peer review forms
- Blind review protocols
- Quality attestation templates

**Knowledge Required**:
- Domain expertise (matching SME level)
- No conflict of interest with content creators
- Understanding of verification standards
- Academic integrity training

**Trigger**: Grade A+ certification, controversial content, public release

**Output**: Third-party verification certificate, conflict notes, quality attestation

---

### 7. Web Research Specialist

**Who**: Research analyst, information professional, or trained agent

**What They Do**:
- Search current web for contradicting information
- Monitor knowledge currency
- Identify new developments affecting content
- Check for superseding guidelines/research
- Validate against reputable web sources

**Tools They Use**:
- Google Scholar alerts
- PubMed RSS feeds
- Specialty society websites
- News monitoring services
- `@web-scraper` agent for systematic searches

**Knowledge Required**:
- Advanced search techniques
- Source evaluation (CRAAP test)
- Understanding of information recency
- Domain news awareness

**Trigger**: Scheduled currency review, external event notification

**Output**: Currency report, update recommendations, new source list

---

### 8. Quality Coordinator

**Who**: Project manager, quality lead, or senior team member

**What They Do**:
- Assign work to appropriate specialists
- Track quality metrics and trends
- Manage reassessment schedules
- Escalate issues requiring expert decision
- Maintain quality tracking database
- Generate quality reports

**Tools They Use**:
- `python .project/agents/quality-assurance/tools/reassessment_tool.py` - Queue management
- `python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py` - Full assessment
- `.project/tracking/quality-scores.yaml` - Quality database
- Project management tools

**Knowledge Required**:
- Quality management principles
- Understanding of all quality roles
- Familiarity with assessment tools
- Project coordination skills

**Trigger**: Always active (coordination role)

**Output**: Assignment lists, quality reports, trend analyses, escalations

---

## Workflow Definitions

### Workflow 1: New AKU Quality Review

**Purpose**: Ensure new AKUs meet quality standards before integration

```
STEP 1: Initial Creation
  WHO: Domain SME
  WHAT: Creates AKU with original content
  TOOL: Text editor, domain references
  OUTPUT: Draft AKU JSON file
  
STEP 2: Structural Validation
  WHO: Quality Coordinator (automated)
  WHAT: Validate JSON schema and required fields
  TOOL: python validate_aku_v2.py path/to/aku.json
  OUTPUT: Structural validation pass/fail
  
STEP 3: Ontology Check
  WHO: Ontology Specialist
  WHAT: Validate domain_path and relationships
  TOOL: python validate_cross_domain.py path/to/aku.json
  OUTPUT: Ontology validation report
  
STEP 4: Fact Verification
  WHO: Fact-Checker
  WHAT: Verify all claims against sources
  TOOL: PubMed, authoritative sources
  OUTPUT: Fact-check report with score
  
STEP 5: Reference Audit
  WHO: Reference Librarian
  WHAT: Validate all citations
  TOOL: CrossRef, citation checkers
  OUTPUT: Reference validation report
  
STEP 6: Pedagogy Review
  WHO: Pedagogy Reviewer
  WHAT: Assess learning objectives and examples
  TOOL: Learning objective rubrics
  OUTPUT: Pedagogy score and recommendations
  
STEP 7: Final Assessment
  WHO: Quality Coordinator
  WHAT: Calculate composite score, assign grade
  TOOL: python comprehensive_quality_assessment.py
  OUTPUT: Final grade (A+ to F), recommendations
  
STEP 8: Domain SME Sign-off
  WHO: Domain SME (original or different)
  WHAT: Final accuracy approval
  TOOL: Review assessment reports
  OUTPUT: Approval or revision request
```

**Timeline**: 2-5 business days depending on complexity

---

### Workflow 2: Reassessment Review

**Purpose**: Update quality scores for existing AKUs based on triggers

```
STEP 1: Trigger Detection
  WHO: Quality Coordinator (or automated)
  WHAT: Identify AKUs due for reassessment
  TOOL: python reassessment_tool.py --priority-queue
  OUTPUT: Prioritized reassessment list
  
STEP 2: Dimension-Specific Review
  WHO: Varies by lowest-scoring dimension
  WHAT: Focus improvement on weak areas
  TOOL: Dimension-specific tools
  OUTPUT: Improvement recommendations
  
  IF lowest = fact_accuracy: Assign Fact-Checker
  IF lowest = ontology: Assign Ontology Specialist
  IF lowest = references: Assign Reference Librarian
  IF lowest = pedagogy: Assign Pedagogy Reviewer
  IF lowest = currency: Assign Web Research Specialist
  
STEP 3: Update Implementation
  WHO: Domain SME or assigned specialist
  WHAT: Apply recommended improvements
  TOOL: Text editor, reference sources
  OUTPUT: Updated AKU file
  
STEP 4: Re-score
  WHO: Quality Coordinator
  WHAT: Recalculate quality score
  TOOL: python comprehensive_quality_assessment.py
  OUTPUT: New grade, improvement delta
  
STEP 5: History Update
  WHO: Quality Coordinator (automated)
  WHAT: Log reassessment in quality history
  TOOL: python reassessment_tool.py --log
  OUTPUT: Updated quality-scores.yaml
```

**Timeline**: 1-3 business days per AKU

---

### Workflow 3: Third-Party Verification

**Purpose**: Independent validation for high-stakes or controversial content

```
STEP 1: Eligibility Check
  WHO: Quality Coordinator
  WHAT: Determine if third-party review needed
  CRITERIA:
    - Target grade A+ certification
    - Controversial or contested content
    - Public release or external use
    - New domain launch
  OUTPUT: Verification request or bypass approval
  
STEP 2: Reviewer Selection
  WHO: Quality Coordinator
  WHAT: Identify qualified external reviewer
  CRITERIA:
    - Domain expertise matching SME level
    - No conflict of interest
    - Available within timeline
  OUTPUT: Reviewer assignment, NDA if needed
  
STEP 3: Blind Review
  WHO: Third-Party Verifier
  WHAT: Independent content evaluation
  TOOL: Review checklist, independent sources
  OUTPUT: Verification report, discrepancy list
  
STEP 4: Discrepancy Resolution
  WHO: Domain SME + Third-Party Verifier
  WHAT: Resolve any conflicting assessments
  TOOL: Conference call or written exchange
  OUTPUT: Resolved position, updated content
  
STEP 5: Certification
  WHO: Third-Party Verifier + Quality Coordinator
  WHAT: Issue verification certificate
  TOOL: Certification template
  OUTPUT: Signed attestation, metadata update
```

**Timeline**: 1-2 weeks for full process

---

### Workflow 4: Supportive AKU Gap Analysis

**Purpose**: Identify missing prerequisite or related AKUs

```
STEP 1: Dependency Mapping
  WHO: Ontology Specialist
  WHAT: Extract all relationship links from AKU
  TOOL: python comprehensive_quality_assessment.py --check-dependencies
  OUTPUT: List of referenced AKUs
  
STEP 2: Existence Verification
  WHO: Quality Coordinator (automated)
  WHAT: Check if all referenced AKUs exist
  TOOL: File system search, concept index lookup
  OUTPUT: Missing AKU list
  
STEP 3: Gap Prioritization
  WHO: Quality Coordinator + Domain SME
  WHAT: Prioritize which missing AKUs to create
  CRITERIA:
    - Number of AKUs depending on missing content
    - Importance for learning path
    - Feasibility of creation
  OUTPUT: Prioritized gap list
  
STEP 4: Creation Assignment
  WHO: Quality Coordinator
  WHAT: Assign gap AKUs to appropriate SMEs
  TOOL: Assignment tracking
  OUTPUT: Work assignments with deadlines
  
STEP 5: Gap Closure Verification
  WHO: Ontology Specialist
  WHAT: Verify new AKUs resolve dependencies
  TOOL: Re-run dependency check
  OUTPUT: Updated relationship graph
```

**Timeline**: Varies by number of gaps

---

### Workflow 5: Web Search Verification

**Purpose**: Validate content against current web sources

```
STEP 1: Source Identification
  WHO: Web Research Specialist
  WHAT: Identify authoritative web sources for domain
  SOURCES:
    - Medical: UpToDate, Mayo Clinic, NICE guidelines
    - Finance: Investopedia, SEC, Federal Reserve
    - Science: Nature, Science, domain journals
  OUTPUT: Source list with URLs
  
STEP 2: Claim Extraction
  WHO: Web Research Specialist (or automated)
  WHAT: Extract verifiable claims from AKU
  TOOL: Content analysis
  OUTPUT: Claim list with current values
  
STEP 3: Web Verification
  WHO: Web Research Specialist
  WHAT: Search for contradicting or supporting info
  TOOL: Google Scholar, specialty databases
  OUTPUT: Verification matrix (claim vs source)
  
STEP 4: Currency Assessment
  WHO: Web Research Specialist
  WHAT: Check if any information is outdated
  CRITERIA:
    - Guidelines superseded
    - Statistics more than 3 years old
    - Practices changed
  OUTPUT: Currency report, update recommendations
  
STEP 5: Update Integration
  WHO: Domain SME
  WHAT: Incorporate verified updates
  TOOL: Text editor
  OUTPUT: Updated AKU with current information
```

**Timeline**: 1-2 days per AKU

---

## Role Assignment Matrix

| Task | Primary Role | Secondary Role | Tool Required |
|------|--------------|----------------|---------------|
| Create new AKU | Domain SME | - | Text editor |
| Structural validation | Quality Coordinator | Automated | validate_aku_v2.py |
| Domain path check | Ontology Specialist | - | validate_cross_domain.py |
| Fact verification | Fact-Checker | Domain SME | PubMed, sources |
| Citation check | Reference Librarian | - | CrossRef, DOI resolver |
| Learning assessment | Pedagogy Reviewer | - | Bloom's taxonomy |
| Currency check | Web Research Specialist | - | Web search tools |
| Third-party review | External Verifier | - | Independent sources |
| Score calculation | Quality Coordinator | Automated | comprehensive_quality_assessment.py |
| Reassessment queue | Quality Coordinator | Automated | reassessment_tool.py |
| Gap analysis | Ontology Specialist | Quality Coordinator | Dependency tools |

---

## Quick Reference: Who To Call

| Issue | Contact This Role |
|-------|-------------------|
| "Is this claim accurate?" | Fact-Checker → Domain SME |
| "Where should this AKU go?" | Ontology Specialist |
| "Is this citation valid?" | Reference Librarian |
| "Is this too advanced for beginners?" | Pedagogy Reviewer |
| "Is this information current?" | Web Research Specialist |
| "Who reviews this AKU?" | Quality Coordinator |
| "Need independent validation" | Third-Party Verifier |
| "What AKUs are we missing?" | Ontology Specialist |

---

## Agent Mappings

For automated workflows, these agents correspond to the roles:

| Human Role | AI Agent | Agent File |
|------------|----------|------------|
| Domain SME | @math-expert, @domain-expert-template | `.github/agents/math-expert.agent.md` |
| Ontology Specialist | @ontology, @semantic-harmonization | `.github/agents/ontology.agent.md` |
| Fact-Checker | @fact-checking, @verification | `.github/agents/fact-checking.agent.md` |
| Reference Librarian | @citation, @citation-extractor | `.github/agents/citation.agent.md` |
| Pedagogy Reviewer | @pedagogy, @assessment-creation | `.github/agents/pedagogy.agent.md` |
| Web Research Specialist | @web-scraper, @research | `.github/agents/web-scraper.agent.md` |
| Third-Party Verifier | @peer-review, @contrarian | `.github/agents/peer-review.agent.md` |
| Quality Coordinator | @quality, @coordinator | `.github/agents/quality.agent.md` |

---

## Training Requirements

### For New Team Members

| Role | Minimum Training |
|------|------------------|
| Domain SME | AKU format training (2 hours) + Domain expertise (existing) |
| Ontology Specialist | Ontology fundamentals (4 hours) + WorldSMEGraphs structure (2 hours) |
| Fact-Checker | Research verification methods (4 hours) + Tool training (2 hours) |
| Reference Librarian | Citation standards (2 hours) + Tool training (1 hour) |
| Pedagogy Reviewer | Instructional design basics (4 hours) + Assessment rubrics (2 hours) |
| Web Research Specialist | Advanced search techniques (2 hours) + Source evaluation (2 hours) |
| Third-Party Verifier | Review protocols (2 hours) + Domain expertise (existing) |
| Quality Coordinator | All role overview (4 hours) + Tool proficiency (4 hours) |

---

## Escalation Path

```
Level 1: Role Specialist → Quality Coordinator
  Issues: Tool problems, unclear instructions, minor discrepancies
  
Level 2: Quality Coordinator → Domain SME
  Issues: Content accuracy disputes, interpretation questions
  
Level 3: Domain SME → Third-Party Verifier
  Issues: Unresolved accuracy disputes, controversial content
  
Level 4: Third-Party Verifier → Project Leadership
  Issues: Policy decisions, resource constraints, scope changes
```

---

**Last Updated**: 2026-01-08
**Version**: 1.0.0
**Author**: Quality Assurance Team
