# Relational selves, maintained organization, and answerability

Research audit, 5 October 2026. Existing deliverables were read and preserved. This audit supports a new branch, rather than replacing the retained theories. The mathematical model below is newly constructed; the corpus findings are inherited; the philosophical proposal is a synthesis.

## Strongest defensible positive formulation

> **A self can be a maintained, situated organization of a common process: a real center of sensing and action whose continuation depends on conditions it does not independently supply. Its boundary organizes relations rather than abolishing them.**

This permits a precise reading of “no self”: no independently self-existing, externally sovereign controller is required to explain the modeled organization. It does not mean that there are no individuals, experiences, distinct causal roles, or reasons to protect someone. Those are different claims. A person's experiences are not shown to belong to everybody merely because the conditions of that person are shared.

The existing joint-organization branch already derived relatively autonomous coarse units from connected dynamics. The new step below shows how an organized state can remain stable while the original material continuously disappears. It is a constructive instance of persistence through replacement. It does not assume that every part affects every other part at every moment, or that every thing is an agent.

## Exact maintained-organization model

Let \(x,y\) be concentrations of two mutually supporting species. Let \(a,b,\delta,\mu,c>0\), and let \(f\ge0\) be a resource level held fixed by the environment over the modeled interval. The reservoirs supply newly produced material; \(b\) includes the maintained precursor conditions for producing \(y\). This is an open system, not a creation of matter from nothing.

\[
\dot x=afy-\delta x-cx^2,\qquad
\dot y=bx-\mu y.
\tag{S1}
\]

The positive quadrant is forward invariant: on either coordinate axis the missing species has nonnegative derivative. The rates specify reciprocal production, ordinary loss, and a density-dependent loss of \(x\). No separate controller occurs in the equations. The species, reaction capacities, and reservoirs are supplied assumptions; the model does not derive them.

**Existence.** A strictly positive equilibrium exists exactly when

\[
\boxed{abf>\delta\mu.}
\tag{S2}
\]

Substitution of \(y_*=(b/\mu)x_*\) gives

\[
x_*={abf/\mu-\delta\over c},\qquad
y_*={b\over\mu}x_*.
\tag{S3}
\]

Below the threshold, no positive equilibrium exists. At equality, the only nonnegative equilibrium is still the origin; the nonlinear loss removes the neutral continuum of the earlier unsaturated linear model. The zero-state linearization has one zero eigenvalue at equality, so do not claim exponential decay there from linearization alone.

**Global maintenance above threshold.** Assume (S2), set

\[
u=x/x_*,\quad v=y/y_*,\quad
R=abf/\mu,\quad C=cx_*=R-\delta>0.
\]

Then

\[
\dot u=R(v-u)-Cu(u-1),\qquad \dot v=\mu(u-v).
\]

For \(u,v>0\), use

\[
W(u,v)=u-1-\log u+{R\over\mu}(v-1-\log v).
\]

It is nonnegative, vanishes only at \((1,1)\), diverges at the boundary and at infinity, and satisfies the exact identity

\[
\boxed{\dot W=-R{(u-v)^2\over uv}-C(u-1)^2.}
\tag{S4}
\]

To check it, differentiate using \(d(s-1-\log s)/ds=1-1/s\). The two coupling terms combine into \(-R(u-v)^2/(uv)\); the density term is \(-C(u-1)^2\). Thus \(\dot W<0\) away from \((1,1)\). A positive trajectory remains in a compact sublevel set, and the derivative is bounded strictly below zero on any closed region in that set separated from the equilibrium. Therefore every positive initial condition converges to \((x_*,y_*)\). This proves asymptotic restoration after finite perturbations that leave both concentrations positive, under the unchanged model conditions.

**Material turnover.** Now mark all material present at time zero. Assume labels do not affect kinetics, newly produced material is unmarked, and losses sample old and new material without label preference. If \(x_o,y_o\) denote marked concentrations, their equations are

\[
\dot x_o=-(\delta+cx)x_o,\qquad
\dot y_o=-\mu y_o.
\tag{S5}
\]

Therefore

