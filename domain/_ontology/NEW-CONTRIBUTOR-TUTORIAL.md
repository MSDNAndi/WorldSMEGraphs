# New Contributor Tutorial

> **Purpose**: Step-by-step tutorial for first-time contributors to the WorldSMEGraphs domain hierarchy project.

## Welcome!

Thank you for your interest in contributing to WorldSMEGraphs! This tutorial will guide you through making your first contribution to the domain hierarchy.

**Estimated Time**: 30 minutes

---

## Prerequisites

Before starting, ensure you have:
- [ ] Git installed and configured
- [ ] Python 3.6+ installed
- [ ] Text editor or IDE
- [ ] GitHub account
- [ ] Repository cloned locally

**Clone Command**:
```bash
git clone https://github.com/MSDNAndi/WorldSMEGraphs.git
cd WorldSMEGraphs
```

---

## Tutorial Path

Choose your learning path:

### Path A: Adding Your First AKU
**Best for**: Content contributors, subject matter experts  
**Time**: 20 minutes  
**Skills**: Basic JSON, domain knowledge

### Path B: Improving Documentation
**Best for**: Technical writers, documentarians  
**Time**: 15 minutes  
**Skills**: Markdown

### Path C: Running Validation
**Best for**: QA testers, validators  
**Time**: 10 minutes  
**Skills**: Command line basics

---

## Path A: Adding Your First AKU

### Step 1: Understand the Domain Hierarchy

**Read First**:
- Quick overview: `domain/_ontology/INDEX.md`
- Structure: `.project/structure.md`
- Native domain principle: `domain/_ontology/CROSS-DOMAIN-LINKING-GUIDE.md`

**Key Concept**: Every piece of knowledge belongs to its **native domain** (where it originated), not where it's used.

### Step 2: Choose a Simple Concept

**Good First Concepts**:
- A mathematical definition (algebra, geometry)
- A physics formula (classical mechanics)
- An economic concept (supply/demand)
- A medical term (basic anatomy)

**Example for this tutorial**: We'll create an AKU for "Pythagorean Theorem"

**Native Domain**: `formal-sciences/mathematics/geometry`

### Step 3: Check If It Already Exists

```bash
# Search for existing content
find domain/ -name "*.json" | xargs grep -l "Pythagorean"
```

**If found**: Choose a different concept or improve existing AKU  
**If not found**: Proceed to create new AKU

### Step 4: Create the Directory Structure

```bash
# Create directories if they don't exist
mkdir -p domain/formal-sciences/mathematics/geometry/akus/theorems/
```

### Step 5: Create Your AKU File

**File**: `domain/formal-sciences/mathematics/geometry/akus/theorems/pythagorean-theorem.json`

```json
{
  "@context": "aku-v2",
  "@type": "theorem",
  "@id": "wsmg:formal-sciences/mathematics/geometry/pythagorean-theorem",
  
  "metadata": {
    "version": "1.0.0",
    "created": "2026-01-04T16:00:00.000Z",
    "modified": "2026-01-04T16:00:00.000Z",
    "contributors": ["your-github-username"],
    "confidence": 0.95,
    "status": "draft"
  },
  
  "classification": {
    "domain_path": "formal-sciences/mathematics/geometry",
    "type": "theorem",
    "difficulty": "elementary",
    "importance": "foundational",
    "isNativeDomain": true,
    "isApplicationDomain": false
  },
  
  "content": {
    "primary_statement": {
      "informal": "In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides",
      "formal": "For a right triangle with sides a, b and hypotenuse c: a² + b² = c²"
    },
    "proof_sketch": "Multiple proofs exist, including geometric dissection and algebraic methods",
    "applications": [
      "Distance calculations",
      "Navigation",
      "Computer graphics"
    ]
  },
  
  "cross_domain_applications": {
    "physics": "Vector magnitude calculations",
    "computer_science": "2D/3D distance formulas",
    "engineering": "Structural analysis"
  },
  
  "metadata_extended": {
    "historical_context": "Known to ancient civilizations, formalized by Pythagoras ~500 BCE",
    "difficulty_rationale": "Taught in middle school, fundamental to geometry"
  }
}
```

**Key Points**:
- Replace `your-github-username` with your actual username
- Use current UTC timestamp (run `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"`)
- `isNativeDomain: true` because math is where this originated
- Include cross_domain_applications to show where it's used

