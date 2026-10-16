import OutcomeContinuation
import ConstructiveDecisions

/-!
# A connected operational continuation of the generative model

This additive entry point uses the original Process/Trace semantics. It joins
the reached acquired-successor history to an outcome-sensitive root contract,
and installs equivalent constructive decisions in a full identification-process
view. It does not modify any frozen original law or claim that its supplied laws,
initialization, practical grounds or authority have been derived without premises.
-/

namespace Generative.Connected

open ConstructiveDecisions

/-- The same validity condition, using the exhaustively defined escrow function. -/
def identificationValid (s : RecipientIdentification.State) : Prop :=
  s.hardware.q < 4 ∧ s.escrow = requiredEscrow s.phase

/-- An executable presentation of the existing complete identification process.
The full-domain equivalence below is required; no desired transition is added. -/
def identificationProcess (laws : RecipientCorrection.Laws) :
    Process RecipientIdentification.State RecipientIdentification.Event where
  step s e t := identificationValid s ∧ RecipientIdentification.Enabled s e ∧
    t = identificationAdvance laws s e

theorem identification_step_iff (laws : RecipientCorrection.Laws)
    (s t : RecipientIdentification.State) (e : RecipientIdentification.Event) :
    (identificationProcess laws).step s e t ↔ RecipientIdentification.Step laws s e t := by
  change (s.hardware.q < 4 ∧ s.escrow = requiredEscrow s.phase) ∧
      RecipientIdentification.Enabled s e ∧ t = identificationAdvance laws s e ↔
    (s.hardware.q < 4 ∧ s.escrow = RecipientIdentification.requiredEscrow s.phase) ∧
      RecipientIdentification.Enabled s e ∧ t = RecipientIdentification.advance laws s e
  rw [requiredEscrow_eq, identificationAdvance_eq]

theorem identification_histories_iff (laws : RecipientCorrection.Laws)
    (s t : RecipientIdentification.State) (events : List RecipientIdentification.Event) :
    Trace (identificationProcess laws) s events t ↔
      Trace (RecipientIdentification.process laws) s events t := by
  constructor
  · intro history
    induction history with
    | nil s => exact .nil s
    | cons step _ ih => exact .cons ((identification_step_iff laws _ _ _).mp step) ih
  · intro history
    induction history with
    | nil s => exact .nil s
    | cons step _ ih => exact .cons ((identification_step_iff laws _ _ _).mpr step) ih

/-- The replacement preserves every actual boundary and endpoint observation,
including records, recipient effects and resources, over the same event words. -/
theorem identification_outcomes_iff {Outcome : Type}
    (laws : RecipientCorrection.Laws) (initial : RecipientIdentification.State)
    (observe : RecipientIdentification.State → Outcome)
    (past future : List RecipientIdentification.Event) (outcome : Outcome) :
    OutcomeContinuation.OutcomeResidual (identificationProcess laws) initial observe past future outcome ↔
      OutcomeContinuation.OutcomeResidual (RecipientIdentification.process laws) initial observe past future outcome := by
  constructor
  · rintro ⟨endpoint, history, observed⟩
    exact ⟨endpoint, (identification_histories_iff laws _ _ _).mp history, observed⟩
  · rintro ⟨endpoint, history, observed⟩
    exact ⟨endpoint, (identification_histories_iff laws _ _ _).mpr history, observed⟩

end Generative.Connected

#print axioms Generative.Connected.identificationValid
#print axioms Generative.Connected.identificationProcess
#print axioms Generative.Connected.identification_step_iff
#print axioms Generative.Connected.identification_histories_iff
#print axioms Generative.Connected.identification_outcomes_iff
