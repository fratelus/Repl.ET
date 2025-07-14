# 📊 Reproducibility Scoring API

## repl_et_score.py

Calculates reproducibility score across 10 dimensions (0.0-1.0 scale).

### Usage

```bash
python tools/repl_et_score.py
```

### Output Files

Generated in temporary directory:
- `report.json`: Detailed scores by dimension
- `score.png`: Radar chart visualization  
- `report.md`: Human-readable summary

### Scoring Dimensions

1. **Metadata**: Study information completeness
2. **Participants**: Demographics and recruitment
3. **Equipment**: Hardware specifications  
4. **Stimuli**: Materials and annotations
5. **AOIs**: Areas of Interest definitions
6. **Data Quality**: Collection and processing
7. **Preprocessing**: Data cleaning pipeline
8. **Analysis**: Statistical methods and results
9. **Threats**: Validity considerations
10. **Reproducibility**: Materials sharing

### Programmatic Usage

```python
import subprocess
import json
import re
import tempfile

# Run scoring
result = subprocess.run(['python', 'repl_et_score.py'], 
                       capture_output=True, text=True)

# Extract overall score
match = re.search(r'(\d+\.\d+)/1\.0', result.stdout)
overall_score = float(match.group(1)) if match else 0.0

print(f"Reproducibility Score: {overall_score*100:.1f}%")
```
