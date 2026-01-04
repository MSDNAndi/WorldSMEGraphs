# Health Sciences

> **Domain Path**: `health-sciences/`  
> **UNESCO Code**: 09 (Health and Welfare)  
> **Library of Congress**: R (Medicine)  
> **Version**: 1.0.0  
> **Created**: 2026-01-04

## Overview

The Health Sciences are disciplines concerned with human health, disease prevention, diagnosis, treatment, and healthcare delivery. These sciences integrate knowledge from natural sciences (biology, chemistry, physics), social sciences (psychology, epidemiology), and applied practice (clinical medicine, nursing).

## What are Health Sciences?

Health sciences study:
- **Human health**: Normal physiology and anatomy
- **Disease**: Pathophysiology, diagnosis, treatment
- **Prevention**: Public health, epidemiology, health promotion
- **Healthcare systems**: Delivery, policy, quality
- **Medical technologies**: Diagnostics, therapeutics, devices

**Key Methodology**: Evidence-based medicine + clinical trials + epidemiology + basic research

## Subdomain Structure

### Medicine

**Path**: `health-sciences/medicine/`  
**Coverage**: All medical specialties

**Content (64 AKUs migrated 2026-01-04)**:
- **Surgery** - Surgical specialties
  - **Vascular Surgery** (64 AKUs)
    - **Complications/Endoleaks** (8 AKUs)
      - Type 2 endoleak definition, classification, imaging, treatment
    - **Pathology/Mesenteric Ischemia** (56 AKUs)
      - Overview, acute/chronic presentations, diagnosis, imaging
      - Treatment, outcomes, complications
      - Comprehensive clinical knowledge

**Planned Medical Specialties**:
- **Internal Medicine**
  - Cardiology, Gastroenterology, Pulmonology, Nephrology, Endocrinology, Oncology
- **Pediatrics** - Medical care of children
- **Psychiatry** - Mental health disorders
- **Emergency Medicine** - Acute illness and injury
- **Radiology** - Medical imaging
- **Pathology** - Disease diagnosis from tissues

### Nursing

**Path**: `health-sciences/nursing/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Patient Care
- Health Education
- Clinical Procedures
- Nursing Theory

### Pharmacy

**Path**: `health-sciences/pharmacy/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Pharmacology
- Pharmaceutical Chemistry
- Drug Interactions
- Clinical Pharmacy

### Public Health

