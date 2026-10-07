import CompletionExamples

/-!
Full predicate admission is equivalent to finite admission plus closure under
every ambient nonempty directed union. The family quantifier is unrestricted.
Finite-or-cofinite predicates provide a proper, finitely closed comparison.
This checks and refines the earlier closure argument; no metaphysical priority
or independent warrant for the unrestricted family range is established.
-/
namespace PredicateAdmission
open CompletionWarrant CompletionExamples
universe u v

def Included (P Q : A → Prop) : Prop := ∀ a, P a → Q a

def PredicateUnion (D : (A → Prop) → Prop) : A → Prop := fun a => ∃ P, D P ∧ P a

structure NonemptyDirected (D : (A → Prop) → Prop) : Prop where
  nonempty : ∃ P, D P
  directed : ∀ P Q, D P → D Q → ∃ R, D R ∧ Included P R ∧ Included Q R

def IncludesFinite (C : (A → Prop) → Prop) : Prop := ∀ F : FinitePart A, C F.mem

def DirectedUnionClosed (C : (A → Prop) → Prop) : Prop :=
  ∀ D : (A → Prop) → Prop, NonemptyDirected D →
    (∀ P, D P → C P) → C (PredicateUnion D)

def Full (C : (A → Prop) → Prop) : Prop := ∀ P, C P

def FiniteProfiles (S : A → Prop) : (A → Prop) → Prop :=
  fun P => ∃ F : FinitePart A, P = F.mem ∧ (partsOf S).mem F

theorem finiteProfiles_directed (S : A → Prop) : NonemptyDirected (FiniteProfiles S) := by
  constructor
  · exact ⟨(emptyPart A).mem, emptyPart A, rfl, fun _ h => False.elim h⟩
  · rintro P Q ⟨F, rfl, hF⟩ ⟨G, rfl, hG⟩
    obtain ⟨H, hH, hFH, hGH⟩ := (partsOf S).directed hF hG
    exact ⟨H.mem, ⟨H, rfl, hH⟩, hFH, hGH⟩

theorem union_finiteProfiles (S : A → Prop) : PredicateUnion (FiniteProfiles S) = S := by
  funext a
  apply propext
  constructor
  · rintro ⟨P, ⟨F, rfl, hF⟩, ha⟩
    exact hF a ha
  · intro ha
    refine ⟨(singletonPart a).mem, ⟨singletonPart a, rfl, ?_⟩, rfl⟩
    intro b hb
    exact hb ▸ ha

theorem finiteProfiles_admitted (C : (A → Prop) → Prop) (hc : IncludesFinite C)
    (S P : A → Prop) (hP : FiniteProfiles S P) : C P := by
  obtain ⟨F, rfl, _⟩ := hP
  exact hc F

theorem full_of_finite_directed (C : (A → Prop) → Prop)
    (hf : IncludesFinite C) (hd : DirectedUnionClosed C) : Full C := by
  intro S
  have h := hd (FiniteProfiles S) (finiteProfiles_directed S)
    (fun P hP => finiteProfiles_admitted C hf S P hP)
  rwa [union_finiteProfiles] at h

theorem full_iff_finite_directed (C : (A → Prop) → Prop) :
    Full C ↔ IncludesFinite C ∧ DirectedUnionClosed C := by
  constructor
  · intro h
    exact ⟨fun F => h F.mem, fun D _ _ => h (PredicateUnion D)⟩
  · intro h
    exact full_of_finite_directed C h.1 h.2

theorem directed_iff_full_given_finite (C : (A → Prop) → Prop) (hf : IncludesFinite C) :
    DirectedUnionClosed C ↔ Full C :=
  ⟨full_of_finite_directed C hf, fun h => (full_iff_finite_directed C).mp h |>.2⟩

def Finite (P : A → Prop) : Prop := ∃ l : List A, ∀ a, P a ↔ a ∈ l

def Complement (P : A → Prop) : A → Prop := fun a => ¬ P a

def BinaryUnion (P Q : A → Prop) : A → Prop := fun a => P a ∨ Q a

def FiniteOrCofinite (P : A → Prop) : Prop := Finite P ∨ Finite (Complement P)

theorem finite_congr {P Q : A → Prop} (h : ∀ a, P a ↔ Q a) : Finite P ↔ Finite Q := by
  constructor
  · rintro ⟨l, hl⟩
    exact ⟨l, fun a => (h a).symm.trans (hl a)⟩
  · rintro ⟨l, hl⟩
    exact ⟨l, fun a => (h a).trans (hl a)⟩

