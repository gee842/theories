import ExplanatoryBranching
import ExplanatoryUniversality

/-! Compound questions about one whole's jointly realizable parts. The joint
relation has no assumed associativity, unit, commutativity or free duplication.
Compactness is imposed on correlated pairs, not on their separate marginals. -/
namespace Generative.ExplanatoryJointness
open ExplanatoryUniqueness
universe u v w x y z

def FiberCompact {W : Type u} {Q : Type v} (domain : W → Prop)
    (truth : W → Q → Prop) : Prop :=
  ∀ Γ : Q → Prop,
    (∀ fs : List Q, (∀ f, f ∈ fs → Γ f) →
      ∃ t, domain t ∧ ∀ f, f ∈ fs → truth t f) →
    ∃ t, domain t ∧ ∀ f, Γ f → truth t f

theorem finite_exclusions {W : Type u} {Q : Type v} (truth : W → Q → Prop)
    (xs : List W) (Γ : Q → Prop)
    (fail : ∀ t, t ∈ xs → ∃ f, Γ f ∧ ¬ truth t f) :
    ∃ fs : List Q, (∀ f, f ∈ fs → Γ f) ∧
      ∀ t, t ∈ xs → ∃ f, f ∈ fs ∧ ¬ truth t f := by
  induction xs with
  | nil => exact ⟨[], by simp, by simp⟩
  | cons t xs ih =>
    obtain ⟨f, gf, nf⟩ := fail t List.mem_cons_self
    obtain ⟨fs, gs, ns⟩ := ih (fun s hs => fail s (List.mem_cons_of_mem t hs))
    refine ⟨f :: fs, ?_, ?_⟩
    · intro g hg
      cases List.mem_cons.mp hg with
      | inl eq => exact eq ▸ gf
      | inr mem => exact gs g mem
    · intro s hs
      cases List.mem_cons.mp hs with
      | inl eq => subst s; exact ⟨f, List.mem_cons_self, nf⟩
      | inr mem =>
        obtain ⟨g, hg, ng⟩ := ns s mem
        exact ⟨g, List.mem_cons_of_mem f hg, ng⟩

theorem finite_fiber_compact {W : Type u} {Q : Type v} (domain : W → Prop)
    (truth : W → Q → Prop) (xs : List W) (cover : ∀ t, domain t ↔ t ∈ xs) :
    FiberCompact domain truth := by
  classical
  intro Γ finiteParts
  apply Classical.byContradiction
  intro no
  have fail : ∀ t, t ∈ xs → ∃ f, Γ f ∧ ¬ truth t f := by
    intro t ht
    apply Classical.byContradiction
    intro absent
    apply no
    refine ⟨t, (cover t).mpr ht, ?_⟩
    intro f gf
    apply Classical.byContradiction
    exact fun nf => absent ⟨f, gf, nf⟩
  obtain ⟨fs, gs, exclude⟩ := finite_exclusions truth xs Γ fail
  obtain ⟨t, ht, all⟩ := finiteParts fs gs
  obtain ⟨f, hf, nf⟩ := exclude t ((cover t).mp ht)
  exact nf (all f hf)

inductive Test (A : Type v) (O : Type w) where
  | top
  | atom : O → Test A O
  | neg : Test A O → Test A O
  | conj : Test A O → Test A O → Test A O
  | after : A → Test A O → Test A O
  | together : Test A O → Test A O → Test A O

structure Model (S : Type u) (A : Type v) (O : Type w) where
  process : Process S A
  condition : S → O → Prop
  joint : S → S → S → Prop

def Holds {S : Type u} {A : Type v} {O : Type w} (m : Model S A O) (s : S) : Test A O → Prop
  | .top => True
  | .atom o => m.condition s o
  | .neg f => ¬ Holds m s f
  | .conj f g => Holds m s f ∧ Holds m s g
  | .after a f => ∃ t, m.process.step s a t ∧ Holds m t f
  | .together f g => ∃ l r, m.joint s l r ∧ Holds m l f ∧ Holds m r g

def allTests {A : Type v} {O : Type w} : List (Test A O) → Test A O
  | [] => .top
  | f :: fs => .conj f (allTests fs)

variable {S : Type u} {T : Type x} {A : Type v} {O : Type w}
variable {m : Model S A O} {n : Model T A O}

theorem holds_allTests (s : S) (fs : List (Test A O)) :
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

def Same (m : Model S A O) (n : Model T A O) (s : S) (t : T) : Prop :=
  ∀ f, Holds m s f ↔ Holds n t f

def StepCompact (m : Model S A O) : Prop :=
  ∀ s a, FiberCompact (m.process.step s a) (Holds m)

def JointCompact (m : Model S A O) : Prop :=
  ∀ s, FiberCompact (fun p : S × S => m.joint s p.1 p.2)
    (fun (p : S × S) (fg : Test A O × Test A O) => Holds m p.1 fg.1 ∧ Holds m p.2 fg.2)

