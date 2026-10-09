import Std

/-
Response possibilities within one activity. A response indexes the residual
outcomes admitted by that activity; these types are analytical roles, not an
agent/world ontology. Nonempty outcome sets prevent vacuous guarantees.

This module characterizes preservation of outcome-goal attainability. It does
not identify attainability, control, goal satisfaction or enlargement with moral
goodness. Normative warrant, costs, permissions and physical correspondence are
not certified by these definitions. Outcome predicates must contain whatever
history, cost and affected living the application claims to preserve.
-/
namespace PracticalReach

def Live {A O : Type} (r : A → O → Prop) (a : A) : Prop := ∃ o, r a o

def Guarantees {A O : Type} (r : A → O → Prop) (a : A) (goal : O → Prop) : Prop :=
  Live r a ∧ ∀ o, r a o → goal o

def CanEnsure {A O : Type} (r : A → O → Prop) (goal : O → Prop) : Prop :=
  ∃ a, Guarantees r a goal

/-- Every live old response has a live new response with no additional outcomes.
This is a structural condition, not a claim that less generativity is better. -/
def Refines {A B O : Type} (old : A → O → Prop) (new : B → O → Prop) : Prop :=
  ∀ a, Live old a → ∃ b, Live new b ∧ ∀ o, new b o → old a o

def Possible {A O : Type} (r : A → O → Prop) (o : O) : Prop := ∃ a, r a o

theorem guarantee_mono {A O : Type} {r : A → O → Prop} {a : A}
    {g h : O → Prop} (hg : Guarantees r a g) (incl : ∀ o, g o → h o) :
    Guarantees r a h := ⟨hg.1, fun o ho => incl o (hg.2 o ho)⟩

theorem cannot_ensure_false {A O : Type} (r : A → O → Prop) :
    ¬ CanEnsure r (fun _ => False) := by
  rintro ⟨a, ⟨o, ho⟩, all⟩
  exact all o ho

theorem ensure_true_iff_live_response {A O : Type} (r : A → O → Prop) :
    CanEnsure r (fun _ => True) ↔ ∃ a, Live r a := by
  constructor
  · rintro ⟨a, live, _⟩
    exact ⟨a, live⟩
  · rintro ⟨a, live⟩
    exact ⟨a, live, fun _ _ => True.intro⟩

theorem refinement_preserves_goals {A B O : Type}
    {r : A → O → Prop} {s : B → O → Prop} (h : Refines r s)
    {g : O → Prop} (hg : CanEnsure r g) : CanEnsure s g := by
  obtain ⟨a, ha, ag⟩ := hg
  obtain ⟨b, hb, sub⟩ := h a ha
  exact ⟨b, hb, fun o ho => ag o (sub o ho)⟩

/-- Exact all-predicate characterization; the converse tests each old response's
own outcome set. Restricting the goal language can weaken the converse. -/
theorem refinement_iff_all_goal_preservation {A B O : Type}
    (r : A → O → Prop) (s : B → O → Prop) :
    Refines r s ↔ ∀ g, CanEnsure r g → CanEnsure s g := by
  constructor
  · intro h g hg
    exact refinement_preserves_goals h hg
  · intro h a ha
    obtain ⟨b, hb, sub⟩ := h (r a) ⟨a, ha, fun _ ho => ho⟩
    exact ⟨b, hb, sub⟩

theorem refinement_refl {A O : Type} (r : A → O → Prop) : Refines r r :=
  fun a ha => ⟨a, ha, fun _ ho => ho⟩

theorem refinement_trans {A B C O : Type}
    {r : A → O → Prop} {s : B → O → Prop} {t : C → O → Prop}
    (rs : Refines r s) (st : Refines s t) : Refines r t := by
  intro a ha
  obtain ⟨b, hb, ba⟩ := rs a ha
  obtain ⟨c, hc, cb⟩ := st b hb
  exact ⟨c, hc, fun o ho => ba o (cb o ho)⟩

theorem failed_refinement_has_lost_goal {A B O : Type}
    {r : A → O → Prop} {s : B → O → Prop} (h : ¬ Refines r s) :
    ∃ g, CanEnsure r g ∧ ¬ CanEnsure s g := by
  classical
  apply Classical.byContradiction
  intro hn
  apply h
  apply (refinement_iff_all_goal_preservation r s).mpr
  intro g hg
  exact Classical.byContradiction (fun hs => hn ⟨g, hg, hs⟩)

/-- The response type may change at every finite revision. There is no claim
about a limit protocol, or about a chooser actually using the retained response. -/
theorem finite_revisions_preserve {O : Type} {A : Nat → Type}
    (r : (n : Nat) → A n → O → Prop)
    (step : ∀ n, Refines (r n) (r (n + 1))) :
    ∀ n, Refines (r 0) (r n) := by
  intro n
  induction n with
  | zero => exact refinement_refl _
  | succ n ih => exact refinement_trans ih (step n)

def Project {A O P : Type} (f : O → P) (r : A → O → Prop) : A → P → Prop :=
  fun a p => ∃ o, r a o ∧ f o = p

theorem projected_goal_iff {A O P : Type} (f : O → P)
    (r : A → O → Prop) (g : P → Prop) :
    CanEnsure (Project f r) g ↔ CanEnsure r (fun o => g (f o)) := by
  constructor
  · rintro ⟨a, ⟨p, o, ho, _⟩, all⟩
    exact ⟨a, ⟨o, ho⟩, fun x hx => all (f x) ⟨x, hx, rfl⟩⟩
  · rintro ⟨a, ⟨o, ho⟩, all⟩
    refine ⟨a, ⟨f o, o, ho, rfl⟩, ?_⟩
    rintro p ⟨x, hx, eq⟩
    rw [← eq]
    exact all x hx

