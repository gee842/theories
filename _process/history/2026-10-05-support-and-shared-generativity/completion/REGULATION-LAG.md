# The finite cost and delay of constructing regulation

5 October 2026. AI-assisted mathematical continuation for Ren. This note proves a construction-lag result for the autonomous gate in [Physical regulation](PHYSICAL-REGULATION.md), extending the [joint capability bridge](JOINT-CAPABILITY-BRIDGE.md). It concerns one declared mesoscopic process, not a universal physical law or a moral conclusion.

The result is precise: from the shared initial preparation, constructing the gate first lowers the probability of retaining a usable reserve. Inhibition only becomes possible at a later event order. This does not decide whether regulation subsequently improves particular joint capabilities.

## 1. Two processes with the same initial preparation

Use unit volume and packet size. The count state is

\[
x=(R,C,Y,D,F,G,GF,YG),
\qquad R+C+Y+D+G+GF+2YG=N=3.
\tag{1}
\]

Here \(GF\) and \(YG\) name complex species; a product such as \(G\,F\) denotes multiplication of free counts. The original plant reactions are

| Event | Propensity |
|---|---:|
| \(R\to C\) | \(R\) |
| \(C\to D\) | \(C\) |
| \(R+Y\to2Y\) | \(R\,Y\) |
| \(Y\to D\) | \(Y\) |
| Capture: \(F\mapsto F+1\) | \(gC\) |
| Free leakage: \(F\mapsto F-1\) | \(F\) |
| \(D+F+C\to R+C\) | \(F\,D\,C\) |
| \(D+F+Y\to R+Y\) | \(\theta F\,D\,Y\) |

The gate adds the following events.

| Event | Propensity |
|---|---:|
| Paid construction: \(R+F\to G\) | \(\kappa R\,F\) |
| Fuel association: \(G+F\to GF\) | \(\alpha G\,F\) |
| Fuel dissociation: \(GF\to G+F\) | \(\rho GF\) |
| Y association: \(G+Y\to YG\) | \(\mu G\,Y\) |
| Y dissociation: \(YG\to G+Y\) | \(\nu YG\) |
| Bound fuel leakage: \(GF\to G\) | \(GF\) |
| Gate wear: \(G\to D\) | \(G\) |
| Gate wear in \(GF\): \(GF\to D+F\) | \(GF\) |
| Gate wear in \(YG\): \(YG\to Y+D\) | \(YG\) |
| Y wear in \(YG\): \(YG\to G+D\) | \(YG\) |
| Reproduction retained while bound: \(R+YG\to Y+YG\) | \(R\,YG\) |

Bound Y cannot catalyze recycling, but it retains reproduction. The selected design therefore gates recycling specifically. Suppressing reproduction as well would be a different physical model.

All parameters are fixed and finite, with \(g,\theta,\kappa,\alpha,\rho,\mu,\nu\ge0\). Strict inequalities below require the indicated products to be positive. The capture coefficient \(g\) has the incident-support interpretation already specified in the stochastic realization; changing it entails changing that support consistently.

Both compared processes start at

\[
x_0=(0,1,1,1,1,0,0,0).
\tag{2}
\]

Write \(\mathbb P_\kappa\) for construction enabled and \(\mathbb P_0\) for the same law with \(\kappa=0\). Other coefficients and incident support are identical. Under \(\mathbb P_0\), all gate species remain absent, so this is exactly the original plant process embedded in the larger state space. Specifying an available construction reaction remains a declared difference between arrangements; the comparison does not derive that reaction capability from more fundamental chemistry.

Define protected plant activity, reserve readiness, and the two event counters by

\[
A(x)=R+C+Y+YG,\qquad
E_h=\{F(h)\ge1,\ A(x(h))\ge1\},
\tag{3}
\]

\[
K_G(h)=\#\{R+F\to G\text{ events by }h\},\qquad
K_{YG}(h)=\#\{G+Y\to YG\text{ events by }h\}.
\tag{4}
\]

The counters record events of the autonomous process; no agent receives a costless readout or issues interventions. Gate material by itself is not counted as protected plant activity. The face \(A=0\) cannot generate new plant activity in this reaction network, so terminal \(A\ge1\) also excludes earlier total loss of plant activity.

Construction has a real cost under the reduced work-equivalent ledger

