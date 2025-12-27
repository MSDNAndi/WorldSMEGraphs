# Medicine Domain

## Overview
This domain contains medical knowledge representations organized by medical specialty and subspecialty. The structure follows clinical practice organization while maintaining consistency with the WorldSMEGraphs knowledge representation format.

## Current Structure

```
medicine/
├── surgery/
│   └── vascular/
│       ├── procedures/
│       │   └── evar/              (Endovascular Aortic Repair - prerequisite)
│       ├── pathology/
│       │   └── aaa/               (Abdominal Aortic Aneurysm - prerequisite)
│       └── complications/
│           └── endoleaks/
│               └── type-2/        ✓ Complete (5 AKUs)
│                   ├── concept-index.yaml
│                   └── akus/
│                       ├── definitions/
│                       ├── pathophysiology/
│                       ├── diagnosis/
│                       ├── management/
│                       └── clinical/
```

## Implemented Topics

### Vascular Surgery - Type 2 Endoleak (Complete)
**Location**: `medicine/surgery/vascular/complications/endoleaks/type-2/`

**Atomic Knowledge Units**: 5 AKUs covering:
- **Definition** (2 AKUs):
  - aku-001: Type 2 Endoleak Definition
  - aku-002: Endoleak Classification System (Types 1-5)
- **Pathophysiology** (1 AKU):
  - aku-003: Retrograde Flow Mechanism
- **Diagnosis** (1 AKU):
  - aku-005: CT Angiography Imaging Findings
- **Management** (1 AKU):
  - aku-009: Treatment Algorithm
- **Clinical** (1 AKU):
  - aku-010: Clinical Significance and Outcomes

**Medical Specialty**: Vascular Surgery, Interventional Radiology

**Target Audiences**: 
- Vascular surgery residents
- Interventional radiology fellows
- Vascular surgeons
- Medical students (advanced)

**Clinical Context**: Post-EVAR (Endovascular Aortic Repair) complication management

## Prerequisites and Cross-Links

The Type 2 endoleak content references several prerequisite concepts that should be developed:

### High Priority Prerequisites
1. **Abdominal Aortic Aneurysm (AAA)** - `medicine/surgery/vascular/pathology/aaa/`
   - Essential for understanding why EVAR is performed
   - Natural history, rupture risk, screening

2. **Endovascular Aortic Repair (EVAR)** - `medicine/surgery/vascular/procedures/evar/`
   - The procedure that leads to endoleak complications
   - Technique, indications, immediate outcomes

3. **Vascular Anatomy - Abdominal Aorta** - `medicine/anatomy/vascular/abdominal-aorta/`
   - Branch vessels (lumbar arteries, IMA, etc.)
   - Collateral circulation
   - Normal anatomy and variants

### Medium Priority Prerequisites
4. **CT Angiography Technique** - `medicine/radiology/ct-angiography/`
   - Imaging protocols
   - Contrast timing
   - Image interpretation

5. **Hemodynamics Principles** - `medicine/physiology/hemodynamics/`
   - Blood flow dynamics
   - Pressure gradients
   - Collateral circulation

6. **Embolization Techniques** - `medicine/interventional-radiology/embolization/`
   - Transarterial approach
   - Embolic agents
   - Complications

## Knowledge Representation Format

All AKUs follow the WorldSMEGraphs V2 format:
- JSON-LD with schema.org context for semantic web compatibility
- Comprehensive metadata including confidence, contributors, timestamps
- Multi-representation content (text, formal notation, code where applicable)
- Extensive relationships (prerequisites, enables, related concepts)
- Provenance with source citations
- Pedagogical information (audiences, learning objectives, clinical pearls)
- Rendering hints for multiple audience levels

## Medical-Specific Features

Medical AKUs include additional fields relevant to clinical practice:
- **Medical specialty**: Primary and related specialties
- **Clinical context**: Where/when the knowledge applies
- **Epidemiology**: Incidence, prevalence data
- **Clinical features**: Presentation, natural history
- **Evidence level**: Strength of evidence supporting statements
- **Guidelines**: Relevant professional society recommendations
- **Patient communication**: Key messages for counseling

## Future Expansion

### Planned Topics (in order of prerequisite dependency)
1. **Abdominal Aortic Aneurysm** - Foundation for all EVAR-related topics
2. **EVAR Procedure** - Core procedure knowledge
3. **Type 1 Endoleak** - Higher urgency complication
4. **Type 3 Endoleak** - Structural failure complication
5. **Post-EVAR Surveillance** - Long-term management
6. **Aneurysm Rupture** - Emergency management
7. **Open Aortic Repair** - Alternative to EVAR

### Additional Vascular Surgery Topics
- Carotid artery stenosis and CEA/CAS
- Peripheral arterial disease
- Diabetic foot and amputation
- Venous disease (DVT, varicose veins)
- Vascular access for dialysis

### Other Medical Specialties
As the project expands, additional specialties will be added:
- Cardiology
- Neurology
- Orthopedic surgery
- Internal medicine subspecialties
- Emergency medicine

## Contributing

When adding medical knowledge:
1. Ensure clinical accuracy - cite authoritative sources
2. Follow professional society guidelines when available
3. Include evidence levels for clinical recommendations
4. Consider multiple audience levels (students, residents, attendings)
5. Link to prerequisite concepts appropriately
6. Include practical clinical pearls from experience
7. Address common misconceptions and errors

## Quality Assurance

Medical AKUs should be validated by:
1. Checking against current clinical practice guidelines
2. Verifying citations and source accuracy
3. Ensuring consistency with related AKUs
4. Reviewing for appropriate clinical detail level
5. Testing with intended audience for clarity

## References and Standards

Medical content should reference:
- Professional society guidelines (e.g., Society for Vascular Surgery)
- Peer-reviewed medical literature
- Standard medical textbooks (e.g., Rutherford's Vascular Surgery)
- Evidence-based medicine databases (Cochrane, UpToDate)

## Contact

For questions about medical domain content:
- Vascular Surgery topics: Coordinate with vascular surgery SME agents
- General medical questions: Use medical domain expert agents
- Format/structure questions: Refer to .project/knowledge-format-v2.md

---

**Last Updated**: 2025-12-27  
**Status**: Initial implementation with Type 2 endoleak complete  
**Next Priority**: EVAR and AAA prerequisite concepts
