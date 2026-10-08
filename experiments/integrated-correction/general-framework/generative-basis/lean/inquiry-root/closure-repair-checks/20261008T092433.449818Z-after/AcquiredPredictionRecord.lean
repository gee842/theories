import PredictionAction
import OutcomeContinuation

/-!
# Acquired writes, retained records and the next executed command

The unchanged PredictionAction process already implements an action-conditioned
receipt, a paid write, retained memory and a command selected from that memory.
This module derives the provenance of its current score by replaying the writes
of an actual history, retaining the inherited starting score. The transcript is
an analyst's extraction of consumed write inputs; it is not an installed log or
a new transition law. A general trace can begin with an inherited receipt; only
the concrete beginning-to-correction witness establishes acquisition in its run.

The score and retained last-action reference determine the next command, but
not the affordability, availability or all possible future effects of a command.
The supplied noiseless receipt law, updater recipe, decoder, register and event
scheduling remain explicit. This result does not establish selfhood or concern.
-/

namespace AcquiredPredictionRecord

open PredictionAction

/-- Existing updater mode and action-conditioned label at each actual write. -/
abbrev WriteInput := Bool × Bool

def writeInputs (p : Parameters) : State → List Event → List WriteInput
  | _, [] => []
  | s, a :: rest =>
    match a with
    | .formUpdater u => writeInputs p (advance p s (.formUpdater u)) rest
    | .rent => writeInputs p (advance p s .rent) rest
    | .work => writeInputs p (advance p s .work) rest
    | .write => (s.physical.directed, label s) :: writeInputs p (advance p s .write) rest
    | .finish => writeInputs p (advance p s .finish) rest
    | .reverse => writeInputs p (advance p s .reverse) rest

/-- Replay uses the existing update recipe and the inherited starting memory. -/
def replay : Nat → List WriteInput → Nat
  | score, [] => score
  | score, (fast, target) :: rest => replay (revisedScore fast score target) rest

/-- Every score change is explained by actual writes from the inherited score. -/
theorem trace_memory_is_replay {p : Parameters} {s t : State} {events : List Event}
    (h : Trace p s events t) : t.score = replay s.score (writeInputs p s events) := by
  induction h with
  | nil => exact rfl
  | @cons s m t a rest hs _ ih =>
    rcases hs with ⟨_, rfl⟩
    cases a <;> exact ih

/-- The command readout depends on two retained fields, not the hidden regime. -/
theorem equal_read_fields_equal_commands {s t : State}
    (hscore : s.score = t.score)
    (hreference : s.physical.core.selector = t.physical.core.selector) :
    command s = command t := by
  unfold command
  exact hscore ▸ hreference ▸ rfl

/-- Acquired history can be forgotten for this readout only after its writes
have been incorporated into the retained score. No exact-future claim is made. -/
theorem same_acquisition_same_next_command
    {p q : Parameters} {s t u v : State} {left right : List Event}
    (hleft : Trace p s left t) (hright : Trace q u right v)
    (hstart : s.score = u.score)
    (hinputs : writeInputs p s left = writeInputs q u right)
    (hreference : t.physical.core.selector = v.physical.core.selector) :
    command t = command v := by
  apply equal_read_fields_equal_commands _ hreference
  have hreplay : replay s.score (writeInputs p s left) = replay u.score (writeInputs q u right) :=
    hstart ▸ hinputs ▸ rfl
  exact (trace_memory_is_replay hleft).trans
    (hreplay.trans (trace_memory_is_replay hright).symm)

/-- With the inherited memory and last-action reference fixed, different later
commands require different acquired write transcripts in this implementation. -/
theorem different_commands_require_different_acquisition
    {p q : Parameters} {s t u v : State} {left right : List Event}
    (hleft : Trace p s left t) (hright : Trace q u right v)
    (hstart : s.score = u.score)
    (hreference : t.physical.core.selector = v.physical.core.selector)
    (hdifferent : command t ≠ command v) :
    writeInputs p s left ≠ writeInputs q u right := by
  intro hinputs
  exact hdifferent (same_acquisition_same_next_command hleft hright hstart hinputs hreference)

/-- A write keeps its action reference: the receipt concerns the preceding
issued command, while the resulting score influences a later command. -/
theorem write_retains_action_reference {p : Parameters} {s t : State}
    (h : Step p s .write t) :
    t.physical.core.selector = s.physical.core.selector ∧
      t.score = revisedScore s.physical.directed s.score (label s) := by
  rcases h with ⟨_, rfl⟩
  exact ⟨rfl, rfl⟩

