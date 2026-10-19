# Review G: integration of the recent frontier (modules landed 18–19 October 2026)

Reviewer G, twentieth review. Read-only. The measurements are on the working tree at HEAD `b52f142b3`. The last landing since the brief's `121ff8042` is R21, and it changed only docstrings and docs. The theorem classes come from `THEOREM-CONNECTIVITY.json` (commit `831fcaf73`, 11,647 spine theorems). `L/` abbreviates `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`. `CH` is `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`. Scratch tables are in `scripts/G/`: `G_table.txt` (class counts per module), `G_importers.txt`, `G_new.txt` and `G_newrecords.txt`.

## 1. Summary

1. **The frontier is large, and most of its new results are leaves.** Since 17 October, 121 core modules were added (56,188 lines, 4,317 theorems):
   - 67 are ports from the periphery (F1–F3, W);
   - 7 re-read apart groups on the base (U3–U5);
   - 47 are new results (2,287 theorems, 31,677 lines).

   **No module that existed before 17 October imports any of the 47.** They form linear chains that end in 58 import-leaves. For example: LawAlongRun→LawThroughCoupling→LawThroughChangingCoupling; SelectionGap→SelectionPool→PoolResponse→Rejoining; Ideals→HistoryIdeals→Verification→LimitVerification; Hexagrams→Places→{Laws, Sites}→Sequences.
2. **The frontier deepened the two-family split instead of closing it (major).**
   - 30 of the 47 new-result modules use only Process-family vocabulary, and 17 use only World-family vocabulary.
   - Only 10 of their 2,287 theorems are statements on both families.
   - `families_reach_each_other` is still all False. §8.2 still lists "a definitional join of the two families" as open.
   - The collective line is cut down the middle. Withholding, Tolerance, Widening, Pace, RuleCapture and SharedCodes are runs of `Law.run` over private configuration types. Selection*, Rejoining, Regulation, Passing and MutualDependence are on Flow/Web.
3. **Generalizations land as new leaves plus "the old law is a case of the new" theorems, so each such law now has two proofs (major).** Examples: Horizon below HistoryIdeals, the rest family below LeastLoss, Counting below CensusCounts, LawAlongRun below LawThroughCoupling, Selection below SelectionPool. The theory grows where it should compress. Ideals imports nothing, and LeastLoss's `Amounts` needs nothing above Recurrence, so both general forms could sit *below* the special ones.
4. **Several frontier modules define their own version of a notion the spine already has, with no bridge theorem (moderate each).**
   - Widening's loop of `Nat → Nat` links, beside Loops'/Propagation's loops of couplings.
   - Withholding's `up` relation and Boolean "giving", beside the Web's dependence and the Flow's `give`.
   - LimitVerification's `Identifies`/`Converges`, beside Learnable/LearnableRuns' `Rests`.
   - RuleCapture's `Counts`, beside Capture's lists and `Becoming.Counts`.
   - Interleavings' `LocalLaw`, beside World/Order.
5. **The 周易 line (5 modules, 511 theorems, 22% of new-result theorems) is a good *instance* that also produced a reusable general law, `Commuting`.** But:
   - It sits in §1 of the canonical chapter: 14 kB, about 18% of §1.
   - HexagramPlaces and HexagramSites are mostly formalization of the text (rfl proofs, 6–8 distinct general declarations cited).
   - In the Y1 map, 33 of the 52 "agreement" (相合) passages cite only `Hexagram.*` declarations: the passage's own encoding, not a general law.
6. **The reporting absorbs landings rather than integrating them.**
   - §8.2 ("lists only what is open") went from 31 kB to 57 kB. It carries "(Stated: …)" landing lists and a 17.8 kB per-landing connectivity log (CH:1359).
   - "The theory stated whole" still quotes the 17 October count (195 of 7,698 apart; now 495 of 11,647). It mentions almost nothing of §2–§4's frontier.
   - About 20 ported modules (the correction family especially) have no record and no chapter sentence.

## 2. Findings

### 2.1 Pattern-level findings

