import PredictionProtocolBridge

/-!
# Recovering an actual consumed receipt in the paid prediction protocol

The finished circuit clears its transient receipt. Within the bounded register
subprocess, the old and new score, installed update rule and executed action
still determine the record that was actually consumed by the write. This is a
semantic label for that earlier observation, not an installed endpoint sensor
or a claim that the circuit retains a second copy of its old memory.

The concrete examples retain aborted paid prefixes of the unchanged source
law. They do not cover its separately executable skipped-write, rebuilding or
stochastic-outage branches.
-/

namespace PredictionProtocolObservation

open Generative Generative.Learning.Protocols PredictionAction
open PredictionProtocolBridge

def postWork (p : Parameters) (s : State) : State :=
  advance p (advance p s .rent) .work

def recoveredTarget (s t : State) : Bool :=
  Nat.beq t.score (revisedScore s.physical.directed s.score true)

def recoveredReceipt (s : State) (action : Bool) (t : State) : Bool :=
  recoveredTarget s t == action

/-- The bounded prior is essential to this particular score-only decoder. -/
theorem update_targets_distinct (fast : Bool) (q : Nat) (hq : q ≤ 4) :
    revisedScore fast q false ≠ revisedScore fast q true := by
  cases fast <;> simp [revisedScore] <;> omega

theorem updated_score_identifies_target (fast target : Bool) (q : Nat) (hq : q ≤ 4) :
    Nat.beq (revisedScore fast q target) (revisedScore fast q true) = target := by
  cases target with
  | false =>
    cases heq : Nat.beq (revisedScore fast q false) (revisedScore fast q true) with
    | false => rfl
    | true => exact False.elim (update_targets_distinct fast q hq (Nat.eq_of_beq_eq_true heq))
  | true => simp

theorem unbounded_prior_collision :
    revisedScore false 5 false = revisedScore false 5 true := by decide

theorem receipt_decode_inverse (action receipt : Bool) :
    (decode action receipt == action) = receipt := by
  cases action <;> cases receipt <;> decide

theorem cycle_score_is_actual_write (p : Parameters) (s : State) :
    (cycleEnd p s).score =
      revisedScore s.physical.directed s.score (label (postWork p s)) := rfl

theorem post_work_keeps_executed_action (p : Parameters) (s : State) :
    (postWork p s).physical.core.selector = command s := rfl

theorem finish_clears_transient_receipt (p : Parameters) (s : State) :
    (cycleEnd p s).receipt = false := rfl

/-- Algebraic recovery is used as a report only on a proved executable cycle. -/
theorem recovered_target_is_consumed_label (p : Parameters) (s : State)
    (hq : s.score ≤ 4) :
    recoveredTarget s (cycleEnd p s) = label (postWork p s) := by
  exact updated_score_identifies_target s.physical.directed (label (postWork p s))
    s.score hq

theorem recovered_receipt_is_actual_record (p : Parameters) (s : State)
    (hq : s.score ≤ 4) (action : Bool) (ha : action = command s) :
    recoveredReceipt s action (cycleEnd p s) = (postWork p s).receipt := by
  unfold recoveredReceipt
  rw [recovered_target_is_consumed_label p s hq, ha]
  change (decode (command s) (postWork p s).receipt == command s) = _
  exact receipt_decode_inverse _ _

