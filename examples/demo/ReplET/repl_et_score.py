import os
import json
import matplotlib.pyplot as plt

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
    # Salva JSON
    with open("ReplET/report.json", "w") as f:
        json.dump(scores, f, indent=2)
    # Gera gráfico radar
    labels = list(scores.keys())
    values = list(scores.values())
    values += values[:1]  # fecha o radar
    angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
    angles += angles[:1]
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticks([0,0.25,0.5,0.75,1.0])
    ax.set_yticklabels(["0","0.25","0.5","0.75","1.0"])
    plt.title("Repl.ET Replicability Radar")
    plt.tight_layout()
    plt.savefig("ReplET/score.png")
    # Gera report.md
    with open("ReplET/report.md", "w") as f:
        f.write("# Repl.ET Replicability Report\n\n")
        for k, v in scores.items():
            f.write(f"- **{k}**: {v}\n")
        f.write("\nVeja score.png para o gráfico radar.\n")

if __name__ == "__main__":
    main() 