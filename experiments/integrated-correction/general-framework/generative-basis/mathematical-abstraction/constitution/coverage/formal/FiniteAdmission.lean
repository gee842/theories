import FunctionGraphs

/-!
Full admission on a supplied finite carrier needs only finite admission.
This eliminates the infinitary closure premise at that scope, not the
background carrier, classical interpretation or finite-admission premise.
-/
namespace FiniteAdmission
open CompletionExamples PredicateAdmission FunctionGraphReconstruction
universe u v

variable {A : Type u} {B : Type v}

def FiniteCarrier (A : Type u) : Prop := ∃ l : List A, ∀ a, a ∈ l

def selections : List A → List (List A)
  | [] => [[]]
  | a :: l => selections l ++ (selections l).map (List.cons a)

theorem selection_represents (l : List A) (P : A → Prop) :
    ∃ s, s ∈ selections l ∧ ∀ a, a ∈ s ↔ a ∈ l ∧ P a := by
  classical
  induction l with
  | nil => exact ⟨[], by simp [selections], by simp⟩
  | cons a l ih =>
    obtain ⟨s, hs, hp⟩ := ih
    by_cases ha : P a
    · refine ⟨a :: s, ?_, ?_⟩
      · apply List.mem_append.mpr
        exact Or.inr (List.mem_map.mpr ⟨s, hs, rfl⟩)
      · intro x
        simp only [List.mem_cons, hp]
        constructor
        · intro h
          rcases h with h | h
          · exact ⟨Or.inl h, h ▸ ha⟩
          · exact ⟨Or.inr h.1, h.2⟩
        · rintro ⟨h, hx⟩
          exact h.elim Or.inl (fun hl => Or.inr ⟨hl, hx⟩)
    · refine ⟨s, List.mem_append.mpr (Or.inl hs), ?_⟩
      intro x
      rw [hp]
      constructor
      · exact fun h => ⟨List.mem_cons.mpr (Or.inr h.1), h.2⟩
      · rintro ⟨hx, hp⟩
        rcases List.mem_cons.mp hx with hx | hx
        · exact False.elim (ha (hx ▸ hp))
        · exact ⟨hx, hp⟩

theorem finite_domain_family_complete (l : List A) (h : ∀ a, a ∈ l) (P : A → Prop) :
    ∃ s, s ∈ selections l ∧ ∀ a, a ∈ s ↔ P a := by
  obtain ⟨s, hs, hp⟩ := selection_represents l P
  exact ⟨s, hs, fun a => (hp a).trans ⟨And.right, fun ha => ⟨h a, ha⟩⟩⟩

theorem finite_total (h : FiniteCarrier A) : Finite (fun _ : A => True) := by
  obtain ⟨l, hl⟩ := h
  exact ⟨l, fun a => ⟨fun _ => hl a, fun _ => True.intro⟩⟩

theorem predicate_finite (h : FiniteCarrier A) (P : A → Prop) : Finite P :=
  finite_subset (finite_total h) (fun _ _ => True.intro)

theorem finite_carrier_iff_all_predicates_finite :
    FiniteCarrier A ↔ ∀ P : A → Prop, Finite P := by
  constructor
  · exact predicate_finite
  · intro h
    obtain ⟨l, hl⟩ := h (fun _ => True)
    exact ⟨l, fun a => (hl a).mp True.intro⟩

theorem full_of_finite (h : FiniteCarrier A) (C : (A → Prop) → Prop)
    (hf : IncludesFinite C) : Full C := by
  intro P
  exact hf ⟨P, predicate_finite h P⟩

theorem full_iff_finite (h : FiniteCarrier A) (C : (A → Prop) → Prop) :
    Full C ↔ IncludesFinite C :=
  ⟨fun hf F => hf F.mem, full_of_finite h C⟩

theorem list_admitted (C : (A → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ a, C (fun x => x = a))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) (l : List A) :
    C (fun a => a ∈ l) := by
  induction l with
  | nil =>
    have h : (fun a : A => a ∈ ([] : List A)) = (fun _ => False) := by
      funext a
      exact propext (by simp)
    rwa [h]
  | cons a l ih =>
    have h : (fun x => x ∈ a :: l) = BinaryUnion (fun x => x = a) (fun x => x ∈ l) := by
      funext x
      exact propext (by simp [BinaryUnion])
    rw [h]
    exact hu _ _ (hs a) ih

