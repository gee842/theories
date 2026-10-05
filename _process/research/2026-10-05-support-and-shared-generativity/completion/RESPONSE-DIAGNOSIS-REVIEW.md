# Independent review of the construction-response diagnosis

5 October 2026. AI-assisted review of the selected g=8, H=3, original joint profile (1,1,1). **The finite response identity and its net numerical implementation pass this review.** The negative result remains a result about this preparation, reaction network and assay. This is a posthoc diagnosis of a known failure, not a new prospective test of a favorable direction.

## Reading and independent check

Read the full [response proof](REGULATION-RESPONSE.md), frozen regulator producer, diagnostic protocol, diagnostic producer and explanatory README; inspected the saved decomposition summaries, groups, time bins and leading state contributions. The [new checker](../../../../experiments/shared-renewal-capability/regulation/response/independent_check.py) imports only the earlier **independent** reaction reconstruction, never either producer. It rebuilds integer generators and uses its own sorted state order. The [machine-readable check](../../../../experiments/shared-renewal-capability/regulation/response/independent-check.json) records every input hash, software versions, tolerance and output.

At cap 48, the common responsive graph contains 6,584 states, including 2,284 construction-eligible states. The baseline keeps both association constants at 4 and removes only construction. This is essential: using the named absent arm on hypothetical G-containing states would change additional reactions. From the common zero-G initial state, this conditional baseline agrees with the absent arm.

Exact integer checks confirm common-graph closure, zero row sums, and the full identity Q1−Q0=B, where B includes both the construction jump and its negative diagonal. Construction preserves material, lowers free-plus-bound fuel U and assigned work W by 1, and lowers productive material A by 1. Its terminal assay contrast is nonpositive. All construction-eligible states already have a recycling flag under this preparation; assembly likewise implies recycling. These flag implications are preparation-specific, not general properties of arbitrary states.

The A=0 face is invariant. In the 382 reachable states where construction consumes the last productive unit, its target therefore has zero future assay success for every remaining horizon. This supplies an exact nonpositive contribution for that class, independent of time integration. In the baseline, total regulator material G+GF+YG has drift minus its own count, so the retained binding law creates no new gate material.

## Net identity without time quadrature

For function-column generators, apply the exponential of

\[
\mathcal M=\begin{pmatrix}Q_1&B\\0&Q_0\end{pmatrix}
\]

to the column (0,f). Its lower block is P0(H)f; its upper block is the Duhamel response. The latter must equal P1(H)f−P0(H)f. This block matrix itself is not a Markov generator.

The independent calculation gives:

| Quantity, cap 48 | Value |
|---|---:|
| Baseline success | 0.6925433833168245 |
| Responsive success | 0.1987903017280950 |
| Block response | −0.4937530815887266 |
| Initial-state identity residual | 3.00e−15 |
| Maximum identity residual across all states | 8.66e−15 |

The largest discrepancy from the primary endpoint values is 6.42e−15, below the disclosed 1e−10 comparison tolerance. Both implementations use SciPy matrix-exponential actions; this check changes the reconstruction and response calculation, not the numerical library. No roundoff enclosure is claimed.

The primary 768-interval integral differs from this block result by about −5.14e−10. At cap 64, its saved endpoint difference is −0.4937530830721258, a cap shift of−1.48e−9. Every saved cap 64 group and time-bin net is negative. The last-productive-unit group contributes approximately 19.25% of the net under this decomposition. These grouped and sign-separated integrals were inspected, not independently re-integrated.

## Conditional boundary values require their own error control

The small positive integrated terms do not establish beneficial construction in the unbounded process. At one unit of remaining time, the independently computed largest cap 48 construction contrast occurs at physical state (R,C,Y,D,F,G,GF,YG)=(1,2,0,0,48,0,0,0), with assay flags already satisfied. The stopped contrast is +0.2082934. Conditional overflow is 0.3288732 before construction and 0.1013830 after it.

For a local stopped contrast deltaK=uK(Tz)−uK(z), the same coupling argument yields

\[
\delta_K-o(s,z)\le\delta_\infty\le\delta_K+o(s,Tz).
\]

Using these floating values gives approximately [−0.12058,0.30968], which does not determine the original-process sign. This is an illustration of truncation uncertainty, not a rigorous numerical interval. Spending a packet can reduce artificial overflow substantially near the boundary. Small overflow from the actual initial state does not control such conditional values. Conversely, tiny integrated positive values do not prove an exact zero or global nonpositivity.

## Interpretation and provenance

The response includes all downstream consequences of construction. It is not a separation into a pure fuel cost, material cost and control benefit. Reversing the valid semigroup ordering changes state/time attribution while preserving the total. The mechanism-specific negative result is sound; a claim that every construction is harmful would exceed it.

The original eight assays describe inherited plant functions. They do not test a new delivered regulation function. Consequently this result neither establishes a universal decline of generativity nor orders every possible future capability. A common expanded functional vocabulary and an independently specified productive conflict are needed before testing whether regulation solves that conflict. Physical success would still not by itself establish an ethical ordering.

Check-time HEAD was `9aa1b3ab1623b824082d6b5a1da2b2f22d3e29da`; the new response files were uncommitted. The checker verifies every recorded producer input hash. The original diagnostic protocol hash matches the preserved `PROTOCOL-at-run.txt`; the current protocol differs by exactly the single relative-link replacement recorded in `protocol-link-repair.json`. No scientific setting changed. Complete SHA-256 values are preserved in the linked check JSON, including the primary results hash `ee23df652c8b7f53d81ab4892669fa201b3890ba4e8835ee8a04959776771df6`.
