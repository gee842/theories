# How shared dynamics produce individuals and viewpoints

Research branch for Ren, 5 October 2026. The earlier theories remain unchanged. This investigation develops the [nonseparation proposal](nonseparation-and-selfhood.md) by explaining three transitions: the formation of physical differences, the maintenance of a boundary by the process it supports, and the production of distinct records that guide action within one shared environment.

The strongest result is a conditional mechanism for **differentiation within common dynamics**. One process can support different persistent organizations. Those organizations can encounter different conditions, retain different histories, and regulate different consequences. Their common law does not require identical states or identical access to the world.

Our next candidate foundation is:

> **An individual can be a difference that a process maintains. A functional viewpoint arises when a situated organization retains differences in its encounters and uses them to regulate its continuation. The organization, its standpoint, and their supporting conditions all belong to the shared process.**

The proofs below establish particular mechanisms. They do not deduce all actual beings from monism, explain the origin of the supplied substrate and chemistry, or identify functional information processing with experienced subjectivity. The transitions are proved in separate constructions; an integrated account of their joint physical formation remains a further burden.

## The explanatory steps

| What needs explaining | Mechanism investigated here | Result |
|---|---|---|
| Distinct physical domains | Instability amplifies a perturbation; nonlinear dynamics stabilize it. | Domain membership can follow from the evolved state without a preferred pair partition in the laws. |
| A maintained individual boundary | Internal production replenishes a barrier; the barrier reduces losses from internal activity. | A stable operating regime exists; disruption and rescue identify the boundary's causal role. |
| A functional viewpoint | Local contact writes a record; memory retains it; the record selects consequential action. | Different standpoints can arise within one symmetric global process. |
| A wider understanding | Communication supplies a distinction absent from the local record. | A previously impossible all-state control task becomes possible. |

These are explanatory steps, not a proposed universal sequence of biological evolution. Objects, organisms, agents, and experiencing subjects do not have identical requirements.

## How identical laws generate distinct domains

The earlier four-site exchange model selected useful pairs because some couplings were stronger than others. The new construction removes that preferred grouping. Four identical sites occupy a ring, with identical interactions along all four edges.

Let each site have a dimensionless phase variable \(x_i\), with \(\sum_i x_i=0\). The variable is a signed contrast, not a nonnegative amount. Let \(L\) be the ring Laplacian, so \((Lx)_i=2x_i-x_{i-1}-x_{i+1}\), with indices around the ring. Specify

\[
F(x)=\frac14\sum_i(x_i^2-1)^2+\frac\kappa2x^TLx,
\qquad
\boxed{\dot x=-L\nabla F(x)},\quad \kappa>0.
\tag{1}
\]

The first term favors local alternatives; the second penalizes neighboring differences. Movement follows differences in the resulting chemical potential. These mechanisms, the ring geometry, and initial conditions are supplied premises. No permanent pair boundary is supplied.

The total contrast is conserved and

\[
\dot F=-(\nabla F)^TL\nabla F\le0.
\tag{2}
\]

**Exact threshold.** For \(\kappa\ge1/2\), the unique global energy minimum is the homogeneous state \(x=0\). For \(0<\kappa<1/2\), there are exactly four global minima:

\[
\boxed{x^*=\sqrt{1-2\kappa}\,\sigma,}
\qquad
\sigma\text{ is a cyclic rotation of }(+,+,-,-).
\tag{3}
\]

Each contains two simultaneous connected phase domains. Ignoring the names of the positive and negative phases leaves two possible pair partitions. The law favors neither orientation. A realized state supplies the domain membership.

The proof is short. On the zero-mean subspace, \(x^TLx\ge2\|x\|^2\), while \(\sum_i x_i^4\ge\|x\|^4/4\). Therefore

\[
F\ge1+(\kappa-\tfrac12)\|x\|^2+\frac{\|x\|^4}{16}.
\]

Minimizing this expression and requiring equality in both inequalities gives exactly (3). The Hessian is positive on the conserved subspace at those states, proving local asymptotic stability. Small permitted disturbances relax back.

