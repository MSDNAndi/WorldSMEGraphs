# Domain Maturity Tracking System

Comprehensive tools for assessing, tracking, and managing knowledge domain completeness.

## Overview

The Domain Maturity Tracking system enables data-driven decisions about domain readiness for different use cases by providing:

- **Maturity Assessment**: Quantify domain completeness (5 levels: Nascent → Reference)
- **Gap Analysis**: Identify missing components and prioritize work
- **Progress Tracking**: Historical tracking of domain development
- **Visual Dashboards**: ASCII and HTML visualizations
- **CI/CD Integration**: Automated maturity checks on pull requests

## Quick Start

### Easy Way: Use the Helper Script

```bash
# Show help
./.project/agents/domain-maturity/maturity help

# Assess a domain
./.project/agents/domain-maturity/maturity assess science/physics/quantum-mechanics/planck-units

# View dashboard
./.project/agents/domain-maturity/maturity dashboard

# Generate HTML dashboard
./.project/agents/domain-maturity/maturity dashboard-html > maturity.html

# View history
./.project/agents/domain-maturity/maturity history science/physics/quantum-mechanics/planck-units

# Target level analysis
./.project/agents/domain-maturity/maturity target science/physics/quantum-mechanics/planck-units 3
```

### Direct Python Usage

### 1. Assess a Domain

```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units
```

### 2. View All Domains

```bash
python generate_dashboard.py
```

### 3. Track Progress

```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --save-history

# View history
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --history
```

## Files in This Directory

### Tools

- **`maturity`**: Quick-start helper script (Bash)
  - Simplified interface for common operations
  - Colored output for better readability
  - Example usage built-in

- **`domain_maturity_tracker.py`**: Core assessment tool
  - Scans domains and calculates maturity metrics
  - Identifies gaps and provides recommendations
  - Supports JSON and text output formats
  
- **`generate_dashboard.py`**: Visual dashboard generator
  - Creates ASCII art terminal dashboards
  - Generates interactive HTML dashboards
  - Filter by specific domains

### Data

- **`maturity_history.json`**: Historical tracking data
  - Auto-generated when using `--save-history`
  - Tracks maturity progression over time
  - Used for trend analysis and velocity calculations

## Maturity Levels

| Level | Name | Completeness | Description |
|-------|------|--------------|-------------|
| 1 | **Nascent** 🌱 | 0-20% | Basic groundwork only |
| 2 | **Emerging** 🌿 | 20-40% | Core concepts present |
| 3 | **Established** 🌳 | 40-60% | Ready for expert use |
| 4 | **Comprehensive** 🏛️ | 60-85% | Graduate-level complete |
| 5 | **Reference** 💎 | 85-100% | Publication-quality |

## Usage Examples

### Basic Assessment

```bash
# Assess single domain
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units

# Output: Full maturity report with level, gaps, recommendations
```

### Target Level Analysis

```bash
# See what's needed to reach Level 3
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --target-level 3

# Output: Specific requirements and gaps to close
```

### JSON Output

```bash
# Machine-readable output
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --format json > report.json
```

### Dashboard Generation

```bash
# ASCII dashboard (terminal-friendly)
python generate_dashboard.py

# HTML dashboard (visual, interactive)
python generate_dashboard.py --format html > dashboard.html

# Filter to specific domains
python generate_dashboard.py --domains economics medicine
```

### Historical Tracking

```bash
# Save current state to history
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --save-history

# View historical progress
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --history

# Output:
# 2025-12-28: Level 1 (Nascent) - 0 AKUs (0.0%)
# 2025-12-29: Level 2 (Emerging) - 23 AKUs (29.5%)
```

## Metrics Tracked

### Primary Metrics

1. **Maturity Level** (1-5): Overall domain completeness
2. **Completeness %**: Current AKUs / Target AKUs
3. **AKU Counts**: Total and by type (definitions, formulas, theory, examples, applications)
4. **Type Distribution Score**: How well balanced the content is
5. **Cross-Link Density**: Internal and external connectivity
6. **Validation Pass Rate**: Percentage passing structural/content validation

### Gap Analysis

- Missing AKUs to reach target
- Type imbalances (too many definitions, too few examples)
- Missing critical types for advancement (theory for Level 3+, applications for Level 4+)
- Cross-linking gaps
- Specific recommendations

## Completeness Metadata

Each domain can include a `COMPLETENESS_METADATA.yaml` file with:

```yaml
domain_path: science/physics/quantum-mechanics/planck-units
maturity_level: 2
target_aku_count: 78
critical_gaps:
  - "0 theory AKUs - blocks Level 3"
  - "Missing 19 Planck units"
use_cases:
  - audience: physics_graduate_students
    sufficient: true
  - audience: quantum_gravity_researchers
    sufficient: false
next_priorities:
  - priority: 1
    action: "Split over-bundled AKUs"
    effort: "2-3 hours"
```

