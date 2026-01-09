#!/usr/bin/env python3
"""
Generate super-explicit prompts for Carotid Stenosis V2 story
40 panels with Dr. Yuna Erben character
"""

import json
import os

# Load storyboard
storyboard_path = "../story-development/03-storyboard.json"
with open(storyboard_path, 'r') as f:
    storyboard = json.load(f)

# Dr. Erben character description (used in ALL panels)
DR_ERBEN_DESC = """Dr. Yuna Erben is a petite Korean-American woman in her 40s, approximately 5 feet tall. She has straight black hair pulled back in a neat, practical low ponytail. She wears distinctive expressive rectangular glasses with thin black frames that sit prominently on her face. Her facial features are East Asian: almond-shaped dark brown eyes behind her glasses, small nose, warm smile. She wears teal/cyan colored medical scrubs (#008B8B dark cyan) with a white coat over them when not in the OR, or full surgical gown when operating. Her hands are small and delicate but precise. She has an intelligent, warm, focused expression. Her posture is confident despite her small stature. She wears comfortable medical shoes. Her ethnicity is clearly Korean with East Asian facial features throughout"""

# Style guide (applied to ALL panels)
STYLE_GUIDE = """
CRITICAL STYLE REQUIREMENTS (DORA THE EXPLORER INSPIRED):
- Cartoon illustration style, NOT photorealistic
- Thick black outlines around ALL objects, characters, and elements (3-4 pixels wide, #000000 solid black)
- Flat, bright, saturated colors with NO gradients, NO shading, NO shadows
- Simple, clean shapes and forms
- Characters have large expressive eyes (eyes should be approximately 30% of face height)
- Exaggerated facial expressions showing clear emotions
- Bold, primary color palette: bright reds (#DC143C), blues (#1E90FF), greens (#32CD32), yellows (#FFD700)
- White backgrounds or simple colored backgrounds
- No texture, no depth, pure flat 2D style
- Educational labels and arrows when showing anatomical or technical elements
- Landscape orientation: 1536 pixels wide × 1024 pixels tall (3:2 aspect ratio)
- Composition: characters and key elements centered and prominent
- Clarity over realism: simplified anatomy when showing medical concepts

CHARACTER CONSISTENCY FOR DR. ERBEN:
- SAME outfit across all panels in story (teal scrubs #008B8B, OR scenes: surgical gown + mask + cap)
- SAME glasses in every panel (rectangular black frames)
- SAME hair style (black hair in low ponytail)
- SAME height (petite, notably shorter than other adults)
- SAME facial features (Korean, East Asian)
- Expressions change but core appearance IDENTICAL across all 40 panels
"""

