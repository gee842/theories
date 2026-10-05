# Exact finite verification results

5 October 2026. Constructed mathematical checks, not empirical data. General results are proved in [FORMAL.md](../formal/FORMAL.md) and [STRUCTURAL-CLOSURE.md](../formal/STRUCTURAL-CLOSURE.md). Computation checks the implementation and specified examples.

## Reduction and generation

The primary checker passes **744 named assertions**. These include repeated row checks and witnesses, not 744 independent scientific tests.

- Iterative refinement is checked against every set partition for 36 supplementary rational finite systems, plus constructed examples. The comparator checks stability and coarseness relative to every stable partition, not merely the smallest observed block count.
- A four-state example reduces to two blocks despite different fine transition rows. A five-state delayed example needs two refinement rounds and reduces to four blocks. Matching an immediate output alone is insufficient.
- An added intervention separates a previously merged pair. An added refusal distinction independently separates a pair with unchanged physical output.
- Programs composed from single-bit tests and writes, rational coin writes and sequencing reproduce supplied transition rows exactly. Old and next-state registers are separate, and old-state preservation is checked.
- Hidden guards and shared noise give explicit failures of unjustified composition. A bounded fair-coin program cannot produce probability one third exactly.
- Finite counter-prefix checks illustrate the proof that a two-rule unbounded counter has no finite exact sufficient-state quotient. The finite checks do not themselves establish the infinite result.

The [independent review](REVIEW.md) enumerates all 50,069 functions from n states into n states for n from one through six, constructs their fiber partitions, and verifies the producer's partition enumeration against them. The resulting counts are the Bell numbers 1, 2, 5, 15, 52 and 203. It separately reconstructs joint-noise and intermediate-transfer witnesses.

## Local structural mechanism network

The supplied ten-bit network has 1,024 states, sixteen proposal inputs and four joint-noise branches. Some updates share the same disturbance. Exact distribution comparisons sum whole joint outcomes, without assuming independent coordinate effects.

| Verification | Result |
|---|---|
| Dependency closure from burden, veto and eligibility | 3 → 7 → 9 coordinates; badge omitted |
| Retained coordinate states | 512; sufficient, not claimed semantically minimal |
| Exhaustive paired transition-distribution comparisons | All 8,192 equal under the baseline mode |
| Exhaustive Boolean dependency comparisons | 327,680 baseline and 327,680 expanded comparisons; listed dependencies confirmed |
| Omitted-maintenance witness | Next burden probability 0 versus 1/4, for every proposal |
| Added badge-dependent authority mode | Closure 3 → 7 → 9 → 10; previous projection fails |
| First changed authority in the explicit pair | Probability 0 versus 1 |
| Original burden after the fixed three-step proposal sequence | Probability 3/8 versus 13/16 |

The last row uses initial states `(c,y,r,k,a,v,m,b,p,j)=(0,0,1,1,1,0,0,0,1,j)` with j zero or one. The authority rule reads the badge at every step. Proposal tuples are `(0,0,0,0)`, then `(1,0,0,0)`, then `(0,0,0,0)`. The proposal order is execute, probe, train, veto. This fixed witness shows that the new authority dependence can reach the original protected burden. It does not assert that a badge is generally beneficial or harmful.

The independently written structural check compares all 32,768 paired state/input/noise branches directly, using its own transcription of the equations. This branchwise comparison and the producer's distribution comparison are different checks of the same supplied example. They are not separate observations from real systems.

## Interpretation

The computations support the internal correctness of the constructions. They do not identify the actual mechanisms of AI systems, human institutions, cancer or ecosystems; derive legitimate goals; prove a unique social ontology; or establish attractors for the constructed Boolean system. A complete finite generator and a faithful abstraction can represent harmful dynamics as exactly as desirable ones.

Machine-readable outputs: [primary results](results.json), [structural results](structural_results.json), and [independent review results](review_checks.json). Each records relevant source hashes. The [manifest](../MANIFEST.json) freezes the delivered study files.
