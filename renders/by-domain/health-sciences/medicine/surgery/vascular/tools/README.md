# Vascular Surgery Render Tools

This directory contains utility scripts for managing vascular surgery educational content.

## Available Tools

### 1. `generate_viewing_files.py`

**Purpose**: Automatically generate three viewing format markdown files for comic directories.

**Features** (v1.1 - Updated 2026-01-09):
- Scans for comic directories with `panels-gpt/` folders
- Extracts panel images (deduplicates automatically)
- **NEW**: Handles broken panel numbering (all `image_001_*`) using timestamp ordering
- Reads `storyboard.json` for dialogue/captions when available
- Generates three viewing formats

**Usage**:
```bash
python3 tools/generate_viewing_files.py
```

**What it does**:
- Scans for comic directories with `panels-gpt/` folders
- Extracts panel images (deduplicates automatically)
- Reads `storyboard.json` for dialogue/captions when available
- Generates three viewing formats:
  - `6-panel-grid-view.md` - 2×3 grid layout
  - `continuous-story-view.md` - Sequential with dialogue
  - `pictures-only-view.md` - Pure visual

**Requirements**:
- Python 3.6+
- Standard library only (no external dependencies)

**Example output**:
```
Processing pathology/carotid-artery-stenosis/english/carotid-artery-stenosis/comic (8 panels)...
  Created: 6-panel-grid-view.md
  Created: continuous-story-view.md
  Created: pictures-only-view.md
```

### 2. `validate_structure.py` (in parent directory)

**Purpose**: Validate the render structure integrity.

**Usage**:
```bash
python3 validate_structure.py
```

**What it checks**:
- Directory structure matches ontology (procedures/pathology/complications)
- All comics have required viewing files
- Image references in viewing files are valid
- No misplaced comics

**Exit codes**:
- `0` - All validations passed
- `1` - Issues found

## Workflow for Adding New Comics

### Step 1: Create Comic Structure
```bash
mkdir -p pathology/[topic]/english/[comic-name]/comic/panels-gpt/
# or
mkdir -p procedures/[procedure]/english/[comic-name]/comic/panels-gpt/
```

### Step 2: Add Images
Place your panel images in `panels-gpt/`:
```
image_001_[timestamp]_[hash].png
image_002_[timestamp]_[hash].png
...
```

### Step 3: (Optional) Add Storyboard
Create `storyboard.json` with panel metadata:
```json
{
  "panels": [
    {
      "panel": 1,
      "dialogue": "Panel 1 dialogue",
      "caption": "Panel 1 caption"
    }
  ]
}
```

### Step 4: Generate Viewing Files
```bash
cd /path/to/vascular/
python3 tools/generate_viewing_files.py
```

### Step 5: Validate
```bash
python3 validate_structure.py
```

### Step 6: Update Navigation
Add links to `INDEX.md`

## Future Tools (Planned)

- **`generate_pdf.py`** - Create PDF compilations from comics
- **`generate_html.py`** - Create interactive HTML viewers
- **`translate_comics.py`** - Generate multi-language versions
- **`extract_learning_objectives.py`** - Parse README files for objectives
- **`generate_quiz.py`** - Create assessment questions from comics

## Contributing

To add new tools:

1. **Follow naming convention**: `[verb]_[noun].py`
2. **Use standard library**: No external dependencies preferred
3. **Add documentation**: Update this README
4. **Include usage examples**: Show how to run the tool
5. **Test thoroughly**: Validate with existing comics

## Maintenance

### Regular Tasks

**Weekly**:
- Run `validate_structure.py` to check integrity
- Review new comics for viewing files

**After adding content**:
- Run `generate_viewing_files.py` for new comics
- Validate with `validate_structure.py`
- Update `INDEX.md`

**Monthly**:
- Review tool performance
- Update scripts for new requirements
- Archive old tools if superseded

## Troubleshooting

### generate_viewing_files.py issues

**No comics found**:
- Check that `panels-gpt/` directory exists
- Verify images follow naming pattern: `image_NNN_*.png`

**Broken image links**:
- Ensure relative paths are correct
- Check image files exist in `panels-gpt/`

**All panels show as "Panel 1"**:
- This occurs when all images have `image_001_*` prefix (broken numbering)
- The tool now automatically uses timestamp ordering as fallback
- Look for message: "Note: All images numbered as panel 1, using timestamp order"
- To fix permanently, regenerate images with proper `--output image_XX` parameter

**Missing dialogue**:
- Add `storyboard.json` if you want dialogue in continuous view
- Script works fine without storyboard (pictures only)

### validate_structure.py issues

**Directory structure errors**:
- Check that comics are in procedures/pathology/complications
- Verify no comics directly under vascular/

**Missing viewing files**:
- Run `generate_viewing_files.py` to create them

**Broken image references**:
- Check that image files haven't been moved
- Regenerate viewing files if needed

## Support

For issues or questions:
1. Check this README first
2. Review the script source code (well-commented)
3. Check `REFACTORING-SUMMARY.md` for structure details
4. Create an issue in the repository

---

**Last Updated**: 2026-01-09  
**Maintainer**: GitHub Copilot  
**License**: Part of WorldSMEGraphs project
