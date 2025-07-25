# 📖 ReplET User Guide

A comprehensive guide to using the **Repl.ET: Eye Tracking Replication Template** for reproducible research.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (recommended: 3.11)
- Git
- Text editor (VS Code, PyCharm, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/ReplET.git
cd ReplET

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r config/requirements.txt
```

## 📁 Understanding the Structure

### Core Components

```
ReplET/
├── 📄 metadata.json              # Study overview & objectives
├── 👥 participants/              # Demographics & recruitment
├── 🖥️  equipment/                # Eye tracker & setup specs
├── 🎯 stimuli/                   # Code samples & materials
├── 📐 aois/                      # Areas of Interest definitions
├── 📋 collection/                # Data collection protocols
├── 🔧 preprocessing/             # Data cleaning procedures
├── 📊 analysis/                  # Statistical methods & results
├── ⚠️  validity/                 # Threats & limitations
├── 🔄 reproducibility/           # Replication materials
├── 📐 schemas/                   # JSON validation schemas (13 files)
├── 🧰 utils/                     # Assessment and scoring tools
└── 🏗️  data/                     # Organized data storage structure
```

### Example Implementations

- **📋 Template (Root)**: Clean starting template (5.0% score - empty foundation)
- **📚 examples/basic/**: Learning example (~30% score - basic implementation) 
- **🏆 examples/advanced/**: Publication-ready study (83.0% score - complete documentation)

## 🎯 Choosing Your Starting Point

### For Learning → examples/basic/
```bash
cd examples/basic/
python ../../utils/update_readme_with_assessment.py
# Score: ~30% | Status: Basic Setup
```

### For New Study → Root Template
```bash
# Start from clean template
python utils/update_readme_with_assessment.py
# Score: 5.0% | Status: Empty Template
```

### For Publication → examples/advanced/
```bash
cd examples/advanced/
python ../../utils/update_readme_with_assessment.py  
# Score: 83.0% | Status: Complete (Publication Ready)
```

## 📊 Assessment and Scoring

### Generate Your Study Score
```bash
# From any directory containing study files
python utils/update_readme_with_assessment.py
```

This generates:
- **📈 Spider graph PNG**: Visual reproducibility assessment
- **📋 Compliance checklist**: Component-by-component status
- **📊 Scores table**: Detailed breakdown by criteria
- **📝 Updated README**: Automatic documentation updates

### Understanding Scores

| Score Range | Status | Meaning |
|------------|--------|---------|
| **80-100%** | ✅ Complete | Publication-ready documentation |
| **60-79%** | ⚠️ Good Practice | Solid foundation, minor gaps |
| **40-59%** | 🟠 Needs Work | Basic structure, major improvements needed |
| **0-39%** | ⚪ Template/Learning | Starting point or educational baseline |

## 🔄 Workflow: From Template to Publication

### Step 1: Initialize Your Study
```bash
# Copy template structure
cp -r ReplET/ MyStudy/
cd MyStudy/

# Run initial assessment
python utils/update_readme_with_assessment.py
# Expected: ~5% (Empty Template)
```

### Step 2: Fill Core Components
Edit these files first:
1. `metadata.json` - Study title, objectives, authors
2. `participants/participants.json` - Demographics and recruitment
3. `equipment/tracker_specs.json` - Your eye tracker setup

```bash
# Check progress
python utils/update_readme_with_assessment.py
# Expected: 20-40% (Basic Setup)
```

### Step 3: Complete Methodology
4. `stimuli/stimuli_metadata.json` - Your experimental materials
5. `aois/aois_definition.json` - Areas of interest
6. `collection/protocol.json` - Data collection procedures
7. `preprocessing/preprocessing.json` - Analysis pipeline

```bash
# Check progress  
python utils/update_readme_with_assessment.py
# Expected: 50-70% (Good Practice)
```

### Step 4: Research Rigor
8. `analysis/analysis.json` - Statistical methods and results
9. `validity/validity.json` - Threats and limitations
10. `reproducibility/reproducibility.json` - Sharing materials

```bash
# Final assessment
python utils/update_readme_with_assessment.py
# Target: 80%+ (Publication Ready)
```

## 🏆 Advanced Features

### Data Organization
The template includes a complete data organization structure:

```
data/
├── raw/                   # Original data files (not in Git)
│   ├── eye_tracking/     # .gazedata, .tsv files
│   ├── eeg/              # .eeg, .vhdr, .vmrk files  
│   └── behavioral/       # Response data, questionnaires
├── processed/            # Cleaned data ready for analysis
├── analysis/             # Final datasets for statistics
└── results/              # Outputs, figures, reports
```

### Multi-Modal Studies
The advanced example demonstrates:
- **Synchronized data collection**: Eye tracking + EEG + physiological
- **Quality control**: Real-time monitoring and validation
- **Complex analyses**: Machine learning, network analysis, cognitive load

### Validation and Testing
```bash
# Run template validation
python tests/run_tests.py

# Check data integrity
python tests/test_data_integrity.py

# Validate JSON schemas
python utils/validate_jsons.py
```

## 🎓 Learning Path

### Beginner: Understand Structure
1. Read `examples/basic/` to see simple implementations
2. Run assessment to see component scoring
3. Practice editing one component at a time

### Intermediate: Build Complete Study  
1. Start from root template
2. Fill components systematically
3. Aim for 60%+ score with good practices

### Advanced: Publication Standards
1. Study `examples/advanced/` for comprehensive documentation
2. Implement advanced features (multi-modal, international collaboration)
3. Achieve 80%+ score for publication readiness

## 🔧 Customization

### Adapting for Your Domain
- Modify `schemas/*.schema.json` for domain-specific requirements
- Customize scoring weights in `utils/update_readme_with_assessment.py`
- Add new components following existing patterns

### Integration with Analysis Tools
```python
# Import scoring functions
from utils.repl_et_score import calculate_reproducibility_score

# Use in your analysis pipeline
score = calculate_reproducibility_score('path/to/study/')
```

## ❓ Troubleshooting

### Common Issues

**Low scores despite complete files**:
- Check for template placeholder text
- Ensure realistic, specific content
- Verify file structure matches schemas

**Assessment script errors**:
- Confirm all required JSON files exist
- Validate JSON syntax
- Check Python dependencies

**Data organization confusion**:
- Use provided `data/` structure
- Follow naming conventions
- Keep raw data separate from processed

### Getting Help
- 📖 Check documentation in `.project/docs/`
- 🐛 Report issues on GitHub
- 💬 Join community discussions
- 📧 Contact maintainers for research collaborations

## 📈 Success Metrics

Track your progress toward reproducible research:

- **📋 Documentation Completeness**: All 10 components filled
- **📊 Reproducibility Score**: Target 80%+ for publication
- **🔄 Replication Support**: Materials available for others
- **✅ Validation Passing**: All tests and schema validation
- **🌟 Community Impact**: Citations and reuse by other researchers

Remember: The goal isn't just high scores, but **genuinely reproducible research** that advances scientific knowledge! 