import ChanceGrounding
open ChanceGrounding

-- Concrete diagnostic; not an additional theorem count.
example : refine (1, 1) = (3, 1) ∧ Improves (1, 1) (3, 1) := by
  unfold refine Improves scoreNumerator total
  decide
