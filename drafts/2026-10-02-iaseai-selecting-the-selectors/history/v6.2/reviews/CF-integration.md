# CF-integration: the Codex reviews of V6.2, integration track and the findings no other track owns

*4 October 2026. Verifier: Claude (Opus 5.5), same model family as the drafters. Inputs: `REVIEW-v6.2-codex.md` (integration report I1–I4, preservation sample, build record) and `REVIEW-v6.2-codex-second.md` (with `codex-second/second-checks/AUDIT-CHECKS-TRANSITION.md` and `assertion-audit.tsv`). Every finding was tested against the CURRENT `src/` and `checks_v62.py` (after the internal round of `FIXES-v6.2-verify.md`), not the snapshot f50fb6a1. No project file was edited. Scripts and logs: `/private/tmp/claude-501/v62codexfix/integration/`.*

| Script | What it establishes |
|---|---|
| `i1_harness_audit.py` | Static audit (ast): blocks of the current checker with no `expect()`; the legacy runner's exit status |
| `i1_fault_injection.py` | Known-false results injected into a copy: FB, TC, BI exit 0; the control (FF, which asserts) exits 1 |
| `i1_patch.py` → `checks_v62_gated.py` | The proposed gates applied to a copy; the 14 formerly print-only blocks pass all 23 new gates; the same injections now exit 1; `--inject-fail` and `--inject-raise` exit 1; full default run: `checks_v62_gated.log` |
| `checks_v62_gated_crtk.py` | Two further gates on print-only comparisons inside extended blocks (CR(b), TK base): pass |
| `i3_test_e.py` | Test E as written cannot tell the interlock from separate causes with one ordinary spillover; two estimands that can |
| `i2_precursor.py` | A rule learned from reversible failures that share the mechanism protects against a global irreversible failure in time, without any model of it |
| `n2_tag_sync.py` | CLAIMS tags against declaration tags (consistent today; nothing guards them through the repairs) |
| `iso/` | An isolated copy of v6.2 without the sibling `v6/`: `refs_v62.py` and `xref_v62.py` fail; adding `v6/THEORY.md` makes xref pass |

## Ownership of every finding (both reviews)

Track assignment follows `planning/workflows/v62-codex-fix.js`: formal = §§2–5 mathematics; systems = §§6, 9–11, readiness and transition; governance = §§7–8, 12, cruxes, activation and withdrawal, evidence and comparisons; integration = I1–I4 and whatever none of those covers.

| Finding | Owner | Note |
|---|---|---|
| First review synthesis 1–2; F1–F6; F-C1, F-C2 | formal | |
| Formal report "Numerical and proof workflow" 1–6; δ=0 and zero-conversion boundary conventions; "return" as convergence at a cap equal to K* | formal | Item 1 (count is not certification) is also answered by I1/X-kinds below; FS's rest branch is gated in I1 |
| Synthesis 3–4; SA-01–SA-09 | systems | |
| Synthesis 5; EG1–EG10; the 18-entry source audit; "Normative disagreements" (O1 against forgone benefits; provider exclusion) | governance | |
| Synthesis "Table 7.1 audit" | governance (§7), with the formal and systems content of each row | |
| Synthesis "Revision order" item 4 (propagate statuses) | plan, area D | Guard proposed here as N2 |
| I1, I2, I3, I4 | integration | Below |
| Integration report: preservation sample | integration | Below, I-pres |
| Integration report: "What the build checks establish" (sibling bibliography; register-only citations) | integration | Below, B1, B2 |
| Evidence report "C0 and the empirical programme", Test E paragraph | integration | Folded into I3 (the report itself defers to the root review) |
| Second review 1 (balanced growth), 2 (responsive-rival price, finite-jump lottery, catch-up clarification), 3 (detection link), 4 (payoff-monotone), boundary row θ₀=−1 | formal | |
| Second review 5 (row-sum certificate is not independence now) | systems (topology, §6.5; §4 certificate), with its §12 use by governance | |
| Second review 6 (zero tax, equal sanction), 8 (SPRT termination); boundary rows: core pruning at gain one, receiver tie at the threshold, dwell an infimum, post-pause summability, serial product p_ℓ^k | systems | |
| Second review checks audit: the ratchet under pulsed insulation | systems (§11) | |
| Second review 7 (Table 7.1), 9 (judgment adds decision principles) | governance | Its capture-row floor premise was already restored by FIXES M2-08 (`core/70_s7.md:22`) |
| Second review "What the checks establish": 13 blocks without counted assertions | integration | = I1 |
| Second review: S15 says the default run writes `checks_v62.log` | integration | Below, X-S15log |
| Second review: assertion map, S15's kind labels incomplete at part level | integration | Below, X-kinds |
| Second review: JX and MP are hybrid checks | formal | JX already relabelled (FIXES M1, M9); MP(a) listed in X-kinds for coordination |
| Review-status lines made stale by the two Codex reviews | integration (not a Codex finding) | Below, N1 |

