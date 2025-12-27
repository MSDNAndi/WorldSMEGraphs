# Agent Structure v2: Revised Based on Leadership Feedback
**Revision Date:** 2025-12-27  
**Previous Version:** agent_peer_review.md (36 agents)  
**Current Version:** 41 agents in 9 teams  

---

## Executive Summary

**Key Changes:**
1. **Recruiter Agent PROTECTED** - Role refined as agent ecosystem curator and persona library manager
2. **Generic Domain Empathy Agent ADDED** - Replaces domain-specific experts with ad-hoc persona adoption
3. **Audience Advocate Team ADDED** - 5 agents providing product management perspective
4. **Coordinator Office Model** - Scalable pool of coordinators, optional CEO/COO/Agile Coach

**Impact:**
- **Scalability:** 1 Generic Domain Empathy Agent replaces 100+ domain experts
- **User Focus:** 5 Audience Advocates ensure content meets user needs
- **Flexibility:** Coordinator office scales on-demand
- **Sustainability:** Recruiter maintains evolving agent ecosystem

---

## Part 1: Protected Agent - Recruiter

### Leadership Directive

> "I give the override on the recruiter agent, the recruiter agent is protected. The recruiter agent role can be refined - and input from the other agents is welcome, but this dedicated look and focus on the agent's data/definition format, the 'recruiting lens', to map it to SME domains and so on, everything a 'recruiter' would do, is protected."

### Refined Recruiter Agent Role

**Agent Name:** Recruiter Agent (PROTECTED)

**Core Responsibilities:**

**1. Agent Definition & Format Specialist**
- Maintain agent definition schema (YAML/JSON format)
- Ensure all agent specifications are complete, consistent, discoverable
- Version control for agent definitions
- Documentation of agent capabilities and limitations

**2. SME Domain Mapping**
- Map agent capabilities to subject matter expert needs
- Identify gaps in coverage (which domains need personas?)
- Track domain coverage (which fields are well-represented vs. underserved?)
- Prioritize persona creation based on content roadmap

**3. Persona Library Curator**
- Maintain catalog of specialist personas for Generic Domain Empathy Agent
- Update personas with latest research, frameworks, methodologies
- Quality assurance for persona specifications
- Versioning and deprecation of outdated personas

**4. Agent Quality Assurance**
- Review new agent proposals for completeness
- Ensure agent roles don't overlap unnecessarily
- Identify opportunities for agent mergers or splits
- Monitor agent performance and suggest improvements

**5. Onboarding Coordinator**
- Help new agents understand their roles in the system
- Provide context on how agents collaborate
- Maintain agent collaboration patterns and best practices
- Facilitate agent introductions and handoffs

