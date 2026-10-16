# Mathematical audit of the primary optimal-foundation formulation

5 October 2026. Internal AI-agent review of [OPTIMAL-FOUNDATION.md](../OPTIMAL-FOUNDATION.md), including Theorems N1–N4, the observed/hidden interface distinction, and the exact examples. This is not independent human peer review, empirical validation, or a novelty assessment.

## Final finding

No unresolved mathematical finding remains from this audit. The claimed optima are valid within their explicitly different comparison classes. The revisions now distinguish a well-defined recurrent predictor from an effectively executable implementation, preserve actual observation restrictions, and qualify the scope of the predictive-rank claim.

## Theorems and assumptions checked

**N1: least exact deterministic representation.** Equality of complete required response profiles defines an equivalence relation. Any exact representation has fibers contained in its classes, giving the claimed factorization. Mutual factorization of least representations yields identical partitions and a bijection on attained values. Finite-state cardinality minimality and discrete finite-entropy minimality follow as stated. These statements are relative to a supplied contract; neither entails causal identification or a uniquely optimal ontology.

**N2: recursive predictive state.** For the actual observed interface, continuation probabilities determine one-step marginals, and conditional continuation is the ratio of a prefixed probability to the positive one-step probability. Consequently equivalent histories remain equivalent after a common possible observation. The full finite-test family supplies the needed continuation closure. Impossible observations are correctly excluded from that division. Extension to adaptive policies preserves the same residual policy and initialized controller memory; it does not identify distinct historical controllers merely because their environmental predictions agree.

The final text correctly requires added exact labels to be functions of actual observed history with a preserved observation-based update. An unobserved current label cannot be supplied to the policy through a prediction of its future. Section 5.1 separately handles joint protected-outcome forecasts using causal conditioning and marginalization over the hidden first audit value. Its persistent-hidden-bit example correctly shows why such a forecast profile is not automatically a one-state Markov generator of independently sampled audit outputs.

**N3: minimum linear dimension.** For algebraic response-matrix rank \(r\), a basis of actual test columns gives exact linear readout. Every competing ordinary linear \(d\)-coordinate representation factors the matrix through \(\mathbb R^d\), so \(d\ge r\). The prefixed-test Bayesian update is valid on positive-probability observations and coherent reachable probability states. Because the empty-test column is the constant one, a basis can include it; storing the other \(r-1\) coordinates gives affine readout. Conversely \(d\) affine variable coordinates span at most \(d+1\) column functions, proving \(r-1\) minimal. Additional current/protected tests can change rank and require their own conditioning closure, as the revised text states.

This rank optimum is not minimum nonnegative latent-state size, finite-bit memory, nonlinear coordinate count, or runtime. The response basis is not unique even though its span and the associated response equivalence are fixed.

**N4: finite physical-state quotient.** Label/interface initialization and action-indexed block-row refinement give a stable partition. Every faithful competitor refines each successive partition by summation over its finer blocks, proving the unique coarsest faithful quotient. Exact rational tables make this an effective finite procedure. The document appropriately separates this stronger internal Markov preservation problem from prediction of observable histories.

**Other claims.** The robust capacity statement uses one common permitted policy across unresolved models. Contract expansion refines response equivalence. The \(\delta/2\) worst-case error bound for a merged separated response follows by the triangle inequality. The stated nontransitivity example rules out treating tolerance-based closeness as automatic exact equivalence. The hidden-mixture example distinguishes infinite predictive classes from rank-two linear prediction.

## Independent checks of the constructed examples

I read `verify_optimality.py` and its saved results. I then checked the reported counts independently, without importing or rerunning that implementation:

- The Bell-number recurrence gives \(B_8=4{,}140\) partitions of eight active states.
- Distinct reserve/delay combinations must remain separate: one wait distinguishes reserves, and waiting to reserve one followed by dispatch distinguishes delays.
- Each of the four resulting active classes contains two badge values. For a fixed delay, splitting the lower-reserve badge pair forces the upper pair to split, because waiting maps the latter to the former. The three permitted choices are merge both, split only the upper pair, or split both. The two delays therefore give exactly \(3^2=9\) faithful refinements.
- Only merging both pairs for both delays attains the six-class quotient, including the two absorbing labeled states.
- Independent rational calculation reproduces all thirteen hidden-environment predictions, from \(1/2\) through \(2731/4097\). Their strict monotonicity follows algebraically from the displayed formula; the finite calculation is not used as proof of infinitely many predictive classes.

The timing construction is explicitly a macrostep model. It does not preserve unrecorded travel hazards, exact arrival-time observations, or interventions during travel. Its conclusions match that scope.

## Findings raised and resolved before completion

1. “Executable predictor” was stronger than the existence theorem, which permits noncomputable causal laws and infinite response states. The text now says recursively defined/updated predictor and separately states effective representation and precision requirements.
2. Added current labels could have been read as exposing hidden outcomes to the updater. Their observable/compatible-update condition is now explicit, with hidden conditional forecasting treated separately.
3. The rank theorem could have been read as minimizing a richer evaluative contract automatically. The text now restricts it to its stated observed-test matrix and requires additional protected queries and update closure before extending the claim.
4. The affine-coordinate claim now includes its lower bound \(\operatorname{rank}D\le d+1\), establishing minimality as well as attainability.

No claim about a universal ethical optimum, unrestricted causal discovery, or minimum physical implementation follows from these results, and the document does not assert one. The primary approach is a defensible methodological choice with proved representational optima and a retained mechanistic alternative.
