# Open Issues and Blockers

> **Last Updated**: 2026-01-09  
> **Purpose**: Track open issues, blockers, and problems needing resolution  
> **Archives**: Resolved issues are archived in `.project/tracking/archived/`

## Status Legend
- 🔴 **Blocker**: Preventing progress on critical work
- 🟡 **Important**: Should be addressed soon
- 🟢 **Minor**: Nice to have, not urgent
- ✅ **Resolved**: Completed and verified

---

## Active Issues

### 🔴 Critical Blockers
*Issues preventing progress on critical work*

#### Issue #6: Systematic Wikidata Q1 Error Across 2,743 AKUs 🚨
**Status**: 🔴 CRITICAL - OPEN  
**Created**: 2026-01-10  
**Priority**: P0 (Immediate)  
**Area**: Data Quality / Semantic Web  
**Assignee**: TBD  
**Discovered by**: fact-checking-agent

**Description**:
Systematic error discovered where 2,743 AKUs incorrectly reference Wikidata entity Q1 ("Universe") in their `skos:exactMatch` field. This causes complete failure of semantic web integration, as all affected AKUs link to the wrong concept.

**Impact**:
- ❌ Semantic web integration BROKEN for 2,743 AKUs
- ❌ Knowledge graph cannot be published
- ❌ RDF/SPARQL queries return incorrect results
- ❌ External validation tools flag as errors
- ❌ Damages project credibility

**Root Cause**:
Appears to be template/generation error that used Q1 as placeholder value and was never corrected during bulk AKU creation.

**Scope by Domain**:
- Economics/Macroeconomics: ~50 AKUs (8 fixed, 42 remaining)
- Medicine: ~1000+ AKUs (estimated)
- Natural Sciences: ~500+ AKUs (estimated)
- Formal Sciences: ~200+ AKUs (estimated)
- Engineering/Other: ~1000+ AKUs (estimated)

**Fixes Completed** (Session 2026-01-10):
- [x] macro-001-gdp.json: Q1 → Q12638 (GDP)
- [x] macro-003-inflation.json: Q1 → Q179174 (Inflation)
- [x] macro-002-gdp-components.json: Q1 → Q186039 (GDP component)
- [x] macro-004-cpi.json: Q1 → Q181865 (CPI)
- [x] macro-007-business-cycles.json: Q1 → Q221395 (Business cycle)
- [x] macro-008-recession.json: Q1 → Q176494 (Recession)
- [x] macro-009-aggregate-demand.json: Q1 → Q4691546 (Aggregate demand)
- [x] Created comprehensive issue documentation

**Remaining Work**:
- [ ] Fix remaining ~42 macroeconomics AKUs (P0)
- [ ] Fix ~1000+ medicine AKUs (P0)
- [ ] Develop automated Wikidata lookup tool (P1)
- [ ] Create domain-specific mapping heuristics (P1)
- [ ] Fix remaining ~1600+ AKUs across all domains (P2)

**Action Items**:
1. **Immediate (P0)**: Fix all economics macroeconomics AKUs manually
2. **This Week**: Develop automation for Wikidata entity lookup
3. **Next Sprint**: Systematic correction by domain priority
4. **Prevention**: Add Q1 validation rule to AKU validator

**Documentation**:
- Full report: `domain/economics/macroeconomics/akus/CRITICAL-SYSTEMATIC-WIKIDATA-Q1-ERROR.md`
- Fact-check report: `domain/economics/macroeconomics/akus/FACT-CHECK-REPORT-macro-001-gdp.md`

**Related Commits**:
- 3981f38: GDP fact-checking (Q1 → Q12638)
- 3f07c60: Inflation fact-checking (Q1 → Q179174)
- 2ef30dd: 5 macro AKUs systematic fix

---

**None currently** ✅

---

### 🟡 Important Issues  
*Should be addressed in current phase*

#### Issue #5: Agent Documentation and Format Compliance
**Status**: ✅ COMPLETE  
**Created**: 2026-01-09  
**Completed**: 2026-01-09T17:25:00.000Z  
**Priority**: High  
**Area**: Agent Infrastructure  
**Assignee**: GitHub Copilot

