import FiniteAdmission

/-!
Finite dependent domains and the strength of arbitrary fiber specification.
The base and the whole fiber assignment are supplied. Finiteness of each fiber
alone is not a restriction on the predicate encoded by nonempty fibers.
-/
namespace FamilyAdmission
open FiniteAdmission PredicateAdmission TypedTruth
universe u v w

variable {A : Type u} {B : A → Type v}

theorem finite_of_injective {X : Type u} {Y : Type v}
    (f : X → Y) (hinj : ∀ x y, f x = f y → x = y)
    (hy : FiniteCarrier Y) : FiniteCarrier X := by
  classical
  by_cases hx : Nonempty X
  · obtain ⟨x₀⟩ := hx
    obtain ⟨l, hl⟩ := hy
    let g : Y → X := fun y =>
      if h : ∃ x, f x = y then Classical.choose h else x₀
    have hg : ∀ x, g (f x) = x := by
      intro x
      dsimp [g]
      rw [dif_pos ⟨x, rfl⟩]
      exact hinj _ _ (Classical.choose_spec (show ∃ z, f z = f x from ⟨x, rfl⟩))
    exact ⟨l.map g, fun x => List.mem_map.mpr ⟨f x, hl (f x), hg x⟩⟩
  · exact ⟨[], fun x => False.elim (hx ⟨x⟩)⟩

theorem sigma_finite (ha : FiniteCarrier A)
    (hb : ∀ a, FiniteCarrier (B a)) : FiniteCarrier (Sigma B) := by
  classical
  obtain ⟨l, hl⟩ := ha
  let fibers : (a : A) → List (B a) := fun a => Classical.choose (hb a)
  have hf : ∀ a b, b ∈ fibers a := fun a => Classical.choose_spec (hb a)
  refine ⟨l.flatMap (fun a => (fibers a).map (Sigma.mk a)), ?_⟩
  rintro ⟨a, b⟩
  exact List.mem_flatMap.mpr ⟨a, hl a, List.mem_map.mpr ⟨b, hf a b, rfl⟩⟩

theorem sections_finite (ha : FiniteCarrier A)
    (hb : ∀ a, FiniteCarrier (B a)) : FiniteCarrier ((a : A) → B a) := by
  apply finite_of_injective (fun f a => (⟨a, f a⟩ : Sigma B))
  · intro f g h
    funext a
    have he := congrFun h a
    exact eq_of_heq (Sigma.mk.inj he).2
  · exact functions_finite ha (sigma_finite ha hb)

theorem finite_sigma_full_admission (ha : FiniteCarrier A)
    (hb : ∀ a, FiniteCarrier (B a)) (C : (Sigma B → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ x, C (fun y => y = x))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : Full C :=
  full_of_finite_formation (sigma_finite ha hb) C he hs hu

theorem finite_sections_full_admission (ha : FiniteCarrier A)
    (hb : ∀ a, FiniteCarrier (B a)) (C : (((a : A) → B a) → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ x, C (fun y => y = x))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : Full C :=
  full_of_finite_formation (sections_finite ha hb) C he hs hu

def support (B : A → Type v) : A → Prop := fun a => Nonempty (B a)

def truthFibers (P : A → Prop) (a : A) : Type := PLift (P a)

theorem truthFibers_subsingleton (P : A → Prop) (a : A) :
    Subsingleton (truthFibers P a) :=
  ⟨fun x y => by cases x; cases y; rfl⟩

theorem truthFibers_finite (P : A → Prop) (a : A) :
    FiniteCarrier (truthFibers P a) := by
  classical
  by_cases h : P a
  · exact ⟨[⟨h⟩], fun x => by cases x; simp⟩
  · exact ⟨[], fun x => False.elim (h x.down)⟩

theorem support_truthFibers (P : A → Prop) : support (truthFibers P) = P := by
  funext a
  apply propext
  exact ⟨fun ⟨x⟩ => x.down, fun h => ⟨⟨h⟩⟩⟩

theorem full_iff_subsingleton_support (C : (A → Prop) → Prop) :
    Full C ↔ ∀ B : A → Type, (∀ a, Subsingleton (B a)) → C (support B) := by
  constructor
  · exact fun h B _ => h (support B)
  · intro h P
    have hp := h (truthFibers P) (truthFibers_subsingleton P)
    rwa [support_truthFibers] at hp

theorem full_iff_finite_support (C : (A → Prop) → Prop) :
    Full C ↔ ∀ B : A → Type, (∀ a, FiniteCarrier (B a)) → C (support B) := by
  constructor
  · exact fun h B _ => h (support B)
  · intro h P
    have hp := h (truthFibers P) (truthFibers_finite P)
    rwa [support_truthFibers] at hp

/-- The predicate is recovered by projection of the supplied dependent domain. -/
def truthFamilyMap (P : A → Prop) : BiMap (Sigma (truthFibers P)) {a // P a} where
  forward x := ⟨x.1, x.2.down⟩
  backward x := ⟨x.1, ⟨x.2⟩⟩
  backward_forward x := by cases x; rfl
  forward_backward x := by cases x; rfl

theorem truthFamily_projection (P : A → Prop) (x : Sigma (truthFibers P)) :
    ((truthFamilyMap P).forward x).val = x.1 := rfl

/-- Pointwise nonemptiness concerns one section, not the admission of all sections. -/
theorem section_exists_iff (B : A → Type v) :
    Nonempty ((a : A) → B a) ↔ ∀ a, Nonempty (B a) := by
  constructor
  · exact fun ⟨f⟩ a => ⟨f a⟩
  · exact fun h => ⟨fun a => Classical.choice (h a)⟩

theorem singleton_fibers_infinite_total :
    (∀ _ : Nat, FiniteCarrier PUnit) ∧
      ¬ FiniteCarrier (Sigma (fun _ : Nat => PUnit)) := by
  constructor
  · intro _
    exact ⟨[PUnit.unit], fun x => by cases x; simp⟩
  · intro h
    apply nat_not_finite
    exact finite_of_injective (fun n : Nat => (⟨n, PUnit.unit⟩ : Sigma (fun _ : Nat => PUnit)))
      (fun _ _ he => congrArg Sigma.fst he) h

theorem boolean_fibers_infinite_sections :
    (∀ _ : Nat, FiniteCarrier Bool) ∧ ¬ FiniteCarrier (Nat → Bool) := by
  constructor
  · exact fun _ => bool_finite
  · intro h
    apply nat_not_finite
    apply finite_of_injective (fun n k : Nat => decide (k = n)) ?_ h
    intro n m he
    have hv := congrFun he n
    by_cases hn : n = m
    · exact hn
    · simp [hn] at hv

end FamilyAdmission