This is a formation mechanism as well as a classification. Along any pattern in (3), write \(x=a\sigma\). Then

\[
\dot a=2a(1-2\kappa-a^2).
\tag{4}
\]

For \(\kappa=1/4\) and \(a(0)=1/100\), its exact solution is

\[
a(t)=\sqrt{\frac{1/2}{1+4999e^{-2t}}}.
\tag{5}
\]

A small supplied contrast grows and saturates. The interactive illustration shows this exact family, not arbitrary starting states. Some other preparations can approach other local minima at sufficiently small \(\kappa\); no generic convergence to a global minimum is claimed. Raising \(\kappa\) to at least \(1/2\) makes every zero-mean state converge to homogeneity, so the conditions can also dissolve differentiation.

The threshold has a graph-general form. Take a finite undirected graph with at least two sites, nonnegative edge weights, and connected positive-weight edges. Replace 2 by its smallest positive Laplacian eigenvalue \(\lambda_2\). If \(\kappa\lambda_2\ge1\), homogeneity uniquely minimizes the same energy. If \(\kappa\lambda_2<1\), it is unstable and every global minimum is nonconstant. Exact domain shapes require further analysis of that graph.

There is a necessary distinction between unity and perfect homogeneity. Under a symmetric deterministic law with unique solutions, an exactly symmetric initial state retains its symmetry. Applying a symmetry to its trajectory produces the same initial-value problem, hence the same trajectory. Thus \(x=0\) stays there even when unstable. Initial differences or fluctuations must enter the explanation. Turing makes the importance of small irregularities explicit in his original pattern-formation argument. Our model is a phase-separation construction, not his two-species reaction–diffusion system. [Turing, 1952, section 4](https://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf).

The phase domains are real differences in the modeled state. Their interfaces are not impermeable membranes: mobility remains positive across every edge. A persistent pattern alone does not establish a living individual or a viewpoint.

## How an organization can help maintain its own boundary

To explain a stronger kind of individuality, make the barrier itself a produced and decaying variable.

Let \(c\) measure an autocatalytic internal component in a supplied patch, and \(b\) the amount of a surrounding barrier. Fixed feed conditions support net per-capita production \(A>0\) before leakage and crowding. The barrier reduces leakage to \(\ell/(1+b)\), after choosing the unit of \(b\). The internal component catalyzes barrier production from supplied precursor; the barrier decays:

\[
\boxed{
\dot c=\left[A-\frac\ell{1+b}\right]c-qc^2,
\qquad
\dot b=\beta c-\mu b.}
\tag{6}
\]

All rates are positive. This is an explicit reciprocal mechanism: internal activity helps produce the boundary, and the boundary helps preserve the activity. Matter, energy, the leakage law, and potential barrier geometry are premises. Boundary function is endogenous; its entire spatial formation is not derived by this two-variable model.

Set \(s=\beta/\mu\), \(k=q/s\). If

\[
\ell>A>k>0,\qquad D=(A+k)^2-4k\ell>0,
\]

there are two positive equilibria:

\[
b_\pm=\frac{A-k\pm\sqrt D}{2k},\qquad c_\pm=b_\pm/s.
\tag{7}
\]

The origin is locally stable. The lower positive equilibrium is a saddle; the upper is locally asymptotically stable. At the positive equilibria, the Jacobian has negative trace and determinant

\[
\det J_\pm=\pm\frac{\mu b_\pm\sqrt D}{1+b_\pm},
\]

which proves the classification. Nonnegative states remain nonnegative and bounded. A seed is needed: \(c=0\) cannot create itself under these equations.

For \(A=3\), \(\ell=15/4\), and \(q=\beta=\mu=1\), the positive equilibria are \((1/2,1/2)\) and \((3/2,3/2)\). The operating state can restore small disturbances. Sufficiently small seeds instead decay, so sustained individuation depends on establishment conditions as well as on the rule.

Two interventions make the boundary's role testable:

- **Interrupt production.** Set \(\beta=0\). The barrier decays, leakage eventually exceeds net production, and \(c\) tends to zero.
- **Supply the missing support.** With production still disabled, externally maintain \(b=B>\ell/A-1\). Every positive \(c\) then converges to \([A-\ell/(1+B)]/q>0\). The external maintainer has replaced a failed internal contribution.

This is stronger than labeling a collection a self. It identifies a difference whose continuation depends on a causal loop and predicts failure and rescue. It remains dependent on the environment. No repair capacity, membrane chemistry, or source of feed can be obtained merely by declaring the system one whole.

There is relevant empirical evidence that compartments can form through physical interactions. Hanczyc, Fujikawa, and Szostak reported mineral-assisted fatty-acid vesicle assembly, encapsulation, retention, and growth with supplied material. Their division procedure used extrusion through small pores. That demonstrates components of compartment formation; it does not validate equation (6) or establish complete autonomous life. [Primary experiment, 2003](https://www.microeco.ethz.ch/uni/kurs/mikevol03/scinews/Science_302_2003_618.pdf).

## How different viewpoints arise inside one process

A functional viewpoint requires more than persistence. Its organization must actually receive, retain, and use distinctions. A finite construction makes this transition explicit.

Two identical circuits, A and B, inhabit one shared disturbance field \(h=(h_A,h_B)\), with each bit either 0 or 1. Each has a sensor, retained record, actuator, and continuing-function bit. A shared three-phase clock supplies a sensing period, a retention/communication period, and a response period. The clock and both circuits belong to one global transition rule.

During sensing, a viable circuit physically copies its local input: \(r_A\leftarrow h_A\), \(r_B\leftarrow h_B\). During retention, both current sensor inputs are blank, but the records remain. Their histories can therefore differ despite identical present input.

| Record | Shared field states it leaves possible |
|---|---|
| A records 0 | 00 or 01 |
| A records 1 | 10 or 11 |
| B records 0 | 00 or 10 |
| B records 1 | 01 or 11 |

The viewpoints are different physically produced partitions of the same possibilities. Their difference follows from causal contact. Swapping A and B commutes with the global dynamics; neither receives a privileged law. Equal full histories need not produce different records merely because we give the sites different names.

In the local regulation mode, the required compensation is \(a_i=h_i\). A mismatched response disables that circuit's future sensing and action. Starting with both circuits functioning, the implemented controller uses \(a_i=r_i\), preserving both across all four field states. Flipping a retained record before response makes its circuit fail while the other continues. The record is causally used, rather than merely correlated with the surroundings.

Each site consequently has a functional significance for a different part of the field: a distinction matters because it changes the action needed for that site's continuation. The resulting indexical is operational: **this record guides this action affecting this continuing organization**. It requires no unmodeled controller outside the global process.

The construction supplies its sensors, memory, actuator law, timing, and vulnerability. It explains the production and use of differentiated records given those mechanisms; it does not explain their biological genesis. Calling the functioning bit viability stipulates a functional criterion, not a moral value or an account of subjective wellbeing.

## When a local viewpoint must expand

Let \(\Omega\) be the allowed field states, \(R(\omega)\) the record produced, and \(T(\omega)\) the uniquely required action. An action rule using only that record can always succeed exactly when

\[
\boxed{R(\omega)=R(\omega')\ \Longrightarrow\ T(\omega)=T(\omega').}
\tag{8}
\]

Equal records force the same response, which proves necessity. If the implication holds, choose the common required response on each record class, proving sufficiency.

Now change the disturbance coupling so both circuits need the parity \(h_A\oplus h_B\). Neither local record suffices. To A, 00 and 01 are identical, although they require opposite responses. For a uniform preparation over the four field states, every policy based only on one local bit succeeds on exactly half; randomization cannot improve that average.

Enable a physical message link that copies the other circuit's record during the retention period. Each controller can then compute the required parity. Both succeed in every allowed field state. The claim is exact for this finite model, not a general guarantee that communication always resolves disagreement.

This is a substantive account of multiple viewpoints within common dynamics: the circuits coexist, their continuations depend on a shared disturbance, and exchanging their different records changes what they can accomplish. A global analyst's description never becomes information freely available to either local controller.

It also sharpens the original missing-possibilities question. **Find two possible situations that leave the current record unchanged but change the consequential response.** Such a pair proves that the viewpoint omits a necessary distinction. Looking at other standpoints, earlier histories, and effects outside a chosen boundary can supply that witness. There is no guaranteed search for every unknown omission in an unrestricted world.

## What the other sessions add

The newer continuing-realizability work asks which responses a situated system can actually implement through its information, memory, resources, permissions, and time. Its renewal results add a condition our ideal circuits omit: vulnerable sensing and execution capacities need recurring support. A viewpoint's continued existence therefore requires more than retaining a mathematical mapping from world to record.

One result gives an explicit counterfactual. In a finite acyclic network of support types, where every instance has a bounded lifetime and later instances require a currently functioning predecessor, with no later external organizational entry, all supports expire by a finite path-lifetime bound. Persistence beyond that bound demands correction of at least one premise, such as recognizing a renewal cycle or recurring external provision. A cycle alone does not guarantee sufficient rates or joint feasibility. This makes continued sensing and action themselves explanatory targets.

The ongoing chat titled **Articulate Foundation Lenses** further distinguishes maintaining a present function from maintaining the ability to transform it. Its completed conceptual proposal is useful here; its current unfinished investigation is not treated as verified evidence. A learning viewpoint may need to revise its sensing, records, boundaries, or control practices when their old organization becomes inadequate.

The source snapshots and review scopes are recorded in the evidence file. Other sessions' experiments were not rerun. These contributions extend the present mechanism without converting functional continuation into a universal definition of health or goodness.

## What this explains about unity and selfhood

The constructive answer is a sequence of causal relations:

**Shared interactions can amplify differences. Stabilizing dynamics can preserve them. Reciprocal production can maintain an interface. Selective contact can produce different records. Using those records to regulate continuing activity supplies a functional standpoint.**

Each transition has conditions. A uniform stable medium need not differentiate. Several alternative attractors need not be simultaneous individuals. A passive pattern need not maintain its boundary. A recorder need not use its information. A controller's functioning does not establish experience.

Within those limits, numerical unity no longer conflicts with differentiated individuals. A common process can contain real, causally consequential differences without giving any of them absolute independence. Operational boundaries of information, control, and material maintenance can also differ: communication extends access, tools extend action, and dependencies extend beyond both. A single universal cut around the self is not guaranteed.

The proposed root is therefore **maintained differentiation within shared conditions**. For knowing and acting beings, it becomes maintained differentiation of access, memory, and response. An apparent self can be examined through the mechanisms that establish and renew this organization, rather than assumed to be an independent owner of it.

This is compatible with monism, but does not decide metaphysical grounding against relational pluralism. Nor does it yet explain why any functional standpoint has a felt interior, which organizations have one, or how experienced subjects are individuated. Those questions need an explicit bridge to experience and independently justified evidence. We have explained mechanisms of functional differentiation; phenomenal subjectivity is a separate unresolved target.

The next physical integration test is concrete: in one spatial model or experiment, show that a formed compartment maintains its own interface and sensing/action machinery; demonstrate distinct histories and interventions for coexisting compartments; then disable and restore the relevant supports. The present constructions identify the mechanisms and discriminating tests, but their separate success does not certify that full integration.

## Verification and preservation

All 23 pre-existing output files are preserved unchanged. The [evidence record](differentiation-evidence.json) includes proof notes, exact check programs, results, source scopes, peer reviews, and preservation hashes.

The phase-domain checks cover 2,744 exact conservation/dissipation cases and energy identities, 21,952 symmetry identities, 224 invariant-mode equations, and 1,029 dissolution bounds. The barrier model has exact fixed-point/stability checks and four numerical intervention trajectories verified at two integration steps. The viewpoint model has 12,288 symmetry checks, 128 regulation trials, eight record interventions, and 32 exhaustive tests of the sufficient-record criterion. The displayed proofs establish the general conditional claims; these finite checks detect calculation errors. No new organism, human-subject, or consciousness experiment was performed.
