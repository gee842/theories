# Returning captured support to the organization that can use it

5 October 2026. Prospective model and exact comparison, following repository commit `f81afc02d52b02b19a8848201b15a81d19b79e5a`.

**Result and limit.** The present common-pool model does not make a useful architecture increase merely because it supplies useful work. Its copying drift supplies a specific obstruction. A small, explicit change in storage chemistry does permit a stronger positive result: captured support remains bound to the capture carrier, and carrier damage releases that packet for repair. In the resulting N=4 process, blocking a destructive allocation reaction increases the entire retained-scaffold occupation law and completed repair counts. This is an all-path comparison after a declared physical entry, with failures included. The same storage design, however, prevents later fabricator and gate replacement; an exact availability invariant proves this limitation. It is not a theorem of spontaneous architectural prevalence, complete scaffold succession, or general evolutionary improvement.

The changed chemistry is proposed here, not attributed to an observed chemical system. Its packet/work ledger is exact; a thermodynamic realization and calibrated reaction constants remain separate obligations.

## 1. The obstruction in the current common-pool law

The [architecture-formation note](ARCHITECTURE-FORMATION-CRITIQUE.md) has two fabricators A0 and A1, equal basal formation rates sigma, equal wear eta, and copying constants rho0 and rho1. Its gates differ in bound reproduction: zeta0=0 blocks it, whereas zeta1=1 retains it. Fabrication, copying and formation all require the common R,F pool.

For n=A0+A1 at least two and x=A0/n, its exact generator gives

\[
\mathcal Lx=\frac{RF}{n+1}
\left[\sigma(1-2x)+nx(1-x)(\rho_0-\rho_1)\right].
\tag{1}
\]

Consequently, if rho0<rho1, RF>0 and 1/2<=x<1, the drift is negative even when the A0-supported organization has a larger joint-delivery contribution. Increasing a shared source only changes the common RF factor at this state. It does not reverse this sign. Useful delivery and copying advantage are distinct consequences of the supplied reaction law.

There is already a useful *local* retention fact in the unchanged law. At the physical state A_i=C=YG_i=F=1, require the next event to be C wear and examine a return before any A/G/Y constituent wears. The sole packet can produce one R by recycling. Once that happens, C=U=0; reproduction consuming R makes renewed capture impossible. Thus increasing zeta adds killing during this excursion. This extends the [damage-return comparison](RENEWAL-RETURN.md) to the retained N=4 scaffold. However, arbitrary earlier captures in the unchanged model can accumulate additional free packets. Those other histories do not obey this one-packet argument. It does not order the complete unrestricted occupation law.

The missing connection is therefore concrete: useful work must change the producing organization's actual return or loss kernel. Public availability alone does not guarantee that connection.

## 2. A supplied storage reaction can create that connection

Introduce CF, a capture carrier C holding one captured packet. The symbol CF is distinct from the pre-existing gate/fuel complex GF_i. Replace the old unlimited free-packet source by the following type-neutral reactions:

| Reaction | Propensity | Physical role |
|---|---:|---|
| C -> CF | g C | Capture from the maintained environmental source into an empty carrier |
| CF -> C | ell_c CF | Loss of the stored packet |
| CF -> D + F | b CF | Carrier wear, releasing its stored packet |
| C -> D | b C | Wear of an empty carrier |

Keep all A_i formation, copying, fabrication, wear, G_i/Y binding, reproduction, recycling, and free/bound fuel reactions of the architecture law. CF may catalyze the same recycling reaction as C; that choice is immaterial to the retained-scaffold proof because no D coexists with either form there. No reaction reads an analyst's success flag or changes a parameter following delivery. The same CF reactions apply to both architectural types.

The source supplies work by g C; it does not supply material. The new material and packet counts are

\[
\begin{aligned}
N={}&R+C+CF+Y+D+
\sum_i(A_i+G_i+GF_i+2YG_i),\\
U={}&F+CF+\sum_i GF_i,\qquad W=N-D+U.
\end{aligned}
\tag{2}
\]

