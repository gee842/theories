# 按成果接续研究 / Contributing through canonical results

8 October 2026. AI-authored implementation of [Ren's request](../sources/15-codex-theory-conversations/2026-10-08-result-centered-repository.md). This changes research coordination, not the governing research goals or proof standards.

## Where the current claim lives

For each migrated claim, edit its one JSON record in [results/records](../theories/becoming/results/records). The [register](../RESULTS.md) and matching Markdown pages are generated reading views. The record states the claim, assumptions, interpretation, evidence, status, dependencies, boundaries, aliases and next substantive delta. Proofs remain in their existing modules; arguments remain in their existing theory chapters and studies. Records point to them rather than copying whole arguments or proofs.

每项已迁移主张只有一个可编辑 JSON 记录；登记表与阅读页自动生成。原理论、研究、证明和回执继续保存。登记的是特定范围内的主张，不是把整个会话或一个宽泛主题当成一条定理。

Authority is scoped: a record controls the maintained summary and reuse identity of its migrated claim. It does not overrule contradictory source evidence, Ren's instructions or independent authorized goals. Source drift suspends a claim of current documentary agreement; read and reconcile the change. Unmigrated claims retain their existing canonical chapters and studies. The initial register is a bounded migration, not a claim that every historical proof has been semantically deduplicated.

## Before starting or continuing a study

1. Read the repository entry points and governing method. Search the register by claim, supplied premises and theorem aliases; inspect the linked sources. Search existing studies and Lean declarations too, because migration is incomplete.
2. Name the result ID(s) being reused and the exact new contribution in the existing study note: stronger conclusion, weaker premise, new correspondence, application, counterexample, correction, or a previously missing composition. For an unmigrated claim, identify its source and migrate it when this study substantively changes it. Do not create a new study copy solely to obtain a fresh session workspace.
3. State the output-to-input connection being addressed and what would change the account. A new source survey, recheck, proof wrapper, notation change or repeated acceptance is provenance/evidence for the same result unless it changes substantive content.

开始前检索已有主张及别名；在现有研究记录中写明复用 ID、新增量、剩余前提和能改变判断的结果。已完成机制直接复用；历史“下一步”不自动恢复为当前任务。

Use this short block inside the existing study, not a new report on every turn:

```text
Result(s): existing IDs, or the canonical source awaiting migration
Delta: what this contribution adds or changes
Supplied premises / correspondence: what remains assumed
Evidence: exact proof declarations + source-bound receipt, argument review, or empirical record
Boundary: retained counterexample or the scope that is still unmet
Integration: which existing record changed; which output now meets which input
```

## One identity, explicit relationships

| Contribution | Record action |
|---|---|
| Alias, wrapper, recheck, repeated acceptance | Add alias/evidence/history to the same record; do not count another result. |
| Same claim with better evidence or corrected exposition | Update the same record; preserve the earlier source/receipt and explain the correction in history. |
| Stronger theorem or weaker hypotheses | Give the substantively different claim its own ID; retain and link the narrower result. Supersede only when the earlier claim/status is actually replaced. |
| Application | Link the reused result with `application`; name the real correspondence and added premises. |
| Formal composition | Use `formal-reuse` only for a verified inference using the cited result. Identify the producer output, consumer input, preserved hypotheses and connecting declaration/receipt. |
| Conceptual connection | Use `interpretive` for an argument dependency, or `related` for analogy. Neither is a checked adapter. |
| Counterexample or failed candidate | Preserve the case and its target scope. Revise or withdraw the affected claim without erasing its history. |

相同声明文字可能引用不同命名空间、定义和测试范围，不足以判定重复。多个局部结果分别成立，也不等于已有同一历史中的组合证明。规范根据、识别、动机、实际执行及持续保存各保留自己的推论责任。

## Update and verify

Edit the affected `records/<id>.json` in a directory listed in `_process/research-config.json`. Shared tools live in `tools/research/`; old dated commands remain compatibility entry points. Two schemas validate side by side: schema 1, demonstrated by the seeded records, and schema 2, in which new and migrated records are written ([Writing a record](#writing-a-record-schema-2)). All substantive summaries are paired Chinese/English. IDs are stable semantic names, not dates or session IDs. `canonical_source` and every boundary must refer to a listed source. Record formal names as aliases where they denote the same result; do not use an entire module as an alias for one lemma.

`recorded-checked` requires a proof source and a successful existing receipt with an exact source-hash field. `reviewed-scoped` requires a substantive statement and review. `open` is an unmet target, not a failed local theorem. The source hashes record what was read; they must never be refreshed just to silence a check. When a source changes, inspect its diff and full relevant context, revise the claim/scope if needed, then update that record's hashes and history. Preserve old scientific receipts rather than editing them to match new bytes. A changed mathematical claim requires the actual Lean check directed by Ren. Documentary reorganization alone does not require a new proof run. `reviewed_at_utc` is the documentary review time: refresh it whenever the author revises a record's content (claim, premises, correspondence, limitations, counterexamples, related notes or next step); re-pointing a validation scope to a newer receipt, with the content unchanged, does not refresh it.

```sh
make research-find QUERY=support
make research-render
make research-check
python3 -B tools/research/research.py check --ids joint-plan-composition
python3 -B tools/research/research.py check --changed-since HEAD
python3 -B tools/research/research.py lint --ids joint-plan-composition
```

A stale record keeps its earlier reading page; healthy records and the shared indexes can still render. Exit 1 means invalid metadata, an unincorporated concurrent edit, or outdated rendering; exit 2 means source drift in the selected records. Other records’ drift is reported separately. Changed-file selection follows result dependencies as well as direct source references. No hashes are refreshed automatically. The checker verifies structural requirements, references, declaration presence, receipt hash bindings, unique aliases, dependency cycles and generated views. It does not prove semantic equivalence, audit every transitive import or establish the substantive warrant of premises. New hypotheses hidden inside definitions remain a human/research review obligation.

For supersession, keep the old record with `status: superseded` and `superseded_by: <id>`. Record the precise replacement scope and preserve the old evidence. `withdrawn` needs an explanation in history and a linked boundary; it never deletes the counterexample.

### Lead the README with significant completed results

Maintain the ordered `readme_featured_results` list in `_process/research-config.json`. Each selected record must have status `recorded-checked` or `reviewed-scoped` and an `overview` object with bilingual `title`, `summary` and `evidence` fields. The English fields lead the root README; both languages appear on the record's generated page for review. Keep the summary faithful to the claim's explicit premises and validation scope, and distinguish checked inference from philosophical argument. Selection and renaming do not create another result or strengthen an existing proof. Render and check through the normal commands; do not edit the generated README directly.

The optional ordered `readme_research_goals` list selects existing scoped goals for the README's ongoing-research section. Give each selected goal an `overview` with bilingual `title`, `summary` and `next_step`; retain its existing authorization, premises and completion criteria. English summaries appear in the README and both languages in the generated scope views. Established-result links are derived from that goal's `result_ids`, including only `recorded-checked` and `reviewed-scoped` results. Do not add a parallel scientific-status field to goals or present open targets as achievements; this navigation does not perform new scientific validation.

## Writing a record (schema 2)

先说成果做了什么，再说它的确切条件；只写定理或论证实际承担的边界。轮次编号、章节号、回执时间、会话与“本轮未新增”之类说明属于沿革与证据，不进入公开字段。新增边界时替换或并入已有条目，不在末尾追加；每轮的说明写进 `history`。迁移旧记录时先保存原始字节快照，逐句映射到新字段、通用边界、沿革或快照，再写一条沿革。字段名：`statement` 陈述、`does_not_show` 未表明、`not_required` 不要求、`progress` 已接通。

Say what the result does, then its exact conditions. Write only the boundaries the theorem or argument actually carries. Schema 2 (`"schema_version": 2`) applies to every new record and to every record migrated from schema 1; schema-1 records keep validating unchanged until they are migrated. Every text field is a zh/en pair, and every list item is paired.

| Field | What goes in it | Limit (en / zh characters) |
|---|---|---|
| `title` | A short name, not the statement. | 100 / 40 **(error)** |
| `statement` | What the result does, or what the target asks, in one or two positive sentences. No Lean names, round numbers, sections, dates or receipts. Rendered first, under the title. | 300 / 150 **(error)** |
| `claim` | Optional: the exact statement with its conditions written in, when `statement` is not already exact. | 1500 / 700 |
| `laws` | Optional: one law per item with `declarations`, each a declaration named in `references`. A family of laws goes here, not into `claim`. | 420 / 190 each |
| `hypotheses` | Premises the result uses: logical commitments, supplied laws, normative commitments, correspondence assumptions. | 420 / 190 each, 9 items |
| `does_not_show` | Replaces `limitations`. Substantive non-implications only, one sentence each, typed by `kind`: `non-implication`, `converse`, `correspondence` or `scope`. An optional `witness` names a declaration in `references` or an alias. | 240 / 110 each, 8 items |
| `counterexamples` | Witnessed cases with their hashed source, as in schema 1. A record needs counterexamples or `does_not_show`. | — |
| `standard_boundaries` | Keys of boundaries shared by many records, defined once in the file named by `standard_boundaries` in `_process/research-config.json`. Cite a key instead of writing its sentence out. | — |
| `not_required` | Targets: what the target does not ask. | 200 / 90 each, 6 items |
| `progress` | Targets, assessments, arguments: one line per completed connection, with its boundary; `source` is a hashed reference, optionally with an anchor (`path#anchor`) that must exist. | 240 / 110 each, 16 items |
| `validation_scope` | The current evidence in one paragraph: the kind of evidence and where its receipts are. | 600 / 260 **(error)** |
| `next_delta` | The next substantive step, stated positively. | 400 / 180 **(error)** |
| `correspondence` | As in schema 1; rendered inside the folded block. | 1200 / 500 |
| `history` | Everything about rounds: who asked and when, which round number or section, which receipt, what was reused or not recounted. | — |
| `text_versions` | Hash-bound snapshots of the record's earlier bytes: `path`, `sha256` and a paired `note`. | — |

Other fields (`id`, `kind`, `status`, `family`, `reviewed_at_utc`, `canonical_source`, `aliases`, `dependencies`, `related`, `references`, `proof_bindings`, `overview`) keep their schema-1 meaning and checks. The [migration drafts](research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-general-laws-plan/readability/drafts) show three complete schema-2 records with their sentence-by-sentence mapping tables (examples, not installed records).

**Never in the public fields** (`title`, `statement`, `claim`, `laws`, `does_not_show`, `not_required`, `progress`, `counterexamples`, `next_delta`, `overview`):

- round numbers (P92), section numbers (§29, Section 11), dates, receipt timestamps (20261013T125626Z), session ids ([1c3084]) or round narration ("this round", "has landed", 本轮, 已落地);
- the status in other words ("remains open", "is unproved"): the `status` field says it;
- "no new theorem / Lean run / experiment / independent review": that is `validation_scope`;
- another record's status or scope: link it as a dependency or related result;
- instructions to later sessions ("do not reopen"): those go on the [work board](BECOMING-WORKBOARD.md).

**Replace, do not append.** When a round adds a boundary, reread the existing items. Fold the new sentence into the item it refines, or replace the item it supersedes, and record the change in `history`. Each round leaves one paired history note; receipts stay in `references` and `validation_scope` names where they are, without a paragraph per round. For a target, a completed connection becomes one `progress` line with an anchored link to the study section that holds its argument. The snapshot and git keep every earlier wording.

**Shared boundaries.** The [shared boundary file](../theories/becoming/results/data/standard-boundaries.json) holds each sentence once, in both languages, with its source. Cite a key only where the sentence is true of the record; `no-ethical-premise` ("No ethical premise and no Lean axiom is used.") only where the hypotheses contain no ethical premise and the bound receipts report empty axioms for the cited declarations. Changing a text there changes every citing page, so it needs the same review as a record; add a key when a boundary recurs across records.

**A short title for a schema-1 record.** Schema 1 also accepts an optional `statement`, rendered first, right under the title, and checked as strictly as in schema 2. A long title can thus become a short name, with its old text kept as the statement, before the full migration.

**Migrating a schema-1 record.**

1. Claim the record on the [work board](BECOMING-WORKBOARD.md), reread its current bytes and `git diff`.
2. Run `python3 -B tools/research/research.py snapshot <id>`. It stores the exact current bytes at `_process/architecture/history/<sha256[:16]>/<id>.json`, next to the preserved overview editions (the directory is `record_snapshots` in `_process/research-config.json`), refuses to overwrite a differing copy, and prints the `text_versions` entry. Add that entry to the record.
3. Set `"schema_version": 2`, write the short title and the statement, and map every old sentence to a field, a shared key, `history` or the snapshot. Keep the mapping table in the study that owns the record; nothing is dropped silently.
4. Add one history note and refresh `reviewed_at_utc`. A documentary migration needs no Lean run; source hashes are not refreshed by it.
5. Run `make research-render`, then `python3 -B tools/research/research.py check --ids <id>` and `lint --ids <id>`. If the [generativity chain](../theories/becoming/results/GENERATIVITY-CHAIN.md) fingerprints the record, reconcile it through its own workflow, once per batch.

**Checks.** `research.py check` runs the readability lint. For schema 2, the caps marked *error* above, process markers in public fields and three or more rounds or sections cited in one field are errors; the other caps, a written-out shared boundary, a restated status, an evidence disclaimer in a public field, a negative opening of the statement and items longer than two sentences warn. Every finding on a schema-1 record warns, except on its optional `statement`; README `overview` fields always warn. Warnings never change the exit status: `check` reports their counts under `style_warnings`, and `research.py lint` lists them. `check --changed-since <commit>` also runs the growth ratchet: a changed schema-1 record whose `limitations`, `validation_scope` or `correspondence` is longer in either language than at that commit fails; migrate it to schema 2 first. A new record written in schema 1 warns. The lint judges form only; whether a boundary is substantive is the author's reading.

## Integration and concurrent sessions

At study closure update the affected record and substantive theory chapter/study. Do not append status to generated README, RESEARCH, ROADMAP, CLAIMS, OPEN-QUESTIONS or foundation-index pages. Run `make research-render` to derive their navigation from records and scoped authorizations. Complete earlier text is preserved in linked historical reading editions, including original section anchors. Add new research authorization to the appropriate `_process/goals/<id>.json`; scientific status belongs only to result records. Update the [generativity chain](../theories/becoming/results/GENERATIVITY-CHAIN.md) only when its scientific content changes, following its own bilingual/hash workflow. The full catalogue remains a reading guide; the [session map](../theories/becoming/results/SESSION-RESULTS.md) remains a dated provenance map. Neither becomes a second editable claim register.

Multiple sessions may add different record files concurrently. Before editing a shared record, reread its current bytes and `git diff`; reconcile new evidence rather than replacing another session's update. Before committing, inspect status and review only owned changes unless Ren explicitly authorizes a whole-repository checkpoint. After integration, inspect changes since the starting commit for new work. Report incoming work with its paths and scope; do not silently absorb unfinished proofs, refresh their hashes or mark them accepted. Finishing a structural task does not authorize an endless research or monitoring loop.

If a session appended prose to a generated view, read and reconcile it into the relevant existing source/record, then use `python3 -B tools/research/research.py preserve-view <path> --note '<review and integration scope>'`. Every prior snapshot remains hash-bound. The render command serializes cooperating writers, checks metadata/source changes during rendering, and refuses unincorporated output changes. It cannot prevent arbitrary editors from changing a file after a check; rerun after new work arrives.

合并时保留其他会话改动；科学证据的状态优先于登记表标签。跨会话整合要指出已经接通的推论及仍缺的对应，不能以新增索引或更多文件冒充理论完成。

## Shared validation and discovery

`make research-check` validates the configured registry, scoped goals, generated navigation, local targets, original-byte preservation and declared receipt bindings. GitHub Actions runs the same check and `make research-test`. CI does not build every Lean package or accept a scientific result. For mathematical changes, continue the existing source-bound Lean workflow.

`make research-find QUERY=topic` searches canonical claims first, then active theory, studies and working sources, excluding frozen copies and attempts. Use `python3 -B tools/research/research.py find topic --archives` for deliberate historical discovery. `make research-imports` emits textual import candidates with ambiguous/unresolved names separated; it does not infer a conceptual composition from an import.

Dependency records can include an `interface` with paired `output`, `input` and `conditions` plus a reviewed `evidence` path. Preserve whether the edge is formal reuse, application or interpretation. Reference the exact existing connecting declaration in the reviewed source; adding metadata does not establish a new mathematical bridge.
