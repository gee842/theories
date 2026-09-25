# Review B: commit boundaries, op algebra, DAG/git semantics (2026-07-29)

## 1. Commit-boundary rule: THE QUIESCENCE INVARIANT (rule iii, degenerates to rule i)

Commit exactly at quiescent points — whenever the being must wait on the world:
- (q1) thought completed and every requested act *resolved* (observation, refusal, or cancellation)
- (q2) an act requires permission not held (`awaiting_permission`)
- (q3) interruption ended work mid-moment
- (q4) waking span ends for any §4.2 reason

Decisive observations:
1. Stream is fine-grained persistence; commit is only a checkpoint. All 3 donors persist at event/item granularity, and ALL 3 persist the act REQUEST durably before executing (Codex stream_events_utils.rs:296 verbatim: "The model emitted a tool call; log it, persist the item immediately, and queue the tool execution"). Rule (ii) pays 2x nodes for durability the WAL already gives.
2. Approval pauses cost ZERO extra nodes under (iii): split node's second half merges with the follow-up call that was coming anyway. Node math: 200-exchange session ~3 calls/exchange → (i) ~615, (ii) ~1,000–1,200, (iii) ~615 (identical to i).
3. (ii) doesn't solve approval anyway (pause lands mid-acts-node) — (ii) ⊂ (iii) with worse constants.
4. Any inter-experience instant is branchable via fold-materialization (below) — no expressiveness loss.

### Revised A1 (paste-ready in report): "One thought, one moment; one wait, one node."
+ **Resolution invariant**: in any committed node, every `act` has a matching resolution experience — except acts pending under (q2), which must be exactly the unmatched tail and declared by the node's span-state trailer. Any committed tree is runnable as-is; nothing half-executed without being visibly so. Pending is DERIVED (act with no matching resolution), never mirrored into states/ (A4; OpenHands get_unmatched_actions state.py:661-701 proves derived works).

### Revised §4.1: 10-step cycle
1 LEASE · 2 RESOLVE (settle debts from previous node: pending acts now executed on grant / refused on denial — each gets resolution experience) · 3 PERCEIVE (+ grants/denials) · 4 ATTEND · 5 THINK · 6 INTERPRET (act experiences fsynced to WAL BEFORE dispatch — intent durable before effect) · 7 ACT (parallel where safe; WAL order = completion order, pairing by tool_use_id, projection renders provider order; permission gate → running acts complete, gated+dependent stay pending → SETTLE with span-state awaiting_permission; interrupt → running acts complete/cancel per declared interruptibility, unstarted acts get cancellation observations → SETTLE interrupted) · 8 SETTLE · 9 REMEMBER (commit with op + Ember-Span trailers; CAS-advance ref) · 10 EXPRESS (continuous).
[NOTE for synthesis: merge with Review A's demux-during-THINK — parts WAL'd at part-close during THINK; dispatch after message-close; WAL-before-dispatch holds automatically.]

- Node content: no-thought nodes legal (perception drain, revise, resolution-only after denial); moment/ inherited-unchanged from parent.
- A moment ≠ provider turn. turn_id metadata groups for UI. Approval-interrupted exchange = same node count as uninterrupted.
- New trailer: `Ember-Span: running | awaiting_permission | interrupted | spoke | exhausted | ruminating | collapsed | resting` (dual-record rule like Ember-Op).