\[
\mathcal W=F+R+C+Y+G+2GF+2YG:
\qquad \Delta\mathcal W\big|_{R+F\to G}=-1.
\tag{5}
\]

It also converts a plant unit \(R\) into gate material. The fuller ledger and the scope of its physical interpretation are in the companion note.

## 2. Exact construction-lag theorem

Let \(\lambda=1+\theta\). As \(h\downarrow0\),

\[
\mathbb P_\kappa(K_G(h)\ge1)
=\frac{g\lambda\kappa}{2}h^3+O(h^4),
\tag{6}
\]

\[
\mathbb P_\kappa(E_h)-\mathbb P_0(E_h)
=-\frac{g\lambda\kappa}{2}h^3+O(h^4),
\tag{7}
\]

\[
\mathbb P_\kappa(K_{YG}(h)\ge1)
=\frac{g\lambda\kappa\mu}{8}h^4+O(h^5).
\tag{8}
\]

The implicit constants depend on the fixed physical parameters. Equations (6) and (8) also give the leading probabilities of having a gate unit, respectively a YG complex, present at time \(h\): losing the newly formed unit takes at least one additional event.

If \(g\kappa>0\), (7) is strictly negative for all sufficiently small positive \(h\). If also \(\mu>0\), Y inhibition has strictly positive probability, but its first occurrence begins one power of time later than construction. Neither occurrence nor occupancy by itself proves a benefit.

## 3. Leading paths and the reserve penalty

Initially \(R=0\), so construction is unavailable. A recycling event can create \(R\), but consumes the only initial fuel packet. Construction therefore additionally requires capture. The only three-event orders ending in the first construction are

| Order | Product of successive intensities |
|---|---:|
| Capture → recycle → construct | \(g\cdot2\lambda\cdot\kappa=2g\lambda\kappa\) |
| Recycle → capture → construct | \(\lambda\cdot g\cdot\kappa=g\lambda\kappa\) |

The factor two in the first row is the two-packet fuel reserve available at recycling. The two catalytic recycling labels have the same state update, so their intensities sum to \(\lambda\) initially and \(2\lambda\) after capture. Integrating each leading path over its three ordered jump times gives the factor \(h^3/3!\). Their sum is (6).

In either order, just before construction the state is

\[
x_*=(1,1,1,0,1,0,0,0).
\]

Construction changes it to

\[
x_G=(0,1,1,0,0,1,0,0).
\tag{9}
\]

It retains \(A\ge1\) but removes the last free packet, so the readiness indicator changes from one to zero. No gate exists before this third event; no regulatory benefit, binding, gate wear, or bound reproduction can offset it at this order.

For an explicit generator proof of the probability difference, let \(L_0\) be the construction-disabled generator, let \(f(x)=\mathbf 1_{\{F\ge1,A\ge1\}}\), and write

\[
L_\kappa=L_0+B,\qquad
Bv(x)=\kappa RF\,[v(T_Gx)-v(x)],
\tag{10}
\]

where \(T_G\) is the construction update. The operator \(B\) vanishes at \(x_0\) and at every state reachable from it in one jump. All generator differences through order two consequently vanish, and at order three only

\[
(L_\kappa^3-L_0^3)f(x_0)=L_0^2Bf(x_0)
\]

survives. The two positive-rate routes to \(x_*\) have total intensity product \(3g\lambda\), and \(Bf(x_*)=-\kappa\). Thus

\[
(L_\kappa^3-L_0^3)f(x_0)=-3g\lambda\kappa.
\tag{11}
\]

Multiplication by \(h^3/3!\) gives (7). This argument accounts for the change in waiting probabilities when construction is enabled; it does not compare only selected successful paths while ignoring their competing hazards.

From \(x_G\), Y association has intensity \(\mu\). Appending this event to the two leading construction paths gives total four-event intensity product \(3g\lambda\kappa\mu\). Multiplication by \(h^4/4!\) proves (8). The resulting state is \((0,1,0,0,0,0,0,1)\). Bound reproduction is included in the model but cannot contribute at these orders: there is no complex before association, and the leading association state has \(R=0\).

If \(g=0\), construction is impossible from (2), at every horizon. The initial packet can create \(R\) only by being consumed in recycling; without capture, no source subsequently supplies the packet that construction requires. No gate can first appear to release bound fuel. The two laws therefore coincide from this preparation. The strict lag conclusion requires positive capture as well as positive construction rate.