CF counts once in N and twice in W. Capture adds one W, packet leakage loses one, and CF wear conserves U while losing one W through carrier degradation. Recycling spends one packet to convert D to R, with zero net change in W. A fabrication or birth spends one W, as before. Releasing the stored packet on carrier wear does not create a second packet.

This is a changed storage architecture, not a reinterpretation of the old free-packet source. In particular, the model does not contain CF -> C+F followed by unrestricted recharging. Such a release channel would permit a larger free reserve and invalidate the proof below.

## 3. The entry, failure boundary and finite state space

For each i, consider the actual operational state

\[
P_i:\quad A_i=YG_i=CF=1,\quad F=0,
\qquad N=4,\quad W=5,
\tag{3}
\]

with every unlisted species absent. The three A/G/Y constituents form the retained scaffold; C may wear and be rebuilt repeatedly. End this *scaffold episode* at its first A, G or Y constituent wear, or when capture access is irreversibly lost. A scaffold wear is an observable episode boundary, not a claim that all later organization is impossible. Later successor episodes are not covered by this comparison.

Before such wear, three of the four material units remain committed to A, G and Y. Only one unit can be R, C, CF or D. Starting at P_i:

1. U<=1 throughout the episode: an empty C can store one packet, and releasing that packet through CF wear removes C.
2. R can appear only by recycling D with the released packet. Hence R>0 implies C=CF=U=0.
3. RF=0 throughout. No A birth, copying, or additional G fabrication can occur during the episode. Their rates are not silently set to zero; their reactants are unavailable.
4. Every reproduction event that consumes the sole R leaves R=C=CF=U=0. Subsequent wear can produce D but cannot restart capture or recycling. This is an actual invariant loss of source access under the declared repertoire.

The live episode therefore has only nine states after relabeling the architectural type. Write B for bound YG, V for free G plus free Y, and V_F for GF plus free Y. A=1 is implicit:

\[
(CF,B),(CF,V),(C,B),(C,V),
(D,F,B),(D,F,V),(D,V_F),(R,B),(R,V).
\tag{4}
\]

Both types have the same finite state space and all the same transitions except for bound reproduction from (R,B). A/G/Y wear has total rate

\[
\omega=\eta+\delta+d>0
\tag{5}
\]

in every live state, including bound complexes. Free reproduction also kills capture access, identically for both types. Bound reproduction does so at rate zeta_i beta.

## 4. All-path occupation and renewal comparison

Let Q_zeta be the generator restricted to the nine live states; its row sums include the losses to the failure boundary. Write z=(R,B), e_z for its coordinate vector, and let q=(zeta1-zeta0) beta>=0. Then

\[
Q_{\zeta_1}=Q_{\zeta_0}-q e_z e_z^T.
\tag{6}
\]

This is derived killing, not an assigned fitness bonus. The type-dependent reaction consumes the only precursor through which the organization could regain environmental support.

For every nonnegative state reward r and every t>=0,

\[
\begin{aligned}
\mathbb E_{\zeta_1}[r(X_t);\tau>t]
={}&\mathbb E_{\zeta_0}\left[
r(X_t)\mathbf1_{\{\tau>t\}}
\exp\left(-q\int_0^t\mathbf1_{\{X_s=z\}}ds\right)
\right]\\
\le{}&\mathbb E_{\zeta_0}[r(X_t);\tau>t].
\end{aligned}
\tag{7}
\]

**Proof.** Couple every common reaction until the episode ends, and add an independent rate-q killing clock while in z for the higher-zeta process. Every higher-zeta live trajectory is an identical lower-zeta trajectory until that extra clock rings. The conditional probability that it has not rung is the exponential in (7). The finite graph makes the identity exact without any unbounded-generator interchange. No normalization by survival occurs. All unsuccessful paths reduce the unconditional mass. 

In particular, (7) orders the episode survival probability, probability of having C or CF, expected productive occupation, and occupation of the precise return state P. For positive a,b,g,nu,mu,k theta,beta and unequal zeta, the order is strict at every t>0 for the C/CF occupation reward: the finite route

