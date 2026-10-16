# Costed revision of a selector in a continuing organization

6 October 2026. AI-authored mathematical contribution to the [accepted derivation](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence). The transition addressed is **consequence-dependent retention of responses → consequence-dependent revision of a mechanism that selects responses**. The [previous construction](FORMED-VARIANT-SELECTION-INTEGRATION.md) left the access and copying mechanisms fixed. This construction makes one response-routing mechanism a paid, replaceable, return-maintained structure within the same continuing compartment.

The result is conditional. It supplies a two-member routing repertoire, random assembly, a finite wear counter and a return-funded copying reaction. It derives changes in the routing mechanism from their consequences under that architecture. It does not derive the repertoire, assembly law, copying fidelity, compartment or renewal architecture from the abstract root. The revision mechanism itself does not undergo further revision.

This is a **new conditional process sharing the costed causal-root interface** with the preceding formation study. It is not an exact composition, kinetic quotient or refinement of that molecular model. A physical construction joining the former model's actually formed constituents to this model's routing token and renewal reactions remains an unresolved interface. The present local result cannot silently count that interface as closed.

## 1. State, physical consequence and supplied control architecture

There is one continuing compartment. Its state contains available fuel F≥0, remaining source packets H≥0, a selector type m∈{0,1}, selector lifetime ℓ∈{0,…,L}, and the plant's hidden condition z∈{0,1}. Lifetime zero means no active selector. A residual type label at zero lifetime has no routing power. Every packet contains G fuel units. Material for one selector is recycled; this model does not represent molecular stoichiometry beyond that fixed inventory.

A sensed bit b is routed to a reconstructed response

\[
a=b\mathbin{\mathrm{XOR}}m.
\]

The plant permits capture of the current packet only when a=b XOR z. Thus capture occurs exactly when m=z. This equality is a statement about physical compatibility in the supplied plant. Neither the assembly choice nor a routing computation reads z, elapsed time or the schedule of future conditions. The local mechanism experiences actual return and the absence of return. The externally supplied schedule may change z while retaining all the compartment's existing state.

Let c>0 be assembly cost, d>0 the combined sensing and response-construction cost, r>0 selector renewal cost, and L>0 its lifetime. Assume **G≥r**, so an actual captured packet can pay renewal. The primary experiment uses c=1, d=2, r=1, G=4 and L=2. These are declared discrete costs, not measured biological parameters.

The reactions are:

| Event | Enabling condition | State update |
|---|---|---|
| Assemble m′ | ℓ=0 and F≥c | F′=F−c; m′ sampled equally from {0,1}; ℓ′=L |
| Productive trial | ℓ>0, F≥d, H>0, m=z | F′=F−d+G−r; H′=H−1; ℓ′=L; m unchanged |
| Unproductive trial | ℓ>0, F≥d, H>0, m≠z | F′=F−d; H′=H−1; ℓ′=ℓ−1; m unchanged; G wasted |
| External change | Declared plant schedule | z changes; F,H,m,ℓ unchanged |
| Unused source opportunity | A packet expires | H′=H−1; G wasted; compartment unchanged |

Sensing and response reconstruction are paid **before** capture; future return cannot finance their initiation. A successful trial replaces or renews the routing structure with the same type at cost r. This is type-preserving material inheritance within the compartment, not reproduction of the whole organization. An unproductive trial still reconstructs its selected response and pays its cost. Wear eventually removes the selector's ability to route, exposing the material to another paid assembly. No observation is converted into an analyst-defined score.

The executable round law schedules at most one assembly followed by one trial per opportunity. A paid assembly that leaves insufficient fuel for the trial remains a charged failure. The relational formalization allows individual events and arbitrary supplied reversals; the analytical result below specifies the round schedule and a single ensuing stable condition. The event relation, probabilistic scheduler and executable implementation are distinct claims.

This is **within-organization revision** because one compartment carries its resources and accumulated condition through different response-routing mechanisms. It is not a change in the frequencies of independently competing compartments. The persistent compartment and the physical interpretation of its boundaries remain supplied.

## 2. Energy conservation prevents an implicit reset

Define available total energy, including uncaptured source packets, by

\[
\mathcal E(F,H)=F+GH.
\]

Assembly decreases it by c. A productive trial decreases it by d+r; an unproductive trial decreases it by d+G. Expiry decreases it by G. External condition change leaves it unchanged. Therefore every finite event history satisfies