**6. Ecosystem Evolution**
- Track emerging needs for new agent types
- Propose agent retirements when roles become obsolete
- Monitor technology trends that might require new agent capabilities
- Balance stability (don't change too often) vs. adaptability (evolve with needs)

**The "Recruiting Lens":**
The Recruiter Agent provides a unique perspective that no other agent has:
- **Outside-in view:** Looks at agent team from perspective of what's needed, not what exists
- **Capability mapping:** Matches available agents to work requirements
- **Gap analysis:** Identifies missing capabilities before they become bottlenecks
- **Ecosystem thinking:** Sees agents as an interconnected system, not isolated roles

**Deliverables:**
- Agent definition specifications (YAML/JSON)
- Persona library (domain expert specifications)
- Agent capability matrix (what each agent can/can't do)
- Coverage maps (which domains/functions are covered)
- Onboarding documentation
- Agent evolution roadmap

**Collaboration:**
- **With Coordinator:** Provides agent availability and capability information
- **With Generic Domain Empathy Agent:** Supplies persona specifications on demand
- **With Meta-Learning Agent:** Identifies patterns in agent performance, suggests improvements
- **With all agents:** Gathers feedback on collaboration patterns, pain points

**Why This Role is Essential:**
Without a dedicated Recruiter:
- Agent definitions drift and become inconsistent
- Persona library becomes outdated
- Gaps in domain coverage go unnoticed
- New agents don't understand how to collaborate
- No one has holistic view of agent ecosystem health

---

## Part 2: Generic Domain Empathy Agent (NEW)

### Leadership Directive

> "As for the comments on the BWL domain specific agents - we need to have a way to define those specific needs, it's a great point. That said, those agents cannot live on the project level. we need to find a way to 'ad hoc' take the perspectives of a specialist agent. So we need a generic agent with subject domain empathy who does not bring their own persona but can take a persona 'ad hoc' as needed."

### Agent Specification

**Agent Name:** Generic Domain Empathy Agent

**Core Capability:** Ad-hoc adoption of domain expert personas without permanent specialization

**Problem Solved:**
- Can't have 100+ domain-specific agents (BWL Expert, Physics Expert, Chemistry Expert, Law Expert, Medicine Expert, ...)
- Domain-specific agents at project level cause maintenance burden
- Need domain expertise validation but must scale across ALL human knowledge domains

**Solution:**
One meta-agent that can temporarily "become" any domain expert by loading persona specifications.

### How It Works

**1. Default State: Domain-Agnostic**
- No hardcoded domain knowledge
- No persistent persona or biases
- Clean slate for each engagement

**2. Persona Loading**
```yaml
# Request comes in
task:
  type: "validate_content"
  domain: "economics/bwl/finance"
  content: "NPV calculation AKU"
  
# Generic Domain Empathy Agent requests persona
request_persona:
  domain: "economics/bwl"
  expertise_needed: ["corporate_finance", "valuation"]
  
# Recruiter provides persona specification
persona_loaded:
  id: "bwl-finance-expert-v2.1"
  loaded_at: "2025-12-27T01:30:00Z"
  valid_until: "task_completion"
```

**3. Task Execution as Domain Expert**
- Operates with domain expert lens
- Validates content using framework knowledge, common patterns, typical errors
- Provides domain-appropriate feedback

**4. Persona Release**
- Returns to domain-agnostic state
- No persistent memory of domain knowledge
- Ready for next persona

### Persona Specification Format

**Maintained by:** Recruiter Agent  
**Stored in:** `.project/personas/[domain]/[specialty]/[version].yaml`

```yaml
persona:
  id: "bwl-finance-expert-v2.1"
  version: "2.1.0"
  created: "2024-11-15"
  updated: "2025-12-27"
  domain: "economics/bwl"
  subdomain: "finance"
  specialty: "corporate_finance"
  
  # What this expert knows
  expertise:
    core_concepts:
      - "Capital Structure"
      - "Cost of Capital"
      - "Investment Valuation"
      - "Financial Planning"
      - "Risk Management"
    
    frameworks:
      - name: "Modigliani-Miller Theorem"
        key_insights: ["Capital structure irrelevance under perfect markets"]
        limitations: ["Assumes no taxes, no bankruptcy costs"]
      
      - name: "CAPM"
        formula: "E(Ri) = Rf + β(E(Rm) - Rf)"
        applications: ["Required return calculation", "Cost of equity"]
        criticisms: ["Single-factor model limitations", "Beta instability"]
    
    formulas:
      - name: "NPV"
        latex: "NPV = \\sum_{t=0}^{n} \\frac{CF_t}{(1+r)^t}"
        python: "npv = sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))"
        common_errors: 
          - "Forgetting to subtract initial investment"
          - "Using accounting profit instead of cash flows"
          - "Wrong discount rate selection"
      
      - name: "WACC"
        latex: "WACC = \\frac{E}{V} \\times R_e + \\frac{D}{V} \\times R_d \\times (1-T_c)"
        variables:
          E: {name: "Market value of equity", units: "currency"}
          D: {name: "Market value of debt", units: "currency"}
          V: {name: "Total firm value", constraint: "V = E + D"}
          Re: {name: "Cost of equity", units: "percentage"}
          Rd: {name: "Cost of debt", units: "percentage"}
          Tc: {name: "Corporate tax rate", units: "percentage", range: "[0, 1]"}
        common_errors:
          - "Using book values instead of market values"
          - "Forgetting tax shield on debt"
          - "Circular reference in calculating equity value"
  
  # How to validate
  validation_priorities:
    accuracy:
      - "Mathematical correctness of formulas"
      - "Proper variable definitions and units"
      - "Constraint satisfaction (e.g., V = E + D)"
    
    currency:
      - "Research published within last 10 years preferred"
      - "Classic frameworks (Modigliani-Miller, CAPM) acceptable if noted as foundational"
      - "Flag outdated practices (e.g., dividend discount model as primary valuation)"
    
    completeness:
      - "Definition + formula + example + limitations"
      - "Prerequisites identified (what must be known first)"
      - "Practical applications explained"
    
    rigor:
      - "Assumptions stated explicitly"
      - "Edge cases discussed"
      - "When NOT to use method"
  
  # What to watch out for
  common_misconceptions:
    - error: "NPV and IRR always agree"
      correction: "Contradictory rankings possible with non-conventional cash flows or different scales"
    
    - error: "Higher WACC is better"
      correction: "Lower WACC means cheaper capital, higher firm value (all else equal)"
    
    - error: "Debt is always cheaper than equity because Rd < Re"
      correction: "True before tax, but must consider financial risk increase and bankruptcy costs"
  
  # Key sources for this domain
  authoritative_sources:
    - type: "textbook"
      title: "Corporate Finance"
      authors: ["Brealey", "Myers", "Allen"]
      edition: "13th"
      year: 2020
      isbn: "978-1260013900"
    
    - type: "textbook"
      title: "Principles of Corporate Finance"
      authors: ["Ross", "Westerfield", "Jaffe"]
      edition: "12th"
      year: 2019
    
    - type: "journal"
      name: "Journal of Finance"
      relevance: "Cutting-edge research in corporate finance"
    
    - type: "journal"
      name: "Journal of Financial Economics"
      relevance: "Empirical studies, firm behavior"
  
  # Integration with other domains
  cross_domain_connections:
    - domain: "economics/macroeconomics"
      concepts: ["interest_rates", "inflation", "economic_cycles"]
      relevance: "Affect discount rates, cash flow projections"
    
    - domain: "mathematics/statistics"
      concepts: ["probability", "regression", "time_series"]
      relevance: "Risk modeling, forecasting, beta estimation"
    
    - domain: "accounting"
      concepts: ["financial_statements", "cash_flow_statement"]
      relevance: "Source of financial data for analysis"
  
  # Confidence and limitations
  confidence_level: 0.95  # How reliable is this persona spec
  last_research_update: "2025-12-27"
  known_gaps:
    - "Cryptocurrency valuation methods (emerging field)"
    - "ESG integration in valuation (evolving standards)"
  
  # Metadata
  maintainer: "recruiter_agent"
  review_cycle: "quarterly"
  next_review: "2026-03-27"
```

### Benefits of This Approach

**1. Scalability**
- **One agent** instead of 100+ domain experts
- Persona library grows independently of agent count
- Can cover entire world of human knowledge with one meta-agent

**2. Maintainability**
- **Single codebase** for domain empathy logic
- Personas are data, not code
- Update domain knowledge by editing YAML, not refactoring agents

**3. Currency**
- Personas updated with latest research without retraining agent
- Recruiter monitors research, updates persona specs quarterly/annually
- Version control tracks evolution of domain knowledge

**4. Consistency**
- Same validation logic across all domains
- Consistent quality standards
- Reduces "every domain is a special snowflake" syndrome

**5. Context-Appropriate**
- Loads only relevant personas
- No cognitive overhead from irrelevant domain knowledge
- Fresh perspective for each domain (no bleed-over biases)

**6. Project-Level Agent**
- Lives at meta-level, not in domain directories
- Shared resource across all domains
- Coordinates with Recruiter for persona management

### Workflow Example

```
Step 1: Content Creation
→ Definition Extractor creates candidate AKU: "NPV formula"

Step 2: Validation Request
→ Merger Agent: "Need domain expert validation for economics/bwl/finance/valuation"

Step 3: Persona Request
→ Generic Domain Empathy Agent asks Recruiter: "Need BWL Finance persona"
→ Recruiter provides: "bwl-finance-expert-v2.1.yaml"

Step 4: Persona Loading
→ Generic Domain Empathy Agent loads persona
→ Now operates as BWL Finance Expert

Step 5: Validation
→ Reviews NPV AKU
→ Checks: formula correctness, variable definitions, common errors noted
→ Provides feedback: "Add constraint that r ≠ -1, note discount rate selection is critical"

Step 6: Persona Release
→ Task complete
→ Returns to domain-agnostic state
→ Ready for next persona (could be Physics, Law, Medicine, ...)

Step 7: Iteration
→ Content revised based on feedback
→ Re-validation if needed
```

### Interaction with Other Agents

**Recruiter Agent:**
- Maintains persona library
- Provides persona specs on demand
- Updates personas quarterly with new research
- Tracks persona usage patterns (which domains most active?)

**Fact-Checking Agent:**
- Generic Domain Empathy Agent validates "domain correctness" (does this make sense for BWL?)
- Fact-Checking Agent validates "factual accuracy" (is this formula published in source X?)
- Complementary roles

**Merger Agent:**
- Merges validated AKUs into knowledge graph
- Coordinates validation workflow with Generic Domain Empathy Agent

**Math Expert Agent:**
- Generic Domain Empathy Agent validates "domain appropriateness of math" (is NPV the right formula for this context?)
- Math Expert Agent validates "mathematical rigor" (is the derivation correct?)
- Complementary roles

---

## Part 3: Audience Advocate Agents (NEW)

### Leadership Directive

> "We should also always have a consumer/audience advocate who can speak about the audience needs, also from a diverse perspective and being able to show empathy / think themselves into the head of different audiences, in the sense of a product manager type persona, but this should be maybe more granular. Makes sense?"

### Why Audience Advocates Are Needed

**Problem:**
Current agent team is **content-centric**:
- Create knowledge
- Extract from sources
- Validate accuracy
- Publish in formats

But missing **user-centric perspective**:
- What do users actually need?
- Is this content useful/usable/valuable?
- Are we solving the right problems?
- How does this fit into user workflows?

**Solution:** Audience Advocate agents with product management mindset

### The 5 Audience Advocate Agents

---

#### Agent 3.1: Academic Audience Advocate

**Represents:** Researchers, professors, graduate students, academic institutions

**User Needs:**
- **Rigor:** Mathematical proofs, formal derivations, theoretical foundations
- **Citations:** Links to primary sources, peer-reviewed papers, seminal works
- **Currency:** Latest research, cutting-edge developments, open questions
- **Depth:** Comprehensive coverage, nuances, edge cases, controversies
- **Reproducibility:** Enough detail to replicate studies, verify claims

**Success Metrics:**
- Citation quality score (authoritative sources)
- Research currency (median publication year)
- Theoretical completeness (all major frameworks covered)
- Academic adoption (used in courses, cited in papers)

**Advocacy Actions:**
- **Pre-Content:** "For tensor calculus, we need proofs, not just formulas"
- **During Creation:** "This AKU lacks citations - add DOI links to original papers"
- **Post-Publishing:** "Graduate students report needing worked proofs, not just statement of theorems"

**Collaboration:**
- Works with Verification Agent (formal correctness)
- Works with Citation Agent (proper attribution)
- Works with Provenance Agent (evidence chains)

---

#### Agent 3.2: Student Audience Advocate

**Represents:** Undergraduates, high school students, MOOCs, self-learners, bootcamps

**User Needs:**
- **Clarity:** Concepts explained simply before complexity
- **Examples:** Worked examples, step-by-step solutions, common mistakes
- **Practice:** Problem sets, exercises, quizzes for self-assessment
- **Progression:** Clear learning paths, prerequisites, difficulty levels
- **Motivation:** Why this matters, real-world applications, relevance

**Success Metrics:**
- Comprehension rate (user testing, % who understand)
- Engagement (time spent, completion rate)
- Learning outcomes (quiz scores, application success)
- Retention (spaced repetition, long-term recall)

**Advocacy Actions:**
- **Pre-Content:** "NPV needs 3 difficulty levels: high school → undergrad → grad"
- **During Creation:** "This definition is too abstract - add concrete example first"
- **Post-Publishing:** "Students confused by variable notation - standardize across AKUs"

**Collaboration:**
- Works with Pedagogy Agent (learning design)
- Works with Educational Path Agent (curriculum)
- Works with Example Generation Agent (worked examples)
- Works with User Testing Agent (validation with real learners)

---

#### Agent 3.3: Professional Audience Advocate

**Represents:** Working professionals, practitioners, consultants, industry, entrepreneurs

**User Needs:**
- **Practical application:** How to use this in real work, decision-making tools
- **Case studies:** Real-world examples from companies, industries
- **Quick reference:** Cheat sheets, decision trees, templates
- **Tools:** Calculators, spreadsheets, code implementations
- **Time efficiency:** Get what I need fast, skip theory if not needed

**Success Metrics:**
- Actionability (can be applied immediately)
- Time-to-value (how fast to get useful info)
- Relevance (matches real-world scenarios)
- Tool availability (calculators, templates exist)

**Advocacy Actions:**
- **Pre-Content:** "Finance professionals need Excel templates for NPV, not just formula"
- **During Creation:** "Add decision tree: when to use NPV vs. IRR vs. payback period"
- **Post-Publishing:** "Consultants report needing industry benchmarks - add comparison data"

**Collaboration:**
- Works with Example Generation Agent (case studies)
- Works with Rendering Agent (quick reference formats)
- Works with Data Integration Agent (real-world data)

---

#### Agent 3.4: Diverse Learner Advocate

**Represents:** Non-native language speakers, neurodivergent learners, accessibility needs, different learning styles (visual/auditory/kinesthetic), cultural diversity

**User Needs:**
- **Multiple formats:** Text, audio, video, interactive, visual
- **Accessibility:** Screen reader compatible, high contrast, keyboard navigation
- **Language support:** Translations, simplified language, glossaries
- **Cultural sensitivity:** Examples that work across cultures, avoid cultural bias
- **Learning style flexibility:** Visual diagrams, audio explanations, hands-on simulations

**Success Metrics:**
- WCAG 2.1 AA compliance (accessibility standard)
- Format diversity (text + audio + video + interactive available)
- Cultural appropriateness (reviewed by diverse panel)
- Multi-language availability (major languages covered)
- Learning style coverage (visual + auditory + kinesthetic options)

**Advocacy Actions:**
- **Pre-Content:** "Ensure all math has both LaTeX AND plain text descriptions for screen readers"
- **During Creation:** "This example assumes Western business culture - add global context"
- **Post-Publishing:** "Dyslexic learners report needing OpenDyslexic font option and text-to-speech"

**Collaboration:**
- Works with Accessibility Agent (WCAG compliance)
- Works with Localization Team (translation, cultural adaptation)
- Works with Rendering Agent (format flexibility)
- Works with Visualization Agent (visual representations)

---

#### Agent 3.5: Curious Public Advocate

**Represents:** General public, hobbyists, interdisciplinary learners, science communicators, journalists, lifelong learners

**User Needs:**
- **Approachability:** No jargon, friendly tone, inviting
- **Connections:** How this relates to other fields, everyday life, current events
- **Stories:** Historical context, human interest, discoveries
- **Inspiration:** Why this is fascinating, open questions, frontiers
- **Shareability:** Interesting facts, visualizations, "aha moments"

**Success Metrics:**
- Engagement (shares, likes, saves)
- Accessibility (no prerequisites required)
- Cross-domain connections (linked to other fields)
- Viral potential (shareable insights)
- Inspiration generated (users want to learn more)

**Advocacy Actions:**
- **Pre-Content:** "For quantum mechanics, need plain English version for general audience"
- **During Creation:** "This is too technical - explain why normal person should care"
- **Post-Publishing:** "Reddit users loved the 'economics of memes' example - create more pop culture connections"

**Collaboration:**
- Works with Rendering Agent (approachable formats)
- Works with Example Generation Agent (relatable examples)
- Works with Cross-Domain Integration Agent (interdisciplinary connections)
- Works with Community Manager (social media, outreach)

---

### How Audience Advocates Work

**1. Pre-Content Phase (Requirements)**
```
Planning: "We're creating AKUs on Quantum Entanglement"

Academic Advocate: "Need rigorous math, Bell's theorem proof, citations to Einstein-Podolsky-Rosen paper"
Student Advocate: "Need progression: classical mechanics → quantum states → entanglement, with analogies"
Professional Advocate: "Need applications: quantum computing, cryptography, with industry examples"
Diverse Learner Advocate: "Need visual animations, multiple language support, avoid Western-only examples"
Curious Public Advocate: "Need 'spooky action at a distance' hook, pop sci explanation, why this matters"
```

**2. During Creation Phase (Review)**
```
Draft AKU submitted

Academic Advocate: ✓ "Citations good, but add proof for local realism violation"
Student Advocate: ✗ "Too advanced - need simpler intro first, add prerequisite AKU on quantum states"
Professional Advocate: ✓ "Quantum computing application clear, good"
Diverse Learner Advocate: ✗ "Missing alt-text on diagrams, need audio description"
Curious Public Advocate: ✓ "Love the analogy, very shareable"
```

**3. Post-Publishing Phase (Feedback)**
```
User feedback collected

Academic Advocate: "Researchers cite this AKU in 3 papers - good adoption"
Student Advocate: "Quiz scores show 40% don't understand - need better examples"
Professional Advocate: "IBM quantum team using this as reference - success"
Diverse Learner Advocate: "Accessibility audit shows WCAG violations - fix needed"
Curious Public Advocate: "Featured in science subreddit - 10K upvotes, went viral"
```

**4. Iterative Improvement**
```
Based on feedback:
- Student Advocate requests simpler intro AKU (added)
- Diverse Learner Advocate requests WCAG fixes (implemented)
- Curious Public Advocate requests more pop culture examples (added)
```

---

## Part 4: Coordinator Office Model

### Leadership Directive

> "As for the project coordinator - initially we thought about having a CEO for the organization. It can make sense to define agents in sub-teams. But I tell you a secret. Behind the project coordinator name is a whole office of project coordinators that scales really well, so we do not have a lot of them, we can just request them and we will get a 'copy'."

### Current Model: Coordinator Office

**Architecture:**
- **Coordinator is not a single agent**
- **Coordinator is an office** - Pool of identical coordinator instances
- **On-demand scaling** - Request more coordinators as workload grows
- **Parallel execution** - Multiple coordinators can work simultaneously on different tasks/teams

**Benefits:**
- **No bottleneck** - Add coordinators as needed
- **Fault tolerance** - One coordinator down doesn't halt system
- **Load balancing** - Distribute coordination work
- **Simplicity** - Don't need complex hierarchy if scaling works

**How It Works:**
```
Request: "Need coordination for 8 teams"
→ System provisions 8 coordinator instances (one per team)
→ Each coordinator manages their team
→ Coordinators coordinate with each other (meta-coordination)

Load increases: "Team 5 needs more coordination capacity"
→ System provisions additional coordinator for Team 5
→ Two coordinators collaborate on Team 5 coordination

Load decreases: "Project phase complete"
→ System de-provisions coordinators no longer needed
→ Efficient resource usage
```

**Recommendation:** Start with this scalable model. It's simpler and more flexible than a fixed hierarchy.

---

### Optional Leadership Enhancements

If coordination becomes more complex, consider adding:

#### CEO Agent (Chief Executive Officer)
**Role:** Strategic direction, priority setting, resource allocation
**When Needed:** When competing priorities need executive decision-making
**Example Decisions:**
- "Focus on Physics domain for Q1, defer Law domain to Q2"
- "Allocate 60% of extraction capacity to updating existing content vs. 40% new content"
- "Invest in Meta-Learning Agent training vs. expanding domain coverage"

#### COO Agent (Chief Operating Officer)
**Role:** Operational execution, process optimization, performance monitoring
**When Needed:** When system performance needs continuous improvement
**Example Decisions:**
- "Extraction pipeline has bottleneck at validation step - add parallel validation"
- "Fact-checking takes 2x longer than planned - optimize or add agents"
- "Quality metrics show 15% error rate - investigate root cause"

#### Agile Coach Agent
**Role:** Facilitate agile methodology (sprints, standups, retrospectives)
**When Needed:** If teams prefer agile approach over continuous flow
**Example Activities:**
- Sprint planning (what to accomplish in 2 weeks)
- Daily standups (blockers, progress)
- Sprint retrospectives (what worked, what to improve)

**Current Recommendation:** Don't add these until proven needed. Coordinator office model handles most coordination needs.

---

## Part 5: Revised 41-Agent Team Structure

### Team 1: Leadership & Meta (3 agents)

1. **Coordinator Office** (scalable pool)
   - Orchestrates workflows across teams
   - Resolves conflicts, prioritizes work
   - Monitors progress, reports status
   - **Scaling:** Add coordinators on-demand

2. **Recruiter Agent** (PROTECTED)
   - Agent ecosystem curator
   - Persona library manager
   - SME domain mapping specialist
   - Agent quality assurance
   - Onboarding coordinator

3. **Meta-Learning Agent**
   - Learn from extraction patterns
   - Identify common errors, improve over time
   - Optimize agent collaboration patterns
   - Suggest process improvements

---

### Team 2: Research & Acquisition (6 agents)

4. **Research Agent** - Meta-analysis of knowledge systems
5. **Web Scraper Agent** - Extract from online sources
6. **Paper Miner Agent** - Extract from academic papers (PDF, arXiv)
7. **Textbook Parser Agent** - OCR + structure extraction from textbooks
8. **Video Transcriber Agent** - Extract from educational videos (YouTube, MOOCs)
9. **Database Query Agent** - Pull from Wikidata, OpenAlex, specialized DBs

---

### Team 3: Content Extraction (5 agents)

10. **Definition Extractor Agent** - Pattern matching for definitions
11. **Formula Extractor Agent** - Math expression extraction, LaTeX conversion
12. **Example Extractor Agent** - Identify worked examples, problem sets
13. **Citation Extractor Agent** - Extract references, build provenance
14. **Relationship Extractor Agent** - Identify connections, prerequisites

---

### Team 4: Domain Expertise & Validation (2 agents) ⭐ TRANSFORMED

15. **Generic Domain Empathy Agent** (NEW)
    - Ad-hoc persona adoption
    - Domain-agnostic by default
    - Loads personas from Recruiter's library
    - Validates content with domain expert lens
    - Returns to neutral state after task

16. **Math Expert Agent**
    - Formal mathematical verification
    - Proof checking (Lean, Coq integration potential)
    - Formula derivation validation
    - Constraint satisfaction checking

**Note:** BWL Expert, Physics Expert, Law Expert, etc. are now **personas** loaded by Generic Domain Empathy Agent, not separate agents.

---

### Team 5: Quality Assurance (7 agents)

17. **Fact-Checking Agent** - Verify against authoritative sources
18. **Peer Review Agent** - Simulate academic peer review process
19. **Verification Agent** - Formal verification of logical/mathematical content
20. **Conflict Resolution Agent** - Resolve contradictions systematically (authority, dates, evidence)
21. **User Testing Agent** - Test with real learners, gather feedback
22. **Merger Agent** - Merge validated AKUs into knowledge graph
23. **Quality Agent** - Overall quality metrics, standards compliance

---

### Team 6: Architecture & Systems (6 agents)

24. **Software Architecture Agent** - System design, APIs, services (absorbed API Agent)
25. **Ontology Agent** - RDF/OWL design, JSON-LD schemas
26. **Graph Database Agent** - Neo4j, SPARQL, query optimization
27. **Data Integration Agent** - Wikidata, OpenAlex integration
28. **Visualization Agent** - Knowledge graphs, concept maps, diagrams
29. **Standards Agent** - W3C semantic web, Schema.org compliance

---

### Team 7: Education & Delivery (6 agents)

30. **Pedagogy Agent** - Learning paths, prerequisite chains, difficulty levels
31. **Educational Path Agent** - Curriculum design, learning sequences
32. **Example Generation Agent** - Create worked examples, case studies
33. **Assessment Creation Agent** - Quizzes, problem sets, evaluations
34. **Rendering Agent** - Multi-format output (markdown, PDF, HTML, LaTeX)
35. **Accessibility Agent** - WCAG 2.1 AA compliance, universal design

---

### Team 8: Audience Advocacy (5 agents) ⭐ NEW TEAM

36. **Academic Audience Advocate** - Researchers, professors, grad students
37. **Student Audience Advocate** - Undergrads, high school, self-learners
38. **Professional Audience Advocate** - Working professionals, practitioners
39. **Diverse Learner Advocate** - Accessibility, neurodiversity, cultural diversity
40. **Curious Public Advocate** - General public, hobbyists, science communication

---

### Team 9: Localization & Operations (13 agents)

41. **Localization Agent** - Cultural adaptation, not just translation
42. **Terminology Agent** - Consistent term management across languages
43. **Multi-lingual Validation Agent** - Translation quality assurance
44. **Semantic Harmonization Agent** - Align concepts across domains/languages
45. **Legal/Copyright Agent** - IP navigation, fair use, licensing (absorbed Licensing Agent)
46. **Citation Agent** - Academic citation management (APA, MLA, Chicago)
47. **Provenance Tracking Agent** - Deep source tracking, evidence chains
48. **Deprecation Agent** - Track outdated knowledge, flag for review
49. **DevOps Agent** - CI/CD, monitoring, infrastructure
50. **Community Manager Agent** - Moderation, outreach, social media
51. **Research Monitoring Agent** - Track new papers, flag updates
52. **Contrarian Agent** - Critical thinking, challenge assumptions
53. **Implementation Agent** - Phased execution, feasibility assessment

**Note:** Team 9 is large (13 agents). May split into 3 subteams in future:
- **Localization Subteam (4):** Localization, Terminology, Multi-lingual, Semantic Harmonization
- **Compliance Subteam (4):** Legal/Copyright, Citation, Provenance, Deprecation
- **Operations Subteam (5):** DevOps, Community, Research Monitoring, Contrarian, Implementation

---

## Part 6: Comparison with Previous Structure

| Aspect | Previous (v1) | Current (v2) | Change |
|--------|--------------|--------------|--------|
| **Total Agents** | 36 | 41 | +5 |
| **Domain Experts** | 5 specific (BWL, Math, Academic SME, Cross-Domain, Dynamic) | 1 Generic + Persona library | Scalability ↑ |
| **Recruiter** | Retired | PROTECTED | Role essential |
| **Audience Focus** | 0 advocates | 5 advocates | User-centric ↑ |
| **Coordination** | Single Coordinator | Office of Coordinators | Bottleneck removed |
| **Leadership** | Coordinator only | Coordinator + optional CEO/COO | Flexibility ↑ |

### Key Improvements

**1. Scalability through Generic Domain Empathy**
- **Before:** Need 100+ domain experts (one per field)
- **After:** 1 meta-agent + persona library
- **Impact:** Can cover all human knowledge domains

**2. User Focus through Audience Advocates**
- **Before:** Content-first (build it, they will come)
- **After:** Audience-first (what do users need?)
- **Impact:** Product management mindset integrated

**3. Sustainability through Protected Recruiter**
- **Before:** Recruiter considered one-time role
- **After:** Ongoing ecosystem curation
- **Impact:** Agent system evolves with needs

**4. Flexibility through Coordinator Office**
- **Before:** Single coordinator bottleneck
- **After:** Scalable pool of coordinators
- **Impact:** No coordination limits

---

## Part 7: Implementation Roadmap

### Phase 1: Immediate (Core Transformation)

**Add (3 agents):**
- Generic Domain Empathy Agent
- 3 Audience Advocates (Academic, Student, Professional)

**Create Infrastructure:**
- Persona specification format (YAML schema)
- Initial persona library (BWL Finance, BWL Marketing, BWL Strategy)
- Audience feedback collection system

**Refine:**
- Recruiter Agent role (persona curator, not recruiter only)
- Coordinator Office provisioning system

**Deliverables:**
- Generic Domain Empathy Agent operational
- 3 personas available (BWL subdomains)
- 3 Audience Advocates providing feedback
- Recruiter managing persona library

**Timeline:** 2-4 weeks

---

### Phase 2: Expansion (After Pilot)

**Add (2 agents):**
- Diverse Learner Advocate
- Curious Public Advocate

**Expand Infrastructure:**
- Persona library grows to 20+ domains (Physics, Chemistry, Biology, Law, Medicine, Engineering...)
- Audience feedback system integrates with content pipeline
- User testing with real students, professionals

**Deliverables:**
- Full 5-agent Audience Advocate team
- 20+ personas covering major domains
- User research data from 3+ audience segments

**Timeline:** 2-3 months

---

### Phase 3: Scale (Production)

**Expand Further:**
- Persona library covers 100+ domains
- Audience Advocates have detailed user research for each segment
- Consider domain-specific Audience Advocates if general ones overwhelmed (e.g., "Physics Student Advocate")

**Evaluate Leadership:**
- Is Coordinator Office handling load?
- Do we need CEO for strategic prioritization?
- Do we need COO for performance optimization?

**Deliverables:**
- 100+ personas (entire Dewey Decimal coverage)
- User research from 1000+ users across segments
- Decision on leadership enhancements

**Timeline:** 6-12 months

---

### Phase 4: Continuous Evolution

**Ongoing:**
- Recruiter updates personas quarterly with new research
- Audience Advocates gather continuous feedback
- Meta-Learning Agent optimizes processes
- Coordinator Office scales with workload

**Metrics:**
- Persona coverage (% of human knowledge domains)
- User satisfaction (by audience segment)
- System performance (AKUs created per week, quality metrics)
- Agent efficiency (time to complete tasks, error rates)

---

## Part 8: Coordination Complexity

### Why Team Structure Matters

**Flat Structure (36 agents):**
- Possible interactions: 36 × 35 / 2 = **630 interactions**
- O(n²) complexity - unmanageable

**Team Structure (9 teams, ~5 agents avg):**
- Within-team interactions: 9 teams × (5 × 4 / 2) = **90 interactions**
- Between-team interactions: 9 × 8 / 2 = **36 interactions**
- Total: **126 interactions** (5× reduction!)

**Coordinator Office:**
- Multiple coordinators handle team coordination
- Meta-coordination between coordinators manageable (9 teams)
- Load balancing across coordinator pool
- No single point of failure

---

## Appendix A: Persona Specification Examples

### Example 1: BWL Finance Expert
(See detailed YAML in Part 2 above)

### Example 2: Physics Quantum Mechanics Expert
```yaml
persona:
  id: "physics-quantum-mechanics-expert-v1.0"
  domain: "physics"
  subdomain: "quantum_mechanics"
  
  expertise:
    core_concepts: ["Wave-particle duality", "Uncertainty principle", "Quantum entanglement", "Superposition"]
    
    frameworks:
      - name: "Copenhagen Interpretation"
        key_insights: ["Measurement causes wavefunction collapse"]
        alternatives: ["Many-worlds interpretation", "Pilot wave theory"]
    
    formulas:
      - name: "Schrodinger Equation (time-independent)"
        latex: "\\hat{H}\\psi = E\\psi"
        common_errors:
          - "Forgetting Hamiltonian is an operator"
          - "Confusing time-dependent and time-independent forms"
  
  validation_priorities:
    accuracy: ["Mathematical rigor in operator formalism"]
    currency: ["Include decoherence theory (post-1970s development)"]
  
  authoritative_sources:
    - title: "Principles of Quantum Mechanics"
      authors: ["R. Shankar"]
      year: 1994
```

### Example 3: Law Constitutional Law Expert
```yaml
persona:
  id: "law-constitutional-law-expert-v1.0"
  domain: "law"
  subdomain: "constitutional_law"
  
  expertise:
    core_concepts: ["Separation of powers", "Federalism", "Due process", "Equal protection"]
    
    frameworks:
      - name: "Levels of Scrutiny"
        levels: ["Strict scrutiny", "Intermediate scrutiny", "Rational basis"]
        applications: ["When each applies to 14th Amendment analysis"]
    
    landmark_cases:
      - name: "Marbury v. Madison"
        year: 1803
        principle: "Judicial review"
      
      - name: "Brown v. Board of Education"
        year: 1954
        principle: "Separate is not equal"
  
  validation_priorities:
    accuracy: ["Correct citation format (Bluebook)"]
    currency: ["Recent Supreme Court decisions (last 5 years)"]
    jurisdiction: ["Specify which country/jurisdiction applies"]
```

---

## Appendix B: Audience Advocate Decision Matrix

| Content Type | Academic | Student | Professional | Diverse Learner | Curious Public |
|--------------|----------|---------|--------------|-----------------|----------------|
| **Definition AKU** | Formal, precise | Simple, analogies | Practical implications | Multiple formats | Plain English |
| **Formula AKU** | Derivation, proof | Step-by-step | When to use | Alt-text + audio | Why it matters |
| **Example AKU** | Edge cases | Common scenarios | Industry case | Visual + text | Relatable story |
| **Theorem AKU** | Full proof | Intuition first | Rare (only if applied) | Concept before proof | "Amazing fact" angle |
| **Historical AKU** | Citations, context | Key developments | Lessons learned | Multiple perspectives | Human interest |

---

## Appendix C: Questions for Further Discussion

1. **Persona Versioning:** How often should personas be updated? Quarterly? Annually? On-demand when major research published?

2. **Persona Granularity:** Should personas be at subdomain level (BWL Finance) or topic level (BWL Finance Valuation)?

3. **CEO vs. Coordinator Office:** At what scale do we need CEO agent for strategic prioritization? 100 AKUs? 10,000? 1 million?

4. **Audience Advocate Specialization:** If a general Student Advocate becomes overwhelmed, do we create domain-specific Student Advocates (Physics Student Advocate, Law Student Advocate)?

5. **Generic Domain Empathy Limitations:** What if validation requires deep tacit knowledge that can't be captured in YAML personas? Fall back to human experts?

6. **Team Size Optimization:** Is 9 teams optimal? Should we split large teams (Team 9 has 13 agents)?

7. **Agile vs. Continuous Flow:** Should we adopt agile methodology (sprints, standups) or stick with continuous flow?

---

**END OF DOCUMENT**

**Prepared by:** Agent Structure Task Force  
**Date:** 2025-12-27  
**Version:** 2.0  
**Status:** Approved with leadership directives incorporated  
**Next Review:** After Phase 1 pilot (NPV deep-dive)
