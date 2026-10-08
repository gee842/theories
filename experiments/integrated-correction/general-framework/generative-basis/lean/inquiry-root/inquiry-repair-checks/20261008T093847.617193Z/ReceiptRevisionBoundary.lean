import AcquiredPredictionRecord
import ReceiptIdentification

/-!
# Receipt identification, event time and a paid revision boundary

The existing PredictionAction work law has an available packet and a noiseless
receipt. Its work/write protocol therefore supplies a sound current target to
the declared updater. This is a specialization of receipt identification, not
a theorem that arbitrary failed returns reveal the target.

The unchanged reversal event then gives an actual boundary: a historically
successful observation can remain represented in native memory while the
current regime changes. The receipt is identified at its own event time; no
new timestamp sensor, stored transcript, physical law or correct target is
inserted. The old process clears the transient receipt at finish. References
to that earlier receipt below are proof-level historical references.

The stochastic implementation's unavailable-packet branches are not legal work
steps of this deterministic subprocess. Neither guaranteed sampling nor a
particular event schedule follows from these existential histories.
-/

namespace ReceiptRevisionBoundary

open PredictionAction

/-- The actual paid work edge supplies a witness to the more general receipt
relation; availability is proved from this existing edge law. -/
theorem paid_work_has_compatible_receipt {p : Parameters} {s t : State}
    (h : Step p s .work t) :
    ReceiptIdentification.Compatible (t.physical.core.selector, t.receipt)
      s.physical.core.regime := by
  rcases h with ⟨_, rfl⟩
  exact ⟨true, rfl⟩

/-- Success identifies the regime at the work event, not at all later times. -/
theorem paid_success_identifies_event_regime {p : Parameters} {s t : State}
    (h : Step p s .work t) (hsuccess : t.receipt = true) :
    s.physical.core.regime = t.physical.core.selector := by
  have hcompatible := paid_work_has_compatible_receipt h
  have hsuccessCompatible : ReceiptIdentification.Compatible
      (t.physical.core.selector, true) s.physical.core.regime :=
    hsuccess ▸ hcompatible
  exact (ReceiptIdentification.compatible_success_iff _ _).mp hsuccessCompatible

/-- Correct target input is derived from actual work, receipt and action
reference under the available law; it is not an additional teaching premise.
Slow updating need not change the selected command after this one write. -/
theorem available_work_write_update {p : Parameters} {s observed written : State}
    (hwork : Step p s .work observed) (hwrite : Step p observed .write written) :
    written.score = revisedScore s.physical.directed s.score s.physical.core.regime ∧
    written.physical.core.regime = s.physical.core.regime ∧
    written.physical.core.selector = command s := by
  rcases hwork with ⟨_, rfl⟩
  rcases hwrite with ⟨_, rfl⟩
  have hevidence : label (advance p s .work) = s.physical.core.regime :=
    ReceiptIdentification.available_complete_decoder_recovered (command s) s.physical.core.regime
  exact ⟨congrArg (revisedScore s.physical.directed s.score) hevidence, rfl, rfl⟩

/-- Freshness through the immediate write is supported by the installed phase
law: reversal cannot execute in the observed phase reached by work. -/
theorem work_blocks_reversal_before_write {p : Parameters} {s observed : State}
    (hwork : Step p s .work observed) : ¬ Enabled p observed .reverse := by
  rcases hwork with ⟨_, rfl⟩
  intro hreverse
  change Phase.observed = Phase.ready at hreverse
  cases hreverse

/-- Every enabled next event after work must be write under the actual phase
guards. This does not assert that write is affordable or that a next event
occurs: an acquired receipt can remain at an unfunded deadlock. -/
theorem enabled_after_work_must_be_write {p : Parameters} {s observed : State}
    {event : Event} (hwork : Step p s .work observed)
    (henabled : Enabled p observed event) : event = .write := by
  rcases hwork with ⟨_, rfl⟩
  cases event with
  | formUpdater fast => cases henabled.1
  | rent => cases henabled.1
  | work => cases henabled.1
  | write => rfl
  | finish => cases henabled.1
  | reverse => cases henabled

