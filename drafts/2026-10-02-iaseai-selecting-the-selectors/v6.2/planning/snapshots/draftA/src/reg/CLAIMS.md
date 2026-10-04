# V6.1 claim register

Companion to [THEORY.md](THEORY.md), [SUPPLEMENT.md](SUPPLEMENT.md) and [DISCUSSION.md](DISCUSSION.md). It records the thesis and the definitions fixed before any comparison, every numbered result by its stable key with its v6.0 predecessor and what changed, the dependency chain from mechanism to judgment (link $k$ is item $k$ of THEORY §1.2), the open interfaces, and the disposition of the v6.0 reviews. Prepared 3 October 2026 by Claude (Opus 5.5) under [V6.1-PLAN.md](../V6.1-PLAN.md), from the planning memos in `../v6/v61-planning/`.

**Provenance.** R: Ren's own text or recorded position. A: drafted by an AI in an earlier version and adopted by Ren. D: drafted in this version, not yet reviewed by Ren. L: a standard result from the literature, applied here.

## 1. Thesis

Where carriers are selected by relative success, what is won can be reinvested in the capacity to win, and a lead can become decisive, success raises the stakes and the gain from defection while it weakens the sanctions, the correctors and the shared language that could restrain it. Where success can also buy the selectors, that weakening is reproduced by the selection itself. This is the selection pressure of winning (R), and its reflexive closure is the meta-attractor of winning (R, A). It accelerates the contest, makes it harder and harder to regulate, and alienates language, and the three reinforce one another (R). The conditions are interconnected, and near equal standing they combine into one loop gain (D). AI is the logic's most powerful instrument and can become its next carrier, weakly through the outermost loop and strongly where its lineages become carriers (R, D). There is one host and no outside; against failures that are global and irreversible, integration must be anticipated on an accurate model of the system, which is why understanding that we are one interconnected system is a long-term requirement if growth and change are favoured (R, D). The way out is to change what winning confers, so that the same reflexive structure becomes generative (R, A). Under the protection standard and the present evidence, that change is warranted now, in three tiers (D).

This is a situated argument about the path we are on. It does not claim that every form of bounded competition fails, that every race ends at zero survival, that decisive advantage is attainable, that the signatures load on one factor, or that one institutional blueprint is best.

## 2. Definitions fixed before comparison

- **The selection pressure of winning** ({{cond}}): relative selection with a shared fraction $\beta$; convertibility of winnings into stocks, with provision $k_0$ not won in the contest; decisiveness $r$; and, for the closure, reflexive access to the selection itself. Interconnected conditions, not one cause.
- **The meta-attractor** ({{meta}}): three layers, the mechanism, an attracting configuration in a specified model, and a long transient; a claim of the second layer about the world is a conjecture.
- **Pathological and generative** ({{pathgen}}).
- **Ψ, the winning model** ({{psi}}): locally rational, systemically false, partly made true.
- **Signatures** T1–T6 (THEORY §7.3), grouped W, C, N.
- **Outcomes** O1–O4 (THEORY §1.3) and **the protection standard** with the rule for $\Theta$ (THEORY §8.1).
- **The correctable kernel** ({{kernel}}), **profiles** ({{profile}}) and **durability tests** D1–D8 ({{durability}}).
- **Labels** are listed at the end of THEORY and in SUPPLEMENT S0; premises are named in words, with former letter codes as aliases.

## 3. Claim tags

[def] definition; [val] value; [thm] proved in its model (SUPPLEMENT); [thm∣prem] proved given named premises; [prem] premise; [obs] observation with an evidence row; [num] reproduced by `checks_v61.py` or an earlier suite; [conj] conjecture; [rec] recommendation.

## 4. Contribution inventory

Every numbered result, by stable key. "Carried" means the statement is that of v6.0, possibly shortened in the core with the full statement in the Supplement; changes of content are listed in LEDGER §3.

