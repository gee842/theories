import Std

/-!
Logical scope of the demand that every adequate philosophy be compatible with a
theory. A view is represented by the possibilities satisfying its claims, and
compatibility means an actual common satisfying possibility. This is a semantic
audit, not a definition of scientific standing, a proof that any physical or
ethical possibility is realized, or a discovery of the correct admissible class.
The quantified rival class in the converse contains all predicates, including
singletons; a restricted class of scientific philosophies needs a separate audit.
-/
namespace Generative.ScientificCompatibility

abbrev View (W : Type) := W → Prop

def Entails {W : Type} (p q : View W) : Prop := ∀ w, p w → q w

def Compatible {W : Type} (p q : View W) : Prop := ∃ w, p w ∧ q w

def MandatoryCompatibility {W : Type} (admissible theory : View W) : Prop :=
  ∀ rival : View W, (∃ w, admissible w ∧ rival w) → Compatible theory rival

theorem common_truth_gives_compatibility {W : Type} (p q : View W) (w : W)
    (hp : p w) (hq : q w) : Compatible p q := ⟨w, hp, hq⟩

theorem compatible_symmetric {W : Type} (p q : View W)
    (h : Compatible p q) : Compatible q p := by
  obtain ⟨w, hp, hq⟩ := h
  exact ⟨w, hq, hp⟩

theorem entailment_gives_mandatory_compatibility {W : Type}
    (admissible theory : View W) (h : Entails admissible theory) :
    MandatoryCompatibility admissible theory := by
  intro rival hw
  obtain ⟨w, ha, hr⟩ := hw
  exact ⟨w, h w ha, hr⟩

theorem mandatory_compatibility_requires_entailment {W : Type}
    (admissible theory : View W) (h : MandatoryCompatibility admissible theory) :
    Entails admissible theory := by
  intro w hw
  obtain ⟨v, ht, hv⟩ := h (fun v => v = w) ⟨w, hw, rfl⟩
  exact hv ▸ ht

theorem mandatory_compatibility_iff_entailment {W : Type}
    (admissible theory : View W) :
    MandatoryCompatibility admissible theory ↔ Entails admissible theory :=
  ⟨mandatory_compatibility_requires_entailment admissible theory,
   entailment_gives_mandatory_compatibility admissible theory⟩

-- A restricted rival inventory cannot inherit the singleton argument silently.
theorem one_compatible_rival_does_not_establish_mandatory_compatibility :
    Compatible (fun b : Bool => b = false) (fun _ => True) ∧
    ¬ MandatoryCompatibility (fun _ : Bool => True) (fun b => b = false) := by
  constructor
  · exact ⟨false, rfl, True.intro⟩
  · intro h
    have wrong := mandatory_compatibility_requires_entailment
      (fun _ : Bool => True) (fun b => b = false) h true True.intro
    cases wrong

theorem compatibility_does_not_require_accepting_theory :
    Compatible (fun _ : Bool => True) (fun b => b = false) ∧
    ¬ Entails (fun _ : Bool => True) (fun b => b = false) := by
  constructor
  · exact ⟨false, True.intro, rfl⟩
  · intro h
    have wrong := h true True.intro
    cases wrong

theorem common_error_can_be_compatible :
    Compatible (fun b : Bool => b = false) (fun b => b = false) ∧
    ¬ (true = false) := by
  exact ⟨⟨false, rfl, rfl⟩, by decide⟩

theorem full_package_requires_each_commitment {W : Type}
    (admissible core ethics : View W) :
    Entails admissible (fun w => core w ∧ ethics w) ↔
      Entails admissible core ∧ Entails admissible ethics := by
  constructor
  · intro h
    exact ⟨fun w hw => (h w hw).1, fun w hw => (h w hw).2⟩
  · intro h w hw
    exact ⟨h.1 w hw, h.2 w hw⟩

-- Genuine changed conclusions require a retained difference at the chosen
-- complete reading interface. This does not say that this interface is universal.
theorem changed_conclusion_requires_retained_difference {S E A : Type}
    (record : S → E) (read : E → A) (s t : S)
    (different : read (record s) ≠ read (record t)) : record s ≠ record t := by
  intro same
  exact different (congrArg read same)

theorem changed_conclusion_excludes_identity_update {S A : Type}
    (update : S → S) (read : S → A) (s : S)
    (different : read (update s) ≠ read s) : update s ≠ s := by
  intro same
  exact different (congrArg read same)

-- An atemporal relation can retain every step of a specified functional update.
-- Preservation does not select temporal becoming or a static ontology as primary.
def historyConstraint {S : Type} (update : S → S) (s t : S) : Prop := t = update s

theorem relational_presentation_preserves_update {S : Type}
    (update : S → S) (s t : S) : historyConstraint update s t ↔ t = update s := Iff.rfl

theorem relational_presentation_preserves_changed_conclusion {S A : Type}
    (update : S → S) (read : S → A) (s : S)
    (different : read (update s) ≠ read s) :
    ∃ t, historyConstraint update s t ∧ read t ≠ read s :=
  ⟨update s, rfl, different⟩

end Generative.ScientificCompatibility
