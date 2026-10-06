import CoupledOccurrence
import PlasticityWitness

/-!
# Occurrence descriptions of an existing consequence/learning/response history

This is an observational extension of PairedPlasticity, not a new controller.
The existing state supplies all dynamics and acquired internal records. The
generic imported interface has no Actor/Patient types; the recipient coordinate
below belongs to this previously supplied local organization.

`recipientStock` describes an actual resource coordinate, not experience,
suffering or welfare. A stock decrease is recorded without asserting that it is
morally adverse. Formed links can transmit or suppress response; coformation
and accuracy alone do not establish ethical justification.
-/

namespace Generative.CoupledConcernHistory

open CoupledOccurrence PairedPlasticity PlasticityWitness

set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

/-- A joint analyst description of selected coordinates. Validity phases remain
visible: a cleared or unavailable latch is not an acquired negative finding. -/
structure Snapshot where
  recipientStock : Nat
  availableFuel : Nat
  nativeRecord : Nat
  firstLink : Option Sign
  secondLink : Option Sign
  ownLatch : Bool
  recipientLatch : Bool
  learningPhase : Phase
  factualCommand : Option Bool
  responsePort : PortMode
  packets : Nat
  deriving DecidableEq, Repr

def snapshot (s : State) : Snapshot :=
  ⟨patient s, fuel s, s.n, s.link0, s.link1, s.ownBit, s.recipientBit,
    s.phase, command s, s.portMode, (core s).packets⟩

def occurrence (s : State) (_ : Event) (t : State) : Snapshot × Snapshot :=
  (snapshot s, snapshot t)

def occurrences (s : State) (word : List Event) :=
  replay (advance laws) occurrence s word

def describedProcess := described (process laws) occurrence

/-- The replay is lawful only because each existing event guard is discharged.
No new observation event or actuator is installed by this proof. -/
theorem runnable_occurrences {s : State} {word : List Event}
    (h : Runnable laws s word) :
    Trace describedProcess s (occurrences s word) (run laws s word) := by
  induction word generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    exact .cons ⟨⟨h.1, rfl⟩, rfl⟩ (ih h.2)

#print axioms Generative.CoupledConcernHistory.runnable_occurrences

theorem trace_endpoint_is_actual_run {s t : State} {word : List Event}
    (h : Trace (process laws) s word t) : t = run laws s word := by
  induction h with
  | nil s => rfl
  | cons hs _ ih =>
    rcases hs with ⟨_, rfl⟩
    exact ih

#print axioms Generative.CoupledConcernHistory.trace_endpoint_is_actual_run

theorem trace_occurrences {s t : State} {word : List Event}
    (h : Trace (process laws) s word t) :
    Trace describedProcess s (occurrences s word) t := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih =>
    rcases hs with ⟨henabled, rfl⟩
    exact .cons ⟨⟨henabled, rfl⟩, rfl⟩ ih

#print axioms Generative.CoupledConcernHistory.trace_occurrences

theorem runnable_prefix {s : State} {past future : List Event}
    (h : Runnable laws s (past ++ future)) : Runnable laws s past := by
  induction past generalizing s with
  | nil => trivial
  | cons e es ih => exact ⟨h.1, ih h.2⟩

#print axioms Generative.CoupledConcernHistory.runnable_prefix

theorem occurrences_join_at_actual_state (s : State) (past future : List Event) :
    occurrences s (past ++ future) =
      occurrences s past ++ occurrences (run laws s past) future :=
  replay_append (advance laws) occurrence (run laws) (fun _ => rfl)
    (fun _ _ _ => rfl) s past future

#print axioms Generative.CoupledConcernHistory.occurrences_join_at_actual_state

def responseWord : List Event := [.close, .read, .assess] ++ actionWord

/-- The previously established formation and use now have an explicit joint
occurrence description, joined at the actual trained state. Values and guards
come from the unchanged model, including the final exhausted response packet. -/
theorem actual_formation_then_response :
    Trace describedProcess (entry .active) (occurrences (entry .active) aligned)
      (trained .active) ∧
    Trace describedProcess (trained .active)
      (occurrences (trained .active) responseWord) final ∧
    patient (entry .active) = 40 ∧ patient (trained .active) = 36 ∧ patient final = 46 ∧
    (entry .active).n = 0 ∧ (trained .active).n = 4 ∧ final.n = 4 ∧
    (trained .active).link0 = some .positive ∧ (trained .active).link1 = some .positive ∧
    (core final).packets = 0 ∧ ¬ PairedPlasticity.Enabled final .attempt := by
  refine ⟨runnable_occurrences aligned_paid, ?_, ?_⟩
  · have whole : Trace (process laws) (entry .active) (aligned ++ responseWord) final := by
      simpa only [fullWord, responseWord, List.append_assoc] using whole_suffix_trace
    obtain ⟨middle, hpast, suffix⟩ := trace_append_iff.mp whole
    have actualMiddle : middle = trained .active := trace_endpoint_is_actual_run hpast
    exact actualMiddle ▸ trace_occurrences suffix
  · decide

#print axioms Generative.CoupledConcernHistory.actual_formation_then_response

/-- One actual transition changes the recipient coordinate before a record is
formed. A later binding changes the relation used for response while preserving
that coordinate. Differentiation is retained within the common history. -/
def firstBeforeDecrease := run laws (entry .active) [.ownPay, .ownReturn false]
def firstAfterDecrease := advance laws firstBeforeDecrease .recipientPay
def firstKnown := run laws (entry .active) (acquisitionWord true true)
def firstBound := advance laws firstKnown .bind

