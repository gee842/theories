import PeriodCycleWindows
import PhasePeriodSelection

/-! The three allowed local windows force actual cyclic three-periodicity.
The carrier is arbitrary and positive. A common mask covers the entire cycle.
-/

namespace Generative.InquirySufficiency.PeriodWindowPeriodicity

open PeriodCycleWindows
open PhaseCycleDerivation (bitAt allOf upto)
open PhasePeriodSelection (allOf_member member_upto)
open PeriodLocalCertificate (bit nativeWords invertedWords)

theorem core_fuel_congr (b : Nat) (positive : 0 < b) (fuel : Nat) :
    ∀ other a (ha : a < fuel) (hb : a < other),
    Nat.modCore.go b positive fuel a ha = Nat.modCore.go b positive other a hb := by
  induction fuel with
  | zero => intro other a ha hb; exact False.elim (Nat.not_lt_zero _ ha)
  | succ fuel ih =>
    intro other a ha hb
    cases other with
    | zero => exact False.elim (Nat.not_lt_zero _ hb)
    | succ other =>
      rw [Nat.modCore.go, Nat.modCore.go]
      by_cases bound : b ≤ a
      · rw [dif_pos bound, dif_pos bound]
        exact ih other (a-b) _ _
      · rw [dif_neg bound, dif_neg bound]

theorem core_below (a b : Nat) (positive : 0 < b) (less : a < b) :
    Nat.modCore a b = a := by
  unfold Nat.modCore
  rw [dif_pos positive, Nat.modCore.go, dif_neg (Nat.not_le_of_gt less)]

theorem core_sub (a b : Nat) (positive : 0 < b) (bound : b ≤ a) :
    Nat.modCore a b = Nat.modCore (a-b) b := by
  unfold Nat.modCore
  rw [dif_pos positive, dif_pos positive, Nat.modCore.go, dif_pos bound]
  exact core_fuel_congr b positive a (a-b+1) (a-b) _ _

theorem core_is_mod (a b : Nat) (positive : 0 < b) : Nat.modCore a b = a % b := by
  cases a with
  | zero => exact core_below 0 b positive positive
  | succ a =>
    change Nat.modCore (a+1) b = if b ≤ a+1 then Nat.modCore (a+1) b else a+1
    by_cases bound : b ≤ a+1
    · rw [if_pos bound]
    · rw [if_neg bound]
      exact core_below _ _ positive (Nat.lt_of_not_le bound)

theorem add_sub_cancel (a b : Nat) : a+b-b = a := by
  induction b with
  | zero => rfl
  | succ b ih =>
    rw [Nat.add_succ, Nat.succ_sub_succ]
    exact ih

theorem mod_add_period (a b : Nat) (positive : 0 < b) : (a+b) % b = a % b := by
  rw [← core_is_mod _ _ positive, ← core_is_mod _ _ positive]
  rw [core_sub _ _ positive (Nat.le_add_left b a), add_sub_cancel]

theorem mod_then_one (a b : Nat) (positive : 0 < b) :
    (a % b + 1) % b = (a+1) % b := by
  induction a using Nat.strongRecOn with
  | ind a ih =>
    cases Nat.lt_or_ge a b with
    | inl less => rw [mod_below _ _ less]
    | inr bound =>
      have less : a-b < a := Nat.sub_lt (Nat.lt_of_lt_of_le positive bound) positive
      have reduction : a%b = (a-b)%b := by
        rw [← core_is_mod _ _ positive, ← core_is_mod _ _ positive]
        exact core_sub a b positive bound
      rw [reduction, ih (a-b) less]
      have restore := PacketLawDerivation.sub_add_cancel_constructive a b bound
      have shifted : a+1 = (a-b+1)+b := by
        rw [Nat.add_right_comm, restore]
      rw [shifted, mod_add_period _ _ positive]

theorem walk_mod (period phase steps : Nat) (positive : 0 < period) (bound : phase < period) :
    walk period steps phase = (phase+steps)%period := by
  induction steps with
  | zero => exact (mod_below _ _ bound).symm
  | succ steps ih => rw [walk_step, ih, mod_then_one _ _ positive, Nat.add_assoc]

