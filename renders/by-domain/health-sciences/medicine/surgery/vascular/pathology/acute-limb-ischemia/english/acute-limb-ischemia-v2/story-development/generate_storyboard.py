#!/usr/bin/env python3
"""
Generate storyboard JSON for Acute Limb Ischemia V2 story.
35 panels following the narrative.
"""

import json

storyboard = {
    "story_title": "Acute Limb Ischemia - A Race Against Time",
    "version": "2.0",
    "character": {
        "name": "Dr. Young Erben",
        "ethnicity": "Korean",
        "age": "40s",
        "physical": "Petite",
        "distinctive_feature": "Expressive rectangular glasses",
        "languages": ["Spanish (Venezuelan)", "English", "German", "Korean"]
    },
    "patient": {
        "name": "Carlos Ramirez",
        "age": 68,
        "ethnicity": "Venezuelan immigrant",
        "condition": "Acute left leg ischemia from atrial fibrillation embolus"
    },
    "panel_count": 35,
    "acts": [
        {"act": 1, "title": "Emergency Recognition", "panels": "1-10"},
        {"act": 2, "title": "Surgical Preparation", "panels": "11-18"},
        {"act": 3, "title": "Surgical Procedure", "panels": "19-28"},
        {"act": 4, "title": "Recovery and Prevention", "panels": "29-35"}
    ],
    "panels": [
        # Act 1: Emergency Recognition
        {
            "panel_number": 1,
            "title": "The 3 AM Call",
            "scene": "Dr. Young Erben's bedroom, nightstand with phone ringing, clock showing 3:02 AM",
            "characters": ["Dr. Young Erben in pajamas, reaching for glasses"],
            "key_elements": ["Phone ringing", "Digital clock: 3:02 AM", "Glasses on nightstand", "Dark bedroom"],
            "dialogue": "Phone: *RING* Dr. Erben: 'Dr. Erben speaking...'",
            "educational_focus": "Emergency response - vascular surgeons on call 24/7",
            "emotional_tone": "Alert, immediate response to emergency"
        },
        {
            "panel_number": 2,
            "title": "Racing to Hospital",
            "scene": "Dr. Erben driving through empty pre-dawn streets, dashboard showing 3:11 AM",
            "characters": ["Dr. Erben in casual clothes, focused on driving"],
            "key_elements": ["Car dashboard with time", "Empty dark streets", "Hospital lights in distance", "Serious expression"],
            "dialogue": "Dr. Erben (thinking): 'Embolus vs thrombosis? Need to move fast - every minute counts.'",
            "educational_focus": "Time-critical nature of acute limb ischemia",
            "emotional_tone": "Urgency, professional focus"
        },
        {
            "panel_number": 3,
            "title": "ER Arrival - First Look",
            "scene": "Emergency room, Carlos on stretcher with pale left leg, wife crying nearby",
            "characters": ["Dr. Erben entering", "Carlos Ramirez in pain", "Maria (wife) distressed", "ER resident"],
            "key_elements": ["Obvious color difference between legs", "Pain on Carlos's face", "Clock showing 3:17 AM", "Medical equipment"],
            "dialogue": "ER Resident: 'He's been like this 4 hours. No pulses.'",
            "educational_focus": "Visual presentation of acute ischemia",
            "emotional_tone": "Critical assessment, family fear"
        },
        {
            "panel_number": 4,
            "title": "Speaking Spanish - Building Trust",
            "scene": "Bedside, Dr. Erben speaking to Carlos in Spanish",
            "characters": ["Dr. Erben leaning toward Carlos", "Carlos looking relieved", "Maria watching hopefully"],
            "key_elements": ["Spanish speech bubbles with English subtitles", "Relief on Carlos's face", "Hand on shoulder gesture", "Trust building moment"],
            "dialogue": "Dr. Erben (Spanish): '¡Señor Ramirez! Soy la Dra. Erben. Voy a examinar su pierna ahora.' [Mr. Ramirez! I'm Dr. Erben. I'm going to examine your leg now.]",
            "educational_focus": "Importance of language concordance in emergency medicine",
            "emotional_tone": "Relief, trust, connection"
        },
        {
            "panel_number": 5,
            "title": "The 6 Ps Assessment",
            "scene": "Systematic examination, close-up showing each of the 6 Ps being checked",
            "characters": ["Dr. Erben examining Carlos's leg methodically"],
            "key_elements": ["Checklist overlay showing: Pain ✓, Pallor ✓, Pulselessness ✓, Paresthesias ✓, Paralysis ✓, Poikilothermia ✓", "Pale leg", "Testing sensation", "Unable to move toes"],
            "dialogue": "Dr. Erben: 'All six Ps present. This is complete acute ischemia.'",
            "educational_focus": "The 6 Ps of acute limb ischemia - systematic assessment",
            "emotional_tone": "Clinical, thorough, concerning"
        },
        {
            "panel_number": 6,
            "title": "Doppler Ultrasound - Confirming the Worst",
            "scene": "Dr. Erben using handheld Doppler probe on Carlos's leg",
            "characters": ["Dr. Erben with Doppler", "Nurse listening", "Screen showing flat signal"],
            "key_elements": ["Doppler probe on ankle", "Speaker showing no signal (flat line)", "Volume knob turned up", "Femoral pulse normal (shown for contrast)"],
            "dialogue": "Dr. Erben: 'No arterial signals distally. Complete occlusion. But femoral pulse is strong - blockage is in between.'",
            "educational_focus": "Doppler ultrasound in vascular assessment",
            "emotional_tone": "Diagnostic certainty, gravity of situation"
        },
        {
            "panel_number": 7,
            "title": "EKG Shows Atrial Fibrillation",
            "scene": "Dr. Erben reviewing EKG strip with characteristic irregular rhythm",
            "characters": ["Dr. Erben holding EKG strip", "Carlos and Maria watching"],
            "key_elements": ["EKG strip showing AFib (irregularly irregular, no P waves)", "Dr. Erben pointing at rhythm", "Explanation diagram"],
            "dialogue": "Dr. Erben: 'Here's our culprit - atrial fibrillation. Carlos, ¿toma anticoagulantes?' [do you take blood thinners?] Carlos: 'No, doctora.'",
            "educational_focus": "Atrial fibrillation as source of arterial emboli",
            "emotional_tone": "Discovery, preventable disaster"
        },
        {
            "panel_number": 8,
            "title": "Wife's Fear of Amputation",
            "scene": "Maria bursting into exam room, face showing terror",
            "characters": ["Maria crying", "Carlos reaching for her", "Dr. Erben turning to face her"],
            "key_elements": ["Tears streaming", "Clutched hands", "Fear in eyes", "Desperate body language"],
            "dialogue": "Maria (Spanish): '¡Mi amor! Doctor, por favor, ¿van a cortar su pierna?' [My love! Doctor, please, are you going to cut off his leg?]",
            "educational_focus": "Patient/family fears in vascular emergencies",
            "emotional_tone": "Terror, desperation, need for reassurance"
        },
        {
            "panel_number": 9,
            "title": "The Race Against Time Explained",
            "scene": "Dr. Erben sitting eye-level with couple, drawing quick diagram",
            "characters": ["Dr. Erben seated with couple", "All focused on diagram"],
            "key_elements": ["Clock showing limited time", "Simple diagram of leg with blocked artery", "Catheter illustration", "Urgency in posture"],
            "dialogue": "Dr. Erben: 'We have 2-3 hours before permanent damage. We must move NOW. No delays.'",
            "educational_focus": "Golden window for limb salvage",
            "emotional_tone": "Urgency tempered with competence"
        },
        {
            "panel_number": 10,
            "title": "Informed Consent",
            "scene": "Carlos signing consent form, Dr. Erben explaining risks",
            "characters": ["Dr. Erben with consent form", "Carlos with trembling hand signing", "Maria holding his other hand"],
            "key_elements": ["Consent form visible", "List of risks", "Trembling signature", "Supportive touch"],
            "dialogue": "Carlos (Spanish): 'Haga lo que tenga que hacer, doctora.' [Do what you have to do, doctor.]",
            "educational_focus": "Informed consent in emergency vascular surgery",
            "emotional_tone": "Trust, fear, commitment"
        },
        
        # Act 2: Surgical Preparation
        {
            "panel_number": 11,
            "title": "Team Mobilization",
            "scene": "Dr. Erben outside ER making rapid phone calls, montage of team members waking up",
            "characters": ["Dr. Erben on phone", "Split panels showing: scrub tech waking, circulator answering phone, anesthesiologist getting ready"],
            "key_elements": ["Phone", "Clock: 3:42 AM", "Multiple small panels of team waking", "Hospital at night"],
            "dialogue": "Dr. Erben: 'Emergency OR. Acute limb ischemia. Fogarty embolectomy. 15 minutes.'",
            "educational_focus": "Mobilizing surgical team for emergencies",
            "emotional_tone": "Coordinated urgency, teamwork"
        },
        {
            "panel_number": 12,
            "title": "Heparin Bolus",
            "scene": "Nurse hanging heparin drip, IV going into Carlos's arm",
            "characters": ["Nurse with IV bag", "Carlos watching", "Dr. Erben checking dose calculation"],
            "key_elements": ["Heparin bag labeled", "Drip chamber", "IV line", "Calculation note: 70kg × 80 units/kg"],
            "dialogue": "Dr. Erben: 'This keeps the clot from getting worse while we prepare surgery.'",
            "educational_focus": "Anticoagulation in acute limb ischemia",
            "emotional_tone": "Medical precision, hope building"
        },
        {
            "panel_number": 13,
            "title": "Surgical Diagram",
            "scene": "Dr. Erben drawing simple diagram showing heart, leg, clot, catheter",
            "characters": ["Dr. Erben drawing", "Carlos and Maria studying diagram"],
            "key_elements": ["Paper with diagram", "Heart with X", "Leg with arrow", "Catheter with balloon", "Simple clear illustration"],
            "dialogue": "Dr. Erben: 'Clot formed here (heart), traveled here (leg), we go in here (groin), and pull it out.'",
            "educational_focus": "Patient education using visual aids",
            "emotional_tone": "Teaching, demystifying"
        },
        {
            "panel_number": 14,
            "title": "Carlos's Fear About Walking",
            "scene": "Close-up of Carlos's worried face",
            "characters": ["Carlos emotional", "Dr. Erben listening"],
            "key_elements": ["Tears in eyes", "Work-worn hands visible", "Fear and hope mixed", "Vulnerability"],
            "dialogue": "Carlos: 'Doctora, ¿podré caminar otra vez? I'm a gardener. My work, my life... it's all walking.' [Will I be able to walk again?]",
            "educational_focus": "Impact of vascular disease on livelihood and identity",
            "emotional_tone": "Vulnerability, existential fear"
        },
        {
            "panel_number": 15,
            "title": "Dr. Erben's Reassurance",
            "scene": "Dr. Erben holding Carlos's hand, speaking with quiet confidence",
            "characters": ["Dr. Erben", "Carlos", "Maria"],
            "key_elements": ["Hand holding", "Confident but compassionate expression", "Eye contact through glasses", "Bilingual speech bubbles"],
            "dialogue": "Dr. Erben: 'If we move quickly, yes - you will walk, you will work in your gardens again. Confía en mí.' [Trust me.]",
            "educational_focus": "Surgeon-patient relationship, realistic optimism",
            "emotional_tone": "Reassurance, competence"
        },
        {
            "panel_number": 16,
            "title": "OR Team Assembly",
            "scene": "Operating room, team laying out instruments",
            "characters": ["Scrub tech", "Circulating nurse", "Anesthesiologist", "Dr. Erben reviewing"],
            "key_elements": ["Fogarty catheter set visible", "Sterile blue drapes", "Surgical lights", "Checklist being verified", "Clock: 4:05 AM"],
            "dialogue": "Scrub Tech: 'Fogarty catheters ready - 3, 4, and 5 French. Vascular clamps, check.'",
            "educational_focus": "OR preparation for vascular emergency",
            "emotional_tone": "Professional readiness, precision"
        },
        {
            "panel_number": 17,
            "title": "Spinal Anesthesia",
            "scene": "Carlos positioned on side, anesthesiologist placing spinal",
            "characters": ["Carlos on side", "Anesthesiologist (Dr. Kim)", "Dr. Erben observing"],
            "key_elements": ["Spinal needle", "CSF visible", "Patient positioned", "Monitoring equipment"],
            "dialogue": "Dr. Kim: 'Small pinch, Carlos. Medication going in now. Legs will be numb in minutes.'",
            "educational_focus": "Spinal anesthesia for lower extremity vascular surgery",
            "emotional_tone": "Clinical, careful"
        },
        {
            "panel_number": 18,
            "title": "Surgical Prep and Draping",
            "scene": "Carlos's groin being prepped with betadine, team draping",
            "characters": ["Dr. Erben scrubbed and gowned", "Team draping patient"],
            "key_elements": ["Orange betadine", "Blue sterile drapes", "Only groin exposed", "Surgical lights positioned", "Time out checklist"],
            "dialogue": "Dr. Erben: 'Time out: Carlos Ramirez, 68, acute left leg ischemia, Fogarty embolectomy. Let's save this leg.'",
            "educational_focus": "Surgical time-out and sterile field preparation",
            "emotional_tone": "Final preparations, focus"
        },
        
        # Act 3: Surgical Procedure
        {
            "panel_number": 19,
            "title": "Groin Incision",
            "scene": "Dr. Erben making clean incision over femoral artery",
            "characters": ["Dr. Erben with scalpel", "Surgical assistant"],
            "key_elements": ["Scalpel blade on skin", "Blood welling up", "Straight 10cm incision", "Bovie cautery smoke"],
            "dialogue": "Dr. Erben: 'Knife. Bovie.'",
            "educational_focus": "Surgical approach to femoral artery",
            "emotional_tone": "Focused, precise"
        },
        {
            "panel_number": 20,
            "title": "Exposing Femoral Artery",
            "scene": "Dissection layers showing subcutaneous fat, fascia, then artery",
            "characters": ["Dr. Erben dissecting", "Assistant retracting"],
            "key_elements": ["Weitlaner retractor", "Yellow fat layer", "Femoral artery pulsating", "Vessel loops"],
            "dialogue": "Dr. Erben: 'Good proximal flow. Isolating the vessels now.'",
            "educational_focus": "Surgical anatomy of femoral triangle",
            "emotional_tone": "Methodical, skilled"
        },
        {
            "panel_number": 21,
            "title": "Arteriotomy - Clot Visible",
            "scene": "Opening the artery, dark clot visible inside",
            "characters": ["Dr. Erben cutting into vessel", "Team leaning in"],
            "key_elements": ["Small longitudinal incision in artery", "Dark red clot protruding", "Satinsky clamp", "Bulldog clamps"],
            "dialogue": "Dr. Erben: 'There's our culprit. Look at the size of that embolus.'",
            "educational_focus": "Arteriotomy technique, identifying embolus",
            "emotional_tone": "Discovery, vindication"
        },
        {
            "panel_number": 22,
            "title": "Fogarty Catheter Insertion",
            "scene": "Dr. Erben advancing thin catheter into artery",
            "characters": ["Dr. Erben with catheter", "Assistant watching"],
            "key_elements": ["4-French Fogarty catheter", "Balloon deflated", "Catheter advancing distally", "Measuring marks on catheter"],
            "dialogue": "Dr. Erben: 'Advancing... 10cm... 20cm... 30cm... there's resistance. That's as far as it goes.'",
            "educational_focus": "Fogarty catheter technique",
            "emotional_tone": "Technical precision"
        },
        {
            "panel_number": 23,
            "title": "Balloon Inflation Explained",
            "scene": "Close-up diagram overlay showing balloon inflating inside artery",
            "characters": ["Dr. Erben holding syringe", "Scrub tech watching"],
            "key_elements": ["Diagram showing: catheter tip, balloon inflating against vessel wall, clot ahead of balloon", "0.5mL syringe", "Teaching moment"],
            "dialogue": "Dr. Erben (teaching): 'See how the balloon creates a seal? As I pull back, it drags the clot along. Like a plunger in a pipe.'",
            "educational_focus": "Mechanism of Fogarty thromboembolectomy",
            "emotional_tone": "Educational, demonstrative"
        },
        {
            "panel_number": 24,
            "title": "First Pass Extraction",
            "scene": "Large clot being pulled out of arteriotomy",
            "characters": ["Dr. Erben pulling catheter steadily", "Team gasping"],
            "key_elements": ["Massive 8cm clot emerging", "Dark red color", "Cast-shaped like artery", "Basin catching clot", "Amazed expressions"],
            "dialogue": "Dr. Erben: 'Here it comes... SPLOP! That's what was blocking his leg.'",
            "educational_focus": "Embolus removal, size of typical cardiac embolus",
            "emotional_tone": "Satisfaction, but work not done"
        },
        {
            "panel_number": 25,
            "title": "Multiple Passes",
            "scene": "Repeated catheter passes, progressively smaller clots",
            "characters": ["Dr. Erben working methodically", "Basin filling with clots"],
            "key_elements": ["Multiple clot fragments", "3-French catheter for smaller vessels", "Pass count: 1st, 2nd, 3rd... 7th", "Getting smaller clots each time"],
            "dialogue": "Dr. Erben: 'Keep going until we get fresh bleeding from below. Pass 2... pass 3... pass 4...'",
            "educational_focus": "Complete clot clearance requires multiple passes",
            "emotional_tone": "Persistence, thoroughness"
        },
        {
            "panel_number": 26,
            "title": "Fresh Bleeding - Sign of Success",
            "scene": "Bright red blood pulsing from arteriotomy",
            "characters": ["Dr. Erben observing blood color", "Anesthesiologist noting foot color"],
            "key_elements": ["Bright red vs dark red comparison", "Pulsatile flow", "Foot visible at edge turning pink"],
            "dialogue": "Dr. Erben: 'Look at that color - fresh, oxygenated blood! Distal vessels are patent. We're clear!'",
            "educational_focus": "Back-bleeding as sign of successful revascularization",
            "emotional_tone": "Relief, success"
        },
        {
            "panel_number": 27,
            "title": "Patch Angioplasty",
            "scene": "Dr. Erben suturing bovine pericardial patch over arteriotomy",
            "characters": ["Dr. Erben with needle holder", "Assistant cutting suture"],
            "key_elements": ["Patch material visible", "6-0 Prolene suture", "Even stitches", "Widened vessel lumen"],
            "dialogue": "Dr. Erben: 'Patching prevents narrowing. We didn't go through all this just to have it close up again.'",
            "educational_focus": "Patch angioplasty technique to prevent stenosis",
            "emotional_tone": "Meticulous, preventing recurrence"
        },
        {
            "panel_number": 28,
            "title": "Final Check - Foot Pink",
            "scene": "Dr. Erben feeling for pedal pulses, foot now healthy pink color",
            "characters": ["Dr. Erben at foot level", "Team observing"],
            "key_elements": ["Dorsalis pedis pulse visible", "Posterior tibial pulse", "Pink foot vs previous pale", "Doppler confirming flow", "Toes normal color"],
            "dialogue": "Dr. Erben: 'Dorsalis pedis pulse - present! Posterior tibial - present! Triphasic signals! This leg is saved!'",
            "educational_focus": "Assessment of successful revascularization",
            "emotional_tone": "Victory, triumph"
        },
        
        # Act 4: Recovery and Prevention
        {
            "panel_number": 29,
            "title": "Wiggling Toes",
            "scene": "Recovery room, Carlos moving his toes",
            "characters": ["Carlos in bed", "Dr. Erben at bedside", "Maria holding hand", "All emotional"],
            "key_elements": ["Toes wiggling", "Tears of joy", "Relief on all faces", "Movement arrows"],
            "dialogue": "Dr. Erben: '¿Puedes mover los dedos?' Carlos: '¡Puedo moverlos! ¡Doctora, puedo moverlos!' [Can you move your toes? I can move them!]",
            "educational_focus": "Early recovery signs after revascularization",
            "emotional_tone": "Joy, relief, miracle of restoration"
        },
        {
            "panel_number": 30,
            "title": "Explaining the Source",
            "scene": "Dr. Erben with tablet showing heart diagram",
            "characters": ["Dr. Erben teaching", "Carlos and Maria learning"],
            "key_elements": ["Heart diagram on tablet", "AFib rhythm shown", "Clot formation illustrated", "Travel path indicated"],
            "dialogue": "Dr. Erben: 'Your heart's irregular rhythm caused blood to pool. That formed a clot. The clot traveled to your leg.'",
            "educational_focus": "Pathophysiology of cardiogenic emboli",
            "emotional_tone": "Educational, connecting dots"
        },
        {
            "panel_number": 31,
            "title": "Cardiology Consultation Coming",
            "scene": "Dr. Erben explaining need for anticoagulation",
            "characters": ["Dr. Erben drawing cascade", "Family listening intently"],
            "key_elements": ["Diagram: AFib → clot → travel → blockage", "Breaking the chain at step 2", "Prescription pad visible"],
            "dialogue": "Dr. Erben: 'We need to break this chain. Blood thinners stop new clots from forming. For life, Maria. For life.'",
            "educational_focus": "Prevention of recurrent emboli",
            "emotional_tone": "Serious, preventive focus"
        },
        {
            "panel_number": 32,
            "title": "The Critical Question",
            "scene": "Maria asking about previous care failure",
            "characters": ["Maria emotional", "Carlos listening", "Dr. Erben empathetic"],
            "key_elements": ["Tears", "Guilt and anger on Maria's face", "Dr. Erben's compassionate expression", "System failure acknowledgment"],
            "dialogue": "Maria: '¿Por qué didn't they give him blood thinners before? This should have been prevented!' [Why...]",
            "educational_focus": "System failures, importance of appropriate anticoagulation",
            "emotional_tone": "Accountability, system critique"
        },
        {
            "panel_number": 33,
            "title": "Education About Stroke Risk",
            "scene": "Dr. Erben showing statistics and stroke risk diagram",
            "characters": ["Dr. Erben with tablet", "Family seeing stroke illustration"],
            "key_elements": ["Brain diagram with blocked vessel", "5% risk without treatment", "<1% with treatment", "Risk vs benefit chart"],
            "dialogue": "Dr. Erben: 'Without blood thinners: 5% yearly risk of stroke or another clot. With them: <1%. This is about preventing a stroke that could be devastating.'",
            "educational_focus": "Stroke risk in atrial fibrillation, benefits of anticoagulation",
            "emotional_tone": "Serious education, informed decision"
        },
        {
            "panel_number": 34,
            "title": "Discharge Planning",
            "scene": "Discharge teaching two days later",
            "characters": ["Dr. Erben with folder of papers", "Carlos dressed", "Maria taking notes"],
            "key_elements": ["Coumadin prescription", "INR monitoring schedule", "Lab orders", "Cardiology appointment card", "Dietary instructions"],
            "dialogue": "Dr. Erben: 'Coumadin starts tonight. Lab tomorrow for INR check. Goal 2 to 3. Cardiology appointment next week - don't miss it.'",
            "educational_focus": "Anticoagulation management, monitoring requirements",
            "emotional_tone": "Practical, ensuring follow-through"
        },
        {
            "panel_number": 35,
            "title": "Three-Month Follow-Up - Dancing Again",
            "scene": "Clinic three months later, Carlos dancing with Maria",
            "characters": ["Carlos demonstrating his leg strength", "Maria smiling", "Dr. Erben watching with emotion"],
            "key_elements": ["Carlos's dance steps", "No limp", "Strong gait", "Joy on all faces", "Garden tools visible (back to work)", "INR log showing 2.5"],
            "dialogue": "Carlos: 'Doctora, mira esto! Back in my gardens. Walking miles. Even dancing!' Dr. Erben: 'This is success, Carlos. You saved your own leg by following the plan.'",
            "educational_focus": "Long-term success with appropriate management",
            "emotional_tone": "Triumph, life restored, full circle"
        }
    ]
}

# Write to JSON file
output_file = "03-storyboard.json"
with open(output_file, 'w') as f:
    json.dump(storyboard, f, indent=2)

print(f"Storyboard JSON created: {output_file}")
print(f"Total panels: {len(storyboard['panels'])}")
print("Acts:")
for act in storyboard['acts']:
    print(f"  Act {act['act']}: {act['title']} (Panels {act['panels']})")
