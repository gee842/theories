import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic
import SystemsComplexity

/-! Real-valued, exactly observed linear feedback. These are supplied local
dynamics, not an empirical identification or a model of ethical concern. -/
namespace SystemsComplexity.RealFeedback

noncomputable section

open Filter
open scoped Topology

def immediate (k x : ℝ) (n : ℕ) : ℝ := (1 - k) ^ n * x

def delayedStep (k : ℝ) (s : ℝ × ℝ) : ℝ × ℝ :=
  (s.1 - k * s.2, s.1)

def delayed (k : ℝ) (s : ℝ × ℝ) : ℕ → ℝ × ℝ
  | 0 => s
  | n + 1 => delayedStep k (delayed k s n)

def squaredNorm (s : ℝ × ℝ) : ℝ := s.1 ^ 2 + s.2 ^ 2

def lyapunov (k : ℝ) (s : ℝ × ℝ) : ℝ :=
  2 * s.1 ^ 2 + 2 * k * (s.1 - s.2) ^ 2 + k ^ 2 * (k + 1) * s.2 ^ 2

def dissipation (k : ℝ) : ℝ := k * (1 - k) * (k + 2)

def rate (k : ℝ) : ℝ := 1 - dissipation k / 8

def rotationEnergy (k : ℝ) (s : ℝ × ℝ) : ℝ :=
  s.1 ^ 2 - s.1 * s.2 + k * s.2 ^ 2

theorem immediate_recurrence (k x : ℝ) (n : ℕ) :
    immediate k x (n + 1) = immediate k x n - k * immediate k x n := by
  simp only [immediate, pow_succ]
  ring

theorem immediate_converges_iff (k : ℝ) :
    (∀ x, Tendsto (immediate k x) atTop (𝓝 0)) ↔ 0 < k ∧ k < 2 := by
  constructor
  · intro h
    have h1 := h 1
    change Tendsto (fun n : ℕ => (1 - k) ^ n * 1) atTop (𝓝 0) at h1
    have hp : Tendsto (fun n : ℕ => (1 - k) ^ n) atTop (𝓝 0) := by
      simpa only [mul_one] using h1
    have ha := tendsto_pow_atTop_nhds_zero_iff.mp hp
    rw [abs_lt] at ha
    constructor <;> linarith
  · rintro ⟨hk, hk2⟩ x
    have ha : |1 - k| < 1 := by rw [abs_lt]; constructor <;> linarith
    simpa only [immediate, zero_mul] using
      (tendsto_pow_atTop_nhds_zero_iff.mpr ha).mul_const x

theorem squaredNorm_nonnegative (s : ℝ × ℝ) : 0 ≤ squaredNorm s := by
  unfold squaredNorm
  positivity

theorem lyapunov_nonnegative {k : ℝ} (hk : 0 ≤ k) (s : ℝ × ℝ) :
    0 ≤ lyapunov k s := by
  unfold lyapunov
  positivity

theorem lyapunov_step (k : ℝ) (s : ℝ × ℝ) :
    lyapunov k (delayedStep k s) = lyapunov k s - dissipation k * squaredNorm s := by
  unfold lyapunov delayedStep dissipation squaredNorm
  ring

theorem lyapunov_bounds {k : ℝ} (hk : 0 < k) (hk1 : k < 1) (s : ℝ × ℝ) :
    k ^ 2 * squaredNorm s ≤ lyapunov k s ∧ lyapunov k s ≤ 8 * squaredNorm s := by
  have hkk : 0 ≤ k ^ 2 := sq_nonneg k
  have hkk1 : k ^ 2 ≤ 1 := by nlinarith
  have hx := sq_nonneg s.1
  have hy := sq_nonneg s.2
  have hd := sq_nonneg (s.1 - s.2)
  have hp := sq_nonneg (s.1 + s.2)
  have hcoef : 0 ≤ k ^ 2 * (k + 1) := by positivity
  have hcoef2 : k ^ 2 * (k + 1) ≤ 2 := by nlinarith
  have hlx := mul_nonneg (show 0 ≤ 2 - k ^ 2 by linarith) hx
  have hly := mul_nonneg (show 0 ≤ k ^ 2 * k by positivity) hy
  have hmid := mul_nonneg (show 0 ≤ 2 * k by linarith) hd
  have hmid' := mul_nonneg (show 0 ≤ 2 - 2 * k by linarith) hd
  have hupper := mul_nonneg (show 0 ≤ 2 - k ^ 2 * (k + 1) by linarith) hy
  unfold squaredNorm lyapunov
  constructor <;> nlinarith

