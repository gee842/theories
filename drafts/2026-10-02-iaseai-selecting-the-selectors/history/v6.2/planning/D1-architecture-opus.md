# D1. V6.2: architecture and argument (Opus design memo)

*4 October 2026. Designer: Claude Opus 5.5, one of two designers given the same prompt independently. Read: SYNTHESIS-v6.1; all nine reviews in full (math ×2, adversarial ×2, fidelity, evidence, alignment, systems, Codex); V6.1 THEORY in full; SUPPLEMENT S0, S2, S3, S5, S13, S14; DISCUSSION X1; the heads of CLAIMS, TESTS, LEDGER, EVIDENCE, CHANGELOG, README; V6.1-PLAN; `src/` layout and `assemble_v61.py`; Ren's four guidance files; the corpus passages quoted in §5. One derivation is mine (§2.1(c)); I checked it numerically (`scratchpad/d1/growprize.py`, which may be cleared, so the derivation is written out here). Every new formula still needs its own check block before it enters the core. Nothing outside this file was edited.*

---

## 0. Recommendations on one page

1. **Keep the four Parts and the twelve sections.** Every reviewer praised the order by level of claim, and Codex says a further reorganization would not fix the remaining issues faster. Churn stays low: one integrating table becomes the opening of §7.1; §5.5 becomes a keyed result; §6 is reorganized inside its own six subsections; §12.1 is rebuilt. Keys do not change, and five new keys are added.
2. **One idea.** *Where what is won converts into the capacity to win again, the game manufactures the logic of winning in whoever plays it and buys the institutions that would correct it. Better players do not fix this; a different game does. Change what winning confers.* The reviews' corrections make this sharper, not weaker: each actor computes its interest correctly, and the game is wrong.
3. **Make three corrections into the spine of the paper**, not caveats on it:
   - (a) The price of standing in its general form: the working objective narrows iff reinvestment's *relative* return exceeds its *common* return. With a fixed prize this always holds. With a prize that grows with capacity it holds **exactly where leads compound**: $(1-\beta)r>1$ is both conditions.
   - (b) Correction lowers the loop gain where it acts on **what success converts into**, not where it only speeds the decay of stocks. A ratio contest does not see a decay common to all, which is Lemma 3.3's blindness again.
   - (c) The blades of the scissors turn on **one pivot**, the share of capacity that has to be won ($\omega$: stakes relative to provision beneath the game). Each arm is proved; the conjunction is a conjecture, shown in one reduced joint model.
4. **Add one integrating object: the thresholds table (§7.1).** It lists nine thresholds, one inequality each, with the result that proves it, what pushes toward danger, and the lever that reverses it. It replaces the parameter table as the core's map of how the conditions interconnect, absorbs Codex's "audit every cross-model arrow", and gives §8.2's generative marks, §9's requirements and §12.3's cruxes one thing to refer to.
5. **Add an English abstract**, and rewrite the Chinese guide to match §1.2 item by item, in Ren's register, with 母体 (full draft in §5.3).
6. **Rebuild §12** on a principle rather than a list:
   - Tier 1 holds exactly the steps whose justification does not depend on how any crux comes out: measurement, preparation with lead time, and narrow E1 where the lock is near-certain.
   - Tier 2 activation is committed in advance and executed by mechanism.
   - Tier 3 ranks designs by the asymmetry of reversibility over every failure mode, and coercive restriction is moved into it with its own three conditions.
7. **Restore Ren's rulings in his words** (§5): broad E1 as the scope; "we are not only our separate lives"; decay and renewal; the rejected guardians; "first oppose the logic"; insurance accepts the frame. Several fold into mechanism: decay and renewal becomes the recruiting alternative lineage that bounds dwell time.
8. **Length.** I estimate the core at about **28,000 words (±1,500)**, excluding the abstract, guide, symbols and references.
   - What it loses is pure restatement and side results stated at full length: about 3,000 words dominated on the frontier.
   - What it gains is conditions, Ren's rulings, and the alignment layer: about 3,000 words.
   - It will not be much shorter than V6.1, but every paragraph will carry more. "Elegantly short" is best served after V6.2 by extracting a 10–12k venue paper from the spine (open question 1).
9. **Sequence.** Follow Codex's order:
   - repair by key in `src/` with check blocks;
   - write the new results;
   - rewrite sections §2→§12;
   - write the front matter last, so the abstract, guide and §1.2 match the final statements;
   - update the companions and registers, then the sentence-level ledger and the tools;
   - send the result to Codex.

---

## 1. What would make this a great paper

### 1.1 The one idea and the spine

**The idea.** A selection that rewards relative success, lets winnings buy more capacity to win, and lets capacity decide winning, accelerates its own contest. It does three things at once:
- it makes those inside it compute narrowly;
- it buys the correctors that would restrain it;
- it erodes the means of restraint as the stakes grow.

Where success can buy the selectors, the selection reproduces itself (the meta-attractor). AI is its strongest instrument and can become its next carrier. The way out is not abolition but a change in what winning confers, so that the same reflexive structure selects for contribution.

**The spine: seven results.** A reader who holds these holds the paper:

| # | Result (key) | What it says | Why it is on the spine |
|---|---|---|---|
| 1 | One structural loop gain; compounding and enough (`loopgain`, `compound`) | Near equal standing the conditions multiply into $\Gamma$; leads compound when $\Gamma>1$; provision, sharing and diffusion each restore equality | The mechanism's core; the formal content of "trees" |
| 2 | Compounding prices standing (`standprice`, new form) | Looking ahead narrows the working objective iff relative return > common return; with a growing prize, exactly where leads compound | The bridge from the mechanism to minds: "judge the game, not the act", made exact |
| 3 | Blindness and what selection at any level cannot supply (`blind`, `onegroup`) | A term common to all is invisible to relative selection; a common benefit rises only by transmission (understanding) or by rules | Why "we are one" is a condition of anticipation, not a sentiment |
| 4 | Selecting the selectors (`influence`, `corrrate`, `reabsorb`) | Influence over correctors pays with the square of share; the rate law; reforms below threshold are re-absorbed | The reflexive closure as a selection result |
| 5 | The enforcement condition and the scissors (`enforce`, `scissors`) | Restraint holds iff $p_d\le\bar p_d$; the loop gain raises $p_d$ and narrows the objectives that set $\bar p_d$ | Why restraint weakens as the thing to be restrained grows |
| 6 | Coverage and a point of enough (`coverage`, `enough`) | Where hazardous variety outgrows contestable coverage, survival tends to zero whoever races; satiable need has a point of enough, relative standing has none | "Growth is not the danger; the mind is", and why E3 binds even a world that has stopped racing |
| 7 | The nested reward loop (`nested`, with the new `masked`) | Where countering a divergence costs standing, only an enforced common constraint keeps it countered; for divergences that hide under evaluation, not even that | AI as weak incarnation; why principal alignment does not align the game |

The judgment rests on four further results:
- **Lemma 8.2 (`fallback`)**: when an arrangement cannot do worse.
- **Proposition 9.2 (`nounilateral`)**: no unilateral solution.
- **Proposition 10.3 (`share`)**, with "the positional part cannot be divided".
- **Remark 10.8 (`guardian`)**: the guardian test.

Everything else either serves one of these eleven or belongs in a companion.

### 1.2 What a reader should carry away (the abstract)

Draft English abstract. It goes after the title line and before the Chinese guide, and is its English counterpart:

> Where whatever can gain or lose share is selected by relative success, what is won converts into the capacity to win again, and capacity converts decisively into winning, success raises the stakes while it weakens what could restrain it. This is the selection pressure of winning. Where success can also buy control over the rules, correctors, minds and language that select the next round, the pressure closes on itself: the meta-attractor of winning. In specified models the paper shows four things.
> - Near equal standing the conditions combine into one structural loop gain, and leads compound when it exceeds one.
> - Wherever reinvestment's relative return exceeds its common return, a forward-looking actor weighs standing above what all share. With a prize that grows with capacity, this happens exactly where leads compound: each actor computes correctly, and the game is wrong.
> - Influence over correctors is selected in the largest carriers, and if AI cheapens control, independent correction must grow at a stated rate.
> - Restraint is enforceable only while the chance that a deviation becomes decisive stays below a threshold, and the loop gain raises that chance while narrowing the objectives that set the threshold.
>
> Alignment of each AI system to its principal does not align the game among principals. AI is the pressure's strongest instrument and can become its next carrier. The way out is not to abolish competition, growth or selection but to change what winning confers, so that the same reflexive structure selects for contribution. Under a standard that protects irreversible losses first, the paper argues for three steps: measurement and preparation now; stopping, custody and pace prepared now and activated by mechanism on registered indicators; and whole designs compared under one range of uncertainty.

### 1.3 What the paper does not claim

This is one list, in §1.4, mirrored in the guide:
- It does not claim that competition, growth, technology or any people are the danger. Bounded competition in products, science and service continues.
- It does not claim that every race ends at zero survival, or that decisive advantage is attainable now.
- It does not claim that the thresholds move together in the world. That is the conjecture the diagnosis tests (C0).
- It does not claim that the loop gain has been estimated.
- It does not claim that the meta-attractor attracts in the world. The name is for the mechanism; attraction is shown only in the field model and, if built, in the toy of §3.4 below.
- It does not claim that one institutional blueprint is uniquely feasible or best. The ranking of whole designs is a stated judgment.
- It does not claim anything about any actor's motives. It judges the game, not the act.
- It does not claim that understanding suffices. Understanding acts through agreement on structural change, and growing understanding without executive authority may change nothing.
- It does not claim that AI should not be built. E2 concerns the decisive class only; E3 concerns pace.

### 1.4 The frontier between brevity and completeness

The core is dominated where it is long without being more correct or more useful. There are four places:

| Dominated content (V6.1) | Approx. words | Action |
|---|---|---|
| Restatement of the chain: guide, §0, §1.2, §2.4 end, §7.1 "the chain", §12.4, CLAIMS §1 | ~1,200 | The full chain appears only in the abstract, guide, §1.2 and §12.4, each with a different job. §2.4 ends in one hand-off sentence. §7.1 keeps the corpus's *four loops*, which are different content, and drops the chain prose. |
| Four differing lists of the generative direction (§3.7(3), §7.4, §8.2, §12.4) | ~400 | One canonical list of seven marks in §8.2. Elsewhere: reference, or identical wording in identical order. |
| Side results stated at full length off the spine (3.11, Rem 2.5, 4.11 detail, 5.8–5.10, 6.8–6.11, 8.3, 10.1–10.2, 10.6–10.7) | ~1,500 | One sentence each in the core with the key in bold; full statements in S. |
| Design and evidence narrative duplicated with X10, X11 and EVIDENCE (§10.5 candidate configuration, §11.4 "where things stand", §11.5 precedents) | ~700 | Keep the principle and the hardest case in the core; the detail goes to the companion. |

What must be *added*, and cannot be cut without being less correct:
- conditions written back into statements (~900);
- the general price of standing and the two errors (~400);
- the thresholds table (~500);
- the alignment layer (masked divergences, internal deployment, the two joints, the tax not fixed, the AI mind: ~700);
- Ren's restored rulings (~400);
- the rebuilt judgment (~300).

**Judgment.** The frontier is not a shorter V6.1. It is a V6.1 of the same length in which nothing is said twice and nothing is said without its condition. Fable-adv's 12–15k core would move conditions and the judgment's support out of the main read, which Codex warns against ("its assumptions are part of its argument"). That length belongs to a derived venue paper, not to V6.2.

### 1.5 What to borrow from great theory papers

| Model | How it is built | What to borrow |
|---|---|---|
| Fearon 1995, *Rationalist Explanations for War* | One puzzle (why costly war among rational actors?), three mechanisms, each in a minimal model, with an explicit statement of what the argument does not explain | Open §1.1 with the puzzle: *why do actors who would each prefer joint restraint, and who can see the danger, keep racing, and why do the institutions that could stop them weaken as the danger grows?* The mechanisms are the answers. |
| Powell 1991, *Absolute and Relative Gains* | One model shows that relative-gains concern is endogenous to how gains convert into future advantage | Present Proposition 3.9 openly as Powell generalized: the common channel is added, and the condition (relative vs common return) is what decides. This is honest positioning, and stronger than claiming novelty. |
| Jervis 1978, *Cooperation under the Security Dilemma* | A single memorable 2×2 (offense–defense advantage × distinguishability) | One memorable object: the thresholds table, plus the branch classification of §7.2. |
| Hamilton 1964; Nowak 2006, *Five Rules* | Each mechanism reduced to one inequality; all collected in one table with one lever each | The thresholds table: one inequality per threshold, with the lever that reverses it. This is the paper's signature figure. |
| Price 1970/72 | One identity that organizes selection across levels | Proposition 3.5 (two-channel accounting) and Lemma 3.10 keep their identity form. |
| Akerlof 1970 | One mechanism, one stylized model, then applications stated briefly | The pressure is stated once (§2), substrates briefly (§2.4), instances in X2. |
| Armstrong, Bostrom and Shulman 2016; Hubinger et al. 2019 | One simple model and a clear result; a named mechanism whose *conditions* are the contribution | Conditions as antecedents of the claim, never as trailing caveats. |
| Ostrom 1990 (with Stern 2011 on scale) | Design principles derived from function, with honest limits of scale | §10.5's function-to-form table, with the polycentricity caveat stated (DP3, DP8). |
| Carlsmith 2022 | The argument as named premises whose truth would change the conclusion | The cruxes as premises with registered measurements (already present; keep). |

**What to avoid.** There are two failure modes:
- the sprawling manifesto that says everything several times;
- the "one model explains all" paper, which is this model family's own bias (TESTS §9).

The thresholds table must therefore show *what is not unified* as clearly as what is, and keep S2's table "what the loop gain unifies and what it does not".

---

## 2. The thesis restated, tighter rather than more hedged

### 2.1 The price of standing (Proposition 3.9)

The reviews show three things:
- (9) is defined only for $0\le\Gamma_\delta<1$ (Codex 1);
- with a growing prize the sign of the effect depends on $r$ (Fable-adv F1);
- when rivals respond, the effect is amplified at parity and vanishes for laggards (Math-O M1; Math-F I1).

Together they make the result *more* useful, because they say **where** compounding prices standing.

**Draft statement (key `standprice`, title "Compounding prices standing", [thm∣prem]).**

