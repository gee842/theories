# Plan: general laws, names and record readability

14 October 2026. **Status: proposal awaiting Ren; nothing here has landed.** AI-authored (Claude Opus 5.5 merge session with four Opus planning agents), at Ren's request:

> all needs to have general law proved, change bad names, and spawn a few agents to figure out how to address this: The records' claims and limitations have grown into long lists of caveats and are getting hard to read, then present me with a plan

This package preserves the agents' scratch work so it survives `/private/tmp`. The `.lean` files under `lean/` are scratch builds outside the Lean root, so no checker indexes them. Their audits (`lean/scratch-audit-*.json|txt`) come from `scratch_build.py`: they are not receipts, and the checker's environment audit, controls and prelude-only compile still have to run when the modules land.

## 1. General laws

### 1.1 Audit (records changed since 2026-10-12)

The audit read each claim against the statements of its bound declarations. The full table is in `general-law-audit/audit-table.md`.

| Class | Count | Meaning |
|---|---|---|
| G | 53 | the claim rests on laws over every process/world of its kind |
| G+W | 56 | general laws, with constructed examples only as controls or counterexamples (fine) |
| W | 5 | positive point rests only on constructed examples: P93's `Revising` part, P99 `ReferencePlan`, P103 `ContinuingRevision`, P100 `RepairComparison`, `learned-procedure-transmission` |
| borderline | 1 | `joint-difference-making`: the dichotomy is general, but "the difference belongs to the joint activity" is shown only in `Pool` |
| F | 2 | general only within one constructed family (the support-gated laws): `substitution-preserves-consumption`, `ranking-under-readings` |
| W-neg | 2 | proved by examples, but the point is a limit or counterexample (legitimate) |
| open | 3 | targets with no Lean claim |

The roughly 80 records older than 10-12 were not audited.

### 1.2 Already proved in scratch

All of the following build with `scratch_build.py`, with no `sorry`, no warnings and empty `#print axioms` reports.

**`Becoming.Support`** (imports only `Becoming.Flow`; 40 theorems / 51 declarations). These are process-level laws of drawing on what is held and replenishing it, for every `Process`, `Trace` and `Run`:
- `balanced_iff`: balance at each step is the same as balance along every course.
- `feasible_iff_covered`: a course is feasible exactly when at every prefix the start plus what was replenished so far covers what was drawn.
- `product_feasible_iff`: run jointly with a registration process, a course runs exactly when registration admits it and support covers it.
- `covered_of_trace`: every executed course is covered.
- `Run.replenishes_of_draws`: along every balanced run, drawing without end needs replenishing without end. `Run.draws_iff_replenishes`: with bounded support the two recur together.
- `cycles_need`: if every number of cycles can run, the return covers the draw. `repeat_covered_iff` / `product_repeat_iff`: repetition without end holds exactly when the first pass is covered and the return covers the draw.
- `carried_iff`, `Run.supportFlow_balances_iff`: the support along a run is a balanced `Flow`, so the existing Flow laws apply (one model, not a parallel one).

**`Becoming.Contacts`** (imports `Becoming.Revision`; 24 / 30). It reuses `Training.AgreeOn`, `Through` and `Registration.keeps_iff`.
- `through_data_iff`: registration by agreement on data can select an address's value exactly when the address is in the data.
- `keeps_data_iff` / `survive_data_iff`: changing the data keeps every old selection exactly when it keeps the old data.
- `answers_iff`: a revision rule registers every failure exactly when it puts the failed address into the next plan. `blind_misses`: a rule that ignores what failed leaves some failure unregistered at every plan once addresses are unbounded. `finite_blind_answers`: with finitely many addresses the converse fails.
- `References.drives_iff`: two reference responses drive a two-valued channel to both targets exactly when they differ. `References.stays_iff`: an installed key stays right exactly when the new channel agrees with the old at the keyed inputs.

**`Becoming.RevisionInstances`** (36 / 40). The three examples become instances:
- `Revising.step_iff`: P93's example is a registration process run jointly with a stock. `covered_not_enacted` and `linked_not_enacted` show, as laws, that discrimination, support and enactment are distinct.
- P99's controls become the failure directions of the laws above: the frozen plan is `blind_misses`, failed separation is the converse of `drives_iff`, drift is `inverted_fails`, and exhaustion is `covered_of_trace`.
- P103: `no_run_without_return` (no unending run at yield 0 under any controller; stronger than the old `cut_stops_next`). `renew_recurs` and `success_recurs` hold along every run. `repeats_iff`: for yields up to 9, the cycle repeats for every number of cycles exactly at yield 9.

