# U05 elegance pass, editor B: Section 5 (`core/50_s5.md`) and S5 (`supp/05_S5.md`)

4 October 2026. Started from the current `src/` files, which are identical to `planning/snapshots/draftA/src/`. This directory already held an interrupted earlier attempt (core about 4,816 raw words, S5 with `frontier` moved). I read it, kept two of its choices (`frontier` to S-numbering; the full example of `enforce`(5) in S5), and redid the core from the source. Both files here replace that attempt. No discussion chapter belongs to this unit. Nothing in `src/` was edited.

## 1. Word counts

| | Merged (draftA) | This pass | Change |
|---|---|---|---|
| Core §5, assembler count | 5,579 | **4,768** | −811 (−14.5%) |
| Core `50_s5.md`, raw words | 5,516 | 4,710 | −806 |
| Claim box (Claim + Why) | 306 | 181 | −125 |
| §5.1 / §5.2 / §5.3 / §5.4 / §5.5 (raw) | 583 / 1,830 / 1,258 / 645 / 865 | 552 / 1,507 / 1,220 / 591 / 659 | |
| S5 `05_S5.md`, raw words | 6,304 | 6,390 | +86 |

**Deviation from the target of about 3,700.** The core is about 1,070 words over the target, and I could not close that gap without breaking a rule of the brief. What the extra words carry:
- **Result statements kept whole: 1,814 words**, plus the conditions written into the inline sentences for `join`, `preventattack`, `nonsum` and `freeze`. Every core result of §5 except `frontier` is cited by Parts II–IV or sits on the spine: `dissipate` (§7, §10), `enforce` (§6–§12), `detectlink` (§7–§12), `relpunish` (§7), `restraint`, `wingives`, `racehazard` (§7), `tempo`, `coverage`, `enough`, `talk` and `scissors`. Plan §2 therefore keeps each with its full statement. From inside the statements I moved only illustrations and explanatory clauses (see §2).
- **Definitions that later sections cite by name: about 650 words.** These are the three race premises and $R,T,P,S$ (§7.2's branches), the repeated-game setup, the race channel, the four conditions (legible, overrulable, exercised, resourced) and the three premises of the growth channel (§9 and §12.1 cite them), and E2/E3 (§11.3, §12).
- **Ren's lines and the sharpened rule: about 330 words.** This covers the frontier lines [corpus: meta-attractor], "growth is not the danger; the mind is", 癌亦增长 and the rule's boundary, all verbatim with their keys.

Scope paragraphs now total 520 words across twelve results, most of them two or three sentences.

## 2. Moved from the core (with where it now lives)

1. **`frontier`, the whole Remark.** It moved to S5 as **Remark S5.1**, under the heading "The frontier switch", with its title "what cancer does when the body runs out" and a one-line headline in words before the symbols. No part of II–IV cites it; only CLAIMS, LEDGER and S14 do, and S14's "Remark {{#frontier}}" now prints "Remark S5.1". In the core, one sentence carries its conditions: frontier or destruction available; relative accounting; the switch condition (net marginal value against the net gain in standing); a wider objective stopping at a point of enough; the bound below zero set by private cost against the capacity destroyed. It keeps the cancer image and the [thm; num: FS] tags and points to the toy and the counter-finding. Ren's frontier lines follow it unchanged.
2. **The example of `enforce`(5)** ($C=1$, $P=0$, $D=4$, $V^{\rm sub}=0$, $g=2$, $\delta=0.9$; window $(0.0354,0.0556)$; $v=0.895$ at $q_b=0.045$). It is now a paragraph, "*The example of (5).*", after the proof of `enforce` in S5, with every parameter given. The statement keeps the existence claim with "(S5 gives an example) [num: ES]".
3. **`enforce` Scope: the valuation-check sentence and the 19,965-setting best-response figure** went to S5's Numerics, which already has them in its "Valuation check" and "Best response over plans" bullets. The core keeps the failure condition: where quitting the race pays the punisher, part (5) does not give the credible punishment value.
4. **The folk-theorem paragraph's numerical pair** ($C=3$, $D=6$, $v=1$, deviations X and Y) is in S5's "Per deviation" bullet. The core keeps the point (the quiet deviation is the kind that masking hides) with "S5 gives a pair".
5. **`detectlink`, the memoryless-clock sentence** ($p_d=e^{-T_{\rm dec}/\tau_{\rm det}}$) is in S5's derivation and its check of the clock.
6. **`detectlink`, the explicit payoff mapping** ($R=C_i$, $T=\dots$, $P-F=\dots$) is in S5 under "The correspondence with {{assure}}". The statement keeps the condition in words: "the payoffs of {{assure}} read as the continuation values of cooperation, of a deviation that becomes decisive and of one detected and answered". It also keeps the threshold identity and the $T<R \Leftrightarrow \bar p>1$ case.
7. **`detectlink` Scope, second half** ("the decisive position carrying its own stakes") is in S5 under "Where they differ". The core Scope is now one sentence plus "S5 gives the reading of the payoffs and where the two differ".
8. **`relpunish` Scope numbers** (δ ≥ 0.706, strictness under each perturbation scheme, "nearly every game tried", both punishers preferring the same role, indifference) are in S5's counterexample, Strictness and Indifference paragraphs. The core Scope keeps the conditions: an exchangeable lottery is covered; a label-carrying continuation escapes [num: ES]; with $n\ge3$, role punishers escape, and their punishment is weak as printed, strict under small perturbations, with roles as equilibrium selection [num: CR].
9. **`restraint` Scope counterexample** ($D=0.9$, $\bar p=0.864$) is in S5's proof of `restraint`. The core keeps the conclusion, "does not by itself exempt (S5) [num: ES]".
10. **`enough` Scope numbers** (PE: 0.717; $1.8\times10^{-9}$) are in S5's proof of `enough`. The core says "with a growth-channel example [num: PE]". The clause "because the success function is homogeneous of degree zero" left the statement as proof; it is in S5's proof of `enough`.
11. **`talk`.** The Scope's quadratic third-party robustness is in S5, proof (2), which the core now cites. The clause "What it does to third parties then enters both objectives alike" is proof and is in S5, proof (1). The fading clause in (2) was dropped because the headline carries it.
12. **`scissors` Scope numbers** went to S5. The binary-game figures (0.924, 0.387, 0.9495) are in S5's reduced form, and the joint-model figures (0.551 and 0.542, period 31.8, 12 of 96) are in Remark S5.3 (`jointscissors`). The core keeps the [num: JX] finding in words: the blades cross as the stakes outgrow fixed provision, the objective blade does most of the closing, and neither moves where provision keeps pace. It adds that S5 gives the binary-game figures and where Test G discriminates.
13. **`scissors` arm 2's formula clause** ("by {{eq:twochaneq}} … $C_i-v_i=(1+\theta)(\bar\pi_C-\bar\pi_P)$") is in S5's proof of arm 2. The mechanism stays in words: "since it raises the deviation's gain in objectives and shrinks the sanction that remains". "In one channel $\Gamma_\delta$ is proportional to $\omega$" left arm 2 because the pivot paragraph, part of the same statement, states it for both $\Gamma$ and $\Gamma_\delta$.

## 3. Removed as true duplicates (and where the point lives)

- **The Test G paragraph of §5.5** duplicates §7.4's Test G entry (registered wording, nearly verbatim) and S5's "*Test G*" paragraph. §7.4's "(Section 5.5)" still resolves, because §5.5's Scope points to S5 for where Test G discriminates.
- **"Both sides of (14) are thereby tied to what can be measured …"** duplicates the `detectlink` statement (υ against $T_{\rm dec}$; the threshold rising with the value of winning) and `scissors` arm 1 (a loop gain above one shortens $T_{\rm dec}$).
- **"Both $T_{\rm dec}$ and υ are what masking hides … certified (Section 12.1)"** duplicates §12.1 tier 2, *Estimator* ("The time to a decisive position and the timeliness of detection are what masking hides … estimated by correctors whose row sums are certified (C2)"), which cites `detectlink` and `alarm`.
- **The Gao et al. 2023 clause** ("as optimizing a learned reward past a point lowers the quality it measured") duplicates §6.4 ("Reward hacking is Goodhart's law inside training (Gao et al. 2023)"). The Goodhart sentence stays, since X10 cites §5.4 for it.
- **"as nuclear advantage saturated at a secure second strike [obs]"** duplicates §7.2 ("Branch I′ is how nuclear rivalry stabilized once a survivable second strike was secure … [obs]"). The core now points to "(Section 7.2)".
- **"though the longest-horizon series is at the limit of its task suite"** duplicates §7.4 ("with the longest-horizon series at the limit of its instrument") and EVIDENCE EV5. The [obs: EV5] clause stays.
- **"Lowering decisiveness does not remove the problem if the prize is decisive power"** duplicates §10.2 ("Lowering decisiveness does not remove it, since a lottery can still award a position beyond sanction"). The core keeps the lottery reason and "what has to be limited is what winning confers … (Section 10.2)".
- **In the scissors Scope, "which in the contests computed exceeds the structural gain where a lead discourages the follower and can fall below it where a laggard tries harder"** duplicates §2's `loopgain` Scope and S2's `eqgain`. It is replaced by "which the structural gain does not bound in either direction ({{eqgain}})", §2's own conclusion.
- **The box's glosses of the three means** ("which makes restraint pay through the future", "which makes costs return in time", "which lets the parties see the same danger and believe one another") each open their subsection (§5.2, §5.3, §5.4).
- **"Restraint is enforceable iff $p_d\le\bar p_d$, deviation by deviation"** (first sentence of §5.5) restated `enforce`(2).
- **"…, which is not the same thing"** (after "permanent superiority") is a restatement; S5's `freeze` says why.

## 4. Merged or rewritten within the core (nothing lost)

- **Box.** It is now organized by the three erosions (*Enforcement*, *Correction*, *Shared understanding*), each with its antecedents and tags, plus the C0 sentence. The pivot is carried by one subject: the won share raises the chance where leads compound and narrows the objectives where relative return exceeds common return. The sanction and stakes arms are in the `scissors` headline. "In one reduced model the blades close together [num]" is in §5.5's Scope. "A factor that falls toward one" is in the `talk` headline. "Each erosion feeds the others", with its two concrete links, opens §5.5. "So nothing in it stops growth where need is met" is carried by §5.3's sharpened rule ("decides whether growth stops where need is met").
- **§5.1's κ paragraph and the race-premises paragraph** are kept and tightened. The `join` conditions are unchanged.
- **The folk-theorem paragraph** is now one sentence.
- **After `relpunish`**, two sentences became one: "punishments that break the symmetry [thm]; blocs [conj]". The two ways symmetry breaks are named in the Scope just above.
- **The `wingives` paragraph** folds the AI/C13 sentence into one clause, keeping "whether AI lowers it … is crux C13" and the §8.3 pointer.
- **The §5.3 intro, the growth-channel motivation and the §5.4 last paragraph** are tightened. The last paragraph now says "carried by what its receivers can check without trusting the sender (Section 11.2)", since §11.2 lists the carriers.
- **The §5.5 lead** opens with the interlock; the closing paragraph is tightened. The bold line, "temptation up and restraint down at once" (conditioned on stakes outgrowing provision), trees and "durable cooperation …" are all kept.

## 5. Preservation check: adjudication

Command (scratch copy `/private/tmp/claude-501/u05b-test`):
`python3 src/sentcheck.py <draftA>/src/core/50_s5.md src/core/50_s5.md src/supp/05_S5.md <all other current core/supp/disc files> --min 0.5`
Result: **181 sentences checked; 15 below 0.5.** Each is accounted for here:

| # | Old sentence (start) | Disposition |
|---|---|---|
| 1 | "The first two arms turn on one pivot, the won share, and in one reduced model the blades close together [num]." | Merged. The pivot is in the box's enforcement sentence and the `scissors` pivot; the reduced model is in §5.5's Scope [num: JX] |
| 2 | "A valuation check confirms the algebra of part (1) [identity: EC]." | Moved; S5 Numerics, "Valuation check" (already there) |
| 3 | "Which deviation binds depends on both terms … $C_i=3$ …" | Moved; S5 Numerics, "Per deviation". The core points to it ("S5 gives a pair") |
| 4 | "The verification threshold compares cooperating with defecting … carrying its own stakes." | Merged into the shorter `detectlink` Scope; the rest is in S5, "Where they differ" |
| 5 | "Both $T_{\rm dec}$ and υ are what masking hides … certified (Section 12.1)." | Duplicate of §12.1 tier 2, *Estimator* |
| 6 | "With $n\ge3$, punishers in different roles can hold a relative deviator below zero." | Merged into the `relpunish` Scope ("so, with $n\ge3$, do punishers in different roles"); S5 has the deviator held at −0.5 |
| 7 | "In a three-player example … 0.706; weak as printed … strict …" | Moved to S5's counterexample and Strictness. The core Scope keeps "weak as printed and strict under small perturbations" |
| 8 | "Both punishers prefer the same role, and a purely relative punisher is indifferent …" | Moved to S5, Indifference. The core keeps "which punisher takes which role is a problem of equilibrium selection" |
| 9 | "AI can substitute for the work and the assent of the governed …" | Merged: "whether AI lowers it, by substituting for their work and assent, is crux C13, and Section 8.3 meets the benign winner at its strongest" |
| 10 | "Capability growth is measured, though the longest-horizon series …" | Merged into a clause (keeps [obs: EV5]); the qualifier duplicates §7.4 |
| 11 | "PE: frozen at need, survival … 0.717 … $1.8\times10^{-9}$" | Moved to S5's proof of `enough` (already there) |
| 12 | "This subsection gives that line its content in information, by asking what relative accounting does to talk." | Kept, shortened (the "by asking" clause restated) |
| 13 | "**Measures** … (Gao et al. 2023)" | Goodhart kept; the Gao clause duplicates §6.4 |
| 14 | "In the binary game of {{zonesillus}} … 0.924 … 0.387 … 0.9495" | Moved to S5's reduced form (already there); pointed to from §5.5's Scope |
| 15 | "The arms also fix where Test G discriminates." | Duplicate (Test G paragraph): §7.4 and S5's Test G; pointed to from §5.5's Scope |

The same check run against the new core alone (`--min 0.6`) lists 39 old sentences not retained in the core. The 24 not in the table above are moves into S5 or merges already described in §§2–4: the box sentences; the `frontier` Remark; the `enforce`(5) example; the 19,965 settings; the memoryless clock; the payoff mapping; the "Both sides …" sentence; the old relpunish consequence; the Lowering-decisiveness sentence; the `talk`(1)–(2) clauses; Snidal (kept, reworded); the §5.4 carriers sentence; the old §5.5 lead; the loop-gain clause; the joint-model figures; and the Test G wording.

**S5:** `sentcheck` of draftA's `05_S5.md` against the new files gives **190 sentences checked; 0 below 0.5**. The only existing S5 sentences I rewrote are the old "*In the example, …*" sentence (expanded into "*The example of (5)*") and the old heading "Remark {{#frontier}} in full", now the declaration. The six sentences between 0.64 and 0.89 against S5 alone are unchanged apart from tokenization at those edits.

## 6. Verification

- **Test assembly** in `/private/tmp/claude-501/u05b-test` (a copy of v6.2 with these two files in `src/`): **no problems**. There are 94 core declarations (one fewer: `frontier`) and 34 supplement declarations (one more). New numbering: core `join` 5.1, `dissipate` 5.2, `enforce` 5.3, `detectlink` 5.4, `relpunish` 5.5, `restraint` 5.6, `wingives` 5.7, `preventattack` 5.8, `racehazard` 5.9, `nonsum` 5.10, `tempo` 5.11, `coverage` 5.12, `freeze` 5.13, `enough` 5.14, `talk` 5.15, `scissors` 5.16. In S5: `frontier` S5.1, `zonesillus` S5.2, `jointscissors` S5.3.
- **`xref_v62.py`** in the scratch copy: citation coverage passes for THEORY (119/119) and SUPPLEMENT (74/74); must-stay items are 32/32 ("growth is not the danger; the mind is" and "They are different arrangements" are both in §5); no named states or firms. The only failures are the guide items 1 and 9, which predate this pass and belong to front matter not yet rewritten.
- **Keys, tags, equations.** All keys are kept. `frontier` is now S-numbered, and its citations in CLAIMS, LEDGER and S14 render correctly. Every claim tag is kept. `{{eq:twochaneq}}`, `{{alarm}}` and `{{tdec}}` lost one core citation each; `tdec` is still cited in arm 1. No mathematics changed, and I found no mathematical error. One wording restoration: "(variety grows) … can fail" stays "can fail", not "fails", because exponential coverage need not outpace exponential variety.
- **Fidelity.** These are unchanged and verbatim with their keys:
  - the frontier lines ("peace of abundance … carries the same switch with it" [corpus: meta-attractor]);
  - "**growth is not the danger; the mind is**" [corpus: meta-attractor; Ren, 2026-09-25];
  - 癌亦增长，而其长竭母体之生 with its gloss [corpus: shengsheng, 2026-07-14];
  - the narratives sentence [corpus: selfishness-spiral];
  - the Ψ2 quotation.

  The 讲理/讲赢 line stays at its one home in §3.8, referred to from §5.4. The vocabulary of plan §8 is kept: structural/equilibrium gain, working objective, relative/common return, provision beneath the game, "keep pace", and E2 stopping ≠ E3 slowing.

## 7. Open issues for the integration editor

1. **Plan conflict on `frontier`.** Plan §4 says "`frontier` reduced to two sentences". I read the task's side-result rule as allowing an S-number, since no part of II–IV cites it. The core keeps two sentences carrying its conditions, with the cancer image and Ren's lines. If the integration pass prefers a core-numbered Remark, put back the declaration `**{{!Remark:frontier}} (The frontier switch: what cancer does when the body runs out) [thm].**` before the two sentences and drop the S5 declaration, leaving the S5 heading "Remark {{#frontier}} in full". CHANGELOG should record the move either way.
2. **Length.** See §1. Further cuts would have to come from statements that Parts II–IV cite (a plan §2 decision), or from the narratives paragraph of §5.4, whose lineage would belong in X1. That paragraph is the home §7.1, §7.4, §11.2 and X10 point to.
3. **§7.4's Test G** points to "(Section 5.5)". It still resolves through §5.5's Scope pointer, but "(Section 5.5; S5)" would be more direct. This edit belongs to the §7 unit.
4. **Carried over from the U05 merge notes, still open:**
   - §1.2(4) says "forms blocs" (plan: $n/(n-2)$, blocs [conj]);
   - S13's row should read $p_d=1-\upsilon(T_{\rm dec})$;
   - §8.3(g) should refer back to `detectlink`;
   - S14's `enforce`(5) row should cite the $P<v<C$ example;
   - the CHANGELOG renames.
5. **Numbering.** Core §5 results shift by one from `enforce` onward (`frontier` left), and the S5 remarks shift by one (`frontier` became S5.1). Everything is keyed; LEDGER's automatic crosswalk will show it.
