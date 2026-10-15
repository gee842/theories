import Becoming.Stock
import RenewingFormation

/-!
# Formation beyond renewal as a level drawn on, an instance of `Becoming.Stock`

`RenewingFormation` states, under its supplied no-recovery wear law, that formation whose pressure
persistently exceeds the current renewal rate has a whole-unfolding total bounded by the held
conditions plus a triangular renewal bound (`budget`) and ceases from that time. This periphery
module reads both on the core's laws of a level drawn on and not replenished.

* Steps beyond the current rate are the moves of one process, each move recording the pressure and
  what forms (`beyond`). Across each such step the budget falls by at least what forms
  (`budget_falls`, `Stock.FallsBy`), and something forms wherever the budget is positive
  (`forms_while_held`); both are `beyond_step`.
* The first `n` steps of a course beyond the current rate are a trace of that process
  (`path_trace`), drawing in all what formed (`total_moves`). So, by `Stock.trace_falls`, the
  whole-unfolding total is bounded by the budget (`beyond_current_bounded_by_core`), and by
  `Stock.exhausted_within` and `Stock.draws_nothing_from_empty`, nothing forms from the time equal
  to the budget (`beyond_current_ceases_by_core`). Every allocation of that formation to a part,
  shared formation included, ends with it (`shared_formation_ends_by_core`).

The wear law, the triangular bound and the representation of formation keep the periphery's scope;
which real processes satisfy the law is a correspondence question. The core does not import this
module.
-/

namespace Becoming.RenewingCorrespondence

open Generative RenewingFormation

/-- Steps beyond the current renewal rate: a move records the pressure and what forms. -/
def beyond (law : RenewingFormation.WearLaw) : Process RenewingFormation.Conditions (Nat × Nat) :=
  ⟨fun c a c' => c.renew < a.1 ∧ a.2 = RenewingFormation.formedAt c a.1 ∧ c' = RenewingFormation.next law c a.1⟩

/-- What a move forms. -/
def formedOf (a : Nat × Nat) : Nat := a.2

/-- **Across each step beyond renewal the budget falls by at least what forms.** -/
theorem budget_falls (law : RenewingFormation.WearLaw) :
    Stock.FallsBy (beyond law) RenewingFormation.budget formedOf := by
  rintro c ⟨d, k⟩ c' ⟨over, forms, rfl⟩
  have forms : k = RenewingFormation.formedAt c d := forms
  have := (RenewingFormation.beyond_step law c d over).1
  show RenewingFormation.budget (RenewingFormation.next law c d) + k ≤ RenewingFormation.budget c
  rw [forms, Nat.add_comm]
  exact this

/-- **Something forms wherever the budget is positive.** -/
theorem forms_while_held (law : RenewingFormation.WearLaw) :
    ∀ s a t, (beyond law).step s a t → 0 < RenewingFormation.budget s → 0 < formedOf a := by
  rintro c ⟨d, k⟩ c' ⟨over, forms, _⟩ positive
  have forms : k = RenewingFormation.formedAt c d := forms
  show 0 < k
  rw [forms]
  exact (RenewingFormation.beyond_step law c d over).2 positive

/-- The moves of the first `n` steps. -/
def moves (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat) (n : Nat) : List (Nat × Nat) :=
  (List.range n).map fun i => (demand i, RenewingFormation.formed law c0 demand i)

theorem moves_length (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat) (n : Nat) :
    (moves law c0 demand n).length = n := by
  simp [moves]

theorem moves_succ (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat) (n : Nat) :
    moves law c0 demand (n + 1) = moves law c0 demand n ++ [(demand n, RenewingFormation.formed law c0 demand n)] := by
  simp [moves, List.range_succ]

theorem total_append {α : Type} (xs ys : List α) (q : α → Nat) :
    total (xs ++ ys) q = total xs q + total ys q := by
  induction xs with
  | nil => simp [total]
  | cons x xs ih => simp [total, ih, Nat.add_assoc]

/-- The first `n` steps draw in all what formed. -/
theorem total_moves (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat) :
    ∀ n, total (moves law c0 demand n) formedOf = RenewingFormation.cumulative law c0 demand n
  | 0 => rfl
  | n + 1 => by
    rw [moves_succ, total_append, total_moves law c0 demand n]
    simp [total, formedOf, RenewingFormation.cumulative]

/-- **The first `n` steps of a course beyond the current rate are a trace of the process.** -/
theorem path_trace (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat)
    (over : RenewingFormation.BeyondCurrent law c0 demand) :
    ∀ n, Trace (beyond law) c0 (moves law c0 demand n) (RenewingFormation.path law c0 demand n)
  | 0 => .nil c0
  | n + 1 => by
    rw [moves_succ]
    exact trace_append_iff.mpr ⟨RenewingFormation.path law c0 demand n, path_trace law c0 demand over n,
      .cons ⟨over n, rfl, rfl⟩ (.nil _)⟩

/-- **Beyond the current rate, the whole unfolding's formation is bounded by the budget**
(`Stock.trace_falls`). -/
theorem beyond_current_bounded_by_core (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat)
    (over : RenewingFormation.BeyondCurrent law c0 demand) : ∀ n, RenewingFormation.cumulative law c0 demand n ≤ RenewingFormation.budget c0 := by
  intro n
  have h := Stock.trace_falls (budget_falls law) (path_trace law c0 demand over n)
  rw [total_moves] at h
  exact Nat.le_trans (Nat.le_add_left _ _) h

/-- **Beyond the current rate, nothing forms from the time equal to the budget**
(`Stock.exhausted_within`, `Stock.draws_nothing_from_empty`). -/
theorem beyond_current_ceases_by_core (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (demand : Nat → Nat)
    (over : RenewingFormation.BeyondCurrent law c0 demand) : ∀ n, RenewingFormation.budget c0 ≤ n → RenewingFormation.formed law c0 demand n = 0 := by
  intro n late
  have empty : RenewingFormation.budget (RenewingFormation.path law c0 demand n) = 0 :=
    Stock.exhausted_within (budget_falls law) (forms_while_held law)
      (path_trace law c0 demand over n) (by rw [moves_length]; exact late)
  exact Stock.draws_nothing_from_empty (budget_falls law)
    (a := (demand n, RenewingFormation.formed law c0 demand n)) (t := RenewingFormation.path law c0 demand (n + 1))
    ⟨over n, rfl, rfl⟩ empty

/-- **Every allocation of formation beyond renewal ends with it**: whatever part a share of what
forms goes to, shared formation included, it is nothing from the time equal to the budget. -/
theorem shared_formation_ends_by_core (law : RenewingFormation.WearLaw) (c0 : RenewingFormation.Conditions) (pressure share : Nat → Nat)
    (joint : RenewingFormation.BeyondCurrent law c0 pressure) (allocated : ∀ n, share n ≤ RenewingFormation.formed law c0 pressure n) :
    ∀ n, RenewingFormation.budget c0 ≤ n → share n = 0 := fun n late =>
  Nat.eq_zero_of_le_zero
    (Nat.le_trans (allocated n) (Nat.le_of_eq (beyond_current_ceases_by_core law c0 pressure joint n late)))

end Becoming.RenewingCorrespondence
