import PeriodCoverRules
import PeriodFirstRead

/-! Every bounded normalized inquiry policy is covered by one certified finite
word family member. These families may overapproximate policies: sound coverage,
not exact enumeration or realizability of every retained member, is sufficient.
The second theorem identifies local word evaluation with the original policy
semantics on arbitrary cyclic output patterns. -/
namespace Generative.InquirySufficiency.PeriodPolicyCover
open PhaseCycleDerivation (bitAt)
open PhasePeriodSelection (allOf_member member_upto)
open PeriodLocalCertificate (bit)
open PeriodCoverRules
open PeriodStrategySemantics (wins moved)
open PeriodCycleWindows (walk window bit_window walk_step)

def localWins (value : Bool) : {budget : Nat} → PeriodStrategySemantics.Policy budget →
    Fin 128 → Nat → Bool
  | _, .stop, word, position => bit word.val position == value
  | _, .advance later, word, position => localWins value later word (position + 1)
  | _, .read low high, word, position =>
    if bit word.val position != bit word.val 0 then localWins value high word position
    else localWins value low word position

theorem child_read_bound (budget position : Nat) (bounded : budget + 1 + position < 7) :
    budget + position < 7 :=
  Nat.lt_of_le_of_lt (Nat.add_le_add_right (Nat.le_succ budget) position) bounded

theorem child_advance_bound (budget position : Nat) (bounded : budget + 1 + position < 7) :
    budget + (position + 1) < 7 := by
  rw [Nat.add_assoc, Nat.add_comm 1 position] at bounded
  exact bounded

theorem policy_covered (value : Bool) {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) :
    ∀ position, budget + position < 7 →
      ∃ index, index < (family budget position value).length ∧
        ∀ word : Fin 128, localWins value policy word position = true →
          bit (mask budget position value index) word.val = true := by
  induction policy with
  | @stop budget =>
    intro position bounded
    have rule := stop_rule budget position value bounded
    refine ⟨stopIndex budget position value, of_decide_eq_true (left_true rule), ?_⟩
    intro word success
    have point := allOf_member _ _ _ (right_true rule) (member_upto 128 word.val word.isLt)
    exact implies_true point success
  | @advance budget later ih =>
    intro position bounded
    obtain ⟨child,childBound,covered⟩ := ih (position + 1) (child_advance_bound budget position bounded)
    have rule := allOf_member _ _ _ (advance_rule budget position value bounded)
      (member_upto _ child childBound)
    refine ⟨advanceIndex (budget + 1) position value child, of_decide_eq_true (left_true rule), ?_⟩
    intro word success
    have point := allOf_member _ _ _ (right_true rule) (member_upto 128 word.val word.isLt)
    exact implies_true point (covered word success)
  | @read budget low high lowIH highIH =>
    intro position bounded
    obtain ⟨lowIndex,lowBound,lowCover⟩ := lowIH position (child_read_bound budget position bounded)
    obtain ⟨highIndex,highBound,highCover⟩ := highIH position (child_read_bound budget position bounded)
    have row := allOf_member _ _ _ (read_rule budget position value bounded)
      (member_upto _ lowIndex lowBound)
    have rule := allOf_member _ _ _ row (member_upto _ highIndex highBound)
    refine ⟨readIndex (budget + 1) position value lowIndex highIndex,
      of_decide_eq_true (left_true rule), ?_⟩
    intro word success
    have point := allOf_member _ _ _ (right_true rule) (member_upto 128 word.val word.isLt)
    apply implies_true point
    unfold localWins at success
    cases reading : bit word.val position != bit word.val 0 with
    | false => rw [reading] at success; exact lowCover word success
    | true => rw [reading] at success; exact highCover word success

theorem local_is_original (pattern : List Bool) (period phase : Nat) (value : Bool)
    {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) :
    ∀ position, budget + position < 7 →
      localWins value policy (window pattern period phase) position =
        wins pattern period value policy (walk period position phase,bitAt pattern phase) := by
  induction policy with
  | @stop budget =>
    intro position bounded
    have positionBound := Nat.lt_of_le_of_lt (Nat.le_add_left position budget) bounded
    exact congrArg (fun b => b == value) (bit_window pattern period phase position positionBound)
  | @advance budget later ih =>
    intro position bounded
    have original := ih (position + 1) (child_advance_bound budget position bounded)
    change localWins value later (window pattern period phase) (position + 1) = _
    rw [original,walk_step]
    rfl
  | @read budget low high lowIH highIH =>
    intro position bounded
    have childBound := child_read_bound budget position bounded
    have positionBound := Nat.lt_of_le_of_lt (Nat.le_add_left position budget) childBound
    unfold localWins wins
    rw [bit_window pattern period phase position positionBound,
      bit_window pattern period phase 0 (by decide)]
    change (if bitAt pattern (walk period position phase) != bitAt pattern phase then _ else _) = _
    cases reading : bitAt pattern (walk period position phase) != bitAt pattern phase with
    | false => exact lowIH position childBound
    | true => exact highIH position childBound

theorem winning_residual_covered (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (bounded : budget < 7) (policy : PeriodStrategySemantics.Policy budget)
    (works : ∀ phase, phase < period → wins pattern period value policy (phase,bitAt pattern phase) = true) :
    ∃ index, index < (family budget 0 value).length ∧
      ∀ phase, phase < period → bit (mask budget 0 value index) (window pattern period phase).val = true := by
  obtain ⟨index,indexBound,covered⟩ := policy_covered value policy 0 bounded
  refine ⟨index,indexBound,fun phase phaseBound => ?_⟩
  apply covered (window pattern period phase)
  rw [local_is_original pattern period phase value policy 0 bounded]
  exact works phase phaseBound

end Generative.InquirySufficiency.PeriodPolicyCover

#print axioms Generative.InquirySufficiency.PeriodPolicyCover.localWins
#print axioms Generative.InquirySufficiency.PeriodPolicyCover.child_read_bound
#print axioms Generative.InquirySufficiency.PeriodPolicyCover.child_advance_bound
#print axioms Generative.InquirySufficiency.PeriodPolicyCover.policy_covered
#print axioms Generative.InquirySufficiency.PeriodPolicyCover.local_is_original
#print axioms Generative.InquirySufficiency.PeriodPolicyCover.winning_residual_covered
