import PeriodStrategySemantics
import PeriodCycleWindows

/-! Constructive removal of leading advances, with first-read zero normalization.
The phase permutation is applied only while every bounded phase and both
inversions remain possible. No symmetry between the two observed branches is
assumed. -/
namespace Generative.InquirySufficiency.PeriodFirstRead

open PhaseCycleDerivation (bitAt)
open PhasePeriodSelection
open PeriodStrategySemantics

/-- Add unused budget without adding a command. -/
def pad : {budget : Nat} → PeriodStrategySemantics.Policy budget → PeriodStrategySemantics.Policy (budget + 1)
  | _, .stop => .stop
  | _, .advance later => .advance (pad later)
  | _, .read low high => .read (pad low) (pad high)

theorem pad_wins (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) (candidate : Nat × Bool) :
    wins pattern period value (pad policy) candidate = wins pattern period value policy candidate := by
  induction policy generalizing candidate with
  | stop => rfl
  | advance later ih => exact ih (moved period candidate)
  | read low high lowIH highIH =>
    unfold pad wins
    cases reading : (bitAt pattern candidate.1 != candidate.2) with
    | false => exact lowIH candidate
    | true => exact highIH candidate

def Full (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) : Prop :=
  ∀ phase, phase < period → ∀ inversion, wins pattern period value policy (phase,inversion) = true

theorem bool_eq_of_beq {a b : Bool} (yes : (a == b) = true) : a = b := by
  cases a <;> cases b <;> first | rfl | cases yes

theorem unknown_member (period phase : Nat) (inversion : Bool) (bound : phase < period) :
    (phase,inversion) ∈ unknownStart period := by
  have member := member_upto period phase bound
  cases inversion with
  | false => exact member_append_left _ (member_map (fun p => (p,false)) member)
  | true => exact member_append_right _ (member_map (fun p => (p,true)) member)

theorem full_of_success {pattern : List Bool} {period : Nat} {value : Bool}
    {budget : Nat} {policy : PeriodStrategySemantics.Policy budget}
    (succeeds : Succeeds pattern period value policy (unknownStart period)) :
    Full pattern period value policy :=
  fun phase bound inversion => succeeds _ (unknown_member period phase inversion bound)

/-- Actual endpoint phase of a bounded policy. -/
def endPhase (pattern : List Bool) (period : Nat) :
    {budget : Nat} → PeriodStrategySemantics.Policy budget → (Nat × Bool) → Nat
  | _, .stop, candidate => candidate.1
  | _, .advance later, candidate => endPhase pattern period later (moved period candidate)
  | _, .read low high, candidate =>
    if bitAt pattern candidate.1 != candidate.2 then endPhase pattern period high candidate
    else endPhase pattern period low candidate

theorem end_bounded (pattern : List Bool) (period : Nat) (positive : 0 < period)
    {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) (candidate : Nat × Bool)
    (bound : candidate.1 < period) : endPhase pattern period policy candidate < period := by
  induction policy generalizing candidate with
  | stop => exact bound
  | advance later ih =>
    exact ih (moved period candidate) (PeriodCycleWindows.next_bounded period candidate.1 positive)
  | read low high lowIH highIH =>
    unfold endPhase
    cases reading : (bitAt pattern candidate.1 != candidate.2) with
    | false => exact lowIH candidate bound
    | true => exact highIH candidate bound

theorem wins_at_end (pattern : List Bool) (period : Nat) (value : Bool)
    {budget : Nat} (policy : PeriodStrategySemantics.Policy budget) (candidate : Nat × Bool) :
    wins pattern period value policy candidate =
      (bitAt pattern (endPhase pattern period policy candidate) == value) := by
  induction policy generalizing candidate with
  | stop => rfl
  | advance later ih => exact ih (moved period candidate)
  | read low high lowIH highIH =>
    unfold wins endPhase
    cases reading : (bitAt pattern candidate.1 != candidate.2) with
    | false => exact lowIH candidate
    | true => exact highIH candidate

theorem full_reaches_value {pattern : List Bool} {period : Nat} {value : Bool}
    (positive : 0 < period) {budget : Nat} {policy : PeriodStrategySemantics.Policy budget}
    (full : Full pattern period value policy) :
    ∃ phase, phase < period ∧ bitAt pattern phase = value := by
  have success := full 0 positive false
  rw [wins_at_end] at success
  exact ⟨endPhase pattern period policy (0,false), end_bounded pattern period positive policy (0,false) positive,
    bool_eq_of_beq success⟩

