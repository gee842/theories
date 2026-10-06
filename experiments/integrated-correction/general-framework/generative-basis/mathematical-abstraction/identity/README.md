# Mathematical identity under expanding interfaces

6 October 2026. Finite mathematical checks supporting [the canonical study](../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/IMMANENT-MATHEMATICAL-IDENTITY.md) and [general hand proofs](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/IMMANENT-MATHEMATICAL-IDENTITY-MATH.md). These checks add no empirical measurement or learning controller and do not rerun the earlier acquisition experiments.

The [protocol](PROTOCOL.md) specifies the enumeration before execution. [check.py](check.py) enumerates every partial deterministic process with two actions and a Boolean output on one to three labeled states. It compares descending relation refinement with a separate breadth-first search for distinguishing continuations. It also enumerates every equivalence relation on each carrier to check the coarsest-congruence claim.

The [saved result](results.json) records:

- 33,100 processes: 8 with one state, 324 with two and 32,768 with three;
- 99,300 comparisons between the two algorithms across three interfaces per process;
- 9,736 strict refinements when the second action becomes available;
- 5,202 strict refinements when the parity question is subsequently added;
- exact quotient-factorization and common-action preservation checks;
- a retained failure of the old quotient to support a new action, and the `ab` language counterexample separating state identity from operation identity.

These enumeration counts describe the chosen labeled family, not a probability distribution over physical systems. The parity question is deliberately supplied. Definedness is included in the response contract; the program does not model the acquisition of that contract.

The final finite tally example illustrates compatible truncations for stages zero through twelve. The impossibility of realizing the complete infinite tail as a finite natural number is proved in the hand note, not inferred from that finite sample. Likewise the general directed-family and compactness results rest on proofs rather than this finite enumeration.

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/identity/check.py
```

The result binds the checker and protocol hashes. The [independent review](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/IMMANENT-MATHEMATICAL-IDENTITY-REVIEW.md) records code/proof scope. The two algorithms are distinct implementations in one root-authored script; that distinction is not independent authorship or external peer review.
