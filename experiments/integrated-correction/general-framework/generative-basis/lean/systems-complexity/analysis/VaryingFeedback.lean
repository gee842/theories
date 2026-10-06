import AdaptiveCore

/-! A common envelope for the existing delayed plant under time-varying gains.
No rate of gain change, convergence of the gain, or independence from the state
is assumed. The gain interval is a supplied admissibility condition. A physical
application must establish how paid accessible information actually selects and
supports the realized schedule. -/
namespace SystemsComplexity.VaryingFeedback

noncomputable section
open Filter
open scoped Topology
open AdaptiveCore
open RealFeedback (delayedStep squaredNorm)

theorem envelope_nonnegative (s : ℝ × ℝ) : 0 ≤ envelope s := by
  exact le_trans (abs_nonneg s.1) (le_max_left _ _)

theorem envelope_bounds (s : ℝ × ℝ) :
    |s.1| ≤ envelope s ∧ |s.2| ≤ envelope s ∧ |s.1-s.2| ≤ envelope s := by
  exact ⟨le_max_left _ _, le_trans (le_max_left _ _) (le_max_right _ _),
    le_trans (le_max_right _ _) (le_max_right _ _)⟩

theorem envelope_le_iff (s : ℝ × ℝ) (B : ℝ) :
    envelope s ≤ B ↔ |s.1| ≤ B ∧ |s.2| ≤ B ∧ |s.1-s.2| ≤ B := by
  simp only [envelope, max_le_iff]

theorem weighted_abs_bound {a b x y B : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hx : |x| ≤ B) (hy : |y| ≤ B) :
    |a*x+b*y| ≤ (a+b)*B := by
  calc
    |a*x+b*y| ≤ |a*x|+|b*y| := abs_add_le _ _
    _ = a*|x|+b*|y| := by rw [abs_mul, abs_mul, abs_of_nonneg ha, abs_of_nonneg hb]
    _ ≤ a*B+b*B := add_le_add (mul_le_mul_of_nonneg_left hx ha)
      (mul_le_mul_of_nonneg_left hy hb)
    _ = (a+b)*B := by ring

theorem convex_abs_bound {a x y B : ℝ} (ha : 0 ≤ a) (ha1 : a ≤ 1)
    (hx : |x| ≤ B) (hy : |y| ≤ B) :
    |(1-a)*x+a*y| ≤ B := by
  have h := weighted_abs_bound (show 0 ≤ 1-a by linarith) ha hx hy
  convert h using 1; ring

/-- Each permitted step preserves the same envelope, without freezing its gain. -/
theorem step_nonincrease {k : ℝ} (hk : 0 ≤ k) (hk1 : k ≤ 1) (s : ℝ × ℝ) :
    envelope (delayedStep k s) ≤ envelope s := by
  have hb := envelope_bounds s
  have h0 := envelope_nonnegative s
  apply (envelope_le_iff _ _).mpr
  simp only [delayedStep]
  refine ⟨?_, hb.1, ?_⟩
  · have h := convex_abs_bound hk hk1 hb.1 hb.2.2
    convert h using 1; congr 1; ring
  · have heq : s.1-k*s.2-s.1 = -(k*s.2) := by ring
    rw [heq, abs_neg, abs_mul, abs_of_nonneg hk]
    exact le_trans (mul_le_mul_of_nonneg_left hb.2.1 hk)
      (by nlinarith)

