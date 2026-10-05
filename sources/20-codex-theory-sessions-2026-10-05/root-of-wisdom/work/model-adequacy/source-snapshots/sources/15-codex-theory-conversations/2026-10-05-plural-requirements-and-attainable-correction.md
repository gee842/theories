# Plural requirements and attainable correction

Research continuation, 5 October 2026, Asia/Bangkok. AI-generated research assistance under Ren's direction, with mathematical, implementation, and primary-literature audits by three returning agents. Ren accepted the target of distinguishing incompatible requirements, unavailable correction, and institutionally blocked correction, then requested: “Yes, totally agree. please continue”. This is a research snapshot, not a verbatim conversation or empirical validation.

The central advance is a precise question that does not require a common utility: **does one executable policy meet all the stated requirements together?** This question differs from whether each requirement can be met separately, whether a controller prefers the policy, and whether affected people will continue accepting it. The calculation below answers the first question in a supplied finite system and exposes the limits of that answer.

It builds on [recoverable inquiry](2026-10-05-recoverable-inquiry.md), retaining its production, evidence, cash, rebuilding and repair dynamics. The previous scalar objective is removed. We keep a vector of consequences and provide either a policy satisfying the declared bounds or a numerical certificate that none can do so within the specified policy class.

## Joint feasibility without a common score

Let \(\Pi_\Gamma\) be the observation-based policies permitted by physical resources, available information, timing, and a declared authority rule \(\Gamma\). For policy \(\pi\), write

\[
L(\pi)=(L_1(\pi),\ldots,L_m(\pi)),
\qquad
\mathcal C_\Gamma=\{L(\pi):\pi\in\Pi_\Gamma\}.
\]

Each coordinate records an explicitly defined expected consequence. Different parties can impose bounds \(L_i\le b_i\), without supplying exchange rates between their requirements. Joint feasibility is

\[
\mathcal C_\Gamma\cap\{z:z_i\le b_i\text{ for every }i\}\ne\varnothing.
\]

With finite horizon, finite action and observation alphabets, and admissible ex ante lotteries over deterministic policies, \(\mathcal C_\Gamma\) is a compact convex polytope. Standard separation gives an exact alternative:

\[
\exists\pi\in\Pi_\Gamma:\ L(\pi)\le b
\quad\Longleftrightarrow\quad
\min_{\pi\in\Pi_\Gamma}w\cdot L(\pi)\le w\cdot b
\quad\text{for every }w\ge0.
\]

