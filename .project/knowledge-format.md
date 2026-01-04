# Knowledge Graph Format Specification

> **Version**: 1.0  
> **Status**: Draft  
> **Last Updated**: 2025-12-26  
> **Owner**: Knowledge Graph Agent

## Overview
This document specifies the format for language-agnostic knowledge graphs in WorldSMEGraphs. The format must be:
- **Language-Agnostic**: No natural language in core representation
- **Compressed**: Efficient storage and transfer
- **Cross-Linkable**: Support for unidirectional and bidirectional links
- **Extensible**: Easy to add new concepts and relationships
- **Parseable**: Machine-readable for rendering and querying

## Design Principles

### 1. Separation of Structure and Content
- Core graph contains only structural relationships
- Natural language content lives in renderings
- Universal identifiers link structure to content

### 2. Semantic Clarity
- Explicit relationship types
- Clear node types (concept, property, example, etc.)
- Hierarchical organization

### 3. Compression Without Loss
- Efficient encoding schemes
- Reusable patterns
- Minimal redundancy
- No loss of semantic meaning

### 4. Cross-Domain Compatibility
- Standardized relationship vocabulary
- Universal concept identifiers
- Clear namespace management

## File Format: knowledge.graph

### Format Choice
**Primary Format**: JSON with optional binary compression

**Rationale**:
- Human-readable in JSON form
- Wide language support
- Easily parsed and validated
- Compressible for storage
- Alternative: Protocol Buffers or MessagePack for production

### Structure

```json
{
  "version": "1.0",
  "domain": "science/math/algebra",
  "created": "2025-12-26T19:00:00Z",
  "modified": "2025-12-26T19:00:00Z",
  "language": "graph",
  "compression": "none",
  
  "metadata": {
    "title": "Algebraic Fundamentals",
    "description": "Core concepts in elementary algebra",
    "authors": ["contributor-id"],
    "tags": ["algebra", "equations", "variables"],
    "difficulty": "elementary",
    "prerequisites": ["arithmetic"]
  },
  
  "nodes": {
    "n1": {
      "type": "concept",
      "uid": "algebra:variable",
      "properties": {
        "abstract": true,
        "symbolic": true,
        "foundational": true
      }
    },
    "n2": {
      "type": "concept",
      "uid": "algebra:equation",
      "properties": {
        "abstract": true,
        "relational": true
      }
    },
    "n3": {
      "type": "operation",
      "uid": "algebra:addition",
      "properties": {
        "commutative": true,
        "associative": true,
        "reversible": true
      }
    }
  },
  
  "edges": [
    {
      "from": "n2",
      "to": "n1",
      "type": "contains",
      "properties": {
        "required": true,
        "quantity": "one-or-more"
      }
    },
    {
      "from": "n3",
      "to": "n1",
      "type": "operates-on",
      "properties": {
        "arity": 2
      }
    }
  ],
  
  "cross_links": [
    {
      "target": "science/math/arithmetic:addition",
      "type": "specializes",
      "bidirectional": false,
      "context": "Algebraic addition extends arithmetic addition to variables"
    },
    {
      "target": "science/math/geometry:coordinate",
      "type": "uses",
      "bidirectional": true,
      "context": "Variables represent coordinates in geometric space"
    }
  ],
  
  "hierarchies": [
    {
      "root": "n1",
      "children": ["n1.1", "n1.2"],
      "type": "specialization"
    }
  ]
}
```

## Node Types

### Concept
Primary knowledge unit representing an abstract or concrete idea.

```json
{
  "type": "concept",
  "uid": "domain:concept-name",
  "properties": {
    "abstract": boolean,
    "concrete": boolean,
    "foundational": boolean
  }
}
```

### Operation
Action or process that transforms or relates concepts.

```json
{
  "type": "operation",
  "uid": "domain:operation-name",
  "properties": {
    "commutative": boolean,
    "associative": boolean,
    "reversible": boolean,
    "arity": number
  }
}
```

### Property
Characteristic or attribute of a concept.

```json
{
  "type": "property",
  "uid": "domain:property-name",
  "properties": {
    "measurable": boolean,
    "binary": boolean
  }
}
```

### Example
Concrete instance or application of a concept.

```json
{
  "type": "example",
  "uid": "domain:example-name",
  "properties": {
    "canonical": boolean,
    "complexity": "simple|medium|complex"
  }
}
```

## Edge Types

### Structural Relationships
- **contains**: A includes B as a component
- **part-of**: B is part of A (inverse of contains)
- **requires**: A needs B to be defined/understood
- **uses**: A employs B in its definition or operation

