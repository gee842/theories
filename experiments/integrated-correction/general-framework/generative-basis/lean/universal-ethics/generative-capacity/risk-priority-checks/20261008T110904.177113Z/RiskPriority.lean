import Std

/-
The same asymmetric support family as BasicRiskSharing, represented with integer
numerators on a common positive denominator. Two loss positions differentiate
within one provision history. Independent permissions, equal loss gravity,
matched continuation effects, and the actual selection/hazard law are supplied.

No score below is adopted as an ethical value function. The two diagnostics
expose the extra commitment needed at exact equality. The final conditional
bound does not justify its own comparison coefficients or their local validity.
-/
namespace RiskPriority

structure Exposure where
  a : Int
  b : Int
  deriving DecidableEq

def mixture (n x : Int) : Exposure := ⟨8*n-7*x, n+3*x⟩
def equalized (k : Int) : Exposure := ⟨31*k, 31*k⟩
def departure (k d : Int) : Exposure := ⟨31*k-7*d, 31*k+3*d⟩
def total (p : Exposure) : Int := p.a+p.b
def quadratic (p : Exposure) : Int := p.a*p.a+p.b*p.b
def magnitude (x : Int) : Int := if 0 ≤ x then x else -x
def corner (p : Exposure) : Int := 2*(p.a+p.b)+magnitude (p.a-p.b)

theorem same_support_family (k d : Int) :
    mixture (10*k) (7*k+d) = departure k d := by
  unfold mixture departure
  congr 1 <;> omega

theorem feasible_departure (k d : Int) (hk : 0 < k)
    (hd : 0 ≤ d) (hb : d ≤ 3*k) :
    0 < 100*k ∧ 0 ≤ 7*k+d ∧ 7*k+d ≤ 10*k ∧
    0 ≤ (departure k d).a ∧ 0 ≤ (departure k d).b ∧
    total (departure k d) ≤ 100*k := by
  unfold departure total
  dsimp only
  omega

theorem exposure_exchange (k d : Int) :
    (departure k d).a+7*d = (equalized k).a ∧
    (departure k d).b = (equalized k).b+3*d ∧
    total (departure k d)+4*d = total (equalized k) := by
  unfold departure equalized total
  dsimp only
  omega

theorem quadratic_departure_identity (k d : Int) :
    quadratic (departure k d)+248*k*d =
      quadratic (equalized k)+58*d*d := by
  unfold quadratic departure equalized
  dsimp only
  grind

theorem quadratic_prefers_small_departure (k d : Int)
    (hd : 0 < d) (hsmall : 58*d < 248*k) :
    quadratic (departure k d) < quadratic (equalized k) := by
  have hid := quadratic_departure_identity k d
  have hm := Int.mul_lt_mul_of_pos_right hsmall hd
  omega

/-- A positive-cost partial transfer can win under one diagnostic, while the
exact equalization and the least-total-loss endpoint both lose to it. -/
theorem partial_sharing_control :
    departure 1 2 = mixture 10 9 ∧
    quadratic (departure 1 2) = 1658 ∧
    quadratic (mixture 10 10) = 1700 ∧
    quadratic (equalized 1) = 1922 ∧
    total (departure 1 2) = 54 ∧ total (mixture 10 10) = 50 ∧
    total (equalized 1) = 62 := by decide

theorem corner_departure_identity (k d : Int) (hd : 0 ≤ d) :
    corner (departure k d) = 124*k+2*d := by
  unfold corner departure magnitude
  dsimp only
  split <;> omega

/-- The corner diagnostic favors equality at every positive feasible departure,
including arbitrarily fine finite grids; mere finite sensitivity is insufficient. -/
theorem corner_prefers_equality (k d : Int) (hd : 0 < d) :
    corner (equalized k) < corner (departure k d) := by
  have h := corner_departure_identity k d (Int.le_of_lt hd)
  have hz : corner (equalized k) = 124*k := by
    unfold corner equalized magnitude
    dsimp only
    split <;> omega
  omega

/-- Both diagnostics treat position labels symmetrically. This is not a theorem
that actual histories, roles, permissions or loss gravity are interchangeable. -/
theorem diagnostic_symmetry (a b : Int) :
    quadratic ⟨a,b⟩ = quadratic ⟨b,a⟩ ∧
    corner ⟨a,b⟩ = corner ⟨b,a⟩ := by
  constructor
  · dsimp only [quadratic]
    omega
  · dsimp only [corner, magnitude]
    split <;> split <;> omega

theorem corner_linear_change_bound (a b c d : Int) :
    magnitude (corner ⟨a,b⟩ - corner ⟨c,d⟩) ≤
      3*(magnitude (a-c)+magnitude (b-d)) := by
  unfold corner magnitude
  dsimp only
  split <;> split <;> split <;> split <;> split <;> omega

/-- A local certificate for a particular appraisal: removing 7 units has a
lower bound on its force, adding 3 has an upper bound, and 7*lower > 3*upper.
This is a sufficient comparison interface, not a derived normative scale. -/
theorem bounded_exchange_certificate
    (before middle after lower upper d : Int)
    (hd : 0 < d)
    (remove : middle+7*lower*d ≤ before)
    (add : after ≤ middle+3*upper*d)
    (bound : 3*upper < 7*lower) : after < before := by
  have hm := Int.mul_lt_mul_of_pos_right bound hd
  omega

end RiskPriority
