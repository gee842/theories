#!/usr/bin/env python3
"""R46: the board at landing. The R46 row, rewritten as landed, moves to the history file after the latest landed row
(EV3's); the queue line names R46 as landed and the receipt line names R46's receipt.

usage (from the checkout root): python3 -B board.py BASE RECEIPT_ID SECTION CORE_THEOREMS APART"""
import sys
from pathlib import Path

BASE, RID, SECTION, CORE, APART = sys.argv[1:6]
ROOT = Path(__file__).resolve().parents[6]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HIST = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'

b = BOARD.read_text()
lines = b.split('\n')
rows = [i for i, l in enumerate(lines) if l.startswith("| **R46: interleavings under one renumbering")]
assert len(rows) == 1
del lines[rows[0]]
b = '\n'.join(lines)


def rep(s, old, new):
    assert s.count(old) == 1, old[:80]
    return s.replace(old, new)


b = rep(b, "the latest core receipt is EV4 and EV5's `20261020T094300.398321Z` (20 October 2026).",
        f"the latest core receipt is R46's `{RID}` (20 October 2026).")
b = rep(b, "R46 queued (one renumbering of interleavings; Lean, one checker run)",
        f"R46 landed (core receipt `{RID}`, one renumbering of interleavings, study §{SECTION}, row in the history file)")
BOARD.write_text(b)

row = (
    "| **R46: interleavings under one renumbering, and Reordering's footprints** (R38's open part, study §233). "
    "`Becoming.Interleavings` (now importing `Becoming.Reordering`): for two interleavings of the same courses, every exchange "
    "of each touching some relatum (`Touching`, needed: `Pair.idle_unmatched`), one renumbering of all the steps (`renumber`) "
    "sends each exchange to the same occurrence (`occurrence_matches`, `renumber_exchange`), is each touched relatum's index map "
    "(`renumber_index`), and with the renumbering the other way `Reindexes` the steps below the length, fixing every step from it on "
    "(`renumber_reindexes`, `renumber_beyond`); proved directly, with no adjacent swaps. Through it activity agrees at every relatum "
    "(`world_renumber_active`), levels on what the step's exchange touches (`world_renumber_level`), and every relation read at one step "
    "on those relata, however many (`world_renumber_reads`); levels of untouched relata are not invariant (`Pair.apart_differs`). "
    "Reordering: the renumbering keeps the order of the footprint of the touches (`renumber_keeps`), whose `Contains` holds exactly "
    "where an untouched relatum stays untouched at the next step (`touch_contains_iff`; refuted by `Pair.touch_not_contains`); the "
    "footprint around each step contains the exchanges (`around_contains`) but only the identity keeps its order "
    "(`around_keeps_identity`); `world_renumber_correspondence` gathers the premises of `converse` met. "
    "| Claude Code session of 19–20 October (\"full review\", R24) "
    f"| landed 2026-10-20 on `{BASE}`: core receipt `{RID}` passed (core 275 modules and {CORE} theorems; every axiom report empty); "
    f"connectivity {APART}, register check passes; render, check, links and tests pass; study §{SECTION} "
    "| worktree `.claude/worktrees/agent-ab8dd93899af84e52`, kit `development/r46-one-renumbering/` "
    "| the shared index a reading for whatever is read at one step on what its exchange touches (§0 block A, §8.1 item 1) |")
h = HIST.read_text()
anchor = "| **EV3: the evolution chapter restated from the spine**"
i = h.index(anchor)
j = h.index('\n', i)
assert "R46: interleavings under one renumbering" not in h
h = h[:j + 1] + row + '\n' + h[j + 1:]
HIST.write_text(h)
print('board and history written')
