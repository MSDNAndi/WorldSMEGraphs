# WorldSMEGraphs Copilot Agents

> **Last Updated**: 2025-12-29  
> **Total Agents**: 61 agent configurations  
> **Location**: `.github/agents/` (per GitHub Copilot standards)
> **Format**: `.agent.md` files
> **Quality Standard**: All agents follow GitHub Copilot custom agent format

## Overview

This directory contains 60 specialized GitHub Copilot agent configurations that work together to create, manage, and enhance the WorldSMEGraphs knowledge representation system. All agents follow the official GitHub Copilot custom agent format as documented at: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents

## Agent Format Standard

All agents MUST follow this format:
- **File Extension**: `.agent.md` (not `.agent.md`, `.yaml`, or plain `.md`)
- **Location**: `.github/agents/[agent-name].agent.md`
- **Structure**: Markdown format with required sections (see individual agents)

## Quick Reference - All 60 Agents

### Core Infrastructure (3 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| coordinator.agent.md | 180 | Multi-agent workflow orchestration, task delegation |
| recruiter.agent.md | 180 | Agent ecosystem management, capability matching |
| quality.agent.md | 180 | Comprehensive QA procedures, validation |

### Content Creation & Extraction (9 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| textbook-parser.agent.md | 181 | Extract content from textbooks across all disciplines |
| paper-miner.agent.md | 180 | Extract from research papers, analyze methodologies |
| video-transcriber.agent.md | 181 | Transcribe and extract from educational videos |
| definition-extractor.agent.md | 180 | Extract formal definitions from sources |
| formula-extractor.agent.md | 180 | Extract mathematical formulas, convert to LaTeX |
| example-extractor.agent.md | 181 | Extract worked examples and problems |
| citation-extractor.agent.md | 180 | Extract and format citations, build bibliographies |
| relationship-extractor.agent.md | 181 | Extract conceptual relationships, build dependency graphs |
| web-scraper.agent.md | 197 | Scrape educational content from websites |

### Knowledge Organization (8 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| ontology.agent.md | 180 | Design ontologies, define taxonomies |
| graph-database.agent.md | 180 | Graph database architecture and optimization |
| semantic-harmonization.agent.md | 207 | Resolve semantic conflicts across sources |
| terminology.agent.md | 182 | Manage domain terminology and glossaries |
| merger.agent.md | 184 | Merge duplicate or overlapping AKUs |
| conflict-resolution.agent.md | 183 | Resolve conflicting information from sources |
| provenance-tracking.agent.md | 183 | Track content lineage and sources |
| aku-atomicity-specialist.agent.md | 521 | Manage AKU granularity (split/merge/recombine) |

### Quality Assurance (5 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| fact-checking.agent.md | 181 | Verify factual accuracy across domains |
| peer-review.agent.md | 180 | Multi-dimensional quality review |
| verification.agent.md | 181 | Formal verification, proof checking |
| citation.agent.md | 183 | Citation validation and management |
| database-query.agent.md | 183 | Query external databases for validation |

### Rendering & Presentation (4 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| rendering.agent.md | 215 | Transform AKUs into audience-appropriate formats |
| visualization.agent.md | 216 | Create visual representations of knowledge |
| localization.agent.md | 182 | Adapt content for different languages and cultures |
| accessibility.agent.md | 216 | Ensure WCAG compliance, screen reader support |

### Pedagogy & Learning (5 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| pedagogy.agent.md | 182 | Learning science, instructional design |
| educational-path.agent.md | 213 | Curriculum design, prerequisite mapping |
| assessment-creation.agent.md | 180 | Create assessments using Bloom's taxonomy |
| user-testing.agent.md | 185 | User research and usability testing |
| meta-learning.agent.md | 197 | Learning analytics, adaptive systems |

