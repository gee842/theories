---
name: history-core-program
description: "Current main track (since 2026-08-13): History Core / Continuation Pipeline / Mediated Runtime program — phases 0–9 complete and ACCEPTED: final release published, Ren signed 2026-08-20, independent final review passed 2026-08-21 (0 P0/P1, 7 P2); ADR-019/029 accepted to freeze-registry scope; next: ADR-030 (proposed) on Ren's go"
metadata: 
  node_type: memory
  type: project
  originSessionId: 5b71429d-275b-4cb1-a410-4b3ca58a37d5
  modified: 2026-08-20T19:00:20.000Z
---

The engine plan (`specs/plan.md` v0.9) is fully implemented: Stages 0–11 all have acceptance records
(ADR-014 component layer, ADR-015 Stage-9 boundary, ADR-016 Stage-10 multi-agent, ADR-017 Temporal,
ADR-018 blob namespaces). The next round is the **History Core program**, whose docs supersede the old
draft as main plan while v0.9 + frozen bytes stay the operational baseline until phases activate:

- `specs/history-kernel-mediated-runtime.md` — target architecture (8-reviewer approved to *begin*, not to freeze). Center: agent-free History Core · explicit Continuation Pipeline (Request→Resolved→Materialized→ContextIR→Rendered) · non-authoritative scoped decision actors · Mediated Runtime owning contact/commit/publication. Seven Laws replace the Twenty (status: proposed until Phase 0–2A evidence + delta review).
- `specs/history-core-execution-plan.md` — phases 0, 1, 2A, 2B, 3–9; per-phase work packages `HC<phase>.<n>`, gates, stop/rollback. Completion = candidate-bound artifact in `bench/results/history-core/phase-N.json` + Ren sign-off in `specs/acceptance/history-core/phase-N.md`.
- `specs/adr/019-history-context-authority-boundaries.md` — proposed, NOT accepted; terminology + claim-by-claim supersession in `specs/history-core/`.

**State (2026-08-14):** Phase 0 is COMPLETE — artifact published (920c76d/c26bf49/523bded) and Ren's sign-off recorded in `specs/acceptance/history-core/phase-0.md` (commit 103a109, which also retired the overbuilt harness pieces — see [[phase-gates-stay-narrow]]). Phase 0 shipped one substantive production change: migration-entry trust-root validation + M013 ACL-residue / M030 backfill-RLS compatibility bridges (real released-defect repairs, tested). Phase 1 is open. Loose thread: `specs/acceptance/stage-11.md` still shows its own sign-off checkbox unchecked ("Ren sign-off pending") even though CLAUDE.md calls stages 0–11 signed.

**Phase 1 (2026-08-14/15): IMPLEMENTED, artifact published, awaiting Ren's sign-off** in
`specs/acceptance/history-core/phase-1.md` (checkbox left unchecked). Six commits d7fd9e8 → e52d0c8:
contracts + envelope/anchor/retention registry (ADR-020 records six resolved plan-vs-target-doc deltas,
e.g. doc-literal `open/commitStep/publish/recover`, ref reads on the reader, RefAdmin admin-only,
pending→`unknown`); in-memory + Postgres adapters pass one factory-driven conformance kit (46 identical
titles each; Postgres adds 2 writer-exclusivity tests); migration 032 (10 perimeter tables, RLS,
append-only triggers); micro-host (4 scenarios × 2 adapters + mechanical dependency-closure test);
HC1.6 drills. Gate: `--phase 1` release ran green (targeted 135/6 files, workspace 714/110 files,
~7 min, disposable PG16); artifact `7c91663f…` at candidate 0360405; `--phase 1 --verify` and
`--phase 0 --verify` both green. Notable deferrals recorded in ADR-020: object-level erasure via the
port → Phase 4; Postgres adapter deliberately NOT re-exported from the public entrypoint (B01 keeps
raw-store out of the perimeter closure); one step per batch; no `absorbed` settlements yet. After
sign-off: Phase 2A (Authority/Invocation/Ingress bridge, size XL).

