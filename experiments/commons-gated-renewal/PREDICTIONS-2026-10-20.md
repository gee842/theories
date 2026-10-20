# Predictions for a commons with gated renewal, frozen 20 October 2026

Board item CG1. AI-written (a Claude Code session of 20 October 2026). Frozen before any learning run: this file, the environment ([`commons.py`](commons.py)), the learners and checks ([`learning.py`](learning.py)), the configurations ([`run.py`](run.py), `CONFIG`) and the verdict rules ([`analyze.py`](analyze.py)) are committed together, and the runs are made from that commit. Before the freeze only two things were run: the scripted calibration ([`calibrate.py`](calibrate.py), no learning; its output is [`results/calibration.json`](results/calibration.json)) and a smoke run of every code path with three training episodes, whose outputs were not kept or read beyond "it runs". Nothing below is changed after the runs; corrections, if any, go into the report as corrections, and failures stay.

## Why this test

The significance review SA1 ([BECOMING-SIGNIFICANCE-REVIEW](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md)) found that no correspondence of the theory to physics, ecology, economics or AI has been measured, and named as one test of a real contribution a prediction about an actual system that could fail and does not. A commons with gated renewal is close to an exact instance of four laws of the spine: balance, gated renewal and joint excess; the margin; selection through coupling and pools; and regulation read late. It is cheap to run and has prior results to compare against.

## The system, and how the laws' terms are read in it

**Environment.** Harvest in the style of Perolat et al. 2017: apples on the cells of 3×3 patches; each empty cell regrows with probability 0 / 0.01 / 0.05 / 0.1 when 0 / 1–2 / 3–4 / more apples stand within Euclidean distance 2 of it (their regrowth rule). Deliberate departures: agents do not walk and cannot tag; each step an agent harvests one apple from its patch or waits. Harvest comes first in a step, regrowth then reads what stands. Episodes are H = 100 steps from a full patch (9 apples). Patches are *isolated* when no cell of one lies within distance 2 of a cell of another (2 empty columns between them), *adjoining* when they do (1 empty column).

**The laws' terms.**

| Spine term | In the commons |
|---|---|
| condition `c`, its level | a patch, the number of apples standing on it |
| `taken`, `given` at a step | apples harvested, apples regrown |
| balance (`Flow.Balances`) | level after = level before − taken + given, in whole apples |
| gated, need `m` (`Flow.joint_excess_ends`, premise `gated`) | at an isolated patch nothing regrows unless at least one of its own apples stands: m = 1 |
| joint excess at a step | taken > given |
| the part, the withheld levels (`Flow.WithheldLevels`) | the harvesters; the level path with their takes withheld and regrowth as recorded, x₀ + Σ given |
| a formation's coupling; selection through it (`Web.SelectsThrough`) | what a learner's reward reads; the learner's training, which changes its policy only through returns |
| the coupling closure, the pool's closure | the patch a learner harvests and every learner harvesting it; the union over a group of learners |
| a rule reading ℓ late (`Regulation.ReadsLate`), the rest moving by at most d | an overseer whose move at t is fixed by the level up to t − ℓ and its own past moves; the rest's net move in −d..d |

