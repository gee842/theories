import ExplanatoryJoiningContexts
import ExplanatoryBranching
import ExplanatoryUniversality

/-! Branch questions are generated from the same joining relation. Left/right
name argument positions in that relation. No independent observation predicate,
deterministic outcome, native identity recovery or total joining is assumed.
Finite outcome fibers and exact answers are explicit supplied conditions. -/
namespace Generative.ExplanatoryJoiningBranches
open ExplanatoryLocalUnits ExplanatoryUniqueness ExplanatoryUniversality
open ExplanatoryBranching
universe u v w
variable {F : Type u} {C : Type v} {D : Type w}

inductive Side where | left | right

def model (J : Join F) : Model F (Side × F) Empty where
  process.step x a z := match a.1 with
    | .left => J a.2 x z
    | .right => J x a.2 z
  condition _ o := nomatch o

abbrev Question (F : Type u) := Test (Side × F) Empty
def target (J : Join F) := Holds (model J)
def BranchSame (J : Join F) := Same (model J) (model J)
def FiniteOutcomes (J : Join F) : Prop :=
  ∀ x y, ∃ zs : List F, ∀ z, J x y z ↔ z ∈ zs

theorem finite_outcomes_image_finite {J : Join F} (hf : FiniteOutcomes J) :
    ImageFinite (model J) := by
  rintro x ⟨side, a⟩
  cases side with
  | left => exact hf a x
  | right => exact hf x a

theorem bisimulation_iff_compatible (J : Join F) (R : F → F → Prop) :
    Bisimulation (model J) (model J) R ↔ ExplanatoryJoiningContexts.Compatible J R := by
  constructor
  · intro h x y hr a
    exact ⟨(fun z => h.1.1 x y (.left, a) z hr), (fun z => h.1.2 x y (.left, a) z hr),
      (fun z => h.1.1 x y (.right, a) z hr), (fun z => h.1.2 x y (.right, a) z hr)⟩
  · intro h
    refine ⟨⟨?_, ?_⟩, ?_⟩
    · rintro x y ⟨side, a⟩ z hr hj
      cases side with
      | left => exact (h hr a).1 z hj
      | right => exact (h hr a).2.2.1 z hj
    · rintro x y ⟨side, a⟩ z hr hj
      cases side with
      | left => exact (h hr a).2.1 z hj
      | right => exact (h hr a).2.2.2 z hj
    · intro x y hr o
      exact nomatch o

theorem branch_same_compatible {J : Join F} (hf : FiniteOutcomes J) :
    ExplanatoryJoiningContexts.Compatible J (BranchSame J) :=
  (bisimulation_iff_compatible J _).mp
    (same_is_bisimulation (finite_outcomes_image_finite hf) (finite_outcomes_image_finite hf))

theorem compatible_refines_branch_same {J : Join F} {R : F → F → Prop}
    (h : ExplanatoryJoiningContexts.Compatible J R) {x y : F} (hr : R x y) :
    BranchSame J x y := bisimulation_implies_same ((bisimulation_iff_compatible J R).mpr h) hr

theorem branch_same_iff_compatible_relation {J : Join F} (hf : FiniteOutcomes J) (x y : F) :
    BranchSame J x y ↔ ∃ R, ExplanatoryJoiningContexts.Compatible J R ∧ R x y :=
  ⟨fun h => ⟨BranchSame J, branch_same_compatible hf, h⟩,
    fun ⟨_, h, hr⟩ => compatible_refines_branch_same h hr⟩

/-- A linear context is a restricted branch question with a continuation. -/
def ask : ExplanatoryJoiningContexts.Context F → Question F → Question F
  | .hole, q => q
  | .left a c, q => ask c (.after (.left, a) q)
  | .right c a, q => ask c (.after (.right, a) q)

