import ExplanatoryBranching

/-! Independent finite continuation/capacity questions witness why word lists
lose branch correlations. Forward questions also have a checked history limit.
No claim that conjunction executes two destructive tests on the same specimen. -/
namespace Generative.ExplanatoryBranchingWitnesses
open ExplanatoryBranching
universe u v

inductive Event where | enter | left | right deriving DecidableEq
inductive Node where | root | both | leftOnly | rightOnly | finish deriving DecidableEq

def nexts (split : Bool) : Node → Event → List Node
  | .root, .enter => if split then [.leftOnly, .rightOnly] else [.both]
  | .both, .left => [.finish]
  | .both, .right => [.finish]
  | .leftOnly, .left => [.finish]
  | .rightOnly, .right => [.finish]
  | _, _ => []

def forkModel (split : Bool) : Model Node Event Empty where
  process.step s a t := t ∈ nexts split s a
  condition _ o := nomatch o

def Can {S : Type u} {A : Type v} (P : Process S A) (s : S) (word : List A) : Prop :=
  ∃ t, Trace P s word t

theorem can_nil {S : Type u} {A : Type v} (P : Process S A) (s : S) : Can P s [] :=
  ⟨s, .nil s⟩

theorem can_cons {S : Type u} {A : Type v} (P : Process S A) (s : S) (a : A) (word : List A) :
    Can P s (a :: word) ↔ ∃ t, P.step s a t ∧ Can P t word := by
  constructor
  · rintro ⟨end', trace⟩
    obtain ⟨t, hs, ht⟩ := trace_cons_iff.mp trace
    exact ⟨t, hs, end', ht⟩
  · rintro ⟨t, hs, end', ht⟩
    exact ⟨end', .cons hs ht⟩

theorem fork_finitely_branching (split : Bool) : ImageFinite (forkModel split) :=
  fun s a => ⟨nexts split s a, fun _ => Iff.rfl⟩

theorem finish_words (split : Bool) (word : List Event) :
    Can (forkModel split).process .finish word ↔ word = [] := by
  cases word with
  | nil => exact ⟨fun _ => rfl, fun _ => can_nil _ _⟩
  | cons a word => simp [can_cons, forkModel, nexts]

theorem both_words (split : Bool) (word : List Event) :
    Can (forkModel split).process .both word ↔
      word = [] ∨ word = [.left] ∨ word = [.right] := by
  cases word with
  | nil => exact ⟨fun _ => Or.inl rfl, fun _ => can_nil _ _⟩
  | cons a word =>
    rw [can_cons]
    cases a <;> simp [forkModel, nexts, ← finish_words split word]

theorem left_words (split : Bool) (word : List Event) :
    Can (forkModel split).process .leftOnly word ↔ word = [] ∨ word = [.left] := by
  cases word with
  | nil => exact ⟨fun _ => Or.inl rfl, fun _ => can_nil _ _⟩
  | cons a word =>
    rw [can_cons]
    cases a <;> simp [forkModel, nexts, ← finish_words split word]

theorem right_words (split : Bool) (word : List Event) :
    Can (forkModel split).process .rightOnly word ↔ word = [] ∨ word = [.right] := by
  cases word with
  | nil => exact ⟨fun _ => Or.inl rfl, fun _ => can_nil _ _⟩
  | cons a word =>
    rw [can_cons]
    cases a <;> simp [forkModel, nexts, ← finish_words split word]

theorem root_words (split : Bool) (word : List Event) :
    Can (forkModel split).process .root word ↔
      word = [] ∨ word = [.enter] ∨ word = [.enter, .left] ∨ word = [.enter, .right] := by
  cases word with
  | nil => exact ⟨fun _ => Or.inl rfl, fun _ => can_nil _ _⟩
  | cons a word =>
    rw [can_cons]
    change (∃ t, t ∈ nexts split .root a ∧ Can (forkModel split).process t word) ↔ _
    cases split <;> cases a <;>
      simp [nexts, both_words, left_words, right_words, or_assoc, or_left_comm]

theorem same_all_words (word : List Event) :
    Can (forkModel false).process .root word ↔ Can (forkModel true).process .root word :=
  (root_words false word).trans (root_words true word).symm

/-- Both alternatives remain possible from the SAME successor of enter. This
is not the assertion that both event executions can occur simultaneously. -/
def retainedAlternatives : Test Event Empty :=
  .after .enter (.conj (.after .left .top) (.after .right .top))

theorem shared_condition_retains_alternatives : Holds (forkModel false) .root retainedAlternatives :=
  ⟨.both, by simp [forkModel, nexts],
    ⟨.finish, by simp [forkModel, nexts], True.intro⟩,
    ⟨.finish, by simp [forkModel, nexts], True.intro⟩⟩

