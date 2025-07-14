import os
import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt
import numpy as np

def check_metadata():
    try:
        with open("ReplET/metadata.json") as f:
            data = json.load(f)
        required = ["study_title", "paradigm", "task_description"]
        if all(k in data and data[k] for k in required):
            return 1.0
        elif any(k in data for k in required):
            return 0.5
        else:
            return 0.25
    except Exception:
        return 0

def check_participants():
    path = "ReplET/participants/participants.json"
    if not os.path.exists(path):
        return 0
    try:
        with open(path) as f:
            data = json.load(f)
        if "participants" in data and len(data["participants"]) > 0:
            fields = ["age", "gender", "handedness", "vision"]
            has_fields = all(all(field in p for field in fields) for p in data["participants"])
            if has_fields:
                return 1.0
            else:
                return 0.75
        else:
            return 0.25
    except Exception:
        return 0

def check_equipment():
    files = ["ReplET/equipment/tracker_specs.json", "ReplET/equipment/screen_setup.json", "ReplET/equipment/software_env.json"]
    found = sum(os.path.exists(f) for f in files)
    if found == 3:
        return 1.0
    elif found == 2:
        return 0.75
    elif found == 1:
        return 0.5
    else:
        return 0

def check_stimuli():
    meta = "ReplET/stimuli/stimuli_metadata.json"
    ann = "ReplET/stimuli/stimuli_annotations.json"
    raw = "ReplET/stimuli/stimuli_raw"
    score = 0
    if os.path.exists(meta):
        score += 0.4
    if os.path.exists(ann):
        score += 0.3
    if os.path.isdir(raw) and len(os.listdir(raw)) > 0:
        score += 0.3
    return min(score, 1.0)

def check_aois():
    aois = "ReplET/aois/aois_definition.json"
    vis = "ReplET/aois/aois_visualizations"
    if os.path.exists(aois):
        if os.path.isdir(vis) and len(os.listdir(vis)) > 0:
            return 1.0
        else:
            return 0.75
    else:
        return 0

def check_data_quality():
    proto = "ReplET/collection/protocol.json"
    logs = "ReplET/collection/logs"
    if os.path.exists(proto):
        if os.path.isdir(logs) and len(os.listdir(logs)) > 0:
            return 1.0
        else:
            return 0.75
    else:
        return 0

def check_preprocessing():
    pre = "ReplET/preprocessing/preprocessing.json"
    scripts = "ReplET/preprocessing/scripts"
    if os.path.exists(pre):
        if os.path.isdir(scripts) and len(os.listdir(scripts)) > 0:
            return 1.0
        else:
            return 0.75
    else:
        return 0

def check_analysis():
    ana = "ReplET/analysis/analysis.json"
    tables = "ReplET/analysis/results_tables"
    vis = "ReplET/analysis/visualizations"
    score = 0
    if os.path.exists(ana):
        score += 0.5
    if os.path.isdir(tables) and len(os.listdir(tables)) > 0:
        score += 0.25
    if os.path.isdir(vis) and len(os.listdir(vis)) > 0:
        score += 0.25
    return min(score, 1.0)

def check_threats():
    val = "ReplET/validity/validity.json"
    if os.path.exists(val):
        with open(val) as f:
            data = json.load(f)
        if "threats" in data and len(data["threats"]) > 0:
            return 1.0
        else:
            return 0.5
    else:
        return 0

def check_reproducibility():
    files = ["ReplET/README.md", "ReplET/LICENSE", "ReplET/reproducibility/environment.yml", "ReplET/reproducibility/CITATION.cff", "ReplET/repl_et_checklist.md"]
    found = sum(os.path.exists(f) for f in files)
    if found == len(files):
        return 1.0
    elif found >= 3:
        return 0.75
    elif found >= 2:
        return 0.5
    elif found >= 1:
        return 0.25
    else:
        return 0

def main():
    scores = {
        "metadata": check_metadata(),
        "participants": check_participants(),
        "equipment": check_equipment(),
        "stimuli": check_stimuli(),
        "aois": check_aois(),
        "data_quality": check_data_quality(),
        "preprocessing": check_preprocessing(),
        "analysis": check_analysis(),
        "threats": check_threats(),
        "reproducibility": check_reproducibility()
    }
    
    # Create temporary output directory
    import tempfile
    import os
    output_dir = tempfile.mkdtemp(prefix="replet_report_")
    
    # Salva JSON
    json_path = os.path.join(output_dir, "report.json")
    with open(json_path, "w") as f:
        json.dump(scores, f, indent=2)
    
    # Enhanced spider graph with better labels and styling
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
    
    # Get criteria in consistent order
    criteria = list(criteria_labels.keys())
    labels = [criteria_labels[c] for c in criteria]
    values = [scores.get(c, 0.0) for c in criteria]
    
    # Close the radar chart
    angles = np.linspace(0, 2*np.pi, len(criteria), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    
    # Calculate overall score for coloring
    overall_score = sum(scores.values()) / len(scores)
    if overall_score >= 0.8:
        color = '#2ecc71'  # Green for excellent
    elif overall_score >= 0.6:
        color = '#f39c12'  # Orange for good
    elif overall_score >= 0.4:
        color = '#e74c3c'  # Red for needs improvement
    else:
        color = '#95a5a6'  # Gray for baseline/template
    
    # Create the spider plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.plot(angles, values, 'o-', linewidth=3, color=color, markersize=8)
    ax.fill(angles, values, alpha=0.25, color=color)
    
    # Customize the chart
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Add title with score
    plt.title(f'ReplET Reproducibility Analysis\n{overall_score*100:.1f}% Overall Score', 
              fontsize=16, fontweight='bold', pad=30)
    
    # Add value labels for non-zero scores
    for angle, value, label in zip(angles[:-1], values[:-1], labels):
        if value > 0.05:  # Only show labels for significant values
            ax.text(angle, value + 0.08, f'{value:.2f}', 
                   ha='center', va='center', fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, edgecolor=color))
    
    plt.tight_layout()
    
    png_path = os.path.join(output_dir, "score.png")
    plt.savefig(png_path)
    
    # Gera report.md
    md_path = os.path.join(output_dir, "report.md")
    with open(md_path, "w") as f:
        f.write("# Repl.ET Replicability Report\n\n")
        for k, v in scores.items():
            f.write(f"- **{k}**: {v}\n")
        f.write(f"\nVeja score.png para o gráfico radar.\n")
    
    # Print location of generated files
    print(f"📊 Reproducibility Report Generated!")
    print(f"📁 Output directory: {output_dir}")
    print(f"📄 JSON report: {json_path}")
    print(f"📈 Radar chart: {png_path}")
    print(f"📝 Markdown report: {md_path}")
    
    # Calculate overall score
    overall_score = sum(scores.values()) / len(scores)
    print(f"\n🏆 Overall Reproducibility Score: {overall_score:.3f}/1.0 ({overall_score*100:.1f}%)")

if __name__ == "__main__":
    main() 