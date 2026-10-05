# How actual interactions can force missing distinctions

Independent subtask for the substantive-foundation revision, 5 October 2026. This memo reads sibling work without changing it. Its constructive advance is an exact bridge from measured intervention responses to a required state dimension and a recoverable dynamical recurrence. The example is constructed, not empirical evidence about the universe.

## Judgment

The strongest defensible move beyond `q T = Tbar q` is to stop supplying the reduced state's variables in advance. Start from reproducible input/output responses, then ask which distinctions and state dimension any exact model of those responses must retain. In a restricted class this can be solved constructively. The world, through the responses, rules out entire families of descriptions.

Suggested principle:

> Consequential distinctions are imposed by the stable dependencies through which differences propagate into further interactions. A faithful model must retain enough history or state to reproduce those dependencies across the interventions it claims to cover.

This is a substantive research principle when it makes specific predictions about responses, boundaries, or required memory. “Everything interacts” alone supplies no such predictions. Neither the principle nor the mathematics derives a unique ultimate physical law without measured responses and substantive model-class assumptions.

There are three separate claims, which must not be merged:

1. An actual coupling makes an existing difference affect a chosen outcome.
2. A changed process can produce differences that were not present before.
3. An observer acquires a distinction that was previously absent from its model.

The third can occur without the second; a previously hidden process need not come into existence when it is discovered. The first can change when a new coupling is installed. Deterministic symmetric laws do not, by themselves, guarantee asymmetric outcomes from symmetric initial states, and interaction alone does not guarantee perpetual novelty.

## What the recent sessions add

**Generative basis, `STRUCTURAL-CLOSURE.md`.** Given explicitly supplied local update circuits, close a seed of outcomes, observations and permissions under all their parent dependencies. The resulting least structural boundary supports an exact retained process, including correlated noise. A decorative badge is removable until a new authority rule depends on it; then it enters the boundary. This is a constructive explanation of how a boundary changes under a new mechanism. It remains conditional on the actual circuits, intervention family and question. Syntactic closure can overretain because dependencies can cancel; it does not discover the actual circuits.

Read from `/Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/work/fundamental-root/snapshots/generative-basis/STRUCTURAL-CLOSURE.md`.

**Scientific principles, `integrated-scientific-inquiry.md`.** A complete bounded program connects ordinary outcomes, paid investigation, a change in who has standing, fresh comparison, deployment, and maintenance. Its especially relevant contribution is that the old evaluated target can remain satisfactory while an excluded group encounters failures. New attention need not follow an anomaly inside the old target. Its mechanisms-of-change report also distinguishes missing linked information from a search grammar that cannot combine available fields. The integration demonstrates candidate discovery within an installed grammar; it does not establish unrestricted creation of variables or ultimate criteria.

Read from `/Users/ren/Documents/Codex/2026-10-05/scientific-principles/outputs/integrated-scientific-inquiry.md`, `mechanisms-of-scientific-change.md`, and selected passages of `theory-of-scientific-change.md` and `scientific-change-formal-results.md`.

**Recursive self-modeling, the identification proof and anchor mechanism.** A latent translation can leave all permitted sensor readings and actions unchanged while changing an absolute physical target. Allowing both reference biases to be learned is insufficient when the dynamics fixes the wrong origin. Relative agreement therefore does not create an absolute semantic anchor. A known reference, known dynamics, or calibrated repeated-episode initial distribution can supply an anchor under its respective assumptions. This rules out the tempting claim that input/output identification automatically discovers uniquely interpreted physical variables.

Read from `/Users/ren/Documents/Codex/2026-10-05/recursive-self-modeling/outputs/experiment/identifiability-proof.md` and `correction-access/anchor-mechanism.md`.

**Structural foundations, cycle 6.** A regime distinction can be necessary for one affordable response repertoire and unnecessary when a funded mixture works in both regimes. The need to know is relative to the actual duty and feasible alternatives, not a demand to represent every physical difference. Correct diagnosis can also arrive after implementation is no longer affordable.