**Description**:
Agents were not being utilized correctly due to format issues. Investigation needed to check agent parsing, validate against official GitHub Copilot documentation, and create comprehensive agent documentation.

**Root Cause**:
- `image-generation.agent.md` was missing required YAML frontmatter
- Legacy script in `.github/copilot/agents/` was outdated (looking for .yml files)
- Documentation needed updates with official format requirements

**Completed Work**:
- [x] Fixed `image-generation.agent.md` - added YAML frontmatter
- [x] Created `docs/agents/AGENTS-GUIDE.md` - comprehensive 16KB guide
- [x] Created `docs/agents/AGENT-SEGMENTATION-STRATEGY.md` - future scaling plans
- [x] Created `AGENTS.md` at repository root (per AGENTS.md standard)
- [x] Created `.github/scripts/validate-agent-format.sh` - format validation
- [x] Updated `.github/agents/README.md` with format requirements
- [x] Updated `.github/copilot-instructions.md` with troubleshooting
- [x] Updated `docs/README.md` with agent documentation links
- [x] Updated `.project/structure.md` with current counts (61 agents)
- [x] Updated `.project/TODO-agent-fixes.md` - marked all issues resolved
- [x] Removed legacy `.github/copilot/agents/check-agent-lengths.sh`

**Validation**:
- All 61 agents pass format validation
- All 61 agents pass line count validation (180+ lines)
- All agent names match their filenames

**Documentation Created**:
- `AGENTS.md` (repository root) - 5KB
- `docs/agents/AGENTS-GUIDE.md` - 16KB
- `docs/agents/AGENT-SEGMENTATION-STRATEGY.md` - 8KB
- `.github/scripts/validate-agent-format.sh` - 4KB

---

#### Issue #4: Renders Infrastructure Refactoring
**Status**: ✅ COMPLETE  
**Created**: 2026-01-06  
**Completed**: 2026-01-06T19:06:00.000Z  
**Priority**: High  
**Area**: Infrastructure  
**Assignee**: GitHub Copilot

**Description**:
Extract all .render/.renders content from domain/ hierarchy and centralize in renders/ directory at repository root. Update all path references throughout documentation and code.

**Impact**:
- ✅ Centralized render management (255 files migrated)
- ✅ Flexible organization (by-domain, by-language, by-audience)
- ✅ Better tracking and automation
- ✅ Multi-domain content support enabled
- ✅ 21 documentation files updated
- ✅ CI/CD validation added
- ✅ Developer tools created

**Completed Work**:
- [x] Migrate 255 files from 6 .renders directories to renders/by-domain/
- [x] Remove empty .renders directories
- [x] Update 21 documentation files (instructions, structure, agents, specs)
- [x] Create renders/README.md (comprehensive overview)
- [x] Create migration-log.md (complete migration history)
- [x] Create RECOMMENDATIONS.md (11KB future enhancements)
- [x] Create VALIDATION_REPORT.md (7KB verification details)
- [x] Create DEVELOPER_GUIDE.md (13KB comprehensive guide)
- [x] Create audience-profiles.yaml (8 audience definitions)
- [x] Create generate_render_index.py tool
- [x] Create generate_aku_usage_matrix.py tool
- [x] Create validate-renders.yml CI/CD workflow
- [x] Generate initial render-index.yaml (1816 lines, 255 files)
- [x] Generate initial aku-usage-matrix.yaml (658 AKUs tracked)

**Metrics**:
- Files migrated: 255
- Docs updated: 21
- Tools created: 3 (2 Python scripts + 1 CI/CD workflow)
- Documentation created: 6 files (50KB+ total)
- AKUs tracked: 658
- Current render coverage: 2.7% (18 AKUs with renders)

**See Also**:
- `renders/README.md` - Overview of new structure
- `renders/_metadata/RECOMMENDATIONS.md` - Next steps
- `renders/_metadata/VALIDATION_REPORT.md` - Verification details
- `renders/_metadata/DEVELOPER_GUIDE.md` - Developer reference

**Target Date**: 2026-01-06 ✅ COMPLETED ON TIME

---

