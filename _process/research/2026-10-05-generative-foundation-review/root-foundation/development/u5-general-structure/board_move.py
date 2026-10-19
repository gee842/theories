#!/usr/bin/env python3
"""Move U5's row from the live board to the history file (board rule 4) and add U5 to the landed list of the queue
note, in place, for the landing commit.
usage (from the repository root): python3 -B board_move.py RECEIPT SECTION APART TOTAL
The landing commit holds the move, so the state names the receipt and the study section, not the commit's own hash."""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
receipt, section, apart, total = sys.argv[1:5]
PREFIX = '| **U5: the general-structure groups of §196 read on the base** '
STATE = (f'landed 2026-10-19: core receipt `{receipt}`; three core modules (`WitnessRefinementRuns`, `NarrowingRuns`, '
         '`HistoryIdealsTraces`) and `FrontierWorlds` extended state the four general-structure groups of §196 on the '
         'base; empty axiom reports; connectivity '
         f'{apart} apart of {total}, none in the new modules; each group\'s disposition in '
         f'[study §{section}](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md); '
         '`order_paired_by_law` in Y1\'s passage map offered to its owner')
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
old = ', ahead of W2): W2 ('
board = '\n'.join(lines)
assert board.count(old) == 1
board = board.replace(old, f', ahead of W2; U5 landed, core receipt `{receipt}`, ahead of W2): W2 (')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist[last + 1:last + 1] = [moved]
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved U5 row to', HISTORY, 'after line', last + 1)
