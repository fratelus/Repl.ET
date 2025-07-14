#!/bin/bash

# 🔗 Local Link Checker Script
# Run this before committing to catch broken links early

set -e

echo "🔗 Checking documentation links..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check if a file exists
check_file_exists() {
    local file="$1"
    if [[ ! -f "$file" ]]; then
        echo -e "${RED}❌ Missing file: $file${NC}"
        return 1
    fi
    return 0
}

# Function to check internal references
check_internal_refs() {
    echo "🔍 Checking internal file references..."
    
    local errors=0
    
    # Check docs references
    if grep -r "docs/repl_et_checklist.md" . --include="*.md" >/dev/null 2>&1; then
        if ! check_file_exists "docs/repl_et_checklist.md"; then
            ((errors++))
        fi
    fi
    
    # Check outputs references
    if grep -r "outputs/reproducibility_spider_analysis.png" . --include="*.md" >/dev/null 2>&1; then
        if ! check_file_exists "outputs/reproducibility_spider_analysis.png"; then
            echo -e "${YELLOW}⚠️  Spider analysis PNG missing. Generate with:${NC}"
            echo "   python3 tools/generate_enhanced_spider_report.py"
            ((errors++))
        fi
    fi
    
    # Check CONTRIBUTING.md references
    if grep -r "CONTRIBUTING.md" . --include="*.md" >/dev/null 2>&1; then
        if ! check_file_exists "CONTRIBUTING.md"; then
            ((errors++))
        fi
    fi
    
    return $errors
}

# Function to check for common problematic patterns
check_problematic_patterns() {
    echo "🔍 Checking for problematic link patterns..."
    
    local errors=0
    
    # Check for placeholder DOIs (excluding documentation examples)
    if grep -r "zenodo.placeholder\|doi.placeholder" . --include="*.md" --exclude="*LINK_CHECKING.md" >/dev/null 2>&1; then
        echo -e "${RED}❌ Found placeholder DOI references${NC}"
        grep -rn "zenodo.placeholder\|doi.placeholder" . --include="*.md" --exclude="*LINK_CHECKING.md"
        ((errors++))
    fi
    
    # Check for non-existent GitHub features (like discussions if not enabled)
    if grep -r "/discussions" . --include="*.md" >/dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Found GitHub Discussions references. Ensure discussions are enabled.${NC}"
        grep -rn "/discussions" . --include="*.md"
    fi
    
    # Check for localhost or development URLs
    if grep -r "localhost\|127.0.0.1\|0.0.0.0" . --include="*.md" >/dev/null 2>&1; then
        echo -e "${RED}❌ Found development URLs in documentation${NC}"
        grep -rn "localhost\|127.0.0.1\|0.0.0.0" . --include="*.md"
        ((errors++))
    fi
    
    return $errors
}

# Main execution
main() {
    echo "🚀 Starting link check..."
    
    local total_errors=0
    
    # Check internal references
    if ! check_internal_refs; then
        ((total_errors+=$?))
    fi
    
    # Check problematic patterns
    if ! check_problematic_patterns; then
        ((total_errors+=$?))
    fi
    
    # Summary
    if [[ $total_errors -eq 0 ]]; then
        echo -e "${GREEN}✅ All link checks passed!${NC}"
        exit 0
    else
        echo -e "${RED}❌ Found $total_errors issue(s). Please fix before committing.${NC}"
        exit 1
    fi
}

# Run if called directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi 