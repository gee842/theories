import TuningCorrespondence

/-! Timing uncertainty formed from a serial execution and its recorded brackets.
Acquisition, retained plans and issued commands are relations within that history.
Source fidelity and physical drift/calibration remain separate application premises.
Commanded exposure is not electrical energy or an ethical value. -/
namespace TimedFeedback
noncomputable section

theorem acquisition_age_bound (lo acquired issued hi : ℝ)
    (hl : lo ≤ acquired) (ha : acquired ≤ issued) (hi' : issued ≤ hi) :
    0 ≤ issued-acquired ∧ issued-acquired ≤ hi-lo := by
  constructor <;> linarith

/-- A queued plan uses an earlier record. The lower bound concerns the record
timestamp, not the unrecorded instant at which its sensor value was acquired. -/
theorem queued_timestamp_age (previous current issued next : ℝ)
    (hc : current ≤ issued) (hn : issued ≤ next) :
    current-previous ≤ issued-previous ∧ issued-previous ≤ next-previous := by
  constructor <;> linarith

theorem source_ordered_calibration (lo acquired issued hi xRead xIssue estimate error rate : ℝ)
    (hl : lo ≤ acquired) (ha : acquired ≤ issued) (hi' : issued ≤ hi)
    (hr : 0 ≤ rate) (calibrated : |xRead-estimate| ≤ error)
    (drift : |xIssue-xRead| ≤ rate*(issued-acquired)) :
    |xIssue-estimate| ≤ error+rate*(hi-lo) := by
  have age := acquisition_age_bound lo acquired issued hi hl ha hi'
  calc
    _ ≤ |xIssue-xRead|+|xRead-estimate| := abs_sub_le _ _ _
    _ ≤ rate*(issued-acquired)+error := add_le_add drift calibrated
    _ ≤ error+rate*(hi-lo) := by
      have h := mul_le_mul_of_nonneg_left age.2 hr
      linarith

/-- Directly consumes the existing actual-case and indexed-protection connection.
The timing part of its radius is explained by ordered acquisition and actuation;
actual readout calibration, drift law and case inclusion are still required. -/
theorem timed_protection_at_actual {W P I : Type}
    (live : W → Prop) (actual estimate measured error rate threshold : W → P → I → ℝ)
    (lo acquired issued hi : W → P → I → ℝ) (w : W) (p : P) (truth : live w)
    (ordered : ∀ v, live v → ∀ i, lo v p i ≤ acquired v p i ∧
      acquired v p i ≤ issued v p i ∧ issued v p i ≤ hi v p i)
    (rates : ∀ v, live v → ∀ i, 0 ≤ rate v p i)
    (calibrated : ∀ v, live v → ∀ i, |measured v p i-estimate v p i| ≤ error v p i)
    (drift : ∀ v, live v → ∀ i, |actual v p i-measured v p i| ≤
      rate v p i*(issued v p i-acquired v p i))
    (margin : PracticalJudgment.Robust live (fun v a => ∀ i,
      threshold v a i+(error v a i+rate v a i*(hi v a i-lo v a i)) ≤ estimate v a i) p) :
    ∀ i, threshold w p i ≤ actual w p i := by
  apply TuningCorrespondence.calibrated_protection_at_actual live actual estimate
    (fun v a i => error v a i+rate v a i*(hi v a i-lo v a i)) threshold w p truth
  · intro v hv i
    have h := ordered v hv i
    exact source_ordered_calibration _ _ _ _ _ _ _ _ _ h.1 h.2.1 h.2.2
      (rates v hv i) (calibrated v hv i) (drift v hv i)
  · exact margin

/-- Exact commanded exposure of a held old command followed by the new command,
within one observed interval or its clipped common-window subinterval. -/
def segment (old next width switchAfter : ℝ) : ℝ :=
  old*switchAfter+next*(width-switchAfter)

theorem segment_midpoint_bound (old next width switchAfter : ℝ)
    (hl : 0 ≤ switchAfter) (hu : switchAfter ≤ width) :
    |segment old next width switchAfter-width/2*(old+next)| ≤ width/2*|old-next| := by
  have half : |switchAfter-width/2| ≤ width/2 := abs_le.mpr ⟨by linarith, by linarith⟩
  have identity : segment old next width switchAfter-width/2*(old+next) =
      (switchAfter-width/2)*(old-next) := by unfold segment; ring
  rw [identity, abs_mul]
  exact mul_le_mul_of_nonneg_right half (abs_nonneg _)

theorem segment_interval_endpoints (old next width : ℝ) :
    width/2*(old+next)-width/2*|old-next| = width*min old next ∧
    width/2*(old+next)+width/2*|old-next| = width*max old next := by
  rcases le_total old next with h | h
  · rw [abs_of_nonpos (sub_nonpos.mpr h), min_eq_left h, max_eq_right h]
    constructor <;> ring
  · rw [abs_of_nonneg (sub_nonneg.mpr h), min_eq_right h, max_eq_left h]
    constructor <;> ring

theorem history_exposure_bound (old next width switchAfter : ℕ → ℝ) (N : ℕ)
    (ht : ∀ n < N, 0 ≤ switchAfter n ∧ switchAfter n ≤ width n) :
    |FeedbackMemory.exposure (fun n => segment (old n) (next n) (width n) (switchAfter n)) (fun _ => 1) N-
      FeedbackMemory.exposure (fun n => width n/2*(old n+next n)) (fun _ => 1) N| ≤
      FeedbackMemory.exposure (fun n => width n/2*|old n-next n|) (fun _ => 1) N := by
  apply FeedbackMemory.exposure_error _ _ _ _ N (fun _ _ => by norm_num)
  intro n hn
  exact segment_midpoint_bound _ _ _ _ (ht n hn).1 (ht n hn).2

/-- The uncertainty domain comes from unrecorded switch positions in the same
histories. Separated exposure intervals justify this particular comparison. -/
theorem separated_history_exposure {P : Type}
    (old next width switchAfter : P → ℕ → ℝ) (N : P → ℕ) (a b : P)
    (timed : ∀ p ∈ [a,b], ∀ n < N p, 0 ≤ switchAfter p n ∧ switchAfter p n ≤ width p n)
    (gap : FeedbackMemory.exposure (fun n => width a n/2*(old a n+next a n)) (fun _ => 1) (N a)+
        FeedbackMemory.exposure (fun n => width a n/2*|old a n-next a n|) (fun _ => 1) (N a) <
      FeedbackMemory.exposure (fun n => width b n/2*(old b n+next b n)) (fun _ => 1) (N b)-
        FeedbackMemory.exposure (fun n => width b n/2*|old b n-next b n|) (fun _ => 1) (N b)) :
    FeedbackMemory.exposure (fun n => segment (old a n) (next a n) (width a n) (switchAfter a n)) (fun _ => 1) (N a) <
      FeedbackMemory.exposure (fun n => segment (old b n) (next b n) (width b n) (switchAfter b n)) (fun _ => 1) (N b) := by
  exact TuningCorrespondence.separated_model_comparison
    (fun p => FeedbackMemory.exposure (fun n => segment (old p n) (next p n) (width p n) (switchAfter p n)) (fun _ => 1) (N p))
    (fun p => FeedbackMemory.exposure (fun n => width p n/2*(old p n+next p n)) (fun _ => 1) (N p))
    (fun p => FeedbackMemory.exposure (fun n => width p n/2*|old p n-next p n|) (fun _ => 1) (N p))
    a b (history_exposure_bound _ _ _ _ _ (timed a (by simp)))
    (history_exposure_bound _ _ _ _ _ (timed b (by simp))) gap

end
end TimedFeedback
