# Declared structural verification supplement

5 October 2026. Recorded after the structural theorem and its example were written, before the producer's structural computation. The expected answers follow analytically from that example; this is a verification specification, not an empirical preregistration.

Use exactly the ten Boolean coordinates, sixteen proposal inputs, four joint-noise realizations and equations (3) and (5) in [STRUCTURAL-CLOSURE.md](formal/STRUCTURAL-CLOSURE.md). Keep every right-hand side on the old state and reuse the same disturbance bit wherever specified. Use exact rational probabilities.

1. Trace the listed parent sets from `{b,v,p}`. Expect retained-set sizes `3,7,9`, followed by no change. The badge is the only omitted coordinate.
2. Independently derive the actual Boolean input dependencies by flipping each old-state coordinate across every state, proposal and noise branch. Compare with the listed parent sets. This tests dependencies of these supplied functions, not a universal causal discovery procedure.
3. For every pair of states differing only in the badge, and every proposal, compare exact distributions of the retained next state. Expect equality for all `512 × 16` pairs. Do not multiply separate coordinate marginals.
4. Reconstruct the omitted-maintenance witness. Two seed-identical states must give next-burden probabilities zero and one quarter.
5. Add only the badge-dependent authority mode. Expect the closure to include all ten coordinates and the old nine-coordinate projection to fail. Exhibit the authority difference and a later difference in the original protected burden, showing why an internal difference can matter to the original question.
6. Record result and source hashes. A separate agent's independently written branchwise check is reported separately. Counts indicate exhaustive finite comparisons, not empirical replications or general theorem proofs.

No parameter search, data fitting, attractor claim, or claim that all nine retained coordinates are semantically indispensable is authorized by these checks.
