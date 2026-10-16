# v5 change log

Decisions, preserved and relocated content, withdrawn claims and open items for *Changing the AI Trajectory* v5.0 and v5.1 (THEORY.md), relative to *No Winning Position* v4.5 (`../v4/THEORY.md`, reading copy `../v4/THEORY-clean.md`). The manuscript itself carries no revision narration; it is kept here.

## 3 October 2026: v5.2, repairs after the self-review

Source: `reviews/REVIEW-v5.1.md` (a self-review by the drafting model; numerical checks in `reviews/checks_review_v51.py`). Ren: "let's fix, then spawn a round of review". Ψ, "the winning model" and the title are kept. v5.1 is archived as `THEORY-v5.1.md`.

- **F1 (error).** The three levers after Prop 1.4 are restated. Survival needs the product of the three factors to be summable. The second lever is shrinking what is contested, not merely halting its growth. A constant-stakes example shows a fixed race still decays.
- **F2 (overclaim).** "We are one is a long-run requirement" is now conditional on $(\mathrm{A_G})$ in §1.1, Prop 1.4's discussion, §9.2, §9.7, the Chinese overview and CLAIMS. The text says that $(\mathrm{A_G})$ carries the eventual loss and that the decomposition is the contribution. It also says that with saturating or summable hazards, growth and the race can coexist. §1.1 step 1 now says "under the inclusive self-model", not "outside Ψ".
- **F3 (model and interpretation).** Prop 1.5 now has two parts:
  - (1) Pooling payoffs widens the effective self and fails under relative selection.
  - (2) Sharing the contested prize scales intensity, dissipation and hazard by $1-\beta$ for every self-model, and reverses selection for load once $\beta>1-c_u/\nu_g$.

  The proof is in A.1, and block GM gains prize-sharing checks. The lessons now distinguish the two levers, and the C6 crux is restated.
- **F4.** Ψ governs where held or attributed. This covers the security dilemma and the spiral model, and the structural route of §4.6 and Prop 6.2(1) runs through the same attribution. It explains why §8's verification belongs to the pivot.
- **F5.** §1.1 step 4 now asks for a self-model that approaches the inclusive one. A conjecture [C] is added that true coupling $\kappa$ rises with a planetary technology's power, so accuracy and inclusion converge.
- **F6.** The power-scaling premise of Prop 1.3(3) is labelled [A]. Without it, the dissipated share is constant (1.007 at every scale).
- **F7.** §1.4 Material now separates two facts. Supply-chain interdependence (E13) refutes Ψ3's "win or be dominated". The argument against Ψ1 uses unpriced coupling (shared host, propagation, systemic risk). E13's premise and effect are rewritten.
- **F8.** The critique targets Ψ's reading of markets, not markets, consistent with Henrich et al.'s market-integration finding and with V5 (§1.4, E14).
- **F9.** Friedman's "so long as it stays within the rules of the game" is quoted. Its failure is located in signature C: rules become a prize when success buys them (§1.5, E15).
- **F10.** The major-transitions objection is answered. Between-group competition drove past integrations, but at planetary scale there is no outside group, and seeking an external rival is Ψ one level up.
- **F11.** The application of self-confirming equilibrium is limited to games with a cooperative equilibrium: repeated play and the common frontier (Prop 7.5).
- **F12.** §1.3 states the two models, faithful AI and the contest, before using them.
- **Minor.**
  - The standing term is read as a rank prize.
  - The third hazard factor is tied to signature C.
  - §2.6 and E15 note that the history of institutional criteria concerns firms generally.
  - The notation is now $(\mathrm{A_G})$.
  - The relational self is attributed to the author's theory of the relational self and 大同.

## 3 October 2026: v5.1, one governing model

### What governed the revision

Ren's critique of v5.0: six dynamics T1–T6 are too many. Most of them follow from one false competitive model, with three parts: compounding, winner-take-all logic, and naive Darwinism. Only inside that logic does the race make sense as a game, and the trajectory persists whatever is designed inside it. The reasons are the complexity of the system, the meta layer over long horizons, evolved wants such as status, and the dominant policy vocabulary and its history. Understanding that we are one interconnected system, not isolated rational selves, is a long-term requirement if growth and change are favoured.

