import BasicRiskSharing

/-
The existing asymmetric risk law, now retaining intermediate mixtures and
the scope of an added-loss allowance. All numerators share denominator 100*k
when k>0. These are two diagnostics in a fixed finite probability law, not
ethical utility, a universal ordering or repeated-trial risk probabilities.
-/
namespace BoundedRiskRevision

open BasicRiskSharing

def total (k x : Nat) : Nat := asymmetricA (10 * k) x + asymmetricB (10 * k) x
def greatest (k x : Nat) : Nat := max (asymmetricA (10 * k) x) (asymmetricB (10 * k) x)

def Dominates (k y x : Nat) : Prop :=
  total k y ≤ total k x ∧ greatest k y ≤ greatest k x ∧
    (total k y < total k x ∨ greatest k y < greatest k x)

def Efficient (k x : Nat) : Prop :=
  x ≤ 10 * k ∧ ¬ ∃ y, y ≤ 10 * k ∧ Dominates k y x

theorem greatest_on_frontier (k x : Nat) (hl : 7 * k ≤ x) (hu : x ≤ 10 * k) :
    greatest k x = asymmetricB (10 * k) x := by
  unfold greatest
  apply Nat.max_eq_right
  unfold asymmetricA asymmetricB
  omega

theorem dominated_beyond_balance (k x : Nat) (h : x < 7 * k) :
    Dominates k (7 * k) x := by
  unfold Dominates total greatest asymmetricA asymmetricB
  simp only [Nat.max_def]
  split <;> split <;> omega

theorem no_joint_improvement_on_frontier (k x y : Nat)
    (hl : 7 * k ≤ x) (hu : x ≤ 10 * k) (hy : y ≤ 10 * k)
    (ht : total k y ≤ total k x) (hg : greatest k y ≤ greatest k x) : y = x := by
  have hb : asymmetricB (10 * k) y ≤ greatest k y := Nat.le_max_right _ _
  rw [greatest_on_frontier k x hl hu] at hg
  simp only [total, asymmetricA, asymmetricB] at ht hg hb
  omega

theorem frontier_exact (k x : Nat) :
    Efficient k x ↔ 7 * k ≤ x ∧ x ≤ 10 * k := by
  constructor
  · rintro ⟨hu, hn⟩
    constructor
    · by_cases h : 7 * k ≤ x
      · exact h
      · have hx : x < 7 * k := by omega
        exact False.elim (hn ⟨7 * k, by omega, dominated_beyond_balance k x hx⟩)
    · exact hu
  · rintro ⟨hl, hu⟩
    refine ⟨hu, ?_⟩
    rintro ⟨y, hy, ht, hg, hs⟩
    have he := no_joint_improvement_on_frontier k x y hl hu hy ht hg
    subst y
    omega

theorem intermediate_profiles :
    (asymmetricA 10 10, asymmetricB 10 10, total 1 10, greatest 1 10) = (10,40,50,40) ∧
    (asymmetricA 10 9, asymmetricB 10 9, total 1 9, greatest 1 9) = (17,37,54,37) ∧
    (asymmetricA 10 8, asymmetricB 10 8, total 1 8, greatest 1 8) = (24,34,58,34) ∧
    (asymmetricA 10 7, asymmetricB 10 7, total 1 7, greatest 1 7) = (31,31,62,31) := by decide

theorem whole_allowance_iff (k x allowance : Nat) (hx : x ≤ 10 * k) :
    total k x ≤ 50 * k + allowance ↔ 40 * k ≤ 4 * x + allowance := by
  unfold total asymmetricA asymmetricB
  omega

/- The number 4 is a diagnostic constraint, not an ethically justified cap. -/
theorem four_point_constraint_optimum (k x : Nat) :
    (x ≤ 10 * k ∧ total k x ≤ 54 * k ∧ greatest k x ≤ 37 * k) ↔ x = 9 * k := by
  unfold total greatest asymmetricA asymmetricB
  simp only [Nat.max_def]
  split <;> omega

theorem scope_bounds_compose (reference middle final allowance₁ allowance₂ : Nat)
    (h₁ : middle ≤ reference + allowance₁) (h₂ : final ≤ middle + allowance₂) :
    final ≤ reference + (allowance₁ + allowance₂) := by omega

theorem resetting_allowance_exceeds_original_scope :
    total 1 9 ≤ total 1 10 + 4 ∧
    total 1 8 ≤ total 1 9 + 4 ∧
    total 1 7 ≤ total 1 8 + 4 ∧
    ¬ total 1 7 ≤ total 1 10 + 4 := by decide

end BoundedRiskRevision
