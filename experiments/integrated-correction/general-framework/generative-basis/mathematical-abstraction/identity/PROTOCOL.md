# Finite checks of mathematical identity under expanding interfaces

6 October 2026. This protocol precedes execution of `check.py`. These are finite mathematical checks of the accompanying hand proofs, not empirical measurements, a new learner, or a revalidation of earlier experiments.

Enumerate every partial deterministic process on one, two and three labeled states, with two action labels and one Boolean output. An action entry is either a successor state or undefined. This gives 8, 324 and 32,768 configurations respectively, for 33,100 total. State labels do not supply an ontological interpretation.

For each configuration, compute contextual equivalence twice: descending relation refinement and a separate breadth-first search for a distinguishing pair continuation. Definedness is observable in both methods. Compare three interfaces: the first action and original output; both actions and original output; both actions and the output paired with state-label parity. Parity is a deliberately supplied extra question, not acquired knowledge. Check equality of the two algorithms, refinement inclusions, surjective quotient factorization, output and definedness preservation, and action compatibility over each common alphabet. Exhaustively enumerate equivalence relations on the carrier to check the coarsest-congruence characterization.

Retain the first enumerated counterexample to making the newly available second action operate on the old quotient. Separately evaluate the total automaton accepting exactly the word `ab`: histories `b` and `aa` have the same residual behavior from the initial state, while prefixing `a` distinguishes them. This checks why history equivalence does not suffice for substitutable operations.

Finally, display finite stages of the hand-proof example `S = N`, increment, and observations `min(n,k)`. Every chosen finite family of tail classes has a witness, while the general proof establishes that their full intersection is empty. The script checks only its stated finite window and never claims to computationally certify the infinite intersection.

Save counts, scope, counterexamples and source hashes to `results.json`. Fail immediately on any asserted identity or preservation failure. Do not replace the declared family after examining results.
