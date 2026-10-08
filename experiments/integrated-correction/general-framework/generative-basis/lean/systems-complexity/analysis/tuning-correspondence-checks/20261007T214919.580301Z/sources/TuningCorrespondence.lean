import FeedbackMemory
import PracticalJudgment

/-! Finite model selection and residual-transfer correspondence.
Engineering losses remain specified comparisons, not ethical value. Output,
retained state, commands and fitted residuals describe one dynamical history.
Exact fit with an output correction does not identify its counterfactual transfer. -/
namespace TuningCorrespondence
noncomputable section

def tracking (target temperature : ℕ → ℝ) (n : ℕ) : ℝ :=
  FeedbackMemory.exposure (fun t => |target t-temperature t|) (fun _ => 1) n

def objective (weight : ℝ) (target temperature command : ℕ → ℝ) (n : ℕ) : ℝ :=
  tracking target temperature (n+1)+weight*FeedbackMemory.movement command n

theorem tracking_error (target x y E : ℕ → ℝ) (N : ℕ)
    (h : ∀ n < N, |x n-y n| ≤ E n) :
    |tracking target x N-tracking target y N| ≤ FeedbackMemory.exposure E (fun _ => 1) N := by
  apply FeedbackMemory.exposure_error _ _ _ _ _ (fun _ _ => by norm_num)
  intro n hn
  calc
    _ ≤ |(target n-x n)-(target n-y n)| := abs_abs_sub_abs_le_abs_sub _ _
    _ = |x n-y n| := by congr 1 <;> ring
    _ ≤ E n := h n hn

theorem objective_error (weight : ℝ) (target x y u v E C : ℕ → ℝ) (n : ℕ)
    (ht : ∀ k < n+1, |x k-y k| ≤ E k) (hc : ∀ k ≤ n, |u k-v k| ≤ C k) :
    |objective weight target x u n-objective weight target y v n| ≤
      FeedbackMemory.exposure E (fun _ => 1) (n+1)+|weight|*FeedbackMemory.movementRadius C n := by
  have he := tracking_error target x y E (n+1) ht
  have hm := FeedbackMemory.movement_error u v C n hc
  have eqn : objective weight target x u n-objective weight target y v n =
      (tracking target x (n+1)-tracking target y (n+1))+
      weight*(FeedbackMemory.movement u n-FeedbackMemory.movement v n) := by
    unfold objective; ring
  rw [eqn]
  apply (abs_add_le _ _).trans
  apply add_le_add he
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left hm (abs_nonneg _)

/-- Reuses the established finite-frontier result with a stated engineering order.
This neither creates a physically feasible menu nor justifies its chosen loss. -/
theorem finite_model_minimum {P : Type} (cost : P → ℝ) (menu : List P) (hne : menu ≠ []) :
    ∃ a ∈ menu, ∀ b ∈ menu, cost a ≤ cost b := by
  obtain ⟨a,ha,hbest⟩ := PracticalJudgment.finite_frontier (fun a b => cost a < cost b)
    (fun _ => lt_irrefl _) (fun hab hbc => lt_trans hab hbc) menu hne
  exact ⟨a,ha,fun b hb => le_of_not_gt (hbest b hb)⟩

theorem estimated_minimum_actual_regret {P : Type} (actual estimate radius : P → ℝ)
    (a b : P) (best : estimate a ≤ estimate b)
    (ha : |actual a-estimate a| ≤ radius a) (hb : |actual b-estimate b| ≤ radius b) :
    actual a ≤ actual b+radius a+radius b := by
  have h1 := (abs_le.mp ha).2
  have h2 := (abs_le.mp hb).1
  linarith

theorem separated_model_comparison {P : Type} (actual estimate radius : P → ℝ)
    (a b : P) (ha : |actual a-estimate a| ≤ radius a) (hb : |actual b-estimate b| ≤ radius b)
    (gap : estimate a+radius a < estimate b-radius b) : actual a < actual b :=
  FeedbackMemory.separated_costs _ _ _ _ _ _ ha hb gap

