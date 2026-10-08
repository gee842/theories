# Repository architecture repair / 仓库架构修正

8 October 2026. Implementation of [Ren's architecture request](../../sources/15-codex-theory-conversations/2026-10-08-repository-architecture-repair.md). This is a structural repair record, not another scientific result register.

| Problem | Implemented repair |
|---|---|
| Competing current-status summaries | Eleven current overviews are generated from canonical result records and scoped goals. Update the source record, then render. |
| Shared tools buried in a dated study | Shared implementations now live in [tools/research](../../tools/research/README.md). Five older build commands remain importable wrappers. Active studies and experimental packages stay in place. |
| Session objectives mixed into global instructions | [AGENTS.md](../../AGENTS.md) retains permanent method and contribution rules. Nine authorization records generate [GOALS.md](../../GOALS.md); original detailed directives remain preserved. |
| Weak result identity and connection visibility | [RESULTS.md](../../RESULTS.md) reads the individual records; [DEPENDENCIES.md](../../DEPENDENCIES.md) renders typed relationships and explicit producer/output, consumer/input, retained-condition and evidence contracts where recorded. New connections retain their existing proof scope. |
| Frozen copies dominate discovery | `make research-find QUERY=topic` searches canonical claims and active sources. Historical evidence requires `--archives`. `make research-imports` separates textual candidates from unresolved module names. |
| No shared checks or safe rendering | Root Make targets, GitHub Actions, focused drift checks, source-bound receipt validation, local links/anchors, preserved-byte hashes, input-change checks, serialized rendering and per-output overwrite guards are in place. |

当前概览由成果与授权记录生成，不再由各会话反复追加竞争的状态段落。稳定工具与旧命令兼容；完成范围、原反例、原证明与实际工作位置保持。检索区分工作源码和冻结证据，依赖区分正式复用、应用、解释及关联。

## Preservation and reconciliation

[history-manifest.json](history-manifest.json) binds exact previous bytes and separately labelled, link-adapted reading editions. Its `prior_versions` and reconciliation notes preserve additions that arrived during the repair. Original heading anchors remain available through generated historical links. This includes the complete earlier README, RESEARCH, BRIEF, instructions, theory entry point, roadmap, study index, open questions and claim ledger.

One temporary generated result page became orphaned when its concurrent author removed the editable record. The page's original bytes and reading edition remain in the manifest; only the orphan generated page was retired. Its supporting theorem remains in the unchanged scientific source. No proof source, counterexample or scientific receipt was deleted.

[start-state.json](start-state.json) records the starting Git state. [generated-manifest.json](generated-manifest.json) records managed output versions, not scientific approval. To reconcile a later prose addition, read it, integrate its content into the relevant existing source/record, then use the documented `preserve-view` command before rendering.

## Validation and remaining scope

The repair passed the infrastructure tests, complete metadata/navigation check, legacy registry check and invocation from outside the repository. The recorded check results are in [validation.json](validation.json). The exact working-module and textual-import counts at the validation cutoff are recorded with the checks. These are navigation counts, not distinct theorem counts or elaborated Lean dependency proofs.

No Lean source was changed by this repair and no new mathematical claim was introduced. Existing source/receipt bindings were checked; mathematical and empirical work arriving from other sessions retains those sessions' recorded scope. A whole-repository checkpoint preserves incoming work without upgrading its validation status.

Historical semantic migration is not exhaustive. The register explicitly distinguishes migrated coverage from the full corpus; existing reading catalogues and studies retain unmigrated claims. Physical relocation of active workspaces, a universal Lean build, automatic hash refresh and universal semantic equivalence detection are not part of the repair. Future research should migrate the particular result it changes and reuse its existing evidence. New independent authorization remains valid even before its scope record is added.