**`Becoming.LossMatching`** (pure core; 34 / 42) and **`Becoming.RepairComparison`** (19 new theorems on top of the 17 old ones; 65 declarations). These are P100's general laws, for every `Frame`:
- `StrictLossMatch.trans` and `.mono`.
- `strictLossMatch_of_extension` and `SufficientMatching.comparison`: a generative extension is a match by identity, so P100's sufficiency commitment contains C.
- `SufficientMatching.not_mutual` and the `EndlessLosses` example: with infinitely many losses a configuration strictly matches itself, so finiteness is needed.
- `StrictLossMatch.length_lt`: with losses listed once, matching is a strict order.
- `strictLossMatch_iff_counts` (Y iff Z): with content read as a class, a strict match exists exactly when the better configuration loses no more in each class and fewer in total.
- `not_strictLossMatch_of_base_lost`: a configuration that loses the common support is strictly matched below nothing.
- `readsAt_iff_settled` and `ReadsAt.loss_retained`: a claim is read at its episode time exactly when it is settled from then on, and restoring support never re-realizes a missed claim.
- P100's repair process becomes an instance: `matches_iff`, with loss counts 3/4/3/2.

### 1.3 Still to prove

| Item | Proposed law | Size |
|---|---|---|
| `learned-procedure-transmission` | `expose_isSome_iff ↔ 0 < active ∧ demand ≤ source`; `reconstruct_isSome_iff ↔ tested ∧ 0 < capacity`; inheritance; support conserved across reconstruction | ~½ day |
| `joint-difference-making` | a set of parties makes the difference while no single member does, wherever withholding each member still breaks the dependence and withholding the set keeps it | small |
| P103 parameters | fuel and yield as parameters, so `repeats_iff` holds at every yield | 1–2 h |
| non-class content (P100) | Hall-type characterization; only the necessity direction is general now | open, optional |
| F-scoped records | e.g. `ConsumingIn` is kept under any change of dependence that keeps the draw on the consumed condition | needs Ren's go |
| records before 10-12 | the same audit; prove any W found | ~1 session for the audit |

### 1.4 Records

Each affected claim is rewritten law first, with the old example kept as an instance or control and the new bindings added. No status changes: P100 stays reviewed-scoped because FR is a normative commitment, and the laws only state its exact content.

## 2. Names

The working data is in `names/` (`flagged.txt` and `counts.txt` hold every reference). The audit window starts at main `355ca27b`, the last main commit before 10-12; it covers 62 Lean modules (39 new) and 51 new records. The criteria come from Ren's 10-06, 10-10 and 10-12 sources and the P36 precedents.

### 2.1 Renames (Lean; statements and proofs unchanged)

| # | Current | Problem | Proposed |
|---|---|---|---|
| A1 | `Person` (`focal`, `peerOne…`), `owner`, `personClaim` (RepairComparison) | person, ownership and social framing | `Life` (`p q r s`), `lifeOf`, `firstEpisodeOf` (or `Position`) |
| A2 | `Loop.own` (Response, Counterfactual) | ownership | `Loop.paired` |
| A3 | ReferencePlan `cost`, `spent`, `receipt`, `step_account`, `trace_account`, `actual_cost_without_reset`, `references_paid_before_exhaustion`, `constant_channel_contacts_paid`, `erased_receipt_cannot_activate`, `propose_from/without_receipt` | market words (Ren 10-06: 付费记录 "太市场了，不够基本"); `receipt` collides with checker receipts | `use`, `used`, `mismatch`, `step_conserves`, `trace_conserves`, `fuel_used_without_reset`, `references_use_fuel_before_exhaustion`, `constant_channel_contacts_use_fuel`, `erased_mismatch_cannot_activate`, `propose_from/without_mismatch` |
| A4 | ContinuingRevision `credit`, `cost`, `no_unearned_return`, `*_account`; its docstring speaks of a "right … earned" | credit, earning and rights | `enabled`, `use`, `no_return_without_success`, `*_conserves` / `all_cycles_amounts` |
| A5 | `error_budgets_require_reach`, `…_timed_reach`, `unreached_by_deadline_coverage_eq_errors` (FallibleInquiry) | budget (P35 precedent), deadline | `error_bounds_require_reach`, `…_timed_reach`, `unreached_in_time_coverage_eq_errors` |
| A6 | `Delayed.commandAt` (TimedResponse) | command | `Delayed.sourceAt` |
| A7 | `Flow.FollowsGift`, `carried_of_gift_exceeds`, `spent_keeps_nothing` (Feeding) | gift (P36 renamed it), spent | `FollowsGiven`, `carried_of_given_exceeds`, `depleted_keeps_nothing` |
| A8 | `reform_reabsorbed`, `reform_drawnInto`, `state_reform_*`, `rule_reform_*` (Capture, Branching) | political word | `…perturbation…` |
| A9 | constructor `needy` (Persistence, Identity) | poverty word | `consumer` |
| A10 | `Diversion.restrained`, `restrainedLevel`, `restrained_balances` (Selection) | moral restraint | `undiverted…` |
| A11 | `Frame.unclaimed` (Bridge) | ownership sense | `Frame.bare` |
| B1 | `MakesSense`, `makesSense_iff`, `still_makes_sense`, … (Description) | a formal name taken from Ren's own words | `IdentifiesAlike` (the definition is `π s = π s' ↔ Alike F F s s'`) |
| B2 | `Identification.knowing`, `knowing_right`, `knowing_earliest` | names a state of mind | `withBound`, `withBound_exact`, `withBound_earliest` |
| B3 | `Denial`, `denial_never_rests`, … | psychological | `Negation`, `negation_never_rests`, … |
| B4 | `separation_surplus` | economic | `separation_admits_extra` |
| B5 | `Interference.truncation_misleads` | treats the truncation as an agent | `truncation_misses_cancellation` |
| N | new scratch names: `trace_account_of_law`; `Support` (close to `Web.Supported`) | as A3; possible confusion | `trace_conserves_of_law`; `Support` or `Stock` |