### Changes

- **§1 rewritten around the governing model.** It is retitled "The governing model and the decision before us" and now has ten subsections.
- **The governing model.** Definition 1.1 introduces the winning model Ψ (讲赢 rather than 讲理). Its tenets are the isolated self (Ψ1), naive Darwinism (Ψ2) and winner-take-all compounding (Ψ3). It is named Ψ, not R, because R already denotes the readiness dimensions R1–R6 and a payoff.
- **Signatures.** T1–T6 are derived from Ψ and grouped into three signatures:
  - W: winning sets the objective and the tempo (T1, T2);
  - C: success buys control of correction (T4, T3);
  - N: the shared is invisible and cooperation looks naive (T5, T6).

  Every component of each dynamic is kept. The mapping is in CLAIMS.md §2.
- **New results, with proofs in Appendix A.1 and checks in block GM:**
  - **Prop 1.2, what a self-model can see.** At $\theta=-1$ the game in objectives is zero-sum. At $\theta=n-1$ it is a common-interest game. A shared change registers as the fraction $(1+\theta)/n$.
  - **Prop 1.3, the race and the self-model.**
    - The faithful-AI race ends above $\theta^\ast(\epsilon)<n-1$, and $\theta^\ast$ rises with AI effectiveness.
    - The share of the stakes dissipated rises with power, toward $r(n-1-\theta)/(1+\theta)$. It is unbounded at $\theta=-1$.
    - The total stays positive at every scale if and only if $\theta\ge(r(n-1)-1)/(1+r)$.
  - **Prop 1.4, growth needs a widening self.**
    - Under premise (A_G), the hazard is proportional to $r_t\Omega_tL_t(n-1-\theta_t)/(c+(1+\theta_t)L_t)$. Each factor is one tenet of Ψ.
    - With $L_t\ge L_{\min}$, survival is positive if and only if $\sum r_t\Omega_t(n-1-\theta_t)<\infty$: the boundary must close faster than the contested stakes grow.
  - **Prop 1.5, institutions widen the effective self.**
    - Benefit sharing raises the effective self-model to $n-1$ for anyone who values its own absolute payoff.
    - Under relative selection sharing changes nothing for $\beta<1$, and the lever moves to what winning converts into.
- **§1.4, why Ψ is false.** Four counts:
  - material: interdependence, including the semiconductor supply chain (E13);
  - biological: the major transitions, and cancer as cheating;
  - behavioural: E14;
  - compounding: partly true, and partly made true by institutions.
- **§1.5, why a false model governs.** Five mechanisms:
  - self-confirmation (Fudenberg and Levine 1993);
  - performativity;
  - selection of minds;
  - the status drive, with its two routes of dominance and prestige (E16);
  - the history of the policy vocabulary, through the neoliberal turn (E15).

  It also explains why design inside Ψ is re-absorbed (Meadows 1999; Props 3.11, 4.1, 4.5).
- **Framing of "Western".** The history is presented as the genealogy of a strand of thought that became dominant, first in the Anglo-American economies and then globally. It is not presented as the essence of any civilization, and the same tradition's critics are named. The body still names no pair of states or firms: Ψ is held by actors of every origin, and the analysis is the same wherever the dynamics are present.
- **Definition 1.6.** Continuation and pivot are redefined through Ψ. Continuation leaves Ψ governing; a pivot is a change of governing model, embodied in the same four elements as before.
- **Renumbering.** Old §1.2–1.7 became §1.6–1.10, with levels of claim and "what is claimed" merged into §1.9 without loss. References to §1.5 (outcomes) now point to §1.8.
- **Elsewhere in the paper:**
  - §2.6's evidence table has rows for Ψ governing and Ψ being false, and the T-rows are relabelled by signature;
  - §4.3 introduces θ by reference to §1.3;
  - §4.6 identifies the unbounded relative objective as Ψ in its purest form;
  - §6 classifications and the §6.9 table use W, C and N;
  - §9.2 gains a first link ("the trajectory has one root"), §9.3 a crux C6 (whether institutions widen the effective self), and §9.7 a paragraph on the governing model;
  - the Chinese overview is rewritten with a first item, 根模型.
