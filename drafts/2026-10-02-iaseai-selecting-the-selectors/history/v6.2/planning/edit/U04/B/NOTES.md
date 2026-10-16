# U04 elegance pass, editor B: Section 4 (`core/40_s4.md`) and S4 (`supp/04_S4.md`)

4 October 2026. Start point: the current `src/` files (identical to `planning/snapshots/draftA/src/`). This directory held an interrupted earlier attempt (core and supp only, no notes); I checked it, kept its sound moves, reversed one (see §7), and completed the pass.

## 1. Word counts

| | Core §4 (assembler rule, assembled) | S4 (same rule, assembled) |
|---|---|---|
| V6.1 | 2,613 | 1,631 |
| Merged (snapshot) | 4,473 | 4,857 |
| This pass | **4,246** | **5,027** |
| Target given | about 3,000 | — |

Claim box: 221 → 205 words by the assembler's rule (which counts each tag and each formula as a word); about 170 words of English.

**Why the core stays near 4,250 and not 3,000.** Every result of §4 is cited from Parts II–IV, several by part number: `corrrate`(1)–(4) (R3a, §8.3, §10.3/10.5, S2, S7, S8, S9, S10, S14, X8), `humancorr`(1)–(2) (§9, §12.1 tier 1(b) and release, S7), `certificate`(1)–(4), `reabsorb`, `pausefield`, `slowroute`, `masking`, `alarm`, `noinside`, `influence`. None may move to the Supplement as a side result, and no statement may lose a premise. Against V6.1's 2,613 words, the merged section carries, in words that no companion can hold for it:

- `humancorr`: lead, statement, Scope and the both-sides consequence (about 330);
- the two directions of capture, in the Definition and the mechanism paragraph that follows it (about 180);
- `corrrate`(2)'s two halves with the tracking condition, (3)'s three cases with the transient clause and the lump sum, and the halves' $\xi_v$-independence (about 230);
- the definitions the halves need: "certified", $\hat Y$, $\hat B$, the selected level with the floor (about 70);
- `alarm`'s evidence ruling (the bound from weights, activations, training data and elicitation; $x_{\rm ev}$ observable) (about 80);
- `slowroute`'s clock version, (b), (c) and (clock), with the premise list set out (about 90);
- `pausefield`'s frozen-share formula (plan §3, Sys I4) (about 50);
- the line-363 repair and the hand-off (about 60);
- Ren's restored lines and the corpus key (about 50);
- the box, with every result given its antecedent and a tag per sentence (about 110).