\[
CF\text{ wear}\;\to\;YG\text{ dissociation}
\;\to\;Y\text{-recycling}\;\to\;Y\text{-binding}
\;\to\;C\text{ assembly}\;\to\;\text{capture}
\tag{8}
\]

has positive probability of completing before t, with positive time spent at z. It restores the exact state P. One packet pays for recycling; one fresh capture restores the packet that will fund a later repair. There is no reset or supplied reserve at the return.

In the same coupling, count C reassemblies or completed C-damage/renewed-capture episodes up to the first scaffold loss, freezing the count at that boundary. Every event of the higher-zeta process is also an event of the lower-zeta process until their separation; the former produces no further episode events afterward. Thus the lower-zeta count dominates pathwise under this coupling, and its unconditional count tails and expectation dominate. This includes all retained-scaffold repair routes, not just route (8). It does not include A/G/Y succession.

There is also an explicit occupation formula. Let

\[
M_0=-Q_{\zeta_0},\quad N_0=M_0^{-1},\quad
V_0=N_0r.
\]

Since the episode is killed at rate at least omega, its mean duration is at most 1/omega and the inverse exists. The exact rank-one inverse identity gives, from any live initial state p,

\[
\boxed{V_0(p)-V_1(p)=
\frac{q\,N_0(p,z)\,V_0(z)}{1+qN_0(z,z)}.}
\tag{9}
\]

Every factor has a physical interpretation: time spent exposed to the destructive allocation, productive continuation available from that state, and the extra loss rate. The relation predicts an absolute occupation gain, not an enriched proportion among survivors.

## 5. A finite moderate-rate example and an identifiable test

Set all active rate constants to one, including k theta=1, eta=delta=d=1, and compare zeta0=0 with zeta1=1. Thus omega=3. In the state order (4), the non-killing jumps and killing rates are:

| Row | Jumps, each at unit rate | Killing rate |
|---:|---|---:|
| 1 | 2, 3, 5 | 3 |
| 2 | 1, 4, 6 | 3 |
| 3 | 1, 4 | 4 |
| 4 | 2, 3 | 4 |
| 5 | 6 | 4 |
| 6 | 5, 7, 9 | 4 |
| 7 | 6 | 4 |
| 8 | 3, 9 | 3+zeta |
| 9 | 4, 8 | 4 |

Exact rational inversion of this nine-state matrix, starting at row 1, gives:

| Unconditional quantity until episode loss | Blocking, zeta=0 | Nonblocking, zeta=1 |
|---|---:|---:|
| Mean episode duration | 332837/1101408 | 401591/1329312 |
| Expected time with C or CF | 11497/45892 | 13875/55388 |
| Expected fresh captures | 11593/275352 | 13987/332328 |
| Expected C reassemblies | 24/11473 | 28/13847 |

For example, expected C reassemblies increase from approximately 0.00202210 to 0.00209187, a small positive absolute gain. All rates are finite and comparable; no extremely fast formation limit is needed for this *retention* comparison. The small numbers also show that a beneficial mechanism need not be a reliable organization.

For reproduction of these arithmetic claims, form Q from the transition table, put its diagonal equal to minus the entire row exit rate, and multiply (-Q)^{-1} by the reward vectors: all ones; the indicator of rows 1–4; the indicator of rows 3–4; or the indicator of rows 8–9, respectively. An exact rational calculation additionally gives N_0(1,8)=4/11473 and N_0(8,8)=2374/11473, supplying a direct check of (9).

The practical next test is identifiable: independently measure the nine-state transition rates, including packet retention and release on C wear, then predict the unconditional number of C reassemblies and total C/CF occupation per entered scaffold. Measure all entered scaffolds, including immediate failures. Do not infer those rates from the same survival-selected output being predicted. Count supplied/captured packets, leaked packets, carrier loss and repair events as separate observations. The primary structural test is whether R>0 really implies C=CF=U=0 during the declared episode. A substantial reserve, a packet-release bypass, additional precursor stock, or a source-access restart invalidates the killing reduction and requires a larger model. A scalar improvement in survival cannot establish the proposed mechanism if these transitions are unobserved.

