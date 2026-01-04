# API Documentation Guide for WorldSMEGraphs

> **Purpose**: Guidelines for creating and using APIs with WorldSMEGraphs  
> **Audience**: Developers, integrators, API designers  
> **Last Updated**: 2026-01-04

## Table of Contents

1. [Introduction](#introduction)
2. [AKU JSON Schema](#aku-json-schema)
3. [REST API Design](#rest-api-design)
4. [GraphQL Schema](#graphql-schema)
5. [Query Patterns](#query-patterns)
6. [Response Formats](#response-formats)
7. [Error Handling](#error-handling)
8. [Authentication](#authentication)
9. [Rate Limiting](#rate-limiting)
10. [Examples](#examples)

---

## Introduction

WorldSMEGraphs uses a file-based architecture, but provides API interfaces for querying and rendering knowledge. This guide covers API design principles and implementation patterns.

### Architecture Overview

```
┌─────────────────────────────────────────────────┐
│          Client Applications                     │
│  (Web, Mobile, Desktop, CLI)                    │
└──────────────────┬──────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼────┐   ┌────▼────┐   ┌────▼────┐
│  REST  │   │ GraphQL │   │  Direct │
│  API   │   │   API   │   │  File   │
└───┬────┘   └────┬────┘   └────┬────┘
    │              │              │
    └──────────────┼──────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│         Knowledge Graph Layer                    │
│  - Query Engine                                  │
│  - Cross-Domain Resolver                         │
│  - Render Engine                                 │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│         File System Storage                      │
│  - AKU JSON files                                │
│  - Rendered content                              │
│  - Metadata indexes                              │
└──────────────────────────────────────────────────┘
```

---

## AKU JSON Schema

### Core Schema (v2.0)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AKU v2.0 Schema",
  "type": "object",
  "required": ["@context", "@type", "@id", "metadata", "classification", "content"],
  "properties": {
    "@context": {
      "type": "string",
      "const": "aku-v2",
      "description": "AKU version identifier"
    },
    "@type": {
      "type": "string",
      "enum": ["definition", "theorem", "formula", "procedure", "example", "concept"],
      "description": "Type of knowledge unit"
    },
    "@id": {
      "type": "string",
      "pattern": "^[a-z0-9:-]+$",
      "description": "Unique identifier (domain:subdomain:topic:id)"
    },
    "metadata": {
      "type": "object",
      "required": ["version", "created", "updated", "status"],
      "properties": {
        "version": { "type": "string" },
        "created": { "type": "string", "format": "date-time" },
        "updated": { "type": "string", "format": "date-time" },
        "contributors": { "type": "array", "items": { "type": "string" } },
        "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
        "status": { 
          "type": "string",
          "enum": ["draft", "review", "validated", "published", "archived"]
        },
        "tags": { "type": "array", "items": { "type": "string" } }
      }
    },
    "classification": {
      "type": "object",
      "required": ["domain_path", "type", "difficulty"],
      "properties": {
        "domain_path": { "type": "string" },
        "type": { "type": "string" },
        "difficulty": {
          "type": "string",
          "enum": ["beginner", "intermediate", "advanced", "expert"]
        },
        "importance": {
          "type": "string",
          "enum": ["foundational", "important", "supplementary"]
        },
        "isNativeDomain": { "type": "boolean" },
        "prerequisites": { "type": "array", "items": { "type": "string" } },
        "learning_objectives": { "type": "array", "items": { "type": "string" } }
      }
    },
    "content": {
      "type": "object",
      "description": "Content structure depends on @type"
    },
    "cross_domain_references": {
      "type": "object",
      "additionalProperties": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["@id", "sourceDomain", "relationship"],
          "properties": {
            "@id": { "type": "string" },
            "sourceDomain": { "type": "string" },
            "relationship": { "type": "string" },
            "applicationContext": { "type": "string" }
          }
        }
      }
    },
    "semantic_links": {
      "type": "object",
      "properties": {
        "exact_matches": { "type": "array", "items": { "type": "string", "format": "uri" } },
        "close_matches": { "type": "array", "items": { "type": "string", "format": "uri" } },
        "broad_matches": { "type": "array", "items": { "type": "string", "format": "uri" } },
        "related_matches": { "type": "array", "items": { "type": "string", "format": "uri" } },
        "skos_concept": { "type": "string", "format": "uri" },
        "skos_preferred_label": { "type": "object" },
        "skos_alt_label": { "type": "object" }
      }
    }
  }
}
```

### Validation

```bash
# Validate AKU against schema
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate cross-domain references
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json
```

---

## REST API Design

### Base URL

```
https://api.worldsmegraphs.org/v2/
```

### Endpoints

#### Get AKU by ID

```http
GET /akus/{aku_id}

# Example
GET /akus/math:geometry:pythagorean-theorem

# Response
{
  "status": "success",
  "data": {
    "@context": "aku-v2",
    "@type": "theorem",
    "@id": "math:geometry:pythagorean-theorem",
    // ... full AKU content
  }
}
```

#### Search AKUs

```http
GET /akus/search?q={query}&domain={domain}&difficulty={level}

# Example
GET /akus/search?q=pythagorean&domain=mathematics&difficulty=intermediate

# Response
{
  "status": "success",
  "data": {
    "total": 1,
    "results": [
      {
        "@id": "math:geometry:pythagorean-theorem",
        "title": "Pythagorean Theorem",
        "domain": "formal-sciences/mathematics/geometry",
        "difficulty": "intermediate",
        "snippet": "In a right triangle..."
      }
    ]
  },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total_pages": 1
  }
}
```

#### Get Domain Hierarchy

```http
GET /domains

# Response
{
  "status": "success",
  "data": [
    {
      "name": "formal-sciences",
      "subdomains": [
        {
          "name": "mathematics",
          "subdomains": [...]
        },
        {
          "name": "computer-science",
          "subdomains": [...]
        }
      ]
    },
    // ... other domains
  ]
}
```

#### Get Rendered Content

```http
GET /akus/{aku_id}/render?language={lang}&audience={level}

# Example
GET /akus/math:geometry:pythagorean-theorem/render?language=english&audience=high-school

# Response
{
  "status": "success",
  "data": {
    "aku_id": "math:geometry:pythagorean-theorem",
    "language": "english",
    "audience": "high-school",
    "format": "markdown",
    "content": "# Pythagorean Theorem\n\n..."
  }
}
```

#### Get Cross-Domain Links

```http
GET /akus/{aku_id}/cross-domain-links

# Response
{
  "status": "success",
  "data": {
    "native_domain": "formal-sciences/mathematics/pure-mathematics/category-theory",
    "applications": [
      {
        "domain": "formal-sciences/computer-science/functional-programming",
        "akus": ["cs:fp:monads", "cs:fp:functors"],
        "relationship": "applies"
      }
    ],
    "references": [
      {
        "aku_id": "math:algebra:groups",
        "relationship": "prerequisite"
      }
    ]
  }
}
```

---

## GraphQL Schema

### Type Definitions

```graphql
type AKU {
  id: ID!
  context: String!
  type: AKUType!
  metadata: Metadata!
  classification: Classification!
  content: JSON!
  crossDomainReferences: [CrossDomainReference!]
  semanticLinks: SemanticLinks
  renders(language: Language, audience: AudienceLevel): [Render!]
}

enum AKUType {
  DEFINITION
  THEOREM
  FORMULA
  PROCEDURE
  EXAMPLE
  CONCEPT
}

type Metadata {
  version: String!
  created: DateTime!
  updated: DateTime!
  contributors: [String!]
  confidence: Float
  status: Status!
  tags: [String!]
}

enum Status {
  DRAFT
  REVIEW
  VALIDATED
  PUBLISHED
  ARCHIVED
}

type Classification {
  domainPath: String!
  type: String!
  difficulty: Difficulty!
  importance: Importance
  isNativeDomain: Boolean
  prerequisites: [String!]
  learningObjectives: [String!]
}

enum Difficulty {
  BEGINNER
  INTERMEDIATE
  ADVANCED
  EXPERT
}

enum Importance {
  FOUNDATIONAL
  IMPORTANT
  SUPPLEMENTARY
}

type CrossDomainReference {
  id: String!
  sourceDomain: String!
  relationship: String!
  applicationContext: String
  referencedAKU: AKU
}

type SemanticLinks {
  exactMatches: [String!]
  closeMatches: [String!]
  broadMatches: [String!]
  relatedMatches: [String!]
  skosConcept: String
  skosPreferredLabel: JSON
}

type Render {
  language: Language!
  audience: AudienceLevel!
  format: RenderFormat!
  content: String!
}

enum Language {
  ENGLISH
  SPANISH
  GERMAN
  FRENCH
  CHINESE
  JAPANESE
  // ...
}

enum AudienceLevel {
  TODDLER
  CHILD
  PRE_TEEN
  HIGH_SCHOOL
  UNDERGRADUATE
  GRADUATE
  PROFESSIONAL
}

enum RenderFormat {
  MARKDOWN
  HTML
  PDF
  LATEX
}

type Query {
  # Get single AKU
  aku(id: ID!): AKU
  
  # Search AKUs
  search(
    query: String
    domain: String
    difficulty: Difficulty
    tags: [String!]
    limit: Int = 20
    offset: Int = 0
  ): SearchResult!
  
  # Get domain hierarchy
  domains: [Domain!]!
  
  # Get AKUs by domain
  akusByDomain(
    domainPath: String!
    recursive: Boolean = false
  ): [AKU!]!
  
  # Get cross-domain graph
  crossDomainGraph(fromDomain: String!, toDomain: String!): [CrossDomainLink!]!
}

type SearchResult {
  total: Int!
  results: [AKU!]!
  facets: SearchFacets
}

type SearchFacets {
  domains: [FacetCount!]!
  difficulties: [FacetCount!]!
  types: [FacetCount!]!
}

type FacetCount {
  value: String!
  count: Int!
}

type Domain {
  path: String!
  name: String!
  description: String
  akuCount: Int!
  subdomains: [Domain!]
}

type CrossDomainLink {
  from: AKU!
  to: AKU!
  relationship: String!
  context: String
}
```

### Example Queries

```graphql
# Get AKU with renders
query GetPythagoreanTheorem {
  aku(id: "math:geometry:pythagorean-theorem") {
    id
    type
    classification {
      difficulty
      domainPath
    }
    content
    renders(language: ENGLISH, audience: HIGH_SCHOOL) {
      content
    }
  }
}

# Search with filters
query SearchMathematics {
  search(
    query: "theorem"
    domain: "formal-sciences/mathematics"
    difficulty: INTERMEDIATE
    limit: 10
  ) {
    total
    results {
      id
      type
      classification {
        domainPath
        difficulty
      }
      metadata {
        tags
      }
    }
    facets {
      domains {
        value
        count
      }
    }
  }
}

# Get cross-domain connections
query CategoryTheoryApplications {
  aku(id: "math:category-theory:monad") {
    id
    classification {
      isNativeDomain
    }
    crossDomainReferences {
      sourceDomain
      relationship
      applicationContext
      referencedAKU {
        id
        classification {
          domainPath
        }
      }
    }
  }
}
```

---

## Query Patterns

### Common Queries

#### 1. Get AKU with Full Context

```python
import requests

def get_aku_with_context(aku_id):
    """Get AKU with prerequisites and related concepts."""
    response = requests.get(f"https://api.worldsmegraphs.org/v2/akus/{aku_id}")
    aku = response.json()['data']
    
    # Get prerequisites
    prerequisites = []
    for prereq_id in aku['classification'].get('prerequisites', []):
        prereq = requests.get(f"https://api.worldsmegraphs.org/v2/akus/{prereq_id}")
        prerequisites.append(prereq.json()['data'])
    
    return {
        'aku': aku,
        'prerequisites': prerequisites
    }
```

#### 2. Traverse Cross-Domain Links

```python
def get_cross_domain_applications(native_aku_id):
    """Find all application domains for a native concept."""
    response = requests.get(
        f"https://api.worldsmegraphs.org/v2/akus/{native_aku_id}/cross-domain-links"
    )
    return response.json()['data']['applications']
```

#### 3. Build Learning Path

```python
def build_learning_path(target_aku_id):
    """Build learning path with all prerequisites."""
    visited = set()
    path = []
    
    def traverse(aku_id):
        if aku_id in visited:
            return
        visited.add(aku_id)
        
        aku = get_aku(aku_id)
        for prereq in aku['classification'].get('prerequisites', []):
            traverse(prereq)
        
        path.append(aku)
    
    traverse(target_aku_id)
    return path
```

---

## Response Formats

### Success Response

```json
{
  "status": "success",
  "data": { ... },
  "meta": {
    "timestamp": "2026-01-04T17:20:00Z",
    "version": "2.0",
    "request_id": "abc123"
  }
}
```

### Error Response

```json
{
  "status": "error",
  "error": {
    "code": "AKU_NOT_FOUND",
    "message": "AKU with ID 'invalid-id' not found",
    "details": {
      "searched_id": "invalid-id",
      "suggestions": [
        "math:geometry:pythagorean-theorem",
        "math:geometry:triangle-properties"
      ]
    }
  },
  "meta": {
    "timestamp": "2026-01-04T17:20:00Z",
    "request_id": "abc123"
  }
}
```

---

## Error Handling

### Error Codes

```
# Client Errors (4xx)
400 BAD_REQUEST          - Invalid parameters
401 UNAUTHORIZED         - Authentication required
403 FORBIDDEN           - Insufficient permissions
404 NOT_FOUND           - Resource not found
422 VALIDATION_ERROR    - Invalid AKU structure
429 RATE_LIMIT_EXCEEDED - Too many requests

# Server Errors (5xx)
500 INTERNAL_ERROR      - Server error
503 SERVICE_UNAVAILABLE - Temporary unavailability
```

### Error Response Examples

```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "AKU validation failed",
    "details": {
      "errors": [
        {
          "field": "classification.domain_path",
          "message": "Domain path not in global hierarchy"
        }
      ]
    }
  }
}
```

---

## Authentication

### API Key Authentication

```http
GET /akus/math:geometry:pythagorean-theorem
Authorization: Bearer YOUR_API_KEY
```

### OAuth 2.0

```http
GET /akus/math:geometry:pythagorean-theorem
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## Rate Limiting

### Rate Limits

```
Free Tier:     100 requests/hour
Basic Tier:    1,000 requests/hour
Pro Tier:      10,000 requests/hour
Enterprise:    Unlimited
```

### Rate Limit Headers

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1704390000
```

---

## Examples

### Python SDK Example

```python
from worldsmegraphs import WorldSMEGraphsClient

# Initialize client
client = WorldSMEGraphsClient(api_key="YOUR_API_KEY")

# Get AKU
aku = client.akus.get("math:geometry:pythagorean-theorem")
print(f"AKU: {aku.id}")
print(f"Type: {aku.type}")
print(f"Domain: {aku.classification.domain_path}")

# Search
results = client.akus.search(
    query="pythagorean",
    domain="mathematics",
    difficulty="intermediate"
)
print(f"Found {results.total} results")

# Get render
render = client.akus.render(
    aku_id="math:geometry:pythagorean-theorem",
    language="english",
    audience="high-school"
)
print(render.content)

# Get cross-domain links
links = client.akus.cross_domain_links("math:category-theory:monad")
for app in links.applications:
    print(f"Used in: {app.domain}")
```

### JavaScript/TypeScript Example

```typescript
import { WorldSMEGraphsClient } from '@worldsmegraphs/client';

// Initialize
const client = new WorldSMEGraphsClient({
  apiKey: 'YOUR_API_KEY'
});

// Get AKU
const aku = await client.akus.get('math:geometry:pythagorean-theorem');
console.log(`AKU: ${aku.id}`);

// Search
const results = await client.akus.search({
  query: 'pythagorean',
  domain: 'mathematics',
  difficulty: 'intermediate'
});
console.log(`Found ${results.total} results`);

// Get render
const render = await client.akus.render({
  akuId: 'math:geometry:pythagorean-theorem',
  language: 'english',
  audience: 'high-school'
});
console.log(render.content);
```

---

**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Maintainer**: WorldSMEGraphs Team
