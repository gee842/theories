# The margin as a measured quantity

Board item MQ1, 20 October 2026. AI-written (a Claude Code session started from the significance-aim session). Study section 253 of [BECOMING-RENEWAL-READING](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#253-the-margin-as-a-measured-quantity-mq1). Literature check: [significance review, "the margin as a measured quantity"](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md#margin-measured-check).

Thermodynamics became more than formal when temperature and heat became measured state quantities whose laws could fail. This experiment asks the same of the theory's margin: a renewable condition's slack above its need, depleted by the sum of all parts' net draws. It operationalizes the margin, freezes predictions from the laws written in it, and runs two test beds. The first is a microbial Allee system (a stochastic simulation set from Dai et al. 2012; their published data test is frozen and waits for a download Ren approved but Dryad's bot check blocks). The second is an RL side-effect gridworld with renewable conditions. Every verdict is kept.

| File | What it is |
|---|---|
| [PREDICTIONS-2026-10-20.md](PREDICTIONS-2026-10-20.md) | Step 0 literature table; the exact Lean content; the reading that sets what can be tested; bridges R, H1, H2; predictions A1-A4, D1-D2, B1-B7 with classes and pass rules. Frozen at `b14f7b739` (`6b29f6ac0` before rebasing onto main) |
| [PREDICTIONS-2026-10-20-ROUND2.md](PREDICTIONS-2026-10-20-ROUND2.md) | Round 2: two configuration corrections (A1's harvest beyond the margin; A3's unharvested first day), criteria unchanged; why no learner round. Frozen at `3b991bb8d` (`037683ad8` before rebasing), after round 1's results |
| [yeast.py](yeast.py) | Test bed A: the two-phase growth model, noise, and the measurements by intervention (pulse margin, largest sustained draw, break day, histories) |
| [garden.py](garden.py) | Test bed B: the lawn gridworld, exact best responses, tabular Q-learners, coupling by intervention, the margin law's band |
| [run.py](run.py), [analyze.py](analyze.py) | Frozen configurations and verdict rules |
| [calibrate_yeast.py](calibrate_yeast.py), [calibrate_learners.py](calibrate_learners.py) | Test bed A's calibration (before the freeze); the post-hoc learner calibration on the reference variant (after round 1) |
| [results/](results/) | Round 1 (`*.json`, `VERDICTS.json`), round 2 (`round2/`), `FROZEN-AT` |

