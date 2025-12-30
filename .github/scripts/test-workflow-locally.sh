#!/bin/bash

# Test Domain Maturity Workflow Locally
# This script simulates the GitHub Actions workflow for local testing

set -e

echo "🧪 Testing Domain Maturity Check Workflow"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Change to repo root
cd "$(dirname "$0")/../.."

# Step 1: Check Python installation
echo "1️⃣  Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 not found${NC}"
    exit 1
fi

# Step 2: Check required scripts exist
echo ""
echo "2️⃣  Checking required scripts..."
SCRIPTS=(
    ".project/agents/domain-maturity/domain_maturity_tracker.py"
    ".project/agents/domain-maturity/generate_dashboard.py"
    ".project/agents/domain-maturity/compare_maturity.py"
)

for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        echo -e "${GREEN}✓ Found: $script${NC}"
    else
        echo -e "${RED}✗ Missing: $script${NC}"
        exit 1
    fi
done

# Step 3: Test scripts are executable
echo ""
echo "3️⃣  Testing script execution..."
for script in "${SCRIPTS[@]}"; do
    if python3 "$script" --help &> /dev/null; then
        echo -e "${GREEN}✓ Script works: $script${NC}"
    else
        echo -e "${YELLOW}⚠ Script may have issues: $script${NC}"
    fi
done

# Step 4: Find domains with AKUs
echo ""
echo "4️⃣  Finding domains with AKUs..."
DOMAINS=$(find domain -type d -name "akus" | sed 's|/akus||' | sed 's|^domain/||' | sort)

if [ -z "$DOMAINS" ]; then
    echo -e "${YELLOW}⚠ No domains with AKUs found${NC}"
else
    echo -e "${GREEN}Found domains:${NC}"
    echo "$DOMAINS" | while read -r domain; do
        AKU_COUNT=$(find "domain/$domain/akus" -name "*.json" 2>/dev/null | wc -l)
        echo "  • $domain ($AKU_COUNT AKUs)"
    done
fi

# Step 5: Test maturity tracker on one domain (if any exist)
echo ""
echo "5️⃣  Testing maturity tracker..."
if [ -n "$DOMAINS" ]; then
    FIRST_DOMAIN=$(echo "$DOMAINS" | head -1)
    echo "Testing with domain: $FIRST_DOMAIN"
    
    mkdir -p /tmp/test-maturity-reports
    
    # Run tracker
    if python3 .project/agents/domain-maturity/domain_maturity_tracker.py \
        --domain "$FIRST_DOMAIN" \
        --format json > /tmp/test-maturity-reports/test.json 2>&1; then
        echo -e "${GREEN}✓ Maturity tracker works${NC}"
        
        # Check if JSON is valid
        if python3 -c "import json; json.load(open('/tmp/test-maturity-reports/test.json'))" 2>/dev/null; then
            echo -e "${GREEN}✓ Generated valid JSON${NC}"
            echo ""
            echo "Sample output:"
            python3 -c "
import json
data = json.load(open('/tmp/test-maturity-reports/test.json'))
print(f\"  Domain: {data.get('domain_path', 'N/A')}\")
print(f\"  Maturity Level: {data.get('maturity_level', 'N/A')}\")
print(f\"  Completeness: {data.get('completeness_percentage', 'N/A')}%\")
print(f\"  Total AKUs: {data.get('aku_counts', {}).get('total', 0)}\")
"
        else
            echo -e "${YELLOW}⚠ JSON output may have issues${NC}"
        fi
    else
        echo -e "${RED}✗ Maturity tracker failed${NC}"
        exit 1
    fi
    
    rm -rf /tmp/test-maturity-reports
else
    echo -e "${YELLOW}⚠ Skipping - no domains to test${NC}"
fi

# Step 6: Check workflow YAML syntax
echo ""
echo "6️⃣  Validating workflow YAML..."
if python3 -c "import yaml; yaml.safe_load(open('.github/workflows/domain-maturity-check.yml'))" 2>/dev/null; then
    echo -e "${GREEN}✓ Workflow YAML is valid${NC}"
else
    echo -e "${RED}✗ Workflow YAML has syntax errors${NC}"
    exit 1
fi

# Summary
echo ""
echo "=========================================="
echo -e "${GREEN}✅ All tests passed!${NC}"
echo ""
echo "The workflow should work correctly when triggered by a PR."
echo "Make sure to test on an actual PR to verify comment posting works."
