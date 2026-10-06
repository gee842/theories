import Std

/-!
# Exact feedback dynamics over rational states

The plant is x(t+1) = x(t) + u(t), with exact stationary linear dynamics,
no saturation, no disturbances, and no resource constraint. Delay changes the
complete state from x to (current x, previous x). These are mathematical models,
not an identified model of the finite concern learner.

The main contrast uses the SAME gain 6/5. Immediate feedback converges for every
rational initial state (an actual epsilon/eventually statement). Delayed feedback
escapes every bound in full-state squared distance for every nonzero rational
initial state. An exact quadratic energy identity supplies the proof; a finite
list of computed points or a renamed eigenvalue condition is not the conclusion.
-/

namespace SystemsComplexity.Feedback

def immediate (k x : Rat) : Nat → Rat
  | 0 => x
  | n + 1 => (1 - k) * immediate k x n

def delayedStep (k : Rat) (s : Rat × Rat) : Rat × Rat :=
  (s.1 - k * s.2, s.1)

def delayed (k : Rat) (s : Rat × Rat) : Nat → Rat × Rat
  | 0 => s
  | n + 1 => delayedStep k (delayed k s n)

def delayedEnergy (k : Rat) (s : Rat × Rat) : Rat :=
  s.1 * s.1 - s.1 * s.2 + k * s.2 * s.2

def normSq (s : Rat × Rat) : Rat := s.1 * s.1 + s.2 * s.2

def gain : Rat := 6 / 5

/-- Elementary ordered-field fact, with no analytic library. -/
theorem square_nonneg (x : Rat) : 0 ≤ x * x := by
  by_cases h : 0 ≤ x
  · exact Rat.mul_nonneg h h
  · have hh : 0 ≤ -x := by grind
    have hhh := Rat.mul_nonneg hh hh
    grind

/-- Rational Archimedean property derived from the actual floor operation. -/
theorem exists_nat_gt (a : Rat) : ∃ n : Nat, a < (n : Rat) := by
  refine ⟨(a.floor + 1).toNat, ?_⟩
  have h := Rat.lt_floor_add_one a
  have hi := Int.self_le_toNat (a.floor + 1)
  have hr := Rat.intCast_le_intCast.mpr hi
  have hr2 : ((a.floor + 1 : Int) : Rat) ≤ ((a.floor + 1).toNat : Rat) := by
    simpa only [Rat.intCast_natCast] using hr
  grind

theorem immediate_formula (k x : Rat) (n : Nat) :
    immediate k x n = (1-k)^n * x := by
  induction n with
  | zero => simp [immediate, Rat.pow_zero, Rat.one_mul]
  | succ n ih => simp only [immediate, ih, Rat.pow_succ]; grind

/-- Exact transport for every rational gain; positivity needs further conditions. -/
theorem delayed_energy_step (k : Rat) (s : Rat × Rat) :
    delayedEnergy k (delayedStep k s) = k * delayedEnergy k s := by
  simp only [delayedEnergy, delayedStep]
  grind

theorem delayed_energy_formula (k : Rat) (s : Rat × Rat) (n : Nat) :
    delayedEnergy k (delayed k s n) = k^n * delayedEnergy k s := by
  induction n with
  | zero => simp [delayed, Rat.pow_zero, Rat.one_mul]
  | succ n ih =>
    simp only [delayed, delayed_energy_step, ih, Rat.pow_succ]
    grind

/-- Full-state coercivity; it is not a bound on each scalar sample separately. -/
theorem energy_lower (s : Rat × Rat) :
    normSq s / 2 ≤ delayedEnergy gain s := by
  have h := square_nonneg (s.1-s.2)
  have hy := square_nonneg s.2
  unfold normSq delayedEnergy gain
  grind

theorem energy_upper (s : Rat × Rat) :
    delayedEnergy gain s ≤ 2 * normSq s := by
  have h := square_nonneg (s.1+s.2)
  have hx := square_nonneg s.1
  have hy := square_nonneg s.2
  unfold normSq delayedEnergy gain
  grind

theorem normSq_nonneg (s : Rat × Rat) : 0 ≤ normSq s := by
  have hx := square_nonneg s.1
  have hy := square_nonneg s.2
  unfold normSq
  grind

