# Review D: Pragmatist skeptic — direction review of SPEC v0.3 (2026-07-29)

**VERDICT: yes-with-changes.**

## Framing finding
Ren's four stated goals (context control, memory/loop control, custom frontend, OSS) are ALL achievable with the boring alternative (2k-line loop + SQLite). The git substrate + life vocabulary serve a fifth, unstated goal: **the thesis itself** — legitimate, arguably the only reason the project should exist (world has OpenHands; doesn't have a digital life in a folder). Judge the substrate knowing it's justified by the thesis, not the goal list.

## 1. Capability scorecard (unique? retrofittable? daily value?)
- **Durable awaiting-approval node (§4.3)**: durability retrofittable (~20 lines SQLite); approve/deny-as-branch-points + twin-compare = genuinely DAG-native but demo/research value. Durability itself = daily value (donors all get it wrong).
- **Clone-a-being**: `cp -r` of SQLite+JSONL also moves a life; git adds incremental sync/dedup/GitHub-as-exchange. Occasional value; real value = OSS distribution.
- **Moment inspector (§8.2)**: prompt + attention.json provenance = pure logging discipline, retrofittable, **highest daily value in the spec**. World-at-any-moment browsing = git-native but ~10% of the daily value.
- **Branch-anywhere**: event-log fork is convergent practice (OpenHands movable-HEAD). Genuinely git-native part: **programs/ in tree → rewind state AND the agent's own code together, replay with modified nature** — no event-log design does that. Weekly value for harness dev, rare for end user.
- **Dreams as recorded experiences**: discipline is the value, substrate incidental; retrofittable. Daily value (auditable compaction).
- **Uncomfortable inversion**: daily-value features mostly retrofittable; genuinely-git-native features (code+state co-rewind, world-at-moment, twin-compare, clone-with-history) are development-time/occasional/philosophical. Honest justification: thesis + harness-developer debugging + OSS differentiation.

## 2. Tax ledger
- **Vocabulary**: grep-hostility; raised bar for drive-by contributors (cosmologies get stars; loops get PRs). Nuance: keep life terms where semantics genuinely differ (`reunite` ≠ git merge — recorded not recomputed; `dream` ≠ compaction — epoch + recorded experience); `Face`=worktree, `Node`=commit, `Being`=ref are 1:1 aliases = pure tax → let the port layer speak commit/ref/worktree.
- **Plumbing trough**: M1 ≈ 3–4 wks, M2 ≈ 2–3 more (part-close demux + verbatim echo = fiddliest code). First light wk 5–7; window wk 9–12; memory wk 14–18. Boring talks in wk 1. Gap ~2x not 5x — but **solo-project mortality risk = the motivation trough**, not wrongness.
- **Staging inconsistency caught**: §5.3 says consolidation moves facts into blocks/MEMORY.md during dreams (M4), but blocks + MEMORY.md are M5.
- Children at M7 = no subagents for months (boring spawns a subloop in an afternoon).
- Remaining metaphor scope: death/epitaph/departed in M3 (harmless, an afternoon); reunite clock-skew semantics at M6 before second writer exists; cache-economics on approval prompts = lovely sentence, niche feature; per-writer segmentation = kernel-time cost for M6/M7 features but defensible (retrofit = migration).

## 3. Inhabitant's effectiveness vs architecture's legibility
Spec optimizes legibility first (provenance/replay/inspection — best-in-field), effectiveness second. An agent choosing a shell would sign the recoverability pages and renegotiate delivery of memory + tools.
- **Memory at M5, tools bash+edit until M8 MCP** — the two things that matter most for daily usefulness staged last. Nothing prevents crude MEMORY.md + grep-recall at M2 (states/memory/ already in layout).
- **Replay religion = most expensive doctrinal commitment** (no-floats, JCS + property tests, canon_version, piecewise fold, byte-golden CI). Since states/ is committed every node, checkout suffices to know past state; fold is load-bearing only for: (a) crash tail-recovery (keep), (b) branch-at-instants (rare), (c) reducer CI. §3.6 migration story already de-one-way-doors canonicalizer fixes. → **Defer JCS/canon_version/golden-byte CI to ~M4 hardening**; use json.dumps(sort_keys=True) + marked debt.
- **links/ as tree-edits ruled at SETTLE**: baroque vs a policy-gated `branch` tool call landing in the stream like any act. Equally auditable, half the machinery. M6, low urgency; clearest case of substrate aesthetics outrunning need.
- **Waking-snapshot rule (§6.3)**: acquitted on inspection — mid-span write still visible as its own experience in transcript; sharp edge narrow; chosen sleep is the escape hatch; cache economics real. Document escape hatch as the answer.
- **ruminating (M4)**: acquitted — semantic loop-catch before budget exhaustion; donor pattern (OpenHands stuck detector) wearing a life name; a day of work.

