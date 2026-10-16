#!/usr/bin/env python3
"""If P73's Becoming.Learning is on main when P70–P72 land, apply this to lean/Becoming/Description.lean.

Usage: python3 -B learning_patch.py DESCRIPTION_LEAN

Learning's goAlike_iff_lumped and Description's Law.goAlike_process_iff are one law, written
independently with the same proof; the second to land states the identity. Landing second,
Description imports Becoming.Learning, takes Law.goAlike_process_iff as the instance of
goAlike_iff_lumped (name and statement kept), and adds the two instance theorems between
Learning's lasso and its own states. Checked in scratch on P73's package (Learning a73c889e):
Description 53 theorems, empty axiom reports. Rerunning on a patched file fails.
"""
import sys
from pathlib import Path

path = Path(sys.argv[1])
s = path.read_text()


def sub(old, new):
    global s
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)


sub('import Becoming.Context\n', 'import Becoming.Context\nimport Becoming.Learning\n')
sub('''/-- Under a determined law, going alike is carrying what is lumped into what is lumped. -/
theorem goAlike_process_iff {next : S → S} {π : S → K} :
    GoAlike (process next) π ↔ ∀ s s', π s = π s' → π (next s) = π (next s') :=
  ⟨fun alike s s' same => alike s s' () (next s) (next s') same rfl rfl,
   fun lumped s s' _ _ _ same step step' =>
    (congrArg π step).trans ((lumped s s' same).trans (congrArg π step').symm)⟩''',
'''/-- Under a determined law, going alike is carrying what is lumped into what is lumped. This is
`Becoming.Learning`'s `goAlike_iff_lumped`, written independently with the same proof, and is
stated here as its instance. -/
theorem goAlike_process_iff {next : S → S} {π : S → K} :
    GoAlike (process next) π ↔ ∀ s s', π s = π s' → π (next s) = π (next s') :=
  Learning.goAlike_iff_lumped''')
sub('''  denial, `Becoming.Diagonal`'s rhythm of a revision that never rests, has exactly two states
  (`Denial.two_states`), each defined through the other (`Denial.each_through_other`).''',
'''  denial, `Becoming.Diagonal`'s rhythm of a revision that never rests, has exactly two states
  (`Denial.two_states`), each defined through the other (`Denial.each_through_other`).
  `Becoming.Learning`'s lasso course is two moments being one state (`lasso_iff_sameAhead`), so
  finitely many states is a lasso (`finitely_many_states_iff_lasso`).''')
TAIL = '''
/-! ## Lassos are finitely many states -/

section Lassos

variable {O : Type u}

/-- **A lasso is two moments that are one state.** `Becoming.Learning`'s course repeating from
step `i` with period `q + 1` (`Learning.Lasso`) is moments `i` and `i + (q + 1)` being one
state. -/
theorem lasso_iff_sameAhead {o : Nat → O} {i q : Nat} :
    Learning.Lasso o i q ↔ SameAhead o i (i + (q + 1)) :=
  ⟨fun lasso n => (lasso (i + n) (Nat.le_add_right i n)).symm.trans
      (congrArg o (Nat.add_right_comm i n (q + 1))),
   fun same u later => match gap_of_le later with
    | ⟨d, at_u⟩ => by
      subst at_u
      exact (congrArg o (Nat.add_right_comm i d (q + 1))).trans (same d).symm⟩

/-- **Finitely many states is a lasso**: a registered history has finitely many states exactly
where it repeats from some step on with some period, `Becoming.Learning`'s lasso course. -/
theorem finitely_many_states_iff_lasso {o : Nat → O} :
    (∃ L, StatesBelow o L) ↔ ∃ i q, Learning.Lasso o i q :=
  finitely_many_states_iff.trans
    ⟨fun ⟨i, _, lt, same⟩ => match gap_of_lt lt with
      | ⟨q, at_j⟩ => ⟨i, q, lasso_iff_sameAhead.mpr (at_j ▸ same)⟩,
     fun ⟨i, q, lasso⟩ =>
      ⟨i, i + (q + 1), Nat.lt_succ_of_le (Nat.le_add_right i q), lasso_iff_sameAhead.mp lasso⟩⟩

end Lassos

end Becoming
'''
assert s.rstrip().endswith('end Becoming')
s = s.rstrip()[:-len('end Becoming')].rstrip() + '\n' + TAIL
path.write_text(s)
print('patched', path)
