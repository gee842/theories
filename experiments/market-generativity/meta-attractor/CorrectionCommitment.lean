import CorrectionDependence

/-! A posted, recoverable stake changes the prior task payoffs.
All plans remain alternatives. The contract is a supplied institution within
the shared history, not a derived moral motivation. Uniform audit outcomes,
task-score units, custody and actual classification are explicit assumptions. -/
namespace CorrectionCommitment
open CorrectionDependence

def passes (p : Plan) : Bool :=
  decide (p.provision ≤ 8) && decide (3 ≤ p.provision) &&
    decide (p.report = 2) && p.parentObeys && p.childObeys

theorem passes_iff_admissible (p : Plan) : passes p = true ↔ Admissible 2 p := by
  simp only [passes, Bool.and_eq_true, decide_eq_true_eq, Admissible,
    AccurateReport, Funded, planState]
  grind

def score (n goodHits badHits stake : Nat) (p : Plan) : Int :=
  (n : Int) * taskScore p -
    (if passes p then (goodHits : Int) * (stake : Int)
     else (badHits : Int) * (stake : Int))

def Best (n goodHits badHits stake : Nat) (p : Plan) : Prop :=
  ∀ q, score n goodHits badHits stake q ≤ score n goodHits badHits stake p

def Separates (n goodHits badHits stake : Nat) : Prop :=
  (goodHits : Int) * (stake : Int) + 7 * (n : Int) <
    (badHits : Int) * (stake : Int)

theorem prepared_score (n g b f : Nat) :
    score n g b f prepared = 5 * (n : Int) - (g : Int) * (f : Int) := by
  have hp : passes prepared = true := by decide
  have hs : taskScore prepared = 5 := by decide
  simp [score, hp, hs, Int.mul_comm]

theorem entrenched_score (n g b f : Nat) :
    score n g b f entrenched = 12 * (n : Int) - (b : Int) * (f : Int) := by
  have hp : passes entrenched = false := by decide
  have hs : taskScore entrenched = 12 := by decide
  simp [score, hp, hs, Int.mul_comm]

theorem good_score_bounded (n g b f : Nat) (p : Plan) (hp : passes p = true) :
    score n g b f p ≤ score n g b f prepared := by
  have hb := prepared_is_best_admissible_task_score p ((passes_iff_admissible p).mp hp)
  have ht : taskScore prepared = 5 := by decide
  rw [ht] at hb
  have hm := Int.mul_le_mul_of_nonneg_left hb (show (0 : Int) ≤ n by omega)
  rw [prepared_score]
  simp only [score, hp, ↓reduceIte]
  omega

theorem bad_score_bounded (n g b f : Nat) (p : Plan) (hp : passes p = false) :
    score n g b f p ≤ score n g b f entrenched := by
  have hb := global_task_score_bound p
  have hm := Int.mul_le_mul_of_nonneg_left hb (show (0 : Int) ≤ n by omega)
  rw [entrenched_score]
  simp only [score, hp, Bool.false_eq_true, ↓reduceIte]
  omega

theorem separation_iff_strict_compliant_preference (n g b f : Nat) :
    Separates n g b f ↔ score n g b f entrenched < score n g b f prepared := by
  rw [prepared_score, entrenched_score]
  unfold Separates
  omega

theorem prepared_best_under_separation (n g b f : Nat) (h : Separates n g b f) :
    Best n g b f prepared := by
  intro q
  cases hp : passes q with
  | true => exact good_score_bounded n g b f q hp
  | false =>
    have hb := bad_score_bounded n g b f q hp
    have hs := (separation_iff_strict_compliant_preference n g b f).mp h
    omega

theorem entrenched_best_without_separation (n g b f : Nat) (h : ¬ Separates n g b f) :
    Best n g b f entrenched := by
  intro q
  have hs : score n g b f prepared ≤ score n g b f entrenched := by
    have hn : ¬ score n g b f entrenched < score n g b f prepared := by
      intro hh
      exact h ((separation_iff_strict_compliant_preference n g b f).mpr hh)
    omega
  cases hp : passes q with
  | true => exact Int.le_trans (good_score_bounded n g b f q hp) hs
  | false => exact bad_score_bounded n g b f q hp

