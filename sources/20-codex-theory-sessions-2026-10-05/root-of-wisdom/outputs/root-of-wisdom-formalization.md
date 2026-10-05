# How interactions generate laws and consequential distinctions

Revised for Ren, 5 October 2026. The target is a strong explanatory foundation: a small set of principles that generates consequences, identifies indispensable distinctions, and can be corrected by the world. It does not require proving that no deeper formulation could ever exist. The earlier invariant account is preserved in [version two](root-of-wisdom-formalization-v2.md).

**The substantive advance is that independently warranted constraints can select a law, while intervention responses can force distinctions that were missing from our model.** The earlier invariance equation then checks whether a description preserves those consequences. It is part of the foundation, rather than its entire explanatory content.

## The stronger candidate root

> Actual interactions constrain what can happen. Their organization gives rise to effective laws and determines which differences affect consequences. Activity can then maintain, damage, or reorganize the conditions of subsequent activity.

For understanding, this becomes a generative discipline: identify the mechanisms and constraints, derive the responses they permit, and retain the distinctions those responses require. For wisdom, include how our participation changes the lives, interests, and capacities of affected beings.

This proposal contains more than an injunction to notice connections. A substantive account must specify which interaction exists, what it changes, its magnitude and timing, what sustains it, and which response would contradict the account. Constraints should be stated independently of the result they are invoked to explain. Their role is to rule out possible dynamics and generate predictions.

An effective law describes a process at a stated scale using enough state or memory for its intended predictions. It can remain reliable while many microscopic details vary. Its applicability can also change when a coupling, preparation, resource condition, or time scale changes. Discovering a previously hidden dependency is distinct from that dependency first coming into existence.

## A substantive law can be selected rather than supplied

Consider a ring of \(N\ge5\) sites carrying nonnegative amounts \(p_i\). Assume linear autonomous evolution \(\dot p=Gp\), nearest-neighbor interactions, identical rules at each site, reflection symmetry, conservation of total amount, and preservation of nonnegativity.

These conditions force

\[
\boxed{\dot p_i=\kappa(p_{i-1}-2p_i+p_{i+1}),\qquad\kappa\ge0.}
\tag{1}
\]

**Derivation.** Locality and translation symmetry reduce the unknown law to \(\dot p_i=a p_{i-1}+b p_i+c p_{i+1}\). Reflection requires \(a=c\); conservation requires \(a+b+c=0\). Positivity requires the neighboring coefficients to be nonnegative: starting with a unit amount at a neighbor cannot make an initially empty site immediately negative. Thus \(a=c=\kappa\), \(b=-2\kappa\), and \(\kappa\ge0\). Conversely, this generator preserves nonnegative amounts and total mass. For example, writing it as \(\kappa(S+S^{-1}-2I)\), the exponential has nonnegative entries and unit column sums. □

The law's form is determined; its rate remains to be measured. Here \(\kappa\) has units of inverse time. A continuum diffusivity has different units and would require a specified spatial scaling and limiting argument.

The theorem yields further consequences without fitting another law. With conserved mean \(\bar p\),

\[
\frac{d}{dt}\frac12\sum_i(p_i-\bar p)^2
=-\kappa\sum_i(p_{i+1}-p_i)^2.
\tag{2}
\]

For \(\kappa>0\), every nonconstant mode decays and the distribution tends toward uniformity. This is a prediction of the specified mechanism, not a premise that all processes equalize.

Each physical restriction matters. Without reflection, directed transport is allowed. Without nearest-neighbor locality, longer jumps are allowed. Without conservation, sources and losses are allowed. Without translation symmetry, location-dependent conductances are allowed. Negative diffusion satisfies the remaining equalities but violates positivity. Nonlinear or history-dependent evolution belongs to a different starting class.

Exact rational verification began with all 25 entries of an arbitrary five-site generator. The constraints had rank 24 and left one parameter. Removing individual constraints admitted explicit competing generators. This checks a real selection of possible laws, beyond making an arbitrary law consistent under renaming.

## Contact with physical reality determines the remaining content

Einstein's Brownian-motion derivation provides a physical example. For dilute spheres in an isothermal liquid, with continuum Stokes drag, negligible drift, and unconfined diffusion on times long enough to neglect inertial memory, it relates diffusion to independently meaningful conditions:

\[
D=\frac{k_B T}{6\pi\eta r},\qquad
\langle(\Delta x)^2\rangle=2Dt.
\tag{3}
\]

