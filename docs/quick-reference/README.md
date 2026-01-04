# Quick Reference Cards

> **Purpose**: Printable cheat sheets for daily work  
> **Audience**: All contributors and developers  
> **Format**: Single-page reference cards

## Available Cheatsheets

### [AKU-FORMAT-CHEATSHEET.md](AKU-FORMAT-CHEATSHEET.md)
**Essential AKU structure and fields**

**Use when**:
- Creating new AKUs
- Checking required fields
- Looking up content structure by type
- Verifying cross-domain reference format

**Contains**:
- Complete AKU structure template
- Content examples for all 6 types
- Cross-domain reference patterns
- Domain path hierarchy
- Validation commands
- Quick creation checklist

**Print tip**: Single-sided, keep at desk

---

### [VALIDATION-COMMANDS-CHEATSHEET.md](VALIDATION-COMMANDS-CHEATSHEET.md)
**Common validation and testing commands**

**Use when**:
- Validating AKUs before commit
- Running quality checks
- Searching for files
- Troubleshooting issues

**Contains**:
- AKU validation (single, directory, domain)
- Cross-domain validation
- Agent and structure checks
- File and Git commands
- Search patterns (find, grep)
- Python validation snippets
- Common workflows

**Print tip**: Double-sided, reference frequently

---

### [GIT-WORKFLOW-CHEATSHEET.md](GIT-WORKFLOW-CHEATSHEET.md)
**Git commands and workflows for WorldSMEGraphs**

**Use when**:
- Checking what changed
- Viewing history
- Reverting mistakes
- Finding commits
- Working with branches

**Contains**:
- ⚠️ Critical rule (use report_progress, not git commit)
- Status and diff commands
- History viewing
- Reverting changes
- Finding and comparing
- Stashing
- Common workflows
- Troubleshooting

**Print tip**: Keep with other Git reference materials

---

## Printing Tips

### Recommended Setup
- **Paper**: Letter (8.5" × 11") or A4
- **Orientation**: Portrait
- **Font Size**: Default (small enough to fit, large enough to read)
- **Colors**: Black & white works fine
- **Margins**: Narrow (0.5")

### Print Commands

**From Markdown** (using pandoc):
```bash
# Install pandoc if needed
sudo apt-get install pandoc

# Convert to PDF
pandoc AKU-FORMAT-CHEATSHEET.md -o AKU-FORMAT-CHEATSHEET.pdf

# Or all at once
for f in *.md; do
  pandoc "$f" -o "${f%.md}.pdf"
done
```

**From Browser**:
1. Open .md file in GitHub
2. Click "Display the source diff"
3. Print to PDF
4. Or use browser print (Ctrl+P / Cmd+P)

### Lamination
For frequently referenced cards, consider laminating:
- Makes them spill-proof
- Lasts longer
- Can write on with dry-erase marker
- Wipes clean

---

## Usage Patterns

### Quick Lookup
Keep printed cheatsheets at your desk for fast reference without leaving your editor.

### Team Onboarding
Print sets for new team members as part of onboarding package.

### Code Reviews
Reference during code reviews to verify standards compliance.

### Pair Programming
Keep visible for both participants to reference.

---

## Digital Usage

### As Sidebar
Open in split screen while coding:
- Left: Your editor with AKU
- Right: Cheatsheet for reference

### As Quick Tab
Keep in browser tab for fast Cmd+Tab / Alt+Tab access.

### In Terminal
```bash
# View in terminal
cat docs/quick-reference/AKU-FORMAT-CHEATSHEET.md | less

# Search within
grep "cross_domain" docs/quick-reference/*.md
```

---

## Contributing

### Adding New Cheatsheets

Follow this template:

```markdown
# [Topic] Cheat Sheet

> **Quick Reference**: [Brief description]  
> **[Context]**: [When to use]

## [Section 1]

[Content]

## [Section 2]

[Content]

---

**Full Documentation**: [Link to detailed guide]  
**Last Updated**: YYYY-MM-DD
```

### Guidelines

**DO**:
- Keep it concise (1-2 pages when printed)
- Use clear section headers
- Include copy-paste ready commands
- Provide real examples
- Link to full documentation
- Update timestamp

**DON'T**:
- Duplicate full documentation
- Include long explanations
- Use tiny fonts
- Omit examples
- Forget cross-links

---

## Related Documentation

**Full Guides** (for deep dives):
- [CONTENT-CREATION-GUIDE.md](../CONTENT-CREATION-GUIDE.md)
- [VISUALIZATION-STYLE-GUIDE.md](../VISUALIZATION-STYLE-GUIDE.md)
- [MULTILINGUAL-CONTENT-GUIDE.md](../MULTILINGUAL-CONTENT-GUIDE.md)
- [API-DOCUMENTATION-GUIDE.md](../API-DOCUMENTATION-GUIDE.md)

**Tools Documentation**:
- [domain/_ontology/TOOLS-DOCUMENTATION.md](../../domain/_ontology/TOOLS-DOCUMENTATION.md)
- [domain/_ontology/FAQ.md](../../domain/_ontology/FAQ.md)

**Tutorials**:
- [tutorials/PYTHON-AKU-TUTORIAL.md](../tutorials/PYTHON-AKU-TUTORIAL.md)

---

**Last Updated**: 2026-01-04  
**Maintained By**: Documentation Team
