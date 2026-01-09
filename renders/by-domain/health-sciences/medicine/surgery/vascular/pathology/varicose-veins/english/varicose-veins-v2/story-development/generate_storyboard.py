#!/usr/bin/env python3
"""
Generate detailed storyboard JSON for Varicose Veins V2 story.
Creates 32-panel storyboard with complete scene descriptions for each panel.
"""

import json

def create_storyboard():
    """Create complete 32-panel storyboard based on narrative."""
    
    storyboard = {
        "story_title": "Varicose Veins: From Discomfort to Dancing",
        "character": "Dr. Young Erben",
        "patient": "Elena Vasquez, 45, Venezuelan elementary school teacher",
        "panel_count": 32,
        "acts": 4,
        "panels": []
    }
    
    # Act 1: Recognition & Diagnosis (Panels 1-10)
    panels_act1 = [
        {
            "panel": 1,
            "title": "After School Ache",
            "scene": "Elena in classroom at end of day, sitting at desk with visible exhaustion",
            "characters": ["Elena Vasquez"],
            "key_elements": ["Classroom setting", "Elena rubbing swollen ankles", "Visible varicose veins on legs", "Clock showing 4 PM"],
            "dialogue": "Elena (Spanish): 'Mis piernas me están matando...' (My legs are killing me...)",
            "educational_focus": "Symptom recognition - leg aching after prolonged standing",
            "emotional_tone": "Tired, uncomfortable"
        },
        {
            "panel": 2,
            "title": "Six Months of Discomfort",
            "scene": "Split panel showing Elena's progression over 6 months",
            "characters": ["Elena Vasquez"],
            "key_elements": ["September: mild discomfort", "December: visible veins", "March: swelling ankles", "Timeline visual"],
            "dialogue": "Narration: 'What started as mild aching had become constant pain'",
            "educational_focus": "Disease progression timeline",
            "emotional_tone": "Progressive concern"
        },
        {
            "panel": 3,
            "title": "The Morning Routine",
            "scene": "Elena's bedroom, morning light, examining legs in mirror",
            "characters": ["Elena Vasquez"],
            "key_elements": ["Full-length mirror", "Twisted blue-purple veins visible", "Compression stockings on dresser", "Concerned expression"],
            "dialogue": "Elena (thinking): 'These veins are getting worse...'",
            "educational_focus": "Visual appearance of varicose veins - twisted, enlarged",
            "emotional_tone": "Self-conscious, worried"
        },
        {
            "panel": 4,
            "title": "Daughter's Concern",
            "scene": "Kitchen table, Elena and her daughter Sofia having breakfast",
            "characters": ["Elena Vasquez", "Sofia (daughter, 20)"],
            "key_elements": ["Kitchen setting", "Elena wincing while standing", "Sofia noticing", "Venezuelan breakfast foods"],
            "dialogue": "Sofia (Spanish): 'Mamá, you need to see a doctor about your legs!'",
            "educational_focus": "Family recognition of symptoms",
            "emotional_tone": "Caring concern"
        },
        {
            "panel": 5,
            "title": "Primary Care Visit",
            "scene": "Primary care clinic exam room",
            "characters": ["Elena Vasquez", "Primary care physician"],
            "key_elements": ["Exam table", "Doctor examining legs", "Chart showing venous anatomy", "Referral paperwork"],
            "dialogue": "Doctor: 'These need evaluation by a vascular surgeon. I'm referring you to Dr. Erben.'",
            "educational_focus": "Referral pathway for varicose veins",
            "emotional_tone": "Professional concern"
        },
        {
            "panel": 6,
            "title": "Meeting Dr. Erben",
            "scene": "Vascular surgery clinic, Dr. Erben's office",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Dr. Erben - petite, Korean, 40s, expressive glasses", "Comfortable office setting", "Medical models of veins", "Warm greeting"],
            "dialogue": "Dr. Erben (Spanish): '¡Bienvenida, Elena! Tell me about your legs.'",
            "educational_focus": "Patient-centered consultation, multilingual care",
            "emotional_tone": "Warm, trusting"
        },
        {
            "panel": 7,
            "title": "Venous Ultrasound",
            "scene": "Ultrasound room, Elena lying on exam table",
            "characters": ["Dr. Young Erben", "Elena Vasquez", "Sonographer"],
            "key_elements": ["Ultrasound machine", "Probe on leg", "Screen showing blood flow", "Color Doppler imaging"],
            "dialogue": "Dr. Erben: 'The ultrasound shows which valves aren't working properly.'",
            "educational_focus": "Venous duplex ultrasound - diagnostic tool",
            "emotional_tone": "Technical, informative"
        },
        {
            "panel": 8,
            "title": "Explaining the Problem",
            "scene": "Consultation room with anatomical diagram",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Diagram of leg veins", "Normal vs. insufficient valves", "Great saphenous vein highlighted", "CEAP classification chart"],
            "dialogue": "Dr. Erben (Spanish): 'The valves in your saphenous vein are leaking - we call this reflux.'",
            "educational_focus": "Venous insufficiency pathophysiology, CEAP C3-C4",
            "emotional_tone": "Educational, clear"
        },
        {
            "panel": 9,
            "title": "Treatment Options",
            "scene": "Same consultation room, reviewing treatment flowchart",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Treatment options chart", "EVLA diagram", "Before/after photos", "Insurance information"],
            "dialogue": "Dr. Erben: 'Endovenous laser ablation - EVLA - is minimally invasive and very effective.'",
            "educational_focus": "Treatment options - conservative vs. interventional",
            "emotional_tone": "Informative, hopeful"
        },
        {
            "panel": 10,
            "title": "Decision to Proceed",
            "scene": "Consultation room, Elena signing consent forms",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Consent forms", "Procedure scheduling calendar", "Educational pamphlets", "Hopeful expressions"],
            "dialogue": "Elena (Spanish): '¡Sí! I want to be able to stand and teach without pain again.'",
            "educational_focus": "Informed consent process",
            "emotional_tone": "Hopeful determination"
        }
    ]
    
    # Act 2: Planning & Preparation (Panels 11-16)
    panels_act2 = [
        {
            "panel": 11,
            "title": "Pre-Op Instructions",
            "scene": "Clinic, nurse going over pre-procedure instructions",
            "characters": ["Elena Vasquez", "Pre-op nurse"],
            "key_elements": ["Instruction sheet", "Medications list", "Compression stockings", "Checklist"],
            "dialogue": "Nurse: 'Stop aspirin 7 days before. Bring loose pants for after the procedure.'",
            "educational_focus": "Pre-operative preparation",
            "emotional_tone": "Practical, organized"
        },
        {
            "panel": 12,
            "title": "The Night Before",
            "scene": "Elena's bedroom, evening, preparing for tomorrow",
            "characters": ["Elena Vasquez", "Sofia"],
            "key_elements": ["Laid out comfortable clothes", "Reminder notes", "Sofia offering support", "Calm atmosphere"],
            "dialogue": "Sofia: 'I'll drive you tomorrow, Mamá. Everything will be fine.'",
            "educational_focus": "Family support importance",
            "emotional_tone": "Nervous anticipation, supported"
        },
        {
            "panel": 13,
            "title": "Procedure Day Arrival",
            "scene": "Outpatient surgery center entrance, morning",
            "characters": ["Elena Vasquez", "Sofia"],
            "key_elements": ["Modern facility exterior", "Clear signage", "Elena and Sofia walking in", "Morning sunlight"],
            "dialogue": "Elena: 'Here we go...'",
            "educational_focus": "Outpatient setting for EVLA",
            "emotional_tone": "Nervous but ready"
        },
        {
            "panel": 14,
            "title": "Check-In and Prep",
            "scene": "Pre-procedure area, Elena changing into gown",
            "characters": ["Elena Vasquez", "Pre-op nurse"],
            "key_elements": ["Private prep bay", "Hospital gown", "IV setup", "Vital signs monitoring"],
            "dialogue": "Nurse: 'We'll start an IV and mark the vein we're treating.'",
            "educational_focus": "Pre-procedure preparation steps",
            "emotional_tone": "Clinical, professional"
        },
        {
            "panel": 15,
            "title": "Dr. Erben's Pre-Op Visit",
            "scene": "Pre-op bay, Dr. Erben explaining final details",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Dr. Erben marking leg with marker", "Ultrasound machine nearby", "Consent verification", "Reassuring interaction"],
            "dialogue": "Dr. Erben (Spanish): 'I'll be with you the whole time. You'll be awake but comfortable.'",
            "educational_focus": "Local anesthesia vs. general - procedure can be done awake",
            "emotional_tone": "Reassuring, professional"
        },
        {
            "panel": 16,
            "title": "To the Procedure Room",
            "scene": "Hallway, Elena on gurney being wheeled to procedure room",
            "characters": ["Elena Vasquez", "Transport staff"],
            "key_elements": ["Hospital corridor", "Procedure room doors ahead", "Elena looking determined", "Clean, modern facility"],
            "dialogue": "Elena (thinking): 'Soon I'll be able to stand all day without pain...'",
            "educational_focus": "Outpatient procedure setting",
            "emotional_tone": "Determined, hopeful"
        }
    ]
    
    # Act 3: EVLA Procedure (Panels 17-26)
    panels_act3 = [
        {
            "panel": 17,
            "title": "Procedure Room Setup",
            "scene": "Modern EVLA procedure room with ultrasound and laser equipment",
            "characters": ["Dr. Young Erben", "Nurse", "Sonographer"],
            "key_elements": ["Procedure table", "Ultrasound machine", "Laser generator", "Sterile draping", "Monitoring equipment"],
            "dialogue": "Dr. Erben: 'Let's get started. Elena, you'll feel some cold from the cleaning solution.'",
            "educational_focus": "EVLA equipment and setup",
            "emotional_tone": "Professional, focused"
        },
        {
            "panel": 18,
            "title": "Ultrasound Guidance",
            "scene": "Close-up of ultrasound probe on Elena's leg",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Ultrasound probe", "Screen showing vein", "Dr. Erben's focused expression", "Elena calm on table"],
            "dialogue": "Dr. Erben: 'I'm using ultrasound to see the vein and guide the needle.'",
            "educational_focus": "Ultrasound-guided access",
            "emotional_tone": "Focused, technical"
        },
        {
            "panel": 19,
            "title": "Accessing the Vein",
            "scene": "Dr. Erben inserting catheter into saphenous vein",
            "characters": ["Dr. Young Erben", "Elena Vasquez", "Nurse"],
            "key_elements": ["Small needle insertion", "Guidewire visible", "Ultrasound screen", "Dr. Erben's steady hands"],
            "dialogue": "Dr. Erben: 'Small stick - just like getting blood drawn. You're doing great, Elena.'",
            "educational_focus": "Percutaneous venous access",
            "emotional_tone": "Calm, reassuring"
        },
        {
            "panel": 20,
            "title": "Laser Fiber Insertion",
            "scene": "Threading laser fiber through catheter",
            "characters": ["Dr. Young Erben", "Sonographer"],
            "key_elements": ["Laser fiber being advanced", "Ultrasound showing fiber tip position", "Measurement markings", "Precise technique"],
            "dialogue": "Dr. Erben: 'Threading the laser fiber all the way up to the saphenofemoral junction.'",
            "educational_focus": "Laser fiber positioning",
            "emotional_tone": "Technical precision"
        },
        {
            "panel": 21,
            "title": "Tumescent Anesthesia",
            "scene": "Dr. Erben injecting anesthetic around the vein",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Multiple small injections", "Ultrasound guidance", "Anesthetic solution spreading", "Pain-free technique"],
            "dialogue": "Dr. Erben (Spanish): 'Multiple tiny injections of numbing medicine around the vein. This protects surrounding tissue.'",
            "educational_focus": "Tumescent anesthesia technique",
            "emotional_tone": "Careful, methodical"
        },
        {
            "panel": 22,
            "title": "Activating the Laser",
            "scene": "Laser generator activated, fiber glowing",
            "characters": ["Dr. Young Erben", "Nurse monitoring laser"],
            "key_elements": ["Laser console display", "Power settings", "Fiber tip glowing", "Safety goggles", "Controlled energy delivery"],
            "dialogue": "Dr. Erben: 'Laser activated. We'll slowly pull back the fiber, sealing the vein as we go.'",
            "educational_focus": "Endovenous laser ablation mechanism",
            "emotional_tone": "Technical, controlled"
        },
        {
            "panel": 23,
            "title": "Pullback Technique",
            "scene": "Dr. Erben slowly withdrawing fiber through vein",
            "characters": ["Dr. Young Erben", "Sonographer"],
            "key_elements": ["Measured pullback", "Ultrasound showing vein closure", "Timer display", "Precise technique", "Team coordination"],
            "dialogue": "Sonographer: 'Good closure throughout. The vein is sealing perfectly.'",
            "educational_focus": "Controlled pullback ensures complete ablation",
            "emotional_tone": "Focused teamwork"
        },
        {
            "panel": 24,
            "title": "Treating Additional Veins",
            "scene": "Dr. Erben using phlebectomy hooks for varicosities",
            "characters": ["Dr. Young Erben", "Elena Vasquez", "Nurse"],
            "key_elements": ["Tiny incisions", "Phlebectomy hooks", "Removing bulging veins", "Minimal invasiveness"],
            "dialogue": "Dr. Erben: 'Now removing these bulging veins through tiny incisions - they'll heal without stitches.'",
            "educational_focus": "Ambulatory phlebectomy for varicosities",
            "emotional_tone": "Thorough, meticulous"
        },
        {
            "panel": 25,
            "title": "Final Checks",
            "scene": "Dr. Erben doing ultrasound to verify complete closure",
            "characters": ["Dr. Young Erben", "Sonographer"],
            "key_elements": ["Ultrasound scan", "No blood flow in treated vein", "Satisfied expression", "Quality verification"],
            "dialogue": "Dr. Erben: 'Perfect! The vein is completely closed with no flow. Excellent result.'",
            "educational_focus": "Immediate verification of treatment success",
            "emotional_tone": "Satisfied, professional"
        },
        {
            "panel": 26,
            "title": "Applying Compression",
            "scene": "Nurse applying compression stocking",
            "characters": ["Elena Vasquez", "Nurse"],
            "key_elements": ["Compression stocking", "Leg bandaging", "Elena sitting up", "Relief visible"],
            "dialogue": "Nurse: 'Compression stocking goes on now. Wear it for one week.'",
            "educational_focus": "Post-procedure compression importance",
            "emotional_tone": "Care completion, relief"
        }
    ]
    
    # Act 4: Recovery & Results (Panels 27-32)
    panels_act4 = [
        {
            "panel": 27,
            "title": "Walking Out",
            "scene": "Elena walking out of procedure room unassisted",
            "characters": ["Elena Vasquez", "Dr. Young Erben", "Sofia"],
            "key_elements": ["Elena walking steadily", "Sofia's surprised expression", "Dr. Erben smiling", "Discharge papers"],
            "dialogue": "Elena: '¡No puedo creerlo! I just walked after the procedure!'",
            "educational_focus": "Immediate ambulation after EVLA",
            "emotional_tone": "Amazed, happy"
        },
        {
            "panel": 28,
            "title": "Post-Op Instructions",
            "scene": "Discharge area, reviewing care instructions",
            "characters": ["Elena Vasquez", "Sofia", "Discharge nurse"],
            "key_elements": ["Instruction sheets", "Activity guidelines", "Follow-up appointment card", "Pain medication"],
            "dialogue": "Nurse: 'Walk 30 minutes daily. No heavy lifting for 2 weeks. Call if you have concerns.'",
            "educational_focus": "Post-EVLA care instructions",
            "emotional_tone": "Informative, supportive"
        },
        {
            "panel": 29,
            "title": "One Week Follow-Up",
            "scene": "Clinic exam room, Elena showing legs to Dr. Erben",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Healing incisions", "Reduced swelling", "Dr. Erben examining", "Positive progress"],
            "dialogue": "Dr. Erben: 'Healing beautifully! How are your symptoms?'",
            "educational_focus": "Early follow-up assessment",
            "emotional_tone": "Positive progress"
        },
        {
            "panel": 30,
            "title": "Back to Teaching",
            "scene": "Elena in classroom, teaching energetically, no pain",
            "characters": ["Elena Vasquez", "Students"],
            "key_elements": ["Elena standing comfortably all day", "Engaged students", "No leg pain visible", "Compression stocking still on"],
            "dialogue": "Elena (thinking): 'I can stand all day without pain! It's amazing!'",
            "educational_focus": "Return to normal activities",
            "emotional_tone": "Energetic, grateful"
        },
        {
            "panel": 31,
            "title": "Three-Month Result",
            "scene": "Clinic, Dr. Erben showing Elena her ultrasound results",
            "characters": ["Dr. Young Erben", "Elena Vasquez"],
            "key_elements": ["Ultrasound screen showing closed vein", "Before/after comparison", "Elena's legs looking normal", "Successful outcome"],
            "dialogue": "Dr. Erben: 'The vein is completely closed. Your symptoms are gone. Perfect result!'",
            "educational_focus": "Long-term EVLA success",
            "emotional_tone": "Successful, satisfied"
        },
        {
            "panel": 32,
            "title": "Dancing at the Festival",
            "scene": "Community Venezuelan festival, Elena dancing with Sofia",
            "characters": ["Elena Vasquez", "Sofia", "Festival crowd"],
            "key_elements": ["Venezuelan music/dance", "Elena dancing energetically", "No compression stockings", "Legs looking normal", "Joy and celebration"],
            "dialogue": "Elena (Spanish): '¡Bailemos! My legs feel like they're 20 years younger!'",
            "educational_focus": "Full recovery and return to active lifestyle",
            "emotional_tone": "Joyful celebration, quality of life restored"
        }
    ]
    
    # Combine all panels
    storyboard["panels"] = panels_act1 + panels_act2 + panels_act3 + panels_act4
    
    return storyboard

def main():
    """Generate and save storyboard JSON."""
    storyboard = create_storyboard()
    
    with open('03-storyboard.json', 'w', encoding='utf-8') as f:
        json.dump(storyboard, f, ensure_ascii=False, indent=2)
    
    print(f"Generated storyboard with {len(storyboard['panels'])} panels")
    print(f"Saved to: 03-storyboard.json")

if __name__ == "__main__":
    main()
