# v6 claim register

Companion to [THEORY.md](THEORY.md). It records the thesis and definitions fixed before the comparison, every formal result with its status, predecessors and provenance, the dependency chain from mechanism to judgment, the interfaces between modules, and the disposition of every issue raised against v5.2 by the self-review, the five reviews and the GPT-6 revision path. Prepared 3 October 2026 by Claude (Opus 5.5), under the [V6 plan](../V6-PLAN.md), from the six planning memos in [`../v6-planning/`](../v6-planning/).

**Provenance marks.** **R**: Ren's own text or recorded position. **A**: drafted by an AI in an earlier version and adopted by Ren. **D**: drafted in this version and not yet reviewed by Ren. **L**: a standard result from the literature, applied here. Several marks can apply to one claim.

## 1. Thesis

Wherever carriers are selected by relative success, and what is won can be reinvested in the capacity to win again, there is a selection pressure of winning (R, D). When success can also buy control over the selection itself, over the rules, the correctors, the formation of minds and the language in which success is described, the pressure closes on itself: the meta-attractor of winning (R, A). It is not bound to any substrate (R).

The pressure acts through overlapping mechanisms and has three consequences: acceleration, correction that falls behind and is captured, and the alienation of language (R). These erode the three means of restraining it, enforcement, correction and shared understanding, and growth widens the gap (D). AI is the logic's most powerful instrument and can become its next carrier; the outermost loop of training is the selection among developers (R, D).

There is one host and no outside. At this scale integration must be anticipatory, so understanding that we are one interconnected system is a long-term requirement if growth and change are favoured (R, D). The way out is to change what the system selects for, so that the same reflexive structure becomes generative (R, A). Under standard D and the present evidence, that change is warranted now.

This is a situated argument about the path we are on. It does not claim that every form of bounded competition fails, that every race ends at zero survival, that decisive advantage is attainable, or that one institutional blueprint is best.

## 2. Definitions fixed before comparison

**The selection pressure of winning** (THEORY Definition 2.1): relative selection, convertibility ($\chi$, $\rho$) and decisiveness ($r$) together. Remove any one and the loop opens.

**The meta-attractor** (Definition 2.2), stated in three layers, each claim saying which it concerns:
1. the mechanism, reflexive selection with positive coupling $\gamma$ (in linear form $ab$);
2. an attracting configuration in a specified model, shown in the field model of THEORY §4;
3. a long transient, which is not an attractor.

Real-world attractiveness is marked [C] wherever it is asserted.

**Pathological and generative** (Remark 2.4): pathological to the degree that reproduction depletes the unpriced shared conditions, weakens correction, or forecloses alternatives; generative to the degree that it strengthens independent correction and keeps alternatives reachable.

**Ψ, the winning model** (Definition 2.5): the configuration of self-model and doctrine the pressure selects. Ψ1 the isolated self; Ψ2 naive Darwinism, with a normative clause; Ψ3 winner-take-all compounding. Ψ is not the root of the dynamics. It is locally rational, systemically false and partly made true by institutions.

**Signatures** (THEORY §2.5).

| Code | Signature | Group |
|---|---|---|
| T1 | Strategic success defined by relative or decisive advantage | W |
| T2 | Capability, deployment and delegation accelerate when rivals advance | W |
| T3 | Oversight depends on the overseen | C |
| T4 | Success reinvested in influence over evaluation and rules | C |
| T5 | Shared harms not reflected in decisions | N |
| T6 | Restraint and shared provision treated as unrealistic | N |

**Outcomes** (THEORY §1.4).

| Code | Outcome | Weight |
|---|---|---|
| O1 | Physical catastrophe: large-scale loss of life | Protected first |
| O2 | Irreversible loss of human decision authority over consequential systems in a defined domain | Protected first |
| O3 | Interruption of essential services | Protected |
| O4 | The end of a particular organization's or government's tenure | Not protected as such |

