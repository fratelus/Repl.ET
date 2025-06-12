#!/usr/bin/env python3
"""
Repl.ET Test Runner

This script runs the complete test suite for the Repl.ET framework
and generates coverage reports.

Usage:
    python tests/run_tests.py [options]

Options:
    --unit          Run only unit tests
    --integration   Run only integration tests
    --slow          Include slow tests
    --coverage      Generate coverage report
    --html          Generate HTML coverage report
"""

import sys
import subprocess
import argparse
import os

def run_tests(test_type=None, coverage=False, html_report=False, verbose=True):
    """Run tests with specified options."""
    
    cmd = ["python", "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=.", "--cov-report=term-missing"])
        if html_report:
            cmd.append("--cov-report=html")
    
    if test_type:
        cmd.extend(["-m", test_type])
    
    cmd.append("tests/")
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=".")
    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Run Repl.ET tests")
    parser.add_argument("--unit", action="store_true", 
                       help="Run only unit tests")
    parser.add_argument("--integration", action="store_true",
                       help="Run only integration tests") 
    parser.add_argument("--slow", action="store_true",
                       help="Include slow tests")
    parser.add_argument("--coverage", action="store_true",
                       help="Generate coverage report")
    parser.add_argument("--html", action="store_true",
                       help="Generate HTML coverage report")
    parser.add_argument("--quiet", action="store_true",
                       help="Reduce output verbosity")
    
    args = parser.parse_args()
    
    # Determine test type
    test_type = None
    if args.unit:
        test_type = "unit"
    elif args.integration:
        test_type = "integration"
    elif args.slow:
        test_type = "slow"
    
    # Check if we're in the right directory
    if not os.path.exists("tests"):
        print("Error: tests/ directory not found. Run from repository root.")
        sys.exit(1)
    
    # Run tests
    exit_code = run_tests(
        test_type=test_type,
        coverage=args.coverage,
        html_report=args.html,
        verbose=not args.quiet
    )
    
    if exit_code == 0:
        print("\n✅ All tests passed!")
        if args.coverage and args.html:
            print("📊 Coverage report generated: htmlcov/index.html")
    else:
        print("\n❌ Some tests failed!")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main() 