import MarketGenerativity

/- Rational boundaries of the existing paid-correction market law.
   These are certificates and stationary-state results, not a full basin theorem. -/
namespace RegimeBoundary
open MarketGenerativity

def margin (alpha beta lambda theta : Rat) : Rat :=
  alpha * (1-theta) - beta*lambda*theta

def FloorProtected (alpha beta lambda theta : Rat) : Prop :=
  ∀ q w : Rat, theta ≤ q → q ≤ 1 → 0 ≤ w → w ≤ lambda →
    theta ≤ qualityStep q alpha beta w 1 0

theorem clip_floor_iff (z theta : Rat) (ht0 : 0 < theta) (ht1 : theta ≤ 1) :
    theta ≤ clip01 z ↔ theta ≤ z := by
  unfold clip01
  grind

theorem exact_floor_boundary (alpha beta lambda theta : Rat)
    (ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (ht0 : 0 < theta) (ht1 : theta ≤ 1) :
    FloorProtected alpha beta lambda theta ↔ 0 ≤ margin alpha beta lambda theta := by
  constructor
  · intro h
    have hcorner := h theta lambda (by grind) ht1 hl0 (by grind)
    unfold qualityStep at hcorner
    have hz := (clip_floor_iff _ theta ht0 ht1).mp hcorner
    unfold margin
    grind
  · intro hm q w hq _hq1 hw0 hw
    apply (quality_preserves_floor q alpha beta w theta lambda 0 0
      hq (by grind) ht1 ha hb hab hw0 hw (by grind) (by grind) _).1
    unfold margin at hm
    grind

theorem negative_margin_crosses_floor (alpha beta lambda theta : Rat)
    (ht0 : 0 < theta) (ht1 : theta ≤ 1)
    (hm : margin alpha beta lambda theta < 0) :
    qualityStep theta alpha beta lambda 1 0 < theta := by
  have hz : ¬ theta ≤ (1-alpha*1-beta*lambda)*theta+alpha*1-0 := by
    unfold margin at hm
    grind
  have h : ¬ theta ≤ clip01 ((1-alpha*1-beta*lambda)*theta+alpha*1-0) := by
    intro hf
    exact hz ((clip_floor_iff _ theta ht0 ht1).mp hf)
  unfold qualityStep
  grind

/- Positive-width low-selection rectangles from the existing mathematical study. -/
def LowCertificate (alpha beta lambda theta x q w : Rat) : Prop :=
  0 < x ∧ x < 1 ∧ 0 ≤ q ∧ q < theta ∧ 0 ≤ w ∧ w ≤ 1 ∧
  w ≤ lambda*(1-x) ∧ alpha*(1-q) ≤ beta*w*q

theorem low_certificate_requires_negative_margin (alpha beta lambda theta x q w : Rat)
    (ha : 0 < alpha) (hb : 0 ≤ beta) (hl : 0 ≤ lambda)
    (h : LowCertificate alpha beta lambda theta x q w) :
    margin alpha beta lambda theta < 0 := by
  rcases h with ⟨hx0,hx1,hq0,hqt,hw0,_hw1,hw,hbalance⟩
  have hlx := Rat.mul_nonneg hl (show 0 ≤ x by grind)
  have hwl : w ≤ lambda := by grind
  have hbwl := Rat.mul_le_mul_of_nonneg_left hwl hb
  have hbwlq := Rat.mul_le_mul_of_nonneg_right hbwl hq0
  have hbl := Rat.mul_nonneg hb hl
  have hqt' := Rat.mul_le_mul_of_nonneg_left (show q ≤ theta by grind) hbl
  have haqt := (Rat.mul_lt_mul_left ha).mpr hqt
  unfold margin
  grind

theorem zero_margin_is_protected_but_has_no_low_certificate
    (alpha beta lambda theta : Rat)
    (ha : 0 < alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (ht0 : 0 < theta) (ht1 : theta ≤ 1)
    (hm : margin alpha beta lambda theta = 0) :
    FloorProtected alpha beta lambda theta ∧
      ¬ ∃ x q w, LowCertificate alpha beta lambda theta x q w := by
  constructor
  · exact (exact_floor_boundary alpha beta lambda theta (by grind) hb hab
      hl0 hl1 ht0 ht1).mpr (by grind)
  · rintro ⟨x,q,w,h⟩
    have hn := low_certificate_requires_negative_margin alpha beta lambda theta x q w
      ha hb hl0 h
    grind

theorem negative_margin_has_low_certificate (alpha beta lambda theta : Rat)
    (ha : 0 < alpha) (hb : 0 ≤ beta)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (ht0 : 0 < theta) (ht1 : theta < 1)
    (hm : margin alpha beta lambda theta < 0) :
    ∃ x q w, LowCertificate alpha beta lambda theta x q w := by
  have hneed := Rat.mul_pos ha (show 0 < 1-theta by grind)
  have hpressure : alpha*(1-theta) < beta*lambda*theta := by
    unfold margin at hm
    grind
  have hbpos : 0 < beta := by
    by_cases h : 0 < beta
    · exact h
    · have : beta = 0 := by grind
      simp only [this, Rat.zero_mul] at hpressure
      grind
  have hlpos : 0 < lambda := by
    by_cases h : 0 < lambda
    · exact h
    · have : lambda = 0 := by grind
      simp only [this, Rat.mul_zero, Rat.zero_mul] at hpressure
      grind
  have hbt := Rat.mul_pos hbpos ht0
  let t := alpha*(1-theta)/(beta*theta)
  have htpos : 0 < t := by
    dsimp [t]
    apply (Rat.lt_div_iff hbt).mpr
    grind
  have htl : t < lambda := by
    dsimp [t]
    apply (Rat.div_lt_iff hbt).mpr
    grind
  have hteq : t*(beta*theta) = alpha*(1-theta) := by
    dsimp [t]
    exact Rat.div_mul_cancel (by grind)
  let w := (t+lambda)/2
  have hw0 : 0 < w := by dsimp [w]; grind
  have htw : t < w := by dsimp [w]; grind
  have hwl : w < lambda := by dsimp [w]; grind
  have hreturn := (Rat.mul_lt_mul_right hbt).mpr htw
  have hbw := Rat.mul_pos hbpos hw0
  have hden : 0 < alpha+beta*w := by grind
  let q := alpha/(alpha+beta*w)
  have hq0 : 0 < q := by
    dsimp [q]
    apply (Rat.lt_div_iff hden).mpr
    grind
  have hqt : q < theta := by
    dsimp [q]
    apply (Rat.div_lt_iff hden).mpr
    grind
  have hqeq : q*(alpha+beta*w) = alpha := by
    dsimp [q]
    exact Rat.div_mul_cancel (by grind)
  let x := (lambda-w)/lambda
  have hx0 : 0 < x := by
    dsimp [x]
    apply (Rat.lt_div_iff hlpos).mpr
    grind
  have hx1 : x < 1 := by
    dsimp [x]
    apply (Rat.div_lt_iff hlpos).mpr
    grind
  have hxeq : x*lambda = lambda-w := by
    dsimp [x]
    exact Rat.div_mul_cancel (by grind)
  exact ⟨x,q,w,hx0,hx1,by grind,hqt,by grind,by grind,by grind,by grind⟩

theorem exact_low_certificate_boundary (alpha beta lambda theta : Rat)
    (ha : 0 < alpha) (hb : 0 ≤ beta)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (ht0 : 0 < theta) (ht1 : theta < 1) :
    (∃ x q w, LowCertificate alpha beta lambda theta x q w) ↔
      margin alpha beta lambda theta < 0 := by
  constructor
  · rintro ⟨x,q,w,h⟩
    exact low_certificate_requires_negative_margin alpha beta lambda theta x q w ha hb hl0 h
  · exact negative_margin_has_low_certificate alpha beta lambda theta ha hb hl0 hl1 ht0 ht1

theorem low_share_step (x eta fine q theta : Rat)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (he : 0 ≤ eta) (hf : 0 ≤ fine)
    (hq0 : 0 ≤ q) (hqt : q ≤ theta) (hbound : eta*fine*theta ≤ 1) :
    0 ≤ shareStep x eta (fine*(q-theta)) ∧
      shareStep x eta (fine*(q-theta)) ≤ x := by
  have ht : 0 ≤ 1-x := by grind
  have hgap := Rat.mul_nonneg hf (show 0 ≤ theta-q by grind)
  have hegap := Rat.mul_nonneg he hgap
  have hef := Rat.mul_nonneg he hf
  have hqmul := Rat.mul_nonneg hef hq0
  have htake := Rat.mul_le_mul_of_nonneg_left (show 1-x ≤ 1 by grind) hegap
  have hfactor : 0 ≤ 1-eta*fine*(1-x)*(theta-q) := by grind
  have hlow := Rat.mul_nonneg hx0 hfactor
  have hdec := Rat.mul_nonneg (Rat.mul_nonneg hx0 ht) hegap
  unfold shareStep
  grind

theorem low_quality_step (alpha beta q w qd wd : Rat)
    (_ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hq : q ≤ qd) (hqd : 0 ≤ qd) (hwd : wd ≤ w) (hw1 : w ≤ 1)
    (hbalance : alpha*(1-qd) ≤ beta*wd*qd) :
    0 ≤ qualityStep q alpha beta w 1 0 ∧
      qualityStep q alpha beta w 1 0 ≤ qd := by
  have hbw := Rat.mul_le_mul_of_nonneg_left hw1 hb
  have hc : 0 ≤ 1-alpha-beta*w := by grind
  have hqm := Rat.mul_le_mul_of_nonneg_left hq hc
  have hwm := Rat.mul_le_mul_of_nonneg_left hwd hb
  have hwmq := Rat.mul_le_mul_of_nonneg_right hwm hqd
  have hraw : (1-alpha-beta*w)*q+alpha ≤ qd := by grind
  unfold qualityStep clip01
  grind

theorem low_influence_step (w mu lambda x xd wd : Rat)
    (hwd : wd ≤ w) (hwl : w ≤ lambda) (hm0 : 0 ≤ mu) (hm1 : mu ≤ 1)
    (hl : 0 ≤ lambda) (hx0 : 0 ≤ x) (hxd : x ≤ xd)
    (hreturn : wd ≤ lambda*(1-xd)) :
    wd ≤ influenceStep w mu lambda x ∧ influenceStep w mu lambda x ≤ lambda := by
  have hcoef : 0 ≤ 1-mu := by grind
  have htarget := Rat.mul_le_mul_of_nonneg_left (show 1-xd ≤ 1-x by grind) hl
  have hlower : wd ≤ lambda*(1-x) := by grind
  have hmlo := Rat.mul_le_mul_of_nonneg_left hlower hm0
  have hwlo := Rat.mul_le_mul_of_nonneg_left hwd hcoef
  have hupper := Rat.mul_le_mul_of_nonneg_left (show 1-x ≤ 1 by grind) hl
  have hmhi := Rat.mul_le_mul_of_nonneg_left hupper hm0
  have hwhi := Rat.mul_le_mul_of_nonneg_left hwl hcoef
  unfold influenceStep
  grind

abbrev OperatingState := Rat × Rat × Rat

def step (alpha beta lambda eta fine mu theta : Rat) (s : OperatingState) : OperatingState :=
  (shareStep s.1 eta (fine*(s.2.1-theta)),
   qualityStep s.2.1 alpha beta s.2.2 1 0,
   influenceStep s.2.2 mu lambda s.1)

def LowBox (lambda xd qd wd : Rat) (s : OperatingState) : Prop :=
  0 ≤ s.1 ∧ s.1 ≤ xd ∧ 0 ≤ s.2.1 ∧ s.2.1 ≤ qd ∧ wd ≤ s.2.2 ∧ s.2.2 ≤ lambda

theorem low_box_step (alpha beta lambda eta fine mu theta xd qd wd : Rat)
    (ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (he : 0 ≤ eta) (hf : 0 ≤ fine) (hbound : eta*fine*theta ≤ 1)
    (hm0 : 0 ≤ mu) (hm1 : mu ≤ 1)
    (hc : LowCertificate alpha beta lambda theta xd qd wd)
    (s : OperatingState) (hs : LowBox lambda xd qd wd s) :
    LowBox lambda xd qd wd (step alpha beta lambda eta fine mu theta s) := by
  rcases hc with ⟨_hxd0,hxd1,hqd0,hqdt,_hwd0,_hwd1,hwret,hbalance⟩
  rcases hs with ⟨hx0,hxd,hq0,hqd,hwd,hwl⟩
  have hx := low_share_step s.1 eta fine s.2.1 theta hx0 (by grind) he hf
    hq0 (by grind) hbound
  have hq := low_quality_step alpha beta s.2.1 s.2.2 qd wd ha hb hab
    hqd hqd0 hwd (by grind) hbalance
  have hw := low_influence_step s.2.2 mu lambda s.1 xd wd hwd hwl hm0 hm1 hl0
    hx0 hxd hwret
  unfold LowBox step
  exact ⟨hx.1,by grind,hq.1,hq.2,hw.1,hw.2⟩

def history (f : OperatingState → OperatingState) (s : OperatingState) : Nat → OperatingState
  | 0 => s
  | n+1 => f (history f s n)

theorem low_box_all_times (alpha beta lambda eta fine mu theta xd qd wd : Rat)
    (ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (he : 0 ≤ eta) (hf : 0 ≤ fine) (hbound : eta*fine*theta ≤ 1)
    (hm0 : 0 ≤ mu) (hm1 : mu ≤ 1)
    (hc : LowCertificate alpha beta lambda theta xd qd wd)
    (s : OperatingState) (hs : LowBox lambda xd qd wd s) :
    ∀ n, LowBox lambda xd qd wd (history (step alpha beta lambda eta fine mu theta) s n) := by
  intro n
  induction n with
  | zero => exact hs
  | succ n ih =>
    exact low_box_step alpha beta lambda eta fine mu theta xd qd wd ha hb hab hl0 hl1
      he hf hbound hm0 hm1 hc _ ih

theorem example_below_critical :
    margin (1/4) (1/4) 1 (3/8) = 1/16 := by decide +kernel

theorem example_at_critical :
    margin (1/4) (5/12) 1 (3/8) = 0 := by decide +kernel

theorem example_parameter_boundary (beta : Rat) :
    (0 ≤ margin (1/4) beta 1 (3/8) ↔ beta ≤ 5/12) ∧
    (margin (1/4) beta 1 (3/8) = 0 ↔ beta = 5/12) := by
  unfold margin
  grind

theorem example_above_critical :
    margin (1/4) (1/2) 1 (3/8) = -1/32 ∧
    LowCertificate (1/4) (1/2) 1 (3/8) (1/10) (9/25) (9/10) := by
  unfold margin LowCertificate
  decide +kernel

def RobustFloorProtected (alpha beta lambda theta epsilon : Rat) : Prop :=
  ∀ q w e : Rat, theta ≤ q → q ≤ 1 → 0 ≤ w → w ≤ lambda → 0 ≤ e → e ≤ epsilon →
    theta ≤ qualityStep q alpha beta w 1 e

theorem exact_robust_floor_boundary (alpha beta lambda theta epsilon : Rat)
    (ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hl0 : 0 ≤ lambda) (hl1 : lambda ≤ 1)
    (ht0 : 0 < theta) (ht1 : theta ≤ 1) (he : 0 ≤ epsilon) :
    RobustFloorProtected alpha beta lambda theta epsilon ↔
      epsilon ≤ margin alpha beta lambda theta := by
  constructor
  · intro h
    have hcorner := h theta lambda epsilon (by grind) ht1 hl0 (by grind) he (by grind)
    unfold qualityStep at hcorner
    have hz := (clip_floor_iff _ theta ht0 ht1).mp hcorner
    unfold margin
    grind
  · intro hm q w e hq _hq1 hw0 hw _he0 heps
    apply (quality_preserves_floor q alpha beta w theta lambda e epsilon
      hq (by grind) ht1 ha hb hab hw0 hw (by grind) heps _).1
    unfold margin at hm
    grind

theorem strict_loss_of_renewing_share (eta fine theta xd qd : Rat) (s : OperatingState)
    (he : 0 < eta) (hf : 0 < fine) (hx0 : 0 < s.1) (hxd : s.1 ≤ xd) (hxd1 : xd < 1)
    (hq : s.2.1 ≤ qd) (hqt : qd < theta) :
    shareStep s.1 eta (fine*(s.2.1-theta)) < s.1 := by
  have h := Rat.mul_pos
    (Rat.mul_pos (Rat.mul_pos he hx0) (show 0 < 1-s.1 by grind))
    (Rat.mul_pos hf (show 0 < theta-s.2.1 by grind))
  unfold shareStep
  grind

theorem gap_correspondence (fine theta q lobby cost : Rat)
    (ht : fine*theta = cost-lobby) :
    gap fine q lobby cost = fine*(q-theta) := by
  unfold gap
  grind

end RegimeBoundary
