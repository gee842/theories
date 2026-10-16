# Finite audit of the self/other symmetry bridge

6 October 2026. An abstract exhaustive check for the [whole-theory necessity study](../../../../../theories/becoming/history/HUIGEN.md), not an empirical measurement of moral judgment.

For each size from one to four, [check.py](check.py) enumerates every binary relation `r(actor, patient)` and tests every simultaneous permutation of actor and patient indices directly. It compares the invariant relations with the independently stated diagonal/off-diagonal characterization. Positive self-standing and actor independence are tested separately.

Run with Python's standard library:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/necessity-symmetry/check.py
```

The [verification record](verification.json) contains the source SHA-256 and all admitted invariant matrices. Across **66,066** enumerated matrices, invariant counts are **2, 4, 4, 4**. Imposing positive diagonals leaves **1, 2, 2, 2**; also requiring actor independence leaves exactly one relation at each size, the all-positive relation. For every tested size above one, the self-only relation satisfies joint renaming and positive self-standing but fails actor independence.

The [general two-orbit proof](../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/HUIGEN-FULL-THEORY-AUDIT.md#42-two-orbit-lemma) applies to arbitrary finite size at least two in a fixed homogeneous context. It supplies the universal argument; this finite enumeration corroborates small instances. No inference from a finite sample to all ethical contexts is made. Contextual attributes and relationships require their own action and invariance analysis. Neither renaming nor these calculations justify why another center's harm supplies a reason: they identify precisely what a proposed proof must add.
