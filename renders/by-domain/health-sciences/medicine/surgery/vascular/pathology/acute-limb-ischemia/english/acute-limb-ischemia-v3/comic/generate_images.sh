#!/bin/bash
# Acute Limb Ischemia V3 - Image Generation Script
# Uses single-line prompts for reliable generation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_FILE="$SCRIPT_DIR/prompts-single-line.txt"
OUTPUT_DIR="$SCRIPT_DIR/panels-gpt"
TOOL_PATH="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools/gpt_image_generator.py"

echo "🎨 Acute Limb Ischemia V3 - Generating 25 panels"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Create output directory if needed
mkdir -p "$OUTPUT_DIR"

# Check if prompts file exists
if [ ! -f "$PROMPTS_FILE" ]; then
    echo "❌ Error: Prompts file not found: $PROMPTS_FILE"
    exit 1
fi

# Count total prompts
TOTAL=$(wc -l < "$PROMPTS_FILE")
echo "📋 Total prompts: $TOTAL"
echo ""

# Generate images in parallel batches
PARALLEL_COUNT=5
PANEL_NUM=1

while IFS= read -r prompt; do
    # Skip empty lines
    [ -z "$prompt" ] && continue
    
    # Format panel number with leading zeros
    PANEL_NUM_STR=$(printf "%02d" $PANEL_NUM)
    
    # Check if panel already exists
    if ls "$OUTPUT_DIR"/image_${PANEL_NUM_STR}_*.png >/dev/null 2>&1; then
        echo "✓ Panel $PANEL_NUM_STR already exists, skipping"
        ((PANEL_NUM++))
        continue
    fi
    
    echo "📌 Generating Panel $PANEL_NUM_STR..."
    
    # Generate image with explicit output naming
    python3 "$TOOL_PATH" \
        --prompt "$prompt" \
        --output "image_${PANEL_NUM_STR}" \
        --output-dir "$OUTPUT_DIR" \
        --aspect landscape \
        --quality high \
        --enhance \
        --max-retries 3 \
        2>&1 | grep -E "✓|✗|Error|Warning" || true
    
    ((PANEL_NUM++))
    
    # Rate limit between images
    sleep 2
    
done < "$PROMPTS_FILE"

echo ""
echo "✅ Generation complete!"
echo "📁 Output: $OUTPUT_DIR"
ls -la "$OUTPUT_DIR"/*.png 2>/dev/null | wc -l | xargs echo "🖼️ Images generated:"
