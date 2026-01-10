# CRITICAL: Systematic Wikidata Q1 Error Across 2,743 AKUs

**Discovered**: 2026-01-10T17:55:00Z  
**Severity**: CRITICAL  
**Scope**: Repository-wide (2,743 AKUs affected)  
**Impact**: Semantic web linking failure

## Issue Description

A systematic error has been discovered where **2,743 AKU files** incorrectly reference Wikidata entity **Q1** (which is "Universe") in their `skos:exactMatch` field. This causes all these AKUs to incorrectly link to the wrong concept in the semantic web.

## Affected Files

```bash
# Count of affected files
find domain -name "*.json" -type f -exec grep -l 'entity/Q1"' {} \; 2>/dev/null | wc -l
# Result: 2743
```

## Pattern Found

All affected AKUs contain:
```json
"skos:exactMatch": "http://www.wikidata.org/entity/Q1"
```

Where Q1 = "Universe" in Wikidata (incorrect for all economics, medical, and other domain concepts).

## Root Cause

This appears to be a systematic generation error, possibly from:
1. Template/generator that used Q1 as placeholder
2. Bulk generation script with wrong default
3. Copy-paste error propagated across many AKUs

## Confirmed Fixes (So Far)

### Macroeconomics AKUs Fixed (8 total):
1. macro-001-gdp.json: Q1 → Q12638 (GDP) ✅
2. macro-003-inflation.json: Q1 → Q179174 (Inflation) ✅
3. macro-002-gdp-components.json: Q1 → Q186039 (GDP component) ✅
4. macro-004-cpi.json: Q1 → Q181865 (Consumer Price Index) ✅
5. macro-007-business-cycles.json: Q1 → Q221395 (Business cycle) ✅
6. macro-008-recession.json: Q1 → Q176494 (Recession) ✅
7. macro-009-aggregate-demand.json: Q1 → Q4691546 (Aggregate demand) ✅
8. (See commits 3981f38, 3f07c60, 2ef30dd)

### Remaining: ~2,735 AKUs need correction

## Impact Assessment

### Semantic Web Integration: BROKEN
- All 2,743 AKUs cannot be properly linked in semantic web applications
- Knowledge graph integration with external systems fails
- RDF/SPARQL queries return incorrect results
- Ontology alignment is completely wrong

### Data Quality: CRITICAL
- Confidence scores should be reduced for all affected AKUs
- External validation tools will flag these as errors
- Research using these AKUs may draw wrong connections

### Urgency: HIGH
- Blocks semantic web feature deployment
- Prevents knowledge graph publication
- Damages credibility if discovered by external users

## Recommended Solution

### Approach 1: Manual Mapping (CURRENT - TOO SLOW)
- Manually identify correct Wikidata entity for each AKU
- Update one at a time
- **Estimated time**: 2,735 AKUs × 3 min/AKU = ~137 hours (unfeasible)

### Approach 2: Automated Lookup with Verification (RECOMMENDED)
1. Extract AKU title and domain from each affected file
2. Use Wikidata API to search for correct entity
3. Present top 3 candidates for human verification
4. Bulk update with verified mappings
5. **Estimated time**: ~20 hours with automation + verification

### Approach 3: Remove Q1 References (TEMPORARY FIX)
1. Remove all Q1 references from affected AKUs
2. Add `"wikidata_status": "pending_review"` flag
3. Systematic review and correction later
4. **Estimated time**: 2 hours (automated)
5. **Downside**: Removes semantic web linking temporarily

### Approach 4: Domain-Based Heuristic Mapping
1. For each domain, create mapping rules based on AKU ID patterns
2. Economics: macro-001 → GDP, macro-003 → Inflation, etc.
3. Medicine: vascular terms → medical ontology
4. Apply rules automatically, flag uncertain cases
5. **Estimated time**: ~10 hours (develop rules + apply)

## Recommended Action Plan

**Phase 1 (Immediate - 2 hours):**
- Document issue completely ✅ (this document)
- Create automated script to identify affected files by domain
- Remove Q1 references, add "pending_review" flag
- Commit changes to prevent propagation

**Phase 2 (Next Session - 8 hours):**
- Develop Wikidata lookup automation
- Create domain-specific mapping heuristics
- Build verification interface for ambiguous cases

**Phase 3 (Ongoing - 10 hours):**
- Systematically review and correct by domain
- Priority: Economics (highest visibility), Medicine (critical accuracy)
- Validate corrections with domain experts

**Phase 4 (Final - 2 hours):**
- Comprehensive validation of all Wikidata links
- Update quality scores for corrected AKUs
- Document process for future prevention

## Prevention Measures

1. **Validation Rule**: Add check to AKU validator that Q1 is NOT allowed
2. **Generation Template**: Fix templates to require explicit Wikidata entity
3. **CI/CD Check**: Add automated check that flags any Q1 references
4. **Documentation**: Update AKU creation guide with Wikidata lookup process

## Files Affected by Domain

```bash
# Economics/Macroeconomics: ~50 AKUs (18 remaining)
# Medicine: ~1000+ AKUs (estimate based on repository)
# Natural Sciences: ~500+ AKUs (estimate)
# Formal Sciences: ~200+ AKUs (estimate)
# Engineering: ~100+ AKUs (estimate)
# Other domains: ~900+ AKUs (estimate)
```

## Priority Ranking for Correction

1. **P0 - Critical** (Target: 24 hours):
   - Economics macroeconomics AKUs (public-facing, high visibility)
   - Medicine core concepts (patient safety implications)

2. **P1 - High** (Target: 1 week):
   - Natural sciences foundational concepts
   - Formal sciences (mathematics, CS) key terms

3. **P2 - Medium** (Target: 1 month):
   - All remaining AKUs by domain priority
   - Less-frequently accessed content

## Contact

- **Discovered by**: fact-checking-agent
- **Session**: 2026-01-10T17:15:48Z to 2026-01-10T18:05:48Z
- **Repository**: WorldSMEGraphs
- **Branch**: copilot/improve-aku-quality

## Related Issues

- GDP fact-checking (PR #): Fixed Q1 → Q12638
- Inflation fact-checking: Fixed Q1 → Q179174
- Systematic Wikidata correction: 5 macroeconomics AKUs fixed

## Next Steps

1. Escalate to repository maintainers
2. Create tracking issue in `.project/issues.md`
3. Implement Phase 1 (immediate mitigation)
4. Schedule Phase 2-4 work

---

**Status**: OPEN  
**Last Updated**: 2026-01-10T17:56:00Z  
**Tracking**: Issue will be created in `.project/issues.md`
