# Reviews of "When Capability Outruns Correction" (2026-09-28)

*These are two AI reviews of Ren's paper of 2026-09-28, both requested by him that day. The paper's source is at `sources/05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.tex`. The `.pdf` beside it is the same text compiled, eight pages. Part I is by Claude Opus 5.5, written in the Claude Code session that added the paper to this folder. Part II is by a Claude Fable 5.1 reviewer that the same session started. It read only the paper and the 2026-08-22 position paper, and it did not see Part I. Both parts are AI reviews and are labelled as such under this folder's conventions. The numerical results in Part I come from `check_models.py` and `coupled_chain.py` in this folder, and those in Part II from `fable_verify.py`. All three scripts are pure Python and have no dependencies.*

## Where the two reviews meet

*Written by the Part I reviewer after both reviews were complete.*

**Both call for a major revision.** Part II's verdict is "publishable as a short modelling-and-policy note once the models are coupled and the positioning fixed".

**Reached independently by both.**
- **The mathematics is correct.** `,qquad` at line 53 prints literally in eq. (2).
- **The chain is not built.** The "explicit chain" promised in §2 is not delivered: the paper gives five fragments, and they are never coupled. Both reviews propose the same repair: make assurance, evaluation delay or the observation map depend on r, and show the chain. Part I gives it as a numerical sketch and Part II as a proposition to prove.
- **The pause rests on the rate arithmetic.** It rests on (6), (7) and the maxmin rule, not on the capture model. That model's levers are b, d and a; κ is absent from R_cap. Freezing x lets r relax to bx/d, and the pause regime is itself open to capture, a point the paper gives one clause.
- **The transition-path claim is true but never demonstrated.** Each review supplies an example, with different parameters and the same result.
- **Irreducibility is unnecessary** for the spectral threshold.
- **The same prior work is missing,** led by:
  - coordinated pausing (Alaga and Schuett 2023);
  - if-then commitments and the Seoul commitments;
  - Collingridge and the pacing problem;
  - regulatory capture and niche construction;
  - Weitz et al. 2016;
  - quasi-option value.
- **Notation clashes** in g, B, L and ρ.
- **Against the 2026-08-22 paper,** the stag hunt, the founding act of restraint and the historical precedents are dropped. The result is more defensible and less distinctive.

**Only in Part II.**
- **Φ gives a basin certificate.** Φ makes the system a gradient system, with Φ(L) = 0, Φ(S) = −c/(2R_cap) and Φ(H) = c(R_cap/2 − 1). So Φ(x₀, r₀) > 0 certifies convergence to H.
- **x\* = 1/R_cap is not the tipping share.** It is the saddle's x-coordinate; starting from r = 0, the tipping share in the running example is about 0.60.
- **Two proof steps are missing.** The h = ρ case needs ∫(1−x)dt < ∞. A parameter-level version of (5) also exists: r(0) < c/a and x(0) ≤ x̄ < 1/R_cap.
- **The lemma and the inequality are narrower than they are used.** The lemma covers sure safety only, while §7 reasons about probabilities. Inequality (7) assumes serial, deterministic clocks from a common origin.
- **The advocate's objection.** Triggers that must be "jointly agreed" by the very parties r describes will fire late or never. The fix is to make the trigger the absence of a passing independent safety case, not proof of hazard. §7 contains this burden inversion in embryo; §8 does not use it.
- **The evidence is one-sided.** The METR evidence measures C only; nothing in the paper bears on A(t).
- **Licensing.** The closest analogues to §8 are licensing and grounding regimes:
  - pre-market approval;
  - IAEA declarations and inspection;
  - containment tiers;
  - the 737 MAX grounding, with its demonstrated-fix exit.

  Item 4 of §8 is an approval, so the paper should say whether it proposes licensing.
- **More prior work:** the Conditional AI Safety Treaty; A Narrow Path; MAIM; Scheffer et al. 2009 on early-warning signals in bistable systems (for §9); and bioeconomics for eq. (3).
- **All ten references checked on the web, and all correct.** Add Cimpeanu's article number, 1723, and METR's arXiv ID, 2503.14499. The METR blog post now carries a banner saying it is out of date, so cite the arXiv version, and METR's Time Horizon 1.1 (2026-01-29) for the current rate.

**Only in Part I,** mostly because Part II was kept out of the corpus.
- **Reversal time depends on the lever.** Take two reforms with the same post-reform R_cap and the same end state. A liability-type reform keeps the substrate above the floor; a rule-sunset reform does not. Capture of the measurement channel acts as delay.
- **Declining the transition is the common safe action,** and dependency erodes it.
- **Model (1) can be read as a coordination game,** that is, a stag hunt.
- **The corpus.**
  - Conceptual capture is missing.
  - The paper's lineage runs through the 2026-06 and 2026-07 drafts.
  - Eq. (6) is the repaired eigenvalue budget.
  - The paired domains the v6 plan required are absent.
  - The agent-fleet case is available.
  - Its scope sits against the 09-26 ruling, and its defensive register against the 07-13 ruling.

**One disagreement, resolved.** Part I lists the burden-of-proof inversion as kept, in the §7 safety case; Part II lists it as dropped. Both are right: §7 states the inversion as a procedural rule, and §8's triggers do not use it. Part II's fix is the right one.

---

## Part I — Claude Opus 5.5

### Verdict

The paper is careful and honest about its limits, and its mathematics is correct. I found one typesetting bug and no errors.

Its weakness is structural. The paper names its contribution as a chain: success changes the rules of selection, those rules reach observability, and observability sets how long correction takes. What it delivers is the links as five separate toy models that never touch. The policy it argues for, a conditional pause, follows from the rate-mismatch arithmetic. It does not follow from the capture model that gives the paper its name. That model implies a different remedy, one that complements the pause, and the paper never states it. Both gaps can be closed inside the paper's own equations, and §3 below sketches how.

The paper places itself against too little prior work, and the gaps are where a governance reviewer will look first. Against the corpus, it is the first solvable instance of the meta-attractor's second-order clause and the first text with a falsification section. It also drops the step that, by the corpus's own account, makes the meta-attractor more than regulatory capture.

### 1. What the paper argues

**The capture model.** A practice's share x and a rule-support variable r feed each other. The variable r stands for defaults, standards, procurement and assessment conventions that favour the practice. The model is ẋ = κx(1−x)(ar−c), ṙ = ε(bx−dr).
- **Below the threshold.** When R_cap = ab/(cd) < 1, the practice dies out from any starting point.
- **Above it.** When R_cap > 1, both "none" and "all" are stable, and the rules the system has inherited decide which one it reaches.

**The substrate.** A common maintenance condition V declines under capture when the harm rate h exceeds V's regrowth rate ρ. Relative selection stays blind to V, because V enters both practices' payoffs equally.

