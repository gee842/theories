#!/usr/bin/env python3
"""A4-L landed (19 October 2026): record the landing in A4-L's row, move the row from the live board to the history
file (board rule 4) with its links re-rooted, and take A4-L out of the queue. Each edit must match exactly once.
usage (from the repository root): python3 -B board_land.py LANDING_COMMIT CORE_RECEIPT CORR_RECEIPT SECTION APART"""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
COMMIT, RECEIPT, CORR, SECTION, APART = sys.argv[1:6]
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **A4-L: the family of ideals in the core** ')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
assert cells[2].startswith('claimed 2026-10-19; core modules `Becoming.Ideals`'), cells[2][:80]
cells[2] = (f'claimed 2026-10-19; landed 19 October 2026 as `{COMMIT}`, core receipt `{RECEIPT}`: `Becoming.Ideals` '
            '(99 theorems: ideals of an order of stretches, refutable and closed classes with the two double-negation '
            'calibrations, the hull, avoidance, a lower set\'s order, the completion and its readings) and '
            '`Becoming.HistoryIdeals` (80: runs as the ideals of their stretches; each law of ideals read on the '
            'histories of a process in `Stretches`, with Horizon\'s laws derived as the case of runs, adhering as the '
            'least closed class, the calibrations asked of every process, the completion at runs and the classification '
            'for every process with settling ⇔ LPO; words, histories and classes of histories), every axiom report '
            'empty; `IdealsCorrespondence` (92 theorems, 40 of 103 declarations with empty reports) checked by '
            f'`check_ideals_correspondence.py`, receipt `{CORR}`; record `a-history-read-off-its-finite-stretches`, '
            f'study §{SECTION}. Connectivity: the first build stood apart (115 of 139 theorems), so each law was read '
            f'on the histories of a process; at the landing rerun {APART} of the spine stand apart, 25 of them in the '
            'two modules, their 18 roots registered. The board row\'s earlier count of 41 empty correspondence '
            'reports was a miscount; the checker\'s list has 40')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
start = board.index('): A4-L (Claude Code session of 18 October, the family of ideals in the core')
assert board.count('): A4-L (Claude Code session of 18 October, the family of ideals in the core') == 1
end = board.index('Then W2 (', start)
board = board[:start] + f'; A4-L landed as `{COMMIT}`, core receipt `{RECEIPT}`): ' + board[end + len('Then '):]
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('A4-L row moved after history line', last + 1, '; queue updated')
