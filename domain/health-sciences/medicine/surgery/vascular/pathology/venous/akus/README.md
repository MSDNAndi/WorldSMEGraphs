# Venous Disease AKUs

> **Domain**: health-sciences/medicine/surgery/vascular/pathology/venous  
> **Last Updated**: 2026-01-06  
> **AKUs in this akus/ directory**: 15 (see categories below; additional venous AKUs are defined in other subdomains)

## Directory Structure

```
akus/
├── physiology/           # Venous physiology fundamentals
│   ├── ven-001-hemodynamics.json
│   ├── ven-002-valve-function.json
│   ├── ven-003-muscle-pump.json
│   └── ven-004-venous-hypertension.json
├── chronic-venous-disease/  # Classification and skin changes
│   ├── cvd-001-ceap-classification.json
│   ├── cvd-002-vcss-scoring.json
│   ├── cvd-004-lipodermatosclerosis.json
│   ├── cvd-005-atrophie-blanche.json
│   ├── cvd-006-venous-claudication.json
│   └── svd-001-gsv-anatomy.json
└── procedures/           # Venous interventions
    ├── vproc-001-gsv-ablation.json
    ├── vproc-003-perforator-treatment.json
    ├── vproc-005-foam-sclerotherapy.json
    ├── dvd-004-iliac-stenting.json
    └── dvd-005-ivus-venous.json
```

## AKU Categories

### Venous Physiology (VEN-001 to VEN-004)
Foundational concepts for understanding venous disease:
- **VEN-001**: Venous hemodynamics - pressure dynamics, return mechanisms
- **VEN-002**: Valve function - structure, distribution, reflux criteria
- **VEN-003**: Muscle pump - calf pump physiology and measurement
- **VEN-004**: Venous hypertension - pathophysiology of skin changes

### Chronic Venous Disease (CVD-001 to CVD-006)
Classification systems and clinical manifestations:
- **CVD-001**: CEAP classification - C0-C6, etiology, anatomy, pathophysiology
- **CVD-002**: VCSS scoring - 10-component severity measurement
- **CVD-004**: Lipodermatosclerosis - acute vs chronic, treatment
- **CVD-005**: Atrophie blanche - microangiopathy, differential diagnosis
- **CVD-006**: Venous claudication - iliofemoral obstruction

### Superficial Venous Disease (SVD-001)
- **SVD-001**: GSV anatomy - course, tributaries, ultrasound identification

### Venous Procedures (VPROC-001 to VPROC-005)
Interventional treatments:
- **VPROC-001**: GSV ablation - RFA, laser, glue, MOCA comparison
- **VPROC-003**: Perforator treatment - PAPS, SEPS, criteria
- **VPROC-005**: Foam sclerotherapy - agents, technique, complications

### Deep Venous Disease (DVD-004 to DVD-005)
- **DVD-004**: Iliac vein stenting - May-Thurner, PTS, technique
- **DVD-005**: IVUS in venous disease - imaging, measurements

## Quality Standards

All AKUs in this directory follow the enhanced AKU v2 format:
- **Size**: 6-10 KB per AKU
- **Structure**: @context, metadata, classification, content, clinical_features, skos, relationships, provenance, pedagogical, medicalCode
- **Codes**: SNOMED-CT and ICD-10-CM codes included
- **Board Yield**: HIGH or MODERATE rating
- **Clinical Pearls**: 4-5 per AKU

## Validation

Run from the project root directory (`/home/runner/work/WorldSMEGraphs/WorldSMEGraphs` or wherever the repository is cloned):

```bash
# Validate all AKUs in this directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/health-sciences/medicine/surgery/vascular/pathology/venous/akus/

# Validate specific subdirectory
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/health-sciences/medicine/surgery/vascular/pathology/venous/akus/physiology/
```

## Cross-References

### Related Domains
- `vascular/foundations/hemodynamics/` - General hemodynamics
- `vascular/pathology/arterial/` - Arterial disease
- `vascular/diagnostics/` - Vascular imaging

### Prerequisites
All venous disease AKUs build on VEN-001 (hemodynamics) and VEN-002 (valve function).

## Related AKUs in Subdirectories

The venous domain includes additional AKUs in subdirectories:

**Superficial Venous Disease** (`superficial/akus/anatomy/`):
- SFJ-001: Saphenofemoral Junction Anatomy
- SPJ-001: Saphenopopliteal Junction Anatomy  
- SVD-001A: GSV Anatomy Overview
- SVD-002: SSV Anatomy
- PERF-001: Perforator Anatomy

**Deep Venous Disease** (`deep/akus/`):
- DVD-001: Deep Venous Reconstruction
- PTS-001: Post-Thrombotic Syndrome

**Venous Thrombosis** (`svt/akus/`, `ivc/akus/`):
- SVT-001: Superficial Thrombophlebitis
- IVC-001: IVC Filters

**Specific Conditions** (`varicose-veins/`, `compression-syndromes/`):
- VV-001: Varicose Veins
- MTS-001: May-Thurner Syndrome
- NCS-001: Nutcracker Syndrome
- PCS-001: Pelvic Congestion Syndrome

## Contributing

When adding new AKUs:
1. Follow the enhanced v2 format (see any AKU in `procedures/` for template)
2. Include SNOMED-CT and ICD-10 codes
3. Add clinical pearls and learning objectives
4. Update this README
5. Run validation before committing

## AKU ID Conventions

| Prefix | Category |
|--------|----------|
| VEN-   | Venous physiology |
| CVD-   | Chronic venous disease |
| SVD-   | Superficial venous disease |
| DVD-   | Deep venous disease |
| VPROC- | Venous procedures |
| SFJ-   | Saphenofemoral junction |
| SPJ-   | Saphenopopliteal junction |
| PERF-  | Perforator veins |
| PTS-   | Post-thrombotic syndrome |
| SVT-   | Superficial thrombophlebitis |
| IVC-   | Inferior vena cava |
| VV-    | Varicose veins |
| MTS-   | May-Thurner syndrome |
| NCS-   | Nutcracker syndrome |
| PCS-   | Pelvic congestion syndrome |
