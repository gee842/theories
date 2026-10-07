import Std

/-!
General ideal-admissibility theorems, corresponding to W1, W2 and W2a in
COMPLETION-WARRANT-MATH.md. The supplied poset is an approximation representation,
not an ontological separation. Classical reasoning concerns arbitrary predicates;
no effective witness procedure or ethical warrant is inferred.
-/

namespace CompletionWarrant

universe u

structure Poset (α : Type u) where
  le : α → α → Prop
  refl : ∀ a, le a a
  trans : ∀ {a b c}, le a b → le b c → le a c
  antisymm : ∀ {a b}, le a b → le b a → a = b

variable {α : Type u} (P : Poset α)

structure Ideal where
  mem : α → Prop
  nonempty : ∃ p, mem p
  lower : ∀ {p q}, P.le p q → mem q → mem p
  directed : ∀ {p q}, mem p → mem q → ∃ r, mem r ∧ P.le p r ∧ P.le q r

namespace Ideal

variable {P}

def LE (I J : Ideal P) : Prop := ∀ p, I.mem p → J.mem p

theorem ext {I J : Ideal P} (h : ∀ p, I.mem p ↔ J.mem p) : I = J := by
  cases I with
  | mk im ine il id =>
    cases J with
    | mk jm jne jl jd =>
      have he : im = jm := funext (fun p => propext (h p))
      cases he
      rfl

theorem le_refl (I : Ideal P) : LE I I := fun _ h => h

theorem le_trans {I J K : Ideal P} (h : LE I J) (k : LE J K) : LE I K :=
  fun p hp => k p (h p hp)

theorem le_antisymm {I J : Ideal P} (h : LE I J) (k : LE J I) : I = J :=
  ext (fun p => ⟨h p, k p⟩)

end Ideal

def principal (p : α) : Ideal P where
  mem q := P.le q p
  nonempty := ⟨p, P.refl p⟩
  lower h k := P.trans h k
  directed hp hq := ⟨p, P.refl p, hp, hq⟩

theorem principal_mem (p : α) : (principal P p).mem p := P.refl p

theorem principal_le_iff (p : α) (I : Ideal P) :
    Ideal.LE (principal P p) I ↔ I.mem p := by
  constructor
  · intro h; exact h p (P.refl p)
  · intro h q hq; exact I.lower hq h

theorem principal_mono {p q : α} (h : P.le p q) :
    Ideal.LE (principal P p) (principal P q) := fun _ k => P.trans k h

structure DirectedFamily (D : Ideal P → Prop) : Prop where
  nonempty : ∃ I, D I
  directed : ∀ {I J}, D I → D J → ∃ K, D K ∧ Ideal.LE I K ∧ Ideal.LE J K

def familyUnion (D : Ideal P → Prop) (hd : DirectedFamily P D) : Ideal P where
  mem p := ∃ I, D I ∧ I.mem p
  nonempty := by
    obtain ⟨I, hI⟩ := hd.nonempty
    obtain ⟨p, hp⟩ := I.nonempty
    exact ⟨p, I, hI, hp⟩
  lower := by
    intro p q hpq hq
    obtain ⟨I, hI, hi⟩ := hq
    exact ⟨I, hI, I.lower hpq hi⟩
  directed := by
    intro p q hp hq
    obtain ⟨I, hI, hip⟩ := hp
    obtain ⟨J, hJ, hjq⟩ := hq
    obtain ⟨K, hK, hik, hjk⟩ := hd.directed hI hJ
    obtain ⟨r, hr, hpr, hqr⟩ := K.directed (hik p hip) (hjk q hjq)
    exact ⟨r, ⟨K, hK, hr⟩, hpr, hqr⟩

theorem le_familyUnion (D : Ideal P → Prop) (hd : DirectedFamily P D)
    {I : Ideal P} (hI : D I) : Ideal.LE I (familyUnion P D hd) :=
  fun _ hp => ⟨I, hI, hp⟩

theorem familyUnion_le (D : Ideal P → Prop) (hd : DirectedFamily P D)
    (J : Ideal P) (hJ : ∀ I, D I → Ideal.LE I J) :
    Ideal.LE (familyUnion P D hd) J := by
  intro p hp
  obtain ⟨I, hI, hi⟩ := hp
  exact hJ I hI p hi

def principalFamily (I : Ideal P) (J : Ideal P) : Prop :=
  ∃ p, I.mem p ∧ J = principal P p

