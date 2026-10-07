import PeriodGeneralProof

/-!
The former period-eight restriction is removed from guaranteed-draw selection.
This still uses worst-case knowing arrival, the same other live cells/workspace,
and the supplied retained-cycle cell representation. It is not average-case
selection, a claim about every realized branch, or a premise-free physical law.
-/

namespace Generative.InquirySufficiency.PeriodCostSelection

open NativePacketProcess
open PhasePeriodSelection

theorem nonrepeating_needs_eight (pattern : List Bool) (period budget : Nat)
    (positive : 0 < period)
    (nonrepeating : repeatsEveryThree pattern period ≠ true)
    (known : bothKnowableWithin pattern period budget = true) : 8 ≤ budget := by
  cases Nat.lt_or_ge budget 8 with
  | inr enough => exact enough
  | inl fewer =>
    obtain ⟨extra, sum⟩ := Nat.le.dest (Nat.le_of_lt_succ fewer)
    have seven := both_knowable_later pattern period budget extra known
    rw [sum] at seven
    exact False.elim (nonrepeating
      (PeriodGeneralProof.seven_repeatsEveryThree pattern period positive seven))

theorem three_phase_least_guaranteed_draw_unbounded (pattern : List Bool) (commands rest : Nat)
    (threeState otherState : State)
    (three : 3 ≤ pattern.length)
    (known : bothKnowableWithin pattern pattern.length commands = true)
    (threeLive : threeState.live = rest + retainedCycleCells 3)
    (otherLive : otherState.live = rest + retainedCycleCells pattern.length)
    (workspace : threeState.workspace = otherState.workspace) :
    7 * draw threeState ≤ commands * draw otherState ∧
      (pattern.length ≠ 3 → 7 * draw threeState < commands * draw otherState) := by
  have seven := PeriodGeneralProof.bothValues_at_least_seven pattern pattern.length
    (Nat.lt_of_lt_of_le (by decide) three) commands known
  have perCommand : draw threeState ≤ draw otherState := by
    cases Nat.lt_or_eq_of_le three with
    | inl longer =>
      exact Nat.le_of_lt (draw_grows_with_live threeState otherState
        (by rw [threeLive, otherLive]
            exact Nat.add_lt_add_left (retained_cells_grow 3 _ longer) rest) workspace)
    | inr same =>
      unfold draw peak
      rw [threeLive, otherLive, workspace, ← same]
      exact Nat.le_refl _
  refine ⟨Nat.mul_le_mul seven perCommand, fun different => ?_⟩
  have longer : 3 < pattern.length := by
    cases Nat.lt_or_eq_of_le three with
    | inl longer => exact longer
    | inr same => exact absurd same.symm different
  have strictly : draw threeState < draw otherState :=
    draw_grows_with_live threeState otherState
      (by rw [threeLive, otherLive]
          exact Nat.add_lt_add_left (retained_cells_grow 3 _ longer) rest) workspace
  exact Nat.mul_lt_mul_of_le_of_lt seven strictly (Nat.lt_of_lt_of_le (by decide) seven)

end Generative.InquirySufficiency.PeriodCostSelection

#print axioms Generative.InquirySufficiency.PeriodCostSelection.nonrepeating_needs_eight
#print axioms Generative.InquirySufficiency.PeriodCostSelection.three_phase_least_guaranteed_draw_unbounded
