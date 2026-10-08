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

/-- A small resource derivation calculus. Contraction is absent from its
constructors. Configurations serve as resource expressions; this is not a
complete propositional language or a derivation of the metatheory. -/
inductive Derives (P : Process S E) (join : S → S → S) : S → S → Prop
  | identity (s : S) : Derives P join s s
  | primitive {s t : S} {e : E} : P.step s e t → Derives P join s t
  | cut {s m t : S} : Derives P join s m → Derives P join m t → Derives P join s t
  | frame (g : S) {s t : S} : Derives P join s t →
      Derives P join (join g s) (join g t)

theorem derivation_sound {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) {s t : S} (h : Derives P join s t) : Reach P s t := by
  induction h with
  | identity s => exact reach_refl P s
  | primitive hs => exact reach_step P _ _ _ hs
  | cut _ _ ih₁ ih₂ => exact reach_trans P _ _ _ ih₁ ih₂
  | frame g _ ih => exact reach_frame hf g ih

theorem reach_derivable {P : Process S E} {join : S → S → S}
    {s t : S} (h : Reach P s t) : Derives P join s t := by
  obtain ⟨w, hw⟩ := h
  induction hw with
  | nil s => exact .identity s
  | cons hs _ ih => exact .cut (.primitive hs) ih

theorem derivation_iff_reach {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) (s t : S) : Derives P join s t ↔ Reach P s t :=
  ⟨derivation_sound hf, reach_derivable⟩

def AdmissibleContraction (P : Process S E) (join : S → S → S) (a : S) : Prop :=
  ∀ g c, Derives P join (join g (join a a)) c → Derives P join (join g a) c

theorem admissible_contraction_of_duplicate {P : Process S E} {join : S → S → S}
    (hf : StepFrame P join) {a : S} (h : Reach P a (join a a)) :
    AdmissibleContraction P join a := by
  intro g c hc
  exact reach_derivable (replacement_of_reach hf h g c (derivation_sound hf hc))

theorem duplicate_of_admissible_contraction {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) (hf : StepFrame P join)
    {a : S} (h : AdmissibleContraction P join a) : Reach P a (join a a) := by
  have hd : Derives P join (join unit (join a a)) (join a a) := by
    rw [hu]
    exact .identity _
  have hr := derivation_sound hf (h unit (join a a) hd)
  rw [hu] at hr
  exact hr

theorem admissible_contraction_iff_duplicate {P : Process S E} {join : S → S → S}
    (unit : S) (hu : ∀ x, join unit x = x) (hf : StepFrame P join) (a : S) :
    AdmissibleContraction P join a ↔ Reach P a (join a a) :=
  ⟨duplicate_of_admissible_contraction unit hu hf,
    admissible_contraction_of_duplicate hf⟩

end Generative.Logic

#print axioms Generative.Logic.reach_frame
#print axioms Generative.Logic.replacement_of_reach
#print axioms Generative.Logic.reach_of_replacement
#print axioms Generative.Logic.replacement_iff_reach
#print axioms Generative.Logic.contraction_iff_duplicate
#print axioms Generative.Logic.duplicate_finite
#print axioms Generative.Logic.contraction_finite
#print axioms Generative.Logic.derivation_sound
#print axioms Generative.Logic.reach_derivable
#print axioms Generative.Logic.derivation_iff_reach
#print axioms Generative.Logic.admissible_contraction_of_duplicate
#print axioms Generative.Logic.duplicate_of_admissible_contraction
#print axioms Generative.Logic.admissible_contraction_iff_duplicate
