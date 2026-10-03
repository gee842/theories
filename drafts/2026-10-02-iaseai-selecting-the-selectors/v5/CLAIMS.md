# v5 claim register

Companion to [THEORY.md](THEORY.md). It records the thesis and definitions fixed before the comparison, every retained formal result with its status and predecessors, the dependency chain from mechanism to judgment, the interfaces between modules, and the repair of each issue raised against v4.5 (V45-01 to V45-11 of the [handoff review](../../../sources/19-v5-handoff-2026-10-03/v5_0_handoff/02_theory_v4_5_deep_review_and_handoff.md)). Prepared 3 October 2026 by Claude (Opus 5.5), and updated the same day for v5.1 (the governing model Ψ) and v5.2 (repairs after the self-review), under the [v5 plan](../V5-PLAN.md) and the [authorial brief](../../../sources/19-v5-handoff-2026-10-03/v5_0_direction_and_authorial_brief.md).

## 1. Thesis

The dynamics of the present trajectory follow from one governing model, the winning model Ψ: the isolated self, naive Darwinism, and winner-take-all compounding. Inside Ψ the race is the rational game, and its cost grows with the power of the technology. Ψ is false about actors' interests, about evolution and about human behaviour; it governs because it confirms itself, makes itself true through its institutions, recruits the status drive and selects its holders. Ψ governs where it is held and where it is attributed to others. If growth and change are favoured, and the shared damage of racing converts into irreversible risk, a self-model that approaches the inclusive one, "we are one", is a long-run requirement. Institutions can begin the change before every mind does: sharing the contested prize shrinks the stakes for every actor, and pooling makes a wider self-model effective.

The present trajectory of AI development pursues decisive advantage through acceleration, inside institutions whose conditions of evaluation and correction can themselves be reshaped by competitive success. The meta-attractor mechanism explains how such a trajectory reproduces its incentives and absorbs local safety reforms. Connected to delegation, shared exposure and the capacity to detect and correct consequential errors, it supports a practical judgment: the trajectory warrants a cooperative change of course, and the change needs institutions able to sustain shared flourishing, effective correction and a reachable transition.

This is a situated argument about the path we are on. It is not a claim that every form of bounded competition is impossible or unstable.

## 2. Definitions fixed before comparison

**The governing model** (THEORY Definition 1.1). The winning model Ψ is a model of self and world embodied in declared objectives, institutional selection rules and narratives of success. Its tenets:
- Ψ1, the isolated self;
- Ψ2, naive Darwinism ("the winner takes all, and the winner justifies all");
- Ψ3, winner-take-all compounding.

It is a property of the effective governing logic, not an accusation against any person or people.

**The present trajectory** shows three signatures derived from Ψ. Each is a proposition to substantiate (EVIDENCE.md), not a fact established by listing it. v5.0 listed six dynamics T1–T6; v5.1 derives them from Ψ and groups them as follows.

| Signature | Components | v5.0 codes |
|---|---|---|
| W. Winning sets the objective and the tempo | Strategic success defined substantially by relative or decisive advantage; capability, deployment and consequential delegation accelerating when rivals advance | T1, T2 |
| C. Success buys control of correction | Success reinvested in productive capacity and in influence over future evaluation and rules; oversight dependent on the resources, access, tools, schedules or personnel of those it oversees | T4, T3 |
| N. The shared is invisible, and cooperation looks naive | Shared harms and dependencies not reflected in individual decisions; collective restraint and shared provision treated as unrealistic, acceleration as the default | T5, T6 |

**Continuation** is any policy that leaves Ψ governing: it retains W, together with the conversion of success into influence over evaluation and rules (C), whatever safeguards it adds. **Pivot** is any policy that changes the governing model, by a mechanism that does not depend on one actor's continued unilateral restraint, embodied in a material change to at least one of four elements:
- *objectives*: consequential AI is directed to shared provision rather than to relative advantage (W);
- *decision rights*: strategic and coercive uses of AI sit under jointly verified limits, and evaluators' appointment, funding and access are separated from success (C);
- *constraints*: the tempo of capability and delegation is bound to the capacity for effective correction (W);
- *shared provision*: common infrastructure supplies useful services and correction that no actor owns, which makes the shared visible in every objective (N; THEORY Prop 1.5).

