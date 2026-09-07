import json
import subprocess

with open('scratch/analysis_05sep/batch_input.json', 'r') as f:
    data = json.load(f)

results = []
for m in data['matches']:
    with open('scratch/analysis_05sep/temp_match.json', 'w') as tf:
        json.dump(m, tf)
    cmd = ["python3", "scripts/calc_engine.py", "--input", "scratch/analysis_05sep/temp_match.json", "--output", "scratch/analysis_05sep/temp_out.json"]
    subprocess.run(cmd, check=True)
    with open('scratch/analysis_05sep/temp_out.json', 'r') as of:
        out = json.load(of)
        out['league'] = m.get('league', '')
        out['id'] = m['id']
        results.append(out)

with open('scratch/analysis_05sep/batch_results.json', 'w') as rf:
    json.dump(results, rf, indent=2, ensure_ascii=False)

print("Batch processing complete.")
