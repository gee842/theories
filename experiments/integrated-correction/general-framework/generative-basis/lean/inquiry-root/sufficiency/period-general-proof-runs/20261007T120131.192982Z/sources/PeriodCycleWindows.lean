import PeriodLocalCertificate

/-!
Concrete cyclic windows for the period-independent inquiry argument.
The seven bits are actual outputs along the same native advance operation.
No restriction on the carrier size is imposed; short cycles wrap repeatedly.
-/

namespace Generative.InquirySufficiency.PeriodCycleWindows

open PhaseCycleDerivation (bitAt)
open PeriodLocalCertificate (bit)

def walk (period : Nat) : Nat → Nat → Nat
  | 0, phase => phase
  | steps + 1, phase => walk period steps ((phase + 1) % period)

theorem walk_step (period steps phase : Nat) :
    walk period (steps + 1) phase = (walk period steps phase + 1) % period := by
  induction steps generalizing phase with
  | zero => rfl
  | succ steps ih => exact ih ((phase + 1) % period)

def encode7 (a b c d e f g : Bool) : Nat :=
  a.toNat + 2*b.toNat + 4*c.toNat + 8*d.toNat +
    16*e.toNat + 32*f.toNat + 64*g.toNat

theorem encode7_lt (a b c d e f g : Bool) : encode7 a b c d e f g < 128 := by
  cases a <;> cases b <;> cases c <;> cases d <;>
    cases e <;> cases f <;> cases g <;> decide

def window (pattern : List Bool) (period phase : Nat) : Fin 128 :=
  ⟨encode7 (bitAt pattern (walk period 0 phase))
    (bitAt pattern (walk period 1 phase)) (bitAt pattern (walk period 2 phase))
    (bitAt pattern (walk period 3 phase)) (bitAt pattern (walk period 4 phase))
    (bitAt pattern (walk period 5 phase)) (bitAt pattern (walk period 6 phase)),
    encode7_lt _ _ _ _ _ _ _⟩

theorem encoded_bits (a b c d e f g : Bool) :
    bit (encode7 a b c d e f g) 0 = a ∧
    bit (encode7 a b c d e f g) 1 = b ∧
    bit (encode7 a b c d e f g) 2 = c ∧
    bit (encode7 a b c d e f g) 3 = d ∧
    bit (encode7 a b c d e f g) 4 = e ∧
    bit (encode7 a b c d e f g) 5 = f ∧
    bit (encode7 a b c d e f g) 6 = g := by
  cases a <;> cases b <;> cases c <;> cases d <;>
    cases e <;> cases f <;> cases g <;> decide

theorem bit_window (pattern : List Bool) (period phase k : Nat) (hk : k < 7) :
    bit (window pattern period phase).val k = bitAt pattern (walk period k phase) := by
  have bits := encoded_bits
    (bitAt pattern (walk period 0 phase)) (bitAt pattern (walk period 1 phase))
    (bitAt pattern (walk period 2 phase)) (bitAt pattern (walk period 3 phase))
    (bitAt pattern (walk period 4 phase)) (bitAt pattern (walk period 5 phase))
    (bitAt pattern (walk period 6 phase))
  rcases bits with ⟨h0, h1, h2, h3, h4, h5, h6⟩
  match k with
  | 0 => exact h0
  | 1 => exact h1
  | 2 => exact h2
  | 3 => exact h3
  | 4 => exact h4
  | 5 => exact h5
  | 6 => exact h6
  | k + 7 => exact False.elim ((Nat.not_lt_of_ge (Nat.le_add_left 7 k)) hk)

theorem encode7_next (a b c d e f g h : Bool) :
    encode7 b c d e f g h = encode7 a b c d e f g / 2 ∨
    encode7 b c d e f g h = encode7 a b c d e f g / 2 + 64 := by
  cases a <;> cases b <;> cases c <;> cases d <;>
    cases e <;> cases f <;> cases g <;> cases h <;> decide

