import Std

/-!
All formulas of the pure equality/order language are determined by finite
order patterns in dense linear orders without endpoints. Witness generation
uses the stated before, after and between operations, never semantic answers.
The order laws, available operations and Lean metatheory are explicit inputs.
-/
namespace OrderGenerativity

structure DenseOrder (A : Type u) where
  lt : A → A → Prop
  irrefl : ∀ a, ¬ lt a a
  trans : ∀ {a b c}, lt a b → lt b c → lt a c
  tri : ∀ a b, lt a b ∨ a = b ∨ lt b a
  seed : A
  before : A → A
  after : A → A
  between : A → A → A
  before_lt : ∀ a, lt (before a) a
  lt_after : ∀ a, lt a (after a)
  between_lt : ∀ {a b}, lt a b → lt a (between a b) ∧ lt (between a b) b

def LE (O : DenseOrder A) (a b : A) : Prop := O.lt a b ∨ a = b

theorem lt_asymm (O : DenseOrder A) {a b : A} (h : O.lt a b) : ¬ O.lt b a :=
  fun h' => O.irrefl a (O.trans h h')

theorem le_refl (O : DenseOrder A) (a : A) : LE O a a := Or.inr rfl

theorem le_trans (O : DenseOrder A) {a b c : A} (h : LE O a b) (k : LE O b c) :
    LE O a c := by
  rcases h with h | rfl
  · rcases k with k | rfl
    · exact Or.inl (O.trans h k)
    · exact Or.inl h
  · exact k

theorem lt_of_le_lt (O : DenseOrder A) {a b c : A} (h : LE O a b) (k : O.lt b c) :
    O.lt a c := by
  rcases h with h | rfl
  · exact O.trans h k
  · exact k

theorem lt_of_lt_le (O : DenseOrder A) {a b c : A} (h : O.lt a b) (k : LE O b c) :
    O.lt a c := by
  rcases k with k | rfl
  · exact O.trans h k
  · exact h

theorem finite_max (O : DenseOrder A) (n : Nat) (v : Fin n → A) (P : Fin n → Prop)
    (h : ∃ i, P i) : ∃ i, P i ∧ ∀ j, P j → LE O (v j) (v i) := by
  classical
  induction n with
  | zero => obtain ⟨i, _⟩ := h; exact Fin.elim0 i
  | succ n ih =>
    by_cases ht : ∃ i : Fin n, P i.succ
    · obtain ⟨i, hi, hm⟩ := ih (fun i => v i.succ) (fun i => P i.succ) ht
      by_cases hz : P 0
      · rcases O.tri (v 0) (v i.succ) with hl | he | hr
        · refine ⟨i.succ, hi, ?_⟩
          intro j
          refine Fin.cases ?_ (fun j => ?_) j
          · exact fun _ => Or.inl hl
          · exact hm j
        · refine ⟨i.succ, hi, ?_⟩
          intro j
          refine Fin.cases ?_ (fun j => ?_) j
          · exact fun _ => Or.inr he
          · exact hm j
        · refine ⟨0, hz, ?_⟩
          intro j
          refine Fin.cases ?_ (fun j => ?_) j
          · exact fun _ => le_refl O _
          · exact fun hj => le_trans O (hm j hj) (Or.inl hr)
      · refine ⟨i.succ, hi, ?_⟩
        intro j
        refine Fin.cases ?_ (fun j => ?_) j
        · exact fun h => False.elim (hz h)
        · exact hm j
    · have hz : P 0 := by
        obtain ⟨i, hi⟩ := h
        cases i using Fin.cases with
        | zero => exact hi
        | succ i => exact False.elim (ht ⟨i, hi⟩)
      refine ⟨0, hz, ?_⟩
      intro j
      refine Fin.cases ?_ (fun j => ?_) j
      · exact fun _ => le_refl O _
      · exact fun hj => False.elim (ht ⟨j, hj⟩)

def reverse (O : DenseOrder A) : DenseOrder A where
  lt a b := O.lt b a
  irrefl := O.irrefl
  trans h k := O.trans k h
  tri a b := O.tri b a |>.imp_right (fun h => h.imp_left Eq.symm)
  seed := O.seed
  before := O.after
  after := O.before
  between a b := O.between b a
  before_lt := O.lt_after
  lt_after := O.before_lt
  between_lt h := ⟨(O.between_lt h).2, (O.between_lt h).1⟩

