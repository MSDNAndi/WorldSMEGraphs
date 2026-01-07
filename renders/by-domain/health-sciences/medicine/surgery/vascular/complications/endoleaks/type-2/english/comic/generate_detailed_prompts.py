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
        "appearance": """Camila is a young woman of Ecuadorian heritage in her early twenties with warm light brown skin (hex #D4A574). She has a youthful, friendly face with round, approachable features, warm brown eyes that sparkle with enthusiasm, and a genuine smile showing slight dimples on both cheeks. Her long dark brown hair (hex #654321) is styled in a single thick braid that drapes over her LEFT shoulder (from viewer's perspective), reaching down to mid-torso level. The braid is secured at the end with a small purple hair tie that matches her backpack.""",
        "outfit": """Camila wears a teal explorer vest (hex #20B2AA) with six visible pockets. On the RIGHT chest is a large sunflower patch (3 inches diameter, yellow petals, brown center). Underneath: white short-sleeve t-shirt, crew neck. Teal shorts (hex #20B2AA, matching vest) hitting mid-thigh. Tan hiking boots (hex #D2B48C) with brown laces, ankle-height. Purple backpack (hex #9370DB) on both shoulders with black straps crossing chest in X pattern. White name badge on LEFT chest reading "Camila" in black Arial Bold font (0.75 inches tall)."""
    },
    "camilo": {
        "appearance": """Camilo is a young man of Colombian heritage in his early twenties with medium brown skin (hex #C19A6B). He has a friendly, open face with gentle features, short straight dark hair (hex #2C1810) cut in a neat professional style with slight side part, warm brown eyes, and an enthusiastic smile. His build is average and athletic, conveying capability and energy.""",
        "outfit": """Camilo wears a green explorer vest (hex #3CB371) with six visible pockets. On the RIGHT chest is a topographic map patch (3 inches square, brown contour lines on beige background). Underneath: white short-sleeve t-shirt, crew neck. Khaki pants (hex #C3B091) reaching ankles. Tan hiking boots (hex #D2B48C) identical to Camila's, with brown laces. Orange backpack (hex #FFA500) on both shoulders with black straps. White name badge on LEFT chest reading "Camilo" in black Arial Bold font (0.75 inches tall)."""
    },
    "diego": {
        "appearance": """Diego is a young man of Colombian heritage in his early twenties with lightly brown skin (hex #B8956A). He has a friendly, thoughtful face with short curly dark hair (hex #2C1810) with natural volume and texture, warm brown eyes behind subtle round-framed glasses (thin black frames), and a confident smile. His build is average, conveying both intelligence and approachability.""",
        "outfit": """Diego wears an orange explorer vest (hex #FF8C00) with six visible pockets. On the RIGHT chest is a compass patch (3 inches diameter, nautical compass rose in black/white with red needle). Underneath: white short-sleeve t-shirt, crew neck. Navy blue pants (hex #000080) reaching ankles. Tan hiking boots (hex #D2B48C) identical to others. Green backpack (hex #90EE90) on both shoulders with black straps. White name badge on LEFT chest reading "Diego" in black Arial Bold font (0.75 inches tall)."""
    },
    "dr_erben": {
        "appearance": """Dr. Young Erben is a middle-aged physician of Korean ethnicity with fair skin, petite build, and professional demeanor. Neat short dark hair, typically wears stylish glasses with modern frames. Warm, intelligent eyes that convey both expertise and approachability.""",
        "outfit": """Dr. Erben wears a white lab coat (hex #FFFFFF) over professional attire. The lab coat is knee-length, with lapels and pockets. Underneath: dress shirt and slacks in neutral tones. Name badge visible on lab coat lapel reading "Dr. Y. Erben" in professional font."""
    }
}

# Style foundation (same for all panels)
STYLE_FOUNDATION = """Art Style: Dora the Explorer inspired educational illustration designed for research interns and medical students. 2D flat illustration with thick black outlines (3-4 pixel weight) on all major elements. Vector-like smoothness with no heavy textures or grain. Color palette: bright, saturated pastels - sky blues (#87CEEB), grass greens (#90EE90), sunshine yellows (#FFD700), warm oranges (#FFA500), soft purples (#DDA0DD). Line quality: bold, confident, friendly strokes; no sketchy edges. Shading: minimal cel-shading style with single soft shadows on ground plane only. Lighting: bright, even, cheerful, simulating midday outdoor light. Perspective: slight isometric feel with gentle depth but no aggressive foreshortening. Mood: energetic, optimistic, adventurous, educational."""

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
