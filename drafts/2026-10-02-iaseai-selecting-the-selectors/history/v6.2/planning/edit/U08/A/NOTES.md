# U08 elegance pass, editor A: Section 8 (core `80_s8.md`), S8 (`08_S8.md`), X8 (`08_X8.md`)

4 October 2026. Start point: the current `src/` files for this unit, which are identical to `planning/snapshots/draftA/src/` (checked with `cmp`). The directory `planning/edit/U08/A/` was empty, so there was no interrupted attempt to finish. Sections 2–5 in `src/` already hold their edited versions; the hand-offs to §7 and §9 and the references from §4, §5.2, §12.1 and X10 were checked against the current files.

Files written (only these four):
- `planning/edit/U08/A/core/80_s8.md`
- `planning/edit/U08/A/supp/08_S8.md` (one sentence changed)
- `planning/edit/U08/A/disc/08_X8.md` (four insertions)
- `planning/edit/U08/A/NOTES.md`

## 1. Word counts

| | Snapshot (draftA) | Edited | Change |
|---|---|---|---|
| core §8, assembler count | 5,388 | 4,436 | −952 (−17.7%) |
| core `80_s8.md`, raw words | 5,393 | 4,443 | −950 |
| Part III lead + heading + claim box (raw) | 342 | 289 | −53 |
| of which the claim box (Claim + Why) | 286 | 233 | −53 |
| §8.1 the standard | 1,185 | 1,048 | −137 |
| §8.2 profiles, marks, durability | 675 | 645 | −30 |
| §8.3 the alternatives | 2,503 | 1,934 | −569 |
| §8.4 the comparison (table + paragraph + hand-off) | 688 | 527 | −161 |
| of which the table | 435 | 341 | −94 |
| supp `08_S8.md`, raw | 3,273 | 3,286 | +13 |
| disc `08_X8.md`, raw | 6,642 | 6,909 | +267 |

Assembled totals in the scratch build: supplement 46,815 → 46,828; discussion 15,047 → 15,287.

**On the target (about 3,300).** The section lands at 4,436. I stopped there because what remains is either a statement that Parts III and IV cite, an item the plan or the reviews put in §8, or a Ren line:
- **Seven keyed results stay in the core, each cited from the core of Parts III–IV or on the spine**, so none can move under plan §2: `kernel` (§10, §12), `fallback` (spine, the judgment's first result, D1-opus §1.1), `profile` (§9's hand-off takes it), `durability` (§12), `preventown` (§12.1), `assure` (§5, §9, §11) and `verify` (§11). Their statements, with every condition their proofs use, are about 800 words. The (g) setup that defines $R,T,P,S,\upsilon,F,\varpi,g_C,g_D$ (about 90) and the $\Phi$ definitions that `preventown` uses (about 50) have to come before them.
- **Plan-required core items**, about 1,350 words: the protection standard with the Jones correction (plan §4 §8, D4 A3) and the N1/C10 sentence; the rule for $\Theta$, naming the design's own failure modes (Codex's symmetric comparison); G1–G7 in canonical wording, with the threshold each reverses; the registered prediction and the pseudo-solution label (restored by the v6.0 fidelity check; LEDGER §4); the strongest form of each alternative with the reading the reviews asked for (Bueno de Mesquita et al. read correctly; Fudenberg–Koh with its two conditions; the tax driven to zero or below class by class; "AI-assisted correction can keep pace", which §4 points to as Section 8.3(a)); κ_W and C13 in (d); the sprint answered by mechanism against E2 and custody; the hard case, which §12.1 cites as "Section 8.3(f)"; the comparison table, which the plan keeps, with the coercive row as a tier-3 candidate.
- **Ren's lines and rulings**: the four capacities 未/可/应/转 and 护闭/成闭 [corpus: possibility-space]; "It persuades by promising both security and benefits; both rest on the winner's restraint after the fact"; "insurance accepts the frame of the contest, hedging against losing instead of declining the game"; "keep the contest, slow it and stay safe" with "the answer is to the position, not to the plan's figures".

