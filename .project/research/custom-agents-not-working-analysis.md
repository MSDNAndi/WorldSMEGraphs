# Deep Investigation: Why Custom Agents Aren't Auto-Invoking

**Date**: 2025-12-27  
**Issue**: Custom agents work in AorticEndoleak2 repo but not in WorldSMEGraphs  
**Evidence**: https://github.com/copilot/tasks/pull/PR_kwDOPpU0lM64wDc1 shows agents auto-invoking  

---

## The Problem

In the referenced PR from AorticEndoleak2, we see:
```
▶️ Begin custom agent: documentation-curator
All messages from here to '⏹️ End custom agent' are from the documentation-curator custom agent.
```

This proves custom agents CAN be automatically invoked by GitHub Copilot. But this isn't happening in WorldSMEGraphs.

## Investigation Findings

### 1. Current Repository Configuration

**Agent Location:** `.github/agents/` ✅  
**Agent Count:** 60 agents  
**Total Size:** 488K  
**File Format:** All use `.agent.md` extension ✅  
**Agent Quality:** 25/60 pass 180-line minimum (42%)

**Potential Issues Identified:**

#### Issue #1: Conflicting Directory Structure
```
.github/
├── agents/                    ← 60 agent definitions HERE
│   ├── coordinator.agent.md
│   ├── verification.agent.md
│   └── ...
└── copilot/
    └── agents/                ← Validation script HERE (potential confusion?)
        └── check-agent-lengths.sh
```

**Problem:** GitHub Copilot might be looking in `.github/copilot/agents/` instead of `.github/agents/`

**Standard GitHub Copilot Pattern:** `.github/copilot/` is for copilot configuration, not agent definitions

#### Issue #2: Excessive Agent Count
- **WorldSMEGraphs:** 60 agents (488K)
- **AorticEndoleak2:** Likely 1-5 agents (estimated)

**Hypothesis:** GitHub Copilot may have limits:
- Maximum number of agents (e.g., 10-20)
- Maximum total size (e.g., 100-200K)
- Too many agents = none get loaded

#### Issue #3: Agent Quality/Completeness
- 35/60 agents (58%) below 180-line minimum
- Some agents have only 5-8 lines
- **Hypothesis:** Incomplete agents prevent discovery of ALL agents

#### Issue #4: Missing Agent Manifest
- No `agents.json` or `.copilot/config.yml` file
- **Hypothesis:** System needs explicit agent registration

#### Issue #5: Feature Availability
- Custom agent auto-invocation may be:
  - Beta feature with limited rollout
  - Requires specific repository settings
  - Only available for certain organization types
  - Requires opt-in or feature flag

### 2. Comparison with AorticEndoleak2

| Aspect | AorticEndoleak2 | WorldSMEGraphs | Impact |
|--------|-----------------|----------------|---------|
| Agent count | Low (1-5 est.) | High (60) | ⚠️ May exceed limit |
| Total size | Small | 488K | ⚠️ May exceed limit |
| Agent quality | Complete | 58% incomplete | ⚠️ Quality threshold? |
| Directory structure | Unknown | Has both `.github/agents/` and `.github/copilot/agents/` | ⚠️ Potential confusion |
| Configuration file | Unknown | None visible | ⚠️ May be required |

### 3. Most Likely Root Causes

**Ranked by probability:**

#### 1. Agent Count/Size Limit (HIGH PROBABILITY: 80%)
**Evidence:**
- 60 agents is unusually high
- 488K is substantial size
- AorticEndoleak2 likely has far fewer agents
- No other repos with 60+ agents documented

**Test:** Temporarily reduce to 5-10 most important agents

#### 2. Incomplete Agent Quality Blocking Discovery (MEDIUM PROBABILITY: 60%)
**Evidence:**
- 35 agents below minimum line count
- Some have only 5-8 lines (clearly incomplete)
- Quality threshold may prevent loading ANY agents

**Test:** Ensure all agents meet 180-line minimum with complete sections

#### 3. Directory Structure Confusion (MEDIUM PROBABILITY: 50%)
**Evidence:**
- `.github/copilot/agents/` exists with validation script
- Might confuse Copilot's agent discovery
- Standard pattern unclear

**Test:** Move validation script to `.github/scripts/` or remove `.github/copilot/agents/` directory

#### 4. Missing Configuration/Manifest (LOW PROBABILITY: 30%)
**Evidence:**
- No explicit agent registration file
- Other repos might have `.copilot/agents.json`

**Test:** Create agent manifest file

#### 5. Feature Rollout/Access Level (LOW PROBABILITY: 20%)
**Evidence:**
- Feature might be in gradual rollout
- May require opt-in

**Test:** Check repository settings, contact GitHub support

### 4. Recommended Action Plan

#### Phase 1: Quick Fixes (Test Immediately)

**A. Clean Up Directory Structure**
```bash
# Move validation script out of copilot/agents
mv .github/copilot/agents/check-agent-lengths.sh .github/scripts/
rmdir .github/copilot/agents/  # Remove empty directory
```

