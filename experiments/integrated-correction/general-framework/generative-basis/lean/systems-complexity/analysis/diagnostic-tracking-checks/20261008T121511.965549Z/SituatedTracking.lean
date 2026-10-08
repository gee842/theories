import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

/- A scalar projection of a single changing history: a current condition,
its acquired reading, and the retained estimate used at the next step.
No independent external world, ethical utility, or general awareness predicate
is postulated. Calibration, projected relevance and continued support are supplied. -/
namespace SituatedTracking

noncomputable section
open Filter
open scoped Topology

def estimate (q : ℝ) (reading : ℕ → ℝ) (initial : ℝ) : ℕ → ℝ
  | 0 => initial
  | n + 1 => q * estimate q reading initial n + (1-q) * reading n

def error (q : ℝ) (reading actual : ℕ → ℝ) (initial : ℝ) (n : ℕ) : ℝ :=
  |estimate q reading initial n - actual n|

def forcing (q : ℝ) (reading actual : ℕ → ℝ) (n : ℕ) : ℝ :=
  (1-q) * |reading n - actual n| + |actual (n+1) - actual n|

theorem one_step (q : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual : ℕ → ℝ) (initial : ℝ) (n : ℕ) :
    error q reading actual initial (n+1) ≤
      q * error q reading actual initial n + forcing q reading actual n := by
  unfold error forcing
  rw [estimate]
  have heq : q * estimate q reading initial n + (1-q)*reading n - actual (n+1) =
      q*(estimate q reading initial n-actual n) +
      (1-q)*(reading n-actual n) + (actual n-actual (n+1)) := by ring
  rw [heq]
  calc
    _ ≤ |q*(estimate q reading initial n-actual n) + (1-q)*(reading n-actual n)| +
        |actual n-actual (n+1)| := abs_add_le _ _
    _ ≤ (|q*(estimate q reading initial n-actual n)| + |(1-q)*(reading n-actual n)|) +
        |actual n-actual (n+1)| := add_le_add (abs_add_le _ _) le_rfl
    _ = _ := by rw [abs_mul, abs_mul, abs_of_nonneg hq,
                    abs_of_nonneg (by linarith : 0 ≤ 1-q), abs_sub_comm (actual n)]; ring

/-- Only the inequalities along this finite prefix are assumed. -/
theorem recurrence_bound (e : ℕ → ℝ) (q B : ℝ) (hq : 0 ≤ q) (n : ℕ)
    (hstep : ∀ i, i < n → e (i+1) ≤ q * e i + (1-q)*B) :
    e n ≤ q^n * e 0 + (1-q^n)*B := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hb := ih (fun i hi => hstep i (by omega))
    have hm := mul_le_mul_of_nonneg_left hb hq
    have hs := hstep n (by omega)
    rw [pow_succ]
    nlinarith

theorem tracking_bound (q noise drift B : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual : ℕ → ℝ) (initial : ℝ) (n : ℕ)
    (hr : ∀ i, i < n → |reading i-actual i| ≤ noise)
    (hd : ∀ i, i < n → |actual (i+1)-actual i| ≤ drift)
    (hb : (1-q)*noise+drift ≤ (1-q)*B) :
    error q reading actual initial n ≤
      q^n * error q reading actual initial 0 + (1-q^n)*B := by
  apply recurrence_bound _ q B hq n
  intro i hi
  have hs := one_step q hq hq1 reading actual initial i
  have hm := mul_le_mul_of_nonneg_left (hr i hi) (by linarith : 0 ≤ 1-q)
  have hh := hd i hi
  unfold forcing at hs
  linarith

/-- A guaranteed eventual band, not necessarily a limiting error equal to B. -/
theorem eventual_band (e : ℕ → ℝ) (q B : ℝ) (hq : 0 ≤ q) (hq1 : q < 1)
    (hB : 0 ≤ B) (hstep : ∀ n, e (n+1) ≤ q*e n+(1-q)*B)
    (ε : ℝ) (hε : 0 < ε) : ∃ N, ∀ n ≥ N, e n < B+ε := by
  have hp := (tendsto_pow_atTop_nhds_zero_of_lt_one hq hq1).mul_const (e 0)
  have hz : Tendsto (fun n : ℕ => q^n * e 0) atTop (𝓝 0) := by simpa using hp
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hz.eventually (gt_mem_nhds hε))
  refine ⟨N, ?_⟩
  intro n hn
  have hb := recurrence_bound e q B hq n (fun i _ => hstep i)
  have hpos : 0 ≤ q^n * B := mul_nonneg (pow_nonneg hq n) hB
  have hh := hN n hn
  nlinarith

/-- Vanishing disturbance suffices; the represented actual condition need not
itself have a limit. This assumes an indefinitely available update history. -/
theorem vanishing_input_convergence (e w : ℕ → ℝ) (q : ℝ)
    (hq : 0 ≤ q) (hq1 : q < 1) (he : ∀ n, 0 ≤ e n)
    (hs : ∀ n, e (n+1) ≤ q*e n+w n)
    (hw : Tendsto w atTop (𝓝 0)) : Tendsto e atTop (𝓝 0) := by
  apply Metric.tendsto_atTop.2
  intro ε hε
  have hsmall : 0 < (1-q)*(ε/2) := mul_pos (by linarith) (by linarith)
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hw.eventually (gt_mem_nhds hsmall))
  have ht : ∀ k, e (N+(k+1)) ≤ q*e (N+k)+(1-q)*(ε/2) := by
    intro k
    have hh := hs (N+k)
    have hwk := hN (N+k) (by omega)
    have h : e (N+k+1) ≤ q*e (N+k)+(1-q)*(ε/2) := by linarith
    simpa only [Nat.add_assoc] using h
  obtain ⟨K, hK⟩ := eventual_band (fun k => e (N+k)) q (ε/2) hq hq1
    (by linarith) ht (ε/2) (by linarith)
  refine ⟨N+K, ?_⟩
  intro n hn
  have hh := hK (n-N) (by omega)
  have hindex : N+(n-N)=n := by omega
  rw [hindex] at hh
  rw [Real.dist_eq, sub_zero, abs_of_nonneg (he n)]
  linarith

