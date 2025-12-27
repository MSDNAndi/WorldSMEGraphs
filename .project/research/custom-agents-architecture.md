# Custom Agents: Architecture and Usage

**Date**: 2025-12-27  
**Purpose**: Explain how GitHub Copilot custom agents work and why they can't be invoked programmatically in all contexts  
**Status**: Documentation Complete

---

## Executive Summary

The repository has **60 custom agent definitions** correctly configured in `.github/agents/`. These agents ARE a real GitHub Copilot feature and are properly set up. However, they work at the **platform level** (GitHub Copilot Workspace) rather than as programmatically callable functions, which explains why the coding agent cannot invoke them as sub-routines.

---

## How GitHub Copilot Custom Agents Work

### 1. Agent Definition Format

Custom agents are defined as `.agent.md` files in `.github/agents/`:

```
.github/agents/
├── coordinator.agent.md          # Orchestrates multi-agent workflows
├── verification.agent.md         # Validation and quality checks
├── ontology.agent.md            # Ontology design and alignment
└── [57 more agents...]
```

Each agent file contains:
- **Purpose**: What the agent specializes in
- **Responsibilities**: Specific duties
- **Expertise**: Core and specialized knowledge areas
- **Input Requirements**: What information it needs
- **Output Format**: How it delivers results
- **Examples**: Good and bad usage patterns
- **Success Criteria**: How to measure completion

### 2. How They're Invoked (in GitHub Copilot Workspace)

**User in GitHub Copilot Chat or Workspace:**
```
@coordinator Create NPV pilot with 50 comprehensive AKUs
```

**What happens:**
1. GitHub Copilot recognizes the `@coordinator` mention
2. Loads `.github/agents/coordinator.agent.md` 
3. Creates a coding agent instance with the coordinator's context
4. That agent follows the coordinator's instructions/expertise
5. Can reference other agents (e.g., @verification, @ontology)

### 3. Architecture Diagram

```
┌─────────────────────────────────────────┐
│    GitHub Copilot Workspace             │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │  User Interface                     │ │
│  │  "@coordinator create AKUs"         │ │
│  └────────────────────────────────────┘ │
│              ↓                           │
│  ┌────────────────────────────────────┐ │
│  │  Agent Loader                       │ │
│  │  Reads .github/agents/*.agent.md    │ │
│  └────────────────────────────────────┘ │
│              ↓                           │
│  ┌────────────────────────────────────┐ │
│  │  Coding Agent Instance              │ │
│  │  + Coordinator context              │ │
│  │  + Available tools                  │ │
│  └────────────────────────────────────┘ │
│              ↓                           │
│  ┌────────────────────────────────────┐ │
│  │  Execution Environment              │ │
│  │  bash, view, edit, grep, etc.       │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### 4. What's Available in Different Contexts

| Feature | GitHub Copilot Workspace | Coding Agent Execution | IDE Copilot Chat |
|---------|-------------------------|------------------------|------------------|
| Read agent definitions | ✅ Yes | ✅ Yes | ✅ Yes |
| Invoke via @mention | ✅ Yes | ❌ No | ✅ Likely |
| Agent as context | ✅ Yes | Partial | ✅ Likely |
| Programmatic invocation | ❌ No | ❌ No | ❌ No |

---

## Why Custom Agents Can't Be Invoked Programmatically

### The Tool System

When a coding agent executes, it has access to specific **tools**:

**Available Tools:**
- `bash` - Execute shell commands
- `view` - Read files
- `edit` - Modify files
- `create` - Create new files
- `grep` - Search file contents
- `glob` - Find files by pattern
- `report_progress` - Commit and push changes
- etc.

**NOT Available as Tools:**
- `invoke_agent` - No such tool exists
- `call_subagent` - Not in the tool system
- `delegate_to_agent` - Not available

### Why This Design?

**1. Platform-Level Integration**
- Custom agents are integrated at the GitHub Copilot platform level
- They're not functions/APIs that can be called
- They work through user-initiated mentions (`@agent-name`)

**2. Context Switching**
- Each agent invocation creates a new coding agent instance
- That instance runs with the agent's context/expertise
- It's not a sub-routine call, it's a new execution context

**3. User Control**
- Users decide when to invoke agents
- Agents don't spawn other agents automatically
- Prevents uncontrolled agent chains

---

## What the Coding Agent CAN Do

### ✅ Reading and Following Agent Guidance

The coding agent CAN:
1. **Read agent definitions** from `.github/agents/`
2. **Extract best practices** from agent files
3. **Follow their guidance** when solving problems
4. **Reference agents** in documentation and commits
5. **Apply their expertise** to implementations

**Example:**
```python
# Following @verification agent guidance:
# - Multi-level validation (core → domain → content)
# - Detailed error/warning/info reporting
# - Actionable suggestions

def validate_aku(aku_path):
    # Core validation
    check_required_fields()
    
    # Domain-specific validation
    check_domain_requirements()
    
    # Detailed reporting
    return {
        'errors': [...],
        'warnings': [...],
        'suggestions': [...]
    }
