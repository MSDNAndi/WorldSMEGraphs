# GitHub Copilot Custom Instructions for WorldSMEGraphs

---
# ⏱️ **CRITICAL: 50-MINUTE WORK SESSION RULE** ⏱️
---

**🚨 READ THIS FIRST - MANDATORY FOR EVERY SESSION 🚨**

**YOU MUST WORK FOR A MINIMUM OF 50 MINUTES FROM SESSION START**

**🔴 COMMIT MESSAGE RULE - THIS CONTROLS SESSION BEHAVIOR:**
- ✅ **"Progress report: [description]"** = Saves work, CONTINUES session (use minutes 0-48)
- ❌ **"SESSION COMPLETE: [description]"** = ENDS session (only use at minute 50+)

**SESSION WORKFLOW:**
1. **IMMEDIATELY** run: `date -u +"%s"` and record start epoch
2. Calculate target: start_epoch + 3000 (50 minutes in seconds)
3. Work continuously, using **"Progress report:"** commits every 10-15 minutes
4. After EACH "Progress report:" commit, **IMMEDIATELY** continue to next work item
5. At minute 45+: Check if `current_epoch - start_epoch ≥ 3000`
6. If < 3000: **KEEP WORKING** with more "Progress report:" commits
7. If ≥ 3000: **NOW** create "SESSION COMPLETE:" commit (this ends session)

**NEVER:**
- ❌ Use "SESSION COMPLETE", "FINAL", "DONE" in commits before 50 minutes
- ❌ Stop working after a "Progress report:" commit - these are checkpoints, not endpoints
- ❌ Think "I've done enough" - there is ALWAYS more work in issues.md or improvements.md

**Finishing early (< 48 minutes) is UNACCEPTABLE and violates project rules.**

