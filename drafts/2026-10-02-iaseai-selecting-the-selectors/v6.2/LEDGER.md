# V6.2 preservation ledger

A new version integrates the old ones; it does not replace them. This ledger records where every result and every sentence of V6.1's core now lives, what changed in content and why, what V6.1 lost or changed without recording it, and where the elements of earlier versions are. It is indexed by stable key, so a result can be found by its V6.1 number or by its key. Prepared 4 October 2026 under [V6.2-PLAN.md](V6.2-PLAN.md), from the two keymaps, the sentence check of §3, the merge and elegance notes in `planning/`, and the V6.1 review round (`../v6.1/reviews/`, the synthesis first). Numbers printed here for V6.2 are rendered from the keys at assembly, so they follow any later renumbering; V6.1 and v6.0 numbers are written out, since they are history.

## 1. How to use it

- **A V6.1 result:** look up its number or key in §2.
- **A V6.1 sentence:** look it up in [LEDGER-v62-sentences.tsv](LEDGER-v62-sentences.tsv), which lists every sentence of V6.1's core with its containment in V6.2 and, for each below 0.4, where it went or why it changed (§3).
- **What changed in content rather than place:** §4, kept apart from structural moves, as the v6.0 fidelity review asked. V6.1's own withdrawals now carry reasons in §5.
- **What the V6.1 fidelity review found lost:** §6. **What V6.1 changed without recording it:** §7. **What V6.2 deleted:** §8.
- **Earlier versions:** §9, which keeps V6.1's ledger of v6.0 with two corrections.

A section mark without a subsection, such as "§2", means that section's claim box or opening. The decisions that wait on Ren, and the renderings of his words that await his confirmation, are listed once, in CLAIMS §9 and §8; this ledger points to them.

## 2. Results, V6.1 to V6.2

