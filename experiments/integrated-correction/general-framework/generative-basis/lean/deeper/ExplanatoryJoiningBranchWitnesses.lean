import ExplanatoryJoiningBranches

/-! One joining law contains shared and prematurely split continuations.
Constructors name positions in this finite example; their universal genesis
is not assumed or proved. No second observer or unrelated terminal predicate. -/
namespace Generative.ExplanatoryJoiningBranchWitnesses
open ExplanatoryJoiningBranches ExplanatoryBranching
open ExplanatoryUniqueness ExplanatoryUniversality ExplanatoryLocalUnits

inductive Piece where
  | shared | split | both | leftOnly | rightOnly | finish | enter | left | right
  deriving DecidableEq

def results : Piece → Piece → List Piece
  | .shared, .enter => [.both]
  | .split, .enter => [.leftOnly, .rightOnly]
  | .both, .left => [.finish]
  | .both, .right => [.finish]
  | .leftOnly, .left => [.finish]
  | .rightOnly, .right => [.finish]
  | _, _ => []

def joining (x y z : Piece) : Prop := z ∈ results x y

theorem finite_outcomes : FiniteOutcomes joining := fun x y => ⟨results x y, fun _ => Iff.rfl⟩

theorem genuinely_multivalued : ¬ Functional joining := by
  intro h
  have bad := h .split .enter .leftOnly .rightOnly
    (by simp [joining, results]) (by simp [joining, results])
  cases bad

def retained : Question Piece :=
  .after (.right, .enter)
    (.conj (.after (.right, .left) .top) (.after (.right, .right) .top))

def path (last : Piece) : Question Piece :=
  .after (.right, .enter) (.after (.right, last) .top)

theorem shared_retains : target joining .shared retained := by
  simp [target, retained, model, Holds, joining, results]

theorem split_loses_shared_continuation : ¬ target joining .split retained := by
  simp [target, retained, model, Holds, joining, results]

theorem both_linear_alternatives_remain :
    target joining .shared (path .left) ∧ target joining .split (path .left) ∧
    target joining .shared (path .right) ∧ target joining .split (path .right) := by
  simp [target, path, model, Holds, joining, results]

theorem roots_branch_distinguished : ¬ BranchSame joining .shared .split :=
  fun h => split_loses_shared_continuation ((h retained).mp shared_retains)

theorem outcomes_branch_distinguished : ¬ BranchSame joining .leftOnly .rightOnly := by
  intro h
  have yes : target joining .leftOnly (.after (.right, .left) .top) := by
    simp [target, model, Holds, joining, results]
  have no : ¬ target joining .rightOnly (.after (.right, .left) .top) := by
    simp [target, model, Holds, joining, results]
  exact no ((h (.after (.right, .left) .top)).mp yes)

theorem every_exact_account_distinguishes_outcomes
    {C : Type} {p : Presentation Piece (Question Piece) C} (hp : Exact (target joining) p) :
    p.encode .leftOnly ≠ p.encode .rightOnly :=
  fun h => outcomes_branch_distinguished (equal_codes_same_answers hp h)

/-- Minimal representation retains two distinct outcomes. The common structure
is a relation, and no choice of one preferred result is hidden in its definition. -/
theorem canonical_operation_still_multivalued :
    ¬ Functional (Lift (canonical joining) joining) := by
  intro h
  have hl := lift_contains (canonical joining) joining
    (a := .split) (b := .enter) (c := .leftOnly) (by simp [joining, results])
  have hr := lift_contains (canonical joining) joining
    (a := .split) (b := .enter) (c := .rightOnly) (by simp [joining, results])
  exact every_exact_account_distinguishes_outcomes (canonical_exact joining) (h _ _ _ _ hl hr)

/-- Nonfunctional joining satisfies the checked representative-wise lifting
conclusion. This instantiates the general bridge, not an additional principle. -/
theorem canonical_outcomes_lift (x y : Piece) (c : Question Piece → Prop) :
    Lift (canonical joining) joining ((canonical joining).encode x) ((canonical joining).encode y) c ↔
      ∃ z, joining x y z ∧ (canonical joining).encode z = c :=
  operation_lifts finite_outcomes (canonical_exact joining) (canonical_reduced joining) x y c

end Generative.ExplanatoryJoiningBranchWitnesses

#print axioms Generative.ExplanatoryJoiningBranchWitnesses.finite_outcomes
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.genuinely_multivalued
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.shared_retains
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.split_loses_shared_continuation
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.both_linear_alternatives_remain
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.roots_branch_distinguished
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.outcomes_branch_distinguished
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.every_exact_account_distinguishes_outcomes
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.canonical_operation_still_multivalued
#print axioms Generative.ExplanatoryJoiningBranchWitnesses.canonical_outcomes_lift
