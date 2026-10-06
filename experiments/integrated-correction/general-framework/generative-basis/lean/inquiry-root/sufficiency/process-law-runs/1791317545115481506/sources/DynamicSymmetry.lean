import DynamicUnderdetermination

/-!
# Total deterministic reversible dynamics are not fixed by Boolean renaming symmetry

The existing static and toggle laws use the same Bool states and Unit actions.
Both have one successor and one predecessor at every state, are symmetric under
step reversal, and preserve their step relations under every bijective renaming
of Bool. They still disagree about whether a state can remain unchanged.

This is a concrete non-uniqueness witness for the properties defined below.
It does not establish impossibility of deriving dynamics from richer grounds,
identify a physical law, or remove the definitions and inference rules used here.
-/

namespace Generative.Deeper

universe u v

/-- Every state and action admits a successor. -/
def StepTotal {State : Type u} {Action : Type v}
    (P : Process State Action) : Prop :=
  ∀ s a, ∃ t, P.step s a t

/-- A fixed state and action permit at most one successor. -/
def StepDeterministic {State : Type u} {Action : Type v}
    (P : Process State Action) : Prop :=
  ∀ s a t r, P.step s a t → P.step s a r → t = r

/-- Each step can be reversed using the same action label. -/
def StepSymmetric {State : Type u} {Action : Type v}
    (P : Process State Action) : Prop :=
  ∀ s a t, P.step s a t → P.step t a s

/-- Every state and action have exactly one predecessor. -/
def UniquePredecessor {State : Type u} {Action : Type v}
    (P : Process State Action) : Prop :=
  ∀ t a, ∃ s, P.step s a t ∧ ∀ r, P.step r a t → r = s

/-- Explicit bijectivity, using the dependency package's available primitives. -/
def BoolBijection (f : Bool → Bool) : Prop :=
  Function.Injective f ∧ ∀ t, ∃ s, f s = t

/-- Invariance is of the entire step relation under simultaneous state renaming. -/
def BoolRenamingInvariant (P : Process Bool Unit) : Prop :=
  ∀ f : Bool → Bool, BoolBijection f →
    ∀ s a t, P.step s a t ↔ P.step (f s) a (f t)

theorem unique_predecessor_of_total_deterministic_symmetric
    {State : Type u} {Action : Type v} (P : Process State Action)
    (htotal : StepTotal P) (hdet : StepDeterministic P)
    (hsym : StepSymmetric P) : UniquePredecessor P := by
  intro t a
  obtain ⟨s, hs⟩ := htotal t a
  refine ⟨s, hsym t a s hs, ?_⟩
  intro r hr
  exact hdet t a r s (hsym r a t hr) hs

theorem static_total : StepTotal static := by
  intro s a
  exact ⟨s, rfl⟩

theorem toggle_total : StepTotal toggle := by
  intro s a
  exact ⟨!s, rfl⟩

theorem static_deterministic : StepDeterministic static := by
  intro s a t r ht hr
  exact ht.symm.trans hr

theorem toggle_deterministic : StepDeterministic toggle := by
  intro s a t r ht hr
  exact ht.trans hr.symm

theorem static_symmetric : StepSymmetric static := by
  intro s a t h
  exact h.symm

theorem toggle_symmetric : StepSymmetric toggle := by
  intro s a t h
  cases s <;> cases t <;> cases h <;> rfl

theorem static_unique_predecessor : UniquePredecessor static :=
  unique_predecessor_of_total_deterministic_symmetric
    static static_total static_deterministic static_symmetric

theorem toggle_unique_predecessor : UniquePredecessor toggle :=
  unique_predecessor_of_total_deterministic_symmetric
    toggle toggle_total toggle_deterministic toggle_symmetric

/-- The quantified renaming class contains identity. -/
theorem identity_bool_bijection : BoolBijection (fun s => s) := by
  constructor
  · intro s t h
    exact h
  · intro t
    exact ⟨t, rfl⟩

/-- The quantified renaming class also contains the nontrivial swap. -/
theorem negation_bool_bijection : BoolBijection Bool.not := by
  constructor
  · intro s t h
    cases s <;> cases t <;> cases h <;> rfl
  · intro t
    refine ⟨!t, ?_⟩
    cases t <;> rfl