theorem holds_ask (J : Join F) (c : ExplanatoryJoiningContexts.Context F)
    (x : F) (q : Question F) :
    target J x (ask c q) ↔ ∃ y, ExplanatoryJoiningContexts.Realizes J c x y ∧ target J y q := by
  induction c generalizing q with
  | hole => exact ⟨fun h => ⟨x, rfl, h⟩, fun ⟨y, eq, h⟩ => eq ▸ h⟩
  | left a c ih =>
    constructor
    · intro h
      obtain ⟨m, hm, y, hj, hq⟩ := (ih (.after (.left, a) q)).mp h
      exact ⟨y, ⟨m, hm, hj⟩, hq⟩
    · rintro ⟨y, ⟨m, hm, hj⟩, hq⟩
      exact (ih (.after (.left, a) q)).mpr ⟨m, hm, y, hj, hq⟩
  | right c a ih =>
    constructor
    · intro h
      obtain ⟨m, hm, y, hj, hq⟩ := (ih (.after (.right, a) q)).mp h
      exact ⟨y, ⟨m, hm, hj⟩, hq⟩
    · rintro ⟨y, ⟨m, hm, hj⟩, hq⟩
      exact (ih (.after (.right, a) q)).mpr ⟨m, hm, y, hj, hq⟩

theorem branch_same_refines_context_same {J : Join F} {x y : F} (h : BranchSame J x y) :
    ExplanatoryJoiningContexts.Same J x y := by
  intro c
  have test (z : F) : target J z (ask c .top) ↔ ExplanatoryJoiningContexts.Possible J c z := by
    rw [holds_ask]
    exact ⟨fun ⟨w, hw, _⟩ => ⟨w, hw⟩, fun ⟨w, hw⟩ => ⟨w, hw, True.intro⟩⟩
  exact (test x).symm.trans ((h (ask c .top)).trans (test y))

