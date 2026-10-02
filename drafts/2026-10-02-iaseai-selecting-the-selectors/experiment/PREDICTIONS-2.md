# Pre-specified predictions for the rubric-editing experiment, design 2

Written after the pilot (design 1, PREDICTIONS.md) and before any run of design 2.

## What the pilot showed

The pilot ran once (20 seeds). P2, P3 and P4 held. P1 failed: mean capacity rose in CLOSED
(0.500 -> 0.675) and fell in FIXED (0.471) and PUBLIC (0.417), but did not fall in REPLAY (0.531)
or FAST (0.503); every arm's 95% interval was about +/- 0.14. With one large lineage per capacity
level, the final composition was a winner-take-all among five lineages decided mostly by true-quality
differences (sd 0.02, comparable to the capacity cost) and drift. The pilot is reported as run.

## Design 2 (changes only)

- More lineages per capacity level: 20 large lineages at 0.04 (4 per level) and 40 small at 0.005
  (8 per level); fragmented start 100 lineages at 0.01.
- Conversion b = 0.04, so the size threshold s* = gamma delta / (a b chi) = 0.025: large lineages are
  above it, small ones below; FAST (delta = 0.5) puts s* at 0.25, above every initial share.
- True-quality spread sigma_theta = 0.01; 40 seeds; everything else as in the pilot.
- Decision rule: "rises" / "falls" means the 95% interval of the per-seed change in mean capacity
  (q_T - q_0) lies above / below zero.

## Predictions

P1 Mean capacity rises in CLOSED and falls in FIXED, REPLAY, PUBLIC and FAST.
P1b CLOSED ends with higher mean capacity than REPLAY, paired by seed (95% interval above zero).
P2 FRAGMENTED: mean capacity does not rise.
P3 A q = 1 lineage starting at 1% does not take over (mean final share < 0.5); starting at 25% it does
   (mean final share > 0.5).
P4 True quality at T is lower in CLOSED than in FIXED, paired by seed (95% interval below zero).

Any failure will be reported as failed, together with the pilot.
Fri Oct  2 21:49:40 +07 2026
