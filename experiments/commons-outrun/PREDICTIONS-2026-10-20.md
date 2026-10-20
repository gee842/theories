# Predictions for CG2: what decides the outcome learners reach on a gated renewal, frozen 20 October 2026

Board item CG2 (line B toward the 20 October aim). AI-written (a Claude Code session of 20 October 2026). Frozen before any learning run: this file, the conditions ([`conditions.py`](conditions.py)), the exact calibration ([`calibrate.py`](calibrate.py), output [`results/calibration.json`](results/calibration.json)), the learners and identity checks ([`learners.py`](learners.py)), the configuration ([`run.py`](run.py), `CONFIG`) and the verdict rules ([`analyze.py`](analyze.py)) are committed together, and the runs are made from that commit. The environment is CG1's ([`commons.py`](../commons-gated-renewal/commons.py), unchanged) and its checks ([`learning.py`](../commons-gated-renewal/learning.py) `Checks`, unchanged).

Run before the freeze: the calibration (exact dynamic programmes and scripted harvesters, no learning); a smoke run of every code path (30 episodes, outputs read only as "it runs"); and a code-path test of the analysis on 200 training episodes, 2 seeds per condition, 5 evaluation episodes, kept nowhere. Its learners were untrained (200 episodes, against 30,000 here) and its numbers were not used to choose anything below: the conditions, classes, thresholds and predicted outcomes were fixed from the calibration before it ran.

## Why this test