### Audience Advocates (5 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| academic-audience-advocate.agent.md | 184 | Academic rigor, research standards |
| student-audience-advocate.agent.md | 185 | Student learning needs |
| professional-audience-advocate.agent.md | 180 | Professional practitioner needs |
| diverse-learner-advocate.agent.md | 185 | Accessibility, diverse learning styles |
| curious-public-advocate.agent.md | 183 | General public accessibility |

### Domain Expertise (4 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| generic-domain-empathy.agent.md | 184 | Understand any domain, create personas |
| math-expert.agent.md | 180 | Mathematical verification across domains |
| legal-copyright.agent.md | 180 | IP law, fair use, licensing |
| standards.agent.md | 188 | Technical standards compliance |

### Technical Infrastructure (7 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| software-architecture.agent.md | 180 | Architecture patterns, scalability, cloud |
| devops.agent.md | 190 | CI/CD pipelines, automation, monitoring |
| implementation.agent.md | 232 | Feasibility assessment, execution planning |
| research-monitoring.agent.md | 181 | Track research advances in domains |
| community-manager.agent.md | 200 | Community engagement, contribution management |
| deprecation.agent.md | 180 | Manage outdated content, migrations |
| data-integration.agent.md | 187 | Integrate data from multiple sources |

### Special Purpose (4 agents)
| Agent | Lines | Purpose |
|-------|-------|---------|
| contrarian.agent.md | 183 | Challenge assumptions, identify weaknesses |
| multi-lingual-validation.agent.md | 181 | Validate translations, cultural adaptation |

## Quality Standards

All 61 agents meet these standards:
- ✅ **Minimum 180 lines** of comprehensive specifications
- ✅ **Maximum <30,000 characters** per agent
- ✅ Detailed input/output formats with examples
- ✅ 50-75+ usage examples across domains
- ✅ Clear workflows and expertise areas
- ✅ Proper cross-referencing with related agents
- ✅ Verified via `check-agent-lengths.sh`

## Acceptance Testing

```bash
cd .github/agents
bash ../../scripts/check-agent-lengths.sh
# Output: ✅ ACCEPTANCE CRITERIA MET
#         All agents meet 180-line minimum
#         Total Agents: 61
#         Passed: 61
#         Failed: 0
```

## How to Use Agents

### Basic Syntax
```
@[agent-name] [specific request with context]
```

### Examples with YAML Agents

#### Extract Knowledge from Sources
```
@textbook-parser Extract Chapters 1-3 from Brealey Corporate Finance 13e, domain: finance, depth: comprehensive

@paper-miner Extract methodology section from arXiv:2103.12345 including supplementary materials

@video-transcriber Process MIT 18.06 Linear Algebra Lecture 10, extract all matrix operations and proofs
```

#### Validate and Review Content
```
@fact-checking Verify all statistics in economics AKUs against Federal Reserve and BEA data

@peer-review Comprehensive review: NPV module (20 AKUs), standards: CFA Institute + academic rigor

@verification Formal proof check: Nash equilibrium theorem, use Lean prover
```

#### Organize Knowledge
```
@ontology Design ontology for finance domain: valuation, risk, markets, derivatives

@merger Merge 3 NPV AKUs from textbooks, keep all unique examples, resolve formula notation

@conflict-resolution Three economics textbooks define 'elasticity' differently, resolve using authority + recency

@aku-atomicity-specialist Analyze domain/social-sciences/economics/bwl/finance/valuation/npv/ for over-bundled AKUs, recommend splits

@aku-atomicity-specialist Split aku-npv-complete.json into atomic units: definition, formula, decision-rule, example
```

#### Render for Audiences
```
@rendering Transform NPV AKUs for German elementary school students, age-appropriate examples

@localization Adapt economics content for Japanese business culture, honorifics and cultural context

@accessibility Ensure WCAG AA compliance for mathematics content, MathML + screen reader support
```

#### Design Learning Experiences  
```
@pedagogy Design 12-week Corporate Finance course from 80 AKUs, undergrad level, include assessments

@educational-path Create adaptive learning path: calculus derivatives with 3 difficulty tracks

@assessment-creation Create Bloom's taxonomy assessments for NPV concepts, all 6 cognitive levels
```

