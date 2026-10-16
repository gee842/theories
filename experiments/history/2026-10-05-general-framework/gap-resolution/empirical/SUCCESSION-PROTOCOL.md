# Frozen exploratory one-round information-to-investment test

5 October 2026. This new question was proposed **after** the contemporaneous results were known. Its design is frozen before constructing person-level lagged outcomes or estimating any lagged effect. It is a separate exploratory analysis, not a retroactive primary endpoint or an independent confirmation.

## Question and design

In Experiment 1 of Dickson, Gordon and Huber (2022), does a person's experience of the randomized higher-accuracy draw at round t change their choice to make the big accuracy investment if assigned authority at round t+1? Use the already downloaded, hash-verified CC0 file. No new datasets.

Join the same person by session and subject across exactly adjacent rounds t=1,...,19. Current exposure is Z=`g_accuracy-e_biginvestment` at t, a fair draw conditional on the authority's preceding investment. Include current citizens and current authorities. Retain only people assigned authority (`z_isenforcer==1`) at t+1. Outcome Y is that person's binary `e_biginvestment` at t+1. Do not condition on later accuracy, enforcement, contribution, earnings or earlier chosen investment. Verify all participant-period rows are unique, all required adjacent rows exist, treatment is binary, and next-round authority counts are fixed as specified by group size.

The article says group and role assignments are randomized anew after each period. For this causal interpretation we specifically require that those assignment draws ignore past accuracy and behavior, and that treatment does not affect participation or availability. Next-role selection is then externally randomized rather than a behavioral mediator of the earlier draw. A fixed number of authority places makes the eligible count fixed within each session. If data or documentation contradict this, stop and report the identification obstruction. The archived assignment algorithm itself is not available for an independent random-number audit.

Z remains randomized conditional on the authority's preceding investment even when the currently exposed person was that authority. The effect can operate through payoffs, prior punishment, attention, beliefs or other experience; it does not isolate a cognitive mechanism. Random role assignment supplies who can act next; it is not evidence for endogenous institutional selection or organic succession.

## Fixed estimand and inference

For every eligible person-round, compute 2(2Z−1)(Y−0.5). Average within each session, then average sessions equally, exactly as in the contemporaneous protocol. This is a two-sided exploratory effect; neither a positive nor negative direction is assumed in advance. Interpret it as a one-round effect under the experiment's mixed past histories and randomized next-role process, not as the effect of changing every historical draw or a long-run rule-selection policy.

Use the six session estimates for an approximate Student-t 95% interval with five degrees of freedom, and report leave-one-session-out estimates. Session-level clustering encompasses repeated people and the shared treatment of prior group members. Report the group/person-opportunity-weighted score, raw treated/control investment rates, role counts and each session effect as descriptive checks. No individual-row standard errors, exact randomization p-value, power-based equivalence claim or selective participant exclusions.

Only this single lag, endpoint and full eligible population will be tested. Do not try other lags, current-role subgroups, quiz filters, alternate outcomes or fitted models after observing the result. Preserve null, negative or unstable findings. Missing main outcomes or unresolved assignment coding stops the analysis; no imputation.

## Scope and provenance

A detected effect would support one bounded experience→later chosen information-investment link under external assignment. A null would leave that proposed link unsupported at this horizon and resolution, not prove its universal absence. Neither result establishes funded infrastructure persistence, endogenous successor selection, commitment formation, shared ecological dynamics or a validated general theory. Save joined rows, code, all session estimates, protocol/data hashes and results separately from the original primary intervention analysis.