/-- The existing reversal preserves acquired memory, the action reference and
resources while changing the target. Native retention is not automatic truth. -/
theorem reversal_retains_readout_changes_regime {p : Parameters} {s t : State}
    (hreverse : Step p s .reverse t) :
    t.score = s.score ∧ t.physical.core.selector = s.physical.core.selector ∧
    command t = command s ∧ t.physical.core.fuel = s.physical.core.fuel ∧
    t.physical.core.packets = s.physical.core.packets ∧
    t.physical.core.regime = !s.physical.core.regime := by
  rcases hreverse with ⟨_, rfl⟩
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- The sixth successful trial in the already constructed corrective history. -/
def successStart : State := exampleState 29 7 4 true 6 true false 2
def successObservation : State := advance primary (advance primary successStart .rent) .work
def successWritten : State := advance primary successObservation .write
def beforeReversal : State := advance primary successWritten .finish
def afterReversal : State := advance primary beforeReversal .reverse

theorem actual_success_prefix :
    Trace primary beginning (cycles 5 ++ [.rent, .work]) successObservation := by
  apply cycle_then (u := exampleState 17 11 3 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 20 10 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 23 9 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := exampleState 26 8 4 true 6 true false 2) (by decide) (by decide)
  apply cycle_then (u := successStart) (by decide) (by decide)
  apply Generative.Trace.cons (m := advance primary successStart .rent)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := successObservation)
    (by change Step _ _ _ _; decide)
  exact .nil _

theorem actual_success_then_reversal :
    Trace primary successObservation [.write, .finish, .reverse] afterReversal := by
  apply Generative.Trace.cons (m := successWritten) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := beforeReversal) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := afterReversal) (by change Step _ _ _ _; decide)
  exact .nil _

/-- An actual successful receipt identified its historical regime, while the
retained score and command now point away from the changed current regime.
This is a reached counterexample to carrying success-time identification
forward without an appropriate stability or fresh-evidence justification. -/
theorem acquired_success_does_not_identify_current_regime :
    Trace primary beginning
      ((cycles 5 ++ [.rent, .work]) ++ [.write, .finish, .reverse]) afterReversal ∧
    successObservation.receipt = true ∧
    label successObservation = successObservation.physical.core.regime ∧
    label successObservation ≠ afterReversal.physical.core.regime ∧
    afterReversal.score = beforeReversal.score ∧ afterReversal.score = 4 ∧
    command afterReversal = true ∧ afterReversal.physical.core.regime = false := by
  refine ⟨Generative.trace_append_iff.mpr
    ⟨successObservation, actual_success_prefix, actual_success_then_reversal⟩,
    rfl, rfl, ?_, rfl, rfl, rfl, rfl⟩
  intro h
  cases h

def freshObservation : State := advance primary (advance primary afterReversal .rent) .work
def freshWritten : State := advance primary freshObservation .write

/-- The same actual post-reversal resources fund a new observation and write. -/
theorem actual_fresh_observation_and_write :
    Trace primary afterReversal [.rent, .work, .write] freshWritten := by
  apply Generative.Trace.cons (m := advance primary afterReversal .rent)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := freshObservation) (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := freshWritten) (by change Step _ _ _ _; decide)
  exact .nil _

/-- With unknown availability, this failed receipt remains ambiguous. The
available-law specialization identifies its actual target; the existing Slow
rule updates toward that target but does not instantly reverse the command. -/
theorem fresh_available_failure_has_scoped_correction :
    freshObservation.receipt = false ∧
    ReceiptIdentification.partialDecode freshObservation.physical.core.selector
      freshObservation.receipt = none ∧
    label freshObservation = freshObservation.physical.core.regime ∧
    freshWritten.score = 3 ∧ command freshWritten = true ∧
    freshWritten.physical.core.regime = false ∧
    freshWritten.physical.core.fuel = 27 ∧ freshWritten.physical.core.packets = 5 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- The new observation/revision is part of the same continuing history, with
