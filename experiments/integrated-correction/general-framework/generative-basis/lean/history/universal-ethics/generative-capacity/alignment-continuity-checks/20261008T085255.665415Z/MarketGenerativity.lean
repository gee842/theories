import Std

/-! Conditional rational market dynamics. The policy, charges, reserve levy,
measurement bounds, causal stock effects and protected floors are supplied inputs.
No real-limit convergence or empirical applicability claim is encoded here. -/

namespace MarketGenerativity

def clip01 (z : Rat) : Rat := min 1 (max 0 z)
def profitR (price levy cost : Rat) : Rat := price - levy - cost
def profitE (price levy fine q lobby : Rat) : Rat := price - levy - fine*q - lobby
def gap (fine q lobby cost : Rat) : Rat := fine*q+lobby-cost
def shareStep (x eta g : Rat) : Rat := x+eta*x*(1-x)*g
def influenceStep (w mu lambda x : Rat) : Rat := (1-mu)*w+mu*lambda*(1-x)
def installed (budget fee : Rat) : Rat := if fee ≤ budget then 1 else 0
def qualityStep (q alpha beta w u error : Rat) : Rat :=
  clip01 ((1-alpha*u-beta*w)*q+alpha*u-error)
def reserveStep (budget fee levy cap : Rat) : Rat :=
  min cap (budget-fee*installed budget fee+levy)
def reserveSurplus (budget fee levy cap : Rat) : Rat :=
  max 0 (budget-fee*installed budget fee+levy-cap)
def supportStep (stock depreciation renewal damage x baseline shock : Rat) : Rat :=
  max 0 ((1-depreciation)*stock+(renewal+damage)*x-damage-baseline-shock)

theorem profits_difference (price levy cost fine q lobby : Rat) :
    profitR price levy cost - profitE price levy fine q lobby =
      gap fine q lobby cost := by
  unfold profitR profitE gap
  grind

theorem clip_bounds (z : Rat) : 0 ≤ clip01 z ∧ clip01 z ≤ 1 := by
  unfold clip01
  grind

theorem clip_preserves_floor (z floor : Rat) (hf : floor ≤ 1) (hz : floor ≤ z) :
    floor ≤ clip01 z := by
  unfold clip01
  grind

theorem payment_guard (budget fee : Rat) (hb : fee ≤ budget) :
    installed budget fee = 1 ∧ 0 ≤ budget-fee*installed budget fee := by
  simp only [installed, if_pos hb]
  grind

theorem no_unfunded_activation (budget fee : Rat) (hb : budget < fee) :
    installed budget fee = 0 := by
  simp only [installed]
  split <;> grind

theorem reserve_accounting (budget fee levy cap : Rat) :
    reserveStep budget fee levy cap + reserveSurplus budget fee levy cap =
      budget-fee*installed budget fee+levy := by
  unfold reserveStep reserveSurplus
  grind

theorem reserve_preserves_floor (budget fee levy cap : Rat)
    (hb : fee ≤ budget) (hl : fee ≤ levy) (hc : fee ≤ cap) :
    fee ≤ reserveStep budget fee levy cap ∧ reserveStep budget fee levy cap ≤ cap := by
  simp only [reserveStep, installed, if_pos hb]
  grind

theorem gap_monotone (fine q floor lobby cost : Rat)
    (hf : 0 ≤ fine) (hq : floor ≤ q) :
    gap fine floor lobby cost ≤ gap fine q lobby cost := by
  have h := Rat.mul_le_mul_of_nonneg_left hq hf
  unfold gap
  grind

theorem share_step_bounds (x eta g : Rat)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (he : 0 ≤ eta)
    (hg : 0 ≤ g) (hs : eta*g ≤ 1) :
    x ≤ shareStep x eta g ∧ shareStep x eta g ≤ 1 := by
  have hz := Rat.mul_nonneg he hg
  have ht : 0 ≤ 1-x := by grind
  have hp := Rat.mul_nonneg hx0 ht
  have hn := Rat.mul_nonneg hp hz
  have hb := Rat.mul_le_mul_of_nonneg_left hs hx0
  have hu : x*(eta*g) ≤ 1 := by grind
  have hm := Rat.mul_le_mul_of_nonneg_right hu ht
  unfold shareStep
  grind

