# Image Prompt Engineering Guide for WorldSMEGraphs

**Purpose**: Guidelines for creating comprehensive, detailed image prompts that leverage the full 32,000 character capacity of GPT Image 1.5

---

## Overview

Many image generation prompts are too brief, resulting in generic or inaccurate images. This guide teaches how to write prompts that are:
- **Comprehensive**: Cover all visual elements needed
- **Precise**: Specify exact positions, orientations, and relationships
- **Detailed**: Include style, color, mood, and technical requirements
- **Domain-accurate**: Reflect correct subject matter expertise

---

## The Anatomy of an Excellent Prompt

### 1. Subject Description (500-2000 characters)

**Bad Example:**
```
Medical diagram of the heart
```

**Good Example:**
```
Create a detailed anatomical cross-section illustration of the human heart as it would appear in a professional medical textbook for cardiology residents. The heart is shown in a FRONTAL CORONAL section, with the viewer looking at the anterior surface of the heart that has been cut away to reveal internal structures.

The heart should be positioned in the CENTER of the image with the apex (bottom pointed tip) oriented toward the LOWER LEFT corner at approximately a 45-degree angle, reflecting the natural anatomical position in the chest.

Visible structures from LEFT to RIGHT as the viewer sees them:
- RIGHT ATRIUM on the viewer's LEFT side (remember: anatomical right is on viewer's left)
- RIGHT VENTRICLE in the lower left portion of the image
- INTERVENTRICULAR SEPTUM running vertically through the center
- LEFT VENTRICLE on the viewer's RIGHT side, with notably thicker muscular walls (3x thicker than RV)
- LEFT ATRIUM in the upper right portion

Major vessels entering/exiting at the TOP of the heart:
- SUPERIOR VENA CAVA entering the right atrium from above-right
- INFERIOR VENA CAVA entering the right atrium from below
- AORTA exiting LEFT ventricle, arching toward viewer's RIGHT
- PULMONARY TRUNK exiting RIGHT ventricle, bifurcating into left and right pulmonary arteries
- PULMONARY VEINS (4 total) entering left atrium from the lungs
```

### 2. Orientation and Direction Specification (500-1000 characters)

**Critical Rule**: Always specify:
- What is on the LEFT vs RIGHT of the image
- What flows FROM where TO where (use arrows with direction)
- What is in the FOREGROUND vs BACKGROUND
- What is at the TOP vs BOTTOM

**Example:**
```
BLOOD FLOW DIRECTION must be clearly indicated with arrows:
- BLUE-colored blood flows FROM the superior and inferior vena cava INTO the right atrium, then DOWN through the tricuspid valve INTO the right ventricle, then UP and OUT through the pulmonary valve INTO the pulmonary trunk
- RED-colored oxygenated blood flows FROM the pulmonary veins INTO the left atrium, then DOWN through the mitral valve INTO the left ventricle, then UP and OUT through the aortic valve INTO the aorta

Arrows indicating flow should be:
- Drawn as sleek, curved arrows following the natural flow path
- Color-coded: BLUE arrows for deoxygenated blood, RED arrows for oxygenated blood
- Arrowheads should be clearly visible at the END of each flow direction (pointing in the direction of flow)
```

### 3. Visual Style Specification (500-1000 characters)

**Include:**
- Art style (realistic, cartoon, vector, watercolor, etc.)
- Color palette
- Line weight and quality
- Background
- Mood/atmosphere
- Reference artists or styles if helpful

**Example:**
```
VISUAL STYLE:
- Medical illustration style similar to Netter's Atlas of Human Anatomy
- Rich, saturated colors with accurate anatomical coloring:
  - Arterial blood: bright oxygenated red (RGB: 200, 50, 50)
  - Venous blood: dark deoxygenated blue-red (RGB: 100, 40, 80)
  - Myocardium: warm pink-brown muscle tissue color
  - Valves: pearly white-gray with fibrous texture
  - Pericardium (if shown): thin transparent yellowish membrane

- Clean, precise line work with consistent line weight (heavier for outer structures, finer for internal details)
- Subtle shading to convey 3D depth without obscuring anatomical details
- Clean white or very light gray background
- No decorative elements, borders, or text (labels can be added separately)
- Professional medical illustration quality suitable for publication
```

### 4. Technical and Educational Requirements (500-1000 characters)

**For educational content, specify:**
- Target audience level
- Key concepts that must be visible
- What should be emphasized or highlighted
- What should be de-emphasized or simplified

**Example:**
```
EDUCATIONAL REQUIREMENTS:
This illustration is for medical students learning cardiac anatomy.

MUST CLEARLY SHOW:
1. All four chambers with clear size differentiation (LV notably larger than RV)
2. All four valves in their correct positions
3. Separation between pulmonary and systemic circuits
4. Coronary arteries on the epicardial surface (LAD, RCA, Circumflex visible)
5. Papillary muscles and chordae tendineae in both ventricles

EMPHASIZE (make visually prominent):
- The thickness difference between LV and RV walls
- The position and structure of the atrioventricular valves
- The relationship between the great vessels at the base

DE-EMPHASIZE (include but don't highlight):
- Fine trabeculations of the endocardium
- Conduction system (not visible in standard cross-section)
- Lymphatic drainage
```

### 5. Avoiding Common Errors (500+ characters)

**Explicitly state what NOT to include:**

