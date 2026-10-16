# Why the constructed regulator loses the original joint test

This secondary analysis applies the proved [reaction-response identity](../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REGULATION-RESPONSE.md) to the failed g=8, H=3 joint assay. It identifies where the loss occurs in one declared response decomposition. It does not choose a new favorable model, collect observations, or attribute a unique intrinsic value to each reaction.

The [diagnostic protocol](PROTOCOL.md) was written before this calculation, after the original negative result. [decompose.py](decompose.py) and [results.json](results.json) retain every resolution and packet cap. The original experiment is unchanged.

One relative link in the protocol was repaired after the calculation. [PROTOCOL-at-run.txt](PROTOCOL-at-run.txt) preserves the exact bytes whose hash the results record; [protocol-link-repair.json](protocol-link-repair.json) records the sole link replacement and both hashes. Scientific settings are unchanged. The independent checker verifies this provenance as well as the numerical identity.

## The net effect and its accounting

The test requires recycling, C assembly, a free packet and surviving productive material. At packet cap64, the computed unregulated and regulated success probabilities differ by **−0.4937530831**. Integrating the construction reaction's conditional future-success contrast gives **−0.4937530836** at 768 time intervals. The numerical identity residual is about **5.14e-10**. This is ordinary floating-point and quadrature agreement, not a rigorous interval enclosure.

The baseline conditional futures retain all fuel and Y binding reactions but disable further construction. The outer state frequencies come from the fully constructing process. From the common initial state, the conditional baseline is exactly the absent-regulator law because no G can appear there. Keeping its behavior defined on G-containing states is essential for the identity.

The construction event consumes usable R and F, and all its downstream consequences appear in the conditional contrast. Its contribution includes altered sequestration, inhibition, wear, capture and production. The integral does **not** isolate a pure energetic cost from a pure control benefit. Another valid semigroup ordering would assign different time/state contributions while preserving the same total effect.

| Productive material before construction | Capture machinery C present | Integrated contribution |
|---|---|---:|
| 3 units | Yes | −0.133946 |
| 3 units | No | −0.019658 |
| 2 units | Yes | −0.203708 |
| 2 units | No | −0.041375 |
| 1 unit | No | −0.095066 |

The last row has an exact structural explanation: construction requires R>=1. If only one productive unit remains, it is R; turning it into G reaches the invariant dead-plant face A=0. The constructed state then has zero chance of passing this assay at any later time under this repertoire. Its response contribution is nonpositive independently of numerical approximation. Under the chosen decomposition, these transitions account for approximately 19.3% of the total negative effect; that percentage is not a unique partition into fundamental causes.

All five prespecified time bins have negative net contributions. No integrated positive state contribution exceeds the declared reporting threshold 1e-12. This observed finite calculation is not a proof that every construction state has a negative conditional contrast or that constructing any regulator is harmful.

## Why apparently positive boundary states are not evidence of useful regulation

The largest positive conditional construction contrasts occur near the artificial packet cap. Construction spends a packet and can delay hitting the artificial overflow-failure state. Such a conditional contrast can be sizable even though occupation of that state from the actual preparation is extremely small.

At cap48, the integrated positive part is about 2.18e-12. At cap64 it falls to approximately 1.70e-19, with the largest positive state contributions at free-packet counts62–64. These values are smaller than the numerical accuracy claimed for the net effect. They do not demonstrate a real positive contribution in the original unbounded process. We also do not infer an exact zero or a global sign theorem from small floating values.

This is a useful distinction: a small overflow probability from the initial preparation protects the endpoint comparison, but does not make every conditional value near the truncation boundary accurate. Individual state attribution requires its own care.

## Numerical verification and remaining scope

The initial 192-interval result missed the endpoint difference by 1.34e-7, triggering the protocol's declared refinement. Residuals fell to 8.25e-9 at384 intervals and 5.14e-10 at768. All runs are retained. Moving the cap from48 to64 shifts the endpoint difference by about1.48e-9. These sensitivity checks are empirical numerical diagnostics, not proved roundoff or quadrature bounds.

The implementation checks the full construction increment including its generator diagonal, a common closed state space, the impossibility of a positive terminal construction contrast, zero future success after consuming the last productive unit, and the preparation-specific implication that construction-eligible states already include a recycling event. The [independent response review](../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/RESPONSE-DIAGNOSIS-REVIEW.md) records a separate block-matrix calculation and its scope.

The remaining theoretical issue is more basic than tuning inhibitor strength. In the original law, recycling converts a leaking fuel packet into usable R without losing the assigned work value. It does not compete with a second modeled productive fuel use. A loss of free reserve is therefore not yet a demonstration of impaired later production. A proposed regulator needs an independently specified harmful reaction or resource conflict to resolve, and new functional claims need a common expanded assay vocabulary.

Return to the [original regulator comparison](../README.md) and the [completion plan](../../../../theories/becoming/history/COMPLETION-PLAN.md).