theorem principalFamily_directed (I : Ideal P) :
    DirectedFamily P (principalFamily P I) := by
  constructor
  · obtain ⟨p, hp⟩ := I.nonempty
    exact ⟨principal P p, p, hp, rfl⟩
  · intro J K hJ hK
    obtain ⟨p, hp, rfl⟩ := hJ
    obtain ⟨q, hq, rfl⟩ := hK
    obtain ⟨r, hr, hpr, hqr⟩ := I.directed hp hq
    exact ⟨principal P r, ⟨r, hr, rfl⟩, principal_mono P hpr, principal_mono P hqr⟩

theorem union_principalFamily (I : Ideal P) :
    familyUnion P (principalFamily P I) (principalFamily_directed P I) = I := by
  apply Ideal.ext
  intro p
  constructor
  · intro h
    obtain ⟨J, ⟨q, hq, rfl⟩, hp⟩ := h
    exact I.lower hp hq
  · intro hp
    exact ⟨principal P p, ⟨p, hp, rfl⟩, P.refl p⟩

/-! Admission predicates are independently stated; finite refutation is not defined
as Scott closure or as the desired representation. -/

def LowerBasis (Q : α → Prop) : Prop :=
  ∀ {p q}, P.le p q → Q q → Q p

def Admits (Q : α → Prop) (I : Ideal P) : Prop := ∀ p, I.mem p → Q p

def Permitted (C : Ideal P → Prop) (p : α) : Prop := C (principal P p)

def Content (C : Ideal P → Prop) (p : α) : Prop := ∃ I, C I ∧ I.mem p

def FiniteRefutable (C : Ideal P → Prop) : Prop :=
  ∀ I, ¬ C I → ∃ p, I.mem p ∧ ∀ J, C J → ¬ J.mem p

structure ScottClosed (C : Ideal P → Prop) : Prop where
  lower : ∀ {I J}, C I → Ideal.LE J I → C J
  directedClosed : ∀ (D : Ideal P → Prop) (hd : DirectedFamily P D),
    (∀ I, D I → C I) → C (familyUnion P D hd)

theorem admits_principal_iff (Q : α → Prop) (hq : LowerBasis P Q) (p : α) :
    Admits P Q (principal P p) ↔ Q p := by
  constructor
  · intro h; exact h p (P.refl p)
  · intro h q hq'; exact hq hq' h

theorem refutable_scottClosed (C : Ideal P → Prop) (hc : FiniteRefutable P C) :
    ScottClosed P C := by
  classical
  constructor
  · intro I J hI hji
    apply Classical.byContradiction
    intro hJ
    obtain ⟨p, hp, hex⟩ := hc J hJ
    exact hex I hI (hji p hp)
  · intro D hd hdc
    apply Classical.byContradiction
    intro hu
    obtain ⟨p, ⟨I, hI, hp⟩, hex⟩ := hc (familyUnion P D hd) hu
    exact hex I (hdc I hI) hp

theorem permitted_lower (C : Ideal P → Prop) (hc : ScottClosed P C) :
    LowerBasis P (Permitted P C) := by
  intro p q hpq hq
  exact hc.lower hq (principal_mono P hpq)

theorem scottClosed_iff_admits_permitted (C : Ideal P → Prop) (hc : ScottClosed P C)
    (I : Ideal P) : C I ↔ Admits P (Permitted P C) I := by
  constructor
  · intro hi p hp
    exact hc.lower hi ((principal_le_iff P p I).mpr hp)
  · intro hi
    have hprincipal : ∀ J, principalFamily P I J → C J := by
      intro J hj
      obtain ⟨p, hp, rfl⟩ := hj
      exact hi p hp
    have h := hc.directedClosed (principalFamily P I) (principalFamily_directed P I)
      hprincipal
    rw [union_principalFamily P I] at h
    exact h

theorem admits_refutable (Q : α → Prop) : FiniteRefutable P (Admits P Q) := by
  classical
  intro I hi
  have hex : ∃ p, I.mem p ∧ ¬ Q p := by
    apply Classical.byContradiction
    intro hn
    apply hi
    intro p hp
    apply Classical.byContradiction
    intro hq
    exact hn ⟨p, hp, hq⟩
  obtain ⟨p, hp, hnq⟩ := hex
  exact ⟨p, hp, fun J hj hjp => hnq (hj p hjp)⟩

theorem admits_scottClosed (Q : α → Prop) : ScottClosed P (Admits P Q) :=
  refutable_scottClosed P (Admits P Q) (admits_refutable P Q)