**Phase 2A (2026-08-15): COMPLETE, superseded artifact published, sign-off open.** Commits f4bfcde
(domain authority/invocation/continuation vocabulary + 3 vector files + ADR-021), f2587f2 (durable
authority ledger: migration 033, permits/budgets/revocation-epochs with two conformance drivers),
a2353d3 (authority-port/v3 + parser consolidation into domain/authority/grants.ts), 69aa4dd (ingress
attestation shadow + legacy envelope reader — live-product rows are `partial` by honest design),
1e027d2/5e71331 (first gate), then the **independent delta review**
(specs/reviews/2026-08-15-phase-0-2a-delta-review.md: 3 P0 — forged permits, manifest split-brain,
revocation race; 9 P1 incl. unverified envelope identity on the write path) remediated in e0c2421 +
a31ec18 (migration 034), review archived 62302ea, superseding artifact e8d0047/68d01d2
(`074c7adb…`, supersedes `6366062c…`, 114 pinned titles). ADR-019 marked **constitution candidate**.
Under Ren's overnight standing directive ("no more signs, make your own judgement") sign-off boxes
stay unchecked with continuation notes; classifier blocks checking boxes on Ren's behalf — use
annotated-unchecked form. Findings for Ren: ops.session_commands.request retains raw refused
payloads (Phase 4 owns projection); Postgres history adapter deliberately not re-exported from
public entrypoint.

**Phase 2B (2026-08-15): COMPLETE, artifact published (`d79879c1…` at candidate f8a1830), sign-off
open.** a952f61 domain continuation vocabulary (ContinuationRequest/v1, ResolvedContinuation/v1 with
six pinned|unavailable|refusal slots, ResolutionId = whole-record cr-history-payload-v1 digest,
16-kind validator, resolution-v1.json vectors, ADR-022); d04f6c8 runtime resolver (7 read-only ports
make "latest config without identity" inexpressible; legacy adapter values-only; no-contact shadow
with recorder+tripwires; runtime→compiler/store edges avoided via injected values/structural types);
f8a1830/c2f1a51 gate (29 pinned titles incl. gates a–h, workspace 989/989). Known wart: `--phase 2a
--preflight` doc-marker check now stale vs ADR-019 candidate status (verify unaffected). Resolver is
consumable by Phase 3's materializer; nothing live calls it.

**Phase 3 (2026-08-15): COMPLETE, artifact `ee807e8b…` at candidate a564ce6, sign-off open.**
618dd29 domain context vocabulary (7-axis CandidateAdmission, SourceObservationBundle structurally
claim-free, MaterializationId/CompilationKey, vectors); 139b3c1 pure compiler core (compiler/core
subpath, compilation-record/v6, single selection engine — legacy v4/v5 facade routes through it with
legacy-ordering module, renderers + render-loss/v1 + ArtifactSink, debt D03 closed, cross-locale
tr_TR/TZ/process goldens); 4a4d9ea runtime coordinator (candidate-admission engine — provenance from
runtimeFacts only, closing indexer self-assigned authority; context-materializer with ScopedAuthorityRef-
scoped source ports; context-sources adapters incl. legacy-parity; compiler-shadow with allow-listed
projection deltas {authority,reason,source}); gate 1b53532/ce3bb63/a564ce6/38daa2c (78 pinned titles,
built-closure static over dist, workspace 1120/136). Runtime→compiler edge opened deliberately (no rule
violation). Watch: frozen workspace source-policy scan rejects any test property named `retry`.

