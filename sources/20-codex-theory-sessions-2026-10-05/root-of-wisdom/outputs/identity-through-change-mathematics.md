# Mathematical notes on replacement and continuity

Companion to [What continues when the material changes](identity-through-change.md), prepared 5 October 2026. The two parts establish different results: a specified mechanism maintains a population while original material leaves, and a present-state description can omit a definite historical fact. Neither result is a definition of personal or numerical identity.

The reaction model is a constructed illustration of established kinetics, not a newly discovered physical law. Its proof is self-contained. Primary experimental comparisons and their limits are in the main report. The [evidence record](identity-through-change-evidence.json) contains the exact check program and results.

## Model and what it assumes

Use a well-mixed vessel of fixed volume. Fresh precursor A enters at concentration a_in>0. Every molecule has common outflow rate D>0. An existing X catalyzes conversion of one A into one additional X at mass-action coefficient k>0:

    A + X -> X + X.

Here the pre-existing catalyst molecule survives the conversion event. The newly converted precursor is a new X molecule. A and X are idealized equal-unit carriers. This is a deliberately supplied reaction scheme and kinetic law, not an assertion about all actual autocatalytic chemistry. We assume no X in the inflow, no spontaneous A->X conversion, no return flow, and no inherited *material* label in a newly formed X. The vessel, mixing, feed, and rate coefficients are externally maintained conditions; the reaction does not manufacture those conditions.

Writing a(t),x(t) for nonnegative concentrations gives

\[
\dot a=D(a_{\mathrm{in}}-a)-kax,\qquad
\dot x=kax-Dx.
\tag{1}
\]

Units are concentration for a,x,a_in, inverse time for D, and inverse concentration-time for k. Production flux J=kax and outflow loss Dx have concentration/time units.

The nonnegative region is forward invariant: at a=0, its derivative is D a_in>0, while x=0 is an invariant boundary. Adding the equations gives exact material balance:

\[
s(t):=a(t)+x(t)
=a_{\mathrm{in}}+[s(0)-a_{\mathrm{in}}]e^{-Dt}.
\tag{2}
\]

Both concentrations remain bounded. Existence and uniqueness therefore extend for all finite positive times.

## Main theorem: a supplied mechanism sustains concentration

Let r=k a_in-D. There are two possible equilibria in the nonnegative region:

\[
(a,x)=(a_{\mathrm{in}},0),
\]

and, precisely when r>0,

\[
\boxed{a_*=D/k,\qquad x_*=a_{\mathrm{in}}-D/k>0.}
\tag{3}
\]

If x(0)>0, every trajectory tends to the positive equilibrium when r>0; otherwise x tends to zero and a tends to a_in. If x(0)=0, x remains zero even when r>0. The positive attractor is therefore an attractor for seeded initial states, not for the entire nonnegative region.

On the particularly simple preparation s(0)=a_in, equation (2) fixes a+x=a_in at every time and equation (1) becomes exactly

\[
\boxed{\dot x=rx-kx^2.}
\tag{4}
\]

For \(x_0>0\) and \(r\ne0\),

\[
x(t)=\frac{x_0e^{rt}}
{1+(kx_0/r)(e^{rt}-1)}.
\tag{5}
\]

For r=0, x(t)=x0/(1+k x0 t). Thus the equality case is asymptotic washout at rate 1/(kt), not a positive maintained state. At the positive equilibrium, production exactly replaces loss:

\[
\boxed{J_*=ka_*x_*=Dx_*>0.}
\tag{6}
\]

The equilibrium expresses continual activity. It is not a static collection of the same molecules. The Jacobian eigenvalues at this equilibrium are -D and -r, both negative. At washout they are -D and r.

### Proof beyond the special preparation

Let c=s(0)-a_in, so equation (1) gives

\[
\dot x=[r+kc e^{-Dt}]x-kx^2.
\]

For x0>0 set

\[
Q(t)=rt+\frac{kc}{D}(1-e^{-Dt}).
\]

Solving the linear equation for 1/x gives

\[
x(t)=\frac{e^{Q(t)}}{x_0^{-1}+k\int_0^t e^{Q(v)}\,dv}.
\tag{7}
\]

For r>0, numerator and integral grow exponentially; taking their ratio using differentiation gives x->r/k. For r<0 the numerator tends to zero while the denominator stays positive, so x->0. For r=0, e^Q tends to a strictly positive constant and the integral grows like that constant times t, giving x~1/(kt). Equation (2) then fixes the limit of a. This proves the theorem for every nonnegative a(0) and positive x(0), not just points on the chosen invariant line.

## Material continuity and genealogical continuity are different observables

