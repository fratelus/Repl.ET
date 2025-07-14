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
└── 📐 schemas/                   # JSON validation schemas (13 files)
```

### Example Implementations

- **📚 Demo/**: Basic learning example (0.0% score - template baseline)
- **🏆 Demo02/**: Publication-ready example (70.0% score - good practice)

## 🛠️ Step-by-Step Workflow

### 1. Start with an Example

```bash
# Explore the basic example
cd Demo/
python tools/validate_jsons.py    # See validation
python tools/repl_et_score.py     # Generate spider graph (0.0%)
pytest                      # Run tests

# Study the advanced example
cd ../Demo02/
python tools/validate_jsons.py    # Validate comprehensive data
python tools/repl_et_score.py     # Generate spider graph (70.0%)
pytest                      # Run tests
```

### 2. Customize for Your Study

#### A. Study Metadata (`metadata.json`)
```json
{
  "study_title": "Your Study Title",
  "paradigm": "free_viewing|task_driven|reading",
  "task_description": "Detailed task description",
  "research_questions": ["RQ1", "RQ2"],
  "hypotheses": ["H1", "H2"]
}
```

#### B. Participants (`participants/participants.json`)
```json
{
  "recruitment": {
    "method": "convenience|snowball|random",
    "criteria_inclusion": ["criteria"],
    "criteria_exclusion": ["criteria"]
  },
  "participants": [
    {
      "id": "P01",
      "age": 25,
      "gender": "female|male|other",
      "handedness": "right|left|ambidextrous",
      "vision": "normal|corrected|impaired"
    }
  ]
}
```

#### C. Equipment Setup
```bash
# Edit equipment specifications
nano equipment/tracker_specs.json     # Eye tracker details
nano equipment/screen_setup.json      # Display configuration  
nano equipment/software_env.json      # Software environment
```

#### D. Stimuli and AOIs
```bash
# Prepare your code stimuli
mkdir stimuli/stimuli_raw/
# Add your code files here

# Define your areas of interest
nano aois/aois_definition.json
```

### 3. Validate Your Data

```bash
# Validate all JSON files against schemas
python tools/validate_jsons.py

# Check for specific issues
python tools/validate_jsons.py --verbose
```

### 4. Generate Reproducibility Score

```bash
# Generate spider graph analysis
python tools/repl_et_score.py

# Output includes:
# - Beautiful spider graph (PNG)
# - Detailed JSON report
# - Markdown summary
# - Temporary directory path shown
```

### 5. Run Quality Tests

```bash
# Run all 35 automated tests
pytest

# Run specific test categories
pytest -m schema tests/        # Schema validation
pytest -m integration tests/  # Cross-file consistency
pytest -m scoring tests/       # Reproducibility scoring

