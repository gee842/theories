import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Tactic

/- A source-mapped developmental law, not an ethical objective or a universal
physics. A coefficient may start at zero; its perturbation changes subsequent
activity through the same recurrence. Parameter differentiation holds the stated
initial profile, other coefficients and law constants fixed. -/
noncomputable section
open scoped BigOperators

namespace ConnectionistRecovery

abbrev Profile (n : Nat) := Fin n → ℝ
abbrev Network (n : Nat) := Fin n → Fin n → ℝ

def input {n : Nat} (B : Network n) (p : Profile n) (i : Fin n) : ℝ :=
  ∑ j, B i j * p j

def perturb {n : Nat} (B : Network n) (a b : Fin n) (w : ℝ) : Network n :=
  fun i j => B i j + if i = a ∧ j = b then w else 0

def step {n : Nat} (σ : ℝ → ℝ) (τ δ : ℝ) (B : Network n)
    (p : Profile n) : Profile n :=
  fun i => (1 - δ) * p i + τ * σ (input B p i)

def develop {n : Nat} (σ : ℝ → ℝ) (τ δ : ℝ) (B : Network n)
    (g : Profile n) : Nat → Profile n
  | 0 => g
  | t + 1 => step σ τ δ B (develop σ τ δ B g t)

def score {n : Nat} (s p : Profile n) : ℝ := 1 + ∑ i, s i * p i

theorem input_perturb {n : Nat} (B : Network n) (p : Profile n)
    (a b i : Fin n) (w : ℝ) :
    input (perturb B a b w) p i = input B p i + if i = a then w * p b else 0 := by
  classical
  by_cases h : i = a
  · subst i
    simp [input, perturb, add_mul, Finset.sum_add_distrib]
  · simp [input, perturb, h]

theorem one_step_difference {n : Nat} (B : Network n) (g : Profile n)
    (a b i : Fin n) (τ δ w : ℝ) :
    step id τ δ (perturb B a b w) g i - step id τ δ B g i =
      if i = a then τ * w * g b else 0 := by
  rw [step, step, input_perturb]
  split_ifs <;> simp only [id_eq] <;> ring

theorem one_step_score_difference {n : Nat} (B : Network n) (g s : Profile n)
    (a b : Fin n) (τ δ w : ℝ) :
    score s (step id τ δ (perturb B a b w) g) - score s (step id τ δ B g) =
      τ * w * g b * s a := by
  classical
  unfold score
  rw [show (1 + ∑ i, s i * step id τ δ (perturb B a b w) g i) -
      (1 + ∑ i, s i * step id τ δ B g i) =
      ∑ i, s i * (step id τ δ (perturb B a b w) g i - step id τ δ B g i) by
        simp only [mul_sub, Finset.sum_sub_distrib]; ring]
  simp_rw [one_step_difference]
  simp only [mul_ite, mul_zero]
  simp
  ring

theorem beneficial_iff_hebbian {n : Nat} (B : Network n) (g s : Profile n)
    (a b : Fin n) (τ δ w m : ℝ) (hτ : 0 < τ) (hm : 0 < m)
    (aligned : g b = m * s b) :
    score s (step id τ δ B g) < score s (step id τ δ (perturb B a b w) g) ↔
      0 < w * s a * s b := by
  rw [← sub_pos, one_step_score_difference, aligned]
  have eqn : τ * w * (m * s b) * s a = (τ * m) * (w * s a * s b) := by ring
  rw [eqn, mul_pos_iff_of_pos_left (mul_pos hτ hm)]

