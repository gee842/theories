# CF-governance: the evidence and governance findings of the two Codex reviews, tested against the current src

*2026-10-04. Track: evidence, alternatives, governance, activation and withdrawal. Inputs: `REVIEW-v6.2-codex.md` (synthesis item 5; EG1–EG10; the 18-entry primary-source audit; the C0 and normative notes of that report) and the findings of `REVIEW-v6.2-codex-second.md` that bear on §§7–8, §12, the cruxes, the activation and release rules, the evidence and the comparisons (its Findings 5–9, and three boundary rows on pause, dwell and signal release). Both reviews read the snapshot with THEORY SHA-256 f50fb6a1…; every location below is in the **current** `src/` (after the internal verification round, FIXES-v6.2-verify.md), as file:line. No project file was edited.*

*Method. Each finding was located in the current src, its demonstration re-run with a script of my own (standard library only), and judged: **holds** (present now), **partly** (present, but part already repaired or the proposed repair needs correcting), **already-fixed** (the internal round, or the register as it stands, already does what is asked; where), **refuted**, **needs-ren** (a value or wording that is Ren's). For each that holds or partly: the exact repair, every citing place by key or file:line, and the assertion to add.*

*Scripts and logs, in `/private/tmp/claude-501/v62codexfix/governance/`:*
- *`gv_checks.py` → `gv_checks.log`: the proposed block **GV** for `checks_v62.py`, 24 assertions, all pass, 2 s. Sections (a)–(p) are cited below as GV(a) etc.*
- *`cert_time.py`: the time bound of the new {{certificate}}(2) clause, 150 random cases.*
- *`codex_second_rerun.log`: Codex's `counterexamples_v62_codex_second.py` re-run against nothing of the manuscript's code: all assertions pass (numbers quoted below where used).*
- *Sources re-fetched 2026-10-04 through a summarizing fetch tool with quotations requested verbatim (the register's ‡ (page) standard): Fudenberg and Koh, arXiv:2609.28291, abstract and HTML §3.5 (Proposition 4); EO 14365 §§3, 5(a), 5(b) on govinfo; the UK release of 14 February 2025; FRUS 1946 vol. I doc. 448. The OpenAI Preparedness Framework v2 PDF came back as binary and could not be read here (SRC-03).*

*Standing rules applied: roles, not names, in the body; race-camp arguments get no more than they earn (EG3, EG7 add the design's own terminal branches and the full pacing result, and nothing beyond); E2 ≠ E3 kept; judge the game; affirmative meaning untouched; nothing consolidated away; statements own their conditions; no tolerance loosened.*

## Summary

| ID | Priority | Status | Where now (main) | One line |
|---|---|---|---|---|
| EG1 | P1 | holds | core/c0_s12.md:58, :24, :53; reg/TESTS.md:7, :12, :84, :108, :150; supp/11_S11.md:59; disc/08_X8.md:11; disc/11_X11.md:80; core/00_head.md:29 | Release on "falling" residual risk; activation on "not falling" |
| EG2 | P2 | holds | core/80_s8.md:7, :13, :29; core/c0_s12.md:3, :33; core/10_s01.md:27; core/00_head.md:30; disc/08_X8.md:133, :179 | "Admits an irreversible loss" read as "fails the tolerance" |
| EG3 | P2 | holds | core/c0_s12.md:5, :34; disc/08_X8.md:133–175; core/00_head.md:30 | Design gets remedies, continuation gets terminal outcomes |
| EG4 | P2 | partly | core/c0_s12.md:24, :26; reg/TESTS.md:142, :146, :148 | "Commitment leaves only detecting"; T_dec not a conservative bound |
| EG5 | P2 | partly | core/c0_s12.md:11, :15; reg/TESTS.md:44, :56, :60, :65; reg/CLAIMS.md:21, :39; core/00_head.md:27 | "On every reading"; "costs only the preparation" |
| EG6 | P2 | holds (Ren note) | core/c0_s12.md:23–24, :53, :58; reg/TESTS.md:7, :84, :91–93 | No precedence between C1 withdrawal and C5/C7 activation |
| EG7 | P2 | holds | disc/08_X8.md:21–26; core/80_s8.md:58; reg/EVIDENCE.md:198; reg/TESTS.md:210 | Pacing comparison reversed; lag extension missed |
| EG8 | P2 | holds (Ren note) | core/70_s7.md:73; disc/11_X11.md:41; reg/EVIDENCE.md:116; reg/TESTS.md:17 | Benchmark leads read as "no breakout beyond punishment" |
| EG9a | P3 | partly | reg/EVIDENCE.md:78 | EO 14365 §5(a) directs a notice; it does not itself make states ineligible |
| EG9b | P3 | holds | reg/EVIDENCE.md:77 | UK release does not show a narrowed remit |
| EG9c | P3 | holds | disc/11_X11.md:43; reg/TESTS.md:154 | "No dimension is met" vs "none shown to meet" |
| EG9d | P3 | holds | disc/08_X8.md:97 | "No, unless custody follows" ignores the detection route |
| EG9e | P3 | partly | reg/TESTS.md:149 | 2.8× read as a binding cap schedule |
| EG9f | P3 | partly | disc/11_X11.md:69; core/b0_s11.md:95 | "Custody must precede decisiveness" credited to the precedent |
| EG10 | P2 | holds | disc/10_X10.md:14, :34; reg/CLAIMS.md:285 | Hash commitment ≠ held-out secrecy |
| SRC-01…18 | P3 | 12 already-fixed, 6 routed or holds | see §Source audit | Register against the primary sources |
| EG-C0 | P3 | holds | reg/TESTS.md:11, :124; core/70_s7.md:99 | Disclosure duty is not a one-signature control |
| EG-N1 | — | needs-ren | core/80_s8.md:13 | Boundary of O1 against benefits forgone |
| EG-N2 | — | already-fixed | disc/10_X10.md:42 | Provider voice without vote: a stated trade-off |
| S2-5 | High | holds | core/60_s6.md:91; core/40_s4.md:85–87; supp/04_S4.md:86; core/c0_s12.md:25, :31; core/b0_s11.md:50; disc/10_X10.md:9 | Row-sum certificate is eventual, not present-tense |
| S2-6 | Medium | partly | core/c0_s12.md:20, :66; core/60_s6.md:101; reg/TESTS.md:20, :74, :95; disc/08_X8.md:7 | Withdrawal at a measured zero tax |
| S2-7 | Medium | partly | core/70_s7.md:15–27 | Table 7.1 rows lose premises |
| S2-8 | Medium | holds | supp/11_S11.md:69, :71; core/b0_s11.md:50 | SPRT termination needs iid or divergent information |
| S2-9a | Medium | partly | = EG5 | Tier 1(a) |
| S2-9b | Medium | holds | core/c0_s12.md:18; reg/TESTS.md:69 | Withdrawal rule lacks the remedy-fails escape |
| S2-9c | Medium | partly | = EG4 | Tier 2 is a specification, not proof of execution |
| S2-9d | Medium | holds | core/c0_s12.md:34; disc/08_X8.md:145, :155, :162, :169 | Lockin, converted correctors, standby: unequal reversal tests |
| S2-9e | Medium | holds | = EG2 | §8.1 needs the bound, not an outcome's existence |
| S2-B1 | boundary | holds | supp/11_S11.md:45, :47; core/b0_s11.md:48; core/50_s5.md:74 | Summable post-pause hazards need h<1 and survival to the change |
| S2-B2 | boundary | holds | supp/11_S11.md:79, :82, :99; core/c0_s12.md:27 | Dwell is an infimum; release needs a margin |
| S2-B3 | boundary | holds | core/b0_s11.md:27 | Receiver must randomize at equality |

Second-review items left to the other tracks: Findings 1–4 (formal: balanced-path Jacobian, responsive-rival derivative, detection clock, cumulative selection), the strict-narrowing endpoint, core pruning at gain one, the serial oversight formula. SA-02's threshold-wide guarantee is the systems track's; S2-8 below touches the same remark and says where the two repairs meet.

---

## EG1 (P1; keys: coverage, nonsum, racehazard; cruxes C1, C3a, C12) — holds

**Claim.** The C1 rule withdraws E3 and the case for E2 when residual risk is "falling"; the theorem turns on summability, and a decision on a finite horizon turns on cumulative risk. Trend, finite-horizon acceptability and the tail are three propositions.

**Current text (unchanged by the internal round).** core/c0_s12.md:58 (C1 row: "Residual risk per class falling under present incentives: E3 and the case for E2 lapse for that class, with their triggers"); core/c0_s12.md:24 (E3 trigger: "residual risk not falling (C1)"); core/c0_s12.md:53; reg/TESTS.md:7, :12 (third column), :84, :108 ("and residual risk falls"), :150 ("Residual risk not falling (C1)"); supp/11_S11.md:59 (Q1: "Has the residual hazard of the relevant classes fallen"); disc/08_X8.md:11 ("residual risk per hazard class falling over generations (C1)"); disc/11_X11.md:80 ("its hazards fell with learning (Nye 1987), the case in which residual risk becomes summable"); core/00_head.md:29 ("残余风险不降").

**Test (GV(a)).**
- (a1) Codex's case inside the theorem's premises: $U_t/Y_t=1/(t+2)$, $h=0.02$, $q_t=0.02+0.01/(t+1)$. $q_t$ strictly falls, meets (coverage lags) and $q_t\ge h(1-U_t/Y_t)$ on $10^5$ periods; survival 0.793, 0.1258, $1.559\times10^{-9}$ at 10, 100, 1000 periods.
- (a2) $q_t=1/(2(t+1))$ falls to zero; survival 0.0563, 0.00564, 0.000564 at $10^2,10^4,10^6$: $\propto N^{-1/2}$.
- (a3) A constant $10^{-5}$ a month: cumulative risk $6.00\times10^{-4}$ at five years and $5.98\times10^{-3}$ at fifty, under tolerances of $10^{-3}$ and $10^{-2}$, though not summable. "Not falling" would activate E3 on it.
- (a4) The same 24 declining observations continue as $0.01/(t+1)$ (survival to $10^6$ 0.8659, tending to zero) or $0.01/(t+1)^2$ (0.9625, bounded): a finite record does not identify the tail.
- (a5) The cumulative test passes the falling, summable $2\times10^{-4}\cdot0.97^t$ (B = 0.0056, 0.0066, 0.0066 at 60, 240, 600 months against 0.01, 0.02, 0.03) and fails the falling series of (a1) at five years (above 0.7).

**Repair.**
1. *A definition of a favourable C1*, inserted in THEORY §12.3 after the sentence "C1 is the central crux…" (core/c0_s12.md:53) and mirrored in TESTS §1 under the table: "C1 is measured favourable for a hazard class when (H) an upper bound on the cumulative probability of O1 or O2 arising from that class, over each protected horizon of Section 8.1 and at the deployment scale planned, estimated by evaluators certified independent with its confidence and model uncertainty stated, lies below the tolerance registered for that horizon; and, wherever the long-run results of Section 5.3 are invoked, (T) a bound $h_t\le\bar h_t<1$ with $\sum_t\bar h_t<\infty$ is justified by a named mechanism, since a finite record of falling estimates does not establish a tail ({{nonsum}}). A falling trend is evidence that the case for slowing weakens; by itself it withdraws nothing [def; thm]."
2. core/c0_s12.md:53: "C1 is the central crux: on it turn E3 and the hazard ground of E2 (Section 5.3); E2's strategic ground turns on C5 and C7 (EG6)." Same at reg/TESTS.md:7.
3. core/c0_s12.md:58, C1 row, third column: "The bound (H) below its tolerance at every protected horizon, with any tail claim (T) justified separately: E3 lapses for that class with its trigger, and so does E2's hazard ground for it; E2's strategic ground stands on C5 and C7". Same at reg/TESTS.md:12 (third column).
4. core/c0_s12.md:24, E3 trigger: "E3 activates for a hazard class whose coverage falls behind: the bound (H) of C1 above its tolerance at some protected horizon, or catch rates of planted defects (C3a) or, for masked classes, independent auditors' detection (C12) falling as capability rises." *Ren:* whether a class for which no bound can yet be estimated activates E3 (the burden of proof of tier 1(b) applied to tier 2) is a value choice; the text above does not activate on an absent estimate, as the present text does not either.
5. reg/TESTS.md:84: "| C1 favourable for a hazard class, (H) and, where invoked, (T) | E3 and E2's hazard ground lapse for that class, with their triggers | Tier 1; E2's strategic ground (C5, C7); measurement of the class continues, and a bound later above its tolerance re-activates E3 |".
6. reg/TESTS.md:108: "…keeps pace with hazardous variety under present incentives, and the bound on cumulative residual risk per class falls below the registered tolerance at every protected horizon."
7. reg/TESTS.md:150, first two cells: "| E3, per hazard class | The bound (H) of C1 above its tolerance at a protected horizon; catch rates of planted defects at fixed human hours falling as capability rises (C3a); for masked classes, independent auditors' detection falling (C12) |".
8. supp/11_S11.md:59, Q1 question: "Is the upper bound on the cumulative residual risk of the relevant classes, over each protected horizon and at the deployment scale to be resumed, below its registered tolerance, by evidence independent of the developer and valid against evaluation awareness?"
9. disc/08_X8.md:11: "…the bound on cumulative residual risk per hazard class below the registered tolerance at every protected horizon, and falling over generations (C1)."
10. disc/11_X11.md:80: "…and its hazards fell with learning (Nye 1987), a record consistent with the case in which residual risk becomes summable; a finite record of survival and of falling estimates does not establish an infinite sum."
11. core/00_head.md:29 (for Ren's ear): "（按危险类别：某一受保护期限上累积残余风险的上界超过登记的容忍线，或植入缺陷的检出率随能力上升而下降）".
12. reg/CHANGELOG.md: record the change without quoting the withdrawn phrases verbatim (they become banned phrases).

**Check to add.** Block GV(a), assertions (a1)–(a5′) with the numbers above (strict fall on $10^5$ periods; survival $<10^{-8}$ at 1000; $N^{-1/2}$ ratio within 1%; $6.00\times10^{-4}$ and $5.98\times10^{-3}$; 0.8659 and 0.9625; B(60) > 0.01 for (a1)). Add to `BANNED` in src/assemble_v62.py: `r'falling under present incentives'`, `r'[Rr]esidual risk not falling'`, `r'残余风险不降'`.

## EG2 (P2; key: kernel; standard of Section 8.1) — holds

**Claim.** The standard compares upper bounds on the probability of O1/O2 at common horizons against a tolerance; the text concludes that every path fails it because every path's range admits an irreversible loss. Existence of an outcome is not a bound above tolerance. The manuscript's admission that estimates are missing is credited; the defect is the unconditional preceding sentence.

**Current text.** core/80_s8.md:7 ("where every worst case crosses the tolerance, as each does under the rule for that range"); :29 ("both include an irreversible loss, so the standard does not by itself rank them"); core/c0_s12.md:3 (same as :7); :33 ("every path's worst case includes an irreversible loss, so none meets the tolerance"); core/10_s01.md:27 ("where every worst case crosses the tolerance"); core/00_head.md:30 ("各路径的最坏情形都越过容忍线"); disc/08_X8.md:133 ("compares paths whose worst cases all exceed the tolerance"), :179 ("Both fail the tolerance in their worst case").

**Test (GV(b)).** Two paths, both admitting O1 in their range; five-year bounds 0.001 and 0.5; tolerance 0.01: one meets it.

**Repair.**
1. core/80_s8.md:13, after "Third, if no path meets the tolerance, prefer the one with the lowest bound that keeps options open.": "Write $B_j(H)=\sup_{\theta\in\Theta}\Pr_{j,\theta}(\text{O1 or O2 by }H)$; a path meets the tolerance when $B_j(H)$ is below it at every common horizon. Where the bounds have not been estimated, no path is shown to meet it, and a ranking is a judgment on stated reasons [val], which the bounds, once estimated, override." (*Ren:* the last clause makes the reasons of §12.1 a tie-break subordinate to the bounds; that is how §12.1 already uses them, but it is an addition to the standard's text.)
2. core/80_s8.md:7 and core/c0_s12.md:3: "where no path has been shown to meet the tolerance, as none yet has, the ranking is a judgment made at the standard's third step without the bounds that step needs [val]".
3. core/80_s8.md:29: "Under the rule for $\Theta$ the ranges of continuation with strong correction and of a design that changes selection both admit an irreversible loss, and neither path's bound has been estimated, so the standard does not yet rank them: neither is shown to meet the tolerance, the comparison falls to its third step, which needs the bounds, and Section 12.1 states the ranking there as a judgment, over the failure modes of every path that X8 lists."
4. core/c0_s12.md:33, first sentence: "Under the rule for $\Theta$ every path's range admits an irreversible loss, and no path's bound on the probability of O1 or O2 at the common horizons has been estimated: the register bounds neither the residual floor on continuation nor the hazard of custody's capture on the design, so no path has been shown to meet the tolerance, and the ranking falls to the standard's third step, the lowest bound that keeps options of correction open (Section 8.1)." The rest of the paragraph stands.
5. core/10_s01.md:27: "where no path has been shown to meet the tolerance, the ranking is a judgment". core/00_head.md:30: "没有哪条路径已被表明守得住容忍线，排序是明说的判断" (Ren's ear).
6. disc/08_X8.md:133: "The third step of the protection standard compares paths none of which has been shown to meet the tolerance…"; :179: "Neither has been shown to meet the tolerance, and neither path's bound is estimated, and the comparison moves to the standard's third step, which needs estimates on both sides."
7. Optional, not demanded: one transparent illustrative $\Theta$ with a tolerance, kept apart from any estimate.

**Check to add.** GV(b) (bounds 0.001 ≤ 0.01 < 0.5 with both ranges admitting O1). BANNED: `r'none meets the tolerance'`, `r'as each does under the rule'`, `r'Both fail the tolerance'`, `r'every worst case crosses'`, `r'最坏情形都越过容忍线'`.

## EG3 (P2; keys: kernel, coverage, slowroute, masked, lockin, influence, wingives) — holds

**Claim.** The failure-mode comparison gives continuation its terminal branches and the design its remedies. A captured registry, a standby that fails before a loss, a masked system that outruns oversight are the same late-detection branches; "every other design failure has a reversal" uses a timing asymmetry.

**Current text.** The internal round (coldread M6) made the asymmetry conditional ("if they occur", "none yet shown to work"); the structure is unchanged: core/c0_s12.md:34 lists the design's five reversals and continuation's four irreversible modes; :5; disc/08_X8.md:133 (definition of reversible has no timing), :167–173 (no design row for coverage outgrown, capture or masked admission before evidence, covert internal deployment), :169 (standby "Reversible"), :175; core/00_head.md:30. §5.3 (core/50_s5.md:88) itself says the growth channel binds a world that has stopped racing.

**Test (GV(c)).** Fault 0.1, detection before the boundary 0.5: a continuation remedy timely with probability 0.6 gives loss 0.070; a design branch "reversible by recertification" that executes after the boundary gives 0.100; with matched timeliness both are 0.070. A named reversal changes the loss probability only through its timeliness.

**Repair.**
1. disc/08_X8.md:133, definition: "A mode is *reversible* only if its reversal is named, is executed by someone other than the failing party, and completes before O1 or O2; where a loss can come first, the row says so, on every path alike."
2. New design rows after disc/08_X8.md:167:
   - "| | Hazardous variety outgrows contestable coverage under its pace (E3 mis-set, evaded or outrun), and a floor is crossed | Irreversible once a loss of O1 or O2 occurs; before that, by tightening E3 or E2 | [thm∣prem] {{coverage}}; [doc] X10 | Bounds on cumulative residual risk per class; catch rates of planted defects at fixed human hours (C1, C3a) |"
   - "| | Capture of a function, or admission of a masked system, before evidence | Irreversible where a protected loss comes before recertification or recall; otherwise reversible by them | [thm∣prem] {{slowroute}}, {{masked}}; [doc] X10 | Release-to-evaluation time against harm-to-detection time; auditors' detection at fixed access (C12) |"
   - "| | Covert internal deployment beyond the compact's admission | Irreversible if it becomes decisive or reaches its own selectors | [thm] {{verify}}(3); [thm∣prem] {{masked}}; [—] | Compute accounting against algorithmic diffusion; detection latency (C7; EV9) |"
3. disc/08_X8.md:169: "| | Interruption of an essential service | Reversible where the share cap, escrowed systems and funded standby carry the service before harm accrues; harm done during the interruption is not reversed | [doc] X10; [—] no base rate | Standby and escrow drills, timed against the harm window (D6) |".
4. The symmetric changes on the other paths are S2-9d (converted correctors, delegation).
5. disc/08_X8.md:175, the sentences from "The design's other failures…" to "…no floor has been crossed.": "On every path, the design's included, a fault detected or remedied too late ends in a protected loss. More of the design's faults have a named reversal that can complete before one, the escalation of its coercive fallback apart, and none of those reversals has yet been shown to work; continuation's reversals act only while no position is decisive and no floor has been crossed."
6. core/c0_s12.md:34, reason (i), replaced whole:
   "- **(i) Reversibility, on matched branches.** A failure is reversible only if its reversal is named, is executed by someone other than the failing party, and completes before O1 or O2, so every fault on every path has two branches, a reversal in time and a loss first, and X8 lists both. On both paths a fault caught too late ends in a protected loss: on continuation, coverage outgrown and a floor crossed ({{coverage}}), capture before evidence ({{slowroute}}), a decisive position reached ({{wingives}}), and the capacity to overrule lost where the contest denies its recovery ({{lockin}}) [thm∣prem]; on the design, the same growth hazard where its pace is mis-set or evaded, capture of a function or admission of a masked system before evidence, and an interruption that standby does not cover in time (X8) [thm∣prem; doc]. What differs is how many faults have a named reversal, executed by another party, that can complete in time: the design provides one for dissolution, capture of one function, interruption, collusion among its checks and overreach of a common constraint, none yet shown to work (C4) [conj]; continuation's reversals act only while no position is decisive and no floor has been crossed, and for hazards that manifest late its premises cannot be measured before they bind ({{tempo}}). The design's exceptions are the escalation of its coercive fallback, which every coercive path carries, and the failure of (ii). The asymmetry is therefore in the chance that a fault reaches a protected loss before a reversal completes, which the design is built to lower and has not shown that it lowers; that is C4, and the ranking's reliance on the design's bounded own risk is C4 (Section 8.1). Keeping options of correction open is staying in the correctable kernel ({{kernel}}): a state from which a named reversal, if it works against every error in $\Theta$, still avoids the protected losses lies inside it, and a failure without one has left it [def]."
7. core/c0_s12.md:5 (Why), last sentence: "…a design built to Section 10 contests it, and more of that design's faults have named reversals that could complete before a protected loss, its coercive fallback's escalation apart, none yet shown to work, while on both paths a fault caught too late ends in one [thm∣prem; val]."
8. core/00_head.md:30 (Ren's ear): "两边的失效若发现或补救太晚都会造成不可逆损失；设计让更多失效有可在损失之前完成的退路，均未经验证；现状最坏的失效没有退路".
9. reg/CLAIMS.md:237: append "; reversal tested on matched branches, timely or late, on every path (Codex V6.2 EG3)".

**Check to add.** GV(c) (0.070, 0.100, 0.070). In xref_v62.py, a parity check on the assembled DISCUSSION.md: the "A design changing selection" block of the failure-mode table contains rows matching `outgrows contestable coverage`, `before evidence` and `Covert internal deployment`, and no "Reversible" cell in any block lacks one of `before|while|where|once` (the timing qualifier).

## EG4 (P2; keys: tdec, detectlink, enforce, restraint, tempo, scissors) — partly

**Claim.** A registered trigger is not a commitment technology; precommitment removes a decision step, not detection, communication, execution and failed actuation; prepared, installed and in force are mixed; the $T_{\rm dec}$ indicator is a constant-factor extrapolation, not a conservative bound.

**Already fixed** (coldread M2, core/c0_s12.md:26): commitment binds only where its means are in force before the trigger (dormant hardware limits or escrowed keys held by custody, {{restraint}}(a); a sanction that survives success, {{restraint}}(b)); otherwise activation against the leading party falls to tier 3; installing dormant means is prepared now under D4 and D5; C4 and C7 register whether the means are in force (core/c0_s12.md:62; reg/TESTS.md:16, :19). The detection probability $\upsilon$ in {{detectlink}} already means "detected and answered".

**Still present.** core/c0_s12.md:26, last sentence: "preparation shortens the delay of the response from building, deciding and detecting to deciding and detecting, and commitment leaves only detecting"; core/c0_s12.md:24 and reg/TESTS.md:142 ("less the time custody needs to be installed and verified": installation of what is already in force is zero, execution is absent); reg/TESTS.md:146 ($T_{\rm dec}$ from a constant factor and the public gap); reg/TESTS.md:148 (no failed actuation).

**Test (GV(d)).** $T_{\rm dec}=10$, detection hazard 0.25 a period: detection alone gives $p_d=0.056$; with two periods of execution and 10% failed actuation $p_d=0.190$. $T_{\rm dec}$ extrapolated from a 1% public gap at factor 1.05 to a 50% decisive gap is 80.2 periods; with the internal gap three times the public one, 57.7; with the factor rising 2% of its excess each period, 54. Remark S2.1's own numbers show where the linearization is conservative (saturation: 11.6 against 13; diffusion: 80 against never), so the repair names the non-conservative directions only.

**Repair.**
1. core/c0_s12.md:26, the last sentence replaced: "With its means in force, preparation removes building from the delay of the response, and commitment removes a fresh discretionary decision; what remains is detecting, classifying, communicating and executing until the restraint binds, with a chance that execution fails or is refused. That remaining delay, with its chance of failure, is the delay {{tempo}} bounds when the mode to be held is a lead that compounds, and it enters $p_d=1-\upsilon(T_{\rm dec})$ with $\upsilon$ the probability that the restraint binds within $T_{\rm dec}$ ({{detectlink}}) [thm∣prem]. Whether a committed mechanism executes against the strongest participant is C4 (D5), not shown."
2. core/c0_s12.md:24 and reg/TESTS.md:142, the trigger: "A trigger fires when a conservative estimate of the time to a decisive position, less the time the response needs to bind (installing and verifying whatever of custody's means is not yet in force, then detecting, executing and making the restraint binding), falls below a margin registered in advance".
3. reg/TESTS.md:146, second column, append: "For activation it is used at a conservative lower bound over $\Theta$: the internal gap at its upper bound, since internal deployment and masking hide it; the equilibrium rather than the structural factor where rivals respond ({{eqgain}}); the factor's rise with the stakes and the won share ({{scissors}}); and the lower end of the decisive gap's interval. The linearization is itself conservative where the contest saturates or diffusion holds the gap short ({{tdec}}), not in these directions."
4. reg/TESTS.md:148, third column, append: "execution latency and the rate of failed or refused actuation, from drills against a deliberately non-compliant strongest participant with an injected correlated error (Study 3)".
5. reg/TESTS.md:147 (time to install and verify custody), second column: "The lead time of whatever of custody's means is not in force before the trigger (tier 1(a), item 4), separately from the means already installed and dormant".

**Check to add.** GV(d): $p_d$ 0.0563 → 0.1901 (assert more than three times); $T_{\rm dec}$ 80.2, 57.7, 54 (assert both below 0.75 × 80.2). BANNED: `r'commitment leaves only detecting'`.

## EG5 = S2-9a (P2 / Medium; keys: delegatelock, durability; tiers) — partly

**Claim.** Tier 1(a)'s "on every reading of the cruxes" exceeds an option-value argument; durable powers and a binding activation commitment to a design still under C4 do not belong there; "costs only the preparation" and "forgoes nothing" omit the cost; the empirical, not the normative, cruxes can be meant.

**Already fixed** (coldread M3): the activation commitment moved to tier 2, conditional on custody passing D1–D8 (core/c0_s12.md:15, :26; reg/TESTS.md:46, :65); dormant means installed only if they pass D4 and D5.

**Still present.** core/c0_s12.md:11 ("Warranted now, on every reading of the cruxes"; "preparation whose lead time exceeds any warning"); :15 ("If decisive advantage never arrives, this costs only the preparation"); reg/TESTS.md:44 (L: "takes longer than any warning a crux could give"), :56 ("the preparation is the whole cost"), :60 ("preparation forgoes nothing"), :65 ("The cruxes change what each item contains, not whether it is warranted"); reg/CLAIMS.md:21, :39; core/00_head.md:27 ("任何读法下都成立"). TESTS:65 itself concedes that N2 bears on item 5, so "every reading of the cruxes" is literally false of the normative cruxes.

**Test.** Logical; no numeric demonstration needed. Item 5's equilibrium holds only among actors who price in the lock ({{delegatelock}}(1)), which N2 can deny.

**Repair.**
1. core/c0_s12.md:11: "**Tier 1(a). Warranted now, on every reading of the empirical cruxes, within the values of Section 1 and a budget registered in advance [rec].** A step belongs here only if its justification does not depend on how any empirical crux comes out: measurement that decides the cruxes, preparation whose lead time can exceed the warning the indicators of tier 2 can be relied on to give, so that it has option value, an equilibrium without trust among actors who price in the lock (N2), or research that is a public good. Each is registered with a budget, its exit conditions and the other uses of its resources; none creates powers or binds an activation, which are tier 2's. TESTS sets each item against every crux."
2. core/c0_s12.md:15, the sentence "If decisive advantage never arrives, this costs only the preparation; …": "If decisive advantage never arrives, this costs the preparation, its registered budget and the other uses of those resources, and it has created no powers; if it arrives, custody begun at a warning comes too late wherever building it takes longer than the warning gives (Section 7.2) [thm∣prem]."
3. reg/TESTS.md:44, L: "**L**, lead time: what the item builds can take longer than the warning the indicators of §6.1 can be relied on to give, so that preparing it has option value at its registered budget." Same sentence opening: "…only if its justification does not depend on how any empirical crux comes out…".
4. reg/TESTS.md:56, col (4): "L: favourable, activation lapses, the preparation spent within its budget is the cost, and preparation is scaled to what the remaining readings justify; unfavourable, custody begun at a warning comes late (THEORY §7.2)".
5. reg/TESTS.md:60, col (4): "L: preparation forgoes no benefit of capability; it costs its budget and the other uses of it; C10 bears on E2's activation and on the ranking of tier 3".
6. reg/TESTS.md:65, second sentence: "The empirical cruxes change what each item contains and how much of it is warranted, not whether some of it is:".
7. reg/CLAIMS.md:21 ("on every reading of the cruxes") and :39 ("1(a), on every reading of the cruxes"): "on every reading of the empirical cruxes, within a registered budget".
8. core/00_head.md:27 (Ren's ear): "**第一层（甲），关键经验分歧的任何读法下都成立（在本文的价值与登记的预算之内）：**".

**Check to add.** BANNED after the change: `r'on every reading of the cruxes'`, `r'forgoes nothing'`, `r'costs only the preparation'`, `r'exceeds any warning'`.

## EG6 (P2; keys: coverage, detectlink, enforce; cruxes C1, C4, C5, C7) — holds, with a note for Ren

**Claim.** E2 has two grounds, hazard outrunning correction and a decisive position defeating enforcement. Tier 2 activates E2 on the C5/C7 trigger; the C1 row withdraws "E3 and the case for E2 … with their triggers". No precedence rule.

**Current text.** core/c0_s12.md:23–24 (trigger activates custody and E2 on time to decisive position); :53 and :58 (C1 withdraws E3 and E2 with triggers); :63 (C5); :77; reg/TESTS.md:7, :84, :91, :92, :93.

**Test (GV(l)).** Over the 16 cells of (C1 favourable, C5 decisive, C7 timely, C4 custody passes), the current rules both activate and withdraw E2 in 4 cells, every one with C1 favourable and a decisive class; with E2's two grounds separated and OR-combined, none.

**Repair.**
1. core/c0_s12.md:23, after "Stopping is not slowing, and each is activated on its own indicators (Section 11.3);": "E2 has two grounds, each with its own trigger and its own withdrawal: a hazard ground, rollback where hazardous variety in the decisive class already exceeds coverage, which C1 activates and withdraws; and a strategic ground, that a decisive position would defeat enforcement, which C5 and C7 activate and withdraw. E2 is in force where either ground is (TESTS §3.4)."
2. core/c0_s12.md:24, "and custody and E2 activate" → "and E2 on its strategic ground activates, held by custody where detection is not timely (C7) and custody has passed its stress tests (C4)".
3. core/c0_s12.md:53, :58 and reg/TESTS.md:7, :12, :84: as EG1 items 2, 3, 5 ("E3 and E2's hazard ground").
4. core/c0_s12.md:63 and reg/TESTS.md:91, third column: "activation of custody and of E2's strategic ground lapses; E2's hazard ground stays with C1; preparation stays".
5. New reg/TESTS.md §3.4 "How the triggers combine", after §3.3:

| C1 for the class | C5 | C7 | C4 for custody | E3 | E2, hazard ground | E2, strategic ground | What holds the strategic ground |
|---|---|---|---|---|---|---|---|
| unfavourable | any | any | any | in force | in force where hazardous variety exceeds coverage, with rollback | as the next columns | — |
| favourable | any | any | any | lapses | lapses | as the next columns | — |
| any | favourable | any | any | — | — | lapses | preparation stays |
| any | unfavourable | favourable | any | — | — | in force | a verified agreement with timely detection; custody not required |
| any | unfavourable | unfavourable | favourable | — | — | in force | custody, activated by the committed mechanism |
| any | unfavourable | unfavourable | unfavourable | — | — | in force | no design passes; the comparison of tier 3, the coercive candidate under its three conditions, the hard case |

"E2 is in force where either of its grounds is. Each favourable crux withdraws only the ground it bears."
6. *Ren.* CLAIMS §9 item 10 is open: whether E2 and E3 are put in force by the failure of broad E1 (his condition), by the forecast trigger, or both. The table defines what each favourable crux withdraws under any of the three; under (a) or (c) a column "broad E1 achieved" is added, and whether a favourable C1 may ever erase E2's strategic ground is his to say (the table says it may not).

**Check to add.** GV(l): current 4 conflicting cells of 16, all with C1 favourable and C5 decisive; proposed 0.

## EG7 (P2; keys: twochan, standprice, slowroute, enforce, masking, masked) — holds

**Claim.** X8's pacing comparison reverses one inference (an understated hazard puts participants in the racing region, not the pacing one), treats "effective hazard" as the hazard an actor counts and sees, and contrasts with internal deployment although the full paper models a monitoring lag.

**Current text.** disc/08_X8.md:21 ("from the abstract only (EV11)"); :22 ("*The effective hazard* is the part of a hazard that the objective an actor acts on counts, and that it sees … a path can lie in the racing region of the real parameters while its participants compute the pacing region"); :23 (internal deployment as a failure of transparency); :26 ("should be checked against the full paper"); core/80_s8.md:58 (the conditions of winning erode "the hazard through relative accounting"); reg/EVIDENCE.md:198 (‡ (abstract), *checked 2026-10-03*); reg/TESTS.md:210.

**Test.** GV(p): pacing iff effective hazard ≥ 1; real 1.4, seen 0.84 → real parameters in the pacing region, participants in the racing region. Source, re-fetched 2026-10-04: the abstract itself says "If internal capabilities are hidden with a fixed lag until deployment, it is harder to sustain pacing which highlights the importance of transparency about internal capabilities" (so the register's abstract reading already missed it); §3.5 "Monitoring lags: internal vs deployed models", Proposition 4: for every lag, joint racing is an equilibrium outcome; (a) if $\lambda^{\rm eff}<(1-g)(\alpha-\beta)$ no pure equilibrium sustains pacing; (b) intermediate, pacing iff $L\le L^\ast$; (c) if $\lambda^{\rm eff}\ge(1-g)\alpha$, joint pacing is an equilibrium outcome for every $L>0$. In the lag model the hazard depends only on **deployed** capability ($\lambda_t=\lambda(A_{t-L}-X_t)$), the lag is exogenous, and the only absorbing event is the common disaster, which "permanently ends both firms' future profits"; $\lambda^{\rm eff}$ is defined from the racing payoff at the safety boundary, a payoff-equivalent quantity.

**Repair.**
1. disc/08_X8.md:21: "As the register now reads it, from the paper's text (EV11), Fudenberg and Koh (2026) study … with no agreement among the developers; they also give the case in which internal capability is hidden for a fixed lag until deployment."
2. disc/08_X8.md:22: "- *The effective hazard* is, in their model, a payoff-equivalent quantity built from the common disaster hazard, which ends both firms' profits, and from the racing payoff at the safety boundary [obs: EV11]. This paper's reading, a conjecture with no translation between their payoff function and the objectives of Section 3 supplied, is that what an actor's objective counts and what it sees enter there: relative accounting weighs a shared hazard by $1+\theta$ and drops it at $\theta=-1$ ({{twochan}}), compounding narrows the working objective as the discounted gain rises ({{standprice}}), and where harm manifests late or is masked the hazard seen is below the real one ({{slowroute}}). A path can then lie in the pacing region of the real parameters while its participants, seeing less of the hazard, compute and act in the racing region [conj]."
3. disc/08_X8.md:23: "- *Transparency.* Their model already contains internal capability hidden for a fixed lag: the lag makes pacing harder to sustain, and pacing remains an equilibrium at every lag where the effective hazard is high enough (their Proposition 4(c)) [obs: EV11], so monitoring delay alone does not refute pacing. What the model leaves out is where Part I bears: a hazard that arises from capability before it is deployed, since in their lag model only deployed capability carries risk (internal deployment, EV6); a lag that is not fixed but lengthened by quiet deviation, captured evaluation and masking ({{enforce}}, {{masking}}, {{masked}}); and the open–closed gap (EV5)."
4. disc/08_X8.md:24, first sentence: "Their only absorbing event is the common disaster; where outrunning the frontier can yield a decisive position, the prize ends the game and the enforcement condition, not the hazard, decides ({{enforce}})."
5. disc/08_X8.md:26, last sentence: delete "The correspondence should be checked against the full paper in outside review." and put "The translation of their effective hazard into this paper's objectives is heuristic and needs outside review."
6. core/80_s8.md:58, *What remains*, the clause from "and the conditions of winning erode…": "and, by this paper's conjecture, the conditions of winning erode both conditions of pacing, which G1 and G6 secure: the hazard an actor acts on through relative accounting ({{twochan}}) [conj], transparency through quiet deviation, captured evaluation and masking ({{enforce}}, {{masking}}, {{masked}}); their model's own monitoring lag leaves pacing an equilibrium at every lag where the effective hazard is high enough, and what it does not cover is hazard before deployment, a lag that masking lengthens, and a deviation that becomes decisive (X8)."
7. reg/EVIDENCE.md:198, replaced: "Fudenberg and Koh, "Cooperating against Catastrophe", arXiv:2609.28291, 23 September 2026. Two firms race against a linearly advancing safety threshold; when the frontier exceeds it, a common disaster arrives at a hazard increasing in the gap and ends both firms' profits. Markov perfect equilibria: racing only, coexistence, pacing only as risk, the safety rate and flow payoffs rise; across subgame perfect equilibria high risk rules out perpetual racing. The effective hazard $\lambda^{\rm eff}$ is defined from the racing payoff at the safety boundary. §3.5, with internal capability observed by the rival only after a fixed lag $L$ and only deployed capability carrying risk: joint racing is an equilibrium outcome at every lag, and joint pacing is one at every lag where $\lambda^{\rm eff}\ge(1-g)\alpha$ (Proposition 4(c)), only up to a finite lag in an intermediate range, and at no lag below $(1-g)(\alpha-\beta)$. The only absorbing event is the disaster. ‡ (page), the HTML text, quotations requested verbatim, *checked 2026-10-04* ([arXiv](https://arxiv.org/html/2609.28291v1)). The V6.2 build read the abstract only and missed its sentence on hidden internal capability. THEORY §8.3(b) asks whether its conditions hold on the present path; the mapping of its effective hazard onto this paper's objectives is this register's interpretation."
8. reg/TESTS.md:210: delete "the correspondence with Fudenberg and Koh (2026) is read from its abstract and needs the full paper;" and put "the translation of Fudenberg and Koh's effective hazard into this paper's objectives (X8) is heuristic;".

**Check to add.** GV(p). BANNED: `r'racing region of the real parameters while'`.

## EG8 (P2; keys: tdec, enforce, branches) — holds; one clause is Ren's

**Claim.** Short public benchmark leads become "no breakout has yet put anyone beyond punishment". Public lag measures neither the existence nor the absence of a position beyond sanction.

**Current text.** core/70_s7.md:73 ("They support enforcement: no breakout has yet put anyone beyond punishment, so enforced cooperation remains available and common custody is a preparation, not an emergency"); disc/11_X11.md:41 (Q7: "leads short on every measure, so the window is open"); reg/EVIDENCE.md:116 ("That tells against (decisive) at present."); reg/TESTS.md:17 (next measurement).

**Test.** Source: METR's page warns its series is unreliable above 16 hours on its suite; Epoch's ECI gap is a public-model average (EV5 as registered). Neither observes internal capability, convertibility into control, or balancing time. GV(d) shows how a masked internal gap shortens $T_{\rm dec}$ (80.2 → 57.7).

**Repair.**
1. core/70_s7.md:73, from "Short leads cut both ways." to "…not an emergency.": "Short leads cut both ways. On public measures they give no sign that a breakout has put anyone beyond punishment, and they are consistent with a window in which enforced cooperation remains available; public lags do not measure internal capability, the conversion of a lead into strategic control or the time others need to balance it, so they bound neither the window nor the absence of a position beyond sanction (EV5; C5, C7) [obs]. On this evidence common custody is a preparation, not yet an emergency." *Ren:* the clause "a preparation, not an emergency" waits on CLAIMS §9 item 10 (FIXES §三 item 1); the repair above changes only the inference before it and adds "yet".
2. disc/11_X11.md:41, Q7: "No custody; hardware verification of compute proposed and prototyped, not deployed; leads short on every public measure, consistent with an open window whose size these data do not bound".
3. reg/EVIDENCE.md:116: append "Benchmark and index lags do not observe internal capability, the conversion of a lead into strategic control, or the time balancing needs; they give no affirmative sign of decisive advantage and do not establish its absence."
4. reg/TESTS.md:17, fourth column, append: "convertibility of a lead into strategic control (compute, deployment permissions, complementary assets) and the time others need to balance it, kept apart from benchmark lead duration".

**Check to add.** BANNED: `r'no breakout has yet put anyone beyond punishment'`.

## EG9 — narrow corrections (P3)

### EG9a (EO 14365 §5(a); SRC-12) — partly
*Already fixed* (evidence E15(c)): "non-deployment funds" and §5(b) are now right (reg/EVIDENCE.md:78). *Still present:* "§5(a) makes states with AI laws it calls onerous ineligible". Source re-fetched: §5(a) directs the Secretary of Commerce, within 90 days, to issue a Policy Notice on eligibility for remaining BEAD funding, and "That Policy Notice must provide that States with onerous AI laws identified pursuant to section 4 of this order are ineligible for non-deployment funds, to the maximum extent allowed by Federal law." **Repair** (reg/EVIDENCE.md:78): "§5(a) directs the Secretary of Commerce to issue within 90 days a Policy Notice on States' eligibility for the BEAD program's remaining funding, which "must provide that States with onerous AI laws identified pursuant to section 4 … are ineligible for non-deployment funds, to the maximum extent allowed by Federal law"; whether the notice issued and funds were withheld is not recorded here." **Check:** none (register).

### EG9b (UK remit; SRC-11) — holds
reg/EVIDENCE.md:77 says "a narrowed remit". Source re-fetched: the release says "The work of the AI Security Institute won't change, but this renewed focus will ensure our citizens … are protected", launches "a new criminal misuse team" with the Home Office, and the partnership with the developer is "the work of the UK's new Sovereign AI unit". **Repair** (reg/EVIDENCE.md:77, the last two sentences): "The release presents the focus as renewed and the institute's work as unchanged ("won't change"), and launches a criminal misuse team with the Home Office. Its bearing on T3 is narrow: a renamed institute with a stated security focus and a government partnership with an evaluated developer, announced together, are the kind of arrangement Test I measures; whether the remit narrowed needs the prior remit and the programme compared, which this register has not done, and neither shows an impaired purpose." core/70_s7.md:85 (T3, "refocused") stands.

### EG9c ("No dimension is met") — holds
disc/11_X11.md:43; reg/TESTS.md:154. **Repair** (X11:43): "No dimension has been shown to meet its registered criterion, and none is yet measured in the form {{readiness}} asks for: no domain of use has set a threshold, so no residence has begun [obs]. The states differ: Q5 and Q7 are absent (no binding tempo, no custody); Q3 has contrary evidence in written commitments; Q1 and Q4 are unmeasured, Q4 with adverse indications; Q2 and Q6 are mixed." Add a column "State" to the table at X11:33–41 with those entries. reg/TESTS.md:154, last sentence: "…*Where things stand*: none has been shown to meet its criterion, some are absent and some unmeasured, and none is yet measured in the form {{readiness}} asks for." **Check:** BANNED `r'No dimension is met'`, `r'none is met'`.

### EG9d (present-policy table) — holds
disc/08_X8.md:97, last cell "No, unless custody follows". **Repair:** "Only if detection and response act before a breakout becomes decisive (C7; {{detectlink}}), or custody follows".

### EG9e (2.8× cap; SRC-08) — partly
EV9 (reg/EVIDENCE.md:185) already says the figure is pre-training efficiency to 2023; disc/11_X11.md:58 calls it "a rate condition verification must meet". reg/TESTS.md:149 reads as a schedule ("must tighten about 2.8 times a year"). **Repair** (TESTS:149, third cell): "Efficiency-corrected compute caps. At the central estimate for pre-training efficiency on language benchmarks to 2023, a nominal cap must tighten about 2.8 times a year to hold a capability line (about 1.5 to 64 across the published interval; EV9), an illustration; a binding schedule needs an efficiency envelope estimated for each regulated capability, with post-training, inference-time and algorithmic uncertainty. Capability measured through compute, training data and elicitation by fine-tuning." **Check:** GV(o) ($2^{12/8}=2.828$, $2^{12/22}=1.459$, $2^{12/2}=64$).

### EG9f ("Custody must precede decisiveness"; SRC-16) — partly
The internal evidence review judged the X11 wording apt (R-v6.2-evidence:300), and X11's last column does qualify the analogy; but core/b0_s11.md:95 states the necessity in bold as what the 1946 failure shows, and disc/11_X11.md:69 puts it in "What it shows". The theory's own ground is the enforcement condition (core/70_s7.md:69–71; {{restraint}}), not the precedent. **Repair.** core/b0_s11.md:95: "The 1946 proposals for international ownership of atomic energy failed on sequence and on enforcement against violators, the record this theory reads, with its own reason from the enforcement condition (Section 7.2; {{restraint}}), as **custody must precede decisiveness**." disc/11_X11.md:69, third cell: "Read by this theory: custody has to be in place before any party could hold decisive capability alone, and enforcement against violators is part of the bargain; the record shows a sequence that failed, not that the requirement is necessary"; second cell, add the primary source verified by Codex and re-fetched here: "(Bundy 1988; the policy memorandum of 7 June 1946 to the U.S. representative: "when the system of control is fully in operation there would be no stockpiles of bombs in existence", FRUS 1946 vol. I, doc. 448)", and register it in disc/z9_refs.md with ‡ (page), *checked 2026-10-04*.

## EG10 (P2; DISCUSSION X10; SRC-18) — holds

**Claim.** Publishing a hash lets anyone verify prior choice; it does not make the metric secret, and "no one can train on it" does not follow.

**Current text.** disc/10_X10.md:34 ("committed in advance by a cryptographic hash … so that anyone can check that the metric was fixed beforehand and no one can train on it"); :14 (standard-setting, "committed in advance by hash"); reg/CLAIMS.md:285.

**Test (GV(e)).** 10,000 candidate metric configurations: the unsalted SHA-256 commitment is inverted by enumeration; a commitment salted with 256 bits matches no candidate by enumeration and verifies on opening.

**Repair.**
1. disc/10_X10.md:34, replaced: "**Held-out metrics.** A held-out metric published at registration is no longer held out: it becomes a target (Section 5.4). Each metric is committed in advance by a salted commitment under a stated scheme, the test package with a fresh random nonce of at least 128 bits, so that anyone can check on opening that it was fixed beforehand. The commitment binds; it hides only while nonce and package stay secret, and it does nothing against those who hold them. Secrecy is a separate protocol: the package and nonce are held by a body other than the standards body and every assessed party, under logged access audited by a different lineage, with a leak recorded as a violation; and each metric is retired after its first use, since opening it makes it public. The commitment shows prior choice; that no one trained on the metric rests on the access log and on a fresh metric at each evaluation, and is tested, not assumed."
2. disc/10_X10.md:14, "Corrected by" cell: "Held-out metrics, committed in advance by salted commitment, held under logged access by a separate holder and revealed only at evaluation; evaluation network; chamber".
3. reg/CLAIMS.md:285: "held-out metrics committed by salted commitment, with secrecy a separately audited protocol".

**Check to add.** GV(e). BANNED: `r'no one can train on it'`.

## Source audit (Codex's 18 entries)

"Already-fixed" here means the register already states what the audit verified; no change is needed.

| ID | Source; register row | Status | Where now; action |
|---|---|---|---|
| SRC-01 | RSP v3.0; EV2 | already-fixed | reg/EVIDENCE.md:53, :68: "written commitments, not conduct". None. |
| SRC-02 | RSP history (v3.4, 8 July 2026); EV2 | already-fixed | reg/EVIDENCE.md:53, :64: discretion kept apart from obligation. None. |
| SRC-03 | OpenAI Preparedness Framework v2 §4.3; EV2 | holds (P3) | reg/EVIDENCE.md:52 omits that, per Codex's reading of the PDF, the framework also states safeguards during internal development. Under the one-standard rule it is contrary evidence on internal deployment. Add after the §4.3 quotation: "The framework also sets safeguards that apply during internal development and deployment (§ to be cited on re-reading); per the Codex review of 4 October 2026." I could not read the PDF here (binary); re-read it and cite the section before entering. |
| SRC-04 | Zhu, Silent Revision; EV2 | already-fixed | reg/EVIDENCE.md:60: 710 instances, twelve pairs, 77%, 67%/53%, workshop review. None. |
| SRC-05 | EvalDetectBench; EV6 | already-fixed | reg/EVIDENCE.md:125: identifier 2609.01611 with date 8 June 2026 as retrieved; do not "correct" from the identifier. None. |
| SRC-06 | METR time horizons; EV5 | already-fixed (row); downstream EG8 | reg/EVIDENCE.md:110. The not-a-sanctionability-measure point is EG8. |
| SRC-07 | Epoch open–closed ECI gap; EV5 | already-fixed (row); downstream EG8 | reg/EVIDENCE.md:112. |
| SRC-08 | Ho et al. 2024; EV9 | already-fixed (row); downstream EG9e | reg/EVIDENCE.md:184–185. |
| SRC-09 | Fudenberg and Koh; EV11, X8 | holds | EG7. |
| SRC-10 | Public First Action announcements; EV4 | already-fixed | reg/EVIDENCE.md:93, :101: "pledges and reports, not audited disclosures". None. |
| SRC-11 | UK AISI rename; EV3 | holds | EG9b. |
| SRC-12 | EO 14365; EV1, EV3 | partly | EG9a. |
| SRC-13 | White House fact sheet, 25 Sept 2026; EV8 | already-fixed | reg/EVIDENCE.md:174: no binding limit marked as interpretation. None. |
| SRC-14 | UN preliminary-report announcement; EV7, EV8 | already-fixed | reg/EVIDENCE.md:150: "primary announcement … the report itself not read". Codex could not retrieve it (403); keep the coverage statement exactly. |
| SRC-15 | Business Roundtable 2019; EV15 | already-fixed | reg/EVIDENCE.md:249, :256: declared criteria, not conduct. None. |
| SRC-16 | Truman memorandum, FRUS 1946 v. I d. 448; X11 | partly | EG9f: add as the primary source of the Baruch row; necessity not shown by it. |
| SRC-17 | OECD side-by-side package; EV18, X10 | partly (P3) | reg/EVIDENCE.md:285 and disc/10_X10.md:81 read the exemption as unravelling. The arrangement exempts in recognition of that participant's own minimum-tax rules and keeps domestic minimum top-up taxes. Repair EV18: replace "This is closer to the unravelling of coverage … than to leakage where coverage is incomplete." with "The arrangement presents the exemption as recognition of an equivalent domestic rule; read by this register as closer to the unravelling of coverage in THEORY §9, the largest participant exempted, than to leakage, an interpretation the alternative-rule structure qualifies; the full implementing package was not read." X10:81: "…the largest participant's groups were exempted from two of its rules in recognition of that participant's own minimum-tax rules (EVIDENCE EV18), which this paper reads as the coverage problem of Section 9's participation threshold arising at the participant whose coverage matters most." |
| SRC-18 | Stanford CS355 lecture 3; X10 | holds | EG10 (binding vs hiding); cite in disc/z9_refs.md if the X10 repair cites a commitment scheme. |

## EG-C0 (P3; key: thresholds; crux C0; Test E) — holds (overlaps integration I3)

**Claim.** Test E's contrast, a disclosure duty, is not automatically a one-signature control: disclosure can move funding, access, reputation, enforcement and language. The test lacks unit, estimand, dwell window, effect size and power.

**Current text.** reg/TESTS.md:11 (C0 next measurement), :124 (Test E); core/70_s7.md:99.

**Repair.** reg/TESTS.md:124, append to "What is measured": "Registered before the intervention: the unit of analysis; the intervention's direct channels, listed; W, C and N outcome measures; the dwell window; a minimum effect size with power. The contrast rule must be shown in advance to act directly on one signature only, its direct channels listed; otherwise the test compares the number of groups moved beyond what each intervention's listed channels explain." core/70_s7.md:99: "…where a rule aimed at one signature, with its direct channels listed in advance, should not." **Check:** none (design).

## EG-N1 (normative; core/80_s8.md:13) — needs-ren

Codex: define the boundary between O1 and deaths from benefits forgone so two equally large irreversible losses are not classed differently only because one is by omission. The text already gives a reason in §11.3 (core/b0_s11.md:44): the asymmetry is in the option set, not the size of the losses (Arrow and Fisher 1974). **Options for Ren:** (a) keep, and add to core/80_s8.md:13 after "their weight is the normative crux N1": "The line is drawn by the option set, not by commission or omission: a loss that forecloses choice for everyone is O1, and a delay that leaves later choice open is a cost of the path, however large (Section 11.3)"; (b) define O1 by irreversibility and common cause whatever the route, moving large forgone-benefit mortality that forecloses choice into O1. Wording and choice are his.

## EG-N2 (normative; disc/10_X10.md:42) — already-fixed

Providers' voice without vote is stated as a trade-off, with the loss of local knowledge and compliance recorded (Ostrom 1990) and "managed, not dissolved". Codex's request, to test it under C4 rather than prove it, is met by C4 (core/c0_s12.md:62). Optional: add to reg/TESTS.md:16 (C4 next measurement) "the cost of voice without vote in withheld knowledge and compliance".

---

## S2-5 (High; keys: certificate, topology; institutional use) — holds; a corrected repair with a proof

**Claim.** {{certificate}}(2) proves $x_i\to0$ from $x_i(0)<1$; the text reads it as present independence ("no party controls the checks' funding, appointment or access"), and §12's estimators and custody rely on it now.

**Current text.** core/60_s6.md:91; core/40_s4.md:85–87; supp/04_S4.md:86; uses at core/c0_s12.md:12, :25 (estimator), :31 (coercive condition), core/b0_s11.md:50 (assessor), reg/TESTS.md:142, :147, disc/10_X10.md:9, :15, core/80_s8.md:48 (D4).

**Test (GV(f); codex_second_rerun.log).** Row sum 0.5, $x(0)=0.9$, $z(0)=2$, $\varepsilon=0.01$: $x(50)=1-2.2\times10^{-16}$, $z(50)=1.410$; the share peaks at $t=100\ln3=109.86$ and is $8.9\times10^{-152}$ by 1000. The certificate is true throughout.

**A sharper repair than "add a bound on current share".** In the field model, on the face $a_iz_i=c_i$, $\dot z_i=\varepsilon_i(\sum_jb_{ij}x_j-d_ic_i/a_i)\le\varepsilon_id_i(c_i/a_i)(\sum_jG_{ij}-1)<0$, since $x_j\le1$ and $\sum_jb_{ij}=(c_id_i/a_i)\sum_jG_{ij}$. So $\{a_iz_i\le c_i\}$ is forward invariant whatever the other domains do, and on it $\dot x_i\le0$. Before it is reached, $z_i(t)\le\bar z_i+(z_i(0)-\bar z_i)e^{-\varepsilon_id_it}$ with $\bar z_i=(c_i/a_i)\sum_jG_{ij}$, which reaches $c_i/a_i$ by $T_i$ below. Since $\dot x_i$ has the sign of $a_iz_i-c_i$ for $0<x_i<1$, "support at or below break-even" is observable as "the captured share not rising".

**Repair.**
1. core/40_s4.md:85, part (2): "*(2) If $\sum_jG_{ij}<1$, then $x_i\to0$ from every state with $x_i(0)<1$, whatever happens elsewhere; and the captured share stops rising no later than $T_i=(\varepsilon_id_i)^{-1}\ln^+\big[(a_iz_i(0)/c_i-\sum_jG_{ij})/(1-\sum_jG_{ij})\big]$ and does not rise again, so where it is not rising now, $a_iz_i(0)\le c_i$, it never exceeds its present value.*"
2. core/40_s4.md:87, Scope, append: "Part (2) certifies eventual removal; before $T_i$ the share can approach one under a valid certificate (a domain with row sum 0.5 is almost wholly captured for more than fifty periods, S4) [num: GV]. A certificate used for a decision now needs, besides the row sum, the present captured share measured and not rising."
3. supp/04_S4.md:86, proof of (2): append the two sentences of the derivation above, and the example ($x(50)>1-10^{-12}$, peak at $100\ln3$).
4. core/60_s6.md:91, first sentence: "Full inbound row sums below one are a sufficient certificate that capture of the checks' funding, appointment or access is removed in the end, from every start below full capture ({{certificate}}(2)), not a necessary one; a check relied on now needs in addition its present captured share measured and not rising, under which the share cannot exceed its present value; and they certify nothing about whether the checks' errors are independent: …".
5. core/c0_s12.md:25 (estimator) and :31 (coercive condition 2), and core/b0_s11.md:50 (assessor), reg/TESTS.md:142, :147: "correctors whose row sums are certified" → "correctors certified for present use, with full inbound row sums below one and present captured share measured and not rising ({{certificate}}(2))". core/c0_s12.md:12 (item 1): "certified row sums, with the present captured share, for every corrector domain".
6. disc/10_X10.md:9: "every body whose findings or decisions have force carries a full inbound row-sum certificate and a measured present share that is not rising ({{certificate}}(2))"; :15, end condition: "a row-sum certificate fails, or the measured captured share rises, for a reason not attributable to a party under its assessment".
7. core/80_s8.md:48 (D4) unchanged: a design test, read as "eventual" by (2)'s scope.

**Check to add.** GV(f): (a) $x(50)>1-10^{-12}$ and $x(1000)<10^{-100}$; (b) 150 random three-domain cases, others pinned at full capture, row sum below one and $a z(0)\le c$: largest rise of $x_0$ above $x_0(0)$ ≤ $10^{-12}$ (observed $-9.6\times10^{-6}$); (c) 150 cases with $z(0)$ above break-even: no rise after $T_i$; $T_i=109.861$ in Codex's example. Add "certificate" to GV's keys.

## S2-6 (Medium; keys: nested, blind, require; R8a, R8b) — partly

**Already fixed** (math-II M2-04, M2-05): "a negative tax spreads, a zero tax is neutral" and "keeps it from spreading …, removes it under cumulative selection if every inequality is strict" in core/c0_s12.md:14, :20; core/60_s6.md:63, :65, :75; core/90_s9.md:21; supp/07_S7.md:104; reg/TESTS.md:59.

**Still present.** Withdrawal at a measured zero: core/c0_s12.md:20 ("Withdrawn for a class whose tax is measured zero or negative … at zero, costs its developer nothing against its rivals"); :66 (C9a row); core/60_s6.md:101 ("until their tax is measured zero or negative"); reg/TESTS.md:20 (C9a third column), :74, :95 ("No common constraint is needed for that class"); disc/08_X8.md:7 ("the common constraint loses its reason to exist in that class").

**Test (GV(g); codex_second_rerun.log).** Unsafe share 0.3 at zero tax: withdrawn, it stays 0.300 forever; kept with sanction 0.05, $1.9\times10^{-5}$ by $t=200$. Equal sanction and cost (0.2, 0.2): both variants at 0.8, evaders remain.

**Repair.** At a measured zero, selection no longer removes unsafe variants and only level-1 choice does (supp/07_S7.md:104), so:
1. core/c0_s12.md:20: "Withdrawn for a class whose tax is measured negative, since its safeguard then pays privately; at a measured zero the constraint is neutral among developers, and is withdrawn only where the class's unsafe variants are measured absent among deployed systems, internal deployment included, or their developers are shown to counter the divergence unconstrained (Test L), since at zero selection no longer removes them (C9)."
2. core/c0_s12.md:66 and reg/TESTS.md:20 (C9a, third column): "Negative for a class, net of C9b and C9c: item 7 is withdrawn for it; zero: withdrawn only where its unsafe variants are measured absent or countered unconstrained (Test L). Positive, yet countered by developers alone: $(A_\tau)$ fails for that class (Test L)".
3. reg/TESTS.md:74, second and third columns: "C9a negative for a class, net of C9b and C9c; zero, with the class's unsafe variants measured absent or countered unconstrained; …" / "The constraint for that class, whose safeguard then pays privately or, at zero, is chosen without it; …".
4. reg/TESTS.md:95: "| C9a negative for a class, net of C9b and C9c; or zero with unsafe variants measured absent | No common constraint is needed for that class | … |".
5. core/60_s6.md:101: "until their tax is measured negative, or zero with their unsafe variants measured absent (Section 12.1)".
6. disc/08_X8.md:7: "…while those it brings to a tax of exactly zero are neutral under selection, and there the common constraint is needed only until the unsafe variants already deployed are gone (Section 6.4; {{nested}})."

**Check to add.** GV(g): 0.300 exactly at zero gap (tolerance $10^{-12}$); below $10^{-3}$ under sanction 0.05 by $t=200$.

## S2-7 and the synthesis's Table 7.1 audit (Medium; keys: thresholds, load, relsel, blind, certificate, enforce, detectlink, talk) — partly

**Already fixed** (math-II M2-08): Capture row has "with no per-unit cost floor, a positive cultivation channel and capacity tracking that level" (core/70_s7.md:22); Enforcement row has $D_i(a)>v_i$ (:23); Compounding "Both, through $p_d$" (:20).

**Still present, row by row** (core/70_s7.md:15–27):
- *Load* (:19): the danger side lacks the cumulative-selection premise that M2-01 put into Definition 3.2, {{load}} and Table 9.1 R1 ("cumulative ({{relsel}})"); "unequal incidence" is listed as pushing toward danger and "equal incidence" as reversing, though equal incidence serves neutrality among compliers (R8b), not host protection, and unequal incidence can fall on the more harmful variant. Codex's cubic rule (codex_second_rerun.log: share 0.001 → 0.00165, host above 0.997, though $B=\ln(1+t)\to\infty$) and VF(g) already reproduce why.
- *Capture* (:22): "row sum at least one" is the loss of a sufficient certificate, not capture from every start (S14's row sum two from a low start); the certified start of {{corrrate}} is not stated.
- *Enforcement* (:23): the detection form is stated without "in the one-period reduction" (fixed in {{detectlink}}, core/50_s5.md:40–42, and {{assure}}'s scope, core/80_s8.md:82, by M1); "objectives under which a decisive position is worth no more than restraint" does not alone deter a large immediate gain (GV(m): $\delta=0.9$, $C=1$, $D=0.9$, $g=1$: $0.100>0.090$).
- *Talk* (:25): verification, derivations, protocols and costly signals bypass the cheap-talk bias; they do not lower it below $\frac14$.
- *Header* (:15): "Reversed by" does not distinguish a directional comparative static from a magnitude that crosses the threshold.
- *Standing*: the endpoint $\theta_0=-1$ is the formal track's (F4).

**Repair.**
1. core/70_s7.md:15, append to the table's label: "In *Reversed by*, a lever moves its threshold toward the safe side in that row's model; whether it crosses depends on a magnitude the row does not supply, and an entry that acts by another route than the row's inequality says so."
2. :19 Load, danger side: "$\tau_{\rm eff}<\nu$: effective liability below the private advantage of loading the host, with cumulative advantage unbounded, under cumulative selection ({{relsel}}); under (reach) the host falls below its floor"; *pushed by*: replace "unequal incidence" with "incidence that falls more lightly on the more harmful variant"; *reversed by*: "Consequences returned to their source: a liability above the private advantage, covering every capable carrier, sanctioned above the gain from evasion; equal incidence among those who comply keeps the rule neutral among them (R8b)".
3. :22 Capture, danger side, append: "(the loss of the sufficient certificate of {{certificate}}(2), not capture from every start; the rate condition holds from a certified start)".
4. :23 Enforcement, danger side: "…; where punishment is triggered by detection, in the one-period reduction of {{detectlink}}, $\upsilon(T_{\rm dec})<1-\bar p_{d,i}$, with the exact conditions for real delays in S5"; *reversed by*: replace "objectives under which a decisive position is worth no more than restraint" with "objectives under which a decisive position is worth enough less than restraint to cover the immediate gain, $(1-\delta)g_i\le\delta(C_i-D_i)$ ({{enforce}}(4))".
5. :25 Talk, *reversed by*: "Wider working objectives and lower contested stakes, which lower the effective bias; verification, derivations from public premises, protocols agreed in advance and costly signals, which bypass it with information whose credibility does not rest on the sender's bias (Section 11.2)".
6. Propagate to supp/07_S7.md (the full matrix) wherever the same cells are printed, and to reg/CLAIMS.md:186, :190, :192 (crosswalk rows) only if they restate the cells.

**Check to add.** GV(m) ($0.100>0.090$). VF(g) already covers the cumulative-selection premise; no new assertion for the wording.

## S2-8 (Medium; keys: readrule, readiness) — holds

**Claim.** Remark S11.3(2) asserts termination with probability one from independent readings with correct likelihood ratios, with no condition that information keeps accumulating.

**Current text.** supp/11_S11.md:69 ("on independent readings whose likelihood ratio is computed from their distribution … The test ends with probability one"), :71 (proof "Wald's termination theorem"). M2-14 already restricted the error bounds to the registered levels and named the indifference zone (supp/11_S11.md:69, :73; core/b0_s11.md:50).

**Test (GV(h)).** $H_0$: Bernoulli(1/2), $H_1$: Bernoulli($1/2+2^{-t-4}$): every log-likelihood ratio on every path stays in [−0.127701, 0.122485], inside the boundaries (−4.93159, 4.59800) for $a=0.01$, $b=0.05/7$; the test never ends.

**Repair.**
1. supp/11_S11.md:69, part (2): "…on independent, identically distributed readings whose log-likelihood ratio is not zero with probability one, its distribution known to the test…. The test then ends with probability one (Wald 1945); with readings whose informativeness can fade, termination needs the accumulated information to diverge, and without it the test can run forever on every path (S11) [num: GV]." Proof (:71): "(2) is Wald's termination theorem for independent, identically distributed log-likelihood increments that are not almost surely zero, and his bounds…".
2. core/b0_s11.md:50, Definition {{readiness}}, after "with a model of the noise in its readings": "independent and identically distributed under each level, or with information that accumulates without bound,"; and, to meet SA-02 (systems track) at the same place, "the rate of declaring it met when it stands at the lower level" for "the rate of declaring it met when it is not", with "a reading that ends inside the indifference zone leaves the dimension unmet".
3. reg/TESTS.md:154: "…each decided by a sequential test registered in advance, on readings that accumulate information ({{readrule}})".

**Check to add.** GV(h): bounds −0.127701, 0.122485 (±$10^{-5}$) inside −4.93159, 4.59800.

## S2-9b (Medium; tier 1(b) withdrawal) — holds

**Claim.** "Withdrawn only where a named crux is measured favourable" needs a precautionary value premise stated as such, and an escape for evidence that the remedy itself fails or raises the protected risk (Test M, C4); bounds 0.1 without a mandate and 0.2 with a badly designed one are compatible with late evidence.

**Current text.** core/c0_s12.md:18 ("each item stands until its crux is measured favourable, and then loses only the part that crux bears [val]"); reg/TESTS.md:69. Test M's revision clause (reg/TESTS.md:131) is not in the rule.

**Repair.** core/c0_s12.md:18, the sentence beginning "A protection that waits…": "A protection that waits for that evidence waits too long, so under the protection standard the burden of proof lies on withdrawal, a choice of value [val]: each item stands until its crux is measured favourable, and then loses only the part that crux bears; and an item shown, as specified, to fail its stress test or to raise the protected risk it was meant to lower is revised in form, its purpose kept (Test M; C4)." reg/TESTS.md:69, same addition after "loses only the part that crux bears". **Check:** none.

## S2-9c (Medium; tier 2) — partly

Same defect and repair as EG4. The design specification is in place (already-fixed part of EG4); "commitment leaves only detecting" and the execution accounting are not. E2 and E3 are kept separate (EG6).

## S2-9d (Medium; keys: lockin, delegatelock, influence, wingives, sprint) — holds

**Claim.** In tier 3 the design's capture and collusion are reversible given timely recertification, while a holder's or restrictor's converted correctors are simply irreversible, citing {{influence}}, which proves selection for influence, not impossibility of correction; the summary loses {{lockin}}'s qualification (delay, not irreversibility); standby restoration cannot reverse harm already done.

**Current text.** core/c0_s12.md:34 ("the capacity to overrule lost ({{lockin}})"); disc/08_X8.md:145 ("Delegation locks | Irreversible once the capacity to overrule is lost"), :155 ("The holder's own correctors are converted | Irreversible | [thm] {{influence}}"), :162 ("The restrictor's correctors are converted | Irreversible | [thm] {{influence}}"), :169 (standby; EG3 item 3). The lemma itself (core/60_s6.md:35) and :39 (when $q_L$ is near one) are correct.

**Test (GV(n); codex_second_rerun.log).** Capacity 0.2, recoverable level 1, floor 0.5, rate 0.1: back at the floor after $10\ln1.6=4.70004$.

**Repair.**
1. core/c0_s12.md:34: "the capacity to overrule lost where the decision is irreversible within the time for deliberation or the contest denies the recovery time ({{lockin}}; {{delegatelock}})" (already in EG3's text).
2. disc/08_X8.md:145: "| | Delegation locks | Irreversible where the decision is irreversible within the time for deliberation, or delegation has outlasted $T_{\rm lock}$ while the contest denies the recovery time; otherwise capacity returns after it | [thm] {{lockin}}, {{delegatelock}}; [obs] EV8 | Declared doctrine; inspected exercises; drills of parallel capacity (narrow E1) |".
3. disc/08_X8.md:155: "| | The holder's own correctors are converted | Irreversible where the holder holds decisive capability, since no one is above it; {{influence}} shows why conversion is selected, not that it cannot be undone | [thm] {{sprint}}, {{wingives}}; [thm] {{influence}}; [—] | Row sums inside the holder |".
4. disc/08_X8.md:162: "| | The restrictor's correctors are converted | Reversible on the design's terms, by recertification under the conditions of Section 12.1, while the restrictor holds no decisive capability and a corrector outside it can still execute; irreversible where it does hold it | [thm] {{influence}}, {{wingives}}; [—] | Row sums of the restrictor's correctors (the conditions of Section 12.1) |".

**Check to add.** GV(n) (4.70004 ± $10^{-5}$).

## S2-9e (Medium; §8.1) — holds

The existence of an irreversible outcome in a path's range does not show its bound exceeds the tolerance. Same repair and check as EG2.

## S2-B1 (boundary; keys: pausevalue, nonsum) — holds

**Current text.** supp/11_S11.md:45 (pausevalue(2): "A pause after which the residual sequence is summable … keeps survival bounded away from zero"); core/b0_s11.md:48 (same); core/50_s5.md:74 ({{nonsum}} summary: "stays bounded away from zero if it is at most a summable one"). The proof (supp/11_S11.md:47) and the full lemma (supp/05_S5.md:95) already use $\bar h_k<1$. **Test (GV(i)).** $(1,0,0,\dots)$ is summable and gives zero survival. **Repair.** supp/11_S11.md:45, (2): "*(2) A pause after which the residual hazards are at most a summable sequence $\bar h_t<1$ on every surviving history, where before they were not, keeps survival bounded away from zero, provided survival to the change is positive.*" core/b0_s11.md:48: "a pause after which they are at most a summable sequence, each term below one, keeps survival bounded away from zero once survival to the change is positive". core/50_s5.md:74: "…and stays bounded away from zero if it is at most a summable one with every term below one…". **Check:** GV(i).

## S2-B2 (boundary; keys: dwell, capturebasin, readiness; release) — holds

**Current text.** supp/11_S11.md:79 ("the *dwell* $T_{\min}$ is the least $T$ after which the state converges to absence of capture"), :82–85 (values), :99 ({{capturebasin}}: "held for the $T_{\min}$ … the minimum capture time"); core/c0_s12.md:27 (release "held for the dwell time"); core/b0_s11.md:72. **Test (GV(j); codex_second_rerun.log).** $G=2$, equal speeds, $x_0=0.99$: boundary 5.858956; a hold 0.001 shorter is re-captured, 0.001 longer succeeds; released exactly on the separatrix, the state goes to the saddle. Also from $x_0=1$ no hold suffices (invariant face). **Repair.** supp/11_S11.md:79: "the *dwell* $T_{\min}$ is the infimum of the holds $T$ after which the state converges to absence of capture; a hold of exactly $T_{\min}$ releases the state onto the saddle's stable manifold, so release needs $T>T_{\min}$, by a margin registered in advance. From $x_0=1$ no hold suffices, since the face $x=1$ is invariant." {{dwell}} statement (:81): "Start an insulating reform … with share $x_0<1$." :99: "…the basin of absence is reached from a captured state with $x_0<1$ iff insulation is held longer than the $T_{\min}$ of {{dwell}}, which is therefore the infimum capture time, not attained". core/c0_s12.md:27: "each held beyond the dwell time of the slow variable it rests on, by a registered margin". **Check:** GV(j), boundary 5.858956 ± $10^{-3}$, opposite basins at ±0.001; add to DW's keys.

## S2-B3 (boundary; key: signal) — holds

**Current text.** core/b0_s11.md:27: "A receiver restrains iff its belief that the sender is $\mathsf S$ is at least $\varpi^\ast$". The proof (supp/11_S11.md:27) already lets the receiver randomize at equality, and part (2)'s bounding equilibrium needs it. **Test (GV(k)).** $\mu=0.5$, $\varpi^\ast=0.6$, $c_{\mathsf R}=0.05$, $\Pi_{\mathsf R}=0.2$: $\mathsf R$ imitates with probability 0.6667, the posterior is exactly 0.6, and restraint is 0.25; were restraint certain at equality, $\mathsf R$'s step would pay 0.15 > 0, so it imitates always and the posterior falls to 0.5. **Repair.** core/b0_s11.md:27: "A receiver restrains when its belief that the sender is $\mathsf S$ exceeds $\varpi^\ast\in(0,1)$, races when it falls short, and may randomize at equality". **Check:** GV(k).

---

## The proposed block GV

`/private/tmp/claude-501/v62codexfix/governance/gv_checks.py` is written to drop into `checks_v62.py` as `check_GV`, added to `ORDER` after `VF`: replace its local `expect` with the harness's, call `block('GV', 'coverage, nonsum, kernel, tdec, detectlink, certificate, nested, readrule, pausevalue, dwell, signal, enforce, lockin', 'independent: direct computation (products, simulation, Euler and RK4 integration, enumeration); (b), (o), (p) identity', 'Governance decision rules: release and activation, comparison, commitment, certificates, readiness')`. 24 assertions, 2 s, all pass. Its numbers are the ones quoted in each entry; no tolerance was set to fit a claim (each tolerance is an order of magnitude below the effect it guards or a stated rounding).

Banned phrases for `src/assemble_v62.py` `BANNED`, to guard against regressions (word CHANGELOG entries so as not to quote them): `falling under present incentives`, `[Rr]esidual risk not falling`, `残余风险不降`, `none meets the tolerance`, `as each does under the rule`, `Both fail the tolerance`, `every worst case crosses`, `最坏情形都越过容忍线`, `commitment leaves only detecting`, `on every reading of the cruxes`, `forgoes nothing`, `costs only the preparation`, `exceeds any warning`, `racing region of the real parameters while`, `no breakout has yet put anyone beyond punishment`, `No dimension is met`, `none is met`, `no one can train on it`.

## Limits

I did not re-prove inherited results, run `checks_v62.py`, or rebuild the documents (src unchanged; the build writes assembled files). Sources were re-fetched through a summarizing tool with quotations requested verbatim; the OpenAI framework PDF could not be read. The new clause of {{certificate}}(2) is a derivation of mine with a numerical check, and needs the same outside review as the rest. I belong to the drafting model family; the readings most exposed to that are EG3's matched rows and EG6's table, which choose a structure the paper did not state.
