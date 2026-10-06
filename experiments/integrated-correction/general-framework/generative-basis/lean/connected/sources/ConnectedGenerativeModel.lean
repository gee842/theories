import GenerativeOutcomeModel
import ConnectedModel
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

/-- An admitted write uses the actual acquired recipient receipt in its native
updater and pays the original escrow cost; it cannot choose a substitute label. -/
theorem acquired_recipient_record_is_used
    {laws : RecipientCorrection.Laws} {s t : RecipientIdentification.State}
    (received : Bool) (step : (identificationProcess laws).step s .write t)
    (recorded : s.phase = .acquired .recipient (some received)) :
    t.hardware = RecipientIdentification.setRegisters s.hardware
      (RecipientIdentification.revise (RecipientIdentification.registers s.hardware) received) ∧
    t.patient = s.patient ∧ t.escrow = s.escrow - 2 := by
  rcases step with ⟨_, _, rfl⟩
  constructor
  · change RecipientIdentification.setRegisters s.hardware
        (feedback (RecipientIdentification.registers s.hardware)
          (targetOf s.phase) (acquiredRecord s.phase)) = _
    rw [recorded]
    rfl
  · exact ⟨rfl, rfl⟩

/-- An absent receipt does not become negative feedback. The existing register
value is written and the same recording cost is still paid. -/
theorem missing_receipt_writes_existing_registers
    {laws : RecipientCorrection.Laws} {s t : RecipientIdentification.State}
    (step : (identificationProcess laws).step s .write t)
    (recorded : s.phase = .acquired .recipient none) :
    t.hardware = RecipientIdentification.setRegisters s.hardware
      (RecipientIdentification.registers s.hardware) ∧
    t.patient = s.patient ∧ t.escrow = s.escrow - 2 := by
  rcases step with ⟨_, _, rfl⟩
  constructor
  · change RecipientIdentification.setRegisters s.hardware
        (feedback (RecipientIdentification.registers s.hardware)
          (targetOf s.phase) (acquiredRecord s.phase)) = _
    rw [recorded]
    rfl
  · exact ⟨rfl, rfl⟩

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

/-- A root outcome claim at the actual acquired successor's cut. This applies
to every finite admitted continuation, not merely the displayed settlement. -/
theorem acquired_cut_bounds_every_recorded_outcome
    (events : List EvaluativeSuccession.Event) (credit : Nat)
    (observed : OutcomeContinuation.OutcomeResidual
      (EvaluativeSuccession.process SuccessionWitness.changed)
      ConnectedModel.Actual.cutAfterWork (fun s => s.core.patient) [] events credit) :
    credit = 80 := by
  rcases observed with ⟨endpoint, history, value⟩
  have retained := ConnectedModel.Actual.actual_cut_all_continuations history
  exact value.symm.trans retained.2

end Generative.Connected

#print axioms Generative.Connected.identificationValid
#print axioms Generative.Connected.identificationProcess
#print axioms Generative.Connected.acquired_recipient_record_is_used
#print axioms Generative.Connected.missing_receipt_writes_existing_registers
#print axioms Generative.Connected.identification_step_iff
#print axioms Generative.Connected.identification_histories_iff
#print axioms Generative.Connected.identification_outcomes_iff
#print axioms Generative.Connected.acquired_cut_bounds_every_recorded_outcome
