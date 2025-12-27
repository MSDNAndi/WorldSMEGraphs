# Knowledge Representation Format v2.0
**Version**: 2.0  
**Date**: 2025-12-27  
**Status**: Specification Draft

## Core Design Principles

### 1. Meta-Level Architecture
**Problem**: Can't predefine domain-specific structures for all of world's knowledge.

**Solution**: Generic, extensible format that works for ANY domain:
- Physics, Chemistry, Business, Law, Medicine, Philosophy, etc.
- Format is domain-agnostic
- Domain-specific semantics emerge from content, not structure

### 2. Text-Only Representation
**Requirement**: Must use text-based meta-languages only.

**Supported formats** (ordered by preference):
1. **JSON-LD** - Primary (JSON + semantic web compatibility)
2. **YAML** - Human-readable alternative
3. **XML/RDF** - Standards compatibility
4. **Protocol Buffers** - Binary serialization for performance

**Why text-only**:
- Version control friendly (Git)
- Human readable/editable
- Language/tool agnostic
- Mergeable
- Diffable

### 3. Logarithmic Navigation
**Requirement**: Navigate root → leaf in O(log n) time.

**Solution**: Hierarchical tree structure with indexing:
```
domain/
├── index.json          # O(1) lookup to any subdomain
├── subdomain1/
│   ├── index.json      # O(1) lookup to any topic
│   └── topic1/
│       ├── index.json  # O(1) lookup to any AKU
│       └── aku0001.json
```

**Navigation complexity**:
- Depth: ~5-7 levels max
- Fanout: ~10-100 per level
- Total: O(log₁₀ n) ≈ 5-7 steps for millions of AKUs

### 4. Research-First, Expert-Guided
**Workflow**:
1. **Meta-level agents** research and extract from sources
2. **Generic extraction agents** create raw AKU candidates
3. **Domain expert agents** validate, merge, refine
4. **Human experts** final approval

**Not**: Experts create everything from scratch  
**But**: Experts curate what agents extract

---

## Format Specification

### Top-Level Structure

```yaml
# domain-root.yaml
domain:
  id: "economics/bwl"
  version: "2.0"
  schema: "https://worldsmegraphs.org/schema/v2/domain"
  
metadata:
  title:
    en: "Business Administration"
    de: "Betriebswirtschaftslehre"
  description: "Complete knowledge representation of business administration"
  created: "2025-12-27T00:00:00Z"
  modified: "2025-12-27T00:00:00Z"
  contributors:
    - id: "agent:research-001"
    - id: "expert:bwl-001"
  license: "CC-BY-4.0"
  sources:
    - doi: "10.1234/example"
    - isbn: "978-3-8006-4600-1"
    - url: "https://openalex.org/W..."

index:
  subdomains:
    - id: "accounting"
      title: "Rechnungswesen"
      aku_count: 2500
      path: "accounting/index.yaml"
    - id: "finance"
      title: "Finanzwirtschaft"
      aku_count: 3200
      path: "finance/index.yaml"
    # ... more subdomains

navigation:
  total_akus: 85000
  depth: 5
  fanout_avg: 15
  index_type: "b-tree"
```

### Subdomain Index

```yaml
# subdomain-index.yaml
subdomain:
  id: "finance"
  parent: "economics/bwl"
  schema: "https://worldsmegraphs.org/schema/v2/subdomain"

metadata:
  title:
    en: "Corporate Finance"
    de: "Finanzwirtschaft"
  aku_count: 3200
  
index:
  topics:
    - id: "capital-structure"
      title: "Capital Structure"
      aku_count: 450
      path: "capital-structure/index.yaml"
    - id: "valuation"
      title: "Valuation"
      aku_count: 680
      path: "valuation/index.yaml"
    # ... more topics

prerequisites:
  - domain: "mathematics/statistics"
    topics: ["probability", "distributions"]
  - domain: "economics/microeconomics"
    topics: ["market-equilibrium"]

cross_links:
  - domain: "economics/bwl/accounting"
    topics: ["financial-statements"]
    relationship: "provides-data-for"
```

