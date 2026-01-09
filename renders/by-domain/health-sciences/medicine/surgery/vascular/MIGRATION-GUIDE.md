# Migration Guide: Old to New Structure

**Date**: 2026-01-09  
**Reason**: Alignment with domain ontology

## Overview

The vascular surgery render structure was refactored to align with the authoritative domain hierarchy defined in `domain/_ontology/global-hierarchy.yaml`. This document helps you update any bookmarks, links, or references to the old structure.

## What Changed?

### High-Level Summary

**Old structure**: All comics under `.../complications/endoleaks/type-2/english/`  
**New structure**: Comics organized by category (procedures/pathology/complications)

## Path Mappings

### Pathology Topics

#### Abdominal Aortic Aneurysm
```
OLD: .../complications/endoleaks/type-2/english/abdominal-aortic-aneurysm/
NEW: .../pathology/abdominal-aortic-aneurysm/english/abdominal-aortic-aneurysm/
```

#### Carotid Artery Stenosis
```
OLD: .../complications/endoleaks/type-2/english/carotid-artery-stenosis/
NEW: .../pathology/carotid-artery-stenosis/english/carotid-artery-stenosis/

OLD: .../complications/endoleaks/type-2/english/carotid-artery-stenosis-v2/
NEW: .../pathology/carotid-artery-stenosis/english/carotid-artery-stenosis-v2/
```

#### Varicose Veins
```
OLD: .../complications/endoleaks/type-2/english/varicose-veins/
NEW: .../pathology/varicose-veins/english/varicose-veins/

OLD: .../complications/endoleaks/type-2/english/varicose-veins-v2/
NEW: .../pathology/varicose-veins/english/varicose-veins-v2/
```

#### Acute Limb Ischemia
```
OLD: .../complications/endoleaks/type-2/english/acute-limb-ischemia/
NEW: .../pathology/acute-limb-ischemia/english/acute-limb-ischemia/

OLD: .../complications/endoleaks/type-2/english/acute-limb-ischemia-v2/
NEW: .../pathology/acute-limb-ischemia/english/acute-limb-ischemia-v2/
```

### Procedure Topics

#### Diabetic Foot Bypass
```
OLD: .../complications/endoleaks/type-2/english/diabetic-foot-bypass/
NEW: .../procedures/bypass/english/diabetic-foot-bypass/

OLD: .../complications/endoleaks/type-2/english/diabetic-foot-bypass-v2/
NEW: .../procedures/bypass/english/diabetic-foot-bypass-v2/
```

### Unchanged

#### Type 2 Endoleak (Correctly Placed)
```
SAME: .../complications/endoleaks/type-2/english/comic/
```

## Finding Content in New Structure

### By Category

**Pathology** (disease conditions):
- `/renders/by-domain/health-sciences/medicine/surgery/vascular/pathology/`

**Procedures** (surgical techniques):
- `/renders/by-domain/health-sciences/medicine/surgery/vascular/procedures/`

**Complications** (post-surgery issues):
- `/renders/by-domain/health-sciences/medicine/surgery/vascular/complications/`

### Using the Index

The easiest way to find content is using the **INDEX.md** file:
```
/renders/by-domain/health-sciences/medicine/surgery/vascular/INDEX.md
```

This provides direct links to all comics and viewing formats.

## For Developers

### Git History

All moves used `git mv`, so file history is preserved:

```bash
# See history of a moved file
git log --follow path/to/new/location/file.md
```

### Automated Migration

If you have scripts that reference the old paths:

```bash
# Find old pattern
OLD_BASE=".../complications/endoleaks/type-2/english"

# Replace with appropriate new base:
# - For pathology: ".../pathology/[topic]/english"
# - For procedures: ".../procedures/[type]/english"
```

### Regex Pattern

Old path pattern:
```regex
complications/endoleaks/type-2/english/([^/]+)/
```

New path patterns:
```regex
# Pathology
pathology/\1/english/\1/

# Procedures
procedures/[procedure-type]/english/\1/
```

## Updating Bookmarks

### Browser Bookmarks

If you had bookmarks to the old paths:

1. **Use the INDEX.md** - Bookmark this instead for quick navigation
2. **Update specific bookmarks** - Use the path mappings above
3. **Or browse by category** - Navigate to pathology/procedures/complications

### Documentation Links

If you maintain documentation that links to these comics:

1. **Update all references** to use new paths
2. **Consider linking to INDEX.md** instead for stability
3. **Use relative paths** where possible for resilience

## Quick Reference Table

| Topic | Old Location | New Location | Type |
|-------|-------------|--------------|------|
| AAA | `...endoleaks/type-2/english/abdominal-aortic-aneurysm/` | `.../pathology/abdominal-aortic-aneurysm/english/...` | Pathology |
| Carotid Stenosis | `...endoleaks/type-2/english/carotid-artery-stenosis/` | `.../pathology/carotid-artery-stenosis/english/...` | Pathology |
| Varicose Veins | `...endoleaks/type-2/english/varicose-veins/` | `.../pathology/varicose-veins/english/...` | Pathology |
| Acute Limb Ischemia | `...endoleaks/type-2/english/acute-limb-ischemia/` | `.../pathology/acute-limb-ischemia/english/...` | Pathology |
| Diabetic Bypass | `...endoleaks/type-2/english/diabetic-foot-bypass/` | `.../procedures/bypass/english/...` | Procedure |
| Type 2 Endoleak | `...endoleaks/type-2/english/comic/` | *No change* | Complication |

## Need Help?

- **Can't find something?** Check [INDEX.md](INDEX.md)
- **Technical details?** See [REFACTORING-SUMMARY.md](REFACTORING-SUMMARY.md)
- **Getting started?** Read [QUICK-START.md](QUICK-START.md)
- **General info?** View [README.md](README.md)

## Rollback (Emergency Only)

If you absolutely need to revert to the old structure:

```bash
# Check out the commit before refactoring
git checkout 52ea822~1

# Or restore specific files
git restore --source=52ea822~1 path/to/file
```

**Note**: This is NOT recommended. The new structure is correct per the ontology.

## Benefits of New Structure

1. **Ontologically Correct**: Matches official domain hierarchy
2. **Better Organization**: Clear separation of concepts
3. **Easier Discovery**: Find topics by their classification
4. **Maintainable**: Logical structure for future additions
5. **Scalable**: Easy to add more procedures, pathologies, etc.

---

**Questions?** Create an issue in the repository or consult the documentation files listed above.
