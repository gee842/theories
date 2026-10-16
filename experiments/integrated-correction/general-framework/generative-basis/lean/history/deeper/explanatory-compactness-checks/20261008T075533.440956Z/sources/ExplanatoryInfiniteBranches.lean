import ExplanatoryCompactness

/-! The classical finite-countdown / endless-branch comparison, strengthened
from agreement on finite words to agreement on ALL finite Boolean modal tests.
No independent atomic predicate is toggled: the atom vocabulary is empty. -/
namespace Generative.ExplanatoryInfiniteBranches
open ExplanatoryBranching ExplanatoryCompactness

inductive Node where
  | root
  | finite : Nat → Node
  | endless
  deriving DecidableEq

def step (extra : Bool) : Node → Unit → Node → Prop
  | .root, _, .finite _ => True
  | .root, _, .endless => extra = true
  | .root, _, .root => False
  | .finite 0, _, _ => False
  | .finite (n+1), _, t => t = .finite n
  | .endless, _, t => t = .endless

def model (extra : Bool) : Model Node Unit Empty where
  process.step := step extra
  condition _ o := nomatch o

def depth : Test Unit Empty → Nat
  | .top => 0
  | .atom _ => 0
  | .neg f => depth f
  | .conj f g => max (depth f) (depth g)
  | .after _ f => depth f + 1

theorem after_zero (b : Bool) (f : Test Unit Empty) :
    ¬ Holds (model b) (.finite 0) (.after () f) := by
  simp [Holds, model, step]

theorem after_succ (b : Bool) (n : Nat) (f : Test Unit Empty) :
    Holds (model b) (.finite (n+1)) (.after () f) ↔ Holds (model b) (.finite n) f := by
  simp [Holds, model, step]

theorem after_endless (b : Bool) (f : Test Unit Empty) :
    Holds (model b) .endless (.after () f) ↔ Holds (model b) .endless f := by
  simp [Holds, model, step]

theorem finite_approximates_endless (b : Bool) (f : Test Unit Empty) :
    ∀ n, depth f ≤ n → (Holds (model b) (.finite n) f ↔ Holds (model b) .endless f) := by
  induction f with
  | top => intro n _; exact Iff.rfl
  | atom o => exact nomatch o
  | neg f ih =>
    intro n hn
    exact not_congr (ih n hn)
  | conj f g ihf ihg =>
    intro n hn
    have hf : depth f ≤ n := Nat.le_trans (Nat.le_max_left _ _) hn
    have hg : depth g ≤ n := Nat.le_trans (Nat.le_max_right _ _) hn
    exact and_congr (ihf n hf) (ihg n hg)
  | after a f ih =>
    cases a
    intro n hn
    cases n with
    | zero => simp [depth] at hn
    | succ n =>
      exact (after_succ b n f).trans ((ih n (Nat.le_of_succ_le_succ hn)).trans
        (after_endless b f).symm)

theorem finite_model_agreement (f : Test Unit Empty) :
    ∀ n, Holds (model false) (.finite n) f ↔ Holds (model true) (.finite n) f := by
  induction f with
  | top => intro n; exact Iff.rfl
  | atom o => exact nomatch o
  | neg f ih => intro n; exact not_congr (ih n)
  | conj f g ihf ihg => intro n; exact and_congr (ihf n) (ihg n)
  | after a f ih =>
    cases a
    intro n
    cases n with
    | zero => exact iff_of_false (after_zero false f) (after_zero true f)
    | succ n => exact (after_succ false n f).trans ((ih n).trans (after_succ true n f).symm)

theorem root_after_false (f : Test Unit Empty) :
    Holds (model false) .root (.after () f) ↔ ∃ n, Holds (model false) (.finite n) f := by
  constructor
  · rintro ⟨t, ht, hf⟩
    cases t with
    | root => exact False.elim ht
    | finite n => exact ⟨n, hf⟩
    | endless => cases ht
  · rintro ⟨n, hf⟩
    exact ⟨.finite n, True.intro, hf⟩

theorem root_after_true (f : Test Unit Empty) :
    Holds (model true) .root (.after () f) ↔
      (∃ n, Holds (model true) (.finite n) f) ∨ Holds (model true) .endless f := by
  constructor
  · rintro ⟨t, ht, hf⟩
    cases t with
    | root => exact False.elim ht
    | finite n => exact Or.inl ⟨n, hf⟩
    | endless => exact Or.inr hf
  · rintro (⟨n, hf⟩ | hf)
    · exact ⟨.finite n, True.intro, hf⟩
    · exact ⟨.endless, rfl, hf⟩

theorem roots_same_all_finite_tests : Same (model false) (model true) .root .root := by
  intro f
  induction f with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg f ih => exact not_congr ih
  | conj f g ihf ihg => exact and_congr ihf ihg
  | after a f _ =>
    cases a
    rw [root_after_false, root_after_true]
    constructor
    · rintro ⟨n, hf⟩
      exact Or.inl ⟨n, (finite_model_agreement f n).mp hf⟩
    · rintro (⟨n, hf⟩ | hf)
      · exact ⟨n, (finite_model_agreement f n).mpr hf⟩
      · exact ⟨depth f, (finite_model_agreement f (depth f)).mpr
          ((finite_approximates_endless true f (depth f) (Nat.le_refl _)).mpr hf)⟩

