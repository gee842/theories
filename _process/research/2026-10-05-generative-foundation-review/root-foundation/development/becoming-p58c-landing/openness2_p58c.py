#!/usr/bin/env python3
"""P58c, Openness second pass: module docstring, exchange, hatch, Few. Usage: openness2_p58c.py FILE"""
import sys
from pathlib import Path
p = Path(sys.argv[1]); t = p.read_text()


def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)


once('''or act, and the flow too comes to rest (`World.exchange_stops`).''',
     '''or act, and the exchange does not recur either (`World.exchange_not_recurring`).''')
once('''* **Standing comes to rest.** So where every step from some step on is enclosed around
  what stands, no condition's standing changes at arbitrarily late steps
  (`Flow.stills`).
* **The exchange comes to rest.** Across such a step,''',
'''* **Standing stops changing, unrefuted.** So where every step from some step on is enclosed
  around what stands, that no condition's standing changes from some step on cannot be refuted
  (`Flow.change_stops_unrefuted_around`), and change does not recur
  (`Flow.change_not_recurring_from`).
* **The exchange does not recur.** Across such a step,''')
once('''  gives at arbitrarily late steps (`Flow.exchanges_finitely`, `World.exchange_stops`),''',
     '''  gives at arbitrarily late steps (`Flow.exchange_not_recurring`, `World.exchange_not_recurring`),''')
once('''* **The rest theorem.** Where what stands is listed, whatever arises is embodied, the
  flow balances and dissipates, and every step from some step on is enclosed around what
  stands, arising stops, since standing stops changing (`World.arising_stops`); more, that
  it stops from some step on cannot be refuted even where the flow is only not refuted to run
  down: it is not the case that after every step from then on a later arising stays
  unrefuted (`World.arising_stops_unrefuted_from`, from `Flow.change_stops_unrefuted`). With a
  census of what is active as well, ceasing stops too: the world comes to rest
  (`World.comes_to_rest`). No decision
  procedure is used, and of the census only that it covers what is active: under a covering
  list, ceasing recurring leaves a later arising unrefuted after every step
  (`Covers.not_not_coming_from`), which the unrefuted stopping refutes (`World.comes_to_rest_from`).''',
'''* **The rest theorem.** Where what stands is listed, whatever arises is embodied, the
  flow balances and dissipates, and every step from some step on is enclosed around what
  stands, that arising stops from some step on cannot be refuted, since standing stops
  changing (`World.arising_stops_unrefuted`); so too where the flow is only not refuted to run
  down (`World.arising_stops_unrefuted_from`, from `Flow.change_stops_unrefuted`). With a
  census of what is active as well, that the world rests from some step on cannot be refuted
  (`World.comes_to_rest_unrefuted`, `World.RestsFrom`), so neither arising nor ceasing recurs
  (`World.not_recurring_of_rests_unrefuted`). No decision procedure is used, and of the census
  only that it covers what is active: under a covering list, ceasing left unrefuted after every
  step leaves a later arising unrefuted after every step (`Covers.not_not_coming_from`), which
  the unrefuted stopping of arising refutes (`World.comes_to_rest_unrefuted_from`). Naming the
  step is a principle of omniscience (`World.lpo_of_finite_ends`).''')
once('''  (`World.Finite.comes_to_rest`), its relata covering whatever is active.''',
     '''  (`World.Finite.comes_to_rest_unrefuted`), its relata covering whatever is active.''')
once('''  active lists what stands (`World.rests_around`), and enclosure from some step on''',
     '''  active lists what stands (`World.rests_unrefuted_around`), and enclosure from some step on''')
once('''  what stands, and the totals compared are numbers (`World.rests_enclosed`). Read the''',
     '''  what stands, and the totals compared are numbers (`World.rests_unrefuted_enclosed`). Read the''')
once('''  changes, though the world is not finite (`World.hatch_rests`).''',
     '''  changes, though the world is not finite (`World.hatch_rests_unrefuted`).''')
once('''/-- Coming to hold happens at most once. -/
theorem quiet : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (passed s a) t :=''',
     '''/-- Coming to hold does not recur: it happens at most once. -/
theorem coming_not_recurring : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (passed s a) t :=''')
once('''      (Few.quiet s) with''', '''      (Few.coming_not_recurring s) with''')
once('''/-- In such a world the exchange comes to rest as well: no relatum takes or gives at
arbitrarily late steps (`Flow.exchanges_finitely`). This needs only the census of what
stands, balance, dissipation and enclosure, not a census of activity or embodiment. -/
theorem exchange_stops {stand''',
     '''/-- In such a world the exchange does not recur either: no relatum takes or gives at
arbitrarily late steps (`Flow.exchange_not_recurring`). This needs only the census of what
stands, balance, dissipation and enclosure, not a census of activity or embodiment. -/
theorem exchange_not_recurring {stand''')
once('''  Flow.exchanges_finitely balanced dissipative standing around''',
     '''  Flow.exchange_not_recurring balanced dissipative standing around''')
once('''/-- A world meeting all eight premises with each binding comes to rest (`hatch_binds`).
Across the first step the child arises and the parent ceases; every step is enclosed
within the food, the parent and the child, and finitely many stand at each step, though
the world is not finite. -/
theorem hatch_rests : hatch.web.Arises 0 .child ∧ hatch.web.Ceases 0 .parent ∧
    ¬ hatch.ArisingRecurs ∧ ¬ hatch.CeasingRecurs :=
  ⟨⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, ⟨Nat.zero_lt_one, Nat.lt_irrefl 0⟩,
   rests_enclosed hatch_counted''',
     '''/-- In a world meeting all eight premises with each binding (`hatch_binds`), that it rests
from some step on cannot be refuted. Across the first step the child arises and the parent
ceases; every step is enclosed within the food, the parent and the child, and finitely many
stand at each step, though the world is not finite. -/
theorem hatch_rests_unrefuted : hatch.web.Arises 0 .child ∧ hatch.web.Ceases 0 .parent ∧
    ¬ ¬ ∃ N, hatch.RestsFrom N :=
  ⟨⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, ⟨Nat.zero_lt_one, Nat.lt_irrefl 0⟩,
   rests_unrefuted_enclosed hatch_counted''')
p.write_text(t)
print('ok')
