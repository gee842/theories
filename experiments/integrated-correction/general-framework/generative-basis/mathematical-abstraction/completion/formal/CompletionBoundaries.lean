import CompletionExamples
import FiniteBranching

/-! Counterexamples showing the distinct work of compactness and generation in
A3. The Nat-with-infinity carrier is represented as nonempty ideals of Nat, using
the same completion that the other checked results construct. -/
namespace CompletionBoundaries
open CompletionWarrant CompletionRole CompletionExamples

abbrev NatInfinity := Ideal natOrder
abbrev infinityOrder := idealPoset natOrder
abbrev infinityDcpo := idealDcpo natOrder

/-- The all-natural-numbers ideal is not a compact point. -/
theorem infinity_not_compact : ¬ Compact infinityDcpo allNaturals := by
  intro h
  obtain ⟨n, hn⟩ := (compact_iff_principal natOrder allNaturals).mp h
  have hm : (principal natOrder n).mem (n+1) := hn ▸ True.intro
  change n+1 ≤ n at hm
  omega

/-- All finite initial segments of the ideal carrier, excluding its infinity. -/
def finiteSegments : Ideal infinityOrder where
  mem I := ∃ n, Ideal.LE I (principal natOrder n)
  nonempty := ⟨principal natOrder 0, 0, Ideal.le_refl _⟩
  lower hJI hI := by
    obtain ⟨n, hn⟩ := hI
    exact ⟨n, Ideal.le_trans hJI hn⟩
  directed hp hq := by
    obtain ⟨n, hn⟩ := hp
    obtain ⟨m, hm⟩ := hq
    exact ⟨principal natOrder (max n m), ⟨max n m, Ideal.le_refl _⟩,
      Ideal.le_trans hn (principal_mono natOrder (Nat.le_max_left _ _)),
      Ideal.le_trans hm (principal_mono natOrder (Nat.le_max_right _ _))⟩

theorem infinity_not_finite : ¬ finiteSegments.mem allNaturals := by
  rintro ⟨n, hn⟩
  have h := hn (n+1) True.intro
  change n+1 ≤ n at h
  omega

theorem finiteSegments_ne_principal_infinity :
    finiteSegments ≠ principal infinityOrder allNaturals := by
  intro h
  apply infinity_not_finite
  rw [h]
  exact Ideal.le_refl _

def finitePrincipalFamily (J : Ideal infinityOrder) : Prop :=
  ∃ n, J = principal infinityOrder (principal natOrder n)

theorem finitePrincipalFamily_directed :
    Directed infinityOrder (fun I => ∃ n, I = principal natOrder n) := by
  constructor
  · exact ⟨principal natOrder 0, 0, rfl⟩
  · rintro I ⟨n, rfl⟩ J ⟨m, rfl⟩
    exact ⟨principal natOrder (max n m), ⟨max n m, rfl⟩,
      principal_mono natOrder (Nat.le_max_left _ _),
      principal_mono natOrder (Nat.le_max_right _ _)⟩

theorem infinity_is_old_sup :
    infinityDcpo.sup (fun I => ∃ n, I = principal natOrder n)
      finitePrincipalFamily_directed = allNaturals := by
  apply Ideal.ext
  intro n
  constructor
  · intro _; trivial
  · intro _; exact ⟨principal natOrder n, ⟨n, rfl⟩, Nat.le_refl n⟩

theorem finitePrincipalFamily_directed_again :
    Directed (idealPoset infinityOrder) finitePrincipalFamily := by
  constructor
  · exact ⟨principal infinityOrder (principal natOrder 0), 0, rfl⟩
  · rintro I ⟨n, rfl⟩ J ⟨m, rfl⟩
    exact ⟨principal infinityOrder (principal natOrder (max n m)),
      ⟨max n m, rfl⟩,
      principal_mono infinityOrder (principal_mono natOrder (Nat.le_max_left _ _)),
      principal_mono infinityOrder (principal_mono natOrder (Nat.le_max_right _ _))⟩

theorem completed_old_sequence_sup :
    (idealDcpo infinityOrder).sup finitePrincipalFamily
      finitePrincipalFamily_directed_again = finiteSegments := by
  apply Ideal.ext
  intro I
  constructor
  · rintro ⟨J, ⟨n, rfl⟩, hI⟩
    exact ⟨n, hI⟩
  · rintro ⟨n, hI⟩
    exact ⟨principal infinityOrder (principal natOrder n), ⟨n, rfl⟩, hI⟩

/-- Principal embedding does not preserve an already existing infinite supremum. -/
theorem old_infinite_supremum_not_preserved :
    (idealDcpo infinityOrder).sup finitePrincipalFamily finitePrincipalFamily_directed_again ≠
      principal infinityOrder
        (infinityDcpo.sup (fun I => ∃ n, I = principal natOrder n)
          finitePrincipalFamily_directed) := by
  rw [completed_old_sequence_sup, infinity_is_old_sup]
  exact finiteSegments_ne_principal_infinity

def flatten : Ideal infinityOrder → NatInfinity :=
  extend infinityDcpo id (fun _ _ h => h)

