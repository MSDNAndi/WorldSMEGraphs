# Documentation Maintenance Checklist

> **Purpose**: Monthly/quarterly documentation review checklist  
> **Audience**: Maintainers, documentation team  
> **Frequency**: Review monthly, deep dive quarterly

## Monthly Review Checklist

### 1. Accuracy Check

- [ ] Review all statistical numbers in PROJECT-STATISTICS.md
- [ ] Update AKU counts per domain
- [ ] Verify validation success rates
- [ ] Update agent count if changed
- [ ] Check migration statistics current

### 2. Link Validation

- [ ] Check all internal links in docs/
- [ ] Verify cross-references to domain files
- [ ] Test quick-reference links
- [ ] Validate tutorial links
- [ ] Check external ontology URLs

### 3. Timestamp Updates

- [ ] Update "Last Updated" timestamps
- [ ] Check VERSION.md (if exists)
- [ ] Update changelog entries
- [ ] Review date-sensitive content
- [ ] Update project statistics dates

### 4. Content Freshness

- [ ] Review for outdated information
- [ ] Check if new features documented
- [ ] Update command examples if tools changed
- [ ] Verify file paths still accurate
- [ ] Check if new domains added

### 5. Consistency Check

- [ ] Verify consistent terminology
- [ ] Check formatting consistency
- [ ] Validate style guide compliance
- [ ] Review tone and voice
- [ ] Check capitalization standards

---

## Quarterly Deep Dive

### 1. Comprehensive Review

#### Documentation Completeness
- [ ] All new features documented
- [ ] All domains have READMEs
- [ ] All tools have documentation
- [ ] All agents have descriptions
- [ ] All workflows documented

#### Example Validation
- [ ] Test all code examples
- [ ] Verify command examples work
- [ ] Check Python snippets
- [ ] Validate bash commands
- [ ] Test API examples

#### Screenshot/Diagram Updates
- [ ] Review all diagrams for accuracy
- [ ] Update screenshots if UI changed
- [ ] Check ASCII art displays correctly
- [ ] Verify visualization examples
- [ ] Update flowcharts if process changed

### 2. User Feedback Integration

- [ ] Review GitHub issues for documentation requests
- [ ] Check discussion forums for questions
- [ ] Analyze most-asked questions
- [ ] Identify documentation gaps
- [ ] Plan improvements

### 3. Competitive Analysis

- [ ] Review similar projects' documentation
- [ ] Identify best practices to adopt
- [ ] Note innovative presentation methods
- [ ] Benchmark against industry standards
- [ ] Plan enhancements

### 4. Accessibility Audit

- [ ] Check WCAG compliance
- [ ] Verify screen reader compatibility
- [ ] Test keyboard navigation
- [ ] Check color contrast ratios
- [ ] Validate alt text present

### 5. Internationalization Review

- [ ] Check if new content needs translation
- [ ] Verify translation accuracy
- [ ] Update multilingual glossaries
- [ ] Check RTL language support
- [ ] Validate CJK character rendering

---

## Specific Document Checks

### Content Creation Guide
- [ ] All 6 AKU types still current
- [ ] Audience levels still relevant
- [ ] Examples still accurate
- [ ] Quality standards current
- [ ] Workflow still valid

### API Documentation
- [ ] Schema matches implementation
- [ ] Endpoints still accurate
- [ ] Error codes current
- [ ] Rate limits correct
- [ ] Examples work

### Visualization Style Guide
- [ ] Color palette still used
- [ ] Typography standards current
- [ ] Tool recommendations valid
- [ ] WCAG guidelines current
- [ ] Examples still relevant

### Multilingual Content Guide
- [ ] Languages list current
- [ ] Translation tools still relevant
- [ ] Workflow still efficient
- [ ] Examples culturally appropriate
- [ ] Quality levels accurate

### Quick Reference Cheatsheets
- [ ] Commands still work
- [ ] Paths still accurate
- [ ] Examples current
- [ ] Tools still used
- [ ] Workflow patterns valid

---

## Automation Opportunities

### Scripts to Create