/-- The command is not only a proposed output: the work event installs it as
the actual issued action used by the unchanged receipt law. -/
theorem work_executes_readout {p : Parameters} {s t : State}
    (h : Step p s .work t) :
    t.physical.core.selector = command s ∧
      t.receipt = receiptOf (command s) s.physical.core.regime true := by
  rcases h with ⟨_, rfl⟩
  exact ⟨rfl, rfl⟩

/-- The existing noiseless receipt supplies a target only together with the
actual action reference kept by work. This does not cover outages. -/
theorem work_record_decodes_actual_regime {p : Parameters} {s t : State}
    (h : Step p s .work t) : label t = s.physical.core.regime := by
  rcases h with ⟨_, rfl⟩
  exact noiseless_receipt_decodes_target (command s) s.physical.core.regime

/-- A raw success bit alone cannot decode the target across differing actions. -/
theorem no_receipt_only_target_decoder :
    ¬ ∃ readout : Bool → Bool, ∀ action regime,
      readout (receiptOf action regime true) = regime := by
  rintro ⟨readout, h⟩
  have hfalse : readout true = false := h false false
  have htrue : readout true = true := h true true
  have impossible : false = true := hfalse.symm.trans htrue
  cases impossible

/-- The endpoint-sensitive interface identifies the command actually issued by
an enabled work event. Its complete physical state still determines enabledness. -/
theorem enabled_work_outcome_iff (p : Parameters) (s : State)
    (henabled : Enabled p s .work) (outcome : Bool) :
    Generative.OutcomeContinuation.OutcomeResidual (process p) s
      (fun t => t.physical.core.selector) [] [.work] outcome ↔ command s = outcome := by
  have hstep : Step p s .work (advance p s .work) := ⟨henabled, rfl⟩
  exact Generative.OutcomeContinuation.outcome_singleton_at_unique_successor
    (P := process p) (observe := fun t => t.physical.core.selector) hstep (fun _ h => h.2)

/-- The acquired-memory result and the outcome representation describe the same
current causal state. No fresh memory or resource state is supplied at this join. -/
theorem acquired_record_and_executed_outcome
    {p : Parameters} {s t : State} {events : List Event}
    (hpast : Trace p s events t) (hwork : Enabled p t .work) (outcome : Bool) :
    t.score = replay s.score (writeInputs p s events) ∧
    (Generative.OutcomeContinuation.OutcomeResidual (process p) t
      (fun endpoint => endpoint.physical.core.selector) [] [.work] outcome ↔ command t = outcome) :=
  ⟨trace_memory_is_replay hpast, enabled_work_outcome_iff p t hwork outcome⟩

/-- Equal acquired command information is an exact summary of this admitted
work output, while the two complete states retain their own feasibility checks. -/
theorem same_acquisition_same_work_outcomes
    {p q : Parameters} {s t u v : State} {left right : List Event}
    (hleft : Trace p s left t) (hright : Trace q u right v)
    (hstart : s.score = u.score)
    (hinputs : writeInputs p s left = writeInputs q u right)
    (hreference : t.physical.core.selector = v.physical.core.selector)
    (hworkLeft : Enabled p t .work) (hworkRight : Enabled q v .work) (outcome : Bool) :
    Generative.OutcomeContinuation.OutcomeResidual (process p) t
      (fun endpoint => endpoint.physical.core.selector) [] [.work] outcome ↔
    Generative.OutcomeContinuation.OutcomeResidual (process q) v
      (fun endpoint => endpoint.physical.core.selector) [] [.work] outcome := by
  have hcommand := same_acquisition_same_next_command hleft hright hstart hinputs hreference
  exact (enabled_work_outcome_iff p t hworkLeft outcome).trans
    (hcommand ▸ (enabled_work_outcome_iff q v hworkRight outcome).symm)

def correctivePrefix : List Event :=
  cycles 6 ++ [.reverse] ++ cycles 2 ++ [.formUpdater true, .rent, .work]