theorem flatten_finiteSegments : flatten finiteSegments = allNaturals := by
  apply Ideal.le_antisymm
  · exact completed_nat_greatest _
  · intro n _
    have h := extend_upper infinityDcpo id (fun _ _ h => h) finiteSegments
      (principal natOrder n) ⟨n, Ideal.le_refl _⟩
    exact h n (Nat.le_refl n)

theorem flatten_principal_infinity :
    flatten (principal infinityOrder allNaturals) = allNaturals :=
  extend_principal infinityDcpo id (fun _ _ h => h) allNaturals

/-- Two different ideals collapse when a named noncompact infinity is evaluated. -/
theorem flatten_not_injective :
    ∃ I J : Ideal infinityOrder, I ≠ J ∧ flatten I = flatten J :=
  ⟨finiteSegments, principal infinityOrder allNaturals,
    finiteSegments_ne_principal_infinity,
    flatten_finiteSegments.trans flatten_principal_infinity.symm⟩

/-- Identity always has faithful comparison and generation by all predecessors. -/
theorem identity_approximation {α : Type u} (P : Poset α) (D : Dcpo P) (x : α) :
    ∃ h : Directed P (fun p => P.le p x),
      D.sup (Image id (fun p => P.le p x))
        (image_directed (fun _ _ h => h) h) = x := by
  let h : Directed P (fun p => P.le p x) :=
    ⟨⟨x, P.refl x⟩, fun p hp q hq => ⟨x, P.refl x, hp, hq⟩⟩
  refine ⟨h, P.antisymm ?_ ?_⟩
  · apply D.least
    rintro p ⟨q, hq, rfl⟩
    exact hq
  · exact D.upper _ _ x ⟨x, P.refl x, rfl⟩

theorem identity_infinity_embedding :
    ∀ p q : NatInfinity, infinityOrder.le (id p) (id q) ↔ infinityOrder.le p q :=
  fun _ _ => Iff.rfl

theorem identity_infinity_not_basis :
    ¬ BasisRole infinityOrder infinityOrder infinityDcpo id :=
  fun R => infinity_not_compact (R.compact allNaturals)

/-- A singleton approximation order. -/
def unitOrder : Poset Unit where
  le _ _ := True
  refl _ := True.intro
  trans _ _ := True.intro
  antisymm := by intro a b _ _; cases a; cases b; rfl

def onlyFalse (_ : Unit) : Prop := False

theorem onlyFalse_embedding (a b : Unit) :
    truthPoset.le (onlyFalse a) (onlyFalse b) ↔ unitOrder.le a b :=
  ⟨fun _ => True.intro, fun _ h => h⟩

theorem false_compact : Compact truthDcpo False := by
  intro S hS _
  obtain ⟨p, hp⟩ := hS.nonempty
  exact ⟨p, hp, False.elim⟩

theorem onlyFalse_compact (a : Unit) : Compact truthDcpo (onlyFalse a) := false_compact

theorem false_approximants_directed (x : Prop) :
    Directed unitOrder (fun a => truthPoset.le (onlyFalse a) x) := by
  exact ⟨⟨(), False.elim⟩, fun _ _ _ _ => ⟨(), False.elim, True.intro, True.intro⟩⟩

theorem onlyFalse_monotone : Monotone unitOrder truthPoset onlyFalse :=
  fun _ _ _ h => h

/-- Even the full set of supplied approximations below True generates only False. -/
theorem false_generation_at_true :
    truthDcpo.sup (Image onlyFalse (fun a => truthPoset.le (onlyFalse a) True))
      (image_directed onlyFalse_monotone (false_approximants_directed True)) = False := by
  apply propext
  constructor
  · rintro ⟨p, ⟨a, _, rfl⟩, hp⟩
    exact hp
  · exact False.elim

theorem true_not_generated :
    truthDcpo.sup (Image onlyFalse (fun a => truthPoset.le (onlyFalse a) True))
      (image_directed onlyFalse_monotone (false_approximants_directed True)) ≠ True := by
  rw [false_generation_at_true]
  intro h
  exact Eq.mpr h True.intro

/-- Dropping generation admits the extra True point despite compact embedding. -/
theorem onlyFalse_not_basis : ¬ BasisRole unitOrder truthPoset truthDcpo onlyFalse := by
  intro R
  have h := R.generates True
  have hp := Eq.mpr h True.intro
  obtain ⟨p, ⟨a, _, rfl⟩, hf⟩ := hp
  exact hf


/-- Restrict concrete steps to nodes retaining the declared history condition. -/
def GuardedStep {α : Type u} (R : α → α → Prop) (admitted : α → Prop)
    (a b : α) : Prop := R a b ∧ admitted b

