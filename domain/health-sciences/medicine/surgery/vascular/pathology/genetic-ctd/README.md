# Genetic and Connective Tissue Disorders

This directory contains Atomic Knowledge Units (AKUs) for genetic and connective tissue disorders relevant to vascular surgery.

## Overview

Genetic connective tissue disorders are a group of inherited conditions affecting the structural proteins of blood vessels and other tissues. They are critical to vascular surgery because they cause aneurysms, dissections, and other vascular complications at young ages with unique management requirements.

## AKU Contents

### Marfan Syndrome (7 AKUs)
- **MARFAN-001**: Definition and Ghent criteria (`marfan-syndrome-001-definition.json`)
- **MARFAN-003**: Aortic root replacement (`marfan-003-root-replacement.json`)
- **MARFAN-004**: Valve-sparing root replacement (`marfan-004-valve-sparing.json`)
- **MARFAN-005**: Beta-blocker prophylaxis (`marfan-005-beta-blocker.json`)
- **MARFAN-006**: Pregnancy management (`marfan-006-pregnancy.json`)
- **MARFAN-007**: Surveillance protocols (`marfan-007-surveillance.json`)

### Loeys-Dietz Syndrome (5 AKUs)
- **LDS-001**: Definition and TGF-beta pathway (`loeys-dietz-syndrome-001-definition.json`)
- **LDS-002**: Subtypes LDS1-5 (`lds-002-subtypes.json`)
- **LDS-003**: Aggressive vascular phenotype (`lds-003-aggressive.json`)
- **LDS-004**: Surgical thresholds (`lds-004-surgical-thresholds.json`)
- **LDS-005**: Surveillance protocols (`lds-005-surveillance.json`)

### Vascular Ehlers-Danlos Syndrome (5 AKUs)
- **EDS-001**: Definition and diagnosis (`vascular-ehlers-danlos-001-definition.json`)
- **EDS-002**: COL3A1 mutations (`eds-002-col3a1.json`)
- **EDS-003**: Surgical avoidance strategies (`eds-003-surgical-avoidance.json`)
- **EDS-004**: Pregnancy risk (`eds-004-pregnancy.json`)
- **EDS-005**: Celiprolol evidence (`eds-005-celiprolol.json`)

### Fibromuscular Dysplasia (3 AKUs)
- **FMD-001**: Definition and types (`fibromuscular-dysplasia-001-definition.json`)
- **FMD-003**: Renal FMD (`fmd-003-renal.json`)
- **FMD-004**: Carotid FMD (`fmd-004-carotid.json`)

### Vasculitis (2 AKUs)
- **TAKAYASU-001**: Takayasu arteritis (`takayasu-arteritis-001-definition.json`)
- **BUERGER-001**: Buerger disease (`buerger-disease-001-definition.json`)

## Key Clinical Concepts

### Surgical Thresholds by Condition
| Condition | Aortic Root Threshold | Comparison |
|-----------|----------------------|------------|
| Marfan Syndrome | 5.0 cm (4.5 cm with risk factors) | Standard for CTDs |
| Loeys-Dietz Syndrome | 4.0-4.2 cm | **1 cm lower than Marfan** |
| Vascular EDS | Avoid surgery when possible | No safe threshold - rupture at any size |

### Pregnancy Risk Comparison
| Condition | Maternal Mortality | Key Feature |
|-----------|-------------------|-------------|
| Marfan Syndrome | 1-3% | Risk stratified by aortic diameter |
| Loeys-Dietz Syndrome | Higher than Marfan | More aggressive |
| Vascular EDS | 5-12% per pregnancy | **Highest risk, no safe threshold** |

## Medical Codes Coverage
All AKUs include:
- **ICD-10-CM** diagnosis codes
- **SNOMED-CT** concept codes
- **CPT** procedure codes (where applicable)

## Cross-Domain Links
- `formal-sciences/mathematics/category-theory` - Risk modeling
- `health-sciences/medicine/genetics` - Genetic testing and counseling
- `health-sciences/medicine/obstetrics` - Pregnancy management

## Validation Status
All 21 AKUs in this directory pass validation with the domain-aware validator.

```bash
# Validate all AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/health-sciences/medicine/surgery/vascular/pathology/genetic-ctd/akus/
```

## Last Updated
2026-01-06
