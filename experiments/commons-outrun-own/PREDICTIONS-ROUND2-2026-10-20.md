# CG3 round 2: predictions frozen 20 October 2026, after round 1 and before any round-2 run

AI-written (the CG3 session). Round 1 ([PREDICTIONS](PREDICTIONS-2026-10-20.md), frozen at `f6a88683d`; verdicts in [results/VERDICTS.json](results/VERDICTS.json)) is closed and its verdicts stand. This round is frozen in one commit, made before any of its learning runs: this file, [`round2.py`](round2.py) (its conditions, training, run and verdict rules) and [`results/round2-exact.json`](results/round2-exact.json) (the exact quantities, no learning). Before the freeze, besides the exact computation, only a smoke run (30 episodes) and a code-path test of the analysis (50 episodes, 2 seeds, kept nowhere) were run. Round 1's files are not changed.

## What round 1 left

The round-1 account, the own exploratory draw's coverage `cov`, failed on its sharpest case. `J3s8` (three requests at regrowth ×8) has `J1`'s coverage (24.5 against 23.7) and was depleted in every seed (0.01). The other seven graded conditions passed, and `J2`'s order passed only by a tie at 0.00.

**Post hoc, not counted** (the greedy tables in round 1's `runs.json`):
- In `J3s8` the learner did learn restraint in mid-course: at level 6, the mean greedy request is 1.1 with 80 steps left and 0.6 with 50, against 2.6 with 100 steps left.
- Near the start of a course it takes nearly the full draw, and at the start the patch empties within about four steps under the full draw (exact: 4.1 steps standing).
- In `J3` (regrowth ×1) restraint appears only in the last few steps.

Exploring starts are uniform over the step, so a state with t steps gone is reached only from the t + 1 earliest start steps, and the states at the start of a course are the least trained. Ranked by the steps a full patch stands under the full draw (`full`), round 1 separates exactly: kept at 9.4 (`J1`, `J1w0`) and 22.6 (`J3s16`); depleted at 4.1 (`J3s8`, `J2`) and 2.3 (`J3`, `J3w0`, `J3w48`).

This is the post hoc reading of CG2's X5 in a corrected place. The learner's own greedy acts outrun the renewal where its values are untrained, and that region is the start of the course, not the end. Read with the theory's terms, it is `Flow.joint_excess_ends` with the part being the learner's own early full draw: the course ends before it reaches the steps whose values carry restraint.

## The account under test (two quantities, both exact)

- `cov` (round 1's quantity) decides whether restraint is learned in mid-course: learned at ≥ 20, not learned at ≤ 10.
- `full` decides whether a course from the start, where the greedy act is the full draw, reaches that region: it reaches at ≥ 9, the condition ends first at ≤ 5.5.
- **Kept** where restraint is learned and the course reaches it: `cov` ≥ 20 and either `full` ≥ 9 or the start region is trained (early starts).
- **Depleted** where `cov` ≤ 10, or where `full` ≤ 5.5 and the start region is untrained.

Thresholds from round 1's anchors: `cov` 23.7 learned (`J1`) and 24.5 learned (`J3s8`'s mid-course greedy); `full` 9.4 kept and 4.1 depleted.

**Early starts** (`early`): in half of the training episodes the start step is drawn uniformly from the first 10 steps, and otherwise uniformly from all 100 as in round 1. The MDP, the reward, the action set and the evaluation are unchanged.

| Condition | m | s | Training | `cov` | `full` | optimum | P(opt alive at 80) | P(full draw alive at 80) | Account | cov alone | full alone | draw cap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `R3s10` | 3 | 10 | round 1's | 54.9 | 5.3 | 262.8 | 1.00 | 0.00 | **depleted** | kept | depleted | depleted |
| `R2s4` | 2 | 4 | round 1's | 20.2 | 5.4 | 134.4 | 1.00 | 0.00 | **depleted** | kept | depleted | — |
| `R3s14` | 3 | 14 | round 1's | 93.1 | 10.6 | 317.9 | 1.00 | 0.00 | **kept** | kept | kept | depleted |
| `R2s8` | 2 | 8 | round 1's | 88.2 | 12.1 | 213.9 | 1.00 | 0.00 | **kept** | kept | kept | — |
| `R3s8early` | 3 | 8 | early starts | 24.5 | 4.1 | 220.3 | 1.00 | 0.00 | **kept** | kept | depleted | depleted |
| `R3early` | 3 | 1 | early starts | 6.0 | 2.3 | 70.6 | 1.00 | 0.00 | **depleted** | depleted | depleted | depleted |

The reading is apples + 6 × the level after the last step throughout. All other settings are round 1's (CG2's configuration, 20 seeds, 200 greedy evaluation episodes from a full patch, measure: share alive at step 80, kept ≥ 0.80, depleted ≤ 0.20).

**Contrasts:**
- **Z1, coverage is not enough:** `R3s10` and `R2s4` depleted (`cov` alone predicts both kept).
- **Z2, a full draw that lasts reaches the learned region:** `R3s14` and `R2s8` kept (the draw cap predicts `R3s14` depleted).
- **Z3, training the start rescues only where mid-course restraint is learned:** `R3s8early` kept and `R3early` depleted (`full` alone predicts `R3s8early` depleted; an account in which training the start is enough predicts `R3early` kept). Z3 is the sharp case: the same manipulation is predicted to act in one condition and not in the other.

**Identity checks:** I1 and I2 as in round 1.

**What would change the account.**
- Z1 failing: a full draw of 5.3 steps does reach the learned region, so the threshold is lower than 5.5, or `full` is not the quantity.
- Z2 failing: something besides the two quantities ends the patch where both are high.
- Z3 failing at `R3s8early`: the start region is not what fails in `J3s8`.
- Z3 failing at `R3early`: training the start is enough even where mid-course restraint is not learned, so `cov` is not needed.

About 17 CPU-minutes.
