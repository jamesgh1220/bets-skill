#!/usr/bin/env python3
"""Batch processor: runs calc_engine for each match in batch_matches.json"""
import json
import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.chdir(project_root)

from scripts.calc_engine import run_ensemble, load_model_config

def main():
    with open("scratch/batch_matches.json", "r", encoding="utf-8") as f:
        matches = json.load(f)
    
    config = load_model_config("models/model-v1.0.json")
    
    all_results = []
    for match in matches:
        result = run_ensemble(match, config)
        result["id"] = match.get("id", "")
        result["league"] = match.get("league", "")
        all_results.append(result)
    
    with open("scratch/batch_output.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    print(f"Procesados {len(all_results)} partidos. Resultados en scratch/batch_output.json")

if __name__ == "__main__":
    main()
