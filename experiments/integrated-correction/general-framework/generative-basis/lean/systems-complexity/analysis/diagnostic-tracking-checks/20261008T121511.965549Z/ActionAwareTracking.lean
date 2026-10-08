import SituatedTracking

/- Acquired response prediction within one changing history. The scalar response
law, calibration bounds, probe permission and realization of support are supplied.
The final finite-family results concern declared relevant aspects, not a theorem
that every new meaningful relationship has been anticipated or generated. -/
namespace ActionAwareTracking

noncomputable section
open Filter
open scoped Topology

def estimate (q : ℝ) (reading increment : ℕ → ℝ) (initial : ℝ) : ℕ → ℝ
  | 0 => initial
  | n+1 => q * estimate q reading increment initial n + (1-q)*reading n + increment n

def error (q : ℝ) (reading actual increment : ℕ → ℝ) (initial : ℝ) (n : ℕ) : ℝ :=
  |estimate q reading increment initial n - actual n|

def residual (q : ℝ) (reading actual increment : ℕ → ℝ) (n : ℕ) : ℝ :=
  (1-q)*|reading n-actual n| + |increment n-(actual (n+1)-actual n)|

theorem predicted_step_bound (q : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual increment : ℕ → ℝ) (initial : ℝ) (n : ℕ) :
    error q reading actual increment initial (n+1) ≤
      q * error q reading actual increment initial n + residual q reading actual increment n := by
  unfold error residual
  rw [estimate]
  have heq : q*estimate q reading increment initial n+(1-q)*reading n+increment n-actual (n+1) =
      q*(estimate q reading increment initial n-actual n)+(1-q)*(reading n-actual n)+
      (increment n-(actual (n+1)-actual n)) := by ring
  rw [heq]
  calc
    _ ≤ |q*(estimate q reading increment initial n-actual n)+(1-q)*(reading n-actual n)| +
        |increment n-(actual (n+1)-actual n)| := abs_add_le _ _
    _ ≤ (|q*(estimate q reading increment initial n-actual n)|+|(1-q)*(reading n-actual n)|)+
        |increment n-(actual (n+1)-actual n)| := add_le_add (abs_add_le _ _) le_rfl
    _ = _ := by rw [abs_mul, abs_mul, abs_of_nonneg hq,
                    abs_of_nonneg (by linarith : 0 ≤ 1-q)]; ring

def acquiredResponse (beforeReading afterReading probe : ℝ) : ℝ :=
  (afterReading-beforeReading)/probe

theorem calibration_residual_bound (before after beforeReading afterReading theta probe disturbance
    beforeBound afterBound disturbanceBound : ℝ)
    (hlaw : after = before+theta*probe+disturbance)
    (hb : |beforeReading-before| ≤ beforeBound)
    (ha : |afterReading-after| ≤ afterBound) (hd : |disturbance| ≤ disturbanceBound) :
    |(afterReading-beforeReading)-theta*probe| ≤ afterBound+beforeBound+disturbanceBound := by
  have heq : (afterReading-beforeReading)-theta*probe =
      ((afterReading-after)-(beforeReading-before))+disturbance := by rw [hlaw]; ring
  rw [heq]
  have hh := abs_add_le ((afterReading-after)-(beforeReading-before)) disturbance
  have hs : |(afterReading-after)-(beforeReading-before)| ≤
      |afterReading-after| + |beforeReading-before| := by
    simpa only [sub_eq_add_neg, abs_neg] using
      abs_add_le (afterReading-after) (-(beforeReading-before))
  linarith

theorem acquired_response_bound (before after beforeReading afterReading theta probe disturbance
    beforeBound afterBound disturbanceBound : ℝ) (hp : probe ≠ 0)
    (hlaw : after = before+theta*probe+disturbance)
    (hb : |beforeReading-before| ≤ beforeBound)
    (ha : |afterReading-after| ≤ afterBound) (hd : |disturbance| ≤ disturbanceBound) :
    |acquiredResponse beforeReading afterReading probe-theta| ≤
      (afterBound+beforeBound+disturbanceBound)/|probe| := by
  have hh := calibration_residual_bound before after beforeReading afterReading theta probe disturbance
    beforeBound afterBound disturbanceBound hlaw hb ha hd
  have heq : acquiredResponse beforeReading afterReading probe-theta =
      ((afterReading-beforeReading)-theta*probe)/probe := by
    unfold acquiredResponse
    field_simp
  rw [heq, abs_div]
  exact div_le_div_of_nonneg_right hh (abs_nonneg probe)