theorem scottClosed_refutable (C : Ideal P → Prop) (hc : ScottClosed P C) :
    FiniteRefutable P C := by
  intro I hi
  have hn : ¬ Admits P (Permitted P C) I :=
    fun h => hi ((scottClosed_iff_admits_permitted P C hc I).mpr h)
  obtain ⟨p, hp, hex⟩ := admits_refutable P (Permitted P C) I hn
  exact ⟨p, hp, fun J hj => hex J ((scottClosed_iff_admits_permitted P C hc J).mp hj)⟩

/-- W1, equivalence 1 ↔ 2. -/
theorem finiteRefutable_iff_scottClosed (C : Ideal P → Prop) :
    FiniteRefutable P C ↔ ScottClosed P C :=
  ⟨refutable_scottClosed P C, scottClosed_refutable P C⟩

/-- W1, equivalence 2 ↔ 3, quantified over arbitrary lower predicates. -/
theorem scottClosed_iff_lower_basis (C : Ideal P → Prop) :
    ScottClosed P C ↔ ∃ Q : α → Prop, LowerBasis P Q ∧
      ∀ I, C I ↔ Admits P Q I := by
  constructor
  · intro hc
    exact ⟨Permitted P C, permitted_lower P C hc,
      scottClosed_iff_admits_permitted P C hc⟩
  · intro h
    obtain ⟨Q, _, heq⟩ := h
    apply refutable_scottClosed P C
    intro I hi
    have hn : ¬ Admits P Q I := fun h => hi ((heq I).mpr h)
    obtain ⟨p, hp, hex⟩ := admits_refutable P Q I hn
    exact ⟨p, hp, fun J hj => hex J ((heq J).mp hj)⟩

/-- W1, equivalence 1 ↔ 3. -/
theorem finiteRefutable_iff_lower_basis (C : Ideal P → Prop) :
    FiniteRefutable P C ↔ ∃ Q : α → Prop, LowerBasis P Q ∧
      ∀ I, C I ↔ Admits P Q I :=
  (finiteRefutable_iff_scottClosed P C).trans (scottClosed_iff_lower_basis P C)

theorem basis_eq_permitted (C : Ideal P → Prop) (Q : α → Prop)
    (hq : LowerBasis P Q) (heq : ∀ I, C I ↔ Admits P Q I) :
    Q = Permitted P C := by
  funext p
  apply propext
  exact ((heq (principal P p)).trans (admits_principal_iff P Q hq p)).symm

/-- W1's lower basis is unique, as equality of arbitrary predicates. -/
theorem lower_basis_unique (C : Ideal P → Prop) (Q R : α → Prop)
    (hq : LowerBasis P Q) (hr : LowerBasis P R)
    (heq : ∀ I, C I ↔ Admits P Q I) (her : ∀ I, C I ↔ Admits P R I) : Q = R :=
  (basis_eq_permitted P C Q hq heq).trans (basis_eq_permitted P C R hr her).symm

theorem permitted_eq_content (C : Ideal P → Prop) (hc : ScottClosed P C) :
    Permitted P C = Content P C := by
  funext p
  apply propext
  constructor
  · intro hp; exact ⟨principal P p, hp, P.refl p⟩
  · intro h
    obtain ⟨I, hI, hp⟩ := h
    exact hc.lower hI ((principal_le_iff P p I).mpr hp)

theorem basis_eq_content (C : Ideal P → Prop) (Q : α → Prop)
    (hq : LowerBasis P Q) (heq : ∀ I, C I ↔ Admits P Q I) :
    Q = Content P C := by
  have hc := (scottClosed_iff_lower_basis P C).mpr ⟨Q, hq, heq⟩
  exact (basis_eq_permitted P C Q hq heq).trans (permitted_eq_content P C hc)

/-- Empty basis has no nonempty ideals, without assuming an inhabited poset. -/
theorem admits_empty (I : Ideal P) : ¬ Admits P (fun _ => False) I := by
  intro h
  obtain ⟨p, hp⟩ := I.nonempty
  exact h p hp

theorem empty_scottClosed : ScottClosed P (fun _ => False) := by
  apply (scottClosed_iff_lower_basis P (fun _ => False)).mpr
  refine ⟨(fun _ => False), ?_, ?_⟩
  · intro _ _ _ h; exact h
  · intro I
    exact ⟨False.elim, admits_empty P I⟩

