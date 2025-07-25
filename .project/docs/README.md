# 📖 ReplET Documentation

Welcome to the ReplET documentation! Here you'll find comprehensive guides and references for using the Eye Tracking Replication Template.

## 📋 Quick Navigation

### 🚀 Getting Started
- **[User Guide](USER_GUIDE.md)** - Complete step-by-step guide for using ReplET
- **[Research Checklist](repl_et_checklist.md)** - Quality checklist for your study
- **[Examples Comparison](examples/demo-comparison.md)** - Detailed comparison of basic vs advanced examples

### 📊 Understanding Scores
Your reproducibility spider graph shows 10 criteria:

| Criteria | Weight | Description |
|----------|--------|-------------|
| Study Metadata | 10% | Title, objectives, paradigm definition |
| Participant Info | 10% | Demographics, recruitment transparency |
| Equipment Specs | 10% | Eye tracker specifications completeness |
| Stimuli & Materials | 10% | Code samples, annotations quality |
| Areas of Interest | 10% | AOI definitions and visualizations |
| Data Quality | 10% | Collection protocols and quality control |
| Data Preprocessing | 10% | Cleaning pipeline documentation |
| Statistical Analysis | 10% | Methods, results, effect sizes |
| Validity Threats | 10% | Internal/external validity discussion |
| Reproducibility Materials | 10% | Sharing and replication support |

### 🎯 Score Targets

- **🟢 80%+ (Publication-Ready)**: Meets gold standard for reproducible research
- **🟡 60-79% (Good Practice)**: Solid foundation, minor improvements needed
- **🟠 40-59% (Needs Work)**: Basic structure, significant gaps to address
- **⚪ <40% (Template/Learning)**: Educational baseline or starting template

## 🏆 Examples Breakdown

### Template/ (Root Directory) - Empty Template (5.0%)
- **Purpose**: Clean starting template for new studies
- **Status**: Empty Template (4/17 criteria met - 24% compliance)
- **Files**: All JSON components with placeholder structure
- **Use**: Clone and fill with your study information

### examples/basic/ - Learning Example (~30%)
- **Purpose**: Basic study implementation for learning
- **Status**: Basic Setup (~8/17 criteria met - 47% compliance) 
- **Strengths**: Simple but realistic data examples
- **Use**: Understand component relationships and basic completion

### examples/advanced/ - Publication-Ready Example (83.0%)
- **Purpose**: Comprehensive multi-modal study demonstration
- **Status**: Complete - Publication Ready (8/10 criteria met - 80% compliance)
- **Strengths**: 
  - ✅ Study Metadata (95%), Equipment (95%), Stimuli (95%)
  - ✅ Preprocessing (95%), Analysis (95%), Validity (95%), Reproducibility (95%)
  - ✅ Participant Info (90%)
  - ⚠️ AOIs (70%)
  - ❌ Data Quality (5%) - Template level
- **Use**: Reference for journal submission and publication standards

## 📈 Score Evolution

```
Template → Basic → Advanced
  5.0%  →  30%   →  83.0%
  
Growth: 16.6x improvement from template to advanced!
```

## 🔧 Advanced Topics

### Customizing Schemas
The 13 JSON schemas in `../schemas/` can be customized for your research domain while maintaining validation compatibility.

### Running Assessment
Generate your study's reproducibility score:
```bash
python utils/update_readme_with_assessment.py
```

### API References
- **[Scoring API](api/scoring.md)** - Automated reproducibility scoring
- **[Validation API](api/validation.md)** - Schema validation tools 