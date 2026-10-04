# V6.2 final build notes (2026-10-04)

## 1. Build

The build ran from `v6.2/` in this order: `python3 src/assemble_v62.py`; `(cd src && python3 refs_v62.py)`; `python3 src/assemble_v62.py`; `python3 xref_v62.py`; `python3 checks_v62.py > checks_v62.log`.

- **assemble:** no problems. There are 93 core declarations and 35 supplement declarations.
- **refs:** THEORY has 103 entries, SUPPLEMENT 89 and DISCUSSION 132. No problems.
- **xref:** ALL CHECKS PASS.
  - Citation coverage holds in both directions. THEORY cites 103 works and lists 103; SUPPLEMENT cites and lists 89; DISCUSSION cites and lists 132.
  - All 32 must-stay items are present.
  - The Chinese guide and Section 1.2 match at 9/9 items, each above the 60% threshold. The two lowest are item 1 at 82% and item 9 at 67%.
  - No state or firm is named in the core's prose.
- **checks:** exit code 0, run time 327 s.
  - **188 assertions passed, 0 failed** (default sizes).
  - All eight of Codex's starred boundary cases appear in a block and hold.
  - Against the previous full log (12:57), nothing changed apart from timing lines and the blocks added since. Those additions are CI (k), `unravel` across types (Remark S9.1), and SM (15)–(16), which cover Proposition S6.2(2) homeostasis roots and Remark S3.1 `thrrep`.
- **Mechanical failures:** none. **No edits were made to src/.**

Two items are for information and are not failures:
- EVIDENCE cites works that no reference list carries: Bowles and Polanía-Reyes 2012; Dietz, Ostrom and Stern 2003; Farrell and Newman 2019; Friedman 1953; and the REAIM/Seoul/Hague event citations.
- TESTS cites Kenton et al. 2024, Khan et al. 2024 and Zhu 2026, which no reference list carries either.

## 2. Words (the assembler's count; a formula counts as one word; references excluded)

| Core section | Words |
|---|---|
| front | 551 |
| 0 | 495 |
| 1 | 2,936 |
| 2 | 3,622 |
| 3 | 4,962 |
| 4 | 4,047 |
| 5 | 4,993 |
| 6 | 5,643 |
| 7 | 5,193 |
| 8 | 4,723 |
| 9 | 2,583 |
| 10 | 5,959 |
| 11 | 4,788 |
| 12 | 4,917 |
| symbols | 785 |
| **core total** | **56,197** |

- Parts III and IV come to 22,970 words, 41% of the core.
- The Chinese guide (导读) is 2,645 字.

**Supplement: 58,890 words.** By chapter (split on chapter headings, so the sum differs from the total by heading words):

| Chapter | Words |
|---|---|
| head | 129 |
| S0 | 2,565 |
| S2 | 5,033 |
| S3 | 4,472 |
| S4 | 5,089 |
| S5 | 6,463 |
| S6 | 4,543 |
| S7 | 5,244 |
| S8 | 3,334 |
| S9 | 4,857 |
| S10 | 3,031 |
| S11 | 4,438 |
| S13 | 2,595 |
| S14 | 4,522 |
| S15 | 2,561 |

**Discussion: 20,573 words.**

| Chapter | Words |
|---|---|
| head | 78 |
| X1 | 6,522 |
| X2 | 486 |
| X8 | 6,650 |
| X10 | 3,915 |
| X11 | 2,917 |

## 3. Results

**Core: 93 declarations.**
- Formal results: 41 Propositions, 3 Theorems, 6 Lemmas and 3 Corollaries, **53 in all**.
- Other declarations: 10 Definitions, 1 Assumption, 11 Remarks, 3 Tables and 15 numbered equations.

**Supplement: 35 S-numbered declarations.**
- Formal results: 13 Propositions, 1 Lemma and 1 Corollary, **15 in all**.
- Other declarations: 18 Remarks, 1 Table and 1 equation.

**Together: 68 formal results.**

## 4. Sentence preservation