#### Architecture and Development
```
@software-architecture Design scalable rendering engine for global knowledge graph, 100M AKUs, multi-language

@devops Set up CI/CD pipeline: validate AKUs, test renderings, deploy on merge to main

@implementation Create detailed execution plan for multi-language rendering support, 10-language pilot
```

## Agent Collaboration Patterns

### Pattern 1: Extract → Validate → Organize → Review
**Use Case**: Creating AKUs from textbook sources

1. **Extract**: textbook-parser extracts content sections
2. **Extract Details**: definition-extractor, formula-extractor, example-extractor pull specific elements
3. **Validate**: fact-checking verifies accuracy, citation-extractor validates sources
4. **Organize**: ontology structures concepts, relationship-extractor builds dependencies
5. **Merge**: merger combines duplicates, conflict-resolution handles discrepancies
6. **Review**: peer-review validates quality, contrarian challenges assumptions

### Pattern 2: Research → Mine → Verify → Integrate
**Use Case**: Incorporating research papers

1. **Query**: database-query finds relevant papers (PubMed, arXiv, etc.)
2. **Mine**: paper-miner extracts methodology, results, conclusions
3. **Extract**: citation-extractor builds bibliography, relationship-extractor finds connections
4. **Verify**: verification checks formal proofs, fact-checking validates claims
5. **Integrate**: data-integration merges with existing knowledge, provenance-tracking maintains lineage
6. **Review**: quality agent validates final integration

### Pattern 3: Design → Render → Adapt → Test → Refine
**Use Case**: Creating multi-audience renderings

1. **Design**: pedagogy designs learning sequence, educational-path maps prerequisites
2. **Render**: rendering transforms AKUs for target audience level
3. **Adapt Culture**: localization adapts for language/culture
4. **Adapt Access**: accessibility ensures WCAG compliance, screen reader support
5. **Visualize**: visualization creates diagrams, concept maps
6. **Test**: user-testing validates with real users, audience advocates review
7. **Refine**: Based on feedback, iterate with rendering and adaptation agents

### Pattern 4: Monitor → Research → Implement → Deploy
**Use Case**: Adding new domains or features

1. **Monitor**: research-monitoring tracks advances in target domain
2. **Research**: generic-domain-empathy understands domain, creates expert persona
3. **Plan**: software-architecture designs system, implementation creates execution plan
4. **Build**: Coordinate development across multiple agents
5. **Quality**: peer-review, verification, quality agents validate
6. **Deploy**: devops sets up CI/CD, monitoring, deployment
7. **Manage**: community-manager handles user feedback, deprecation manages updates

### Pattern 5: Create → Critique → Improve → Validate
**Use Case**: Ensuring highest quality output

1. **Create**: Primary agent creates initial output
2. **Critique**: contrarian identifies weaknesses, challenges assumptions
3. **Verify**: Domain expert agents (math-expert, standards, legal-copyright) validate
4. **Review**: peer-review comprehensive quality check
5. **Improve**: Based on feedback, enhance output
6. **Final**: quality agent final validation before release

## Agent Selection Guide

### For Content Extraction
**Textbooks**: textbook-parser → definition-extractor, formula-extractor, example-extractor  
**Research Papers**: paper-miner → citation-extractor, relationship-extractor  
**Videos**: video-transcriber → example-extractor  
**Web Content**: web-scraper → appropriate extractors

### For Knowledge Organization
**Structure**: ontology → graph-database → terminology  
**Relationships**: relationship-extractor → merger → conflict-resolution  
**Quality**: provenance-tracking → semantic-harmonization

### For Validation
**Facts**: fact-checking → database-query  
**Formulas**: verification → math-expert  
**Citations**: citation → citation-extractor  
**Quality**: peer-review → quality  
**Standards**: standards → legal-copyright

