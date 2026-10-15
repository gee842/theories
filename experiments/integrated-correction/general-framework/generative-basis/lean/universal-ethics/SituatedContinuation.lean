import GenerativeCore -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Run.renewal_recurs`, `Becoming.Invariant.run`, `ContinuationRenewal.renewal_within_rank_plus_one_steps` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md
import ContinuationRenewal
import SituatedRenewal

/-!
General situated implementation of continuation requirements.

States describe selected relations in one process. An allowed action is a
context-dependent certificate, not an ethical verdict. The process, invariant,
independently identified renewal event and progress rank are explicit premises.
The rank restricts waiting between renewals; it is not a universal resource.

The first result covers every actual compliant history, including all outcomes
allowed by a nondeterministic transition law. The constructive result supplies
an actual history from explicit implementation functions, without choice. It
does not synthesize those functions or assume all contexts are observable.
-/

namespace Generative.SituatedContinuation

universe u v w

variable {State : Type u} {Action : Type v}

/-- Explicit iteration; each successor uses the state actually reached. -/
def trajectory (next : State → State) (initial : State) : Nat → State
  | 0 => initial
  | n + 1 => next (trajectory next initial n)

/-- Existence of a whole admissible continuation satisfying an independently
specified state condition. No ethical predicate or decision procedure is added. -/
def HasContinuation (P : Process State Action) (alive : State → Prop)
    (s : State) : Prop :=
  ∃ states : Nat → State, ∃ actions : Nat → Action,
    states 0 = s ∧
    (∀ n, P.step (states n) (actions n) (states (n + 1))) ∧
    ∀ n, alive (states n)

/-- The suffix uses the exact state reached; no reserves or relations reset. -/
theorem actual_suffix_continues (P : Process State Action) (alive : State → Prop)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (lives : ∀ n, alive (states n)) (start : Nat) :
    HasContinuation P alive (states start) := by
  refine ⟨fun n => states (start + n), fun n => actions (start + n), ?_, ?_, ?_⟩
  · exact congrArg states (Nat.add_zero start)
  · intro n
    change P.step (states (start + n)) (actions (start + n)) (states (start + (n + 1)))
    rw [← Nat.add_assoc]
    exact steps (start + n)
  · intro n; exact lives (start + n)

/-- An actually continuing history cannot take an action all of whose allowed
outcomes eliminate that same continuation. It does not follow that a merely
possible favorable outcome guarantees success under nondeterminism. -/
theorem excludes_all_routes_cannot_sustain (P : Process State Action)
    (alive : State → Prop) (s : State) (a : Action)
    (cuts : ∀ t, P.step s a t → ¬ HasContinuation P alive t) :
    ¬ ∃ states : Nat → State, ∃ actions : Nat → Action,
      states 0 = s ∧ actions 0 = a ∧
      (∀ n, P.step (states n) (actions n) (states (n + 1))) ∧
      ∀ n, alive (states n) := by
  rintro ⟨states, actions, starts, first, steps, lives⟩
  have step := steps 0
  rw [starts, first] at step
  exact cuts (states 1) step (actual_suffix_continues P alive states actions steps lives 1)

/-- Joint continuation supplies every component condition on the SAME history.
The converse from separately existing histories is deliberately not assumed. -/
theorem joint_continuation_supplies_components {Index : Type w}
    (P : Process State Action) (condition : Index → State → Prop) (s : State)
    (joint : HasContinuation P (fun t => ∀ i, condition i t) s) :
    ∀ i, HasContinuation P (condition i) s := by
  obtain ⟨states, actions, starts, steps, satisfies⟩ := joint
  intro i
  exact ⟨states, actions, starts, steps, fun n => satisfies n i⟩

/-- One actual continuation jointly carries the responses of all required
dependencies. The demand premise is identified independently on admissible
living histories. Existence is supplied here and constructed by the later
implementation theorem when its stronger certificate is available. -/
theorem continuation_realizes_required_dependencies {Index : Type w}
    {Route : Type v} [DecidableEq Route]
    (P : Process State Action) (alive : State → Prop)
    (law : SituatedRenewal.DependencyLaw P Index Route) (initial : State)
    (existsContinuation : HasContinuation P alive initial)
    (required : ∀ states : Nat → State, ∀ actions : Nat → Action,
      states 0 = initial →
      (∀ n, P.step (states n) (actions n) (states (n + 1))) →
      (∀ n, alive (states n)) →
      ∀ i start, ∃ length, law.remaining i (states start) <
        SituatedRenewal.totalDemand law i states actions start length) :
    ∃ states : Nat → State, ∃ actions : Nat → Action,
      states 0 = initial ∧
      (∀ n, P.step (states n) (actions n) (states (n + 1))) ∧
      (∀ n, alive (states n)) ∧
      ∀ i start, ∃ n, start ≤ n ∧
        SituatedRenewal.Response law i (states n) (actions n) (states (n + 1)) := by
  obtain ⟨states, actions, starts, steps, lives⟩ := existsContinuation
  have responses := SituatedRenewal.every_required_dependency_recurrently_responds
    law states actions steps (required states actions starts steps lives)
  refine ⟨states, actions, starts, steps, lives, ?_⟩
  intro i start
  obtain ⟨n, after, _, responded⟩ := responses i start
  exact ⟨n, after, responded⟩

/-- Local rules retain their invariant along every actual compliant history. -/
theorem rules_retain_invariant (P : Process State Action)
    (Inv : State → Prop) (allowed : State → Action → Prop)
    (retains : ∀ s a t, Inv s → allowed s a → P.step s a t → Inv t)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (compliant : ∀ n, allowed (states n) (actions n))
    (initial : Inv (states 0)) : ∀ n, Inv (states n) := by
  intro n
  induction n with
  | zero => exact initial
  | succ n ih => exact retains _ _ _ ih (compliant n) (steps n)

/-- A common local certificate yields actual bounded renewal on every compliant
history. The interval contains rank(start)+1 candidate transitions. -/
theorem certified_history_renews (P : Process State Action)
    (Inv : State → Prop) (allowed : State → Action → Prop)
    (renewal : State → Action → State → Prop) (rank : State → Nat)
    (retains : ∀ s a t, Inv s → allowed s a → P.step s a t → Inv t)
    (progress : ∀ s a t, Inv s → allowed s a → P.step s a t →
      renewal s a t ∨ rank t < rank s)
    (states : Nat → State) (actions : Nat → Action)
    (steps : ∀ n, P.step (states n) (actions n) (states (n + 1)))
    (compliant : ∀ n, allowed (states n) (actions n))
    (initial : Inv (states 0)) :
    (∀ n, Inv (states n)) ∧
      ∀ start, ∃ n, start ≤ n ∧ n ≤ start + rank (states start) ∧
        renewal (states n) (actions n) (states (n + 1)) := by
  have maintained := rules_retain_invariant P Inv allowed retains states actions
    steps compliant initial
  refine ⟨maintained, ?_⟩
  intro start
  -- The positive disjunction supplies the witness constructively; no decision
  -- procedure for arbitrary renewal predicates is required.
  have bounded : ∀ bound start, rank (states start) ≤ bound →
      ∃ n, start ≤ n ∧ n ≤ start + bound ∧
        renewal (states n) (actions n) (states (n + 1)) := by
    intro bound
    induction bound with
    | zero =>
      intro start bound
      cases progress _ _ _ (maintained start) (compliant start) (steps start) with
      | inl renewed => exact ⟨start, Nat.le_refl _, Nat.le_add_right _ _, renewed⟩
      | inr lower => exact False.elim (Nat.not_lt_zero _ (Nat.lt_of_lt_of_le lower bound))
    | succ bound ih =>
      intro start boundAtStart
      cases progress _ _ _ (maintained start) (compliant start) (steps start) with
      | inl renewed => exact ⟨start, Nat.le_refl _, Nat.le_add_right _ _, renewed⟩
      | inr lower =>
        have boundNext : rank (states (start + 1)) ≤ bound :=
          Nat.le_of_lt_succ (Nat.lt_of_lt_of_le lower boundAtStart)
        obtain ⟨n, after, before, renewed⟩ := ih (start + 1) boundNext
        refine ⟨n, Nat.le_trans (Nat.le_succ start) after, ?_, renewed⟩
        exact (Nat.add_right_comm start 1 bound) ▸ before
  exact bounded (rank (states start)) start (Nat.le_refl _)

/-- A supplied, actually admissible implementation constructs a sustaining
history. `alive` is an independently specified represented condition, not good. -/
theorem implemented_rules_sustain (P : Process State Action)
    (Inv alive : State → Prop) (allowed : State → Action → Prop)
    (renewal : State → Action → State → Prop) (rank : State → Nat)
    (realizes : ∀ s, Inv s → alive s)
    (retains : ∀ s a t, Inv s → allowed s a → P.step s a t → Inv t)
    (progress : ∀ s a t, Inv s → allowed s a → P.step s a t →
      renewal s a t ∨ rank t < rank s)
    (choose : State → Action) (next : State → State)
    (implemented : ∀ s, Inv s → allowed s (choose s) ∧ P.step s (choose s) (next s))
    (initial : State) (starts : Inv initial) :
    ∃ states : Nat → State, ∃ actions : Nat → Action,
      states 0 = initial ∧
      (∀ n, P.step (states n) (actions n) (states (n + 1))) ∧
      (∀ n, allowed (states n) (actions n)) ∧
      (∀ n, alive (states n)) ∧
      ∀ start, ∃ n, start ≤ n ∧ n ≤ start + rank (states start) ∧
        renewal (states n) (actions n) (states (n + 1)) := by
  let states := trajectory next initial
  let actions := fun n => choose (states n)
  have maintained : ∀ n, Inv (states n) := by
    intro n
    induction n with
    | zero => exact starts
    | succ n ih =>
      exact retains _ _ _ ih (implemented _ ih).1 (implemented _ ih).2
  have steps : ∀ n, P.step (states n) (actions n) (states (n + 1)) :=
    fun n => (implemented _ (maintained n)).2
  have compliant : ∀ n, allowed (states n) (actions n) :=
    fun n => (implemented _ (maintained n)).1
  have renewed := certified_history_renews P Inv allowed renewal rank retains
    progress states actions steps compliant starts
  exact ⟨states, actions, rfl, steps, compliant,
    fun n => realizes _ (maintained n), renewed.2⟩

/-- A disjunctive requirement preserves alternative implementations. -/
theorem alternatives_remain_alternatives
    (left right : State → Action → Prop) (s : State) (a : Action)
    (adequate : left s a ∨ right s a) : ¬ (¬ left s a ∧ ¬ right s a) := by
  rintro ⟨noLeft, noRight⟩
  cases adequate with
  | inl h => exact noLeft h
  | inr h => exact noRight h

/-! A complete elementary implementation with two adequate restoration routes.
The same condition is restored; no additional complexity is inferred. -/

inductive Event where
  | use
  | repair
  | replace

def supportProcess : Process Bool Event where
  step s a t := match a with
    | .use => s = true ∧ t = false
    | .repair => s = false ∧ t = true
    | .replace => s = false ∧ t = true

def restorative (_ : Bool) (a : Event) (_ : Bool) : Prop :=
  a = .repair ∨ a = .replace

def supportRank (s : Bool) : Nat := if s then 1 else 0

theorem support_progress (s : Bool) (a : Event) (t : Bool)
    (step : supportProcess.step s a t) :
    restorative s a t ∨ supportRank t < supportRank s := by
  cases a with
  | use =>
    obtain ⟨rfl, rfl⟩ := step
    exact .inr (by decide)
  | repair => exact .inl (.inl rfl)
  | replace => exact .inl (.inr rfl)

def repairChoice (s : Bool) : Event := if s then .use else .repair
def replacementChoice (s : Bool) : Event := if s then .use else .replace

theorem repair_implements (s : Bool) :
    supportProcess.step s (repairChoice s) (!s) := by
  cases s <;> exact ⟨rfl, rfl⟩

theorem replacement_implements (s : Bool) :
    supportProcess.step s (replacementChoice s) (!s) := by
  cases s <;> exact ⟨rfl, rfl⟩

theorem repair_never_replaces (s : Bool) : repairChoice s ≠ .replace := by
  cases s <;> intro h <;> cases h

theorem replacement_never_repairs (s : Bool) : replacementChoice s ≠ .repair := by
  cases s <;> intro h <;> cases h

/-- Both routes sustain actual recurrence. Neither named recipe is necessary. -/
theorem adequate_alternative_histories :
    (∃ states : Nat → Bool, ∃ actions : Nat → Event,
      (∀ n, supportProcess.step (states n) (actions n) (states (n + 1))) ∧
      (∀ start, ∃ n, start ≤ n ∧ restorative (states n) (actions n) (states (n + 1))) ∧
      ∀ n, actions n ≠ .replace) ∧
    (∃ states : Nat → Bool, ∃ actions : Nat → Event,
      (∀ n, supportProcess.step (states n) (actions n) (states (n + 1))) ∧
      (∀ start, ∃ n, start ≤ n ∧ restorative (states n) (actions n) (states (n + 1))) ∧
      ∀ n, actions n ≠ .repair) := by
  have build : ∀ choose : Bool → Event,
      (∀ s, supportProcess.step s (choose s) (!s)) →
      ∃ states : Nat → Bool,
        (∀ n, supportProcess.step (states n) (choose (states n)) (states (n + 1))) ∧
        ∀ start, ∃ n, start ≤ n ∧ restorative (states n) (choose (states n)) (states (n + 1)) := by
    intro choose implementation
    let states := trajectory Bool.not true
    have steps : ∀ n, supportProcess.step (states n) (choose (states n)) (states (n + 1)) :=
      fun n => implementation (states n)
    have cert := certified_history_renews supportProcess (fun _ => True) (fun _ _ => True)
      restorative supportRank (by intros; trivial)
      (fun s a t _ _ h => support_progress s a t h)
      states (fun n => choose (states n)) steps (by intros; trivial) trivial
    refine ⟨states, steps, ?_⟩
    intro start
    obtain ⟨n, after, _, renewed⟩ := cert.2 start
    exact ⟨n, after, renewed⟩
  obtain ⟨left, leftSteps, leftRenews⟩ := build repairChoice repair_implements
  obtain ⟨right, rightSteps, rightRenews⟩ := build replacementChoice replacement_implements
  exact ⟨⟨left, fun n => repairChoice (left n), leftSteps, leftRenews,
      fun n => repair_never_replaces (left n)⟩,
    ⟨right, fun n => replacementChoice (right n), rightSteps, rightRenews,
      fun n => replacement_never_repairs (right n)⟩⟩

/-! Keeping an attainable achievement available does not force its realization. -/

inductive Opportunity where
  | wait
  | finish

def opportunityProcess : Process Bool Opportunity where
  step s a t := match a with
    | .wait => t = s
    | .finish => t = true

/-- Every reached state has an actual one-step completion route. The supplied
waiting history is admissible and nevertheless never completes. -/
theorem permanent_opportunity_without_completion :
    ∃ states : Nat → Bool, ∃ actions : Nat → Opportunity,
      (∀ n, opportunityProcess.step (states n) (actions n) (states (n + 1))) ∧
      (∀ n, ∃ t, opportunityProcess.step (states n) .finish t ∧ t = true) ∧
      (∀ n, states n = false) ∧
      ¬ ∃ n, actions n = .finish := by
  refine ⟨fun _ => false, fun _ => .wait, ?_, ?_, ?_, ?_⟩
  · intro n; rfl
  · intro n; exact ⟨true, rfl, rfl⟩
  · intro n; rfl
  · rintro ⟨n, impossible⟩; cases impossible

end Generative.SituatedContinuation

#print axioms Generative.SituatedContinuation.trajectory
#print axioms Generative.SituatedContinuation.HasContinuation
#print axioms Generative.SituatedContinuation.actual_suffix_continues
#print axioms Generative.SituatedContinuation.excludes_all_routes_cannot_sustain
#print axioms Generative.SituatedContinuation.joint_continuation_supplies_components
#print axioms Generative.SituatedContinuation.continuation_realizes_required_dependencies
#print axioms Generative.SituatedContinuation.rules_retain_invariant
#print axioms Generative.SituatedContinuation.certified_history_renews
#print axioms Generative.SituatedContinuation.implemented_rules_sustain
#print axioms Generative.SituatedContinuation.alternatives_remain_alternatives
#print axioms Generative.SituatedContinuation.Event
#print axioms Generative.SituatedContinuation.supportProcess
#print axioms Generative.SituatedContinuation.restorative
#print axioms Generative.SituatedContinuation.supportRank
#print axioms Generative.SituatedContinuation.support_progress
#print axioms Generative.SituatedContinuation.repairChoice
#print axioms Generative.SituatedContinuation.replacementChoice
#print axioms Generative.SituatedContinuation.repair_implements
#print axioms Generative.SituatedContinuation.replacement_implements
#print axioms Generative.SituatedContinuation.repair_never_replaces
#print axioms Generative.SituatedContinuation.replacement_never_repairs
#print axioms Generative.SituatedContinuation.adequate_alternative_histories
#print axioms Generative.SituatedContinuation.Opportunity
#print axioms Generative.SituatedContinuation.opportunityProcess
#print axioms Generative.SituatedContinuation.permanent_opportunity_without_completion
