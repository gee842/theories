# U09 elegance pass, editor B: notes

4 October 2026. Files: `core/90_s9.md`, `supp/09_S9.md`. This unit has no Discussion chapter. Both files start from the current `src/` (identical to `planning/snapshots/draftA/src/`), and `src/` was not edited. No files from an earlier attempt existed in this directory.

## Word counts (assembler rule; a citation prints as "Kind N.k", three words)

| | Before | After |
|---|---|---|
| Core §9 (assembler) | 3,089 | 2,393 |
| of which Table 9.1 | ~1,040 | ~970 |
| of which `nounilateral` | 212 | 212 |
| S9 | ~4,320 | ~4,900 (+~580, all received from the core) |

Test assembly in `/private/tmp/claude-501/u09B-scratch` (a full copy of `v6.2/` with these two files in `src/`): 95 core and 33 supplement declarations, **no problems**. Core total 56,966.

### Why the core is about 2,400 words and not about 1,600

About 1,180 words are statements that carry their own conditions:
- Table 9.1, about 970 words. Every cell of the "Needed for, in which model" column is a premise of its row. The "Not needed when" column is what the claim box promises ("with the conditions under which it does not bind [def]"). About 35 citations print as three words each.
- `nounilateral`, 212 words. Parts II–IV cite it (§8(b) `{{>nounilateral}}`, the Scope of `safeguards` in §10, X8, S14), so it keeps its full statement (plan §2).

The table was cut only where a cell carried an illustration, an explanation or a duplicate (list below). It was not cut where that would drop a premise or a qualifier. The merge notes' qualifiers stay: R3a "for the certificate from some date on" / "in the end", and R8a "within a type".

The remaining ~1,200 words are the box (177; the guide is 90–140, see below) and eight short pieces with no other core home:
- the reading of the kinds (test, route, declared);
- what is not a row (the levers);
- the corrector row (the closure of `meta`, the spine);
- the limits of admission;
- form and regulated competition;
- the cooperation conclusion (V6.1, verbatim in substance);
- the unravelling mechanism, which X10 cites as "Section 9, 'coverage can unravel'" and §11.3 relies on;
- the hand-off.

Getting to 1,600 would mean dropping either table conditions or one of these points.

**The box** is 177 words. The Claim's second sentence keeps both of its antecedents: (reach) with a race carrier present, and no rule-maker that reaches every carrier able to carry the host below its floor. The Why keeps the three mechanisms of `nounilateral` and the corrector sentence, which states part (3) and the reflexive closure. I moved "regulated competition included" from the Why into the Claim, so that the Why explains the Claim's second sentence and the Claim states the first plainly.

## Moves (core → S9), each with a pointer left in the core

1. **"What the table does not list"**:
   - Moved to S9, verbatim, as a new paragraph after "Sufficient safeguards": the mechanism of `compound`, the sentence "What sets them apart is that each meets several rows at once", and the `scissors` and `corrrate`(1) sentence.
   - The last sentence gains the names of the two marks, "G2 and G5", as the crosswalk reads them.
   - The core keeps two sentences in the opening paragraph: they are not rows, being alternatives of which any one can carry the margin (`compound`) [thm]; and they are the levers of Section 10.2, each meeting several rows at once (S9).
2. **"Where admission does not reach"**:
   - The full paragraph moves to the end of S9's R8a bullet, as *Where admission does not reach*. It replaces the old pointer sentence "The limits of admission … are stated under the table …", which those limits make redundant. The mechanisms covered: internal deployment; open weights fine-tuned around any constraint; masked detection times sanction against the tax; the control-protocol capability threshold.
   - The core keeps three sentences:
     - Admission reaches only what it admits (Section 6.4), and its limits bound R8a without making it unnecessary.
     - Open weights: release is the admission decision for every later use, and liability on attributable use, the route of R1, is what remains.
     - Masked classes: R8a is necessary and not sufficient; admission is stated in capability, and beyond it the class is stopped (E2) or held to the pace at which control covers it (E3) (`masked`; C12).
   - E2 and E3 are kept distinct.
3. **"Sufficient safeguards, and form"**. Three pieces of the safeguard list move to S9 "Sufficient safeguards", merged into its existing sentences:
   - the `topology` caveat ("they say nothing about whether the correctors' errors are independent");
   - "a threshold set by the host, the floor, the initial composition and the speed of selection";
   - "meet R4 by changing the premise of `enforce` rather than its terms".

   The core keeps a one-sentence list of the four safeguards with "S9 states them with their conditions". The form sentences stay verbatim.