- **Evidence register.** New rows E13–E16. Rows E1–E4 and E8 are relabelled by signature, and gap 6 is added.
- **Claims register.**
  - New rows Def 1.1 and Props 1.2–1.5.
  - L0 is added to the dependency chain.
  - A stale pointer (E15 for experimental evidence) is corrected to E11.
- **References.** A new group on evolution, behaviour, performativity and history. ‡ marks entries checked on 3 October 2026; † marks the classics not re-checked.

### Open after v5.1

- (A_G) is a modelling premise linking shared damage to the irreversible event. Its empirical counterpart is crux C1.
- The decisiveness $r$ of present contests and the conduct of actors under benefit sharing (crux C6) are unmeasured.
- Leonard (2009), Ostrom (1990), Polanyi (1944), Kropotkin (1902), Smith (1759) and Darwin (1871) are cited from prior knowledge (†).

## 3 October 2026: v5.0

### What governed the rewrite

- **Ren's direction**, through the v5 authorial brief (`sources/19-v5-handoff-2026-10-03/v5_0_direction_and_authorial_brief.md`).
  - The thesis is situational: the present winning-and-acceleration trajectory warrants a cooperative pivot. It is not a proof that bounded competition is impossible.
  - Credit the existing meta-attractor results.
  - Make perfect principal alignment within a harmful human game central.
  - A pause is not readiness to resume.
  - AI is a planetary technology, for people collectively.
  - Authority is a productive capacity for public purpose, and its design is a mechanism-design problem.
  - Preserve the nine layers. Theory before compression.
- **The v5 plan** (`../V5-PLAN.md`): fix the spine, repair, gather evidence, compare fairly, develop cooperation and transition, then write.
- **The handoff review of v4.5** (V45-01 to V45-11), checked against the actual statements; the repairs are recorded in CLAIMS.md §7.
- **Earlier rulings still in force.**
  - No pair of states or firms is made the subject; the body speaks of leading states and developers, and named sources appear only in the evidence register and references.
  - Do not promote race-camp arguments as strongest; each alternative is given its best case on its merits.
  - Repair in place; preserve plurality; no lossy consolidation.
  - E2 (stop) and E3 (slow) stay distinct, because stopping is itself a choice.

### Structure

v4.5's fourteen sections are reorganized into nine, in the order of the argument:
1. the decision;
2. the system and the present trajectory;
3. the meta-attractor mechanism;
4. faithful AI in a harmful game;
5. capability, delegation and correction;
6. the strongest case for continuing;
7. cooperation;
8. transition;
9. judgment and cruxes.

Every one of the nine layers keeps a home (THEORY.md §1.7 in v5.0; §1.10 in v5.1).

### Where v4.5's results went

