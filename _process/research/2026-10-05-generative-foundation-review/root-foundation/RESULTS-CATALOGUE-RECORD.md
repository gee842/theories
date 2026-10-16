<a id="成果目录的整理记录--results-catalogue-editorial-record"></a>
# Results catalogue editorial record

> Some passages exist only in the [Chinese edition](RESULTS-CATALOGUE-RECORD.zh.md): sections “Results catalogue editorial record”; “Request and scope”; “Files and maintenance units”; “Evidence boundaries”; “Homepage preservation and concurrency”; “Regeneration and checks”.

<a id="请求与范围--request-and-scope"></a>
## Request and scope

Ren’s request in this conversation (original language, verbatim):

> 虽然没有把我们的目标完全证明，但是现在有的已经很可观了，我们应该系统化的把每一个论证的英文，中文，lean做一个系统化，有list，可以查看的文档
> 同时，我们也要解释每一个理论的significance，并且还有哪些方向正在/应该继续探索
>
> 并且update README， 它现在的主要页应该是我们目前的理论结果和理论进度

The quotation preserves the user’s request; the remaining prose and bilingual catalogue are AI-authored. This round organizes existing results, their significance and their future questions, and makes them the homepage. It neither sets a replacement research objective nor contributes a new theorem.

<a id="文件与维护单元--files-and-maintenance-units"></a>
## Files and maintenance units

The 107 chapters are document/argument-family units, not 107 independent theorems. The bilingual entries reconstruct the core argument and significance; they do not claim to translate every historical sentence or every auxiliary Lean declaration. The original claim register, detailed proofs and reviews remain linked. Lean declaration inventory provides the finer source-level view.

<a id="证据边界--evidence-boundaries"></a>
## Evidence boundaries

These are documentary boundaries. A proof under explicit premises and the substantive warrant of those premises remain different achievements. This round performs no new Lean build, empirical experiment or retrospective repository-wide proof audit.

<a id="首页保留与并行工作--homepage-preservation-and-concurrency"></a>
## Homepage preservation and concurrency

Both pre-reorganization homepage versions are byte-preserved, including the concurrent generative-premise update. Their relative links retain the original repository-root base. The new homepage and catalogue supply navigable links; historical snapshot bytes remain unchanged.

<a id="复现目录与验证--regeneration-and-checks"></a>
## Regeneration and checks

```sh
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_results_catalogue.py --check
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_lean_catalogue.py --check
```

The first command checks catalogue coverage, fields, referenced files, source-version hashes and generated output consistency. Edit the three reading JSON registers, reread changed sources, then regenerate without `--check`. The Lean generator refreshes its source inventory and compares generated outputs. Neither command compiles Lean or certifies an ethical premise.

<a id="发布快照续记--release-snapshot-continuation--2026-10-08"></a>
## Release snapshot continuation — 2026-10-08

Ren subsequently authorized committing this work together with the latest research and pushing remote `main`. The local snapshot and remote changes were combined in an isolated checkout, preserving later concurrent edits in the live workspace. Affected entries were reread and refreshed. This release checks catalogue consistency and selected existing receipt/source bindings; it performs no new Lean compilation or retrospective repository-wide proof audit.
