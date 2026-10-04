# V6.1 preservation ledger

A new version integrates the old ones; it does not replace them. This ledger records where every numbered result and every paragraph of v6.0 now lives, what changed in content, what was restored, what was deleted and why, and where the elements of earlier versions are. It is indexed by stable key, so that a reader can look up a result by its v6.0 number or by its key. Prepared 3 October 2026 under [V6.1-PLAN.md](../V6.1-PLAN.md) and the structure plan `../v6/v61-planning/Q1-structure-opus.md`.

## 1. How to use it

To find a v6.0 result, look up its number in §2. To find a v6.0 paragraph, look up its unit identifier (`L-60-§x.y-pNN`, paragraph NN of v6.0 section x.y) in [LEDGER-units.tsv](LEDGER-units.tsv). To see what changed in content rather than place, read §3. Structural moves (moved, compressed, merged) are kept apart from content changes (restated, corrected, withdrawn), as the fidelity review of v6.0 asked.

## 2. Numbering crosswalk, v6.0 to V6.1

| v6.0 | Key | V6.1 |
|---|---|---|
| Def 2.1 | `cond` | Definition 2.1 |
| Def 2.2 | `meta` | Definition 2.4 |
| Rem 2.3 | `bench` | Remark 2.5 |
| Rem 2.4 | `pathgen` | Remark 2.6 |
| Def 2.5 | `psi` | Definition 3.12 |
| Def 3.1 | `viab` | Definition 3.1 |
| Def 3.2 | `relsel` | Definition 3.2 |
| Lem 3.3 | `blind` | Lemma 3.3 |
| Prop 3.4 | `load` | Proposition 3.4 |
| Prop 3.5 | `twochan` | Proposition 3.5 |
| Prop 3.6 | `wow` | Proposition 3.7 |
| Rem 3.7 | `thrrep` | Remark S3.1 |
| Rem 3.8 | `unequal` | Remark 3.8 |
| Prop 3.9 | `boundary` | Proposition 3.6 |
| Lem 3.10 | `onegroup` | Lemma 3.10 |
| Prop 3.11 | `club` | Proposition 3.11 |
| Def 4.1 | `capture` | Definition 4.1 |
| Prop 4.2(1)–(3) | `influence` | Proposition 4.3 |
| Prop 4.2(4) | `scope` | Proposition S4.1 |
| Prop 4.3 | `noinside` | Proposition 4.4 |
| Prop 4.4 | `corrrate` | Proposition 4.5 |
| Rem 4.5 | `countervail` | Remark 4.6 |
| Prop 4.6 | `masking` | Proposition 4.7 |
| Rem 4.7 | `alarm` | Remark 4.8 |
| Prop 4.8 | `certificate` | Proposition 4.9 |
| Prop 4.9 | `reabsorb` | Proposition 4.10 |
| Prop 4.10 | `pausefield` | Proposition 4.11 |
| Thm 4.11 | `slowroute` | Theorem 4.12 |
| Prop 5.1 | `join` | Proposition 5.1 |
| Prop 5.2 | `dissipate` | Proposition 5.2 |
| Rem 5.3 | `compound` | Proposition 2.3 |
| Prop 5.4 | `racehazard` | Proposition 5.9 |
| Lem 5.5 | `nonsum` | Lemma 5.10 |
| Rem 5.6 | `frontier` | Remark 5.3 |
| Prop 5.7 | `enforce` | Proposition 5.4 |
| Cor 5.8 | `relpunish` | Corollary 5.5 |
| Rem 5.9 | `zonesillus` | Remark S5.1 |
| Prop 5.10 | `wingives` | Proposition 5.7 |
| Prop 5.11 | `tempo` | Proposition 5.11 |
| Thm 5.12 | `coverage` | Theorem 5.12 |
| Prop 5.13 | `freeze` | Proposition 5.13 |
| Prop 5.14 | `talk` | Proposition 5.15 |
| Thm 5.15 | `branches` | Theorem 7.1 |
| Thm 5.16(1)(2) | `restraint` | Corollary 5.6 |
| Thm 5.16(3) | `racepremise` | Corollary 7.3 |
| Prop 6.1 | `faithful` | Proposition 6.1 |
| Prop 6.2 | `delegate` | Proposition 6.2 |
| Lem 6.3 | `lockin` | Lemma 6.3 |
| Prop 6.4 | `delegatelock` | Proposition 6.4 |
| Lem 6.5 | `retain` | Lemma 6.5 |
| Rem 6.6 | `transmit` | Remark 6.6 |
| Prop 6.7 | `nested` | Proposition 6.7 |
| Prop 6.8 | `opaquecorr` | Proposition 6.8 |
| Prop 6.9 | `topology` | Proposition 6.9 |
| Rem 6.10 | `lyapunov` | Remark 6.10 |
| Prop 6.11 | `homeostasis` | Proposition 6.11 |
| Rem 7.1 | `lead` | Remark 8.6 |
| Prop 7.2 | `raceselects` | Proposition 7.2 |
| Prop 7.3 | `sprint` | Remark 8.7 |
| Prop 7.4 | `preventattack` | Proposition 5.8 |
| Prop 7.5 | `preventown` | Proposition 8.8 |
| Prop 7.6 | `overhang` | Proposition 8.12 |
| Thm 7.7 | `verify` | Theorem 8.11 |
| Def 7.8 | `durability` | Definition 8.5 |
| Prop 7.9 | `survassure` | Proposition 8.3 |
| Prop 7.10 | `require` | Proposition 9.1 |
| Lem 7.11 | `fallback` | Lemma 8.2 |
| Def 7.12 | `profile` | Definition 8.4 |
| Rem 7.13 | `insure` | Remark 8.9 |
| Thm 8.2 | `safeguards` | Theorem 10.5 |
| Prop 8.3 | `nounilateral` | Proposition 9.2 |
| Prop 8.4 | `commonfront` | Proposition 10.1 |
| Prop 8.5 | `commonfrontn` | Proposition 10.2 |
| Prop 8.6 | `share` | Proposition 10.3 |
| Rem 8.7 | `twoorders` | Remark 10.4 |
| Prop 8.8 | `rivalverify` | Proposition 10.6 |
| Prop 8.9 | `participate` | Proposition 10.7 |
| Def 8.10 | `kernel` | Definition 8.1 |
| Prop 8.11 | `enough` | Proposition 5.14 |
| Rem 8.12 | `guardian` | Remark 10.8 |
| Prop 9.1 | `assure` | Proposition 8.10 |
| Cor 9.2 | `relaxtrust` | Corollary 11.1 |
| Prop 9.3 | `signal` | Proposition 11.2 |
| Prop 9.4 | `pausevalue` | Proposition 11.3 |
| Def 9.5 | `readiness` | Definition 11.4 |
| Prop 9.6 | `reachable` | Proposition 11.5 |
| App A field lemma | `fieldlemma` | Lemma S4.2 |
| Thm 5.16 | `dilemma` (retired) | Corollary 5.6; Corollary 7.3 |
| Def 8.1 | `changesel` (retired) | merged into Proposition 9.1 |

