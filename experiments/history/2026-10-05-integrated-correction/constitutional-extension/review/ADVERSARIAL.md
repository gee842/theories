# Adversarial review of paid verification and custodian integrity

5 October 2026. This review examines whether the constitutional extension adds an actual threat to the funding arrangement, pays for its response, and permits the people maintaining that response to become corrupt. It is an AI-agent review of a conditional model, not independent human peer review or evidence that the mechanism works in an existing institution.

## Criteria for the extension

The original model stipulated that nonpayers could not receive the direct service. Giving an effectiveness coefficient its own differential equation would not by itself explain that restriction. The extension needs an alternative that obtains unpaid access when protection fails, funding that actually pays for protection, and a failure mode among those entrusted with protection. A finite threat class is sufficient if its boundary is explicit.

The proposed extension meets that design requirement. It includes payoff-selected nonpayers who attempt unpaid access, a depreciating verifier stock, and payoff-selected custodians who can claim compensation without doing the required work. Successful protection is conditional on paid verification and a sufficiently maintained honest fraction, rather than a permanent honest enforcer.

The model still needs a physical or procedural basis for acting on verified evidence. Making every substrate defeasible without specifying any feasible action would prevent a constructive result. The appropriate boundary is therefore an explicit payment and verification primitive, not a claim to have explained all possible forms of authority.

## Two repairs made during review

The first proposal contrasted paying users with forgers who incurred a fixed attempt cost. That could misleadingly favor payment by excluding the ordinary no-service option. The final default uses costless bypass: a nonpayer weakly outperforms an uninformed nonparticipant. Thus the omitted no-service option cannot defeat an otherwise selected payment practice. Extensions with positive bypass costs must compare against both alternatives.

A second early possibility paid verifier wages but assumed their work was delivered. Payment alone does not establish honesty. The selected repair introduces honest and fraudulent work practices, pays them according to specified verification outcomes, and lets their relative returns determine which practice spreads. The funding mechanism can therefore fail through its own custodians.

## Exact resource accounting

Let the payer fraction be \(x\), the honest custodian fraction \(h\), service capacity \(C\), and verification capacity \(G\). The direct service receipt is \(r(C)=y_0+Aq(C)\), where \(A=\chi B\). Fees are \(F=\tau xr(C)\). Fraction \(\lambda F\) buys service replacement, leaving verifier budget \(V=(1-\lambda)F\).

An honest custodian delivers work costing \(mV\) per unit custodian population and keeps \((1-m)V\). A fraudulent custodian does no work, claims the allocation, and receives it only if undetected. The chance of an effective check is \(D=hp(G)\): it requires an honest assigned peer and functioning verification infrastructure. Detected fraudulent allocations remain in an inert reserve \(Q\), with no automatic repair or rescue use.

The verifier budget is exhausted exactly by

\[
\underbrace{mhV}_{\text{delivered verifier work}}
+\underbrace{(1-m)hV}_{\text{honest retained receipts}}
+\underbrace{(1-h)(1-D)V}_{\text{undetected fraudulent receipts}}
+\underbrace{(1-h)DV}_{\text{withheld reserve}}
=V.
\]

Nothing is financed by an imaginary fine, assumed recovery of money already stolen, or a second use of the same fee. The honest work requirement and conversion coefficient must include the work needed for both user checking and custodian checking. A different inspection workload would change the capacity-production relation.

Payment decisions occur before release from escrow. If payments had already been irrevocably transferred, the reserve term would require an additional collection mechanism and could not simply be credited. Likewise, deferred payment can require working capital for actual installations; instantaneous conversion and liquidity are model premises rather than a financial engineering result.

User and custodian selection concern separate normalized role populations. If the same individuals hold both roles and their incomes covary with payer status, those combined incomes could alter the user-selection equation. That alternative is not silently covered by the present equations.

## The new threats have actual incentives

