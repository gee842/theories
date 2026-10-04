# U02 elegance pass, editor B: §2 (core/20_s2.md) and S2 (supp/02_S2.md)

4 October 2026. Start: the current `src/` files (identical to `planning/snapshots/draftA/`). Read: V6.2-PLAN, merge notes U02, D1-opus §3.3 (§2 spec, 2,400 words) and §1.4/§1.5, the current §1, §3 (standprice, twoerrors, Ψ), X2, S0, the symbol table, and every citation of a §2 key or of "Section 2.x" in the other units. The directory held an interrupted earlier attempt (a core file about 5% shorter than the start, no supp file); it is superseded by the files here.

Files: `core/20_s2.md`, `supp/02_S2.md`, this note. Nothing in `src/` was touched.

## 1. Word counts (assembler's rule; formulas count as one word)

| | Core §2 (assembler, with headings and the Part I lead) | S2 |
|---|---|---|
| Start (= draftA snapshot) | 4,007 | 4,810 |
| This pass | 3,625 | 4,889 |

Scratch assembly (`/private/tmp/claude-501/u02B-95743`, with these two files in `src/`): 95 core and 33 supplement declarations, **no problems**. Sentence check: core 145 sentences, 7 below 0.5 (adjudicated in §4); S2 142 sentences, 0 below 0.5.

## 2. Why 3,625 and not about 2,700

The guide was 2,700. The deviation is about 925 words, and here is what they carry. The core of §2 now has about 2,000 words that cannot leave without making it less correct or less complete in its conditions:
- the four statements with their premises inside them (`cond` 160, `loopgain` 44 + 434, `compound` 242, `meta` 146 = 1,026), of which `loopgain`(4) with its two decisivenesses (about 115) and `compound`(2) restated with its premises (about 130) are additions the plan requires over V6.1;
- the two Scope paragraphs (172 + 102): each says what the result does not cover and what makes it fail, and the `loopgain` Scope carries the one number the box relies on (the equilibrium gain above one at a structural gain of 0.45) and the premise failure of (4);
- the box as the plan fixes it, D1-opus plus the corrected lever sentence by channel (186);
- Ren's six lines verbatim with their keys (about 140);
- the lever paragraph (196), which §7.1 (twice), §8.2, §10.1, §10.3 and §12.2 cite as "Section 2.2" for specific claims (channel by channel; provision changes nothing in a level channel; the wrong lever; blocking diffusion raises the gain; diffusion as the third inflow);
- the "does not decide" paragraph (176), the home of the two conditions §1.2 summarizes and of "Γ is not estimated" (Test Γ) and Λ* (S7, S13).

