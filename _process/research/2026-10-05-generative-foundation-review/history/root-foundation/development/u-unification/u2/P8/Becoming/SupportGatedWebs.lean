import Becoming.RenewalBridge

/-!
# The support-gated family on its webs

`RelationalRenewal` classifies a formation by its relation to the conditions it participates
in, and states for its support-gated family that formation does not decide the class, that a
formation's own trajectory does not, that formations each within renewal can consume jointly
and that escalation consumes; its seasonal unfolding is neither renewing nor consuming.
`RenewalRecovery` gives two pulses of the family, one recovering and one ending.
`RenewalComparison` reads the course without the focal formation as an unfolding.
`Becoming.RenewalBridge` shows every law of the family balanced by a flow on its static web
(`SupportGated.web`), and `Web.static` reads every unfolding as a web whose dependence,
renewal and consumption are the unfolding's (`Web.static_dependent`, `Web.static_renewingIn`,
`Web.static_consumingIn`). This module states those results of the webs.

* **Formation does not decide the class.** On the web of every law of the family a step at
  which the focal formation is active forms one unit; the web of cultivation is renewing and
  forms at every step, while the web of malignant growth is consuming and its focal formation
  ends with bounded formation (`formation_does_not_decide`).
* **The own trajectory does not decide.** The webs of sharing and of winning have the focal
  formation active at the same steps with the same formation, and one is renewing, the other
  consuming (`own_trajectory_does_not_decide`).
* **Joint consumption.** Two formations each within renewal alone are renewing on their webs,
  while their joint web is consuming and both formations end there (`jointly_consuming`).
* **Escalation.** A draw that grows past renewal consumes on its web and its focal formation
  ends with bounded formation (`escalation_consumes`).
* **Neither class.** The seasonal web is dependent and neither renewing nor consuming
  (`fluctuating_dependent`, `fluctuating_neither`).
* **Two pulses.** The levels of the webs of the two pulses (`pulse_levels`), and on the
  unsupported pulse the level stays 0 and every formation is inactive from step 1 on
  (`unsupported_pulse_ends`).