4. **"Which rows need more than one party"**:
   - The row-by-row sentences for R4 (custody, not building, detection), R5 (shared failure), R8a ($(A_\tau)$) and R9 (strength) move verbatim to a new S9 subsection, "Which rows need more than one party", after the proof of `nounilateral`.
   - The core keeps R2, R6, R1 and R3 in one sentence, and says "R4, R5, R8a and R9 do under their own premises (S9)".
   - The conclusion, the "conditional result … not a proof from first principles" sentence and the [val] split are unchanged.
5. **"Reading the rows"** (this paragraph is dissolved):
   - The R2/R5 distinction moves into the table caption: "Coverage is of actors in R2 and of hazard modes in R5 (Section 5.3)".
   - The sentence explaining the R8 split moves to the head of S9's R8b bullet.
   - "R9 is the row for O2" moves to the head of S9's R9 bullet. The rest of the R9 sentence duplicated S9's R9 bullet ("keeping the capacity in practice … costs strength"), and the cost-at-strength point is also in S9's new "Which rows need more than one party".
6. **Table cells** (the material removed is already present in S9, so these are not new moves):
   - R4: "that is $\bar p_{d,i}\ge1$"; and "which a decisive position worth less than cooperation does not by itself give". Both are in S9 R4, and the second is also in the Scope of `restraint` (§5).
   - R5: the description of `opaquecorr` ("a correction architecture … summable without coverage"), now "as under correction whose blocking becomes complete". It is in S9 R5.
   - R6: the examples "verifiable deployments, compute and the performance of contracts". They are in S9 R6.
   - R8a: "so that the safeguard spreads without coordination" and "returns the common cost to the developer". Both are in S9 R8a (the *Not needed* list and *The liability route*).
   - R2: the duplicate `({{join}})` in the model column. `join` is still in the Basis column.
   - Other rewordings change no condition: R2 "too small for their load to carry"; R3a "a level suffices where …"; R5 and R9 "Met, not excused" / "Met without an arrangement" placed first.

## Duplicates removed (true duplicates; where the point lives)

- Box Why, sentence 1, "A requirement stated with its model … can be checked against any design, regulated competition included, which can then be found to meet it". It is now a clause of the Claim ("and any design, regulated competition included, checked against it"). "Found to meet it" lives in the form paragraph ("Regulated competition meets the rows its rules carry …") and in §12.3 ("If regulated competition … meets a row of {{require}}, the text will say so without renaming it").
- Box Why, "and the other requirements weaken through the interfaces that {{thresholds}} marks [thm∣prem]". This is a duplicate of the corrector paragraph ("loses the other rows through the interfaces that {{thresholds}} marks † [thm∣prem]"), which is its home.
- "Coverage can unravel": the readiness sentence ("A readiness rule that demands every dimension at once … (Section 11.3) [conj]"). It duplicates §11.3 (`b0_s11.md`, readiness paragraph: "a pause held past its evidence raises the cost of staying, and coverage tips … ({{unravel}}) [thm∣prem]") and S9's discussion after `unravel`.
- "Where admission does not reach": its fuller sentences are in S9 R8a now (see Moves 2). Three of them also duplicate §6.4:
  - "Admission reaches only what it admits: openly released weights can be fine-tuned around it after release";
  - the internal deployment of research-automating systems (§6.4, last paragraph);
  - capability admission with E2/E3 beyond it, and C12 (after `masked`).

## Preservation check (sentcheck, `--min 0.5`, against `planning/snapshots/draftA/src/core/90_s9.md`; pool = the new core and S9 plus all other current src files)

74 sentences checked; 7 below 0.5. Each is accounted for:

| Containment | Sentence (start) | Disposition |
|---|---|---|
| 0.28 | "**Why.** A requirement stated with its model and its exceptions can be checked …" | Merged into the Claim's first sentence ("and any design, regulated competition included, checked against it"). "Found to meet it" duplicates the form paragraph and §12.3. |
| 0.49 | "Every sanction, observation and count of coverage that the requirements call for is a corrector's act …" | Kept, shortened, in the box Why. Its last clause duplicates the corrector paragraph. |
| 0.33 | "The kind of support decides how a row may be used." | Kept in other words: "The kind of support decides the use: …" |
| 0.12 | "Reading the rows. Two senses of coverage are kept apart:" | Merged into the caption ("Coverage is of actors in R2 and of hazard modes in R5 (Section 5.3)"). |
| 0.47 | "R5's is of hazard modes, the share of hazardous variety under correction that meets the four conditions of Section 5.3." | Merged into the caption with a pointer to Section 5.3, where coverage $U_t$ is defined ("meets four conditions at a stated catch rate"). |
| 0.28 | "A readiness rule that demands every dimension at once … [conj]" | Duplicate of §11.3 and of S9 after `unravel` (see Duplicates). |
| 0.43 | "Coverage can also fall without an exit, when the largest participant is exempted (EV18, read in X10) [obs], so the threshold is stated in coverage weighted by share, not in numbers of parties." | Kept in other words: "exempting the largest participant lowers coverage with no exit at all (EV18, read in X10) [obs]"; and "… participation threshold, in coverage weighted by share, not in numbers of parties, and type by type". |