/-- Neither recovery function consults the hidden efficacy regime. -/
theorem recovered_receipt_ignores_regime (s t : State) (action z z' : Bool) :
    recoveredReceipt
      { s with physical := { s.physical with core := { s.physical.core with regime := z } } }
      action
      { t with physical := { t.physical with core := { t.physical.core with regime := z' } } } =
    recoveredReceipt s action t := rfl

def boundaryReport {p : Parameters} (s : Boundary p) (action : Bool)
    (t : Boundary p) : Bool := recoveredReceipt s.val action t.val

/-- Independently stated completed exposure law with its actual intermediate
receipt. The report is not manufactured from the hidden regime. -/
def referenceReported (p : Parameters) : Process (Boundary p) (Bool × Bool) where
  step s event t := event.1 = command s.val ∧ macroGuard p s.val event.1 ∧
    t.val = macroEnd p s.val event.1 ∧ event.2 = (postWork p s.val).receipt

theorem reported_step_exact (p : Parameters) (s t : Boundary p) (event : Bool × Bool) :
    (reportedProcess (trialProtocol p) boundaryReport).step s event t ↔
      (referenceReported p).step s event t := by
  change ((blockProcess (trialProtocol p)).step s event.1 t ∧
      event.2 = recoveredReceipt s.val event.1 t.val) ↔ _
  constructor
  · rintro ⟨hblock, hreport⟩
    have hmacro := macro_step_iff_completed.mpr hblock
    obtain ⟨ha, hc, ht⟩ := completed_step_iff.mp hblock
    refine ⟨hmacro.1, hmacro.2.1, hmacro.2.2, hreport.trans ?_⟩
    rw [ht]
    exact recovered_receipt_is_actual_record p s.val s.property.2 event.1 ha
  · rintro ⟨ha, hg, he, hreport⟩
    have hblock := macro_step_iff_completed.mp ⟨ha, hg, he⟩
    obtain ⟨_, _, ht⟩ := completed_step_iff.mp hblock
    refine ⟨hblock, hreport.trans ?_⟩
    rw [ht]
    exact (recovered_receipt_is_actual_record p s.val s.property.2 event.1 ha).symm

theorem reported_histories_exact (p : Parameters) (s t : Boundary p)
    (events : List (Bool × Bool)) :
    Generative.Trace (reportedProcess (trialProtocol p) boundaryReport) s events t ↔
      Generative.Trace (referenceReported p) s events t := by
  constructor
  · exact trace_map (f := id) (fun s event t h => (reported_step_exact p s t event).mp h)
  · exact trace_map (f := id) (fun s event t h => (reported_step_exact p s t event).mpr h)

/-- Every report belongs to its own actual paid block and inherited boundary. -/
theorem reference_history_iff_reported_realization (p : Parameters) (s t : Boundary p)
    (events : List (Bool × Bool)) :
    Generative.Trace (referenceReported p) s events t ↔
      ∃ micro, ReportedRealization (trialProtocol p) boundaryReport s events t micro := by
  rw [← reported_histories_exact p s t events]
  exact reported_trace_iff_realization (trialProtocol p) boundaryReport s events t

theorem successful_cycle_has_nonempty_cleared_record :
    CycleEnabled primary beginning ∧
    (postWork primary beginning).receipt = true ∧
    (cycleEnd primary beginning).receipt = false ∧
    recoveredReceipt beginning (command beginning) (cycleEnd primary beginning) = true := by
  decide

def upfrontStart : State := exampleState 3 1 4 true 6 true true 2
def afterRent : State := advance primary upfrontStart .rent

theorem paid_rent_prefix : PredictionAction.Trace primary upfrontStart [.rent] afterRent := by
  exact .cons (by change Step primary upfrontStart .rent afterRent; decide) (.nil _)

/-- Prospective capture cannot finance the work charge that precedes it. -/
theorem prospective_return_does_not_prefund_work :
    afterRent.physical.core.fuel = 2 ∧ capture afterRent = true ∧
      ¬ Enabled primary afterRent .work ∧ ¬ CycleEnabled primary upfrontStart := by
  decide

theorem rented_abort_has_no_event (event : Event) : ¬ Enabled primary afterRent event := by
  cases event <;> decide +revert

def unwriteableStart : State := exampleState 4 1 4 true 6 false false 2
def unwriteableRecord : State := postWork primary unwriteableStart

theorem paid_record_prefix :
    PredictionAction.Trace primary unwriteableStart [.rent, .work] unwriteableRecord := by
  exact .cons (m := advance primary unwriteableStart .rent)
    (by change Step primary unwriteableStart .rent (advance primary unwriteableStart .rent); decide)
    (.cons (by change Step primary (advance primary unwriteableStart .rent) .work unwriteableRecord; decide) (.nil _))

/-- The actual record exists, but no paid write updates the retained prediction. -/
theorem acquired_record_cannot_be_written :
    unwriteableRecord.phase = .observed ∧ unwriteableRecord.physical.core.fuel = 0 ∧
    unwriteableRecord.physical.core.packets = 0 ∧ unwriteableRecord.receipt = false ∧
    unwriteableRecord.score = 4 ∧ label unwriteableRecord = false ∧
    ¬ Enabled primary unwriteableRecord .write := by
  decide

theorem observed_abort_has_no_event (event : Event) :
    ¬ Enabled primary unwriteableRecord event := by
  cases event <;> decide +revert

def captureFundedStart : State := exampleState 4 1 4 true 6 true true 2

/-- A return may fund the subsequent write, while still not prefunding work. -/
theorem actual_capture_funds_later_write :
    captureFundedStart.physical.core.fuel = primary.rent + primary.base.selector.trial ∧
    captureFundedStart.physical.core.fuel < primary.rent + primary.base.selector.trial + primary.writing ∧
    (postWork primary captureFundedStart).receipt = true ∧
    (postWork primary captureFundedStart).physical.core.fuel = 8 ∧
    CycleEnabled primary captureFundedStart ∧
    (cycleEnd primary captureFundedStart).physical.core.fuel = 7 := by
  decide

def expiryStart : State := exampleState 5 2 4 true 6 false true 1
def correctedWritten : State := advance primary (postWork primary expiryStart) .write

/-- Completion may itself reach an expired module and unusable next boundary. -/
theorem complete_cycle_can_end_expired :
    CycleEnabled primary expiryStart ∧
    (cycleEnd primary expiryStart).phase = .ready ∧
    (cycleEnd primary expiryStart).score = 0 ∧
    (cycleEnd primary expiryStart).physical.moduleLease = 0 ∧
    (cycleEnd primary expiryStart).physical.core.packets = 1 ∧
    ¬ CycleEnabled primary (cycleEnd primary expiryStart) := by
  decide

/-- A corrected future command does not relabel the trial being completed. -/
theorem correction_keeps_current_committed_action :
    command correctedWritten = false ∧ correctedWritten.physical.core.selector = true ∧
    (committed (trialProtocol primary) true).step correctedWritten .finish
      (cycleEnd primary expiryStart) := by
  refine ⟨by decide, by decide, ?_⟩
  change Step primary correctedWritten .finish (cycleEnd primary expiryStart) ∧
    true = correctedWritten.physical.core.selector
  decide

end PredictionProtocolObservation

#print axioms PredictionProtocolObservation.update_targets_distinct
#print axioms PredictionProtocolObservation.updated_score_identifies_target
#print axioms PredictionProtocolObservation.unbounded_prior_collision
#print axioms PredictionProtocolObservation.receipt_decode_inverse
#print axioms PredictionProtocolObservation.cycle_score_is_actual_write
#print axioms PredictionProtocolObservation.post_work_keeps_executed_action
#print axioms PredictionProtocolObservation.finish_clears_transient_receipt
#print axioms PredictionProtocolObservation.recovered_target_is_consumed_label
#print axioms PredictionProtocolObservation.recovered_receipt_is_actual_record
#print axioms PredictionProtocolObservation.recovered_receipt_ignores_regime
#print axioms PredictionProtocolObservation.reported_step_exact
#print axioms PredictionProtocolObservation.reported_histories_exact
#print axioms PredictionProtocolObservation.reference_history_iff_reported_realization
#print axioms PredictionProtocolObservation.successful_cycle_has_nonempty_cleared_record
#print axioms PredictionProtocolObservation.paid_rent_prefix
#print axioms PredictionProtocolObservation.prospective_return_does_not_prefund_work
#print axioms PredictionProtocolObservation.rented_abort_has_no_event
#print axioms PredictionProtocolObservation.paid_record_prefix
#print axioms PredictionProtocolObservation.acquired_record_cannot_be_written
#print axioms PredictionProtocolObservation.observed_abort_has_no_event
#print axioms PredictionProtocolObservation.actual_capture_funds_later_write
#print axioms PredictionProtocolObservation.complete_cycle_can_end_expired
#print axioms PredictionProtocolObservation.correction_keeps_current_committed_action
