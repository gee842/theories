import PeriodPolicyCover
import PeriodPrunedCover
import PeriodWindowPeriodicity

/-! Period-independent conclusions for the original knowsWithin game.
The carrier is positive; no bound on its size or on the output pattern is used.
Knowing both values means a possibly different adaptive strategy for each
requested value, each required to succeed at every unknown phase/inversion.
Commands are worst-case budgets, not lengths of every realized branch. -/
namespace Generative.InquirySufficiency.PeriodGeneralProof
open PhaseCycleDerivation (bitAt)
open PhasePeriodSelection
open PeriodStrategySemantics (knows_has_policy)
open PeriodFirstRead
open PeriodPolicyCover (winning_residual_covered)
open PeriodCoverRules (family mask left_true right_true)
open PeriodPrunedCover (Covered)

theorem residual_covers (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (budget : Nat) (bounded : budget < 7)
    (known : bothKnowableWithin pattern period (budget + 1) = true) :
    ∃ i0 i1, i0 < (family budget 0 false).length ∧ i1 < (family budget 0 true).length ∧
      Covered pattern period (mask budget 0 false i0) ∧
      Covered pattern period (mask budget 0 true i1) := by
  obtain ⟨low,lowWins⟩ := knows_has_policy pattern period false (budget + 1) _ (left_true known)
  obtain ⟨high,highWins⟩ := knows_has_policy pattern period true (budget + 1) _ (right_true known)
  have lowFull := full_of_success lowWins
  have highFull := full_of_success highWins
  obtain ⟨lowPhase,lowBound,lowValue⟩ := full_reaches_value positive lowFull
  obtain ⟨highPhase,highBound,highValue⟩ := full_reaches_value positive highFull
  have oppositeLow : ∃ phase, phase < period ∧ bitAt pattern phase ≠ false :=
    ⟨highPhase,highBound,by rw [highValue]; decide⟩
  have oppositeHigh : ∃ phase, phase < period ∧ bitAt pattern phase ≠ true :=
    ⟨lowPhase,lowBound,by rw [lowValue]; decide⟩
  have before := fun phase bound => PeriodCycleWindows.predecessor period phase positive bound
  obtain ⟨lowResidual,lowWorks⟩ := normalize_first_read pattern period false before oppositeLow budget low lowFull
  obtain ⟨highResidual,highWorks⟩ := normalize_first_read pattern period true before oppositeHigh budget high highFull
  obtain ⟨i0,b0,c0⟩ := winning_residual_covered pattern period false bounded lowResidual lowWorks
  obtain ⟨i1,b1,c1⟩ := winning_residual_covered pattern period true bounded highResidual highWorks
  exact ⟨i0,i1,b0,b1,c0,c1⟩

theorem no_six_commands (pattern : List Bool) (period : Nat) (positive : 0 < period) :
    bothKnowableWithin pattern period 6 ≠ true := by
  intro known
  obtain ⟨i0,i1,b0,b1,c0,c1⟩ := residual_covers pattern period positive 5 (by decide) known
  exact PeriodPrunedCover.six_impossible pattern period positive i0 i1 b0 b1 c0 c1

theorem bothValues_at_least_seven (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (budget : Nat) (known : bothKnowableWithin pattern period budget = true) : 7 ≤ budget := by
  cases Nat.lt_or_ge budget 7 with
  | inr enough => exact enough
  | inl fewer =>
    obtain ⟨extra,sum⟩ := Nat.le.dest (Nat.le_of_lt_succ fewer)
    have six := both_knowable_later pattern period budget extra known
    rw [sum] at six
    exact False.elim (no_six_commands pattern period positive six)

theorem seven_has_one_triple (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (known : bothKnowableWithin pattern period 7 = true) :
    Covered pattern period PeriodLocalCertificate.nativeWords ∨
      Covered pattern period PeriodLocalCertificate.invertedWords := by
  obtain ⟨i0,i1,b0,b1,c0,c1⟩ := residual_covers pattern period positive 6 (by decide) known
  exact PeriodPrunedCover.seven_classified pattern period positive i0 i1 b0 b1 c0 c1

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem seven_repeatsEveryThree (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (known : bothKnowableWithin pattern period 7 = true) : repeatsEveryThree pattern period = true := by
  cases seven_has_one_triple pattern period positive known with
  | inl covered => exact PeriodWindowPeriodicity.covered_repeatsEveryThree pattern period positive false covered
  | inr covered => exact PeriodWindowPeriodicity.covered_repeatsEveryThree pattern period positive true covered

end Generative.InquirySufficiency.PeriodGeneralProof

#print axioms Generative.InquirySufficiency.PeriodGeneralProof.residual_covers
#print axioms Generative.InquirySufficiency.PeriodGeneralProof.no_six_commands
#print axioms Generative.InquirySufficiency.PeriodGeneralProof.bothValues_at_least_seven
#print axioms Generative.InquirySufficiency.PeriodGeneralProof.seven_has_one_triple
#print axioms Generative.InquirySufficiency.PeriodGeneralProof.seven_repeatsEveryThree
