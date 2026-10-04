# U03 elegance pass, editor A: Section 3 (`core/30_s3.md`) and S3 (`supp/03_S3.md`)

4 October 2026. Start point: the current `src/` files, identical to `planning/snapshots/draftA/src/`. An interrupted earlier attempt in this directory (core at 5,144 words, S3 unmodified, no notes) was superseded; its sound moves are incorporated (box sentence 3 restructured; `blind`(1) in one sentence; Scope "X1 places (2) and (3)"; the duplicated "wherever reinvestment's relative return exceeds its common return" dropped from the §3.5 opening; §3.8's multiplicity figures reduced to a pointer). Its weakness was that the numbers it removed from the core had no home, since it had not touched S3; they now do.

Nothing in the mathematics changed. No key was added, removed or renamed; no S-number shifts (S3 gains no declarations), so the core numbering stays as the merge notes record it (`twoerrors` 3.10, `onegroup` 3.11, `club` 3.12, `psi` 3.13; `thrrep` S3.1, `growprize` S3.2). Every claim tag, every corpus key and every Ren line (with its Chinese original) stands as merged; the merge notes' "For Ren" items (the rendering of the ruling, the 讲赢 translation, 我们即是集, the 局部胜出 line) are untouched.

## 1. Word counts

Rendered by the assembler in the scratch build: **§3 core 5,452 → 4,914**; **S3 4,145 → 4,520**. Source `wc -w`: core 4890, S3 4529.

| Subsection | merged (snapshot) | this edit |
|---|---|---|
| 3. One system: what relative selection c | 231 | 209 |
| 3.1 Levels, measures and the host | 275 | 252 |
| 3.2 Relative selection is blind to what  | 765 | 684 |
| 3.3 Accounting: what an objective can se | 241 | 241 |
| 3.4 Interdependence and the boundary err | 673 | 589 |
| 3.5 The weight on winning, and how compo | 1027 | 889 |
| 3.6 No outside | 763 | 674 |
| 3.7 What "we are one" means | 592 | 548 |
| 3.8 The logic as held: Ψ | 815 | 758 |
| **total (assembler count)** | **5382** | **4844** |

(The table counts the source files by the assembler's method, formulas as one word, before markup is rendered; the headline figures above are the assembler's own counts of the rendered THEORY.md and SUPPLEMENT.md, which add the printed kind names and numbers.)

**Where the words are.** Of the 4,914: box 201; result statements (headline, italic statement, numbered parts) 1639; Scope and Proof lines 303; headings 68; prose 2633. The first four, 2211 words, cannot move under the rules (statements own their conditions; the box carries five tagged claims with their antecedents; no side result qualifies for the Supplement, since Parts II–IV cite `club`, `onegroup`, `twochan`, `boundary`, `load`, `blind`, `psi` and `twoerrors` and the rest are on the spine). The prose fell from 2,966 to 2633.

**The 3,700 target was not reached, and I do not think it is on the frontier for this section.** The figure is 0.68 × 5,452, the whole-core ratio applied uniformly. §3 is the paper's densest section in statements: thirteen keyed results, three of them (`blind`, `standprice`, `onegroup`) restored this round to the full conditions the reviews asked for, with `standprice` alone at about 430 words because it must define two returns and two loop gains in words before the equation. On top of the 2211-word floor, the prose carries: eight verbatim Ren lines with originals (the ruling, 讲赢/讲理, 局部胜出, 我们即是集, 大同/并育, 和实生物, 共开共续, "we are the ecology of our cells"), about 250 words; the cancer ruling and the "never applied to persons" rule; two tagged conjectures that §12.3's crux C11 and EV14 rest on; the three jobs of "we are one" (plan §4: "§3.7 is kept, tightened, in Ren's words"; plan §9 declines moving §3.7–3.8 to X1); the as-held/attributed distinction §8 and §11.2 use; and the hand-offs. To go further I would have to drop a premise, paraphrase a quoted line, or move Ren's §3.7–3.8 content out of the core, each of which the rules forbid. What I did instead is below: every illustration and worked instance went to S3, and every within-section restatement was given one home.

## 2. Moved (core → S3), with the pointer left in the core

| From | What | To (S3) | Core pointer |
|---|---|---|---|
| §3.1 | the sentence on which results transfer to harsher hosts (crossing a fortiori; viability needs a margin) | already stated, verbatim in substance, in "Hosts harsher than the forgiving one" (duplicate) | "S3 says which results transfer to harsher hosts, and which need a margin" |
| §3.4 opening | the EV13 instance (no vertical integration across the semiconductor chain; one input gas, over a hundred times its direct value) | new heading "The coupling as a material fact", before the proof of `boundary`, with [obs: EV13] | "(S3 gives an instance [obs: EV13])" |
| §3.5 opening | "A classical commons needs each actor's share of the loss to be small; selection on relative standing depletes it even among a privileged few" | after the proof of `wow`, tied to part (2) ("at every λ when n>Υ") | none needed; `wow`'s core sentence carries the conditions |
| §3.5 `standprice` Scope | the mechanism of the gross-winnings case ("the relative part of private cost is not amplified") | the SP numerics sentence that already held the figures (−0.3125 against −0.1649) | "where only gross winnings convert, the working weight is narrower still (S3) [num: SP]" |
| §3.5 `standprice` Scope | the strategic figures: "exactly 2(n−1)/n in a two-period contest with effort [thm]"; "about 1.05 to 7.9 times"; the laggard's price "below zero with a shared loss, and it stops contesting standing"; "turns the correction the other way" | "Rivals who respond", which already listed every number; the [thm] tag and the 1.05–7.9 headline range added there | the Scope keeps the conditions and signs (elasticity replaces r; fixed prize keeps (9); discouraging lead amplifies at parity and lowers a laggard's; catch-up reverses) with "S3 gives the factors" [num: MP; held for outside review] |
| §3.5 prose after `standprice` | "Inside the actor, growth whose return is common widens the self-model and decisiveness … narrows it; a part of the stakes that does not grow with capacity … adds to the relative return only" | new paragraph "Levers inside the actor", after the `growprize` numerics, citing `standprice`(2) and `growprize`(1) | the provision lever and the Test Γ sign stay in the core (Table 7.1 cites `standprice` for them); "S3 reads the other levers off the two returns [num: SP]" |
| §3.6 | the list of the five endgames and the mapping of four to results (7.2, 4.5; 3.2, 4.6, 5.3; 5.2) | new heading "The five endgames", before the proof of `club` | the core keeps the corpus key, "four are results here (S3 maps them)", and the fifth endgame in full, since the section turns on it (the lemma's transmission term) |
| §3.8 | "that competition selects organizations that behave *as if* they maximize (Alchian 1950) is part of this theory, not an objection to it" | end of "Which preferences evolve", tied to `boundary`(3) | "S3 places the 'as if' argument" |
| §3.8 | the winner-take-all price "about 9 to 12.5 times the structural value" | already in "Rivals who respond" (12.5 and 8.8 at Γ=0.2 and 0.3) and in `eqgain`(4) (duplicate; the core's range was a rounding of those two) | "({{eqgain}}; S3 gives its price)" |

## 3. Duplicates removed (the point lives elsewhere)

- §3.2 Scope, "what is added is the separation of neutrality from compliance, and the connection to captured enforcement" → X1, item 6 of what is new ("its connection to incidence, evasion and the capture of enforcement (Lemma blind(2)(3))"); the Scope now says "X1 places (2) and (3)".
- §3.2 bridge, "A common *liability* on the harmful conduct works differently again: it makes the conduct pay less, and reverses selection once it exceeds the private advantage" → the headline of `load`, three lines below ("until liability exceeds its private advantage").
- §3.2 bridge, "barriers against challengers beside accommodation of the incumbent's own practice" → `capture` (Definition 4.1) names the two directions; the bridge keeps "success has reached the selectors by a second direction ({{>capture}})".
- §3.4 `boundary`(3), the per-citation glosses ("for the finite-population evolutionarily stable intensity"; "for full dissipation in this contest") → the S3 proof of (3) attributes each step; the citations stay.
- §3.4 prose, "e(θ) depends on private cost and shared loss only through c+(1+θ)ℓ" → S3 "Measuring the weight" (first sentence); the core keeps the observable ratio 1+θ and the Test Γ pointer.
- §3.5 opening, the closing "wherever reinvestment's relative return exceeds its common return" → the headline of `standprice`, which follows.
- §3.5 `standprice` statement, "1+λ_rel=1/(1−Γ_δ) and 1+λ_com=1/(1−Γ^c_δ)" → the second equality of (9) states the same identity.
- §3.6, "not because nothing else can integrate at this scale, but because against failures that cannot be undone nothing else acts in time" → merged into the bold clause "where the failure to be avoided is global and irreversible, only it acts in time".
- §3.6 endgames, "and the purpose of this paper" → §3.7 "which is why this paper is written" (one home for the paper's purpose; §3.6 keeps "the lemma's transmission term").
- §3.7(3), the four properties of a system that "knows it is one" in non-canonical wording → cited as G1 and G3 of §8.2 in their canonical wording, plus coverage (Section 9). This applies plan §4 (§8): "Every other list cites them or uses identical wording and order", and closes merge-notes open issue 6.
- §3.7, "which each actor computes correctly and no argument changes" → `twoerrors` ("the correct first-order computation of its interest"); the clause "which no argument changes" is kept, since it is the distinct point.
- §3.8 triple, Ψ3's list "sharing, convertibility, decisiveness, provision and diffusion" → the statement of `compound`, which is cited in its place.

## 4. Preservation check (sentcheck, snapshot core vs new core + new S3 + the other current src files, --min 0.5)

176 sentences checked; 6 below 0.5, each adjudicated:
1. "Results that a trajectory *crosses* the floor therefore hold a fortiori … need a margin (S3)." — duplicate of S3 "Hosts harsher than the forgiving one"; pointer kept (§2 above).
2. "Part (1) is the known translation invariance … what is added is the separation of neutrality from compliance, and the connection to captured enforcement." — first clause kept; second clause duplicate of X1 item 6 (§3 above).
3. "That is the second direction in which success reaches the selectors, barriers against challengers beside accommodation …" — merged into the bridge sentence; the two directions are `capture`'s (§3 above).
4. "A common *liability* on the harmful conduct works differently again …" — duplicate of `load`'s headline (§3 above).
5. "Hehenkamp, Leininger and Possajennikov 2004 for full dissipation in this contest)." — citation kept; gloss duplicate of the S3 proof (§3 above).
6. "Section 8.2 states them as the marks of a generative order, and Section 10 gives them forms." — merged into §3.7(3)'s closing sentence ("(G1 and G3 of Section 8.2) … Section 10 gives them forms").

S3: 122 sentences of the snapshot checked against the new files; 0 below 0.5 (S3's existing text was not rewritten, only added to).

## 5. Other changes

- Box: 224 → 201 words, by phrasing only; all five claims, their antecedents and tags stand. It is above the 90–140 guide because the section has five spine results and sentence 3 must carry both prize cases with their conditions.
- §3.1: the illustrative clause on different interests shortened ("a citizen's continued agency is none of them").
- Verified in the scratch build: `{{>capture}}` renders "Definition 4.1"; `{{eqgain}}` "Remark S2.x"; `{{growprize}}` "Proposition S3.2"; no unknown keys, forward uses, doubled kinds or banned phrases; "no problems".

## 6. Open issues for the integration editor

1. `supp/07_S7.md` line 24 cites "({{eqgain}}(3); Section 3.5)" for "about 1.05 to 7.9 times". The range now lives in S3 ("Rivals who respond") and `eqgain`; "Section 3.5" there should read "S3" (U07).
2. EVIDENCE: EV13's core use moved to S3; the core keeps "[obs: EV13]" with the pointer. The register's "used in" entry should name S3 (registers phase).
3. CLAIMS line 18 still reads "Ψ … locally rational, systemically false, partly made true"; the merged core has the plan's triple. Registers phase.
4. If §8.2's G-marks are renumbered, §3.7(3)'s "G1 and G3" must follow.
5. Length: 4,914 against the 3,700 guide, for the reasons in §1. If a shorter §3 is wanted, the remaining candidates are all content decisions for Ren, not edits: the five-endgame sentence (already a pointer), the two [conj] paragraphs of §3.4 (C11 depends on them), and the relational-self paragraph of §3.7 (the only core home of four corpus lines).
