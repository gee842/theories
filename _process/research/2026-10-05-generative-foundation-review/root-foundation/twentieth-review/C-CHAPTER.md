# Twentieth review, reviewer C: coherence and elegance of the canonical chapter

Read-only review of `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md` (abbreviated **CH**; line numbers are those of the file on main 121ff8042 as read on 19 October 2026, while R21 was editing nearby, so lines may shift by a few), with AGENTS.md, NONDUAL-METHOD.md, OPENING.md (flag only) and the zh edition (structure only). All measurements were taken by read-only scripts in my scratch directory (`scripts/C/measure.py`, `scripts/C/deps.py` (the folded copy of the chapter is not kept)). **V** marks a verified count or quotation; **J** marks a judgment of elegance, argued. Nineteenth-review findings (E1–E5, O1–O3, P1–P11, N1–N3, L1–L3) are not repeated.

## 1. Summary

1. **The chapter is a register, not an argument (major).** It has 1,967 lines, 738,669 bytes and about 99,000 words. It names 2,402 distinct backticked identifiers, and 1,698 of them appear only once. 59% of nonempty lines carry Lean names, and the body §1–§7 has 1,416 parenthesised Lean names. Sections §1–§3 cite study sections (§70–§214) much more than earlier sections of the chapter. The argument has no visible line: you cannot read section *n* as resting on section *n−1* (V counts; J reading).
2. **The order is inverted (major).** The foundation, "the whole and its parts" (premises carve parts, rest, openness, least loss), comes at the end of §1 (CH:325–361), after hexagram scholarship. The response and propagation dynamics that §3, §4 and §7 need sit in the middle of §2 (CH:526–550, 53 KB). §5 depends forward on §6.12, and §6.7 holds dynamics laws (CH:967–973).
3. **The theory is stated five or more times (major).** The places are the Status block, "stated in full" (11 items), §0, "stated whole", §9, the glossary (50% of its names already appear in §0–§7) and OPENING's footnotes. Measured overlap of names: §7.2 repeats §1–§6 completely (29/29), §6.15 95%, §6.10 74% of §2, "stated whole" 53%. One structure is proposed (C2).
4. **§6 can be five sections, not fifteen (major).** The old→new mapping is in table C3.
5. **Process history is mixed into the theory (major/moderate).** One table cell in §8.2 (CH:1359) is a 17.8 KB connectivity log with 50 receipt IDs. The chapter also has 62 receipts, 93 "October", 22 full dates in the body, 18 "is now / until the F3 sweep" palimpsests and 32 "Ren asked/wrote" narrations, which goes against AGENTS "live text gives the reason". About 25–30% of the bytes are process material or duplicate material.
6. **A reader-first chapter of about 1/3 the length is feasible (docs only).** It would put ten central results in front, and its outline is in §2.5. The zh edition lags in structure: its §8 is in the old form, it has no §8.6 (although it refers to it), it has no corpus crosswalk, and it keeps the catalogue inline.

## 2. Findings

### 2.1 Line of argument (question 1)

**Section dependency map (V, counted from section references and shared Lean names):**