### 2.2 Titles and public text

**Record titles** (IDs stay stable):
- `target-capture`: "reforming" → "perturbing".
- `identification-where-bounded`: "knows the bound" → "given the bound" / 给定界的.
- `finite-aggregation-…`: drop "FR candidate" from the title.
- `recurring-reference-revision`: zh/en mismatch; 再生产 → 活动形成并重现参考修订.
- `seeking-boundary`: lead with the structure, keep 无明 as an alias (Ren's choice).

**Process jargon in public text:**
- P-number leads in the spine module table (`P93：`, `P99：`, `慧根接通：P91/P93`, "(P72q，由 P64–P68 的所有者写成)").
- Headings "6.13 …（P56）" and "6.14 …（P91）".
- 劫持 → 捕获 in the Capture row; 强化俘获 → 捕获; 资格 → 条件; 累计支承账 → 累计支承量; "deadline discrimination" → "discrimination by the answer time".
- P-numbers and Ren quotes in Lean docstrings move to the studies.

### 2.3 Kept

- `Transfer`, `conveyor`, `Delayed`; `give`/`take`/`givers`/`takers`/`renewers`.
- The biology and demography words P36 kept (`child`, `Lineage`, `forager`, `census`, …).
- `Capture` and `escalation` (dynamics and systems terms).
- `policy`, `favours`, `share_rises`, `Seeking`, `AboveAll`, `yield`, `fuel`.
- The `Quantum` module name: renaming it would change paths and receipt keys; only "(P72q)" goes.

Older than the window, and in this pass only if Ren widens it: `KeepsTenure`, Part II `Standpoints.own` / `Metaethics.own`, the titles of `own-count-misses-joint-excess` and `ranking-under-readings` (which use "winning" and "restraint"), and 原资金法则.

### 2.4 Execution

1. Add an old→new table after P36's in BECOMING-UNIFICATION-PLAN §10, plus a short study note.
2. Rename only, in one Lean batch with the new laws.
3. Replace the old names outright in record `aliases`, as P36 did, and add one history note per touched record.
4. Re-point the proof bindings to the new receipts. Historical receipts, run folders and landing packages stay byte-unchanged.

## 3. Record readability

### 3.1 Diagnosis

There are 202 records. Median claim length is 1,164 English characters (p90 3,834; max 13,172), and 105 claims exceed 1,000. Limitations have a median of 356 and a maximum of 4,834. 98 titles are longer than 120 characters, because they carry the whole statement.

Growth: wisdom-root's limitations went from 249 characters (10-09) to 4,834, and its validation scope from 271 to 5,529. The 10-14 jump is the merge of the 10-13 rounds, each of which appended a boundary sentence, a receipt paragraph and a section mapping.

In the 96 labelled sentences of the worst records:

| Share | Kind |
|---|---|
| ~58% | substantive: 38% non-implications or counterexamples, 10% premises, 10% limits of correspondence to reality |
| ~37% | noise: restated status, round narration, repeated standard boundaries, duplicates |

The main failure is that boundaries from up to 16 rounds sit unsorted in one block of negations, with no sentence first saying what the result does.

There are two patterns:
1. In the 16 target, assessment and argument records, each round appends to every free-text field.
2. In ~105 spine records, the claim is a catalogue: every law with its Lean names, and the title is the whole statement.

### 3.2 Design ("schema 2", alongside schema 1 until migration ends)

Every field stays a zh/en pair.

| Field | Content |
|---|---|
| `title` | a short name (≤100 en / 40 zh characters) |
| `statement` | new: one or two positive sentences saying what the result does (≤300); no Lean names, P-numbers or receipts |
| `claim` | the exact statement |
| `laws` | optional: one law per item with its declarations, checked against references |
| `hypotheses` | unchanged |
| `does_not_show` | replaces limitations: one sentence per item, typed as non-implication, converse, correspondence or scope, with an optional witness |
| `standard_boundaries` | keys into one shared bilingual file (11 drafted, e.g. discrete-steps, decidability, formal-not-empirical, omission-not-refutation, conditional-not-universal) |
| `not_required`, `progress` | for targets: what the target does not ask; one line per completed connection, with an anchored study link |
| `validation_scope` | one paragraph (≤600); round-by-round receipt narration moves to history |
| `text_versions` | hash-bound snapshots of the old bytes |

**Render:** statement first, then progress, exact claim or laws, conditions, does_not_show and counterexamples, the standard boundaries on one line, evidence and next step. Correspondence, dependencies, sources and history fold into one collapsed block.

**Lint, run by `research.py check`:** process markers in public fields, restated status, a title that is a statement, a negative opening, boilerplate written out instead of a key, three or more rounds cited in one field, and over-length fields. Hard errors only for title, statement, validation_scope, next_delta and process markers; other caps only warn.

A **ratchet** on changed records stops schema-1 records from growing until they are migrated.

On today's records the prototype lint flags 142 of 202 records (1,519 findings). The prototype passes the 49 existing tests plus 10 new ones on a copy of the tools.

### 3.3 Prototype rewrites (`readability/drafts/`)

Each draft comes with a sentence-by-sentence mapping table; every old sentence lands in a new field, a standard key, history or the snapshot.

| Record | Limitations → does_not_show | Page above the collapsed block |
|---|---|---|
| wisdom-root | 4,834 → 918 (+13 progress lines) | 43.4k → 11.5k |
| scientific-inquiry-foundation | — | 12.3k → 7.5k |
| finite-aggregation | — | 14.7k → 9.7k (mostly genuine premises and counterexamples, which stay) |

### 3.4 Migration

Per record:
1. Claim it on the work board and reread its current bytes.
2. Snapshot the old text.
3. Generate a mechanical draft.
4. Read it with the study open: classify the items, pair zh/en and write the statement.
5. Add a history note and refresh `reviewed_at_utc`. No Lean run is needed.

| Category | Records | Estimate |
|---|---|---|
| short theorems | 81 | ~10 h |
| catalogue theorems | 105 | ~45 h |
| targets and arguments | 16 | ~18 h |
| tooling | — | ~1 session |

The generativity chain fingerprints 49 records; each batch needs one documented reconciliation there.

## 4. Order of work

1. **Tooling (one session).** Land schema 2, the lint, the ratchet, the render and the guide, then run `make research-test`. Once it is in, every record touched later is written once, in the new form.
2. **One Lean batch.** Land the general laws (Support, Contacts, LossMatching, the instance theorems in Revision/ReferencePlan/ContinuingRevision/RepairComparison) together with the renames A1–A11 and B1–B5. Each checker runs once: core with bridge, FallibleInquiry, CorrectionInquiry.
   - Prerequisites: claim on the board, a worktree from clean main, and `scratch_build.py` first.
   - After the checks: update spine §9, the old→new table and the affected records (law first, schema 2).
3. **Remaining laws.** learned-procedure-transmission, joint-difference-making, P103 parameters; then the F-scoped lifts if Ren agrees.
4. **Migration tranche one.** The 16 targets and arguments plus the worst 15 records; then the rest at the pace Ren chooses.
5. **Audit before 10-12.** Audit the older records for example-only results and prove any found.

## 5. Choices for Ren

1. **Scope of "all":**
   - Also audit and generalize the ~80 records older than 10-12? (Recommended: yes.)
   - Lift the two family-scoped results into Part I? (Recommended: yes, where the law exists.)
2. **Names:**
   - A1: `Life` or `Position`.
   - B1: rename `MakesSense` → `IdentifiesAlike`? (Recommended: yes; "the split that makes sense" stays as the prose reading.)
   - The new module: `Support` or `Stock`.
   - P-numbers in public headings and the module table: move them to provenance? (Recommended: yes.)
   - `seeking-boundary`: lead its title with the structure? (Recommended: yes, keeping 无明 as an alias.)
3. **Readability:**
   - Field names: statement/陈述, does_not_show/未表明, not_required/不要求, progress/已接通.
   - Short titles for the ~103 spine records? (Recommended: yes.)
   - Pace: a dedicated pass for tranche one plus the ratchet for the rest (recommended), or a full pass of ~70–80 agent-hours.
   - Make "No ethical premise and no Lean axiom is used" (now in 41 claims) a standard key? (Recommended: yes.)
