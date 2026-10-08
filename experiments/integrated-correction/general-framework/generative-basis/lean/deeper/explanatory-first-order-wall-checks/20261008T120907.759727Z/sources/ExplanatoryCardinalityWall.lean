import ExplanatoryFiniteLogic

/-! An explicit elementary but nonisomorphic pair. The global distinction is
Cantor's diagonal, not inaccessible padding or an arbitrary truth toggle. -/
namespace Generative.ExplanatoryCardinalityWall
open ExplanatoryJointness ExplanatoryFiniteLogic
universe u v

theorem nat_valuation_bound (n : Nat) (x : Fin n → Nat) : ∃ b, ∀ i, x i < b := by
  induction n with
  | zero => exact ⟨0, fun i => Fin.elim0 i⟩
  | succ n ih =>
    obtain ⟨b, hb⟩ := ih (fun i => x i.succ)
    refine ⟨x 0 + b + 1, ?_⟩
    intro i
    refine Fin.cases (by omega) (fun j => ?_) i
    have := hb j
    omega

theorem nat_fresh : Fresh Nat := by
  intro n x
  obtain ⟨b, hb⟩ := nat_valuation_bound n x
  exact ⟨b, fun i eq => (Nat.ne_of_lt (hb i)) eq.symm⟩

abbrev Streams := Nat → Bool

theorem streams_fresh : Fresh Streams := by
  intro n x
  let d : Streams := fun k => if h : k < n then !(x ⟨k, h⟩ k) else false
  refine ⟨d, ?_⟩
  intro i eq
  have bad := congrArg (fun s : Streams => s i.val) eq
  simp only [d, dif_pos i.isLt] at bad
  cases h : x i i.val <;> simp [h] at bad

def Enumerable (X : Type u) : Prop := ∃ f : Nat → X, ∀ x, ∃ n, f n = x

def diagonal (f : Nat → Streams) : Streams := fun n => !(f n n)

theorem diagonal_missing (f : Nat → Streams) (n : Nat) : f n ≠ diagonal f := by
  intro eq
  have bad := congrArg (fun s : Streams => s n) eq
  change f n n = !(f n n) at bad
  cases h : f n n <;> simp [h] at bad

theorem nat_enumerable : Enumerable Nat := ⟨id, fun n => ⟨n, rfl⟩⟩

theorem streams_not_enumerable : ¬ Enumerable Streams := by
  rintro ⟨f, onto⟩
  obtain ⟨n, eq⟩ := onto (diagonal f)
  exact diagonal_missing f n eq

def Elementary {X : Type u} {Y : Type v} (m : Model X Unit Empty)
    (q : Model Y Unit Empty) (f : X → Y) : Prop :=
  ∀ n (formula : Formula n) (x : Fin n → X),
    Meaning m x formula ↔ Meaning q (fun i => f (x i)) formula

structure Isomorphism {X : Type u} {Y : Type v} (m : Model X Unit Empty)
    (q : Model Y Unit Empty) (f : X → Y) : Prop where
  injective : ∀ {x y}, f x = f y → x = y
  onto : ∀ y, ∃ x, f x = y
  steps : ∀ x y, m.process.step x () y ↔ q.process.step (f x) () (f y)
  joints : ∀ x y z, m.joint x y z ↔ q.joint (f x) (f y) (f z)

theorem elementary_injective {X : Type u} {Y : Type v}
    {m : Model X Unit Empty} {q : Model Y Unit Empty} {f : X → Y}
    (h : Elementary m q f) {x y : X} (eq : f x = f y) : x = y := by
  let valuation : Fin 2 → X := Fin.cases x (fun _ => y)
  exact (h 2 (.equal 0 1) valuation).mpr eq

theorem elementary_steps {X : Type u} {Y : Type v}
    {m : Model X Unit Empty} {q : Model Y Unit Empty} {f : X → Y}
    (h : Elementary m q f) (x y : X) :
    m.process.step x () y ↔ q.process.step (f x) () (f y) := by
  let valuation : Fin 2 → X := Fin.cases x (fun _ => y)
  exact h 2 (.step 0 1) valuation

theorem elementary_joints {X : Type u} {Y : Type v}
    {m : Model X Unit Empty} {q : Model Y Unit Empty} {f : X → Y}
    (h : Elementary m q f) (x y z : X) :
    m.joint x y z ↔ q.joint (f x) (f y) (f z) := by
  let valuation : Fin 3 → X := Fin.cases x (Fin.cases y (fun _ => z))
  exact h 3 (.joint 0 1 2) valuation

theorem elementary_onto_isomorphism {X : Type u} {Y : Type v}
    {m : Model X Unit Empty} {q : Model Y Unit Empty} {f : X → Y}
    (h : Elementary m q f) (onto : ∀ y, ∃ x, f x = y) : Isomorphism m q f :=
  ⟨elementary_injective h, onto, elementary_steps h, elementary_joints h⟩

theorem elementary_isomorphism_iff_onto {X : Type u} {Y : Type v}
    {m : Model X Unit Empty} {q : Model Y Unit Empty} {f : X → Y}
    (h : Elementary m q f) : Isomorphism m q f ↔ (∀ y, ∃ x, f x = y) :=
  ⟨fun iso => iso.onto, elementary_onto_isomorphism h⟩

def oneHot (n : Nat) : Streams := fun k => decide (k = n)

theorem oneHot_injective {n m : Nat} (eq : oneHot n = oneHot m) : n = m := by
  have atn := congrArg (fun s : Streams => s n) eq
  simpa [oneHot] using atn