---

## I1. The test runner does not fail on every reported numerical failure (P2)

**Status: holds.** Keys: `bench`, `twochan`, `club`, `require` (R3b), `alarm`, `racehazard`, `frontier`, `zonesillus`, `wingives`, `talk`, `enough`, `fallback`, `loopgain`, `compound`, `standprice` (deterministic), `relpunish`.

**Where now.** `checks_v62.py`: FB 65–78, TC 81–115, TH 117–126, CB 128–139, RH 141–168, FS 170–206, BI 208–230, WG 232–237, TK 239–263 (base), PE 284–298, FD 300–316, CR 482 (base, part (b)), LG 521–712, T3 714–770, AC 1245–1275, FA 1343–1361; main 5885–5916. `supp/15_S15.md:3` and the "What it asserts" column; `reg/README.md:20`; `reg/CHANGELOG.md:53`.

**Reproduction on the current file.** The internal round added block VF but no gate to any inherited block. Exactly Codex's fourteen blocks still contribute no `expect()`: FB, LG, TC, TH, CB, FA, AC, RH, FS, BI, WG, T3, PE, FD (23 base functions have none; 9 of them carry asserting extensions). Thirty [num:]/[identity:] tags in the text are served by these blocks, among them S8's 0.976/0.864/0.211 against 0.875/0.575/0.026 [num: FD], S5's 0.717 and 1.8×10⁻⁹ [num: PE], S5's frontier at 322 against 320 and host minima 0.245/0.194 [num: FS], S4's 0.9814 and 0.376 [num: AC], S3's 5.17/0.37 and 31.0/2.2 [num: CB], S9's 3.2×10⁻¹⁰ [num: FA], S7's "grows to about 4" [num: LG]. Inside extended blocks two printed comparisons are also ungated: CR(b) "violations 0/3000" and TK's "equilibria whose receiver payoff differs from the no-talk value: 0" (S15's TK row says it asserts this). Fault injection on a copy (`i1_fault_injection.py`): FB with `agree += False` prints "agreement 0/200000", TC with a broken identity prints "failures 18053", BI with an inflated count prints "mismatches 7": each run ends "0 passed, 0 failed" and exits 0. The control, a false `expect` in FF, exits 1, so the gate itself works. Two further gaps: (a) `--legacy` prints each suite's exit code and never fails; the legacy suites contain no assertion at all, so their exit code says only that they ran without crashing; (b) T3 prints "two-message equilibrium: none (exists iff bias<1/4: True)" at n=10, b₀=0.2, because the golden-section bias is 0.2499999… while the exact bias is ¼: a reader of the log sees a disagreement exactly at the boundary the text resolves ("at exactly ¼, none", `supp/05_S5.md:125`). A gate must use the exact b₀n/(n−2) and the boundary rule.

**Repair (checks_v62.py; exact code in `i1_patch.py` and `checks_v62_gated_crtk.py`).** Add one `expect` per comparison the text relies on, labelled with the numbers it must reproduce:

| Block | Assertion (label as it should print) | Numbers reproduced |
|---|---|---|
| FB | `agree == N`: spectral radius < 1 iff ab < d_u d_w | 200,000/200,000 |
| TC | identity failures 0; λ↔θ failures 0; levy, renege and host values equal formulas to 1e-12; spite pays iff θ < −(n−1)c/Δ_y | 0, 0; θ=−1,0,1(,3) |
| TH | θ recovered to 1e-3 at θ=−1,−0.5,0,0.4,1,2,2.9 | ratios 0, 0.5714, 1.3333, 2.1538, 4, 12, 156 |
| CB | club and system intensities equal (W/(2(c+nℓ)))², (W/(2(c+nℓ+m_oℓ_o)))² to 1e-4 | 5.17 vs 0.37; harm 31.0 vs 2.2 |
| FA | stays in [0,0.1]×[0,0.2]; x(20) ∈ (3.1, 3.3)×10⁻¹⁰; z < 1e-7 | 3.2×10⁻¹⁰ |
| AC | lag-one autocorrelation identical across m=0, 0.25, 0.5 to 1e-12; means 0.358, 0.519, 0.679; φ=0.9814; condition 0.376; filter with memory 0.042 | as listed |
| RH | grid best response within one grid step of the symmetric intensity | 0.11444 (the h lines stay an identity) |
| FS | θ=−1: switch at frontier within 1% of 322.2 (simulated 320.4), peak 494, final stock < 1e-8; no switch at θ=0, 3; host minimum 0.245 vs 0.194; with Δ_y=0.05 no switch at θ=−1, 0 (rest beats destruction) | 320/322, 494, 0.245, 0.194 |
| BI | brute force agrees with closed-form zones, mismatches 0, draws > 10,000 | 14,429 draws |
| WG | grid optimum within 1e-4 of θ/(1+θ) | 0.286, 0.500, 0.667, 0.750 |
| T3 | (a) identity < 1e-12; (b) bias equals b₀n/(n−2) to 1e-6, a two-message equilibrium exists iff exact bias < ¼ (none at exactly ¼), boundary within 1e-3 of ½−2·bias; (c) max |O_S+O_R| < 1e-12 | 3.6e-15; boundaries 0.5, 0.2, 0.02, 0.1, 0.2; none at 0.3, 0.3, 0.25 |
| PE | frozen: survival 0.717, coverage catches up at t=14; compounding: 1.7e-9 < S < 1.9e-9 | 0.717, 14, 1.83e-9 |
| FD | (H, arrangement, continuation) = (10, 0.976, 0.875), (30, 0.864, 0.575), (100, 0.211, 0.026) | as listed |
| LG | (A) mismatches 0, fewer than 20 skipped; (A′) gap > 1 iff Γ > 1 and < 1e-10 otherwise in six cases, the reflexive case 3.96 ± 0.01; (B) max relative error < 1e-5 where Γ < 1, and where Γ ≥ 1 > Γ_δ the PV at x=1e-10 within 1e-3 of Γ_δ/(1−Γ_δ) in the three printed cases; (C), (C′) direct e* equals e(θ_eff) to 1e-6, labelled [identity] | 3,996 systems; 3.96; 1.7e-6; 6.2428/6.2436 |
| CR | (b) violations 0 in 3,000 anonymous games | 0/3000 |
| TK | 300 games, equilibria found > 0, none differs from the no-talk value | 1,096 equilibria |

Harness: add `_harness_selftest()`, called in every full default run before the index, which runs the script with `--inject-fail` (one block 'ZZ' asserting `False`) and `--inject-raise` (a block raising) in subprocesses and asserts exit status 1 and nonzero; under `--legacy`, append any nonzero legacy exit to the failure list and print "(diagnostic: legacy suites print and assert nothing)". Print-only lines that remain (TC's θ table, BI's θ_rep and p_d cut-offs, PE's Tullock lines, FS's asymmetric start) stay as printed diagnostics; mark them "[diagnostic]" in the print.

On the copy all 23 gates in the fourteen blocks pass, CR and TK's two pass, both self-test modes exit 1, and the injected FB, TC and BI faults now exit 1 with `[FAIL]` lines. Full default run of the gated copy: see the closing note of this file for the count.

**Text to update with the gates.** `supp/15_S15.md:3`: "passes 202 assertions" → the count the run prints, and add: "Every comparison a tag in the text relies on is asserted; lines marked [diagnostic] are printed and not asserted. The run also tests itself: an injected false assertion and an exception inside a block must each end it with a nonzero exit status." S15 table: the "What it asserts" cells of FB, LG, TC, TH, CB, FA, AC, RH, FS, BI, WG, T3, PE, FD become true as written once gated; RH's cell adds "the grid best response 0.11444 is asserted". "Earlier suites": "each runs and exits without error as of 4 October 2026" → add "they print and assert nothing; `--legacy` fails if any exits with an error". `reg/README.md:20` and `reg/CHANGELOG.md:53`: the new block and assertion counts. Keep the Supplement's disclaimer that no suite certifies every proof.

**Check to add.** The 25 gates above and the two self-test assertions (`harness: an injected false assertion gives exit status 1`; `harness: an exception inside a block gives a nonzero exit status`). With nothing else changed the default count rises from 202 to 229.

---