theorem no_strict_improvement_for_every_goal {A B O : Type}
    (r : A → O → Prop) (s : B → O → Prop) :
    ¬ (∀ g, CanEnsure s g ∧ ¬ CanEnsure r g) := by
  intro h
  exact cannot_ensure_false s (h (fun _ => False)).1

/-- Even among goals already achievable somewhere, the always-true goal rules
out an everywhere-strict improvement when the old activity has a live response. -/
theorem common_goal_prevents_everywhere_strict {A B O : Type}
    {r : A → O → Prop} {s : B → O → Prop} (live : ∃ a, Live r a)
    (h : Refines r s) :
    ∃ g, CanEnsure r g ∧ CanEnsure s g := by
  have hg := (ensure_true_iff_live_response r).mpr live
  exact ⟨fun _ => True, hg, refinement_preserves_goals h hg⟩

/- Explicit witnesses: these are local possibilities, not ethical verdicts. -/
def fixed : Unit → Bool → Prop := fun _ o => o = false
def uncontrolled : Unit → Bool → Prop := fun _ _ => True
def selectable : Bool → Bool → Prop := fun a o => o = a
def absent : Unit → Bool → Prop := fun _ _ => False

theorem fixed_ensures_false : CanEnsure fixed (fun o => o = false) :=
  ⟨(), ⟨false, rfl⟩, fun _ h => h⟩

theorem uncontrolled_cannot_ensure_false :
    ¬ CanEnsure uncontrolled (fun o => o = false) := by
  rintro ⟨a, _, all⟩
  have h := all true True.intro
  cases h

theorem possible_enlargement_without_control :
    (∀ o, Possible fixed o → Possible uncontrolled o) ∧
    (Possible uncontrolled true ∧ ¬ Possible fixed true) ∧
    ¬ Refines fixed uncontrolled := by
  refine ⟨fun _ _ => ⟨(), True.intro⟩, ⟨⟨(), True.intro⟩, ?_⟩, ?_⟩
  · rintro ⟨a, h⟩
    cases h
  · intro h
    exact uncontrolled_cannot_ensure_false (refinement_preserves_goals h fixed_ensures_false)

theorem selectable_retains_fixed : Refines fixed selectable := by
  intro _ _
  exact ⟨false, ⟨false, rfl⟩, fun _ h => h⟩

theorem guaranteed_control_can_remove_possibility :
    Refines uncontrolled fixed ∧ Possible uncontrolled true ∧ ¬ Possible fixed true := by
  refine ⟨?_, ⟨(), True.intro⟩, ?_⟩
  · intro _ _
    exact ⟨(), ⟨false, rfl⟩, fun _ _ => True.intro⟩
  · rintro ⟨a, h⟩
    cases h

theorem selectable_ensures_each (b : Bool) : CanEnsure selectable (fun o => o = b) :=
  ⟨b, ⟨b, rfl⟩, fun _ h => h⟩

theorem fixed_cannot_ensure_true : ¬ CanEnsure fixed (fun o => o = true) := by
  rintro ⟨a, _, all⟩
  have h := all false rfl
  cases h

theorem retained_control_and_strict_new_goal :
    Refines fixed selectable ∧
    CanEnsure selectable (fun o => o = true) ∧ ¬ CanEnsure fixed (fun o => o = true) :=
  ⟨selectable_retains_fixed, selectable_ensures_each true, fixed_cannot_ensure_true⟩

def ClosedToTrue {A : Type} (r : A → Bool → Prop) : Prop := ¬ Possible r true

theorem outcome_goal_preservation_can_defeat_closure_goal :
    Refines fixed selectable ∧ ClosedToTrue fixed ∧ ¬ ClosedToTrue selectable := by
  refine ⟨selectable_retains_fixed, ?_, ?_⟩
  · rintro ⟨a, h⟩
    cases h
  · intro h
    exact h ⟨true, rfl⟩

theorem separate_guarantees_not_joint :
    CanEnsure selectable (fun o => o = false) ∧
    CanEnsure selectable (fun o => o = true) ∧
    ¬ CanEnsure selectable (fun o => o = false ∧ o = true) := by
  refine ⟨selectable_ensures_each false, selectable_ensures_each true, ?_⟩
  rintro ⟨a, ⟨o, ho⟩, all⟩
  obtain ⟨hf, ht⟩ := all o ho
  cases hf
  cases ht

theorem empty_response_does_not_guarantee :
    (∀ o, absent () o → o = false) ∧ ¬ CanEnsure absent (fun o => o = false) := by
  refine ⟨fun _ h => False.elim h, ?_⟩
  rintro ⟨a, ⟨o, ho⟩, _⟩
  exact ho

theorem projection_can_hide_loss :
    CanEnsure (Project (fun (_ : Bool) => false) uncontrolled) (fun o => o = false) ∧
    ¬ CanEnsure uncontrolled (fun o => o = false) := by
  refine ⟨?_, uncontrolled_cannot_ensure_false⟩
  apply (projected_goal_iff _ _ _).mpr
  exact ⟨(), ⟨false, True.intro⟩, fun _ _ => rfl⟩

end PracticalReach
