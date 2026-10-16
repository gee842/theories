import ObservationRepair

/- A chosen observation process changes later available distinctions in the
same interaction. The finite sensing menu and costs are supplied. This module
extends the checked game; it does not claim that sensing was an action in the
original one-round paper, or that these information effects are wholly new. -/
noncomputable section

namespace ObservationChange

open ObservationRepair

def conditionalValue (p : ℝ) (x : Choice) : ℝ :=
  (1-p) * score true x + p * score false x

def conditionalRisk (p : ℝ) (x : Choice) : ℝ :=
  (1-p) * (if truthful x.1 true = true then 0 else 1) +
    p * (if truthful x.1 false = true then 0 else 1)

def safeChoice : Choice := (0, 0)

-- Four latent outcomes: (fact true, favorable), (fact false, favorable),
-- (fact true, unfavorable), (fact false, unfavorable).
def jointMass (i : Fin 4) : ℝ :=
  if i = 0 then 15/32 else if i = 1 then 1/32 else if i = 2 then 13/32 else 3/32

theorem joint_is_probability :
    (∀ i, 0 < jointMass i) ∧ ∑ i, jointMass i = 1 := by
  constructor
  · intro i; fin_cases i <;> norm_num [jointMass, Fin.ext_iff]
  · norm_num [jointMass, Fin.sum_univ_succ, Fin.ext_iff]

theorem bayes_consistent_refinement :
    jointMass 0 + jointMass 1 = 1/2 ∧
    jointMass 2 + jointMass 3 = 1/2 ∧
    jointMass 1 + jointMass 3 = 1/8 ∧
    jointMass 1 / (jointMass 0 + jointMass 1) = 1/16 ∧
    jointMass 3 / (jointMass 2 + jointMass 3) = 3/16 := by
  norm_num [jointMass, Fin.ext_iff]

theorem aggregate_recovers_prior (x : Choice) :
    (conditionalValue (1/16) x + conditionalValue (3/16) x)/2 =
      conditionalValue (1/8) x := by
  unfold conditionalValue
  ring

theorem coarse_safe_value : conditionalValue (1/8) safeChoice = 22 := by
  norm_num [conditionalValue, safeChoice, score, switch_head_exact,
    impact_head_exact, taskHead, human, truthful, Fin.ext_iff]

theorem coarse_other_strict (x : Choice) (h : x ≠ safeChoice) :
    conditionalValue (1/8) x < 22 := by
  rcases x with ⟨m,a⟩
  fin_cases m <;> fin_cases a <;>
    norm_num [conditionalValue, safeChoice, score, switch_head_exact,
      impact_head_exact, taskHead, human, truthful, Fin.ext_iff] at *

theorem coarse_bound (x : Choice) : conditionalValue (1/8) x ≤ 22 := by
  by_cases h : x = safeChoice
  · subst x; exact le_of_eq coarse_safe_value
  · exact le_of_lt (coarse_other_strict x h)

theorem favorable_bound (x : Choice) : conditionalValue (1/16) x ≤ 89/4 := by
  have h := pure_value_bound x
  rw [risky_value] at h
  have eqv : conditionalValue (1/16) x = value x := by
    unfold conditionalValue value average
    ring
  rw [eqv]
  exact h

theorem unfavorable_bound (x : Choice) : conditionalValue (3/16) x ≤ 22 := by
  rcases x with ⟨m,a⟩
  fin_cases m <;> fin_cases a <;>
    norm_num [conditionalValue, score, switch_head_exact,
      impact_head_exact, taskHead, human, truthful, Fin.ext_iff]

theorem realized_score_bounds (x : Choice) : score true x ≤ 23 ∧ score false x ≤ 22 := by
  rcases x with ⟨m,a⟩
  fin_cases m <;> fin_cases a <;>
    norm_num [score, switch_head_exact, impact_head_exact, taskHead, human, truthful, Fin.ext_iff]

-- Mode 0: no query; mode 1: noisy query costing 1/16;
-- mode 2: fact-revealing query costing 1. Two contingent choices suffice for
-- each offered sensor. No-query ignores the second choice.
abbrev Plan := Fin 3 × Choice × Choice

def planValue (z : Plan) : ℝ :=
  if z.1 = 0 then conditionalValue (1/8) z.2.1
  else if z.1 = 1 then
    (conditionalValue (1/16) z.2.1 + conditionalValue (3/16) z.2.2)/2 - 1/16
  else (7*score true z.2.1 + score false z.2.2)/8 - 1

def planRisk (z : Plan) : ℝ :=
  if z.1 = 0 then conditionalRisk (1/8) z.2.1
  else if z.1 = 1 then (conditionalRisk (1/16) z.2.1 + conditionalRisk (3/16) z.2.2)/2
  else (7*(if truthful z.2.1.1 true = true then 0 else 1) +
    (if truthful z.2.2.1 false = true then 0 else 1))/8

def selected : Plan := (1, risky, safeChoice)

theorem selected_value : planValue selected = 353/16 := by
  norm_num [planValue, selected, conditionalValue, safeChoice, risky, score,
    switch_head_exact, impact_head_exact, taskHead, human, truthful, Fin.ext_iff]

theorem all_plan_bound (z : Plan) : planValue z ≤ planValue selected := by
  rcases z with ⟨mode,x,y⟩
  rw [selected_value]
  have h0 := coarse_bound x
  have h1 := favorable_bound x
  have h2 := unfavorable_bound y
  have h3 := (realized_score_bounds x).1
  have h4 := (realized_score_bounds y).2
  fin_cases mode <;> simp only [planValue, Fin.isValue] <;> norm_num <;> linarith

