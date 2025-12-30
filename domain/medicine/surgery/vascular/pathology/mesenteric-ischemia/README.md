# Mesenteric Ischemia Knowledge Domain

> **Version**: 1.0  
> **Status**: Core Complete  
> **Last Updated**: 2025-12-30  
> **Domain Path**: medicine/surgery/vascular/pathology/mesenteric-ischemia

## Overview

This domain contains comprehensive knowledge on mesenteric ischemia, covering both acute and chronic forms of the disease. The content is designed from the perspective of an experienced academic vascular surgeon and is suitable for vascular surgeons, general surgeons, surgical trainees, and other medical professionals involved in the care of patients with mesenteric vascular disease.

## Clinical Significance

Mesenteric ischemia remains one of the most lethal conditions in vascular surgery:
- **Acute Mesenteric Ischemia (AMI)**: 50-80% mortality
- **Nonocclusive Mesenteric Ischemia (NOMI)**: 70-90% mortality  
- **Mesenteric Venous Thrombosis (MVT)**: 20-50% mortality
- **Chronic Mesenteric Ischemia (CMI)**: 5-10% operative mortality with excellent long-term outcomes

## Content Structure

### Atomic Knowledge Units (AKUs)

Currently contains **29 comprehensive AKUs** organized by category:

#### Definitions (4 AKUs)
- `aku-001`: Mesenteric ischemia overview and classification
- `aku-002`: Acute mesenteric ischemia (AMI)
- `aku-003`: Chronic mesenteric ischemia (CMI)
- `aku-004`: Mesenteric arterial anatomy

#### Epidemiology (1 AKU)
- `aku-005`: AMI epidemiology and risk factors

#### Pathophysiology (4 AKUs)
- `aku-007`: Arterial occlusion mechanisms (embolism vs thrombosis)
- `aku-008`: Nonocclusive mesenteric ischemia (NOMI)
- `aku-009`: Mesenteric venous thrombosis
- `aku-010`: Intestinal infarction and necrosis

#### Diagnosis (3 AKUs)
- `aku-011`: AMI clinical presentation
- `aku-012`: CMI clinical presentation
- `aku-013`: Laboratory findings

#### Imaging (2 AKUs)
- `aku-015`: CT angiography for mesenteric ischemia
- `aku-016`: Duplex ultrasound

#### Treatment (6 AKUs)
- `aku-019`: Initial resuscitation and stabilization
- `aku-020`: Anticoagulation therapy
- `aku-021`: Open surgical revascularization
- `aku-022`: Endovascular treatment options
- `aku-023`: Bowel resection and second-look laparotomy
- `aku-024`: Hybrid surgical-endovascular approaches

#### Surgical Dilemmas (6 AKUs)
- `aku-025`: Open vs endovascular approach dilemma
- `aku-026`: Bowel viability assessment challenges
- `aku-027`: Damage control surgery decisions
- `aku-028`: Massive bowel resection decisions
- `aku-029`: Timing of revascularization
- `aku-030`: Managing elderly and comorbid patients

#### Outcomes (2 AKUs)
- `aku-031`: Mortality and survival outcomes
- `aku-032`: Short bowel syndrome

#### Follow-up (1 AKU)
- `aku-035`: Surveillance protocols

### Rendered Content

#### Book Chapter: "Mesenteric Ischemia: Dilemmas in Diagnosis, Treatment, and Decision-Making"

**Location**: `.renders/english/book-chapter-surgical-dilemmas.md`

A comprehensive ~25-30 page book chapter suitable for a surgical textbook or reference on dilemmas in surgery. The chapter covers:

1. **The Diagnostic Dilemma**: Challenges in recognizing mesenteric ischemia
2. **The Treatment Dilemma**: Open vs endovascular approach selection
3. **The Intraoperative Dilemma**: Bowel viability assessment
4. **The Resection Dilemma**: How much bowel to remove
5. **Special Populations**: NOMI, MVT, CMI
6. **Outcomes and Long-Term Considerations**
7. **The Human Element**: Communicating with families
8. **Case-Based Learning**: Learning from failure

