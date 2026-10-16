# Revisable inheritance with paid inquiry and public signals

Exploratory exact finite decision study, 5 October 2026. It examines which retained observations permit reinterpretation under an expanded model, while jointly choosing archive inspection, readiness, disclosure, and a current diagnostic. It does not test a universal claim that history repeats or never repeats.

## Information chronology

A four-transition binary history begins in an independent fair state. Its last state Z is publicly available from a routine observation. Earlier switch bits may be retained in one of four formats fixed before the path is seen: last state only (no private bits), total switch count (3 bits), two half-window switch counts (4 bits), or the full ordered switch word (4 bits). Retention has a price per bit. Timestamps, length, and the midpoint are common known metadata; omitting them would be a different information experiment.

At handoff a model family and its prior are supplied to both parties. This is explicit model admission, not spontaneous discovery or ordinary Bayesian updating out of zero prior support. Three families are examined: constant slow or fast rate; slow then fast or fast then slow; and the expanded union of all four. Slow=.05 and fast=.45; priors are uniform within each family. The final regime determines the next transition, when the successor acts. The selected generating model remains fixed for a history, though its rates can change within that history; the model index is not redrawn each step.

Format comparisons are conditional evaluations of already retained records. Choosing the lowest-loss format with hindsight about the later model family is labeled a best-format benchmark, not an achievable earlier policy without a prior over future model admission.

After seeing public Z, the caretaker chooses whether to pay to inspect the retained private statistic. Declining inspection leaves only the correctly computed cue-conditioned prior. This is an endogenous inquiry choice. A record that has already discarded ordering cannot yield that ordering when inspected. The caretaker also chooses whether to open a reliable message opportunity, paying its fixed setup fee even if no payload is sent; opening and inspection choices occur before the private statistic is read and are public.

After inspection, the caretaker chooses next-period ready capacity (at a maintenance price) and whether to transmit the retained statistic if the channel was opened. These choices may depend only on information actually retained and inspected. The successor sees Z, format, inspection and channel-opening flags, readiness, and the truthful payload or silence. Readiness and silence are information channels. Attempted-message fees depend only on these visible choices, so no extra hidden bill conveys an omitted signal.

At the next decision, ready capacity permits a perfect paid diagnostic of current need. Absent capacity cannot be rebuilt before this decision. The successor chooses no response, response, or diagnostic followed by response exactly when needed. Response costs .3 and avoids loss1 if need is present. The common loss criterion and perfect diagnostic are supplied assumptions. There is no passive signal of current need before choosing. History does not determine the next state with certainty.

## Resource and optimization rules

The branchwise inquiry cap covers sunk retention, archive inspection, message-channel setup, readiness, payload, and any current diagnostic. It is a total episode budget on each realized path, not a per-period cap. Response has separate sufficient funding; its cost and untreated loss are counted in total loss. Unspent allowance is not a cost. A ready capability may also convey information even when its diagnostic is not exercised; costs and this informational role must be reported separately.

For fixed public information, inspection choice, and channel-opening choice, enumerate the successor's two possible actions after silent absent capacity and three after silent ready capacity. A transmitted statistic reveals the caretaker's entire private type, permitting its best feasible response to be computed directly. For each of these six silent decoder pairs, independently choose the cheapest feasible readiness/transmission action for each private type. This is an exhaustive finite-team minimization with additive expected costs and branchwise constraints. It is not a learning algorithm or an account of how a shared protocol emerges.

Controls forbid payloads, fix readiness before private information, forbid the current diagnostic, or remove prices. All receivers condition on their actual information. A constrained sender is not compared to an artificially ignorant successor. Store each selected prescription, receiver posterior, cost component, and branch feasibility result.

## Anticipated checks and boundaries

Under constant-rate uncertainty, final state plus total switch count should have the same gross decision information as the full ordered path. Under the equal-half ordered family, total count has exactly the same distribution under both regime orders; it cannot identify whether the final regime is slow or fast. Timed counts retain that distinction. Equal-price timed and full records should give equal optima for the declared families. This does not establish sufficiency under every future model or the universal desirability of raw storage.

Independently compare the decoder method with exhaustive sender-rule enumeration on small instances; verify Bayes posteriors, normalized likelihoods, inquiry charges, public-signal inference, and branch caps. Preserve all exploratory parameter cases and revisions. These are exact conditional numerical expectations, not randomized empirical trials, held-out evaluation, or evidence about historians' beliefs.