```
AVOID THE FOLLOWING COMMON ERRORS:
- Do NOT reverse the left/right orientation (remember: anatomical left is on viewer's right)
- Do NOT show blood flow going in the wrong direction
- Do NOT make the RV wall thickness equal to LV wall thickness
- Do NOT omit the interventricular septum
- Do NOT show the aorta and pulmonary trunk exiting from the wrong ventricles
- Do NOT use cartoon-style simplification that loses anatomical accuracy
- Do NOT add text labels embedded in the image (these will be added digitally)
- Do NOT include a logo or watermark
- Do NOT show pathology unless specifically requested
```

---

## Complete Example: Medical Workflow Diagram

Here is a complete prompt for a complex medical workflow:

```
Create a comprehensive medical workflow diagram illustrating the complete clinical algorithm for diagnosing and managing acute mesenteric ischemia, designed for display in an emergency department or surgical suite.

OVERALL LAYOUT:
- Landscape orientation (wider than tall, approximately 16:9 aspect ratio)
- Flowchart format with clear hierarchical structure
- Flow direction is primarily TOP to BOTTOM with some horizontal branching
- Use consistent spacing between elements (approximately equal margins)

STARTING POINT (TOP CENTER):
A rectangular box at the TOP CENTER of the image containing "SUSPECTED ACUTE MESENTERIC ISCHEMIA" with an icon of an abdomen with a lightning bolt or warning symbol.

FIRST DECISION BRANCH (below starting point):
An arrow pointing DOWNWARD leads to a diamond-shaped decision box asking "PERITONITIS OR HEMODYNAMIC INSTABILITY?"

LEFT BRANCH (YES - CRITICAL PATH):
- If YES (left exit from diamond), a BOLD RED arrow points LEFT then DOWNWARD
- This leads to a red-bordered box: "IMMEDIATE SURGICAL EXPLORATION"
- Further down: "RESECTION OF NECROTIC BOWEL"
- Then: "REVASCULARIZATION IF POSSIBLE"
- End point: "ICU ADMISSION"

RIGHT BRANCH (NO - DIAGNOSTIC PATH):
- If NO (right exit from diamond), a BLUE arrow points RIGHT then DOWNWARD
- This leads to: "CT ANGIOGRAPHY" (with small CT scanner icon)

SECONDARY DECISION BRANCH (below CT Angiography):
Diamond-shaped box: "ARTERIAL OCCLUSION IDENTIFIED?"

[Continue with similar detail for remaining workflow steps...]

VISUAL STYLE:
- Clean, modern medical infographic style
- Color coding:
  * RED: urgent/surgical pathway elements
  * BLUE: diagnostic pathway elements  
  * GREEN: positive outcomes
  * YELLOW: monitoring/observation steps
  * GRAY: supportive care elements
- Rounded rectangle boxes for action steps
- Diamond shapes for decision points
- Ovals for start/end points
- All arrows clearly show direction with arrowheads AT THE END of each arrow
- Sans-serif font for any text (if included)
- White or very light gray background
- Subtle drop shadows on boxes for depth
- Icons or small illustrations within boxes to aid quick recognition

SIZE AND RESOLUTION:
- High resolution suitable for printing at poster size (24x36 inches at 300 DPI)
- All text should be readable when printed at this size

AVOID:
- Cluttered overlapping elements
- Ambiguous arrow directions
- Inconsistent box sizes for similar elements
- Color choices that are not colorblind-accessible
- Overly decorative elements that distract from information
```

---

## Domain-Specific Prompt Additions

### Medical Illustrations
- Specify anatomical orientation (anterior/posterior, medial/lateral, proximal/distal)
- Reference standard anatomical position
- Specify if pathology should be shown
- Reference standard atlases (Netter, Gray's) for style

### Children's Educational Content
- Specify cartoon style (Peppa Pig, Bluey, generic children's book, etc.)
- Describe character emotions and expressions
- Specify age-appropriate complexity
- Include safety/non-scary requirements for medical content

### Technical Diagrams
- Specify if using standard notation (UML, flowchart symbols, electrical symbols)
- Define coordinate systems if relevant
- Specify scale or proportions
- Include legend requirements

### Architectural/Spatial
- Specify viewpoint (bird's eye, isometric, cross-section)
- Define scale and proportions
- Specify lighting direction and shadows
- Include context/surroundings

---

## Quick Checklist for Every Prompt

Before submitting any image prompt, verify you have specified:

- [ ] **Subject**: What is the main subject?
- [ ] **Position**: Where is each element located (left/right/top/bottom/center)?
- [ ] **Direction**: Which way do things flow, point, or face?
- [ ] **Style**: What art style is needed?
- [ ] **Colors**: What specific colors should be used?
- [ ] **Background**: What is behind the subject?
- [ ] **Audience**: Who will view this image?
- [ ] **Purpose**: What should viewers learn or understand?
- [ ] **Avoid**: What common mistakes must be prevented?
- [ ] **Quality**: What resolution or format is needed?

---

## Character Limits

- GPT Image 1.5 accepts prompts up to **32,000 characters**
- Aim for **2,000-8,000 characters** for most complex images
- Simple subjects may need only **500-1,500 characters**
- Never assume "the AI will figure it out" - be explicit

---

**Document Metadata:**
- **Version**: 1.0
- **Created**: 2026-01-04
- **Purpose**: Image prompt engineering guide for WorldSMEGraphs contributors
- **License**: CC-BY-4.0
