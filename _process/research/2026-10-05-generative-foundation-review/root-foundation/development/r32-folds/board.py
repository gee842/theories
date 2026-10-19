#!/usr/bin/env python3
"""R32's landing on the work board (from the checkout root), after R31's board.py: an R32 sub-row to the history
file after R31's, the R28-R36 row's state, the receipt line and the queue line. Idempotent.
usage: python3 -B board.py RECEIPT_ID MAIN_COMMIT RECORDS"""
import sys
from pathlib import Path

RID, MAIN, RECORDS = sys.argv[1:4]
BOARD = Path('_process/BECOMING-WORKBOARD.md')
HIST = Path('_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md')
b = BOARD.read_text()
h = HIST.read_text()
if '| **R32: forwarders, copies and reading modules' in h:
    raise SystemExit('already applied')

lines = b.split('\n')
for row in [l for l in lines if l.startswith('| **R32')]:
    lines.remove(row)
b = '\n'.join(lines)

pairs = [
    ("the latest core receipt is R31's `20261019T213206.644158Z` (20 October 2026).",
     "the latest core receipt is R32's `" + RID + "` (20 October 2026)."),
    ("- **Queue:** R32 at the head (companion modules folded back, forwarders removed, the connectivity measure's new class); "
     "R31 landed (core receipt `20261019T213206.644158Z`).",
     "- **Queue:** empty; R32 landed (core receipt `" + RID + "`); R33 next."),
    ("the copies with another argument order left); R32 next |",
     "the copies with another argument order left); "
     "R32 landed (forwarders, copies and reading modules, core receipt `" + RID + "`, study §223, sub-row in the history file; "
     "the connectivity measure no longer counts a named restatement, 473 of 11,330 apart; 173 forwarders and 61 copies removed, "
     "26 modules folded; twelve copy groups naming definition twins left to B6); R33 next |"),
]
for a, c in pairs:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)

r32 = ('| **R32: forwarders, copies and reading modules** (twentieth review B7(a), B8, B9 remainder, B10, B15, G3). '
       'The connectivity measure stops rewarding restatement: the dump reads pure forwarders off the compiled proofs (a theorem whose whole proof applies another to its own binders, no witness or literal among the arguments), a forwarder on the base records its target\'s instance and no longer counts as using it, the class "instance on the base recorded" (by such a forwarder, the register\'s `instances` list or a Lean example), the class "statement on the base only through a law of its own module" (G3, 172 statements: HexagramLaws, Undecided, Pace, Withholding and others), apart split into general structure by design and the rest; baseline on main\'s tree 481 of 11,566 apart, 50 by design (THEOREM-CONNECTIVITY §11). '
       '173 pure forwarders removed, uses pointed at the law (262 rewrites, 26 hand edits); kept where the chapter, OPENING, the Chinese-sources and 易传 chapters or the RO and Y1 maps cite them (22), where they name a witness (13), or for dot notation or their statement (12). '
       '61 copies removed (B9): 48 where one member lies below the others, 13 by stating twelve prelude-only statements once in `Becoming.Prelude`; two helpers only a removed copy used dropped. '
       '26 reading and small modules folded into the module they read as its final section (PresentationFrames, CensusWebs, MoveRuns, CaptureWorlds, CountdownCourses, DependenceWebs, ExchangeFlows, JointPlanFrames, LevelWebs, ListedOutcomeFrames, OrderWorlds, PassageWorlds, RecurrenceRuns, RetrodictionRuns, CandidateRuns, ReducedRuns, RevisionRuns, StockTraces, TallyWorlds, BoundaryFlows, BoundaryWorlds, DiagonalRuns, TailRuns, Grains, SupportRecovery, AcceptanceFrames), declarations and names unchanged, their files to `lean/history/` with their bytes; layers 3, 256, 19; modules reaching the ethics 20 → 18 (`BoundaryWorlds` now a section of `Boundaries`). '
       'Not done: twelve copy groups whose statement names a definition twin (`Distinct`, `steps`, `total`, `excess`, `nonzero`; B6) and one with a periphery member; reading modules with content of their own, cited by the chapter or the chain, or whose fold would add an import to their source (study §223 lists them). Two checker runs (the second after the docs followed the removals) | '
       'Claude Code session of 20 October (R28–R36 programme) | landed 2026-10-20: core receipt `' + RID + '` on `' + MAIN + '`, passed (279 core modules, 11,330 theorems, 15,621 declarations; 305, 11,566 and 15,857 before; every core axiom report empty; every kept declaration\'s printed type as before and each removed copy\'s as its kept name\'s up to bound names, sigcheck.py); '
       'connectivity 473 apart of 11,330 (49 by design), 92 register instances keep the removed forwarders\' instances, 47 forwarders left; register: seven entries retired, three laws took their entries; '
       + RECORDS + ' records rebound or re-pointed after reading; verify_ro.py and verify_mapping.py pass; study §223; kit `development/r32-folds/`; render, check, links and test pass | '
       'worktree `.claude/worktrees/agent-a008c36a288e70526` | one name per statement, a measure that counts no restatement → R33 (the 172 statements read through their own module\'s law, G6, G7) and B6 (the definition twins) |')
anchor = [l for l in h.split('\n') if l.startswith('| **R31: layers and one prelude')]
assert len(anchor) == 1
h = h.replace(anchor[0], anchor[0] + '\n' + r32)
BOARD.write_text(b)
HIST.write_text(h)
print('board updated')
