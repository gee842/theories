# Constraints across scale and their different outcomes

Continuation: the [fourth cycle](../cycle-4/synthesis.md) now models actual adoption, paid learning, and rule transmission. This record preserves the third-cycle results.

The [formal synthesis](synthesis.md) connects feasible continuation, cross-scale implementation, paid repair infrastructure, retained evidence, succession, and actual selection. Its central proposal is that the constraints on feasible continuation retain their form while the organization satisfying them changes with scale, space, and time.

## Read the results

- [Formal synthesis](synthesis.md): the connected account and its explanatory limits.
- [Constraint transport](constraint-transport.md): sufficient policy-transfer and composition proofs, internal timing and payment obligations, and counterexamples.
- [Scale and renewal](scale-and-renewal.md): an exact recurring-repair frontier with paid infrastructure; too little or too much can fail.
- [Paid memory and succession](paid-memory-and-succession.md): physical registers, stale evidence, funding chronology, access, and an exact preservation/reacquisition frontier.
- [Universality audit](universality-audit.md): coarse-state memory, prior art, actual selection, empirical tests, and normative boundaries.
- [Claim register](CLAIMS.md): definitions, theorems, constructed results, and open hypotheses.

The scale model is a robust indefinite-safety result. The memory model primarily uses a finite expected-error criterion; its constant-condition special case supplies a separate sure guarantee. They share an operational framework but have not been silently fused into one fully endogenous recurrent succession model.

## Reproduce the finite checks

From this directory, run the standard-library scripts:

```text
python3 verification/check_constraint_transport.py
python3 verification/check_integrated_scale.py
python3 verification/check_paid_memory.py
```

The [verification receipt](verification/verification-receipt.json) records the final run and file hashes. Results are preserved separately for [transport](verification/constraint-transport-results.json), [scale and renewal](verification/integrated-scale-results.json), and [paid memory](verification/paid-memory-results.json). The scale script enumerates all stage schedules in its finite safety games; the memory script enumerates actual finite encoders and decoders, with no perfect-recall history passed to the actuator.

These are conditional proofs and synthetic computations, with complementary review. They do not establish empirical universality or mathematical novelty. The prior [second cycle](../cycle-2/README.md) and [initial research](../synthesis.md) remain available.