/-- This is the inspected two-lag linear input/output recurrence. Initial outputs,
coefficients and input histories are explicit. No estimated coefficient is true by definition. -/
def arx (a₀ a₁ b₀ b₁ c x₀ x₁ γ : ℝ) (u : ℕ → ℝ) : ℕ → ℝ
  | 0 => x₀
  | 1 => x₁
  | n+2 => a₀*arx a₀ a₁ b₀ b₁ c x₀ x₁ γ u (n+1)+
      a₁*arx a₀ a₁ b₀ b₁ c x₀ x₁ γ u n+γ*(b₀*u (n+1)+b₁*u n)+c

/-- Varying input gain scales differences between full input histories with the
same initialization. This concerns response dependence, not a freely toggled verdict. -/
theorem arx_input_difference_scales (a₀ a₁ b₀ b₁ c x₀ x₁ γ : ℝ) (u v : ℕ → ℝ) (n : ℕ) :
    arx a₀ a₁ b₀ b₁ c x₀ x₁ γ u n-arx a₀ a₁ b₀ b₁ c x₀ x₁ γ v n =
      γ*(arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 u n-arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 v n) := by
  induction n using Nat.twoStepInduction with
  | zero => simp [arx]
  | one => simp [arx]
  | more n ih₀ ih₁ =>
    simp only [arx]
    linear_combination a₀*ih₁+a₁*ih₀

def corrected (prediction : ℝ → (ℕ → ℝ) → ℕ → ℝ)
    (observed recordedInput : ℕ → ℝ) (γ : ℝ) (input : ℕ → ℝ) (n : ℕ) : ℝ :=
  prediction γ input n+(observed n-prediction γ recordedInput n)

theorem every_corrected_model_fits_record (prediction : ℝ → (ℕ → ℝ) → ℕ → ℝ)
    (observed recordedInput : ℕ → ℝ) (γ : ℝ) (n : ℕ) :
    corrected prediction observed recordedInput γ recordedInput n = observed n := by
  unfold corrected; ring

theorem corrected_arx_response (a₀ a₁ b₀ b₁ c x₀ x₁ γ : ℝ)
    (observed recordedInput input : ℕ → ℝ) (n : ℕ) :
    corrected (arx a₀ a₁ b₀ b₁ c x₀ x₁) observed recordedInput γ input n =
      observed n+γ*(arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 input n-
        arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 recordedInput n) := by
  have h := arx_input_difference_scales a₀ a₁ b₀ b₁ c x₀ x₁ γ input recordedInput n
  unfold corrected
  linarith

/-- All models fit the same original record after their correction, yet two
positive response gains can disagree elsewhere. Actual gain admissibility still needs evidence. -/
theorem fitted_record_does_not_identify_transfer (a₀ a₁ b₀ b₁ c x₀ x₁ γ δ : ℝ)
    (observed recordedInput input : ℕ → ℝ) (n : ℕ)
    (gains : γ ≠ δ)
    (effect : arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 input n ≠ arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 recordedInput n) :
    corrected (arx a₀ a₁ b₀ b₁ c x₀ x₁) observed recordedInput γ input n ≠
      corrected (arx a₀ a₁ b₀ b₁ c x₀ x₁) observed recordedInput δ input n := by
  rw [corrected_arx_response,corrected_arx_response]
  intro h
  have hz : (γ-δ)*(arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 input n-
      arx a₀ a₁ b₀ b₁ c x₀ x₁ 1 recordedInput n) = 0 := by nlinarith
  rcases mul_eq_zero.mp hz with left | right
  · exact gains (sub_eq_zero.mp left)
  · exact effect (sub_eq_zero.mp right)

/-- The gain family is not evidence that every physical alternative is live. The
actual case must belong to the justified domain before robustness transports. -/
theorem calibrated_protection_at_actual {W P I : Type}
    (live : W → Prop) (actual estimate radius threshold : W → P → I → ℝ)
    (w : W) (a : P) (truth : live w)
    (calibrated : ∀ v, live v → ∀ i, |actual v a i-estimate v a i| ≤ radius v a i)
    (margin : PracticalJudgment.Robust live
      (fun v p => ∀ i, threshold v p i+radius v p i ≤ estimate v p i) a) :
    ∀ i, threshold w a i ≤ actual w a i := by
  exact RelationsAcrossScales.protected_conditions (actual w a) (estimate w a)
    (radius w a) (threshold w a) (calibrated w truth)
    (PracticalJudgment.robust_at_actual truth margin)

end
end TuningCorrespondence
