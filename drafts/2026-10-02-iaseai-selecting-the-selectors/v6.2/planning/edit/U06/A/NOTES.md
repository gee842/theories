# U06 elegance pass, editor A: Section 6 (core `60_s6.md`) and S6 (`06_S6.md`)

4 October 2026. I started from the current `src/` files of this unit. Both were byte-identical to `planning/snapshots/draftA/src/` when I began and when I finished. The directory held no earlier attempt.

I read:
- V6.2-PLAN (§1, §2, §4 §6, §5, §8);
- merge notes U06;
- D1-opus §1.4, §3.3 §6 and §7;
- V6.1's §6, for comparison;
- every passage elsewhere in `src/` that cites a §6 key or a "Section 6.x";
- §5.3, §7.1, §9 (as merged by U09 during this pass), §11.3, §12.3, §12.4, X1, X8, X11, S4, S9 and EV6.

Files written (only these three):
- `planning/edit/U06/A/core/60_s6.md`
- `planning/edit/U06/A/supp/06_S6.md`
- `planning/edit/U06/A/NOTES.md`

The mathematics is unchanged. Every declaration is unchanged and in the same order, so numbering does not change: 6.1 `faithful` to 6.9 `topology`, and S6.1 `nearlock` to S6.5 `lyapunov`. Every key and every claim tag survives (§4). Every Ren line is verbatim with its corpus key. No statement lost a premise.

## 1. Word counts

| | Snapshot (draftA) | Edited | Change |
|---|---|---|---|
| §6, assembler count (rendered) | 6,015 | **5,642** | −373 (−6.2%) |
| `60_s6.md`, assembler rule on source | 5,873 | 5,498 | −375 |
| `60_s6.md`, `wc -w` | 5,853 | 5,481 | −372 |
| claim box (Claim + Why) | 280 | 226 | −54 |
| by subsection (source): head+box / 6.1 / 6.2 / 6.3 / 6.4 / 6.5 / 6.6 | 285 / 233 / 346 / 1,265 / 1,938 / 759 / 1,047 | 231 / 209 / 346 / 1,154 / 1,832 / 716 / 1,010 | |
| `06_S6.md`, assembler rule | 4,070 | 4,378 | +308 |
| `06_S6.md`, `wc -w` | 3,974 | 4,280 | +306 |

**On the target (about 3,800).** The section lands at 5,642, about 1,840 above the guide. I stopped there on purpose. Here is what the extra words carry:

1. **Statements, Scopes and the model setup: about 1,440 words that cannot move.** Nine core results are all cited by Parts II–IV or stand on the spine:
   - `faithful` (§8, X8);
   - `delegate` (Table 7.1, §7.2 branches, S7);
   - `lockin` (§4, §9, §11, §12);
   - `delegatelock` (§7, §9–§12);
   - `retain` (§7, §8, §9);
   - `nested` (§7–§10);
   - `masked` (spine item 5, cited from §5 to §12);
   - `topology` (§8–§12);
   - `transmit`, an inline Remark that costs no words.

   By plan §2 each keeps its full statement with every premise. The five side results are already S-numbered, each with one core sentence that carries its conditions.
2. **The alignment layer the plan and D1-opus E1–E8 require: about 1,600 words of prose.** None of it was in V6.1:
   - the masked admission recommendation, with C12 and E2/E3;
   - the tax not fixed, with two fates and the speed tax;
   - the two joints, with `humancorr`, hidden loyalties, the audits [rec] that §12 cites, and C13;
   - internal deployment (Stix), which §9 cites;
   - made minds, where §5.3 now points;
   - the two kinds of independence, the same-lineage common cause and budgets per topology;
   - the inner level (Ali I8);
   - floor, not objective;
   - N4 with the 同行者 line;
   - broad E1 in Ren's words, with its mechanism before the line.
3. **Ren's lines and their mechanisms: about 140 English words.** These are the 45:06 question, the 至善 passage and line, the broad-E1 line, "all beings" and "growth is not the danger; the mind is". The Chinese text does not count.