theorem walk_before (period steps : Nat) (bound : steps < period) :
    walk period steps 0 = steps := by
  induction steps with
  | zero => rfl
  | succ steps ih =>
    rw [walk_step, ih (Nat.lt_trans (Nat.lt_succ_self _) bound), mod_below _ _ bound]

theorem walk_return (period : Nat) (positive : 0 < period) : walk period period 0 = 0 := by
  cases period with
  | zero => exact False.elim (Nat.lt_irrefl _ positive)
  | succ n => rw [walk_step, walk_before _ _ (Nat.lt_succ_self n), mod_self]

inductive Third where | a | b | c
  deriving DecidableEq

def next : Third → Third | .a => .b | .b => .c | .c => .a

def code : Bool → Third → Nat
  | false, .a => 18 | false, .b => 73 | false, .c => 36
  | true, .a => 109 | true, .b => 54 | true, .c => 91

def chosenMask (inverted : Bool) : Nat := if inverted then invertedWords else nativeWords

def Allowed (inverted : Bool) (word : Nat) : Prop :=
  word = code inverted .a ∨ word = code inverted .b ∨ word = code inverted .c

instance decidableAllowed (inverted : Bool) (word : Nat) : Decidable (Allowed inverted word) :=
  inferInstanceAs (Decidable (_ ∨ _ ∨ _))

theorem allowed_certificate (inverted : Bool) :
    allOf (upto 128) (fun word => !bit (chosenMask inverted) word ||
      decide (Allowed inverted word)) = true := by
  cases inverted <;> decide +kernel

theorem masked_allowed (inverted : Bool) (word : Fin 128)
    (covered : bit (chosenMask inverted) word.val = true) : Allowed inverted word.val := by
  have accepted := allOf_member _ _ _ (allowed_certificate inverted)
    (member_upto 128 word.val word.isLt)
  rw [covered] at accepted
  exact of_decide_eq_true accepted

theorem allowed_has_tag (inverted : Bool) (word : Nat) (allowed : Allowed inverted word) :
    ∃ tag, word = code inverted tag := by
  cases allowed with
  | inl h => exact ⟨.a, h⟩
  | inr rest =>
    cases rest with
    | inl h => exact ⟨.b, h⟩
    | inr h => exact ⟨.c, h⟩

theorem allowed_successor (inverted : Bool) (tag : Third) (word : Nat)
    (allowed : Allowed inverted word)
    (edge : word = code inverted tag / 2 ∨ word = code inverted tag / 2 + 64) :
    word = code inverted (next tag) := by
  cases inverted <;> cases tag <;>
    rcases allowed with h | h | h <;> subst word <;>
    rcases edge with h | h <;> first | rfl | contradiction

theorem code_injective (inverted : Bool) (left right : Third)
    (same : code inverted left = code inverted right) : left = right := by
  cases inverted <;> cases left <;> cases right <;> first | rfl | contradiction

def turn : Nat → Third → Third
  | 0, tag => tag
  | steps + 1, tag => turn steps (next tag)

theorem turn_step (steps : Nat) (tag : Third) : turn (steps+1) tag = next (turn steps tag) := by
  induction steps generalizing tag with
  | zero => rfl
  | succ steps ih => exact ih (next tag)

theorem turn_three (steps : Nat) (tag : Third) : turn (steps+3) tag = turn steps tag := by
  cases tag <;> rfl

theorem return_divisible (steps : Nat) : ∀ tag, turn steps tag = tag → steps % 3 = 0 := by
  induction steps using Nat.strongRecOn with
  | ind steps ih =>
    intro tag same
    match steps with
    | 0 => rfl
    | 1 => cases tag <;> contradiction
    | 2 => cases tag <;> contradiction
    | steps + 3 =>
      rw [turn_three] at same
      have less : steps < steps + 3 := Nat.lt_add_of_pos_right (by decide)
      rw [mod_add_period steps 3 (by decide)]
      exact ih steps less tag same

def Covered (pattern : List Bool) (period : Nat) (inverted : Bool) : Prop :=
  ∀ phase, phase < period → bit (chosenMask inverted) (window pattern period phase).val = true

