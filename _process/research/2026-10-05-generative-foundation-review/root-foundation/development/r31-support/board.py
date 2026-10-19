#!/usr/bin/env python3
"""R31's landing on the work board (from the checkout root): an R31 sub-row to the history file after R30's,
the R28-R36 row's state, the receipt line and the queue line. Idempotent.
usage: python3 -B board.py RECEIPT_ID MAIN_COMMIT APART PRELUDE_ONLY RECORDS"""
import sys
from pathlib import Path

RID, MAIN, APART, PRELUDE, RECORDS = sys.argv[1:6]
BOARD = Path('_process/BECOMING-WORKBOARD.md')
HIST = Path('_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md')
b = BOARD.read_text()
h = HIST.read_text()
if '| **R31: layers and one prelude' in h:
    raise SystemExit('already applied')

lines = b.split('\n')
for row in [l for l in lines if l.startswith('| **R31')]:
    lines.remove(row)
b = '\n'.join(lines)

pairs = [
    ("the latest core receipt is R30's `20261019T194851.524223Z` (20 October 2026).",
     "the latest core receipt is R31's `" + RID + "` (20 October 2026)."),
    ("- **Queue:** R31 at the head of the queue (the twentieth review's support and layers), built and checked on its branch; its lander fast-forwards main (rule 5).",
     "- **Queue:** empty; R31 landed (core receipt `" + RID + "`); R32 next."),
    ("the 28 `Unfolding` sites left for R34); R31 next |",
     "the 28 `Unfolding` sites left for R34); "
     "R31 landed (layers and one prelude, core receipt `" + RID + "`, study §222, sub-row in the history file; "
     "the ethics closure 138 → 20 modules; four modules reaching it without the condition, the B6 definition twins and "
     "the copies with another argument order left); R32 next |"),
]
for a, c in pairs:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)

r31 = ('| **R31: layers and one prelude** (twentieth review A4, A5, A7, A9, A12, B6, B12, B15, G15). '
       'The conditional theorems out of the general import closure: what takes no condition in Significance, Regions, Continuation, Interdependence, Feedback and ValuationFrames to `Becoming.Retaining`, `Becoming.Clearing` (the witness in one low module) and `Becoming.Extension`, the theorems where bounded significance meets the condition to `Becoming.BoundedSignificance`; '
       'modules reaching `Metaethics` or `Significance` 138 of 298 → 20 of 304 (16 naming the condition or a valuation; `ActiveReading`, `BoundaryWorlds`, `Ranking`, `ScoreRepresentation` reach it without). '
       'One law module `Becoming.Laws` after the frame (`Determined`, the laws of change and partial laws, `GoAlikeUnder`, `GoAlike` as its case at equality), names unchanged. '
       'One prelude `Becoming.Prelude` (imports only Init): Naturals, ListTests, the arithmetic of Dependence and OneStep, the Bool, Option and list lemmas; 111 copies removed by `dedup-table.json` (59 groups), every use pointed to the kept name; Integers and IntegerOrder kept; no name OPENING, the chapter or the RO and Y1 maps cite removed. '
       '`Becoming.Order` split into `Stuttering`, `Reordering`, `IdleRemoval`; Order.lean, Naturals.lean and ListTests.lean to `lean/history/` with their bytes. '
       'Layers computed (`layers.py`: L0 World, Frame, Prelude; L2 what names `Unrestricted` or `Valuation` and what imports it; L1 the rest; 3, 280, 21), no module imports a higher layer; the README tables, the notes in Becoming.lean and the Chinese chapter\'s table follow them; §9 points to the generated table. '
       'Not done: the B6 definition twins and the copies with another argument order (kept as names), seven copies differing in universe level only removed (`Learnable.length_map`\'s polymorphic form no longer stated), FallibleInquiry not moved (its own checker and receipts), TransmissionCorrespondence\'s `import Becoming.Order` left to its checker. Five checker runs (the first failed on a missing `end`, the second found a binder order changed, the next two docs and root imports) | '
       'Claude Code session of 20 October (R28–R36 programme) | landed 2026-10-20: core receipt `' + RID + '` on `' + MAIN + '`, passed (305 core modules, 11,566 theorems, 15,857 declarations; 11,658 and 15,949 before; every core axiom report empty; every kept declaration\'s printed type as before, sigcheck.py); '
       'connectivity ' + APART + ' apart of 11,566 (' + PRELUDE + ' prelude-only; 489 and 43 before), World → Process true; register: two entries retired, one root added; '
       + RECORDS + ' records rebound or re-pointed after reading; verify_ro.py and verify_mapping.py pass; study §222; kit `development/r31-support/`; render, check, links and test pass | '
       'worktree `.claude/worktrees/agent-a45bbb5e24b08ca44` | the prelude, the three-layer table, the companion modules → R32 (companion modules folded back, forwarders, the connectivity class) and R34 (the four modules reaching the ethics) |')
anchor = [l for l in h.split('\n') if l.startswith('| **R30: one notion, one name')]
assert len(anchor) == 1
h = h.replace(anchor[0], anchor[0] + '\n' + r31)
BOARD.write_text(b)
HIST.write_text(h)
print('board updated')
