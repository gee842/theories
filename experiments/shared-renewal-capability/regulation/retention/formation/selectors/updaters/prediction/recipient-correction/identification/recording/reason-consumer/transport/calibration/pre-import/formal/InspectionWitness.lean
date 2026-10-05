import ActionWitness
import PaidPreImport
import InspectionPreparation

namespace InspectionWitness

set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

def laws := ActionWitness.laws
def entry := PaidPreImport.initial
  (RecipientAction.advance laws ActionWitness.entry .fund) 3
def afterCommand := PaidPreImport.advance laws entry .readCommand
def checked := PaidPreImport.inspect laws afterCommand
def consumed := PaidPreImport.advance laws checked .consume
def imported := PaidPreImport.advance laws consumed .install

instance (s : PaidPreImport.State) (e : PaidPreImport.Event) : Decidable (PaidPreImport.Enabled s e) := by
  cases e <;> unfold PaidPreImport.Enabled PaidPreImport.Ready <;> infer_instance

/- This is the accepted three-record producer and paid replay endpoint before
import. It is not an initializer applied to an arbitrary imported q/last pair. -/
theorem actual_original_acquired_anchor :
    PaidPreImport.candidate entry=true ∧ PaidPreImport.qualification entry=true ∧
    entry.inner.imported=none ∧ entry.originUnused=true ∧
    RecipientIdentification.Sound
      (RecipientIdentification.registers (RecipientAction.core entry.inner).hardware) true := by decide

theorem actual_paid_read_and_inspection :
    PaidPreImport.Step laws entry .readCommand afterCommand ∧
    Generative.Trace (PaidPreImport.process laws) afterCommand
      [.readCandidate,.readFlag,.compare] checked ∧
    checked.permit=some true ∧ checked.reserve=0 ∧ checked.spent=3 := by
  refine ⟨⟨by decide,rfl⟩,?_,by decide,by decide,by decide⟩
  exact (PaidPreImport.paid_inspection_trace laws afterCommand
    (by decide) (by decide) (by decide) (by decide) (by decide) (by decide)).1

theorem actual_consumption_and_import :
    PaidPreImport.Step laws checked .consume consumed ∧
    PaidPreImport.Step laws consumed .install imported ∧
    imported.originUnused=false ∧
    ¬ PaidPreImport.Enabled imported .readCandidate := by
  exact ⟨⟨by decide,rfl⟩,⟨by decide,rfl⟩,by decide,by decide⟩

theorem exact_parent_import_state :
    imported.inner=RecipientAction.run laws ActionWitness.entry ActionWitness.bindingWord := by
  rfl

theorem actual_module_isolation_and_account :
    RecipientAction.material entry.inner+2=34 ∧
    RecipientAction.energy entry.inner+entry.reserve=67 ∧
    (RecipientAction.core checked.inner).hardware.fuel=9 ∧
    (RecipientAction.core imported.inner).hardware.fuel=8 ∧
    checked.spent=3 ∧ checked.reserve=0 ∧
    RecipientAction.energy ActionWitness.afterAction+10+checked.spent=67 := by decide

/- The inherited feasible trial now follows the exact same imported state.
The three new inspection units were charged outside the actor/recipient ledger. -/
theorem actual_trial_from_guarded_import :
    Generative.Trace (RecipientAction.process laws) imported.inner
      ((RecipientIdentification.trial .recipient true true).map RecipientAction.Event.execute)
      ActionWitness.afterAction ∧
    (RecipientAction.core ActionWitness.afterAction).patient=30 ∧
    imported.spent=3 ∧ imported.reserve=0 := by
  have old := ActionWitness.actual_action_trace
  cases old with
  | cons he h =>
    rcases he with ⟨_,rfl⟩
    cases h with
    | cons he h =>
      rcases he with ⟨_,rfl⟩
      cases h with
      | cons he h =>
        rcases he with ⟨_,rfl⟩
        exact ⟨h,ActionWitness.actual_recipient_effect.1,by decide,by decide⟩

end InspectionWitness

#print axioms InspectionWitness.actual_original_acquired_anchor
#print axioms InspectionWitness.actual_paid_read_and_inspection
#print axioms InspectionWitness.actual_consumption_and_import
#print axioms InspectionWitness.exact_parent_import_state
#print axioms InspectionWitness.actual_module_isolation_and_account
#print axioms InspectionWitness.actual_trial_from_guarded_import
