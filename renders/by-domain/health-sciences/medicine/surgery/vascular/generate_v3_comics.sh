#!/bin/bash
# V3 Comics - Parallel Image Generation Script
# Generates images for all 4 v3 comics

set -e

BASE_DIR="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/renders/by-domain/health-sciences/medicine/surgery/vascular"
TOOL_PATH="/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/agents/image-generation/tools/gpt_image_generator.py"

# Comic directories
declare -a COMICS=(
    "pathology/acute-limb-ischemia/english/acute-limb-ischemia-v3"
    "pathology/varicose-veins/english/varicose-veins-v3"
    "pathology/carotid-artery-stenosis/english/carotid-artery-stenosis-v3"
    "procedures/bypass/english/diabetic-foot-bypass-v3"
)

echo "🎨 V3 Comics - Image Generation"
echo "================================"
echo ""

# Function to generate images for a comic
generate_comic() {
    local comic_path="$1"
    local comic_name=$(basename "$comic_path")
    local full_path="$BASE_DIR/$comic_path/comic"
    local prompts_file="$full_path/prompts-single-line.txt"
    local output_dir="$full_path/panels-gpt"
    
    echo "📚 Processing: $comic_name"
    
    # Check if prompts file exists
    if [ ! -f "$prompts_file" ]; then
        echo "  ⚠️  No prompts file found, skipping"
        return
    fi
    
    mkdir -p "$output_dir"
    
    local panel_num=1
    while IFS= read -r prompt; do
        [ -z "$prompt" ] && continue
        
        local panel_str=$(printf "%02d" $panel_num)
        
        # Skip if exists
        if ls "$output_dir"/image_${panel_str}_*.png >/dev/null 2>&1; then
            echo "  ✓ Panel $panel_str exists"
            ((panel_num++))
            continue
        fi
        
        echo "  🔄 Panel $panel_str generating..."
        
        python3 "$TOOL_PATH" \
            --prompt "$prompt" \
            --output "image_${panel_str}" \
            --output-dir "$output_dir" \
            --aspect landscape \
            --quality high \
            --enhance \
            --max-retries 3 \
            2>&1 | grep -E "✓|✗" || true
        
        ((panel_num++))
        sleep 1
        
    done < "$prompts_file"
    
    echo "  ✅ $comic_name complete"
}

# Process each comic
for comic in "${COMICS[@]}"; do
    generate_comic "$comic"
    echo ""
done

echo "================================"
echo "✅ All V3 comics processed"
