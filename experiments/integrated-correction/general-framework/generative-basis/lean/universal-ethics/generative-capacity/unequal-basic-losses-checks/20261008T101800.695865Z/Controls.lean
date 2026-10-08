import UnequalBasicLosses
open UnequalBasicLosses

-- Root's worked joint-loss comparison; not an additional theorem count.
example : CumulativeLT (2, 0) (1, 1) := by
  simp [CumulativeLT, CumulativeLE, total]

-- Joint comparison improving both total number and higher-tier count.
example : CumulativeLT (2, 0) (1, 2) := by
  simp [CumulativeLT, CumulativeLE, total]
