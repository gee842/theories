#!/usr/bin/env python3
"""R28's landing on the work board (from the checkout root): S4's row and an R28 sub-row to the history file,
the R28-R36 row's state, the receipt line and the queue line. Idempotent."""
from pathlib import Path

RID = '20261019T181519.226999Z'
BOARD = Path('_process/BECOMING-WORKBOARD.md')
HIST = Path('_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md')
b = BOARD.read_text()
h = HIST.read_text()
if '| **R28: one base by definition' in h:
    raise SystemExit('already applied')

lines = b.split('\n')
s4 = [l for l in lines if l.startswith('| **S4: scratch feasibility of "one base"**')]
assert len(s4) == 1
s4row = s4[0]
lines.remove(s4row)
old = 'Awaits the integrator\'s decision on step 4; the row goes to history when that is taken or the claim lapses |'
assert old in s4row
s4row = s4row.replace(old, 'Taken by R28 (run root), which landed on 20 October 2026 with core receipt `' + RID + '`; the row moved to history in R28\'s landing commit |')
b = '\n'.join(lines)

pairs = [
    ("the latest core receipt is R27's `20261019T174929.247241Z` (19 October 2026).",
     "the latest core receipt is R28's `" + RID + "` (20 October 2026)."),
    ("- **Queue:** empty; R25 landed (docs only; see the landing queue below).",
     "- **Queue:** empty; R28 landed (core receipt `" + RID + "`); R29 next."),
    ("| claimed 2026-10-20 on `2b80b5500`; R28 next |",
     "| claimed 2026-10-20 on `2b80b5500`; R28 landed (one base by definition, core receipt `" + RID + "`, study §219, sub-row in the history file); R29 next |"),
]
for a, c in pairs:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)

r28 = ('| **R28: one base by definition, the run** (twentieth review step 4, definitional part; S4\'s run root). `structure Dependence` in `Becoming.World` and `Web F C := Dependence Nat F C`; '
       '`World` one kind of relatum with its history, a `Run` of `everyStep (WebAt R) (Exchange R)`, read by `World.web`, `World.flow`, `World.move`, built by `World.of` (`World.of_web`, `World.of_flow` by `rfl`); '
       '`Becoming.World` and `Becoming.Recurrence` import the frame; `Law.Lossless/Merges/Returns/Reachable/KeepsPossibilities` abbreviations at `Law.process next` with five unfolding lemmas, the `Branching.law_*_iff` bridges `Iff.rfl`; '
       '`World.run_history`. Docstrings (World, Runs, Recurrence, Labelled, Branching, fifteen "does not import the frame" clauses), `Becoming.lean`, package README (en, zh), checker `SCOPE` text, chapter §1/§8.1/§9 and the Chinese edition. One checker run | '
       'Claude Code session of 20 October (R28–R36 programme) | landed 2026-10-20: core receipt `' + RID + '` on `4c40745f8`, passed (298 core modules, 11,684 theorems, eight more, no statement\'s meaning changed; every core axiom report empty); '
       'connectivity on the same sources: `families_reach_each_other` World → Process true (Flow, Web, Process → World false), 870 statements on both families, 485 apart of 11,684 (495 of 11,676 before), four apart roots retired to the kit; '
       '193 records rebound or re-pointed after reading, 21 of them with moved declarations re-homed, `worlds-are-runs` advanced; study §219; kit `development/r28-one-base/`; render, check, links and test pass | '
       'worktree `.claude/worktrees/agent-ab333e386f6f59ce1` | World, Runs, Recurrence, Branching, Labelled, Dependence and the modules building worlds or reading orbit forms → records `worlds-are-runs`, `recurrence-without-premise`, chapter §1, §8.1, §9 |')
anchor = [l for l in h.split('\n') if l.startswith('| **R25: the twentieth review\'s step 1, docs now**')]
assert len(anchor) == 1
h = h.replace(anchor[0], anchor[0] + '\n' + s4row + '\n' + r28)
BOARD.write_text(b)
HIST.write_text(h)
print('board updated')