# Generate coverage report
pytest --cov=. --cov-report=html tests/
```

## 🕷️ Understanding Spider Graphs

### Criteria Breakdown

Your spider graph shows scores (0.0-1.0) for:

1. **Study Metadata**: Title, objectives, paradigm clarity
2. **Participant Info**: Demographics, recruitment transparency  
3. **Equipment Specs**: Eye tracker specifications completeness
4. **Stimuli & Materials**: Code samples, annotations quality
5. **Areas of Interest**: AOI definitions and visualizations
6. **Data Quality**: Collection protocols and quality control
7. **Data Preprocessing**: Cleaning pipeline documentation
8. **Statistical Analysis**: Methods, results, effect sizes
9. **Validity Threats**: Internal/external validity discussion
10. **Reproducibility Materials**: Sharing and replication support

### Color Interpretation

- **🟢 Green (80%+)**: Publication-ready, excellent reproducibility
- **🟡 Orange (60-79%)**: Good practice, minor improvements needed
- **🟠 Red (40-59%)**: Fair reproducibility, significant gaps
- **⚪ Gray (<40%)**: Template/learning baseline

## 📊 Improving Your Score

### Quick Wins (Easy improvements):

1. **Complete metadata.json** with all required fields
2. **Add participant demographics** with proper inclusion/exclusion criteria
3. **Document equipment specifications** thoroughly
4. **Create AOI visualizations** for your stimuli
5. **Write analysis plan** with statistical methods

### Advanced Improvements:

1. **Add ORCID IDs** and funding information
2. **Include power analysis** and sample size justification
3. **Document preprocessing pipeline** with scripts
4. **Add validity threat assessment**
5. **Provide replication materials** (code, data, protocols)

### Publication-Ready Checklist:

- [ ] ✅ All 13 JSON files complete and valid
- [ ] ✅ Reproducibility score ≥ 80%
- [ ] ✅ All 35 tests passing
- [ ] ✅ Spider graph shows balanced coverage
- [ ] ✅ Documentation includes replication materials

## 🤖 GitHub Integration

### Automated Workflows

When you push to GitHub, automated workflows will:

1. **Run all tests** across Python 3.8-3.12
2. **Generate spider graphs** for all examples  
3. **Update README** with latest spider analysis
4. **Validate schemas** and cross-references
5. **Benchmark performance** and generate reports

### Accessing Results

1. **View in README**: Spider graph automatically visible
2. **Download artifacts**: Actions → workflow run → spider-analysis
3. **Local reports**: Run scoring scripts for detailed breakdown

## 🔧 Advanced Features

### Custom Validation

```python
from validate_jsons import validate_all_files

# Validate specific directory
result = validate_all_files("path/to/study/")
if result["valid"]:
    print("All files valid!")
else:
    print(f"Errors: {result['errors']}")
```

### Scoring API

```python
from repl_et_score import calculate_overall_score

# Get programmatic score
score = calculate_overall_score()
print(f"Reproducibility: {score:.3f}/1.0 ({score*100:.1f}%)")
```

### Batch Processing

```bash
# Process multiple studies
for dir in study1/ study2/ study3/; do
    cd $dir
    echo "Processing $dir..."
    python tools/validate_jsons.py
    python tools/repl_et_score.py
    cd ..
done
```

## 🆘 Troubleshooting

### Common Issues

**Q: Validation fails with "file not found"**
A: Ensure all required JSON files exist. Check `schemas/` for required structure.

**Q: Low reproducibility score**  
A: Run with `--verbose` to see which criteria need improvement. Focus on metadata, participants, and analysis sections.

**Q: Tests failing**
A: Run `pytest -v` for detailed output. Common issues: missing files, invalid JSON, ID mismatches.

**Q: Spider graph not generating**
A: Install matplotlib: `pip install matplotlib`. Check that output directory is writable.

### Getting Help

1. **Check examples**: Compare with Demo/ and Demo02/ implementations
2. **Read error messages**: Most validation errors include specific guidance
3. **Run tests**: `pytest -v` shows exactly what's failing
4. **Check schemas**: `schemas/` directory documents expected structure

## 📚 Research Standards Compliance

ReplET ensures compliance with:

- **🔬 FAIR Principles**: Findable, Accessible, Interoperable, Reusable
- **👁️ PRISMA-Eye**: Reporting guidelines for eye tracking studies
- **📋 iGuidelines**: International eye tracking research standards  
- **🔄 TRRRACED**: Transparency framework for reproducible research

## 🎓 Best Practices

### For Beginners
1. Start with Demo/ to understand structure
2. Copy and modify rather than starting from scratch
3. Validate early and often
4. Aim for basic completeness before perfection

### For Advanced Users
1. Study Demo02/ for publication-ready standards
2. Customize schemas for specific research domains
3. Integrate with existing data analysis pipelines
4. Contribute improvements back to the community

---

**📧 Support**: For questions, create an issue on GitHub or consult the main README.md
**🔗 More Info**: Visit the full documentation and examples in the repository. 