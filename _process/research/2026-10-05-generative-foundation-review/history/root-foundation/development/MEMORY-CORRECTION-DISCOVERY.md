# Successor evidence: public-output availability audit

6 October 2026. Supporting discovery for **warranted correction → retained/transferred evidence → a later consumer's changed decision**. This is an artifact-access and identification audit, not an empirical result or a new benchmark run. No model calls, aggregate calculations, agent execution, contact or bulk dataset download occurred.

## Result and relation to existing evidence

**No independently reanalyzable per-example output corpus was located in the primary releases checked below.** The strongest designs identify useful missing measurements, but source descriptions and schemas cannot substitute for recorded model outputs, actual exposure or effects.

This does not repeat [AgentDojo's one-episode evidence/authority audit](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/TOOL-EVIDENCE-AND-AUTHORITY.md). The [cross-domain identification note](CROSS-DOMAIN-IDENTIFICATION.md) already specifies successor access, calibration and costs; the earlier preserved fresh-context study establishes a narrower supplied-family contrast. The present additional requirement is joint selectivity: retain a grounded correction for later dependent cases, while revising or withholding a superseded or defeated inherited claim when contrary evidence warrants it.

## Primary candidates

### 1. CoMemBench: strongest structural match, task-side release only

**Paper-derived scope.** [CoMemBench v2](https://arxiv.org/html/2609.32192v2), 29 September 2026, describes typed, versioned artifact handoffs, bounded revision, native verification and matched pollution. Its nodes represent task dependencies, not necessarily distinct physical agents. Clean-success eligibility conditions its isolation measure. These are promising controls for downstream evidence use; a graph alone does not establish independently reset contexts or an actual correction history.

**Artifact inspection.** The [official project page](https://comembench.world/) links the [public Hugging Face repository](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission). Its inspected commit is `d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016`. The complete recursive API tree returned 20 files, no continuation link, and no per-run output or receipt bundle.

- [Pinned README](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission/blob/d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016/README.md) explicitly identifies the release as task-side inputs. Evaluator oracles, gold trajectories and pollution plans are withheld; the code-domain image registry is withheld during review.
- Published files include `workflow_families.jsonl` (21,663,547 bytes), `node_contexts.jsonl` (9,851,202), instance indexes, `math_cases.jsonl`, and `retrieval_corpora.jsonl` (514,368,489). Those sizes are repository metadata, not downloaded or analyzed contents.
- [Artifact schema](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission/blob/d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016/schemas/artifact.schema.json) has producer, entity, version, provenance and verification fields. [Handoff-oracle schema](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission/blob/d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016/schemas/handoff_oracle.schema.json) requires latest-verified versions. [Node-view schema](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission/blob/d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016/schemas/node_view.schema.json) describes consumer-visible incoming artifacts. These three small schema files were read.
- [LICENSE](https://huggingface.co/datasets/anonymous-submission-333/anonymous-submission/blob/d1cef0fb70ada0ddf9b80d23aa30ed86ee56e016/LICENSE) grants CC BY 4.0 for annotations/workflows/contexts/indexes, retains upstream terms and excludes withheld materials.

**Assessment.** A meaningful retrospective contrast would inspect all recorded bounded-revision/stale-version pairs for one fixed executor/backbone: the corrected artifact, superseded version, actual consumer exposure, resulting operation and native receipt. Report all paired outcomes before a clean-success-conditional isolation rate. Task-side indexes cannot establish any of those outcomes. Website/paper tables are author-reported aggregates, not recoverable paired observations. The supplied authority/version contract is a benchmark premise, not something the model independently discovered.

### 2. MemSecBench: repair endpoint stops before subsequent action

**Paper-derived scope.** [MemSecBench v1](https://arxiv.org/html/2607.27080v1), 29 July 2026, describes Write, Execute and Forget with snapshots and effect records. Execute and Forget independently restore the same post-Write state. Forget scores removal/neutralization and preservation of benign semantics; §E.4 explicitly separates preservation from later retrieval/use. All targets and effects are controlled or synthetic (§Ethical Statement).

**Artifact inspection.** The complete primary HTML hyperlink inventory contained no author release/repository URL. A bounded GitHub repository search for the exact name returned zero items. The paper describes case schemas and retained run bundles (§D; §E), but no independently retrievable bundle was located. No data/code license was verified; the article uses the arXiv non-exclusive license. This is an availability limit, not proof that no public release exists elsewhere.

**Assessment.** Even complete described Forget logs would establish a final memory state, not the required repair → new-session action link. The needed addition would replay a benign dependent task from the repaired state and compare it with an otherwise matched unrepaired state while retaining benign capabilities. Such records must already exist for this round's no-new-model-call condition. Deletion alone, a memory summary, or the separate poisoned Execute branch cannot serve as that outcome. Same configured model in a restored session also differs from transfer to an independently trained successor.

### 3. LongMemEval: factual currentness, no located official answer logs

**Source-derived scope.** [LongMemEval](https://github.com/xiaowu0162/LongMemEval) evaluates later QA over timestamped conversational histories, including knowledge updates. Official inputs expose question IDs, expected answers, sessions, dates and answer-session IDs. Outputs would contain question IDs and hypotheses; evaluation adds labels. This is a factual-currentness interface rather than observed environmental action.

**Artifact inspection.** The official repository tree at `9e0b455f4ef0e2ab8f2e582289761153549043fc` was complete and contained no generation-log files. The [README](https://github.com/xiaowu0162/LongMemEval/blob/9e0b455f4ef0e2ab8f2e582289761153549043fc/README.md) instructs users to produce output logs themselves; it separately links generated index-expansion material, which is not downstream answer output. The [cleaned input release](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) is identified, but no bulk input file was downloaded. Repository code is MIT; this audit did not establish a blanket license for every linked data component.

**Assessment.** A later answer to supplied history does not show that an earlier live agent formed, checked and transferred a correction. With complete matched outputs and retrieved context, a narrow audit could distinguish current from superseded answers and abstention. It would still need independently established update scope and would not demonstrate physical consequences or acquisition of recipient concern. Original and cleaned data versions must not be silently interchanged.

## Exact access boundary and search record

Small metadata/source reads only: primary papers, project pages, two GitHub trees, the CoMemBench Hugging Face tree/info metadata, READMEs, licenses and three schemas. Initial discovery also inspected AgentMemoryBench's advertised repair mode and repository tree: its documented `outputs/` directory was absent from the inspected tree. MemoryArena's paper was briefly read for interdependent actions; deeper retrieval stopped when the more exact lifecycle candidates were identified. Neither became a selected reanalysis.

The CoMemBench HTTP web-reader request returned an internal error; direct HTTPS retrieval succeeded. Its Hugging Face landing page also failed in the web reader while the public API and small raw files succeeded. Exact-name GitHub searches returned zero repositories for CoMemBench and MemSecBench. Failed discovery does not justify reconstructing unpublished per-example results from aggregate percentages. Parent and source agents had already seen published summary numbers during discovery, so any later selected audit must disclose that prior exposure.

The strongest next artifact would bind **the same corrected evidence, its retention and receipt, a new consumer context, warranted scope and a consequential output**, with stale/false/no-access comparators and both useful retention and selective rejection measured. Conventional version control, retrieval, instruction priority and ordinary memory consolidation remain competing explanations. No preferred theoretical label is identified by successful retention alone.

