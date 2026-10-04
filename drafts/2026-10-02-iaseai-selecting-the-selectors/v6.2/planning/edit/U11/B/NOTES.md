# U11 elegance pass, editor B: Section 11 (`core/b0_s11.md`), S11 (`supp/11_S11.md`) and X11 (`disc/11_X11.md`)

4 October 2026. The starting point was the current `src/`, byte-identical to `planning/snapshots/draftA/src/` for all three files (checked with `diff -q`). No files from an earlier attempt were in this directory. Edited files: `core/b0_s11.md`, `supp/11_S11.md`, `disc/11_X11.md`.

**Result.**
- Core §11 is **4,880 words** by the assembler's count, down from 5,921 (−1,041). Raw, with a formula counted as one word, it is 4,927, down from 5,987.
- S11 is 4,901 raw (+670). X11 is 2,936 raw (+483).
- The numbering is unchanged: Corollary 11.1, Proposition 11.2, Proposition 11.3, Definition 11.4, Table 11.5; Remark S11.1, Proposition S11.2, Remarks S11.3–S11.4. That gives 95 core and 33 supplement declarations.
- The assembler reports **no problems**, and `xref_v62.py` reports must-stay 32/32 and no named states or firms.
- The bibliography lists are unchanged: THEORY 103 cited, SUPPLEMENT 89, DISCUSSION 92/92, with the same uncited and missing entries as before.
- The mathematics is unchanged. No error was found.
- Test assembly: `/private/tmp/claude-501/u11B-elegance/`, a full copy of `v6.2/` with the three files put in place.

## 1. On the target (about 3,200)

The core is about 1,680 words over the guide. I judge it to be at the frontier: every further cut I could find either drops a premise or moves something that a later section or the plan needs in the core. The extra words carry the following.

**Statements that later sections cite or the plan names, kept in full (about 1,030 words).**
- `signal` (244). §8.3 cites it (`80_s8.md` l.76), and so does §12.1 item 5.
- `readiness` with its table (357). §12.1 tier 2 *Release* reads "the slow variable it rests on" from it.
- Table 11.5 with its support column (427). Plan §2 makes it "[def, with support]", and every cell carries a tag and a condition.

**The box (229).** It makes eight tagged claims, each with its antecedent. It was 269.

**V6.2 content that V6.1 did not have, each item named in plan §4 §11 or by a ruling.**
- Counter-performativity (MacKenzie), the home of §0's last clause.
- Dwell depth, with the recruitable lineage at 10.45 → 3.81.
- The readiness decision rule. U09's elegance merge dropped §9's readiness sentence because §11.3 is its home (`0.95^7≈0.70` [thm] and the `unravel` tipping [thm∣prem]), so it must stay here.
- Narrow E1's link to `detectlink`.
- The condition under which E1 has to be held in common.
- The three Ren lines.

**Ren rulings.**
- "Broad E1 is the scope; narrow E1 is the first step".
- E2 "can be large (crux C10)", with its cost argued at its strongest.

**Further moves I considered and declined, with their savings.** Each would make the core less useful to its reader. The comparator may weigh them differently.

| Move | Saving | Why declined |
|---|---|---|
| Readiness table → S11 | about −190 | It is the content of the definition §12 cites |
| Tracks table → X11, as one prose sentence | about −100 | §12.1's "longest time constant starts first (Section 11.4)" reads it |
| Deterrence paragraph to one clause | about −80 | The merge kept it to meet the objection at its strongest |
| Precedents to two sentences, with the BWC, nuclear-power and Montreal lessons to X11 | about −90 | Plan §4 §11 wants "precedents with their limiting conditions" in §11 |
| "Where things stand" to a pointer | about −50 | It is the hardest case, which D1-opus §1.4 keeps in the core |

## 2. Part by part

