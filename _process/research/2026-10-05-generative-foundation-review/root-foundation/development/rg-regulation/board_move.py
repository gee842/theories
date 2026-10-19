#!/usr/bin/env python3
"""Move RG's row from the live board to the history file (board rule 4) and add RG to the landed list of the queue
note, in place, for the landing commit.
usage (from the repository root): python3 -B board_move.py RECEIPT SECTION APART TOTAL
The landing commit holds the move, so the state names the receipt and the study section, not the commit's own hash."""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
receipt, section, apart, total = sys.argv[1:5]
PREFIX = '| **RG: two-sided regulation of a level, and regulation that reads the level late** '
STATE = (f'landed 2026-10-19: core receipt `{receipt}`; one core module (`Becoming.Regulation`), empty axiom reports; '
         'the bound is exactly no overshoot, the least band of a rule reading `ℓ` late is `2 (ℓ + 1) d`, the late '
         'relay\'s threshold is exact; one policy for every start and the lumping left open; connectivity '
         f'{apart} apart of {total}, none in the module; record two-sided-regulation-and-late-reading; '
         f'[study §{section}](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md); '
         'RO\'s four passages, chapter §8 and §11 and record re-pointed')
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
old = '): W2 ('   # the end of the landed list in the queue note, whatever the last landing wrote before it
board = '\n'.join(lines)
assert board.count(old) == 1
board = board.replace(old, f'; RG landed, core receipt `{receipt}`, ahead of W2): W2 (')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist[last + 1:last + 1] = [moved]
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved RG row to', HISTORY, 'after line', last + 1)
