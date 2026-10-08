import CrossedClaims
open CrossedClaims

-- Concrete coupled application; not an additional theorem count.
example : protectedTickets (transfer ⟨1, 1, 0⟩) .p = 1 ∧
    protectedTickets (transfer ⟨1, 1, 0⟩) .q = 2 ∧
    protectedTickets (transfer ⟨1, 1, 0⟩) .r = 1 := by decide
