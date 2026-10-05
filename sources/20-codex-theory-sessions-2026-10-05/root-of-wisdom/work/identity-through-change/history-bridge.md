# Bridge: future equivalence does not settle a historical question

Prepared 5 October 2026. This appendix connects the reactor example to the earlier theory of response equivalence. It strengthens the investigation by locating a precise information loss; it does not purport to establish numerical identity from reactor dynamics.

## Reactor and admissible histories

Use the supplied reactor state \(z=(a,x)\), with substrate \(a\), autocatalytic population \(x\), and equations

\[
\dot a=D(a_{\rm in}-a)-kax,\qquad
\dot x=kax-Dx.
\]

For \(k a_{\rm in}>D\), the positive equilibrium is

\[
z^*=(a^*,x^*)=\left(D/k,\ a_{\rm in}-D/k\right).
\]

Consider two *open reactor histories* over a specified interval \([-T,0]\):

- \(H_1\): the reactor remains at \(z^*\) throughout.
- \(H_2\): the reactor has no \(X\) population for a nonempty earlier interval; an external preparation later refills/reseeds it exactly to \(z^*\), after which it remains at equilibrium through time zero.

An external refill is an additional preparation operation. It is not claimed that the displayed autonomous ODE spontaneously recreates \(X\) after extinction. Indeed \(x=0\) is invariant under that ODE. Exact refill is a stipulated ideal preparation for the counterexample, not a reported laboratory event. An instantaneous reset can be treated as a separate preparation map; if a fully resolved preparation process is wanted, its environmental state and dynamics must be added.

Define the narrowly physical historical predicate

\[
C(H)=\mathbf 1\{x_H(s)>0\text{ for every }s\in[-T,0]\}.
\]

Then \(C(H_1)=1\) and \(C(H_2)=0\), while \(z_{H_1}(0)=z_{H_2}(0)=z^*\). The predicate refers to uninterrupted presence in this reactor during this interval. It does not say that the species disappeared from the world, that an externally stored seed has no wider lineage, or that this property is a sufficient definition of organismal or personal identity.

## Exact nonfactorization result

Let \(\mathcal H\) be the allowed histories and let \(\pi(H)=z_H(0)\) be their current-state projection. A historical property \(C\) can be represented as a function of current state, \(C=c\circ\pi\), **if and only if it is constant on every fiber of \(\pi\)**.

Necessity follows because \(\pi(H)=\pi(H')\) implies \(c(\pi(H))=c(\pi(H'))\). For sufficiency, define \(c(z)\) to be the common value of \(C\) on histories projecting to \(z\); constancy makes that definition unambiguous on the image of \(\pi\).

The two histories above violate fiber constancy. Therefore there is no function of the current unlabeled reactor state that answers the stated uninterrupted-presence question on all allowed histories.

This is the same mathematical issue as a proposed observable failing to descend to a quotient. It reveals why an otherwise excellent reduction can be inadequate for a newly posed question.

## Why future interventions do not necessarily recover the loss

Suppose that after time zero the allowed controlled dynamics are well posed and depend only on the current reactor state and the chosen input:

\[
\dot z=F(z,u(t)),\qquad y=G(z,u(t)).
\]

For every admissible common future input sequence, uniqueness gives the same future state and observation trajectory from \(z^*\). Therefore \(H_1\) and \(H_2\) have the same entire future response profile within this specified observation and intervention class. Any function of that profile gives the same answer for both histories and consequently cannot equal \(C\).

The claim also covers a deterministic adaptive experiment whose later choices use only the shared available observations: identical observation histories lead to identical next inputs. For a Markov stochastic version with identical current state and controls, the corresponding statement concerns identical future observation distributions, rather than identical independently realized sample paths.

The exclusions matter. A surviving tracer, a controller's log, an external witness, or a changed vessel surface can supply history. If an allowed intervention reads such a record, the two cases are no longer equivalent under that enlarged observation class. Conversely, a new label attached only after time zero cannot by itself reveal which unrecorded past occurred.

Nor does the argument claim that different histories of a completely closed deterministic universe converge to one complete physical state. The two reactor preparations differ in their environments and inputs. The reactor projection omits those records and mechanisms. The displayed sufficient state is sufficient for its stipulated future dynamics, not an assertion that its two concentrations encode every physical fact.

## What this adds to the earlier foundation

Earlier response equivalence correctly groups descriptions that agree on every *specified future consequence*. This example shows that an equivalence suitable for prediction may discard information needed for a historical or genealogical question. Restoring the information might require keeping a record or broadening the boundary, rather than changing the reactor's predictive equations.

The precise conclusion is:

> A description can be sufficient for every allowed future response and still be insufficient for a fact about how the present came about.

Prefer **“the sufficiency of a description depends on the question”** to “truth is question-relative.” Once the interval, physical predicate, and history are fixed, the uninterrupted-presence claim has a definite truth value in this example. Changing the question changes the information required; it does not make either history a matter of preference.

For this particular predicate, a recorded bit could suffice: initialize it to one at the interval's start and set it permanently to zero if extinction occurs. That bit records a selected fact, rather than recovering forgotten history from the present. More demanding genealogical questions may require substantially richer records.

## Link to splitting, fusion, and identity

The reactor example separates sameness of response from sameness of history. The next distinction is between a history of descent and numerical identity. Descent can branch: one occurrence can contribute to two later occurrences. Numerical identity cannot identify one thing with both of two distinct things, because \(A=B\) and \(A=C\) imply \(B=C\).

Likewise two distinct earlier occurrences may both contribute to a fused later occurrence without both being numerically identical to it. A faithful account can retain a graph of continuation and contribution, while separately specifying any rule used to count continuing individuals. It should not force that graph into a one-to-one identity relation by concealing branching or fusion.

Thus the example does not solve identity by stipulation. It proves that any proposed identity criterion sensitive to this kind of uninterrupted history cannot be determined from the supplied current-state or future-response description alone. Whether uninterrupted history is necessary, sufficient, or neither for a particular kind of entity remains the next substantive question.
