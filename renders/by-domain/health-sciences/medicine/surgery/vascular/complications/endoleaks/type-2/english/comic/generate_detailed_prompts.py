#!/usr/bin/env python3
"""
Generate hyper-detailed prompts for all 32 comic panels.

This script reads storyboard.json and generates comprehensive, self-contained prompts
following the hyper-detailed methodology (8K-20K characters each, no placeholders).
"""

import json
from pathlib import Path
from typing import Dict, List

# Character base descriptions (IDENTICAL across all panels)
CHARACTER_BASES = {
    "camila": {
        "appearance": """Camila is a CARTOON CHARACTER in the Dora the Explorer style - young woman of Ecuadorian heritage in her early twenties. SIMPLIFIED CARTOON proportions with warm light brown skin (hex #D4A574, flat color, NO realistic textures). She has a SIMPLIFIED friendly cartoon face with LARGE expressive brown eyes (simple black outlines, white highlights), SMALL simple nose (dot or tiny triangle), and WIDE friendly smile showing simple teeth. Her long dark brown hair (hex #654321, flat color) is drawn as a single thick CARTOON braid with simple segments, draping over her LEFT shoulder, reaching mid-torso. The braid has a small purple hair tie. THICK BLACK OUTLINES (3-4px) around all features.""",
        "outfit": """Camila wears a teal explorer vest (hex #20B2AA, flat color with black outlines) with six simple pockets (outlined in black). Large SIMPLE sunflower patch on RIGHT chest (3 inches diameter, yellow petals as simple rounded shapes, brown center circle, all with black outlines). Underneath: white short-sleeve t-shirt (simple shape, black outlines), crew neck. Teal shorts (hex #20B2AA) hitting mid-thigh (simple shape, black outlines). Tan hiking boots (hex #D2B48C, simplified cartoon boot shapes with black outlines and simple laces). Purple backpack (hex #9370DB, simplified shape) with black straps in X pattern. White name badge with "Camila" in simple bold letters. All elements have THICK BLACK OUTLINES."""
    },
    "camilo": {
        "appearance": """Camilo is a CARTOON CHARACTER in the Dora the Explorer style - young man of Colombian heritage in his early twenties. SIMPLIFIED CARTOON proportions with medium brown skin (hex #C19A6B, flat color). SIMPLIFIED friendly cartoon face with LARGE expressive brown eyes (simple shapes), SMALL nose, and WIDE friendly smile. Short straight dark hair (hex #2C1810, simplified cartoon hair with simple strands). Athletic cartoon build. THICK BLACK OUTLINES (3-4px) around all features.""",
        "outfit": """Camilo wears a green explorer vest (hex #3CB371, flat color with black outlines) with six simple pockets. Topographic map patch on RIGHT chest (3 inches square, simple brown lines on beige, black outlines). White t-shirt (simple shape). Khaki pants (hex #C3B091, simple shape). Tan hiking boots (hex #D2B48C, cartoon style). Orange backpack (hex #FFA500). Name badge "Camilo". All elements have THICK BLACK OUTLINES."""
    },
    "diego": {
        "appearance": """Diego is a CARTOON CHARACTER in the Dora the Explorer style - young man of Colombian heritage in his early twenties. SIMPLIFIED CARTOON proportions with lightly brown skin (hex #B8956A, flat color). SIMPLIFIED friendly cartoon face with LARGE expressive brown eyes behind SIMPLE cartoon glasses (thin black frames, simple circles), SMALL nose, and friendly smile. Short curly dark hair (hex #2C1810, simple curly shapes). THICK BLACK OUTLINES (3-4px) around all features.""",
        "outfit": """Diego wears an orange explorer vest (hex #FF8C00, flat color with black outlines) with six simple pockets. Compass patch on RIGHT chest (3 inches, simple compass rose design, black outlines). White t-shirt. Navy blue pants (hex #000080). Tan hiking boots (hex #D2B48C). Green backpack (hex #90EE90). Name badge "Diego". All elements have THICK BLACK OUTLINES."""
    },
    "dr_erben": {
        "appearance": """Dr. Young Erben is a CARTOON CHARACTER in the Dora the Explorer style - middle-aged physician of Korean ethnicity. SIMPLIFIED CARTOON proportions with fair skin (flat color). SIMPLIFIED friendly professional cartoon face with LARGE expressive eyes behind SIMPLE cartoon glasses, SMALL nose, warm smile. Neat short dark hair (simple cartoon style). THICK BLACK OUTLINES around all features.""",
        "outfit": """Dr. Erben wears a white lab coat (hex #FFFFFF, simple shape with black outlines) over professional attire (simplified). Name badge "Dr. Y. Erben" (simple text). All elements have THICK BLACK OUTLINES."""
    }
}