theorem normSq_positive (s : Rat × Rat) (hs : s ≠ (0,0)) : 0 < normSq s := by
  have hx := square_nonneg s.1
  have hy := square_nonneg s.2
  apply Classical.byContradiction
  intro h
  have hx0 : s.1*s.1 = 0 := by unfold normSq at h; grind
  have hy0 : s.2*s.2 = 0 := by unfold normSq at h; grind
  have hx1 : s.1 = 0 := (Rat.mul_eq_zero.mp hx0).elim id id
  have hy1 : s.2 = 0 := (Rat.mul_eq_zero.mp hy0).elim id id
  exact hs (Prod.ext hx1 hy1)

theorem energy_nonneg (s : Rat × Rat) : 0 ≤ delayedEnergy gain s := by
  have h := energy_lower s
  have hn := normSq_nonneg s
  grind

theorem energy_positive (s : Rat × Rat) (hs : s ≠ (0,0)) :
    0 < delayedEnergy gain s := by
  have h := energy_lower s
  have hn := normSq_positive s hs
  grind

/-- At gain 6/5, squared immediate deviation shrinks by the exact factor 1/25. -/
theorem immediate_square_step (x : Rat) (n : Nat) :
    immediate gain x (n+1) * immediate gain x (n+1) =
      (immediate gain x n * immediate gain x n) / 25 := by
  simp only [immediate]
  unfold gain
  grind

/-- An arbitrary-time reciprocal bound, adequate for epsilon convergence. -/
theorem immediate_bound (x : Rat) (n : Nat) :
    ((n : Rat)+1) * (immediate gain x n * immediate gain x n) ≤ x*x := by
  induction n with
  | zero => simp only [immediate]; grind
  | succ n ih =>
    have hn := Rat.natCast_nonneg (a := n)
    have he := square_nonneg (immediate gain x n)
    have hp := Rat.mul_nonneg (show 0 ≤ 24*(n : Rat)+23 by grind) he
    have hs := immediate_square_step x n
    rw [hs]
    simp only [Rat.natCast_add]
    grind

/-- Convergence of squared deviation: every positive tolerance eventually holds forever. -/
theorem immediate_square_tends_zero (x ε : Rat) (hε : 0 < ε) :
    ∃ N : Nat, ∀ n : Nat, N ≤ n →
      immediate gain x n * immediate gain x n < ε := by
  obtain ⟨N, hN⟩ := exists_nat_gt (x*x/ε)
  refine ⟨N, ?_⟩
  intro n hn
  have hratio : x*x < (N : Rat)*ε := (Rat.div_lt_iff hε).mp hN
  have hcast : (N : Rat) ≤ (n : Rat) := Rat.natCast_le_natCast.mpr hn
  have hmul := Rat.mul_le_mul_of_nonneg_right hcast (show 0 ≤ ε by grind)
  have hb := immediate_bound x n
  have hcoef : 0 ≤ (n : Rat)+1 := by have := Rat.natCast_nonneg (a := n); grind
  apply Classical.byContradiction
  intro h
  have hεx : ε ≤ immediate gain x n * immediate gain x n := by grind
  have hmul2 := Rat.mul_le_mul_of_nonneg_left hεx hcoef
  grind

/-- Ordinary two-sided epsilon convergence, derived from the squared bound. -/
theorem immediate_tends_zero (x ε : Rat) (hε : 0 < ε) :
    ∃ N : Nat, ∀ n : Nat, N ≤ n →
      -ε < immediate gain x n ∧ immediate gain x n < ε := by
  have hε2 : 0 < ε*ε := Rat.mul_pos hε hε
  obtain ⟨N,hN⟩ := immediate_square_tends_zero x (ε*ε) hε2
  refine ⟨N, ?_⟩
  intro n hn
  have hsq := hN n hn
  constructor
  · apply Classical.byContradiction
    intro h
    have h1 : 0 ≤ -immediate gain x n - ε := by grind
    have h2 : 0 ≤ -immediate gain x n + ε := by grind
    have hp := Rat.mul_nonneg h1 h2
    grind
  · apply Classical.byContradiction
    intro h
    have h1 : 0 ≤ immediate gain x n - ε := by grind
    have h2 : 0 ≤ immediate gain x n + ε := by grind
    have hp := Rat.mul_nonneg h1 h2
    grind