| v4.5 | v5 | Change |
|---|---|---|
| Def 1, eq. (1) | Def 2.1, §2.2 | Unchanged |
| Def 2, Lemma 0 | Def 2.2, Lemma 2.3 | Cites translation invariance (Weibull 1995) |
| Prop 1 | Prop 2.4 | (2) stated for the mean load, with the counterexample in which the maximal-load share falls (V45-11) |
| Prop 2, Remark 1 | Prop 2.5, Remark 2.6 | Unchanged |
| Prop 3 | Prop 4.2 | Moved to the human side of alignment; boundary of (3) stated |
| Remark 2 | Remark 2.7 | Unchanged |
| Props 4–5 | Props 5.1–5.2 | (4) uses $\xi_i$ |
| Prop 6(1)–(5) | Prop 5.3 | Unchanged |
| Prop 6(6), Prop 31 | Prop 5.5 | Strict dominance at $q_L=1$ proved for every finite speed and profile; thresholds for $q_L<1$; bounded speed does not zero others; narrow and broad E1 separated (V45-05) |
| Lemma 1 | Lemma 5.4 | Unchanged |
| Remark 3 | Remark 4.3 | With the meta-attractor's "obedient system amplifying selected operators" |
| Lemma 2, Prop 7 | Prop 5.7 | (3) single-point weight check stated as necessary only (V45-11) |
| Prop 8 | Prop 6.4 | (1) "if", and "only if" when peace gives A the whole flow today |
| Props 9–11 | Props 3.4–3.6 | Third moment instead of HHI; fixed splitting delays capture by $2\ln k/(g-(1+\eta)\alpha)$; $U$ and $d$ kept separate (V45-11); predecessor comparison added |
| Remark 4 | Remark 3.7 | Unchanged |
| Section 4.4 (winner is a field) | §6.4 | As part of the benign winner |
| Prop 12, Remark 5 | Prop 3.8, Remark 3.9 | $\beta_{\text{model}}$ added |
| Theorem 1 | Theorem 3.13 | Unchanged |
| Theorem A | Theorem 5.15 | Branch I′ (decisive but saturating) added; (c) qualified by Prop 5.5 |
| Props 13–15, Cor 1 | Props 8.1, 8.3, 6.6; Cor 8.2 | Prop 13: $n$-player condition needs a bound on deviation gains; the no-trust case needs $g_D>0$ (V45-09) |
| Theorem B | Theorem 6.7 | With the second route of verification and its rate |
| Def 3 | Def 7.1 | Shared provision (g) and answerability (h) added |
| Theorem 2, Prop 16 | Theorem 7.2, Prop 7.3 | Unchanged |
| Props 17, 22 | Props 7.4, 7.5 | 0.413 named a correlated-belief threshold; the coalition's cooperation strictly dominant (V45-09) |
| Prop 18 | Prop 7.7 | Unchanged |
| Prop C | Prop 8.5 | Unchanged in substance |
| Props 19–21 | Props 3.10–3.12 | Brought into the main sequence |
| Lemma D | Lemma 5.6 | A conditional action-selection result with premises (a)–(d); enforced admission conditions block it (V45-03) |
| (X), (U), (φ′), (φ-s) | §5.4 premises | Stated about the hazardous set $Y$; (U) with uniformity; (φ) explicitly about residual risk after correction; growth-theory ground qualified by the symmetric case of AI raising $A_U$ |
| Lemma M | Theorem 5.8 | The conservative version with a uniform gap; liminf, not limit; summability without catch-up (V45-04) |
| Lemma M′ | Prop 5.9 | Uses $Y$, not $X$; linear and exponential coverage as stated models; bursts counterexample (V45-04) |
| Prop 26 | Prop 5.10 | Net residual risk; the recursion withdrawn as a theorem (V45-03) |
| Lemma 4 | Prop 5.11 | Serial and redundant topologies, with common causes (V45-03) |
| Lemma 5 | Remark 5.12 | Prediction separated from certification (V45-03) |
| Prop 27 | Prop 6.2 | $p_{L4}$ a belief; worst-case only as a named rule applied to every action (V45-01) |
| Prop 28 | Prop 5.13 | Implicit equation; multiple branches; sign change; saturation with summable risk; several levers (V45-02) |
| Remark 7 (was Prop 29) | Remark 6.1 | Unchanged in substance |
| Prop 23, Theorem S | Prop 5.14 | One discrete convention; finite horizons; mixed beliefs with their sign conditions (V45-07) |
| Prop 30 | Prop 6.3 | A trade-off, not an exclusion (V45-06) |
| Prop 24 | §8.3 (E1) | As the reason E1 must be held in common |
| Lemma P | Prop 6.5 | Repeated failure needs its premises; compared by hazard rate symmetrically (V45-06) |
| Corollary 2 | §8.2 and Prop 8.4 | Self-signalling near the limits withdrawn; the costly signal stated as a two-type game (V45-08) |
| Prop 32 | Prop 7.8 | Interim incentive compatibility; strict participation; other routes to equal shares (V45-09) |
| Remark 8 | Remark 7.6 | Third moment |
| Def 4 | Def 6.8 | Six durability tests applied to every arrangement, including the cooperative design (V45-10) |
| Remark 6 | Remark 4.7 | Unchanged in substance; the bound tied to the belief $p_{L4}$ |
| §10.4 (logic to oppose) | §4.6 | Destruction of the holder made conditional on the premises of §5.4 |
| §10.5 exits | §8.3 | E1 narrow and broad; E2; E3 with (E3-i) and (E3-ii); temporary pause as a fourth arrangement |
| §10.7 precedents | §8.6 | ABM Treaty read as reciprocal constraint changing the value of extra advantage (V45-10) |
| §10.8 (trees) | §7.1 | Unchanged in substance |
| §12 conditions | Appendix C; EVIDENCE.md | Indicators kept; observations moved to the evidence register |
| §13 objections | §§6, 9 | Each objection answered in place by the comparison or a crux |

