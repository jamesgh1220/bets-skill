#!/usr/bin/env python3
"""Batch runner: procesa cada partido del batch_input.json a través de calc_engine.py."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from scripts.calc_engine import run_ensemble, load_model_config

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'batch_input.json')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'batch_results.json')
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'model-v1.2.json')

def main():
    with open(INPUT_PATH, 'r', encoding='utf-8') as f:
        matches = json.load(f)
    model_config = load_model_config(CONFIG_PATH)
    results = []
    for match in matches:
        result = run_ensemble(match, model_config)
        result['league'] = match.get('league', '')
        results.append(result)
        print(f"✓ {result['match']} ({result['league']})")
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n{len(results)} partidos procesados → {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