The remaining 1,600 words are §2.1 (286), the mapping of Ren's sentence (101), §2.3's prose (about 785, including Definition 2.4's gloss, the meta-attractor of winning, the one-sentence `bench`, the hurricane line and `pathgen`), §2.4 (239) and three bridges. D1-opus's 2,400 predates (4), the Scope's strategic-response clause and the lever paragraph. Two further moves would bring the core to about 3,500 and are not mine to make, because they need Discussion files outside this unit (open issues 1–2).

## 3. Moves (core → companion), with the pointer left behind

| What left the core | Where it now lives | Pointer in the core |
|---|---|---|
| `loopgain` Scope: "r^eq/r is 1.09 at a structural gain of 0.2 and 1.18 at 0.3, and about 2.5 to 5.4 at structural gains from 0.45 to 0.9, where Γ^eq exceeds one and equal standing breaks although Γ<1" | S2 `eqgain`, closing paragraph (new sentence, [num: MP]; the table above it holds the individual values) | "Γ^eq exceeds one already at a structural gain of 0.45 … [num: MP]; … {{eqgain}} gives the magnitudes" |
| `loopgain` Scope: "The stability calculation is standard (X1 gives the lineage); what is new is the organization, with provision and diffusion inside the gain, and its consequence for objectives (Section 3.5)." | S2, *Bounds*, new last bullet (verbatim) | none needed: §1.4 states the paper's novelty once ("the loop gain that interconnects the conditions"), and §2.4 points to X1 for the lineage |

Everything else that left the core was a duplicate of text that already has its home (§4 below); no other text was added to S2. S2 grew by 79 words.

## 4. Preservation check, adjudicated

Seven sentences of the snapshot core fall below 0.5 containment. Each is accounted for:

| Flagged sentence | Verdict |
|---|---|
| "The neglectful organization need not be more capable in general." | Merged into §2.1 ¶1: "the neglectful one need only be more capable at securing the resources that decide survival and expansion". |
| "A population of practices changes because some practices expand, are imitated or replace others, while many individuals keep their values." | Merged into §2.1 ¶3: "practices expand, are imitated or are replaced while many individuals keep their values". |
| "The question is not only what people believe is good but which practices receive the means to continue." | Merged into the same sentence: "what decides is which practices receive the means to continue"; the contrast with belief is carried by the paragraph's first clause ("Nothing here requires that people be or become selfish") and its last ("The primitive is selection, not greed"). |
| "The channels add only because one win share feeds every stock: a stock fed by an expenditure chosen under another rule, such as lobbying bought from profits by a separate decision, is not a term of the sum." | Kept in other words in the Scope: "reinforcing and fed by the one win share … a stock fed by a separate decision, such as lobbying bought from profits, is not a term of the sum"; the "add because" clause is also `loopgain`(1). |
| "If it stays fixed while capacity grows without depreciation, the condition of (1) holds date by date with the current total (S2)." | Duplicate of S2 *Growth variants* (a) ("with S the current total, a condition that changes with time"); the core Scope now says "S2 gives the condition of (1) for a prize that stays fixed while capacity grows". |
| "Practices that produce more publications receive more funding, attract more students and are more widely copied." | Merged into §2.3 ¶2: "funds, staffs and copies the practices that produce more publications". |
| "Now add one step: their practitioners come to occupy the positions that decide recruitment, training and evaluation." | Merged into the same sentence: "once their practitioners occupy the positions that decide recruitment, training and evaluation". |

Sentences removed that the check did not flag, because their trigrams exist elsewhere in the paper (true duplicates, each with its home):
- `loopgain` Scope, "Where such a contest runs in many small rounds, a winner-take-all equilibrium coexists with the smooth one already at a structural gain of 0.2; and where standing below the top is costly enough that a laggard tries harder, the strategic correction shrinks, and in one computed case reverses [num: MP; both held for outside review]": S2 `eqgain`(4) and (5), labelled "held for outside review"; in the core, §3.8 carries the multiplicity and §3.5's Scope the catch-up reversal. The §2 Scope keeps "two findings held for outside review" with the pointer.
- `compound` Scope, the explicit proportional-prize condition "κ_c g((1−β)r−1) > δ_f" and "the condition does not drift": S2 *Growth variants* (b). The core keeps the no-provision, no-diffusion form (1−β)r>1 and the {{>standprice}} link, which §3.5(2) relies on.
- `compound` Scope, "as at K̄=K* with diffusion, their own losses to diffusion enter": S2 *Leaders held*. The core keeps the bound and "held by assumption".
- "with a little diffusion alone a laggard can stall short of the cap [num: CE]": S2 *Numerics (CE)*, "Not a guarantee … stalls at 0.16 of the cap". The core keeps "a source, not a guarantee [num: CE]".
- "an objective satiable in the stakes has a point of enough, and relative standing has none": the statement of {{enough}} (§5.5). The core keeps "Who stops at a cap is a question of objectives, not of the loop ({{>enough}})".
- Lever paragraph, the three cases of correction in a ratio channel ("leaves that channel's gain unchanged without diffusion, raises it with diffusion, and always raises the discounted gain") and "Provision lowers it through capacity and changes nothing in a level channel, where it adds the same to everyone": S2 `chansign`(2) and (3), cited at the head of the paragraph. The core keeps the mechanism (invisible to a contest of ratios; raises the discounted gain; adds the same to everyone, dilutes what is won in a ratio channel, changes nothing in a level one), the {{>blind}} link, the wrong lever, the trees line and the diffusion consequence.
- §2.2, the parenthetical list "(the rules, the evaluators and correctors, the formation of minds, the language in which success is described)": §2.3 ¶1, its home.
- "and every claim says which of the three senses it uses" (the *Why "meta-attractor"* paragraph): Definition 2.4's opening sentence. The rest of that paragraph is merged, in full, into the paragraph after the definition.
- `bench`: the two core sentences are now one, with the same conditions (decays in (0,1], non-negative coefficients), "same form, not a case" and "names a channel"; the full remark is S2 Remark S2.6.
- §2.4, the one-line instances "In security competition a gain for one is read as a threat to another", "Members of a federation compete for capital and residents, and the strongest can capture the centre", "In science, metrics allocate positions and the positions then set the metrics", "In training, a policy is selected by a reward that a developer sets, and the developer is selected by a contest": X2 (States, Federations, Science, Training loops), verbatim or fuller; the science line is also §2.3 ¶2. The core names the substrates and points to X2, as D1-opus §1.5 asks ("substrates briefly (§2.4), instances in X2").
- §2.4, "in the channels named above" and "reproducible units that gain or lose share": the second is Definition 2.1's gloss of carriers.

## 5. What is unchanged

- Every key (`cond`, `loopgain`, `eq:stocks`, `eq:gamma`, `compound`, `meta`, `pathgen`; S2's `tdec`, `eqgain`, `delayosc`, `chansign`, `gammarange`, `bench`, `eq:secular`), every citation ({{>standprice}} ×2, {{delayosc}}, {{eqgain}}, {{>enough}}, {{chansign}}, {{>blind}}, {{tdec}} ×2, {{gammarange}}, {{>thresholds}}, {{bench}}, {{>noinside}}, {{cond}} ×3, {{loopgain}} ×2, {{eq:gamma}}) and every claim tag.
- Every statement, word for word, with its premises: Definition 2.1 (three conditions plus the reflexive closure), Proposition 2.2 (1)–(4) and its Model, Proposition 2.3 (1)–(2), Definition 2.4, Remark 2.5. No mathematics changed; no error found.
- Ren's six lines, verbatim with their keys and the bracketed repairs as they stand: "The agent that only optimiz[es] capital value…" [corpus: meta-attractor]; "if you use what you have to compete for more … and trade everything for winning" [corpus: selfishness-spiral], with the clause mapping; "Trees are providers" [corpus: shengsheng]; the game-design rule with "Then the game collapses" [corpus: possibility-space]; "more like a hurricane than a black hole" [corpus: meta-attractor]; "change the basin, then add speed" [corpus: meta-attractor].
- The Ren rulings of this round: carriers glossed at first use; the completed sentence; the box's lever sentence by channel ("at least in proportion"); §2.4 ends in one hand-off sentence; the analytic step for §2.1's corpus claim with the empirical extent handed to Part II; "provision not won in the contest" defined once as "provision beneath the game".
- Plan §8 vocabulary throughout: structural loop gain, equilibrium gain, price of standing, won share, provision beneath the game, selection pressure of winning, meta-attractor of winning.
- Everything the other units cite as "Section 2.x" still stands at that place (checked against §1.2, §3.5, §4.1, §7.1, §7.4, §8.2, §10.1, §10.3, §12.2, S5, S7, S13).
- The S2 text is the snapshot's plus the two sentences in §3; nothing in S2 was rewritten.

## 6. Other changes of form

- §2.1 ¶1 and ¶2 are one paragraph (thesis, then the two organizations); ¶3 opens with "The step is analytic" placed before the quotation it governs.
- The reflexive-closure sentence after Definition 2.1's three items now italicizes *closes on itself*, marking it as the definition's fourth clause (Ren's decision 1: three conditions plus the reflexive closure).
- The *Why "meta-attractor"* paragraph is merged into the paragraph that follows Definition 2.4 (one home for what the name adds).
- §2.3 ¶1's last sentence is joined to the one before it; §2.3 ¶2 is one worked sentence plus the transition sentence.
- The Scope of `loopgain` orders its conditions as the plan asks: domain, reinforcing channels and the rank-one premise, (4)'s number and failure case, benchmark, pointer, proof.
- "Discussion X2" is now "X2", the convention of the other sections.

## 7. Open issues

1. **A further move to X2.** The research-community example (§2.3 ¶2, about 100 words) is a worked instance; X2 "Science" has its one-line form. Moving the worked paragraph to X2 and keeping the transition sentence in the core would save about 60 words. X2 is outside this unit's files, so it is not done here.
2. **A further move to X1.** The "generator functions" comparison (about 55 words of the paragraph after Definition 2.4) is lineage; X1 is its natural home, with one clause left in the core. Not done for the same reason.
3. The lever paragraph no longer spells out the three cases of correction in a ratio channel (unchanged without diffusion, raised with diffusion, discounted gain always raised); it says "invisible to a contest of ratios … and raises the discounted gain", with `chansign`(2) cited at the head of the paragraph. If the integration editor wants the three cases in the core, it is one clause (about 20 words).
4. Downstream, unchanged from the merge notes: S13's row should read "T_dec set by Λ*", not by Γ; §1.2 item 1 still says the loop gain "prices standing for every actor", which the merge notes judged false as stated (the §2 box and `loopgain`(3) now carry the conditions).
5. "The author" is used five times in §2, as before; the integration editor settles one form across the core.
6. The earlier interrupted attempt's file in this directory is overwritten by this one; it had no supp file and no notes.