Bounded competition can continue inside a pivot. A safeguard does not become a pivot because it succeeds; it is classified by what it changes.

**Outcomes** are kept distinct, and the normative weight differs.

| Code | Outcome | Weight |
|---|---|---|
| O1 | Physical catastrophe: large-scale loss of life | Protected first |
| O2 | Loss of human decision authority over consequential systems in a defined domain, irreversible within the horizon | Protected first |
| O3 | Interruption of essential services | Protected |
| O4 | The end of a particular organization's or government's tenure | Not protected as such |

**Decision standard D.** Each candidate policy is evaluated at common horizons (near, medium, long), under one justified parameter range Θ applied to every policy, including the cooperative design's own failure modes: dissolution, capture, unjustified restriction and loss of service.
1. Bound the probability of O1 and O2 within each horizon over Θ.
2. Among policies whose bound stays below a stated tolerance, prefer the one with greater useful benefit, fairly distributed, and more retained corrective options.
3. If none meets the tolerance, prefer the policy with the lowest bound that keeps options open.

This is robust satisficing on irreversible losses, a normative choice. Expected-value and discounted-welfare criteria are reported where they disagree (THEORY.md §1.8, §6.9).

## 3. Claim types

Every claim in THEORY.md carries one type: **D** definition; **V** value or normative premise; **T** theorem or proposition proved within its model; **A** assumption (a premise of a theorem); **O** observation with a dated source (EVIDENCE.md); **N** numerical observation in a stated model (`checks_v5.log` and the v4 logs); **C** conjecture; **R** recommendation.

## 4. Contribution inventory

One row per retained formal result. "Proof" gives the location in THEORY.md Appendix A and its status. Predecessor comparisons are at the level of model structure. Where only an abstract or secondary account was inspected, the row says so.

