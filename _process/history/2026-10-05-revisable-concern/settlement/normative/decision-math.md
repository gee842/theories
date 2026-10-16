# Finite decisions under uncertain standing and plural reasons

5 October 2026. Original finite application for this research; no priority claim for the elementary order, group, or indistinguishability arguments. Ethical premises are defended separately in [the foundation](FOUNDATION.md). These proofs establish conditional consequences rather than the truth of the supplied reason models.

## Model and admissibility

Let A be a finite nonempty feasible action set and M a finite nonempty set of retained models. A model combines a factual account with a normative evaluation; membership in M needs a documented evidential and argumentative ground. For each m, let ≥m be a reflexive, transitive relation on A. Completeness is not required. Write a >m b when a ≥m b and not b ≥m a.

An application must specify what an action actually implements, its costs and timing, its consequences under the factual accounts, relevant claimants and consent, and the reason relations. Models must respect the commitments defended for that application. A speculation inconsistent with admitted facts or a declared premise is not retained simply to make the choice indecisive. Conversely, inconvenience to the decision maker is not an evidential defeater.

Define robust strict dominance and the remainder by

\[
a\succ_M b\quad\Longleftrightarrow\quad
(\forall m\in M\;a\ge_m b)\;\land\;(\exists m\in M\;\neg(b\ge_m a)),
\]

\[
R_M(A)=\{a\in A:\nexists b\in A\text{ such that }b\succ_M a\}.
\]

An input with cyclic strict judgments must be repaired or represented as disagreement between models rather than silently treated as a preorder. This representation is a restriction, not proof that actual deliberation is always transitive.

## Proposition N1 on the existence and witnesses of the remainder

The relation ≻M is irreflexive and transitive. Consequently R_M(A) is nonempty. Every b outside R_M(A) is dominated by some a inside R_M(A).

**Proof.** Reflexivity of all ≥m makes a ≻M a impossible. If a ≻M b and b ≻M c, transitivity of each model gives a ≥m c. Select k with not b ≥k a from the first strict comparison. Were c ≥k a, then b ≥k c ≥k a, a contradiction. Thus not c ≥k a and a ≻M c. On a finite set an irreflexive transitive relation has no directed cycle. Starting from any excluded action and following a dominator must reach an undominated action; transitivity makes that final action a dominator of the starting one. ∎

The decision rule “choose from R_M(A)” is an additional weak normative commitment to honor these unanimous weak comparisons with at least one strict ground. No choice selected from this remainder is guaranteed to be uniquely right. A reason can be absent from every supplied model, every factual model can be wrong, or models can disagree about the winner.

## Proposition N2 on uncertainty without a gratuitous burden

Let p and h be feasible. Suppose p ≥m h for every retained model and p >k h for at least one. Then h is excluded. In particular, let models differ over whether a candidate has the relevant patienthood. If protection is strictly better when it avoids that candidate's established harm and is tied or better in every other retained account, uncertain patienthood does not make the harmful alternative admissible.

**Proof.** These are exactly the clauses of p ≻M h. ∎

This is a valid narrow result, not a general expected utility theorem. No cardinal scale, interpersonal sum, probability of patienthood, or conversion of confidence grades to moral weights is required. Real precaution costs or conflicting authorization can make the first premise false.

**Exact witness.** Let A={protect, harm}; one model assigns only the ordinal relation protect > harm and a second is indifferent. R={protect}. Add a third model in which a genuine competing burden makes harm > protect. R then contains both. Thus the rule does not give one speculative positive claim an automatic veto over adverse reasons.

## Proposition N3 on identity consistency

Let a finite group G act by renamings on A and M. Assume the whole decision description is preserved: for every g, a ≥m b if and only if ga ≥gm gb. Then gR_M(A)=R_M(A) when M is closed under these renamings. More generally, without invariance of the context, the result is equivariance R_gM(gA)=gR_M(A).

**Proof.** Substitute gm for m in the universal and existential dominance clauses. A dominating witness before renaming is a witness after renaming and conversely. Therefore membership in the remainder is preserved. ∎