* **The course without the focal formation** is a dependent web (`absent_dependent`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace SupportGatedWebs

open RelationalRenewal RelationalRenewal.Law

/-- **Formation does not decide the class, on the webs of the family.** -/
theorem formation_does_not_decide :
    (∀ L : Law, ∀ t, (SupportGated.web L).active t .focal → L.formed (t + 1) = L.formed t + 1) ∧
    ((SupportGated.web cultivation).RenewingIn .focal ∧ ∀ t, cultivation.formed t = t) ∧
    (malignant.formed 1 = 1 ∧ (SupportGated.web malignant).ConsumingIn .focal ∧
      ∃ T, (∀ t, T ≤ t → ¬ (SupportGated.web malignant).active t .focal) ∧
        ∀ t, malignant.formed t ≤ T) :=
  match Law.formation_does_not_decide with
  | ⟨forms, ⟨renewing, always⟩, ⟨one, consuming, ends⟩⟩ =>
    ⟨forms, ⟨(Web.static_renewingIn _ _).mpr renewing, always⟩,
     ⟨one, (Web.static_consumingIn _ _).mpr consuming, ends⟩⟩

/-- **The focal formation's own trajectory does not decide the class, on the webs of sharing
and winning.** -/
theorem own_trajectory_does_not_decide :
    (∀ t, (SupportGated.web sharing).active t .focal ↔
      (SupportGated.web winning).active t .focal) ∧
    (∀ t, sharing.formed t = winning.formed t) ∧
    (SupportGated.web sharing).RenewingIn .focal ∧
      (SupportGated.web winning).ConsumingIn .focal :=
  match Law.own_trajectory_does_not_decide with
  | ⟨same, formed, renewing, consuming⟩ =>
    ⟨same, formed, (Web.static_renewingIn _ _).mpr renewing,
     (Web.static_consumingIn _ _).mpr consuming⟩

/-- **Formations each within renewal alone consume jointly, on their webs**, and both end on the
joint web. -/
theorem jointly_consuming (start renew need : Nat) (d1 d2 : Nat → Nat)
    (within1 : ∀ t, d1 t ≤ renew) (within2 : ∀ t, d2 t ≤ renew)
    (joint : ∀ t, renew < d1 t + d2 t) (positive : 0 < need) (supported : need ≤ start) :
    (SupportGated.web (alone start renew need d1)).RenewingIn .focal ∧
    (SupportGated.web (alone start renew need d2)).RenewingIn .focal ∧
    (SupportGated.web (together start renew need d1 d2)).ConsumingIn .focal ∧
    ∃ T, ∀ t, T ≤ t → ¬ (SupportGated.web (together start renew need d1 d2)).active t .focal ∧
      ¬ (SupportGated.web (together start renew need d1 d2)).active t .sustaining :=
  match Law.jointly_consuming start renew need d1 d2 within1 within2 joint positive supported with
  | ⟨first, second, consuming, ends⟩ =>
    ⟨(Web.static_renewingIn _ _).mpr first, (Web.static_renewingIn _ _).mpr second,
     (Web.static_consumingIn _ _).mpr consuming, ends⟩

/-- **Escalation that begins within renewal consumes on its web**, and its focal formation ends
with bounded formation. -/
theorem escalation_consumes :
    (∀ t, t ≤ 2 → escalation.draw t ≤ escalation.renew + escalation.contrib t) ∧
    (SupportGated.web escalation).level 3 () = 6 ∧ escalation.formed 3 = 3 ∧
    (SupportGated.web escalation).ConsumingIn .focal ∧
    ∃ T, (∀ t, T ≤ t → ¬ (SupportGated.web escalation).active t .focal) ∧
      ∀ t, escalation.formed t ≤ T :=
  match Law.escalation_consumes with
  | ⟨within, level, formed, consuming, ends⟩ =>
    ⟨within, level, formed, (Web.static_consumingIn _ _).mpr consuming, ends⟩

/-- **The seasonal web is dependent.** -/
theorem fluctuating_dependent : (Web.static fluctuating).Dependent :=
  (Web.static_dependent _).mpr RelationalRenewal.fluctuating_dependent

/-- **The seasonal web is neither renewing nor consuming**: the classification is not a
dichotomy. -/
theorem fluctuating_neither :
    ¬ (Web.static fluctuating).RenewingIn () ∧ ¬ (Web.static fluctuating).ConsumingIn () :=
  match RelationalRenewal.fluctuating_neither with
  | ⟨notRenewing, notConsuming⟩ =>
    ⟨fun renewing => notRenewing ((Web.static_renewingIn _ _).mp renewing),
     fun consuming => notConsuming ((Web.static_consumingIn _ _).mp consuming)⟩

/-- **The levels of the two pulses' webs**: both start at 2, the supported pulse falls to 1 and
returns to 2, the unsupported one falls to 0. -/
theorem pulse_levels :
    (SupportGated.web (RenewalRecovery.pulse 2)).level 0 () = 2 ∧
    (SupportGated.web (RenewalRecovery.pulse 3)).level 0 () = 2 ∧
    (SupportGated.web (RenewalRecovery.pulse 2)).level 1 () = 1 ∧
    (SupportGated.web (RenewalRecovery.pulse 3)).level 1 () = 0 ∧
    (SupportGated.web (RenewalRecovery.pulse 2)).level 2 () = 2 :=
  RenewalRecovery.two_actual_pulses

/-- **On the web of the unsupported pulse the level stays 0 and every formation is inactive
from step 1 on.** -/
theorem unsupported_pulse_ends (n : Nat) :
    (SupportGated.web (RenewalRecovery.pulse 3)).level (1 + n) () = 0 ∧
      ∀ p, ¬ (SupportGated.web (RenewalRecovery.pulse 3)).active (1 + n) p :=
  have zero := RenewalRecovery.unsupported_pulse_never_recovers n
  ⟨zero, fun p => match p with
    | .focal => fun active => Nat.not_succ_le_zero 0 (Nat.le_trans active (Nat.le_of_eq zero))
    | .sustaining => fun active => Nat.not_succ_le_zero 1 (Nat.le_trans active (Nat.le_of_eq zero))⟩

/-- **The course without the focal formation is a dependent web.** -/
theorem absent_dependent (L : Law) : (Web.static (RenewalComparison.absent L)).Dependent :=
  (Web.static_dependent _).mpr (RenewalComparison.absent_dependent L)

end SupportGatedWebs

end Becoming
