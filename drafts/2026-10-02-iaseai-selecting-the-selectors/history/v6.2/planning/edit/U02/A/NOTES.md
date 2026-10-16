# U02 elegance pass, editor A: §2 (core/20_s2.md) and S2 (supp/02_S2.md)

4 October 2026. Inputs: current `src/core/20_s2.md` and `src/supp/02_S2.md` (both byte-identical to `planning/snapshots/draftA/src/`), V6.2-PLAN, merge notes U02, D1-opus §3.3 (box and section spec), and the neighbouring text that §2 hands off to or is cited from: §0, §1.2, §3.1–3.8, §4 (end), §7.1 (Table 7.1, four loops, formal correspondence), §7.4 (Test Γ), X1, X2.

**Earlier attempt.** This directory already held a core draft from an interrupted attempt (no S2, no notes). I did not build on it blindly. I redid the pass from the current `src/` files and reused a few of its compressions where they checked out. The files here replace it.

## 1. Word counts (assembler rule: a formula counts as one word)

| | Before (draftA) | After | Change |
|---|---|---|---|
| Core §2 (from "## 2.", assembler) | 4,007 | **3,503** | −504 (−12.6%) |
| Claim box (without tags) | 185 | 150 | −35 |
| Part I lead (counted under §1) | 36 | 36 | 0 |
| S2 (rendered, assembler rule) | 4,879 | 5,039 | +160 |
| Core total | 59,516 | 59,012 | −504 |

**Against the target of about 2,700.** The core is about 800 words over. I would rather name what those words carry than cut a condition. The fixed part of §2 is its statements:
- `cond`: 162 words;
- `loopgain`, Model and parts (1)–(4): 479;
- `compound` (1)–(2): 243;
- `meta` with its gloss: 185;
- `pathgen`: 161.

These total about 1,230 words. By the rule that statements own their conditions, none of it can be shortened.

The rest carries four kinds of content:
1. **Scopes the reviews asked for**, about 250 words:
   - the rank-one and reinforcing-channel conditions;
   - (4) as a benchmark in both directions, with the outside-review labels;
   - the proportional-prize condition that §3's `standprice`(2) relies on;
   - the leaders-held premise of (2).
2. **The core home of `chansign`'s mechanism**, about 130 words. §7.1 points to it ("there the levers are correction … (Section 2.2)"). It holds the plan's line "Trees for capacity, correction for rule support, sharing and openness for all", and "blocking diffusion raises the gain".
3. **The Λ\* sentence and the limits paragraph.** §7.4's Test Γ cites "Γ is not estimated (Section 2.2)".
4. **Six verbatim lines from Ren**, with their clause mapping and the analytic step: about 250 words in all.

