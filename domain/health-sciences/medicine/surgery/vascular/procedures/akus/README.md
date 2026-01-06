# Vascular Surgery Procedures - Atomic Knowledge Units (AKUs)

This directory contains rigorous Atomic Knowledge Units for fundamental vascular surgical procedures. Each AKU follows the WorldSMEGraphs format with complete medical coding, clinical context, and pedagogical structure.

## Contents

### Open Surgical Exposures
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-001-femoral-exposure.json` | Femoral Artery Exposure | CFA/SFA/PFA dissection, lymphatic preservation |
| `proc-002-popliteal-exposure.json` | Popliteal Artery Exposure | Above-knee/below-knee approaches, medial dissection |
| `proc-003-tibial-exposure.json` | Tibial Artery Exposure | AT/PT/peroneal approaches, limb salvage anatomy |
| `proc-004-carotid-exposure.json` | Carotid Artery Exposure | Cervical approach, cranial nerve protection |
| `proc-005-subclavian-exposure.json` | Subclavian Artery Exposure | Supraclavicular approach, phrenic nerve, scalene triangle |

### Aortic Exposures
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-008-retroperitoneal-aortic.json` | Retroperitoneal Aortic Exposure | Left flank approach, reduced ileus |
| `proc-009-transperitoneal-aortic.json` | Transperitoneal Aortic Exposure | Midline laparotomy, left renal vein landmark |
| `proc-010-medial-visceral-rotation.json` | Medial Visceral Rotation | Mattox maneuver, Cattell-Braasch, trauma exposure |

### Anastomotic Techniques
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-011-end-to-end.json` | End-to-End Anastomosis | Spatulation, intima-to-intima, suture technique |
| `proc-012-end-to-side.json` | End-to-Side Anastomosis | Arteriotomy geometry, heel-toe suturing, bypass |

### Extra-Anatomic Bypass
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-018-axillobifemoral.json` | Axillobifemoral Bypass | Extra-anatomic reconstruction, hostile abdomen |
| `proc-019-femorofemoral.json` | Femorofemoral Bypass | Crossover graft, donor iliac assessment |

### Quality Control
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-021-completion-angio.json` | Completion Angiography | Intraoperative imaging, technical error detection |
| `proc-022-completion-duplex.json` | Completion Duplex | Velocity criteria, PSV thresholds, non-invasive |

### Wound Management
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-025-sartorius-flap.json` | Sartorius Muscle Flap | Groin wound coverage, vascular graft protection |

### Endovascular Access
| File | Procedure | Key Topics |
|------|-----------|------------|
| `proc-029-us-guided-access.json` | Ultrasound-Guided Access | Real-time imaging, 50-70% complication reduction |
| `proc-030-micropuncture.json` | Micropuncture Technique | 21G access, reduced bleeding, small vessels |
| `proc-031-radial-access.json` | Radial Access | Transradial approach, 80% bleeding reduction |
| `proc-033-closure-devices.json` | Closure Device Selection | VCDs, Perclose, AngioSeal, preclose technique |
| `proc-035-large-bore-access.json` | Large Bore Access | TAVR/EVAR access, iliofemoral assessment |

## AKU Structure

Each AKU contains:
- **@context**: JSON-LD context references
- **metadata**: Version, creation date, contributors, confidence
- **classification**: Domain path, type, difficulty, importance, medical specialty
- **content**: Statement, explanation (intuition, key insight, technical details), glossary
- **clinical_features**: Indications, contraindications, technique, complications
- **skos**: Preferred/alternate labels, definition, notation
- **relationships**: Prerequisites, enables, broader/narrower/related concepts
- **provenance**: Sources with citations and confidence
- **pedagogical**: Target audience, learning objectives, clinical pearls, board yield
- **medicalCode**: SNOMED-CT, CPT, ICD-10-PCS codes

## Validation

All AKUs pass validation with:
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py [aku-file.json]
```

## Statistics

- **Total AKUs**: 20
- **Total Size**: ~220KB
- **Average AKU Size**: ~11KB
- **Size Range**: 10-13KB per AKU
- **All SNOMED-CT/CPT/ICD-10 Coded**: Yes

## Related Resources

- Parent domain: `domain/health-sciences/medicine/surgery/vascular/`
- Pathology AKUs: `../pathology/akus/`
- Foundations AKUs: `../foundations/akus/`
- Complications AKUs: `../complications/akus/`
- Devices AKUs: `../devices/akus/`

## Contributing

When adding new procedure AKUs:
1. Follow the established JSON schema
2. Include complete medical coding (SNOMED-CT, CPT, ICD-10)
3. Validate with the v2 validator before committing
4. Ensure all clinical_features sections are complete
5. Include at least 4-5 clinical pearls

---
Last Updated: 2026-01-06
