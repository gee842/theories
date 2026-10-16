import PracticalJudgment

/-
Two-tier loss comparison, 8 October 2026.

These are standard order/comparison diagnostics under a supplied classification.
The counts must represent distinct, relevant loss relationships. Neither tier
assignment nor interchangeability/additivity follows from these definitions.
Positive base/increment parameters are a diagnostic family, not ethical utility.
Unanimity in that family is not unanimity among all warranted ethical views.
LC's normative force, chances, permissions, dependencies and residual claims
remain separately justified. No theorem below makes a cost inequality decisive.
-/
namespace UnequalBasicLosses

/-- Number of lower-tier and higher-tier losses, respectively. Both are basic. -/
abbrev Profile := Nat × Nat

def total (p : Profile) : Nat := p.1 + p.2

/-- Fewer losses at each of the two supplied severity thresholds. -/
def CumulativeLE (a b : Profile) : Prop := total a ≤ total b ∧ a.2 ≤ b.2

def CumulativeLT (a b : Profile) : Prop :=
  CumulativeLE a b ∧ (total a < total b ∨ a.2 < b.2)

/-- Lower-tier weight = base; higher-tier weight = base + increment. -/
def diagnosticCost (base increment : Nat) (p : Profile) : Nat :=
  base * total p + increment * p.2

theorem positive_linear_diagnostics_iff (a b c d : Nat) :
    (∀ x y : Nat, 0 < x → 0 < y → x * a + y * b ≤ x * c + y * d) ↔
      a ≤ c ∧ b ≤ d := by
  constructor
  · intro all
    constructor
    · by_cases h : a ≤ c
      · exact h
      apply False.elim
      have step : c + 1 ≤ a := by omega
      have scale := Nat.mul_le_mul_left (d + 1) step
      have bound := all (d + 1) 1 (by omega) (by omega)
      simp only [Nat.mul_add, Nat.mul_one, Nat.one_mul] at scale bound
      omega
    · by_cases h : b ≤ d
      · exact h
      apply False.elim
      have step : d + 1 ≤ b := by omega
      have scale := Nat.mul_le_mul_left (c + 1) step
      have bound := all 1 (c + 1) (by omega) (by omega)
      simp only [Nat.mul_add, Nat.mul_one, Nat.one_mul] at scale bound
      omega
  · rintro ⟨hac, hbd⟩ x y _ _
    exact Nat.add_le_add (Nat.mul_le_mul_left x hac) (Nat.mul_le_mul_left y hbd)

theorem cumulative_iff_all_positive_diagnostics (a b : Profile) :
    CumulativeLE a b ↔
      ∀ x y : Nat, 0 < x → 0 < y → diagnosticCost x y a ≤ diagnosticCost x y b := by
  exact (positive_linear_diagnostics_iff (total a) a.2 (total b) b.2).symm

theorem strict_cumulative_iff_all_positive_diagnostics (a b : Profile) :
    CumulativeLT a b ↔
      ∀ x y : Nat, 0 < x → 0 < y → diagnosticCost x y a < diagnosticCost x y b := by
  constructor
  · rintro ⟨⟨ht, hh⟩, strict⟩ x y hx hy
    rcases strict with strict | strict
    · have left := Nat.mul_lt_mul_of_pos_left strict hx
      have right := Nat.mul_le_mul_left y hh
      exact Nat.add_lt_add_of_lt_of_le left right
    · have left := Nat.mul_le_mul_left x ht
      have right := Nat.mul_lt_mul_of_pos_left strict hy
      exact Nat.add_lt_add_of_le_of_lt left right
  · intro all
    have weak : CumulativeLE a b :=
      (cumulative_iff_all_positive_diagnostics a b).mpr
        (fun x y hx hy => Nat.le_of_lt (all x y hx hy))
    refine ⟨weak, ?_⟩
    have strict := all 1 1 (by decide) (by decide)
    simp only [diagnosticCost, Nat.one_mul] at strict
    omega

theorem cumulative_strict_irrefl (a : Profile) : ¬ CumulativeLT a a := by
  simp [CumulativeLT]

theorem cumulative_strict_trans {a b c : Profile}
    (ab : CumulativeLT a b) (bc : CumulativeLT b c) : CumulativeLT a c := by
  unfold CumulativeLT CumulativeLE at *
  omega