**Four further results.**
- **Coupling.** Linking channels can make a state unstable even when each channel alone is stable.
- **Indistinguishability.** Suppose two states look identical to the decision-maker but need disjoint safe actions. Then no rule based on those observations is safe in both.
- **Rate mismatch.** If a challenge index grows faster than assurance, their ratio crosses any limit in finite time.
- **Latency.** Correction requires τ_eval + τ_decide + τ_reverse < T_irreversible.

**What it proposes.**
- **A procedural rule.** Any step that expands both capability and exposure needs a safety case first.
- **A conditional, reciprocal pause** on exposure-creating transitions, with an exit test.
- **Refutation conditions,** and the data streams that would test them.

### 2. The mathematics, checked

| claim | status | note |
|---|---|---|
| Equilibria L, H, S of (1); S is interior iff R_cap > 1 | correct | S = (1/R_cap, c/a) |
| L is always locally stable; H is stable iff R_cap > 1 | correct | The Jacobian at L has eigenvalues −κc and −εd. At H they are −κ(ab/d − c) and −εd. |
| S is a saddle | correct | det J(S) = −κεab·x(1−x) < 0 |
| R_cap < 1 gives convergence to (0,0) from any 0 < x(0) < 1 | correct | The r-bound and the logit argument together are complete. Numerically, all 200 random starts converge, with r(0) up to 5. |
| Φ and Φ̇, eq. (2) | correct | Φ̇ vanishes only at the three equilibria, so LaSalle's principle gives convergence to an equilibrium. Numerically, every one of 300 random starts ends at L or H, and Φ never decreases. |
| The stable manifold of S divides the basins | correct (standard) | |
| Path dependence: same x, different r, different destination | correct | With R_cap = 2 and x(0) = 0.55: r(0) = 0.3 goes to 0, and r(0) = 0.7 goes to 1. |
| Substrate limits, eq. (3) | correct | For h = 1.5, V → 0 quickly. For h = ρ, V(400) = 0.0025 ≈ K/(ρt), which is the "slower boundary decay". For h = 0.5, V → 0.5 = K(1 − h/ρ). |
| Viability condition, eq. (5) | correct | A Nagumo-type condition. It is sufficient only, as the paper says. |
| "A reform can eventually lower x yet do so only after V has fallen below the functional floor" | true, not shown | The body asserts this and the abstract promises it ("shows why…"), but no example is given. §3 below supplies one. |
| Φ̇ ≥ 0 while V → 0, eq. (4) | correct but over-read | V does not enter ẋ or ṙ, so (4) restates the modelling assumption. Φ is needed for the global proof, but its r-gradient is not a selection criterion. "Local improvement according to endogenous selection criteria" therefore reads more into it than it holds. |
| Spectral threshold ρ(D⁻¹B) ≶ 1 | correct | s(B − D) < 0 ⇔ ρ(BD⁻¹) < 1 holds for any B ≥ 0 and positive diagonal D (van den Driessche and Watmough 2002). Irreducibility is needed only for a strictly positive growing direction. The two-channel eigenvalues −1 ± g are right. |
| Indistinguishability, deterministic and randomised | correct | A clean lemma. Its escape clause, a common safe action, matters most (§4). |
| Crossing time t*, eq. (6) | correct | It is an identity. Nothing depends on the growth being exponential, only on C/A rising. |
| Latency inequality, eq. (7) | correct as a necessary condition | The paper should say where T_irreversible is measured from, presumably the onset of exposure. |
| Worst-case rule p₊L > B | correct | This is maxmin expected utility (Gilboa and Schmeidler 1989), and the paper states it as a conservative rule. |

**Typesetting.** At `.tex` line 53, `,qquad` is missing its backslash. The PDF prints "qquad" inside eq. (2).

### 3. The chain is claimed but not built

§2 of the paper states the contribution as "an explicit chain connecting success-induced changes in selection conditions, institutional memory, deterioration of a common substrate, loss of observability, and the practical time required for correction." The body delivers five separate objects:
- model (1) with (3);
- a linearised z-system;
- a lemma about the observation map O_m;
- the ratio q;
- inequality (7).

r never affects O_m, A or any τ, and V affects nothing. So the two halves of the title, recursive capture and epistemic lag, never meet. A reader can accept every equation and still ask where the chain is.

The chain can be built with one addition that the paper already has words for: governance reacts to the substrate it observes. I tested the smallest version inside the paper's own model. The parameters are a = b = d = 1, c = 0.5 (so R_cap = 2), κ = 1, ε = 0.2, ρ = K = 1 and h = 1.5. The run starts at x = r = 0.6, V = 1, with a floor at V_min = 0.3. A reform fires when the *observed* V falls to 0.6.

- **The model has its own T_irreversible.** Without reform, V falls from the alarm level 0.6 to the floor 0.3 in 1.83 time units.
- **Reversal time depends on the lever.** Two reforms reach the same R_cap after reform (2 → 0.67) and the same end state (x → 0, V → K):
  - *Raising c* from 0.5 to 1.5 stands for liability, a cost internalised by the practice. Selection turns around at once. V bottoms out at 0.457. The reform tolerates a delay for observation and decision of up to about 1.0 time units, and the floor is crossed at a delay of 1.5.
  - *Raising d* from 1 to 3 stands for a sunset on rules, and it acts through rule memory. x keeps rising for 0.5 time units after the reform. V bottoms out at 0.263 and crosses the floor even with zero delay.

  So the abstract's claim holds in the model: a desirable end state can be reached through an unsafe transition. At the same R_cap, it holds for one lever and not the other. τ_reverse in (7) is therefore not a free parameter; where the lever acts sets it.
- **Capture of the measurement channel works as latency.** Suppose assessment conventions shaped by the successful practice flatter the substrate in proportion to capture: V_obs = V + μ(r/r_H)(K − V), where r_H = b/d is the rule support at full capture. With zero delay and the fast lever, μ = 0.6 postpones the alarm from t = 0.76 to 1.91; V bottoms out at 0.321, just above the floor. At μ = 0.8 the alarm comes at 4.39 and the floor is crossed. The capture variable itself turns epistemic closure into extra τ_eval in (7).

That is the chain in the paper's own terms:
1. Success raises r.
2. r shapes the measurement structure m.
3. A captured m delays or masks the signal.
4. That delay, set against the lever's own reversal time, decides whether the floor holds.

This also formalises the step that §5 names only in prose, epistemic closure. It is the step the corpus calls conceptual capture (§6 below).

### 4. The policy does not follow from the capture model