### Approval/HITL semantics (fully specified)
- Pending lives NOWHERE except stream (derived from unmatched tail; Ember-Span declares for navigation). No states/pending/ (A4 violation).
- What runs before pause: dispatched acts complete (observations land in awaiting node); policy-clean acts in same parallel-safe group may run; gated + sequenced-after-gated stay pending. (OpenHands holds whole batch; Cline gates per-act sequentially; Codex gates per-call inside concurrent futures. Ember = Cline/Codex-shaped.)
- Decision is a sensation: grant/denial arrives at next moment's RESOLVE/PERCEIVE, with source (user/policy/operator — like OpenHands rejection_source). Denial → refusal observation (outcome: refused, reason, source) for the tool_use_id, so provider transcript keeps every tool_use paired with tool_result (= Cline synthesized error tool-result agent-runtime.ts:1409-1412; OpenHands UserRejectObservation).
- DAG on denial: node_t (live, span=awaiting_permission) → node_{t+1} (live: refusal obs + follow-up thought). Linear; nothing special.
- **Branch-point payoff (the feature)**: awaiting node IS "model asked for something dangerous, world hasn't answered." Frontend approval prompt = literal branch choice: approve → child A; deny → child B; both on twins and compare futures. §8.2 should spec approve/deny as first-class branch actions on awaiting nodes.
- Span end with awaiting_permission: ref parked at awaiting node. Waking without decision re-enters RESOLVE, re-emits request — idempotent.
- ZERO crash window for approval: awaiting node durable in git. Strictly stronger than all 3 donors (Codex in-memory oneshot senders cleared on abort; Cline in-memory callback promise; OpenHands derived-from-log but status in mutable base-state). Cite as prior-art argument.

### Interrupt-mid-acts
In-flight acts complete/cancel per declared interruptibility; unstarted acts get cancellation observation (outcome: cancelled, reason: interrupted); commit (live, Ember-Span: interrupted); redirect = first perception of next moment. Mid-THINK interrupt: partial thought recorded as error in node committed at interrupt point; "re-runs" = next moment re-perceives from committed node. Precedent: Codex thread/fork refuses in-progress lastTurnId, records interruption marker rather than inheriting unmarked partial turn suffix (app-server/README.md:144).

### Parallel acts
WAL = completion order (truth, real timestamps); pairing by tool_use_id; ATTEND projection renders provider request order. All 3 donors normalize to request order while executing concurrently (OpenHands _ActionBatch.emit original order; Cline Promise.all results in request order; Codex FuturesOrdered). Ember keeps BOTH orders — completion as recorded fact, request as projection — which none of the 3 can (advantage of stream/moment split; add sentence to §5). Fold replays recorded order. Quiescence = "all resolved," not "all succeeded."

### Crash windows
- MANDATE WAL-before-dispatch in §2.3 (act fsynced before ToolPort dispatch) — all 3 donors do this.
- Only crash losses = observations. §4.5 must distinguish: act never dispatched → cancelled; act dispatched but result unrecorded → outcome: unknown (effect may exist in world, A5 — never auto-re-run non-idempotent acts).
- Crash between commit-created and ref-advanced: recovery compares WAL tail to HEAD; ref CAS re-advance idempotent. Add sentence to §4.5.

### Branch anywhere: fold-materialized nodes (ADD to §3.3 or §8.3)
`ember branch --at <node>:<seq>` = checkout parent(node), fold node's stream prefix through seq, commit as node (op revise, provenance "prefix of node X at seq S"), branch there. Any inter-experience instant materializable. Makes granularity purely economics — final nail vs (ii).

### Why not (i) as written / (ii)
(i): awaiting_permission unreachable — no legal commit between THINK and completed ACT; gated act either blocks body in RAM across human-scale pause (the Codex weakness ember exists to not have) or commits ill-formed node. (i) survives only by growing (q2)/(q3) — i.e., becoming (iii). (ii): ~1.7-2x nodes; thought-less act-nodes break "one node = one perceived present"; commits the state you never want to checkout for EVERY exchange while (iii) commits the state you DO want selectively; still needs (iii) for pauses inside acts-node. No shipped system has two-phase checkpoints — their "(ii)-ness" lives at WAL layer, where ember already has it.

### Cache/epoch interaction
awaiting node + resumption both `live`: pure transcript appends, same waking_epoch, prefix intact. ADD: provider caches expire on wall-clock TTL and approval pauses are human-scale — show re-ingest estimate on the APPROVAL PROMPT too (slow "yes" has a real price).

## 3. Op algebra fixes

