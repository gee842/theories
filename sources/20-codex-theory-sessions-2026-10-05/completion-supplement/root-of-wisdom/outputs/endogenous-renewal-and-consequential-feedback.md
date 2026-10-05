# How renewal and regulation arise within a shared situation

Research continuation for Ren, 5 October 2026. This advances the physical question in [Relational regeneration and a direction in reality](relational-regeneration-and-direction.md): how can a situation develop and maintain its own renewal machinery? The explanatory unit remains the coupled situation, including its differentiated capacities and the conditions through which they work.

**The new result is that renewal machinery can start absent, form from available material, and establish a regenerative regime that attracts every deterministic state containing some usable material or machinery, above a calculable threshold.** The same reactions produce rudimentary regulation with a level determined by their rates. A second result explains why successful regulation of an aggregate can leave an internal deterioration invisible. Neither result establishes a universal tendency toward kindness, but both give the proposed direction toward 善 more specific physical content.

## Renewal machinery can form within the process

Consider usable material \(R\), renewal machinery \(C\), and degraded material \(D\). Available material assembles into machinery; machinery wears out; powered machinery converts degraded material back into usable material:

\[
R\xrightarrow{a}C,\qquad
C\xrightarrow{b}D,\qquad
D+C\xrightarrow{k,\;\text{powered}}R+C.
\]

The rates \(a,b,k\) are positive. The last reaction requires a maintained source of usable energy. At fixed volume, the joint equations are

\[
\dot R=kCD-aR,\qquad
\dot C=aR-bC,\qquad
\dot D=bC-kCD.
\]

The total \(M=R+C+D\) is conserved. Machinery has a material cost, wears out, and must be rebuilt. Its abundance is a changing part of the situation. In particular, if \(C(0)=0\) and \(R(0)>0\), then \(\dot C(0)=aR(0)>0\): the machinery actually forms.

There is an exact threshold:

\[
\boxed{kM>b.}
\]

Above it, every deterministic trajectory with some initial usable material or machinery converges to

\[
D_*=\frac bk,\qquad
C_*=\frac{a}{a+b}\left(M-\frac bk\right),\qquad
R_*=\frac{b}{a+b}\left(M-\frac bk\right).
\]

At or below the threshold, usable material and machinery both tend to zero. The all-degraded state remains inactive even above the threshold because this reaction scheme contains no route out of it without some initial \(R\) or \(C\).

For unit rates, starting with \((R,C,D)=(3,0,0)\) yields \((R,C,D)\to(1,1,1)\). The positive amounts are maintained by continuing transformation. This is a global convergence result within the stated deterministic model, extending the earlier result about recovery near an already installed regenerative arrangement.

![Machinery forms from zero and persists only above the renewal threshold](/Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/outputs/endogenous-renewal.png)

The figure illustrates the constructed model with maintained energy input. The threshold curve is analytic; the time courses were checked at two integration step sizes. They are not experimental observations.

## A regulatory level emerges from the reactions

The equation for degraded material can be written

\[
\boxed{\dot D=-kC\left(D-\frac bk\right).}
\]

Where machinery persists, departures from \(b/k\) generate a restoring response. Above that level, recycling exceeds degradation; below it, degradation exceeds recycling. No controller was given a desired level of \(D\). That level follows from the reaction rates, while the speed of return depends on how much machinery the same process maintains.

This gives a minimal physical example of activity forming the means through which its enabling conditions are renewed and regulated. It is rudimentary regulation. Anticipation, learning, allostasis, and consciousness are not present in these equations.

The premise has also become clearer. The model supplies possible reactions, including a catalytic function and a route for its assembly. It derives their sustained organization and operation. It does not derive the chemical laws that make those functions possible or explain the invention of a new reaction repertoire.

## A broader constraint on continued organization

A general result explains why the threshold matters. Suppose enabling capacities are consumed or wear out, and their production is bounded by the contributions of other capacities. If the whole network's productive feedback is too weak to compensate for losses, all those capacities decay. An acyclic production network necessarily fails this test when no independent production is available.