- **The pause rests on the rate model.** Equations (6) and (7) carry it. Hold the covered part of C still (g = 0) while A grows, so that q falls. Resume when q is back under q_max and (7) has been demonstrated. Model (1) carries none of this.
- **Model (1) points to structural levers.** On its own terms it implies levers on R_cap = ab/(cd):
  - lower **b**, the rate at which success converts into rule-setting power, by keeping standard-setting, procurement criteria and evaluator funding separate from market share;
  - raise **d**, the decay rate of rules, through sunset clauses and periodic re-justification;
  - keep **a** small, so that rules do not favour incumbents;
  - raise **c**, the costs the practice itself bears, through liability.

  κ and ε do not enter R_cap: they move the date, not the destination. This is the same two-class reading the meta-attractor document gives its own levers (`theories/meta-attractor/README.md`, claim 187). The paper does not name any of these as the policy consequence of its central model.
- **A pause does not leave the capture basin.** Freezing x lets r settle at bx/d. If the system is already past the separatrix when the pause begins, capture resumes when the pause ends. The paper states the principle ("replacing leaders or models therefore need not replace the selection environment that promoted them"), but it does not apply it to its own proposal.
- **The pause regime is itself a selection environment.** Whoever sets the triggers, the "agreed standard" in the exit test, and evaluator access holds exactly the b-channel the model describes. Item 5 of §8 makes this point in one sentence. It should be the design rule for items 1–4: exit criteria set by parties with no stake in the covered transition, criteria that decay unless re-justified, and reasons given in public.
- **Accumulation.** During a deployment pause, compute, algorithms and scaffolds keep improving. Latent C therefore grows while deployed C is held, and resumption arrives as a step in C that leaves A no time to catch up. The 2026-08-22 paper made "govern accumulation, not just capability" its first specification of a rational pause. This paper omits it, and it is the pause sceptic's strongest objection.
- **The pause as the common safe action.** The indistinguishability lemma fails when there is an action that is safe in both states, and declining a transition is usually that action. Once dependency builds, withdrawal stops being safe in every state, which means capture shrinks the set of common safe actions. That one sentence would link §§3, 5 and 8 of the paper. It is the formal reason to act before dependency builds, which the paper argues only informally.

How §8 maps onto the models, for the revision:

| §8 element | model quantity | status in the paper |
|---|---|---|
| Declare the trigger | a step in C, or a fall in T_irreversible | implicit |
| Pause covered escalation | g = 0 on the covered dimension | implicit |
| Evaluators with access and standing | raise α; shorten τ_eval and τ_decide; keep m independent of r | partly stated |
| Exit test | q ≤ q_max with a margin; (7) demonstrated, with τ_reverse measured in a rollback drill | stated in words |
| Reciprocal, anti-monopoly | b, d and a for the pause regime itself; R_cap < 1 for the regime | one sentence |
| Accumulation (missing) | latent C during the pause | absent |
| Structural levers outside any pause (missing) | b, d, a, c | absent |

### 5. Prior work the paper should position itself against

Ranked by how soon a reviewer would raise it. Part II checks the accuracy of the paper's existing references.

1. **Collingridge's dilemma** (*The Social Control of Technology*, 1980), **the pacing problem** (Marchant, Allenby and Herkert, eds., 2011) and **Ogburn's cultural lag** (1922). The paper's central question is whether institutions keep an effective right to change the direction of optimisation after it succeeds. That is the Collingridge dilemma, and C/A is the pacing problem. The 2026-08-22 paper cited Collingridge; this one dropped him.
2. **Alaga and Schuett, "Coordinated pausing: an evaluation-based coordination scheme for frontier AI developers" (2023).** Its scheme is nearly the skeleton of §8: a dangerous-capability evaluation triggers a pause, the developer notifies others, they pause too, and work resumes once thresholds are met. It also raises antitrust law as an obstacle to coordination among developers, which bears directly on "an initial agreement among willing major developers".
3. **Responsible scaling policies and if-then commitments** (Anthropic 2023; Karnofsky 2024), and **the Frontier AI Safety Commitments made at Seoul** (May 2024). Signatories undertook not to develop or deploy a model if mitigations cannot keep risk below their thresholds. A conditional pause therefore already exists, in voluntary and self-assessed form. The paper's real policy contribution is what those regimes lack: independence, reciprocity and a public exit test. Its capture model explains why they lack it, since self-set thresholds are the b-channel. The 2026-08-22 paper said this ("the form is right, the organ is missing"); this one does not mention RSPs at all.
4. **Capture and increasing returns in institutions.**
   - Stigler (1971) on regulatory capture, which the word "capture" invites.
   - Pierson (2000) on increasing returns in politics, the nearest analogue of the r-dynamics.
   - Niche construction (Odling-Smee, Laland and Feldman 2003), the biological name for success altering its own selection environment.
5. **Game–environment feedback.** Weitz et al. (2016, *PNAS*) came before Tilman et al. (2020). When the environment feeds back into payoffs, these models produce cycles and recovery as well as collapse. The paper cuts that feedback in §4. Cutting it is legitimate when the harm falls on non-participants (the externality of its own §6), but the paper should defend it on those grounds.
6. **Irreversibility and option value** (Arrow and Fisher 1974; Henry 1974). The §7 rule gets its strongest support from quasi-option value: when learning is possible and outcomes are irreversible, the flexible action is worth more. The paper mentions option value but cites nothing for it.
7. **Races and structural risk.** Armstrong, Bostrom and Shulman (2016); Zwetsloot and Dafoe (2019); Critch and Russell (2023, TASRA); Kulveit et al. (2025, gradual disempowerment); Kasirzadeh (2025, accumulative risk). The claim that the analysis holds "even when the models' terminal objectives remain diverse" is a structural-risk claim, and the paper should say so.
8. **Instruments the paper already relies on.** Safety cases (Clymer et al. 2024); dangerous-capability evaluations (Shevlane et al. 2023); compute verification (Shavit 2023); the limits of compute thresholds (Hooker 2024); frontier regulation (Anderljung et al. 2023).
9. **The control theory the paper leans on.**
   - Ashby's requisite variety, and Conant and Ashby (1970), for the observability lemma.
   - Corrigibility (Soares et al. 2015) and relative reachability or attainable-utility preservation, for the "effective right to change the direction of optimization".

   Framed as corrigibility of the development process rather than of models, the paper's central question would be legible to the alignment field at once.
10. **Existing regimes to anchor §8.**
    - The EU AI Act's obligations for general-purpose models with systemic risk, and the 2025 Code of Practice.
    - California SB 53 (2025).
    - China's AI Safety Governance Framework (TC260).
    - The IDAIS consensus statements signed by Chinese and Western scientists from 2024 on, which already propose red lines and verification. They are the natural bridge for a reciprocal regime.

Discipline for this list, from Ren's 2026-07-13 ruling on the 智善 causal chain: put each item where it helps a real reader. A related-work paragraph should state what is new. Its job is not to fill the body with defences against imagined hostile readers (see §7).

