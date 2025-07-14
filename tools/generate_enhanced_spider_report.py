#!/usr/bin/env python3

import os
import subprocess
import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import tempfile
import sys

def run_scoring_with_details(directory):
    """Run scoring script in a directory and extract detailed scores."""
    original_dir = os.getcwd()
    try:
        os.chdir(directory)
        result = subprocess.run(['python3', 'repl_et_score.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Find the temporary directory from output
            lines = result.stdout.split('\n')
            temp_dir = None
            for line in lines:
                if 'Output directory:' in line:
                    temp_dir = line.split(': ')[1].strip()
                    break
            
            if temp_dir and os.path.exists(os.path.join(temp_dir, 'report.json')):
                with open(os.path.join(temp_dir, 'report.json'), 'r') as f:
                    scores = json.load(f)
                return scores
            else:
                print(f"Warning: Could not find report.json for {directory}")
                return None
        else:
            print(f"Error running scoring for {directory}: {result.stderr}")
            return None
    finally:
        os.chdir(original_dir)

def create_beautiful_spider_chart():
    """Create beautiful spider charts showing individual criteria for each directory."""
    
    # Get detailed scores for all directories
    directories = {
        'ReplET Template': '.',
        'Demo (Learning)': 'Demo',
        'Demo02 (Publication)': 'Demo02'
    }
    
    all_scores = {}
    for name, path in directories.items():
        scores = run_scoring_with_details(path)
        if scores:
            all_scores[name] = scores
            # Calculate overall score
            overall = sum(scores.values()) / len(scores)
            print(f"{name}: {overall*100:.1f}% overall")
        else:
            print(f"Failed to get scores for {name}")
            return None, None
    
    if not all_scores:
        print("No valid scores found!")
        return None, None
    
    # Set up the plot with modern styling
    plt.style.use('default')
    fig = plt.figure(figsize=(20, 12))
    
    # Define criteria labels (cleaned up)
    criteria_labels = {
        'metadata': 'Study\nMetadata',
        'participants': 'Participant\nInfo',
        'equipment': 'Equipment\nSpecs',
        'stimuli': 'Stimuli\n& Materials',
        'aois': 'Areas of\nInterest',
        'data_quality': 'Data Quality\n& Collection',
        'preprocessing': 'Data\nPreprocessing',
        'analysis': 'Statistical\nAnalysis',
        'threats': 'Validity\nThreats',
        'reproducibility': 'Reproducibility\nMaterials'
    }
    
    # Create individual spider plots for each directory
    for i, (name, scores) in enumerate(all_scores.items(), 1):
        ax = plt.subplot(2, 3, i, projection='polar')
        
        # Get criteria in consistent order
        criteria = list(criteria_labels.keys())
        labels = [criteria_labels[c] for c in criteria]
        values = [scores.get(c, 0.0) for c in criteria]
        
        # Close the radar chart
        angles = np.linspace(0, 2*np.pi, len(criteria), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]
        
        # Color based on overall score
        overall_score = sum(scores.values()) / len(scores)
        if overall_score >= 0.8:
            color = '#2ecc71'  # Green
        elif overall_score >= 0.6:
            color = '#f39c12'  # Orange
        elif overall_score >= 0.4:
            color = '#e74c3c'  # Red
        else:
            color = '#95a5a6'  # Gray
        
        # Plot the spider chart
        ax.plot(angles, values, 'o-', linewidth=3, color=color, markersize=6)
        ax.fill(angles, values, alpha=0.25, color=color)
        
        # Customize the chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=9)
        ax.set_ylim(0, 1.0)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=8)
        ax.grid(True, alpha=0.3)
        
        # Add title with score
        ax.set_title(f'{name}\n{overall_score*100:.1f}% Overall Score', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Add value labels for non-zero scores
        for angle, value, label in zip(angles[:-1], values[:-1], labels):
            if value > 0.1:  # Only show labels for significant values
                ax.text(angle, value + 0.05, f'{value:.2f}', 
                       ha='center', va='center', fontsize=8, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    # Create comparison chart
    ax_comp = plt.subplot(2, 3, (4, 6))
    
    # Prepare data for comparison
    comparison_data = {}
    for criterion in criteria:
        comparison_data[criteria_labels[criterion]] = [
            all_scores[name].get(criterion, 0.0) for name in all_scores.keys()
        ]
    
    # Create grouped bar chart
    x = np.arange(len(criteria_labels))
    width = 0.25
    
    colors = ['#95a5a6', '#95a5a6', '#2ecc71']  # Gray for templates, green for publication
    for i, (name, color) in enumerate(zip(all_scores.keys(), colors)):
        values = [all_scores[name].get(c, 0.0) for c in criteria]
        bars = ax_comp.bar(x + i*width, values, width, label=name, color=color, alpha=0.8)
        
        # Add value labels on bars for non-zero values
        for bar, value in zip(bars, values):
            if value > 0.05:
                height = bar.get_height()
                ax_comp.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                           f'{value:.2f}', ha='center', va='bottom', fontsize=8)
    
    ax_comp.set_xlabel('Reproducibility Criteria', fontsize=12)
    ax_comp.set_ylabel('Score (0.0 - 1.0)', fontsize=12)
    ax_comp.set_title('Reproducibility Criteria Comparison', fontsize=16, fontweight='bold')
    ax_comp.set_xticks(x + width)
    ax_comp.set_xticklabels([criteria_labels[c] for c in criteria], rotation=45, ha='right')
    ax_comp.legend()
    ax_comp.grid(axis='y', alpha=0.3)
    ax_comp.set_ylim(0, 1.1)
    
    plt.tight_layout()
    
    # Save the chart
    output_path = 'outputs/reproducibility_spider_analysis.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()  # Clean up memory instead of showing
    
    return all_scores, output_path

def generate_markdown_report(all_scores):
    """Generate a comprehensive markdown report with spider graph."""
    
    # Calculate overall scores
    overall_scores = {}
    for name, scores in all_scores.items():
        overall_scores[name] = sum(scores.values()) / len(scores)
    
    markdown = f"""
## 📊 Reproducibility Analysis

![Reproducibility Spider Analysis](outputs/reproducibility_spider_analysis.png)

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
| **ReplET Template** | {overall_scores.get('ReplET Template', 0)*100:.1f}% | 📋 Template | Base template for new studies |
| **Demo (Learning)** | {overall_scores.get('Demo (Learning)', 0)*100:.1f}% | 🎓 Learning | Minimal example for understanding |
| **Demo02 (Publication)** | {overall_scores.get('Demo02 (Publication)', 0)*100:.1f}% | ✅ Publication Ready | Gold standard implementation |

### 🎯 Score Interpretation

- **🟢 80%+ (Excellent)**: Publication-ready, meets gold standards
- **🟡 60-79% (Good)**: Solid reproducibility with minor gaps  
- **🟠 40-59% (Fair)**: Basic reproducibility, needs improvement
- **⚪ <40% (Template/Learning)**: Educational baseline or template

### 📋 Detailed Criteria Scores
"""

    # Add detailed breakdown for Demo02 (the high-scoring one)
    if 'Demo02 (Publication)' in all_scores:
        demo02_scores = all_scores['Demo02 (Publication)']
        markdown += "\n#### 🏆 Demo02 (Publication-Ready) Breakdown:\n"
        
        criteria_descriptions = {
            'metadata': 'Study metadata with ORCID, funding, ethics',
            'participants': 'Comprehensive demographics & power analysis',
            'equipment': 'Professional eye tracker specifications',
            'stimuli': 'Annotated code samples with ground truth',
            'aois': 'Detailed areas of interest definitions',
            'data_quality': 'Rigorous collection protocols',
            'preprocessing': 'Documented data cleaning pipeline',
            'analysis': 'Complete statistical analysis plan',
            'threats': 'Thorough validity threat assessment',
            'reproducibility': 'Full replication materials & sharing'
        }
        
        for criterion, score in demo02_scores.items():
            status = "✅" if score >= 0.8 else "🟡" if score >= 0.6 else "🟠" if score >= 0.4 else "❌"
            description = criteria_descriptions.get(criterion, criterion)
            markdown += f"- {status} **{criterion.replace('_', ' ').title()}**: {score:.2f} - {description}\n"
    
    markdown += """
### 🚀 Quick Start

```bash
# Run scoring on main template
python3 repl_et_score.py

# Compare with examples
cd Demo && python3 repl_et_score.py     # Learning baseline
cd ../Demo02 && python3 repl_et_score.py  # Publication standard
```
"""
    
    return markdown

if __name__ == "__main__":
    print("🔄 Generating enhanced spider graph analysis...")
    
    scores, chart_path = create_beautiful_spider_chart()
    if scores:
        markdown_report = generate_markdown_report(scores)
        
        print(f"\n📈 Spider analysis saved as: {chart_path}")
        print(f"\n📝 Markdown report:\n{markdown_report}")
        print(f"\n✅ Enhanced spider graph analysis complete!")
    else:
        print("❌ Failed to generate spider graph analysis")
        sys.exit(1) 