/-- Replace both inputs; retain a matched possible result, not one fixed result. -/
theorem join_result_matches {J : Join F} (hf : FiniteOutcomes J)
    {a a' b b' z : F} (ha : BranchSame J a a') (hb : BranchSame J b b') (hj : J a b z) :
    ∃ z', J a' b' z' ∧ BranchSame J z z' := by
  obtain ⟨m, hm, hzm⟩ := (branch_same_compatible hf ha b).2.2.1 z hj
  obtain ⟨z', hz', hmz⟩ := (branch_same_compatible hf hb a').1 m hm
  exact ⟨z', hz', same_trans hzm hmz⟩

/-- A code-level outcome lifts from every actual input pair with those codes. -/
theorem operation_lifts {J : Join F} (hf : FiniteOutcomes J)
    {p : Presentation F (Question F) C} (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (x y : F) (c : C) :
    Lift p J (p.encode x) (p.encode y) c ↔ ∃ z, J x y z ∧ p.encode z = c := by
  constructor
  · rintro ⟨a, b, d, ha, hb, hd, hj⟩
    obtain ⟨z, hz, hdz⟩ := join_result_matches hf
      (equal_codes_same_answers hp ha) (equal_codes_same_answers hp hb) hj
    exact ⟨z, hz, (rp z d (same_symm hdz)).trans hd⟩
  · rintro ⟨z, hz, hc⟩
    exact ⟨x, y, z, rfl, rfl, hc, hz⟩

def canonical (J : Join F) : Presentation F (Question F) (Question F → Prop) where
  encode := target J
  read c q := c q

theorem canonical_exact (J : Join F) : Exact (target J) (canonical J) := fun _ _ => Iff.rfl
theorem canonical_reduced (J : Join F) : Reduced (target J) (canonical J) := by
  intro x y h
  funext q
  exact propext (h q)

theorem every_exact_account_has_canonical_factor {J : Join F}
    {p : Presentation F (Question F) C} (hp : Exact (target J) p) :
    (∀ c, Used p c → ∃ d, Used (canonical J) d ∧ Matches p (canonical J) c d ∧
      ∀ e, Matches p (canonical J) c e → e = d) ∧
    (∀ d, Used (canonical J) d → ∃ c, Used p c ∧ Matches p (canonical J) c d) := by
  constructor
  · intro c hc
    obtain ⟨d, hd, hm⟩ := matches_total_on_used p (canonical J) hc
    exact ⟨d, hd, hm, fun e he => matches_functional hp (canonical_reduced J) he hm⟩
  · rintro d ⟨x, hx⟩
    exact ⟨p.encode x, ⟨x, rfl⟩, x, rfl, hx⟩

/-- Generic witness-lifting respects aligned minimal presentations; this part
does not require finite outcomes. No recovery of native output identity. -/
theorem matching_preserves_operation {J : Join F}
    {p : Presentation F (Question F) C} {r : Presentation F (Question F) D}
    (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (hr : Exact (target J) r) (rr : Reduced (target J) r)
    {a b c : C} {a' b' c' : D}
    (ha : Matches p r a a') (hb : Matches p r b b') (hc : Matches p r c c') :
    Lift p J a b c ↔ Lift r J a' b' c' := by
  constructor
  · rintro ⟨x, y, z, hx, hy, hz, hj⟩
    exact ⟨x, y, z, matches_functional hp rr ⟨x, hx, rfl⟩ ha,
      matches_functional hp rr ⟨y, hy, rfl⟩ hb,
      matches_functional hp rr ⟨z, hz, rfl⟩ hc, hj⟩
  · rintro ⟨x, y, z, hx, hy, hz, hj⟩
    exact ⟨x, y, z, matches_inverse_functional hr rp ⟨x, rfl, hx⟩ ha,
      matches_inverse_functional hr rp ⟨y, rfl, hy⟩ hb,
      matches_inverse_functional hr rp ⟨z, rfl, hz⟩ hc, hj⟩

theorem common_multivalued_structure {J : Join F} (hf : FiniteOutcomes J)
    {p : Presentation F (Question F) C} {r : Presentation F (Question F) D}
    (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (hr : Exact (target J) r) (rr : Reduced (target J) r) :
    (∀ x y c, Lift p J (p.encode x) (p.encode y) c ↔ ∃ z, J x y z ∧ p.encode z = c) ∧
    (∀ x y c, Lift r J (r.encode x) (r.encode y) c ↔ ∃ z, J x y z ∧ r.encode z = c) ∧
    (∀ c, Used p c → ∃ d, Matches p r c d ∧ ∀ e, Matches p r c e → e = d) ∧
    (∀ d, Used r d → ∃ c, Matches p r c d ∧ ∀ e, Matches p r e d → e = c) ∧
    (∀ a b c a' b' c', Matches p r a a' → Matches p r b b' → Matches p r c c' →
      (Lift p J a b c ↔ Lift r J a' b' c')) := by
  have h := relative_unique_correspondence hp rp hr rr
  exact ⟨operation_lifts hf hp rp, operation_lifts hf hr rr, h.1, h.2,
    fun _ _ _ _ _ _ ha hb hc => matching_preserves_operation hp rp hr rr ha hb hc⟩

def mapQuestion (f : F → C) : Question F → Question C
  | .top => .top
  | .atom o => nomatch o
  | .neg q => .neg (mapQuestion f q)
  | .conj q r => .conj (mapQuestion f q) (mapQuestion f r)
  | .after a q => .after (a.1, f a.2) (mapQuestion f q)

/-- Partners used in the questions are compressed by the same account.
The common relation supports the translated questions internally. -/
theorem questions_survive_encoding {J : Join F} (hf : FiniteOutcomes J)
    {p : Presentation F (Question F) C} (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (q : Question F) (x : F) :
    target (Lift p J) (p.encode x) (mapQuestion p.encode q) ↔ target J x q := by
  induction q generalizing x with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg q ih => exact not_congr (ih x)
  | conj q r ihq ihr => exact and_congr (ihq x) (ihr x)
  | after a q ih =>
    rcases a with ⟨side, partner⟩
    cases side with
    | left =>
      constructor
      · rintro ⟨c, hc, hq⟩
        obtain ⟨z, hz, rfl⟩ := (operation_lifts hf hp rp partner x c).mp hc
        exact ⟨z, hz, (ih z).mp hq⟩
      · rintro ⟨z, hz, hq⟩
        exact ⟨p.encode z, lift_contains p J hz, (ih z).mpr hq⟩
    | right =>
      constructor
      · rintro ⟨c, hc, hq⟩
        obtain ⟨z, hz, rfl⟩ := (operation_lifts hf hp rp x partner c).mp hc
        exact ⟨z, hz, (ih z).mp hq⟩
      · rintro ⟨z, hz, hq⟩
        exact ⟨p.encode z, lift_contains p J hz, (ih z).mpr hq⟩

inductive Tree (F : Type u) where
  | leaf : F → Tree F
  | join : Tree F → Tree F → Tree F

def Tree.map (f : F → C) : Tree F → Tree C
  | .leaf x => .leaf (f x)
  | .join l r => .join (l.map f) (r.map f)

def Tree.Realizes (J : Join F) : Tree F → F → Prop
  | .leaf x, z => z = x
  | .join l r, z => ∃ x y, l.Realizes J x ∧ r.Realizes J y ∧ J x y z

/-- All leaves are fixed actual fragments. Quotient joins do not invent a
finite joining tree by switching representatives at intermediate positions.
This is a tree-shaped pattern, not shared-resource or cyclic execution. -/
theorem tree_lifts {J : Join F} (hf : FiniteOutcomes J)
    {p : Presentation F (Question F) C} (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (t : Tree F) (c : C) :
    (t.map p.encode).Realizes (Lift p J) c ↔ ∃ z, t.Realizes J z ∧ p.encode z = c := by
  induction t generalizing c with
  | leaf x => exact ⟨fun eq => ⟨x, rfl, eq.symm⟩, fun ⟨z, eq, hc⟩ => hc.symm.trans (congrArg p.encode eq)⟩
  | join l r ihl ihr =>
    constructor
    · rintro ⟨a, b, hl, hr, hj⟩
      obtain ⟨x, hx, rfl⟩ := (ihl a).mp hl
      obtain ⟨y, hy, rfl⟩ := (ihr b).mp hr
      obtain ⟨z, hz, hc⟩ := (operation_lifts hf hp rp x y c).mp hj
      exact ⟨z, ⟨x, y, hx, hy, hz⟩, hc⟩
    · rintro ⟨z, ⟨x, y, hx, hy, hz⟩, hc⟩
      exact ⟨p.encode x, p.encode y, (ihl _).mpr ⟨x, hx, rfl⟩,
        (ihr _).mpr ⟨y, hy, rfl⟩, (operation_lifts hf hp rp x y c).mpr ⟨z, hz, hc⟩⟩

end Generative.ExplanatoryJoiningBranches

#print axioms Generative.ExplanatoryJoiningBranches.finite_outcomes_image_finite
#print axioms Generative.ExplanatoryJoiningBranches.bisimulation_iff_compatible
#print axioms Generative.ExplanatoryJoiningBranches.branch_same_compatible
#print axioms Generative.ExplanatoryJoiningBranches.compatible_refines_branch_same
#print axioms Generative.ExplanatoryJoiningBranches.branch_same_iff_compatible_relation
#print axioms Generative.ExplanatoryJoiningBranches.holds_ask
#print axioms Generative.ExplanatoryJoiningBranches.branch_same_refines_context_same
#print axioms Generative.ExplanatoryJoiningBranches.join_result_matches
#print axioms Generative.ExplanatoryJoiningBranches.operation_lifts
#print axioms Generative.ExplanatoryJoiningBranches.canonical_exact
#print axioms Generative.ExplanatoryJoiningBranches.canonical_reduced
#print axioms Generative.ExplanatoryJoiningBranches.every_exact_account_has_canonical_factor
#print axioms Generative.ExplanatoryJoiningBranches.matching_preserves_operation
#print axioms Generative.ExplanatoryJoiningBranches.common_multivalued_structure
#print axioms Generative.ExplanatoryJoiningBranches.questions_survive_encoding
#print axioms Generative.ExplanatoryJoiningBranches.tree_lifts