theorem empty_finiteRefutable : FiniteRefutable P (fun _ => False) :=
  scottClosed_refutable P (fun _ => False) (empty_scottClosed P)

theorem empty_content : Content P (fun _ => False) = (fun _ => False) := by
  funext p
  apply propext
  constructor
  · intro h; obtain ⟨_, hI, _⟩ := h; exact hI
  · exact False.elim

theorem content_lower (C : Ideal P → Prop) : LowerBasis P (Content P C) := by
  intro p q hpq hq
  obtain ⟨I, hI, hqi⟩ := hq
  exact ⟨I, hI, I.lower hpq hqi⟩

def ScottHull (C : Ideal P → Prop) : Ideal P → Prop := Admits P (Content P C)

theorem hull_scottClosed (C : Ideal P → Prop) : ScottClosed P (ScottHull P C) :=
  admits_scottClosed P (Content P C)

theorem hull_contains (C : Ideal P → Prop) (I : Ideal P) (hi : C I) : ScottHull P C I :=
  fun _ hp => ⟨I, hi, hp⟩

/-- W2: the displayed hull is below every Scott-closed enlargement. -/
theorem hull_least (C E : Ideal P → Prop) (he : ScottClosed P E)
    (hce : ∀ I, C I → E I) : ∀ I, ScottHull P C I → E I := by
  intro I hi
  apply (scottClosed_iff_admits_permitted P E he I).mpr
  intro p hp
  obtain ⟨J, hj, hpj⟩ := hi p hp
  exact he.lower (hce J hj) ((principal_le_iff P p J).mpr hpj)

/-- W2's no-new-finite-content assertion. -/
theorem hull_preserves_content (C : Ideal P → Prop) :
    Content P (ScottHull P C) = Content P C := by
  funext p
  apply propext
  constructor
  · intro h
    obtain ⟨I, hi, hp⟩ := h
    exact hi p hp
  · intro h
    obtain ⟨I, hi, hp⟩ := h
    exact ⟨I, hull_contains P C I hi, hp⟩

theorem hull_unique (C H : Ideal P → Prop) (hh : ScottClosed P H)
    (hcontains : ∀ I, C I → H I)
    (hleast : ∀ E, ScottClosed P E → (∀ I, C I → E I) → ∀ I, H I → E I) :
    H = ScottHull P C := by
  funext I
  apply propext
  exact ⟨hleast (ScottHull P C) (hull_scottClosed P C) (hull_contains P C) I,
    hull_least P C H hh hcontains I⟩

def AvoidingBasis (F : α → Prop) (p : α) : Prop :=
  ¬ ∃ b, F b ∧ P.le b p

def Respects (F : α → Prop) (I : Ideal P) : Prop :=
  ∀ b, F b → ¬ I.mem b

theorem avoiding_lower (F : α → Prop) : LowerBasis P (AvoidingBasis P F) := by
  intro p q hpq hq hp
  obtain ⟨b, hb, hbp⟩ := hp
  exact hq ⟨b, hb, P.trans hbp hpq⟩

/-- W2a, finite prohibitions characterize the permitted ideal class. -/
theorem respects_iff_admits_avoiding (F : α → Prop) (I : Ideal P) :
    Respects P F I ↔ Admits P (AvoidingBasis P F) I := by
  constructor
  · intro h p hp hex
    obtain ⟨b, hb, hbp⟩ := hex
    exact h b hb (I.lower hbp hp)
  · intro h b hb hib
    exact h b hib ⟨b, hb, P.refl b⟩

theorem respects_scottClosed (F : α → Prop) : ScottClosed P (Respects P F) :=
  (scottClosed_iff_lower_basis P (Respects P F)).mpr
    ⟨AvoidingBasis P F, avoiding_lower P F, respects_iff_admits_avoiding P F⟩

theorem respects_finiteRefutable (F : α → Prop) : FiniteRefutable P (Respects P F) :=
  scottClosed_refutable P (Respects P F) (respects_scottClosed P F)

/-- Maximality among arbitrary classes satisfying the independently given prohibitions. -/
theorem respects_maximal (F : α → Prop) (C : Ideal P → Prop)
    (h : ∀ I, C I → ∀ b, F b → ¬ I.mem b) :
    ∀ I, C I → Respects P F I := h

theorem respects_principal (F : α → Prop) (p : α) :
    Respects P F (principal P p) ↔ AvoidingBasis P F p :=
  (respects_iff_admits_avoiding P F (principal P p)).trans
    (admits_principal_iff P (AvoidingBasis P F) (avoiding_lower P F) p)