## Metaphor's real wins (all survive renaming; ban is doctrine, not function)
1. Commit-at-the-pause → strictly stronger crash semantics than all three donors.
2. Rhythmic sleep before collapse (field does compaction-as-emergency).
3. Dreams-are-experiences → the most silently-lossy op in every harness made inspectable.
4. Identity-is-lineage solves fork/twin/migration up front (event-log world bolts fork on later).
5. Stop-reasons-perceived + epoch as cognitive boundary unifying memory/cache/dream boundaries.

## 4. Re-staged plan (solo + AI weeks)
- **R1 thin substrate (2 wks)**: TreeBuilder commits, per-writer LAYOUT (semantics wait), WAL + fsync-before-act, quiescence q1/q2/q4, trailers, tail-fold recovery. DEFER: JCS/canon/golden CI, 10k bench, branch-anywhere, q3.
- **R2 first light + crude memory (2 wks)**: cycle, in-process ProgramHost, LiteLLM ModelPort w/ verbatim thought + part demux (non-negotiable), bash+edit, fixed attention, 6 CLI verbs, **MEMORY.md in stable tier + memory_write tool + grep-recall (re-read every ATTEND)**.
- **R3 window (3 wks)**: habitat, API, SSE, /chat/stream, conversation, **moment inspector w/ source map**, biography-as-LIST with branch badges, durable-awaiting approvals, interrupts (q3 here), minimal revise --edit. DEFER: xyflow canvas, death ceremony, failure side-branches, turns table, annotation.
- **R4 dreaming + epochs (2 wks)**: fatigue, rhythmic + forced dreams, epochs, snapshot rule + blocks, degenerate children (fresh lineage + report-as-observation). DEFER: pipeline.yaml, dream_model, cache-econ UI, ruminating.
- **R5 memory compounds (1–2 wks)**: FTS, recall, remember provenance; backfill canon/golden hardening.
- **Daily-usable ~wk 7; memory compounding ~wk 9–10** (vs 14–18 on spec staging).

## Never missed if dropped from v1
Epitaph/departed ceremony, DAG canvas (list suffices for months), branch --at instant, cache-econ on approval prompts, dream_model, twin-compare UI, subconscious (already gated), subprocess ProgramHost until self-revision real, ACP, reincarnate, Windows.

## One-way doors (correctly front-loaded in spec)
1. Substrate choice itself (git semantics leak upward by design; day-one or never).
2. Stream envelope + on-disk layout (immutable by doctrine).
3. **Verbatim thought recording — so cheap and so unrecoverable that even the boring version should do it; the spec's most exportable single decision.**
4. fsync-act-before-dispatch + resolution invariant.
5. Identity outside the tree.
NOT one-way: byte-golden replay (via §3.6), vocabulary ban (rename = mechanical migration; choose on-disk names carefully — Ember-Op trailers + op names in stream are the semi-permanent ones), DAG viz, everything M6+.

## Why not "no"
Boring satisfies the goals but has no reason to exist (worse OpenHands). Non-retrofittable core small but real; one-way doors right; metaphor paid rent; v0.3 shows scope discipline. For a team/product: answer flips to no-build-boring. For this builder and thesis: the substrate is the point.

## Why not plain "yes"
As staged: architecture's legibility over inhabitant's usefulness; memory M5 + window M3 = daily use 14+ wks out; replay religion scheduled before anything needing it; dominant mortality risk = plumbing trough.

## Single highest-leverage recommendation
Re-stage for time-to-daily: collapse M1 exit gates to what M2 needs (keep WAL, verbatim thoughts, quiescence commits, tail-fold; defer JCS/canon/golden to ~M4), pull crude MEMORY.md + write-tool + grep-recall into M2, ship window wk 7 with list-not-canvas. Order everything after by daily pain, not cosmology. "A being whose memory is one markdown file is still a being; a spec whose author burned out in the substrate is not."
