import ActionAwareTracking

/- Evidence-to-predictor connection within a supplied bilinear response family.
The four readings come from a supported common-reference calibration episode.
Their error bounds, persistence to use, probe access and permission are premises.
Identifying this response does not uniquely locate its physical causes. -/
namespace DiagnosticTracking

noncomputable section
open Filter
open scoped Topology

def response (bias gain context joint command setting : ℝ) : ℝ :=
  bias + gain*command + context*setting + joint*command*setting

def acquiredGain (baseline driven : ℝ) : ℝ := driven-baseline

def acquiredJoint (baseline driven situated combined : ℝ) : ℝ :=
  combined-driven-situated+baseline

def acquiredEffect (baseline driven situated combined command setting : ℝ) : ℝ :=
  acquiredGain baseline driven*command + acquiredGain baseline situated*setting +
    acquiredJoint baseline driven situated combined*command*setting

theorem same_discrepancy_different_repairs :
    response 1 1 0 0 1 1 = 2 ∧ response 0 2 0 0 1 1 = 2 ∧
    response 0 1 1 0 1 1 = 2 := by norm_num [response]

theorem diagnostic_records_distinguish :
    (response 1 1 0 0 0 0, response 1 1 0 0 1 0, response 1 1 0 0 0 1) = (1,2,1) ∧
    (response 0 2 0 0 0 0, response 0 2 0 0 1 0, response 0 2 0 0 0 1) = (0,2,0) ∧
    (response 0 1 1 0 0 0, response 0 1 1 0 1 0, response 0 1 1 0 0 1) = (0,1,1) := by
  norm_num [response]

theorem three_probes_miss_joint_relation (b g k h : ℝ) :
    response b g k h 0 0 = response b g k 0 0 0 ∧
    response b g k h 1 0 = response b g k 0 1 0 ∧
    response b g k h 0 1 = response b g k 0 0 1 := by simp [response]

theorem joint_probe_exposes_missing_relation (b g k h : ℝ) :
    response b g k h 1 1 - response b g k 0 1 1 = h := by unfold response; ring

theorem four_readings_recover_parameters (b g k h : ℝ) :
    response b g k h 0 0 = b ∧
    acquiredGain (response b g k h 0 0) (response b g k h 1 0) = g ∧
    acquiredGain (response b g k h 0 0) (response b g k h 0 1) = k ∧
    acquiredJoint (response b g k h 0 0) (response b g k h 1 0)
      (response b g k h 0 1) (response b g k h 1 1) = h := by
  dsimp [response, acquiredGain, acquiredJoint]
  constructor; · ring
  constructor; · ring
  constructor <;> ring

theorem acquired_effect_matches (b g k h u z : ℝ) :
    acquiredEffect (response b g k h 0 0) (response b g k h 1 0)
      (response b g k h 0 1) (response b g k h 1 1) u z = g*u+k*z+h*u*z := by
  unfold acquiredEffect acquiredGain acquiredJoint response
  ring

theorem acquired_parameters_error_bounds (b g k h y0 yu yz yuz e0 eu ez euz : ℝ)
    (h0 : |y0-response b g k h 0 0| ≤ e0)
    (hu : |yu-response b g k h 1 0| ≤ eu)
    (hz : |yz-response b g k h 0 1| ≤ ez)
    (huz : |yuz-response b g k h 1 1| ≤ euz) :
    |y0-b| ≤ e0 ∧ |acquiredGain y0 yu-g| ≤ eu+e0 ∧
    |acquiredGain y0 yz-k| ≤ ez+e0 ∧
    |acquiredJoint y0 yu yz yuz-h| ≤ euz+eu+ez+e0 := by
  simp only [response, mul_zero, mul_one, add_zero] at h0 hu hz huz
  refine ⟨h0, ?_, ?_, ?_⟩
  all_goals
    simp only [acquiredGain, acquiredJoint]
    apply abs_le.mpr
    obtain ⟨h0l,h0r⟩ := abs_le.mp h0
    obtain ⟨hul,hur⟩ := abs_le.mp hu
    obtain ⟨hzl,hzr⟩ := abs_le.mp hz
    obtain ⟨huzl,huzr⟩ := abs_le.mp huz
    constructor <;> linarith

theorem reference_and_readout_offsets_confounded (reference bias g k h u z : ℝ) :
    reference + response bias g k h u z = response (reference+bias) g k h u z := by
  unfold response
  ring

theorem four_probes_do_not_certify_unrepresented_curvature (b g k h c : ℝ) :
    (∀ u ∈ ({0,1} : Finset ℝ), ∀ z ∈ ({0,1} : Finset ℝ),
      response b g k h u z+c*u*(u-1) = response b g k h u z) ∧
    (response b g k h 2 0+c*2*(2-1))-response b g k h 2 0 = 2*c := by
  constructor
  · intro u hu z _
    simp only [Finset.mem_insert, Finset.mem_singleton] at hu
    rcases hu with rfl | rfl <;> ring
  · ring

