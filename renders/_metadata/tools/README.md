# Renders Metadata Tools

**Location**: `renders/_metadata/tools/`  
**Purpose**: Automation tools for render management and validation  
**Last Updated**: 2026-01-06

---

## Available Tools

### 1. generate_render_index.py

**Purpose**: Scans renders directory and generates comprehensive index

**What it does**:
- Scans all files in `renders/by-domain/`
- Extracts metadata (domain, language, file type, size)
- Generates statistics (by language, domain, extension)
- Creates `render-index.yaml` with complete catalog

**Usage**:
```bash
python renders/_metadata/tools/generate_render_index.py
```

**Output**: `renders/_metadata/render-index.yaml`

**When to run**:
- After adding new renders
- After modifying existing renders
- Before committing render changes
- Automatically via CI/CD

**Example Output**:
```
Scanning renders directory...
Generated: renders/_metadata/render-index.yaml
Total: 255 files
```

---

### 2. generate_aku_usage_matrix.py

**Purpose**: Tracks which renders use which AKUs (bidirectional mapping)

**What it does**:
- Scans all AKU files in `domain/` hierarchy
- Scans all render files for AKU references
- Creates bidirectional mapping:
  - AKU → renders (which renders use this AKU)
  - Render → AKUs (which AKUs does this render use)
- Calculates coverage metrics

**Usage**:
```bash
python renders/_metadata/tools/generate_aku_usage_matrix.py
```

**Output**: `renders/_metadata/aku-usage-matrix.yaml`

**When to run**:
- After adding new renders
- After modifying AKU files
- To assess render coverage
- For impact analysis of AKU changes

**Example Output**:
```
Finding AKUs...
Found 658 AKU files
Scanning renders for AKU references...
Found 2 renders with AKU references

AKU Usage Matrix Generation Complete
Total AKUs: 658
AKUs with renders: 18 (2.7%)
```

**What it tracks**:
- Total AKUs in repository
- AKUs with at least one render
- Renders that reference AKUs
- Coverage percentage
- Most referenced AKUs

---

### 3. render_quality_linter.py

**Purpose**: Checks rendered content for quality issues

**What it checks**:
- **Readability**: Sentence length, word count
- **Filename**: Naming conventions (kebab-case)
- **Metadata**: YAML frontmatter validation
- **Headings**: Proper hierarchy, no skipped levels
- **Images**: Alt text presence, file existence
- **Links**: Descriptive link text (not "click here")
- **Length**: Very short or very long content
- **Structure**: Overall content organization

**Usage**:
```bash
# Check single file
python renders/_metadata/tools/render_quality_linter.py renders/by-domain/path/to/file.md

# Check entire directory
python renders/_metadata/tools/render_quality_linter.py renders/by-domain/natural-sciences/physics/
```

**Output**: Issues and warnings report with actionable suggestions

**Example Output**:
```
======================================================================
Render Quality Linter Report
======================================================================
Files checked: 12
Issues: 2
Warnings: 5

ISSUES (must fix)
======================================================================
renders/by-domain/physics/planck-units/english/elementary.md:
  ❌ Image missing alt text: diagram.png

WARNINGS (should fix)
======================================================================
renders/by-domain/physics/planck-units/english/graduate.md:
  ⚠️  Average sentence length 35.2 words (consider shorter sentences)
  ⚠️  Poor link text: 'click here' (use descriptive text)
```

---

### 4. create_render.sh

**Purpose**: Interactive helper to create new renders with proper structure

**What it does**:
- Creates directory structure
- Generates render template with metadata
- Auto-runs index generators
- Provides next-step guidance

**Usage**:
```bash
bash renders/_metadata/tools/create_render.sh [domain-path] [language] [audience]
```

**Example**:
```bash
# Create undergraduate English render for Planck units
bash renders/_metadata/tools/create_render.sh \
  natural-sciences/physics/quantum-mechanics/planck-units \
  english \
  undergraduate

# Output:
# ✓ Created directory
# ✓ Created render file with template
# ✓ Regenerated render index
# ✓ Regenerated AKU usage matrix
# Next steps: Edit file, check quality, commit
```

**Available Audiences**:
- preschool, elementary-school, middle-school, high-school
- undergraduate, graduate, adult-limited-reading, professional

**Template Generated**:
- Proper heading structure
- Metadata placeholders
- Section guidelines for audience
- Source attribution

---

## Tool Development Guidelines

### Creating New Tools

1. **Location**: Place in `renders/_metadata/tools/`
2. **Format**: Python scripts (use standard library only)
3. **Naming**: Use `snake_case.py`
4. **Documentation**: Include docstring with usage
5. **Error handling**: Graceful failures with clear messages

### Template Structure

