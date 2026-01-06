# Renders Developer Guide

**Last Updated**: 2026-01-06  
**For**: Content creators, developers, and contributors  
**Status**: Active

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Directory Structure](#directory-structure)
3. [Creating New Renders](#creating-new-renders)
4. [File Naming Conventions](#file-naming-conventions)
5. [Metadata Standards](#metadata-standards)
6. [Audience Profiles](#audience-profiles)
7. [Quality Standards](#quality-standards)
8. [Tools and Automation](#tools-and-automation)
9. [CI/CD Integration](#cicd-integration)
10. [Troubleshooting](#troubleshooting)

---

## Quick Start

### 1. Understand the Structure

Rendered content is centralized in the `renders/` directory, organized primarily **by-domain** to maintain clear connection to source AKUs (Atomic Knowledge Units).

**Path Pattern**: `renders/by-domain/[domain-path]/[language]/[filename]`

**Example**: 
```
renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/adult-limited-reading.md
```

### 2. Before Creating a Render

✅ **DO**:
- Ensure source AKUs exist in `domain/` hierarchy
- Review audience profiles in `renders/_metadata/audience-profiles.yaml`
- Check existing renders for style consistency
- Plan content structure before writing

❌ **DON'T**:
- Create renders in `domain/` hierarchy (old structure)
- Use arbitrary audience names not in profiles
- Duplicate content across languages without coordination
- Forget to update render index after changes

---

## Directory Structure

```
renders/
├── README.md                           # Overview documentation
├── _metadata/                          # Metadata and tools
│   ├── migration-log.md               # Migration history
│   ├── RECOMMENDATIONS.md             # Future enhancements
│   ├── VALIDATION_REPORT.md           # Migration validation
│   ├── audience-profiles.yaml         # Audience definitions
│   ├── render-index.yaml              # Auto-generated index
│   ├── DEVELOPER_GUIDE.md             # This file
│   └── tools/                         # Automation tools
│       └── generate_render_index.py   # Index generator
│
├── by-domain/                         # PRIMARY: Organized by source domain
│   ├── formal-sciences/
│   │   └── mathematics/
│   │       └── pure-mathematics/
│   │           └── algebra/
│   │               ├── english/
│   │               │   ├── elementary-school.md
│   │               │   └── graduate.md
│   │               └── german/
│   │                   └── gymnasium.md
│   ├── natural-sciences/
│   ├── social-sciences/
│   └── health-sciences/
│
├── by-language/                       # FUTURE: Language-organized view
└── by-audience/                       # FUTURE: Audience-organized view
```

---

## Creating New Renders

### Step-by-Step Process

#### 1. Identify Source Content

```bash
# Find the domain and AKUs
ls domain/natural-sciences/physics/quantum-mechanics/planck-units/
# Should see: knowledge.graph, schema.json, akus/, etc.
```

#### 2. Choose Target Audience

Review `renders/_metadata/audience-profiles.yaml` and select:
- `preschool` (ages 3-5)
- `elementary-school` (grades 1-5)
- `middle-school` (grades 6-8)
- `high-school` (grades 9-12)
- `undergraduate` (college)
- `graduate` (graduate/professional)
- `adult-limited-reading` (adults, 6-8th grade reading level)
- `professional` (expert practitioners)

#### 3. Determine Language

Standard language codes:
- `english` (or `english-us`, `english-uk` for specificity)
- `german`
- `french`
- `spanish`
- etc.

#### 4. Create Directory Structure

```bash
# Pattern: renders/by-domain/[domain-path]/[language]/
mkdir -p renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english
```

#### 5. Create Content File

**Naming Convention**:
- Use audience profile name or descriptive purpose
- Use kebab-case (lowercase with hyphens)
- Include file extension

**Examples**:
- `elementary-school.md`
- `adult-limited-reading.md`
- `graduate-technical-reference.md`
- `quick-reference-card.pdf`

```bash
# Create file
touch renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
```

#### 6. Write Content

Follow audience profile guidelines:
- Reading level
- Vocabulary constraints
- Sentence length
- Concept density
- Visual aid requirements

**Example Template**:

```markdown
# Planck Units - Elementary School Level

> **For**: Grades 1-5 (ages 6-11)  
> **Reading Level**: 3rd-4th grade  
> **Time**: 15 minutes

## What Are Planck Units?

Imagine the tiniest things you can think of. Maybe a grain of sand? A speck of dust? Well, scientists have discovered units of measurement that are even tinier than that!

[... continue with appropriate content ...]

## Learn More

Want to know more? Ask your teacher about atoms and how small things can be!

---

**Source**: Based on AKUs from domain/natural-sciences/physics/quantum-mechanics/planck-units/
**Last Updated**: 2026-01-06
```

#### 7. Regenerate Index

```bash
# Update render index
python renders/_metadata/tools/generate_render_index.py
```

#### 8. Commit Changes

```bash
git add renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/english/elementary-school.md
git add renders/_metadata/render-index.yaml
git commit -m "Add elementary school render for Planck units"
```

---

## File Naming Conventions

### Filename Format

**Pattern**: `[audience-or-purpose].[extension]`

**Good**:
- `elementary-school.md`
- `graduate-research-guide.md`
- `quick-reference.pdf`
- `visual-guide.md`
- `comprehensive-textbook-chapter.md`

**Bad**:
- `ES.md` (unclear abbreviation)
- `version2.md` (no context)
- `file.md` (generic)
- `MyDocument.md` (wrong case)

### Extension Guidelines

- `.md` - Markdown (primary format)
- `.pdf` - PDF documents
- `.pptx` - PowerPoint presentations
- `.html` - HTML pages
- `.tex` - LaTeX source
- `.png`, `.jpg` - Images (in subdirectories)
- `.json` - Metadata files

### Special Files

- `README.md` - Domain-specific documentation
- `INDEX.md` - Table of contents for multiple renders
- `NOTES.md` - Development notes
- `metadata.json` or `metadata.yaml` - Render metadata

---

## Metadata Standards

### Optional Metadata File

For complex renders, create accompanying metadata:

**Format**: `[filename].metadata.yaml`

**Example**: `elementary-school.md.metadata.yaml`

```yaml
render:
  id: "render-physics-planck-elementary"
  title: "The Tiniest Things - Planck Units for Kids"
  created: "2026-01-06T10:00:00Z"
  updated: "2026-01-06T15:30:00Z"
  version: "1.0.0"
  
source:
  domain: "natural-sciences/physics/quantum-mechanics/planck-units"
  aku_ids:
    - "aku-planck-length-001"
    - "aku-planck-time-002"
  graph_version: "2.1.0"
  
target:
  language: "english"
  language_variant: "us"
  audience: "elementary-school"
  reading_level: 3.5  # Flesch-Kincaid grade level
  estimated_reading_time_minutes: 15
  
quality:
  word_count: 847
  readability_flesch_kincaid: 3.5
  readability_flesch_reading_ease: 85.2
  accessibility_wcag: "AA"
  peer_reviewed: true
  last_reviewed: "2026-01-06"
  reviewed_by: ["pedagogy-agent", "accessibility-agent"]
  
contributors:
  - name: "Pedagogy Agent"
    role: "primary_author"
  - name: "Accessibility Agent"
    role: "reviewer"
    
notes: |
  Simplified quantum mechanics concepts for young learners.
  Uses concrete analogies to everyday objects.
  All technical terms are defined inline.
```

---

## Audience Profiles

See `renders/_metadata/audience-profiles.yaml` for complete definitions.

### Quick Reference

| Profile | Ages | Reading Level | Vocabulary | Sentence Length |
|---------|------|---------------|------------|-----------------|
| Preschool | 3-5 | Pre-reading | 500-1000 | 3-5 words |
| Elementary | 6-11 | 1st-5th grade | 2000-5000 | 8-15 words |
| Middle School | 11-14 | 6th-8th grade | 5000-8000 | 12-20 words |
| High School | 14-18 | 9th-12th grade | 8000-15000 | 15-25 words |
| Undergraduate | 18-22 | College | 15000-25000 | 20-30 words |
| Graduate | 22+ | Graduate | Unlimited | No limit |
| Adult Limited | 18+ | 6th-8th grade | 5000-8000 | 12-18 words |
| Professional | 25+ | Professional | Field-specific | Efficient |

---

## Quality Standards

### Content Quality Checklist

- [ ] Accurate information (verified against source AKUs)
- [ ] Appropriate for target audience
- [ ] Clear, concise writing
- [ ] Proper grammar and spelling
- [ ] Technical terms defined when first used
- [ ] Consistent terminology
- [ ] Proper citations (if applicable)
- [ ] Cultural sensitivity

### Accessibility Checklist (WCAG 2.1 AA)

- [ ] Alternative text for all images
- [ ] Proper heading hierarchy (H1, H2, H3...)
- [ ] Sufficient color contrast (if using colors)
- [ ] Meaningful link text (avoid "click here")
- [ ] Keyboard navigable (for digital content)
- [ ] Screen reader compatible
- [ ] Captions for videos
- [ ] Transcripts for audio

### Readability Targets

**By Audience**:
- Elementary: Flesch-Kincaid 2-5, Flesch Reading Ease 80-90
- Middle School: FK 6-8, FRE 70-80
- High School: FK 9-12, FRE 60-70
- Undergraduate: FK 13-16, FRE 50-60
- Graduate: FK 16+, FRE 30-50
- Adult Limited: FK 6-8, FRE 70-80

**Tools**:
- Online: https://readable.com/, https://hemingwayapp.com/
- CLI: `textstat` Python library
- VS Code Extension: "Readability Check"

---

## Tools and Automation

### Available Tools

#### 1. Render Index Generator

**Location**: `renders/_metadata/tools/generate_render_index.py`

**Purpose**: Scans renders/ and generates render-index.yaml

**Usage**:
```bash
python renders/_metadata/tools/generate_render_index.py
```

**Output**: `renders/_metadata/render-index.yaml` (auto-generated, commit to repo)

#### 2. Future Tools (Planned)

See `renders/_metadata/RECOMMENDATIONS.md` for roadmap:
- AKU usage matrix generator
- Render quality linter
- Readability checker
- Accessibility validator
- Translation status tracker

### Creating Custom Tools

Place tools in `renders/_metadata/tools/`:

```python
#!/usr/bin/env python3
"""
My Custom Tool

Description of what it does.
"""

import os
import yaml

def my_tool_function():
    # Implementation
    pass

if __name__ == "__main__":
    my_tool_function()
```

Make executable:
```bash
chmod +x renders/_metadata/tools/my_tool.py
```

---

## CI/CD Integration

### Automated Validation

**Workflow**: `.github/workflows/validate-renders.yml`

**Runs On**:
- Push to `renders/**`
- Push to `domain/**/*.graph`
- Pull requests
- Manual trigger

**Checks**:
1. Directory structure integrity
2. No legacy `.renders/` directories in `domain/`
3. Render index up-to-date
4. No orphaned renders
5. Documentation references updated

### Manual Trigger

```bash
# Via GitHub CLI
gh workflow run validate-renders.yml

# Via GitHub UI
Actions tab → "Validate Renders" → "Run workflow"
```

---

## Troubleshooting

### Common Issues

#### Issue: "Can't find source AKUs"

**Solution**: Ensure AKUs exist in `domain/` first. Check path matches exactly.

```bash
ls -la domain/natural-sciences/physics/quantum-mechanics/planck-units/
```

#### Issue: "Render index out of sync"

**Solution**: Regenerate index:

```bash
python renders/_metadata/tools/generate_render_index.py
git add renders/_metadata/render-index.yaml
git commit -m "Update render index"
```

#### Issue: "Wrong directory structure"

**Wrong**: `domain/natural-sciences/physics/.renders/...`  
**Right**: `renders/by-domain/natural-sciences/physics/...`

#### Issue: "Readability score too high"

**Solution**:
- Shorten sentences
- Use simpler words
- Break long paragraphs
- Add more examples
- Remove unnecessary jargon

**Tools**: Hemingway Editor, Readable.com

#### Issue: "Accessibility warnings"

**Common Fixes**:
- Add alt text: `![Description](image.png)` not `![](image.png)`
- Fix heading order: Don't skip levels (H1 → H3)
- Improve link text: "View tutorial" not "click here"
- Add table headers: Use `| Header |` in first row

---

## Best Practices

### DO ✅

- Keep renders focused on single topic or concept
- Use consistent terminology across all renders
- Reference source AKUs in content
- Include creation/update dates
- Test content with target audience when possible
- Proofread before committing
- Update render index after changes
- Follow audience profile guidelines strictly

### DON'T ❌

- Copy-paste without adapting for audience
- Use copyrighted content without attribution
- Create renders without source AKUs
- Ignore accessibility requirements
- Use ambiguous filenames
- Mix multiple audiences in one render
- Forget to update documentation

---

## Getting Help

### Resources

1. **Audience Profiles**: `renders/_metadata/audience-profiles.yaml`
2. **Recommendations**: `renders/_metadata/RECOMMENDATIONS.md`
3. **Validation Report**: `renders/_metadata/VALIDATION_REPORT.md`
4. **Main README**: `renders/README.md`
5. **Rendering Spec**: `.project/rendering-spec.md`

### Ask For Help

- Create GitHub issue with `[renders]` tag
- Consult with @pedagogy-agent for education questions
- Consult with @accessibility-agent for accessibility
- Consult with @rendering-agent for technical questions

---

## Contributing

See `docs/CONTRIBUTING.md` for general contribution guidelines.

**Render-Specific**:
1. Fork repository
2. Create renders in `renders/by-domain/`
3. Follow this guide
4. Regenerate index
5. Submit pull request
6. Address review feedback

---

**Document Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**Maintained By**: Rendering Agent, Pedagogy Agent  
**Next Review**: 2026-02-06