A nonpayer receives the useful service when checking fails. Its advantage over payment is positive when saving the fee outweighs the additional benefit secured by paid access. This makes unpaid access a genuine selective threat rather than an externally imposed disturbance.

Custodian honesty has private advantage

\[
U_H-U_F=V[(1-m)-(1-D)]=V(D-m).
\]

Honesty is therefore selected against when verification is too weak. There is no preference for being honest in the payoff rule. Dishonest peers who approve fraud are represented by the factor \(h\): their presence lowers both user protection and the chance of detecting custodian fraud.

The remaining assumption is that peer assignment actually samples the population rather than allowing a claimant to select a friendly auditor. Strategic matching, bribery that changes an assigned honest peer's decision, forged audit evidence, or direct compromise of escrow require additional mechanisms. The model covers its stated approval and work-omission threats; it does not prove resistance to all collusion.

There is also a restriction on the practice repertoire. The variable h bundles genuine maintenance delivery and truthful peer reporting in one practice; the opposing practice omits maintenance and approves fraud. A contractor that delivers maintenance but falsifies another contractor's audit is a possible hybrid outside this binary repertoire. The result derives selection between the stated composite practices, not a separate incentive theorem for every component of truthful auditing. This restriction matters when interpreting the phrase “no permanently honest guardian.”

## Proof obligations and failure interpretation

A successful theorem must show both a positive funded regime and a parameter or state region in which bypass or custodian fraud is favored. A local high-functioning equilibrium is useful, but must not be presented as a global recovery guarantee. An invariant region must protect both physical stocks and both practice shares under the same budget allocation.

There is a particularly important failure distinction. Custodian updating is proportional to \(V\). If funding stops, selection among custodians can stop before every honest practice disappears. With \(0<h_0<m\), the comparison

\[
-\dot h\ge\nu(1-h_0)(m-h_0)hV
\]

bounds cumulative paid honest work. It can force verification and service capacity to disappear even though the eventual honest fraction remains positive. Fractions of latent practices do not establish operating capacity. The final report should describe loss of the institution's function, not necessarily universal corruption or societal extinction.

## Primary comparisons