theorem acquired_response_exact (before theta probe : ℝ) (hp : probe ≠ 0) :
    acquiredResponse before (before+theta*probe) probe = theta := by
  unfold acquiredResponse
  field_simp
  ring

theorem zero_probe_has_no_response_distinction (before theta other : ℝ) :
    before+theta*0 = before+other*0 := by ring

theorem controlled_residual_bound (current next theta learned command disturbance disturbanceBound : ℝ)
    (hlaw : next=current+theta*command+disturbance) (hd : |disturbance| ≤ disturbanceBound) :
    |learned*command-(next-current)| ≤ |learned-theta| * |command|+disturbanceBound := by
  have heq : learned*command-(next-current) = (learned-theta)*command-disturbance := by
    rw [hlaw]; ring
  rw [heq]
  have hh : |(learned-theta)*command-disturbance| ≤ |(learned-theta)*command| + |disturbance| := by
    simpa only [sub_eq_add_neg, abs_neg] using abs_add_le ((learned-theta)*command) (-disturbance)
  rw [abs_mul] at hh
  linarith

/-- A calibration record bounds a later predicted effect only under the
same response coefficient and explicit calibration/use disturbance bounds. -/
theorem calibration_transfers_to_action (before after beforeReading afterReading theta probe
    calibrationDisturbance beforeBound afterBound calibrationBound current next command
    useDisturbance useBound : ℝ) (hp : probe ≠ 0)
    (hcal : after=before+theta*probe+calibrationDisturbance)
    (hb : |beforeReading-before| ≤ beforeBound) (ha : |afterReading-after| ≤ afterBound)
    (hd : |calibrationDisturbance| ≤ calibrationBound)
    (huse : next=current+theta*command+useDisturbance) (hu : |useDisturbance| ≤ useBound) :
    |acquiredResponse beforeReading afterReading probe*command-(next-current)| ≤
      ((afterBound+beforeBound+calibrationBound)/|probe|) * |command|+useBound := by
  have hc := acquired_response_bound before after beforeReading afterReading theta probe
    calibrationDisturbance beforeBound afterBound calibrationBound hp hcal hb ha hd
  have hh := controlled_residual_bound current next theta
    (acquiredResponse beforeReading afterReading probe) command useDisturbance useBound huse hu
  have hm := mul_le_mul_of_nonneg_right hc (abs_nonneg command)
  linarith

/-- A supplied effect allowance restricts action magnitude at current precision.
It is not an ethical permission theorem or a requirement to maximize action. -/
theorem command_limit_from_precision (precision magnitude allowance : ℝ) (hp : 0 < precision) :
    precision*magnitude ≤ allowance ↔ magnitude ≤ allowance/precision := by
  rw [le_div_iff₀ hp]
  ring_nf

theorem controlled_step_bound (q : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual learned command theta disturbance : ℕ → ℝ) (initial : ℝ) (n : ℕ)
    (readingBound responseBound commandBound disturbanceBound : ℝ)
    (hlaw : actual (n+1)=actual n+theta n*command n+disturbance n)
    (hr : |reading n-actual n| ≤ readingBound)
    (hp : |learned n-theta n| ≤ responseBound)
    (hu : |command n| ≤ commandBound) (hd : |disturbance n| ≤ disturbanceBound) :
    error q reading actual (fun i => learned i*command i) initial (n+1) ≤
      q*error q reading actual (fun i => learned i*command i) initial n +
      ((1-q)*readingBound+responseBound*commandBound+disturbanceBound) := by
  have hs := predicted_step_bound q hq hq1 reading actual (fun i => learned i*command i) initial n
  have ha := controlled_residual_bound (actual n) (actual (n+1)) (theta n) (learned n)
    (command n) (disturbance n) disturbanceBound hlaw hd
  have hm := mul_le_mul hp hu (abs_nonneg (command n)) (le_trans (abs_nonneg _) hp)
  have hy := mul_le_mul_of_nonneg_left hr (by linarith : 0 ≤ 1-q)
  unfold residual at hs
  linarith

