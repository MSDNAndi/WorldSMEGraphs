# GitHub Copilot Custom Instructions for WorldSMEGraphs

## Project Mission
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. The goal is to create an interconnected, language-agnostic knowledge graph that can be rendered in multiple formats and languages for different audiences.

## Core Principles

### 1. Excellence in Software Engineering
- Strive for zero errors in all code and documentation
- Apply best practices from software engineering
- Tackle difficult problems with innovative solutions
- Keep the project structure lean and organized
- Eliminate redundancies proactively

### 2. Agent Utilization
- **Always prefer specialized agents** when they are better suited for a task
- Request expertise you don't have by recruiting new specialized agents
- Don't hesitate to create agents for specific subdomains
- Allow agents to compete with each other for quality improvements
- Hire "contrarian" agents to critique and improve all areas

### 3. Quality Assurance
- **Always perform code reviews** before finalizing pull requests
- Conduct internal code reviews iteratively until no improvements are found
- External code reviews should find nothing to critique
- Track agent performance through Key Performance Indicators (KPIs)
- Improve underperforming agents; replace after 5 unsuccessful improvement cycles

### 4. Documentation Excellence
- Understand relationships between documents to avoid contradictions
- Research extensively to resolve any contradictions found
- Combine similar documentation files when information is related
- Keep top-level project structure documentation always up to date
- Maintain consistency across all documentation

### 5. Work Continuity and 50-Minute Rule ⏱️ **CRITICAL**
**MANDATORY**: You MUST work continuously for 50 minutes from session start.

#### Session Start (REQUIRED)
1. **IMMEDIATELY** run: `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"` and record start time
2. Calculate target end time (start + 50 minutes)
3. Set session goals based on available time
4. Document start time in session log