theorem encode7_previous (a b c d e f g h : Bool) :
    encode7 a b c d e f g = encode7 b c d e f g h * 2 % 128 ∨
    encode7 a b c d e f g = encode7 b c d e f g h * 2 % 128 + 1 := by
  cases a <;> cases b <;> cases c <;> cases d <;>
    cases e <;> cases f <;> cases g <;> cases h <;> decide

theorem next_window (pattern : List Bool) (period phase : Nat) :
    (window pattern period ((phase + 1) % period)).val =
      (window pattern period phase).val / 2 ∨
    (window pattern period ((phase + 1) % period)).val =
      (window pattern period phase).val / 2 + 64 :=
  encode7_next _ _ _ _ _ _ _ _

theorem previous_window_at_next (pattern : List Bool) (period phase : Nat) :
    (window pattern period phase).val =
      (window pattern period ((phase + 1) % period)).val * 2 % 128 ∨
    (window pattern period phase).val =
      (window pattern period ((phase + 1) % period)).val * 2 % 128 + 1 :=
  encode7_previous _ _ _ _ _ _ _ _

theorem next_bounded (period phase : Nat) (positive : 0 < period) :
    (phase + 1) % period < period := Nat.mod_lt _ positive

theorem mod_below (a b : Nat) (less : a < b) : a % b = a := by
  cases a with
  | zero => rfl
  | succ a =>
    change (if b ≤ a + 1 then Nat.modCore (a + 1) b else a + 1) = a + 1
    exact if_neg (Nat.not_le_of_gt less)

theorem mod_self (n : Nat) : n % n = 0 := by
  cases n with
  | zero => rfl
  | succ n =>
    change (if n + 1 ≤ n + 1 then Nat.modCore (n + 1) (n + 1) else n + 1) = 0
    rw [if_pos (Nat.le_refl _)]
    unfold Nat.modCore
    rw [dif_pos (Nat.zero_lt_succ n), Nat.modCore.go, dif_pos (Nat.le_refl _)]
    simp only [Nat.sub_self]
    rw [Nat.modCore.go, dif_neg (Nat.not_le_of_gt (Nat.zero_lt_succ n))]

theorem predecessor (period phase : Nat) (positive : 0 < period) (bounded : phase < period) :
    ∃ previous, previous < period ∧ (previous + 1) % period = phase := by
  cases phase with
  | zero =>
    refine ⟨period - 1, Nat.sub_lt positive (by decide), ?_⟩
    have eq : period - 1 + 1 = period :=
      PacketLawDerivation.sub_add_cancel_constructive period 1 positive
    rw [eq, mod_self]
  | succ phase =>
    exact ⟨phase, Nat.lt_trans (Nat.lt_succ_self phase) bounded, mod_below _ _ bounded⟩

theorem previous_window (pattern : List Bool) (period phase : Nat)
    (positive : 0 < period) (bounded : phase < period) :
    ∃ previous, previous < period ∧
      ((window pattern period previous).val = (window pattern period phase).val * 2 % 128 ∨
       (window pattern period previous).val = (window pattern period phase).val * 2 % 128 + 1) := by
  obtain ⟨previous, bound, eq⟩ := predecessor period phase positive bounded
  have windowEq := previous_window_at_next pattern period previous
  rw [eq] at windowEq
  exact ⟨previous, bound, windowEq⟩

end Generative.InquirySufficiency.PeriodCycleWindows

#print axioms Generative.InquirySufficiency.PeriodCycleWindows.walk
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.walk_step
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.encode7
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.encode7_lt
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.window
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.encoded_bits
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.bit_window
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.encode7_next
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.encode7_previous
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.next_window
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.previous_window_at_next
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.next_bounded
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.mod_below
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.mod_self
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.predecessor
#print axioms Generative.InquirySufficiency.PeriodCycleWindows.previous_window
