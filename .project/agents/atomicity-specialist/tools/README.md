# AKU Atomicity Specialist Tools

Tools for analyzing and managing Atomic Knowledge Unit (AKU) granularity.

## Available Tools

### 1. Atomicity Analyzer (`analyze_atomicity.py`)

Analyzes AKUs to detect atomicity violations - over-bundled units with multiple concepts or under-specified fragments.

**Features:**
- Detects over-bundled AKUs (multiple concepts in one unit)
- Identifies under-specified fragments (too small to be useful)
- Calculates atomicity scores (0.0 - 1.0)
- Provides split/merge recommendations
- Supports single file or directory analysis

**Usage:**

```bash
# Analyze single AKU
python analyze_atomicity.py path/to/aku.json

# Analyze single AKU with verbose output
python analyze_atomicity.py path/to/aku.json --verbose

# Analyze entire directory
python analyze_atomicity.py --directory domain/social-sciences/economics/bwl/finance/

# Analyze by domain path
python analyze_atomicity.py --domain economics/bwl/finance/valuation/npv
```

**Example Output:**

```
============================================================
Analyzing Atomicity: example-npv-definition.json
============================================================

Status: OVER_BUNDLED
Recommendation: SPLIT
Atomicity Score: 0.30 / 1.0
Concept Count: 8
Is Fragment: False

Rationale: Contains 8 distinct concepts - should be split into atomic units

Detected Concepts:
  1. Definition (682 bytes)
  2. Formula (588 bytes)
  3. Advantages (259 bytes)
  4. Limitations (335 bytes)
  5. Applications (265 bytes)

Content Keys: definition, formula, decision_rule, components, 
              example_calculation, advantages, limitations, 
              applications, related_concepts, references
```

**Directory Analysis Summary:**

```
============================================================
ATOMICITY ANALYSIS SUMMARY
============================================================
Total AKUs Analyzed: 25
  ✅ Atomic (1 concept): 18 (72.0%)
  🔴 Over-bundled (>1 concept): 5 (20.0%)
  🟡 Under-specified (fragment): 2 (8.0%)
  ⚪ Unclear: 0 (0.0%)

Average Atomicity Score: 0.85 / 1.0

⚠️  SPLIT RECOMMENDATIONS:
   - aku-npv-complete.json (8 concepts)
   - aku-capm-full.json (5 concepts)
   - aku-irr-comparison.json (3 concepts)

⚠️  MERGE RECOMMENDATIONS:
   - aku-discount-rate-symbol.json (fragment)
   - aku-cf-notation.json (fragment)
```

## Atomicity Scoring

The analyzer calculates an atomicity score from 0.0 to 1.0:

- **1.0**: Perfectly atomic (exactly 1 concept)
- **0.7**: Slightly over-bundled (2 concepts)
- **0.5**: Moderately over-bundled (3-4 concepts)
- **0.3**: Severely over-bundled (5+ concepts) OR under-specified fragment

## Detection Heuristics

### Over-Bundling Indicators
The analyzer looks for multiple major sections in an AKU:
- `definition` + `formula` (likely 2 concepts)
- `definition` + `example_calculation` (likely 2 concepts)
- `advantages` + `limitations` (often separate concepts)
- `procedure` + `applications`
- `theorem` + `proof`
- `symptoms` + `diagnosis` + `treatment`

### Under-Specification Indicators
The analyzer identifies fragments that are too small:
- Content size < 200 bytes
- Only contains: `symbol`, `notation`, `unit`, `abbreviation`
- Limited content keys (≤ 2 sections)

## Integration with AKU Atomicity Specialist Agent

This tool is designed to support the `@aku-atomicity-specialist` agent:

```bash
# Agent invocation example
@aku-atomicity-specialist Analyze domain/social-sciences/economics/bwl/finance/valuation/npv/ 
for atomicity violations using analyze_atomicity.py tool. Provide split/merge 
recommendations with rationale.
```

The agent can use this tool's output to:
1. Identify which AKUs need transformation
2. Prioritize split/merge operations
3. Track atomicity improvements over time
4. Generate audit reports

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Future Enhancements

Planned improvements for atomicity analysis:

1. **Machine Learning**: Train models on validated AKUs to improve detection
2. **Domain-Specific Rules**: Custom heuristics for math, medicine, economics
3. **Relationship Analysis**: Consider prerequisite chains when scoring
4. **Learning Analytics**: Use learner performance data to refine granularity
5. **Automatic Splitting**: Generate split plans with new AKU IDs
6. **Merge Suggestions**: Identify related fragments that should be combined
7. **Visualization**: Graph concept boundaries and relationships
8. **Batch Processing**: Process hundreds of AKUs efficiently
9. **CI/CD Integration**: Validate atomicity on commit
10. **Confidence Intervals**: Statistical confidence in atomicity assessments

## Related Documentation

- **Agent**: `.github/agents/aku-atomicity-specialist.agent.md`
- **Documentation**: `docs/agents/aku-atomicity-specialist.md`
- **AKU Schema**: Domain-specific schema files
- **Validators**: `.project/agents/quality-assurance/tools/validate_aku_v2.py`

## Contributing

To improve atomicity detection:

1. **Add Domain Rules**: Update `OVER_BUNDLED_INDICATORS` for your domain
2. **Refine Scoring**: Adjust `_calculate_atomicity_score()` weights
3. **New Heuristics**: Add detection logic in `_count_concepts()`
4. **Test Cases**: Validate on known atomic/non-atomic AKUs
5. **Documentation**: Update this README with new features

## Version History

- **v1.0** (2025-12-29): Initial release
  - Basic over-bundling detection
  - Fragment identification
  - Atomicity scoring
  - Directory analysis with summaries
  - Verbose output mode
