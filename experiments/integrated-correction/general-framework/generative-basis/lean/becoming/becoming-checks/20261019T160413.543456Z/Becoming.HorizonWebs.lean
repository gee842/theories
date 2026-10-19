import Becoming.Dependence

/-!
# The horizon in the support-gated law, on its webs

`Becoming.Horizon` shows that no finite stretch of a run decides whether the focal formation
renews or consumes, for the runs of `Renewable` and for the support-gated law of
`RelationalRenewal` (`Feedback.prefix_does_not_decide`). A support-gated law is one unfolding
with one shared condition (`RelationalRenewal.Law.unfolding`), read as a web of the spine whose
dependences never change (`Web.static`), with the same renewing and consuming formations
(`Web.static_renewingIn`, `Web.static_consumingIn`). This module states the support-gated horizon
law on those webs.

* **No prefix decides, on webs.** For every horizon `h`, the static webs of the support-gated law
  under the schedule that stops overdrawing at `h` and under the one that never stops stand at the
  same level of the shared condition up to `h`, and the focal formation renews in the first and
  consumes in the second (`prefix_does_not_decide`).

No ethical predicate, ranking or axiom occurs.

Declarations moved here unchanged, with their names, from `Becoming.Horizon` (board item W): see the
sections so headed.
-/

/-! ## The support-gated law (moved from `Becoming.Horizon`) -/

namespace Becoming

universe u v

variable {S : Type u} {A : Type v}

namespace Feedback

open RelationalRenewal RelationalRenewal.Law

/-- Start `h + 1`, renewal one unit, sustaining need one, focal need zero, no
contribution. Renewal stops below support. -/
def law (h : Nat) (d : Nat → Nat) : Law := ⟨h + 1, 1, 1, 0, d, fun _ => 0⟩

/-- Two units a step before `h`, then the renewal only. -/
def stopping (h t : Nat) : Nat := if t < h then 2 else 1

/-- Two units a step throughout. -/
def continuing (_ : Nat) : Nat := 2

theorem step_two {h t m : Nat} {d : Nat → Nat} (high : (law h d).level t = m + 2)
    (two : d t = 2) : (law h d).level (t + 1) = m + 1 := by
  rw [level_succ, high,
    if_pos (show (law h d).needG ≤ m + 2 from Nat.succ_le_succ (Nat.zero_le _)),
    if_pos (show (law h d).needF ≤ m + 2 from Nat.zero_le _)]
  show m + 1 + 1 + 1 + 0 - d t = m + 1
  rw [two]
  exact add_sub_self (m + 1) 2

theorem step_one {h t : Nat} {d : Nat → Nat} (one : (law h d).level t = 1) (same : d t = 1) :
    (law h d).level (t + 1) = 1 := by
  rw [level_succ, one, if_pos (show (law h d).needG ≤ 1 from Nat.le_refl 1),
    if_pos (show (law h d).needF ≤ 1 from Nat.zero_le _)]
  show 1 + 1 + 0 - d t = 1
  rw [same]

/-- Before the horizon, the level falls by one a step under either schedule. -/
theorem descending (h : Nat) (d : Nat → Nat) (two : ∀ t, t < h → d t = 2) :
    ∀ k, k ≤ h → (law h d).level k + k = h + 1
  | 0, _ => rfl
  | k + 1, le => by
    have ih := descending h d two k (Nat.le_of_succ_le le)
    have bound : 2 + k ≤ (law h d).level k + k := by
      rw [ih, Nat.add_comm 2 k]
      exact Nat.succ_le_succ le
    obtain ⟨m, hm⟩ := Nat.le.dest (le_of_add_le_add_right k bound)
    have high : (law h d).level k = m + 2 := by rw [← hm, Nat.add_comm]
    rw [step_two high (two k (Nat.lt_of_succ_le le))]
    rw [high] at ih
    rw [Nat.add_succ, ← Nat.succ_add]
    exact ih

theorem at_horizon (h : Nat) : (law h (stopping h)).level h = 1 :=
  add_right_cancel h ((descending h (stopping h) (fun _ before => if_pos before) h
    (Nat.le_refl h)).trans (Nat.add_comm h 1))

theorem after_horizon (h : Nat) : ∀ j, (law h (stopping h)).level (h + j) = 1
  | 0 => at_horizon h
  | j + 1 => step_one (after_horizon h j) (if_neg (Nat.not_lt_of_le (Nat.le_add_right h j)))

theorem supported (h t : Nat) : 1 ≤ (law h (stopping h)).level t :=
  match Nat.lt_or_ge t h with
  | .inl before =>
    le_of_add_le_add_right t (Nat.le_trans
      (show 1 + t ≤ h + 1 from (Nat.add_comm 1 t) ▸ Nat.succ_le_succ (Nat.le_of_lt before))
      (Nat.le_of_eq (descending h (stopping h) (fun _ b => if_pos b) t
        (Nat.le_of_lt before)).symm))
  | .inr after =>
    match Nat.le.dest after with
    | ⟨j, sum⟩ => sum ▸ Nat.le_of_eq (after_horizon h j).symm

/-- For every horizon, in the support-gated law, from the same start, under draws that
agree before the horizon (two units, one beyond renewal): stopping there renews,
continuing consumes. The renewing schedule never reaches the threshold below which
renewal stops, so the feedback does not change the horizon result. -/
theorem prefix_does_not_decide (h : Nat) :
    (law h (stopping h)).start = (law h continuing).start ∧
    (∀ t, t < h → stopping h t = continuing t) ∧
    RenewingIn (law h (stopping h)).unfolding .focal ∧
    ConsumingIn (law h continuing).unfolding .focal :=
  ⟨rfl, fun _ before => if_pos before,
   fun _ _ t g depends => match g, depends with
     | .sustaining, _ => supported h t,
   (overdraw_consuming (law h continuing) Nat.zero_lt_one (Nat.zero_le 1) (T0 := 0)
     fun _ _ => Nat.lt_succ_self 1).1⟩

end Feedback

end Becoming


namespace Becoming

namespace HorizonWebs

open RelationalRenewal

/-- **No prefix decides, on webs.** For every horizon `h`, the static webs of the support-gated
law under two draw schedules that agree before `h` stand at the same level of the shared condition
up to `h`; in the web of the schedule that stops overdrawing at `h` the focal formation renews,
and in the web of the schedule that never stops it consumes. -/
theorem prefix_does_not_decide (h : Nat) :
    (∀ t, t ≤ h →
      (Web.static (Feedback.law h (Feedback.stopping h)).unfolding).level t () =
        (Web.static (Feedback.law h Feedback.continuing).unfolding).level t ()) ∧
      (Web.static (Feedback.law h (Feedback.stopping h)).unfolding).RenewingIn .focal ∧
      (Web.static (Feedback.law h Feedback.continuing).unfolding).ConsumingIn .focal :=
  ⟨fun t bound => add_right_cancel t
    ((Feedback.descending h (Feedback.stopping h) (fun _ before => if_pos before) t bound).trans
      (Feedback.descending h Feedback.continuing (fun _ _ => rfl) t bound).symm),
   (Web.static_renewingIn _ _).mpr (Feedback.prefix_does_not_decide h).2.2.1,
   (Web.static_consumingIn _ _).mpr (Feedback.prefix_does_not_decide h).2.2.2⟩

end HorizonWebs

end Becoming