**Against V6.1** (`sentcheck.py ../v6.1/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4`): 1,060 sentences checked, **101 below 0.4**.
- At the end of the elegance pass the figure was 81, and those 81 were adjudicated in `elegance-build-notes.md` §3. None of them has been resolved since.
- The 20 new flags all come from the front-matter pass (`front-notes.md`) and the coherence pass (`coherence-notes.md`).

**Against draftA** (`sentcheck.py planning/snapshots/draftA/THEORY.md … --min 0.5`): 1,889 sentences checked, **101 below 0.5**.
- At the end of the elegance pass the figure was 80. Since then 25 flags are new and 6 are resolved.
- The new flags are the 20 above, plus five draftA sentences in Sections 0–1, 6 and the symbols note.

I adjudicated every new flag against the assembled text.

**Rewritten in place (front pass)**
- *Section 0, meaning paragraph.* "the part that forgets it belongs to a whole", "a larger process of becoming", "keep the future open" and "the meaning is affirmative" are now one paragraph at THEORY l.47 ("an objective with no point of enough, held by a part that counts only itself … a future kept open to every participant"). The full version, with Ren's quotation, is at l.1227.
- *The game, not the act.* "A single use of AI can help one person …" now reads "The game, not the act" at l.45 and §6.6.
- *Review status, reading paths, What is new, substrate.*
  - "one model family" is kept at l.92.
  - The 怎样读 line was rewritten. The tokenizer reads Chinese as 0.00, so this flag is an artefact.
  - The English reading paths are now the *How to read* box (l.94) and the README's formal path (S0, S2–S6, S13, S14, S15).
  - "What is new" was rewritten at l.90.
  - "None of this is bound to a substrate" now survives as the heading of §2.4.
- *§1.2 items.* The items were rewritten to close open issue 1 of `elegance-build-notes.md` §6:
  - "manufactures" (a banned word) is gone;
  - "prices standing for every actor" is now restricted by its conditions;
  - item 5 is now "Weakly, the logic of winning re…", which covers "Weakly, the outermost loop decides …";
  - "Correction falls behind the tempo" is carried by §5.3 and item 4.
  - "Where success can also buy the selectors …" is now the abstract's "buy control over the selection".

**Corrected (substantive, and deliberate)**
- *V6.1's §4.6 sentence "The same recursion can be generative: success that funds correctors it cannot control is selected in the same way …"* V6.1 contradicted Proposition 4.4 here. draftA corrected it ("not by the same selection … not selected among carriers"), and coherence edit 15 deleted the paragraph. Its points now live in Remark 2.5 and §10.4 (l.1011–1013): the loop runs through the whole and not through its winners, and whether it attracts is [conj].
- *Proposition 5.16 (Talk under relative accounting).* "Among three or more, rivals fall silent and allies form blocs" is now the proved multiplier $n/(n-2)$, which falls toward one. The bloc reading is demoted to [conj] at l.482. This closes U05's "forms blocs" issue.
- *Symbols note.* "Each symbol … has one meaning throughout" is now restricted to the table's own symbols, with the exceptions listed in S0 (l.1231). This closes open issue 2.

**Reworded or renamed (coherence pass)**
- "For classes with an irreducible lag only slowing helps" → l.512: "a is the only lever left … and slowing is what lowers it."
- "It does not decide global behaviour …" → §2.2 *What the loop gain does not decide* (l.157). That paragraph now names the speed (Perron root), decisiveness beyond sanction and capability outrunning correction.
- "Sufficient safeguards … Four safeguards are sufficient and not necessary" → "Sufficient routes, and form. Four routes are sufficient …" (l.922).
- "The premise that a rival might win decisively describes the case in which repetition stops enforcing restraint" → Branch I of Proposition 7.2 (l.720), and l.743.

**Verdict.** No point was lost, and nothing needs restoring. The three substantive changes listed under *Corrected* are deliberate corrections, each with its source named above.

## 5. Not touched

No prose was changed, so the open questions for Ren in `elegance-build-notes.md` §6 (items 6–9) still stand, except where the front and coherence passes closed them (items 1–2 above).
