/-! 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Readout.reading_single_iff`, `Becoming.Readout.law_through_iff`, `Becoming.Readout.foldl_semiconj` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md
# A formed perspective's present and future correspondence

The shared process state can include acquired records, selective dispositions,
and changing material relations. `step` is its supplied, closed deterministic
continuation law; `observe` is the specified readout of a perspective within
that state. The later action-indexed version quantifies over a supplied repertoire
and finite words under one total law. No subject/world split, scalar value,
probability, or order law is assumed. A second supplied relation `R` states the
comparison to be preserved.

The older `Generative.SelfFormation.exact_summary_exists_iff` already checks
factorization of finite feasibility profiles. This companion applies that
discipline to arbitrary binary comparisons and their evolution. Its distinctive
test is whether present representational equality remains sound under the
actual continuation law. It does not derive an ethical comparison or a formed
readout mechanism.
-/

namespace Perspectival

universe u v w

variable {S : Type u} {O : Type v} {A : Type w}

/-- Iteration of the one supplied law, including its state-dependent selection. -/
def evolve (step : S → S) : Nat → S → S
  | 0, s => s
  | n + 1, s => step (evolve step n s)

/-- Current representation equality survives one actual transition. -/
def StepCongruent (step : S → S) (observe : S → O) : Prop :=
  ∀ x y, observe x = observe y → observe (step x) = observe (step y)

/-- No pairwise comparison is changed by substituting observational equals. -/
def Saturated (observe : S → O) (R : S → S → Prop) : Prop :=
  ∀ x x' y y', observe x = observe x' → observe y = observe y' →
    (R x y ↔ R x' y')

def Represents (observe : S → O) (R : S → S → Prop)
    (C : O → O → Prop) : Prop :=
  ∀ x y, C (observe x) (observe y) ↔ R x y

/-- An analysis-level relation; neither a computable decoder nor a new evaluator. -/
def Pooled (observe : S → O) (R : S → S → Prop) (a b : O) : Prop :=
  ∃ x y, observe x = a ∧ observe y = b ∧ R x y

theorem represented_is_saturated {observe : S → O} {R : S → S → Prop}
    {C : O → O → Prop} (h : Represents observe R C) : Saturated observe R := by
  intro x x' y y' hx hy
  constructor
  · intro hxy
    have hc := (h x y).mpr hxy
    exact (h x' y').mp (hx ▸ hy ▸ hc)
  · intro hxy
    have hc := (h x' y').mpr hxy
    exact (h x y).mp (hx.symm ▸ hy.symm ▸ hc)

theorem saturated_is_represented {observe : S → O} {R : S → S → Prop}
    (h : Saturated observe R) : Represents observe R (Pooled observe R) := by
  intro x y
  constructor
  · rintro ⟨x', y', hx, hy, hr⟩
    exact (h x' x y' y hx hy).mp hr
  · intro hr
    exact ⟨x, y, rfl, rfl, hr⟩

/-- This is the binary-relation specialization of the inherited factorization
discipline, not a novel grounding theorem. It needs no order/scalar structure. -/
theorem representation_exists_iff (observe : S → O) (R : S → S → Prop) :
    (∃ C, Represents observe R C) ↔ Saturated observe R := by
  constructor
  · rintro ⟨C, hc⟩
    exact represented_is_saturated hc
  · intro hs
    exact ⟨Pooled observe R, saturated_is_represented hs⟩

/-- A single transition condition suffices at every finite horizon. -/
theorem step_congruence_preserves_futures {step : S → S} {observe : S → O}
    (hc : StepCongruent step observe) (n : Nat) (x y : S)
    (hxy : observe x = observe y) :
    observe (evolve step n x) = observe (evolve step n y) := by
  induction n with
  | zero => exact hxy
  | succ n ih => exact hc _ _ ih

/-- Conversely, an exact prediction of every future readout includes one step.
This equivalence concerns all readouts, a stronger task than one selected R. -/
theorem step_congruence_iff_futures (step : S → S) (observe : S → O) :
    StepCongruent step observe ↔
      ∀ n x y, observe x = observe y →
        observe (evolve step n x) = observe (evolve step n y) := by
  constructor
  · exact step_congruence_preserves_futures
  · intro hf x y hxy
    exact hf 1 x y hxy

def FutureRelation (step : S → S) (R : S → S → Prop) (n : Nat) : S → S → Prop :=
  fun x y => R (evolve step n x) (evolve step n y)

/-- The exact necessary-and-sufficient condition for one selected comparison. -/
theorem future_representation_exists_iff (step : S → S) (observe : S → O)
    (R : S → S → Prop) :
    (∃ C : Nat → O → O → Prop,
      ∀ n, Represents observe (FutureRelation step R n) (C n)) ↔
      ∀ n, Saturated observe (FutureRelation step R n) := by
  constructor
  · rintro ⟨C, hc⟩ n
    exact represented_is_saturated (hc n)
  · intro hs
    exact ⟨fun n => Pooled observe (FutureRelation step R n),
      fun n => saturated_is_represented (hs n)⟩

/-- Practical sufficient test: preserve the current comparison and preserve
observational equality through actual change. It need not be necessary for R. -/
theorem current_and_step_preserve_future_comparison {step : S → S}
    {observe : S → O} {R : S → S → Prop}
    (hs : Saturated observe R) (hc : StepCongruent step observe) :
    ∀ n, Saturated observe (FutureRelation step R n) := by
  intro n x x' y y' hx hy
  exact hs _ _ _ _ (step_congruence_preserves_futures hc n x x' hx)
    (step_congruence_preserves_futures hc n y y' hy)

theorem current_and_step_give_future_representation {step : S → S}
    {observe : S → O} {R : S → S → Prop}
    (hs : Saturated observe R) (hc : StepCongruent step observe) :
    ∃ C : Nat → O → O → Prop,
      ∀ n, Represents observe (FutureRelation step R n) (C n) :=
  (future_representation_exists_iff step observe R).mpr
    (current_and_step_preserve_future_comparison hs hc)

/-- A real omitted continuation distinguishes two members of one current
representation class. No decoder of that current representation can fix it. -/
theorem omitted_future_obstructs_representation {step : S → S}
    {observe : S → O} {R : S → S → Prop} (n : Nat)
    (x x' y y' : S) (hx : observe x = observe x') (hy : observe y = observe y')
    (hyes : FutureRelation step R n x y)
    (hno : ¬ FutureRelation step R n x' y') :
    ¬ ∃ C, Represents observe (FutureRelation step R n) C := by
  rintro ⟨C, hc⟩
  exact hno ((represented_is_saturated hc x x' y y' hx hy).mp hyes)

/-! ## Several supplied continuations: action-indexed laws

`A` is a supplied repertoire of event/action labels in one modeled unfolding.
It does not denote a fundamentally external controller. These results quantify
over specified words, not an acquired policy, and assume the law is total on S
and A. An application must represent blocking/failure or restrict its repertoire
appropriately; no theorem here invents feasible interventions.
-/

/-- Execute a specified finite word using the supplied action-indexed law. -/
def follow (step : S → A → S) : List A → S → S
  | [], s => s
  | a :: rest, s => follow step rest (step s a)

/-- Preservation must hold uniformly for every label in the stated repertoire. -/
def ActionCongruent (step : S → A → S) (observe : S → O) : Prop :=
  ∀ a x y, observe x = observe y → observe (step x a) = observe (step y a)

theorem action_congruence_preserves_words {step : S → A → S} {observe : S → O}
    (hc : ActionCongruent step observe) (word : List A) (x y : S)
    (hxy : observe x = observe y) :
    observe (follow step word x) = observe (follow step word y) := by
  induction word generalizing x y with
  | nil => exact hxy
  | cons a rest ih => exact ih _ _ (hc a x y hxy)

/-- Exactly the criterion for predicting every finite common action word. -/
theorem action_congruence_iff_words (step : S → A → S) (observe : S → O) :
    ActionCongruent step observe ↔
      ∀ word x y, observe x = observe y →
        observe (follow step word x) = observe (follow step word y) := by
  constructor
  · exact action_congruence_preserves_words
  · intro hw a x y hxy
    exact hw [a] x y hxy

/-- Each side can take a different specified continuation. Within a side, a
replacement with the same initial readout must be tested under the same word. -/
def WordComparison (step : S → A → S) (R : S → S → Prop)
    (left right : List A) : S → S → Prop :=
  fun x y => R (follow step left x) (follow step right y)

theorem current_and_action_preserve_word_comparisons {step : S → A → S}
    {observe : S → O} {R : S → S → Prop}
    (hs : Saturated observe R) (hc : ActionCongruent step observe) :
    ∀ left right, Saturated observe (WordComparison step R left right) := by
  intro left right x x' y y' hx hy
  exact hs _ _ _ _ (action_congruence_preserves_words hc left x x' hx)
    (action_congruence_preserves_words hc right y y' hy)

/-- Exact criterion for the selected comparison, again weaker than preservation
of every observable difference under every word. -/
theorem word_representation_exists_iff (step : S → A → S) (observe : S → O)
    (R : S → S → Prop) :
    (∃ C : List A → List A → O → O → Prop,
      ∀ left right, Represents observe (WordComparison step R left right) (C left right)) ↔
      ∀ left right, Saturated observe (WordComparison step R left right) := by
  constructor
  · rintro ⟨C, hc⟩ left right
    exact represented_is_saturated (hc left right)
  · intro hs
    exact ⟨fun left right => Pooled observe (WordComparison step R left right),
      fun left right => saturated_is_represented (hs left right)⟩

/-- Supplying the two words supplies the alternatives to be compared; neither
their ethical standing nor a policy implementing them follows from this result. -/
theorem current_and_action_give_word_representation {step : S → A → S}
    {observe : S → O} {R : S → S → Prop}
    (hs : Saturated observe R) (hc : ActionCongruent step observe) :
    ∃ C : List A → List A → O → O → Prop,
      ∀ left right, Represents observe (WordComparison step R left right) (C left right) :=
  (word_representation_exists_iff step observe R).mpr
    (current_and_action_preserve_word_comparisons hs hc)

/-! ## A concrete shared-law witness with endogenous regime revision

The deliberately minimal state carries three coupled quantities. `count` counts
enacted cycles, `capacity` enables another cycle, and `route` determines whether
that cycle restores the used capacity. A successful un-restored cycle switches
the route to restored activity only when capacity was initially one. At that
point capacity has already become zero, so a changed route cannot retrospectively
enable a further cycle. This is a stated synthetic mechanism, not empirical
cancer dynamics or an ethical diagnosis.
-/

inductive Route where
  | restored
  | unRestored
  deriving DecidableEq, Repr

structure Condition where
  count : Nat
  capacity : Nat
  route : Route
  deriving DecidableEq, Repr

def cycleStep (s : Condition) : Condition :=
  match s.capacity with
  | 0 => s
  | k + 1 =>
    match s.route with
    | .restored => ⟨s.count + 1, k + 1, .restored⟩
    | .unRestored =>
      ⟨s.count + 1, k, if k = 0 then .restored else .unRestored⟩

def initial (route : Route) : Condition := ⟨0, 3, route⟩

/-- The displayed current conditions omit the continuation route. -/
def currentView (s : Condition) : Nat × Nat := (s.count, s.capacity)

/-- A descriptive capacity comparison, with no ethical identification. -/
def CapacityLE (x y : Condition) : Prop := x.capacity ≤ y.capacity

theorem current_capacity_is_represented :
    Represents currentView CapacityLE (fun a b => a.2 ≤ b.2) := by
  intro x y
  exact Iff.rfl

theorem initial_views_agree :
    currentView (initial .restored) = currentView (initial .unRestored) := rfl

theorem current_view_not_step_congruent : ¬ StepCongruent cycleStep currentView := by
  intro hc
  have heq := hc (initial .restored) (initial .unRestored) initial_views_agree
  have hcap : (3 : Nat) = 2 := congrArg Prod.snd heq
  exact (by decide : (3 : Nat) ≠ 2) hcap

theorem current_fidelity_does_not_give_future_fidelity :
    (∃ C, Represents currentView CapacityLE C) ∧
      ¬ ∃ C, Represents currentView (FutureRelation cycleStep CapacityLE 1) C := by
  refine ⟨⟨_, current_capacity_is_represented⟩, ?_⟩
  exact omitted_future_obstructs_representation 1
    (initial .unRestored) (initial .restored)
    (initial .restored) (initial .unRestored)
    initial_views_agree.symm initial_views_agree
    (by change 2 ≤ 3; decide) (by change ¬ (3 ≤ 2); decide)

/-- The cumulative count is identical through three completed cycles. -/
theorem three_cycle_count_histories_agree :
    (List.range 4).map (fun n => (evolve cycleStep n (initial .restored)).count) =
    (List.range 4).map (fun n => (evolve cycleStep n (initial .unRestored)).count) := rfl

theorem third_cycle_has_different_continuation_conditions :
    evolve cycleStep 3 (initial .restored) = ⟨3, 3, .restored⟩ ∧
    evolve cycleStep 3 (initial .unRestored) = ⟨3, 0, .restored⟩ := ⟨rfl, rfl⟩

/-- A now-matching selective route does not repair the already lost capacity. -/
theorem fourth_cycle_diverges_despite_matching_routes :
    evolve cycleStep 4 (initial .restored) = ⟨4, 3, .restored⟩ ∧
    evolve cycleStep 4 (initial .unRestored) = ⟨3, 0, .restored⟩ := ⟨rfl, rfl⟩

/-- Current capacity detects depletion even while cumulative success hides it. -/
theorem one_cycle_exposes_capacity_before_count_diverges :
    (evolve cycleStep 1 (initial .restored)).count =
      (evolve cycleStep 1 (initial .unRestored)).count ∧
    (evolve cycleStep 1 (initial .restored)).capacity ≠
      (evolve cycleStep 1 (initial .unRestored)).capacity := by
  exact ⟨rfl, by decide⟩

/-- Adding the actually governing route re-encodes all three state coordinates.
This is an explicit full-state sufficient witness for the synthetic law, not a
derived compressed or learned field, and not omniscience about an application. -/
def routeView (s : Condition) : Nat × Nat × Route := (s.count, s.capacity, s.route)

theorem route_view_step_congruent : StepCongruent cycleStep routeView := by
  intro x y heq
  cases x with
  | mk xc xk xr =>
    cases y with
    | mk yc yk yr =>
      have hc : xc = yc := congrArg Prod.fst heq
      have hk : xk = yk := congrArg (fun z => z.2.1) heq
      have hr : xr = yr := congrArg (fun z => z.2.2) heq
      cases hc
      cases hk
      cases hr
      rfl

theorem route_view_represents_capacity :
    Represents routeView CapacityLE (fun a b => a.2.1 ≤ b.2.1) := by
  intro x y
  exact Iff.rfl

theorem route_view_preserves_all_future_capacity_comparisons :
    ∃ C : Nat → (Nat × Nat × Route) → (Nat × Nat × Route) → Prop,
      ∀ n, Represents routeView (FutureRelation cycleStep CapacityLE n) (C n) :=
  current_and_step_give_future_representation
    (represented_is_saturated route_view_represents_capacity) route_view_step_congruent

end Perspectival
