# What unrestricted universality can and cannot supply

Research note, 5 October 2026. These are mathematical statements about declared classes, not empirical claims about the actual universe. The reductions below are written proofs; the accompanying finite illustrations do not establish undecidability by experiment.

## 1. An exact separation: representing a law versus selecting it

Let a root schema describe a successor relation by

\[
J(x)=\{x\mathbin{\oplus}i:i\in I(x)\}.
\]

For any relation \(R\subseteq X\times X\), choose \(I(x)=\{y:xRy\}\) and define \(x\oplus y=y\). Then \(J(x)\) is exactly the successor set of \(R\). Thus this unrestricted schema represents every relation on the chosen state space.

**Representation proposition.** If the schema imposes no further restrictions on \(I\) or \(\oplus\), it cannot entail any property of \(R\) that is false of at least one relation on that space.

**Proof.** Every such counterrelation is an admitted instance of the schema by the construction just given. A conclusion of the schema must hold in every instance. Therefore the counterrelation prevents the proposed entailment. \(\square\)

The proposition does not say the schema is useless. It can unify descriptions, support exact conditional theorems, and express constraints on feasible control. It says that a law selecting some dynamics and excluding others requires additional content. Nor must a useful foundational theory select a unique history: a restrictive family of laws can be scientifically substantive while leaving boundary conditions and chance open.

This also identifies a completion that is attainable now: a universal **semantic** definition of the winning set can apply to all systems represented by the schema. Whether the world belongs to a narrower, empirically justified law family is a separate question. The established greatest-fixed-point safety theorem already gives such a semantic characterization with observation and action-availability semantics included. Its arbitrary-set version concerns unrestricted causal strategies selected with ordinary set-theoretic choice; computability, measurability, and physical realization require separate justification.

## 2. No total effective exact evaluator for all computable instances

Consider the following particularly simple model class:

- State descriptions are finite strings or natural numbers, so the state set may be countably infinite.
- The next-state function is total and computable.
- There is one available action, complete observation, and no environmental uncertainty.
- Whether a state is protected is decidable.
- A progress output is an explicitly identified fresh integer, not an unstated judgment of meaningful novelty.

Even in this class, there is no algorithm that always terminates and correctly decides, for every finite system description and initial state, whether protection lasts forever. The same impossibility holds for indefinitely producing fresh integers while remaining protected.

### Explicit reduction

Take an arbitrary program \(M\) and input \(w\). Its ordinary execution has finite configurations \(c\); determining whether a configuration is halted, and taking one machine step from a nonhalting configuration, are computable operations. Define a new system with states

\[
S=(\mathrm{Configurations}_M\times\mathbb N)\cup\{\bot\},
\qquad K=S\setminus\{\bot\}.
\]

The initial state is \((c_{M,w},0)\). Its sole transition is

\[
F(c,n)=
\begin{cases}
\bot,&c\text{ is halted},\\
(\mathrm{step}_M(c),n+1),&c\text{ is not halted},
\end{cases}
\qquad F(\bot)=\bot.
\]

Each nonhalting simulation step outputs the new integer \(n+1\). The map from \((M,w)\) to this system's finite description is effective. Its next-state function is total: each call performs at most one machine step, regardless of whether the simulated program eventually halts.

- If \(M(w)\) never halts, the system remains in \(K\) forever and outputs \(1,2,3,\ldots\).
- If \(M(w)\) halts after \(T\) steps, the system reaches \(\bot\) on the following transition and has produced only finitely many outputs. The extra transition merely makes the convention explicit.

Therefore

\[
\boxed{\text{indefinite protection and endlessly fresh outputs}
\iff M(w)\text{ does not halt}.}
\]

