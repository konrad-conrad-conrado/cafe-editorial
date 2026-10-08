import json
from functools import cache
from pathlib import Path

DATA = Path(__file__).parent / 'data'

@cache
def load(name:str):
    with open(DATA/f"{name}.json", encoding="utf-8") as f:
        return json.load(f)
