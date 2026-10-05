# Identifying reproduction mechanisms and testing their added value

5 October 2026. Completed mathematical validation specification for the specialist-review package. This document supplies causal estimands, identification assumptions, an impossibility result, a finite-budget test-design optimum, an exactly solvable example, and a prospective analysis contract. It reports no newly collected observations. The current empirical failures remain in force.

The proposed scientific contribution is a testable distinction among current performance, existing corrective resources, outcome-responsive production of those resources, executable transmission to successors, and continued appropriateness after change. The existence of feedback, endogenous institutions, causal mediation methods, and optimal experiment design are established prior art. The contribution must be assessed as a particular integration and its discriminating predictions.

## 1. A supplied structural model, with the shortcuts exposed

The unit is an organizational lineage: founders, one completed maintenance opportunity, an actual handoff, and successors facing independently scored new cases. Repeated generations require repeated instances of this sequence. A single handoff is a finite transmission test.

Let:

- \(X,D\): pre-assignment circumstances and independently verified consequences of founder work;
- \(A\): timely rather than delayed access to the same verified outcome report;
- \(R\): the report actually received, including timing and content;
- \(W,M\): maintenance effort and the complete delivered package, respectively;
- \(B\): operative successor access, randomized after the package is sealed;
- \(Z\): what actually reaches the successor, including usability and execution permissions;
- \(X^+\): prespecified successor circumstances, including any change in the task;
- \(Y\): independently scored successor response by the deadline, with nonresponse retained;
- \(E,E^+\): dated support and access conditions.

One permissive structural model is
\[
\begin{aligned}
D&=f_D(X,U_D),&
R&=f_R(D,A,X,U_R),\\
(W,M)&=f_M(R,X,E,U_M),&
Z&=f_Z(M,B,X,E^+,U_Z),\\
Y&=f_Y(A,B,R,W,M,Z,X,X^+,E^+,U_Y).
\end{aligned}
\tag{I1}
\]
The exogenous \(U\)'s may be dependent. In particular, founder skill can confound errors and maintenance, and successor circumstances can confound actual use and success. The random assignments \(A,B\) are supplied by the design, not by assuming independence of all substantive variables.

The permissive outcome equation deliberately allows direct or alternative routes. Report timing might alter attention, founder service, or informal communication. The access treatment might alter successor expectations. Those routes cannot be deleted merely because the desired explanation is mediation through \(M\).

The hypothesized reproduction route is
\[
D\longrightarrow R\longrightarrow(W,M)
\longrightarrow Z\longrightarrow Y
\longrightarrow\text{the next maintenance opportunity}.
\tag{I2}
\]
The experiment manipulates access to information about \(D\), not harmful consequences \(D\) themselves. It therefore identifies an informational outcome-to-maintenance route. It does not identify every biological, financial, or political consequence-to-continuation route.

The empirical variables must be specified before observing outcomes. A scalar count of work slots is not the complete mediator when content, timing, readability, authority, or counterexample selection can change. Keep those dimensions and service sacrificed separate. The named intervention \(B\) controls one concrete access package; it is not an intervention on every possible meaning of corrective capacity.

## 2. What the two randomizations identify

Write \(M(a)\) for the complete package under the first assignment, \(L(a)=\ell(M(a))\) for a prespecified bounded measurement of delivered maintenance, and \(Y(a,b)\) for the successor outcome under both assignments. The complete artifact remains recorded even when \(L\) is binary. Assume:

1. **Well-defined versions and consistency.** The report, delivery times, access intervention, deadline, and outcome measurement have specified versions. Observed outcomes equal their assigned potential outcomes.
2. **Sequential randomization.** Given pre-assignment \(X,D\), \(A\) is independent of relevant potential outcomes. After sealing the package, \(B\) is randomized given recorded pre-\(B\) history \(H\), independently of future potential outcomes conditional on that history.
3. **Positivity.** Every arm in the target contrast has positive known assignment probability in the included strata. A protocol that cannot deliver an arm must not claim to identify its effect.
4. **A declared communication boundary.** Different experimental lineages do not interfere, or interference and exposure assignments are explicitly included. Within-lineage interaction is part of the treatment.
5. **Complete target-population accounting.** Include initially assigned lineages that produce no package, cannot act, or fail to answer. Missing measurement is distinct from measured nonresponse.
6. **A predeclared measurement and sampling target.** Outcomes are not redefined to make inherited-rule compliance count as correct response. Population generalization requires an additional sampling/transport argument.

For assignment probabilities \(p_a(X,D)\) and \(q_b(H)\), define
\[
\mu_{ab}=\mathbb E[Y(a,b)],\qquad
\widehat\mu_{ab}=\frac1N\sum_{i=1}^N
\frac{\mathbf1(A_i=a,B_i=b)Y_i}{p_a(X_i,D_i)q_b(H_i)}.
\tag{I3}
\]

**Proposition I1 — Assignment-effect identification.** Under assumptions 1–5, the population counterpart of (I3) equals \(\mu_{ab}\). Likewise, inverse weighting only by \(p_a\) identifies \(\mathbb E[L(a)]\). The resulting contrasts identify
\[
\tau_M=\mathbb E[L(1)-L(0)],\qquad
\tau_B(a)=\mu_{a1}-\mu_{a0},\qquad
\Delta=\mu_{11}-\mu_{10}-\mu_{01}+\mu_{00}.
\tag{I4}
\]

**Proof.** Conditional expectation over the second assignment cancels \(q_b(H)\), recovering the outcome under \(B=b\) at the first-stage history. Conditional expectation over the first assignment cancels \(p_a(X,D)\), recovering the outcome under \(A=a\). Consistency supplies the observed terms. The same first-stage argument applies to maintenance, which is sealed before \(B\). Linearity gives the contrasts. ∎

\(\tau_M\) measures the effect of timely information on delivered maintenance. \(\tau_B(a)\) measures the intention-to-treat effect of operative access after information assignment \(a\). \(\Delta\) measures complementarity of the two assignment effects. None is automatically the causal effect of increasing a scalar maintenance measurement.

An error stratum defined from \(D\) before \(A\) may be used to study effect modification. Error severity was not randomized. Conditioning on later maintenance, survival, package receipt, or use generally destroys the original randomized comparison.

## 3. Identifying the route needs an additional condition or intervention

Suppose the protocol justifies the stronger exclusion:
\[
Y(a,b)=G(X,U;b,M(a)),\qquad
G(X,U;0,m)=Y_0(X,U)\quad\text{for every admissible }m.
\tag{I5}
\]
Here \(M\) includes the whole successor-relevant package, and closing access removes its effect. There is no other \(A\)-to-\(Y\) route, and the blocked outcome has no dependence on \(A\).

**Proposition I2 — Gated transmission contrast.** Under (I5),
\[
\Delta=
\mathbb E\!\left[G(X,U;1,M(1))-G(X,U;1,M(0))\right].
\tag{I6}
\]
Thus the randomized interaction measures the effect of the report-induced package change through this particular operative route.

**Proof.** Substitute (I5) into (I4). The two blocked-access terms are the same \(\mathbb E[Y_0]\) and cancel. ∎

This result does not require independence between the package and outcome disturbances. Its force comes from randomization plus the strong route exclusion, not from treating maintenance as randomized. It still does not identify a response curve for arbitrary forced maintenance values, or natural indirect effects in the permissive model (I1).

### An exact counterexample to inferring mediation from a positive interaction

Consider two deterministic models:
\[
\begin{array}{c|cc}
&M&Y\\ \hline
\text{package route}&A&BM\\
\text{direct-channel rival}&A&AB.
\end{array}
\tag{I7}
\]
They have identical \((M,Y)\) in all four randomized \((A,B)\) arms, including \(\tau_M=1\) and \(\Delta=1\). In the second model, intervening on \(M\) has no effect. The factorial data alone therefore cannot determine whether maintenance caused the improvement.