**Target Audience**: 
- Vascular surgeons
- General surgeons
- Surgical residents and fellows
- Academic surgeons

**Format**: Markdown, suitable for conversion to PDF, LaTeX, or other formats

## Key Themes

### Surgical Dilemmas Addressed

1. **When to suspect mesenteric ischemia?** The "pain out of proportion to examination" paradigm and its limitations

2. **Endovascular or open surgery?** Balancing minimally invasive revascularization against the need to assess bowel viability

3. **Is the bowel viable?** Using clinical signs, adjunctive technologies, and second-look laparotomy

4. **How much to resect?** Balancing adequate margins against short bowel syndrome risk

5. **When is surgery futile?** Massive necrosis and goals-of-care decisions

### Clinical Pearls

- Anticoagulation should be started immediately upon clinical suspicion - do not wait for imaging
- CT angiography is the diagnostic cornerstone - obtain emergently
- The single most important prognostic factor is the presence of bowel necrosis
- When in doubt about bowel viability, plan a second-look laparotomy
- NOMI is the silent killer of the ICU - think of it in patients on vasopressors with rising lactate

## Related Domains

- `medicine/surgery/vascular/pathology/aaa`: Abdominal aortic aneurysm (may cause mesenteric ischemia)
- `medicine/surgery/vascular/procedures/evar`: EVAR (IMA sacrifice considerations)
- `medicine/surgery/vascular/complications/endoleaks`: Post-EVAR complications
- `medicine/gastroenterology/short-bowel-syndrome`: Consequence of massive resection

## Future Development

### Potential Additional AKUs (Reserved Numbering)
- `aku-006`: CMI epidemiology (separate from AMI)
- `aku-014`: Physical examination findings
- `aku-017`: Conventional/digital subtraction angiography
- `aku-018`: MR angiography
- `aku-033`: Reintervention and patency rates
- `aku-034`: Quality of life outcomes
- `aku-036`: Secondary prevention strategies
- `aku-037`: Nutritional management

### Planned Renders
- Medical student guide (simplified)
- Patient education materials
- Quick reference algorithm cards
- Training simulation scenarios

## Contributors

- copilot-agent (primary author)
- vascular-surgery-knowledge-base (domain expertise)

## Quality Assurance

All AKUs include:
- Formal medical coding (ICD-10, SNOMED-CT, CPT where applicable)
- Evidence-based provenance with source citations
- Pedagogical guidance including learning objectives and clinical pearls
- Relationship mapping to other concepts
- Rendering hints for visualization

### Atomicity Audit (2025-12-30)

All 29 AKUs have been audited for atomicity compliance:
- **Result**: 100% pass (29/29 atomic)
- **Violations Found**: None (no over-bundled or under-specified AKUs)
- **Transformations Required**: None
- **Full Report**: `.project/audits/mesenteric-ischemia-atomicity-audit.md`

### Critical Analysis (2025-12-30)

A comprehensive contrarian review has been conducted identifying areas for improvement:
- **Overall Assessment**: Competent but incomplete
- **Critical Gaps Identified**: 4 (differential diagnosis, atypical presentations, ischemia-reperfusion, NOMI expansion)
- **High Priority Recommendations**: 10
- **Full Report**: `.project/critical-analysis-contrarian-review.md`
- **Action Plan**: `.project/improvement-plan.md`

**Key Findings:**
1. Vascular surgeon perspective bias — needs interdisciplinary input
2. Evidence quality gaps — some citations need strengthening
3. Missing critical topics for clinical completeness
4. Book chapter needs structural enhancements (summary boxes, algorithms)

## Usage

This content is suitable for:
- Medical education
- Residency training curricula
- Board examination preparation
- Clinical decision support
- Textbook development
- Continuing medical education

---

*For questions or contributions, please refer to the project's main CONTRIBUTING.md guidelines.*