## 3. Content changes

**Restated** (raised to the right level, content kept):
- "One pressure" → interconnected conditions with one loop gain at their core (Definition 2.1, Proposition 2.2); single-factor covariation a research question.
- The dilemma of decisiveness → the enforcement condition and what restraint needs where breakouts are possible (Proposition 5.4, Corollary 5.6, Corollary 7.3).
- "We are one" → three jobs done through understanding; "oneness is what these requirements are requirements of" (THEORY §3.7, §7.2).
- "Integration must be anticipatory" → against global, irreversible failures integration must be anticipated, while reversible failures can be learned by polycentric trial (Lemma 3.10).
- "Universal constraints are invisible to selection" → common constraints survive with equal incidence and sanctioned evasion (Lemma 3.3).
- The nested reward loop → under the alignment-tax premise, with weak and strong incarnation (Proposition 6.7; THEORY §6.4).
- Requirements R1–R8 → requirements by kind of support (Proposition 9.1).
- Talk under opposed objectives → two parties silenced, three or more forming blocs (Proposition 5.15).
- Carried from v6.0: "one root" → interconnected conditions; "growing self" → what selection at any level cannot supply; "re-absorption" → the exact condition of Proposition 4.10; "three zones" → an illustration (Remark S5.1).

**Corrected:**
- The enforcement bound (v6.0 Proposition 5.7), exact only at $D=C$; its numerical check was circular.
- Corollary 5.8's scope for $n\ge3$.
- Remark 5.3: $\chi$ was a sharing parameter; caps protect equal standing only locally without inflow not tied to rank; the growth variant.
- Proposition 5.10(3): the renege gain is $\beta\Omega(n-1-\theta)/(n-1)$ when the promise was to the others.
- Proposition 3.11(2): blocs carry shared loss $s\ell$.
- Section 3.4: the identification of $\theta$ is confounded by the perceived share $\psi$.
- Lemma 7.11: the conditioning step of the proof; proof by coupling.
- Proposition 6.1(5): the cost-exponent condition.
- Proposition 6.4(2): at least one equilibrium always exists.
- Proposition 6.9: row sums do not certify independent errors.
- Section 4: the size threshold, splitting factor and concentration measure depend on how the cost of influence scales; "AI lowers the cost of control" stated as $[H_\gamma]$.
- Theorem 8.2(1): a margin is needed on pointwise harsher threshold hosts.
- Proposition 4.10: the frozen-share threshold is 0.68, not 0.8; dwell times exact.
- Remark 4.7(4): the autocorrelation result is exact for static affine masking.
- Proposition 8.6(3): convertibility stabilizes only with provision not won in the contest.
- Definition 8.10: the correctable kernel is a discriminating kernel.
- Evidence and citations: the corrections listed at the end of EVIDENCE.md and in DISCUSSION X11. Carried from v6.0: "sharing reverses selection"; the national genealogy; the claim that 21,096 cases "agree with direct evaluation".

