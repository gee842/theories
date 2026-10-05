# Costed selector revision and conventional feedback

6 October 2026. AI-authored protocol written before the numerical comparisons, following Ren's request to execute the selector-revision milestone. This is a new conditional process within the existing study, not an exact kinetic refinement of the preceding molecular construction. No chemical identification or historical-priority claim is supplied.

## Question and supplied mechanism

Can one continuing compartment change the rule that selects reconstructed responses, through actual consequences of those responses, while paying formation, sensing/work and renewal costs? Compare against explicitly costed conventional controllers with the same information, resources and replacement opportunities.

A selector token has orientation `m` in {0,1} and remaining lifetime `ell` in {0,...,L}. On encountering sensory bit `b`, it reconstructs response `b XOR m`. The external condition `z` makes response `b XOR z` productive. The selector and all controller policies receive no `z`, reversal time or future packet information. Actual fuel capture is their consequence signal. Cue transduction and response reconstruction jointly cost `d`; the basic case uses one unit for each, `d=2`.

The compartment initially has no selector, reserve `F0`, one recyclable selector precursor and a finite stream of `H` source packets, each worth `G` fuel units. An absent or expired selector can be assembled at cost `c`. At expiry its old orientation remains observable in its residue until reconstruction; every controller has the same access to that residue. The primary law samples either orientation with probability one half. Orientation changes alter an input-to-response mapping, not merely population counts.

Each exposure permits assembly if needed, followed by at most one paid trial. This is a coarse timing convention: it charges assembly fuel but gives it no additional whole exposure of latency. A finer timing model must charge any additional delay. Trial payment precedes capture. Captured fuel pays `r` units for template-preserving selector renewal, restoring lifetime `L`. Without capture, lifetime decreases by one. Assume `G>=r` so any captured packet can fund renewal. At all stages previously spent fuel remains spent. If assembly leaves too little for the trial, its payment is not rolled back.

Packets arrive on an external clock. Each exposure spends one of the initially counted source packets. A mismatch, unavailable packet, or inactive compartment spills the entire packet to waste; no inactive controller accrues a hidden store. This boundary assumption matters. No selector or reserve is reset at a condition reversal. The finite source cannot support indefinite continuation.

## Controllers and interventions

All competitive arms share the same candidate orientations, replacement times, costs, initial state, cue stream, hidden-condition prior and packet law. Their policies receive only current reserve, current/expired orientation and lifetime; they can observe past actual returns. No competitive policy uses the hidden regime or reversal clock.

1. **Material random renewal:** unbiased paid assembly; actual capture pays for same-type renewal; failures wear the selector. This is the proposed mechanism.
2. **Conventional random-restart automaton:** separately expressed conventional feedback law with the same probabilities. Exact equivalence is the prediction; equality is not a performance win.
3. **Directed failure feedback:** initial assembly is unbiased; after expiry, assemble the opposite orientation. It has the same action menu, replacement opportunities and prices. Its selective assembly coupling is a supplied alternative controller architecture, just as the primary random assembly coupling is supplied. It has no oracle and no extra memory beyond the shared residue.
4. **Fixed mapping:** unbiased initial orientation, always reconstruct the same expired orientation. This is an ablation, not the strongest comparator.

A separate **outcome-blind renewal** intervention replaces capture-gated renewal with an independent fair renewal coin, charging `r` from the actual available reserve. Capture still supplies actual fuel. This changes the physical renewal coupling; it is an ablation, not an information-matched competitive controller or a match of realized expenditures. If the coin requests unaffordable renewal, the token wears. It tests the role of consequence-sensitive maintenance.

## Declared cases and measurements

The primary case is `F0=9,c=1,d=2,r=1,G=4,L=2,H=12`; initial hidden condition has probability one half for each orientation. It reverses after four exposures. The cue alternates 0,1. It is identical across arms and conveys no information about `z`. Successful matching trials capture with probability `p=1`; robustness cases use `p=3/4` to permit misleading failure signals.

Before execution, declare primary, no reversal, two reversals (after four and eight exposures), noisy reversal, reserves 3/6/12, assembly cost 2, lifetime 1/3, and low-yield `G=3` cases. Do not select a winner after inspecting results. All probabilities and expectations use exact rational arithmetic over all paths, including failed formation and depletion.

Report unconditional paid trials, captured packets, remaining reserve, selector changes, renewals, captures after the first condition boundary, probability of any such capture, and ability to pay the next trial/assembly from the final actual reserve. The final readiness measure is a reserve diagnostic after the last packet, not demonstrated future survival. Also report the probability of capture on both sides of the first boundary, without conditioning on successful startup. No scalar score drives the transition law, and no one outcome is a universal success measure.

A separate within-compartment witness requires all three events in order: capture using one mapping before the boundary, a paid post-boundary assembly changing to the other mapping, and a subsequent capture using that new mapping. This excludes a previously unsuccessful fixed mapping becoming useful solely because the environment changes. It is counted unconditionally from the original absent-selector start.

Verify for every reachable history:

`reserve + assembly_spend + trial_spend + renewal_spend + spilled_source + remaining_source = F0 + H*G`.

No numerical stochastic simulation or fitted biological claim is involved. The program enumerates and sums the finite distributions. An independent implementation must reproduce the results without importing the producer's transition function. The exact-emulation conventional arm must agree as a complete physical-state distribution, not only in one mean.

## Sharp diagnostic and acceptance

A separate diagnostic starts immediately after a reversal with a now-unproductive selector of residual lifetime `k`, inherited reserve `F` and `T` opportunities remaining. This is explicitly conditional and does not replace the original-start comparisons. With deterministic productive capture, `j` failed candidate orientations before first useful orientation cost `C_j=k*d+c+d+j*(c+L*d)` before first capture and require `k+j*L+1` exposures. The number `N` of affordable timely candidate trials gives recovery probability `1-2^(-N)` under unbiased assembly. Check the exact threshold, including one unit below it, and finite-horizon constraints. Directed failure feedback has different recovery probabilities and must not be assigned the random formula.

Accept the local milestone only if selector-state changes alter the response-selection mapping in a persistent compartment, consequences pay for retention/revision without an observer reward, conditions change without resets, all prices and sources balance, and both conventional comparisons are retained. The immutable assembly/renewal chemistry, binary repertoire, sensor and scaffold remain supplied. This does not establish open-ended learning, learned evaluative representations, concern or historical novelty. Equivalence or inferiority to a conventional controller is an informative possible result.
