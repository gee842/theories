# Review of V6: keep the architecture, repair the necessities

Prepared for Ren on 3 October 2026. This reviews the actual V6 manuscript and its central proof dependencies, alongside the pasted completion report and V6 plan. It takes the newer authorial direction seriously: one interconnected host, a substrate-independent selection pressure, AI as instrument and potential carrier of that pressure, and institutional design by function.

**Assessment: V6 is conceptually clearer, but its strongest conclusions are not yet established.** The main problem is concentrated. Several new results turn a conditional identity, a sufficient safeguard, or a limiting case into a general necessity. Those extensions now support the opening thesis and §10. Repairing them should precede release or submission.

This was a targeted audit of the newly central mathematical results and the argument connecting them, with parallel mathematical, institutional/alignment, and systems reviews. It is not a certification of all 85 numbered results or a complete bibliography audit. I ran `checks_v6.py` successfully and independently checked the counterexamples below. No manuscript, register, or existing script was edited; nothing was committed.

Line references refer to the reviewed snapshot of [THEORY.md](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md). Its SHA-256 is `df44516ced03c7504c79c7cd06a104ae813ca94e0b7f5875a51d12f28e218483`. Independent calculations are in [counterexamples_codex.py](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/reviews/counterexamples_codex.py).

## Findings that affect the main argument

### 1. High priority: the decisiveness proposition uses the wrong continuation assumption, and the dilemma changes a limit into mere attainability

Locations: [Proposition 5.7](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:975), [Theorem 5.16](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1132), proofs at 2582–2584 and 2613.

Let the cooperative per-period objective be $C_i$, the one-period deviation gain $g_i$, the credible punishment value $v_i$, and the decisive state's per-period continuation payoff $d_i$. Direct comparison of discounted payoffs gives

$$
g_i\le\frac{\delta}{1-\delta}\left[(1-p_d)(C_i-v_i)+p_d(C_i-d_i)\right].
$$

The printed equation drops the second term. That requires $d_i=C_i$. The text instead assumes the decisive payoff is **at no more than** cooperation. With $d_i<C_i$, the omitted term is positive: cooperation can survive even with $p_d=1$ and a positive stage deviation gain.

A direct counterexample is $C=3$, $g=1$, $\delta=.9$, $p_d=1$, $d=2$. Cooperation is worth $30$; deviation is worth $4+.9(20)=22$. The printed condition says cooperation is unsustainable because its right side is zero. The proof also calls the upper bound on the deviation payoff the most favourable case for cooperation. It is the least favourable case.

There is a separate error even after setting $d=C$. Theorem 5.16 uses **attainable decisive advantage** to conclude that only stage-equilibrium cooperation remains. Proposition 5.7's benchmark reaches that conclusion only as $p_d\to1$ at fixed discount and payoffs. With $C=3$, $v=1$, $g=1$, $\delta=.9$, $p_d=.5$, $d=3$, cooperation is again worth $30$ and deviation $22$. Given the credible punishment continuation stipulated by the model, the non-stage cooperative profile survives despite attainable decisiveness. V6's own binary example sustains restraint at $\theta=0$ until roughly $p_d=.95$.

The proof at 2613 explicitly substitutes “bounded away from zero” for the limit toward one. Further, Branch II is “decisive but slow” at 1125 but is classified as unattainable decisiveness at 1133. Custody that reduces $p_d$ restores the possibility of repeated enforcement; it does not require that restraint subsequently be a stage equilibrium.

**Repair:** replace the binary dilemma with the exact enforcement condition

$$
\underbrace{(1-\delta)g_i+\delta p_d(d_i-C_i)}_{\text{immediate and decisive gains}}
\le
\underbrace{\delta(1-p_d)(C_i-v_i)}_{\text{remaining sanction}}.
$$

State the observability and credible-continuation assumptions. Analyze changes in temptation, decisive gains, detection, custody, punishment, and objectives through this condition. If $d_i\ge C_i$, the printed bound is necessary; equality requires the benchmark. Even then, stage-equilibrium behavior need not be sufficient if gaining the decisive state has extra value. The mechanism survives this repair, but the exclusivity claim does not.

### 2. High priority: translation invariance does not establish institutional persistence or the general nested-reward conclusion

Locations: [Lemma 3.3](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:476), [Proposition 6.7](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1311), and 1896, 1922, 2342, 2345.

Lemma 3.3 correctly states that subtracting the **same additive amount** from every payoff leaves relative selection unchanged. The prose and Proposition 6.7 replace this with a claim about any universally applicable constraint, then conclude that the constraint survives selection.

Universal application is not equal incidence. A common rule costing two otherwise equal developers $.3$ and $.1$ changes their relative payoffs. The paper's own effective liability is an especially important example:

