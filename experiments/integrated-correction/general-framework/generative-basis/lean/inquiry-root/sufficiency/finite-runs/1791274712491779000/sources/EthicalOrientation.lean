import DynamicConsequences

/-!
# Operational differences and the direction of an evaluative extension

This module derives an operational preorder from the unchanged Process/Trace
semantics: inclusion of feasible finite action words. It proves composition and
exact-projection properties. It then uses the EXISTING toggle process to compare
its empty history with an actual two-event cycle under the same law and with the
same initial and final state. No event law, reward, patient interpretation, or
ethical premise is added.

History-length order and its converse are both reflexive, transitive, invariant
under action renaming, and independent of annotations attached to the histories.
They rank those histories oppositely, although both have the same future-word
profile. This is exact non-entailment from the specified coherence/invariance
constraints, not impossibility of every richer ethical justification. Naming
one orientation morally correct would require a further justification that is
not supplied by a definition here. The annotations are not generated selves;
the invariance test only states what these mathematical comparisons depend on.

Continuation inclusion concerns finite existential word feasibility, not
infinite sustainability, experienced adversity, permission, or actual relief.
History length measures event count, not value or patient welfare.
-/

namespace Generative.EthicalOrientation

universe u v w

/-- An objective operational comparison relative to a declared process. -/
def ContinuationLe {State : Type u} {Action : Type v}
    (P : Process State Action) (s t : State) : Prop :=
  ∀ word, Feasible P s word → Feasible P t word

/-- Algebraic coherence alone; no ethical correctness is encoded here. -/
def PreorderLaws {State : Type u} (R : State → State → Prop) : Prop :=
  (∀ s, R s s) ∧ (∀ s t r, R s t → R t r → R s r)

def converse {State : Type u} (R : State → State → Prop) : State → State → Prop :=
  fun s t => R t s

def pullback {State : Type u} {Other : Type w}
    (q : State → Other) (R : Other → Other → Prop) : State → State → Prop :=
  fun s t => R (q s) (q t)

/-- Invariance on the stated projection fibers, not a definition of moral objectivity. -/
def FiberInvariant {State : Type u} {Other : Type w}
    (q : State → Other) (R : State → State → Prop) : Prop :=
  ∀ s s' t t', q s = q s' → q t = q t' → (R s t ↔ R s' t')

theorem continuation_preorder {State : Type u} {Action : Type v}
    (P : Process State Action) : PreorderLaws (ContinuationLe P) := by
  constructor
  · intro s word h
    exact h
  · intro s t r hst htr word h
    exact htr word (hst word h)

theorem converse_preorder {State : Type u} {R : State → State → Prop}
    (h : PreorderLaws R) : PreorderLaws (converse R) := by
  constructor
  · exact h.1
  · intro s t r hst htr
    exact h.2 r t s htr hst

theorem pullback_preorder {State : Type u} {Other : Type w}
    (q : State → Other) {R : Other → Other → Prop}
    (h : PreorderLaws R) : PreorderLaws (pullback q R) := by
  constructor
  · intro s
    exact h.1 (q s)
  · intro s t r hst htr
    exact h.2 (q s) (q t) (q r) hst htr

theorem pullback_fiber_invariant {State : Type u} {Other : Type w}
    (q : State → Other) (R : Other → Other → Prop) :
    FiberInvariant q (pullback q R) := by
  intro s s' t t' hs ht
  change R (q s) (q t) ↔ R (q s') (q t')
  exact hs ▸ ht ▸ Iff.rfl

/-- Inclusion survives the core's synchronous intersection of word constraints. -/
theorem continuation_product_mono
    {State : Type u} {Other : Type w} {Action : Type v}
    {P : Process State Action} {Q : Process Other Action}
    {s t : State} {q r : Other}
    (hp : ContinuationLe P s t) (hq : ContinuationLe Q q r) :
    ContinuationLe (productProcess P Q) (s, q) (t, r) := by
  intro word h
  obtain ⟨left, right⟩ := feasible_product_iff.mp h
  exact feasible_product_iff.mpr ⟨hp word left, hq word right⟩

