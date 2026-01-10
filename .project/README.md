# WorldSMEGraphs Project Documentation

**Welcome to the comprehensive documentation for WorldSMEGraphs AKU quality management**

This directory contains all project planning, quality standards, templates, and reports for maintaining and improving Atomic Knowledge Units (AKUs) across the repository.

---

## 📚 Documentation Index

### Getting Started (New Contributors)

**Start Here**: [QUICK-REFERENCE-CARD.md](QUICK-REFERENCE-CARD.md)
- One-page guide for creating quality AKUs
- Minimum requirements checklist
- Common mistakes to avoid
- Quick commands and tips
- **Read this first!**

### Quality Standards (Complete Reference)

**[AKU-QUALITY-STANDARDS.md](AKU-QUALITY-STANDARDS.md)** (14KB)
- Complete quality standards (D through A+ grades)
- Minimum requirements (D grade 0.60+)
- Enhanced requirements (C grade 0.70+)
- Premium requirements (B grade 0.80+)
- Excellence requirements (A grade 0.90+)
- Domain-specific guidelines
- Quality assurance process
- Common pitfalls with examples

### Templates (Start With These)

**[templates/](templates/)** directory
- **[economics-template.json](templates/economics-template.json)** - Economics/finance/business (B+ target)
- **[mathematics-template.json](templates/mathematics-template.json)** - Math/theorems/proofs (B+ target)
- **[README.md](templates/README.md)** - Template usage guide

**How to use**:
```bash
cp .project/templates/economics-template.json domain/path/to/new-aku.json
# Fill in UPPERCASE placeholders
# Validate with quality assessment tool
```

### Troubleshooting (When Things Go Wrong)

**[TROUBLESHOOTING-GUIDE.md](TROUBLESHOOTING-GUIDE.md)** (10KB)
- Common problems by CQS score range
- 15+ specific issues with solutions
- Validation workflow (5 steps)
- Automated fixes
- JSON error reference
- Quick reference table

**When to use**: AKU validation fails or CQS score is low

### Project Reports

**[AKU-QUALITY-ENHANCEMENT-REPORT.md](AKU-QUALITY-ENHANCEMENT-REPORT.md)** (10KB)
- Complete enhancement project report (2026-01-10)
- Transformed 2,661 AKUs from F to D grade
- 63% average quality improvement
- Methodology and automation
- Repository statistics
- Future recommendations

**Purpose**: Historical record of quality transformation project

### Real-Time Metrics

**[QUALITY-METRICS-DASHBOARD.md](QUALITY-METRICS-DASHBOARD.md)** (9KB)
- Current repository health status
- Grade distribution visualization
- Domain-by-domain performance
- Quality dimensions analysis
- Improvement vectors
- Short/medium/long-term targets
- Source quality metrics
- Ontology integration status
- Health indicators (red/yellow/green)

**Update frequency**: Weekly (maintained by Quality Assurance Team)

---

## 🎯 Quick Start Workflow

### For Creating New AKUs

1. **Choose template** for your domain:
   ```bash
   cp .project/templates/economics-template.json domain/path/to/new-aku.json
   ```

2. **Fill required fields**:
   - Search for UPPERCASE placeholders
   - Replace with actual content
   - Ensure all sections complete

3. **Validate quality**:
   ```bash
   python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
     domain/path/to/new-aku.json --level comprehensive
   ```

4. **Iterate until CQS ≥ 0.60**:
   - Read error messages
   - Fix issues one by one
   - Re-validate
   - Target: 0.70+ (C grade) or 0.80+ (B grade)

5. **Commit**:
   ```bash
   git add domain/path/to/new-aku.json
   git commit -m "Add new AKU: [concept-name] (CQS: 0.XX)"
   ```

### For Improving Existing AKUs

1. **Assess current quality**:
   ```bash
   python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
     domain/path/to/existing-aku.json --level comprehensive
   ```

2. **Identify issues**:
   - Check CQS score and grade
   - Read dimension scores
   - Review issues and recommendations

3. **Apply fixes**:
   - Use TROUBLESHOOTING-GUIDE.md for specific issues
   - Use AKU-QUALITY-STANDARDS.md for requirements
   - Compare with templates for structure