Temperature, viscosity, and particle radius constrain the predicted displacement. Einstein explicitly separates observation intervals over which successive increments can be treated as independent. These relations therefore make conditional predictions rather than asserting that every irregular motion is diffusive. [Einstein, 1905, sections 3–5](https://personal.lse.ac.uk/ROBERT49/teaching/ph232/pdf/einstein-brownianmotion.pdf).

Measurements by Li and colleagues later resolved short-time ballistic motion of optically trapped beads in air. Their analysis distinguishes the momentum-relaxation time from the regime where the usual free-particle diffusion relation applies; the trap adds its own longer-time effects. Velocity matters at a scale where a simpler diffusive description omits it. This is an empirical example of why a change in temporal resolution can require a richer description. [Li et al., 2010](https://users.physics.ox.ac.uk/~Foot/Phynance/Raizen1BrownianM.pdf).

These published results illustrate the explanatory route. No new Brownian-motion experiment was performed in this inquiry. The finite ring theorem is our independently checked illustration of law selection, not a derivation of all microscopic fluid dynamics.

## Responses can force a missing distinction

The earlier quotient theorem began with a supplied state space and determined what could be omitted. We can sometimes reverse that direction: observed responses can rule out a model whose state is too small.

For a discrete linear time-invariant process,

\[
z_{t+1}=Az_t+Bu_t,\qquad y_t=Cz_t,
\]

prepare \(z_0=0\), apply \(u_0=1\), and then set the input to zero. The response coefficients are \(h_k=CA^kB=y_{k+1}\). The derivation below assumes exact, noiseless coefficients. Measured noisy responses require uncertainty bounds excluding a zero determinant before they establish the claimed dimension lower bound. The preparation, timing, and input and output interpretation are part of the experiment.

For an illustrative mechanism,

\[
A=\begin{pmatrix}a&\gamma\\0&b\end{pmatrix},\quad
B=\begin{pmatrix}0\\1\end{pmatrix},\quad
C=\begin{pmatrix}1&0\end{pmatrix},
\]

the input changes an unobserved coordinate, whose influence reaches the observed coordinate through coupling \(\gamma\). Direct calculation gives

\[
h_0=0,\quad h_1=\gamma,\quad
h_2=\gamma(a+b),\quad
h_3=\gamma(a^2+ab+b^2).
\]

Consequently,

\[
\boxed{\det\begin{pmatrix}h_0&h_1\\h_1&h_2\end{pmatrix}=-\gamma^2.}
\tag{4}
\]

For nonzero coupling, those responses require at least two internal state dimensions within the stated class. A one-state linear realization would have \(h_1=\alpha h_0\), which cannot produce zero followed by a nonzero response. An unexplained input delay would itself contain memory and cannot be exempted from the comparison.

Thus a physical response can demand a distinction that the observer did not begin by postulating. It does not uniquely name a hidden physical substance: alternative internal coordinates can describe the same response.

Four response terms also recover a candidate law. Put

\[
s=\frac{h_2}{h_1},\qquad p=s^2-\frac{h_3}{h_1}.
\]

For the displayed mechanism, \(s=a+b\), \(p=ab\), and its characteristic polynomial gives

\[
\boxed{h_{k+2}=s h_{k+1}-p h_k.}
\tag{5}
\]

This connects the discovery of necessary memory to predictions about subsequent responses. For example, \(a=1/2,b=1/4,\gamma=1/8\) gives \(s=3/4,p=1/8\). Exact rational checks across 245 constructed systems confirmed the determinant and response calculations. In all 196 nonzero-coupling cases, coefficients fitted from four terms reproduced 28 further terms computed from the full state dynamics. The other 49 cases were zero-coupling controls.

There is a precise evidential boundary. A nonzero finite response determinant establishes a dimension lower bound. A finite sequence cannot rule out an additional mode that first appears later. The displayed two-state mechanism supplies the exact upper bound and all-time recurrence; an empirical application requires prospective tests and justified model-class assumptions. The broader method belongs to established realization theory, documented in [Ho and Kalman's original work](https://ntrs.nasa.gov/citations/19670049337).

## A hidden interaction can become memory

A second derivation makes the source of missing distinctions concrete. Suppose

\[
\dot x=-kx-gy+u(t),\qquad
\dot y=-gx-\lambda y,\qquad\lambda>0.
\]

Eliminating the hidden coordinate \(y\) gives the exact visible equation

\[
\dot x(t)=-kx(t)+u(t)
+g^2\int_0^t e^{-\lambda(t-s)}x(s)\,ds
-g e^{-\lambda t}y(0).
\tag{6}
\]

The hidden coordinate leaves both a history term and a dependence on its initial condition. Two systems with the same current \(x\) but different \(y\) have derivative difference \(-g\Delta y\). If \(g=0\), the hidden coordinate is irrelevant to this response under the same input. If \(g\ne0\), erasing it can lose information needed to predict the response.

This supplies a concrete way to search for omitted possibilities: change the preparation or intervention timing and check whether the response depends on a history the current model treats as irrelevant. The required correction may be a new state variable, retained memory, a changed boundary, or a narrower domain of validity. It need not be another layer of introspection.

A fast hidden coordinate can sometimes be approximated after its transient by \(y\approx-gx/\lambda\). The resulting simpler law has coefficient \(k-g^2/\lambda\). The saved audit derives an explicit remainder bound; “fast” alone is not an exact deletion rule. This explains how a distinction can be negligible for one question and indispensable for another without making its physical existence depend on our vocabulary.

## Activity changes the conditions of future activity

The other sessions add the reflexive part of the proposed foundation. An inquiry can produce a record, a repair can restore a capacity, and a rule can change who is heard or which intervention is available. Those results alter what can happen next.

A useful modeling form separates ordinary state \(x\) from produced structures or capacities \(\theta\):

\[
x_{t+1}=F_{\theta_t}(x_t,u_t,\xi_t),\qquad
\theta_{t+1}=G(\theta_t,x_t,u_t,\xi_t).
\tag{7}
\]

The substantive content lies in independently supported restrictions on \(F\) and \(G\). An arbitrary pair of functions would merely rename the problem. A structure may be a material arrangement, a retained skill, an enacted permission, or an installed controller; each needs its own causal mechanism.

For example, two capacities that produce one another while decaying can be modeled over a suitable interval by

\[
\dot x=afy-\delta x,\qquad
\dot y=bx-\mu y,
\]

with positive rates and a held resource level \(f\ge0\). Its characteristic polynomial is \(r^2+(\delta+\mu)r+\delta\mu-abf\). A growing mode exists exactly when

\[
\boxed{abf>\delta\mu.}
\tag{8}
\]

The same dependency cycle can therefore decay, maintain a neutral mode at equality, or amplify according to quantitative support and loss. The inequality predicts how changing a resource or a loss rate shifts the regime. Resource depletion and saturation require further mechanisms before predicting long-run persistence. This is a constructed conditional law, not a claim that every feedback loop sustains itself.

The latest full-picture work supplies an implemented counterpart at a different level: paid inquiry, evaluator revision, execution, maintenance, training, and succession share one actual process and resource account. The scientific-inquiry work joins service outcomes, complaints, mandate revision, fresh testing, and upkeep. Its relevance is that a change in concern or evaluation has consequences only through actual channels and execution. The structural-closure work shows that a formerly decorative feature becomes causally relevant when a permission mechanism begins to depend on it. These source results were reviewed; their full runs were not repeated here.

## How the world selects among competing laws

For a finite class of \(n\) deterministic candidate mechanisms, suppose the actual mechanism is included. Supply a finite experiment menu and its candidate response predictions, with reliable observations, stable response laws, feasible preparation or reset conditions, and enough means for the required sequence. If two surviving candidates predict different responses to an experiment on that menu, the experiment eliminates at least one while retaining the actual candidate. Repeating identifies its menu-relative equivalence class in at most \(n-1\) experiments. Without an effective way to find separating tests and establish equivalence, the analogous bound is an existence statement rather than a guaranteed terminating procedure.

This elementary result has useful content: the result of an intervention supplies a constraint that reasoning alone cannot choose. It also identifies why some laws remain unresolved: they may make the same predictions through the available interface. No such finite guarantee follows for unrestricted candidates or noisy observations without further assumptions.

The stronger research practice is therefore to specify physical restrictions before seeing the target outcome, measure parameters through an independent route where possible, and derive responses to interventions not used to choose the law. A disagreement must be allowed to challenge the law, its regime, the preparation, or the observation channel. Continually redefining the constraints to fit every result would remove the explanatory achievement.

## What this means for the root of wisdom

This work strengthens the proposed root in three connected ways. Laws can be derived from concrete constraints. Important distinctions can be demanded by responses rather than handed to the model. Activity can change the conditions under which future understanding and action occur.

Some stakes arise from the organization of the affected system: a loss can disable its capacity to sense, maintain itself, or respond regardless of an observer's score. Other stakes concern experienced suffering, agency, obligations, or relationships. These must enter the account through warranted interpretation and ethical reasons. Functional persistence alone does not establish moral worth, and ending a harmful process can be justified.

The integrated candidate is:

> Understand what generates and sustains possible responses; let actual consequences correct the distinctions used to understand them; and take responsibility for how one's participation changes the conditions of life, agency, and further understanding.

This is a proposed foundation for wisdom with substantive mathematical realizations and contact with established physical evidence. It no longer rests only on a tuple of desirable capacities or invariance under description. Its strength comes from deriving outcomes that could have been otherwise, identifying what observations demand, and accounting for the material and social conditions of correction.

## Verification and status

The [evidence record](root-of-wisdom-substantive-evidence.json) preserves the new proofs, exact checks, source provenance, and technical audits. The five-site generator calculation has one remaining nonnegative rate after the stated constraints. The 245-system response check verifies the constructed identification example. These are exact mathematical checks; the cited Brownian-motion experiment is separate published empirical evidence. No new physical, human, or AI-response experiment was run in this revision.

The new conclusions are conditional law selection, constructive discovery of necessary state distinctions, explicit memory from eliminated interactions, and a quantitative threshold for reciprocal support. The unifying interpretation is our synthesis. The next empirical burden is to make it generate independently testable predictions in a consequential target domain. It is no longer necessary to demand an explanation of why precisely this universe exists before recognizing these explanatory gains.