## X-S15log. S15 says the default run writes the log (second review, checks section; P3)

**Status: holds.** `supp/15_S15.md:3`: "a default run … passes 202 assertions and writes `checks_v62.log`". The script writes standard output; the log exists only through the redirection its own docstring and README show (`python3 checks_v62.py > checks_v62.log`).

**Repair.** `supp/15_S15.md:3`: "…a default run takes about five minutes and passes [N] assertions; `python3 checks_v62.py > checks_v62.log` writes the log." No check needed.

---

## X-kinds. S15's kind labels and the meaning of the count, at the level of parts (second review assertion map; first review formal workflow items 1–2; P3)

**Status: holds** (JX already relabelled by FIXES M1/M9). Locations: `supp/15_S15.md` rows AL (12), CH (16), ES (23), FF (27), MP (33), SP (42), TR (49); block headers in `checks_v62.py` (SP 1381, MP 1807, CH 2325, FF 3369, ES 3650, AL 4203, TR 4359).

**Verified in the current code.** Parts S15 calls independent that evaluate a stated formula or an identity: SP(H) (`checks_v62.py:1656–1665`: 1+θ from `theta_effective(gains(...))`); CH: Γ_δ of a ratio channel rising with d (2369–2372), outside case 2 (2394–2401), Γ_δ ≤ Γ in 2,000 systems (2656–2663); ES(e) R4 by `pbar`/`cond` (3741–3749), ES(g) windows from closed forms (3770–3781), ES(h) homogeneity of p̄ (3783–3789); AL(6.1) θ* (4209–4221), AL(BT) (4280–4285), AL(6.11) (4330–4343), AL(bounded), AL(contest) (4344–4357); TR(d) shift invariance by inserting zeros in the same product (4472–4479), TR(f) 0.95⁷ and the fixed design's normal-CDF power (4486–4503); FF(B)'s last line, d_f rising under [H_f] by its formula (3423–3425); MP(a) the static factor from the closed-form weighted-Tullock equilibrium, finite-differenced (1888–1911).

**Repair.** S15 kind cells: SP → "independent: (B), (C), (D), (F), (G); identity: (A), (E), (H), (I), (J)", and in its last column "Test Γ's sign under provision from the gain formula (H); the observable 1+θ optimized directly in (G)". CH → "independent; formula evaluations: Γ_δ rising with d in (a), outside case 2 in (c), Γ_δ ≤ Γ in s1; (h) derived". ES → "independent; identity: (e), (f), (g), (h) (formula evaluations of p̄ and (14)); the incentive check is (d)". AL → "independent: (6.2), (6.4), (6.7), (6.8), (6.10); derived, evaluating stated formulas: (6.1), (BT), (6.9), (6.11), (bounded), (contest)". TR → "(a)–(c) search over strategy profiles; (e) direct computation; (g) simulation; (d), (h) identity; (f) arithmetic and the normal distribution". FF → "independent; in (B) the line on d_f under [H_f] evaluates its formula". MP → "independent (value iteration), except (a): the static factor 2(n−1)/n from the closed-form equilibrium, derived" (coordinate with the formal track, which may restructure MP under F1 and second-review 2). Mirror each change in the block header string. Add to S15's opening: "The count is of checks, not of independent derivations: the parts marked identity or derived guard against slips, and only the independent parts are evidence for the statements they serve."

**Check.** None (labels). Optional: a test in the harness that every S15 row's code exists in `ORDER` (already implied by xref's tag inventory).

---

## I2. The necessity of shared understanding is a thesis beyond Lemma 3.11 (P2)

**Status: partly; two sub-choices need Ren.** Keys: `onegroup`; D36; CLAIMS §9 item 12.

**Where now.** `core/30_s3.md:94` (§3.6, after {{onegroup}}); `core/10_s01.md:22` (§1.2 item 2); `core/00_head.md:5` (abstract) and `:17` (guide item 2); `core/c0_s12.md:81` (§12.4); `reg/CLAIMS.md:21`, `:203`, `:425` (D36), `:452` (item 12); `disc/01_X1.md:154` (item 6).

**What the current text already does.** §3.6 has been narrowed since V6.1: "That, and not that nothing else can integrate at this scale, is the formal content of the claim". §12.2 states the lemma correctly ("the one term in which a benefit common to all can rise without a rule"). The planning record behind D36 already warns that Ren's sentence is about understanding as a condition of coordination, not a survival theorem (`v6-planning/P5-ren-corpus-generators.md`, item 2 of the overstatements).