### Topic Index

```yaml
# topic-index.yaml
topic:
  id: "valuation"
  parent: "economics/bwl/finance"
  schema: "https://worldsmegraphs.org/schema/v2/topic"

metadata:
  title:
    en: "Business Valuation"
    de: "Unternehmensbewertung"
  aku_count: 680
  
index:
  concepts:
    - id: "npv"
      title: "Net Present Value"
      aku_count: 120
      path: "npv/index.yaml"
    - id: "irr"
      title: "Internal Rate of Return"
      aku_count: 95
      path: "irr/index.yaml"
    # ... more concepts

search_index:
  # For O(1) keyword lookup
  keywords:
    "discounting": ["npv", "dcf", "wacc"]
    "cash-flow": ["fcf", "fcfe", "fcff"]
  formulas:
    "NPV": ["npv-001", "npv-002"]
```

### Concept Index

```yaml
# concept-index.yaml
concept:
  id: "npv"
  parent: "economics/bwl/finance/valuation"
  schema: "https://worldsmegraphs.org/schema/v2/concept"

metadata:
  title:
    en: "Net Present Value"
    de: "Kapitalwert"
  aku_count: 120
  
index:
  aku_groups:
    - group: "definition"
      count: 5
      akus: ["npv-def-001", "npv-def-002", ...]
    - group: "formula"
      count: 8
      akus: ["npv-formula-001", "npv-formula-002", ...]
    - group: "derivation"
      count: 12
      akus: ["npv-deriv-001", "npv-deriv-002", ...]
    - group: "example"
      count: 25
      akus: ["npv-ex-001", "npv-ex-002", ...]
    - group: "application"
      count: 15
      akus: ["npv-app-001", "npv-app-002", ...]
    - group: "limitation"
      count: 10
      akus: ["npv-lim-001", "npv-lim-002", ...]
    - group: "comparison"
      count: 8
      akus: ["npv-cmp-001", "npv-cmp-002", ...]
    - group: "historical"
      count: 5
      akus: ["npv-hist-001", "npv-hist-002", ...]

relationships:
  prerequisites: ["time-value-money", "discounting", "cash-flow"]
  enables: ["project-selection", "capital-budgeting"]
  compares_to: ["irr", "payback-period", "profitability-index"]
```

---

## Atomic Knowledge Unit (AKU) Format

### AKU Structure (JSON-LD)