At time zero mark every X molecule then present. The mark identifies the original molecular cohort; it is not copied onto newly converted precursor. Marked X remains active and has the same dilution probability as unmarked X. The original marked concentration ell then satisfies

\[
\boxed{\dot\ell=-D\ell,\qquad \ell(t)=\ell(0)e^{-Dt}.}
\tag{8}
\]

Reaction preserves the old catalyst, while outflow removes it. New X is unmarked. At a maintained equilibrium with ell(0)=x*, the fraction of original X molecules is exactly

\[
\boxed{\ell(t)/x_*=e^{-Dt}.}
\tag{9}
\]

The abundance and production rate remain constant while the original cohort dwindles. In the continuous description that cohort is never exactly zero at a finite time. For example, at t=log(100)/D, it is one percent of its initial amount. This is an exact label prediction in the model, not an empirical measurement.

Genealogy needs a different label. If every new X inherits the identity of its catalyst's ancestry class, and x1,x2 are two otherwise identical lineages, then

\[
\dot x_i=(ka-D)x_i,\qquad
\frac{d}{dt}\frac{x_i}{x_1+x_2}=0
\tag{10}
\]

between external introductions. A genealogical class includes newly made molecules; an original-material cohort does not. It is therefore consistent for no original molecule to remain in a finite realization while all current molecules are descendants of the original seed. Removing material identity does not by itself remove causal or genealogical continuity.

## What the mechanism predicts under interventions

1. **Partial depletion.** For parameters r>0, reducing x but leaving any positive seed, with a still nonnegative, leads back to the same positive equilibrium. Equation (7) establishes recovery even when a+x is disturbed. Recovery time diverges logarithmically as a seed approaches zero in the logistic preparation; recovery is not instantaneous or equally easy at every seed size.
2. **Complete removal.** Setting x=0 leaves the process on an invariant boundary. Feeding A cannot re-create X in this model. A new X seed is required. This is a consequence of the specified absence of spontaneous nucleation, not a universal statement about chemistry.
3. **Reaction inhibition.** Setting k=0 gives x(t)=x(T)e^{-D(t-T)} after intervention time T. A constant concentration cannot be maintained merely by keeping the original vessel and feed.
4. **Feed removal.** Setting a_in=0 while continuing fresh solvent inflow and outflow gives a+x=[a(T)+x(T)]e^{-D(t-T)}. Therefore x eventually falls below every fixed positive detection threshold. Finite-time exact extinction does not follow from this deterministic ODE.
5. **Excessive dilution.** Changing conditions to k a_in<=D eliminates the maintained positive equilibrium. Equality gives algebraic decay; strict inequality gives asymptotic washout.

Stopping both inflow and outflow is a different intervention from replacing the feed with blank solvent. If D=0 after time T, total s=a+x stays fixed and the closed-vessel equation is x'=k(s-x)x. With any seed x(T)>0 it tends to x=s, a=0: production stops because precursor is exhausted, while catalyst remains. At the state a=0, x>0, D=0 there is no reaction flux but the capacity to resume after precursor addition remains. No catalyst degradation process was supplied, so indefinite storage in this ideal closed model is not an empirical prediction about actual molecules. This counterexample matters conceptually: continuity of a carrier or capacity does not require uninterrupted current activity. Likewise, stopping activity is not automatically destruction. The main positive-attractor theorem assumes D>0; this deliberate intervention changes that regime.

These interventions distinguish an explanatory mechanism from a descriptive resemblance: continuing appearance depends on particular production and loss relationships. They do not establish which historical continuation should count as numerical identity. A reset and external reseeding can reproduce the same later concentrations while having a different ancestry; the concentration variables deliberately do not record that history.

## Finite-volume stochastic limitation

A finite molecular version exposes why a positive deterministic attractor must not be called guaranteed indefinite survival. Let volume V be finite. Counts N_A,N_X have these transition rates:

| Event | Count change | Rate |
|---|---|---|
| Precursor arrival | (N_A+1,N_X) | D V a_in |
| Precursor outflow | (N_A-1,N_X) | D N_A |
| Catalyst outflow | (N_A,N_X-1) | D N_X |
| Catalytic conversion | (N_A-1,N_X+1) | k N_A N_X/V |

The total N=N_A+N_X is exactly an immigration-death process: upward rate lambda=D V a_in and downward rate D N; the reaction does not change N. Its normalized stationary probabilities are

\[
\pi_n=e^{-V a_{\mathrm{in}}}\frac{(V a_{\mathrm{in}})^n}{n!},
\]

