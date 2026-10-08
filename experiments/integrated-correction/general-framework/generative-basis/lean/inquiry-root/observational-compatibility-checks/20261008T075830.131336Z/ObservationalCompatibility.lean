import Std

/-!
Compatibility for rivals whose claims depend only on a specified inquiry
profile. A profile is an analytical projection within a complete configuration;
it is not a fundamentally separate observer or an exhaustive definition of
science. Admissibility, correspondence, and the proposed theory are supplied.
The finite witnesses are logical examples, not ethical countermodels.
-/
namespace Generative.ObservationalCompatibility

def Covers {W E : Type} (admissible theory : W → Prop) (profile : W → E) : Prop :=
  ∀ w, admissible w →
    ∃ v, admissible v ∧ profile v = profile w ∧ theory v

def MandatoryAtProfile {W E : Type}
    (admissible theory : W → Prop) (profile : W → E) : Prop :=
  ∀ claim : E → Prop, (∃ w, admissible w ∧ claim (profile w)) →
    ∃ v, admissible v ∧ theory v ∧ claim (profile v)

def ConstantOnProfiles {W E : Type}
    (admissible theory : W → Prop) (profile : W → E) : Prop :=
  ∀ v w, admissible v → admissible w → profile v = profile w →
    (theory v ↔ theory w)

theorem coverage_gives_compatibility {W E : Type}
    (admissible theory : W → Prop) (profile : W → E)
    (h : Covers admissible theory profile) :
    MandatoryAtProfile admissible theory profile := by
  intro claim witness
  obtain ⟨w, hw, hc⟩ := witness
  obtain ⟨v, hv, same, ht⟩ := h w hw
  exact ⟨v, hv, ht, same.symm ▸ hc⟩

theorem compatibility_requires_coverage {W E : Type}
    (admissible theory : W → Prop) (profile : W → E)
    (h : MandatoryAtProfile admissible theory profile) :
    Covers admissible theory profile := by
  intro w hw
  obtain ⟨v, hv, ht, same⟩ := h (fun e => e = profile w) ⟨w, hw, rfl⟩
  exact ⟨v, hv, same, ht⟩

theorem compatibility_iff_coverage {W E : Type}
    (admissible theory : W → Prop) (profile : W → E) :
    MandatoryAtProfile admissible theory profile ↔ Covers admissible theory profile :=
  ⟨compatibility_requires_coverage admissible theory profile,
   coverage_gives_compatibility admissible theory profile⟩

theorem universal_truth_gives_coverage {W E : Type}
    (admissible theory : W → Prop) (profile : W → E)
    (h : ∀ w, admissible w → theory w) : Covers admissible theory profile := by
  intro w hw
  exact ⟨w, hw, rfl, h w hw⟩

theorem coverage_and_constancy_give_universal_truth {W E : Type}
    (admissible theory : W → Prop) (profile : W → E)
    (cover : Covers admissible theory profile)
    (constant : ConstantOnProfiles admissible theory profile) :
    ∀ w, admissible w → theory w := by
  intro w hw
  obtain ⟨v, hv, same, ht⟩ := cover w hw
  exact (constant v w hv hw same).mp ht

theorem finer_coverage_gives_coarser_coverage {W E F : Type}
    (admissible theory : W → Prop) (fine : W → E) (coarsen : E → F)
    (h : Covers admissible theory fine) :
    Covers admissible theory (fun w => coarsen (fine w)) := by
  intro w hw
  obtain ⟨v, hv, same, ht⟩ := h w hw
  exact ⟨v, hv, congrArg coarsen same, ht⟩

-- A restriction on an unreported coordinate can meet every reported profile.
-- Giving the full pair as the profile exposes the excluded configuration.
theorem profile_coverage_can_hide_a_false_commitment :
    Covers (fun _ : Bool × Bool => True) (fun w => w.2 = false) Prod.fst ∧
    (¬ ∀ w : Bool × Bool, w.2 = false) ∧
    ¬ Covers (fun _ : Bool × Bool => True) (fun w => w.2 = false) id := by
  constructor
  · intro w _
    exact ⟨(w.1, false), True.intro, rfl, rfl⟩
  constructor
  · intro h
    have wrong := h (false, true)
    cases wrong
  · intro h
    obtain ⟨v, _, same, ht⟩ := h (false, true) True.intro
    change v = (false, true) at same
    have wrong : true = false := same ▸ ht
    cases wrong

-- Three elementary constraints are jointly incompatible although every pair
-- has a common realization. This checks the need for ONE full-package witness.
theorem pairwise_realizations_do_not_give_joint_realization :
    (∃ w : Bool × Bool, w.1 = false ∧ w.2 = false) ∧
    (∃ w : Bool × Bool, w.1 = false ∧ w.1 ≠ w.2) ∧
    (∃ w : Bool × Bool, w.2 = false ∧ w.1 ≠ w.2) ∧
    ¬ (∃ w : Bool × Bool, w.1 = false ∧ w.2 = false ∧ w.1 ≠ w.2) := by
  refine ⟨⟨(false, false), rfl, rfl⟩,
    ⟨(false, true), rfl, by decide⟩,
    ⟨(true, false), rfl, by decide⟩, ?_⟩
  intro h
  obtain ⟨w, hfirst, hsecond, hne⟩ := h
  exact hne (hfirst.trans hsecond.symm)

end Generative.ObservationalCompatibility