Getting to 3,300 would mean thinning those statements, which was V6.1's error, or emptying (a)–(e) down to labels, which would leave the core reader without the mechanism by which each alternative leaves its thresholds. What I did cut is every strongest-form citation, number and "what remains" clause that X8 or S8 already holds in full. If the integration pass wants §8 shorter, the uniform options are in §6 below.

**Claim box.** 233 words against the brief's 90–140, down from 286. It states four claims and the conjecture, each sentence with its antecedent and its tag, and gives one line for each of the four mechanisms. The cuts came from inside sentences: "what decides is the direction, for whom, and whether the change survives success" is already said in the Claim's second sentence and in the profile definition, and the mechanisms are compressed to one clause each.

## 2. Moves (core → companion), with the pointer left in the core

Most of what left the core was already in X8 or S8 in fuller form; those items are listed under duplicates in §3. These sentences had no adequate home and were moved:

| # | What left the core | Where it now lives | Pointer in the core |
|---|---|---|---|
| M1 | §8.4 table, column "Main residual risk" (nine cells) | X8, new table **Main residual risk, path by path**, after the present-policies table and before the evidence standard; X8's opening sentence now lists it among the closing tables | "X8 gives each path's main residual risk and, path by path, each failure mode in $\Theta$ …" |
| M2 | (e) "The sprint's freeze answers to the sprinter's own correctors and, when the sprinter breaks it, to no one (D4, D5); custody is designed for separated functions under correctors certified independent of every party, certificates not yet measured (C4; X8 sets the two side by side)." | X8, *Against common custody*, after the D4/D5 table, verbatim, as "its certificates not yet measured (C4)" | "… incidence and holder, which X8 compares on D4 and D5" |
| M3 | §8.1 "For a leader whose exit would hand a rival a decisive win, the shared hazard is what carries the case for restraint [num: legacy v4.4, SV]." | S8, `survassure` *Numbers*, third bullet, replacing S8's "For the leader, the shared hazard carries the argument." (same point; the core's wording names the condition) | `({{survassure}})` at the end of the survival paragraph |
| M4 | (a) strongest form "oversight with the right topology ({{topology}})" | X8, *Technical alignment*, Best case: "Oversight can be built with the right topology, redundantly or adversarially by debate ({{topology}})" (the key was missing there) | `{{topology}}` stays in (a)'s *What remains* |

Nothing moved into S8 apart from M3; S8 already held every number the core dropped (Jones's figures, the lead's 4.7/7.9/12.2 months, the survival examples, the advantage formula).

## 3. Duplicates removed (true duplicates of text elsewhere in the paper)

