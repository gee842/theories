# Invariance, irreducibility, and a genuine minimal root

Audit prepared 5 October 2026. Other workspaces were read without modification. The most recent inspected structural report is cycle 6, last modified 05:33; the causal formal report was modified 03:55. These are the same latest output families located by this audit; no later causal or structural output appeared in their output directories.

## The constructive result

The strongest exact answer available here is **an irreducible structure of responses to declared possible interventions**. Its minimality can be proved, and its invariance has an explicit equation. This is stronger than a checklist of cognitive capacities, but it is not a discovered governing equation for the actual universe.

For a deterministic system with states `Z`, admitted inputs `A`, transitions `F_a: Z → Z`, and declared observable outcomes `O: Z → Y`, define

\[
x\sim y\quad\Longleftrightarrow\quad
O(F_w(x))=O(F_w(y))\quad\text{for every }w\in A^*.
\tag{1}
\]

Here `w` is any finite input sequence, including the empty sequence, and `F_w` is its composed transition. Failed attempts can be modeled explicitly as outcomes; admitting an input does not declare it affordable, permitted, or successful. If those distinctions matter, they must occur in the modeled states and outputs. The intervention meanings must be supplied and justified.

The proposed mathematical root of this particular response system is

\[
\mathfrak C=(Z/{\sim},\{\bar F_a\}_{a\in A},\bar O),
\qquad
qF_a=\bar F_aq,\quad O=\bar Oq.
\tag{2}
\]

Equation (2) says that abstracting and then evolving gives the same result as evolving and then abstracting, while preserving the outcome questions. Equation (1) says exactly which distinctions the root must retain: those that can change the answer to at least one admitted future test.

### Minimal response theorem

**Claim.** The relation in (1) is the coarsest equivalence relation that preserves `O` and is stable under every `F_a`. The quotient in (2) is well defined and preserves every finite input/output experiment. Every exact representation from which all these experiment results can be recovered must retain enough information to identify each `~` class. In a finite system, its number of classes is therefore the least possible number of states in any exact deterministic representation of the response functions represented here. At the level of the coarsest partition, the result is unique up to a relabeling of classes.

**Proof.** Equality of answer vectors is an equivalence relation. The empty sequence gives `O(x)=O(y)` whenever `x~y`. If `x~y`, then for every input `a` and continuation `w`, equality of the answers to the concatenated sequence `aw` gives `F_a(x)~F_a(y)`. Thus `F̄_a([x])=[F_a(x)]` and `Ō([x])=O(x)` are well defined. Induction gives `qF_w=F̄_wq`, hence all finite experiment outcomes agree. If another encoding `h` permits exact recovery of every answer, then `h(x)=h(y)` implies all answers agree, so `x~y`. Therefore `q=rh` for a well-defined map `r` on the image of `h`. Such an encoding cannot merge distinct `~` classes. Conversely `q` itself suffices. Finally, any equivalence preserving the output and closed under transitions preserves all input-sequence answers by induction, so it refines `~`. ∎