### Hierarchical Relationships
- **specializes**: A is a more specific version of B
- **generalizes**: A is a broader category including B
- **instance-of**: A is a specific example of B

### Operational Relationships
- **operates-on**: Operation A applies to concept B
- **produces**: A creates or results in B
- **transforms**: A changes B into C

### Logical Relationships
- **implies**: A logically leads to B
- **contradicts**: A is incompatible with B
- **equivalent**: A and B represent the same thing

## Universal Identifiers (UIDs)

### Format
`domain:subdomain:...:concept-name`

### Examples
- `algebra:variable`
- `algebra:equation:linear`
- `macroeconomics:gdp:nominal`

### Rules
1. Hierarchical path from domain to concept
2. Use lowercase with hyphens for multi-word names
3. Unique within global namespace
4. Permanent (don't change once established)

## Cross-Linking

### Cross-Link Structure
```json
{
  "target": "target-domain:concept-uid",
  "type": "relationship-type",
  "bidirectional": boolean,
  "context": "explanation of relationship",
  "strength": "weak|moderate|strong"
}
```

### Types of Cross-Links
- **specializes**: Current concept is specialized form of target
- **generalizes**: Current concept is general form of target
- **uses**: Current concept employs target concept
- **analogous-to**: Similarity between concepts in different domains
- **prerequisite**: Target must be understood before current

### Bidirectional Links
When `bidirectional: true`, both domains should maintain the link.

## Schema Definition (schema.json)

Each knowledge graph has an accompanying schema:

```json
{
  "version": "1.0",
  "graph": "knowledge.graph",
  "node_types": ["concept", "operation", "property", "example"],
  "edge_types": ["contains", "requires", "uses", "specializes"],
  "custom_properties": {
    "difficulty": ["elementary", "intermediate", "advanced"],
    "domain_specific_property": "description"
  },
  "validation_rules": {
    "required_edges": ["Every concept must have at least one relationship"],
    "cross_link_limits": "Maximum 20 cross-links per graph"
  }
}
```

## Compression Strategies

### Level 1: JSON Minification
Remove whitespace, use short keys where possible.

### Level 2: Binary Encoding
Use Protocol Buffers, MessagePack, or BSON for binary representation.

### Level 3: Content Addressing
Store unique nodes/edges once, reference by hash.

### Level 4: Semantic Compression
- Reuse common patterns
- Reference external vocabularies
- Employ abbreviation schemes

## Validation

### Required Elements
- Version
- Domain path
- At least one node
- Valid node types
- Valid edge types
- Unique node IDs within graph

### Consistency Checks
- All edge references point to existing nodes
- UIDs follow naming conventions
- Cross-links target valid domains
- No circular dependencies in hierarchies
- Schema matches graph structure

## Rendering Integration

### UID to Content Mapping
Renderings use UIDs to reference concepts:

```markdown
# Variables
A variable (uid: algebra:variable) is...
```

### Multi-Language Support
Same UID maps to translations:
- English: "variable"
- German: "Variable"
- Spanish: "variable"

## Evolution and Versioning

### Version Format
`major.minor.patch`

### Breaking Changes (Major)
- Change in file format structure
- Removal of required fields
- Change in UID format

### Non-Breaking Changes (Minor)
- Addition of optional fields
- New node/edge types
- Extended properties

### Patches
- Bug fixes
- Documentation updates
- Validation improvements

## Best Practices

### Creating Knowledge Graphs
1. Start with core concepts (nodes)
2. Define relationships (edges)
3. Add properties for depth
4. Establish cross-links
5. Validate against schema
6. Document design decisions

### Naming Conventions
- Use descriptive UIDs
- Keep consistent with domain
- Avoid abbreviations unless standard
- Use American English spelling for UIDs

### Performance Considerations
- Limit graph size to ~500 nodes per file
- Split large domains into sub-graphs
- Use cross-links between sub-graphs
- Index UIDs for fast lookup

## Examples

See pilot implementations:
- `domain/formal-sciences/mathematics/pure-mathematics/algebra/knowledge.graph` (planned)
- `domain/social-sciences/economics/macroeconomics/knowledge.graph` (planned)

## Future Enhancements

### Under Consideration
1. **Temporal Knowledge**: Version concepts over time
2. **Probabilistic Relations**: Confidence scores on edges
3. **Multimedia Integration**: Links to images, videos, animations
4. **Interactive Elements**: Executable examples or simulations
5. **Collaborative Editing**: Merge strategies and conflict resolution

## References

- Semantic Web standards (RDF, OWL)
- Knowledge Graph best practices
- Graph database schemas (Neo4j, etc.)
- Ontology engineering principles

---

**Status**: This specification is in draft form and will be refined based on pilot implementation feedback.