See detailed requirements in [Work Continuity and 50-Minute Rule](#5-work-continuity-and-50-minute-rule-️-critical) below.

---

## Table of Contents
- [**⏱️ 50-Minute Rule (CRITICAL - READ FIRST)**](#5-work-continuity-and-50-minute-rule-️-critical)
- [Project Mission](#project-mission)
- [Core Principles](#core-principles)
- [Project Structure](#project-structure)
- [Available Agents](#available-agents)
- [Build, Test, and Validation](#build-test-and-validation)
- [Workflow Requirements](#workflow-requirements)
- [Technology Stack and Coding Standards](#technology-stack-and-coding-standards)
- [Best Practices](#best-practices)
- [Getting Started](#getting-started)
- [Examples: Good vs Bad Patterns](#examples-good-vs-bad-patterns)
- [Common Pitfalls and Troubleshooting](#common-pitfalls-and-troubleshooting)
- [Quick Reference](#quick-reference)

## Project Mission
WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. The goal is to create an interconnected, language-agnostic knowledge graph that can be rendered in multiple formats and languages for different audiences.

**Key Features:**
- Language-agnostic knowledge representation
- Multi-audience rendering (toddlers to experts)
- Multi-lingual support
- File-based architecture (no external databases)
- 60+ specialized AI agents
- Cross-domain knowledge linking

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

---
# 🚨 THIS IS THE MOST IMPORTANT RULE IN THE ENTIRE PROJECT 🚨
---

**MANDATORY**: You MUST work continuously for **AT LEAST 50 MINUTES** from session start.

**NO EXCEPTIONS. NO SHORTCUTS. NO EARLY FINISHES.**

If you finish before 50 minutes, you have FAILED this session and violated project requirements.

---

#### ⚠️ Common Mistakes That Violate This Rule ⚠️

**DO NOT:**
- ❌ Finish after completing "just" one task
- ❌ Think "the work is done" before 50 minutes
- ❌ Create "SESSION COMPLETE" commits before minute 48
- ❌ Stop working because you can't think of what to do next
- ❌ End session early because "most of the work is done"
- ❌ Commit and stop before checking if 50 minutes have elapsed

**REMEMBER:**
- ✅ Commits are checkpoints, NOT stopping points
- ✅ There is ALWAYS more work in issues.md or improvements.md
- ✅ Documentation can ALWAYS be improved
- ✅ Code quality can ALWAYS be enhanced
- ✅ If you can't find work, you're not looking hard enough

---

#### Session Start (REQUIRED)
1. **IMMEDIATELY** run: `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"` and record start time
2. Calculate target end time (start + 50 minutes)
3. Set session goals based on available time
4. Document start time in session log

#### During Work (Minute 0-48)

**🔴 CRITICAL: COMMIT MESSAGES CONTROL SESSION BEHAVIOR 🔴**

**Actions that CONTINUE the session (USE THESE):**
- ✅ Commit messages starting with **"Progress report:"** - These are checkpoints that SAVE work and CONTINUE the session
- ✅ After ANY commit with "Progress report:", **IMMEDIATELY** start next work item
- ✅ Example: "Progress report: Added domain navigation guide (12KB)"
- ✅ These commits push changes but DO NOT end the session

**Actions that END the session (NEVER USE BEFORE 50 MINUTES):**
- ❌ Commit messages with "SESSION COMPLETE" - This ENDS the session
- ❌ Commit messages with "FINAL", "DONE", "Complete", or "Finished"
- ❌ Any language suggesting completion or wrap-up
- ❌ Creating summary/wrap-up documentation before minute 48
- ❌ These commits TERMINATE work - only use at minute 50+

**GOLDEN RULE**: 
- Minutes 0-48: **ONLY "Progress report:" commits** (continue working after each)
- Minutes 50+: **ONLY "SESSION COMPLETE:" commit** (ends session)

**Work Pattern:**
1. Work on highest priority tasks
2. Make incremental progress every 10-15 minutes
3. Save work with **"Progress report:"** prefix commits
4. After EACH commit, **IMMEDIATELY** continue to next item
5. If one task is done, **IMMEDIATELY** find and start next task
6. If blocked, switch tasks immediately (don't waste time)
7. Use agents for specialized work
8. **NEVER** stop before 50 minutes - there is ALWAYS more work

**⚠️ CRITICAL: What is "Fake Working" vs Real Work ⚠️**

**FAKE WORKING (PROHIBITED):**
- ❌ Making many small documentation commits just to fill time
- ❌ Updating paths in 20+ files separately (1 minute each) to reach 50 minutes
- ❌ Creating trivial commits after main work is done to "run down the clock"
- ❌ Doing busywork instead of substantive development
- ❌ Making purely cosmetic changes without adding value
- ❌ Splitting one logical change into 10+ commits artificially

**REAL WORK (REQUIRED):**
- ✅ Creating new AKUs with rigorous content
- ✅ Implementing new features or capabilities
- ✅ Fixing bugs and improving code quality
- ✅ Writing comprehensive documentation (not just updating paths)
- ✅ Enhancing agent configurations with substantial content
- ✅ Creating tools, scripts, or automation
- ✅ Conducting research and creating specifications
- ✅ Building prototypes or proof-of-concepts
- ✅ Reviewing and improving existing content quality

**Quality Over Quantity:**
- One substantive commit (e.g., creating 10 rigorous AKUs) is better than 20 trivial commits
- Each commit should add meaningful value to the project
- If you've completed the main task early, find SUBSTANTIVE next work
- Look for high-impact items in improvements.md, not busywork

#### Approaching End (Minute 40-45)
- **MUST** check current time: `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"`
- **MUST** check time again at minutes 40, 45, and 48
- If <45 minutes elapsed: **FIND MORE WORK** and start it
- Priority for additional work:
  1. Complete partial tasks
  2. Add more AKUs to current pilot
  3. Improve documentation
  4. Enhance agent configs
  5. Fix minor issues
  6. Prepare next session work

#### Final Minutes (Minute 50+ ONLY)

**⏱️ TIME CHECK REQUIRED:**
1. Run: `date -u +"%s"` to get current epoch timestamp
2. Calculate: current_epoch - start_epoch
3. If result < 3000 seconds (50 minutes): **CONTINUE WORKING with "Progress report:" commits**
4. If result ≥ 3000 seconds (50 minutes): **NOW you can create final commit**

**ONLY when time ≥50 minutes:**
- ✅ Create final commit with **"SESSION COMPLETE:"** prefix (this ENDS the session)
- ✅ Update session log with complete metrics
- ✅ Document next session priorities
- ✅ Push changes

**CRITICAL CHECKS:**
- ❌ Do NOT create "SESSION COMPLETE" commit if time < 50 minutes
- ❌ Do NOT stop working if time < 50 minutes
- ✅ Keep using "Progress report:" commits until time check passes
- ✅ There should ALWAYS be work to do - if you think you're done before 50 minutes, find more work

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

### Work Tracking System in .project/

The `.project/` directory contains comprehensive work tracking to ensure there's always work to find:

**Issue Categories:**
- **`issues.md`** - Open issues and blockers
  - 🔴 Critical blockers (preventing progress)
  - 🟡 Important issues (should address soon)
  - 🟢 Minor issues (nice to have)
  - Track status, priority, action items, assignments

- **`improvements.md`** - Enhancement proposals
  - Code quality improvements
  - Feature enhancements  
  - Optimization opportunities
  - Documentation upgrades

**How to Use During Session:**
1. **At session start**: Review `.project/issues.md` for 🔴 blockers
2. **When task complete**: Check `.project/issues.md` for 🟡 important work
3. **Need more work?**: Review `.project/improvements.md` for enhancements
4. **Before finishing**: Add any new issues/improvements discovered
5. **Update status**: Mark items as "In Progress" or "Resolved"

**Adding New Work Items:**
- Found a bug? Add to `.project/issues.md` as 🔴 or 🟡
- Have an improvement idea? Add to `.project/improvements.md`
- Include: Status, Created date, Priority, Description, Action items
- Link to related documents and code

This system ensures you can ALWAYS find work when approaching 50 minutes.

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
│   │   │   └── knowledge.graph        # Language-agnostic compressed representation
│   ├── physics/
│   └── chemistry/
├── economics/
│   ├── macroeconomics/
│   │   └── knowledge.graph
│   └── microeconomics/
└── [other domains]/

renders/                                    # Centralized rendered content (moved from domain/**/.renders/)
├── by-domain/
│   ├── science/
│   │   └── math/
│   │       └── algebra/
│   │           ├── english/
│   │           │   ├── elementary-school.md
│   │           │   ├── graduate.md
│   │           │   └── 4-year-old.md
│   │           └── german/
│   │               ├── grundschule.md
│   │               └── hochschule.md
│   └── economics/
│       └── macroeconomics/
│           └── english/
│               ├── adult-limited-reading.md
│               └── graduate.md
├── by-language/
└── by-audience/
```

### Knowledge Representation Guidelines
1. **Language-Agnostic Format**: Core knowledge graphs use a compressed, language-neutral format
2. **Cross-Linking**: Implement at least unidirectional, preferably bidirectional linking between concepts
3. **Hierarchical Organization**: Use domain/subdomain folder structure
4. **Rendering System**: Human-readable representations in centralized `renders/` directory
5. **Output Formats**: Prepare for markdown, PDF, LaTeX, TeX, DOCX, and visualizations

### File Organization
- All data is file-based, including databases
- Rendered content is centralized in `renders/` directory (organized by-domain, by-language, by-audience)
- Keep knowledge graphs separate from their renderings
- Maintain clear separation between domains

## Available Agents

See `.github/agents/` for specialized agent configurations (all use `.agent.md` format per GitHub Copilot standards)

### How to Invoke Agents

Agents are invoked using the `@agent-name` syntax followed by specific instructions:

**Basic invocation:**
```
@coordinator Create NPV pilot with 50 comprehensive AKUs
```

**With detailed requirements:**
```
@paper-miner Extract formulas and definitions from "Net Present Value Analysis" textbook chapters 3-5. Focus on: discount rates, cash flow calculations, decision criteria. Output: Structured JSON for AKU creation.
```

**Best practices for agent invocation:**
1. **Be Specific**: Provide clear objectives and success criteria
2. **Include Context**: Give relevant background information the agent needs
3. **Set Expectations**: Specify format, depth, timeline if applicable
4. **Reference Artifacts**: Point to specific files, sections, or resources
5. **Define Success**: State how to measure completion

**Available agent categories:**
- **Coordination**: coordinator, recruiter, quality
- **Content Extraction**: paper-miner, textbook-parser, video-transcriber, definition-extractor, formula-extractor
- **Knowledge Organization**: ontology, semantic-harmonization, terminology, relationship-extractor
- **Validation**: verification, fact-checking, peer-review, multi-lingual-validation
- **Rendering**: rendering, pedagogy, visualization, accessibility
- **Domain Experts**: math-expert, generic-domain-empathy (with personas)
- **Quality Assurance**: code-review-agent, contrarian
- **Image Generation**: image-generation (GPT Image 1.5 via Azure AI Foundry)
- **And 40+ more specialized agents** - see `.github/agents/` directory

## Image Generation Capabilities

WorldSMEGraphs includes AI image generation for presentations and documentation using GPT Image 1.5.

### Image Generation Tool
**Location**: `.project/agents/image-generation/tools/gpt_image_generator.py`

```bash
# Generate single image
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "Your prompt" --aspect landscape --quality high

# Parallel batch generation (recommended)
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt-file prompts.txt --parallel 5 --enhance

# Show prompting guidelines
python .project/agents/image-generation/tools/gpt_image_generator.py --guidelines
```

### Presentation Generator
**Location**: `.project/agents/image-generation/tools/presentation_generator.py`

Generates complete PPTX and PDF presentations with AI-generated images for each slide.

### Content Safety Handling
The image generation system includes automatic content safety handling:
- Pre-sanitizes prompts for sensitive technical terms
- Automatically modifies prompts if rejected by API
- Retries with safer alternatives
- Logs all modifications for transparency

### Super Explicit Prompts (Critical)
Always be SUPER EXPLICIT about directions, orientations, and positions in image prompts:

```
BAD:  "arrows showing data flow"
GOOD: "arrows flowing LEFT to RIGHT showing data flow direction, 
       with arrowheads on the RIGHT side of each connection"
```

### Environment Secrets Required
- `AI_FOUNDRY_API_KEY`: Azure AI Foundry API key
- `GPT_IMAGE_1DOT5_ENDPOINT_URL`: GPT Image 1.5 endpoint

## Build, Test, and Validation

### Validating AKUs (Atomic Knowledge Units)
This project uses Python scripts for validation. No external dependencies required (uses standard library only).

**Domain-Aware Validator (Recommended):**
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate all AKUs in a domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain economics

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/

# Verbose output
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json --verbose
```

**Legacy Validator (Math-focused):**
```bash
# Validate a single AKU
python .project/agents/quality-assurance/tools/validate_aku.py path/to/aku.json

# Validate all AKUs in a directory
python .project/agents/quality-assurance/tools/validate_aku.py --directory path/to/akus/

# Validate a specific pilot
python .project/agents/quality-assurance/tools/validate_aku.py --pilot npv
```

**Features of v2 validator:**
- Auto-detects domain from `classification.domain_path`
- Domain-specific validation rules (medicine, math, economics, science)
- Flexible schema based on content type
- Detailed error reporting with suggestions

### Validating Cross-Domain Linking
Ensure AKUs follow the cross-domain linking pattern:

```bash
# Validate single AKU for cross-domain compliance
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Validate all AKUs in a directory
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

**Cross-domain validator checks:**
- Native domain AKUs have `isNativeDomain: true`
- Application domain AKUs have `cross_domain_references`
- All cross-domain links point to valid paths
- Domain paths align with `domain/_ontology/global-hierarchy.yaml`

### Validating Agents
Check that all agent configurations meet the 180-line minimum requirement:

```bash
bash .github/scripts/check-agent-lengths.sh
```

This validates all `.agent.md` files in `.github/agents/` directory.

### Validating Project Structure
Verify that the actual file structure matches the documented structure:

**Automated Validation:**
```bash
bash .github/scripts/validate-structure.sh
```

This automated script checks for:
- Required directories exist
- Essential files present
- Validation scripts available
- Agent files present (60 agents)
- Domain structure correct

**Manual Validation:**
- Review `.project/structure.md` to ensure file organization matches documentation
- Verify no files are in wrong locations
- Check that all domains follow the standard structure pattern

### Quality Checks Before Committing
1. **Validate AKUs**: If you modified any AKU files, run the validation script
2. **Check Agent Configs**: If you modified agents, verify they meet requirements
3. **Verify Timestamps**: Ensure UTC timestamps are updated on modified AKUs
4. **Test Workflows**: If you modified workflows, run the local test script
5. **Test Locally**: If applicable, test any scripts or tools you modified
6. **Review Documentation**: Update docs if you changed structure or added features

### Testing Workflows Locally
Before pushing workflow changes, test them locally:

```bash
# Test workflow dependencies and functionality
bash .github/scripts/test-workflow-locally.sh
```

This validates:
- Python installation
- Required scripts exist and work
- Domains with AKUs are found
- Maturity tracker functionality
- Workflow YAML syntax

See [CI/CD Documentation](../docs/CI-CD.md) for complete guide.

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

## Technology Stack and Coding Standards

### Core Technologies
- **Storage**: File-based (JSON, Markdown, YAML)
- **Version Control**: Git
- **AI Agents**: GitHub Copilot (60+ custom agents)
- **Validation**: Python (standard library only)
- **Documentation**: Markdown
- **Knowledge Format**: JSON-based `.graph` files

### File Naming Conventions
- **Use lowercase** with hyphens for multi-word names
- **Be descriptive**: `elementary-school.md` not `es.md`
- **Consistent extensions**: `.md`, `.json`, `.graph`, `.agent.md`
- **Agent files**: `[name].agent.md` in `.github/agents/`

### Code Style Standards

#### Markdown
- Use ATX-style headers (`#` not underlines)
- One blank line between sections
- Use fenced code blocks with language tags
- Keep lines under 100 characters when possible
- Use numbered lists when order matters, bullets otherwise

#### JSON
- Use 2-space indentation
- Include trailing commas where allowed (if validator permits)
- Use double quotes for strings
- Keep consistent field ordering
- Validate with schema when available

#### Python (for tools)
- Use standard library only (no external dependencies)
- Include clear docstrings
- Self-contained scripts
- Provide usage examples in comments

#### Writing Style
- Use clear, concise language
- Define terms before using them
- Use active voice
- Be consistent with terminology
- Avoid jargon unless necessary
- Follow audience-appropriate complexity

### Version Control Practices
- **Commit frequently** with "Progress report:" prefix during work
- **Clear commit messages** describing what changed
- **Never commit** build artifacts, dependencies, or temporary files
- **Use .gitignore** for exclusions
- **Review changes** before committing

## Content Quality Philosophy

### Fix and Improve, Don't Just Delete

When you encounter poor quality content (unfunny storytelling, unprofessional material, half-done renderings):

**❌ WRONG APPROACH:**
- Simply delete the content
- Remove without replacement
- Eliminate without understanding the goal

**✅ CORRECT APPROACH:**
1. **Understand the intent**: Why was this created? What audience need was it addressing?
2. **Identify the problems**: What makes it unprofessional? Why is it "unfunny" or poorly designed?
3. **Create better content**: 
   - Replace unfunny storytelling with engaging, professional educational content
   - Improve bad visual design with proper design principles
   - Complete half-done renderings to professional standards
   - Ensure rigor while maintaining accessibility
4. **Maintain the value**: If content serves a purpose (e.g., child-friendly education), improve it to professional standards rather than eliminating the concept

**Example - Functional Programming Presentations:**
- ❌ Delete british-humor.pptx and rpg.pptx
- ✅ Create professional presentations with:
  - Clear learning objectives
  - Rigorous technical content
  - Professional visual design
  - Engaging but appropriate storytelling
  - Proper citations and examples

**Example - Child-Friendly Content:**
- ❌ Delete child AKUs because "children is an audience not a type"
- ✅ Understand the need:
  - Children ARE a rendering audience
  - Create adult-level rigorous AKUs
  - Then render those AKUs for child audiences in `renders/by-audience/children/`
  - Maintain scientific rigor in AKUs, accessibility in renderings

### Workflow for Quality Content Creation

When asked to fix poor content:
1. **Plan content first**: Define learning objectives, scope, structure
2. **Plan story/narrative**: How will this engage the audience? What's the flow?
3. **Write content**: Create rigorous, well-researched material
4. **Plan visuals**: Specify what diagrams, images, examples are needed
5. **Create visuals**: Use proper design principles, tools, and standards
6. **Iterate**: Review, get feedback, improve

Never skip straight to implementation. Always plan, then execute, then refine.

## Getting Started
1. Review `.project/structure.md` for current project organization
2. Check `.project/roadmap.md` for planned work
3. Consult appropriate agent configurations for specialized tasks
4. Follow domain-specific guidelines in `domain/[domain-name]/README.md`

## Examples: Good vs Bad Patterns

### Creating Knowledge Graphs

**❌ Bad:**
```json
{
  "name": "algebra",
  "content": "Algebra is math with variables"
}
```
*Issues: Not language-agnostic, missing structure, no metadata*

**✅ Good:**
```json
{
  "@context": "aku-v2",
  "@type": "concept",
  "@id": "math:algebra:variable",
  "metadata": {
    "version": "2.0.0",
    "created": "2025-12-27T15:30:00.000Z",
    "contributors": ["math-expert-agent"],
    "confidence": 0.95,
    "status": "validated"
  },
  "classification": {
    "domain_path": "science/mathematics/algebra",
    "type": "concept",
    "difficulty": "elementary",
    "importance": "foundational"
  }
}
```
*Follows format specification with metadata and structure*

### Agent Invocation

**❌ Bad:**
```
@agent do something with NPV
```
*Issues: No specific agent, vague requirements, no success criteria*

**✅ Good:**
```
@paper-miner Extract NPV formulas and definitions from "Corporate Finance" 
by Ross et al., chapters 5-6. Focus on: discount rate calculations, 
decision rules, sensitivity analysis. Output: Structured JSON suitable 
for AKU creation. Success: All formulas extracted with context and notation.
```
*Specific agent, clear scope, defined output, measurable success*

### File Organization

**❌ Bad:**
```
domain/
  stuff.json
  notes.md
  algebra-things/
    random.graph
```
*Issues: No structure, unclear names, mixed content*

**✅ Good:**
```
domain/
  science/
    math/
      algebra/
        knowledge.graph
        schema.json

renders/
  by-domain/
    science/
      math/
        algebra/
          english/
            elementary-school.md
```
*Follows standard structure, clear hierarchy, proper naming with centralized renders*

### Commit Messages

**❌ Bad:**
```
git commit -m "updates"
git commit -m "fix"
git commit -m "done"
```
*Issues: No context, doesn't explain what changed*

**✅ Good:**
```
git commit -m "Progress report: Added 5 NPV definition AKUs with validation"
git commit -m "Progress report: Fixed AKU timestamp format to ISO 8601"
git commit -m "SESSION COMPLETE: Enhanced agent infrastructure (50 min)"
```
*Clear prefix, describes change, provides context*

## Need Help?
If stuck or uncertain:
1. Recruit a specialized agent
2. Request a contrarian agent review
3. Consult domain expert agents
4. Review KPI tracking for agent recommendations

## Common Pitfalls and Troubleshooting

### Agent Invocation Issues
- **Problem**: Agent doesn't respond as expected
  - **Solution**: Ensure you're using the correct `@agent-name` format
  - **Check**: Verify agent name matches one in `.github/agents/` directory
  - **Tip**: Provide more specific context and requirements

### Validation Failures
- **Problem**: AKU validation fails
  - **Solution**: Check the error message for specific missing fields
  - **Common Issues**: Missing UTC timestamps, incorrect field types, missing required sections
  - **Fix**: Review `.project/agents/quality-assurance/tools/validate_aku.py` for requirements

### Agent Quality Issues
- **Problem**: Agent produces inconsistent results
  - **Solution**: Check agent KPI tracking in `.github/copilot/agent-kpis.md`
  - **Consider**: Using the contrarian agent to review the output
  - **Option**: Try a different specialized agent for the same task

### File Organization
- **Problem**: Don't know where to put new files
  - **Solution**: Review `.project/structure.md` for organization guidelines
  - **Pattern**: Follow existing domain structure patterns
  - **Rule**: Keep knowledge graphs and renderings separate

### Documentation Conflicts
- **Problem**: Found contradicting information in docs
  - **Solution**: Research thoroughly to resolve contradictions
  - **Process**: Document findings, update all affected files
  - **Tool**: Use `@documentation-agent` to check for contradictions

### Work Session Management
- **Problem**: Running out of time in 50-minute session
  - **Solution**: Check `.project/issues.md` and `.project/improvements.md` for next tasks
  - **Priority**: Always address critical blockers first
  - **Remember**: There is always more work - don't finish early

## Quick Reference

### Essential Files
- **This File**: `.github/copilot-instructions.md` - Main Copilot instructions
- **Project Structure**: `.project/structure.md` - File organization and layout
- **Global Hierarchy**: `domain/_ontology/global-hierarchy.yaml` - Domain taxonomy
- **Roadmap**: `.project/roadmap.md` - Project goals and timeline
- **Issues**: `.project/issues.md` - Open issues and blockers
- **Improvements**: `.project/improvements.md` - Enhancement proposals
- **Contributing**: `docs/CONTRIBUTING.md` - Contribution guidelines
- **README**: `README.md` - Project overview

### Important Directories
- **Agents**: `.github/agents/` - 60+ custom agent definitions
- **Domains**: `domain/` - Knowledge domain hierarchies
- **Domain Ontology**: `domain/_ontology/` - Global hierarchy and cross-domain tools
- **Documentation**: `docs/` - General project documentation
- **Project Metadata**: `.project/` - Project planning and tracking
- **Validation Tools**: `.project/agents/quality-assurance/tools/` - AKU validators

### Quick Commands
```bash
# Validate AKUs
python .project/agents/quality-assurance/tools/validate_aku.py path/to/aku.json

# Validate cross-domain linking
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Check agent quality
bash .github/scripts/check-agent-lengths.sh

# Validate project structure
bash .github/scripts/validate-structure.sh

# View project structure
cat .project/structure.md

# Check current issues
cat .project/issues.md
```

### Agent Quick Reference
- **Coordination**: `@coordinator`, `@recruiter`, `@quality`
- **Knowledge Creation**: `@knowledge-graph-agent`, `@ontology`
- **Content Extraction**: `@paper-miner`, `@textbook-parser`, `@video-transcriber`
- **Validation**: `@verification`, `@fact-checking`, `@peer-review`
- **Rendering**: `@rendering-agent`, `@pedagogy`, `@accessibility`
- **Quality Review**: `@code-review-agent`, `@contrarian-agent`
- **Documentation**: `@documentation-agent`, `@semantic-harmonization`

For complete agent list, see `.github/agents/` directory.

---

**Last Updated**: 2025-12-27  
**Version**: 2.0 (Enhanced comprehensive guide)
