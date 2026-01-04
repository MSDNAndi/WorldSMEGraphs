# Domain Navigation Guide

> **Purpose**: Help users quickly find and navigate content across the WorldSMEGraphs domain hierarchy.

## Quick Domain Access

### Formal Sciences
**Location**: `domain/formal-sciences/`

#### Mathematics
- **Pure Mathematics**: `formal-sciences/mathematics/pure-mathematics/`
  - **Category Theory** (8 AKUs): Native math domain
    - Historical origins, category definitions, morphisms
    - Composition, identity morphisms, category laws
    - Examples, universal properties
    - **Cross-domain applications**: Functional programming, type theory

#### Computer Science
- **Programming Paradigms**: `formal-sciences/computer-science/programming-paradigms/`
  - **Functional Programming**: Application domain with cross-refs to math
    - See: `science/computer-science/functional-theory/` (legacy location)

---

### Natural Sciences
**Location**: `domain/natural-sciences/`

#### Physics (136 AKUs)
**Path**: `natural-sciences/physics/`

**Subdisciplines**:
- **Quantum Mechanics**: `quantum-mechanics/planck-units/`
  - 102 AKUs covering Planck scale, quantum gravity
  - Holographic principle, string theory connections
  - Black hole thermodynamics, loop quantum gravity
  
- **Measurement Limits**: `measurement-limits/`
  - Fundamental constraints on measurement precision
  
- **Cosmology**: `cosmology/`
  - Universe structure and evolution
  
- **Particle Physics**: `particle-physics/`
  - Fundamental particles and interactions
  
- **Atomic Physics**: `atomic-physics/`
  - Atomic structure and properties
  
- **General Relativity**: `general-relativity/`
  - Spacetime, gravity, relativistic effects

**Key Content**:
- Planck units formulas (comprehensive mathematical framework)
- Natural units and fundamental constants
- Quantum gravity regime analysis
- Theoretical physics at smallest scales

---

### Social Sciences
**Location**: `domain/social-sciences/`

#### Economics (1 AKU migrated, 11 pending)
**Path**: `social-sciences/economics/`

**Subdisciplines**:
- **Business Administration (BWL)**: `bwl/finance/valuation/`
  - **Net Present Value (NPV)**: 1 AKU migrated
    - Financial valuation methodology
    - Semantic annotations for knowledge graphs

**Status**: 
- ✅ 1 AKU successfully migrated
- ⚠️ 11 AKUs pending (missing classification.domain_path)

**Planned Structure**:
- Microeconomics
- Macroeconomics
- Financial economics
- Behavioral economics
- Econometrics

---

### Health Sciences
**Location**: `domain/health-sciences/`

#### Medicine (64 AKUs)
**Path**: `health-sciences/medicine/`

**Specialties**:

##### Vascular Surgery (64 AKUs total)
**Path**: `surgery/vascular/`

**Major Topics**:

1. **Endoleaks - Type 2** (9 AKUs)
   - **Path**: `complications/endoleaks/type-2/`
   - **Categories**:
     - Definitions (3 AKUs): Type 2 definition, classification
     - Pathophysiology (2 AKUs): Retrograde flow, branch vessel sources
     - Diagnosis (1 AKU): CTA imaging findings
     - Management (2 AKUs): Embolization technique, treatment algorithm
     - Clinical (1 AKU): Clinical significance
   - **Visual Guide**: `.renders/type2-endoleak-visual-guide.md`

2. **Mesenteric Ischemia** (55 AKUs)
   - **Path**: `pathology/mesenteric-ischemia/`
   - **Categories**:
     - Definitions (5 AKUs): Overview, acute/chronic types, anatomy, colonic
     - Epidemiology (2 AKUs): AMI and CMI prevalence
     - Pathophysiology (4 AKUs): Arterial occlusion, NOMI, venous thrombosis
     - Diagnosis (8 AKUs): Clinical presentation, lab findings, imaging
     - Imaging (4 AKUs): CTA, duplex ultrasound, angiography, MRA
     - Treatment (9 AKUs): Surgical approaches, endovascular interventions
     - Outcomes (5 AKUs): Mortality, complications, quality of life
     - Follow-up (3 AKUs): Surveillance, prevention, nutrition
     - Guidelines (7 AKUs): SVS, ESVS, ACG clinical pathways
     - Emerging (4 AKUs): Innovations, AI/ML, biomarkers
     - Special Topics (4 AKUs): Pediatric, geriatric, ICU management

