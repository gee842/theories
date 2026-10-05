# A maintained concentration with changing material

Constructed mathematical example, 5 October 2026. This is a further clarification of the maintenance result already present in `outputs/nonseparation-and-selfhood.md`, not a claim to have discovered turnover or autocatalysis. The new contribution is explicit material balance, separation of original-material and inherited-lineage labels, and precise recovery and cessation conditions. It does not settle numerical or personal identity.

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

For x0>0 and r!=0,

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

## Verification and literature scope

`check_mechanism.py` uses exact rational arithmetic. It checks 27 parameter sets (10 active, 7 critical, 10 below threshold), the actual two-dimensional Jacobian, 243 mass-balance states, 240 closed-form logistic derivatives, 84 critical derivatives, 729 original-cohort ratio identities, 729 lineage-ratio identities, 121 stochastic projection states, and 31 detailed-balance pairs. All assertions passed. These checks supplement the displayed analytic proofs; they neither establish empirical adequacy nor replace proof over all parameter values. No physical experiment or stochastic simulation was run.

The chemostat is an established experimental and theoretical setting. The primary bibliographic record for Novick and Szilard's *Description of the Chemostat* (1950) was consulted at https://pubmed.ncbi.nlm.nih.gov/14787503/; the original article text was not reviewed and no result of that experiment is used as evidence for this particular ideal reaction.

The abstract of Andersen et al., *Defining Autocatalysis in Chemical Reaction Networks* (2021), https://arxiv.org/abs/2107.03086, explicitly distinguishes several notions of autocatalysis. Only its abstract was read, and it supplies contextual attribution rather than this model's proof. The abstract of Pal (2004), https://arxiv.org/abs/cond-mat/0404582, was also inspected; its reservoir and reaction model differ from ours, so its conclusions are not substituted for the explicit finite-volume argument above. The root synthesis's literature agent supplied a more relevant network-maintenance reference, Piedrafita et al. (2010), https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000872, which that agent reviewed. None is presented as a new empirical test performed in this session.