structure Bisimulation (m : Model S A O) (n : Model T A O) (R : S → T → Prop) : Prop where
  atomic : ∀ s t, R s t → ∀ o, m.condition s o ↔ n.condition t o
  forth : ∀ s t a s', R s t → m.process.step s a s' →
    ∃ t', n.process.step t a t' ∧ R s' t'
  back : ∀ s t a t', R s t → n.process.step t a t' →
    ∃ s', m.process.step s a s' ∧ R s' t'
  jointForth : ∀ s t l r, R s t → m.joint s l r →
    ∃ l' r', n.joint t l' r' ∧ R l l' ∧ R r r'
  jointBack : ∀ s t l' r', R s t → n.joint t l' r' →
    ∃ l r, m.joint s l r ∧ R l l' ∧ R r r'

theorem same_symm {s : S} {t : T} (h : Same m n s t) : Same n m t s := fun f => (h f).symm

theorem complete_theory_same {s : S} {t : T}
    (h : ∀ f, Holds m s f → Holds n t f) : Same m n s t := by
  classical
  intro f
  refine ⟨h f, ?_⟩
  intro yes
  apply Classical.byContradiction
  exact fun no => h (.neg f) no yes

theorem bisimulation_preserves_tests {R : S → T → Prop} (bis : Bisimulation m n R) :
    ∀ f s t, R s t → (Holds m s f ↔ Holds n t f) := by
  intro f
  induction f with
  | top => intro s t _; exact Iff.rfl
  | atom o => intro s t hr; exact bis.atomic s t hr o
  | neg f ih => intro s t hr; exact not_congr (ih s t hr)
  | conj f g ihf ihg => intro s t hr; exact and_congr (ihf s t hr) (ihg s t hr)
  | after a f ih =>
    intro s t hr
    constructor
    · rintro ⟨s', hs, hf⟩
      obtain ⟨t', ht, rel⟩ := bis.forth s t a s' hr hs
      exact ⟨t', ht, (ih s' t' rel).mp hf⟩
    · rintro ⟨t', ht, hf⟩
      obtain ⟨s', hs, rel⟩ := bis.back s t a t' hr ht
      exact ⟨s', hs, (ih s' t' rel).mpr hf⟩
  | together f g ihf ihg =>
    intro s t hr
    constructor
    · rintro ⟨l, r, hj, hf, hg⟩
      obtain ⟨l', r', hj', hl, hr'⟩ := bis.jointForth s t l r hr hj
      exact ⟨l', r', hj', (ihf l l' hl).mp hf, (ihg r r' hr').mp hg⟩
    · rintro ⟨l', r', hj', hf, hg⟩
      obtain ⟨l, r, hj, hl, hr'⟩ := bis.jointBack s t l' r' hr hj'
      exact ⟨l, r, hj, (ihf l l' hl).mpr hf, (ihg r r' hr').mpr hg⟩

theorem compact_step_match (compact : StepCompact n)
    {s s' : S} {t : T} {a : A} (same : Same m n s t) (step : m.process.step s a s') :
    ∃ t', n.process.step t a t' ∧ Same m n s' t' := by
  have parts : ∀ fs : List (Test A O), (∀ f, f ∈ fs → Holds m s' f) →
      ∃ t', n.process.step t a t' ∧ ∀ f, f ∈ fs → Holds n t' f := by
    intro fs all
    have yes : Holds m s (.after a (allTests fs)) := ⟨s', step, (holds_allTests s' fs).mpr all⟩
    obtain ⟨t', ht, hf⟩ := (same (.after a (allTests fs))).mp yes
    exact ⟨t', ht, (holds_allTests t' fs).mp hf⟩
  obtain ⟨t', ht, all⟩ := compact t a (Holds m s') parts
  exact ⟨t', ht, complete_theory_same all⟩