| v5 | v4.5 | Statement | Key assumptions | Proof | Closest predecessor | Overlap | Difference | Present-world use |
|---|---|---|---|---|---|---|---|---|
| Def 1.1 | — | The winning model Ψ (isolated self, naive Darwinism, winner-take-all compounding) and its signatures W, C, N | Ren's direction (3 October 2026); corpus theories of the relational self, the selfishness spiral and narrative attractors | D | Self-confirming equilibrium (Fudenberg and Levine 1993); performativity (Ferraro, Pfeffer and Sutton 2005); leverage points (Meadows 1999) | A false model can be stable | One root for the trajectory's dynamics; applied to the meta-attractor of governing models | Organizing diagnosis |
| Prop 1.2 | — | Under a common self-model $\theta$, objectives sum to $(1+\theta)$ times the total; a shared change registers as the fraction $(1+\theta)/n$; zero-sum at $\theta=-1$, common interest at $\theta=n-1$ | Objectives $O_i=\pi_i+\theta\bar\pi_{-i}$ | A.1; elementary | Other-regarding preferences; translation invariance (Weibull 1995) | Standard algebra | Read as what each self-model can see; the dilemma located in the objectives | Why Ψ cannot see cooperation |
| Prop 1.3 | — | The race ends above $\theta^\ast(\epsilon)<n-1$, which rises with AI effectiveness; the dissipated share rises with power toward $r(n-1-\theta)/(1+\theta)$, unbounded at $\theta=-1$ | Faithful-AI game (standing as a rank prize); Tullock contest; [A] shared loss per unit scales with power while private cost does not | A.1; brute force and numerical best responses (GM) | Prop 4.2; Hehenkamp, Leininger and Possajennikov 2004 | Contest with other-regard | Power scaling; threshold $\theta_g$ rising with decisiveness | Cost of separateness grows with power |
| Prop 1.4 | — | Under $(\mathrm{A_G})$, survival is positive iff $\sum q_t<\infty$ with $q_t\propto r_t\Omega_tL_t(n-1-\theta_t)/(c+(1+\theta_t)L_t)$; with $L_t\ge L_{\min}$, iff $\sum r_t\Omega_t(n-1-\theta_t)<\infty$. The product must be summable; no single factor suffices otherwise | $(\mathrm{A_G})$: hazard proportional to shared damage, which makes a persistent race nonsummable by premise | A.1; chain rule | Lemma 4.4; time of perils | Standard product form | The decomposition: each factor is where one part of Ψ acts, and the rate each lever must achieve | "We are one" as a long-run requirement of growth |
| Prop 1.5 | — | (1) Pooling all payoffs turns a held $\theta_0>-1$ into $\theta_{\text{eff}}$, rising to $n-1$, but changes nothing at $\theta_0=-1$ or under relative selection. (2) Sharing a fraction $\beta$ of the contested prize scales intensity, dissipation and hazard by $1-\beta$ for every self-model, and reverses selection for load once $\beta>1-c_u/\nu_g$ | Linear pooling; equal division of the shared part of the prize | A.1; random checks and best responses (GM) | Profit sharing and team incentives; contest design with partial prizes | Standard | Two distinct levers: pooling widens the self, prize sharing shrinks what is contested and works under relative selection | Institutions first; V5 and Corollary 8.2 formalized |
| Lem 2.3 | Lem 0 | Relative selection is blind to terms common to all payoffs | Relative rule; additive common term (A1) | A, one line; standard | Translation invariance of relative dynamics (Weibull 1995) | Identical | Applied to shared host and to retention of delegated systems | Why shared harm does not register in selection (N) |
| Prop 2.4 | Prop 1 | Payoff-monotone selection raises mean load; with cumulative advantage the race type spreads and the host falls below its floor under C0 | Replicator or payoff-monotone rule; $B(t)\to\infty$ | A; v4.5 proof, wording of (2) narrowed to the mean (V45-11) | Alchian 1950; Schaffer 1988; Price 1970 | Selection on relative payoff | Floor of a shared host; cumulative condition; counterexample with converging $B$ | Mechanism of N |
| Prop 2.5 | Prop 2 | The weight on winning makes depletion dominant beyond $\bar\lambda$; all lose $\nu\bar e(\Theta-1)$ | Linear host; symmetric | A; brute force 180 cases (v3) | Armstrong, Bostrom and Shulman 2016; positional public goods (Frank 1985) | Comparative statics | Privileged groups deplete under relative selection | Links W to N |
| Def 3.1 | — | Meta-attractor: a region of state × selection-rule space with positive reflexive coupling | Corpus formal layer (2025-08) | D | Endogenous institutions; Goodhart; Acemoglu, Egorov and Sonin 2012 | Rules change with state | Coupling stated as a product of measurable channels | Organizing concept |
| Prop 3.4 | Prop 9 | Influence over correctors is selected, with return $\chi p^2\bar y^\top M\bar y$; above a size threshold when costs have a fixed part | Appropriability $\chi$; horizon-weighted support; faithful transmission | A; v4.5 proof; a local gradient, not an equilibrium | Krakauer, Page and Erwin 2009 (full text inspected); Bombardini 2008; Acemoglu, Egorov and Sonin 2012 (abstract) | Appropriability rescues costly modification of the environment (KPE) | The modified object is the selection rule; return scales with share squared; cross-domain conversion; valence reversed (a public good, correction, is eroded) | Mechanism of C |
| Prop 3.5 | Prop 10 | Correction is not supplied from inside a practice; keyed correction is control | Payoff-monotone selection | A; standard second-order public good | Oliver 1980; Heckathorn 1989 | Second-order free riding | Keyed correction as a form of Prop 3.4 | Why correction must be supplied outside |
| Prop 3.6 | Prop 11 | Independent correction must grow at $g/(1+\eta)$ (times returns to scale of cultivation) against a falling cost of control; fixed splitting delays capture by $2\ln k/(g-(1+\eta)\alpha)$ | Long horizons; positive channel; initial certificate | A; v4.5 proof plus V45-11 repairs | Regulatory capture (Stigler 1971; Laffont and Tirole 1991) | Capture as an equilibrium of influence | A rate condition tied to the falling cost of control | The certificate's failure time; what AI-equipped correction must achieve |
| Props 3.10–3.12 | Props 19–21 | Capture certificates; seeded cascades; re-absorption of reforms; a pause that freezes shares completes or undoes capture depending on whether rule-making is insulated | Cooperative monotone field (3) | A; v4.5 proofs (pruning, comparison, Lyapunov) | Granovetter 1978; Morris 2000; Kempe, Kleinberg and Tardos 2003; Acemoglu and Robinson 2008 | Threshold cascades; k-cores; de facto power | Certificates by full row sums; reform re-absorption; two pause designs | Why local reforms fail and how a pause must be designed |
| Prop 3.8, Rem 3.9 | Prop 12, Rem 5 | Captured evaluation silences moderate harm; conservative and disjunctive alarms | Averaged reports; known bound on masking | A; elementary | Certification (Lizzeri 1999); audit independence | Biased certifiers | Silent crossing as a property of the alarm rule | Observation layer |
| Thm 3.13 | Thm 1 | The slow route: the host crosses its floor before any alarm under C0–C6 | All of the above | A | — | — | A combined conditional result | Tier-2 conclusion, needs C0 |
| Prop 4.1 | — | Faithful AI implements a collectively inferior outcome when principals' objectives value relative standing | $b>c+d$ | A; brief §3A; standard | Positional externality games | Identical in form | Placed as the test of principal alignment | Core of §4 |
| Prop 4.2 | Prop 3 | The boundary error of the self-model; selection on actions favours $\theta=-1$ | Tullock contest | A; closed form checked to $10^{-7}$ | Schaffer 1988; Güth and Yaari 1992; Heifetz, Shannon and Spiegel 2007 | Preference evolution | The self-model as the human side of alignment | Why objectives reproduce |
| Lem 4.4 | — | Nonsummable residual hazard on surviving histories sends survival to zero; a mere delay does not change it | Uniform lower bounds on surviving histories | A; chain rule; standard | Time of perils (Sagan 1994; Ord 2020; Thorstad 2022) | Standard | Applied to "pause then resume unchanged" | §4.3 |
| Props 5.1–5.2 | Props 4–5 | Join or eliminate in the objective; dissipation; the penalty for falling behind dissipates in the decisive limit | Tullock or all-pay | A; v4.5 | Tullock; Hillman and Riley 1989; Baye, Kovenock and de Vries 1996 | Standard contest results | The objective/material/welfare split | Contest layer |
| Prop 5.3 | Prop 6(1)–(5) | Exact condition for delegation to become dominant as speed grows | Additive stakes, one period | A; v4.5 | Armstrong, Bostrom and Shulman 2016 | Racing trades safety for speed | Delegation as the traded variable | Point of no return I |
| Prop 5.5 | Props 6(6), 31 | With the lock priced in ($q_L=1$), not delegating strictly dominates at every finite speed; $q_L<1$ gives speed thresholds; one delegator does not drive others' survival to zero | One-period survival form | A; proved in general (V45-05) | — | — | New | Why E1 can be an equilibrium among informed actors |
| Prop 5.7 | Prop 7 | Tempo bound; peak sensitivity at least $e^{a\tau}$; irreducible lags | LTI delayed mode | A; Hayes 1950; maximum modulus | Skogestad and Postlethwaite 2005 | Standard control facts | Single-point weight check stated as necessary only (V45-11) | Point of no return II |
| Prop 5.13 | Prop 28 | Risk homeostasis on a stable interior branch; multiplicity; saturation permits summable risk | Continuous delegation, $r=1$ | A; implicit equation; numerics | Peltzman 1975; Wilde 1982; Stafford, Trager and Dafoe 2022 | Risk compensation in races | Delegation as the compensating margin; branch structure | Limits on what safety gains buy inside a contest |
| Thm 5.8 | Lemma M | On a continuation branch with a uniform coverage gap and a residual-hazard lower bound on surviving histories, survival decays geometrically | (X), (U), (φ) as stated premises | A; chain rule | Time of perils | Standard form | The premises named and made measurable | Conditional mismatch result |
| Prop 5.9 | Lemma M′ | Freezing after a sprint leaves exposure until coverage catches up with the hazardous set; rolling back ends it | Linear or exponential coverage | A; corrected to $Y$ (V45-04) | — | — | New | Finite sprint |
| Prop 5.11 | Lemma 4 | Serial oversight chains lose reliability as $f^k$; redundant checks can approach one, limited by common causes | Stated topology | A; reliability theory | Series–parallel reliability | Standard | Applied to scalable oversight | AI-assisted correction can succeed or fail |
| Prop 6.4 | Prop 8 | Preventive attack under a commitment problem | Bargaining protocol (A8) | A | Fearon 1995; Powell 2006 | Standard | Survival-first comparison (Prop 6.5) | Deterrence and prevention |
| Prop 6.6, Thm 6.7 | Prop 15, Thm B | Commitment under a growing overhang; verification required to the degree winning exceeds cooperating; a bound on undetected defection as a second route | Assurance game | A | Schelling 1960; arms-control verification | Standard deterrence calculus | The two routes and the rate condition | Verified agreements |
| Thm 7.2, Prop 7.3 | Thm 2, Prop 16 | Sufficient safeguards and a necessary average-liability condition; no unilateral solution | Replicator; C0 | A | — | — | Combined | What cooperation must contain |
| Prop 7.5 | Prop 22 | A common frontier turns a dilemma into coordination; 0.413 is a correlated-belief threshold | Two-stage timing | A; Nash-verified numerics | Coalition stability (Barrett 1994) | Coalitions of the willing | Pooled frontier with non-subordination | Common frontier design |
| Prop 7.8 | Prop 32 | Participation: efficiency, information (interim IC), distribution | Private types; interim participation | A; corrected (V45-09) | Myerson and Satterthwaite 1983; Fearon 1995 | Standard mechanism design | Survival compression | Participation of the strongest actor |
| Prop 8.1 | Prop 13 | Assurance threshold; n-player sufficient condition needs a bound on deviation gains | Two-action reduction | A; corrected (V45-09) | Kydd 2005; Carlsson and van Damme 1993 | Standard | Measures stated | Trust |
| Prop 8.3 | Prop 14 | Cheap talk credible only when the receiver's action is commonly wanted | Crawford–Sobel uniform-quadratic | A; standard | Crawford and Sobel 1982 | Identical | Applied to talk about shared hazard | Why talk does not carry the transition |
| Prop 8.4 | — | A verifiable, durable E1 separates types iff it costs a relative-objective actor more than it gains by inducing restraint | Two-type signaling | A; standard costly signaling | Spence 1973; Kydd 2005 | Standard | Specifies what makes E1 a signal (V45-08) | First step of the transition |