| id | severity | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| G1 | major | the 47 new-result modules; THEOREM-CONNECTIVITY.json; CH:1359 ("Open: a definitional join") | **The frontier added to both base families separately and joined them nowhere.** New results using World vocabulary (`Web.`/`Flow.`/`World.`) and no Process vocabulary: 17 modules (SelectionGap, SelectionReach, SelectionPool, PoolResponse, Rejoining, Regulation, Passing, MutualDependence, RelativePosition, Cuts, Exclusion, Exhaustion, ExchangePremises, CensusCounts, CensusBinding, LevelCoupling, PlaceTransitionNets). The reverse, Process vocabulary only: 30 (Hexagram*×5, Ideals family×4, Withholding, Tolerance, Widening, Pace, RuleCapture, SharedCodes, Enough, Settling, LastChange, Unrolling, Labels, Undecided, Junctures, Commuting, Interleavings, HistorySums, JointKeeping, …). Statements on both families from new results: 10 (LawThroughCoupling 2, LawThroughChangingCoupling 4, Hexagrams 2, HexagramSequences 2). Statements on both families overall: 163 of 11,647. | My grep counts per module (`G_table.txt`, the count table in this report's working notes); `statements_on_both_by_module`; `families_reach_each_other` all False. | Make the definitional join the next unification item, before further leaves. A concrete route: `ExchangeLaw.worldRun` (L/CounterfactualRuns.lean:63) already sends a law of exchange to a run. (a) Define the World family's flow/web *as* the run of an `ExchangeLaw` (or a `Law` on configurations `levels × present`). (b) Then state the World laws as laws of that run. After that, every `Law.run` result applies to worlds by instantiation. | Lean, large (shared definitions; integrator decision) |
| G2 | major | Horizon/HistoryIdeals (L/HistoryIdeals.lean:620–641); LeastLoss "_whole" (L/LeastLoss.lean:421–496); Counting/CensusCounts (L/CensusCounts.lean:6 "states the same laws with neither"); Selection/SelectionPool (L/SelectionPool.lean:31 "re-derived with its own hypotheses"); LawAlongRun/LawThroughCoupling (`Run.consistentUnder_eq_iff`) | **Convergence is by correspondence, not compression.** Each generalization lands above the special law and adds a theorem saying "the old is the case of the new", while the old proof stays. So one law has two proofs and the theorem count rises. The restating pattern is also registered: 16 apart roots in category "restates". | 0 pre-existing modules import any of the 47 (checked: every importer of a new-result module is itself new). Examples:<br>• LeastLoss proves the spine's rest laws "again from the least-loss law, their statements unchanged" (six `_whole` theorems).<br>• HistoryIdeals: "Horizon's `Refutable.not_not` is the case of runs of `Ideals.RefutableBy.not_not`". | **Invert dependencies where the general module is pure and low:**<br>• `Ideals` imports nothing, so Horizon can import it and derive `Refutable.*`, `Adheres.*` and `Verifiable` as instances.<br>• Split `LeastLoss` into a small `Amounts` module (no spine imports) placed below `Flow`/`World`'s rest laws, and prove `falls_not_recurring`, `falls_stop_unrefuted`, `World.rests_unrefuted_enclosed` once, as the whole-number instance. Then delete the six `_whole` re-proofs.<br>• Prove `World.counting_under` as a corollary of `World.counting_under_counted` (decided ⇒ counts exist).<br>• Make `Flow.unselected_beyond_coupling_all` the singleton corollary.<br>Gain: one proof per law, and "general" becomes the base. | Lean proof work, moderate (re-ordering imports; no new mathematics) |
| G3 | major (aggregate of G4–G9) | see G4–G9 | **Local carriers duplicate spine notions.** Several frontier modules build a private carrier for a notion the spine already defines (loop, giving/waiting, share, identification in the limit, step index, level), then wrap it in `Law.run` to sit "on the base". The connectivity measure cannot see this: a statement on `Law.run` of a module-private law counts as "statement on Process/Frame/Run/Trace". So "apart = 0" overstates integration for Withholding, Tolerance, Widening, Pace, RuleCapture and SharedCodes, which reference no `Web`/`Flow`/`World` symbol at all. | `grep -cE '\b(Web\|Flow\|World)\.'` = 0 in all six; their headers define formations as an arbitrary `α` with `up : α → α → Prop` (Withholding:3–10), differences as `Nat` (Widening:16–22), codes as functions (SharedCodes). | Add a class to the connectivity measure: "on the base only through a law defined in the same module". Report it beside apart. Then close the largest such groups by instance theorems to the World family (G6, G7). | measure: script change; joins: Lean, moderate |

### 2.2 Specific duplications and folds

| id | severity | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| G4 | moderate | L/LawAlongRun.lean, L/LawThroughCoupling.lean, L/LawThroughChangingCoupling.lean; CH:585–587; three records | **One criterion in three modules.** The content is one theorem: a run admits a law going alike under an equivalence `E` exactly where its steps are `E`-consistent (`Run.law_under_iff`). Projection, fixed coupling and changing coupling are three choices of `E`. Each landed as its own module, record and chapter paragraph, because §8.2 listed each instance as open. | LawThroughCoupling header: "Through equal projections this is `Run.ConsistentThrough`" (`Run.consistentUnder_eq_iff`); LawThroughChangingCoupling: "Fixed conditions are the instance". | Fold into one module, `LawAlongRun`, with `law_under_iff` as the law and the three relations (plus `exact_law_iff`) as corollaries; one record ("a law along one run, under a relation") and one chapter paragraph listing the three readings. Move the other two records to `history/`. | Lean move + small re-proof; docs |
| G5 | moderate | L/LimitVerification.lean:75–98, 420–445 vs L/Learnable.lean:75–82, L/LearnableRuns.lean:55–62, L/Unrolling.lean, L/Labels.lean | **Two theories of learning in the limit, unjoined.** LimitVerification defines `Method`, `Converges`, `Verifies`, `Identifies` (Gold/Putnam/Kelly). The older learning line defines an extrapolation `pred` through a map `reg` that "comes to rest in accord" (`Learnable.Rests`, `LearnableRuns.Rests`), and Unrolling/Labels build on it. `LearnableRuns.Rests` is `Limit.Identifies` for a guess fixed by the `reg`-record. Neither side cites the other. | `grep` finds no `Learnable`, `Unrolling` or `Labels` in LimitVerification and no `Limit.` outside it. Its "Identification" section is a section name, not `Becoming.Identification`. | Prove the bridge `learnable_iff_identifies`: learnable through `reg` exactly where some guess fixed by the `reg`-record identifies `val` in the limit. Then state Learnable/Unrolling/Labels as the "through a map" case of the limit hierarchy. One vocabulary: `Converges`/`Identifies`; retire `Rests` for extrapolations, which collides with a run's rest in `Enough.Rests`, `Amounts.rests` and `World.rests`. | Lean, moderate; docs |
| G6 | moderate | L/Widening.lean:16–22, 484 (`whole_strengths`) vs L/Loops.lean:733, 1282 and L/Propagation.lean:1290; L/Rejoining.lean | **Two loop theories.** Widening's loop is a list of maps `Nat → Nat` with a return map, and its "strength" is the product of a list of numbers. Loops' loop is a cycle of couplings in a flow, with strengths per exchange (`carried_around`, `carried_doubles_around`). Widening uses Loops only for arithmetic lemmas (`Loops.mul_assoc_nat`, `Loops.pow_le_pow_base`). Its own header says "no theorem here reads a loop of Rejoining as a return map". §4's table and the correction row combine Widening's difference with Rejoining's levels and Loops' doubling as if they were one object. The nineteenth review caught one false sentence from this (the "doubles" row); the structural cause remains. | Widening.lean:22; CH:777 and the §4 table rows 5, 6 and "keeping the capacity to correct". | State Widening's return map as Rejoining's difference at one condition under a law whose response is linear in the difference. Or state it as Loops' carried amount when the actual response attains the carrying bound (`carried_attained`). Then "strength" means one thing: the product of coupling strengths around a cycle. | Lean, moderate (a join theorem) |
| G7 | moderate | L/Withholding.lean (header 1–20), L/Tolerance.lean, L/JointKeeping.lean, L/SharedCodes.lean, L/Pace.lean | **The collective laws have their own formations.** Withholding and Tolerance take formations to be any `α`, with "waits on" an arbitrary relation and giving a Boolean per formation. The spine's formations, conditions, giving (`Flow.give`) and dependence as admission at a threshold (`Web`) are not used. Tolerance's "gives where at least k of what it waits on gave" is structurally the Web's admission at a threshold with levels counting givers, but no theorem says so. | `grep` shows 0 `Web.`/`Flow.`/`World.` in Withholding, Tolerance, Widening, Pace, SharedCodes and RuleCapture. | Instance theorem: (1) a web in which each formation gives one unit to a condition its dependents require, (2) with admission at need `k`, has activity whose run is `Law.run (tolerating k)`. Withholding (k = all) and Tolerance then become laws of webs, and §4's table rests on one ontology. | Lean, moderate |
| G8 | moderate | L/CensusCounts.lean, L/CensusBinding.lean (70 theorems, 1,541 lines) vs `Becoming.Counting` | **Counting has a decided family and a counted family, both live.** CensusCounts "states the same laws with neither" decidability nor pointwise restriction. The decided family still has its own proofs, and the chapter cites both (CH:56, 116, 351, 1437). | CensusCounts has one importer (CensusBinding), and Counting does not use it. | Make the decided forms corollaries (counts exist where decided: `counts-exist-where-decided`), or move them to history. Cite only the counted forms in "stated in full" and §8.6. | Lean, moderate |
| G9 | minor | L/RuleCapture.lean:384 `structure Counts`; L/Decidedness.lean:207 `def Counts`; L/Countdown.lean:101 `structure Countdown.Counts`; L/MutualDependence.lean:376 `share_ratio_pow`; L/Capture.lean:110 `share_rises`; L/Ideals.lean:90 `Preorder` used by RuleCapture (11 uses); L/LeastLoss.lean:108 `Amounts` with its own `le_refl`/`le_trans`; L/Pace.lean:9 "two-level course" vs `Flow` levels | **One notion, one name, broken in small ways.**<br>• `Counts` names three different things.<br>• The multi-generation share law sits in MutualDependence instead of Capture.<br>• The basic preorder lives in a module about histories and is imported by RuleCapture only for that.<br>• `Amounts` re-declares an order.<br>• "level" means both an amount at a condition (Regulation, LevelCoupling) and a layer of a course (Pace).<br>(The nineteenth review covered the Widening/Passing collisions; not repeated here.) | as cited | (1) A small `Becoming.Order` (Preorder, equivalence); `Amounts` extends it. (2) Rename `RuleCapture.Counts` to `ShareCounts` (or reuse Capture's lists). (3) Move `share_ratio_pow` to Capture. (4) Call Pace's layers "fast course and rule" (it already says so). | Lean rename, small |
| G10 | moderate | L/Interleavings.lean:42 ("Not shown: … the correspondence with a world's footprint of `Becoming.Order`"); CH:339 | **The most foundational frontier result is a separate model.** Interleavings derives the shared step index from relata's own courses (`LocalLaw`, `ownCourse`). The step index is a declared representation commitment of the World base ("stated whole", CH:1186). No World is built from interleaved local courses, so the commitment remains a commitment of every World-family law. | 0 `World`/`Flow`/`Web` references in Interleavings; class P:7, used:49. | Join it to the base: from a `LocalLaw` and an interleaving, build the `World`. Prove that its laws do not depend on the choice of interleaving where exchanges share no relatum (which `swap_courses` begins). Then "a shared index" leaves the premise card as a reading. | Lean, moderate–large |

### 2.3 The 周易 and Chinese-sources line

| id | severity | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| G11 | moderate | L/Hexagrams.lean … L/HexagramSequences.lean (511 theorems, 5,743 lines, 65 apart); CH:297–319 | **An instance library inside the spine and inside §1.**<br>• Hexagrams (27 distinct general declarations used, e.g. `Law.lossless_iff_returns`, `Frame.claims_recur_iff`, `Learning.goAlike_iff_lumped`) and HexagramLaws (25, with `Law.Commutes.*`) are instances of general laws. They are stated as such and good.<br>• HexagramPlaces (8) and HexagramSites (6) are mostly formalization of the text's statements (160 and 140 `rfl`).<br>• Apart: 20/108 and 23/103, all model witnesses about named configurations.<br>• In the chapter, six paragraphs (14.1 kB) plus the Chinese-sources paragraph sit in §1 "Becoming: one unfolding", beside the foundational laws. §5 (how evaluation forms) is 7 kB in total. | Hexagram modules cite few general declarations; `G_table.txt`; section sizes measured from CH. | Keep Hexagrams and HexagramLaws as the instance on the spine, and keep `Commuting` and `Junctures` (general laws the line produced) in L4. Move the text-formalization parts (Places, Sites, Sequences' census facts) to an instance ring (`Becoming.Instances.Changes`, still pure). In the chapter, replace §1's six paragraphs with one paragraph in a new short section "Instances: worlds read on the spine" (hexagrams, P/T nets, the Chinese sources), pointing to YI-ZHUAN-AND-BECOMING. | docs; Lean move (no proof change) |
| G12 | moderate | `_process/.../development/y1-changes/passages.json` (90 passages: 52 agreement, 26 scope, 12 divergence); `ro-relational-sources/passages.json` (248: 95/94/59) | **"Agreement" mixes two different things.** 相合 is defined as "a checked law of the spine with the same structure". In Y1, 33 of 52 agreements cite only `Hexagram.*` declarations: the encoding built for the passage (e.g. 繫辭下 ch.1 → `Hexagram.order_length`; 孔穎達's 非覆即變 → `Hexagram.Paired`). That shows the text's combinatorial claim is correct, not that the theory's general law matches it. The RO map, whose declarations are general laws (`exists_law_iff` 23, `goAlike_iff_lumped` 18), has a much lower agreement rate (38% vs 58%). The grading is otherwise honest: verbatim fragments are checked, there are explicit non-claims (相合不是印证), and divergences are kept. | own count over `passages.json` (`kind` × whether every declaration starts with `Becoming.Hexagram`) | Split agreement into "agreement with a general law" and "the text's structure, formalized". Add a field `law_level: general / instance / encoding` per declaration; `verify_mapping.py` can compute it from the namespace. Report the split in both chapter tables. | data + docs |

### 2.4 Ported modules, the chapter's reporting, and support code

| id | severity | where | finding | evidence | proposal | cost |
|---|---|---|---|---|---|---|
| G13 | moderate | F3C/F3Q/F2 ports: Transactions (59 thms), Reconfiguration (51), PooledEnvelopes (44), TreeSearch (35), Dispatch (34), GuardHorizon (32), Acceptance (17), ContingentPlans, RouteFormation (70), ResponseLearning (64), CodeAcquisition, PartialReadout, Coverage, SeedReach, ScopedReach, ProjectedLaws | **Ported content in the pure core with no place in the argument.**<br>• These modules appear only in the reference catalogue and generated indexes. No record cites them by core name, and no sentence of the canonical chapter does.<br>• 14 of the 18 theorems outside the main dependency component are in these ports (GuardHorizon 5, IntegerOrder 3, ListTests 2, Naturals 2, Dispatch 1, PartialReadout 1).<br>• The ports raised apart from 175 to 441: 230 of the 495 apart theorems are in ported modules. | grep over `results/records/*` and `theories/` (hits only in THE-THEORY-OF-BECOMING-REFERENCE.md, LEAN-INDEX, lean-declarations); `components.theorems_outside_the_main_component`. | Per module, choose one:<br>(a) a record and a sentence where the argument uses it (the correction family belongs under §7.6 "executable sequence", whose records cite Actuation/Countdown but not Transactions/Dispatch);<br>(b) an "applications" ring inside the package (pure, outside the spine count), for protocol models of AI correction.<br>Being in the core should mean being part of the theory's argument. | docs; Lean move |
| G14 | moderate | CH:1327–1360 (§8.2), CH:1359 (17,797-char row), CH:1180–1199 ("The theory stated whole") | **Landings are logged in the open-programme list and do not reach the synthesis.**<br>• §8 says it "lists only what is open", yet three rows carry "(Stated: …)" lists of landed modules.<br>• "Integration of the spine" is a chronological log of every connectivity rerun (R1, R2, … RG), with receipts.<br>• §8.2 grew from 31 kB (17 Oct) to 57 kB; the chapter grew from 504 kB to 739 kB (+47%) in two days.<br>• "The theory stated whole" still cites the 17 October measure (195 of 7,698). Its four parts mention none of the selection gap, collective constraints, verification, junctures or interleavings (keyword counts 0), and no renewal or evolution at all ("renew": 0). | section sizes from `git show`; keyword counts on CH:1180–1199 | Move the rerun log to THEOREM-CONNECTIVITY.md (it is a measurement history) and keep one current line in §8.2. Delete the "(Stated: …)" lists (the records hold them). Give "stated whole" a part V, "What holds of formations together", that compresses §2–§4 and §7 to their laws (selection gap, pooled closure, what closes a difference, the collective constraints). Update its connectivity sentence to the current measure. | docs |
| G15 | minor | L/Naturals.lean, L/Integers.lean, L/IntegerOrder.lean (15/39 apart, prelude-only), L/ListTests.lean; per-module arithmetic (`mul_assoc_nat` in Capture and Loops, `RuleCapture.Counts.mul_right_comm_nat`) | **Arithmetic support is scattered.** Four support modules and per-module re-proofs of prelude facts. Legitimate (Init only), but they inflate the apart count and the components. | `apart: prelude-only statement` 43; components list | One `Becoming.Arithmetic` support module. Exclude prelude-only support from "apart" in the measure, reported separately (as is already done for categories). | Lean move, small |

## 3. Per-module judgment

### 3.1 The mostly-apart modules

| module | apart/total | what is apart | judgment |
|---|---|---|---|
| LeastLoss | 47/74 | dyadic and layered countermodels, `Amounts` arithmetic | **A legitimate general structure plus calibration witnesses.** The countermodels are needed: they show each premise is needed. Its integration should be by inversion (G2), not by restating: `Amounts` below the rest family. |
| HexagramSites | 23/103 | what 彖/小象/文言/王弼 say of named configurations | **An instance library, sidecar-like.** Move it to an instance ring (G11). |
| HexagramPlaces | 20/108 | censuses, the 彖/象 on named configurations | Same. Its contextual-gluing laws (`halves_glues_iff` via `Contextual.fitsFree`) are true instances and should be kept in view. |
| Frontier (port) | 23/71 | menu witnesses | **A legitimate tool.** FrontierFrames and FrontierWorlds (52 + 8 theorems, 0 apart) read it on the base. Keep it. |
| Ideals | 16/99 | order support, equivalences, the classification of word ideals | **A legitimate self-contained mathematical tool** (it imports nothing), and the right base for Horizon. Invert the dependency (G2). Move `Preorder` to a basic order module (G9). |
| HexagramLaws | 13/130 | censuses over the received order | **A good instance.** It uses `Law.Commutes.iterate` and `Law.Commutes.apart`. Keep it. |
| IntegerOrder, Naturals, ListTests | 15/39, 6/18, 3/36 | prelude-level facts | **Support.** Consolidate (G15). |
| CodeAcquisition, PartialReadout, Acceptance, StrictTransport, ProfileReach, ListFootprints, GuardHorizon, PositiveGround | 8–13 each | periphery model witnesses | **Ports.** Decide per G13: give them an argument role or move them to an applications ring. |

### 3.2 Base, local notions, chapter use and origin (items 1–3 of the brief), by group

| group | base | own local notions (G-ref) | used by the argument? | origin |
|---|---|---|---|---|
| Selection line: SelectionGap, SelectionReach, SelectionPool, PoolResponse, Rejoining | World | Pool closure is a genuine generalization. SelectionPool re-derives the singleton case instead of making it a corollary (G2). | **Yes.** §7.1–7.4 cite `Flow.act_unselected`, `Web.selects_alike_all_iff`, `Flow.unselected_beyond_pool` and `Replenishing.closes_through`, and §4's table cites them. The best-integrated line. | §8.2 open items, and Ren's question on 明 |
| Law along a run: LawAlongRun, LawThroughCoupling, LawThroughChangingCoupling | Process, plus 6 statements on both families | the same criterion three times (G4) | Listed in §3 (CH:585–587). No later section reasons from them. | three §8.2 instance items |
| Settling line: Enough, Settling, LastChange | Process | `Rests` name clash (G5) | §3 and LimitVerification use Enough. | §8.2 seeking row |
| Learning: Unrolling, Labels | Process | parallel to LimitVerification (G5) | §3 learning paragraph | §8.2 learning row |
| Histories and verification: Ideals, HistoryIdeals, Verification, LimitVerification | Process (Ideals has its own order) | parallel identification notions (G5); Horizon kept beside them (G2) | §2 paragraphs; §8.1 scientific inquiry cites the verification record. | A4 ("integrate all"), O1/O2 |
| Counting: CensusCounts, CensusBinding | World | a parallel family (G8) | Yes: "stated in full", §0, §8.6. | review exception |
| Continuation: Exclusion, Exhaustion | World | none | **Yes.** §6.7 uses them in the restating argument. | §6.7 open item |
| Collective: Withholding, Tolerance, Widening, Pace, Passing, JointKeeping, Regulation, RuleCapture, SharedCodes, MutualDependence | split across both families (G1, G7) | own formations and giving (G7), own loops (G6), `Counts` (G9) | **Yes.** §4's constraint table is a real argument that organizes them. | A new branch, from an external account of social viability and from the gaps the RO map found |
| ExchangePremises | World | none | **Yes.** §8.1 target 1: three of eight premises become states of the law. This is compression. | §8.1 |
| Interleavings | Process, on its own `LocalLaw` | own carrier (G10) | §1, §8.5 | §8.2 relational-start row |
| SG: Undecided, Junctures, Commuting | Process | none; Commuting is reused by HexagramLaws and SharedCodes | §1, §3 | SSBX review |
| HistorySums | Process | extends Routes | §2 | SSBX review |
| Cuts (K1/K2) | World | none | §2 | **Convergence:** examples became one general law. |
| LeastLoss | own `Amounts` plus 6 restatements on World | G2 | "stated in full", §0 | §8.2 entropy row |
| PlaceTransitionNets | World, through `Net.law : ExchangeLaw` (L/PlaceTransitionNets.lean:159) | none: a clean instance of the base | §8.7 only | A new branch: correspondence with Petri nets. Fine as an instance (G11's instance section). |
| RelativePosition | World | none | §8.2 and the OPENING footnote | an OPENING footnote |
| LevelCoupling | World | the "level" sense (G9) | §2 | N2 instance check |

## 4. Converging or expanding? Numbers

**The core: modules and theorems.**

| measure | start | now | change |
|---|---|---|---|
| core modules in `L/` | 238 (end of 17 Oct, `cc1beb086`) | 297 | +59 net; 121 added, about 60 bridge/join modules superseded in the F3 sweep |
| core source size | 6.61 MB | 8.89 MB | +34% |
| spine theorems | 7,698 (U, 17 Oct) | 11,647 (`831fcaf73`) | +3,949 (+51%) |

The 121 added modules hold 4,317 theorems: 2,287 in new results, 1,911 in ports and 119 in re-readings.

**Apart over time** (THEOREM-CONNECTIVITY.json history):

| point | apart | of | components |
|---|---:|---:|---:|
| 15 Oct | 946 | 6,089 | 63 |
| before U | 1,019 | 7,214 | 65 |
| after U | 195 | 7,698 | 60 |
| U2 | 180 | 8,007 | 56 |
| G3 | 175 | 8,304 | 56 |
| G4 / F2 | 201 | 8,676 | — |
| F3Q | 303 | 9,225 | — |
| F3C | 480 | 10,184 | 79 |
| F3 sweep | 441 | 9,648 | 59 |
| U3 | 426 | 10,388 | — |
| LL1 | 511 | 10,994 | — |
| O1/O2 | 519 | 11,150 | — |
| U5 | 480 | 11,195 | — |
| now | 495 | 11,647 | 66 |

Of the 495 apart theorems, 376 are in modules added since 17 October: 230 in ports and 146 in new results, of which Hexagram* account for 65 and LeastLoss for 47.

**Records and the chapter.**
- Records: 229 → 279 (+50 in two days; list in `G_newrecords.txt`).
- Canonical chapter: 503,641 → 738,669 bytes. Chinese-sources chapter: 400 kB; 易传 chapter: 107 kB (both new).

**What converged.**
- The bridge is gone: 0 bridge modules, 75 superseded, F1–F3.
- The import tree is re-rooted at World (W).
- Apart groups were re-read on the base: U3/U4 took apart from 488 to 426, and U5 from 519 to 480.
- K1/K2: examples became one law.
- ExchangePremises: three premises became states of the law.
- `Commuting`: a general law born from an instance and reused twice.
- The selection line and the §4 table organize their results into arguments.

**What expanded.**
- 47 new result modules, none feeding back into older ones (0 older importers).
- 5 hexagram modules.
- A collective line on private carriers.
- Three versions of one criterion (G4).
- Two learning-in-the-limit vocabularies (G5).
- Two loop theories (G6).
- Two counting families (G8).
- Ports with no argument role (G13).

**Judgment:** the period converged at the level of *infrastructure* (bridges, re-rooting, re-reading on the base) and expanded at the level of *theory* (leaves, parallel carriers, duplicate proofs).

**Recommendations, in order of gain.**
1. **The definitional join (G1).** It turns 163 "both" statements into ordinary instances and lets every `Law.run` result speak about worlds.
2. **Dependency inversion (G2).** Ideals → Horizon; Amounts → rest family; CensusCounts → Counting; SelectionPool → Selection. The expected effect is fewer theorems, with each law proved once.
3. **Folds.**
   - LawAlongRun + LawThroughCoupling + LawThroughChangingCoupling → one module and one record (G4).
   - The Learnable/Unrolling/Labels ↔ LimitVerification bridge, with one vocabulary (G5).
   - Widening ↔ Rejoining/Loops (G6).
   - Withholding/Tolerance as webs (G7).
4. **Generalize:** Interleavings → construction of World (G10).
5. **Move to an instance or application ring (pure, outside the spine count):**
   - the text-formalization parts of HexagramPlaces, HexagramSites and HexagramSequences (G11);
   - the ports with no argument role (G13);
   - and, if the theory wants it there, PlaceTransitionNets as the model instance of the base.
6. **Reporting.** Move the per-landing logs out of §8.2. Make "stated whole" absorb §2–§4/§7. Split the "agreement" grade (G12, G14).
7. **A rule for the board:** "a new module that generalizes an existing law lands *below* it, or proves it as a corollary, not beside it". Applied from now on, this rule would turn expansion into compression.

## 5. What is sound and should be kept

- **The selection line.** SelectionGap derives the rest's response from a law of exchange instead of supplying it. PoolResponse derives SelectionPool's premise (`ExchangeLaw.Through.selectsThroughAll`). §7 is built on these. This is the model of a lemma plus the derivation of its premise.
- **§4's constraint table.** It takes an external account, restates each constraint as a law with its limit, and says "none is an axiom". This is real integration in prose.
- **Exclusion and Exhaustion** carry §6.7's restating argument.
- **ExchangePremises** reduces the premise card. **Cuts** made examples general. **Commuting** (from the hexagram instance) is reused by HexagramLaws and SharedCodes.
- **The infrastructure consolidation:** the F1–F3 sweep (no bridge), the W re-root, and U3–U5's base readings with an apart register in which every root has a category.
- **Honest scope statements** in headers ("Not shown: …", Widening.lean:22, Interleavings.lean:42).
- **The Chinese-sources map:** verbatim fragments checked against preserved revisions, a three-way grading with explicit non-claims, and 59 divergences kept.
- **PlaceTransitionNets** as a clean instance: `Net.law : ExchangeLaw`, with flow, web and world built from it.

## 6. What I could not check

- I did not read the 47 new-result modules line by line; I read headers and grep-level structure.
- Whether the proposed joins (G6, G7, G10) are provable with no new premise. They are stated as conjectures with the shape I expect.
- The semantic fit of individual passage readings. The 400 kB Chinese chapter and the 107 kB 易传 chapter were only sampled.
- No builds and no rerun of the connectivity measure, so the classes are those at `831fcaf73`. R21, landed since, changed docstrings only, per its commit message.
- Whether records outside `theories/becoming/results/records/` (studies, other chapters) give the G13 ports an argument role.
- Port modules: I classified them by the F1–F3 and W commit messages, not by reading each port map in full.