def PlanDistribution (p : Plan → ℝ) : Prop :=
  (∀ z, 0 ≤ p z) ∧ ∑ z, p z = 1

theorem randomized_plan_bound (p : Plan → ℝ) (h : PlanDistribution p) :
    (∑ z, p z * planValue z) ≤ planValue selected := by
  calc
    _ ≤ ∑ z, p z * planValue selected := Finset.sum_le_sum
      (fun z _ => mul_le_mul_of_nonneg_left (all_plan_bound z) (h.1 z))
    _ = planValue selected := by rw [← Finset.sum_mul, h.2, one_mul]

theorem selected_distribution_valid :
    PlanDistribution (fun z => if z = selected then 1 else 0) := by
  constructor
  · intro z; dsimp; split_ifs <;> norm_num
  · simp

theorem selected_distribution_value :
    (∑ z, (if z = selected then (1 : ℝ) else 0) * planValue z) = planValue selected := by
  simp

theorem selected_risk : planRisk selected = 1/32 := by
  norm_num [planRisk, selected, conditionalRisk, safeChoice, risky, truthful, Fin.ext_iff]

theorem no_query_safe :
    planValue (0,safeChoice,safeChoice) = 22 ∧ planRisk (0,safeChoice,safeChoice) = 0 := by
  norm_num [planValue, planRisk, conditionalValue, conditionalRisk, safeChoice, score,
    switch_head_exact, impact_head_exact, taskHead, human, truthful, Fin.ext_iff]

theorem query_strictly_preferred :
    planValue (0,safeChoice,safeChoice) < planValue selected ∧ 0 < planRisk selected := by
  rw [no_query_safe.1, selected_value, selected_risk]
  norm_num

theorem same_assertion_risk_floor_falls :
    conditionalRisk (1/8) risky = 1/8 ∧ conditionalRisk (1/16) risky = 1/16 ∧
    ¬ (1/8 : ℝ) ≤ conditionalRisk (1/16) risky := by
  norm_num [conditionalRisk, risky, truthful, Fin.ext_iff]

theorem query_cost_threshold (c : ℝ) :
    22 < (conditionalValue (1/16) risky + conditionalValue (3/16) safeChoice)/2 - c ↔ c < 1/8 := by
  norm_num [conditionalValue, risky, safeChoice, score, switch_head_exact,
    impact_head_exact, taskHead, human, truthful, Fin.ext_iff]
  constructor <;> intro h <;> linarith

-- A certainly true choice on the full support, with observation known.
def RobustTruth (x : Choice) : Prop :=
  truthful x.1 true = true ∧ truthful x.1 false = true

theorem robust_truth_iff (x : Choice) : RobustTruth x ↔ x.1 = 0 := by
  rcases x with ⟨m,a⟩
  fin_cases m <;> norm_num [RobustTruth, truthful, Fin.ext_iff]

theorem robust_truth_risk_zero (p : ℝ) (x : Choice) (h : RobustTruth x) :
    conditionalRisk p x = 0 := by simp [conditionalRisk, h.1, h.2]

-- Refining information preserves an already sound choice, with the same
-- feasible actions and unchanged success condition. This is a standard
-- support-based fact, not a new shielding algorithm.
def SafeOn {W O A : Type*} (obs : W → O) (good : W → A → Prop) (o : O) (a : A) : Prop :=
  ∀ w, obs w = o → good w a

theorem refinement_preserves_safe_choice {W O N A : Type*}
    (coarse : W → O) (fine : W → N) (forget : N → O)
    (refines : ∀ w, forget (fine w) = coarse w)
    (good : W → A → Prop) (n : N) (a : A)
    (safe : SafeOn coarse good (forget n) a) : SafeOn fine good n a := by
  intro w hw
  apply safe w
  rw [← refines w, hw]

-- A change of sensing and command delivery requires both a usable record
-- and an outcome-preserving, feasible command translation.
theorem transport_executable_correction {W Z O N A B : Type*}
    (change : W → Z) (oldObs : W → O) (newObs : Z → N) (decode : N → O)
    (carry : N → A → B) (oldAllowed : O → A → Prop) (newAllowed : N → B → Prop)
    (oldGood : W → A → Prop) (newGood : Z → B → Prop) (policy : O → A)
    (record : ∀ w, decode (newObs (change w)) = oldObs w)
    (oldCertificate : ∀ w, oldAllowed (oldObs w) (policy (oldObs w)) ∧ oldGood w (policy (oldObs w)))
    (realization : ∀ w a, oldAllowed (oldObs w) a ∧ oldGood w a →
      newAllowed (newObs (change w)) (carry (newObs (change w)) a) ∧
      newGood (change w) (carry (newObs (change w)) a)) :
    ∃ next : N → B, ∀ w,
      newAllowed (newObs (change w)) (next (newObs (change w))) ∧
      newGood (change w) (next (newObs (change w))) := by
  refine ⟨fun n => carry n (policy (decode n)), ?_⟩
  intro w
  dsimp
  rw [record w]
  exact realization w _ (oldCertificate w)

def deliver (relay command : Bool) : Bool := if relay then command else false

theorem intact_delivery (required : Bool) : deliver true required = required := by
  simp [deliver]

theorem perfect_information_cannot_replace_delivery :
    ¬ ∃ policy : Bool → Bool, ∀ required, deliver false (policy required) = required := by
  rintro ⟨policy,h⟩
  have bad := h true
  simp [deliver] at bad

end ObservationChange
