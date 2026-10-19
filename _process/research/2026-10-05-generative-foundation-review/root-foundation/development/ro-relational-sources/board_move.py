#!/usr/bin/env python3
"""Move RO's row from the live board to the history file (board rule 4), in place, for the landing commit, and name the
landing in the queue note. usage (from the repository root): python3 -B board_move.py STATE
  STATE  the new state cell, written with links relative to the live board (they are re-rooted for the history file)
The landing commit holds the move, so the state names the study section and record, not the commit's own hash."""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **RO: the relational ontology of the Chinese sources, mapped onto the spine** '
state = sys.argv[1]
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith(PREFIX)]
assert len(rows) == 1, (PREFIX, len(rows))
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = state
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
# The queue note's list of landings ends at the first '): W2'; RO's landing is appended there.
NOTE = '): W2 ('
assert board.count(NOTE) == 1, board.count(NOTE)
board = board.replace(NOTE, '; RO landed, docs and records with no checker run, ahead of W2' + NOTE)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved RO row to', HISTORY, 'after line', last + 1)
