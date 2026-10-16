# Adversarial review of a generative basis

2026-10-05. This review establishes scope conditions and separating examples. It does not claim a new universal minimality theorem or empirical validation.

**Verdict.** A precise completeness result is available relative to a declared state space, consequence labels, admissible interventions, boundary inputs, and observation privileges. A representation can preserve that interface exactly, and a finite computational instruction set can generate a broad class of dynamics. Neither result establishes that five named semantic roles are computationally irreducible, that the description is causally identified from observations, or that future purposes and interventions are already covered. These are different questions.

## 1. What is actually minimal?

For a finite controlled system, write `K_u(s,·)` for each permitted transition kernel and `L(s)` for its declared labels. A deterministic summary `q:S→Q` supports a state-independent quotient kernel exactly when the block transition probabilities agree:

\[
q(s)=q(t)\Longrightarrow
L(s)=L(t),\quad A(s)=A(t),\quad
K_u(s,q^{-1}B)=K_u(t,q^{-1}B)
\]

for every admissible input/action and quotient block `B`. Here `A` records admissible inputs, not an optimizer selected by the analyst. Boundary inputs must be included in the same quantifier. The necessity statement ranges over every represented initial state; agreement under one particular initial mixture is insufficient. Sufficiency extends to policies adapted to the retained information, not arbitrary policies that secretly inspect discarded state.

This is established strong lumpability/probabilistic bisimulation machinery. [Givan, Dean and Greig (2003)](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf), especially §§3.3–4.3 and Theorems 4–7, develop stochastic bisimulation and coarsest quotient construction for MDPs. Their reward labels can be replaced by a vector of declared labels; a scalar social objective is unnecessary. This adaptation does not by itself create a new bisimulation theorem.

**Minimal among which representations?** The coarsest such partition is minimal among the corresponding label-preserving, strongly lumpable quotients. It need not be the smallest representation of observable output laws. Consider:

```
A → C;       C → G or H, each with probability 1/2
B → D or E, each with probability 1/2; D → G; E → H
```

`A,B` share a start label; `C,D,E` share a middle label; `G,H` have distinct labels and are absorbing. The entire label-trace laws from `A` and `B` agree. Yet they are not strongly bisimilar: `C` has half its successor mass in each terminal label, whereas `D` and `E` have deterministic, different terminal labels. Thus `C` cannot share a bisimulation block with either, and the outgoing block masses from `A,B` differ. Do not identify strong quotient minimality with unrestricted predictive minimality.

