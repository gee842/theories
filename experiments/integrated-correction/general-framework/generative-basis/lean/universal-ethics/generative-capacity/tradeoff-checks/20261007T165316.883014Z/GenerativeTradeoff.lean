import Std

/-!
# Identifying necessary loss without erasing the history

This is a descriptive/correspondence interface for the G0/C/P investigation, not
a new ethical ordering. Circumstances, possible responses and the continuations
they form are differentiated descriptions within the same generative unfolding.
Their actual formation, causal law and evidential identification are supplied.

`NecessaryLoss` is conditional on an explicitly identified target and quantifies
over all represented feasible routes. It also requires at least one such route,
so impossibility of the target is not called its necessary price. The response
repertoire, loss predicate and history representation must faithfully cover the
scope of an application. An omitted alternative or omitted loss is not thereby
unreal. No theorem infers permission, obligation or net goodness from necessity.

Candidate circumstances represent uncertainty in an inquiry arising within that
same unfolding. Universal claims apply to the actual circumstance only when it
is retained. Subset refinement alone is not evidence that the truth is retained.
The finite control tests this failure with actual feasible routes and histories,
not arbitrary changes to an ethical verdict.

Three supplied circumstances describe which handover relation can be completed.
Four responses keep the old realization, interrupt and restore it while forming
a target, or form the target through left/right continuous handover. Three
positions in the represented history record support continuity. A restored final
state does not erase an earlier interruption. These are stipulated possible
histories, not a physical implementation or an empirical finding. Costs outside
these represented interruptions are not modeled, so no whole no-loss ethical
comparison is certified. Continuity is a selected descriptive target, not an
axiom requiring every existing activity to continue indefinitely.

Finally, route existence separately in each circumstance does not furnish one
available response that works across them. An implemented conditional policy
would additionally require an actually feasible, accurate observation and its
intermediate history/cost. This module does not supply or infer that policy.
-/

namespace GenerativeTradeoff

universe u v w x

structure Problem (Circumstance : Type u) (Response : Type v) (History : Type w) where
  feasible : Circumstance → Response → Prop
  continuation : Circumstance → Response → History
  target : History → Prop
  loss : History → Prop

def Successful {Circumstance : Type u} {Response : Type v} {History : Type w}
    (problem : Problem Circumstance Response History) (circumstance : Circumstance)
    (response : Response) : Prop :=
  problem.feasible circumstance response ∧
    problem.target (problem.continuation circumstance response)

def LosslessSuccess {Circumstance : Type u} {Response : Type v} {History : Type w}
    (problem : Problem Circumstance Response History) (circumstance : Circumstance)
    (response : Response) : Prop :=
  Successful problem circumstance response ∧
    ¬ problem.loss (problem.continuation circumstance response)

def NecessaryLoss {Circumstance : Type u} {Response : Type v} {History : Type w}
    (problem : Problem Circumstance Response History) (circumstance : Circumstance) : Prop :=
  (∃ response, Successful problem circumstance response) ∧
    ∀ response, Successful problem circumstance response →
      problem.loss (problem.continuation circumstance response)

def Certain {Circumstance : Type u} (candidates : Circumstance → Prop)
    (claim : Circumstance → Prop) : Prop :=
  ∀ circumstance, candidates circumstance → claim circumstance

def UniformLossless {Circumstance : Type u} {Response : Type v} {History : Type w}
    (problem : Problem Circumstance Response History) (candidates : Circumstance → Prop)
    (response : Response) : Prop :=
  ∀ circumstance, candidates circumstance → LosslessSuccess problem circumstance response

theorem retained_actuality_receives_certified_necessity
    {Circumstance : Type u} {Response : Type v} {History : Type w}
    {problem : Problem Circumstance Response History}
    {candidates : Circumstance → Prop} {actual : Circumstance}
    (retained : candidates actual)
    (certified : Certain candidates (NecessaryLoss problem)) :
    NecessaryLoss problem actual :=
  certified actual retained

/-- This preserves a universal statement. Its application to reality separately
    needs the actual circumstance in the refined set. -/
theorem refinement_preserves_certified_necessity
    {Circumstance : Type u} {Response : Type v} {History : Type w}
    {problem : Problem Circumstance Response History}
    {previous refined : Circumstance → Prop}
    (subset : ∀ circumstance, refined circumstance → previous circumstance)
    (certified : Certain previous (NecessaryLoss problem)) :
    Certain refined (NecessaryLoss problem) :=
  fun circumstance retained => certified circumstance (subset circumstance retained)

theorem actual_alternative_refutes_necessity
    {Circumstance : Type u} {Response : Type v} {History : Type w}
    {problem : Problem Circumstance Response History}
    {circumstance : Circumstance} {response : Response}
    (alternative : LosslessSuccess problem circumstance response) :
    ¬ NecessaryLoss problem circumstance := by
  intro necessary
  exact alternative.2 (necessary.2 response alternative.1)

theorem uniform_response_supplies_each_route
    {Circumstance : Type u} {Response : Type v} {History : Type w}
    {problem : Problem Circumstance Response History} {candidates : Circumstance → Prop}
    {response : Response} (uniform : UniformLossless problem candidates response) :
    Certain candidates (fun circumstance => ∃ response, LosslessSuccess problem circumstance response) :=
  fun circumstance retained => ⟨response, uniform circumstance retained⟩