/-- Every injective Boolean map is pointwise identity or pointwise negation. -/
theorem injective_bool_map_forms (f : Bool → Bool) (hf : Function.Injective f) :
    (∀ s, f s = s) ∨ (∀ s, f s = !s) := by
  cases hfalse : f false <;> cases htrue : f true
  · have hbad : false = true := hf (hfalse.trans htrue.symm)
    cases hbad
  · left
    intro s
    cases s
    · exact hfalse
    · exact htrue
  · right
    intro s
    cases s
    · exact hfalse
    · exact htrue
  · have hbad : false = true := hf (hfalse.trans htrue.symm)
    cases hbad

theorem injective_bool_map_commutes_not
    (f : Bool → Bool) (hf : Function.Injective f) (s : Bool) :
    f (!s) = !(f s) := by
  obtain hid | hnot := injective_bool_map_forms f hf
  · exact (hid (!s)).trans (congrArg Bool.not (hid s)).symm
  · exact (hnot (!s)).trans (congrArg Bool.not (hnot s)).symm

theorem static_renaming_invariant : BoolRenamingInvariant static := by
  intro f hf s a t
  constructor
  · intro h
    exact congrArg f h
  · intro h
    exact hf.1 h

theorem toggle_renaming_invariant : BoolRenamingInvariant toggle := by
  intro f hf s a t
  constructor
  · intro h
    exact (congrArg f h).trans (injective_bool_map_commutes_not f hf.1 s)
  · intro h
    exact hf.1 (h.trans (injective_bool_map_commutes_not f hf.1 s).symm)

/-- The complete finite constraint package being tested, with no chosen dynamics. -/
def SymmetryCandidate (P : Process Bool Unit) : Prop :=
  StepTotal P ∧ StepDeterministic P ∧ StepSymmetric P ∧
    UniquePredecessor P ∧ BoolRenamingInvariant P

theorem static_symmetry_candidate : SymmetryCandidate static :=
  ⟨static_total, static_deterministic, static_symmetric,
    static_unique_predecessor, static_renaming_invariant⟩

theorem toggle_symmetry_candidate : SymmetryCandidate toggle :=
  ⟨toggle_total, toggle_deterministic, toggle_symmetric,
    toggle_unique_predecessor, toggle_renaming_invariant⟩

theorem static_ne_toggle : static ≠ toggle := by
  intro heq
  have h : static.step false () false := static_event false
  rw [heq] at h
  exact toggle_always_changes h rfl

/-- The laws cannot be identified even by an arbitrary map of their state labels. -/
theorem no_state_map_identifies_static_toggle (f : Bool → Bool) :
    ¬ (∀ s a t, static.step s a t ↔ toggle.step (f s) a (f t)) := by
  intro h
  have hloop := (h false () false).mp (static_event false)
  exact toggle_always_changes hloop rfl

/-- Adding these properties to the common carrier does not select a unique law. -/
theorem symmetric_dynamics_remain_underdetermined :
    ∃ P Q : Process Bool Unit,
      SymmetryCandidate P ∧ SymmetryCandidate Q ∧ P ≠ Q ∧
        P.step false () false ∧ ¬ Q.step false () false := by
  refine ⟨static, toggle, static_symmetry_candidate, toggle_symmetry_candidate,
    static_ne_toggle, static_event false, ?_⟩
  intro h
  exact toggle_always_changes h rfl

end Generative.Deeper

#print axioms Generative.Deeper.unique_predecessor_of_total_deterministic_symmetric
#print axioms Generative.Deeper.static_total
#print axioms Generative.Deeper.toggle_total
#print axioms Generative.Deeper.static_deterministic
#print axioms Generative.Deeper.toggle_deterministic
#print axioms Generative.Deeper.static_symmetric
#print axioms Generative.Deeper.toggle_symmetric
#print axioms Generative.Deeper.static_unique_predecessor
#print axioms Generative.Deeper.toggle_unique_predecessor
#print axioms Generative.Deeper.identity_bool_bijection
#print axioms Generative.Deeper.negation_bool_bijection
#print axioms Generative.Deeper.injective_bool_map_forms
#print axioms Generative.Deeper.injective_bool_map_commutes_not
#print axioms Generative.Deeper.static_renaming_invariant
#print axioms Generative.Deeper.toggle_renaming_invariant
#print axioms Generative.Deeper.static_symmetry_candidate
#print axioms Generative.Deeper.toggle_symmetry_candidate
#print axioms Generative.Deeper.static_ne_toggle
#print axioms Generative.Deeper.no_state_map_identifies_static_toggle
#print axioms Generative.Deeper.symmetric_dynamics_remain_underdetermined