theorem finite_min (O : DenseOrder A) (n : Nat) (v : Fin n → A) (P : Fin n → Prop)
    (h : ∃ i, P i) : ∃ i, P i ∧ ∀ j, P j → LE O (v i) (v j) := by
  obtain ⟨i, hi, hm⟩ := finite_max (reverse O) n v P h
  refine ⟨i, hi, fun j hj => ?_⟩
  rcases hm j hj with h | h
  · exact Or.inl h
  · exact Or.inr h.symm

def extend (x : A) (a : Fin n → A) : Fin (n+1) → A := Fin.cases x a

def SamePattern (O : DenseOrder A) (P : DenseOrder B)
    (a : Fin n → A) (b : Fin n → B) : Prop :=
  (∀ i j, a i = a j ↔ b i = b j) ∧ (∀ i j, O.lt (a i) (a j) ↔ P.lt (b i) (b j))

theorem pattern_symm (O : DenseOrder A) (P : DenseOrder B)
    {a : Fin n → A} {b : Fin n → B} (h : SamePattern O P a b) : SamePattern P O b a :=
  ⟨fun i j => (h.1 i j).symm, fun i j => (h.2 i j).symm⟩

theorem pattern_extend (O : DenseOrder A) (P : DenseOrder B)
    {a : Fin n → A} {b : Fin n → B} {x : A} {y : B} (h : SamePattern O P a b)
    (he : ∀ i, x = a i ↔ y = b i)
    (hl : ∀ i, O.lt x (a i) ↔ P.lt y (b i))
    (hr : ∀ i, O.lt (a i) x ↔ P.lt (b i) y) :
    SamePattern O P (extend x a) (extend y b) := by
  constructor
  · intro i j
    refine Fin.cases ?_ (fun i => ?_) i
    · refine Fin.cases ?_ (fun j => ?_) j
      · simp [extend]
      · simpa [extend] using he j
    · refine Fin.cases ?_ (fun j => ?_) j
      · simpa [extend, eq_comm] using he i
      · simpa [extend] using h.1 i j
  · intro i j
    refine Fin.cases ?_ (fun i => ?_) i
    · refine Fin.cases ?_ (fun j => ?_) j
      · exact iff_of_false (O.irrefl x) (P.irrefl y)
      · simpa [extend] using hl j
    · refine Fin.cases ?_ (fun j => ?_) j
      · simpa [extend] using hr i
      · simpa [extend] using h.2 i j

inductive WitnessCase (n : Nat) where
  | seed
  | existing : Fin n → WitnessCase n
  | before : Fin n → WitnessCase n
  | after : Fin n → WitnessCase n
  | between : Fin n → Fin n → WitnessCase n

def candidate (P : DenseOrder B) (b : Fin n → B) : WitnessCase n → B
  | .seed => P.seed
  | .existing i => b i
  | .before i => P.before (b i)
  | .after i => P.after (b i)
  | .between i j => P.between (b i) (b j)