/-- This is a prefix of the previously constructed learner history, with its
actual spent reserves, leases and remembered prior action retained. -/
theorem actual_corrective_prefix : Trace primary beginning correctivePrefix correctiveObservation := by
  apply cycle_then (u := exampleState 17 11 3 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 20 10 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 23 9 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 26 8 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 29 7 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 32 6 4 true 6 true false 2) (by decide) (by decide)
  apply Generative.Trace.cons (m := exampleState 32 6 4 true 6 false false 2) (by change Step _ _ _ _; decide)
  apply cycle_then (u := exampleState 27 5 3 true 5 false false 1) (by decide) (by decide)
  apply cycle_then (u := exampleState 22 4 2 true 4 false false 0) (by decide) (by decide)
  apply Generative.Trace.cons (m := exampleState 20 4 2 true 4 false true 2) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := advance primary (exampleState 20 4 2 true 4 false true 2) .rent)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := correctiveObservation) (by change Step _ _ _ _; decide)
  exact .nil _

def afterCorrectiveWrite : State := advance primary correctiveObservation .write
def beforeCorrectedWork : State := advance primary (advance primary afterCorrectiveWrite .finish) .rent
def afterCorrectedWork : State := advance primary beforeCorrectedWork .work

/-- The new command is actually executed in a paid continuation, whose receipt
changes from failure to success under the same unchanged regime. -/
theorem actual_write_then_corrected_work :
    Trace primary correctiveObservation [.write, .finish, .rent, .work] afterCorrectedWork ∧
    correctiveObservation.receipt = false ∧ command correctiveObservation = true ∧
    command afterCorrectiveWrite = false ∧
    afterCorrectedWork.physical.core.selector = false ∧ afterCorrectedWork.receipt = true := by
  refine ⟨?_, rfl, rfl, rfl, rfl, rfl⟩
  apply Generative.Trace.cons (m := afterCorrectiveWrite) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := advance primary afterCorrectiveWrite .finish) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := beforeCorrectedWork) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := afterCorrectedWork) (by change Step _ _ _ _; decide)
  exact .nil _

/-- The replay theorem now applies to an actual acquired record and its later
executed effect, without choosing a fresh starting memory at the join. -/
theorem actual_acquisition_replay_and_effect :
    Trace primary beginning (correctivePrefix ++ [.write, .finish, .rent, .work]) afterCorrectedWork ∧
    afterCorrectedWork.score = replay beginning.score
      (writeInputs primary beginning (correctivePrefix ++ [.write, .finish, .rent, .work])) ∧
    afterCorrectedWork.physical.core.selector = false ∧ afterCorrectedWork.receipt = true := by
  have h := Generative.trace_append_iff.mpr
    ⟨correctiveObservation, actual_corrective_prefix, actual_write_then_corrected_work.1⟩
  exact ⟨h, trace_memory_is_replay h, rfl, rfl⟩

/-- The general endpoint interface is instantiated by the existing learner's
actual retained command and receipt, after the same acquired corrective prefix. -/
theorem actual_acquisition_has_corrected_outcome :
    Generative.OutcomeContinuation.OutcomeResidual (process primary) beginning
      (fun s => (s.physical.core.selector, s.receipt)) correctivePrefix
      [.write, .finish, .rent, .work] (false, true) :=
  Generative.OutcomeContinuation.outcome_of_actual_history
    actual_corrective_prefix actual_write_then_corrected_work.1 rfl

end AcquiredPredictionRecord

#print axioms AcquiredPredictionRecord.trace_memory_is_replay
#print axioms AcquiredPredictionRecord.equal_read_fields_equal_commands
#print axioms AcquiredPredictionRecord.same_acquisition_same_next_command
#print axioms AcquiredPredictionRecord.different_commands_require_different_acquisition
#print axioms AcquiredPredictionRecord.write_retains_action_reference
#print axioms AcquiredPredictionRecord.work_executes_readout
#print axioms AcquiredPredictionRecord.work_record_decodes_actual_regime
#print axioms AcquiredPredictionRecord.no_receipt_only_target_decoder
#print axioms AcquiredPredictionRecord.enabled_work_outcome_iff
#print axioms AcquiredPredictionRecord.acquired_record_and_executed_outcome
#print axioms AcquiredPredictionRecord.same_acquisition_same_work_outcomes
#print axioms AcquiredPredictionRecord.actual_corrective_prefix
#print axioms AcquiredPredictionRecord.actual_write_then_corrected_work
#print axioms AcquiredPredictionRecord.actual_acquisition_replay_and_effect
#print axioms AcquiredPredictionRecord.actual_acquisition_has_corrected_outcome