theorem windows_follow (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (inverted : Bool) (covered : Covered pattern period inverted) (tag : Third)
    (initial : (window pattern period 0).val = code inverted tag) :
    ∀ steps, (window pattern period (walk period steps 0)).val = code inverted (turn steps tag)
  | 0 => initial
  | steps + 1 => by
    have current := windows_follow pattern period positive inverted covered tag initial steps
    have bound := next_bounded period (walk period steps 0) positive
    have allowed := masked_allowed inverted (window pattern period ((walk period steps 0 + 1) % period))
      (covered _ bound)
    have edge := next_window pattern period (walk period steps 0)
    rw [current] at edge
    rw [walk_step, turn_step]
    exact allowed_successor inverted (turn steps tag) _ allowed edge

theorem covered_period_divisible (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (inverted : Bool) (covered : Covered pattern period inverted) : period % 3 = 0 := by
  obtain ⟨tag, initial⟩ := allowed_has_tag inverted (window pattern period 0).val
    (masked_allowed inverted _ (covered 0 positive))
  have final := windows_follow pattern period positive inverted covered tag initial period
  rw [walk_return period positive, initial] at final
  have same := code_injective inverted tag (turn period tag) final
  exact return_divisible period tag same.symm

theorem allowed_three_equal (inverted : Bool) (word : Nat) (allowed : Allowed inverted word) :
    bit word 0 = bit word 3 := by
  obtain ⟨tag, same⟩ := allowed_has_tag inverted word allowed
  rw [same]
  cases inverted <;> cases tag <;> rfl

theorem covered_three_step (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (inverted : Bool) (covered : Covered pattern period inverted) (phase : Nat)
    (bound : phase < period) : bitAt pattern phase = bitAt pattern ((phase+3)%period) := by
  have eq := allowed_three_equal inverted (window pattern period phase).val
    (masked_allowed inverted _ (covered phase bound))
  rw [bit_window pattern period phase 0 (by decide),
    bit_window pattern period phase 3 (by decide), walk_mod period phase 3 positive bound] at eq
  exact eq

theorem allOf_append {α : Type} (test : α → Bool) : ∀ (left right : List α),
    allOf (left ++ right) test = (allOf left test && allOf right test)
  | [], right => rfl
  | head :: rest, right => by
    change (test head && allOf (rest ++ right) test) =
      ((test head && allOf rest test) && allOf right test)
    rw [allOf_append test rest right]
    cases test head <;> rfl

theorem allOf_upto_of (test : Nat → Bool) : ∀ count,
    (∀ index, index < count → test index = true) → allOf (upto count) test = true
  | 0, _ => rfl
  | count+1, every => by
    change allOf (upto count ++ [count]) test = true
    rw [allOf_append, allOf_upto_of test count
      (fun index bound => every index (Nat.lt_trans bound (Nat.lt_succ_self count)))]
    change (test count && true) = true
    rw [every count (Nat.lt_succ_self count)]
    rfl

theorem covered_repeatsEveryThree (pattern : List Bool) (period : Nat) (positive : 0 < period)
    (inverted : Bool) (covered : Covered pattern period inverted) :
    PhasePeriodSelection.repeatsEveryThree pattern period = true := by
  have divisible := covered_period_divisible pattern period positive inverted covered
  have repeating : allOf (upto period) (fun phase =>
      bitAt pattern phase == bitAt pattern ((phase+3)%period)) = true := by
    apply allOf_upto_of
    intro phase bound
    rw [covered_three_step pattern period positive inverted covered phase bound]
    cases bitAt pattern ((phase+3)%period) <;> rfl
  unfold PhasePeriodSelection.repeatsEveryThree
  rw [divisible, repeating]
  rfl

end Generative.InquirySufficiency.PeriodWindowPeriodicity

#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.core_fuel_congr
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.core_below
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.core_sub
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.core_is_mod
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.mod_add_period
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.walk_before
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.walk_return

#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.add_sub_cancel
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.Third
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.next
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.code
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.chosenMask
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.Allowed
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.decidableAllowed
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allowed_certificate
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.masked_allowed
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allowed_has_tag
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allowed_successor
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.code_injective
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.turn
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.turn_step
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.turn_three
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.return_divisible
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.Covered
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.windows_follow
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.covered_period_divisible

#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.mod_then_one
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.walk_mod
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allowed_three_equal
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.covered_three_step
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allOf_append
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.allOf_upto_of
#print axioms Generative.InquirySufficiency.PeriodWindowPeriodicity.covered_repeatsEveryThree
