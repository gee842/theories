# U07 elegance pass, editor A: Section 7 (core `70_s7.md`) and S7 (`supp/07_S7.md`)

4 October 2026. Start point: the current `src/` files, byte-identical to `planning/snapshots/draftA/src/`. The directory held no earlier attempt. The unit has no Discussion chapter.

Files written (only these three):
- `planning/edit/U07/A/core/70_s7.md`
- `planning/edit/U07/A/supp/07_S7.md`
- `planning/edit/U07/A/NOTES.md`

## 1. Word counts

Assembler's rule (a formula counts as one word), from the scratch assembly `/private/tmp/claude-501/u07-A-scratch`:

| | Snapshot (draftA) | Edited | Change |
|---|---|---|---|
| core §7, assembler count | 5,563 | **5,381** | −182 (−3.3%) |
| core `70_s7.md`, raw | 5,405 | 5,219 | −186 |
| Part II lead | 63 | 63 | 0 |
| claim box (Claim + Why) | 250 | 232 | −18 |
| §7.1 intro | 93 | 93 | 0 |
| Table 7.1 | 928 | 922 | −6 |
| the paragraph after the table (was two paragraphs: 140 + 158) | 298 | 282 | −16 |
| four loops (Ren's words) | 279 | 279 | 0 |
| formal correspondence | 314 | 247 | −67 |
| the drive, driver, substrate | 328 | 311 | −17 |
| §7.2 | 1,681 | 1,656 | −25 |
| §7.3 (T-table 337 → 334) | 683 | 667 | −16 |
| §7.4 | 451 | 430 | −21 |
| supp `07_S7.md`, raw | 4,800 | 4,981 | +181 |

**On the target (about 3,200).** The section lands at 5,381, and I stopped there deliberately. The plan fixes most of this section's weight in objects that the rules of this pass do not let me thin:

- **Table 7.1** (922 words) is the paper's integrating figure (plan §1 item 6), with six mandated columns: the inequality with its conditions, the result, the pushers, the levers by channel (plan §1 item 2), and the side of (14) moved. Every cell is a condition, a parameter or a lever; the only illustration in it, the 0.45 structural gain, is now stated as the condition it illustrates.
- **`branches`** (470 words plus a 95-word Scope) is a reading list by construction: each branch is the set of results already proved, read under the branch's condition, and each clause carries that result's own premise (`enforce`(4)'s "worth at least cooperation"; `join`'s $S_i<P_i$; `delegatelock`'s certain lock; (A8); the [prem] of Branch II's delegation clause). Dropping a clause drops a result from the classification; shortening one drops its premise (V6.1's error).
- **`raceselects`, `racepremise`** and their Scopes (about 400) are cited from §5.1, §8.3, §12.1 and X8 and carry the conditional-independence premise the merge restored.
- **The T-table** (334) is what Part III takes from this section ("the status column of Section 7.3"), with D4's status readings.
- **Ren's four loops** (279) are verbatim with their corpus keys, and the drive paragraph carries the attractor-of-attractors line after its mechanism.
- **The box** (232) states five results with their antecedents and tags, as other units' boxes do (U05: 205).

That is about 2,750 words before any prose. The remaining 2,600 carry the plan's one paragraph after the table (the three recurring parameters, the three bold entries, the S7 pointer, C0), the formal correspondence (Sys I2), the drive with its made/held split (C8, `twoerrors`), the §7.2 consequences that later sections point to (the nuclear [obs] that §5.1 points to; the field sentence that `frontier` points forward to; the oneness ruling; the act-before paragraph that §12.1 cites twice; near parity, which §8.3(c) cites; the lineage sentence), the §7.3 reading with Ren's T6 line, and the three tests, the refutation and the hand-off. D1-opus budgeted §7 at 2,550 with a 250-word table and a one-sentence Why; the plan's additions (the (14) column, levers by channel, conditions in every statement, D4's readings) are what the difference carries. Reaching 3,200 would need the table cut to parameter names or `branches` reduced to its branch conditions, and I judge both to make the core less complete in its conditions.

## 2. Moves (core → companion), with the pointer left in the core

| # | What left the core | Where it now lives | Pointer in the core |
|---|---|---|---|
| M1 | Formal correspondence, loop by loop: "Capture lowers its gain, since a captured corrector imposes less and reports less (`corrrate`), and so does the erosion of the human capacity on which correction rests (`humancorr`); acceleration shortens the time correction has, masking hides the harm that would start it, and alienated language delays the recognition that would mobilize it, so its delay lengthens (`tempo`, `masking`, `talk`)" | S7 "The four loops, formally", new paragraph *Loop by loop* before the loops table | the core keeps the claim with every citation: "capture and the erosion of human capacity lower its gain (`corrrate`, `humancorr`), while acceleration, masking and alienated language lengthen its delay (`tempo`, `masking`, `talk`) [thm, each in its model]" and "(S7 gives the correspondence loop by loop)" |
| M2 | The delays with their formulas: turnover of capacity about $1/(d_K+\delta_f)$; settling of rule support about $1/(\varepsilon d)$ | S7 *Loop by loop* (the loops table's Delay column already held them) | "across delays that run from the turnover of capacity to the formation of minds over generations" |
| M3 | The `delayosc` numbers: gain 0.5 against $-0.05$ through a slow stock, net 0.25, period about 52, 292 times after 600 | S7, closing paragraph of "The four loops, formally" (S2's Remark `delayosc` holds the same case in full) | "at a net gain below one, deviations can still grow, oscillating (`delayosc`) [num: CH]" |
| M4 | `branches` Scope numbers: 0.8 + 0.3 opens the loop at 1.1 [num: LG]; equilibrium gain above one from a structural gain of 0.45 [num: MP] | S7, proof of `branches`, Branch III (already there verbatim, with 1.11 at 0.45 and 2.83 at 0.6) | Scope keeps the condition: "channels of capacity and rule support add in $\Gamma$ (`loopgain`(1)), and rivals who respond can lift the equilibrium gain above one from a structural gain below one where a lead discourages the follower (`eqgain`; S7 gives the cases) [num: LG; MP]" |
| M5 | Table 7.1, Compounding danger side: "reached at a structural gain of 0.45 where a lead discourages the follower" | S7 Branch III proof (as M4) | "which a structural gain below one does not exclude where a lead discourages the follower [num: MP]" |
| M6 | Near parity, the four facts in full ("in the computed two-actor contests in which a lead discourages the follower, the price of standing is amplified at parity (Section 3.5), its sum over the two contestants is higher at parity than at a three-to-one split in every case computed, total effort is highest at parity and falls as a lead opens, and a laggard's price falls, below zero with a shared loss") | S7 "Near parity" (already there, with the numbers and the leader exception) | the same four facts in a shorter sentence, with the condition kept as an antecedent ("in contests in which a lead discourages the follower") and "(S7 gives the cases) [num: MP; held for outside review]" |
| M7 | Test Γ: "in one computed case it rises from 0.58 to 0.81 as the won share falls from one to a half" | S7 matrix, row P4 (already there) | "(S7, row P4, gives a computed case) [num: SP]" |

No key changed kind or number; the four declarations (`thresholds`, `branches`, `raceselects`, `racepremise`) stand in the same order. `{{eqgain}}` is the one new citation (an S2 Remark, resolves). Nothing moved to a Discussion chapter.

## 3. Duplicates removed (true duplicates of text elsewhere in the paper)

| Sentence removed | Where the point lives |
|---|---|
| "In a level channel such as rule support, provision adds the same to everyone and changes nothing; there the levers are correction and non-appropriability (Section 2.2)." | §2.2's lever paragraph ("In a level channel, such as rule support …, provision, which adds the same to everyone, changes nothing") and S7 row P5; the core keeps the clause "in a level channel such as rule support it changes nothing, and the levers there are correction and non-appropriability (Section 2.2)" |
| "by one composite index the frontier has stayed with developers in one state, while on a preference leaderboard the gap at the top is a few per cent" (the leaderboard gap) | EVIDENCE EV5, *Reading for decisiveness*, which the §7.3 Decisiveness row summarizes; the core keeps "staying with developers in one state on a composite index while reported to have been traded on a preference leaderboard [obs: EV5, EV9; C5]" (D4 Verification 12's "reported to have been traded" kept) |
| "The reinvestment of success in influence over rules … is now visible as political spending in both directions but remains the least measured" | the T4 row of the same table ("large political spending by developers and their backers on both sides of rule-making; its scaling with share and its appropriable part not measured"); the core keeps "The least measured signature is T4, the link to Section 4, since what Section 4 predicts is appropriable support that scales with share" |
| "Where offense has the advantage and is hard to tell from defense, AI sits in the doubly dangerous quadrant" as a separate sentence | X1 holds the lineage in full; the core keeps it as a clause with its citation (Jervis 1978; X1), so no reference entry is orphaned |
| Why, "read by one standard for every actor" | the Part II lead and the §7.3 intro |
| "Correction that arrives late can destabilize what it is meant to steady" as a separate sentence | merged into the `delayosc` sentence as its consequence |

## 4. Preservation check

Run in the scratch copy: `python3 src/sentcheck.py <draftA>/src/core/70_s7.md src/core/70_s7.md src/supp/07_S7.md <all other current core/supp/disc files> --min 0.5`. **130 sentences checked, 5 below 0.5**, each adjudicated:

| # | Old sentence (start) | Disposition |
|---|---|---|
| 1 | "**Why.** Each threshold is one inequality in a specified model, and a parameter that enters several moves each …" (0.49) | kept in shorter words with the same content and tag (one inequality per model; a parameter entering several moves each in its own model; a cross-model sign names its interface, not proved [thm]) |
| 2 | "Among persons, the desire for status, respect freely conferred, is a fundamental motive (Anderson …), with two routes to rank …" (0.46) | merged with the next sentence into one: the drive channels status into dominance rather than prestige, respect freely conferred, both citations kept [conj]; the generative counterpart and the convertibility condition (V5; EV16) kept. Not moved to S7 because the Supplement's reference list has neither source |
| 3 | "Low structural decisiveness does not place a contest in Branch III: a channel of rule support adds 0.3 …" (0.44) | moved, M4; the Scope keeps the claim as a condition with `loopgain`(1) and `eqgain` |
| 4 | "Whether the lead has changed hands depends on the measure: by one composite index …" (0.43) | merged into the evidence sentence (§3, duplicate of EV5 for the leaderboard gap); "depends on the measure", the composite index, the one state and "reported to have been traded" kept |
| 5 | "The reinvestment of success in influence over rules … least measured …" (0.46) | duplicate of the T4 row (§3); the non-duplicate half kept ("least measured … appropriable support that scales with share") |

Against the new core alone (`--min 0.7`, 15 listed), every further item is in §2 or §3 above: the level-channel sentence (M-/dup), the promised-sharing sentence (reworded, same content), the loop-by-loop sentence (M1), the `delayosc` numbers (M3), the drive's second sentence (reworded: "raises the weight on winning, shortens the horizon, narrows the working objective and weakens the repetition on which enforcement rests" is kept whole), the two Branch III numbers (M4), the near-parity sentence (M6), Test Γ's "holding declared objectives fixed" (kept, moved to the front of the sentence). Nothing needed restoring.

**S7:** draftA's `07_S7.md` against the final files: **161 sentences, 0 below 0.5**. The only existing S7 text rewritten is the first sentence of "The four loops, formally" (extended into the *Loop by loop* paragraph) and the closing paragraph (the `delayosc` case added).

**Tags and keys (core):** [thm 22→22; [obs 4→4; [conj 6→6; [prem 3→3; [val 3→3; corpus 3→3; † 17→17; [num 8→7 (the Scope's two brackets [num: LG] and [num: MP] are now one bracket [num: LG; MP]). Ren's lines verified verbatim against the snapshot by string match (seven English lines, the Chinese line, the T6 line); the rulings "Oneness is what these requirements are requirements of", "what each can rationally do cannot be what all should choose", "a change of the game, which accurate understanding alone does not make", "committed in advance and executed by mechanism", "The window for custody and the hardest-fought stretch …", "not every incentive to compete" are present.

## 5. Other changes

- **"both blades" → "both arms"** in the provision entry (§7.1), matching merged `scissors` (merge notes: "blade" corrected to "arm"); the core still said "blades".
- **§12.1's pointer now lands.** §12.1 cites "(Section 7.2)" for "custody begun at a warning is in place too late wherever building it takes longer than the warning gives"; §7.2 did not state it. The act-before paragraph now reads "Custody … has to be prepared while leads are short: begun at a warning, it is in place too late wherever building it takes longer than the warning gives."
- **Test G** points to "(Section 5.5; S5)" (U05 elegance notes, open issue 3).
- **Plan §4: "followed by its one paragraph."** The two paragraphs after Table 7.1 are now one, in the order the plan gives: the three recurring parameters, the three bold entries (the first kept in bold as V6.1's; patience and promised sharing as plain clauses with their mechanisms), the S7 matrix pointer, C0.
- The "defensive realism" paragraph is one sentence; the Fidelity-minor-4 wording is kept.
- A banned phrase ("one pressure") that a first draft introduced was caught by the assembler and reverted to "a single pressure".
- Mathematics unchanged; no error found. The `raceselects`(2) identity and the Branch I reduction of (14) at $p_d\to1$ were re-read against the S7 proofs.

## 6. Verification

- Test assembly in `/private/tmp/claude-501/u07-A-scratch` (a fresh copy of v6.2 with the two files installed): **no problems**; 95 core and 33 supplement declarations; §7 = 5,381; Table 7.1, Propositions 7.2 and 7.3, Corollary 7.4 as before.
- `xref_v62.py` there: must-stay 32/32; no named states or firms in core prose; THEORY citation coverage complete for this unit (Anderson 2015, Henrich and Gil-White 2001, Fearon 1995, Powell 2006, Wendt 1992, Jervis 1978 all cited and listed). The failures it reports are not this unit's: Rankin, Bargum and Kokko 2007 uncited in THEORY and missing with Alchian 1950 from the SUPPLEMENT list (both cited from §3/S3 only), and guide items 1 and 9 (front matter, later phase).
- Vocabulary of plan §8 kept: "the drive" (never "gain" for it); structural/equilibrium gain; price of standing; working objective; provision not won / beneath the game; E2 stopping, E3 pace; "signature"; "per-unit cost floor"; "masked divergence".

## 7. Open issues for the integration editor or Ren

1. **Length.** If a shorter §7 is wanted, the only large levers left are the ones this pass declined: the "Pushed toward danger by" column of Table 7.1 (about 230 words) could point to S7's matrix rows instead of listing pushers, and the T-table's status cells (about 230) could be shortened to one-phrase statuses with EVIDENCE holding the readings. Each is a plan-mandated element, so I leave the choice to the editor.
2. **The status-motive sentence** (Anderson 2015; Henrich and Gil-White 2001) belongs by content with S7's mechanism index row "The drive". Moving it needs both entries added to `src/supp/z9_refs.md`, which is outside this unit's files.
3. **S2 and S7 both hold the `delayosc` case** (S2 as the Remark, S7 as one sentence beside the loops table, where the core's pointer lands). If one home is preferred, drop the S7 sentence and let the loops table's `{{delayosc}}` citation carry it.
4. **X1** still says "defensive realism with one more variable" (merge notes, open issue 11; X1 unit).
5. Carried from the merge notes, untouched by this pass: the assembler's `Table` kind (now present); S13's interface names; registers (Test Γ's sign, C8 renamed, Test G's wording, C5's "frontier has not changed hands", EV16's header, CLAIMS marks D); the quotation convention (verbatim versus bracketed repairs; both conventions appear in the paper); §10.4's fifth strand.
