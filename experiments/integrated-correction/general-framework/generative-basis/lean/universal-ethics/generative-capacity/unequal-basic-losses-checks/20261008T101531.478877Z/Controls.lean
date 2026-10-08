import UnequalBasicLosses
open UnequalBasicLosses

-- Root's worked joint-loss comparison; not an additional theorem count.
example : CumulativeLT (2, 0) (1, 1) := by
  simp [CumulativeLT, CumulativeLE, total]