theorem bound_transfers_with_drift (estimate old current precision drift : ℝ)
    (hp : |estimate-old| ≤ precision) (hd : |old-current| ≤ drift) :
    |estimate-current| ≤ precision+drift := by
  have := abs_sub_le estimate old current
  linarith

theorem corrected_reading_bound (raw actual bias learned noiseBound biasBound : ℝ)
    (hr : |raw-(actual+bias)| ≤ noiseBound) (hb : |learned-bias| ≤ biasBound) :
    |(raw-learned)-actual| ≤ noiseBound+biasBound := by
  obtain ⟨hrl,hrr⟩ := abs_le.mp hr
  obtain ⟨hbl,hbr⟩ := abs_le.mp hb
  apply abs_le.mpr
  constructor <;> linarith

theorem revised_effect_bound (current next g k h learnedG learnedK learnedH u z d G K H D : ℝ)
    (hlaw : next=current+g*u+k*z+h*u*z+d)
    (hg : |learnedG-g| ≤ G) (hk : |learnedK-k| ≤ K) (hh : |learnedH-h| ≤ H)
    (hd : |d| ≤ D) :
    |learnedG*u+learnedK*z+learnedH*u*z-(next-current)| ≤
      G*|u|+K*|z|+H*|u*z|+D := by
  have heq : learnedG*u+learnedK*z+learnedH*u*z-(next-current) =
      ((learnedG-g)*u+(learnedK-k)*z)+(learnedH-h)*(u*z)+(-d) := by rw [hlaw]; ring
  rw [heq]
  have ha := abs_add_le (((learnedG-g)*u+(learnedK-k)*z)+(learnedH-h)*(u*z)) (-d)
  have hb := abs_add_le ((learnedG-g)*u+(learnedK-k)*z) ((learnedH-h)*(u*z))
  have hc := abs_add_le ((learnedG-g)*u) ((learnedK-k)*z)
  simp only [abs_mul, abs_neg] at ha hb hc
  have mg := mul_le_mul_of_nonneg_right hg (abs_nonneg u)
  have mk := mul_le_mul_of_nonneg_right hk (abs_nonneg z)
  have mh := mul_le_mul_of_nonneg_right hh (abs_nonneg (u*z))
  rw [abs_mul] at mh ⊢
  linarith

/-- Uses only the four acquired values in the correction. The actual family,
calibration-error bounds and calibration/use correspondence are hypotheses. -/
theorem calibration_to_revised_residual
    (q b g k h y0 yu yz yuz e0 eu ez euz raw current next u z d noiseBound D : ℝ)
    (hq : q ≤ 1)
    (h0 : |y0-response b g k h 0 0| ≤ e0)
    (hu : |yu-response b g k h 1 0| ≤ eu)
    (hz : |yz-response b g k h 0 1| ≤ ez)
    (huz : |yuz-response b g k h 1 1| ≤ euz)
    (hr : |raw-(current+b)| ≤ noiseBound)
    (hlaw : next=current+g*u+k*z+h*u*z+d) (hd : |d| ≤ D) :
    (1-q)*|(raw-y0)-current|+|acquiredEffect y0 yu yz yuz u z-(next-current)| ≤
      (1-q)*(noiseBound+e0)+(eu+e0)*|u|+(ez+e0)*|z|+
        (euz+eu+ez+e0)*|u*z|+D := by
  obtain ⟨hb,hg,hk,hh⟩ := acquired_parameters_error_bounds b g k h y0 yu yz yuz e0 eu ez euz h0 hu hz huz
  have reading := corrected_reading_bound raw current b y0 noiseBound e0 hr hb
  have effects := revised_effect_bound current next g k h (acquiredGain y0 yu)
    (acquiredGain y0 yz) (acquiredJoint y0 yu yz yuz) u z d (eu+e0) (ez+e0)
    (euz+eu+ez+e0) D hlaw hg hk hh hd
  have weighted := mul_le_mul_of_nonneg_left reading (by linarith : 0 ≤ 1-q)
  unfold acquiredEffect
  linarith

