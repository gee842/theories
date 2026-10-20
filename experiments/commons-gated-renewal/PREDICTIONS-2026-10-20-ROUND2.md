# Round 2 of the commons test, frozen 20 October 2026

Board item CG1. AI-written. Frozen before any round-2 run, with the code change below; round 1's verdicts ([predictions](PREDICTIONS-2026-10-20.md), results at `c8765a03c`) stand as recorded, failures included, and nothing here revises them.

## Why a second round

In round 1 every learner, coupled ones included, emptied its patch before step 80 in every evaluation episode. The cause was H2 (that the learners come near the best return), not a law. Their mean harvest, 16.6 apples, was above harvesting at every step (10.45) but far below the best scripted rule (28.5). The Q-tables show why: in training, random play emptied the patch early, so no course reached a late step with an apple standing. The values of those states stayed at their initial 0, and the coupling term (λ times the level after the last step) never once returned a nonzero reward. Round 1 therefore tested the learners' coverage, not the laws, on C2, C3, D1's manipulation check and D2. (Read through the spine, the learners met the gap's condition in an unplanned way: a reward term coupled into a level that no course reaches selects nothing. That reading is post hoc, and it is not counted as a result.)

## The one change

Training episodes start from **exploring starts**: at a uniformly random step t₀ of the 100, with each cell of each patch holding an apple with probability u, u uniform on [0, 1] and drawn anew for each patch and episode. The draws come from one stream of the run, `"{seed}/starts"`, which no agent reads, so D1's two conditions get identical starts. Exploring starts are a standard remedy for coverage in tabular reinforcement learning. Evaluation is unchanged: greedy, from full patches at step 0, on the round-1 evaluation streams. Everything else is unchanged: the environment, rewards, λ = 2, learning rate, exploration schedule, episode counts, seeds, the evaluation and every prediction, criterion and class. `analyze.py` is the round-1 file with correction 1. Round 2 reruns C, D1 and D2 only (`python3 run.py round2`, results in `results/round2/`). A, B and E involve no learner whose training changes, so their round-1 runs are reused.

## What round 2 can show

If H2 now holds, C1–C3, D1 and D2 test the laws' readings as frozen. If H2 still fails, they fail again under the same rule, and the report says so. The not-testable rule is unchanged (no better than harvesting at every step). The report also gives each learning condition's mean evaluation harvest against the best scripted rule (28.5), as a descriptive measure of H2. That measure was not a criterion in round 1 and is not one here.

Run only after this file and the code change are committed.