An additional feasible package intervention can distinguish them: hold \(A=B=1\) and independently assign the delivered package to \(M=0\). The first model yields \(Y=0\); the second yields \(Y=1\). This must manipulate a specified delivered artifact, not merely instruct people to “have less maintenance.” Preserve the original effort, service cost, and artifact history separately, and audit whether the replacement procedure creates another route to \(Y\). If such a manipulation cannot be implemented consistently, the exclusion remains an assumption or the effect remains unidentified.

A second simple counterexample explains why two favorable main effects are insufficient: \(M=A,\ Y=B\) has positive effects on both maintenance and successor response, but maintenance is irrelevant to the response. Conversely, a null interaction does not exclude all coupled mechanisms: effects may be additive, average out, or operate outside the tested bottleneck.

These identification limits agree with the established mediation literature: randomized treatment alone does not generally randomize its mediator; additional assumptions or mediator interventions are required. [Imai, Keele and Yamamoto, 2010](https://imai.fas.harvard.edu/research/files/mediation.pdf); [Imai, Tingley and Yamamoto, 2013](https://imai.fas.harvard.edu/research/files/Design.pdf).

## 4. Exact identification is relative to feasible tests and delivered information

Let \(\mathcal M=\{M_1,\ldots,M_k\}\) be a finite set of frozen candidate mechanisms. Let \(\mathcal E\) be a finite catalogue of experiments that can actually be delivered with the current authority, support, time, and observation interfaces. A test may itself be a finite adaptive protocol. Its observed record has a finite alphabet \(\mathcal O_e\), and \(P_j^e\) is its law under candidate \(M_j\).

Tests must be feasible under all candidate possibilities covered by the guarantee. Hidden states are not available to the test policy unless its observations reveal them. A generic experiment that exhausts the system before its outcome can be recorded is not a feasible discriminating test.

Define
\[
M_i\equiv_{\mathcal E}M_j
\quad\Longleftrightarrow\quad
P_i^e=P_j^e\quad\text{for every }e\in\mathcal E.
\tag{I8}
\]

**Theorem I3 — Feasible discrimination and its impossibility boundary.** Suppose repeated experiments use independent, reset lineages under a fixed candidate model.

1. If \(M_i\equiv_{\mathcal E}M_j\), no adaptive selection of experiments from this catalogue can distinguish the pair from its delivered records. With equal prior weight on the pair, every decision rule has average error at least \(1/2\).
2. If every pair has different laws under some catalogue experiment, a fixed randomized design placing positive weight on all those separating experiments permits consistent identification as the number of independent lineages grows.

**Proof.** For part 1, a shared testing policy sees the same past-record law under both candidates. It therefore chooses the next experiment with the same conditional law; the next delivered record also has the same law. Induction gives equality for every finite transcript, including randomized policies and stopping decisions. An identical distribution contains no information about an equally weighted binary label. For part 2, record the experiment identity \(e\). The joint single-lineage laws \(J_j(e,o)=\lambda_eP_j^e(o)\) are distinct for all candidates. Empirical frequencies converge to the true finite-alphabet law. Since finitely many different laws have positive minimum pairwise separation, selecting the closest candidate empirical law is eventually correct almost surely. ∎

The theorem is about identifiability in this candidate class, not proof that one of the candidates is true. Include model checking and an unresolved/outside-class report. Do not force a substantive conclusion when every candidate misses a held-out intervention.

Removing observations can only decrease separability. If \(K\) is a common record-coarsening channel, then
\[
\operatorname{TV}(KP,KQ)\le \operatorname{TV}(P,Q).
\tag{I9}
\]
For finite records this follows by applying the triangle inequality to \(\frac12\sum_y|\sum_xK(y\mid x)(P(x)-Q(x))|\). Thus a valid measurement can matter even when the physical intervention is unchanged. The experiment identity itself must be retained: two mechanisms can have opposite deterministic responses to two experiments, yet identical unlabelled mixtures.

## 5. A proved optimum for choosing finite experiments

Let
\[
d_{ij,e}=\operatorname{TV}(P_i^e,P_j^e)
=\tfrac12\sum_o|P_i^e(o)-P_j^e(o)|.
\tag{I10}
\]
Let \(c_e\) be a vector of declared resource costs, \(C\) the componentwise expected budget per assigned lineage, and \(\lambda\) a randomized design. Costs can separately represent time, work, experimental burden, or another bounded resource; no common social objective is inferred.

Use the optimization
\[
\begin{aligned}
\max_{\lambda,t}\quad&t\\
\text{subject to}\quad&
\sum_e\lambda_e d_{ij,e}\ge t &&(i<j),\\
&\sum_e\lambda_ec_e\le C,\qquad
\sum_e\lambda_e=1,\qquad \lambda_e\ge0.
\end{aligned}
\tag{I11}
\]
Each catalogue test must separately satisfy any hard safety, permission, and deadline constraints. An expected-budget constraint cannot replace a requirement that every realized experiment fit available support. Finite total-budget scheduling also needs a feasible allocation of actual trials; independent randomization under (I11) does not guarantee a hard realized total budget.

**Theorem I4 — Exact finite-budget pairwise design optimum.** If the feasible design set is nonempty, (I11) attains an optimum. Because the experiment identity is observed,
\[
\operatorname{TV}(J_i^\lambda,J_j^\lambda)
=\sum_e\lambda_e d_{ij,e}.
\tag{I12}
\]
Consequently (I11) maximizes the worst pairwise separation of the single-lineage joint record. Equivalently, it minimizes the worst pair's best equal-prior binary classification error, which is \((1-t)/2\).

**Proof.** The feasible simplex slice is compact, and the minimum of finitely many continuous affine functions attains its maximum. Equation (I12) follows directly from the disjoint labelled records \((e,o)\). For two equally likely finite laws \(P,Q\), choose the more likely model at each observation. Its error is \(\frac12\sum_o\min(P(o),Q(o))=(1-\operatorname{TV}(P,Q))/2\). ∎

This is a precise chosen optimum, not a claim to minimize simultaneous multiclass error, sequential sample size, or deployment regret. Those are different optimization problems. The pairwise optimal decision rule may depend on which pair is under consideration; a single multiclass classifier need not attain every pairwise bound.

A matching dual certificate is
\[
\min_{\alpha,\beta,\rho}\ \alpha+\beta^\top C,\qquad
\alpha+\beta^\top c_e\ge\sum_{i<j}\rho_{ij}d_{ij,e}\quad(\forall e),
\quad\beta\ge0,\quad \rho\ge0,\quad\sum_{i<j}\rho_{ij}=1.
\tag{I13}
\]
Here \(\alpha\) is unrestricted. Weak duality follows by weighting the primal pairwise inequalities by \(\rho\), then applying the cost and normalization constraints. Finite linear-programming duality supplies matching optima. A primal design and a same-valued dual certificate prove optimality without relying solely on numerical solver status.

Point-candidate laws must be supplied or fitted before the discriminating outcomes are used. Estimated nuisance parameters require uncertainty propagation. A finite grid without approximation guarantees does not establish an optimum over a continuous uncertain model family. If the class contains an observationally indistinguishable direct-channel rival such as (I7), its unresolved pair forces \(t^*=0\) unless the feasible catalogue is expanded.

## 6. A complete finite example and exact budget certificate

Work in a pre-assignment stratum with a verified correctable founder error. Let \(A\) indicate timely relevant information; \(B\) indicate successor access; \(M\) indicate delivery of one defined corrective package; \(Y\) indicate correct successor response. There is enough support and time to deliver any listed test. Three deterministic candidate models are
\[
\begin{array}{c|cc}
\text{candidate}&M&Y\\ \hline
C\text{: outcome-responsive production and effective transfer}&A&BM\\
P\text{: preset production and effective transfer}&1&BM\\
N\text{: outcome-responsive production without effective transfer}&A&0.
\end{array}
\tag{I14}
\]
The calibration regime \(A=1,B=0\) yields \(M=1,Y=0\) under all three. No amount of data from that regime selects among them. Their descriptions refer only to the specified error stratum; they do not assert that the act of report assignment is itself informative in all settings.

Permit two new experiments:

| Experiment | Assignment | Recorded response under \(C\) | Under \(P\) | Under \(N\) | Resource cost |
|---|---|---|---|---|---:|
| \(F\): information withheld until after maintenance | \(A=0,B=0\) | \((0,0)\) | \((1,0)\) | \((0,0)\) | 1 |
| \(T\): operative handoff after timely information | \(A=1,B=1\) | \((1,1)\) | \((1,1)\) | \((1,0)\) | 2 |

The pairwise distance matrix is
\[
\begin{array}{c|cc}
&F&T\\ \hline
CP&1&0\\
CN&0&1\\
PN&1&1.
\end{array}
\tag{I15}
\]
With expected resource budget \(C=5/4\), put \(p=\lambda_F\). The constraint is \(2-p\le5/4\), hence \(p\ge3/4\). The objective is \(\min(p,1-p,1)\), uniquely maximized at
\[
\lambda_F=3/4,\qquad \lambda_T=1/4,\qquad t^*=1/4.
\tag{I16}
\]
The worst-pair optimal equal-prior single-lineage classification error is therefore \(3/8\). A dual certificate is \(\rho_{CN}=1,\ \beta=1,\ \alpha=-1\), with all other \(\rho\)'s zero. The two dual constraints read \(0\ge0\) and \(1\ge1\), and the bound is \(-1+5/4=1/4\). This exactly matches the design. For batches of four lineages, assigning three to \(F\) and one to \(T\) realizes the same proportions with total cost five; independently repeated assignment instead meets the budget only in expectation.

### What fails when an enabling condition is absent

- If successor access is unavailable, only \(B=0\) tests are feasible. \(C\) and \(N\) remain indistinguishable: maintenance delivery does not reveal whether transfer would work.
- If report timing cannot vary and only \(A=1\) is available, \(C\) and \(P\) remain indistinguishable: useful inheritance does not reveal outcome-responsive production.
- If only \(M\) is recorded, \(C\) and \(N\) remain indistinguishable even when \(T\) is executed: observing maintained resources is insufficient to establish correction.
- Introduce support \(s\in\{0,1\}\) and replace the package equations by \(M_C=M_N=sA,\ M_P=s\), retaining \(Y_C=Y_P=BM,\ Y_N=0\). At \(s=0\), all delivered records coincide. Removing support destroys the test's capacity to reveal the mechanism, not just its practical capacity to help.
- If the purported timely report carries no relevant information, let received relevant content be \(R=iA\) with \(i=0\), and let \(M_C=M_N=sR\). Then \(C,N\) coincide even with access. A null information-treatment effect in such an interface is not a universal refutation of responsive maintenance.

The numbers are an exact constructed witness, not estimated institutional effects. The unequal costs are declared experimental costs, not a claim about the price of actual human interventions. Adding feasible tests, hidden rival routes, observation noise, or model uncertainty changes the optimum.

## 7. The prospective validation and comparison contract

The existing [handoff design](../../../../experiments/integrated-correction/general-framework/reproduction-test/design/DESIGN.md) supplies the physical sequence. The following completes its mathematical decision rules while leaving real recruitment and data collection unperformed.

1. **Freeze the candidate restrictions and channels.** Include a preset-maintenance account, useful inheritance without outcome-responsive maintenance, direct attention or communication routes, and harmful inheritance. Specify the observations available for fitting separately from the interventions reserved for discrimination.
2. **Define the concrete physical test.** Independently score founder work; randomize timely versus delayed truthful reports with equal maintenance opportunities; record effort and seal the complete package; randomize operative access; replace founders; score fresh successor cases by a common deadline. Where mediation is claimed, add a feasible artifact manipulation or justify the route exclusion in (I5).
3. **Name distinct outcomes.** Use a prespecified delivered-package measure for the first arrow, independently scored successor response for the second, and separate service sacrifice, burden, unequal consequences, and inherited-rule obedience. Keep non-maintenance and nonresponse in the target population.
4. **Prespecify the precision and failure criterion.** Name the smallest practically relevant effect \(\delta>0\), error allowance \(\alpha\), relevant error stratum, and the predictions of each restricted mechanism before outcomes. A wide interval is inconclusive; an interval excluding a model's declared prediction challenges that model. A null interaction alone does not reject all reproduction mechanisms.
5. **Use appropriate units and assignment inference.** The independent unit is the lineage, not each case response. For the actual factorial study, use its assignment probabilities in (I3); stratification and repeated lineages require their corresponding analysis. Do not condition on post-treatment use or survival.
6. **Test added prediction before refitting.** Fit every rival on the same declared calibration channel. Freeze fitted laws or an uncertainty set. Predict the held-out randomized effects and joint outcomes. Do not refit the rival on the discriminating intervention and then count its original failure as a fair held-out comparison. Publish the negative results.
7. **Test added decision value separately.** A mechanism can be statistically distinguishable yet recommend the same action. At matched resources and information, compare a prespecified framework-informed intervention with the strongest simpler feasible alternative on the protected outcomes. Finding a difference in model likelihood is not itself evidence of improved coordination.
8. **Extend only after the first test.** A second real handoff tests repeated reproduction over a specified horizon. Another independently mapped domain tests transport. Neither is supplied by a single successful handoff.

For a conservative finite-sample reference, suppose lineages are independent, \(A,B\) are independent fair coins, and \(L,Y\in[0,1]\). The direct inverse-weighted summand for \(\Delta\) is
\[
V_i=4(2A_i-1)(2B_i-1)Y_i\in[-4,4].
\]
It has expectation \(\Delta\). The bounded-sum inequality gives
\[
\Pr(|\widehat\Delta-\Delta|\ge\delta)
\le2\exp(-N\delta^2/32).
\tag{I17}
\]
The same conservative bound covers each access contrast; the maintenance contrast has the stronger denominator eight. A union bound therefore gives simultaneous error at most \(\alpha\) for the four contrasts in (I4) whenever
\[
N\ge \frac{32}{\delta^2}\log\frac8\alpha.
\tag{I18}
\]
This is a sufficient, often very conservative precision bound, not a recommended sample size or a claim of adequate power for an unspecified effect. Independent lineages, bounded outcomes, fixed sample size, and known assignments are its premises. Shared sessions, adaptive stopping, or different assignments require changed guarantees. A blinded implementation pilot can support a more efficient prespecified design, but cannot retroactively supply confirmatory evidence.

For finite positive predictive laws, expected held-out log-score improvement of a true candidate \(P\) over \(Q\) equals
\[
\sum_e\lambda_e\operatorname{KL}(P^e\Vert Q^e).
\tag{I19}
\]
This is an interpretation of a proper predictive score, not a theorem that the more elaborate model wins in data. Fit uncertainty, misspecification, and the cost of collecting extra state variables all belong in the comparison. Zero predicted probabilities need an explicit scoring convention.

## 8. Existing evidence remains bounded and mixed

The previous [reproduction-test dossier](../../../../experiments/integrated-correction/general-framework/reproduction-test/README.md) already exhibits two models with identical permitted calibration history laws and different execution-intervention responses: approximately +9.99 percentage points versus zero in 25-round skill retention. That is internal mechanism discrimination. The stipulated harm-to-turnover law has not been empirically identified.

The same dossier's stationary-versus-reversal calculation shows why retained evidence can cease to be appropriate. Its large change in accuracy is a constructed model result, not an estimate for institutions or AI deployments.

The public institutional reanalysis reports a +42.59-point contrast in retained sanction permission, but 66 of 72 groups preserve the same agreement category. Treatment scheduling and coding qualify causal interpretation. The data identify neither repeated renewal nor endogenous continuation of the externally supplied experiment. The earlier one-round investment estimate is inconclusive, the microbial primary joint predictive criterion failed, and the earlier AI selector pilot's failed prediction remains in the record. See [the current evidence ledger](../FOUNDATION.md#162-empirical-results-include-failures-and-unresolved-links).

The present specification does not convert any of these into a favorable empirical result. It determines what a new test must observe and what would count against the proposed mechanism.

## 9. Prior art and the defensible contribution

| Primary source | Established contribution relevant here | Consequence for the present novelty claim |
|---|---|---|
| [Imai, Keele and Yamamoto, 2010](https://imai.fas.harvard.edu/research/files/mediation.pdf) | Identification and sensitivity analysis for causal mediation under explicit assumptions | Randomization/mediation distinctions and identifying restrictions are not new. |
| [Imai, Tingley and Yamamoto, 2013](https://imai.fas.harvard.edu/research/files/Design.pdf) | Experimental designs that manipulate or encourage mediators, with their consistency and exclusion limits | The added artifact intervention belongs to an established design family. |
| [Nitinawarat, Atia and Veeravalli, 2013](https://arxiv.org/abs/1205.0858) | Controlled sensing for fixed-sample and sequential multihypothesis tests; adaptive design can improve performance | Choosing informative interventions is established; (I11) uses a narrower, explicitly proved single-lineage pairwise criterion. |
| [Nitinawarat and Veeravalli, controlled Markov observations and nonuniform costs](https://arxiv.org/abs/1310.1844) | Sequential controlled tests with resource costs and asymptotic optimality results | No priority claim for cost-sensitive information acquisition or sequential optimal testing is justified. |
| [Weitz and colleagues, 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/) | Replicator dynamics coupled to environmental feedback, including an oscillating commons failure | Coupled selection–environment feedback is established prior art. |
| [Itao and Kaneko, 2025](https://doi.org/10.1073/pnas.2500960122) | Evolving decision functions, environmental dynamics, endogenous norms and punishment, and institutional regularities | Neither endogenous institutions nor decision rules shaping subsequent institutional evolution can be claimed as first discoveries here. |

The defensible candidate contribution is the alignment-specific assembly: reproduction of observation, authority, maintenance, transmission, and justified revision is evaluated through distinctions that survive feasible interventions, with explicit competitors and support costs. The present propositions provide a transparent route from that framing to identified estimands, nonidentifiability certificates, and a scoped test optimum.

These propositions are elementary applications or combinations of established causal inference, probability, decision theory, and linear programming. The particular synthesis and examples may be useful, but no exhaustive novelty search or priority proof has been completed. High significance would be earned by accurate new intervention predictions, useful design changes, and independent replication.

## 10. What is closed, and what new data must decide

The **formal validation specification is closed at this scope**: the causal target, observation and intervention contracts, identifiable contrasts, mediation boundary, feasible-test impossibility condition, finite optimal-design criterion, exact witness and certificate, primary comparison rules, and evidence limits are explicit.

The **empirical claim remains open**. New observations must establish whether outcomes actually change delivered maintenance, whether its operative transmission changes successor response, when inherited corrections become harmful or obsolete, and whether this account improves prediction or intervention beyond simpler competitors. Formal elaboration cannot determine the sign, magnitude, persistence, or transportability of those real effects.

The resulting contribution is neither merely “feedback exists” nor a completed universal empirical theory. It is a mechanism-specific, falsifiable, resource-aware programme with proved conditions for when its proposed distinctions can be tested at all.