If joint feasibility fails, some nonnegative weight vector proves it: every available policy has weighted consequence above the weighted requested bound. The weights serve as a **certificate of incompatibility**. They do not become a common preference or determine whose requirement should change. This is established constrained-control and convex-feasibility mathematics; [Etessami and colleagues (2008)](https://arxiv.org/abs/0810.5728) provide a particularly close treatment of attainable probabilities and multiobjective strategy construction.

A certificate also gives a necessary lower bound on concessions. If every policy obeys \(w\cdot L\ge M>w\cdot b\), any nonnegative relaxation \(\Delta\) of the bounds must satisfy

\[
w\cdot\Delta\ge M-w\cdot b.
\]

This does not authorize concessions, and satisfying this one inequality is not generally sufficient. The obstruction could instead be changed by new information, resources, technology or permissions.

The convex geometry can even accommodate different declared beliefs. For each deterministic common policy, each participant may evaluate their coordinate under their own specified model or prior. A common ex ante lottery still averages those vectors linearly, provided the randomizer is independent of the exogenous state under each model and the policy has one shared meaning on all relevant observation histories. The theorem therefore does not intrinsically require one common world model. **The implemented occupancy calculation below does use one common known model.** Independently optimizing a different policy for each belief would not establish the existence of a common policy.

## Separate and pairwise success can conceal joint failure

Consider three available policies with loss vectors

\[
(1,0,0),\quad(0,1,0),\quad(0,0,1).
\]

Require every coordinate to be at most .3. Each individual requirement is satisfiable. Every pair is satisfiable: put the loss on the omitted coordinate. Yet every lottery has total loss one, while the three bounds allow a total of only .9. The equal-weight certificate proves joint infeasibility, with normalized violation at least \(1/30\).

This illustrates the difference between “for each party, there exists a policy” and “there exists one policy for every party”. Even pairwise agreement need not establish a common arrangement. Positive slack computed from different policies cannot be combined as if it belonged to one policy. Positive slack in every coordinate of the **same** policy would, of course, establish feasibility.

Expectations introduce a separate issue. A fair lottery over \((0,2)\) and \((2,0)\) meets expected bounds \((1,1)\), but neither realization meets both bounds. If the requirement protects each realized person or history, this expected-vector calculation answers the wrong question. Rights restricting randomization or realized harm must constrain the policy class or outcome events themselves. Their validity cannot be inferred from an attractive average.

## A diagnostic right changes what can be jointly achieved

The experiment reuses the preceding model's full physical and observation chronology. We evaluate three coordinates:

- \(F\): probability of productive stock reaching its absorbing failure state by the horizon;
- \(H\): expected target-absent repair count plus .05 per paid test;
- \(C\): expected expenditure minus actual earned output.

The former terminal stock salvage value and collapse penalty are absent. There is no overall weighted objective. Illustrative constituencies might require reliable service, limited exposure to interventions, and adequate net resources. These are **aggregate requirements, not three represented populations**. The model does not allocate individual injuries or ownership of output. Moreover, \(H\) contains an explicit internal weighting, and repair can restore stock even when its fault target is absent. Removing one common score does not remove all evaluative choices.

A one-period instance permits a direct calculation. Start with stock one, cash eight, ready diagnostics, and fault probability one-half. Pay upkeep and test; repair only after a positive test. The existing noisy diagnostic and stock dynamics give

\[
(F,H,C)=(.085,.10,.04).
\]

Thus one deterministic contingent policy meets requirements

\[
F\le .10,\qquad H\le .10,\qquad C\le .05.
\]

If paid diagnosis is unavailable, every policy satisfies

\[
F+.9H=.45.
\]

Indeed, with randomized repair probability \(r\), failure is \(.45(1-r)\) and target-absent burden is \(.5r\). The first two requirements would instead imply \(F+.9H\le .19\), an impossibility. This is a checkable certificate; it does not depend on a solver's failure status or on choosing a social exchange rate. Paid diagnosis distinguishes cases before the consequential response, permitting the requirements to be met together.

Authorization timing matters. A rule allowing repair only when fault probability is at least .75 permits this policy if applied **after** the diagnostic: a positive result raises the posterior to .9. Applying the same threshold to the **opening** belief .5 blocks every repair prescription in this one-period instance. The measured consequences differ even though the numerical threshold is identical. A post-test threshold .95 also blocks every repair here. These are supplied permission rules; the model does not establish which is legitimate.

The six-period calculation starts with healthy stock three and retains changing hidden faults, passive production evidence, paid rebuilding and prefix cash constraints. Requirements \((F,H,C)\le(.02,.02,-30)\) are jointly feasible with diagnostic access. One witness has approximately

\[
(F,H,C)=(.018233,.018233,-30.017674).
\]

Without paid diagnosis the same requirements are infeasible. Loosening the burden bound to .03 makes them feasible in both modes. Tightening the failure bound to .01 while keeping burden .02 and net expense −30 is infeasible even with full diagnostic access. The result distinguishes conditional incompatibility from compatibility lost under a particular restriction. It does not say that access always resolves the conflict.

## One missing condition can hide the value of another

Resource and authority changes need not have separately visible benefits. In the same one-period example, begin with cash two and no repair permission. Granting permission alone cannot fund the three-unit repair or the three-unit diagnostic-with-upkeep. Increasing cash to eight while keeping repair prohibited cannot avert the .45 failure probability. Doing both permits the policy with failure .085, burden .10 and net expense .04.

Both changes are necessary in this constructed comparison. It follows that an ineffective isolated intervention need not identify an irrelevant capacity. Funding, actionable information, permission and timing can be complements. There need not be a useful one-coordinate direction from every constrained state to an acceptable correction. The example is deliberately simple; it demonstrates a structural possibility, not the prevalence of institutional obstruction.

For pure action removal, holding everything else fixed,

\[
\Pi_{\rm restricted}\subseteq\Pi_{\rm full}
\quad\Longrightarrow\quad
\mathcal C_{\rm restricted}\subseteq\mathcal C_{\rm full}.
\]

This inclusion does not establish that every restriction is undesirable. A restriction may protect a consequence omitted from the vector. Nor can the inclusion be transferred unchanged to a political change that also alters trust, disclosure, cooperation, production or enforcement.

More fundamentally, an identical missing diagnostic action could represent broken equipment, unaffordable access, or a prohibition. The attainable set alone does not identify the historical or causal source. The experiment can isolate an explicitly imposed permission change; classifying an observed real-world failure requires evidence about why the feasible policy class took that form. Restoring several conditions at once can also be necessary, so there may be no unique “binding cause”.

## How the numerical claims were checked

Expected state/action visits satisfy ordinary flow conservation. Their consequence vector is linear. A phase-I linear program minimizes the largest normalized requirement violation. A nonpositive value produces a feasible witness; a positive separating margin certifies infeasibility. Coordinate scales normalize this diagnostic search but do not define an agreed utility. On an infeasible query, the returned policy still violates requirements and is never reported as acceptable.

Dual separating weights are independently checked by a backward dynamic program minimizing their weighted consequence. Occupancy ratios reconstruct an observation-based randomized policy, which is evaluated independently. The upstream production model is an unchanged byte copy; authority comparisons remove actions without changing the surviving transitions or costs.

All 252 main threshold queries are retained, with twelve detailed main examples, six one-period permission comparisons, four cash/permission comparisons, and 84 constrained frontier points. Detailed cases overlap the grid and are not independent replications. The thresholds were selected after exploration; grid counts do not estimate frequencies in society. Nine independent tests pass, including direct latent-event enumeration, the analytic witness and certificate, policy reconstruction, authority inclusion, finance/permission complementarity and terminal-only states. Review found and repaired an initially unsupported terminal-only graph; prior results and the unchanged upstream dynamics remain preserved.

See the [experiment and reproduction record](../../experiments/plural-correction/README.md), [mathematical proofs](../../_process/research/2026-10-04-integrated-evolution/plural-correction-math.md), and [implementation audit](../../_process/research/2026-10-04-integrated-evolution/plural-correction-design-review.md). These checks establish the finite calculations, not empirical adequacy, consent or ethical completeness.

## Feasible agreement can fail after people learn who bears the cost

The next boundary already has a small exact counterexample. Suppose a fair public coin determines whether a corrective plan imposes losses \((0,2)\) or \((2,0)\). Before the coin is revealed, both participants prefer its expected losses \((1,1)\) to a fallback \((1.1,1.1)\). Initial expected bounds \((1.05,1.05)\) are therefore achievable if the plan is carried out.

After either outcome is revealed, the participant facing loss two prefers the fallback. If that participant can refuse, refusal triggers the fallback, and no transfer, binding commitment or alternative response changes these consequences, the initially acceptable plan cannot be voluntarily implemented. The plan does not permit exchanging the burden after revelation. Randomly sometimes implementing it after revelation also fails the burdened participant's continuation test.

This is a separate analytic example, not a strategic extension already implemented in the productive model. Its implication is precise: **initial expected acceptability does not ensure continuing acceptance**. It neither argues against refusal rights nor recommends coercive commitment. Insurance, transfers, different responses or changed refusal consequences can change the outcome, but their resource and authority requirements must be explicit.

For a participant permitted to refuse at history \(h\), a necessary condition for voluntary continuation is

\[
V_i^\pi(h)\le d_i(h),
\]

where \(V_i^\pi(h)\) is their conditional expected remaining loss from continuing and \(d_i(h)\) is their loss under the specified refusal outcome. This condition addresses refusal deviations only. It does not prove truthful reporting or obedience to other actions. Histories must retain what participants actually know, including a disclosed lottery outcome; a physical belief state can discard distinctions relevant to promises and consent.

The [primary-literature audit](../../_process/research/2026-10-04-integrated-evolution/plural-correction-prior-art.md) connects these distinctions to established bargaining, constrained partially observed control, decentralized information, and incentive-compatibility results. A common objective is not a prerequisite for the mathematics of compatibility. Some shared procedural assumptions, meaningful policy descriptions, and justified requirements still have to be established.

## The next target

The next experiment should make participation a continuing decision inside the existing resource and information structure. Specify who bears each consequence, who can refuse at which histories, what refusal does, and whether compensation is available and actually funded. Compare initial joint feasibility with feasibility that also survives those participation decisions. Keep truthful reporting, hidden information and purpose revision separate until they are explicitly modeled.

This moves the north star from a universal scalar gradient toward **conditions for mutually acceptable, executable and revisable continuation**. The present theorem covers finite expected feasibility. It does not yet explain how acceptable requirements are formed, how people negotiate them, or how a collective preserves the standing to challenge them. Those are now identifiable missing structures rather than details hidden inside a common reward function.