theorem finite_empty : Finite (fun _ : A => False) := ⟨[], by simp⟩

theorem finite_singleton (a : A) : Finite (fun b => b = a) := ⟨[a], by simp⟩

theorem finite_subset {P Q : A → Prop} (hQ : Finite Q) (hpq : Included P Q) : Finite P := by
  classical
  obtain ⟨l, hl⟩ := hQ
  refine ⟨l.filter (fun a => decide (P a)), ?_⟩
  intro a
  simp only [List.mem_filter, decide_eq_true_eq]
  exact ⟨fun h => ⟨(hl a).mp (hpq a h), h⟩, fun h => h.2⟩

theorem finite_union {P Q : A → Prop} (hP : Finite P) (hQ : Finite Q) :
    Finite (BinaryUnion P Q) := by
  obtain ⟨l, hl⟩ := hP
  obtain ⟨m, hm⟩ := hQ
  exact ⟨l ++ m, fun a => by simp [BinaryUnion, hl a, hm a]⟩

theorem finiteOrCofinite_includes_finite : IncludesFinite (FiniteOrCofinite (A := A)) :=
  fun F => Or.inl F.finite

theorem finiteOrCofinite_empty : FiniteOrCofinite (fun _ : A => False) :=
  Or.inl finite_empty

theorem finiteOrCofinite_full : FiniteOrCofinite (fun _ : A => True) :=
  Or.inr ⟨[], fun _ => by simp [Complement]⟩

theorem finiteOrCofinite_singleton (a : A) : FiniteOrCofinite (fun b => b = a) :=
  Or.inl (finite_singleton a)

theorem finiteOrCofinite_complement {P : A → Prop} (h : FiniteOrCofinite P) :
    FiniteOrCofinite (Complement P) := by
  classical
  rcases h with h | h
  · right
    exact (finite_congr (fun a => show (¬ ¬ P a) ↔ P a from
      ⟨fun hn => Classical.byContradiction hn, fun hp hn => hn hp⟩)).mpr h
  · exact Or.inl h

theorem finiteOrCofinite_union {P Q : A → Prop}
    (hP : FiniteOrCofinite P) (hQ : FiniteOrCofinite Q) :
    FiniteOrCofinite (BinaryUnion P Q) := by
  rcases hP with hP | hP
  · rcases hQ with hQ | hQ
    · exact Or.inl (finite_union hP hQ)
    · exact Or.inr (finite_subset hQ (fun a h hq => h (Or.inr hq)))
  · exact Or.inr (finite_subset hP (fun a h hp => h (Or.inl hp)))

theorem finite_pattern (S : A → Prop) (l : List A) :
    ∃ P, Finite P ∧ ∀ a, a ∈ l → (P a ↔ S a) := by
  refine ⟨fun a => a ∈ l ∧ S a, ?_, ?_⟩
  · exact finite_subset ⟨l, fun _ => Iff.rfl⟩ (fun _ h => h.1)
  · intro a ha
    exact ⟨fun h => h.2, fun h => ⟨ha, h⟩⟩

theorem finiteOrCofinite_pattern (S : A → Prop) (l : List A) :
    ∃ P, FiniteOrCofinite P ∧ ∀ a, a ∈ l → (P a ↔ S a) := by
  obtain ⟨P, hP, h⟩ := finite_pattern S l
  exact ⟨P, Or.inl hP, h⟩

def Image (f : A → B) (P : A → Prop) : B → Prop := fun b => ∃ a, P a ∧ f a = b

def Bijective (f : A → B) : Prop := Function.Injective f ∧ Function.Surjective f

theorem finite_image (f : A → B) {P : A → Prop} (h : Finite P) : Finite (Image f P) := by
  obtain ⟨l, hl⟩ := h
  refine ⟨l.map f, ?_⟩
  intro b
  constructor
  · rintro ⟨a, ha, rfl⟩
    exact List.mem_map.mpr ⟨a, (hl a).mp ha, rfl⟩
  · intro hb
    obtain ⟨a, ha, hab⟩ := List.mem_map.mp hb
    exact ⟨a, (hl a).mpr ha, hab⟩

theorem bijective_image_complement (f : A → B) (hf : Bijective f)
    (P : A → Prop) (b : B) : Image f (Complement P) b ↔ Complement (Image f P) b := by
  constructor
  · rintro ⟨a, ha, hab⟩ ⟨c, hc, hcb⟩
    have hca : c = a := hf.1 (hcb.trans hab.symm)
    exact ha (hca ▸ hc)
  · intro hb
    obtain ⟨a, hab⟩ := hf.2 b
    exact ⟨a, fun ha => hb ⟨a, ha, hab⟩, hab⟩

