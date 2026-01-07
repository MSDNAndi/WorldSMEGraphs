#!/bin/bash
# Master script to generate complete comic with all formats from storyboard
# Usage: ./generate_complete_comic.sh <story_dir>

set -e

if [ -z "$1" ]; then
    echo "Usage: ./generate_complete_comic.sh <story_dir>"
    echo "Example: ./generate_complete_comic.sh carotid-artery-stenosis"
    exit 1
fi

STORY_DIR="$1"
COMIC_DIR="${STORY_DIR}/comic"
STORYBOARD="${COMIC_DIR}/storyboard.json"

if [ ! -f "$STORYBOARD" ]; then
    echo "Error: Storyboard not found: $STORYBOARD"
    exit 1
fi

echo "=== Generating Complete Comic for ${STORY_DIR} ==="
echo

# Step 1: Generate hyper-detailed prompts
echo "Step 1: Generating hyper-detailed prompts..."
python generate_story_complete.py \
    "$STORYBOARD" \
    "${COMIC_DIR}/prompts-all-panels.txt"
echo "✓ Prompts generated"
echo

# Step 2: Generate images (parallel)
echo "Step 2: Generating images (32 panels, parallel processing)..."
python .project/agents/image-generation/tools/gpt_image_generator.py \
    --prompt-file "${COMIC_DIR}/prompts-all-panels.txt" \
    --output-dir "${COMIC_DIR}/panels-gpt" \
    --aspect landscape \
    --quality high \
    --parallel 10 \
    --enhance
echo "✓ Images generated"
echo

# Step 3: Generate markdown story
echo "Step 3: Generating markdown story..."
python generate_markdown_story.py \
    "$STORYBOARD" \
    "${COMIC_DIR}/story.md"
echo "✓ Markdown story generated"
echo

# Step 4: Generate 6-panel markdown layout
echo "Step 4: Generating 6-panel markdown layout..."
python generate_6panel_markdown.py \
    "${COMIC_DIR}/panels-gpt" \
    "$STORYBOARD" \
    "${COMIC_DIR}/story-6-panel.md"
echo "✓ 6-panel layout generated"
echo

# Step 5: Generate PDF
echo "Step 5: Generating PDF..."
python build_gpt_pdf.py \
    --input-dir "${COMIC_DIR}/panels-gpt" \
    --output "${COMIC_DIR}/comic.pdf"
echo "✓ PDF generated"
echo

# Step 6: Generate HTML
echo "Step 6: Generating HTML..."
python generate_html_comic.py \
    "$STORYBOARD" \
    "${COMIC_DIR}/panels-gpt" \
    "${COMIC_DIR}/comic.html"
echo "✓ HTML generated"
echo

# Step 7: Check file sizes and compress if needed
echo "Step 7: Checking file sizes..."
PDF_SIZE=$(stat -f%z "${COMIC_DIR}/comic.pdf" 2>/dev/null || stat -c%s "${COMIC_DIR}/comic.pdf" 2>/dev/null || echo "0")

if [ "$PDF_SIZE" -gt 52428800 ]; then
    echo "PDF over 50MB (${PDF_SIZE} bytes), compressing..."
    tar -czf "${COMIC_DIR}/comic-images.tar.gz" -C "${COMIC_DIR}" panels-gpt
    split -b 45M "${COMIC_DIR}/comic-images.tar.gz" "${COMIC_DIR}/comic-images.tar.gz.part_"
    echo "✓ Compressed and split into <45MB parts"
    echo "  To reconstruct: cat ${COMIC_DIR}/comic-images.tar.gz.part_* > ${COMIC_DIR}/comic-images.tar.gz && tar -xzf ${COMIC_DIR}/comic-images.tar.gz"
else
    echo "✓ PDF size OK (${PDF_SIZE} bytes, under 50MB limit)"
fi
echo

echo "=== Comic Generation Complete ==="
echo
echo "Output files:"
echo "  - Prompts: ${COMIC_DIR}/prompts-all-panels.txt"
echo "  - Images: ${COMIC_DIR}/panels-gpt/ (32 PNG files)"
echo "  - Markdown story: ${COMIC_DIR}/story.md"
echo "  - Markdown 6-panel: ${COMIC_DIR}/story-6-panel.md"
echo "  - PDF: ${COMIC_DIR}/comic.pdf"
echo "  - HTML: ${COMIC_DIR}/comic.html"
echo
echo "Done!"
