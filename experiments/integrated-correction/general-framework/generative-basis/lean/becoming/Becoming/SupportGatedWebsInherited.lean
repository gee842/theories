import Becoming.SupportGatedWebs

/-!
# Recovery on the support-gated webs, through the periphery's proofs

`RenewalRecovery` states recovery within the support-gated family: repair by an active focal
formation contributing more than it draws restores the sustaining need within the deficit; two
pulses with the same later inputs, one recovering and one ending; and the recovered history is
neither renewing nor consuming. This module states those results of the family's static webs
(`SupportGated.web`). `Becoming.RenewalBridge` derives the restoration from `Flow.restores`
without axioms (`SupportGated.repair_restores`); the joins here go through the periphery
theorems.

* **Repair reactivates the sustaining formation**: where the focal formation is active on the web
  and contributes more than it draws at each step of the deficit, the sustaining formation is
  active on the web once the deficit is repaired (`repair_reactivates`).
* **Same later inputs, opposite futures.** The two pulses draw and contribute the same after the
  first step, while the web of the supported pulse stays at the sustaining need from step 2 on and
  the web of the unsupported pulse stays at 0 from step 1 on (`same_inputs_opposite_futures`).
* **Recovery is neither class**: the web of the supported pulse is neither renewing nor consuming
  for its focal formation (`recovered_neither`).

This module inherits `propext` and `Quot.sound` from
`RenewalRecovery.repair_restores_sustaining_support`, `RenewalRecovery.supported_pulse_recovers`
and `RenewalRecovery.recovered_history_neither_global_class`, and `propext` from
`RenewalRecovery.same_future_inputs`; it adds no axiom of its own. No ethical predicate or
ranking occurs.
-/

namespace Becoming

namespace SupportGatedWebsInherited

open RelationalRenewal RelationalRenewal.Law

/-- **Repair reactivates the sustaining formation on the web.** -/
theorem repair_reactivates (L : Law) (T : Nat) (fOn : (SupportGated.web L).active T .focal)
    (surplus : ∀ d, d < L.needG - (SupportGated.web L).level T () →
      L.draw (T + d) < L.contrib (T + d)) :
    (SupportGated.web L).active (T + (L.needG - (SupportGated.web L).level T ())) .sustaining :=
  RenewalRecovery.repair_restores_sustaining_support L T fOn surplus

/-- **Same later inputs, opposite futures**: the two pulses draw and contribute the same after the
first step; the supported pulse's web stays at the sustaining need from step 2 on and the
unsupported pulse's web at 0 from step 1 on. -/
theorem same_inputs_opposite_futures (n : Nat) :
    (RenewalRecovery.pulse 2).draw (n + 1) = (RenewalRecovery.pulse 3).draw (n + 1) ∧
    (RenewalRecovery.pulse 2).contrib (n + 1) = (RenewalRecovery.pulse 3).contrib (n + 1) ∧
    (RenewalRecovery.pulse 2).needG ≤ (SupportGated.web (RenewalRecovery.pulse 2)).level (2 + n) () ∧
    (SupportGated.web (RenewalRecovery.pulse 3)).level (1 + n) () = 0 :=
  match RenewalRecovery.same_future_inputs n with
  | ⟨draws, contributes⟩ => ⟨draws, contributes, RenewalRecovery.supported_pulse_recovers n,
      RenewalRecovery.unsupported_pulse_never_recovers n⟩

/-- **The recovered history is neither class on its web.** -/
theorem recovered_neither :
    ¬ (SupportGated.web (RenewalRecovery.pulse 2)).RenewingIn .focal ∧
      ¬ (SupportGated.web (RenewalRecovery.pulse 2)).ConsumingIn .focal :=
  match RenewalRecovery.recovered_history_neither_global_class with
  | ⟨notRenewing, notConsuming⟩ =>
    ⟨fun renewing => notRenewing ((Web.static_renewingIn _ _).mp renewing),
     fun consuming => notConsuming ((Web.static_consumingIn _ _).mp consuming)⟩

end SupportGatedWebsInherited

end Becoming
