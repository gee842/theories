# Restricted generative completeness and faithful reduction

5 October 2026. AI-assisted formal research note. These are conditional mathematical results for a declared finite class, not a proof that the alignment programme has discovered a unique generative root of society or life. The proofs below make the claim testable without requiring a scalar objective. They extend the earlier [finite closure study](../../closure-study/FORMAL.md); they do not replace its safety, recurrence, information, or normative qualifications.

The two questions answered here are different:

1. When does a proposed smaller state preserve the consequences of every declared intervention?
2. What class of stochastic systems can a restricted instruction set generate?

The first supplies a nontrivial completeness test for a proposed representation. The second supplies a constructive expressiveness result. Neither alone establishes that the generating instructions explain why the physical or social mechanisms take their particular forms.

## 1. Declared class and contract

Let a model be

\[
\mathcal M=(S,U,D,K,L),
\]

where \(S\) is a nonempty finite state space, \(U\) is a finite set of permitted interventions, \(D\) is a finite set of declared boundary inputs, and \(K_{u,d}(s,t)\) is a row-stochastic transition matrix for each input pair. The labels

\[
L:S\longrightarrow\mathcal O
\]

can be a tuple of physical outcomes, burdens on different parties, observations available to particular participants, current normative commitments, and event-monitor states. Only the image of \(L\) must be finite; no ordering, scalar reward, or common objective is required. A variable whose past matters must be included in the state or a finite monitor. History-dependent systems lacking a finite sufficient state fall outside this class.

For simplicity, every input pair is permitted in every state. State-dependent permission can instead be included in the labels, with kernels and equalities restricted to the common permitted inputs of each block. Alternatively, denied proposals can be explicit events. An intervention is a supplied implementable change, not an analyst's undeclared power to rewrite the world. Multiple actors' joint actions can be included in \(U\); the theorem does not grant any actor knowledge or authority over the whole joint action.

Boundary inputs need not be benign, stationary, or chosen to optimize anything. We condition on their specified values. A claim about an endogenously interacting environment must also specify its input-generating process. A process depending on hidden fine-state distinctions is not automatically preserved by a coarse model.

State labels and actual agents' information are distinct. An analyst may retain an outcome for assessment that the agents cannot observe. Policies must use their stated information; including the outcome in \(L\) does not authorize agents to use it.

Let \(q:S\twoheadrightarrow Q\) be a proposed surjective abstraction. We ask for a single quotient model, independent of which fine state in a block is the initial state, with the same input names and with

\[
L=\bar L\circ q,
\qquad
\sum_{t:q(t)=b}K_{u,d}(s,t)=\bar K_{u,d}(q(s),b).
\tag{1}
\]

This is a strong state-level contract. It preserves transitions between abstract states, not merely a selected list of aggregate performance measures. We do not claim it is necessary for every weaker notion of prediction or trace equivalence.

## 2. The faithful-quotient theorem

**Theorem 1.** A quotient satisfying (1) exists if and only if both of the following hold:

1. \(q(s)=q(t)\) implies \(L(s)=L(t)\).
2. For every pair \(s,t\) with \(q(s)=q(t)\), every declared input pair \((u,d)\), and every block \(b\in Q\),

\[
\sum_{v:q(v)=b}K_{u,d}(s,v)
=\sum_{v:q(v)=b}K_{u,d}(t,v).
\tag{2}
\]

When it exists, this quotient is unique for the fixed map \(q\).

**Proof.** Necessity follows by evaluating (1) at \(s\) and \(t\): the right sides agree. For sufficiency, define \(\bar L(a)\) using any representative of block \(a\), and define \(\bar K_{u,d}(a,b)\) by the left side of (1) using any such representative. The two conditions make these definitions independent of the representative. Every entry is nonnegative and the sum over the disjoint blocks is one, so the result is a stochastic kernel. Equation (1) follows by construction. The same equations force the values of any other proposed quotient, proving uniqueness. \(\square\)

