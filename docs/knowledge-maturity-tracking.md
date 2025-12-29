# Knowledge Maturity Tracking

## Overview

The Knowledge Maturity Tracking system provides comprehensive tools for assessing, tracking, and managing the completeness and development level of knowledge domains within WorldSMEGraphs. It enables data-driven decisions about domain readiness for different use cases.

## Table of Contents

- [Quick Start](#quick-start)
- [Understanding Maturity Levels](#understanding-maturity-levels)
- [Using the Tracker Tool](#using-the-tracker-tool)
- [Using the Dashboard](#using-the-dashboard)
- [Completeness Metadata](#completeness-metadata)
- [Decision Framework](#decision-framework)
- [Case Studies](#case-studies)
- [CI/CD Integration](#cicd-integration)
- [Best Practices](#best-practices)

---

## Quick Start

### 1. Assess a Single Domain

```bash
cd /path/to/WorldSMEGraphs
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units
```

**Output**: Comprehensive maturity report with level, completeness %, AKU counts, gaps, and recommendations.

### 2. View All Domains

```bash
python .project/agents/domain-maturity/generate_dashboard.py
```

**Output**: ASCII art dashboard showing all domains with maturity levels and progress bars.

### 3. Track Historical Progress

```bash
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --save-history

# View history later
python .project/agents/domain-maturity/domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --history
```

---

## Understanding Maturity Levels

### The Five Levels

| Level | Name | Completeness | Description | Use Cases |
|-------|------|--------------|-------------|-----------|
| 1 | **Nascent** | 0-20% | Basic groundwork only | Research, proof-of-concept |
| 2 | **Emerging** | 20-40% | Core concepts present | Expert reference (single domain) |
| 3 | **Established** | 40-60% | Ready for expert use | Graduate coursework, multi-domain queries |
| 4 | **Comprehensive** | 60-85% | Graduate-level complete | Education, publication-quality |
| 5 | **Reference** | 85-100% | Authoritative | Academic citation, global reference |

### Level Details

#### Level 1: Nascent 🌱
- **AKU Count**: 1-15
- **Distribution**: 80% definitions, 15% formulas, 5% examples
- **Cross-Links**: <5%
- **Sufficient For**: Initial research, domain scoping
- **NOT Sufficient For**: Production use, education

#### Level 2: Emerging 🌿
- **AKU Count**: 16-40
- **Distribution**: 65% definitions, 20% formulas, 10% examples, 5% theory
- **Cross-Links**: 10-20%
- **Sufficient For**: Expert-level reference (isolated queries)
- **NOT Sufficient For**: Complex interconnected questions

#### Level 3: Established 🌳
- **AKU Count**: 41-80
- **Distribution**: 45% definitions, 25% formulas, 12% theory, 12% examples, 6% applications
- **Cross-Links**: 30-40%
- **Sufficient For**: Expert consultation, graduate coursework
- **NOT Sufficient For**: Publication-quality reference

#### Level 4: Comprehensive 🏛️
- **AKU Count**: 81-150
- **Distribution**: 35% definitions, 27% formulas, 17% theory, 17% examples, 12% applications
- **Cross-Links**: 50-70%
- **Sufficient For**: Complete curricula, professional training
- **NOT Sufficient For**: Exhaustive academic coverage

#### Level 5: Reference 💎
- **AKU Count**: 150+
- **Distribution**: Balanced across all types
- **Cross-Links**: 70-90%
- **Sufficient For**: Authoritative reference, academic publication
- **Maintenance**: Quarterly updates required

---

## Using the Tracker Tool

### Basic Commands

#### Scan Single Domain
```bash
python domain_maturity_tracker.py --domain <domain-path>
```

**Example**:
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units
```

#### Scan All Domains
```bash
python domain_maturity_tracker.py --all
```

#### JSON Output
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --format json > planck_maturity.json
```

### Advanced Features

#### Target Level Analysis
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --target-level 3
```

**Output**: Shows exactly what's needed to reach Level 3 (Established):
- AKU count gap
- Type distribution targets
- Critical requirements

#### Save to History
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --save-history
```

**Use Case**: Track progress over time. Run this after significant domain updates.

#### View Historical Progress
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --history
```

**Output**:
```
2025-12-28: Level 1 (Nascent) - 0 AKUs (0.0%)
2025-12-29: Level 2 (Emerging) - 23 AKUs (29.5%)
```

### Understanding the Report

#### Sample Report Sections

**1. Maturity Level**
```
Maturity Level: 2 - Emerging (28.7% complete)
```
- Current level and name
- Completeness percentage (current AKUs / target AKUs)

**2. AKU Counts**
```
AKU Count: 23 / 80 (target)

By Type:
  - Definitions: 15 (65.2%)
  - Formulas: 5 (21.7%)
  - Examples: 3 (13.0%)
```
- Total vs target
- Breakdown by type with percentages

**3. Type Distribution Score**
```
Type Distribution Score: 0.95 (1.0 = perfect balance)
```
- How well the distribution matches the ideal for this maturity level
- 1.0 = perfect, 0.0 = completely wrong

**4. Cross-Links**
```
Cross-Links:
  - Internal: 0 (0.0% density)
  - External: 0 (0.0% density)
  - Total: 0
```
- Internal: links between AKUs in same domain
- External: links to other domains
- Density: percentage of potential connections established

**5. Critical Gaps**
```
Critical Gaps & Recommendations:
  1. 57 more AKUs needed to reach target (80)
  2. 1 theory AKUs needed for Level 3
  3. Over-emphasis on definitions; add more formulas and examples
```
- Prioritized list of what's missing
- Specific recommendations

**6. Sufficiency Assessment**
```
Sufficient For:
  ✓ Expert-level reference (single domain queries)

NOT Sufficient For:
  ✗ Expert consultation on interconnected questions
  ✗ Graduate-level complete coursework
```
- Clear yes/no on what the domain can support

**7. Next Steps**
```
Next Steps to Reach Level 3 (Established):
  • 57 more AKUs needed to reach target (80)
  • Add theory AKUs (target 10% of total)
  • Establish cross-domain connections
```
- Concrete actions to advance to next level

---

## Using the Dashboard

### ASCII Dashboard

```bash
python generate_dashboard.py
```

**Output**: Terminal-friendly visual dashboard

**Features**:
- Summary statistics (total domains, AKUs, average maturity)
- Progress bars for each domain
- Emoji indicators for maturity levels
- Top priority gap for each domain
- Color-coded by level (via border characters)

### HTML Dashboard

```bash
python generate_dashboard.py --format html > dashboard.html
open dashboard.html  # macOS
xdg-open dashboard.html  # Linux
start dashboard.html  # Windows
```

**Features**:
- Interactive, visually appealing web dashboard
- Animated progress bars
- Color-coded cards by maturity level
- Hover effects
- Responsive design
- Legend explaining levels

### Filter by Domains

```bash
python generate_dashboard.py --domains economics medicine
```

**Use Case**: Focus dashboard on specific domains

---

## Completeness Metadata

### What Is It?

`COMPLETENESS_METADATA.yaml` is a manually maintained file in each domain that provides:
- Explicit target AKU count
- Critical gaps identified
- Use case sufficiency assessment
- Next development priorities
- Quality metrics

### Location

```
domain/
  science/
    physics/
      quantum-mechanics/
        planck-units/
          COMPLETENESS_METADATA.yaml  ← Here
          akus/
            definitions/
            formulas/
            ...
```

### Template

```yaml
# Domain Completeness Metadata
domain_path: science/physics/quantum-mechanics/planck-units
maturity_level: 2  # Emerging
completeness_percentage: 29%
last_updated: 2025-12-29

# AKU Statistics
aku_count:
  total: 23
  definitions: 15
  formulas: 5
  theory: 0
  examples: 3

target_aku_count: 78

# Critical Gaps
critical_gaps:
  - "0 theory AKUs - blocks Level 3"
  - "Missing 19 Planck units"

# Use Cases
use_cases:
  - audience: physics_graduate_students
    sufficient: true
    notes: "Core concepts covered"
  
  - audience: quantum_gravity_researchers
    sufficient: false
    notes: "Need theory AKUs"

# Next Priorities
next_priorities:
  - priority: 1
    action: "Split over-bundled AKUs"
    effort: "2-3 hours"
  
  - priority: 2
    action: "Add missing units"
    effort: "1 week"
```

### Why Metadata?

**1. Overrides Heuristics**
- Tracker uses heuristic target AKU count if metadata absent
- Metadata provides expert-defined target

**2. Documents Decisions**
- Records "good enough" decisions
- Explains sufficiency for use cases

**3. Guides Development**
- Prioritizes next work
- Estimates effort

**4. Tracks Quality**
- Cross-link goals
- Validation requirements

### When to Update

- After adding significant AKUs (10+)
- When maturity level changes
- After external review/feedback
- When use case requirements change
- Quarterly review minimum

---

## Decision Framework

### Question: "Is This Domain Good Enough?"

#### Step 1: Define Use Case

**Options**:
- Expert consultation (single domain)
- Expert consultation (multi-domain)
- Graduate education
- K-12 education
- General public education
- Publication-quality reference
- Multi-lingual expert translation

#### Step 2: Check Minimum Level

| Use Case | Minimum Level | Recommended |
|----------|---------------|-------------|
| Expert (single domain) | 2 | 3 |
| Expert (multi-domain) | 3 | 4 |
| Graduate education | 3 | 4 |
| K-12 education | 4 | 4-5 |
| General public | 3 | 4 |
| Publication quality | 4 | 5 |
| Multi-lingual (5-10 languages) | 3 | 4 |

#### Step 3: Run Tracker

```bash
python domain_maturity_tracker.py --domain <domain-path>
```

#### Step 4: Review Sufficiency

Look at the "Sufficient For" and "NOT Sufficient For" sections.

#### Step 5: Assess Gaps

**Critical Gaps** (must fix):
- Missing core definitions
- Zero cross-links
- Validation failures
- Factual errors

**Important Gaps** (limit use cases):
- Missing formulas
- No examples
- Single audience
- Sparse cross-links

**Nice-to-Have** (quality improvements):
- Limited languages
- Missing applications
- No historical context

#### Step 6: Make Decision

**Go**: Domain meets minimum level, no critical gaps
**Fix Critical Gaps First**: Don't proceed until fixed
**Plan Enhancement**: Schedule work to reach recommended level

---

## Case Studies

### Case Study 1: Planck Units Domain

**Situation**: 23 AKUs created, need to decide if ready for use

**Assessment**:
```bash
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units
```

**Result**: Level 2 (Emerging), 29% complete

**Decision**:
- **Use Case**: Graduate student coursework (isolated topic)
  - **Verdict**: ✅ **SUFFICIENT**
  - **Rationale**: Core definitions and formulas present, examples provided
  
- **Use Case**: Quantum gravity research (interconnected)
  - **Verdict**: ❌ **NOT SUFFICIENT**
  - **Rationale**: Missing theory AKUs, zero cross-links, only 29% complete
  - **Action**: Need Level 3, add theory AKUs and cross-links

**Next Steps**:
1. Add 11 theory AKUs (quantum foam, holographic principle)
2. Add 19 missing Planck units
3. Establish cross-links to GR and QM
4. Target: Level 3 (Established) - 60-80 AKUs

### Case Study 2: NPV Pilot Completion

**Situation**: Phase 1 pilot ending, assess if goals met

**Target State**: 50 AKUs, Level 3, multi-audience, multi-lingual

**Assessment**:
```bash
python domain_maturity_tracker.py \
  --domain economics/bwl/finance/valuation/npv \
  --target-level 3
```

**Expected Result**: Level 3 (Established), 62% complete

**Decision**:
- **Phase 1 Goals**: ✅ **MET**
  - 50 AKUs achieved
  - Level 3 reached
  - 2 audience renderings
  - 10 German translations
  
- **Ready for Phase 2**: ✅ **YES**
  - Sufficient foundation for expansion
  - Quality metrics meet standards
  - Cross-links established

**Next Steps**: Proceed to Phase 2 (expand to CAPM, DCF, Budgeting)

### Case Study 3: Medicine Domain - Type 2 Endoleaks

**Situation**: 8 AKUs created, clinical application proposed

**Assessment**:
```bash
python domain_maturity_tracker.py \
  --domain medicine/surgery/vascular/complications/endoleaks/type-2
```

**Result**: Level 1 (Nascent), 20% complete

**Decision**:
- **Use Case**: Clinical decision support
  - **Verdict**: ❌ **NOT SUFFICIENT**
  - **Rationale**: Only 8 AKUs, missing treatment protocols, no diagnosis AKUs
  - **Risk**: Patient safety - incomplete information
  
- **Action**: **BLOCK** clinical use until Level 3
  - Add 32 more AKUs
  - Complete diagnosis section
  - Add treatment protocols
  - External medical review required

---

## CI/CD Integration

### Workflow: Domain Maturity Check

**File**: `.github/workflows/domain-maturity-check.yml`

```yaml
name: Domain Maturity Check

on:
  pull_request:
    paths:
      - 'domain/**/*.json'

jobs:
  check-maturity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Scan affected domains
        run: |
          # Extract changed domains
          CHANGED_DOMAINS=$(git diff --name-only origin/main... | \
            grep '^domain/' | \
            cut -d'/' -f1-5 | \
            sort -u)
          
          for domain in $CHANGED_DOMAINS; do
            python .project/agents/domain-maturity/domain_maturity_tracker.py \
              --domain $domain \
              --format json > "${domain//\//_}_maturity.json"
          done
      
      - name: Check for regressions
        run: |
          # Compare with baseline (if exists)
          # Alert if maturity level decreased
          # Block if validation pass rate decreased
          python .github/scripts/check-maturity-regression.py
      
      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            // Post maturity report as PR comment
            const fs = require('fs');
            const reports = fs.readdirSync('.')
              .filter(f => f.endsWith('_maturity.json'))
              .map(f => JSON.parse(fs.readFileSync(f)));
            
            const comment = reports.map(r => 
              `## ${r.domain_path}\n` +
              `**Maturity**: Level ${r.maturity_level} (${r.maturity_name})\n` +
              `**Completeness**: ${r.completeness_percentage}%\n` +
              `**AKUs**: ${r.aku_counts.total}/${r.aku_counts.target}\n`
            ).join('\n---\n');
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
      
      - name: Save history
        run: |
          for domain in $CHANGED_DOMAINS; do
            python .project/agents/domain-maturity/domain_maturity_tracker.py \
              --domain $domain \
              --save-history
          done
```

### Benefits

1. **Automatic Tracking**: Every PR updates maturity history
2. **Regression Detection**: Blocks PRs that decrease maturity
3. **Visibility**: Team sees maturity status in PR comments
4. **Historical Data**: Automatic history log for trend analysis

---

## Best Practices

### 1. Regular Assessment

**Frequency**:
- **Active Development**: Weekly assessments
- **Mature Domains**: Monthly assessments
- **Reference Domains**: Quarterly reviews

**Command**:
```bash
# Weekly assessment with history save
python domain_maturity_tracker.py \
  --domain science/physics/quantum-mechanics/planck-units \
  --save-history
```

### 2. Gap-Driven Development

**Workflow**:
1. Run tracker to identify gaps
2. Prioritize critical gaps (block advancement)
3. Address gaps before new features
4. Re-run tracker to verify

**Example**:
```bash
# Identify gaps
python domain_maturity_tracker.py --domain <domain> | grep "Critical Gaps"

# After fixing, verify
python domain_maturity_tracker.py --domain <domain>
```

### 3. Quality Over Quantity

**Don't**:
- Inflate AKU count with low-quality content
- Split AKUs artificially to increase numbers
- Advance maturity level with critical gaps

**Do**:
- Focus on validation pass rate (aim for 100%)
- Prioritize cross-link quality over density
- Ensure balanced type distribution

### 4. Set Realistic Targets

**How to Set Target AKU Count**:
1. Compare to similar domains (reference)
2. Expert estimation of scope
3. Adjust based on complexity
4. Update as understanding deepens

**Don't**:
- Use arbitrary numbers (e.g., "100 sounds good")
- Set targets to appear more complete
- Keep outdated targets

### 5. Document Decisions

**Use COMPLETENESS_METADATA.yaml**:
- Record "good enough" decisions
- Explain sufficiency for use cases
- Document expert assessments
- Track quality metrics

### 6. Multi-Dimensional Growth

**Balance**:
- AKU count growth **+** cross-linking
- Content creation **+** audience coverage
- Depth **+** breadth

**Don't**:
- Only focus on AKU count
- Ignore cross-links until later
- Forget multi-audience rendering

### 7. Use History for Velocity

**Track Velocity**:
```bash
# View historical progress
python domain_maturity_tracker.py --domain <domain> --history
```

**Calculate**:
- AKUs per week
- Weeks to next maturity level
- Adjust targets based on actual velocity

---

## Troubleshooting

### Issue: Tracker Shows Wrong Maturity Level

**Cause**: Metadata file missing or heuristic target incorrect

**Solution**:
1. Create `COMPLETENESS_METADATA.yaml`
2. Set explicit `target_aku_count`
3. Re-run tracker

### Issue: Dashboard Shows No Domains

**Cause**: No `akus/` directories with JSON files

**Solution**:
1. Verify domain structure: `domain/[path]/akus/[type]/*.json`
2. Check for JSON files: `find domain -name "*.json" -type f`

### Issue: Historical Data Lost

**Cause**: `maturity_history.json` deleted or corrupted

**Solution**:
1. Re-run tracker with `--save-history` on all domains
2. Backup history file regularly
3. Store in version control (`.gitignore` exceptions)

### Issue: Cross-Link Count Zero Despite Links

**Cause**: Links not in standard `relationships` section

**Solution**:
1. Check AKU structure: `relationships.related_to`, `relationships.prerequisite_for`, etc.
2. Verify link format: `["domain/path/to/aku"]`
3. Run validator: `validate_aku_v2.py`

---

## Reference

### Tracker Options

```
--domain <path>        Domain to scan
--all                  Scan all domains
--history              Show historical progress
--target-level N       Show requirements for level N
--format json|text     Output format
--save-history         Save to history log
```

### Dashboard Options

```
--format ascii|html    Output format
--domains <d1> <d2>    Filter to specific domains
```

### Maturity Level Reference

| Level | Name | % Complete | AKU Range | Key Characteristics |
|-------|------|------------|-----------|---------------------|
| 1 | Nascent | 0-20% | 1-15 | Basic definitions only |
| 2 | Emerging | 20-40% | 16-40 | Core concepts present |
| 3 | Established | 40-60% | 41-80 | Ready for expert use |
| 4 | Comprehensive | 60-85% | 81-150 | Graduate-level complete |
| 5 | Reference | 85-100% | 150+ | Publication-quality |

---

## Additional Resources

- **Maturity Model Specification**: `.project/knowledge-maturity-model.md`
- **Knowledge Format**: `.project/knowledge-format-v2.md`
- **AKU Validation**: `.project/agents/quality-assurance/tools/validate_aku_v2.py`
- **Project Structure**: `.project/structure.md`

---

**Version**: 1.0.0  
**Last Updated**: 2025-12-29  
**Maintained By**: Implementation Agent, Quality Agent
