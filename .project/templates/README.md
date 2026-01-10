# AKU Templates Library

This directory contains high-quality templates for creating new AKUs across different domains.

## Available Templates

### 1. economics-template.json
**For**: Economics, Finance, Business concepts
**Grade Target**: B+ (0.85+)
**Features**:
- Mathematical formulations
- Policy implications
- Historical context
- Measurement methodology
- 4 diverse examples
- 6 authoritative sources

**Use when creating**:
- Macroeconomic concepts
- Microeconomic principles
- Financial instruments
- Economic indicators
- Market structures

### 2. mathematics-template.json (Coming Soon)
**For**: Pure and applied mathematics
**Features**:
- Theorem statements
- Proofs or proof sketches
- Multiple worked examples
- Connections to other areas
- Applications

### 3. medicine-template.json (Coming Soon)
**For**: Medical concepts, diseases, procedures
**Features**:
- Evidence-based content
- Clinical guidelines
- Diagnostic criteria
- Treatment protocols
- Safety considerations

### 4. engineering-template.json (Coming Soon)
**For**: Engineering principles and applications
**Features**:
- Design specifications
- Calculation examples
- Industry standards
- Safety requirements
- Practical applications

### 5. physics-template.json (Coming Soon)
**For**: Physics concepts and theories
**Features**:
- Mathematical models
- Experimental validation
- Measurement techniques
- Uncertainty analysis
- Historical development

## How to Use Templates

1. **Copy the appropriate template**:
   ```bash
   cp .project/templates/economics-template.json domain/social-sciences/economics/subdomain/akus/your-aku.json
   ```

2. **Replace placeholder text**:
   - Search for UPPERCASE_PLACEHOLDERS
   - Fill in ALL required fields
   - Remove placeholder text

3. **Customize for your concept**:
   - Add domain-specific content
   - Include relevant examples
   - Update all sources
   - Verify ontology links

4. **Validate**:
   ```bash
   python .project/agents/quality-assurance/tools/comprehensive_quality_assessment.py \
     domain/path/to/your-aku.json --level comprehensive
   ```

5. **Iterate until target grade achieved**:
   - D grade (0.60+): Minimum acceptable
   - C grade (0.70+): Good quality
   - B grade (0.80+): High quality
   - A grade (0.90+): Excellent quality

## Template Standards

All templates follow these standards:
- Version 3.0.0 format
- Complete metadata
- Full taxonomy paths
- Ontology integration
- Minimum 6 sources
- Comprehensive glossary (8 terms)
- Multiple examples (4+)
- Detailed explanations

## Creating New Templates

To create a template for a new domain:
1. Review several high-quality AKUs from that domain
2. Identify common structure and required fields
3. Include domain-specific requirements
4. Add helpful placeholder text
5. Document in this README
6. Submit for review

## Quality Targets

Templates are designed to achieve:
- **Minimum**: D grade (0.60) - all required fields
- **Target**: B grade (0.80) - comprehensive content
- **Stretch**: A grade (0.90) - research-level quality

## Support

See:
- `.project/AKU-QUALITY-STANDARDS.md` - Complete quality standards
- `.project/knowledge-format.md` - Format specification
- `.project/AKU-QUALITY-ENHANCEMENT-REPORT.md` - Enhancement project results

---

**Last Updated**: 2026-01-10
**Maintained By**: Quality Assurance Team
