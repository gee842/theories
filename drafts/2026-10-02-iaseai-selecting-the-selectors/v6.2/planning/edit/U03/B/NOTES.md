# U03 elegance pass, editor B: Section 3 (`core/30_s3.md`) and S3 (`supp/03_S3.md`)

4 October 2026. Started from the current `src/` files, which match the snapshot `planning/snapshots/draftA/src/`. This directory held a partial core file from an interrupted earlier attempt: a light trim to 5,026 words, with nothing moved and no S3. I checked it and replaced it, keeping its sound trims.

## 1. What changed, in one paragraph

Every key, declaration, result statement, condition, claim tag, equation and Ren line stays in the core. No mathematics changed (a formula-by-formula check: nothing in the new core is absent from the old one, and the three inline formulas that left the core, $\Gamma_\delta\to1^-$, $2(n-1)/n$ and $r$, now sit in S3). The core lost:
- Scope numbers, moved to S3;
- lineage that X1 already holds;
- a few illustrative clauses, moved to S3;
- sentences that only restated a statement or a later remark.

Most of the reduction comes from tightening sentences. The section's order, subsections and hand-offs are unchanged.

## 2. Moves (core → S3)

| What moved | From | To |
|---|---|---|
| What makes the host "forgiving" (regenerates fastest per unit when most depleted; no threshold of its own) | §3.1, last paragraph | S3 "Hosts harsher than the forgiving one", first sentence; "harsher" is now named there as the condition already stated ("regeneration per unit no greater than $\rho(1-V)$ at every level"). The core keeps the condition itself, "hosts that regenerate less at every level", and points to S3. |
| "What carriers value decides which strategies they try, not which ones grow: evolutionary suicide … (Rankin, Bargum and Kokko 2007)" | §3.2, after `load` | S3, after the proof of `load` (lineage). |
| "A classical commons needs each actor's share of the loss to be small" | §3.5, `wow` paragraph | S3, opening of "Full statement and proof of Proposition `wow`". The core keeps "even among a privileged few". |
| "Where only gross winnings convert, the relative part of private cost is not amplified and the working weight is narrower still [num: SP]" | `standprice` Scope | S3, "Numerics for `standprice`": the mechanism now stands beside the figures (−0.3125 against −0.1649). The core Scope keeps "net payoff reinvested, which is load-bearing (S3)". |
| "So 'where the loop gain is high' reads as the limit $\Gamma_\delta\to1^-$" | `standprice` Scope | S3 *Bounds* (with the $\Gamma_\delta\ge1$ clause). The core Scope keeps "At $\Gamma_\delta\ge1$ no finite weight represents the actor". |
| Rivals who respond: "by exactly $2(n-1)/n$ in a two-period contest with effort [thm] and by about 1.05 to 7.9 times in the two-actor Markov-perfect contests computed, while a laggard's price falls, below zero with a shared loss, and it stops contesting standing"; Harris and Vickers 1987; Konrad and Kovenock 2009 | `standprice` Scope | S3 "Rivals who respond", merged with the figure list already there into one paragraph. Each figure now carries its pointer to `eqgain` parts (2)–(5). The core Scope keeps three things: the elasticity of `loopgain`(4); "with a fixed prize (eq) keeps its form"; and one clause each for amplification and the catch-up reversal, [num: MP; held for outside review]. The phrase "about 1.05 to 7.9", which the MP s2b printout quotes, survives in S3 and in S7. |
| The mapping of four endgames to results (freeze → Section 7.2; deadlock → Section 4.5; collapse → Sections 3.2, 4.6, 5.3; winner takes all → Section 5.2) | §3.6, endgames paragraph | New S3 subsection "The five endgames", keyed [corpus: selfishness-spiral]. The core keeps "five endgames" (an xref must-stay phrase), names the fifth (the change of narrative), and says it is the transmission term and the paper's purpose; "the other four are results here (S3)". |

## 3. Duplicates removed (only true duplicates; where each point lives)

