# Renders - By Domain Organization

This directory contains rendered content organized by source domain, maintaining the hierarchy from the `domain/` directory structure.

## Purpose

The `by-domain/` organization is the **primary** organizational structure for renders, chosen because:

1. **Clear Source Tracing**: Easy to find renders related to specific AKUs
2. **Domain Coherence**: Keeps related content together
3. **Maintenance**: Updates to source AKUs can quickly identify affected renders
4. **Discovery**: Natural navigation from domain knowledge to its renders

## Structure

```
by-domain/
├── formal-sciences/           # Mathematics, Computer Science, Logic
│   ├── mathematics/
│   │   └── pure-mathematics/
│   │       ├── category-theory/
│   │       ├── geometry/
│   │       └── number-theory/
│   └── computer-science/
│       └── programming-paradigms/
│           └── functional-programming/
│
├── natural-sciences/          # Physics, Chemistry, Biology
│   └── physics/
│       └── quantum-mechanics/
│           └── planck-units/
│
├── social-sciences/           # Economics, Psychology, Sociology
│   └── economics/
│       └── bwl/
│
└── health-sciences/           # Medicine, Nursing, Pharmacy
    └── medicine/
        └── surgery/
            └── vascular/
```

## Path Format

**Pattern**: `by-domain/[domain-path]/[language]/[filename]`

**Example**: 
```
by-domain/
  natural-sciences/
    physics/
      quantum-mechanics/
        planck-units/
          english/
            adult-limited-reading.md
            elementary-school.md
            undergraduate.md
          german/
            erwachsene-eingeschraenktes-lesen.md
```

## Relationship to Source Domain

Each path in `renders/by-domain/` mirrors a path in `domain/`:

- **Domain AKUs**: `domain/natural-sciences/physics/quantum-mechanics/planck-units/akus/`
- **Rendered Content**: `renders/by-domain/natural-sciences/physics/quantum-mechanics/planck-units/`

This correspondence makes it easy to:
- Find renders for specific AKUs
- Identify which renders need updates when AKUs change
- Maintain consistency between source and rendered content

## Language Organization

Within each domain path, content is organized by language:

- `english/` - English language renders
- `german/` - German language renders
- `french/` - French language renders
- etc.

This allows:
- Easy translation workflows
- Language-specific content adaptations
- Consistent organization across languages

## Audience Levels

File names typically indicate target audience:

- `preschool.md` - Ages 3-5
- `elementary-school.md` - Grades 1-5 (ages 6-11)
- `middle-school.md` - Grades 6-8 (ages 11-14)
- `high-school.md` - Grades 9-12 (ages 14-18)
- `undergraduate.md` - College level
- `graduate.md` - Graduate/professional level
- `adult-limited-reading.md` - Adults with limited reading ability
- `professional.md` - Expert practitioners

See `renders/_metadata/audience-profiles.yaml` for complete definitions.

## Adding New Renders

### Quick Method

Use the helper script:

```bash
bash renders/_metadata/tools/create_render.sh \
  natural-sciences/physics/quantum-mechanics/planck-units \
  english \
  undergraduate
```

### Manual Method

1. **Create directory structure**:
   ```bash
   mkdir -p renders/by-domain/[domain-path]/[language]
   ```

2. **Create render file**:
   ```bash
   touch renders/by-domain/[domain-path]/[language]/[audience].md
   ```

3. **Add content** following audience guidelines

4. **Regenerate indexes**:
   ```bash
   python renders/_metadata/tools/generate_render_index.py
   python renders/_metadata/tools/generate_aku_usage_matrix.py
   ```

5. **Commit**:
   ```bash
   git add renders/
   git commit -m "Add [audience] render for [domain]"
   ```

## Quality Guidelines

All renders should:

- ✅ Match target audience reading level
- ✅ Use appropriate vocabulary
- ✅ Include proper citations to source AKUs
- ✅ Follow accessibility guidelines (WCAG 2.1 AA)
- ✅ Use descriptive filenames
- ✅ Include metadata (YAML frontmatter recommended)

Run quality checks:
```bash
python renders/_metadata/tools/render_quality_linter.py renders/by-domain/[path]/
```

## Finding Renders

### By Domain
Navigate directly:
```bash
ls -R renders/by-domain/natural-sciences/physics/
```

### By Language
Search for language subdirectories:
```bash
find renders/by-domain -type d -name "english"
find renders/by-domain -type d -name "german"
```

### By Audience
Search for audience-specific files:
```bash
find renders/by-domain -name "undergraduate.md"
find renders/by-domain -name "elementary-school.*"
```

### Using the Index
Check the generated index:
```bash
cat renders/_metadata/render-index.yaml
```

## Statistics (Current)

- **Total Renders**: 255 files
- **Languages**: English (249), German (6)
- **Domains**: 4 active (formal, natural, social, health sciences)
- **File Types**: .md, .png, .jpg, .pdf, .pptx, .json

## Alternative Organizations

While `by-domain/` is the primary organization, future enhancements may include:

- **`by-language/`**: All renders grouped by language (for translation workflows)
- **`by-audience/`**: All renders grouped by audience level (for curriculum development)
- **`composite/`**: Multi-domain content that spans multiple domains

These are prepared but not yet populated. See `renders/_metadata/RECOMMENDATIONS.md` for roadmap.

## Tools

Located in `renders/_metadata/tools/`:

1. **create_render.sh** - Interactive render creation
2. **generate_render_index.py** - Catalog all renders
3. **generate_aku_usage_matrix.py** - Track AKU-render relationships
4. **render_quality_linter.py** - Check quality standards

See `renders/_metadata/tools/README.md` for complete documentation.

## Documentation

Complete guides available in `renders/_metadata/`:

- **README.md** - Overview of renders infrastructure
- **DEVELOPER_GUIDE.md** - Comprehensive developer reference (13KB)
- **audience-profiles.yaml** - Audience definitions and guidelines
- **PROJECT_COMPLETION_SUMMARY.md** - Migration details

## Need Help?

- **Quick Start**: See `renders/_metadata/DEVELOPER_GUIDE.md`
- **Quality Standards**: See `renders/_metadata/audience-profiles.yaml`
- **Tools Usage**: See `renders/_metadata/tools/README.md`
- **Recommendations**: See `renders/_metadata/RECOMMENDATIONS.md`

---

**Last Updated**: 2026-01-06  
**Status**: Active, Production Ready  
**Files**: 255 renders across 4 major domains
