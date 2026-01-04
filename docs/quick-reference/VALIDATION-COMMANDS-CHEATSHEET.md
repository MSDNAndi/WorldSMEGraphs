# Validation Commands Cheat Sheet

> **Quick Reference**: Common validation commands  
> **Keep Handy**: For daily development work

## AKU Validation

### Single AKU
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json
```

### With Verbose Output
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json --verbose
```

### Directory of AKUs
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/
```

### Specific Domain
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine
```

## Cross-Domain Validation

### Single AKU
```bash
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json
```

### Directory
```bash
python domain/_ontology/tools/validate_cross_domain.py --directory path/to/akus/
```

## Agent Validation

### Check Agent Lengths
```bash
bash .github/scripts/check-agent-lengths.sh
```

Verifies all agents meet 180-line minimum requirement.

## Structure Validation

### Verify Repository Structure
```bash
bash .github/scripts/validate-structure.sh
```

Checks:
- Required directories exist
- Essential files present
- Validation scripts available
- Agent files present

## Workflow Testing

### Test Workflows Locally
```bash
bash .github/scripts/test-workflow-locally.sh
```

Validates:
- Python installation
- Script functionality
- Domain discovery
- YAML syntax

## File Checks

### Check Encoding
```bash
file -i path/to/file.md
```

Should show: `charset=utf-8`

### Count Lines
```bash
wc -l path/to/file.md
```

### Check JSON Syntax
```bash
python -m json.tool path/to/file.json > /dev/null
```

No output = valid JSON

### Validate Against Schema
```bash
python -c "import json, jsonschema; ..."
```

## Git Commands

### Check Status
```bash
git status
```

### Check Changes
```bash
git --no-pager diff
```

### Check Specific File
```bash
git --no-pager diff path/to/file
```

### View Commit
```bash
git --no-pager show COMMIT_HASH
```

## Search Commands

### Find AKUs
```bash
find domain/ -name "*.json" -type f ! -name "schema.json"
```

### Find by Domain
```bash
find domain/formal-sciences/mathematics -name "*.json"
```

### Count AKUs in Domain
```bash
find domain/natural-sciences/physics -name "*.json" ! -name "schema.json" | wc -l
```

### Find Missing Field
```bash
find domain/ -name "*.json" ! -name "schema.json" | while read f; do
  if ! grep -q '"domain_path"' "$f" 2>/dev/null; then
    echo "$f"
  fi
done
```

## Grep Commands

### Find Text in AKUs
```bash
grep -r "pythagorean" domain/formal-sciences/mathematics/
```

### Find Field Value
```bash
grep -r '"difficulty": "beginner"' domain/
```

### Count Occurrences
```bash
grep -r '"@type": "theorem"' domain/ | wc -l
```

## Python Quick Commands

### Validate AKU in Script
```python
import json, sys

with open(sys.argv[1]) as f:
    aku = json.load(f)

assert aku.get('@context') == 'aku-v2', "Invalid context"
assert '@id' in aku, "Missing @id"
assert 'classification' in aku, "Missing classification"
assert 'domain_path' in aku.get('classification', {}), "Missing domain_path"

print("✅ Basic validation passed")
```

### Count AKUs by Type
```python
import json, glob
from collections import Counter

types = []
for f in glob.glob("domain/**/*.json", recursive=True):
    if "schema.json" in f:
        continue
    try:
        with open(f) as fp:
            aku = json.load(fp)
            if aku.get('@context') == 'aku-v2':
                types.append(aku.get('@type'))
    except:
        pass

print(Counter(types))
```

## Troubleshooting

### JSON Decode Error
```bash
python -m json.tool problematic.json
```

Shows exact line/column of error.

### UTF-8 Encoding Issues
```bash
iconv -f UTF-8 -t UTF-8 file.json -o /dev/null
```

Returns error if file isn't valid UTF-8.

### Find Large Files
```bash
find domain/ -name "*.json" -size +100k
```

### Find Recent Changes
```bash
find domain/ -name "*.json" -mtime -1
```

Files modified in last 24 hours.

## Common Workflows

### Before Committing
```bash
# 1. Validate changed AKUs
git diff --name-only | grep ".json$" | while read f; do
  echo "Validating $f"
  python .project/agents/quality-assurance/tools/validate_aku_v2.py "$f"
done

# 2. Check structure
bash .github/scripts/validate-structure.sh

# 3. Run agent check (if modified agents)
bash .github/scripts/check-agent-lengths.sh
```

### After Migration
```bash
# 1. Validate migrated directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/new-location/

# 2. Check cross-domain links
python domain/_ontology/tools/validate_cross_domain.py --directory domain/new-location/

# 3. Count successes
find domain/new-location/ -name "*.json" ! -name "schema.json" | wc -l
```

### Quality Check
```bash
# 1. Validate all AKUs in domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain mathematics

# 2. Check for common issues
grep -r '"isNativeDomain"' domain/ | grep -v "true"  # Find application domains

# 3. Verify timestamps
grep -r '"created":' domain/ | grep -v "T.*Z"  # Find non-ISO timestamps
```

---

**Full Documentation**: 
- [CONTENT-CREATION-GUIDE.md](../CONTENT-CREATION-GUIDE.md)
- [TROUBLESHOOTING.md](../../domain/_ontology/TROUBLESHOOTING.md)
- [TOOLS-DOCUMENTATION.md](../../domain/_ontology/TOOLS-DOCUMENTATION.md)

**Last Updated**: 2026-01-04