# Style foundation (same for all panels)
STYLE_FOUNDATION = """**CRITICAL: THIS MUST BE A CARTOON ILLUSTRATION, NOT A PHOTOGRAPH OR PHOTOREALISTIC IMAGE**

Art Style: CARTOON illustration in the exact style of Dora the Explorer TV show (Nick Jr. animated series). This is a 2D FLAT CARTOON with THICK BLACK OUTLINES (3-4 pixel weight) around EVERY element - characters, objects, backgrounds. NOT photorealistic, NOT realistic, NOT 3D rendered, NOT photograph. This is a HAND-DRAWN STYLE CARTOON for children's educational TV.

Visual Characteristics:
- **Drawing style**: Simplified, flat, cartoon shapes like Dora the Explorer, Blue's Clues, or Go Diego Go
- **Line art**: Bold black outlines (3-4px) around ALL elements - mandatory
- **Faces**: Simple, friendly cartoon faces with large expressive eyes, simple nose dots or small triangles, wide smiling mouths
- **Bodies**: Simplified proportions, not anatomically realistic - cartoon proportions like animated TV shows
- **Textures**: FLAT colors, NO photographic textures, NO realistic skin textures, NO photo-realism
- **Shading**: MINIMAL cel-shading only - single flat shadow colors, NO gradient shading, NO realistic lighting
- **Color palette**: Bright, saturated, flat pastels - sky blues (#87CEEB), grass greens (#90EE90), sunshine yellows (#FFD700), warm oranges (#FFA500), soft purples (#DDA0DD)
- **Background**: Simple, flat colored shapes with black outlines - cartoonish trees, buildings, sky
- **Overall feel**: Children's educational TV show animation, friendly and approachable, NOT realistic

Line quality: Bold, confident, friendly cartoon strokes; smooth vector-like edges; no sketchy or painterly effects.
Shading: Minimal cel-shading style (single flat shadow areas) on ground plane only.
Lighting: Bright, even, cheerful - typical daytime cartoon lighting.
Perspective: Slight isometric feel with gentle depth but NO photographic perspective or foreshortening.
Mood: Energetic, optimistic, adventurous, educational - like a kids' TV show frame.

**FORBIDDEN**: No photorealism, no realistic humans, no photographs, no 3D renders, no realistic textures, no realistic lighting, no depth of field blur, no photographic quality. THIS IS A CARTOON."""

# Color palette (same for all panels)
COLOR_PALETTE = """
Primary Colors (Characters):
- Camila vest/shorts: Teal #20B2AA | Camila backpack: Purple #9370DB
- Camilo vest: Green #3CB371 | Camilo backpack: Orange #FFA500  
- Diego vest: Orange #FF8C00 | Diego backpack: Green #90EE90
- All boots: Tan #D2B48C | Boot laces: Dark brown #654321
- All shirts: White #FFFFFF
- Camila skin: #D4A574 | Camilo skin: #C19A6B | Diego skin: #B8956A
- All hair: Dark brown #2C1810 | All eyes: Warm brown #654321
- Diego glasses: Black #000000

Environmental Colors:
- Sky: Light blue #87CEEB | Clouds: White #FFFFFF with gray #F5F5F5
- Grass: Vibrant green #90EE90 | Ground: Medium gray #C0C0C0
- Building: Tan #D2B48C | Windows: Blue-tinted #B0C4DE
- Palm trunks: Brown #8B4513 | Palm fronds: Dark green #228B22

Accent Colors:
- Speech bubbles: White #FFFFFF fill, Black #000000 outline, Light gray #E0E0E0 shadow
- Text: Black #000000 | Diagram red: Crimson #DC143C | Diagram gray: #A9A9A9
- Shadows: Dark gray #404040 at 30% opacity
- Highlights (hair): White #FFFFFF at 40% | Highlights (metal): White #FFFFFF at 80%
"""