Condition (2) is intervention-wise strong lumpability, also expressed as controlled probabilistic bisimulation. The theorem is established mathematics in an explicit form adapted to this programme. A primary predecessor is [Givan, Dean and Greig, *Equivalence Notions and Model Minimization in Markov Decision Processes* (2003), sections 3–4 and appendix](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf). That work develops stochastic bisimulation and model reduction; the present note uses plural labels and separates interventions from boundary inputs rather than introducing a reward-maximization premise.

**Corollary 1: all declared path questions.** If Theorem 1 holds, the fine process projected through \(q\) and the quotient have equal path laws, starting from corresponding initial distributions and using the same policy on abstract histories. Therefore every measurable event of that path has the same probability, including finite deadlines, repeated renewal, harmful recurrence, and conjunctions of different outcome conditions, provided those events were retained in the labels or monitors.

**Proof.** Given any fine history with current state \(s\), the conditional next-block distribution under input \((u,d)\) is exactly the quotient row at \(q(s)\). Conditioning only on the abstract history mixes identical rows and leaves that row unchanged. If an input policy uses the same abstract history in both systems, its conditional input distribution also agrees. Induction gives equality of every finite cylinder probability. Cylinder probabilities determine the path measure on the countable product of finite alphabets, establishing equality for measurable infinite-horizon events as well. \(\square\)

The corollary includes randomized, time-dependent, and history-dependent policies, provided they respect the same information contract. It does not equate arbitrary fine-state policies with policies forbidden to see those distinctions. In particular, a quotient state may contain information available to the analyst but hidden from a participant; a policy depending on that information remains impermissible in both models. Each participant's observation map and action permissions must be preserved, and transferred policies must use only those observations. Full-state bisimulation does not itself authorize observation of the full quotient state. Nor does it preserve an unrecorded internal event merely because some endpoint outcome agrees. Joint next-state/event kernels can be handled by including the event in a finite monitor before applying the theorem.

For a decentralised policy profile, the corollary applies when each participant's observation history and policy are preserved, hence the induced joint input law agrees. It does not replace decentralised information constraints with an omniscient central policy.

## 3. A constructive coarsest faithful partition

Let \(P_0\) partition states by equal labels, including any declared permission distinctions. Given partition \(P_n\), define the signature

\[
\sigma_n(s)=
\left([s]_{P_n},
\left(\sum_{v\in B}K_{u,d}(s,v)\right)_{(u,d),B\in P_n}\right).
\tag{3}
\]

Form \(P_{n+1}\) by grouping states with equal signatures. Equality is exact; for rational kernels it can be decided using rational arithmetic. A floating-point tolerance defines a different approximate problem.

**Theorem 2.** This algorithm terminates and returns the unique coarsest partition refining \(P_0\) that satisfies (2). There are at most \(|S|-|P_0|\) strict refinement rounds. Every faithful deterministic state quotient preserving the declared labels refines the returned partition.

**Proof.** Each new partition refines its predecessor because the old block appears in the signature. Each strict refinement increases the number of blocks by at least one, so the stated termination bound follows. At termination, signatures are constant on blocks, which is exactly (2).

Let \(R\) be any stable partition refining \(P_0\). We show by induction that \(R\) refines every \(P_n\). This holds at \(n=0\). If it holds at \(n\), every \(P_n\)-block is a union of \(R\)-blocks. Two states in one \(R\)-block have equal transition sums to each \(R\)-block by stability. Summing these equalities gives equal sums to every \(P_n\)-block for every input. Their old blocks and signatures therefore agree, so they remain together in \(P_{n+1}\). Thus \(R\) refines the limit. Since the limit itself is stable, it is coarsest. Two coarsest partitions must refine each other and hence coincide. \(\square\)

This is minimality among the specified deterministic state partitions. It is not minimality among all latent-state predictive models, all history-based sufficient statistics, all encodings, or all explanatory theories. The partition may consist of singletons: an exact claim can legitimately yield no compression. Uniqueness of this partition does not imply a unique semantic decomposition into participants, environment, relations, rules, and representations.

**Corollary 2: expanding the question only refines the quotient.** Keep the same fine state space and old kernels. Add permitted input pairs, add label coordinates, or require the same partition to satisfy (2) for every member of an enlarged finite family of kernels. The new coarsest faithful partition refines the old one.