```python
#!/usr/bin/env python3
"""
Tool Name

Brief description of what it does.

Usage:
    python tool_name.py [options]
"""

import os
import yaml
from datetime import datetime

def main():
    """Main function."""
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

### Best Practices

**DO**:
- Use standard library only (no external dependencies)
- Make scripts executable (`chmod +x script.py`)
- Include comprehensive docstrings
- Print progress messages
- Handle errors gracefully
- Output to `renders/_metadata/` directory
- Use YAML for human-readable output
- Include timestamp in generated files

**DON'T**:
- Require external dependencies
- Modify files outside renders/
- Assume specific directory structure (use os.path)
- Silently fail (print errors)
- Hardcode paths (make relative to script location)

---

## Planned Tools (Future)

See `renders/_metadata/RECOMMENDATIONS.md` for complete roadmap:

### render_quality_linter.py (Week 2)
- Check readability scores
- Validate metadata format
- Check for broken references
- Verify audience compliance
- Accessibility checks

### render_metadata_generator.py (Week 2)
- Generate metadata.yaml for renders
- Extract reading level
- Calculate word count
- Determine audience fit

### translation_status_tracker.py (Week 3)
- Track translation progress
- Compare versions across languages
- Identify missing translations
- Generate translation reports

### render_search.py (Week 4+)
- Full-text search across renders
- Filter by language, audience, domain
- Search by AKU references
- Export search results

### render_comparator.py (Week 4+)
- Compare different audience levels
- Track content evolution
- Identify inconsistencies
- Suggest improvements

---

## CI/CD Integration

Tools are integrated into GitHub Actions workflows:

### validate-renders.yml

**Triggers**:
- Push to `renders/**`
- Push to `domain/**/*.graph`
- Pull requests
- Manual workflow_dispatch

**What it does**:
1. Validates directory structure
2. Checks for legacy `.renders/` directories
3. Regenerates render index (verifies up-to-date)
4. Counts renders by language and type
5. Checks for orphaned renders
6. Validates documentation references

**See**: `.github/workflows/validate-renders.yml`

---

## Usage Examples

### Example 1: After Adding New Renders

```bash
# 1. Add your new render files
touch renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/undergraduate.md

# 2. Edit the render
vim renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/undergraduate.md

# 3. Regenerate index
python renders/_metadata/tools/generate_render_index.py

# 4. Update AKU usage matrix
python renders/_metadata/tools/generate_aku_usage_matrix.py

# 5. Commit everything
git add renders/
git commit -m "Add undergraduate render for Planck units"
```

### Example 2: Checking AKU Coverage

```bash
# Generate matrix
python renders/_metadata/tools/generate_aku_usage_matrix.py

# View matrix
cat renders/_metadata/aku-usage-matrix.yaml | grep "coverage_percentage"

# Find AKUs without renders
# (Look for AKUs not in aku_to_renders section)
```

### Example 3: Impact Analysis

**Question**: "If I change aku-001-mesenteric-ischemia, which renders are affected?"

```bash
# Generate matrix
python renders/_metadata/tools/generate_aku_usage_matrix.py

# Search matrix
grep -A5 "aku-001-mesenteric-ischemia" renders/_metadata/aku-usage-matrix.yaml
```

---

## Troubleshooting

### Tool fails with "No such file or directory"

**Cause**: Running from wrong directory

**Solution**: Run from repository root or use absolute paths

```bash
cd /path/to/WorldSMEGraphs
python renders/_metadata/tools/generate_render_index.py
```

### "Permission denied" error

**Cause**: Script not executable

**Solution**: 
```bash
chmod +x renders/_metadata/tools/generate_render_index.py
```

### Tool runs but produces no output

**Cause**: No renders found

**Solution**: Check that `renders/by-domain/` exists and contains files

```bash
ls -R renders/by-domain/
```

### YAML file not updating

**Cause**: Tool completed but file cached

**Solution**: 
```bash
# Force refresh
rm renders/_metadata/render-index.yaml
python renders/_metadata/tools/generate_render_index.py
```

---

## Contributing

To add a new tool:

1. Create Python script in `renders/_metadata/tools/`
2. Follow template structure above
3. Test thoroughly
4. Add documentation to this README
5. Update `RECOMMENDATIONS.md` if applicable
6. Submit pull request

---

## Related Documentation

- `renders/_metadata/DEVELOPER_GUIDE.md` - Complete developer guide
- `renders/_metadata/RECOMMENDATIONS.md` - Future enhancements
- `renders/README.md` - Renders overview
- `.github/workflows/validate-renders.yml` - CI/CD workflow

---

**Maintained By**: Implementation Agent  
**Review Frequency**: Monthly or as tools are added  
**Version**: 1.0.0