$$
\pi_k-\pi_l=(\nu-\tau_{\rm eff})(e_k-e_l)+\phi_k-\phi_l.
$$

A common liability can reverse which practice is favoured. It works precisely by changing payoff differences, rather than being invisible to them.

Nor does invariance among compliant carriers establish stability against evasion, exemption, or changes to enforcement. If everyone is assumed bound forever, durability has been imposed as a premise. The endogenous weakening of rules studied in §4 still needs to be analyzed.

The unilateral conclusion is also too broad. A safeguard reducing error probability from $.20$ to $.01$ at cost $.01$, with revenue $1-p_{\rm error}$, raises the developer's payoff from $.80$ to $.98$. Relative selection favours it. The “other advantages” qualification in 6.7(1) disappears in 6.7(3) and the statement at 1327 that no developer can unilaterally counter instrumental convergence or reward hacking without losing standing. Relative outer selection also does not by itself make a developer's own objective purely relative, or imply that every reward specification contains exploitable divergence.

**Repair:** retain the identical-cost identity with its exact scope. State a conditional result about safeguards whose **net private cost remains positive**, including benefits from reliability, demand, liability, and avoided losses. Model common admission as a restriction on feasible conduct, and separately test whether enforcement survives success. The strong valid claim remains that faithful alignment to each principal does not resolve every conflict among principals. The larger claim that technical alignment failures are necessarily coordination problems is unsupported.

### 3. High priority: one planetary host does not make anticipatory design the uniquely possible source of integration

Locations: [Lemma 3.10 and its interpretation](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:605), proof at 2493, repeated at 2348.

With one group, the between-group covariance is zero. That identity does not eliminate institutional selection, subgroups, recoverable experiments, or transmission and innovation within the host. The Price equation's remaining term cannot generally be replaced with adverse within-group selection alone. Frank explicitly describes its recursive decomposition into selection among subgroups and transmission. [Frank, 1995, pp. 376–377](https://stevefrank.org/reprints-pdf/95JTB-Price.pdf).

For example, a costly trait under selection and transmission can obey

$$\dot z=-cz(1-z)+\mu(1-z),$$

with a stable positive equilibrium $z=\mu/c$ for $0<\mu<c$. This is one population with an unchanged relative cost and a source of change other than selection. It is not offered as a planetary solution; it identifies an assumption missing from the claimed exclusion.

