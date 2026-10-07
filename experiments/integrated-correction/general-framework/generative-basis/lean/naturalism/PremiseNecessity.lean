import ProtectedScopeLimits

/-!
# Necessity of the remaining inputs

Ren's rule (6 October 2026): no assumptions, no axioms. Every input a result relies on
must be derived in Lean from the process, or proved necessary for the stated
conclusion. This module proves necessity for the two normative inputs of the
ethical-naturalism study that are not derived.

* **An orientation input is necessary.** Call a relation *credentialed* when it has every
  natural credential this package proves: preorder laws, supervenience on visited states,
  composition along histories, and invariance under exact re-representation. Two
  credentialed relations give opposite verdicts on an actual transition of `dip`
  (`credentials_do_not_determine_verdict`). So no rule that consults only these
  credentials can return the verdict "this transition is a loss"; a further input is
  needed to fix the orientation.
* **A scope input is necessary.** A scope of activities is *unprivileged* when every
  renaming of actions maps it onto itself. The empty scope and the whole scope are both
  unprivileged (`empty_and_whole_unprivileged`), and under the empty scope even the
  converse orientation is non-undermining, while under the whole scope it is not
  (`unprivileged_does_not_fix_scope`). So "no activity privileged" does not determine the
  protected scope; choosing the whole scope is a further input.

* **A vocabulary input is necessary.** `dip` and `dipCoarse` have the same states and the
  same possible state changes; they differ only in whether `go` and `use` count as distinct
  activities. The transition from 2 to 1 is a loss in the first and not in the second
  (`vocabulary_changes_verdict`). So the state dynamics do not fix which activities there
  are; the individuation of activities is a further input.

None of these inputs is assumed by any theorem: each theorem that uses one states it as a
hypothesis or a definition. These results show the inputs cannot be dropped.
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v

variable {State : Type u} {Action : Type v}

/-- Every natural credential proved in this package. -/
def Credentialed (P : Process State Action) (R : State → State → Prop) : Prop :=
  PreorderLaws R ∧
  Covaries (fun h : History P => Along R h.2.2) History.states ∧
  (∀ {s m t : State} (r : Run P s m) (r' : Run P m t),
    (Along R (r.append r') ↔ Along R r ∧ Along R r'))

theorem continuation_credentialed (P : Process State Action) :
    Credentialed P (ContinuationLe P) :=
  ⟨continuation_preorder P, (credentials_hold_for_every_relation P _).1,
    fun r r' => along_append _ r r'⟩

theorem converse_credentialed (P : Process State Action) :
    Credentialed P (converse (ContinuationLe P)) :=
  ⟨converse_preorder (continuation_preorder P), (credentials_hold_for_every_relation P _).1,
    fun r r' => along_append _ r r'⟩

/-- The credentials do not determine the verdict on the actual transition 2 → 1 of `dip`.
Invariance under exact re-representation holds for both (`continuation_projection_iff`,
`converse_projection_iff`). -/
theorem credentials_do_not_determine_verdict :
    ¬ ∀ R S : Nat → Nat → Prop, Credentialed dip R → Credentialed dip S → (R 2 1 ↔ S 2 1) := by
  intro h
  have := (h (ContinuationLe dip) (converse (ContinuationLe dip))
    (continuation_credentialed dip) (converse_credentialed dip)).mpr dip_two_dominates_one
  exact witness_refutes_preservation ⟨dip_use_at_two, dip_no_use_at_one⟩ this

/-- Renaming actions with an inverse pair maps the scope onto itself. -/
def Unprivileged (W : List Action → Prop) : Prop :=
  ∀ (f g : Action → Action), (∀ a, g (f a) = a) → (∀ a, f (g a) = a) →
    ∀ word, (W word ↔ W (word.map f))

def emptyScope : List Action → Prop := fun _ => False

theorem empty_and_whole_unprivileged :
    Unprivileged (emptyScope (Action := Action)) ∧ Unprivileged (wholeScope (Action := Action)) :=
  ⟨fun _ _ _ _ _ => Iff.rfl, fun _ _ _ _ _ => Iff.intro (fun _ => True.intro) (fun _ => True.intro)⟩

theorem empty_scope_admits_everything (P : Process State Action) (R : State → State → Prop) :
    NonUndermining P emptyScope R :=
  fun _ _ _ _ hw _ => absurd hw (fun h => h)

/-- Both scopes are unprivileged, yet they disagree about the converse orientation. -/
theorem unprivileged_does_not_fix_scope :
    Unprivileged (emptyScope (Action := DipAct)) ∧ Unprivileged (wholeScope (Action := DipAct)) ∧
      NonUndermining dip emptyScope (converse (ContinuationLe dip)) ∧
      ¬ NonUndermining dip wholeScope (converse (ContinuationLe dip)) :=
  ⟨empty_and_whole_unprivileged.1, empty_and_whole_unprivileged.2,
    empty_scope_admits_everything dip _, converse_undermines_in_dip⟩

/-! ## The action vocabulary is a necessary input -/

/-- The same state dynamics as `dip`, with `go` and `use` no longer told apart. -/
def dipCoarse : Process Nat Unit where
  step s _ t := dip.step s .go t ∨ dip.step s .use t

theorem dipCoarse_from_two : (word : List Unit) → Feasible dipCoarse 2 word
  | [] => ⟨2, .nil 2⟩
  | _ :: rest => by
    obtain ⟨t, ht⟩ := dipCoarse_from_two rest
    exact ⟨t, .cons (Or.inr (show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩)) ht⟩

theorem dipCoarse_from_one : (word : List Unit) → Feasible dipCoarse 1 word
  | [] => ⟨1, .nil 1⟩
  | _ :: rest => by
    obtain ⟨t, ht⟩ := dipCoarse_from_two rest
    exact ⟨t, .cons (m := 2) (Or.inl (show (2 : Nat) ≤ 2 ∧ (1 : Nat) ≤ 2 + 1 by decide)) ht⟩

/-- Same states and the same possible state changes: the transition 2 → 1 is a loss when
`go` and `use` are distinct activities, and no loss when they are not. -/
theorem vocabulary_changes_verdict :
    (∀ s t, (∃ a, dip.step s a t) ↔ (∃ a, dipCoarse.step s a t)) ∧
      ¬ ContinuationLe dip 2 1 ∧ ContinuationLe dipCoarse 2 1 := by
  refine ⟨?_, witness_refutes_preservation ⟨dip_use_at_two, dip_no_use_at_one⟩,
    fun word _ => dipCoarse_from_one word⟩
  intro s t
  constructor
  · rintro ⟨a, h⟩
    cases a with
    | go => exact ⟨(), Or.inl h⟩
    | use => exact ⟨(), Or.inr h⟩
  · rintro ⟨_, h | h⟩
    · exact ⟨.go, h⟩
    · exact ⟨.use, h⟩

end Generative.Naturalism

#print axioms Generative.Naturalism.continuation_credentialed
#print axioms Generative.Naturalism.converse_credentialed
#print axioms Generative.Naturalism.credentials_do_not_determine_verdict
#print axioms Generative.Naturalism.empty_and_whole_unprivileged
#print axioms Generative.Naturalism.empty_scope_admits_everything
#print axioms Generative.Naturalism.unprivileged_does_not_fix_scope
#print axioms Generative.Naturalism.dipCoarse_from_two
#print axioms Generative.Naturalism.dipCoarse_from_one
#print axioms Generative.Naturalism.vocabulary_changes_verdict
