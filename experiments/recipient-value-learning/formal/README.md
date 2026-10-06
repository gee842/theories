# Offered-choice identification bounds

This additive package proves the probability and response-overlap part of the [bounded-alternative account](../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md). It does not read or change the earlier participant data, analysis or frozen empirical protocol.

**Status:** the complete fresh Lean 4.29.1 build passes 27 audited declarations across two modules, including algebra helpers. Separate internal review checks the propositions, source identity and their interpretation. Only the standard `propext`, `Quot.sound` and `Classical.choice` dependencies occur; no custom axiom, proof hole or unchecked native decision is used.

## Exact scope

[OfferedChoiceBounds.lean](OfferedChoiceBounds.lean) represents a finite list of paired units with nonnegative rational weights summing to one. Each unit supplies two response probabilities, two conditional target-directed choice probabilities, and a covered flag. On covered units, the choice-probability difference is bounded by `m`; uncovered mass is at most `epsilon`.

The theorem bounds the signed difference in target-directed responses per offered opportunity using both marginal response levels. It proves the mirrored bound separately. Its five-stratum construction attains the upper endpoint for every admissible rational set of marginal levels, probability-gap and coverage parameters. Equal response rates with disjoint responding groups remain a checked counterexample to treating mean equality as unchanged individual gates.

[OddsEnvelope.lean](OddsEnvelope.lean) proves the exact rational-odds quadratic equivalence and a sufficient discriminant/positive-coefficient certificate, then carries the bound through genuinely paired response gates. It includes sharp rational examples. The coefficient certificate is not advertised as a proved necessary characterization, and a marginal response difference does not supply its paired gate premise.

The real-valued logistic calculation, its score decomposition, statistical inference and measurement interpretation live in the [mathematical companion](../../../_process/research/2026-10-05-concern-theory/reward-association/BOUNDED-IDENTIFICATION-MATH.md). In particular, Lean does not identify beliefs or evaluative coefficients in a real population. Endpoint probability witnesses can require limiting scores in a logistic interpretation.

## Reproduction

Run from this directory:

```sh
python3 check.py
```

[The checker](check.py) uses the pinned Lean 4.29.1 toolchain in a fresh temporary build, records exact source/checker/compiler hashes and audits theorem dependencies. [The current receipt](verification.json) records the build scope. The prospective obligations and earlier attempts remain under [development](development/); failed attempts are provenance, not independent confirmations.

The separate [numerical checks](../bounded-identification/checks.json) concern analytical boundaries and constructed counterexamples, with no empirical data input. The [internal review](../../../_process/research/2026-10-05-concern-theory/reward-association/BOUNDED-IDENTIFICATION-REVIEW.md) distinguishes those checks, formal proof and empirical identification. The full foundation remains ongoing.