### Withdrawn

Each withdrawal names the review issue that broke the claim.
- "No winning position" and "no branch of the race secures survival" as theorems over all paths. Freezing and rolling back keep positive survival, and saturation, bounded speed and summable risk are not excluded (V45-04, -05, -06). The title changes accordingly.
- "Lasting safety excludes the contest" (Corollary 3 of v4.4–4.5) as a theorem. It depended on the delegation channel and on an unbounded speed limit (V45-05). The situated judgment of §9 replaces it.
- Theorem E's long-run necessity of cooperation as a derivation. The same judgment is reached as a practical conclusion under standard D with stated cruxes.
- Risk compensation as support for a permanent hazard floor (V45-02).
- The recursion "a corrector beyond understanding relocates the uncovered region" as a theorem (V45-03).
- "Win and then stop keeps nothing" (V45-06).
- Maxmin applied only to restraint (V45-01).
- "I will cooperate" as self-signalling near the limits (V45-08).
- "IC requires constant shares", and "lowering the value of winning is the only route to equal shares" (V45-09).
- Pseudo-solution verdicts drawn from source figures read beyond what the sources state (V45-10).

### Added

- §1: the decision; the dynamics T1–T6; continuation and pivot defined in advance; outcomes O1–O4; decision standard D; values V1–V5.
- §2.6: the present trajectory against dated evidence.
- §3.1: the meta-attractor defined (reflexive coupling) and the local feedback benchmark; §3.2: capture defined independently of success.
- §4: perfect principal alignment and the harmful game (Prop 4.1, with an effectiveness parameter); how the objective reproduces; the chain-rule lemma; what a pause must change; readiness to resume (Def 4.6).
- §6: each continuation policy given its best case, installation path, residual risk and classification; a comparison at common horizons with a two-crux illustration.
- §7: the positive purpose; one concrete design (the Compact) by function; six stress tests and the durability tests applied to it.
- §8: the four temporal arrangements; a staged pathway with incentives, interim vulnerability and responses to breakdown; readiness applied to present evidence.
- §9: the judgment, its chain, seven cruxes, three redirecting outcomes, predictions and a research program.
- EVIDENCE.md: twelve evidence rows, with sources checked on 3 October 2026 where marked.
- CLAIMS.md: thesis, definitions, contribution inventory, dependency chain, interfaces, repair record.
- `checks_v5.py`: fourteen blocks of checks.

### Open

- The production relation between contestable coverage $U$ and the rate $d$ at which rule support is corrected (V45-11; CLAIMS.md §6).
- Measurements for cruxes C1–C5 (§9.3), especially residual risk after correction and the conversion channels $b_{ij}$, $\chi$.
- A full model-level comparison with dynamic models of constitutions (Acemoglu, Egorov and Sonin 2012); only the abstract was inspected.
- The broad form of E1 (labour, finance, persuasion) needs its own action space.
- A Bayesian treatment of the hard case beyond §6.6.
- Studies A–D (§9.6); design 2 of the pilot.
- Sources marked † or "from prior knowledge" in EVIDENCE.md and the references are to be checked before public use.
- Review: separate mathematical, empirical and governance reviews of v5.0, labelled as generated reviews, followed by a focused revision (plan pass 5).
- A venue-specific derivative, if wanted, after checking the venue's current requirements (plan pass 6).