```json
{
  "@context": "https://worldsmegraphs.org/context/v2/aku",
  "@type": "AtomicKnowledgeUnit",
  "@id": "urn:wskg:bwl:finance:valuation:npv:formula:001",
  
  "metadata": {
    "created": "2025-12-27T00:00:00Z",
    "modified": "2025-12-27T00:00:00Z",
    "version": "1.0",
    "status": "validated",
    "confidence": 1.0,
    "contributors": [
      {"id": "agent:research-001", "role": "extraction"},
      {"id": "agent:extraction-001", "role": "formatting"},
      {"id": "expert:finance-001", "role": "validation"}
    ],
    "language": "en",
    "translations": ["de", "es", "fr"]
  },
  
  "classification": {
    "domain": "economics/bwl",
    "subdomain": "finance",
    "topic": "valuation",
    "concept": "npv",
    "type": "formula",
    "difficulty": "undergraduate",
    "importance": 0.95
  },
  
  "content": {
    "statement": {
      "text": "Net Present Value is the sum of discounted cash flows",
      "formal": "NPV = ∑(t=0 to n) CF_t / (1+r)^t"
    },
    
    "representations": {
      "latex": "NPV = \\sum_{t=0}^{n} \\frac{CF_t}{(1+r)^t}",
      
      "mathml": "<math><mrow>...</mrow></math>",
      
      "code": {
        "python": "def npv(cash_flows, rate): return sum(cf/(1+rate)**t for t, cf in enumerate(cash_flows))",
        "julia": "npv(cf, r) = sum(cf[t]/(1+r)^(t-1) for t in 1:length(cf))",
        "r": "npv <- function(cf, r) sum(cf / (1+r)^(0:(length(cf)-1)))"
      },
      
      "variables": [
        {
          "symbol": "CF_t",
          "name": "Cash Flow at time t",
          "type": "Real",
          "unit": "currency",
          "constraints": "CF_t ∈ ℝ"
        },
        {
          "symbol": "r",
          "name": "Discount rate",
          "type": "Real",
          "unit": "percentage",
          "constraints": "r > -1"
        },
        {
          "symbol": "t",
          "name": "Time period",
          "type": "Natural",
          "unit": "time_period",
          "constraints": "t ∈ ℕ₀, 0 ≤ t ≤ n"
        }
      ]
    },
    
    "explanation": {
      "intuition": "NPV converts future cash flows to today's value, accounting for the time value of money",
      "key_insight": "Money today is worth more than money tomorrow due to earning potential",
      "common_misconception": "NPV and profit are not the same; NPV accounts for timing"
    }
  },
  
  "relationships": {
    "prerequisites": [
      {"id": "urn:wskg:bwl:finance:time-value-money:001", "strength": 1.0},
      {"id": "urn:wskg:math:algebra:summation:001", "strength": 0.8}
    ],
    "enables": [
      {"id": "urn:wskg:bwl:finance:capital-budgeting:001", "strength": 0.9}
    ],
    "related": [
      {"id": "urn:wskg:bwl:finance:irr:001", "type": "alternative_method"},
      {"id": "urn:wskg:bwl:finance:pi:001", "type": "derived_metric"}
    ],
    "conflicts": [],
    "supersedes": []
  },
  
  "provenance": {
    "sources": [
      {
        "type": "textbook",
        "citation": "Brealey, R. A., Myers, S. C., & Allen, F. (2020). Principles of Corporate Finance. McGraw-Hill.",
        "isbn": "978-1260013900",
        "page": "108-112",
        "confidence": 1.0
      },
      {
        "type": "paper",
        "doi": "10.1111/j.1540-6261.1978.tb02055.x",
        "confidence": 0.95
      },
      {
        "type": "research_database",
        "url": "https://openalex.org/W2048953928",
        "extracted_date": "2025-12-27"
      }
    ],
    "extraction_method": "agent:research-001",
    "validation": {
      "validator": "expert:finance-001",
      "date": "2025-12-27",
      "notes": "Formula verified against multiple sources"
    }
  },
  
  "pedagogical": {
    "target_audience": ["undergraduate", "mba", "professional"],
    "estimated_time": "15min",
    "difficulty_curve": 0.6,
    "prerequisites_check": true,
    "common_errors": [
      "Forgetting to include t=0 (initial investment)",
      "Using nominal instead of real discount rate",
      "Mixing different time units"
    ]
  },
  
  "rendering_hints": {
    "primary_representation": "latex",
    "show_derivation": true,
    "include_worked_example": true,
    "visualization": "cash_flow_timeline"
  }
}
```

### AKU Types

**1. Definition AKU**
```json
{
  "@type": "AtomicKnowledgeUnit",
  "classification": {"type": "definition"},
  "content": {
    "statement": {"text": "Precise definition"},
    "formal_logic": "∀x (P(x) → Q(x))"
  }
}
```

**2. Formula AKU**
```json
{
  "@type": "AtomicKnowledgeUnit",
  "classification": {"type": "formula"},
  "content": {
    "representations": {
      "latex": "...",
      "code": {...},
      "variables": [...]
    }
  }
}
```

**3. Example AKU**
```json
{
  "@type": "AtomicKnowledgeUnit",
  "classification": {"type": "example"},
  "content": {
    "scenario": "A company considering investment...",
    "given": {"CF": [-1000, 300, 400, 500], "r": 0.10},
    "solution": {
      "steps": [...],
      "result": 49.21,
      "interpretation": "..."
    }
  }
}
```