theorem finite_admission_of_formation (C : (A → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ a, C (fun x => x = a))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : IncludesFinite C := by
  intro F
  obtain ⟨l, hl⟩ := F.finite
  have h : F.mem = (fun a => a ∈ l) := funext (fun a => propext (hl a))
  rw [h]
  exact list_admitted C he hs hu l

theorem full_of_finite_formation (h : FiniteCarrier A) (C : (A → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ a, C (fun x => x = a))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : Full C :=
  full_of_finite h C (finite_admission_of_formation C he hs hu)

theorem directed_closure_of_finite (h : FiniteCarrier A) (C : (A → Prop) → Prop)
    (hf : IncludesFinite C) : DirectedUnionClosed C :=
  (full_iff_finite_directed C).mp (full_of_finite h C hf) |>.2

theorem graph_finite (h : FiniteCarrier A) (f : A → B) : Finite (graph f) := by
  obtain ⟨l, hl⟩ := h
  refine ⟨l.map (fun a => (a, f a)), ?_⟩
  intro p
  constructor
  · intro hp
    apply List.mem_map.mpr
    exact ⟨p.1, hl p.1, Prod.ext rfl hp⟩
  · intro hp
    obtain ⟨a, _, ha⟩ := List.mem_map.mp hp
    cases ha
    rfl

theorem function_graph_admitted (h : FiniteCarrier A)
    (C : (A × B → Prop) → Prop) (hf : IncludesFinite C) (f : A → B) : C (graph f) :=
  hf ⟨graph f, graph_finite h f⟩

theorem bool_finite : FiniteCarrier Bool := by
  refine ⟨[false, true], ?_⟩
  intro a
  cases a <;> simp

theorem nat_not_finite : ¬ FiniteCarrier Nat := by
  intro h
  exact even_not_finite (predicate_finite h Even)

theorem predicates_finite (h : FiniteCarrier A) : FiniteCarrier (A → Prop) := by
  obtain ⟨l, hl⟩ := h
  refine ⟨(selections l).map (fun s a => a ∈ s), ?_⟩
  intro P
  obtain ⟨s, hs, hp⟩ := finite_domain_family_complete l hl P
  exact List.mem_map.mpr ⟨s, hs, funext (fun a => propext (hp a))⟩

noncomputable def update (f : A → B) (a : A) (b : B) : A → B := by
  classical
  exact fun x => if x = a then b else f x

noncomputable def assignments (values : List B) (seed : A → B) : List A → List (A → B)
  | [] => [seed]
  | a :: l => (assignments values seed l).flatMap (fun f => values.map (update f a))

theorem assignments_cover (values : List B) (hv : ∀ b, b ∈ values)
    (seed target : A → B) (l : List A) :
    ∃ f, f ∈ assignments values seed l ∧ ∀ a, a ∈ l → f a = target a := by
  classical
  induction l with
  | nil => exact ⟨seed, by simp [assignments], by simp⟩
  | cons a l ih =>
    obtain ⟨f, hf, he⟩ := ih
    refine ⟨update f a (target a), ?_, ?_⟩
    · apply List.mem_flatMap.mpr
      exact ⟨f, hf, List.mem_map.mpr ⟨target a, hv _, rfl⟩⟩
    · intro x hx
      by_cases hxa : x = a
      · simp [update, hxa]
      · have hxl : x ∈ l := (List.mem_cons.mp hx).resolve_left hxa
        simpa [update, hxa] using he x hxl

theorem functions_finite (ha : FiniteCarrier A) (hb : FiniteCarrier B) :
    FiniteCarrier (A → B) := by
  classical
  by_cases hex : ∃ f : A → B, True
  · obtain ⟨seed, _⟩ := hex
    obtain ⟨args, ha⟩ := ha
    obtain ⟨values, hb⟩ := hb
    refine ⟨assignments values seed args, ?_⟩
    intro target
    obtain ⟨f, hf, he⟩ := assignments_cover values hb seed target args
    have h : f = target := funext (fun a => he a (ha a))
    exact h ▸ hf
  · exact ⟨[], fun f => False.elim (hex ⟨f, True.intro⟩)⟩

theorem direct_type_finite (h : FiniteCarrier A) :
    ∀ t : TypedTruth.Ty, FiniteCarrier (TypedTruth.Direct A t)
  | .base => h
  | .arr s t => functions_finite (direct_type_finite h s) (direct_type_finite h t)
  | .pred s => predicates_finite (direct_type_finite h s)

theorem finite_type_full_admission (h : FiniteCarrier A) (t : TypedTruth.Ty)
    (C : (TypedTruth.Direct A t → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ a, C (fun x => x = a))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : Full C :=
  full_of_finite_formation (direct_type_finite h t) C he hs hu

theorem finite_transport (e : TypedTruth.BiMap A B) (h : FiniteCarrier A) : FiniteCarrier B := by
  obtain ⟨l, hl⟩ := h
  refine ⟨l.map e.forward, ?_⟩
  intro b
  exact List.mem_map.mpr ⟨e.backward b, hl _, e.forward_backward b⟩

theorem completed_type_finite (h : FiniteCarrier A) (t : TypedTruth.Ty) :
    FiniteCarrier (GraphCompleted A t) :=
  finite_transport (graphTypeMap (TypedTruth.identity A) t) (direct_type_finite h t)

theorem completed_type_full_admission (h : FiniteCarrier A) (t : TypedTruth.Ty)
    (C : (GraphCompleted A t → Prop) → Prop)
    (he : C (fun _ => False)) (hs : ∀ a, C (fun x => x = a))
    (hu : ∀ P Q, C P → C Q → C (BinaryUnion P Q)) : Full C :=
  full_of_finite_formation (completed_type_finite h t) C he hs hu

end FiniteAdmission
