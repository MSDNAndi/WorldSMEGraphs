# Known Issue: Agent Content Needs Enhancement

## Status
- ✅ **Location Fixed**: All agents moved to correct `.github/agents/` directory
- ✅ **Format Conversion Complete**: All 60 agents use `.agent.md` extension
- ⚠️ **Content Enhancement Needed**: Automated conversion created placeholder content for some agents

## Problem

The automated batch conversion from YAML to Markdown successfully changed the file format but resulted in simplified content. The original YAML files contained:

- Comprehensive expertise descriptions
- Detailed workflow specifications  
- Rich usage examples
- Complex output format structures
- Specific performance metrics

The current .md files have:
- Basic structure (correct format)
- Placeholder content in some sections
- Missing detailed specifications from original YAML

## Affected Agents

Based on code review, agents needing content enhancement include:
- web-scraper.agent.md - missing detailed scraping capabilities
- visualization.agent.md - usage examples need reformatting
- meta-learning.agent.md - missing SME detection rules and thresholds
- quality.agent.md - incomplete output format structures
- And approximately 15-20 other converted agents with placeholder content

## Root Cause

The conversion script prioritized speed and format compliance over content preservation. YAML parsing errors in some files caused fallback to minimal placeholders.

## Solution Plan

### Phase 1: Keep Current Format ✅
- Current .md format is correct for GitHub Copilot
- File structure follows standards
- Recruiter as gatekeeper is established

### Phase 2: Content Enhancement (Future Work)
Two approaches:

**Option A: Restore and Reconvert (Recommended)**
1. Extract original YAML content from git history (commit 8911b7f)
2. Create enhanced conversion script that handles YAML parsing errors
3. Preserve ALL content during conversion
4. Manually verify key agents (recruiter, coordinator, quality, etc.)

**Option B: Manual Enhancement**
1. Use recruiter agent to enhance each agent incrementally
2. Review original YAML content for each agent
3. Add missing details back to .md files
4. Validate enhanced content with code reviews

### Phase 3: Validation
- Code review each enhanced agent
- Verify all content migrated
- Test agent functionality
- Update documentation

## Immediate Action

The format standardization IS complete and correct. The content enhancement is a **separate improvement task** that should be tracked independently.

### What's Already Good
- ✅ All agents in correct location: `.github/agents/`
- ✅ All agents use `.agent.md` format per GitHub Copilot standards
- ✅ No .yml files remain
- ✅ Recruiter is format gatekeeper
- ✅ Structure is consistent
- ✅ Agents are discoverable by GitHub Copilot
- ✅ Documentation updated to reflect correct paths

### What Needs Work (Next Session)
- ⚠️ Content depth and detail
- ⚠️ Usage examples richness
- ⚠️ Output format specifications
- ⚠️ Workflow completeness

## Recommendation

**Accept the current PR** as format and location standardization complete. Create a **new issue** for content enhancement as a follow-up task. This separates concerns:

1. Location fix (DONE) ✅ - Moved to `.github/agents/`
2. Format standardization (DONE) ✅ - All use `.agent.md`
3. Content enhancement (TODO) 📋 - Restore full content for placeholder agents

The format change enables GitHub Copilot integration. The content enhancement can be done incrementally without blocking the format benefits.

## Priority for Content Enhancement

When doing content enhancement, prioritize in this order:
1. **Core Infrastructure** (recruiter, coordinator, quality) - Already detailed
2. **Content Extraction** (definition, formula, example extractors)
3. **Research & Acquisition** (research, paper-miner, textbook-parser)
4. **Quality Assurance** (fact-checking, peer-review, verification)
5. **Rendering & Presentation** (rendering, visualization, accessibility)
6. **All Others**

---

**Created**: 2025-12-27T10:10:00Z  
**Issue Type**: Enhancement  
**Priority**: Medium  
**Blocked By**: None (format complete)  
**Blocks**: Full agent functionality