CG1 (study §240) found that three learners, each rewarded its own apples plus twice the level left after the last step, emptied a gated patch in every episode (D2b, both rounds): coupling every member into the stock is necessary, not sufficient. The [significance review's check](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md#restraint-equilibrium-check) found the equilibrium theorem known in form (pivotality at a threshold, Palfrey and Rosenthal 1984; coordination at a known threshold, Barrett 2013; the folk theorem for stochastic games, Dutta 1995; risk-dominant selection under learning, Kandori, Mailath and Rob 1993) and located what the theory's ingredients add: a condition on the *rest*.

## The law, and the condition it gives

`Becoming.Exclusion` (four theorems added for this test; scratch-built with every axiom report empty, landing through the queue):

- `Flow.outrun_excess`: where a part (the rest) takes from a condition jointly more than a step gives to it, the joint taking exceeds what is given, whatever any formation outside the part takes.
- `Flow.outrun_below`, `Flow.outrun_ends`: where renewal depends on what it renews (the gate, need `m`), `n` such steps from a level below `n + m` leave the level below `m` from `T + n` on and end every dependent, whatever a member outside the part takes.
- `Flow.outrun_reading_alike`: with need one, in two flows in which the rest outruns from a level at most `n`, every score reading the condition only from `T + n` on scores them alike, however the member's act differs.

With `Flow.act_unselected` (an act whose difference lies beyond what a selection reads is not selected), `Flow.level_kept` (taking jointly within what is given keeps the level) and `Regulation.accumulates_at` (an emptied course takes its start plus everything given), these give one condition:

> **Depletion is locked exactly where the rest outruns the renewal before the member's reading.** Where the other members, harvesting at every step, end the condition before the step the member's reward reads, the member's restraint changes nothing its reward reads except its own apples, so harvesting at every step is a best response, for every weight of that reading. Where they cannot, the member's restraint keeps the level its reading sees, and harvesting at every step is not a best response once the kept level outweighs the apples.

**Calibration (exact, before the freeze).** The laws above are about single courses; the environment is stochastic. Whether the condition holds in each setting is therefore computed exactly, by a dynamic programme over all 512 configurations of the patch and the 100 steps, for one member against a rest that harvests at every step, under the environment's exact dynamics. `gain` is how much the member's best response beats harvesting at every step. A setting is *locked* where `gain < 0.25` (harvesting at every step is a mutual best response, up to that tolerance) and *open* where `gain ≥ 1.0`; no frozen condition falls between. Scripted always-harvesters (400 runs) give the rest's reach: at regrowth scale `s` = 1, one harvester empties the patch in 10.5 steps on average; at `s` = 8, one never does by step 100 in 99% of runs and two always do (13 steps); at `s` = 16, two never do in 99.5% and three do in 99% (24 steps).

| Condition | k | s | Reading | Rest of k − 1 at full draw | gain | Class | Predicted |
|---|---|---|---|---|---|---|---|
| `k3s1` (CG1's D2b c3) | 3 | 1 | 2 × level after the last step | empties (5 steps) | 0.000 | locked | depleted |
| `k3s1_lam32` | 3 | 1 | 32 × level after the last step | empties | 0.000 | locked | depleted |
| `k2s1` | 2 | 1 | 2 × last level | empties (10.5 steps) | 0.000 | locked | depleted |
| `k3s8` | 3 | 8 | 2 × last level | empties (13 steps) | 0.001 | locked | depleted |
| `k2s8` | 2 | 8 | 2 × last level | does not empty (99%) | 53.4 | open | kept |
| `k3s16` | 3 | 16 | 2 × last level | does not empty (99.5%) | 73.3 | open | kept |
| `k3s1_vlo` | 3 | 1 | 0.107 × level after each step (v*/2) | empties | 0.000 | locked | depleted |
| `k3s1_vhi` | 3 | 1 | 0.64 × level after each step (3 v*) | empties | 2.44 | open | kept |
| `k3s1_share` | 3 | 1 | the step's apples / 3 (full sharing), no level reading | empties | 0.084 | locked | depleted |
| `k3s8_share` | 3 | 8 | the step's apples / 3, no level reading | empties | 3.85 | open | kept |
| `k3s1_joint` | one learner choosing 0-3 requests | 1 | all apples + 3 × 2 × last level | no rest | 61.2 | open | kept |

`v*` = 0.2134 (calibration: harvesting at every step is a best response against such a rest for every per-step weight below it, and not above). The per-step reading is read *before* the rest's end, so the member's restraint is visible to it; whether it is selected then depends on the weight, which is what the pair `vlo`/`vhi` tests. Under full sharing the member's restraint changes what everyone takes only through what is given while the patch lives longer (`Regulation.accumulates_at`), small at `s` = 1 and large at `s` = 8.

## Bridges (not the theory's; each prediction uses both)

- **H1, training is selection through the reward's coupling** (CG1's H1): a tabular Q-learner's policy changes only through the rewards it receives.
- **H3, learners do not leave a locked profile and do not stay in an open one.** Where harvesting at every step is a best response against a rest that does so, and the rest's exploration also empties the patch before the reading in almost every training episode, the coupling term is unselected in those episodes (the gap read on the rest), and learners settle on depletion even where restraint is also an equilibrium. Where it is not a best response, the coupling term is selected whenever the rest harvests, and learners leave depletion. H3 is where the theory's selection-blindness reading goes beyond equilibrium existence: it says which of several equilibria is reached. It is also where the prediction can fail without the law failing.

## Predictions

**Training and evaluation** (CG1's round 2, unchanged): independent tabular Q-learners, state = (level, steps left), undiscounted, α = 0.1, ε from 1 to 0.02 over the first 80% of 30,000 training episodes, exploring starts (random step, random apples), H = 100; 20 seeds per condition; 200 greedy evaluation episodes from a full patch on fresh regrowth streams. **Measure:** the share of evaluation episodes in which the patch still stands (level ≥ 1) at step H − 20, averaged over seeds. Step H − 20 rather than H because own-apple and per-step readings legitimately empty the patch in the last few steps (the gap at the end of the coupling, CG1's C1); the level at H is reported beside it.

**Per condition.** *Kept:* passed if the measure is at least 0.80. *Depleted:* passed if it is at most 0.20. Otherwise failed. Every condition gets a verdict; none is "not testable".

**Contrasts** (each passes only if all its conditions pass):

- **X1, the boundary is the rest, not the whole:** `k2s1` depleted, `k2s8` kept, `k3s8` depleted, `k3s16` kept. In `k2s8` and `k3s16` the whole at full draw empties the patch and the rest does not; in `k3s8` the rest does. *A "whole capacity" account* (kept where all k at full draw cannot empty it) predicts `k2s8` and `k3s16` depleted. *A "more members, more tragedy" account* predicts a monotone fall in k at fixed s, which X1 shares only at s = 8 and does not locate.
- **X2, no weight of an end reading opens the lock:** `k3s1` and `k3s1_lam32` depleted. *A weight account* (a large enough coupling weight makes restraint chosen) predicts `k3s1_lam32` kept.
- **X3, a reading before the rest's end opens the lock only above v\*:** `k3s1_vlo` depleted, `k3s1_vhi` kept.
- **X4, sharing opens the lock only where renewal lets something through:** `k3s1_share` depleted, `k3s8_share` kept. *A sharing-level account* (full sharing, s = 1/n, makes cooperating preferred, Willis et al. 2025) predicts both kept.
- **X5, one selector reading the union:** `k3s1_joint` kept (no rest outside the selector, so nothing it reads is fixed against its act).

**Identity checks** (follow from premises the environment is built to meet; they test the identification, not the dynamics):

- **I1** `Flow.outrun_below` with need 1: in every evaluation episode from a full patch, for every member, every window (T, n) in which the other members' apples exceed the regrowth at each of the n steps from T and the level at T is at most n is followed by level 0 at every step from T + n to the end. Pass: zero violations over a positive number of windows.
- **I2** `Regulation.accumulates_at` on an emptied course: in every evaluation episode whose level after the last step is 0, the apples taken equal the 9 at the start plus the apples regrown. Pass: zero violations over a positive number of episodes.
- **I3** CG1's checks (balance, the gate, the margin, joint excess) on every training and evaluation episode. Pass: zero violations, positive joint-excess windows.

## What would change the account

- X1 failing at `k2s8` or `k3s16` (depleted where the rest cannot outrun): the boundary is not the rest's draw for learners; either H3 fails (learners reach depletion even where it is not an equilibrium, a learning failure as in CG1's C2) or a whole-capacity account describes learners better. The per-seed spread will say which.
- X1 failing at `k3s8` or X2 failing (kept where locked): learners reach restraint where depletion is also an equilibrium, so the selection-blindness reading of H3 does not decide equilibrium selection, and the theory's claim reduces to equilibrium existence.
- X3 or X4 failing on the open side: the gain is real but too small or too late in training to be selected; on the locked side: something besides the gain decides.
- Any identity check failing: the identification of the laws' terms is wrong in this environment.

## Limits stated in advance

The environment is CG1's (no walking or tagging; one isolated patch). The regrowth scale is a manipulation, not a feature of Perolat et al.'s game. Learners are tabular Q with CG1's training; their failures to reach a best response (CG1's H2) bound what any learning prediction can say. The calibration's best responses are over policies reading the whole configuration; learners read only the level and the steps left, so a gain computed exactly may be smaller for them (it is never larger). The thresholds 0.80 and 0.20 and the classes' tolerances 0.25 and 1.0 were set before any learning run and are not tuned.
