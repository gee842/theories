import Std

/- Exact algebraic corrections to historical universal claims. These results
do not formalize continuous-time ODE existence or spectral convergence. -/
namespace LegacyReconciliation

abbrev Pair := Rat × Rat
def mean (x : Pair) : Rat := (x.1+x.2)/2
def moment (x y : Pair) : Rat := (x.1*y.1+x.2*y.2)/2
def cov (x y : Pair) : Rat := moment x y - mean x * mean y

theorem raw_moment_decomposition (x y : Pair) :
    moment x y = cov x y + mean x * mean y := by
  unfold cov
  grind

theorem constant_proxy_has_no_covariance :
    moment (1,1) (2,2) = 2 ∧ cov (1,1) (2,2) = 0 := by decide +kernel

def linear (a b c d : Rat) (x : Pair) : Pair :=
  (a*x.1+b*x.2,c*x.1+d*x.2)

theorem same_positive_cross_product :
    (1/4:Rat)*(1/4) > 0 ∧ (1/4:Rat)*(1/4) = (1/4:Rat)*(1/4) := by decide +kernel

theorem contracting_diagonal (r : Rat) :
    linear (1/4) (1/4) (1/4) (1/4) (r,r) = (r/2,r/2) := by
  simp only [linear, Prod.mk.injEq]
  constructor <;> grind

theorem expanding_diagonal (r : Rat) :
    linear (7/4) (1/4) (1/4) (7/4) (r,r) = (2*r,2*r) := by
  simp only [linear, Prod.mk.injEq]
  constructor <;> grind

theorem negative_links_positive_product :
    (-1:Rat)*(-1) > 0 ∧ ¬ (0 < (-1:Rat)) := by decide +kernel

def rankOneCov (x : Pair) : Pair := linear 1 (-2) (-2) 4 x
def dot (x y : Pair) : Rat := x.1*y.1+x.2*y.2

theorem gram_square (x : Pair) :
    dot x (rankOneCov x) = (x.1-2*x.2)*(x.1-2*x.2) := by
  unfold dot rankOneCov linear
  grind

theorem covariance_from_two_centered_observations :
    cov (1,-1) (1,-1) = 1 ∧ cov (1,-1) (-2,2) = -2 ∧
    cov (-2,2) (-2,2) = 4 := by decide +kernel

theorem covariance_does_not_preserve_positive_weights :
    let w : Pair := (1,1)
    let v := rankOneCov w
    0 < w.1 ∧ 0 < w.2 ∧ w.1+2*v.1 < 0 := by decide +kernel

def dominantDiagonal : Pair → Pair := linear 3 0 0 2
def iterate (f : Pair → Pair) (x : Pair) : Nat → Pair
  | 0 => x
  | n+1 => f (iterate f x n)

theorem missing_dominant_component_stays_absent (n : Nat) :
    (iterate dominantDiagonal (0,1) n).1 = 0 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change 3 * (iterate dominantDiagonal (0,1) n).1 + 0 * (iterate dominantDiagonal (0,1) n).2 = 0
    rw [ih]
    grind

def first : Pair → Pair := linear 2 0 0 1
def second : Pair → Pair := linear 2 1 1 2
theorem changing_covariance_order_matters :
    second (first (1,0)) ≠ first (second (1,0)) := by decide +kernel

theorem uniform_weight_rate_has_scale :
    linear 3 1 1 2 (1/2,1/2) = (2,3/2) ∧
    linear 3 1 1 2 (1/2,1/2) ≠ (4,3) := by decide +kernel

/-- Exact embedding of a chosen rule update into joint dynamics, no attraction claim. -/
def joint {X W : Type} (f : X → W → X) (g : X → W → W) (s : X × W) :=
  (f s.1 s.2,g s.1 s.2)
theorem joint_rule_coordinate {X W : Type} (f : X → W → X)
    (g : X → W → W) (x : X) (w : W) :
    (joint f g (x,w)).2 = g x w := rfl

/-- A shared label need not admit an autonomous next-label law. -/
theorem no_closed_label_update
    {S Q : Type} (f : S → S) (q : S → Q) (a b : S)
    (same : q a = q b) (different : q (f a) ≠ q (f b)) :
    ¬ ∃ g : Q → Q, ∀ s, q (f s) = g (q s) := by
  rintro ⟨g,h⟩
  apply different
  rw [h a,h b,same]

end LegacyReconciliation
