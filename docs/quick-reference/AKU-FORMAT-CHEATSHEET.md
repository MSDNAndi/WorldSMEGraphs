# AKU Format Cheat Sheet

> **Quick Reference**: Essential AKU structure and fields  
> **Print This**: Keep handy while creating content

## Required Structure

```json
{
  "@context": "aku-v2",           ← Always "aku-v2"
  "@type": "TYPE",                ← definition|theorem|formula|procedure|example|concept
  "@id": "domain:subdomain:id",  ← Unique identifier
  
  "metadata": {
    "version": "2.0.0",
    "created": "2026-01-04T17:00:00.000Z",  ← ISO 8601
    "updated": "2026-01-04T17:00:00.000Z",
    "contributors": ["name"],
    "confidence": 0.95,                      ← 0.0-1.0
    "status": "draft|review|validated|published|archived",
    "tags": ["tag1", "tag2"]
  },
  
  "classification": {
    "domain_path": "formal-sciences/mathematics/...",
    "type": "TYPE",                          ← Same as @type
    "difficulty": "beginner|intermediate|advanced|expert",
    "importance": "foundational|important|supplementary",
    "isNativeDomain": true|false,
    "prerequisites": ["id1", "id2"],
    "learning_objectives": ["objective1"]
  },
  
  "content": {
    // Type-specific content
  }
}
```

## Content by Type

### Definition
```json
"content": {
  "definition": {
    "simple": "For beginners/children",
    "primary": "Standard undergraduate level",
    "technical": "Graduate/professional level"
  }
}
```

### Theorem
```json
"content": {
  "statement": "Formal theorem statement",
  "proof_methods": ["method1", "method2"],
  "applications": ["app1", "app2"]
}
```

### Formula
```json
"content": {
  "formula": {
    "standard": "E = mc²",
    "latex": "E = mc^2",
    "notation": {
      "E": "Energy",
      "m": "Mass",
      "c": "Speed of light"
    }
  }
}
```

### Procedure
```json
"content": {
  "steps": [
    {"step": 1, "action": "...", "details": "..."},
    {"step": 2, "action": "...", "details": "..."}
  ],
  "prerequisites": [...],
  "tools_required": [...]
}
```

### Example
```json
"content": {
  "scenario": "Description",
  "demonstration": "Step-by-step",
  "conclusion": "What this shows"
}
```

### Concept
```json
"content": {
  "overview": "High-level explanation",
  "components": ["part1", "part2"],
  "relationships": [...],
  "significance": "Why this matters"
}
```

## Cross-Domain References

### Native Domain (Math Concept)
```json
"classification": {
  "isNativeDomain": true
},
"cross_domain_applications": {
  "used_in": [
    {
      "domain": "formal-sciences/computer-science/...",
      "context": "How it's used",
      "examples": ["example1"]
    }
  ]
}
```

### Application Domain (CS Using Math)
```json
"classification": {
  "isNativeDomain": false,
  "isApplicationDomain": true
},
"cross_domain_references": {
  "applies": [
    {
      "@id": "wsmg:formal-sciences/mathematics/...",
      "sourceDomain": "formal-sciences/mathematics/...",
      "relationship": "applies",
      "applicationContext": "We use this concept to..."
    }
  ]
}
```

## Semantic Links
```json
"semantic_links": {
  "exact_matches": [
    "http://www.wikidata.org/entity/Q123456",
    "http://dbpedia.org/resource/Concept"
  ],
  "skos_concept": "http://www.wikidata.org/entity/Q123456",
  "skos_preferred_label": {
    "en": "English Name",
    "de": "German Name",
    "es": "Spanish Name"
  }
}
```

## Domain Paths

```
formal-sciences/
  mathematics/
    pure-mathematics/
      algebra/
      geometry/
      category-theory/
    applied-mathematics/
  computer-science/
  logic/

natural-sciences/
  physics/
  chemistry/
  biology/

social-sciences/
  economics/
  psychology/
  sociology/

health-sciences/
  medicine/
  public-health/
```

## Validation Commands

```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate cross-domain references
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/
```

## Quick Checklist

Before saving:
- [ ] @context is "aku-v2"
- [ ] @type is valid
- [ ] @id follows pattern
- [ ] metadata.created is ISO 8601
- [ ] classification.domain_path matches global hierarchy
- [ ] isNativeDomain set correctly
- [ ] Content appropriate for @type
- [ ] All required fields present
- [ ] Validates without errors

## Common Patterns

**Creating UTC Timestamp**:
```bash
date -u +"%Y-%m-%dT%H:%M:%S.000Z"
```

**Python Timestamp**:
```python
from datetime import datetime
datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
```

**ID Format**:
- domain:subdomain:topic:specific-id
- Use lowercase
- Use hyphens for multi-word
- Example: `math:geometry:pythagorean-theorem`

---

**Full Documentation**: See [CONTENT-CREATION-GUIDE.md](../CONTENT-CREATION-GUIDE.md)  
**API Reference**: See [API-DOCUMENTATION-GUIDE.md](../API-DOCUMENTATION-GUIDE.md)  
**Last Updated**: 2026-01-04