## 5. Dependency chain

The practical judgment of §9 depends on the following claims. Each link names its type and where it is supported.

| Link | Claim | Type | Support | Status |
|---|---|---|---|---|
| L0 | The trajectory's dynamics follow from the winning model Ψ, held or attributed; inside Ψ the race is rational and its cost grows with the stakes; under $(\mathrm{A_G})$, with growing stakes and harm per unit not driven to zero, survival needs the gap to the inclusive self-model to close faster than the contested stakes grow, or what is contested to shrink; Ψ is false and maintains itself | D + T (Props 1.2–1.5) + A ($\mathrm{A_G}$, power scaling) + O + C (convergence of $\kappa$) | THEORY §1; EVIDENCE E1, E13–E16 | Mechanisms proved in their models; Ψ's governance evidenced in declarations and in the history of firms generally; $\mathrm{A_G}$ a modelling premise tied to crux C1 |
| L1 | Relative success is reinvested in influence over future evaluation and rules, when appropriable, persistent and large relative to cost | T (Prop 3.4) + O (C) | THEORY §3; EVIDENCE E4–E7 | Mechanism proved; diagnosis partly evidenced |
| L2 | Local reforms are re-absorbed when inbound conversion from captured domains exceeds one | T (Prop 3.11) | THEORY §3.6 | Proved in the field model; channels to be measured |
| L3 | Faithful AI does not resolve a harmful human game, and the game's objective reproduces | T (Props 4.1, 4.2) + O (W) | THEORY §4; EVIDENCE E1–E3 | Mechanism proved; diagnosis evidenced in declared objectives and framework clauses |
| L4 | Safety gains inside the contest are partly absorbed by more delegation and speed | T (Prop 5.13) + O | THEORY §5.5; EVIDENCE E2 | Branch-dependent; not a permanent hazard floor |
| L5 | Correction must keep pace with the hazardous set it must cover; the gap today is real for some hazard classes | A ((X), (U), (φ)) + O | THEORY §5.4; EVIDENCE E8–E11 | Premises stated; partly evidenced; central crux |
| L6 | Credible continuation policies do not meet standard D without changing W or C | Comparison | THEORY §6 | Argued per alternative; cruxes stated |
| L7 | A cooperative design can meet standard D, survive its own stress tests, and be reached in stages | R + T (Thm 7.2, Props 7.5, 7.8, 8.4) | THEORY §§7–8 | Design specified; feasibility conditional |
| L8 | Therefore a cooperative change of course, a change of governing model, is warranted now | R | THEORY §9 | Holds if L5 and L6 hold within Θ; L0 strengthens it and C6 tests its institutional route; cruxes named |

