#!/usr/bin/env python3
"""Run each package's delta with that package's actual study section, not the batch start."""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
W = Path(sys.argv[1]).resolve()
S = int(sys.argv[2])
for offset, package in enumerate(['becoming-p86-landing', 'becoming-p87-landing', 'becoming-p88-landing']):
    subprocess.run([sys.executable, '-B', str(BASE / package / 'record_delta.py'), str(W), str(S + offset)], check=True)
