# Example: Splitting an Over-Bundled NPV AKU

This example demonstrates how the AKU Atomicity Specialist would split an over-bundled AKU into atomic units.

## Problem: Over-Bundled AKU

**File**: `aku-npv-complete.json` (example)  
**Issue**: Contains 8 distinct concepts in a single AKU  
**Atomicity Score**: 0.30 / 1.0 (severely over-bundled)

**Detected Concepts**:
1. NPV Definition
2. NPV Formula
3. Decision Rule
4. Components (CF, r, I₀, t)
5. Worked Example
6. Advantages
7. Limitations
8. Applications

## Recommended Split Plan

### Split into 8 Atomic AKUs

#### AKU 1: NPV Definition
**File**: `aku-npv-definition.json`  
**@id**: `economics:finance:npv:definition-v1`  
**Concept**: Core definition of Net Present Value  
**Prerequisites**: 
- `economics:finance:time-value-of-money`
- `economics:finance:present-value:concept`

**Content**:
- Primary definition
- Technical definition  
- Simple definition
- Context and purpose

**Atomicity**: 1.0 (exactly one concept)

---

#### AKU 2: NPV Formula
**File**: `aku-npv-formula.json`  
**@id**: `economics:finance:npv:formula-v1`  
**Concept**: Mathematical formula for NPV calculation  
**Prerequisites**:
- `economics:finance:npv:definition-v1`

**Content**:
- Standard formula
- LaTeX representation
- Notation guide

**Atomicity**: 1.0 (exactly one concept)

---

## Transformation Process

### Step 1: Analyze Atomicity
```bash
python .project/agents/atomicity-specialist/tools/analyze_atomicity.py aku-npv-complete.json --verbose
```

### Step 2: Generate Split Plan
```bash
@aku-atomicity-specialist Generate split plan for aku-npv-complete.json 
with 8 atomic units.
```

### Step 3: Create New AKU Files
For each concept, create new JSON file with proper structure and relationships.

### Step 4: Validate Split AKUs
```bash
python .project/agents/quality-assurance/tools/validate_aku_v2.py *.json
```

### Step 5: Verify Atomicity
```bash
python .project/agents/atomicity-specialist/tools/analyze_atomicity.py --directory .
```

Expected: All 8 new AKUs score 1.0 (atomic)

---

## Benefits of Splitting

### Learning Effectiveness
- **Focused Learning**: Each AKU teaches one concept clearly
- **Reduced Cognitive Load**: Smaller, digestible units
- **Clear Prerequisites**: Explicit learning path

### Assessment Granularity
- **Precise Testing**: Test understanding of specific concepts
- **Targeted Feedback**: Identify exact knowledge gaps

### Content Reusability
- **Flexible Composition**: Mix and match for different courses
- **Multi-Audience**: Same atoms, different rendering

---

**Example Created**: 2025-12-29  
**Purpose**: Demonstrate atomicity specialist workflow  
**Status**: Reference implementation
