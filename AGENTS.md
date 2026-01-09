# AGENTS.md

> **Standard**: [AGENTS.md](https://agents.md) - Open format for guiding coding agents  
> **Version**: 1.0.0  
> **Updated**: 2026-01-09

## Project Overview

WorldSMEGraphs is a file-based knowledge representation system for subject matter expert domains. This project creates an interconnected, language-agnostic knowledge graph that can be rendered in multiple formats and languages for different audiences.

## Dev Environment Setup

```bash
# Clone repository
git clone https://github.com/MSDNAndi/WorldSMEGraphs.git
cd WorldSMEGraphs

# No external dependencies required - uses Python standard library only
python --version  # Python 3.8+ required
```

## Build & Validation Commands

### Validate AKUs (Atomic Knowledge Units)

```bash
# Validate single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py path/to/aku.json

# Validate all AKUs in a domain
python .project/agents/quality-assurance/tools/validate_aku_v2.py --domain medicine

# Validate directory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory path/to/akus/
```

### Validate Cross-Domain Linking

```bash
# Validate cross-domain compliance
python domain/_ontology/tools/validate_cross_domain.py path/to/aku.json
```

### Validate Agents

```bash
# Check agent frontmatter format
bash .github/scripts/validate-agent-format.sh

# Check agent line counts (180+ lines required)
bash .github/scripts/check-agent-lengths.sh
```

### Validate Project Structure

```bash
bash .github/scripts/validate-structure.sh
```

## Testing Instructions

- Run validation scripts before committing changes
- All AKUs must pass JSON schema validation
- Agent files must have valid YAML frontmatter
- Cross-domain links must point to valid paths

## Code Style

- **Markdown**: ATX-style headers, fenced code blocks with language tags
- **JSON**: 2-space indentation, double quotes for strings
- **Python**: Standard library only, clear docstrings, self-contained scripts
- **Writing**: Clear, concise language; define terms before use

## Project Structure

```
WorldSMEGraphs/
├── .github/
│   ├── agents/              # 61 Copilot custom agents (.agent.md files)
│   ├── copilot/             # Copilot instructions and KPIs
│   ├── scripts/             # Validation scripts
│   └── workflows/           # CI/CD workflows
├── domain/                   # Knowledge domain hierarchies
│   ├── _ontology/           # Global hierarchy and cross-domain tools
│   ├── formal-sciences/     # Math, CS, Logic
│   ├── natural-sciences/    # Physics, Chemistry, Biology
│   ├── social-sciences/     # Economics, Psychology
│   └── health-sciences/     # Medicine
├── renders/                  # Centralized rendered content
│   ├── by-domain/
│   ├── by-language/
│   └── by-audience/
├── docs/                     # Documentation
│   ├── agents/              # Agent documentation
│   └── tutorials/           # How-to guides
├── .project/                 # Project tracking and planning
└── AGENTS.md                 # This file
```

## Custom Agents

WorldSMEGraphs uses 61 specialized GitHub Copilot agents located in `.github/agents/`. Key agents include:

### Core Agents
- `@coordinator` - Orchestrate multi-agent workflows
- `@quality` - Comprehensive QA validation
- `@recruiter` - Agent capability matching

### Content Extraction
- `@paper-miner` - Extract from research papers
- `@textbook-parser` - Extract from textbooks
- `@definition-extractor` - Extract formal definitions

### Validation
- `@fact-checking` - Verify factual accuracy
- `@peer-review` - Quality review
- `@verification` - Formal proof checking

### Rendering
- `@rendering-agent` - Transform for audiences
- `@accessibility` - WCAG compliance
- `@localization` - Language/culture adaptation

See `.github/agents/README.md` for the complete list.

## Invoking Agents

```
@agent-name [specific request with context]
```

### Examples

```
@paper-miner Extract NPV formulas from "Corporate Finance" chapters 5-6

@fact-checking Verify all statistics in economics AKUs

@rendering-agent Create elementary school rendering of algebra concepts
```

## Commit Message Guidelines

- **During work**: Use "Progress report: [description]" prefix
- **Session end**: Use "SESSION COMPLETE: [description]" prefix
- Be descriptive about what changed

## PR Guidelines

1. Run all validation scripts before PR
2. Update relevant documentation if structure changes
3. Ensure all AKUs pass validation
4. Keep changes focused and minimal

## Security Considerations

- Never commit secrets or API keys
- Use environment variables for sensitive configuration
- See `.github/copilot-instructions.md` for security guidelines

## Links

- [Agent Documentation](docs/agents/AGENTS-GUIDE.md)
- [Contributing Guide](docs/CONTRIBUTING.md)
- [Project Roadmap](.project/roadmap.md)
- [GitHub Copilot Instructions](.github/copilot-instructions.md)