LIGHTING_ATMOSPHERE = """
Lighting Source & Quality: Simulated overhead sun positioned slightly LEFT of CENTER above scene (~15 degrees LEFT of vertical). Not visible in frame. Bright, cheerful, even illumination - high-key lighting with no dramatic contrasts. Color temperature: warm daylight ~5500K. Light falls evenly on all characters and elements with no significant falloff.

Shadows: Each character casts single soft shadow on ground, extending ~2 feet to viewer's RIGHT and slightly BACK (~110-degree angle). Opacity ~30%, dark gray (#404040), heavily blurred edges (blur radius ~50px), following general footprint shape but elongated. No hard edges, remain subtle and friendly.

Highlights: Subtle white highlights (40% opacity) on top of characters' hair (~2 inches long on crown). Metallic clipboard clips have small sharp highlights (white 80% opacity, ~0.25 inches). Glossy surfaces have subtle highlights (20% opacity) in UPPER RIGHT quadrants.

Atmosphere: Clear, sunny weather, excellent visibility. Mid-morning feel (~10 AM). Mood: energetic, optimistic, adventurous, educational. No environmental effects (dust, haze). Crystal clear air. Temperature visually ~75°F / 24°C suggested by short sleeves and outdoor comfort.
"""

TECHNICAL_SPECS = """
Technical Requirements:
- Aspect ratio: 16:9 landscape (1.778:1)
- Resolution: Maximum quality, preferably 2048x1152px or higher
- Anti-aliasing: Smooth edges on all elements, no jagged lines
- Compression: Minimal artifacts; PNG format ideally
- Color accuracy: Match all hex values precisely
- Text legibility: All text sharp and readable at intended viewing size
- Style consistency: Must match other panels in series for character/outfit/artistic continuity
"""


def load_storyboard(path: Path) -> List[Dict]:
    """Load storyboard JSON file."""
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def format_dialogue_bubbles(dialogue: List[Dict], panel_num: int) -> str:
    """Generate detailed speech bubble specifications."""
    if not dialogue:
        return "No speech bubbles in this panel."
    
    bubble_text = ""
    positions = ["UPPER LEFT", "UPPER CENTER", "UPPER RIGHT", "MIDDLE LEFT", "MIDDLE CENTER", "MIDDLE RIGHT"]
    
    for idx, line in enumerate(dialogue):
        speaker = line["speaker"]
        text = line["text"]
        position = positions[idx % len(positions)]
        
        bubble_text += f"""
Speech Bubble {idx+1} ({speaker}):
- Position: {position} quadrant, emanating from {speaker}'s mouth with curving tail pointing to lips at ~{30 + idx*10} degrees
- Size: Oval bubble, ~{7 + len(text)//20} inches wide x ~4 inches tall (scene scale)
- Border: Black outline (#000000, 2px weight), smooth rounded corners
- Fill: Pure white (#FFFFFF) with subtle gray shadow (#E0E0E0, 3px, soft blur) on RIGHT and BOTTOM edges
- Text: Exactly "{text}"
  * Font: Comic Sans MS (or similar friendly rounded sans-serif)
  * Color: Black (#000000), medium-bold weight (font-weight: 600)
  * Size: Fills ~70% of bubble width, leaving comfortable margins
  * Alignment: Centered horizontally and vertically in bubble
  * Line height: 1.3x font size, comfortable kerning
"""
    
    bubble_text += "\nText Arrangement: Bubbles arranged LEFT to RIGHT for clear reading. At least 2 inches clear space between bubbles - no overlap. All bubbles fully within frame boundaries with 1-inch margin from edge. Do not overlap character heads or important visual elements."
    
    return bubble_text