Read from `/Users/ren/Documents/Codex/2026-10-05/structural-foundations/outputs/cycle-6/synthesis.md`.

Together these support: actual coupling determines causal relevance; the retained consequences determine the question; access and grammar determine discoverability; resources and response alternatives determine practical necessity. These are connected constraints with independently variable failure modes.

## A precise bridge from responses to a missing dimension

Assume a finite-dimensional, time-invariant linear process during a controlled experiment:

\[
x_{t+1}=Ax_t+Bu_t,\qquad y_t=Cx_t.
\]

An exact common-input comparison of two initial states with difference \(\delta\) produces output differences \(CA^k\delta\). Thus the unobservable differences are exactly

\[
\mathcal N=\bigcap_{k\ge0}\ker(CA^k).
\]

By the characteristic polynomial of an \(n\)-dimensional \(A\), the first \(n\) powers suffice. The observable quotient is \(\mathbb R^n/\mathcal N\). This identifies which differences matter for the declared channel even when individual coordinates are interchangeable. Input-driven identification additionally concerns which directions can be reached through \(B\).

For zero initial state, measured impulse coefficients are \(h_k=CA^kB\). With \(u_0=1\) and all later inputs zero, \(h_k\) is \(y_{k+1}\); the time alignment is part of the experiment. Arrange them in a block Hankel matrix. A finite block factors as an observability matrix times a reachability matrix, so its rank cannot exceed the state dimension of any compatible linear realization. For a minimal reachable and observable realization, sufficiently large blocks attain that dimension. This is established realization theory, not a new theorem of this project. [Frazzoli, MIT, Minimal Realizations, slides 2 and 8–9](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/c4b2f9d80e51e07a7f1ff6e7be4308e7_MIT6_241JS11_lec21.pdf).

The important change from the previous foundation is epistemic: an actual response sequence can require a dimension the learner did not initially postulate.

### Constructed two-coordinate example

Take

\[
A=\begin{pmatrix}a&\gamma\\0&b\end{pmatrix},
\quad B=\begin{pmatrix}0\\1\end{pmatrix},
\quad C=\begin{pmatrix}1&0\end{pmatrix}.
\]

The first coordinate is observed. The second is perturbed by the input, and coupling \(\gamma\) transfers its influence to the first. Direct multiplication gives

\[
h_0=0,\quad h_1=\gamma,\quad
h_2=\gamma(a+b),\quad
h_3=\gamma(a^2+ab+b^2).
\]

Consequently

\[
\det\begin{pmatrix}h_0&h_1\\h_1&h_2\end{pmatrix}
=-\gamma^2.
\]

For \(\gamma\ne0\), every exact time-invariant linear realization needs at least two state dimensions. The displayed two-dimensional mechanism attains the bound. An elementary alternative proof is that a scalar state has \(h_1=\alpha h_0\), which cannot combine \(h_0=0\) and \(h_1\ne0\). A delayed input counts as memory and cannot be silently exempted from the state dimension.

This is stronger than noticing a prediction error and adding an arbitrary variable: the intervention response establishes a lower bound on the necessary memory.

The same data recover coefficients of a law. When \(h_1\ne0\), set

\[
s=\frac{h_2}{h_1},\qquad
p=s^2-\frac{h_3}{h_1}.
\]

Then \(s=a+b\), \(p=ab\), and the characteristic polynomial gives the whole response recurrence

\[
h_{k+2}=s h_{k+1}-p h_k.
\]

For \(a=1/2,b=1/4,\gamma=1/8\), the first terms are

\[
0,\;1/8,\;3/32,\;7/128,\;15/512,\ldots
\]

The inferred recurrence is \(h_{k+2}=\tfrac34h_{k+1}-\tfrac18h_k\). Exact rational calculation fitted the first four terms and reproduced ten subsequent terms obtained from direct state evolution. The small check is saved in `work/substantive-foundation/distinctions-bridge-check.json`. This validates the arithmetic and construction, not an empirical natural law.

