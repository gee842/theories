import Becoming.RenewalFlow

/-!
# Recovery in the support-gated renewal family: its window and its obstruction

`Becoming.RenewalFlow` reads every law of the support-gated family (`RelationalRenewal.Law`) as a
balanced flow and proves restoration (`SupportGated.repair_restores`) and loss for good
(`SupportGated.below_for_good`) as instances of laws of every flow. Board item F3R (18 October
2026) states here, on the core and constructively, what `RenewalRecovery` (8 October) proved of
the family's recovery window and its pulse histories, and what the joins `SupportGatedWebs` and
`SupportGatedWebsInherited` read of them on the webs.

* **No third route.** Where both formations have lost their support, the level stays where it is
  whatever is later drawn or contributed (`absorbs`).
* **The window.** A supported step of positive net repair raises the level by at least one even
  where the sustaining formation is inactive (`repair_step`), so a window of such steps raises it
  by at least its length (`window_progress`); restoration of the sustaining need is
  `SupportGated.repair_restores`.
* **Two pulses.** Two histories start at level 2 and differ only in their first draw; every later
  draw and contribution is the same (`same_later_inputs`). The supported pulse falls to 1 and
  returns to 2 (`pulse_levels`) and stays at the sustaining need from step 2 on
  (`supported_pulse_recovers`); the unsupported pulse falls to 0 and stays there with every
  formation inactive (`unsupported_pulse_ends`). The recovered history is neither renewing nor
  consuming in the family's whole-time classification, on its unfolding and its web
  (`recovered_neither`, `recovered_web_neither`): the classification has a scope, which this states.

The amounts, thresholds and contribution schedule are the family's inputs; no source of them and
no ethical direction is inferred. Every declaration has an empty axiom report.
-/

namespace Becoming

open RelationalRenewal RelationalRenewal.Law

namespace SupportRecovery

/-! ## No third route -/

/-- **Where both formations have lost their support, the level stays.** -/
theorem absorbs (L : Law) (T : Nat) (fOff : L.level T < L.needF) (gOff : L.level T < L.needG) :
    ∀ n, L.level (T + n) = L.level T
  | 0 => rfl
  | n + 1 => by
    have before := absorbs L T fOff gOff n
    show L.level (T + n + 1) = L.level T
    rw [L.level_succ, before, if_neg (Nat.not_le_of_gt gOff), if_neg (Nat.not_le_of_gt fOff)]

/-! ## The window -/

/-- **A supported step of positive net repair raises the level by at least one**, whether or not
the sustaining formation is active. -/
theorem repair_step (L : Law) (t : Nat) (fOn : L.needF ≤ L.level t)
    (surplus : L.draw t < L.contrib t) : L.level t + 1 ≤ L.level (t + 1) := by
  have one : 1 ≤ L.contrib t - L.draw t := SupportGated.sub_pos_of_lt surplus
  rw [L.level_succ, if_pos fOn, if_pos fOn]
  cases Nat.lt_or_ge (L.level t) L.needG with
  | inl gOff =>
    rw [if_neg (Nat.not_le_of_gt gOff),
      SupportGated.add_sub_assoc_of_le _ (Nat.le_of_lt surplus)]
    exact Nat.add_le_add_left one _
  | inr gOn =>
    rw [if_pos gOn, SupportGated.add_sub_assoc_of_le _ (Nat.le_of_lt surplus), Nat.add_assoc]
    exact Nat.add_le_add_left (Nat.le_trans one (Nat.le_add_left _ _)) _

/-- **A window of supported positive net repair raises the level by at least its length**; the
repairing formation stays supported because the level never falls within the window. -/
theorem window_progress (L : Law) (T N : Nat) (fOn : L.needF ≤ L.level T)
    (surplus : ∀ d, d < N → L.draw (T + d) < L.contrib (T + d)) :
    ∀ d, d ≤ N → L.level T + d ≤ L.level (T + d)
  | 0, _ => Nat.le_refl _
  | d + 1, bound =>
    have prior := window_progress L T N fOn surplus d (Nat.le_of_succ_le bound)
    have active : L.needF ≤ L.level (T + d) :=
      Nat.le_trans fOn (Nat.le_trans (Nat.le_add_right _ d) prior)
    Nat.le_trans (Nat.succ_le_succ prior)
      (repair_step L (T + d) active (surplus d (Nat.lt_of_succ_le bound)))

