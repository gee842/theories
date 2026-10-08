import GenerativeCore

/-!
A necessary restriction on a proposed explanation of newly formed asymmetry.
Transformations act on configurations of one process; they are not primitive
independent components. Action labels are fixed by the transformation here.
The local branching example separates a symmetric possibility relation from
the symmetry of an individual result. No universal physical law is asserted.
-/

namespace FormationSymmetry

open Generative

universe u v
variable {S : Type u} {A : Type v}

def PreservesSteps (P : Process S A) (g : S → S) : Prop :=
  ∀ s a t, P.step s a t → P.step (g s) a (g t)

def UniqueAfter (P : Process S A) (s : S) (word : List A) : Prop :=
  ∀ t u, Trace P s word t → Trace P s word u → t = u

theorem fixed_start_unique_end {P : Process S A} {g : S → S}
    (preserves : PreservesSteps P g) {s t : S} {word : List A}
    (fixed : g s = s) (run : Trace P s word t)
    (unique : UniqueAfter P s word) : g t = t := by
  have mapped := trace_map preserves run
  rw [fixed] at mapped
  exact unique (g t) t mapped run

/-- The alternative outcome is exhibited constructively, with no excluded
    middle or claim that it will actually occur. -/
theorem changed_end_exhibits_alternative {P : Process S A} {g : S → S}
    (preserves : PreservesSteps P g) {s t : S} {word : List A}
    (fixed : g s = s) (run : Trace P s word t) (changed : g t ≠ t) :
    ∃ other, Trace P s word other ∧ other ≠ t := by
  have mapped := trace_map preserves run
  rw [fixed] at mapped
  exact ⟨g t, mapped, changed⟩

theorem asymmetry_excludes_joint_contract {P : Process S A} {g : S → S}
    {s t : S} {word : List A} (run : Trace P s word t) (changed : g t ≠ t) :
    ¬ (PreservesSteps P g ∧ g s = s ∧ UniqueAfter P s word) := by
  intro ⟨preserves, fixed, unique⟩
  exact changed (fixed_start_unique_end preserves fixed run unique)

/-- Symmetry of the whole outcome domain does not say each outcome is fixed. -/
theorem outcome_domain_symmetric {P : Process S A} {g : S → S}
    (preserves : PreservesSteps P g) (involution : ∀ s, g (g s) = s)
    {s : S} (fixed : g s = s) (word : List A) (t : S) :
    Trace P s word (g t) ↔ Trace P s word t := by
  constructor
  · intro run
    have mapped := trace_map preserves run
    rw [fixed, involution] at mapped
    exact mapped
  · intro run
    have mapped := trace_map preserves run
    rw [fixed] at mapped
    exact mapped

theorem step_uniqueness_implies_trace_uniqueness (P : Process S A)
    (unique : ∀ s a t u, P.step s a t → P.step s a u → t = u)
    (s : S) (word : List A) : UniqueAfter P s word := by
  intro t u first second
  induction first generalizing u with
  | nil s =>
    cases second
    rfl
  | @cons s m t a word step tail ih =>
    cases second with
    | @cons _ n _ _ _ next rest =>
      have same := unique s a m n step next
      cases same
      exact ih rest

def exchange : Option Bool → Option Bool
  | none => none
  | some b => some (!b)

def branching : Process (Option Bool) Unit where
  step
    | none, _, some _ => True
    | some b, _, some c => c = b
    | _, _, none => False

theorem exchange_involutive (s : Option Bool) : exchange (exchange s) = s := by
  cases s with
  | none => rfl
  | some b => cases b <;> rfl

theorem exchange_fixes_unformed : exchange none = none := rfl

theorem exchange_changes_formed (b : Bool) : exchange (some b) ≠ some b := by
  cases b <;> intro bad <;> cases bad

theorem branching_preserves_exchange : PreservesSteps branching exchange := by
  intro s a t step
  cases s with
  | none =>
    cases t with
    | none => exact False.elim step
    | some b => exact True.intro
  | some b =>
    cases t with
    | none => exact False.elim step
    | some c =>
      change c = b at step
      cases step
      rfl

theorem formed_branch_retained (b : Bool) (n : Nat) :
    Trace branching (some b) (List.replicate n ()) (some b) := by
  induction n with
  | zero => exact .nil _
  | succ n ih => exact .cons rfl ih