theorem acquired_revision_bounds_tracking_step
    (q b g k h y0 yu yz yuz e0 eu ez euz noiseBound D initial : ℝ)
    (hq : 0 ≤ q) (hq1 : q ≤ 1)
    (raw actual command setting disturbance : ℕ → ℝ) (n : ℕ)
    (h0 : |y0-response b g k h 0 0| ≤ e0)
    (hu : |yu-response b g k h 1 0| ≤ eu)
    (hz : |yz-response b g k h 0 1| ≤ ez)
    (huz : |yuz-response b g k h 1 1| ≤ euz)
    (hr : |raw n-(actual n+b)| ≤ noiseBound)
    (hlaw : actual (n+1)=actual n+g*command n+k*setting n+h*command n*setting n+disturbance n)
    (hd : |disturbance n| ≤ D) :
    ActionAwareTracking.error q (fun i => raw i-y0)
      actual (fun i => acquiredEffect y0 yu yz yuz (command i) (setting i)) initial (n+1) ≤
    q*ActionAwareTracking.error q (fun i => raw i-y0)
      actual (fun i => acquiredEffect y0 yu yz yuz (command i) (setting i)) initial n +
    ((1-q)*(noiseBound+e0)+(eu+e0)*|command n|+(ez+e0)*|setting n|+
      (euz+eu+ez+e0)*|command n*setting n|+D) := by
  have step := ActionAwareTracking.predicted_step_bound q hq hq1 (fun i => raw i-y0) actual
    (fun i => acquiredEffect y0 yu yz yuz (command i) (setting i)) initial n
  have bound := calibration_to_revised_residual q b g k h y0 yu yz yuz e0 eu ez euz
    (raw n) (actual n) (actual (n+1)) (command n) (setting n) (disturbance n) noiseBound D
    hq1 h0 hu hz huz hr hlaw hd
  unfold ActionAwareTracking.residual at step
  linarith

/-- Earlier finite errors need not be erased. A sound repaired tail suffices. -/
theorem repaired_tail_converges (q : ℝ) (hq : 0 ≤ q) (hq1 : q < 1)
    (reading actual increment : ℕ → ℝ) (initial : ℝ) (N : ℕ)
    (hr : ∀ n, N ≤ n → reading n=actual n)
    (hi : ∀ n, N ≤ n → increment n=actual (n+1)-actual n) :
    Tendsto (ActionAwareTracking.error q reading actual increment initial) atTop (𝓝 0) := by
  apply ActionAwareTracking.prediction_converges q hq hq1 reading actual increment initial
  have he : ActionAwareTracking.residual q reading actual increment =ᶠ[atTop] (fun _ => (0 : ℝ)) := by
    apply eventually_atTop.2
    refine ⟨N, ?_⟩
    intro n hn
    simp [ActionAwareTracking.residual, hr n hn, hi n hn]
  exact tendsto_const_nhds.congr' he.symm

theorem acquired_repair_restores_convergence
    (q : ℝ) (hq : 0 ≤ q) (hq1 : q < 1) (b g k h initial : ℝ)
    (reading actual increment raw command setting : ℕ → ℝ) (N : ℕ)
    (hread : ∀ n, N ≤ n → raw n=actual n+b)
    (hlaw : ∀ n, N ≤ n → actual (n+1)=actual n+g*command n+k*setting n+h*command n*setting n)
    (hinstallRead : ∀ n, N ≤ n → reading n=raw n-response b g k h 0 0)
    (hinstallEffect : ∀ n, N ≤ n → increment n=
      acquiredEffect (response b g k h 0 0) (response b g k h 1 0)
        (response b g k h 0 1) (response b g k h 1 1) (command n) (setting n)) :
    Tendsto (ActionAwareTracking.error q reading actual increment initial) atTop (𝓝 0) := by
  apply repaired_tail_converges q hq hq1 reading actual increment initial N
  · intro n hn
    rw [hinstallRead n hn, hread n hn]
    simp [response]
  · intro n hn
    rw [hinstallEffect n hn, acquired_effect_matches, hlaw n hn]
    ring

/-- Persistent nonzero input bounds establish a band, not exact convergence. -/
theorem bounded_repaired_tail (e w : ℕ → ℝ) (q B : ℝ)
    (hq : 0 ≤ q) (hq1 : q < 1) (hB : 0 ≤ B) (N : ℕ)
    (hs : ∀ n, N ≤ n → e (n+1) ≤ q*e n+w n)
    (hw : ∀ n, N ≤ n → w n ≤ (1-q)*B) :
    ∀ ε : ℝ, 0 < ε → ∃ M, ∀ n, M ≤ n → e n < B+ε := by
  have tailstep : ∀ n, e (n+N+1) ≤ q*e (n+N)+(1-q)*B := by
    intro n
    exact le_trans (hs (n+N) (by omega)) (add_le_add le_rfl (hw (n+N) (by omega)))
  have band := SituatedTracking.eventual_band (fun n => e (n+N)) q B hq hq1 hB
    (by intro n; simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using tailstep n)
  intro ε hε
  obtain ⟨M,hM⟩ := band ε hε
  refine ⟨M+N, ?_⟩
  intro n hn
  have hh := hM (n-N) (by omega)
  simpa only [Nat.sub_add_cancel (by omega : N ≤ n)] using hh

end
end DiagnosticTracking
