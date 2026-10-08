import GenerativeOutcomeModel
import NondualCore

/-!
# Nondual description interface of the existing generative model

This additive entry imports the existing public model and its endpoint-sensitive
continuations unchanged. It requires no Actor, Patient or moral orientation.
Descriptions remain supplied mathematical readouts. An acquired description
that changes the process must have its own physical realization inside the law.
The history carrier retains start, word and endpoint with a Trace proof; it does
not distinguish all hidden branches sharing those data.
-/

namespace Generative.Model

open NondualCore
universe u v w x

/-- A supplied description of a realized history neither creates nor removes
    finite continuations, including their actual final state. -/
theorem nondual_history_description_exact
    {S : Type u} {E : Type v} {D : Type w}
    (P : Process S E) (describe : ActualHistory P → D)
    (h : ActualHistory P) (events : List E) (endpoint : S) :
    Trace P h.finish events endpoint ↔
      ∃ k, Trace (presentedProcess (historyProcess P) describe)
        (present describe h) events (present describe k) ∧ k.finish = endpoint := by
  constructor
  · intro actual
    obtain ⟨k, continued, final⟩ := (history_continuations_exact h events endpoint).mp actual
    exact ⟨k, (described_history_continuations_exact describe h k events).mpr continued, final⟩
  · rintro ⟨k, described, final⟩
    exact (history_continuations_exact h events endpoint).mpr
      ⟨k, (described_history_continuations_exact describe h k events).mp described, final⟩

/-- Role annotation preserves the model's existing endpoint outcome question.
    This is stronger than preservation of event-word feasibility alone, but
    supplies neither the readout's physical sensor nor an ethical evaluation. -/
theorem nondual_description_preserves_outcome
    {S : Type u} {E : Type v} {D : Type w} {O : Type x}
    (P : Process S E) (describe : S → D) (initial : S)
    (observe : S → O) (past future : List E) (outcome : O) :
    OutcomeContinuation.OutcomeResidual (presentedProcess P describe)
      (present describe initial) (fun z => observe (forget z)) past future outcome ↔
    OutcomeContinuation.OutcomeResidual P initial observe past future outcome := by
  constructor
  · rintro ⟨endpoint, actual, observed⟩
    exact ⟨forget endpoint,
      (presented_trace_exact P describe (present describe initial) endpoint
        (past ++ future)).mp actual, observed⟩
  · rintro ⟨endpoint, actual, observed⟩
    exact ⟨present describe endpoint,
      (presented_trace_exact P describe (present describe initial)
        (present describe endpoint) (past ++ future)).mpr actual, observed⟩

end Generative.Model

#print axioms Generative.Model.nondual_history_description_exact
#print axioms Generative.Model.nondual_description_preserves_outcome
