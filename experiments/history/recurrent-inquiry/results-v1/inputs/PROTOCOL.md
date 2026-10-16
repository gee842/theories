# Recurrent inquiry and successor evidence

Exploratory exact decision calculations, 5 October 2026. This study has two separate modules. It is not an integration of paid succession into the preceding candidate-discovery simulator, and it makes no held-out empirical claim.

## Questions fixed before calculation

1. Can paying to keep inquiry available be strictly preferable when testing now has no value?
2. Does adapting capacity expenditure to diagnostic experience improve decisions relative to the best fixed calendar? Compare both equal per-period feasibility and a matched expected inquiry expenditure constraint.
3. How does an old warranted negative result lose relevance under known environmental change?
4. When does paid transmission improve a successor's decision after accounting for other visible traces and the information in silence?

## Module A

A binary hidden need follows a symmetric Markov chain with known switch probability h. Treatment costs c and prevents a loss L that would otherwise occur in state one. Treatment does not change the transition law. The evaluator observes consequences, but the controller does not observe untreated loss, the state, or a state-dependent resource balance. Without this restriction there can be free diagnostic information.

A diagnostic costs d and is possible only when inquiry capacity is ready. With probability s it reveals the current state without error; otherwise it returns an explicit uninformative failure symbol. Success is independent of need. A warranted negative result is thus distinct from a failed diagnostic. This specified diagnostic is an isolation assumption, not newly generated explanatory knowledge.

After the diagnostic, keeping ready capacity for the next period costs m. Rebuilding absent capacity costs K and takes one period, so it cannot enable a current test. Declining either leaves capacity absent next period. The inquiry procurement cap B applies to diagnostic plus upkeep/rebuilding in each realized branch. Ordinary treatment has a separate ample operating budget. All treatment, untreated loss, diagnostic, upkeep, and rebuilding costs enter the common objective with declared unit weights.

The posterior is retained for free in this module. No successor reset or paid archive is claimed here. A finite-horizon Bellman calculation chooses tests and future capacity from the available posterior; it knows the supplied model. This is endogenous allocation within a fixed decision rule, not the endogenous emergence of that rule or its purposes.

The baseline comparison chooses the best capacity calendar before any test result while allowing equally adaptive diagnostics and treatment. A separate linear program compares against the best ex ante lottery over those calendars, with adaptive randomized tests and the same expected inquiry expenditure bound as the adaptive solution. Treatment remains Bayes-optimal and receives no private information advantage. Spending is matched in expectation, not path by path; unused allowance is not expenditure.

The short exact certificate is specified analytically: two periods, initial known-negative state and ready capacity, h=.2, L=10, c=4, diagnostic cost1 and success1, upkeep .1, rebuilding2, procurement cap3. A current diagnostic has zero information value. Maintaining permits next-period loss1.8 rather than2, so total1.9 beats2. The loss is lower by .1 after upkeep.

Longer parameter examples and sensitivity calculations are exploratory conditional illustrations. Parameters and all evaluated examples will be saved, including cases with no adaptive advantage. No selection of favorable cases will be called preregistered evidence or used for a statistical significance claim.

## Module B

A predecessor knows a past binary state. A successor sees a public cue about it and any delivered truthful message. The cue channel, state prior, elapsed time, Markov law, and communication protocol are common knowledge. Evidence aging uses the same known transition law, not an unconditional reset.

The parties choose whether to establish a communication opportunity from public information before private-state-dependent disclosure. Establishment costs f0 even if no message is sent. A truthful message costs f when attempted. A delivery failure is indistinguishable from intentional silence; its known probability is independent of state. The successor updates from both the visible cue and the presence, content, or absence of a message. There are four deterministic disclosure rules per cue: send neither, only zero, only one, or both. Enumerating these is exhaustive for this one-step team decision; randomizing over agreed rules cannot improve its minimum linear expected cost.

The example family fixes prior .5, L1, c.4, h.1, setup .02 and message .1, while varying evidence age, cue accuracy, and delivery reliability. Fully revealing cues should remove the incremental benefit of an archive. Reliable selective disclosure can make silence informative; delivery failure weakens that result. This module charges a one-time handoff, not indefinitely maintained archives, training, or endogenous succession.

## Verification and limits

Check the analytic two-period certificate, posterior transition, accounting, branch feasibility, independent forward evaluation of the chosen policy, and linear-program flow and budget residuals. Compare Bellman and linear-program values when the budget does not bind. Check the communication calculation against direct joint probability enumeration, full-cue redundancy, informative silence, and unreliable delivery.

Retain source hashes, numerical settings, all example outcomes, and a scientific figure. These finite-model conclusions are standard decision-theoretic reasoning specialized to this research question. They do not establish a universal optimum, real institutional performance, a societal attractor, or a solution to value formation and AI alignment.
