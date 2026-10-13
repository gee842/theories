def beyond : Nat → Nat → Bool
  | _, 0 => false
  | 0, _ + 1 => true
  | t + 1, s + 1 => beyond t s

example (n : Nat) : beyond (n + 1) 1 = false := rfl
example (n : Nat) : beyond (n + 1) (0 + 1) = beyond (n + 1) 0 := rfl

def beyond2 (t : Nat) : Nat → Bool
  | 0 => false
  | s + 1 => match t with
    | 0 => true
    | t + 1 => beyond2 t s

example (n : Nat) : beyond2 (n + 1) (0 + 1) = beyond2 (n + 1) 0 := rfl
theorem b2 : ∀ t s, ¬ s = t → beyond2 t (s + 1) = beyond2 t s
  | 0, 0, other => absurd rfl other
  | 0, _ + 1, _ => rfl
  | _ + 1, 0, _ => rfl
  | t + 1, s + 1, other => b2 t s (fun same => other (congrArg (· + 1) same))
#print axioms b2
