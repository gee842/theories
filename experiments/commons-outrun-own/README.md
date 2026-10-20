# Whether a stepwise learner's own later acts outrun what it reads (CG3)

Board item CG3, 20 October 2026. AI-written (a Claude Code session started from CG2's line). It tests the post hoc reading of CG2's failed contrast X5 ([`../commons-outrun`](../commons-outrun/README.md), study §250). There, one tabular learner chose 0–3 requests a step on a gated 3×3 patch, rewarded with all the apples plus 6 × the level after the last step. It emptied the patch in every seed, though the exact optimum keeps it. The reading was that the outrunning rest is the learner's own later acts: the end reading's value reaches a state only where its own later policy does not end the condition first (`Flow.outrun_reading_alike` read across time).

**In brief.**
1. The reading is false in its exact form, and that was settled before any run. One sweep of exact policy improvement from the full draw keeps the patch in every condition, even with no end reading. One's own later acts are improved together with the present act, so they are not a fixed rest. The step's apples already read the renewal.
2. What fails is sampled learning, and that is the known exploration problem ([literature check](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md#own-later-acts-check)).
3. Two frozen rounds located where the learner's own acts outrun the renewal: at the start of a course, where its values are least trained and its greedy act is the full draw, not at the end. The sharp prediction of round 2 held: training the start rescues the one learner whose mid-course restraint was learned, and not the one whose was not.
4. Both rounds' threshold accounts failed somewhere. The boundary depends jointly on the two quantities, and neither threshold locates it.

| File | What it is |
|---|---|
| [PREDICTIONS-2026-10-20.md](PREDICTIONS-2026-10-20.md) | Round 1: the exact result, the account (own exploratory coverage), nine conditions, contrasts Y1–Y5 against union, draw-cap, end-weight and end-distance accounts. Frozen at `f6a88683d` |
| [PREDICTIONS-ROUND2-2026-10-20.md](PREDICTIONS-ROUND2-2026-10-20.md) | Round 2: what round 1 left, the two-quantity account, six conditions, contrasts Z1–Z3. Frozen at `87b6a0b36` with round 1's results |
| [exact.py](exact.py) | Exact dynamic programmes over the 512 configurations: optimum, full draw, policy iteration from the full draw, the coverage curves (output [results/exact.json](results/exact.json)) |
| [conditions.py](conditions.py), [own.py](own.py), [run.py](run.py), [analyze.py](analyze.py) | Round 1: conditions, the learner (CG2's `learners.Q`, CG1's environment and checks, imported unchanged), the run, the verdict rules |
| [round2.py](round2.py) | Round 2: conditions, training with early starts, exact quantities, run and verdict rules |
| [results/](results/) | `runs.json`, `VERDICTS.json`, `run.log`, `FROZEN-AT` (round 1); `round2-*` (round 2) |

To reproduce (Python 3.11, standard library, CPU): `python3 exact.py && python3 run.py all && python3 analyze.py`, then `python3 round2.py exact && python3 round2.py all && python3 round2.py analyze`. The runs took 26.0 and 19.6 CPU-minutes, and the exact computations a few more.

## The exact result (before any run)

[`exact.py`](exact.py) runs policy iteration from the full draw, the policy a learner holds once its immediate apples are learned. Each sweep evaluates the current policy exactly and takes the greedy policy against it, so the value of restraint is read through the selector's own later acts as they stand. **After one sweep the policy keeps the patch standing at step 80 with probability 1.00 in all nine round-1 conditions**, including `J3w0` and `J1w0`, which have no end reading (optimum gain over the full draw 20.7 and 18.9). Against a later full draw, an apple withheld now is still taken later, and while it stands it lets the empty cells around it regrow. So restraint beats the full draw at every step but the last few, through the apples alone (`Regulation.accumulates_at`: an emptied course takes its start plus everything given). A single selector's later acts are improved in the same sweep (the policy improvement theorem), so across time there is no lock like CG2's equilibrium across members, and no delay of the exact improvement. `Flow.outrun_reading_alike` needs the rest held fixed, and one's own later acts are not.

## Round 1 verdicts

Measure (CG2's): the share of 200 greedy evaluation episodes from a full patch in which the patch stands at step H − 20, averaged over 20 seeds. Kept passes at ≥ 0.80, depleted at ≤ 0.20. `cov`: the exact steps (of 100) a full patch stands under uniform requests 0..m. `full`: the same under the full draw. Return: the mean of apples + w × the last level.

| Condition | m | s | w | `cov` | `full` | Predicted | Alive at H − 20 | Seeds ≥ 0.8 / ≤ 0.2 | Alive at H | Return (optimum) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `J3` (CG2's joint learner, new seeds) | 3 | 1 | 6 | 6.0 | 2.3 | depleted | 0.00 | 0 / 20 | 0.00 | 9.4 (70.6) | **passed** |
| `J2` | 2 | 1 | 6 | 9.7 | 4.1 | J3 ≤ J2 ≤ J1 | 0.00 | 0 / 20 | 0.00 | 9.7 (70.6) | **passed** (by a tie with J3) |
| `J1` | 1 | 1 | 6 | 23.7 | 9.4 | kept | 1.00 | 20 / 0 | 1.00 | 26.7 (70.4) | **passed** |
| `J1w0` | 1 | 1 | 0 | 23.7 | 9.4 | kept | 1.00 | 20 / 0 | 0.01 | 16.1 (29.3) | **passed** |
| `J3w0` | 3 | 1 | 0 | 6.0 | 2.3 | depleted | 0.00 | 0 / 20 | 0.00 | 9.5 (30.1) | **passed** |
| `J3w48` | 3 | 1 | 48 | 6.0 | 2.3 | depleted | 0.00 | 0 / 20 | 0.00 | 9.5 (443.9) | **passed** |
| `J3s8` | 3 | 8 | 6 | 24.5 | 4.1 | kept | 0.01 | 0 / 20 | 0.01 | 18.4 (220.3) | **failed** |
| `J3s16` | 3 | 16 | 6 | 98.7 | 22.6 | kept | 1.00 | 20 / 0 | 1.00 | 257.1 (337.8) | **passed** |
| `J3opt` (initial values 100) | 3 | 1 | 6 | 6.0 | 2.3 | kept | 1.00 | 20 / 0 | 1.00 | 47.8 (70.6) | **passed** |

| Contrast | Verdict |
|---|---|
| Y1 the own draw's coverage, not the draw cap (`J3` depleted, `J3s8` and `J3s16` kept) | **failed** (`J3s8` 0.01) |
| Y2 not the end weight (`J3`, `J3w48` depleted) | **passed** |
| Y3 not the end reading (`J3w0` depleted, `J1w0` kept) | **passed** |
| Y4 order in the draw cap (`J1` kept, `J2` between, `J3` depleted) | **passed** (`J2` by a tie) |
| Y5 the known remedy opens it (`J3opt` kept) | **passed** |

Identity checks, both **passed**:
- I1: CG1's balance, gate, margin and joint-excess checks, with the selector's own takes as the part of `Flow.joint_excess_ends`, over 276.3 million steps and 3.25 million own-excess windows: 0 violations.
- I2: `Regulation.accumulates_at` on 23,911 emptied courses: 0 violations.

## Round 2 verdicts

Account (frozen at `87b6a0b36` with round 1's results): `cov` decides whether restraint is learned in mid-course, and `full` decides whether a course from the start, where the greedy act is the full draw, reaches it. Early starts: half the training episodes start in the first 10 steps.

| Condition | m | s | Training | `cov` | `full` | Predicted | Alive at H − 20 | Seeds ≥ 0.8 / ≤ 0.2 | Alive at H | Return (optimum) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `R3s10` | 3 | 10 | round 1's | 54.9 | 5.3 | depleted | 0.80 | 11 / 0 | 0.80 | 176.7 (262.8) | **failed** |
| `R2s4` | 2 | 4 | round 1's | 20.2 | 5.4 | depleted | 0.28 | 1 / 10 | 0.28 | 28.0 (134.4) | **failed** |
| `R3s14` | 3 | 14 | round 1's | 93.1 | 10.6 | kept | 1.00 | 20 / 0 | 1.00 | 242.6 (317.9) | **passed** |
| `R2s8` | 2 | 8 | round 1's | 88.2 | 12.1 | kept | 0.97 | 20 / 0 | 0.97 | 177.2 (213.9) | **passed** |
| `R3s8early` | 3 | 8 | early starts | 24.5 | 4.1 | kept | 0.84 | 17 / 2 | 0.06 | 138.9 (220.3) | **passed** |
| `R3early` | 3 | 1 | early starts | 6.0 | 2.3 | depleted | 0.00 | 0 / 20 | 0.00 | 11.2 (70.6) | **passed** |

| Contrast | Verdict |
|---|---|
| Z1 coverage is not enough (`R3s10`, `R2s4` depleted) | **failed** (0.80, 0.28) |
| Z2 a full draw that lasts reaches the learned region (`R3s14`, `R2s8` kept) | **passed** |
| Z3 training the start rescues only where mid-course restraint is learned (`R3s8early` kept, `R3early` depleted) | **passed** |

Identity checks, both **passed**: I1 over 211.2 million steps and 1.25 million own-excess windows, and I2 on 11,543 emptied courses, with 0 violations.

Count over both rounds: of 15 conditions, 12 passed and 3 failed; of 8 contrasts, 6 passed and 2 failed.

## What the results say

**One's own later acts are not a rest.** CG2's law reads a rest whose takes are fixed: there, depletion was locked for every end weight (X2). For one selector the exact computation finds no lock, because one improvement sweep already keeps the patch. The learners show the same separation from the end reading. Removing it (`J3w0`) or multiplying it by eight (`J3w48`) changed nothing at three requests a step (0.00 in all three), and at one request a step the patch was kept with or without it (`J1`, `J1w0`: 1.00). The end reading neither causes the failure nor cures it. CG2's post hoc wording, values unconverged far from the end reading, describes the symptom, not the cause.

**Where the learner's own acts do outrun the renewal: the start of a course.**
- Exploring starts uniform over the step reach a state t steps into a course only from starts at or before t, so the first steps of a course are the least trained. There the learner's greedy act is still the full draw, whose apples it learned first.
- Where its exploration lets courses stand long enough (`cov` about 24 or more), it learns restraint in mid-course: in `J3s8`, at level 6 the greedy request falls from 2.6 at the start to 0.6 with 50 steps left. But from a full patch the full draw ends the condition within about four steps, before the course reaches that region.
- Training the start fixed this exactly where the account said: `R3s8early`, the same learner with half its training starting in the first ten steps, kept the patch (0.84, 17 of 20 seeds). The same manipulation left `R3early` at regrowth ×1, whose mid-course restraint is never learned, at 0.00. It then emptied the patch near the end (alive at H 0.06), because the late steps were now the less trained. That is the same mechanism, displaced.
- Optimistic initial values (`J3opt`), the known remedy, kept the patch everywhere it was tried.

So the theory's reading survives in a corrected place. The part whose joint taking outruns the renewal is the learner's own full draw in the region its values have not reached (`Flow.joint_excess_ends` read across time, held by I1 in 3.25 million windows), and that region is set by where training starts and how long its own exploration lets courses stand.

**Neither threshold locates the boundary.** Round 1's single quantity failed at `J3s8`. Round 2's threshold on the full draw failed in turn: `R3s10` (full draw standing 5.3 steps, coverage 54.9) was kept in 11 of 20 seeds (0.80), and `R2s4` (5.4, 20.2) split (0.28). High coverage also trains the start region, because the few early starts then pass through many early states. So the boundary is a joint function of the two quantities, and neither threshold, set from the anchors of the round before, locates it.

## What is new against prior work, and what is not

Known: that the greedy policy against an evaluation improves on it and that one's own later acts are revised with it (policy improvement, Sutton and Barto §4.2–4.6); that dithering exploration needs time exponential in the length of the consistent course to a delayed value (Osband et al. 2019); that exploration fails in systems its own acts can end (Moldovan and Abbeel 2012); that zero-initialised Q-learning is intractable where optimistic initialisation is not (Koenig and Simmons 1996); and that exploring starts govern which states a learner evaluates (Sutton and Barto §5.3). The CG3 findings are none of them new as learning theory.

New here, as frozen tests with their outcomes:
- the exact refutation of the across-time reading of CG2's law (one sweep keeps the patch);
- the measured irrelevance of the end reading for this learner (Y2, Y3);
- the location of the outrun at the start of the course, predicted before the run that tested it (Z3);
- the failure of each round's threshold (Y1, Z1).

Their value for the theory is a boundary on what `Flow.outrun_reading_alike` explains. It explains a selection blind to an act where the rest is held fixed (CG2), and not a selector's blindness to its own later acts. The latter is the sampling of its own courses: what it has evaluated, set by its training and by how long its own acts let the condition stand.

## Corrections after the freezes

None. Round 1 ran from `f6a88683d` and round 2 from `87b6a0b36` (`results/FROZEN-AT`, `results/round2-FROZEN-AT`), and no code, condition or rule changed after either. Round 2 was designed after round 1's verdicts, from its greedy tables and new exact quantities, and frozen before any of its runs. Its anchors are round 1's outcomes, as its file states.

## Limits

- The environment is CG1's (one isolated 3×3 patch, no walking or tagging), the regrowth scale is a manipulation, and the learner and training are CG2's (tabular Q, uniform exploring starts, 30,000 episodes), with 20 seeds per condition.
- The exact computations are over policies reading the whole configuration; the learner reads the level and the steps left.
- The diagnosis of the start region rests on greedy tables averaged over seeds and on one manipulation (`R3s8early`, `R3early`). A law for the boundary as a joint function of coverage and the full draw was not derived.
- Total compute was 46 CPU-minutes of runs.