**Proof.** Every partition meeting the expanded requirements meets the old requirements. By Theorem 2, every old-faithful partition refines the old coarsest partition. Apply this to the new coarsest partition. \(\square\)

For a finite model family indexed by \(\theta\), include \(\theta\) in the index of transition sums in (3). The result is a common partition with a potentially different quotient kernel \(\bar K^\theta\) for each model. It is not a single model-independent prediction. Requiring one identical quotient kernel for all models is a stronger cross-model equality condition. If the same fine state and input have genuinely different retained-outcome laws in different models, splitting fine states alone cannot fix that discrepancy; the model index or other relevant uncertainty must enter the state/representation, or the result must remain a family or bound. Observation of that added index is not granted to agents. Allowing the model to switch arbitrarily over time also changes the process class; a theorem for each fixed model does not automatically validate arbitrary switching.

Thus admitting a new intervention, a previously excluded affected party's outcome, or a new family of environmental regimes can expose distinctions that an earlier abstraction omitted. This is a theorem about a nested expansion of the contract, not a claim that every revision of a research question is monotone. It imposes no hierarchy among the added outcome coordinates.

The refinement algorithm also produces witnesses. Whenever a proposed block is split, a particular input and target block have different transition probabilities. Such a difference falsifies that proposed quotient under contract (1), even if passive observations at the original input do not distinguish the states.

**Simple witness.** Let \(S=\{s_0,s_1,g,b\}\), with equal current labels at \(s_0,s_1\), a good label at \(g\), and a bad label at \(b\). Under input `wait`, each state is unchanged. Under input `repair`, let \(s_0\to g\) and \(s_1\to b\) deterministically. Then the abstraction merging \(s_0,s_1\) matches all passive label histories from those states but cannot preserve the repair intervention. No single quotient row can put probability both one and zero on \(g\).

The witness is relative to the declared intervention family. Removing `repair` changes the completeness question. Matching the averaged behaviour of a mixture of \(s_0,s_1\) also does not repair the all-initial-states contract.

## 4. Composition: when faithful parts remain faithful together

Let \(C\) be the state-to-block indicator matrix, \(C(s,a)=\mathbf1\{q(s)=a\}\). Equation (1) becomes

\[
K C=C\bar K.
\tag{4}
\]

**Theorem 3.** A common quotient is preserved by the following operations under the stated restrictions.

**Sequential composition.** If \(K_1C=C\bar K_1\) and \(K_2C=C\bar K_2\), then

\[
(K_1K_2)C=C(\bar K_1\bar K_2).
\]

This follows by substitution and associativity. It applies to the declared sequencing of material effects, observation, execution, and succession when each module actually has the required quotient. Intermediate outcomes must be retained separately if they are part of the question; equality only at the final boundary does not certify their safety.

**Mixtures and guards.** If every \(K_i\) respects the quotient and mixture weights satisfy \(w_i(s)=\bar w_i(q(s))\), with nonnegative weights summing to one, then \(K(s,\cdot)=\sum_i w_i(s)K_i(s,\cdot)\) respects it. Sum the equal block rows with the common weights. A deterministic conditional is the special case of weights zero or one. The guard must be constant within a block, unless equality of its different branches is verified directly.

For a counterexample to unrestricted guards, take two kernels that always go to distinct labelled states \(g\) and \(b\). Each kernel separately respects any partition merging the initial states. Choosing the first kernel at \(s_0\) and the second at \(s_1\) destroys that quotient. Thus composing well-behaved components through a hidden guard can reveal an omitted distinction.

**Independent parallel composition.** If \(q_i:S_i\to Q_i\) respect \(K_i\), and the joint transition is genuinely the product

\[
K((s_1,s_2),(t_1,t_2))=K_1(s_1,t_1)K_2(s_2,t_2),
\]

then the product map \(q_1\times q_2\) respects the product kernel. Summing over a product block factors into the product of the two preserved block sums. This proves the claim; it does not assert independence in a system with shared shocks.

Separate preservation of marginal kernels is insufficient for parallel composition. Suppose two successor bits are individually fair in both fine states, but at one state they are always equal, while at the other they are always opposite. Both marginal models agree; the joint probability of equality is respectively one and zero. A joint event relevant to coordination distinguishes them. Shared noise and cross-level coupling must therefore be represented jointly or verified under additional sufficient conditions.