**4. Theorem/Proof AKU**
```json
{
  "@type": "AtomicKnowledgeUnit",
  "classification": {"type": "theorem"},
  "content": {
    "statement": "NPV is continuous and monotonically decreasing in r",
    "proof": {
      "method": "calculus",
      "steps": [...],
      "qed": true
    }
  }
}
```

**5. Historical AKU**
```json
{
  "@type": "AtomicKnowledgeUnit",
  "classification": {"type": "historical"},
  "content": {
    "event": "Irving Fisher introduced time value concepts",
    "date": "1907",
    "significance": "Foundation for modern DCF",
    "source": {"work": "The Rate of Interest", "year": 1907}
  }
}
```

---

## Navigation & Indexing

### B-Tree Index Structure

```yaml
# global-index.yaml
index:
  version: "2.0"
  type: "b-tree"
  fanout: 100
  
  # Root level - Domains
  domains:
    - {id: "mathematics", aku_count: 250000, path: "domain/mathematics"}
    - {id: "physics", aku_count: 180000, path: "domain/physics"}
    - {id: "economics", aku_count: 150000, path: "domain/economics"}
    # ... ~100 domains
  
  # Search accelerators
  keyword_index:
    # Inverted index for O(1) keyword lookup
    "npv": ["economics/bwl/finance/valuation/npv"]
    "discounting": ["economics/bwl/finance/valuation/npv", "economics/bwl/finance/wacc"]
  
  formula_index:
    # Math expression search
    "\\sum.*CF.*r": ["economics/bwl/finance/valuation/npv"]
  
  concept_graph:
    # Prerequisite DAG for learning paths
    nodes: [...]
    edges: [...]
```

### Navigation Query Examples

**Query 1: Direct access to AKU**
```
Path: economics/bwl/finance/valuation/npv/formula/001
Steps: 
1. Load domain index (O(1))
2. Load subdomain index (O(1))
3. Load topic index (O(1))
4. Load concept index (O(1))
5. Load AKU (O(1))
Total: O(5) = O(log n) with depth=5
```

**Query 2: Keyword search**
```
Query: "NPV formula"
1. Lookup "npv" in keyword_index → concept path (O(1))
2. Lookup "formula" in concept index → AKU list (O(1))
3. Load AKU (O(1))
Total: O(3)
```

**Query 3: Learning path**
```
Query: "Learn valuation from scratch"
1. Lookup "valuation" → topic (O(1))
2. Get prerequisites from topic index
3. Topological sort of prerequisite DAG (O(n))
4. Return ordered learning path
```

---

## Extraction & Research Workflow

### Meta-Level Agent Architecture

**Generic Research Agents** (no domain knowledge):
1. **Web Scraper Agent** - Extracts from online sources
2. **Paper Miner Agent** - Extracts from academic papers (PDF, arXiv)
3. **Textbook Parser Agent** - OCR + structure extraction
4. **Video Transcriber Agent** - Extracts from educational videos
5. **Database Query Agent** - Pulls from Wikidata, OpenAlex, etc.

**Generic Extraction Agents** (no domain knowledge):
1. **Definition Extractor** - Identifies definition patterns
2. **Formula Extractor** - Extracts mathematical formulas
3. **Example Extractor** - Identifies worked examples
4. **Citation Extractor** - Builds provenance
5. **Relationship Extractor** - Identifies connections

**Domain-Specific Expert Agents** (guides):
1. **BWL Expert Agent** - Validates finance/accounting content
2. **Math Expert Agent** - Validates mathematical rigor
3. **Merger Agent** - Resolves conflicts between sources
4. **Quality Agent** - Ensures consistency, completeness

### Workflow

