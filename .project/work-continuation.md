# Work Continuation Guide

> **Purpose**: Guide for keeping work sessions productive and continuous for up to 50 minutes from start

## Overview
This guide helps agents and contributors maintain momentum, find new work, and overcome blockers during work sessions.

## 50-Minute Work Session Structure

### Minutes 0-5: Session Start
**Objectives**: Orient and plan

**Actions**:
1. Review current state of work
2. Check last progress report
3. Identify highest priority tasks
4. Set specific goals for this session
5. Note any known blockers

**Questions to Answer**:
- What was completed last session?
- What needs to be done next?
- Are there any blockers?
- What can I accomplish in 45 minutes?

### Minutes 5-40: Deep Work
**Objectives**: Execute planned tasks

**Actions**:
1. Work on highest priority items first
2. Make incremental progress
3. Document decisions as you go
4. Commit frequently (every 10-15 minutes)
5. Switch tasks if blocked

**Stay Focused**:
- Minimize context switching
- Complete one thing before starting another
- Document blockers immediately
- Use agents for specialized tasks

### Minutes 40-50: Review & Plan
**Objectives**: Document progress and prepare for next session

**Actions**:
1. Review all completed work
2. Update documentation
3. Plan next session priorities
4. Commit and push changes
5. Update progress tracking
6. Note any new blockers or questions

**Deliverables**:
- Progress report with updated checklist
- Committed changes
- Plan for next session
- Documented blockers/questions

## Finding Work Priority Order

When you need to find new work, follow this priority order:

### Priority 1: Critical Blockers
Issues preventing others from working or system from functioning.

**Examples**:
- Build failures
- Broken CI/CD
- Security vulnerabilities
- Corrupted data

**Action**: Fix immediately or escalate.

### Priority 2: Current Phase Objectives
Tasks aligned with current project phase (see [Roadmap](roadmap.md)).

**Examples** (Foundation Phase):
- Complete format specifications
- Create agent configurations
- Write core documentation

**Action**: Work on incomplete phase objectives.

### Priority 3: Documentation Gaps
Missing or incomplete documentation.

**Finding Gaps**:
- Review file structure for missing READMEs
- Check for undocumented features
- Look for broken cross-references
- Verify all specifications are complete

**Action**: Create or improve documentation.

### Priority 4: Agent Improvements
Enhance agent performance based on KPIs and feedback.

**Check**:
- Review [Agent KPIs](../.github/copilot/agent-kpis.md)
- Look for underperforming agents
- Identify improvement opportunities
- Update agent instructions

**Action**: Improve or replace underperforming agents.

### Priority 5: Code Quality Issues
Technical debt, refactoring opportunities, code smells.

**Finding Issues**:
- Run linters
- Review code for clarity
- Check for duplicated code
- Look for overly complex functions

**Action**: Refactor and improve code quality.

### Priority 6: Redundancy Elimination
Duplicate or unnecessary files, code, or content.

**Finding Redundancies**:
- Look for duplicate documentation
- Check for similar content in multiple places
- Identify unused files
- Find overlapping functionality

**Action**: Consolidate, combine, or remove redundancies.

### Priority 7: Structure Optimization
Improve file organization and project structure.

**Check**:
- Review directory organization
- Look for misplaced files
- Check naming consistency
- Verify structure documentation is current

**Action**: Reorganize and update structure docs.

### Priority 8: Future Phase Preparation
Prepare for upcoming phases.

**Examples**:
- Research pilot domain topics
- Prototype rendering tools
- Design validation frameworks
- Plan automation approaches

**Action**: Do preparatory work for next phase.

## Overcoming Blockers

### When Stuck: Decision Tree

```
Am I stuck?
├─ Yes
│  ├─ Is it a knowledge gap?
│  │  ├─ Yes → Recruit specialist agent or research
│  │  └─ No
│  ├─ Is it a design decision?
│  │  ├─ Yes → Request contrarian agent review
│  │  └─ No
│  ├─ Is it a technical problem?
│  │  ├─ Yes → Break into smaller pieces or seek help
│  │  └─ No
│  ├─ Is it waiting on external input?
│  │  ├─ Yes → Document and move to different task
│  │  └─ No
│  └─ Other → Request human guidance
└─ No → Continue working
```

### Strategies for Common Blockers

#### Knowledge Gap
**Problem**: Don't have expertise needed.

**Solutions**:
1. Recruit specialized agent
2. Research topic (time-boxed: 15 min)
3. Document question for later
4. Move to related task you can do
5. Request human expert input

#### Design Uncertainty
**Problem**: Multiple approaches possible, unclear which is best.

