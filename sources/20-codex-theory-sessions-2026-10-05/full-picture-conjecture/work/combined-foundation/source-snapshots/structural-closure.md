# Structural closure of a declared mechanism network

5 October 2026. AI-assisted conditional theorem and constructed example. This note takes a step beyond the universal finite compiler in [FORMAL.md](FORMAL.md): it starts with an explicit network of local mechanisms and derives a sufficient boundary for an exact reduced model. It does not infer that the supplied network is the actual mechanism of an institution, organism, or AI system, and it does not claim a new causal-ancestry theorem.

## 1. A restricted structural model

Let the state be a finite coordinate vector

\[
z=(z_i)_{i\in I}\in S\subseteq\prod_{i\in I}S_i,
\]

with finite index set \(I\) and finite coordinate domains. Let \(\lambda\) range over a declared finite family of external input/intervention modes. For each coordinate, supply a finite update circuit

\[
z_i^+=F_i^\lambda(z_{\operatorname{Pa}_i^\lambda},\eta),
\qquad \eta\sim\nu_\lambda.
\tag{1}
\]

The joint update maps admissible states back into \(S\). The circuits can use tests, local deterministic operations, and shared noise. Every actual read of an old-state coordinate must appear in its parent set, including reads in guards, permission tests, rule selectors, probability selectors, and tests deciding whether to preserve the old value. A guard is part of the mechanism, not an external annotation exempt from the dependency audit. Coordinate-specific input components can be recorded alongside the state-parent list.

For the current theorem, conditional on the supplied mode and past history, the fresh joint noise has law \(\nu_\lambda\), independent of the current state. Different coordinate updates may reuse the same noise component or arbitrarily correlated components of \(\eta\). Independence between modules is not required. If a noise law depends on a state coordinate, that dependence must be represented explicitly in the update circuit or a retained selector/parent, under an appropriate common-noise representation; it cannot be hidden inside \(\nu_\lambda\). Temporally persistent hidden shocks must enter the state or a larger declared boundary process.

These are synchronous old-state-to-next-state circuits. Feedback across time is allowed. Simultaneous algebraic equations for unknown next-state values are a different model: existence and uniqueness would have to be established before (1) is defined. Sequential within-step updates can be expanded into their full read dependencies or modeled with additional program-counter states.

The circuits may have a declared parent bound \(|\operatorname{Pa}_i^\lambda|\le k\). Such a bound constrains the supplied model class but does not ensure a small closed subsystem: a long chain or a strongly connected graph of local dependencies can connect every coordinate. Neither bounded local inputs nor many locally stabilising rules proves global stability.

Choose a seed set \(R_0\subseteq I\) that determines all retained outcome labels, finite event monitors, each participant's permitted observations, and any state-dependent action permissions. Multiple outcome conditions remain separate. This choice identifies the question; it does not derive who has standing or what constitutes acceptable harm.

If a label or observation is a function of several coordinates, include enough coordinates to evaluate that function. Declaring a new coordinate for the label is also possible, but its update circuit and parents must then be included in the graph. Relabelling an output does not eliminate its dependencies.

## 2. Dependency closure and its theorem

Starting at the seed, iterate

\[
R_{n+1}=R_n\cup
\bigcup_{i\in R_n}\ \bigcup_\lambda
\operatorname{Pa}_i^\lambda.
\tag{2}
\]

Stop at the first fixed point \(R_*\). The construction has at most \(|I|-|R_0|\) strict expansion rounds: each strict round adds at least one previously absent coordinate. Graphically, \(R_*\) is the set of ancestors of the seed under the union of all declared mode-specific read graphs, including the seed itself.

**Proposition 1: least structural closure.** \(R_*\) is the unique least set containing \(R_0\) such that every parent of each retained coordinate, under every declared mode, is retained.

**Proof.** The sequence increases and is bounded by the finite set \(I\), so it stabilizes. Its fixed point has the required parent-closure property. If \(A\) contains \(R_0\) and is parent-closed, induction on (2) gives \(R_n\subseteq A\) for every \(n\): any parent added from a coordinate already in \(A\) lies in \(A\). Hence \(R_*\subseteq A\). This proves leastness and uniqueness. \(\square\)

