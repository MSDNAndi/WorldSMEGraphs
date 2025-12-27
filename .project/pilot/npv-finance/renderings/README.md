# Rendering Metadata

## Audience-Specific Renderings for NPV Concept

### Overview

This directory contains multi-audience renderings of NPV (Net Present Value) content, demonstrating how the same formal knowledge (stored in AKUs) can be transformed for vastly different audiences while maintaining conceptual accuracy.

---

## Available Renderings

### 1. German Elementary School (Ages 8-10)
**File:** `german-elementary-school/geld-heute-oder-morgen.md`
**Language:** German
**Level:** Grundschule (Primary School)
**Length:** ~5,000 characters
**Key Features:**
- Story-based learning (Lisa und ihr Taschengeld)
- Real-world examples (machine replacement simplified)
- Age-appropriate math (percentages, simple multiplication)
- Emoji visual aids for engagement
- Glossary with child-friendly definitions
- Practice exercises with answers
- Cultural context (Euro currency, German school system)

**Learning Objectives:**
- Understand time value of money concept
- Compare present vs. future value
- Recognize opportunity cost in decisions
- Apply simple discounting logic

**Rendering Approach:**
- Simplified the equipment replacement example
- Used relatable scenarios (pocket money, birthday presents)
- Broke down complex formulas into step-by-step arithmetic
- Maintained conceptual accuracy while reducing mathematical rigor

---

### 2. US Toddlers (Ages 2-4)
**File:** `us-toddlers/money-now-or-later.md`
**Language:** English (US)
**Level:** Pre-K (Toddler/Preschool)
**Length:** ~5,000 characters
**Key Features:**
- Cookie/toy metaphors (concrete objects)
- Repetition and simple language
- Heavy use of emojis as visual aids
- One-sentence paragraphs (attention span consideration)
- Interactive "What would YOU choose?" prompts
- Parent's note explaining pedagogical approach
- Finger counting activities (pre-math skills)

**Learning Objectives:**
- Recognize immediate vs. delayed gratification
- Understand "now" vs. "later" temporal concepts
- Compare quantities (more/less)
- Introduction to trade-offs (opportunity cost foundation)

**Rendering Approach:**
- Abstracted NPV to "Cookie now vs. Cookie later"
- Used concrete objects (toys, cookies, stickers)
- No numbers beyond simple counting (1-10)
- Focused on intuition over calculation
- Emphasized emotional/experiential learning
- Parent note bridges to formal concepts

---

## Rendering Methodology

### Source AKUs Used:
1. `aku-001-npv-definition.json` - Core definition and intuition
2. `aku-003-present-value-concept.json` - Time value of money
3. `aku-027-equipment-replacement-example.json` - Worked example

### Transformation Process:

**Step 1: Audience Analysis**
- German Elementary: Can read, do arithmetic, understand abstract concepts with concrete examples
- US Toddlers: Pre-literate, concrete thinking, ~3-minute attention span, learning through play

**Step 2: Content Selection**
- Elementary: NPV definition, formula (simplified), worked example (scaled down)
- Toddlers: Basic intertemporal choice, quantity comparison, no formulas

**Step 3: Language Adaptation**
- Elementary: Story narrative, active voice, direct address, cultural references
- Toddlers: Short sentences, repetition, exclamations, emoji-heavy, interactive prompts

**Step 4: Cognitive Scaffolding**
- Elementary: Build from known (pocket money) to new (discounting), include practice
- Toddlers: Anchor to immediate experience (cookies, toys), celebrate choices

**Step 5: Accuracy Preservation**
- Elementary: Mathematically correct (though simplified), preserves key relationships
- Toddlers: Conceptually aligned (present bias, trade-offs), intuition-focused

---

## Validation

### Elementary School Rendering:
✅ **Mathematical Accuracy:** Calculations correct, relationships preserved
✅ **Age Appropriateness:** Vocabulary at 8-10 year level (CEFR A1-A2 German)
✅ **Cultural Sensitivity:** Euro currency, German school context, appropriate examples
✅ **Pedagogical Soundness:** Scaffolded learning, practice opportunities, glossary
✅ **Engagement:** Story-based, relatable characters, visual aids

### Toddler Rendering:
✅ **Developmental Appropriateness:** Concrete objects, simple choices, pre-math skills
✅ **Language Level:** One-concept sentences, repetition, exclamations
✅ **Safety:** No complex concepts that could frustrate, celebrates all choices
✅ **Parent Involvement:** Note explains pedagogy, bridges to formal learning
✅ **Engagement:** Interactive, playful, emoji-driven, short sections

---

## Future Renderings Planned

### Additional Audiences:
- **German Gymnasium (High School)** - With calculus, formal proofs, research citations
- **Undergraduate Business Students** - WACC derivation, CAPM integration, case studies
- **MBA/Graduate** - Real options, multi-period models, sensitivity analysis
- **CFO/Practitioners** - Tax considerations, regulatory constraints, strategic implications
- **Non-native English Speakers** - Simplified vocabulary, glossary, slower pacing
- **Visual Learners** - Diagram-heavy, flowcharts, interactive visualizations
- **Audio/Podcast Format** - Conversational, story-based, no visual dependencies

### Planned Languages:
- Spanish (Mexico, Spain variants)
- Mandarin Chinese
- French
- Arabic
- Hindi
- Portuguese

---

## Technical Notes

### Rendering Engine (Future)
When automated rendering is implemented:

**Input:** AKU IDs + Audience Profile
**Process:**
1. Load AKUs from knowledge graph
2. Apply audience template (language, complexity, format)
3. Semantic transformation (formulas → stories for toddlers)
4. Cultural adaptation (currency, examples, references)
5. Validation against audience criteria
6. Output formatted document (MD, PDF, HTML, audio)

**Current Status:** Manual renderings (demonstrate capability)

**Next Steps:**
- Build template library for common audience types
- Create transformation rules (formula → concrete examples)
- Develop validation rubrics per audience
- Implement automated pipeline

---

## Usage

### For Educators:
- Use German Elementary for primary school finance literacy
- Adapt examples to local context (currency, cultural references)
- Combine with hands-on activities (piggy bank, purchase decisions)

### For Parents:
- Use Toddler rendering for early financial literacy
- Make it interactive (real cookies, real choices)
- Follow up with questions, celebrate learning

### For Researchers:
- Study effectiveness across audiences
- A/B test different metaphors/approaches
- Measure comprehension and retention
- Refine rendering methodology

---

## Metadata

**Created:** 2025-12-27
**Authors:** Generic Domain Empathy Agent + Audience Advocate Agents (Academic, Student)
**Source AKUs:** 3 (definition, concept, example)
**Validation:** Manual review for accuracy and appropriateness
**License:** CC-BY-4.0 (educational use)
**Last Updated:** 2025-12-27

---

## Feedback

For feedback on these renderings:
- Elementary School: Contact Student Audience Advocate
- Toddlers: Contact Diverse Learner Advocate + Curious Public Advocate
- General: Contact Rendering Agent

**Improvement Ideas Welcome!**
