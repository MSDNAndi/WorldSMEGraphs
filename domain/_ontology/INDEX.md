# Domain Migration Documentation Index

> **Purpose**: Central index for all domain hierarchy migration documentation  
> **Last Updated**: 2026-01-04  
> **Status**: Complete for Phase 1-4

## Quick Links

### For New Users
- **Start Here**: [Migration Quick-Start Guide](MIGRATION-QUICKSTART.md)
- **Navigation**: [Domain Navigation Guide](DOMAIN-NAVIGATION-GUIDE.md) ⭐ NEW
- **Checklist**: [Migration Checklist Template](MIGRATION-CHECKLIST-TEMPLATE.md) ⭐ NEW
- **Overview**: [Migration Summary](MIGRATION-SUMMARY.md)
- **Results**: [Validation Report](VALIDATION-REPORT.md)

### For Project Managers
- **Completion Summary**: [`../.project/PROJECT-COMPLETION-SUMMARY.md`](../.project/PROJECT-COMPLETION-SUMMARY.md)
- **Issue Tracking**: [`../.project/issues.md`](../.project/issues.md) (Issue #3)
- **Roadmap**: [`../.project/roadmap.md`](../.project/roadmap.md) (Phase 1 status)

### For Developers
- **Global Hierarchy**: [global-hierarchy.yaml](global-hierarchy.yaml)
- **Migration Guide**: [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md)
- **Tools Documentation**: [TOOLS-DOCUMENTATION.md](TOOLS-DOCUMENTATION.md) ⭐ NEW
- **Domain Comparison**: [DOMAIN-COMPARISON-MATRIX.md](DOMAIN-COMPARISON-MATRIX.md) ⭐ NEW
- **Design Documentation**: [README.md](README.md)

### For Contributors
- **Contributing Guide**: [`../../docs/CONTRIBUTING.md`](../../docs/CONTRIBUTING.md)
- **Migration Checklist**: [MIGRATION-CHECKLIST-TEMPLATE.md](MIGRATION-CHECKLIST-TEMPLATE.md) ⭐ NEW
- **Quick-Start**: [MIGRATION-QUICKSTART.md](MIGRATION-QUICKSTART.md)
- **Before/After Comparison**: [BEFORE-AFTER-COMPARISON.md](BEFORE-AFTER-COMPARISON.md)

## Documentation Overview

### Migration Planning & Design

| Document | Purpose | Audience |
|----------|---------|----------|
| [global-hierarchy.yaml](global-hierarchy.yaml) | Authoritative domain taxonomy | All |
| [README.md](README.md) | Ontology design principles | Architects, Developers |
| [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md) | Detailed migration patterns | Developers |

### Migration Execution

| Document | Purpose | Audience |
|----------|---------|----------|
| [MIGRATION-QUICKSTART.md](MIGRATION-QUICKSTART.md) | Quick 3-step guide | New users |
| [MIGRATION-CHECKLIST-TEMPLATE.md](MIGRATION-CHECKLIST-TEMPLATE.md) | 22-step detailed checklist | Contributors ⭐ NEW |
| [MIGRATION-SUMMARY.md](MIGRATION-SUMMARY.md) | Complete migration record | All |
| [VALIDATION-REPORT.md](VALIDATION-REPORT.md) | Quality assurance results | QA, Management |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common issues & solutions | Developers, Users |
| [BEFORE-AFTER-COMPARISON.md](BEFORE-AFTER-COMPARISON.md) | Visual hierarchy transformation | All |

### Navigation & Reference

| Document | Purpose | Audience |
|----------|---------|----------|
| [DOMAIN-NAVIGATION-GUIDE.md](DOMAIN-NAVIGATION-GUIDE.md) | Complete navigation system | All ⭐ NEW |
| [DOMAIN-COMPARISON-MATRIX.md](DOMAIN-COMPARISON-MATRIX.md) | Side-by-side domain analysis | Architects, Developers ⭐ NEW |
| [TOOLS-DOCUMENTATION.md](TOOLS-DOCUMENTATION.md) | Comprehensive tool guide | Developers ⭐ NEW |

### Project Management

| Document | Purpose | Audience |
|----------|---------|----------|
| [../.project/PROJECT-COMPLETION-SUMMARY.md](../.project/PROJECT-COMPLETION-SUMMARY.md) | Executive summary | Management, Stakeholders |
| [../.project/SESSION-LOG-2026-01-04.md](../.project/SESSION-LOG-2026-01-04.md) | Work session timeline | Team, Management |
| [../.project/issues.md](../.project/issues.md) | Issue tracking (Issue #3) | Development team |
| [../.project/structure.md](../.project/structure.md) | Project structure status | All |
| [../.project/roadmap.md](../.project/roadmap.md) | Phase tracking | Management |

### Domain-Specific Documentation

| Domain | README Location | AKUs | Status |
|--------|----------------|------|---------|
| Formal Sciences | [../../domain/formal-sciences/README.md](../../domain/formal-sciences/README.md) | 27 | ✅ Active |
| → Mathematics / Category Theory | [../../domain/formal-sciences/mathematics/pure-mathematics/category-theory/README.md](../../domain/formal-sciences/mathematics/pure-mathematics/category-theory/README.md) | 8 | ✅ Complete |
| Natural Sciences | [../../domain/natural-sciences/README.md](../../domain/natural-sciences/README.md) | 136 | ✅ Active |
| → Physics | [../../domain/natural-sciences/physics/README.md](../../domain/natural-sciences/physics/README.md) | 136 | ✅ Complete |
| Social Sciences | [../../domain/social-sciences/README.md](../../domain/social-sciences/README.md) | 1 | ⚠️ Partial |
| Health Sciences | [../../domain/health-sciences/README.md](../../domain/health-sciences/README.md) | 64 | ✅ Active |

### Tools & Scripts

| Tool | Purpose | Location |
|------|---------|----------|
| migrate_category_theory.py | Category theory migration | [tools/migrate_category_theory.py](tools/migrate_category_theory.py) |
| update_fp_cross_domain.py | FP cross-domain refs | [tools/update_fp_cross_domain.py](tools/update_fp_cross_domain.py) |
| migrate_domain.py | General migration | [tools/migrate_domain.py](tools/migrate_domain.py) |
| validate_cross_domain.py | Cross-domain validation | [tools/validate_cross_domain.py](tools/validate_cross_domain.py) |

## Migration Statistics

### Overall Success
- **Total AKUs Processed**: 228
- **Migrated**: 209 (91.7%)
- **Updated**: 19 (8.3%)
- **Success Rate**: 99.5%
- **Validation Pass Rate**: 99.5%

### By Domain
| Domain | Found | Migrated | Success % |
|--------|-------|----------|-----------|
| Category Theory | 8 | 8 | 100% |
| Functional Programming | 19 | 19 (updated) | 100% |
| Physics | 138 | 136 | 99.5% |
| Economics | 12 | 1 | 8.3%* |
| Medicine | 67 | 64 | 95.5% |

*Economics low rate due to pre-existing data quality issues

## Key Concepts

### Native Domain Principle
Every concept belongs to exactly ONE native domain - the field where it was originally developed, regardless of where it's heavily used.

**Example**: Category theory is mathematics (native), even though it's heavily used in computer science.

### Cross-Domain References
Application domains link to native domain concepts via `cross_domain_references`:
```json
{
  "cross_domain_references": {
    "applies": [{
      "@id": "wsmg:formal-sciences/mathematics/.../monad",
      "sourceDomain": "formal-sciences/mathematics/...",
      "relationship": "applies",
      "applicationContext": "..."
    }]
  }
}
```

### Domain Markers
- **Native Domain**: `isNativeDomain: true`
- **Application Domain**: `isApplicationDomain: true`, `isNativeDomain: false`

## Reading Path

### For Complete Understanding
1. Read [global-hierarchy.yaml](global-hierarchy.yaml) to understand taxonomy
2. Read [README.md](README.md) for design principles
3. Read [MIGRATION-SUMMARY.md](MIGRATION-SUMMARY.md) for what was done
4. Read [VALIDATION-REPORT.md](VALIDATION-REPORT.md) for quality assurance

### For Quick Start
1. Read [MIGRATION-QUICKSTART.md](MIGRATION-QUICKSTART.md)
2. Try: `migrate_domain.py --source X --target Y --dry-run`
3. Review validation results

### For Management Review
1. Read [PROJECT-COMPLETION-SUMMARY.md](../.project/PROJECT-COMPLETION-SUMMARY.md)
2. Check metrics and success criteria
3. Review next steps

## Troubleshooting

### Issue: Can't find migration documentation
**Solution**: Start with this index file

### Issue: Don't know which domain to use
**Solution**: Consult [global-hierarchy.yaml](global-hierarchy.yaml)

### Issue: Migration tool not working
**Solution**: See [MIGRATION-QUICKSTART.md](MIGRATION-QUICKSTART.md) troubleshooting section

### Issue: Validation failing
**Solution**: See [VALIDATION-REPORT.md](VALIDATION-REPORT.md) for common warnings

## Next Steps

### Immediate
- Fix 11 economics AKUs missing classification
- Fix 3 medicine terminology files
- Investigate 2 skipped physics AKUs

### Near-Term
- Migrate remaining math content (science/math/)
- Migrate functional-theory to new location
- Remove legacy directories

### Long-Term
- Complete all domain migrations
- Deprecate legacy structure
- Implement automated rendering

## Contact & Support

- **Questions?**: See individual document "Questions?" sections
- **Issues?**: Add to [`../.project/issues.md`](../.project/issues.md)
- **Improvements?**: Add to [`../.project/improvements.md`](../.project/improvements.md)

---

**Index Version**: 1.0.0  
**Last Updated**: 2026-01-04  
**Maintained By**: GitHub Copilot  
**Status**: Complete for Phase 1-4