theorem share_strictly_increases (x eta g : Rat)
    (hx0 : 0 < x) (hx1 : x < 1) (he : 0 < eta) (hg : 0 < g) :
    x < shareStep x eta g := by
  have ht : 0 < 1-x := by grind
  have h := Rat.mul_pos (Rat.mul_pos (Rat.mul_pos he hx0) ht) hg
  unfold shareStep
  grind

theorem influence_preserves_ceiling (w mu lambda x xb wb : Rat)
    (hw0 : 0 ≤ w) (hw : w ≤ wb) (hm0 : 0 ≤ mu) (hm1 : mu ≤ 1)
    (hl : 0 ≤ lambda) (hx : xb ≤ x) (hx1 : x ≤ 1)
    (hboundary : lambda*(1-xb) ≤ wb) :
    0 ≤ influenceStep w mu lambda x ∧ influenceStep w mu lambda x ≤ wb := by
  have hm : 0 ≤ 1-mu := by grind
  have ht : 0 ≤ 1-x := by grind
  have htarget := Rat.mul_nonneg hl ht
  have hn1 := Rat.mul_nonneg hm hw0
  have hn2 := Rat.mul_nonneg hm0 htarget
  have hdiff : 1-x ≤ 1-xb := by grind
  have htargetb := Rat.mul_le_mul_of_nonneg_left hdiff hl
  have htargetb' : lambda*(1-x) ≤ wb := by grind
  have hb1 := Rat.mul_le_mul_of_nonneg_left hw hm
  have hb2 := Rat.mul_le_mul_of_nonneg_left htargetb' hm0
  unfold influenceStep
  grind

