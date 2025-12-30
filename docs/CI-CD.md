# CI/CD Pipeline Documentation

> **Last Updated**: 2025-12-30T00:23:00Z  
> **Purpose**: Comprehensive guide to Continuous Integration and Deployment workflows

## Overview

WorldSMEGraphs uses GitHub Actions for automated quality checks, validation, and deployment. This document describes the CI/CD pipeline, how to work with it, and how to troubleshoot issues.

## Active Workflows

### 1. Domain Maturity Check (`domain-maturity-check.yml`)

**Purpose**: Automatically assess and report on knowledge domain maturity and completeness.

**Trigger**: Pull requests modifying:
- `domain/**/*.json` (AKU files)
- `domain/**/COMPLETENESS_METADATA.yaml` (metadata files)

**Process**:
1. Checkout code with full Git history
2. Setup Python 3.11
3. Identify changed domains using Git diff
4. Scan maturity for each changed domain
5. Check for quality regressions (validation rate < 95%)
6. Generate dashboard (HTML + JSON reports)
7. Post comment on PR with maturity report
8. Upload reports as artifacts (30-day retention)
9. Block merge if critical regressions found

**Outputs**:
- PR comment with maturity report (emoji indicators, percentages, gaps)
- Artifact: `maturity-reports/` (JSON + TXT + HTML)
- Status: Pass/Fail based on validation rate

**Permissions Required**:
- `contents: read` - Access repository files
- `pull-requests: write` - Post comments on PRs

**Recent Fixes (2025-12-30)**:
- Added missing permissions block
- Added comprehensive error handling
- Fixed directory existence checks
- Added PR context validation
- No longer fails on non-PR contexts

---

## Validation Scripts

### Local Testing Scripts

All scripts are located in `.github/scripts/` and are executable.

#### `test-workflow-locally.sh`
**Purpose**: Test workflow dependencies and functionality locally before pushing.

**Usage**:
```bash
bash .github/scripts/test-workflow-locally.sh
```

**Checks**:
- ✅ Python 3 installation
- ✅ Required scripts exist
- ✅ Scripts are executable and working
- ✅ Domains with AKUs exist
- ✅ Maturity tracker functionality
- ✅ YAML syntax validation

**Output**: Colored terminal output with pass/fail indicators

---

#### `check-agent-lengths.sh`
**Purpose**: Validate that all agent definitions meet the 180-line minimum requirement.

**Usage**:
```bash
bash .github/scripts/check-agent-lengths.sh
```

**Checks**: All `.agent.md` files in `.github/agents/` directory

**Output**: List of passing/failing agents with line counts

---

#### `validate-structure.sh`
**Purpose**: Verify that the actual file structure matches the documented structure.

**Usage**:
```bash
bash .github/scripts/validate-structure.sh
```

**Checks**:
- Required directories exist
- Essential files present
- Validation scripts available
- Agent files present
- Domain structure correct

---

## Python Validation Tools

### AKU Validation

#### `validate_aku_v2.py` (Domain-Aware)
**Location**: `.project/agents/quality-assurance/tools/`

**Purpose**: Validate AKU files with domain-specific rules.

**Usage**:
```bash
# Single AKU
python3 .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# All AKUs in a domain
python3 .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine

# Directory of AKUs
python3 .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/

# Verbose output
python3 .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json --verbose
```

**Features**:
- Auto-detects domain from `classification.domain_path`
- Domain-specific validation (medicine, math, economics, science)
- Flexible schema based on content type
- Detailed error reporting with suggestions

---

### Domain Maturity Tools

#### `domain_maturity_tracker.py`
**Location**: `.project/agents/domain-maturity/`

**Purpose**: Track maturity level and completeness of knowledge domains.

**Usage**:
```bash
# Single domain
python3 .project/agents/domain-maturity/domain_maturity_tracker.py --domain science/physics/units/planck

# All domains
python3 .project/agents/domain-maturity/domain_maturity_tracker.py --all

# JSON output
python3 .project/agents/domain-maturity/domain_maturity_tracker.py --domain <domain> --format json

# Save to history
python3 .project/agents/domain-maturity/domain_maturity_tracker.py --domain <domain> --save-history
```

**Output**:
- Maturity level (1-5)
- Completeness percentage
- AKU count by type
- Validation pass rate
- Identified gaps

---

#### `generate_dashboard.py`
**Location**: `.project/agents/domain-maturity/`

**Purpose**: Generate visual dashboards of domain maturity.

