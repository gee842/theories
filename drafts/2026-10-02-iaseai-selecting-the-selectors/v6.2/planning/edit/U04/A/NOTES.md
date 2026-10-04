# U04 elegance pass, editor A: Section 4 (`core/40_s4.md`) and S4 (`supp/04_S4.md`)

4 October 2026. Started from the current `src/` files, which are identical to the draftA snapshot. This directory held an unfinished core file from an interrupted earlier attempt: a partial edit with no S4 and no notes. I read it and then rewrote the unit from the snapshot. I kept three of its choices: the box's first two sentences merged; the closure sentence moved to §4.4; the Test B refutation added to §4.6's list.

The mathematics is unchanged and I found no errors. Every key, every declaration and every number is unchanged (95 core and 33 supplement declarations, as before). §4's numbering is unchanged: Definition 4.1 to Proposition 4.13; S4.1 `scope`, S4.2 `capdyn`, S4.3 `fieldlemma`.

## Word counts (assembler rule)

| | Snapshot | This edit | Change |
|---|---|---|---|
| Core §4 | 4,473 | 4,033 | −440 (−10%) |
| S4 | 4,857 | 5,126 | +269 |
| Claim box | 221 | 192 | −29 |

**Why the core is about 1,000 words above the target of about 3,000.** The extra words are result statements, together with conditions their proofs use. The rules forbid cutting them.
- Every result in §4 is cited by Parts II–IV, so none can move to the Supplement:
  - `capture` (§7, §9);
  - `influence` (§8, §10, §12);
  - `corrrate`(1)–(4) (§8, §9 R3a, §10);
  - `humancorr`(1)–(2) (§9, §12);
  - `masking` and `alarm` (§5, §6, §9, §12);
  - `certificate` (§9–§12);
  - `reabsorb` (§11, §12);
  - `pausefield` (§11's `pausevalue`(3));
  - `slowroute` (§7, §11, §12).

  `costq` is the premise of these results. `noinside` and `countervail` were already stated in S4.
- The declared statements, with the box and the model set-up they need, come to about 2,500 words. That leaves about 1,500 for the mechanism, Ren's lines, the consequences, the Scopes and the hand-off.
- Compared with V6.1's 2,613 words, the extra words carry the plan's mandated additions:
  - `humancorr`, with its lead-in, Scope and consequence (≈320);
  - the restored conditions of `corrrate`: the two halves of (2); (3)'s three cases, transient and lump sum; the Scope on gradual selection (≈250);
  - the barrier direction of capture (≈110);
  - `alarm`'s bound from evidence the model does not control, and the observability of $x_{\rm ev}$ (≈60);
  - `slowroute`'s clock version and Scope (≈120);
  - the restored line "growing understanding without executive authority may change nothing" (≈30);
  - the line-363 repair (≈70);
  - Ren's corpus line after the share-twice mechanism (≈60);
  - `pausefield`'s frozen-share formula (≈45);
  - the conditions on keeping pace (≈40).

What could still go, by about 150 words: the evidence standard for a claim that the loop operates (§4.1), the insurer clause (§4.4) and the lineage sentence in `influence`'s Scope. I kept all three:
- The evidence standard is what keeps the theory from validating claims about particular actors ("judge the game, not the act").
- The insurer clause is a design point.
- The lineage sentence follows the convention of every other section's Scope.

## Moves: core → S4

| Material (snapshot core) | Now in |
|---|---|
| "They differ in what shows them. Accommodation shows in enforcement that softens: an exemption, a threshold set where the incumbent already stands, a discounted liability." | S4, new first subsection "Capture: the two directions, and what does not suffice", sentences 1–2. The core points to it: "S4 gives the forms each direction takes, and the test". |
| Barrier forms "access conditioned on its interfaces, an obligation its lineage already meets" | Same subsection, sentence 3. The core keeps the per-carrier compliance cost (EV4). |
| "A carrier supports a rule that raises every carrier's costs when the rule is keyed to it, and opposes correction keyed to no one even where that correction would burden its rivals more; support for such correction at net cost to itself refutes the channel (TESTS, Test B)." | The prediction is in that S4 subsection, verbatim. The refutation is also the fourth item of §4.6's "What would refute the mechanism here", so the refutation tests stay in one list. |
| "though contraction can intensify the loop, since with less surplus to share relative position separates from everyone's absolute conditions" | Same S4 subsection, paragraph 2. The core keeps "Neither hierarchy nor contraction suffices (S4)". |
| "(LEDGER credits the distinctions to the first version)" | Same S4 subsection, last sentence. The distinctions stay in §4.1, so LEDGER's pointer (§4.1) is still right. |
| `influence` statement's "a square-root threshold when the floor is paid per carrier, a linear one when it is paid per decision" | Proof of `influence` in S4, after the threshold derivation. It is a reading of the exponent, not a condition. |
| `corrrate`(4)'s "for $\eta=1$, the third moment of shares when $\xi_v=0$ and the Herfindahl index when $\xi_v=1$" | Proof of `corrrate`(4) in S4. The core statement ends "a high moment of shares", the phrase §8 and §10 cite. TESTS Test B also gives the reading. |
| `corrrate` Scope's mechanism clause "which growing correction lowers, while cheaper control merely removes the brake" | S4.2 *Reading*, first sentence. |
| `alarm`'s AC sentence: "it leaves the lag-one autocorrelation of reports unchanged, so the host's recovery rate can still be read" | S4, "`alarm` in full", item (6), now with the clause "hides levels, not dynamics … recovery rate can still be read". The core keeps a one-sentence pointer with [num: AC]. |
| `pausefield` Scope's numbers for $x_\sigma$ (0.68, 0.98) | S4 DW numerics: 0.676 and 0.984. This was already there, so the numbers are now only in S4. The core Scope keeps the dependence: "$x_\sigma$ rises as rule-making slows relative to adoption [num: DW]". |
| §4.1 "Closure can also go deeper than masked measurement …" [conj; TESTS, Study 4] | Moved within the core, verbatim, to the end of §4.4's common-bias paragraph, where masking has been defined. |

## Duplicates removed, with their homes

- **"Equal incidence is not what keeps a rule; it is what keeps a rule from becoming a weapon."** Duplicate of §3.2 (`30_s3.md`, the paragraph after `blind`): "The sanction keeps a rule; equal incidence keeps a rule from becoming a weapon."
- **"A rule whose cost differs across carriers is selected on like any payoff difference ({{blind}}(2))."** Duplicate of the statement of `blind`(2). The core now cites it: "since unequal incidence re-sorts the compliant ({{blind}}(2))".
- **Why: "Delegation that erodes human capacity erodes the corrector too [thm]."** Duplicate of:
  - the box's own claim, "where correction rests on human capacity that delegation erodes, the required rate rises …";
  - `humancorr`'s title, "Delegation erodes the corrector";
  - `humancorr`'s lead sentence.
- **§4.1: "…({{>certificate}}(2)), a certificate that is sufficient, not necessary."** Duplicate of `certificate`'s Scope: "Part (2) is sufficient, not necessary".
- **`corrrate`(3): "its size threshold is proportional to $F_q^{\eta/(2+2\eta-\xi_v-\eta\xi_f)}$".**
  - The same formula is in the S4 proof of (3), "With $\hat Y\propto p^2$ the size threshold is proportional to …".
  - The core no longer uses the symbol $F_q$; S4 defines it.
- **`corrrate`(3): "after which only uncultivated conversion remains".** Duplicate of the S4 proof's "afterwards $G_{\rm ev}=A/(c_{\rm ev}d)\to0$". The statement now says the certificate holds from some date on.
- **`corrrate` Scope: "adjustment at a constant rate $\kappa_q$ delays failure by $\eta\ln(1+g_q/\kappa_q)/(\ldots)$, with $g_q=\ldots$ the growth rate of the selected level".** Duplicate of `capdyn`(2)(a) and of its hypothesis (S4.2).
- **`corrrate` Scope: "below the rate law selected capacity rises, so capacity that lags stays below it".** Duplicate of `capdyn`(1). The core keeps the conclusion, "fails no earlier than the quasi-static date ({{capdyn}})".
- **`corrrate`(2): "as it does for carriers that optimize and for adjustment at a constant rate".** This illustrates when $\liminf q/q^\ast>0$ holds; it is not a premise. The Scope says the same with its reason: "a result about carriers that optimize or adjust at a rate that does not fall".
- **`humancorr`'s "where $\mathcal M$ is the human capacity on which correction rests".** The lead-in paragraph and the box define $\mathcal M$. The statement keeps "the human capacity $\mathcal M$".
- **`humancorr` Scope: "with the cost of control constant and capacity at its selected level".** Not removed: it moved into statement (2) as its antecedent, so the statement owns its conditions. The Scope keeps "Part (2) is one simulation of one loop."
- **`alarm`: "a filter with memory defeats this, and once used as an alarm the indicator becomes a target".** Duplicate of S4 "`alarm` in full":
  - "a report filter with memory … the indicator fails";
  - "once used as an alarm it becomes a target".
- **`pausefield` Scope: "How long is long enough follows from the separatrix."** Duplicate of the S4 proof, "*The length of an insulated pause.* By cooperativity the basin of absence is a down-set, bounded by the separatrix".
- **`pausefield` Scope: "no pause is needed where $S(x_p)\ge G$".** It follows from the formula the core gives, and the S4 proof says "zero where $S(x_p)\ge G$".
- **`pausefield` Scope: "With $G=2$ and equal speeds the length is zero from $x_p=0.3$, $\ln2/(\varepsilon d)$ from $x_p=1/G$ and $1.50/(\varepsilon d)$ from 0.6 [num: DW]".** Duplicate of S4's DW numerics ("zero from $x_p=0.1$ and 0.3, 0.69 from 0.5 and 1.50 from 0.6") and the proof's "$\ln G/(\varepsilon d)$ at $x_p=1/G$". The core points to them: "(S4 gives the lengths)".
- **`slowroute` Scope: "In the joint simulations capture follows the certificate's failure by 8 to 85 periods, longer as correction approaches the rate law [num: QS]".** Duplicate of S4's QS numerics, "Across these runs capture follows the certificate's failure by 8 to 85 periods, longer as correction approaches the rate law".
- **`slowroute` Scope: "With correction not growing, capacity that adjusts fast enough lets the floor be crossed before the alarm, while capacity that adjusts slowly leaves evaluation uncaptured when the alarm is due; with correction growing at half the rate law, capture comes too late under every dynamic [num: SR]".** Duplicate of S4's SR numerics, which give each case with its numbers. The core sentence is now: "in the joint model either clock can come first, according to how fast correction grows and how fast capacity adjusts [num: QS, SR]".
- **Line-363 paragraph: "What keeps it is coverage and financing fixed in formula, through a loop that runs through the whole … (Section 10.4)".** Kept, shortened, as the second clause of the repair sentence. It now cites `pathgen` (Remark 2.5), the first home of "built and held by the whole, through coverage and formula funding".

## Merged or rephrased in place (no content lost)

- **Box.**
  - "In the models of this section the reflexive closure is a selection result [thm]" is merged into sentence 1: "In these models the reflexive closure is a selection result: where …".
  - The rate-law, floor and human-capacity claims are one sentence with three clauses, each tagged [thm].
  - The Why's "Success therefore converts into rule support that favours it, and the capacity for that conversion is …" is now "The capacity to convert success into rule support is …".
  - "Lowers the cost of control" reads "cheapens control".
- **§4.1.**
  - "Power can help an actor succeed under existing conditions or determine those conditions; the second closes the loop" is merged into "Power closes the loop when it determines the conditions of success rather than helping an actor succeed under them, and a claim that it does must show …".
  - "A barrier wears the form of correction, since a rule exists and is enforced" now reads "…, a rule that exists and is enforced, …".
- **`corrrate`.**
  - (3)'s cases are reordered:
    - $\alpha_{\rm cor}>\alpha_f$ carries the transient clause;
    - $\alpha_{\rm cor}=\alpha_f$ with $d_0\ge d_f(0)$;
    - otherwise the rate law decides, with the two sub-cases named.

    Every case and condition is kept, as is "three cases decide whether the certificate holds eventually".
  - (4): "with $f=0$ this delays … without preventing it".
  - The Scope's first sentence is reworded. Its "the rate law does not depend on how the cost of influence scales with size" is a duplicate of (2)'s "Both halves hold for every size elasticity $\xi_v$".
- **`humancorr`(2).** Reworded: "If captured evaluation reports delegation to be safe, so that delegation rises with $x_{\rm ev}$, capture is hysteretic: in one domain, with …, undoing capture … takes a permanent correction rate 1.6 to 2.6 times the rate that would certify evaluation without this loop, …".
- **`slowroute` Scope.** "Conditions (b) and (c) supply the mechanism … but they do not imply (e) …". The phrase "with the time constant of capacity among its terms" is merged into "how fast capacity adjusts".
- **Small tightenings.**
  - "Share enters twice …: hence the square, and hence the largest carriers …".
  - "as decision-makers' capacity does under delegation ({{>lockin}})".

## Preservation check (sentcheck, `--min 0.5`)

Run against the snapshot core, with the pool consisting of the new core, the new S4 and every other current core, supplement and discussion file: 148 sentences, 8 below 0.5. All are accounted for:

| Containment | Sentence | Adjudication |
|---|---|---|
| 0.43 | "Delegation that erodes human capacity erodes the corrector too [thm]." | Duplicate: the box claim, and `humancorr`'s title and lead sentence |
| 0.19 | "Power can help an actor succeed under existing conditions or determine those conditions; the second closes the loop." | Merged into §4.1's "Power closes the loop when it determines the conditions of success rather than helping an actor succeed under them" |
| 0.46 | "Off the selected level ({{capdyn}}): … $\kappa_q$ delays failure by …" | Merged: the conclusion is in the core Scope, "Capacity that lags its selected level fails no earlier than the quasi-static date". The formula duplicates `capdyn`(2)(a) |
| 0.44 | "AC]; a filter with memory defeats this, and once used as an alarm the indicator becomes a target." | Duplicate of S4 "`alarm` in full", (6) and AC numerics. The core keeps a pointer |
| 0.38 | `pausefield` Scope's "It depends on the speed of rule-making … 0.68 … 0.98 [num: DW]" | Rephrased in the core: "The threshold $x_\sigma$ rises as rule-making slows relative to adoption [num: DW]". The numbers are in S4's DW numerics (0.676, 0.984) |
| 0.14 | "How long is long enough follows from the separatrix." | Duplicate of the S4 proof, "*The length of an insulated pause.* … bounded by the separatrix" |
| 0.27 | "With $G=2$ and equal speeds the length is zero from $x_p=0.3$ …" | Duplicate of S4's DW numerics and proof |
| 0.47 | "With correction not growing, capacity that adjusts fast enough …" | Duplicate of S4's SR numerics. Summarized in the core's "either clock can come first …" |

S4 checked against the snapshot S4: 142 sentences, 0 below 0.5. Existing S4 text was only appended to, never rewritten:
- the threshold reading in the `influence` proof;
- the Herfindahl reading in proof (4);
- the first sentence of the S4.2 *Reading*;
- item (6) of "`alarm` in full";
- the new first subsection.

Containment between 0.5 and 0.85 comes from rephrasings in place, listed above. Two S4 sentences that are heavy with mathematics also fall in that range ((1) and the sufficient-half display, at 0.81 and 0.50). Both are byte-identical to the snapshot; the low scores are an artefact of the checker stripping the mathematics.

## Test assembly

The scratch copy at `/private/tmp/claude-501/u04A/test`, with these two files in `src/`, assembles with "no problems": 95 core and 33 supplement declarations, numbering unchanged. Rendered citations check out:
- `({{pathgen}}; Section 10.4)` renders as "(Remark 2.5; Section 10.4)";
- `({{bench}})` renders as "(Remark S2.6)";
- the S4 heading renders as "Capture: the two directions, and what does not suffice (Definition 4.1)".

## Kept deliberately

These stay verbatim, with their keys, Ren's ruling, tags and the plan's vocabulary:
- Ren's corpus line: 被选择的，开始选择选择者 [corpus: meta-attractor].
- The restored line "growing understanding without executive authority may change nothing". §12.2 points to it at Section 4.3.
- The claim box's existence "can" ("can be kept by those who buy it").
- "AI-assisted correction can keep pace" with its two conditions.
- The two halves of the rate law, (3)'s three cases with the transient, and the lump sum.
- `alarm`'s bound from evidence the evaluated model's behaviour does not control, and $x_{\rm ev}$ observable today.
- The line-363 repair.
- The hand-off.

## Open issues

1. **Length.** The core is 4,033 words against a guide of about 3,000. See the justification above. If the integration editor wants about 150 more words out, there are three candidates:
   - the §4.1 evidence standard for a claim that the loop operates (to S4's new subsection);
   - the insurer clause in §4.4 (to the S4 masking proof);
   - the lineage sentence in `influence`'s Scope (to S4's "Relation to earlier work"). If it moves, Dal Bó 2006 must move with it to the supplement reference list, since it would no longer be cited in the core.
2. **Box length.** The box is 192 words against a guide of 90–140. It carries six results, each with its antecedent conditions. The only further cut that respects "conditions as antecedents" is to drop "half under quadratic cost", which §4.3's double-duty paragraph also states.
3. **New citation of `pathgen` from §4.6.** It points back to the first home of the generative order's "held by the whole". If U02 rewrites `pathgen`, check that it still says this.
4. **CLAIMS.** The `pausefield` row says "Frozen-share threshold 0.68". The number is now in S4 only, and the core Scope carries the dependence with [num: DW]. The row's location ("S4; DW") is still right.
5. **TESTS.** Test B (ii)'s refutation now also appears in §4.6's refutation list. One home for refutation tests in this section; TESTS keeps the register entry.
6. **Carried over from the merge notes, untouched by this pass:**
   - references (Goldowsky-Dill, van der Weij, Greenblatt four-author, Grossman and Helpman, Smith 1995);
   - the QS and FF check comments;
   - the S13 rows;
   - the symbol table.