| Section | Bytes | Depends on (as written) | Read as |
|---|---|---|---|
| §0 premise card CH:91–186 | 22.4 KB | none | the standing commitments |
| §1 Becoming CH:193–361 | 78 KB | §0, study sections only | readings → pairs → histories → no-premise laws → dependence → identity → 九句 → attraction → branching → junctures → onward → **6 hexagram paragraphs** → order of change → one-step → weighted histories → transmission → interleavings → **whole and parts (the foundation) last** |
| §2 Organization CH:363–553 | 112 KB | §0; "section 6.8" (forward); study sections | renewal, consumption, generation, evolution, finite stretches, verification, **feeding/feedback/reach (CH:512–524)**, **response/propagation/loops/frequency/remainder/routes/history sums/closing/thresholds/observation (CH:526–550)**, dormancy (CH:551) |
| §3 Knowing CH:556–723 | 80 KB | §2 (response), study sections | testing, experiment, mechanism, seeking/enough, **selection family (CH:614–633)**, learning/identification/learnable/parting/situations (CH:635–710) |
| §4 Collective CH:726–798 | 36 KB | §2, §5, §6.10, §7.2, §7.3 (forward) | markets list, meta-attractor, mutual dependence, the 8+1 constraints, V modules, SharedCodes, RuleCapture |
| §5 Evaluation CH:801–828 | 7 KB | §6.1, §6.7, §6.12 (forward) | routes of formation, comparison readings |
| §6 CH:833–1178 | 104 KB | §6 cites itself 60+ times (§6.8 ×12, §6.15 ×9, §6.13 ×9, §6.12 ×7, …) | see C3 |
| §7 Alignment CH:1200–1309 | 33 KB | §3 ×5, §6.15 ×6, §8.2 ×5, §4 ×3 | 明, pooled coupling, direction; 7.1–7.4 mostly re-cite §3 |
| §8–§11 CH:1311–1967 | 210 KB | — | programme, spine facts, glossary, history |

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C1 | major | CH:193–798 overall | The body is a catalogue of results, each "a case of" some law, and not one line of inference. A reader cannot tell which results carry the argument and which are instances. | V: 2,402 distinct backticked names, 1,698 used once. 844 of 1,439 nonempty lines (59%) contain backticks. In §1–§7, 421 of 742 paragraphs contain Lean names, with median paragraph 56 words, max 1,173, and 18 paragraphs over 400 words. 2,524 sentences, p90 43 words, 89 over 60 words. §1–§3 refer to 58 study sections/"Study:" links and almost no earlier chapter section. J: "case of a law" passages (for example the §1 endpoint list, the §3 periphery inquiry list, the §4 markets list) are inventories. | Each body section opens with its one law in words. It follows with at most 3–5 named theorems that carry the inference ("this is used in §n"). Everything else becomes "instances: see record X" or moves to REFERENCE. Rule: a Lean name appears in the prose only where the next sentence uses it. | docs only |
| C1a | major | CH:325–361 vs CH:193 | The foundational structure (premises carve parts; rest; openness; least loss; "the whole and its parts") is the *last* part of §1. Before it come 6 hexagram paragraphs (CH:297–319, 13.4 KB) and transmission/interleavings. | V: the headings in order are as in the map above. J: by the theory's own method (one unfolding, then how parts are carved), parts are carved before identity, attraction and junctures are read. | Move "whole and manifold / whole and its parts" to the opening of §1, right after the three readings of one change. Move the hexagram material to CHINESE-SOURCES-AND-BECOMING (or YI-ZHUAN) and leave a one-line pointer ("the 周易's six-place figures are runs of the core; see …"). | docs only |
| C1b | major | CH:526–550 (§2), CH:512–524 | The response/propagation/loops/frequency/remainder/routes/history-sums/closing/thresholds/observation line (53 KB, 7.2% of the chapter) is a theory of how difference travels. §3 (selection), §4 (pace, regulation) and §7 (pooled coupling) all rest on it, yet it sits inside "organization and renewal". Feeding/feedback/reach (CH:512–524) is restated in §6.9–§6.10. | V: §6.10 shares 74% of its Lean names with §2; §6.9 58%. §4 cites §6.10 for closures. J: closures and coupling are one structure (who reaches whom) and deserve one home. | New body section "Coupling and response": closures (feeding ⊂ influence ⊂ system; reach; coupling), counterfactual as a course, propagation, loops, frequency, remainder. It is placed before knowing. §6.9–§6.10 shrink to a reference to it. | docs only |
| C1c | moderate | CH:801–828 (§5), CH:967–973 (§6.7) | §5 "evaluation" depends forward on §6.12 and §6.1. §6.7, titled "restating from what wants its continuation", holds dynamics laws (fed from beyond, joint excess, relative position/race, Exclusion, Exhaustion; 9 KB) that need no condition. | V: references in §5 go to §6.12, §6.1 and §6.7. The laws in CH:967–973 have no `Unrestricted` hypothesis according to the text itself. | Merge §5 into the new §6.A (C3). Move the CH:967–973 laws to the "premises carve parts" section (fed from beyond, joint excess) and to the collective section (race, exclusion, exhaustion). | docs only |
| C1d | moderate | CH:614–633 (§3) vs §7.1–7.4 CH:1206–1270 | Selection through couplings (gap, reach, pool, pool response, rejoining) is stated in §3 with 8 sub-bullets and stated again in §7. | V: §7.2's Lean names are 100% (29/29) already in §1–§6; §7.1–7.4 75% (65/87); §7.3 68%. | State selection once, in the coupling/seeking section. §7 then gives only what alignment adds: 明 as the reading, pooled coupling as the joint form, the direction claim (7.5), and links back. Its size would drop from about 33 KB to about 10 KB. | docs only |

