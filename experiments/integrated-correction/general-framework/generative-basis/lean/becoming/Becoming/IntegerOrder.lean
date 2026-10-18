import Becoming.Integers

/-!
# Integer order: the order laws of `Int`, constructively

Lean's prelude proves the order laws of `Int` with `propext`, so the core cannot cite them. An
integer `a` is at most `b` where `b - a` is a natural number (`Int.NonNeg`), and `a < b` is
`a + 1 ≤ b`. Through the ring laws of `Becoming.Integers`, every order law the core's score
models use reduces to two facts about naturals read as integers: a sum of naturals is natural
(`nonneg_add`), and an integer or its negative is natural (`nonneg_or_neg`), with one step down
staying natural (`nonneg_pred_or`).

* **Order.** `le_refl`, `le_trans`, `le_antisymm`, `lt_irrefl`, `le_of_lt`, `lt_of_lt_of_le`,
  `lt_of_le_of_lt`, `lt_add_one`.
* **Comparison is decided by cases.** Either `a < b` or `b ≤ a` (`lt_or_le`), so `¬ a < b`
  gives `b ≤ a` (`le_of_not_lt`) and `b ≤ a` excludes `a < b` (`not_lt_of_le`), without any
  appeal to excluded middle.
* **Addition.** `add_le_add`, `add_le_add_left`, `add_le_add_right`, `le_of_add_le_add_left`,
  `le_of_add_le_add_right`, `add_lt_add_left`.
* **Differences.** `sub_nonneg_of_le`, `sub_le_sub_left`, `neg_nonpos_of_nonneg`,
  `le_add_of_nonneg_right`, `add_sub_cancel_right`, `sub_add_cancel`.

No premise; every declaration has an empty axiom report.
-/

namespace Becoming

namespace IntegerOrder

open Integers

/-! ## Natural integers -/

theorem nonneg_add : ∀ {x y : Int}, Int.NonNeg x → Int.NonNeg y → Int.NonNeg (x + y)
  | _, _, ⟨m⟩, ⟨n⟩ => ⟨m + n⟩

theorem nonneg_zero : Int.NonNeg 0 := ⟨0⟩

theorem nonneg_one : Int.NonNeg 1 := ⟨1⟩

/-- **An integer or its negative is natural.** -/
theorem nonneg_or_neg : ∀ x : Int, Int.NonNeg x ∨ Int.NonNeg (-x)
  | .ofNat _ => .inl ⟨_⟩
  | .negSucc n => .inr ⟨n + 1⟩

/-- **A natural integer is zero, or one less is natural.** -/
theorem nonneg_pred_or : ∀ x : Int, Int.NonNeg (-x) ∨ Int.NonNeg (x + -1)
  | .ofNat 0 => .inl ⟨0⟩
  | .ofNat (n + 1) => .inr (by
      show Int.NonNeg (Int.subNatNat (n + 1) 1)
      rw [Int.subNatNat_of_sub_eq_zero
        (show 1 - (n + 1) = 0 from (Nat.succ_sub_succ 0 n).trans (Nat.zero_sub n))]
      exact ⟨_⟩)
  | .negSucc n => .inl ⟨n + 1⟩

/-- An integer and its negative both natural: it is zero. -/
theorem eq_zero_of_nonneg_neg : ∀ {x : Int}, Int.NonNeg x → Int.NonNeg (-x) → x = 0
  | .ofNat 0, _, _ => rfl
  | .ofNat (_ + 1), _, neg => nomatch neg
  | .negSucc _, pos, _ => nomatch pos

theorem not_nonneg_neg_one : ¬ Int.NonNeg (-1) := fun h => nomatch h

/-! ## Differences -/

theorem le_iff {a b : Int} : a ≤ b ↔ Int.NonNeg (b + -a) := Iff.rfl

theorem lt_iff {a b : Int} : a < b ↔ a + 1 ≤ b := Iff.rfl

theorem sub_self (a : Int) : a + -a = 0 := add_right_neg a

/-- `(c + -b) + (b + -a) = c + -a`. -/
theorem sub_add_sub (a b c : Int) : c + -b + (b + -a) = c + -a := by
  rw [add_assoc, ← add_assoc (-b) b (-a), add_left_neg, zero_add]

/-- `(b + d) + -(a + c) = (b + -a) + (d + -c)`. -/
theorem sub_add_add (a b c d : Int) : b + d + -(a + c) = b + -a + (d + -c) := by
  rw [neg_add, add_add_add_comm]

/-- `(a + c) + -(a + b) = c + -b`. -/
theorem add_sub_add_left (a b c : Int) : a + c + -(a + b) = c + -b := by
  rw [neg_add, add_add_add_comm, add_right_neg, zero_add]

/-- `a + -b = -(b + -a)`. -/
theorem neg_sub (a b : Int) : a + -b = -(b + -a) := by
  rw [neg_add, neg_neg, add_comm]

/-- `b + -(a + 1) = (b + -a) + -1`. -/
theorem sub_succ (a b : Int) : b + -(a + 1) = b + -a + -1 := by
  rw [neg_add, add_assoc]

theorem add_sub_cancel_right (a b : Int) : a + b + -b = a := by
  rw [add_assoc, add_right_neg, add_zero]

theorem sub_add_cancel (a b : Int) : a + -b + b = a := by
  rw [add_assoc, add_left_neg, add_zero]

