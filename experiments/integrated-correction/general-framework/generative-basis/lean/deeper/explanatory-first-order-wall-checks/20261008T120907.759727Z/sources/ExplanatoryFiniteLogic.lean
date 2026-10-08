import ExplanatoryJointness

/-! All finite first-order questions in a relational signature with identity,
steps and joint triples. This language can quantify over the entire carrier;
its finite syntax is not a fixed bound on observations or quantifier depth. -/
namespace Generative.ExplanatoryFiniteLogic
open ExplanatoryJointness
universe u v

inductive Formula : Nat → Type where
  | top {n} : Formula n
  | equal {n} : Fin n → Fin n → Formula n
  | step {n} : Fin n → Fin n → Formula n
  | joint {n} : Fin n → Fin n → Fin n → Formula n
  | neg {n} : Formula n → Formula n
  | conj {n} : Formula n → Formula n → Formula n
  | ex {n} : Formula (n + 1) → Formula n

def Meaning {X : Type u} (m : Model X Unit Empty) {n : Nat}
    (valuation : Fin n → X) : Formula n → Prop
  | .top => True
  | .equal i j => valuation i = valuation j
  | .step i j => m.process.step (valuation i) () (valuation j)
  | .joint i j k => m.joint (valuation i) (valuation j) (valuation k)
  | .neg f => ¬ Meaning m valuation f
  | .conj f g => Meaning m valuation f ∧ Meaning m valuation g
  | .ex f => ∃ x, Meaning m (Fin.cases x valuation) f

/-- Every distinct pair can follow one another; three positions participate
jointly exactly when all three are distinct. This is one relational world. -/
def completeModel (X : Type u) : Model X Unit Empty where
  process.step x _ y := x ≠ y
  condition _ o := Empty.elim o
  joint x y z := x ≠ y ∧ x ≠ z ∧ y ≠ z

def Fresh (X : Type u) : Prop :=
  ∀ n (v : Fin n → X), ∃ x, ∀ i, x ≠ v i

def Matches {X : Type u} {Y : Type v} {n : Nat}
    (x : Fin n → X) (y : Fin n → Y) : Prop :=
  ∀ i j, x i = x j ↔ y i = y j

theorem matches_symm {X : Type u} {Y : Type v} {n : Nat}
    {x : Fin n → X} {y : Fin n → Y} (h : Matches x y) : Matches y x :=
  fun i j => (h i j).symm

theorem extend_old {X : Type u} {Y : Type v} {n : Nat}
    {x : Fin n → X} {y : Fin n → Y} (h : Matches x y) (i : Fin n) :
    Matches (Fin.cases (x i) x) (Fin.cases (y i) y) := by
  intro a b
  refine Fin.cases ?_ (fun a => ?_) a
  · refine Fin.cases (iff_of_true rfl rfl) (fun b => h i b) b
  · refine Fin.cases (h a i) (fun b => h a b) b