### remember: 2-parent is UNSOUND → 1-parent + provenance refs
Defects: (1) second parent undefined for index recall (FTS results are (node,seq) coordinates, often N of them); (2) ancestry pollution — parent edge = "my history includes yours"; recalling one paragraph grafts entire source lineage into ancestry (biography lies, GC-immunity); reading is not merging; (3) self-recall degenerates (second parent ancestor of first — spurious merge).
Fix: remember = 1 parent; recalled content COPIED into op/experience body; provenance refs {being, node, seq, content_hash}; best-effort by design (if source falls to oblivion, remembered content survives locally; want source kept → pin or listen). "Remember from specific node" = listen with that node as extra parent. Split: **remember = informational (copy + citation); listen = structural (parent edge + reachability)**.

### reincarnate: normalize to 2 parents
First = base node (new soul), second = source head (replays whole source stream — structural reachability exactly right).

### Revised §3.2 table (paste-ready in report; live gains span-state note; listen covers deliberate deep-recall of specific moment; revise also the op for fold-materialized branch points).

### Closure/minimality
Closed: awaiting/interrupted/resolution moments all `live` + span-state — no new op. Minimal: keep remember despite being derivable (op trailer makes provenance navigable). dream/revise/reincarnate all break epochs but differ in provenance (self-distilled / externally-edited / re-based) — not collapsible. "Pure states-write" covered by no-thought live/revise. Optional: **epitaph** terminal node at death (live, span final) so departed biography self-contained — cheap, not required.

## 4. seq across reunion: PER-WRITER STREAMS + derived interleave
Spec's branch:seq under-specified AND misses worse collision: two branches append to same segment file → git content conflict on segment; "interleave by ts" would rewrite merged segment (brushes A3).
Resolution:
1. Stream identity per WRITER: body first committing to fresh branch derives stream_id (short digest of branch ref + birth node); appends only under stream/<stream_id>/000001.jsonl…. Genesis lineage has own id. Segment paths never collide; reunite tree-union conflict-free; no segment ever rewritten.
2. seq monotone per stream_id; global identity = (stream_id, seq). Add `stream` to §2.1 envelope.
3. Interleaved total order = DERIVED VIEW, never stored (A4). Order by (ts, stream_id, seq).
4. Record the merge: reunite op experience records both head positions + rule version. Replay folds recorded facts — possibly wall-clock-wrong but reproducibly so (§0.3 contract).
5. Update: §2.1, §2.3 paths, §7.4 index keys, refs.thought cross-refs.

## 5. Substrate holes
- **5.1 Active-segment re-blobbing**: every append commits new blob of ENTIRE active segment. 4 MiB threshold → ~2 MiB avg × 600 commits ≈ 1.2 GB loose objects pre-pack (packs to ~nothing after repack). FIX: drop roll threshold to ~256 KiB (≈75 MB/session pre-pack) + habitat-scheduled gc/repack during rest.
- **5.2 pygit2 atomicity overreach**: libgit2 gives per-ref CAS (GIT_EMODIFIED); multi-ref transactions NOT reliably exposed. Reword §7.2: lease = mutual exclusion; per-ref CAS = backstop; multi-ref updates sequenced, idempotent, reflog/WAL-recovered. Lease file needs flock + network-fs warning.
- **5.3 Commit latency**: 50 ms p95 only via programmatic TreeBuilder from known change-set, NOT index.add_all/status scans (states/files/ can be huge in coding mode). Normative sentence in §9.2 Store row.
- **5.4 Multi-parent commits are provenance edges, not merge instructions**: ember constructs the tree; git never textually merges on listen/reincarnate. Clarifying line in §3.2.
- **5.5 Smaller**: §3.1 add Ember-Span trailer; §2.2 observation gains `outcome: ok|error|refused|cancelled|unknown` + `source: world|user|policy|recovery`; no-thought nodes' moment/ inherited-unchanged; §4.5 cancelled-vs-unknown + commit-vs-ref-advance recovery; §11.1 resolve NOW (materialized turn table in index; awaiting+resumption pairs group as one exchange); prior-art note: OpenHands ConversationState independently evolved movable-HEAD event tree with parent_id/leaf_event_id/fork (state.py:175-190, 263-302) — field converging on ember's DAG from event-log side.