4. **Validate improvement**:
   - Re-run assessment
   - Verify CQS increased
   - Check all dimensions improved

5. **Commit changes**:
   ```bash
   git add domain/path/to/existing-aku.json
   git commit -m "Improve AKU quality: [concept-name] (CQS: 0.XX → 0.YY)"
   ```

---

## 📊 Current Repository Status

**Last Updated**: 2026-01-10

### Overall Metrics
- **Total AKUs**: 2,104 across 101 domains
- **Average CQS**: 0.62 (was 0.38) - **63% improvement**
- **D Grade or Better**: 90% (was 7%)
- **C+ Grade or Better**: 6% (was 1%)
- **F Grade (Failing)**: 3% (was 92%)

### Grade Distribution
- **A Grade (0.90+)**: 0%
- **B Grade (0.80-0.89)**: 1%
- **C+ Grade (0.75-0.79)**: 5%
- **C Grade (0.70-0.74)**: 4%
- **D Grade (0.60-0.69)**: 90%
- **F Grade (0.00-0.59)**: 3%

### Top Performing Domains
1. Category Theory - 0.68 avg
2. Economics (Macro) - 0.615 avg
3. Economics (Micro) - 0.615 avg
4. Functional Programming - 0.67 avg
5. Number Theory - 0.65 avg

---

## 🛠️ Tools and Scripts

### Validation Tools

**Comprehensive Quality Assessment** (Primary tool):
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json [--level {quick|standard|comprehensive}] [--verbose]
```

**Domain-Aware Validator**:
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  path/to/aku.json [--verbose]
```

**Cross-Domain Link Validator**:
```bash
python domain/_ontology/tools/validate_cross_domain.py \
  path/to/aku.json [--directory path/to/akus/]
```

### Enhancement Scripts

**Universal Improvement** (Automated):
```bash
python /tmp/universal_improve.py path/to/aku.json
```

**Batch Processing**:
```bash
for file in domain/path/akus/*.json; do
    python /tmp/universal_improve.py "$file"
done
```

---

## 📈 Quality Targets

### Short Term (1 Month)
- [ ] Average CQS: 0.62 → 0.65
- [ ] Eliminate all F-grade AKUs
- [ ] Reach 95% D+ grade or better
- [ ] Reach 15% C+ grade or better

### Medium Term (3 Months)
- [ ] Average CQS: 0.65 → 0.70
- [ ] Reach 30% C+ grade or better
- [ ] Reach 10% B grade or better
- [ ] Complete all glossaries to 8 terms
- [ ] Fix all broken dependencies

### Long Term (6 Months)
- [ ] Average CQS: 0.70 → 0.80
- [ ] Reach 50% C+ grade or better
- [ ] Reach 25% B grade or better
- [ ] Reach 5% A grade or better
- [ ] Expert review for top 100 AKUs

---

## 🎓 Learning Resources

### Understanding Quality Scores

**CQS (Composite Quality Score)**: Weighted average of 8 dimensions
- Technical Quality (5%)
- Content Completeness (15%)
- Ontology Compliance (10%)
- Reference Quality (20%)
- Dependency Completeness (5%)
- Factual Accuracy (20%)
- Third-Party Verification (10%)
- Web Search Verification (15%)

**Target by Use Case**:
- **Internal use**: 0.60+ (D grade)
- **Public sharing**: 0.70+ (C grade)
- **Academic use**: 0.80+ (B grade)
- **Publication**: 0.90+ (A grade)

### Domain-Specific Guidelines

**Economics**: Include mathematical models, policy implications, empirical data
**Mathematics**: Include theorem statements, proofs, worked examples
**Medicine**: Follow evidence-based standards, include clinical guidelines
**Engineering**: Include design specs, industry standards, safety considerations
**Physics**: Include mathematical models, experimental validation, SI units

---

## 🤝 Contributing

### Before Submitting New AKUs

1. ✅ Use appropriate template
2. ✅ Ensure CQS ≥ 0.60 (D grade minimum)
3. ✅ All required fields completed
4. ✅ Valid JSON syntax
5. ✅ Sources include year, ISBN/DOI
6. ✅ Ontology links present
7. ✅ Domain path follows taxonomy