/-- Finite order cuts are realized using only the displayed construction rules. -/
theorem cut_realized (O : DenseOrder A) (P : DenseOrder B)
    (a : Fin n → A) (b : Fin n → B) (h : SamePattern O P a b) (x : A) :
    ∃ c : WitnessCase n,
      (∀ i, O.lt (a i) x → P.lt (b i) (candidate P b c)) ∧
      (∀ i, O.lt x (a i) → P.lt (candidate P b c) (b i)) := by
  classical
  by_cases hlo : ∃ i, O.lt (a i) x
  · obtain ⟨l, hl, hmax⟩ := finite_max O n a (fun i => O.lt (a i) x) hlo
    by_cases hhi : ∃ i, O.lt x (a i)
    · obtain ⟨r, hr, hmin⟩ := finite_min O n a (fun i => O.lt x (a i)) hhi
      have hlr := (h.2 l r).mp (O.trans hl hr)
      refine ⟨.between l r, ?_, ?_⟩
      · intro i hi
        apply lt_of_le_lt P _ (P.between_lt hlr).1
        rcases hmax i hi with hlt | heq
        · exact Or.inl ((h.2 i l).mp hlt)
        · exact Or.inr ((h.1 i l).mp heq)
      · intro i hi
        apply lt_of_lt_le P (P.between_lt hlr).2
        rcases hmin i hi with hlt | heq
        · exact Or.inl ((h.2 r i).mp hlt)
        · exact Or.inr ((h.1 r i).mp heq)
    · refine ⟨.after l, ?_, ?_⟩
      · intro i hi
        apply lt_of_le_lt P _ (P.lt_after (b l))
        rcases hmax i hi with hlt | heq
        · exact Or.inl ((h.2 i l).mp hlt)
        · exact Or.inr ((h.1 i l).mp heq)
      · exact fun i hi => False.elim (hhi ⟨i, hi⟩)
  · by_cases hhi : ∃ i, O.lt x (a i)
    · obtain ⟨r, hr, hmin⟩ := finite_min O n a (fun i => O.lt x (a i)) hhi
      refine ⟨.before r, ?_, ?_⟩
      · exact fun i hi => False.elim (hlo ⟨i, hi⟩)
      · intro i hi
        apply lt_of_lt_le P (P.before_lt (b r))
        rcases hmin i hi with hlt | heq
        · exact Or.inl ((h.2 r i).mp hlt)
        · exact Or.inr ((h.1 r i).mp heq)
    · exact ⟨.seed, fun i hi => False.elim (hlo ⟨i, hi⟩),
        fun i hi => False.elim (hhi ⟨i, hi⟩)⟩

theorem pattern_of_cut (O : DenseOrder A) (P : DenseOrder B)
    {a : Fin n → A} {b : Fin n → B} (h : SamePattern O P a b) (x : A) (y : B)
    (hne : ∀ i, x ≠ a i)
    (lo : ∀ i, O.lt (a i) x → P.lt (b i) y)
    (hi : ∀ i, O.lt x (a i) → P.lt y (b i)) :
    SamePattern O P (extend x a) (extend y b) := by
  apply pattern_extend O P h
  · intro i
    constructor
    · exact fun he => False.elim (hne i he)
    · intro he
      rcases O.tri x (a i) with hl | heq | hr
      · have hy := hi i hl
        rw [he] at hy
        exact False.elim (P.irrefl _ hy)
      · exact False.elim (hne i heq)
      · have hy := lo i hr
        rw [he] at hy
        exact False.elim (P.irrefl _ hy)
  · intro i
    constructor
    · exact hi i
    · intro hy
      rcases O.tri x (a i) with hl | heq | hr
      · exact hl
      · exact False.elim (hne i heq)
      · exact False.elim (lt_asymm P hy (lo i hr))
  · intro i
    constructor
    · exact lo i
    · intro hy
      rcases O.tri x (a i) with hl | heq | hr
      · exact False.elim (lt_asymm P hy (hi i hl))
      · exact False.elim (hne i heq)
      · exact hr

theorem extend_pattern (O : DenseOrder A) (P : DenseOrder B)
    {a : Fin n → A} {b : Fin n → B} (h : SamePattern O P a b) (x : A) :
    ∃ c : WitnessCase n, SamePattern O P (extend x a) (extend (candidate P b c) b) := by
  classical
  by_cases he : ∃ i, x = a i
  · obtain ⟨i, rfl⟩ := he
    exact ⟨.existing i, pattern_extend O P h (h.1 i) (h.2 i) (fun j => h.2 j i)⟩
  · obtain ⟨c, hlo, hhi⟩ := cut_realized O P a b h x
    exact ⟨c, pattern_of_cut O P h x _ (fun i hi => he ⟨i, hi⟩) hlo hhi⟩

inductive Formula : Nat → Type where
  | eq {n} : Fin n → Fin n → Formula n
  | lt {n} : Fin n → Fin n → Formula n
  | neg {n} : Formula n → Formula n
  | conj {n} : Formula n → Formula n → Formula n
  | ex {n} : Formula (n+1) → Formula n

def Holds (O : DenseOrder A) : Formula n → (Fin n → A) → Prop
  | .eq i j, a => a i = a j
  | .lt i j, a => O.lt (a i) (a j)
  | .neg p, a => ¬ Holds O p a
  | .conj p q, a => Holds O p a ∧ Holds O q a
  | .ex p, a => ∃ x, Holds O p (extend x a)

