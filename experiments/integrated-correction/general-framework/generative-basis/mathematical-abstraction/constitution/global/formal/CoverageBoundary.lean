import Std -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Diagonal.fixed_of_complete`, `Becoming.Diagonal.claims_incomplete` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-!
Checked limits on one fixed self-indexed representation family.
These are ordinary diagonal arguments, not a no-go for generative ontology,
external semantics, indexed hierarchies, or all meaningful mathematical truth.
The complete predicate/function space is explicit in the coverage hypotheses.
-/
namespace RootCoverageBoundary

def PointwiseComplete {A : Type u} {Y : Type v} (E : A → A → Y) : Prop :=
  ∀ f : A → Y, ∃ a, ∀ x, E a x = f x

/-- Set/function specialization of the Lawvere diagonal fixed-point theorem. -/
theorem fixed_point_of_complete {A : Type u} {Y : Type v}
    (E : A → A → Y) (complete : PointwiseComplete E) (g : Y → Y) :
    ∃ y, g y = y := by
  obtain ⟨a, ha⟩ := complete (fun x => g (E x x))
  exact ⟨E a a, (ha a).symm⟩

theorem no_complete_fixedpoint_free {A : Type u} {Y : Type v}
    (E : A → A → Y) (g : Y → Y) (noFix : ∀ y, g y ≠ y) :
    ¬ PointwiseComplete E := by
  intro hc
  obtain ⟨y, hy⟩ := fixed_point_of_complete E hc g
  exact noFix y hy

def boolDiagonal {A : Type u} (E : A → A → Bool) (x : A) : Bool := !(E x x)

theorem bool_flip_no_fixed_point (b : Bool) : (!b) ≠ b := by
  cases b <;> decide

theorem bool_diagonal_unrepresented {A : Type u} (E : A → A → Bool) :
    ¬ ∃ a, ∀ x, E a x = boolDiagonal E x := by
  rintro ⟨a, ha⟩
  exact bool_flip_no_fixed_point (E a a) (ha a).symm

theorem no_full_bool_coverage {A : Type u} (E : A → A → Bool) :
    ¬ PointwiseComplete E :=
  no_complete_fixedpoint_free E (fun b => !b) bool_flip_no_fixed_point

def Represents {C : Type u} {X : Type v} (E : C → X → Prop)
    (c : C) (P : X → Prop) : Prop := ∀ x, E c x ↔ P x

def CoversPredicates {C : Type u} {X : Type v} (E : C → X → Prop) : Prop :=
  ∀ P : X → Prop, ∃ c, Represents E c P

def predicateDiagonal {A : Type u} (E : A → A → Prop) (x : A) : Prop := ¬ E x x

theorem no_iff_neg (P : Prop) : ¬ (P ↔ ¬ P) := by
  intro h
  have hn : ¬ P := fun hp => (h.mp hp) hp
  exact hn (h.mpr hn)

theorem predicate_diagonal_unrepresented {A : Type u} (E : A → A → Prop) :
    ¬ ∃ a, Represents E a (predicateDiagonal E) := by
  rintro ⟨a, ha⟩
  exact no_iff_neg (E a a) (ha a)

theorem no_full_predicate_coverage {A : Type u} (E : A → A → Prop) :
    ¬ CoversPredicates E := by
  intro hc
  exact predicate_diagonal_unrepresented E (hc (predicateDiagonal E))

/-- It already suffices that the declared family includes its own diagonal.
This is narrower than requiring every externally specified predicate. -/
theorem no_diagonal_closed_complete_family {A : Type u} (E : A → A → Prop)
    (admissible : (A → Prop) → Prop)
    (includesDiagonal : admissible (predicateDiagonal E))
    (covers : ∀ P, admissible P → ∃ a, Represents E a P) : False :=
  predicate_diagonal_unrepresented E (covers _ includesDiagonal)

/-- A larger description type can represent every predicate of a fixed lower
carrier. The full predicate type is supplied here, not derived from a root. -/
def externalReading (A : Type u) : (A → Prop) → A → Prop := fun P x => P x

theorem external_reading_covers (A : Type u) : CoversPredicates (externalReading A) :=
  fun P => ⟨P, fun _ => Iff.rfl⟩

/-- One explicitly added description covers a previously missing predicate,
while retaining every old description's meaning on the original query domain. -/
def extendReading {C : Type u} {X : Type v} (E : C → X → Prop)
    (P : X → Prop) : Option C → X → Prop
  | none, x => P x
  | some c, x => E c x

theorem extension_preserves {C : Type u} {X : Type v} (E : C → X → Prop)
    (P : X → Prop) (c : C) (x : X) : extendReading E P (some c) x ↔ E c x :=
  Iff.rfl

theorem extension_represents_new {C : Type u} {X : Type v} (E : C → X → Prop)
    (P : X → Prop) : Represents (extendReading E P) none P :=
  fun _ => Iff.rfl

theorem extension_preserves_coverage {C : Type u} {X : Type v}
    (E : C → X → Prop) (P Q : X → Prop) (h : ∃ c, Represents E c Q) :
    ∃ c, Represents (extendReading E P) c Q := by
  obtain ⟨c, hc⟩ := h
  exact ⟨some c, hc⟩

theorem diagonal_extension_strict {A : Type u} (E : A → A → Prop) :
    (∃ c, Represents (extendReading E (predicateDiagonal E)) c (predicateDiagonal E)) ∧
    ¬ (∃ a, Represents E a (predicateDiagonal E)) :=
  ⟨⟨none, extension_represents_new E (predicateDiagonal E)⟩,
    predicate_diagonal_unrepresented E⟩

end RootCoverageBoundary
