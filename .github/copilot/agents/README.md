# Agent Directory

> **Overview**: Specialized Copilot agents available for WorldSMEGraphs project

## Quick Reference

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| [Knowledge Graph Agent](knowledge-graph-agent.md) | Create/maintain knowledge graphs | Creating new domains, validating graphs |
| [Documentation Agent](documentation-agent.md) | Manage documentation | Writing/updating docs, finding contradictions |
| [Code Review Agent](code-review-agent.md) | Quality assurance | Before PR submission, quality checks |
| [Contrarian Agent](contrarian-agent.md) | Critical analysis | Design decisions, challenging assumptions |
| [Rendering Agent](rendering-agent.md) | Generate human-readable content | Creating renderings for audiences |
| [File Organization Agent](file-organization-agent.md) | Maintain structure | Finding redundancies, organizing files |
| [Domain Expert Template](domain-expert-template.md) | Domain-specific expertise | Subject matter validation |

## How to Use Agents

### Basic Syntax
```
@[agent-name] [specific request with context]
```

### Examples

#### Request Knowledge Graph Creation
```
@knowledge-graph-agent Create a knowledge graph for domain/science/math/geometry
covering points, lines, angles, triangles, and circles. Include cross-links to algebra
for coordinate geometry.
```

#### Request Documentation Review
```
@documentation-agent Review all documentation in docs/ directory.
Check for contradictions, outdated information, and broken cross-references.
Suggest consolidations where appropriate.
```

#### Request Code Review
```
@code-review-agent Review the knowledge graph validation script in tools/validate.py.
Focus on error handling, edge cases, and code clarity.
```

#### Request Critical Analysis
```
@contrarian-agent Challenge the proposed rendering system architecture.
What are the weaknesses? What could go wrong at scale?
What alternative approaches should we consider?
```

#### Request Rendering Generation
```
@rendering-agent Generate a high school level rendering in English
for domain/economics/macroeconomics/knowledge.graph.
Focus on making abstract economic concepts concrete with current examples.
```

#### Request File Organization Review
```
@file-organization-agent Review the entire project structure.
Identify redundancies, misplaced files, and organizational improvements.
Update structure documentation after making changes.
```

## Agent Selection Guide

### For Knowledge Creation
- **Primary**: Knowledge Graph Agent
- **Support**: Domain Expert Agent (for validation)
- **Review**: Contrarian Agent (for critique)

### For Documentation
- **Primary**: Documentation Agent
- **Support**: File Organization Agent (for structure)
- **Review**: Code Review Agent (for quality)

### For Code/Tools
- **Primary**: Code Review Agent
- **Support**: Contrarian Agent (for approach)
- **Review**: Documentation Agent (for docs)

### For Quality Assurance
- **Primary**: Code Review Agent
- **Secondary**: Contrarian Agent
- **Final**: Documentation Agent (docs check)

### For Renderings
- **Primary**: Rendering Agent
- **Support**: Domain Expert Agent (accuracy)
- **Review**: Documentation Agent (consistency)

### For Structure/Organization
- **Primary**: File Organization Agent
- **Review**: Documentation Agent (doc updates)

## Best Practices

### 1. Be Specific
Bad: `@rendering-agent Create a rendering`
Good: `@rendering-agent Create an elementary school English rendering of domain/science/math/algebra/knowledge.graph focusing on variables and equations`

### 2. Provide Context
Include:
- What you're trying to achieve
- Any constraints or requirements
- Related work or dependencies
- Target audience or use case

### 3. Use Multiple Agents
For complex tasks:
1. Use primary agent for main work
2. Use contrarian agent for critique
3. Use code review agent for quality
4. Iterate based on feedback

### 4. Review Agent Output
- Don't blindly accept agent suggestions
- Validate accuracy and appropriateness
- Iterate if needed
- Learn from agent approaches

### 5. Track Agent Performance
- Note what works well
- Document issues or failures
- Update agent instructions based on experience
- Report persistent problems for agent improvement

## Creating New Agents

When you need a new specialized agent:

1. **Identify Need**
   - What expertise is lacking?
   - Would a specialized agent help?
   - Is it a recurring need?

2. **Use Template**
   - Copy appropriate template
   - Customize for specific domain/task
   - Define clear responsibilities
   - Set quality criteria

3. **Define KPIs**
   - How will you measure success?
   - What metrics matter?
   - How to track improvement?

4. **Document Agent**
   - Create agent configuration file
   - Add to this index
   - Update main instructions
   - Add to agent KPIs tracking

5. **Test and Iterate**
   - Try agent on sample tasks
   - Gather feedback
   - Refine instructions
   - Update based on performance

## Agent Performance

See [Agent KPIs](agent-kpis.md) for detailed performance tracking.

### Current Status (All Agents)
- **Status**: Active
- **Version**: 1.0
- **Review Cycle**: 0 (newly deployed)
- **Performance**: Awaiting first tasks

### Review Schedule
- First review: After 10 tasks or 1 month
- Regular reviews: Monthly
- Improvement cycles: Up to 5 before replacement

## Requesting New Agents

If you need an agent that doesn't exist:

1. **Check if existing agent can be adapted**
2. **Document the need**:
   - What tasks would it handle?
   - What expertise is required?
   - How would it differ from existing agents?
3. **Create proposal**:
   - Agent purpose and responsibilities
   - Expected KPIs
   - When to use it
4. **Submit for review**
5. **Create agent configuration** if approved

## Agent Improvement Process

If an agent is underperforming:

1. **Document Issues**
   - What went wrong?
   - What was expected vs. actual?
   - Impact of the problem

2. **Root Cause Analysis**
   - Why did it underperform?
   - Is it instruction clarity?
   - Is it capability limitation?

3. **Propose Improvements**
   - Updated instructions
   - Refined responsibilities
   - Better examples
   - Clearer quality criteria

4. **Implement and Test**
   - Update agent configuration
   - Test on similar tasks
   - Verify improvement

5. **Track Progress**
   - Update KPI tracking
   - Document improvement cycle
   - Monitor ongoing performance

6. **Replace if Necessary**
   - After 5 unsuccessful improvement cycles
   - Complete redesign or replacement
   - Document lessons learned

## Related Documents
- [Copilot Instructions](../copilot-instructions.md)
- [Agent KPIs](agent-kpis.md)
- [Individual Agent Configurations](.)

---

**Note**: Agents are tools to enhance productivity. Use them wisely, review their output, and help improve them through feedback.
