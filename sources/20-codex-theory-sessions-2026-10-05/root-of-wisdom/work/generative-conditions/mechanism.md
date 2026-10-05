# Products can become the conditions of later transformations

Mechanism audit, 5 October 2026. This is a deliberately supplied mathematical reaction system, not an empirical chemistry claim. It supplements, rather than replaces, `outputs/generative-becoming.md` and `outputs/changing-the-interface.md`. Those reports already state the recursive proposal and show changing interfaces; the addition here is an explicit, resource-accounted formation mechanism and causal ablation.

## The substantive premise

Change alone is insufficient. The needed premise is that a transformation can produce something which, while it remains present and coupled to suitable surroundings, participates in a later transformation. This includes transient intermediates: "persistence" means lasting long enough to participate, not permanent storage. A produced catalyst is a particularly clear example because the product becomes an enabling factor in a different reaction.

This gives a precise reading of the user's thought:

> Some consequences of an interaction become conditions of subsequent interactions. Because those conditions themselves can be produced, change can alter how later change occurs.

The first sentence is a substantive physical possibility, not a consequence of the bare logical existence of difference. The second explains a conditional mechanism of generativity. Neither entails continual improvement, unlimited growth, or invention of laws.

## A fixed-law cascade with endogenous enabling conditions

Use the following idealized reaction rules:

\[
R_1:A+F\longrightarrow A+B,\qquad
R_2:B+G\longrightarrow B+C,\qquad
R_3:C+H\longrightarrow C+D.
\]

The seed A catalyzes conversion of environmental feed F into catalyst B. B then catalyzes conversion of a different feed G into catalyst C. C enables conversion of H into D. The catalysts are not consumed by these conversions. F, G, H and each catalyst/product have equal assigned unit mass, so each rule conserves that mass. The rules and their feasible chemistry are stipulated; this is not a thermodynamic derivation or an assertion that arbitrary named materials have these reactions.

Start with one A and one each of F, G, H, but no B, C, D. Only R1 can fire. After it produces B, R2 becomes active; after R2 produces C, R3 becomes active. In three events the initial inventory

\[
(A,F,G,H)=(1,1,1,1)
\]

becomes one each of A, B, C, D. It has not acquired mass or a new fundamental law. Its effective repertoire of immediately executable reactions has changed twice through the production of new participants. The reactions R2 and R3 belonged to the global law from the beginning, but their needed catalysts were absent.

Crucially, the catalyst-producing event and the newly enabled event act on different feedstocks. The observation is therefore more specific than a two-state toggle or a reaction repeatedly consuming another unit of the same resource. B is both an outcome of R1 and an input condition of R2. C has the same dual role for R2 and R3.

For an observed organization, these catalysts may be outside its chosen boundary. The operative distinction is participation in shared dynamics, not a metaphysically separate environment. If B diffuses into a neighboring region containing G, its production changes that region's reaction conditions. If B remains physically isolated from G, producing it does not enable the local R2 reaction there. The spatial transport rule would have to be specified to make that variant a spatial model; a coupling parameter below isolates the relevant condition without claiming to derive space.

## Continuous dynamics make the onset explicit

Let the conversion fluxes be

\[
j_1=k_1af,\qquad j_2=\kappa_B k_2bg,\qquad
j_3=\kappa_C k_3ch,
\]

where all k are positive, and coupling factors \(\kappa_B,\kappa_C\in[0,1]\) represent stipulated access of the catalyst to its next feed. The factorization displays three requirements: catalyst, accessible substrate, and a supplied interaction law.

With optional positive catalyst decay rates, a complete material account is

\[
\begin{aligned}
\dot a&=-\delta_Aa,&\dot f&=-j_1,\\
\dot b&=j_1-\delta_Bb,&\dot g&=-j_2,\\
\dot c&=j_2-\delta_Cc,&\dot h&=-j_3,\\
\dot d&=j_3,&\dot w&=\delta_Aa+\delta_Bb+\delta_Cc.
\end{aligned}
\]

All variables are nonnegative, and the total \(a+b+c+d+f+g+h+w\) is constant. Positive irreversible rates presuppose physically suitable reaction conditions; mass conservation alone is not an energy or free-energy account.

At an initial state with \(a_0,f_0,g_0,h_0>0\) and \(b_0=c_0=d_0=0\),

\[
\dot b(0)=k_1a_0f_0>0,
\qquad
\dot c(0)=0,
\qquad
\boxed{\ddot c(0)=\kappa_B k_2g_0k_1a_0f_0.}
\]

If the coupling is positive, the initially inactive second conversion develops positive flux as B is produced. Locally,