**Phase 4 (in progress, 2026-08-15):** 92999f9 HC4.1/4.5 domain products+evidence (subpaths ./products
./evidence; FinalTransitionProduct = view over Phase-1 value with identical digest; RefPublicationAdmission
carries policy alongside unchanged Phase-1 value; normalizers total; ReplayMode vocab); 250fbf5 HC4.2/4.6
ModelGateway (runtime/src/model-gateway; migration 035 ops.invocation_attempt_events append-only; ai
runtime-model-adapter capability table; replay modes; crash rows 1–8,11 tested; no retry path at all).
Then: 9a3d3b2 HC4.3/4.4/4.5 (EffectGateway over existing intent machinery, ProposalSink receipts,
PublicationCoordinator over Phase-1 port, evidence as canonical envelopes — no migration); 09fab1e HC4.7
(mediated host publisher; FinalTransitionProduct value function ALIGNED to what History verifies — my
decision, vectors regenerated pre-artifact); 75e9eec adjunct PARTICIPANTS (owner-extension registry
dispatched inside the transaction — my decision; langgraph checkpoints through coordinator; legacy
HostPublisher DELETED); ddbd569/d0a2503 rollout bundle validator + gateway-shadow + drain/rollback +
MEDIATION_MATRIX; 82032b3 open-phase participants (session turn-origin) + canonical v2 invocation
envelopes cited by transition.citations/v1 strong link + perimeter export; 98cf20b CHAINED batch steps
(history.transition-write/v2 — my decision; closes Phase-1 one-step OPEN; no migration; vectors unchanged);
649012a product gateway composition root (live ports); 4685dda dialog reducer (DAG-equivalence proof vs
TransitionEngine); edac826 ACTIVATION: product chat path gateway-active (resolver→materializer→compileCore→
render→ModelGateway→v2 envelope→2-step chain→coordinator; legacy publish provably unreachable), marker
effect gateway-active, providers active, matrixIsFullyMediated=false honestly. 51643bf agent-store test
20s budget. **Phase 4 GATE PUBLISHED**: 1fca383/f90e3d6, artifact `1c586fbb…` at candidate 1fca383
(197 pinned titles, targeted 265/28 files, workspace 1404/164 files, ~7 min; artifact embeds the
mediation matrix; 4-kit adapter parity). Six artifacts verify (0,1,2a,2b,3,4). Sign-off box open.
Peer-session worktree removed after it committed; root `pnpm check` green.
NOTE: an interrupted agent's uncommitted work can be substantial and green — always assess disk state
before re-spawning. Agents stop on architectural forks — close forks explicitly in briefs.

**Phase 5 (2026-08-15): COMPLETE, artifact `4c8f0ced…` at candidate a8a2137, sign-off open.** bd0e752
HC5.1–5.3 (domain ./activation: OperationId whole-record digest, lease/batch lifecycle laws; runtime
scoped-capabilities server + frozen facades + RevocationRegistry + OperationJournal; step-coordinator with
cause bundles, driver-reentry + enclosed-loop); be635e8 HC5.4/5.5 (DecisionDriver optional profile —
ports optionality structural; scoped-rpc in-process+IPC; agents reference-driver via
AgentGraph.scheduleThroughActor; product chat as driver; deterministic + external-child fixtures under
packages/runtime/test/fixtures/history-core/); b1518e3 HC5.6 (9-title attack suite identical across
internal/external actors; `actors` rollout axis legacy|scoped-shadow|scoped-active; scoped-active chat
identical to gateway-active with directPathCounters all zero); gate a8a2137/a37445c (69 pinned + parity,
workspace 1491/175, actor built-closure static). Seven artifacts verify. Next: Phase 6 (dependency
inversion: constructor inventory HC6.1, TransitionEngine inversion HC6.2, purpose ports HC6.3, product
composition root HC6.4).

**Phase 6 (2026-08-16): COMPLETE, artifact `c9eb180b…` at candidate aae6789, sign-off open.** f6ba80e
HC6.1 dependency-ledger (1239 entries, 0 unclassified); fb992c3 HC6.2 runtime/src/ports + createTransitionEngine
(semantic layer only — coordinator owns publication; 12 conformance drills × 2 adapters); 01e1712…29ab141
HC6.3/6.5 purpose ports per package (host/langgraph/memory/session/terminal/agents/tools-worker) + compat
factories with injected counters; 21bd49e tools runtime-side ports; de603d5 HC6.4 product composition root
(product/src/composition, ActiveImplementationManifest, DualPathError detector); 8507d7b HC6.6 guard — 10
boundary rules evaluated over source+decl+built (was Phase-0-only); 91c83ef REALM carried through the
perimeter (AdmittedTransition.realm, transition-write/v2 realm — my decision, closes the HC6.4 STOP);
2139f09 product DEFAULT rollout = SCOPED_ACTIVE (legacy explicit/counted); gate aae6789/335fbf9 (workspace
1585/188). Eight artifacts verify; phase-6 --verify takes ~4 min (re-derives 3-plane guard). Next: Phase 7
(agent semantics / control-host split).