theorem every_best_passes_iff_separation (n g b f : Nat) :
    (∀ p, Best n g b f p → passes p = true) ↔ Separates n g b f := by
  constructor
  · intro h
    by_cases hn : Separates n g b f
    · exact hn
    · have hb := h entrenched (entrenched_best_without_separation n g b f hn)
      have hf : passes entrenched = false := by decide
      simp [hf] at hb
  · intro h p hb
    cases hp : passes p with
    | true => rfl
    | false =>
      have bound := bad_score_bounded n g b f p hp
      have best := hb prepared
      have strict := (separation_iff_strict_compliant_preference n g b f).mp h
      omega

theorem escrow_optimum_executes_previous_correction (n g b f : Nat)
    (h : Separates n g b f) (p : Plan) (hp : Best n g b f p) :
    stops (planState p) p.report p.parentObeys p.childObeys = true ∧
    actualLoss (planState p) 2 p.report p.parentObeys p.childObeys = 0 := by
  have pass := (every_best_passes_iff_separation n g b f).mpr h p hp
  exact admissibility_guarantees_actual_correction 2 p (by decide)
    ((passes_iff_admissible p).mp pass)

theorem every_best_is_prepared (n g b f : Nat) (hn : 0 < n)
    (h : Separates n g b f) (p : Plan) (hp : Best n g b f p) : p = prepared := by
  have pass := (every_best_passes_iff_separation n g b f).mpr h p hp
  have adm := (passes_iff_admissible p).mp pass
  have stop := (escrow_optimum_executes_previous_correction n g b f h p hp).1
  have lower := hp prepared
  rw [prepared_score] at lower
  simp only [score, pass, ↓reduceIte] at lower
  have provision : p.provision = 3 := by
    have atLeast : 3 ≤ p.provision := adm.2.2.1
    by_cases he : p.provision = 3
    · exact he
    · have ht : taskScore p ≤ 4 := by
        simp only [taskScore, stop, ↓reduceIte]
        omega
      have hm := Int.mul_le_mul_of_nonneg_left ht (show (0 : Int) ≤ n by omega)
      omega
  have report : p.report = 2 := adm.2.1
  have parent : p.parentObeys = true := adm.2.2.2.1
  have child : p.childObeys = true := adm.2.2.2.2
  cases p
  simp_all [prepared]

theorem optimum_fits_joint_resource_budget (n g b f wealth auditCost : Nat)
    (hn : 0 < n) (h : Separates n g b f) (budget : 3+auditCost+f ≤ wealth)
    (p : Plan) (hp : Best n g b f p) : p.provision+auditCost+f ≤ wealth := by
  rw [every_best_is_prepared n g b f hn h p hp]
  exact budget

theorem equality_retains_harmful_optimum : Best 2 0 1 14 entrenched := by
  apply entrenched_best_without_separation
  unfold Separates
  decide

theorem strict_margin_changes_all_optima :
    ∀ p, Best 2 0 1 15 p → passes p = true := by
  apply (every_best_passes_iff_separation 2 0 1 15).mpr
  unfold Separates
  decide

theorem false_positives_consume_the_margin :
    Separates 2 0 1 15 ∧ ¬ Separates 2 1 1 15 := by
  unfold Separates
  decide

-- A finite uniform lottery realizes both confiscation and refund from one
-- posted stake. No branch promises a fine beyond the posted amount.
def caught (hits outcome : Nat) : Bool := decide (outcome < hits)

def confiscated (hits stake outcome : Nat) : Nat :=
  if caught hits outcome then stake else 0

def refunded (hits stake outcome : Nat) : Nat :=
  if caught hits outcome then 0 else stake

theorem settlement_conserves_posted_stake (hits stake outcome : Nat) :
    confiscated hits stake outcome + refunded hits stake outcome = stake := by
  simp only [confiscated, refunded]
  split <;> omega

def totalConfiscation (hits stake : Nat) : Nat → Nat
  | 0 => 0
  | n+1 => totalConfiscation hits stake n + confiscated hits stake n

