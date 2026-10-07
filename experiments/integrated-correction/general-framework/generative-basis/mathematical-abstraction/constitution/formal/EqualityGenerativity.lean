import Std

/-!
Pure equality is a deliberately narrow successful witness-generation case.
The only atomic formulas compare variables. Quantifiers have arbitrary depth.
Freshness for finite tuples suffices for full formula transport; the witness
construction does not inspect the formula's semantic truth. No arithmetic
symbol, higher-order quantifier, or metaphysical grounding is represented.
-/
namespace EqualityGenerativity

inductive Formula : Nat → Type where
  | eq {n : Nat} : Fin n → Fin n → Formula n
  | neg {n : Nat} : Formula n → Formula n
  | conj {n : Nat} : Formula n → Formula n → Formula n
  | ex {n : Nat} : Formula (n + 1) → Formula n

def extend {A : Type u} {n : Nat} (a : A) (v : Fin n → A) : Fin (n + 1) → A :=
  Fin.cases a v

def Holds {A : Type u} {n : Nat} : Formula n → (Fin n → A) → Prop
  | .eq i j, v => v i = v j
  | .neg p, v => ¬ Holds p v
  | .conj p q, v => Holds p v ∧ Holds q v
  | .ex p, v => ∃ a, Holds p (extend a v)

def SamePattern {A : Type u} {B : Type v} {n : Nat}
    (a : Fin n → A) (b : Fin n → B) : Prop :=
  ∀ i j, a i = a j ↔ b i = b j

def Fresh {A : Type u} (a : A) {n : Nat} (v : Fin n → A) : Prop :=
  ∀ i, a ≠ v i

def HasFresh (A : Type u) : Prop :=
  ∀ (n : Nat) (v : Fin n → A), ∃ a, Fresh a v

theorem pattern_symm {A : Type u} {B : Type v} {n : Nat}
    {a : Fin n → A} {b : Fin n → B} (h : SamePattern a b) : SamePattern b a :=
  fun i j => (h i j).symm

theorem pattern_extend {A : Type u} {B : Type v} {n : Nat}
    {a : Fin n → A} {b : Fin n → B} {x : A} {y : B}
    (h : SamePattern a b) (hx : ∀ i, x = a i ↔ y = b i) :
    SamePattern (extend x a) (extend y b) := by
  intro i j
  refine Fin.cases ?_ (fun i => ?_) i
  · refine Fin.cases ?_ (fun j => ?_) j
    · simp [extend]
    · simpa [extend] using hx j
  · refine Fin.cases ?_ (fun j => ?_) j
    · simpa [extend, eq_comm] using hx i
    · simpa [extend] using h i j

theorem extend_pattern {A : Type u} {B : Type v} {n : Nat}
    {a : Fin n → A} {b : Fin n → B} (h : SamePattern a b)
    (fresh : HasFresh B) (x : A) :
    ∃ y, SamePattern (extend x a) (extend y b) := by
  classical
  by_cases hx : ∃ i, x = a i
  · obtain ⟨i, rfl⟩ := hx
    exact ⟨b i, pattern_extend h (fun j => h i j)⟩
  · obtain ⟨y, hy⟩ := fresh n b
    refine ⟨y, pattern_extend h (fun i => ?_)⟩
    constructor
    · intro hi
      exact False.elim (hx ⟨i, hi⟩)
    · intro hi
      exact False.elim (hy i hi)

theorem truth_of_pattern {A : Type u} {B : Type v}
    (fa : HasFresh A) (fb : HasFresh B) {n : Nat} (p : Formula n)
    (a : Fin n → A) (b : Fin n → B) (h : SamePattern a b) :
    Holds p a ↔ Holds p b := by
  induction p with
  | eq i j => exact h i j
  | neg p ih => exact not_congr (ih a b h)
  | conj p q ihp ihq => exact and_congr (ihp a b h) (ihq a b h)
  | ex p ih =>
    constructor
    · rintro ⟨x, hx⟩
      obtain ⟨y, hy⟩ := extend_pattern h fb x
      exact ⟨y, (ih _ _ hy).mp hx⟩
    · rintro ⟨y, hy⟩
      obtain ⟨x, hx⟩ := extend_pattern (pattern_symm h) fa y
      exact ⟨x, (ih _ _ (pattern_symm hx)).mpr hy⟩

def noVars (A : Type u) : Fin 0 → A := fun i => Fin.elim0 i

theorem sentence_agreement {A : Type u} {B : Type v}
    (fa : HasFresh A) (fb : HasFresh B) (p : Formula 0) :
    Holds p (noVars A) ↔ Holds p (noVars B) :=
  truth_of_pattern fa fb p _ _ (fun i => Fin.elim0 i)

def upper : (n : Nat) → (Fin n → Nat) → Nat
  | 0, _ => 0
  | n + 1, v => Nat.max (v 0) (upper n (fun i => v i.succ))