More substantively, V6 already cites Sigmund et al. Their model develops sanctioning institutions through payoff imitation without requiring group selection or comprehensive planning. Its scale and assumptions do not prove planetary applicability. It nevertheless blocks the assertion that a Price decomposition rules out institutional emergence by such routes. [Sigmund et al., 2010, author-hosted paper](https://homepage.univie.ac.at/karl.sigmund/nature09203.html).

The unsupported step is at 611: rules “cannot be discovered by selection among alternatives.” At 613 the manuscript expressly calls the uniqueness of anticipation a theorem. Choosing the whole host as an accounting group cannot prove that.

**Repair:** retain the one-host argument as a reason not to rely on selection through global failures. Distinguish learning from local, reversible trials from learning that would require losing the only host. Anticipatory governance becomes especially important where consequences are global and irreversible. “We are one” can specify the system that foresight must account for, without claiming that every successful institution must originate from shared explicit understanding.

### 4. High priority: R1–R8 are not established as necessary finite-horizon requirements

Locations: [Proposition 7.10](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1673), proof at 2682, conclusion at 2336.

The table mixes all-time viability, sufficient global certificates, and normative commitments, while asserting that every arrangement meeting a probability tolerance at a finite horizon must satisfy them.

**R1 changes the horizon.** Theorem 8.2(3) concerns viability for all time. Set $K=V(0)=1$, $V_{\min}=.2$, $\rho=.01$, $h=.02$, $\nu=1$, $\tau=0$, with load-0 and load-1 carriers present. H0 holds. Since $E(t)\le1$, the host satisfies

$$V(t)\ge\frac{1}{2e^{.01t}-1}.$$

At $H=50$, $V(H)\ge.4353>.2$. The host does not cross its floor at any earlier time despite zero liability. Even continuous full load crosses only at about $109.86$. Hold other loss channels absent and authority intact: finite-horizon tolerance does not require all-time viability. This does not make the arrangement wise indefinitely; it refutes the stated finite-horizon necessity.

**R3 changes sufficiency into necessity.** Proposition 4.8(2) correctly gives full row sums below one as a sufficient global certificate. The manuscript also acknowledges that the uncaptured state is locally stable regardless of conversion. A direct example within Equation (3) is

$$\dot x=x(1-x)(z-1),\qquad\dot z=2x-z,\qquad x(0)=z(0)=.1.$$

Here $R=2$. The rectangle $0\le x\le.1$, $0\le z\le.2$ is invariant; inside it $\dot x\le-.8x(1-x)$, so $x,z\to0$. Channels remain and their gain exceeds damping. Avoiding capture therefore need not require $R<1$. This can coexist with safe host dynamics: with $\tau=2$, $\nu=1$, effective liability stays at least $1.8$, and sufficiently low initial load decreases. Requiring a certificate robust to every initial condition would be a stronger specified design standard, not a consequence of finite-horizon tolerance alone.

R4 inherits finding 1. R8 inherits finding 2 and overstates Lemma 6.5, which permits competition within enforced constraints. R7 explicitly rests partly on a value commitment; it is not a deduction from an O1/O2 probability bound.

**Repair:** separate three columns or tables: necessary conditions under named models and horizons; sufficient safeguards; normative requirements. Then compare institutions. Do not require competing proposals to pass the entire preferred design package as a purported theorem.

### 5. High priority: a zero sum across all actors does not make each communicating pair opposed

Location: [Proposition 5.14(1)](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1090), interpretation at 1097; proof at 2607.

The proof supports a two-party, statewise zero-sum sender–receiver result. The statement extends it to purely relative objectives among arbitrary numbers of actors.

Take three actors at $\theta=-1$. The sender sees a fair bit $t$ and the receiver guesses $y$. Let

$$\pi_1=\pi_2=\mathbf1[y=t],\qquad\pi_3=0.$$

Their relative objectives are $O_1=O_2=\tfrac12\mathbf1[y=t]$ and $O_3=-\mathbf1[y=t]$. They sum to zero. Yet the communicating pair wants the same action, so truthful cheap talk is an equilibrium. Their expected relative payoff rises from $.25$ without information to $.5$ with it. These messages directly concern relative standing.

**Repair:** keep the two-party result and the useful Crawford–Sobel bias example. Specify the actual conflict between sender and receiver. A claim that greater relative accounting generally decreases informativeness needs a mapping from the paper's objectives to communication bias; it does not follow from the aggregate zero sum. Coalitions and common-interest information channels remain possible.

### 6. High priority: the policy categories and decision inference still prevent a clean comparison

Locations: [Definition 7.12](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1712), policy table at 1732, [Definition 8.1](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1895), judgment at 2350.

Definition 7.12 defines a selection change as a change in the map from conduct to shares, resources, or standing. Export controls plainly can change that map, yet the table says they do not change selection because they target rivals and seek a lead. Definition 8.1 then reserves the term for a wide institutional package. These are three different concepts: changing incentives, changing them in a desirable direction, and establishing adequate durable governance.

Use the descriptive definition consistently. Record direction, coverage, enforceability, and durability separately. A policy can change selection and still be harmful or fail. This makes the proposed tests capable of distinguishing mechanisms rather than redefining successful policies as the preferred category.

The decision claim needs a separate repair. Standard D compares policies over a justified common uncertainty set. At 2350, non-exclusion of dangerous continuation is used to prefer changing selection, even though the proposed arrangement's breakdown risk remains unknown. That does not establish that any concrete alternative meets the tolerance or dominates the comparator. Greater joint benefit is secondary under D; it cannot settle an unresolved comparison of protected losses. Lemma 7.11 is a useful conditional dominance statement, but actual satisfaction of F1/F2 is not established.

**Repair:** distinguish the justified programme of independent correction, reciprocal verification, and reversible institutional experiments from a demonstrated ranking of whole arrangements. Give actual candidate policies the same measurable risk criteria. Retain policy advocacy where it is a reasoned value-and-evidence judgment, without calling the uncompleted comparison a theorem.

## Verification: reproducibility is not independent validation

The supplied `checks_v6.py` ran successfully and reproduced its numerical output. That is useful. However, [line 211 of the script](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/checks_v6.py:211) defines “sustainable” using Proposition 5.7's claimed inequality. The block does not independently evaluate the decisive continuation payoff. At $p_d=1$, it compares $g\le0$ with a separately enumerated stage equilibrium, confirming the identity after the contested assumption has already been imposed. The 1,260 symmetric checks verify zero relative payoffs for equal-action profiles, not the existence of credible repeated punishment.

Thus the statement at THEORY:983 that 21,096 cases agree with direct evaluation is misleading as a validation of the proposition as stated. The two-party cheap-talk enumeration is more independent, but it tests that narrower game and cannot establish the multi-party generalization.

The new review script evaluates discounted values directly and checks explicit counterexamples. All its assertions passed. Its field-model integration illustrates an analytic invariant-region argument; numerical convergence alone is not the proof. Neither script estimates the corresponding real-world parameters.

## Further corrections

These are smaller than the six findings above, but should be included in the same repair pass.

| Location | Problem | Repair |
|---|---|---|
| [6.1(5), 1219–1222](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1219) | The last two threshold limits omit cost growth. For $n=4$, $b(\epsilon)=\epsilon$, $d=1$, $c(\epsilon)=\epsilon^3$, the threshold tends to $-\infty$, although $\beta_b>\beta_d$ is said to make it tend to $3$. | State the cost exponent condition relative to the dominant effective prize/harm exponent and handle equality separately. |
| [6.4(2), 1269](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1269) | “Both, one or neither” of all/no delegation cannot occur in the stated model. The two incentive factors satisfy $g_{\rm all}-g_0=A(n-1)s^2/[n(n+s)]\ge0$. Both equilibrium conditions cannot fail. | Change to “one or both.” |
| [1368](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:1368) | Institutional capture parameters $R$ do not certify statistical error independence $\rho$. Even $R=0$ can coexist with a shared technical blind spot. | Specify or measure the interface; keep capture and common-cause error distinct. |
| [8.11 and 2021](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:2014) | The proposition assumes hazardous variety freezes; the prose attributes that bound to need-directed growth itself. New needs, uses, and interactions can continue expanding variety. | Say deliberately bounded hazardous scope with continued correction is a sufficient route. Treat its connection to purpose as a design hypothesis. |
| [T-G, 2394](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6/THEORY.md:2394) | The experiment predicts objectives matter little at high $p_d$, while the enforcement argument says objectives must carry more of the restraint as punishment disappears. | Derive a specific observable comparative static from the repaired model before registering the prediction. |

Lemma 7.11 also needs its conditioning assumptions stated. Its saved example has deterministic hazard schedules and exogenous dissolution. The general proof conditions on a future dissolution date, which can change earlier conditional hazards if dissolution is endogenous. Require the comparison to hold conditional on each such date, or supply a common history/filtration argument. This is a proof-scope gap, not a counterexample to hazard dominance under properly specified assumptions.

## What to preserve

The strongest improvements are substantial: the explicit separation of carriers, strategic actors, welfare and survival; the distinction between participant inclusion and a club that harms outsiders; the repaired treatment of prize sharing and positional power; the fairer comparison of oversight topologies; practical human authority rather than a requirement to follow every internal computation; and the open treatment of the proposed guardian's own capture, participation and breakdown risks. The evidence register's admissions about missing measurements also matter.

Keep the one-system framing, the meta-attractor as a mechanism to investigate, the three erosions as potentially coupled mechanisms, and the positive account of common provision. They do not require the invalid universal claims.

## An economical revision path

The central question can be stated more precisely:

> **Can cooperation remain incentive-compatible when success changes both the gains from defection and the institutions capable of correcting it?**

That question connects the host, the contest, capture, training, language, and transition. It accommodates the author's larger ambition without requiring every module to prove that all alternatives are impossible.

1. **Repair the dependency chain first.** Correct 5.7 and replace 5.16 with the enforcement condition. Limit 3.3/6.7 to the costs and enforcement actually modeled. Remove the Price-based uniqueness claim. Split the requirements table. Propagate those changes through §0, §1, §10 and CLAIMS before polishing the rest.
2. **Give “we are one” three explicit jobs.** It identifies shared dependencies; it grounds the stated commitment to affected parties' standing; and it guides institutions that return consequences and preserve correction. The first is an empirical/modeling claim, the second normative, the third a design programme. None becomes weaker because they have different kinds of support.
3. **Use the existing liability equation to explain common rules.** Coordinated restraint can remove the advantage of harmful conduct and block exemptions. Analyze whether it continues doing so when some actors become successful enough to contest the rule. This is more informative than assuming an equal common cost and declaring it protected.
4. **Make the alternatives measurable.** Classify interventions descriptively before observing success. State the adverse initial states and parameter ranges each safeguard covers. Compare concrete designs, including well-corrected competition, using the same horizon and uncertainty assumptions.
5. **Validate the repaired interfaces.** Test decisive continuation values, heterogeneous compliance costs, endogenous enforcement, several-actor communication, finite horizons, and capture basins. Audit the added citations separately. More random cases of identities already built into the code will not resolve these issues.

A defensible replacement for the strongest headline is:

> Competitive success can increase the gains from defection while weakening sanctions, correction and credible communication. Under specified conditions, this makes restraint fragile even when the participants recognize shared harm. Durable governance must address both the incentives for harmful conduct and the persistence of the institutions that constrain it. A shared host and potentially irreversible losses give particular importance to anticipatory coordination, but the adequacy of any institutional design must be established under the same standards applied to its alternatives.

That is a substantial theory to develop and test. It allows the stronger philosophical and political argument to be made openly, while the mathematical results carry exactly the conclusions they establish.