**Status**:
- ✅ 64/67 AKUs successfully migrated (95.5%)
- ⚠️ 3 terminology files pending (missing classification.domain_path)

---

## Navigation Patterns

### By Discipline Level

#### Top-Level Domains
```
domain/
├── formal-sciences/      # Logic, math, computer science
├── natural-sciences/     # Physics, chemistry, biology
├── social-sciences/      # Economics, sociology, psychology
└── health-sciences/      # Medicine, nursing, public health
```

#### Subdomain Levels
```
formal-sciences/
└── mathematics/
    ├── pure-mathematics/
    │   └── category-theory/
    │       └── akus/
    └── applied-mathematics/
```

### By Content Type

#### AKUs (Atomic Knowledge Units)
- **Location**: `[domain]/[subdomain]/akus/`
- **Format**: JSON files with structured knowledge
- **Naming**: Descriptive kebab-case (e.g., `ct-001-historical-origins.json`)

#### Renders (Human-Readable Content)
- **Location**: `[domain]/[subdomain]/.renders/`
- **Formats**: Markdown, PDF, PowerPoint
- **Audiences**: Multiple levels (4-year-old to graduate)
- **Languages**: English, German, etc.

#### Documentation
- **README.md**: Each domain/subdomain has comprehensive README
- **Migration Docs**: `domain/_ontology/` for migration guides
- **Tools**: `domain/_ontology/tools/` for migration scripts

---

## Finding Specific Content

### By Topic

#### Want to Learn About Category Theory?
1. **Native Math Domain**: `formal-sciences/mathematics/pure-mathematics/category-theory/`
2. **AKUs**: 8 foundational concepts
3. **README**: `category-theory/README.md`
4. **Cross-Domain**: See applications in functional programming

#### Want to Learn About Functional Programming?
1. **Application Domain**: `science/computer-science/functional-theory/`
2. **Topics**: Functors, monoids, monads
3. **Cross-Refs**: Links to native math definitions
4. **Visual Guide**: `.renders/functional-programming-visual-guide.md`

#### Want Medical Information on Endoleaks?
1. **Domain**: `health-sciences/medicine/surgery/vascular/`
2. **Specific**: `complications/endoleaks/type-2/`
3. **AKUs**: 9 comprehensive files
4. **Visual Guide**: `.renders/type2-endoleak-visual-guide.md`

#### Want Physics at Planck Scale?
1. **Domain**: `natural-sciences/physics/quantum-mechanics/`
2. **Specific**: `planck-units/akus/`
3. **Categories**: Theory (19), Formulas (12), History (1)
4. **Total**: 102 AKUs on fundamental limits

---

## Understanding Cross-Domain Relationships

### Native Domain Principle
**Rule**: Concepts belong to their **origin** field, not application domains.

**Example**: Category Theory
- **Native Domain**: Mathematics (where it originated)
- **Application Domains**: Computer science, type theory
- **Implementation**: Math AKU has `isNativeDomain: true`, FP has cross-references

### Cross-Domain References

#### From Application → Native
Functional programming AKUs include:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/pure-mathematics/category-theory/monad",
      "sourceDomain": "formal-sciences/mathematics/pure-mathematics/category-theory",
      "relationship": "applies",
      "applicationContext": "Monads structure effectful computations in FP"
    }]
  }
}
```

#### From Native → Applications
Category theory AKUs include:
```json
{
  "cross_domain_applications": {
    "programming": "Functional programming uses category theory concepts",
    "type_theory": "Type systems formalized with categorical semantics"
  }
}
```

---

## Migration Status Reference

### Completed Migrations ✅
1. **Category Theory**: 8/8 AKUs → formal-sciences/mathematics
2. **Functional Programming**: 19/19 updated with cross-refs
3. **Physics**: 136/138 AKUs → natural-sciences/physics (99.5%)
4. **Medicine**: 64/67 AKUs → health-sciences/medicine (95.5%)
5. **Economics**: 1/12 AKUs → social-sciences/economics

### Pending Work ⚠️
1. **Economics**: 11 AKUs missing classification.domain_path
2. **Medicine**: 3 terminology files missing classification
3. **Physics**: 2 AKUs skipped during migration
4. **Math**: Remaining content in `science/math/` awaiting migration

### Legacy Paths (Deprecated)
- `science/` → Being replaced by `formal-sciences/` + `natural-sciences/`
- `economics/` → Replaced by `social-sciences/economics/`
- `medicine/` → Replaced by `health-sciences/medicine/`

---

## Quick Reference Commands

### Validation
```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/
```

### Cross-Domain Validation
```bash
# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Validate directory
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