## 6. Interfaces between modules

| From → to | Output quantity, units | Population and timing | Receiving premise | Bridge |
|---|---|---|---|---|
| Capability → hazardous behaviour | Variety of hazardous behaviour $Y_t$ in a defined hazard class, per period | Per hazard class; per model generation | (X) of §5.4 | Conjectured; to be measured by predefined hazard modes and coverage units |
| Hazardous behaviour → residual irreversible loss | Conditional per-period probability of O1 or O2 after the correction architecture in place | Per hazard class; per surviving history | (φ) of §5.4 | Conjectured; the AI-risk premise |
| Understanding → executable correction | Coverage $U_t$ (decisions meeting C1–C4) and correction rate $d$ of rule support | Per institution | Prop 3.6, Thm 5.8 | Kept separate (V45-11); a production relation $d\le F(U,\text{resources},\text{delay},\text{authority})$ is an open interface |
| Success → evaluator control | Conversion $b_{ij}$, appropriability $\chi$ | Per domain; per selection horizon | Props 3.4, 3.10 | Mechanism derived; channels to be measured (EVIDENCE E4–E7) |
| Observed danger → policy preference | Change in an actor's policy after evidence of shared hazard | Per actor; per decision cycle | Prop 8.4, §8 | Conjectured; experiment evidence is mixed (EVIDENCE E11) |
| Contest stage → long-run outcome | Whether the contest ends, capability freezes, hazards continue, actors rebuild | Per branch | Thm 5.8, Props 5.9, 6.3 | Stated per branch; no all-paths theorem |