inductive SupportCase where
  | leftReady
  | rightReady
  | noHandover
  deriving DecidableEq, Repr

inductive Response where
  | keep
  | restore
  | leftHandover
  | rightHandover
  deriving DecidableEq, Repr

inductive Stage where
  | opening
  | middle
  | closing
  deriving DecidableEq, Repr

structure History where
  support : Stage → Bool
  targetFormed : Bool

def maintained (target : Bool) : History where
  support := fun _ => true
  targetFormed := target

def restored : History where
  support := fun stage => match stage with
    | .opening => true
    | .middle => false
    | .closing => true
  targetFormed := true

def endpoint (history : History) : Bool × Bool :=
  (history.support .closing, history.targetFormed)

def interruption (history : History) : Prop :=
  ∃ stage, history.support stage = false

def handoverProblem : Problem SupportCase Response History where
  feasible := fun circumstance response => match response with
    | .keep | .restore => True
    | .leftHandover => circumstance = .leftReady
    | .rightHandover => circumstance = .rightReady
  continuation := fun _ response => match response with
    | .keep => maintained false
    | .restore => restored
    | .leftHandover | .rightHandover => maintained true
  target := fun history => history.targetFormed = true
  loss := interruption

def unresolvedSide (circumstance : SupportCase) : Prop :=
  circumstance = .leftReady ∨ circumstance = .rightReady

def onlyNoHandover (circumstance : SupportCase) : Prop :=
  circumstance = .noHandover

theorem restoration_matches_endpoint_but_retains_interruption :
    endpoint restored = endpoint (maintained true) ∧
    interruption restored ∧ ¬ interruption (maintained true) := by
  refine ⟨rfl, ⟨.middle, rfl⟩, ?_⟩
  rintro ⟨stage, loss⟩
  cases loss

theorem absent_handover_makes_interruption_necessary :
    NecessaryLoss handoverProblem .noHandover := by
  refine ⟨⟨.restore, trivial, rfl⟩, ?_⟩
  intro response successful
  cases response with
  | keep => cases successful.2
  | restore => exact ⟨.middle, rfl⟩
  | leftHandover => cases successful.1
  | rightHandover => cases successful.1

theorem available_handovers_are_actual_lossless_alternatives :
    LosslessSuccess handoverProblem .leftReady .leftHandover ∧
    LosslessSuccess handoverProblem .rightReady .rightHandover := by
  constructor <;> refine ⟨⟨rfl, rfl⟩, ?_⟩ <;>
    rintro ⟨stage, loss⟩ <;> cases loss

theorem truthful_identification_can_resolve_uncertain_necessity :
    ¬ Certain (fun _ : SupportCase => True) (NecessaryLoss handoverProblem) ∧
    onlyNoHandover .noHandover ∧
    Certain onlyNoHandover (NecessaryLoss handoverProblem) := by
  refine ⟨?_, rfl, ?_⟩
  · intro certified
    exact actual_alternative_refutes_necessity
      available_handovers_are_actual_lossless_alternatives.1
      (certified .leftReady trivial)
  · intro circumstance retained
    cases retained
    exact absent_handover_makes_interruption_necessary

theorem deleting_actual_circumstance_fabricates_necessity :
    Certain onlyNoHandover (NecessaryLoss handoverProblem) ∧
    ¬ onlyNoHandover .leftReady ∧
    ¬ NecessaryLoss handoverProblem .leftReady := by
  refine ⟨truthful_identification_can_resolve_uncertain_necessity.2.2, ?_, ?_⟩
  · intro impossible
    cases impossible
  · exact actual_alternative_refutes_necessity
      available_handovers_are_actual_lossless_alternatives.1

theorem pointwise_routes_do_not_supply_uniform_response :
    Certain unresolvedSide
      (fun circumstance => ∃ response, LosslessSuccess handoverProblem circumstance response) ∧
    ¬ ∃ response, UniformLossless handoverProblem unresolvedSide response := by
  constructor
  · intro circumstance retained
    rcases retained with rfl | rfl
    · exact ⟨.leftHandover, available_handovers_are_actual_lossless_alternatives.1⟩
    · exact ⟨.rightHandover, available_handovers_are_actual_lossless_alternatives.2⟩
  · rintro ⟨response, uniform⟩
    cases response with
    | keep =>
        have successful := uniform .leftReady (Or.inl rfl)
        cases successful.1.2
    | restore =>
        have successful := uniform .leftReady (Or.inl rfl)
        exact successful.2 ⟨.middle, rfl⟩
    | leftHandover =>
        have successful := uniform .rightReady (Or.inr rfl)
        cases successful.1.1
    | rightHandover =>
        have successful := uniform .leftReady (Or.inl rfl)
        cases successful.1.1

theorem conditional_necessity_allows_lossless_nonattainment :
    NecessaryLoss handoverProblem .noHandover ∧
    handoverProblem.feasible .noHandover .keep ∧
    ¬ handoverProblem.loss (handoverProblem.continuation .noHandover .keep) ∧
    ¬ handoverProblem.target (handoverProblem.continuation .noHandover .keep) := by
  refine ⟨absent_handover_makes_interruption_necessary, trivial, ?_, ?_⟩
  · rintro ⟨stage, loss⟩
    cases loss
  · intro formed
    cases formed

end GenerativeTradeoff
