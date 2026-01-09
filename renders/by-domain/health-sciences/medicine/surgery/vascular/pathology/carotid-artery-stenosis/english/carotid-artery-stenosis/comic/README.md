# Carotid Artery Stenosis - The Stroke Prevention Mystery
## Educational Comic Series - 32 Panels

**Medical Topic**: Carotid artery stenosis, transient ischemic attack (TIA), carotid endarterectomy  
**Target Audience**: Medical students, residents, patients, general public  
**Style**: Dora the Explorer inspired cartoon  
**Status**: ✅ Complete with 32 images generated

---

## Story Overview

Follow the medical team of Camila, Camilo, and Diego as they manage Mr. Rodriguez, a 68-year-old patient who experienced transient vision loss. This urgent case teaches stroke prevention through carotid endarterectomy.

### Patient Case
- **Patient**: Mr. Rodriguez, 68 years old
- **Chief Complaint**: "Like a curtain came down over my eye"
- **Diagnosis**: 80% carotid artery stenosis with heterogeneous plaque
- **Risk Factors**: Diabetes, 20-year smoking history, hypertension
- **Treatment**: Carotid endarterectomy under regional anesthesia

---

## Learning Objectives

By the end of this story, learners will understand:

1. **TIA Pathophysiology**
   - Transient ischemic attack as a warning sign
   - Embolic mechanism from unstable carotid plaque
   - The "ticking time bomb" concept

2. **Clinical Assessment**
   - Physical exam: detecting carotid bruit
   - Significance of classic stroke risk factors
   - Urgency in stroke prevention

3. **Diagnostic Workup**
   - Duplex ultrasound velocity criteria
   - CT angiography for plaque characterization
   - Identification of ulcerated/vulnerable plaque

4. **Surgical Decision-Making**
   - NASCET trial criteria (>70% stenosis)
   - Symptomatic vs asymptomatic stenosis
   - Carotid endarterectomy vs carotid stenting

5. **Procedural Details**
   - Regional anesthesia vs general anesthesia
   - Neuromonitoring during surgery
   - Arteriotomy and plaque extraction technique
   - Patch angioplasty closure

6. **Post-Operative Care**
   - Immediate neurologic assessment
   - Pathology confirmation of unstable plaque
   - Long-term antiplatelet therapy
   - Stroke prevention strategies

---

## Story Arc (32 Panels)

### Act 1: The Mystery (Panels 1-8)
1. Emergency consult - "curtain coming down" vision loss
2. Patient history review - diabetes, smoking, hypertension
3. Physical exam - detecting carotid bruit
4. Dr. Erben explains TIA pathophysiology
5. Camilo orders duplex ultrasound
6. Ultrasound reveals 80% stenosis
7. Team discusses stroke risk
8. Decision to proceed with surgical intervention

### Act 2: Investigation (Panels 9-16)
9. Camila researches NASCET trial
10. CT angiography shows ulcerated plaque
11. Diego compares endarterectomy vs stenting
12. Presentation to vascular surgery team
13. Surgical planning - exposure, shunt consideration
14. Neurologic monitoring discussion
15. Patient education about procedure
16. Regional anesthesia discussion

### Act 3: The Procedure (Panels 17-24)
17. OR setup with neuromonitoring
18. Cervical block administration
19. Surgical exposure of carotid bifurcation
20. Cross-clamping and neurologic monitoring
21. Arteriotomy reveals unstable plaque
22. Plaque extraction - the culprit removed
23. Closure with patch angioplasty
24. Post-op neuro check - success!

### Act 4: Success & Learning (Panels 25-32)
25. Post-op day 1 - patient doing well
26. Pathology report confirms unstable plaque
27. Literature review on stroke prevention
28. Long-term management planning
29. Patient gratitude and education
30. Dr. Erben's teaching moment
31. Team reflection on rapid decision-making
32. Teaser for next case

---

## Files in This Directory

### Generated Content
- **`storyboard.json`** - Complete 32-panel story structure with dialogue
- **`prompts-all-panels.txt`** - Super-explicit prompts for all 32 panels (304KB)
- **`individual-prompts/`** - Individual prompt files (panel_01.txt through panel_32.txt)
- **`panels-gpt/`** - All 32 generated images (PNG, 1536x1024, 144MB total)
  - `image_001_*.png` through `image_032_*.png`
  - `metadata_*.json` - Generation metadata for each image

### Tools
- **`generate_prompts.py`** - Script to generate prompts from storyboard JSON
- **`prompts-first-8.txt`** - First batch of prompts for parallel generation
- **`prompts-panels-9-16.txt`** - Second batch
- **`prompts-panels-17-24.txt`** - Third batch
- **`prompts-panels-25-32.txt`** - Fourth batch

---

## Image Specifications

### Technical Details
- **Resolution**: 1536 x 1024 pixels (landscape, 3:2 aspect ratio)
- **Format**: PNG, high quality
- **Total Size**: 144MB (32 images)
- **Average Size**: ~4.5MB per image
- **Generation Method**: GPT Image 1.5 via Azure AI Foundry
- **Batch Generation**: 4 batches of 8 images (parallel)

### Visual Style
- **Art Style**: Dora the Explorer TV show cartoon
- **Line Work**: THICK BLACK OUTLINES (3-4px) around all elements
- **Proportions**: Simplified cartoon (heads 1/4 of body height)
- **Eyes**: LARGE EXPRESSIVE (30% of face height)
- **Colors**: FLAT, BRIGHT, SATURATED (no gradients)
- **Features**: Simple dot noses, curved line mouths
- **Lighting**: Flat with simple 30% opacity shadows

