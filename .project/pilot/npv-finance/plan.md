# NPV Finance Pilot - Project Plan

## Executive Summary

**Objective:** Demonstrate textbook-level knowledge representation for Net Present Value (NPV) using the V2 knowledge format with 50 Atomic Knowledge Units.

**Duration:** Phase 1 (4 weeks)  
**Start Date:** 2025-12-27  
**Team:** 41-agent system with Generic Domain Empathy Agent (Finance Valuation persona)

## Scope

### 50 Atomic Knowledge Units Breakdown

**Definitions (8 AKUs)**
1. NPV core definition
2. Present value concept
3. Future value concept
4. Discount rate definition
5. Cash flow definition
6. Time value of money
7. Investment decision criteria
8. Capital budgeting context

**Formulas (10 AKUs)**
9. Basic NPV formula
10. NPV formula derivation
11. Present value factor formula
12. Annuity NPV formula
13. Perpetuity NPV formula
14. Growing perpetuity NPV formula
15. Multiple cash flows NPV
16. Continuous compounding NPV
17. Nominal vs. real NPV
18. After-tax NPV formula

**Theory (8 AKUs)**
19. Time preference theory
20. Opportunity cost concept
21. Risk-adjusted discount rates
22. WACC as discount rate
23. Fisher's separation theorem
24. NPV decision rule
25. NPV vs. IRR comparison
26. Capital market efficiency assumptions

**Examples (12 AKUs)**
27. Single cash flow example
28. Multiple cash flows example
29. Annuity investment example
30. Equipment replacement example
31. New product launch example
32. Real estate investment example
33. Bond valuation example
34. Project with salvage value example
35. Expansion vs. replacement example
36. Lease vs. buy example
37. International investment example
38. Sensitivity analysis example

**Applications (8 AKUs)**
39. Corporate investment decisions
40. Merger & acquisition valuation
41. Capital budgeting process
42. Portfolio selection
43. Public project evaluation
44. Environmental cost-benefit analysis
45. R&D project selection
46. Strategic investment timing

**Historical (2 AKUs)**
47. Historical development of DCF
48. Key contributors (Irving Fisher, etc.)

**Limitations & Critiques (2 AKUs)**
49. NPV assumptions and limitations
50. Behavioral finance critiques

## Success Criteria

### Quantitative Metrics
- ✅ 50 AKUs created with complete JSON-LD structure
- ✅ Error rate <2% (validation by finance expert persona)
- ✅ All formulas executable (Python + Wolfram)
- ✅ 10+ worked examples with step-by-step solutions
- ✅ Cross-references: 20+ links to related concepts
- ✅ Rendering time <100ms per AKU
- ✅ Storage <50KB per AKU (total <2.5MB)

### Qualitative Metrics
- ✅ Textbook-level completeness (compare to Brealey & Myers)
- ✅ Academic rigor (suitable for graduate finance course)
- ✅ Practical applicability (CFOs can use)
- ✅ Student accessibility (undergraduates can learn)
- ✅ Multi-audience renderings validated by representatives

## Timeline

**Week 1: Foundation (AKUs 1-15)**
- Day 1-2: Definitions & core formulas
- Day 3-4: Formula derivations
- Day 5-7: Theory & mathematical foundations

**Week 2: Examples (AKUs 16-35)**
- Day 8-10: Basic examples
- Day 11-14: Complex real-world examples

**Week 3: Applications & Context (AKUs 36-50)**
- Day 15-17: Business applications
- Day 18-19: Historical context
- Day 20-21: Limitations & critiques

**Week 4: Validation & Graduation**
- Day 22-24: Expert validation
- Day 25-26: User testing
- Day 27-28: Metrics analysis & retrospective

## Agent Workflow

**Research Agents** → Extract NPV content from sources:
- Brealey, Myers & Allen: Principles of Corporate Finance
- Ross, Westerfield & Jaffe: Corporate Finance
- Damodaran: Investment Valuation
- Academic papers on DCF methods

**Extraction Agents** → Create AKU candidates

**Generic Domain Empathy Agent** → Validate using Finance Valuation Expert persona

**Quality Assurance** → Fact-check formulas, references

**Meta-Learning** → Track success metrics, detect quality issues

**Rendering Agent** → Create multi-audience outputs

## Deliverables

1. **50 AKUs in JSON-LD format** (`.project/pilot/npv-finance/akus/`)
2. **Finance Valuation Expert persona** (`.project/pilot/npv-finance/personas/`)
3. **3 audience-specific renderings** (academic, student, professional)
4. **Validation report** (error rates, performance metrics)
5. **Retrospective document** (lessons learned)
6. **Graduation plan** (integration into main knowledge graph)

## Risk Mitigation

**Risk: Insufficient domain expertise**
- Mitigation: Finance Valuation Expert persona with 50+ references

**Risk: Formula errors**
- Mitigation: Executable code validation, numerical tests

**Risk: Scope creep**
- Mitigation: Strict 50 AKU limit, clear boundaries

**Risk: Quality issues**
- Mitigation: Multi-layer validation (persona, QA, users)

## Next Steps

1. Create Finance Valuation Expert persona
2. Set up validation tools
3. Implement first 10 AKUs (definitions + basic formulas)
4. Run initial validation
5. Iterate based on feedback
