# The central integrated claim: selection and the reproduction of correction

5 October 2026. Research synthesis for Ren. This document separates the programme's organizing claim from the narrower result established by the accompanying model.

The [general-framework synthesis](general-framework/README.md) now makes the broader scope explicit: financial maintenance is one implementation of the continuation and revision of practices and their conditions. The financial thresholds below remain results about this specialization.

The [constitutional extension](constitutional-extension/README.md) now adds paid access verification and custodians who can claim maintenance payments without doing the work. The original two-state result below is preserved; the extension's proved scope and remaining boundary are recorded in the completeness assessment near the end.

## The organizing claim

**When a system's capacity to detect and enact useful revisions depends on institutions altered by selection, selection also changes the conditions for future correction. Durable correction therefore depends on reproducing those conditions through the system's own operation, or explicitly supplying what it cannot reproduce.**

This identifies a recursive relationship: a system selects practices; those practices maintain or erode the information, implementation capacity and resources through which subsequent selection can respond to the world. The proposed object of study is this coupled process.

That statement is an organizing claim, not a newly proved universal law. Its value depends on specifying mechanisms that distinguish continuation from failure, and then testing those distinctions. The accompanying construction supplies one such mechanism. It does not need the environment to optimize a uniform objective or every system to implement backpropagation.

The more ambitious programme includes legitimate authority, contestable evaluations, changing representations and shared ecological support. This model closes a smaller loop: paid contextual information and implementation capacity produce an output benefit; that output finances capacity replacement; observable net returns determine whether the funding practice spreads or disappears.

## The established conditional result

Consider a repeated local task with two equally likely contexts. An uninformed response has expected output \(y_0\). A noisy signal can improve the response, but only if both the evidence channel and the implementation channel work. A paid stock \(C\) supports that paired service, with joint availability

\[
q(C)=\left(\frac{C}{K+C}\right)^2.
\]

Here \(K\) is a capacity scale. The task-derived potential improvement is \(B\), of which a fraction \(\chi\) is privately recoverable by the service user. Any remaining benefit is a common spillover. The binary task entails \(0<\chi B\le B\le y_0\).

Let \(x\) be the share using and funding the service. These users pay fraction \(\tau\) of their direct receipts into upkeep. Nonusers retain baseline production and receive common spillovers, but do not receive the direct service. Capacity converts actual payments into renewal at rate \(\eta\) and depreciates at rate \(\mu\). Practices spread through copying of their measured net returns, with responsiveness \(\kappa\).

The resulting equations are

\[
\dot x=\kappa x(1-x)
\left[(1-\tau)\chi Bq(C)-\tau y_0\right],
\]

\[
\dot C=\eta\tau x[y_0+\chi Bq(C)]-\mu C.
\]

Payments are deducted from the very output that supplies them. There is no extra reward for being designated corrective, no permanent external correction budget, and no foresight about future institutional survival in the copying rule. Service access and the execution of the funding commitment are explicitly fixed assumptions.

**Theorem for this construction.** Some constant financing fraction supports a locally stable, fully participating, self-funded regime that resists invasion by the represented nonfunding practice if and only if

\[
\boxed{\eta\chi B>4\mu K.}
\]

When the inequality holds, a calculable open interval of fees satisfies both selection and financing. Fees below that interval fail to maintain enough useful capacity; fees above it leave too little net advantage to sustain participation. A stable depleted state coexists with the functioning state. Explicit regions leading to each are proved under the same parameters.

Strictly below the threshold, the service is eventually lost from every initial condition containing some nonfunders, however large its initial stock. Above the threshold, changing a fee to a feasible value does not guarantee recovery from depletion. A sufficiently large, finite capacity investment can enable recovery if some funding practice remains; the construction gives a conservative bound on that investment and subsequent adoption proceeds by the original equation. No finite capacity injection creates users when the copying population contains none.

These are theorems about the declared equations. Loss means loss of the additional correction service; baseline production continues. The equality threshold and fee endpoints are excluded from the strict stability claims.

## What the threshold means

At a fully participating stationary state, spending on upkeep exactly replaces depreciation. The funding practice's relative net advantage is therefore

\[
\underbrace{\chi Bq(C)}_{\text{recoverable benefit from correction}}
-
\underbrace{\frac{\mu C}{\eta}}_{\text{cost of replacing its capacity}}.
\]

For this paired-channel technology,

\[
\max_{C>0}\frac{q(C)}C=\frac1{4K},
\]

which explains the exact threshold. The number four comes from this particular response curve. It has no claimed universal significance. The structural comparison is between recoverable benefit and the actual replacement cost of the machinery producing it.

Useful correction, affordability and selection resistance are distinct. A service can produce a real common benefit and still disappear if the represented funding mechanism fails to return enough of that benefit to its maintainers. If nonpayers receive the same direct service without paying, their advantage defeats the funding practice in this model. Other mechanisms—collective commitment, public funding, other selection levels or different access rules—require their own accounting and authority assumptions; this result is not an argument that privatization is universally necessary.

