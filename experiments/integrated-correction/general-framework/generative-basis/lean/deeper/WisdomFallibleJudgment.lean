import WisdomResponseStructure

/-!
Claim-relative adequacy in the existing three-route process. The lists below
are supplied finite event laws with equal weights per entry, not observations
that estimate a future law. Duplicate modes record distinct weighted events.
The one-third bound is a numerical specification, not an ethical permission.
Only the mode/result projection of a history is used in the endpoint test.
-/

namespace Generative.WisdomFallibleJudgment
open CorePredication ContextualWisdom WisdomResponseStructure

def uniformLaw : List Mode := [0, 1, 2]
def biasedLaw : List Mode := [0, 0, 1, 2]

/-- The inherited assured_route_iff identifies a = m with failed arrival. -/
def failureWeight (law : List Mode) (a : Route) : Nat :=
  (law.filter (fun m => decide (a = m))).length

def WithinThird (law : List Mode) (a : Route) : Prop :=
  0 < law.length ∧ 3 * failureWeight law a ≤ law.length

instance (law : List Mode) (a : Route) : Decidable (WithinThird law a) :=
  inferInstanceAs (Decidable (0 < law.length ∧ 3 * failureWeight law a ≤ law.length))

theorem uniform_failure_weight (a : Route) : failureWeight uniformLaw a = 1 := by
  have finite : ∀ b : Fin 3, failureWeight uniformLaw b = 1 := by decide
  exact finite a

theorem bounded_risk_without_uniform_completion (a : Route) :
    WithinThird uniformLaw a ∧ a ∈ uniformLaw ∧
    ¬ Assured routes [a] Reached (a, false) ∧
    ¬ (∀ m : Mode, Assured routes [a] Reached (m, false)) := by
  have member : ∀ b : Fin 3, b ∈ uniformLaw := by decide
  have fails : ¬ Assured routes [a] Reached (a, false) := by
    rw [assured_route_iff]
    exact fun h => h rfl
  refine ⟨?_, member a, fails, fun all => fails (all a)⟩
  unfold WithinThird
  rw [uniform_failure_weight]
  decide

theorem biased_bound_fails :
    failureWeight biasedLaw 0 = 2 ∧ ¬ WithinThird biasedLaw 0 := by decide

theorem matching_realizations_with_different_certificates :
    WithinThird uniformLaw 0 ∧ ¬ WithinThird biasedLaw 0 ∧
    0 ∈ uniformLaw ∧ 0 ∈ biasedLaw ∧ 1 ∈ uniformLaw ∧ 1 ∈ biasedLaw ∧
    ¬ Assured routes [0] Reached (0, false) ∧
    Assured routes [0] Reached (1, false) := by
  refine ⟨(bounded_risk_without_uniform_completion 0).1, biased_bound_fails.2,
    by decide, by decide, by decide, by decide, ?_, ?_⟩
  · simp [assured_route_iff]
  · simp [assured_route_iff]

theorem no_endpoint_only_prior_certificate :
    ¬ ∃ judge : State → Bool,
      ∀ law ∈ [uniformLaw, biasedLaw], ∀ m ∈ law,
        judge (advance (m, false) 0) = decide (WithinThird law 0) := by
  rintro ⟨judge, correct⟩
  have uniform := correct uniformLaw (by simp) 1 (by decide)
  have biased := correct biasedLaw (by simp) 1 (by decide)
  have same : decide (WithinThird uniformLaw 0) = decide (WithinThird biasedLaw 0) :=
    uniform.symm.trans biased
  have unequal : decide (WithinThird uniformLaw 0) ≠ decide (WithinThird biasedLaw 0) := by decide
  exact unequal same

#print axioms Generative.WisdomFallibleJudgment.uniform_failure_weight
#print axioms Generative.WisdomFallibleJudgment.bounded_risk_without_uniform_completion
#print axioms Generative.WisdomFallibleJudgment.biased_bound_fails
#print axioms Generative.WisdomFallibleJudgment.matching_realizations_with_different_certificates
#print axioms Generative.WisdomFallibleJudgment.no_endpoint_only_prior_certificate

end Generative.WisdomFallibleJudgment
