#!/bin/bash
# create_render.sh - Helper script to create new renders with proper structure
#
# Usage:
#   ./create_render.sh [domain-path] [language] [audience]
#
# Example:
#   ./create_render.sh natural-sciences/physics/quantum-mechanics/planck-units english undergraduate

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check arguments
if [ $# -ne 3 ]; then
    echo -e "${RED}Error: Wrong number of arguments${NC}"
    echo ""
    echo "Usage: $0 [domain-path] [language] [audience]"
    echo ""
    echo "Example:"
    echo "  $0 natural-sciences/physics/quantum-mechanics/planck-units english undergraduate"
    echo ""
    echo "Available audiences: preschool, elementary-school, middle-school, high-school,"
    echo "                     undergraduate, graduate, adult-limited-reading, professional"
    exit 1
fi

DOMAIN_PATH=$1
LANGUAGE=$2
AUDIENCE=$3

# Get repo root (script is in renders/_metadata/tools/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
RENDERS_ROOT="$REPO_ROOT/renders"

# Validate domain path exists
DOMAIN_DIR="$REPO_ROOT/domain/$DOMAIN_PATH"
if [ ! -d "$DOMAIN_DIR" ]; then
    echo -e "${RED}Error: Domain directory not found: $DOMAIN_DIR${NC}"
    echo ""
    echo "Available domains:"
    find "$REPO_ROOT/domain" -mindepth 1 -maxdepth 5 -type d | grep -v "^$REPO_ROOT/domain/_" | head -20
    exit 1
fi

# Create target directory
TARGET_DIR="$RENDERS_ROOT/by-domain/$DOMAIN_PATH/$LANGUAGE"
mkdir -p "$TARGET_DIR"

echo -e "${GREEN}✓${NC} Created directory: $TARGET_DIR"

# Create render file
RENDER_FILE="$TARGET_DIR/$AUDIENCE.md"

if [ -f "$RENDER_FILE" ]; then
    echo -e "${YELLOW}⚠${NC}  File already exists: $RENDER_FILE"
    echo "    Skipping file creation"
else
    # Generate template
    DOMAIN_NAME=$(basename "$DOMAIN_PATH")
    TODAY=$(date -u +"%Y-%m-%d")
    
    cat > "$RENDER_FILE" << TEMPLATE
# ${DOMAIN_NAME^} - ${AUDIENCE^} Level

> **For**: ${AUDIENCE^}  
> **Language**: ${LANGUAGE^}  
> **Last Updated**: $TODAY

## Overview

[Introduction paragraph here]

## Key Concepts

### Concept 1

[Explanation appropriate for ${AUDIENCE} level]

### Concept 2

[Explanation appropriate for ${AUDIENCE} level]

## Examples

[Concrete examples appropriate for this audience]

## Summary

[Brief summary of key takeaways]

---

**Source**: Based on AKUs from domain/$DOMAIN_PATH/  
**Audience**: ${AUDIENCE}  
**Reading Level**: [TBD - run readability check]  
**Last Updated**: $TODAY
TEMPLATE
    
    echo -e "${GREEN}✓${NC} Created render file: $RENDER_FILE"
fi

# Regenerate indexes
echo ""
echo "Regenerating render index..."
cd "$RENDERS_ROOT/_metadata/tools"
python3 generate_render_index.py

echo ""
echo "Regenerating AKU usage matrix..."
python3 generate_aku_usage_matrix.py

# Print next steps
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Render Created Successfully!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo ""
echo "File: $RENDER_FILE"
echo ""
echo "Next steps:"
echo "  1. Edit the render file with content"
echo "  2. Add appropriate examples and explanations"
echo "  3. Check readability:"
echo "     python3 renders/_metadata/tools/render_quality_linter.py $RENDER_FILE"
echo "  4. Commit:"
echo "     git add renders/"
echo "     git commit -m \"Add $AUDIENCE render for $DOMAIN_NAME\""
echo ""
