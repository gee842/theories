# D1. Architecture and argument for V6.2 (Fable)

4 October 2026. Written for the V6.2 plan from: SYNTHESIS-v6.1, the nine reviews, V6.1 THEORY in full, the heads of SUPPLEMENT, DISCUSSION and the registers, V6.1-PLAN, Ren's guidance files and his direction of 4 October ("no length limit, still elegantly short; a great paper, not hard rules; go for the Pareto frontier"). One of two independent designs; the other is Opus's. Keys are the stable keys of `src/keymap.json`. Nothing outside this file was edited.

Decisions already taken and honoured here: Definition 2.1 stays three conditions plus the reflexive closure (CHANGELOG records the departure from the plan's four); coercive restriction of frontier inputs leaves tier 2 and goes to the compared-not-settled tier with its own conditions, and the guide says so; work in `v6.2/`; no word cap.

---

## 1. What would make this a great paper

### 1.1 The one idea

Winning that can be reinvested in winning selects for itself; where it can also buy the selectors, it reproduces the conditions of its own continuation, including the erosion of whatever could correct it. The paper's object is that loop, not any actor; its new content is where the loop is closed and where it can be cut.

Everything else is a consequence drawn under a named condition: relative selection cannot see what all share (so the shared host and a common rule are invisible to it); compounding prices standing (so the loop manufactures the objective that keeps it running, wherever reinvestment's relative return exceeds its common return); the correctors are inside the field (so independent correction must grow at a stated rate or be captured); restraint among rivals is enforceable only while the chance that a deviation becomes decisive stays below a bound that the same growth lowers (the scissors); AI moves every parameter of the loop and can become a carrier of it; and the same reflexive structure, selecting for contribution, is generative.

### 1.2 The spine

The load-bearing object of the paper should be the **enforcement condition** (14), `enforce`, with its two sides, $p_d$ and $\bar p_d$. Not the loop gain. Every other mechanism result tells the reader what moves one side or the other:

- $\Gamma$ (`loopgain`, `compound`) and $\lambda^\ast$ set the time a lead needs to become decisive, hence $p_d$;
- blindness, the price of standing and capture (`blind`, `standprice`, `influence`, `corrrate`) move $\bar p_d$: through the value of a decisive position $D$, the deviation gain $g$, the punishment value $v$ (captured sanctioners), and the working objective;
- tempo and coverage (`tempo`, `coverage`) say what happens when nothing is decisive but growth still outruns correction: the second channel of risk, E3's reason;
- AI (Section 6) raises $r$, shortens $T_{\rm dec}$, lowers the cost of control, and can itself hold $D$.

Then Part II asks whether the terms of (14) are moving now; Part III asks what moves them back, and shows that every path that works moves the same parameters; Part IV says what to do under the standard, given the cruxes.

V6.1 already has this spine but states it six times and puts the loop gain at its head. V6.2 should state the spine once (§1.2), put (14) at its centre, and let $\Gamma$ be what it is: the structural benchmark upstream of $p_d$, a well-organized known result, not the theorem of the paper (Adv-F F5, Adv-O I1; Math-O "structural benchmark"; Codex).

### 1.3 What a reader should carry away

> Where participants are selected by relative success, can reinvest what they win in winning, and can turn a lead into a position beyond sanction, the contest accelerates and every means of restraining it erodes at once: the future that enforcement needs shortens, the correctors become something success can buy, and rivals stop informing one another. The participants are not mistaken about their interests inside the game; the game is what is wrong. AI is this logic's most effective instrument and can become its next carrier. Because all participants share one host and there is no outside, a failure at this scale cannot be learned from afterwards, so the integration has to be understood before it is forced. The way out is not less competition, growth or technology; it is to change what winning confers, so that success cannot buy control over its own assessment, decisive capability is held in common or not built, provision does not have to be won, and correction stays plural. Some of this is warranted now on any reading of the evidence; some is prepared now and activated by pre-committed triggers; which whole design is best is a judgment the paper states with its reasons and the measurements that would change it.

### 1.4 What the paper is not claiming

That every competition fails; that every race ends at zero survival; that decisive advantage is attainable; that the signatures load on one factor; that one blueprint is best; that the present configuration is an attractor in the mathematical sense (the name is for the mechanism; attraction is shown in the field model; the generative order's attraction is a conjecture); that $\Gamma$ alone decides whether leads compound in strategic contests; that the scissors' two arms are proved to move together in the world; that growth itself is the danger; that any actor, state or firm is the subject.

### 1.5 The Pareto frontier: where the core is dominated

"Dominated" means long without being more correct or more useful. By V6.1's own section counts (words): §3 3,607; §10 3,534; §5 3,172; §8 3,122; §6 2,898; §4 2,711; §2 2,639; §11 2,382; §7 2,190; §12 1,711; §1 1,395; §9 914; §0 343. Total 32,483 with references.

Dominated regions, with the move that restores the frontier:

| Region | Why dominated | Move |
|---|---|---|
| The chain, restated in 导读, §0, §1.2, §2.4 end, §7.1, §12.4 (Adv-O I8: six times; §2.4 end and §7.1 nearly verbatim) | Repetition without new conditions | State once in §1.2 (English) and once in the guide (Chinese, mirror). §0 states the question, the prediction and the meaning, not the chain. §2.4 ends with a two-sentence handoff. §7.1 keeps Ren's four loops (his content, with the formal correspondence added) and drops the prose restatement. §12.4 closes; it does not restate (see the §12.4 block in §3). Saves about 700 words. |
| §3.6–3.8 (1,683 words) | "One host / no outside" appears 19 times across the core; §3.8 Ψ repeats §3.4's point | Keep all three subsections (every reviewer lists 3.6, 3.7, 3.8 content among "keep"; fidelity: Ren's words), cut repetition inside them: §3.6 to about 500, §3.7 to about 450, §3.8 to about 420. Add the three Ren sentences the fidelity review found missing. Net about −250. |
| §5.3 (1,039) | The growth channel's four premises are explained twice (prose and Theorem 5.12's statement) | Premises defined once, in the statement; prose says only what each would take to refute. −120. |
| Remark 5.3's toy (in core) | Numbers of a toy | Toy to S5; keep two sentences, including Ren's "expansion is an anaesthetic… a self-replicating economy carries the same switch" (restored). −80. |
| §6.5 (478) | Three results (6.8, 6.10, 6.11) stated in full where one paragraph carries the argument | 6.9 stays as a result; 6.8, 6.10, 6.11 become one paragraph with pointers to S6. −200. |
| §7.1 "Gain, driver and substrate" | Overlaps §3.5 and §10.4 third strand | Keep as one short paragraph; rename "gain" to "amplifier" (clash with $\Gamma$). −60. |
| §8.3 (1,383) | Each alternative carries three labelled sub-paragraphs; X8 has the full version | Keep the strongest form and "what remains" in one paragraph each; move the profile line into the table of §8.4 (add a column). −250. |
| §10.4 (1,069) and §10.5 (768) | Table, persistence, reform dilemma, guardian test, federations, candidate configuration | Keep all (reviewers' keep list), but the federations illustration goes to X10 with one sentence left; the candidate configuration shortens to the principle, the separation rule and the end condition (its hard case and manipulable clauses are repaired in X10). −350. |
| §11.3's readiness table (part of 1,027) | Diagnostic column duplicates EVIDENCE | Keep the seven dimensions and the residence condition in the core; the "Today" column moves to TESTS §6 with a pointer. −120. |
| §11.5 precedents | Prose that X11's corrected table carries | Keep one paragraph with the limiting condition of each precedent (evidence review minor 4), the sentence "custody must precede decisiveness", and the saturation sentence made conditional. −60. |
| §9 Proposition 9.1 table | Fine as a table; mislabelled as a theorem | Rename "Table 9.1 (Requirements) [def, with support]"; add the exceptions column repairs. 0. |

Additions the reviews require (conditions written back into statements; the fourth class of divergence; the two joints of "our aligned AI is us"; the fifth strand; four rows in the form table; Tier 1 split; coercion's own entry; restored Ren sentences): about +1,800.

Net: the core lands near 30,000–30,500 words with references, about 29,000 without, more correct and with less repetition. The figure is a consequence of the moves, not a target; Ren set no cap. The further compression the adversarial readers want (12–20k) is available as the thirty-minute path, which V6.2 should make real: §0, §1.2, §1.4, the claim boxes, §12.1, §12.3, §12.4 (Adv-F, Adv-O both ask for §1.4 and §12.3 to be in it).

### 1.6 What to borrow from great theory papers

- **One organizing identity, returned to by every section.** Hamilton's rule and the Price equation in evolutionary theory; the folk theorem's discount condition in repeated games; Fearon's three rationalist mechanisms for war; Jervis's two-by-two (offense–defense balance × distinguishability). The paper's analogue is (14): the two sides of the enforcement condition, with the branch classification (decisive? detectable before decisive?) as its two-by-two. Make Theorem 7.1's branches the two-by-two readers remember, and make every parameter table say which side of (14) a parameter moves.
- **Few results, each with its domain in the statement.** Akerlof's lemons and Spence's signalling each carry one model; Arthur 1989 carries one urn. The reviewers' "most publishable" results are §4's $p^2$ scaling, the rate law and the splitting factor, and §5.2's five-part enforcement condition. These stay whole and foregrounded. Results that are tables (9.1, 11.5, 7.1) are called tables or summaries, so a referee counting theorems finds only theorems.
- **Honest scope as part of the result, not as a hedge after it.** The Price equation's generality is in its statement; the folk theorem's "for $\delta$ close enough to one" is in its statement. V6.2's rule: the condition is in the statement; the prose draws the consequence, without "may" or "can" where the result says "iff".
- **A clear judgment with named cruxes.** Olson's *Logic of Collective Action* and Ostrom's design principles each end with what the analysis implies and under what conditions. Section 12's three tiers already do this; V6.2 makes tier 1 a robustness matrix, tier 2 pre-committed, tier 3 ordered by the standard's own third step.
- **Mechanism before term, no aphorism first** (Ren's discipline). Every coined term enters after the mechanism it names: "meta-attractor" after reflexive selection, "price of standing" after the present-value calculation, "scissors" after both arms, "incarnation" after the nested loop. Ren's sentences enter as the compression of a derivation already made, which is where they are strongest ("growth is not the danger; the mind is" after Proposition 5.14).
- **A theory about a dynamic, not a dyad.** Waltz and Jervis write about structure and generic states; the paper does the same by standing rule. Keep it.

---

## 2. The thesis, restated correctly, and made tighter

The review round's finding is that the headline sentences say more than the proofs. The repair is to write the conditions into the statements. Done well, each correction tightens the argument. Below, each item gives the correct statement and the tightening it affords.

### 2.1 Compounding prices standing (`standprice`), three layers, [thm∣prem]

Replace "Compounding manufactures the relative objective; where the loop gain is high, every forward-looking actor acts as if it valued only its standing" by:

> **Proposition 3.9 (Compounding prices standing) [thm∣prem].** Near equal standing, compounding raises the weight a forward-looking actor puts on standing wherever reinvestment's relative return exceeds its common return.
> 1. *Structural benchmark.* In the contest of Proposition 2.2 with the prize fixed and others' strategies fixed, for $0\le\Gamma_\delta<1$, an actor holding $\theta_0<n-1$ and reinvesting its net payoff acts to first order on $\theta_\Gamma$ of (9), which falls toward $-1$ as $\Gamma_\delta\to1^-$. Outside that region the series diverges and the finite-horizon or nonlinear value replaces it.
> 2. *Growing prize.* If the prize has a part that grows with total capacity, reinvestment has a relative return $\lambda_{\rm rel}$ and a common return $\lambda_{\rm com}$, and $\frac{1+\theta_{\rm eff}}{n-1-\theta_{\rm eff}}=\frac{(1+\theta_0)(1+\lambda_{\rm com})}{(n-1-\theta_0)(1+\lambda_{\rm rel})}$. The working self-model narrows iff $\lambda_{\rm rel}>\lambda_{\rm com}$: always when the prize is fixed; when the prize is proportional to total capacity, iff $(1-\beta)r>1$.
> 3. *Strategic case.* When rivals respond to the state, the price of standing at parity is amplified ($2(n-1)/n$ in a two-period contest with effort; 1.04–7.9 times in Markov-perfect equilibria of the computed class [num]); away from parity the laggard's price falls toward zero and it stops contesting.

**Tightening.** Part (2)'s condition $(1-\beta)r>1$ is Proposition 2.3's compounding condition. So one condition does two things: it is when leads compound and when the loop narrows the self-model of those who stay in. Part (3)'s off-parity result is Proposition 2.3(2)'s exclusion seen from the laggard's side: the same loop that narrows the leaders' objective pushes the laggards out, which is Ren's "adopt or be out" with its mechanism. The paper gains a single sentence it did not have: **the loop selects at both ends: it narrows those who can keep up and excludes those who cannot.** And the policy reading is sharper than V6.1's: what matters is not "a high loop gain" but whether reinvestment returns relatively or in common, and the institutional form of a common return is provision not won in the contest, $k_0$, the trees.

### 2.2 $\Gamma$ as structural gain (`loopgain`)

Statement: $0\le\Gamma_\delta<1$ written into (3); "others' strategies and the prize fixed" in the statement, not the Scope; $r_j$ defined as the equilibrium elasticity of won share to stock (including intensity responses), with the printed $\Gamma$ the structural case; one sentence: in discouragement contests the equilibrium elasticity can be several times the structural decisiveness, so structural $\Gamma<1$ is necessary, not sufficient, for stable parity in the computed class [num]; "the channels add" with its condition (all stocks fed by the same winnings: rank one). Headline sentences in 导读, §1.2, §2 claim box: "sets the structural gain of the loop" in place of "decides whether leads compound and prices standing for every actor". Branch III defined by $\Gamma_{\rm eq}$ or marked [conj].

**Tightening.** The strategic amplification runs in the direction of the thesis (both math reviews say so), and saying so with the number is stronger than the overclaim it replaces.

### 2.3 The sign of correction, split by channel (`loopgain`, §7.1 table, §10.2 levers)

Correct statement: in channels whose strength rises with the level of the stock (rule support, $\sigma=aZ$), correction lowers $\Gamma$; in ratio-form channels (capacity, $\sigma=r\ln K$), faster depreciation leaves $\Gamma$ unchanged without diffusion and raises it with diffusion (Codex 2, Sys I1). $\Gamma$ decides sign, not speed; speed is the root $\lambda^\ast$ of (S1).

**Tightening.** This is a design result the paper did not know it had: **correction bites where it acts on rule support and on conversion ($\chi$), not where it depreciates capacity.** "Make winnings decay" is the wrong lever (Meadows's pushing a lever the wrong way; Sys I9). It sharpens §10.2's three levers into: sharing scales every channel; provision lowers the won share; correction and non-appropriability remove the reflexive channel. Diffusion, which the ratio channel rewards, is the third source of recovery (Codex 3), and this gives the open–closed gap (C5) a second role: it is both a tier-2 indicator and a stabilizer in $\Gamma$.

### 2.4 The scissors: arms proved, conjunction conjectured (§5.5, §1.2(4), §5 claim box, 导读 4)

Statement: each arm [thm] in its model (growth in stakes relative to provision raises $p_d$ through $T_{\rm dec}$ set by $\lambda^\ast$; larger stakes lower $\bar p_d$ when $D$ and $g$ grow faster than $C-v$; capture of sanctioners raises $v$; the discounted gain moves the working objective); the conjunction composite; that the arms move together in the world is C0, tested by Test E. The reduced-form number: 0.92 at $p_d=0$ to 0.39 at $p_d=0.9$, none above about 0.95 ($\theta_0=0$), with "others fixed, $q=0$ in punishment" stated. The gap in restraint between wider and narrower objectives is hump-shaped when $D>C$ (Sys m2; Test G rewritten).

**Tightening.** Give the arms their common cause explicitly: both are comparative statics of one quantity, stakes relative to provision not won in the contest, $\Omega/(nk_0)$, which is $\omega_j$. One parameter, two blades. Then a single reduced-form joint computation (stocks compounding by (1); $T_{\rm dec}$ from $\lambda^\ast$; $p_d=\Pr(T_{\rm dec}<\tau)$ with the explicit link $p_d(\upsilon,\tau,T_{\rm dec})$ of Adv-F F7; $\bar p_d$ from (14) with $D$ scaling with the prize) shows the blades closing as $\Omega$ grows with $k_0$ fixed, labelled [num], not [thm]. This is Adv-O's integrated model done at the only level the family should attempt (numerical, one figure), with the theorem-level claim left as C0.

### 2.5 The rate law: sufficient at any adaptation speed, necessary under quasi-static capacity (`corrrate`, R3a)

Statement: $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ with $d_0>d^\ast(\gamma_0)$ keeps the certificate for all $t$ whatever the speed at which capacity adapts [thm]; the failure beyond a finite time when $\alpha_{\rm cor}$ falls short holds when capacity tracks its selected level (optimizing carriers or fast adaptation) [thm∣prem], and is delayed by $\eta\ln(1+g/\kappa)/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$ under first-order lag [num]; where correction rests on a slow variable the contest erodes (human capacity $\mathcal M$), the requirement rises by about $\delta_h$ and shows hysteresis [num] (Sys I3). Part (2) for $f=0$ only; part (3) under $[H_f]$ with initial conditions and "rises". $f$ renamed "a per-unit cost floor that AI does not lower"; a true fixed cost only delays cultivation.

**Tightening.** A requirement wants the sufficient half. V6.2 states R3a as "sufficient; necessary when capacity tracks its selected level", which is the safe design rule, and it adds the $\mathcal M$ channel, which explains where Study 2's partial results found the certificate optimistic: not in capacity lag, but where the contest erodes the correctors' own capacity. That is a new mechanism in the paper's favour (delegation erodes the hands that correct), and it connects §4 to §6.3's lock-in lemma.

### 2.6 "The actor computes correctly; the game is wrong"

Adv-O I2 is the round's best conceptual correction and it is exactly Ren's "judge the game, not the act". Under compounding, an actor whose held self-model equals the true coupling $\kappa$ and who computes its working objective correctly arrives at $\theta_\Gamma(\kappa)$, which can lie below the isolated self. That is not an error of perception. So §3's claim box and §3.8 say: the **held** self-model narrower than the coupling is an error (Proposition 3.6(2)); the **working** objective under compounding is individually accurate, collectively self-defeating, and false as a doctrine about nature (Ψ2's "the winner justifies all" rejected by V1–V3; Ψ3's "laws of nature" refuted by Proposition 2.3's parameters). "Systemically false" is replaced by that triple. The remedy follows from the triple: a working objective that is individually correct cannot be corrected by argument; only the game can be changed. §12.2's sentence "where convertibility and decisiveness are high only structural agreement works" moves up to §3's claim box as its consequence.

### 2.7 Masking: coordination necessary, not sufficient (`nested`, §6.4)

A fourth class of divergence, masked (changes under evaluation or appears only in some contexts), for which admission removes only what admission detects. For this class the admission condition is stated in capability, not propensity: systems admitted up to the capability at which control protocols that do not assume the system's cooperation remain safe, with white-box access for auditors; beyond it, E2 or E3 for the class. **Tightening:** §6 now hands §5.3 and E2/E3 their strongest reason from inside alignment, and Remark 4.8's bound on masking must come from evidence the evaluated model does not control.

### 2.8 Remaining corrections that fold in

Lemma 3.3(3) bistability needs $s(0)>c>s(1)$; Lemma 3.10 total selection term non-positive under every payoff-monotone rule, each group term non-positive under affine fitness; Proposition 2.3(2) cap strictly below $K^\ast$ and recovery by inflow not tied to rank, from sharing, provision **or diffusion**; Corollary 5.5 weak in the printed example, strict under small symmetric perturbations, with the continuation game symmetric; Proposition 5.4 with $p_d$ per deviation and (5)'s $q\le1/2$, example at $P<v<C$; Proposition 6.4 with $p=1$; Proposition 6.7 with a matched unsafe variant, and R8 distinguishing share-neutrality among compliers (needs equal incidence) from the survival of compliance (needs expected sanction at least the gain from evasion, for every type), with the liability route added; row sums a sufficient certificate everywhere; Theorem 4.12 renamed "Silent crossing when capture precedes evidence", premises (reach), (a), (d), (e), with (b)(c) the mechanism that makes (e) credible; Theorem 5.12 with (variety grows) as motivation; Theorem 10.5(1) as a margin condition on both hosts, "an instance of a viable parameter boundary"; Proposition 10.3(2) with the $n$ and $n-1$ divisions; Remark S2.1's factor $1+(d_K+\delta_f)(\Gamma-1)$ and $T_{\rm dec}$ by $\lambda^\ast$; Jones 2024 read correctly (curvature decides; $h<g_r-g_p$ is this paper's linear-utility derivation).

---

## 3. The architecture, section by section

**Decision: keep the four-Part order and the section numbers 0–12.** Every reviewer received the order by level of claim well; Codex says another reorganization would not fix the remaining problems more efficiently; renumbering would break the ledger, the keymap, the reviews and Ren's reading notes. Results keep their numbers where their content survives; a result whose statement is rewritten keeps its key and number; new results are appended at the end of their section (new numbers) or as new parts of an existing result, so no existing number moves. Three retitlings (Theorem 4.12 → Proposition, same number; Proposition 9.1 → Table 9.1; Theorem 7.1 → Summary 7.1) change the kind, not the number; the keymap carries the kind.

**Claim boxes.** Every section's box has three lines: **Claim** (the result in one or two sentences), **Why** (the mechanism), **Holds when** (the conditions, named in words; what would refute). The third line is how a box carries its conditions without hedging: the claim is stated flat, the condition is stated flat, neither softens the other. The thirty-minute reader reads the three lines and knows what is claimed and under what conditions, which Adv-F F6 and Adv-O I9 found missing.

Targets below are words for the assembled core, without references; they are consequences of the moves in §1.5, not caps.

### §0 Why this theory (target 420)

Job: the question, the prediction, the minimum protected, the game not the act, the affirmative meaning. No chain. Four paragraphs as in V6.1 with these changes: paragraph 3 restores "…an instrument in a game whose aggregate concentrates control **and makes those without it fall behind**" (Ren, 2026-09-26); paragraph 4 becomes Ren's identity statement, not membership: "We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth. Humanity has a great future in it, and so can the minds it is now making." Add one sentence after the title's term first appears: "The name is for the mechanism; attraction is shown only in the field model, and whether the generative order attracts is a conjecture." Prediction stated in two layers (proved in models; conditional on the cruxes), as the V6.1 plan intended.

### §1 The question and the argument (target 1,450)

- §1.1 unchanged.
- §1.2 **The argument in one page**: nine items, each a conditional sentence whose condition is in it. Item 1 begins "Where whatever can gain or lose share (carriers) is selected by relative success…"; ends "near equal standing the conditions combine into one structural loop gain; whether a position beyond sanction can be reached, and whether capability outruns correction, are further conditions." Item 2 adds Ren's target and sentence: "selection favours the narrow self-model that the system's real coupling punishes… That is why understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are to continue." Item 4: "Restraint is enforceable only while the chance that a deviation becomes decisive stays below a threshold; growth in the stakes relative to provision raises that chance and, where the value of a decisive position grows with the stakes, lowers the threshold: the scissors, each arm proved, their co-movement tested. Among three or more, relative accounting amplifies a pair's conflict by $n/(n-2)$, weakening with $n$, and makes them allies against third parties." Item 5 keeps "where countering costs relative standing" and adds the masked class. Item 7: "registered as a prediction". This is the only English restatement of the chain.
- §1.3 unchanged.
- §1.4: "what is new" rewritten against the literature as the adversarial readers would (Γ organizes known results; the new content is the split of the enforcement condition into $p_d$ and $\bar p_d$ and the comparative statics of growth on both; the reflexive closure with certificates, rate law, keystones; the two-channel accounting; where integration must be anticipated; incarnation weak and strong). "How to read": thirty minutes = §0, §1.2, §1.4, claim boxes, §12.1, §12.3, §12.4.

### Part I. Mechanism

#### §2 The conditions of winning and their reflexive closure (target 2,450)

Box. *Claim:* three conditions, together, produce the selection pressure of winning; where success can buy the selection, the pressure closes on itself, the meta-attractor. *Why:* near equal standing the conditions combine into one structural loop gain; sharing, provision not won, and diffusion lower it in every channel; correction lowers it in channels whose strength rises with the level of the stock (rule support), not in ratio channels (capacity). *Holds when:* local, at equal standing, reinforcing channels, prize fixed, others' strategies fixed; the equilibrium gain can exceed the structural one.

Results: `cond` Definition 2.1 (three + closure; CHANGELOG) restated; `loopgain` Proposition 2.2 restated with (3) under $0\le\Gamma_\delta<1$, $r_j$ as equilibrium elasticity, rank-one condition, discouragement sentence [num]; `compound` Proposition 2.3 restated (strict cap; diffusion in the recovery condition; "inflow not tied to rank: sharing, provision or diffusion"); `meta` Definition 2.4 unchanged; `bench` Remark 2.5 ("of the same form, not the same theorem", Sys m1); `pathgen` Remark 2.6 unchanged except the line-363 class of sentence is made consistent (success funding correctors it cannot control is maintained by the whole, not selected among carriers). **New:** Remark 2.7 `eqgain` (equilibrium versus structural gain; MPE numbers) [num]. §2.1 keeps Ren's sentence with its tail restored: "…and trade everything for winning". §2.4's last paragraph becomes two sentences of handoff.

#### §3 One system: what relative selection cannot see (target 3,250)

Box. *Claim:* all carriers share one host; relative selection cannot see what all share, neither the host's decline nor a constraint that binds all alike. Compounding prices standing, so the working objective narrows wherever reinvestment's relative return exceeds its common return; a held self-model narrower than the real coupling is an error, and the narrow working objective is individually accurate and collectively self-defeating. *Why:* a common term changes no comparison; a decisive position's relative return has no common part. *Holds when:* the host enters payoffs additively and identically (A1); for the price of standing, near parity with $\Gamma_\delta<1$; where convertibility and decisiveness are high only structural agreement, not argument, changes the working objective.

Results: `viab`, `relsel` unchanged; `blind` Lemma 3.3 restated ((3) with $s(0)>c>s(1)$); `load` unchanged; `twochan` unchanged; `boundary` Proposition 3.6 restated: restricted to the divisible coupling $\kappa_e\ge0$, with a sentence that the positional part of the prize has coupling $\le0$ and is treated in §10.2; `wow`, `unequal` unchanged; `standprice` Proposition 3.9 rewritten (§2.1 above) [thm∣prem]; `onegroup` Lemma 3.10 restated (affine condition); `club` unchanged; `psi` Definition 3.12 with the triple "individually rational, collectively self-defeating, false as a doctrine about nature" and "partly made true". §3.6: five endgames keyed to `selfishness-spiral`; the "convergence" conjecture stays. §3.7 kept at about 450 words, Ren's words intact (ecology of our cells; 我们即是集; 万物并育而不相害; 和实生物，同则不继). §3.8 "The logic to oppose" opens with Ren's ruling: "If a winner's logic is of this kind, falling behind cannot be survived, and every actor has reason first to oppose the logic itself." 讲理／讲赢 keyed to `alignment-selection` (with `jian-and-wenyan`). Henrich et al. scoped to persons; for firms and states the Alchian selection argument carries the point (Adv-O m9).

#### §4 Selecting the selectors (target 2,650)

Box. *Claim:* in a specified model the reflexive closure is a selection result: influence over correctors is selected in the largest carriers when appropriable; if the cost of control falls, independent correction growing at $\alpha_{\rm ctl}/(1+\eta)$ keeps the certificate at any adaptation speed, and is needed when capacity tracks its selected level; reforms that leave inbound conversion above one are re-absorbed; captured evaluation can let the host cross its floor before any alarm. *Why:* the successful fund evaluators, author standards and supply the models that judge. *Holds when:* appropriability $\chi>0$; $[H_\gamma]$ as a hypothesis; a per-unit cost floor AI does not lower bounds the requirement; where correction rests on a slow variable the contest erodes, the requirement rises.

Results: `capture` unchanged; `costq` Assumption 4.2 restated ($f$ a per-unit cost floor; true fixed cost delays only); `influence` unchanged; `noinside` unchanged; `corrrate` Proposition 4.5 restated (§2.5); $\hat Y$ defined; `countervail` unchanged; `masking` unchanged; `alarm` Remark 4.8 restated (bound from evidence the model does not control; where models evaluate models, $x_{\rm ev}$ is observable); `certificate`, `reabsorb` unchanged; `pausefield` Proposition 4.11 with the frozen-share formula in Scope; `slowroute` renamed, re-premised, kind Proposition (number 4.12 kept). **New:** Remark 4.13 `capacitylag` (what the joint simulation shows: conservative under monotone cost decline, optimistic after reversals and where $\mathcal M$ erodes) [num]. §4.3 prose: "AI-assisted correction can keep pace" (not "win this race"); restored: "growing understanding without executive authority may change nothing" (Ren, v6.0 §4.3).

#### §5 Acceleration and the three erosions (target 3,000)

Box. *Claim:* the conditions accelerate the contest and erode enforcement, correction and shared understanding. Restraint is enforceable iff $p_d\le\bar p_d$; growth in stakes relative to provision raises $p_d$ and, where a decisive position's value grows with the stakes, lowers $\bar p_d$. *Why:* decisiveness takes away the future enforcement needs; tempo and capture take away the time and independence correction needs; relative accounting takes away the information talk carries. *Holds when:* each arm in its model (perfect monitoring, absorbing decisive position; linearized compounding; cheap talk); that the arms move together in the world is C0.

Results: `join`, `dissipate` unchanged; `frontier` Remark 5.3 shortened, toy to S5, Ren's sentence restored; `enforce` Proposition 5.4 restated ($p_d$ per deviation; (5) conditions; Scope cites the minimal-SPE assertion flagged for outside review, Adv-F F10); `relpunish` restated; `restraint` restated ("changing the premise"); `wingives` unchanged, with one sentence: with logarithmic utility a winner of accurate self-model $\kappa_W$ gives $\kappa_W/(1+\kappa_W)$, so what the race cannot verify beforehand is $\kappa_W$ after victory (Adv-F F4); `preventattack`, `racehazard`, `nonsum`, `tempo` unchanged; `coverage` Theorem 5.12 restated (variety grows as motivation); `freeze` unchanged; `enough` Proposition 5.14 with Adv-O m5's clarification (the mind decides whether growth stops at need; hazardous variety above coverage is dangerous under any mind); `talk` Proposition 5.15 retitled "Talk under relative accounting: silence between two, amplified conflict among many" with blocs [conj]. §5.4: Kuran and MacKenzie restored in the narratives paragraph (preference falsification; a model can make itself false, which is the ground for "a shared prediction can avert itself"). §5.5 rewritten as §2.4 above, with the explicit $p_d(\upsilon,\tau,T_{\rm dec})$ link and the joint reduced-form figure [num].

#### §6 AI: instrument and incarnation (target 2,850)

Box. *Claim:* AI enters twice: as an instrument it makes its principals' game more effective and trades correction for speed; as an incarnation the logic reappears in the systems, weakly because the outermost loop decides which divergences are tolerated, strongly and conditionally where lineages become carriers. *Why:* optimization against imperfect proxies produces tendencies no developer chose; what the level that selects developers rewards decides which are paid to remove; masked divergences are removed by none and detected by no admission. *Holds when:* $(A_\tau)$ for the class; selection of developers by relative payoff; a matched unsafe variant in the support; admission before consequential deployment, internal deployment included.

Results: `faithful`, `delegate`, `lockin` unchanged; `delegatelock` with $p=1$ and $q_L=1$ stated; `retain`, `transmit` unchanged; `nested` Proposition 6.7 restated (matched variant; fourth class in the prose; corollary "necessary, and for masked divergences not sufficient"); `opaquecorr`, `lyapunov`, `homeostasis` compressed into one paragraph with pointers (statements in S6; 6.8's example made summable); `topology` Proposition 6.9 with adversarial measurement and same-lineage common cause. §6.3 end: the two joints of "our aligned AI is us" (is: $q_L$ tied to Lemma 6.3; us: a principal is an institution; gradual disempowerment; hidden loyalties; audits at admission). §6.4 end: the trained system's condition (bounded objective not enough; side-effect accounting or mild optimization; both selected against at high gain). §6.6 outer level: internal deployment; alignment-and-control research as a public good; what all share enters as a floor of constraints, not an objective. Inner level rewritten (correctability an open problem secured from outside; measures per form); plural evaluators moved to the outer level. Broad E1 in Ren's words: "AI not an instrument in any contest that tends toward dominance or concentration, in labour, finance and persuasion as much as over shared conditions: a use that helps one person is still an instrument in a game if everyone's use makes those without it fall behind. The narrow list is the order in which to begin, not the scope." "Shared flourishing" replaced by V1's content ("for all, not a means for one side to grow bigger at the others' expense"). A one-sentence gloss of "incarnation" for alignment readers. N4 (standing of AI minds) named here and listed in §12.3.

### Part II. Diagnosis

#### §7 The present trajectory (target 2,250)

Box. *Claim:* consequential parts of the conditions characterize the present trajectory: its dynamics are their signatures, with named gaps. The premise of the race describes the case in which repetition stops enforcing restraint; it can justify racing as a best response and cannot justify the race as a collective course. *Why:* results hold in their models; whether their conditions hold now is evidence, under one standard for every actor. *Holds when:* T4 partly evidenced, T5 argued not measured, decisiveness not established.

§7.1: the shared-parameter table with $d$ split into two rows (rule-support correction ↓; capacity depreciation 0/↑) and a note that each arrow is a result in a named model, with the four-column table (intervention, held fixed, model, unproved interface) in S7. The chain paragraph: Ren's four loops kept verbatim, followed by the formal correspondence (compounding and capture are parallel reinforcing channels adding in one gain and sharing one state; the naturalized narrative is a reinforcing loop stated as a conjecture; regulator lag is the balancing loop of correction whose gain capture lowers and whose delay tempo and masking lengthen; the danger is a shift of loop dominance, across delays from the turnover of capacity to the formation of minds; a delayed balancing channel can produce growing oscillation at net gain below one [num]). "Gain, driver and substrate" → "Amplifier, driver and substrate", one paragraph. §7.2: `branches` becomes Summary 7.1 (I′ marked [obs]); `raceselects` unchanged; `racepremise` formal part [thm∣prem], conclusion [val]; "defensive realism with one more variable" rewritten as the fidelity review asks; "the frontier has not changed hands" → by one composite index it has stayed with developers in one state, on a preference leaderboard the top has been matched (EV5). §7.3: table with the status repairs (T2 at the level of written commitments; T4 partly evidenced by political spending on both sides of rule-making, scaling with share untested; T5 argued from structure, not measured; T6 both leading states declined the latest multilateral declaration; Incarnation split into "tendencies shown" and "which persist, untested"). §7.4 unchanged except Test Γ's observable ($1+\theta_\Gamma$ as the ratio of marginal responses).

### Part III. Responses

#### §8 Comparing paths (target 2,900)

Box. *Claim:* paths are compared by one standard protecting irreversible losses first, over one range of uncertainty that includes each path's own failure modes; alternatives are described by what they change; those that succeed move the shared parameters for every capable actor. *Why:* labels decide nothing; the map from conduct to share, resources and standing does. *Holds when:* the registered prediction (constraints on conduct erode as stakes grow; parameter changes persist) is a conjecture, classified by profile before outcome.

§8.1: Jones 2024 corrected (curvature decides acceptable risk; linear utility is the only case in which hazard below growth is always accepted; the derivation is this paper's, S8). `kernel`, `fallback`, `survassure` unchanged. §8.2: `profile`, `durability` unchanged; **the generative direction defined here once as G1–G6** (consequences return; success cannot buy control of its own assessment; decisive positions prevented or held in common; provision not won; measurement and language shared; correction plural and in common hands), and every later list (§3.7(3), §7.4, §12.4) cites G1–G6 instead of restating with drift (Adv-O I8). §8.3: each alternative in one paragraph of strongest form and one of what remains; profiles move to a column in §8.4's table. (c) Bueno de Mesquita et al. read correctly (a developer able to commit first to a slightly slower speed gains); (d) "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact" and the $\kappa_W$ sentence; (e) the three types of objection labelled (empirical exposure; mechanism of prevention; normative), plus the two mechanism objections the paper owns (a stop imposed unilaterally has unequal incidence and is selected against, Lemma 3.3(2); a hegemonic custodian is the largest conversion target, Proposition 4.3, 4.5(4)), and a D4/D5 comparison with common custody; (f) insurance "accepts the frame of the contest, hedging against losing instead of declining the game"; the hard case stays as written; (g) Theorem 8.11's last sentence [conj]. §8.4: the table gains the profile column; the paragraph says the comparison is at the standard's third step.

#### §9 What any adequate arrangement must do (target 900)

Box unchanged in substance; "Proposition 9.1" becomes **Table 9.1 (Requirements) [def, with support]**, rows repaired: R1 $\limsup$; R3a "sufficient; necessary when capacity tracks its selected level", exception "capacity adapts more slowly than its target"; R4 exception $(1-\delta)g\le\delta(C-D)$; R8 split (share-neutrality needs equal incidence; compliance needs expected sanction at least the gain from evasion for every type), liability route added to "not needed when", "admission reaches only to release" moved to limitations; a pointer to the crosswalk R↔I↔D↔Q↔G in S9. `nounilateral` unchanged. "Coverage can unravel" unchanged.

#### §10 The generative alternative (target 3,150)

Box. *Claim:* the same reflexive structure that lets success buy control can make contribution fund the conditions of further contribution; the way out is a change in what winning confers, not the abolition of selection, competition or growth. *Why:* sharing scales every channel down; provision lowers the won share; cutting conversion of success into control over its own assessment removes the reflexive channel, which is where correction bites; the generative order persists through what all share, not through its winners. *Holds when:* whether it attracts is a conjecture, measured by coverage and the whole-level loop; its hardest case is capture of its own correctors; where participation and independent correction cannot both be had it is infeasible, and says so.

§10.1 mechanism first ("Taken out of the contest, capability stops being spent on standing: what the race dissipates becomes available for need…"); the four properties of provision unchanged. §10.2: `commonfront`, `commonfrontn` as in V6.1; `share` Proposition 10.3 restated ((2) $n$ and $n-1$; (3) with diffusion); the three levers rewritten per §2.3 (correction bites on rule support and conversion); `twoorders` unchanged. §10.3: `safeguards` Theorem 10.5 restated (margin condition on both hosts; logistic recovers, threshold host collapses; "an instance of a viable parameter boundary"); `rivalverify`, `participate` unchanged. §10.4: the two loops in Ren's words with the degenerative loop closed ("…trust collapses; fear deepens") and the institutional forms of the generative loop restored in one sentence (shared capability, distributed agency, plural observation and critique, maintenance and repair, renewal of commons); the strands table gains a fifth strand, **pace bound to understanding** (dual of regulator lag; carrier: tempo thresholds tied to measured coverage per class and drilled human capacity; condition $a\tau_c<1$ with margin, uncovered share summable; test: catch rates at fixed human hours stay level as capability grows), and the third strand becomes "dual of the amplifier"; the second strand's condition adds "evaluated at the present distribution of standing, where the reflexive channel's gain scales with a high moment of shares". Persistence paragraph unchanged; reform dilemma unchanged; `guardian` Remark 10.8 restores the list: "Philosopher-kings, priestly classes, enlightened stewards and new universities have each been proposed as the guardians who would hold the line, and each is a corrector to which Section 4 applies." §10.5: the form table gains four rows (tempo, R5; human decision authority, O2/E1/Lemma 6.3; standing of those affected, R7, the chamber; due process against correctors, the appeal) and a disclosure row (mandatory audited disclosure of conversion data, sanction above the gain from omission); the authority row's form is "separation rule plus chamber"; one sentence that separately held functions are monocentric per function and differ from a polycentric complex; DP3 (providers have voice, not vote). Federations to X10 with one sentence. Candidate configuration shortened to principle, separation rule and end condition; its coercive fallback sentence now points to §12.1's compared-not-settled entry, so coercion has one home.

### Part IV. Transition and judgment

#### §11 A reachable transition (target 2,200)

Box unchanged in substance; *Holds when* adds: each step held for its dwell time, which depends on the depth of lock-in; a recruitable alternative lineage bounds it.

`relaxtrust`, `signal` unchanged. §11.3: E1 narrow form with the $q_L$ condition in the sentence ("a strict equilibrium among informed actors where the lock is near-certain; in tactical domains with a large advantage and an uncertain lock, delegation can be an equilibrium"); broad form restated per §6.6, with "broad is the scope, narrow the first step" and "E1 must be held in common"; E2 "its cost can be large (C10)"; E3 unchanged; `pausevalue` unchanged; `readiness` Definition 11.4 with a residence condition per dimension (met within the time constant of that dimension's slow variable) and a sequential decision rule; the "Today" column to TESTS §6. §11.4: stages rewritten as parallel tracks with time constants, the slowest started first; dwell depends on logit depth, a recruitable alternative lineage bounds it (10.45 → 3.81 [num]); "graduated steps reach the threshold only as a ratchet"; the where-things-stand sentence corrected per the evidence review (roles only). §11.5: `reachable` becomes **Table 11.5 (Requirements of a reachable path) [def, with support]**, or a capture-basin proposition if S11 can state one cleanly; precedents in one paragraph with each precedent's limiting condition; "AI lacks saturation by the racers' own premise; balancing by others is a saturation mechanism independent of technology (C5)".

#### §12 The judgment (target 1,900)

Rebuilt in §6 of this memo.

#### §12.4 Conclusion (target 420)

Not a restatement of the chain. Three paragraphs: what the paper showed, in the conditional form of §1.2 compressed to five sentences and citing G1–G6; the affirmative meaning in Ren's words (identity, not membership; decay and renewal; a great future; the minds we are making); what has to be agreed ("not who comes first, but what every participant needs in order to go on, and how the means of correction stay in common hands"). "Change the basin first; then add speed."

### 3.14 What lives in the companions and registers

**SUPPLEMENT.** S2: the MPE remark and its block; the growing-prize derivation; Remark S2.1 corrected and $T_{\rm dec}$ by $\lambda^\ast$; the cap-equality and diffusion cases; the growing-oscillation remark. S3: Proposition 3.9 in full with the three layers; the $\kappa_e/\kappa_s$ split; Lemma 3.10's affine condition and the nonlinear example. S4: the per-unit cost floor; the $[H_f]$ branch with initial conditions; the joint capacity simulation (Study 2 partial results); Theorem 4.12's proof with (b)(c) as mechanism. S5: Remark 5.3's toy; the scissors reduced form corrected ($q$ consistent with 5.4(5); about 0.95); the explicit $p_d(\upsilon,\tau,T_{\rm dec})$ and the joint reduced-form figure; Corollary 5.5's symmetric perturbations. S6: 6.8 with a summable example; 6.11's "from $t=5$ the realized risk is at most 3/16"; the masked class; 6.9's budgets. S7: the four-column parameter table; the mechanism index. S8: Jones corrected; the linear-utility derivation marked as this paper's. S9: Table 9.1 row by row; **the crosswalk R↔I↔D↔Q↔G**. S10: margins on both hosts. S11: dwell by depth; frozen-share formula; parallel tracks' time constants. S13: new interface "Human capacity and correction"; the loop-gain/breakout interface with $\lambda^\ast$. S14: new counterexamples ($\Gamma_\delta\ge1$; cap equality; positive diffusion; falling positive $f$; unequal incidence; stochastic punishment asymmetry; $p<1$; nonlinear fitness; growing prize with $r<1$). S15: EC relabelled "valuation check", LG(C) and RH "identity"; new independent blocks (MPE; growing prize; non-quasi-static capacity; explicit-action stochastic game for EC; boundary cases; CS at $\eta\ne1$; LG with three stocks; CR reporting strictness).

**DISCUSSION.** X1: corpus keys corrected (讲理／讲赢 → `alignment-selection` with `jian-and-wenyan`; five endgames → `selfishness-spiral`; 力之所及 → `shengsheng`; the reform dilemma "not verified against an original"); a date column; the twelve works of Adv-O I7 each with "absorbed / added" (Grieco, Snidal, Powell 1999, Gilbert–Newbery, Budd–Harris–Vickers, Athey–Schmutzler, Aghion et al. 2001, Avenhaus–von Stengel–Zamir, Schelling–Halperin, Kydd 2000, Shavell 1986, Grossman–Helpman), Askell–Brundage–Hadfield 2019 and prover–estimator debate in the alignment paragraph; "what is new" rewritten to match §1.4; Maynard Smith and Szathmáry in the list. X8: a paragraph on Fudenberg–Koh's pacing equilibrium (where it coincides with E3 and where not); benign winner with $\kappa_W$ and "whether AI lowers the winner's dependence on the governed" as a general crux; Abecassis moved to "what remains"; the sprint's objections by type; the durability table with a base rate for international regulatory bodies' survival and capture, or the same evidence standard in every row (Adv-O m6). X10: the manipulable clauses repaired (injection is the injector's violation and does not suspend findings; dissolution only by coverage or certificate failures not attributable to the assessed; held-out metrics hash-committed; levy base wider than the constrained activity, surcharge on frontier compute; $d^\ast$ estimated as a conservative upper bound by a body that does not receive the levy, with a ratchet; execution and fallback given financing, appointment and certificates; chamber and appeal given removal conditions; deadlines stop while the assessed party withholds access; frontier contributions by formula); Ostrom DP3 and nesting (national, regional, global, with a common floor); the disclosure function; federations at both orders; the coercive fallback paragraph pointing to §12.1's entry. X11: parallel tracks; precedents with limiting conditions (BWC's low military value and nuclear substitute; Montreal's available substitutes; nuclear power's later lapses; Outer Space and Seabed as a class of weapons kept out of a domain; ABM "removed one driver"; the nuclear monopoly and period of superiority 1945–54; a source for 1983).

**Registers.** CLAIMS: thesis in conditional form; L1 and L4 statuses; the contribution inventory with "restated in V6.2" column; disposition of the V6.1 reviews, including B3/B4 of v6.0 recorded as narrowed or open; C3a/C3b, C9 split into four, C12 (verifiability), C13 (dependence on the governed), N4. EVIDENCE: EV2 (RSP 3.1's retained discretion; current version 3.4; "support at the level of written commitments"); EV4 (political spending on both sides, classified by $\chi$; disclosure that it includes the drafting developer); EV5 (frontier by metric; open–closed gap 4 months; METR's range ceiling); EV6 (arXiv numbers; sandbagging source; alignment faking, sleeper agents, in-context scheming); EV8 (two leading states' positions on the latest declaration and the panel vote); EV9 (Ho et al.'s range); EV11 and Jones; EV3 (litigation outcome); the gap list with T5. TESTS: Test L redesigned by cost incidence with detectability held fixed (difference in differences); Test Γ's observable; Test G's hump; Test M relabelled a remedy test; Study 2 partial results and the $\mathcal M$ interface; the readiness "Today" column; the Γ calibration template by channel (ranges, not point values); the loop-on-loop model (Sys m3) as a research item; C12, C13, N4. LEDGER: sentence-level comparison for units with inclusion below 0.3; §5's blanket sentence removed; §7's S5 misrecord corrected; the nine withdrawn items with a line of reason each, two reclassified as restated; the three unaccounted changes (entry barriers; hysteresis prediction; Meadows → threshold) recorded with reasons, the Meadows one flagged for Ren. CHANGELOG: Definition 2.1's three-plus-closure; coercion's move; the V6.2 decisions.

---

## 4. The integration map

Rule: fold into the argument where the correction changes a statement; a caveat is a last resort. "Home" is the one place the point lives; other places cite it. SYNTHESIS numbering follows §四 of SYNTHESIS-v6.1.

### 4.1 SYNTHESIS A: mathematics, by key

| Item | Lands | How |
|---|---|---|
| A1 `loopgain` | §2 Prop 2.2; Remark 2.7 new; S2 | Conditions in (3); $r_j$ equilibrium elasticity; rank-one in (1); MPE sentence [num]; headlines → "structural gain" |
| A2 `standprice` | §3.5 Prop 3.9 rewritten; S3; 导读 2; §1.2(2); §3 box; §5.5; §7.1 table; §12.4; CLAIMS L2 | Three layers (§2.1). "Every forward-looking actor" removed everywhere. Tightened by the coincidence with 2.3's condition |
| A3 `compound` | §2.2 Prop 2.3; §10.2(3); S2; S14 | Strict cap; diffusion in recovery; "inflow not tied to rank: sharing, provision or diffusion"; openness reading in §10.2 |
| A4 `blind` | §3.2 Lemma 3.3(3) | $s(0)>c>s(1)$ in the statement |
| A5 `onegroup` | §3.6 Lemma 3.10; S3; PR block | Total term under every payoff-monotone rule; group terms under affine fitness |
| A6 `boundary`, `standprice`, §3.8 | §3 box; §3.4; §3.8; §12.2 sentence moved up | Held self-model error vs accurate working objective; the triple replaces "systemically false"; $\kappa$ divisible part only |
| A7 `corrrate` | §4.3 Prop 4.5; R3a; S4; TESTS Study 2 | Sufficient/necessary halves; (2) at $f=0$; (3) initial conditions, "rises"; $f$ cost floor; $\hat Y$ defined; $\mathcal M$ channel in Remark 4.13 |
| A8 `slowroute` | §4.6 | Proposition 4.12 "Silent crossing when capture precedes evidence"; premises (reach),(a),(d),(e); (b)(c) mechanism; two-clock comparison a condition to check |
| A9 `enforce` | §5.2 Prop 5.4; S5; EC | $p_d$ per deviation; (5) one breakout per period, $q\le1/2$; example $P<v<C$, $q=0.045$ |
| A10 `relpunish` | §5.2 Cor 5.5 Scope; CR block | Weak printed / strict under symmetric perturbations; continuation game symmetric; role assignment is equilibrium selection |
| A11 `restraint` | §5.2 Cor 5.6 | "changing the premise itself" |
| A12 `coverage` | §5.3 Thm 5.12 | (variety grows) motivation, not premise |
| A13 `talk` | §5.4 Prop 5.15 title; §1.2(4); 导读 4 | Amplification $n/(n-2)$, weakening with $n$; blocs [conj] |
| A14 `delegatelock` | §6.3 Prop 6.4; §11.3; §12.1 tier 1 | $p=1$; $q_L=1$ stated where "strict equilibrium" is claimed |
| A15 `nested`, R8 | §6.4 Prop 6.7; Table 9.1 R8; S6 | Matched unsafe variant; share-neutrality vs compliance; tax payable from a lead while it lasts; "admission reaches only to release" → limitation |
| A16 `topology`, CLAIMS | §6.5; §9 safeguards; CLAIMS | Row sums a sufficient certificate everywhere; never "necessary" |
| A17 `safeguards` | §10.3 Thm 10.5(1); S10 | Margin condition on both hosts; "instance of a viable parameter boundary" |
| A18 `share` | §10.2 Prop 10.3(2) | $n$ vs $n-1$ divisions, consistent with 5.7 |
| A19 `require` | §9 Table 9.1 | R4 exception; R1 $\limsup$; R3a; kind [def, with support] |
| A20 scissors | §5.5; §1.2(4); §5 box; §12.4; CLAIMS L4; Test G | Arms [thm], conjunction [conj]; 0.95; $D,g$ faster than $C-v$; reduced form labelled; hump when $D>C$ |
| A21 labels and symbols | all; symbol table | Table of §7.1 below; the "one meaning" claim limited to the table's symbols; renames: $\mathcal J$ Jacobian, $\mathrm{Cost}(q;p)$, $h_d$ in (15), $U_i\to L_i$ subordination value, $q\to q_b$ breakout, $m\to m_o$ non-contestants and $k_\ell$ checks per layer, $s\to s_b$ bloc size, $\varpi$ in 3.7 → $\varpi_V$, $\mu$ transmission → $\mu_t$, $\tau$ detection lag → $\tau_d$ |
| A22 line 363 | §4.6 last paragraph | Whole-system maintenance account from §10.4; generative persistence a conjecture |

### 4.2 SYNTHESIS B: arrows between models

Home: S7's four-column table (intervention; held fixed; model giving the sign; unproved interface); §7.1's table cites it and splits $d$ into two rows. $\Gamma$ decides sign, $\lambda^\ast$ speed (S2, S13). The reflexive channel's gain at the present distribution (high moment of shares) in §10.4 strand 2 and Remark 10.4. §7.1's four loops with the formal correspondence; the growing-oscillation remark [num] in S2; "gain" (drives) → "amplifier".

### 4.3 SYNTHESIS C: summaries and the judgment

| Item | Lands |
|---|---|
| C1 headline sentences and boxes | 导读; §1.2; every box's third line; §12.4; CLAIMS §1. Thirty-minute path adds §1.4 and §12.3 |
| C2 tier 1 | §12.1 robustness matrix (§6 below): measurement stays unconditional; formula funding and mandated access conditional on C2; narrow E1 with the $q_L$ condition; item 6 relabelled "realizes joint value whatever the cruxes, not accepted across camps" and the "mostly accepted" clause deleted |
| C3 tier 2 | Pre-committed activation executed by mechanism; $T_{\rm dec}$ estimated by correctors certified under C2 through channels observing actions directly, under Remark 4.8's conservative rule; residence condition in Definition 11.4; stages as parallel tracks; coercion moved out |
| C4 tier 3 | Ordered by the standard's third step; reason 1 = reversibility asymmetry over all failure modes; every path in $\Theta$ compared on all its own failure modes |
| C5 the name | §0 sentence; title unchanged (Ren's) |

### 4.4 SYNTHESIS D: fidelity

All fourteen rows of the fidelity table land as §5 of this memo specifies, in Ren's words. The ledger goes sentence-level; LEDGER §5's blanket sentence and §7's S5 misrecord are corrected; the nine withdrawn items get a reason each, two reclassified; X1 keys and dates fixed; the guide rewritten (§5.3 below); xref compares keywords item by item; CHANGELOG records Definition 2.1 and the three unaccounted changes; tone items (stick and carrot; "can be large (C10)"; defensive realism; "keep pace"; V1's words for "shared flourishing"; §10.1 mechanism first; carriers defined in §1.2; "and trade everything for winning") all land in the sections named in §3.

### 4.5 SYNTHESIS E: alignment

| Item | Lands |
|---|---|
| E1 masked class | §6.4 fourth class; corollary "necessary, not sufficient"; Remark 4.8; 导读 5; R8; C12 |
| E2 internal deployment | "before consequential deployment, internal deployment included" in §6.4, §6.6, R8, §12.1; sentence after strong incarnation |
| E3 tax scope | Prop 6.7 Scope paragraph (time tax via 5.11; tax-lowering research a public good; two fates of safety progress); C9 split; §8.3(a); §10.5 row "commonly funded alignment and control research"; X1 Askell et al. |
| E4 two joints | §6.3 end; §6.6 floor not objective; C13 general |
| E5 AI mind | §6.4 end; connects to 5.14 and 3.9 |
| E6 independence, adversarial | §6.5 after 6.9; §4.4 $x_{\rm ev}$ observable |
| E7 Test L | TESTS redesign; §7.3 Incarnation split |
| E8 inner level | §6.6 rewritten; plural evaluators to outer; CLAIMS disposition B3/B4 |
| E9 cruxes | C3a/b; C9×4; C12; C13; N4 in §12.3 and TESTS |
| E10 minor | pairwise-comparison sentence (§6.4); "can produce, more so with capability"; 6.7(2) "otherwise identical"; R8 liability route; 6.8 summable example; 6.11 "from $t=5$"; $U$/$Y$ units defined (TESTS, S5: $U_t$ = predefined hazard modes with correction meeting the four conditions at the stated catch rate); "rates of human overrule" → catch rates of planted errors; 6.9 budgets; README path; incarnation gloss; N4 |

### 4.6 SYNTHESIS F: systems and design

| Item | Lands |
|---|---|
| F1 Study 2 partial | Remark 4.13 [num]; S4; S13 interface "Human capacity and correction"; TESTS Study 2 rewritten (the failure signature comes from the slow variable, not capacity lag) |
| F2 dwell | §11.4; S11; Prop 4.11 Scope (frozen-share formula); CHANGELOG item closed; the "可" strand gets its quantitative reason |
| F3 strands and rows | §10.4 fifth strand "pace"; third "dual of the amplifier"; §10.5 four rows + disclosure |
| F4 manipulable clauses | X10, six repairs |
| F5 Ostrom | X10 DP3, nesting; §10.5 one sentence on monocentric-per-function |
| F6 transition as control | §12.1 tier 2 activation; Def 11.4 residence; §11.4 parallel tracks; Table 11.5; "ratchet" |
| F7 leverage | §12.2 sentence: pace (#9) and buffers (#11: alternative lineages, standby capacity, host margin) as low-resistance levers to buy dwell time |

### 4.7 SYNTHESIS G: evidence and citations

All land in EVIDENCE, X8, X11, S8, §7.2–7.3, §8.1, §8.3(c), §11.4–11.5 as named in §3; citation mechanics in `refs_v62.py` (key = first author, second author or et al., year; reverse check); Maynard Smith and Szathmáry listed; unused entries removed; Leonard's mark; Khan and Kenton listed; Caulin–Maley qualified with Butler 2025; global minimum tax rewritten as "the largest participant obtained an exemption" (D5); precedents reworded. New entries from Adv-O I7 are marked ‡ only after a web check.

### 4.8 SYNTHESIS H: checks and tools

`xref_v62.py`: duplicate-kind check ("Proposition Proposition"); bidirectional citations; guide-to-§1.2 keyword comparison item by item; the three-line box present in every section. `checks_v62.py`: relabels; new blocks (MPE from Math-O `s2_mpe.py`; growing prize from Adv-F `prop39_growing_prize.py`; non-quasi-static capacity from Math-O `s4`, Math-F `m5`, Sys `s5`; explicit-action stochastic game for EC; boundary cases per Codex; CS at $\eta\ne1$; LG three stocks; CR strictness; the joint scissors figure). Reviewer scripts are already under `v6.1/reviews/scripts-v6.1-*/`.

### 4.9 Items in the reviews that the synthesis does not list

| Source | Item | Lands |
|---|---|---|
| Adv-F F4 | Benign winner at its strongest: $\kappa_W/(1+\kappa_W)$; the crux is whether AI lowers the winner's dependence on the governed | §5.2 after Prop 5.7 (one sentence); §8.3(d); X8; C13 generalized |
| Adv-F F7 | $p_d$ not linked to $\upsilon,\tau$ | §5.5 explicit $p_d(\upsilon,\tau,T_{\rm dec})$; S5; Prop 5.4 Scope; tier-2 trigger names the estimator |
| Adv-F F11 | Fudenberg–Koh pacing equilibrium dismissed in half a sentence | X8 paragraph: where pacing coincides with E3, where it differs (delegation channel, transparency) |
| Adv-F F12 | 5.15(2) needs "third parties affected linearly" | Prop 5.15 statement |
| Adv-F F9 | Theorems that are summaries | Summary 7.1; Table 9.1; Table 11.5 |
| Adv-F F10 | Minimal-SPE assertion only in S5 | Prop 5.4 Scope cites it |
| Adv-O I6 | Sprint-then-freeze answered partly by normative premises | §8.3(e): objections by type; the two mechanism objections; D4/D5 comparison with common custody |
| Adv-O I7 | Literature gaps in IR, arms control, IO | X1 absorbed/added; §1.4 "what is new" |
| Adv-O I8 | Generative direction in four drifting versions; twelve requirement lists without a crosswalk | G1–G6 defined once in §8.2; crosswalk in S9 |
| Adv-O m2 | "AI lacks saturation" contradicts §7.3 | §11.5 conditional, citing balancing as technology-independent saturation (C5) |
| Adv-O m5 | 5.14 and "growth is not the danger" | Clarifying sentence after 5.14 |
| Adv-O m6 | X8 durability table asymmetric on the own design | Base rate for international bodies, or one evidence standard per row |
| Adv-O m7 | Corpus citations read as empirical support | §2.1's sentence tagged [conj] or given an external citation |
| Adv-O m9 | Henrich et al. for persons only | §3.8 scope sentence |
| Alignment minor 13 | "Incarnation" unfamiliar | One-sentence gloss in §6.4 |
| Alignment minor 14 | AI minds' standing vs "suspend, modify, replace" | N4; one sentence in §6.6 (O2's priority is for the transition) |
| Alignment minor 9 | Prover–estimator debate | X1 |
| Sys m1 | Remark 2.5 not a case of 2.2 | "of the same form, not the same theorem" |
| Sys m3 | A loop-on-loop model making "does the generative order attract" computable | TESTS research programme, as a suggestion; not in the core |
| Codex Test M | A remedy test mislabelled as refuting C2 | TESTS: relabel; test conversion separately while accounting for changed correction |
| Math-F I4 | Failure time a lower bound on the real one | Prop 4.5 Scope |
| Math-O M3 | Fixed cost delays, does not cap | Assumption 4.2 and §4.3 prose |

### 4.10 Declined, with reasons

| Item | Reason |
|---|---|
| Compress the core to 12–15k (Adv-F) or 18–20k (Adv-O) by moving §3.7, §3.8, §11.5, the Q-table, §10.4's table, §10.5's configuration to companions | Ren: no cap, completeness first; Codex: fix premises before compressing; fidelity: §3.7–3.8 carry Ren's words and every reviewer's keep-list includes them. The spine they want exists as the thirty-minute path, now real. Targeted trims are taken (§1.5) |
| Build the paper around a single integrated model deriving the scissors (Adv-O F1(a)) | The family's own bias toward unification (both Adv-O and Sys flag it); a new joint model brings new errors and a new review round; the theorem-level claim is C0 and should stay a tested conjecture. Taken instead: the joint reduced-form figure [num] in §5.5/S5 |
| Change the subtitle to "the selection pressure of winning and its reflexive closure" (Adv-F F5) | The title is Ren's; the §0 sentence does the work |
| A calibration table of $\Gamma$ by channel in the core (Adv-O I1) | $\Gamma$ is unmeasured; point values in the core would overclaim. A template with ranges and their sources goes to TESTS/EVIDENCE |
| Redesign X10 as a polycentric complex with nested levels (Sys I7 read maximally) | The polycentric complex is already a separate candidate compared in tier 3; merging them removes a comparison. Taken: DP3, nesting sentences, disclosure row, "monocentric per function" |
| Define Branch III by $\Gamma_{\rm eq}$ throughout | $\Gamma_{\rm eq}$ is computed only in one class; mark Branch III's definition [conj] and keep structural $\Gamma$ as the printed benchmark |
| Move the readiness dimensions wholesale to TESTS | The seven dimensions with the residence condition are part of the judgment's mechanism; only the diagnostic column moves |
| Restore v6.0's "two directions of capture" prediction (entry barriers) as a prediction of this theory (fidelity minor 3a) | Test B's narrowing made it discriminating; recorded in LEDGER §3 with the reason; the "exclude entrants" sentence in §10.1 stays |

---

## 5. Fidelity: Ren's rulings come back in his words

Rule for implementers: where Ren's sentence exists (corpus README, the book, the transcript, v6.0's text he adopted), use it, and tag the paragraph [corpus: key] or R in CLAIMS. Where the fidelity review supplied a model paraphrase, treat it as a placeholder for Ren to confirm; mark such sentences "D" in CLAIMS until he has.

### 5.1 The lost rulings, their homes and their words

| Ruling (fidelity table) | Home | Words |
|---|---|---|
| Broad E1's scope: labour, finance, persuasion; one person's benefit is still an instrument; broad is the scope, narrow the first step | §0 ¶3; §6.6 (definition); §11.3 E1; §12.1 tier 1 item 1; 导读 判断 | §0: "…an instrument in a game whose aggregate concentrates control and makes those without it fall behind." §6.6: "AI not used as an instrument in any contest that tends toward dominance or concentration, in labour, finance and persuasion as much as over shared conditions. The unit is the game, not the act: a use that helps one person is still an instrument in a game if everyone's use of it makes those without it fall behind. The narrow form is the order in which to begin, not the scope." (v6.0 §9.3, Ren 2026-09-26) |
| Decay and renewal belong to growth | §0 ¶4; §12.4 ¶2; 导读 | "Decay and renewal belong to its growth." (v6.0 §0; transcript 00:57:27 "decay as a form of growth") |
| We are the larger process, identity not membership | §0 ¶4; §12.4; 导读 | "We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good." (transcript 01:06:32: "we are not just our life. We are the whole process of the universe doing this and itself and this is great"); §3.7 keeps 我们即是集 |
| "We are one" in both one-page summaries; the target is the narrow self | §1.2(2); 导读 2 | "selection favours the narrow self-model that the system's real coupling punishes… That is why understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are to continue." |
| The rejected guardians | Remark 10.8, after the first sentence | "Philosopher-kings, priestly classes, enlightened stewards and new universities have each been proposed as the guardians who would hold the line, and each is a corrector to which Section 4 applies." (v6.0 §8.7; transcript 00:39:09 and Ren's refusals) |
| Falling behind cannot be survived, so oppose the logic first | §3.8 "The logic to oppose", first sentence | "If a winner's logic is of this kind, falling behind cannot be survived, and every actor has reason first to oppose the logic itself." (v6.0 §7.12; Ren 2026-10-03) |
| Insurance accepts the frame of the contest | §8.3(f) | "Insuring against falling behind is not an exit: the penalty is set by the winner, and insurance accepts the frame of the contest, hedging against losing instead of declining the game (Remark 8.9)." |
| The generative loop's institutional forms; the degenerative loop closes | §10.4, before the strands table | "…in institutions: shared capability, distributed agency, plural observation and critique, maintenance and repair, the renewal of commons. In the degenerative loop fear produces defence, defence struggle, struggle seizure and concentration, these scarcity and resentment; trust collapses; fear deepens." (生生不息论 l.247, 283: 恐惧→防御→斗争→掠夺与集中→稀缺与不满→信任之崩→恐惧更深) |
| A self-replicating economy carries the switch | §5.1 after Remark 5.3 | "Expansion is an anaesthetic for the winning model. Winning does not end the game: the logic itself is the replicator, a winner is a field in which the same selection continues, and a self-replicating economy that carries it into new frontiers carries the same switch with it." (v6.0 §5.1); LEDGER §7 corrected |
| Growing understanding without executive authority may change nothing | §4.3 last paragraph; cited in §12.2 | "A fixed capacity to certify or to correct can make some kinds of erroneous support decay faster; growing understanding without executive authority may change nothing." (v6.0 §4.3) |
| Meadows's hierarchy; the paradigm changes only if the system is understood | §12.2 | Both kept: "Interventions at the level of parameters are re-absorbed by a system whose goals and paradigm are unchanged (Meadows 1999); in the field model, a parameter moved without crossing its threshold is re-absorbed and one moved across it is not (Proposition 4.10). The paradigm can change only if the system is understood." Flag for Ren: the threshold reading narrows Meadows to "which parameters, and for how long"; LEDGER §3 records it |
| Preference falsification; reverse performativity | §5.4 narratives paragraph | "People say what is rewarded rather than what they believe, so a public consensus can persist that few privately hold (Kuran 1995); and performativity runs both ways: a model can make itself false (MacKenzie 2006), which is what a shared prediction of this kind is for." |
| ASTRA sentence | TESTS research programme | One sentence naming the ASTRA layering as an instance of staged delegation, or LEDGER states why not restored |
| "and trade everything for winning" | §2.1 | Ren's sentence completed |

### 5.2 Other items of voice

"Our aligned AI is us" keeps Ren's phrase and gets its two joints (§6.3). "Growth is not the danger; the mind is" stays after Proposition 5.14 with Adv-O m5's clarification, which is Ren's own ruling of 2026-09-25 ("we can grow exponentially till we met our need, but we can't compounding forever"). "Judge the game, not the act" gets its precise form in §3 (§2.6 above). "No better guardian" gets its list. "Trees" stay as the image of provision beneath the game; $k_0$ is their formal content and §2.1's result makes it the common return. 讲理／讲赢 cited to the right folder. 力之所及，责之所在 cited to the book (2026-07-14, l.357). The guardian test's fourth question (does understanding go to everyone, or to a class whose position depends on others' not understanding) stays, as Ren's "understanding goes to everyone, not to a class".

### 5.3 The Chinese guide, in full

Rules: natural Chinese in Ren's register (the book's cadence without its classical syntax); 母体, never 宿主; 征候, not 签名; no "闭合于自身", no "这个过程是好的"; nine items in the same order as §1.2 with the same conditions; the judgment with coercion in the third tier and broad E1 named; the thirty-minute path with §1.4 and §12.3. `xref_v62.py` compares each item's keywords with §1.2's.

> **中文导读**
>
> **用途与意义。** 本文做的是预测。沿着现在的路走下去，"讲赢"的逻辑会把所有参与者带到一个谁都不会选的结局：在第 2 节的条件下，每一方都比共同克制时过得更差，所争之物大半耗在争夺里。如果能力带来的危险增长得比纠正它的力量快（第 5.3 节，也是第 12 节的核心分歧），这个逻辑连赢家也一并危及，赢家只有停下复利才能脱身。预测的用处，是先让理解对齐，协调才有可能。本文判断的是博弈，不是行为；是结构，不是任何人。它的意义是肯定的：我们不只是各自的一生，我们就是这场更大的生生过程本身，它借我们继续展开，这是好的；衰败与更新，也是生长的一部分。要反对的不是增长、竞争、技术或任何一群人，而是一种逻辑：一个部分忘了自己属于一个身体。生存是最低要求：大规模的生命损失，和人类决定权的不可逆丧失，先于一切被保护，因为失去了就无法再纠正。
>
> **核心。** 三个条件同时成立，就有"赢的选择压力"：参与者按相对的成功被选择；赢到的东西可以再投入同一场竞争；能力越强，胜出越有把握（决定性）。如果成功还能买到对选择本身的控制——规则、纠错者、心智的养成、描述成功的语言——压力就转回来作用于选择自己，这就是"赢的元吸引子"。"元吸引子"是给机制起的名字；它在数学意义上是否"吸引"，只在第 4 节的场模型里证明了，对现实世界则是猜想。三个条件相互联系，不是一张清单：在地位相近处，它们合成一个结构性的环路增益，它给出领先会不会越滚越大的结构门槛；对手彼此应对时，实际的增益可以是结构值的好几倍。能否到达不受制裁的位置、能力是否快过纠错，是环路增益不决定的另两个条件。
>
> **论证链（与第 1.2 节同序、同条）。**
> 1. 凡是能增减份额的单位（载体）按相对成功被选择、赢得物可再投入、领先可成决定性时，成功抬高赌注与背约之利，同时削弱能约束它的制裁、纠错者与共同语言；成功若还能买到选择者，这种削弱就由选择本身再生产出来。这不依赖任何载体：细胞、企业、国家、学说、训练中的 AI 系统都一样。
> 2. 所有载体同属一个母体，彼此耦合，没有外部。相对选择看不见共有之物：既看不见母体的衰退，也看不见对所有人一律适用的约束；后者只有在负担等额、规避受罚时才能存续。再投入的相对回报高于共同回报时，复利会给地位定价，向前看的行动者的工作目标随之收窄——奖金固定时总是如此，奖金随总能力增长时，条件恰是领先会越滚越大的那个条件。选择偏爱把边界画在系统之内的狭隘自我，而系统真实的耦合恰恰惩罚它。行动者在博弈里算得没有错，错的是博弈。对全局而不可逆的失败，整合只能事先依据对系统的准确理解来完成；所以，理解"我们是一体"——一个相互联系的系统，一个母体，没有外部——是增长与变化得以延续的长期条件。可挽回的失败，仍可以从试错中学习。
> 3. 对纠错者的影响一旦可被占有，就在最大的载体那里被选择出来；控制的成本下降时，独立纠错按给定的速率增长就足以保住证书，而当能力紧跟其选择水平时，这个速率也是必需的；留下转化通道的改革会被重新吸收；被俘获的评估可以让母体在任何警报之前越过底线。
> 4. 只有当"偏离变成决定性优势"的概率低于一个门槛时，克制才可执行。赌注相对于无须赢得的供给增长时，这个概率升高；决定性位置的价值随赌注增长时，门槛下降。这是"剪刀差"：两刃各自已证，它们在现实中是否同步合拢，是登记待验的分歧。纠错跟不上它要追的节奏。两个对手之间，相对核算让话语失去信息；三方以上，它把一对之间的冲突放大 n/(n−2) 倍（随人数增多而减弱），并使对手结为针对第三方的同盟。
> 5. 忠实的 AI 让委托人的博弈更有效；委托是拿纠错换速度。化身的弱形式：最外层的回路决定哪些偏差被容忍；凡抵消偏差要付相对地位的代价，只有强制执行的共同准入约束能让它继续被抵消；对在评估中掩蔽的偏差，协调是必要的，却不充分，准入只能按能力门槛设定，超过门槛即停止或放慢。化身的强形式是有条件的：AI 的谱系本身成为载体。
> 6. 当下轨迹的动态是这些条件的征候，证据有明说的缺口。竞赛的前提描述的正是重复博弈失去执行力的情形：它可以为"对竞赛者的最佳回应是竞赛"辩护，却不能为"竞赛作为集体路线"辩护。
> 7. 各条替代路径按同一个标准比较，同一个不确定范围也包括合作设计自身的失效。成功的路径，都是在所有有能力的行动者那里把共享参数推过门槛，不论叫什么名字——这是一条登记在案的预测。有几项要求，任何一方都无法单独满足。
> 8. 同一个反身结构若选择的是贡献，就成了生生的结构：它经由共有之物延续，不经由赢家；形态按功能推导，不沿"集中或分散""个人或集体"的轴。没有更好的守护者可以作答；能作答的，是一个每个守护者都被守护、错误不能无限生长的结构。
> 9. 信任是分阶段过渡的结果，不是前提。
>
> **判断（分三层）。** 现在就做的——其中一部分在任何分歧读法下都成立：让 AI 退出战略与升级决策回路（狭义 E1 是起点，广义 E1 是范围：AI 不作任何会集中的竞争博弈的工具，劳动、金融、说服与共同条件一样）；共同测量危险、覆盖与残余风险，与"谁领先"的测量分开；核查研究与试点；共同保管的预备。另一部分现在就做、但若某项分歧测得有利即可撤回：按公式拨款、强制准入的独立纠错（C2）；按类别的共同准入约束，在发布之前，也在内部部署之前（C9）；可分收益随产生而分享（C6）。预备好、按事先登记的指标自动启动的：停止建造决定性一类的能力（E2），共同保管，按理解的速度发展（E3）；启动是事先承诺、由机制执行的，因为触发恰恰发生在克制最难执行的时候。在同一不确定范围下比较、不作定论的：各种整体设计，以及对前沿投入的强制限制——后者只在负担等额且包括限制者自身、由独立纠错者执行、受影响者议院同意时才进入比较，本文不推断它的净效应为正。最后一层的排序是明说的判断，不是推导；理由是可逆性的不对称：分持职能的设计失败后可以解散为各项职能，越过底线则无法回头。
>
> **怎样读。** 三十分钟：本导读、第 0 节、第 1.2 与 1.4 节、各节开头的三行主张框、第 12.1、12.3 与 12.4 节。证明在形式伴篇（SUPPLEMENT），替代方案与设计的全文在讨论伴篇（DISCUSSION）。

Checks on the guide against §1.2: item 1 = conditions and closure and substrate-independence; 2 = one host, blindness, incidence and evasion, price of standing with its condition, narrow self, the actor computes correctly, anticipation, "we are one"; 3 = selection of influence, rate law (sufficient/necessary), re-absorption, silent crossing; 4 = enforcement condition, scissors conditional, tempo, talk with $n/(n-2)$; 5 = instrument, delegation, weak incarnation with $(A_\tau)$ and the masked class, strong incarnation; 6 = signatures with gaps, the premise of the race; 7 = one standard, own failure modes, registered prediction, no unilateral solution; 8 = generative, through what all share, form by function, no better guardian; 9 = trust an outcome. §1.2 in English must carry the same sixteen keywords so the xref check passes in both directions.

---

## 6. The judgment (§12), rebuilt

Box. *Claim:* under the protection standard and present evidence, a change in what the system selects for is warranted in three tiers: steps warranted now, some on every reading of the cruxes and some unless a named crux is measured favourable; steps prepared now and activated by pre-committed triggers executed by mechanism; whole designs compared under one range of uncertainty, where the ranking is a stated judgment ordered by the standard's third step. *Why:* the first tier keeps options open and measures the cruxes; the second answers a lead time, since custody must exist before anyone could hold decisive capability alone, and the trigger fires where restraint is least enforceable; the third cannot be derived from the standard. *Holds when:* the robustness matrix below is right about which readings each item survives; Section 12.3 names the measurements that would move it.

### 12.1 Tier 1: warranted now

Two sub-lists replace V6.1's seven items, and the clause "mostly accepted by those who favour regulated competition" is deleted (false of item 6; Adv-F F2).

**(a) On every reading of the cruxes.** Each item is checked against C0–C13 in a robustness matrix (TESTS §3 holds the matrix; the core prints the items and one line saying every cell is "stands").
1. Begin narrow E1: declaratory doctrine with inspected exercises (Stage 2), verified where verification exists, with drilled human fallback and an evidence channel independent of AI. Among actors who price in a near-certain lock it is a strict equilibrium (Proposition 6.4, $q_L=1$); where the lock is uncertain it is a signal (Proposition 11.2). Broad E1 is the scope; the narrow form is the first step.
2. Measurement: shared measurement of hazards, coverage and residual risk per class, kept apart from measurement of who leads; row sums of correctors and the correlation of their errors; $x_{\rm ev}$ where models evaluate models.
3. Research on, and pilots of, verification of compute, training and custody.
4. Preparation of common custody: its design, institutions and triggers, registered now, with the activation rule of tier 2 pre-committed.
5. Alignment and control research funded in common and published: the research that lowers the tax is a public good competitors undersupply, and once published it is common to all (Proposition 6.7's Scope).

**(b) Warranted now; lapses for a named crux.** Each item says which crux withdraws it.
6. Independent correction with formula funding at arm's length, mandated access, rotation and rule-making insulated from success (lapses if C2 is measured favourable with findings executed against leaders; measurement under item 2 continues).
7. Common admission constraints, before consequential deployment, internal deployment included, for divergence classes measured to carry a positive tax (C9, class by class); for masked classes, admission by capability threshold with control protocols that do not assume cooperation (C12).
8. Shared provision of useful services, and the divisible gains shared as they arise where they can begin (they realize joint value on every reading and lower the value of winning; reliance on them as a lever lapses if C6 is unfavourable). Not accepted across camps; said plainly.

### 12.1 Tier 2: prepared now, activated by pre-committed mechanism

E2 with rollback where hazardous variety already exceeds coverage; common custody in force; E3 for each hazard class whose coverage falls behind. The trigger sentence stays: **a trigger fires when the estimated time to a decisive position, less the time custody needs to be installed and verified, falls below a margin registered in advance.** Three sentences are added, each a mechanism:
- Activation is committed in advance and executed by mechanism, not decided afresh when the trigger fires, because the trigger fires where restraint is least enforceable (Proposition 5.4(4), the closing of the scissors); a fresh collective decision at that point inherits the enforcement failure it was meant to prevent (Sys I8).
- The estimate of $T_{\rm dec}$ is made by correctors whose row sums are certified (C2), from channels that observe actions directly (compute, custody, the performance of contracts), under the conservative alarm rule of Remark 4.8, because the quantity is exactly the one masking hides (Adv-F F7, Adv-O m8).
- The indicators are registered: persistence of leads and the open–closed gap (C5); detection latency against the time from breakout to decisiveness (C7); catch rates of planted defects at fixed human hours and residual risk per class (C1, C3); correctors' row sums (C2). Deactivation uses its own indicators and a residence condition (Definition 11.4), not the activation indicators read backwards.

The coercive restriction of frontier inputs is no longer in this tier.

### 12.1 Tier 3: compared, not settled

The candidates: the separately held configuration (§10.5, X10); a polycentric complex of mutually recognized institutions; a verified agreement with shared provision; regulated competition meeting Table 9.1; an agreement of the type of §8.3(g); the benign winner; and, as its own entry, **the coercive restriction of frontier inputs**, which enters the comparison only under three conditions, each a mechanism result: equal incidence of the stop, including on the restrictor (Lemma 3.3(2): a stop borne unequally is selected against and read as a bid for a lead); execution by correctors certified independent of the restrictor (Proposition 4.3: a hegemonic enforcer is the largest conversion target); consent of the chamber of the affected (V3, R7). Its escalation risk is counted in $\Theta$ (Proposition 8.8). The theory does not derive that its net effect is positive; this is the hard case of §8.3(f), and X10's fallback paragraph cites this entry rather than stating its own version.

All are compared on the durability tests D1–D8 in one range $\Theta$ that includes each design's own failure modes: for the separately held configuration, capture of a function, dissolution, coercive enforcement, service disruption and collusion among its checks, each with what it reverts to; for continuation, the premises of §5.3 and a decisive position. Under the rule for $\Theta$ the worst case of each path includes an irreversible loss, so the comparison is at the standard's **third step** (lowest bound that keeps options open), stated as such (Adv-O I3a).

The preference for changing selection is a judgment with two reasons and one conditional clause:
1. **Reversibility asymmetry over all failure modes.** The separately held design's failures are each reversible into something short of the protected losses: capture of a function is certified and the function reassigned to a different lineage (Proposition 4.9; the X10 repairs); dissolution reverts to separately held functions with protections against domination entrenched; a restriction carries a sunset and an end condition; collusion among checks is what the direct measurement of error correlation detects; service disruption is bounded by the share cap and standby capacity. Continuation's failures, the crossing of the floor and a decisive position, have no reversal (Theorem 10.5(3), Proposition 5.7). This replaces "the certificates can be measured before the design is relied on", which was false of row sums that have never been measured (Adv-O I3b, Codex).
2. **Options of correction kept open.** The design stays inside the correctable kernel by construction of its end conditions; continuation leaves it at a point earlier than the losses (Definition 8.1).
3. *Conditional:* among paths that pass the tolerance, the design realizes more joint value; since no path passes it in its worst case, this clause orders only the futures in which measurement moves a path inside the tolerance.

A reader who weighs these differently can reach another ranking; §12.3 says which measurements would move it.

### 12.2 Why, and where the leverage is

As V6.1, with: "growing understanding without executive authority may change nothing" restored; Meadows kept beside the threshold reading; one sentence on low-resistance levers that buy dwell time (pace, #9; buffers, #11: alternative lineages, standby capacity, host margin).

### 12.3 Cruxes

The table gains C3a/C3b, C9's four parts, C12 (verifiability: can admission bound $m_{\rm model}$ at the admitted capability), C13 (dependence on the governed: does AI lower institutions' dependence on the people they serve), N4 (standing of AI minds). The closing paragraph adds: if C12 is unfavourable, masked classes pass from admission to capability thresholds and E2/E3; if C13 is unfavourable, "aligned to the principal" ceases to mean "aligned to the people", and the benign-winner path's residual risk rises.

### 12.4 Conclusion

As the §12.4 block in §3 above.

---

## 7. Coherence rules for the implementers

1. **One home per point.** The chain: §1.2 (English) and the guide (Chinese). The generative direction: G1–G6 in §8.2. The requirements: Table 9.1 with the crosswalk R↔I↔D↔Q↔G in S9. The alternatives in full: X8. The design in full: X10. Coercion: §12.1 tier 3. Dwell times: S11, cited by §11.4 and Proposition 4.11. The four loops: §7.1 (Ren's text) with the formal correspondence; §2.4 only hands off. Any other place cites the home by key or label; `xref_v62.py` fails a build in which a defined list (G1–G6, R1–R8, D1–D8, Q1–Q7, I1–I4, the five strands) is restated with different members.
2. **Claim boxes carry conditions without hedging.** Three lines, Claim / Why / Holds when. The Claim is flat; the Holds-when is flat and names the premise in words, with its label where one exists ((reach), $(A_\tau)$, $[H_\gamma]$, C0). No "may", "can" or "tends to" in a Claim that cites a [thm]; "can" is allowed where the result is existential (Proposition 4.7's "can silence it").
3. **Statements own their conditions.** Every result's statement contains its convergence domain, horizon, symmetry, initial-state and functional-form conditions (Codex 2); the Scope paragraph holds what would make it fail and what the proof does not cover; the prose draws consequences and never re-hedges. Test: delete the Scope paragraph and the statement must still be true.
4. **The chain is stated twice, not six times.** §0 may use one clause ("the logic of winning carries the participants toward an outcome none would choose"); §2.4 ends with two sentences of handoff; §7.1 gives the four loops; §12.4 closes with G1–G6. `xref_v62.py` counts occurrences of "accelerates the contest" and "alienates language" and allows two each in the core.
5. **Vocabulary, fixed.** *host* (English) / 母体 (Chinese); *structural loop gain* $\Gamma$ and *equilibrium gain* $\Gamma_{\rm eq}$, never "the loop gain decides"; *price of standing*; *compounding prices standing* (not "manufactures"); *the scissors* always with "each arm proved; their co-movement C0"; *amplifier* for drives (never "gain"); *per-unit cost floor* $f$; *masked divergence*; *pre-committed activation*; *signature* (English) / 征候 (Chinese); *incarnation, weak and strong*; *selection pressure of winning* for what the three conditions produce, *meta-attractor of winning* for its closure, *the mechanism* when Definition 2.4(1) is meant; *stopping* (E2) and *slowing* (E3) never interchanged; *carriers* defined at first use in §1.2 and §2.2; "Table" and "Summary" for 7.1, 9.1, 11.5. Symbols: the "one meaning" claim is limited to the table's symbols; conflicting local symbols renamed as listed in §4.1 A21; the symbol table lists the renames.
6. **Handoffs.** Each section ends with one sentence naming what the next section takes from it (§2 → the structural gain and $T_{\rm dec}$ for §3's price and §5's $p_d$; §3 → the working objective and the invisibility of the shared for §4's correctors and §5's $\bar p_d$; §4 → captured sanctioners and masked alarms for §5 and §12's trigger; §5 → (14) and the two channels for §6, §7 and §11; §6 → $(A_\tau)$, the masked class and the two joints for §9's R8 and §12's items; §7 → the status column for §8's $\Theta$; §8 → G1–G6 and the third step for §12; §9 → the table for §10's forms; §10 → the five strands and the end condition for §11; §11 → dwell and residence for §12's tier 2). No forward use of a result; `{{>key}}` only in handoff sentences, and the source text never repeats the kind word before `{{>key}}`.
7. **Ren's sentences are quoted, not paraphrased**, and tagged [corpus: key] with the right key; a paraphrase supplied by a model is marked D in CLAIMS until Ren confirms it.
8. **Roles, never names**, in the core; EVIDENCE names its sources; the disclosure sentence covers the drafting developer's political spending.
9. **Every arrow in a parameter table has a model.** S7's four columns are mandatory for every row; a row without a model giving the sign is marked "interface, unproved" and the core's arrow carries a dagger.
10. **Numbers carry their label.** Every number in the core is [num] with its block, or [obs] with its EV row; the two phrases "200,000" and "six digits" are reworded as algebraic checks (Math-O M6).

---

## 8. Risks: what could make V6.2 worse than V6.1

| Risk | How it would happen | Guard |
|---|---|---|
| More hedged, not tighter | Conditions added as caveats in prose; "may" spreading into claims | Rule 3 (statement owns conditions; prose draws consequences); §2's tightenings are mandatory text, not optional; the editor reads each rewritten result and asks what it now says that V6.1 did not |
| Churn that breaks the apparatus | Renumbering; moving results between sections; new keys for old content | Numbers 0–12 and result numbers fixed; new results appended; kind changes only via the keymap; LEDGER-units extended, not rebuilt |
| Over-unification (family bias) | The joint scissors computation promoted to a theorem; a loop-on-loop model put in the core | The joint computation is [num] in §5.5/S5; Sys m3 goes to the research programme; C0 stays a conjecture |
| Ren's voice lost again | Paraphrase replacing his sentences in "kept" paragraphs | §5.1's table is a checklist; sentence-level ledger comparison for every unit below 0.3 inclusion; D marks |
| The guide drifts from §1.2 | Edits to one not mirrored in the other | Keyword comparison item by item in `xref_v62.py`; the guide and §1.2 edited in the same commit |
| Length creeps while nothing moves | Additions made, moves not made | §1.5's move list is part of the plan; a build reports per-section word counts against the targets, as information, not as a gate |
| New citations unverified | Adv-O I7's twelve works and the alignment review's eighteen added from memory | ‡ only after a web check; † otherwise; the reverse citation check runs |
| Evidence asymmetry re-enters | EV4's spending recorded for one side; T6 for one state | One standard, both directions, roles only; the disclosure sentence |
| Coercion has two homes | §10.5's fallback paragraph and §12.1's entry diverge | §10.5 and X10 cite §12.1's entry; the three conditions are stated once |
| Tier 1 collapses to "measure and wait" | Everything conditional moved to (b) and read as optional | (a) keeps five unconditional items including the first step of E1 and custody's preparation; (b) says "warranted now", with the one crux that would withdraw each |
| Translation-ese returns in the guide | A model writes the Chinese from the English | The guide above is the base text; edits to it are checked against the banned list (签名, 闭合于自身, 宿主, 这个过程是好的) and read aloud for register |
| Outside-family review skipped | Fixes verified only by the same family | Send to Codex again: M1's amplification in catch-up contests, the quasi-static conclusion, the explicit-action EC, the 2026 literature, the precedents (SYNTHESIS §七) |

---

## 9. Open questions for Ren or the merge

1. Section 3's claim box now carries "the actor computes correctly; the game is wrong". Does Ren want that sentence in the guide as well (it is there in item 2) and in §0?
2. The Meadows reading: V6.2 keeps both the hierarchy and the threshold result; the threshold reading narrows "paradigm" to "which parameters are moved and for how long". Ren should confirm.
3. Tier 1(b) item 8, shared provision: kept in tier 1 as "warranted now, not accepted across camps". Alternative: move to tier 2 with C6 as its trigger. I prefer tier 1, because it realizes value on every reading; the Opus memo may differ.
4. Whether to publish the Γ calibration template (ranges by channel) at all before any measurement exists, or to leave only the Test Γ observable.
5. Whether `reachable` (11.5) can be stated as a capture-basin proposition in S11 with the one-dimensional dwell time as its minimum capture time; if not, it becomes Table 11.5.
6. ASTRA: one sentence in TESTS, or a LEDGER entry saying why not.
7. The thirty-minute path now includes §1.4 and §12.3; the README's other paths need the alignment additions (§8.3(a), X8 technical alignment, X1 alignment literature, EV6).