**Decision standard D** (THEORY §1.4): robust satisficing on O1 and O2 at common horizons over one justified range $\Theta$ applied to every path, the cooperative design's own failure modes included.

**What an arrangement changes** (Definition 7.12): a profile, not a label. Mechanisms acted on; whether it changes selection (consequences return; success cannot buy control of its own assessment; decisive stakes bounded or held in common; shared measurement and language); coverage; bindingness; whether enforcement survives decisiveness; reversibility by success; fallback and own risk; durability D1–D8. The *pivot* is the direction in which profiles move, whatever an arrangement is called. Registered prediction [C]: arrangements that constrain conduct under an unchanged pressure erode as stakes and speed grow; arrangements that change selection persist.

**Label families**: H0–H5 conditions of Theorem 4.11; U1–U4 conditions of contestable coverage; P1–P3 premises of the race; C0–C8 cruxes; N1–N3 normative cruxes; R1–R8 requirements; Q1–Q7 readiness dimensions; D1–D8 durability tests; E1–E3 temporal arrangements; EV1–EV17 evidence rows; T-A to T-K pre-registered tests.

## 3. Claim types

[D] definition; [V] value; [T] theorem proved in its model (THEORY Appendix A); [T∣A] composite or conditional result; [A] assumption serving as a premise; [O] observation with an evidence row; [N] numerical observation reproduced by `checks_v6.py` or an earlier suite; [C] conjecture; [R] recommendation.

## 4. Contribution inventory

