import CoupledOccurrence

/-!
# A whole-history correspondence condition for situated practice

This is a generic adequacy test on the existing Process/Trace, not a controller,
a definition of Wang Yangming's true knowledge, or a derivation of moral warrant.
States and transitions can include changing purposes and appraisals. Full finite
occurrence histories retain intermediate states. `Fits` assesses their whole
continuation; it is not defined as satisfying a fixed list of purposes.

An analyst readout is tested for whether it can support one finite response word
whose every admitted realization fits. Acquisition, effective synthesis, motive,
actual enactment and the ethical truth of Fits are separate obligations. The
criterion is intentionally robust and finite; it does not characterize all forms
of knowledge, ethical wisdom, contingent policies or infinite continuations.
-/

namespace Generative.SituatedPractice

open CoupledOccurrence
universe u v w x

variable {State : Type u} {Event : Type v}

abbrev Occurrence := Event × (State × State)

def wholeDescription (P : Process State Event) : Process State (Occurrence (State := State) (Event := Event)) :=
  described P (fun s _ t => (s, t))

/-- A mathematical occurrence history, not an internally stored complete record. -/
structure History (P : Process State Event) where
  start : State
  occurrences : List (Occurrence (State := State) (Event := Event))
  last : State
  actual : Trace (wholeDescription P) start occurrences last

variable {P : Process State Event}

def extend (h : History P) (suffix : List (Occurrence (State := State) (Event := Event)))
    (last : State) (actual : Trace (wholeDescription P) h.last suffix last) : History P :=
  ⟨h.start, h.occurrences ++ suffix, last,
    trace_append_iff.mpr ⟨h.last, h.actual, actual⟩⟩

/-- Extension uses the actual reached state; no resource or relationship reset. -/
theorem extension_erases_to_actual_trace (h : History P)
    (suffix : List (Occurrence (State := State) (Event := Event))) (last : State)
    (actual : Trace (wholeDescription P) h.last suffix last) :
    Trace P h.start ((h.occurrences ++ suffix).map Prod.fst) last :=
  erase_described_trace (extend h suffix last actual).actual

/-- A possible finite response with every admitted realization fitting the whole
extended history. Neither existence nor fitting is inferred from a report alone. -/
def Ready (Fits : History P → Prop) (h : History P) (word : List Event) : Prop :=
  Feasible P h.last word ∧
    ∀ (suffix : List (Occurrence (State := State) (Event := Event))) (last : State)
      (actual : Trace (wholeDescription P) h.last suffix last),
      suffix.map Prod.fst = word → Fits (extend h suffix last actual)

/-- Actual enactment is an additional trace premise. Readiness does not cause it. -/
theorem enacted_ready_fits {Fits : History P → Prop} {h : History P} {word : List Event}
    (ready : Ready Fits h word)
    (suffix : List (Occurrence (State := State) (Event := Event))) (last : State)
    (actual : Trace (wholeDescription P) h.last suffix last)
    (labels : suffix.map Prod.fst = word) :
    Trace P h.start ((h.occurrences ++ suffix).map Prod.fst) last ∧
      Fits (extend h suffix last actual) :=
  ⟨extension_erases_to_actual_trace h suffix last actual,
    ready.2 suffix last actual labels⟩

/-- Readiness has at least one whole-history realization, without asserting
which realization occurs or that a selector is physically implemented. -/
theorem ready_has_fitting_extension {Fits : History P → Prop} {h : History P}
    {word : List Event} (ready : Ready Fits h word) :
    ∃ suffix last, ∃ actual : Trace (wholeDescription P) h.last suffix last,
      suffix.map Prod.fst = word ∧ Fits (extend h suffix last actual) := by
  obtain ⟨last, actual⟩ := ready.1
  obtain ⟨suffix, describedActual, labels⟩ := describe_actual_trace
    (report := fun s _ t => (s, t)) actual
  exact ⟨suffix, last, describedActual, labels,
    ready.2 suffix last describedActual labels⟩

/-- An empty continuation is permitted exactly when the supplied whole appraisal
accepts the existing history. Stopping is not assumed always good or always bad. -/
theorem ready_empty_iff {Fits : History P → Prop} (h : History P) :
    Ready Fits h [] ↔ Fits h := by
  constructor
  · intro ready
    have fitted := ready.2 [] h.last (.nil h.last) rfl
    simpa only [extend, List.append_nil] using fitted
  · intro fitted
    refine ⟨⟨h.last, .nil h.last⟩, ?_⟩
    intro suffix last actual labels
    have empty : suffix = [] := List.map_eq_nil_iff.mp labels
    subst suffix
    have same := trace_nil_iff.mp actual
    subst last
    simpa only [extend, List.append_nil] using fitted

/-- No first ethical warrant is manufactured by passing to this interface. -/
theorem no_fitting_history_no_ready (Fits : History P → Prop)
    (none : ∀ h, ¬ Fits h) (h : History P) (word : List Event) : ¬ Ready Fits h word := by
  intro ready
  obtain ⟨suffix, last, actual, _, fits⟩ := ready_has_fitting_extension ready
  exact none (extend h suffix last actual) fits

section Descriptions

variable {Reading : Type w} {Finer : Type x}