#### Issue #3: Domain Hierarchy Migration - Ontology Compliance
**Status**: ✅ COMPLETE  
**Created**: 2026-01-04  
**Updated**: 2026-01-04T18:46:00.000Z  
**Priority**: High  
**Area**: Domain Organization  
**Completed**: 2026-01-04

**Description**:
Migrate all domains from legacy flat structure to rigorous hierarchical taxonomy per `domain/_ontology/global-hierarchy.yaml`. Ensure concepts are placed in their native domains (origin), not application domains (usage).

**Impact**:
- ✅ Ontological integrity restored across all major domains
- ✅ Native domain principle established and enforced
- ✅ Cross-domain linking pattern implemented
- ✅ 293 total files migrated (40 new migrations, 253 duplicates removed)
- ✅ All old directories removed (science, economics, medicine)

**Final Completion (2026-01-04)**:
- [x] Create new directory structure (formal, natural, social, health sciences)
- [x] Move category theory AKUs to mathematics (27 AKUs total: 8 ct, 6 functors, 8 monads, 5 monoids)
- [x] Update functional-programming with cross-domain references (19 AKUs)
- [x] Migrate physics to natural-sciences (138/138 AKUs - added 2 missing metadata files)
- [x] Migrate economics to social-sciences (12/12 AKUs - added 11 schema files)
- [x] Migrate medicine to health-sciences (68/67 AKUs - added 3 terminology files)
- [x] Migrate math content (21 AKUs: 5 geometry, 16 number-theory)
- [x] Create migration tools (3 scripts)
- [x] Validate all migrated AKUs
- [x] Create comprehensive READMEs (4 domains)
- [x] Update structure.md documentation
- [x] Update concept-index.yaml
- [x] Remove old directories (domain/science, domain/economics, domain/medicine)

**Final Statistics**:
- **Category Theory/Functional Programming**: 27 AKU files (functors, monads, monoids, category-theory)
- **Mathematics**: 21 AKU files (geometry, number-theory with 7 subdirectories)
- **Physics**: 138 JSON files (all subdirectories preserved)
- **Medicine**: 68 JSON files (including 3 terminology files)
- **Economics**: 12 JSON files (including 11 schema files)
- **Total Files Migrated**: 266 JSON files
- **AKU Files**: 256 (excluding schema/metadata)
- **Directories Removed**: 3 (science, economics, medicine)

**See**: Migration completion summary in PR description for full details.

**Cleanup Needed**:
- 🔧 Economics: 11 AKUs need `classification.domain_path` added
- 🔧 Medicine: 3 terminology files need `classification.domain_path` added
- 🔧 Physics: 2 skipped AKUs need investigation
- 🗑️ Legacy directories: Remove after verification

**Remaining Work** (Low Priority):
- ⏳ Mathematics: Other math content in science/math/ (primes, number-theory, geometry)
- ⏳ Computer Science: Other CS content organization
- 🗑️ Delete old category-theory directory

**Tools Created**:
- `domain/_ontology/tools/migrate_category_theory.py` - Specialized CT migration ✅
- `domain/_ontology/tools/update_fp_cross_domain.py` - Cross-domain refs ✅
- `domain/_ontology/tools/migrate_domain.py` - General-purpose migration ✅

**Statistics**:
- **Migrated**: 209 AKUs (8 CT + 136 physics + 1 economics + 64 medicine)
- **Updated**: 19 FP AKUs with cross-domain references
- **Total Processed**: 228 AKUs
- **Success Rate**: 99.5% (2 skipped for valid reasons)

**Dependencies**: 
- Global hierarchy approved ✅ (domain/_ontology/global-hierarchy.yaml)
- Cross-domain linking pattern defined ✅ (domain/_contexts/cross-domain.jsonld)

**Assigned To**: Copilot (Phases 1-4 complete)  
**Target Date**: 2026-01-15 (for cleanup completion)

---

#### Issue #0: Copilot Instructions Setup
**Status**: ✅ Resolved  
**Created**: 2025-12-27  
**Resolved**: 2025-12-27  
**Priority**: High  
**Area**: Development Infrastructure