### Characters (Consistent Across All Panels)
1. **Camila** - Lead Vascular Surgery Resident
   - Teal explorer vest with sunflower patch
   - Stethoscope, clipboard
   - Warm brown eyes, long braid

2. **Camilo** - Med Student, Tech Expert
   - Navy blue hoodie with medical school patch
   - Tablet computer
   - Spiky hair, tech-savvy

3. **Diego** - Surgical Fellow
   - Red polo shirt
   - Stethoscope, medical reference book
   - Thoughtful, research-focused

4. **Dr. Erben** - Attending Vascular Surgeon
   - Navy scrubs with white coat
   - Experienced, authoritative but friendly
   - Gray hair, wise expression

5. **Mr. Rodriguez** - Patient
   - Latino heritage, 70s
   - Concerned but trusting
   - Hospital gown or casual clothes

---

## Usage Instructions

### Viewing Images
Images are named sequentially:
```
image_001_*.png - Panel 1: Emergency Consult
image_002_*.png - Panel 2: Patient History
...
image_032_*.png - Panel 32: Preview Next Case
```

Open in any image viewer or use for presentations, documents, or educational materials.

### Regenerating Images
If you need to regenerate any images:

```bash
cd /path/to/carotid-artery-stenosis/comic/

# Regenerate all prompts
python3 generate_prompts.py

# Generate images (requires Azure AI Foundry credentials)
python3 /path/to/gpt_image_generator.py \
  --prompt-file prompts-all-panels.txt \
  --output-dir panels-gpt \
  --parallel 8 \
  --aspect landscape \
  --quality high
```

### Creating Documents
Images can be compiled into:
- PDF presentations
- HTML web pages
- PowerPoint slides
- Print materials
- Educational videos

See `.project/agents/image-generation/tools/` for compilation scripts.

---

## Educational Use Cases

### Medical Education
- **Medical School**: Introduction to vascular surgery
- **Residency Training**: Surgical decision-making scenarios
- **Grand Rounds**: Case presentations
- **Board Prep**: Stroke prevention concepts

### Patient Education
- **Pre-Operative**: Explaining carotid endarterectomy
- **Risk Factor Education**: Stroke prevention strategies
- **Informed Consent**: Visual aid for procedure understanding
- **Support Groups**: Shared experience narratives

### Public Health
- **Stroke Awareness Campaigns**: "Know the signs" education
- **Screening Programs**: AAA and carotid screening importance
- **Risk Factor Modification**: Smoking cessation, diabetes control
- **Health Literacy**: Accessible medical information

---

## Medical Accuracy

### Evidence-Based References
- **NASCET Trial**: North American Symptomatic Carotid Endarterectomy Trial
  - >70% stenosis with symptoms = surgery indicated
  - Validates surgical intervention for stroke prevention

- **Duplex Ultrasound Criteria**: Velocity thresholds for stenosis grading
- **TIA Guidelines**: Urgent evaluation and intervention protocols
- **Perioperative Management**: Regional vs general anesthesia considerations

### Clinical Consultation
Content reviewed for medical accuracy. Not a substitute for professional medical advice.

---

## Accessibility

### Alt Text (Recommended)
When using these images online or in documents, add descriptive alt text:

```html
<img src="image_001.png" alt="Cartoon medical team rushing in hospital corridor at night responding to emergency TIA case. Camila answers phone while Camilo and Diego gather clipboards. Dora-style illustration with thick black outlines and bright colors.">
```

### Screen Reader Compatibility
- Use semantic HTML when embedding images
- Provide text transcripts of dialogue
- Include captions for key medical terms
- Link to glossary for technical terminology

---

## Copyright and Usage

### Educational Use
These images are created for educational purposes and may be used in:
- Academic presentations
- Medical training materials
- Non-commercial patient education
- Research and scholarship

### Attribution
When using these images, please credit:
```
Carotid Artery Stenosis Educational Comic
WorldSMEGraphs Project
Generated with GPT Image 1.5
Dora the Explorer style inspiration (Nickelodeon)
```

### Restrictions
- Do not use for commercial products without permission
- Do not claim ownership of the Dora the Explorer style
- Maintain educational integrity of content
- Respect patient privacy in any derivative works

---

## Contact and Feedback

For questions, corrections, or suggestions:
- **Project**: WorldSMEGraphs
- **Repository**: github.com/MSDNAndi/WorldSMEGraphs
- **Issues**: Use GitHub issue tracker for bug reports or feature requests

---

## Version History

- **v1.0** (2026-01-08): Initial 32-panel story with images generated
- **Workflow**: Validated with PR #40 workflow compliance tools
- **Quality**: 100/100 prompt quality score (all 32 panels)

---

## Related Stories

- **Acute Limb Ischemia** - Race Against Time (8 panels)
- **Diabetic Foot Bypass** - Saving the Limb (8 panels)
- **Varicose Veins** - When Cosmetic Meets Medical (8 panels)
- **Abdominal Aortic Aneurysm** - The Silent Threat (completed)

All stories feature the same medical education team for continuity.

---

**Last Updated**: 2026-01-08  
**Status**: ✅ Complete and validated  
**Next Steps**: Create PDF compilation, add HTML viewer, develop assessment questions
