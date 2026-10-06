import RecipientIdentification

/-!
# What the cumulative patient coordinate does and does not represent

In the unchanged identification law, patient is accumulated resource credit.
Translation of that credit leaves admissibility and every other coordinate's
updates unchanged, while remaining visible in patient outcomes and total energy.
This localizes a representational omission: this process alone does not model
a recipient's own continuing organization or need-dependent response. It does
not prove that real recipients lack those relations or that significance is
external to generative activity. No revised law is installed here.
-/

namespace Generative.RecipientContinuationProjection

open RecipientIdentification

def shiftPatient (amount : Nat) (s : State) : State :=
  {s with patient := s.patient + amount}

theorem shift_preserves_control_coordinates (amount : Nat) (s : State) :
    (shiftPatient amount s).hardware = s.hardware ∧
    (shiftPatient amount s).packets = s.packets ∧
    (shiftPatient amount s).escrow = s.escrow ∧
    (shiftPatient amount s).phase = s.phase ∧
    (shiftPatient amount s).active = s.active := ⟨rfl, rfl, rfl, rfl, rfl⟩

theorem enabled_ignores_patient_amount (amount : Nat) (s : State) (event : Event) :
    RecipientIdentification.Enabled (shiftPatient amount s) event ↔
      RecipientIdentification.Enabled s event := by
  cases event <;> rfl

theorem valid_ignores_patient_amount (amount : Nat) (s : State) :
    Valid (shiftPatient amount s) ↔ Valid s := Iff.rfl

theorem advance_commutes_with_patient_shift (laws : RecipientCorrection.Laws)
    (amount : Nat) (s : State) (event : Event) :
    advance laws (shiftPatient amount s) event = shiftPatient amount (advance laws s event) := by
  cases event <;>
    simp [shiftPatient, advance, returned, issued, Nat.add_assoc, Nat.add_comm]

theorem shift_patient_injective (amount : Nat) {s t : State}
    (same : shiftPatient amount s = shiftPatient amount t) : s = t := by
  cases s with
  | mk sh sp sn se sc sa =>
    cases t with
    | mk th tp tn te tc ta =>
      have hardware := congrArg State.hardware same
      have patient := congrArg State.patient same
      have packets := congrArg State.packets same
      have escrow := congrArg State.escrow same
      have phase := congrArg State.phase same
      have active := congrArg State.active same
      change sh = th at hardware
      change sp + amount = tp + amount at patient
      change sn = tn at packets
      change se = te at escrow
      change sc = tc at phase
      change sa = ta at active
      have balance : sp = tp := Nat.add_right_cancel patient
      cases hardware
      cases balance
      cases packets
      cases escrow
      cases phase
      cases active
      rfl

/-- Exactly the same step remains possible at a translated patient balance. -/
theorem step_shift_iff (laws : RecipientCorrection.Laws) (amount : Nat)
    (s t : State) (event : Event) :
    Step laws (shiftPatient amount s) event (shiftPatient amount t) ↔
      Step laws s event t := by
  constructor
  · rintro ⟨valid, enabled, result⟩
    refine ⟨valid, (enabled_ignores_patient_amount amount s event).mp enabled, ?_⟩
    apply shift_patient_injective amount
    exact result.trans (advance_commutes_with_patient_shift laws amount s event)
  · rintro ⟨valid, enabled, result⟩
    exact ⟨valid, (enabled_ignores_patient_amount amount s event).mpr enabled,
      (congrArg (shiftPatient amount) result).trans
        (advance_commutes_with_patient_shift laws amount s event).symm⟩

theorem trace_patient_shift {laws : RecipientCorrection.Laws} (amount : Nat)
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) :
    Trace (process laws) (shiftPatient amount s) events (shiftPatient amount t) := by
  induction history with
  | nil s => exact .nil _
  | cons step _ ih => exact .cons ((step_shift_iff laws amount _ _ _).mpr step) ih

/-- A shifted trace from this exact shifted start has an actual unshifted
counterpart, rather than an arbitrary endpoint chosen independently. -/
theorem trace_from_shifted_start {laws : RecipientCorrection.Laws} (amount : Nat)
    {s t : State} {events : List Event}
    (history : Trace (process laws) (shiftPatient amount s) events t) :
    ∃ original, Trace (process laws) s events original ∧ t = shiftPatient amount original := by
  induction events generalizing s t with
  | nil =>
    have same := trace_nil_iff.mp history
    exact ⟨s, .nil _, same.symm⟩
  | cons event events ih =>
    rcases trace_cons_iff.mp history with ⟨middle, step, tail⟩
    have shifted : middle = shiftPatient amount (advance laws s event) :=
      step.2.2.trans (advance_commutes_with_patient_shift laws amount s event)
    rw [shifted] at tail
    rcases ih tail with ⟨original, rest, endpoint⟩
    have first : Step laws s event (advance laws s event) :=
      ⟨step.1, (enabled_ignores_patient_amount amount s event).mp step.2.1, rfl⟩
    exact ⟨original, .cons first rest, endpoint⟩

theorem feasible_ignores_patient_amount (laws : RecipientCorrection.Laws)
    (amount : Nat) (s : State) (events : List Event) :
    Feasible (process laws) (shiftPatient amount s) events ↔ Feasible (process laws) s events := by
  constructor
  · rintro ⟨t, history⟩
    rcases trace_from_shifted_start amount history with ⟨original, actual, _⟩
    exact ⟨original, actual⟩
  · rintro ⟨t, history⟩
    exact ⟨shiftPatient amount t, trace_patient_shift amount history⟩

/-- The same operational histories are not the same full physical outcomes. -/
theorem patient_outcome_and_energy_are_shifted (amount : Nat) (s : State) :
    (shiftPatient amount s).patient = s.patient + amount ∧
    energy (shiftPatient amount s) = energy s + amount := by
  constructor
  · rfl
  · simp [energy, shiftPatient, Nat.add_assoc, Nat.add_left_comm, Nat.add_comm]

theorem positive_shift_changes_recorded_outcome {amount : Nat} (positive : 0 < amount)
    (s : State) : (shiftPatient amount s).patient ≠ s.patient := by
  change s.patient + amount ≠ s.patient
  omega

end Generative.RecipientContinuationProjection

#print axioms Generative.RecipientContinuationProjection.shift_preserves_control_coordinates
#print axioms Generative.RecipientContinuationProjection.enabled_ignores_patient_amount
#print axioms Generative.RecipientContinuationProjection.valid_ignores_patient_amount
#print axioms Generative.RecipientContinuationProjection.advance_commutes_with_patient_shift
#print axioms Generative.RecipientContinuationProjection.shift_patient_injective
#print axioms Generative.RecipientContinuationProjection.step_shift_iff
#print axioms Generative.RecipientContinuationProjection.trace_patient_shift
#print axioms Generative.RecipientContinuationProjection.trace_from_shifted_start
#print axioms Generative.RecipientContinuationProjection.feasible_ignores_patient_amount
#print axioms Generative.RecipientContinuationProjection.patient_outcome_and_energy_are_shifted
#print axioms Generative.RecipientContinuationProjection.positive_shift_changes_recorded_outcome