V6.1's §2 was 2,640 words without (4), without `chansign` and with weaker statements. Its prose (§2.1, the three paragraphs of §2.3, §2.4) is kept here but tightened. Each further cut I tried would have:
- dropped a premise;
- moved a worked instance into the Supplement, which is the wrong genre (instances belong in X2, which is not this unit's chapter);
- or removed a Ren line.

Three further cuts are possible if a shorter §2 is wanted. Together they save about 150 words:
- the research-community example, sent to X2's Science bullet (by the X2 owner);
- "*Why 'meta-attractor'*", sent to X1;
- §2.4's instance list cut to a list of names, with the mechanisms left in X2.

## 2. What moved from the core, and where

Every sentence below left the core. Its content sits in S2 beside the result it serves. Where the point was already in S2, I name the duplicate in §3 below instead.

| Core text (draftA) | Now in |
|---|---|
| loopgain Scope: "The stability calculation is standard (X1 gives the lineage); what is new is the organization, with provision and diffusion inside the gain, and its consequence for objectives (Section 3.5)." | S2, new *Lineage.* paragraph after the proof of (4), before *Numerics* (verbatim) |
| loopgain Scope: "$r^{\rm eq}/r$ is 1.09 at a structural gain of 0.2 and 1.18 at 0.3, and about 2.5 to 5.4 at structural gains from 0.45 to 0.9, where $\Gamma^{\rm eq}$ exceeds one and equal standing breaks although $\Gamma<1$" | S2 `eqgain`(3), new closing sentence "Across the cases computed, then, …" (verbatim, [num: MP]) |
| loopgain Scope: "Where catch-up is so strong that a carrier's equilibrium win share falls with one of its own stocks, the premise of (4) fails and $\Gamma^{\rm eq}$ alone does not decide." | S2 `eqgain`(5) catch-up (verbatim, with a pointer to the proof of (4), which already says it) |
| loopgain Scope: "already at a structural gain of 0.2" | S2 `eqgain`(4) (already there: "At $\Gamma=0.2$, $d=0.05$ …") |
| compound Scope: growing capacity under a fixed prize, "holds date by date with the current total" | S2 *Growth variants* (a) (already there). The core now says "S2 … lets capacity grow under a fixed prize" |
| compound Scope: "the condition does not drift" | S2 *Growth variants* (b): "a condition constant in time" (already there) |
| compound Scope: "their own losses to diffusion enter", "in the ten cases computed" | S2 proof of `compound`, *Leaders held*, and *Numerics (CE)*, "Ten cases …" (already there) |
| After compound: "Diffusion … draws a laggard toward the mean, since what one carrier learns others can learn" | S2 *Numerics (CE)*, *Diffusion as a source*, new first sentence (verbatim) |
| Levers: "Making winnings decay faster pushes the wrong lever; changing what winning converts into pushes the right one." | S2 `chansign`, consequences paragraph, second sentence (verbatim) |
| Levers: faster decay of capacity "leaves that channel's gain unchanged without diffusion, raises it with diffusion, and always raises the discounted gain … a stock that turns over faster is made more of recent winnings" | S2 `chansign`(2) statement, and the consequences paragraph (already there, verbatim). The core keeps "never does [lower the gain]" with the reason |
| Limits: "so the same gain on a slowly turning stock opens leads slowly" | S2 `tdec`, first bullet, appended to the 0.02-turnover number (verbatim) |
| Limits: "which the loop reaches only through the time a gap needs to become decisive" | S2 `tdec`: "This is the channel through which a larger loop gain raises the breakout probability $p_d$ of Section 5.2" (already there). §5 `scissors`(1) says it again |
| Bench: "of the same form as {{loopgain}} but not a case of it, and each of its coefficients names a channel that can be measured" | S2 Remark S2.6 `bench` (already there, verbatim), and the S2 table row |

## 3. Duplicates removed (the point lives elsewhere)

1. **Box, B's rivals sentence:**
   > "Where rivals respond, the same form holds with an equilibrium decisiveness [thm], and in the contests computed where a lead discourages the follower, leads compound below a structural gain of one [num]."
   - The same claim stands in `loopgain`(4) [thm], in its Scope [num: MP] and in Table 7.1's Compounding row.
   - The plan sets the box "as D1-opus, with the corrected lever sentence", and D1-opus's box has no rivals sentence.
   - The Claim keeps the antecedent "with the prize and the actors' conduct fixed", so it stays true.
   - See open issue 1.
2. **"They combine in one quantity."** This only restated the next sentence. The `loopgain` headline says it: "The conditions multiply into a single structural loop gain".
3. **"no particular culture"** (from the closure paragraph). §2.4's "Nothing in {{cond}} refers to a culture, a political system or a species" says it.
4. **§2.3 ¶1's list** "the rules, the evaluators and correctors, the formation of the minds that will hold positions, and the language in which success is described". The list's home is the closure paragraph after `cond`. §2.3 ¶1 now says "because what can be won includes control over the selection itself".
5. **"Structural explanation … does not erase responsibility, which differs with knowledge, discretion and power."** This is §0, *The game, not the act*: "Responsibility differs with knowledge, discretion and power, and structural explanation does not erase it". D1-opus's §0 draft keeps that sentence. The half specific to §2.3 is kept: "why intentions alone cannot account for recurrence".
6. **"*Why 'meta-attractor'*", last sentence:**
   > "One concept covers the mechanism and its generative dual, and every claim says which of the three senses it uses."
   - "Each claim in this paper says which it concerns" is in Definition `meta`.
   - "a generative counterpart" is in the same paragraph.
7. **`pathgen`:**
   > "since correction keyed to no one is selected against among otherwise identical carriers"
   - The home is §4's last paragraph: "Correction keyed to no one is not selected among carriers ({{noinside}})". `noinside` itself also says it.
   - The core keeps the {{>noinside}} pointer.
   - The trailing "(Section 10)" was also dropped: Section 10.4 is cited one sentence earlier.
8. **"What the loop gain does not decide", last sentence:**
   > "linked by a few shared parameters and by one shared state, the concentration of standing"
   - The home is §7.1: "a few parameters on which several thresholds turn". The formal correspondence adds "reinforcing channels on one state, the concentration of standing".
   - §2 keeps "not one quantity but a set of interconnected conditions with one structural loop gain at its core ({{>thresholds}})".
9. **§2.4 instances.** The cells clause "recruits surrounding tissue" and the federation sentence. X2's Cells and Federations bullets carry both, with the same citations. §10 has federations at length.
10. **§2.4, "reproducible units that gain or lose share"** (after "Trained AI systems are themselves carriers"). This is the definition of carriers in `cond`.
11. **§2.4, the another-planet clause** "wherever selection is relative, winnings convert and the successful can edit the selection". It is now "wherever the three conditions hold", which is the same for "the same pressure". X2's *Another planet* bullet keeps the full clause verbatim.
12. **compound Scope, "the linearization is neutral"** (at equality). The S2 proof of `compound`(1) says it. The core keeps "the proposition is silent".

## 4. Other changes (wording; no mathematics changed)

- **Precision.**
  - "one that answers with delay produces a growing oscillation while the net gain is below one" became "can oscillate with growing amplitude".
  - `delayosc` proves that a net gain below one does not ensure stability, and exhibits one oscillating case. That is an existence claim, so "can" is the right word.
- **Levers paragraph, regrouped by channel type.**
  - Ratio channel: provision lowers the gain; a common decay "never does, since a contest of ratios does not see it, the first instance of what {{>blind}} says of every common term".
  - Level channel: correction lowers the gain; provision changes nothing.
  - Then sharing and diffusion, and the blocking-diffusion consequence with the Section 10 pointer.
  - Then the plan's "Trees for capacity …" line, which now closes the paragraph as its summary.
  - "Never lowers" is exact by `chansign`(2). In a ratio channel the elasticity of Γ in d is δ_f/(d+δ_f) ≥ 0, and that of Γ_δ is positive.
- **After `compound`.** Ren's game-design rule now follows the clause it compresses ("The second is the author's rule of game design"). The order is mechanism first, then Ren's line, then provision and trees, then diffusion, then enough.
- **The bench sentence** joins the paragraph "The meta-attractor of winning" as one sentence. It carries every condition of Remark S2.6: decays in (0,1], non-negative coefficients, and stable exactly when the product of coefficients < the product of rates. It cites "(Richardson 1960; {{bench}})".
- **"What the loop gain does not decide"** now has three sentences plus a closing line. The phrase "what the loop does to those who live with it" (V6.1) is kept.
- **Tightened without changing claims:** §2.1 ¶2 (two sentences merged), the §2.3 research-community example, the opening of "*Why 'meta-attractor'*", the compound Scope (the proportional-prize condition is stated first, because `standprice`(2) uses it), and the AI paragraph.
- **Kept unchanged:**
  - every statement (`cond`, `loopgain` Model and (1)–(4), `compound` (1)–(2), `meta`, `pathgen` apart from the duplicate clause in §3 item 7);
  - all six of Ren's quotations, verbatim with their keys and bracketed repairs;
  - every key;
  - the hand-off sentence.
- **Tags.**
  - Every remaining claim keeps its tag.
  - [num: CE] stays on "alone it can leave a laggard stalled short of the cap".
  - The [thm] and [num] of the box's rivals sentence went with that sentence (§3 item 1). Their claims keep their tags in `loopgain`(4) and its Scope.
- **S2 edits** are additions only: the six insertions listed in §2 above. No existing S2 sentence was changed or removed.

## 5. Preservation check: adjudication

Command, run from a scratch copy of v6.2 with these files in `src/`:
`python3 src/sentcheck.py planning/snapshots/draftA/src/core/20_s2.md src/core/20_s2.md src/supp/02_S2.md <all other src core/supp/disc files> --min 0.5`

The result was 145 sentences checked and 7 below 0.5. A second run, with only the two unit files as the pool, listed 12. All 12 are below.

| Containment | Sentence (draftA) | Disposition |
|---|---|---|
| 0.25 | "The other redirects those resources into expansion while continuing to use what others maintain." | **Merged** into "One spends resources maintaining it; the other redirects them into expansion while using what others maintain." (§2.1 ¶2) |
| 0.42 | "The channels add only because one win share feeds every stock: a stock fed by an expenditure chosen under another rule, such as lobbying bought from profits by a separate decision, is not a term of the sum." | **Merged** into the Scope's sentence "The channels must reinforce and be fed through one win share: … a stock fed by a separate decision, such as lobbying bought from profits, is not a term of the sum." |
| 0.30 (0.10 unit pool) | "If it stays fixed while capacity grows without depreciation, the condition of (1) holds date by date with the current total (S2)." | **Duplicate** of S2 *Growth variants* (a). The core Scope points to it: "S2 … lets capacity grow under a fixed prize". |
| 0.47 (unit pool only) | "Provision lowers it through capacity and changes nothing in a level channel, where it adds the same to everyone." | **Merged** into the levers paragraph ("provision lowers the gain" in a ratio channel; "provision, which adds the same to everyone, changes nothing" in a level channel). |
| 0.49 (0.22 unit pool) | "The core of the pressure is one structural loop gain; the pressure as a whole is a set of interconnected conditions, linked by … the concentration of standing. {{>thresholds}} sets them out." | **Merged** into "The pressure is therefore not one quantity but a set of interconnected conditions with one structural loop gain at its core ({{>thresholds}})". The "linked by …" clause is a **duplicate** of §7.1 (§3 item 8). |
| 0.36 | "Practices that produce more publications receive more funding, attract more students and are more widely copied." | **Kept in other words**: "Practices that publish more receive more funding and students and are more widely copied." |
| 0.30 (unit pool only) | "Structural explanation explains why intentions alone cannot account for recurrence; it does not erase responsibility, which differs with knowledge, discretion and power." | First half **merged** into the preceding sentence ("… and why intentions alone cannot account for recurrence"). Second half a **duplicate** of §0 (§3 item 5). |
| 0.00 | "The conditional form keeps its conditions in the sentence:" | **Merged**: "In conditional form, *recursive selection …*" (the italic statement is unchanged). |
| 0.22 (0.17 unit pool) | "One concept covers the mechanism and its generative dual, and every claim says which of the three senses it uses." | **Duplicate** (§3 item 6). |
| 0.14 (unit pool only) | "Members of a federation compete for capital and residents, and the strongest can capture the centre." | **Duplicate** of X2, *Federations* (§3 item 9). |
| 0.40 (unit pool only) | "In science, metrics allocate positions and the positions then set the metrics." | **Kept in other words**: "in science, metrics allocate the positions that then set the metrics". |
| 0.24 (unit pool only) | "In training, a policy is selected by a reward that a developer sets, and the developer is selected by a contest." | **Kept in other words**: "a policy in training is selected by a reward its developer sets, the developer by a contest". |

**Partial matches (0.5–0.8) worth naming,** from a stricter self-check run at 0.8 against the unit files:
- the box rivals sentence (0.61; §3 item 1);
- the levers' "Correction does the reverse …" (0.57; §2, chansign rows);
- "which the loop reaches only through the time a gap needs…" (0.72; §2, tdec row);
- the Richardson sentence (0.67; §2, bench row);
- the `pathgen` "since …" clause (0.61; §3 item 7);
- "recruits surrounding tissue" (0.70; §3 item 9);
- the another-planet clause (0.67; §3 item 11);
- "reproducible units that gain or lose share" (0.57; §3 item 10).

All the others in that range are rewordings with the same content.

**S2 against the snapshot:** 142 sentences checked, 0 below 0.5. S2 was changed by additions only.

## 6. Verification

1. **Test assembly** in `/private/tmp/claude-501/u02a/v62/` (a copy of v6.2 with both files in `src/`): "no problems"; 95 core declarations and 33 supplement declarations, as before. The rendered pointers read correctly: "(Table 7.1)", "(Richardson 1960; Remark S2.6)", "(Proposition S2.4)", "(Remark S2.1/S2.2/S2.3/S2.5)", "Proposition 3.9", "Proposition 4.4", "Proposition 5.15". No `{{` is left in the rendered §2.
2. **Preservation:** as in §5.
3. **Word counts:** as in §1.
4. **Mechanical checks:**
   - no kind word before `{{key}}` or `{{>key}}`;
   - no hedging "may", "plausibly" or "tends to" (one "tends to it as δ→1" is a limit);
   - no named states or firms;
   - all six Ren quotations are identical to draftA;
   - the key set is identical to draftA.

## 7. Open issues

1. **The rivals sentence in the box.** The box is 150 words without it, already above the 90–140 guide. With it, the box would be about 180 words. I followed the plan (D1-opus box plus the corrected lever sentence). If Ren or the integration editor wants the 30-minute reader to meet "leads can compound below a structural gain of one" in the box itself, the compact form is:
   > "Where rivals respond, the gain keeps its form with an equilibrium decisiveness [thm], and in the contests computed where a lead discourages the follower, leads compound below a structural gain of one [num]."

   D1-opus's §1.2 item 1 carries the same point ("and in contests where a lead discourages the follower, already below it").
2. **§7.1 points to §2.2 for "correction and non-appropriability"** as the levers in a level channel. §2.2 names correction (and $\chi\to0$ is in Table 7.1) but not "non-appropriability". This mismatch was already in draftA. One word in §2.2's levers paragraph ("correction and non-appropriability lower the gain") would close it, but I left the §2.2 claim as `chansign` states it, since non-appropriability is not a parameter of {{eq:gamma}}. The §7 unit should decide the wording.
3. **References.** These §2.4 citations are kept: Hanahan and Weinberg 2011; Aktipis et al. 2015; Arthur 1989; Stigler 1971. No core citation was removed, so `core/z9_refs.md` is unaffected. The draftA issue about SUPPLEMENT's references (Richardson, Harris and Vickers, Konrad and Kovenock) still stands: run `src/refs_v62.py` and reassemble.
4. **The responsibility clause** now lives only in §0 (§3 item 5). If the phase-2 rewrite of §0 drops it, restore it in §2.3 after "why intentions alone cannot account for recurrence".
5. **Carried over from the U02 merge notes, unchanged by this pass:**
   - the bracketed repairs in Ren's quotations;
   - "the author" used for Ren;
   - the renames for the symbol table;
   - the CHANGELOG entries (`bench` → Remark S2.6, `pathgen` → Remark 2.5, the `tdec` factor, talk among three or more);
   - the downstream consistency items for §3.8, §7, §10 and S13.