A total exact evaluator for this class would decide nonhalting, and therefore halting, by applying it to the constructed description. That contradicts computable undecidability of the halting problem. For the standard diagonal argument and careful historical attribution, see [Hamkins and Nenu, section 1](https://arxiv.org/pdf/2407.00680). Their paper also explains why the familiar modern halting proof should not be described as appearing verbatim in Turing's 1936 paper.

The restriction to a countably infinite state class matters. This reduction does not contradict the exact finite-state algorithms already established. It uses the possibility of unbounded computation and storage; it does not assert that every physical system supplies those resources, or that physical systems can perform infinitely many steps in finite elapsed time.

### What the reduction does and does not decide

It rules out the package **all computable instances + total termination + exact yes/no classification**. It does not rule out a universal law, a uniform implicit characterization, useful finite subclasses, sound sufficient certificates, approximate analysis, or procedures that are allowed to return "unresolved". It does not imply that an effective theory cannot prove important universal theorems: the displayed reduction is itself one. It also does not justify claiming that all real instances are unanswerable. Many particular instances have short proofs.

In particular, the greatest-fixed-point formula can characterize a winning set exactly even when membership has no general terminating algorithm. An exact definition and an effective way to decide every instance are distinct mathematical achievements.

## 3. A fixed effective certificate system cannot cover every true instance

The boundary is stronger than the absence of one convenient solver.

**Certificate limitation.** For the simulation class above, there is no sound, effectively enumerable certificate system that certifies every system which is protected forever.

Here "effectively enumerable" means that candidate certificates and successful certification can be systematically searched. A terminating computable checker on finite certificates is a familiar sufficient implementation of this condition. Sound means that every certified continuation claim is true.

**Proof.** Suppose such a complete and sound system exists. Given \((M,w)\), construct the simulation system and interleave two effective searches:

1. Simulate \(M(w)\), stopping with "halts" if it halts.
2. Search for a certificate of indefinite protection, stopping with "does not halt" if one is found.

If \(M(w)\) halts, search 1 eventually succeeds and soundness prevents an incorrect certificate. If it does not halt, completeness makes search 2 eventually succeed. Thus the combined procedure always terminates with the correct answer, contradicting the preceding undecidability result. \(\square\)

This is a specific incompleteness consequence of the reduction, not an invocation of Gödel's theorem without hypotheses. It concerns one fixed sound effective certification scheme over the unrestricted class. It does not prevent stronger theories from settling previously unresolved instances, and it does not prevent complete non-effective semantic descriptions. Increasing expressive coverage can therefore force a choice among effective completeness, soundness, or the scope of the admitted systems.

For the proposed root, the practical conclusion is to preserve three honest result types: a verified continuation certificate, a verified obstruction, or an unresolved case. An unresolved case is not proof of impossibility or evidence that generation must continue.

## 4. No fixed observation duration establishes inexhaustibility throughout this class

For every natural number \(N\), define two total computable transition systems on \(\mathbb N\cup\{\bot\}\), both starting at zero and treating every natural-number state as protected:

\[
F_\infty(n)=n+1,\quad F_\infty(\bot)=\bot,
\]

\[
F_N(n)=\begin{cases}n+1,&n<N,\\\bot,&n\ge N,\end{cases}
\quad F_N(\bot)=\bot.
\]

Both produce exactly the observed state prefix \(0,1,\ldots,N\). Their next states differ: \(N+1\) and \(\bot\). The first produces endlessly distinct protected states; the second stops doing so.

The quantifier is: for every finite duration, there exists such a pair. Merely increasing the duration of successful observation is therefore not a uniformly sufficient test across this unrestricted computable class. Some particular finite records can be conclusive under independently justified premises: an observed complete state repeating under a fixed deterministic transition law supplies a cycle certificate, and a complete finite transition table can support an invariant proof. This construction does not say that finite evidence is worthless or that justified inference is impossible. Additional law restrictions, prior information, experiments, and representation contracts supply the premises that an unrestricted observation-duration argument lacks.

## 5. Consequence for the requested full root

There are two distinct conclusions, and neither should be inflated:

1. A universal structural characterization of possibility can be exact while taking mechanisms, observation rules, and criteria as arguments. We already have this for safety in the established set-based model. This is real mathematical universality within that class.
2. Unrestricted representation does not derive the mechanisms or evaluate every instance effectively. No amount of further finite simulation can turn arbitrary supplied dynamics into one empirically restrictive law, and the computability reduction prevents a total exact evaluator for all computable systems.

These results close a specific uncertainty about what a "full root" could promise. If it means a universal organizing language and conditional structural theory, the existing results already supply part of that foundation. If it means an assumption-free law that selects all physical mechanisms and normative criteria, that does not follow. If it means an always-terminating exact method for all computable continuation problems, the claim is false under the explicit class above.

The obstruction is not a reason to stop theory building. It tells us to state the target accurately: unrestricted semantic scope can coexist with sound but incomplete certificates, while substantive empirical claims require restrictions that can fail against independently specified observations.

## Finite illustration

`universality_barrier_examples.py` checks the indexing and divergence of the finite-prefix construction for 201 values of \(N\), and checks the simulator wrapper against elementary halting and nonhalting toy programs over finite horizons. Its JSON output deliberately labels these as finite illustrations. They do not constitute the general mathematical proof or an empirical test of the philosophical theory.