def generate_panel_prompt(panel_data, panel_num):
    """Generate super-explicit prompt for a single panel"""
    
    # Extract panel info
    title = panel_data['title']
    scene = panel_data['scene']
    characters = panel_data['characters']
    key_elements = panel_data['key_elements']
    educational_focus = panel_data['educational_focus']
    emotion = panel_data['emotion']
    act = panel_data['act']
    
    # Build comprehensive prompt
    prompt = f"""PANEL {panel_num}/40: {title}
ACT: {act}
SCENE: {scene}

{STYLE_GUIDE}

CHARACTER DESCRIPTIONS:
{DR_ERBEN_DESC if "Dr. Erben" in str(characters) or "Dr. Yuna Erben" in str(characters) else ""}

CHARACTERS IN THIS PANEL: {', '.join(characters)}

DETAILED SCENE COMPOSITION:
"""
    
    # Add specific scene details based on panel number
    if panel_num == 1:
        prompt += """
- FOREGROUND (bottom 40% of image): Carmen Rodriguez (67-year-old Venezuelan woman, gray-black hair, worried expression, casual clothing) walking through automatic sliding glass doors, supported on LEFT side by her daughter Maria (40s, dark hair, concerned face, holding mother's left arm) and RIGHT side by son-in-law Jorge (40s, short dark hair, supportive, holding mother's right arm/back)
- MIDDLE GROUND (center 40%): Automatic sliding glass doors in OPEN position, glass panels reflecting slightly, chrome/silver metal frames
- BACKGROUND (top 20%): Hospital emergency department interior visible through doors, emergency signage in RED letters reading "EMERGENCIA / EMERGENCY" with red cross symbol, white walls, bright fluorescent lighting
- LIGHTING: Bright afternoon sunlight from LEFT side casting soft shadows to RIGHT
- POSITIONING: Carmen in CENTER of frame, family members flanking her symmetrically, doors framing the group
- COLORS: Carmen's outfit muted earth tones (#8B7355 brown), Maria in blue blouse (#4169E1), Jorge in gray shirt (#808080), hospital walls white (#FFFFFF), signage bright red (#DC143C)
- FACIAL EXPRESSIONS: Carmen's face showing worry lines, slightly furrowed brow, downturned mouth corners; Maria's face concerned with raised eyebrows; Jorge's face serious and supportive
- BODY LANGUAGE: Carmen slightly hunched, leaning on family; Maria and Jorge in protective supportive stances
"""
    
    elif panel_num == 2:
        prompt += """
- FOREGROUND (bottom 50%): Dr. Yuna Erben sitting on a short rolling stool (her feet barely touching ground, emphasizing petite stature), positioned at EYE LEVEL with Carmen who is sitting on exam table edge. Dr. Erben leaning forward slightly, hands holding a tablet computer (#C0C0C0 silver), warm engaging smile on face, rectangular black glasses prominent, black ponytail visible
- MIDDLE GROUND: Carmen on exam table (white padded surface) looking relieved and relaxed, making eye contact with Dr. Erben. Maria standing slightly BEHIND and to the RIGHT of Carmen, taking notes on phone
- BACKGROUND: Exam room wall in pale blue (#B0E0E6), medical posters in Spanish showing cardiovascular system, blood pressure cuff on wall mount, hand sanitizer dispenser
- SPEECH BUBBLES: Dr. Erben's bubble in Spanish "Buenas tardes, Señora Rodriguez. Soy la Doctora Erben" with small English subtitle below "Good afternoon, Mrs. Rodriguez. I am Doctor Erben"
- Carmen's response bubble "¡Habla español!" (You speak Spanish!) with relief expression
- POSITIONING: Dr. Erben LEFT side of frame on stool (lower than Carmen), Carmen CENTER-RIGHT on exam table, Maria background RIGHT
- COLORS: Dr. Erben's teal scrubs (#008B8B), white coat over scrubs, Carmen's brown clothing, exam table white (#FFFFFF), wall light blue (#B0E0E6)
- FACIAL DETAILS: Dr. Erben's warm smile with slight eye crinkles, engaged direct eye contact; Carmen's face showing visible relief, eyebrows relaxed, slight smile appearing; Maria's attentive expression
- KEY VISUAL: The eye-level positioning emphasizing Dr. Erben's respect and cultural sensitivity
"""
    
    # Add key elements as bullet points
    prompt += "\n\nKEY VISUAL ELEMENTS THAT MUST BE INCLUDED:\n"
    for i, element in enumerate(key_elements, 1):
        prompt += f"{i}. {element} - position, color, size, and orientation specified precisely\n"
    
    # Add emotion/tone direction
    prompt += f"\n\nEMOTIONAL TONE: {emotion}\n"
    prompt += f"- Facial expressions must clearly convey: {emotion}\n"
    prompt += f"- Body language should reinforce: {emotion}\n"
    prompt += f"- Color palette should support mood: {emotion}\n"
    
    # Add educational focus
    prompt += f"\n\nEDUCATIONAL PURPOSE: {educational_focus}\n"
    prompt += "- Include clear visual elements that teach this concept\n"
    prompt += "- Use arrows, labels, or inset diagrams if helpful for education\n"
    prompt += "- Make medical concepts accessible through simplified visuals\n"
    
    # Directional precision
    prompt += """

DIRECTIONAL SPECIFICATIONS:
- LEFT means viewer's left (character's right)
- RIGHT means viewer's right (character's left)
- Arrows must have clearly visible arrowheads pointing in specified direction
- Text must be horizontal and readable
- Shadows (if any are used despite flat style preference) cast in consistent direction

LIGHTING DIRECTION:
- Main light source from TOP-LEFT (45-degree angle)
- Minimal shadowing (flat cartoon style)
- Highlights on glasses and reflective surfaces only

COLOR SPECIFICATIONS (HEX CODES):
- Use exact hex codes for consistency
- Skin tones: Light Asian #F4E4D4, Latino #D4A66A
- Blood: Arterial #DC143C (crimson red), Venous #4169E1 (royal blue)
- Surgical field: Pink/red tones #FFB6C1 (light pink) to #DC143C (deep red)
- Plaque: Yellow-white #FFFACD (lemon chiffon) with gray (#696969) calcifications
- Scrubs: Teal #008B8B, Surgical gowns: Light green #90EE90
- Medical equipment: Silver/chrome #C0C0C0, White plastic #F5F5F5

TEXT AND LABELS:
- All text in SANS-SERIF font (Arial or Helvetica equivalent)
- Medical terms in smaller text with arrows pointing to relevant anatomy
- Spanish dialogue in speech bubbles with small English subtitles below
- Text must be HORIZONTAL (0 degrees rotation)
- Font color BLACK (#000000) on light backgrounds, WHITE (#FFFFFF) on dark backgrounds

FINAL QUALITY CHECKS:
- All characters present from character list? YES/NO
- Dr. Erben matches description (if present)? YES/NO
- Thick black outlines on all elements? YES/NO
- Flat colors with no gradients? YES/NO
- Landscape orientation 1536×1024? YES/NO
- Educational elements clear? YES/NO
- Emotion clearly conveyed? YES/NO
- All key elements included? YES/NO

RENDER THIS SCENE WITH MAXIMUM CLARITY AND EDUCATIONAL VALUE.
"""
    
    return prompt

# Generate all 40 prompts
output_dir = "individual-prompts"
os.makedirs(output_dir, exist_ok=True)

all_prompts = []

for panel in storyboard['panels']:
    panel_num = panel['panel_number']
    prompt = generate_panel_prompt(panel, panel_num)
    
    # Save individual prompt
    filename = f"{output_dir}/panel_{panel_num:02d}.txt"
    with open(filename, 'w') as f:
        f.write(prompt)
    
    all_prompts.append(f"{'='*80}\n{prompt}\n")
    print(f"✅ Generated prompt for Panel {panel_num}: {panel['title']}")

# Save combined file
with open("prompts-all-panels.txt", 'w') as f:
    f.write(f"SUPER-EXPLICIT PROMPTS FOR ALL 40 PANELS\n")
    f.write(f"Carotid Artery Stenosis V2 - Dr. Yuna Erben Story\n")
    f.write(f"{'='*80}\n\n")
    f.write('\n'.join(all_prompts))

print(f"\n✅ Generated all 40 prompts")
print(f"   Individual files: {output_dir}/panel_01.txt through panel_40.txt")
print(f"   Combined file: prompts-all-panels.txt")
print(f"   Average prompt length: {sum(len(p) for p in all_prompts) // 40} characters")

