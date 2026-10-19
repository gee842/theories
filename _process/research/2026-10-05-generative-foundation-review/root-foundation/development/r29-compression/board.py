#!/usr/bin/env python3
"""R29's landing on the work board (from the checkout root): an R29 sub-row to the history file after R28's,
the R28-R36 row's state, the receipt line and the queue line. Idempotent."""
from pathlib import Path

RID = '20261019T185632.962707Z'
BOARD = Path('_process/BECOMING-WORKBOARD.md')
HIST = Path('_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md')
b = BOARD.read_text()
h = HIST.read_text()
if '| **R29: compression under rule 9' in h:
    raise SystemExit('already applied')

# A sub-row of R29 on the board, if a session added one, goes to history with the landing.
lines = b.split('\n')
for row in [l for l in lines if l.startswith('| **R29')]:
    lines.remove(row)
b = '\n'.join(lines)

pairs = [
    ("the latest core receipt is R28's `20261019T181519.226999Z` (20 October 2026).",
     "the latest core receipt is R29's `" + RID + "` (20 October 2026)."),
    ("- **Queue:** R29 at the head of the queue (the twentieth review's compression under rule 9), built and checked on its branch; its lander fast-forwards main (rule 5).",
     "- **Queue:** empty; R29 landed (core receipt `" + RID + "`); R30 next."),
    ("R28 landed (one base by definition, core receipt `20261019T181519.226999Z`, study §219, sub-row in the history file); R29 next |",
     "R28 landed (one base by definition, core receipt `20261019T181519.226999Z`, study §219, sub-row in the history file); "
     "R29 landed (compression under rule 9, core receipt `" + RID + "`, study §220, sub-row in the history file; G8's counted → decided counting not done, left to B11's census table, study §220); R30 next |"),
]
for a, c in pairs:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)

r29 = ('| **R29: compression under rule 9, generalize below, not beside** (twentieth review B1, B3, B9, B10, G2, G8). '
       'The laws of every process that `Law.*` restated (Branching\'s `Merges.not_lossless`, `Reachable.earlier`, `lost_stays`, `Returns.reachable`, `Lossless.returns` and others), `Law.run`, `Law.run_state` and `Run.onward` move into `Becoming.Recurrence`; '
       'the `Law.*` forms are their one-line cases at the law\'s run or are removed (`Law.Merges.not_lossless`, `Law.Reachable.earlier`, `Law.Returns.reachable`). '
       '`Becoming.Amounts` (new, imports only `Naturals`) below the rest family, which Renewal, Space, Dissipation and Openness prove as its whole-number instance; LeastLoss\'s six `_whole` re-proofs removed, its countermodels kept. '
       'The pool closure in `Becoming.Selection`, `Flow.unselected_beyond_coupling_all` proved at the singleton pool. One name per statement for the B9 pairs (17 second names removed). `Readout.image` removed for `Image`. '
       'Not done: counted → decided counting (G8): only the forward directions could follow, the converses need the witnesses; left to B11. One checker run | '
       'Claude Code session of 20 October (R28–R36 programme) | landed 2026-10-20: core receipt `' + RID + '` on `87ecfdee5`, passed (299 core modules, 11,658 theorems, 26 fewer, no kept statement changed; every core axiom report empty); '
       'connectivity on the same sources: families unchanged (World → Process true), 866 statements on both families, 489 apart of 11,658 (485 of 11,684 before), two register entries retired to the kit and four apart roots registered; '
       '204 records rebound or re-pointed after reading, 25 of them with moved or replaced declarations; study §220; kit `development/r29-compression/`; render, check, links and test pass | '
       'worktree `.claude/worktrees/agent-ae45fd9075b02ccd6` | Recurrence, Branching, Labelled, Amounts, LeastLoss, Renewal, Space, Dissipation, Openness, Selection, SelectionPool, Readout and the B9 modules → records `least-loss-rest`, `what-pooled-coupling-reaches`, `recurrence-without-premise`, chapter §9 |')
anchor = [l for l in h.split('\n') if l.startswith('| **R28: one base by definition, the run**')]
assert len(anchor) == 1
h = h.replace(anchor[0], anchor[0] + '\n' + r29)
BOARD.write_text(b)
HIST.write_text(h)
print('board updated')