V6.1 declared 91 results and V6.2 declares 112: 78 in the core and 34 in the Supplement. No key was removed or renamed. Twenty-one keys are new, six in the core and fifteen in the Supplement (Table L2). Fourteen results moved from the core to the Supplement with their keys, each leaving in the core one sentence that carries its conditions (plan §2, "side results"). Four changed kind: `slowroute` and `branches` from Theorem to Proposition, `require` and `reachable` from Proposition to Table (the assembler gained the kind `Table`, numbered in the section's counter). The sixteen equation keys and their numbers, (1)–(15) and (S1), are unchanged, so a literal "(9)" or "(14)" still points where it did. Titles, tags and the status of each result are in CLAIMS §4.

**Table L1. Every V6.1 result, in V6.1 order.** "Renumbered" means the kind and place are unchanged and an insertion before it moved its number.

| Key | V6.1 | V6.2 | Change |
|---|---|---|---|
| `cond` | Definition 2.1 | Definition 2.1 | — |
| `loopgain` | Proposition 2.2 | Proposition 2.2 | — |
| `compound` | Proposition 2.3 | Proposition 2.3 | — |
| `meta` | Definition 2.4 | Definition 2.4 | — |
| `bench` | Remark 2.5 | Remark S2.6 | to the Supplement |
| `pathgen` | Remark 2.6 | Remark 2.5 | renumbered |
| `viab` | Definition 3.1 | Definition 3.1 | — |
| `relsel` | Definition 3.2 | Definition 3.2 | — |
| `blind` | Lemma 3.3 | Lemma 3.3 | — |
| `load` | Proposition 3.4 | Proposition 3.4 | — |
| `twochan` | Proposition 3.5 | Proposition 3.5 | — |
| `boundary` | Proposition 3.6 | Proposition 3.6 | — |
| `wow` | Proposition 3.7 | Proposition 3.7 | — |
| `unequal` | Remark 3.8 | Remark 3.8 | — |
| `standprice` | Proposition 3.9 | Proposition 3.9 | — |
| `onegroup` | Lemma 3.10 | Lemma 3.11 | renumbered |
| `club` | Proposition 3.11 | Proposition 3.12 | renumbered |
| `psi` | Definition 3.12 | Definition 3.13 | renumbered |
| `capture` | Definition 4.1 | Definition 4.1 | — |
| `costq` | Assumption 4.2 | Assumption 4.2 | — |
| `influence` | Proposition 4.3 | Proposition 4.3 | — |
| `noinside` | Proposition 4.4 | Proposition 4.4 | — |
| `corrrate` | Proposition 4.5 | Proposition 4.5 | — |
| `countervail` | Remark 4.6 | Remark 4.7 | renumbered |
| `masking` | Proposition 4.7 | Proposition 4.8 | renumbered |
| `alarm` | Remark 4.8 | Remark 4.9 | renumbered |
| `certificate` | Proposition 4.9 | Proposition 4.10 | renumbered |
| `reabsorb` | Proposition 4.10 | Proposition 4.11 | renumbered |
| `pausefield` | Proposition 4.11 | Proposition 4.12 | renumbered |
| `slowroute` | Theorem 4.12 | Proposition 4.13 | kind: Theorem → Proposition |
| `join` | Proposition 5.1 | Proposition 5.1 | — |
| `dissipate` | Proposition 5.2 | Proposition 5.2 | — |
| `frontier` | Remark 5.3 | Remark 5.3 | — |
| `enforce` | Proposition 5.4 | Proposition 5.4 | — |
| `relpunish` | Corollary 5.5 | Corollary 5.6 | renumbered |
| `restraint` | Corollary 5.6 | Corollary 5.7 | renumbered |
| `wingives` | Proposition 5.7 | Proposition 5.8 | renumbered |
| `preventattack` | Proposition 5.8 | Proposition 5.9 | renumbered |
| `racehazard` | Proposition 5.9 | Proposition 5.10 | renumbered |
| `nonsum` | Lemma 5.10 | Lemma 5.11 | renumbered |
| `tempo` | Proposition 5.11 | Proposition 5.12 | renumbered |
| `coverage` | Theorem 5.12 | Theorem 5.13 | renumbered |
| `freeze` | Proposition 5.13 | Proposition 5.14 | renumbered |
| `enough` | Proposition 5.14 | Proposition 5.15 | renumbered |
| `talk` | Proposition 5.15 | Proposition 5.16 | renumbered |
| `faithful` | Proposition 6.1 | Proposition 6.1 | — |
| `delegate` | Proposition 6.2 | Proposition 6.2 | — |
| `lockin` | Lemma 6.3 | Lemma 6.3 | — |
| `delegatelock` | Proposition 6.4 | Proposition 6.4 | — |
| `retain` | Lemma 6.5 | Lemma 6.5 | — |
| `transmit` | Remark 6.6 | Remark 6.6 | — |
| `nested` | Proposition 6.7 | Proposition 6.7 | — |
| `opaquecorr` | Proposition 6.8 | Proposition S6.4 | to the Supplement |
| `topology` | Proposition 6.9 | Proposition 6.9 | — |
| `lyapunov` | Remark 6.10 | Remark S6.5 | to the Supplement |
| `homeostasis` | Proposition 6.11 | Proposition S6.2 | to the Supplement |
| `branches` | Theorem 7.1 | Proposition 7.2 | kind: Theorem → Proposition |
| `raceselects` | Proposition 7.2 | Proposition 7.3 | renumbered |
| `racepremise` | Corollary 7.3 | Corollary 7.4 | renumbered |
| `kernel` | Definition 8.1 | Definition 8.1 | — |
| `fallback` | Lemma 8.2 | Lemma 8.2 | — |
| `survassure` | Proposition 8.3 | Proposition S8.1 | to the Supplement |
| `profile` | Definition 8.4 | Definition 8.3 | renumbered |
| `durability` | Definition 8.5 | Definition 8.4 | renumbered |
| `lead` | Remark 8.6 | Remark S8.2 | to the Supplement |
| `sprint` | Remark 8.7 | Remark S8.3 | to the Supplement |
| `preventown` | Proposition 8.8 | Proposition 8.5 | renumbered |
| `insure` | Remark 8.9 | Remark S8.4 | to the Supplement |
| `assure` | Proposition 8.10 | Proposition 8.6 | renumbered |
| `verify` | Theorem 8.11 | Theorem 8.7 | renumbered |
| `overhang` | Proposition 8.12 | Proposition S8.5 | to the Supplement |
| `require` | Proposition 9.1 | Table 9.1 | kind: Proposition → Table |
| `nounilateral` | Proposition 9.2 | Proposition 9.2 | — |
| `commonfront` | Proposition 10.1 | Proposition S10.1 | to the Supplement |
| `commonfrontn` | Proposition 10.2 | Proposition 10.1 | renumbered |
| `share` | Proposition 10.3 | Proposition 10.2 | renumbered |
| `twoorders` | Remark 10.4 | Remark 10.3 | renumbered |
| `safeguards` | Theorem 10.5 | Theorem 10.4 | renumbered |
| `rivalverify` | Proposition 10.6 | Proposition S10.2 | to the Supplement |
| `participate` | Proposition 10.7 | Proposition S10.3 | to the Supplement |
| `guardian` | Remark 10.8 | Remark 10.5 | renumbered |
| `relaxtrust` | Corollary 11.1 | Corollary S11.1 | to the Supplement |
| `signal` | Proposition 11.2 | Proposition 11.1 | renumbered |
| `pausevalue` | Proposition 11.3 | Proposition S11.2 | to the Supplement |
| `readiness` | Definition 11.4 | Definition 11.2 | renumbered |
| `reachable` | Proposition 11.5 | Table 11.3 | kind: Proposition → Table |
| `tdec` | Remark S2.1 | Remark S2.1 | — |
| `thrrep` | Remark S3.1 | Remark S3.1 | — |
| `scope` | Proposition S4.1 | Proposition S4.1 | — |
| `fieldlemma` | Lemma S4.2 | Lemma S4.3 | renumbered |
| `zonesillus` | Remark S5.1 | Remark S5.1 | — |

**Table L2. Keys new in V6.2, in V6.2 order.**

| Key | V6.2 | Where |
|---|---|---|
| `twoerrors` | Remark 3.10 | core |
| `humancorr` | Proposition 4.6 | core |
| `detectlink` | Remark 5.5 | core |
| `scissors` | Proposition 5.17 | core |
| `masked` | Remark 6.8 | core |
| `thresholds` | Table 7.1 | core |
| `eqgain` | Remark S2.2 | Supplement |
| `delayosc` | Remark S2.3 | Supplement |
| `chansign` | Proposition S2.4 | Supplement |
| `gammarange` | Remark S2.5 | Supplement |
| `growprize` | Proposition S3.2 | Supplement |
| `capdyn` | Proposition S4.2 | Supplement |
| `jointscissors` | Remark S5.2 | Supplement |
| `nearlock` | Remark S6.1 | Supplement |
| `boundedopt` | Remark S6.3 | Supplement |
| `unravel` | Remark S9.1 | Supplement |
| `crosswalk` | Table S9.2 | Supplement |
| `readrule` | Remark S11.3 | Supplement |
| `dwell` | Proposition S11.4 | Supplement |
| `ratchet` | Remark S11.5 | Supplement |
| `capturebasin` | Remark S11.6 | Supplement |

The six new core keys are those plan §2 fixed. Of the fifteen Supplement keys, seven were named by the plan (`chansign`, `eqgain`, `delayosc`, `growprize`, `capdyn`, `jointscissors`, `crosswalk`); the other eight (`gammarange`, `nearlock`, `boundedopt`, `unravel`, `readrule`, `dwell`, `ratchet`, `capturebasin`) were added by the merges, as the plan allows.

## 3. Sentences, V6.1 to V6.2

The V6.1 fidelity review showed that a paragraph-level check cannot see a paragraph kept whole with its one normative sentence removed (R-v6.1-fidelity 重要5). This round therefore checks sentences.

**Method.** From `v6.2/`, after assembling: `python3 src/sentcheck.py ../v6.1/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 --all`. The script splits V6.1's core into sentences of at least eight content words, strips markup, mathematics and citations, and reports for each the share of its word trigrams found anywhere in V6.2's three documents. [LEDGER-v62-sentences.tsv](LEDGER-v62-sentences.tsv) adds, for each sentence, its V6.1 location, the V6.2 section that contains most of it (a pointer, not a proof), and, for every sentence below 0.4, a disposition read by hand against the assembled text.

**Result.** 1,060 sentences, including the 69 of the reference list, which the TSV marks separately.

| Containment | Sentences | Disposition |
|---|---:|---|
| at least 0.8 | 569 | kept nearly verbatim |
| 0.6 to 0.8 | 255 | kept, reworded in part |
| 0.4 to 0.6 | 136 | kept, reworded; best-matching section given |
| below 0.4 | 100 | read one by one (below) |

These are the counts of the build after the verification round of 4 October (`reviews/FIXES-v6.2-verify.md`, fidelity m10); the build of 4 October 15:01 gave 589, 239, 133 and 99, and the TSV's earlier count of 99 already included V61-0880 at 0.395, printed 0.40. The 100 below 0.4 were each found in V6.2 or accounted for:

| Disposition | Count | What it means |
|---|---:|---|
| reworded | 53 | the point is at the named home in other words, usually with its condition now stated |
| corrected | 17 | the sentence was wrong or overclaimed; the correct form and its source are named (§4.2) |
| moved | 10 | to the Supplement, the Discussion, a register or README, with a pointer left where needed |
| replaced | 8 | superseded by a new result, a quotation of Ren's own words, or V1's wording |
| merged | 7 | joined to another sentence that now carries both |
| duplicate | 3 | removed under one home per point; the surviving home is named |
| withdrawn | 1 | "what relative accounting does to talk is not a function of Γ", false under the unified talk result (`talk`; S2) |
| artefact | 1 | a reference entry split by the sentence splitter |

**No V6.1 point is without a findable home, and nothing needed restoring.** Three sentences fell below 0.4 after the TSV was written, and are adjudicated as the rest: V61-0452, "For classes with an irreducible lag only slowing helps", reworded at §5.3 ("For hazard classes whose manifestation window no testing shortens, $a$ is the only lever left …"); V61-0579, the claim box of §7, reworded in V6.2's box; and V61-0387, "The same recursion can be generative …", corrected, since it was false (§4.2). Two the TSV had below 0.4 are back above it, V61-0015 and V61-0075, since §0 again says the theory opposes a logic, "not growth, competition, technology or any participant". V61-0388, the pilot experiment, is reworded, not kept verbatim: V6.2's build had softened it and the verification round restored that the experiment did not support the mechanism. Of the 99 of the earlier count, 81 were already below 0.4 after the elegance pass and were adjudicated then (`planning/elegance-build-notes.md` §3); each was re-verified against the current text. The other eighteen fell below 0.4 when the front matter (abstract, guide, §0, §1, symbols) was rewritten from the final sections; most are V6.1's one-page summary sentences, now restated with their conditions (§1.2) or corrected (the price of standing, talk, membership into identity).

**Two earlier passes agree.** Against the pre-elegance snapshot (`planning/snapshots/draftA/`), 1,889 sentences were checked at 0.5 and none was lost (`elegance-build-notes.md` §2). At paragraph level, 486 V6.1 paragraphs of at least twelve words gave 437 kept, 49 rewritten and none unmatched (`planning/build-notes.md` §0).

**What the check cannot see.** The Chinese guide has no Latin words to match; it was rewritten whole from the final §1.2 and §12.1, and xref checks each of its nine items against §1.2 by a bilingual term list (front-notes §1). A string match cannot certify meaning: a sentence above 0.4 can have lost its qualifier, and one below can be kept exactly in other words. For that reason §6 checks Ren's normative sentences by keyword, which is where V6.1 lost what it lost. The V6.2 numbers in the TSV at the root are those of the build of 4 October 15:01; the regeneration against the build after the verification round, with the dispositions above, is `src/reg/LEDGER-v62-sentences.tsv`, which replaces it when copied to the root (the verification round could write only under `src/`). The keys it names are authoritative; its best-matching sections are pointers from the earlier build.

## 4. Content changes in V6.2

The review round's corrections became the spine rather than caveats (plan §1). The direction was the same as at V6.1: write the conditions back into the statements; withdraw no thesis.

### 4.1 Restated: raised, sharpened or made exact, content kept

- **The selection pressure of winning** is three conditions plus the reflexive closure (Definition 2.1; Definition 2.4); its strength near equal standing is the *structural* loop gain, with the prize and conduct fixed, and where rivals respond the same form holds with an equilibrium decisiveness (Proposition 2.2(4); Remark S2.2). Γ decides whether a gap grows; the Perron root Λ* decides how fast (Remark S2.1).
- **The levers act channel by channel** (Proposition S2.4): sharing and diffusion lower the gain in every channel; provision not won in the contest where decisiveness rises less than in proportion to the stock (capacity); correction where it rises at least in proportion (rule support). "Trees for capacity, correction for rule support, sharing and openness for all" (§2.2).
- **Compounding prices standing** (Proposition 3.9, retitled): the general form compares reinvestment's relative return with its common return; with a fixed prize the objective narrows wherever the discounted gain is positive, with a prize proportional to capacity exactly where leads compound. The two errors, of the held self-model and of the working objective, are told apart (Remark 3.10): each actor computes correctly; the game is wrong.
- **Ψ**, "locally rational and systemically false", is now the triple: individually rational where compounding prices standing, collectively self-defeating, false as a doctrine about nature (Definition 3.13; §3.8; §12.4).
- **Capture has two directions** (Definition 4.1): accommodation of the practice and barriers against its challengers, the second through unequal incidence (Lemma 3.3(2)); see §7(a).
- **The rate law has two halves** (Proposition 4.5(2)): sufficient at any speed of adaptation, necessary where capacity tracks its selected level; correction resting on human capacity that delegation erodes needs $+w\delta_h$, and capture that makes delegation look safe is hysteretic (Proposition 4.6).
- **The silent route** is a Proposition with the premises its proof uses, (reach), (a), (d), (e), and a clock version; (b) and (c) are the mechanism that makes (e) credible (Proposition 4.13, "Silent crossing when capture precedes evidence").
- **Masking:** the bound on masking by the evaluated model must come from evidence its behaviour does not control (Remark 4.9); masked divergences are the fourth class, for which coordination is necessary and not sufficient (Remark 6.8).
- **Enforcement** is stated per deviation, with exclusive or independent breakouts (Proposition 5.4); the detection link $p_d=1-\upsilon(T_{\rm dec})$ joins it to the verification threshold (Remark 5.5); what restraint needs reads "changing the premise", not "keeping $p_d$ low" (Corollary 5.7(a)).
- **The scissors** turn on one pivot, the share of capacity that has to be won; each arm is proved, a reduced joint model closes the first two together [num], and their co-movement in the world is C0 [conj] (Proposition 5.17; Remark S5.2).
- **The contest branches** are a Proposition tagged branch by branch, with the nuclear analogy in prose [obs] (Proposition 7.2); near parity is where the summed price of standing is highest, where a lead discourages the follower (§7.2).
- **The thresholds table** integrates Part II (Table 7.1): nine thresholds, one inequality each, the result that proves it, what pushes toward danger, the lever that reverses it, and the side of (14) it moves. The S7 matrix gives every arrow its intervention, what is held fixed, the model that signs it and the interface left unproved.
- **"Gain"** in §7.1's driver is now **"the drive"**, so that it is not read as Γ.
- **The requirements** (Table 9.1, now [def, with support]): R3a in its two halves; R4's exception exact; R8 split into R8a (compliance) and R8b (neutrality among those who comply); "admission reaches only to release" moved from the exceptions to the limits, beside internal deployment and open weights; R9 new, pending Ren (CHANGELOG, *Deviations*; CLAIMS §9).
- **Admission** reads "before consequential deployment, internal deployment included", everywhere (§6.4, §6.6, §12.1).
- **Broad E1** is any competitive game that concentrates, in labour, finance and persuasion as much as over shared conditions, judged by the game and not the act; broad E1 is the scope and narrow E1 the first step (§0; §6.6; §11.3; §12.1). Narrow E1 is scoped to "decisions whose delegation would lock with near certainty" (Proposition 6.4; Remark S6.1).
- **The judgment** is in tiers sorted by the kind of justification: tier 1(a) on every reading of the cruxes, tier 1(b) withdrawn only where a named crux is measured favourable, tier 2 prepared now and activated by a mechanism committed in advance on indicators estimated by certified correctors, tier 3 compared and not settled, with coercive restriction of frontier inputs under three conditions of its own (Ren's decision). Tier 3's reasons are the reversibility asymmetry and the irreversible failure every path shares (§12.1).
- **The transition:** stages became parallel tracks, slowest first; readiness has residence and a decision rule (Definition 11.2; Remark S11.3); dwell depends on the depth of lock-in and is bounded only by a lineage that can recruit (Proposition S11.4); graduated steps reach only as a ratchet (Remark S11.5); the requirements of a reachable path are a table (Table 11.3); "AI lacks saturation" is conditional (§11.5).
- **The generative loop** has its institutional forms and closes on "fear deepens"; a fifth strand, pace, is the dual of regulator lag, and the third strand the dual of the drive; six functions joined the form table (pace; human decision authority; standing of those affected; due process against correctors; disclosure of conversion data; alignment and control research) (§10.4, §10.5).

### 4.2 Corrected

Each correction names what was wrong. Sources: the synthesis of the V6.1 reviews (§四), the merge notes `planning/merge-notes/Uxx.md` §2 (derivations), and `checks_v62.log`.

*Part I.*
- Proposition 2.2(3): the price formula holds only on $0\le\Gamma_\delta<1$, with the net payoff reinvested; beyond it the price is infinite (a cusp), not negative (Codex 1; PD).
- Proposition 3.9: "where the loop gain is high, every forward-looking actor" and "compounding manufactures the relative objective" overclaimed. With rivals responding the price at parity is amplified 1.05 to 7.9 times and a laggard's falls toward zero; with a growing prize the sign turns on $(1-\beta)r$ against one. The plan's "with a fixed prize this always holds" fails at $\Gamma_\delta=0$; the statement says "wherever $\Gamma_\delta>0$" (Codex 1; Math-O M1; Math-F I1; Adv-F F1; U03 §2.3).
- The sign of correction: in a ratio channel faster depreciation leaves Γ unchanged without diffusion and raises it with diffusion; only in a level channel does correction lower it (Codex 2; Sys I1; CH).
- Remark S2.1: the growth factor is $1+(d_K+\delta_f)(\Gamma-1)$ (Math-F m5; Math-O m12; TD).
- Proposition 2.3(2): the cap must be strictly below $K^\ast$; diffusion is a third inflow not tied to rank, beside sharing and provision; with diffusion alone the laggard can stall, at 0.16 of the cap, not 0.36 (Codex 3; CE).
- Lemma 3.3(3): bistability needs $s(0)>c>s(1)$, a sanction continuous and strictly decreasing; compliance survives at equality and prevails only where every inequality is strict (U03 §2.1–2).
- Lemma 3.3(2) and R8: equal incidence is needed for neutrality among those who comply, not for compliance; the per-type sanction condition is exact within a type and sufficient across types (Codex 5; CI(h); checks-notes finding 3).
- Proposition 3.5: of the common channel's four effects, two fall as θ falls and two rise; V6.1 listed all four as falling (U03 §2.4).
- Lemma 3.11: the total selection term is non-positive under every payoff-monotone rule; the two level terms separately only under affine fitness (Codex; Math-O M4; PR).
- Identifying θ: the two observable ratios read a true θ of zero as −0.5 and −0.43; V6.1 attached −0.43 to the wrong one (U03 §2.14).
- Assumption 4.2 and Proposition 4.5: the floor is a per-unit cost floor $f$, and a true lump sum only delays; (2) holds only for $f=0$ (a falling positive floor can end cultivation for good: Codex 4; FF); (3) states its initial condition and says the level *rises*; "necessary iff liminf" is "if" (U04 §2.1); capture follows the certificate's failure by 8 to 85 periods, not 12 to 75 (U04 §2.3).
- Proposition 4.12: the frozen-share pause length is exactly $\ln(G/S(x_p))/(\varepsilon d)$; "at least" and "plus the time to repay the lock-in" do not apply to a frozen share (Sys I4).
- V6.1's §4.6 (line 363 of its THEORY.md): "success funding correctors it cannot control is selected in the same way" was false; the repair is the whole-system account (Remark 2.5; §4.6) (Codex).
- Proposition 5.4(1): $p_d$ is per deviation; (5) needs exclusive breakouts ($q\le\frac12$) or reads $q(1-q)$ for independent ones; the example now has $P<v<C$ ($q=0.045$), V6.1's being kept in S5 for its different point (Math-O; ES).
- R4's exception "$D<C$" was false; the exact form is $(1-\delta)g\le\delta(C-D)$, that is $\bar p_d\ge1$ (ES(e): $\bar p_d=0.864$ with $D<C$) (U05 §2.2; U09).
- Corollary 5.6: the printed example is a weak equilibrium, strict under small symmetric perturbations; the mirror argument needs the whole continuation, start state included, to be exchangeable; role assignment is equilibrium selection (Math-F I5; Math-O m4; Codex 6; CR).
- Proposition 5.16(2): "allies form blocs" is not proved; among three or more relative accounting multiplies the conflict by $n/(n-2)$, a factor that fades with $n$, and blocs are a reading [conj] (TK).
- Remark 5.3: the switch condition omitted the private cost $c_y$ and had the wrong sign (U05 §2.6).
- Proposition 5.17: 0.99 is 0.9495 (0.9793 for the second case); "D and g grow faster than C−v" is "by a common factor relative to C−v", since the term is $D-C$ (Math-O; U05 §2.4; NB, JX).
- Proposition 4.13: (b) and (c) were idle in the proof and the title oversold it (Math-F I3; Math-O m6).
- Theorem 5.13: (variety grows) was idle in the proof; it is motivation, not a premise.

*AI.*
- Proposition 6.4: $p=1$ restored; "strict equilibrium" only with $q_L=1$; for $p<1$ the interior equilibrium needs a decreasing ratio (Codex 7; DL).
- Proposition 6.7(2): the matched unsafe variant is a premise; a tax can be paid from a lead only against rivals that lack the developer's other advantages (Ali m3; U06 §2.c).
- Proposition S6.4: V6.1's example was not summable; the exact condition is $\sum(1-c_{b,t})<\infty$ and $\sum h_{c,t}<\infty$, with a summable example (SM(11)).
- Proposition S6.2(3): an equilibrium at every $t$, with the tail bound "at most 3/16" from $t=5$, which is the union bound (SM(12)).
- Proposition 6.9: the row-sum certificate is sufficient, not necessary, and certifies nothing about independence; independence is measured two ways (miss correlation; adversarial control evaluations) (Ali; SM).
- Remark S6.5: 7.4 and 37.3, not 7.5 and 37.5 (AL(6.10)).
- Proposition 6.2(1): the equality case was missed; Remark S6.3 needs $c<1$.

*Parts II–IV.*
- Proposition 7.3(2) needs conditional independence; V6.1 omitted it (U07 §2.1).
- Proposition 8.6(2) needs $T-P+F>0$; Proposition 8.5(1)'s bound tends to one only where $s_P\Phi^R>0$; Theorem 8.7(3) is an identity [def] plus a conjecture [conj] (U08 §2).
- Theorem 10.4(1): "viable if, in addition, the host stays above its floor while the load falls" was circular; it is a margin condition on both kinds of host, and "the first computable instance of the correctable kernel" is an instance of the boundary of viable parameters for one fixed strategy (Math-O M5; U10).
- Proposition 10.2(2): both sharing conventions, $n$ and $n-1$; (3): non-convertibility stabilizes only with provision, not with diffusion (U10 §2.1–2). Proposition S10.1's proof: equality iff $n=1$ or $c=0$.
- Proposition 11.1(2): V6.1's clause held only among pure-strategy equilibria; with prior trust short the receiver restrains after the step with probability at most $c_{\mathsf R}/\Pi_{\mathsf R}$ in every equilibrium (U11 §2.1; TR).
- Corollary S11.1(3): covert preparation needs $\upsilon F\ge(1-\upsilon)\Delta V$; Remark S11.3(2): Wald's bounds need the true likelihood ratio (U11 §2).
- §12.1: "each of the design's failures has a reversal" holds for all but two (the fallback's escalation; capture of custody) (U12 §2.c).
- Tags: branch I′ [obs]; "cannot justify" in Corollary 7.4 [val]; Theorem 8.7's last clause [conj]; Table 9.1 and Table 11.3 [def, with support]; the margin of Theorem 10.4(1) [num].

*Evidence and attribution* (EVIDENCE's corrections list and D4-evidence-notes, Verification, are the full record).
- Jones (2024), a misreading introduced at V6.1: his result turns on the curvature of utility; "a race is preferred iff $h<g_r-g_p$" is this paper's derivation under linear utility (§8.1; S8; EV11).
- Bueno de Mesquita et al.: the result concerns a firm that commits first to slowing; V6.1's "a leader … can lead rivals to slow" was not carried.
- "The frontier has not changed hands" depends on the measure; leads are short (EV5; D4 B1–B3). T5 is "inferred from the structure of harm, not measured"; T2 and §8.3(b) rest on two developers' frameworks and one unreviewed study.
- Corpus keys: 讲理/讲赢 is keyed to `alignment-selection` and `jian-and-wenyan`, the five endgames to `selfishness-spiral`, 力之所及 to `shengsheng`; the reform dilemma's 2025 date is marked unverified (fidelity 重要6; X1).
- S14: the holdout example's numbers do not reproduce; under (6) they are 0.033 and 0.975, not 0.015 and 0.989; V6.1's "talk among three raises the receiver's value from 1/4 to 1/2", which no block computed, is replaced by T3(b) (s13-notes).
- Proposition S10.3's figures come from the v4.5 K7 block, not as V6.1 attributed them (U10 §2.6).
- Assembly: V6.1 printed a kind word twice before two numbers (§8.3(b); Table 9.1, row R1), because a source wrote the kind before a key that prints its own; the assembler now catches doubled kinds in every document, registers included.

### 4.3 Withdrawn in V6.2, each with its reason

| Withdrawn (V6.1 wording) | Reason | Now |
|---|---|---|
| "Every forward-looking actor"; "compounding manufactures the relative objective" | Holds only where reinvestment's relative return exceeds its common return; strategic and growing-prize cases differ | Proposition 3.9; "prices standing" (plan §8.3) |
| "The same number prices standing for every actor" (§2 box; §1.2) | The price is a separate result with its own condition; off parity a laggard's price falls toward zero | Proposition 3.9; Remark S2.2 |
| "Among three or more actors, what relative accounting does to talk is not a function of Γ either" | False: the effective bias falls in θ, and θ is θ_Γ | Proposition 5.16; S2's table |
| "Allies form blocs" as a result; "forms blocs" in §1.2 and the guide | Not proved | blocs are a reading [conj] |
| "Taken together, characterize" (§7 box) | Overclaim: the signatures are [obs]; their co-movement is C0 [conj] | §7 box |
| "On any reading of the cruxes" for all of tier 1 | False for items that turn on C2, on $q_L$ or on C6/C8 | tier 1(a) and 1(b) |
| "Mostly accepted by those who favour regulated competition" (tier 1) | False of shared provision and divisible gains | tier 1(b): "not accepted across camps" |
| "The certificates can be measured before the design is relied on" (tier 3, reason 1) | Row sums have never been measured | the reversibility asymmetry, §12.1 (i) |
| Coercive restriction of frontier inputs as a tier-2 activation | The paper cannot sign its net effect, and it had no trigger of its own | tier 3, under three conditions (Ren's decision) |
| R4's exception "$D<C$" | False (ES(e)) | $(1-\delta)g\le\delta(C-D)$ |
| Theorem 10.4(1)'s viability clause; "first computable instance of the correctable kernel" | Circular; overclaimed | margin condition; one boundary of viable parameters |
| V6.1's example as summable (Proposition S6.4) | It is not summable | a summable example; V6.1's kept as the comparison |
| "Locally rational and systemically false" | Less exact than what is shown | Ψ's triple |
| "Shared flourishing" (§6.6, §12.4) | Generic phrase, not Ren's | V1's content |
| "Its force comes from the combination of stick and carrot" (§8.3(d), X8) | Reads the strategy by its own account | "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact" |
| "Defensive realism with one more variable" (§7.2, X1) | Equates the theory with one branch of realism | nearest neighbour, extended and departed from (§7.2) |
| "The cost is large" (E2) | Unsupported, and against the sentence before it | "can be large (crux C10)" |
| "AI-assisted correction can win this race" | Race grammar in the theory's own voice | "can keep pace" |
| "We are part of a larger process of becoming" | Membership, where Ren says identity | §0 and §12.4; §6 below |

### 4.4 Declined, with reasons (plan §9)

| Proposal | Decision and reason |
|---|---|
| Compress the core to 12–20k words now (Adv-F F6; Adv-O I8) | Deferred to a separate venue paper. Ren's direction: no cap, the best paper first. |
| A single integrated model as a theorem | Taken instead as a reduced joint model [num] (Remark S5.2), held for outside review. |
| A change of subtitle | The title is Ren's. |
| A calibration of Γ in the core (Adv-O I1) | Illustrative ranges in Remark S2.5, with "Γ is not estimated" (§2.2). |
| A polycentric redesign as a requirement (Adv-F F5) | Kept as an option: a candidate of tier 3 and of X10. |
| Moving §3.7 and §3.8 to X1 | They carry Ren's ruling and the definition of the logic opposed; they stay in the core. |
| ASTRA's seven layers in the core | One sentence in TESTS Study 4 says which layers V6.2 carries and which remain. |
| The meta-loop toy in the core (Sys m3) | A suggestion in the TESTS research programme, with block ML's numbers; it is a toy. |
| Entry barriers restored as this theory's own prediction | Test B keeps entry barriers without appropriability as the discriminating contrary; their mechanism is folded in through unequal incidence and the barrier direction of capture (§7(a)). |

## 5. V6.1's nine withdrawals, with reasons

The V6.1 fidelity review (次要1) found that only one of V6.1's nine withdrawals gave a reason, and that two were restatements. Each now has its v6.0 location and a reason; the two restatements are reclassified.

| v6.0 wording and location | Status | Reason, and where it lives now |
|---|---|---|
| "That the lemma leaves only this route is a theorem" (§3.7, after the one-group lemma, Lemma 3.10) | Withdrawn | The lemma shows that no level of selection supplies what benefits all; it does not exclude learning from sub-catastrophic failures, coalitions of the harmed or design, so "only this route" was asserted, not proved (R-v6.0-math I3). §3.6: anticipation is required against failures that cannot be undone, and that it can succeed "has no biological precedent … is a conjecture" [conj]. |
| "Power-seeking emerges where advantage compounds" (§10.8) | **Restated** | The sentence went beyond Turner et al. (2021), whose result concerns optimal policies, not trained ones (R-v6.0-evidence). Its content is weak incarnation: the outer loop selects which divergences are paid to remove (§6.4; Proposition 6.7), with strong incarnation conditional. |
| Theorem 5.16(2): "durable restraint requires common custody" as the only route, and "after custody only stage equilibria remain" | Withdrawn | The enforcement result gives a disjunction: $p_d$ can be kept low also by not building the decisive class, by detection faster than breakout, or by a defence that dominates (R-v6.0-math). Now Corollary 5.7(a)–(c) and Corollary 7.4. |
| "Those are toy settings, but they are measurements" (§6.5) | Withdrawn | The oversight success rates are derived from fitted scaling curves by the authors' theory, not measured (R-v6.0-evidence). §6.5 says "derived from fitted scaling curves in four games (Engels et al. 2025)". |
| "Only the third [lever] changes the direction of the pressure" (§8.4, after Proposition 8.6) | **Restated** | "Only" was too strong: a liability above the private advantage also reverses selection (Proposition 3.4; Theorem 10.4). The exact content is Proposition 10.2: sharing shrinks the pressure; non-convertibility stabilizes equal standing only with provision not won in the contest. |
| "Oneness is a gain in one case and a requirement in another" (§5.5, after Theorem 5.16) | Withdrawn | It slid "we are one" back to a weight on others, θ = n−1, which the paper itself shows is a club (X-v6.0-fidelity-opus-check 重要1a). Oneness is a property of the system on every branch; what changes between branches is the institutional form its recognition requires (§7.2). |
| "The thresholds of Remark 5.9 are lower bounds" | Withdrawn | The direction needed $D\ge O^\ast$, the opposite of the setting (R-v6.0-math). The zones are an illustration of the binary game (Remark S5.1); the general result is Proposition 5.4. |
| The discounting result attributed to Fudenberg and Koh (2026) (§7.9) | Withdrawn | Their paper does not contain it (R-v6.0-evidence, from the abstract). It is cited for what it shows, a pacing equilibrium under transparency (§8.3(c); X8); the discounting result is this paper's derivation beside Jones (2024) (§4.2 above). |
| Carried from v6.0's own list: the bistable model's numbers and slope condition; "what is shared is the prize of decisive standing"; "θ = n−1 is oneness" | Withdrawn | Respectively: deferred to research, as a slow variable with possible bistability and hysteresis (TESTS Study 2; block ML a toy); the positional part cannot be divided (§10.2); oneness is a property of the system, and θ = n−1 among contestants is a club (Proposition 3.12). |

## 6. The fourteen losses found in V6.1, and their homes

R-v6.1-fidelity 重要5 listed fourteen points that V6.1 lost inside paragraphs its ledger called kept or rewritten. Every one now has a home.

| v6.0 location (V6.1 ledger status) | Lost in V6.1 | Home in V6.2 |
|---|---|---|
| §0-p03 (kept 0.74) | "…and makes those without it fall behind" | §0 *The game, not the act*: an instrument every contestant adopts "pushes down whoever lacks it"; §6.6: "everyone's use of it makes those without it fall behind" |
| §0-p04 (kept 0.59) | "Decay and renewal belong to growth." With it (重要2), V6.1's "part of a larger process": membership, where Ren says identity | §0 and §12.4 "we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth" [corpus: shengsheng, 2026-10-02]; §12.4 also quotes Ren's spoken sentence verbatim; guide 意义 衰败与更新，也属于它的生长 (renderings: D in CLAIMS §8) |
| §9.3-p02 (rewritten 0.25) | Broad E1 in labour, finance and persuasion; "a use that helps one person is still an instrument in a game" | §6.6 (criterion, Ren's line [corpus: alignment-selection], three layers); §0; Proposition 6.4's Scope names the other mechanism |
| §10.1-p01 (rewritten 0.17) | Broad E1 is the scope, narrow E1 the first step | §1.2 item 9; §11.3 [corpus: alignment-selection, 2026-09-26]; §12.1 *The scope*; guide 判断 |
| §10.2-p01 (check, deleted as duplicate) | "Understanding that we are one … is a long-term requirement" in the one-page summary | Abstract; §1.2 item 2, with the narrow self as the target; guide item 2; §12.4 |
| §7.12-p03 (kept 0.51) | "Falling behind cannot be survived, and every actor has reason first to oppose the logic itself" | §3.8, first sentence, with Ren's Chinese |
| Remark 7.13, third reason (insure) | Insurance accepts the frame of the contest | §8.3(f); Remark S8.4; X8 |
| §8.7-p01 (kept 0.51) | Philosopher-kings, priestly classes, enlightened stewards, new universities: the rejected guardians | Remark 10.5, §10.4 |
| §8.2-p01 (kept 0.46) | The generative loop's institutional forms; the degenerative loop's closing "fear deepens" | §10.4, both loops in the book's words [corpus: shengsheng, 2026-07-14 第十四章], ending 恐惧愈深 |
| §5.1-p23 (rewritten 0.24) | "Expansion is an anaesthetic for the winning model … a self-replicating economy … carries the same switch with it" | §5.1, beside Remark 5.3 [corpus: meta-attractor]; the toy in S5 |
| §4.3-p04 (rewritten 0.23) | "Growing understanding without executive authority may change nothing" | §4.3; §12.2 *The theory of change*; §1.4 *What is not claimed*; S13 |
| §10.2-p02 (kept 0.43) | Meadows's hierarchy; "the paradigm can change only if the system is understood" | §12.2 *The hierarchy and the thresholds*, beside the threshold account (§7(c), for Ren) |
| §5.4-p04 (rewritten) | Preference falsification (Kuran 1995); counter-performativity, a model making itself false (MacKenzie 2006) | Kuran: §5.4 and X1; MacKenzie: §11.2, the home of counter-performativity, to which §0's last clause points |
| v6.0 reviews; V6.1 plan §三.6 | ASTRA's layers and the nine-step chain: "one sentence" promised, not written | TESTS Study 4: which layers V6.2 carries and which remain (endogenous domains, the ecology of practices) |

xref's must-stay check (32 items) still passes, and these fourteen were checked by keyword in the assembled documents. CLAIMS §7.2, row D1, records the same dispositions from the reviews' side.

## 7. V6.1 changes that V6.1 did not record

The fidelity review (次要2, 次要3) found three content changes and one departure from the approved plan that V6.1 made without recording them, and one promised item it did not do; V6.1 also left one attribution open. Each is recorded here with what V6.2 did.

**(a) Entry barriers.** v6.0 §2.7 predicted two directions of capture: captured rules "raise entry barriers against challengers. The second direction is easy to overlook". V6.1 Test B listed support for rules that raise rivals' costs as a prediction *against* the theory, while §10.1 still said success cannot buy the right to "exclude entrants". The narrowing kept Test B discriminating against entry-barrier theory (Stigler 1971), but it hid Ren's second loop, "adopt or be out". V6.2 restores the barrier inside the theory: Definition 4.1 names both directions (accommodation; barriers), unequal incidence is how a rule becomes a barrier against challengers (Lemma 3.3(2)), and Test B (ii) predicts support for rules keyed to the carrier that fall on challengers. The discriminating contrary is now narrower: entry barriers *without appropriability*, in which incumbents would support correction keyed to no one wherever it burdens rivals more. Plan §9 declined only the undifferentiated form.

**(b) The hysteresis prediction.** v6.0 predicted that withdrawing a rule that changed selection does not fully restore behaviour; V6.1 replaced it with Test D's "two phases". V6.2 restores it: Test D is "Two phases, and hysteresis", with the hold growing with the age of capture unless a recruitable lineage persists (Proposition S11.4, [num: DW]), and with sunk-cost path dependence (Pierson) and ordinary policy reversal as the contraries.

**(c) Meadows, and the threshold reading. For Ren.** v6.0 §10.2 read Meadows (1999) as saying that a system whose goals and paradigm are unchanged re-absorbs a change of parameters, and that "the paradigm can change only if the system is understood". V6.1 replaced this, without recording it, by "interventions that move a parameter without crossing its threshold are re-absorbed, and those that cross it are not". V6.2 §12.2 states both and their relation: the paper's levers sit in Meadows's ranking (loops #7 and #8, information #6, rules #5, self-organization #4, goals #3); moving sharing, provision and convertibility across their thresholds is Meadows's own exception, a parameter that sets off a higher place; the paradigm decides which parameters are moved and whether they are held, and it changes only if the system is understood. "Both accounts stand: the paradigm is the highest place, and it acts through thresholds." This gives the paradigm the role of deciding which parameters move and how long they are held, which Ren should confirm or reject (CLAIMS §9, item 2; D33).

**(d) Definition 2.1.** The approved V6.1 plan had four conditions (relative selection, convertibility, decisiveness, reflexive closure); V6.1 wrote three conditions with the closure stated separately and did not record it. V6.2 keeps three plus closure, by Ren's decision, and the CHANGELOG records the departure.

**(e) ASTRA.** The V6.1 plan promised one sentence on ASTRA's layers; it was not written. It is now in TESTS Study 4 (§6 above, last row).

**(f) A result shared with another of the author's papers.** Proposition 4.12 also appears as Proposition 10 of the author's paper of 28 September 2026 (`../../2026-09-28-capability-outruns-correction/`). V6.1 listed the attribution as not done; S4 now notes the overlap and points here. Which paper states it first, and how each cites the other, is the author's to settle.

## 8. Deleted in V6.2, with survivors

Deleted means removed from the documents, not moved. Each deletion was a duplicate, version narrative, or a figure no block could reproduce; corrected and withdrawn statements are in §4.

| Deleted (V6.1) | Reason | Survivor |
|---|---|---|
| §2.4 "The rest of Part I follows one chain" and its chain | One home per point (plan §8.1) | Abstract, guide, §1.2, §12.4; §2.4 ends in a hand-off |
| §7.1's restatement of the chain as four loops in series, with V6.1's glosses | Duplicate; glosses replaced by Ren's own lines | §7.1 *Four loops* in Ren's words, with their formal correspondence; S7 *The four loops, formally* |
| §5.4's second quotation of 讲理/讲赢 | One home | §3.8 (`psi`), referred to from §5.4 |
| §5.5 "In the corpus: change the basin, then add speed" | One home | §2.3 (Remark 2.5); §12.4 |
| §10.4's 和实生物，同则不继 | One home | §3.7; §10.4 points to it |
| The participation–independence feasibility sentence, stated twice | Duplicate | §10.3, once |
| §8.2's four marks of the generative direction; §12.4's six-item list | Superseded by G1–G7, which contain every member | §8.2 (canonical), §12.4 (identical wording and order) |
| §12.2 "(compare Powell 1991)" | One home | §3.5, with the high-convertibility point and Remark 3.10 |
| §1.4's reading paths other than thirty minutes | Belong to the README | README |
| S11's note that the 10.45 → 3.81 dwell effect "has not been reproduced" | Superseded: reproduced | Proposition S11.4 [num: DW] |
| S14's "talk among three raises the receiver's value from 1/4 to 1/2" | No block computed it | S14, T3(b)'s facts |
| §10.5's coercive fallback "treated exactly as Section 8.3 treats prevention", and §8.3(f)'s and X8's statements of coercion's conditions | One home for coercion's three conditions | §12.1 tier 3; X10's hard case |
| The "Today" column of the readiness table | A dated reading belongs with the evidence | X11 *Readiness, read today*; §11.4 *Where things stand* keeps the summary, in D4 C1's verified wording |

## 9. Earlier versions

V6.1's ledger of v6.0 is kept below, with two corrections the V6.1 fidelity review asked for: the sentence that opened its list of deletions, "Only true duplicates and version narrative were deleted", is removed, since §6 above shows that more was lost; and its record that "a self-replicating economy carries the switch with it" lived in SUPPLEMENT S5 is corrected, since S5 never had it. Results are cited there by their V6.1 numbers, written out; their V6.2 numbers are in Table L1. Its list of corrections cites results by their v6.0 numbers, as V6.1 recorded them; keys are added.

### 9.1 Numbering crosswalk, v6.0 to V6.1 (V6.1 numbers)

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

### 9.2 V6.1's content changes

**Restated at V6.1** (raised to the right level, content kept):
- "One pressure" → interconnected conditions with one loop gain at their core (Definition 2.1, Proposition 2.2); single-factor covariation a research question.
- The dilemma of decisiveness → the enforcement condition and what restraint needs where breakouts are possible (Proposition 5.4, Corollary 5.6, Corollary 7.3).
- "We are one" → three jobs done through understanding; "oneness is what these requirements are requirements of" (THEORY §3.7, §7.2).
- "Integration must be anticipatory" → against global, irreversible failures integration must be anticipated, while reversible failures can be learned by polycentric trial (Lemma 3.10).
- "Universal constraints are invisible to selection" → common constraints survive with equal incidence and sanctioned evasion (Lemma 3.3).
- The nested reward loop → under the alignment-tax premise, with weak and strong incarnation (Proposition 6.7; THEORY §6.4).
- Requirements R1–R8 → requirements by kind of support (Proposition 9.1).
- Talk under opposed objectives → two parties silenced, three or more forming blocs (Proposition 5.15).
- Carried from v6.0: "one root" → interconnected conditions; "growing self" → what selection at any level cannot supply; "re-absorption" → the exact condition of Proposition 4.10; "three zones" → an illustration (Remark S5.1).

**Corrected at V6.1** (v6.0 numbers, keys added):
- The enforcement bound (v6.0 Proposition 5.7; `enforce`), exact only at $D=C$; its numerical check was circular.
- Corollary 5.8's scope for $n\ge3$ (`relpunish`).
- Remark 5.3 (`compound`): $\chi$ was a sharing parameter; caps protect equal standing only locally without inflow not tied to rank; the growth variant.
- Proposition 5.10(3) (`wingives`): the renege gain is $\beta\Omega(n-1-\theta)/(n-1)$ when the promise was to the others.
- Proposition 3.11(2) (`club`): blocs carry shared loss $s\ell$.
- Section 3.4: the identification of $\theta$ is confounded by the perceived share $\psi$ (V6.2 corrects which ratio reads −0.43; §4.2).
- Lemma 7.11 (`fallback`): the conditioning step of the proof; proof by coupling.
- Proposition 6.1(5) (`faithful`): the cost-exponent condition.
- Proposition 6.4(2) (`delegatelock`): at least one equilibrium always exists (V6.2 restores $p=1$; §4.2).
- Proposition 6.9 (`topology`): row sums do not certify independent errors.
- Section 4 (`influence`, `costq`): the size threshold, splitting factor and concentration measure depend on how the cost of influence scales; "AI lowers the cost of control" stated as $[H_\gamma]$.
- Theorem 8.2(1) (`safeguards`): a margin is needed on pointwise harsher threshold hosts.
- Proposition 4.10 (`pausefield`): the frozen-share threshold is 0.68, not 0.8; dwell times exact.
- Remark 4.7(4) (`alarm`): the autocorrelation result is exact for static affine masking.
- Proposition 8.6(3) (`share`): convertibility stabilizes only with provision not won in the contest.
- Definition 8.10 (`kernel`): the correctable kernel is a discriminating kernel.
- Evidence and citations: the corrections listed at the end of EVIDENCE.md and in DISCUSSION X11. Carried from v6.0: "sharing reverses selection"; the national genealogy; the claim that 21,096 cases "agree with direct evaluation".

**Withdrawn at V6.1:** the nine items, with reasons, are in §5.

### 9.3 Restored at V6.1

Content that the fidelity review of v6.0 and its Opus check found lost or flattened, restored in V6.1: the relational self and 大同, with 力之所及 and 共开共续 under it (THEORY §3.7, §10.1); coupling rising with power, a conjecture and crux C11 (§3.4); $\theta_g$ (Proposition 5.2); the reform dilemma (§10.4); the four loops, as loops (§7.1); the W→C→N loop (§7.3); the definition of an unbounded relative objective (§3.8); the five endgames (§3.6); the sample-size hedge (§3.6; §10.5); the offense–defense quadrant (§7.2; DISCUSSION X1); "continuation acts on one lever" (§5.3); the narrative–value frame mechanism (§5.4); the four levels of epistemic closure (§4.1; TESTS Study 4); the positive roles of AI in the generative loop (§6.6); why "meta-attractor" and not "generator functions" (§2.3); the credit to the first version for the distinctions among concentration, capture, field capture, damage, collapse and closure (§4.1). The paragraph check of §6 restored a further dozen points in this pass, among them "a cartel is cooperation", "our aligned AI is us", the pseudo-solution label, the registered prediction, that readiness does not require private motives to change first, and the mechanism index (SUPPLEMENT S7). (§4.1 here is V6.1's section; in V6.2 the four levels of epistemic closure are in §4.4 and TESTS Study 4.)

### 9.4 Deleted at V6.1, with survivors

V6.1 recorded these deletions, each a duplicate or version narrative with a survivor. The list was not all that V6.1 lost: §6 gives the fourteen points the V6.1 fidelity review found missing inside paragraphs recorded as kept.

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

### 9.5 The paragraph check of V6.1

v6.0's body was cut into 641 paragraph units. For each, a script found the best-matching section of V6.1 by word-trigram containment and coverage of content words: 251 units are kept nearly verbatim (containment at least 0.4), 321 are rewritten at a destination that shares their content words, and 69 were flagged for reading. Every flagged unit was read; the 321 rewritten units were not, which is why V6.2 checks sentences (§3). Most are proofs rewritten in the Supplement's notation, appendices moved to registers, summaries deleted as duplicates, or the old forms of corrected results; twelve were points dropped in compression, now restored (§4). The table, with each unit's destination and disposition, is [LEDGER-units.tsv](LEDGER-units.tsv). A string match cannot certify meaning; the table guards against silent loss, it does not prove preservation.

**Must stay in the core.** At V6.1 an automated check (`xref_v61.py`) confirmed that each of the 32 items the structure plan listed as belonging in the core appear in THEORY.md, and `xref_v62.py` confirms the same 32 in V6.2: success is not contribution; selection removes the balanced; the primitive is selection, not greed; the three ingredients and the winner's rule; the meta-attractor and why the name; 讲理 and 讲赢; "the locally winning strategy has taken the name of rationality"; molochlization; change the basin, then add speed; another planet; federations; "we are one" as a property of the system, not a weight; oneness is not sameness, 和实生物，同则不继; the relational self and 大同; judge the game, not the act; growth is not the danger, the mind is; affirmative meaning; prediction shared before coordination; survival as the minimum; AI's two problems; form by function, not the individual–collective axis; 力之所及，责之所在; 共开、共续、不夺共续; trees; trust as an outcome; no optimizing out of an optimization trap; the reform dilemma; the guardian test; no better guardian; the five endgames; the sample-size hedge; E2 is not E3.

### 9.6 v5.2 to v6.0, and the elements of earlier versions

**v5.2 to v6.0** (carried from v6.0's ledger; the right-hand numbers are v6.0's, mapped to V6.1 by §9.1 and to V6.2 by Table L1): D1.1 → Def 2.5; P1.2 → Prop 3.5(1)–(2); P1.3 → Props 6.1(4), 5.2(2)–(3); P1.4 → Prop 5.4; P1.5 → Prop 8.6; D1.6 → Def 7.12; D2.1, D2.2, L2.3 → Defs 3.1, 3.2, Lemma 3.3; P2.4, P2.5, R2.6, R2.7 → Props 3.4, 3.6, Remarks 3.7, 3.8; D3.1 → Def 2.2; R3.2 → Remark 2.3; D3.3–R3.9 → Def 4.1–Remark 4.7; P3.10–T3.13 → Props 4.8–4.10, Thm 4.11; P4.1 → Prop 6.1; P4.2 → Prop 3.9; R4.3 → Remark 6.6; L4.4 → Lemma 5.5; P4.5, D4.6 → Prop 9.4, Def 9.5; R4.7 → Remark 7.13; P5.1–P5.2 → Props 5.1–5.2; P5.3–L5.6 → Prop 6.2–Lemma 6.5; P5.7–P5.9 → Props 5.11–5.13; P5.10–P5.13 → Props 6.8–6.11; P5.14 → Prop 7.9; T5.15 → Thm 5.15; R6.1–D6.8 → Remark 7.1–Def 7.8; D7.1 → Def 8.1; T7.2–P7.8 → Thm 8.2–Prop 8.9; P8.1, C8.2 → Prop 9.1, Cor 9.2; P8.3 → Prop 5.14(2); P8.4 → Prop 9.3; P8.5 → Prop 9.6.

**Elements of earlier versions, and where they are now.**

| Element | Origin | In V6.1 | In V6.2 |
|---|---|---|---|
| The primitive is selection, not greed; selection removes the balanced | Author's corpus (2024) | THEORY §2.1 | §2.1 |
| What is won is kept, used to compete for more, and the competing never stops | Author's corpus (2024, 2026) | §2.2 | §2.2 |
| Four loops; paradigm convergence | Author's corpus | §7.1 | §7.1 |
| Appropriability asymmetry: the returns to control can be kept, those to correction cannot | v3 plan | §4.2 | §4.2 |
| The reform dilemma and the guardian test | Author's corpus (dated 2025, not verified against an original); conversation of 2026-10-02 | §10.4 | §10.4, Remark 10.5 |
| What the environment rewards, the mind promotes | Author's corpus (2025) | §3.4 | §3.4 |
| Being selected by a rule versus helping reproduce it; the persistent entity can be a way of succeeding | v1 | §2.3 | §2.3 |
| A system can retain abundant information while losing the ability to let it change course | v1 | §5.4 | §5.4 |
| Keystones, and a window that closes | v1, v2 | §4.5 | §4.5; §11.4 *Windows* |
| Dependence and capture reinforce each other; crisis as a field of accumulation | v1 | §7.1 | §7.1 |
| Captured evaluation keeps everyone from seeing | v3.1 | §4.4 | §4.4 (Proposition 4.8, Remark 4.9) |
| A single winner restrains; the failure is in the race | v3.1 | DISCUSSION X8 | §8.3(d); X8 |
| The premise that motivates the race | v4.0 | §7.2 | §7.2, Corollary 7.4 |
| Survival as the minimum requirement | v4.5 | §0 | §0; §1.3 (V2) |
| Production directed at need has a point of enough; trees | v4.5 | §5.3, §10.1 | §5.3, Proposition 5.15; §2.2; §10.1 |
| Trust is an outcome, not a prerequisite | Author's corpus (2025) | §11 | §11.1; §1.2 item 9 |
| A self-replicating economy carries the switch with it | Author's corpus | not present: V6.1 recorded SUPPLEMENT S5, which never had it | §5.1, beside Remark 5.3 [corpus: meta-attractor] |
| One cannot optimize one's way out of an optimization trap | Author's corpus | §10 | §10 claim box |
| Unity without differentiation becomes another totalizing attractor | Author's corpus (2026) | §3.7, §10.4 | §3.7; §10.4 |

**The nine layers of the earlier theory** (V6.1 sections, the same in V6.2 except as Table L1 shows): host and shared conditions (§3.1); first-order selection (§3.2–3.5); the contest in AI (§5.1); correctors selected by what they correct (§4); observation and masking (§4.4, §5.4); failure and survival (§5.3, §8.1); trust and verification (§8.3(g), §10.3, §11.1–11.2); cooperation (§10); transition (§11).

### 9.7 Notation, v6.0 to V6.1

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

V6.2's renames are listed chapter by chapter in SUPPLEMENT S0, and every symbol of the core's table in *Symbols and labels*.