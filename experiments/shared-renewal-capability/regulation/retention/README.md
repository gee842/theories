# Paid response formation, support access and retention

6 October 2026. Executable implementation of the [analytical reaction law](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-MATH.md), advancing the [first derivation gate](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#first-acceptance-gate). AI-authored research under Ren's direction. The [protocol](PROTOCOL.md) records the comparisons before this implementation was run; the main fixture had already been chosen analytically.

The process begins with damaged capture sites, precursor, two usable fuel units, two incident source units and no assembled regulator. Damage catalyzes paid formation. A regulator can repair a capture site at further cost; that site can then obtain fresh fuel, which can pay for copies of the regulator. No analyst's reward enters the law. This is a formation/repair/retention mechanism under supplied chemistry, not origin of the reaction repertoire or a learned selector.

## Results and their limits

The following are rounded readings of the outward enclosures in [results.json](results.json), at H=12 with the same damaged initial state. Site occupation is expected integrated intact-site count, bounded by 12 in this one-site fixture.

| Arm | Copies | Fresh captures | Site occupation | G at H |
|---|---:|---:|---:|---:|
| Active repair | 0.799827 | 0.399928 | 2.325206 | 2.197305 |
| Repair disabled | 0.499958 | 0 | 0 | 1.997601 |
| Equally paid ineffective repair | 0.399971 | 0 | 0 | 1.797849 |
| Capture disabled | 0.399971 | 0 | 2.325145 | 1.797849 |
| Capture burns incident fuel | 0.399971 | 0 | 2.325145 | 1.797849 |
| Copying disabled | 0 | 0.666537 | 3.832084 | 1.664995 |
| Constitutive formation | 0.633231 | 0.399928 | 2.325182 | 2.197346 |

The active process gains more than the analytical lower bound 53/1250 expected copies over repair-disabled dynamics. With no incident source, active repair instead yields 0.399971 copies versus 0.499958 without repair, verifying the adverse bound 153/2500. Zero-loss terminal copy expectations are exactly 4/5, 1/2 and 2/5 for active, disabled and ineffective repair. Positive-loss terminal expectations are also computed exactly as rational numbers.

Removing formation or using the wrong cue prevents regulator formation from this entirely damaged preparation. Starting with fewer than two usable fuel units prevents repair and capture despite available incident support. These statements follow structurally; numerical zero enclosures supplement the invariant rather than replacing it.

**Retention is not a universal success metric.** Disabling copying increases fresh captures and intact-site occupation in the main fixture, since it frees fuel for repair and formation. Active formation yields more copies than constitutive formation while their endpoint regulator stocks are nearly equal; route labels are different from total retained capacity. In the initially intact preparation, constitutive formation produces more regulators and captures over this horizon. The study therefore establishes the stated causal return and its comparison-specific effects, not dominance of feedback, more useful behavior in every task, or an ordering of all future possibilities. Incident consumption also depends on free storage: capturing more is not automatically better preservation of usable resources.

## Actual-successor interventions

From the explicit post-repair state (C,G,F,E)=(1,1,0,2), disabling capture for four time units and restoring it for eight yields about 1.996527 copies. Permanent disruption yields zero; uninterrupted capture yields about 1.999440. The first episode's distribution, including wear and damage, is passed to the second. Nothing is refilled or reset. Likewise, restoring the damage cue after a four-unit disruption produces formation and copying, with the fuel losses and shortened response time retained. These are interventions in an authored law, not laboratory observations.

The split calculation under an unchanged law encloses the same outcomes as its unsplit calculation. This verifies the implementation's use of the actual successor distribution in the tested case, not a universal theorem about arbitrary numerical code.

## Exact and numerical verification

[model.py](model.py) enumerates the finite reachable graph. For every admitted event, the integer rank

\[
4E+2F+C+G
\]

strictly decreases. Damage and wear reduce it by one; formation, copying and successful repair reduce it by one; capture, leakage and ineffective repair reduce it by two; incident burning reduces it by four. Thus exact rational backward recursion gives terminal expectations even with positive losses. No state truncation or simulation sample is used.

Finite-time expectations use uniformization at an integer rate at least the largest exit rate. Every operation on nonnegative probability and reward intervals is rounded outward using 60-digit decimal arithmetic. A rational Taylor sum and geometric remainder bound enclose exp(−λH). A geometric Poisson-tail bound accounts for omitted terms. Each event count is bounded by the initial rank; the intact-site time tail uses the Poisson first-moment identity. The implementation assumes the usual finite-state CTMC construction; its numerical semantics are not Lean-verified. Source hashes identify the actual checked program and protocol.

Run from this directory:

```sh
python3 check.py
python3 independent_check.py
python3 formal/check.py
```

The first command writes [results.json](results.json), including all nine intervention arms, twelve diagnostic comparisons, exact terminal expectations, the constructive six-event path, analytical rational certificates and successor-state interventions. The second is a separately written stoichiometric and numerical check; consult its record and the [internal review](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-REVIEW.md) for scope. The final command checks arbitrary event-trace properties of the declared law with pinned Lean; it does not certify CTMC probabilities or Python refinement.

## Contribution and next bridge

The subsequent [formed-variant study](formation/README.md) now starts with neither response type present and joins paid formation, association and mixed copying under one continuing resource history. Its [integration audit](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-INTEGRATION.md) advances the next task to formation and revision of the selection mechanisms themselves. This is a new declared law; the earlier study and its scope remain intact.

This round checks a conditional causal loop from initially absent response to consequence-dependent material reconstruction. Formation, operation and copying spend actual fuel. Its failures include bootstrap exhaustion, loss of productive support and competition between copying and continued repair.

The [shared-pool neutrality result](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-REVIEW.md#why-this-does-not-yet-derive-selection-of-useful-responses) remains decisive: useful repair can fund an ineffective competitor just as readily. The next bridge concerns differential return to actual alternative responses and, later, how sensing and selection mechanisms themselves change. The [gate audit](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REGULATION-RETENTION-INTEGRATION.md) accepts the first conditional causal-loop milestone. A physical scaffold, response repertoire, copy specificity and storage capacity remain supplied; empirical identification and the wider derivation remain open.
