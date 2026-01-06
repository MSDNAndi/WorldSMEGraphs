# Vascular Surgery Terminology Guide

> **Version**: 1.0.0  
> **Created**: 2026-01-05T18:58:00.000Z  
> **Last Updated**: 2026-01-05T18:58:00.000Z  
> **Domain Path**: `health-sciences/medicine/surgery/vascular`  
> **Maintainer**: terminology-agent

---

## Overview

This document establishes terminology standards for the vascular surgery knowledge domain in WorldSMEGraphs. It ensures consistent, accurate, and standardized use of medical terminology across all Atomic Knowledge Units (AKUs), enabling effective cross-referencing, searchability, and compliance with international medical nomenclature standards.

---

## Table of Contents

1. [Approved Abbreviations](#1-approved-abbreviations)
2. [Naming Conventions for AKU Files](#2-naming-conventions-for-aku-files)
3. [SNOMED-CT Usage Guidelines](#3-snomed-ct-usage-guidelines)
4. [Terminology Usage Standards](#4-terminology-usage-standards)
5. [Capitalization and Formatting Rules](#5-capitalization-and-formatting-rules)
6. [Directory Naming Standards](#6-directory-naming-standards)
7. [Known Terminology Inconsistencies](#7-known-terminology-inconsistencies)
8. [Preferred Terms vs. Synonyms](#8-preferred-terms-vs-synonyms)
9. [Medical Coding Standards](#9-medical-coding-standards)
10. [Validation Checklist](#10-validation-checklist)

---

## 1. Approved Abbreviations

### 1.1 Arterial Disease Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **AAA** | Abdominal Aortic Aneurysm | Use after first full mention | Spell out on first use |
| **TAA** | Thoracic Aortic Aneurysm | Use after first full mention | Spell out on first use |
| **TAAA** | Thoracoabdominal Aortic Aneurysm | Use after first full mention | Spell out on first use |
| **PAD** | Peripheral Arterial Disease | Use after first full mention | Spell out on first use |
| **CLI** | Critical Limb Ischemia | **DEPRECATED** - Use CLTI | See CLTI |
| **CLTI** | Chronic Limb-Threatening Ischemia | Preferred over CLI (per GVG 2019) | Spell out on first use |
| **ALI** | Acute Limb Ischemia | Use after first full mention | Spell out on first use |
| **PAU** | Penetrating Aortic Ulcer | Use after first full mention | Spell out on first use |
| **IMH** | Intramural Hematoma | Use after first full mention | Spell out on first use |
| **FMD** | Fibromuscular Dysplasia | Use after first full mention | Spell out on first use |
| **ABI** | Ankle-Brachial Index | Use after first full mention | Spell out on first use |
| **TBI** | Toe-Brachial Index | Use after first full mention | Spell out on first use |

### 1.2 Venous Disease Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **DVT** | Deep Vein Thrombosis | Use after first full mention | Spell out on first use |
| **VTE** | Venous Thromboembolism | Use after first full mention | Spell out on first use |
| **PE** | Pulmonary Embolism | Use after first full mention | Spell out on first use |
| **CVI** | Chronic Venous Insufficiency | Use after first full mention | Spell out on first use |
| **PTS** | Post-Thrombotic Syndrome | Use after first full mention | Spell out on first use |
| **SVT** | Superficial Vein Thrombosis | Use after first full mention | Spell out on first use |
| **IVC** | Inferior Vena Cava | Use after first full mention | Spell out on first use |

### 1.3 Procedural Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **EVAR** | Endovascular Aortic Repair | Use after first full mention | Spell out on first use |
| **TEVAR** | Thoracic Endovascular Aortic Repair | Use after first full mention | Spell out on first use |
| **FEVAR** | Fenestrated Endovascular Aortic Repair | Use after first full mention | Spell out on first use |
| **CEA** | Carotid Endarterectomy | Use after first full mention | Spell out on first use |
| **CAS** | Carotid Artery Stenting | Use after first full mention | Spell out on first use |
| **TCAR** | TransCarotid Artery Revascularization | Use after first full mention | Spell out on first use |
| **PTA** | Percutaneous Transluminal Angioplasty | Use after first full mention | Spell out on first use |
| **DCB** | Drug-Coated Balloon | Use after first full mention | Spell out on first use |
| **DES** | Drug-Eluting Stent | Use after first full mention | Spell out on first use |
| **CDT** | Catheter-Directed Thrombolysis | Use after first full mention | Spell out on first use |
| **AVF** | Arteriovenous Fistula | Use after first full mention | Spell out on first use |
| **AVG** | Arteriovenous Graft | Use after first full mention | Spell out on first use |
| **LVA** | Lymphovenous Anastomosis | Use after first full mention | Spell out on first use |
| **VLNT** | Vascularized Lymph Node Transfer | Use after first full mention | Spell out on first use |
| **REBOA** | Resuscitative Endovascular Balloon Occlusion of the Aorta | Use after first full mention | Spell out on first use |

### 1.4 Diagnostic Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **CTA** | Computed Tomography Angiography | Use after first full mention | Spell out on first use |
| **MRA** | Magnetic Resonance Angiography | Use after first full mention | Spell out on first use |
| **IVUS** | Intravascular Ultrasound | Use after first full mention | Spell out on first use |
| **TcPO₂** | Transcutaneous Oxygen Pressure | Use after first full mention | Spell out on first use |
| **SPP** | Skin Perfusion Pressure | Use after first full mention | Spell out on first use |
| **PVR** | Pulse Volume Recording | Use after first full mention | Spell out on first use |
| **EMG** | Electromyography | Use after first full mention | Spell out on first use |
| **NCS** | Nerve Conduction Study | Use after first full mention | Spell out on first use |

### 1.5 Syndrome Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **TOS** | Thoracic Outlet Syndrome | Use after first full mention | Spell out on first use |
| **NTOS** | Neurogenic Thoracic Outlet Syndrome | Use after first full mention | Spell out on first use |
| **ATOS** | Arterial Thoracic Outlet Syndrome | Use after first full mention | Spell out on first use |
| **VTOS** | Venous Thoracic Outlet Syndrome | Use after first full mention | Spell out on first use |
| **MTS** | May-Thurner Syndrome | Use after first full mention | Spell out on first use |
| **NCS** | Nutcracker Syndrome | Context-dependent (avoid confusion with Nerve Conduction Study) | Always spell out |
| **HIT** | Heparin-Induced Thrombocytopenia | Use after first full mention | Spell out on first use |
| **PAES** | Popliteal Artery Entrapment Syndrome | Use after first full mention | Spell out on first use |
| **MALS** | Median Arcuate Ligament Syndrome | Use after first full mention | Spell out on first use |
| **NOMI** | Non-Occlusive Mesenteric Ischemia | Use after first full mention | Spell out on first use |
| **HHS** | Hypothenar Hammer Syndrome | Use after first full mention | Spell out on first use |

### 1.6 Genetic/Connective Tissue Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **EDS** | Ehlers-Danlos Syndrome | Use after first full mention | Spell out on first use |
| **vEDS** | Vascular Ehlers-Danlos Syndrome | Preferred over "Type IV EDS" | Spell out on first use |
| **LDS** | Loeys-Dietz Syndrome | Use after first full mention | Spell out on first use |
| **HHT** | Hereditary Hemorrhagic Telangiectasia | Use after first full mention | Spell out on first use |
| **NF1** | Neurofibromatosis Type 1 | Use after first full mention | Spell out on first use |
| **BAV** | Bicuspid Aortic Valve | Use after first full mention | Spell out on first use |

### 1.7 Vasculitis Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **GCA** | Giant Cell Arteritis | Use after first full mention | Spell out on first use |
| **TAO** | Thromboangiitis Obliterans (Buerger Disease) | Preferred: Use "Buerger disease" | Spell out on first use |
| **PAN** | Polyarteritis Nodosa | Use after first full mention | Spell out on first use |
| **ANCA** | Anti-Neutrophil Cytoplasmic Antibody | Use after first full mention | Spell out on first use |

### 1.8 Anatomy Abbreviations

| Abbreviation | Full Term | Preferred Usage | First-Use Rule |
|-------------|-----------|-----------------|----------------|
| **SFA** | Superficial Femoral Artery | Use after first full mention | Spell out on first use |
| **CFA** | Common Femoral Artery | Use after first full mention | Spell out on first use |
| **PFA** | Profunda Femoris Artery | Use after first full mention | Spell out on first use |
| **IMA** | Inferior Mesenteric Artery | Use after first full mention | Spell out on first use |
| **SMA** | Superior Mesenteric Artery | Use after first full mention | Spell out on first use |
| **GSV** | Great Saphenous Vein | Use after first full mention | Spell out on first use |
| **SSV** | Small Saphenous Vein | Use after first full mention | Spell out on first use |
| **SFJ** | Saphenofemoral Junction | Use after first full mention | Spell out on first use |
| **SPJ** | Saphenopopliteal Junction | Use after first full mention | Spell out on first use |

---

## 2. Naming Conventions for AKU Files

### 2.1 Directory Naming

**Pattern**: `[topic-name-in-lowercase-with-hyphens]/`

**Rules**:
- Use lowercase letters only
- Separate words with hyphens (kebab-case)
- Use full descriptive names, not abbreviations for directories
- Exception: Well-established abbreviations may be used when the abbreviation is the primary identifier (e.g., `aaa/` is acceptable for "abdominal aortic aneurysm")

**Examples**:
```
✅ CORRECT:
  pathology/deep-vein-thrombosis/
  pathology/peripheral-arterial-disease/
  pathology/aortic-dissection/
  procedures/carotid-endarterectomy/
  pathology/aaa/  (acceptable - AAA is primary identifier)

❌ INCORRECT:
  pathology/DVT/  (use deep-vein-thrombosis)
  pathology/PAD/  (use peripheral-arterial-disease)
  pathology/DeepVeinThrombosis/  (no PascalCase)
  pathology/deep_vein_thrombosis/  (no underscores)
```

### 2.2 AKU File Naming

**Pattern**: `[prefix]-[number]-[descriptor].json`

**Rules**:
- Use lowercase with hyphens
- Include a meaningful prefix (3-5 characters) identifying the topic
- Use 3-digit numbering (001, 002, etc.)
- Include descriptive suffix indicating content type

**Standard Prefixes**:
| Prefix | Domain | Example |
|--------|--------|---------|
| aaa- | Abdominal Aortic Aneurysm | aaa-001-definition.json |
| pad- | Peripheral Arterial Disease | pad-003-ankle-brachial-index.json |
| dvt- | Deep Vein Thrombosis | dvt-001-definition.json |
| carotid- | Carotid Disease | carotid-002-duplex-ultrasound.json |
| diss- | Aortic Dissection | diss-001-definition.json |
| evar- | EVAR Procedures | evar-001-overview.json |
| cea- | Carotid Endarterectomy | cea-001-overview.json |
| tos- | Thoracic Outlet Syndrome | tos-001-definition.json |
| aku- | Generic AKU | aku-001-topic-name.json |

**Standard Suffixes**:
| Suffix | Content Type |
|--------|--------------|
| -definition | Concept definition |
| -classification | Classification systems |
| -diagnosis | Diagnostic approaches |
| -treatment | Treatment methods |
| -technique | Procedural techniques |
| -overview | General overview |
| -epidemiology | Epidemiological data |
| -pathophysiology | Pathophysiology |
| -management | Management algorithms |
| -complications | Complication types |
| -anatomy | Anatomical concepts |

### 2.3 Subdirectory Organization

**Standard Structure**:
```
[topic]/
├── akus/
│   ├── definitions/
│   ├── diagnosis/
│   ├── treatment/
│   ├── complications/
│   ├── techniques/
│   └── [other-categories]/
├── terminology/
└── .renders/
```

---

## 3. SNOMED-CT Usage Guidelines

### 3.1 Coding System Naming

**Standard**: Use `SNOMED-CT` (hyphenated, all caps except 'CT')

```json
✅ CORRECT:
"codingSystem": "SNOMED-CT"

❌ INCORRECT:
"codingSystem": "SNOMED CT"
"codingSystem": "snomed-ct"
"codingSystem": "Snomed-CT"
"codingSystem": "SNOMED_CT"
```

### 3.2 Code Formatting

**Standard Structure**:
```json
{
  "@type": "MedicalCode",
  "codingSystem": "SNOMED-CT",
  "codeValue": "233985008",
  "uri": "http://snomed.info/id/233985008",
  "description": "Abdominal aortic aneurysm (disorder)"
}
```

**Field Requirements**:
- `codeValue`: Numeric code as string
- `uri`: Full SNOMED URI format: `http://snomed.info/id/[code]`
- `description`: Include Fully Specified Name (FSN) with semantic tag

### 3.3 SNOMED-CT Field Variations

**Acceptable Formats** (legacy support):
```json
// Modern format (preferred)
"snomed_ct": {
  "code": "233985008",
  "uri": "http://snomed.info/id/233985008"
}

// Legacy format (acceptable)
"snomed_codes": ["233985008"]
"snomed_ct": "233985008"
```

### 3.4 Common Vascular SNOMED-CT Codes

| Condition | SNOMED-CT Code | FSN |
|-----------|---------------|-----|
| Abdominal aortic aneurysm | 233985008 | Abdominal aortic aneurysm (disorder) |
| Deep vein thrombosis | 128053003 | Deep vein thrombosis (disorder) |
| Peripheral arterial disease | 399957001 | Peripheral arterial occlusive disease (disorder) |
| Carotid stenosis | 64586002 | Carotid artery stenosis (disorder) |
| Endoleak | 445080003 | Endoleak (disorder) |
| Type 2 endoleak | 449567000 | Type II endoleak (disorder) |
| Aortic dissection | 308546005 | Dissection of aorta (disorder) |
| Thoracic outlet syndrome | 49484002 | Thoracic outlet syndrome (disorder) |

---

## 4. Terminology Usage Standards

### 4.1 Claudication Terminology

**Preferred Terms**:
- Use **"intermittent claudication"** for the full formal term
- Use **"claudication"** as acceptable shorthand after first full mention
- Use **"neurogenic claudication"** specifically for spinal stenosis-related symptoms

**Context-Specific Usage**:
| Context | Preferred Term |
|---------|---------------|
| Definition | Intermittent claudication |
| Casual reference | Claudication |
| Differential diagnosis | Specify: "intermittent claudication" vs "neurogenic claudication" |
| Symptoms list | Claudication (if context is clear) |

### 4.2 Critical Limb Ischemia Terminology

**Current Standard** (per Global Vascular Guidelines 2019):
- **Preferred**: Chronic Limb-Threatening Ischemia (CLTI)
- **Deprecated**: Critical Limb Ischemia (CLI)

**Transition Guidance**:
```
✅ CORRECT: "Chronic limb-threatening ischemia (CLTI) is defined as..."
⚠️ ACCEPTABLE: "Critical limb ischemia (CLI, now termed CLTI)..."
❌ AVOID: Using CLI without noting the CLTI terminology update
```

### 4.3 Endoleak Terminology

**Preferred**: "endoleak" (one word, lowercase unless starting a sentence)

**Type Classification**:
- Use Arabic numerals: "Type 1," "Type 2," etc.
- Accept Roman numerals in citations: "Type II" (when quoting sources)
- Preferred format: "Type 2 endoleak" (not "Type II endoleak")

**Directory Naming**:
- Singular preferred: `endoleak/` (not `endoleaks/`)
- Note: Currently both exist - see [Section 7: Known Inconsistencies](#7-known-terminology-inconsistencies)

### 4.4 Thoracic Outlet Syndrome Types

**Preferred Terminology**:
| Type | Full Term | Abbreviation | Alternative |
|------|-----------|--------------|-------------|
| Neurogenic | Neurogenic Thoracic Outlet Syndrome | NTOS | - |
| Venous | Venous Thoracic Outlet Syndrome | VTOS | Paget-Schroetter Syndrome |
| Arterial | Arterial Thoracic Outlet Syndrome | ATOS | - |

**Cross-Reference**: When referring to Paget-Schroetter syndrome, also reference VTOS.

---

## 5. Capitalization and Formatting Rules

### 5.1 Disease and Syndrome Names

**General Rule**: Capitalize proper nouns; lowercase general terms.

| Pattern | Example |
|---------|---------|
| Named after person | Marfan syndrome, Buerger disease |
| Anatomic location + disease | peripheral arterial disease |
| Abbreviation title case | Peripheral Arterial Disease (PAD) |
| Generic disease | aneurysm, dissection, thrombosis |

**Exception**: Title case acceptable in headings and prefLabels.

### 5.2 Procedure Names

**Pattern**: Capitalize proper nouns only.

```
✅ CORRECT:
  carotid endarterectomy
  endovascular aortic repair
  Fogarty catheter embolectomy (Fogarty = proper noun)

❌ INCORRECT:
  Carotid Endarterectomy (unless in heading)
  Endovascular Aortic Repair (unless in heading)
```

### 5.3 Anatomical Terms

**Pattern**: Use lowercase for anatomical terms unless starting a sentence.

```
✅ CORRECT:
  superficial femoral artery
  inferior mesenteric artery
  great saphenous vein

❌ INCORRECT:
  Superficial Femoral Artery
  Inferior Mesenteric Artery
```

### 5.4 Abbreviation Formatting

**Rules**:
1. All abbreviations in CAPS (AAA, DVT, EVAR)
2. Subscripts where appropriate (TcPO₂)
3. No periods between letters (use "AAA" not "A.A.A.")

---

## 6. Directory Naming Standards

### 6.1 Preferred Directory Names

| Condition | Preferred Directory | Avoid |
|-----------|-------------------|-------|
| Deep Vein Thrombosis | `deep-vein-thrombosis/` | `dvt/` |
| Peripheral Arterial Disease | `peripheral-arterial-disease/` | `pad/` |
| Abdominal Aortic Aneurysm | `aaa/` (acceptable exception) | `abdominal-aortic-aneurysm/` |
| Thoracic Outlet Syndrome | `thoracic-outlet-syndrome/` | `tos/` |
| Carotid Disease | `carotid-disease/` | `carotid/` |
| Endoleak | `endoleak/` (singular) | `endoleaks/` |

### 6.2 Subdomain Hierarchy

**Standard Hierarchy**:
```
pathology/
├── [condition-name]/
│   └── akus/
│       ├── definitions/
│       ├── diagnosis/
│       ├── treatment/
│       └── [other-categories]/
```

**Avoid**:
- Duplicate directories for same condition (e.g., both `dvt/` and `deep-vein-thrombosis/`)
- Mixing abbreviation and full-name directories

---

## 7. Known Terminology Inconsistencies

### 7.1 Directory Duplications Requiring Resolution

| Inconsistency | Current State | Recommended Action |
|--------------|---------------|-------------------|
| DVT directories | Both `dvt/` and `deep-vein-thrombosis/` exist | Consolidate to `deep-vein-thrombosis/` |
| PAD directories | Both `pad/` and `peripheral-arterial-disease/` exist | Consolidate to `peripheral-arterial-disease/` |
| TOS directories | `tos/`, `arterial-tos/`, `neurogenic-tos/`, `venous-thoracic-outlet/` | Consolidate under `thoracic-outlet-syndrome/` with subdirs |
| Endoleak | Both `endoleak/` and `endoleaks/` exist | Consolidate to `endoleak/` (singular) |

### 7.2 Terminology Variations Found

| Variation | Locations | Recommended Standard |
|-----------|-----------|---------------------|
| "CLI" vs "CLTI" | Multiple PAD AKUs | Use CLTI (per GVG 2019) |
| "Type II endoleak" vs "Type 2 endoleak" | Endoleak AKUs | Use "Type 2 endoleak" |
| "SNOMED-CT" vs "snomed_ct" | Various JSON fields | Use "SNOMED-CT" in codingSystem |
| "claudication" vs "intermittent claudication" | PAD AKUs | Define as "intermittent claudication," use "claudication" subsequently |

### 7.3 Inconsistent File Naming Patterns

| Pattern Found | Example | Recommended |
|--------------|---------|-------------|
| Mixed prefixes | `aku-001-` vs `dvt-001-` | Use topic-specific prefix (e.g., `dvt-001-`) |
| Inconsistent suffixes | `*-definition` vs `*-overview` | Use standard suffixes from Section 2.2 |
| Capitalization | Some files have uppercase | All lowercase |

---

## 8. Preferred Terms vs. Synonyms

### 8.1 Disease Terms

| Preferred Term | Acceptable Synonyms | Deprecated Terms |
|---------------|---------------------|-----------------|
| Peripheral arterial disease | PAD, lower extremity arterial disease | Peripheral vascular disease (PVD) - too broad |
| Chronic limb-threatening ischemia | CLTI | Critical limb ischemia (CLI) |
| Deep vein thrombosis | DVT, deep venous thrombosis | - |
| Venous thromboembolism | VTE | - |
| Abdominal aortic aneurysm | AAA, infrarenal aortic aneurysm | - |
| Buerger disease | Thromboangiitis obliterans | TAO (acceptable in abbreviation) |
| Paget-Schroetter syndrome | Venous TOS, effort thrombosis | - |
| Marfan syndrome | MFS | Marfan's syndrome (avoid possessive) |

### 8.2 Procedure Terms

| Preferred Term | Acceptable Synonyms |
|---------------|---------------------|
| Endovascular aortic repair | EVAR, endovascular aneurysm repair |
| Carotid endarterectomy | CEA |
| Catheter-directed thrombolysis | CDT, lytic therapy |
| Percutaneous transluminal angioplasty | PTA, balloon angioplasty |

---

## 9. Medical Coding Standards

### 9.1 Required Coding Systems

Each AKU should include codes from the following systems where applicable:

1. **SNOMED-CT** (Required)
   - Primary terminology standard
   - Include URI: `http://snomed.info/id/[code]`

2. **ICD-10-CM** (Required for diagnoses)
   - Billing and epidemiology
   - Format: Letter + numbers (e.g., I71.4)

3. **MeSH** (Recommended)
   - PubMed indexing
   - Include URI: `http://id.nlm.nih.gov/mesh/[descriptor]`

### 9.2 Medical Code Block Format

```json
"medicalCode": [
  {
    "@type": "MedicalCode",
    "codingSystem": "SNOMED-CT",
    "codeValue": "233985008",
    "uri": "http://snomed.info/id/233985008",
    "description": "Abdominal aortic aneurysm (disorder)"
  },
  {
    "@type": "MedicalCode",
    "codingSystem": "ICD-10-CM",
    "codeValue": "I71.4",
    "description": "Abdominal aortic aneurysm, without rupture"
  },
  {
    "@type": "MedicalCode",
    "codingSystem": "MeSH",
    "codeValue": "D017544",
    "uri": "http://id.nlm.nih.gov/mesh/D017544",
    "description": "Aortic Aneurysm, Abdominal"
  }
]
```

---

## 10. Validation Checklist

### 10.1 Before Creating New AKUs

- [ ] Check if abbreviations are in approved list (Section 1)
- [ ] Follow file naming conventions (Section 2)
- [ ] Include required SNOMED-CT codes (Section 3)
- [ ] Use preferred terminology (Section 8)
- [ ] Apply correct capitalization (Section 5)
- [ ] Place in correct directory structure (Section 6)

### 10.2 Terminology Review Checklist

- [ ] Abbreviations expanded on first use
- [ ] Consistent use of CLTI vs CLI (prefer CLTI)
- [ ] Consistent use of "Type 2 endoleak" format
- [ ] SNOMED-CT URIs included
- [ ] No deprecated terms in active use
- [ ] No possessive forms of eponyms (Marfan syndrome, not Marfan's)

### 10.3 Cross-Reference Validation

- [ ] SKOS relationships use consistent term identifiers
- [ ] Related concepts link correctly
- [ ] Broader/narrower relationships are accurate
- [ ] Cross-domain references are valid

---

## Appendix A: Reference Resources

### Medical Terminology Standards

1. **SNOMED International**: https://www.snomed.org/
2. **ICD-10-CM**: https://www.cms.gov/medicare/coding/icd10
3. **MeSH**: https://www.nlm.nih.gov/mesh/

### Vascular Surgery Guidelines

1. **SVS Practice Guidelines**: https://vascular.org/clinicians/clinical-practice-guidelines
2. **ESVS Guidelines**: https://www.esvs.org/guidelines
3. **Global Vascular Guidelines (GVG)**: J Vasc Surg. 2019;69(6S):3S-125S

### Internal Resources

1. **Terminology Database**: `terminology/vascular-surgery-terms.json`
2. **Domain Ontology**: `ONTOLOGY.md`
3. **AKU Backlog**: `AKU-BACKLOG.md`

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-05 | Initial terminology guide creation |

---

*This guide is a living document. Updates should be submitted via pull request with justification for terminology changes.*