/-- Exact feasible-word representations preserve and reflect this comparison. -/
theorem continuation_projection_iff
    {State : Type u} {Other : Type w} {Action : Type v}
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    (hexact : ∀ s word, Feasible P s word ↔ Feasible Q (q s) word)
    (s t : State) :
    ContinuationLe P s t ↔ ContinuationLe Q (q s) (q t) := by
  constructor
  · intro h word hw
    exact (hexact t word).mp (h word ((hexact s word).mpr hw))
  · intro h word hw
    exact (hexact t word).mpr (h word ((hexact s word).mp hw))

/-- A history statistic already available without an owner or reward variable. -/
def HistoryLengthLe {Action : Type v} (xs ys : List Action) : Prop :=
  xs.length ≤ ys.length

/-- Direct structural proof avoids importing extensionality through rewriting. -/
theorem history_length_map {Action : Type v} {Other : Type w}
    (f : Action → Other) (word : List Action) :
    (word.map f).length = word.length := by
  induction word with
  | nil => exact Eq.refl 0
  | cons a word ih => exact congrArg Nat.succ ih

theorem history_length_preorder {Action : Type v} :
    PreorderLaws (HistoryLengthLe (Action := Action)) := by
  constructor
  · intro word
    exact Nat.le_refl word.length
  · intro xs ys zs hxy hyz
    exact Nat.le_trans hxy hyz

/-- Even non-injective renaming preserves these two comparisons.
This does not assert that renaming preserves the process's admissible histories. -/
theorem history_orders_renaming_invariant {Action : Type v} {Other : Type w}
    (f : Action → Other) (xs ys : List Action) :
    (HistoryLengthLe (xs.map f) (ys.map f) ↔ HistoryLengthLe xs ys) ∧
      (converse HistoryLengthLe (xs.map f) (ys.map f) ↔
        converse HistoryLengthLe xs ys) := by
  have hx := history_length_map f xs
  have hy := history_length_map f ys
  constructor
  · change (xs.map f).length ≤ (ys.map f).length ↔ xs.length ≤ ys.length
    exact hx ▸ hy ▸ Iff.rfl
  · change (ys.map f).length ≤ (xs.map f).length ↔ ys.length ≤ xs.length
    exact hy ▸ hx ▸ Iff.rfl

/-- Descriptive annotations are projected away; they are not additional dynamics. -/
def growthOrder : (List Unit × Bool) → (List Unit × Bool) → Prop :=
  pullback Prod.fst HistoryLengthLe

def reverseGrowthOrder : (List Unit × Bool) → (List Unit × Bool) → Prop :=
  pullback Prod.fst (converse HistoryLengthLe)

/-- Count has a strict factual orientation once 'more events' is the stated comparison. -/
theorem two_events_strictly_longer :
    HistoryLengthLe ([] : List Unit) [(), ()] ∧
      ¬ HistoryLengthLe [(), ()] ([] : List Unit) := by
  constructor
  · exact Nat.zero_le 2
  · intro h
    exact Nat.not_succ_le_zero 1 h

/-- Invariance and coherent ordering hold equally in both directions. -/
theorem opposed_coherent_annotation_invariant_orders :
    PreorderLaws growthOrder ∧ PreorderLaws reverseGrowthOrder ∧
      FiberInvariant Prod.fst growthOrder ∧ FiberInvariant Prod.fst reverseGrowthOrder ∧
      growthOrder ([], false) ([(), ()], true) ∧
      ¬ growthOrder ([(), ()], true) ([], false) ∧
      reverseGrowthOrder ([(), ()], true) ([], false) ∧
      ¬ reverseGrowthOrder ([], false) ([(), ()], true) :=
  ⟨pullback_preorder Prod.fst history_length_preorder,
    pullback_preorder Prod.fst (converse_preorder history_length_preorder),
    pullback_fiber_invariant _ _, pullback_fiber_invariant _ _,
    two_events_strictly_longer.1, two_events_strictly_longer.2,
    two_events_strictly_longer.1, two_events_strictly_longer.2⟩

/-- Exact failure of this proposed selection criterion, with no global moral premise. -/
theorem coherence_and_annotation_invariance_do_not_select_growth :
    ¬ (∀ R : (List Unit × Bool) → (List Unit × Bool) → Prop,
      PreorderLaws R → FiberInvariant Prod.fst R →
      R ([], false) ([(), ()], true)) := by
  intro h
  have facts := opposed_coherent_annotation_invariant_orders
  exact facts.2.2.2.2.2.2.2 (h reverseGrowthOrder facts.2.1 facts.2.2.2.1)