This is an elementary response-equivalence/minimization result, not a novelty claim. Related established theory includes automata minimization and stochastic bisimulation. Givan, Dean, and Greig formulate action-indexed state transitions and outcomes, then develop stochastic equivalence supporting model minimization and policy transfer in a declared MDP. Their results are not a theorem that every physical or ethical phenomenon has that form. [Primary paper, *Equivalence Notions and Model Minimization in Markov Decision Processes*](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

This theorem is a constructive positive answer to “can we obtain an irreducible root?”: **yes, for a specified response domain, and irreducibility has an exact test**. It does not establish that its quotient is finite, effectively discoverable, or the uniquely correct domain for wisdom or the universe. With infinite states, partition minimality remains meaningful; cardinality alone is too weak to express it.

## The probabilistic counterpart already established in the other session

The causal session proves a sharper version than a bare slogan of invariance. For a surjective finite-state map `h:Z→X`, intervention kernels `P^i`, and incidence matrix `H(z,x)=1{h(z)=x}`, an exact closed macro kernel exists precisely when the pushed-forward next-state distribution is constant on each fiber:

\[
\sum_{z':h(z')=x'}P^i(z'\mid z)
=\bar P^i(x'\mid h(z))
\quad\Longleftrightarrow\quad
P^iH=H\bar P^i.
\tag{3}
\]

The equivalence is between the existence of such macro kernels and that fiber constancy condition, for all admitted interventions. Point-mass initial conditions prove necessity. Constancy makes each conditional mixture over a fiber produce the same next macro distribution, proving sufficiency. With compatible observations, intervention availability, outcome definitions, and the same macro-information policy, induction gives equality of finite path laws. Additional dependence between observation and transition must be represented by a joint kernel; equality of separate marginals is insufficient.

This is a genuine constraint on a proposed many-to-one abstraction. It cannot generally be satisfied by dropping arbitrary detail. The source also proves that a uniform one-step total-variation error `ε` bounds horizon-`T` path error by `1−(1−ε)^T≤Tε`, under its stated observation and policy assumptions. Average training fit is not that uniform guarantee.

Source: `../causal-foundations/outputs/formal-results.md`, Proposition A. The exact deterministic formulation above supplies a particularly transparent minimality result; stochastic notions of trace equivalence, bisimulation, and minimal realization should not be silently identified.

## Two explicit examples that expose what “irreducible” means

Let states be `(x,n)∈{0,1}²`, inputs `a∈{0,1}`, and current outcome `O(x,n)=x`.

1. With `F_a(x,n)=(a,n xor a)`, the nuisance bit never changes any present or future output. The irreducible response quotient has two states, corresponding to `x`. Retaining `n` adds no predictive distinction for these tests.
2. With `F_a(x,n)=(a xor n,n)`, both coordinates matter. Distinct current `x` values are distinguished by the empty test; equal `x` and different `n` values are distinguished by one input. The irreducible quotient has all four states. The representation `h(x,n)=x` therefore fails the closure equation.

Adding a question that reads `n` makes all four states relevant even in the first system. This is not a failure of the earlier theorem. Its domain of preserved questions has changed.

For arbitrary states `Z` and a declared query family `Q`, the more general static relation is

\[
x\sim_Qy\iff \forall q\in Q\;q(x)=q(y).
\tag{4}
\]

If `Q` includes every predicate on `Z`, two distinct states are separated by the indicator of either singleton. Hence `~_Q` is equality. **There is no universally lossless, nontrivial many-to-one compression when literally every distinction may later matter.** Compact generative descriptions of a large state space remain possible: this theorem concerns merging semantically distinguishable states, not the length of a program defining them.

## Why covariance is not dynamics

For any bijection `b:Z→Z'` and any law `F`, one can define `F'=bFb⁻¹`. Then `bF=F'b` automatically. Both the bit law `F(x)=x` and the bit law `G(x)=1−x` satisfy this kind of covariance, while making different next-state predictions. Thus covariance under coherent relabeling does not select between them.

This is the decisive distinction for the “Maxwell equation” ambition. A substantive law has to constrain which histories, intervention responses, or parameter relations are physically admitted. A rule saying that equivalent descriptions preserve answers constrains descriptions; it does not by itself supply the physical answer. A universal notation admitting every possible transition relation cannot yield a nontrivial property falsified by one of those relations without adding a restriction.

The equation `qF=F̄q` is stronger when a proposed *many-to-one* `q` and independently specified target questions are fixed: it then forbids some abstractions of a given dynamics. It still leaves the dynamics to be established. Calling that exact abstraction law “the whole truth” would erase the main unsolved step.

## The assumptions are separable

These roles cannot be removed by writing a smaller tuple:

| Role | Witness that the remaining roles do not determine it |
|---|---|
| Actual transition/intervention law | Identity and bit flip have the same state and input types but different futures. |
| Meaning and scope of outcomes | Observing `x` alone versus `(x,n)` changes the minimal quotient with no change of dynamics. |
| Admitted possible interventions | Adding a repair input sensitive to `n` can destroy an abstraction valid for ordinary inputs. |
| Information available to the controller | A hidden fair bit can be matched with probability one when revealed and only one half when the only permitted evidence is constant. |
| Means of execution | A correct chosen response can fail when an actuator or permission gate is absent. |
| Evaluative ordering | The same exact transition facts permit rankings favoring opposite terminal states. |

Encoding these roles into a single set or relation shortens notation; it does not derive one from the others. Their physical realizations may overlap, and they need not be independent manipulable substances. The independence claimed here is logical: the remaining supplied structure does not uniquely determine the omitted role.

The structural session adds a particularly useful correction to “more information creates wisdom.” Its cycle-6 audit finds that a supplied query can identify a changed contract correctly yet consume the funds needed for the corrected successor. A cheaper blind revision or funded mixed policy can sometimes preserve the specified objective. Thus information is not universally necessary, and correct information is not sufficient. Whether it is needed depends on the outcome criterion, intervention family, information, and remaining means. Source: `../structural-foundations/outputs/cycle-6/revision-audit.md`, especially its epoch-27/28 calculation and quota-control counterexample.

## What this supports for the revised root project

The most defensible compact claim is:

> A representation is exact for a domain precisely when it preserves the distinctions that can change the domain's answers under its admitted interventions; its irreducible form identifies exactly the states that no such test can distinguish.

That claim is a universal structural theorem schema with a constructive minimal object in the deterministic case. It gives three concrete ways to progress:

1. Fix candidate physical or practical outcome questions independently of success on the examples.
2. Propose an economical law generating their intervention responses and derive a quotient/invariance certificate. The law must prohibit identifiable alternatives.
3. Challenge both the law and the chosen question family: a new outcome, intervention, observer, or stakeholder can reveal a distinction the earlier quotient was allowed to erase.

The final step is how the formal result connects to missing possibilities. A model can be perfectly irreducible and complete **relative to a question family that omits something important**. Mathematics alone cannot certify that the chosen family covers every morally or practically important possibility. Nor does this prove that a more fundamental empirical theory is impossible; it identifies exactly which work the invariance theorem has and has not done.

## Inspection record

Read relevant passages and proofs from:

- `../causal-foundations/outputs/formal-results.md` (Propositions A–D and semantic setup).
- `../causal-foundations/outputs/causal-foundations.md` (embedded observer, invariance, intervention/counterfactual distinctions, implementation examples).
- `../structural-foundations/outputs/formal-foundations.md` (semantic core, fixed-ambient representation, information-sensitive capacity transfer).
- `../structural-foundations/outputs/cycle-6/synthesis.md` and `revision-audit.md` (paid evaluator revision and counterexamples to diagnosis necessity).
- The author-hosted Givan–Dean–Greig paper above, opening sections and formal setup. No claim of full independent reproduction of that paper's proofs.

The deterministic theorem and four-state examples were independently derived here. No new benchmark was used to stand in for a proof; no empirical universality or novelty is claimed.