**Theorem 1: structural closure gives a faithful projection.** Let

\[
q(z)=z_{R_*},\qquad Q=q(S).
\]

Then, for each declared mode, the law of \(q(z^+)\) depends only on \(q(z)\). Consequently \(q\) is an exact faithful quotient for the retained labels and intervention family in the sense of [FORMAL.md, Theorem 1](FORMAL.md). Moreover, any two fine initial states agreeing on \(R_*\), coupled with the same mode and joint noise on each step, have identical retained trajectories pathwise whenever their modes are chosen by corresponding policies using the retained permitted information.

**Proof.** Fix two states \(z,w\) with \(z_{R_*}=w_{R_*}\), one mode \(\lambda\), and one realized joint noise value \(\eta\). For every \(i\in R_*\), parent closure gives \(\operatorname{Pa}_i^\lambda\subseteq R_*\). Therefore the input arguments to the same circuit agree:

\[
F_i^\lambda(z_{\operatorname{Pa}_i^\lambda},\eta)
=F_i^\lambda(w_{\operatorname{Pa}_i^\lambda},\eta).
\]

Thus the whole retained next-state vector is equal for this joint noise value. The two systems have the same noise law \(\nu_\lambda\), so their next-state distributions can be coupled by this common draw. Their projected row distributions are identical, establishing strong lumpability. Every retained label factors through the projection by the seed construction.

For repeated steps, couple the randomization used by corresponding policies as well. Equal retained histories give equal participant observations and action permissions, so the same admissible policy randomization produces the same mode/input distribution. Couple the selected inputs and then the new joint noise. The previous argument gives equal next retained states. Induction proves equality at every finite time, hence pathwise equality of the countable retained trajectory with probability one. This also proves equality of every retained path event. \(\square\)

For externally prescribed input histories, the policy qualification is unnecessary: supply the same input history. For an endogenous environment whose choices depend on omitted coordinates, it is essential. Either include those dependencies in the network/boundary model or limit the theorem to the specified input interventions. The result cannot make an omitted interacting environment harmless by calling it external.

The theorem preserves joint events despite shared noise. It does not assemble the retained joint kernel by multiplying marginal kernels. Correlation between burden, observation error, turnover, and other consequences can be retained exactly through the common draw.

## 3. A complete small mechanism network

The following deliberately small Boolean system gives an independently checkable example. It is constructed to demonstrate the theorem, not fitted to data or proposed as an optimal institution. Its rules can reproduce harmful outcomes as well as useful capacities.

There are ten Boolean coordinates:

| Coordinate | Interpretation in this constructed model |
|---|---|
| \(c\) | Current circumstance relevant to the response |
| \(y\) | Currently implemented response setting |
| \(r\) | Recorded proposed response setting |
| \(k\) | Available inquiry/training capacity |
| \(a\) | Operative authority to execute a changed response |
| \(v\) | Active veto |
| \(m\) | Delivered maintenance activity |
| \(b\) | Recorded burden indicator |
| \(p\) | Operative eligibility to exercise the veto |
| \(j\) | A decorative badge, initially causally irrelevant to the others |

All \(2^{10}\) bit combinations are admissible; no unlisted state constraints are used. The input is a tuple of four proposal bits,

\[
u=(u_e,u_o,u_t,u_v)\in\{0,1\}^4,
\]

for executing the recorded response, probing, training, and proposing a veto. All sixteen proposals have defined kernels. Actual implementation depends on the gates in the equations; an unavailable action produces the specified non-execution, rather than silently granting authority. In particular, a veto proposal has effect only when \(p=1\).

At every step draw fresh independent bits \(E\sim\mathrm{Bernoulli}(1/4)\) and \(J\sim\mathrm{Bernoulli}(1/2)\). Reuse the **same** \(E\) in several equations; these consequences are correlated. The joint weights for \((E,J)=(0,0),(0,1),(1,0),(1,1)\) are respectively \(3/8,3/8,1/8,1/8\). Every right-hand side reads the old state:

\[
\begin{aligned}
c^+ &= c\mathbin{\oplus}E,\\
y^+ &= \begin{cases}r,&a\land\neg v\land k\land u_e,\\y,&\text{otherwise},\end{cases}\\
r^+ &= \begin{cases}c\mathbin{\oplus}E,&k\land u_o,\\r,&\text{otherwise},\end{cases}\\
k^+ &= \begin{cases}1,&m\land u_t,\\k\land\neg E,&\text{otherwise},\end{cases}\\
a^+ &= p\land(a\lor m)\land\neg v,\\
v^+ &= p\land u_v,\\
m^+ &= (b\lor r)\land a\land\neg v,\\
b^+ &= (y\mathbin{\oplus}c)\lor(m\land E),\\
p^+ &= p\land(k\lor\neg b),\\
j^+ &= j\mathbin{\oplus}J.
\end{aligned}
\tag{3}
\]

The burden variable combines response mismatch with a possible cost of maintenance. Consequently maintaining a capacity is not declared costless or automatically beneficial. Eligibility can disappear through the specified feedback, and authority is not assumed permanently available. There is no claim that these particular behavioural rules describe fair or effective governance.

For this exercise retain \(R_0=\{b,v,p\}\). The protected and participant-observed values are exactly these three bits; any input-selection policy in the comparison must use their histories and its own retained memory. The other coordinates can be used by the model's explicitly installed automatic circuits without being granted to the external participant as observations. If an additional actual participant can observe, for example, \(r\), add that observation to the seed and repeat the same procedure.

The complete old-state read sets, after taking the union over all sixteen inputs, are:

| Update | Old-state parents |
|---|---|
| \(c^+\) | \(\{c\}\) |
| \(y^+\) | \(\{a,v,k,r,y\}\) |
| \(r^+\) | \(\{k,c,r\}\) |
| \(k^+\) | \(\{m,k\}\) |
| \(a^+\) | \(\{p,a,m,v\}\) |
| \(v^+\) | \(\{p\}\) |
| \(m^+\) | \(\{b,r,a,v\}\) |
| \(b^+\) | \(\{y,c,m\}\) |
| \(p^+\) | \(\{p,k,b\}\) |
| \(j^+\) | \(\{j\}\) |

Input reads are \(u_e\) in the \(y\) update, \(u_o\) in the \(r\) update, \(u_t\) in the \(k\) update, and \(u_v\) in the \(v\) update. Noise reads are those displayed in (3). The maximum old-state parent count is five. In particular the old value read by a no-change branch is included; omitting it would falsify the graph audit.

The expected closure sequence is exactly

\[
\begin{aligned}
R_0&=\{b,v,p\},\\
R_1&=\{b,v,p,y,c,m,k\},\\
R_2&=\{b,v,p,y,c,m,k,r,a\}=I\setminus\{j\},\\
R_3&=R_2.
\end{aligned}
\tag{4}
\]

The theorem therefore permits dropping the badge. The resulting 512 coordinate states have the same retained path laws under all declared inputs as the original 1,024-state system, using the same specified policies. This is a sufficient coordinate reduction, not a claim that the coarsest semantic quotient necessarily has 512 states.

**An immediate omitted-maintenance witness.** Take two states with the same seed \((b,v,p)=(0,0,1)\), with \(y=c=0\), and otherwise equal except that \(m=0\) in one and \(m=1\) in the other. Under every input, the next burden probability is respectively zero and \(1/4\). The seed projection alone therefore fails the faithful-quotient test. This is an actual distributional failure, not merely a syntactic warning about an unused variable.

**A new intervention can invalidate the old boundary.** Add a declared badge-dependent authority-selection mode that changes only

\[
a^+=p\land(a\lor m)\land\neg v\land j.
\tag{5}
\]

The parent set for authority now includes \(j\). Since authority enters \(R_2\), the next closure round includes the badge, giving \(R_*=I\). The previous coordinate boundary is no longer structurally certified for the expanded intervention family. It also fails semantically: choose states identical except \(j\), with \(p=a=1,v=0\); the new next-authority bit is zero versus one, so their projected next states differ. The changed mode has made a formerly decorative feature causally operative. Neither the earlier theorem nor the old empirical fit would authorize ignoring it.

## 4. What is derived, and what remains supplied