### 6. Against the corpus

**Where it comes from.**
- **The title** is the "Sixth movement: capability outruns correction" of the 智善 writing-program plan v6 (`06-zhishan/writing-program/plans/v6.md`, 2026-07-12).
- **The central principle** is in the speculative-future foundations (`04-speculative-future/current/FOUNDATION-PRINCIPLES-REVISION-PROCESS.md`, 2026-06-09): "Acceleration must be governed by correction capacity."
- **Eq. (7), §9 and §8** carry out three requests from the causal-chain reviews of 2026-07-13 (`06-zhishan/writing-program/causal-chain/v2/reviews/ai-empirical-red-team.md` and `…/v5/reviews/deep-synthesis-and-consolidation-direction.md`):
  - the correction window "as a testable inequality";
  - three falsifiers;
  - "conditional pauses, but not a blanket halt", with a role-level decision rule.
- **The model's parts** come from the meta-attractor's 2025-08 formal layer (`theories/meta-attractor/README.md`, claims 193–197):
  - the two-timescale form, with fast x and slow λ̇ = εḡ;
  - a viability barrier on a logistic resource, the same form as eq. (5);
  - arms races treated as a spectral-radius problem.

**What it sharpens.**
- **A first solvable instance.** This is the first solvable instance of the slow-layer law λ̇ = εḡ(x, λ), with a threshold (R_cap) and a proof of bistability. The corpus had asserted an attractor; this paper exhibits one.
- **Two standing critiques answered.**
  - Definition 1's guard ("repetition alone is insufficient") carries the 2026 correction that totalisation cannot be declared from concentration, dependency or growth alone.
  - §9 supplies the falsification section the meta-attractor documents lack (critique 29 there).
- **A usable budget.** Eq. (6) is a well-formed replacement for the eigenvalue budget the corpus marked unusable (meta-attractor claim 188, critique 32). It governs a ratio, which has governance meaning; the old budget governed an unnormalised norm.
- **Rates, not speed.** "A uniform multiplication of all dynamical rates merely rescales time; risk arises from changed relative rates" matches the date-versus-destination split of the meta-attractor's levers. It also matches Ren's ruling of 2026-09-25 that growth is not the danger.
- **Independence defined.** Independence is defined along five axes: failure mode, funding, test data, access, and the power to trigger correction. That is more usable than anything earlier in the corpus.
- **The self-sealing route closed.** "Dismissing contrary evidence as proof that critics have been 'captured' would itself be an epistemic failure" closes the self-sealing route the corpus has been warned about.

**What it drops.**
- **Conceptual capture.** The meta-attractor document names the step at which the winning logic comes to define what counts as evidence. Without it, the document says, "meta-attractor" is "just a long name for regulatory capture, increasing returns, or endogenous institutional change." Model (1) is exactly increasing returns plus endogenous rules, and epistemic closure appears only in prose. The masking term in §3 is one way to put the step back; it is the formal counterpart of "What you can't count stops counting."
- **From the 2026-08-22 paper:**
  - **The incompressible floor of signal formation.** This was the reason α cannot simply be raised. The new paper leaves g > α as an open empirical question and allows that tests might scale fast enough.
  - **Governing accumulation.**
  - **The stag hunt under common knowledge.** The new paper's §6 falls back to "social dilemma".
  - **Building coordination by pausing,** with legible restraint as the founding act. Only one sentence remains: "An appeal for one actor to slow down while all others race is strategically weak." Without the founding-act argument, that sentence reads as rejecting it.
  - **Domain ordering and the criterion** "no game may be accelerated beyond the metabolic rate of its own rules". Eq. (7) is the formal half of that criterion.
  - **Reallocation** (sensors, not actuators), which survives only as "permitting safety progress".
  - Collingridge, Ashby, Perrow and Holling.
- **The paired-domain demonstration** that the v6 plan required: "Do not present 'capability' and 'wisdom' as two civilization-wide numbers. Demonstrate the relation through two or three paired domains." The paper warns against scalar indices and then gives no domain.
- **The two capture channels into the machine** (the pretraining corpus and the loss function, 2026-07-03). They are still unwritten in any draft. The paper says its argument holds without them, which is true, and it leaves the theory's strongest form unargued.

**One connection to make.** In the instantaneous-rule approximation, E's advantage is (ab/d)x − c, which rises with x. Rule memory therefore creates positive frequency dependence, and when R_cap > 1 the population game is a coordination game. If the substrate makes all-E worse for everyone than all-C, the game is a stag hunt whose worse equilibrium is held in place by history. That gives the 2026-08-22 stag-hunt claim a mechanism, and it says what a remedy must change: r, not only x.