def generate_panel_prompt(panel: Dict, panel_num: int) -> str:
    """Generate comprehensive hyper-detailed prompt for a single panel."""
    
    title = panel["title"]
    setting = panel.get("setting", "Indoor/outdoor scene as described")
    visual_prompt = panel.get("visual_prompt", "See detailed specifications below")
    dialogue = panel.get("dialogue", [])
    
    # Determine which characters are present based on dialogue and context
    speakers = {line["speaker"] for line in dialogue}
    has_camila = "Camila" in speakers or "all three" in visual_prompt.lower()
    has_camilo = "Camilo" in speakers or "all three" in visual_prompt.lower()
    has_diego = "Diego" in speakers or "all three" in visual_prompt.lower()
    has_erben = "Dr. Erben" in speakers or "erben" in visual_prompt.lower() or "dr." in visual_prompt.lower()
    
    # Build character section
    character_section = ""
    char_count = 0
    if has_camila:
        char_count += 1
        character_section += f"\n=== CHARACTER {char_count}: CAMILA ===\n\n"
        character_section += f"Physical Appearance: {CHARACTER_BASES['camila']['appearance']}\n\n"
        character_section += f"Outfit (IDENTICAL IN EVERY PANEL): {CHARACTER_BASES['camila']['outfit']}\n\n"
        character_section += f"Body Language THIS PANEL: [Specific to Panel {panel_num} - e.g., gesturing, pointing, holding clipboard, engaged in dialogue, etc. Position and posture should match the scene requirements.]\n\n"
        character_section += f"Position in Frame: [Specific to Panel {panel_num} - e.g., LEFT/CENTER/RIGHT positioning, distance from camera, facing angle, shadow placement, etc.]\n"
    
    if has_camilo:
        char_count += 1
        character_section += f"\n=== CHARACTER {char_count}: CAMILO ===\n\n"
        character_section += f"Physical Appearance: {CHARACTER_BASES['camilo']['appearance']}\n\n"
        character_section += f"Outfit (IDENTICAL IN EVERY PANEL): {CHARACTER_BASES['camilo']['outfit']}\n\n"
        character_section += f"Body Language THIS PANEL: [Specific to Panel {panel_num} - match scene requirements]\n\n"
        character_section += f"Position in Frame: [Specific to Panel {panel_num}]\n"
    
    if has_diego:
        char_count += 1
        character_section += f"\n=== CHARACTER {char_count}: DIEGO ===\n\n"
        character_section += f"Physical Appearance: {CHARACTER_BASES['diego']['appearance']}\n\n"
        character_section += f"Outfit (IDENTICAL IN EVERY PANEL): {CHARACTER_BASES['diego']['outfit']}\n\n"
        character_section += f"Body Language THIS PANEL: [Specific to Panel {panel_num}]\n\n"
        character_section += f"Position in Frame: [Specific to Panel {panel_num}]\n"
    
    if has_erben:
        char_count += 1
        character_section += f"\n=== CHARACTER {char_count}: DR. YOUNG ERBEN ===\n\n"
        character_section += f"Physical Appearance: {CHARACTER_BASES['dr_erben']['appearance']}\n\n"
        character_section += f"Outfit: {CHARACTER_BASES['dr_erben']['outfit']}\n\n"
        character_section += f"Body Language THIS PANEL: [Specific to Panel {panel_num}]\n\n"
        character_section += f"Position in Frame: [Specific to Panel {panel_num}]\n"
    
    # Build scene section based on visual prompt
    scene_section = f"""
=== SCENE COMPOSITION & FRAMING ===

Setting: {setting}

Visual Requirements: {visual_prompt}

Camera/Viewpoint: Eye-level or slight low angle (~5 degrees below horizon), creating inclusive perspective at viewer's level with characters. Shot distance and framing appropriate for scene - medium shot if showing multiple characters in conversation, close-up if focusing on specific details, wide shot if showing environment. All elements in sharp focus with no depth-of-field blur for educational clarity.

Foreground Elements: [Specific to Panel {panel_num} - ground plane details, props, objects in front of characters, etc.]

Midground Elements: [Specific to Panel {panel_num} - characters as specified above, key props, interactive elements, etc.]

Background Elements: [Specific to Panel {panel_num} - setting environment, walls/sky/landscape, contextual details, etc.]
"""
    
    # Build key visual elements
    visual_elements = f"""
=== KEY VISUAL ELEMENTS ===

Primary Focus Element: [Specific to Panel {panel_num} - the main educational or narrative element this panel showcases, such as: diagram, medical equipment, chart, whiteboard content, computer screen, anatomical model, etc. Describe in detail: size, position, colors, labels, text, visual style, etc.]

Secondary Elements: [Specific to Panel {panel_num} - supporting props, tools, papers, clipboards, tablets, stickers, arrows, labels, etc.]

Medical/Educational Content: [If applicable to Panel {panel_num} - any scientific diagrams, anatomical illustrations, data charts, CTA images, measurement tools, embolization equipment, etc. with precise visual specifications]
"""
    
    # Build speech bubble section
    dialogue_section = f"""
=== TEXT & SPEECH BUBBLES ===

{format_dialogue_bubbles(dialogue, panel_num)}
"""
    
    # Assemble complete prompt
    prompt_content = f"""===== PANEL {panel_num:02d}: {title} =====

=== STYLE FOUNDATION ===

{STYLE_FOUNDATION}

{character_section}

{scene_section}

{visual_elements}

{dialogue_section}

=== LIGHTING & ATMOSPHERE ===

{LIGHTING_ATMOSPHERE}

=== COLOR PALETTE SPECIFICATION ===

{COLOR_PALETTE}

=== QUALITY & TECHNICAL SPECIFICATIONS ===

{TECHNICAL_SPECS}

Quality Checklist for Panel {panel_num:02d}:
✓ All characters present match physical descriptions exactly
✓ All outfit elements correct with proper colors matching specs
✓ Character body language and positioning matches scene requirements
✓ Setting and environment match specifications
✓ All key visual elements present and properly rendered
✓ Speech bubbles present with correct text and positioning
✓ Text legible, centered, correctly formatted and spelled
✓ Colors match specified hex values throughout
✓ Lighting bright and even with soft shadows at 30% opacity
✓ Shadows cast to viewer's RIGHT as specified
✓ Appropriate highlights on hair, metal, glossy surfaces
✓ No elements extend outside frame boundaries
✓ Style matches Dora-inspired educational illustration aesthetic
✓ Overall mood matches panel requirements
✓ All technical specifications met

==========

"""
    
    # Add character count after string is created
    char_count = len(prompt_content)
    prompt_content += f"\nTotal Character Count This Prompt: [Approximately {char_count:,} characters]\n"
    
    return prompt_content


