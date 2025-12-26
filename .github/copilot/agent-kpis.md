# Agent Performance Tracking System

## Overview
This system tracks agent performance through Key Performance Indicators (KPIs) to ensure quality and identify agents needing improvement or replacement.

## Performance Review Cycle
Each agent undergoes performance reviews:
- **Review Frequency**: After every 10 tasks or monthly (whichever comes first)
- **Improvement Threshold**: 5 review cycles without improvement
- **Action**: Replace or completely redesign underperforming agents

## KPI Categories

### 1. Quality Metrics
- **Accuracy**: Correctness of output
- **Completeness**: Thoroughness of work
- **Consistency**: Reliability across tasks
- **Target**: >95% quality score

### 2. Efficiency Metrics
- **Time to Complete**: Duration for typical tasks
- **Resource Usage**: Computational/human resources needed
- **Throughput**: Tasks completed per time period
- **Target**: Completion within expected timeframes

### 3. Improvement Metrics
- **Feedback Response**: How well agent incorporates feedback
- **Issue Resolution**: Fixes for problems identified
- **Learning Curve**: Improvement over time
- **Target**: Measurable improvement each cycle

### 4. Reliability Metrics
- **Success Rate**: Percentage of tasks completed successfully
- **Error Rate**: Frequency of mistakes or failures
- **Consistency**: Variation in quality across tasks
- **Target**: >98% success rate

## Agent Performance Log

### Template
```yaml
agent_name: [agent-name]
version: [version]
last_reviewed: [date]
review_cycle: [number]
performance_score: [0-100]
status: [active|under-review|needs-improvement|scheduled-for-replacement]

kpis:
  quality_score: [0-100]
  efficiency_score: [0-100]
  improvement_score: [0-100]
  reliability_score: [0-100]

tasks_completed: [number]
issues_identified: [number]
issues_resolved: [number]

improvement_actions:
  - [action taken]
  - [action taken]

notes: |
  [Additional observations]
```

## Current Agent Performance

### Knowledge Graph Agent
```yaml
agent_name: knowledge-graph-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

### Documentation Agent
```yaml
agent_name: documentation-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

### Code Review Agent
```yaml
agent_name: code-review-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

### Contrarian Agent
```yaml
agent_name: contrarian-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

### Rendering Agent
```yaml
agent_name: rendering-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

### File Organization Agent
```yaml
agent_name: file-organization-agent
version: 1.0
last_reviewed: 2025-12-26
review_cycle: 0
performance_score: N/A (new agent)
status: active
tasks_completed: 0
notes: Newly deployed, awaiting first tasks
```

## Improvement Process

### When Performance Issues Are Identified
1. **Document the Issue**: Record specific problems and their impact
2. **Root Cause Analysis**: Understand why the agent underperformed
3. **Improvement Plan**: Define specific actions to address issues
4. **Implementation**: Update agent instructions/prompts
5. **Re-evaluation**: Test agent on similar tasks
6. **Track Progress**: Monitor if improvements are effective

### After 5 Unsuccessful Improvement Cycles
- **Complete Redesign**: Start from scratch with new approach
- **Agent Replacement**: Deploy competing agent with different strategy
- **Competitive Selection**: Let multiple agents compete, keep the best

## Agent Competition Framework

### When to Enable Competition
- After 5 unsuccessful improvement cycles
- When trying new approaches
- For critical/high-impact tasks
- When multiple valid strategies exist

### Competition Process
1. Deploy 2-3 competing agents with different approaches
2. Assign same tasks to all competing agents
3. Compare results using standardized metrics
4. Select best-performing agent
5. Retire underperforming agents
6. Document lessons learned

## Reporting

### Monthly Performance Report
Generate report including:
- Agent performance scores
- Tasks completed by each agent
- Issues found and resolved
- Agents under review
- Improvement actions taken
- Agents scheduled for replacement

### Quarterly Strategic Review
- Overall agent effectiveness
- System-wide improvements
- New agent needs identified
- Retired agents and reasons
- Success stories and best practices

## Updating This Document
- Update agent performance after each review cycle
- Add new agents as they are created
- Document all improvement actions
- Track replacement decisions and outcomes
- Maintain historical performance data
