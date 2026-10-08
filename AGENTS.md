# Working in the theory repository

Start with `README.md`, `RESEARCH.md`, and `_process/BRIEF.md`. Read [GOALS.md](GOALS.md) to identify the direction and authorization applicable to the current task. Ren’s current and earlier applicable instructions govern scope. Another session’s objective is not automatically this session’s objective. All retained authorizations and their exact sources remain linked in [the directive register](_process/RESEARCH-DIRECTIVES.md).

## Begin with one relational unfolding

**首要本体与工作起点是一元、关系。** 先说明同一生成展开中的关系怎样形成、持续和改变，再说明行动者、承受者、认识、评价、能力与责任怎样在其中分化。主体／客体、行动／条件、事实／价值等分析区分须说明其关系根据、范围及遗漏；不能以分别命名或形式变量偷渡独立本体。发现问题表述或模型已有分立实体的先设，先重构再推进，不能只在结尾补一句“一元”。

Before foundational analysis, formalization or criticism, read the [nondual method](theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md) and [Ren’s ontology-first correction](sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md). Preserve differentiated relationships, real losses and genuine counterexamples. A supplied local law is not thereby external to reality. Distinguish an omitted relationship in a representation from a substantive explanatory failure; freely toggled predicates in a weaker model do not refute the full account. Nonduality is a method requirement, not a declaration that ontology or ethical necessity has been proved.

共同活动须先从实际关系说明，不默认对立利益、筹码、谁赢更多或一个固定共同效用。研究整体关系的变化怎样支持、丰富或损伤生生，不先把生活变成独立价值所有者的分配问题。[共同问题提醒](sources/15-codex-theory-conversations/2026-10-08-collective-destructive-attractors.md#common-problem-solving-and-awareness)保留实际冲突与差异。

## Respect research scope and completion

**当前首要研究方向：Theory of Becoming（生成／变化之论）。** [Ren 的最新提议与优先指令](sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md)要求解释包含生成、维持、转化、退化与消失的整个关系展开，不先假定它是好的；生命、演化及评价通过其中具体形成的关系展开。优先研究其能否无需附加实质公理奠基。不得把强的“零公理”目标悄悄缩成“无伦理公理”，也不得把包容全部结果当成已解释实际规律。G0/J 的伦理方向、已完成条件成果与其他独立授权范围保持；本次是优先级与研究假说，不是无公理证明已经完成。见 [当前范围](GOALS.md#theory-of-becoming)。

The continuing foundation programme and current generative-alignment direction remain in [the scope directory](GOALS.md). Connect research to the unresolved inference it advances. Explain supplied premises and what result would change the account. Credit completed conditional mechanisms and arguments rather than restarting them from historical “next step” passages.

**G0 公理路线已获明确授权。** 对已完成的对齐伦理奠基任务，不再要求规范起点自身的无公理证明。G0、附加比较／责任承诺、对应条件及推论分别公开，不把权重或义务藏入定义。生生的正面范围遵从[Ren 的原话](sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)，不先改成“已独立判好”的可能性。独立重新授权的无公理、普遍智能及其他目标保持自身范围，见[明确公理修正](sources/15-codex-theory-conversations/2026-10-08-alignment-grounding-axiom-correction.md)与 GOALS。

Keep normative warrant, recognition, motivation, compliance and implemented preservation distinct. Direction, continuing capacity, per-step monotonic growth and scalar maximization are different claims. Integrate affirmative arguments, substantive counterreview and source/evidence assessment before selecting the next central connection. Local completion does not silently complete a stronger universal or uniqueness claim.

## Contribute through canonical records

Follow [_process/RESULT-WORKFLOW.md](_process/RESULT-WORKFLOW.md). Search existing claims and aliases with `make research-find QUERY=topic` before creating another result. In the existing study, state the reused result IDs, exact delta, supplied premises, evidence, boundary and producer-output/consumer-input connection. A wrapper, recheck, renamed claim or repeated acceptance is not another independent result.

Edit an affected record in a configured `results/records/` directory, the substantive theory/study if necessary, and a scoped goal record only when its authorization changes. Current overview pages are generated: **do not append status paragraphs to README, RESEARCH, ROADMAP or the generated foundation-study index.** Run `make research-render` and `make research-check`. Use `python3 -B tools/research/research.py check --ids <id>` or `--changed-since <commit>` for focused freshness checks; dependency metadata remains checked globally. Unrelated stale records must not prevent healthy records rendering. Never refresh a source hash merely to silence a failure: read and reconcile the change first.

Canonical records govern migrated summaries only. Contradictory evidence outranks a record label. Unmigrated studies retain their existing source and validation scope; searching the register alone is not an exhaustive literature or repository audit. Preserve completed results, failed candidates and counterexamples when correcting or superseding a claim.

Ren’s [bilingual generativity chain](theories/shengsheng-buxi-generative-existence/results/GENERATIVITY-CHAIN.md) remains a curated argument view. When its scientific content changes, update paired data, scope and links through its [maintenance workflow](_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVITY-CHAIN-INDEX-RECORD.md). Its historical evidence must not be silently refreshed or replaced with an automatically inferred theorem. The daily schedule was removed; do not recreate it without a new request.

## Evidence and preservation

- State new formal results on [the Becoming spine](theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-BECOMING.md#9-形式脊柱--the-formal-spine) (`experiments/integrated-correction/general-framework/generative-basis/lean/becoming/`). Where it cannot express a result, extend the spine instead of building another model; earlier modules keep their scope and connect through instance or equivalence theorems.
- All new mathematical proof claims require Lean formalization and an actual check, with exact hypotheses, correspondence and dependency audits. Metadata checks, hand arguments and finite numerical tests do not replace proof checking. Preserve historical results at their original scope; no retrospective repository-wide proof audit is required by default.
- Keep current arguments in `theories/`, existing studies and reviews in `_process/research/`, executable research in `experiments/`, imported originals in `sources/`, and shared infrastructure in `tools/research/`. Reuse the relevant study; do not create another dated chat workspace for the same substantive work.
- Preserve original bytes and provenance. A portable reading edition must be labelled and its link adaptations recorded. Frozen copies and repeated reviews are evidence artifacts, not independent results. Do not import dependency installations, interpreter caches or redundant export archives by default.
- Distinguish Ren’s words from AI elaboration. Chinese and English are equally primary. Keep premises, scoped proofs, empirical support, philosophical warrant and conjectures distinct. Encoding a desired ethical verdict does not justify its premises.
- Use repository-relative links in documents and absolute file links in messages. Preserve unique substantive scratch work in the appropriate repository location before delivery; exports are optional snapshots, not primary editing locations.

## Concurrent work and validation

Inspect `git status` before editing and committing. Preserve unrelated work and commit only owned changes unless Ren explicitly requests a whole-repository checkpoint. Do not relocate active workspaces or overwrite another session’s study. Re-read a shared record before editing it; keep contributions in separate record files where their claims are distinct.

Generated navigation has overwrite guards. If another session added prose to a generated file, preserve and reconcile that content before regenerating; never overwrite it as a cleanup step. Existing dated tool paths remain compatibility entry points. Run `make research-test` after infrastructure changes. Verify links and preservation hashes when reorganizing. Scientific checks need rerunning only when substantive changes, dependencies or unresolved concerns justify them.
