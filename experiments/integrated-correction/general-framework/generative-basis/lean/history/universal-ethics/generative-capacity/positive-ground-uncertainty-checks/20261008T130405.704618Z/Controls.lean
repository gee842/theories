import PositiveGroundUncertainty
open PositiveGroundUncertainty GenerativeComparison Generative.StandardsBridge

-- The concrete new formation feeds G0 directly without requiring C or no loss.
example (m : FormationModel) (productive : 0 < magnitude m)
    (positive : Bool → LivingClaim → Prop)
    (g0 : G0 (generatedInventory m) positive) :
    ∀ branch, ∃ q, positive branch q ∧ ¬ prior branch q := by
  apply contingent_generation_has_positive_ground (fun _ => True)
    prior (generatedInventory m) positive g0
  intro branch _
  exact (same_response_secures_generation_without_fixed_form m productive).1 branch

-- Existing truth retention applies to the same acquired evidence mechanism.
example (m : FormationModel) (included : rule m ∈ repertoire) :
    rule m ∈ learn repertoire (acquire (rule m) 1 [true]) :=
  actual_rule_retained (rule m) repertoire _ included
    (acquired_evidence_faithful (rule m) 1 [true])

-- Existing robust scope-to-actual transport needs actual coverage only here.
example (m : FormationModel) (covered : live m) (branch : Bool) :
    0 < finiteIntegral positiveDomain (contribution (respond initial) m branch) := by
  apply PracticalJudgment.robust_at_actual (w := m) (a := branch) covered
  intro model admitted
  exact acquired_evidence_secures_good_and_leaves_both_opennesses.2.2.2.2.2.1 model admitted branch

-- Represented physical realization is independent of merely changing evidence.
example (m : FormationModel) (branch : Bool) :
    finiteIntegral positiveDomain (contribution initial m branch) = 0 := by
  cases m <;> cases branch <;> rfl