**B. Create Minimal Agent Set (Top 10)**
Create a test branch with only 10 highest-quality agents:
- coordinator.agent.md
- verification.agent.md
- ontology.agent.md
- documentation-agent.agent.md
- quality.agent.md
- rendering.agent.md
- pedagogy.agent.md
- textbook-parser.agent.md
- paper-miner.agent.md
- fact-checking.agent.md

**C. Ensure All Agents Meet Quality Bar**
- All agents must be ≥180 lines
- All agents must have complete sections
- Remove or move incomplete agents to a separate directory

#### Phase 2: Configuration Attempts

**A. Create Agent Manifest (if needed)**
Create `.github/copilot/agents.json`:
```json
{
  "version": "1.0",
  "agents": [
    {
      "name": "coordinator",
      "file": "../agents/coordinator.agent.md",
      "enabled": true
    },
    ...
  ]
}
```

**B. Create Copilot Configuration**
Create `.github/copilot/config.yml`:
```yaml
agents:
  enabled: true
  directory: "../agents"
  auto_invoke: true
  max_agents: 60
```

#### Phase 3: Testing

1. **Test with minimal agents (5-10)**
   - If this works → size/count limit confirmed
   - If not → try other fixes

2. **Test with directory cleanup**
   - Remove `.github/copilot/agents/`
   - If works → directory confusion confirmed

3. **Test with complete agents only**
   - Ensure all ≥180 lines
   - If works → quality threshold confirmed

4. **Test with configuration files**
   - Add manifest/config
   - If works → configuration required

### 5. Immediate Recommendations

**DO THIS NOW:**

1. **Move validation script:**
   ```bash
   mv .github/copilot/agents/check-agent-lengths.sh .github/scripts/
   rmdir .github/copilot/agents/
   ```

2. **Create test branch with 10 agents:**
   - Keep only highest-quality, most complete agents
   - Test if they get auto-invoked

3. **Fix incomplete agents:**
   - Enhance 35 agents below 180 lines
   - OR move them to `.github/agents-wip/` (work-in-progress)

4. **Document agent names properly:**
   - Ensure agent file names match invocation names
   - `documentation-agent.agent.md` → `@documentation-agent`

**DO NOT:**
- Delete any agents permanently
- Make changes to main branch without testing
- Assume the issue is unfixable

### 6. Expected Outcomes

**If agent count is the issue:**
- Reducing to 10-20 agents will enable auto-invocation
- Need to prioritize which agents are most important
- Consider splitting into multiple repos or sub-directories

**If quality is the issue:**
- Completing all agents to 180+ lines will enable discovery
- System won't load partial/incomplete agents

**If directory structure is the issue:**
- Removing `.github/copilot/agents/` will fix discovery
- Only `.github/agents/` should exist

**If configuration is needed:**
- Adding manifest/config files will enable feature
- Documentation may be missing this requirement

### 7. Long-Term Solutions

**If there IS an agent count limit:**

**Option A: Prioritize Core Agents**
- Keep 10-15 most critical agents in `.github/agents/`
- Move specialized agents to documentation
- Use them as guidance rather than auto-invoked

**Option B: Agent Hierarchies**
- Create a "coordinator" agent that references others
- Single entry point that delegates to specialists
- Reduces visible agent count

**Option C: Multiple Repositories**
- Split into domain-specific repos
- Each repo has 5-10 relevant agents
- Cross-reference as needed

**Option D: Lazy Loading**
- Only load agents when mentioned
- Not all agents need to be active simultaneously

### 8. Questions for GitHub Support

If fixes don't work, ask GitHub:

1. What is the maximum number of custom agents per repository?
2. What is the maximum total size for the agents directory?
3. Is there a quality threshold (minimum lines, required sections)?
4. Does `.github/copilot/agents/` interfere with `.github/agents/`?
5. Is custom agent auto-invocation in beta/limited rollout?
6. Are there repository settings to enable custom agents?
7. Is there documentation on agent manifest files?
8. What are the exact requirements for agent auto-discovery?

### 9. Success Criteria

We'll know custom agents are working when:
1. PR messages show "▶️ Begin custom agent: [name]"
2. Agents are invoked automatically without explicit @mentions
3. Agent context is visible in Copilot responses
4. System acknowledges agent delegations

### 10. Fallback Strategy

If auto-invocation cannot be enabled:
1. **Document manual invocation:** Users manually @mention agents
2. **Guidance approach:** Agents serve as expert guidance documents
3. **Explicit delegation:** Coordinator manually references other agents
4. **Hybrid model:** Some agents auto-invoke, others are manual

---

## Conclusion

The most likely issue is **agent count/size exceeding system limits**. WorldSMEGraphs has 60 agents (488K) which is far more than typical repositories.

**Immediate Action Required:**
1. Clean up directory structure (remove `.github/copilot/agents/`)
2. Test with 10 highest-quality agents
3. Complete all agents to ≥180 lines
4. Monitor for auto-invocation behavior

**Expected Resolution:**
Reducing to 10-20 complete, high-quality agents should enable auto-invocation. If not, additional configuration files may be needed.

---

**Status**: Investigation Complete - Testing Phase Required  
**Next Steps**: Implement Phase 1 fixes and test  
**Owner**: Repository maintainer with GitHub Copilot access