theorem either_branch_forms_and_continues (b : Bool) (n : Nat) :
    Trace branching none (List.replicate (n + 1) ()) (some b) :=
  .cons True.intro (formed_branch_retained b n)

theorem formed_branch_cannot_switch (b : Bool) {word : List Unit}
    {t : Option Bool} (run : Trace branching (some b) word t) : t = some b := by
  generalize hs : some b = s at run
  induction run with
  | nil s => exact hs.symm
  | @cons s m t a word step tail ih =>
    cases hs
    cases m with
    | none => exact False.elim step
    | some c =>
      change c = b at step
      cases step
      exact ih rfl

theorem symmetric_law_has_retained_asymmetric_outcomes (n : Nat) :
    PreservesSteps branching exchange ∧ exchange none = none ∧
      Trace branching none (List.replicate (n + 1) ()) (some false) ∧
      exchange (some false) ≠ some false ∧
      ¬ UniqueAfter branching none (List.replicate (n + 1) ()) := by
  refine ⟨branching_preserves_exchange, rfl,
    either_branch_forms_and_continues false n, exchange_changes_formed false, ?_⟩
  intro unique
  have bad := unique (some false) (some true)
    (either_branch_forms_and_continues false n)
    (either_branch_forms_and_continues true n)
  cases bad

/-- A deterministic refinement retains the branch seed as part of the same
    whole configuration. Its initial state is no longer symmetric. -/
def seededUpdate (s : Option Bool × Bool) : Option Bool × Bool :=
  match s.1 with
  | none => (some s.2, s.2)
  | some b => (some b, s.2)

def seededExchange (s : Option Bool × Bool) : Option Bool × Bool :=
  (exchange s.1, !s.2)

def seeded : Process (Option Bool × Bool) Unit where
  step s _ t := t = seededUpdate s

theorem seeded_update_commutes (s : Option Bool × Bool) :
    seededUpdate (seededExchange s) = seededExchange (seededUpdate s) := by
  cases s with
  | mk state seed => cases state <;> rfl

theorem seeded_is_deterministic :
    ∀ s a t u, seeded.step s a t → seeded.step s a u → t = u := by
  intro s a t u ht hu
  exact ht.trans hu.symm

theorem seed_supplies_initial_asymmetry (b : Bool) :
    seededExchange (none, b) ≠ (none, b) := by
  cases b <;> intro bad <;> cases bad

theorem seeded_step_projects (s t : Option Bool × Bool) (a : Unit)
    (step : seeded.step s a t) : branching.step s.1 a t.1 := by
  change t = seededUpdate s at step
  cases step
  cases s with
  | mk state seed =>
    cases state with
    | none => exact True.intro
    | some b => rfl

theorem seeded_trace_projects {s t : Option Bool × Bool} {word : List Unit}
    (run : Trace seeded s word t) : Trace branching s.1 word t.1 :=
  trace_map (fun s a t h => seeded_step_projects s t a h) run

theorem fixed_seed_does_not_cover_other_branch :
    Trace branching none [()] (some true) ∧
      ¬ ∃ t, Trace seeded (none, false) [()] t ∧ t.1 = some true := by
  refine ⟨either_branch_forms_and_continues true 0, ?_⟩
  intro ⟨t, run, target⟩
  cases run with
  | cons step tail =>
    cases tail
    change t = (some false, false) at step
    cases step
    cases target

#print axioms PreservesSteps
#print axioms UniqueAfter
#print axioms fixed_start_unique_end
#print axioms changed_end_exhibits_alternative
#print axioms asymmetry_excludes_joint_contract
#print axioms outcome_domain_symmetric
#print axioms step_uniqueness_implies_trace_uniqueness
#print axioms exchange
#print axioms branching
#print axioms exchange_involutive
#print axioms exchange_fixes_unformed
#print axioms exchange_changes_formed
#print axioms branching_preserves_exchange
#print axioms formed_branch_retained
#print axioms either_branch_forms_and_continues
#print axioms formed_branch_cannot_switch
#print axioms symmetric_law_has_retained_asymmetric_outcomes
#print axioms seededUpdate
#print axioms seededExchange
#print axioms seeded
#print axioms seeded_update_commutes
#print axioms seeded_is_deterministic
#print axioms seed_supplies_initial_asymmetry
#print axioms seeded_step_projects
#print axioms seeded_trace_projects
#print axioms fixed_seed_does_not_cover_other_branch

end FormationSymmetry