theorem early_split_loses_shared_alternatives : ¬ Holds (forkModel true) .root retainedAlternatives := by
  rintro ⟨s, hs, ⟨l, hl, _⟩, ⟨r, hr, _⟩⟩
  have cases' : s = .leftOnly ∨ s = .rightOnly := by simpa [forkModel, nexts] using hs
  cases cases' with
  | inl eq => subst s; simp [forkModel, nexts] at hr
  | inr eq => subst s; simp [forkModel, nexts] at hl

theorem trace_equivalence_misses_branching :
    (∀ word, Can (forkModel false).process .root word ↔ Can (forkModel true).process .root word) ∧
    ¬ Same (forkModel false) (forkModel true) .root .root :=
  ⟨same_all_words, fun h => early_split_loses_shared_alternatives
    ((h retainedAlternatives).mp shared_condition_retains_alternatives)⟩

/-- The observed shared-condition question rules out ANY claimed bisimulation,
not only an identity or a selected naming of the nodes. -/
theorem no_rooted_bisimulation :
    ¬ ∃ R, Bisimulation (forkModel false) (forkModel true) R ∧ R .root .root := by
  rintro ⟨R, bis, related⟩
  exact trace_equivalence_misses_branching.2 (bisimulation_implies_same bis related)

/-- Mathematical forward tests do not automatically distinguish native labels
or reconstruct a particular past. Reuse the existing relational result. -/
def unmarked {S : Type u} {A : Type v} (P : Process S A) : Model S A Empty where
  process := P
  condition _ o := nomatch o

theorem unmarked_bisimulation {S : Type u} {T : Type u} {A : Type v}
    {P : Process S A} {Q : Process T A} {R : S → T → Prop}
    (h : Deeper.Bisimulation P Q R) : Bisimulation (unmarked P) (unmarked Q) R :=
  ⟨h, fun _ _ _ o => nomatch o⟩

theorem static_toggle_same_all_tests (s t : Bool) :
    Same (unmarked Deeper.static) (unmarked Deeper.toggle) s t :=
  bisimulation_implies_same (unmarked_bisimulation Deeper.static_toggle_one_dynamics) True.intro

/-- One-event and two-event actual histories from the same root have the same
endpoint in this process; no endpoint-only answer restores their event count. -/
def mergeProcess : Process Bool Unit where
  step _ _ t := t = true

theorem two_actual_histories_same_endpoint :
    Trace mergeProcess false [()] true ∧ Trace mergeProcess false [(), ()] true :=
  ⟨.cons rfl (.nil true), .cons rfl (.cons rfl (.nil true))⟩

theorem all_future_tests_agree_after_both_histories :
    ∀ f : Test Unit Empty, Holds (unmarked mergeProcess) true f ↔ Holds (unmarked mergeProcess) true f :=
  fun _ => Iff.rfl

theorem actual_length_not_endpoint_readable :
    ¬ ∃ read : Bool → Nat, ∀ word end', Trace mergeProcess false word end' → read end' = word.length := by
  rintro ⟨read, h⟩
  have one := h [()] true two_actual_histories_same_endpoint.1
  have two := h [(), ()] true two_actual_histories_same_endpoint.2
  have impossible : (1 : Nat) = 2 := one.symm.trans two
  cases impossible

end Generative.ExplanatoryBranchingWitnesses

#print axioms Generative.ExplanatoryBranchingWitnesses.can_nil
#print axioms Generative.ExplanatoryBranchingWitnesses.can_cons
#print axioms Generative.ExplanatoryBranchingWitnesses.fork_finitely_branching
#print axioms Generative.ExplanatoryBranchingWitnesses.finish_words
#print axioms Generative.ExplanatoryBranchingWitnesses.both_words
#print axioms Generative.ExplanatoryBranchingWitnesses.left_words
#print axioms Generative.ExplanatoryBranchingWitnesses.right_words
#print axioms Generative.ExplanatoryBranchingWitnesses.root_words
#print axioms Generative.ExplanatoryBranchingWitnesses.same_all_words
#print axioms Generative.ExplanatoryBranchingWitnesses.shared_condition_retains_alternatives
#print axioms Generative.ExplanatoryBranchingWitnesses.early_split_loses_shared_alternatives
#print axioms Generative.ExplanatoryBranchingWitnesses.trace_equivalence_misses_branching
#print axioms Generative.ExplanatoryBranchingWitnesses.no_rooted_bisimulation
#print axioms Generative.ExplanatoryBranchingWitnesses.unmarked_bisimulation
#print axioms Generative.ExplanatoryBranchingWitnesses.static_toggle_same_all_tests
#print axioms Generative.ExplanatoryBranchingWitnesses.two_actual_histories_same_endpoint
#print axioms Generative.ExplanatoryBranchingWitnesses.all_future_tests_agree_after_both_histories
#print axioms Generative.ExplanatoryBranchingWitnesses.actual_length_not_endpoint_readable
