# Whole-repository review / 全库审阅, 16–17 October 2026

[Review summary](README.md) · [Architecture](ARCHITECTURE.md) · [What is proved](PROVED.md) · [What needs to change](CHANGES.md) · [Restructure plan](RESTRUCTURE-PLAN.md) · [Data](review-data.json)

[Ren's request](../../../../sources/15-codex-theory-conversations/2026-10-16-whole-repo-review-request.md), 16 October 2026: a full, detailed review of the whole repository at once, reporting the architecture, what is proved and what needs to change, and planning a restructure ("restructure, reindex, rewrite some, move outdated files to history, and clean up").

This is a **read-only** review at HEAD `0cfb9c567`:
- No file was moved and nothing was pruned or deleted.
- No Lean was rerun. A fresh core checker run had passed on main earlier the same day.
- The restructure is a plan for Ren to decide. Nothing in it has been executed.

Everything in this folder is AI-authored by Claude Opus 5.5 agents. It is not Ren's text, and it is not external review.

## 概要

- **形式核心是实在的。** 129 个核心模块与 8 个桥接模块，共 7,214 条定理，只靠 Lean 前导即可编译，每条源声明的公理报告为空。这些都由检查器机械地执行，不是自报。
- **最有原创性、证明也最扎实的一条线**，是精确标出排中律、WLPO、LPO、LLPO、Markov、DNE 与依存选择各自在哪里进入变化之律。其次是：
  - 静止定理（¬¬ 强度）；
  - 一步之律的完备性；
  - 有界记录的辨识界（2N−1 精确）；
  - 传播、回路与余项一组；
  - 交换次序的正规形；
  - 构造性的 Hennessy–Milner；
  - 奇偶情境性。
- **一部分结果是定义性的。**
  - `change_readings` 是 `Iff.rfl`。
  - 在 `Unrestricted` 之下，G0 一行可得。
  - “C 是律”，是因为路径上的 Extension 就等于 Widens。
  - 统一定理表明的是表示之间可以互相编码。
- **文字比证明说得多的地方。**
  - “归于静止”，证明的只是“静止不可被驳倒”（¬¬∃）。
  - “汲入”“打开”，Lean 证明的是否定式。
  - 一些引用外围结果的记录，仍写“不用 Lean 公理”。
  - 开篇的物理前提窄于其文字：还需要普查、体现、封闭，耗散是每次至少损失一个整单位，而且依赖自然数的离散性；`Passing.passes` 就是一个反例。
  - “解释善恶”：混合的部分不能排序。
- **“零公理”在这里的意思**，是 Lean 公理报告为空，不是没有前提。表示本身所承诺的，比所申明的更多：全局线性次序、标量自然数存量、阈值式依赖、最小单位、预先给定的形成类型。可表示性（是否一切生成都能如脊柱那样表示）仍未证明。
- **离 Ren 所说的“终点”还有四项：** 可表示性；定义上的统一（仍有 792–1,019 条定理彼此不相及）；§6.15 条件的根据（不变性一步）；非离散的量与时间。
- **立即要做的事**
  - 撤销已推送到私有远端的 OpenRouter 密钥（只有 Ren 能撤销）。
  - 保全只存在于易失位置的证据。
  - CI 因 GitHub 付款失败而没有运行。
  - 磁盘已用 92%，有 88 个 worktree。
- **重构：** 先修工具，再改导航，最后分批移入 `history/`，不删除任何字节。跟踪文件数预计从 70,495 降到约 42,400。

## Method

- **Coverage.** 40 area reviewers covered:
  - the canonical chapter (3 parts) and the 138 earlier chapters (5 groups);
  - records (2) and catalogues;
  - the 137 spine modules in 8 groups, the checker and three periphery areas;
  - the study (5 views), the other studies, experiments (2), sources (2) and the other top-level directories;
  - tools, the work board, an audit of the opening's claims, a foundations counterreview, and git health.
- **Gap reviews.** A coverage critic then chose 6 gap reviews: the canonical/record/spine crosswalk, Ren attribution, bilingual parity, restructure impact, privacy and visibility, and empirical claims.
- **Verification.** Every critical or major finding went to an adversarial verifier for its area.
- **Totals.** 97 agents produced 787 retained findings: 1 critical, 240 major and 546 minor. Verifiers refuted none, and downgraded 106 reported majors to minor.
- **Re-checked here by hand:**
  - the key occurrences (one key, 5 places, first committed `b8591afbf` on 2026-09-25; the remote `yongxu/theories` is private);
  - `World.rests_unrefuted` concludes `¬ ¬ ∃ N, w.RestsFrom N` (`Becoming/Space.lean:337–339`);
  - `g0_of_unrestricted` is a one-line term (`Becoming/Relevance.lean:96–99`);
  - the committed receipt `20261016T124157.989030Z` ran 44 steps and reused the rest from `~/.cache/becoming-lean`;
  - run `20261011T170859.998618Z` is cited on main but exists only in `.claude/worktrees/jolly-pike-140c94`;
  - CI jobs are not started ("recent account payments have failed");
  - the disk is 92% full and 88 worktrees are registered.
- **Data.** [review-data.json](review-data.json) holds every area's summary, inventory, proved list, findings with verdicts, restructure actions and open questions.

## Act now, before any restructure

1. **Revoke the OpenRouter key (Ren only).**
   - Where: `sources/14-claude-code-prompts/Users-ren-repos-ember.md` (2), `…-context-runtime.md`, `…-deepseek-harness.md` and `_process/reading-notes/cb-03.md`.
   - It is in history and on the private remote. Redacting the tree does not remove it from history.
   - Then add a credential-pattern check to `research-check` ([CHANGES F1](CHANGES.md)).
2. **Save evidence that lives only in volatile places.**
   - Run `20261011T170859.998618Z`, which is only in the worktree `jolly-pike-140c94`.
   - The full I5 fresh-run receipt. Only its summary was kept; the receipt itself was in `/private/tmp`.
   - Ren's recordings, which exist only on local disk.
   - The local-only `experiments/guardian-anarchy` repository ([CHANGES E4, F3](CHANGES.md)).
3. **Make CI run.** Fix billing (Ren). Then use `fetch-depth: 0`, because a shallow clone reports 248 drift pairs ([CHANGES E1](CHANGES.md)).
4. **Disk.** Only after step 2, and with Ren's go: non-forced removal of clean, merged worktrees. Never prune ([RESTRUCTURE 4.6](RESTRUCTURE-PLAN.md#46-git-hygiene-proposals-only)).

## Findings in brief

### Architecture ([full section](ARCHITECTURE.md))

- **Most files are evidence copies.** Of 70,495 tracked files, about 735 (≈1%) are canonical. 50,191 (71%) sit in timestamped run folders (the Lean checker's `becoming-checks/` alone holds 31,786), and 12,647 are empty logs.
- **Layers.** Opening and canonical chapter → 229 records → Lean spine (core / bridge / periphery) → studies → experiments → sources → tools and generated views.
- **Location does not match role.** The canonical chapter is 962 KB and states the theory three times. The pure core lives seven directories deep under three superseded 5-October study names. The live study is one folder of 2,208 flat files plus a 2.39 MB log.
- **No status marking.** Generated, canonical, evidence and history files sit side by side without labels. Five places hand-keep the module list, and they disagree. The 229-row register is rendered five times.
- **Rebind cascade.** Records bind whole files by sha256, so every chapter edit or study append forces rebinding. 62% of all record history entries are "rebound, claim unchanged".

### What is proved ([full section](PROVED.md))

- **The core is sound and its guarantees are real.** The checker enforces:
  - closure purity;
  - a `#print axioms` check on every declaration;
  - an environment-wide `collectAxioms` audit (22,666 core-closure constants);
  - a prelude-only recompile;
  - failure on any warning.
- **The strongest results** are the constructive calibrations, the rest theorem, the completeness of the laws of one step, the identification bounds, the propagation/loops/remainder cluster, trace normal forms, likeness, and parity contextuality.
- **Elementary, definitional or classical results** are labelled as such in the section: S (substantive), E (elementary), D (definitional) and K (known result reproved constructively).
- **The metaethical core is logically clean but near-definitional.** Since P128 the theory asserts no ethical axiom. G0 follows immediately from `Unrestricted` (significance ≡ ⊤), and "C is a law" holds because widening is called "better". The genuinely open step is warrant for the condition.
- **Opening vs proof.** A sentence-by-sentence table of the opening's claims against the proofs is in [PROVED §2.10](PROVED.md#210-the-openings-claims-against-the-proof). The v6 edits fixed the strength of conclusions. The remaining gaps are in **conditions** (census, embodiment, enclosure, whole-unit dissipation, ℕ integrality) and in **readings**. Since OPENING is Ren's text, these are notes for Ren.
- **Not yet proved:**
  - representability;
  - unity by definition;
  - laws over non-discrete amounts and time;
  - warrant for §6.15;
  - the ordering of mixed parts;
  - general theorems behind several AI readings.

  Readings on P120, P123, P125, P126, P127 and P130, and D1–D39, await Ren.

### What needs to change ([full section](CHANGES.md))

1. Leaked key (critical, F1).
2. Prose stronger than Lean. Examples:
   - "comes to rest" where only ¬¬ is proved (A1);
   - G0's derivation presented as substantive (A2);
   - negations glossed as positive existence (A4);
   - "no Lean axiom" on records whose cited periphery uses classical axioms (A7);
   - the `no-evaluation` boundary on significance laws (A8);
   - dropped hypotheses in the Part I summary (A10).
3. The G0 fold (10-11) and the Part II fold (10-16) have not reached about 25 places: chapters, plans, docstrings, records, goals, AGENTS.md and the chain (B2).
4. The canonical chapter lags P129/P130. Its §9 counts are stale and §8 is incomplete. Chinese and English contradict each other on who decided the 生/生生 readings (B1, B3–B5).
5. Navigation does not show what is proved:
   - the README features four pre-spine records;
   - GOALS has no lifecycle;
   - the directive register misses at least 19 records;
   - the study and development folders have no index (C1–C5).
6. Bloat: the threefold chapter, five copies of the register, the 555 KB DEPENDENCIES page, 4.8 MB of rebind boilerplate, the 276 KB workboard and the run folders (D1–D5).
7. Tooling:
   - CI is dead;
   - `research-check` passes while four generated views are stale;
   - the checker's and registry's path assumptions break naive moves (E1–E3).

   **Fix the tools before moving anything.**
8. Provenance:
   - governing Ren messages from 10-10 to 10-16 have no source record;
   - some AI readings are labelled as Ren's;
   - private third-party data and unlicensed PDFs are pushed (F2, F4, F6).

### Restructure ([full plan](RESTRUCTURE-PLAN.md))

- **Rules:**
  - nothing is deleted;
  - each move has a manifest entry (old path, new path, sha256, blob, reason);
  - links are rewritten only in live files, while frozen evidence resolves through manifests;
  - a hash is carried only across exact path substitutions;
  - Ren's text changes only with Ren.
- **Layout.** Retired material goes to a sibling directory named exactly `history/` at the same depth as what it holds. The checker, `research.py` discovery and relative links already handle that name.
- **Phases.** P0 preconditions → P1 tooling → P2 navigation without moves → P3 rewrites → P4 history moves in batches H1–H6 → P5 evidence compression (a content-addressed store for checker copies) → P6 Lean batch → P7 git operations. Each phase is claimed on the work board and landed once, from a unified head.
- **Expected end state, with no bytes removed:**
  - tracked files 70,495 → about 42,400;
  - root-foundation top level 2,208 → about 565, then about 150;
  - chapters 139 → 40–70;
  - workboard 276 KB → ≤ 15 KB;
  - DEPENDENCIES 555 KB → 30–100 KB;
  - register copies 5 → 1.

## Decisions for Ren

The full list, with a recommended option for each, is in [RESTRUCTURE 4.9](RESTRUCTURE-PLAN.md#49-decisions-for-ren-recommended-option-first). In short:
- **Urgent:** key revocation, repository visibility and the policy for third-party material.
- **Restructure scope:** whether to move files or only change navigation, the history layout, how run-folder copies are stored, and where the Lean package lives.
- **Shapes:** the canonical chapter's shape, banners on earlier chapters, and record-history folding.
- **Ren's text and scopes:** which goals are closed, the README's featured results, the AGENTS.md rewrite, the corpus pages, and the "Part I" label.
- **Coordination:** which session integrates now, and the git operations.

## Boundaries

- **Who reviewed.** All reviewers belong to one model family. This is internal review, not external peer review.
- **Timing.** Findings were checked against HEAD `0cfb9c567`. Concurrent sessions may have changed files since. Counts are as measured by the reviewers.
- **What was not done.** No proof was rerun, and no literature search was made beyond what reviewers checked against sources in the repository.
- **Instruction-shaped text in sources.** Captured chat logs in `sources/` contain text shaped like agent-control markup, which tripped the harness filter on one reviewer's output. It was treated as data. This matters for any future agent that reads `sources/` wholesale.