/-! ## Order -/

theorem le_refl (a : Int) : a ≤ a := by
  show Int.NonNeg (a + -a)
  rw [sub_self]
  exact nonneg_zero

theorem le_trans {a b c : Int} (ab : a ≤ b) (bc : b ≤ c) : a ≤ c := by
  show Int.NonNeg (c + -a)
  rw [← sub_add_sub a b c]
  exact nonneg_add bc ab

theorem le_antisymm {a b : Int} (ab : a ≤ b) (ba : b ≤ a) : a = b :=
  have back : Int.NonNeg (-(b + -a)) := by
    rw [← neg_sub a b]
    exact ba
  have zero : b + -a = 0 := eq_zero_of_nonneg_neg ab back
  (add_right_cancel (zero.trans (add_right_neg a).symm)).symm

theorem lt_irrefl (a : Int) : ¬ a < a := fun h => not_nonneg_neg_one (by
  have h' : Int.NonNeg (a + -(a + 1)) := h
  rw [sub_succ, add_right_neg, zero_add] at h'
  exact h')

theorem lt_add_one (a : Int) : a < a + 1 := le_refl (a + 1)

theorem le_of_lt {a b : Int} (h : a < b) : a ≤ b :=
  le_trans (show a ≤ a + 1 by
    show Int.NonNeg (a + 1 + -a)
    rw [add_comm, ← add_assoc, add_left_neg, zero_add]
    exact nonneg_one) h

theorem lt_of_lt_of_le {a b c : Int} (ab : a < b) (bc : b ≤ c) : a < c := le_trans ab bc

theorem lt_of_le_of_lt {a b c : Int} (ab : a ≤ b) (bc : b < c) : a < c :=
  le_trans (show a + 1 ≤ b + 1 by
    show Int.NonNeg (b + 1 + -(a + 1))
    rw [add_comm b 1, add_comm a 1, add_sub_add_left]
    exact ab) bc

/-- **Either `a < b` or `b ≤ a`.** -/
theorem lt_or_le (a b : Int) : a < b ∨ b ≤ a :=
  match nonneg_pred_or (b + -a) with
  | .inl down => .inr (by
      show Int.NonNeg (a + -b)
      rw [neg_sub a b]
      exact down)
  | .inr up => .inl (by
      show Int.NonNeg (b + -(a + 1))
      rw [sub_succ a b]
      exact up)

theorem le_of_not_lt {a b : Int} (h : ¬ a < b) : b ≤ a := (lt_or_le a b).resolve_left h

theorem not_lt_of_le {a b : Int} (h : b ≤ a) : ¬ a < b :=
  fun lt => lt_irrefl a (lt_of_lt_of_le lt h)

theorem le_total (a b : Int) : a ≤ b ∨ b ≤ a :=
  match lt_or_le a b with
  | .inl lt => .inl (le_of_lt lt)
  | .inr le => .inr le

/-! ## Addition -/

theorem add_le_add {a b c d : Int} (ab : a ≤ b) (cd : c ≤ d) : a + c ≤ b + d := by
  show Int.NonNeg (b + d + -(a + c))
  rw [sub_add_add a b c d]
  exact nonneg_add ab cd

theorem add_le_add_left {a b : Int} (ab : a ≤ b) (c : Int) : c + a ≤ c + b :=
  add_le_add (le_refl c) ab

theorem add_le_add_right {a b : Int} (ab : a ≤ b) (c : Int) : a + c ≤ b + c :=
  add_le_add ab (le_refl c)

theorem le_of_add_le_add_left {a b c : Int} (h : a + b ≤ a + c) : b ≤ c := by
  have h' : Int.NonNeg (a + c + -(a + b)) := h
  rw [add_sub_add_left] at h'
  exact h'

theorem le_of_add_le_add_right {a b c : Int} (h : a + c ≤ b + c) : a ≤ b := by
  rw [add_comm a c, add_comm b c] at h
  exact le_of_add_le_add_left h

theorem add_lt_add_left {a b : Int} (ab : a < b) (c : Int) : c + a < c + b := by
  show c + a + 1 ≤ c + b
  rw [add_assoc]
  exact add_le_add_left ab c

/-! ## Differences and signs -/

theorem sub_nonneg_of_le {a b : Int} (h : a ≤ b) : 0 ≤ b + -a := by
  show Int.NonNeg (b + -a + -0)
  rw [show (-0 : Int) = 0 from rfl, add_zero]
  exact h

theorem sub_le_sub_left {a b : Int} (h : a ≤ b) (c : Int) : c + -b ≤ c + -a := by
  show Int.NonNeg (c + -a + -(c + -b))
  rw [neg_add, neg_neg, add_add_add_comm, add_right_neg, zero_add, add_comm]
  exact h

theorem neg_nonpos_of_nonneg {e : Int} (h : 0 ≤ e) : -e ≤ 0 := by
  show Int.NonNeg (0 + -(-e))
  rw [zero_add, neg_neg]
  have h' : Int.NonNeg (e + -0) := h
  rw [show (-0 : Int) = 0 from rfl, add_zero] at h'
  exact h'

theorem le_add_of_nonneg_right {a e : Int} (h : 0 ≤ e) : a ≤ a + e := by
  have h' := add_le_add_left h a
  rw [add_zero] at h'
  exact h'

end IntegerOrder

end Becoming