theorem rate_bounds {k : ℝ} (hk : 0 < k) (hk1 : k < 1) :
    0 ≤ rate k ∧ rate k < 1 := by
  have hd : 0 < dissipation k := by unfold dissipation; positivity
  have hnext := lyapunov_nonnegative hk.le (delayedStep k (1, 0))
  rw [lyapunov_step] at hnext
  norm_num [lyapunov, squaredNorm] at hnext
  unfold rate
  constructor <;> linarith

theorem lyapunov_contraction {k : ℝ} (hk : 0 < k) (hk1 : k < 1) (s : ℝ × ℝ) :
    lyapunov k (delayedStep k s) ≤ rate k * lyapunov k s := by
  have hb := (lyapunov_bounds hk hk1 s).2
  have hd : 0 ≤ dissipation k := by unfold dissipation; positivity
  have hm := mul_nonneg hd (show 0 ≤ 8 * squaredNorm s - lyapunov k s by linarith)
  rw [lyapunov_step]
  unfold rate
  nlinarith

theorem lyapunov_geometric_bound {k : ℝ} (hk : 0 < k) (hk1 : k < 1)
    (s : ℝ × ℝ) (n : ℕ) :
    lyapunov k (delayed k s n) ≤ rate k ^ n * lyapunov k s := by
  induction n with
  | zero => simp [delayed]
  | succ n ih =>
    have hstep := lyapunov_contraction hk hk1 (delayed k s n)
    have hm := mul_le_mul_of_nonneg_left ih (rate_bounds hk hk1).1
    simp only [delayed, pow_succ]
    nlinarith

theorem delayed_converges {k : ℝ} (hk : 0 < k) (hk1 : k < 1) (s : ℝ × ℝ) :
    Tendsto (fun n => squaredNorm (delayed k s n)) atTop (𝓝 0) := by
  have hr := rate_bounds hk hk1
  have hpow := tendsto_pow_atTop_nhds_zero_of_lt_one hr.1 hr.2
  have he : Tendsto (fun n => lyapunov k (delayed k s n)) atTop (𝓝 0) := by
    apply squeeze_zero (fun n => lyapunov_nonnegative hk.le _)
      (lyapunov_geometric_bound hk hk1 s)
    simpa only [zero_mul] using hpow.mul_const (lyapunov k s)
  have hk2 : 0 < k ^ 2 := sq_pos_of_pos hk
  have hu : ∀ n, squaredNorm (delayed k s n) ≤ lyapunov k (delayed k s n) / k ^ 2 := by
    intro n
    apply (le_div_iff₀ hk2).mpr
    simpa only [mul_comm] using (lyapunov_bounds hk hk1 (delayed k s n)).1
  apply squeeze_zero (fun n => squaredNorm_nonnegative _) hu
  simpa only [zero_div] using he.div_const (k ^ 2)

/-- Lyapunov stability in squared Euclidean norm, in addition to convergence. -/
theorem delayed_stable {k : ℝ} (hk : 0 < k) (hk1 : k < 1) :
    ∀ ε : ℝ, 0 < ε → ∃ δ : ℝ, 0 < δ ∧ ∀ s : ℝ × ℝ,
      squaredNorm s < δ → ∀ n, squaredNorm (delayed k s n) < ε := by
  intro ε hε
  have hk2 : 0 < k ^ 2 := sq_pos_of_pos hk
  refine ⟨ε * k ^ 2 / 8, by positivity, ?_⟩
  intro s hs n
  have hpow : rate k ^ n ≤ 1 := pow_le_one₀ (rate_bounds hk hk1).1 (rate_bounds hk hk1).2.le
  have hb := lyapunov_geometric_bound hk hk1 s n
  have hm := mul_le_mul_of_nonneg_right hpow (lyapunov_nonnegative hk.le s)
  have hlo := (lyapunov_bounds hk hk1 (delayed k s n)).1
  have hup := (lyapunov_bounds hk hk1 s).2
  nlinarith

theorem rotationEnergy_step (k : ℝ) (s : ℝ × ℝ) :
    rotationEnergy k (delayedStep k s) = k * rotationEnergy k s := by
  unfold rotationEnergy delayedStep
  ring

