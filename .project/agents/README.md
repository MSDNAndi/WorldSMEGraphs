# Agent Tooling Infrastructure

This directory contains agent-specific tools, storage, and utilities for the 41-agent system.

## Directory Structure

```
agents/
├── meta-learning/          # Meta-Learning Agent tools
├── quality-assurance/      # QA Agent tools
├── research/               # Research Agent tools
├── extraction/             # Extraction Agents tools
├── generic-domain-empathy/ # Generic Domain Empathy Agent
├── recruiter/              # Recruiter Agent tools
├── coordinator/            # Coordinator Office tools
└── README.md              # This file
```

## Agent Tool Guidelines

### 1. Self-Contained Scripts
- All Python scripts must include dependencies inline or in requirements.txt
- Must run on GitHub Actions runners without manual setup
- Use standard library when possible

### 2. Storage Pattern
```
agent-name/
├── tools/
│   ├── script1.py         # Executable tools
│   └── script2.py
├── storage/
│   ├── metrics/          # Agent-specific data
│   ├── cache/
│   └── logs/
├── requirements.txt      # Python dependencies
└── README.md            # Agent-specific docs
```

### 3. Shared vs. Agent-Specific
- **Agent-specific:** Tools unique to one agent's role
- **Shared:** Common utilities in `.project/tools/`

### 4. Discoverability
- Each agent directory has README.md
- Scripts have docstrings explaining purpose
- Storage locations documented

## Running Agent Tools

```bash
# Navigate to agent directory
cd .project/agents/meta-learning

# Install dependencies (if needed)
pip install -r requirements.txt

# Run tool
python tools/track_metrics.py --domain economics/bwl/finance
```

## Integration with Dynamic SME Framework

Agent tools support the dynamic SME detection and provisioning workflow:
- Meta-Learning tracks extraction success rates
- QA monitors error rates by domain
- Research discovers new domains
- Generic Domain Empathy loads personas and validates

See `.project/research/dynamic_sme_framework.md` for complete workflow.
