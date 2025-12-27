#!/bin/bash
# Agent Length Checker - Acceptance Criteria
# Verifies all agent YAML files meet the 180-line minimum requirement

set -e

AGENTS_DIR="$(dirname "$0")"
MIN_LINES=180
FAIL_COUNT=0
PASS_COUNT=0
TOTAL_COUNT=0

echo "=================================="
echo "Agent Length Verification"
echo "Minimum Required: ${MIN_LINES} lines"
echo "=================================="
echo ""

# Check all .yml files except README
for agent_file in "$AGENTS_DIR"/*.yml; do
    if [ -f "$agent_file" ]; then
        TOTAL_COUNT=$((TOTAL_COUNT + 1))
        filename=$(basename "$agent_file")
        line_count=$(wc -l < "$agent_file")
        
        if [ "$line_count" -ge "$MIN_LINES" ]; then
            echo "✅ PASS: $filename ($line_count lines)"
            PASS_COUNT=$((PASS_COUNT + 1))
        else
            echo "❌ FAIL: $filename ($line_count lines) - BELOW MINIMUM"
            FAIL_COUNT=$((FAIL_COUNT + 1))
        fi
    fi
done

echo ""
echo "=================================="
echo "Summary:"
echo "  Total Agents: $TOTAL_COUNT"
echo "  Passed: $PASS_COUNT"
echo "  Failed: $FAIL_COUNT"
echo "=================================="

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo ""
    echo "❌ ACCEPTANCE CRITERIA NOT MET"
    echo "   $FAIL_COUNT agent(s) below ${MIN_LINES}-line minimum"
    exit 1
else
    echo ""
    echo "✅ ACCEPTANCE CRITERIA MET"
    echo "   All agents meet ${MIN_LINES}-line minimum"
    exit 0
fi
