#!/usr/bin/env python3
"""P58c: Resolution wording for the not-recurring statements; unused binder. Usage: resolution2_p58c.py TREE"""
import sys
from pathlib import Path
p = Path(sys.argv[1]) / 'Becoming/Resolution.lean'; t = p.read_text()
for old, new in [
 ('so taking from a closed family stops (`Flow.taking_not_recurring`)', 'so taking from a closed family does not recur (`Flow.taking_not_recurring`)'),
 ('/-- With the unit fixed from some step on, taking from a closed family stops. -/', '/-- With the unit fixed from some step on, taking from a closed family does not recur. -/'),
 ('on the refinement gives the family nothing, taking from it stops: counted', 'on the refinement gives the family nothing, taking from it does not recur: counted'),
 ('unit: with it fixed, taking from the closed pool stops (`Flow.Balances.taking_not_recurring`). -/', 'unit: with it fixed, taking from the closed pool does not recur\n(`Flow.Balances.taking_not_recurring`). -/'),
 ('/-- Arising at a size not vanishing needs loss in proportion. With loss in proportion it\nstops in every enclosed world', '/-- Arising at a size not vanishing needs loss in proportion. With loss in proportion it\ndoes not recur in every enclosed world'),
 ('what stands stops (`World.exchange_not_recurring`).', 'what stands does not recur (`World.exchange_not_recurring`).'),
 ('closed family stops in every flow balanced at that resolution and dissipative;', 'closed family does not recur in every flow balanced at that resolution and dissipative;'),
 ('every step from `T` on, that the world rests from some step on cannot be refuted. Counted so, balance at a\nrefining unit',
  'every step from `T` on, that the world rests from some step on cannot be refuted. Counted so,\nbalance at a refining unit'),
 ('  fun t later x => match Nat.le.dest later with', '  fun _ later x => match Nat.le.dest later with'),
]:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
p.write_text(t); print('ok')
