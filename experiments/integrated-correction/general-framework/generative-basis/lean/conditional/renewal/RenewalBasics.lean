/-!
# Axiom-free facts about lists and natural numbers

Ren's rule of 6 October 2026 asks for no axioms. Lean's `omega` and `simp`, and
several core lemmas about list membership, appending and truncated subtraction,
depend on the standard axioms `propext` and `Quot.sound`. The renewal proofs use
the facts below instead. Each is proved by induction, case analysis on
constructors and axiom-free core lemmas, so each has an empty axiom report.
-/

namespace Generative.Conditional.Renewal

universe u

variable {α : Type u}

/-! ## Lists -/

theorem mem_cons_split {a b : α} {l : List α} (member : a ∈ b :: l) : a = b ∨ a ∈ l := by
  cases member with
  | head => exact Or.inl rfl
  | tail _ inside => exact Or.inr inside

theorem mem_singleton_eq {a b : α} (member : a ∈ [b]) : a = b := by
  cases member with
  | head => rfl
  | tail _ inside => cases inside

theorem mem_append_split {a : α} : ∀ {l₁ l₂ : List α}, a ∈ l₁ ++ l₂ → a ∈ l₁ ∨ a ∈ l₂
  | [], _, member => Or.inr member
  | b :: l₁, l₂, member => by
    cases mem_cons_split member with
    | inl same =>
      rw [same]
      exact Or.inl List.mem_cons_self
    | inr inside =>
      cases mem_append_split inside with
      | inl here => exact Or.inl (List.mem_cons_of_mem _ here)
      | inr there => exact Or.inr there

theorem append_nil_eq : ∀ l : List α, l ++ [] = l
  | [] => rfl
  | a :: l => by rw [List.cons_append, append_nil_eq l]

theorem append_assoc_eq : ∀ l₁ l₂ l₃ : List α, l₁ ++ l₂ ++ l₃ = l₁ ++ (l₂ ++ l₃)
  | [], _, _ => rfl
  | a :: l₁, l₂, l₃ => by
    rw [List.cons_append, List.cons_append, List.cons_append, append_assoc_eq l₁ l₂ l₃]

theorem length_append_eq : ∀ l₁ l₂ : List α, (l₁ ++ l₂).length = l₁.length + l₂.length
  | [], l₂ => (Nat.zero_add _).symm
  | a :: l₁, l₂ => by
    rw [List.cons_append, List.length_cons, List.length_cons, length_append_eq l₁ l₂,
      Nat.add_right_comm]

theorem eq_of_mem_replicate_eq {a b : α} : ∀ {m : Nat}, a ∈ List.replicate m b → a = b
  | 0, member => by cases member
  | m + 1, member => by
    have member' : a ∈ b :: List.replicate m b := member
    cases mem_cons_split member' with
    | inl same => exact same
    | inr inside => exact eq_of_mem_replicate_eq inside

/-! ## Natural numbers -/

theorem succ_ne_zero_of (n : Nat) : n + 1 ≠ 0 := fun same => Nat.noConfusion same

theorem add_right_cancel_eq {n m : Nat} : ∀ {k : Nat}, n + k = m + k → n = m
  | 0, same => same
  | _ + 1, same => add_right_cancel_eq (Nat.succ.inj same)

theorem add_left_cancel_eq {n m k : Nat} (same : k + n = k + m) : n = m := by
  rw [Nat.add_comm k n, Nat.add_comm k m] at same
  exact add_right_cancel_eq same

theorem le_of_add_le_add_right_of {n m : Nat} : ∀ {k : Nat}, n + k ≤ m + k → n ≤ m
  | 0, le => le
  | _ + 1, le => le_of_add_le_add_right_of (Nat.le_of_succ_le_succ le)

theorem le_of_add_le_add_left_of {n m k : Nat} (le : k + n ≤ k + m) : n ≤ m := by
  rw [Nat.add_comm k n, Nat.add_comm k m] at le
  exact le_of_add_le_add_right_of le

theorem add_mul_eq (a b c : Nat) : (a + b) * c = a * c + b * c := by
  rw [Nat.mul_comm, Nat.mul_add, Nat.mul_comm c a, Nat.mul_comm c b]

theorem mul_assoc_eq (a b : Nat) : ∀ c : Nat, a * b * c = a * (b * c)
  | 0 => rfl
  | c + 1 => by rw [Nat.mul_succ, Nat.mul_succ, Nat.mul_add, mul_assoc_eq a b c]

theorem add_sub_cancel_eq (n : Nat) : ∀ m : Nat, n + m - m = n
  | 0 => rfl
  | m + 1 => by
    show (n + m).succ - m.succ = n
    rw [Nat.succ_sub_succ]
    exact add_sub_cancel_eq n m

theorem add_sub_cancel_left_eq (n m : Nat) : n + m - n = m := by
  rw [Nat.add_comm]
  exact add_sub_cancel_eq m n

theorem sub_add_cancel_of_le {n m : Nat} (le : m ≤ n) : n - m + m = n := by
  obtain ⟨k, sum⟩ := Nat.le.dest le
  rw [← sum, Nat.add_comm m k, add_sub_cancel_eq]

theorem add_sub_of_le_eq {n m : Nat} (le : m ≤ n) : m + (n - m) = n := by
  rw [Nat.add_comm]
  exact sub_add_cancel_of_le le

theorem le_sub_of_add_le_of {n m k : Nat} (le : m + k ≤ n) : k ≤ n - m := by
  obtain ⟨j, sum⟩ := Nat.le.dest le
  rw [← sum, Nat.add_assoc, add_sub_cancel_left_eq]
  exact Nat.le_add_right k j