/-- Only attained descriptions are in the domain; no arbitrary response at an
unattained description or inhabitation premise is hidden in policy existence. -/
def ReachedReading (readout : History P → Reading) :=
  {r : Reading // ∃ h, readout h = r}

def readingAt (readout : History P → Reading) (h : History P) : ReachedReading readout :=
  ⟨readout h, h, rfl⟩

def SoundResponse (Fits : History P → Prop) (readout : History P → Reading)
    (respond : ReachedReading readout → List Event) : Prop :=
  ∀ h, Ready Fits h (respond (readingAt readout h))

/-- The exact common-continuation condition. Quantification is over the full
readout fibre, not over separately chosen pairwise comparisons. -/
def CommonContinuation (Fits : History P → Prop) (readout : History P → Reading) : Prop :=
  ∀ r : ReachedReading readout, ∃ word, ∀ h, readout h = r.val → Ready Fits h word

/-- Standard selection/fibre criterion specialized to whole actual histories.
The backward direction is classical existence, not an acquired algorithm. -/
theorem sound_response_iff_common_continuation (Fits : History P → Prop)
    (readout : History P → Reading) :
    (∃ respond, SoundResponse Fits readout respond) ↔ CommonContinuation Fits readout := by
  constructor
  · intro existsResponse r
    obtain ⟨respond, sound⟩ := existsResponse
    refine ⟨respond r, ?_⟩
    intro h same
    have eq : readingAt readout h = r := Subtype.ext same
    simpa only [eq] using sound h
  · intro common
    classical
    let respond := fun r => Classical.choose (common r)
    exact ⟨respond, fun h => Classical.choose_spec (common (readingAt readout h)) h rfl⟩

/-- Better discrimination cannot destroy the existence of a fitting response
for this unchanged law, history domain and appraisal. Costs of obtaining the
finer description are not omitted from an implemented claim: none is made. -/
theorem refinement_preserves_response_existence (Fits : History P → Prop)
    (coarse : History P → Reading) (fine : History P → Finer)
    (forget : Finer → Reading) (refines : ∀ h, coarse h = forget (fine h))
    (common : CommonContinuation Fits coarse) : CommonContinuation Fits fine := by
  intro r
  obtain ⟨h₀, attained⟩ := r.property
  obtain ⟨word, all⟩ := common (readingAt coarse h₀)
  refine ⟨word, ?_⟩
  intro h same
  apply all h
  change coarse h = coarse h₀
  rw [refines h, refines h₀, same, attained]

/-- Two indistinguishable complete histories with no common fitting response
refute only sufficiency of that readout, not the nondual theory or ethics. -/
theorem incompatible_histories_obstruct_response {Fits : History P → Prop}
    {readout : History P → Reading} (h k : History P)
    (same : readout h = readout k)
    (incompatible : ∀ word, Ready Fits h word → ¬ Ready Fits k word) :
    ¬ ∃ respond, SoundResponse Fits readout respond := by
  rintro ⟨respond, sound⟩
  have eq : readingAt readout h = readingAt readout k := Subtype.ext same
  exact incompatible _ (sound h) (by simpa only [eq] using sound k)

/-- Correcting an appraisal need not preserve every old choice. No claim is
made here that the new appraisal is ethically true just because it is supplied. -/
theorem changed_appraisal_requires_response_revision {Old New : History P → Prop}
    {readout : History P → Reading} {respond : ReachedReading readout → List Event}
    (h : History P) (oldSound : SoundResponse Old readout respond)
    (newExcludes : ¬ Ready New h (respond (readingAt readout h))) :
    Ready Old h (respond (readingAt readout h)) ∧ ¬ SoundResponse New readout respond :=
  ⟨oldSound h, fun newSound => newExcludes (newSound h)⟩

end Descriptions

/-! A small set-theoretic boundary for integral compatibility. These are three
mathematical constraints, NOT three primitive interests, ethical persons or
independently warranted goods. No Yangming interpretation is proved by it. -/
namespace PairwiseBoundary

def Accepts (context response : Fin 3) : Prop := context ≠ response

theorem every_pair_has_common_response :
    ∀ i j : Fin 3, ∃ a : Fin 3, Accepts i a ∧ Accepts j a := by decide

theorem whole_family_has_no_common_response :
    ¬ ∃ a : Fin 3, ∀ i : Fin 3, Accepts i a := by
  rintro ⟨a, all⟩
  exact all a rfl

/-- Differentiate the contexts and a fitting response exists; its quality is
only the mathematical Accepts relation above, not a normative certification. -/
def differentiated : Fin 3 → Fin 3
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => 2
  | _ => 0

theorem differentiated_response_fits :
    ∀ i : Fin 3, Accepts i (differentiated i) := by decide

end PairwiseBoundary
end Generative.SituatedPractice

#print axioms Generative.SituatedPractice.extension_erases_to_actual_trace
#print axioms Generative.SituatedPractice.enacted_ready_fits
#print axioms Generative.SituatedPractice.ready_has_fitting_extension
#print axioms Generative.SituatedPractice.ready_empty_iff
#print axioms Generative.SituatedPractice.no_fitting_history_no_ready
#print axioms Generative.SituatedPractice.sound_response_iff_common_continuation
#print axioms Generative.SituatedPractice.refinement_preserves_response_existence
#print axioms Generative.SituatedPractice.incompatible_histories_obstruct_response
#print axioms Generative.SituatedPractice.changed_appraisal_requires_response_revision
#print axioms Generative.SituatedPractice.PairwiseBoundary.every_pair_has_common_response
#print axioms Generative.SituatedPractice.PairwiseBoundary.whole_family_has_no_common_response
#print axioms Generative.SituatedPractice.PairwiseBoundary.differentiated_response_fits
