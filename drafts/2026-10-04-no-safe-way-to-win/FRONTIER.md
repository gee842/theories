# The talk's Pareto frontier, and the point chosen

On 2026-10-04 Ren handed the talk's open choices back: "I'll let you to generate the pareto frontier of your own". This note is that frontier and the decision taken from it. Everything here is the assistant's judgment, made explicit so it can be argued with: [frontier.py](frontier.py) recomputes it, and its full output is in [frontier-output.txt](frontier-output.txt).

## Objectives

Three, for a 10–20 minute talk to a mixed international audience:
- **Time** (minimise): seconds, from the script's timing cues.
- **Fidelity, F** (maximise): how much of Ren's argument a slide carries, judged against the 2026-10-04 recording and the theory documents.
- **Reception, R** (maximise): how much a slide helps a mixed room understand and accept the argument, net of the risk of being misread (as allegiance, essentialism, naivety or fate).

Six slides are required by the argument's spine (cover, *winning buys the means to win again*, *AI enters the game*, *there is no safe way to win*, *an order of moves*, the close). Sixteen are optional. Coherence constraints: the 心/理 slide needs the relations slide; part 3 (why careful people can't see the exit) and the affirmative alternative must each keep at least one slide; the mechanism must keep at least one of *minds*, *boundary*, *kernel*. Within each part, a second slide counts 0.85, a third 0.72, and so on, so a talk that covers every part beats one that piles slides into one part.

| slide | s | F | R | part |
|---|---|---|---|---|
| film (75 s excerpt + framing) | 105 | 5 | 8 | opening |
| agenda | 35 | 1 | 3 | opening |
| minds: the game selects ways of deciding | 55 | 9 | 6 | the game |
| boundary: the error that wins | 50 | 9 | 7 | the game |
| kernel: "the biggest, then bigger" | 45 | 8 | 7 | the game |
| endgames, and slack | 50 | 6 | 6 | the game |
| training ground | 45 | 7 | 8 | the hinge |
| alignment at three scales | 55 | 8 | 9 | the hinge |
| brakes: complexity vs understanding | 40 | 7 | 7 | the hinge |
| frame: Moloch and Leviathan | 45 | 7 | 6 | the frame |
| mirror: proposals read across the boundary | 45 | 7 | 9 | the frame |
| dilemma: "we need to win" | 50 | 8 | 8 | the frame |
| relations first | 40 | 8 | 6 | another way to see |
| 心 and 理 | 50 | 6 | 4 | another way to see |
| acceleration needs a direction | 40 | 7 | 7 | another way to see |
| trust before verification | 50 | 7 | 9 | what follows |

## The frontier

31,360 coherent configurations; 202 are Pareto-optimal on (time, F, R). Along the frontier, picking the best point at each time budget by 0.45 F + 0.55 R (reception weighted a little higher for a mixed room):

| budget | uses | F (of max) | R (of max) | cut |
|---|---|---|---|---|
| 10 min | 10.0 | 60% | 61% | film, agenda, minds, boundary, endgames, training, frame, 心/理 |
| 12 min | 11.8 | 75% | 73% | film, agenda, endgames, brakes, frame, 心/理 |
| 14 min | 14.0 | 88% | 85% | film, agenda, minds |
| 15 min | 14.9 | 94% | 89% | film, agenda |
| 16 min | 15.8 | 95% | 94% | agenda, 心/理 |
| 17 min | 16.7 | 99% | 97% | agenda |
| 18 min | 17.2 | 100% | 100% | none |

Read per minute, the best value is in *trust*, *mirror*, *direction*, *brakes*, *training*, *dilemma* and *scales*; the weakest is the agenda, then the film, the 心/理 slide and the endgames. The film is the most expensive slide by far, so a pure optimiser cuts it below 16 minutes. Ren had already chosen to keep a short excerpt, so the decision below holds it fixed.

**Robustness.** With the film fixed, every score perturbed by up to ±1.5 and the reception weight drawn from 0.40 to 0.70 (300 draws per budget), the share of draws that keep each slide:

| slide | ≤ 15 min | ≤ 16 min | ≤ 17 min |
|---|---|---|---|
| agenda | 0% | 0% | 1% |
| 心 and 理 | 0% | 40% | 99% |
| endgames | 7% | 63% | 100% |
| minds | 94% | 99% | 100% |
| every other slide | ≥ 99% | ≥ 99% | 100% |

So three results are robust: the agenda goes at any length; every slide that addresses the room directly (training ground, three scales, brakes, the frame, the mirror, the dilemma, direction, trust) stays at 15 minutes and up; and 心/理 and the endgames are the swing slides between 15 and 17 minutes.

## The title

| title / subtitle | clarity cold | fidelity | mechanism before conclusion | memorable | low misreading risk |
|---|---|---|---|---|---|
| No Safe Way to Win / Competition, AI, and the logic we are about to build into it | 8 | 9 | 3 | 9 | 5 |
| **The Game of Winning** / Competition, AI, and the logic we are about to build into it | 7 | 8 | 9 | 8 | 9 |
| The Game We Are Building AI Into / Why no one can win it safely | 8 | 8 | 7 | 6 | 8 |
| Why the Race Cannot Be Made Safe | 9 | 8 | 5 | 6 | 6 |
| Selecting the Selectors / How competition chooses the minds that build AI | 5 | 8 | 9 | 6 | 9 |

All five are non-dominated. "The Game of Winning" scores highest under weights 0.25 / 0.20 / 0.15 / 0.20 / 0.20 (8.1, against 7.1 for the old title). It keeps Ren's rule that a mechanism comes before its conclusion. It shares a name with the film the audience sees next, which was itself chosen over "The Game of Superintelligence" because the cause is the game, not the technology. And "No safe way to win" is not lost: the full-slide statement at 9:30 lands it after the mechanism has earned it.

## The decision

- **About 16 minutes**, at 140 words a minute. This is the knee: 95% of the fidelity and 94% of the reception for 92% of the full length. It leaves four minutes of a 20-minute slot for questions.
- **The film stays** (Ren's choice), from the card "One star is not enough" to the end.
- **The agenda and 心/理 slides are hidden, not deleted**, and their points are folded into the notes of neighbouring slides. This is a better point than the frontier itself offers, because it keeps most of each slide's fidelity at about 15 seconds of time instead of 35 and 50:
  - the agenda's point (a good theory predicts; the outcome is in nobody's interest) is now in the film slide's notes;
  - 心 and 理 as one dynamic is now one sentence in the notes of *Start from relations*.
- **Title**: "The Game of Winning". The deck is renamed "The Game of Winning (talk)".
- **Other lengths**, all one switch away:
  - 17 minutes: unhide 心/理, and drop its sentence from the notes of *Start from relations*.
  - 15 minutes: also hide the endgames slide.
  - About 12 minutes: also hide the film, *brakes* and *frame*. This matches the 12-minute frontier point.

  When the agenda is unhidden, drop its sentences from the film slide's notes.

  The timing cues in the notes are for the 16-minute version.
