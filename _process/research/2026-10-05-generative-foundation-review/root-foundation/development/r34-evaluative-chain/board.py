#!/usr/bin/env python3
"""R34: the board after landing, after R33's board.py. The R34 sub-row goes into the history file after R33's; the
R28-R36 row says R34 landed and R35 next; the queue line and the receipt line name R34's receipt. Each edit is exact
and occurs once. usage: python3 -B board.py LANDED_ON"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HISTORY = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
RID = '20261020T005554.047169Z'
ON = sys.argv[1]

ROW = (
    "| **R34: one evaluative chain** (twentieth review step 5: D2/F13, D3/F7, D6, D7, F9). **D2(a)** the run classes "
    "and widening in `Becoming.Retaining`: `Flow.Balances.includes_of_renewed`, `not_narrows_of_renewed`, "
    "`includes_of_renewingIn` (balance, `Flow.Taking`, every drawn condition renewed over the run: the part does not "
    "narrow) and `narrows_of_consumed` (a consumed dependence the levels without the part meet, the part giving no more "
    "than it takes: it narrows); boundaries `Preemption.renewingAt_consuming_narrows` (within renewal at its step, "
    "consuming over the run, narrowing: the stepwise/run overlap stated exactly) and `Untaken.consuming_keeps` "
    "(consuming alone does not narrow); new record the-run-classes-and-widening; D2 revised [AI reading]: the "
    "formation-level reading dropped from \"generative\". **D2(b)** `Web.paths_one_object` (the condition, significance "
    "and C read one object, admission); `LivingSignificance` moved to `Extension`. **D3/F7** the laws hold for any type "
    "of standpoints; `Web.selfValuation` and six laws in `Boundaries` (own = closure under a relation, `sig` the only "
    "supplied evaluative parameter); `obs` named the second supplied relation. **D7** `Becoming.Direction`: C read as "
    "widening on a web's moves, J1–J4 (`Direction.chosen_keeps_basic`, `kept_required`, `narrowed_not_chosen`), the "
    "pool part (`Direction.widening_selected_by_pool`) and `Clearing.direction`; record alignment-direction-g0-j "
    "retitled, premises without G0, the periphery module an instance by reading. **D6** docs (GrownBy is static "
    "sharing structure over fixed types; no Lean). **F9** Ranking, Relevance and ActiveReading read worlds as webs; "
    "Ranking, ActiveReading and ScoreRepresentation leave L2. Not done: the class of arising over a run; a `World`'s "
    "exchanges as the family of moves (the schema is on a web's moves, not `FrontierWorlds`); the periphery direction "
    "as a formal core instance; widening over a grown world; `Conditions.along` still returns the foundation's "
    "`Unfolding`; how a center forms step by step | Claude Code session of 20 October (R28–R36 programme) | landed "
    "2026-10-20: core receipt `" + RID + "` on `" + ON + "`, passed (278 core modules, 11,401 theorems, 15,713 "
    "declarations; 277, 11,381 and 15,687 before; every core axiom report empty; 7 Lean steps ran, 1,117 reused; "
    "sigcheck.py: 11,360 kept theorems print their type, 21 restated, listed old → new in the study, two removed as "
    "the same statement as a kept one and one definition renamed (kit RENAME-TABLE.json), 22 new); layers 3, 258, 16; "
    "ethics closure 73 → 71; modules reaching Metaethics or Significance 18 → 15; connectivity on `395bfa9e5` 476 "
    "apart of 11,401 (56 by design; 479 of 11,381 before), both families 859 → 876, two register roots retired; one "
    "record new, five extended or rebound, 228 re-pointed after reading; study §225; kit "
    "`development/r34-evaluative-chain/`; render, check, links and test pass | worktree "
    "`.claude/worktrees/agent-a995b9c4663f4d23b` | the chain from the unfolding through the condition (scope) and C "
    "(order) to the direction ends on the spine → R35 (corpus moves), R36 (chapter rewrite) |\n")

h = HISTORY.read_text()
anchor = '| **R33: joins**'
i = h.index(anchor)
j = h.index('\n', i) + 1
if '| **R34: one evaluative chain**' not in h:
    h = h[:j] + ROW + h[j:]
    HISTORY.write_text(h)

b = BOARD.read_text()
SUBS = [
    ("the latest core receipt is R33's `20261019T235844.485705Z` (20 October 2026).",
     f"the latest core receipt is R34's `{RID}` (20 October 2026)."),
    ("- **Queue:** R34 at the head (one evaluative chain: standpoints as formations, `own` as a closure, the direction on "
     "the spine, widening over a grown world, the `Unfolding` sites); R33 landed (core receipt `20261019T235844.485705Z`).",
     f"- **Queue:** empty; R34 landed (core receipt `{RID}`); R35 next."),
    ("G6 around longer cycles left open, 479 of 11,381 apart); R34 next |",
     "G6 around longer cycles left open, 479 of 11,381 apart); R34 landed (one evaluative chain, core receipt `" + RID +
     "`, study §225, sub-row in the history file; the run classes related to widening under named premises with "
     "Preemption and Untaken as boundaries, the condition, significance and C one object of admission, standpoints as "
     "formations with `own` a closure, the direction as a core schema on a web's moves, Ranking, Relevance and "
     "ActiveReading on webs; the class of arising, a World's exchanges as moves, widening over a grown world and "
     "`Conditions.along` left open, 476 of 11,401 apart); R35 next |"),
]
for old, new in SUBS:
    if new in b:
        continue
    assert b.count(old) == 1, old[:60]
    b = b.replace(old, new)
BOARD.write_text(b)
print('board done on', ON)