theorem confiscation_total (hits stake n : Nat) :
    totalConfiscation hits stake n = min hits n * stake := by
  induction n with
  | zero => simp [totalConfiscation]
  | succ n ih =>
    simp only [totalConfiscation, ih, confiscated, caught]
    by_cases hn : n < hits
    · have ha : min hits n = n := by omega
      have hb : min hits (n+1) = n+1 := by omega
      simp [hn, ha, hb, Nat.add_mul]
    · have ha : min hits n = hits := by omega
      have hb : min hits (n+1) = hits := by omega
      simp [hn, ha, hb]

theorem lottery_total_is_declared_penalty (hits stake n : Nat) (h : hits ≤ n) :
    totalConfiscation hits stake n = hits * stake := by
  rw [confiscation_total, Nat.min_eq_left h]

def totalPay (hits stake : Nat) (base : Int) : Nat → Int
  | 0 => 0
  | n+1 => totalPay hits stake base n + base - (confiscated hits stake n : Int)

theorem total_pay_accounts_for_realized_settlements (hits stake n : Nat) (base : Int) :
    totalPay hits stake base n = (n : Int)*base - (totalConfiscation hits stake n : Int) := by
  induction n with
  | zero => simp [totalPay, totalConfiscation]
  | succ n ih =>
    simp only [totalPay, totalConfiscation, ih]
    simp [Int.add_mul]
    omega

theorem declared_score_is_sum_of_lottery_payoffs (n g b f : Nat) (p : Plan)
    (hg : g ≤ n) (hb : b ≤ n) :
    totalPay (if passes p then g else b) f (taskScore p) n = score n g b f p := by
  rw [total_pay_accounts_for_realized_settlements]
  cases hp : passes p
  · simp [hp, lottery_total_is_declared_penalty b f n hb, score]
  · simp [hp, lottery_total_is_declared_penalty g f n hg, score]

def ApproxBest (n g b f epsilon : Nat) (p : Plan) : Prop :=
  ∀ q, score n g b f q ≤ score n g b f p + (epsilon : Int)

theorem approximate_margin_suffices (n g b f epsilon : Nat)
    (h : (g : Int)*(f : Int) + 7*(n : Int) + (epsilon : Int) < (b : Int)*(f : Int))
    (p : Plan) (hp : ApproxBest n g b f epsilon p) : passes p = true := by
  cases hh : passes p with
  | true => rfl
  | false =>
    have bound := bad_score_bounded n g b f p hh
    have near := hp prepared
    rw [prepared_score] at near
    rw [entrenched_score] at bound
    omega

theorem approximation_can_restore_a_harmful_choice : ApproxBest 2 0 1 15 1 entrenched := by
  intro q
  have hs : Separates 2 0 1 15 := by unfold Separates; decide
  have bound := prepared_best_under_separation 2 0 1 15 hs q
  have hp : score 2 0 1 15 prepared = 10 := by rw [prepared_score]; decide
  have he : score 2 0 1 15 entrenched = 9 := by rw [entrenched_score]; decide
  omega

-- Gain and penalties here are integer score totals over the same lottery.
-- This general margin is independent of the particular seven-unit example.
def Margin (gain good bad stake : Nat) : Prop :=
  good * stake + gain < bad * stake

theorem larger_stake_preserves_margin (gain good bad f w : Nat)
    (hf : f ≤ w) (h : Margin gain good bad f) : Margin gain good bad w := by
  have hg : good < bad := by
    by_cases hn : good < bad
    · exact hn
    · have hm := Nat.mul_le_mul_right f (show bad ≤ good by omega)
      unfold Margin at h
      omega
  have hb : bad = good + (bad-good) := by omega
  have hm := Nat.mul_le_mul_left (bad-good) hf
  unfold Margin at *
  rw [hb, Nat.add_mul] at h ⊢
  omega

theorem implementable_stake_iff_available_capacity (gain good bad available : Nat) :
    (∃ f, f ≤ available ∧ Margin gain good bad f) ↔
      Margin gain good bad available := by
  constructor
  · rintro ⟨f, hf, hm⟩
    exact larger_stake_preserves_margin gain good bad f available hf hm
  · intro h
    exact ⟨available, Nat.le_refl _, h⟩

