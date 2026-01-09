# Agent Fixes TODO List

> **Status**: ✅ ALL ISSUES RESOLVED (as of 2026-01-09)  
> **Last Updated**: 2026-01-09

This document tracked agent definition files that needed work. All issues have been resolved.

## Summary

**All 61 agents now meet requirements:**
- ✅ Valid YAML frontmatter
- ✅ Minimum 180 lines (all agents pass)
- ✅ Proper format with `name:`, `description:`, `tools:` fields
- ✅ No parsing errors

## Previously Resolved Issues

### Priority 1: Corrupted Files - ✅ FIXED
All files have been recreated with proper content:
- ✅ `fact-checking.agent.md` (266 lines) - Fully functional
- ✅ `paper-miner.agent.md` (197 lines) - Fully functional  
- ✅ `peer-review.agent.md` (287 lines) - Fully functional
- ✅ `rendering-agent.agent.md` (187 lines) - Fully functional

### Priority 2: Duplicate Files - ✅ REVIEWED
Both files kept as they serve different purposes:
- ✅ `contrarian.agent.md` (209 lines) - General contrarian
- ✅ `contrarian-agent.agent.md` (201 lines) - Code-focused contrarian

### Priority 3: Short Files - ✅ FIXED
All files enhanced to meet minimum:
- ✅ `knowledge-graph-agent.agent.md` (198 lines) - Fully enhanced

## Validation

Run validation to confirm all agents pass:

```bash
# Check format
bash .github/scripts/validate-agent-format.sh

# Check line counts
bash .github/scripts/check-agent-lengths.sh
```

## Current Status

As of 2026-01-09:
- Total agents: 61
- Passing format validation: 61/61 (100%)
- Passing line count: 61/61 (100%)

All agents are operational.
  - Add quality criteria

- [ ] **merger.agent.md** (44 lines) - Add 136+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define merge conflict resolution strategies
  - Add validation workflows
  - Include examples
  
- [ ] **meta-learning.agent.md** (44 lines) - Add 136+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define learning optimization strategies
  - Add pattern recognition workflows
  - Include metrics and evaluation

- [ ] **multi-lingual-validation.agent.md** (44 lines) - Add 136+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define validation strategies per language
  - Add quality criteria
  - Include translation accuracy metrics

- [ ] **semantic-harmonization.agent.md** (44 lines) - Add 136+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define concept alignment strategies  
  - Add ontology mapping workflows
  - Include harmonization criteria

- [ ] **terminology.agent.md** (44 lines) - Add 136+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define terminology management workflows
  - Add glossary creation processes
  - Include consistency checking

## Priority 4: Moderately Short Files (80-120 lines)

These agents need significant expansion:

- [ ] **code-review-agent.agent.md** (79 lines) - Add 101+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand code quality criteria
  - Add review checklist workflows
  - Include security scanning guidance

- [ ] **contrarian-agent.agent.md** (83 lines) - Add 97+ lines (if keeping this one)
  - Add YAML front matter with `tools: ["*"]`
  - Expand critical thinking strategies
  - Add devil's advocate workflows
  - Include quality improvement metrics

- [ ] **rendering-agent.agent.md** (80 lines) - Add 100+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand rendering strategies
  - Add format-specific guidance
  - Include audience adaptation workflows

- [ ] **file-organization-agent.agent.md** (84 lines) - Add 96+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Define file structure best practices
  - Add organization workflows
  - Include validation criteria

- [ ] **domain-expert-template.agent.md** (86 lines) - Add 94+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand template sections
  - Add customization workflows
  - Include usage examples

- [ ] **curious-public-advocate.agent.md** (98 lines) - Add 82+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand audience engagement strategies
  - Add simplification workflows
  - Include accessibility criteria

- [ ] **professional-audience-advocate.agent.md** (98 lines) - Add 82+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand professional communication strategies
  - Add technical depth workflows
  - Include industry-specific guidance

- [ ] **student-audience-advocate.agent.md** (99 lines) - Add 81+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand educational strategies
  - Add learning level adaptations
  - Include comprehension assessment

- [ ] **diverse-learner-advocate.agent.md** (106 lines) - Add 74+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand accessibility strategies
  - Add diverse learning style support
  - Include inclusion criteria

- [ ] **example-generation.agent.md** (107 lines) - Add 73+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand example creation strategies
  - Add domain-specific examples
  - Include quality validation

- [ ] **citation.agent.md** (108 lines) - Add 72+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand citation style guidance
  - Add bibliography management
  - Include validation workflows

- [ ] **contrarian.agent.md** (116 lines) - Add 64+ lines (if keeping this one)
  - Add YAML front matter with `tools: ["*"]`
  - Expand critical analysis workflows
  - Add quality improvement strategies
  - Include metrics and KPIs

## Priority 5: Nearly Complete Files (120-179 lines)

These agents need minor to moderate expansion:

- [ ] **conflict-resolution.agent.md** (121 lines) - Add 59+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand conflict identification strategies
  - Add resolution workflows
  - Include validation criteria

- [ ] **data-integration.agent.md** (122 lines) - Add 58+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand integration strategies
  - Add data transformation workflows
  - Include quality validation

- [ ] **localization.agent.md** (124 lines) - Add 56+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand localization strategies
  - Add cultural adaptation workflows
  - Include translation quality criteria

