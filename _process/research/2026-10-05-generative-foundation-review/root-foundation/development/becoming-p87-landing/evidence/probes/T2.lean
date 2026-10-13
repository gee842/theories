def beyond2 (t : Nat) : Nat → Bool
  | 0 => false
  | s + 1 => match t with
    | 0 => true
    | t + 1 => beyond2 t s

example : beyond2 5 3 = false := rfl
example (n : Nat) : beyond2 n 0 = false := rfl
example (n : Nat) : beyond2 (n+1) (0+1) = false := rfl
example (n : Nat) : beyond2 (n+1) 1 = beyond2 n 0 := rfl
example (n : Nat) : beyond2 (n+1) (Nat.succ 0) = beyond2 n 0 := rfl

def beyond3 : Nat → Nat → Bool
  | 0, 0 => false
  | 0, _ + 1 => true
  | _ + 1, 0 => false
  | t + 1, s + 1 => beyond3 t s
example (n : Nat) : beyond3 (n+1) 0 = false := rfl
example (n : Nat) : beyond3 (n+1) 1 = false := rfl
example (n : Nat) : beyond3 n n = false := rfl