**Usage**:
```bash
# HTML dashboard for specific domains
python3 .project/agents/domain-maturity/generate_dashboard.py \
  --format html --domains science/physics economics/npv

# ASCII dashboard for all domains
python3 .project/agents/domain-maturity/generate_dashboard.py --format ascii
```

---

#### `compare_maturity.py`
**Location**: `.project/agents/domain-maturity/`

**Purpose**: Compare domain maturity between two points in time.

**Usage**:
```bash
# Compare against baseline
python3 .project/agents/domain-maturity/compare_maturity.py --domain <domain> --baseline baseline.json

# Compare with history
python3 .project/agents/domain-maturity/compare_maturity.py --domain <domain> --since 2025-01-01
```

---

## Workflow Development

### Creating a New Workflow

1. Create YAML file in `.github/workflows/`
2. Define trigger events (on push, PR, schedule, etc.)
3. Add required permissions block
4. Define jobs and steps
5. Add error handling (try-catch in scripts)
6. Test locally using validation scripts
7. Update `.github/workflows/README.md`
8. Add badge to main README if needed

**Example Template**:
```yaml
name: My Workflow

on:
  pull_request:
    paths:
      - 'path/to/watch/**'

jobs:
  my-job:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      # Add other permissions as needed
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      # Add your steps here
```

---

### Best Practices

#### Error Handling
- Always wrap GitHub Scripts in try-catch
- Check for file/directory existence before reading
- Validate context (PR, commit, etc.) before actions
- Use `if: always()` for cleanup steps
- Log errors but don't necessarily fail workflow

#### Permissions
- Always add explicit permissions block
- Use least privilege (only what's needed)
- Document why each permission is needed

#### Testing
- Test locally before pushing
- Use validation scripts
- Check for deprecation warnings
- Validate YAML syntax

#### Documentation
- Update workflow README when adding workflows
- Add troubleshooting guides
- Document dependencies
- Include usage examples

---

## Troubleshooting

### Workflow Fails at "Comment on PR"

**Symptoms**: Workflow fails when trying to post PR comment.

**Causes**:
- Missing `pull-requests: write` permission
- Not running in PR context
- GitHub API rate limit
- Network issues

**Solutions**:
1. Check permissions block includes `pull-requests: write`
2. Verify workflow triggered by PR event
3. Check GitHub Actions logs for specific error
4. Add error handling to make step non-fatal if needed

---

### Python Script Errors

**Symptoms**: Steps running Python scripts fail.

**Causes**:
- Python not installed
- Script not found
- Missing dependencies
- Invalid input data

**Solutions**:
1. Verify Python setup step runs successfully
2. Check script paths are correct
3. Test scripts locally first
4. Add error handling in scripts
5. Use `|| true` for non-critical scripts

---

### YAML Syntax Errors

**Symptoms**: Workflow doesn't appear in Actions tab or fails to parse.

**Causes**:
- Invalid YAML syntax
- Incorrect indentation
- Missing required fields

**Solutions**:
1. Validate YAML locally:
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('.github/workflows/file.yml'))"
   ```
2. Use YAML linter or validator
3. Check GitHub Actions documentation for correct syntax

---

### Workflow Runs But Doesn't Do What's Expected

**Symptoms**: Workflow succeeds but doesn't produce expected results.

**Causes**:
- Incorrect trigger paths
- Wrong Git refs or branches
- Cached data
- Timing issues

**Solutions**:
1. Check trigger paths match changed files
2. Verify `fetch-depth` for Git operations
3. Add debug output to understand what's happening
4. Check step conditions and `if:` statements

---

## Monitoring and Maintenance

### Regular Checks
- Review workflow run history weekly
- Check for deprecation warnings
- Monitor execution times
- Review artifact storage usage

### Updates
- Keep action versions current (e.g., `actions/checkout@v4`)
- Update Python version as needed
- Review and update permissions
- Refresh documentation

### Metrics to Track
- Success/failure rate
- Average execution time
- Artifact storage used
- API rate limit usage

---

## Getting Help

1. Check workflow run logs in GitHub Actions tab
2. Review this documentation
3. Consult `.github/workflows/README.md` for workflow-specific help
4. Review `.project/issues.md` for known issues
5. Test locally using validation scripts
6. Check GitHub Actions documentation
7. Contact repository maintainers

---

## Related Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow README](../.github/workflows/README.md)
- [Project Issues](../.project/issues.md)
- [Improvements Tracking](../.project/improvements.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

**Maintained By**: Infrastructure Team  
**Review Schedule**: Monthly  
**Last Review**: 2025-12-30
