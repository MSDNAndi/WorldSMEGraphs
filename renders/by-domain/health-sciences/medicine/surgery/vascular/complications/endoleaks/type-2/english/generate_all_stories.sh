#!/bin/bash

# Master script to generate all 5 additional vascular surgery stories
# Uses parallel image generation (8-10 concurrent requests)

set -e

COMIC_DIR="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/renders/by-domain/health-sciences/medicine/surgery/vascular/complications/endoleaks/type-2/english/comic"
GENERATOR="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools/gpt_image_generator.py"

echo "========================================="
echo "Vascular Surgery Comic Generation Pipeline"
echo "========================================="
echo "Stories to generate: 5"
echo "Panels per story: 32"
echo "Total images: 160"
echo "Parallel requests: 10"
echo "========================================="

# Story 2: Carotid Artery Stenosis
echo "[1/5] Generating Carotid Artery Stenosis story..."
STORY_DIR="../carotid-artery-stenosis/comic"
if [ -f "$STORY_DIR/gpt-prompts-all-panels.txt" ]; then
    python3 "$GENERATOR" \
        --prompt-file "$STORY_DIR/gpt-prompts-all-panels.txt" \
        --output-dir "$STORY_DIR/panels-gpt" \
        --aspect landscape \
        --quality high \
        --parallel 10 \
        --enhance
    echo "✓ Carotid story complete"
else
    echo "⚠ Skipping - prompts not ready"
fi

# Story 3: Abdominal Aortic Aneurysm  
echo "[2/5] Generating AAA story..."
STORY_DIR="../abdominal-aortic-aneurysm/comic"
if [ -f "$STORY_DIR/gpt-prompts-all-panels.txt" ]; then
    python3 "$GENERATOR" \
        --prompt-file "$STORY_DIR/gpt-prompts-all-panels.txt" \
        --output-dir "$STORY_DIR/panels-gpt" \
        --aspect landscape \
        --quality high \
        --parallel 10 \
        --enhance
    echo "✓ AAA story complete"
else
    echo "⚠ Skipping - prompts not ready"
fi

# Story 4: Acute Limb Ischemia
echo "[3/5] Generating Acute Limb Ischemia story..."
STORY_DIR="../acute-limb-ischemia/comic"
if [ -f "$STORY_DIR/gpt-prompts-all-panels.txt" ]; then
    python3 "$GENERATOR" \
        --prompt-file "$STORY_DIR/gpt-prompts-all-panels.txt" \
        --output-dir "$STORY_DIR/panels-gpt" \
        --aspect landscape \
        --quality high \
        --parallel 10 \
        --enhance
    echo "✓ ALI story complete"
else
    echo "⚠ Skipping - prompts not ready"
fi

# Story 5: Diabetic Foot Ulcer
echo "[4/5] Generating Diabetic Foot story..."
STORY_DIR="../diabetic-foot-ulcer/comic"
if [ -f "$STORY_DIR/gpt-prompts-all-panels.txt" ]; then
    python3 "$GENERATOR" \
        --prompt-file "$STORY_DIR/gpt-prompts-all-panels.txt" \
        --output-dir "$STORY_DIR/panels-gpt" \
        --aspect landscape \
        --quality high \
        --parallel 10 \
        --enhance
    echo "✓ Diabetic Foot story complete"
else
    echo "⚠ Skipping - prompts not ready"
fi

# Story 6: Varicose Veins
echo "[5/5] Generating Varicose Veins story..."
STORY_DIR="../varicose-veins/comic"
if [ -f "$STORY_DIR/gpt-prompts-all-panels.txt" ]; then
    python3 "$GENERATOR" \
        --prompt-file "$STORY_DIR/gpt-prompts-all-panels.txt" \
        --output-dir "$STORY_DIR/panels-gpt" \
        --aspect landscape \
        --quality high \
        --parallel 10 \
        --enhance
    echo "✓ Varicose Veins story complete"
else
    echo "⚠ Skipping - prompts not ready"
fi

echo "========================================="
echo "✓ All stories generated!"
echo "========================================="