**Description**:
Configure Copilot instructions for the repository according to GitHub best practices. Ensure agent definitions are correct and validation tools work properly.

**Resolution**:
1. ✅ Enhanced `.github/copilot-instructions.md` from 241 to 589 lines (+144%)
   - Added Table of Contents for navigation
   - Added "How to Invoke Agents" section with syntax and best practices
   - Added "Build, Test, and Validation" section with all commands
   - Added "Technology Stack and Coding Standards" section
   - Added "Common Pitfalls and Troubleshooting" section
   - Added "Examples: Good vs Bad Patterns" section
   - Added "Quick Reference" section with files, commands, and agent list
   - Created project structure validation script

2. ✅ Fixed `.github/copilot/agents/check-agent-lengths.sh`
   - Changed from checking `.yml` files to `.agent.md` files
   - Fixed path resolution to find agents in `.github/agents/`
   - Verified script works correctly (validates 60 agents)

3. ✅ Verified agent invocation patterns in documentation match definitions

**Outcome**:
- Copilot instructions now comprehensive and follow GitHub best practices
- All validation tools functional
- Agent usage documented with examples
- Quick reference guide available for developers

**Completed**: 2025-12-27

---

#### Issue #1: AKU Validator Needs Medical Domain Support
**Status**: ✅ Resolved  
**Created**: 2025-12-27  
**Resolved**: 2025-12-27  
**Priority**: Medium  
**Area**: Quality Assurance Tools

**Description**:
The current AKU validator (`validate_aku.py`) expected math-centric fields like `representations` and `variables` which are not applicable to medical content. Medical AKUs use clinical-specific fields like `clinical_features`, `imaging_characteristics`, etc.

**Impact**:
- Cannot validate medical AKUs with current tool
- Medical AKUs show as "invalid" despite being structurally sound
- Need domain-specific validation rules

**Resolution**:
Created `validate_aku_v2.py` with domain-aware validation following @verification and @ontology agent guidance:
- Auto-detects domain from `classification.domain_path`
- Domain-specific validation rules for medicine, math, economics, science
- Flexible schema validation based on content type
- Validates medical AKUs correctly (8/8 pass)
- Detailed error reporting with actionable suggestions
- Supports `--domain` flag for domain-specific validation

