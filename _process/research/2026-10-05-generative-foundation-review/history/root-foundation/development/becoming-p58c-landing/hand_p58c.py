#!/usr/bin/env python3
"""P58c hand edits after the token renames: Premises, Sampling, Resolution, Counting. Usage: hand_p58c.py TREE"""
import sys
from pathlib import Path
B = Path(sys.argv[1]) / 'Becoming'


def edit(name, pairs):
    p = B / name; t = p.read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (name, t.count(old), old[:70])
        t = t.replace(old, new)
    p.write_text(t)


edit('Premises.lean', [(
'''/-- A finite world which meets the premises comes to rest: neither arising nor ceasing
recurs. The proof uses balance, dissipation and embodiment, and no decision procedure. -/
theorem premised_rests_unrefuted (finite : w.Finite)
    (premised : w.Premised) : ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  rests finite''',
'''/-- In a finite world which meets the premises, that it rests from some step on cannot be
refuted, so neither arising nor ceasing recurs (`not_recurring_of_rests_unrefuted`). The proof
uses balance, dissipation and embodiment, and no decision procedure. -/
theorem premised_rests_unrefuted (finite : w.Finite)
    (premised : w.Premised) : ¬ ¬ ∃ N, w.RestsFrom N :=
  rests_unrefuted finite''')])
edit('Sampling.lean', [(
'''/-- The laws of a world hold at every step size: a finite world read at coarser steps, whose
flow balances and dissipates and whose arisings are embodied, has neither arising nor ceasing
recurring, with no decision procedure (`World.rests`). -/
theorem sample_rests_unrefuted (strict : Strict σ)
    (finite : w.Finite) (once : w.flow.Once) (balanced : w.Balanced)
    (dissipative : w.Dissipative) (embodied : w.Embodied) :
    ¬ (w.sample σ).ArisingRecurs ∧ ¬ (w.sample σ).CeasingRecurs :=
  rests (sample_finite finite)''',
'''/-- The laws of a world hold at every step size: of a finite world read at coarser steps, whose
flow balances and dissipates and whose arisings are embodied, that it rests from some coarse step
on cannot be refuted, with no decision procedure (`World.rests_unrefuted`). -/
theorem sample_rests_unrefuted (strict : Strict σ)
    (finite : w.Finite) (once : w.flow.Once) (balanced : w.Balanced)
    (dissipative : w.Dissipative) (embodied : w.Embodied) :
    ¬ ¬ ∃ N, (w.sample σ).RestsFrom N :=
  rests_unrefuted (sample_finite finite)''')])
edit('Resolution.lean', [
('''/-- Rest from a step on is rest. -/
theorem rests_unrefuted_of_after {T : Nat}
    (rest : ¬ (w.after T).ArisingRecurs ∧ ¬ (w.after T).CeasingRecurs) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  ⟨fun arising => rest.1 (after_recurs (p := fun t x => w.web.Arises t x) arising),
   fun ceasing => rest.2 (after_recurs (p := fun t x => w.web.Ceases t x) ceasing)⟩''',
'''/-- Rest of the world from step `T` on is rest of the world: where the world after `T` rests
from step `N` on, the world rests from step `T + N` on. -/
theorem restsFrom_of_after {T N : Nat} (rest : (w.after T).RestsFrom N) : w.RestsFrom (T + N) :=
  fun t later x => match Nat.le.dest later with
  | ⟨k, same⟩ => Eq.subst (motive := fun u => ¬ w.web.Arises u x ∧ ¬ w.web.Ceases u x)
      ((Nat.add_assoc T N k).symm.trans same) (rest (N + k) (Nat.le_add_right N k) x)

/-- That the world from step `T` on rests from some step on cannot be refuted, so that the world
rests from some step on cannot be refuted. -/
theorem rests_unrefuted_of_after {T : Nat}
    (rest : ¬ ¬ ∃ N, (w.after T).RestsFrom N) : ¬ ¬ ∃ N, w.RestsFrom N :=
  fun none_ => rest fun ⟨N, quiet⟩ => none_ ⟨T + N, restsFrom_of_after quiet⟩'''),
('''anything, neither arising nor ceasing recurs. -/
theorem rests_unrefuted_without_refinement (counted : w.Counted) (embodied : w.Embodied) {split : Nat → Nat}
    (balances : w.flow.BalancesAt (fun t => split t + 1) w.web) (dissipative : w.Dissipative)
    {T : Nat} (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t)
    (unrefined : ∀ t, T ≤ t → ∀ x, split t * w.web.level t x = 0) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  rests_unrefuted_of_after (rests_enclosed''',
'''anything, that the world rests from some step on cannot be refuted. -/
theorem rests_unrefuted_without_refinement (counted : w.Counted) (embodied : w.Embodied)
    {split : Nat → Nat}
    (balances : w.flow.BalancesAt (fun t => split t + 1) w.web) (dissipative : w.Dissipative)
    {T : Nat} (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t)
    (unrefined : ∀ t, T ≤ t → ∀ x, split t * w.web.level t x = 0) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
  rests_unrefuted_of_after (rests_unrefuted_enclosed'''),
('''every step from `T` on, neither arising nor ceasing recurs. Counted so,''',
 '''every step from `T` on, that the world rests from some step on cannot be refuted. Counted so,'''),
('''    (enclosed : ∀ t, T ≤ t → (w.flow.withRefinement w.web split).Enclosed t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have unrefined''',
'''    (enclosed : ∀ t, T ≤ t → (w.flow.withRefinement w.web split).Enclosed t) :
    ¬ ¬ ∃ N, w.RestsFrom N :=
  have unrefined'''),
('''  rests_unrefuted_of_after (rests_enclosed (after_counted counted T) (after_embodied embodied T)
    (after_balanced balances unrefined)
    (after_dissipative fun t later cs distinct closed =>''',
'''  rests_unrefuted_of_after (rests_unrefuted_enclosed (after_counted counted T)
    (after_embodied embodied T) (after_balanced balances unrefined)
    (after_dissipative fun t later cs distinct closed =>'''),
('''  fun enclosed => (rests_unrefuted_refinement_counted counted embodied balances dissipative enclosed).1
    arising''',
'''  fun enclosed => (not_recurring_of_rests_unrefuted
    (rests_unrefuted_refinement_counted counted embodied balances dissipative enclosed)).1 arising'''),
('''    (rests_unrefuted_without_refinement counted embodied balances dissipative enclosed unrefined).1 arising''',
'''    (not_recurring_of_rests_unrefuted
      (rests_unrefuted_without_refinement counted embodied balances dissipative enclosed unrefined)).1
      arising'''),
])
edit('Counting.lean', [
('''premise binds and arising stops (`hatch_rests_unrefuted`); in a queue''',
 '''premise binds and arising does not recur (`hatch_rests_unrefuted`); in a queue'''),
('''  ⟨⟨hatch_binds.1, hatch_binds.2, hatch_rests_unrefuted.2.2.1⟩,''',
 '''  ⟨⟨hatch_binds.1, hatch_binds.2, (not_recurring_of_rests_unrefuted hatch_rests_unrefuted.2.2).1⟩,'''),
])
print('ok')