| Removed | Lives at |
|---|---|
| `blind` Scope: "Part (1) is the known translation invariance of relative dynamics (Weibull 1995); what is added is the separation of neutrality from compliance, and the connection to captured enforcement." | X1 "What is absorbed, and what is new": "the translation invariance of relative selection (Weibull 1995), which is Lemma `blind`(1)"; and item 6, "not the invisibility itself, which is absorbed, but its connection to incidence, evasion and the capture of enforcement (Lemma `blind`(2)(3))". |
| `blind` Scope: "a type whose evasion pays still loses its evaders when another type's compliers earn more" | S3 proof of `blind`, *Not necessary across types*. The core keeps "sufficient, not necessary (S3)". |
| "That is the second direction in which success reaches the selectors, barriers against challengers beside accommodation of the incumbent's own practice" | §4.1, Definition `capture` ("Capture runs in two directions: toward accommodation … toward barriers …") and the paragraph after it. The core keeps the barrier mechanism ("costs challengers more while binding everyone in name: newcomers adopt it or are out") and the pointer `{{>capture}}`. |
| "A constraint that costs challengers more than incumbents picks winners among the compliant (part 2)" | `blind`(2) ("re-sorts the compliers toward those it costs least"). It is merged into the barrier sentence ("when it costs challengers more"). |
| Liability "reverses selection once it exceeds the private advantage" | `load` headline ("until liability exceeds its private advantage") and S3 CI numerics (τ = 1.5 > ν = 1). The core keeps "A common liability works on the conduct instead, making it pay less". |
| `twochan` proof pointer: "and why identification fails exactly where shared harm goes unseen" | S3 "Measuring the weight", last sentence; §7.4 Test Γ also points to S3 for the confound. |
| Powell paragraph: "what decides is how far gains convert into advantage relative to how far they enlarge what all share" | `standprice` headline and statement (relative against common return). |
| Powell paragraph: "Selection on conduct favours the relative objective (`boundary`(3)); compounding prices standing in whoever looks ahead" | §3.8 *Individually rational* ("selection favours that conduct … (`boundary`(3), `load`)") and the `standprice` headline. The V6.1 point ("compounding manufactures it in whoever looks ahead") stays findable in the proposition itself. |
| §3.6: "not because nothing else can integrate at this scale, but because against failures that cannot be undone nothing else acts in time" (second half) | The bold sentence before it ("Where the failure to be avoided is global and irreversible, only the second acts in time"). The first half is kept ("That, and not that nothing else can integrate at this scale, is the formal content …"). The premise is not compressed away. |
| §3.7: "The two errors of `twoerrors` divide the work: 'we are one' understood corrects the held boundary, and only 'we are one' built into what selection rewards corrects the working objective, which each actor computes correctly and no argument changes." | `twoerrors`, last sentence ("Understanding acts on the first error directly, and on the second only through agreement to change what winning confers"), and §12.2, the theory of change ("The two places answer the two errors of `twoerrors` …"). "Each actor computes correctly" is in `twoerrors` and the box. |
| §3.8: "Held as self-model and doctrine, the logic has three parts." | Definition `psi`, first sentence ("the configuration of self-model and doctrine") and its three parts. |
| §3.8 *Collectively self-defeating*: "however much any carrier values it" | `load` statement ("however much any carrier values it"). |
| §3.8 Ψ3: "of a game that can be changed" | Definition `psi`, last sentence ("rather than parameters of a game that can be changed"). |
| §3.8 "Partly made true": "whose price of standing is about 9 to 12.5 times the structural value" | S3 "Rivals who respond" (about 12.5 and 8.8 times for Γ = 0.2 and 0.3) and S2 `eqgain`(4). This takes the merge notes' item 8: §3.8 keeps the pointer `{{eqgain}}`, [num: MP; held for outside review] and the belief reading [conj]. |
| §3.4 positional paragraph: "by holding decisive capability in common or not building it" | §10.2 ("It can only be kept from forming, by not building capability of the decisive class … or held in common custody … Section 3.4 located the crux of design here"). The core keeps "That locates the crux of design", which §10.2 points back to. |

## 4. Merged or reworded (meaning kept)

- §3.1: "Persons, firms … different interests: a citizen's …" and "Two levels are kept apart" are now one sentence (the illustration in parentheses). "It is not a preference everyone must adopt, and not a weight θ" is folded into the first sentence of §3.7. The xref must-stay phrase "not a weight $\theta$" is kept.
- §3.2 prose: "is also what protects a common rule: a constraint that … turns the pathology into a protection" is now "also protects a common rule that … : the pathology turned into a protection". "The two conditions do different work" is folded into "The sanction keeps the rule; equal incidence keeps it from becoming a weapon".
- `blind`(2): "equal incidence makes a constraint neutral among those who comply, and does nothing more" is now "it leaves their relative growth unchanged, and does nothing more". The neutrality clause is the lemma's headline. D1-opus §2.6's point, "does nothing more", is kept.
- §3.4: "Part (2) is the sense in which …" is now "Part (2) makes …". "Toward what can be divided" is kept, because the error is only toward the divisible part.
- `standprice` Scope: "Diffusion separates the two conditions of (2): the self-model narrows before equal standing is lost, in a band that `growprize` gives in closed form" is now "… opening a band in which the self-model narrows while equal standing is stable (`growprize`)". Same content and tags.
- Powell paragraph: "Patience cuts both ways: it strengthens repetition and raises the price of standing" is kept as a clause ("patience cuts both ways, strengthening repetition and raising the price of standing"). "Inside the actor, growth whose return is common widens …" is kept with the same three levers.
- §3.6: "Understanding acts in the lemma's own terms, as the transmission through which …" is now "Understanding is the lemma's transmission term, by which …". The endgames paragraph is folded into the same paragraph (§2 above).
- §3.8: "Ψ1 draws a boundary"; "all who act on it end worse off"; "that would itself be the attribution". Small rewordings only.