theorem tracking_convergence (q : ℝ) (hq : 0 ≤ q) (hq1 : q < 1)
    (reading actual : ℕ → ℝ) (initial : ℝ)
    (hf : Tendsto (forcing q reading actual) atTop (𝓝 0)) :
    Tendsto (error q reading actual initial) atTop (𝓝 0) := by
  exact vanishing_input_convergence _ _ q hq hq1 (fun n => abs_nonneg _)
    (one_step q hq (le_of_lt hq1) reading actual initial) hf

/-- A retained upper bound; the inputs must be accessible, warranted bounds,
not unknown realized error renamed as confidence. -/
def radius (q : ℝ) (inputBound : ℕ → ℝ) (initialBound : ℝ) : ℕ → ℝ
  | 0 => initialBound
  | n+1 => q * radius q inputBound initialBound n + inputBound n

theorem radius_nonnegative (q : ℝ) (inputBound : ℕ → ℝ) (initialBound : ℝ)
    (hq : 0 ≤ q) (hi : 0 ≤ initialBound) (hw : ∀ n, 0 ≤ inputBound n) (n : ℕ) :
    0 ≤ radius q inputBound initialBound n := by
  induction n with
  | zero => exact hi
  | succ n ih => exact add_nonneg (mul_nonneg hq ih) (hw n)

theorem radius_sound (q : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual inputBound : ℕ → ℝ) (initial initialBound : ℝ) (n : ℕ)
    (hi : error q reading actual initial 0 ≤ initialBound)
    (hw : ∀ i, i < n → forcing q reading actual i ≤ inputBound i) :
    error q reading actual initial n ≤ radius q inputBound initialBound n := by
  induction n with
  | zero => exact hi
  | succ n ih =>
    have hb := ih (fun i hi => hw i (by omega))
    have hs := one_step q hq hq1 reading actual initial n
    have hm := mul_le_mul_of_nonneg_left hb hq
    have hh := hw n (by omega)
    simp only [radius]
    linarith

theorem radius_converges (q : ℝ) (inputBound : ℕ → ℝ) (initialBound : ℝ)
    (hq : 0 ≤ q) (hq1 : q < 1) (hi : 0 ≤ initialBound)
    (hw : ∀ n, 0 ≤ inputBound n) (hl : Tendsto inputBound atTop (𝓝 0)) :
    Tendsto (radius q inputBound initialBound) atTop (𝓝 0) := by
  exact vanishing_input_convergence _ _ q hq hq1
    (radius_nonnegative q inputBound initialBound hq hi hw)
    (fun _ => le_rfl) hl

/-- The threshold must be justified separately; this only transfers a bound. -/
theorem certificate_sound (actual retained radius cap : ℝ)
    (he : |retained-actual| ≤ radius) (hc : retained+radius ≤ cap) : actual ≤ cap := by
  have := (abs_le.mp he).1
  linarith

/-- A strict margin supports eventual finite decisions before exact certainty. -/
theorem eventually_certifies (actual retained radius cap : ℕ → ℝ) (margin : ℝ)
    (hm : 0 < margin) (he : ∀ n, |retained n-actual n| ≤ radius n)
    (ha : ∀ n, actual n ≤ cap n-margin)
    (hr : Tendsto radius atTop (𝓝 0)) :
    ∃ N, ∀ n ≥ N, retained n+radius n ≤ cap n := by
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hr.eventually (gt_mem_nhds (by linarith : 0 < margin/2)))
  refine ⟨N, ?_⟩
  intro n hn
  have hh := (abs_le.mp (he n)).2
  have hb := ha n
  have hs := hN n hn
  linarith

theorem misleading_reading_fixed (q initial : ℝ) (n : ℕ) :
    estimate q (fun _ => initial) initial n = initial := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [estimate, ih]; ring

theorem stable_error_can_be_wrong (q : ℝ) (n : ℕ) :
    error q (fun _ => 0) (fun _ => 1) 0 n = 1 := by
  unfold error
  rw [misleading_reading_fixed]
  norm_num

theorem changing_condition_retains_lag (n : ℕ) :
    error 0 (fun t => (t:ℝ)) (fun t => (t:ℝ)) 0 (n+1) = 1 := by
  simp only [error, estimate, zero_mul, sub_zero, one_mul, zero_add, Nat.cast_add, Nat.cast_one]
  have h : (n:ℝ)-((n:ℝ)+1) = -1 := by ring
  rw [h]
  norm_num

theorem boundary_accuracy_without_certificate :
    Tendsto (fun n : ℕ => (1/2:ℝ)^n) atTop (𝓝 0) ∧
    ∀ n : ℕ, ¬ ((1/2:ℝ)^n + (1/2:ℝ)^n ≤ 0) := by
  constructor
  · exact tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  · intro n
    have hp : 0 < (1/2:ℝ)^n := pow_pos (by norm_num) n
    linarith

end
end SituatedTracking
