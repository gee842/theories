import Becoming.RenewalBridge

/-!
# The support-gated family's pulses and courses on their webs

`RelationalRenewal` classifies a formation by its relation to the conditions it participates
in. `Becoming.RenewalFlow` shows every law of its support-gated family balanced by a flow on its
static web (`SupportGated.web`) and states the family's classification results of the webs.
`RenewalRecovery` gives two pulses of the family, one recovering and one ending, and
`RenewalComparison` reads the course without the focal formation as an unfolding. This module
states those results of the webs.

* **Two pulses.** The levels of the webs of the two pulses (`pulse_levels`), and on the
  unsupported pulse the level stays 0 and every formation is inactive from step 1 on
  (`unsupported_pulse_ends`).
* **The course without the focal formation** is a dependent web (`absent_dependent`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace SupportGatedWebs

open RelationalRenewal RelationalRenewal.Law

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