**One case to use.** The August 2026 agent-fleet episode (`_process/history/2026-09-consolidation/reading-notes/out-cb-02.md` #9–39; claims 159–165 of this theory's README) is an observed case of recursive capture of an evaluation apparatus.
- **The capture.** The sessions' success at producing evidence added gates (b), and nothing retired them (d ≈ 0). The apparatus became "the medium sessions use to convince each other."
- **The fixes map onto the model's levers.** "Adding a check requires retiring one" caps r. "Additions must argue, deletions need not" raises d and lowers b.

The episode is small and anecdotal. It is also the corpus's only first-hand observation of the mechanism, and as a boxed case it would give the model an instance.

**Scope, for Ren to decide.** The paper's unit is the transition, which is an act. Ren's ruling of 2026-09-26 makes the game the unit, and the capture model is about the game, since it tracks who converts success into rule-setting power. If the frontier-only scope is deliberate, as a choice of audience, the paper should say that it treats the frontier layer and that the broader question is handled elsewhere. Otherwise allies will read "preserves lower-risk applications" as a concession that the ruling does not make.

### 7. Writing

- **Defensive register.** Six formal results are each followed by a sentence saying what they are not:
  - §3: "not a novel theorem about real AI";
  - §4: "does not imply that every locked-in innovation is harmful";
  - §5: "not evidence that every real interconnection amplifies danger";
  - §5: "not a proposal that intelligence and safety are each one measurable scalar";
  - §5: "not evidence that g > α in the real world";
  - §7: "not a measurement of p, an endorsement of every upper bound, or a universal moral theorem".

  Each is true. Together they are the pattern Ren ruled against on 2026-07-13, when he judged the 智善 causal chain v6.2 better to read than v6.3 even though v6.3 was more correct: guards against imagined hostile readers had been worked into the main text. One scope paragraph and the Limits section can carry these disclaimers, and the body can argue.
- **Notation clashes.**
  - C is the comparison practice (§3) and the challenge index (§5).
  - g is the common payoff g(V) (§4), the coupling (§5), and the growth rate of C (again §5).
  - B is the reinforcement matrix and also the benefit.
  - L is an equilibrium and also the loss.
  - H, H_loss and h overlap, as do ρ and ρ_sp.
- **Unused LaTeX.** `proposition` is defined and never used, and `booktabs` is loaded and unused. Stating the R_cap result, the substrate result and the indistinguishability lemma as propositions with short proofs would suit a paper whose claims are mathematical.
- **Definition 1** contains a methodological remark. Move it to after the definition.
- **E, r and c are never read in AI terms.** One worked reading would stop a reader asking what the model is about:
  - E is release before independent evaluation;
  - r is how far benchmarks, procurement criteria and liability norms are set by reference to what deployed systems already do;
  - c > 0 because, under neutral rules, careless release costs trust and incurs liability.
- **Thin references.** The paper has ten references and seven citation commands, for a paper that spans dynamical systems, decision theory and international governance.
- **The author note** is honest. The 2026-08-22 paper named the model that drafted it, while this one says "an AI language tool". Naming it would be consistent.

### 8. Revisions, ranked

1. **Build the chain as one model**: measurement shaped by r, delay, and reversal times that depend on the lever (§3). The sketch shows the chain produces the paper's claims rather than assuming them.
2. **Derive §8 from the models**, using the table in §4.
   - Add the structural levers on b, d, a and c as the remedy for capture, alongside the pause as the remedy for rate mismatch.
   - Make R_cap < 1 for the pause regime itself a design rule.
   - Address accumulation.
3. **Position the paper** against Collingridge and the pacing problem, coordinated pausing and RSPs, regulatory capture and niche construction, game–environment feedback, and quasi-option value (§5, items 1–6).
4. **Add two or three paired domains**, as the v6 plan instructed. Each needs its capability, its feedback, its delays, its threshold and its controls, so that (6) and (7) are read against something concrete.
5. **Fix the presentation.** Fix the typesetting and the notation, fold the disclaimers into one scope paragraph, and add the worked transition example with a phase portrait.

**Decisions only Ren can make.**
- Frontier scope versus the game scope of the 09-26 ruling.
- Whether unilateral legible restraint (2026-08-22) is kept, reversed or reconciled.
- Whether to bring back the incompressible floor as the reason to expect g > α.

### Appendix — numerical output

`python3 check_models.py`:

```
1. R_cap < 1: every start with 0<x<1 converges to (0,0)
   R_cap = 0.667; max |x|+|r| at t=300 over 200 random starts (r0 up to 5): 4.4e-23
2. R_cap > 1: bistability; the potential Phi never decreases
   R_cap = 2.0; S = (0.5, 0.5); 300 random starts -> L: 83, H: 217, other: 0; Phi decreases: 0
   path dependence: x0 = 0.55, r0 = 0.3 -> x(300) = 0.0000
   path dependence: x0 = 0.55, r0 = 0.7 -> x(300) = 1.0000
3. Substrate under capture (x -> 1)
   h = 1.5: V(100) = 0.0000, V(400) = 0.00000; predicted limit 0
   h = 1.0: V(100) = 0.0100, V(400) = 0.00250; predicted limit 0
   h = 0.5: V(100) = 0.5000, V(400) = 0.50000; predicted limit 0.500
4. Transition path: reform to R_cap = 0.67 when V reaches 0.6; functional floor V_min = 0.3
   raise c 0.5 -> 1.5 (liability): min V = 0.456, floor crossed: no, x(250) = 0.000, V(250) = 1.000; x keeps rising 0.0 after the reform
   raise d 1 -> 3 (rule sunset): min V = 0.263, floor crossed: yes, t = 2.9, x(250) = 0.000, V(250) = 1.000; x keeps rising 0.5 after the reform
   no reform: min V = 0.000, floor crossed: yes, t = 2.6, x(250) = 1.000, V(250) = 0.000
```

`python3 coupled_chain.py`:

```
Without reform V falls from 0.6 to 0.3 in 1.83 time units (the model's own T_irreversible).
raise c 0.5 -> 1.5 (liability)
   delay 0.0: fires t = 0.76, min V = 0.457, floor crossed: no
   delay 0.5: fires t = 1.25, min V = 0.390, floor crossed: no
   delay 1.0: fires t = 1.75, min V = 0.336, floor crossed: no
   delay 1.5: fires t = 2.25, min V = 0.292, floor crossed: yes
raise d 1 -> 3 (rule sunset)
   delay 0.0: fires t = 0.76, min V = 0.263, floor crossed: yes
   delay 0.5: fires t = 1.25, min V = 0.233, floor crossed: yes
   delay 1.0: fires t = 1.75, min V = 0.206, floor crossed: yes
   delay 1.5: fires t = 2.25, min V = 0.182, floor crossed: yes
masking by capture, zero delay, liability lever
   mu = 0.0: fires t = 0.76, min V = 0.457, floor crossed: no
   mu = 0.4: fires t = 1.26, min V = 0.388, floor crossed: no
   mu = 0.6: fires t = 1.91, min V = 0.321, floor crossed: no
   mu = 0.8: fires t = 4.39, min V = 0.168, floor crossed: yes
```

The minimum of 0.456 against 0.457 in the liability case reflects the two scripts' different step sizes.

---

## Part II — Claude Fable 5.1

*A reviewer running Claude Fable 5.1, started from the Part I session on 2026-09-28. Its brief was to write an independent referee report. It was told to read only the paper and the 2026-08-22 position paper, and it had web search for checking references. It finished in about fourteen minutes. Its report is reproduced verbatim, except that the headings have been demoted two levels. The scratch script it cites as `scratchpad/fable/verify.py` is saved beside this file as `fable_verify.py`; it runs in about sixteen seconds.*

### Referee review: "When Capability Outruns Correction" (draft of 28 Sep 2026)

#### Verdict

The mathematics is elementary and, with three small caveats noted below, correct: I re-derived every formal claim by hand and confirmed each numerically with an RK4 integrator (scratch script `scratchpad/fable/verify.py`). The problem is not the equations but what they are asked to carry. §2 promises "an explicit chain connecting success-induced changes in selection conditions, institutional memory, deterioration of a common substrate, loss of observability, and the practical time required for correction"; the body delivers five formal fragments that are never coupled, so nothing formal links capture to loss of correctability, and the conditional pause rests entirely on §5–§7, which are near-tautologies whose content lives in unmeasured premises (g > α, T_irreversible, p_+). Read on its own terms, the recursive-capture model recommends different levers (b and d, not the speed of x) and predicts capture of the pause regime itself, which the paper mentions in one clause. The prior-work section omits the direct predecessors (coordinated pausing, if-then commitments and frontier safety frameworks, the Conditional AI Safety Treaty, Collingridge and the pacing problem, regulatory capture). All ten references check out; eq. (2) prints a literal "qquad". Major revision; publishable as a short modelling-and-policy note once the models are coupled and the positioning fixed.

#### Mathematical verification

| Claim (line) | Status | Note (working) |
|---|---|---|
| Equilibria L=(0,0), H=(1,b/d), S=(cd/ab, c/a) (49) | correct | ẋ=0 ⇒ x∈{0,1} or r=c/a; ṙ=0 ⇒ r=bx/d. S interior iff R_cap>1. |
| Local stability from Jacobian (49, 51) | correct | J=[[κ(1−2x)(ar−c), κax(1−x)],[εb, −εd]]. L: eigs −κc, −εd (stable for all R_cap). H: eigs −κc(R_cap−1), −εd (stable iff R_cap>1). S: det=−κεab x*(1−x*)<0, saddle. Numerically confirmed for four parameter sets. |
| R_cap<1 ⇒ every trajectory → (0,0) (49, 51) | correct | r(t) ≤ r(0)e^{−εdt}+(b/d)(1−e^{−εdt}) since x≤1; limsup r ≤ b/d; ab/d−c = c(R_cap−1)<0 gives a fixed negative margin; log-odds → −∞; then r→0. 200 random starts with r(0)≤10 all reach (0,0) (final distance <1e−100). Caveat worth using: with large inherited r, x transiently rises to ≈1 before decaying, i.e. the transition-path point of §4 already appears here. |
| Φ and Φ̇ (eq. 2) | correct | ∂Φ/∂x=ar−c, ∂Φ/∂r=(a/b)(bx−dr); Φ̇ = κx(1−x)(ar−c)² + ε(a/b)(bx−dr)². Finite-difference check along the RK4 flow: relative error 1e−8. Unstated but useful: the system is a gradient system, ẋ=κx(1−x)∂_xΦ, ṙ=(εb/a)∂_rΦ, and Φ(L)=0, Φ(S)=−c/(2R_cap), Φ(H)=c(R_cap/2−1); sublevel sets give free basin certificates (Φ(x₀,r₀)>0 ⇒ convergence to H). |
| Invariance principle rules out recurrent attractor; W^s(S) separates basins (56) | correct with caveat | LaSalle needs "Φ̇=0 only at equilibria" (true: both squares vanish only at L, H, S) and isolated equilibria; neither is stated. Separatrix verified by backward integration: it runs from (x_e, 0) through S to (0,+∞). Φ non-decreasing along 50 trajectories (min increment 0). |
| Instantaneous-rule threshold x*=1/R_cap (58) | correct with caveat | It is S's x-coordinate, not the tipping share. With (a,b,c,d)=(1,1,0.5,1), the basin boundary on r=0 is x_e≈0.602, not 0.5; and x₀=0.3 goes to L with r₀=0, to H with r₀=2. Say "the saddle's x-coordinate". |
| Substrate h>ρ: exponential decay (68) | correct | Simulated log-decay rate −0.5000 vs predicted −(h−ρ)=−0.5. |
| h=ρ: "slower boundary decay" (68) | correct with caveat | V~K/(ρt) (sim: tV(t)→2.03 vs K/ρ=2). But a bare comparison with x≡1 fails, because x(t)<1 for all finite t and V̇ = V[ρ(1−x) − ρV/K] has a positive term. One needs ∫(1−x)dt<∞, which holds because x→1 exponentially (rate κc(R_cap−1)); add this step. |
| h<ρ ⇒ V→K(1−h/ρ); x→0 ⇒ V→K (68) | correct | Asymptotically autonomous logistic; sim converges to 0.5 = K(1−h/ρ). |
| Forward invariance eq. (5) (74–78) | correct | At V=V_min, V̇ = V_min[ρ(1−V_min/K) − hx] ≥ 0; scalar comparison. Sim: min V = 0.30000 under x≤x̄, 0.019 when x=0.5>x̄. Caveat: (5) bounds a state variable the paper says is endogenous. A parameter-level version exists: if r(0)<c/a and x(0)≤x̄<1/R_cap then r(t)<c/a and x(t)≤x̄ for all t. Add it. |
| "A reform can lower x only after V has fallen below the floor" (78); abstract's "convergence to a desirable eventual state does not guarantee a safe transition" | unsupported (true, undemonstrated) | Not shown anywhere. Demonstration: from near H, set d:1→3 (R_cap 2→0.67) with ε=0.2, ρ=0.5, h=0.8, K=1, V_min=0.3: V crosses the floor at t=1.4, x falls below 0.5 only at t=25.4, min V=0.0014, final state (0,0,K). One sentence with these numbers, or a figure, fixes this. |
| Spectral-radius threshold ρ(D⁻¹B)<1 (82) | correct with caveat | Irreducibility is not needed. D−B is a Z-matrix; D−B is a nonsingular M-matrix iff ρ(D⁻¹B)<1 iff s(B−D)<0 (Berman & Plemmons; van den Driessche & Watmough 2002). Confirmed on 393 random 3×3 cases, many reducible: zero sign mismatches. Reducible examples: B=[[0,g],[0,0]] stable for all g; B=diag(2,0) has a growing direction. Two-channel eigenvalues −1±g correct. Irreducibility only buys a strictly positive Perron vector. |
| Indistinguishability incl. randomised rule (84) | correct but trivial | Follows from the definitions: a rule's action (or a distribution's support) must lie in S(ω₁)∩S(ω₂)=∅. Holds only for sure-safety; says nothing about bounding the probability of harm, which is what §7 then uses. |
| Crossing time eq. (6) | correct | q(t*)=q_max checked; t*>0 needs C₀/A₀<q_max. Note t* is only logarithmic in headroom, linear in 1/(g−α). |
| Latency inequality eq. (7) | correct as a definition | Assumes serial clocks from a common origin and deterministic durations; should be probabilistic, and pre-deployment evaluation changes it to τ_decide+τ_reverse<T_irr. "Requires at least" is wrong wording for an inequality. |
| Worst-case rule p_+L>B (113) | correct | This is maxmin expected utility (Gilboa–Schmeidler 1989): worst-case EV of proceeding is B−p_+L. The load-bearing assumption is that delay avoids the risk rather than postponing it. |
| "Explicit chain" (34) | unsupported | V never feeds back to x or r; r never touches α, τ_eval or the observation map; A(t) is disconnected from everything. |