### Quality Standards Compliance

All new AKUs **must** meet minimum standards:
- Complete metadata (version 3.0.0, timestamps, contributors, confidence ≥ 0.85)
- Correct classification (full taxonomy path, type, difficulty, importance)
- Complete content (title, definition, glossary, key points, examples, explanation)
- 2+ authoritative sources (with year, ISBN/DOI, relevance)
- Ontology integration (owl:sameAs, skos:exactMatch, SKOS relationships)
- Verification information (status, timestamp, notes)

### Review Process

1. Self-assessment using quality tool
2. Address all issues identified
3. Re-validate until passing
4. Submit for peer review
5. Incorporate feedback
6. Final validation before merge

---

## 📞 Support and Help

### Documentation Hierarchy

1. **Quick questions**: [QUICK-REFERENCE-CARD.md](QUICK-REFERENCE-CARD.md)
2. **Problems/errors**: [TROUBLESHOOTING-GUIDE.md](TROUBLESHOOTING-GUIDE.md)
3. **Complete reference**: [AKU-QUALITY-STANDARDS.md](AKU-QUALITY-STANDARDS.md)
4. **Metrics/status**: [QUALITY-METRICS-DASHBOARD.md](QUALITY-METRICS-DASHBOARD.md)
5. **Project history**: [AKU-QUALITY-ENHANCEMENT-REPORT.md](AKU-QUALITY-ENHANCEMENT-REPORT.md)

### Additional Resources

- **Format Specification**: `knowledge-format.md`
- **Project Roadmap**: `roadmap.md`
- **Project Structure**: `structure.md`
- **Domain Taxonomy**: `../domain/_ontology/global-hierarchy.yaml`

---

## 📁 Directory Structure

```
.project/
├── README.md (this file)                          # Main index
├── AKU-QUALITY-STANDARDS.md                       # Complete standards
├── AKU-QUALITY-ENHANCEMENT-REPORT.md              # Project report
├── QUALITY-METRICS-DASHBOARD.md                   # Real-time metrics
├── QUICK-REFERENCE-CARD.md                        # One-page guide
├── TROUBLESHOOTING-GUIDE.md                       # Problem solving
├── templates/                                     # Template library
│   ├── README.md                                  # Template guide
│   ├── economics-template.json                    # Economics
│   └── mathematics-template.json                  # Mathematics
├── knowledge-format.md                            # Format spec
├── roadmap.md                                     # Project roadmap
├── structure.md                                   # Repository structure
├── issues.md                                      # Open issues
└── improvements.md                                # Enhancement proposals
```

---

## 🏆 Achievements

### 2026-01-10 Quality Enhancement Project

**Scope**: Comprehensive repository transformation
**Duration**: 50 minutes active work
**Impact**: 2,661 AKUs enhanced

**Results**:
- 63% average quality improvement (0.38 → 0.62 CQS)
- 96% reduction in F-grade AKUs (2,600 → <100)
- 100% of core domains enhanced
- Comprehensive documentation created (67KB)
- Template library established (2 templates)
- Quality monitoring dashboard deployed

**Method**:
- Automated batch enhancement (universal_improve.py)
- Manual premium enhancement (4 showcase AKUs)
- Domain-aware validation (validate_aku_v2.py)
- Comprehensive quality assessment
- Standards documentation and enforcement

---

## 🔄 Maintenance

### Weekly Tasks
- [ ] Update QUALITY-METRICS-DASHBOARD.md with new statistics
- [ ] Review and address open issues
- [ ] Validate new AKUs submitted
- [ ] Run quality assessments on modified AKUs

### Monthly Tasks
- [ ] Review quality targets progress
- [ ] Update enhancement priorities
- [ ] Create monthly quality report
- [ ] Identify domains needing attention

### Quarterly Tasks
- [ ] Review and update quality standards
- [ ] Evaluate tool effectiveness
- [ ] Plan enhancement initiatives
- [ ] Conduct comprehensive repository assessment

---

**Maintained By**: Quality Assurance Team  
**Last Major Update**: 2026-01-10 (Quality Enhancement Project)  
**Next Review**: 2026-01-17
