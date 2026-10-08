import GeneratedPaths

/-!
Resource contraction for the existing process root. The context operation,
its left unit and primitive frame compatibility are explicit local inputs.
No logical syntax, classical reasoning, or physical interpretation is derived.
-/
namespace Generative.Logic
open Generative.Deeper
universe u v
variable {S : Type u} {E : Type v}

def StepFrame (P : Process S E) (join : S → S → S) : Prop :=
  ∀ g s e t, P.step s e t → P.step (join g s) e (join g t)

theorem reach_frame {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) (g : S) {s t : S} (h : Reach P s t) :
    Reach P (join g s) (join g t) :=
  reach_evaluate (reach_refl P) (reach_trans P)
    (fun s e t hs => reach_step P _ _ _ (hf g s e t hs)) h

/-- Every endpoint continuation available after y is available after x,
uniformly in an explicitly declared left context. -/
def Replacement (P : Process S E) (join : S → S → S) (x y : S) : Prop :=
  ∀ g c, Reach P (join g y) c → Reach P (join g x) c

theorem replacement_of_reach {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) {x y : S} (h : Reach P x y) :
    Replacement P join x y := by
  intro g c hc
  exact reach_trans P _ _ _ (reach_frame hf g h) hc

theorem reach_of_replacement {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) {x y : S}
    (h : Replacement P join x y) : Reach P x y := by
  have hy : Reach P (join unit y) y := by
    rw [hu]
    exact reach_refl P y
  have hx := h unit y hy
  rw [hu] at hx
  exact hx

theorem replacement_iff_reach {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) (hf : StepFrame P join) (x y : S) :
    Replacement P join x y ↔ Reach P x y :=
  ⟨reach_of_replacement unit hu, replacement_of_reach hf⟩

def Contraction (P : Process S E) (join : S → S → S) (a : S) : Prop :=
  Replacement P join a (join a a)

theorem contraction_iff_duplicate {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) (hf : StepFrame P join) (a : S) :
    Contraction P join a ↔ Reach P a (join a a) :=
  replacement_iff_reach unit hu hf a (join a a)

def Copies (join : S → S → S) (a : S) : Nat → S
  | 0 => a
  | n + 1 => join a (Copies join a n)

/-- Binary duplication supports any finite positive multiplicity. No infinite
execution, scheduling guarantee, or exponential promotion is asserted. -/
theorem duplicate_finite {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) {a : S} (h : Reach P a (join a a)) (n : Nat) :
    Reach P a (Copies join a n) := by
  induction n with
  | zero => exact reach_refl P a
  | succ n ih =>
    exact reach_trans P _ _ _ h (reach_frame hf a ih)

theorem contraction_finite {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) (hf : StepFrame P join)
    {a : S} (h : Contraction P join a) (n : Nat) :
    Replacement P join a (Copies join a n) :=
  replacement_of_reach hf
    (duplicate_finite hf ((contraction_iff_duplicate unit hu hf a).mp h) n)

end Generative.Logic

#print axioms Generative.Logic.reach_frame
#print axioms Generative.Logic.replacement_of_reach
#print axioms Generative.Logic.reach_of_replacement
#print axioms Generative.Logic.replacement_iff_reach
#print axioms Generative.Logic.contraction_iff_duplicate
#print axioms Generative.Logic.duplicate_finite
#print axioms Generative.Logic.contraction_finite