/-- W2a uniqueness needs both finite refutation and the exact permitted basis. -/
theorem respects_unique (F : α → Prop) (C : Ideal P → Prop)
    (hc : FiniteRefutable P C)
    (hprincipal : ∀ p, C (principal P p) ↔ AvoidingBasis P F p) :
    C = Respects P F := by
  have hsc := refutable_scottClosed P C hc
  funext I
  apply propext
  constructor
  · intro hi
    apply (respects_iff_admits_avoiding P F I).mpr
    intro p hp
    exact (hprincipal p).mp ((scottClosed_iff_admits_permitted P C hsc I).mp hi p hp)
  · intro hi
    apply (scottClosed_iff_admits_permitted P C hsc I).mpr
    intro p hp
    exact (hprincipal p).mpr ((respects_iff_admits_avoiding P F I).mp hi p hp)

/-- The classification fixes admission once the principal classification is fixed. -/
theorem refutable_eq_admits (C : Ideal P → Prop) (Q : α → Prop)
    (hc : FiniteRefutable P C) (hq : ∀ p, C (principal P p) ↔ Q p) :
    C = Admits P Q := by
  have hsc := refutable_scottClosed P C hc
  funext I
  apply propext
  constructor
  · intro hi p hp
    exact (hq p).mp ((scottClosed_iff_admits_permitted P C hsc I).mp hi p hp)
  · intro hi
    apply (scottClosed_iff_admits_permitted P C hsc I).mpr
    intro p hp
    exact (hq p).mpr (hi p hp)

/-- A hull never combines two finite contents without a jointly admitted upper content. -/
theorem hull_joint_content (C : Ideal P → Prop) (I : Ideal P) (hi : ScottHull P C I)
    {p q : α} (hp : I.mem p) (hq : I.mem q) :
    ∃ J, C J ∧ ∃ r, J.mem r ∧ P.le p r ∧ P.le q r := by
  obtain ⟨r, hr, hpr, hqr⟩ := I.directed hp hq
  obtain ⟨J, hj, hjr⟩ := hi r hr
  exact ⟨J, hj, r, hjr, hpr, hqr⟩

/-! Explicit identification with ideals of the lower subset, including the empty
subset. This does not assume the identification as a definition. -/