theorem truth_of_pattern (O : DenseOrder A) (P : DenseOrder B) (p : Formula n)
    (a : Fin n → A) (b : Fin n → B) (h : SamePattern O P a b) :
    Holds O p a ↔ Holds P p b := by
  induction p with
  | eq i j => exact h.1 i j
  | lt i j => exact h.2 i j
  | neg p ih => exact not_congr (ih a b h)
  | conj p q ihp ihq => exact and_congr (ihp a b h) (ihq a b h)
  | ex p ih =>
    constructor
    · rintro ⟨x, hx⟩
      obtain ⟨c, hc⟩ := extend_pattern O P h x
      exact ⟨candidate P b c, (ih _ _ hc).mp hx⟩
    · rintro ⟨y, hy⟩
      obtain ⟨c, hc⟩ := extend_pattern P O (pattern_symm O P h) y
      exact ⟨candidate O a c, (ih _ _ (pattern_symm P O hc)).mpr hy⟩

def noVars (A : Type u) : Fin 0 → A := fun i => Fin.elim0 i

theorem sentence_agreement (O : DenseOrder A) (P : DenseOrder B) (p : Formula 0) :
    Holds O p (noVars A) ↔ Holds P p (noVars B) :=
  truth_of_pattern O P p _ _ ⟨fun i => Fin.elim0 i, fun i => Fin.elim0 i⟩

theorem finite_witness_reduction (O : DenseOrder A) (p : Formula (n+1))
    (a : Fin n → A) :
    Holds O (.ex p) a ↔ ∃ c : WitnessCase n, Holds O p (extend (candidate O a c) a) := by
  constructor
  · rintro ⟨x, hx⟩
    obtain ⟨c, hc⟩ := extend_pattern O O ⟨fun _ _ => Iff.rfl, fun _ _ => Iff.rfl⟩ x
    exact ⟨c, (truth_of_pattern O O p _ _ hc).mp hx⟩
  · rintro ⟨c, hc⟩
    exact ⟨candidate O a c, hc⟩

theorem exists_witness_case (Q : WitnessCase n → Prop) :
    (∃ c, Q c) ↔ Q .seed ∨ (∃ i, Q (.existing i)) ∨ (∃ i, Q (.before i)) ∨
      (∃ i, Q (.after i)) ∨ (∃ i j, Q (.between i j)) := by
  constructor
  · rintro ⟨c, hc⟩
    cases c with
    | seed => exact Or.inl hc
    | existing i => exact Or.inr (Or.inl ⟨i, hc⟩)
    | before i => exact Or.inr (Or.inr (Or.inl ⟨i, hc⟩))
    | after i => exact Or.inr (Or.inr (Or.inr (Or.inl ⟨i, hc⟩)))
    | between i j => exact Or.inr (Or.inr (Or.inr (Or.inr ⟨i, j, hc⟩)))
  · intro h
    rcases h with h | ⟨i, h⟩ | ⟨i, h⟩ | ⟨i, h⟩ | ⟨i, j, h⟩
    · exact ⟨.seed, h⟩
    · exact ⟨.existing i, h⟩
    · exact ⟨.before i, h⟩
    · exact ⟨.after i, h⟩
    · exact ⟨.between i j, h⟩

def anyWitness (f : WitnessCase n → Bool) : Bool :=
  f .seed || (decide (∃ i, f (.existing i) = true) ||
    (decide (∃ i, f (.before i) = true) ||
      (decide (∃ i, f (.after i) = true) || decide (∃ i j, f (.between i j) = true))))

theorem anyWitness_correct (f : WitnessCase n → Bool) :
    anyWitness f = true ↔ ∃ c, f c = true := by
  simp only [anyWitness, Bool.or_eq_true, decide_eq_true_eq]
  exact (exists_witness_case (fun c => f c = true)).symm

def evaluate (O : DenseOrder A) [DecidableEq A] [DecidableRel O.lt] :
    Formula n → (Fin n → A) → Bool
  | .eq i j, a => decide (a i = a j)
  | .lt i j, a => decide (O.lt (a i) (a j))
  | .neg p, a => !(evaluate O p a)
  | .conj p q, a => evaluate O p a && evaluate O q a
  | .ex p, a => anyWitness (fun c => evaluate O p (extend (candidate O a c) a))