This preserves relevant relationships as part of the context. A parent-child tie is not removed by a pure renaming; a claimed duty based on that tie needs independent justification. The result does not require identical actions toward different needs.

## Proposition N4 on impartial randomization under scarcity

Suppose n claimants have genuinely symmetric relevant circumstances, exactly k with 0<k<n must receive an indivisible benefit, and the only deterministic actions are the k-element recipient subsets. The full permutation group S_n acts on these actions.

There is no deterministic selector invariant under every relevant renaming. If lotteries over these subsets are permissible and implementable, there is exactly one invariant lottery: uniform probability over all \(\binom nk\) subsets. Each claimant receives marginal probability k/n.

**Proof.** Every k-subset contains one claimant and excludes another; swapping that pair changes the subset, so none is fixed by every permutation. Any two k-subsets are mapped to one another by a permutation. Invariance therefore gives them equal probability, and normalization sets that probability to 1/\(\binom nk\). A given claimant occurs in \(\binom{n-1}{k-1}\) subsets, yielding marginal k/n. ∎

The lottery domain is the finite-dimensional probability simplex over the finite deterministic set. The theorem solves only its linear invariance and normalization constraints. It assumes neither an expected welfare ranking over lotteries nor convexity of general moral preferences. With a smaller symmetry group, probability must be equal within each orbit but masses across orbits remain undetermined. With asymmetric needs or duties the premise may fail. Operational randomness, timely delivery, and an ethical reason to allow lotteries are supplied, not generated by the proof. Equal ex ante chances do not remove the realized loss of those unselected.

## Proposition N5 on informative limits

Suppose two states have exactly the same distribution of every admitted observation history, while their sets of actions meeting a demanded protection are disjoint. Any randomized policy using only those histories has the same action distribution in both states. It therefore cannot have probability one of satisfying the demanded protection in both states.

**Proof.** Equal history distributions passed through the same policy kernel yield equal action distributions. A probability measure supported with probability one on each of two disjoint sets cannot exist. ∎

This settles the specified guarantee question. It does not assert that actual states of patienthood are observationally identical or that evidence of experience cannot be strong. Different evidence, a less demanding guarantee, or an action safe in both states can change the answer.

## How evidence changes the model set

Write models as pairs (ω,τ), where ω describes the relevant facts and τ a normative account. An observation can challenge ω while leaving τ intact; a counterargument can challenge τ without changing the physical prediction. A sound noiseless test can delete factual accounts inconsistent with its result. Noisy tests require a separately justified updating or exclusion criterion, including error allowances; one unlikely observation is not logical disproof. Additional evidence can also reveal a previously unrepresented account. Ethical revision must state the premise, interpretation, or priority being changed and the reason for doing so.

For retained set M(D) given evidence and argument D, record for each change: the model, the defeating or supporting ground, the affected comparisons, and the practical consequence. Protect valid support through communication obstruction. Revise it when its actual ground fails. This uses the warrant, retained-support, and operational-access distinctions already established by the parent study.

The remainder need not shrink monotonically as models are added or removed. If the old model ties a and b, adding one with a>b removes b. If the old model has a>b, adding one with b>a restores b. These exact cases show why “more uncertainty always produces a larger remainder” is false for the chosen weak-in-all, strict-in-some rule. Neither size change alone measures ethical improvement.

## Verification

[check_decisions.py](check_decisions.py) enumerates all reflexive transitive relations on three labeled actions, all ordered triples of those relations, checks strict-order properties, nonempty remainders, and final dominating witnesses, and compares the construction with Pareto dominance on a finite ordinal-vector family. It also verifies all action renamings for each enumerated three-action preorder, the explicit scope and disagreement cases, and exact rational lottery marginals and invariance for 2≤n≤7 and 1≤k<n. The independent construction in the vector-family check concerns implementation only; neither that check nor the abstract theorems establish the supplied ethical orderings.

[results.json](results.json) records actual counts and status. Finite checks support implementation correctness. General results rest on the proofs above, not on exhaustive testing of all ethical decisions.
