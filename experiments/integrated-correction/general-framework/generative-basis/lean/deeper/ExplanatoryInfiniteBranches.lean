import ExplanatoryCompactness -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Likeness.Unbounded.sameBranchingTests`, `Becoming.Likeness.Unbounded.not_alike`, `Becoming.Likeness.Unbounded.rest_holds_iff` — 同一陈述 / the same statement; MODULE-CLASSIFICATION.md

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
  have hs : (model true).process.step .root () .endless := rfl
  obtain ⟨t, ht, same⟩ := compact_successor_match compact
    (same_symm roots_same_all_finite_tests) hs
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
  | finite n =>
    exact no_infinite_run_from_finite false n
      ⟨fun k => r (k+1), h, fun k => steps (k+1)⟩

theorem completed_has_infinite_run : InfiniteRun true .root := by
  refine ⟨fun k => match k with | 0 => .root | _+1 => .endless, rfl, ?_⟩
  intro k
  cases k <;> rfl

theorem finite_answers_do_not_determine_infinite_realization :
    Same (model false) (model true) .root .root ∧
    ¬ InfiniteRun false .root ∧ InfiniteRun true .root :=
  ⟨roots_same_all_finite_tests, countdown_has_no_infinite_run, completed_has_infinite_run⟩

/-- This is a semantic question about one successor, outside the finitary
test syntax. It does not itself assert an actually taken infinite history. -/
def UnboundedSuccessor (b : Bool) : Prop :=
  ∃ t, step b .root () t ∧ ∀ k, Holds (model b) t (survives k)

theorem countdown_no_unbounded_successor : ¬ UnboundedSuccessor false := by
  rintro ⟨t, ht, all⟩
  cases t with
  | root => exact ht
  | endless => cases ht
  | finite n =>
    have impossible := (finite_survives_iff false n (n+1)).mp (all (n+1))
    omega

theorem completed_unbounded_successor : UnboundedSuccessor true :=
  ⟨.endless, rfl, endless_survives true⟩

theorem no_finite_test_defines_unbounded_successor :
    ¬ ∃ f : Test Unit Empty, ∀ b, Holds (model b) .root f ↔ UnboundedSuccessor b := by
  rintro ⟨f, reads⟩
  have yes := (reads true).mpr completed_unbounded_successor
  exact countdown_no_unbounded_successor ((reads false).mp
    ((roots_same_all_finite_tests f).mpr yes))

theorem completed_successorCompact : SuccessorCompact (model true) := by
  classical
  intro s a Γ finiteParts
  cases a
  cases s with
  | root =>
    by_cases he : ∀ f, Γ f → Holds (model true) .endless f
    · exact ⟨.endless, rfl, he⟩
    · have separator : ∃ f, Γ f ∧ ¬ Holds (model true) .endless f := by
        apply Classical.byContradiction
        intro no
        apply he
        intro f gf
        apply Classical.byContradiction
        exact fun nf => no ⟨f, gf, nf⟩
      obtain ⟨f, gf, nf⟩ := separator
      apply Classical.byContradiction
      intro no
      let xs := (List.range (depth f)).map Node.finite
      have fail : ∀ t, t ∈ xs → ∃ g, Γ g ∧ ¬ Holds (model true) t g := by
        intro t ht
        have st : step true .root () t := by
          obtain ⟨n, _, rfl⟩ := List.mem_map.mp ht
          exact True.intro
        apply Classical.byContradiction
        intro absent
        apply no
        refine ⟨t, st, ?_⟩
        intro g gg
        apply Classical.byContradiction
        exact fun ng => absent ⟨g, gg, ng⟩
      obtain ⟨fs, gs, exclude⟩ := finite_exclusion_list xs Γ fail
      have inΓ : ∀ g, g ∈ f :: fs → Γ g := by
        intro g hg
        cases List.mem_cons.mp hg with
        | inl eq => exact eq ▸ gf
        | inr mem => exact gs g mem
      obtain ⟨t, ht, all⟩ := finiteParts (f :: fs) inΓ
      cases t with
      | root => exact ht
      | endless => exact nf (all f List.mem_cons_self)
      | finite n =>
        have below : n < depth f := by
          apply Nat.lt_of_not_ge
          intro large
          exact nf ((finite_approximates_endless true f n large).mp (all f List.mem_cons_self))
        have mem : Node.finite n ∈ xs := List.mem_map.mpr ⟨n, List.mem_range.mpr below, rfl⟩
        obtain ⟨g, hg, ng⟩ := exclude (.finite n) mem
        exact ng (all g (List.mem_cons_of_mem f hg))
  | finite n =>
    cases n with
    | zero =>
      obtain ⟨t, ht, _⟩ := finiteParts [] (by simp)
      exact False.elim ht
    | succ n =>
      refine ⟨.finite n, rfl, ?_⟩
      intro f gf
      obtain ⟨t, ht, all⟩ := finiteParts [f] (by simpa)
      change t = .finite n at ht
      subst t
      exact all f List.mem_cons_self
  | endless =>
    refine ⟨.endless, rfl, ?_⟩
    intro f gf
    obtain ⟨t, ht, all⟩ := finiteParts [f] (by simpa)
    change t = .endless at ht
    subst t
    exact all f List.mem_cons_self

theorem completed_not_imageFinite : ¬ ImageFinite (model true) := by
  intro finite
  obtain ⟨xs, hx⟩ := finite .root ()
  let bound := (xs.map (fun s => match s with | .finite n => n+1 | _ => 0)).foldr max 0
  have members_bounded : ∀ t, t ∈ xs → ∀ n, t = .finite n → n < bound := by
    intro t ht n eq
    subst t
    have general : ∀ ys : List Node, ∀ k, Node.finite k ∈ ys →
        k < (ys.map (fun s => match s with | .finite j => j+1 | _ => 0)).foldr max 0 := by
      intro ys
      induction ys with
      | nil => simp
      | cons z zs ih =>
        intro k hk
        cases List.mem_cons.mp hk with
        | inl eq => subst z; simp only [List.map_cons, List.foldr_cons]; omega
        | inr mem =>
          have h := ih k mem
          simp only [List.map_cons, List.foldr_cons]
          exact Nat.lt_of_lt_of_le h (Nat.le_max_right _ _)
    exact general xs n ht
  exact (Nat.lt_irrefl bound) (members_bounded (.finite bound) ((hx _).mp True.intro) bound rfl)

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
#print axioms Generative.ExplanatoryInfiniteBranches.countdown_no_unbounded_successor
#print axioms Generative.ExplanatoryInfiniteBranches.completed_unbounded_successor
#print axioms Generative.ExplanatoryInfiniteBranches.no_finite_test_defines_unbounded_successor
#print axioms Generative.ExplanatoryInfiniteBranches.completed_successorCompact
#print axioms Generative.ExplanatoryInfiniteBranches.completed_not_imageFinite