**Path**: `health-sciences/public-health/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Epidemiology
- Health Policy
- Disease Prevention
- Health Promotion
- Biostatistics

### Allied Health

**Path**: `health-sciences/allied-health/`  
**Status**: ⏳ Pending creation

**Planned Coverage**:
- Physical Therapy
- Occupational Therapy
- Speech Therapy
- Medical Laboratory Science

## Cross-Domain Applications

Health sciences draw from and contribute to other domains:

### From Natural Sciences
- **Biology**: Anatomy, physiology, pathophysiology, genetics
- **Chemistry**: Biochemistry, pharmacology, drug development
- **Physics**: Medical imaging (MRI, CT, ultrasound), radiation therapy

### From Formal Sciences
- **Mathematics/Statistics**: Epidemiology, clinical trial design, biostatistics
- **Computer Science**: Medical informatics, AI diagnostics, electronic health records

### From Social Sciences
- **Psychology**: Mental health, health behavior, patient communication
- **Economics**: Health economics, cost-effectiveness analysis
- **Sociology**: Social determinants of health, health disparities

### To Engineering
- **Biomedical Engineering**: Medical devices, prosthetics, imaging equipment

## Native Domain Principle

Health sciences concepts belong here even when they use tools from other domains:

| Concept | Native Domain | Tools/Methods From |
|---------|---------------|-------------------|
| Endovascular Repair | Medicine/Surgery | Engineering (stent design), Physics (imaging) |
| Disease Epidemiology | Public Health | Statistics, Data Science |
| Drug Development | Pharmacy | Chemistry, Biology, Statistics |
| Mental Health Disorders | Psychiatry | Psychology, Neuroscience |

## Medical Knowledge Characteristics

Health sciences have unique requirements:
- **Evidence-Based**: Conclusions based on clinical trials and research
- **Patient-Centered**: Focus on safety, outcomes, quality of life
- **Ethical**: HIPAA, informed consent, do no harm
- **Regulated**: FDA approval, medical licensing, standards of care
- **Multidisciplinary**: Integration across specialties

## Migration Status

**Created**: 2026-01-04  
**Status**: Initial structure with medicine/surgery migrated

### Migrated Content
- ✅ **Medicine/Surgery/Vascular** (64/67 AKUs) migrated from `medicine/`
  - All vascular surgery content successfully migrated
  - 3 AKUs skipped (missing classification.domain_path - terminology files)
  - Domain paths updated to `health-sciences/medicine/*`
  - Timestamps updated to 2026-01-04

### Issues to Resolve
- ⚠️ **3 terminology files missing classification**: Need domain_path added
  - Located in vascular surgery directories

### Pending Migrations
- ⏳ Other medical specialties (if any exist in legacy structure)
- ⏳ Create nursing content
- ⏳ Create pharmacy content
- ⏳ Create public health content

## Content Statistics

**Current AKUs**: 64 (medicine/surgery/vascular)  
**Pending Fix**: 3 terminology files  
**Pending Creation**: Nursing, Pharmacy, Public Health, Allied Health  
**Target**: Comprehensive medical knowledge across all specialties

## Directory Structure

```
health-sciences/
├── medicine/                      ✅ 64 AKUs migrated
│   ├── surgery/
│   │   ├── general-surgery/       ⏳ Future
│   │   ├── cardiac-surgery/       ⏳ Future
│   │   ├── neurosurgery/          ⏳ Future
│   │   ├── orthopedic-surgery/    ⏳ Future
│   │   └── vascular/              ✅ 64 AKUs
│   │       ├── complications/
│   │       │   └── endoleaks/
│   │       │       └── type-2/    (8 AKUs)
│   │       └── pathology/
│   │           └── mesenteric-ischemia/  (56 AKUs)
│   │
│   ├── internal-medicine/         ⏳ Future
│   │   ├── cardiology/
│   │   ├── gastroenterology/
│   │   ├── pulmonology/
│   │   ├── nephrology/
│   │   ├── endocrinology/
│   │   └── oncology/
│   │
│   ├── pediatrics/                ⏳ Future
│   ├── psychiatry/                ⏳ Future
│   ├── emergency-medicine/        ⏳ Future
│   ├── radiology/                 ⏳ Future
│   └── pathology/                 ⏳ Future
│
├── nursing/                       ⏳ Pending
│   ├── patient-care/
│   └── clinical-procedures/
│
├── pharmacy/                      ⏳ Pending
│   ├── pharmacology/
│   └── clinical-pharmacy/
│
├── public-health/                 ⏳ Pending
│   ├── epidemiology/
│   ├── health-policy/
│   └── disease-prevention/
│
└── allied-health/                 ⏳ Pending
    ├── physical-therapy/
    └── occupational-therapy/
```

## Medical Terminology

Health sciences use standardized medical ontologies:
- **SNOMED CT**: Systematized Nomenclature of Medicine - Clinical Terms
- **ICD-11**: International Classification of Diseases (WHO)
- **MeSH**: Medical Subject Headings (NLM)
- **LOINC**: Logical Observation Identifiers Names and Codes
- **RxNorm**: Normalized drug names

These are integrated via `domain/_contexts/medicine.jsonld`

## References

### Classification Standards
- UNESCO ISCED-F 2013: Field 09 (Health and Welfare)
- Library of Congress Classification (R: Medicine)
- Dewey Decimal Classification (610: Medicine and Health)

### Medical Standards
- Evidence-Based Medicine Guidelines
- Cochrane Reviews
- UpToDate Clinical Guidelines
- WHO International Classification of Diseases (ICD-11)
- SNOMED CT Clinical Terminology

### Foundational Documents
- `domain/_ontology/global-hierarchy.yaml` - Authoritative taxonomy
- `domain/_ontology/README.md` - Design principles
- `domain/_contexts/medicine.jsonld` - Medical vocabulary and SNOMED integration

## Contributing

When adding content to health sciences:

1. **Evidence-Based**: Cite peer-reviewed sources, clinical trials, guidelines
2. **Patient Safety**: Review for accuracy, potential harm, contraindications
3. **Current Standards**: Reflect current best practices and guidelines
4. **Ethical Review**: Consider patient privacy, informed consent implications
5. **Mark Domain Status**: Set `isNativeDomain: true` for native medical concepts
6. **Use Standard Terminology**: Reference SNOMED CT, ICD-11, MeSH when applicable
7. **Follow AKU Format**: Use AKU v2.0 specification
8. **Validate**: Run validation tools before committing

## Validation

```bash
# Validate medicine AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --domain medicine \
  --directory domain/health-sciences/medicine/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/health-sciences/medicine/
```

## Related Domains

- **Natural Sciences** (`natural-sciences/`) - Biology, Chemistry, Physics provide foundations
- **Formal Sciences** (`formal-sciences/`) - Statistics, Computer Science provide tools
- **Social Sciences** (`social-sciences/`) - Psychology, Sociology inform patient care
- **Engineering** (`engineering/`) - Biomedical engineering creates medical devices

---

**Authoritative Source**: This directory hierarchy follows the global ontology defined in `domain/_ontology/global-hierarchy.yaml`

**Medical Disclaimer**: This is educational content. Always consult healthcare professionals for medical advice.

**Questions?** See `domain/_ontology/README.md` for design principles and migration guidance.
