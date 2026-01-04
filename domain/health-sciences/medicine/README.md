# Medicine

> **Domain Path**: `health-sciences/medicine/`  
> **Parent Domain**: Health Sciences  
> **Version**: 1.0.0  
> **Migrated**: 2026-01-04

## Overview

Medicine is the science and practice of diagnosis, treatment, and prevention of disease. It encompasses a variety of health care practices evolved to maintain and restore health through the prevention and treatment of illness.

## Content in This Directory

This directory contains **64 successfully migrated AKUs** covering vascular surgery topics, with **3 terminology files pending manual fix**.

### Current Content (64 AKUs)

#### Vascular Surgery - Complications
**Endoleaks** (8 AKUs)
- **Location**: `surgery/vascular/complications/endoleaks/type-2/`
- **Coverage**: Type 2 endoleak complications after endovascular aneurysm repair (EVAR)
- **Topics**: 
  - Definition and classification
  - Retrograde flow mechanism
  - Branch vessel sources
  - CTA imaging findings
  - Embolization technique
  - Treatment algorithm
  - Clinical significance

#### Vascular Surgery - Pathology
**Mesenteric Ischemia** (56 AKUs)
- **Location**: `surgery/vascular/pathology/mesenteric-ischemia/`
- **Coverage**: Comprehensive clinical knowledge on mesenteric ischemia
- **Subdomains**:
  - **Definitions** (5 AKUs): Overview, acute vs chronic, anatomy, colonic ischemia
  - **Diagnosis** (8 AKUs): Clinical presentation, lab findings, physical exam, differential dx
  - **Epidemiology** (2 AKUs): AMI and CMI epidemiology
  - **Imaging** (4 AKUs): CTA, duplex ultrasound, conventional angiography, MRA
  - **Pathophysiology** (4 AKUs): Arterial occlusion, NOMI, venous thrombosis, infarction
  - **Treatment** (9 AKUs): Endovascular, open surgical, medical management
  - **Outcomes** (5 AKUs): Mortality, short bowel syndrome, reintervention, QOL
  - **Follow-up** (3 AKUs): Surveillance, secondary prevention, nutrition
  - **Special Topics** (16 AKUs): Differential diagnosis, complications, biomarkers, etc.

### Migration Statistics
- **Total AKUs Found**: 67
- **Successfully Migrated**: 64 (95.5%)
- **Skipped**: 3 (terminology files missing classification.domain_path)
- **Failed**: 0

All migrated AKUs have:
- Updated `domain_path`: `medicine/surgery/vascular/*` → `health-sciences/medicine/surgery/vascular/*`
- Added `isNativeDomain: true` marker
- Updated `modified` timestamp: 2026-01-04

### Pending Content (3 AKUs)

**Issue**: 3 terminology files in vascular surgery directories lack the `classification.domain_path` field.

**Action Required**: Add classification section to terminology files:
```json
{
  "classification": {
    "domain_path": "health-sciences/medicine/surgery/vascular/appropriate/path",
    "type": "terminology",
    "difficulty": "graduate",
    "importance": "reference"
  }
}
```

## Medical Specialties Represented

### Surgery (Current)
**Vascular Surgery** - ✅ 64 AKUs present
- Focus: Blood vessel diseases and conditions
- Topics: Endoleaks, mesenteric ischemia, endovascular procedures

**Future Surgical Specialties**:
- General Surgery
- Cardiac Surgery
- Neurosurgery
- Orthopedic Surgery
- Plastic Surgery

### Internal Medicine (Future)
Planned subspecialties:
- Cardiology (heart diseases)
- Gastroenterology (digestive system)
- Pulmonology (respiratory system)
- Nephrology (kidney diseases)
- Endocrinology (hormones and metabolism)
- Oncology (cancer)

### Other Specialties (Future)
- Pediatrics (child health)
- Psychiatry (mental health)
- Emergency Medicine (acute care)
- Radiology (medical imaging)
- Pathology (disease diagnosis)

## Migration Details

### Source and Target
- **Source**: `medicine/` (legacy flat location)
- **Target**: `health-sciences/medicine/` (new hierarchical location)
- **Migration Date**: 2026-01-04
- **Tool Used**: `domain/_ontology/tools/migrate_domain.py`

### Directory Structure Preserved
The entire subdirectory structure was maintained:
```
health-sciences/medicine/
└── surgery/
    └── vascular/
        ├── complications/
        │   └── endoleaks/
        │       └── type-2/akus/
        │           ├── clinical/
        │           ├── definitions/
        │           ├── diagnosis/
        │           ├── management/
        │           └── pathophysiology/
        └── pathology/
            └── mesenteric-ischemia/akus/
                ├── definitions/
                ├── diagnosis/
                ├── epidemiology/
                ├── follow-up/
                ├── imaging/
                ├── outcomes/
                ├── pathophysiology/
                └── treatment/
```

