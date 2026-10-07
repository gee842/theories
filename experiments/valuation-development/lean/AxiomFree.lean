/-
  Axiom-free arithmetic and list lemmas for the valuation-development modules.

  7 October 2026. Core Lean's own versions of these lemmas, and the `simp` and
  `omega` tactics, reach `propext` or `Quot.sound`. Ren's standing rule is that the
  generative model needs no axioms, so the valuation modules prove what they need
  here by structural induction. Every declaration in this file depends on no axiom.
-/

namespace ValuationDevelopment.AF

theorem mul_assoc : ∀ (a b c : Nat), a * b * c = a * (b * c)
  | a, b, 0 => rfl
  | a, b, c + 1 => by
    show a * b * c + a * b = a * (b * c + b)
    rw [Nat.left_distrib, mul_assoc a b c]

theorem mul_left_comm (a b c : Nat) : a * (b * c) = b * (a * c) := by
  rw [← mul_assoc, Nat.mul_comm a b, mul_assoc]

theorem add_sub_cancel : ∀ (n m : Nat), n + m - m = n
  | n, 0 => rfl
  | n, m + 1 => by
    show (n + m).succ - m.succ = n
    rw [Nat.succ_sub_succ]
    exact add_sub_cancel n m

theorem sub_add_cancel : ∀ {n m : Nat}, m ≤ n → n - m + m = n
  | n, 0, _ => rfl
  | 0, m + 1, h => absurd h (Nat.not_succ_le_zero m)
  | n + 1, m + 1, h => by
    rw [Nat.succ_sub_succ]
    show (n - m + m).succ = n.succ
    rw [sub_add_cancel (Nat.le_of_succ_le_succ h)]

theorem add_sub_of_le {a b : Nat} (h : a ≤ b) : a + (b - a) = b := by
  rw [Nat.add_comm]; exact sub_add_cancel h

theorem le_of_add_le_add_right : ∀ {a b c : Nat}, a + b ≤ c + b → a ≤ c
  | _, 0, _, h => h
  | _, _ + 1, _, h => le_of_add_le_add_right (Nat.le_of_succ_le_succ h)

theorem le_of_add_le_add_left {a b c : Nat} (h : a + b ≤ a + c) : b ≤ c := by
  rw [Nat.add_comm a b, Nat.add_comm a c] at h; exact le_of_add_le_add_right h

theorem le_sub_of_add_le {a b c : Nat} (h : a + b ≤ c) : a ≤ c - b := by
  have hb : b ≤ c := Nat.le_trans (Nat.le_add_left b a) h
  have : a + b ≤ c - b + b := by rw [sub_add_cancel hb]; exact h
  exact le_of_add_le_add_right this

theorem sub_le_of_le_add {a b c : Nat} (h : a ≤ b + c) : a - c ≤ b := by
  induction c generalizing a with
  | zero => exact h
  | succ c ih =>
    cases a with
    | zero => rw [Nat.zero_sub]; exact Nat.zero_le _
    | succ a =>
      rw [Nat.succ_sub_succ]
      exact ih (Nat.le_of_succ_le_succ h)

theorem mem_append {α : Type} {x : α} : ∀ {l m : List α}, x ∈ l ++ m → x ∈ l ∨ x ∈ m
  | [], _, h => Or.inr h
  | _ :: _, _, .head _ => Or.inl (.head _)
  | _ :: l, _, .tail _ h => match mem_append h with
    | .inl h' => Or.inl (.tail _ h')
    | .inr h' => Or.inr h'

theorem mem_append_left {α : Type} {x : α} : ∀ {l : List α} (m : List α), x ∈ l → x ∈ l ++ m
  | _ :: _, _, .head _ => .head _
  | _ :: _, m, .tail _ h => .tail _ (mem_append_left m h)

theorem mem_append_right {α : Type} {x : α} : ∀ (l : List α) {m : List α}, x ∈ m → x ∈ l ++ m
  | [], _, h => h
  | _ :: l, _, h => .tail _ (mem_append_right l h)

theorem mem_map {α β : Type} {f : α → β} {y : β} : ∀ {l : List α}, y ∈ l.map f → ∃ x, x ∈ l ∧ f x = y
  | [], h => nomatch h
  | x :: _, .head _ => ⟨x, .head _, rfl⟩
  | _ :: _, .tail _ h => match mem_map h with
    | ⟨x, hx, e⟩ => ⟨x, .tail _ hx, e⟩

theorem mem_singleton {α : Type} {x y : α} : x ∈ [y] → x = y
  | .head _ => rfl

theorem not_mem_nil {α : Type} {x : α} : ¬ x ∈ ([] : List α) := fun h => nomatch h

theorem map_append {α β : Type} (f : α → β) : ∀ (l m : List α), (l ++ m).map f = l.map f ++ m.map f
  | [], _ => rfl
  | x :: l, m => by show f x :: (l ++ m).map f = f x :: (l.map f ++ m.map f); rw [map_append f l m]

theorem sum_append : ∀ (l m : List Nat), (l ++ m).sum = l.sum + m.sum
  | [], m => (Nat.zero_add _).symm
  | x :: l, m => by
    show x + (l ++ m).sum = x + l.sum + m.sum
    rw [sum_append l m, Nat.add_assoc]

/-- Boolean disjunction is true exactly when one side is. -/
theorem or_true_cases : ∀ {a b : Bool}, (a || b) = true → a = true ∨ b = true
  | true, _, _ => Or.inl rfl
  | false, true, _ => Or.inr rfl

theorem or_false_cases : ∀ {a b : Bool}, (a || b) = false → a = false ∧ b = false
  | false, false, _ => ⟨rfl, rfl⟩

theorem decide_true {p : Prop} [Decidable p] (h : decide p = true) : p := of_decide_eq_true h
theorem decide_false {p : Prop} [Decidable p] (h : decide p = false) : ¬ p := of_decide_eq_false h

end ValuationDevelopment.AF