/- Exact sensitivity of the finite nonlinear recurrence, for an arbitrary
differentiable activation. No precomputed effective derivative is an input. -/
def response {n : Nat} (σ σ' : ℝ → ℝ) (τ δ : ℝ) (B : Network n)
    (g : Profile n) (a b : Fin n) (w : ℝ) : Nat → Profile n
  | 0 => fun _ => 0
  | t + 1 => fun i =>
      (1 - δ) * response σ σ' τ δ B g a b w t i +
      τ * σ' (input (perturb B a b w) (develop σ τ δ (perturb B a b w) g t) i) *
        ((if i = a then develop σ τ δ (perturb B a b w) g t b else 0) +
          input (perturb B a b w) (response σ σ' τ δ B g a b w t) i)

theorem coefficient_derivative {n : Nat} (B : Network n) (a b i j : Fin n)
    (w : ℝ) : HasDerivAt (fun x => perturb B a b x i j)
      (if i = a ∧ j = b then 1 else 0) w := by
  by_cases h : i = a ∧ j = b
  · simpa [perturb, h] using (hasDerivAt_id w).const_add (B i j)
  · simpa [perturb, h] using hasDerivAt_const w (B i j)

theorem developmental_response {n : Nat} (σ σ' : ℝ → ℝ)
    (hσ : ∀ x, HasDerivAt σ (σ' x) x) (τ δ : ℝ) (B : Network n)
    (g : Profile n) (a b : Fin n) (w : ℝ) (t : Nat) (i : Fin n) :
    HasDerivAt (fun x => develop σ τ δ (perturb B a b x) g t i)
      (response σ σ' τ δ B g a b w t i) w := by
  classical
  induction t generalizing i with
  | zero => simpa [develop, response] using hasDerivAt_const w (g i)
  | succ t ih =>
    have hin : HasDerivAt
        (fun x => input (perturb B a b x) (develop σ τ δ (perturb B a b x) g t) i)
        ((if i = a then develop σ τ δ (perturb B a b w) g t b else 0) +
          input (perturb B a b w) (response σ σ' τ δ B g a b w t) i) w := by
      have hsum := HasDerivAt.fun_sum (u := Finset.univ)
        (fun j _ => (coefficient_derivative B a b i j w).mul (ih j))
      convert hsum using 1
      simp only [Finset.sum_add_distrib, input]
      by_cases hia : i = a
      · simp [hia, mul_comm]
      · simp [hia, mul_comm]
    have h := ((ih i).const_mul (1 - δ)).add ((hσ _).comp w hin |>.const_mul τ)
    convert h using 1
    simp only [response]
    ring

theorem tanh_derivative (x : ℝ) :
    HasDerivAt Real.tanh (1 / (Real.cosh x) ^ 2) x := by
  have h := (Real.hasDerivAt_sinh x).div (Real.hasDerivAt_cosh x) (ne_of_gt (Real.cosh_pos x))
  convert h using 1
  · funext y; exact Real.tanh_eq_sinh_div_cosh y
  · have hc := Real.cosh_sq_sub_sinh_sq x
    congr 1
    nlinarith

theorem tanh_developmental_response {n : Nat} (τ δ : ℝ) (B : Network n)
    (g : Profile n) (a b : Fin n) (w : ℝ) (t : Nat) (i : Fin n) :
    HasDerivAt (fun x => develop Real.tanh τ δ (perturb B a b x) g t i)
      (response Real.tanh (fun z => 1 / (Real.cosh z) ^ 2) τ δ B g a b w t i) w :=
  developmental_response _ _ tanh_derivative τ δ B g a b w t i

def netScore {n : Nat} (σ : ℝ → ℝ) (τ δ : ℝ) (B : Network n)
    (g : Profile n) (a b : Fin n) (t : Nat) (s : ℝ → Profile n)
    (cost : ℝ → ℝ) (w : ℝ) : ℝ :=
  score (s w) (develop σ τ δ (perturb B a b w) g t) - cost w

theorem changing_selection_response {n : Nat} (σ σ' : ℝ → ℝ)
    (hσ : ∀ x, HasDerivAt σ (σ' x) x) (τ δ : ℝ) (B : Network n)
    (g : Profile n) (a b : Fin n) (w : ℝ) (t : Nat) (s : ℝ → Profile n)
    (s' : Profile n) (cost : ℝ → ℝ) (cost' : ℝ)
    (hs : ∀ i, HasDerivAt (fun x => s x i) (s' i) w)
    (hc : HasDerivAt cost cost' w) :
    HasDerivAt (netScore σ τ δ B g a b t s cost)
      ((∑ i : Fin n, (s' i * develop σ τ δ (perturb B a b w) g t i +
        s w i * response σ σ' τ δ B g a b w t i)) - cost') w := by
  have hsum := HasDerivAt.fun_sum (u := Finset.univ)
    (fun i _ => (hs i).mul (developmental_response σ σ' hσ τ δ B g a b w t i))
  simpa [netScore, score] using (hsum.const_add 1).sub hc

theorem fixed_selection_response {n : Nat} (σ σ' : ℝ → ℝ)
    (hσ : ∀ x, HasDerivAt σ (σ' x) x) (τ δ : ℝ) (B : Network n)
    (g s : Profile n) (a b : Fin n) (w : ℝ) (t : Nat) :
    HasDerivAt (fun x => score s (develop σ τ δ (perturb B a b x) g t))
      (∑ i, s i * response σ σ' τ δ B g a b w t i) w := by
  simpa [netScore] using changing_selection_response σ σ' hσ τ δ B g a b w t
    (fun _ => s) (fun _ => 0) (fun _ => 0) 0
    (fun i => hasDerivAt_const w (s i)) (hasDerivAt_const w 0)

theorem one_step_cost_threshold {n : Nat} (B : Network n) (g s : Profile n)
    (a b : Fin n) (τ δ w : ℝ) (cost : ℝ → ℝ) :
    score s (step id τ δ B g) - cost 0 <
      score s (step id τ δ (perturb B a b w) g) - cost w ↔
    cost w - cost 0 < τ * w * g b * s a := by
  have h := one_step_score_difference B g s a b τ δ w
  constructor <;> intro hx <;> linarith

def changingRuleExample (w : ℝ) : ℝ :=
  netScore id 1 0 (fun (_ : Fin 1) _ => 0) (fun _ => 1) 0 0 1
    (fun x _ => 1 - 2 * x) (fun _ => 0) w

theorem changed_rule_exact_difference (w : ℝ) :
    changingRuleExample w - changingRuleExample 0 = -w - 2 * w ^ 2 := by
  simp [changingRuleExample, netScore, score, develop, step, input, perturb]
  ring

theorem changing_rule_reverses_gain (w : ℝ) (hw : 0 < w) (hsmall : w < 1/2) :
    0 < 1 - 2 * w ∧ 1 < 1 + w ∧ changingRuleExample w < changingRuleExample 0 := by
  have h := changed_rule_exact_difference w
  have hs := sq_nonneg w
  constructor
  · linarith
  constructor <;> linarith

/- A sufficient condition stated on actual propagated interactions. Signed
orientation allows both co-selected and oppositely selected traits. It does not
assume the response has the desired sign. -/
theorem oriented_input_nonnegative {n : Nat} (B : Network n) (s d : Profile n)
    (r : ℝ) (unit : ∀ j, s j * s j = 1)
    (hB : ∀ i j, 0 ≤ s i * B i j * s j)
    (hd : ∀ j, 0 ≤ r * s j * d j) (i : Fin n) :
    0 ≤ r * s i * input B d i := by
  have eqn : r * s i * input B d i =
      ∑ j, (s i * B i j * s j) * (r * s j * d j) := by
    unfold input
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    calc
      r * s i * (B i j * d j) = (r * s i * B i j * d j) * 1 := by ring
      _ = (r * s i * B i j * d j) * (s j * s j) := by rw [unit]
      _ = _ := by ring
  rw [eqn]
  exact Finset.sum_nonneg (fun j _ => mul_nonneg (hB i j) (hd j))

theorem response_preserves_orientation {n : Nat} (σ σ' : ℝ → ℝ)
    (τ δ : ℝ) (B : Network n) (g s : Profile n) (a b : Fin n)
    (w : ℝ) (T : Nat) (hτ : 0 ≤ τ) (hδ : δ ≤ 1)
    (hσ' : ∀ x, 0 ≤ σ' x) (unit : ∀ i, s i * s i = 1)
    (hB : ∀ i j, 0 ≤ s i * perturb B a b w i j * s j)
    (hp : ∀ t, t < T → 0 ≤ s b * develop σ τ δ (perturb B a b w) g t b)
    (i : Fin n) :
    0 ≤ (s a * s b) * s i * response σ σ' τ δ B g a b w T i := by
  induction T generalizing i with
  | zero => simp [response]
  | succ T ih =>
    have hd : ∀ j, 0 ≤ (s a * s b) * s j * response σ σ' τ δ B g a b w T j := by
      intro j
      exact ih (fun t ht => hp t (Nat.lt_trans ht (Nat.lt_succ_self T))) j
    have hb := oriented_input_nonnegative (perturb B a b w) s
      (response σ σ' τ δ B g a b w T) (s a * s b) unit hB hd i
    have he : 0 ≤ (s a * s b) * s i *
        (if i = a then develop σ τ δ (perturb B a b w) g T b else 0) := by
      by_cases h : i = a
      · subst i
        simp only [ite_true]
        have eqn : (s a * s b) * s a * develop σ τ δ (perturb B a b w) g T b =
            (s a * s a) * (s b * develop σ τ δ (perturb B a b w) g T b) := by ring
        rw [eqn, unit, one_mul]
        exact hp T (Nat.lt_succ_self T)
      · simp [h]
    have hstay := mul_nonneg (sub_nonneg.mpr hδ) (hd i)
    have hchange := mul_nonneg (mul_nonneg hτ (hσ' (input (perturb B a b w) (develop σ τ δ (perturb B a b w) g T) i))) (add_nonneg he hb)
    simp only [response]
    nlinarith only [hstay, hchange]

theorem terminal_response_orientation {n : Nat} (σ σ' : ℝ → ℝ)
    (τ δ : ℝ) (B : Network n) (g s : Profile n) (a b : Fin n)
    (w : ℝ) (T : Nat) (hτ : 0 ≤ τ) (hδ : δ ≤ 1)
    (hσ' : ∀ x, 0 ≤ σ' x) (unit : ∀ i, s i * s i = 1)
    (hB : ∀ i j, 0 ≤ s i * perturb B a b w i j * s j)
    (hp : ∀ t, t < T → 0 ≤ s b * develop σ τ δ (perturb B a b w) g t b) :
    0 ≤ (s a * s b) * ∑ i, s i * response σ σ' τ δ B g a b w T i := by
  rw [Finset.mul_sum]
  apply Finset.sum_nonneg
  intro i _
  simpa only [mul_assoc] using
    response_preserves_orientation σ σ' τ δ B g s a b w T hτ hδ hσ' unit hB hp i

theorem recurrent_hebbian_direction {n : Nat} (σ σ' : ℝ → ℝ)
    (hσ : ∀ x, HasDerivAt σ (σ' x) x) (τ δ : ℝ) (B : Network n)
    (g s : Profile n) (a b : Fin n) (w : ℝ) (T : Nat)
    (hτ : 0 ≤ τ) (hδ : δ ≤ 1) (hσ' : ∀ x, 0 ≤ σ' x)
    (unit : ∀ i, s i * s i = 1)
    (hB : ∀ i j, 0 ≤ s i * perturb B a b w i j * s j)
    (hp : ∀ t, t < T → 0 ≤ s b * develop σ τ δ (perturb B a b w) g t b) :
    0 ≤ (s a * s b) * deriv
      (fun x => score s (develop σ τ δ (perturb B a b x) g T)) w := by
  rw [(fixed_selection_response σ σ' hσ τ δ B g s a b w T).deriv]
  exact terminal_response_orientation σ σ' τ δ B g s a b w T hτ hδ hσ' unit hB hp

/- An exact finite adverse case: a positive link absent at w=0 is formed.
Its first-step effect is positive but the recurrent native route reverses its
terminal effect. Initial and adult traits both agree with positive selection. -/
def adverseNetwork : Network 2 := fun i j => if i = 0 ∧ j = 0 then -3 else 0
def ones : Profile 2 := fun _ => 1

theorem adverse_initial_alignment : ∀ i : Fin 2, 0 < ones i := by
  intro i; norm_num [ones]

theorem adverse_link_initially_absent : adverseNetwork 0 1 = 0 := by
  norm_num [adverseNetwork]

theorem adverse_first_step (w : ℝ) :
    develop id 1 0 (perturb adverseNetwork 0 1 w) ones 1 0 = -2 + w := by
  norm_num [develop, step, input, perturb, adverseNetwork, ones, Fin.sum_univ_two]
  ring

theorem adverse_second_step (w : ℝ) :
    develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2 0 = 4 - w ∧
    develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2 1 = 1 := by
  norm_num [develop, step, input, perturb, adverseNetwork, ones, Fin.sum_univ_two]
  ring

theorem adverse_score_difference (w : ℝ) :
    score ones (develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2) -
      score ones (develop id 1 0 adverseNetwork ones 2) = -w := by
  norm_num [score, develop, step, input, perturb, adverseNetwork, ones, Fin.sum_univ_two]
  ring

theorem positive_formation_can_reduce_score (w : ℝ) (hw : 0 < w) (hsmall : w < 4) :
    (∀ i, 0 < develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2 i) ∧
    score ones (develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2) <
      score ones (develop id 1 0 adverseNetwork ones 2) := by
  constructor
  · intro i
    fin_cases i
    · change 0 < develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2 0
      rw [(adverse_second_step w).1]; linarith
    · change 0 < develop id 1 0 (perturb adverseNetwork 0 1 w) ones 2 1
      rw [(adverse_second_step w).2]; norm_num
  · have h := adverse_score_difference w
    linarith

end ConnectionistRecovery