/-- Every member respects the two individual numerical sensitivities, without
thereby agreeing on their joint tradeoff or establishing the ethical principles. -/
theorem individual_sensitivities_agree (x y : Nat) (hx : 0 < x) (hy : 0 < y) :
    diagnosticCost x y (1, 0) < diagnosticCost x y (0, 1) ∧
    ∀ n m : Nat, n < m →
      diagnosticCost x y (n, 0) < diagnosticCost x y (m, 0) ∧
      diagnosticCost x y (0, n) < diagnosticCost x y (0, m) := by
  constructor
  · apply (strict_cumulative_iff_all_positive_diagnostics _ _).mp ?_ x y hx hy
    simp [CumulativeLT, CumulativeLE, total]
  · intro n m hnm
    constructor
    · apply (strict_cumulative_iff_all_positive_diagnostics _ _).mp ?_ x y hx hy
      simp only [CumulativeLT, CumulativeLE, total, Nat.add_zero]
      omega
    · apply (strict_cumulative_iff_all_positive_diagnostics _ _).mp ?_ x y hx hy
      simp only [CumulativeLT, CumulativeLE, total, Nat.zero_add]
      omega

theorem one_higher_two_lower_cross_thresholds :
    ¬ CumulativeLE (0, 1) (2, 0) ∧ ¬ CumulativeLE (2, 0) (0, 1) := by
  simp [CumulativeLE, total]

theorem positive_diagnostics_reverse_crossed_case :
    diagnosticCost 1 2 (2, 0) < diagnosticCost 1 2 (0, 1) ∧
    diagnosticCost 2 1 (0, 1) < diagnosticCost 2 1 (2, 0) := by
  decide

/- The inventory is a supplied scope of actual grounds; it must be complete and
   without duplicates to serve as a faithful count. Report identifiers already
   refer to those grounds. This representation result does not acquire that
   correspondence or discover ethical units from unclassified reports. -/
def reportedGrounds {G : Type} [DecidableEq G] (inventory reports : List G) : List G :=
  inventory.filter (fun g => decide (g ∈ reports))

theorem same_reported_grounds_same_inventory {G : Type} [DecidableEq G]
    (inventory left right : List G) (same : ∀ g, g ∈ left ↔ g ∈ right) :
    reportedGrounds inventory left = reportedGrounds inventory right := by
  unfold reportedGrounds
  apply List.filter_congr
  intro g _
  simp only [same g]

theorem duplicating_reports_does_not_multiply_grounds {G : Type} [DecidableEq G]
    (inventory reports : List G) :
    reportedGrounds inventory (reports ++ reports) = reportedGrounds inventory reports := by
  apply same_reported_grounds_same_inventory
  intro g
  simp

theorem duplicate_row_count_can_reverse_comparison :
    ([false] : List Bool).length < [false, true].length ∧
    [false, true].length < ([false, false, false] : List Bool).length ∧
    (reportedGrounds [false, true] [false, false, false]).length <
      (reportedGrounds [false, true] [false, true]).length := by
  decide

/- Direct interruption counts do not automatically preserve whole outcomes.
   One shared provision has two substitute supplies and one necessary relay.
   Both routes interrupt one position. The single dependency law determines
   whether the provision continues; no favorable verdict is toggled freely. -/
inductive SupportPoint where
  | mainSupply
  | spareSupply
  | relay
  deriving DecidableEq

def directLossProfile (lost : List SupportPoint) : Profile := (lost.length, 0)

def provisionContinues (lost : List SupportPoint) : Prop :=
  (SupportPoint.mainSupply ∉ lost ∨ SupportPoint.spareSupply ∉ lost) ∧
    SupportPoint.relay ∉ lost

theorem equal_direct_profiles_different_common_continuation :
    directLossProfile [.spareSupply] = directLossProfile [.relay] ∧
    provisionContinues [.spareSupply] ∧ ¬ provisionContinues [.relay] := by
  simp [directLossProfile, provisionContinues]

theorem direct_profile_does_not_determine_continuation :
    ¬ ∃ classify : Profile → Prop,
      ∀ lost, classify (directLossProfile lost) ↔ provisionContinues lost := by
  rintro ⟨classify, correct⟩
  obtain ⟨same, yes, no⟩ := equal_direct_profiles_different_common_continuation
  have recognized := (correct [.spareSupply]).mpr yes
  rw [same] at recognized
  exact no ((correct [.relay]).mp recognized)

/-- The inherited comparator can see the shared protection lost by the profile.
This does not classify every direct interruption as ethically interchangeable. -/
theorem common_support_distinguishes_histories_in_existing_comparator :
    PracticalJudgment.Better
      (fun lost (_ : Unit) => provisionContinues lost)
      (fun (_ : List SupportPoint) (_ : Unit) => False)
      [.spareSupply] [.relay] := by
  apply PracticalJudgment.protection_anchor (c := ())
  · intro _ h
    exact False.elim (equal_direct_profiles_different_common_continuation.2.2 h)
  · exact equal_direct_profiles_different_common_continuation.2.1
  · exact equal_direct_profiles_different_common_continuation.2.2

end UnequalBasicLosses