\[
c(t)=\tfrac12\kappa_B k_2g_0k_1a_0f_0\,t^2+O(t^3).
\]

The third stage begins one order later:

\[
d(t)=\tfrac16\kappa_C k_3h_0\kappa_B k_2g_0k_1a_0f_0\,t^3+O(t^4).
\]

These are local Taylor statements for the supplied smooth equations, not general universal powers of time. The derivatives expose mediation: C is initially unchanged, but a prior product causes its later rate of change to become positive. Fixed laws can therefore generate changing effective causal participation.

The ideal rules set uncatalyzed conversion to zero. In a less ideal model with a positive background reaction rate, the appropriate claim may instead be that a product accelerates a reaction enough to make an outcome achievable within a specified budget or time. A previously inactive channel and a newly useful rate must not be conflated.

## Witnesses and ablations

The following comparisons preserve the relevant starting feedstocks and reaction laws except for the named intervention:

1. **Retained intermediate:** permit R1, retain B, and keep B coupled to G. R2 and then R3 can occur.
2. **Remove the product after its formation:** transfer B into an inert waste compartment immediately after R1. R1 still occurred and its resource cost is still paid, but no C or D is produced from the remaining initial state. This isolates the intermediate's role without pretending to hold the whole state identical.
3. **Break the coupling:** set \(\kappa_B=0\). B is still produced; C and D stay zero. The presence of a product alone is insufficient.
4. **Remove the complementary condition:** set \(g_0=0\). B can form, but C cannot. The product's capacity is relational: it depends on an available partner under the supplied law.
5. **Break the second coupling:** set \(\kappa_C=0\). C can still form but D cannot. A generative cascade can stop after an intermediate success.

These comparisons discriminate the proposed mechanism from mere chronology. It is not enough that C follows B; disabling B's participation prevents the specified downstream transformation. The discrete exact check enumerates reachable inventories and verifies these claims. Its purpose is checking the tiny construction, not establishing a scientific novelty claim.

## Resource exhaustion is an exact limit

Let \(N_i\) be the number of firings of reaction Ri in the discrete model. Since each firing consumes one distinct feed token,

\[
N_1\le F_0,\quad N_2\le G_0,\quad N_3\le H_0,
\qquad
N_1+N_2+N_3\le F_0+G_0+H_0.
\]

Thus every trajectory in a closed finite inventory contains finitely many productive events, even if catalysts never decay. The same continuous bound is \(\int_0^\infty(j_1+j_2+j_3)dt\le f_0+g_0+h_0\). A finite chain of condition production does not sustain its own supply conditions.

When all catalyst decay rates are positive, A tends to zero directly. Each later catalyst is a stable linear decay process driven by a nonnegative input with finite integral; consequently B and C also tend to zero. Retained inert product D can remain after productive capacity has vanished.

Closing the dependency diagram with \(C+H\to C+A\), rather than producing D, would create a catalytic renewal cycle, but it would not remove this finite-feed bound. A cycle without replenishment is not indefinite generativity. Supplying feed indefinitely addresses exhaustion but still does not prove genuinely new kinds of capacity keep appearing: this finite network has only the listed conversions. These two failures are logically distinct.

## What can be generalized, and what cannot

For a fixed global law L, an effective enabled-reaction set can be defined as

\[
\mathcal E_L(z)=\{r: \text{all participants and coupling conditions for r occur in z}\}.
\]

A transition \(z\to z'\) can change \(\mathcal E_L\) when its products participate in later reactions. That alone can include trivial toggles. The cascade supplies the additional mechanistic witness: a produced participant activates a distinct conversion, and removing its participation removes that conversion. The definition does not by itself identify all important mechanisms or discover unlisted possibilities.

The operative feedback can be stated as: **an interaction changes the participants and surroundings of later interactions; where those changes persist and couple appropriately, the consequences become productive conditions.** The active channels can change while the underlying laws remain fixed.

This explains a way the world can be naturally generative without an external designer or a separate source of each new local operation. It does not derive those laws from monism, establish that every change is generative, prove that the actual universe grows indefinitely more complex, or prove that all novelty is beneficial. Sustained novelty additionally requires renewable resources and losses under control, while open-ended novelty needs a model whose constructible repertoire is not exhausted after finitely many prelisted stages.

The strongest advance over the prior reports is therefore small but substantive: the product/condition dual role is now instantiated by a mass-balanced mechanism, a time-resolved onset, causal ablations, and a precise exhaustion bound. It gives physical content to the proposed recursive principle without presenting a notation for dynamics as an explanation of all dynamics.