This is a suggested experimental interface, not evidence that any existing molecular implementation has these states or kinetics.

## 6. Formation is paid, but its complete direction remains open

The same common-law preparation as the earlier architecture theorem is available:

\[
Z_0:\quad R=3,\ Y=1,\ F=2,
\quad A_i=G_i=C=CF=0.
\tag{10}
\]

The first-five-event route

\[
\text{form }A_i\to\text{fabricate }G_i
\to\text{bind Y}\to\text{assemble C}\to\text{capture into CF}
\tag{11}
\]

reaches P_i. Both types are generated under one fixed reaction law; all intermediate objects are constructed and both formation packets are consumed. Here W starts at 6 and ends at 5: two construction losses and one new capture. The entry is not energy-neutral, and its net expenditure is not hidden by defining P as the later starting state.

Let E_i(dt) be the *subprobability* time measure that the first five reactions are precisely (11). Its five selected rates are 6 sigma, 2 kappa, mu, a, g. Every other reaction remains in its holding-time denominator. If rho0<=rho1 and the remaining type-specific constants agree, those total hazards differ only at two stages: the A1 copying competition is larger after formation, and the zeta1 reproduction competition is larger after binding. Hence E_0>=E_1 as time measures. This is an actual probability comparison from Z0, with unsuccessful first events included, not a normalized selection of successfully formed types.

Convolving E_i with the occupation or return kernels above gives a larger unconditional retained-scaffold contribution for the blocking type along this declared paid formation event. Thus the retention theorem can attach to a material formation process rather than to a freely supplied regulator.

