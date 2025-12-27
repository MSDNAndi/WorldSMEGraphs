# Open Issues and Blockers

> **Last Updated**: 2025-12-27T03:36:30Z  
> **Purpose**: Track open issues, blockers, and problems needing resolution

## Status Legend
- 🔴 **Blocker**: Preventing progress on critical work
- 🟡 **Important**: Should be addressed soon
- 🟢 **Minor**: Nice to have, not urgent
- ✅ **Resolved**: Completed and verified

---

## Active Issues

### 🔴 Critical Blockers
*Issues preventing progress on critical work*

**None currently** ✅

---

### 🟡 Important Issues  
*Should be addressed in current phase*

#### Issue #1: Need More Comprehensive AKUs for NPV Pilot
**Status**: 🟡 In Progress  
**Created**: 2025-12-27  
**Priority**: High  
**Area**: NPV Pilot

**Description**:
NPV pilot currently has only 6 AKUs. Need 44 more to reach pilot goal of 50 AKUs with textbook-level depth.

**Impact**:
- Pilot cannot be considered complete
- Cannot fully validate V2 format
- Cannot demonstrate scalability

**Action Items**:
- [ ] Create 10 more definition AKUs
- [ ] Create 10 more formula AKUs  
- [ ] Create 10 more example AKUs
- [ ] Create 7 more theory AKUs
- [ ] Create 7 more application AKUs

**Assigned To**: Current session  
**Target Date**: 2025-12-28  

---

#### Issue #2: Agent Configurations Need More Detail
**Status**: 🟡 In Progress  
**Created**: 2025-12-27  
**Priority**: High  
**Area**: Agent Infrastructure

**Description**:
Only 18/53 agents have full MusicVideoPipeline-level detail (34% complete). Remaining 35 agents have basic configs (28-102 lines) and need comprehensive enhancement to 150-215 lines with:
- Detailed input requirements (required vs optional with context)
- 3+ good input examples (comprehensive, realistic scenarios)
- 2+ bad input examples (common mistakes explained)
- Comprehensive output format specifications
- Clear success criteria
- Performance expectations
- 3-7 related agents with workflow descriptions
- 10-step typical workflows
- 8-10 expertise areas
- 5-7 detailed usage examples with full context

**Current Status:**
- ✅ Fully enhanced (18): coordinator, recruiter, meta-learning, rendering, generic-domain-empathy, quality, web-scraper, research, academic/student/professional/diverse-learner/curious-public advocates, citation, localization, terminology, standards, semantic-harmonization, community-manager
- ⚠️ Need enhancement (35): All extraction agents (5), quality agents (5), education agents (5), technical agents (12), operations agents (8)

**Impact**:
- Agents harder to use effectively
- Unclear input/output contracts
- Limited discoverability

**Action Items**:
- [ ] Enhance remaining 35 agent configs to 150-215 lines each
- [ ] Add success criteria to each agent
- [ ] Add examples of good vs bad inputs (3+ good, 2+ bad)
- [ ] Document performance expectations
- [ ] Link related agents and workflows
- [ ] Add 10-step typical workflows
- [ ] List 8-10 expertise areas
- [ ] Include 5-7 detailed usage examples

**Assigned To**: Current session  
**Target Date**: 2025-12-27  

---

#### Issue #3: No Automated Timestamp Updates
**Status**: 🟡 Open  
**Created**: 2025-12-27  
**Priority**: Medium  
**Area**: Developer Experience

**Description**:
AKUs require UTC millisecond timestamps, but currently manual. Need Git pre-commit hook to auto-update timestamps on file edits.

**Impact**:
- Manual timestamp updates error-prone
- Easy to forget updating timestamps
- Inconsistent timestamp discipline

**Action Items**:
- [ ] Create pre-commit hook script
- [ ] Auto-detect touched AKU files
- [ ] Update timestamps to current UTC milliseconds
- [ ] Test with sample commits
- [ ] Document in .project/rules/

**Assigned To**: TBD  
**Target Date**: 2025-12-30  

---

### 🟢 Minor Issues
*Nice to have improvements, not urgent*

#### Issue #4: No Visualization Tools Yet
**Status**: 🟢 Future  
**Created**: 2025-12-27  
**Priority**: Low  
**Area**: Developer Tools

**Description**:
Would be helpful to visualize knowledge graph structure and relationships.

**Impact**:
- Harder to understand graph structure
- Manual navigation required
- Limited insight into cross-links

**Action Items**:
- [ ] Research graph visualization libraries
- [ ] Create prototype visualizer
- [ ] Support interactive exploration
- [ ] Add to developer tools

**Assigned To**: Phase 3  
**Target Date**: 2026-03-01  

---

#### Issue #5: No Search Functionality
**Status**: 🟢 Future  
**Created**: 2025-12-27  
**Priority**: Low  
**Area**: User Experience

**Description**:
Need ability to search across all AKUs by keywords, concepts, formulas.

**Impact**:
- Users must browse manually
- Hard to find specific content
- Limited discoverability

**Action Items**:
- [ ] Design search index format
- [ ] Implement indexing script
- [ ] Create search query API
- [ ] Add search UI

**Assigned To**: Phase 4  
**Target Date**: 2026-04-15  

---

## Resolved Issues

### ✅ Issue #R1: No GitHub Copilot Agent Configurations
**Resolved**: 2025-12-27  
**Resolution**: Created all 53 agent YAML configurations per GitHub Copilot documentation

### ✅ Issue #R2: No UTC Timestamps on AKUs
**Resolved**: 2025-12-27  
**Resolution**: Added ISO 8601 UTC millisecond timestamps to all 6 existing AKUs

### ✅ Issue #R3: No Validation Tools
**Resolved**: 2025-12-27  
**Resolution**: Created validate_aku.py with comprehensive checks including timestamps

---

## Issue Lifecycle

### How to Add an Issue
1. Add to appropriate section (Blocker/Important/Minor)
2. Include: Status emoji, Created date, Priority, Area
3. Write clear description with impact
4. List specific action items
5. Assign if possible, set target date

### Issue Progression
```
Open → In Progress → Resolved → Archived (monthly)
```

### Review Schedule
- **Daily**: Check for new blockers
- **Weekly**: Review Important issues, update progress
- **Monthly**: Archive resolved issues, reprioritize

---

## Related Documents
- [Improvements Tracking](.project/improvements.md)
- [Session Log](.project/session-log.md)
- [Roadmap](.project/roadmap.md)
