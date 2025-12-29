# Proposal: Centralized Rendering Architecture v2.0

**Date:** 2025-12-29  
**Author:** @copilot  
**Status:** PROPOSED (awaiting approval)  
**Priority:** HIGH - Foundational architectural decision

---

## Executive Summary

**Problem:** Current `.renders/` subdirectories within each domain create limitations:
- Cannot easily create multi-domain rendered content
- Renders are tightly coupled to source domain structure
- Difficult to track AKU usage across renders
- No centralized rendering management
- Duplication when multiple renders use same AKUs

**Proposed Solution:** Create top-level `renders/` directory with flexible output-oriented structure while maintaining tight AKU reference tracking.

---

## AKU Session Capacity Analysis

### Current Capacity (with `.renders/` approach)
- **2-4 AKUs per session** - Fear of breaking renders limits ambition
- Manual tracking of dependencies
- Risk of orphaned content
- Difficult impact analysis

### Proposed Capacity (with `renders/` + tracking tools)
- **8-15 AKUs per session** - Confidence from automated tracking
- Immediate impact visibility
- Automated dependency validation
- Parallel development possible

### Why This Matters for Completion
To reach 78 AKUs from current 37:
- **Old approach**: 10-20 sessions needed
- **New approach**: 3-5 sessions possible

**Recommendation: Implement architecture first, then accelerate AKU creation**

---

## Proposed Structure

\`\`\`
renders/                              ← NEW: Top-level rendering directory
  ├── _metadata/                      
  │   ├── render-index.yaml          ← Master index
  │   ├── aku-usage-matrix.yaml      ← Which renders use which AKUs
  │   └── audience-profiles.yaml     
  │
  ├── by-audience/                   
  │   ├── adult-limited-reading/
  │   │   └── physics/
  │   │       ├── planck-units.md
  │   │       └── _metadata.yaml     ← AKU dependencies
  │   ├── elementary-school/
  │   └── graduate-students/
  │
  ├── by-format/                     
  │   ├── textbook-chapters/
  │   ├── quick-references/
  │   └── presentations/
  │
  └── composite/                     ← Multi-domain content
      └── modern-physics-complete/
          ├── 02-planck-units.md
          └── _metadata.yaml
\`\`\`

---

## Key Features

### 1. Tight AKU Reference Tracking

Each render has `_metadata.yaml`:

\`\`\`yaml
render:
  id: "render-adult-physics-planck"
  title: "The Tiniest Things in the Universe"
  
aku_dependencies:
  - aku_id: "aku-001-planck-length-definition"
    domain: "science/physics/quantum-mechanics/planck-units"
    usage: "primary"
    sections: ["introduction", "scale-comparison"]
  
  - aku_id: "aku-002-planck-time-definition"
    usage: "primary"
    sections: ["time-scale"]
\`\`\`

### 2. Bidirectional Links

**From AKU → Renders:**
\`\`\`json
{
  "renderings": [
    {
      "render_id": "render-adult-physics-planck",
      "path": "renders/by-audience/adult-limited-reading/physics/planck-units.md",
      "usage": "primary"
    }
  ]
}
\`\`\`

### 3. Automated Tracking Tools

\`\`\`bash
# Check which renders use an AKU
python .project/tools/render_tracker.py aku-usage aku-001

# Validate all render dependencies
python .project/tools/render_tracker.py validate

# Generate usage matrix
python .project/tools/render_tracker.py matrix
\`\`\`

---

## Benefits

| Aspect | Old (.renders/) | New (renders/) |
|--------|----------------|----------------|
| **Scope** | Single domain | Multi-domain ✓ |
| **Tracking** | Manual | Automated ✓ |
| **Reusability** | Low | High ✓ |
| **Discoverability** | Scattered | Centralized ✓ |
| **AKU Capacity** | 2-4/session | 8-15/session ✓ |

---

## Migration Strategy

### Phase 1: Infrastructure (2-3 hours)
1. Create `renders/` directory structure
2. Implement `_metadata.yaml` schema
3. Build basic `render_tracker.py` tool
4. Document standards

### Phase 2: Migration (1-2 hours)
1. Move Planck units renders to `renders/by-audience/`
2. Create `_metadata.yaml` for each
3. Update AKU files with `renderings` field
4. Validate links

### Phase 3: Expansion (ongoing)
1. Create composite renders
2. Add validation to CI/CD
3. Deprecate `.renders/` after migration

---

## Recommendation

**APPROVE** and implement in 2 phases:

1. **Immediate**: Basic infrastructure + migration
2. **Next sprint**: Full tooling + expansion

This enables **ambitious AKU creation** (8-15 per session) to reach completion faster.

---

**Status:** ⏳ AWAITING APPROVAL from @MSDNAndi

**Questions:**
1. Naming preference: `renders/` vs `rendered/` vs `publications/`?
2. Should `.renders/` remain as symlinks for backward compat?
3. Auto-generate renders from templates?