theorem sub_eq_zero_of_le_of : ∀ {n m : Nat}, n ≤ m → n - m = 0
  | 0, m, _ => Nat.zero_sub m
  | n + 1, 0, le => absurd le (Nat.not_succ_le_zero n)
  | _ + 1, _ + 1, le => by
    rw [Nat.succ_sub_succ]
    exact sub_eq_zero_of_le_of (Nat.le_of_succ_le_succ le)

theorem sub_le_of_le_add_of {n m k : Nat} (le : n ≤ m + k) : n - m ≤ k := by
  by_cases small : n ≤ m
  · rw [sub_eq_zero_of_le_of small]
    exact Nat.zero_le k
  · have back := sub_add_cancel_of_le (Nat.le_of_lt (Nat.gt_of_not_le small))
    rw [← back, Nat.add_comm (n - m) m] at le
    exact le_of_add_le_add_left_of le

theorem add_le_of_le_sub_of {n m k : Nat} (within : m ≤ n) (le : k ≤ n - m) : m + k ≤ n := by
  have sum := Nat.add_le_add_left le m
  rw [add_sub_of_le_eq within] at sum
  exact sum

theorem min_eq_left_of_le {a b : Nat} (le : a ≤ b) : min a b = a := by
  show (if a ≤ b then a else b) = a
  rw [if_pos le]

theorem min_eq_right_of_le {a b : Nat} (le : b ≤ a) : min a b = b := by
  show (if a ≤ b then a else b) = b
  by_cases ab : a ≤ b
  · rw [if_pos ab]
    exact Nat.le_antisymm ab le
  · rw [if_neg ab]

theorem le_min_of {a b c : Nat} (left : c ≤ a) (right : c ≤ b) : c ≤ min a b := by
  show c ≤ if a ≤ b then a else b
  by_cases ab : a ≤ b
  · rw [if_pos ab]
    exact left
  · rw [if_neg ab]
    exact right

theorem min_le_left_of (a b : Nat) : min a b ≤ a := by
  show (if a ≤ b then a else b) ≤ a
  by_cases ab : a ≤ b
  · rw [if_pos ab]
    exact Nat.le_refl a
  · rw [if_neg ab]
    exact Nat.le_of_lt (Nat.gt_of_not_le ab)

theorem min_le_right_of (a b : Nat) : min a b ≤ b := by
  show (if a ≤ b then a else b) ≤ b
  by_cases ab : a ≤ b
  · rw [if_pos ab]
    exact ab
  · rw [if_neg ab]
    exact Nat.le_refl b

theorem min_zero_eq (a : Nat) : min a 0 = 0 := min_eq_right_of_le (Nat.zero_le a)

/-- Two bounds added: a common pattern in place of `omega`. -/
theorem add_le_add_of {a b c d : Nat} (left : a ≤ c) (right : b ≤ d) : a + b ≤ c + d :=
  Nat.add_le_add left right

theorem le_of_add_le_left_of {a b c : Nat} (le : a + b ≤ c) : b ≤ c :=
  Nat.le_trans (Nat.le_add_left b a) le

theorem le_of_add_le_right_of {a b c : Nat} (le : a + b ≤ c) : a ≤ c :=
  Nat.le_trans (Nat.le_add_right a b) le

theorem lt_of_add_one_le_of {a b : Nat} (le : a + 1 ≤ b) : a < b := le

theorem add_one_le_of_lt_of {a b : Nat} (lt : a < b) : a + 1 ≤ b := lt

theorem pos_of_ne_zero_of {a : Nat} (nonzero : a ≠ 0) : 0 < a := by
  cases a with
  | zero => exact False.elim (nonzero rfl)
  | succ a => exact Nat.zero_lt_succ a

theorem eq_zero_or_pos_of (a : Nat) : a = 0 ∨ 0 < a := by
  cases a with
  | zero => exact Or.inl rfl
  | succ a => exact Or.inr (Nat.zero_lt_succ a)

#print axioms mem_cons_split
#print axioms mem_singleton_eq
#print axioms mem_append_split
#print axioms append_nil_eq
#print axioms append_assoc_eq
#print axioms length_append_eq
#print axioms eq_of_mem_replicate_eq
#print axioms succ_ne_zero_of
#print axioms add_right_cancel_eq
#print axioms add_left_cancel_eq
#print axioms le_of_add_le_add_right_of
#print axioms le_of_add_le_add_left_of
#print axioms add_mul_eq
#print axioms mul_assoc_eq
#print axioms add_sub_cancel_eq
#print axioms add_sub_cancel_left_eq
#print axioms sub_add_cancel_of_le
#print axioms add_sub_of_le_eq
#print axioms le_sub_of_add_le_of
#print axioms sub_eq_zero_of_le_of
#print axioms sub_le_of_le_add_of
#print axioms add_le_of_le_sub_of
#print axioms min_eq_left_of_le
#print axioms min_eq_right_of_le
#print axioms le_min_of
#print axioms min_le_left_of
#print axioms min_le_right_of
#print axioms min_zero_eq
#print axioms add_le_add_of
#print axioms le_of_add_le_left_of
#print axioms le_of_add_le_right_of
#print axioms lt_of_add_one_le_of
#print axioms add_one_le_of_lt_of
#print axioms pos_of_ne_zero_of
#print axioms eq_zero_or_pos_of

end Generative.Conditional.Renewal
