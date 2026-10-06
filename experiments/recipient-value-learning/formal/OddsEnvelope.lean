import Std

/-!
# Rational-odds certificate for the paired response-gate envelope

The rational odds multiplier is a supplied bound. This module proves the exact
quadratic equivalence and a sufficient discriminant certificate, not properties
of real exponentials, logarithms or square roots. The separate analysis provides
that interpretation. A marginal response-rate difference does not supply the
pointwise gate premise below.
-/

namespace OddsEnvelope

def probability (t : Rat) : Rat := t / (1+t)

def quadratic (k rho B t : Rat) : Rat :=
  k*(B-rho)*t*t + ((k+1)*B-(k-1+rho))*t+B

theorem probability_account {t : Rat} (ht : 0 ≤ t) :
    probability t * (1+t) = t := by
  exact Rat.div_mul_cancel (by grind)

theorem probability_bounds {t : Rat} (ht : 0 ≤ t) :
    0 ≤ probability t ∧ probability t ≤ 1 := by
  have account := probability_account ht
  have positive : 0 < 1+t := by grind
  constructor
  · exact Rat.le_of_mul_le_mul_right (by grind) positive
  · exact Rat.le_of_mul_le_mul_right (by grind) positive

theorem probability_monotone {s t : Rat} (hs : 0 ≤ s) (hst : s ≤ t) :
    probability s ≤ probability t := by
  have ht : 0 ≤ t := by grind
  have a := probability_account hs
  have b := probability_account ht
  have denominator : 0 < (1+s)*(1+t) := Rat.mul_pos (by grind) (by grind)
  apply Rat.le_of_mul_le_mul_right (c := (1+s)*(1+t)) _ denominator
  have left : probability s*((1+s)*(1+t)) = s*(1+t) := by
    rw [← Rat.mul_assoc, a]
  have right : probability t*((1+s)*(1+t)) = t*(1+s) := by
    rw [Rat.mul_comm (1+s) (1+t), ← Rat.mul_assoc, b]
  rw [left, right]
  grind

/-- The polynomial is the exact numerator after multiplying positive denominators. -/
theorem quadratic_iff {k rho B t : Rat} (hk : 1 ≤ k) (ht : 0 ≤ t) :
    probability (k*t) - (1-rho)*probability t ≤ B ↔
      0 ≤ quadratic k rho B t := by
  have hkt := Rat.mul_nonneg (show 0 ≤ k by grind) ht
  have a := probability_account hkt
  have b := probability_account ht
  have denominator : 0 < (1+k*t)*(1+t) := Rat.mul_pos (by grind) (by grind)
  have identity : (B-(probability (k*t)-(1-rho)*probability t))*((1+k*t)*(1+t)) =
      quadratic k rho B t := by unfold quadratic; grind
  constructor
  · intro bound
    have h := Rat.mul_nonneg (show 0 ≤ B-(probability (k*t)-(1-rho)*probability t) by grind)
      (show 0 ≤ (1+k*t)*(1+t) by grind)
    simpa only [identity] using h
  · intro nonnegative
    have h : 0 ≤ B-(probability (k*t)-(1-rho)*probability t) := by
      apply Rat.le_of_mul_le_mul_right (c := (1+k*t)*(1+t)) _ denominator
      grind
    grind

theorem square_nonnegative (x : Rat) : 0 ≤ x*x := by
  by_cases sign : 0 ≤ x
  · exact Rat.mul_nonneg sign sign
  · have h : 0 ≤ -x := by grind
    have square := Rat.mul_nonneg h h
    grind

/-- A nonnegative leading coefficient and discriminant certificate suffice
on the half-line; a nonnegative linear coefficient also suffices there. -/
theorem nonnegative_quadratic {A M B t : Rat}
    (hA : 0 ≤ A) (hB : 0 ≤ B) (ht : 0 ≤ t)
    (certificate : 0 ≤ M ∨ M*M ≤ 4*A*B) :
    0 ≤ A*t*t+M*t+B := by
  rcases certificate with positive | discriminant
  · have aa := Rat.mul_nonneg (Rat.mul_nonneg hA ht) ht
    have mm := Rat.mul_nonneg positive ht
    grind
  · by_cases zero : A = 0
    · subst A
      simp only [Rat.mul_zero, Rat.zero_mul] at discriminant
      have sq := square_nonnegative M
      have eq : M*M = 0 := Rat.le_antisymm discriminant sq
      have mz : M = 0 := by
        rcases Rat.mul_eq_zero.mp eq with h | h <;> exact h
      simpa only [mz, Rat.zero_mul, Rat.zero_add] using hB
    · have pa : 0 < 4*A := by grind
      have sq := square_nonnegative (2*A*t+M)
      have gap : 0 ≤ 4*A*B-M*M := by grind
      have identity : 4*A*(A*t*t+M*t+B) = (2*A*t+M)*(2*A*t+M)+(4*A*B-M*M) := by grind
      apply Rat.le_of_mul_le_mul_left (c := 4*A) _ pa
      grind