/-- The first coordinate is already strictly controlled after two interior steps. -/
theorem two_step_first_bound {a b : ℝ} (ha : 0 ≤ a) (_ha1 : a ≤ 1)
    (_hb : 0 ≤ b) (hb1 : b ≤ 1) (s : ℝ × ℝ) :
    |(delayedStep b (delayedStep a s)).1| ≤ max a (1-b) * envelope s := by
  have hs := envelope_bounds s
  have h0 := envelope_nonnegative s
  have heq : (delayedStep b (delayedStep a s)).1 = (1-b)*s.1-a*s.2 := by
    simp only [delayedStep]
    ring
  rw [heq]
  by_cases hab : a+b ≤ 1
  · have h := weighted_abs_bound (show 0 ≤ 1-a-b by linarith) ha hs.1 hs.2.2
    have hid : (1-b)*s.1-a*s.2 = (1-a-b)*s.1+a*(s.1-s.2) := by ring
    rw [hid]
    apply le_trans h
    have hm := mul_le_mul_of_nonneg_right (le_max_right a (1-b)) h0
    nlinarith
  · have h := weighted_abs_bound (show 0 ≤ 1-b by linarith)
      (show 0 ≤ a+b-1 by linarith) hs.2.2
      (show |-s.2| ≤ envelope s by simpa only [abs_neg] using hs.2.1)
    have hid : (1-b)*s.1-a*s.2 = (1-b)*(s.1-s.2)+(a+b-1)*(-s.2) := by ring
    rw [hid]
    apply le_trans h
    have hm := mul_le_mul_of_nonneg_right (le_max_left a (1-b)) h0
    nlinarith

/-- Three steps contract uniformly even when the gains differ at every step. -/
theorem three_step_contraction {δ a b c : ℝ} (hδ : 0 < δ) (_hδ2 : δ ≤ 1/2)
    (ha : δ ≤ a ∧ a ≤ 1-δ) (hb : δ ≤ b ∧ b ≤ 1-δ)
    (hc : δ ≤ c ∧ c ≤ 1-δ) (s : ℝ × ℝ) :
    envelope (delayedStep c (delayedStep b (delayedStep a s))) ≤
      (1-δ)*envelope s := by
  have ha0 : 0 ≤ a := by linarith
  have ha1 : a ≤ 1 := by linarith
  have hb0 : 0 ≤ b := by linarith
  have hb1 : b ≤ 1 := by linarith
  have hc0 : 0 ≤ c := by linarith
  have hc1 : c ≤ 1 := by linarith
  have hs := envelope_bounds s
  have h0 := envelope_nonnegative s
  have htwo := two_step_first_bound ha0 ha1 hb0 hb1 s
  have hmax : max a (1-b) ≤ 1-δ := max_le ha.2 (by linarith)
  have hfirst : |(delayedStep b (delayedStep a s)).1| ≤ (1-δ)*envelope s :=
    le_trans htwo (mul_le_mul_of_nonneg_right hmax h0)
  have hdiff : |(delayedStep b (delayedStep a s)).1 -
      (delayedStep b (delayedStep a s)).2| ≤ (1-δ)*envelope s := by
    have heq : (delayedStep b (delayedStep a s)).1 -
      (delayedStep b (delayedStep a s)).2 = -(b*s.1) := by
      simp only [delayedStep]
      ring
    rw [heq, abs_neg, abs_mul, abs_of_nonneg hb0]
    exact le_trans (mul_le_mul_of_nonneg_left hs.1 hb0)
      (mul_le_mul_of_nonneg_right hb.2 h0)
  apply (envelope_le_iff _ _).mpr
  refine ⟨?_, hfirst, ?_⟩
  · have h := convex_abs_bound hc0 hc1 hfirst hdiff
    convert h using 1; simp only [delayedStep]; congr 1; ring
  · have hone := step_nonincrease ha0 ha1 s
    have hxb := (envelope_bounds (delayedStep a s)).1
    have hx : |(delayedStep a s).1| ≤ envelope s := le_trans hxb hone
    have heq : (delayedStep c (delayedStep b (delayedStep a s))).1 -
      (delayedStep c (delayedStep b (delayedStep a s))).2 =
      -(c*(delayedStep a s).1) := by
      simp only [delayedStep]
      ring
    rw [heq, abs_neg, abs_mul, abs_of_nonneg hc0]
    exact le_trans (mul_le_mul_of_nonneg_left hx hc0)
      (mul_le_mul_of_nonneg_right hc.2 h0)

theorem trajectory_nonincrease (gain : ℕ → ℝ) (initial : ℝ × ℝ)
    (hg : ∀ n, 0 ≤ gain n ∧ gain n ≤ 1) (n : ℕ) :
    envelope (trajectory gain initial n) ≤ envelope initial := by
  induction n with
  | zero => simp [trajectory]
  | succ n ih =>
    exact le_trans (step_nonincrease (hg n).1 (hg n).2 _) ih

