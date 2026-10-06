import AdaptiveCore

/-!
Every gain frozen separately is stable, while the actual varying trajectory
stays away from zero. The persistent deviation is derived from an inductive
geometric account, not supplied as an assumption. The schedule here is specified;
its endogenous formation, observation costs and renewal are separate questions.
-/

namespace SystemsComplexity.ShrinkingGain

noncomputable section

open Filter
open scoped Topology

def shrinkingGain (n : ℕ) : ℝ := (1 / 2 : ℝ) ^ (n + 2)

def gainSum : ℕ → ℝ
  | 0 => 0
  | n + 1 => gainSum n + shrinkingGain n

def lowerBound (n : ℕ) : ℝ := 1 / 2 + (1 / 2 : ℝ) ^ (n + 1)

def orbit (n : ℕ) : ℝ × ℝ := AdaptiveCore.trajectory shrinkingGain (1, 1) n

theorem shrinking_gain_range (n : ℕ) : 0 < shrinkingGain n ∧ shrinkingGain n < 1 := by
  unfold shrinkingGain
  constructor
  · positivity
  · exact pow_lt_one₀ (by norm_num) (by norm_num) (by omega)

/-- Exact finite sum of the gain schedule, derived for every prefix. -/
theorem gain_sum_closed (n : ℕ) :
    gainSum n = (1 / 2 : ℝ) - (1 / 2 : ℝ) ^ (n + 1) := by
  induction n with
  | zero => norm_num [gainSum]
  | succ n ih =>
    simp only [gainSum, ih, shrinkingGain]
    rw [show n + 2 = (n + 1) + 1 by omega, pow_succ]
    ring

theorem lower_bound_account (n : ℕ) : lowerBound n = 1 - gainSum n := by
  rw [gain_sum_closed]
  unfold lowerBound
  ring

theorem lower_bound_step (n : ℕ) :
    lowerBound (n + 1) = lowerBound n - shrinkingGain n := by
  rw [lower_bound_account, lower_bound_account]
  simp only [gainSum]
  ring

theorem lower_bound_above_half (n : ℕ) : (1 / 2 : ℝ) < lowerBound n := by
  have hp : (0 : ℝ) < (1 / 2 : ℝ) ^ (n + 1) := by positivity
  unfold lowerBound
  linarith

theorem orbit_succ (n : ℕ) :
    orbit (n + 1) = ((orbit n).1 - shrinkingGain n * (orbit n).2, (orbit n).1) := by
  rfl

/-- The comparison uses both the genuinely reached coordinate bounds and the
    actual coefficient at the current step; no coordinate bound is a premise. -/
theorem orbit_bounds (n : ℕ) :
    lowerBound n ≤ (orbit n).1 ∧ (orbit n).1 ≤ 1 ∧
    lowerBound n ≤ (orbit n).2 ∧ (orbit n).2 ≤ 1 := by
  induction n with
  | zero => norm_num [orbit, AdaptiveCore.trajectory, lowerBound]
  | succ n ih =>
    obtain ⟨hxl, hxu, hyl, hyu⟩ := ih
    have hg := (shrinking_gain_range n).1
    have hlow := lower_bound_above_half n
    have hmul : shrinkingGain n * (orbit n).2 ≤ shrinkingGain n := by
      simpa only [mul_one] using mul_le_mul_of_nonneg_left hyu hg.le
    have hnonneg : 0 ≤ shrinkingGain n * (orbit n).2 :=
      mul_nonneg hg.le (by linarith)
    have hstep := lower_bound_step n
    rw [orbit_succ]
    dsimp only
    constructor
    · linarith
    constructor
    · linarith
    constructor
    · linarith
    · exact hxu

theorem orbit_coordinates_above_half (n : ℕ) :
    (1 / 2 : ℝ) < (orbit n).1 ∧ (1 / 2 : ℝ) < (orbit n).2 := by
  have hb := orbit_bounds n
  have hl := lower_bound_above_half n
  exact ⟨lt_of_lt_of_le hl hb.1, lt_of_lt_of_le hl hb.2.2.1⟩