/-- A4b's admitted-node condition survives the actual constructed branch. -/
theorem guarded_concrete_lifting {α : Type u} (R : α → α → Prop)
    (initial : List α) (children : α → List α)
    (enumerates : ∀ a b, R a b ↔ b ∈ children a) (admitted : α → Prop)
    (arbitraryDepth : ∀ n, ∃ a, a ∈ initial ∧ admitted a ∧
      CompletionLifting.Reach (GuardedStep R admitted) a n) :
    ∃ path : Nat → α, path 0 ∈ initial ∧
      (∀ n, admitted (path n)) ∧ ∀ n, R (path n) (path (n+1)) := by
  classical
  let roots := initial.filter (fun a => decide (admitted a))
  let nexts := fun a => (children a).filter (fun b => decide (admitted b))
  have hen : ∀ a b, GuardedStep R admitted a b ↔ b ∈ nexts a := by
    intro a b
    simp [GuardedStep, nexts, enumerates a b]
  have harb : ∀ n, ∃ a, a ∈ roots ∧
      CompletionLifting.Reach (GuardedStep R admitted) a n := by
    intro n
    obtain ⟨a, ha, had, hr⟩ := arbitraryDepth n
    exact ⟨a, by simp [roots, ha, had], hr⟩
  obtain ⟨path, hp, he⟩ := CompletionLifting.finite_initial_lifting
    (GuardedStep R admitted) roots nexts hen harb
  have hi : path 0 ∈ initial ∧ admitted (path 0) := by
    simpa [roots] using hp
  refine ⟨path, hi.1, ?_, fun n => (he n).1⟩
  intro n
  cases n with
  | zero => exact hi.2
  | succ n => exact (he n).2


/-- A bounded nonempty natural ideal has a greatest natural member. -/
theorem bounded_nat_greatest (I : Ideal natOrder) (N : Nat)
    (bound : ∀ n, I.mem n → n ≤ N) :
    ∃ k, I.mem k ∧ ∀ n, I.mem n → n ≤ k := by
  classical
  induction N with
  | zero =>
    obtain ⟨k, hk⟩ := I.nonempty
    exact ⟨k, hk, fun n hn => Nat.le_trans (bound n hn) (Nat.zero_le k)⟩
  | succ N ih =>
    by_cases hN : I.mem (N+1)
    · exact ⟨N+1, hN, bound⟩
    · apply ih
      intro n hn
      have hb := bound n hn
      have hne : n ≠ N+1 := fun h => hN (h ▸ hn)
      omega

/-- The chosen carrier is exactly the finite principal points plus one infinity. -/
theorem natInfinity_classification (I : NatInfinity) :
    (∃ n, I = principal natOrder n) ∨ I = allNaturals := by
  classical
  by_cases hb : ∃ N, ∀ n, I.mem n → n ≤ N
  · obtain ⟨N, hN⟩ := hb
    obtain ⟨k, hk, hmax⟩ := bounded_nat_greatest I N hN
    exact Or.inl ⟨k, Ideal.ext (fun n => ⟨hmax n, fun hn => I.lower hn hk⟩)⟩
  · apply Or.inr
    apply Ideal.ext
    intro n
    constructor
    · intro _; trivial
    · intro _
      apply Classical.byContradiction
      intro hn
      apply hb
      refine ⟨n, ?_⟩
      intro m hm
      apply Classical.byContradiction
      intro hmn
      have hnm : n ≤ m := by omega
      exact hn (I.lower hnm hm)

/-- The singleton basis's ideal completion itself has only one point. -/
theorem unit_ideal_unique (I : Ideal unitOrder) : I = principal unitOrder () := by
  apply Ideal.ext
  intro a
  constructor
  · intro _; trivial
  · intro _
    obtain ⟨b, hb⟩ := I.nonempty
    exact I.lower True.intro hb

end CompletionBoundaries

/- Kernel dependency audit of every named theorem. -/
#print axioms CompletionBoundaries.infinity_not_compact
#print axioms CompletionBoundaries.infinity_not_finite
#print axioms CompletionBoundaries.finiteSegments_ne_principal_infinity
#print axioms CompletionBoundaries.finitePrincipalFamily_directed
#print axioms CompletionBoundaries.infinity_is_old_sup
#print axioms CompletionBoundaries.finitePrincipalFamily_directed_again
#print axioms CompletionBoundaries.completed_old_sequence_sup
#print axioms CompletionBoundaries.old_infinite_supremum_not_preserved
#print axioms CompletionBoundaries.flatten_finiteSegments
#print axioms CompletionBoundaries.flatten_principal_infinity
#print axioms CompletionBoundaries.flatten_not_injective
#print axioms CompletionBoundaries.identity_approximation
#print axioms CompletionBoundaries.identity_infinity_embedding
#print axioms CompletionBoundaries.identity_infinity_not_basis
#print axioms CompletionBoundaries.onlyFalse_embedding
#print axioms CompletionBoundaries.false_compact
#print axioms CompletionBoundaries.onlyFalse_compact
#print axioms CompletionBoundaries.false_approximants_directed
#print axioms CompletionBoundaries.onlyFalse_monotone
#print axioms CompletionBoundaries.false_generation_at_true
#print axioms CompletionBoundaries.true_not_generated
#print axioms CompletionBoundaries.onlyFalse_not_basis
#print axioms CompletionBoundaries.guarded_concrete_lifting
#print axioms CompletionBoundaries.bounded_nat_greatest
#print axioms CompletionBoundaries.natInfinity_classification
#print axioms CompletionBoundaries.unit_ideal_unique