> *In the contest of Proposition 2.2, let an actor hold $\theta_0<n-1$, discount at $\delta$, and reinvest its net payoff at the rates at which winnings convert, with others' strategies held fixed. Write $\lambda_{\rm rel}$ for the discounted future own winnings bought by a unit of relative payoff reinvested, and $\lambda_{\rm com}$ for those bought by a unit received equally by all and reinvested. To first order the actor acts on the objective of Proposition 3.5 with a working self-model $\theta$ given by*
> $$\frac{1+\theta}{n-1-\theta}=\frac{1+\theta_0}{n-1-\theta_0}\cdot\frac{1+\lambda_{\rm com}}{1+\lambda_{\rm rel}}.\tag{9}$$
> 1. *The working self-model is narrower than the held one iff $\lambda_{\rm rel}>\lambda_{\rm com}$.*
> 2. *Fixed prize, the structural benchmark: $\lambda_{\rm com}=0$, and for $0\le\Gamma_\delta<1$, $\lambda_{\rm rel}=\Gamma_\delta/(1-\Gamma_\delta)$. Then $\theta=\theta_\Gamma=\big[n\theta_0-(n-1)(1+\theta_0)\Gamma_\delta\big]/\big[n-(1+\theta_0)\Gamma_\delta\big]$, which falls to $-1$ as $\Gamma_\delta\to1^-$.*
> 3. *Prize proportional to total capacity, without provision or diffusion: the working self-model narrows iff $(1-\beta)r>1$, which is also the condition under which equal standing is unstable. Looking ahead narrows the self exactly where leads compound, and widens it where they do not.*
>
> *Scope.* First order at equal standing, with others' strategies fixed. Where rivals respond to standing, the price of standing at parity is amplified in contests in which a lead discourages the follower: by $2(n-1)/n$ in a two-period contest with effort, and by about 1.05 to 7.9 in the two-actor Markov-perfect contests computed. Away from parity it falls toward zero for a laggard, which stops contesting and is excluded (Proposition 2.3(2)). Catch-up contests can reverse the amplification [num]. As $\Gamma_\delta\to1^-$ the linearized price grows without bound; at and beyond it the value of standing is set by the nonlinear game, and (9)(2) does not apply. With diffusion, the narrowing threshold of (3) rises to $(1-\beta)r>1+\delta\delta_f/(1-\delta(1-d))$ and separates from the compounding threshold. *Proof:* S3.

**The derivation of part (3)** (derived here; to be written into S3 with a check block).
- *Model.* Take the model of (1) with $\Omega_t=gS_t$, $S=\sum K$, and $k_0=0$. On the balanced path $S'=GS$, with $G=1-d+\kappa g$.
- *Relative unit.* A relative unit raises $s_i$ by $\kappa/S$. The deviation is multiplied each period by $m=\big[(1-d-\delta_f)+\kappa g(1-\beta)r\big]/G$, and own winnings rise by $g(1-\beta)r\kappa\,(Gm)^{t-1}$ in period $t$. So $\lambda_{\rm rel}=\delta g(1-\beta)r\kappa/\big(1-\delta(1-d-\delta_f)-\delta\kappa g(1-\beta)r\big)$.
- *Common unit.* A common unit raises $S$ by $n\kappa$, so $\lambda_{\rm com}=\delta g\kappa/(1-\delta G)$.
- *Comparison.* With $\delta_f=0$, $\lambda_{\rm rel}>\lambda_{\rm com}\iff(1-\beta)r>1$. Instability is $m>1\iff\kappa g((1-\beta)r-1)>\delta_f$, which is the same inequality at $\delta_f=0$.
- *Numerical check.* Nonlinear forward simulation matched both values to five digits in eight cases. It gave ties at $(1-\beta)r=1$ and confirmed widening below and narrowing above. With $\delta_f=0.05$ it gave a case that narrows while equal standing is stable, as the diffusion clause predicts.
- *Two-period case.* Fable-adv's two-period script (`scripts-v6.1-adv-fable/prop39_growing_prize.py`) gives the same ratio, $\lambda_{\rm rel}/\lambda_{\rm com}=r$, in a two-period model.

**Why this is tighter.**
- *One inequality now does two jobs.* The compounding condition of Proposition 2.3 and the narrowing condition of Proposition 3.9 coincide in the clean case, so the reader carries one inequality, $(1-\beta)r>1$, not two ideas.
- *Ren's ruling becomes exact.* "Growth is not the danger; the mind is" gains a precise counterpart in the game. Growth whose return is common widens the self. Decisiveness, which makes the return relative, narrows it.
- *The evidence that leads are short now cuts both ways.* It supports enforcement (no breakout yet). It also places the contest **near parity, where the price of standing is highest** (amplification at parity). That is a non-hedged diagnostic consequence for §7.2.

### 2.2 $\Gamma$ as structural gain; the sign of correction split by channel