\[
\boxed{\mathcal E_{\rm final}
+\text{assembly, sensing, response and renewal expenditure}
+\text{wasted packet energy}
=\mathcal E_{\rm initial}.}
\tag{1}
\]

The [Lean event law](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean) proves this ledger for every valid trace. Its traces use the existing `Generative.Trace` definition directly; concatenation passes the actual intermediate state. Reversal has no fuel or lifetime reset.

A mechanically checked example starts without a selector at F=7,H=4. It pays assembly of m=0, obtains a productive return under z=0, experiences z=1, pays two unproductive trials, pays assembly of m=1 and obtains a productive return. The final state has F=3,H=0 and the revised selector. Its sensory response mapping has changed. The same example also exhausts its source; it is not indefinite persistence.

The finite source implies a limit on the total number of actual trials and renewals. We make no claim that maintaining a selector can manufacture unlimited opportunities or fuel. More generally, successful maintenance can preserve a mechanism while leaving the compartment poorer if G<d+r. Return-funded persistence is not identical to net organizational growth.

## 3. Exact reserve and time threshold for first recovery

Consider an actual reversal boundary at which the compartment has fuel F, an outdated selector m≠z with residual lifetime k∈{0,…,L}, and H remaining source opportunities. The k=0 case denotes an already expired selector residue; its next exposure begins with paid assembly. The new condition stays constant through the diagnostic interval. The remaining k trials under the outdated selector are unproductive. Thereafter each assembly independently produces a useful selector with probability q; the binary unbiased law has q=1/2. For the calculation, there is no packet interception, false local return, further condition reversal or unmodeled leakage.

Call **recovery** the first productive trial and its paid same-type renewal. This is not a requirement of subsequent survival, long-run return, accurate representation or ethical concern. Since G≥r, the productive packet itself pays the renewal, but its capture must first be initiated from current fuel.

If exactly j useless candidate selectors are assembled before the first useful one, the paid pre-return prefix contains:

1. k unproductive trials from the inherited selector;
2. j blocks, each containing one paid assembly and L unproductive trials;
3. one further assembly and the productive trial's prepaid sensing/response cost.

Consequently its exact cost and opportunity count are

\[
\boxed{C_j=kd+c+d+j(c+Ld),\qquad T_j=k+1+jL.}
\tag{2}
\]

All these pre-return costs are nonnegative and there is no inflow before the last trial. Thus the prefix can pay **every intermediate charge** if and only if C_j≤F. This is not merely an endpoint estimate: the formal `Paid` relation checks sequential affordability and proves it equivalent to the sum bound. The full selector-prefix correspondence is supplied by the event decomposition above; the proof package does not claim an automated refinement of that decomposition or of Python.

Set C₀=kd+c+d and B=c+Ld. The number of affordable, timely opportunities for a first useful candidate is

\[
N(F,H,k)=
\begin{cases}
0,&F<C_0\text{ or }H<k+1,\\
1+\min\!\left(
\left\lfloor\frac{F-C_0}{B}\right\rfloor,
\left\lfloor\frac{H-k-1}{L}\right\rfloor
\right),&\text{otherwise}.
\end{cases}
\tag{3}
\]

The mutually exclusive successful cases are j=0,…,N−1, each with probability (1−q)^j q. Therefore

\[
\boxed{\Pr(\text{recovery}\mid F,H,k,\ m\ne z)
=\sum_{j=0}^{N-1}(1-q)^jq
=1-(1-q)^N.}
\tag{4}
\]

For the primary q=1/2 this is 1−2⁻ᴺ. The N=0 case is exactly zero, including histories that can afford a final assembly but cannot afford its ensuing trial. The cost and opportunity thresholds are sharp for this law: crossing each complete failed-candidate block boundary makes one more distinct successful history possible. A higher initial fuel supply need not change the probability between these thresholds.

For c=1,d=2,L=k=2,H=8, C₀=7 and B=5. Recovery probability is zero when F<7, 1/2 for F=7,…,11, 3/4 for F=12,…,16 and 7/8 for F≥17. The finite opportunity horizon admits only three useful candidate opportunities. Unlimited additional fuel cannot raise this eight-opportunity probability above 7/8 under unbiased assembly.

Equations (2)–(4) are conditional on the **actual inherited** state at the reversal. In a full experiment starting without any selector, both that state and whether a compartment reaches it depend on prior formations and outcomes. An unconditional result must integrate over those histories, including extinction, a selector already appropriate for the new condition, and failed initial assembly. Installing a common favorable F,k at reversal would be a separate intervention; it cannot stand in for the continuing-history experiment.