theorem rotationEnergy_iterate (k : ℝ) (s : ℝ × ℝ) (n : ℕ) :
    rotationEnergy k (delayed k s n) = k ^ n * rotationEnergy k s := by
  induction n with
  | zero => simp [delayed]
  | succ n ih => rw [delayed, rotationEnergy_step, ih, pow_succ]; ring

theorem nonpositive_gain_retains_deviation {k : ℝ} (hk : k ≤ 0) (n : ℕ) :
    1 ≤ (delayed k (1, 1) n).1 ∧ 1 ≤ (delayed k (1, 1) n).2 := by
  induction n with
  | zero => norm_num [delayed]
  | succ n ih =>
    have hm := mul_nonpos_of_nonpos_of_nonneg hk (show 0 ≤ (delayed k (1, 1) n).2 by linarith [ih.2])
    simp only [delayed, delayedStep]
    constructor <;> linarith [ih.1]

theorem nonpositive_gain_not_convergent {k : ℝ} (hk : k ≤ 0) :
    ¬ Tendsto (fun n => squaredNorm (delayed k (1, 1) n)) atTop (𝓝 0) := by
  intro h
  have hlo : ∀ n, (1 : ℝ) ≤ squaredNorm (delayed k (1, 1) n) := by
    intro n
    have hi := nonpositive_gain_retains_deviation hk n
    have hy := sq_nonneg (delayed k (1, 1) n).2
    unfold squaredNorm
    nlinarith [hi.1]
  have bad : (1 : ℝ) ≤ 0 := ge_of_tendsto h (Filter.Eventually.of_forall hlo)
  norm_num at bad

theorem rotationEnergy_upper {k : ℝ} (hk : 1 ≤ k) (s : ℝ × ℝ) :
    rotationEnergy k s ≤ (k + 2) * squaredNorm s := by
  have hx := sq_nonneg s.1
  have hy := sq_nonneg s.2
  have hp := sq_nonneg (s.1 + s.2)
  have hm := mul_nonneg (show 0 ≤ k by linarith) hx
  unfold rotationEnergy squaredNorm
  nlinarith

theorem large_gain_not_convergent {k : ℝ} (hk : 1 ≤ k) :
    ¬ Tendsto (fun n => squaredNorm (delayed k (1, 0) n)) atTop (𝓝 0) := by
  intro h
  have he : ∀ n, 1 ≤ rotationEnergy k (delayed k (1, 0) n) := by
    intro n
    rw [rotationEnergy_iterate]
    norm_num [rotationEnergy]
    exact one_le_pow₀ hk
  have hu : ∀ n, (1 : ℝ) ≤ (k + 2) * squaredNorm (delayed k (1, 0) n) := by
    intro n
    exact (he n).trans (rotationEnergy_upper hk _)
  have ht : Tendsto (fun n => (k + 2) * squaredNorm (delayed k (1, 0) n)) atTop (𝓝 0) := by
    simpa only [mul_zero] using h.const_mul (k + 2)
  have bad : (1 : ℝ) ≤ 0 := ge_of_tendsto ht (Filter.Eventually.of_forall hu)
  norm_num at bad

/-- Exact convergence classification for every real initial full state. -/
theorem delayed_converges_iff (k : ℝ) :
    (∀ s, Tendsto (fun n => squaredNorm (delayed k s n)) atTop (𝓝 0)) ↔
      0 < k ∧ k < 1 := by
  constructor
  · intro h
    constructor
    · by_contra hn
      exact nonpositive_gain_not_convergent (le_of_not_gt hn) (h (1, 1))
    · by_contra hn
      exact large_gain_not_convergent (le_of_not_gt hn) (h (1, 0))
  · rintro ⟨hk, hk1⟩ s
    exact delayed_converges hk hk1 s

theorem same_gain_different_convergence :
    (∀ x, Tendsto (immediate (6 / 5) x) atTop (𝓝 0)) ∧
      ¬ Tendsto (fun n => squaredNorm (delayed (6 / 5) (1, 0) n)) atTop (𝓝 0) := by
  constructor
  · exact (immediate_converges_iff (6 / 5)).mpr (by norm_num)
  · exact large_gain_not_convergent (by norm_num)

