import CalibrationRenewal

noncomputable section

namespace DriftMargins
open ConnectionistRecovery DevelopmentalMemory UpdaterConsequences CalibratedUpdater CalibrationRenewal

def decode (zero one reading : ℝ) : ℝ := (reading-zero)/(one-zero)

theorem decoded_error (old current : Channel) (p noise : ℝ) (hg : old.gain ≠ 0) :
    decode (raw old 0) (raw old 1) (raw current p+noise)-p =
      ((current.gain-old.gain)*p+(current.bias-old.bias)+noise)/old.gain := by
  simp only [decode,raw,mul_zero,zero_add,mul_one,add_sub_cancel_right]
  field_simp
  ring

theorem decoding_error_bound (old current : Channel) (p noise dg db e : ℝ)
    (hg : old.gain ≠ 0) (hp : |p| ≤ 1)
    (hdg : |current.gain-old.gain| ≤ dg) (hdb : |current.bias-old.bias| ≤ db)
    (he : |noise| ≤ e) :
    |decode (raw old 0) (raw old 1) (raw current p+noise)-p| ≤ (dg+db+e)/|old.gain| := by
  rw [decoded_error old current p noise hg,abs_div]
  apply div_le_div_of_nonneg_right _ (abs_nonneg _)
  have hdg0 : 0 ≤ dg := le_trans (abs_nonneg _) hdg
  calc
    |(current.gain-old.gain)*p+(current.bias-old.bias)+noise|
        ≤ |(current.gain-old.gain)*p+(current.bias-old.bias)|+|noise| := abs_add_le _ _
    _ ≤ (|(current.gain-old.gain)*p|+|current.bias-old.bias|)+|noise| :=
      add_le_add (abs_add_le _ _) le_rfl
    _ ≤ (dg+db)+e := by
      rw [abs_mul]
      have hm : |current.gain-old.gain| * |p| ≤ dg := by
        calc
          _ ≤ dg*|p| := mul_le_mul_of_nonneg_right hdg (abs_nonneg _)
          _ ≤ dg*1 := mul_le_mul_of_nonneg_left hp hdg0
          _ = dg := mul_one _
      linarith

theorem successive_change_bound (values : Nat → ℝ) (rate : ℝ)
    (hstep : ∀ n, |values (n+1)-values n| ≤ rate) (n : Nat) :
    |values n-values 0| ≤ (n:ℝ)*rate := by
  induction n with
  | zero => simp
  | succ n ih =>
    calc
      |values (n+1)-values 0| = |(values (n+1)-values n)+(values n-values 0)| := by congr 1; ring
      _ ≤ |values (n+1)-values n|+|values n-values 0| := abs_add_le _ _
      _ ≤ rate+(n:ℝ)*rate := add_le_add (hstep n) ih
      _ = ((n+1:Nat):ℝ)*rate := by push_cast; ring

def radius (gain gainRate biasRate noiseBound : ℝ) (age : Nat) : ℝ :=
  ((age:ℝ)*(gainRate+biasRate)+noiseBound)/|gain|