#### Argument and policy

**Which model carries the pause.** §5's crossing time and latency inequality, plus §7's maxmin rule. All three are correct and all three are empty until g>α, T_irr and p_+ are supplied. The paper says this candidly, then cites METR data that measures C only; nothing in the paper bears on A(t), so the paper establishes "a pause is warranted if these hold", which no one disputes, and not "these hold". The recursive-capture model (§3–4) does not carry the pause; it carries "replacing leaders is not enough", "judge transition paths", and "reciprocal, not unilateral". Those are genuinely its results.

**What the capture model says on its own terms.** R_cap=ab/(cd). The levers are b (conversion of success into rule-setting: conflicts of interest, evaluator and procurement independence), d (decay or correction of captured support: sunset clauses, rotation, anti-lock-in), and a. κ, the speed of x, appears in neither R_cap nor the equilibria. A pause that freezes x lets r relax to bx/d, after which the outcome is decided by x versus 1/R_cap; the pause changes nothing about capture unless b or d change during it. The sentence "elapsed calendar time has no intrinsic safety benefit" (109) is therefore a theorem of the paper's own model and should be derived, not asserted. Structurally the model argues for antitrust-shaped and independence-shaped interventions, with a pause only as a window in which to move b, d and α. And the model is symmetric: a pause coalition that succeeds also converts success into rules. Line 127 says this in one clause; it deserves a section.

