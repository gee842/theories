import IndexedAssembly

/-!
Indexed assembly as extensional abstraction of an already supplied witness
relation. Whole witness domains and closure under the specified quotient and
inverse correspondence remain premises of object admission.
-/
namespace RelationalAssembly
universe u

variable {I A : Type u}

def Projection (R : I → A → Prop) : A → Prop := fun a => ∃ i, R i a

abbrev Witness (R : I → A → Prop) := {p : I × A // R p.1 p.2}

def witnessSetoid (R : I → A → Prop) : Setoid (Witness R) where
  r x y := x.val.2 = y.val.2
  iseqv := ⟨fun _ => rfl, fun h => h.symm, fun h k => h.trans k⟩

abbrev Assembly (R : I → A → Prop) := Quotient (witnessSetoid R)

abbrev Support (R : I → A → Prop) := {a : A // Projection R a}

def abstractWitness (R : I → A → Prop) (w : Witness R) : Assembly R :=
  Quotient.mk (witnessSetoid R) w

def output (R : I → A → Prop) : Assembly R → Support R :=
  Quotient.lift (fun w => ⟨w.val.2, w.val.1, w.property⟩)
    (fun _ _ h => Subtype.ext h)

theorem output_abstract (R : I → A → Prop) (w : Witness R) :
    (output R (abstractWitness R w)).val = w.val.2 := rfl

noncomputable def realize (R : I → A → Prop) (a : Support R) : Assembly R :=
  abstractWitness R ⟨(Classical.choose a.property, a.val),
    Classical.choose_spec a.property⟩

theorem output_realize (R : I → A → Prop) (a : Support R) :
    output R (realize R a) = a := by
  apply Subtype.ext
  rfl

theorem realize_output (R : I → A → Prop) (a : Assembly R) :
    realize R (output R a) = a := by
  induction a using Quotient.inductionOn with
  | h w =>
    apply Quotient.sound
    rfl

theorem output_injective (R : I → A → Prop) : Function.Injective (output R) := by
  intro x y h
  have hh := congrArg (realize R) h
  simpa only [realize_output] using hh

theorem output_surjective (R : I → A → Prop) : Function.Surjective (output R) :=
  fun a => ⟨realize R a, output_realize R a⟩

theorem abstract_eq_iff (R : I → A → Prop) (x y : Witness R) :
    abstractWitness R x = abstractWitness R y ↔ x.val.2 = y.val.2 := by
  constructor
  · intro h
    exact congrArg (fun a => (output R a).val) h
  · intro h
    exact Quotient.sound h

theorem projection_iff_output (R : I → A → Prop) (a : A) :
    Projection R a ↔ ∃ q : Assembly R, (output R q).val = a := by
  constructor
  · intro h
    exact ⟨realize R ⟨a, h⟩, congrArg Subtype.val (output_realize R ⟨a, h⟩)⟩
  · rintro ⟨q, hq⟩
    exact hq ▸ (output R q).property

theorem projected_content_unique (R : I → A → Prop) (P : A → Prop)
    (h : ∀ a, P a ↔ ∃ q : Assembly R, (output R q).val = a) :
    P = Projection R := by
  funext a
  exact propext ((h a).trans (projection_iff_output R a).symm)

theorem projection_reindex {J : Type u} (R : I → A → Prop) (f : J → I)
    (hf : Function.Surjective f) : Projection (fun j a => R (f j) a) = Projection R := by
  funext a
  apply propext
  constructor
  · rintro ⟨j, hj⟩
    exact ⟨f j, hj⟩
  · rintro ⟨i, hi⟩
    obtain ⟨j, rfl⟩ := hf i
    exact ⟨j, hi⟩

theorem parity_projection :
    Projection (fun n a => (IndexedAssembly.parityStages n).mem a) =
      PredicateAdmission.Even := IndexedAssembly.parity_union

theorem parity_iff_output (a : Nat) : PredicateAdmission.Even a ↔
    ∃ q : Assembly (fun n a => (IndexedAssembly.parityStages n).mem a),
      (output _ q).val = a := by
  rw [← parity_projection]
  exact projection_iff_output _ a

def OutputAbstractionClosed (C : (X : Type u) → (X → A) → Prop) : Prop :=
  ∀ {I : Type u} (R : I → A → Prop),
    C (Witness R) (fun w => w.val.2) →
    C (Assembly R) (fun q => (output R q).val)

def CorrespondenceClosed (C : (X : Type u) → (X → A) → Prop) : Prop :=
  ∀ {X Y : Type u} (f : X → Y) (g : Y → X) (vx : X → A) (vy : Y → A),
    (∀ x, g (f x) = x) → (∀ y, f (g y) = y) →
    (∀ x, vy (f x) = vx x) → C X vx → C Y vy

theorem support_admitted (C : (X : Type u) → (X → A) → Prop)
    (hq : OutputAbstractionClosed C) (he : CorrespondenceClosed C)
    (R : I → A → Prop) (hw : C (Witness R) (fun w => w.val.2)) :
    C (Support R) Subtype.val :=
  he (output R) (realize R) (fun q => (output R q).val) Subtype.val
    (realize_output R) (output_realize R) (fun _ => rfl) (hq R hw)

end RelationalAssembly