/-- The comparison concerns two admissible histories of one existing process,
with the same start/end state, rather than unvisited carrier points. -/
theorem toggle_same_endpoint_histories :
    Trace Deeper.toggle false [] false ∧
      Trace Deeper.toggle false [(), ()] false :=
  ⟨.nil false, Deeper.toggle_two_event_cycle false⟩

/-- All states of this total process have the same finite existential options. -/
theorem toggle_continuation_equivalent (s t : Bool) :
    ContinuationLe Deeper.toggle s t ∧ ContinuationLe Deeper.toggle t s := by
  constructor
  · intro word _
    exact Deeper.feasible_of_step_total Deeper.toggle_total t word
  · intro word _
    exact Deeper.feasible_of_step_total Deeper.toggle_total s word

/-- Even after retaining the entire compared histories, their residual future-word
profiles agree in this existing process. Length is not a capability improvement. -/
theorem toggle_compared_histories_same_residual (word : List Unit) :
    Feasible Deeper.toggle false ([] ++ word) ↔
      Feasible Deeper.toggle false ([(), ()] ++ word) := by
  constructor
  · intro _
    exact Deeper.feasible_of_step_total Deeper.toggle_total false ([(), ()] ++ word)
  · intro _
    exact Deeper.feasible_of_step_total Deeper.toggle_total false ([] ++ word)

/-- Histories, endpoints and residuals are held fixed while the candidate orientation
varies. The false conclusion is selection by coherence/invariance alone. -/
theorem actual_histories_with_unselected_orientation :
    (Trace Deeper.toggle false [] false ∧
      Trace Deeper.toggle false [(), ()] false) ∧
    (∀ word, Feasible Deeper.toggle false ([] ++ word) ↔
      Feasible Deeper.toggle false ([(), ()] ++ word)) ∧
    ¬ (∀ R : (List Unit × Bool) → (List Unit × Bool) → Prop,
      PreorderLaws R → FiberInvariant Prod.fst R →
      R ([], false) ([(), ()], true)) :=
  ⟨toggle_same_endpoint_histories, toggle_compared_histories_same_residual,
    coherence_and_annotation_invariance_do_not_select_growth⟩

/-- Nonempty recurrence does not supply strict improvement on every event. -/
theorem toggle_has_no_every_step_strict_order :
    ¬ (∃ R : Bool → Bool → Prop,
      (∀ s, ¬ R s s) ∧
      (∀ s t r, R s t → R t r → R s r) ∧
      (∀ s a t, Deeper.toggle.step s a t → R s t)) := by
  rintro ⟨R, hirr, htrans, hstep⟩
  have forward : R false true := hstep false () true (Eq.refl true)
  have backward : R true false := hstep true () false (Eq.refl false)
  exact hirr false (htrans false true false forward backward)

end Generative.EthicalOrientation

#print axioms Generative.EthicalOrientation.continuation_preorder
#print axioms Generative.EthicalOrientation.converse_preorder
#print axioms Generative.EthicalOrientation.pullback_preorder
#print axioms Generative.EthicalOrientation.pullback_fiber_invariant
#print axioms Generative.EthicalOrientation.continuation_product_mono
#print axioms Generative.EthicalOrientation.continuation_projection_iff
#print axioms Generative.EthicalOrientation.history_length_map
#print axioms Generative.EthicalOrientation.history_length_preorder
#print axioms Generative.EthicalOrientation.history_orders_renaming_invariant
#print axioms Generative.EthicalOrientation.two_events_strictly_longer
#print axioms Generative.EthicalOrientation.opposed_coherent_annotation_invariant_orders
#print axioms Generative.EthicalOrientation.coherence_and_annotation_invariance_do_not_select_growth
#print axioms Generative.EthicalOrientation.toggle_same_endpoint_histories
#print axioms Generative.EthicalOrientation.toggle_continuation_equivalent
#print axioms Generative.EthicalOrientation.toggle_compared_histories_same_residual
#print axioms Generative.EthicalOrientation.actual_histories_with_unselected_orientation
#print axioms Generative.EthicalOrientation.toggle_has_no_every_step_strict_order
