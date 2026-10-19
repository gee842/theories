#!/usr/bin/env python3
"""R32: the modules R32 folded go to the Lean history folder with their bytes, by `research.py move`
(plan history-moves.tsv, written here; batch R32-history), as R31's history_move.py did: the pin on
the package's Lean files is lifted for this move only and restored byte for byte after it.

usage: python3 -B history_move.py restore   (puts each folded module's bytes as on main BASE back at its path)
       python3 -B history_move.py move      (with those files committed at their old paths)"""
import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fold  # noqa: E402

ROOT = HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
HIST = 'experiments/integrated-correction/general-framework/generative-basis/lean/history/becoming/Becoming'
BASE = 'ad2efa757'
PLAN = HERE / 'history-moves.tsv'


def base_bytes(name):
    return subprocess.run(['git', 'show', f'{BASE}:{PKG}/Becoming/{name}.lean'], capture_output=True, check=True, cwd=ROOT).stdout


def main():
    if sys.argv[1] == 'restore':
        rows = []
        for x, s in fold.FOLDS:
            data = base_bytes(x)
            path = ROOT / PKG / 'Becoming' / f'{x}.lean'
            assert not path.exists(), path
            assert not (ROOT / HIST / f'{x}.lean').exists(), x
            path.write_bytes(data)
            rows.append(f'{PKG}/Becoming/{x}.lean\t{HIST}/{x}.lean\tR32 (20 October 2026): folded into Becoming.{s} '
                        f'as its final section {x}, declarations and names unchanged; bytes as on main {BASE}')
            print(x, hashlib.sha256(data).hexdigest()[:12])
        PLAN.write_text('\n'.join(rows) + '\n')
        return
    for x, _ in fold.FOLDS:
        path = f'{PKG}/Becoming/{x}.lean'
        assert (ROOT / path).read_bytes() == base_bytes(x), path
    config = ROOT / '_process/research-config.json'
    pinned = config.read_bytes()
    pattern = f'    "{PKG}/Becoming/**",\n'
    assert pinned.decode().count(pattern) == 1
    config.write_text(pinned.decode().replace(pattern, '', 1))
    try:
        subprocess.run([sys.executable, '-B', 'tools/research/research.py', 'move', '--plan', str(PLAN),
                        *sys.argv[2:], '--batch', 'R32-history', '--summary'], check=True, cwd=ROOT)
    finally:
        config.write_bytes(pinned)
    print('pin restored')


if __name__ == '__main__':
    main()
