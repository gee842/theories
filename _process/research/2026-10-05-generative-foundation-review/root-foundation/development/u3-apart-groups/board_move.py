#!/usr/bin/env python3
"""Move U3's and U4's rows from the live board to the history file (board rule 4) and add U3/U4 to the landed list
of the queue note, in place, for the landing commit.
usage (from the repository root): python3 -B board_move.py RECEIPT SECTION APART TOTAL
The landing commit holds the move, so the state names the receipt and the study section, not the commit's own hash."""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
receipt, section, apart, total = sys.argv[1:5]
STATES = {
    '| **U3: theorems apart from the base, largest groups first** ':
        f'landed 2026-10-19: core receipt `{receipt}`; four core modules (`FrontierFrames`, `FrontierWorlds`, '
        '`AcceptanceFrames`, `PresentationFrames`) read the largest apart groups on the base, `Hexagrams` reads the '
        'received pairing through the law, `Listing` counts what takes part in a step; empty axiom reports; '
        f'connectivity {apart} apart of {total}; each remaining group\'s disposition in '
        f'[study §{section}](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md)',
    '| **U4: the practical commitments in the core** ':
        'landed with U3 (2026-10-19): J1–J4 recorded as in the core since F3J (premise card F and glossary corrected, '
        'English and Chinese); the choice at a step calibrated as weak excluded middle '
        '(`FrontierFrames.choice_exists_iff_weakly`); record practical-judgment-g0-j',
}
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
moved = []
for prefix, state in STATES.items():
    rows = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(rows) == 1, (prefix, len(rows))
    row = lines.pop(rows[0])
    cells = row.split(' | ')
    assert len(cells) == 5, len(cells)
    cells[2] = state
    moved.append(' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/'))
old = ', ahead of W2): W2 ('
board = '\n'.join(lines)
assert board.count(old) == 1
board = board.replace(old, f', ahead of W2; U3/U4 landed, core receipt `{receipt}`, ahead of W2): W2 (')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist[last + 1:last + 1] = moved
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved U3 and U4 rows to', HISTORY, 'after line', last + 1)
