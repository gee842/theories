#!/usr/bin/env python3
"""R33: the board after landing. The R33 sub-row goes into the history file after R32's; the R28-R36 row says
R33 landed and R34 next; the queue line and the receipt line name R33's receipt. Each edit is exact and occurs
once. usage: python3 -B board.py LANDED_ON"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HISTORY = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
RID = '20261019T235844.485705Z'
ON = sys.argv[1]

ROW = (
    "| **R33: joins** (twentieth review G4, G5, G6, G7, G10). **G4** one law along a run: `Becoming.LawThroughCoupling` "
    "and `Becoming.LawThroughChangingCoupling` joined into `Becoming.LawAlongRun` with every declaration under its name, "
    "their files to `lean/history/` with their bytes (`research.py move`, batch R33-history); the law is "
    "`Run.law_under_iff` (under an equivalence), `Run.law_through_iff` proved from it, the changing coupling "
    "(`Run.law_through_dependence_iff`) and the fixed conditions (`Run.law_through_coupling_iff`) its instances; "
    "`exact_law_iff` stays beside it as exactness; one record, a-law-through-a-projection-along-one-run retitled \"A law "
    "along one run, under a relation\", the other two superseded with their IDs. **G5** learning through a map is "
    "tracking in the limit: `Limit.Tracks`, `Limit.identifies_iff_tracks`, `LearnableRuns.predicts_iff_tracks`, "
    "`tracks_of_learnable`, `learnable_iff_tracks` (in a world a list holds), `learnable_iff_identifies` (with the "
    "feature invariant along the law) and the countermodel `Merge.learnable_not_identifies`; `LearningRuns."
    "pair_first_not_rests`/`pair_whole_rests` renamed `…_predicts` (R30 had renamed `Rests`; the candidate-rest family "
    "of Seeking keeps its names). **G6** one loop theory: `LoopReturn.strength` → `factor`, `whole_strengths` → "
    "`whole_factors`; `geomBound_eq_course`, `selfLoop_carried`, `selfLoop_gap`, `carried_around_course` (a lower bound "
    "around a cycle of several conditions); the chapter's §4 rows cite the join. **G7** collective laws on webs: "
    "`Tolerance.web_tolerating`, `web_activity_tolerating`, `giftWeb_tolerating`, `web_answers` (k = all, "
    "`Withholding.answers`), no new import, the ethics closure unchanged (73). **G10** interleavings build the World "
    "(partial): `Interleavings.LocalLaw.world`, `world_balances`, `standings_of_courses`, `standings_of_interleavings`, "
    "`world_final`, `world_swap`, `world_swap_between`. Not done: G10's step-by-step relation between the worlds of "
    "interleavings differing by more than one adjacent swap (blocker: the world-level `run_move` composed along "
    "`split_heads`); G5's converse without a list (a run per prefix); G6's equality around a cycle of several "
    "conditions and the Rejoining reading; G3's own-module class not closed (172 → 176) | Claude Code session of 20 "
    "October (R28–R36 programme) | landed 2026-10-20: core receipt `" + RID + "` on `ada4b87f1`, passed (277 core "
    "modules, 11,381 theorems, 15,687 declarations; 279, 11,330 and 15,621 before; every core axiom report empty; "
    "84 Lean steps ran, 1,036 reused; every kept declaration's printed type as before, three under the names of the "
    "rename table, 51 new, sigcheck.py); layers 3, 254, 19; connectivity on `3d1ae727b` 479 apart of 11,381 (56 by "
    "design; 473 of 11,330 before), both families 850 → 859, pure forwarders 47 → 50; register: "
    "`standings_of_interleavings` added as general structure, `Naturals.add_le_of_le_sub` retired; two records new, two "
    "extended, two superseded, 208 re-pointed after reading; study §224; kit `development/r33-joins/`; render, check, "
    "links and test pass | worktree `.claude/worktrees/agent-a70a138f3410a197e` | one law along a run, learning in "
    "Limit's vocabulary → R34 (the evaluative chain); the open G10 relation → the necessity target's shared index |\n")

h = HISTORY.read_text()
anchor = '| **R32: forwarders, copies and reading modules**'
i = h.index(anchor)
j = h.index('\n', i) + 1
if '| **R33: joins**' not in h:
    h = h[:j] + ROW + h[j:]
    HISTORY.write_text(h)

b = BOARD.read_text()
SUBS = [
    ("the latest core receipt is R32's `20261019T231053.882924Z` (20 October 2026).",
     f"the latest core receipt is R33's `{RID}` (20 October 2026)."),
    ("- **Queue:** R33 at the head (frontier joins: one law along a run, learning in the limit, loops, collective laws on "
     "webs, interleavings building the world); R32 landed (core receipt `20261019T231053.882924Z`).",
     f"- **Queue:** empty; R33 landed (core receipt `{RID}`); R34 next."),
    ("twelve copy groups naming definition twins left to B6); R33 next |",
     "twelve copy groups naming definition twins left to B6); R33 landed (joins, core receipt `" + RID + "`, study "
     "§224, sub-row in the history file; one law along a run in LawAlongRun, learning through a map as tracking, the "
     "self-loop's return map as the carried amount, the tolerance law on webs, the World an interleaving builds; G10's "
     "general step-by-step relation, G5's converse without a list and G6 around longer cycles left open, 479 of 11,381 "
     "apart); R34 next |"),
]
for old, new in SUBS:
    if new in b:
        continue
    assert b.count(old) == 1, old[:60]
    b = b.replace(old, new)
BOARD.write_text(b)
print('board done on', ON)