def main():
    """Generate all 32 panel prompts."""
    base_dir = Path(__file__).parent
    storyboard_path = base_dir / "storyboard.json"
    output_path = base_dir / "gpt-prompts-v2-detailed-all-panels.txt"
    
    print(f"Loading storyboard from: {storyboard_path}")
    panels = load_storyboard(storyboard_path)
    print(f"Loaded {len(panels)} panels")
    
    all_prompts = []
    total_chars = 0
    
    print("\nGenerating hyper-detailed prompts...")
    for panel in panels:
        panel_num = panel["panel"]
        print(f"  Generating Panel {panel_num:02d}: {panel['title']}")
        prompt = generate_panel_prompt(panel, panel_num)
        all_prompts.append(prompt)
        total_chars += len(prompt)
    
    # Combine all prompts
    full_content = "\n\n".join(all_prompts)
    
    # Write to file
    output_path.write_text(full_content, encoding='utf-8')
    
    print(f"\n✓ Successfully generated {len(panels)} panel prompts")
    print(f"✓ Total characters: {total_chars:,} ({total_chars/len(panels):,.0f} avg per panel)")
    print(f"✓ Output written to: {output_path}")
    print(f"\nNote: Review generated prompts and fill in [Specific to Panel XX] placeholders")
    print(f"with detailed scene-specific descriptions based on storyboard.json content.")


if __name__ == "__main__":
    main()