### Step 6: Validate Your AKU

```bash
# From repository root
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  domain/formal-sciences/mathematics/geometry/akus/theorems/pythagorean-theorem.json
```

**Expected Output**:
```
✅ pythagorean-theorem.json
  Domain: formal-sciences/mathematics/geometry
  Type: theorem
  Required fields: ✓ All present
  Timestamps: ✓ Valid ISO 8601 format
  Classification: ✓ Valid domain_path
```

**If errors**: Fix them and validate again until you see ✅

### Step 7: Create a Branch and Commit

```bash
# Create feature branch
git checkout -b add-pythagorean-theorem

# Add your file
git add domain/formal-sciences/mathematics/geometry/akus/theorems/pythagorean-theorem.json

# Commit with descriptive message
git commit -m "Add Pythagorean Theorem AKU to mathematics/geometry

- Created new AKU for foundational geometry theorem
- Includes formal/informal statements
- Documents cross-domain applications
- Validated successfully"

# Push to your fork
git push origin add-pythagorean-theorem
```

### Step 8: Create Pull Request

1. Go to GitHub repository
2. Click "Pull Requests" → "New Pull Request"
3. Select your branch
4. Fill in PR template:
   - **Title**: "Add Pythagorean Theorem AKU"
   - **Description**: Explain what you added and why
   - **Validation**: Note that validation passed
5. Submit!

**Congratulations!** 🎉 You've created your first AKU!

---

## Path B: Improving Documentation

### Step 1: Find Documentation to Improve

**Look for**:
- Typos or unclear explanations
- Missing examples
- Outdated information
- Broken links

**Good starting points**:
- Domain READMEs
- Migration guides
- Tool documentation

### Step 2: Make Your Improvements

**Example**: Adding an example to `FAQ.md`

1. **Open file**: `domain/_ontology/FAQ.md`

2. **Find section**: Navigate to relevant question

3. **Add example**:
```markdown
### Q: How do I validate an AKU?

**A**: Use the validation tool:

```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json
```

**Example** (NEW):
```bash
# Validate the Pythagorean theorem AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  domain/formal-sciences/mathematics/geometry/akus/theorems/pythagorean-theorem.json
```
```

### Step 3: Preview Your Changes

**Markdown Preview**:
- Use IDE markdown preview
- Or render with `markdown` command if installed
- Check formatting looks correct

### Step 4: Commit and Create PR

```bash
git checkout -b improve-faq-examples
git add domain/_ontology/FAQ.md
git commit -m "Add validation example to FAQ

- Added concrete example for AKU validation
- Uses Pythagorean theorem as sample
- Improves clarity for new users"
git push origin improve-faq-examples
```

Then create PR on GitHub.

---

## Path C: Running Validation

### Step 1: Understand Validation

**What it checks**:
- JSON syntax valid
- Required fields present
- Proper formatting (timestamps, paths)
- Domain paths in global hierarchy

### Step 2: Validate Single AKU

```bash
# Pick any AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/ct-001-historical-origins.json
```

**Output Analysis**:
- ✅ = Passed
- ❌ = Failed (fix required)
- ⚠️ = Warning (review recommended)

### Step 3: Validate Entire Domain

```bash
# Validate all category theory AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --directory domain/formal-sciences/mathematics/pure-mathematics/category-theory/akus/
```

**Sample Output**:
```
Validating 8 AKU files...

✓ ct-001-historical-origins.json
✓ ct-002-category-definition.json
[... 6 more ...]

=== Summary ===
Total: 8
Valid: 8
Invalid: 0
Success: 100%
```

### Step 4: Check Cross-Domain References

```bash
# Validate that cross-refs work
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/science/computer-science/functional-theory/
```

**What it checks**:
- Native/application domain flags correct
- Cross-references point to existing files
- @id format is correct

### Step 5: Report Issues

**If you find invalid AKUs**:

1. **Document the issue**:
   - Which AKU failed
   - What error message
   - What validation command

2. **Create GitHub issue**:
   - Title: "Validation Error: [AKU name]"
   - Include error details
   - Tag as "validation"

3. **Optional**: Fix it yourself and submit PR!

---

## Common First-Time Mistakes

### Mistake 1: Wrong Timestamp Format

**❌ Wrong**:
```json
{
  "metadata": {
    "created": "2026-01-04 16:00:00"  // Missing T and Z
  }
}
```

