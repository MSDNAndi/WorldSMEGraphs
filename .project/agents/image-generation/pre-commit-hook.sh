#!/bin/bash
# Git Pre-Commit Hook - Workflow Order Validation
# 
# This hook enforces the correct workflow order for content generation:
# Phase 1-2: Storyboard → Phase 3: Prompts → Phase 4: Images → Phase 5: Documents
#
# Installation:
#   cp .project/agents/image-generation/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# To bypass (NOT RECOMMENDED):
#   git commit --no-verify
#
# Version: 1.0.0
# Created: 2026-01-08

set -e

echo "🔍 Checking workflow order..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track if we found any violations
VIOLATIONS=0

# Check if any final documents (PDF, PPTX, HTML) are being committed
FINAL_DOCS=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(pptx|pdf|html)$' || true)

if [ -n "$FINAL_DOCS" ]; then
    echo "📄 Found final document(s) being committed:"
    echo "$FINAL_DOCS" | sed 's/^/   - /'
    
    # For each final document, check if corresponding images directory exists
    while IFS= read -r doc; do
        if [ -z "$doc" ]; then
            continue
        fi
        
        # Get the directory of the document
        doc_dir=$(dirname "$doc")
        
        # Check for images/ directory
        images_dirs=(
            "$doc_dir/images"
            "$doc_dir/panels-gpt"
            "$doc_dir/panels-gpt-v2"
        )
        
        found_images=false
        for images_dir in "${images_dirs[@]}"; do
            if [ -d "$images_dir" ]; then
                # Check if directory has PNG files
                image_count=$(find "$images_dir" -maxdepth 1 -name "*.png" 2>/dev/null | wc -l)
                if [ "$image_count" -gt 0 ]; then
                    echo -e "   ${GREEN}✓${NC} $doc: Found $image_count images in $(basename "$images_dir")"
                    found_images=true
                    break
                fi
            fi
        done
        
        if [ "$found_images" = false ]; then
            echo -e "   ${RED}✗${NC} $doc: No images directory found"
            echo ""
            echo -e "${RED}❌ WORKFLOW VIOLATION${NC}"
            echo "   Document: $doc"
            echo "   Problem: Final document being committed without corresponding images"
            echo ""
            echo "   You MUST generate images (Phase 4) BEFORE creating documents (Phase 5)."
            echo ""
            echo "   Checked for images in:"
            for images_dir in "${images_dirs[@]}"; do
                echo "     - $images_dir"
            done
            echo ""
            echo "   See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
            echo ""
            VIOLATIONS=$((VIOLATIONS + 1))
        fi
    done <<< "$FINAL_DOCS"
fi

# Check if prompts are being committed and validate them
PROMPT_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E 'prompt.*\.txt$|.*prompts.*\.txt$' || true)

if [ -n "$PROMPT_FILES" ]; then
    echo ""
    echo "📝 Validating prompt files..."
    
    # Check if validation script exists
    if [ -f ".project/agents/image-generation/tools/validate_prompts.py" ]; then
        while IFS= read -r prompt_file; do
            if [ -z "$prompt_file" ]; then
                continue
            fi
            
            # Check for placeholders in the prompt
            if grep -qi "PLACEHOLDER\|TODO\|TBD\|FIXME\|\[insert\|\[add\|Apply STYLE BASE" "$prompt_file" 2>/dev/null; then
                echo -e "   ${YELLOW}⚠${NC}  $prompt_file: Contains placeholders (not recommended)"
                echo "      Prompts should be complete and self-contained"
                VIOLATIONS=$((VIOLATIONS + 1))
            fi
            
            # Check prompt length
            if [ -f "$prompt_file" ]; then
                size=$(wc -c < "$prompt_file")
                if [ "$size" -lt 1000 ]; then
                    echo -e "   ${YELLOW}⚠${NC}  $prompt_file: Only $size bytes (recommend 5KB+)"
                    VIOLATIONS=$((VIOLATIONS + 1))
                else
                    echo -e "   ${GREEN}✓${NC} $prompt_file: $size bytes"
                fi
            fi
        done <<< "$PROMPT_FILES"
    fi
fi

# Final result
echo ""
if [ "$VIOLATIONS" -gt 0 ]; then
    echo -e "${RED}❌ Found $VIOLATIONS workflow violation(s)${NC}"
    echo ""
    echo "Correct workflow order:"
    echo "  1-2. Create storyboard (content planning)"
    echo "  3. Write complete prompts (no placeholders)"
    echo "  4. Generate images using prompts"
    echo "  5. Create final documents referencing images"
    echo ""
    echo "To fix:"
    echo "  - Generate images before committing final documents"
    echo "  - Remove placeholders from prompts"
    echo "  - Ensure prompts are substantial (5KB+ recommended)"
    echo ""
    echo "See: .project/agents/image-generation/WORKFLOW-ENFORCEMENT.md"
    echo ""
    echo "To bypass this check (NOT RECOMMENDED):"
    echo "  git commit --no-verify"
    echo ""
    exit 1
else
    echo -e "${GREEN}✅ Workflow order check passed${NC}"
    exit 0
fi
