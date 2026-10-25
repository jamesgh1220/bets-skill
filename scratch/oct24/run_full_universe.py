import json
import subprocess
import os

with open("scratch/oct24/clubelo.json") as f:
    clubelo = json.load(f)

# Helper for elo
def get_elo(team, default=1500):
    for k, v in clubelo.items():
        if team.lower() in k.lower() or k.lower() in team.lower():
            return v
    return default

print("ClubElo sample:", get_elo("Arsenal"), get_elo("Everton"), get_elo("Chelsea"), get_elo("Dortmund"))