**Benefits**:
- Overrides heuristic target calculations
- Documents "good enough" decisions
- Guides development priorities
- Tracks domain-specific quality requirements

## CI/CD Integration

The system includes a GitHub Actions workflow (`.github/workflows/domain-maturity-check.yml`) that:

1. **Detects Changed Domains**: Automatically identifies domains with modified AKUs
2. **Generates Reports**: Creates maturity reports for each changed domain
3. **Posts to PR**: Comments on pull requests with maturity status
4. **Checks Regressions**: Blocks PRs if validation rate drops below 95%
5. **Archives Reports**: Saves reports as artifacts for 30 days

## Decision Framework

### "Is This Domain Good Enough?"

1. **Define Use Case**:
   - Expert consultation (single domain): Level 2+
   - Expert consultation (multi-domain): Level 3+
   - Graduate education: Level 3+
   - K-12 education: Level 4+
   - Publication-quality: Level 4-5

2. **Run Assessment**:
   ```bash
   python domain_maturity_tracker.py --domain <domain-path>
   ```

3. **Check Sufficiency Section**:
   - Review "Sufficient For" and "NOT Sufficient For"
   
4. **Assess Gaps**:
   - **Critical** (must fix): Missing core content, validation failures
   - **Important** (limit use): Missing formulas/examples, sparse cross-links
   - **Nice-to-have**: Language coverage, historical context

5. **Decide**:
   - ✅ **Go**: Meets minimum level, no critical gaps
   - ❌ **Fix First**: Critical gaps present
   - 🚧 **Plan Enhancement**: Schedule work to reach recommended level

## Best Practices

### 1. Regular Assessment

- **Active Development**: Weekly with `--save-history`
- **Mature Domains**: Monthly
- **Reference Domains**: Quarterly

### 2. Gap-Driven Development

1. Run tracker to identify gaps
2. Prioritize critical gaps
3. Fix gaps before new features
4. Re-run to verify

### 3. Quality Over Quantity

- Aim for 100% validation pass rate
- Balance type distribution
- Don't inflate counts artificially

### 4. Set Realistic Targets

- Compare to similar domains
- Expert estimation
- Adjust as understanding deepens

### 5. Track Velocity

```bash
# Historical view shows AKU creation rate
python domain_maturity_tracker.py --domain <domain> --history

# Use to estimate time to next level
```

## Technical Details

### Self-Contained

Both tools use **Python standard library only**:
- No external dependencies
- No `pip install` required
- Compatible with Python 3.8+

### Domain Detection

Automatically detects domains by scanning for:
```
domain/<domain-path>/akus/<type>/*.json
```

### Type Categories

Standard AKU types:
- `definitions/`: Concept definitions
- `formulas/`: Mathematical expressions
- `theory/`: Theoretical explanations
- `examples/`: Worked examples
- `applications/`: Real-world applications

### Cross-Link Detection

Looks for links in AKU `relationships` section:
- `related_to`: Related concepts
- `prerequisite_for`: Prerequisites
- `derived_from`: Derivations
- `applied_in`: Applications

### Target Estimation

If no `COMPLETENESS_METADATA.yaml`:
- Nascent (1-15 AKUs) → Target: 40
- Emerging (16-40 AKUs) → Target: 80
- Established (41-80 AKUs) → Target: 150
- Comprehensive (81+ AKUs) → Target: 2x current

## Troubleshooting

### No Domains Found

**Cause**: No `akus/` directories with JSON files

**Solution**: Check structure: `domain/<path>/akus/<type>/*.json`

### Wrong Maturity Level

**Cause**: Missing or incorrect metadata

**Solution**: Create `COMPLETENESS_METADATA.yaml` with explicit `target_aku_count`

### Zero Cross-Links Detected

**Cause**: Links not in standard `relationships` section

**Solution**: Check AKU structure and format

### Historical Data Lost

**Cause**: `maturity_history.json` deleted

**Solution**: Re-run with `--save-history` on all domains

## Related Documentation

- **Visual Guide**: `VISUAL_GUIDE.md` - ASCII diagrams and flowcharts for visual learners
- **Implementation Summary**: `IMPLEMENTATION_SUMMARY.md` - Complete implementation documentation
- **Maturity Model**: `/.project/knowledge-maturity-model.md` - Detailed model specification
- **Usage Guide**: `/docs/knowledge-maturity-tracking.md` - Comprehensive usage documentation
- **Knowledge Format**: `/.project/knowledge-format-v2.md` - AKU format specification
- **Validation**: `/.project/agents/quality-assurance/tools/validate_aku_v2.py` - AKU validator

## Version

**Version**: 1.0.0  
**Created**: 2025-12-29  
**Author**: Implementation Agent  
**License**: MIT (same as project)

## Support

For issues or questions:
1. Check the comprehensive guide: `/docs/knowledge-maturity-tracking.md`
2. Review maturity model: `/.project/knowledge-maturity-model.md`
3. Open an issue in the repository