These results make recursive level-building mathematically precise in a limited sense. A faithful module can be composed with other faithful modules through a declared compatible interface. Naming a higher level does not establish interface compatibility, and a quotient of marginals is not a quotient of their coupled whole.

## 5. An explicit generative instruction set

We now restrict to rational transition probabilities. There are finitely many instruction forms, with rational probabilities encoded as finite data; this is not a fixed finite menu of biased coins. The syntax consists of finite programs using:

- finitely many Boolean registers;
- tests of a single register and a two-branch conditional;
- assignments of zero or one to one register;
- a fresh coin instruction writing one register, with a declared rational probability \(p\in[0,1]\);
- finite sequential composition and termination.

Each program has a bounded number of instructions along every execution. No arbitrary transition function, unbounded loop, or oracle instruction is allowed. Copying a bit can be implemented by testing it and assigning the destination. A conjunction or a lookup can be implemented through a finite tree of bit tests. Coin draws are fresh independent draws conditional on the chosen instruction; correlation between output registers can be created by shared registers and conditional branches.

A macrostep starts with encoded old state and input in fixed registers. These input registers remain unchanged while the next-state registers are constructed. Temporary registers are private to the macrostep and are reset before use. At termination the next-state registers define the output. For repeated execution, the old bank can then be overwritten from the finished next-state bank using tests and single-bit assignments; no row-selection guard runs until that transfer is complete. The macrostep boundary is part of the contract: intermediate writes and instruction costs are not automatically invisible in an application. If interventions or observations can interrupt a partially written state, the macrostep kernel is not the full behaviour to be preserved, and program counter and register updates must be modeled as additional states/events.

**Theorem 4: constructive rational-kernel completeness.** At these macrostep boundaries, the instruction set generates exactly all finite controlled stochastic kernels with rational entries, up to finite state/input encoding and unused binary codes.

**Proof: every generated kernel is rational and finite.** There are finitely many registers and finitely many execution paths. Each path has probability equal to a finite product of rational coin probabilities or their complements. Summing the probabilities of paths ending in a given output gives a nonnegative rational entry. Every execution terminates and outputs exactly one encoded state, so each row sums to one. Invalid binary input encodings can be assigned a fixed default output; they need not occur on the intended state space.

**Proof: every finite rational kernel is generated.** Enumerate the \(N\) target states as \(t_1,\ldots,t_N\). A finite tree of bit tests identifies the current state and input pair. In that branch write

\[
p_j=K_{u,d}(s,t_j),\qquad
R_j=\sum_{i=j}^N p_i.
\]

Beginning with \(j=1\), if \(R_j>0\), use a coin with rational success probability \(p_j/R_j\). On success, write the bit code of \(t_j\) and terminate. On failure, continue to \(j+1\). If \(R_j=0\), that branch is unreachable from the row; assign any fixed terminating output there. At most \(N-1\) nontrivial coins are needed; the final remaining positive mass can be assigned deterministically.

The probability of reaching stage \(j\) is \(R_j\): this holds initially because \(R_1=1\); after failure it becomes \(R_j(1-p_j/R_j)=R_{j+1}\). The probability of outputting \(t_j\) is therefore \(R_j p_j/R_j=p_j\). Writing each destination code takes finitely many one-register assignments. Repeating the construction for every finite source/input branch produces the required program. \(\square\)

The theorem supplies an explicit construction rather than hiding the whole transition inside a function symbol. It also exposes the price: in the worst case the program still stores the original row-by-row probabilities. The number of listed target weights can be \(|U||D||S|^2\). The result is expressiveness, not a compression guarantee, a mechanism-discovery algorithm, or an explanation of where those weights came from.

**Theorem 5: an informative restriction.** If fresh coin instructions are restricted to fair coins, and each macrostep has a bounded number of coin draws, the generated finite kernels are exactly those with dyadic rational entries (rational numbers with denominator a power of two).