However, other formation histories exist. Ordering these particular subprobability contributions does not order the complete endogenous entry measures, architectural prevalence, or population reproduction. Equal scaffold preparation is also not a claim of identical physical microstates: the two structures and their supplied reaction channels differ. The [other note's turnover construction](INTEGRATED-FORMATION-RENEWAL.md) belongs to the old free-packet chemistry and cannot be imported into this new storage architecture.

Indeed, the precise one-slot CF law has a stronger limitation. Define the accessible-precursor count

\[
V=R+C+CF+F+\sum_iGF_i.
\tag{11a}
\]

At P, V=1. Every reaction preserves or decreases V: capture exchanges C for CF; charged-carrier wear exchanges CF for F; recycling exchanges F for R; packet transfer between F and GF preserves it; formation and fabrication consume both R and F. Thus V<=1 forever from P, including after scaffold wear. Consequently RF=0 forever, and **no later A birth, copying or G fabrication is possible under this precise storage law**. Full scaffold replacement is impossible, not merely unproved. V is an availability count, not energy: the prospective reaction CF -> C+F would raise V by one while preserving W. The obstruction concerns how captured support can reach the combinations required for construction.

A concrete prospective extension is to provide paid access to the bound packet without first destroying C, for example

\[
D+CF\to R+C,\qquad
R+CF\to A_i+C,\qquad
A_i+R+CF\to A_i+G_i+C.
\tag{11b}
\]

These would be new supplied reaction channels with finite material-dependent propensities, not instructions issued on a successful history. They spend one bound packet each; recycling preserves W and A/G construction loses one W. They are disabled in all nine live states of (4), so adding just these channels leaves the retained-scaffold theorem and arithmetic unchanged. They become relevant after scaffold wear. For example, A wear -> bound-packet recycling -> capture -> bound-packet A formation -> capture would restore P with two fresh packets and all formation competitors present. This specifies a paid return route and a testable interface. It does not establish a comparison of the full successor kernels, favorable total entry, or architectural selection. Those claims remain the next target under an explicitly extended law; the invariant (11a) must not be carried over to that different law.

## 7. Observable limits and thermodynamic scope

At the state immediately after charged-C wear, the only possible first events are packet leakage, YG dissociation, and scaffold constituent wear. Therefore the all-path probability of returning to P while retaining this scaffold obeys

\[
\Pr(\text{return to }P)\le
\frac{\nu}{\nu+\ell+\omega}.
\tag{12}
\]

Increasing fabrication, capture or binding cannot remove this first-stage bound: those favorable reactions are disabled there. If the source is unavailable, renewed capture cannot occur. If k theta=0 or nu=0, this damaged bound state cannot perform the needed recycling before scaffold loss. Very rapid rebinding can also prevent free Y from recycling in time. The mechanism has an explicit failure region, not a universal sign for arbitrary parameter changes.

Positive wear further gives

\[
\mathbb E\tau\le1/\omega,\qquad
\mathbb E K_{\text{C reassembly}}\le b/\omega,
\tag{13}
\]

because C reassembly requires a preceding C wear and the carrier-wear intensity is at most b. No infinite retained-scaffold life follows from the strict improvement.

The irreversible channels here are an effective driven model. Adding thermodynamic reverse channels can permit recovery across the original failure boundary and break the exact killing representation. A finite-horizon strict gap can nevertheless be robust: if the total added-channel rate before its first occurrence is bounded by epsilon on the old reachable states, an individual bounded-event probability changes by at most 1-exp(-epsilon T). An old gap larger than twice this amount persists when both compared laws are extended. That perturbation bound does not provide the reverse rates, establish local detailed balance, or justify arbitrary affinities. Expected unbounded rewards require a separate moment bound; the bounded-event statement must not be reused for them.

There is also a precise equilibrium obstruction to interpreting kinetic usefulness as an unconditional physical selection law. Suppose a reversible completion has a finite connected conserved class, every retained reaction pair obeys detailed balance with a distribution

\[
\pi(n)=Z^{-1}\frac{\exp[-\Phi(n)]}{\prod_s n_s!},
\tag{14}
\]

and the class and Phi are invariant under exchanging A0 with A1 and all corresponding gate complexes. The stationary law then has exactly that exchange symmetry, even if kinetic prefactors differ or an entire reaction pair is omitted. Detailed balance remains valid on every remaining edge; connectedness makes its stationary law unique. Thus every swapped architecture event has equal equilibrium probability. Without connectedness, the conclusion requires restricting to a swap-invariant communicating class; a class chosen asymmetrically is not evidence of useful-architecture selection.

A maintained nonequilibrium source can remove this equilibrium obstruction, but does not by itself supply a favorable retention or copying coupling. Equation (6) exhibits one such coupling under a declared material constraint. Whether a physically realized organization has it must be determined from its actual reaction and transport law.

## Provenance and review scope

Read in full for this note: the architecture-formation source, [renewal-return source](RENEWAL-RETURN.md), [integrated formation/renewal note](INTEGRATED-FORMATION-RENEWAL.md), and repository instructions. The [direction/turnover result](DIRECTION-AND-TURNOVER.md) was read and reviewed in the preceding turn; its unchanged source hash is retained below. The current integrated-formation checker output was also read to check its 21-event turnover path and declared hazard polynomials; that turnover proof was not treated as a proof for the changed CF chemistry. No empirical physical source is invoked in support of the proposed CF mechanism.

Frozen antecedent hashes:

| Source | SHA-256 |
|---|---|
| ARCHITECTURE-FORMATION-CRITIQUE.md | `d20d3284cb2afe84884d567c7d39efe1b3a360fee9375b2158c8116fc7e50362` |
| RENEWAL-RETURN.md | `8c72623e2cb4d4cc11ae944ef8fbefeb25e5b002187f0e7544670cfd13db827c` |
| DIRECTION-AND-TURNOVER.md | `7c819e13ff39c2c42e602946a498cc159e943bccd985444839e8724b3d97fe20` |

The nine-state generator and exact-rational values above are newly derived here. They establish a finite effective-model result. Endogenous total entry, complete successor organization, thermodynamic realization and prevalence remain distinct unfinished claims.