theorem orbit_first_nonincreasing (n : ℕ) : (orbit (n + 1)).1 ≤ (orbit n).1 := by
  have hg := (shrinking_gain_range n).1
  have hy := (orbit_coordinates_above_half n).2
  have hnonneg : 0 ≤ shrinkingGain n * (orbit n).2 :=
    mul_nonneg hg.le (by linarith)
  rw [orbit_succ]
  dsimp only
  linarith

theorem envelope_above_half (n : ℕ) :
    (1 / 2 : ℝ) ≤ AdaptiveCore.envelope (orbit n) := by
  have hx := (orbit_coordinates_above_half n).1
  have habs : (orbit n).1 ≤ |(orbit n).1| := le_abs_self _
  have hmax : |(orbit n).1| ≤ AdaptiveCore.envelope (orbit n) := le_max_left _ _
  linarith

theorem squared_norm_above_half (n : ℕ) :
    (1 / 2 : ℝ) ≤ RealFeedback.squaredNorm (orbit n) := by
  have hxy := orbit_coordinates_above_half n
  have hx := sq_nonneg ((orbit n).1 - 1 / 2)
  have hy := sq_nonneg ((orbit n).2 - 1 / 2)
  unfold RealFeedback.squaredNorm
  nlinarith [hxy.1, hxy.2]

theorem every_frozen_gain_converges (t : ℕ) (s : ℝ × ℝ) :
    Tendsto (fun n => RealFeedback.squaredNorm
      (RealFeedback.delayed (shrinkingGain t) s n)) atTop (𝓝 0) := by
  exact RealFeedback.delayed_converges
    (shrinking_gain_range t).1 (shrinking_gain_range t).2 s

theorem varying_envelope_not_convergent :
    ¬ Tendsto (fun n => AdaptiveCore.envelope (orbit n)) atTop (𝓝 0) := by
  intro h
  have bad : (1 / 2 : ℝ) ≤ 0 :=
    ge_of_tendsto h (Filter.Eventually.of_forall envelope_above_half)
  norm_num at bad

theorem varying_squared_norm_not_convergent :
    ¬ Tendsto (fun n => RealFeedback.squaredNorm (orbit n)) atTop (𝓝 0) := by
  intro h
  have bad : (1 / 2 : ℝ) ≤ 0 :=
    ge_of_tendsto h (Filter.Eventually.of_forall squared_norm_above_half)
  norm_num at bad

/-- Each fixed gain's true convergence coexists with failure of the actual
    time-dependent composition, for the very same paired-state update law. -/
theorem frozen_convergence_not_varying_convergence :
    (∀ t s, Tendsto (fun n => RealFeedback.squaredNorm
      (RealFeedback.delayed (shrinkingGain t) s n)) atTop (𝓝 0)) ∧
    ¬ Tendsto (fun n => AdaptiveCore.envelope (orbit n)) atTop (𝓝 0) ∧
    ¬ Tendsto (fun n => RealFeedback.squaredNorm (orbit n)) atTop (𝓝 0) := by
  exact ⟨every_frozen_gain_converges, varying_envelope_not_convergent,
    varying_squared_norm_not_convergent⟩

end
end SystemsComplexity.ShrinkingGain

#print axioms SystemsComplexity.ShrinkingGain.shrinking_gain_range
#print axioms SystemsComplexity.ShrinkingGain.gain_sum_closed
#print axioms SystemsComplexity.ShrinkingGain.lower_bound_account
#print axioms SystemsComplexity.ShrinkingGain.lower_bound_step
#print axioms SystemsComplexity.ShrinkingGain.lower_bound_above_half
#print axioms SystemsComplexity.ShrinkingGain.orbit_succ
#print axioms SystemsComplexity.ShrinkingGain.orbit_bounds
#print axioms SystemsComplexity.ShrinkingGain.orbit_coordinates_above_half
#print axioms SystemsComplexity.ShrinkingGain.orbit_first_nonincreasing
#print axioms SystemsComplexity.ShrinkingGain.envelope_above_half
#print axioms SystemsComplexity.ShrinkingGain.squared_norm_above_half
#print axioms SystemsComplexity.ShrinkingGain.every_frozen_gain_converges
#print axioms SystemsComplexity.ShrinkingGain.varying_envelope_not_convergent
#print axioms SystemsComplexity.ShrinkingGain.varying_squared_norm_not_convergent
#print axioms SystemsComplexity.ShrinkingGain.frozen_convergence_not_varying_convergence