**Proof.** If at most \(B\) fair coins can be drawn, pad shorter paths with ignored fair draws. Every output probability is the number of corresponding length-\(B\) bit strings divided by \(2^B\), hence dyadic. Conversely, for any finite dyadic kernel, choose a common denominator \(2^B\) for all its entries. Generate \(B\) fair bits and assign the resulting equally probable strings to output states in the requisite counts, using a finite bit-test tree. Source/input selection remains deterministic. \(\square\)

The one-row distribution \((1/3,2/3)\) is a direct falsifier of completeness for that bounded fair-coin grammar. Allowing an unbounded rejection loop would change the generated class and the resource/termination contract; it is not a free repair within this theorem. Allowing arbitrary real-probability coin instructions would enlarge the class but place real-number information in a primitive. Such extensions must be counted rather than treated as discoveries of an underlying universal mechanism.

The syntax is related to established probabilistic guarded-command modelling. The [official PRISM language description](https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Commands) specifies guarded probabilistic updates; the [module documentation](https://www.prismmodelchecker.org/manual/ThePRISMLanguage/ModulesAndVariables) explains local variables and module interactions. Our compilation proof and its bounded fair-coin restriction are written out above; no novelty claim is made for probabilistic programming or finite-kernel expressiveness.

## 6. What the theorems establish together

For a supplied finite rational model and a declared set of labels, interventions and boundary inputs, the procedure is constructive:

1. Encode its fully specified transition laws using the finite instruction set.
2. Compute the coarsest faithful partition by exact refinement.
3. Construct its unique quotient for that partition.
4. Evaluate retained plural path conditions or compose compatible quotient modules.

This yields a complete representation and reduction method for the stated class. It does not require a uniform goal, a gradient landscape, or an optimal controller. Endogenous rules, learning, competing commitments, succession, and changes to the environment can all be included **when they have a supplied finite representation**.

The construction does not prove that any particular five semantic categories are the uniquely necessary basis. Nor does it derive environmental transition laws, observation channels, harmful outcomes, the legitimacy of changed commitments, or the world's accessible interventions. These are inputs to the model. Placing rules in the state can stop a representational regress within the finite model; it does not explain the causal origins of every rule-update mechanism or make an open system self-sufficient.

The universality theorem is deliberately accompanied by the quotient test and restricted-grammar falsifier. A universal encoder can reproduce every model while explaining none economically. A candidate substantive theory earns stronger status by imposing restrictions that compress or link independently specified mechanisms and by deriving consequences that another permitted model could violate.

## 7. Remaining mathematical targets for a substantive generative basis

A claim that the programme has a full explanatory basis would need additional results that are not supplied here:

- **A substantive domain theorem.** State a class defined independently of the proposed grammar, and prove its members have the required representation. Finite representability cannot be inferred from a finite list of observed variables or actions.
- **Mechanism restrictions.** Identify which local dependencies, information routes, physical budgets, and update forms define reproduction of conditions, and which admissible systems violate those restrictions. Replacing each transition row with a different parameter does not supply this structure.
- **Explanatory compression or invariant consequences.** Show what is derived across systems from common constraints, rather than inserted separately into each kernel. A reduction in state count is one kind of compression, not sufficient evidence of a shared social or biological mechanism.
- **Necessity at a stated level.** Supply a counterexample when an indispensable mechanism is removed, relative to declared outcomes and disturbances. Variable-count minimality is not ontology minimality because tuples can be recoded into one finite variable.
- **Controlled extension.** Prove how new observations, events, interventions, entities, or environmental regimes alter the equivalence relation. A previously sufficient state may cease to be sufficient when the question changes. The correct response is a new contract and refinement, not a retrospective universal claim.

The immediate theoretical gain is therefore precise: a proposed generative state can now fail an exact completeness criterion, and an explicit finite instruction set has a proved generated class and a proved boundary. This is a foundation for testing a stronger explanatory basis, not a declaration that the full basis has already been found.

## Source and proof status

Primary sources above were checked on 5 October 2026. The bisimulation, aggregation, and partition-refinement principles are established. The propositions are proved explicitly here so that their assumptions, intervention scope, composition rules, and limits can be audited directly. The finite compiler is a constructive mathematical exercise and should not be credited as a discovery of a universal alignment mechanism. Existing empirical results remain separate; this note adds no empirical validation.