/-- Bernoulli-type lower bound for the growing delayed energy, for every time. -/
theorem delayed_energy_growth (s : Rat × Rat) (n : Nat) :
    (1+(n : Rat)/5) * delayedEnergy gain s ≤
      delayedEnergy gain (delayed gain s n) := by
  induction n with
  | zero => simp only [delayed]; grind
  | succ n ih =>
    have he := energy_nonneg s
    have hn := Rat.natCast_nonneg (a := n)
    have hp := Rat.mul_nonneg hn he
    have hi := Rat.mul_le_mul_of_nonneg_left ih (show 0 ≤ gain by unfold gain; grind)
    simp only [delayed, delayed_energy_step, Rat.natCast_add]
    unfold gain at *
    grind

/-- Every nonzero delayed state eventually escapes every bound, permanently. -/
theorem delayed_normSq_tends_infinity (s : Rat × Rat) (hs : s ≠ (0,0)) (B : Rat) :
    ∃ N : Nat, ∀ n : Nat, N ≤ n → B < normSq (delayed gain s n) := by
  have he := energy_positive s hs
  obtain ⟨N,hN⟩ := exists_nat_gt (10*B/delayedEnergy gain s)
  refine ⟨N, ?_⟩
  intro n hn
  have hratio : 10*B < (N : Rat)*delayedEnergy gain s := (Rat.div_lt_iff he).mp hN
  have hcast : (N : Rat) ≤ (n : Rat) := Rat.natCast_le_natCast.mpr hn
  have hmul := Rat.mul_le_mul_of_nonneg_right hcast (show 0 ≤ delayedEnergy gain s by grind)
  have hg := delayed_energy_growth s n
  have hu := energy_upper (delayed gain s n)
  grind

theorem delayed_add (k : Rat) (s : Rat × Rat) (n m : Nat) :
    delayed k s (n+m) = delayed k (delayed k s n) m := by
  induction m with
  | zero => rfl
  | succ m ih =>
    change delayedStep k (delayed k s (n+m)) = delayedStep k (delayed k (delayed k s n) m)
    rw [ih]

/-- The boundary gain 1 is periodic, so oscillation alone is not chaos. -/
theorem delayed_one_six (s : Rat × Rat) : delayed 1 s 6 = s := by
  cases s with
  | mk x y =>
    simp only [delayed, delayedStep]
    apply Prod.ext <;> simp only <;> grind

theorem delayed_one_periodic (s : Rat × Rat) (n : Nat) :
    delayed 1 s (n+6) = delayed 1 s n := by
  rw [delayed_add, delayed_one_six]

end SystemsComplexity.Feedback

#print axioms SystemsComplexity.Feedback.square_nonneg
#print axioms SystemsComplexity.Feedback.exists_nat_gt
#print axioms SystemsComplexity.Feedback.immediate_formula
#print axioms SystemsComplexity.Feedback.delayed_energy_step
#print axioms SystemsComplexity.Feedback.delayed_energy_formula
#print axioms SystemsComplexity.Feedback.energy_lower
#print axioms SystemsComplexity.Feedback.energy_upper
#print axioms SystemsComplexity.Feedback.normSq_nonneg
#print axioms SystemsComplexity.Feedback.normSq_positive
#print axioms SystemsComplexity.Feedback.energy_nonneg
#print axioms SystemsComplexity.Feedback.energy_positive
#print axioms SystemsComplexity.Feedback.immediate_square_step
#print axioms SystemsComplexity.Feedback.immediate_bound
#print axioms SystemsComplexity.Feedback.immediate_square_tends_zero
#print axioms SystemsComplexity.Feedback.immediate_tends_zero
#print axioms SystemsComplexity.Feedback.delayed_energy_growth
#print axioms SystemsComplexity.Feedback.delayed_normSq_tends_infinity
#print axioms SystemsComplexity.Feedback.delayed_add
#print axioms SystemsComplexity.Feedback.delayed_one_six
#print axioms SystemsComplexity.Feedback.delayed_one_periodic
