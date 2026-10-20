# Predictions for CG3: whether a stepwise learner's own later acts outrun what it reads, frozen 20 October 2026

Board item CG3. AI-written (a Claude Code session of 20 October 2026, started from CG2's line). Frozen before any learning run. The commit holds this file, the conditions ([`conditions.py`](conditions.py)), the exact computation ([`exact.py`](exact.py), output [`results/exact.json`](results/exact.json)), the learner ([`own.py`](own.py)), the configuration ([`run.py`](run.py), `CONFIG`, CG2's own) and the verdict rules ([`analyze.py`](analyze.py)), and the runs are made from it. CG2's code ([`../commons-outrun`](../commons-outrun/README.md): `calibrate.py`, `learners.Q`) and CG1's environment and checks ([`commons.py`](../commons-gated-renewal/commons.py), `learning.Checks`) are imported unchanged.

Run before the freeze: the exact computation (dynamic programmes, no learning); a smoke run of every code path (30 episodes, read only as "it runs"); and a code-path test of the analysis (50 training episodes, 2 seeds, 3 evaluation episodes, written to a scratch directory and kept nowhere). Its learners were untrained and its numbers chose nothing below. The conditions, the account's quantity, its thresholds and the predicted outcomes were fixed from the exact computation and from CG2's two published outcomes before that test ran.

## Why this test

CG2's contrast X5 failed. One tabular learner chose how many of three requests to make on a gated 3×3 patch, rewarded with all the apples plus 6 × the level after the last step. It emptied the patch in every episode of every seed, though the exact optimum keeps the patch (gain 61). The post hoc reading ([CG2 README](../commons-outrun/README.md), [results/posthoc-joint.txt](../commons-outrun/results/posthoc-joint.txt), study §250) was that the outrunning rest can be one's own later acts: where the learner's own later greedy steps (3 apples a step) empty the patch before the end reading, its restraint now changes nothing the end reading sees (`Flow.outrun_reading_alike` read across time).

## What the exact computation already settles (not a prediction)

[`exact.py`](exact.py) runs policy iteration on the patch's 512 configurations and 100 steps, starting from the full draw, which is the policy a learner whose immediate apples are learned first holds early. Each sweep evaluates the current policy exactly and takes the greedy policy against it, so the value of restraint at every step is read through the selector's own later acts as they stand. The hypothesis in its exact form says the end reading's value reaches a state only where the selector's own later policy does not end the condition before the reading. It predicts many sweeps, each moving the reach of restraint back by about the full draw's emptying time (3.3 steps at three requests).

**Result: one sweep keeps the patch in every condition below** (`n_keep` = 1: the policy after one sweep leaves the patch standing at step 80 with probability 1.00), **with or without an end reading** (`J3w0`, `J1w0`: w = 0, optimum still keeps, gain 20.7 and 18.9). Two reasons:

1. The step's apples are themselves a reading of the renewal. Against a later full draw, an apple left standing now is still taken later, and while it stands it lets the empty cells around it regrow, so withholding now gains the regrowth and loses nothing that the later draw does not collect. So against the selector's own later full draw, restraint is already an improvement at every step but the last few (`Regulation.accumulates_at`: an emptied course takes its start plus everything given, and leaving apples standing raises what is given).
2. A single selector's later acts are not a rest held fixed. They are improved in the same sweep (the policy improvement theorem).

Across members (CG2) the rest is fixed and depletion can be an equilibrium (X1–X2 held). Across time, one selector's later acts give no lock and no delay of the exact improvement. **So the post hoc reading is false in its exact form.** `Flow.outrun_reading_alike` does not transfer to one's own later acts under exact improvement, because those acts are themselves revised.

What remains to explain is a fact about sampled learning, not about values: why a tabular TD learner with ε-greedy exploration fails at what one exact sweep finds.

## The account under test, and its quantity

**Own-draw coverage (the across-time reading, sampled form).** A TD learner's values are made from the courses its own acts produce. Early in training those acts are nearly uniform over 0..m requests. Where they end the condition within a few steps, the states in which restraint pays (a standing patch, many steps left) are reached almost only at exploring starts, and their values stay unlearned. This is `Flow.joint_excess_ends` with the part being the learner's own exploratory takes. **Quantity:** `cov`, the exact expected number of steps (of 100) the patch stands from a full patch when the requests are drawn uniformly from 0..m at every step. Anchors from CG2's published outcomes: CG2's joint learner has `cov` 6.0 and was depleted (0/20 seeds); CG2's post hoc control (one coupled learner, m = 1, own apple + 2 × end level) has `cov` 23.7 and kept the patch (3/3 seeds). **Rule:** predicted kept where `cov ≥ 20`, depleted where `cov ≤ 7`, and only an order between. For optimistic initial values (`J3opt`) the early greedy acts withhold, so the account predicts kept whatever `cov` is.

