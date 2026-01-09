#!/bin/bash
# Agent Format Validator
# Verifies all agent .agent.md files have valid YAML frontmatter
# 
# Checks:
# 1. File starts with ---
# 2. Has closing --- for frontmatter
# 3. Contains 'name:' field
# 4. Contains 'description:' field
# 5. Contains 'tools:' field
#
# Usage: bash .github/scripts/validate-agent-format.sh [--verbose]

set -e

SCRIPT_DIR="$(dirname "$0")"
AGENTS_DIR="$(cd "$SCRIPT_DIR/../agents" && pwd)"
VERBOSE="${1:-}"

ERROR_COUNT=0
WARNING_COUNT=0
PASS_COUNT=0
TOTAL_COUNT=0

echo "=================================="
echo "Agent Format Validation"
echo "Checking: ${AGENTS_DIR}"
echo "=================================="
echo ""

check_agent() {
    local file="$1"
    local filename=$(basename "$file")
    local errors=""
    local warnings=""
    local passed=true
    
    # Check 1: File starts with ---
    if ! head -1 "$file" | grep -q "^---$"; then
        errors="${errors}  ❌ Missing frontmatter start (---)\n"
        passed=false
    fi
    
    # Check 2: Has closing ---
    local frontmatter_end=$(awk '/^---$/{count++; if(count==2) {print NR; exit}}' "$file")
    if [ -z "$frontmatter_end" ] || [ "$frontmatter_end" -lt 3 ]; then
        errors="${errors}  ❌ Missing frontmatter end or malformed frontmatter\n"
        passed=false
    fi
    
    # Check 3: Contains name: field (within frontmatter)
    local has_name=$(awk 'NR==1,/^---$/' "$file" | awk '/^---$/,/^---$/' | grep -c "^name:" || true)
    if [ "$has_name" -eq 0 ]; then
        # Fallback check - look for name: in first 10 lines
        has_name=$(head -10 "$file" | grep -c "^name:" || true)
    fi
    if [ "$has_name" -eq 0 ]; then
        errors="${errors}  ❌ Missing 'name:' field in frontmatter\n"
        passed=false
    fi
    
    # Check 4: Contains description: field
    local has_description=$(head -15 "$file" | grep -c "^description:" || true)
    if [ "$has_description" -eq 0 ]; then
        errors="${errors}  ❌ Missing 'description:' field in frontmatter\n"
        passed=false
    fi
    
    # Check 5: Contains tools: field
    local has_tools=$(head -15 "$file" | grep -c "^tools:" || true)
    if [ "$has_tools" -eq 0 ]; then
        warnings="${warnings}  ⚠️ Missing 'tools:' field in frontmatter (optional)\n"
    fi
    
    # Check 6: Line count warning
    local line_count=$(wc -l < "$file")
    if [ "$line_count" -lt 180 ]; then
        warnings="${warnings}  ⚠️ Only $line_count lines (recommend 180+)\n"
    fi
    
    # Output results
    if [ "$passed" = true ]; then
        if [ -n "$VERBOSE" ] || [ -n "$warnings" ]; then
            echo "✅ $filename"
            if [ -n "$warnings" ] && [ -n "$VERBOSE" ]; then
                printf "$warnings"
            fi
        else
            echo "✅ $filename"
        fi
        PASS_COUNT=$((PASS_COUNT + 1))
    else
        echo "❌ $filename"
        printf "$errors"
        if [ -n "$warnings" ]; then
            printf "$warnings"
        fi
        ERROR_COUNT=$((ERROR_COUNT + 1))
    fi
    
    # Count warnings
    if [ -n "$warnings" ]; then
        local warn_count=$(echo -e "$warnings" | grep -c "⚠️" || true)
        WARNING_COUNT=$((WARNING_COUNT + warn_count))
    fi
}

# Check all .agent.md files
for agent_file in "$AGENTS_DIR"/*.agent.md; do
    if [ -f "$agent_file" ]; then
        TOTAL_COUNT=$((TOTAL_COUNT + 1))
        check_agent "$agent_file"
    fi
done

echo ""
echo "=================================="
echo "Summary:"
echo "  Total Agents: $TOTAL_COUNT"
echo "  Passed: $PASS_COUNT"
echo "  Errors: $ERROR_COUNT"
echo "  Warnings: $WARNING_COUNT"
echo "=================================="

if [ "$ERROR_COUNT" -gt 0 ]; then
    echo ""
    echo "❌ VALIDATION FAILED"
    echo "   $ERROR_COUNT agent(s) have format errors"
    echo ""
    echo "Common fixes:"
    echo "  1. Add YAML frontmatter at file start:"
    echo "     ---"
    echo "     name: agent-name"
    echo "     description: Agent description"
    echo "     tools:"
    echo "     - '*'"
    echo "     infer: true"
    echo "     ---"
    echo ""
    exit 1
else
    echo ""
    echo "✅ VALIDATION PASSED"
    echo "   All agents have valid frontmatter format"
    exit 0
fi