theorem evaluate_correct (O : DenseOrder A) [DecidableEq A] [DecidableRel O.lt]
    (p : Formula n) (a : Fin n → A) : evaluate O p a = true ↔ Holds O p a := by
  induction p with
  | eq i j => simp [evaluate, Holds]
  | lt i j => simp [evaluate, Holds]
  | neg p ih =>
    change (!(evaluate O p a)) = true ↔ ¬ Holds O p a
    rw [← ih a]
    cases evaluate O p a <;> decide
  | conj p q ihp ihq =>
    simp only [evaluate, Bool.and_eq_true, Holds]
    exact and_congr (ihp a) (ihq a)
  | ex p ih =>
    rw [finite_witness_reduction]
    change anyWitness _ = true ↔ _
    rw [anyWitness_correct]
    exact exists_congr (fun c => ih _)

theorem sentence_evaluation (O : DenseOrder A) (P : DenseOrder B)
    [DecidableEq A] [DecidableRel O.lt] (p : Formula 0) :
    evaluate O p (noVars A) = true ↔ Holds P p (noVars B) :=
  (evaluate_correct O p _).trans (sentence_agreement O P p)

def rationalOrder : DenseOrder Rat where
  lt a b := a < b
  irrefl _ := Rat.lt_irrefl
  trans h k := by grind
  tri a b := by
    rcases Rat.le_total (a := a) (b := b) with h | h
    · rcases Rat.le_iff_lt_or_eq.mp h with h | h
      · exact Or.inl h
      · exact Or.inr (Or.inl h)
    · rcases Rat.le_iff_lt_or_eq.mp h with h | h
      · exact Or.inr (Or.inr h)
      · exact Or.inr (Or.inl h.symm)
  seed := 0
  before a := a - 1
  after a := a + 1
  between a b := (a + b) / 2
  before_lt a := by grind
  lt_after a := by grind
  between_lt h := by
    constructor
    · rw [Rat.lt_div_iff (by decide : (0 : Rat) < 2)]
      grind
    · rw [Rat.div_lt_iff (by decide : (0 : Rat) < 2)]
      grind

instance rationalDecidable : DecidableRel rationalOrder.lt :=
  fun a b => inferInstanceAs (Decidable (a < b))

def decideSentence (p : Formula 0) : Bool := evaluate rationalOrder p (noVars Rat)

theorem decideSentence_correct (O : DenseOrder A) (p : Formula 0) :
    decideSentence p = true ↔ Holds O p (noVars A) :=
  sentence_evaluation rationalOrder O p

def Formula.all (p : Formula (n+1)) : Formula n := .neg (.ex (.neg p))

theorem all_semantics (O : DenseOrder A) (p : Formula (n+1)) (a : Fin n → A) :
    Holds O p.all a ↔ ∀ x, Holds O p (extend x a) := by
  classical
  change (¬ ∃ x, ¬ Holds O p (extend x a)) ↔ _
  constructor
  · intro h x
    exact Classical.byContradiction (fun hx => h ⟨x, hx⟩)
  · intro h hn
    obtain ⟨x, hx⟩ := hn
    exact hx (h x)

def Formula.or (p q : Formula n) : Formula n := .neg (.conj (.neg p) (.neg q))

theorem or_semantics (O : DenseOrder A) (p q : Formula n) (a : Fin n → A) :
    Holds O (p.or q) a ↔ Holds O p a ∨ Holds O q a := by
  classical
  change (¬ (¬ Holds O p a ∧ ¬ Holds O q a)) ↔ _
  constructor
  · intro h
    by_cases hp : Holds O p a
    · exact Or.inl hp
    · exact Or.inr (Classical.byContradiction (fun hq => h ⟨hp, hq⟩))
  · intro h hn
    exact h.elim hn.1 hn.2

def densitySentence : Formula 0 :=
  .all (.all (Formula.or (.neg (.lt 1 0)) (.ex (.conj (.lt 2 0) (.lt 0 1)))))

def leastElementSentence : Formula 0 := .ex (.all (.neg (.lt 0 1)))

def greatestElementSentence : Formula 0 := .ex (.all (.neg (.lt 1 0)))

theorem density_decision : decideSentence densitySentence = true := by decide +kernel

theorem leastElement_decision : decideSentence leastElementSentence = false := by decide +kernel