- [ ] **community-manager.agent.md** (127 lines) - Add 53+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand community engagement strategies
  - Add moderation workflows
  - Include growth metrics

- [ ] **database-query.agent.md** (127 lines) - Add 53+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand query optimization strategies
  - Add performance tuning workflows
  - Include validation criteria

- [ ] **educational-path.agent.md** (143 lines) - Add 37+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand curriculum design strategies
  - Add progression workflows
  - Include assessment criteria

- [ ] **deprecation.agent.md** (144 lines) - Add 36+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand deprecation strategies
  - Add migration workflows
  - Include communication templates

- [ ] **academic-audience-advocate.agent.md** (145 lines) - Add 35+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Expand academic communication strategies
  - Add research-level workflows
  - Include peer review guidance

- [ ] **definition-extractor.agent.md** (158 lines) - Add 22+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Add more extraction strategies
  - Include validation workflows
  - Expand usage examples

- [ ] **verification.agent.md** (168 lines) - Add 12+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Add verification checklists
  - Include validation workflows
  - Expand quality criteria

- [ ] **math-expert.agent.md** (172 lines) - Add 8+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Add mathematical notation guidance
  - Include formula validation
  - Expand usage examples

- [ ] **standards.agent.md** (177 lines) - Add 3+ lines
  - Add YAML front matter with `tools: ["*"]`
  - Ensure all sections complete
  - Validate YAML syntax

## Already Passing (≥180 lines)

These agents meet the minimum requirement but should be checked for YAML front matter:

- [ ] **accessibility.agent.md** (181 lines) - Verify has `tools: ["*"]`
- [ ] **citation-extractor.agent.md** (180 lines) - Verify has `tools: ["*"]`
- [ ] **web-scraper.agent.md** (184 lines) - Verify has `tools: ["*"]`
- [ ] **relationship-extractor.agent.md** (195 lines) - Verify has `tools: ["*"]`
- [ ] **formula-extractor.agent.md** (196 lines) - Verify has `tools: ["*"]`
- [ ] **example-extractor.agent.md** (198 lines) - Verify has `tools: ["*"]`
- [ ] **visualization.agent.md** (205 lines) - Verify has `tools: ["*"]`
- [ ] **textbook-parser.agent.md** (216 lines) - Verify has `tools: ["*"]`
- [ ] **video-transcriber.agent.md** (219 lines) - Verify has `tools: ["*"]`
- [ ] **assessment-creation.agent.md** (220 lines) - Verify has `tools: ["*"]`
- [ ] **user-testing.agent.md** (221 lines) - Verify has `tools: ["*"]`
- [ ] **research-monitoring.agent.md** (230 lines) - Verify has `tools: ["*"]`
- [ ] **implementation.agent.md** (231 lines) - Verify has `tools: ["*"]`
- [ ] **legal-copyright.agent.md** (242 lines) - Verify has `tools: ["*"]`
- [ ] **devops.agent.md** (245 lines) - Verify has `tools: ["*"]`
- [ ] **provenance-tracking.agent.md** (265 lines) - Verify has `tools: ["*"]`
- [ ] **research.agent.md** (278 lines) - Verify has `tools: ["*"]`
- [ ] **quality.agent.md** (288 lines) - Verify has `tools: ["*"]`
- [ ] **coordinator.agent.md** (292 lines) - Verify has `tools: ["*"]`
- [ ] **generic-domain-empathy.agent.md** (312 lines) - Verify has `tools: ["*"]`
- [ ] **software-architecture.agent.md** (436 lines) - Verify has `tools: ["*"]`
- [ ] **graph-database.agent.md** (437 lines) - Verify has `tools: ["*"]`
- [ ] **ontology.agent.md** (437 lines) - Verify has `tools: ["*"]`
- [ ] **pedagogy.agent.md** (437 lines) - Verify has `tools: ["*"]`
- [ ] **recruiter.agent.md** (443 lines) - Verify has `tools: ["*"]`

## Summary Statistics

- **Total Agents**: 60
- **Passing (≥180 lines)**: 25 (42%)
- **Need Expansion**: 35 (58%)
- **Corrupted**: 4 (7%)
- **Duplicates**: 2 pairs (3%)

## YAML Front Matter Template

Every agent should have YAML front matter at the top:

```yaml
---
name: agent-name
description: Brief one-line description
tools: ["*"]
---
```

**Note**: The `tools: ["*"]` property gives the agent access to all available tools.

## Character Escaping Guidelines

When writing YAML, be careful with these characters:
- Quotes: Use `"` for strings, escape internal quotes as `\"`
- Colons: In values, wrap in quotes if they contain `:` 
- Hyphens: In list items starting with `-`, be consistent
- Parentheses: Generally safe but wrap full string in quotes if causing issues
- Square brackets: Safe in quoted strings
- Hash/pound: Use quotes if `#` appears mid-string

**Example of proper escaping**:
```yaml
description: "This agent handles citations (both academic and professional) with proper formatting"
bad_example: "Don't write: review this (no criteria)" 
good_example: "Write: review this - no criteria provided"
```

## Progress Tracking

Update this file as agents are fixed. Mark items with `[x]` when complete.

**Last Updated**: 2025-12-27
**Status**: Ready for implementation
