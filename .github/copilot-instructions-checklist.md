# Copilot Instructions Quality Checklist

> **Purpose**: Ensure copilot-instructions.md meets all quality standards and best practices

## Usage

Run this checklist periodically to verify the copilot-instructions.md file remains comprehensive and up-to-date.

**Recommended Frequency**: Monthly or after significant project changes

## Core Requirements ✓

- [ ] File exists at `.github/copilot-instructions.md`
- [ ] File is readable (no permission issues)
- [ ] File size is reasonable (not empty, not excessively large)
- [ ] Clear project description present
- [ ] Technical stack documented
- [ ] File organization explained
- [ ] Build instructions provided
- [ ] Test instructions provided
- [ ] Coding standards documented

## Content Quality ✓

- [ ] Table of contents present
- [ ] Clear section headers (proper hierarchy)
- [ ] Code examples included
- [ ] Good vs bad patterns shown
- [ ] Common pitfalls documented
- [ ] Troubleshooting guide included
- [ ] Quick reference section available
- [ ] All sections have actual content (no placeholders)

## Project-Specific Elements ✓

- [ ] Custom agents documented
- [ ] Agent invocation patterns explained
- [ ] Validation tools documented
- [ ] Workflow requirements clear
- [ ] Contributing guidelines linked
- [ ] Related documentation linked
- [ ] Project-specific terminology explained

## Maintenance Quality ✓

- [ ] Last updated date present and recent
- [ ] Version number noted
- [ ] All links verified and working
- [ ] No unresolved TODOs or FIXMEs
- [ ] File organization matches reality
- [ ] Cross-references are accurate

## Technical Verification ✓

### Run These Commands:

```bash
# 1. Check file exists
test -f .github/copilot-instructions.md && echo "✅ File exists" || echo "❌ File missing"

# 2. Check line count (should be substantial)
wc -l .github/copilot-instructions.md

# 3. Verify no syntax errors (basic Markdown check)
grep -c "^#" .github/copilot-instructions.md

# 4. Check for broken internal links
grep -o '\[.*\](.*.md)' .github/copilot-instructions.md | sed 's/.*(\(.*\))/\1/' | while read file; do
  if [ ! -f "$file" ] && [ ! -f ".github/$file" ]; then
    echo "❌ Broken link: $file"
  fi
done

# 5. Verify validation scripts mentioned work
bash .github/copilot/agents/check-agent-lengths.sh > /dev/null 2>&1 && echo "✅ Agent validator works"
bash .github/scripts/validate-structure.sh > /dev/null 2>&1 && echo "✅ Structure validator works"
```

## Content Accuracy ✓

- [ ] Agent names match actual agent files
- [ ] File paths are correct
- [ ] Command examples have been tested
- [ ] Version numbers match other documentation
- [ ] Statistics are current (agent counts, etc.)

## Completeness ✓

### Must Cover:

- [ ] Project mission and goals
- [ ] Core principles and values
- [ ] Development setup
- [ ] Build process
- [ ] Testing approach
- [ ] Code style guidelines
- [ ] Common workflows
- [ ] Troubleshooting steps
- [ ] Where to find more help

## Usability ✓

- [ ] New contributors can understand it
- [ ] Clear navigation (TOC or similar)
- [ ] Examples are practical and useful
- [ ] Language is clear and accessible
- [ ] No jargon without explanation
- [ ] Formatting enhances readability

## GitHub Copilot Compatibility ✓

- [ ] Located in standard location
- [ ] Format is Markdown
- [ ] Provides clear context about project
- [ ] Explains how to invoke custom agents
- [ ] Documents validation and testing
- [ ] Includes examples of expected patterns

## Update Triggers

Review and update copilot-instructions.md when:

- [ ] Major project structure changes
- [ ] New validation tools added
- [ ] Agent ecosystem changes significantly
- [ ] Technology stack updates
- [ ] Workflow changes
- [ ] Common issues emerge
- [ ] Best practices evolve

## Review History

| Date | Reviewer | Status | Issues Found | Notes |
|------|----------|--------|--------------|-------|
| 2025-12-27 | Copilot Agent | ✅ Pass | 0 | Initial comprehensive setup |
| | | | | |

---

**Last Updated**: 2025-12-27  
**Version**: 1.0  
**Next Review Due**: 2026-01-27
