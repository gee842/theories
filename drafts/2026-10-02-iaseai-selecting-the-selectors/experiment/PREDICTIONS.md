# Pre-specified predictions for the rubric-editing experiment

Written before any run of experiment.py. Timestamp below is from `date` at writing.

Setting: lineages with heritable capacity q in {0, .25, .5, .75, 1} edit an evaluation rubric.
A fraction chi of each lineage's editing effort (q times its own share) raises the weight on its own
distinctive feature; the rest raises a generic weight that all lineages share. Weights decay at rate delta.
Fitness = true quality + own feature weight - gamma q. Analytic size threshold s* = gamma delta / (a b chi).
Baseline parameters put s* near 0.1 at chi = 0.8.

P1 (control channel). Mean capacity at T rises above its initial value only in the closed-loop
appropriable arm (concentrated start). It falls in FIXED (rules frozen), REPLAY (rule changes from an
independent run, assigned at random within size class), CLOSED-PUBLIC (chi = 0) and FAST-CORRECTION
(delta = 0.5).

P2 (concentration precondition). In the closed-loop appropriable arm, a fragmented start (all lineages
below s*) does not raise mean capacity.

P3 (invasion barrier). A q = 1 lineage starting at 1% does not take over a q = 0 population; the same
lineage starting at 25% does.

P4 (success without contribution). In the closed-loop appropriable arm, the share-weighted true quality
at T is lower than in FIXED, because rubric capture lets lower-quality, higher-capacity lineages win.

Any prediction that fails will be reported as failed.
Fri Oct  2 21:47:25 +07 2026