### 2.2 Repetition and one structure (question 2)

**Overlap measured (V).** The table gives the share of a section's Lean names already cited earlier in the chapter, plus phrase repeats:

| Statement layer | Where | Size | Names already earlier | Notes |
|---|---|---|---|---|
| In one sentence + Status + Scope + Two targets | CH:22–42 | 4.8 KB | — | Status already explains "instantiation / orders nothing" |
| The theory stated in full (items 1–11) | CH:43–89 | 16.7 KB | 52% (items vs. §0 and front) | a second summary |
| §0 premise card | CH:91–186 | 22.4 KB | 23% | the right home for commitments |
| The theory stated whole (I–IV, "deepest part", "what this completeness is") | CH:1180–1197 | 11.8 KB | 53% in §0–§6, 100% somewhere in body | a fourth summary |
| §9 formal spine | CH:1545–1613 | 15.0 KB | — | repeats the pure-core explanation a fifth time |
| §10 glossary | CH:1616–1821 | 69.3 KB | 50% (288/578) | many entries restate theorems (tally, change bound, coming to rest, census) |
| OPENING footnotes | OPENING.md | ~54 KB of ~54 KB file beyond body | — | sixth layer (flag only) |

Phrase repeats (V): "stricter than constructive" 5× (CH:27, 99, 1184, 1435, 1564). "step of invariance" 14×. "instantiation" 13×. "no/not a positive valence" 12×. "calling widening better" 6×. "not a field of" 6×. "shrink geometrically" 5×. `Web.significance_undetermined` 10×. `Law.perturbation_reabsorbed` 12×. `law_iff_em` 5×, "lemma of the decided law" 3×. "Feeding closure" 34×. "Living significance is the condition restricted to living claims" is said in Status (CH:~27), §0 E, §5, §6.8, §6.12 and §6.15, which makes 6 homes.

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C2 | major | CH:22–186, 1180–1197, 1545–1613, 1616–1821 | The theory is summarised four times before and after the body, and twice more in §9 and the glossary. Each layer adds detail, so none can be skipped, and a reader cannot tell which is canonical. | table above | **One structure, each thing said once:** (a) *Preface* (≤ 1 page): one sentence; the four kinds of standing (theorem without premise / theorem under stated premises / the condition / reading); where the ethics lies (one sentence each for condition, C, invariance). (b) *§0 premise card*: the **only** place that explains the pure core, "stricter than constructive", the representation commitments and the eight premises. Elsewhere one link. (c) *Body*, said once. (d) *Theorem map* (closing, one table): result in one line, standing, premises, section, record. It replaces "stated in full" **and** "stated whole". (e) *Glossary*: definitions only, one line each, no theorems. (f) §9: only facts about the Lean artefact (layers, how to check), with counts generated from the receipt. | docs only (plus a generator for the theorem map, optional) |
| C2a | moderate | CH:1184–1190 "The deepest part" | "Stated whole" raises the calibrations of classical logic (EM, WLPO, LPO, …) to "the sharpest results". AGENTS.md (Proof and naming) says a calibration of the logic alone is a lemma unless its record says what the need means for the unfolding. | V quotation at CH:~1188. J: this puts the logic, not the unfolding, at the summit. | In the theorem map, list each calibration under the law it calibrates, with its unfolding meaning ("settling is deciding whether a run changes again"). Drop "the deepest part" as a heading. | docs only |
| C2b | moderate | CH:1196 vs §9 CH:1547 vs §8.2 CH:1359 | The connectivity figures differ between sections: "195 of 7,698" (stated whole), "466 of 9,895" (§9), and the head measure is 495 of 11,647 (PREAMBLE, THEOREM-CONNECTIVITY.json). Nineteenth P1 covered §9 only. | V: the three text strings. | Give one number, at one place (§9), generated from the receipt. Other places link to it. | docs only |
| C2c | minor | CH:1616–1821 glossary | Glossary entries restate theorems with Lean names: 623 backtick spans in 10,312 words, and 21.4 backticks per 100 words in "Retired Lean names". | V | One-line definitions. Theorem content moves to the theorem map. "Retired labels / Retired Lean names" move to REFERENCE or history. | docs only |

