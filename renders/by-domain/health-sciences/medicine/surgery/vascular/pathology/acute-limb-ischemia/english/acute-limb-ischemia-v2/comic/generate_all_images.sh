#!/bin/bash
# Generate all 35 images for Acute Limb Ischemia V2 story sequentially

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TOOL_DIR="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools"
PROMPTS_DIR="$SCRIPT_DIR/individual-prompts"
OUTPUT_DIR="$SCRIPT_DIR/panels-gpt"

mkdir -p "$OUTPUT_DIR"

echo "Starting image generation for all 35 panels..."
echo "Output directory: $OUTPUT_DIR"

for i in $(seq 1 35); do
    panel_num=$(printf "%02d" $i)
    prompt_file="$PROMPTS_DIR/panel_${panel_num}.txt"
    
    if [ ! -f "$prompt_file" ]; then
        echo "ERROR: Prompt file not found: $prompt_file"
        continue
    fi
    
    echo ""
    echo "=== Generating Panel $panel_num ==="
    echo "Reading prompt from: $prompt_file"
    
    # Read prompt content
    prompt_content=$(cat "$prompt_file")
    
    # Generate image using --prompt flag with proper panel numbering
    # IMPORTANT: Use --output to ensure correct panel number in filename
    python "$TOOL_DIR/gpt_image_generator.py" \
        --prompt "$prompt_content" \
        --output "image_${panel_num}" \
        --aspect landscape \
        --quality high \
        --output-dir "$OUTPUT_DIR" \
        --timeout 120
    
    if [ $? -eq 0 ]; then
        echo "✓ Panel $panel_num generated successfully"
    else
        echo "✗ Panel $panel_num failed - will retry"
        sleep 5
        
        # Retry once
        python "$TOOL_DIR/gpt_image_generator.py" \
            --prompt "$prompt_content" \
            --output "image_${panel_num}" \
            --aspect landscape \
            --quality high \
            --output-dir "$OUTPUT_DIR" \
            --timeout 120
        
        if [ $? -eq 0 ]; then
            echo "✓ Panel $panel_num generated on retry"
        else
            echo "✗✗ Panel $panel_num failed after retry"
        fi
    fi
    
    # Small delay between requests
    sleep 3
done

echo ""
echo "Image generation complete!"
echo "Check $OUTPUT_DIR for generated images"