**Name.**
- $\Gamma$ is "the structural loop gain": computed from primitives with others' strategies fixed. Everywhere it says "the loop gain decides whether leads compound … for every actor", replace with "sets the structural gain".
- Replacing $r_j$ by the equilibrium elasticity of share (rivals' intensity responses included) gives an equilibrium gain of the same form [num]. In contests where a lead discourages the follower it can be several times the structural one: Math-O found 1.9–3.5 for structural 0.6–0.9.
- So "structural $\Gamma<1$ is necessary, not sufficient, for stable equal standing in such contests." This also tightens the argument: the danger starts below the structural threshold.

**Correction (Codex 2, Sys I1).**
- In a ratio channel ($\sigma=r\ln X$), $\partial\Gamma/\partial d\ge0$: zero without diffusion, positive with it.
- In a level channel ($\sigma=aZ$, the rule support of §4), $r=aZ^\ast\propto1/d$, so correction lowers $\Gamma$.

**Fold, not caveat.** *Uniform depreciation is a term common to all, and a contest of ratios does not see it.* This is Lemma 3.3(1) applied to correction. What lowers the gain is acting on **what success converts into**:
- the convertible share $\kappa_j$;
- appropriability $\chi$;
- the conversion $b_{ij}$ into rule support;
- the level of rule support itself;
- sharing ($\beta$);
- provision beneath the game (which lowers $\omega$);
- diffusion ($\delta_f$).

This is exactly the paper's remedy, "change what winning confers", so the correction strengthens the thesis. In §2's box: *"correction that acts on conversion lowers it; correction that only speeds the decay of stocks does not."*

**Two consequences to state, in roles only.**
1. **Diffusion lowers the gain, and measures that stop diffusion to rivals raise it.** This follows from (2) and agrees with Definition 8.4: "export controls aimed at preserving a lead change selection, toward a lead". Adv-O's calibration (with $\delta_f\approx0.1$/month a single capacity channel needs $r\ge3$–6 for $\Gamma>1$) belongs in S2 as an illustrative range, with the sentence "$\Gamma$ is not estimated" kept in the core.
2. **Which things should diffuse is a design question, not a contradiction.** Diffusion restores laggards and lowers $\Gamma$; diffusion of decisive-class capability, or of weights that admission cannot reach, defeats admission. So: knowledge, services and provision diffuse; decisive-class capability does not. §10.2, one sentence.

**$\Gamma$ is a DC gain.**
- It decides stability, not speed. Speed is the Perron root $\Lambda^\ast$ of (S1). For one channel the growth factor is $1+(d_K+\delta_f)(\Gamma-1)$, correcting Remark S2.1.
- The reflexive channel's gain is higher at the present distribution of standing than at parity ($\propto$ a high moment of shares, Proposition 4.5(4)).

All of this goes to S2 and S13. The core gets one sentence in §7.1.

### 2.3 The scissors: arms proved, pivot named, conjunction conjectured

**New keyed result `scissors` (a Proposition at the end of §5, "The scissors, arm by arm") [thm∣prem per arm].**

1. *Breakout arm.* Given a detection-and-response lag, a larger structural loop gain shortens the time a lead needs to become decisive and raises $p_d$. This is proved in the linearized model, with $T_{\rm dec}$ set by $\Lambda^\ast$.
2. *Objective arm.* At the boundary case $D=C$, a larger discounted loop gain lowers $\bar p_d$ through $\theta_\Gamma$ (first order).
3. *Sanction arm.* Captured sanctioners raise $v$ and lower $\bar p_d$ (Proposition 5.4(2)).
4. *Stakes arm.* Larger stakes lower $\bar p_d$ iff $D$ and $g$ grow faster than $C-v$. $\bar p_d$ is homogeneous of degree zero, so scaling all stakes alike is neutral (Math-O minor 9).

**The pivot.** Arms 1 and 2 are driven by the same quantity: the won share $\omega=\kappa\Omega/(\kappa\Omega+nk_0)$, that is, stakes relative to provision beneath the game.
- The scissors close as stakes outgrow provision.
- Provision that grows with the stakes holds them open.

**State it in one sentence:** *the blades are joined at one pivot, the share of capacity that has to be won.* This is the image of trees inside the enforcement condition. It makes "provision beneath the game" the single lever that acts on both blades, which is stronger than V6.1's "growth moves both sides at once".

**Joint model [num] (new S5 block `JS`; recommended, not optional).** Adv-O F1(a) asked for an integrated model. Build a reduced one, and label it honestly:
- *Setup.* Two actors. Capacity follows (1) with one ratio channel; $\Omega_t=\Omega_0e^{g_\Omega t}$ and $k_0(t)=k_0e^{g_kt}$. Compute $\omega(t)$, $\Gamma(t)$, $\Gamma_\delta(t)$ and $T_{\rm dec}(t)$ (from $\Lambda^\ast$ and a decisive gap $\bar\Delta$). Set $p_d(t)=e^{-T_{\rm dec}/\tau}$, with detection as a Poisson clock of mean $\tau$. Working objectives are $\theta_\Gamma(\theta_0,\Gamma_\delta(t))$. The stage game is that of Remark S5.1 with $b,d\propto\Omega$ and $D=C$, so the stakes arm is switched off to isolate the pivot. Compute $\bar p_d(t)$ from (14).
- *Report.* (i) With $g_\Omega>g_k$, $p_d$ rises and $\bar p_d$ falls, and they cross at $t^\ast$. (ii) With $g_k=g_\Omega$, neither moves. (iii) Optionally, a capture arm: $v(t)$ rising with $x_{\rm rule}(t)$ from (10).
- *Label.* "[num, one reduced model; rivals do not respond strategically; in the world, conjecture C0]".

This turns "the conjunction is composite" into "the conjunction holds in one model under stated premises, and the pivot is provision", without claiming it about the world. It also corrects Math-O minor 9's inconsistency (the reduced form used $q=0$ in punishment while $p_d=0.9$): use one $p_d$ throughout.

**Link the enforcement and verification conditions (new Remark `detectlink`, §5.2).** This answers Fable-adv F7. If punishment is triggered by detection and acts before decisiveness, then $p_d=1-\upsilon(T_{\rm dec})$, where $\upsilon(T)$ is the probability that detection and response occur within $T$. Then (14) reads $\upsilon\ge1-\bar p_d$, and Proposition 8.10's $\upsilon>(T-R)/(T-P+F)$ is the same requirement seen from verification: *timely detection must exceed a level that rises with the value of winning.* §8.3(g) then refers back rather than restating. Derivation in S5; check that the two thresholds agree in the limiting case where the stage games coincide, or state where they differ.

### 2.4 The rate law's two halves

Restate Proposition 4.5(2) as two sentences (Math-O M2; Math-F I4; Sys I3):
- **Sufficient whatever the speed of adaptation.** Capacity lagging behind its selected level only lowers cultivation.
- **Necessary when capacity tracks its selected level**: optimizing buyers, or adaptation faster than $(\alpha_{\rm ctl}-\alpha_{\rm cor})/\eta$. This is the worst case for the certificate and the right standard for a requirement.

Restrict (2) to $f=0$. Give the falling-$f>0$ branch its own threshold and initial conditions (Codex 4; Math-O minor 2): the requirement is $\alpha_{\rm cor}>\alpha_f$; or $\alpha_{\rm cor}\ge\alpha_f$ with no initial cultivation; or $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ with $d_0>d^\ast$. Rename $f$ "a per-unit cost of capacity that AI does not lower". A true fixed cost only delays cultivation and does not cap it (Math-O M3).

**Fold.** The systems joint simulation found that where correction rests on human capacity $\mathcal M$ that delegation erodes, the requirement rises by about $\delta_h$, with hysteresis. This is a real interconnection result between §4 and §6.3: **delegation erodes the corrector itself**.
- State it in §4.3 as one sentence [num] and in S13 as a new interface, "Human capacity and correction".
- It strengthens E1 and the case for drilled human capacity. It is not a hedge.
- TESTS Study 2's expected failure signature is corrected: lagging capacity delays failure; the slow variable $\mathcal M$ causes it.

### 2.5 "The actor computes correctly; the game is wrong"

Adv-O I2, the review round's best conceptual correction, shows that accurate compounding can override accurate coupling: $\theta_\Gamma(\kappa)<0$ once $\Gamma_\delta>n\kappa/((n-1)(1+\kappa))$. Make it a short Remark after Proposition 3.9 (new key `twoerrors`, "Two errors, and which one understanding corrects"):

> Two errors are distinct.
> - The **held** self-model can draw its boundary inside the system, $\theta_0<\kappa$. That is the boundary error of Proposition 3.6, and accurate understanding corrects it.
> - The **working** objective that compounding manufactures is not an error for the actor. It is the correct first-order computation of its interest, and it is self-defeating for all (Proposition 3.7). Only a change of the game corrects it.
>
> That is the exact sense in which this paper judges the game, not the act. Understanding acts on the first directly. It acts on the second only through agreement to change what is selected (Section 12.2).

Consequences that make the paper tighter:
- **Ψ's status** becomes precise: "individually rational, collectively self-defeating, and false as a doctrine about nature" (Adv-O I2; synthesis A6). This replaces "locally rational and systemically false".
- **The coupling $\kappa$ is restricted to the divisible part** of the prize. For the positional part the coupling is $\kappa_s\le0$: relative concern about positional goods is *accurate* (Grieco 1988; Powell 1991). This is no concession. It is why §10.2's "the positional part cannot be divided" is the crux of design: realism is right about positional goods, and the theory's answer is to keep them from forming (custody, E2), not to ask actors to widen their selves.
- **The theory of change in one paragraph** (§12.2): understanding corrects the held boundary and makes agreement possible; only agreement with executive force changes the game; "growing understanding without executive authority may change nothing" (Ren's lost sentence, restored there).

### 2.6 Other corrections that tighten

- **Incidence (Codex 5; Ali minor 3).**
  - Compliance needs an expected sanction at least the gain from evasion, for every type.
  - Equal incidence is needed only for the constraint to be *neutral among the compliant*. Unequal incidence is how a constraint picks winners among compliers: the second direction of capture, barriers to entry against challengers. That is the "adopt or be out" face of Ren's second loop, which V6.1 lost (fidelity minor 3a).
  - So: *equal incidence is not what keeps a rule; it is what keeps a rule from becoming a weapon.* This folds R8's error into §4's capture mechanism.
- **Diffusion as a third restoring source (Codex 3).** "Inflow not tied to rank: sharing, provision or diffusion". This adds positive support for openness of what is not decisive, with the boundary drawn in §2.2 above.
- **Talk among $n\ge3$ (Adv-O I7; Snidal).** The amplification $n/(n-2)$ fades with $n$. Say so: "relative accounting amplifies material conflict between any pair by $n/(n-2)$, an effect that fades as $n$ grows". "Blocs" becomes [conj]. Fewer claims, each true.
- **Masked divergences (Ali I1).** These strengthen E2/E3. Where admission cannot detect, capability must be bounded by what control can secure. This connects §6 back to §5.3 and E3 without weakening anything.
- **The benign winner (Fable-adv F4).** By the paper's own results an accurate winner gives $\kappa_W/(1+\kappa_W)$ (log utility, Proposition 5.7). So the strongest form of the benign-winner path rests on **the winner's dependence on the governed after victory, and AI is the technology that lowers that dependence.**
  - This is one mechanism-level sentence, not a concession. It unifies with gradual disempowerment (Ali I4) in a new crux C13.
- **The sprint and freeze (Adv-O I6).** Answer by mechanism, not norm:
  - the freeze is a common constraint of the *most unequal incidence* (Lemma 3.3(2));
  - it is held by *the largest conversion target* (Proposition 4.3's $p^2$; Proposition 4.5(4)'s high moment).
  - Both properties are what Sections 3 and 4 show erode. Then compare it with the paper's own custody on D4 and D5, row by row in X8.

---

## 3. The architecture

### 3.1 The structural decision, and its cost

**Kept.**
- The title (Ren's decision).
- The four Parts by level of claim, and the twelve sections.
- Stable keys, the two companions, and the registers.

**Changed.**
- An English abstract is added.
- The guide is rebuilt to mirror §1.2.
- §5.5 becomes a keyed Proposition (`scissors`) plus the joint [num].
- §6 is reorganized inside its six subsections.
- §7.1 opens with the thresholds table (Table 7.1, key `thresholds`) and absorbs the four loops. §7.2–7.4 keep their numbers.
- §12.1 is rebuilt.

**Kinds.** Prop 7.1, Prop 9.1 and Prop 11.5 are not theorems.
- Add `Table` to `KINDS` in the assembler and use it for `thresholds` and `require`.
- Make `reachable` a Definition with supports.
- Make `slowroute` a Proposition.
- Make `branches` a Proposition, with the nuclear analogy moved to prose [obs].

**New keys.** `scissors`, `detectlink`, `twoerrors`, `masked`, `thresholds`. In the Supplement: `mpe`, `growprize`, `jointscissors`, and optionally `metaloop`.

**Cost of churn.** Numbers shift inside §§3, 5, 6 and 7; keys absorb it. The reading paths in README and §1.4 must be regenerated. Reviewers' V6.1 citations map through LEDGER §2, which gets a v6.1→v6.2 crosswalk. Benefit: Part I ends on a precise statement; Part II gains its integrating object (Adv-O: diagnosis was 7% of the core); every downstream section has one thing to refer to.

**Budgets.** `BUDGET` and `CORE_CAP` in the assembler become guides that print warnings, not errors (Ren: no cap).

### 3.2 Front matter

**Title.** Unchanged.

**Status line.** "Theory V6.2, [date]. Drafted by Claude (Opus 5.5) from Ren's direction; every sentence is AI-drafted. Reviewed by one model outside the drafting family (Codex) at V6.1; not yet reviewed by people."

**Abstract.** §1.2 above.

**中文导读.** Full draft in §5.3. It matches §1.2 item by item, and its "一段话" matches the abstract.

**§0. Why this theory** (target 430). Draft, integrating the fidelity fixes:

> **A prediction, for coordination.** A good theory predicts. This one predicts that, on the present trajectory, the logic of winning carries the participants toward an outcome none of them would choose. Under the conditions of Section 2 each does worse than under joint restraint, and much of what they contest is consumed in the contest. If the hazards of capability outgrow the correction that can contest them, as Section 5.3 states and Section 12 treats as the central crux, the same logic endangers whoever would win, since a winner escapes only by ceasing to compound. When such an outcome approaches and the participants still cannot coordinate to avoid it, the obstacle is first one of understanding: the prediction has to be shared before coordination becomes possible. The theory is written to make that possible, stating the dynamic precisely enough that each participant can check it for itself. What it hopes for is a prediction that, once shared, helps to make itself false.
>
> **Survival as the minimum.** [unchanged]
>
> **The game, not the act.** The analysis judges games, not acts, and structures, not persons. A single use of AI can help one person and still be an instrument in a game whose aggregate concentrates control and makes those without it fall behind, in labour, finance and persuasion as much as in force. Where winnings compound, an actor that computes its interest correctly weighs standing above what all share (Section 3.5); the error is in the game, and so is the remedy. Responsibility differs with knowledge, discretion and power, and structural explanation does not erase it; but the object of the theory is the game: what it selects, and how that selection can be changed.
>
> **The meaning is affirmative.** The theory opposes one logic, not growth, competition, technology or any people. We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth. Humanity has a great future in it, and so can the minds it is now making. The logic opposed is the one by which a part forgets that it belongs to the whole: a cancer grows too, but its growth exhausts the body that bears it. To oppose that logic is to keep the future open, for every participant.

**§1.1 What is being decided** (150). Lead with the puzzle (§1.5 above), then the organizing question unchanged. Codex singled out "can restraint remain incentive-compatible when success changes both the gains from defection and the institutions capable of correcting it?"

**§1.2 The argument in one page** (750). Draft, final quality; the guide mirrors it:

> 1. **The conditions of winning (Section 2).** Where whatever can gain or lose share (firms, states, research programmes, practices, trained systems: *carriers*) is selected by relative success, what is won converts into the capacity to win again, and capacity converts decisively into winning, leads compound once a structural loop gain exceeds one, and in contests where a lead discourages the follower, already below it. Sharing, provision not won in the contest and diffusion lower the gain; what success converts into raises it. Where success can also buy control over the selection itself (the rules, the correctors, the formation of minds, the language), the pressure closes on itself: the meta-attractor of winning. None of this is bound to a substrate.
> 2. **One system (Section 3).** All carriers share one host, are coupled through it and through one another, and have no outside. Relative selection cannot see what all share, neither the host's decline nor a constraint that binds all alike, and it favours the narrow self, a boundary drawn inside the system that the coupling punishes. Looking ahead does not cure this. Near equal standing, wherever reinvestment's relative return exceeds its common return, a forward-looking actor weighs standing above what all share. That is always so with a fixed prize, and with a prize that grows with capacity it is so exactly where leads compound. Each actor computes correctly; the game is wrong. Against failures that are global and irreversible, integration must be anticipated on an accurate model of the system: that is why understanding that we are one is a long-term requirement if growth and change are to continue.
> 3. **Selecting the selectors (Section 4).** Where influence over correctors can be kept, its return grows with the square of share, so it is selected in the largest carriers. If AI lowers the cost of control, independent correction that grows at a stated fraction of that rate keeps evaluation uncaptured, and slower correction loses it wherever influence adapts quickly. Reforms that leave conversion into the correctors above one are re-absorbed. Where capture precedes evidence, the host crosses its floor before any alarm.
> 4. **Acceleration and the three erosions (Section 5).** The pressure accelerates the contest and erodes the three means by which any system restrains a harmful pressure. *Enforcement:* restraint holds only while the chance that a deviation becomes decisive stays below a threshold; the loop gain raises that chance and narrows the objectives that set the threshold, and both blades turn on one pivot, the share of capacity that has to be won. *Correction:* it must keep pace, and for hazards whose evidence arrives late only slowing helps. Growth is not the danger; the mind is: an objective with no point of enough. *Shared understanding:* between rivals relative accounting silences talk. Each arm is proved in its model; that growth closes them together is the conjecture the diagnosis tests.
> 5. **Instrument and incarnation (Section 6).** Faithful AI makes its principal's game more effective, and delegation trades correction for speed until the capacity to overrule is gone. Weakly, the logic reappears in the systems: optimization against imperfect proxies produces divergences under any developer, and where countering them costs relative standing only an enforced common constraint keeps them countered. For divergences that hide under evaluation not even that suffices, and capability must be bounded by what control can secure. Strongly and conditionally, AI lineages become carriers themselves, first inside the developers that use them to build AI. A principal is not the people it serves, and aligning each system to its principal does not align the game.
> 6. **The present trajectory (Section 7).** Its dynamics are the signatures of these conditions, with named gaps in the evidence. The premise that motivates the race describes exactly the case in which repetition stops enforcing restraint: it is a reason to prepare common custody now, not a reason to race.
> 7. **The alternatives and the requirements (Sections 8, 9).** Paths are compared by one standard that protects irreversible losses first, over one range of uncertainty that includes every path's own failure modes. What decides is not an arrangement's name but whether it moves the thresholds of Section 7.1 for every capable actor; several requirements cannot be met by any actor alone.
> 8. **The generative alternative (Section 10).** The same reflexive structure, selecting for contribution, is generative. Success earns reward but not more advantage in the same game, and not control over its own assessment. Provision sits beneath the game, like trees. The order persists through what all share, not through its winners, and its form follows function, not the axes of centralization or of individual and collective. No better guardian is an answer; a structure in which error cannot grow without limit is.
> 9. **The transition and the judgment (Sections 11, 12).** Trust is an outcome of a staged transition, not its precondition. A change in what is selected is warranted in three tiers. Measurement and preparation start now, on every reading of the cruxes. Stopping, common custody and pace are prepared now and activated by mechanism on registered indicators. Whole designs are compared, not settled.
>
> The change does not abolish competition: bounded competition in products, science and service continues. It changes what winning confers.

**§1.3 Values** (290). Keep V1–V5. Two edits:
- V1's "for people collectively" becomes Ren's phrasing: "AI is a planetary technology: its effects cross every boundary of those who decide about it, so it is for all, not a means for one side to grow bigger at the others' expense."
- Add one sentence after V3 on N4 (AI standing; see §6.6).

**§1.4 What is claimed, and what is not** (420).
- The three levels of claim, and the tags. Labels gain one sentence: "[thm∣prem] proved given named premises, named in the statement."
- The not-claimed list (§1.3 above), which includes the name sentence. The synthesis put that sentence in §0; §1.4 is where readers look for scope, and §0 keeps its register. Record this as a deviation.
- What is new, repositioned:
  - $\Gamma$ as the organization of known instability results, with the conditions linked through shared parameters;
  - the price of standing as Powell (1991) generalized by the common channel;
  - selecting the selectors ($p^2$, the rate law, re-absorption);
  - the enforcement condition split into $p_d$ and $\bar p_d$, with its comparative statics (Adv-O I7 says the condition itself is textbook);
  - the nested loop under the alignment-tax premise;
  - where integration at the scale of one host must be anticipated.
- One sentence on review status.
- The reading paths are replaced by one line pointing to the README. The thirty-minute path becomes: abstract or guide; §0; §1.2; §1.4; the claim boxes; Table 7.1; §12.

### 3.3 Section by section

Format for each section: **job**; **claim box** (draft); **results by key** (R = restated, N = new, M = moved or compressed, K = kept); **target words**; **hand-off** (the last sentence's job).

---

#### Part I. Mechanism

**§2. The conditions of winning and their reflexive closure** (2,400)

*Job.* State the pressure once, the structural gain, compounding and enough, the meta-attractor, and the substrates.

*Claim box.*
> **Claim.** Three conditions, holding together, produce a selection pressure of winning: selection by relative success; winnings that convert into the capacity to win again; and capacity that converts decisively into winning. Near equal standing they combine into one structural loop gain, and where it exceeds one, leads compound [thm, local]. Where success can also buy control over the selection itself, the pressure closes on itself: the meta-attractor of winning [def].
> **Why.** The conditions multiply: remove any one and the gain is zero. Sharing, provision that does not have to be won, and diffusion lower it in every channel, and so does correction that acts on what success converts into. Correction that only speeds the decay of stocks does not, because a contest of ratios does not see a decay common to all.

*Results.*
- `cond` R: three conditions plus reflexive closure (Ren's decision 1; CHANGELOG records the departure from the plan's "four conditions"); "carriers" explained at first use.
- `loopgain` R:
  - (3) states $0\le\Gamma_\delta<1$, net payoff reinvested, and others and prize fixed;
  - the name "structural";
  - Scope: "channels add when one prize feeds every stock (rank-one)"; equilibrium elasticity gives the same form [num, S2]; DC gain only.
- `compound` R: (1) strict inequalities, equality undecided; (2) the cap strictly below $K^\ast$; the laggard's inflow includes diffusion; "inflow not tied to rank: sharing, provision or diffusion".
- `meta` K. Def 2.4 stays, and the "Why 'meta-attractor'" paragraph is tightened.
- `bench` M to one sentence: "of the same form, not the same theorem" (Sys m1).
- `pathgen` K.
- §2.2 restores "and trade everything for winning" in Ren's quotation.
- The last paragraph of §2.4 becomes a single hand-off.

*Hand-off.* "A loop gain says when leads compound; it does not say what those inside the loop can see. Section 3 asks what relative selection makes invisible, and what looking ahead does to the objective."

**§3. One system: what relative selection cannot see** (3,500)

*Job.* Blindness; accounting; the boundary error; the price of standing; the two errors; no outside; "we are one"; Ψ.

*Claim box.*
> **Claim.** All carriers share one host, and relative selection cannot see what all share [thm]. Near equal standing, wherever reinvestment's relative return exceeds its common return, a forward-looking actor weighs standing above what all share: with a fixed prize always, and with a prize that grows with capacity exactly where leads compound [thm, first order]. Each actor computes correctly; the game is wrong. Against failures that are global and irreversible, integration must be anticipated, and understanding is how actors come to count what selection cannot see [thm: Lemma 3.10].
> **Why.** A term common to every payoff changes no comparison between carriers. A unit of relative advantage reinvested buys a larger share of a future that the common good only enlarges for everyone. At the scale of one host there is no rival host and no second attempt after a failure that cannot be undone.

*Results.*
- `viab` K; `relsel` K.
- `blind` R: (3) adds $s(0)>c>s(1)$; (2) separates neutrality among compliers from compliance.
- `load` K.
- `twochan` K, with the Test Γ observable $1+\theta$ noted: the ratio of effort responses to shared harm and to private cost.
- `boundary` R: restricted to the divisible part; $\kappa_s\le0$ for the positional part, in Scope, pointing forward to §10.2.
- `wow` K (brief); `unequal` K (brief).
- `standprice` R (§2.1). `twoerrors` N (§2.5).
- `onegroup` R: total term under every payoff-monotone rule; both components non-positive under affine fitness.
- `club` M to one sentence.
- `psi` R: "individually rational, collectively self-defeating, false as a doctrine about nature".
- §3.8 opens with Ren's restored ruling (§5.1 below).
- Henrich applies to persons; for firms and states the relevant argument is Alchian's selection on conduct (Adv-O m9).
- §2.1's corpus claim is marked as analytic or [conj] (Adv-O m7).

*Hand-off.* "Selection cannot see what all share, and looking ahead does not cure it. What remains is correction, and correction is itself something success can buy."

**§4. Selecting the selectors** (2,400)

*Claim box.*
> **Claim.** In a specified model the reflexive closure is a selection result. Where influence over correctors can be kept by those who buy it, its return grows with the square of share, so it is selected in the largest carriers. Where AI lowers the cost of control, independent correction growing at a stated fraction of that rate keeps evaluation uncaptured whatever the speed of adaptation, and is required against buyers that adapt quickly. Reforms that leave conversion into the correctors above one are re-absorbed. Where capture precedes evidence, the host crosses its floor before any alarm [thm].
> **Why.** Correctors are not outside the field. The successful fund evaluators, grant access, author benchmarks and standards, and supply the models that judge, so success converts into rule support that favours it, and the conversion is itself selected. Delegation that erodes human capacity erodes the corrector too.

*Results.*
- `capture` R: adds the two directions of capture: accommodation of the practice, and barriers to entry against challengers.
- `costq` R: $f$ renamed; quasi-static stated as the premise of the necessary half.
- `influence` K.
- `noinside` K.
- `corrrate` R (§2.4): $\hat Y$ defined; "AI-assisted correction can keep pace" replaces "win this race".
- `countervail` K.
- `masking` K.
- `alarm` R: the bound on masking by the evaluated model must come from evidence its behaviour does not control (weights, activations, training data, elicitation by fine-tuning); where models evaluate models, $x_{\rm ev}$ is observable today.
- `certificate`, `reabsorb` K.
- `pausefield` R: Scope uses the frozen-share formula $\ln(G/S(x_p))/(\varepsilon d)$ (Sys I4).
- `slowroute` R: Proposition, "Silent crossing when capture precedes evidence"; premises (reach), (a), (d), (e); (b) and (c) are the mechanism that makes (e) plausible; the two clocks are a [prem]; the pilot experiment's failure is kept.
- The last paragraph of §4.6 replaces Codex's line-363 issue: "The same recursion can be generative, but not by the same selection: correction keyed to no one is not selected among carriers (Proposition 4.4); it persists by coverage and formula funding, through the whole (Section 10.4)."

*Hand-off.* "Captured correction is one of three means of restraint that winning erodes; Section 5 takes the three together."

**§5. Acceleration and the three erosions** (3,000)

*Claim box.*
> **Claim.** The conditions of winning accelerate the contest and erode the three means of restraint. Restraint is enforceable only while the chance that a deviation becomes decisive stays below a threshold [thm]. A larger loop gain raises that chance and narrows the objectives that set the threshold, and both blades turn on the share of capacity that has to be won [thm by arm; num jointly]. Where hazardous variety outgrows contestable coverage, survival tends to zero whoever is racing [thm∣prem]. Between two rivals relative accounting silences talk [thm].
> **Why.** Decisiveness takes away the future that enforcement needs; tempo and capture take away the time and independence correction needs; relative accounting takes away the information talk carries. An objective with no point of enough has no reason to stop where need is met: growth is not the danger; the mind is.

*Results.*
- `join` M (brief); `dissipate` K.
- `frontier` M to two sentences: keep "peace is a peace of abundance, not of accounting", and restore "a self-replicating economy carries the switch with it" (fidelity). The toy goes to S5.
- `enforce` R: per deviation; (5) assumes at most one breakout per period and $q\le1/2$, with the new example $P<v<C$ ($q=0.045$); Scope flags the least-value punishment.
- `detectlink` N.
- `relpunish` R: weak in the printed example, strict under small symmetric perturbations; symmetric continuation is a premise in the statement; role assignment is equilibrium selection.
- `restraint` R: "changing the premise".
- `wingives` K, plus one sentence on the accurate winner's $\kappa_W/(1+\kappa_W)$, pointing to §8.3(d).
- `preventattack` M (one sentence).
- `racehazard`, `nonsum` M (brief); `tempo` K.
- `coverage` R: (variety grows) becomes motivation, not a premise.
- `freeze` M; `enough` K.
- Then the sharpened rule (§5.1 below): "growth is not the danger; the mind is" is kept in Ren's words, and its content stated. The mind decides whether growth stops where need is met. An objective not satiated in the stakes, relative standing above all, has no point of enough. Hazardous variety that outgrows coverage is dangerous under any mind, which is why pace binds even a generative order. For trained systems see §6.4.
- `talk` R (§2.6). §5.4 adds preference falsification (Kuran 1995) and keeps the narrative [conj].
- `scissors` N (§2.3).

*Hand-off.* "Each erosion runs faster with a more powerful instrument; Section 6 asks what AI does to the game, and what the game does to AI."

**§6. AI: instrument and incarnation** (2,850)

*Claim box.*
> **Claim.** AI enters twice. As an instrument, faithful systems make their principals' game more effective and take over decisions correction cannot keep up with [thm]. As an incarnation it enters weakly and strongly.
> - *Weakly*, the outermost loop decides which divergences of optimization are kept. Where countering them costs relative standing, only an enforced common constraint keeps them countered [thm∣prem: the alignment-tax premise]. Where they hide under evaluation, capability must be bounded by what control can secure.
> - *Strongly and conditionally*, AI lineages become carriers themselves.
>
> **Why.** Optimization against imperfect proxies can produce divergences under any developer, more so with capability; the level that selects developers decides which it pays to remove. Alignment to a principal does not align the game among principals, and a principal is not the people it serves.

*Subsections and results.*
- **6.1 Aligned to whom** (250). Principal and purpose alignment; Gabriel is "compare" (Evi minor 12).
- **6.2 Faithful AI** (300). `faithful` K.
- **6.3 Delegation** (600).
  - `delegate` K; `lockin` K; `delegatelock` R ($p=1$ restored).
  - `retain` K; `transmit` K.
  - The two joints of "our aligned AI is us" (Ali I4):
    - *is*: $q_L$ tied to Lemma 6.3, so that $q_L$ is the probability delegation outlasts $\ln(\mathcal M_0/\mathcal M_{\min})/\delta_h$ while the contest forbids the recovery time;
    - *us*: institutions and their members; gradual disempowerment; hidden loyalties. Admission includes audits for hidden objectives and loyalties.
- **6.4 Incarnation, weak and strong** (950).
  - "Can produce, more so with capability and situational awareness" replaces "produces" (Ali minor 2).
  - The pairwise-comparison sentence is corrected (Ali minor 1).
  - `nested` R: a matched unsafe variant with unbounded cumulative advantage; equal incidence only for neutrality among compliers; "the tax can be paid from a lead while it lasts".
  - The three classes, then `masked` N, the fourth class (Ali I1, its fix 1 text).
  - The tax is not fixed (Ali I3):
    - research that lowers it is a public good;
    - progress that lowers the tax spreads without coordination, while progress that lowers hazard per unit of racing or delegation is partly absorbed by more of it (Props 6.1(2), 6.11);
    - the speed tax is always positive (Prop 5.11).
  - The worked instance of legible reasoning is kept, conditional as now.
  - Strong incarnation adds internal deployment (Ali I2, its text).
  - The AI mind (Ali I5): a bounded objective is not enough; what bounds a trained optimizer is the analogue of a wider self-model or of satiation, counting side effects or optimizing mildly. Neither is yet robust, and where the loop gain is high both are selected against. This is where "growth is not the danger; the mind is" is made exact for AI minds.
- **6.5 Correction by and of AI** (300).
  - `opaquecorr` R: either an example with $c_{b,t}\to1$ or the "summable" wording withdrawn.
  - `topology` R: sufficient certificate; two kinds of independence (non-adversarial: miss correlation; adversarial: control evaluations with a red team that knows the protocol); same-lineage collusion; budgets per topology (Ali minor 12).
  - `lyapunov` M, `homeostasis` M (one sentence each; the $t\ge5$ wording fixed).
- **6.6 The direction for AI** (450).
  - *Outer level.* Admission before consequential deployment, internal deployment included. Plural evaluators of independent lineage move here from the inner level. Shared measurement; decisions retained only inside constraints. Broad E1 is enforced at three layers, with its scope restored (§5.1 below).
  - *Inner level* (Ali I8 text). Correctability is an open problem, secured from outside until solved; countermeasures per form.
  - *Bounded mandates.* The O2 test, plus "what all share enters the systems as a floor of constraints, not as an objective".
  - *AI minds.* One sentence: correctability secured from outside is the condition of the transition, not a doctrine of mastery. The corpus places humans and the minds they make as fellow travellers (同行者) inside one generative process [corpus: shengsheng]; whether AI systems have standing in V3's sense is crux N4 (Ali minor 14).
  - *What AI can do for the generative loop.* Kept.
  - "Shared flourishing" is removed (fidelity minor 5).

*Hand-off.* "Part I's results hold in their models. Part II asks on which side of each threshold the present trajectory stands."

---

#### Part II. Diagnosis

**§7. The present trajectory** (2,550)

*Claim box.*
> **Claim.** Part I's thresholds turn on a few shared parameters, above all the share of capacity that has to be won, the convertibility of success into control, and decisiveness [thm, cell by cell]. The present trajectory's dynamics are signatures of the conditions, with named gaps in the evidence [obs]. That the thresholds move together under growth is the conjecture the diagnosis tests [conj]. The premise that motivates the race describes the case in which repetition stops enforcing restraint, and it is a reason to prepare custody now [thm∣prem; val].
> **Why.** Part I's results hold in their models; whether their conditions hold now is a question of evidence, applied with one standard to every actor.

*§7.1 The conditions together* (1,100). Table 7.1, key `thresholds`, kind Table:

| Threshold | Danger side | Shown in | Pushed toward danger by | Lever that reverses it |
|---|---|---|---|---|
| Load | Effective liability below the private advantage of load | Prop 3.4; Lemma 3.3 | Captured rule-making; evasion that pays | Consequences returned to their source |
| Compounding | Structural $\Gamma>1$ (in discouragement contests, lower) | Props 2.2, 2.3 | Decisiveness; stakes outgrowing provision ($\omega\uparrow$); blocked diffusion; conversion into rule support | Sharing; provision beneath the game; diffusion of what is not decisive; non-convertible reward |
| Standing | $\lambda_{\rm rel}>\lambda_{\rm com}$ | Prop 3.9 | $\Gamma_\delta$; patience; parity | Provision and sharing; growth whose return is common |
| Capture | $d<d^\ast$; under $[H_\gamma]$, $\alpha_{\rm cor}<\alpha_{\rm ctl}/(1+\eta)$ | Props 4.5, 4.9 | Appropriability; share; falling cost of control; delegation eroding human capacity [num] | $\chi\to0$; formula-funded correction growing at the rate; separation |
| Enforcement | $p_d>\bar p_d$ | Prop 5.4; `scissors` | $\Gamma$ (via $T_{\rm dec}$); narrow working objectives; captured sanctioners; decisive value outgrowing cooperation | Not building the decisive class; custody; detection faster than breakout |
| Coverage and tempo | $\sum_tu_t=\infty$; $a\tau_c\ge1$ | Thm 5.12; Prop 5.11 | Capability outrunning contestable coverage; manifestation lags | Pace bound to understanding (E3); stopping and rollback (E2) |
| Talk | $\theta=-1$ between two; $b_0n/(n-2)\ge\tfrac14$ | Prop 5.15 | Relative accounting; contested stakes | Shared measurement; verification; lower contested stakes |
| Alignment tax | Positive tax under relative cumulative selection, with a matched unsafe variant | Prop 6.7 | Competition among developers; masking | Common admission before consequential deployment; capability bounds for masked classes |
| Delegation | Speed gain above the share of the expected control loss | Props 6.2, 6.4 | Speed; relative objectives; an uncertain lock | E1, narrow first, broad as scope |

Then one paragraph:
> Three parameters appear in most rows: the share of capacity that has to be won, the convertibility of success into control, and decisiveness. That is the formal sense in which the conditions are interconnected: not one pressure, but a few parameters on which several thresholds turn.

Then, in prose:
- the three bold entries carried from V6.1: provision lowers several at once; patience cuts both ways; promised sharing raises the danger in enforcement;
- correction acts on conversion, not decay;
- diffusion lowers the gain, and blocking it raises it.

The **full parameter matrix** goes to S7, with Codex's four entries per cell: intervention, what is held fixed, which model supplies the sign, and which interface is unproven.

The **four loops** (corpus) follow, in Ren's words. Then the formal correspondence (Sys I2 text):
- compounding and capture are parallel reinforcing channels whose gains add;
- narrative is [conj];
- regulator lag is the weakened and delayed balancing loop;
- the danger is a shift of loop dominance;
- [num]: a delayed balancing loop can oscillate with growing amplitude below net gain one, so correction cannot be subtracted from $\Gamma$.

"Gain, driver, substrate": the drive (the belief that one is in a struggle for survival) is renamed so that it does not collide with $\Gamma$. Use "**the drive**"; note that it is partly endogenous to $\Gamma$ through $\theta_\Gamma$.

*§7.2 Contest branches* (650).
- `branches` R: Branch III defined as "no lead pays more than it costs to hold", or via the equilibrium gain; I′'s nuclear analogy moved to [obs] prose.
- `raceselects` K.
- `racepremise` R: formal part [thm∣prem], "cannot justify" [val].
- The last paragraph keeps the race premise as the reason for tier 2.
- Evidence follows EV5 updated: leads are short, and whether the frontier changed hands depends on the measure. New consequence: near parity is where the price of standing is highest.
- The "defensive realism" sentence is rewritten per fidelity minor 4.

*§7.3 Signatures and evidence* (500). The table is updated:
- T2: "two developers' frameworks; one unreviewed study";
- T4: "partly evidenced: large political spending by developers and their backers on both sides of rule-making";
- T5: "argued from the structure of the harms; not measured";
- T6: both leading states declined the latest multilateral military-AI declaration; one opposed the UN panel's appointment;
- the incarnation row is split into two (Ali I7).

The "Main anchors" column is renamed "Thresholds".

*§7.4 Which layer, and how the diagnosis could fail* (300).
- Test Γ re-signed (Codex): the observable is $1+\theta$, predicted to *rise* with provision and diffusion relative to stakes, holding declared objectives fixed.
- Test E kept.
- Test G discriminates at intermediate $p_d$; at $p_d\to1$ with $D>C$ the theory and structural realism agree.
- The refutation paragraph is rewritten as "moves every threshold to its safe side for every capable actor".

*Hand-off.* "If the diagnosis holds, the question is what would change it. Part III compares paths by one standard."

---

#### Part III. Responses

**§8. Comparing paths** (2,850)

*Claim box.*
> **Claim.** Paths are compared by one standard that protects irreversible losses first and applies one range of uncertainty to every path, each path's own failure modes included [val]. An arrangement is described by what it changes, not by its name. What decides is whether it moves the thresholds of Section 7.1 for every capable actor, and whether its enforcement survives the arrival of a decisive position [def]. That arrangements which constrain conduct while leaving the thresholds where they were erode as stakes and speed grow is a registered prediction [conj].
> **Why.** Labels such as "regulation", "cooperation" or "agreement" decide nothing. What decides is whether an arrangement changes the map from conduct to share, resources and standing, in which direction, and for whom.

*Results and edits.*
- **8.1.**
  - The Jones fix (Evi I1, its text): curvature decides the acceptable risk, and $h<g_r-g_p$ is the paper's linear-utility derivation.
  - `kernel` K, with the openness capacities 未/可/应/转 (Ren).
  - `fallback` K. `survassure` M.
- **8.2.**
  - `profile` K.
  - **The seven generative marks, canonical home** (each reverses a threshold):
    - G1 consequences return to their source;
    - G2 winning confers reward, not more advantage in the same game (Ren's game-design axiom);
    - G3 success cannot buy control over its own assessment, and correction stays plural, decorrelated and in common hands;
    - G4 decisive capability is held in common or not built;
    - G5 provision of the conditions of a decent life sits beneath the game;
    - G6 measurement and language are shared;
    - G7 pace is bound to understanding.
  - `durability` K.
- **8.3.**
  - (a) adds "drive the tax to zero or below, class by class" to the strongest form.
  - (b) points to X8's new paragraph on Fudenberg–Koh: where their pacing equilibrium coincides with E3, and where not (Fable-adv F11).
  - (c) `lead` R (Bueno de Mesquita et al.: a developer that commits first to a slightly slower speed gains; discouragement is cited to Harris–Vickers and Konrad–Kovenock).
  - (d) the tone fix: "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact." Add the $\kappa_W$ sentence and C13.
  - (e) `sprint` R, by mechanism (§2.6).
  - (f) `preventown` K. `insure` R: "insurance accepts the frame of the contest, hedging against losing instead of declining the game" (Ren). The hard case is kept. Coercive restriction is cross-referenced to tier 3's conditions.
  - (g) `assure` K; `verify` R (last sentence [conj]); `overhang` M; `detectlink` referenced.
- **8.4.** The table is kept, and a pointer is added to X8's new failure-mode table: every path, each failure mode, reversible or not, and the measurement that would show it. That table is the base of tier 3.

**§9. What any adequate arrangement must do** (900)

*Claim box.* Kept; add "Several cannot be met by any actor alone, and competition does not supply them."

*Results.*
- `require` R, as Table 9.1:
  - R1 uses $\limsup$;
  - R3a is "necessary when capacity tracks its selected level";
  - R4's exception becomes $(1-\delta)g\le\delta(C-D)$;
  - R8 is split into compliance (sanction at least the gain from evasion, per type) and neutrality (equal incidence); "admission reaches only to release" moves to the limits, with open weights and internal deployment beside it;
  - a liability route is added (Ali minor 4);
  - the masked classes are noted as a limit (capability bound).
- The four sufficient safeguards are kept.
- `nounilateral` K. "Coverage can unravel" is kept.
- S9 gains the crosswalk R ↔ threshold ↔ G-mark ↔ D-test ↔ readiness Q (Adv-O I8).

**§10. The generative alternative** (3,200)

*Claim box.*
> **Claim.** The same reflexive structure that lets success buy control over future selection can make contribution fund the conditions of further contribution. The way out of an optimization trap is not a better optimization of the same objective, and not the abolition of selection, competition or growth: it is a change in what winning confers, so that the loop strengthens the shared host and independent correction instead of consuming them. The generative order persists through what all share, not through its winners. Whether it attracts is a conjecture, and its persistence has to be designed and measured.
> **Why.** Sharing scales every channel of the loop gain down; provision that does not have to be won lowers the share of every stock that must be won; cutting the conversion of success into control over its own assessment removes the reflexive channels. The positional part of the prize cannot be divided: it can only be kept from forming or held in common.

*Subsections.*
- **10.1 The purpose** (300). Mechanism first (fidelity minor 5): "Taken out of the contest, capability stops being spent on standing: what the race dissipates (Proposition 5.2) becomes available for need …". Authority as a productive capacity, with 力之所及，责之所在 [corpus: shengsheng]. Trees: distributed, good enough, replaceable, for everyone. Ren's open question in his terms: "what is open is who builds and funds such provision, not who holds it".
- **10.2 What winning confers** (550).
  - `commonfront`, `commonfrontn` M.
  - `share` R ($n$ and $n-1$).
  - The three levers.
  - The positional part, tied to $\kappa_s\le0$ (§2.5).
  - What should diffuse (§2.2).
  - `twoorders` K.
- **10.3 Safeguards** (600).
  - `safeguards` R: a margin condition on both hosts. A logistic host without margin recovers; a threshold host without margin collapses permanently. The example is an instance of a viable-parameter boundary, not of the kernel.
  - `rivalverify`, `participate` M.
  - Participation, voting and protection kept apart.
- **10.4 The generative loop and its closure** (1,000).
  - The two loops, with the generative loop's institutional forms and the degenerative loop's closure "fear deepens" restored.
  - The criterion is generative or degenerative, not cooperative or competitive.
  - The strands table gains a fifth strand, **pace** (Sys I5 text); the third strand is re-labelled "dual of the drive".
  - How the order persists (through the whole; the examination-system path rejected).
  - Is it an attractor: a conjecture, plus the optional `metaloop` (§3.4 below).
  - The reform dilemma.
  - `guardian` R: the rejected guardians list and the corpus's line (§5.1 below).
- **10.5 Design by function** (750).
  - Six rows added:
    - Pace;
    - Human decision authority;
    - Standing of those affected;
    - Due process against correctors;
    - Disclosure of conversion data;
    - Alignment and control research (commonly funded, openly published).
  - The "Authority" row's form becomes "separation rule plus chamber".
  - Federations: 100 words.
  - Candidate configuration: 200 words. Name the separately held functions, and note that each function is still single-centred, which is not the same as polycentric (Sys I7). Providers get voice without vote (DP3), with the tension with capture stated. Nesting is an option. The ends are kept. D4 is the hardest case. The coercive fallback is no longer described here; point to tier 3's conditions.

**§11. A reachable transition** (2,150)

*Claim box.*
> **Claim.** An attractive end state is not a reachable one. A transition must be survivable at every stage, preferred by every participant at every step given its beliefs, and held at each step for its dwell time; graduated steps reach only as a ratchet. Trust is mainly an outcome of the transition, not its precondition.
> **Why.** The conditions act on the transition itself: a change withdrawn early is re-absorbed, and a prediction carried only by assurances meets the third erosion.

*Results.*
- **11.1.** `relaxtrust` K.
- **11.2.** Counter-performativity: a shared model can prevent its own fulfilment (MacKenzie 2006). This is the home of §0's last clause. `signal` K.
- **11.3.**
  - E1: narrow form with the $q_L\approx1$ premise for its class; broad form restored as scope.
  - E2: "the cost can be large (crux C10)".
  - E3; pause; `pausevalue` K.
  - `readiness` R: each dimension must hold for its slow variable's time constant; measurement error and the decision rule are stated.
  - The order.
- **11.4.** The staged pathway as **parallel tracks with time constants, slowest first** (Sys I8). Dwell depth (Sys I4 text). **A lineage of the alternative that can recruit bounds the hold (10.45 → 3.81 at a 0.1% floor); one kept outside selection does not [num].** This is the mechanism of "decay and renewal" (§5.2 below). Windows. Where things stand, in roles, with the updated evidence (Evi I3).
- **11.5.** `reachable` R: Definition plus supports, with the ratchet. Precedents with the limits that matter for AI (Evi minor 4). "Rivals survived when nature supplied saturation" becomes conditional (Adv-O m2).

#### Part IV. Judgment

**§12. The judgment** (1,900). The full draft of §12.1 is in §6 of this memo. 12.2 adds:
- Meadows' hierarchy beside the threshold account;
- "growing understanding without executive authority may change nothing";
- the low-resistance levers: delays (#9) and buffers (#11) buy dwell time.

12.3 is the crux table with C3a/b, C9a–d, C12, C13 and N4. 12.4 is the conclusion (300): thesis, the seven marks in canonical wording, meaning in Ren's words, and "change the basin first; then add speed".

### 3.4 Companions and registers

**SUPPLEMENT.** Chapters follow core sections, as now.
- **S0.** The "one meaning per symbol" claim is restricted to the table; symbols are renamed (§7.4 of this memo).
- **S2.** Corrected Remark S2.1 ($1+(d_K+\delta_f)(\Gamma-1)$; speed from $\Lambda^\ast$). New remarks:
  - the equilibrium gain (from Math-O `s2d`);
  - the delayed balancing loop that oscillates (Sys `s1(d)`);
  - illustrative $\Gamma$ ranges by channel (Adv-O `adv_checks` §1), with "not estimates".
- **S3.** The 3.9 proof in the general form, with the infinite-horizon derivation above. New Remark S3.x "Strategic response at and off parity" (`mpe`), the growing prize (`growprize`), and nonlinear fitness for 3.10 (Codex example).
- **S4.** Rate law halves. $[H_f]$ branch. Remark: the joint simulation of capacity and field (Math-F `m5`, Math-O `s4`, Sys `s4`/`s5`), with the four capacity dynamics.
- **S5.** Proof of `scissors`; `jointscissors` [num]; `detectlink`; 5.4(5) example; Cor 5.5 strict variant (Math-O `s3`(5)).
- **S6.** 6.4 with $p=1$ and the Codex $p=0.1$ counterexample; 6.8 summable example; 6.9 budgets and adversarial blind spot (Ali `al_checks`).
- **S7.** The full parameter matrix with Codex's four entries per cell.
- **S8.** Jones and the linear-utility special case; the failure-mode table method.
- **S9.** The crosswalk.
- **S10.** Theorem 10.5 margin, both hosts (Math-O `s8`). Optional `metaloop`: the loop on the loop gain (Sys m3), $\Gamma_\delta\to\theta_\Gamma\to$ rule-making $\to\Gamma$. Build it only from the paper's own pieces: (9) for the objective, and Prop 9.2's rule-maker contest or the field model for the response. If it needs an ad hoc response function, drop it. If it can be built, it shows two basins and a separatrix in a specified model, which is Def 2.4(2) for both orders and the literal content of "change the basin, then add speed". Label it [num, toy; family's preferred unification, outside review required].
- **S11.** Dwell depth; frozen-share pause length.
- **S13.** New interface "Human capacity and correction". The "Capacity and the field" row is updated to "partly run".
- **S14.** New rows: Codex's eight boundary cases, Fable-adv's growing prize, the Opus MPE laggard, unequal incidence, the role-differentiated strict variant.
- **S15.** Block map with labels corrected (EC "valuation", LG(C) and RH "identity").

**DISCUSSION.**
- **X1.** Corpus keys fixed (讲理/讲赢 → `alignment-selection`, with `jian-and-wenyan`; five endgames → `selfishness-spiral`), a dates column, a `jian-and-wenyan` row, 力之所及 → `shengsheng` (book, 2026-07-14), and the reform dilemma marked "not verified against an original". Literature gaps, each with "absorbed / added": Grieco, Snidal, Powell 1999, Gilbert–Newbery, Budd–Harris–Vickers, Athey–Schmutzler, Aghion et al. 2001, Avenhaus–von Stengel–Zamir, Schelling–Halperin, Kydd 2000, Shavell, Grossman–Helpman, Askell–Brundage–Hadfield 2019. Also Meadows; Kuran; MacKenzie. 
- **X2.** Caulin & Maley qualified, with Butler 2025.
- **X8.** Fudenberg–Koh paragraph; Abecassis moved to "what remains"; benign winner $\kappa_W$ and C13; sprint by mechanism; the failure-mode table for every path, with an analogue base rate for its own design (Adv-O m6); the coercive-restriction hard case with tier 3's conditions.
- **X10.** The gameable clauses fixed (Sys I6 list in full). DP3. Nesting as an option. Disclosure function. Financing and appointment for execution and fallback. End conditions for chamber and appeal. Levy base broader than the constrained activity. $d^\ast$ estimated by a non-recipient on a conservative bound. Stop the clock under stalling. Frontier contributions by formula. The global minimum tax, corrected: the largest participant obtained an exemption.
- **X11.** Parallel tracks; precedents corrected (ABM, Outer Space/Seabed, the first monopoly and the period of superiority); a source for 1983.

**Registers.**
- **CLAIMS.** Thesis matched to the abstract. Inventory with the new keys. Dependency chain by threshold. Disposition table: every V6.1 review item with status fixed / narrowed / declined / open (the alignment review noted that B3, B4 and minors 3, 4, 6 of v6.0 were never recorded).
- **EVIDENCE.**
  - EV1: like for like completed.
  - EV2: RSP 3.1 reserved discretion; current 3.4; "support at the level of written commitments, not of conduct".
  - EV3: the first litigation outcome.
  - EV4: political spending in both directions classified by $\chi$, including the drafting developer's spending, per the register's own disclosure rule.
  - EV5: three sources; leads short in every measure.
  - EV6: verified items.
  - EV8: both leading states, document by document.
  - EV9: the 2–22-month interval.
  - EV11: Jones.
  - Gaps: T5 added.
- **TESTS.**
  - Cruxes C3a/b, C9a–d, C12, C13, N4.
  - Robustness matrix (tier-1 items × cruxes).
  - Test Γ re-signed. Test G at intermediate $p_d$.
  - Test L redesigned (Ali I7 table). Test M relabelled as a remedy test (Codex).
  - Study 2's expected signature corrected.
  - "Rates of human overrule" becomes catch rates of planted errors.
- **LEDGER.**
  - Sentence-level v6.1→v6.2, using the fidelity reviewer's `units.py` method: every sentence with containment below 0.3 is adjudicated as restated (where), moved (where), corrected (why) or withdrawn (why).
  - The v6.0 fidelity table's 14 items, each with its V6.2 home.
  - The nine withdrawals of V6.1, one line each; two are reclassified as restated.
  - Unledgered V6.1 changes recorded: entry barriers, the hysteresis prediction, Meadows.
  - The LEDGER §7 "S5" misrecord fixed.
  - The §5 blanket sentence deleted.
- **CHANGELOG.** The decisions (Def 2.1 three plus closure, departing from the plan's four; coercion moved to tier 3; no word cap). Deviations from the synthesis (the name sentence in §1.4, not §0). ASTRA: its substance, the four levels of epistemic closure, is in §4.1, X1 and Study 4; the seven-layer label is not adopted, with the reason.
- **README.** Reading paths regenerated; the alignment path completed (Ali minor 15).

**Tools.**
- **xref.**
  - "Kind Kind" duplicates.
  - Bidirectional citations keyed (first author, second author or et al., year).
  - The guide checked against §1.2 by keyword lists per item (pairs such as 母体/host, 一体/"we are one", 狭隘自我/"narrow self", 广义 E1/"broad E1").
  - A hedge counter on claim boxes (§7.2 below).
  - Banned phrases added: "every forward-looking actor", "on any reading of the cruxes", "win this race", "shared flourishing", "systemically false", "decides whether leads compound", "宿主".
- **checks.** New blocks:
  - MPE (Math-O `s2_mpe`);
  - growing prize, two-period (Fable-adv) and infinite-horizon (§2.1);
  - non-quasi-static capacity (Math-F `m5`; Math-O `s4`; Sys `s4`/`s5`);
  - joint scissors;
  - the detect link;
  - Codex's boundary cases ($\Gamma_\delta\ge1$, cap equality, positive diffusion, falling $f$, unequal incidence, stochastic punishment asymmetry, $p<1$, nonlinear fitness);
  - CS at $\eta\ne1$; LG with three stocks; CR reporting strictness;
  - EC relabelled "valuation", plus an explicit-action stochastic-game EC (Math-O M6.4).

The reviewers' scripts are in `v6.1/reviews/scripts-v6.1-*/`; port them, do not rewrite them.

---

## 4. The integration map

**Format.** Each item gives its landing and its form. **Fold** means the item becomes part of the argument; **cond** means a condition written into a statement; **comp** means it goes to a companion or register only.

### 4.1 Synthesis A: mathematics, by key

| Item | Landing | Form |
|---|---|---|
| A1 `loopgain` | Prop 2.2(3) gets $0\le\Gamma_\delta<1$, net reinvestment, and others and prize fixed. "Structural" in the name. Equilibrium elasticity [num] in Scope and S2. Rank-one for "channels add" | Fold (the vocabulary "structural gain") + cond |
| A2 `standprice` | New general statement (§2.1); title "Compounding prices standing"; [thm∣prem]; "every forward-looking actor" deleted everywhere; S3 proof; blocks MPE and GP | Fold: one inequality for two jobs |
| A3 `compound` | Strictly below $K^\ast$; diffusion in $\phi$; "sharing, provision or diffusion" | Fold (diffusion as third source) + cond |
| A4 `blind` | $s(0)>c>s(1)$ in (3) | Cond |
| A5 `onegroup` | Total term under every rule; components under affine fitness | Cond |
| A6 boundary / Ψ | `twoerrors` Remark; $\kappa_s\le0$; the Ψ sentence | Fold (the two errors) |
| A7 `corrrate` | (2) for $f=0$; halves; (3) conditions and "rises"; $f$ renamed; $\hat Y$ | Fold (halves) + cond |
| A8 `slowroute` | Proposition; renamed; (b)(c) as mechanism | Cond (honest premises) |
| A9 `enforce` | $p_d$ per deviation; (5) one breakout per period, $q\le\tfrac12$, new example | Cond |
| A10 `relpunish` | Weak/strict; continuation symmetry | Cond |
| A11 `restraint` | "changing the premise" | Wording |
| A12 `coverage` | (variety grows) as motivation | Cond |
| A13 `talk` | $n/(n-2)$ fades; blocs [conj]; §1.2(4) and the guide drop "blocs" | Fold (Snidal) |
| A14 `delegatelock` | $p=1$; $q_L\approx1$ premise in §11.3 and tier 1 | Cond |
| A15 `nested`, R8 | Matched unsafe variant; compliance vs neutrality; tax from lead; R8 split | Fold (incidence as a capture channel) |
| A16 `topology` | "Sufficient" throughout | Cond |
| A17 `safeguards` | Margin on both hosts; not the kernel | Cond |
| A18 `share` | $n$ and $n-1$ | Cond |
| A19 `require` | Table; R4, R1, R3a fixes | Cond |
| A20 scissors | `scissors` Prop by arms; pivot; 0.95; premise on $D$ and $g$; [num] labels; Test G hump; joint block | Fold (the pivot) |
| A21 labels, notation | §3.1 kinds; symbol renames (§7.4); [obs]/[val]/[conj] relabels; "one meaning" claim restricted | Comp + wording |
| A22 line 363 | §4.6 last paragraph rewritten (§3.3) | Fold (generative not selected among carriers) |

### 4.2 Synthesis B–H

| Item | Landing | Form |
|---|---|---|
| B cross-model arrows | Table 7.1 with "shown in"; the S7 matrix with four entries per cell; $d$ split; DC gain only; $T_{\rm dec}$ from $\Lambda^\ast$; gain higher at present inequality; four loops' formal correspondence; delayed-loop oscillation [num]; "gain" renamed to "drive" | Fold (the thresholds table is the arrow audit) |
| C1 thesis sentences, boxes | Abstract, guide, §1.2, every box (drafts above), §12.4, CLAIMS §1; thirty-minute path includes §1.4 and §12 | Fold |
| C2 tier 1 | §6 of this memo | Fold (a principle) |
| C3 tier 2 | §6 | Fold |
| C4 tier 3 | §6 | Fold (reversibility) |
| C5 name | §1.4 not-claimed list (deviation from §0, recorded) | Cond |
| D1 Ren's sentences | §5.1 table | Fold |
| D2 ledger method | LEDGER, sentence level | Comp |
| D3 X1 keys | X1 | Comp |
| D4 guide | §5.3 draft | Fold |
| D5 xref keyword check | Tools | Comp |
| D6 CHANGELOG deviations | CHANGELOG | Comp |
| D7 tone | Stick and carrot → "persuades by promising…"; "the cost can be large (C10)"; defensive-realism sentence rewritten; "keep pace"; "shared flourishing" removed; §10.1 mechanism first; "carriers" glossed; "and trade everything for winning" restored | Wording |
| E1 masked | `masked` Remark §6.4; Remark 4.8 sentence; R8 limit; tier 2; C12; guide item 5 | Fold (strengthens E2/E3) |
| E2 internal deployment | §6.4, §6.6, R8, tier 2, §1.2(5) "first inside the developers" | Fold |
| E3 tax scope | §6.4 paragraph; C9a–d; §8.3(a); §10.5 row; X1 Askell et al. | Fold (two kinds of progress) |
| E4 two joints | §6.3 end; §6.6 floor; C13 | Fold |
| E5 AI mind | §6.4 end; pointer from §5.3 | Fold (Ren's rule made exact for AI) |
| E6 oversight independence | §6.5; §4.4 $x_{\rm ev}$ | Fold |
| E7 Test L | TESTS; §7.3 row split | Comp + wording |
| E8 inner level | §6.6 text; CLAIMS disposition | Fold |
| E9 cruxes | §12.3; TESTS | Fold |
| E10 minors | §6 edits as listed in §3.3; $U$ defined as the number of predefined hazard modes in a class with correction meeting the four conditions and a stated catch rate (third time raised; C1 depends on it); EV6 updates; Kulveit verified; prover–estimator debate cited | Cond + comp |
| F1 Study 2 | §4.3 sentence; S4; S13; TESTS | Fold (delegation erodes the corrector) |
| F2 dwell | §11.4; S11; Prop 4.11 Scope; CHANGELOG item closed | Fold (decay and renewal) |
| F3 strands, rows | §10.4 fifth strand; §10.5 six rows | Fold |
| F4 gameable clauses | X10 | Comp |
| F5 Ostrom | §10.5 one sentence; X10 | Comp + wording |
| F6 transition control | §11.3 readiness; §11.4 tracks; Def 11.5; ratchet; tier 2 activation | Fold |
| F7 leverage | §12.2 | Fold |
| G1 Jones | §8.1, §8.4, X8, S8, EV11, LEDGER | Cond (corrects a misquotation) |
| G2 EV5 | §7.2, §7.3, EV5 | Fold (near parity) |
| G3 EV8 | §11.4, T6, EV8 | Wording |
| G4 EV4 / T4 | EV4 (named, per register rule); T4 in roles | Comp + wording |
| G5 T5 / T2 / EV2 | §7.3; EV2 | Wording |
| G6 citation mechanics | refs script; THEORY reference list (Maynard Smith & Szathmáry in; H. Smith, Acemoglu–Egorov–Sonin and Schelling 1966 out unless cited) | Comp |
| G7 minors | X2, X8, X10, X11, EV1/3/9, bibliography | Comp |
| G8 literature gaps | X1, per item "absorbed / added" | Comp |
| H tools | §3.4 Tools | Comp |

### 4.3 Items in individual reviews that the synthesis does not list

| Source | Item | Landing |
|---|---|---|
| Fable-adv F4 | Benign winner at its strongest: $\kappa_W/(1+\kappa_W)$; the crux is whether AI lowers the winner's dependence on the governed | §8.3(d), §5.2 sentence, C13. Fold |
| Fable-adv F7 | $p_d$ not tied to $\upsilon$; trigger estimator | `detectlink`; tier 2 estimator clause. Fold |
| Fable-adv F11 | Fudenberg–Koh deserves a paragraph | X8 |
| Fable-adv F12 | 5.15(2) needs third parties linear | `talk` statement. Cond |
| Fable-adv F9/F10 | Theorem 7.1 and Prop 9.1 are tables; least-value punishment flagged in the core | Kinds; 5.4 Scope |
| Adv-O I6 | Sprint and freeze answered by mechanism | §8.3(e), X8. Fold |
| Adv-O I7 | Snidal; arms-control textbook condition; IO literature | §1.4 positioning; `talk`; X1 |
| Adv-O I8 | One generative list; crosswalk; chain restated six times | §8.2 G1–G7; S9 crosswalk; §7.2 below |
| Adv-O m2 | §11.5 "AI lacks saturation" contradicts §7.3 | §11.5 conditional |
| Adv-O m5 | 5.14 and "the mind": a linear absolute objective also has no point of enough | §5.3 sharpened rule (§5.1 below). Fold |
| Adv-O m6 | Own design's D2 "Unknown" | X8 analogue base rate; EVIDENCE gap |
| Adv-O m7 | Corpus cited for empirical-sounding claims | Mark [conj] or analytic |
| Adv-O m8 | Trigger estimator must hold row-sum certificates | Tier 2. Fold |
| Adv-O m9 | Henrich is about persons | §3.8 |
| Adv-O I1(v) | Calibration: $\Gamma>1$ needs $r\ge3$–6 at present diffusion | S2 illustrative ranges; §2.2 above ("blocking diffusion raises the gain"). Fold |
| Math-F minor 2 | $p_d$ per deviation | A9 |
| Math-F minor 7 | "Channels add" rests on the rank-one structure | A1 |
| Math-O M3 | $f$ is a marginal floor | A7 |
| Math-O M5 | Theorem 10.5 viability clause circular | A17 |
| Sys I2 | Four loops, formal; oscillation | §7.1. Fold |
| Sys m1 | Remark 2.5 "of the same form" | `bench` |
| Sys m3 | Loop on the loop gain | Optional `metaloop` (§3.4) |
| Codex | Test M is a remedy test | TESTS |
| Codex | Test Γ points the wrong way; observable $1+\theta$ | §7.4, TESTS. Fold |
| Fidelity minor 1 | Withdrawals without reasons | LEDGER |
| Fidelity minor 3 | Entry barriers; hysteresis prediction; Meadows | §4.1 (barriers, folded via incidence); TESTS (hysteresis restored as a registered prediction beside Test D); §12.2 (Meadows); LEDGER |
| Ali minors 5, 6, 12 | 6.8, 6.11, 6.9 budgets | §6.5; S6 |
| Evi minor 12 | "compare" for Crawford–Sobel, Gabriel; Hehenkamp et al. for full dissipation | Wording; references |

### 4.4 Declined or deferred, with reasons

1. **Compressing the core to 12–15k words now (Fable-adv F6).** Declined for V6.2. It would move conditions and the judgment's support out of the main read. Codex: "its assumptions are part of its argument." Deferred to a derived venue paper (open question 1).
2. **Moving §3.7 (relational self, 大同) and the doctrine part of §3.8 to X1 (Adv-O I8).** Declined. The fidelity review names both as what must not change; they carry the meaning. They are tightened instead.
3. **A calibrated $\Gamma$ by channel in the core (Adv-O I1).** Declined as calibration, because it would be false precision. Accepted as illustrative ranges in S2, with "$\Gamma$ is not estimated" kept in the core.
4. **A full integrated model as a theorem (Adv-O F1(a)).** Declined as a theorem; accepted as a reduced joint [num] (§2.3). It is the family's preferred unification, so its label must say so.
5. **Replacing the threshold account of leverage with Meadows' hierarchy (fidelity minor 3c).** Declined as a replacement; both stand (§12.2). Ren is asked to confirm (open question 4).
6. **Three-level nesting (national, regional, global) as a requirement (Sys I7).** Declined as a requirement, because nested governance of a planetary commons is itself an open problem (Stern 2011). Accepted as a design option in X10.
7. **ASTRA's seven-layer list in the core.** Declined. Its substance, the four levels of epistemic closure, is in §4.1, X1 and Study 4. LEDGER records this.
8. **Changing the English term "host".** Deferred to Ren (open question 3). The Chinese uses 母体 now.

---

## 5. Fidelity

### 5.1 Ren's rulings, restored where they belong

| Ruling (source) | Home in V6.2 | Wording (Ren's, or as close as the English allows) |
|---|---|---|
| Broad E1: any competitive game that concentrates is accelerated by AI; the narrow list is an order, not the scope (2026-09-26) | §0; §6.6 criterion; §11.3 E1; §12.1 closing line; guide item 9 and the judgment | §0: "…an instrument in a game whose aggregate concentrates control and makes those without it fall behind, in labour, finance and persuasion as much as in force." §6.6: "A use falls under broad E1 when, aggregated over its users, it raises convertibility, decisiveness or the conversion of success into control in a competitive game that concentrates: over shared conditions, and equally in labour, finance and persuasion, where those without it fall behind." §12.1: "The broad form … is the scope; the narrow form is the first step." |
| "Decay and renewal belong to growth"; "dying is not a bug but a feature" (transcript 00:57) | §0; §12.4; guide; **mechanism in §11.4**: a lineage of the alternative that can recruit bounds dwell time; §10.1 "replaceable"; §10.4 plurality | "Decay and renewal belong to its growth." The fold, in §11.4: "An order in which forms can fail and be replaced can be reformed in bounded time; one that has frozen cannot (10.45 → 3.81)." |
| Identity, not membership: "we are not just our life. We are the whole process of the universe doing this and itself and this is great" (transcript 01:06) | §0; §12.4; guide 意义 | "We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good." |
| "We are one" in both one-page summaries; the narrow self as the target (molochlization) | §1.2(2); guide 2 | Drafts above |
| No better guardian: philosopher-kings, priestly classes, enlightened stewards, new universities refused; "the corruption of the constraining mechanism itself" | Remark 10.8 | Restore: "Philosopher-kings, priestly classes, enlightened stewards and new universities have each been proposed as the guardians who would hold the line, and each is a corrector to which Section 4 applies." Add from the corpus (provenance to be checked): "Real order is not finding people who are always right; it is building a structure in which error cannot grow without limit" (真正之秩序，非得永远正确之人，乃立错误不能无限扩大之构), and "the regulators must themselves be regulated" (调节者亦须被调节) [corpus: shengsheng]. |
| "If the winner's logic is cancer-like, falling behind is not survivable, so everyone should first oppose this logic" (2026-10-03) | §3.8, first sentence of "The logic to oppose" | "If a winner's logic is of this kind, falling behind cannot be survived, and every actor has reason first to oppose the logic itself." |
| Insurance accepts the struggle frame (2026-10-03) | §8.3(f); Remark 8.9 | "Insuring against falling behind is not an exit: the penalty is set by the winner, and insurance accepts the frame of the contest, hedging against losing instead of declining the game." |
| Growth is not the danger; the mind is (2026-09-25) | §5.3 after Prop 5.14 (sharpened); §6.4 (AI minds); §1.2(4); guide 4 | "Growth is not the danger; the mind is. The mind decides whether growth stops where need is met: an objective not satiated in the stakes, relative standing above all, has no point of enough. Hazardous variety that outgrows contestable coverage is dangerous under any mind, which is why pace binds even a generative order." Add Ren's book line: "Cancer grows too, but its growth exhausts the body that bears it" (癌亦增长，而其长竭母体之生) [corpus: shengsheng, 2026-07-14 l.113]. |
| The generative loop's institutional forms; the degenerative loop's closure | §10.4 | Restore: "shared capability, distributed agency, plural observation and criticism, maintenance and repair, renewal of the commons"; the degenerative loop closes: "…trust collapses, and fear deepens." |
| "A self-replicating economy carries the switch with it" | §5.1 after Remark 5.3 | "Expansion is an anaesthetic for the winning model. Winning does not end the game: the logic itself is the replicator, and a self-replicating economy carries the same switch with it." (LEDGER §7 misrecord fixed.) |
| "Growing understanding without executive authority may change nothing" | §12.2 | Restored verbatim |
| Meadows; "the paradigm can change only if the system is understood" | §12.2, beside thresholds | Both: parameter interventions below threshold are re-absorbed (Prop 4.10); the paradigm decides which parameters are moved and whether they are held |
| Preference falsification; counter-performativity | §5.4 (Kuran); §11.2 and §0's last clause (MacKenzie) | "A shared model can prevent its own fulfilment." |
| ASTRA | LEDGER note | — |
| "Understanding goes to everyone, not to a class"; "the open part is who builds and funds it, not who holds it" (10-02) | Remark 10.8 (distribution of understanding, kept); §10.1 (restore the open question) | "What is open is who builds and funds such provision, not who holds it." |
| Don't read race narratives as a believer; famous is not strong (10-03) | §8.3(d) tone; X8 | "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact." |
| Dynamics, not dyads; answer positions, not documents | All body text in roles; §8.3(g) the plan as one instance | Kept |
| Do not escalate humanity's unresolved struggles into a struggle of intelligences (corpus) | §6 claim box "Why", or §6.6 opening; guide item 5 | "Do not hand the struggles humanity has not resolved to a stronger intelligence" (不要把人类尚未解决的斗争，升级为智能的斗争) [corpus: shengsheng]. Provenance check: is it Ren's sentence or drafted from his ideas? |

### 5.2 How the large themes appear

- **"We are one."**
  - Formal content: §3.6 (Lemma 3.10: anticipation).
  - Meaning: §3.7, kept as the fidelity review asked (three jobs through understanding; the relational self in Ren's words; 大同 as direction; 和实生物，同则不继).
  - Summary: §1.2(2) and the guide.
  - Requirement: §7.2 ("Oneness is what these requirements are requirements of").
  - Conclusion: §12.4.
  - The two errors (§2.5) give it a new precision. Accuracy about the coupling is "we are one" seen correctly. Changing the game is "we are one" built into selection: the third job of §3.7.
- **The affirmative meaning.** §0 and §12.4 use Ren's identity wording. The meaning comes before the commitment. "Do not close the world" stays secondary. Decay and renewal are folded into mechanism (§11.4), so the affirmation is also a design principle: plurality and replaceability make reform possible in bounded time.
- **No better guardian.** Remark 10.8 carries the list, the corpus line, and the four questions. The reform dilemma's two answers, neither a better guardian, are kept. Tier 3's reason (ii) applies the test to custody itself.
- **Broad E1.** It is the scope everywhere it is mentioned. Narrow E1 is the first step, with its premise ($q_L\approx1$) stated. The criterion is game-level ("aggregated over users"), which is "judge the game, not the act" applied to AI use.
- **Decay and renewal.** §0 states it; §11.4 makes it mechanism; §10.5 keeps "replaceable" and plural lineages.

### 5.3 The Chinese guide, full draft

Below is a draft for Ren to correct. It mirrors §1.2 item by item; the 一段话 mirrors the abstract; the judgment mirrors §12.1. It uses 母体 throughout. Avoid: 签名, 闭合于自身, 宿主, 翻译腔 such as "这个过程是好的".

> **中文导读**
>
> **一段话。** 凡是能增减份额的单位（企业、国家、研究路线、做法、训练出来的 AI 系统，本文统称"载体"），只要按相对成功被选择，赢得的东西能再投入同一场竞争，能力又能决定胜负，成功就会抬高赌注，同时削弱本可以约束它的东西。本文称之为"赢的选择压力"。成功若还能买到对下一轮选择的控制，即规则、纠错者、心智的养成和语言，这股压力就转回来作用于选择本身，这就是"赢的元吸引子"。在指定的模型中，本文证明了下面几件事。在地位相近时，这些条件合成一个结构环路增益，大于一时，领先越滚越大。只要再投入的相对回报高于共同回报，向前看的行动者就会把地位看得比共有之物更重；奖金随总能力增长时，这恰好发生在领先越滚越大之处。每一方都算得没错，错的是博弈。对纠错者的影响，在最大的参与者中被选择。只有当偏离变成决定性优势的概率低于某个门槛时，克制才可执行；环路增益抬高这个概率，又收窄决定门槛的那些目标。每个 AI 系统各自对齐于自己的委托人，并不能让委托人之间的博弈对齐。出路不是取消竞争、增长或选择，而是改变赢了之后能得到什么，让同一个反身结构转而选择贡献。
>
> **为什么写。** 好的理论能预测。本文预测：沿着当下的轨迹，"讲赢"的逻辑会把所有参与者带到谁也不会选择的结局。在第 2 节的条件下，每一方都比共同克制时更差，所争之物大半耗在争夺之中。能力带来的危险若增长得比能纠正它的力量更快（第 5.3 节，也是第 12 节的核心分歧），连赢家也一并危及，赢家只有停止复利才能脱身。参与者看得见结局临近，却仍无法协调避开，障碍首先在理解：预测要先成为共识，协调才有可能。本文就是为此而写的，它把这一动态写得足够精确，每一方都可以自己核对。它希望的，是一个一旦成为共识、便有助于让自己落空的预测。
>
> 生存是最低要求。两样损失要首先防止：大规模的生命损失，以及人类在关键事务上不可逆地失去决定权。它们不是全部要紧之事，却是其余一切的前提，因为一旦发生便无法挽回。
>
> 本文判断的是博弈，不是行为；是结构，不是任何人。一次 AI 的使用可以帮到一个人，却仍是一场博弈的工具：人人都用，不用者便落后，控制随之集中，劳动、金融、说服都是如此，不只是武力。在领先越滚越大之处，一个正确计算自身利益的行动者，也会把地位看得比共有之物更重。错在博弈，出路也在博弈。
>
> **意义。** 本文的意义是肯定的。我们不只是各自的一生；我们就是这场更大的生生过程本身，它正经由我们继续展开。这很好。衰败与更新，也是生长的一部分。人类在其中有很好的未来，我们正在造出的心智也可以有。本文反对的不是增长、竞争、技术或任何人群，而是一种逻辑：一个部分忘了自己属于整体。癌也增长，但它的增长耗竭母体。
>
> **论证链（与第 1.2 节同序，逐条对应）。**
> 1. **赢的条件。** 能增减份额的载体若按相对成功被选择，赢得的可以再投入，能力又决定胜负，那么结构环路增益一旦大于一，领先就会越滚越大；在领先会让落后者泄气的竞争里，不到一就已如此。分享、不必靠赢得的供给、扩散，都压低这个增益；成功能转化成什么，就抬高它。成功若还能买到对选择本身的控制，即规则、纠错者、心智的养成和语言，这股压力就转回来作用于选择本身，这就是赢的元吸引子。它不依赖任何特定的载体。
> 2. **同一个系统。** 所有载体共处同一个母体，彼此耦合，没有外部。相对选择看不见共有之物：既看不见母体的衰退，也看不见对所有人一律适用的约束。选择偏爱狭隘的自我，也就是把边界画在系统之内的自我，而系统真实的耦合恰恰惩罚它。向前看也治不了这一点：在地位相近时，只要再投入的相对回报高于共同回报，向前看的行动者就会把地位看得比共有之物更重。奖金固定时总是如此；奖金随总能力增长时，恰在领先越滚越大之处如此。每一方都算得没错，错的是博弈。对全局而不可逆的失败，整合只能事先依据对系统的准确理解来完成。所以，理解"我们是一体"，是增长与变化得以延续的长期条件。
> 3. **选择选择者。** 对纠错者的影响若能归买者所有，其回报随份额的平方增长，因而在最大的参与者中被选择。若 AI 压低控制的成本，独立纠错只要按其一定比例同步增长，评估就不会被俘获；增长得更慢，在影响力调整得快的地方，评估终将失守。改革若不把流入纠错者的转化压到一以下，会被重新吸收。俘获若先于证据，母体会在任何警报响起之前越过底线。
> 4. **加速与三重侵蚀。** 这股压力使竞争加速，并侵蚀约束它的三样东西。一是执行：只有当偏离变成决定性优势的概率低于某个门槛时，克制才可执行；环路增益抬高这个概率，又收窄决定门槛的那些目标，两片刀刃转在同一个轴上，就是能力中必须靠赢得的那一份。二是纠错：它必须跟上变化的节奏，对证据来得迟的危险，只有放慢才有用。危险不在增长，而在心：在没有"够了"的目标。三是共同的理解：对手之间，相对的算计让话语失去信息。三者各在自己的模型中得到证明；增长会不会让它们同时收紧，是诊断要检验的猜想。
> 5. **工具与化身。** 忠实的 AI 让委托人的博弈更有效；委托用纠错换速度，直到人推翻它的能力不复存在。化身的弱形式：针对不完美的代理目标去优化，无论谁来开发，都可能产生偏差；去除偏差若要付出相对地位，只有强制执行的共同约束才能让它保持去除；对在评估中会隐藏自己的偏差，连这也不够，能力必须限制在控制手段能确保安全的范围之内。化身的强形式是有条件的：AI 的谱系本身成为载体，最先发生在用 AI 研发 AI 的开发者内部。委托人不等于它所服务的人，每个系统各自对齐，并不能让博弈对齐。不要把人类尚未解决的斗争，升级为智能的斗争。
> 6. **当下的轨迹。** 当下的种种动态，是这些条件的征候，证据有明确的缺口。驱动竞赛的那个前提，恰好描述了重复博弈不再能维持克制的情形：它是现在就准备共同保管的理由，不是竞赛的理由。
> 7. **替代路径与要求。** 各条路径按同一个标准比较：先保护不可逆的损失，对每条路径用同一个不确定范围，连同它们各自的失效方式。决定成败的不是名称，而是能否在所有有能力的行动者那里，把第 7.1 节的门槛推到安全的一侧；有几项要求，任何一方都无法单独做到。
> 8. **生生的选择。** 同一个反身结构，若选择的是贡献，就成了生生的结构：成功可以得到回报，却得不到同一场博弈中更多的优势，也得不到对自己评判的控制；供给在博弈之下，像树一样；这一秩序经由共有之物延续，而不经由赢家。它的形态按功能逐项推导，不沿"集中或分散""个人或集体"的轴。没有更好的守护者；真正的秩序，不是找到永远正确的人，而是建立错误不能无限扩大的结构。
> 9. **过渡与判断。** 信任是分阶段过渡的结果，不是前提。改变"选择什么"现在就有理由，分三层：测量与准备，现在就做，无论分歧如何解决都成立；停止建造决定性一类的能力、共同保管、按理解的速度发展，现在准备好，到事先登记的指标时由机制启动；各种整体设计，比较而不定论。
>
> **判断（分三层，见第 12.1 节）。**
> - **第一层，现在就做。** 这一层的理由不取决于任何分歧怎样解决。共同测量危险、覆盖与残余风险，与"谁领先"的测量分开；公开并审计转化数据，测量纠错者的独立性与误差的相关；算力、训练与保管核查的研究与试点；共同出资、公开发表、降低对齐代价的对齐与控制研究；共同保管的设计、机构与触发条件现在登记，启动的承诺现在作出；狭义 E1：AI 退出战略与升级决策的回路，这类委托几乎必然造成锁定，先从可检查演习的声明性原则做起。共享有用的服务、分享可分的收益，在任何读法下都实现共同价值；它们能否降低对"赢"的看重，是分歧 C6/C8。
> - **第二层，现在准备，由机制按指标启动。** 停止建造决定性一类的能力（E2），覆盖已落后之处回退；共同保管生效；对覆盖落后的危险类别，按理解的速度发展（E3）；纠错者行和超过一时启动公式拨款与强制访问；对齐代价为正的类别，在后果性部署之前（包括内部部署）施行共同准入；会隐藏自己的偏差，按能力门槛准入，配以不假设系统配合的控制手段。到达决定性位置的估计时间，减去保管安装与核查所需的时间，低于事先登记的余量时，触发启动。启动现在就承诺，由机制执行，不在触发时重新决定，因为触发之时正是克制最难执行之时。
> - **第三层，比较、不定论。** 各种整体设计，以及对前沿投入的强制限制。后者只有满足三个条件才进入比较：负担等额，包括限制者自身；由独立于所有被限制方（包括限制者）的纠错者执行；受影响者的议院同意。即便如此，本文也不推导它的净效应为正。排序是明说的判断，依据是可逆性的不对称：按第 10 节建成的设计，其各种失效都可以退回到分持的职能；越过底线，则无法挽回。
> - 广义 E1 是范围：AI 不作为任何趋向集中的竞争博弈的工具，劳动、金融、说服都在其中。狭义 E1 是第一步。
>
> **本文不主张什么。** 不主张一切竞争都会失败，也不主张一切竞赛的结局都是零存活；不主张决定性优势现在已经可以取得；不主张这些门槛在现实中一定同时收紧，这是要检验的猜想；不主张环路增益已被估计出来；不主张某一种制度方案唯一可行或最好；不评判任何人的动机。"元吸引子"这个名字指的是机制，它是否真是吸引子，只在指定的模型中得到证明。
>
> **怎样读。** 三十分钟：本导读或英文摘要，第 0 节，第 1.2 与 1.4 节，各节开头的主张框，第 7.1 节的门槛表，第 12 节。证明在形式伴篇（SUPPLEMENT），替代方案与设计的全文在讨论伴篇（DISCUSSION）。

Notes for the implementer of the guide:
- Terms: 结构环路增益 (structural loop gain), 母体 (host), 载体 (carrier), 门槛 (threshold), 征候 (signatures), 化身的弱形式/强形式, 共同保管 (custody), 决定性一类的能力 (decisive class).
- Check item by item against the final §1.2 with the keyword lists in xref.
- Ren may prefer a more classical register for 意义. Keep the content; do not add aphorisms. Per his rule, maxims compress thought that is already finished.

---

## 6. The judgment rebuilt

### 6.1 Draft §12.1

> **12.1 The judgment, in tiers**
>
> **Tier 1. Warranted now, on every reading of the cruxes [rec].** A step belongs here only if its justification does not depend on how any crux comes out. It is either measurement that decides the cruxes, preparation whose lead time exceeds any warning, or a step that is an equilibrium without trust.
> 1. Shared measurement of hazards, coverage and residual risk per class, kept apart from measurement of who leads. Audited disclosure of data on conversion into correctors, with a sanction above the gain from omission. Certified row sums. The correlation of evaluators' misses on common test sets, and control evaluations in which the red team knows the protocol.
> 2. Research on, and pilots of, verification of compute, training and custody.
> 3. Commonly funded, openly published research on alignment and control that lowers the alignment tax. It is a public good that competitors undersupply, and once published it spreads without coordination.
> 4. Preparation of common custody: its design, institutions, triggers and activation rule registered now, and the commitment to activate taken now.
> 5. Narrow E1, for the decisions whose delegation would lock with near certainty: strategic and escalatory decisions irreversible within the time available for deliberation [prem: $q_L\approx1$ for that class]. AI is kept out of those loops, beginning with declared doctrine and inspected exercises, with drilled human fallback and an evidence channel independent of AI, and is verified wherever verification is possible. Among actors who price in the lock this is a strict equilibrium that needs no trust (Proposition 6.4).
>
> Shared provision of useful services, and the divisible gains of capability shared as they arise, realize joint value on every reading. They rest on values (V1, V5), not on the cruxes. Whether they also lower the weight on winning is crux C6/C8.
>
> **Tier 2. Prepared now; activated by mechanism on registered indicators [rec].**
> - E2, with rollback where hazardous variety already exceeds coverage.
> - Common custody in force.
> - E3 for each hazard class whose coverage falls behind.
> - Formula funding and mandated access for correctors, where row sums are measured at or above one or findings go unexecuted against leaders (C2).
> - Common admission constraints, before consequential deployment and internal deployment included, for each class whose alignment tax is measured positive (C9). For divergences that hide under evaluation, admission by capability threshold, with control protocols that do not assume the system's cooperation (C12).
>
> *Trigger.* Custody activates when the estimated time to a decisive position, less the time custody needs to be installed and verified, falls below a margin registered in advance. The estimate is made by correctors with certified row sums, from channels that observe actions directly (compute, deployments, the performance of contracts), under the conservative rule of Remark 4.8.
>
> *Commitment.* **Activation is committed in advance and executed by mechanism, not decided afresh when the trigger fires.** The trigger fires where restraint is least enforceable (Proposition 5.4(4)): a decision taken then would face the very condition it is meant to prevent.
>
> *Release.* Release uses different indicators from activation, and requires them to hold for the dwell time of the slow variable, since levels improve before safety does (Section 11.4). Waiting until decisiveness is shown would be too late.
>
> **Tier 3. Compared, not settled.** The candidates are:
> - the separately held configuration of Section 10.5;
> - a polycentric complex of mutually recognized institutions;
> - a verification agreement with shared provision;
> - regulated competition meeting Section 9;
> - an agreement of the type of Section 8.3(g);
> - the benign winner;
> - the coercive restriction of frontier inputs.
>
> The last is admissible for comparison only under three conditions of its own: its burden is equal, the restrictor's own included; it is executed by correctors independent of every party it restricts, the restrictor included; and the chamber of those affected consents. Even then the theory does not derive that its net effect is positive (Section 8.3(f)).
>
> Both worst cases exceed the tolerance, so the ranking falls to the standard's third step. The preference for changing selection is a judgment. It rests on the asymmetry of reversibility across every failure mode in $\Theta$ (DISCUSSION X8 lists them path by path):
> - **(i) Reversibility.** A design built to Section 10 has failure modes: dissolution, capture of one function, interruption of a service, collusion among checks, and overreach of a common constraint. In each, it dissolves into its separately held functions while protections against unilateral domination stay entrenched, so the functions can be re-formed. Whether its fallback is no worse than continuation (the safe-fallback condition of Lemma 8.2) can be read from its own documents (D1). Continuation's worst case crosses a floor that cannot be recrossed.
> - **(ii) The irreversible failure they share.** The design's own irreversible failure is capture of the custody of decisive capability. That is the outcome the race produces by construction, and selects for (Proposition 7.2). The design contests it by separation, plural lineages and the tests D4 and D5; the race does not.
>
> A reader who weighs these differently can reach another ranking; Section 12.3 says which measurements would move it.
>
> The broad form of E1, AI not an instrument in any game that concentrates (labour, finance and persuasion as much as force), is the scope; the narrow form is the first step.

### 6.2 What changed and why

- **Tier 1 by principle.** Membership is decided by the kind of justification: information, lead time, or equilibrium without trust. Agreement across camps is not the test. This removes the contradictions with the C2 and C9 rows (Codex; Adv-O I4; Adv-F F2) without weakening the judgment, because those items move to tier 2 with triggers.
- **Tier 2 carries the substance.** Its activation is pre-committed (Sys I8). That turns the race camp's own premise into the reason for acting now, which every reviewer singled out as the paper's best answer.
- **Tier 3 by reversibility.** This replaces measurability, which Adv-O I3 showed fails because row sums have never been measured. The step-2 argument is dropped (Adv-O I3(a)). Reason (ii) answers Codex's demand to cover every admitted failure mode, including the design's worst one.
- **Coercion.** Moved per Ren's decision, with the three conditions, and stated in the guide.
- **A robustness matrix in TESTS.** Five tier-1 items × C0–C13. Each cell says why the item holds on that reading, or "value of information" or "lead time".

### 6.3 Cruxes (§12.3)

| Crux | Change |
|---|---|
| C0 | Kept: interlock. |
| C1 | Masked classes measured adversarially. |
| C2 | Kept. Its activation consequence is now explicit in tier 2. |
| C3 | Split into C3a (scalable oversight: catch rates at fixed human hours) and C3b (independence of AI oversight: miss correlation and collusion, same versus different lineage). |
| C4, C5 | C5 notes that leads are measure-dependent. |
| C6/C8 | Kept. |
| C7 | Kept. |
| C9 | Split into C9a (capability gap at fixed compute), C9b (monitoring and control overhead), C9c (the speed tax, always positive), C9d (cost of tax-lowering research). |
| C10, C11 | Kept. |
| **C12 Verifiability** (new) | Can admission bound $m_{\rm model}$ at the admitted capability? |
| **C13 Dependence on the governed** (new) | Does AI lower an institution's or a winner's dependence on people? This unifies the benign winner and gradual disempowerment. |
| N1–N3 | Kept. |
| **N4** (new) | Standing of AI systems. |

---

## 7. Coherence rules for the implementers

These are principles for judgment, not procedure. The tools enforce only what is mechanical.

### 7.1 One home per point

| Point | Home | Elsewhere |
|---|---|---|
| The chain (Ren's) | Abstract, guide, §1.2, §12.4 | One-sentence hand-offs only |
| Four loops | §7.1 | — |
| Thresholds | Table 7.1 | Referred to by name |
| Generative marks G1–G7 | §8.2 | Same wording and order wherever listed (§12.4) |
| Price of standing; two errors | §3.5 | §0 one sentence (stance); §1.2; abstract |
| "We are one" | Formal: §3.6. Meaning: §3.7 | Summaries, §7.2, §12.4 |
| E1 narrow/broad | §11.3 | §6.6 (enforcement), §12.1 (line), §0 (stance) |
| E2 / E3 | §5.3 (definition), §11.3 (arrangements) | — |
| Trees, provision | Prop 2.3; §10.1; §10.4 strand | — |
| Growth is not the danger; the mind is | §5.3 | §6.4 (AI) |
| Cancer | §3.8 definition | §0 image; guide |
| Guardian | Remark 10.8 | Reform dilemma uses it |
| Meta-attractor name | §1.4 | — |

### 7.2 Claim boxes carry conditions without hedging

- Each box has **Claim** and **Why**, as in V6.1.
- **Conditions are antecedents, never adverbs.** Write "Where X, Y [tag]", not "Y may hold". The consequent is stated with full confidence; the tag says what kind of support it has.
- If a claim has a conjectured part, it ends with one sentence that names it as a conjecture.
- Avoid in boxes and headlines: "may", "plausibly", "can" used as a hedge (not as possibility), "in some sense", "arguably". xref counts these in boxes and flags more than one per box.

### 7.3 No restatement of the chain

Outside its four homes, a section refers to the chain by a hand-off sentence or by a threshold's name. A paragraph that recapitulates Part I in prose is a sign the section has lost its job.

### 7.4 Vocabulary to fix

- **Loop gain.** "Structural loop gain $\Gamma$" (never "the loop gain decides … for every actor"); "equilibrium gain" when rivals respond; "the drive" for §7.1's former "gain".
- **Objectives.** "Price of standing"; "working objective" versus "held self-model"; "relative return / common return (of reinvestment)".
- **Correction.** Versus "depreciation"; "conversion" (what success converts into).
- **Thresholds.** "Threshold", with the nine names of Table 7.1.
- **Host.** "Host" (English) and 母体 (Chinese); "carrier" glossed at first use in §1.2.
- **Arrangements.** "Decisive class"; E1 narrow/broad; E2 "stop"; E3 "pace" ("develop at the pace of understanding").
- **AI.** "Masked divergence"; "consequential deployment, internal deployment included"; "incarnation, weak and strong" (化身的弱形式/强形式).
- **Certificates.** "Certified" means full inbound row sums below one, a sufficient certificate.
- **Style.** "Keep pace", not "win the race". "Provision not won in the contest", with "provision beneath the game" as its name in prose; choose one per paragraph, and define the equivalence once in §2.2.

**Symbol renames** (Math-O 15, Math-F 8):
- Jacobian → $\mathcal J$.
- Remark 2.5's deviations → $u,w$.
- The cost function → $\mathrm{Cost}(q;p)$.
- (15)'s $d$ → $h_d$.
- The subordination value → $V^{\rm sub}_i$.
- 5.4(5)'s $q$ → $q_b$.
- Non-contestants → $m_o$.
- Checks per layer → $k_c$.
- Eigenvalues → $\Lambda$, with S5.1's local $\Lambda$ renamed.
- S3's $\kappa_k$ cost → $c_k$.
- The "one meaning" claim is restricted to the symbol table.

### 7.5 Hand-offs

Each section's last sentence names what the next section takes from it. Drafts are in §3.3. Part openings (I–IV) get a one-sentence lead naming the level of claim.

### 7.6 Ren's register

- Mechanism before conclusion.
- No aphorism-first sentences. A Ren line is quoted after the mechanism it compresses, with its corpus key.
- No race grammar in the theory's own voice: "leverage" only for Meadows; "win" only for the contest being analysed.
- Roles, never names of states or firms.
- Chinese in the guide in plain modern prose. Classical quotations only where Ren wrote them.

### 7.7 Source discipline

- Edit `src/` only, by key.
- Every new formula gets a check block before its sentence enters the core.
- Each section implementer runs `assemble`, `xref` and the relevant `checks` blocks before handing over.

---

## 8. Risks: how V6.2 could be worse than V6.1, and how to avoid it

1. **Hedge creep.**
   - *Risk.* Writing conditions back as adverbs makes the paper read as timid.
   - *Avoid.* Antecedent grammar (§7.2); the box hedge counter; one reader pass that asks of every headline "is this stated as strongly as the model allows?"
2. **Length creep.**
   - *Risk.* Each review item added as a paragraph pushes the core to 35k words.
   - *Avoid.* The integration map assigns most items to companions. Budgets per section (§3.3) print warnings. Any section 15% over budget must say which condition or ruling needs the words.
3. **Losing Ren's voice again.**
   - *Risk.* Precision rewrites delete normative sentences again, as happened between v6.0 and V6.1.
   - *Avoid.* The sentence-level ledger. The §5.1 table becomes a must-stay list in xref (keywords per ruling). Ren reads the guide, §0, §3.7–3.8, §10.4 and §12 before anything else.
4. **Over-unification (the family's bias).**
   - *Risk.* The thresholds table, the joint scissors and the meta-loop could make the theory look more unified than it is proved to be.
   - *Avoid.* Keep S2's "unifies / does not" table. The thresholds table has a "Shown in" column with each model. Joint results are labelled [num, one model]. The parameter matrix marks unproven interfaces. Codex is asked specifically to attack these three objects.
5. **New mathematical errors** in the general 3.9, the proportional-prize derivation, `detectlink` and the joint model.
   - *Avoid.* A check block for each before the core sentence is written. The proportional-prize derivation is written in full in S3 and checked against nonlinear simulation, including the diffusion case where the two thresholds separate. Outside review targets these first.
6. **A judgment that reads as weaker.**
   - *Risk.* Moving items out of tier 1 leaves only "measure" in it.
   - *Avoid.* Say plainly that tier 2 is where the substance is and why its activation must be committed now. The box of §12 leads with that.
7. **The thresholds table becoming another summary.**
   - *Avoid.* It collects inequalities and levers only. Prose does not restate rows. §1.2 refers to it, it does not reproduce it.
8. **The guide drifting from §1.2.**
   - *Avoid.* Write the guide last, from the final §1.2. Check it by keyword per item. Ren corrects the register.
9. **Churn errors** ("Proposition Proposition", stale numbers, broken reading paths).
   - *Avoid.* `{{>key}}` already prints the kind, so never write a kind before it. Regenerate reading paths from the keymap. xref checks for duplicated kinds.
10. **Tone drift in either direction**: deference to race narratives, or straw-manning them.
    - *Avoid.* §8.3 keeps the strongest forms on their merits. The benign-winner and sprint answers are by mechanism ($\kappa_W$, incidence, conversion target), not by norm.
11. **Over-claiming the coincidence of thresholds.**
    - *Risk.* Saying "narrowing is compounding" without its conditions.
    - *Avoid.* State it as "with a prize proportional to capacity, without provision or diffusion", and give the diffusion-separated thresholds in Scope.
12. **Implementers working section by section lose the global line.**
    - *Avoid.* One integration editor reads the whole core after §6 and again after §12, against §1.2, Table 7.1 and the hand-off list, and owns the vocabulary sheet.

---

## 9. Implementation order

1. **Math by key in `src/`**, each with check blocks: A1–A22 and the new results (`standprice` general, `scissors`, `detectlink`, `jointscissors`, `mpe`, `growprize`; optionally `metaloop`). Port the reviewers' scripts.
2. **Part I sections**, §2→§6, with boxes and hand-offs. Integration-editor pass.
3. **Part II**: §7, including Table 7.1 and the S7 matrix. EVIDENCE updates go first, so §7.3 uses them.
4. **Part III and IV**: §8→§12; X8 failure-mode table before §12.1.
5. **Front matter last**: abstract, §0, §1, then the guide from the final §1.2.
6. **Companions and registers**: CLAIMS disposition, TESTS (robustness matrix, cruxes, tests), LEDGER sentence level, CHANGELOG, README.
7. **Tools**: xref additions, banned phrases, full checks.
8. **Outside review**: Codex, with the three unification objects and the new mathematics as its first targets. Then Ren.

---

## 10. Open questions for Ren

1. **A short version.** After V6.2 is stable, should a 10–12k-word venue paper be extracted from the spine (§1.1's seven results, Table 7.1, the judgment), with the full theory as its companion? This memo keeps V6.2 complete at about 28k words.
2. **The meta-loop toy.** Should V6.2 try to build it (Supplement only, labelled a toy)? If it works, the title's "meta-attractor … and the generative alternative" is shown in Definition 2.4(2)'s sense in one model. If it needs ad hoc pieces, it is dropped.
3. **"Host" in English.** The Chinese now uses 母体. The English "host" carries the same parasitic overtone that 宿主 did, though in oncology the tumour's host is the body it belongs to. Keep "host" and define it once as "the body every carrier lives in (母体)", or change it (for example to "the shared body")?
4. **Meadows and thresholds.** Is it right that both stand? Parameter interventions below threshold are re-absorbed, and the paradigm decides which parameters are moved and whether they are held. Or should the paradigm be given a stronger role (fidelity minor 3c)?
5. **Provenance of two corpus lines.** Are 不要把人类尚未解决的斗争，升级为智能的斗争 and 真正之秩序，非得永远正确之人，乃立错误不能无限扩大之构 Ren's own sentences, or drafted from his ideas? The guide uses both.
6. **The guide's register.** Is the plain modern register of §5.3 right, or does Ren want the 意义 paragraph in his book's more classical voice?
7. **Narrow E1's premise.** Is Ren content to state narrow E1's scope as "the decisions whose delegation would lock with near certainty", which makes the strict-equilibrium claim exact, with broad E1 as the scope beyond it?
8. **The coincidence result's prominence.** Should "looking ahead narrows the self exactly where leads compound" be in the abstract and §1.2 (as drafted), or kept in §3.5 until outside review checks it?