theorem compact_joint_match (compact : JointCompact n)
    {s l r : S} {t : T} (same : Same m n s t) (joint : m.joint s l r) :
    ∃ l' r', n.joint t l' r' ∧ Same m n l l' ∧ Same m n r r' := by
  let Γ := fun fg : Test A O × Test A O => Holds m l fg.1 ∧ Holds m r fg.2
  have parts : ∀ fs : List (Test A O × Test A O), (∀ fg, fg ∈ fs → Γ fg) →
      ∃ p : T × T, n.joint t p.1 p.2 ∧
        ∀ fg, fg ∈ fs → Holds n p.1 fg.1 ∧ Holds n p.2 fg.2 := by
    intro fs all
    have left : Holds m l (allTests (fs.map Prod.fst)) := by
      apply (holds_allTests _ _).mpr
      intro f hf
      obtain ⟨fg, mem, rfl⟩ := List.mem_map.mp hf
      exact (all fg mem).1
    have right : Holds m r (allTests (fs.map Prod.snd)) := by
      apply (holds_allTests _ _).mpr
      intro f hf
      obtain ⟨fg, mem, rfl⟩ := List.mem_map.mp hf
      exact (all fg mem).2
    have yes : Holds m s (.together (allTests (fs.map Prod.fst)) (allTests (fs.map Prod.snd))) :=
      ⟨l, r, joint, left, right⟩
    obtain ⟨l', r', hj, hl, hr⟩ := (same _).mp yes
    refine ⟨(l', r'), hj, ?_⟩
    intro fg mem
    exact ⟨(holds_allTests _ _).mp hl fg.1 (List.mem_map.mpr ⟨fg, mem, rfl⟩),
      (holds_allTests _ _).mp hr fg.2 (List.mem_map.mpr ⟨fg, mem, rfl⟩)⟩
  obtain ⟨p, hj, all⟩ := compact t Γ parts
  refine ⟨p.1, p.2, hj, complete_theory_same ?_, complete_theory_same ?_⟩
  · intro f hf
    exact (all (f, .top) ⟨hf, True.intro⟩).1
  · intro f hf
    exact (all (.top, f) ⟨True.intro, hf⟩).2

theorem compact_same_bisimulation (sm : StepCompact m) (sn : StepCompact n)
    (jm : JointCompact m) (jn : JointCompact n) : Bisimulation m n (Same m n) := by
  constructor
  · intro s t same o; exact same (.atom o)
  · intro s t a s' same step; exact compact_step_match sn same step
  · intro s t a t' same step
    obtain ⟨s', hs, rel⟩ := compact_step_match sm (same_symm same) step
    exact ⟨s', hs, same_symm rel⟩
  · intro s t l r same joint; exact compact_joint_match jn same joint
  · intro s t l' r' same joint
    obtain ⟨l, r, hj, hl, hr⟩ := compact_joint_match jm (same_symm same) joint
    exact ⟨l, r, hj, same_symm hl, same_symm hr⟩

theorem compact_same_iff_bisimilar (sm : StepCompact m) (sn : StepCompact n)
    (jm : JointCompact m) (jn : JointCompact n) (s : S) (t : T) :
    Same m n s t ↔ ∃ R, Bisimulation m n R ∧ R s t :=
  ⟨fun h => ⟨Same m n, compact_same_bisimulation sm sn jm jn, h⟩,
    fun ⟨_, bis, hr⟩ f => bisimulation_preserves_tests bis f s t hr⟩

theorem finite_steps_compact
    (finite : ∀ s a, ∃ xs : List S, ∀ t, m.process.step s a t ↔ t ∈ xs) : StepCompact m := by
  intro s a
  obtain ⟨xs, hx⟩ := finite s a
  exact finite_fiber_compact _ _ xs hx

theorem finite_joints_compact
    (finite : ∀ s, ∃ xs : List (S × S), ∀ p, m.joint s p.1 p.2 ↔ p ∈ xs) : JointCompact m := by
  intro s
  obtain ⟨xs, hx⟩ := finite s
  exact finite_fiber_compact _ _ xs hx

def Separated (m : Model S A O) : Prop := ∀ s t, Same m m s t → s = t

theorem same_target_unique (sep : Separated n) {s : S} {t t' : T}
    (h : Same m n s t) (h' : Same m n s t') : t = t' :=
  sep t t' (fun f => (h f).symm.trans (h' f))

theorem separated_joint_correspondence (jm : JointCompact m) (jn : JointCompact n)
    (sm : Separated m) (sn : Separated n) {s l r : S} {t l' r' : T}
    (hs : Same m n s t) (hl : Same m n l l') (hr : Same m n r r') :
    m.joint s l r ↔ n.joint t l' r' := by
  constructor
  · intro h
    obtain ⟨x, y, hj, hx, hy⟩ := compact_joint_match jn hs h
    have ex := same_target_unique sn hx hl
    have ey := same_target_unique sn hy hr
    exact ex ▸ ey ▸ hj
  · intro h
    obtain ⟨x, y, hj, hx, hy⟩ := compact_joint_match jm (same_symm hs) h
    have ex := same_target_unique sm hx (same_symm hl)
    have ey := same_target_unique sm hy (same_symm hr)
    exact ex ▸ ey ▸ hj

def codeJoint {C : Type y} (m : Model S A O) (p : Presentation S (Test A O) C)
    (c l r : C) : Prop := ∃ s x y, p.encode s = c ∧ p.encode x = l ∧
      p.encode y = r ∧ m.joint s x y

