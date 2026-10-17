import Becoming.ReachableFrames

/-!
# A certified positive integral over a policy's scope (periphery-join ring)

`PositiveGroundUncertainty` proves that a positive finite signed integral of occurrences, each
positive occurrence corresponding to new generative content, secures positive ground and, with a
direct articulation, a contributory reason at every admitted continuation
(`certified_integral_supplies_contributory_reason`). `Becoming.Bridge` reads the inventory off a
frame (`Frame.inventory`, with living significance `G0` on the frame) and the admitted
continuations of an inquiry as the scope of a policy (`Scope`). This module states the law of
that reading.

* **A certified integral over a policy's scope.** Under living significance on a frame, where
  every configuration of a policy's scope has a positive integral of occurrences and each
  positively contributing occurrence there means a living claim the configuration realizes and
  lacked before, every configuration of the scope holds positively relevant new content and has
  the articulated reason (`certified_reason_on_scope`).

No ranking occurs; living significance and the articulation are named hypotheses. Axioms
inherited: `propext` and `Quot.sound`, from
`PositiveGroundUncertainty.certified_integral_supplies_contributory_reason`; nothing else.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

namespace ReachableFramesInherited

/-- **A certified integral over a policy's scope.** Under living significance on a frame, with a
reason articulated from positive relevance, where every configuration the policy's executions
reach has a positive finite integral of occurrences, and each positively contributing occurrence
there means a living claim realized at that configuration and absent before, every configuration
of the scope holds positively relevant content absent before and has the reason. -/
theorem certified_reason_on_scope {S A C R O : Type} {k : Nat} (F : Frame S A C)
    (living : C → Prop) {sense : S → A → S → Fin k} {response : R → List A} {B : S → Prop}
    {policy : Policy A R k} (before : S → C → Prop) (positive : S → C → Prop)
    (reason : S → Prop) (g0 : G0 F living positive) (articulate : ∀ t c, positive t c → reason t)
    (domain : List O) (contribution : S → O → Int) (meaning : O → C)
    (correspondence : ∀ t, Scope F.P sense response B policy t → ∀ o, o ∈ domain →
      0 < contribution t o → living (meaning o) ∧ F.realized t (meaning o) ∧ ¬ before t (meaning o))
    (certificate : ∀ t, Scope F.P sense response B policy t →
      0 < PositiveGroundUncertainty.finiteIntegral domain (contribution t)) :
    ∀ t, Scope F.P sense response B policy t → (∃ c, positive t c ∧ ¬ before t c) ∧ reason t :=
  PositiveGroundUncertainty.certified_integral_supplies_contributory_reason
    (Scope F.P sense response B policy) before (F.inventory living) positive reason g0 articulate
    domain contribution meaning correspondence certificate

end ReachableFramesInherited

end Becoming