/-- A positive-budget uniformly winning policy can be replaced by the zero
branch of its first read, after deleting any initial advances. The replacement
has one fewer command available and succeeds with inversion equal to the first
actual output at every bounded phase. -/
theorem normalize_first_read (pattern : List Bool) (period : Nat) (value : Bool)
    (predecessor : ∀ phase, phase < period → ∃ previous, previous < period ∧ (previous + 1) % period = phase)
    (opposite : ∃ phase, phase < period ∧ bitAt pattern phase ≠ value) :
    ∀ budget (policy : PeriodStrategySemantics.Policy (budget + 1)), Full pattern period value policy →
      ∃ residual : PeriodStrategySemantics.Policy budget, ∀ phase, phase < period →
        wins pattern period value residual (phase,bitAt pattern phase) = true := by
  have noStop : ∀ {budget}, ¬ Full pattern period value (PeriodStrategySemantics.Policy.stop (budget := budget)) := by
    intro budget full
    obtain ⟨phase,bound,different⟩ := opposite
    exact different (bool_eq_of_beq (full phase bound false))
  have afterAdvance : ∀ {budget} (later : PeriodStrategySemantics.Policy budget),
      Full pattern period value (.advance later) → Full pattern period value later := by
    intro budget later full phase bound inversion
    obtain ⟨previous,before,step⟩ := predecessor phase bound
    have actual := full previous before inversion
    change wins pattern period value later (((previous + 1) % period),inversion) = true at actual
    rw [step] at actual
    exact actual
  have afterRead : ∀ {budget} (low high : PeriodStrategySemantics.Policy budget),
      Full pattern period value (.read low high) →
      ∀ phase, phase < period → wins pattern period value low (phase,bitAt pattern phase) = true := by
    intro budget low high full phase bound
    have actual := full phase bound (bitAt pattern phase)
    change (if bitAt pattern phase != bitAt pattern phase then _ else _) = true at actual
    cases reading : bitAt pattern phase <;> rw [reading] at actual <;> exact actual
  have shorter : ∀ {budget} (policy : PeriodStrategySemantics.Policy budget), Full pattern period value policy →
      ∃ used, used < budget ∧ ∃ residual : PeriodStrategySemantics.Policy used,
        ∀ phase, phase < period → wins pattern period value residual (phase,bitAt pattern phase) = true := by
    intro budget policy
    induction policy with
    | stop => intro full; exact False.elim (noStop full)
    | @read budget low high lowIH highIH =>
      intro full
      exact ⟨budget,Nat.lt_succ_self budget,low,afterRead low high full⟩
    | @advance budget later ih =>
      intro full
      obtain ⟨used,bound,residual,works⟩ := ih (afterAdvance later full)
      exact ⟨used,Nat.lt_trans bound (Nat.lt_succ_self budget),residual,works⟩
  have enlarge : ∀ {used} (residual : PeriodStrategySemantics.Policy used) (extra : Nat),
      ∃ larger : PeriodStrategySemantics.Policy (used + extra),
        ∀ candidate, wins pattern period value larger candidate = wins pattern period value residual candidate := by
    intro used residual extra
    induction extra with
    | zero => exact ⟨residual,fun _ => rfl⟩
    | succ extra ih =>
      obtain ⟨larger,equal⟩ := ih
      exact ⟨pad larger,fun candidate => (pad_wins _ _ _ _ _).trans (equal candidate)⟩
  intro budget policy full
  obtain ⟨used,bound,residual,works⟩ := shorter policy full
  obtain ⟨extra,equal⟩ := Nat.le.dest (Nat.le_of_lt_succ bound)
  obtain ⟨larger,same⟩ := enlarge residual extra
  cases equal
  exact ⟨larger,fun phase bound => (same _).trans (works phase bound)⟩

end Generative.InquirySufficiency.PeriodFirstRead

#print axioms Generative.InquirySufficiency.PeriodFirstRead.pad
#print axioms Generative.InquirySufficiency.PeriodFirstRead.pad_wins
#print axioms Generative.InquirySufficiency.PeriodFirstRead.Full
#print axioms Generative.InquirySufficiency.PeriodFirstRead.bool_eq_of_beq
#print axioms Generative.InquirySufficiency.PeriodFirstRead.unknown_member
#print axioms Generative.InquirySufficiency.PeriodFirstRead.full_of_success
#print axioms Generative.InquirySufficiency.PeriodFirstRead.endPhase
#print axioms Generative.InquirySufficiency.PeriodFirstRead.end_bounded
#print axioms Generative.InquirySufficiency.PeriodFirstRead.wins_at_end
#print axioms Generative.InquirySufficiency.PeriodFirstRead.full_reaches_value
#print axioms Generative.InquirySufficiency.PeriodFirstRead.normalize_first_read