**Withdrawn:**
- "That the lemma leaves only this route is a theorem."
- "Power-seeking emerges where advantage compounds."
- Theorem 5.16's "durable restraint requires common custody" as the only route, and "after custody, only stage equilibria remain".
- "Those are toy settings, but they are measurements" (the figures are derived).
- "Only changing what winning converts into reverses the direction."
- "Oneness is a gain in one case and a requirement in another."
- "The thresholds of Remark 5.9 are lower bounds."
- The discounting result attributed to Fudenberg and Koh (2026).
- Carried from v6.0: the bistable numbers and slope condition; "what is shared is the prize of decisive standing"; "$\theta=n-1$ is oneness".

## 4. Restored

Content that the fidelity review of v6.0 and its Opus check found lost or flattened, restored in V6.1: the relational self and 大同, with 力之所及 and 共开共续 under it (THEORY §3.7, §10.1); coupling rising with power, a conjecture and crux C11 (§3.4); $\theta_g$ (Proposition 5.2); the reform dilemma (§10.4); the four loops, as loops (§7.1); the W→C→N loop (§7.3); the definition of an unbounded relative objective (§3.8); the five endgames (§3.6); the sample-size hedge (§3.6; §10.5); the offense–defense quadrant (§7.2; DISCUSSION X1); "continuation acts on one lever" (§5.3); the narrative–value frame mechanism (§5.4); the four levels of epistemic closure (§4.1; TESTS Study 4); the positive roles of AI in the generative loop (§6.6); why "meta-attractor" and not "generator functions" (§2.3); the credit to the first version for the distinctions among concentration, capture, field capture, damage, collapse and closure (§4.1). The paragraph check of §6 restored a further dozen points in this pass, among them "a cartel is cooperation", "our aligned AI is us", the pseudo-solution label, the registered prediction, that readiness does not require private motives to change first, and the mechanism index (SUPPLEMENT S7).

## 5. Deleted, with survivors

Only true duplicates and version narrative were deleted.

| Deleted | Reason | Survivor |
|---|---|---|
| §1.6 section by section | Duplicate | THEORY §1.2 |
| §1.5 "It claims five things" | Duplicate | THEORY §1.2, §1.4 |
| §4.7 and §5.6 section summaries | Duplicate | Scope lines of each result; THEORY §1.4; §4.6 |
| §10.2 ten-link chain | Duplicate | THEORY §1.2; CLAIMS §5 |
| §10.8 paragraphs 1–3 | Duplicate | THEORY §12.4 |
| §9.2 first paragraph | Duplicate | THEORY §0 |
| Repeated "coordination succeeds where unilateral virtue fails" | Duplicate, and needed conditions | THEORY §3.2, with incidence and evasion; §9 |
| Twenty-one numbered references in the Chinese summary | A barrier to cold readers | THEORY §1.2 carries the section numbers |
| "In the first version of this model…" (§4.5) | Narrative | SUPPLEMENT S4; CHANGELOG |
| "This is the correct form of an earlier claim…" (§5.5) | Narrative | CHANGELOG |
| "Two further predictions carry over from earlier versions" (§10.5) | Narrative; the predictions are kept | TESTS §5 |
| File paths in the status line and §6.4 | Narrative | README; SUPPLEMENT S15 |