**Solutions**:
1. Request contrarian agent review
2. Prototype 2-3 approaches (small scale)
3. Document trade-offs
4. Make decision and document rationale
5. Plan to revisit after pilot implementation

#### Technical Difficulty
**Problem**: Implementation is harder than expected.

**Solutions**:
1. Break problem into smaller pieces
2. Implement simplest version first
3. Research similar solutions
4. Request code review for guidance
5. Document blocker and try alternative approach

#### Waiting on Input
**Problem**: Need information or decision from others.

**Solutions**:
1. Document what's needed
2. Move to different task
3. Make reasonable assumption and proceed
4. Set reminder to follow up
5. Find preparatory work for once input arrives

### Time-Boxing Blockers

If stuck for more than:
- **5 minutes**: Try different approach
- **10 minutes**: Seek agent assistance
- **15 minutes**: Document blocker and move on
- **20 minutes**: Request human help

Don't let a single blocker consume entire session.

## Finding New Work Strategies

### 1. Review Open Issues
```bash
# Check issue tracker
# Look for issues labeled: "good first issue", "help wanted"
# Pick one aligned with your skills
```

### 2. Check Roadmap
Review [Roadmap](roadmap.md) for:
- Current phase incomplete items
- Next phase preparation opportunities
- Identified risks needing mitigation

### 3. Run File Organization Agent
```
@file-organization-agent Review project structure. 
Identify redundancies, misplaced files, and improvement opportunities.
```

### 4. Review Documentation
- Read through all docs
- Look for contradictions
- Check for outdated information
- Find missing cross-references
- Identify clarity improvements

### 5. Explore Domain Directory
```bash
# Look at domain structure
ls -R domain/

# Check for:
# - Incomplete knowledge graphs
# - Missing renderings
# - Broken cross-links
# - Inconsistent structures
```

### 6. Review Agent Performance
Check [Agent KPIs](../.github/copilot/agent-kpis.md):
- Agents needing improvement
- Missing agent configurations
- KPI tracking updates needed
- Performance reviews due

### 7. Proactive Quality Improvements
Even without specific tasks:
- Improve error messages
- Add examples to documentation
- Create templates for common tasks
- Write validation scripts
- Enhance testing

## Work Continuation Checklist

Use this checklist each session:

### Session Start ✓
- [ ] Reviewed last progress report
- [ ] Identified priorities for this session
- [ ] Set specific goals
- [ ] Noted any blockers

### During Work ✓
- [ ] Making incremental progress
- [ ] Documenting decisions
- [ ] Committing regularly
- [ ] Using agents appropriately
- [ ] Staying focused

### Session End ✓
- [ ] Reviewed completed work
- [ ] Updated documentation
- [ ] Committed and pushed changes
- [ ] Updated progress report
- [ ] Planned next session
- [ ] Documented blockers

### Quality Checks ✓
- [ ] No errors introduced
- [ ] No redundancies added
- [ ] Documentation updated
- [ ] Structure maintained
- [ ] Standards followed

## Metrics to Track

### Session Productivity
- Tasks completed
- Lines of code/docs written
- Issues closed
- Blockers encountered
- Blockers resolved

### Session Quality
- Errors introduced (target: 0)
- Rework required
- Agent assistance needed
- Human help needed
- Review feedback

## Tips for Sustained Productivity

### Do
- Set specific, achievable goals
- Break large tasks into smaller ones
- Document as you go
- Commit frequently
- Use agents for specialized work
- Take mental breaks when stuck
- Switch tasks when blocked

### Don't
- Try to do everything at once
- Skip documentation
- Ignore blockers
- Let perfect be the enemy of good
- Work on low-priority items when high-priority exist
- Continue struggling beyond time-box

## Emergency Procedures

### If Build Breaks
1. Stop all other work
2. Identify breaking change
3. Revert if necessary
4. Fix root cause
5. Verify fix
6. Document what happened

### If Stuck Completely
1. Document current state
2. List what you've tried
3. Clearly describe the blocker
4. Request human assistance
5. Move to different task while waiting

### If Time Running Out (Minute 45+)
1. Commit current work
2. Update progress report
3. Document next steps
4. Push changes
5. Don't start new major work

## Success Indicators

You're succeeding when:
- Completing planned tasks
- Making steady progress
- Documenting clearly
- Finding work easily
- Resolving blockers quickly
- Maintaining quality
- Contributing value

## Related Documents
- [Project Roadmap](roadmap.md)
- [Agent KPIs](../.github/copilot/agent-kpis.md)
- [Project Structure](structure.md)
- [Copilot Instructions](../.github/copilot-instructions.md)

---

**Remember**: The goal is continuous, quality progress. It's better to complete one thing well than to start many things and finish none.