### Migration
```bash
# Migrate domain
python domain/_ontology/tools/migrate_domain.py \
  --source "old/path" \
  --target "new/path" \
  --dry-run  # preview first

# Run actual migration
python domain/_ontology/tools/migrate_domain.py \
  --source "old/path" \
  --target "new/path"
```

---

## Documentation Index

### Getting Started
- `MIGRATION-QUICKSTART.md` - 3-step quick start
- `INDEX.md` - Central navigation
- This file - Domain navigation

### Reference
- `MIGRATION-SUMMARY.md` - Complete migration record
- `VALIDATION-REPORT.md` - QA results
- `TROUBLESHOOTING.md` - Common issues & solutions
- `BEFORE-AFTER-COMPARISON.md` - Visual transformation guide

### Project Management
- `PROJECT-COMPLETION-SUMMARY.md` - Executive summary
- `SESSION-LOG-2026-01-04.md` - Work session timeline
- `.project/roadmap.md` - Project roadmap
- `.project/issues.md` - Issue tracking

### Domain READMEs
- `formal-sciences/README.md`
- `natural-sciences/README.md`
- `social-sciences/README.md`
- `health-sciences/README.md`

### Subdomain READMEs
- `category-theory/README.md`
- `physics/README.md`
- `economics/README.md`
- `medicine/README.md`

---

## Content Statistics

### Total AKUs by Domain
- **Formal Sciences**: 27 (8 category theory + 19 FP updated)
- **Natural Sciences**: 136 (physics)
- **Social Sciences**: 1 (economics, 11 pending)
- **Health Sciences**: 64 (medicine)
- **Grand Total**: 228 AKUs processed

### Documentation
- **Total Files**: 23+ files
- **Total Size**: ~175KB
- **Languages**: English (primary)
- **Formats**: Markdown, visual guides

### Tools
- **Migration Scripts**: 3 reusable Python tools
- **Validators**: 2 (AKU, cross-domain)
- **Success Rate**: 99.5% automated migration

---

## Tips for Navigation

### New Users
1. Start with `INDEX.md` for overview
2. Read `MIGRATION-QUICKSTART.md` for basics
3. Explore your domain of interest (formal/natural/social/health)
4. Read domain README for structure

### Contributors
1. Review `MIGRATION-SUMMARY.md` for context
2. Check `TROUBLESHOOTING.md` for common issues
3. Use migration tools in `domain/_ontology/tools/`
4. Follow native domain principle

### Researchers
1. Navigate to your discipline's domain
2. Browse AKUs for atomic knowledge
3. Check `.renders/` for visual guides
4. Use cross-domain references to find related content

### Developers
1. Read `global-hierarchy.yaml` for authoritative structure
2. Review migration scripts for automation
3. Run validators before committing
4. Check `VALIDATION-REPORT.md` for standards

---

## Support & Resources

### Questions?
- Check `TROUBLESHOOTING.md` first
- Review domain README for structure
- Examine example AKUs for patterns
- Consult migration guides for processes

### Contributing?
- Read `docs/CONTRIBUTING.md`
- Follow native domain principle
- Use migration tools
- Run validators before PR

### Need Help?
- Review comprehensive documentation in `domain/_ontology/`
- Check session logs for recent work
- Examine validation reports for quality standards
- Reference global hierarchy for organization

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Status**: Comprehensive - covers all migrated domains