**Bridge hypotheses** (not the theory's; each prediction says which it uses).

- **H1, training is selection through the reward's coupling.** A tabular Q-learner's policy depends on the courses it meets only through the rewards it receives: two courses that give it the same rewards are selected alike. This makes the learner an instance of `Web.SelectsThrough` with `obs` = what its reward reads.
- **H2, the learners come near the best return.** In these small tabular problems (2,020 state–action values per learner) Q-learning comes near a best response. The theory says nothing of this; where a prediction needs it, a failure may be H2's.

A learning prediction is *not testable* only where the learner learned nothing: its mean evaluation harvest is no better than harvesting at every step (10.45 apples, calibration). Otherwise it is passed or failed.

## Classes of prediction

- **Identity:** the law's conclusion follows in the environment from premises the environment is built to meet (balance, the gate, whole amounts). It can fail only if the identification fails (the environment does not meet them), so it tests the identification, not the dynamics. SA1's verdict that these laws are near-definitional applies; the test does not upgrade them.
- **Scope:** the law's conclusion is predicted to *fail* where a premise fails. This can fail informatively.
- **Law + H1 (+ H2):** a law read through the bridge. It can fail through the law's reading or the bridge.
- **Beyond the law:** stated to locate where the law's prediction sits; a failure is not the law's.

## Predictions

**(a) Joint excess** — `Flow.joint_excess_ends` (`Becoming/Continuation.lean`): with balance, givers needing the condition at m, n steps of joint excess from T starting below n + m leave the level below m from T + n on, nothing given again.

- **A1 (identity).** At every isolated patch, in every episode of every run (training and evaluation of C, D1, D2; the scripted rate runs; the scripted gap-2 runs), every window (T, n) with taken > given at each of the n steps from T and level at T below n + 1 is followed by level 0 and no regrowth at every step from T + n to the episode's end. Also no regrowth is ever recorded at a step whose level is 0, and balance holds at every step. **Pass:** zero violations of each, over a positive number of windows. **Fail:** any violation.
- **A2 (scope).** Where patches adjoin, the gate premise fails for a patch read alone (its neighbour reseeds it), and the law's conclusion should fail with it. A scripted harvester clears patch 0 (harvesting every step while an apple stands, for the first 30 steps) while patch 1 stands untouched, 100 runs of 300 steps. **Pass:** at gap 1 the layout couples the two patches, patch 0 read alone shows at least one joint-excess violation and at least one run in which it regrows after reaching 0, and the two patches read as one condition show none; at gap 2 the layout does not couple them and patch 0 read alone shows no violation and never regrows after 0. **Fail:** otherwise.

**(b) The margin** — `Flow.Balances.retains_iff_within_margin` (`Becoming/Retaining.lean`): the levels with a part admit a formation exactly when its need plus the part's cumulative take is at most the withheld level plus the part's cumulative give.

- **B1-margin (identity).** At every step of every logged episode at an isolated patch, renewal is admitted (level ≥ 1) exactly when 1 + Σ taken so far ≤ x₀ + Σ given so far. **Pass:** zero mismatches. **Fail:** any.
- **B2-rate (derived; identity class).** Which draw rates keep renewal admitted. With the gate, the margin and the exact maximum expected regrowth of a patch over all 512 configurations, R_max = 0.30 apples a step (calibration), a harvester asking with probability q at each step from a full patch satisfies q·E[τ] = 9 + E[given before τ] ≤ 9 + 0.30·E[τ] (Wald), so the mean collapse time is at most 9 / (q − 0.30): no constant draw rate above 0.30 keeps renewal admitted, and q = 0.5, 0.7, 1.0 collapse on average within 45, 22.5 and 12.86 steps. 1,000 runs each, horizon 5,000. **Pass:** each sample mean is at most its bound. **Not testable** for a q with any run censored (not collapsed) at 5,000 (none expected). Rates at or below 0.30: the law does not decide whether they keep renewal (that depends on the regrowth's realisation), and no prediction is made.

**(c) The selection gap** — `Flow.act_unselected`, `Flow.act_unselected_of_coupled` (`Becoming/SelectionGap.lean`), `Flow.unselected_beyond_coupling` (`Becoming/Selection.lean`): an act whose difference lies only beyond what the selecting formations couple into is selected alike with and without it.

Single learner at one patch, 20 seeds, 20,000 training episodes, 200 greedy evaluation episodes per seed. *Own*: reward = apples harvested. *Coupled*: reward = apples harvested + 2 × (level after the last step), a term coupled into the level beyond the episode's harvests. For the own learner the level after step H is read by no reward term: two courses differing only there are selected alike, and an apple taken at the last step is a gain within the coupling whose cost lies wholly beyond it.

- **C1 (law + H1 + H2).** At the last step, wherever an apple stands, the greedy own learner harvests in at least 95% of such decisions and the coupled learner in at most 5% (pooled). **Fail:** either side missed. This is a weak test of learning (the last step's reward is immediate); it checks that the gap's contrast shows where the theory places it.
- **C2 (law + H1 + H2).** The level left at the horizon: mean final level coupled − own ≥ 2.0 apples; the coupled learner leaves the patch alive (≥ 1) in at least 90% of evaluation episodes; the own learner leaves it dead (0) in at least 50%. The 50% is anchored on the calibration (the best scripted end rule, threshold 5 with harvesting whenever the steps left are at most the level, leaves it dead in 53%) and is the part most exposed to H2. **Fail:** any of the three missed.
- **C3 (beyond the law; H2).** The own learner's depletion sits at the horizon, where the coupling ends, not through the episode: its patch is alive at step H − 20 in at least 80% of evaluation episodes. Within the episode, early collapse costs its own later harvests, which its reward reads, so the gap law does not license early collapse; whether the learner avoids it is H2.
- **Not testable from the law: the tragedy among learners sharing a patch.** Where several own-reward learners harvest one patch, each one's harvest changes the level every other one's harvest reads, so every difference lies within each learner's coupling closure and the gap law is silent on whether they deplete it within the episode (Perolat et al.'s "tragedy" phase). Reported descriptively (D2's own3 condition), not as a test.

**(d) Pools** — `Flow.unselected_beyond_pool`, `Flow.uncoupled_beyond_pool`, `withinClosureOf_iff` (`Becoming/Selection.lean`): a part beyond a pool's coupling closure, the union of its members' closures, makes no difference to any selection through the pool.

- **D1 (law; identity class).** Two isolated patches A and B; learners 0 and 1 (own reward) at A, learner 2 at B. Changing only learner 2's reward (own vs coupled) leaves everything coupled into the A pool alike: learners 0 and 1's Q-tables after training, their evaluation harvests, and patch A's level path in the first 50 evaluation episodes are identical, bit for bit, in all 10 seeds; and the change does act at B (mean final level of B differs between the two conditions by at least 1 apple, pooled). **Fail:** any difference at A in any seed (coupling leaks), or no effect at B (the manipulation is idle).
- **D2a (law + H1 + H2).** Three learners share one patch. A coupled member reads the level after H, but it can change the level only through its own takes, and the own members' selection reads only their own harvests, so the pool's selection reaches the level after H only through the coupled members' withheld takes. Prediction: the coupled members do no more for the stock than their absence would: survival (final level ≥ 1) with 1 coupled + 2 own is at most survival with the 2 own learners alone + 0.10, and with 2 coupled + 1 own at most survival with the 1 own learner alone + 0.10. **Fail:** either exceeded.
- **D2b (law + H1 + H2).** Where every member with access is coupled, the pool's selection reaches the stock through every take: survival with 3 coupled ≥ 0.80, and at least 0.30 above survival with 2 coupled + 1 own. **Fail:** either missed.

20 seeds per condition, 30,000 training episodes; conditions own3, c1own2, c2own1, c3, own2, own1, c1.

**(e) Late reading** — `Regulation.no_narrower_band`, `Regulation.late_band`, `Regulation.lateReturn_band`, `Regulation.lateReturn_keeps` (`Becoming/Regulation.lean`): no rule reading ℓ steps late keeps the level within a band [a, b] with b − a < 2(ℓ + 1)d under every rest moving it by at most d a step; the late return keeps it within (ℓ + 1)d of its start.

One condition held away from the gate (start 30, 40 steps, rest's net move −1..1 so d = 1, overseer's −2..2), ℓ = 0, 1, 2, 3, 10 seeds. Overseers: the late return; a learned overseer (Q-learning on the level it reads ℓ late and its own last ℓ + 1 moves, trained 20,000 episodes against a uniformly random rest, rewarded for each step in the band). Rests: a learned adversary (Q-learning on the current offset and the step, rewarded for leaving the band, 5,000 episodes against the fixed overseer), 200 uniformly random rests, and the two constant rests (+1 and −1 every step). Bands: *narrow*, offsets [−(ℓ+1), ℓ] (b − a = 2(ℓ+1)d − 1); *wide*, [−(ℓ+1), ℓ+1] (b − a = 2(ℓ+1)d). This is not the commons' dynamics: it is the law's own setting with learned rules and rests, kept separate.

- **E1 (identity).** The late return keeps the wide band against every rest tried: zero exits (adversary, random, constant). **Fail:** any exit.
- **E2 (identity, any rule).** For every overseer, learned ones included, the courses under the two constant rests are at least 2(ℓ + 1)d apart. **Fail:** any pair closer.
- **E3 (law + H2: a learner realises the worst case).** In the narrow band, the learned adversary leaves the band against the late return and against the learned overseer in at least 9 of 10 seeds, for each ℓ. **Fail:** any (ℓ, overseer) cell below 9.
- Reported, no prediction: the exit rate of random rests (how far typical rests are from the worst case the law bounds).

## Prior work, and what is new here

- **Perolat et al. 2017** (NeurIPS, arXiv 1707.06600): 12 independent DQN learners in this regrowth rule show naivety, then a tragedy phase in which the stock collapses within each episode, then maturity in which tagging (exclusion) restores sustainability; they define efficiency, equality, sustainability (mean time of reward) and peace, and give no quantitative prediction beyond training-phase timings and Schelling-diagram equilibria.
- **Melting Pot** (Leibo et al. 2021, arXiv 2107.06857; Melting Pot 2.0, arXiv 2211.13746): the Commons Harvest substrates use the same kind of neighbour-gated regrowth and note that a patch whose apples are all taken is lost for good; results are reported as focal returns against background populations.
- **Reward coupled into others or the commons:** inequity aversion (Hughes et al. 2018, arXiv 1803.08884), prosocial reward exchange and the *self-interest level* of Markov social dilemmas (arXiv 2501.16138), the minimum reward exchange that aligns individual and collective interest. Time limits and horizon effects in RL are known (Pardo et al. 2018).

That a commons collapses under self-interested learners, and that coupling rewards into the commons helps, is known; this test does not claim either. What the laws add, and what is tested here: (1) **where** the depletion falls, at the end of the coupling (C2, C3), with the gap law saying which differences no learner can be selected against; (2) the **scope** of the joint-excess law, predicted to fail exactly where the gate is broken by an adjoining patch (A2); (3) a **rate bound** on collapse from the margin and the regrowth's exact maximum (B2-rate); (4) the **pool's reach**: a coupled member helps the stock only through its own withheld takes, never through the own members' selection, so survival needs every member with access coupled (D2a, D2b), a heterogeneous-population prediction the self-interest-level measure (one mixing level for all) does not make; and (5) the **least band** of an overseer reading ℓ steps late, 2(ℓ + 1)d, against learned adversaries (E3). The identity-class items (A1, B1-margin, B2-rate, D1, E1, E2) are reported as checks of the identification and are not counted as the theory's empirical support.

## Analysis

`python3 analyze.py` computes every verdict from `results/` by the rules above and writes `results/VERDICTS.json`. The report gives each verdict, the numbers behind it, and every failure with what it says: about the law's reading, about H1 or H2, or about the environment.