```bash
# Link checker script
#!/bin/bash
# Check all markdown links
find docs -name "*.md" -exec grep -oP '\[.*?\]\(\K[^)]+' {} \; | \
  while read link; do
    [[ -f "$link" ]] || echo "Broken: $link"
  done
```

```bash
# Timestamp updater
#!/bin/bash
# Update "Last Updated" to current date
current_date=$(date -u +"%Y-%m-%d")
find docs -name "*.md" -exec sed -i \
  "s/Last Updated.*$/Last Updated: $current_date/" {} \;
```

```python
# Statistics updater
import glob, json
from collections import Counter

# Count AKUs by type
types = Counter()
for f in glob.glob("domain/**/*.json", recursive=True):
    if "schema.json" not in f:
        with open(f) as fp:
            aku = json.load(fp)
            if aku.get('@context') == 'aku-v2':
                types[aku.get('@type')] += 1

print(f"Total AKUs: {sum(types.values())}")
print(f"By type: {dict(types)}")
```

### Automated Checks

- [ ] Set up monthly cron job for link checking
- [ ] Automated statistics generation
- [ ] Spell check CI/CD integration
- [ ] Link validation in PR checks
- [ ] Documentation coverage reports

---

## Issue Tracking

### Documentation Issues Template

```markdown
**Issue Type**: Documentation
**Affected File**: path/to/file.md
**Section**: Section name
**Problem**: [Describe issue]
**Proposed Fix**: [Suggestion]
**Priority**: High/Medium/Low
```

### Common Issue Types

1. **Outdated Information**
   - Statistics no longer accurate
   - Commands changed
   - Paths modified
   - Tools deprecated

2. **Broken Links**
   - Internal links to moved files
   - External links to dead URLs
   - Anchor links to removed sections

3. **Missing Content**
   - New features undocumented
   - Gaps in coverage
   - Insufficient examples
   - Missing cross-references

4. **Clarity Issues**
   - Confusing explanations
   - Missing context
   - Jargon without definitions
   - Poor examples

5. **Formatting Problems**
   - Inconsistent style
   - Broken markdown
   - Display issues
   - Accessibility problems

---

## Priority System

### High Priority
- Security documentation
- Breaking changes
- Broken links in README
- Installation instructions
- Getting started guides

### Medium Priority
- Feature documentation
- Tutorial updates
- API reference accuracy
- Example freshness
- Cross-reference completion

### Low Priority
- Style improvements
- Minor clarifications
- Additional examples
- Enhanced diagrams
- Translation updates

---

## Success Metrics

### Documentation Health

**Target Metrics**:
- Link validity: 100%
- Freshness: < 3 months old
- Completeness: 95%+
- User satisfaction: > 4/5
- Issue resolution: < 1 week

**How to Measure**:
- Automated link checking
- Last-modified timestamps
- Coverage analysis
- User surveys
- Issue tracking

### Continuous Improvement

**Track**:
- Issues opened per month
- Issues closed per month
- Time to close documentation issues
- User feedback scores
- Documentation usage analytics

**Review Quarterly**:
- Trends in documentation issues
- Most-visited pages
- Search queries
- Feedback themes
- Improvement opportunities

---

## Tools and Resources

### Link Checkers
- [markdown-link-check](https://github.com/tcort/markdown-link-check)
- [linkchecker](https://github.com/linkchecker/linkchecker)
- [awesome_bot](https://github.com/dkhamsing/awesome_bot)

### Spell Checkers
- [aspell](http://aspell.net/)
- [hunspell](https://hunspell.github.io/)
- [codespell](https://github.com/codespell-project/codespell)

### Markdown Linters
- [markdownlint](https://github.com/DavidAnson/markdownlint)
- [remark-lint](https://github.com/remarkjs/remark-lint)

### Documentation Generators
- [pandoc](https://pandoc.org/) - Format conversion
- [mkdocs](https://www.mkdocs.org/) - Static site
- [docsify](https://docsify.js.org/) - Dynamic docs

---

## Contact

**Documentation Maintainers**: See CONTRIBUTING.md  
**Questions**: Open an issue with "docs:" prefix  
**Suggestions**: Submit PR with documentation improvements

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Next Review**: 2026-02-04
