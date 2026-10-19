#!/usr/bin/env python3
"""Move SC's row from the live board to the history file (board rule 4), in place, for the landing commit, with a state
cell built from the receipt, the connectivity log and the numbers apply_text.py chose, and name the landing in the
queue note.

usage (from the repository root): python3 -B board_move.py RECEIPT CHECKER_MAIN_SHORT CONN_LOG SECTION DECISION
The landing commit holds the move, so the state names the receipt and record, not the commit's own hash; a board commit
after the landing names the landing and connectivity commits in the queue note."""
import json
import sys
from pathlib import Path

R, MAIN, CONN, N, DN = sys.argv[1:6]
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **SC: a code formed between formations** '
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = 'research/2026-10-05-generative-foundation-review/root-foundation'
MOD = 'Becoming.SharedCodes'
RID = 'a-code-formed-between-formations'
receipt = json.loads(Path(f'{PKG}/becoming-checks/{R}/verification.json').read_text())
mod = next(m for m in receipt['modules'] if m['module'] == MOD)
text = Path(CONN).read_text()
conn = json.loads(text[text.index('{'):text.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
total = sum(conn['classes'].values())
assert conn['apart_by_module'].get(MOD, [0])[0] == 0, conn['apart_by_module'].get(MOD)
d = int(DN[1:])
D_ID = f'd{d}-在形成之间形成的编码--a-code-formed-between-formations'
state = (f'claimed 2026-10-19; **landed** 2026-10-19: `{MOD}`, {mod["theorems"]} theorems, {len(mod["declarations"])} '
         f'declarations, empty axiom reports, core receipt `{R}` on `{MAIN}` (rule 5); connectivity {apart:,} apart of '
         f'{total:,}, none of them in the module; record [{RID}](../theories/becoming/results/records/{RID}.md), '
         f'[study §{N}]({RF}/BECOMING-RENEWAL-READING.md#{N}-a-code-formed-between-formations-sc), decision '
         f'[{DN}]({RF}/DELEGATED-CHOICES.md#{D_ID}); all six proposed points hold, several sharpened (agreement is kept '
         f'exactly through hearings closed on it; an order forms agreement from every start exactly where it gives every '
         f'formation one origin); beyond them, agreement needs a broken symmetry (`never_agrees_of_both`), the '
         f'coupling-closure form proposed for 名无固宜 is false (`Path.never_agree`; a pointer law agrees exactly where '
         f'its paths meet), and where records are only added a resolution is lost but never replaced '
         f'(`added_never_replaced`); RO\'s second gap closed, four of its passages re-pointed (同则同之, 名无固宜, the '
         f'說文\'s 止戈 gloss, 书同文), its chapter (§5.4, §8, §11) and record brought up to it; render, check, strict '
         f'check, links, test and secrets pass')
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
# The queue note's list of landings ends at the first '): W2 ('; SC's landing is appended there.
NOTE = '): W2 ('
assert board.count(NOTE) == 1, board.count(NOTE)
board = board.replace(NOTE, f'; SC landed, core receipt `{R}`, ahead of W2' + NOTE)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved SC row to', HISTORY, 'after line', last + 1)