as follows directly from detailed balance pi_n lambda=pi_(n+1) D(n+1). The nonexplosive irreducible birth-death chain is positive recurrent, so it visits N=0 almost surely from every finite starting state. Consequently X reaches zero almost surely. Once X is zero it remains absent, although precursor later returns. No estimate of the time to extinction is claimed here; it may be enormously long for large volume. The ODE describes a different, continuous regime and its long-time limit cannot be interchanged casually with the finite-volume stochastic limit.

One can prove the hitting claim without relying on the stationary argument. Let q_n be the probability, starting with total n, of ever reaching zero. The first-jump equation gives lambda(q_(n+1)-q_n)=Dn(q_n-q_(n-1)) for n>=1, with q_0=1. Differences therefore satisfy q_n-q_(n-1)=(q_1-1)(D/lambda)^(n-1)(n-1)!. Unless q_1=1, summing these differences eventually violates 0<=q_n<=1. Thus every q_n=1. Nonexplosion follows because total arrivals during a finite interval are bounded by a finite Poisson count, deaths only lower the total, and reaction rates are bounded along each such finite-interval count bound.

This exact argument is specific to this model. It does not imply every finite maintained system must go extinct by the same mechanism or on a useful observational time scale.

## What this does and does not establish about identity

The result establishes maintained concentration and activity despite constituent turnover; seed-dependent recovery; distinguishable material and genealogical labels; and loss conditions. It supplies an example of how persistence can occur *through replacement*. A philosophical criterion of numerical identity is not an extra eigenvalue hiding in the equations.

The model does not explain formation of its containing boundary, the initial catalyst, the reaction law, mixing, energy source, or the apparatus maintaining the feed. It does not establish consciousness, moral standing, monism, or an ultimate metaphysical priority of process over substance. Its positive lesson remains precise: a continuing production process can account for a stable observable that cannot be explained by retaining the same initial constituents.


## Present responses and historical facts

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

Let \(\mathcal H\) be the allowed histories and let \(\pi(H)=z_H(0)\) be their current-state projection. A historical property \(C\) can be represented as a function of current state, \(C=c\circ\pi\), **if and only if it is constant on every fiber of \(\pi\)**. A fiber is the set of histories with the same present state.

Necessity follows because \(\pi(H)=\pi(H')\) implies \(c(\pi(H))=c(\pi(H'))\). For sufficiency, define \(c(z)\) to be the common value of \(C\) on histories projecting to \(z\); constancy makes that definition unambiguous on the image of \(\pi\).

The two histories above violate fiber constancy. Therefore there is no function of the current unlabeled reactor state that answers the stated uninterrupted-presence question on all allowed histories.

The historical property cannot be represented using only the reduced description. This reveals why an otherwise excellent reduction can be inadequate for a newly posed question.

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

**The sufficiency of a description depends on the question. The historical fact itself remains definite.** Once the interval, physical predicate, and history are fixed, the uninterrupted-presence claim has a definite truth value in this example. Changing the question changes the information required; it does not make either history a matter of preference.

For this particular predicate, a recorded bit could suffice: initialize it to \(\mathbf 1\{x(-T)>0\}\) and set it permanently to zero whenever the population is absent during the interval. This is an ideal continuous record of the stated predicate, not a claim that intermittent measurements can detect every absence. That bit records a selected fact, rather than recovering forgotten history from the present. More demanding genealogical questions may require substantially richer records.

## Link to splitting, fusion, and identity

The reactor example separates sameness of response from sameness of history. The next distinction is between a history of descent and numerical identity. Descent can branch: one occurrence can contribute to two later occurrences. Numerical identity cannot identify one thing with both of two distinct things, because \(A=B\) and \(A=C\) imply \(B=C\).

Likewise two distinct earlier occurrences may both contribute to a fused later occurrence without both being numerically identical to it. A faithful account can retain a graph of continuation and contribution, while separately specifying any rule used to count continuing individuals. It should not force that graph into a one-to-one identity relation by concealing branching or fusion.

Thus the example does not solve identity by stipulation. It proves that any proposed identity criterion sensitive to this kind of uninterrupted history cannot be determined from the supplied current-state or future-response description alone. Whether uninterrupted history is necessary, sufficient, or neither for a particular kind of entity remains the next substantive question.

## Verification

Exact rational checks passed for 27 positive-parameter regimes: 10 above the sustaining threshold, 7 at it, and 10 below it. Checks also covered 243 material-balance states, 240 noncritical and 84 critical closed-solution derivative identities, 729 original-cohort identities, 729 ancestry-fraction identities, 121 finite-molecule projection states, and 31 detailed-balance pairs. The global convergence, extinction, and history claims rest on their general proofs, rather than extrapolation from these finite checks. No new physical experiment or stochastic simulation was run.