theorem rotationEnergy_positive {k : ℝ} (hk : 1 ≤ k) (s : ℝ × ℝ)
    (hs : s ≠ (0, 0)) : 0 < rotationEnergy k s := by
  have hn : 0 < squaredNorm s := by
    unfold squaredNorm
    have hx := sq_nonneg s.1
    have hy := sq_nonneg s.2
    by_contra h
    have hzero : s.1 = 0 ∧ s.2 = 0 := by constructor <;> nlinarith
    exact hs (Prod.ext hzero.1 hzero.2)
  have hd := sq_nonneg (s.1 - s.2)
  have hy := sq_nonneg s.2
  have hm := mul_nonneg (show 0 ≤ k - 1 by linarith) hy
  unfold rotationEnergy squaredNorm at *
  nlinarith

theorem delayed_diverges {k : ℝ} (hk : 1 < k) (s : ℝ × ℝ)
    (hs : s ≠ (0, 0)) :
    Tendsto (fun n => squaredNorm (delayed k s n)) atTop atTop := by
  have he := rotationEnergy_positive hk.le s hs
  have hc : 0 < k + 2 := by linarith
  have hg : Tendsto (fun n : ℕ => k ^ n * (rotationEnergy k s / (k + 2))) atTop atTop :=
    (tendsto_pow_atTop_atTop_of_one_lt hk).atTop_mul_const (div_pos he hc)
  apply tendsto_atTop_mono (fun n => ?_) hg
  have hu := rotationEnergy_upper hk.le (delayed k s n)
  rw [rotationEnergy_iterate] at hu
  rw [← mul_div_assoc]
  apply (div_le_iff₀ hc).mpr
  simpa only [mul_comm] using hu

theorem delayed_gain_one_six_periodic (s : ℝ × ℝ) : delayed 1 s 6 = s := by
  simp only [delayed, delayedStep]
  apply Prod.ext <;> dsimp <;> ring

theorem delayed_eq_iterate (k : ℝ) (s : ℝ × ℝ) (n : ℕ) :
    delayed k s n = SystemsComplexity.SymbolicDynamics.iterate (delayedStep k) n s := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [delayed, SystemsComplexity.SymbolicDynamics.iterate, ih]

theorem real_delayed_generative_trace (k : ℝ) (s : ℝ × ℝ) (n : ℕ) :
    Generative.Trace
      (SystemsOrganization.deterministic (fun state (_ : Unit) => delayedStep k state))
      s (List.replicate n ()) (delayed k s n) := by
  rw [delayed_eq_iterate]
  exact SystemsComplexity.iterate_generative_trace (delayedStep k) s n

end
end SystemsComplexity.RealFeedback

#print axioms SystemsComplexity.RealFeedback.immediate_recurrence
#print axioms SystemsComplexity.RealFeedback.immediate_converges_iff
#print axioms SystemsComplexity.RealFeedback.squaredNorm_nonnegative
#print axioms SystemsComplexity.RealFeedback.lyapunov_nonnegative
#print axioms SystemsComplexity.RealFeedback.lyapunov_step
#print axioms SystemsComplexity.RealFeedback.lyapunov_bounds
#print axioms SystemsComplexity.RealFeedback.rate_bounds
#print axioms SystemsComplexity.RealFeedback.lyapunov_contraction
#print axioms SystemsComplexity.RealFeedback.lyapunov_geometric_bound
#print axioms SystemsComplexity.RealFeedback.delayed_converges
#print axioms SystemsComplexity.RealFeedback.delayed_stable
#print axioms SystemsComplexity.RealFeedback.rotationEnergy_step
#print axioms SystemsComplexity.RealFeedback.rotationEnergy_iterate
#print axioms SystemsComplexity.RealFeedback.nonpositive_gain_retains_deviation
#print axioms SystemsComplexity.RealFeedback.nonpositive_gain_not_convergent
#print axioms SystemsComplexity.RealFeedback.rotationEnergy_upper
#print axioms SystemsComplexity.RealFeedback.large_gain_not_convergent
#print axioms SystemsComplexity.RealFeedback.delayed_converges_iff
#print axioms SystemsComplexity.RealFeedback.same_gain_different_convergence
#print axioms SystemsComplexity.RealFeedback.rotationEnergy_positive
#print axioms SystemsComplexity.RealFeedback.delayed_diverges
#print axioms SystemsComplexity.RealFeedback.delayed_gain_one_six_periodic
#print axioms SystemsComplexity.RealFeedback.delayed_eq_iterate
#print axioms SystemsComplexity.RealFeedback.real_delayed_generative_trace