theorem consequence_and_acquisition_are_distinct_dependent_changes :
    Trace describedProcess (entry .active)
      (occurrences (entry .active) (acquisitionWord true true ++ [.bind])) firstBound ∧
    PairedPlasticity.Step laws firstBeforeDecrease .recipientPay firstAfterDecrease ∧
    patient firstBeforeDecrease = 40 ∧ patient firstAfterDecrease = 38 ∧
    firstAfterDecrease.n = firstBeforeDecrease.n ∧
    firstAfterDecrease.link0 = firstBeforeDecrease.link0 ∧
    firstKnown.phase = .bothKnown ∧ firstKnown.recipientBit = true ∧
    firstKnown.link0 = none ∧ firstBound.link0 = some .positive ∧
    patient firstBound = patient firstKnown ∧ patient firstBound = 38 := by
  refine ⟨runnable_occurrences (by decide), ⟨by decide, rfl⟩, ?_⟩
  decide

#print axioms Generative.CoupledConcernHistory.consequence_and_acquisition_are_distinct_dependent_changes

/-- Both feedback histories are actual. They preserve the compared native
record and resource readings while formed links and enabled response differ.
This reused behavioral contrast is not a claim that withdrawal is warranted. -/
theorem actual_feedback_changes_response_constraints :
    Trace describedProcess (entry .active true)
      (occurrences (entry .active true) (continued ++ [.close, .read, .assess]))
      (revisionChosen .active) ∧
    Trace describedProcess (entry .frozen true)
      (occurrences (entry .frozen true) (continued ++ [.close, .read, .assess]))
      (revisionChosen .frozen) ∧
    (revisionChosen .active).n = (revisionChosen .frozen).n ∧
    patient (revisionChosen .active) = patient (revisionChosen .frozen) ∧
    fuel (revisionChosen .active) = fuel (revisionChosen .frozen) ∧
    command (revisionChosen .active) = command (revisionChosen .frozen) ∧
    (revisionChosen .active).link0 ≠ (revisionChosen .frozen).link0 ∧
    PairedPlasticity.Enabled (revisionChosen .active) .abstain ∧
    ¬ PairedPlasticity.Enabled (revisionChosen .active) .attempt ∧
    PairedPlasticity.Enabled (revisionChosen .frozen) .attempt ∧
    ¬ PairedPlasticity.Enabled (revisionChosen .frozen) .abstain := by
  refine ⟨runnable_occurrences ?_, runnable_occurrences ?_, ?_⟩
  · apply runnable_prefix (future := [.abstain])
    simpa only [List.append_assoc] using revision_changes_assessment_not_native_data.1
  · exact runnable_prefix revision_changes_assessment_not_native_data.2.1
  decide

#print axioms Generative.CoupledConcernHistory.actual_feedback_changes_response_constraints

/-- A selected endpoint/current-record summary. It deliberately omits count,
available resources and all earlier intermediate occurrences. -/
abbrev EndpointSummary := Nat × Nat × Option Sign × Option Sign × Option Bool

def endpointSummary (s : State) : EndpointSummary :=
  (patient s, s.n, s.link0, s.link1, command s)

def hasRecipientDecrease (log : List (Event × (Snapshot × Snapshot))) : Bool :=
  log.any (fun item => decide (item.2.2.recipientStock < item.2.1.recipientStock))

def returnedWord := pair false false
def returnedState := run laws (entry .active) returnedWord

/-- A complete actual pair restores the recipient quantity and leaves these
current acquired readings unchanged, but passed through a lower stock. This is
not a claim that the complete endpoint states coincide or that stock=experience. -/
theorem actual_return_does_not_erase_intermediate_decrease :
    Trace describedProcess (entry .active)
      (occurrences (entry .active) returnedWord) returnedState ∧
    endpointSummary returnedState = endpointSummary (entry .active) ∧
    hasRecipientDecrease (occurrences (entry .active) returnedWord) = true ∧
    hasRecipientDecrease (occurrences (entry .active) []) = false := by
  refine ⟨runnable_occurrences (by decide), ?_⟩
  decide

#print axioms Generative.CoupledConcernHistory.actual_return_does_not_erase_intermediate_decrease

/-- No decoder of that endpoint summary can recover this historical property
on all actual histories: the empty and the returned pair already disagree. -/
theorem no_endpoint_summary_decoder_of_actual_decrease :
    ¬ ∃ decode : EndpointSummary → Bool, ∀ word, Runnable laws (entry .active) word →
      decode (endpointSummary (run laws (entry .active) word)) =
        hasRecipientDecrease (occurrences (entry .active) word) := by
  rintro ⟨decode, correct⟩
  have atEmpty := correct [] trivial
  have atReturned := correct returnedWord (by decide)
  change decode (endpointSummary (entry .active)) = false at atEmpty
  change decode (endpointSummary returnedState) = true at atReturned
  rw [actual_return_does_not_erase_intermediate_decrease.2.1, atEmpty] at atReturned
  exact Bool.noConfusion atReturned

#print axioms Generative.CoupledConcernHistory.no_endpoint_summary_decoder_of_actual_decrease

/-- An unavailable report clears the latch while the actual deficit persists.
The retained validity phase prevents this from masquerading as known no-loss. -/
theorem missing_readout_does_not_remove_consequence :
    Trace describedProcess (entry .active)
      (occurrences (entry .active) missingWord) missingEnd ∧
    missingEnd.recipientBit = false ∧ missingEnd.phase = .missing ∧
    patient missingEnd = 38 ∧ patient missingEnd < patient (entry .active) ∧
    ¬ PairedPlasticity.Enabled missingEnd .bind ∧
    ¬ PairedPlasticity.Enabled missingEnd .nativeWrite := by
  refine ⟨runnable_occurrences missing_acquisition_blocks_without_zero_write.1, ?_⟩
  decide

#print axioms Generative.CoupledConcernHistory.missing_readout_does_not_remove_consequence

end Generative.CoupledConcernHistory
