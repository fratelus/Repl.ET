# 👁️ Repl.ET: Eye Tracking Replication Template

[![Tests](https://img.shields.io/badge/tests-35%2F35%20passing-brightgreen)](https://github.com/fratelus/Repl.ET)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/fratelus/Repl.ET)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending-blue)](#)

A **standardized, validated template** for eye tracking experiments in **Software Engineering** and **Human-Computer Interaction** research. Designed to promote reproducibility and align with international guidelines.

## 🎯 Why Repl.ET?

- **🔬 Scientific Rigor**: Follows FAIR, PRISMA-Eye, iGuidelines, and TRRRACED standards
- **📋 Complete Template**: 13 JSON schemas covering all aspects of eye tracking studies  
- **✅ 100% Validated**: 35 automated tests ensure data integrity and compliance
- **📊 Reproducibility Scoring**: Automated assessment of your study's reproducibility
- **🎓 Research-Ready**: Template used in published eye tracking studies
- **🔗 Link Verification**: Automated link checking prevents broken documentation

## 🚀 Quick Start

```bash
# 1. Setup
git clone https://github.com/your-org/ReplET.git
cd ReplET
pip install -r config/requirements.txt

# 2. Explore Examples
cd Demo/ && python repl_et_score.py      # Basic example (0.0% baseline)
cd ../Demo02/ && python repl_et_score.py # Advanced example (70.0% good practice)

# 3. Customize & Validate
cd .. && cp -r Demo/ MyStudy/           # Start from template
# Edit JSON files in MyStudy/
python tools/validate_jsons.py         # Validate your data
python tools/repl_et_score.py          # Generate your spider graph

# 4. Quality Check
pytest tests/ -v                       # Run all 35 tests
./scripts/check-links.sh               # Check documentation links
```

📖 **[→ Read the Complete User Guide](docs/USER_GUIDE.md)** for detailed instructions, troubleshooting, and best practices.

## 📁 Repository Structure

```
ReplET/
├── 📄 Core Data Files            # metadata.json + 12 data directories
├── 📐 schemas/                   # 13 JSON validation schemas  
├── 🧪 tests/                     # 35 automated tests
├── 📚 Demo/                      # Basic example (0.0% baseline)
├── 🏆 Demo02/                    # Advanced example (70.0% good practice)
├── 📖 docs/                      # Documentation (user guide, checklist)
└── 🕷️ repl_et_score.py           # Spider graph generator
```

**13 Data Components**: metadata, participants, equipment (3 files), stimuli, aois, collection, preprocessing, analysis, validity, reproducibility - each with schemas and validation.

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

*Complete checklist: [repl_et_checklist.md](docs/repl_et_checklist.md)*

## 🔬 Example Studies

### 📖 Demo: Code Review Eye Tracking
```bash
cd examples/demo/ReplET
python tools/validate_jsons.py  # ✅ All valid
python tools/repl_et_score.py   # 📊 Score: 0.95/1.0
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

### 🤖 GitHub Actions Integration

ReplET includes comprehensive **CI/CD automation** that generates spider graphs automatically:

```yaml
# Automated spider graph generation on every push/PR
🕷️ Reproducibility Spider Analysis:
  - Generates individual spider graphs for main template + demos
  - Creates comparative analysis with side-by-side visualization  
  - Uploads spider analysis as downloadable artifacts
  - Supports headless environments (Linux, macOS, Windows)
```

**Features in GitHub Actions:**
- ✅ **Automated Testing**: 35 tests across Python 3.8-3.12
- ✅ **Spider Graph Generation**: Individual + comparative analysis
- ✅ **Auto-Update README**: Commits updated spider graph to repository
- ✅ **Cross-platform**: Ubuntu, macOS, Windows compatibility
- ✅ **Artifact Storage**: 30-day retention of spider graphs
- ✅ **Demo Validation**: Ensures Demo02 maintains 80%+ score
- ✅ **Performance Benchmarking**: Speed and memory profiling

**Accessing Results:**
1. **View in README**: Spider graph automatically visible above (auto-updated)
2. **Download Artifacts**: Go to **Actions** → workflow run → download **reproducibility-spider-analysis** 
3. **Individual Reports**: Run `python3 repl_et_score.py` locally for detailed breakdown

## 📊 Reproducibility Analysis

![Reproducibility Spider Analysis](outputs/reproducibility_spider_analysis.png)

> 🤖 **Auto-Updated**: This spider graph is automatically regenerated by GitHub Actions on every push, ensuring it always reflects the current state of all examples.

### 🕷️ Spider Graph Breakdown

The spider graphs above show **10 reproducibility criteria** for each implementation:

| Criteria | Description |
|----------|-------------|
| **Study Metadata** | Title, objectives, paradigm definition |
| **Participant Info** | Demographics, recruitment, inclusion criteria |
| **Equipment Specs** | Eye tracker specifications, calibration |
| **Stimuli & Materials** | Code samples, annotations, ground truth |
| **Areas of Interest** | AOI definitions and visualizations |
| **Data Quality** | Collection protocols, quality control |
| **Data Preprocessing** | Cleaning pipeline, filtering methods |
| **Statistical Analysis** | Methods, results, effect sizes |
| **Validity Threats** | Internal/external validity discussion |
| **Reproducibility Materials** | Sharing, documentation, replication |

### 📈 Overall Scores

| Implementation | Overall Score | Status | Purpose |
|----------------|---------------|--------|---------|
| **ReplET Template** | 0.0% | 📋 Template | Base template for new studies |
| **Demo (Learning)** | 0.0% | 🎓 Learning | Minimal example for understanding |
| **Demo02 (Publication)** | 82.5% | ✅ Publication Ready | Gold standard implementation |

### 🎯 Score Interpretation

- **🟢 80%+ (Excellent)**: Publication-ready, meets gold standards
- **🟡 60-79% (Good)**: Solid reproducibility with minor gaps  
- **🟠 40-59% (Fair)**: Basic reproducibility, needs improvement
- **⚪ <40% (Template/Learning)**: Educational baseline or template

### 📋 Detailed Criteria Scores

#### 🏆 Demo02 (Publication-Ready) Breakdown:
- ❌ **Metadata**: 0.25 - Study metadata with ORCID, funding, ethics
- 🟡 **Participants**: 0.75 - Comprehensive demographics & power analysis
- ✅ **Equipment**: 1.00 - Professional eye tracker specifications
- ✅ **Stimuli**: 1.00 - Annotated code samples with ground truth
- 🟡 **Aois**: 0.75 - Detailed areas of interest definitions
- ✅ **Data Quality**: 1.00 - Rigorous collection protocols
- 🟡 **Preprocessing**: 0.75 - Documented data cleaning pipeline
- 🟡 **Analysis**: 0.75 - Complete statistical analysis plan
- ✅ **Threats**: 1.00 - Thorough validity threat assessment
- ✅ **Reproducibility**: 1.00 - Full replication materials & sharing

### 🚀 Quick Start

```bash
# Run scoring on main template (generates spider graph)
python3 repl_et_score.py
# ↳ Creates beautiful spider graph showing all 10 reproducibility criteria
# ↳ Saves to temporary directory (path shown in output)

# Compare with examples
cd Demo && python3 repl_et_score.py     # Learning baseline (own spider graph)
cd ../Demo02 && python3 repl_et_score.py  # Publication standard (own spider graph)

# Generate comparative analysis (all 3 directories)
python3 generate_enhanced_spider_report.py
# ↳ Creates side-by-side comparison with individual spider graphs
```

### 🕷️ Spider Graph Features

Each `repl_et_score.py` execution generates a **beautiful spider graph** with:

- **🎨 Color-coded visualization**: Green (80%+), Orange (60-79%), Red (40-59%), Gray (<40%)
- **📊 10 reproducibility criteria**: Individual scores for each research aspect
- **🏷️ Value annotations**: Exact scores displayed for significant values  
- **📐 Professional styling**: Clear grid, readable labels, publication-ready quality
- **💾 Multiple formats**: PNG image, JSON data, Markdown report

**Example Spider Graph Breakdown:**
- **Study Metadata**: Title, objectives, paradigm definition
- **Participant Info**: Demographics, recruitment, inclusion criteria  
- **Equipment Specs**: Eye tracker specifications, calibration
- **Stimuli & Materials**: Code samples, annotations, ground truth
- **Areas of Interest**: AOI definitions and visualizations
- **Data Quality**: Collection protocols, quality control
- **Data Preprocessing**: Cleaning pipeline, filtering methods
- **Statistical Analysis**: Methods, results, effect sizes
- **Validity Threats**: Internal/external validity discussion
- **Reproducibility Materials**: Sharing, documentation, replication

## 📚 Documentation

- **[📖 User Guide](docs/USER_GUIDE.md)** - Complete usage guide with examples
- **[📐 Schema Reference](schemas/)** - 13 JSON validation schemas  
- **[🧪 Test Documentation](tests/)** - 35 automated tests
- **[📋 Research Checklist](docs/repl_et_checklist.md)** - Quality checklist

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
  url = {https://github.com/fratelus/Repl.ET},
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

- **🐛 Issues**: [GitHub Issues](https://github.com/fratelus/Repl.ET/issues)
- **💬 Questions**: Create an issue with the "question" label  
- **📧 Email**: replET@research.dev

---

**🎓 Research-grade • ✅ Validated • 🔬 Open Source** 