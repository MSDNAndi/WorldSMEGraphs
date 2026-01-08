#!/bin/bash
# Generate remaining panels 19-40 for carotid V2 story

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/individual-prompts"
OUTPUT_DIR="$SCRIPT_DIR/panels-gpt"
TOOL_PATH="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools/gpt_image_generator.py"

echo "🎨 Generating remaining panels 19-40 for Carotid V2 story"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Function to generate a single panel with retry
generate_panel() {
    local panel_num=$1
    local max_retries=3
    local retry_count=0
    
    echo "📌 Panel $panel_num:"
    
    # Check if panel already exists
    if ls "$OUTPUT_DIR"/image_${panel_num}_*.png >/dev/null 2>&1; then
        echo "  ✓ Already exists, skipping"
        return 0
    fi
    
    while [ $retry_count -lt $max_retries ]; do
        echo "  🔄 Attempt $((retry_count + 1))/$max_retries..."
        
        if python "$TOOL_PATH" \
            --prompt-file "$PROMPTS_DIR/panel_${panel_num}.txt" \
            --output "$OUTPUT_DIR" \
            --aspect landscape \
            --quality high \
            2>&1 | grep -q "✓ Saved:"; then
            echo "  ✅ Success!"
            return 0
        fi
        
        retry_count=$((retry_count + 1))
        if [ $retry_count -lt $max_retries ]; then
            echo "  ⚠️  Failed, retrying in 5 seconds..."
            sleep 5
        fi
    done
    
    echo "  ❌ Failed after $max_retries attempts"
    return 1
}

# Generate panels 19-40
failed_panels=()
for i in $(seq -f "%03g" 19 40); do
    if ! generate_panel "$i"; then
        failed_panels+=("$i")
    fi
    sleep 2  # Brief pause between panels
done

echo ""
echo "════════════════════════════════════════"
echo "Generation Complete"
echo "════════════════════════════════════════"

# Count total panels
total_panels=$(ls "$OUTPUT_DIR"/image_*.png 2>/dev/null | sed 's/.*image_\([0-9]*\)_.*/\1/' | sort -u | wc -l)
echo "✅ Total unique panels: $total_panels/40"

if [ ${#failed_panels[@]} -gt 0 ]; then
    echo "❌ Failed panels: ${failed_panels[*]}"
    exit 1
else
    echo "🎉 All panels generated successfully!"
    exit 0
fi