\[
0\le x_o(t)\le x_o(0)e^{-\delta t},\qquad
y_o(t)=y_o(0)e^{-\mu t}.
\tag{S6}
\]

The original marked material tends to zero while the maintained concentrations approach positive values. At equilibrium, \(x_o(t)=x_o(0)e^{-Rt}\). For any requested \(0<\varepsilon<1\), waiting at least \(\log(1/\varepsilon)/\min(\delta,\mu)\) reduces each marked concentration to at most \(\varepsilon\) times its initial value. **The continuous model does not make a positive original label exactly zero at a finite time.**

For \(a=b=\delta=\mu=c=1,f=2\), the maintained state is \(x_*=y_*=1\), with original material declining as \(e^{-2t}\) and \(e^{-t}\). Its Jacobian eigenvalues are \(-2\pm\sqrt3\), both negative.

The result establishes persistence of specified organization without persistence of its original material tokens. It does not establish that there are no necessary functional roles: the two production capacities and environmental conditions remain indispensable to this construction. Maintenance alone does not supply sensing, deliberation, or a first-person standpoint, and a stable pattern is not thereby a person. It does not establish human personal identity, a membrane or spatial boundary, consciousness, or metaphysical no-self. Finite-population stochastic extinction is also outside this deterministic concentration model.

The positive result is enough to rule out one inference: an enduring organized unit need not be an unchanging collection of matter. Its continued distinction can be a maintained activity. Both the unit and its dependence are real in this model.

## The observer and controller remain within the account

An observer-controller can be represented by an internal state \(c_t\), observation \(o_t\), and action \(u_t\):

\[
o_t=M(x_t,e_t),\quad u_t=\pi(c_t),\quad
c_{t+1}=H(c_t,o_t),\quad
x_{t+1}=F(x_t,u_t,e_t),\quad
e_{t+1}=E(e_t,x_t,u_t).
\tag{S7}
\]

The combined state evolves under one specified transition rule. The observer's measurements, memories, action capacities, and effects are among the modeled processes. An unexplained controller outside that state is not needed for this model. A genuinely complete physical account would additionally justify that its chosen state and laws suffice; merely writing (S7) cannot establish completeness or metaphysical monism.

The controller can still make a causal difference: with other relevant conditions fixed, different admissible controller states can yield different actions and outcomes. Dependence on prior causes therefore does not by itself erase this model-level causal agency. The model does not settle debates about free will, phenomenal experience, or moral responsibility. If “the whole observes itself” is used, its precise content is only that a subsystem's observation of another subsystem is an event in their common process. It supplies no evidence of a single cosmic subject.