```
Source (Textbook/Paper)
        ↓
[Web Scraper Agent] → Raw HTML/PDF
        ↓
[Textbook Parser Agent] → Structured text
        ↓
[Definition Extractor] → Definition AKU candidates
[Formula Extractor] → Formula AKU candidates
[Example Extractor] → Example AKU candidates
        ↓
[Citation Extractor] → Add provenance
[Relationship Extractor] → Link to existing AKUs
        ↓
AKU Candidate Pool
        ↓
[Domain Expert Agent] → Validate, merge, refine
        ↓
[Quality Agent] → Check consistency
        ↓
Validated AKU → Insert into knowledge graph
        ↓
Update indexes (domain, subdomain, topic, concept)
```

---

## Rendering Engine

### Multi-Audience Rendering

**Input**: Query + Audience + Language
```json
{
  "query": "Explain NPV",
  "audience": "high-school",
  "language": "de",
  "format": "markdown",
  "include": ["definition", "simple_example"],
  "exclude": ["proof", "advanced_topics"]
}
```

**Process**:
1. Resolve query → concept (npv)
2. Load concept index
3. Filter AKUs by audience difficulty ≤ high-school
4. Select AKUs: definition + simple examples
5. Apply language translation (en → de)
6. Apply template for markdown format
7. Return rendered document

**Output**: Markdown document explaining NPV for German high-school students

### Template System

```yaml
# rendering-template.yaml
template:
  audience: "high-school"
  language: "de"
  format: "markdown"
  
structure:
  - section: "Definition"
    source: "aku_type:definition"
    transformation: "simplify"
  
  - section: "Intuition"
    source: "aku.content.explanation.intuition"
    
  - section: "Einfaches Beispiel"
    source: "aku_type:example"
    filter: "difficulty ≤ 0.5"
    limit: 1
    
  - section: "Warum ist das wichtig?"
    source: "aku.content.explanation.key_insight"
```

---

## Storage & Performance

### File Organization

```
worldsmegraphs/
├── data/
│   ├── index/
│   │   ├── global-index.yaml     # Root index
│   │   ├── keyword-index.db      # Fast keyword lookup
│   │   └── formula-index.db      # Formula search
│   │
│   ├── domain/
│   │   ├── economics/
│   │   │   ├── bwl/
│   │   │   │   ├── domain-index.yaml
│   │   │   │   ├── finance/
│   │   │   │   │   ├── subdomain-index.yaml
│   │   │   │   │   ├── valuation/
│   │   │   │   │   │   ├── topic-index.yaml
│   │   │   │   │   │   ├── npv/
│   │   │   │   │   │   │   ├── concept-index.yaml
│   │   │   │   │   │   │   ├── akus/
│   │   │   │   │   │   │   │   ├── npv-def-001.json
│   │   │   │   │   │   │   │   ├── npv-formula-001.json
│   │   │   │   │   │   │   │   └── ...
```

### Performance Targets

- **Navigation**: O(log n) = ~5-7 file reads for millions of AKUs
- **Keyword search**: O(1) with inverted index
- **Load time**: <100ms for single AKU
- **Index rebuild**: <10min for 100K AKUs
- **Storage**: ~1KB per AKU → 100GB for 100M AKUs

---

## Comparison: v1 vs v2

| Aspect | v1 (Current) | v2 (Proposed) |
|--------|-------------|---------------|
| Granularity | 58 nodes | 50K-100K AKUs per domain |
| Navigation | Linear scan | O(log n) tree |
| Format | Plain JSON | JSON-LD + indexes |
| Search | None | Keyword + formula indexes |
| Extraction | Manual | Agent-driven research |
| Domain knowledge | Hardcoded | Emergent from content |
| Scalability | Limited | World-scale |
| Performance | Slow | Fast (indexed) |

---

## Next Steps

1. **Implement v2 format** for ONE concept (NPV)
2. **Build extraction pipeline** with generic agents
3. **Create domain expert** agent for validation
4. **Test rendering** for multiple audiences
5. **Measure performance** (navigation, search)
6. **Iterate and refine** based on results

