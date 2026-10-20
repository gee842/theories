#!/usr/bin/env python3
"""R38: the board at landing. The R38 row, rewritten as landed, moves to the history file after R40's row (R39's and R40's landed while R38 was in the queue);
the queue line and the receipt line name R38's receipt.

usage (from the checkout root): python3 -B board.py BASE RECEIPT_ID"""
import sys
from pathlib import Path

BASE = sys.argv[1]
ROOT = Path(__file__).resolve().parents[6]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HIST = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
RID = sys.argv[2]

b = BOARD.read_text()
lines = b.split('\n')
rows = [i for i, l in enumerate(lines) if l.startswith("| **R38: the open parts of R33's G6 and G10**")]
assert len(rows) == 1
del lines[rows[0]]
b = '\n'.join(lines)


def rep(s, old, new):
    assert s.count(old) == 1, old[:80]
    return s.replace(old, new)


b = rep(b, "the latest core receipt is R40's `20261020T065352.292900Z` (20 October 2026).",
        f"the latest core receipt is R38's `{RID}` (20 October 2026).")
b = rep(b, "- **Queue:** R38 at the head (the open parts of G6 and G10); R40 landed",
        f"- **Queue:** empty; R38 landed (core receipt `{RID}`, the open parts of G6 and G10, study §233, row in the history file); R40 landed")
BOARD.write_text(b)

row = (
    "| **R38: the open parts of R33's G6 and G10** (study §224; Ren, 20 October: \"please\" after the open parts were named). "
    "G6, `Becoming.LoopReturn` (now importing `Becoming.Rejoining`): a strength is what a link gives per unit of the level it reads, "
    "a factor what a return map multiplies a difference by in one turn; around a cycle of links each giving exactly its strength "
    "(`GivesExactly`) one turn is stated exactly (`carried_around_exact`; the excess over the return map's course, `carried_around_excess`), "
    "equal to the course exactly where the loop gains nothing over the turn and the intermediate conditions carry nothing on "
    "(`around_course_iff`); on a ring of two or more conditions the bound is strict (`Ring.bound_strict`, the countermodel to equality); "
    "Rejoining's gap at one condition is a return map's course exactly where the exchanges respond to it (`RespondsByReturn`, `responds_iff`, "
    "`gap_course`, `gap_scaling`), which its witness meets from the act on and not across it (`replenishing_no_return`). "
    "G10, `Becoming.Interleavings`: for any two interleavings of the same courses, an index map for each relatum under which its levels agree "
    "(`indexMap`, `runUpTo_index`, `world_index`) and its exchanges match (`index_matches`), so readings through its own steps are the same "
    "for every interleaving (`world_reads_alike`); proved directly from own counts, not by composing `world_swap`. Open, with blocker: one "
    "renumbering of all the steps, and the correspondence with `Becoming.Reordering`'s footprints (the world's activity is per touched step; "
    "reindexing needs that one renumbering). Every kept statement keeps its type (sigcheck against R40's receipt: 11,428 agree, 0 differ, 51 new). "
    "| Claude Code session of 19–20 October (\"full review\", R24) "
    f"| landed 2026-10-20 on `{BASE}`: core receipt `{RID}` passed (core 268 modules and 10,733 theorems, instances 7 and 567, "
    "applications 6 and 179; every axiom report empty); connectivity 477 of 11,479 apart, register check passes; render, check, links "
    "and tests pass; study §233 "
    "| worktree `.claude/worktrees/agent-aadaebba27a95eb2a`, kit `development/r38-open-joins/` "
    "| the loop law from a gap that is a return map's course under a stated premise (§8.1 item 7); the shared index a reading per relatum "
    "(§0 block A, item 1, K4) |")
h = HIST.read_text()
anchor = "| **R40: the ethics chain is one derivation"
i = h.index(anchor)
j = h.index('\n', i)
assert "R38: the open parts" not in h
h = h[:j + 1] + row + '\n' + h[j + 1:]
HIST.write_text(h)
print('board and history written')