theorem code_joint_lifts_from_whole {C : Type y} {p : Presentation S (Test A O) C}
    (compact : JointCompact m) (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p)
    (s : S) (l r : C) :
    codeJoint m p (p.encode s) l r ↔
      ∃ x y, m.joint s x y ∧ p.encode x = l ∧ p.encode y = r := by
  constructor
  · rintro ⟨s', x', y', hs, hx, hy, hj⟩
    have same : Same m m s' s := equal_codes_same_answers exact hs
    obtain ⟨x, y, h, he, hf⟩ := compact_joint_match compact same hj
    exact ⟨x, y, h, (reduced x' x he).symm.trans hx, (reduced y' y hf).symm.trans hy⟩
  · rintro ⟨x, y, h, hx, hy⟩
    exact ⟨s, x, y, rfl, hx, hy, h⟩

/-- A finite nested joint plan retains a common witness at each decomposition.
It does not yet fix specific leaf identities or cross-branch sharing. -/
inductive Plan (Q : Type v) where
  | leaf : Q → Plan Q
  | pair : Plan Q → Plan Q → Plan Q

def Realizes {X : Type u} {Q : Type v} (J : X → X → X → Prop)
    (leaf : X → Q → Prop) : X → Plan Q → Prop
  | s, .leaf q => leaf s q
  | s, .pair p q => ∃ x y, J s x y ∧ Realizes J leaf x p ∧ Realizes J leaf y q

theorem joint_plan_lifts {C : Type y} {Q : Type z} {p : Presentation S (Test A O) C}
    (compact : JointCompact m) (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p)
    (leaf : S → Q → Prop) (read : C → Q → Prop)
    (correct : ∀ s q, read (p.encode s) q ↔ leaf s q) (plan : Plan Q) :
    ∀ s, Realizes (codeJoint m p) read (p.encode s) plan ↔ Realizes m.joint leaf s plan := by
  induction plan with
  | leaf q => exact fun s => correct s q
  | pair left right ihl ihr =>
    intro s
    constructor
    · rintro ⟨l, r, hj, hl, hr⟩
      obtain ⟨x, y, hxy, hx, hy⟩ := (code_joint_lifts_from_whole compact exact reduced s l r).mp hj
      exact ⟨x, y, hxy, (ihl x).mp (hx.symm ▸ hl), (ihr y).mp (hy.symm ▸ hr)⟩
    · rintro ⟨x, y, hj, hx, hy⟩
      exact ⟨p.encode x, p.encode y, ⟨s, x, y, rfl, rfl, rfl, hj⟩,
        (ihl x).mpr hx, (ihr y).mpr hy⟩

def sequential (m : Model S A O) : ExplanatoryBranching.Model S A O :=
  ⟨m.process, m.condition⟩

def embed : ExplanatoryBranching.Test A O → Test A O
  | .top => .top
  | .atom o => .atom o
  | .neg f => .neg (embed f)
  | .conj f g => .conj (embed f) (embed g)
  | .after a f => .after a (embed f)

theorem embed_preserves (f : ExplanatoryBranching.Test A O) :
    ∀ s, Holds m s (embed f) ↔ ExplanatoryBranching.Holds (sequential m) s f := by
  induction f with
  | top => exact fun _ => Iff.rfl
  | atom o => exact fun _ => Iff.rfl
  | neg f ih => intro s; exact not_congr (ih s)
  | conj f g ihf ihg => intro s; exact and_congr (ihf s) (ihg s)
  | after a f ih =>
    intro s
    constructor
    · rintro ⟨t, ht, hf⟩; exact ⟨t, ht, (ih t).mp hf⟩
    · rintro ⟨t, ht, hf⟩; exact ⟨t, ht, (ih t).mpr hf⟩

end Generative.ExplanatoryJointness

#print axioms Generative.ExplanatoryJointness.finite_exclusions
#print axioms Generative.ExplanatoryJointness.finite_fiber_compact
#print axioms Generative.ExplanatoryJointness.holds_allTests
#print axioms Generative.ExplanatoryJointness.same_symm
#print axioms Generative.ExplanatoryJointness.complete_theory_same
#print axioms Generative.ExplanatoryJointness.bisimulation_preserves_tests
#print axioms Generative.ExplanatoryJointness.compact_step_match
#print axioms Generative.ExplanatoryJointness.compact_joint_match
#print axioms Generative.ExplanatoryJointness.compact_same_bisimulation
#print axioms Generative.ExplanatoryJointness.compact_same_iff_bisimilar
#print axioms Generative.ExplanatoryJointness.finite_steps_compact
#print axioms Generative.ExplanatoryJointness.finite_joints_compact
#print axioms Generative.ExplanatoryJointness.same_target_unique
#print axioms Generative.ExplanatoryJointness.separated_joint_correspondence
#print axioms Generative.ExplanatoryJointness.code_joint_lifts_from_whole
#print axioms Generative.ExplanatoryJointness.joint_plan_lifts
#print axioms Generative.ExplanatoryJointness.embed_preserves