| v6 | v5.2 | Statement | Key assumptions | Proof or check | Closest predecessor | Difference | Provenance |
|---|---|---|---|---|---|---|---|
| Def 2.1 | — | The selection pressure of winning | Relative selection; convertibility; decisiveness | D | Moloch; "success to the successful" (Senge 1990); generator functions | One pressure, three conditions, substrate-free | R (three ingredients, 2024, 2026; the winner's rule, 2024), D |
| Def 2.2, Remark 2.3 | Def 3.1, Remark 3.2 | Meta-attractor in three layers; local benchmark $ab<\mu\delta$ | Linearization | D; FB | Richardson 1960; Thomas's rule (Soulé 2003); Goodhart; Campbell | Layers separated; Richardson named | R (2025), A, D |
| Remark 2.4 | — | Pathological and generative meta-attractors | — | D | Corpus v2 neutral definition | Same structure, opposite selection | A |
| Def 2.5 | Def 1.1 | Ψ as the configuration selected, locally rational and systemically false | — | D | Alchian 1950; Friedman 1953 | Not a root; attributed Ψ split into misjudgment and correct forecast | R, D |
| §2.7 | — | Five predictions of "one pressure" and its refutation conditions | — | C | Systems review S | Makes the claim falsifiable | D |
| Lemma 3.3 | Lemma 2.3 | (1) Relative selection is blind to common terms; (2) universal constraints are invisible to it, unilateral ones are selected against | A1 | A; UC | Weibull 1995 | Part (2): the formal reason coordination works | L, D |
| Prop 3.4 | Prop 2.4 | Selection raises the load | Payoff-monotone | A | Price 1970; Schaffer 1988 | — | A |
| Prop 3.5 | Prop 1.2 | Two-channel accounting identity; λ↔θ; rebated levy $\tau(n-1-\theta)/n$; renege gain; host and spite thresholds | $O_i=\pi_i+\theta\bar\pi_{-i}$ | A; TC (4,000 games) | Other-regarding preferences | One identity unifies six results | D |
| §3.4 (measuring θ) | — | Two perturbations identify θ: $R=n(1+\theta)/(n-1-\theta)$ | Contest of §3.6 | TH | — | A measurement design | D |
| Prop 3.6, Remarks 3.7–3.8 | Prop 2.5, Remarks 2.6–2.7 | Weight on winning; thresholds and repetition need observation; unequal exposure | Linear host | A | Armstrong, Bostrom and Shulman 2016 | — | A |
| Prop 3.9 | Prop 4.2 | The boundary error; selection favours θ = −1 | Tullock | A | Schaffer 1988; Güth and Yaari 1992 | — | A |
| Lemma 3.10 | — | One group: no between-group term, so integration must be institutional and anticipatory | Price equation | A | Price 1970; Maynard Smith and Szathmáry 1995; West et al. 2015 | The formal content of "we are one" as a requirement; that anticipatory integration can succeed is [C] | R (2026-10-02 direction), D |
| Prop 3.11 | — | Clubs over-produce harm to outsiders; blocs reproduce the game | Concave common value | A; CB | Choi and Bowles 2007 | Inclusion of contestants is not inclusion of the system | D |
| Def 4.1; Props 4.2–4.4; Remark 4.5 | Def 3.3; Props 3.4–3.6; Remark 3.7 | Selector modification; influence selected with return ∝ share²; correction not supplied from inside; required rate $g/(1+\eta)$ | Appropriability; long horizons | A | Krakauer, Page and Erwin 2009; Stigler 1971 | — | A |
| Prop 4.6, Remark 4.7 | Prop 3.8, Remark 3.9 | Masking; alarms that do not miss | Averaged reports | A | Lizzeri 1999 | — | A |
| Props 4.8–4.10, Thm 4.11 | Props 3.10–3.12, Thm 3.13 | Certificates, cascades, keystones, pauses; the slow route | Cooperative field | A | Kempe, Kleinberg and Tardos 2003; Acemoglu and Robinson 2008 | Conditions renamed H0–H5 | A |
| Props 5.1, 5.2 | Props 5.1, 5.2, 1.3(2)–(3) | Join or eliminate; dissipation and its ceiling | Tullock | A | Hillman and Riley 1989 | — | A |
| Remark 5.3 | — | Equal standing unstable iff $\chi r>1$; a point of enough below $K^\ast$ preserves standing | Linear reinvestment | A; RI | Arthur, Ermoliev and Kaniovski 1987 | Exact content for the three ingredients | R (2024, 2026), D |
| Prop 5.4 | Prop 1.4 | Race-generated hazard and its four levers; background hazard; summability, not saturation | $(\mathrm{A_G})$; myopic stage equilibria | A; RH | Time of perils | A decomposition, not a necessity theorem | D (after GPT-6) |
| Lemma 5.5 | Lemma 4.4 | Nonsummable residual hazard | Bounds on surviving histories | A | Ord 2020 | — | A |
| Remark 5.6 | — | The frontier switch: peace of abundance, not of accounting | Toy model | A; FS2 | Hirshleifer 1991; Skaperdas 1992; Hamilton 1970 | Cancer's switch made exact | R (cosmic cancer), D |
| Prop 5.7 | — | Decisiveness removes the shadow of the future: sustainable iff $g_i\le\frac{\delta(1-p_d)}{1-\delta}(O_i(a^\ast)-v_i)$ | Decisive position valued at most the cooperative payoff | A; DF (5,274/5,274) | Folk theorem; Abreu 1988 | General form of the first erosion | D |
| Cor 5.8 | — | Relative objectives cannot be held by symmetric punishment | Symmetric game, symmetric punishment | A; DF (1,260) | Duersch, Oechssler and Schipper 2012 | Scope stated | D |
| Remark 5.9 | — | The binary illustration: $\theta^\ast$, $\theta_{\text{rep}}$ | Faithful-AI game | A; DF | — | The former three zones, as an illustration | D |
| Prop 5.10 | — | What a decisive winner gives: nothing (linear) or $\theta/(1+\theta)$ (log) | Unconstrained winner | A; WG | — | "The winner justifies all", formally | D |
| Props 5.11, Thm 5.12, Prop 5.13 | Props 5.7, Thm 5.8, Prop 5.9 | Tempo bound; coverage mismatch; freezing and rollback | (X), (U), (φ) | A | Hayes 1950 | Coverage conditions renamed U1–U4 | A |
| Prop 5.14 | Prop 8.3 | Talk under opposed objectives: uninformative in zero-sum games; Crawford–Sobel bias | — | A; TK | Crawford and Sobel 1982; Farrell and Rabin 1996 | Part (1) and its use as the third erosion | L, D |
| Thm 5.15 | Thm 5.15 | Classification of contest branches | — | A | — | — | A |
| Thm 5.16 | — | The dilemma of decisiveness | Composite | A | Fearon 1995; Powell 2006 | Oneness necessary only under C5, C7 and incomplete coverage | D |
| Prop 6.1 | Prop 4.1 | Faithful AI in a harmful game | — | Text | ARCHES (Critch and Krueger 2020) | Scaling cases | A |
| Props 6.2–6.4, Lemma 6.5 | Props 5.3, 5.5; Lemmas 5.4, 5.6 | Delegation; capacity lock-in; the lock priced in | — | A | — | — | A |
| Prop 6.7 | — | The nested reward loop: what the outermost level selects reaches the innermost optimizer, except constraints common to all | Level 2 relative and payoff-monotone | A (composition) | Omohundro 2008; Turner et al. 2021; Skalse et al. 2022 | Instrumental convergence and reward hacking as coordination problems at the level that decides | R (2026-10-03 direction), D |
| Props 6.8–6.11, Remark 6.10 | Props 5.10–5.13, Remark 5.12 | Correction beyond understanding; oversight topology; prediction and certification; risk homeostasis | — | A | — | — | A |
| Remark 7.1–Thm 7.7; Def 7.8 | Remark 6.1–Thm 6.7; Def 6.8 | The alternatives at their strongest; durability tests | — | A | — | D7 and D8 added | A, D |
| Prop 7.9 | Prop 5.14 | Assurance in survival terms | — | A | — | — | A |
| Prop 7.10 | — | Requirements R1–R8 with their non-necessity conditions | — | A (collection) | — | Necessary, not sufficient; R4, R7, R8 new | D |
| Lemma 7.11 | — | Fallback dominance under F1, F2 | Pointwise hazard bounds | A; FD | — | Turns the comparison into two design conditions | D |
| Def 8.1, Thm 8.2, Prop 8.3 | Def 7.1, Thm 7.2, Prop 7.3 | What a selection-changing arrangement contains; safeguards; no unilateral solution | — | A | — | Custody and admission constraints added | A, D |
| Props 8.4, 8.5, Remark 8.7 | Props 7.4, 7.5, Remark 7.6 | Common frontier; concentration at two orders | — | A | Barrett 1994 | Lineage diversity inside a merged frontier | A |
| Prop 8.6 | Prop 1.5 | Pooling; sharing the divisible prize shrinks the pressure (uninvadable intensity $r\Omega_{\text{eff}}/(nc)$); changing convertibility opens the loop | One common field, $r\le1$ | A; SH | Math review M2; GPT-6 $\Omega_e/\Omega_s$ | "Reverses" withdrawn; credibility factor; positional part | R (the winner's rule), D |
| Props 8.8, 8.9 | Props 7.7, 7.8 | Rival verification; participation | — | A | — | Participation, voting and protection kept apart | A, D |
| Def 8.10 | — | The correctable kernel | — | D | Aubin 1991 | Openness as four capacities | R (keep the possibility space open), D |
| Prop 8.11 | — | A point of enough: bounded exposure under need-directed growth; none for relative objectives | Converse of (φ) | A; PE | — | "Growth is not the danger; the mind is", exactly | R (2026-09-25), D |
| Remark 8.12 | — | The guardian test | — | D | — | Applied to every remedy | R (2025; 2026-10-02) |
| Prop 9.1, Cor 9.2, Prop 9.3 | Prop 8.1, Cor 8.2, Prop 8.4 | Assurance; what relaxes trust constraints; E1 as a costly signal | — | A | Kydd 2005 | — | A |
| Prop 9.4, Def 9.5 | Prop 4.5, Def 4.6 | Pauses valued by what changes; readiness Q1–Q7 | — | A | — | Q7 custody and verifiability | A, D |
| Prop 9.6 | Prop 8.5 | Requirements of a reachable path | — | A | — | Dwell times | A, D |

## 5. Dependency chain

| Link | Claim | Type | Support | Status |
|---|---|---|---|---|
| L0 | One pressure acts through overlapping mechanisms, and the signatures T1–T6 are its marks | D + C | THEORY §2; EV1–EV4, EV15 | Definitions fixed; the one-pressure claim registered with refutation conditions (crux C0) |
| L1 | Relative selection is blind to common terms and to universal constraints | T | Lemma 3.3 | Proved |
| L2 | Success is converted into control over correctors when appropriable; reforms leaving conversion above one are re-absorbed | T + O | THEORY §4; EV3, EV4 | Mechanism proved; diagnosis partly evidenced (crux C2) |
| L3 | The pressure erodes enforcement, correction and shared understanding, and growth widens the gap | T∣A | THEORY §5 | Each arm proved under its conditions; the conjunction composite |
| L4 | Where decisive advantage is attainable, only cooperation built into objectives and custody holds | T∣A | Theorem 5.16 | Conditional on C5, C7; present evidence points to saturation |
| L5 | AI is instrument and incarnation; only constraints common to all survive the outer loop | T + T∣A | THEORY §6 | Proved in the stated structure |
| L6 | Correction must keep pace with the hazardous set; the gap is real for some classes | A + O | THEORY §5.3; EV5–EV7 | Premises stated; crux C1 |
| L7 | Alternatives that succeed do so by changing what is selected; R1–R8 are necessary on active branches | T∣A + comparison | THEORY §7 | Necessity, not sufficiency; registered conditions under which continuation wins |
| L8 | There is one host and no outside; integration must be anticipatory | T + C | Lemma 3.10 | The route is a theorem; its success a conjecture |
| L9 | A generative arrangement can be specified, stress-tested and approached in stages | R + T | THEORY §§8–9 | Design specified; durability unknown (crux C4) |
| L10 | Therefore the change of selection is warranted now | R | THEORY §10 | Holds if L6 and L7 hold within Θ; not a claim that every cooperative design beats regulated competition |

## 6. Interfaces between modules

See THEORY Appendix E for the full table. The open interfaces are:
- the production relation between contestable coverage $U$ and the correction rate $d$;
- the step from capability to hazardous variety, (X);
- the step from coverage to residual risk, (φ);
- the slow variable for minds selected by the pressure, not modelled;
- hosts of Allee type and vector hosts.

## 7. Disposition of the v5.2 review findings

Status: **repaired** (corrected in THEORY.md), **raised** (a claim moved from the level of mind to the level of game and selection, keeping its content), **narrowed** (kept in a weaker, supported form), **withdrawn**, or **open**.

| Source | Finding | v6 action | Status |
|---|---|---|---|
| Self-review F1–F12 | Repaired in v5.2 | Carried | Repaired |
| Math M1 | "One is necessary" fails; a single holdout wins | Theorem 5.16: necessity only under C5, C7 and incomplete coverage; coverage, not identity, required; Appendix G | Raised and narrowed |
| Math M2 | Sharing only shrinks selection in one common field; example in separate fields | Proposition 8.6(2) with $x^\ast=r\Omega_{\text{eff}}/(nc)$; example in one field; positional part; credibility | Repaired |
| Math M3 | The myopic hazard proposition; θ = 0 and θ = −1 separate with foresight and repetition | Proposition 5.7 and Corollary 5.8 generalize; Proposition 5.4 a decomposition | Repaired |
| Math (zones) | Three zones hold only in the binary game; a point in the Tullock contest | Remark 5.9 as illustration; scope notes | Narrowed |
| Systems | $B>4s$ is not bistability; dwell times; compensating loops; crisis windows; Allee hosts; dynamic indicators | Bistable model deferred (§10.6); §9.4 dwell times, loops, crisis windows; §3.2 Allee note; Remark 4.7(4) | Repaired |
| Alignment | Two AI problems; outer loop; O2 test by practical capacity; N3 | §6 instrument and incarnation; Proposition 6.7; §6.6 O2 test; N3 | Repaired |
| Governance realism | Benign winner at its strongest; regulated competition can win; voting and participation | §7.4; registered conditions in §7.11; §8.5 three things kept apart | Repaired |
| Evidence and history Z1/Z2 | Genealogy asymmetric; "first in Anglo-American" | §2.8 two strands, plural traditions, the strand travelled; no national attribution | Repaired |
| Evidence I1 | SIA–BCG wording strengthened | §3.6 and EV13 corrected; C4F6 and propagation cases added | Repaired |
| Evidence I2 | Biology overgeneralized; parochial altruism | §3.7 transitions in individuality; Lemma 3.10; [C] on anticipatory integration | Repaired |
| Evidence I3 | "Ψ is false" undifferentiated; Frank et al. misplaced | §2.6 per tenet; κ condition; Ostrom scope; Frank et al. moved to §3.3; performativity evidence replaced | Repaired |
| Evidence I4 | Opponents' strongest forms | Friedman's remedy, shareholder primacy (Hart and Zingales), Social Darwinism history, realism on future intentions | Repaired |
| Evidence I5 | Status definition; dominance viable; prestige compounds | §2.3 gain; V5 convertibility condition; EV16 | Repaired |
| Evidence I6 | Plural traditions | §2.8; V4 | Repaired |
| Evidence I7 | Missing evidence | EV5 leads, EV13 coupling, EV15 Hirschman and Slobodian; gaps 7–11 | Partly repaired; gaps listed |
| Evidence (E2 quote) | "may adjust our requirements" not in the PDF | EV2 restated with all conditions | Repaired |
| GPT-6 | Centre on the proved mechanism; separate objectives, beliefs and institutions | §2.2–2.3; three objects measured separately (Appendix C) | Adopted |
| GPT-6 | One root out of the chain | One pressure with refutation conditions; Ψ the selected configuration | Raised |
| GPT-6 | Durable regulation with unchanged motives as a counterexample | Registered refutation condition (§2.7, Def 7.12); INPO and Montreal in §9.6 | Adopted |
| GPT-6 | Do not rename successful regulation a pivot | Profiles, not labels (Def 7.12); §10.4 | Adopted |
| GPT-6 | Hazard decomposition, levy incidence, $\Omega_e/\Omega_s$, renege at indifference | Propositions 5.4, 3.5(5), 8.6, 5.10 | Adopted |
| GPT-6 | Compact superiority not established | §8.6 candidate only; §10.1 scope | Adopted |
| GPT-6 | Quality gate before submission | §10.7; submission decided after review | Adopted |
| Ren, 2026-10-03 | Substrate independence; two AI problems; no binary axes; one pressure; three zones too narrow; "one" as system; meta-attractor | §2.8; §6; §8.6; §2; §5; §3.8; Def 2.2 | Adopted |

**Withdrawn**: the list is in THEORY Appendix F.

**Open**: the $U\to d$ production relation; the slow variable for minds; the size of $\kappa$; real-world attractiveness of either meta-attractor; the durability of any arrangement that changes selection.

**The experiment record.** One 20-seed rubric-editing pilot exists. Its first prediction failed; the other three held. Design 2 has not been run. v6 reports the failure (EV12, §10.6).