## 6. The paragraph check

v6.0's body was cut into 641 paragraph units. For each, a script found the best-matching section of V6.1 by word-trigram containment and coverage of content words: 251 units are kept nearly verbatim (containment at least 0.4), 321 are rewritten at a destination that shares their content words, and 69 were flagged for reading. Every flagged unit was read. Most are proofs rewritten in the Supplement's notation, appendices moved to registers, summaries deleted as duplicates, or the old forms of corrected results; twelve were points dropped in compression, now restored (§4). The table, with each unit's destination and disposition, is [LEDGER-units.tsv](LEDGER-units.tsv). A string match cannot certify meaning; the table guards against silent loss, it does not prove preservation.

**Must stay in the core.** An automated check (`xref_v61.py`) confirms that each of the 32 items the structure plan listed as belonging in the core appears in THEORY.md: success is not contribution; selection removes the balanced; the primitive is selection, not greed; the three ingredients and the winner's rule; the meta-attractor and why the name; 讲理 and 讲赢; "the locally winning strategy has taken the name of rationality"; molochlization; change the basin, then add speed; another planet; federations; "we are one" as a property of the system, not a weight; oneness is not sameness, 和实生物，同则不继; the relational self and 大同; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; prediction shared before coordination; survival as the minimum; AI's two problems; form by function, not the individual–collective axis; 力之所及，责之所在; 共开、共续、不夺共续; trees; trust as an outcome; no optimizing out of an optimization trap; the reform dilemma; the guardian test; no better guardian; the five endgames; the sample-size hedge; E2 is not E3.

## 7. Earlier versions

**v5.2 to v6.0** (carried from v6.0's ledger; the right-hand numbers are v6.0's, mapped to V6.1 by §2): D1.1 → Def 2.5; P1.2 → Prop 3.5(1)–(2); P1.3 → Props 6.1(4), 5.2(2)–(3); P1.4 → Prop 5.4; P1.5 → Prop 8.6; D1.6 → Def 7.12; D2.1, D2.2, L2.3 → Defs 3.1, 3.2, Lemma 3.3; P2.4, P2.5, R2.6, R2.7 → Props 3.4, 3.6, Remarks 3.7, 3.8; D3.1 → Def 2.2; R3.2 → Remark 2.3; D3.3–R3.9 → Def 4.1–Remark 4.7; P3.10–T3.13 → Props 4.8–4.10, Thm 4.11; P4.1 → Prop 6.1; P4.2 → Prop 3.9; R4.3 → Remark 6.6; L4.4 → Lemma 5.5; P4.5, D4.6 → Prop 9.4, Def 9.5; R4.7 → Remark 7.13; P5.1–P5.2 → Props 5.1–5.2; P5.3–L5.6 → Prop 6.2–Lemma 6.5; P5.7–P5.9 → Props 5.11–5.13; P5.10–P5.13 → Props 6.8–6.11; P5.14 → Prop 7.9; T5.15 → Thm 5.15; R6.1–D6.8 → Remark 7.1–Def 7.8; D7.1 → Def 8.1; T7.2–P7.8 → Thm 8.2–Prop 8.9; P8.1, C8.2 → Prop 9.1, Cor 9.2; P8.3 → Prop 5.14(2); P8.4 → Prop 9.3; P8.5 → Prop 9.6.

**Elements of earlier versions, and where they are now.**