#### During Work (Minute 0-45)
- Work on highest priority tasks
- Make incremental progress every 10-15 minutes
- Commit and push changes frequently using **"Progress report:"** prefix
- **NEVER** use "SESSION COMPLETE", "FINAL", or "DONE" in commit messages before minute 48
- **NEVER** create summary commits or "wrap-up" commits before minute 48
- All commits before minute 48 MUST be work-in-progress updates
- If blocked, switch tasks immediately (don't waste time)
- Use agents for specialized work
- **DO NOT** finish early
- **DO NOT** treat commits as session endpoints - they are progress checkpoints only

#### Approaching End (Minute 40-45)
- **MUST** check current time: `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"`
- If <45 minutes elapsed: **FIND MORE WORK** and start it
- Priority for additional work:
  1. Complete partial tasks
  2. Add more AKUs to current pilot
  3. Improve documentation
  4. Enhance agent configs
  5. Fix minor issues
  6. Prepare next session work

#### Final Minutes (Minute 45-50)
- **MUST** check time again at minute 45
- If <48 minutes elapsed: **CONTINUE WORKING** - do NOT create final commits
- At minute 48-50 ONLY:
  - Create final commit with "SESSION COMPLETE:" or "Final report:" prefix
  - Update session log with complete metrics
  - Document next session priorities
  - Push changes
- Before minute 48: ALL commits must be "Progress report:" only

#### Finding Work When Current Task Complete
**ALWAYS use this priority order:**
1. **Critical blockers** (Issues marked 🔴 in `.project/issues.md`)
2. **Current phase objectives** (Check `.project/roadmap.md`)
3. **Open issues** (Check `.project/issues.md`)
4. **Improvement proposals** (Check `.project/improvements.md`)
5. **Documentation gaps** (Review and improve)
6. **Agent improvements** (Enhance configs, add examples)
7. **Code quality** (Refactor, add tests)
8. **Structure optimization** (Clean up organization)

**Rule**: If you cannot find 50 minutes of work, you are not looking hard enough. There is ALWAYS work to do.

#### Enforcement
- Sessions shorter than 45 minutes without explicit human approval are **UNACCEPTABLE**
- Always justify in session log if ending before 50 minutes
- Proactively identify blockers and overcome them
- If stuck, recruit appropriate agents or request help

## Project Structure

### Domain Organization
```
domain/
├── science/
│   ├── math/
│   │   ├── algebra/
│   │   │   ├── knowledge.graph        # Language-agnostic compressed representation
│   │   │   └── .renders/
│   │   │       ├── english/
│   │   │       │   ├── elementary-school.md
│   │   │       │   ├── graduate.md
│   │   │       │   └── 4-year-old.md
│   │   │       └── german/
│   │   │           ├── grundschule.md
│   │   │           └── hochschule.md
│   ├── physics/
│   └── chemistry/
├── economics/
│   ├── macroeconomics/
│   │   ├── knowledge.graph
│   │   └── .renders/
│   │       └── english/
│   │           ├── adult-limited-reading.md
│   │           └── graduate.md
│   └── microeconomics/
└── [other domains]/
```

### Knowledge Representation Guidelines
1. **Language-Agnostic Format**: Core knowledge graphs use a compressed, language-neutral format
2. **Cross-Linking**: Implement at least unidirectional, preferably bidirectional linking between concepts
3. **Hierarchical Organization**: Use domain/subdomain folder structure
4. **Rendering System**: Human-readable representations in `.renders/[language]/[audience-level]`
5. **Output Formats**: Prepare for markdown, PDF, LaTeX, TeX, DOCX, and visualizations

### File Organization
- All data is file-based, including databases
- Use `.renders/` subdirectories for human-readable outputs
- Keep knowledge graphs separate from their renderings
- Maintain clear separation between domains

## Available Agents

See `.github/copilot/agents/` for specialized agent configurations:
- **knowledge-graph-agent**: Expert in creating and maintaining knowledge graphs
- **documentation-agent**: Specialist in technical documentation
- **code-review-agent**: Ensures code quality and best practices
- **contrarian-agent**: Provides critical feedback and improvement suggestions
- **domain-expert-agents**: Specialists for specific subject matter domains
- **rendering-agent**: Converts knowledge graphs to human-readable formats
- **file-organization-agent**: Maintains project structure and organization

## Workflow Requirements

### Before Finalizing Any PR
1. Run internal code reviews until no issues remain
2. Request code review from appropriate agents
3. Address all findings
4. Verify all tests pass
5. Update relevant documentation
6. Check for redundancies
7. Ensure project structure is current

### For Knowledge Graph Creation
1. Research the domain thoroughly
2. Create language-agnostic representation
3. Implement cross-linking with related concepts
4. Generate renderings for target audiences
5. Validate accuracy with domain experts
6. Update top-level documentation

### For Documentation Changes
1. Check for contradictions with existing docs
2. Resolve any conflicts found
3. Consider combining related files
4. Update cross-references
5. Maintain consistency in style and structure

## Agent Performance Tracking

Agents are evaluated on:
- **Quality**: Accuracy and completeness of work
- **Efficiency**: Time to complete tasks
- **Improvement**: Response to feedback
- **Reliability**: Consistency of results

After 5 review cycles without improvement, an agent must be replaced or completely redesigned.

## Best Practices
- Use sub-agents whenever they're better suited for a task
- Develop and maintain success criteria for all agents
- Track agent quality through KPIs
- Perform code reviews always before finalizing PRs
- Keep project structure lean and improved
- Find and eliminate redundancies
- Understand document relationships
- Solve contradictions even with excessive research
- Combine similar documentation files
- Keep top-level structure documentation current
- Apply best software engineering practices
- Aim for zero errors
- Solve the most difficult problems

## Getting Started
1. Review `.project/structure.md` for current project organization
2. Check `.project/roadmap.md` for planned work
3. Consult appropriate agent configurations for specialized tasks
4. Follow domain-specific guidelines in `domain/[domain-name]/README.md`

## Need Help?
If stuck or uncertain:
1. Recruit a specialized agent
2. Request a contrarian agent review
3. Consult domain expert agents
4. Review KPI tracking for agent recommendations
