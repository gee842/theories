# V6.2 elegance pass: integration build notes

4 October 2026. This is the integration step after the elegance merges of U02–U12 (unit notes: `planning/elegance-notes/Uxx.md`). Before any edit, `src/`, THEORY, SUPPLEMENT and DISCUSSION were backed up to the session scratchpad (`.../scratchpad/backup/`). The v6.2 folder is untracked in git, so that backup is the only copy of the pre-integration state.

## 1. Build and fixes

**First assembly** (`python3 src/assemble_v62.py`): "no problems", with 93 core and 35 supplement declarations. U11 moved `relaxtrust` and `pausevalue` to S11, which accounts for 95/33 becoming 93/35.

**Cross-unit checks beyond the assembler's own:**
- **Forward use.** None. Every key that moved to the Supplement (`relaxtrust`, `pausevalue`) is cited in the core only after S-numbering, and supplement keys have no order constraint. The core contexts read correctly: "(Corollary S11.1)", "(Proposition S11.2)", Table 11.3's Reachability row.
- **Kind words.** All `Kind {{#key}}` uses in core, supp, disc and reg were checked against `keymap.json`: 0 mismatches. Doubled kind names: none (assembler).
- **Hard-coded result numbers** outside markup in src: none.
- **Homes another unit relies on** (U12 open issue 2, U06 open issue 2, U11 open issue 7). All present:
  - §11.3: narrow E1's domain ("use of force and nuclear command"), the drilled fallback, the evidence channel, and the tactical-domain clause;
  - §11.4: the non-recruiting control [num: DW];
  - §10.5: the R9 row;
  - §4.4: channels that observe actions directly;
  - §6.6: broad E1's domains ("labour, finance and persuasion");
  - §8.3(e)/(f): "read as a lead being kept" and denial raising the weight on winning;
  - X8: "Read across paths".
- **U03 open issue 2** (`supp/07_S7.md` l.24 citing "Section 3.5"): already fixed in src (it reads "S3").

**Edits made in src (two files, the smallest edits that remove a contradiction):**
1. `src/core/d0_symbols.md`, *Labels*. The line was stale against the merged sections:
   - "R1–R8 requirements" became "R1–R9 requirements (R3 and R8 split into a and b)";
   - "C0–C11 empirical cruxes and N1–N3 normative ones" became "C0–C13 empirical cruxes (C3a, C3b; C9a–C9d) and N1–N4 normative ones";
   - "Stages 1–5" became "Tracks 1–5" (U11 open issue 3);
   - "G1–G7 marks of the generative direction" was added, since §8.2 uses those labels throughout.

   **If Ren rejects R9**, revert "R1–R9" together with the removals listed in merge notes U09. Symbol renames and additions (U08 open issue 6) are left to the front-matter phase, which owns this file.
2. `src/supp/13_S13.md`, row *Loop gain and breakout probability*. "with $T_{\rm dec}$ set by $\Gamma$" contradicted Remark S2.1 ("In the interfaces of S13 it is $\Lambda^\ast$, not $\Gamma$, that sets $T_{\rm dec}$") and §2.2. It now reads "with $T_{\rm dec}$ set by $\Lambda^\ast$; $\Gamma$ decides only whether the gap grows (Remark S2.1)" (U02 open issue 5). No other S13 or S15 text was touched; both are scheduled for the next phase (see §5).

**References.** `cd src && python3 refs_v62.py` regenerated the three `z9_refs.md` files: THEORY 103, SUPPLEMENT 89 and DISCUSSION 92 entries.
- THEORY dropped: Baker 2025; Burns 2023; Calvano 2020; Fish 2024; Greenblatt, Denison et al. 2024; Hubinger 2024; Ikenberry 2001; Kindleberger 1973; Korbak 2025; Langosco 2022; MacDiarmid 2025; Meinke 2024; Olson 1993; Rankin 2007; Schoen 2025; Turner and Tadepalli 2022. All are now cited only in companions.
- SUPPLEMENT gained: Alchian 1950; Baker; Calvano; Fish; Greenblatt, Denison et al.; Guan 2025; Hubinger; Korbak; Langosco; MacDiarmid; Meinke; Rankin; Schoen; Turner and Tadepalli; Turner et al. 2021.

**Second assembly:** "no problems", 93/35.

**`python3 xref_v62.py`:**
- Citation coverage: 103/103, 89/89 and 92/92 both ways.
- Must-stay phrases: 32/32.
- Named states or firms in core prose: none.
- Guide items 9 against §1.2 items 9: match.
- **Only failure:** guide items 1 (33%) and 9 (33%) against §1.2. This is expected, since the front matter is rewritten next.
- **Information only, not failures** (unchanged by this pass; for the register phase):
  - EVIDENCE cites works in no reference list: Bowles and Polanía-Reyes 2012, Dietz, Ostrom and Stern 2003, Farrell and Newman 2019, Friedman 1953, Perez et al. 2023.
  - The same EVIDENCE list contains parser artefacts: "Butler et al. (2025", "Hague, February 2023", "Index 2026", "REAIM 2026", "Seoul, September 2024".
  - TESTS cites Kenton et al. 2024, Khan et al. 2024 and Zhu 2026, which are in no reference list.

## 2. Whole-core preservation against draftA

Command: `python3 src/sentcheck.py planning/snapshots/draftA/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.5`
- Result: 1,889 sentences checked, 80 below 0.5. That is the 79 adjudicated by the units, plus the symbols label line this pass corrected.
- The same sentences appear in the unit notes; each disposition below was re-verified against the final assembled text, since units ran in parallel and a "duplicate of §N" could have been cut in §N.
- **No sentence was lost, and nothing needed restoring.** Every cross-unit home named by a unit still exists.