| Element | Origin | In V6.1 |
|---|---|---|
| The primitive is selection, not greed; selection removes the balanced | Author's corpus (2024) | THEORY §2.1 |
| What is won is kept, used to compete for more, and the competing never stops | Author's corpus (2024, 2026) | §2.2 |
| Four loops; paradigm convergence | Author's corpus | §7.1 |
| Appropriability asymmetry: the returns to control can be kept, those to correction cannot | v3 plan | §4.2 |
| The reform dilemma and the guardian test | Author's corpus (2025); conversation of 2026-10-02 | §10.4 |
| What the environment rewards, the mind promotes | Author's corpus (2025) | §3.4 |
| Being selected by a rule versus helping reproduce it; the persistent entity can be a way of succeeding | v1 | §2.3 |
| A system can retain abundant information while losing the ability to let it change course | v1 | §5.4 |
| Keystones, and a window that closes | v1, v2 | §4.5 |
| Dependence and capture reinforce each other; crisis as a field of accumulation | v1 | §7.1 |
| Captured evaluation keeps everyone from seeing | v3.1 | §4.4 |
| A single winner restrains; the failure is in the race | v3.1 | DISCUSSION X8 |
| The premise that motivates the race | v4.0 | §7.2 |
| Survival as the minimum requirement | v4.5 | §0 |
| Production directed at need has a point of enough; trees | v4.5 | §5.3, §10.1 |
| Trust is an outcome, not a prerequisite | Author's corpus (2025) | §11 |
| A self-replicating economy carries the switch with it | Author's corpus | SUPPLEMENT S5 |
| One cannot optimize one's way out of an optimization trap | Author's corpus | §10 |
| Unity without differentiation becomes another totalizing attractor | Author's corpus (2026) | §3.7, §10.4 |

**The nine layers of the earlier theory**: host and shared conditions (§3.1); first-order selection (§3.2–3.5); the contest in AI (§5.1); correctors selected by what they correct (§4); observation and masking (§4.4, §5.4); failure and survival (§5.3, §8.1); trust and verification (§8.3(g), §10.3, §11.1–11.2); cooperation (§10); transition (§11).

## 8. Notation

| v6.0 | V6.1 |
|---|---|
| $O_i$ (objective) | $J_i$, to avoid O1–O4 |
| $\chi$ as the winner's share, $\rho$ as reinvestment (Definition 2.1, Remark 5.3) | $1-\beta$ and $\kappa_c$; $\chi$ only for appropriability in §4 |
| $\delta$ as depreciation or damping | $d_K$, $d_u$, $d_v$; $\delta$ only for discounting |
| $K$ (host capacity) | normalized to 1 |
| $h$ (host load) | $h_V$ |
| $\Theta$ (value of restraint, §3.5) | $\Upsilon$; $\Theta$ only for the justified range |
| $\Gamma$ in Proposition 5.13 | local $\varrho$; $\Gamma$ is the loop gain |
| $R_{ij}$, $s_i(\mathcal C)$ | $G_{ij}$, $G_i(\mathcal C)$ |
| $\mathsf D$, $\mathsf E$, $\mathsf S$ (domains) | subscripts dev, ev, rule |
| $\beta_{\rm in}$, $\beta_{\rm out}$, $\beta_{\rm model}$ | $m_{\rm in}$, $m_{\rm out}$, $m_{\rm model}$ |
| $g$, $\alpha$, $b$, $g_c$ (rate law) | $\alpha_{\rm ctl}$, $\alpha_{\rm cor}$, $\alpha_B$, $\alpha_{uc}$ |
| $\mathcal K$ (human capacity) | $\mathcal M$ |
| $\delta_c$, $\beta_c$ (lock-in) | $\delta_h$, $\varrho_h$ |
| $L_t$ (shared loss) | $\ell_t$ |
| $S_N$, $S^A$ (survival) | $\Phi$ |
| Standard D | the protection standard |
| Tags [D] [V] [T] [T∣A] [A] [O] [N] [C] [R] | [def] [val] [thm] [thm∣prem] [prem] [obs] [num] [conj] [rec] |
| H0–H5; P1–P3; (X), (U), (φ), (φ-s); U1–U4; $(\mathrm{A_G})$ | (reach), (a)–(e); (decisive), (fast), (unsaturated); (variety grows), (coverage lags), (residual floor), (shared failure); legible, overrulable, exercised, resourced; (hazard–damage link) |
| T-A to T-K; Studies A–E | Tests A–M and Γ; Studies 1–5 |