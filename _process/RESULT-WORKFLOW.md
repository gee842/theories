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

Edit the affected `records/<id>.json` in a directory listed in `_process/research-config.json`. Shared tools live in `tools/research/`; old dated commands remain compatibility entry points. Its schema is demonstrated by the seeded records; all substantive summaries are paired Chinese/English. IDs are stable semantic names, not dates or session IDs. `canonical_source` and every boundary must refer to a listed source. Record formal names as aliases where they denote the same result; do not use an entire module as an alias for one lemma.

`recorded-checked` requires a proof source and a successful existing receipt with an exact source-hash field. `reviewed-scoped` requires a substantive statement and review. `open` is an unmet target, not a failed local theorem. The source hashes record what was read; they must never be refreshed just to silence a check. When a source changes, inspect its diff and full relevant context, revise the claim/scope if needed, then update that record's hashes and history. Preserve old scientific receipts rather than editing them to match new bytes. A changed mathematical claim requires the actual Lean check directed by Ren. Documentary reorganization alone does not require a new proof run. `reviewed_at_utc` is the documentary review time: refresh it whenever the author revises a record's content (claim, premises, correspondence, limitations, counterexamples, related notes or next step); re-pointing a validation scope to a newer receipt, with the content unchanged, does not refresh it.

```sh
make research-find QUERY=support
make research-render
make research-check
python3 -B tools/research/research.py check --ids joint-plan-composition
python3 -B tools/research/research.py check --changed-since HEAD
```

A stale record keeps its earlier reading page; healthy records and the shared indexes can still render. Exit 1 means invalid metadata, an unincorporated concurrent edit, or outdated rendering; exit 2 means source drift in the selected records. Other records’ drift is reported separately. Changed-file selection follows result dependencies as well as direct source references. No hashes are refreshed automatically. The checker verifies structural requirements, references, declaration presence, receipt hash bindings, unique aliases, dependency cycles and generated views. It does not prove semantic equivalence, audit every transitive import or establish the substantive warrant of premises. New hypotheses hidden inside definitions remain a human/research review obligation.

For supersession, keep the old record with `status: superseded` and `superseded_by: <id>`. Record the precise replacement scope and preserve the old evidence. `withdrawn` needs an explanation in history and a linked boundary; it never deletes the counterexample.

### Lead the README with significant completed results

Maintain the ordered `readme_featured_results` list in `_process/research-config.json`. Each selected record must have status `recorded-checked` or `reviewed-scoped` and an `overview` object with bilingual `title`, `summary` and `evidence` fields. The English fields lead the root README; both languages appear on the record's generated page for review. Keep the summary faithful to the claim's explicit premises and validation scope, and distinguish checked inference from philosophical argument. Selection and renaming do not create another result or strengthen an existing proof. Render and check through the normal commands; do not edit the generated README directly.

The optional ordered `readme_research_goals` list selects existing scoped goals for the README's ongoing-research section. Give each selected goal an `overview` with bilingual `title`, `summary` and `next_step`; retain its existing authorization, premises and completion criteria. English summaries appear in the README and both languages in the generated scope views. Established-result links are derived from that goal's `result_ids`, including only `recorded-checked` and `reviewed-scoped` results. Do not add a parallel scientific-status field to goals or present open targets as achievements; this navigation does not perform new scientific validation.

## Integration and concurrent sessions

At study closure update the affected record and substantive theory chapter/study. Do not append status to generated README, RESEARCH, ROADMAP, CLAIMS, OPEN-QUESTIONS or foundation-index pages. Run `make research-render` to derive their navigation from records and scoped authorizations. Complete earlier text is preserved in linked historical reading editions, including original section anchors. Add new research authorization to the appropriate `_process/goals/<id>.json`; scientific status belongs only to result records. Update the [generativity chain](../theories/becoming/results/GENERATIVITY-CHAIN.md) only when its scientific content changes, following its own bilingual/hash workflow. The full catalogue remains a reading guide; the [session map](../theories/becoming/results/SESSION-RESULTS.md) remains a dated provenance map. Neither becomes a second editable claim register.

Multiple sessions may add different record files concurrently. Before editing a shared record, reread its current bytes and `git diff`; reconcile new evidence rather than replacing another session's update. Before committing, inspect status and review only owned changes unless Ren explicitly authorizes a whole-repository checkpoint. After integration, inspect changes since the starting commit for new work. Report incoming work with its paths and scope; do not silently absorb unfinished proofs, refresh their hashes or mark them accepted. Finishing a structural task does not authorize an endless research or monitoring loop.

If a session appended prose to a generated view, read and reconcile it into the relevant existing source/record, then use `python3 -B tools/research/research.py preserve-view <path> --note '<review and integration scope>'`. Every prior snapshot remains hash-bound. The render command serializes cooperating writers, checks metadata/source changes during rendering, and refuses unincorporated output changes. It cannot prevent arbitrary editors from changing a file after a check; rerun after new work arrives.

合并时保留其他会话改动；科学证据的状态优先于登记表标签。跨会话整合要指出已经接通的推论及仍缺的对应，不能以新增索引或更多文件冒充理论完成。

## Shared validation and discovery

`make research-check` validates the configured registry, scoped goals, generated navigation, local targets, original-byte preservation and declared receipt bindings. GitHub Actions runs the same check and `make research-test`. CI does not build every Lean package or accept a scientific result. For mathematical changes, continue the existing source-bound Lean workflow.

`make research-find QUERY=topic` searches canonical claims first, then active theory, studies and working sources, excluding frozen copies and attempts. Use `python3 -B tools/research/research.py find topic --archives` for deliberate historical discovery. `make research-imports` emits textual import candidates with ambiguous/unresolved names separated; it does not infer a conceptual composition from an import.

Dependency records can include an `interface` with paired `output`, `input` and `conditions` plus a reviewed `evidence` path. Preserve whether the edge is formal reuse, application or interpretation. Reference the exact existing connecting declaration in the reviewed source; adding metadata does not establish a new mathematical bridge.
