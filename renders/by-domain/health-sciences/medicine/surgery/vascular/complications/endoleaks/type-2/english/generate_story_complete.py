#!/usr/bin/env python3
"""
Complete story generation system for vascular surgery educational comics.
Generates hyper-detailed Dora-style prompts and creates multiple output formats.
"""

import json
import sys
import os
from pathlib import Path

def create_hyper_detailed_prompt(panel_data, panel_number, total_panels=32):
    """
    Generate hyper-detailed prompt (up to 32,000 characters) for Dora-style cartoon panel.
    """
    
    # Character base specifications (identical for all panels for consistency)
    CAMILA_BASE = """
=== CHARACTER 1: CAMILA (Lead Explorer) ===
Physical Appearance: CARTOON character inspired by Dora the Explorer style. Ecuadorian heritage, 
early twenties, warm light brown CARTOON skin (simplified flat color #D4A574), round friendly 
CARTOON face with LARGE expressive eyes (warm brown #654321, OVERSIZED compared to realistic 
proportions - eyes are 30% of face height). Simple dot nose (just a small circle). Wide friendly 
smile with simple curved line mouth. Long dark brown hair in single thick braid over RIGHT shoulder, 
tied with sunflower-yellow ribbon.

Outfit (IDENTICAL EVERY PANEL - CRITICAL for consistency):
- Teal explorer vest (hex #20B2AA) with THICK BLACK OUTLINES (3-4px)
- Six pockets visible on vest (three LEFT, three RIGHT)
- Sunflower patch on RIGHT chest (3" diameter, bright yellow petals #FFD700, brown center #8B4513)
- White short-sleeve shirt underneath (hex #FFFFFF)
- Khaki cargo pants (hex #C3B091)  
- Comfortable hiking sneakers (gray #808080 with white #FFFFFF laces)
- Clipboard in hand (wooden backing #D2691E, white paper #FFFFFF)

CARTOON STYLE REQUIREMENTS for Camila:
- SIMPLIFIED CARTOON proportions: head is 1/4 of total body height (larger than realistic)
- Arms and legs: simple cylindrical shapes with minimal detail
- Hands: mittens with thumb + 3-4 fingers simplified
- THICK BLACK OUTLINES (3-4px) around ALL elements of character
- FLAT COLORS - no gradients, no shading complexity, just bright solid colors
- LARGE expressive eyes that can show emotions clearly
- Simple geometric shapes for body parts
"""

    CAMILO_BASE = """
=== CHARACTER 2: CAMILO (Tech Specialist) ===
Physical Appearance: CARTOON character in Dora the Explorer style. Mexican American heritage, early 
twenties, warm tan CARTOON skin (simplified flat color #C68642), rectangular CARTOON face with 
LARGE expressive eyes (dark brown #3E2723, OVERSIZED - 30% of face height). Simple dot nose. 
Friendly smile. Short dark brown hair, slightly spiky on top.

Outfit (IDENTICAL EVERY PANEL - CRITICAL for consistency):
- Navy blue hoodie (hex #1C3F5C) with THICK BLACK OUTLINES (3-4px)
- Medical school logo patch on LEFT chest (circular, 2" diameter, white/blue)
- Gray t-shirt underneath (visible at neck, hex #A9A9A9)
- Blue jeans (hex #4682B4)
- White sneakers (hex #FFFFFF with gray #808080 trim)
- Tablet computer in hand (black frame #000000, glowing blue screen #4FC3F7)

CARTOON STYLE REQUIREMENTS for Camilo:
- SIMPLIFIED CARTOON proportions: head is 1/4 of total body height
- Arms and legs: simple cylindrical shapes
- Hands: mittens with thumb + 3-4 fingers simplified  
- THICK BLACK OUTLINES (3-4px) around ALL elements
- FLAT COLORS - no gradients, bright solid colors
- LARGE expressive eyes
- Geometric shapes for body parts
"""

    DIEGO_BASE = """
=== CHARACTER 3: DIEGO (Research Expert) ===
Physical Appearance: CARTOON character in Dora the Explorer style. Filipino American heritage, 
early twenties, warm light tan CARTOON skin (simplified flat color #E0AC69), round friendly 
CARTOON face with LARGE expressive eyes (dark brown #4A2511, OVERSIZED - 30% of face height). 
Simple dot nose. Warm smile. Short black hair, neat and professional.

Outfit (IDENTICAL EVERY PANEL - CRITICAL for consistency):
- Red polo shirt (hex #DC143C) with THICK BLACK OUTLINES (3-4px)
- Stethoscope around neck (gray tubing #708090, silver chest piece #C0C0C0)
- Khaki chinos (hex #E3CF8F)
- Brown loafers (hex #8B4513)
- Medical reference book tucked under LEFT arm (blue cover #4169E1, white pages visible)

CARTOON STYLE REQUIREMENTS for Diego:
- SIMPLIFIED CARTOON proportions: head is 1/4 of total body height
- Arms and legs: simple cylindrical shapes
- Hands: mittens with thumb + 3-4 fingers simplified
- THICK BLACK OUTLINES (3-4px) around ALL elements
- FLAT COLORS - no gradients, bright solid colors  
- LARGE expressive eyes
- Geometric shapes for body parts
"""

    # Build the comprehensive prompt
    prompt = f"""🚨 CRITICAL: THIS MUST BE A CARTOON, NOT PHOTOREALISTIC 🚨
🚨 FORBIDDEN: No photorealism, No realistic humans, No 3D rendered characters, No photographs 🚨
🚨 REQUIRED: Dora the Explorer TV show cartoon style - THICK BLACK OUTLINES, SIMPLIFIED features 🚨

===== PANEL {panel_number:02d} of {total_panels}: {panel_data.get('title', 'Scene')} =====

=== STYLE FOUNDATION ===
Art Style: CARTOON illustration in the EXACT style of Dora the Explorer television show. This is a 2D 
FLAT cartoon with THICK BLACK OUTLINES (3-4 pixels wide) around EVERY element. Characters have 
SIMPLIFIED CARTOON proportions with LARGE EXPRESSIVE EYES (eyes are 30% of face height, much larger 
than realistic). All features are SIMPLIFIED: simple dot noses, curved line mouths, mitten-like hands 
with minimal finger detail.

Color Palette: BRIGHT, SATURATED, FLAT COLORS with NO gradients or complex shading:
- Sky: Bright sky blue (#87CEEB) or sunset orange (#FF8C42) 
- Grass/Ground: Bright grass green (#90EE90) or sandy beige (#F5DEB3)
- Buildings: Simple flat colors (white #FFFFFF, gray #D3D3D3, brick red #CB4154)
- Medical equipment: Clean whites (#FFFFFF), steel grays (#C0C0C0), monitor blues (#4FC3F7)

Line Work: THICK BLACK OUTLINES (3-4px) around:
- Character bodies and faces
- All clothing items  
- Props and objects
- Background elements
- Speech bubbles
- Everything visible in frame

Lighting: FLAT lighting with minimal shadows. Shadows are simple, solid color fills at 30% opacity, 
not gradients. Light source from upper LEFT creates shadows extending to RIGHT and slightly down.

{CAMILA_BASE}

Body Language THIS PANEL: {panel_data.get('camila_pose', 'Standing naturally, arms at sides')}
Position in Frame: {panel_data.get('camila_position', 'CENTER of frame')}
Facial Expression: {panel_data.get('camila_expression', 'Friendly smile, eyes wide and curious')}

{CAMILO_BASE}

Body Language THIS PANEL: {panel_data.get('camilo_pose', 'Standing naturally, arms at sides')}
Position in Frame: {panel_data.get('camilo_position', 'LEFT of center')}
Facial Expression: {panel_data.get('camilo_expression', 'Friendly smile, attentive')}

{DIEGO_BASE}

Body Language THIS PANEL: {panel_data.get('diego_pose', 'Standing naturally, arms at sides')}
Position in Frame: {panel_data.get('diego_position', 'RIGHT of center')}  
Facial Expression: {panel_data.get('diego_expression', 'Friendly smile, thoughtful')}

=== SCENE COMPOSITION ===
Setting: {panel_data.get('setting', 'Hospital hallway')}
Background: {panel_data.get('background', 'Simple hospital corridor with doors')}

Foreground Elements: {panel_data.get('foreground', 'The three characters')}
Midground Elements: {panel_data.get('midground', 'Medical equipment or furniture')}
Background Elements: {panel_data.get('background_detail', 'Hospital walls, doors, signs')}

Camera Angle: {panel_data.get('camera_angle', 'Eye level, straight on')}
Framing: {panel_data.get('framing', 'Medium shot showing characters waist up')}

=== VISUAL ELEMENTS ===
Key Props: {panel_data.get('props', 'Clipboards, tablets, medical equipment')}
Medical Equipment: {panel_data.get('medical_equipment', 'Stethoscopes, monitors')}
Anatomical Diagrams: {panel_data.get('anatomy', 'None visible')}
Text/Labels: {panel_data.get('labels', 'None')}

Special Effects: {panel_data.get('effects', 'None')}
Action Lines: {panel_data.get('action_lines', 'None')}

=== SPEECH BUBBLES ===
{panel_data.get('dialogue', 'No dialogue this panel')}

Speech Bubble Style: CARTOON style with THICK BLACK OUTLINES (2-3px), white fill (#FFFFFF), 
rounded rectangular shape with tail pointing to speaking character. Text in clear black sans-serif 
font (Comic Sans style), size appropriate to bubble, centered in bubble.

Bubble Placement: {panel_data.get('bubble_placement', 'Top third of frame')}

=== LIGHTING & ATMOSPHERE ===
Primary Light Source: Upper LEFT, 45-degree angle, creating simple flat shadows extending RIGHT
Shadow Style: Solid color fills at 30% opacity (#000000 with alpha), no gradients
Ambient Light: Bright and cheerful, appropriate for educational children's content
Special Lighting: {panel_data.get('special_lighting', 'None')}

=== COLOR PALETTE THIS PANEL ===
Dominant Colors: {panel_data.get('dominant_colors', 'Blues, greens, warm skin tones')}
Accent Colors: {panel_data.get('accent_colors', 'Bright yellows, teals, reds')}
Background Colors: {panel_data.get('bg_colors', 'Soft pastels, light blues and greens')}

All colors are FLAT (no gradients), BRIGHT (high saturation), and AGE-APPROPRIATE (cheerful, 
non-threatening palette).

=== TECHNICAL SPECIFICATIONS ===
Resolution: Landscape orientation, 16:9 aspect ratio, 1920x1080 pixels minimum
File Format: PNG with transparency support where applicable
Output Requirements: High quality, print-ready, suitable for PDF compilation

=== DORA STYLE CHECKLIST ===
✓ THICK BLACK OUTLINES (3-4px) around ALL elements
✓ SIMPLIFIED CARTOON proportions (heads 1/4 of body height)
✓ LARGE EXPRESSIVE EYES (30% of face height, much bigger than realistic)
✓ FLAT COLORS with NO gradients
✓ Simple dot noses and curved line mouths
✓ Mitten-like hands with minimal finger detail
✓ Bright, saturated, age-appropriate color palette
✓ NO photorealism, NO realistic humans, NO 3D rendering
✓ Cheerful, educational, child-friendly aesthetic
✓ Clear visual storytelling suitable for teaching

=== NARRATIVE CONTEXT ===
Previous Panel: {panel_data.get('previous', 'Start of story')}
This Panel: {panel_data.get('action', 'Main action happening now')}
Next Panel: {panel_data.get('next', 'What happens next')}

Educational Purpose: {panel_data.get('teaching_point', 'Medical education content')}

=== FINAL REMINDERS ===
🚨 THIS IS A CARTOON like Dora the Explorer TV show 🚨
🚨 NOT photorealistic, NOT realistic humans, NOT a photograph 🚨
🚨 THICK BLACK OUTLINES around everything 🚨
🚨 SIMPLIFIED features, LARGE eyes, FLAT colors 🚨
🚨 Bright, cheerful, age-appropriate, educational 🚨
"""

    return prompt.strip()


def generate_prompts_file(storyboard_path, output_path):
    """Generate hyper-detailed prompts file from storyboard."""
    with open(storyboard_path, 'r') as f:
        storyboard = json.load(f)
    
    panels = storyboard.get('panels', [])
    
    with open(output_path, 'w') as f:
        for i, panel in enumerate(panels, 1):
            prompt = create_hyper_detailed_prompt(panel, i, len(panels))
            f.write(prompt)
            f.write('\n\n' + '='*80 + '\n\n')
    
    print(f"Generated {len(panels)} hyper-detailed prompts")
    print(f"Average prompt length: {sum(len(create_hyper_detailed_prompt(p, i)) for i, p in enumerate(panels, 1)) // len(panels)} characters")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python generate_story_complete.py <storyboard.json> <output_prompts.txt>")
        sys.exit(1)
    
    storyboard_path = sys.argv[1]
    output_path = sys.argv[2]
    
    generate_prompts_file(storyboard_path, output_path)