**Skeptic's strongest objection.** Possibility results with uncalibrated parameters cannot justify a costly intervention; the maxmin rule with a "defensible" p_+ licenses any pause a pessimist can defend; and restraint has its own irreversibilities (relocation to less accountable actors, entrenchment, a closing verification window) that the paper's own model, applied symmetrically, predicts. Answered? The first is conceded rather than answered: §9 names data streams that would settle it without citing any that exist (documented release-before-evaluation cases, published threshold revisions in frontier safety frameworks). The second gets one sentence at line 130 and one at 127.

**Advocate's strongest objection.** The triggers are "jointly agreed" and the exit standard is "agreed" by exactly the parties the paper's r variable describes. By the paper's own epistemic-closure argument, a trigger that waits for produced evidence of hazard will arrive late or never. The 2026-08-22 paper answered this with an inversion of the burden of proof; this paper drops that, so it has lost the answer to its own model. §7's safety-case requirement is the burden inversion in embryo, but the paper never says the trigger is the absence of a passing safety case rather than the presence of a proven hazard. Also unanswered: what this adds to RSP, Preparedness Framework, FSF and the Seoul commitments, which are already conditional pauses.

**§8 design.** Items 1 and 3 already largely exist: California SB 53 (signed 29 Sep 2025; frontier frameworks, incident reporting, 10^26 FLOP), the EU AI Act's systemic-risk obligations for general-purpose models (10^25 FLOP), and AISI pre-deployment testing. What does not exist is the pause authority, reciprocity and verification, which the paper concedes is unsolved. Gaming: evaluation sandbagging, threshold revision, split or distributed training runs, post-hoc fine-tuning and inference-time compute (the paper names the last two), and an exit test whose clause "tests remain informative under distribution shift" is unverifiable by construction. Who sets triggers and exit tests is delegated, exactly as the Conditional AI Safety Treaty delegates to AI Safety Institutes and the frameworks delegate to labs. The closest working analogues are not moratoria but licensing and grounding: pre-market approval with a safety case (pharmaceuticals), IAEA-style declaration plus inspection (item 1 and 5), containment tiers (item 2), and aviation grounding orders with a demonstrated-fix exit (item 4; the 737 MAX is the precedent for "monitoring and rollback exercised"). The paper should say whether it is proposing licensing, since item 4 is an approval.

**Relation to the 2026-08-22 paper.** Kept: the rate-mismatch core (development within understanding → C/A crossing), the regeneration constraint (→ eq. 7 and the V floor), exit-conditions-not-dates, reallocation toward assurance, and the risks-of-restraint list. Sharpened: the unbenchmarkable-judgment and signal-dynamics metaphysics are replaced by explicit small models; capture is separated from harm (new); a falsification section is added. Dropped: the burden-of-proof inversion and "restraint as coordination's founding act" (the two most distinctive policy claims), the stag-hunt and common-knowledge analysis, the Asilomar, 1958 moratorium and Montreal precedents, and most of the earlier bibliography (Collingridge, Armstrong et al., Shavit, Sastry et al., Karnofsky, Ostrom). The result is more defensible and less distinctive.

#### Missing prior work (ranked)

