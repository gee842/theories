import Becoming
import RenewalComparison
import RenewalRecovery

/-!
# The support-gated renewal law's peripheral results as instances of the spine's laws

`RelationalRenewal.Law` is one family of unfoldings: a shared condition renewed by a
sustaining formation while the condition supports it, drawn on and contributed to by a
focal formation while the condition supports that one. Three peripheral results were
proved for this family only: the classification of overdraw and joint drawing
(`RelationalRenewal`), recovery (`RenewalRecovery`) and the comparison of courses
(`RenewalComparison`). `Becoming.RenewalFlow` shows every law of the family to be a balanced
flow on its static web and derives the family's restoration, loss for good and joint ending
from laws that hold for every balanced flow. This module reads the other two peripheral
modules through those laws:

* Restoration: the supported pulse of `RenewalRecovery` is an instance of
  `SupportGated.repair_restores` (`pulse_restores`), as in
  `RenewalRecovery.repair_restores_sustaining_support`.
* Comparison of courses (`Ranking.renewed_extends_iff`): `RenewalComparison`'s relational
  extension of the course without an overdrawing formation, and of sharing over winning by
  consumption, are instances of the law of comparison with a renewing course
  (`overdraw_extension`, `contest_extensions`).

Every declaration has an empty axiom report. Of the peripheral modules only definitions and
`RenewalComparison.undisturbed_sustains` are used.
-/

namespace Becoming

namespace SupportGated

open RelationalRenewal RelationalRenewal.Law

variable (L : Law)

/-- `RenewalRecovery`'s supported pulse, from step 1, where its level is 1: one step of
net giving restores the sustaining need. -/
theorem pulse_restores :
    (RenewalRecovery.pulse 2).needG ≤ (RenewalRecovery.pulse 2).level
      (1 + ((RenewalRecovery.pulse 2).needG - (RenewalRecovery.pulse 2).level 1)) :=
  repair_restores (RenewalRecovery.pulse 2) 1 (by decide) (by decide)

/-! ## Comparison of courses -/

/-- `RenewalComparison`'s relational extension of the course without an overdrawing
formation is an instance of `Ranking.renewed_extends_iff`: the course without it renews
every condition, is active at every event the course with it includes, and the sustaining
formation is active there after the loss. -/
theorem overdraw_extension (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG)
    (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    GenerativeComparison.GenerativeExtension
      (RenewalComparison.relationalInventory (RenewalComparison.course L)) .occurs .absent :=
  have sustains : ∀ t, L.needG ≤ RenewalComparison.undisturbed L t := fun t =>
    Nat.le_trans gStart (RenewalComparison.undisturbed_sustains L gStart t)
  match overdraw_consuming L positive fWithin over with
  | ⟨consuming, T, lost⟩ =>
    (Ranking.renewed_extends_iff (U := RenewalComparison.course L) (w := .occurs)
      (w' := .absent) fun _ t g _ => match g with
        | .focal => Nat.le_trans fWithin (sustains t)
        | .sustaining => sustains t).1.mpr
      ⟨fun
        | (.focal, _), ⟨_, notConsuming⟩ => absurd consuming notConsuming
        | (.sustaining, t), _ => sustains t,
       (.sustaining, T), sustains T, fun alive => lost T (Nat.le_refl T) alive.1⟩

/-- `RenewalComparison`'s extensions of winning by consumption by sharing, under both its
readings, are instances of the law of comparison with a renewing course in which every
formation is active at every step. -/
theorem contest_extensions :
    GenerativeComparison.GenerativeExtension
        (RenewalComparison.relationalInventory RenewalComparison.contest) .wins .shares ∧
      GenerativeComparison.GenerativeExtension
        (RenewalComparison.broadInventory RenewalComparison.contest) .wins .shares :=
  match overdraw_consuming winning (Nat.succ_pos 0) (Nat.zero_le 1) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1) with
  | ⟨_, T, lost⟩ =>
    have kept := within_renewal_sustains sharing (fun _ => Nat.le_refl 1)
      (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
    have renews : ∀ c, Renewed (RenewalComparison.contest .shares) c :=
      fun _ t g depends => match g, depends with
        | .focal, depends => absurd depends (Nat.lt_irrefl 0)
        | .sustaining, _ => Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t)
    have always : ∀ t p, (RenewalComparison.contest .shares).active t p := fun t p =>
      match p with
      | .focal => Nat.zero_le _
      | .sustaining => Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t)
    ⟨(Ranking.renewed_active_extends_iff (U := RenewalComparison.contest) (w := .wins)
        (w' := .shares) renews always).1.mpr
        ⟨(.sustaining, T), fun alive => lost T (Nat.le_refl T) alive.1⟩,
     (Ranking.extendsUnder_iff_of_exact (reading := fun (w : RenewalComparison.Contest) (e : Part × Nat) =>
        (RenewalComparison.contest w).active e.2 e.1) (w := .wins) (w' := .shares)
        fun _ => Iff.rfl).mpr
        ⟨fun e _ => always e.2 e.1, ((Part.sustaining, T) : Part × Nat), always T .sustaining,
          lost T (Nat.le_refl T)⟩⟩

end SupportGated

end Becoming
