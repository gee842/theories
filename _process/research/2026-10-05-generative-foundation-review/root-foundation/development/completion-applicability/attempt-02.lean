import ConnectedModel

/-!
# Completion information and the existing successor's operative selector

No process law or state is changed. The acquired successor can revise factual
registers and permissions, but its internal help flag depends only on two
fields which every event preserves. A second result distinguishes two external
quantity requests over its one actual history; these are diagnostic supplied
interpretations, not axioms of welfare or counterexamples to the old fixed
one-service meaning. Nothing here installs a new completion-sensitive controller.
The qualified command, permission and actual execution can still change.
-/

namespace Generative.CompletionApplicability

open EvaluativeSuccession
set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

/-- There is no route revision event in the existing successor repertoire. -/
theorem step_preserves_route {laws : RecipientCorrection.Laws}
    {s t : State} {e : Event} (step : Step laws s e t) : t.route = s.route := by
  rcases step with ⟨_, rfl⟩
  cases e with
  | bank e => cases e with
    | bind i h | write => rfl
    | core e w => cases e with
      | contextChange c => rfl
      | core e => cases e <;> rfl
  | attempt => simp only [advance]; split <;> rfl
  | _ => rfl

theorem trace_preserves_route {laws : RecipientCorrection.Laws}
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) : t.route = s.route := by
  induction history with
  | nil => rfl
  | cons step _ ih => exact ih.trans (step_preserves_route step)

/-- The complete dependency of this particular recommendation is explicit. -/
theorem same_selector_inputs_same_help {s t : State}
    (route : t.route = s.route) (weight : t.native.n = s.native.n) : help t = help s := by
  unfold help
  rw [route, weight]

/-- A changed flag would require an actual change to at least one of its inputs.
This necessary interface chooses no mechanism or justification for such a change. -/
theorem changed_help_requires_changed_selector_input {s t : State}
    (changed : help t ≠ help s) : t.route ≠ s.route ∨ t.native.n ≠ s.native.n := by
  by_cases route : t.route = s.route
  · exact Or.inr (fun weight => changed (same_selector_inputs_same_help route weight))
  · exact Or.inl route

/-- Actual recipient learning, archive changes, permission changes and copying
can never revise this recommendation under the existing successor law. -/
theorem help_invariant_on_every_trace {laws : RecipientCorrection.Laws}
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) : help t = help s := by
  exact same_selector_inputs_same_help (trace_preserves_route history)
    (congrArg Native.n (trace_retains_native_and_history history).1)

theorem no_current_law_recommendation_reversal {laws : RecipientCorrection.Laws}
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) (recommended : help s = true) :
    ¬ help t = false := by
  intro reversed
  have same := (help_invariant_on_every_trace history).trans recommended
  have impossible : false = true := reversed.symm.trans same
  cases impossible

/-- A presentation preserving every original edge also preserves the obstruction.
Changing proof syntax alone cannot add selector revision. -/
theorem equivalent_process_preserves_help
    {laws : RecipientCorrection.Laws} (Q : Process State Event)
    (same : ∀ s e t, Q.step s e t ↔ Step laws s e t)
    {s t : State} {events : List Event} (history : Trace Q s events t) : help t = help s := by
  have original : Trace (process laws) s events t := by
    induction history with
    | nil s => exact .nil s
    | cons step _ ih => exact .cons ((same _ _ _).mp step) ih
  exact help_invariant_on_every_trace original

namespace Actual

open SuccessionWitness

theorem entrance_recommends : help entry = true := by decide

theorem all_reached_states_recommend {s : State} {events : List Event}
    (history : Trace (process changed) entry events s) : help s = true :=
  (help_invariant_on_every_trace history).trans entrance_recommends

/-- This concerns the operative assessment, not whether execution is authorized.
The paid assessment cannot choose its abstain branch in any reached state. -/
theorem every_reached_assessment_recommends_and_pays
    {s t : State} {events : List Event}
    (history : Trace (process changed) entry events s) (step : Step changed s .assess t) :
    t.port = .help ∧ help t = true ∧ energy t + 1 = energy s := by
  have retained : help t = true :=
    (help_invariant_on_every_trace (.cons step (.nil _))).trans (all_reached_states_recommend history)
  have bill := step_energy step
  have recommended := all_reached_states_recommend history
  rcases step with ⟨_, rfl⟩
  exact ⟨by simp only [advance, recommended, ↓reduceIte], retained, bill⟩

