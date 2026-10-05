# Integration review: paid verification, custodians and conditional payment

5 October 2026. Internal AI mechanism and accounting review. This memo assesses a bounded extension of the funded-correction model. It is not empirical validation or an originality claim. The coordinating agent implements verification; the mathematical lead supplies the final construction and proofs.

## Which remaining assumption is being addressed

The previous model selected and financed participation in a corrective service, but excluded nonpayers from its private benefits and executed its fee allocation by assumption. The extension admits two additional failure routes: users can forge access credentials, and custodians can divert the budget intended to maintain verification. Verification capacity is paid from the same real output as the productive correction service, deteriorates, and cannot be supplied for free when the institution weakens.

The extension does not explain every primitive that supports a constitution. It studies whether a population of potentially dishonest custodians can remain sufficiently honest and funded under a specified payment-and-audit architecture. In particular, conditional payment execution and the authenticity of a verified audit receipt remain trusted primitives. Those must be named rather than hidden in a generic word such as authority.

## Actors, stocks and returns

There are two populations with separate roles. Users choose whether to pay the service fee. Custodians choose whether to deliver the maintenance their contract specifies. Neither population's payoff silently includes an additional strategic income from controlling the other role. If users and custodians form coalitions, own one another, or jointly choose policies, a different return model is necessary.

Let x∈[0,1] be the fee-paying user share and h∈[0,1] the honest custodian share. Productive correction capacity is C≥0; verification capacity is G≥0. The prior noisy binary task still supplies baseline output y₀ and a potential incremental output B, with 0<B≤y₀. A privately recoverable fraction χ gives A=χB. Write

q(C)=[C/(K+C)]²,

p(G)=G/(L+G),

D(h,G)=h p(G).

D is the probability of an effective verification: the operation must function and the sampled peer must report honestly. Dishonest peers collude rather than becoming an external source of reliable oversight. The probability therefore falls with either verification-stock loss or guardian corruption.

A paying user receives direct gross receipts r(C)=y₀+Aq(C) and pays fraction τ. A nonpayer attempts to obtain service with forged credentials. If effective verification blocks that attempt, it receives baseline output; otherwise it obtains the same direct service. Forgery has no extra cost in this conservative threat model. A nonpayer consequently does at least as well as an uninformed nonparticipant, so adding that baseline option does not create the earlier costly-forgery outside-option problem.

The fraction actually served is

Z=x+(1−x)(1−D).

Common spillovers are S=(1−χ)Bq(C)Z. User returns are

U_P=(1−τ)r(C)+S,

U_F=y₀+(1−D)Aq(C)+S.

Their difference is derived from actual access and payments:

s_P=D A q(C)−τr(C).

Gross user output is Y=y₀+Bq(C)Z. The fee flow actually collected is F=τx r(C), and user consumption satisfies

xU_P+(1−x)U_F=Y−F.

The public spillover must include the output of successfully served nonpayers. Using the previous expression with x alone would omit real output in this extension, even though a common omitted term might accidentally cancel in the selection equation.

## Custodian contracts and the full budget

Fraction λ∈(0,1) of the collected flow finances C. The remaining verification-contract flow is

V=(1−λ)F.

An honest custodian commits fraction m∈(0,1) of its contract to actual maintenance and keeps the remainder as compensation. A fraudulent custodian attempts to provide no maintenance and retain the whole contract. The contract is released conditionally after verification. If fraud is detected, its entire unpaid tranche remains in an inert segregated reserve Q. The model does not recover money already consumed by the fraudster or create fine revenue.

Per unit of aggregate verification-contract flow, the four disjoint uses are:

| Use | Flow |
|---|---:|
| Delivered verification maintenance | m h V |
| Honest custodians' compensation | (1−m)hV |
| Undetected fraudulent consumption | (1−h)(1−D)V |
| Detected tranche retained in reserve | (1−h)DV |

Their sum is V. Thus

λF + m hV + (1−m)hV + (1−h)(1−D)V + Qdot = F,

where Qdot=(1−h)DV. Adding user consumption restores exactly Y. The reserve is not used to replenish C or G, pay a reward or subsidize recovery. Its balance is a record of withheld resources; none of the stability claims can silently use it again.

Under a normalization with one aggregate unit of custodians, expected honest and fraudulent compensation is respectively (1−m)V and (1−D)V. Their difference is

s_H=V(D−m).

If another fixed custodian-population size is used, divide both returns by that size and absorb it into the imitation coefficient. A changing custodian population needs its own dynamics.

The selected maintenance and funding dynamics are therefore

xdot=κx(1−x)[D A q(C)−τr(C)],

hdot=νh(1−h)V[D−m],

Cdot=η_C λF−μ_C C,

Gdot=η_G m hV−μ_G G,

Qdot=(1−h)DV.

Both productive and verification maintenance consume funds already subtracted from user receipts. There is no externally supplied policing budget, arbitrary alignment bonus, unlimited penalty or penalty financed by the victim's future production.

## What a conditional-payment primitive must mean

The transaction must distinguish a delivered maintenance commitment from a fabricated claim before releasing funds. An operational interpretation is a task-specific escrow contract: an honest claimant commits part of the tranche to verifiable maintenance delivery; the remaining part becomes compensation. A fraudster seeks release with fabricated delivery evidence. Functioning verification plus an honest sampled peer exposes that fabrication.

This interpretation carries substantive restrictions:

1. The conditional-release mechanism itself cannot be seized or bypassed within this threat class. Otherwise detected fraud would still collect, changing s_H.
2. Genuine evidence of fraud can be authenticated; dishonest peers cannot generate a valid false accusation against an honest custodian. A model of ambiguous or corruptible adjudication would need false-positive and contested-appeal dynamics.
3. Audit assignment cannot be controlled by the subject or flooded with costless new identities. The endogenous honest fraction determines peer quality under the stated assignment process.
4. The production and depreciation parameters for G include the resources required for both access checks and custodian audits at the declared workloads. Using one G for two tasks does not mean one check is performed twice without cost. Variable workloads or competition for inspection capacity would require explicit allocation.
5. The positive construction assumes a coordinated or atomic delivery-and-payment arrangement: the assigned budget can finance genuinely delivered maintenance without requiring an unmodeled advance from the honest contractor. Ordinary escrow alone does not provide that working capital, and a verified promise is not delivered maintenance. If an implementation instead requires advance finance, collateral or delayed settlement, its costs and feasibility must be modeled and may block initiation.

These primitives prevent an infinite verbal chain of ever-higher monitors by defining a bounded model with a specified transaction kernel and a revisable set of attacks. They do not establish that every actual institution possesses an incorruptible kernel. The honest auditors are endogenous members of the same custodian population; the trusted execution rule is the remaining boundary.

## A rigorous insider attack when recourse is removed

An informative negative control preserves verification funding and user audits but disables the detection or consequence of custodian fraud. Honest workers then receive (1−m)V while fraudulent workers keep V. The guardian dynamics become

hdot=−νmV h(1−h).

Suppose 0≤h₀<1; at least some fraud is possible initially. For h₀=0, delivered maintenance is zero and G simply decays. For 0<h₀<1,

d/dt log(1−h)=νmVh.

Since log(1−h)≤0, integration yields

∫₀^∞ h(t)V(t)dt ≤ −log(1−h₀)/(νm) < ∞.

Hence the total input into G is finite. The linear depreciation equation implies G(t)→0. This conclusion does not require h to approach zero: paid activity itself can vanish first, leaving a nonzero honest fraction of a failing institution.

Because D≤p(G)→0 and q≤1, the user advantage eventually obeys

s_P=D A q−τr ≤−τy₀/2<0.

For every initial x₀<1, the log-odds identity or the x=0 boundary then gives x→0. Consequently F→0 and C→0. Thus the institution's paid user-level enforcement can collapse because selection favors the custodians who divert its maintenance budget. Funds and verification are not enough when a different selection process rewards disabling their renewal.

The exceptions are explicit: if h₀=1, purely imitative dynamics cannot introduce a missing fraudulent practice; if x₀=1, they cannot introduce a missing nonpayer. A deterministic boundary's persistence should never be advertised as resistance to those invaders. Finite populations, mutation and entry would require additional analysis.

## What would make the positive construction substantive

A successful positive result must show that paid, effective verification can make honest delivery relatively rewarding **and** keep paying users relatively willing to fund it, while maintaining both C and G from actual receipts. The relevant inequalities are separate: user participation needs D A q>τr; honest guardians need D>m; both stocks need funded replacement. A region satisfying all of them is more informative than a favorable equilibrium or a positive private return alone.

The model should also retain failed states under the same technologies and funding rules. Depleted G or a low honest share can make custodians' fraud profitable, further weaken verification and remove the reason for users to pay. More inherited C alone need not restore the missing guardian incentives. This creates a testable distinction between supplying a useful service and maintaining the arrangement that makes its continued financing possible.

The extension can therefore establish a conditional layer of constitutional maintenance: endogenous participation, paid verification, selected custodian honesty and explicit theft all appear in one budgeted process. It cannot by itself establish resistance to forged adjudication, capture of the payment mechanism, arbitrary coalitions, unrestricted constitutional changes or disagreement about what ought to count as correction.

## Implementation review and the high-maintenance counterexample

I read the completed mathematical construction and the root `verify_extension.py`, including its saved numerical outputs. The equations, user served-fraction account, contractor accounts and the no-withholding intervention agree. Under no withholding, user credential checks remain active, but the contract uses zero effective detection for compensation and the reserve receives no money. This is the intended separation of evidence from an enforceable payment consequence.

The implementation uses log odds for both practice populations and logarithms for both positive capacities. Its saved log states preserve rare practices when displayed shares round to one. The full reference equilibrium is x=h=1 and C=G=3; both selection margins and all four linearized eigenvalues match the canonical witness.

The m=.9 counterexample is stronger than a local-instability calculation alone. Starting with C≤3 and G≤5.4, those upper bounds are invariant: their funding cannot exceed the x=h=1 benchmark with the same parameters. Effective detection is therefore at most p(5.4)=.84375<m=.9 throughout the trajectory. Honest maintenance has a uniformly negative return gap per unit verifier budget. Integrating its decline bounds total delivered maintenance, so G vanishes, and then x and C vanish whenever bypass was initially present. An initially favorable payer margin does not supply the missing custodian margin.

This conclusion concerns functioning capacity and participation. It should not be stated as elimination of every honest contractor. The saved m=.9 path has an extremely small but positive honest share; other failing paths retain large honest shares, including approximately .918 after starting with depleted productive capacity. Once fee revenue vanishes, replacement of custodian practices also slows. The graph's payer-benefit label refers to the initial condition, since the payer advantage reverses later.
