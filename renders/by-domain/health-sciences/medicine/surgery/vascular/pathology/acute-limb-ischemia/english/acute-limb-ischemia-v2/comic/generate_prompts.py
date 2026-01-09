#!/usr/bin/env python3
"""Generate super-explicit prompts for Acute Limb Ischemia V2 story."""

import json
import os

# Load storyboard
storyboard_path = "../story-development/03-storyboard.json"
with open(storyboard_path) as f:
    storyboard = json.load(f)

# Create output directory
os.makedirs("individual-prompts", exist_ok=True)

# Character description for Dr. Young Erben
DR_ERBEN_DESC = """Dr. Young Erben: A petite Korean woman in her early 40s with shoulder-length black hair tied in a practical low ponytail. She wears distinctive rectangular black-framed glasses that frame her warm, intelligent brown eyes. Her face has gentle East Asian features with high cheekbones and a reassuring smile. She wears teal hospital scrubs (#008B8B) with a white coat bearing her name tag. Her presence is calm and competent, with body language that conveys both professionalism and compassion."""

DR_ERBEN_OR_DESC = """Dr. Young Erben in surgical attire: Wearing surgical greens (#2F4F4F), surgical cap covering her ponytail, surgical mask, but her distinctive rectangular black-framed glasses are still visible above the mask. Her brown eyes show focus and determination."""

# Style guide
STYLE_GUIDE = """Dora the Explorer cartoon style: thick black outlines (3-4px width) around ALL objects and characters, flat bright colors with NO gradients or shading, simple geometric shapes, large expressive eyes (about 30% of face height), exaggerated facial expressions, clean white backgrounds or simple color blocks, bold sans-serif text for dialogue, landscape orientation 1536×1024 pixels."""

def generate_prompt(panel):
    """Generate super-explicit prompt for a single panel."""
    panel_num = panel["panel_number"]
    title = panel["title"]
    scene = panel["scene"]
    characters = ", ".join(panel["characters"])
    elements = panel["key_elements"]
    dialogue = panel.get("dialogue", "")
    educational = panel["educational_focus"]
    tone = panel["emotional_tone"]
    
    # Determine if OR scene
    is_or = "operating room" in scene.lower() or "surgical" in scene.lower() or "OR" in scene
    dr_desc = DR_ERBEN_OR_DESC if is_or else DR_ERBEN_DESC
    
    prompt = f"""Create a cartoon-style medical education illustration for Panel {panel_num}: "{title}".

STYLE REQUIREMENTS:
{STYLE_GUIDE}

CHARACTER DESCRIPTIONS:
{dr_desc}

Patient Carlos Ramirez: A Venezuelan man in his 60s with gray hair, concerned expression, wearing hospital gown. His RIGHT leg appears pale and mottled compared to LEFT leg.

SCENE DESCRIPTION:
{scene}

CHARACTERS PRESENT:
{characters}

KEY VISUAL ELEMENTS (be SUPER EXPLICIT about placement):
"""
    
    # Add visual elements with explicit directions
    for i, element in enumerate(elements, 1):
        prompt += f"{i}. {element}\n"
    
    prompt += f"""
DIALOGUE (include as text bubbles):
{dialogue}

EDUCATIONAL FOCUS:
{educational}

EMOTIONAL TONE:
{tone}

COMPOSITION:
- Landscape format 1536×1024 pixels
- Main action in CENTER of frame
- Dr. Young Erben positioned on LEFT side when facing patient
- Patient Carlos on RIGHT side
- Clear sight lines between characters
- Speech bubbles positioned ABOVE characters' heads
- Text readable at small sizes (minimum 24pt equivalent)

COLOR PALETTE (use exact hex codes):
- Dr. Erben scrubs: #008B8B (teal) or #2F4F4F (surgical green in OR)
- Dr. Erben glasses frames: #000000 (black)
- Patient gown: #E6F3FF (light blue)
- Affected RIGHT leg: #B0C4DE (pale blue-gray)
- Normal LEFT leg: #FFE4C4 (peachy beige)
- Background: #FFFFFF (white) or #F0F8FF (alice blue)
- Emergency red indicators: #DC143C (crimson)
- Medical equipment: #C0C0C0 (silver)

SPANISH DIALOGUE with English subtitles beneath:
{dialogue if dialogue else "No dialogue in this panel"}

CRITICAL: Use thick black outlines (3-4px) on EVERYTHING. No gradients. Flat colors only. Large expressive eyes. Dora the Explorer cartoon aesthetic throughout."""

    return prompt

# Generate all prompts
all_prompts = []
for panel in storyboard["panels"]:
    prompt = generate_prompt(panel)
    panel_num = panel["panel_number"]
    
    # Save individual file
    filename = f"individual-prompts/panel_{panel_num:02d}.txt"
    with open(filename, 'w') as f:
        f.write(prompt)
    
    all_prompts.append(f"=== PANEL {panel_num:02d}: {panel['title']} ===\n\n{prompt}\n\n")
    print(f"Generated prompt for Panel {panel_num:02d}: {panel['title']}")

# Save combined file
with open("prompts-all-panels.txt", 'w') as f:
    f.write("".join(all_prompts))

print(f"\nGenerated {len(all_prompts)} prompts successfully!")
print(f"Average prompt length: {sum(len(p) for p in all_prompts) // len(all_prompts)} characters")
