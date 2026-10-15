import ExplanatoryBranchingRecovery -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Composition.jointAlike_iff_sameJointTests`, `Becoming.Composition.SameJointTests.step_passing`, `Becoming.CompositionBridge.compact_same_iff_bisimilar_of_stable` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-! Successor compactness replaces finite branching. It is an explicit
realization condition on the selected model, not a principle inferred from
finite observations or a postulate about all reality. -/
namespace Generative.ExplanatoryCompactness
open ExplanatoryBranching ExplanatoryUniqueness ExplanatoryBranchingRecovery
universe u v w x y

def allTests {A : Type v} {O : Type w} : List (Test A O) → Test A O
  | [] => .top
  | f :: fs => .conj f (allTests fs)

theorem holds_allTests {S : Type u} {A : Type v} {O : Type w}
    (m : Model S A O) (s : S) (fs : List (Test A O)) :
    Holds m s (allTests fs) ↔ ∀ f, f ∈ fs → Holds m s f := by
  induction fs with
  | nil => simp [allTests, Holds]
  | cons f fs ih =>
    simp only [allTests, Holds, ih, List.mem_cons]
    constructor
    · rintro ⟨hf, hs⟩ g (rfl | hg)
      · exact hf
      · exact hs g hg
    · intro h
      exact ⟨h f (Or.inl rfl), fun g hg => h g (Or.inr hg)⟩

def FinitelyRealizable {S : Type u} {A : Type v} {O : Type w}
    (m : Model S A O) (s : S) (a : A) (Γ : Test A O → Prop) : Prop :=
  ∀ fs : List (Test A O), (∀ f, f ∈ fs → Γ f) →
    ∃ t, m.process.step s a t ∧ ∀ f, f ∈ fs → Holds m t f

def SuccessorCompact {S : Type u} {A : Type v} {O : Type w}
    (m : Model S A O) : Prop :=
  ∀ s a Γ, FinitelyRealizable m s a Γ →
    ∃ t, m.process.step s a t ∧ ∀ f, Γ f → Holds m t f

variable {S : Type u} {T : Type x} {A : Type v} {O : Type w}
variable {m : Model S A O} {n : Model T A O}

theorem finite_exclusion_list (xs : List S) (Γ : Test A O → Prop)
    (fail : ∀ s, s ∈ xs → ∃ f, Γ f ∧ ¬ Holds m s f) :
    ∃ fs : List (Test A O), (∀ f, f ∈ fs → Γ f) ∧
      ∀ s, s ∈ xs → ∃ f, f ∈ fs ∧ ¬ Holds m s f := by
  induction xs with
  | nil => exact ⟨[], by simp, by simp⟩
  | cons s xs ih =>
    obtain ⟨f, gf, hf⟩ := fail s List.mem_cons_self
    obtain ⟨fs, gs, hs⟩ := ih (fun t ht => fail t (List.mem_cons_of_mem s ht))
    refine ⟨f :: fs, ?_, ?_⟩
    · intro g hg
      cases List.mem_cons.mp hg with
      | inl eq => exact eq ▸ gf
      | inr mem => exact gs g mem
    · intro t ht
      cases List.mem_cons.mp ht with
      | inl eq => subst t; exact ⟨f, List.mem_cons_self, hf⟩
      | inr mem =>
        obtain ⟨g, hg, no⟩ := hs t mem
        exact ⟨g, List.mem_cons_of_mem f hg, no⟩

theorem imageFinite_successorCompact (finite : ImageFinite m) : SuccessorCompact m := by
  classical
  intro s a Γ finiteParts
  apply Classical.byContradiction
  intro no
  obtain ⟨xs, hx⟩ := finite s a
  have fail : ∀ t, t ∈ xs → ∃ f, Γ f ∧ ¬ Holds m t f := by
    intro t ht
    apply Classical.byContradiction
    intro absent
    apply no
    refine ⟨t, (hx t).mpr ht, ?_⟩
    intro f gf
    apply Classical.byContradiction
    exact fun nf => absent ⟨f, gf, nf⟩
  obtain ⟨fs, gf, exclude⟩ := finite_exclusion_list xs Γ fail
  obtain ⟨t, ht, holds⟩ := finiteParts fs gf
  obtain ⟨f, hf, nf⟩ := exclude t ((hx t).mp ht)
  exact nf (holds f hf)

theorem complete_theory_forces_same {s : S} {t : T}
    (h : ∀ f, Holds m s f → Holds n t f) : Same m n s t := by
  classical
  intro f
  refine ⟨h f, ?_⟩
  intro yes
  apply Classical.byContradiction
  intro no
  exact h (.neg f) no yes

theorem successor_theory_finitely_realizable {s s' : S} {t : T} {a : A}
    (same : Same m n s t) (step : m.process.step s a s') :
    FinitelyRealizable n t a (Holds m s') := by
  intro fs trueAt
  have yes : Holds m s (.after a (allTests fs)) :=
    ⟨s', step, (holds_allTests m s' fs).mpr trueAt⟩
  obtain ⟨t', ht, all⟩ := (same (.after a (allTests fs))).mp yes
  exact ⟨t', ht, (holds_allTests n t' fs).mp all⟩

theorem compact_successor_match (compact : SuccessorCompact n)
    {s s' : S} {t : T} {a : A} (same : Same m n s t)
    (step : m.process.step s a s') :
    ∃ t', n.process.step t a t' ∧ Same m n s' t' := by
  obtain ⟨t', ht, all⟩ := compact t a (Holds m s')
    (successor_theory_finitely_realizable same step)
  exact ⟨t', ht, complete_theory_forces_same all⟩

theorem compact_same_is_bisimulation (cm : SuccessorCompact m) (cn : SuccessorCompact n) :
    Bisimulation m n (Same m n) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · intro s t a s' same hs
    exact compact_successor_match cn same hs
  · intro s t a t' same ht
    obtain ⟨s', hs, related⟩ := compact_successor_match cm (same_symm same) ht
    exact ⟨s', hs, same_symm related⟩
  · intro s t same o
    exact same (.atom o)

theorem compact_same_iff_bisimilar (cm : SuccessorCompact m) (cn : SuccessorCompact n)
    (s : S) (t : T) : Same m n s t ↔ ∃ R, Bisimulation m n R ∧ R s t :=
  ⟨fun h => ⟨Same m n, compact_same_is_bisimulation cm cn, h⟩,
    fun ⟨_, h, hr⟩ => bisimulation_implies_same h hr⟩

theorem compact_structural_correspondence (cm : SuccessorCompact m) (cn : SuccessorCompact n)
    {root : S} {otherRoot : T} (h : Same m n root otherRoot)
    (rm : ReachableFrom m root) (rn : ReachableFrom n otherRoot)
    (sm : Separated m) (sn : Separated n) :
    (∀ s, ∃ t, Same m n s t ∧ ∀ t', Same m n s t' → t' = t) ∧
    (∀ t, ∃ s, Same m n s t ∧ ∀ s', Same m n s' t → s' = s) := by
  constructor
  · intro s
    obtain ⟨word, trace⟩ := rm s
    obtain ⟨t, _, related⟩ := bisimulation_lifts_trace (compact_same_is_bisimulation cm cn) h trace
    exact ⟨t, related, fun _ h' => same_functional sn h' related⟩
  · intro t
    obtain ⟨word, trace⟩ := rn t
    obtain ⟨s, _, related⟩ := bisimulation_lifts_trace (compact_same_is_bisimulation cn cm)
      (same_symm h) trace
    have hs := same_symm related
    exact ⟨s, hs, fun _ h' => same_inverse_functional sm h' hs⟩

theorem compact_correspondence_preserves_steps (cm : SuccessorCompact m) (cn : SuccessorCompact n)
    (sm : Separated m) (sn : Separated n) {s s' : S} {t t' : T}
    (h : Same m n s t) (h' : Same m n s' t') (a : A) :
    m.process.step s a s' ↔ n.process.step t a t' := by
  constructor
  · intro hs
    obtain ⟨z, hz, he⟩ := compact_successor_match cn h hs
    exact same_functional sn he h' ▸ hz
  · intro ht
    obtain ⟨z, hz, he⟩ := compact_successor_match cm (same_symm h) ht
    exact same_inverse_functional sm (same_symm he) h' ▸ hz

variable {C : Type y} {account : Presentation S (Test A O) C}

theorem compact_code_step_lifts (compact : SuccessorCompact m)
    (exact : Exact (Holds m) account) (reduced : Reduced (Holds m) account)
    (s : S) (a : A) (d : C) :
    (codeProcess m account).step (account.encode s) a d ↔
      ∃ t, m.process.step s a t ∧ account.encode t = d := by
  constructor
  · rintro ⟨x, y, hx, hxy, hy⟩
    have eq : Same m m x s := equal_codes_same_answers exact hx
    obtain ⟨t, ht, related⟩ := compact_successor_match compact eq hxy
    exact ⟨t, ht, (reduced t y (same_symm related)).trans hy⟩
  · rintro ⟨t, ht, hd⟩
    exact ⟨s, t, rfl, ht, hd⟩

theorem compact_code_trace_lifts (compact : SuccessorCompact m)
    (exact : Exact (Holds m) account) (reduced : Reduced (Holds m) account)
    (s : S) (word : List A) (d : C) :
    Trace (codeProcess m account) (account.encode s) word d ↔
      ∃ t, Trace m.process s word t ∧ account.encode t = d := by
  constructor
  · intro trace
    generalize hstart : account.encode s = c at trace
    induction trace generalizing s with
    | nil c => exact ⟨s, .nil s, hstart⟩
    | @cons c mid finish a rest step tail ih =>
      have st : (codeProcess m account).step (account.encode s) a mid := hstart ▸ step
      obtain ⟨t, ht, hm⟩ := (compact_code_step_lifts compact exact reduced s a mid).mp st
      obtain ⟨u, hu, hd⟩ := ih t hm
      exact ⟨u, .cons ht hu, hd⟩
  · rintro ⟨t, ht, rfl⟩
    exact native_trace_projects ht

/-- A whole code run lifts using representative-wise one-step lifting and
standard classical choice. This is not an inference from observed prefixes. -/
theorem code_run_lifts_of_step_lifts
    (lift : ∀ s a d, (codeProcess m account).step (account.encode s) a d →
      ∃ t, m.process.step s a t ∧ account.encode t = d)
    (start : S) (events : Nat → A) (codes : Nat → C)
    (initial : account.encode start = codes 0)
    (valid : ∀ k, (codeProcess m account).step (codes k) (events k) (codes (k+1))) :
    ∃ states : Nat → S, states 0 = start ∧
      (∀ k, m.process.step (states k) (events k) (states (k+1))) ∧
      ∀ k, account.encode (states k) = codes k := by
  classical
  let next : ∀ k, (s : {s : S // account.encode s = codes k}) →
      {t : S // m.process.step s.val (events k) t ∧ account.encode t = codes (k+1)} :=
    fun k s =>
      let h := lift s.val (events k) (codes (k+1)) (s.property.symm ▸ valid k)
      ⟨Classical.choose h, Classical.choose_spec h⟩
  let states : (k : Nat) → {s : S // account.encode s = codes k} :=
    fun k => Nat.rec ⟨start, initial⟩
      (fun k s => ⟨(next k s).val, (next k s).property.2⟩) k
  refine ⟨fun k => (states k).val, rfl, ?_, fun k => (states k).property⟩
  intro k
  exact (next k (states k)).property.1

theorem compact_code_run_lifts (compact : SuccessorCompact m)
    (exact : Exact (Holds m) account) (reduced : Reduced (Holds m) account)
    (start : S) (events : Nat → A) (codes : Nat → C)
    (initial : account.encode start = codes 0)
    (valid : ∀ k, (codeProcess m account).step (codes k) (events k) (codes (k+1))) :
    ∃ states : Nat → S, states 0 = start ∧
      (∀ k, m.process.step (states k) (events k) (states (k+1))) ∧
      ∀ k, account.encode (states k) = codes k :=
  code_run_lifts_of_step_lifts
    (fun s a d => (compact_code_step_lifts compact exact reduced s a d).mp)
    start events codes initial valid

end Generative.ExplanatoryCompactness

#print axioms Generative.ExplanatoryCompactness.holds_allTests
#print axioms Generative.ExplanatoryCompactness.finite_exclusion_list
#print axioms Generative.ExplanatoryCompactness.imageFinite_successorCompact
#print axioms Generative.ExplanatoryCompactness.complete_theory_forces_same
#print axioms Generative.ExplanatoryCompactness.successor_theory_finitely_realizable
#print axioms Generative.ExplanatoryCompactness.compact_successor_match
#print axioms Generative.ExplanatoryCompactness.compact_same_is_bisimulation
#print axioms Generative.ExplanatoryCompactness.compact_same_iff_bisimilar
#print axioms Generative.ExplanatoryCompactness.compact_structural_correspondence
#print axioms Generative.ExplanatoryCompactness.compact_correspondence_preserves_steps
#print axioms Generative.ExplanatoryCompactness.compact_code_step_lifts
#print axioms Generative.ExplanatoryCompactness.compact_code_trace_lifts
#print axioms Generative.ExplanatoryCompactness.code_run_lifts_of_step_lifts
#print axioms Generative.ExplanatoryCompactness.compact_code_run_lifts