| # | c | draftA sentence (start) | Disposition (verified home) |
|---|---|---|---|
| 1 | .25 | The other redirects those resources into expansion… | Merged, §2.1: "One spends resources maintaining it; the other redirects them into expansion while using what others maintain." |
| 2 | .42 | The channels add only because one win share feeds every stock… lobbying… | Merged into the Proposition 2.2 Scope: "must reinforce and be fed through one win share … a stock fed by a separate decision, such as lobbying bought from profits, is not a term of the sum". The "add because" clause is Proposition 2.2(1). |
| 3 | .43 | MP; both held for outside review] (Remark S2.2). | Tag fragment. The tag stands unchanged in the Proposition 2.2 Scope ("[num: MP; both held for outside review]"). |
| 4 | .35 | If it stays fixed while capacity grows without depreciation… | Reworded, §2.2: "S2 gives the condition of (1) date by date when capacity grows under it without depreciation". The formula is in S2 *Growth variants* (a). |
| 5 | .47 | Which levers lower the gain. The levers of (2) do not act alike… | Reworded, §2.2: "The levers act channel by channel, according to how decisiveness responds to the level of a stock (Proposition S2.4) [thm]". |
| 6 | .36 | Practices that produce more publications… | Reworded, §2.3: "Practices that publish more receive more funding and students and are more widely copied." |
| 7 | .00 | The conditional form keeps its conditions in the sentence: | Merged, §2.3: "In conditional form, *recursive selection creates…*". The statement is unchanged. |
| 8 | .22 | One concept covers the mechanism and its generative dual… | Duplicate: Definition 2.4 ("each claim in this paper says which it concerns"), and §2.3 *Why "meta-attractor"* ("and a generative counterpart"). |
| 9 | .45 | The sanction keeps a rule; equal incidence keeps a rule from becoming a weapon. | Reworded, §3.2: "The sanction keeps the rule; equal incidence keeps it from becoming a weapon." Also S9, R8b. |
| 10 | .23 | That is the second direction in which success reaches the selectors… | Merged, §3.2: "success has reached the selectors by a second direction (Definition 4.1)". The two directions are named in Definition 4.1 (§4.1). |
| 11 | .22 | A common liability … reverses selection once it exceeds the private advantage. | Merged, §3.2: "A common liability works on the conduct instead, making it pay less". The reversal duplicates Proposition 3.4's headline and Theorem 10.4 ("iff liability exceeds the private advantage by a margin"). |
| 12 | .44 | TH], and why identification fails exactly where shared harm goes unseen. | Moved: S3, *Proof of Proposition 3.5, and measuring θ*, last sentence. The core proof pointer keeps "and where it fails". |
| 13 | .45 | Patience cuts both ways: it strengthens repetition and raises the price of standing. | Kept as a clause in §3.5, and in §7.1 ("with a fixed prize"). |
| 14 | .45 | The two errors of Remark 3.10 divide the work… | Duplicate. Remark 3.10's last sentence: "Understanding acts on the first error directly, and on the second only through agreement to change what winning confers (Section 12.2)". Also §12.2 ¶1. |
| 15 | .12 | Held as self-model and doctrine, the logic has three parts. | Duplicate of Definition 3.13's first sentence and Ψ1–Ψ3. |
| 16 | .29 | Delegation that erodes human capacity erodes the corrector too [thm]. | Merged into the §4 box ("the required rate rises by the weighted rate of erosion [thm]"). Proposition 4.6's title is "Delegation erodes the corrector"; §6.3 has "erodes the corrector itself". |
| 17 | .39 | A barrier wears the form of correction… | Merged, §4.1: "a barrier in correction's own form, a rule that stands and is enforced, which is why it is the easier to overlook". |
| 18 | .36 | Equal incidence is not what keeps a rule… | Duplicate of #9 (§3.2) and S9 R8b. |
| 19 | .19 | Power can help an actor succeed under existing conditions or determine those conditions… | Reworded, §4.1: "Power closes the loop when it determines the conditions of success rather than helping an actor succeed under them…". |
| 20 | .45 | Off the selected level (Proposition S4.2): … delays failure by η ln(1+g_q/κ_q)/… | Sufficiency kept, §4.3: "Below the rate law, capacity that lags its selected level stays below it, so the quasi-static failure date is the earliest (Proposition S4.2)". The delay formula duplicates Proposition S4.2(2)(a). |
| 21 | .44 | AC]; a filter with memory defeats this… | Merged into one conditioned sentence, §4.4 (Remark 4.9): "until reports pass through a filter with memory or the indicator, once an alarm, becomes a target (S4)". Also S4, *Remark 4.9 in full*. |
| 22 | .38 | Scope. It depends on the speed of rule-making… 0.68 … 0.98 | Proposition 4.12 Scope keeps the dependence ("$x_\sigma$ rises as rule-making slows relative to adoption [num: DW]"). The numbers moved to S4 *The field model*, *Numerics (DW)* (0.676, 0.984). |
| 23 | .14 | How long is long enough follows from the separatrix. | Merged into the Scope's formula sentence: "an insulated pause must last $\ln(G/S(x_p))/(\varepsilon d)$, where $S(x_p)$ is the separatrix's height…". |
| 24 | .36 | With G=2 and equal speeds the length is zero from x_p=0.3… | Moved: S4 *The field model* ("S4 gives the lengths"). |
| 25 | .47 | With correction not growing, capacity that adjusts fast enough lets the floor be crossed before the alarm… | Moved: S4 *Proof of Proposition 4.13, and the two clocks*. The core Scope keeps "in the joint model either can come first … [num: QS, SR]". |
| 26 | .49 | Claim. The conditions of winning … erode the three means … (with glosses) | Box shortened. The three glosses duplicate the openings of §5.2, §5.3 and §5.4. |
| 27 | .39 | The first two arms turn on one pivot, the won share… | Merged into the §5 box ("in one reduced model the first two close together [num]"). The pivot is in Proposition 5.17. |
| 28 | .25 | A valuation check confirms the algebra of part (1) [identity: | Moved: S5 *Valuation check*. The Proposition 5.4 proof line names it, with its tag. |
| 29 | .23 | Which deviation binds … C_i=3, D_i=6… | Moved: S5 *Per deviation*. The core reads "S5 gives a pair". |
| 30 | .24 | The verification threshold compares cooperating with defecting… | Merged into the Remark 5.5 Scope ("takes the sanction F as given and leaves the rest to trust"). The remainder is in S5 *Where they differ*. |
| 31 | .20 | With n≥3, punishers in different roles can hold a relative deviator below zero. | Merged, Corollary 5.6 Scope ("so, with n≥3, do punishers in different roles"). |
| 32 | .13 | In a three-player example … δ≥0.706 … | Moved: S5 counterexample and *Strictness*. The core keeps "weak as printed and strict under small perturbations". |
| 33 | .44 | Both punishers prefer the same role… | Moved: S5 *Indifference*. The core keeps the equilibrium-selection clause. |
| 34 | .48 | Capability growth is measured, though the longest-horizon series… | Merged as a clause of §5.3 (variety grows) with [obs]. The qualifier duplicates §7.3 ("at the limit of its instrument"). |
| 35 | .39 | PE: frozen at need … 0.717 … 1.8×10⁻⁹ | Moved: S5, *Proof of Proposition 5.15*. |
| 36 | .47 | This subsection gives that line its content in information, by asking… | Kept in §5.4; the restating clause was dropped. |
| 37 | .35 | Measures become targets … (Gao et al. 2023) | Goodhart kept in §5.4 with [obs]. The Gao clause duplicates §6.4 ("Reward hacking is Goodhart's law inside training (Gao et al. 2023)"). |
| 38 | .48 | In the binary game of Remark S5.1 at D=C … 0.924 … 0.387 … 0.9495 | Moved: S5 *The reduced form (JX)*. The Proposition 5.17 proof line points to it. See U05 open issue 2: 0.9495 now prints only in S5. |
| 39 | .25 | This is *principal alignment*, each system serving its principal faithfully. | Reworded, §6.1: "This is *principal alignment*; *purpose alignment* … is not granted". |
| 40 | .36 | Delegation pressure arrives well below decisive capability … about 0.52 | §6.3 keeps the claim ("(S6 gives an example)"). The number moved to S6, *Proof of Proposition 6.2* (0.5196). |
| 41 | .47 | It has to be stated in capability, not propensity… | Reworded, §6.4. The formal point is in S6, *The formal part of Remark 6.8*. |
| 42 | .19 | The topologies also differ in budget … 36 layer-checks … 0.989 … 0.994 | §6.5 keeps the comparison ("checks at every layer catch more than checks across the gap with half the layer-checks [num]"). The numbers are in S6, *Proof of Proposition 6.9*. |
| 43 | .42 | Sections 6.2–6.4 give the mechanisms by which it becomes the opposite. | Reworded, §6.6: "Sections 6.2–6.4 show how it becomes the opposite." |
| 44 | .29 | The table names, for each threshold, the result that proves it… | §7.1 keeps the side-of-(14) reading. The other columns are Table 7.1's own headers. |
| 45 | .31 | Patience cuts both ways (Section 3.5), and so enters two rows with opposite signs. | Kept in §7.1 ("Patience cuts both ways … (P19; Section 3.5)"). The two opposite signs are S7 matrix row P19 (Stand. ↑ with a fixed prize; Enf. ±). |
| 46 | .28 | A balancing loop cannot be subtracted … 0.25 … 52 rounds … 292 | §7.1 keeps the point (Remark S2.3 [num]). The numbers duplicate S2, *Proof of Proposition 2.2* (51.6 rounds, 292). |
| 47 | .44 | Low structural decisiveness does not place a contest in Branch III: 0.3 … 0.8 … 1.1 | §7.2 keeps the point with its reason. The numbers are in S7, *Proofs of Proposition 7.2…* (Γ=1.1). |
| 48 | .46 | The reinvestment of success in influence over rules … political spending in both directions… | Table of §7.3, T4 row ("large political spending … on both sides of rule-making; its scaling with share … not measured"), and §7.3 ("The least measured signature is T4…"). |
| 49 | .24 | An arrangement whose fallback is no more hazardous than continuation… | Reworded in the §8 box. Lemma 8.2 carries the conditions. |
| 50 | .45 | The standard's second and third steps … staying inside the kernel. | Reworded, §8.1: "The standard's preference for keeping options of correction open is a preference for staying inside the kernel." |
| 51 | .38 | Deterrence by threatened sabotage acts on p_d, as custody does… | Reworded, §8.3, with its means and fallback named. |
| 52 | .17 | Profile: nothing changes in selection during the sprint. | X8 *A finite sprint* ("What it changes. Nothing during the sprint"). The §8.4 table row gives its profile. |
| 53 | .46 | At the standard's third step … estimates on both sides… | §12.1 tier 3 ("That step needs estimates on both sides, which the cruxes would supply and do not yet"). Also X8 *Where the criteria disagree*. |
| 54 | .28 | Why. A requirement stated with its model and its exceptions… | Merged into the §9 Claim ("any design, regulated competition included, checked against it"). |
| 55 | .12 | Reading the rows. Two senses of coverage are kept apart: | The Table 9.1 caption has "Coverage is of actors in R2 and of hazard modes in R5 (Section 5.3)". The R8 split reason is in S9 R8b. |
| 56 | .42 | R5's is of hazard modes … four conditions of Section 5.3. | Same caption as #55. |
| 57 | .28 | A readiness rule that demands every dimension at once … [conj] | §11.3: "noise and conjunction together bias a fixed reading toward 'not ready' … a pause held past its evidence raises the cost of staying" [thm; thm∣prem]. Also S9 *Coverage can unravel* and Remark S11.3. |
| 58 | .43 | Coverage can also fall without an exit … EV18 … weighted by share | §9, unravel paragraph: "exempting the largest participant lowers coverage with no exit at all (EV18, read in X10) [obs]"; "in coverage weighted by share, not in numbers of parties". |
| 59 | .38 | SH: … sharing all of the divisible prize only halves the uninvadable intensity … | The core keeps Proposition 10.2(2)'s bound. The figure is in S10, *Proof of Proposition 10.2*. |
| 60 | .44 | Inside it carriers are still selected, for usefulness… | Reworded, §10.4: "Carriers inside it are still selected, for usefulness; the rule is not…". |
| 61 | .33 | The theory has two answers, and neither is a better guardian. | Reworded, §10.4: "neither of the theory's two answers is a better guardian". |
| 62 | .25 | Its separation rule is the last row of the table. | Duplicate: the §10.5 form table's Authority row ("Separation rule plus chamber"). |
| 63 | .42 | Keeping AI out of the contest, stopping, slowing and pausing are different choices… | Reworded, §11.3: "differ in cost, in verification and in how they fail". |
| 64 | .27 | A temporary pause is the fourth arrangement, and by itself it changes nothing. | Merged, §11.3, with Proposition S11.2's conditions ("valued by what changes during it…"). |
| 65 | .44 | Readiness does not ask for four rows … R1, R2, R7 and R8b… | Reworded, §11.3: "Readiness presupposes rows R1, R2, R7 and R8b of Table 9.1 (Table S9.2), since no pause supplies them." |
| 66 | .46 | The residence condition is there because levels move before slow variables cross… | Merged, §11.3: "Residence is required because levels move before slow variables cross (Section 11.4)". The basin-of-capture clause duplicates §11.4 *Dwell* ("shares are back at their starting level before the state has left the basin of capture"). |
| 67 | .40 | Readiness is the release rule of the second tier of Section 12.1… | §12.1 tier 2 *Release* ("Release reads indicators of its own … not those of activation run backwards"). Also §11.5's closing hand-off. |
| 68 | .44 | From a captured share of 0.99 the hold … 1.89 to 10.45 … 5.86 to 16.18 | Moved: S11, Proposition S11.4 *(Values)*. §11.4 keeps the G=10 case with the lineage floor. |
| 69 | .43 | Windows. Whether frontier development is still the keystone, the domain whose reform… | Reworded, §11.4, with a pointer to §4.5, where "keystone" is defined. |
| 70 | .42 | The judgment applies the protection standard of Section 8.1 to the present evidence. | Merged into the §12 Claim: "Under the protection standard and the present evidence…". |
| 71 | .47 | TESTS sets each item against every crux, and each survives for a reason of its own kind. | Tier 1(a) keeps "TESTS sets each item against every crux". The kinds are named in its admission rule (measurement, preparation, an equilibrium without trust, public-good research). |
| 72 | .47 | A protection that waits for proof … not only after it is measured unfavourable [val]. | Reworded, tier 1(b): "the burden of proof lies on withdrawal: each item stands until its crux is measured favourable, and then loses only the part that crux bears [val]". |
| 73 | .11 | A release read from the activation indicators would come too early. | Merged, tier 2 *Release*: "not those of activation run backwards, which would release too early". |
| 74 | .48 | Read from its own documents, each of the design's failures but two has such a reversal: dissolution … | Compressed in §12.1 (i) "(X8, row by row)". The full list is in the X8 failure-mode rows: dissolution with protections entrenched; certificate failure; share cap, escrow and standby; rotation; sunset. |
| 75 | .46 | (ii) The irreversible failure every path shares … | Reworded, §12.1 (ii). Also X8 *Read across paths*. |
| 76 | .38 | The held boundary is an error, and an actor that sees the coupling counts it. | Duplicate: Remark 3.10 ("the boundary error of Proposition 3.6(2), which accurate understanding corrects"), §3.7 (1) and §12.2 ("it corrects the held boundary"). |
| 77 | .16 | Where the working objective rules, understanding acts through agreement … not on anyone's weights directly. | Duplicate: Remark 3.10's last sentence and §12.2 ("Understanding reaches it only as the way actors agree on which parameters to move"). |
| 78 | .36 | The sequence is understanding shared, agreement on what winning confers… | Reworded, §12.2 *The theory of change*. |
| 79 | .45 | The logic of winning is therefore individually rational there… | Reworded, §12.4 (with "(Section 3.8)"). |
| 80 | .00 | C0–C11 empirical cruxes and N1–N3 normative ones; | Corrected by this pass (§1, edit 1). |

**Companion chapters.** This pass rewrote no existing Supplement or Discussion sentence, apart from the one S13 cell (§1, edit 2). Each unit ran the chapter-level checks for its own S/X chapters (unit notes; none below 0.5 except where a unit names a splitter artefact).

## 3. Preservation of V6.1 across both passes

Command: `python3 src/sentcheck.py ../v6.1/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4`
- Result: 1,060 sentences checked, 81 below 0.4.
- Of these, 51 were already below 0.4 against draftA. The merge round adjudicated them (merge notes Uxx, plan §1, §5, §8); they are re-verified here.
- The other 30 fell below 0.4 in the elegance pass. They are the same sentences as in §2, or their V6.1 forms (marked **E** below).
- **No V6.1 point is without a findable home. Nothing was restored.**
- **Superseded, not lost:** where V6.2 corrected or withdrew a V6.1 sentence (rows 2, 10, 22, 34, 49, 74, 75, 79), the correction's source is named.

| # | c | V6.1 sentence (start) | Disposition (home in V6.2) |
|---|---|---|---|
| 1 | .38 | Why. The conditions are not a list of separate causes. | §1.2 item 1: "interconnected, not a list". Also §7.1 ("not a single pressure, but a few parameters on which several thresholds turn"). |
| 2 | .35 | Sharing, provision …, diffusion and correction lower it; decisiveness … raise it. | Corrected (plan §1 item 2). Proposition 2.2 lists the three removals that give Γ=0. The §2.2 levers paragraph and Proposition S2.4: correction lowers the gain only in a level channel and never in a ratio channel, where it raises the discounted gain. |
| 3 | .25 | The other redirects… **E** | As §2 #1. |
| 4 | .16 | An agent that optimizes only the value that is measured… [corpus: meta-attractor] | §2.1 quotes Ren's line verbatim with its key, after the analytic step that it compresses. |
| 5 | .37 | Scope. Local, at equal standing, … in (3), others' strategies are held fixed. | Now inside the Proposition 2.2 statement and box ("actors' conduct fixed"), with (4) for rivals who respond (statements own their conditions). |
| 6 | .13 | Proof: S2; checked against numerical Jacobians … 4,000 random systems… | The proof line is "Proof: S2 [num: LG, PD, MP]". The 4,000 systems are in S2, *Numerics*, block LG. |
| 7 | .24 | It is restored from every starting point iff a laggard's inflow exceeds its depreciation… | Proposition 2.3 (ii): "returns from every start iff $\phi>0$ on $(0,\bar K)$". |
| 8 | .36 | When r>1 that needs inflow not tied to rank…; βκcΩ/n+k0 ≥ d_K K̄ suffices. | Proposition 2.3: "return from every start needs an inflow not tied to rank: sharing, provision or diffusion … $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ suffices". |
| 9 | .26 | With growth in total capacity and no depreciation… **E** | As §2 #4. S2 *Growth variants* (b) has "constant only if the stakes grow with capacity". |
| 10 | .33 | Among three or more actors, what relative accounting does to talk is not a function of Γ either… **E** | Superseded in the merge round. S2's "What the loop gain unifies" now classifies talk, between two parties and among three or more, as a comparative static through the working self-model (Proposition 5.16; plan §7 "TK: talk unified"; blocks TK, T3). §2.2 names the two conditions Γ does not decide. |
| 11 | .36 | Practices that produce more publications… **E** | As §2 #6. |
| 12 | .00 | The conditional form keeps its conditions… **E** | As §2 #7. |
| 13 | .07 | One concept covers the mechanism and its generative dual… **E** | As §2 #8. |
| 14 | .30 | It can raise the growth of hazardous behaviour relative to contestable coverage. | §2.4: "where it raises the growth of hazardous behaviour faster than contestable coverage…". |
| 15 | .29 | And it can become a carrier itself (Section 6). | §2.4: "Trained AI systems are themselves carriers (Section 6)". |
| 16 | .33 | The rest of Part I follows one chain. | One home per point (merge notes U02): the chain lives in the abstract, guide, §1.2 and §12.4. |
| 17 | .25 | What an objective sees of the shared depends on where its self-model draws its boundary… | §3 box, sentence 2; §3.3 (θ marks where the self-model draws its boundary); Proposition 3.9. |
| 18 | .23 | A common liability … reverses selection… **E** | As §2 #11. |
| 19 | .39 | Scope. First order, others' strategies and the prize fixed; two-period contest … six digits | The conditions are in the Proposition 3.9 statement. The two-period check, relabelled as algebraic per plan §7, is in S3, *Full form and proof of Proposition 3.9* (7.6×10⁻⁸ in 14 cases). |
| 20 | .25 | Selection on conduct favours the relative objective; compounding manufactures it… **E** | §3 box ("selection favours the narrowest"; "a forward-looking actor weighs standing above what all share…"). §1.2 item 2 still says "manufactures"; plan §8.3 replaces it with "prices standing" (front-matter phase). |
| 21 | .19 | Power can help an actor succeed under existing conditions… **E** | As §2 #19. |
| 22 | .11 | Scope. Quasi-static capacity; a joint simulation … has not been run (TESTS, Study 2). | Superseded. Proposition S4.2 computes capacity off its selected level together with the field [num: QS], and §4.3 points to it. S13 and S15 still say "not run" (§5, item 3). |
| 23 | .29 | AI-assisted correction can win this race (Section 8.3). | §4.3: "AI-assisted correction can keep pace (Section 8.3(a))", the vocabulary of plan §8.3. |
| 24 | .39 | Scope. It depends on the speed of rule-making … 0.68 … 0.98 **E** | As §2 #22. |
| 25 | .27 | A long enough pause is at least ln G/(εd) plus … (S11). | §11.4 *Dwell*; Proposition S11.4. |
| 26 | .30 | Proof: S5; direct evaluation … 200,000 random settings, and the bound without the breakout term fails… | The Proposition 5.4 proof line, relabelled as a valuation check per plan §7. The 200,000 settings are in S5 *Valuation check*. The bound without the breakout term is in the statement. |
| 27 | .19 | Scope. With n≥3, punishers in different roles … 0.706 **E** | As §2 #31–#32. |
| 28 | .20 | In cooperation one reasons (讲理); in contest one argues to win (讲赢)… [corpus: meta-attractor] | §3.8 gives Ren's line in full with its Chinese and corrected keys [corpus: alignment-selection; jian-and-wenyan] (merge notes U03). |
| 29 | .35 | Measures become targets … (Gao et al. 2023). **E** | As §2 #37. |
| 30 | .00 | Meanwhile tempo outruns correction and relative accounting drains talk. | §5 box (the three erosions); §1.2 item 4. |
| 31 | .19 | As an instrument, faithful systems make the game … more effective… | §6 box: "As an instrument: where principals play a harmful game, faithful AI makes it more effective, and … decisions pass to AI…". |
| 32 | .39 | What the level that selects developers rewards decides … no mechanism that binds every capable developer… **E** | §6 box Why: "The level that selects developers decides which of them it pays to remove [thm∣prem], and at present no mechanism binds every capable developer under independent verification [obs]". |
| 33 | .39 | Lowering the harm alone cuts the loss at all-racing but raises θ*… | §6.2: statement, plus "a safety improvement inside the game has this double edge". |
| 34 | .30 | AI is a planetary technology, and its purpose can be shared flourishing. | §6.6 and V1. "Shared flourishing" is replaced by V1's content (plan §5; fidelity minor 5; merge notes U06, U12). |
| 35 | .35 | Why. Part I's results hold in their models; … one standard to every actor. **E** | Part II's opening: "read by one standard for every actor and with their gaps named". Also the §7 box ("with named gaps in the evidence [obs]"). |
| 36 | .24 | The same few parameters enter the threshold results … growth moves them together. | §7.1, "a few parameters on which several thresholds turn … whether they move together in the world … is C0 [conj]". |
| 37 | .22 | Arrows show whether a rise raises or lowers the danger … (S7 gives the full table…) | §7.1: "S7 gives the full matrix of parameters against thresholds…". |
| 38 | .12 | Parameter \| Loop gain \| Working objective \| … (V6.1 arrow table) | S7, *The matrix of shared parameters* (P1–P19), now with intervention, what is held fixed, model and interface. |
| 39 | .37 | Acceleration makes the contest harder and harder to regulate… **E** | §12.4: "it accelerates the contest, makes it harder and harder to regulate, and alienates language". Also the §5.3 opening. |
| 40 | .25 | In the corpus the chain is four loops in series [corpus: selfishness-spiral]: | §7.1 *Four loops*: "The author describes the pressure as four loops [corpus: selfishness-spiral]". |
| 41 | .12 | compounding, what is won kept and used to win more; | §7.1 *Four loops*, Compounding in the author's words. |
| 42 | .12 | naturalized narrative …; and regulator lag, produced by the first three. | §7.1: "Regulator lag is not a fourth reinforcing loop but the balancing loop of correction and mobilization…, and the first three act on its two properties". Also S7, *The four loops, formally*. |
| 43 | .36 | The driver is technology, AI above all… | §7.1, *The drive, the driver and the substrate*. |
| 44 | .36 | The three parts of the race's premise define four branches. | §7.2, first sentence. |
| 45 | .34 | On that comparison, each alternative is described by what it changes, not by its name… **E** | §8 box and Definition 8.3. Also §1.2 item 7 ("whatever they are called"). |
| 46 | .00 | Why. Labels such as "regulation", "cooperation" or "agreement" decide nothing. **E** | §8 box Why: "so labels decide nothing [def]". Heading of §8.2: "Profiles, not labels". |
| 47 | .38 | Proof: S8, with examples in which the shared hazard carries the argument for a leader. **E** | S8, *Survival at a common horizon* ("For a leader whose exit would hand a rival a decisive win, the shared hazard is what carries the case for restraint"). |
| 48 | .38 | Deterrence by threatened sabotage acts on p_d… **E** | As §2 #51. |
| 49 | .12 | Its force comes from the combination of stick and carrot. | Replaced by the plan's tone sentence, §8.3(d) and X8: "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact" (merge notes U08). |
| 50 | .39 | Proposition 8.8 (Prevention under the preventer's own criterion)… | Now Proposition 8.5, restated with its conditions. |
| 51 | .17 | Why. A requirement stated with its model and horizon can be checked … **E** | As §2 #54. |
| 52 | .20 | Lemma 6.5 \| selection by public mandate; zero or negative alignment tax; … | Table 9.1, the R8a/R8b "Not needed" cell. Also S9, *Table 9.1, row by row*. |
| 53 | .31 | Coverage can unravel. The protection of Lemma 3.3(2) holds only under full coverage. | §9 *Coverage can unravel*: "A common constraint protects only while it covers every capable actor". Also S9. |
| 54 | .29 | They give shelter and fruit, maintain the system they belong to, and do not become it. | §10.1 quotes Ren's line verbatim ("the lungs of the ecosystem" … "become the whole ecosystem") [corpus: shengsheng]. |
| 55 | .31 | Scope. The transient is real: … the host dips to 0.14 before recovering [num]. **E** | The Theorem 10.4 statement now carries the transient as its condition ("throughout iff liability exceeds the private advantage by a margin the host sets"). The dip (0.1397) is in S10, *Proof of Theorem 10.4*. |
| 56 | .36 | The corpus states two loops with the same reflexive structure and opposite signs [corpus: shengsheng]. | §10.4: "The author's book states the two signs as two loops of the same structure [corpus: shengsheng, 2026-07-14 第十四章]". |
| 57 | .38 | Its positive loop runs through the system, not through its winners; its negative loop … keyed to no one. **E** | §10.4 ("by financing fixed in formula …; and by a loop that runs through the whole, not through its winners"). Also §4.6 ("correction keyed to no one"). |
| 58 | .33 | The theory has two answers, and neither is a better guardian. **E** | As §2 #61. |
| 59 | .10 | Each counter-mechanism requires a particular form… **E** | §10 box: "Each counter-mechanism requires its own form…". Also §10.5. |
| 60 | .32 | The levy is indexed to the coverage each hazard class requires … and is itself treated as a prize. | X10 *Functions, held separately* (the correction fund is indexed to coverage, not to capability or perceived harm) and X10: "The levy formula is itself a prize". |
| 61 | .12 | Claim. An attractive end state is not a reachable one. | §11 Claim: "An end state that every participant would keep is not thereby one they can reach…". |
| 62 | .27 | The transition must be survivable at every stage … every step meets a compensating loop. | §11 Claim. Also §11.4: "Each track meets a compensating loop of its own". |
| 63 | .36 | Why. The conditions act on the transition itself: a change withdrawn early is re-absorbed… **E** | §11 box Why. Also the §11.4 opening ("holds only if that variable crosses its threshold before the commitment is withdrawn (Proposition 4.11)"). |
| 64 | .09 | Verification lowers the assurance threshold on verifiable dimensions but carries no unverifiable information. | §11.1 ("Verification relaxes the first … and only on what it observes"). Also the §8.3 Scope ("Verification does not carry unverifiable information (Proposition 5.16)") and Corollary S11.1. |
| 65 | .21 | Sanctions relax assurance and exit at the price of escalation, and cannot be enforced against a decisive defector… **E** | §11.1: "a sanction relaxes the first and the third only while it can still be imposed, so that against a defector whose position has become decisive it acts only through the bound $\bar p_d$ …; and the price of sanctions is escalation". |
| 66 | .36 | Proposition 11.2 (When keeping AI out of one's decision loops is a signal)… **E** | Now Proposition 11.1, statement with its conditions. |
| 67 | .40 | Such a step separates the types … iff … | Proposition 11.1 statement. |
| 68 | .33 | A reversible or unverifiable step is cheap talk. | Proposition 11.1 statement. Also S11, *Proof of Proposition 11.1*. |
| 69 | .33 | Scope. Whether it separates in practice depends on measured costs… | Proposition 11.1 Scope. |
| 70 | .25 | Its coverage comes from consent or coercion, and coercion's escalation risk is counted in Θ. | §11.3: "Coverage of E2 comes from consent or from coercion, whose risk of escalation is counted in Θ and whose conditions are stated once, in Section 12.1". |
| 71 | .28 | Dwell times. A change must be held until rule support falls below break-even … [conj for real institutions]. | §11.4 *Dwell*. Also §12.1 tier 2 *Release* ("in the field model [thm] and by conjecture for institutions [conj]"). |
| 72 | .22 | Each stage has its own slow variable: human capacity in Stage 2, the capability held in check in Stage 4. | §11.4 tracks table, Tracks 2 and 4. |
| 73 | .38 | Windows. Development is plausibly still the keystone [conj]; … Stage 3 cannot wait for Stage 4's trust. **E** | §11.4 *Windows*: "[conj] … the correction track cannot wait for the trust that custody needs". |
| 74 | .23 | Warranted now, on any reading of the cruxes [rec]. … mostly accepted by those who favour regulated competition: | §12.1 tier 1(a). The acceptance clause is withdrawn as false (merge notes U12; item 8: "They are not accepted across camps"). |
| 75 | .31 | Continuation's worst case needs only that the premises of Section 5.3 hold … the certificates can be measured before the design is relied on. | First half: §12.1 (i) ("for hazards that manifest late its premises cannot be measured before they bind"). Second half: withdrawn as false, since row sums have never been measured (merge notes U12). It is replaced by the reversibility asymmetry ("designed and not yet tested" against "derived and cannot be undone"). |
| 76 | .10 | And among paths that pass the tolerance it realizes more joint value. | §12.1, third consideration. |
| 77 | .27 | Where convertibility and decisiveness are high, the first is selected against … not on anyone's weights directly (compare Powell 1991). **E** | As §2 #77. Powell 1991 is cited in §3.5. |
| 78 | .16 | Interventions that move a parameter without crossing its threshold are re-absorbed… | §12.2, Meadows paragraph ("below its threshold a reform is re-absorbed, and across it, it is not (Proposition 4.11)"). |
| 79 | .17 | The logic is locally rational and systemically false. | Replaced by Ψ's triple, §3.8 and §12.4 (plan; merge notes U03, U12). |
| 80 | .00 | C0–C11 empirical cruxes and N1–N3 normative ones; | Corrected (§1, edit 1). |
| 81 | .33 | Birkhäuser. † Crawford, V. and Sobel, J. 1982. | Reference-list splitting artefact. The Crawford and Sobel entry is in THEORY's references. |

## 4. Word counts

**Core sections:**
- The core column is the assembler's rule: a formula counts as one word.
- The Supplement and Discussion columns are per chapter, by the same rule, from the assembled documents, without references.
- In the core column, the first figure is the assembler's per-section count and the second is the chapter-split count; the two differ only by headings.

| Section | V6.1 | draftA | now | change |
|---|---|---|---|---|
| front | — | 77 | 77 | 0 |
| §0 | 343 | 343 | 343 | 0 |
| §1 | 1,410 | 1,446 | 1,446 | 0 |
| §2 | 2,645 | 4,007 | 3,620 | −387 |
| §3 | 3,586 | 5,452 | 4,960 | −492 |
| §4 | 2,613 | 4,473 | 4,115 | −358 |
| §5 | 3,184 | 5,579 | 4,962 | −617 |
| §6 | 2,903 | 6,015 | 5,636 | −379 |
| §7 | 2,020 | 5,563 | 5,192 | −371 |
| §8 | 3,086 | 5,388 | 4,722 | −666 |
| §9 | 870 | 3,089 | 2,583 | −506 |
| §10 | 3,484 | 6,520 | 5,954 | −566 |
| §11 | 2,318 | 5,921 | 4,789 | −1,132 |
| §12 | 1,664 | 5,321 | 4,845 | −476 |
| symbols | — | 322 | 341 | +19 (labels fix) |
| **core total** (assembler) | ≈30.5k | ≈59.5k | **53,585** | ≈ −5.9k |

Parts III+IV: 22,893 words, 43% of the core. The 导读 is 1,181 字 (unchanged; rewritten next).

**Supplement chapters** (total 48,624 by chapter split; assembler figure 48,729):

| Chapter | V6.1 | draftA | now | change |
|---|---|---|---|---|
| S0 | 524 | 524 | 524 | 0 |
| S2 | 905 | 4,879 | 5,034 | +155 |
| S3 | 1,598 | 4,109 | 4,473 | +364 |
| S4 | 1,631 | 4,857 | 5,090 | +233 |
| S5 | 2,568 | 6,430 | 6,464 | +34 |
| S6 | 1,454 | 4,151 | 4,544 | +393 |
| S7 | 896 | 5,143 | 5,245 | +102 |
| S8 | 1,826 | 3,322 | 3,335 | +13 |
| S9 | 696 | 4,309 | 4,858 | +549 |
| S10 | 1,217 | 3,029 | 3,029 | 0 |
| S11 | 637 | 3,589 | 4,439 | +850 |
| S13 | 309 | 309 | 316 | +7 |
| S14 | 770 | 770 | 770 | 0 |
| S15 | 503 | 503 | 503 | 0 |

**Discussion chapters** (total 15,783 by chapter split; assembler figure 15,861):

| Chapter | V6.1 | draftA | now | change |
|---|---|---|---|---|
| X1 | 1,941 | 1,943 | 1,943 | 0 |
| X2 | 355 | 355 | 355 | 0 |
| X8 | 2,604 | 6,450 | 6,651 | +201 |
| X10 | 1,863 | 3,779 | 3,916 | +137 |
| X11 | 1,409 | 2,442 | 2,918 | +476 |

## 5. Checks

`python3 checks_v62.py > checks_v62.log` ran in 283 s with exit code 0.
- **Assertions:** 169 passed, 0 failed (default sizes).
- **Codex's boundary cases:** all eight of plan §7 appear in a block and hold.
- **Against the previous log:** apart from the timing lines, identical. The elegance pass changed no mathematics, and the suite does not read the prose.
- **Not a failure:** line 140, "the conditional step fails, the unconditional claim holds", is the FD block's intended contrast.

## 6. Open issues

**For the next phase (front matter, symbols, S13–S15, registers):**
1. **Guide and §1.2.** Guide items 1 and 9 are below threshold (expected).
   - §1.2 item 1 says the loop gain "prices standing for every actor", which the conditions in §2 and §3 now restrict (U02 #5).
   - §1.2 item 2 says compounding "manufactures" the relative objective; plan §8.3 bans "manufactures".
   - Plan §1 item 1's "always" must become "wherever $\Gamma_\delta>0$" in any abstract or guide wording (U03 #3).
   - §1.2(4) "forms blocs" (U05).
2. **Symbols.** The labels line is fixed here. Still open: the symbol renames and additions ($\Phi^R,\Phi^T,\Phi^P,\Phi^S$, $\mathsf u_t$, $V^{\rm exit}$, $V^{\rm stay}$; U08 #6), and restricting the "one meaning" claim to the table's own symbols.
3. **S13 and S15 contradict S4 and S11.**
   - S13's row *Capacity and the field* says "Joint simulation not run (TESTS, Study 2)".
   - S15 says "Not yet computed: the joint simulation of capacity and the field … and the effect of an alternative lineage on dwell times".
   - Both are false now: Proposition S4.2 [num: QS] and Proposition S11.4 [num: DW] compute them.
   - S15 as a whole still describes `checks_v61.py` and V6.1's blocks; it lacks SP, PD, MP, CE, CH, TD, QS, FF, ES, JX, SR, among others.
   - S13 still lacks the row "Human capacity and correction" (U04 #4), the $p_d=1-\upsilon(T_{\rm dec})$ form (U05) and the U07 interface names.
   - All of this is the S13–S15 task of `v62-front-registers.js`. It was left there, apart from the one $T_{\rm dec}$ cell fixed here.
4. **Registers.**
   - LEDGER: "levels of epistemic closure (§4.1)" should read §4.4, and "Remark 4.7(4)" is stale (now Remark 4.9) (U04 #2–3).
   - CLAIMS:
     - the two-period factor is [num: MP];
     - Ψ's triple;
     - the `require` row;
     - the `pausefield` location;
     - the D-marks listed by U03, U05, U06, U08, U10 and U12.
   - TESTS: C7 "Stage 1 transparency"; Study 2, which is now partly run (S4.2).
   - EV6 pointer (U06 #3).
   - CHANGELOG: the moves listed in each unit's notes, among them `relaxtrust` and `pausevalue` to S11, the readiness table to S11, the tracks columns to X11, the `enforce`(5) example to S5, and the masking citations to S6.
   - The EVIDENCE/TESTS citations missing from reference lists (§1).
5. **Wording questions left by units:**
   - S2 l.80 says "correction and non-appropriability to rule support", while §2.2 names only correction (U02 #3, U07 #5).
   - "Favourable" in tier 1(b) fits items 6 and 7 but not item 8 (U12 #3).
   - §12.1's *Estimator* restates §5.2's masking sentence (U05 #4).
   - X8's "Read across paths" nearly restates §12.1 (ii) (U12 #5).
   - Pointer convention: "X1" or "Discussion X10" (U02 #7).
   - Quotation convention: "the author" or the corpus key.

**For Ren:**
6. Keep R9 or reject it (U09 #1). The symbols line now says R1–R9.
7. Should 0.9495, the corrected figure, be visible in the core (U05 #2)? Should the readiness table return to the core (U11 #1, about +110 words)? Should the Meadows mapping move to X1 (U12 #1, about −110)? Should `frontier` stay a core Remark (U05 #1)?
8. **Length.** §0–§12 come to 53.2k against draftA's 59.1k: −5.95k, about 10%, while the companions grew by about 3.5k. Every unit stopped 20–60% above its guide, for the same stated reason: statements that keep every premise, and plan-mandated tables and boxes. Each unit's notes list its remaining levers and their costs (U02 #1–2, U06 #4, U07 #1, U08 #1, U09 #5, U10 #1, U11 #2, U12 #10).
9. **Box lengths.** The boxes run 177–304 words against the 90–140 guide. Each unit's notes name the one cut that would lose no antecedent; a uniform box pass would settle them together.