A relevant published proposal treats agency as an organization that regulates its environmental coupling in relation to its own continuation. It explicitly combines dependence with distinct individuality and causal asymmetry. This is an established research position rather than scientific consensus about every sense of self. [Barandiaran, Di Paolo, and Rohde, 2009, sections 3–4](https://xabier.barandiaran.net/wp-content/uploads/2009/07/barandiaran_dipaolo_rohde_-_defining_agency_v_1_0_-_jab_20091.pdf). Review scope: author-hosted primary paper, abstract and sections 3–4 (PDF pages 6–8); the model (S1) is our construction, not their experiment.

## “No us versus others”: what follows, and what needs another premise

A common physical process places effects on others inside the causal account. It does not automatically give everyone the same information, experiences, interests, or authority. A tiny counterexample makes this exact: let a single conserved resource satisfy \(r_A+r_B=1\), with interests \(U_A=r_A\), \(U_B=r_B\). The parties are completely linked by the constraint but prefer opposite reallocations. A common state space does not supply a unique maximand.

An ethical bridge can be stated explicitly:

1. Other affected beings' experiences and agency provide reasons for action, even when those beings fall outside one's current identity boundary. This is a normative commitment, not a conservation law.
2. Shared dependencies reveal how actions reach those beings and which conditions their agency needs. This is an explanatory contribution.
3. Distinct participants have information and reasons that one center cannot simply claim to possess. Their participation, criticism, and refusal can therefore be necessary to a warranted judgment.

Where morally relevant facts are unchanged, changing only an arbitrary “us/them” label should not reverse a judgment **if impartial treatment of such labels is accepted**. This premise does not require equal treatment when morally relevant needs, roles, history, or responsibilities differ. Nor does it forbid justified resistance or protective boundaries.

The sharpest formulation inherited from the user's corpus is **answerability without incorporation**: another's reality enters judgment without being absorbed into one's objective or represented by a supposedly all-inclusive self. The primary ethical danger is not addressed by enlarging “me” until other people's differences disappear.

## Read-only corpus findings and source scope

1. `outputs/next-root-joint-organization.md`, read in full: relatively autonomous parts depend on timescale, exchange strengths, prediction target, and appropriate tests. Its existing proof already separates connectedness from exact independence and existential monism from priority monism. The present construction adds maintenance and replacement; it does not overwrite that work.
2. `outputs/root-of-wisdom-formalization.md`, relevant mathematical and wisdom sections read: the earlier unsaturated reciprocal-production model supplies a growth threshold but not stable persistence. Equation (S1) adds an explicit saturation mechanism and proves actual restoration to a positive state. The retained ethics already distinguishes functional persistence from goodness.
3. `/Users/ren/theories/sources/06-zhishan/writing-program/causal-chain/v5/independent-en.md`, lines 81–103 read: explicitly develops “answerability without incorporation,” denying that interdependence entitles one center to represent an undifferentiated whole. This is a historical source for the phrase, not the newest version of the essay.
4. `/Users/ren/theories/sources/06-zhishan/writing-program/causal-chain/v7/independent-en.md`, lines 77, 81, 89 inspected: preserves distinct personhood, injury, responsibility, refusal, and answerability among distinct centers. This confirms the substantive direction survived revision.
5. `/Users/ren/theories/sources/06-zhishan/writing-program/causal-chain/v8/independent-en.md`, line 75 inspected: states that compassion, Ubuntu, interdependence, and nondual traditions differ in metaphysics and practice, and that stable systems can still wrong concrete beings. This is current corpus evidence against claiming all traditions literally teach the same ontology. It is the user's research synthesis, not independent historical verification of those traditions.
6. `/Users/ren/theories/sources/06-zhishan/writing-program/context/meta-attractor-foundational-context.md`, lines 490–530 read: mutual generation cannot require participants to become expendable, voiceless, unable to refuse, or incapable of maintaining their own agency; common provision can need meaningful boundaries and restrictions.
7. `/Users/ren/theories/drafts/2026-09-04-one-work/ESSAY.md`, lines 45–80 read; `/Users/ren/theories/_process/reading-notes/out-hb-02.md`, lines 482–510 read: recover the user's older relational-self formulation, including the self as part of the whole recognizing a self. The essay's stronger suggestion that care is “the same act” from either end of a relation is interpretive, not a theorem. The counterexample above guards against reading it as identity of interests.
8. `/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v7.3/src/core/30_s3.md`, relational-self passages inspected: presents the person as a center formed by body, care, language, institutions, and choices; insists that oneness does not mean sameness, and that suppressing difference repeats totalization. `/v7.3/src/core/a0_s10.md`, relevant passages inspected: common projects retain internal allocation contests; pooling interests and abolishing conflict are different mechanisms. No experiments from those projects were rerun here.

## Verification and status

`check_self_maintenance.py` uses exact rational arithmetic over 972 parameter tuples. It finds 288 above-threshold positive equilibria, 531 below-threshold tuples, and 153 at equality. It verifies equilibrium residuals, Jacobian signs, and 7,200 point evaluations of the Lyapunov identity, including its unique zero. Results: `self-maintenance-checks.json`, all passed. The general algebraic proof above, rather than the finite checks, establishes the continuous parameter claim.

These results support a positive next root: **real individuality can consist in maintained differentiation within shared conditions, without an independently self-existing controller or enduring original material core.** Its application to particular organisms or persons requires domain-specific evidence. The more universal claim that all reality is one ultimately fundamental process remains a philosophical hypothesis. The strongest next empirical question is which material mechanisms actually produce a boundary, maintain a viewpoint, and regulate exchange under changing conditions.