## Medical Knowledge Characteristics

### Evidence-Based
All medical content should be:
- ✅ Based on peer-reviewed research
- ✅ Supported by clinical guidelines
- ✅ Referenced to authoritative sources
- ✅ Updated with current best practices

### Patient-Centered
Focus on:
- Safety and efficacy
- Clinical outcomes
- Quality of life
- Ethical considerations

### Quality Standards
- Follow clinical practice guidelines
- Reference standard textbooks and journals
- Use standard medical terminology (SNOMED CT, ICD-11, MeSH)
- Maintain HIPAA compliance for case examples

## Cross-Domain Applications

Medicine integrates knowledge from multiple domains:

### From Natural Sciences
- **Biology**: Anatomy, physiology, pathophysiology, genetics
- **Chemistry**: Biochemistry, pharmacology, drug interactions
- **Physics**: Medical imaging, radiation therapy, biomechanics

### From Formal Sciences
- **Mathematics/Statistics**: Epidemiology, clinical trial design, biostatistics
- **Computer Science**: Medical informatics, AI diagnostics, EHR systems

### From Social Sciences
- **Psychology**: Mental health, behavioral medicine, patient compliance
- **Economics**: Health economics, cost-effectiveness, healthcare policy

### To Engineering
- **Biomedical Engineering**: Medical devices, prosthetics, imaging equipment
- **Chemical Engineering**: Drug formulation and delivery systems

## Validation

Medicine AKUs are validated using domain-aware validation:

```bash
# Validate all medicine AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --domain medicine \
  --directory domain/health-sciences/medicine/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/health-sciences/medicine/
```

**Current Status**: 64/64 migrated AKUs validate successfully  
**Note**: Validator shows "Unknown domain 'health-sciences'" warning - this is expected and uses generic validation rules

## Contributing

When adding medical AKUs:

### Requirements
1. **Evidence-Based**: Cite peer-reviewed sources, clinical trials, guidelines
2. **Current Standards**: Reflect current best practices
3. **Patient Safety**: Review for accuracy, potential harm, contraindications
4. **Ethical Review**: Consider patient privacy, informed consent
5. **Standard Terminology**: Use SNOMED CT, ICD-11, MeSH when applicable
6. **Mark as Native**: Set `isNativeDomain: true`
7. **Follow AKU Format**: Use AKU v2.0 specification

### Classification Template
```json
{
  "classification": {
    "domain_path": "health-sciences/medicine/specialty/topic",
    "type": "definition|procedure|diagnosis|treatment",
    "difficulty": "medical-student|resident|attending",
    "importance": "foundational|common|rare",
    "maturity": "evidence-based|emerging|experimental"
  }
}
```

### Medical Evidence Levels
When citing sources, consider evidence hierarchy:
1. Systematic reviews and meta-analyses
2. Randomized controlled trials (RCTs)
3. Cohort studies
4. Case-control studies
5. Case series and case reports
6. Expert opinion

## Standard Medical Ontologies

Medicine uses standardized vocabularies integrated via JSON-LD:

- **SNOMED CT**: Clinical terminology (diseases, procedures, findings)
- **ICD-11**: International Classification of Diseases (WHO)
- **MeSH**: Medical Subject Headings (NLM indexing)
- **LOINC**: Laboratory test codes
- **RxNorm**: Normalized drug names

See: `domain/_contexts/medicine.jsonld` for vocabulary mappings

## References

### Clinical Guidelines
- UpToDate (evidence-based clinical resource)
- Cochrane Reviews (systematic reviews)
- National Guideline Clearinghouse
- Specialty society guidelines (AHA, ACC, ACCP, etc.)

### Standards Organizations
- World Health Organization (WHO) - ICD-11
- National Library of Medicine (NLM) - MeSH, UMLS
- SNOMED International - SNOMED CT
- American Medical Association (AMA) - CPT codes

### Related Documents
- Parent: `domain/health-sciences/README.md`
- Ontology: `domain/_ontology/global-hierarchy.yaml`
- Context: `domain/_contexts/medicine.jsonld`
- Migration: `domain/_ontology/MIGRATION-SUMMARY.md`

## Medical Disclaimer

⚠️ **IMPORTANT**: This is educational content for knowledge representation purposes. It is NOT medical advice. Always consult qualified healthcare professionals for diagnosis and treatment decisions.

---

**Status**: Active - 64 AKUs present, 3 pending fix  
**Coverage**: Vascular surgery (endoleaks, mesenteric ischemia)  
**Quality**: All migrated AKUs validated successfully  
**Evidence Level**: Based on peer-reviewed literature and clinical guidelines

**Questions?** See parent `health-sciences/README.md` or `domain/_ontology/README.md`
