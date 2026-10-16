# Review of constructive succession and access

Prepared 5 October 2026. Internal AI-assisted review and reproducibility record, not external peer review.

## Verification completed

The first independent implementation audit examined 360 diagnostic configurations. It found no blocking hidden-target, source-transfer, ledger or installation error. It identified three correctable issues: unnecessary cache recovery on already solved repeat tasks, wording overstating the diversity heuristic, and a baseline-match indicator that omitted unused public primitives. All were corrected before the main grid. The [design review](DESIGN-REVIEW.md) preserves the original findings and inspected source hash; its initial-version warnings should be read with this resolution record.

Six mechanism tests passed. They check paid construction and independent circuit evaluation, a serialized handoff with no predecessor state, recovery after a failed task, no unnecessary recovery on repeat tasks, complete dependency payments, and resource and source correctness across policies and costs.

The main grid contains 7,740 trajectories, 30,960 successor episodes and 180 configuration groups. A separate audit reconstructed every recorded resource ledger and checked the implication from new composition to solved non-inherited target. All passed. Paired random families use 64 seed clusters per configuration; the much larger trajectory count is not an independent sample size.

An additional check evaluated every inherited source node outside the learner's policy for all 6,192 source-without-extra-cache successor episodes. It found zero cases where a recorded new composition's function already existed in unread inherited source. These evaluator-only checks never guided synthesis or retention.

The supplementary access intervention contains 3,072 pairs. The audit checked identical opening balances and inherited exact-match status, identical immediate success on inherited targets, and every ledger. These comparisons hold the initial package fixed; later handoff packages can differ.

Adding the optional access argument did not alter default behavior. The current model reproduced every saved field of all 7,740 main trajectories, excluding only the newly added `activate_extra=True` log field. This check is recorded in [default-equivalence.json](../../../../experiments/constructive-succession/results-access/default-equivalence.json). The original main source and the supplementary source each have immutable copied inputs with verified SHA256 hashes.

The reserve theorem was checked independently through explicit contingent-policy enumeration, direct resource-prefix calculations, two receipt timings and an inductive infinite-horizon certificate. [RESERVE-VERIFICATION.json](RESERVE-VERIFICATION.json) records all checks. The witness's stipulated costs are kept separate from the observed computational trajectories.

The synthesis and experiment README were checked against result counts and local links. The scientific figure was rendered, inspected, and repaired for clipping and overlapping annotations. Its PNG and SVG present the same data.

## Interpretation boundaries

The main experiment is exploratory. The development run informed the reserve comparison, and the main grid motivated the access intervention. Neither is represented as preregistered or held-out confirmation. Selected numerical examples illustrate contrasting outcomes; the complete grid remains available.

Every arm has the same supplied NAND semantics, synthesis competence, base search method and external work flow. Their reproduction is not modeled. Complete target tables make this paid deterministic synthesis, not empirical discovery. The archive and cache prices are stipulated, and bookkeeping remains free.

Retained packages change search ordering as well as costs. The matched-package experiment isolates the access policy for one episode, but does not learn which policy to choose. Neither all-active nor dormant access dominates. A future policy selector would need its own information and cost account; it cannot be granted an oracle that picks the successful mode afterward.

The broader core is a causal hypothesis constrained by the examples and proofs. No empirical universality, optimal openness quota, unrestricted invention, self-sufficient resource loop, or universal moral metric has been established.