| Key | V6.1 | v6.0 | Result | Proof; check | Change in V6.1 |
|---|---|---|---|---|---|
| `cond` | {{cond}} | Def 2.1 | The selection pressure of winning | S2; — | Three conditions plus reflexive access; $\chi,\rho$ replaced by $\beta,\kappa_c,k_0$; "interconnected conditions", not one pressure |
| `loopgain` | {{loopgain}} | new | One loop gain | S2; LG | New: one loop gain decides compounding and prices standing |
| `compound` | {{compound}} | Rem 5.3 | When winnings compound, and what enough requires | S2; LG, SM | Remark → proposition; $\beta$, convertible share and provision $k_0$; global condition for caps; growth variant corrected |
| `meta` | {{meta}} | Def 2.2 | Meta-attractor | S2; — | Carried |
| `bench` | {{bench}} | Rem 2.3 | A local feedback benchmark | S2; FB | Carried |
| `pathgen` | {{pathgen}} | Rem 2.4 | Pathological and generative meta-attractors | S2; — | Carried |
| `viab` | {{viab}} | Def 3.1 | Viability | S3; — | Carried |
| `relsel` | {{relsel}} | Def 3.2 | Relative selection | S3; — | Carried |
| `blind` | {{blind}} | Lem 3.3 | Blindness, and what a common rule needs | S3; CI | (2) incidence and (3) evasion with a tipping share replace "universal constraints are invisible" |
| `load` | {{load}} | Prop 3.4 | Selection raises the load | S3; — | Carried |
| `twochan` | {{twochan}} | Prop 3.5 | Two-channel accounting | S3; TC, TH, SM | Renege gain to the $n-1$ others is $\beta\Omega(n-1-\theta)/(n-1)$; identification confounded by $\psi$ |
| `boundary` | {{boundary}} | Prop 3.9 | The boundary error of the self-model | S3; RH | Carried |
| `wow` | {{wow}} | Prop 3.6 |  | S3; — | Stated briefly in the core; $\Theta\to\Upsilon$ |
| `unequal` | {{unequal}} | Rem 3.8 |  | S3; — | Carried |
| `standprice` | {{standprice}} | new | Compounding manufactures the relative objective | S3; LG, NB | New: compounding manufactures the relative objective ($\theta_\Gamma$) |
| `onegroup` | {{onegroup}} | Lem 3.10 | What selection at any level cannot supply | S3; PR | For every partition, with the transmission term; anticipation needed only for global irreversible failures |
| `club` | {{club}} | Prop 3.11 | Clubs and blocs | S3; CB, SM | Blocs carry shared loss $s\ell$; unequal blocs asymmetric |
| `psi` | {{psi}} | Def 2.5 | Ψ, the winning model | S3; — | Carried |
| `capture` | {{capture}} | Def 4.1 | Selector modification and capture | S4; — | Carried |
| `costq` | {{costq}} | new | The cost of conversion capacity | S4; — | New: cost structure explicit; $[H_\gamma]$, $[H_f]$ stated as hypotheses |
| `influence` | {{influence}} | Prop 4.2(1)–(3) | Influence over correctors is selected in the largest carriers | S4; CS | Threshold exponent depends on the size elasticity of cost |
| `noinside` | {{noinside}} | Prop 4.3 |  | S4; — | Carried |
| `corrrate` | {{corrrate}} | Prop 4.4 | Required independent correction, and its rate | S4; CS | Rate law robust to cost scaling; threshold, splitting factor and concentration measure are not (third moment or Herfindahl) |
| `countervail` | {{countervail}} | Rem 4.5 |  | S4; — | Carried |
| `masking` | {{masking}} | Prop 4.6 | Detection under a fixed averaged alarm | S4; — | Carried |
| `alarm` | {{alarm}} | Rem 4.7 | Alarms that do not miss | S4; AC | (4) exact for static affine masking; filter with memory defeats it |
| `certificate` | {{certificate}} | Prop 4.8 | Configurations and certificates | S4; FA | Carried |
| `reabsorb` | {{reabsorb}} | Prop 4.9 | Cascades and reforms | S4; — | Carried |
| `pausefield` | {{pausefield}} | Prop 4.10 | A pause that freezes shares | S4; DW | Frozen-share threshold 0.68 (was 0.8); dwell exact |
| `slowroute` | {{slowroute}} | Thm 4.11 | No viable race through the host | S4; — | H0–H5 renamed (reach), (a)–(e); dependence on $[H_\gamma]$ stated |
| `join` | {{join}} | Prop 5.1 |  | S5; — | Carried |
| `dissipate` | {{dissipate}} | Prop 5.2 | Dissipation | S5; — | $\theta_g$ restored |
| `frontier` | {{frontier}} | Rem 5.6 | The frontier switch: what cancer does when the body runs out | S5; FS | Carried |
| `enforce` | {{enforce}} | Prop 5.7 | The enforcement condition | S5; EC, NB | Breakout term $\delta p_d(D-C)$; exact $\bar p_d$; old bound exact only at $D=C$; breakouts during punishment |
| `relpunish` | {{relpunish}} | Cor 5.8 | Relative objectives and punishments that can be imitated | S5; CR | $n=2$ all punishments; $n\ge3$ same-strategy only; role-differentiated counterexample |
| `restraint` | {{restraint}} | Thm 5.16(1)(2) | What restraint needs where breakouts are possible | S5; — | Replaces Thm 5.16(1)(2): two kinds of means; no claim that custody is the only route |
| `wingives` | {{wingives}} | Prop 5.10 | What a decisive winner gives | S5; WG, SM | Renege denominator $n-1$ |
| `preventattack` | {{preventattack}} | Prop 7.4 |  | S5; — | Carried |
| `racehazard` | {{racehazard}} | Prop 5.4 | Race-generated hazard and its four levers | S5; RH | Carried |
| `nonsum` | {{nonsum}} | Lem 5.5 |  | S5; — | Carried |
| `tempo` | {{tempo}} | Prop 5.11 | The tempo bound | S5; — | Carried |
| `coverage` | {{coverage}} | Thm 5.12 | Coverage mismatch on a continuation branch | S5; — | Carried |
| `freeze` | {{freeze}} | Prop 5.13 |  | S5; — | $\Gamma\to\varrho$; stated briefly in the core |
| `enough` | {{enough}} | Prop 8.11 | A point of enough | S5; PE, SM | (3) non-satiation, not relative position alone |
| `talk` | {{talk}} | Prop 5.14 | Talk under relative accounting | S5; TK, T3 | $n\ge3$: effective bias $b_0n/(n-2)$; rivals silent, allies blocs |
| `faithful` | {{faithful}} | Prop 6.1 | Faithful AI in a harmful game | S6; SM | Cost-exponent condition corrected |
| `delegate` | {{delegate}} | Prop 6.2 |  | S6; — | Carried |
| `lockin` | {{lockin}} | Lem 6.3 | Capacity lock-in | S6; — | Carried |
| `delegatelock` | {{delegatelock}} | Prop 6.4 | Delegation when the lock counts | S6; SM; v5 DL | "At least one, possibly both" |
| `retain` | {{retain}} | Lem 6.5 | Delegation and the selection of decisions | S6; — | Carried |
| `transmit` | {{transmit}} | Rem 6.6 |  | S6; — | Carried |
| `nested` | {{nested}} | Prop 6.7 | The nested reward loop | S6; CI | Alignment-tax premise $(A_\tau)$; three classes of divergence; weak and strong incarnation |
| `opaquecorr` | {{opaquecorr}} | Prop 6.8 | Correction that people cannot understand | S6; v5 OV | Carried |
| `topology` | {{topology}} | Prop 6.9 | Oversight topology | S6; SM | Row sums necessary, not sufficient, for independent errors |
| `lyapunov` | {{lyapunov}} | Rem 6.10 |  | S6; — | Carried |
| `homeostasis` | {{homeostasis}} | Prop 6.11 |  | S6; v5 HO | Stated briefly in the core |
| `branches` | {{branches}} | Thm 5.15 | Classification of contest branches | S7; — | Branches defined by loop gain and breakout probability |
| `raceselects` | {{raceselects}} | Prop 7.2 | What the race selects | S7; — | Moved before the corollary that uses it; premise stated |
| `racepremise` | {{racepremise}} | Thm 5.16(3) | What the premise of the race cannot justify | S7; — | Replaces Thm 5.16(3): individual and collective rationality separated |
| `kernel` | {{kernel}} | Def 8.10 | The correctable kernel | S8; — | Discriminating (guaranteed-viability) kernel |
| `fallback` | {{fallback}} | Lem 7.11 | When an arrangement cannot do worse | S8; FD, SM | Proof by coupling; conditioning step withdrawn |
| `survassure` | {{survassure}} | Prop 7.9 | Assurance in survival terms at a common horizon | S8; v5 SR | Carried |
| `profile` | {{profile}} | Def 7.12 | What an arrangement changes | S8; — | Descriptive: direction of selection recorded |
| `durability` | {{durability}} | Def 7.8 | Durability tests | S8; — | Carried |
| `lead` | {{lead}} | Rem 7.1 |  | S8; — | Carried |
| `sprint` | {{sprint}} | Prop 7.3 |  | S8; — | Carried |
| `preventown` | {{preventown}} | Prop 7.5 | Prevention under the preventer's own criterion | S8; — | Carried |
| `insure` | {{insure}} | Rem 7.13 |  | S8; — | Carried |
| `assure` | {{assure}} | Prop 9.1 | Assurance | S8; v5 N13 | Carried |
| `verify` | {{verify}} | Thm 7.7 | Verification and the value of winning | S8; — | Carried |
| `overhang` | {{overhang}} | Prop 7.6 |  | S8; — | Carried |
| `require` | {{require}} | Prop 7.10 | Requirements, by the kind of support each has | S9; HO, FA | Three kinds of support; R1, R3, R4, R8 exceptions completed; R7 normative |
| `nounilateral` | {{nounilateral}} | Prop 8.3 | No unilateral solution | S9; — | $\Theta_s\to\Upsilon_s$ |
| `commonfront` | {{commonfront}} | Prop 8.4 |  | S10; — | Carried |
| `commonfrontn` | {{commonfrontn}} | Prop 8.5 |  | S10; — | Carried |
| `share` | {{share}} | Prop 8.6 | What sharing, pooling and convertibility change | S10; SH | (3) with provision $k_0$; "only the third lever reverses" withdrawn |
| `twoorders` | {{twoorders}} | Rem 8.7 | Concentration at two orders | S10; — | Carried |
| `safeguards` | {{safeguards}} | Thm 8.2 | Sufficient safeguards, and a necessary condition | S10; HO | Margin on pointwise harsher threshold hosts |
| `rivalverify` | {{rivalverify}} | Prop 8.8 | Rival verification | S10; — | Carried |
| `participate` | {{participate}} | Prop 8.9 | Participation | S10; v5 K7 | Carried |
| `guardian` | {{guardian}} | Rem 8.12 | The guardian test | S10; — | Carried |
| `relaxtrust` | {{relaxtrust}} | Cor 9.2 | What relaxes the trust constraints | S11; — | Carried |
| `signal` | {{signal}} | Prop 9.3 | When keeping AI out of one's decision loops is a signal | S11; — | Carried |
| `pausevalue` | {{pausevalue}} | Prop 9.4 | A pause is valued by what changes during it | S11; — | Carried |
| `readiness` | {{readiness}} | Def 9.5 | Readiness to resume | S11; — | Carried |
| `reachable` | {{reachable}} | Prop 9.6 | Requirements of a reachable path | S11; — | Carried |
| `tdec` | {{tdec}} | new | Time to decisiveness | S2; — | New |
| `thrrep` | {{thrrep}} | Rem 3.7 | Thresholds and repetition need observation | S3; — | Carried |
| `scope` | {{scope}} | Prop 4.2(4) | Scope | S4; — | Carried |
| `fieldlemma` | {{fieldlemma}} | App A field lemma | The field is cooperative | S4; — | Carried |
| `zonesillus` | {{zonesillus}} | Rem 5.9 | An illustration: the faithful-AI game at the boundary case | S5; BI, NB | Moved to the Supplement; thresholds are of the boundary case $D=C$, not bounds |