V6.1's §6 was 2,882 words. The statements grew by about 600 once their premises were written back in, and the additions in item 2 come to about 1,600. That gives about 5,100 before the Ren lines and the S-sentences. A cut to 3,800 would mean dropping plan-mandated points or thinning statements, which was V6.1's error. Every other paragraph was rewritten for one home per point (§2, §3). I judge about 5,600 to be this unit's frontier under the plan. §6 below lists what could still go if the integration pass wants §6 shorter, and what each cut would cost.

**Claim box: 226 words** against the brief's 90–140. It states five results and the conjecture, each sentence with its antecedent and tag. Three sentences left the box, and all three are kept elsewhere (§2, M1–M3). What remains could not lose a clause without losing an antecedent:
- instrument (two antecedents);
- weak incarnation;
- masked [thm∣prem] with its [rec];
- strong incarnation [def];
- [conj];
- Why: [obs], [thm∣prem] and [thm].

## 2. Moves (core → S6 or elsewhere), with the pointer left in the core

| # | What left the core | Where it now lives | Pointer in the core |
|---|---|---|---|
| M1 | Box: "the systems used to build AI are deployed first inside their developers, before any admission at release [obs]" | §6.4 Strong incarnation, Stix sentence, which now carries the [obs] tag; §9 cites it there | — (same section) |
| M2 | Box Why: "humanity has at present no mechanism that binds every capable developer under independent verification [obs]" | §6.4, after the bold conclusion of the three classes: "At present no mechanism binds every capable developer under independent verification [obs]" | — |
| M3 | Box Why: "aligning it to an institution is not aligning it to the people the institution serves [def]" | §6.3 *Us* joint, which now carries the [def] tag | — |
| M4 | §6.3: the 0.52 example ("a lone delegator would win against two rivals with probability about 0.52") | S6, Numerics of `delegate`, already there (s*=1.1628, 0.5196, "far from decisive … the sense of 'well below decisive capability' in Section 6.3") | "Delegation pressure arrives well below decisive capability (S6 gives an example) [num: AL(6.2)]" |
| M5 | §6.3 `homeostasis` sentence: "and it rises as that hazard falls" | S6, `homeostasis` Numerics (1), now explicit: "so on the interior branch it rises as the hazard per unit of delegation falls" | `{{homeostasis}}` |
| M6 | §6.4 Weak incarnation: "In some environments optimal policies seek power for most reward functions (Turner et al. 2021), as do decision-makers that are not optimal but can be retargeted (Turner and Tadepalli 2022); trained policies can pursue misgeneralized goals (Langosco et al. 2022)." | S6, new section "The tendencies of weak incarnation (Section 6.4)", verbatim | "S6 gives the formal results on power-seeking and misgeneralization". Turner et al. 2021 is still cited in the core (made minds). The Gao and tampering sentence stays in the core: it names the selected rewriting its selector, the paper's own mechanism, and U05 removed its Gao clause from §5 because §6.4 holds it |
| M7 | §6.4: "a learned reward is identified only up to a constant for each context" | S6 "Relative selection inside training", already there ("identified up to an additive constant for each context, and whether to act at all is not in it") | "(S6) [num: AL(BT)]" |
| M8 | §6.4 masked: "since a capability shown under evaluation is only a lower bound, which sandbagging lowers"; the long form of "propensity … cannot prove it absent" | S6 "The formal part of `masked`", already there ("A capability evaluation gives a lower bound … sandbagging lowers it"; "it cannot show one absent") | The core keeps both points in short form, with "(S6)" |
| M9 | §6.4 worked instance: "and of roughly equal incidence across architectures if it is not to re-sort them"; "At the current frontier reinforcement learning has not materially lowered monitorability (Guan et al. 2025), so the instance is conditional" | S6, new section "A worked instance: legible reasoning (Section 6.4)". It holds the whole instance, with the EV6 reading of Guan that merge note §2(b) adopted: a positive tax paid in compute | The core keeps both conditions (detectable evasion; a capability gap of zero or below) and "Present evidence leaves the instance conditional (S6)" |
| M10 | §6.5: "six checks of catch probability 0.9 catch only $(1-\rho_{\rm cc})(1-0.1^6)$ of hazards that strike at random [num: SM(7)]" | S6 `topology` Numerics. The formula is now stated there with its SM(7) figures, and the wording follows `checks_v62.py` SM(7) | "(S6)". S14's row cites Proposition `topology`, not this sentence |
| M11 | §6.5: "as pricing algorithms learn to in simulated markets (Calvano et al. 2020; Fish, Gonczarowski and Shorrer 2024)" | S6 `topology` Numerics, in the common-causes list | The point and its consequence stay: "Systems of one lineage serving rival principals can also coordinate around them (S6), a second reason for evaluators of independent lineage" |
| M12 | §6.5 budget figures: 36 layer-checks catch 0.989; 18 catch 0.994 | S6 `topology` Numerics, already there | "Budgets differ by topology: in the example of S6, checks at every layer catch more than checks across the gap with half the layer-checks [num: SM(13)]". The plan's "budgets per topology" keeps a core clause |
| M13 | §6.4 made minds: the figures behind "intensity bounded as private cost falls" | S6 `boundedopt`, already there (0.25 → 250 under θ=−1; 0.144 → 0.623 under θ=0) | "(S6) [num: AL(contest)]" |