**What remains.** (a) The bold sentence "**Where the failure to be avoided is global and irreversible, only the second acts in time**" is false without an antecedent: a rule learned from reversible failures that share the global failure's mechanism acts in time without any model of the global failure. `i2_precursor.py`: restraint costs its bearer 0.05; unrestrained conduct causes local reversible failures at rate 1·(1−z) and a global irreversible hazard 0.02·(1−z); after five local failures a liability 0.15 is enacted. Where the local failures share the mechanism, the liability comes at t=8.99, restraint goes to 1.0000 and survival of the global failure is 0.7494; where they do not, survival is 0.0242, the same as with no rule. What only anticipation can do is protect against what no reversible failure teaches in time. (b) The requirement itself carries no tag although §1.4 says each claim does, and three places present it as following ("that is why", "which is why", "has to be anticipated:"). Codex is right that the lemma does not prove it; Codex's repair is also right that it should be kept as Ren's thesis, not dropped. (c) Whose understanding, of what, over which horizon: unspecified (needs Ren).

**Repair (keeps "if growth and change are favoured" verbatim in all places, as Ren settled).**
1. `core/30_s3.md:94`, replace the bold sentence and the next one by: "**A failure that is global and irreversible cannot itself be learned from: against it, rules learned from reversible failures that share its mechanism, where such failures come first, and adoption guided by a model of the system act in time, and against what no reversible failure teaches in time only the second does** [thm∣prem]. That, and not that nothing else can integrate at this scale, is the formal reason behind the claim that **understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are favoured**. The claim goes beyond the lemma; it is the author's thesis [conj]: rules that change relative payoffs are themselves set, kept and adapted by someone, and the thesis is that at the scale of one host, under growth and change, they are kept only where those who set and keep them understand that they share one host. Compliance with a rule does not need that understanding." The sentence "Understanding is the lemma's transmission term…" and the rest of the paragraph stay.
2. `core/10_s01.md:22`, last sentence → "However carriers are grouped, selection does not favour what benefits all, and a failure that is global and irreversible cannot itself be learned from: what no reversible failure teaches in time has to be anticipated on an accurate model of the system. That is the reason for the thesis that understanding that we are one, one interconnected system with no outside, is a long-term requirement if growth and change are favoured."
3. `core/00_head.md:5` → "…integration against global failures that cannot be undone, where no reversible failure teaches it in time, has to be anticipated; hence the thesis that understanding that we are one is a long-term requirement if growth and change are favoured."
4. `core/00_head.md:17` (guide item 2, Chinese for Ren to confirm) → "全局不可逆的失败无法从它本身学到：可逆的失败来不及教会的，整合只能依准确的理解预先完成。由此本文主张：若增长与变化是我们所看重的，理解"我们是一体"、一个相互联系的系统，就是长期的必需。"
5. `core/c0_s12.md:81` → "Against such failures, where no reversible failure teaches in time, integration must be anticipated, which is the reason for the thesis that understanding that we are one, one interconnected system, is a long-term requirement if growth and change are favoured."
6. `reg/CLAIMS.md:21`: same wording as the abstract, with "(R, D; §9)". `:203` chain row 2: "global irreversible failure must be anticipated" → "what no reversible failure teaches must be anticipated; shared understanding as its requirement is the author's thesis", tags "thm; thm∣prem; conj". `:425` D36, add: "Status: the requirement is Ren's thesis [conj]; {{onegroup}} and the anticipation argument are its formal reason, not its proof (Codex I2)." `:452` item 12: add that the thesis sentence of §3.6 states its scope (setting and keeping rules, not compliance) and that the reason for the condition remains his choice between (i) and (ii).
7. `disc/01_X1.md:154` item 6: "failures that are global and irreversible cannot be learned by trial" → "…cannot be learned by trial, except through reversible failures that share their mechanism".

**Needs Ren.** (i) The tag of the requirement: [conj] (a claim about the world that could be wrong; the default above) or [val]. (ii) Its scope: "those who set and keep the rules" (default above), or broader ("enough of those they answer to", or everyone), which also bears on the item-12 reading he chooses. Neither choice changes the proved part.

**Check to add (optional, only if the text quotes the toy).** A PR extension `PR(e) precursor`: with the parameters of `i2_precursor.py`, assert that with a shared mechanism the liability comes at t ∈ (8.9, 9.1), restraint ends above 0.999 and survival is 0.749 ± 0.001; without it survival is 0.024 ± 0.001 and equals the no-rule value to 1e-9.