**Phase 7 (2026-08-16): COMPLETE, artifact `55c16794…` at candidate 216812a, sign-off open.** 2861f3b
HC7.1–7.4 (agent.lifecycle/v1 State fact via Proposal→transition — my decision: canon.agents.status
reinterpreted as INITIAL status, three-fact resolution; migration 036 ops.agent_control_* with role
context_runtime_control lacking canon privilege; AgentStore compat facade; agent-state-ownership.json 46
loci + validator); ce2ba29 control kit 14×2 + HC7.7 recovery drills; e2741f6; 8b1678b HC7.5
AgentDecisionDriver (reference driver = preset over it; agent origin in shared 9-attack array); 82c4f65
Agent ContextSource (planAgentScopedSelection lifted; equivalence proof); 2385687 HC7.6 spawn-request/
collaboration/derivation-witness families + spawnFromRequest + 27 adversarial tests (no migration).
Gate 216812a/864ae76 (115 pinned, workspace 1702/198). Nine artifacts verify. NOTE: phase-6 verify ~4
min, phase-7 verify ~8 min (re-runs dependency verifiers) — Phase 8 gate must bound dependency checks to
digest+ancestry. Next: Phase 8 (framework integrations / executable coverage; needs
HISTORY_CORE_EGRESS_SANDBOX_RUNNER for the OS-sandbox gate).