For history-based prediction, [Barnett and Crutchfield's ε-transducer construction](https://csc.ucdavis.edu/~cmg/papers/et1.pdf) is a closer primary lineage: histories are grouped by their conditional future-output laws given input sequences. Its maximal-prescience and minimality results concern an explicitly defined channel and statistical setting. An observed input-output distribution is not automatically an experimentally identified causal channel.

## 2. Five separating witnesses—and the correct necessity quantifier

These finite examples establish that each distinction **can** matter. They do not establish that every system needs all five as separate variables. All examples can be encoded as ordinary finite transition systems with declared observation channels.

### Observation

Let an unknown fair bit `X` specify which action `a∈{0,1}` avoids harm, with `H=1[a≠X]`. The two systems have identical feasible actions, execution, and retention. One has a perfect pre-action signal `Y=X`; the other has a constant signal. With the first signal, choosing `a=Y` has zero harm. With the constant signal, every randomized action policy has expected harm `1/2`. More physical capacity cannot substitute for this missing distinction under the specified deadline and action set.

The qualification is essential: adding an always-safe third action makes detailed observation unnecessary for safety. Information is not universally necessary or intrinsically beneficial regardless of costs. The connection between informative variety and regulation is established in [Ashby (1956), chapters 11–12](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf); that lineage does not determine which outcomes are desirable.

### Feasible response versus implementation authority

Let `f,a∈{0,1}` denote a working repair tool and an execution gate. A repair request succeeds exactly when `fa=1`. Both states `(f,a)=(0,1)` and `(1,0)` fail the same current repair request, with identical information and goals. But the intervention **supply the tool** restores success only in the first; **open the gate** restores it only in the second. A summary retaining only the product `fa` loses these intervention effects.

If the interface never permits interventions on either component, the product may be a faithful summary for the remaining questions. The semantic distinction becomes necessary relative to interventions, not because the words “capacity” and “authority” must inhabit separate registers. Biological examples need not contain a political authority; an implementation gate can be a physical causal mechanism without institutional meaning.

### Renewal and retention

Compare a reusable repair apparatus and a one-use apparatus. Both repair the first known disturbance perfectly. After use, the former retains capacity and the latter has none. A second identical disturbance followed by the same repair command yields success versus failure. Current performance, information, and initial action availability are identical; the enabling condition's transition differs.

This separates a successful response from continuation of its prerequisites. A new member need not be involved: physical renewal and intergenerational transmission are distinct possible mechanisms. Conversely, a genuinely one-shot task may require no renewal variable.

### Changing interpretation and purpose

Two independent distinctions fit this broad role. First, with physical input bit `X`, an installed interpretation `ψ` can implement `a=X XOR ψ`. Changing `ψ` changes the response under the same raw input; whether this corrects an error requires a separately stated consequence model. Second, let physical condition `x=0` remain fixed while an accepted criterion `p` changes from 1 to 0. The verdict `1[x=p]` improves from 0 to 1 without any physical recovery. A representation keeping only the verdict cannot distinguish restoration from changing the standard.

A fixed goal is permitted; explicit goal revision is not required in every model. Nor can behavior alone settle which inferred goal deserves endorsement. [Armstrong and Mindermann (NeurIPS 2018)](https://proceedings.neurips.cc/paper_files/paper/2018/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html) show that separating a policy into reward and planning components needs additional assumptions. Modeling purpose formation is not deriving legitimate purposes from physical observations.

The warranted quantifier is: **for each role, there exists a permitted finite model and intervention/query family in which erasing its relevant distinction is unfaithful**. The unwarranted quantifier is: **every adequate model must contain five separately identifiable primitive components**.

## 3. Why a five-part ontology cannot be proved computationally irreducible

Let a finite model's state be a tuple of the five proposed components. A bijection from that product into integers pushes every kernel, observation, label, and intervention forward without changing predictions. The resulting model has one encoded state variable. Conversely, redundant coordinates can split one component into many. Variable counts and names therefore cannot furnish representation-invariant necessity.

One can obtain a meaningful minimality result only after restricting admissible encodings or interfaces—for example, requiring that separately manipulable components remain separately addressable, constraining locality or modularity, or bounding description length and computational cost. These restrictions must be stated and justified. A finite set of computational instructions can be universal without being a uniquely explanatory social or biological vocabulary.

## 4. An intervention can invalidate an otherwise exact summary

**Fixed-signature extension obstruction.** Suppose `q(s)=q(t)` for distinct states. If an expanded query family admits a label `ℓ` with `ℓ(s)≠ℓ(t)`, no function of `q` represents that label exactly. In particular, admitting all state indicators makes every noninjective summary incomplete. This is not an argument against compression: many indicators are irrelevant to the original problem.

Likewise, if a newly permitted intervention `v` satisfies

\[
K_v(s,q^{-1}B)\ne K_v(t,q^{-1}B)
\]

for some retained block `B`, the old summary cannot support a well-defined quotient for the enlarged interface. The repair is to refine the summary or restrict the claim, rather than declare the new intervention already covered by the old theorem. Internal goal changes already encoded in the original state and transition rules are different from an analyst admitting an entirely new question afterward.

**Passive-data obstruction.** Two models both take action `a` under the installed policy and reach success deterministically. Under unused action `b`, model 1 succeeds and model 2 fails. Every passive trajectory under the installed policy agrees; the intervention contrast differs by one. Observed agreement cannot identify the missing intervention kernel, even if the formal model class can represent it perfectly.

## 5. Closure of a generative language needs interface restrictions

**Hidden guards.** Let `s~t`. Primitive `K0` sends either to output 0; primitive `K1` sends either to output 1. Each primitive respects the quotient. A raw-state guard selecting `K0` at `s` and `K1` at `t` does not. Branch guards, stopping rules, and mixture weights must factor through retained information, or their combined kernel must be checked directly for lumpability. Quotient-measurable mixing is sufficient; it is not necessary when the mixed primitive quotient kernels happen to coincide.

**Shared noise.** Two next-state bits each have a fair marginal. In mode 0, draw one fair bit `B` and set `(X,Y)=(B,B)`; in mode 1, set `(X,Y)=(B,1−B)`. All component marginal laws agree, but `P(X=Y)` is 1 versus 0. A componentwise product theorem therefore requires genuine conditional independence or an explicitly preserved joint coupling. Matching marginals alone does not justify composition.

**One initial mixture.** If `s,t` are merged but lead deterministically to different terminal labels, a quotient using a half-half transition fits the initial distribution `½δs+½δt`. It does not fit both point initial states. An all-initial-state exactness theorem cannot be verified solely under one training distribution.

**Compiler scope.** A finite rational transition table can be generated by bit tests, updates, rational random choices, and sequencing. This proves expressive completeness for that class, at a declared macrostep boundary. It need not provide compression, efficient inference, a physical implementation, or an explanation of why a social mechanism has those transition probabilities. Intermediate steps, concurrency, timing, and costs must not be erased if the requested properties can inspect them. The compiler's universal ability to reproduce a table is a computational foundation, not evidence that the table describes the world.

## 6. Finite generators do not imply finitely many predictive states

Let `c∈N` be a counter, with two actions:

\[
\mathrm{push}:c\mapsto c+1,\qquad
\mathrm{pop}:c\mapsto\max(c-1,0),
\]

and observation `1[c=0]`. For any `0<n<m`, the same present observation is returned, but `n` consecutive pops produce zero from `n` and a positive count from `m`. Hence every count has a distinct intervention-predictive future: no finite-state exact quotient covers all counts and horizons.

**This system has a very small finite generative rule set.** The example refutes finite exact *state compression*, not finite generators, a finite descriptive program, or a computational root. Nor does dependence on arbitrarily old observations automatically imply infinite predictive state: parity is a counterexample. Barnett and Crutchfield's channel examples explicitly distinguish finite-state representations from finite-window history descriptions.

Similarly, for each finite validation horizon `H`, a finite countdown system can agree with a permanently safe system for `H` steps and fail at `H+1`. No finite horizon validates unbounded continuation uniformly over a class allowing arbitrary delay. A specified known finite kernel permits stronger checks; this obstruction concerns extrapolation across an unrestricted class.

If the generative language is extended to arbitrary unbounded programs, universal automatic safety certification faces the standard undecidability obstruction: simulate a program while emitting “safe,” and emit “failure” exactly when it halts. A decider for indefinite safety of all such generators would decide halting. This limits general certification, not expressibility or mathematical proofs for restricted families. The classical primary computational lineage is [Turing's computability paper](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf); the safety reduction here is the elementary modern construction, not a claim about that paper's exact terminology.

## 7. Non-vacuity and contribution threshold

A defensible contribution is a **situated completeness contract**: declare the interface, demonstrate what can be generated, characterize exact information-preserving reductions, and supply witnesses showing which omitted distinctions matter under which interventions. It is useful even though its core abstraction and computation results have substantial prior art.

For explanatory contribution beyond representability, the model still needs restrictions that exclude possible behavior: testable intervention predictions, justified factorization or resource laws, identified mechanisms, or a smaller description with improved generalization against specified alternatives. A universal table compiler fits arbitrary outcomes by construction and cannot supply these restrictions alone. Evidence that the machinery represents an institution, an ecosystem, and an AI system does not demonstrate that all three share the same causal mechanism or permit the same intervention.

Accept a completeness theorem only with the following scope attached: fixed declared interface; state/observation distinction; actual versus hypothetical control; uniform initial-state quantifier where needed; retained joint noise; quotient-measurable control; precise macrostep semantics; and normative criteria kept distinct from material consequences. None requires an immutable universal goal. They make a situated, revisable theory mathematically assessable.

## 8. Audit of the supplied formal construction

I read the complete [formal note](../formal/FORMAL.md), including Theorems 1–5. I found no blocking error in the quotient existence/uniqueness proof, coarsest refinement proof and termination bound, observation-restricted path-law corollary, stated composition rules, rational-kernel compiler, or bounded fair-coin obstruction. The note explicitly retains the substantive limitations identified above. This is an independent review within the AI-assisted team, not external peer review or empirical validation.

One terminology qualification remains useful: “finite instruction set” here means finitely many instruction **forms**, with rational probabilities provided as finite input data. It does not mean a fixed finite menu of coin biases already explains every row. The proof openly accounts for those supplied coefficients. Enlarging the instructions to unbounded execution, arbitrary real constants, or interruptible microsteps changes the theorem being claimed.

## Primary sources actually inspected

1. Givan, R., Dean, T., and Greig, M. (2003). *Equivalence notions and model minimization in Markov decision processes*. Artificial Intelligence 147, 163–223. DOI 10.1016/S0004-3702(02)00376-4. Author-hosted PDF inspected directly, especially PDF pages 13–15.
2. Barnett, N., and Crutchfield, J. P. (2015). *Computational Mechanics of Input–Output Processes: Structured Transformations and the ε-Transducer*. Journal of Statistical Physics 161, 404–451. DOI 10.1007/s10955-015-1327-5. Author-hosted manuscript and arXiv:1412.2690 inspected; PDF version dated February 6, 2016.
3. Ashby, W. R. (1956). *An Introduction to Cybernetics*. Author-family archive scan inspected, including requisite-variety discussion. This is prior theory of regulation, not a proof of the programme's entire proposed architecture.
4. Armstrong, S., and Mindermann, S. (2018). *Occam's razor is insufficient to infer the preferences of irrational agents*. Official NeurIPS proceedings abstract and paper accessed. Supports the need for additional assumptions in preference interpretation, not an impossibility of all normative reasoning.
5. Turing, A. M. (1936–37). *On Computable Numbers, with an Application to the Entscheidungsproblem*. Original-paper scan accessed. Cited only for the computational limitation identified above.