| Part | What changed | Why |
|---|---|---|
| Part IV lead | Unchanged | — |
| Claim | The two [def] sentences become one ("…not thereby one they can reach: a path is reachable when …"). "A step that moves a parameter without carrying the state across its threshold, or that is released on share levels before its dwell" becomes "a step released before its slow variable has crossed its threshold". "Unless a lineage … can be recruited when the rule changes" becomes the antecedent "without a recruitable lineage of the alternative" | Same claims, conditions and tags. The two cases of re-absorption are one condition: release before the slow variable has crossed. "Recruitable" is defined in §11.4 |
| Why | "Rule support falls only at the rate at which it is corrected, while shares lag it" becomes "Shares lag rule support". "And meets its own compensating loop" leaves the box | The mechanism has its home in §11.4's dwell paragraph. The compensating loop has its home in §11.4 ("Each track meets a compensating loop of its own …") and X11's first table. The "third erosion" clause stays (D1-opus's box draft) |
| Trust paragraph | Verbatim | V6.1's "confidence in … instruments of verification" is one of trust's three meanings |
| `relaxtrust` | Declared inline in the core, as `freeze`, `nonsum` and `join` already are: "(**{{!Corollary:relaxtrust}}**, S11) [thm]". The core keeps the conclusion with its conditions: $g_C,g_D>0$ for the belief threshold; $T-P+F>0$ and $P>S$ for verification; a sanction acts only while it can be imposed, and through $\bar p_d$ against a decisive defector. The four-part statement, verbatim, opens S11 as "Corollary 11.1 in full", followed by its proof | It is a corollary, a set of differentiations of `assure`, `talk` and `overhang`. Only Table 11.5 and X10 cite it, by key, and both still resolve. Its key and number are unchanged. The verification clause states the sufficient conditions of (2), not a necessary "only where" |
| Levers | "Which the comparison counts in $\Theta$" becomes "counted in $\Theta$". The common-frontier sentence is joined with a semicolon | — |
| Trust as outcome; Ren's line | Verbatim. The must-stay "Trust is mainly an outcome" is present | — |
| Obstacles | The narrow-E1 sentences move to §11.3 E1, where narrow E1 has its home | "It removes AI from decisions …, so it leaves $p_d=1-\upsilon(T_{\rm dec})$ where it was ({{detectlink}})" is now in the E1 paragraph. "Narrow E1 is a first step that needs no trust" and "among actors who price in a certain lock it is a gain, not a cost" duplicate E1's strict-equilibrium sentence and the box |
| Counter-performativity | Light tightening only | Home of §0's clause |
| Carriers | "A finding of exploratory analysis" becomes "in exploratory analysis" (V6.1's words). "Shared understanding removes one road … but not the others" is now one sentence | — |
| `signal` statement | Verbatim | Cited by §8 and §12 |
| `signal` Scope | Two sentences: measured costs, with $c_{\mathsf S}\le0$ possible under a certain lock and $c_{\mathsf R}$ the speed forgone; uniqueness under the intuitive criterion. The full reading of costs moves to S11 as *The costs, read from the lock* | The scope says what would make the result fail; the illustration moves to S11 |
| After `signal` | One sentence. "Which is the difference a signal needs" is dropped (it restates the result's lead). "It answers a misjudgment of a rival's present objective; a correct forecast … (Section 3.8)" is dropped as a duplicate | That sentence is in §3.8 (`30_s3.md` l.123, which points here) and in the last sentence of the counter-performativity paragraph |
| §11.3 opening | "Differ in cost, verification and failure" | Same content |
| E1 | Narrow form: limits, fallback and the evidence channel go into the defining sentence; the $q_L=1$/`nearlock` sentence is verbatim; the `detectlink` sentence comes in from §11.1. Tactical domains are verbatim, without the cyber-defence example (now in X11's narrow-E1 section). Broad form: "AI not an instrument in any contest that tends toward dominance or concentration", with criterion and enforcement in §6.6. Ren's bold line is verbatim. "Held in common" is now one sentence with its condition | "In labour, finance and persuasion as much as over shared conditions, judged by the game and not by the act" duplicates §6.6 (`60_s6.md` l.103) and §12.1 "The scope" (`c0_s12.md` l.41), both in Ren's words |
| Deterrence objection | Tightened. The strongest form, the four answers in theory terms, 1983 with (Podvig 2002; Hoffman 2009) [obs: EV18], `blind` [thm∣prem], and the X11 pointer are kept | "When an officer judged an alarm false and did not report an attack" is in X11 answer 3 (verbatim detail) |
| E2 | Arrow–Fisher is folded into the cost sentence; the coercion sentence is reworded | Every clause is kept: decisive class only; lives; C10; irreversible for those who bear it; option set; consent or coercion; escalation in $\Theta$; §12.1 as the single home of coercion |
| E3 | Verbatim | — |
| Pause and `pausevalue` | Declared inline, "(**{{!Proposition:pausevalue}}**, S11) [thm]". The prose states all three parts with every premise: no added hazard; the same process resumes; zero where the hazards are not summable; bounded away from zero after summability; in the field model, completion of capture above $1/G$. The full statement opens S11 "Proposition 11.3 in full". The pause paragraph and the bold certificate sentence are kept | It is not cited outside §11, and the box keeps "A pause that changes nothing buys time, not survival". The numbering is unchanged |
| `readiness` | Verbatim, except "since resuming too early is the error that cannot be undone" | That clause duplicates S11's readiness paragraph ("declaring a dimension met too early is the error the protection standard weighs, since resuming cannot be undone") |
| Readiness table | The third column is shortened to the slow variable and the period its residence must cover. The removed clauses go to S11, *The residence times of Definition 11.4, in full*: Q3 "long enough to show provision keeping pace with them"; Q4 "not the return of shares to their former level"; Q5 "across which catch rates of planted defects at fixed human hours stay level"; Q7 "against the time to a decisive position", "since the net gain from exit grows with it" | — |
| Readiness paragraph | Pointers to S11 and X11 are added. "Readiness is the release rule of the second tier of Section 12.1, read on indicators of its own …" is dropped as a duplicate. "Resuming unchanged after a pause …" moves to S11. Residence and decision-rule reasons are kept with their tags | The dropped sentence duplicates §12.1 tier 2 *Release* (`c0_s12.md` l.29) and §11's own hand-off |
| The order | The three orders are kept. The EV9 numbers and "a rate condition that verification must meet" are dropped as duplicates. The gloss "stopping before the decisive class is built, or bringing development below the speed …" is dropped | The EV9 material is in X11 *Feasibility*, verbatim, with the 1.5×–64× range. The gloss duplicates the E2 and E3 paragraphs and §5.3. EV9, EV17 [obs] and "proposed and prototyped" (register wording) stay |
| Tracks paragraph | Tightened. "Named in the third column of the table below" is dropped | Structural |
| Tracks table | Two columns: Track, and Slow variable with its time constant (cells verbatim). *What is committed*, *Mechanisms acted on*, *Compensating loop to anticipate* and *Indicator of progress* move verbatim to X11's first table | The slow variable is the theory's content. §12.1 lists what is committed now, tier by tier |
| After the table | One new sentence: "Each track meets a compensating loop of its own, from … the first to … the fifth; X11 gives …". The slowest-first sentence keeps its consequence (tracks 3 and 4 begin before their trust; the openness of track 5 from the first; hence §12.1's first two tiers together). "Rule support … moves slowest, custody … ahead of any warning" moves to X11's tracks paragraph | That clause also duplicates the table's Track 3 and Track 4 cells and S11's track list |
| Dwell | Mechanism, [thm] sentences, Test D, observability, the unbounded-depth [thm], and the lineage bound [thm] with 10.45 → 3.81 versus 10.44 [num: DW] are kept, now stating their conditions inline (share 0.99, $G=10$, rule-making ten times slower, units $1/(\varepsilon d)$). The fixed-$G$ caveat and [conj] are kept. The ranges 1.89–10.45 and 5.86–16.18, and 28.9 at $1-10^{-12}$, are dropped from the core | Those numbers are in S11 `dwell`(2) and *Numerics* (duplicates) |
| Decay and renewal | Mechanism sentence and Ren's line verbatim. "This is the second job of plurality that Section 10.4 names …" moves to S11 `dwell` *Scope* | §10.4 (`a0_s10.md` l.79) already points here for it |
| Ratchet | Kept with its condition (each step carries its slow variable across and is held for its dwell) and its closing line. "Since a step that moves a parameter without crossing is re-absorbed ({{reabsorb}}) and one released on levels is premature" is dropped | It duplicates the box, the tracks paragraph and the dwell paragraph ("premature (Test D)") |
| Windows | Kept: the keystone [conj], the closing window, Gunderson–Holling [obs], the prepared design, the end condition for an emergency closure (with an X11 pointer), and standing on every track | Reworded only |
| Where things stand | Two sentences: the seeds of the first two tracks; narrow E1 with no multilateral document; the slow tracks without a seed; "binding, verifiable and broader". The D4 C1 verified paragraph moves verbatim to X11, *Where things stand* | Plan §1.4 (D1-opus): "keep the principle and the hardest case in the core; the detail goes to the companion" |
| Table 11.5 | Verbatim | — |
| Capture basin | One sentence. "The basin for several domains, with the host's floor and with disturbances, is not computed" is dropped | It duplicates S11 `capturebasin` *Not proved*. "Proved only in the one-domain field model" keeps the scope |
| Precedents | The 1946 lesson and the saturation conditional are verbatim. BWC, nuclear power and Montreal are one sentence, each with its limiting condition: military value low with another deterrent held, and a covert programme without verification; the shared loss returns to its source and no prize is decisive, "a change of selection, not of motive"; substitutes made the value of winning low. "With later lapses" is dropped | That phrase is in X11's nuclear row ("later lapses show the durability is not automatic") |
| Hand-off | Verbatim | — |

## 3. Moves (core → companion)

| Left the core | Now in |
|---|---|
| `relaxtrust` statement, parts (1)–(4) (verbatim) | S11, *Corollary 11.1 in full*, before its proof |
| `pausevalue` statement, (1)–(3) (verbatim) | S11, *Proposition 11.3 in full*, before its proof |
| `signal` Scope: "that type takes the step whatever the receiver does"; "the longer the period, the larger $c_{\mathsf R}$" (the whole original sentence) | S11, *The costs, read from the lock*, after *The signal and its imitation* |
| Readiness table, third-column clauses for Q3, Q4, Q5, Q7 | S11, *The residence times of Definition 11.4, in full* |
| "Resuming unchanged after a pause would repeat the process that made the pause necessary." | S11, end of the `pausevalue` example ("Read on the indicators of {{readiness}}, …") |
| "This is the second job of plurality that Section 10.4 names: lineages kept inside selection and able to grow make reform possible in bounded time, as well as decorrelating errors." | S11, `dwell` *Scope* |
| Tracks table columns *What is committed*, *Mechanisms acted on*, *Compensating loop to anticipate*, *Indicator of progress* (cells verbatim) | X11, *The tracks, by commitment*, first table. The opening sentence there was rewritten to introduce both tables; "Compensating loops beyond those in the core" became "… in the first table" |
| "Rule support in the corrector domains moves slowest, custody has to be prepared further ahead of need than any warning gives" | X11, the tracks paragraph |
| "Where things stand" (D4 C1 verified wording: the panel's first report; the opposition to its appointment, "an overreach"; the multilateral declaration and the General Assembly resolution; "its only shared basis is that bilateral affirmation"; the official's rejection; developers' contingent commitments; EV2, EV7, EV8; EV3, EV17) | X11, *Where things stand* (new subsection, before *Readiness, read today*) |
| "Such as response in cyber defence within stated limits" | X11, *Narrow E1 and the value of commitment*, last paragraph |

## 4. Duplicates removed (text that left the paper's core with its point kept elsewhere)

1. "It answers a misjudgment of a rival's present objective; a correct forecast of what the game will select is answered only by changing what it selects (Section 3.8)." The same sentence is in §3.8 (`30_s3.md` l.123), and §11.2's counter-performativity paragraph ends on the same point.
2. "Readiness is the release rule of the second tier of Section 12.1, read on indicators of its own rather than on those of activation run backwards." This is in §12.1 tier 2 *Release* (`c0_s12.md` l.29) and in §11's hand-off.
3. "Narrow E1 is a first step that needs no trust", and "among actors who price in a certain lock it is a gain, not a cost ({{delegatelock}}(1))". These are in the box and in §11.3 E1's strict-equilibrium sentence.
4. The order's gloss "stopping before the decisive class is built, or bringing development below the speed at which understanding and response can follow". This is in the E2 and E3 paragraphs and §5.3.
5. The order's EV9 figures and "a rate condition that verification must meet". These are in X11 *Feasibility*.
6. The dwell ranges (1.89–10.45; 5.86–16.18) and 28.9 at $1-10^{-12}$. These are in S11 `dwell`(2) and *Numerics*.
7. Ratchet: "since a step that moves a parameter without crossing is re-absorbed ({{reabsorb}}) and one released on levels is premature". This is in the box, the tracks paragraph ({{reabsorb}}) and the dwell paragraph.
8. Broad E1's "in labour, finance and persuasion as much as over shared conditions, judged by the game and not by the act". This is in §6.6 (l.103) and §12.1 "The scope" (l.41).
9. Readiness definition: "since resuming too early is the error that cannot be undone". This is in S11's readiness paragraph.
10. Capture basin: "the basin for several domains, with the host's floor and with disturbances, is not computed". This is in S11 `capturebasin` *Not proved*.
11. Deterrence: "when an officer judged an alarm false and did not report an attack". This is in X11, answer 3.
12. Precedents: "with later lapses". This is in X11's nuclear-power row.
13. "Which is the difference a signal needs" restates `signal`'s lead sentence. "Named in the third column of the table below" and "and the next subsection gives it" are structural.

## 5. Preservation check

The command, run in `/private/tmp/claude-501/u11B-elegance`:

`python3 src/sentcheck.py …/snapshots/draftA/src/core/b0_s11.md src/core/*.md src/supp/*.md src/disc/*.md --min 0.5`

The pool is my three files and every other current core, supplement and discussion file. **153 sentences checked; 6 below 0.5.**

| Containment | Sentence (start) | Disposition |
|---|---|---|
| 0.42 | "Keeping AI out of the contest, stopping, slowing and pausing are different choices, with different costs, different verification and different failures." | **Kept in other words**: "… differ in cost, verification and failure." |
| 0.27 | "A temporary pause is the fourth arrangement, and by itself it changes nothing." | **Merged** into "A temporary pause, the fourth arrangement, is valued by what changes during it …" and "A pause that changes nothing buys time, not survival." |
| 0.32 | "Readiness does not ask for four rows of {{require}}, R1, R2, R7 and R8b ({{crosswalk}}); it presupposes them, since no pause supplies them." | **Kept in other words**: "Readiness presupposes rows R1, R2, R7 and R8b of {{require}} ({{crosswalk}}), since no pause supplies them." |
| 0.27 | "The residence condition is there because levels move before slow variables cross: shares fall back while rule support still sits in the basin of capture (Section 11.4)." | **Merged**: "Residence is required because levels improve before safety does (Section 11.4)". The mechanism is stated in the box's Why ("Shares lag rule support, so levels improve before safety does [thm]") and in the dwell paragraph ("shares are back at their starting level before the state has left the basin of capture [thm]") |
| 0.40 | "Readiness is the release rule of the second tier of Section 12.1, read on indicators of its own …" | **Duplicate** of §12.1 tier 2 *Release* and of §11's hand-off (§4 item 2) |
| 0.44 | "From a captured share of 0.99 the hold that is needed runs, in units of $1/(\varepsilon d)$, from 1.89 to 10.45 …" | **Moved/duplicate**: S11 `dwell`(2) gives 1.89, 5.32, 10.45 and 5.86, 10.34, 16.18. The core keeps 10.45 → 3.81 with its conditions |

**Sentences between 0.5 and 0.85.** These were reworded or compressed (40 below 0.85 at the 0.85 setting). Each is accounted for in §2–§4. The ones with a moved part:
- The box sentences (§2).
- The obstacles' narrow-E1 sentence (moved within the core to E1; duplicate part §4.3).
- The order (§4.4, §4.5).
- The tracks-table header (the columns moved to X11).
- "Slowest first …" (part moved to X11).
- The dwell depth sentence (numbers to S11).
- The ratchet (§4.7).
- Windows (reworded).
- Capture basin (§4.10).
- Nuclear power and Montreal (merged into one precedent sentence; "with later lapses" §4.12, "once substitutes were available" kept as "once substitutes had made the value of winning low").

**Companion chapters, checked against their own snapshots at `--min 0.9`.**
- S11: 105 sentences, 2 below. These are the first line of `dwell` and its (3) increment line, both byte-identical to the snapshot (confirmed by `diff`). The low score is an artifact: the splitter cuts inside "[thm; num: DW]" and the half tag is not stripped.
- X11: 50 sentences, 2 below. One is the rewritten opening sentence (it now introduces both tables). The other is the staying-out identity, which is byte-identical (the same tag-split artifact).

**Keys.** Every key cited in the snapshot unit is still cited in the unit.
- `verify` and `countervail` left the core file and are cited in S11 (`relaxtrust` in full) and X11 (first table, Track 5).
- S11 gains `delegate` and `detectlink`.

Outside citations still resolve:
- X10 → `relaxtrust`.
- §8, §12 → `signal`.
- §12 → `readiness`.
- S9, S11 → `reachable`.
- §3.8 → "Section 11.2".
- §4.3, §6.3, §6.6, §10.5 table, §12.1 → "Section 11.3".
- §7, §10.4, §12.1, §12.4 → "Section 11.4".
- §5 l.111, §12.2 → "Section 11.2".
- EVIDENCE EV18 → "THEORY §11.3; X11" (1983 is still in §11.3).
- EV9 and EV17 → §11.3 (both still cited there).

**Tags in the core, snapshot → final.**

| Tag | Snapshot | Final | Reason |
|---|---|---|---|
| [def] | 6 | 5 | The box's two [def] sentences are now one sentence |
| [thm] | 31 | 32 | The inline `relaxtrust` is two tagged sentences |
| [num: DW] | 3 | 1 | Two moved with the numbers to S11, which tags them [num: DW] |
| [num: TR] | 3 | 2 | `pausevalue`'s "*Proof:* S11 [num: TR]" pointer; the TR example is tagged in S11 |

[thm∣prem], [obs], [obs: EV18], [conj] and [corpus] are unchanged. No tag was dropped from the paper.

## 6. Word counts

| | draftA (src) | This edit |
|---|---|---|
| Core §11, assembler | 5,921 | **4,880** |
| Core §11, raw | 5,987 | 4,927 |
| S11, raw | 4,231 | 4,901 |
| X11, raw | 2,453 | 2,936 |
| Supplement, assembler | 47,872 | 48,531 |
| Discussion, assembler | 15,248 | 15,733 |

Largest core blocks (raw, keys as one word):

| Block | Words |
|---|---|
| Table 11.5 | 373 |
| E1 | 299 |
| Dwell | 252 |
| `signal` | 244 |
| Box | 229 |
| Carriers | 208 |
| E2 | 192 |
| Readiness table | 190 |
| Precedents | 179 |
| Counter-performativity | 173 |
| `relaxtrust` and levers | 168 |
| Readiness paragraph | 168 |
| `readiness` | 167 |
| Pause | 164 |
| Tracks table | 145 |

## 7. Open issues

1. **Inline declarations.** `relaxtrust` and `pausevalue` are now declared in core prose with their full statements in S11. This follows the pattern of `freeze`, `nonsum` and `join` (`50_s5.md`), so the numbers and keys are unchanged. If the comparator prefers their full statements in the core, restoring them from S11 is a paste back (+≈150 and +≈60).
2. **Registers.**
   - CLAIMS rows 115 and 117 ("S11; —") stay correct.
   - TESTS §6, if it points to X11, can now also point to X11's *Where things stand*.
   - CHANGELOG: tracks-table columns moved to X11; "Where things stand" moved to X11; `relaxtrust` and `pausevalue` stated in full in S11.
3. **X11 overlap, pre-existing.** The "Compensating loops beyond those in the first table" paragraph repeats the first table's Track 3 cell (reformers selected out) and Track 5 cell (mobilization falls back, `countervail`). Merging that paragraph into the table's cells would remove the repeat. I left it, since it is in the companion.
4. **The rest of merge notes U11 §4** (assembler Table kind, block TR, bibliography entries for Kydd, Cho–Kreps and Wald, symbols "Tracks 1–5") is unaffected by this pass. Podvig 2002 and Hoffman 2009 are still cited in the core.