theorem radius_nonneg (gain a b e : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (he : 0 ≤ e) (n : Nat) :
    0 ≤ radius gain a b e n := by
  unfold radius
  positivity

theorem radius_monotone (gain a b e : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (n m : Nat) (hnm : n ≤ m) : radius gain a b e n ≤ radius gain a b e m := by
  unfold radius
  apply div_le_div_of_nonneg_right _ (abs_nonneg _)
  have hnm' : (n:ℝ) ≤ m := by exact_mod_cast hnm
  nlinarith

theorem residual_noise_floor (gain a b e : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (n : Nat) :
    e/|gain| ≤ radius gain a b e n := by
  simpa [radius] using radius_monotone gain a b e ha hb 0 n (Nat.zero_le _)

theorem aged_decoding_bound (channels : Nat → Channel) (a b e p noise : ℝ) (n : Nat)
    (hg : (channels 0).gain ≠ 0) (hp : |p| ≤ 1)
    (hgain : ∀ k, |(channels (k+1)).gain-(channels k).gain| ≤ a)
    (hbias : ∀ k, |(channels (k+1)).bias-(channels k).bias| ≤ b)
    (he : |noise| ≤ e) :
    |decode (raw (channels 0) 0) (raw (channels 0) 1) (raw (channels n) p+noise)-p| ≤
      radius (channels 0).gain a b e n := by
  have h := decoding_error_bound (channels 0) (channels n) p noise ((n:ℝ)*a) ((n:ℝ)*b) e
    hg hp (successive_change_bound (fun k => (channels k).gain) a hgain n)
    (successive_change_bound (fun k => (channels k).bias) b hbias n) he
  convert h using 1
  dsimp [radius]
  ring

theorem assurance_window (gain a b e margin : ℝ) (hg : gain ≠ 0) (hr : 0 < a+b) (n : Nat) :
    2*radius gain a b e n < margin ↔
      (n:ℝ) < (|gain| * margin/2-e)/(a+b) := by
  have hgp : 0 < |gain| := abs_pos.mpr hg
  rw [lt_div_iff₀ hr]
  unfold radius
  constructor
  · intro h
    have h' : ((n:ℝ)*(a+b)+e)/|gain| < margin/2 := by linarith
    have := (div_lt_iff₀ hgp).mp h'
    nlinarith
  · intro h
    have h' : ((n:ℝ)*(a+b)+e)/|gain| < margin/2 := by
      apply (div_lt_iff₀ hgp).mpr
      nlinarith
    linarith

def verdict (r estimate : ℝ) : Option Bool := by
  classical
  exact if r < estimate then some true else if estimate ≤ -r then some false else none

theorem verdict_true_iff (r z : ℝ) : verdict r z = some true ↔ r < z := by
  simp [verdict]

theorem verdict_false_iff (r z : ℝ) (hr : 0 ≤ r) :
    verdict r z = some false ↔ z ≤ -r := by
  by_cases h : r < z
  · have hn : ¬ z ≤ -r := by linarith
    simp [verdict,h,hn]
  · simp [verdict,h]

theorem verdict_none_iff (r z : ℝ) : verdict r z = none ↔ -r < z ∧ z ≤ r := by
  simp only [verdict]
  split_ifs <;> simp_all

theorem positive_certificate (r z actual : ℝ) (he : |z-actual| ≤ r)
    (hv : verdict r z = some true) : 0 < actual := by
  have := (verdict_true_iff r z).mp hv
  have := (abs_le.mp he).2
  linarith

theorem negative_certificate (r z actual : ℝ) (he : |z-actual| ≤ r)
    (hv : verdict r z = some false) : actual ≤ 0 := by
  have hr : 0 ≤ r := le_trans (abs_nonneg _) he
  have := (verdict_false_iff r z hr).mp hv
  have := (abs_le.mp he).1
  linarith

theorem positive_interval_exact (r z : ℝ) (hr : 0 ≤ r) :
    verdict r z = some true ↔ ∀ actual, |z-actual| ≤ r → 0 < actual := by
  constructor
  · intro h actual he; exact positive_certificate r z actual he h
  · intro h
    have hb : |z-(z-r)| ≤ r := by simpa using le_of_eq (abs_of_nonneg hr)
    have := h (z-r) hb
    apply (verdict_true_iff r z).2
    linarith

theorem negative_interval_exact (r z : ℝ) (hr : 0 ≤ r) :
    verdict r z = some false ↔ ∀ actual, |z-actual| ≤ r → actual ≤ 0 := by
  constructor
  · intro h actual he; exact negative_certificate r z actual he h
  · intro h
    have hb : |z-(z+r)| ≤ r := by simpa using le_of_eq (abs_of_nonneg hr)
    have := h (z+r) hb
    apply (verdict_false_iff r z hr).2
    linarith

theorem unresolved_contains_opposites (r z : ℝ) (hr : 0 ≤ r) (hv : verdict r z = none) :
    ∃ positive nonpositive : ℝ, |z-positive| ≤ r ∧ 0 < positive ∧
      |z-nonpositive| ≤ r ∧ nonpositive ≤ 0 := by
  have h := (verdict_none_iff r z).mp hv
  refine ⟨z+r,z-r,?_,by linarith,?_,by linarith⟩
  · simpa using le_of_eq (abs_of_nonneg hr)
  · simpa using le_of_eq (abs_of_nonneg hr)

theorem separated_verdict (r z actual : ℝ) (he : |z-actual| ≤ r)
    (hm : 2*r < |actual|) :
    verdict r z = some (@decide (0 < actual) (Classical.propDecidable _)) := by
  classical
  have hr : 0 ≤ r := le_trans (abs_nonneg _) he
  have hlo := (abs_le.mp he).1
  have hhi := (abs_le.mp he).2
  by_cases hp : 0 < actual
  · rw [abs_of_pos hp] at hm
    have hz : r < z := by linarith
    simp [verdict,hz,hp]
  · have hn : actual ≤ 0 := le_of_not_gt hp
    rw [abs_of_nonpos hn] at hm
    have hz : z ≤ -r := by linarith
    have hz' : ¬ r < z := by linarith
    simp [verdict,hz',hz,hp]

theorem zero_radius_exact (z : ℝ) :
    verdict 0 z = some (@decide (0 < z) (Classical.propDecidable _)) := by
  classical
  by_cases h : 0 < z
  · simp [verdict,h]
  · simp [verdict,h,le_of_not_gt h]

def combine (values : Fin 3 → Option Bool) : Option Bool :=
  join (values 0) (join (values 1) (values 2))

theorem join_false_iff (a b : Option Bool) :
    join a b = some false ↔ a = some false ∨ b = some false := by
  cases a with
  | none => cases b with
    | none => simp [join]
    | some b => cases b <;> simp [join]
  | some a => cases a <;> cases b with
    | none => simp [join]
    | some b => cases b <;> simp [join]

theorem combine_true_iff (values : Fin 3 → Option Bool) :
    combine values = some true ↔ ∀ i, values i = some true := by
  simp [combine,join_true_iff,Fin.forall_fin_succ]

theorem combine_false_iff (values : Fin 3 → Option Bool) :
    combine values = some false ↔ ∃ i, values i = some false := by
  simp [combine,join_false_iff,Fin.exists_fin_succ]

def marginReport (radii estimates : Profile 3) : Option Bool :=
  combine (fun i => verdict (radii i) (estimates i))

theorem report_positive (radii estimates actual : Profile 3)
    (he : ∀ i, |estimates i-actual i| ≤ radii i)
    (hv : marginReport radii estimates = some true) : ∀ i, 0 < actual i := by
  intro i
  exact positive_certificate _ _ _ (he i) ((combine_true_iff _).mp hv i)

theorem report_negative (radii estimates actual : Profile 3)
    (he : ∀ i, |estimates i-actual i| ≤ radii i)
    (hv : marginReport radii estimates = some false) : ∃ i, actual i ≤ 0 := by
  obtain ⟨i,hi⟩ := (combine_false_iff _).mp hv
  exact ⟨i,negative_certificate _ _ _ (he i) hi⟩

theorem separated_report (radii estimates actual : Profile 3)
    (he : ∀ i, |estimates i-actual i| ≤ radii i) (hm : ∀ i, 2*radii i < |actual i|) :
    marginReport radii estimates = some (@decide (∀ i, 0 < actual i) (Classical.propDecidable _)) := by
  classical
  simp only [marginReport,combine,separated_verdict _ _ _ (he _) (hm _),join_some]
  congr 1
  simp [Fin.forall_fin_succ]

def guardedUpdate (radii estimates : Profile 3) (B : Network 3) (task : Task) : Network 3 :=
  match marginReport radii estimates with
  | some false => learn 1 (profile task) B
  | _ => B

def response (B : Network 3) (task : Task) : Profile 3 := step Real.tanh 1 1 B (profile task)

def actualMargins (B : Network 3) (task : Task) : Profile 3 := fun i => profile task i * response B task i

theorem guarded_update_exact (radii estimates : Profile 3) (B : Network 3) (task : Task)
    (he : ∀ i, |estimates i-actualMargins B task i| ≤ radii i)
    (hm : ∀ i, 2*radii i < |actualMargins B task i|) :
    guardedUpdate radii estimates B task = update .responsive B task := by
  classical
  unfold guardedUpdate
  rw [separated_report radii estimates (actualMargins B task) he hm]
  by_cases hs : succeeds B task
  · have h : ∀ i, 0 < actualMargins B task i := hs
    simp [h,update,hs]
  · have h : ¬ ∀ i, 0 < actualMargins B task i := hs
    simp [h,update,hs]

theorem certified_update_requires_failure (radii estimates : Profile 3) (B : Network 3) (task : Task)
    (he : ∀ i, |estimates i-actualMargins B task i| ≤ radii i)
    (hv : marginReport radii estimates = some false) : ¬ succeeds B task := by
  obtain ⟨i,hi⟩ := report_negative radii estimates (actualMargins B task) he hv
  intro hs
  exact (not_lt_of_ge hi) (hs i)

def observed (channels : Fin 3 → Channel) (noise : Profile 3) (B : Network 3) (task : Task) : Profile 3 :=
  fun i => raw (channels i) (response B task i)+noise i

def estimatedMargins (old : Fin 3 → Channel) (readings : Profile 3) (task : Task) : Profile 3 :=
  fun i => profile task i * decode (raw (old i) 0) (raw (old i) 1) (readings i)

theorem profile_abs_one (task : Task) (i : Fin 3) : |profile task i| = 1 := by
  cases task <;> fin_cases i <;> norm_num [profile,first,second]

theorem response_bound (B : Network 3) (task : Task) (i : Fin 3) : |response B task i| ≤ 1 := by
  simpa [response,step] using le_of_lt (Real.abs_tanh_lt_one (input B (profile task) i))

def ageRadii (channels : Fin 3 → Nat → Channel) (a b e : Profile 3) (n : Nat) : Profile 3 :=
  fun i => radius (channels i 0).gain (a i) (b i) (e i) n

theorem actual_aged_errors (channels : Fin 3 → Nat → Channel) (noise a b e : Profile 3)
    (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ i, |noise i| ≤ e i) (n : Nat) (B : Network 3) (task : Task) :
    ∀ i, |estimatedMargins (fun j => channels j 0) (observed (fun j => channels j n) noise B task) task i -
      actualMargins B task i| ≤ ageRadii channels a b e n i := by
  intro i
  unfold estimatedMargins observed actualMargins
  rw [← mul_sub,abs_mul,profile_abs_one,one_mul]
  exact aged_decoding_bound (channels i) (a i) (b i) (e i) (response B task i) (noise i) n
    (hg i) (response_bound B task i) (hgain i) (hbias i) (he i)

def nativeGuardedStep (channels : Fin 3 → Nat → Channel) (noise a b e : Profile 3) (n : Nat)
    (B : Network 3) (task : Task) : Network 3 :=
  guardedUpdate (ageRadii channels a b e n)
    (estimatedMargins (fun i => channels i 0) (observed (fun i => channels i n) noise B task) task) B task

theorem native_step_exact (channels : Fin 3 → Nat → Channel) (noise a b e : Profile 3)
    (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ i, |noise i| ≤ e i) (n : Nat) (B : Network 3) (task : Task)
    (hm : ∀ i, 2*ageRadii channels a b e n i < |actualMargins B task i|) :
    nativeGuardedStep channels noise a b e n B task = update .responsive B task := by
  exact guarded_update_exact _ _ B task (actual_aged_errors channels noise a b e hg hgain hbias he n B task) hm

def memoryMargin : ℝ := Real.tanh 1

theorem memory_margin_positive : 0 < memoryMargin := by
  exact (tanh_positive_iff 1).2 (by norm_num)

theorem tanh_abs_margin (x : ℝ) (hx : 1 ≤ |x|) : Real.tanh 1 ≤ |Real.tanh x| := by
  by_cases hp : 0 ≤ x
  · have ht : 0 ≤ Real.tanh x := by simpa using tanh_strictMono.monotone hp
    rw [abs_of_nonneg hp] at hx
    rw [abs_of_nonneg ht]
    exact tanh_strictMono.monotone hx
  · have hn : x < 0 := lt_of_not_ge hp
    have ht := (tanh_negative_iff x).2 hn
    rw [abs_of_neg hn] at hx
    rw [abs_of_neg ht,← Real.tanh_neg]
    exact tanh_strictMono.monotone hx

theorem field_gives_margin (B : Network 3) (task : Task) (i : Fin 3)
    (hx : 1 ≤ |input B (profile task) i|) : memoryMargin ≤ |actualMargins B task i| := by
  simp only [actualMargins,abs_mul,profile_abs_one,one_mul]
  simpa [memoryMargin,response,step] using tanh_abs_margin (input B (profile task) i) hx

theorem overwritten_margin (i : Fin 3) : memoryMargin ≤ |actualMargins (weighted 1 4) .a i| := by
  apply field_gives_margin
  fin_cases i <;> norm_num [profile,first_field]

theorem repaired_margin (task : Task) (i : Fin 3) : memoryMargin ≤ |actualMargins (weighted 2 4) task i| := by
  apply field_gives_margin
  cases task <;> fin_cases i <;> norm_num [profile,first_field,second_field]

theorem bounded_drift_repairs (channels : Fin 3 → Nat → Channel) (noise a b e : Profile 3)
    (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ i, |noise i| ≤ e i) (n : Nat)
    (hm : ∀ i, 2*ageRadii channels a b e n i < memoryMargin) :
    nativeGuardedStep channels noise a b e n (weighted 1 4) .a = weighted 2 4 := by
  rw [native_step_exact channels noise a b e hg hgain hbias he n _ _
    (fun i => lt_of_lt_of_le (hm i) (overwritten_margin i))]
  exact repaired_by_responsive

theorem bounded_drift_preserves (channels : Fin 3 → Nat → Channel) (noise a b e : Profile 3)
    (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ i, |noise i| ≤ e i) (n : Nat) (task : Task)
    (hm : ∀ i, 2*ageRadii channels a b e n i < memoryMargin) :
    nativeGuardedStep channels noise a b e n (weighted 2 4) task = weighted 2 4 := by
  rw [native_step_exact channels noise a b e hg hgain hbias he n _ _
    (fun i => lt_of_lt_of_le (hm i) (repaired_margin task i))]
  cases task <;> simp [update,post_failure_both.1,post_failure_both.2]

theorem understated_bound_false_success :
    verdict (1/8) (decode (raw (⟨1,0⟩ : Channel) 0) (raw (⟨1,0⟩ : Channel) 1)
      (raw (⟨1,1/2⟩ : Channel) (-1/4))) = some true ∧
    ¬ (0 < (-1/4:ℝ)) ∧
    (1/8:ℝ) < |decode 0 1 (raw (⟨1,1/2⟩ : Channel) (-1/4))-(-1/4)| := by
  norm_num [verdict,decode,raw]

-- Ages count successive changes in this local execution, not physical seconds.
def agedRun (channels : Fin 3 → Nat → Channel) (noises : Nat → Profile 3)
    (a b e : Profile 3) (age : Nat) (B : Network 3) : List Task → Network 3
  | [] => B
  | task::tasks => agedRun channels noises a b e (age+1)
      (nativeGuardedStep channels (noises age) a b e age B task) tasks

theorem aged_run_preserves_repaired (channels : Fin 3 → Nat → Channel) (noises : Nat → Profile 3)
    (a b e : Profile 3) (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ n i, |noises n i| ≤ e i) (ha : ∀ i, 0 ≤ a i) (hb : ∀ i, 0 ≤ b i)
    (horizon : Nat) (hm : ∀ i, 2*ageRadii channels a b e horizon i < memoryMargin)
    (tasks : List Task) (age : Nat) (ht : age+tasks.length ≤ horizon) :
    agedRun channels noises a b e age (weighted 2 4) tasks = weighted 2 4 := by
  induction tasks generalizing age with
  | nil => rfl
  | cons task tasks ih =>
    have hn : age ≤ horizon := by simp only [List.length_cons] at ht; omega
    have hm' : ∀ i, 2*ageRadii channels a b e age i < memoryMargin := by
      intro i
      have hd := radius_monotone (channels i 0).gain (a i) (b i) (e i) (ha i) (hb i) age horizon hn
      have hh := hm i
      dsimp [ageRadii] at *
      linarith
    rw [agedRun,bounded_drift_preserves channels (noises age) a b e hg hgain hbias (he age) age task hm']
    apply ih (age+1)
    simp only [List.length_cons] at ht
    omega

theorem repair_then_retained_history (channels : Fin 3 → Nat → Channel) (noises : Nat → Profile 3)
    (a b e : Profile 3) (hg : ∀ i, (channels i 0).gain ≠ 0)
    (hgain : ∀ i k, |(channels i (k+1)).gain-(channels i k).gain| ≤ a i)
    (hbias : ∀ i k, |(channels i (k+1)).bias-(channels i k).bias| ≤ b i)
    (he : ∀ n i, |noises n i| ≤ e i) (ha : ∀ i, 0 ≤ a i) (hb : ∀ i, 0 ≤ b i)
    (horizon : Nat) (hm : ∀ i, 2*ageRadii channels a b e horizon i < memoryMargin)
    (tasks : List Task) (age : Nat) (ht : age+(Task.a::tasks).length ≤ horizon) :
    agedRun channels noises a b e age (weighted 1 4) (.a::tasks) = weighted 2 4 := by
  have hn : age ≤ horizon := by simp only [List.length_cons] at ht; omega
  have hm' : ∀ i, 2*ageRadii channels a b e age i < memoryMargin := by
    intro i
    have hd := radius_monotone (channels i 0).gain (a i) (b i) (e i) (ha i) (hb i) age horizon hn
    have hh := hm i
    dsimp [ageRadii] at *
    linarith
  rw [agedRun,bounded_drift_repairs channels (noises age) a b e hg hgain hbias (he age) age hm']
  apply aged_run_preserves_repaired channels noises a b e hg hgain hbias he ha hb horizon hm tasks (age+1)
  simp only [List.length_cons] at ht
  omega

theorem wide_bound_withholds (B : Network 3) (task : Task) :
    marginReport (fun _ => 1) (actualMargins B task) = none ∧
    guardedUpdate (fun _ => 1) (actualMargins B task) B task = B := by
  have hv : ∀ i, verdict 1 (actualMargins B task i) = none := by
    intro i
    apply (verdict_none_iff _ _).2
    have hm : |actualMargins B task i| < 1 := by
      simp only [actualMargins,abs_mul,profile_abs_one,one_mul]
      simpa [response,step] using Real.abs_tanh_lt_one (input B (profile task) i)
    exact ⟨(abs_lt.mp hm).1, le_of_lt (abs_lt.mp hm).2⟩
  have hr : marginReport (fun _ => 1) (actualMargins B task) = none := by
    simp [marginReport,combine,hv,join]
  exact ⟨hr,by simp [guardedUpdate,hr]⟩

theorem uncertainty_can_retain_failure :
    guardedUpdate (fun _ => 1) (actualMargins (weighted 1 4) .a) (weighted 1 4) .a = weighted 1 4 ∧
    ¬ succeeds (weighted 1 4) .a := by
  exact ⟨(wide_bound_withholds _ _).2,by norm_num [succeeds_first_iff]⟩

end DriftMargins