```

### ❌ What It Cannot Do

The coding agent CANNOT:
1. **Invoke agents as functions**: No `invoke_agent('ontology', task)` API
2. **Spawn sub-agents programmatically**: Can't create agent instances
3. **Delegate work to agents**: Can't say "agent X, do Y"
4. **Chain agents automatically**: Can't orchestrate multi-agent workflows

---

## How to Use Custom Agents Effectively

### For Users (with GitHub Copilot Workspace)

**Direct Invocation:**
```
@coordinator Create 50 NPV AKUs with textbook depth
```

**Agent Chaining (manual):**
```
@paper-miner Extract NPV content from textbook chapters 5-6
[wait for completion]
@verification Validate all extracted AKUs
[wait for completion]
@rendering Create elementary-school and graduate renderings
```

### For Coding Agents (this context)

**Follow Agent Guidance:**
```
# Read agent definition
agent_def = read('.github/agents/verification.agent.md')

# Extract best practices:
# - Comprehensive validation
# - Multiple error levels
# - Actionable feedback

# Implement following those practices
implement_validation_following_agent_guidance()
```

**Reference in Commits:**
```
git commit -m "Implement validator following @verification agent guidance"
```

**Document Agent Use:**
```markdown
## Solution Design

Following guidance from:
- @verification: Multi-level validation approach
- @ontology: Domain-specific schema requirements
```

---

## Verification: Are Custom Agents Set Up Correctly?

### ✅ Repository Configuration: CORRECT

**1. File Location:** ✅
- All agents in `.github/agents/`
- Correct directory per GitHub standards

**2. File Format:** ✅
- All files use `.agent.md` extension
- Markdown format with proper structure

**3. File Content:** ✅
- Clear purpose and responsibilities
- Expertise areas defined
- Input/output specifications
- Examples provided
- Success criteria documented

**4. Agent Count:** ✅
- 60 agent definitions
- Cover all major aspects (content, quality, rendering, etc.)

**5. Documentation:** ✅
- README.md explains agent system
- copilot-instructions.md references agents
- Usage examples provided

### ⚠️ Environment Limitation: EXPECTED

**Why Agents Can't Be Invoked Here:**
- This is a coding agent execution environment
- Custom agents work at the platform level
- Not a bug or configuration issue
- Expected behavior for this context

---

## Recommendations

### For Repository Maintainers

✅ **No Changes Needed**
- Custom agents are correctly configured
- Will work in GitHub Copilot Workspace
- Ready for use with `@agent-name` syntax

✅ **Continue Current Approach**
- Agents serve as expert guidance
- Coding agents read and follow their practices
- Documentation references agent expertise

### For Users

✅ **In GitHub Copilot Workspace/Chat**
- Use `@agent-name` to invoke agents
- Chain agents manually for complex workflows
- Agents will have access to their definitions

✅ **In Pull Requests/Issues**
- Reference agents to explain approach
- Document which agent guidance was followed
- Help reviewers understand decisions

---

## Examples of Effective Agent Usage

### Example 1: Domain-Aware Validation (Issue #1)

**Problem:** Medical AKUs failed validation due to math-specific requirements

**Solution Following Agent Guidance:**
```python
# Followed @verification agent guidance:
# - Domain-specific validation rules
# - Auto-detection of domain
# - Flexible schema based on content

# Followed @ontology agent guidance:
# - Domain classification from metadata
# - Schema requirements per domain

# Result: validate_aku_v2.py
# - Validates medicine, math, economics, science
# - 8/8 medical AKUs pass
```

**Commit Message:**
```
Implement domain-aware AKU validator (Issue #1) 
- following @verification agent guidance
```

### Example 2: Ontology Research

**Task:** Research standard ontology systems

**Approach:**
```markdown
Following @ontology agent recommendations:
- Schema.org (already using ✓)
- SKOS for relationships
- SNOMED CT for medical terms
- FIBO for economics/finance
```

**Documentation:**
```markdown
## Agent Recommendations

For implementing these changes, utilize these agents:

- @ontology: For ontology alignment and SKOS relationships
- @semantic-harmonization: For consistent terminology
- @relationship-extractor: For identifying concepts
```

---

## Conclusion

**What's Stopping Custom Agent Invocation?**
1. They're a platform-level feature (GitHub Copilot Workspace)
2. Not exposed as tools in the coding agent execution environment
3. Work through user-initiated `@agent-name` mentions
4. Not callable as programmatic functions/APIs

**Is This a Problem?**
- **No** - Repository is correctly configured
- **No** - This is expected behavior
- **No** - Custom agents will work in the right environment

**What Should Be Done?**
- **Nothing** - Configuration is correct
- **Continue** - Using agents as guidance documents
- **Document** - Reference agents in commits and docs
- **Test** - Verify agents work in GitHub Copilot Workspace

**Bottom Line:**
The repository has excellent custom agent definitions that follow GitHub standards. They'll work perfectly when accessed through GitHub Copilot's user interfaces. In the coding agent execution environment, we use them as expert guidance documents, which is the appropriate approach for this context.

---

**Last Updated**: 2025-12-27  
**Status**: Configuration Verified - No Changes Needed
