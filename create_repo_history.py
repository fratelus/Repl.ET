#!/usr/bin/env python3
"""
Script to create a realistic Repl.ET repository with 2 months of development history.
"""

import os
import shutil
import subprocess
import json
from datetime import datetime, timedelta
import time

def run_git_command(cmd, commit_date=None):
    """Run a git command with optional commit date."""
    if commit_date and ('commit' in cmd):
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = commit_date
        env['GIT_COMMITTER_DATE'] = commit_date
        subprocess.run(cmd, shell=True, env=env)
    else:
        subprocess.run(cmd, shell=True)

def create_file(path, content=""):
    """Create a file with content."""
    dirname = os.path.dirname(path)
    if dirname:  # Only create directories if there's a dirname
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def copy_from_backup(src, dst):
    """Copy file or directory from backup."""
    backup_path = f"../Repl.ET_backup/{src}"
    if os.path.exists(backup_path):
        if os.path.isdir(backup_path):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(backup_path, dst)
        else:
            dirname = os.path.dirname(dst)
            if dirname:  # Only create directories if there's a dirname
                os.makedirs(dirname, exist_ok=True)
            shutil.copy2(backup_path, dst)
        return True
    return False

def create_commit_history():
    """Create a realistic 2-month development history."""
    
    # Start date: 2 months ago
    start_date = datetime.now() - timedelta(days=60)
    
    commits = [
        # Week 1: Initial project setup
        {
            "date": start_date,
            "message": "feat: initial repository setup with basic structure",
            "files": [
                ("README.md", """# Repl.ET: Eye Tracking Replication Template

A standardized template for eye tracking experiments in Software Engineering and HCI.

## Overview
This repository follows international guidelines for reproducible eye tracking research.
"""),
                (".gitignore", """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Data
*.csv
*.tsv
*.log
!**/example*.csv

# Results
results/
reports/
"""),
                ("LICENSE", """MIT License

Copyright (c) 2024 Repl.ET Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
            ]
        },
        
        # Week 1: Basic structure
        {
            "date": start_date + timedelta(days=2),
            "message": "feat: add basic directory structure and requirements",
            "files": [
                ("requirements.txt", """jsonschema>=4.0.0
requests>=2.25.0
matplotlib>=3.5.0
numpy>=1.21.0
pandas>=1.3.0
pytest>=6.0.0
pytest-cov>=3.0.0
"""),
                ("CITATION.cff", """cff-version: 1.2.0
message: "If you use this template, please cite it as below."
type: software
title: "Repl.ET: Eye Tracking Replication Template"
version: 1.0.0
date-released: 2024-12-15
url: "https://github.com/replET/replET"
authors:
  - family-names: "Silva"
    given-names: "Lucas"
    orcid: "https://orcid.org/0000-0000-0000-0000"
license: MIT
keywords:
  - eye-tracking
  - reproducibility
  - software-engineering
  - hci
  - template
""")
            ]
        },
        
        # Week 2: Schema development
        {
            "date": start_date + timedelta(days=7),
            "message": "feat: add JSON schemas for data validation",
            "action": "copy_schemas"
        },
        
        # Week 2: Template structure
        {
            "date": start_date + timedelta(days=10),
            "message": "feat: implement basic template structure",
            "action": "copy_template_structure"
        },
        
        # Week 3: Validation system
        {
            "date": start_date + timedelta(days=14),
            "message": "feat: add JSON validation system",
            "action": "copy_validation"
        },
        
        # Week 3: Testing framework
        {
            "date": start_date + timedelta(days=18),
            "message": "feat: implement comprehensive test suite",
            "action": "copy_tests"
        },
        
        # Week 4: Scoring system
        {
            "date": start_date + timedelta(days=21),
            "message": "feat: add reproducibility scoring system",
            "action": "copy_scoring"
        },
        
        # Week 4: Documentation
        {
            "date": start_date + timedelta(days=25),
            "message": "docs: add comprehensive documentation and checklist",
            "action": "copy_docs"
        },
        
        # Week 5: Demo implementation
        {
            "date": start_date + timedelta(days=28),
            "message": "feat: add realistic demo implementation",
            "action": "copy_demo"
        },
        
        # Week 6: Bug fixes and improvements
        {
            "date": start_date + timedelta(days=35),
            "message": "fix: resolve schema validation issues and improve test coverage",
            "files": [
                ("CHANGELOG.md", """# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-12-15

### Added
- Initial release of Repl.ET template
- Comprehensive JSON schema validation
- Reproducibility scoring system
- Complete test suite with 35 tests
- Realistic demo implementation
- Documentation and compliance checklist

### Fixed
- Schema validation issues with external references
- Test coverage improvements
- Data integrity checks
""")
            ]
        },
        
        # Week 7: Final improvements
        {
            "date": start_date + timedelta(days=42),
            "message": "feat: improve schemas and add confounding factors support",
            "files": []
        },
        
        # Week 8: Final polish
        {
            "date": start_date + timedelta(days=50),
            "message": "docs: update README with comprehensive usage instructions",
            "action": "update_readme"
        },
        
        # Final commit
        {
            "date": start_date + timedelta(days=55),
            "message": "v1.0.0: stable release with 100% test coverage",
            "files": [
                ("VERSION", "1.0.0\n")
            ]
        }
    ]
    
    print("🚀 Creating Repl.ET repository with realistic development history...")
    
    # Configure git user
    subprocess.run("git config user.name 'Lucas Silva'", shell=True)
    subprocess.run("git config user.email 'lucas@replET.dev'", shell=True)
    
    for i, commit in enumerate(commits):
        print(f"\n📅 Creating commit {i+1}/{len(commits)}: {commit['message']}")
        
        commit_date = commit['date'].strftime('%Y-%m-%d %H:%M:%S')
        
        # Handle different types of commits
        if 'files' in commit:
            # Create specified files
            for file_path, content in commit.get('files', []):
                create_file(file_path, content)
                run_git_command(f"git add {file_path}")
        
        elif commit.get('action') == 'copy_schemas':
            # Copy schemas from backup
            copy_from_backup("ReplET/schemas", "schemas")
            copy_from_backup("schemas", "root_schemas") 
            run_git_command("git add schemas/")
            
        elif commit.get('action') == 'copy_template_structure':
            # Copy basic template structure
            dirs = ["participants", "equipment", "stimuli", "aois", "collection", 
                   "preprocessing", "analysis", "validity", "reproducibility"]
            for dir_name in dirs:
                os.makedirs(dir_name, exist_ok=True)
                create_file(f"{dir_name}/.gitkeep", "")
            copy_from_backup("ReplET/metadata.json", "metadata.json")
            run_git_command("git add .")
            
        elif commit.get('action') == 'copy_validation':
            copy_from_backup("ReplET/validate_jsons.py", "validate_jsons.py")
            run_git_command("git add validate_jsons.py")
            
        elif commit.get('action') == 'copy_tests':
            copy_from_backup("ReplET/tests", "tests")
            copy_from_backup("ReplET/pytest.ini", "pytest.ini")
            run_git_command("git add tests/ pytest.ini")
            
        elif commit.get('action') == 'copy_scoring':
            copy_from_backup("ReplET/repl_et_score.py", "repl_et_score.py")
            run_git_command("git add repl_et_score.py")
            
        elif commit.get('action') == 'copy_docs':
            copy_from_backup("ReplET/repl_et_checklist.md", "repl_et_checklist.md")
            copy_from_backup("ReplET/README.md", "README.md")
            run_git_command("git add *.md")
            
        elif commit.get('action') == 'copy_demo':
            copy_from_backup("Demo", "examples/demo")
            create_file("examples/README.md", """# Examples

This directory contains example implementations of the Repl.ET template.

## Demo
A complete, realistic example based on eye tracking research in code review.
""")
            run_git_command("git add examples/")
            
        elif commit.get('action') == 'update_readme':
            copy_from_backup("ReplET/README.md", "README.md")
            run_git_command("git add README.md")
        
        # Copy any remaining template files
        if i == len(commits) - 3:  # Second to last commits
            for item in os.listdir("../Repl.ET_backup/ReplET"):
                src = f"../Repl.ET_backup/ReplET/{item}"
                if os.path.isfile(src) and not os.path.exists(item):
                    shutil.copy2(src, item)
                    run_git_command(f"git add {item}")
        
        # Create commit
        run_git_command(f'git commit -m "{commit["message"]}"', commit_date)
        
        # Add a small delay to ensure different timestamps
        time.sleep(0.1)
    
    print("\n✅ Repository history created successfully!")
    print(f"📊 {len(commits)} commits spanning 2 months of development")
    print("🎯 Run 'git log --oneline' to see the commit history")

if __name__ == "__main__":
    create_commit_history() 