# WorldSMEGraphs AKU Quality - Quick Reference Card

**One-page guide for contributors** | Version 3.0.0 | 2026-01-10

---

## ⚡ Quick Start

```bash
# 1. Copy template
cp .project/templates/economics-template.json domain/path/to/your-aku.json

# 2. Fill required fields (search for UPPERCASE)
# 3. Validate
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  domain/path/to/your-aku.json --level comprehensive

# 4. Iterate until CQS ≥ 0.60
```

---

## 📋 Minimum Checklist (D Grade 0.60+)

- [ ] Metadata complete (version 3.0.0, timestamps, contributors)
- [ ] Classification with full taxonomy path
- [ ] Title and precise definition (50-200 words)
- [ ] Definitions glossary (minimum 4 terms, recommend 8)
- [ ] 3+ key points
- [ ] 1+ example with description and context
- [ ] Statement (one-sentence summary)
- [ ] Explanation (intuition, key_insight, technical_details)
- [ ] 2+ authoritative sources (textbook/journal/academic)
- [ ] Sources with year, ISBN/DOI, relevance
- [ ] owl:sameAs and skos:exactMatch links
- [ ] SKOS relationships (broader, related)
- [ ] Verification status and timestamp

---

## 🎯 Quality Grades

| Grade | CQS | What It Means |
|-------|-----|---------------|
| A+ | 0.95+ | Publication-ready, expert-reviewed |
| A | 0.90+ | Excellent, suitable for academic use |
| B | 0.80+ | High quality, comprehensive |
| C | 0.70+ | Good, meets enhanced standards |
| **D** | **0.60+** | **Minimum acceptable** |
| F | <0.60 | Failing, needs major work |

---

## 🏗️ Domain Taxonomy

Use correct path prefix:

```
formal-sciences/        → Math, CS, Logic
natural-sciences/       → Physics, Chemistry, Biology
social-sciences/        → Economics, Psychology, Sociology
health-sciences/        → Medicine, Nursing, Pharmacy
engineering/            → Electrical, Mechanical, Civil
```

**Example**: `social-sciences/economics/macroeconomics`

---

## 📚 Source Requirements

**Minimum 2 sources** with:

```json
{
  "source": "Author, A. (2021). Title, Ed. Publisher.",
  "type": "textbook",    // or journal, academic, paper
  "year": 2021,          // REQUIRED
  "isbn": "978-XXXXX",   // for books
  "doi": "10.XXX/XXX",   // for articles
  "relevance": "Why cited"
}
```

**Preferred types**: textbook, journal, academic, official documents

---

## 🔗 Ontology Links

**Required at top level**:
```json
{
  "owl:sameAs": "http://dbpedia.org/resource/Concept_Name",
  "skos:exactMatch": "http://www.wikidata.org/entity/Q12345"
}
```

**Required in relationships**:
```json
{
  "skos:broader": ["http://dbpedia.org/resource/Broader_Category"],
  "skos:related": ["http://dbpedia.org/resource/Related_Concept"]
}
```

---

## 💡 Quick Tips

1. **Be specific**: "Sustained price increase" not "Rising price levels"
2. **Add context**: Every example needs "why it matters"
3. **Recent sources**: Prefer publications within 5 years
4. **Real examples**: Use actual data, historical events, current cases
5. **Define terms**: Never use technical terms without glossary entry

---

## ❌ Common Mistakes

| Bad | Good |
|-----|------|
| domain_path: "economics/" | domain_path: "social-sciences/economics/" |
| "Standard reference" | "Mankiw (2021), ISBN 978-..." |
| No glossary | 4-8 terms defined |
| Generic examples | Specific with data and context |
| No ontology links | owl:sameAs + skos links |

---

## 🛠️ Tools

**Validate quality**:
```bash
python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
  path/to/aku.json --level comprehensive
```

**Check format**:
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  path/to/aku.json
```

**Batch enhance** (if needed):
```bash
python /tmp/universal_improve.py path/to/aku.json
```

---

## 📊 Target Scores by Dimension

| Dimension | Minimum | Target | Premium |
|-----------|---------|--------|---------|
| Technical Quality | 1.00 | 1.00 | 1.00 |
| Content Completeness | 0.70 | 0.80 | 0.90 |
| Ontology Compliance | 0.70 | 0.85 | 0.95 |
| Reference Quality | 0.60 | 0.80 | 0.95 |
| Factual Accuracy | 0.60 | 0.75 | 0.90 |

---

## 🚀 From D to B Grade

**Add for C (0.70+)**:
- 4+ sources (not just 2)
- Historical context
- Policy implications (if applicable)
- 4+ examples (not just 1)

**Add for B (0.80+)**:
- 6+ sources
- Mathematical formulations (STEM)
- Pedagogical content
- Common misconceptions
- Cross-domain links

---

## 📖 Full Documentation

- **Standards**: `.project/AKU-QUALITY-STANDARDS.md`
- **Report**: `.project/AKU-QUALITY-ENHANCEMENT-REPORT.md`
- **Dashboard**: `.project/QUALITY-METRICS-DASHBOARD.md`
- **Templates**: `.project/templates/`

---

## 🆘 Need Help?

1. Review template for your domain
2. Check similar high-quality AKUs
3. Run validation and read error messages
4. See full standards document

---

**Remember**: D grade (0.60) is minimum. Aim for C (0.70) or B (0.80)!
