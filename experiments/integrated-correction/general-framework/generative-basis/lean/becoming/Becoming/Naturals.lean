/-!
# Naturals: the subtraction and order laws of the core's drawn amounts, constructively

The core's models of a requested change carried out (`Becoming.Actuation` and the modules after it) draw amounts
from a reserve with truncated subtraction and compare them with an order. Lean's prelude proves
several of the laws they need (`Nat.sub_add_cancel`, `Nat.add_sub_cancel`, `Nat.sub_sub`, …)
with `propext`, so the core cannot cite them. This module proves the ones the models use, by
recursion on the naturals, with empty axiom reports.

* **Subtraction.** Taking away what was added gives back the start (`add_sub_cancel`,
  `add_sub_cancel_left`); adding back what was taken from enough gives back the start
  (`sub_add_cancel`); taking away twice is taking away the sum (`sub_sub`); and a sum within a
  bound leaves room for its second term (`le_sub_of_add_le`).
* **Order.** A sum within a bound bounds each term (`le_of_add_le_left`, `le_of_add_le_right`),
  and an equation or an order survives adding the same amount (`add_right_cancel`,
  `le_of_add_le_add_right`).

No premise; every declaration has an empty axiom report.
-/

namespace Becoming

namespace Naturals

theorem succ_sub_succ (n m : Nat) : (n + 1) - (m + 1) = n - m := Nat.succ_sub_succ n m

theorem add_sub_cancel (a : Nat) : ∀ c : Nat, a + c - c = a
  | 0 => rfl
  | c + 1 => (succ_sub_succ (a + c) c).trans (add_sub_cancel a c)

theorem add_sub_cancel_left (c a : Nat) : c + a - c = a :=
  (congrArg (· - c) (Nat.add_comm c a)).trans (add_sub_cancel a c)

theorem sub_add_cancel : ∀ {a c : Nat}, c ≤ a → a - c + c = a
  | _, 0, _ => rfl
  | 0, _ + 1, h => absurd h (Nat.not_succ_le_zero _)
  | a + 1, c + 1, h =>
    (congrArg (· + (c + 1)) (succ_sub_succ a c)).trans
      (congrArg (· + 1) (sub_add_cancel (Nat.le_of_succ_le_succ h)))

theorem add_sub_of_le {a c : Nat} (h : c ≤ a) : c + (a - c) = a :=
  (Nat.add_comm c (a - c)).trans (sub_add_cancel h)

theorem sub_sub (n a : Nat) : ∀ b : Nat, n - a - b = n - (a + b)
  | 0 => rfl
  | b + 1 => congrArg Nat.pred (sub_sub n a b)

theorem le_of_add_le_left {a b c : Nat} (h : a + b ≤ c) : b ≤ c :=
  Nat.le_trans (Nat.le_add_left b a) h

theorem le_of_add_le_right {a b c : Nat} (h : a + b ≤ c) : a ≤ c :=
  Nat.le_trans (Nat.le_add_right a b) h

theorem add_right_cancel {a b : Nat} : ∀ {k : Nat}, a + k = b + k → a = b
  | 0, same => same
  | k + 1, same => add_right_cancel (k := k) (Nat.succ.inj same)

theorem add_left_cancel {a b k : Nat} (same : k + a = k + b) : a = b :=
  add_right_cancel ((Nat.add_comm a k).trans (same.trans (Nat.add_comm k b)))

theorem le_of_add_le_add_right {a b : Nat} : ∀ {k : Nat}, a + k ≤ b + k → a ≤ b
  | 0, h => h
  | k + 1, h => le_of_add_le_add_right (k := k) (Nat.le_of_succ_le_succ h)

theorem le_of_add_le_add_left {a b k : Nat} (h : k + a ≤ k + b) : a ≤ b :=
  le_of_add_le_add_right ((Nat.add_comm a k) ▸ (Nat.add_comm b k) ▸ h)

theorem le_sub_of_add_le {a b n : Nat} (h : a + b ≤ n) : b ≤ n - a :=
  le_of_add_le_add_left (k := a)
    (Nat.le_trans h (Nat.le_of_eq (add_sub_of_le (le_of_add_le_right h)).symm))

theorem add_le_of_le_sub {a b n : Nat} (within : a ≤ n) (h : b ≤ n - a) : a + b ≤ n :=
  Nat.le_trans (Nat.add_le_add_left h a) (Nat.le_of_eq (add_sub_of_le within))

/-- What is left after drawing, plus what was drawn, is what there was. -/
theorem sub_add_add {r d c : Nat} (within : c ≤ r) : r - c + (d + c) = r + d :=
  ((Nat.add_assoc (r - c) d c).symm.trans (Nat.add_right_comm (r - c) d c)).trans
    (congrArg (· + d) (sub_add_cancel within))

theorem lt_irrefl (n : Nat) : ¬ n < n := Nat.lt_irrefl n

theorem ne_of_lt {a b : Nat} (h : a < b) : a ≠ b := fun e => lt_irrefl b (e ▸ h)

theorem succ_ne_self (n : Nat) : n + 1 ≠ n := fun e => lt_irrefl n (Nat.lt_of_lt_of_le (Nat.lt_succ_self n) (Nat.le_of_eq e))

end Naturals

end Becoming