---

## I3. The test register is a research-design outline, not an operational preregistration (P2)

**Status: holds.** Keys: `thresholds`, C0; Test E; `reabsorb`, `dwell`.

**Where now.** `core/70_s7.md:96–102` (§7.4: Test E bullet at 99, refutation paragraph at 102); `reg/TESTS.md:112` (§4 last paragraph), `:114–116` (§5 intro), `:124` (Test E row), `:131` (Test M "held for the dwell time"), `:154` (release indicators); `core/c0_s12.md:27` (release "held for the dwell time"), `:53`.

**Reproduction (`i3_test_e.py`).** Two linear relaxation models of the groups W, C, N. Interlock (I): one shared parameter in every group's target, the loops of §7.3 at 0.4 each, and a conduct rule whose push decays at 0.25 because the thresholds were not moved (§11.4). Separate causes (S): each group has its own driver and one ordinary spillover, revenue from W funding C (0.4); a conduct rule is ordinary policy. Moving the parameter (1 → 0.8):
- In S, moving W's own driver moves W by −0.2000 and C by −0.0800 and N not at all; a conduct rule aimed at N moves only N (−0.2000). Test E as written reads "interlock" at t = 2, 30 and 60: a false positive from one spillover.
- In I, a conduct rule aimed at W moves W −0.1274 and C −0.0385 at t=2 through the loops of §7.3, and nothing above 0.01 by t=30. Before the dwell, the paper's own model fails Test E's second prediction; the prediction holds only at a horizon that the register leaves to "the dwell time", a model quantity not estimated independently.
- Estimands that discriminate: (A) persistence of a conduct rule's effect on its own target at the registered horizon, I −0.0000 against S −0.2000; (B) the parameter's cross-effect net of what its first signature mediates (ΔC − 0.4ΔW), I −0.2000 against S 0.0000, and on N, I −0.3333 against S 0.

The other points of I3 hold as stated: no test names a unit, first-stage measurement, effect size, equivalence margin or rule for missing access; a null is not the absence of the mechanism.

**Repair.**
1. `reg/TESTS.md` §5, after "confirmatory ones are marked": "*Status.* These are designs for testing mechanisms, registered in the sense that each states its prediction, its rivals and a discriminating contrary before any outcome is seen; none is yet an operational preregistration. Before a first implementation is read as confirming or refuting a mechanism, or used to activate or release a protection, the following are registered before its outcome is observed: (1) the population, unit of observation, selection rule and observation horizon; (2) the intervention, with its measured first-stage change in the model's parameters; (3) the primary outcome and its quantitative link to the model variable; (4) the rival causal models, with their cross-effects, spillovers and anticipation; (5) a minimum consequential effect, an equivalence margin for a null, and the uncertainty procedure; (6) the horizon, fixed from estimates independent of the outcome (for the dwell, of the turnover 1/(εd) of the slow variable, Section 11.4); (7) the treatment of strategic missingness, changes of measurement, substitution and spillovers, with missing access recorded as missing evidence, not as safety or as capture; (8) the inference withdrawn on a positive, a negative and an inconclusive result. The theoretical paper does not need this programme; a claim that a pilot has confirmed or refuted C0, or a decision taken on one, does."
2. `reg/TESTS.md:124`, Test E row. *What is measured:* "Signatures in W, C and N, with first-stage measures of the shared parameter and of each group's own drivers, after an intervention on one shared parameter (formula funding, enforced admission, provision) and after a conduct rule aimed at one signature (a disclosure duty), at a horizon registered in advance from independent estimates of the slow variables' turnover". *This theory predicts:* "(i) The parameter moves signatures that it reaches only through the shared parameter, beyond what the first signature it moves mediates, and the change lasts to the registered horizon. (ii) The conduct rule's effect on its own signature, and any cross-effect it carries through the loops of THEORY §7.3, has decayed by that horizon, because the thresholds were not moved ({{reabsorb}}; {{dwell}}); before it, cross-effects through the loops are expected and are evidence for neither side. This is the test of C0". *Also predicted by:* "Separate causes with ordinary spillovers (revenue that funds influence; reputation that moves financing): a parameter that reaches one group's driver moves the groups downstream of it, so that several groups move favours neither theory". *Discriminating contrary:* "Separate causes: the parameter's cross-effects are wholly mediated by the signature it reaches first, and a conduct rule's effect persists at the registered horizon".
3. `core/70_s7.md:99`, Test E bullet → "**Test E.** Moving one shared parameter should move signatures it reaches only through that parameter, beyond what the first signature it moves mediates, and lastingly; a conduct rule aimed at one signature should lose its effect, and its cross-effects, by a horizon registered in advance, because it leaves the thresholds where they were. That several groups move does not by itself discriminate: separate causes with ordinary spillovers also move several (TESTS §5). This is the test of C0."
4. `core/70_s7.md:102`, refutation: "persist unchanged over the dwell time (Section 11.4)" → "persist, within a margin registered in advance, over a horizon fixed beforehand from independent estimates of the slow variables' turnover (Section 11.4)"; "changes only its own signature over that time" → "changes, beyond what its own signature mediates, no other signature over that horizon". Same two changes in `reg/TESTS.md:112`. In Test M (`:131`), `core/c0_s12.md:27` and `reg/TESTS.md:154`, "the dwell time" → "a dwell horizon registered in advance (Section 11.4)".