theorem trajectory_three_step (gain : ℕ → ℝ) (initial : ℝ × ℝ) {δ : ℝ}
    (hδ : 0 < δ) (hδ2 : δ ≤ 1/2) (hg : ∀ n, δ ≤ gain n ∧ gain n ≤ 1-δ)
    (n : ℕ) :
    envelope (trajectory gain initial (n+3)) ≤
      (1-δ)*envelope (trajectory gain initial n) := by
  exact three_step_contraction hδ hδ2 (hg n) (hg (n+1)) (hg (n+2)) _

/-- A bound at every time, including the one- and two-step remainders. -/
theorem trajectory_geometric_bound (gain : ℕ → ℝ) (initial : ℝ × ℝ) {δ : ℝ}
    (hδ : 0 < δ) (hδ2 : δ ≤ 1/2) (hg : ∀ n, δ ≤ gain n ∧ gain n ≤ 1-δ)
    (n : ℕ) :
    envelope (trajectory gain initial n) ≤ (1-δ)^(n/3)*envelope initial := by
  have hg01 : ∀ n, 0 ≤ gain n ∧ gain n ≤ 1 := by
    intro n
    have := hg n
    constructor <;> linarith
  have hr : 0 ≤ 1-δ := by linarith
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n < 3
    · simpa only [Nat.div_eq_of_lt hn, pow_zero, one_mul] using
        trajectory_nonincrease gain initial hg01 n
    · have hidx : n = (n-3)+3 := by omega
      have hm : n-3 < n := by omega
      have hb := ih (n-3) hm
      have ht := trajectory_three_step gain initial hδ hδ2 hg (n-3)
      rw [← hidx] at ht
      have hmul := mul_le_mul_of_nonneg_left hb hr
      have hdiv : n/3 = (n-3)/3+1 := by omega
      rw [hdiv, pow_succ]
      nlinarith

/-- A finite trajectory consults only the gains at its actual earlier indices. -/
theorem trajectory_eq_of_prefix_eq (gain other : ℕ → ℝ) (initial : ℝ × ℝ)
    (n : ℕ) (heq : ∀ i, i < n → gain i = other i) :
    trajectory gain initial n = trajectory other initial n := by
  revert heq
  induction n with
  | zero => intro _; rfl
  | succ n ih =>
    intro heq
    simp only [trajectory]
    rw [heq n (by omega), ih (fun i hi => heq i (by omega))]

/-- Only the gains actually used in this finite prefix need the interior bounds.
The auxiliary extension in the proof supplies no executed or funded future. -/
theorem trajectory_geometric_bound_prefix (gain : ℕ → ℝ) (initial : ℝ × ℝ)
    {δ : ℝ} (hδ : 0 < δ) (hδ2 : δ ≤ 1/2) (n : ℕ)
    (hg : ∀ i, i < n → δ ≤ gain i ∧ gain i ≤ 1-δ) :
    envelope (trajectory gain initial n) ≤ (1-δ)^(n/3)*envelope initial := by
  let extended : ℕ → ℝ := fun i => if i < n then gain i else δ
  have hfull : ∀ i, δ ≤ extended i ∧ extended i ≤ 1-δ := by
    intro i
    by_cases hi : i < n
    · simpa only [extended, if_pos hi] using hg i hi
    · simp only [extended, if_neg hi]
      exact ⟨le_rfl, by linarith⟩
  have heq : trajectory gain initial n = trajectory extended initial n :=
    trajectory_eq_of_prefix_eq gain extended initial n
      (fun i hi => by simp only [extended, if_pos hi])
  rw [heq]
  exact trajectory_geometric_bound extended initial hδ hδ2 hfull n

