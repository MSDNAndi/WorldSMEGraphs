# GitHub Actions Workflows

This directory contains GitHub Actions workflow files for automated quality checks and CI/CD.

## Active Workflows

### Domain Maturity Check (`domain-maturity-check.yml`)
**Status**: ✅ Active and Fixed (2025-12-30)

Automatically checks the maturity and completeness of knowledge domains when AKU files are modified in pull requests.

**Triggers:**
- Pull requests that modify files in `domain/**/*.json`
- Pull requests that modify `domain/**/COMPLETENESS_METADATA.yaml`

**Features:**
- Identifies changed domains automatically
- Scans maturity level (1-5) for each domain
- Checks completeness percentage
- Validates AKU quality (validation pass rate)
- Analyzes type distribution (definitions, formulas, theory, examples)
- Posts detailed maturity report as PR comment
- Blocks merge if validation rate < 95%

**Recent Fix (2025-12-30):**
- Added required `permissions` block (`contents: read`, `pull-requests: write`)
- Added error handling with try-catch in GitHub Script
- Added directory existence checks
- Added PR context validation
- Prevents workflow failures from blocking CI

**Dependencies:**
- `.project/agents/domain-maturity/domain_maturity_tracker.py`
- `.project/agents/domain-maturity/generate_dashboard.py`
- `.project/agents/domain-maturity/compare_maturity.py`

---

## Planned Workflows

### Knowledge Graph Validation
Automatically validate knowledge graph files on push:
- Check JSON schema compliance
- Verify cross-links point to valid targets
- Validate UID format
- Check for orphaned nodes

### Rendering Generation
Automatically generate renderings when knowledge graphs change:
- Detect changes to knowledge.graph files
- Generate renderings for all configured languages/audiences
- Commit generated files back to repository

### Documentation Updates
Keep documentation in sync:
- Update structure.md when files are added/removed
- Check for broken cross-references
- Validate all links in markdown files

### Quality Checks
Automated quality assurance:
- Run readability metrics on renderings
- Check for duplicate content
- Validate file naming conventions
- Verify .gitignore effectiveness

## Future Enhancements
- Continuous Integration testing
- Automated agent performance reporting
- Cross-domain link validation
- Rendering quality scoring

---

## Troubleshooting Workflow Failures

### Common Issues and Solutions

#### "Comment on PR" Step Failing
**Symptoms:** Workflow fails at the PR comment step with permission errors or script errors.

**Solutions:**
1. Ensure `permissions` block includes `pull-requests: write`
2. Check that the workflow is triggered from a PR context
3. Verify `maturity-reports/` directory exists and contains JSON files
4. Check that Python scripts are executable and working

#### Python Script Errors
**Symptoms:** Steps that run Python scripts fail with import or execution errors.

**Solutions:**
1. Verify Python 3.11 is installed (check "Setup Python" step)
2. Ensure all scripts in `.project/agents/domain-maturity/` are present
3. Test scripts locally: `python3 script.py --help`
4. Check that domains have valid AKU structure

#### No Maturity Reports Generated
**Symptoms:** Workflow succeeds but posts "No maturity reports generated" comment.

**Solutions:**
1. Verify PR modifies files in `domain/**/*.json`
2. Check that changed domains have `akus/` subdirectories
3. Ensure AKU files are valid JSON format
4. Review "Identify changed domains" step output

#### Regression Check Blocking Merge
**Symptoms:** Workflow blocks PR merge due to validation rate < 95%.

**Solutions:**
1. Review failing AKUs in the maturity report
2. Run validator locally: `python3 .project/agents/quality-assurance/tools/validate_aku_v2.py --domain <domain>`
3. Fix validation errors in AKU files
4. Re-run workflow after fixes

### Testing Workflows Locally

Test Python scripts before pushing:
```bash
# Test domain maturity tracker
python3 .project/agents/domain-maturity/domain_maturity_tracker.py --domain science/physics/units/planck

# Test dashboard generation
python3 .project/agents/domain-maturity/generate_dashboard.py --domains science/physics/units/planck

# Validate AKUs
python3 .project/agents/quality-assurance/tools/validate_aku_v2.py --domain science/physics/units/planck
```

### Getting Help

1. Check workflow run logs in GitHub Actions tab
2. Review `.project/issues.md` for known issues
3. Consult `.github/copilot-instructions.md` for development guidelines
4. Contact repository maintainers

---

**Status**: Workflows planned for Phase 3 (Automation) of the project roadmap.