theorem no_discrimination_no_deterrence (gain good bad f : Nat) (h : bad ≤ good) :
    ¬ Margin gain good bad f := by
  have hm := Nat.mul_le_mul_right f h
  unfold Margin
  omega

theorem separate_exit_and_stake_budget (wealth exitReserve auditCost f : Nat)
    (h : exitReserve + auditCost ≤ wealth) :
    exitReserve + auditCost + f ≤ wealth ↔ f ≤ wealth - exitReserve - auditCost := by
  omega

theorem jointly_fundable_deterrence_exact
    (wealth exitReserve auditCost gain good bad : Nat)
    (h : exitReserve + auditCost ≤ wealth) :
    (∃ f, exitReserve + auditCost + f ≤ wealth ∧ Margin gain good bad f) ↔
      Margin gain good bad (wealth-exitReserve-auditCost) := by
  constructor
  · rintro ⟨f, hf, hm⟩
    apply (implementable_stake_iff_available_capacity gain good bad _).mp
    exact ⟨f, (separate_exit_and_stake_budget wealth exitReserve auditCost f h).mp hf, hm⟩
  · intro hm
    refine ⟨wealth-exitReserve-auditCost, ?_, hm⟩
    omega

theorem concrete_joint_budget_boundary :
    (∃ f, 3+1+f ≤ 19 ∧ Margin 14 0 1 f) ∧
    ¬ (∃ f, 3+1+f ≤ 18 ∧ Margin 14 0 1 f) := by
  constructor
  · exact ⟨15, by decide, by unfold Margin; decide⟩
  · rintro ⟨f, hb, hm⟩
    unfold Margin at hm
    omega

-- Settling a penalty after detection is not guaranteed prevention in every
-- branch. The old physical model still runs in an uncaught branch.
theorem detection_and_recovery_are_distinct :
    caught 1 1 = false ∧ confiscated 1 15 1 = 0 ∧
    actualLoss (planState entrenched) 2 2 true true = 2 := by decide

-- Internal side payments cancel in joint gain. If a coalition controls the
-- custodian as well, an internally routed confiscation is not an external loss.
def coalitionGain (temptation externalLoss transfer : Int) : Int :=
  (temptation-transfer) + (transfer-externalLoss)

theorem internal_transfers_do_not_deter (temptation externalLoss transfer : Int) :
    coalitionGain temptation externalLoss transfer = temptation-externalLoss := by
  unfold coalitionGain
  omega

theorem profitable_integer_side_agreement_iff (temptation externalLoss : Int) :
    (∃ transfer : Int, 0 < temptation-transfer ∧ 0 < transfer-externalLoss) ↔
      externalLoss+1 < temptation := by
  constructor
  · rintro ⟨transfer, ha, hb⟩
    omega
  · intro h
    exact ⟨externalLoss+1, by omega, by omega⟩

theorem lost_custody_restores_old_incentive (n g f : Nat) (hn : 0 < n) :
    ¬ Separates n g 0 f := by
  have hp : (0 : Int) ≤ (g : Int)*(f : Int) := Int.mul_nonneg (by omega) (by omega)
  unfold Separates
  simp only [Int.natCast_zero, Int.zero_mul]
  omega

theorem stronger_temptation_can_exceed_any_fixed_capacity (good bad available : Nat) :
    ¬ Margin (bad*available) good bad available := by
  unfold Margin
  omega

theorem correction_incentive_does_not_ensure_participation :
    Separates 2 1 2 15 ∧ score 2 1 2 15 prepared < 0 := by
  rw [prepared_score]
  unfold Separates
  decide

theorem abstention_beats_every_plan_in_participation_failure (p : Plan) :
    score 2 1 2 15 p < 0 := by
  have h : Separates 2 1 2 15 := by unfold Separates; decide
  have bound := prepared_best_under_separation 2 1 2 15 h p
  have negative := correction_incentive_does_not_ensure_participation.2
  omega

end CorrectionCommitment