**✅ Correct**:
```json
{
  "metadata": {
    "created": "2026-01-04T16:00:00.000Z"  // ISO 8601 with timezone
  }
}
```

**Get current UTC**: `date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"`

### Mistake 2: Forgetting Native Domain Flag

**❌ Wrong**:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra"
    // Missing isNativeDomain!
  }
}
```

**✅ Correct**:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra",
    "isNativeDomain": true,
    "isApplicationDomain": false
  }
}
```

### Mistake 3: Invalid JSON Syntax

**Common errors**:
- Missing comma between fields
- Trailing comma after last field
- Unmatched brackets/braces
- Unescaped quotes in strings

**Solution**: Use JSON validator or IDE with JSON support

### Mistake 4: Wrong Domain Path

**❌ Wrong**:
```json
{
  "classification": {
    "domain_path": "science/math/algebra"  // Old structure!
  }
}
```

**✅ Correct**:
```json
{
  "classification": {
    "domain_path": "formal-sciences/mathematics/algebra"  // New hierarchy
  }
}
```

**Check**: Verify path exists in `domain/_ontology/global-hierarchy.yaml`

---

## Next Steps

### After Your First Contribution

1. **Celebrate!** 🎉 You're now a contributor!

2. **Learn More**:
   - Read `CROSS-DOMAIN-LINKING-GUIDE.md` for advanced concepts
   - Review `MIGRATION-CHECKLIST-TEMPLATE.md` for larger changes
   - Study existing AKUs for patterns

3. **Find More to Do**:
   - Check `.project/issues.md` for open issues
   - Look for domains with few AKUs
   - Improve documentation
   - Add examples to guides

4. **Get Involved**:
   - Comment on PRs
   - Help review contributions
   - Answer questions in issues
   - Suggest improvements

### Contribution Ideas

**Easy**:
- Add more examples to FAQ
- Fix typos in documentation
- Validate existing AKUs

**Medium**:
- Add AKUs for basic concepts
- Improve domain READMEs
- Create visual diagrams

**Advanced**:
- Migrate legacy content
- Add new subdomains
- Improve validation tools

---

## Getting Help

### Stuck? Try These Resources

1. **Documentation**:
   - `INDEX.md` - Find all guides
   - `FAQ.md` - Common questions
   - `TROUBLESHOOTING.md` - Solve problems

2. **Examples**:
   - Category theory AKUs - Well-structured examples
   - Functional programming - Cross-domain references
   - Physics AKUs - Large-scale examples

3. **Ask for Help**:
   - GitHub Issues - Ask questions
   - Pull Requests - Request reviews
   - Issue #3 - Migration-specific questions

### Community Guidelines

- Be respectful and professional
- Ask questions - there are no stupid questions!
- Share your knowledge
- Help others when you can
- Celebrate everyone's contributions

---

## Quick Reference Card

### Essential Commands

```bash
# Validation
python .project/agents/quality-assurance/tools/validate_aku_v2.py file.json

# Cross-domain validation
python domain/_ontology/tools/validate_cross_domain.py file.json

# Get UTC timestamp
date -u +"%Y-%m-%dT%H:%M:%S.%3NZ"

# Create branch
git checkout -b your-branch-name

# Commit changes
git add .
git commit -m "Your message"
git push origin your-branch-name
```

### Required AKU Fields

```json
{
  "@context": "aku-v2",
  "@type": "definition|concept|theorem|formula",
  "@id": "wsmg:domain/subdomain/concept",
  "metadata": { "version", "created", "modified" },
  "classification": { "domain_path", "type", "isNativeDomain" },
  "content": { /* your content */ }
}
```

### File Locations

```
domain/_ontology/         # Documentation
  ├── INDEX.md           # Start here
  ├── FAQ.md             # Questions
  └── TROUBLESHOOTING.md # Problems

domain/[domain]/         # Content
  └── akus/              # AKU files here

.project/                # Project management
  ├── issues.md          # Open work
  └── structure.md       # Organization
```

---

## Congratulations!

You're now ready to contribute to WorldSMEGraphs! Remember:
- Start small
- Validate often
- Ask questions
- Have fun! 🚀

**Your contributions help build a comprehensive, high-quality knowledge graph for the world!**

---

**Last Updated**: 2026-01-04  
**Tutorial Version**: 1.0  
**For More Help**: See `INDEX.md` or ask in Issues