In the formal version, production is bounded by a nonnegative matrix \(B\), losses by a positive diagonal matrix \(L\), and the critical quantity is \(\rho(L^{-1}B)\), the spectral radius measuring aggregate renewal gain. If it is below one, an explicit weighted sum of capacities decreases exponentially. Multiple interacting cycles can contribute to this gain; connectivity or a single cycle's presence does not settle the result.

The three-component model fits this bound with capacities \((R,C)\): its spectral radius is \(\sqrt{kM/b}\). Above one, the additional nonlinear equations establish attraction to the active regime. The general inequality alone would not prove that attraction.

This produces testable distinctions: weakening a renewal pathway can cross a threshold; restoring a connection need not restore adequate gain; and independently supplied capacities can maintain a network that cannot renew them internally. These are physical consequences under declared conditions, not an assumption that whatever persists must be good.

## A shared total can hide a consequential difference

The earlier work on [plural requirements and attainable correction](/Users/ren/theories/sources/15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md) showed why separately satisfiable requirements do not guarantee one jointly workable arrangement. Here we add a dynamical counterpart: a healthy aggregate signal does not guarantee that every indispensable support is regulated.

Take two supports within one organization. One can improve while the other deteriorates, leaving their measured total unchanged. In an explicit linear model, a growing difference between the supports is invisible to a controller that receives only their total. Any controller confined to that observation and the specified fixed actuation cannot stabilize every nearby initial state. It receives identical histories from situations that require different corrections.

Adding a response pathway for that difference can restore stability, but its effect must counteract deterioration with sufficient strength and suitable dynamics. Information arriving somewhere is insufficient if it cannot change the relevant activity. The [mathematical companion](endogenous-renewal-mathematics.md) gives the exact inequalities and an independent matrix check.

This connects to the original question about an important possibility missing from a model. Sometimes the missing possibility is a consequential difference erased by the observation itself. More reasoning over the same aggregate cannot reveal it in the constructed example. A different observation, or an intervention that makes the difference observable, is needed.

## Physical scope and evidence

These results belong to an existing research tradition. Montévil and Mossio describe biological organization through constraints that contribute to maintaining one another. Their account concerns open thermodynamic conditions and does not imply an isolated, self-sufficient organism. [Biological organisation as closure of constraints](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/).

There is also relevant experimental evidence: Miras and colleagues report spontaneous formation of inorganic autocatalytic sets from molybdate chemistry, supported by kinetic observations, interventions, and a phenomenological model. This shows that such formation is a physical possibility under particular chemical conditions. It does not validate our exact three-component equations or a universal direction toward 善. [Miras and colleagues, 2020](https://www.chem.gla.ac.uk/cronin/images/pubs/Mathis-PNASMay2020.pdf).

Two limits materially affect the interpretation. First, finite available energy places a finite bound on accumulated machinery activity; the positive regime assumes continuing energetic support. Second, the exact finite-particle stochastic version eventually reaches the all-degraded absorbing state with probability one. The deterministic attractor therefore supplies no guarantee of eternal survival. Its use for finite physical systems requires a scale and time horizon, and any claim about long persistence requires a separate lifetime calculation.

## The revised foundation and the remaining universal claim

The strongest supported formulation is now:

> Under specified physical conditions, transformations can produce and maintain capacities that renew their enabling conditions. The resulting joint organization can exert a restoring influence on its own conditions of continuation. Where destabilizing differences are otherwise hidden, robust regulation can require additional causal access to them.

This brings renewal, information, and correction into a connected physical account. Distinct centers remain consequential within the shared situation. A useful description of the whole must retain differences that affect whether its processes can continue and change.

The proposed direction toward 善 would be stronger still: regenerative organization would increasingly include the conditions of other affected centers in effective repair and regulation. The present models do not derive that widening of concern, the endogenous development of new observation pathways, or open-ended creation of new forms. Their contribution is to identify mechanisms and thresholds that a stronger theory must explain, rather than treating all regulation or all interconnectedness as already sufficient.

The earlier theories remain preserved. Full proofs, finite-energy and stochastic limits are in the [mathematical companion](endogenous-renewal-mathematics.md); checks, source scopes, and the preservation audit are in the [evidence record](endogenous-renewal-evidence.json).