## What this adds to the existing work

Earlier modules already established conditional links among captured authority, harmful selection, shared support and finite funded intervention. Other modules made renewal depend on paid capacity or examined the transmission of maintenance practices. The added result links three things within one dynamical system: **a specified informative response, the production that pays for its continued availability, and selection of the practice making those payments.**

The additional explanatory content is that current output can conceal the direction of institutional renewal. In an exploratory comparison, two states have exactly the same current gross output, 1.1 units. The state with fewer funders has more installed capacity and retains more output immediately, yet loses its service; the state with more funders starts with less capacity and rebuilds a functioning service. Both trajectories enter the corresponding proved attraction regions. This is a model illustration, not an empirical prediction already confirmed. Details and current expenditure are disclosed in [the results](RESULTS.md).

The correction interpretation also produces an intermediate diagnostic: improving evidence can improve proposed responses without improving realized output when implementation is blocked. Restoring implementation alone does not make an uninformed proposal better. Recording both stages is necessary: output and stock trajectories alone could equally describe an ordinary productive club.

## Implications for the alignment programme

The design question suggested by this result is: **does the process selecting behavior also maintain the means to discover and enact its corrections?** An alignment proposal that relies on evaluation, oversight or contestability should specify who supplies these functions, what pays for their reproduction, what happens when they become costly to retain, and whether they can be restored after depletion.

This is a proposed application of the mechanism, not a demonstrated account of AI training or human political systems. The scalar output in the model is a local production and financing variable. It is not a universal welfare function. Preserving the service could help a legitimate task or an objectionable one; legitimacy and plural human interests require additional judgments and constraints.

The situated aspect is essential. An adequate response is defined relative to a declared context and task. The signal is noisy, but its meaning and the available response family are fixed. Open-ended reframing, exclusion of inconvenient evidence, disagreement about ends and discovery of previously unrepresented hazards are not established by solving this binary task.

Similarly, the two attractors here concern a specific service. They neither prove a universal meta-attractor nor identify cancer dynamics or inevitable domination. The useful connection is methodological: distinguish the state of a system from the capacities and transition mechanisms that allow its future states to change.

## What remains unestablished

| Object | Status after this work |
|---|---|
| Useful response to a specified hidden context | Derived from a noisy finite task |
| Funding and renewal of the paired service | Endogenous, with explicit output accounting |
| Selection of the funding practice | Endogenous within two represented alternatives |
| Persistence, depletion and finite initiation | Conditional proofs and numerical illustrations |
| Access verification and delivery of its maintenance | Fixed in the baseline; the extension makes them endogenous against unpaid-access and false-completion practices |
| Survival of settlement, authentic evidence and peer assignment | Still assumed; broader capture and hybrid strategies remain unproved |
| Endogenous interpretation and changing model classes | Not included |
| Plural legitimacy, political opposition and arbitrary successors | Not included |
| Shared ecological support and unknown external hazards | Not included in this minimal model |
| Novelty and empirical predictive advantage | Not established |

The [constitutional extension](constitutional-extension/model/CONSTRUCTION.md) introduces two concrete failures of the enabling arrangement: unpaid access through false credentials and maintenance contracts claimed without delivery. Verification is paid from actual fees, depreciates, and depends on the selected prevalence of the genuine maintenance and truthful reporting practice. It proves separate user and custodian incentive conditions, an exact design threshold, and both recovery and operating-loss results. It therefore addresses a defined part of the previously fixed access and integrity boundary.

The remaining question is survival against changes to the settlement and evidence mechanisms themselves. Authentic successful checks must still control deferred payment, peer assignment must follow the stipulated process, and genuine maintenance is bundled with truthful reporting. A hybrid that performs maintenance while corrupting peer reports, manipulation of assignment or capture of settlement requires an enlarged strategy set. The current result does not establish arbitrary constitutional survival or political legitimacy.

## Scientific standing

There is close prior work. Andrews and colleagues already combine cultural selection, resource governance and costly institutional monitoring in [*The cultural evolution of collective property rights for sustainable resource governance*](https://www.nature.com/articles/s41893-024-01290-1). Lee and colleagues model costly vigilance and corruptible enforcement in [*Social evolution leads to persistent corruption*](https://www.pnas.org/doi/10.1073/pnas.1900078116). Lerch and colleagues derive context-dependent conditions for maintained costly production in [*How public can public goods be?*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010666).

The present work establishes a transparent conditional synthesis within this project. It is not evidence of being the best model in science or the first endogenous institution model. Its broader significance will depend on whether the distinction among evidence, implementation, financing and practice selection yields reliable predictions or interventions beyond those neighboring approaches. The proofs and AI-agent audits justify the bounded result; they do not substitute for that comparison or external validation.