[Sigmund, De Silva, Traulsen and Hauert, Social learning promotes institutions for governing the commons](https://www.nature.com/articles/nature09203), published 14 July 2010, compares advance-funded pool punishment with peer punishment and explains the importance of second-order free riders. The publisher abstract was read directly. Paying for protection and selecting against practices that refuse its costs are established research questions, not a new discovery of this extension.

[Lee, Iwasa, Dieckmann and Sigmund, Social evolution leads to persistent corruption](https://www.pnas.org/doi/10.1073/pnas.1900078116), published 13 June 2019, explicitly models paid information, honest and corrupt umpires, and selection through economic returns. The full publisher article was read in the preceding review. It is a close predecessor for the proposition that maintaining trust in those enforcing rules itself requires costly effort and can produce recurring corruption.

[Andrews and colleagues, The cultural evolution of collective property rights for sustainable resource governance](https://pure.mpg.de/rest/items/item_3571303_1/component/file_3571304/content), published 19 February 2024, already combines paid monitoring, access and use rules, resource dynamics, and cultural selection. The open primary manuscript was read directly. The present extension adds a specific escrow and peer-checking mechanism to this project's prior service model; its wider originality has not been established.

## Completed proof and implementation audit

I read the completed mathematical construction, mechanism review, implementation and saved verification results. The following claims are valid within their stated domains:

| Claim | Audit judgment |
|---|---|
| Full paying and genuine-maintenance regime | The unique positive service-capacity root follows from the task-derived bound A≤y₀. Both strict invasion inequalities are independently necessary for negative invasion exponents, and together sufficient for local asymptotic stability of the four operating variables. |
| Exact co-design threshold | Minimizing replacement cost divided by privately secured output gives the stated threshold. The cubic condition and the active honesty floor are correct. The strict inequality excludes a boundary design with zero custodian advantage; the theorem does not assert that imitation discovers the financing design. |
| Protected recovery region | The lower faces point inward and both practice shares have strictly positive logistic comparison rates. Their convergence, the unique service-capacity root and the linear verifier equation justify convergence of all four operating variables. |
| Low-service loss basin | The upper service and payer faces point inward independently of h and G. Payer decline makes fee revenue integrable; both stocks then vanish. This is distinct from a corruption-triggered loss. |
| h₀<m loss | The comparison bounds the integral of actual delivered verifier work. Depreciation then removes G, which makes bypass favorable and removes x and C whenever x₀<1. A high residual honest fraction does not contradict failure. |
| No executable withholding | The log(1−h) identity bounds the same cumulative delivered work for h₀<1. Keeping access checks temporarily available cannot reverse this result. The x₀=1 and h₀=1 no-entry boundaries are correctly excluded where needed. |

The finite-capacity statement covers all finite initial stocks and a finite number of finite stock injections, or more generally finite total external capacity input. Indefinite external replenishment is a different system. It can directly prevent an externally replenished stock from vanishing and must not be treated as covered by the closed-system proof.

Reserve Q is an inert ledger coordinate. A point in the full five-dimensional state including Q is not locally asymptotically stable: changing its initial reserve leaves that difference unchanged. The claimed attractor and eigenvalue test concern the four operating variables. At the operating equilibrium there is a family of reserve balances, not an attracting unique reserve balance.

The implementation correctly keeps access checking active when only withholding is disabled. It removes the payment consequence in custodian returns and sends no money to the reserve in that control. Log odds retain rare practices even when displayed shares round to one. The analytic Jacobian matches the implemented equations.

The saved record reports 600 allocation checks, 300 Jacobian comparisons and 160 constrained design comparisons, including 70 designs with an active honesty constraint. I verified that its recorded source hash matches the reviewed implementation. The saved design discrepancies have maximum relative error about 1.25×10⁻¹⁵. These computations support implementation consistency; they do not substitute for the symbolic proof.

As an additional independent execution, I recomputed the reference equilibrium and integrated the exact recovery initial condition printed in the mathematical note, (x,h,C,G)=(.92,.92,2.6,2.2). It stays within the certified box and approaches (1,1,3,3). The reference user and custodian return margins are .12 and .0271875; the four eigenvalues are approximately −.12, −.271875, −.844828 and −1. The result is stable with both opposing practices initially present, not just at an artificially invariant pure boundary.

The m=.9 example shows a positive payer margin alongside a negative custodian margin. Its reported declining trajectory is consistent with this diagnosis. A claim about all initial conditions would require a separate global argument; local instability by itself would not supply one.

## Final scope judgment

The extension adds meaningful endogenous failure and maintenance of the previously assumed access boundary. It also puts custodian work under selective pressure. These are substantive additions rather than a relabeling of a fixed effective authority.

The payment primitive still requires authenticated verifiable outcomes, controlled disbursement, coordinated delivery and payment, and the specified peer-assignment procedure. The practice repertoire also bundles delivered work with truthful peer reporting. Those are remaining physical, procedural and behavioral assumptions. A result conditioned on them establishes survival against the admitted bypass and custodian-fraud practices. It cannot establish political legitimacy, arbitrary constitutional reform, or protection against actors able to alter that primitive itself.

No blocking mathematical or implementation issue remains in the reviewed conditional result. It is a substantive extension of this project's previous theorem: a previously fixed access boundary now requires paid capacity and a selected maintenance practice, and those dependencies generate additional failure and recovery conditions. The strongest new lesson within the construction is that supplying more useful or verification equipment can fail when the practice maintaining accountable verification has the wrong incentive. That lesson is demonstrated under an explicit contract, not established as a universal law of societies or a general solution to AI alignment. The surrounding literature already studies costly enforcement, institutional selection and corruptible enforcers; this audit establishes internal validity, not priority or foundational novelty.
