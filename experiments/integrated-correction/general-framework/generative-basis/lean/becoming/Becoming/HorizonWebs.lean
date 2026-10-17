import Becoming.Horizon

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
-/

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