### 2.3 §6 restructured (question 3)

**Current state (V).** §6 has 16 parts and about 104 KB: intro 2.7, 6.1 2.8, 6.2 1.4, 6.3 7.3, 6.4 1.3, 6.5 4.1, 6.6 0.8, 6.7 19.0, 6.8 10.8, 6.9 6.6, 6.10 9.2, 6.11 14.2, 6.12 8.0, 6.13 5.8, 6.14 2.9, 6.15 9.9 KB. It refers to itself more than 60 times. The zero-axiom generative space (§6.13), its cleanest part, comes *after* the conditional material. §6.15, the condition's home, restates §5–§6.14 (95% of its names are earlier).

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C3 | major | CH:833–1178 | §6 mixes three kinds of standing in an order set by history: zero-premise evaluation laws, conditional theorems, and readings/audits. The condition is described in 6.8, 6.11, 6.12 and 6.15. | sizes and self-references above. 6.7 contains "That reading was replaced…" narration. | Five sections, mapped below. Expected size is about 45–55 KB (half), with no result lost. | docs only; anchors kept as `<a id>` aliases |

**Old → new mapping:**

| New section | Content | From |
|---|---|---|
| **6.A Significance without condition** | significance is not settled by the dynamics (`Web.significance_undetermined`, once); what a characterization of living significance needs; minimality and rivals; readings of the connection; reasons; comparison and lifting | §5 (CH:801–828) entire; 6.1; 6.2; 6.3; 6.4; 6.5 |
| **6.B Widening and margins (no axiom)** | the generative space; margin laws (retains/loses/adds iff within/beyond margin); the four cases of a part (widens/narrows/keeps/mixed); regrouping as a remark | 6.13 (moved forward); the margin bullets of 6.8; the four cases from §2; 6.14 as a closing remark |
| **6.C Extent of the route (no condition)** | how far the feeding closure reaches, and the presupposition of a self, *stated by reference* to the new coupling section (C1b) | 6.9 and 6.10 reduced to about 1 KB of links. 6.7's dynamics (CH:967–973) go to the body (C1c). The non-conditional part of 6.11 (super/sub-truth boundaries) |
| **6.D The condition and what it yields** | `Unrestricted` stated; what it adds, exactly; the theorems as instantiations (one paragraph); the audit of uses as one sentence + record link | 6.15 as the base; the condition bullets of 6.8; 6.12 (audit) reduced to a link; 6.7's restatement narrative moved to history |
| **6.E Decomposition, and where ranking lies** | presupposition + step of invariance (A ⇔ P ∧ (P → A)); the condition orders nothing; C and invariance are where ranking enters; what it does not settle | 6.11 decomposition; 6.6 "what it does not do" as the closing paragraph |

J: 6.B before 6.D makes the elegant point visible in the structure: widening is defined and characterized with no axiom, and the condition only adds significance to it. Today a reader meets the condition first.

### 2.4 Density, register, process history (question 4)

**Estimates (V, bytes of the 738,669-byte file):**

