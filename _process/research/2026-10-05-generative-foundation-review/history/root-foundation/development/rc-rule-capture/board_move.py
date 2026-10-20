#!/usr/bin/env python3
"""Move RC's row from the live board to the history file (board rule 4), in place, for the landing commit, with a state
cell built from the receipt, the connectivity log and the numbers apply_text.py chose, and name the landing in the
queue note. The row's aside on the reading against the share names `Switching` of `Becoming.Pace` (it said
`Pace.Switching`, a name the package does not have).

usage (from the repository root): python3 -B board_move.py RECEIPT CHECKER_MAIN_SHORT CONN_LOG SECTION DECISION
The landing commit holds the move, so the state names the receipt and record, not the commit's own hash; a board commit
after the landing names the landing and connectivity commits in the queue note."""
import json
import sys
from pathlib import Path

R, MAIN, CONN, N, D = sys.argv[1:6]
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
PREFIX = '| **RC: capture through the rule** '
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = 'research/2026-10-05-generative-foundation-review/root-foundation'
MOD = 'Becoming.RuleCapture'
RID = 'capture-through-the-rule'
receipt = json.loads(Path(f'{PKG}/becoming-checks/{R}/verification.json').read_text())
mod = next(m for m in receipt['modules'] if m['module'] == MOD)
text = Path(CONN).read_text()
conn = json.loads(text[text.index('{'):text.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
total = sum(conn['classes'].values())
assert conn['apart_by_module'].get(MOD) == [1, mod['theorems']], conn['apart_by_module'].get(MOD)
D_ID = f'd{D}-经由规则的捕获之读--the-readings-of-capture-through-the-rule'
state = (f'claimed 2026-10-19; **landed** 2026-10-19: `{MOD}`, {mod["theorems"]} theorems, {len(mod["declarations"])} '
         f'declarations, empty axiom reports, core receipt `{R}` on `{MAIN}` (rule 5); connectivity {apart:,} apart of '
         f'{total:,}, one of them in the module (`Counts.share_not_lower_counts`, registered: it restates `Capture`\'s '
         f'comparison on counts); record [{RID}](../theories/becoming/results/records/{RID}.md), '
         f'[study §{N}]({RF}/BECOMING-RENEWAL-READING.md#{N}-capture-through-the-rule-rc), decision '
         f'[D{D}]({RF}/DELEGATED-CHOICES.md#{D_ID}); checked and sharpened: where no rule turns against the reading the '
         f'share falls at no step from every start and the course locks from the step after its first reading step '
         f'(`favouring_locks`), stronger than proposed; where rules can favour the others the lock needs a start '
         f'condition and fails without it (`locked_stays`, `Alternating.alternates`); a perturbation of the rule is '
         f'absorbed exactly where it keeps the direction (`perturbation_absorbed`, `Reversed.not_absorbed`); under a '
         f'reading favouring at every share every course locks from its second reading step, exactly (`uniform_locks`, '
         f'`Second.second_exact`), so leaving needs a change of how the rule reads or of the selection; "the winner '
         f'shapes the rule" is the premise `ReadsShare`; RO\'s third gap closed, three passages re-pointed (二柄, '
         f'据有余而制不足, 壹赏壹刑壹教), its chapter (§5.7, §8, §11) and record brought up to it, and the scope record of '
         f'the Chinese sources; render, check, strict check, links, test and secrets pass')
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith(PREFIX)]
assert len(rows) == 1, (PREFIX, len(rows))
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = state
OLD = '(`Pace.Switching` is the reading against the share)'
assert cells[0].count(OLD) == 1
cells[0] = cells[0].replace(OLD, '(`Switching` of `Becoming.Pace` is the reading against the share)')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)
board = '\n'.join(lines)
# The queue note's list of landings ends at the first '): W2 ('; RC's landing is appended there.
NOTE = '): W2 ('
assert board.count(NOTE) == 1, board.count(NOTE)
board = board.replace(NOTE, f'; RC landed, core receipt `{R}`, ahead of RG and W2' + NOTE)
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('moved RC row to', HISTORY, 'after line', last + 1)