## 4. Why the expansions are valid with an unbounded reserve

Finite material does not make the whole state space finite, because \(F\) is unbounded. Nevertheless every jump increases free \(F\) by at most one, including dissociation and release during gate wear. After \(j\) jumps, \(F\le F_0+j\).

For the declared unit ordinary rates, a conservative bound on total jump intensity is \(a_0+b_0F\), with

\[
a_0=N(4+g+\rho+\nu)+N^2(1+\mu),
\qquad
b_0=1+N(\kappa+\alpha)+N^2\max(1,\theta).
\tag{12}
\]

Material conservation bounds every catalyst and gate count. Fuel-dependent propensities are linear in \(F\). Consequently, if \(N_h^{\rm jump}\) is the number of jumps by \(h\), integration over the ordered jump-time simplex gives, for each fixed integer \(m\ge1\),

\[
\Pr(N_h^{\rm jump}\ge m)
\le \frac{h^m}{m!}
\prod_{j=0}^{m-1}\big[a_0+b_0(F_0+j)\big].
\tag{13}
\]

At each fixed jump depth there are only finitely many reachable states. Their finite rates bound the Taylor remainders from exponential waiting factors. Omitting paths with at least four jumps therefore costs \(O(h^4)\), and omitting paths with at least five costs \(O(h^5)\). This justifies both the path expansions and the generator calculation at the stated orders. The same affine hazard bound also rules out explosion by comparison with a linear pure-birth process.

As an arithmetic check, a separate exact-rational generator expansion included every listed event, including bound reproduction. At \(\theta=4,\kappa=1,\mu=\alpha=4,\rho=\nu=1\), the third derivative of the reserve-probability difference at zero was \(-60\) for \(g=4\) and \(-120\) for \(g=8\). The third derivatives of construction probability were \(60,120\), and the fourth derivatives of Y-association probability were \(240,480\), respectively, agreeing with (6)–(8). This finite derivative check is not a finite-horizon probability certification.

## 5. The precise consequence for capability claims

Consider the same installed delivery/readiness outcomes as the joint capability bridge, with failed activity assigned a bottom outcome. The event \(E_h\) is one upward readiness test. By (7), enabling construction cannot stochastically dominate the original installed outcome law at every positive horizon. For each sufficiently small positive \(h\), one can choose a reliability threshold

\[
\mathbb P_\kappa(E_h)<r\le\mathbb P_0(E_h)
\tag{14}
\]

at which the original arrangement certifies this readiness profile and the constructing arrangement does not. Thus an assertion of capability-region inclusion for every horizon and every reliability is false for this preparation.

This is not a proof of incomparable regions at a prespecified reliability such as \(r=1/2\). Both readiness probabilities approach one as \(h\downarrow0\), so both can pass that particular test. Nor does the result order the full laws in the opposite direction, decide later horizons, compare all physically implementable policies, or prove net harm. Arbitrarily strong but finite capture does not remove the leading lag; the sufficiently short interval may depend on \(g\).

## 6. What a later benefit must additionally establish

The gate has a physically meaningful response: fuel binding can reduce the gate fraction available to bind Y. A binding calculation with fixed ligand activities establishes that local response under its stated clamps. It does not establish the response of the full resource-coupled process, where fuel, Y, and gate abundance all evolve and regulation changes their future trajectories.

For the selected network, the reaction \(R+YG\to Y+YG\) preserves Y's material-conversion channel. A favorable local argument that works by preventing Y from consuming R while bound therefore does **not** apply. Blocking that channel as well could be investigated as a separate design, with its own reaction table and comparisons; no such benefit is imported here.

A later joint improvement must instead be demonstrated with the chosen full generator, starting from the common initial preparation and accounting for construction, leakage, wear, fuel sequestration, and inhibited recycling. It must state the horizon, incident source, reliability, joint assays, and implementable protocol class. A certified increase for particular joint profiles would be a positive result. Inclusion of an entire declared profile region is a stronger claim requiring its own certificate. Neither follows from the binding sign or from the gate's existence alone.

The result supplies a compositional constraint on the proposed direction: building a relation that can regulate shared renewal consumes present enabling conditions before its possible future effects are realized. Whether that cost opens more reliable subsequent possibilities is a physical question about the coupled process, not something already settled by calling the structure regulatory.
