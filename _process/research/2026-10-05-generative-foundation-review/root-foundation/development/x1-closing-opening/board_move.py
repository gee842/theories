#!/usr/bin/env python3
"""Move X1's row from the live board to the history file (board rule 4) and add X1 to the landed list of the
queue note, in place, for the landing commit.
usage (from the repository root): python3 -B board_move.py
X1 is docs and records only, so the state names no receipt; the landing commit holds the move, so it names no hash."""
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **X1: the crosswalk of closing and opening** '
STATE = ('landed 2026-10-19, docs and records with no checker run: chapter §10 "Closing and opening: a crosswalk" '
         '(the closure typology and 开 = 未·可·应·转 on landed declarations, 护闭 stated as not yet proved), §1 the '
         '九句 quoted with 归／不归 read as three cases, §8.3 the D49 entry (English and Chinese); '
         '[D49](research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md) (English and '
         'Chinese); four records re-pointed after reading (cited text changed only in §8 and §10); the review '
         'ledger dates reviews written 2026年10月19日 (`stated_date`, with a test)')
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
board = board.replace(old, '; X1 landed, docs and records with no checker run, ahead of W2' + old)
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, moved)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved the X1 row to', HISTORY, 'after line', last + 1)
