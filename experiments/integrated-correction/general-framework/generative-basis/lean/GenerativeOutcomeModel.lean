import GenerativeModel
import OutcomeContinuation

/-!
# Outcome-sensitive extension of the existing generative model

This entry imports the shared model unchanged, preserving parallel acquisition
work. It joins its feasible-history interface to endpoint-sensitive outcomes.
Concrete native acquisition is checked in AcquiredPredictionRecord, which uses
the same outcome interface without adding a physical or ethical law.
-/

namespace Generative.Model

open Deeper
universe u v w

/-- Outcome records have an exactness obligation at least as strong as records
of feasible words. The endpoint readout remains an explicit interpretation. -/
theorem outcome_record_exactness_iff
    {State : Type u} {Action : Type v} {Outcome Summary : Type w}
    (P : Process State Action) (initial : State) (observe : State → Outcome)
    (record : List Action → Summary) :
    (∃ accept, OutcomeContinuation.ExactOutcomeSummary P initial observe record accept) ↔
      ∀ past other, record past = record other →
        OutcomeContinuation.SameOutcomeProfile P initial observe past other :=
  OutcomeContinuation.exact_outcome_summary_exists_iff record

/-- Forgetting endpoint readouts returns the old feasible-future interface. -/
theorem outcome_agreement_preserves_feasible_future_agreement
    {State : Type u} {Action : Type v} {Outcome : Type w}
    {P : Process State Action} {initial : State} {observe : State → Outcome}
    {past other : List Action}
    (h : OutcomeContinuation.SameOutcomeProfile P initial observe past other) :
    SelfFormation.SameProfile P initial past other := by
  intro future
  exact OutcomeContinuation.outcome_profiles_retain_feasibility h future

/-- The old same-word counterexample has distinct endpoint outcomes. This is a
fixed-law witness, not an acquired sensor or a moral ranking. -/
theorem same_words_can_have_different_outcomes :
    (∀ s (word : List Unit), Feasible static s word ↔ Feasible toggle s word) ∧
    OutcomeContinuation.OutcomeResidual static false (fun s => s) [] [()] false ∧
    ¬ OutcomeContinuation.OutcomeResidual toggle false (fun s => s) [] [()] false := by
  refine ⟨static_toggle_same_feasible, ?_, ?_⟩
  · exact ⟨false, static_toggle_singleton_endpoints_differ.1, rfl⟩
  · intro h
    exact static_toggle_singleton_endpoints_differ.2
      ((OutcomeContinuation.identity_outcome_iff_trace [] [()] false).mp h)

end Generative.Model

#print axioms Generative.Model.outcome_record_exactness_iff
#print axioms Generative.Model.outcome_agreement_preserves_feasible_future_agreement
#print axioms Generative.Model.same_words_can_have_different_outcomes
