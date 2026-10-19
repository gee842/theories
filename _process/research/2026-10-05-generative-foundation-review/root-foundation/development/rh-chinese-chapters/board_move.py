#!/usr/bin/env python3
"""Move RH's row from the live board to the history file (board rule 4) and add RH to the landed list of the queue
note, in place, for the landing commit. usage (from the repository root): python3 -B board_move.py
RH is docs and records only, so the state names no receipt; the landing commit holds the move, so it names no hash."""
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **RH: the four earlier Chinese chapters after RO** '
STATE = ('landed 2026-10-19, docs and records with no checker run: the 6–7 October texts of the four chapters moved '
         'byte for byte to `theories/becoming/history/` (move batch `RH-chinese-chapters`, receipt '
         '`_process/architecture/moves/RH-chinese-chapters.json`); at each path a live chapter keeps, in current '
         'terms, what the passage map and the spine do not carry, with a table of where each original section went; '
         'the new chapter §9 and §11, the canonical chapter §11 rows, the RO record and study §207 say so; five '
         'records re-pointed after reading (cited text changed only in the rows RH rewrote)')
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
board = board.replace(old, '; RH landed, docs and records with no checker run, ahead of W2' + old)
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, moved)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved the RH row to', HISTORY, 'after line', last + 1)