/-- The quantity attributed to the actual second query before selected use.
Attribution to a new service still requires an independently supplied binding. -/
def queryCredit : Nat := consumed.core.patient - firstEnd.core.patient

theorem actual_query_credit_is_ten : queryCredit = 10 := by decide

theorem actual_history_keeps_completed_query_and_recommends :
    Trace (process changed) entry prefixWord consumed ∧
    consumed.core.patient = firstEnd.core.patient + 10 ∧
    help consumed = true ∧ chosen.port = .help ∧
    consumed.core.hardware.q = 2 ∧ consumed.native.n = 7 := by
  exact ⟨prefix_trace, by decide, all_reached_states_recommend prefix_trace,
    acquired_assessment.2.1, by decide, by decide⟩

/-- A declared quantity comparison only. This is not the old ServiceMeaning,
an ethical predicate or a new field installed in the runtime state. -/
def QuantityMet (required delivered : Nat) : Prop := required ≤ delivered

theorem same_actual_credit_opposite_quantity_completions :
    QuantityMet 10 queryCredit ∧ ¬ QuantityMet 20 queryCredit := by
  rw [actual_query_credit_is_ten]
  change 10 ≤ 10 ∧ ¬ 20 ≤ 10
  exact ⟨by decide, by decide⟩

/-- Even the full physical endpoint has no argument identifying which external
quantity request is being answered. No state-only decoder can answer both.
The 20-unit case does not satisfy the old one-service interpretation premise. -/
theorem no_requirement_free_full_state_decoder :
    ¬ ∃ decode : State → Bool,
      (decode consumed = true ↔ QuantityMet 10 queryCredit) ∧
      (decode consumed = true ↔ QuantityMet 20 queryCredit) := by
  rintro ⟨decode, one, two⟩
  have facts := same_actual_credit_opposite_quantity_completions
  exact facts.2 (two.mp (one.mpr facts.1))

/-- Any further summary of that same state inherits the missing query binding. -/
theorem no_requirement_free_record_decoder {Record : Type}
    (record : State → Record) :
    ¬ ∃ decode : Record → Bool,
      (decode (record consumed) = true ↔ QuantityMet 10 queryCredit) ∧
      (decode (record consumed) = true ↔ QuantityMet 20 queryCredit) := by
  rintro ⟨decode, one, two⟩
  exact no_requirement_free_full_state_decoder ⟨fun s => decode (record s), one, two⟩

/-- Supplying the diagnostic requirement separates the two exact comparisons.
This pure readout is not used by the current selector or an acquired mechanism. -/
def quantityReadout (required delivered : Nat) : Bool := decide (required ≤ delivered)

theorem quantity_readout_spec (required delivered : Nat) :
    quantityReadout required delivered = true ↔ QuantityMet required delivered := by
  exact ⟨of_decide_eq_true, fun h => decide_eq_true h⟩

theorem query_binding_resolves_these_comparisons :
    quantityReadout 10 queryCredit = true ∧ quantityReadout 20 queryCredit = false := by
  rw [actual_query_credit_is_ten]
  exact ⟨rfl, rfl⟩

end Actual
end Generative.CompletionApplicability

#print axioms Generative.CompletionApplicability.step_preserves_route
#print axioms Generative.CompletionApplicability.trace_preserves_route
#print axioms Generative.CompletionApplicability.same_selector_inputs_same_help
#print axioms Generative.CompletionApplicability.changed_help_requires_changed_selector_input
#print axioms Generative.CompletionApplicability.help_invariant_on_every_trace
#print axioms Generative.CompletionApplicability.no_current_law_recommendation_reversal
#print axioms Generative.CompletionApplicability.equivalent_process_preserves_help
#print axioms Generative.CompletionApplicability.Actual.entrance_recommends
#print axioms Generative.CompletionApplicability.Actual.all_reached_states_recommend
#print axioms Generative.CompletionApplicability.Actual.every_reached_assessment_recommends_and_pays
#print axioms Generative.CompletionApplicability.Actual.actual_query_credit_is_ten
#print axioms Generative.CompletionApplicability.Actual.actual_history_keeps_completed_query_and_recommends
#print axioms Generative.CompletionApplicability.Actual.same_actual_credit_opposite_quantity_completions
#print axioms Generative.CompletionApplicability.Actual.no_requirement_free_full_state_decoder
#print axioms Generative.CompletionApplicability.Actual.no_requirement_free_record_decoder
#print axioms Generative.CompletionApplicability.Actual.quantity_readout_spec
#print axioms Generative.CompletionApplicability.Actual.query_binding_resolves_these_comparisons