/-- A finite rational certificate, without requiring rational square roots. -/
theorem certified_envelope {k rho B t : Rat}
    (hk : 1 ≤ k) (hr : 0 ≤ rho) (hB : rho ≤ B) (ht : 0 ≤ t)
    (certificate :
      0 ≤ (k+1)*B-(k-1+rho) ∨
      ((k+1)*B-(k-1+rho))*((k+1)*B-(k-1+rho)) ≤ 4*k*(B-rho)*B) :
    probability (k*t)-(1-rho)*probability t ≤ B := by
  apply (quadratic_iff hk ht).mpr
  unfold quadratic
  apply nonnegative_quadratic
  · exact Rat.mul_nonneg (by grind) (by grind)
  · grind
  · exact ht
  · grind

/-- Both gates are physically paired; their mean difference is not enough. -/
theorem paired_gates_bounded {r0 r1 t0 t1 k rho B : Rat}
    (_hr0 : 0 ≤ r0) (_hr01 : r0 ≤ 1) (hr1 : 0 ≤ r1) (hr11 : r1 ≤ 1)
    (ht0 : 0 ≤ t0) (ht1 : 0 ≤ t1) (hk : 1 ≤ k)
    (oddsBound : t1 ≤ k*t0) (gateBound : r1-r0 ≤ rho)
    (envelope : probability (k*t0)-(1-rho)*probability t0 ≤ B) :
    r1*probability t1-r0*probability t0 ≤ B := by
  have hkt := Rat.mul_nonneg (show 0 ≤ k by grind) ht0
  have monotone := probability_monotone ht1 oddsBound
  have order : t0 ≤ k*t0 := by
    have h := Rat.mul_le_mul_of_nonneg_right hk ht0
    grind
  have baseline := probability_monotone ht0 order
  have p0 := (probability_bounds ht0).1
  have first := Rat.mul_le_mul_of_nonneg_left monotone hr1
  have gates := Rat.mul_le_mul_of_nonneg_right gateBound p0
  have remaining := Rat.mul_le_mul_of_nonneg_right hr11
    (show 0 ≤ probability (k*t0)-probability t0 by grind)
  grind

/-- Exact rational attainment of the zero-gate-gap logistic modulus at k=4. -/
theorem fourfold_odds_modulus (t : Rat) (ht : 0 ≤ t) :
    probability (4*t)-probability t ≤ 1/3 := by
  have h := certified_envelope (k := 4) (rho := 0) (B := 1/3)
    (by grind) (by grind) (by grind) ht (by right; grind)
  grind

theorem fourfold_odds_attainment :
    probability (4*(1/2))-probability (1/2) = 1/3 := by
  unfold probability
  grind

/-- A nonzero paired-gate example reaches the interior quadratic envelope. -/
theorem gated_rational_attainment :
    probability (4*2)-(1-(5/9))*probability 2 = 16/27 ∧
      ∀ t : Rat, 0 ≤ t → probability (4*t)-(1-(5/9))*probability t ≤ 16/27 := by
  constructor
  · unfold probability; grind
  · intro t ht
    exact certified_envelope (k := 4) (rho := 5/9) (B := 16/27)
      (by grind) (by grind) (by grind) ht (by right; grind)

end OddsEnvelope

#print axioms OddsEnvelope.probability_account
#print axioms OddsEnvelope.probability_bounds
#print axioms OddsEnvelope.probability_monotone
#print axioms OddsEnvelope.quadratic_iff
#print axioms OddsEnvelope.square_nonnegative
#print axioms OddsEnvelope.nonnegative_quadratic
#print axioms OddsEnvelope.certified_envelope
#print axioms OddsEnvelope.paired_gates_bounded
#print axioms OddsEnvelope.fourfold_odds_modulus
#print axioms OddsEnvelope.fourfold_odds_attainment
#print axioms OddsEnvelope.gated_rational_attainment