theorem finiteOrCofinite_bijective_image (f : A → B) (hf : Bijective f)
    {P : A → Prop} (h : FiniteOrCofinite P) : FiniteOrCofinite (Image f P) := by
  rcases h with h | h
  · exact Or.inl (finite_image f h)
  · exact Or.inr ((finite_congr (bijective_image_complement f hf P)).mp (finite_image f h))

noncomputable def inverse (f : A → B) (hf : Bijective f) : B → A :=
  fun b => Classical.choose (hf.2 b)

theorem inverse_right (f : A → B) (hf : Bijective f) (b : B) : f (inverse f hf b) = b :=
  Classical.choose_spec (hf.2 b)

theorem inverse_left (f : A → B) (hf : Bijective f) (a : A) : inverse f hf (f a) = a :=
  hf.1 (inverse_right f hf (f a))

theorem inverse_bijective (f : A → B) (hf : Bijective f) : Bijective (inverse f hf) := by
  constructor
  · intro a b h
    have hh := congrArg f h
    simpa only [inverse_right] using hh
  · exact fun a => ⟨f a, inverse_left f hf a⟩

theorem image_inverse (f : A → B) (hf : Bijective f) (P : A → Prop) :
    Image (inverse f hf) (Image f P) = P := by
  funext a
  apply propext
  constructor
  · rintro ⟨b, ⟨c, hc, hcb⟩, hba⟩
    have hca : c = a := by simpa only [← hcb, inverse_left] using hba
    exact hca ▸ hc
  · intro ha
    exact ⟨f a, ⟨a, ha, rfl⟩, inverse_left f hf a⟩

theorem finiteOrCofinite_bijection_iff (f : A → B) (hf : Bijective f) (P : A → Prop) :
    FiniteOrCofinite (Image f P) ↔ FiniteOrCofinite P := by
  constructor
  · intro h
    have hi := finiteOrCofinite_bijective_image (inverse f hf) (inverse_bijective f hf) h
    rwa [image_inverse] at hi
  · exact finiteOrCofinite_bijective_image f hf

def listBound : List Nat → Nat
  | [] => 0
  | a :: l => Nat.max a (listBound l)

theorem member_le_bound (l : List Nat) (a : Nat) (h : a ∈ l) : a ≤ listBound l := by
  induction l with
  | nil => simp at h
  | cons b l ih =>
    rcases List.mem_cons.mp h with rfl | h
    · exact Nat.le_max_left _ _
    · exact Nat.le_trans (ih h) (Nat.le_max_right _ _)

def Even (n : Nat) : Prop := n % 2 = 0

theorem even_not_finite : ¬ Finite Even := by
  rintro ⟨l, hl⟩
  have he : Even (2 * (listBound l + 1)) := by unfold Even; omega
  have hb := member_le_bound l _ ((hl _).mp he)
  omega

theorem even_complement_not_finite : ¬ Finite (Complement Even) := by
  rintro ⟨l, hl⟩
  have ho : Complement Even (2 * (listBound l + 1) + 1) := by
    unfold Complement Even
    omega
  have hb := member_le_bound l _ ((hl _).mp ho)
  omega

theorem even_not_admitted : ¬ FiniteOrCofinite Even :=
  fun h => h.elim even_not_finite even_complement_not_finite

theorem finiteOrCofinite_not_full : ¬ Full (FiniteOrCofinite (A := Nat)) :=
  fun h => even_not_admitted (h Even)

theorem finiteOrCofinite_not_directed_closed :
    ¬ DirectedUnionClosed (FiniteOrCofinite (A := Nat)) := by
  intro h
  exact finiteOrCofinite_not_full (full_of_finite_directed _ finiteOrCofinite_includes_finite h)

theorem parity_directed_failure :
    NonemptyDirected (FiniteProfiles Even) ∧
      (∀ P, FiniteProfiles Even P → FiniteOrCofinite P) ∧
      ¬ FiniteOrCofinite (PredicateUnion (FiniteProfiles Even)) := by
  refine ⟨finiteProfiles_directed Even,
    fun P hP => finiteProfiles_admitted _ finiteOrCofinite_includes_finite Even P hP, ?_⟩
  rw [union_finiteProfiles]
  exact even_not_admitted

end PredicateAdmission