theorem le_upper (n : Nat) (v : Fin n → Nat) (i : Fin n) : v i ≤ upper n v := by
  induction n with
  | zero => exact Fin.elim0 i
  | succ n ih =>
    refine Fin.cases ?_ (fun j => ?_) i
    · exact Nat.le_max_left _ _
    · exact Nat.le_trans (ih (fun k => v k.succ) j) (Nat.le_max_right _ _)

theorem upper_succ_fresh (n : Nat) (v : Fin n → Nat) : Fresh (upper n v + 1) v := by
  intro i hi
  have h := le_upper n v i
  omega

theorem nat_hasFresh : HasFresh Nat :=
  fun n v => ⟨upper n v + 1, upper_succ_fresh n v⟩

theorem finite_witness_reduction {n : Nat} (p : Formula (n + 1))
    (v : Fin n → Nat) :
    Holds (.ex p) v ↔
      (∃ i, Holds p (extend (v i) v)) ∨ Holds p (extend (upper n v + 1) v) := by
  classical
  constructor
  · rintro ⟨x, hx⟩
    by_cases h : ∃ i, x = v i
    · obtain ⟨i, rfl⟩ := h
      exact Or.inl ⟨i, hx⟩
    · right
      have same : SamePattern (extend x v) (extend (upper n v + 1) v) := by
        apply pattern_extend (fun _ _ => Iff.rfl)
        intro i
        constructor
        · intro hi
          exact False.elim (h ⟨i, hi⟩)
        · intro hi
          exact False.elim (upper_succ_fresh n v i hi)
      exact (truth_of_pattern nat_hasFresh nat_hasFresh p _ _ same).mp hx
  · intro h
    rcases h with ⟨i, hi⟩ | hf
    · exact ⟨v i, hi⟩
    · exact ⟨upper n v + 1, hf⟩

def evaluate {n : Nat} : Formula n → (Fin n → Nat) → Bool
  | .eq i j, v => decide (v i = v j)
  | .neg p, v => !(evaluate p v)
  | .conj p q, v => evaluate p v && evaluate q v
  | .ex p, v =>
      decide (∃ i, evaluate p (extend (v i) v) = true) ||
        evaluate p (extend (upper _ v + 1) v)

theorem evaluate_correct {n : Nat} (p : Formula n) (v : Fin n → Nat) :
    evaluate p v = true ↔ Holds p v := by
  induction p with
  | eq i j => simp [evaluate, Holds]
  | neg p ih =>
    change ((!(evaluate p v)) = true) ↔ ¬ Holds p v
    rw [← ih v]
    cases evaluate p v <;> decide
  | conj p q ihp ihq =>
    simp only [evaluate, Bool.and_eq_true, Holds]
    exact and_congr (ihp v) (ihq v)
  | ex p ih =>
    rw [finite_witness_reduction]
    simp only [evaluate, Bool.or_eq_true, decide_eq_true_eq]
    exact or_congr (exists_congr (fun i => ih _)) (ih _)

theorem sentence_evaluation {A : Type u} (fresh : HasFresh A) (p : Formula 0) :
    evaluate p (noVars Nat) = true ↔ Holds p (noVars A) :=
  (evaluate_correct p _).trans (sentence_agreement nat_hasFresh fresh p)

def double (n : Nat) : Nat := 2 * n

theorem double_injective : Function.Injective double := by
  intro a b h
  unfold double at h
  omega

theorem double_not_surjective : ¬ Function.Surjective double := by
  intro h
  obtain ⟨n, hn⟩ := h 1
  unfold double at hn
  omega

theorem injective_preserves_equality_formulas {A : Type u} {B : Type v}
    (fa : HasFresh A) (fb : HasFresh B) (f : A → B) (hf : Function.Injective f)
    {n : Nat} (p : Formula n) (a : Fin n → A) :
    Holds p a ↔ Holds p (fun i => f (a i)) := by
  apply truth_of_pattern fa fb
  intro i j
  exact ⟨congrArg f, fun h => hf h⟩

theorem double_preserves_all_equality_formulas {n : Nat}
    (p : Formula n) (a : Fin n → Nat) :
    Holds p a ↔ Holds p (fun i => double (a i)) :=
  injective_preserves_equality_formulas nat_hasFresh nat_hasFresh double double_injective p a

/- A finite generation view of the same domain uses zero and successor as
construction rules. They are not symbols of the interpreted equality language. -/
inductive GeneratedNat : Nat → Prop where
  | zero : GeneratedNat 0
  | succ {n : Nat} : GeneratedNat n → GeneratedNat (n + 1)

theorem every_nat_generated (n : Nat) : GeneratedNat n := by
  induction n with
  | zero => exact .zero
  | succ n ih => exact .succ ih

theorem generated_nat_least (P : Nat → Prop) (h0 : P 0)
    (hs : ∀ n, P n → P (n + 1)) {n : Nat} (h : GeneratedNat n) : P n := by
  induction h with
  | zero => exact h0
  | @succ n h ih => exact hs n ih

end EqualityGenerativity