| Kind | Where | Bytes | Share |
|---|---|---|---|
| Connectivity log in one table cell (50 receipts, ~30 reruns) | §8.2 CH:1359 | 17,797 | 2.4% |
| Rest of §8.2 "(Stated: …)" landed lists | CH:1327–1358 | ~39,000 | 5.3% |
| §8.3 adopted readings (re-summaries of D-decisions) | CH:1363–1393 | 13,893 | 1.9% |
| §8.4 governance (integrator, W-root's claim, R18) + §8.8 review table | CH:1394–1420, 1494–1529 | ~12,000 | ~1.6% |
| §9 receipts, names history, "complete-episode comparison" | CH:1545–1613 | ~8,000 of 15,015 | ~1.1% |
| Glossary retired labels / Lean names / two crosswalks | CH:1823–1920 | 23,374 | 3.2% |
| §11 earlier chapters (26 dates, move receipts) | CH:1922–1967 | 10,016 | 1.4% |
| Hexagram/source scholarship inside §1 | CH:297–323 | 14,984 | 2.0% |
| Duplicated statement layers (stated in full, stated whole, §6.9–6.10, §7.1–7.4, §6.12/6.15 overlap) | various | ~75,000 | ~10% |
| **Total process + duplicate** | | **~215,000** | **~29%** |

Inside the body §1–§7 (V): 1,416 parenthesised Lean names; 233 record links; 131 Lean file links; 72 links into `_process/`; 34 into `sources/`; 58 study-section links; 92 "[AI reading" labels; 22 full dates; 73 mentions of `Clearing.`; 18 palimpsest markers. Examples: CH:534 "(they are now joined by `Becoming.Routes`…)", "(the loop-formation theorem is now `Becoming.Closing`, and the reading is revised accordingly…)", "narrowed and taken on 18 October 2026, D43"; CH:923 "(the bridge's `BetterAt` until the F3 sweep)"; CH:1127 "The open-form result, connected on 13 October 2026…"; CH:1151 "Dated note"; CH:325 "historical snapshot (at commit 193c5511)". Ren-narration ("Ren asked/wrote/said/Ren's words"): 32 of 123 "Ren" mentions.

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C4 | major | §8.2 CH:1359 | The row "Integration of the spine" is a chronological log of connectivity reruns: 17.8 KB in one table cell, 50 receipt IDs. It is process history in the canonical chapter, against "only the latest, most informative version stays live". | V | Keep one current sentence ("495 of 11,647 theorems are apart; open: …") with a link. Move the log to THEOREM-CONNECTIVITY.md history. | docs only (`research.py move` for history) |
| C4a | moderate | §8 CH:1311–1544 | §8 says it "lists only what is open", but its rows carry "(Stated: …)" lists of landed results. §8.3 re-summarises adopted readings. §8.4 is titled "Open readings" yet says none is open and holds governance. §8.8 is the review ledger. | V headings and contents | §8 = open targets, open warrants, conjectures, objections (keep §8.9). Adopted readings appear only in the body where used, with a D-link. Governance and reviews go to the board and REVIEWS.md. | docs only |
| C4b | moderate | body §1–§7 | Process traces (dates, "now joined", "until the F3 sweep", study links, receipts, "Ren asked") are interleaved with claims. AGENTS: "live text gives the argument". 32 narrations of Ren's words act as reasons for the order of the work. | counts above | Body sentences state the law and its standing. Provenance goes to one per-section "Records" line (record links only). Dates and palimpsests are removed (the record history keeps them). Ren's words are quoted only where his term is being read, with its source. | docs only |
| C4c | minor | headings with several `<a id>` | Retired-structure anchors remain, e.g. `第一部分的总陈述--part-i-stated-whole`, `68-一条公理推出什么p39-what-the-one-axiom-yields-p39`, `611-公理的分解…p43`, `612-g0-的各处用法在公理之下p44`. OPENING's body links to some of them. | V (grep of `<a id`) | Keep them as invisible aliases (OPENING depends on them) but list them in REFERENCE. A change to OPENING's links goes to Ren as a proposal. | docs only |
| C4d | minor | NONDUAL-METHOD.md | The method chapter also narrates dated "Ren's correction" paragraphs rather than stating the method's reasons. | V reading | Same rule as C4b. Corrections become the reason they give, and the dates go to history. | docs only |

### 2.5 Elegance, central results, reader-first outline (question 5)

**Where it is elegant (J, argued):**
- **One change read three ways** and `keep_pace`/`coming_recurs_iff` hold with no premise. The theory begins from the unfolding and still says something.
- **Recurrence**: lossless ⇔ every configuration returns (finite), and kept history needs openness. Attraction is not-returning, so irreversibility, memory and openness become one fact.
- **Premises carve parts**, and five of the eight World premises are readings of one exchange while three are states of the law. This dissolves "assumptions" into how one carves the unfolding.
- **Margin laws and the four cases**: a part retains/loses/adds iff it is within/beyond its margin. Widening is characterized with no axiom.
- **Decomposition of the condition** into presupposition + step of invariance, and the condition by itself orders nothing. This is honest about where ranking lies.

**Where it is convoluted (J):** §6.7–§6.12 (restatement history, audit of uses, two closure sections); §2's 25-paragraph response line, where each module gets its paragraph and not its place; §4's sequence of V-modules (Withholding, Widening, Pace, Passing, JointKeeping, Tolerance, Regulation) without one governing law; §7 repeating §3.

**Ten central results (candidates for the front).** "In front" means named in the Preface/theorem map today:

| # | Result | In front today? |
|---|---|---|
| 1 | One change, three readings; keep pace; coming recurs iff (no premise) | partly (stated in full item 1) |
| 2 | Recurrence: lossless ⇔ returns; kept history needs openness; attraction | yes, buried in item list |
| 3 | Premises carve parts; 5 readings of exchange + 3 states of the law | in §0 only |
| 4 | Rest under least loss (exact conditions), fed from beyond, arising opens | partly; LeastLoss generalization not in front |
| 5 | Margin law and four cases; widening without axiom | no (§6.13, late) |
| 6 | Closures + selection reaches exactly what couples in; gap; pooled coupling | partly (§7) |
| 7 | Joint excess ends renewers including the greatest; relative position is zero-sum | no (§6.7, CH:967–973) |
| 8 | Learning/identification: no prefix fixes the next value; 2N−1; learnable iff; 理 = `goAlike_iff_lumped` | partly |
| 9 | Significance undetermined by dynamics; condition = presupposition + invariance; orders nothing | yes, repeated 6× |
| 10 | Loops: growth is exponential iff a loop is upstream; frequency | no (§2 middle) |

**Reader-first chapter, about 1/3 length (≈ 200–250 KB). Outline only, section-level content:**

0. **Preface and standing.** One sentence; four kinds of standing; where ethics lies (condition, C, invariance); how to check (one link).
1. **One unfolding.** Readings of one change; law and history; keep pace; recurrence, attraction, branching, junctures (results 1–2).
2. **Premises carve parts.** Whole and manifold; exchange and its five readings; three states of the law; rest and least loss; openness; fed from beyond; joint excess (results 3, 4, 7a).
3. **Organization.** Renewal and consumption; dependence and reserve; identity and wholes; generation (not any new organization); evolution.
4. **Coupling and response.** Closures; counterfactual as course; propagation, loops, frequency, remainder, routes (results 6a, 10).
5. **Knowing.** Testing, experiment, mechanism and 理; learning, identification, learnable; verification on finite stretches (result 8).
6. **Seeking and selection.** Enough and settling; 无明; selection through couplings, gap, pool, capture; collective laws as instances (results 6b, 7b).
7. **Significance without condition.** Undetermined by dynamics; margins; widening; four cases (results 5, 9a).
8. **The continuation condition.** What it adds exactly; decomposition; what it does not settle (result 9b).
9. **Alignment.** 明, pooled coupling, the direction claim and its standing.
10. **Open.** Targets, warrants, conjectures, objections.

Appendices (or REFERENCE): premise card in full; theorem map; logical calibrations with their unfolding meanings; glossary (definitions); crosswalks (corpus, closing/opening, Chinese sources); spine facts.

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C5 | major | whole chapter | The central results are not in front. Results 5, 7 and 10 appear only deep in §2/§6, and the front layers spend their space on standing caveats repeated 6×. | table above | Adopt the outline above. The theorem map leads with the ten results. | docs only |
| C5a | moderate | §4 CH:749–798 | The collective section is a sequence of modules (29.6 KB) without the law that unifies them. J: each is a case of "coupling within/beyond margin across a pool". | V sizes. J unification | Open §4 with the governing law (pool closure + margin). Each module becomes one line as an instance. Whether a Lean instance theorem exists is a question for reviewers A/G. | docs only; possibly Lean proof (instance theorems) |
| C5b | minor | CH:297–323 | Hexagram and Chinese-source scholarship (15 KB, 6 modules) interrupts "one unfolding". | V | One pointer line in §1. The full content goes to the Chinese-sources chapter. | docs only |

### 2.6 Chinese edition, structural parity (question 6)

`theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md` (1,609 lines, 719,508 bytes; V):

| Part | English | zh | Parity |
|---|---|---|---|
| One sentence, stated in full, §0, no-axiom intro | present | present | ok |
| §1–§7, 6.1–6.15, 7.1–7.7 | present | present | ok |
| Stated whole | 11.8 KB (catalogue moved to REFERENCE) | ~56 KB, 103 lines, catalogue inline | **differs** |
| §8 | ### 8.1–8.9 | no subsections; old status table (~45 rows, many "已陈述并检查") + bold headings; no §8.6 logical commitments (LLPO/Markov listing) | **differs** |
| §9 | 15 KB (module table in REFERENCE) | ~118 KB, module table inline | **differs** |
| §10 glossary: retired labels, retired Lean names, closing/opening crosswalk | present | present | ok |
| §10 corpus crosswalk table | present (CH:1864) | absent (only mentioned at zh:1562) | **missing** |
| §11 | present | present | ok |

| id | sev | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| C6 | moderate | zh §8, zh:103 | zh §8 has the pre-restructure form. zh:103 refers to "§8.6", which does not exist in zh (dangling). | V | Mirror the English §8.1–8.9 headings (the content can stay shorter), or remove the §8.6 reference. | docs only |
| C6a | minor | zh stated whole, zh §9 | The catalogue and module table are still inline (~150 KB), while the English moved them to REFERENCE. This makes the two editions unlike in shape. | V sizes | Link to REFERENCE as the English does. | docs only |
| C6b | minor | zh §9 vs CH §9 | The receipts differ: zh cites 20261019T162802.564989Z, English 20261019T160413.543456Z. This was observed during R21's edits and may be transient. | V strings at reading time | R21's lander checks this. | docs only |

### 2.7 OPENING (flag only; Ren's voice, no rewrite proposed)

- Flag (V): the AI footnotes ([^law], [^conditions], [^present], …) make up most of the file's ~54 KB and restate the chapter once more, a sixth statement layer. Footnotes are AI-written and may follow the chapter. If C2 is adopted, the footnotes could point to the theorem map rather than restate.
- Flag (V): the body links to retired-structure anchors (`#第一部分的总陈述--part-i-stated-whole`, `#68-一条公理推出什么p39-what-the-one-axiom-yields-p39`). Any anchor renaming must keep these aliases, or be proposed to Ren.

## 3. What is sound and should be kept

- **The standing labels** (theorem without premise / under premises / condition / reading, with "[AI reading" marks) and the honesty of §6.15 "what the condition adds, exactly": the ethics is never smuggled in.
- **§0 block C** (five readings of one exchange, three states of the law). It is the best single paragraph for the zero-axiom programme and should be the core of the premise card.
- **§6.13** (the generative space without axiom) and the **margin laws**: clean, short, central. Move them forward and do not rewrite them.
- **§7's organization around 明 and pooled coupling**, and the one-sentence direction claim in 7.5.
- **§8.9 objections**: real counter-arguments kept with answers.
- **Scope disclaimers on witnesses** ("a weaker model omitting a relation does not refute"). These are applied consistently.
- **The 九句 and closing/opening crosswalks as scholarship**: keep them, move them to an appendix.
- **Moving the declaration catalogue and module table to REFERENCE** was right. C2 and C6a continue it.

## 4. What I could not check

- Lean correspondence of any statement: no builds were run, and the nineteenth review covered the prose against the Lean.
- Whether REFERENCE.md holds *everything* that would move under C2/C3/C4. I only checked its size (302 KB) and its two main parts.
- Whether a Lean instance theorem unifies the §4 V-modules (C5a). That is a question for reviewers A/G.
- zh wording, beyond its structure.
- Lines being edited by R21 during the review. The line numbers and the receipt discrepancy (C6b) were observed at reading time.
- Whether OPENING's footnotes should change. That is for Ren, so I only flag it.