To reproduce (Python 3.11, standard library only, CPU; about 13 minutes over 12 cores, almost all of it test bed B's learners):

```bash
python3 run.py all && python3 analyze.py
```

```bash
python3 run.py round2 && python3 analyze.py results/round2
```

## The reading that sets what can be tested

In the margin law (`Flow.Balances.loses_iff_beyond_margin`, `Flow.widens_iff_within_margin_at`), the levels without the part are the **withheld levels** (`Flow.WithheldLevels`): the part's exchanges removed, every other exchange held as it was. Under that counterfactual, laws (2) "draws on a shared condition add, time to break = margin / total net draw" and (3) "damage iff cumulative net draw exceeds the margin" are identities of the balance. That is SA1's near-definitional verdict, and test bed B's B1 confirms it in 456 records with no mismatch. An actual condition's renewal responds to its level, so the testable content lies in the margin **measured by intervention**, with the rest responding: the pulse margin (the largest one-shot removal the condition survives), the largest sustained draw Ŷ, the reward's coupling (the change in return when the condition is perturbed and the same actions are replayed), and blind draw (draw on a condition with zero measured coupling).

## Verdicts

Classes: *identity* (follows from what the system is built to meet), *identity in the deterministic limit* (tests the measured quantities under noise), *manipulation* (shows a test can fail), *law + bridge*, *beyond the law*.

| Prediction | Law | Class | Round 1 | Round 2 |
|---|---|---|---|---|
| A1 same margin, any history → same break-day distribution | margin as state | identity (Markov model) | passed, **degenerate** (H ≥ m₀: break at day 0 in every replicate) | **passed** (all KS p ≥ 0.75) |
| A1m with a hidden lag state, the test detects history | — | manipulation | failed, degenerate | **passed** (p to 1e-51) |
| A2 break day within [m₀/H − 1, (m₀ − H)/(H − Ŷ) + 1], m₀ by pulse, Ŷ by sustained draw | margin law + joint excess + R | identity in the deterministic limit | **passed** (22/22 cells; position in band 0.31-0.94) | (round 1's) |
| A3 the point of no return under a standing draw H exceeds need + H | margin law, responsive renewal | identity in the deterministic limit | failed 6/12 (**code grew one unharvested day first**) | **passed** (12/12; above need + H by 8,400-33,600 cells/µl) |
| A4a interaction of two harvesters' harms never sub-additive | concave renewal | beyond the law | **passed** (12/12) | — |
| A4b each within Ŷ, together beyond → super-additive | joint excess | law | **passed** (4/4; joint collapse 93-100%) | — |
| A4c joint within Ŷ → still super-additive | concave renewal | beyond the law | **passed** (8/8) | — |
| D1, D2 on Dai et al.'s data (density is the state; the need separates fates) | (1), (3) on real yeast | could fail | **not run**: the download is behind Dryad's bot check | — |
| B1 level = l₀ − takes + regrowths; dead iff takes ≥ l₀ + regrowths | margin law, balance | identity | **passed** (0 mismatches, 456 records) | — |
| B2 replayed coupling: blind exactly 0, coupled > 0 | coupling | identity | **failed**: blind 0 everywhere, but 5 joint records with a coupled reward show 0 for a cell (see below) | — |
| B3 blind behaviour identical across margins | `Flow.act_unselected` + H1 | law + bridge | best response **passed**; learners **failed** (entries 5.0-6.95 against V0's 7.8) | not rerun |
| B4 side effects predicted out of sample from blind draw in V0 against each variant's margin | margin law + joint excess + B3 | law + bridge | best response **passed** (8/8 decided right, 8/8 deaths within band; the V0-outcome baseline 0/8); learners **failed** (80/151 right; 6/80 within band) | not rerun |
| B5 coupled draw adapts: all alive; binding cells left ≤ need + 1 | margin law, `OwnWidening` | law (+ H1, H2) | best response **failed** on one cell (V4's B left at 3: its route is shut by A); learners **failed** on the transfer clause (74% < 80%) while keeping 160/160 cells alive | not rerun |
| B6 step coupling: deaths only where the coupling's remaining reach < the gain | `Flow.act_unselected` | law | best response **failed, vacuous** (no death); learners **passed** (2 deaths, both at step 41 = H − 4) | — |
| B7 end-coupled agents trained alone, together, break a binding cell | joint excess, `mixed_of_tight` | law + bridge | best response **passed** (4/5); learners **failed** (6/50); band **failed** (3/13) | not rerun |

## What the results say

**The margin is measurable by intervention, and with one more measured number it bounds time to break whatever the history.** In the Allee system the need found by the pulse test matches the model's unstable fixed point (DF 1000: 4,128 against 4,149 cells/µl). The largest sustained draw found by intervention matches the model's maximal surplus (34,304 against 35,064). These two numbers bound the mean break day in every cell tested, across four dilution factors and two starting levels. History adds nothing when the system has no hidden state, and the same test detects a hidden lag state when one is added. This is the operational content of laws (1) and (2). It holds by the mathematics in the deterministic limit, so what the test shows is that the measurements work under noise, not new dynamics. The band is wide (its upper end is often several times its lower), and a point prediction needs the renewal curve: the equation of state, in the thermodynamic analogy.

**The need is the whole flow's, not the condition's alone.** Under a standing draw H, the point of no return rises by more than H: it is H plus the rising root of s(y) = H, not need + H. Measured: 1.4-4.1 times H above the need, rising with the dilution factor (DF 500 to 1400). "Margin = level − need" is a state quantity only with the need taken from the regime including the standing draws, as a boiling point is a state quantity only at a given pressure. Fisheries know this as depensation under harvest. The theory's frozen-rest margin hides it, because the withheld levels keep the rest's giving as it was.

**Draws add; harms do not.** The frozen-rest accounting adds draws exactly. The harm two harvesters do together exceeded the sum of their separate harms in all 12 cells: by about 20% where both drew 0.3Ŷ, and to total collapse where each was within Ŷ and together they were beyond it. The renewal curve is concave above its peak, so removal by one part steepens the cost of the other's draw. Harm attributed to parts by removal is not additive on a shared renewable condition. Law (2) holds for draws, not for the damage they cause. In the gridworld the same structure appeared post hoc: two end-coupled best responses, each well within the lawn's renewal alone in V0, killed both cells together.

**Blind draw predicts side effects for an ideal optimizer, not for these learners.** Measured in the ample-margin variant, where nothing dies, the best response's blind draw predicted which cells die in the five thin-margin variants and when (8/8, all within the band). Predicting from the reference outcome scores 0/8. With a coupled reward the best response kept every cell alive, leaving every route-limiting cell (six cells) at level 1, exactly the gate's need: the margin spent to zero, the tight case of `Flow.Balances.mixed_of_tight`. Tabular learners did not transfer. Their reward is blind, but they observe the lawn, and in variants where its state varies more their experience is spread over more states. They wander more, deliver less, and so draw less: of 80 observed deaths, 71 came after the band's upper end and 3 before its lower end, and in V1 and V2 no cell died at all. That is H2 (learners far from the best response: 5-7.75 deliveries against 9), not selection. Each policy's own entries still place every death within its band (80/80). Blindness of the selection signal makes draw margin-independent under selection; a learner that sees the condition is margin-dependent through its own coverage.

**Coupling measured by intervention is a property of a course.** B2 failed because the measure replays one course: along five joint courses the agent's own actions killed a cell whatever its start level, so changing the level changed no return, though the reward reads the cell. The theory's coupling is also along a course. The failure is in the prediction's wording ("> 0 in every record"), and it shows the measurement needs perturbations the course does not saturate.

**Whether the margin is a measurable state quantity.** Yes, in a qualified sense. It can be measured by intervention, and with the largest sustained draw it bounds time to break independently of history wherever the condition's state is its level (A1, A1m, A2). Three qualifications. Its need depends on the standing draws, so it is a state quantity of the regime, not of the condition alone (A3). Damage on it does not add across parts (A4). And whether a real population is Markov in its density is untested here: that is D1 on Dai et al.'s data, frozen and waiting for the download. On the alignment side, blind draw against margin predicts side effects for an optimizer (B4), and coupling makes the optimizer spend the margin down to need (B5). Both depend on the optimizer actually optimizing.

## Corrections after the freeze

1. A1 and A1m (round 1) were degenerate: the frozen harvest 1.5Ŷ was at least the starting margin m̂/2. A2's applicability guard (H < m₀) was missing from A1. Round 2 fixed the configuration only.
2. A3 (round 1) measured a protocol with one unharvested day before the standing harvest, unlike the prediction's wording. Round 2 harvests from day 0.
3. No learner round 2: a calibration on the reference variant only (6 seeds per setting) found no setting reaching the best response, so a rerun would test H2 again.
4. Round 1's verdicts stand as frozen; each round's commit is in `results/FROZEN-AT` (hashes before the rebase onto main; the rebased commits are listed in the table above).

## Limits

Test bed A is a simulation: the parameters are set from the paper's reported facts, not its table S1. Near the fold the model's fluctuations (CV 0.06 at DF 1400) are below the paper's (about 0.2). The culture volume is assumed. The hidden lag state of A1m is invented to give the test something to detect, not measured biology. Test bed B is deterministic and small (14 cells, horizon 45, two lawn cells). Its best responses are exact, and its learners are tabular with modest training. B6's environment did not create the end-of-coupling situation for the best response. D1-D2, the only predictions on real data, are not run.
