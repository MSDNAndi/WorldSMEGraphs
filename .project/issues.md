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

#### Issue #1: AKU Validator Needs Medical Domain Support
**Status**: 🟡 Open  
**Created**: 2025-12-27  
**Priority**: Medium  
**Area**: Quality Assurance Tools

**Description**:
The current AKU validator (`validate_aku.py`) expects math-centric fields like `representations` and `variables` which are not applicable to medical content. Medical AKUs use clinical-specific fields like `clinical_features`, `imaging_characteristics`, etc.

**Impact**:
- Cannot validate medical AKUs with current tool
- Medical AKUs show as "invalid" despite being structurally sound
- Need domain-specific validation rules

**Action Items**:
- [ ] Create medical AKU validator or extend current validator
- [ ] Define required fields for medical AKUs
- [ ] Support multiple domain formats (math, medical, etc.)
- [ ] Update validation to be domain-aware

**Assigned To**: TBD  
**Target Date**: 2026-01-10

---

#### Issue #2: Need More Comprehensive AKUs for NPV Pilot
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

#### Issue #3: Agent Configurations Need More Detail
**Status**: ✅ Resolved  
**Created**: 2025-12-27  
**Resolved**: 2025-12-27  
**Priority**: High  
**Area**: Agent Infrastructure

**Description**:
Only 18/53 agents had full MusicVideoPipeline-level detail (34% complete). Remaining 35 agents needed comprehensive enhancement to 180+ lines.

**Resolution**:
All 53 agents now enhanced to meet 180-line minimum with comprehensive content:
- 5 agents: 190-232 lines (comprehensive)
- 48 agents: 180-189 lines (quality-focused)
- All include detailed input requirements, examples (good/bad), output formats, success criteria, workflows, expertise areas, and extensive usage examples
- 100% compliance verified with check-agent-lengths.sh script

**Completed**: 2025-12-27  
**Verification**: All 53/53 agents pass 180-line minimum requirement  

---

#### Issue #4: No Automated Timestamp Updates
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

#### Issue #5: No Visualization Tools Yet
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

#### Issue #6: No Search Functionality
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

### ✅ Issue #R4: Agent Configurations Need More Detail  
**Resolved**: 2025-12-27  
**Resolution**: Enhanced all 53 agents to 180+ lines with comprehensive specifications
- 31 agents brought from below 180 lines to compliant status
- Added extensive usage examples across all domains
- Included detailed workflows, input/output specs, expertise areas
- Achieved 100% compliance (53/53 agents ≥180 lines)
- Verification script confirms all agents meet quality standards

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