**Check to add (optional, only if the text quotes the toy).** A block `TE` (derived toy, keyed C0/Test E) running `i3_test_e.py`'s two models: assert, in S, ΔW = −0.2000, ΔC = −0.0800, ΔN = 0 at t=60 under the parameter and Test E's literal reading "interlock" at t = 2, 30, 60 under the rule on N; in I, the rule on W moves W and C by more than 0.01 at t=2 and nothing by t=30; estimand A −0.0000 against −0.2000; estimand B −0.2000 against 0.0000 (each to 1e-3).

---

## I4. The short reading path compresses conditions beyond safe readability (P3, advisory)

**Status: needs Ren** (one part already fixed). Locations: `core/00_head.md:5` (abstract, one paragraph of 513 words), `:35` (怎样读), `reg/README.md` "Reading paths".

**Checked.** The abstract is still one paragraph (513 words after the internal round's additions). "Won share" is no longer a bare term in the entry route: the abstract, §1.2 items 4 and 6 and the guide say "the share of capacity that has to be won" / "必须赢得的那份能力", and §2.2 defines ω in those words (already fixed). xref's guide check is lexical (item 9 at 67% of key terms), as Codex says; it cannot check that qualifications match.

**Proposal for Ren.** Ren has accepted the length and a short paper later; Codex marks this optional. If he wants it now, the lossless step is to break the abstract into four paragraphs at existing sentence boundaries, with no word changed: (1) from "This is a prediction" to "the meta-attractor of winning."; (2) from "In specified models" to "conditioned on evaluated behaviour."; (3) from "With one host" to "change what winning confers."; (4) from "Under a standard" to the end. And README "Structure checks: … the guide against §1.2" → "… the guide against §1.2 by key terms (a lexical check: it does not test that qualifications match)". No check.

---

## I-pres. Preservation and provenance sample (integration report)

**Status: partly** (the sample holds; one propagation gap).

**Re-verified against the sources now.** "the problem is the mind not the approach" (`sources/16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md:13`) behind D13 and §5.3's [corpus] tag; "AI is a planetary technology, it should be used for all…" (`…/2026-09-26-planetary-technology-and-the-literature.md:24`) behind D17; "如果胜利者的逻辑是cancer式的，落后并不可以承受…" (`…/2026-10-03-v4-direction-cooperation.md:74`) as §3.8's first sentence, with the English as a rendering; "I would look at decay as a form of growth" (`drafts/2026-10-02-friend-conversation/transcript.md:483`), now quoted verbatim in §0 (FIXES m6); D34 and D36 as Codex found; E2 ≠ E3 kept throughout. The fourteen-loss table (`reg/LEDGER.md` §6) still has a home for each item, and xref's 32 must-stay items pass. No attribution defect.

**Gap.** The English core states once (§1.4, *Tags*) that renderings of Ren's words are the drafters' and await his confirmation; the Chinese guide, which carries several of them (e.g. 危险不在增长，而在心, D13), has no such line. **Repair:** add to the guide's 怎样读 (`core/00_head.md:35`): "导读中作者的话多是起草方的转述或中文译文，待他确认（CLAIMS §8）。" Wording for Ren to approve. No check.

---

## B1. The reference builder depends on the sibling `v6/THEORY.md` (integration report, build record; P3)

**Status: holds.** `src/refs_v62.py:76` reads `V61.parent/'v6'/'THEORY.md'`; `xref_v62.py` imports `refs_v62`, so both fail without the sibling. Reproduced in `iso/`: an isolated copy of v6.2 assembles ("no problems") but `refs_v62.py` and `xref_v62.py` raise `FileNotFoundError …/v6/THEORY.md`; with `v6/THEORY.md` supplied, xref prints "ALL CHECKS PASS". `reg/README.md` "Rebuilding" does not mention the dependency.

**Repair.** Copy the reference section of `../v6/THEORY.md` (everything after `## References`) verbatim to `src/refs_v60_base.md`; at `src/refs_v62.py:76` read that file, and if `../v6/THEORY.md` exists, check that its reference section is identical and print a warning if not. Add to README "Rebuilding": "`src/refs_v60_base.md` is the v6.0 bibliography the reference builder starts from; the build needs no other folder." Check: xref passes in an isolated copy without `../v6/` (repeat the `iso/` run).

---

## B2. Works cited only in the registers resolve to no reference list (integration report, build record; P3)

**Status: holds.** xref (current): "registers (information, not a failure): EVIDENCE cites Bowles and Polanía-Reyes 2012, Dietz, Ostrom and Stern 2003, Farrell and Newman 2019, Friedman 1953, Hague, February 2023, Index 2026, Perez et al. 2023, REAIM 2026, Seoul, September 2024 (in no reference list)". Five are real works (`reg/EVIDENCE.md:95, 219, 232, 237`); four are place or date strings misparsed as citations. The internal round resolved Khan, Kenton and Zhu by citing them in the core (FIXES E10); these five remain. Bowles and Polanía-Reyes 2012, Farrell and Newman 2019 and Friedman 1953 are in the v6.0 base; Dietz, Ostrom and Stern 2003 is already in `refs_v62.py`'s NEW list; Perez et al. 2023 is in neither.

**Repair.** In `refs_v62.py`, build a fourth list from the same entries for the works cited in the registers and in none of the three documents, and write it as "References cited only in the registers" at the end of `src/reg/EVIDENCE.md` (through a `z9`-style include or a marked block the builder replaces); add to NEW: "- Perez, E. et al. 2023. Discovering language model behaviors with model-written evaluations. *Findings of ACL 2023*. †". Add "Hague", "Index", "REAIM", "Seoul" to the parser's SKIP set (or require a surname shape before a month name). In xref, turn the register line into a failure once the list exists. Check: xref prints no register-only citation.

---

## N1. Review-status lines made stale by the Codex reviews of V6.2 (not a Codex finding; P3)

**Status: holds** (propagation for area D once the repairs land). `core/00_head.md:3` ("Reviewed at V6.1 by one model outside the drafting family (Codex); not yet reviewed by outside readers"), `core/10_s01.md:54` (*Review status*), `reg/README.md:3` ("V6.2 has not yet been reviewed outside the family"), `reg/TESTS.md:208` (§9: "One model outside the family (Codex) reviewed V6.1"), `reg/CLAIMS.md:380` ("V6.2 not yet reviewed outs[ide]"), `reg/CHANGELOG.md:77, 105`. **Repair:** after the fix round, state that Codex reviewed V6.2 twice on 4 October 2026 (snapshot f50fb6a1), where the findings and their dispositions are recorded (CLAIMS §7, `reviews/CF-*.md`, the recheck report), and keep "not yet reviewed by outside readers" and the same-family caveat. No check.

## N2. Nothing guards status propagation through the coming repairs (first review, revision order item 4; formal workflow item 6)

**Status: holds as a process gap.** `n2_tag_sync.py`: of 112 keys in CLAIMS, 93 have a tag at their declaration; eight differ only in form (e.g. `[thm]` against `[thm; num]`, or a long row-by-row tag abbreviated), none in status. So CLAIMS and the declarations agree today, but F1, F2, SA-01, SA-02, EG1 and others will change statuses, and the abstract, §1.2, the guide, Table 7.1, S13 and CLAIMS each restate them. **Repair (xref_v62.py):** for every key with a declaration tag, compare its leading status (thm, thm∣prem, def, prem, conj, val, rec, obs) with the CLAIMS tag column and fail on a difference; print the eight formal variants as information. This would have passed today and will catch a statement whose status changes without CLAIMS following. The restatements in prose (abstract, §1.2, guide, Table 7.1, S13) still need the recheck agent's reading; no lexical check replaces it.