## 7. Repair record for V45-01 to V45-11

Status: **repaired** (the inference is corrected in THEORY.md and the review's counterexample is respected), **narrowed** (the claim is kept in a weaker, supported form), or **open** (the gap remains and is named).

| Issue | v4.5 claim | v5 action | Acceptance case (`checks_v5.log`) | Status |
|---|---|---|---|---|
| V45-01 | Survival-first implies counting domination as certain; P3 implied by P1; P2 implies (X) | $p_{L4}$ is a belief; maxmin, if used, is a named rule applied to every action; P3 is an independent premise with a "decisive but saturating" branch; P2 does not imply (X) | — (logic) | Repaired |
| V45-02 | Risk compensation establishes a permanent hazard floor | Prop 5.13 states the implicit equation, multiple branches, the sign change on the high branch, and saturation with summable risk; (φ) is an independent premise | HO: two interior equilibria at $\Delta\psi=0.9$; summable risk under full delegation | Repaired |
| V45-03 | A corrector beyond understanding relocates the uncovered region; serial $f^k$ for all oversight; chaos excludes certification; Lemma D as a theorem about representation | Prop 5.10 states net residual risk; Prop 5.11 separates serial and redundant topologies with common causes; Remark 5.12 separates trajectory prediction from invariant certification; Lemma 5.6 is a conditional action-selection result with its premises | OV: serial 0.531 vs redundant 0.999999; a fallible corrector raising survival from $7\times10^{-10}$ to 0.63 | Repaired |
| V45-04 | Freeze integral with $X$; sub-exponential $U$ implies $g_U\to0$; summability equals catch-up; lower bound equals actual hazard | Prop 5.9 uses $Y$; linear and exponential coverage stated as models; summability distinguished from catch-up; liminf of a lower bound | MM: zero exposure when $Y\le U$; bursts keep $g_U=0.5$; summable gap never closing | Repaired |
| V45-05 | Two zeros for $q_L$ high; E(2) from $s\to\infty$; narrow E1 implies broad E1 | Prop 5.5: strict dominance at $q_L=1$ for every finite $s$ (proved); thresholds for $q_L<1$; a bounded-speed delegator does not zero others; narrow and broad E1 separated | DL: 0 violations in 20,000 draws; 0.0045125; $s\ge206.42$; 0.33 | Repaired |
| V45-06 | A stopping winner keeps nothing; prevention always fails | Prop 6.3 is a trade-off (freeze 0.53, roll back 0.86 survive); Prop 6.5 compares prevention by hazard rate and states the premises of repeated failure | FS | Repaired |
| V45-07 | Discrete and continuous rates mixed; strict preference between two zero limits; belief-mixing threshold $O(1-p)$ | One discrete convention; comparison at common finite horizons; sign conditions and order of limits stated | SR: 0.04628; racing dominant at $H=1000$ under the review's beliefs | Repaired |
| V45-08 | Near-indifference makes "I will cooperate" self-signalling; E1 separates types | Self-signalling claim withdrawn; Prop 8.4 gives the conditions under which a durable, verifiable E1 separates | SG | Repaired |
| V45-09 | IC requires constant shares; lowering the value of winning is the only route to equal shares; 0.413 is risk dominance; n-player sufficient condition | Interim (Bayesian) IC; strict versus weak participation; share bounds; ex-post participation; other routes to equal shares; 0.413 named a correlated-belief threshold; a bound on deviation gains added | K7: interim share 0.5 with varying ex-post shares; $S_a=2$; N13: $-3.7279$ | Repaired |
| V45-10 | Pseudo-solution verdicts on Plan A from the plan's own figures | Durability stress tests applied symmetrically to every arrangement, the cooperative design included; decline, dissolution and impairment distinguished; handoff described as conditional | — (sources) | Repaired |
| V45-11 | $U$ bounds $d$; HHI as capture pressure; fixed splitting removes capture; mean load as the race share; single-point control check as a certificate | $U$ and $d$ separate; third moment $\sum p^{1+2/\eta}$; splitting delays capture; mean-load wording; single-point check necessary only | CAP: 23.03; 0.25 vs 0.5; $-0.9889$; $\lvert w\rvert=2$ | Repaired, except the $U\to d$ production relation, which is **open** |

**Closed issues kept closed.** Finite-horizon mutual racing can remain a strict equilibrium. Shared hazard does not remove cheap-talk bias. Proposition 24 uses branch-specific decisive probabilities. Proposition 22 distinguishes membership-then-effort timing from deviations against fixed effort. Common-frontier existence has no general requirement that $n\ge3$ and $r>1$. The history-conditional hazard premise and the separate shared-failure premise are kept.

**The experiment record.** One 20-seed rubric-editing pilot exists. Its P1 prediction failed; P2–P4 held ([PREDICTIONS-2.md](../experiment/PREDICTIONS-2.md)). Design 2 has not been run. v5 reports the failed prediction and does not substitute a proposed study for it.