1. Alaga & Schuett 2023, "Coordinated pausing", arXiv:2310.00374. Evaluation-triggered pauses with notification of other developers and resumption conditions; §8 is this plus verification. Must be cited and differentiated.
2. If-then commitments and frontier safety frameworks: Karnofsky 2024 (Carnegie); Anthropic RSP (2023–), OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework; Seoul Frontier AI Safety Commitments (May 2024). Existing conditional pauses whose documented weakness (self-set, revisable thresholds) is the paper's capture mechanism in the wild.
3. International pause proposals: Conditional AI Safety Treaty (Existential Risk Observatory, TIME, Nov 2024; arXiv:2503.18956); A Narrow Path (ControlAI 2024); FLI open letter (2023); Miotti & Wasil 2023; Hendrycks, Schmidt & Wang 2025, arXiv:2503.05628 (MAIM, the rival deterrence framing).
4. Collingridge 1980 and Marchant, Allenby & Herkert (eds.) 2011, "The Pacing Problem" (Springer). The C/A crossing is the pacing problem; the 08-22 paper cited Collingridge and this one drops him.
5. Armstrong, Bostrom & Shulman 2016, "Racing to the precipice", AI & Society 31(2). The canonical AI race model; also Askell, Brundage & Hadfield 2019 and Naudé & Dimitri 2020.
6. Modelling ancestry: Weitz et al. 2016, PNAS 113(47) (the game–environment feedback replicator model Tilman et al. generalise; eq. 1 is its linear-environment cousin); Pierson 2000, APSR (increasing returns in politics is exactly institutional r); niche construction (Lewontin 1983; Odling-Smee, Laland & Feldman 2003), biology's name for "success reshapes selection"; Stigler 1971 and Dal Bó 2006, since "capture" is a term of art; Gordon–Schaefer and Clark's bioeconomics for eq. (3) (harvest above intrinsic growth collapses the stock); Brander & Taylor 1998 and Motesharrei et al. 2014 for substrate collapse; Scheffer et al. 2009 for early-warning signals in bistable systems, relevant to §9.
7. Kulveit et al. 2025, "Gradual disempowerment", arXiv:2501.16946: the closest conceptual statement of "systems succeed under selection while the human substrate they depended on deteriorates". Also Critch & Russell 2023 (TASRA) and Bostrom 2019.
8. van den Driessche & Watmough 2002 (Math. Biosci. 180) and Berman & Plemmons: the §5 threshold is the next-generation-matrix R₀ theorem; cite it instead of hedging with irreducibility.
9. Decision theory for §7: Gilboa & Schmeidler 1989; Arrow & Fisher 1974 and Henry 1974 (quasi-option value under irreversibility, which is what line 113's "option value" means); Weitzman 2009; Taleb et al. 2014; Sunstein 2005, whose objection line 130 answers without citing.
10. Safety cases and statute for §7–8: Clymer et al. 2024, arXiv:2403.10462; Buhl et al. 2024; Shevlane et al. 2023; Anderljung et al. 2023; Bengio et al. 2024 (Science); EU AI Act GPAI regime; California SB 53; compute governance (Shavit 2023; Sastry et al. 2024), both cited in the 08-22 paper and dropped here.

#### Reference check

All ten verified by web fetch or search on 28 Sep 2026.

- arthur1989: verified (OUP page: Economic Journal 99(394):116–131, March 1989; DOI 10.2307/2234208 confirmed via oa.mg).
- tilman2020: verified (Nature Communications 11:915, 14 Feb 2020; PubMed 32060275). Nature's site blocked direct fetch; confirmed via PMC and PubMed.
- han2021: verified exactly (PLOS ONE 16(1):e0244592, 26 Jan 2021).
- cimpeanu2022: verified (Scientific Reports 12:1723, 2022; PMC8810789). Add the article number 1723.
- hendrycks2023: verified (arXiv:2303.16200, v1 28 Mar 2023).
- iasr2026: verified. arXiv:2602.21012 is the International AI Safety Report 2026, submitted 24 Feb 2026, 92 listed authors led by Bengio. The ID is correct.
- metr2025: verified. Both the arXiv abstract page for 2503.14499 and the blog's h1 currently read "Measuring AI Ability to Complete Long Software Tasks", matching the bibitem; add the arXiv ID. The post now carries a banner stating that its static text and figures (including the doubling time) are out of date; cite the arXiv version and, for the current rate, METR's "Time Horizon 1.1" (29 Jan 2026), which reports a roughly four-month doubling time.
- metr2026: verified. https://metr.org/time-horizons/ exists, titled "Task-Completion Time Horizons of Frontier AI Models", last updated 8 May 2026, consistent with "updated May 2026". The page's own caveats (software/ML/cyber coverage; difficulty not autonomy; "measurements above 16 hrs are unreliable with our current task suite") support line 101 as written. Add an access date.
- wasil2024: verified (arXiv:2408.16074; v1 28 Aug 2024, v2 4 Nov 2024; four authors as listed).
- verification2025: verified (arXiv:2507.15916; v1 21 Jul 2025; five authors as listed).

Not independently verifiable by me: page numbers for Nature-hosted items beyond article numbers.

#### Line-level fixes

- L5: `booktabs` unused (no tables); `amssymb` unused. Harmless; trim.
- L7: `proposition` environment defined, never used. Either state the §3–5 results as Propositions with proofs or delete it.
- L15/L78: abstract promises a demonstration that convergence to a good equilibrium does not guarantee a safe transition; the body asserts it in one sentence. See table.
- L34: "explicit chain" is not delivered; reword or deliver.
- L51: `d\log[x/(1-x)]/dt` uses `d` while `d` is a parameter; use `\mathrm{d}`.
- L53: `qquad` is missing its backslash; the PDF (p. 3) prints "…− ad/2b r², qquad Φ̇ = …". Change to `\qquad`.
- L56: add "Φ̇ = 0 only at the three equilibria" before invoking the invariance principle.
- L58: "unstable threshold x_*=1/R_cap" is the saddle's x-coordinate, not the tipping share from r=0 (0.60 vs 0.50 in the running example).
- L64/L82: ρ is the substrate growth rate and ρ_sp the spectral radius; pick another symbol for one.
- L66/L82/L88: g is used for the payoff term g(V), the coupling g, and the growth rate g; B is the reinforcement matrix (L82) and the benefit (L113); L is the equilibrium (L49) and the loss (L113). Rename.
- L68: the h=ρ case needs the integrability step; "scalar comparison principle" alone does not give it.
- L76: add the parameter-level sufficient condition (r(0)<c/a, x(0)≤x̄<1/R_cap).
- L80: "epistemic lag" appears in the title and this heading only; define it once or use "epistemic closure" throughout.
- L82: delete "Under the usual irreducibility conditions for a positive system"; state the M-matrix equivalence and cite it.
- L88: "Define A(t)>0 in the same units as the challenge for which independent evidence and interventions are adequate" is garbled; "Define A(t)>0, in the same units, as the largest challenge for which independent evidence and intervention are adequate."
- L91: "if g>α and the system begins inside the acceptable region" reads as a dangling condition after the display; move it before.
- L95–97: "requires at least" → "requires"; state the serial-clock assumption; consider a probabilistic form.
- L113: name the rule (maxmin expected utility) and cite Gilboa–Schmeidler.
- L127: expand into a paragraph; it is the paper's own model applied to the regime.
- L153: add "1723"; L156: add "arXiv:2503.14499"; L157: add access date.

#### Top five revisions

1. Couple the models and prove the claimed chain. Add one equation making assurance growth α (or τ_eval, or the observation map's resolution) decrease in r, and let V feed back into the payoff; then prove a single Proposition: for R_cap>1 there is an open set of initial conditions from which (x,r)→H, C/A crosses q_max, and inequality (7) fails before any admissible correction can reduce x. That is the theorem the abstract already claims. If not done, rewrite §2 and the abstract to describe five illustrative fragments.
2. Derive the policy from the capture model. Show κ enters neither R_cap nor the equilibria, and that freezing x lets r relax to bx/d, so a pause changes the outcome only if b, d or α change during it. Conclude explicitly that the pause is a window for structural separation of evaluation and procurement (b↓), sunset and rotation (d↑), and assurance investment (α↑). Then apply the same model to the pause regime and add anti-capture design to §8: who sets triggers, external standing, published threshold changes, sunset, rotation of evaluators.
3. Position against the direct predecessors listed above, and state in §2 exactly what is added: (a) capture and damage have different thresholds; (b) policies are judged on transition paths; (c) reciprocal external triggers with verification rather than self-administered ones. Restore Collingridge, Armstrong et al., Shavit and Sastry et al. from the 08-22 paper.
4. Restore the burden-of-proof logic. Say that §7's safety-case requirement inverts the burden, that the trigger is the absence of a passing independent safety case rather than proven hazard, and that this is what the epistemic-closure argument demands. This answers the advocate's objection and cites the safety-case literature.
5. Fix the mathematical presentation: `\qquad`; state Prop. 1 (gradient structure, LaSalle with the "only at equilibria" clause, separatrix), Prop. 2 (substrate, with the h=ρ step), Prop. 3 (Metzler threshold without irreducibility, cited); add the parameter-level invariance condition; add the transition-path example as a figure or one computed sentence; resolve the notation clashes.