Three keys are retired: `dilemma` (v6.0 Theorem 5.16), whose content is now {{restraint}} and {{racepremise}}; `changesel` (v6.0 Definition 8.1), merged into {{require}}; and the v6.0 numbering of the enforcement result, whose key `enforce` is kept.

## 5. Dependency chain

Link $k$ is item $k$ of THEORY §1.2.

| Link | Claim | Type | Support | Status |
|---|---|---|---|---|
| L1 | The conditions of winning combine into one loop gain at their core; decisive positions and the tempo of correction are further conditions | def + thm | {{cond}}, {{loopgain}}, {{compound}} | Proved in the contest model; that the parameters move together in the world is a conjecture (C0) |
| L2 | Relative selection cannot see what all share; common constraints survive only with equal incidence and sanctioned evasion; compounding manufactures the relative objective; global irreversible failures must be anticipated | thm | {{blind}}, {{twochan}}, {{standprice}}, {{boundary}}, {{onegroup}} | Proved; anticipation's success a conjecture |
| L3 | Influence over correctors is selected; independent correction must grow at a stated rate; reforms that leave conversion above one are re-absorbed | thm + obs | THEORY §4; EV3, EV4 | Mechanism proved; diagnosis partly evidenced (C2); quasi-static assumption untested |
| L4 | The conditions accelerate the contest and erode enforcement, correction and talk; growth moves both blades of the scissors | thm∣prem | {{enforce}}, {{restraint}}, {{coverage}}, {{talk}} | Each arm proved; the conjunction composite |
| L5 | AI as instrument and as weak and strong incarnation; under $(A_\tau)$ only enforced common constraints keep common-cost divergences countered | thm + thm∣prem | {{faithful}}, {{delegatelock}}, {{nested}} | Proved in the stated structure; $(A_\tau)$ is crux C9 |
| L6 | The present trajectory shows the signatures; the premise of the race describes the case in which repetition stops enforcing restraint | obs + thm∣prem | THEORY §7; EV1–EV9 | Partly evidenced; T4 the gap; decisiveness not established (C5) |
| L7 | Alternatives that succeed move the shared parameters for every capable actor; requirements by kind; several cannot be met alone | thm∣prem + comparison | {{require}}, {{nounilateral}}; THEORY §8 | Necessity in named models; registered conditions in TESTS §3 |
| L8 | A generative order persists through what all share and can be specified by function | rec + thm | THEORY §10; DISCUSSION X10 | Design specified; durability unknown (C4) |
| L9 | A staged transition is reachable in stages; trust is an outcome | thm + rec | THEORY §11 | Reachability conditional |
| L10 | The change of selection is warranted now, in three tiers | rec | THEORY §12 | Tiers 1–2 do not depend on the ranking of whole designs; tier 3 is a stated judgment |