native score provenance still governed by the existing acquired-record result. -/
theorem same_history_retains_fresh_write_provenance :
    ∃ events, Trace primary beginning events freshWritten ∧
      freshWritten.score = AcquiredPredictionRecord.replay beginning.score
        (AcquiredPredictionRecord.writeInputs primary beginning events) := by
  have hstale := acquired_success_does_not_identify_current_regime.1
  have hwhole := Generative.trace_append_iff.mpr
    ⟨afterReversal, hstale, actual_fresh_observation_and_write⟩
  exact ⟨_, hwhole, AcquiredPredictionRecord.trace_memory_is_replay hwhole⟩

/-- The unchanged post-reversal prefix reaches the observation used in the
previously proved paid correction, without re-proving its final continuation. -/
theorem actual_later_corrective_observation :
    Trace primary afterReversal
      (cycles 2 ++ [.formUpdater true, .rent, .work]) correctiveObservation := by
  apply cycle_then (u := exampleState 27 5 3 true 5 false false 1) (by decide) (by decide)
  apply cycle_then (u := exampleState 22 4 2 true 4 false false 0) (by decide) (by decide)
  apply Generative.Trace.cons (m := exampleState 20 4 2 true 4 false true 2)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := advance primary (exampleState 20 4 2 true 4 false true 2) .rent)
    (by change Step _ _ _ _; decide)
  apply Generative.Trace.cons (m := correctiveObservation) (by change Step _ _ _ _; decide)
  exact .nil _

theorem same_history_reaches_opposed_success :
    ∃ events, Trace primary successObservation events AcquiredPredictionRecord.afterCorrectedWork := by
  have hlater := Generative.trace_append_iff.mpr
    ⟨correctiveObservation, actual_later_corrective_observation,
      AcquiredPredictionRecord.actual_write_then_corrected_work.1⟩
  exact ⟨_, Generative.trace_append_iff.mpr
    ⟨afterReversal, actual_success_then_reversal, hlater⟩⟩

/-- Opposed successful action receipts can both be true in one legal changing
history. Their conflict rejects a fixed-regime pooling interpretation, not
either observation or the dynamic process that generated them. -/
theorem actual_dynamic_successes_refute_fixed_pooling :
    Trace primary beginning (cycles 5 ++ [.rent, .work]) successObservation ∧
    (∃ events, Trace primary successObservation events AcquiredPredictionRecord.afterCorrectedWork) ∧
    (successObservation.physical.core.selector, successObservation.receipt) = (true, true) ∧
    (AcquiredPredictionRecord.afterCorrectedWork.physical.core.selector,
      AcquiredPredictionRecord.afterCorrectedWork.receipt) = (false, true) ∧
    ¬ ∃ regime, ReceiptIdentification.StableCompatible [(true, true), (false, true)] regime := by
  refine ⟨actual_success_prefix, same_history_reaches_opposed_success, rfl, rfl, ?_⟩
  exact ReceiptIdentification.opposed_successes_refute_fixed_regime _
    (by exact .tail _ (.head _)) (by exact .head _)

end ReceiptRevisionBoundary

#print axioms ReceiptRevisionBoundary.paid_work_has_compatible_receipt
#print axioms ReceiptRevisionBoundary.paid_success_identifies_event_regime
#print axioms ReceiptRevisionBoundary.available_work_write_update
#print axioms ReceiptRevisionBoundary.work_blocks_reversal_before_write
#print axioms ReceiptRevisionBoundary.enabled_after_work_must_be_write
#print axioms ReceiptRevisionBoundary.reversal_retains_readout_changes_regime
#print axioms ReceiptRevisionBoundary.actual_success_prefix
#print axioms ReceiptRevisionBoundary.actual_success_then_reversal
#print axioms ReceiptRevisionBoundary.acquired_success_does_not_identify_current_regime
#print axioms ReceiptRevisionBoundary.actual_fresh_observation_and_write
#print axioms ReceiptRevisionBoundary.fresh_available_failure_has_scoped_correction
#print axioms ReceiptRevisionBoundary.same_history_retains_fresh_write_provenance
#print axioms ReceiptRevisionBoundary.actual_later_corrective_observation
#print axioms ReceiptRevisionBoundary.same_history_reaches_opposed_success
#print axioms ReceiptRevisionBoundary.actual_dynamic_successes_refute_fixed_pooling
