#!/usr/bin/env python3
"""R33 (G4): LawThroughCoupling and LawThroughChangingCoupling, whose declarations now sit in
Becoming.LawAlongRun under their names, go to the Lean history folder with their bytes, by
`research.py move` (plan history-moves.tsv, written here; batch R33-history), as R31's and R32's
history_move.py did: the pin on the package's Lean files is lifted for this move only and restored
byte for byte after it.

usage: python3 -B history_move.py plan            (writes history-moves.tsv)
       python3 -B history_move.py move [--apply]  (with the two files as committed at their paths)"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
HIST = 'experiments/integrated-correction/general-framework/generative-basis/lean/history/becoming/Becoming'
BASE = '7950e8798'
PLAN = HERE / 'history-moves.tsv'
MODULES = ['LawThroughCoupling', 'LawThroughChangingCoupling']


def base_bytes(name):
    return subprocess.run(['git', 'show', f'{BASE}:{PKG}/Becoming/{name}.lean'], capture_output=True,
                          check=True, cwd=ROOT).stdout


def main():
    if sys.argv[1] == 'plan':
        rows = []
        for x in MODULES:
            assert not (ROOT / HIST / f'{x}.lean').exists(), x
            rows.append(f'{PKG}/Becoming/{x}.lean\t{HIST}/{x}.lean\tR33 (20 October 2026): joined into '
                        f'Becoming.LawAlongRun (G4, one law along a run), every declaration kept there under '
                        f'its name; bytes as on main {BASE}')
        PLAN.write_text('\n'.join(rows) + '\n')
        return
    for x in MODULES:
        path = f'{PKG}/Becoming/{x}.lean'
        assert (ROOT / path).read_bytes() == base_bytes(x), path
    config = ROOT / '_process/research-config.json'
    pinned = config.read_bytes()
    pattern = f'    "{PKG}/Becoming/**",\n'
    assert pinned.decode().count(pattern) == 1
    config.write_text(pinned.decode().replace(pattern, '', 1))
    try:
        subprocess.run([sys.executable, '-B', 'tools/research/research.py', 'move', '--plan', str(PLAN),
                        *sys.argv[2:], '--batch', 'R33-history', '--summary'], check=True, cwd=ROOT)
    finally:
        config.write_bytes(pinned)
    print('pin restored')


if __name__ == '__main__':
    main()
