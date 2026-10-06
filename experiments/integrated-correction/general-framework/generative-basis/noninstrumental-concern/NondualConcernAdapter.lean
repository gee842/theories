import NondualCore
import GroundingContract

namespace NondualConcernAdapter

/- A situational ethical contract can be articulated through derived roles.
   Coverage is required to reflect it; leaving occurrences unnamed loses scope.
   Neither presentation nor covariance establishes this contract's truth. -/
def SituationContract {X : Type} (Adverse Opportunity Favor : X → Prop) : Prop :=
  ∀ x, Adverse x → Opportunity x → Favor x

theorem contract_pulls_back {X R : Type} (view : R → X)
    {A O F : X → Prop} (h : SituationContract A O F) :
    SituationContract (A ∘ view) (O ∘ view) (F ∘ view) := by
  intro r ha ho
  exact h (view r) ha ho

theorem covered_role_presentation_reflects_contract {X R : Type} (view : R → X)
    {A O F : X → Prop}
    (cover : ∀ x, A x → O x → ∃ r, view r = x)
    (h : SituationContract (A ∘ view) (O ∘ view) (F ∘ view)) :
    SituationContract A O F := by
  intro x ha ho
  obtain ⟨r,hr⟩ := cover x ha ho
  subst x
  exact h r ha ho

theorem covered_role_presentation_contract_iff {X R : Type} (view : R → X)
    {A O F : X → Prop} (cover : ∀ x, A x → O x → ∃ r, view r = x) :
    SituationContract A O F ↔ SituationContract (A ∘ view) (O ∘ view) (F ∘ view) :=
  ⟨contract_pulls_back view, covered_role_presentation_reflects_contract view cover⟩

theorem legacy_c2_is_situational_contract
    (Bad : NoninstrumentalConcern.PatientCondition → Prop)
    (Merit : NoninstrumentalConcern.State → NoninstrumentalConcern.Patient → Prop) :
    NoninstrumentalConcern.C2 Bad Merit ↔
      SituationContract
        (fun x : NoninstrumentalConcern.State × NoninstrumentalConcern.Patient =>
          Bad (NoninstrumentalConcern.condition x.1 x.2))
        (fun x => NoninstrumentalConcern.Eligible x.1 x.2)
        (fun x => Merit x.1 x.2) := by
  exact ⟨fun h x => h x.1 x.2,fun h s patient => h (s,patient)⟩

end NondualConcernAdapter

#print axioms NondualConcernAdapter.legacy_c2_is_situational_contract

#print axioms NondualConcernAdapter.contract_pulls_back
#print axioms NondualConcernAdapter.covered_role_presentation_reflects_contract
#print axioms NondualConcernAdapter.covered_role_presentation_contract_iff