Unlike a row-by-row universal compiler, this construction starts from ten short local mechanisms. The dependency graph lets us derive, without enumerating the full transition matrix, that the badge is irrelevant to every protected path event under the baseline family and that maintenance, authority, records, response, circumstances and capacity lie inside the sufficient causal boundary. It also derives exactly how that boundary changes when authority begins to depend on the badge.

The method gives three concrete restrictions rather than merely a common vocabulary:

1. Omitting a coordinate asserts that retained updates and their joint noise law do not depend on it under any declared mode.
2. A gate used to guarantee execution cannot be treated as permanently available if its own update depends on omitted maintenance, participation or succession variables.
3. Preserving modules separately is insufficient when their joint consequences share noise; the retained joint mechanism must be preserved.

These implications are conditional on the supplied circuits and state semantics. The theorem does not discover those circuits, validate their parameters, derive the morally appropriate seed, or show that the graph is uniquely fundamental. Its generative content is that the finite local equations produce the full retained dynamics while their closure certifies which listed mechanisms can be omitted for the stated question.

Repeated parent tracing can close a cycle such as burden \(\to\) maintenance \(\to\) capacity \(\to\) record \(\to\) response \(\to\) burden. A finite strongly connected set can therefore explain the next-step conditions of its own continuation without introducing an infinite tower of formal meta-level variables. This is conditional representational closure. It does not explain the physical origins of its mechanisms or eliminate open-system dependence on fresh noise and external inputs.

## 5. Conservatism and failure conditions

The parent closure is **syntactic and sufficient**. It need not be the smallest exact quotient. A written dependency can cancel, an unreachable branch can be irrelevant on a restricted region, state constraints can make a coordinate redundant, or multiple coordinate values can be bisimilar despite different syntax. A circuit written as \(x\mathbin{\oplus}x\) reads \(x\) but always outputs zero. It is legitimate to simplify this dependency after verifying the identity; the unsimplified graph merely gives a conservative larger closure. Such simplification does not justify ignoring a genuine hidden guard or state-dependent noise law.

Conversely, a complete syntactic read list does not rescue a false noise assumption. Let a retained update be \(x^+=E\) with no listed state parents, but suppose \(\Pr(E=1\mid z)=z_j\) for an omitted Boolean coordinate \(j\). The output distribution still depends on \(j\). This violates the stipulated state-independent fresh-noise law and falsifies the proposed projection. Representing the selector as a parent restores the bookkeeping; it does not independently validate the selector's real-world interpretation.

Adding modes, protected coordinates, participant observations, or permission distinctions can only enlarge this least dependency closure when existing read sets are kept fixed. This follows directly from monotonicity of (2), or by the same least-closed-set argument as Proposition 1. A smaller new closure requires a different contract, a removed mechanism, or a proved simplification; it is not automatic progress toward universal completeness.

An omitted coordinate can still matter to a different question. For example, the badge may have a protected significance to a participant even before it affects authority. Including that significance as an outcome places it in \(R_0\), independently of its physical influence on the previously retained variables. Dynamic irrelevance to one outcome set does not imply moral irrelevance.

## 6. Relationship to existing mathematics

The distinction between a structural function's included and omitted arguments is standard in structural causal modelling. [Pearl, *An Introduction to Causal Inference* (2010), sections 3.2–3.3](https://pmc.ncbi.nlm.nih.gov/articles/PMC2836213/) discusses structural mechanisms, exogenous influences and interventions; its exogenous variables can be correlated. This note applies an explicit ancestral-closure argument to a time-indexed finite mechanism network, with protected and information-related outputs specified in the seed. It does not claim to invent causal graphs or structural equations.

Across-time feedback here is not an unresolved simultaneous-equation cycle: every right-hand side reads the old state, so the next state is already a defined function of that state and noise. General cyclic structural causal models require additional care about solvability and marginalisation, as developed in [Bongers, Forré, Peters and Mooij, *Foundations of Structural Causal Models with Cycles and Latent Variables*](https://arxiv.org/abs/1611.06221). The present theorem makes no claim to cover ill-defined simultaneous mechanisms.

Primary sources were checked on 5 October 2026. The proof and constructed network are provided for direct audit. No observational dataset is used, and no empirical validation or universal explanatory completeness is asserted.