theorem quality_preserves_floor (q alpha beta w qb wb error epsilon : Rat)
    (hq : qb ≤ q) (hqb0 : 0 ≤ qb) (hqb1 : qb ≤ 1)
    (_ha : 0 ≤ alpha) (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (_hw0 : 0 ≤ w) (hw : w ≤ wb) (hw1 : w ≤ 1)
    (herr : error ≤ epsilon)
    (hboundary : beta*wb*qb+epsilon ≤ alpha*(1-qb)) :
    qb ≤ qualityStep q alpha beta w 1 error ∧
      qualityStep q alpha beta w 1 error ≤ 1 := by
  have hbw := Rat.mul_le_mul_of_nonneg_left hw1 hb
  have hcoef : 0 ≤ 1-alpha-beta*w := by grind
  have hqmul := Rat.mul_le_mul_of_nonneg_left hq hcoef
  have hbw' := Rat.mul_le_mul_of_nonneg_left hw hb
  have hwbq := Rat.mul_le_mul_of_nonneg_right hbw' hqb0
  have hraw : qb ≤ (1-alpha-beta*w)*q+alpha-error := by grind
  have hlo := clip_preserves_floor _ qb hqb1 hraw
  have hhi := (clip_bounds ((1-alpha-beta*w)*q+alpha-error)).2
  unfold qualityStep
  simpa only [Rat.mul_one] using And.intro hlo hhi

theorem support_preserves_floor
    (stock depreciation renewal damage x baseline shock xb floor nu : Rat)
    (hstock : floor ≤ stock) (hd : depreciation ≤ 1)
    (hrd : 0 ≤ renewal+damage) (hx : xb ≤ x) (hv : shock ≤ nu)
    (hboundary : depreciation*floor ≤ (renewal+damage)*xb-damage-baseline-nu) :
    floor ≤ supportStep stock depreciation renewal damage x baseline shock := by
  have hc : 0 ≤ 1-depreciation := by grind
  have hs := Rat.mul_le_mul_of_nonneg_left hstock hc
  have hx' := Rat.mul_le_mul_of_nonneg_left hx hrd
  have hraw : floor ≤ (1-depreciation)*stock+(renewal+damage)*x-damage-baseline-shock := by
    grind
  unfold supportStep
  grind

structure Parameters (n : Nat) where
  (price levy cost fine lobby eta alpha beta mu lambda fee cap : Rat)
  (depreciation renewal damage baseline : Fin n → Rat)
  essential : Fin n → Bool

structure Bounds (n : Nat) where
  (xb qb wb epsilon : Rat)
  (floor nu : Fin n → Rat)

structure State (n : Nat) where
  (x q w budget : Rat)
  stock : Fin n → Rat

structure Disturbance (n : Nat) where
  error : Rat
  shock : Fin n → Rat

structure Certificate {n : Nat} (p : Parameters n) (b : Bounds n) : Prop where
  xb_nonneg : 0 ≤ b.xb
  qb_nonneg : 0 ≤ b.qb
  qb_le_one : b.qb ≤ 1
  wb_le_one : b.wb ≤ 1
  eta_nonneg : 0 ≤ p.eta
  fine_nonneg : 0 ≤ p.fine
  nonnegative_gap : 0 ≤ gap p.fine b.qb p.lobby p.cost
  step_limit : p.eta*(p.fine+p.lobby-p.cost) ≤ 1
  alpha_nonneg : 0 ≤ p.alpha
  beta_nonneg : 0 ≤ p.beta
  alpha_beta_limit : p.alpha+p.beta ≤ 1
  mu_nonneg : 0 ≤ p.mu
  mu_le_one : p.mu ≤ 1
  lambda_nonneg : 0 ≤ p.lambda
  influence_boundary : p.lambda*(1-b.xb) ≤ b.wb
  correction_boundary : p.beta*b.wb*b.qb+b.epsilon ≤ p.alpha*(1-b.qb)
  levy_covers_fee : p.fee ≤ p.levy
  cap_covers_fee : p.fee ≤ p.cap
  depreciation_le_one : ∀ j, p.depreciation j ≤ 1
  net_effect_nonneg : ∀ j, 0 ≤ p.renewal j+p.damage j
  support_boundary : ∀ j, p.depreciation j*b.floor j ≤
    (p.renewal j+p.damage j)*b.xb-p.damage j-p.baseline j-b.nu j

structure Safe {n : Nat} (p : Parameters n) (b : Bounds n) (s : State n) : Prop where
  x_lower : b.xb ≤ s.x
  x_upper : s.x ≤ 1
  q_lower : b.qb ≤ s.q
  q_upper : s.q ≤ 1
  w_lower : 0 ≤ s.w
  w_upper : s.w ≤ b.wb
  funded : p.fee ≤ s.budget
  reserve_cap : s.budget ≤ p.cap
  supports : ∀ j, b.floor j ≤ s.stock j

def Admissible {n : Nat} (b : Bounds n) (d : Disturbance n) : Prop :=
  d.error ≤ b.epsilon ∧ ∀ j, d.shock j ≤ b.nu j

def operatingStep {n : Nat} (p : Parameters n) (s : State n) (d : Disturbance n) : State n :=
  { x := shareStep s.x p.eta (gap p.fine s.q p.lobby p.cost)
    q := qualityStep s.q p.alpha p.beta s.w (installed s.budget p.fee) d.error
    w := influenceStep s.w p.mu p.lambda s.x
    budget := reserveStep s.budget p.fee p.levy p.cap
    stock := fun j => supportStep (s.stock j) (p.depreciation j) (p.renewal j)
      (p.damage j) s.x (p.baseline j) (d.shock j) }

theorem rectangle_one_step {n : Nat} (p : Parameters n) (b : Bounds n)
    (s : State n) (d : Disturbance n) (hc : Certificate p b)
    (hs : Safe p b s) (hd : Admissible b d) :
    Safe p b (operatingStep p s d) := by
  have hx0 : 0 ≤ s.x := by have := hc.xb_nonneg; have := hs.x_lower; grind
  have hg0 : 0 ≤ gap p.fine s.q p.lobby p.cost := by
    have := gap_monotone p.fine s.q b.qb p.lobby p.cost hc.fine_nonneg hs.q_lower
    have := hc.nonnegative_gap
    grind
  have hg1 : gap p.fine s.q p.lobby p.cost ≤ p.fine+p.lobby-p.cost := by
    have := Rat.mul_le_mul_of_nonneg_left hs.q_upper hc.fine_nonneg
    unfold gap
    grind
  have hetag : p.eta*gap p.fine s.q p.lobby p.cost ≤ 1 := by
    have := Rat.mul_le_mul_of_nonneg_left hg1 hc.eta_nonneg
    have := hc.step_limit
    grind
  have hx := share_step_bounds s.x p.eta _ hx0 hs.x_upper hc.eta_nonneg hg0 hetag
  have hw := influence_preserves_ceiling s.w p.mu p.lambda s.x b.xb b.wb
    hs.w_lower hs.w_upper hc.mu_nonneg hc.mu_le_one hc.lambda_nonneg
    hs.x_lower hs.x_upper hc.influence_boundary
  have hw1 : s.w ≤ 1 := by have := hs.w_upper; have := hc.wb_le_one; grind
  have hq := quality_preserves_floor s.q p.alpha p.beta s.w b.qb b.wb
    d.error b.epsilon hs.q_lower hc.qb_nonneg hc.qb_le_one
    hc.alpha_nonneg hc.beta_nonneg hc.alpha_beta_limit hs.w_lower hs.w_upper hw1
    hd.1 hc.correction_boundary
  have hpay := (payment_guard s.budget p.fee hs.funded).1
  have hb := reserve_preserves_floor s.budget p.fee p.levy p.cap
    hs.funded hc.levy_covers_fee hc.cap_covers_fee
  constructor
  · change b.xb ≤ shareStep s.x p.eta _
    have := hs.x_lower
    grind
  · exact hx.2
  · change b.qb ≤ qualityStep s.q p.alpha p.beta s.w (installed s.budget p.fee) d.error
    rw [hpay]
    exact hq.1
  · change qualityStep s.q p.alpha p.beta s.w (installed s.budget p.fee) d.error ≤ 1
    rw [hpay]
    exact hq.2
  · exact hw.1
  · exact hw.2
  · exact hb.1
  · exact hb.2
  · intro j
    exact support_preserves_floor _ _ _ _ _ _ _ _ _ _
      (hs.supports j) (hc.depreciation_le_one j) (hc.net_effect_nonneg j)
      hs.x_lower (hd.2 j) (hc.support_boundary j)

def history {n : Nat} (p : Parameters n) (initial : State n)
    (disturbances : Nat → Disturbance n) : Nat → State n
  | 0 => initial
  | t+1 => operatingStep p (history p initial disturbances t) (disturbances t)

theorem rectangle_all_times {n : Nat} (p : Parameters n) (b : Bounds n)
    (initial : State n) (disturbances : Nat → Disturbance n)
    (hc : Certificate p b) (h0 : Safe p b initial)
    (hd : ∀ t, Admissible b (disturbances t)) :
    ∀ t, Safe p b (history p initial disturbances t) := by
  intro t
  induction t with
  | zero => exact h0
  | succ t ih => exact rectangle_one_step p b _ _ hc ih (hd t)

def essentialReady {n : Nat} (p : Parameters n) (b : Bounds n) (s : State n) : Prop :=
  ∀ j, p.essential j = true → b.floor j ≤ s.stock j

instance {n : Nat} (p : Parameters n) (b : Bounds n) (s : State n) :
    Decidable (essentialReady p b s) :=
  inferInstanceAs (Decidable (∀ j, p.essential j = true → b.floor j ≤ s.stock j))

def guardedStep {n : Nat} (p : Parameters n) (b : Bounds n)
    (d : Disturbance n) : Option (State n) → Option (State n)
  | none => none
  | some s => if essentialReady p b s ∧ essentialReady p b (operatingStep p s d)
      then some (operatingStep p s d) else none

theorem viable_guarded_step {n : Nat} (p : Parameters n) (b : Bounds n)
    (s : State n) (d : Disturbance n) (hc : Certificate p b)
    (hs : Safe p b s) (hd : Admissible b d) :
    guardedStep p b d (some s) = some (operatingStep p s d) := by
  have h : essentialReady p b s := fun j _ => hs.supports j
  have hnext := rectangle_one_step p b s d hc hs hd
  have h' : essentialReady p b (operatingStep p s d) := fun j _ => hnext.supports j
  simp [guardedStep, h, h']

theorem failed_market_absorbing {n : Nat} (p : Parameters n) (b : Bounds n)
    (d : Disturbance n) : guardedStep p b d none = none := by rfl

def guardedHistory {n : Nat} (p : Parameters n) (b : Bounds n)
    (initial : State n) (disturbances : Nat → Disturbance n) : Nat → Option (State n)
  | 0 => some initial
  | t+1 => guardedStep p b (disturbances t) (guardedHistory p b initial disturbances t)

theorem safe_history_never_fails {n : Nat} (p : Parameters n) (b : Bounds n)
    (initial : State n) (disturbances : Nat → Disturbance n)
    (hc : Certificate p b) (h0 : Safe p b initial)
    (hd : ∀ t, Admissible b (disturbances t)) :
    ∀ t, guardedHistory p b initial disturbances t =
      some (history p initial disturbances t) := by
  intro t
  induction t with
  | zero => rfl
  | succ t ih =>
    simp only [guardedHistory, ih, history]
    exact viable_guarded_step p b _ _ hc
      (rectangle_all_times p b initial disturbances hc h0 hd t) (hd t)

/- A fully rational instantiation, independently checkable by kernel reduction. -/
def exampleParameters : Parameters 1 :=
  { price := 10, levy := 1, cost := 2, fine := 4, lobby := 1/2,
    eta := 1/5, alpha := 1/4, beta := 1/2, mu := 1/4, lambda := 1,
    fee := 1, cap := 3, depreciation := fun _ => 1/10,
    renewal := fun _ => 2, damage := fun _ => 1, baseline := fun _ => 0,
    essential := fun _ => true }

def exampleBounds : Bounds 1 :=
  { xb := 3/4, qb := 1/2, wb := 1/4, epsilon := 1/20,
    floor := fun _ => 5, nu := fun _ => 1/2 }

def exampleState : State 1 :=
  { x := 3/4, q := 1/2, w := 1/4, budget := 1, stock := fun _ => 5 }

def exampleWorstShock : Disturbance 1 :=
  { error := 1/20, shock := fun _ => 1/2 }

theorem example_certificate : Certificate exampleParameters exampleBounds := by
  constructor <;> decide +kernel

theorem example_safe : Safe exampleParameters exampleBounds exampleState := by
  constructor <;> decide +kernel

theorem example_worst_admissible : Admissible exampleBounds exampleWorstShock := by
  unfold Admissible
  decide +kernel

theorem example_strict_gap :
    gap exampleParameters.fine exampleBounds.qb exampleParameters.lobby
      exampleParameters.cost = 1/2 := by decide +kernel

theorem example_one_step :
    (operatingStep exampleParameters exampleState exampleWorstShock).x = 123/160 ∧
    (operatingStep exampleParameters exampleState exampleWorstShock).q = 41/80 ∧
    (operatingStep exampleParameters exampleState exampleWorstShock).w = 1/4 ∧
    (operatingStep exampleParameters exampleState exampleWorstShock).budget = 1 ∧
    (operatingStep exampleParameters exampleState exampleWorstShock).stock 0 = 21/4 := by
  decide +kernel

theorem example_arbitrary_history (disturbances : Nat → Disturbance 1)
    (hd : ∀ t, Admissible exampleBounds (disturbances t)) :
    ∀ t, Safe exampleParameters exampleBounds
      (history exampleParameters exampleState disturbances t) :=
  rectangle_all_times exampleParameters exampleBounds exampleState disturbances
    example_certificate example_safe hd

theorem example_threshold (q : Rat) :
    0 < gap 4 q (1/2) 2 ↔ 3/8 < q := by
  unfold gap
  grind

theorem profitable_depletion :
    0 < profitE 10 1 4 (9/25) (1/2) ∧
    profitR 10 1 2 < profitE 10 1 4 (9/25) (1/2) ∧
    supportStep 5 (1/10) 2 1 (1/10) 0 0 = 19/5 ∧
    shareStep (1/10) (1/5) (gap 4 (9/25) (1/2) 2) < 1/10 := by
  decide +kernel

theorem capture_overwhelms_correction :
    0 < gap 4 (2/5) (1/2) 2 ∧
    qualityStep (2/5) (1/4) (1/2) 1 1 0 = 7/20 ∧
    gap 4 (qualityStep (2/5) (1/4) (1/2) 1 1 0) (1/2) 2 < 0 := by
  decide +kernel

theorem later_receipt_cannot_pay_earlier_correction :
    installed (1/2) 1 = 0 ∧ reserveStep (1/2) 1 1 3 = 3/2 ∧
    qualityStep (1/2) (1/4) (1/2) (1/4) (installed (1/2) 1) 0 = 7/16 ∧
    qualityStep (1/2) (1/4) (1/2) (1/4) (installed (1/2) 1) 0 < 1/2 := by
  decide +kernel

theorem one_support_cannot_substitute_for_another :
    supportStep 5 (1/10) 2 1 1 0 0 = 13/2 ∧
    supportStep 5 (1/10) 0 1 1 0 0 = 9/2 ∧
    5 < (supportStep 5 (1/10) 2 1 1 0 0 + supportStep 5 (1/10) 0 1 1 0 0)/2 ∧
    supportStep 5 (1/10) 0 1 1 0 0 < 5 := by
  decide +kernel

theorem no_entry_at_zero : shareStep 0 (1/5) (gap 4 1 (1/2) 2) = 0 := by
  decide +kernel

theorem budget_overflow_is_not_creation :
    reserveStep 3 1 2 3 = 3 ∧ reserveSurplus 3 1 2 3 = 1 := by
  decide +kernel

theorem market_uses_accounting (price levy cost fine q lobby x : Rat) :
    x*profitR price levy cost+(1-x)*profitE price levy fine q lobby + levy +
      x*cost+(1-x)*fine*q+(1-x)*lobby = price := by
  unfold profitR profitE
  grind

theorem funded_total_accounting (price levy cost fine q lobby x budget fee cap : Rat) :
    x*profitR price levy cost+(1-x)*profitE price levy fine q lobby +
      (reserveStep budget fee levy cap-budget) +
      reserveSurplus budget fee levy cap+fee*installed budget fee +
      x*cost+(1-x)*fine*q+(1-x)*lobby = price := by
  have h := reserve_accounting budget fee levy cap
  have h' := market_uses_accounting price levy cost fine q lobby x
  grind

/- A collar may recover into the stricter rectangle in a single funded step.
   The comparison is an interval proof, not a selected endpoint simulation. -/
theorem quality_corner_lower (q alpha beta w q0 w0 error epsilon target : Rat)
    (hq : q0 ≤ q) (hq0 : 0 ≤ q0) (ht : target ≤ 1)
    (hb : 0 ≤ beta) (hab : alpha+beta ≤ 1)
    (hw : w ≤ w0) (hw1 : w ≤ 1) (herr : error ≤ epsilon)
    (hcorner : target ≤ (1-alpha-beta*w0)*q0+alpha-epsilon) :
    target ≤ qualityStep q alpha beta w 1 error := by
  have hbw := Rat.mul_le_mul_of_nonneg_left hw1 hb
  have hcoef : 0 ≤ 1-alpha-beta*w := by grind
  have hqmul := Rat.mul_le_mul_of_nonneg_left hq hcoef
  have hbw' := Rat.mul_le_mul_of_nonneg_left hw hb
  have hwbq := Rat.mul_le_mul_of_nonneg_right hbw' hq0
  have hraw : target ≤ (1-alpha-beta*w)*q+alpha-error := by grind
  have hlo := clip_preserves_floor _ target ht hraw
  unfold qualityStep
  simpa only [Rat.mul_one] using hlo

theorem influence_corner_upper (w mu lambda x w0 x0 target : Rat)
    (hw : w ≤ w0) (hm0 : 0 ≤ mu) (hm1 : mu ≤ 1)
    (hl : 0 ≤ lambda) (hx : x0 ≤ x)
    (hcorner : (1-mu)*w0+mu*lambda*(1-x0) ≤ target) :
    influenceStep w mu lambda x ≤ target := by
  have hm : 0 ≤ 1-mu := by grind
  have hdiff : 1-x ≤ 1-x0 := by grind
  have htarget := Rat.mul_le_mul_of_nonneg_left hdiff hl
  have hb1 := Rat.mul_le_mul_of_nonneg_left hw hm
  have hb2 := Rat.mul_le_mul_of_nonneg_left htarget hm0
  unfold influenceStep
  grind

def collarBounds : Bounds 1 :=
  { exampleBounds with xb := 4/5, qb := 49/100, wb := 13/50 }

theorem collar_certificate : Certificate exampleParameters collarBounds := by
  constructor <;> decide +kernel

theorem collar_recovers (s : State 1) (d : Disturbance 1)
    (hs : Safe exampleParameters collarBounds s)
    (hd : Admissible exampleBounds d) :
    Safe exampleParameters exampleBounds (operatingStep exampleParameters s d) := by
  have hd' : Admissible collarBounds d := hd
  have hnext := rectangle_one_step exampleParameters collarBounds s d
    collar_certificate hs hd'
  have hx : (3/4 : Rat) ≤ (operatingStep exampleParameters s d).x := by
    have h := hnext.x_lower
    change (4/5 : Rat) ≤ _ at h
    grind
  have hw1 : s.w ≤ 1 := by
    have h := hs.w_upper
    change s.w ≤ (13/50 : Rat) at h
    grind
  have hq := quality_corner_lower s.q (1/4) (1/2) s.w (49/100) (13/50)
    d.error (1/20) (1/2) hs.q_lower (by decide +kernel) (by decide +kernel)
    (by decide +kernel) (by decide +kernel) hs.w_upper hw1 hd.1 (by decide +kernel)
  have hw := influence_corner_upper s.w (1/4) 1 s.x (13/50) (4/5) (1/4)
    hs.w_upper (by decide +kernel) (by decide +kernel) (by decide +kernel)
    hs.x_lower (by decide +kernel)
  have hpay := (payment_guard s.budget exampleParameters.fee hs.funded).1
  constructor
  · exact hx
  · exact hnext.x_upper
  · change (1/2 : Rat) ≤ qualityStep s.q (1/4) (1/2) s.w (installed s.budget 1) d.error
    change installed s.budget 1 = 1 at hpay
    rw [hpay]
    exact hq
  · exact hnext.q_upper
  · exact hnext.w_lower
  · exact hw
  · exact hnext.funded
  · exact hnext.reserve_cap
  · exact hnext.supports

def exclusionParameters : Parameters 2 :=
  { price := 10, levy := 1, cost := 2, fine := 4, lobby := 1/2,
    eta := 1/5, alpha := 1/4, beta := 1/2, mu := 1/4, lambda := 1,
    fee := 1, cap := 3, depreciation := fun _ => 1/10,
    renewal := fun j => if j = 0 then 2 else 0,
    damage := fun _ => 1, baseline := fun _ => 0,
    essential := fun j => j = 0 }

def exclusionBounds : Bounds 2 :=
  { xb := 3/4, qb := 1/2, wb := 1/4, epsilon := 1/20,
    floor := fun _ => 5, nu := fun _ => 0 }

def exclusionState : State 2 :=
  { x := 1, q := 1, w := 0, budget := 1, stock := fun _ => 5 }

def exclusionDisturbance : Disturbance 2 :=
  { error := 0, shock := fun _ => 0 }

theorem excluded_recipient_is_harmed :
    (operatingStep exclusionParameters exclusionState exclusionDisturbance).stock 1 <
      exclusionBounds.floor 1 := by decide +kernel

theorem excluded_recipient_harm_does_not_stop_market :
    guardedStep exclusionParameters exclusionBounds exclusionDisturbance (some exclusionState) =
      some (operatingStep exclusionParameters exclusionState exclusionDisturbance) := by
  have h : essentialReady exclusionParameters exclusionBounds exclusionState ∧
      essentialReady exclusionParameters exclusionBounds
        (operatingStep exclusionParameters exclusionState exclusionDisturbance) := by
    unfold essentialReady
    decide +kernel
  simp [guardedStep, h]

end MarketGenerativity

#print axioms MarketGenerativity.profits_difference
#print axioms MarketGenerativity.clip_bounds
#print axioms MarketGenerativity.clip_preserves_floor
#print axioms MarketGenerativity.payment_guard
#print axioms MarketGenerativity.no_unfunded_activation
#print axioms MarketGenerativity.reserve_accounting
#print axioms MarketGenerativity.reserve_preserves_floor
#print axioms MarketGenerativity.gap_monotone
#print axioms MarketGenerativity.share_step_bounds
#print axioms MarketGenerativity.share_strictly_increases
#print axioms MarketGenerativity.influence_preserves_ceiling
#print axioms MarketGenerativity.quality_preserves_floor
#print axioms MarketGenerativity.support_preserves_floor
#print axioms MarketGenerativity.rectangle_one_step
#print axioms MarketGenerativity.rectangle_all_times
#print axioms MarketGenerativity.viable_guarded_step
#print axioms MarketGenerativity.failed_market_absorbing
#print axioms MarketGenerativity.safe_history_never_fails
#print axioms MarketGenerativity.example_certificate
#print axioms MarketGenerativity.example_safe
#print axioms MarketGenerativity.example_worst_admissible
#print axioms MarketGenerativity.example_strict_gap
#print axioms MarketGenerativity.example_one_step
#print axioms MarketGenerativity.example_arbitrary_history
#print axioms MarketGenerativity.example_threshold
#print axioms MarketGenerativity.profitable_depletion
#print axioms MarketGenerativity.capture_overwhelms_correction
#print axioms MarketGenerativity.later_receipt_cannot_pay_earlier_correction
#print axioms MarketGenerativity.one_support_cannot_substitute_for_another
#print axioms MarketGenerativity.no_entry_at_zero
#print axioms MarketGenerativity.budget_overflow_is_not_creation
#print axioms MarketGenerativity.market_uses_accounting
#print axioms MarketGenerativity.funded_total_accounting
#print axioms MarketGenerativity.quality_corner_lower
#print axioms MarketGenerativity.influence_corner_upper
#print axioms MarketGenerativity.collar_certificate
#print axioms MarketGenerativity.collar_recovers
#print axioms MarketGenerativity.excluded_recipient_is_harmed
#print axioms MarketGenerativity.excluded_recipient_harm_does_not_stop_market
