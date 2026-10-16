import PracticalJudgment

/-
Stipulated shared-kitchen histories, 8 October 2026. These are constructed
application cases, not observations, predictions or calibrated thresholds.
The projection preserves two meal windows, contributors' basic rest, demonstrated
learning, usable access, and a free evening. Permission and responsibility are
separate application premises. PracticalJudgment.Better supplies the disclosed
J1/J2 ordering; the kernel does not warrant those ethical commitments.
-/
namespace SituatedKitchen

structure History where
  mealNow : Bool
  mealNext : Bool
  basicRest : Bool
  demonstratedSkill : Bool
  usableAccess : Bool
  freeEvening : Bool

def protection (h : History) (claim : Fin 3) : Prop :=
  (match claim.val with
    | 0 => h.mealNow
    | 1 => h.mealNext
    | _ => h.basicRest) = true

def realization (h : History) (claim : Fin 3) : Prop :=
  (match claim.val with
    | 0 => h.demonstratedSkill
    | 1 => h.demonstratedSkill && h.usableAccess
    | _ => h.freeEvening) = true

def care : History := ⟨true, true, true, false, true, true⟩
def learning : History := ⟨true, true, true, true, true, false⟩
def classOnly : History := ⟨false, true, true, true, true, false⟩
def overloadedCare : History := ⟨true, true, false, false, true, false⟩
def harmfulLearning : History := ⟨true, true, false, true, true, false⟩
def inaccessibleLearning : History := ⟨true, true, true, true, false, false⟩
def exitWithoutCover : History := ⟨true, false, true, false, true, true⟩

theorem timely_care_beats_class_only :
    PracticalJudgment.Better protection realization care classOnly := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem learning_and_care_incomparable :
    ¬ PracticalJudgment.Better protection realization learning care ∧
    ¬ PracticalJudgment.Better protection realization care learning := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem supported_learning_beats_overloaded_care :
    PracticalJudgment.Better protection realization learning overloadedCare := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem care_beats_harmful_learning :
    PracticalJudgment.Better protection realization care harmfulLearning := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem skill_without_usable_route :
    realization inaccessibleLearning 0 ∧ ¬ realization inaccessibleLearning 1 := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem restored_access_improves_same_learning :
    PracticalJudgment.Better protection realization learning inaccessibleLearning := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem competing_basic_losses_incomparable :
    ¬ PracticalJudgment.Better protection realization overloadedCare exitWithoutCover ∧
    ¬ PracticalJudgment.Better protection realization exitWithoutCover overloadedCare := by
  simp only [PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

/-- Public announcement does not overwrite actual next-window coverage. -/
def handoff (_announced actualCoverage : Bool) : History :=
  ⟨true, actualCoverage, true, true, true, false⟩

theorem announcement_cannot_replace_coverage (announced : Bool) :
    ¬ protection (handoff announced false) 1 := by
  simp only [handoff, PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

theorem actual_coverage_repairs_handoff (announced : Bool) :
    PracticalJudgment.Better protection realization
      (handoff announced true) (handoff announced false) := by
  simp only [handoff, PracticalJudgment.Better, PracticalJudgment.StrictIncluded, PracticalJudgment.Included, protection, realization, care, learning, classOnly, overloadedCare, harmfulLearning, inaccessibleLearning, exitWithoutCover]
  all_goals decide +revert

end SituatedKitchen