def lowerPoset (Q : α → Prop) : Poset {p : α // Q p} where
  le p q := P.le p.val q.val
  refl p := P.refl p.val
  trans := P.trans
  antisymm h k := Subtype.ext (P.antisymm h k)

def restrictIdeal (Q : α → Prop) (I : Ideal P) (hi : Admits P Q I) :
    Ideal (lowerPoset P Q) where
  mem p := I.mem p.val
  nonempty := by
    obtain ⟨p, hp⟩ := I.nonempty
    exact ⟨⟨p, hi p hp⟩, hp⟩
  lower := I.lower
  directed := by
    intro p q hp hq
    obtain ⟨r, hr, hpr, hqr⟩ := I.directed hp hq
    exact ⟨⟨r, hi r hr⟩, hr, hpr, hqr⟩

def liftIdeal (Q : α → Prop) (hq : LowerBasis P Q) (J : Ideal (lowerPoset P Q)) :
    Ideal P where
  mem p := ∃ hp : Q p, J.mem ⟨p, hp⟩
  nonempty := by
    obtain ⟨p, hp⟩ := J.nonempty
    exact ⟨p.val, p.property, hp⟩
  lower := by
    intro p q hpq hex
    obtain ⟨hq', hj⟩ := hex
    have hp := hq hpq hq'
    exact ⟨hp, J.lower (p := ⟨p, hp⟩) (q := ⟨q, hq'⟩) hpq hj⟩
  directed := by
    intro p q hp hq'
    obtain ⟨hp', hjp⟩ := hp
    obtain ⟨hq'', hjq⟩ := hq'
    obtain ⟨r, hr, hpr, hqr⟩ := J.directed hjp hjq
    exact ⟨r.val, ⟨r.property, hr⟩, hpr, hqr⟩

theorem lift_admits (Q : α → Prop) (hq : LowerBasis P Q) (J : Ideal (lowerPoset P Q)) :
    Admits P Q (liftIdeal P Q hq J) := fun _ h => h.choose

theorem lift_restrict (Q : α → Prop) (hq : LowerBasis P Q)
    (I : Ideal P) (hi : Admits P Q I) :
    liftIdeal P Q hq (restrictIdeal P Q I hi) = I := by
  apply Ideal.ext
  intro p
  constructor
  · intro h; exact h.choose_spec
  · intro hp; exact ⟨hi p hp, hp⟩

theorem restrict_lift (Q : α → Prop) (hq : LowerBasis P Q)
    (J : Ideal (lowerPoset P Q)) :
    restrictIdeal P Q (liftIdeal P Q hq J) (lift_admits P Q hq J) = J := by
  apply Ideal.ext
  intro p
  constructor
  · intro h
    obtain ⟨hp, hj⟩ := h
    exact hj
  · intro hp; exact ⟨p.property, hp⟩

theorem lift_order_iff (Q : α → Prop) (hq : LowerBasis P Q)
    (J K : Ideal (lowerPoset P Q)) :
    Ideal.LE (liftIdeal P Q hq J) (liftIdeal P Q hq K) ↔ Ideal.LE J K := by
  constructor
  · intro h p hp
    have hk := h p.val ⟨p.property, hp⟩
    obtain ⟨_, hkp⟩ := hk
    exact hkp
  · intro h p hp
    obtain ⟨hqp, hjp⟩ := hp
    exact ⟨hqp, h ⟨p, hqp⟩ hjp⟩

theorem empty_lower_no_ideal (J : Ideal (lowerPoset P (fun _ => False))) : False := by
  obtain ⟨p, _⟩ := J.nonempty
  exact p.property

end CompletionWarrant

/- Kernel dependency audit: no custom axioms or proof placeholders. -/
#print axioms CompletionWarrant.Ideal.ext
#print axioms CompletionWarrant.Ideal.le_refl
#print axioms CompletionWarrant.Ideal.le_trans
#print axioms CompletionWarrant.Ideal.le_antisymm
#print axioms CompletionWarrant.principal_mem
#print axioms CompletionWarrant.principal_le_iff
#print axioms CompletionWarrant.principal_mono
#print axioms CompletionWarrant.le_familyUnion
#print axioms CompletionWarrant.familyUnion_le
#print axioms CompletionWarrant.principalFamily_directed
#print axioms CompletionWarrant.union_principalFamily
#print axioms CompletionWarrant.admits_principal_iff
#print axioms CompletionWarrant.refutable_scottClosed
#print axioms CompletionWarrant.permitted_lower
#print axioms CompletionWarrant.scottClosed_iff_admits_permitted
#print axioms CompletionWarrant.admits_refutable
#print axioms CompletionWarrant.admits_scottClosed
#print axioms CompletionWarrant.scottClosed_refutable
#print axioms CompletionWarrant.finiteRefutable_iff_scottClosed
#print axioms CompletionWarrant.scottClosed_iff_lower_basis
#print axioms CompletionWarrant.finiteRefutable_iff_lower_basis
#print axioms CompletionWarrant.basis_eq_permitted
#print axioms CompletionWarrant.lower_basis_unique
#print axioms CompletionWarrant.permitted_eq_content
#print axioms CompletionWarrant.basis_eq_content
#print axioms CompletionWarrant.admits_empty
#print axioms CompletionWarrant.empty_scottClosed
#print axioms CompletionWarrant.empty_finiteRefutable
#print axioms CompletionWarrant.empty_content
#print axioms CompletionWarrant.content_lower
#print axioms CompletionWarrant.hull_scottClosed
#print axioms CompletionWarrant.hull_contains
#print axioms CompletionWarrant.hull_least
#print axioms CompletionWarrant.hull_preserves_content
#print axioms CompletionWarrant.hull_unique
#print axioms CompletionWarrant.avoiding_lower
#print axioms CompletionWarrant.respects_iff_admits_avoiding
#print axioms CompletionWarrant.respects_scottClosed
#print axioms CompletionWarrant.respects_finiteRefutable
#print axioms CompletionWarrant.respects_maximal
#print axioms CompletionWarrant.respects_principal
#print axioms CompletionWarrant.respects_unique
#print axioms CompletionWarrant.refutable_eq_admits
#print axioms CompletionWarrant.hull_joint_content
#print axioms CompletionWarrant.lift_admits
#print axioms CompletionWarrant.lift_restrict
#print axioms CompletionWarrant.restrict_lift
#print axioms CompletionWarrant.lift_order_iff
#print axioms CompletionWarrant.empty_lower_no_ideal