S9 against the snapshot's S9 (same pool): 122 sentences checked; 1 below 0.5:
- 0.10, "The limits of admission, internal deployment, open weights and masked classes, are stated under the table, because none of them removes the requirement." This pointer is replaced by the limits themselves (Moves 2). Its "because none of them removes the requirement" survives as "None makes R8a unnecessary, which is why Section 9 states them as limits and not in the table's last column".

Edited in place in S9 (containment of the old sentence against the new S9 alone, below 0.9):
- "Sufficient safeguards" sentence 1 (0.81) and the `restraint`(a) sentence (0.53): extended with the material moved from the core.
- The readiness sentence (0.81): re-tagged; see Other changes.

## Other changes

- **The S9 readiness sentence is re-tagged.** "errs toward 'not ready' (Section 11.3) [thm], so an arrangement that holds participants longer than its evidence warrants raises the cost of staying and spends its coverage [thm∣prem]". It was a single [conj].
  - §11.3 now carries the mechanism with these tags: the $0.95^7\approx0.70$ conjunction bias is [thm], and the cost of staying and the tipping are [thm∣prem] with `unravel`.
  - The old [conj] dated from before §11.3 landed (merge notes, open issue 6).
  - This is a tag alignment, not a change of mathematics. The integration editor should confirm it.
- The `unravel` sentence in the core now states the bistability condition: the cost of standing outside goes from above the cost of staying when none stand outside to below it when all do, which is $s_k(0)>c_k>s_k(1)$. That is the "one core sentence that carries their conditions" for an S-numbered result. The old core sentence said only that the cost of standing outside falls.
- R1's "(the scope of {{load}})" and R4's "and ordinary repetition decides" are kept. The second says what still governs when $p_d=0$ (the ordinary repetition condition of `restraint`), so "not needed" is not read as "nothing needed".
- Heading "Reading the rows" removed; the others are kept. X10 cites "Section 9, 'coverage can unravel'", and that heading is unchanged.
- No mathematics changed. No key or tag dropped:
  - every result key cited before is still cited in the core or S9;
  - `{{>safeguards}}` remains the only forward pointer;
  - all Table 9.1 tags are unchanged.
- No named states or firms. E2 and E3 are kept distinct ("stopped (E2) or held to the pace at which control covers it (E3)").

## Open issues

1. **R9** is still awaiting Ren's confirmation (merge notes §4, item 1). If it is kept, three files still say "R1–R8":
   - `core/d0_symbols.md` (line 20);
   - `reg/LEDGER.md` (line 112);
   - CLAIMS/README.
2. **Length.** The core is about 2,390 words against a target of about 1,600, for the reasons under "Why the core is about 2,400 words and not about 1,600". If a further cut is wanted, the next candidates are, in order:
   - the "Where admission does not reach" paragraph, down to its first sentence plus "(S9)", since §6.4 and `masked` hold the rest;
   - the list of the four safeguards, down to "S9 lists four sufficient safeguards";
   - the R3a "Not needed when" cell, down to its clauses with "(S9)", keeping "from some date on" and "in the end".
   
   Each cut makes the core reader turn to S9 or §6.4 for a point now stated here.
3. **The box is 177 words**, above the guide of 90–140. I kept it because shortening it would mean dropping an antecedent of Claim sentence 2 or the corrector sentence of the Why.
4. **S9 now has a separate "Which rows need more than one party" subsection.** If the integration editor prefers fewer subsections, it can join the end of the `nounilateral` proof.
5. These merge-notes items are unchanged by this pass and still open:
   - item 5, the crosswalk findings for §11 (R1, R2, R7 and R8b have no readiness dimension; §11.3 now says "Readiness does not ask for four rows …", so this is resolved);
   - item 7, the EV18 wording in X10, which is already updated in `disc/10_X10.md`;
   - item 9, no check block for the R5 necessity derivation or for the multi-type part of `unravel`.