## 3. Duplicates removed (only true duplicates; where each point lives)

| # | Removed from the core | Lives at |
|---|---|---|
| D1 | §6.1 "each system serving its principal faithfully" (after *principal alignment*) | The preceding sentence's grant: truthful, follows the principal, no goal of its own |
| D2 | §6.1 "what is added is the mechanism by which the game reproduces itself and its correctors (X1)" | X1 ¶ on Critch and Krueger: "What is added is the mechanism by which the game reproduces itself and its correctors". The core keeps "This follows from the multiplicity thesis of Critch and Krueger (2020)" (V6.1's "follows from") and "X1 says what the paper adds to it" |
| D3 | §6.3 q_L: "in two cases … so that once delegated it cannot be overruled in time" | X11 ¶ on `nearlock` ("cannot be overruled in time once it is delegated") and S6's q_L event. The core keeps both cases |
| D4 | §6.3 narrow E1: "therefore needs no trust among actors who price in the lock" | The lead of `delegatelock`, two paragraphs earlier |
| D5 | §6.3 narrow E1: "AI kept out of strategic and escalatory decisions that are irreversible within the time available for deliberation (Section 11.3)" | §11.3 E1 narrow form, the home of E1 by D1-opus §7.1. The core keeps the irreversibility case in the q_L paragraph and the pointer to §11.3 |
| D6 | §6.3 narrow E1: "Where the lock is uncertain, as in tactical domains with a large speed advantage, delegation can be an equilibrium (parts (2) and (3)), and keeping AI out needs a commitment held in common" | §11.3 E1, near verbatim ("Where the lock is uncertain, as in tactical domains with a large speed advantage, delegation can be an equilibrium too ({{delegatelock}}(2), (3)), and keeping AI out rests on a commitment held in common"), and X11. The core keeps "The scope of narrow E1 is thus set by $q_L$, not by a list" |
| D7 | §6.3 joints: "The same dependence couples a winner to the governed after victory, and so decides how much an accurate winner gives them ({{wingives}}); whether AI lowers it is crux C13 (Section 12.3)" | §5 `wingives` ¶ ("What the race cannot verify beforehand is $\kappa_W$ after victory … whether AI lowers it … is crux C13 (Section 12.3)") and §12.3's C13 row. The core keeps one clause: "The same dependence decides how much an accurate winner gives the governed after victory ({{wingives}}; crux C13, Section 12.3)" |
| D8 | §6.6 opening: "its effects cross every boundary of those who decide about it" | V1 in §1 ("Its effects and dependencies cross the boundaries of those who decide about it"). The sentence now reads exactly as §12.4's: "AI is a planetary technology, for all, not a means for one side to grow bigger at the others' expense (V1)" |
| D9 | §6.6 outer level: "with certified row sums, measured correlation of misses and adversarial control evaluations"; "since what lowers the tax is a public good" | §6.5's two independence paragraphs and the row-sum sentence; §6.4's tax paragraph. The list now reads "whose independence is certified and measured ({{topology}})" and "({{onegroup}})" |
| D10 | Within-paragraph restatements merged: "For a single optimizer a bounded objective is not enough" (into the next sentence); the two §6.1 advisor sentences (into one); the countermeasures list (now one sentence, with every countermeasure kept) | — |

## 4. Preservation check

The checks ran in a fresh scratch copy of the current `v6.2` (`/private/tmp/claude-501/u06A/fresh/v6.2`), with U09's merged §9 included and my two files put into its `src/`.

**Assembly.** `python3 src/assemble_v62.py`: **no problems**; 95 core declarations and 33 supplement declarations, as before; §6 = 5,642.

**Keys and tags.** Counted against the snapshot. No key is lost in either file. The core gains `{{nested}}` (outer level) and `{{onegroup}}` (outer level, replacing a restated reason); S6 gains `{{masked}}` and `{{nested}}` (new sections). One tag leaves the core: `[num: SM(7)]`. It moved with its number to S6 (M10), and the `topology` Proof line still cites SM(7). Every [obs], [def] and [rec] is kept, with the moves M1–M3. Each Ren quotation and Chinese line, and each `[corpus: …]` key, was checked as a verbatim string: all present.

**Sentence check, core.** `python3 src/sentcheck.py <draftA>/src/core/60_s6.md src/core/60_s6.md src/supp/06_S6.md <all other current core/supp/disc files> --min 0.5`. It checked 177 sentences and listed **6 below 0.5**:

| Score | Sentence (start) | Disposition |
|---|---|---|
| 0.25 | "This is *principal alignment*, each system serving its principal faithfully." | Merged into "This is *principal alignment*; *purpose alignment*, …"; the clause is a restatement (D1) |
| 0.47 | "A truthful advisor can correct its principal's held self-model where that model draws the boundary inside the system ({{boundary}}(2))." | Merged with the next sentence: "A truthful advisor can correct a held self-model that draws the boundary inside the system ({{boundary}}(2)), but not the working objective …" |
| 0.39 | "Delegation pressure arrives well below decisive capability: in the example of S6 … 0.52 [num: …]" | Claim kept in the core; number moved to S6 (M4) |
| 0.37 | "It has to be stated in capability, not propensity, … only a lower bound, which sandbagging lowers (S6)." | Rewritten shorter in the core ("It is stated in capability, not in propensity, which an evaluation can show present but not absent, and capability is measured through compute, training data and elicitation by fine-tuning, since sandbagging lowers the capability shown (S6)"). The lower-bound reason is in S6 (M8) |
| 0.19 | "The topologies also differ in budget: … 0.989 … 0.994 [num: …]" | Comparison kept in the core; figures in S6 (M12) |
| 0.42 | "Sections 6.2–6.4 give the mechanisms by which it becomes the opposite." | Reworded: "Sections 6.2–6.4 show how it becomes the opposite." |

Ten more sentences fall between 0.5 and 0.7. Each is accounted for:
- the three box sentences (M1–M3);
- "*Us:* …" (reworded, [def] added);
- the C13 sentence (D7);
- the three made-minds sentences (merged; M13);
- the blind-spot sentence (M10);
- the countermeasures list (D10).

**Sentence check, S6.** The same command, with the snapshot's `supp/06_S6.md` as old. It checked 136 sentences and listed **1 below 0.5**: "HO of `../v5/checks_v5.py`, run by `checks_v62.py --legacy`]." This is a tool artefact. The splitter breaks the old sentence inside the bracket `[num: HO of …]`, while the pool strips the whole bracket as a tag. The text is unchanged and verbatim in S6 (string match checked).

**Rewritten S6 text.** Four changes:
- the intro sentence (extended);
- `homeostasis` Numerics (1) (one clause added);
- `topology` Numerics: the blind-spot sentence (formula added, figures unchanged) and the common-causes sentence (one sentence added).

Nothing was removed from S6.

**xref.** I ran `xref_v62.py` against a baseline copy. It reports only the expected citation shifts from M6, M9 and M11:
- the core's reference list keeps entries for works now cited only in S6 (Calvano 2020; Fish, Gonczarowski and Shorrer 2024; Turner and Tadepalli 2022; Langosco 2022; Guan 2025);
- S6 cites works not yet in the supplement's list.

After `python3 src/refs_v62.py` in the scratch copy, coverage is complete: THEORY 110/110, SUPPLEMENT 87/87, DISCUSSION 92/92. That rebuild also fixes the baseline's two missing supplement entries, Alchian 1950 and Rankin et al. 2007, which belong to other units. The guide-coverage failures are present at baseline, and no state or firm is named in core prose.

## 5. Other changes (judgment calls)

- **Narrow E1 in §6.3.** The paragraph is now the derivation only:
  - E1 is named, with a pointer to §11.3 as the arrangement;
  - "near certainty" is made exact by `nearlock`'s bound, the only place in the core that states the bound;
  - "scope set by $q_L$, not by a list" stays.

  The uncertain-lock and tactical-domain sentence lives in §11.3 and X11 (D6).
- **`homeostasis` core sentence.** It now carries, in one sentence, every condition of (1) together with (3) and (4): in degree, additive stakes, interior, far from saturation, saturation, summable, all-or-nothing.
- **§6.5 test of O2.** The pointer reads "decided by the test of O2 (Section 6.6)". It still keeps the designated-body condition and N3, because §6.6's test does not name N3.
- **"Hidden loyalties built into its systems"** is kept in full, so the specificity of Davidson et al. is not lost.
- **Worked instance in the core.** Both conditions are now antecedents ("Where it lets correctors catch … and opacity buys capability"). An earlier draft of mine had asserted the first one.
- **No change to `transmit`'s placement.** It is a side result that could take an S-number, but moving it saves no words: the core sentence stays. It would also renumber `nested`, `masked` and `topology`, whose V6.1 numbers the merge preserved.

## 6. Open issues for the integration editor

1. **Reference lists.** Rerun `src/refs_v62.py` after this unit is merged. It was verified in scratch to give full coverage. The works now cited only in S6 are listed in §4 (xref).
2. **§11.3 is now the only core home** of "where the lock is uncertain, as in tactical domains with a large speed advantage, delegation can be an equilibrium, and keeping AI out rests on a commitment held in common" (D6), and of the narrow-E1 domain wording (D5). The U11 elegance pass must keep both.
3. **EV6 points to "THEORY §6.4"** for "present evidence ties evaluation awareness more to capability and data". That sentence stays in §6.4 for this reason.
4. **Further cuts, if §6 must be shorter.** Each costs something:
   - the inner-level countermeasures list to S6 (about 35 words; loses concreteness for alignment readers);
   - the masked evidence citations to S6 (about 20; the [obs] would then rest on "(EV6; S6)");
   - the made-minds contest sentence to S6 (about 25; loses the falling-cost contrast, Ali I5's point);
   - the box down to Claim only (about 55; the Why would be lost);
   - the remaining Gao and tampering sentence to S6 (about 25; see M6 for why it stayed).

   I would not cut statements, Scopes, Ren lines, the two joints, the masked recommendation or the outer and inner levels.
5. **Carried from merge notes U06 §4**, outside these files:
   - Greenblatt 2024 key collision;
   - the symbol table renames ($h_d$, $\beta_h$, $k_c$, $p_\ell$, $p_{\rm cc}$, $h_0$, $h_{c,t}$, $\mathsf m$, $\mathsf A$, $\mathsf B$, plus the local symbols);
   - CLAIMS/LEDGER dispositions (`topology` "sufficient, not necessary"; new `masked`, `nearlock`, `boundedopt`; S-numbers of `homeostasis`, `opaquecorr`, `lyapunov`);
   - the D marks for Ren to confirm: the 45:06 rendering, the 至善 passage and line, the 同行者 rendering, the [val] O2 sentence, and the broad-E1 definition sentence;
   - porting `dl_nearlock.py` as DL(e) and the `homeostasis`(2) roots into a v6.2 block;
   - S14's `opaquecorr` row (summable example).

   Merge-notes items 2 and 3 (S7's `delegate`(2) citation; S5's $d$ → $h_d$) are already resolved in the current `src`.
6. **E3 wording.** §6.4 says "held to the pace at which control covers it (E3)"; §5.3 defines E3 as "developing at the pace of understanding". They are compatible (merge-notes item 12). I left the wording for the integration pass.
