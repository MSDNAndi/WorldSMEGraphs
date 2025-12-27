#!/bin/bash
# Project Structure Validator
# Validates that the actual file structure matches documented structure
# 
# Usage: bash .github/scripts/validate-structure.sh

set -e

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

echo "=================================="
echo "Project Structure Validation"
echo "=================================="
echo ""

PASS_COUNT=0
FAIL_COUNT=0

# Function to check if directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo "✅ Directory exists: $1"
        PASS_COUNT=$((PASS_COUNT + 1))
        return 0
    else
        echo "❌ Directory missing: $1"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        return 1
    fi
}

# Function to check if file exists
check_file() {
    if [ -f "$1" ]; then
        echo "✅ File exists: $1"
        PASS_COUNT=$((PASS_COUNT + 1))
        return 0
    else
        echo "❌ File missing: $1"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        return 1
    fi
}

echo "=== Core Directories ==="
check_dir ".github"
check_dir ".github/agents"
check_dir ".github/copilot"
check_dir ".github/workflows"
check_dir ".project"
check_dir "docs"
check_dir "domain"
echo ""

echo "=== Essential Files ==="
check_file ".github/copilot-instructions.md"
check_file ".gitignore"
check_file "README.md"
check_file "docs/CONTRIBUTING.md"
check_file ".project/structure.md"
check_file ".project/roadmap.md"
check_file ".project/issues.md"
check_file ".project/improvements.md"
echo ""

echo "=== Validation Scripts ==="
check_file ".github/copilot/agents/check-agent-lengths.sh"
check_file ".project/agents/quality-assurance/tools/validate_aku.py"
check_file ".github/scripts/validate-structure.sh"
echo ""

echo "=== Agent Files ==="
AGENT_COUNT=$(find .github/agents -name "*.agent.md" -type f | wc -l)
if [ "$AGENT_COUNT" -gt 0 ]; then
    echo "✅ Found $AGENT_COUNT agent files"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    echo "❌ No agent files found"
    FAIL_COUNT=$((FAIL_COUNT + 1))
fi
echo ""

echo "=== Domain Structure ==="
if [ -d "domain" ]; then
    DOMAIN_COUNT=$(find domain -mindepth 1 -maxdepth 2 -type d | wc -l)
    if [ "$DOMAIN_COUNT" -gt 0 ]; then
        echo "✅ Found $DOMAIN_COUNT domain directories"
        PASS_COUNT=$((PASS_COUNT + 1))
    else
        echo "⚠️  No domain subdirectories found (expected for new project)"
    fi
fi
echo ""

echo "=================================="
echo "Summary:"
echo "  Passed: $PASS_COUNT"
echo "  Failed: $FAIL_COUNT"
echo "=================================="

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo ""
    echo "❌ VALIDATION FAILED"
    echo "   $FAIL_COUNT check(s) failed"
    exit 1
else
    echo ""
    echo "✅ VALIDATION PASSED"
    echo "   All structure checks passed"
    exit 0
fi
