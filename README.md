# 👁️ Repl.ET: Eye Tracking Replication Template

[![Tests](https://img.shields.io/badge/tests-35%2F35%20passing-brightgreen)](https://github.com/replET/replET)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/replET/replET)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.placeholder-blue)](https://doi.org/10.5281/zenodo.placeholder)

A **standardized, validated template** for eye tracking experiments in **Software Engineering** and **Human-Computer Interaction** research. Designed to promote reproducibility and align with international guidelines.

## 🎯 Why Repl.ET?

- **🔬 Scientific Rigor**: Follows FAIR, PRISMA-Eye, iGuidelines, and TRRRACED standards
- **📋 Complete Template**: 13 JSON schemas covering all aspects of eye tracking studies  
- **✅ 100% Validated**: 35 automated tests ensure data integrity and compliance
- **📊 Reproducibility Scoring**: Automated assessment of your study's reproducibility
- **🎓 Research-Ready**: Template used in published eye tracking studies

## 🚀 Quick Start

### 1. Setup
```bash
git clone https://github.com/replET/replET.git
cd replET
pip install -r requirements.txt
```

### 2. Customize Your Study
Edit the JSON files with your study data:
```bash
# Core metadata
nano metadata.json

# Participant information  
nano participants/participants.json

# Equipment specifications
nano equipment/tracker_specs.json
nano equipment/screen_setup.json
nano equipment/software_env.json

# Study stimuli and AOIs
nano stimuli/stimuli_metadata.json
nano aois/aois_definition.json
```

### 3. Validate & Score
```bash
# Validate all JSON files against schemas
python validate_jsons.py

# Get reproducibility score (0.0-1.0)
python repl_et_score.py
```

### 4. Run Tests
```bash
# Run all 35 tests
pytest tests/ -v

# Generate coverage report
pytest --cov=. --cov-report=html tests/
```

## 📁 Repository Structure

```
replET/
├── 📄 metadata.json              # Study metadata & objectives
├── 👥 participants/              # Participant demographics  
├── 🖥️  equipment/                # Eye tracker & setup specs
├── 🎯 stimuli/                   # Code samples & materials
├── 📐 aois/                      # Areas of Interest definitions
├── 📋 collection/                # Protocols & procedures  
├── 🔧 preprocessing/             # Data cleaning pipeline
├── 📊 analysis/                  # Statistical methods & results
├── ⚠️  validity/                 # Threats & limitations
├── 🔄 reproducibility/           # Replication materials
├── 📐 schemas/                   # JSON validation schemas
├── 🧪 tests/                     # Automated test suite
└── 📖 examples/                  # Demo implementations
```

## 🏆 Features

### ✅ Comprehensive Validation
- **13 JSON Schemas** covering all study aspects
- **35 Automated Tests** ensuring data integrity
- **Cross-file consistency** checks (IDs, references)
- **Schema compliance** verification

### 📊 Reproducibility Assessment  
- **10-axis scoring system** (0.0 - 1.0)
- **FAIR principles** compliance
- **Automated reporting** (JSON, Markdown, PNG)
- **Publication-ready** metrics

### 🎓 Research Standards
- **PRISMA-Eye** compliant reporting
- **iGuidelines** for eye tracking
- **TRRRACED** transparency framework  
- **International best practices**

## 📋 Study Checklist

- [ ] ✅ **Metadata**: Title, objectives, paradigm defined
- [ ] 👥 **Participants**: Demographics, inclusion criteria  
- [ ] 🖥️ **Equipment**: Eye tracker specs, calibration protocol
- [ ] 🎯 **Stimuli**: Code samples, ground truth annotations
- [ ] 📐 **AOIs**: Areas of interest with coordinates
- [ ] 📋 **Protocol**: Data collection procedures
- [ ] 🔧 **Preprocessing**: Cleaning pipeline documented
- [ ] 📊 **Analysis**: Statistical methods specified
- [ ] ⚠️ **Validity**: Threats and limitations discussed
- [ ] 🔄 **Reproducibility**: Replication materials provided

*Complete checklist: [repl_et_checklist.md](repl_et_checklist.md)*

## 🔬 Example Studies

### 📖 Demo: Code Review Eye Tracking
```bash
cd examples/demo/ReplET
python validate_jsons.py  # ✅ All valid
python repl_et_score.py   # 📊 Score: 0.95/1.0
pytest tests/ -v          # 🧪 35/35 tests passing
```

**Study**: Eye movements during Java code review (5 participants, 5 stimuli)  
**Equipment**: Tobii Pro X3-120 (120Hz)  
**Metrics**: Fixation duration, AOI transitions, bug detection accuracy

## 🛠️ Advanced Usage

### Custom Validation
```python
from validate_jsons import validate_all_files
result = validate_all_files("your_study_directory/")
```

### Scoring API
```python  
from repl_et_score import calculate_overall_score
score = calculate_overall_score()
print(f"Reproducibility: {score:.2f}/1.0")
```

### Test Integration
```bash
# Run specific test categories
pytest -m schema tests/        # Schema validation
pytest -m integration tests/  # Cross-file consistency  
pytest -m scoring tests/       # Reproducibility scoring
```

## 📚 Documentation

- **[Getting Started Guide](docs/getting-started.md)** - Step-by-step tutorial
- **[Schema Reference](docs/schemas.md)** - Complete JSON schema documentation  
- **[Test Suite Guide](tests/README.md)** - Understanding the test framework
- **[Reproducibility Scoring](docs/scoring.md)** - How scoring works
- **[Contributing](CONTRIBUTING.md)** - How to contribute to Repl.ET

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- 🐛 Bug reports and feature requests
- 📝 Documentation improvements  
- 🧪 Additional test cases
- 🎯 New example studies

## 📄 Citation

If you use Repl.ET in your research, please cite:

```bibtex
@software{silva2024replet,
  title = {Repl.ET: Eye Tracking Replication Template},
  author = {Silva, Lucas},
  year = {2024},
  url = {https://github.com/replET/replET},
  doi = {10.5281/zenodo.placeholder},
  version = {1.0.0}
}
```

## 📊 Project Stats

- **🎯 Template Completeness**: 13/13 components  
- **✅ Test Coverage**: 35/35 tests passing (100%)
- **📋 Standards Compliance**: FAIR, PRISMA-Eye, iGuidelines, TRRRACED
- **🔬 Validation**: JSON Schema Draft 7 compliant
- **📖 Documentation**: Comprehensive guides and examples

## 🌟 Used By

- University research labs studying code comprehension
- HCI studies on developer tool usability  
- Software engineering eye tracking experiments
- Reproducibility initiatives in empirical SE

## 📞 Support

- **🐛 Issues**: [GitHub Issues](https://github.com/replET/replET/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/replET/replET/discussions)  
- **📧 Email**: replET@research.dev

---

**🎓 Research-grade • ✅ Validated • 🔬 Open Source** 