theorem greatestElement_decision : decideSentence greatestElementSentence = false := by decide +kernel

theorem density_truth (O : DenseOrder A) : Holds O densitySentence (noVars A) :=
  (decideSentence_correct O densitySentence).mp density_decision

theorem no_least_element_truth (O : DenseOrder A) :
    ¬ Holds O leastElementSentence (noVars A) := by
  intro h
  have ht := (decideSentence_correct O leastElementSentence).mpr h
  rw [leastElement_decision] at ht
  exact Bool.noConfusion ht

theorem no_greatest_element_truth (O : DenseOrder A) :
    ¬ Holds O greatestElementSentence (noVars A) := by
  intro h
  have ht := (decideSentence_correct O greatestElementSentence).mpr h
  rw [greatestElement_decision] at ht
  exact Bool.noConfusion ht

structure OrderEmbedding (O : DenseOrder A) (P : DenseOrder B) where
  map : A → B
  injective : Function.Injective map
  order : ∀ a b, O.lt a b ↔ P.lt (map a) (map b)

theorem orderEmbedding_elementary (O : DenseOrder A) (P : DenseOrder B)
    (f : OrderEmbedding O P) (p : Formula n) (a : Fin n → A) :
    Holds O p a ↔ Holds P p (fun i => f.map (a i)) := by
  apply truth_of_pattern O P
  exact ⟨fun _ _ => ⟨congrArg f.map, fun h => f.injective h⟩,
    fun i j => f.order (a i) (a j)⟩

inductive Generated (O : DenseOrder A) : A → Prop where
  | seed : Generated O O.seed
  | before {a} : Generated O a → Generated O (O.before a)
  | after {a} : Generated O a → Generated O (O.after a)
  | between {a b} : Generated O a → Generated O b → Generated O (O.between a b)

structure Closed (O : DenseOrder A) (C : A → Prop) : Prop where
  seed : C O.seed
  before : ∀ a, C a → C (O.before a)
  after : ∀ a, C a → C (O.after a)
  between : ∀ a b, C a → C b → C (O.between a b)

theorem generated_closed (O : DenseOrder A) : Closed O (Generated O) :=
  ⟨Generated.seed, fun _ => Generated.before, fun _ => Generated.after,
    fun _ _ => Generated.between⟩

theorem generated_least (O : DenseOrder A) (C : A → Prop) (hc : Closed O C)
    {a : A} (ha : Generated O a) : C a := by
  induction ha with
  | seed => exact hc.seed
  | before _ ih => exact hc.before _ ih
  | after _ ih => exact hc.after _ ih
  | between _ _ ih1 ih2 => exact hc.between _ _ ih1 ih2

theorem generated_iff_all_closed (O : DenseOrder A) (a : A) :
    Generated O a ↔ ∀ C, Closed O C → C a := by
  constructor
  · exact fun ha C hc => generated_least O C hc ha
  · exact fun h => h (Generated O) (generated_closed O)

def generatedOrder (O : DenseOrder A) : DenseOrder {a : A // Generated O a} where
  lt a b := O.lt a.val b.val
  irrefl a := O.irrefl a.val
  trans := O.trans
  tri a b := by
    rcases O.tri a.val b.val with h | h | h
    · exact Or.inl h
    · exact Or.inr (Or.inl (Subtype.ext h))
    · exact Or.inr (Or.inr h)
  seed := ⟨O.seed, Generated.seed⟩
  before a := ⟨O.before a.val, Generated.before a.property⟩
  after a := ⟨O.after a.val, Generated.after a.property⟩
  between a b := ⟨O.between a.val b.val, Generated.between a.property b.property⟩
  before_lt a := O.before_lt a.val
  lt_after a := O.lt_after a.val
  between_lt := O.between_lt

def generatedEmbedding (O : DenseOrder A) : OrderEmbedding (generatedOrder O) O where
  map := Subtype.val
  injective := fun _ _ => Subtype.ext
  order _ _ := Iff.rfl

theorem generated_elementary (O : DenseOrder A) (p : Formula n)
    (a : Fin n → {x : A // Generated O x}) :
    Holds (generatedOrder O) p a ↔ Holds O p (fun i => (a i).val) :=
  orderEmbedding_elementary (generatedOrder O) O (generatedEmbedding O) p a

end OrderGenerativity