## 5. Minimal correction (recorded)

- **Box, price sentence.** The merged box read "with a fixed prize always". At $\Gamma_\delta=0$, for example with nothing convertible, the relative and common returns are both zero and the working self-model does not narrow (merge notes §2, item 3, corrected the same point in `standprice`(1)). The box now reads "with a fixed prize whenever the discounted loop gain is positive", matching `standprice`(1) and the Standing row of Table 7.1 ("with a fixed prize wherever $\Gamma_\delta>0$").

## 6. Preservation check (adjudication)

The check was run as `python3 src/sentcheck.py <snapshot>/src/core/30_s3.md src/core/30_s3.md src/supp/03_S3.md <all other current core/supp/disc files> --min 0.5`, in a scratch copy with my two files in `src/`. Result: 176 sentences checked; 8 below 0.5.

| Containment | Sentence (start) | Adjudication |
|---|---|---|
| 0.27 | "Part (1) is the known translation invariance … (Weibull 1995) …" | Duplicate of X1 (§3 above). |
| 0.21 | "That is the second direction in which success reaches the selectors …" | Duplicate of §4.1 `capture` (§3 above). The pointer is kept. |
| 0.22 | "A common *liability* on the harmful conduct works differently again …" | Merged: "A common *liability* works on the conduct instead, making it pay less". The reversal clause duplicates the `load` headline. |
| 0.44 | "… and why identification fails exactly where shared harm goes unseen." | Duplicate of S3 "Measuring the weight". |
| 0.48 | "Diffusion separates the two conditions of (2) …" | Reworded and kept in the core Scope (§4 above). |
| 0.45 | "Patience cuts both ways …" | Kept as a clause in the Powell paragraph. |
| 0.40 | "The two errors of `twoerrors` divide the work …" | Duplicate of the last sentence of `twoerrors` and of §12.2 (§3 above). |
| 0.12 | "Held as self-model and doctrine, the logic has three parts." | Duplicate of Definition `psi` (§3 above). |

S3 old against new (same pool): 122 sentences checked, 0 below 0.5. I rewrote existing S3 text only in "Rivals who respond", "Bounds" and the "gross winnings" sentence, all as additions or merges.

## 7. Verification

1. **Test assembly** (scratch copy, my files in `src/`). `python3 src/assemble_v62.py` reports "no problems", with 95 core and 33 supplement declarations, unchanged.
2. **xref** (`python3 xref_v62.py` in the scratch copy).
   - Must-stay phrases: 32/32 present ("five endgames", "plurality of decorrelated units", "not a weight $\theta$", 我们即是集, 和实生物，同则不继, 共开、共续、不夺共续, 讲理, 局部胜出的策略拿走了理性的名字, molochlization, "individual–collective axis").
   - No named states or firms.
   - Citation coverage is clean in all three documents once `src/refs_v62.py` regenerates the generated reference lists (see open issue 1).
   - The two guide-item failures (items 1 and 9) are pre-existing: they appear identically in an unmodified copy.
3. **Word counts** (assembler, rendered; S3 counted on the assembled SUPPLEMENT).

| | Before (merged) | After |
|---|---|---|
| Core §3 | 5,452 | **4,878** |
| S3 | 4,109 | 4,412 |
| Supplement total | 46,029 | 46,332 |

