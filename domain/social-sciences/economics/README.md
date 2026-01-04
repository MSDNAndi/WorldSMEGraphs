# Economics

> **Domain Path**: `social-sciences/economics/`  
> **Parent Domain**: Social Sciences  
> **Version**: 1.0.0  
> **Migrated**: 2026-01-04

## Overview

Economics is the social science that studies the production, distribution, and consumption of goods and services. It examines how individuals, businesses, governments, and nations make choices about allocating resources to satisfy wants and needs.

## Content in This Directory

This directory contains **1 successfully migrated AKU** with **11 AKUs pending manual fix** (missing classification.domain_path field).

### Current Content (1 AKU)

**Net Present Value (NPV)**
- **Location**: `bwl/finance/valuation/npv/`
- **Content**: Example NPV definition with semantic annotations
- **Status**: ✅ Migrated successfully
- **Domain Path**: `social-sciences/economics/bwl/finance/valuation/npv`

### Pending Content (11 AKUs)

**Issue**: 11 economics AKUs in the legacy `economics/` location lack the `classification.domain_path` field, which prevented automated migration.

**Location**: `economics/bwl/` subdirectories (legacy location)

**Action Required**: Manual addition of classification section:
```json
{
  "classification": {
    "domain_path": "social-sciences/economics/appropriate/path",
    "type": "definition|formula|example",
    "difficulty": "undergraduate|graduate|professional",
    "importance": "foundational|important|specialized"
  }
}
```

After adding classification, re-run migration:
```bash
python domain/_ontology/tools/migrate_domain.py \
  --source economics \
  --target social-sciences/economics
```

## Planned Subdomain Structure

### Microeconomics
Study of individual economic units (consumers, firms, markets)

**Topics**:
- Supply and Demand
- Consumer Theory (utility, preferences)
- Producer Theory (costs, production functions)
- Market Structures (perfect competition, monopoly, oligopoly)
- Game Theory

### Macroeconomics  
Study of economy-wide phenomena

**Topics**:
- National Income Accounting (GDP, GNP)
- Inflation and Unemployment
- Monetary Policy
- Fiscal Policy
- Economic Growth

### Financial Economics
Study of resource allocation over time under uncertainty

**Topics**:
- **Valuation** (NPV, IRR, DCF) - ✅ 1 AKU present
- Asset Pricing (CAPM, APT)
- Corporate Finance (capital structure, dividends)
- Portfolio Theory
- Derivatives and Options

### Econometrics
Statistical methods in economics

**Topics**:
- Regression Analysis
- Time Series Analysis
- Panel Data Methods
- Causal Inference

### Behavioral Economics
Psychology and economics intersection

**Topics**:
- Cognitive Biases
- Heuristics
- Prospect Theory
- Nudges and Choice Architecture

## Migration Details

### Source and Target
- **Source**: `economics/` (legacy flat location)
- **Target**: `social-sciences/economics/` (new hierarchical location)
- **Migration Date**: 2026-01-04
- **Tool Used**: `domain/_ontology/tools/migrate_domain.py`

### Migration Results
- **Total AKUs Found**: 12
- **Successfully Migrated**: 1 (8.3%)
- **Skipped**: 11 (missing classification.domain_path)
- **Failed**: 0

The low migration rate is due to pre-existing data quality issues in the legacy economics AKUs, not a problem with the migration process.

### What Was Migrated
The single successfully migrated AKU demonstrates:
- ✅ Updated domain_path: `economics/bwl/finance/valuation/npv` → `social-sciences/economics/bwl/finance/valuation/npv`
- ✅ Added `isNativeDomain: true` marker
- ✅ Updated `modified` timestamp: 2026-01-04

## Cross-Domain Applications

Economics provides analytical frameworks for many other domains:

### Business & Management
- Corporate strategy and decision-making
- Financial analysis and valuation
- Market analysis and pricing

### Public Policy
- Policy design and evaluation
- Cost-benefit analysis
- Regulatory economics

### Engineering
- Operations research and optimization
- Resource allocation
- System efficiency

### Health Sciences
- Health economics and cost-effectiveness
- Healthcare policy
- Insurance design

### Natural Sciences
- Environmental economics
- Resource economics
- Energy economics

## Native Domain Status

Economics concepts belong here even when applied elsewhere:

| Concept | Native Domain | Application Domains |
|---------|---------------|---------------------|
| NPV | Economics / Financial Economics | Engineering (project evaluation), Business (investment decisions) |
| Game Theory | Economics | Computer Science (algorithmic game theory), Biology (evolutionary strategies) |
| Supply & Demand | Economics | Engineering (capacity planning), Business (inventory management) |
| Optimization | Economics | Engineering (operations research), Mathematics (optimization theory) |

## Validation

Economics AKUs can be validated using:

```bash
# Validate all economics AKUs
python .project/agents/quality-assurance/tools/validate_aku_v2.py \
  --domain economics \
  --directory domain/social-sciences/economics/

# Check cross-domain references
python domain/_ontology/tools/validate_cross_domain.py \
  --directory domain/social-sciences/economics/
```

**Current Status**: 1/1 migrated AKU validates successfully

## Contributing

When adding economics AKUs:

1. **Ensure Economics Focus**: Concepts should relate to economic behavior, markets, resources
2. **Place Correctly**: Use appropriate subdomain (micro, macro, financial, etc.)
3. **Mark as Native**: Set `isNativeDomain: true`
4. **Cite Sources**: Reference economic literature, textbooks, research papers
5. **Include Classification**: **REQUIRED** - Must have classification.domain_path
6. **Follow AKU Format**: Use AKU v2.0 specification

### Classification Template
```json
{
  "classification": {
    "domain_path": "social-sciences/economics/subdomain/topic",
    "type": "definition|formula|example|theorem",
    "difficulty": "undergraduate|graduate|professional",
    "importance": "foundational|important|specialized",
    "maturity": "draft|stable|validated"
  }
}
```

## Known Issues

### 🔴 Critical: 11 AKUs Missing Classification
**Issue**: 11 economics AKUs in legacy location lack classification.domain_path field

**Impact**: Cannot be automatically migrated

**Location**: `economics/bwl/` subdirectories

**Solution**:
1. Add classification section to each AKU
2. Specify appropriate domain_path
3. Re-run migration tool
4. Validate migrated content

**Priority**: High - blocking full economics migration

## References

### Economics Resources
- American Economic Association (AEA)
- National Bureau of Economic Research (NBER)
- Journal of Economic Literature (JEL) Classification System

### Standards
- JEL Classification Codes
- Financial Industry Business Ontology (FIBO)
- International Standard Industrial Classification (ISIC)

### Related Documents
- Parent: `domain/social-sciences/README.md`
- Ontology: `domain/_ontology/global-hierarchy.yaml`
- Context: `domain/_contexts/economics.jsonld`
- Migration: `domain/_ontology/MIGRATION-SUMMARY.md`

---

**Status**: Partial - 1 AKU present, 11 pending manual fix  
**Quality**: Successfully migrated content validated  
**Priority**: Complete migration of remaining 11 AKUs

**Questions?** See parent `social-sciences/README.md` or `domain/_ontology/README.md`
