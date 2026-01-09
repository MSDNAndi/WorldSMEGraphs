#!/bin/bash
# Generate missing panels 19-40 sequentially (one at a time)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/individual-prompts"
OUTPUT_DIR="$SCRIPT_DIR/panels-gpt"
TOOL_PATH="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools/gpt_image_generator.py"

echo "🎨 Generating missing panels 19-40 sequentially"
echo ""

# Function to generate a single panel
generate_panel() {
    local panel_num=$1
    
    echo "📌 Panel $panel_num:"
    
    # Check if panel already exists
    if ls "$OUTPUT_DIR"/image_${panel_num}_*.png >/dev/null 2>&1; then
        echo "  ✓ Already exists, skipping"
        return 0
    fi
    
    # Read prompt content (one file = one prompt)
    local prompt_content=$(cat "$PROMPTS_DIR/panel_${panel_num}.txt")
    
    # Generate using --prompt flag with proper output naming
    # FIXED: Use --output for filename prefix, --output-dir for directory
    if timeout 90 python "$TOOL_PATH" \
        --prompt "$prompt_content" \
        --output "image_${panel_num}" \
        --output-dir "$OUTPUT_DIR" \
        --aspect landscape \
        --quality high 2>&1 | tee /tmp/panel_${panel_num}_output.log | grep -q "✓ Saved"; then
        echo "  ✅ Generated successfully!"
        return 0
    else
        echo "  ❌ Generation failed"
        return 1
    fi
}

# Generate panels 19-40
failed_panels=()
success_count=0

for i in $(seq -f "%03g" 19 40); do
    if generate_panel "$i"; then
        success_count=$((success_count + 1))
    else
        failed_panels+=("$i")
    fi
    
    # Brief pause between panels to avoid rate limiting
    sleep 3
done

echo ""
echo "════════════════════════════════════════"
echo "Generation Complete"
echo "════════════════════════════════════════"
echo "✅ Successfully generated: $success_count/22 panels"

# Count total panels
total_panels=$(ls "$OUTPUT_DIR"/image_*.png 2>/dev/null | sed 's/.*image_\([0-9]*\)_.*/\1/' | sort -u | wc -l)
echo "✅ Total unique panels now: $total_panels/40"

if [ ${#failed_panels[@]} -gt 0 ]; then
    echo "❌ Failed panels: ${failed_panels[*]}"
    exit 1
else
    echo "🎉 All remaining panels generated successfully!"
    exit 0
fi
