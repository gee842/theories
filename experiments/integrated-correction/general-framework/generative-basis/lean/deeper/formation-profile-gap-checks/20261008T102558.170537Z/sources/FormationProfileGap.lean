import ContinuationConditions
import SystemIndividuation

/-!
Test the continuation-only abstraction against the unchanged native formation
process. Correlation changes a relation and later right-hand outcomes while
preserving every feasible event word from the same left reading.

This specializes the already developed endpoint-question method; it does not
claim to discover that trace feasibility can omit outcomes. A missing relation
in this abstraction is not an impossibility of explaining the native process.
-/

namespace Generative.FormationProfileGap
open SystemIndividuation ContinuationConditions

theorem step_lift_same_left {s t other : Bool × Bool} {event : Event}
    (same : s.1 = other.1) (step : process.step s event t) :
    ∃ next, process.step other event next ∧ t.1 = next.1 := by
  cases event with
  | correlate =>
    change t = (s.1, s.1) at step
    cases step
    exact ⟨(other.1, other.1), rfl, same⟩
  | flip =>
    change t = (!s.1, !s.2) at step
    cases step
    exact ⟨(!other.1, !other.2), rfl, congrArg Bool.not same⟩
  | pulse =>
    obtain ⟨guard, rfl⟩ := step
    exact ⟨other, ⟨same.symm.trans guard, rfl⟩, same⟩

theorem trace_lift_same_left {s t : Bool × Bool} {word : List Event}
    (trace : Trace process s word t) :
    ∀ other, s.1 = other.1 →
      ∃ next, Trace process other word next ∧ t.1 = next.1 := by
  induction trace with
  | nil s =>
    intro other same
    exact ⟨other, .nil other, same⟩
  | cons step _ ih =>
    intro other same
    obtain ⟨middle, first, retained⟩ := step_lift_same_left same step
    obtain ⟨last, rest, final⟩ := ih middle retained
    exact ⟨last, .cons first rest, final⟩

theorem same_left_same_feasible (s t : Bool × Bool) (same : s.1 = t.1)
    (word : List Event) : Feasible process s word ↔ Feasible process t word := by
  constructor
  · rintro ⟨last, trace⟩
    obtain ⟨next, lifted, _⟩ := trace_lift_same_left trace t same
    exact ⟨next, lifted⟩
  · rintro ⟨last, trace⟩
    obtain ⟨next, lifted, _⟩ := trace_lift_same_left trace s same.symm
    exact ⟨next, lifted⟩

theorem correlation_preserves_word_possibilities (s : Bool × Bool)
    (word : List Event) :
    Feasible process s word ↔ Feasible process (s.1, s.1) word :=
  same_left_same_feasible s (s.1, s.1) rfl word

/-- This is exactly the profile used in ContinuationConditions, at the
formation prefix. It covers all finite suffixes, not a bounded enumeration. -/
theorem correlation_preserves_profile (s : Bool × Bool) :
    SameFuture (Feasible process s) [.correlate] [] := by
  intro suffix
  change Feasible process s (.correlate :: suffix) ↔ Feasible process s suffix
  constructor
  · rintro ⟨last, trace⟩
    obtain ⟨middle, step, rest⟩ := trace_cons_iff.mp trace
    change middle = (s.1, s.1) at step
    cases step
    exact (correlation_preserves_word_possibilities s suffix).mpr ⟨last, rest⟩
  · intro feasible
    obtain ⟨last, rest⟩ := (correlation_preserves_word_possibilities s suffix).mp feasible
    exact ⟨last, .cons rfl rest⟩

theorem genuine_formation_with_unchanged_profile :
    ¬ diagonal (false, true) ∧
    process.step (false, true) .correlate (false, false) ∧
    diagonal (false, false) ∧
    SameFuture (Feasible process (false, true)) [.correlate] [] := by
  exact ⟨fun bad => Bool.noConfusion bad, rfl, rfl,
    correlation_preserves_profile (false, true)⟩

/-- The right-coordinate specialization of the existing NativeAnswer query.
It is a selected mathematical endpoint question, not an installed observer. -/
def RightOutcome (s : Bool × Bool) (word : List Event) (bit : Bool) : Prop :=
  ∃ t, Trace process s word t ∧ t.2 = bit

theorem later_outcome_contrast :
    RightOutcome (false, false) [.flip] true ∧
      ¬ RightOutcome (false, true) [.flip] true := by
  refine ⟨⟨(true, true), .cons rfl (.nil _), rfl⟩, ?_⟩
  rintro ⟨t, trace, outcome⟩
  have step := trace_singleton_iff.mp trace
  change t = (true, false) at step
  cases step
  exact Bool.noConfusion outcome

/-- Exact feasibility cannot replace the already justified endpoint questions. -/
theorem word_equivalence_not_complete_for_outcomes :
    ¬ (∀ s t : Bool × Bool,
      (∀ word, Feasible process s word ↔ Feasible process t word) →
      ∀ word bit, RightOutcome s word bit ↔ RightOutcome t word bit) := by
  intro complete
  have same := complete (false, true) (false, false)
    (correlation_preserves_word_possibilities (false, true)) [.flip] true
  exact later_outcome_contrast.2 (same.mpr later_outcome_contrast.1)

end Generative.FormationProfileGap

#print axioms Generative.FormationProfileGap.step_lift_same_left
#print axioms Generative.FormationProfileGap.trace_lift_same_left
#print axioms Generative.FormationProfileGap.same_left_same_feasible
#print axioms Generative.FormationProfileGap.correlation_preserves_word_possibilities
#print axioms Generative.FormationProfileGap.correlation_preserves_profile
#print axioms Generative.FormationProfileGap.genuine_formation_with_unchanged_profile
#print axioms Generative.FormationProfileGap.later_outcome_contrast
#print axioms Generative.FormationProfileGap.word_equivalence_not_complete_for_outcomes

#print axioms SystemIndividuation.process
#print axioms SystemIndividuation.diagonal
#print axioms SystemIndividuation.correlate_establishes_diagonal
#print axioms SystemIndividuation.diagonal_preserved_by_trace
