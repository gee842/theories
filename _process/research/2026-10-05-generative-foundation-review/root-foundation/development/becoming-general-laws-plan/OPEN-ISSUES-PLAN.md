# Plan: the open issues after the general-laws plan

14 October 2026. **Status: proposal awaiting Ren; nothing here has landed.** AI-authored (Claude Opus 5.5, the integrating session), at Ren's request:

> can you come up a plan to fix all the open issues?

It follows [PLAN.md](PLAN.md), which landed on main through `26705afc` (not pushed). Every item below was checked against the repository before it was written down; the evidence is named in each row.

## 1. Inventory

| # | Open issue | What is actually wrong (checked) | Fix | Size |
|---|---|---|---|---|
| 1 | Push | main is 259 commits ahead of `origin/main` 968e1ef4, a fast-forward; `research.py check` 0 errors, 0 drift; `make research-test` 83 tests pass | push on Ren's yes | Ren |
| 2 | reserve-defers-ending: “the chain coextinction and the cascade are not yet independently reviewed” | False. The twelfth review ([P30-P31-P29B](../../BECOMING-P30-P31-P29B-REVIEW.md)) checked `chain_ends`, `Cascade` and the attained bound; its corrections (T2, T3: chains of any finite length, `short_cascade`, `lpo_of_ending`) were confirmed closed by the thirteenth ([P32-P34](../../BECOMING-P32-P34-REVIEW.md), table “P33b: T1–T8”) | rewrite the evidence sentence; add the thirteenth review as a reference | A |
| 3 | space-and-its-parts: “the corrections after the tenth and the eleventh are not yet independently reviewed” | False. The eleventh review ([P25B-P29](../../BECOMING-P25B-P29-REVIEW.md)) covered P25b, the tenth's corrections; the twelfth covered P29b, the eleventh's (`law_of_em`, `law_iff_em`, `ceases_below`, `seedbank_world` “都对”) | rewrite; add the twelfth review as a reference | A |
| 4 | scientific-inquiry-foundation: hypothesis 1 is a process note with a date | It is Ren's direction of 13 October plus working instructions, not a premise of the result | Ren's support (dated, [source](../../../../../../sources/15-codex-theory-conversations/2026-10-13-scientific-foundation-as-testable-hypothesis.md)) to correspondence; “full-theory necessity is not a proof premise” to `not_required`; “no automation” to history; “local scopes kept” to `does_not_show` | A |
| 5 | continued-change-needs-openness cites `stills` | `Flow.stills` was renamed `change_stops_unrefuted_around` when the rest family was named by strength (35d67bb5, 2a41bec9); law 3 already cites the new name | update the hypothesis label | A |
| 6 | “P3b–P6” in the chapter's §8 review row | It names the first review's object: the relational reading, the unification of renewal and consumption and the dynamic dependence (study §§1–6; Dependence, Renewal, Metaethics) | write those names | A |
| 7 | relational-renewal-classification: “G0's object is 生生” stands unattributed | It is Ren's correction (9 October: “我G0是什么？generative和degenerate…不overlap吧”), here in AI wording | attribute to Ren with the source link; Ren's words verbatim, the AI's restatement labelled | A |
| 8 | substitution-preserves-consumption: next step “the same preservation for general laws with changing dependence” | Partly answered: `Web.consumingIn_kept_iff` gives it for one change of dependence, in every web | narrow the next step to several changes or several formations | A |
| 9 | Market words in record text | `paid` in pending-task-context-applicability (“paid cost”, “paid report coverage”), `budget` in renewing-consuming-formation. (`price` in evolution-on-descent and process-and-frame-as-readings is the Price equation, a scientific term: kept) | structural words: “the work already used”, “covered report”, “renewal bound” | A |
| 10 | Migration judgment calls not yet reviewed by the integrator | FR's three (law 3 strict order without transitivity, law 4 one-class case, two status sentences) and M5's remaining ones (added hypotheses in joint laws 3–5, “to at least m”, review summaries without round labels, sentences moved to history only) | read each against the Lean statement; correct or confirm in a history note | A |
| 11 | Market 5/12 boundary: the landing side rests on the market's own gain estimate | There is no general reaching law: Lasting has the ladder law for lasting and `avoids_iff_closed` for never reaching, not its dual | prove the dual in the core: a determined law reaches a target within `n` steps exactly when some variant (a level that every step outside the target lowers, bounded at the start by `n`) exists. The landing side becomes its instance; the gain estimate is what supplies the variant for that one rational law, stated as the instance's content. Also restate `every_finite_stock_has_obstructed_positive_seeds` as an instance of `exhausts` | B |
| 12 | Three one-history records (enacted-scene-binding, encounter-selection-and-revision, retrospective-source-binding) | Each is an instance of `interprets_every_iff`, but the link from the history to its inputs is a `decide` on one history (`coordinated 37`) | state the law for every history in which the access or encounter supplies the binding inputs; the one history becomes a checked instance; try retrospective's coverage law the same way | B |
| 13 | Four machine records partly general | acquired-revision-of-pending-task (the warranted-revision conditions of one installation), pending-task-context-applicability (two practice protections), joint-practice-forms-continuation (headline `complete_history_is_one_trace` by `decide`), formed-goal-revision-continuation (general only over its construction) | try instances of `Becoming.Revision`/`ContinuingRevision`, `Gated`, `Countdown` and `Assurance.trace_ofPartial_iff`; where the content is the protocol's own definition (what counts as harmful in one installation), say so as instance content rather than leave “partly general” | B |
| 14 | Copying residuals | `finite_lineage_inherits` has only its sufficient side; `registered_copy_cells` covers the product's tokens, not the chain's bonds | prove the converse or give its counterexample; extend to the bonds | B |
| 15 | “credit” as a reading's verb | The spine says a reading “credits” an event (Lean: `stepwise_credits_before_escalation`, `credited_before_loss`, `sharing_credited`, `stops_credited`, `finite_reading_credits_consumption`, `whole_run_credits_overdraw`, `stepwise_credits_substitution`; 149 records; 3 chapter uses). The plan's A4 replaced `credit` in ContinuingRevision as a market word | Ren chooses (§3) | C |
| 16 | Old machines keep market names | 879 Lean files carry such names, most of them frozen run copies (evidence, not to be edited); the live machines the spine now instances: StructuralCopying (`cost`, `charge`, `budget`, `spent`), RecurrentAssembly, CopyingRegistration, CopyingCorrection, RecoverableControl/EffectiveCommand (`charge`, `accounting`, `spend`) | Ren chooses (§3); recommended: leave old machines, guard new names (#17) | C |
| 17 | Nothing stops new market names | Two streams tonight inherited them from old machines; I caught them by reading | a name check: `check_becoming.py` warns on a spine declaration, and `research.py lint` on a schema-2 public field, using a short word list (cost, charge, budget, pay/paid, price except the Price equation, spend/spent, account, credit, fee, profit, fund) with an allowlist | C |
| 18 | Generativity chain: whole review pending | 94 fingerprinted sources changed (28 record JSON, 22 record pages, 17 chapters, 12 Lean, 3 overviews, 3 studies, 2 sources, 7 other), 38 new pages found by discovery (many are earlier reviews), 2 removed (MARKET-INTERNET-DEGENERATION.md, meta-attractor COMMON-ORGANIZATION.md); no entry cites a renamed name | §2, phase D | D |
| 19 | No independent review of tonight's laws | about 380 core theorems (Stock, Contacts, LossMatching, Assurance, Segmentation, Readout, Gated, Copying, Retrodiction, Viability, Countdown, Lasting, the additions to Joint, Substitution, Ranking, Continuation, bridges Instances and RenewalBridge) and about 190 peripheral (six instance modules); author verification only. Ren waived review once (P55: “no extra review needed”) | Ren chooses (§3) | E |
| 20 | 164 records still in schema 1 | 129 records have lint findings (973 warnings, no errors); 45 have ten or more (worst: becoming-stepwise-reading 25, more-needs-renewers 24, unceasing-generation-needs-renewal 24) | Ren chooses (§3); the ratchet keeps them from growing either way | F |

Closed while checking: the laws-of-one-step count (57 in English, 44 in Chinese and the receipt) went away in its migration, which states no count; `prepare_open_form_closure.py` matches an old heading, but it is a one-off landing script from 13 October, kept as evidence, and needs no change.

## 2. Phases

**A. Corrections (items 2–10).** Documentary; I do them myself, no agents, no Lean. Each record gets one paired history note; render, `research.py check`, lint `--changed-since`. One commit per item group.

**B. General laws, batch 4 (items 11–14).** Claim on the work board first. New core law: the reaching law (dual of Lasting's ladder), in `Becoming.Lasting`; the history-supplies-inputs law for scene, encounter and retrospective binding where the core can state it (the machines stay peripheral instances). Two Opus worktree agents: (i) items 11 and 14, (ii) items 12 and 13. I integrate on a `batch4` branch, run the core checker once and the affected peripheral checkers (MarketInstances, MachineInstances, CopyingInstances, ProtocolInstances, VersionedTaskInstances), rebind, land. Where a claim turns out to be genuinely about one machine or one history, the record says what the general law is and what the instance adds; nothing is relabelled general without a theorem.

**C. Names (items 15–17).** After Ren's choices. The “credit” rename, if chosen, rides with batch 4 (same checker run, rename table in unification plan §10, old receipts read through it). The name check (item 17) is tooling: tests in `tools/research/tests/`, `make research-test`.

**D. Generativity chain (item 18).** After B and C, so it is reviewed once. Per the [maintenance workflow](../../GENERATIVITY-CHAIN-INDEX-RECORD.md):
1. A script finds, for each changed source, the git version whose SHA-256 matches the chain's fingerprint and prints the diff.
2. Sort the diffs: history notes, hashes and rendering only; renames (the chain cites none); substantive changes (law-first claims, general laws, chapter text).
3. Read every substantive diff with its paired entry. Revise an entry only where it is now wrong or names a narrower result than the one it rests on, in both languages; record `--record-review` only for sources actually read.
4. Discovery: decide inclusion for the 38 new pages, find where the 2 removed pages went, `--record-discovery-review`.
5. One maintenance entry listing each revised entry; Ren sees that list, because the chain is Ren's curated argument view.

I can do this myself (read-heavy, about a day of reading at the current scale) or with one Opus agent and my review of its list.

**E. Independent review (item 19), if Ren wants it.** One independent Opus agent that wrote none of it reviews the batch 1–4 mathematics: statements against record claims, every “exactly when”, hypotheses doing work, counterexamples, names. Its corrections land as one batch with a checker run.

**F. Readability remainder (item 20), if Ren wants it.** Migrations as before (mapping table per record, snapshot, nothing dropped silently), seven or eight records per agent run.

**Order:** 1 (if yes) → A → Ren's choices → B with C → D → E → F. A needs nothing from Ren and can start at once.

## 3. Choices for Ren

| Choice | Options | Recommendation |
|---|---|---|
| Push now? | now / after A / later | now: main is checked and the remote is an ancestor |
| “credit” (a reading credits an event; 记入) | `includes` (“the events a reading includes”) / `counts` (collides with Counting) / keep | `includes`; zh 记入 unchanged |
| Old machines' market names | leave / rename the six live instanced machines (old receipts read through a table) | leave, and add the name check (item 17) |
| Independent review of batches 1–4 | yes, one agent / no | yes: the general laws are now the headline of about 40 records |
| Remaining schema-1 records | the 45 worst (about 6 agent runs) / all 164 (about 21) / ratchet only | the 45 worst |
| Chain entries | I revise wrong entries and list them for you / I only flag them | revise and list |

## 4. Cost

A: none beyond my session. B: two agents and one core checker run plus five peripheral runs (all reuse cached steps). C: folded into B; the name check is small. D: none or one agent. E: one agent. F: about six agents for the 45 worst. Nothing here needs a fan-out larger than two agents at once.