/-! ## Two pulses -/

/-- Two histories from level 2, sustaining need 2, focal need 1, renewal 1: only the first draw
differs, and one unit is contributed at every later step. -/
def pulse (firstDraw : Nat) : Law :=
  ⟨2, 1, 2, 1, (fun | 0 => firstDraw | _ + 1 => 0), (fun | 0 => 0 | _ + 1 => 1)⟩

/-- **The two pulses draw and contribute the same after the first step.** -/
theorem same_later_inputs (n : Nat) :
    (pulse 2).draw (n + 1) = (pulse 3).draw (n + 1) ∧
      (pulse 2).contrib (n + 1) = (pulse 3).contrib (n + 1) :=
  ⟨rfl, rfl⟩

/-- **The levels of the two pulses**: both start at 2; the supported pulse falls to 1 and returns
to 2, the unsupported one falls to 0. The web's level is the law's. -/
theorem pulse_levels :
    (SupportGated.web (pulse 2)).level 0 () = 2 ∧ (SupportGated.web (pulse 3)).level 0 () = 2 ∧
      (SupportGated.web (pulse 2)).level 1 () = 1 ∧ (SupportGated.web (pulse 3)).level 1 () = 0 ∧
      (SupportGated.web (pulse 2)).level 2 () = 2 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

/-- **The supported pulse stays at the sustaining need from step 2 on.** -/
theorem supported_pulse_recovers (n : Nat) : 2 ≤ (pulse 2).level (2 + n) := by
  have grow := window_progress (pulse 2) 1 (n + 1) (Nat.le_refl 1)
    (fun d _ => by rw [Nat.add_comm 1 d]; exact Nat.zero_lt_one) (n + 1) (Nat.le_refl _)
  have index : 1 + (n + 1) = 2 + n := Nat.add_right_comm 1 n 1
  rw [index] at grow
  exact Nat.le_trans (Nat.succ_le_succ (Nat.le_add_right 1 n)) grow

/-- **The unsupported pulse stays at 0 from step 1 on, with every formation inactive** on its
web. -/
theorem unsupported_pulse_ends (n : Nat) :
    (SupportGated.web (pulse 3)).level (1 + n) () = 0 ∧
      ∀ p, ¬ (SupportGated.web (pulse 3)).active (1 + n) p :=
  have zero : (pulse 3).level (1 + n) = 0 :=
    absorbs (pulse 3) 1 Nat.zero_lt_one Nat.zero_lt_two n
  ⟨zero, fun p => match p with
    | .focal => fun active => Nat.not_succ_le_zero 0 (Nat.le_trans active (Nat.le_of_eq zero))
    | .sustaining => fun active => Nat.not_succ_le_zero 1 (Nat.le_trans active (Nat.le_of_eq zero))⟩

/-- **The recovered history is neither class**: a temporary loss followed by lasting restoration
is neither renewing at all times nor consuming for good. -/
theorem recovered_neither :
    ¬ RenewingIn (pulse 2).unfolding .focal ∧ ¬ ConsumingIn (pulse 2).unfolding .focal :=
  ⟨fun renewing => Nat.not_succ_le_self 1
      (renewing () (Or.inl Nat.zero_lt_one) 1 .sustaining trivial),
   fun ⟨_, _, g, T, _, lost⟩ =>
    have high := supported_pulse_recovers T
    have low := lost (2 + T) (Nat.le_add_left T 2)
    match g, low with
    | .focal, low => Nat.not_le_of_gt low (Nat.le_trans (Nat.le_succ 1) high)
    | .sustaining, low => Nat.not_le_of_gt low high⟩

/-- The recovered history is neither class on its web. -/
theorem recovered_web_neither :
    ¬ (SupportGated.web (pulse 2)).RenewingIn .focal ∧
      ¬ (SupportGated.web (pulse 2)).ConsumingIn .focal :=
  ⟨fun renewing => recovered_neither.1 ((Web.static_renewingIn _ _).mp renewing),
   fun consuming => recovered_neither.2 ((Web.static_consumingIn _ _).mp consuming)⟩

end SupportRecovery

end Becoming