These results sharpen a resource/lag tradeoff. Once a previously successful selector is renewed to lifetime L, a reversal imposes L unsuccessful trials before this architecture admits a fresh assembly. A longer-lived structure can retain its routing behavior longer while also delaying its replacement. Equation (4) is a recovery result for the specified mechanism, not a lower bound on how quickly every controller can adapt.

## 4. Conventional equivalence and a stronger information use

A conventional finite-state feedback controller can keep `(m,ℓ)`, route b to b XOR m, reset ℓ to L after a real return, decrement it otherwise, and choose a fresh random routing policy at zero. Charge that controller exactly c,d,r, expose it to the same signals and returns, and carry its fuel and source state identically. Its one-step transition probabilities equal those above. Induction then gives equality of the complete path laws and of every observable derived from them.

This is an **exact matched conventional realization**, not an inferior baseline. Calling the material mechanism generative cannot create a performance difference from the same law described as a learning automaton. The contribution here is an explicit connection from costly physical dependence to a changing routing mechanism and its budget limitations. Historical novelty of the mechanism or the elementary probability formula is not claimed.

Ordinary binary win-stay/lose-switch is different. In this noiseless two-policy plant, one observed failure implies that the opposite mapping is productive while the condition remains fixed. A controller that is physically allowed to direct assembly toward that opposite type can use information that random reassembly discards. Even if it waits until the same inherited lifetime expires, it has recovery probability one whenever F≥C₀ and H≥k+1. Under those same conditions the unbiased mechanism with finite N has probability strictly less than one. Earlier permitted dismantling can give directed revision a further advantage, but that intervention changes the actuator/replacement rule and must be declared and charged.

Consequently a fair comparison must either permit directed assembly with the same cost and report its outcome, or state the physical constraint preventing it for both implementations. Random assembly is not the strongest possible conventional feedback mechanism. Equal resources and observations do not entail equal use of information, and neither supports a blanket superiority claim.

## 5. Mechanism identification and failure modes

Two interventions distinguish the proposed physical implementation from a description based only on externally recorded success:

- **Detach selector renewal from captured return while preserving bulk capture.** If selector lifetime then fails to reset, behavior differs even though the observer can record the same productive response. The relevant intermediary is material renewal, not an abstract success label. The total charge and the available update route must be recorded separately.
- **Divert captured energy before it reaches the compartment.** A nominally productive response then cannot be counted as usable return. If renewal receives no fuel, the old selector must wear; a score-based controller that still retains it is implementing a different causal law. Outcome and source conditions alone are insufficient to determine selector retention without this coupling.

These are synthetic discriminating interventions between implementations, not evidence that one implementation exists in an organism. A conventional controller built with the same physical coupling will remain equivalent under the same interventions. Return-blind periodic turnover and permanently fixed mappings are useful ablations, not substitutes for that strongest matched comparison.

The mechanism can fail through insufficient inherited reserve, a horizon shorter than its wear lag, repeated assembly of the obsolete mapping, unavailable local return, frequent condition reversals, or renewal that preserves behavior while reducing organizational reserves. It does not optimize an observer's welfare score. Nor does obtaining private return establish that a routing decision is beneficial to other centers.

## 6. What has changed in the derivation

The previous formation-to-retention study explained differential reconstruction of response types while their selection machinery remained supplied and fixed. Here the selector's **type and response mapping** are actual changing state inside one continuing organization, and return from the selected response causally maintains the selector that produced it. Loss of that return permits paid reconstruction of another mapping. The link is constructive under the listed assumptions and has an exact finite-budget recovery obstruction.

The architecture governing those changes remains fixed. The result supplies an elementary return-sensitive memory and revision process; it does not explain the origin of general representations, novel proposal repertoires, selection among distinct update rules, or the evaluative and social capacities assumed by concern and wisdom models. The next unresolved connection is formation and consequence-dependent retention of **alternative revision mechanisms themselves**, with explicit costs and fair comparison to directed feedback—not merely renaming the same automaton at another level.

The [formal package](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/README.md) distinguishes the checked event ledger and deterministic thresholds from analytical probability, computational checking and empirical evidence. The [review](SELECTOR-REVISION-REVIEW.md) is an internal audit, not independent empirical validation or historical priority certification.