theorem extend_fresh {X : Type u} {Y : Type v} {n : Nat}
    {x : Fin n → X} {y : Fin n → Y} (h : Matches x y)
    {a : X} {b : Y} (ax : ∀ i, a ≠ x i) (by' : ∀ i, b ≠ y i) :
    Matches (Fin.cases a x) (Fin.cases b y) := by
  intro i j
  refine Fin.cases ?_ (fun i => ?_) i
  · refine Fin.cases (iff_of_true rfl rfl) (fun j => ?_) j
    exact ⟨fun bad => False.elim (ax j bad), fun bad => False.elim (by' j bad)⟩
  · refine Fin.cases ?_ (fun j => h i j) j
    exact ⟨fun bad => False.elim (ax i bad.symm), fun bad => False.elim (by' i bad.symm)⟩

theorem match_extends {X : Type u} {Y : Type v} (fresh : Fresh Y) {n : Nat}
    {x : Fin n → X} {y : Fin n → Y} (h : Matches x y) (a : X) :
    ∃ b, Matches (Fin.cases a x) (Fin.cases b y) := by
  classical
  by_cases old : ∃ i, a = x i
  · obtain ⟨i, rfl⟩ := old
    exact ⟨y i, extend_old h i⟩
  · obtain ⟨b, hb⟩ := fresh n y
    exact ⟨b, extend_fresh h (fun i eq => old ⟨i, eq⟩) hb⟩

theorem finite_formula_preserved {X : Type u} {Y : Type v}
    (fx : Fresh X) (fy : Fresh Y) {n : Nat} (f : Formula n) :
    ∀ (x : Fin n → X) (y : Fin n → Y), Matches x y →
      (Meaning (completeModel X) x f ↔ Meaning (completeModel Y) y f) := by
  induction f with
  | top => exact fun _ _ _ => Iff.rfl
  | equal i j => exact fun _ _ h => h i j
  | step i j => exact fun _ _ h => not_congr (h i j)
  | joint i j k =>
    exact fun _ _ h => and_congr (not_congr (h i j))
      (and_congr (not_congr (h i k)) (not_congr (h j k)))
  | neg f ih => exact fun x y h => not_congr (ih x y h)
  | conj f g ihf ihg => exact fun x y h => and_congr (ihf x y h) (ihg x y h)
  | ex f ih =>
    intro x y h
    constructor
    · rintro ⟨a, yes⟩
      obtain ⟨b, ext⟩ := match_extends fy h a
      exact ⟨b, (ih _ _ ext).mp yes⟩
    · rintro ⟨b, yes⟩
      obtain ⟨a, ext⟩ := match_extends fx (matches_symm h) b
      exact ⟨a, (ih _ _ (matches_symm ext)).mpr yes⟩

theorem sentence_agreement {X : Type u} {Y : Type v} (fx : Fresh X) (fy : Fresh Y)
    (f : Formula 0) :
    Meaning (completeModel X) Fin.elim0 f ↔ Meaning (completeModel Y) Fin.elim0 f :=
  finite_formula_preserved fx fy f _ _ (fun i => Fin.elim0 i)

theorem rooted_agreement {X : Type u} {Y : Type v} (fx : Fresh X) (fy : Fresh Y)
    (a : X) (b : Y) (f : Formula 1) :
    Meaning (completeModel X) (fun _ => a) f ↔ Meaning (completeModel Y) (fun _ => b) f :=
  finite_formula_preserved fx fy f _ _ (fun _ _ => iff_of_true rfl rfl)

/-- Encode earlier nested modal joint questions as first-order formulas. -/
def modalAt : Test Unit Empty → {n : Nat} → Fin n → Formula n
  | .top, _, _ => .top
  | .atom o, _, _ => Empty.elim o
  | .neg f, _, i => .neg (modalAt f i)
  | .conj f g, _, i => .conj (modalAt f i) (modalAt g i)
  | .after _ f, _, i => .ex (.conj (.step i.succ 0) (modalAt f 0))
  | .together f g, _, i => .ex (.ex (.conj (.joint i.succ.succ 1 0)
      (.conj (modalAt f 1) (modalAt g 0))))

theorem modal_translation_correct {X : Type u} (m : Model X Unit Empty)
    (f : Test Unit Empty) : ∀ {n : Nat} (i : Fin n) (x : Fin n → X),
    Meaning m x (modalAt f i) ↔ Holds m (x i) f := by
  induction f with
  | top => exact fun _ _ => Iff.rfl
  | atom o => exact Empty.elim o
  | neg f ih => exact fun i x => not_congr (ih i x)
  | conj f g ihf ihg => exact fun i x => and_congr (ihf i x) (ihg i x)
  | after a f ih =>
    intro n i x
    cases a
    change (∃ y, m.process.step (x i) () y ∧ Meaning m (Fin.cases y x) (modalAt f 0)) ↔ _
    exact exists_congr (fun y => and_congr Iff.rfl (ih 0 (Fin.cases y x)))
  | together f g ihf ihg =>
    intro n i x
    change (∃ l r, m.joint (x i) l r ∧
      Meaning m (Fin.cases r (Fin.cases l x)) (modalAt f 1) ∧
      Meaning m (Fin.cases r (Fin.cases l x)) (modalAt g 0)) ↔ _
    exact exists_congr (fun l => exists_congr (fun r => and_congr Iff.rfl
      (and_congr (ihf 1 _) (ihg 0 _))))

theorem earlier_questions_agree {X : Type u} {Y : Type v} (fx : Fresh X) (fy : Fresh Y)
    (a : X) (b : Y) : Same (completeModel X) (completeModel Y) a b := by
  intro f
  exact (modal_translation_correct _ f (0 : Fin 1) (fun _ => a)).symm.trans
    ((rooted_agreement fx fy a b (modalAt f (0 : Fin 1))).trans
      (modal_translation_correct _ f (0 : Fin 1) (fun _ => b)))

theorem every_position_generated (X : Type u) (root s : X) : Reach (completeModel X) root s := by
  classical
  by_cases same : root = s
  · exact same ▸ Reach.root
  · exact Reach.step Reach.root (a := ()) same

theorem joint_pairs_exist {X : Type u} (fresh : Fresh X) (root : X) :
    ∃ l r, (completeModel X).joint root l r := by
  obtain ⟨l, hl⟩ := fresh 1 (fun _ => root)
  obtain ⟨r, hr⟩ := fresh 2 (Fin.cases root (fun _ => l))
  exact ⟨l, r, (hl 0).symm, (hr 0).symm, (hr 1).symm⟩

end Generative.ExplanatoryFiniteLogic

#print axioms Generative.ExplanatoryFiniteLogic.matches_symm
#print axioms Generative.ExplanatoryFiniteLogic.extend_old
#print axioms Generative.ExplanatoryFiniteLogic.extend_fresh
#print axioms Generative.ExplanatoryFiniteLogic.match_extends
#print axioms Generative.ExplanatoryFiniteLogic.finite_formula_preserved
#print axioms Generative.ExplanatoryFiniteLogic.sentence_agreement
#print axioms Generative.ExplanatoryFiniteLogic.rooted_agreement
#print axioms Generative.ExplanatoryFiniteLogic.modal_translation_correct
#print axioms Generative.ExplanatoryFiniteLogic.earlier_questions_agree
#print axioms Generative.ExplanatoryFiniteLogic.every_position_generated
#print axioms Generative.ExplanatoryFiniteLogic.joint_pairs_exist
