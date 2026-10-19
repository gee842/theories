#!/usr/bin/env python3
"""R31 (one-shot): Order.lean, Naturals.lean and ListTests.lean, whose content R31 split or moved into other core
modules, go to the Lean history folder with their bytes, by `research.py move` (plan history-moves.tsv, batch
R31-history). The package's Lean files are pinned against moves, since a live module's path is its name; these
three are no longer modules of the run, so the pin is lifted for this move only and restored byte for byte after
it, as the F3 sweep did (development/bridge-fold/sweep_apply.py).

usage: python3 -B history_move.py   (from the checkout root, with the three files committed at their old paths)"""
import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
BASE = '5c55b36f4'
for name in ('Order', 'Naturals', 'ListTests'):
    path = f'{PKG}/Becoming/{name}.lean'
    base = subprocess.run(['git', 'show', f'{BASE}:{path}'], capture_output=True, check=True, cwd=ROOT).stdout
    assert (ROOT / path).read_bytes() == base, path
    print(name, hashlib.sha256(base).hexdigest()[:12])
config = ROOT / '_process/research-config.json'
pinned = config.read_bytes()
pattern = f'    "{PKG}/Becoming/**",\n'
assert pinned.decode().count(pattern) == 1
config.write_text(pinned.decode().replace(pattern, '', 1))
try:
    subprocess.run([sys.executable, '-B', 'tools/research/research.py', 'move', '--plan', str(HERE / 'history-moves.tsv'),
                    '--apply', '--batch', 'R31-history', '--summary'], check=True, cwd=ROOT)
finally:
    config.write_bytes(pinned)
print('moved; pin restored')
