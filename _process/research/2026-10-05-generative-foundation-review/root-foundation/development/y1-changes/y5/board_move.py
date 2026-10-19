#!/usr/bin/env python3
"""Move Y5's row from the live board to the history file (board rule 4), in place, for the landing commit, with a state
cell built from the receipt, the connectivity log and the numbers apply_text.py chose.

usage (from the repository root): python3 -B board_move.py RECEIPT CHECKER_MAIN_SHORT CONN_LOG SECTION DECISION
The landing commit holds the move, so the state names the receipt and record, not the commit's own hash."""
import json
import sys
from pathlib import Path

R, MAIN, CONN, N, DN = sys.argv[1:6]
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **Y5: what of the arrangements of the 傳 is a law** '
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = 'research/2026-10-05-generative-foundation-review/root-foundation'
MOD = 'Becoming.HexagramSequences'
receipt = json.loads(Path(f'{PKG}/becoming-checks/{R}/verification.json').read_text())
mod = next(m for m in receipt['modules'] if m['module'] == MOD)
text = Path(CONN).read_text()
conn = json.loads(text[text.index('{'):text.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
total = sum(conn['classes'].values())
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]
roots = sum(1 for v in json.loads(Path(f'_process/{RF}/THEOREM-CONNECTIVITY-APART.json').read_text())['roots'].values()
            if v['module'] == MOD)
d = int(DN[1:])
D_ID = f'd{d}-传中诸排列之读--the-readings-of-the-arrangements-of-the-傳'
state = (f'claimed 2026-10-19; **landed** 2026-10-19: `{MOD}`, {mod["theorems"]} theorems, {len(mod["declarations"])} '
         f'declarations, empty axiom reports, core receipt `{R}` on `{MAIN}` (rule 5); connectivity {apart:,} apart of '
         f'{total:,}, {mod_apart} of them in the module, its {roots} roots registered (the 雜卦\'s list and the order\'s '
         f'pairing, the census of the twenty, the opposite stations, two restatements); record '
         f'[hexagram-arrangements-and-laws](../theories/becoming/results/records/hexagram-arrangements-and-laws.md), '
         f'[study §{N}]({RF}/BECOMING-RENEWAL-READING.md#{N}-what-of-the-arrangements-of-the-傳-is-a-law-y5), decision '
         f'[{DN}]({RF}/DELEGATED-CHOICES.md#{D_ID}); the 易传 chapter\'s §8 claim that the order is the orbit of no law '
         f'corrected (the order is the run of a table: every law running it reads every line and keeps no symmetry); '
         f'RO\'s seventh gap closed, nine of its passages re-pointed; the 易传 map 90 passages (2 added), check 10 for '
         f'the 雜卦 and the stations; render, check, strict check, links, test and secrets pass')
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
Path(BOARD).write_text('\n'.join(lines), encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved Y5 row to', HISTORY, 'after line', last + 1)