## 6. Open interfaces

SUPPLEMENT S13 gives the full table. Open: the production relation between coverage $U$ and the correction rate $d$; the step from capability to hazardous variety; the step from coverage to residual risk; the price of standing in the full stochastic game; capacity evolving with the field (TESTS, Study 2); the slow variable for selected minds; threshold and vector hosts.

## 7. Disposition of the v6.0 reviews

Sources: six reviews of v6.0 (math, fidelity, adversarial, evidence, alignment, systems), the Codex review and counterexamples, four Opus checks, the synthesis, three readiness assessments, and the GPT review summary Ren supplied. Status words: **repaired**, **restated** (raised to the right level, content kept), **narrowed**, **withdrawn**, **open**.

| Finding | V6.1 action | Status |
|---|---|---|
| "One pressure" not proved; signatures not one factor | Interconnected conditions with one loop gain at their core ({{loopgain}}); single-factor covariation a research question; Test E (cross-effects) and Test Γ registered | Restated |
| Enforcement bound wrong except at $D=C$; DF check circular | {{enforce}} with the breakout term and exact $\bar p_d$; checked by value iteration (EC) | Repaired |
| Theorem 5.16 conflated branches; "requires custody" not derived; individual and collective rationality mixed | {{restraint}} and {{racepremise}}; custody one of several means | Repaired |
| Corollary 5.8 scope | $n=2$ all punishments; $n\ge3$ same-strategy only; counterexample | Repaired |
| Lemma 3.3(2): universal ≠ equal incidence; evasion selected | Incidence and evasion parts, tipping share | Repaired |
| Lemma 3.10 dropped the transmission term; "only anticipation" called a theorem | Every partition; transmission; anticipation only for global irreversible failures; theorem claim withdrawn | Repaired, narrowed |
| Remark 5.3: $\chi$ was a sharing parameter; caps only local | {{compound}} with $\beta$, $\kappa_c$, $k_0$, global cap condition | Repaired |
| Proposition 5.14 fails for $n\ge3$ | {{talk}}(2) | Repaired |
| Proposition 7.10 mixed necessary, sufficient and normative | {{require}} by kind; exceptions completed | Repaired |
| Section 4 depends on cost scaling; AI lowering control cost unsourced | {{costq}}; $[H_\gamma]$ a hypothesis; robust and fragile results separated | Repaired |
| Smaller items: renege denominator; blocs $s\ell$; $\theta$ identification and $\psi$; fallback proof; cost exponents; one-or-both; correlated errors; kernel; harsher hosts; dwell times; autocorrelation | Each repaired at its result; numbers in `checks_v61.py` | Repaired |
| "We are one" slid back to an objective weight in about a dozen places | Three jobs, through understanding; "Oneness is what these requirements are requirements of" | Restated |
| Lost content: relational self and 大同; coupling rising with power; $\theta_g$; reform dilemma; four loops; W→C→N; unbounded relative; five endgames; sample-size hedge; offense–defense; one lever; narrative frames; epistemic closure | Restored (LEDGER §4) | Repaired |
| AI incarnation overstated; reward hacking ≠ tampering | Weak and strong incarnation; $(A_\tau)$; three classes of divergence | Repaired |
| Judgment over-claimed from standard D | Three tiers; rule for $\Theta$; ranking stated as judgment; E2's cost as C10 without redefining O1 | Repaired |
| Generative loop closed through contributors holding rule positions | Closure through what all share; the examination-system path named as the pathology | Repaired |
| Compact owned its own correctors | Separately held functions; correction outside; end conditions; coercive fallback treated as prevention | Repaired |
| Evidence asymmetries and citation errors | EVIDENCE corrections list; precedent table corrected (DISCUSSION X11) | Repaired |
| "Long and unstructured" | Core of about 30,000 words in four Parts by level of claim; Supplement and Discussion; registers | Repaired; length above the 27,000 target (CHANGELOG) |
| Joint quasi-static simulation; alternative-lineage dwell; Codex verification of the new mathematics | Not done | Open |

**The experiment record.** One 20-seed rubric-editing pilot exists; its first prediction failed and three held; Design 2 has not been run (EV12).