**Usage:**
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate all medical AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/
```

**Completed**: 2025-12-27  
**Verification**: All 8 medical AKUs validate successfully

---
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
**Status**: ⚠️ Partially Resolved - Reopened  
**Created**: 2025-12-27  
**Updated**: 2025-12-27  
**Priority**: High  
**Area**: Agent Infrastructure

**Description**:
Only 18/53 agents had full MusicVideoPipeline-level detail (34% complete). Remaining 35 agents needed comprehensive enhancement to 180+ lines.

**Previous Resolution Claim**:
All 53 agents now enhanced to meet 180-line minimum with comprehensive content:
- 5 agents: 190-232 lines (comprehensive)
- 48 agents: 180-189 lines (quality-focused)
- All include detailed input requirements, examples (good/bad), output formats, success criteria, workflows, expertise areas, and extensive usage examples
- 100% compliance verified with check-agent-lengths.sh script

**Current Status (2025-12-27)**:
Validation script now correctly checks `.agent.md` files (was checking non-existent `.yml` files):
- **Total agents**: 60 (verified count of .agent.md files)
- **Passing (≥180 lines)**: 25 agents (42%)
- **Failing (<180 lines)**: 35 agents (58%)
- Some agents have extremely low line counts (5-8 lines) suggesting incomplete or problematic definitions
- Note: Line count validation does not check content validity; some files may have parsing errors

**Action Items**:
- [ ] Investigate discrepancy between claim and actual state
- [ ] Review agents with very low line counts (5-8 lines) for content validity
- [ ] Enhance remaining 35 agents to meet 180-line minimum
- [ ] Ensure all agent files contain valid Markdown content
- [ ] Re-run validation after enhancements

**Assigned To**: TBD  
**Target Date**: 2026-01-05  

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

#### Issue #5: Duplicate Agent Definitions
**Status**: 🟡 Open  
**Created**: 2025-12-27  
**Priority**: Medium  
**Area**: Agent Infrastructure

**Description**:
Two agent pairs have duplicate definitions with different content:
1. `contrarian.agent.md` (116 lines) vs `contrarian-agent.agent.md` (83 lines)
2. `rendering.agent.md` (5 lines) vs `rendering-agent.agent.md` (80 lines)

This creates confusion about which agent to invoke and may lead to inconsistent behavior.

**Impact**:
- Unclear which agent definition is authoritative
- Potential confusion when invoking agents
- Wasted maintenance effort on duplicate definitions
- Inconsistent agent behavior

**Action Items**:
- [ ] Review both versions of each agent to determine correct definition
- [ ] Consolidate to single agent file per function
- [ ] Update any documentation references
- [ ] Remove duplicate files
- [ ] Verify agent invocations use correct names

**Assigned To**: TBD  
**Target Date**: 2026-01-05

---

#### Issue #6: AKU Numbering System Not Sustainable
**Status**: 🟡 Open  
**Created**: 2025-12-27  
**Priority**: High  
**Area**: Knowledge Representation

**Description**:
Current AKU numbering uses local sequential IDs (001-999) within each leaf category. This creates several problems:
- Non-unique across domains (medicine/aku-001, economics/aku-001 both exist)
- Limited range (999 AKUs max per category)
- No semantic meaning
- Manual management prone to conflicts
- Cannot reference globally

**Impact**:
- Scaling beyond 10,000 AKUs will be difficult
- Cross-domain references are ambiguous
- Merge conflicts with multiple contributors
- Renumbering breaks references

**Proposed Solution**:
Adopt semantic URI pattern: `{domain}:{path}:{concept}:{short-hash}`

Example: `medicine:vascular:complications:endoleak-type2:def:7f3a91c8`

**Action Items**:
- [ ] Review research document: `.project/research/ontology-and-numbering-analysis.md`
- [ ] Implement semantic ID generation script
- [ ] Add `canonical_id` field to AKU schema
- [ ] Update validation to check ID uniqueness globally
- [ ] Create migration plan for existing AKUs
- [ ] Update documentation

**Assigned To**: TBD  
**Target Date**: 2026-02-01

**Related Research**: `.project/research/ontology-and-numbering-analysis.md`

---

#### Issue #7: Project Structure Scalability Concerns
**Status**: 🟡 Open  
**Created**: 2025-12-27  
**Priority**: Medium  
**Area**: Infrastructure

**Description**:
Current file-based structure (one JSON file per AKU) will not scale beyond ~10,000 AKUs due to:
- Git performance degradation with many files
- File system limitations (deep nesting, path length)
- No clear boundary for when to split domains
- Single repository for all domains

**Impact**:
- Performance issues with large domains
- Difficult navigation with 100,000+ files
- Repository size becomes unwieldy
- Clone/pull times increase significantly

**Proposed Solutions**:
1. **Hybrid storage**: Index files + JSONL batches (1000 AKUs per file)
2. **Database-backed**: SQLite with auto-generated JSON sync
3. **Monorepo split**: Separate repos per major domain

**Action Items**:
- [ ] Review scalability analysis in research document
- [ ] Prototype hybrid storage approach
- [ ] Benchmark performance with 10k+ AKUs
- [ ] Define split criteria for domains
- [ ] Test Git performance at scale
- [ ] Create migration strategy

**Assigned To**: TBD  
**Target Date**: 2026-03-01

**Related Research**: `.project/research/ontology-and-numbering-analysis.md`

---

#### Issue #8: Need Standard Ontology Integration
**Status**: ✅ Resolved - Phase 1 Complete  
**Created**: 2025-12-27  
**Resolved**: 2025-12-27  
**Priority**: Medium  
**Area**: Knowledge Representation

**Description**:
Currently using ad-hoc knowledge representation without alignment to standard ontologies. Should integrate with:
- **Schema.org**: Already using, but not fully leveraging
- **SKOS**: For concept relationships (broader, narrower, related)
- **SNOMED CT**: For medical terminology
- **FIBO**: For economics/finance concepts
- **BFO/DOLCE**: For upper ontology alignment

**Benefits**:
- Interoperability with external systems
- Standard vocabularies
- Machine-readable semantics
- Link to existing knowledge bases (DBpedia, Wikidata)
- Better search and discovery

**Resolution - Phase 1 (Foundation)**:
- [x] Review ontology research document
- [x] Add SKOS relationships to AKU schema
- [x] Create JSON-LD context files for all domains (base, medicine, economics, science)
- [x] Create comprehensive ontology integration specification (2,185 lines)
- [x] Create implementation guide for developers (495 lines)
- [x] Build validation tool for ontology compliance
- [x] Build migration tool to convert existing AKUs
- [x] Create enhanced AKU example with full ontology integration
- [x] Test validation (100% success rate)

**Deliverables**:
1. `.project/research/ontology-integration-specification.md` - Complete technical specification
2. `.project/research/ontology-implementation-guide.md` - Developer guide
3. `domain/_contexts/` - 5 JSON-LD context files (base, medicine, economics, science, README)
4. `.project/agents/quality-assurance/tools/validate_ontology.py` - Validation tool
5. `.project/agents/quality-assurance/tools/migrate_to_ontology.py` - Migration tool
6. `.project/pilot/npv-finance/akus/definitions/aku-003-present-value-concept-ENHANCED.json` - Example

**Next Steps (Phases 2-5)**:
- Phase 2: Implement external ontology linking to SNOMED, FIBO, etc.
- Phase 3: Migrate all existing AKUs to new ontology format
- Phase 4: Add formal reasoning and inference capabilities
- Phase 5: Integration with external knowledge bases

**Completed**: 2025-12-27  
**Related Research**: 
- `.project/research/ontology-and-numbering-analysis.md`
- `.project/research/ontology-integration-specification.md`
- `.project/research/ontology-implementation-guide.md`

---

#### Issue #9: Mesenteric Ischemia Domain - Content Gaps
**Status**: 🟢 Partially Resolved  
**Created**: 2025-12-30  
**Updated**: 2026-01-04  
**Priority**: High  
**Area**: Medical Knowledge Content

**Description**:
Contrarian agent critical analysis identified significant content gaps in the mesenteric ischemia knowledge domain (29 AKUs). Despite competent core content, several critical topics are missing.

**Critical Gaps Identified**:
1. **Differential diagnosis AKU** — ✅ Already exists (aku-038)
2. **Atypical presentations AKU** — ✅ CREATED (aku-039) - Covers elderly, dementia, post-operative, pediatric
3. **Ischemia-reperfusion injury AKU** — ✅ Already exists (aku-040)
4. **Expanded NOMI content** — ✅ CREATED (aku-043) - Comprehensive ICU management protocol

**Progress (2026-01-04)**:
- [x] Created aku-039 (Atypical Presentations) - 4KB comprehensive content
- [x] Created aku-043 (NOMI Expanded) - 6KB ICU protocol with critical care perspective
- [x] Created comprehensive book chapter rendering with 15 medical illustrations
- [x] Added interdisciplinary perspectives (critical care, ICU protocols)
- [x] Book chapter now includes anatomy, pathophysiology, diagnosis, treatment, outcomes

**Remaining Work**:
- [ ] Audit and fix all vague citations
- [ ] Add IR (interventional radiology) perspective content

**Documentation**:
- Critical Analysis: `domain/health-sciences/medicine/surgery/vascular/pathology/mesenteric-ischemia/.project/critical-analysis-contrarian-review.md`
- Improvement Plan: `domain/health-sciences/medicine/surgery/vascular/pathology/mesenteric-ischemia/.project/improvement-plan.md`
- Book Chapter: `renders/by-domain/health-sciences/medicine/surgery/vascular/pathology/mesenteric-ischemia/english/comprehensive-book-chapter.md`

**Assigned To**: Medical content team  
**Target Date**: 2026-01-15  

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

*Resolved issues are now archived in `.project/tracking/archived/` by month.*

**Recent Archives**:
- [December 2025](.project/tracking/archived/2025-12/issues-resolved.md)
- [January 2026](.project/tracking/archived/2026-01/issues-resolved.md)

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