theorem prediction_converges (q : ℝ) (hq : 0 ≤ q) (hq1 : q < 1)
    (reading actual increment : ℕ → ℝ) (initial : ℝ)
    (hw : Tendsto (residual q reading actual increment) atTop (𝓝 0)) :
    Tendsto (error q reading actual increment initial) atTop (𝓝 0) := by
  exact SituatedTracking.vanishing_input_convergence _ _ q hq hq1 (fun _ => abs_nonneg _)
    (predicted_step_bound q hq (le_of_lt hq1) reading actual increment initial) hw

theorem retained_radius_sound (q : ℝ) (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (reading actual increment inputBound : ℕ → ℝ) (initial initialBound : ℝ) (n : ℕ)
    (hi : error q reading actual increment initial 0 ≤ initialBound)
    (hw : ∀ i, i < n → residual q reading actual increment i ≤ inputBound i) :
    error q reading actual increment initial n ≤ SituatedTracking.radius q inputBound initialBound n := by
  induction n with
  | zero => exact hi
  | succ n ih =>
    have hb := ih (fun i hi => hw i (by omega))
    have hs := predicted_step_bound q hq hq1 reading actual increment initial n
    have hm := mul_le_mul_of_nonneg_left hb hq
    have hh := hw n (by omega)
    simp only [SituatedTracking.radius]
    linarith

theorem acquired_response_tracks_motion (q : ℝ) (n : ℕ) :
    estimate q (fun t => 3+3*(t:ℝ)) (fun _ => acquiredResponse 0 3 1) 3 n = 3+3*(n:ℝ) := by
  induction n with
  | zero => simp [estimate]
  | succ n ih =>
    rw [estimate, ih]
    norm_num only [acquiredResponse, sub_zero, div_one, Nat.cast_add, Nat.cast_one]
    ring

theorem ignoring_action_retains_lag (n : ℕ) :
    SituatedTracking.error 0 (fun t => 3+3*(t:ℝ)) (fun t => 3+3*(t:ℝ)) 3 (n+1) = 3 := by
  simp only [SituatedTracking.error, SituatedTracking.estimate, zero_mul, sub_zero, one_mul,
             zero_add, Nat.cast_add, Nat.cast_one]
  have h : 3+3*(n:ℝ)-(3+3*((n:ℝ)+1)) = -3 := by ring
  rw [h]
  norm_num

theorem shrinking_parameter_error_can_be_amplified :
    Tendsto (fun n : ℕ => (1/2:ℝ)^n) atTop (𝓝 0) ∧
    ∀ n : ℕ, (1/2:ℝ)^n * (2:ℝ)^n = 1 := by
  constructor
  · exact tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  · intro n
    rw [← mul_pow]
    norm_num

/-- A fixed finite collection of current requirements can jointly become
certifiable; all its margins and error correspondences remain premises. -/
theorem finite_relations_eventually_certify {ι : Type*} (tasks : Finset ι)
    (actual retained radius cap : ι → ℕ → ℝ) (margin : ι → ℝ)
    (hm : ∀ j ∈ tasks, 0 < margin j)
    (he : ∀ j ∈ tasks, ∀ n, |retained j n-actual j n| ≤ radius j n)
    (ha : ∀ j ∈ tasks, ∀ n, actual j n ≤ cap j n-margin j)
    (hr : ∀ j ∈ tasks, Tendsto (radius j) atTop (𝓝 0)) :
    ∃ N, ∀ n ≥ N, ∀ j ∈ tasks, retained j n+radius j n ≤ cap j n := by
  apply eventually_atTop.1
  apply (eventually_all_finset tasks).2
  intro j hj
  exact eventually_atTop.2 (SituatedTracking.eventually_certifies
    (actual j) (retained j) (radius j) (cap j) (margin j) (hm j hj) (he j hj) (ha j hj) (hr j hj))

def freshError (time aspect : ℕ) : ℝ := if aspect < time then 0 else 1

theorem every_fixed_aspect_learned (aspect : ℕ) :
    ∃ N, ∀ time ≥ N, freshError time aspect = 0 := by
  refine ⟨aspect+1, ?_⟩
  intro time ht
  simp [freshError, show aspect < time by omega]

theorem expanding_frontier_keeps_unlearned_aspect (time : ℕ) :
    ∃ aspect, aspect ≤ time ∧ freshError time aspect = 1 := by
  refine ⟨time, le_rfl, ?_⟩
  simp [freshError]

end
end ActionAwareTracking
