#!/usr/bin/env python3
"""R37c: the board at landing. The R37c row, rewritten as landed, moves to the history file after LK1's row (the
last landed before it); the queue line and the receipt line name R37c's receipt.

usage (from the checkout root): python3 -B board.py BASE RECEIPT_ID"""
import re
import sys
from pathlib import Path

BASE, RID = sys.argv[1], sys.argv[2]
ROOT = Path(__file__).resolve().parents[7]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HIST = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'

b = BOARD.read_text()
lines = b.split('\n')
rows = [i for i, l in enumerate(lines) if l.startswith('| **R37c: the counted corollaries as compositions**')]
assert len(rows) == 1
del lines[rows[0]]
b = '\n'.join(lines)


def rep(s, old, new):
    assert s.count(old) == 1, old[:80]
    return s.replace(old, new)


b, _n = re.subn(r"the latest core receipt is [^`]*`[0-9T.Z]+` \(20 October 2026\)\.",
                f"the latest core receipt is R37c's `{RID}` (20 October 2026).", b)
assert _n == 1
b = rep(b, " R37c at the head (checker running on R41's main; statements unchanged);", '')
b = rep(b, "- **Queue:** ",
        f"- **Queue:** R37c landed (the counted corollaries as compositions and one tally lemma, statements unchanged; core receipt `{RID}`, study §238, row in the history file); ")
BOARD.write_text(b)

row = (
    "| **R37c: the counted corollaries as compositions** (follow-up to R37b; evidence `development/r37-lens-b/r37b/family/FINDINGS.md`, commit `589ceace5`). "
    "Thirteen counted corollaries of the laws of counting (`counting_binds_iff_counted`, `finite_counting_binds_iff_counted`, the enclosed and finite "
    "change-bound iffs, and the activity, arising and joint iffs in all, finite and enclosed worlds) are now the counted law, the decided law with a "
    "pointwise proof for its property, and the decided corollary, composed; `enclosed_iff_finite_counting_under` and its counted form are read from "
    "one tally lemma, `World.enclosed_iff_finite_tally` (the two tally conditions agree, over any class of properties holding the pointwise ones, "
    "exactly when the selection bounds change and binds counting); `standing_iff_counting_counted` was already a composition. Counting, CensusCounts "
    "and CensusBinding 5,958 → 5,742 lines. Every statement and name kept (sigcheck against R37b's receipt: 11,426 agree, 0 differ, 0 missing; "
    "against R41's: 11,551 agree, 1 new). Study §230's Boundary corrected: a carrier family with fixed activity exists and would save about 60 lines. "
    "| Claude Code session of 20 October (R37c) "
    f"| landed 2026-10-20 on `{BASE}`: core receipt `{RID}` passed (core 269 modules and 10,806 theorems, instances 7 and 567, "
    "applications 6 and 179; every axiom report empty); connectivity 503 of 11,552 apart, register check passes; render, check, links "
    "and tests pass; study §238 "
    "| worktree `.claude/worktrees/agitated-jepsen-b093c6`, kit `development/r37-lens-b/r37c/` "
    "| R37b census table → one proof per corollary (rule 9) |")
h = HIST.read_text()
assert 'R37c: the counted corollaries' not in h
anchor = '| **LK1: relation to known results**'
i = h.index(anchor)
j = h.index('\n', i)
h = h[:j + 1] + row + '\n' + h[j + 1:]
HIST.write_text(h)
print('board and history written')