**Phase 8 (2026-08-16): COMPLETE, artifact `8adc5d74…` at candidate f23384f, sign-off open.** 434a86b/
ae2d8d4 HC8.1 (domain ./integration IntegrationContract + 12-dim coverage lattice, effective =
min(declared, max(observed, enforced)); runtime integration-coverage generator; integration-coverage.ts
CLI; specs/history-core/integrations/*.json — 13 profiles); HC8.2 LangGraph hosted-full/resident/level0
(9e3f7d2/1f29da7/26c46b3, api-surface digests from installed .d.ts); HC8.3 AI SDK facade (LanguageModelV4
implemented, not wrapped)/resident (5aec9c1/63b26db/6a5abd7); HC8.5 ADK probe PASS + packages/adk-adapter
(22nd project; @google/adk 1.6.0 pinned; ae634d8/8e755f2/fc5a8d3); HC8.6 peer fixture (68d9c1c); HC8.7
isolation tiers incl. Seatbelt egress-contained via bench/scripts/history-core/egress-sandbox.ts,
HISTORY_CORE_EGRESS_SANDBOX_RUNNER=seatbelt (9c0c2cc); HC8.8 hostile driver — egress tier hostileNoBypass
TRUE (d4ad62e). Gate 4b88066/f23384f/29316fa (149 pinned, workspace 1907/214; six-origin attack parity).
Verify cost FIXED: cheap dependency validation (readPublishedArtifact) — phase 7 8min→4s, phase 8 5s;
phase 6 still ~4 min (owns guard re-derivation). Ten artifacts verify. 6c13bd5 removed stray build output.
Next: Phase 9 (census, evidence-based freeze, retire legacy/shadow, spec/ADR reconciliation, historical
verification, release.json + phase-9.json; independent final review archived in specs/reviews/).

**Phase 9 (2026-08-16→20): COMPLETE — release candidate published, Ren SIGNED 2026-08-20** (first
explicit sign-off since Phase 0, recorded in `specs/acceptance/history-core/phase-9.md`; phases 1–8 keep
annotated-unchecked retrospective boxes). Census + freeze register
(`specs/history-core/freeze-registry.json`: 9 freeze, 6 frozen-legacy-read-only, 1 private-versioned
(ContextIR), 1 experimental (agent families); IntegrationContract freezes only its 30 exercised fields;
no package split) + ADR-029. Migration 037 drops only the two rebuildable Invocation V2 shadow relations
(001–036 byte-identical). Rollout collapsed to one value per axis (v2-active / active / active /
gateway-active / scoped-active), matrix fully mediated, direct/dual/compat counters zero, drain
instrument retained for compatibility-release safety. supersession.md §11 (ten §9-question dispositions)
+ §12 (final supersession map); plan-digest supersession over Phases 0–8 with their artifacts still
independently verifiable. Release gate = full candidate: all 10 predecessor artifacts + lineage, 22-file
retirement suite (≥200 titles, zero-skip reporter), whole workspace, Stage 11 acceptance,
desktop+mobile Playwright `--retries=0`, Biome, seatbelt egress probe → byte-identical
phase-9.json/release.json in one commit; candidate pair at 5aaf5fe, superseded by the final release
pair at 1a325f0 (source candidate 844891f).

**ACCEPTED (2026-08-21):** the authorized independent final architecture/security/migration review
(`specs/reviews/2026-08-21-phase-9-final-review.md`) concluded **0 P0 / 0 P1, 7 P2** — eligible for
accepted/frozen. ADR-019 = constitution + public freeze accepted, ADR-029 accepted, both limited to the
exact machine-register scope (experimental/unproven dimensions stay unfrozen); phase-9.md governance
boxes both checked (phases 1–8 retrospective boxes stay annotated-unchecked). plan.md updated: the
Phase 9 architecture is now the current source for History/continuation/authority/mediation; v0.9 stays
authoritative for un-superseded product/Encounter material and as the historical source of the Twenty
Laws. The 7 P2s are a hardening backlog: title binding starts after canonical genesis; one bad browser
retry record / key rotation can strand a principal's queue; production-boundary inventory has syntactic
blind spots; drain admission is process-local and misses originless pending commands; ForkContext pins
a binding before a possible refusal; a SIGKILL between artifact renames needs operator repair; exact
retries are rate-charged before idempotency lookup. **Next: ADR-030 (proposed, post-freeze design)** —
"standing over purity": departures as transitions, held worlds, per-ref standings (guaranteed ·
examined · unexamined), operation table; work packages open on Ren's go, accepted only with D1–D4
artifacts + sign-off; evidence pinned at 9e11319. Migration guide `specs/migrations/history-core.md`.
CLAUDE.md status refreshed and merged to main (34b7ec3, 2026-08-21).

**Binding constraints:** frozen assets list (§1.1 — never weaken canonical bytes, OCC, fencing, effect bracket, erasure, replay, tenancy); additive canonical evolution only; one active writer per semantic; rule of two (ContextIR stays private until a second renderer; no package splits without two consumers); ports before packages; every phase independently mergeable and stoppable.

**Gate mechanics to remember:** entrypoint `node --import tsx bench/scripts/history-core-acceptance.ts --phase N`; release gates provision their own disposable PG16 cluster (no caller DB URL) and need a clean committed worktree. On 2026-08-14 (Ren's direction) the Phase 0 release path and its four harness self-test modules were deleted: `--phase 0` now only supports `--preflight` (static checks) and `--verify`, which validates the committed artifact (content + candidate ancestry + committed bytes, titles frozen as data in `phase-0-artifact.ts`) and stays green as the branch moves — the publication-time exact-diff proof is fixed at commit 523bded. The checked-in inventories (`specs/history-core/package-boundaries.json` ~40k lines, `constructor-inventory.json`) are exact snapshots: any source change anywhere makes them stale and preflight fails until `package-boundaries.ts --write` regenerates them (review `activePhaseZeroViolations` stays `[]`). Day-to-day `pnpm test`/`check` is untouched by any of this.