def survives : Nat → Test Unit Empty
  | 0 => .top
  | n+1 => .after () (survives n)

theorem endless_survives (b : Bool) (k : Nat) : Holds (model b) .endless (survives k) := by
  induction k with
  | zero => exact True.intro
  | succ k ih => exact (after_endless b (survives k)).mpr ih

theorem finite_survives_iff (b : Bool) (n k : Nat) :
    Holds (model b) (.finite n) (survives k) ↔ k ≤ n := by
  induction k generalizing n with
  | zero => simp [survives, Holds]
  | succ k ih =>
    cases n with
    | zero => simp [survives, Holds, model, step]
    | succ n => exact (after_succ b n (survives k)).trans ((ih n).trans Nat.succ_le_succ_iff.symm)

theorem no_finite_matches_endless (n : Nat) :
    ¬ Same (model false) (model true) (.finite n) .endless := by
  intro same
  have h := (same (survives (n+1))).mpr (endless_survives true (n+1))
  have impossible := (finite_survives_iff false n (n+1)).mp h
  omega

theorem no_rooted_bisimulation :
    ¬ ∃ R, Bisimulation (model false) (model true) R ∧ R .root .root := by
  rintro ⟨R, bis, hr⟩
  obtain ⟨s, hs, rel⟩ := bis.1.2 .root .root () .endless hr rfl
  cases s with
  | root => exact hs
  | endless => cases hs
  | finite n => exact no_finite_matches_endless n (bisimulation_implies_same bis rel)

theorem countdown_not_successorCompact : ¬ SuccessorCompact (model false) := by
  intro compact
  obtain ⟨t, ht, same⟩ := compact_successor_match compact
    (same_symm roots_same_all_finite_tests) (s' := .endless) (a := ()) rfl
  cases t with
  | root => exact ht
  | endless => cases ht
  | finite n => exact no_finite_matches_endless n (same_symm same)

def InfiniteRun (b : Bool) (s : Node) : Prop :=
  ∃ r : Nat → Node, r 0 = s ∧ ∀ k, step b (r k) () (r (k+1))

theorem no_infinite_run_from_finite (b : Bool) (n : Nat) : ¬ InfiniteRun b (.finite n) := by
  induction n with
  | zero =>
    rintro ⟨r, start, steps⟩
    have first := steps 0
    rw [start] at first
    exact first
  | succ n ih =>
    rintro ⟨r, start, steps⟩
    have first := steps 0
    rw [start] at first
    exact ih ⟨fun k => r (k+1), first, fun k => steps (k+1)⟩

theorem countdown_has_no_infinite_run : ¬ InfiniteRun false .root := by
  rintro ⟨r, start, steps⟩
  have first := steps 0
  rw [start] at first
  cases h : r 1 with
  | root => rw [h] at first; exact first
  | endless => rw [h] at first; cases first
  | finite n => exact no_infinite_run_from_finite false n
      ⟨fun k => r (k+1), h, fun k => steps (k+1)⟩

theorem completed_has_infinite_run : InfiniteRun true .root := by
  refine ⟨fun k => match k with | 0 => .root | _+1 => .endless, rfl, ?_⟩
  intro k
  cases k <;> rfl

theorem finite_answers_do_not_determine_infinite_realization :
    Same (model false) (model true) .root .root ∧
    ¬ InfiniteRun false .root ∧ InfiniteRun true .root :=
  ⟨roots_same_all_finite_tests, countdown_has_no_infinite_run, completed_has_infinite_run⟩

end Generative.ExplanatoryInfiniteBranches

#print axioms Generative.ExplanatoryInfiniteBranches.after_zero
#print axioms Generative.ExplanatoryInfiniteBranches.after_succ
#print axioms Generative.ExplanatoryInfiniteBranches.after_endless
#print axioms Generative.ExplanatoryInfiniteBranches.finite_approximates_endless
#print axioms Generative.ExplanatoryInfiniteBranches.finite_model_agreement
#print axioms Generative.ExplanatoryInfiniteBranches.root_after_false
#print axioms Generative.ExplanatoryInfiniteBranches.root_after_true
#print axioms Generative.ExplanatoryInfiniteBranches.roots_same_all_finite_tests
#print axioms Generative.ExplanatoryInfiniteBranches.endless_survives
#print axioms Generative.ExplanatoryInfiniteBranches.finite_survives_iff
#print axioms Generative.ExplanatoryInfiniteBranches.no_finite_matches_endless
#print axioms Generative.ExplanatoryInfiniteBranches.no_rooted_bisimulation
#print axioms Generative.ExplanatoryInfiniteBranches.countdown_not_successorCompact
#print axioms Generative.ExplanatoryInfiniteBranches.no_infinite_run_from_finite
#print axioms Generative.ExplanatoryInfiniteBranches.countdown_has_no_infinite_run
#print axioms Generative.ExplanatoryInfiniteBranches.completed_has_infinite_run
#print axioms Generative.ExplanatoryInfiniteBranches.finite_answers_do_not_determine_infinite_realization
