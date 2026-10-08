import CorrectionBoundary

/- Several observations are roles within one joint continuation. No independence
is inferred from the number of observers. The probability experiment below
explicitly supplies a product distribution and then a common-mode alternative. -/
namespace CorrectionPopulation

structure World where
  left : Bool
  right : Bool
  deriving DecidableEq, Repr

def polarity (w : World) : Bool := xor w.left w.right

def result (w : World) (command : Bool) : Bool := xor command (polarity w)

theorem joint_observation_corrects (w : World) (requested : Bool) :
    result w (xor requested (xor w.left w.right)) = requested := by
  cases w with | mk a b => cases a <;> cases b <;> cases requested <;> rfl

theorem left_alone_insufficient (requested : Bool) :
    ¬ ∃ policy : Bool → Bool, ∀ w, result w (policy w.left) = requested := by
  rintro ⟨policy,h⟩
  have a := h ⟨false,false⟩
  have b := h ⟨false,true⟩
  exact CorrectionBoundary.opposite_decoders_conflict (policy false) requested ⟨a,b⟩

theorem right_alone_insufficient (requested : Bool) :
    ¬ ∃ policy : Bool → Bool, ∀ w, result w (policy w.right) = requested := by
  rintro ⟨policy,h⟩
  have a := h ⟨false,false⟩
  have b := h ⟨true,false⟩
  exact CorrectionBoundary.opposite_decoders_conflict (policy false) requested ⟨a,b⟩

def repeatedLeft (n : Nat) (w : World) : Fin n → Bool := fun _ => w.left

theorem arbitrarily_many_duplicate_observations_fail (n : Nat) (requested : Bool) :
    ¬ ∃ policy : (Fin n → Bool) → Bool, ∀ w, result w (policy (repeatedLeft n w)) = requested := by
  rintro ⟨policy,h⟩
  have a := h ⟨false,false⟩
  have b := h ⟨false,true⟩
  exact CorrectionBoundary.opposite_decoders_conflict
    (policy (fun _ => false)) requested ⟨a,b⟩

-- A pilot and target share a decoder parameter under the stated transfer law.
def probe (pilotPolarity : Bool) : Bool := xor false pilotPolarity

theorem pilot_transfers (pilotPolarity targetPolarity requested : Bool)
    (transfer : pilotPolarity = targetPolarity) :
    xor (xor requested (probe pilotPolarity)) targetPolarity = requested := by
  subst targetPolarity
  cases pilotPolarity <;> cases requested <;> rfl

theorem target_drift_defeats_pilot : xor (xor true (probe false)) true = false := rfl

-- Three actual error bits: product weights explicitly encode independent,
-- identically distributed Bernoulli errors. Naming three devices does not.
def majority (a b c : Bool) : Bool := (a && b) || (a && c) || (b && c)

def mass (p : ℝ) (error : Bool) : ℝ := if error then p else 1-p

def independentError (p : ℝ) : ℝ :=
  ∑ a : Bool, ∑ b : Bool, ∑ c : Bool,
    if majority a b c then mass p a * mass p b * mass p c else 0

theorem independent_error_formula (p : ℝ) : independentError p = 3*p^2 - 2*p^3 := by
  simp [independentError, majority, mass, Fintype.sum_bool]
  ring

theorem independent_gain (p : ℝ) (positive : 0 < p) (better : p < 1/2) :
    independentError p < p := by
  rw [independent_error_formula]
  have h := mul_pos (mul_pos positive (show 0 < 1-p by linarith))
    (show 0 < 1-2*p by linarith)
  nlinarith

theorem independent_error_nonnegative (p : ℝ) (low : 0 ≤ p) (high : p ≤ 1) :
    0 ≤ independentError p := by
  rw [independent_error_formula]
  have h := mul_nonneg (sq_nonneg p) (show 0 ≤ 3-2*p by linarith)
  nlinarith

def sharedError (p : ℝ) : ℝ :=
  ∑ error : Bool, if majority error error error then mass p error else 0

theorem shared_error_no_gain (p : ℝ) : sharedError p = p := by
  simp [sharedError, majority, mass, Fintype.sum_bool]

-- A common shock causes all readings to be wrong; absent that shock the three
-- errors follow the independent experiment. This mixture is a model premise.
def mixtureError (common p : ℝ) : ℝ := common + (1-common)*independentError p

theorem common_mode_floor (common p : ℝ) (hc : common ≤ 1) (lo : 0 ≤ p) (hi : p ≤ 1) :
    common ≤ mixtureError common p := by
  have h := mul_nonneg (show 0 ≤ 1-common by linarith)
    (independent_error_nonnegative p lo hi)
  unfold mixtureError
  linarith

theorem common_mode_floor_any_count (common : ℝ) (hc : common ≤ 1)
    (residual : Nat → ℝ) (nonnegative : ∀ n, 0 ≤ residual n) (n : Nat) :
    common ≤ common + (1-common)*residual n := by
  have h := mul_nonneg (show 0 ≤ 1-common by linarith) (nonnegative n)
  linarith

theorem independent_tenth_example : independentError (1/10) = 7/250 := by
  rw [independent_error_formula]; norm_num

theorem shared_tenth_example : sharedError (1/10) = 1/10 := by
  rw [shared_error_no_gain]

theorem common_tenth_example : mixtureError (1/10) (1/10) = 313/2500 := by
  rw [mixtureError, independent_tenth_example]; norm_num

-- A pilot test can alter one site while preserving another. This is a stated
-- operation on a joint installation, not an assumption of separate worlds.
structure Sites where
  pilotLive : Bool
  mainLive : Bool
  sharedPower : Bool
  deriving DecidableEq, Repr

def containedTest (s : Sites) : Sites := { s with pilotLive := false }

def uncontainedTest (s : Sites) : Sites := { s with sharedPower := false }

def mainAvailable (s : Sites) : Bool := s.mainLive && s.sharedPower

theorem contained_test_preserves_main (s : Sites) :
    mainAvailable (containedTest s) = mainAvailable s := rfl

theorem shared_support_failure_reaches_main (s : Sites) :
    mainAvailable (uncontainedTest s) = false := by simp [mainAvailable,uncontainedTest]

end CorrectionPopulation