### For Rendering
**Core**: rendering → pedagogy → educational-path  
**Adaptation**: localization → accessibility → visualization  
**Testing**: user-testing → audience advocates (academic, student, professional, diverse-learner, curious-public)  
**Assessment**: assessment-creation

### For Technical Work
**Architecture**: software-architecture → implementation  
**Operations**: devops → deprecation  
**Integration**: data-integration → research-monitoring  
**Community**: community-manager

### For Quality Assurance
**Primary**: quality → peer-review  
**Verification**: verification → fact-checking  
**Challenge**: contrarian → audience advocates  
**Compliance**: standards → legal-copyright → accessibility

## Best Practices

### 1. Be Specific
Bad: `@rendering-agent Create a rendering`
Good: `@rendering-agent Create an elementary school English rendering of domain/formal-sciences/mathematics/pure-mathematics/algebra/knowledge.graph focusing on variables and equations`

### 2. Provide Context
Include:
- What you're trying to achieve
- Any constraints or requirements
- Related work or dependencies
- Target audience or use case

### 3. Use Multiple Agents
For complex tasks:
1. Use primary agent for main work
2. Use contrarian agent for critique
3. Use code review agent for quality
4. Iterate based on feedback

### 4. Review Agent Output
- Don't blindly accept agent suggestions
- Validate accuracy and appropriateness
- Iterate if needed
- Learn from agent approaches

### 5. Track Agent Performance
- Note what works well
- Document issues or failures
- Update agent instructions based on experience
- Report persistent problems for agent improvement

## Creating New Agents

When you need a new specialized agent:

1. **Identify Need**
   - What expertise is lacking?
   - Would a specialized agent help?
   - Is it a recurring need?

2. **Use Template**
   - Copy appropriate template
   - Customize for specific domain/task
   - Define clear responsibilities
   - Set quality criteria

3. **Define KPIs**
   - How will you measure success?
   - What metrics matter?
   - How to track improvement?

4. **Document Agent**
   - Create agent configuration file
   - Add to this index
   - Update main instructions
   - Add to agent KPIs tracking

5. **Test and Iterate**
   - Try agent on sample tasks
   - Gather feedback
   - Refine instructions
   - Update based on performance

## Agent Performance

See [Agent KPIs](agent-kpis.md) for detailed performance tracking.

### Current Status (All Agents)
- **Status**: Active
- **Version**: 1.0
- **Review Cycle**: 0 (newly deployed)
- **Performance**: Awaiting first tasks

### Review Schedule
- First review: After 10 tasks or 1 month
- Regular reviews: Monthly
- Improvement cycles: Up to 5 before replacement

## Requesting New Agents

If you need an agent that doesn't exist:

1. **Check if existing agent can be adapted**
2. **Document the need**:
   - What tasks would it handle?
   - What expertise is required?
   - How would it differ from existing agents?
3. **Create proposal**:
   - Agent purpose and responsibilities
   - Expected KPIs
   - When to use it
4. **Submit for review**
5. **Create agent configuration** if approved

## Agent Improvement Process

If an agent is underperforming:

1. **Document Issues**
   - What went wrong?
   - What was expected vs. actual?
   - Impact of the problem

2. **Root Cause Analysis**
   - Why did it underperform?
   - Is it instruction clarity?
   - Is it capability limitation?

3. **Propose Improvements**
   - Updated instructions
   - Refined responsibilities
   - Better examples
   - Clearer quality criteria

4. **Implement and Test**
   - Update agent configuration
   - Test on similar tasks
   - Verify improvement

5. **Track Progress**
   - Update KPI tracking
   - Document improvement cycle
   - Monitor ongoing performance

6. **Replace if Necessary**
   - After 5 unsuccessful improvement cycles
   - Complete redesign or replacement
   - Document lessons learned

## Related Documents
- [Copilot Instructions](../copilot-instructions.md)
- [Agent KPIs](agent-kpis.md)
- [Individual Agent Configurations](.)

---

**Note**: Agents are tools to enhance productivity. Use them wisely, review their output, and help improve them through feedback.
