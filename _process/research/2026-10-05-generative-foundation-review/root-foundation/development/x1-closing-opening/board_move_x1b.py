#!/usr/bin/env python3
"""Move X1b's row from the live board to the history file (board rule 4) and add X1b to the landed list of the
queue note, in place, for the landing commit.
usage (from the repository root): python3 -B board_move.py
X1b is docs and records only, so the state names no receipt; the landing commit holds the move, so it names no hash."""
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **X1b: the 护闭 texts at the exact scope of the juncture laws** '
STATE = ('landed 2026-10-19, docs and records with no checker run: chapter §1 (the D52 reading) and §10 (the 护闭 row), '
         '[D52](research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md) (2) and the '
         'statement of record every-loss-passes-a-juncture (English and Chinese), and the reading in '
         '[study §199](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md) '
         'say that every loss passes a juncture where s returns (`loss_passes_juncture`) and that keeping is the '
         'largest on its course from s (`keeping_greatest`); records re-pointed after reading (the cited text changed '
         'only in chapter §1 and §10 and study §199)')
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith(PREFIX)]
assert len(rows) == 1, len(rows)
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = STATE
moved = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
board = '\n'.join(lines)
old = '): W2 ('
assert board.count(old) == 1, board.count(old)
board = board.replace(old, '; X1b landed, docs and records with no checker run, ahead of W2' + old)
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, moved)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved the X1b row to', HISTORY, 'after line', last + 1)
