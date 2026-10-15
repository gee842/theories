import Becoming.Weighted
import CorrectionDependence

/-!
# Draws on one shared stock as an instance of the core's law of listed masses

`CorrectionDependence` states, for the first `n` draws given as natural numbers, that every
selection of them fits within the stock exactly when their total does
(`every_selection_within_iff_total_within`), and that draws each fitting alone need not fit
together (`each_within_alone_not_together`). `Becoming.Weighted` states, for every listed domain
and every weighting of its entries, that every event stays within a bound exactly where the whole
domain does (`every_event_within_iff`), and that entries each within the bound need not be within
it together (`entries_within_not_together`).

This periphery module reads the first: the first `n` draws listed latest first are a domain
(`firstDraws`), a selection is an event on it and the draws are the weighting, so the selected
total is the selection's mass (`selectedTotal_eq_mass`) and the total is the whole domain's
(`total_eq_mass`). The two statements of `CorrectionDependence` then follow from the core's
(`every_selection_within_iff_total_within`, `each_within_alone_not_together`). The core does not
import this module; what a draw and the stock stand for keeps `CorrectionDependence`'s scope.
-/

namespace SharedStockInstances

open Becoming

/-- The first `n` draws, latest first. -/
def firstDraws : Nat → List Nat
  | 0 => []
  | n + 1 => n :: firstDraws n

/-- **A selected total is the mass of the selection on the first draws.** -/
theorem selectedTotal_eq_mass (chosen : Nat → Bool) (draws : Nat → Nat) :
    ∀ n, CorrectionDependence.selectedTotal n chosen draws = mass (firstDraws n) draws chosen
  | 0 => rfl
  | n + 1 => by
    show CorrectionDependence.selectedTotal n chosen draws + (if chosen n = true then draws n else 0) =
      (if chosen n = true then draws n else 0) + mass (firstDraws n) draws chosen
    rw [selectedTotal_eq_mass chosen draws n, Nat.add_comm]

/-- **The total is the mass of the whole domain of first draws.** -/
theorem total_eq_mass (draws : Nat → Nat) :
    ∀ n, CorrectionDependence.total n draws = mass (firstDraws n) draws (fun _ => true)
  | 0 => rfl
  | n + 1 => by
    show CorrectionDependence.total n draws + draws n =
      (if true = true then draws n else 0) + mass (firstDraws n) draws (fun _ => true)
    rw [total_eq_mass draws n, if_pos rfl, Nat.add_comm]

/-- **Every selection fits within the stock exactly when the total does**: the core's
`every_event_within_iff` on the first draws. -/
theorem every_selection_within_iff_total_within (n stock : Nat) (draws : Nat → Nat) :
    (∀ chosen, CorrectionDependence.selectedTotal n chosen draws ≤ stock) ↔
      CorrectionDependence.total n draws ≤ stock :=
  ⟨fun all => Eq.subst (motive := fun z => z ≤ stock) (total_eq_mass draws n).symm
      (every_event_within_iff.mp fun event =>
        Eq.subst (motive := fun z => z ≤ stock) (selectedTotal_eq_mass event draws n) (all event)),
   fun whole chosen => Eq.subst (motive := fun z => z ≤ stock) (selectedTotal_eq_mass chosen draws n).symm
      (every_event_within_iff.mpr
        (Eq.subst (motive := fun z => z ≤ stock) (total_eq_mass draws n) whole) chosen)⟩

/-- **Draws each fitting alone need not fit together**: two draws of two on a stock of two, the
whole domain's mass four, as in the core's `entries_within_not_together`. -/
theorem each_within_alone_not_together :
    (∀ i, i < 2 → (fun _ : Nat => 2) i ≤ 2) ∧
      ¬ (∀ chosen, CorrectionDependence.selectedTotal 2 chosen (fun _ => 2) ≤ 2) :=
  ⟨fun _ _ => Nat.le_refl 2, fun within => absurd
    (Eq.subst (motive := fun z => z ≤ 2) (total_eq_mass (fun _ => 2) 2)
      ((every_selection_within_iff_total_within 2 2 (fun _ => 2)).mp within))
    (by decide)⟩

end SharedStockInstances