/-- The realized state converges; the gain schedule itself need not converge. -/
theorem trajectory_envelope_tends_zero (gain : ℕ → ℝ) (initial : ℝ × ℝ) {δ : ℝ}
    (hδ : 0 < δ) (hδ2 : δ ≤ 1/2) (hg : ∀ n, δ ≤ gain n ∧ gain n ≤ 1-δ) :
    Tendsto (fun n => envelope (trajectory gain initial n)) atTop (𝓝 0) := by
  have hpow := tendsto_pow_atTop_nhds_zero_of_lt_one
    (show 0 ≤ 1-δ by linarith) (show 1-δ < 1 by linarith)
  have hdiv : Tendsto (fun n : ℕ => n/3) atTop atTop := by
    apply tendsto_atTop_atTop.mpr
    intro b
    exact ⟨3*b, fun n hn => by omega⟩
  apply squeeze_zero (fun n => envelope_nonnegative _)
    (trajectory_geometric_bound gain initial hδ hδ2 hg)
  simpa only [zero_mul] using (hpow.comp hdiv).mul_const (envelope initial)

theorem squaredNorm_le_envelope (s : ℝ × ℝ) : squaredNorm s ≤ 2*(envelope s)^2 := by
  have hs := envelope_bounds s
  have he := envelope_nonnegative s
  have hx := mul_nonneg (sub_nonneg.mpr hs.1) (add_nonneg he (abs_nonneg s.1))
  have hy := mul_nonneg (sub_nonneg.mpr hs.2.1) (add_nonneg he (abs_nonneg s.2))
  unfold squaredNorm
  nlinarith [sq_abs s.1, sq_abs s.2]

theorem trajectory_squaredNorm_tends_zero (gain : ℕ → ℝ) (initial : ℝ × ℝ) {δ : ℝ}
    (hδ : 0 < δ) (hδ2 : δ ≤ 1/2) (hg : ∀ n, δ ≤ gain n ∧ gain n ≤ 1-δ) :
    Tendsto (fun n => squaredNorm (trajectory gain initial n)) atTop (𝓝 0) := by
  have he := trajectory_envelope_tends_zero gain initial hδ hδ2 hg
  apply squeeze_zero (fun n => RealFeedback.squaredNorm_nonnegative _)
    (fun n => squaredNorm_le_envelope _)
  simpa only [zero_pow (by decide : (2 : ℕ) ≠ 0), mul_zero] using
    (he.pow 2).const_mul 2

/-- Uniform Lyapunov stability in the common envelope, independent of gain changes. -/
theorem trajectory_envelope_stable :
    ∀ ε : ℝ, 0 < ε → ∃ η : ℝ, 0 < η ∧ ∀ gain : ℕ → ℝ,
      (∀ n, 0 ≤ gain n ∧ gain n ≤ 1) → ∀ initial : ℝ × ℝ,
      envelope initial < η → ∀ n, envelope (trajectory gain initial n) < ε := by
  intro ε hε
  refine ⟨ε, hε, ?_⟩
  intro gain hg initial hi n
  exact lt_of_le_of_lt (trajectory_nonincrease gain initial hg n) hi

end
end SystemsComplexity.VaryingFeedback

#print axioms SystemsComplexity.VaryingFeedback.envelope_nonnegative
#print axioms SystemsComplexity.VaryingFeedback.envelope_bounds
#print axioms SystemsComplexity.VaryingFeedback.envelope_le_iff
#print axioms SystemsComplexity.VaryingFeedback.weighted_abs_bound
#print axioms SystemsComplexity.VaryingFeedback.convex_abs_bound
#print axioms SystemsComplexity.VaryingFeedback.step_nonincrease
#print axioms SystemsComplexity.VaryingFeedback.two_step_first_bound
#print axioms SystemsComplexity.VaryingFeedback.three_step_contraction
#print axioms SystemsComplexity.VaryingFeedback.trajectory_nonincrease
#print axioms SystemsComplexity.VaryingFeedback.trajectory_three_step
#print axioms SystemsComplexity.VaryingFeedback.trajectory_geometric_bound
#print axioms SystemsComplexity.VaryingFeedback.trajectory_eq_of_prefix_eq
#print axioms SystemsComplexity.VaryingFeedback.trajectory_geometric_bound_prefix
#print axioms SystemsComplexity.VaryingFeedback.trajectory_envelope_tends_zero
#print axioms SystemsComplexity.VaryingFeedback.squaredNorm_le_envelope
#print axioms SystemsComplexity.VaryingFeedback.trajectory_squaredNorm_tends_zero
#print axioms SystemsComplexity.VaryingFeedback.trajectory_envelope_stable