| Sentence or clause removed from the core | Where the point lives |
|---|---|
| Box Why "and what decides is the direction, for whom, and whether the change survives success" | Box Claim sentence 2; `profile` definition ("so what is recorded is the direction …") |
| §8.1 Jones's figures: "at a 1% annual hazard and 10% growth, a planner with logarithmic utility accepts about a one-in-three cumulative risk for a 55-fold gain in consumption, and with curvature 2 about 4%" | S8 *The discounting comparison* (same figures, with the 40- and 4.5-year stopping times); core points "S8 gives his figures" |
| §8.1 survival paragraph: "With trust $\varpi$ that the other restrains, the advantage of restraint is $\varpi(\Phi^R-\Phi^T)+(1-\varpi)(\Phi^S-\Phi^P)$" | S8 `survassure`(1), verbatim; the core keeps the four-way classification by the two signs |
| §8.1 survival paragraph: the hazard list "delegation's loss of the capacity to overrule, the shared hazard, preventive attack, a rival's decisive win" and the gloss "racing beside a racer survives better than staying out" | S8 `survassure` statement ($q_{\rm I}$, $q_{\rm II}$, $q_W$, $p_{\rm dec}$); the gloss restates $\Phi^P>\Phi^S$ under the definitions just given. The core keeps "each counting the hazards of its branch" as the condition |
| §8.1 "with its reasons" (Section 12.1 states the ranking …) | §12.1 tier 3, reasons (i) and (ii) |
| §8.2 durability prose "each entry is read from the arrangement's own documents and estimates" | `durability` definition, first clause |
| §8.4 "At the standard's third step (Section 8.1) the comparison needs estimates on both sides, and those estimates are what the cruxes of Section 12.3 would supply." | §12.1 tier 3 ("That step needs estimates on both sides, which the cruxes would supply and do not yet"); §8.1 keeps that the comparison falls to the third step and is a judgment |
| §8.4 "An expected-value criterion that puts low probability on a rising uncovered share and values speed highly can prefer continuation, and a discounted criterion with utility linear in consumption prefers racing whenever the hazard it adds is below the growth it adds." | X8 *Where the criteria disagree* (the same sentence) and §8.1 (the linear-utility result, [thm]) |
| (a) "control scoped to early transformative systems"; "weak supervisors eliciting part of a stronger model's capability (Burns et al. 2023)"; "auditors with access to training data finding a planted objective that black-box access missed (Marks et al. 2025)"; "with cheapening control"; "so that the safe variant is also the winning one and its safeguards spread without coordination"; "in its proponents' own plans, a strong international agreement ranked first" | X8 *Technical alignment*, Best case, each in full; §4 ("as fast as it cheapens control") |
| (a) "systems are retained for performance ({{retain}})"; "redundant oversight is capped by the common causes selection produces"; "AI-assisted correction is only as independent as its funding, access, appointment and lineage"; "admission removes only what it detects" | X8 *Technical alignment*, What remains, each verbatim; the lineage condition also in §4 ("only where it is independent of the evaluated lineage") |
| (a) "*Profile:* it leaves compounding, standing and enforcement where they were" | §8.4 table, row 1, column "Thresholds it leaves on the danger side" |
| (b) "after a major accident"; "with independent investigation and insurance pricing" | X8 *Regulated competition*, Best case |
| (b) "coverage across jurisdictions, since" | §8.4 table row ("across jurisdictions") and X8 ("Regulation in one market leaves the load elsewhere") |
| (b) "so a catastrophic or common harm cannot be turned wholly into a private cost" | X8 *Regulated competition*, What remains ("for catastrophic and common harms that is the point at which a common cost cannot be turned into a private one") |
| (b) "and one unreviewed study codes 77% of the changes it traced, in twelve pairs of consecutive framework versions, as weakening" | X8 *Regulated competition*, What remains (verbatim) and §7.3 T2 row |
| (b) "which G1 and G6 secure"; "weighs a shared hazard by $1+\theta$, and not at all at $\theta=-1$" | X8 Fudenberg–Koh paragraph ("an argument for two of them: G1 … G6 …"; "weighs a shared hazard by $1+\theta$ and drops it at $\theta=-1$") |
| (b) "*Profile:* it depends on content." | X8 *Regulated competition*, What it changes ("This depends on content") |
| (c) "a six-month lead diffusing at a tenth a month lasting under five months [num: legacy v4.5, LD]" | S8 `lead`(1) (4.7 months, with 7.9 and 12.2) |
| (c) "the strongest form relies on" (after "discouragement"); "what the margin must buy is coverage, and"; "by the leader's own evaluators under time pressure"; "where effort is greatest" | the strongest form two clauses earlier; S8 `lead`(2), (3); X8 *Leadership* ("where effort is highest in contests of step-by-step innovation") |
| (c) "*Profile:* it acts on tempo for a time and leaves the objective of winning in place." | §8.4 table row; X8 *Leadership*, What it changes ("Tempo for a time; it keeps the objective of winning") |
| (d) "victors have bound themselves through institutions (Ikenberry 2001), a dominant power can supply public goods (Kindleberger 1973), and an encompassing ruler internalizes the shared conditions (Olson 1993)" | X8 *The benign winner*, Best case (all three, with Gilpin and Wohlforth) |
| (d) "with no one to sanction it" | X8 durability table, benign-winner D5 ("with no one outside to enforce it") |
| (d) "the winner is itself a field of agencies, firms, laboratories and systems, whose restraint after victory depends on" | X8 *The benign winner*, What remains (verbatim); the core keeps "the winner's own correctors can be bought by its successes" |
| (d) "*Profile:* it changes nothing in selection before victory. What would show it suffices are the commitment tests: binding limits on what victory confers, benefits shared as they arise rather than promised, and the coalition's own correctors certified independent, with succession rules that survive changes of leadership (Test I)." | §8.4 table row ("Nothing before victory"); X8 *The benign winner*, What it changes and What would show it suffices (the same tests, with C13 added) |
| (e) "or roll back"; "and gives up only permanent superiority" | X8 *A finite sprint*, Best case and Maintenance bullet; S8 `sprint` |
| (e) "by kind of objection. Exposure: … whether that exposure is survivable is C1 and C5. Maintenance: …"; "which V2 and V3 protect"; "and they read it as a lead being kept"; "{{corrrate}}(4)" | X8 *A finite sprint*, What remains, by kind of objection (verbatim, with the kinds labelled); S8 `sprint`(ii) |
| (e) "*Profile:* nothing changes in selection during the sprint." | §8.4 table row ("Tempo, after the sprint"); X8 *A finite sprint*, What it changes ("Nothing during the sprint") |
| (f) the labels "Normatively / Epistemically / Technically"; "detecting unobservable progress and" | X8 *Deterrence and prevention* (*Normative*, *Epistemic*, *Technical*; "detecting unobservable progress and striking at machine speed") |
| (f) "observing datacentres and making compute thresholds salient (Hendrycks, Schmidt and Wang 2025)"; "its credibility can reverse under survival-first comparisons, its red lines are hard to state and to monitor (X8), and algorithmic progress erodes thresholds stated in compute [obs: EV9]" | X8 *Deterrence and prevention*, second paragraph (Best case; What remains: unclear red lines, credibility reversing under survival-first comparisons, EV9) |
| (f) "That is the case the ruling of Section 3.8 closes: against a winner of that logic falling behind cannot be made survivable" | §3.8 (Ren's ruling, its home); S8 `insure` ("which is the reply that the ruling of Section 3.8 rejects, since against a winner of that logic falling behind cannot be made survivable"); X8 hard case |
| Hard case "it compares denial, a coalition that stops the decisive class, and prevention, and" | X8 *The hard case* (verbatim) |
| (g) "with compute declarations, supply-chain accounting, recomputation of workloads" | X8 *A verified agreement*, Best case (verbatim, with research transparency) |
| `assure` Scope "timely detection must exceed a level that rises with the value of winning" | §5 `detectlink` (its home; the same words) |
| Instance "is designed to be enforceable without trust, with proportional reserves and a coalition that must stay ahead of covert projects" | X8 *A verified agreement* ("it works without trust"; "through proportional reserves and a coalition that must stay ahead of covert projects") |

Merged within the core (no content lost):
- §8.2's export-controls paragraph, second sentence ("Deterrence by threatened sabotage acts on $p_d$, as custody does, by a different means and with a different fallback") → merged into (f): "Deterrence by threatened sabotage acts on $p_d$, as custody does, but by threat; its fallback is war or race".
- §8.4 "These disagreements are the normative cruxes." → merged into §8.1: "the criteria it declines rank paths otherwise, and each disagreement is a normative crux".
- §8.3 intro "and what would show that it suffices" → "X8 gives each in full, with how it would be installed and what would show that it suffices" (X8 has a "What would show it suffices" for each of (a)–(d)).
- "*Profile:*" labels in (a), (b), (g): the sentences that carry content no other place has are kept without the label ((a) G3/G7; (b) content-dependence, in the two regulation sentences; (g) "a bridge"). In (d), "A winner that adopts these" became "A winner that meets the commitment tests of X8 (Test I)".
- The κ_W/C13 order in (d): "that need after victory is what the race cannot verify beforehand, and what AI can lower (C13)" now comes first under *What remains*, so it follows the κ_W sentence it qualifies. Both are also in §5.2, which the merge notes name as their home; (d) keeps the one-sentence statement the plan asks for.

Reworded without any change of content: box Claim 3 ("however its dissolution is decided" → "whatever decides its dissolution"); box Claim 5 ("That … is a registered prediction" → "… are predicted to erode … [conj]"; the label "Registered prediction" stays in §8.2); fallback prose ("The two conditions are design conditions, read from …" → "Both conditions are read from …"; the lemma's headline already says "design conditions"); kernel ("The standard's second and third steps, which prefer …" → "The standard's preference for keeping options of correction open …"; "a different and smaller question" → "a smaller thing"); hard case ("has a best course: to propose" → "does best to propose"); table cells ("through" → "by"; "where tax-lowering results are published" → "where its reduction is published"; "the alignment tax for masked classes" → "the tax for masked classes", since the column header and row make it unambiguous).

## 4. Preservation check

Commands, run in the scratch copy `/private/tmp/claude-501/u08A/v6.2` with the three new files in its `src/`:
`python3 src/sentcheck.py <snapshot>/src/core/80_s8.md src/core/80_s8.md src/supp/08_S8.md src/disc/08_X8.md <every other current core/supp/disc file> --min 0.5`, and the same for `supp/08_S8.md` and `disc/08_X8.md`.

**Core: 152 sentences checked, 5 below 0.5.**
1. (0.45) "The standard's second and third steps, which prefer what keeps options of correction open, are a preference for staying inside the kernel." Kept in other words in §8.1: "The standard's preference for keeping options of correction open is a preference for staying inside the kernel." The link is also in §12.1(i).
2. (0.36) "Pacing needs a hazard that the racer itself bears and transparency, which G1 and G6 secure and the conditions of winning erode: relative accounting weighs a shared hazard by $1+\theta$, and not at all at $\theta=-1$ …" Kept in other words in (b): "the conditions of winning erode both conditions of pacing, the hazard through relative accounting ({{twochan}}), transparency through quiet deviation, captured evaluation and masking (…; X8)". The G1/G6 clause and the $\theta=-1$ detail are duplicates of X8's Fudenberg–Koh paragraph (§3).
3. (0.17) "*Profile:* nothing changes in selection during the sprint." Duplicate: §8.4 table row; X8 "What it changes. Nothing during the sprint" (§3).
4. (0.43) "Deterrence by threatened sabotage acts on $p_d$ by threat, observing datacentres … [obs: EV9]." Merged with §8.2's export-controls second sentence into (f)'s "Deterrence by threatened sabotage acts on $p_d$, as custody does, but by threat; its fallback is war or race, and X8 gives its best case and what remains"; the rest duplicates X8's deterrence paragraph (§3).
5. (0.46) "At the standard's third step (Section 8.1) the comparison needs estimates on both sides …" Duplicate of §12.1 tier 3 (§3); §8.1 keeps the fall to the third step.

**S8: 86 sentences checked, 2 below 0.5.**
1. (0.17) "*Numbers* ($n=2$, $p_{\rm ext}=1$) [num: legacy v4.4, SV, …;" Unchanged in S8. A false positive: the line is almost all markup, which the check strips.
2. (0.14) "For the leader, the shared hazard carries the argument." Replaced by the core's fuller sentence (M3), which names the condition.

**X8: 178 sentences checked, 0 below 0.5.** X8's existing text was not rewritten; there were four insertions only.

## 5. Keys, tags, mathematics, references

- **Declarations**: unchanged in all three files: core `kernel`, `fallback`, `profile`, `durability`, `preventown`, `assure`, `verify`; S8 `survassure`, `lead`, `sprint`, `insure`, `overhang`. Kinds and order are unchanged. The scratch assembly gives 95 core and 33 supplement declarations, with **no problems**.
- **Citations of keys left the core only where the clause moved**: `{{retain}}` (in X8), one `{{topology}}` (moved to X8's best case, M4; the core's other one stays) and `{{corrrate}}(4)` in (e) (in S8 `sprint` and X8). Every key is still cited somewhere.
- **Tags**: no tag was changed on a sentence that stays. These tags left the core with their sentences: `[num: legacy v4.4, SV]` (M3, in S8, under the numbers block's label), `[num: legacy v4.5, LD]` (in S8 `lead`) and `[obs: EV9]` on deterrence (X8 gives "(EV9)"; the core's `verify`(3) still cites EV9).
- **Mathematics**: unchanged. No error was found. `assure`'s $T-P+F>0$, `preventown`'s $s_P\Phi^R>0$, `verify`(3)'s [def]/[conj] split and `fallback`'s state-dependent dissolution clause stand as merged.
- **Ren rulings and vocabulary (plan §5, §8)**: all kept verbatim. They include 未/可/应/转 and 护闭/成闭 with their corpus key; the tone sentence of (d); the insurance ruling; "keep the contest, slow it and stay safe"; the G1–G7 wording and order; "provision … beneath the game"; "structural loop gain"; "whatever it is called"; E2 kept apart from E3 (the sprint passage contrasts the sprint with "E2 and common custody" on stopping only).
- **References** (lists are generated by `refs_v62.py`, not by this unit): these works are no longer cited in the THEORY core and are not cited elsewhere in it: Burns et al. 2023; Hendrycks, Schmidt and Wang 2025; Ikenberry 2001; Kindleberger 1973; Olson 1993. All five are cited in X8, so they stay in DISCUSSION. Marks et al. 2025 is still cited in §6. The THEORY list drops these five on the next `refs_v62.py` run.

## 6. Open issues

1. **Length.** §8 is 4,436, about 1,100 over the guide. If the integration pass wants it nearer 3,300, these are the options that lose no condition, in order of cost:
   - (i) move the hard case to X8, leaving one sentence. §12.1 cites "the hard case of Section 8.3(f)", so its wording would then need to change.
   - (ii) cut the strongest-form citations of (b)–(d) to one clause each, with X8 carrying them.
   - (iii) define $\Phi^R,\Phi^P,\Phi^S$ inside `preventown`'s statement and reduce the `survassure` paragraph to one sentence. This saves only about 30 words and weakens the "each counting the hazards of its branch" condition, so I did not do it.
   - (iv) drop the box Why's four mechanisms. They repeat §8.3 one line each, but the box is the only place that gives them together.
2. **§12.1 duplicates §8.1.** It restates that every worst case includes an irreversible loss, so the ranking falls to the third step. Plan §8 makes §8.1 the home of the third step and asks §12.1 only to apply it. That is U12's call. §8 now states it once in the box and once in §8.1.
3. **κ_W and C13** are stated in both §5.2 and §8.3(d), because the plan asks for each. If U05/U12 make §5.2 the single home, (d) can shrink to a pointer.
4. **Inherited from the merge notes and still open:**
   - legacy block labels (v4.4 SV, v4.5 LD, v5 FS/CMP/N13) still need porting into `checks_v62.py`;
   - CLAIMS should mark the model wordings with D (the tone sentence; the English of the insurance ruling);
   - the symbol table needs $\Phi^R,\Phi^T,\Phi^P,\Phi^S$, $\mathsf u_t$, $V^{\rm exit}$ and $V^{\rm stay}$;
   - `{{participate}}` must resolve once U10's S10 declares it (it resolves in the current scratch build);
   - EVIDENCE gap 7 should name the analogue base rate.