The requested broader exact check is implemented by `work/substantive-foundation/check_distinction_bridge.py` with results in `distinctions-grid-checks.json`. It covers 245 rational parameter triples: 196 nonzero-coupling systems and 49 uncoupled controls. The seven values used for each rate include negative, zero, repeated, stable and unstable cases; the five coupling values include both signs and zero. For each nonzero case, four terms determine the candidate recurrence and 28 further terms agree with direct state evolution. Every two-by-two determinant and scalar-state exclusion holds, and an independently applied nontrivial similarity transformation preserves all 32 responses. The grid checks an algebraic claim over varied examples; the symbolic derivation covers arbitrary real rates and nonzero real coupling.

If coupling is removed, the input no longer affects the observed output under the declared zero initial state. The second coordinate becomes invisible to this experiment. This does not imply that it ceases to exist, that arbitrary initial variation of the first coordinate is irrelevant, or that no other observation channel can reveal it.

### What this example does and does not discover

It recovers the minimal order and invariant recurrence of a response family, with predictions for interventions not used for fitting. It does not uniquely identify the physical names of latent coordinates. Similarity transformations change internal coordinates without changing the response; even the ordering of the two rates need not be identified by this scalar response. Physical interpretation requires additional calibrated connections or interventions.

The two-state conclusion is relative to the linear, time-invariant state-space class. It is not a model-free theorem about all conceivable encodings; unusual nonlinear encodings can pack multiple variables into a single real number, while explicit time dependence can hide memory in a clock. Declaring what counts as a state and admissible update law is essential.

There is also a crucial lower-bound/upper-bound distinction. A nonzero finite Hankel minor genuinely rules out every lower-dimensional linear realization of those observations. A finite run of successful predictions does not prove that no higher-order mode is present. Add a parallel delay chain whose first nonzero response arrives after the last observed term: it leaves the entire finite record unchanged and alters later responses. The construction's two-state equations supply the exact upper bound and justify the all-time recurrence. In an empirical application the recovered recurrence is a tested candidate until a justified order bound, verified mechanism, or further relevant evidence supplies stronger warrant. This is a place where a rigorous result about missing distinctions coexists with continuing openness to additional ones.

## A falsifiable experimental version

This is a proposed protocol, not an experiment performed here:

1. Specify a repeatable operating regime, independently calibrated input and output channels, an initial preparation, and the admitted linear approximation and error budget.
2. Obtain repeated impulse responses at multiple small amplitudes. Test superposition, time shifts and drift before treating one response as a stable law.
3. Estimate the necessary Hankel rank with uncertainty bounds; fit the response recurrence on an initial segment.
4. Predict held-out impulse tails and combined input sequences, including preparations and amplitudes not used to choose the order.
5. If a proposed removable coupling can actually be changed, predict how that intervention changes response rank and recurrence, and test it.

A lower bound on model order is supported when the second singular value exceeds the stipulated measurement/model-error bound. Failure of the held-out response predictions challenges the class, regime, calibration or fitted law. It does not authorize adding an unmeasured hidden term after every failure while retaining the original claim of prediction.

Finite noisy data cannot generally establish exact absence of a coupling. A small undetected coupling can matter over a long horizon or under a different intervention. Approximate relevance must therefore declare the measurement precision, horizon and outcome tolerance; exact causal irrelevance is a stronger claim.

## Recommendation to the main synthesis

Use the general idea of stable, composable intervention responses as the operational place where the world constrains a theory. Add the constructive realization example to show that both variables and law coefficients can be demanded by evidence. Link this to the sibling structural closure result: local mechanisms propagate relevance backward through dependencies, while response data can reveal that the initial list of mechanisms or dimensions was insufficient.

Do not state that the world uniquely supplies one privileged set of named variables, that all consequential distinctions must be consciously discovered, or that physical distinguishability determines moral standing. Instead say: once a question and an intervention interface are declared, nature can force distinctions and rule out proposed laws; inquiry can then extend both the question and the interface. That is a stronger answer to the missing-possibility problem than a general instruction to remain open, and it has precise failure conditions.