theorem injection_elementary {X : Type u} {Y : Type v} (fx : Fresh X) (fy : Fresh Y)
    (f : X → Y) (injective : ∀ {x y}, f x = f y → x = y) :
    Elementary (completeModel X) (completeModel Y) f := by
  intro n formula x
  exact finite_formula_preserved fx fy formula x (fun i => f (x i))
    (fun _ _ => ⟨congrArg f, injective⟩)

theorem oneHot_elementary : Elementary (completeModel Nat) (completeModel Streams) oneHot :=
  injection_elementary nat_fresh streams_fresh oneHot oneHot_injective

theorem no_map_onto (f : Nat → Streams) : ¬ (∀ y, ∃ x, f x = y) :=
  fun onto => streams_not_enumerable ⟨f, onto⟩

theorem no_isomorphism : ¬ ∃ f : Nat → Streams,
    Isomorphism (completeModel Nat) (completeModel Streams) f := by
  rintro ⟨f, iso⟩
  exact no_map_onto f iso.onto

theorem all_sentences_agree (formula : Formula 0) :
    Meaning (completeModel Nat) Fin.elim0 formula ↔
    Meaning (completeModel Streams) Fin.elim0 formula :=
  sentence_agreement nat_fresh streams_fresh formula

theorem all_rooted_questions_agree (formula : Formula 1) :
    Meaning (completeModel Nat) (fun _ => 0) formula ↔
    Meaning (completeModel Streams) (fun _ => oneHot 0) formula :=
  rooted_agreement nat_fresh streams_fresh 0 (oneHot 0) formula

/-- Naming a partner separates actual distinct positions; the witness does not
arise by erasing identity from the observation language. -/
theorem partner_separates {X : Type u} (m : Model X Unit Empty) {x y : X} (ne : x ≠ y) :
    Meaning m (Fin.cases x (fun _ : Fin 1 => x)) (.equal 0 1) ∧
    ¬ Meaning m (Fin.cases y (fun _ : Fin 1 => x)) (.equal 0 1) :=
  ⟨rfl, fun eq => ne eq.symm⟩

theorem no_sentence_defines_enumerability : ¬ ∃ formula : Formula 0,
    (Meaning (completeModel Nat) Fin.elim0 formula ↔ Enumerable Nat) ∧
    (Meaning (completeModel Streams) Fin.elim0 formula ↔ Enumerable Streams) := by
  rintro ⟨formula, hn, hs⟩
  exact streams_not_enumerable (hs.mp ((all_sentences_agree formula).mp
    (hn.mpr nat_enumerable)))

theorem coherent_truth_without_coverage :
    Elementary (completeModel Nat) (completeModel Streams) oneHot ∧
    ¬ (∀ y, ∃ x, oneHot x = y) :=
  ⟨oneHot_elementary, no_map_onto oneHot⟩

theorem generated_joint_worlds_without_isomorphism :
    (∀ n, Reach (completeModel Nat) 0 n) ∧
    (∀ s, Reach (completeModel Streams) (oneHot 0) s) ∧
    (∃ l r, (completeModel Nat).joint 0 l r) ∧
    (∃ l r, (completeModel Streams).joint (oneHot 0) l r) ∧
    (∀ formula : Formula 1,
      Meaning (completeModel Nat) (fun _ => 0) formula ↔
      Meaning (completeModel Streams) (fun _ => oneHot 0) formula) ∧
    ¬ ∃ f : Nat → Streams, Isomorphism (completeModel Nat) (completeModel Streams) f :=
  ⟨every_position_generated Nat 0, every_position_generated Streams (oneHot 0),
    joint_pairs_exist nat_fresh 0, joint_pairs_exist streams_fresh (oneHot 0),
    all_rooted_questions_agree, no_isomorphism⟩

end Generative.ExplanatoryCardinalityWall

#print axioms Generative.ExplanatoryCardinalityWall.nat_valuation_bound
#print axioms Generative.ExplanatoryCardinalityWall.nat_fresh
#print axioms Generative.ExplanatoryCardinalityWall.streams_fresh
#print axioms Generative.ExplanatoryCardinalityWall.diagonal_missing
#print axioms Generative.ExplanatoryCardinalityWall.nat_enumerable
#print axioms Generative.ExplanatoryCardinalityWall.streams_not_enumerable
#print axioms Generative.ExplanatoryCardinalityWall.elementary_injective
#print axioms Generative.ExplanatoryCardinalityWall.elementary_steps
#print axioms Generative.ExplanatoryCardinalityWall.elementary_joints
#print axioms Generative.ExplanatoryCardinalityWall.elementary_onto_isomorphism
#print axioms Generative.ExplanatoryCardinalityWall.elementary_isomorphism_iff_onto
#print axioms Generative.ExplanatoryCardinalityWall.oneHot_injective
#print axioms Generative.ExplanatoryCardinalityWall.injection_elementary
#print axioms Generative.ExplanatoryCardinalityWall.oneHot_elementary
#print axioms Generative.ExplanatoryCardinalityWall.no_map_onto
#print axioms Generative.ExplanatoryCardinalityWall.no_isomorphism
#print axioms Generative.ExplanatoryCardinalityWall.all_sentences_agree
#print axioms Generative.ExplanatoryCardinalityWall.all_rooted_questions_agree
#print axioms Generative.ExplanatoryCardinalityWall.partner_separates
#print axioms Generative.ExplanatoryCardinalityWall.no_sentence_defines_enumerability
#print axioms Generative.ExplanatoryCardinalityWall.coherent_truth_without_coverage
#print axioms Generative.ExplanatoryCardinalityWall.generated_joint_worlds_without_isomorphism