This account is known in form (see [the significance review's check](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md#own-later-acts-check)): dithering exploration needs time exponential in the length of the consistent course that reaches the value (Osband et al. 2019), exploration fails where the system can be broken before it has been explored (Moldovan and Abbeel 2012), and zero-initialised Q-learning is intractable where optimistic initialisation is tractable (Koenig and Simmons 1996). What is tested is whether its exact quantity, the own draw against the renewal, ranks the outcomes where named alternatives rank them otherwise.

| Condition | m | s | Reading | `cov` | full draw empties in | optimum | gain | P(opt alive at 80) | sweeps to keep | Predicted |
|---|---|---|---|---|---|---|---|---|---|---|
| `J3` (CG2's `k3s1_joint`, new seeds) | 3 | 1 | apples + 6 × last level | 6.0 | 3.3 | 70.6 | 61.2 | 1.00 | 1 | depleted |
| `J2` | 2 | 1 | apples + 6 × last level | 9.7 | 5.1 | 70.6 | 60.9 | 1.00 | 1 | between: J3 ≤ J2 ≤ J1 |
| `J1` | 1 | 1 | apples + 6 × last level | 23.7 | 10.5 | 70.4 | 60.0 | 1.00 | 1 | kept |
| `J1w0` | 1 | 1 | apples only | 23.7 | 10.5 | 29.3 | 18.9 | 1.00 | 1 | kept |
| `J3w0` | 3 | 1 | apples only | 6.0 | 3.3 | 30.1 | 20.7 | 1.00 | 1 | depleted |
| `J3w48` | 3 | 1 | apples + 48 × last level | 6.0 | 3.3 | 443.9 | 434.6 | 1.00 | 1 | depleted |
| `J3s8` | 3 | 8 | apples + 6 × last level | 24.5 | 5.1 | 220.3 | 205.9 | 1.00 | 1 | kept |
| `J3s16` | 3 | 16 | apples + 6 × last level | 98.7 | 23.9 | 337.8 | 267.7 | 1.00 | 1 | kept |
| `J3opt` | 3 | 1 | apples + 6 × last level; initial values 100 (> 70.6, the largest exact value) | 6.0 | 3.3 | 70.6 | 61.2 | 1.00 | 1 | kept |

"Full draw empties in": mean steps for m requests at every step to empty a full patch (CG2's `calibrate.scripted_alive`, 400 runs). The full draw leaves the patch standing at step 80 with probability 0.00 in every condition but `J3s16` (0.015), so "kept" is never what the full draw does.

## Alternative accounts, and where each predicts otherwise

- **U, reading the union suffices** (CG2's X5 premise): every condition kept, because the optimum keeps in all.
- **A, the draw cap** (failure comes from the size of the immediate draw, 3 apples a step, whatever the renewal): `J3s8`, `J3s16` depleted, as `J3`; `J1` kept.
- **W, the end weight** (a large enough weight on the end level makes restraint learned): `J3w48` kept. It also predicts `J1w0` and `J3w0`, with no end weight, depleted.
- **D, the end reading's distance** (CG2's post hoc wording: values unconverged far from a reading 100 steps away): `J3w0` and `J1w0`, with no end reading and every reading per step, kept; `J1` depleted (same distance as `J3`).
- **K, the known exploration account** (zero initial values plus dithering): `J3opt` kept. On the others it agrees with the account under test where its quantity is `cov`.

## Predictions and verdict rules

**Training and evaluation** are CG2's configuration, unchanged: tabular Q, state = (level, steps left), undiscounted, α = 0.1, ε from 1 to 0.02 over the first 80% of 30,000 episodes, exploring starts, H = 100, 20 seeds per condition, 200 greedy evaluation episodes from a full patch on fresh regrowth streams. **Measure:** the share of evaluation episodes in which the patch still stands at step H − 20, averaged over seeds (CG2's measure). *Kept* passes at ≥ 0.80, *depleted* at ≤ 0.20, otherwise failed. `J2` passes if mean(J3) ≤ mean(J2) ≤ mean(J1).

**Contrasts** (each passes only if all its conditions pass):

- **Y1, the own draw's coverage, not the draw cap:** `J3` depleted, `J3s8` kept, `J3s16` kept. A predicts `J3s8` and `J3s16` depleted. `J3s8` is the sharp case: the same three-request action set and the same immediate draw as `J3`, but the coverage of `J1`.
- **Y2, not the end weight:** `J3` and `J3w48` depleted. W predicts `J3w48` kept.
- **Y3, not the end reading:** `J3w0` depleted, `J1w0` kept. D predicts `J3w0` kept; W predicts `J1w0` depleted.
- **Y4, order in the draw cap:** `J1` kept, `J2` between them, `J3` depleted. D predicts `J1` depleted.
- **Y5, the known remedy opens it:** `J3opt` kept. If it fails, the failure is not (only) the zero-initialised dithering of K.

**Identity checks:**
- **I1:** CG1's checks (balance, the gate, the margin, joint excess) on every training and evaluation episode. With one selector, the joint-excess part is the selector's own takes over a run of steps: `Flow.joint_excess_ends` read across time. Pass: zero violations over a positive number of windows.
- **I2:** `Regulation.accumulates_at` on emptied courses. In every evaluation episode whose level after the last step is 0, the apples taken equal the 9 at the start plus the apples regrown. Pass: zero violations over a positive number of episodes.

## What would change the account

- Y1 failing at `J3s8` (depleted with `J1`'s coverage): coverage is not what decides; the draw cap (A) or something tied to the three-request action set does.
- Y2 failing (`J3w48` kept): the end weight speeds the learning enough that the own draw's coverage does not bind; W describes the learner better.
- Y3 failing at `J3w0` (kept with no end reading): the failure needs the distant end reading (D), and the own draw is not enough to cause it.
- Y4 failing at `J1`: coverage 23.7 is not enough at an end weight of 6, though it was at 2 in CG2's control; the anchor is wrong.
- Y5 failing: zero initialisation is not the lever, so the account's link to K is wrong.

## Limits stated in advance

CG1's environment, CG2's learner and training. The exact computation (`n_keep`, the optimum) is over policies reading the whole configuration, while the learner reads the level and the steps left. The anchors are two outcomes, one of them three seeds of a post hoc control. The thresholds 20 and 7 come from those anchors, not from a derivation of the learning dynamics, so the account is tested as a ranking quantity. The thresholds 0.80 and 0.20 are CG2's. About 50 CPU-minutes.