That is about 1,250 words of conditions and results, which puts the floor of a faithful §4 near 3,850; the remaining 400 are the Scope sentences on off-level capacity, the floor case of `humancorr`, and the common-bias and refutation paragraphs, each of which a reader of the core needs. I could reach 3,000 only by dropping premises (V6.1's error) or by moving parts of cited results, which would break `{{corrrate}}(3)`, `{{corrrate}}(4)` and `{{humancorr}}(2)` citations in other units that I may not edit. I did not do either.

## 2. Moves (core → companion)

Each with the pointer left in the core.

1. **Forms of each direction of capture** (§4.1 prose: "an exemption, a threshold set where the incumbent already stands, a discounted liability"; "access conditioned on its interfaces, an obligation its lineage already meets, or a compliance cost fixed per carrier") → S4, new opening subsection "The two directions of capture: what shows each". Core pointer: "(EV4; S4 gives the forms of each direction)". The mechanism (relief and burden move the same payoff difference; `{{blind}}`(1),(2)), the "weighs most, per decision, on entrants and the smallest carriers (EV4)" clause, "Equal incidence is not what keeps a rule…", the appropriability mark and the Test B refutation sentence all stay in the core.
2. **Contraction's mechanism** ("since with less surplus to share relative position separates from everyone's absolute conditions") → the same S4 subsection, last sentence. Core keeps "though contraction can intensify the loop (S4)". The four-step chain a claim of the loop must show stays in the core (a reader needs it to test claims; the interrupted attempt had moved it, see §7).
3. **Lump-sum size threshold exponent** $F_q^{\eta/(2+2\eta-\xi_v-\eta\xi_f)}$ (`corrrate`(3)) → already derived in S4, proof of `corrrate` (3), "The lump sum". Core pointer: "(S4 gives its size threshold)". The lump sum's conditions (paid once if any is held; only delays; requirement unbounded as control cheapens) stay in the statement.
4. **Transient clause in full** ("A certificate that holds from some date on need not hold before it: cultivation that ends can carry the row sum above one on the way") → merged into (3)'s first case as "though the row sum can pass one before cultivation ends [num: FF]"; the full form is S4, proof of `corrrate` (3), "The transient".
5. **Constant-rate delay formula** $\eta\ln(1+g_q/\kappa_q)/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$ and $g_q$ (`corrrate` Scope) → S4 `capdyn`(2)(a) (already there) and the `capdyn` *Reading* ("Under adjustment at a constant rate the delay of (2)(a) is the whole effect…"). Core Scope keeps "adjustment at a constant rate only delays it".
6. **Gradual-selection mechanism** ("pushes capacity only by its marginal return $\chi\hat Y/d$, which growing correction lowers, while cheaper control merely removes the brake") → `capdyn` *Reading*, first sentence. Core Scope keeps the condition and its consequence: "gradually selected capacity stays bounded unless its variance outgrows capacity".
7. **"correction growing at any positive rate certifies in the end, after a possible transient failure"** (`corrrate` Scope) → `capdyn`(2)(b) states it ("the certificate holds from some date on for every $\alpha_{\rm cor}>0$, after a possible transient failure"); the core Scope cites `{{capdyn}}`.
8. **Autocorrelation detail** (`alarm`: "leaves the lag-one autocorrelation of reports unchanged"; "a filter with memory defeats this, and once used as an alarm the indicator becomes a target") → S4 "`alarm` in full" (6) and the AC numerics (already there). Core keeps one sentence: "Static affine masking hides levels, not dynamics, so the host's recovery rate can still be read from the autocorrelation of reports, until a filter with memory is used or the indicator, once an alarm, becomes a target [num: AC]".
9. **Pause lengths** ("zero from $x_p=0.3$, $\ln2/(\varepsilon d)$ from $x_p=1/G$ and $1.50/(\varepsilon d)$ from $0.6$") and "$x_\sigma$ rises to 0.98 when rule-making is ten times slower" (`pausefield` Scope) → S4 DW numerics (already there; the $0.69=\ln2$ at $0.5=1/G$ gloss added so the moved sentence is findable). Core keeps the dependence on speed with one pair ("never from 0.68 or more, and $x_\sigma$ rises toward one as rule-making slows [num: DW]") and the formula, with "(S4 gives the lengths)".
10. **Capture lag 8 to 85 periods** and the SR dynamics ("With correction not growing, capacity that adjusts fast enough lets the floor be crossed before the alarm…; with correction growing at half the rate law, capture comes too late under every dynamic") (`slowroute` Scope) → S4 QS numerics ("Across these runs capture follows the certificate's failure by 8 to 85 periods, longer as correction approaches the rate law") and SR numerics (already there in full). Core keeps the conclusion the argument needs: "whether capture precedes the alarm turns on how fast capacity adjusts as well as on the rate law [num: QS, SR]".

## 3. Duplicates removed (one home)

- §4.1 setup, "a certificate that is sufficient, not necessary" → home is `certificate`'s Scope ("Part (2) is sufficient, not necessary…"), unchanged.
- Claim box, "half under quadratic cost" → home is the §4.3 double-duty paragraph ("under quadratic cost ($\eta=1$), half the rate suffices"), unchanged. The box keeps "a stated fraction of that rate".
- `corrrate` Scope, "The necessary half is therefore a result about carriers that optimize or adjust at a rate that does not fall" → the statement's (2) already carries "as it does for carriers that optimize and for adjustment at a constant rate"; the Scope keeps only the design consequence ("a result about carriers that optimize, the case a requirement should be designed against"), which R3a relies on.
- S4, end of the `humancorr` QS numerics: "The form $d_{\rm eff}=d(\mathcal M/\mathcal M_0)^w$ is a modelling choice inside the open interface 'Human capacity and correction' (S13)" → home is the core `humancorr` Scope, first sentence. (Inherited from the interrupted attempt; confirmed.)
- Claim box, Why: "Success therefore converts into rule support that favours it, and the capacity for that conversion is a trait…" tightened to "Converting success into rule support is a trait like any other…", since the first clause restated the Claim.

## 4. Preservation check (sentcheck, --min 0.5)

Run in the scratch copy `/private/tmp/claude-501/u04b-1791084978` with the pool = my two files + every other current `src/{core,supp,disc}` file.

**Core** (snapshot `core/40_s4.md`): 148 sentences, 6 below 0.5, each adjudicated:

| Containment | Sentence | Adjudication |
|---|---|---|
| 0.39 | "A barrier wears the form of correction, since a rule exists and is enforced, and is the easier to overlook." | Merged into the core's "They differ in what shows them: accommodation in enforcement that softens; a barrier in correction's own form, a rule that stands and is enforced, which is why it is the easier to overlook." |
| 0.32 | "A claim that it operates must show a transfer of costs onto weaker participants, a resulting change in their dependence, the conversion of that dependence into selection power, and a weakening of correction." | Kept in the core in tighter words with the same four steps in the same order: "must show the chain in sequence: costs shifted onto weaker participants, their dependence changed, that dependence converted into selection power, and correction weakened." |
| 0.40 | "A certificate that holds from some date on need not hold before it: cultivation that ends can carry the row sum above one on the way [num: FF]." | Merged into `corrrate`(3), first case ("though the row sum can pass one before cultivation ends [num: FF]"); full form in S4, proof of `corrrate` (3), "The transient" (move 4). |
| 0.44 | "…AC]; a filter with memory defeats this, and once used as an alarm the indicator becomes a target." | Merged into `alarm`'s last sentence; in full in S4 "`alarm` in full" (6) and AC numerics (move 8). |
| 0.36 | "With $G=2$ and equal speeds the length is zero from $x_p=0.3$, $\ln2/(\varepsilon d)$ from $x_p=1/G$ and $1.50/(\varepsilon d)$ from $0.6$ [num: DW]." | Moved to S4 DW numerics (move 9). |
| 0.47 | "With correction not growing, capacity that adjusts fast enough lets the floor be crossed before the alarm, … with correction growing at half the rate law, capture comes too late under every dynamic [num: SR]." | Moved to S4 SR numerics, which states each case with its dates (move 10). |

Sentences changed but above 0.5 (for the record): the 8–85 lag sentence (S4 QS numerics, verbatim); the delay formula and the gradual-selection mechanism (S4 `capdyn`); the lump-sum exponent (S4 proof (3)); the forms of each direction (S4 new subsection); the Scope sentences of `corrrate` and `slowroute`, compressed to two or three sentences each with every condition kept; the cooperative-system sentence (kept, with "(Hirsch 1985; S4)").

**Supplement** (snapshot `supp/04_S4.md`): 142 sentences, 0 below 0.5. The one sentence removed from S4 is the duplicate listed in §3.

## 5. Assembly and numbers

- `python3 src/assemble_v62.py` in the scratch copy: "no problems"; 95 core and 33 supplement declarations; §4 = 4,246 words.
- No mathematics changed. No number changed; numbers moved keep their check-block labels (FF, QS, DW, SR, AC, CS).
- Every key, every claim tag, every `{{…}}` citation of this unit's keys from other files still resolves to the same kind and part number (`corrrate`(1)–(4), `humancorr`(1)–(2), `certificate`(1)–(4) unchanged in structure).
- Ren's lines kept verbatim with their keys: 被选择的，开始选择选择者 [corpus: meta-attractor]; "growing understanding without executive authority may change nothing" (§4.3, the one home; §12.2 already points to it); the line-363 repair paragraph; the hand-off sentence.
- Standing rules checked: no named states or firms; E2/E3 not touched; "keep pace", "per-unit cost floor", "selected level", "masked", "certified" as plan §8 fixes them. The box keeps the one "can" ("can be kept by those who buy it"), an existence statement (merge notes §4.8); "can raise $d$" in the countervail sentence is likewise existence, and I restored it after briefly writing "raises".

## 6. Scope paragraphs after the pass

`influence` 2 sentences; `corrrate` 3; `humancorr` 3; `certificate` 1; `pausefield` 3; `slowroute` 3. Each states what the result does not cover and what would make it fail; the numbers that illustrate it are in S4, except `pausefield`'s one pair (0.68, rising toward one), which the argument needs to show that the dependence on rule-making speed is large.

## 7. The interrupted attempt

Its moves 1, 3–10 above were sound and are kept. One reversed: it had moved "what a claim of the loop must show" (the four-step chain) and the contraction mechanism to S4 as a paragraph. The four steps are the evidentiary standard a reader of the core needs for any claim of capture, so they stay in the core (tightened); only the contraction mechanism moves. Its S4 subsection title changed accordingly, and the paragraph that duplicated the core's chain was removed. It had also dropped "almost all trajectories converge to equilibria" from the cooperative-system sentence, leaving "so it describes lock-in" without its reason; restored.

## 8. Open issues for the integration editor

1. The box is about 170 English words (205 by the assembler's rule), above the 90–140 guide: five results, each with its antecedent and tag. Cutting further means dropping an antecedent or a result from the box.
2. The claim box's Why and §4.2's first sentence both list the means of conversion (fund evaluators, author benchmarks and standards / drafting standards, building evaluation tooling, authoring benchmarks, funding evaluators). They have different jobs (the observed mechanism; the operational definition Test B uses), so both were kept; if one must go, §4.2's list is the one with a companion (TESTS, Test B).
3. S4's new opening subsection cites `{{blind}}`(2) from the Supplement; it resolves ("Lemma 3.3"), as other S-chapters cite core results.
4. The merge notes' open issues (refs for Goldowsky-Dill, van der Weij, Greenblatt ×4 and Grossman–Helpman; the QS block comment; S13's row and $F(U,\dots)$ rename; TESTS Study 2's signature; CLAIMS provenances) are untouched by this pass and still stand.
5. S4 grew by 170 words (4,857 → 5,027), all received from the core.