By subsection (my count, same rule as the assembler's):

| Subsection | Before | After |
|---|---|---|
| Box | 231 | 217 |
| 3.1 | 275 | 255 |
| 3.2 | 767 | 635 |
| 3.3 | 241 | 233 |
| 3.4 | 673 | 640 |
| 3.5 | 1,054 | 865 |
| 3.6 | 763 | 686 |
| 3.7 | 598 | 544 |
| 3.8 | 839 | 792 |

**Why about 4,880 and not 3,700.** The figure 3,700 looks like the paper-wide scaling (59.5k → about 40k) applied to §3. §3 grew less than the paper in the merge (×1.5 against ×1.95). Its growth over V6.1 (3,577 by this count) is mostly content the plan requires:
- `standprice` in general form with both returns, its Scope and `twoerrors`: §3.5 is 865 words against V6.1's 355;
- the `blind` repair (incidence; falling sanction with continuity and strict decrease);
- the divisible/positional split ($\kappa_s$) in the set-up and `boundary`;
- the ruling that opens §3.8, the full 讲赢 line, and the Ψ status triple with Henrich scoped to persons and Alchian for firms and states.

What the remaining words carry:
- **Box, headings, definitions, model set-ups, full statements and Scopes, about 2,780 words.** That is the full statements of `blind`, `load`, `twochan`, `boundary`, `standprice`, `twoerrors`, `onegroup`, `club` and Definition `psi`, each cited by Sections 4–12, so none can move under plan §2; the in-prose statements of `wow` (cited by §§7, 9) and `unequal`; and the set-ups that §§4, 5 and 10 use (the host, the contest of Section 3.4).
- **Paragraphs carrying Ren's lines with the mechanisms they compress, about 1,230.** These are molochlization; the polycentric hedge and "we are one" as a requirement; 共开、共续、不夺共续; the relational self and 大同; the ruling; 讲赢; 局部胜出. Plan §4 keeps §3.7 "in Ren's words", and plan §9 declined moving §3.7–3.8.
- **Free prose, about 850.** This is the hand-off, the blind→capture link, the observable for Test Γ, the positional crux, the Powell reading with the standing levers, the attribution paragraph, and "partly made true".

Reaching 3,700 would take more than half of the last two groups, which would mean moving §3.6–§3.8 out of the core. The box is about 215 words against a guide of 90–140: it carries five claims (blindness, held error, price of standing with both prize cases, the game is wrong, no outside), each with its antecedents. That is comparable to the boxes of §2 and §4.

## 8. Open issues

1. **Reference lists must be regenerated** (`cd src && python3 refs_v62.py`, then assemble). With my files:
   - THEORY no longer cites Weibull 1995 (X1 still does) or Rankin, Bargum and Kokko 2007;
   - SUPPLEMENT now cites Rankin, Bargum and Kokko 2007.

   Regeneration drops both from `core/z9_refs.md` and adds Rankin to `supp/z9_refs.md`. After it, xref citation coverage is clean (tested). Without it, xref reports two UNCITED entries in THEORY and one MISSING in SUPPLEMENT. I did not edit the generated `z9_refs.md` files, since they are outside this unit.
2. **S7 "Near parity"** (`supp/07_S7.md`, l. 24) cites "(`eqgain`(3); Section 3.5)" for "about 1.05 to 7.9 times". The range now sits in S3 "Rivals who respond", and §3.5 keeps only the qualitative clause. The pointer could read "S3" (U07's file).
3. **Tag of the two-period factor.** "By exactly $2(n-1)/n$ in a two-period contest with effort [thm]" is carried verbatim from the merged core Scope into S3. S2 `eqgain`(2) tags the static Tullock factor [thm; num: MP] and the two-period game "gives the same factor [num: MP]". The integration editor should confirm which tag the two-period statement earns.
4. **§3.7(3) against G1–G3** (merge notes §4, item 6). The list is kept as merged (four properties, own wording). Plan §4 (§8) asks that every other list of the marks "cites them or uses identical wording and order". If the integration editor aligns it, the natural form is G1, G2 ("winning confers reward, not more advantage in the same game"), G3, plus coverage of every capable actor.
5. **Multiplicity, now in three places with distinct jobs:**
   - §2 `loopgain` Scope (existence);
   - S2 `eqgain`(4) (numbers, review items);
   - S3 "Rivals who respond" (figures for §3.5's Scope).

   §3.8 carries only the pointer and the [conj] belief reading.
6. Unchanged from the merge notes and still open for the integration editor: CLAIMS marks D for the English renderings of the ruling, of 一旦争…斗则讲赢 and of 我们即是集; the symbol-table additions; the numbering shift (`twoerrors` Remark 3.10, `onegroup` Lemma 3.11, `club` Proposition 3.12, `psi` Definition 3.13; `thrrep` S3.1, `growprize` S3.2: unchanged by this pass); the `thrrep` cutoffs without a check block.
