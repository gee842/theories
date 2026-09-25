# ADR-030 — Everything is a plugin: the truth layer, the runtime fleet, and the control plane

- **Status:** **implemented — awaiting Ren's sign-off** (2026-08-23). Every work package landed
  under `pnpm test`: engine `main` `a483b7a` (216 files, 1981 tests), product `main` `c8950ff`
  (66 tests); the per-package notes under `specs/acceptance/history-core/` are indexed by
  [`adr-030.md`](../acceptance/history-core/adr-030.md), which also lists the decisions only Ren
  can make. Acceptance stays his act, split as below. Proposed as the converged scope (Ren,
  2026-08-21), superseding two same-day drafts of
  this number (archived as git history at `16c7ce1` and `708a03f`; git is the archive of record for
  same-day iterations of one number). Acceptance is **split in two**: the semantics-and-surface
  program (D1–D4) accepts on its own artifacts and Ren's sign-off, independent of Cordis — none of it
  touches the adoption; the platform program (R0, W1–W6) accepts separately on its artifacts and
  Ren's sign-off. W0 has run and returned **GO** (2026-08-21); its per-gate disposition is in
  `specs/acceptance/history-core/w0.md`. The Phase 9 prerequisite is satisfied (artifact pair
  published; Ren's sign-off 2026-08-20; independent final review 0 P0 / 0 P1 on 2026-08-21,
  `specs/reviews/2026-08-21-phase-9-final-review.md`).
- **Revision (2026-08-21, the freeze directive):** Ren lifted the freeze for **representational**
  constraints — "remove any frozen rules that is in conflict with our new design … prefer broken
  changes and since we are not launched, no legacy compatibility is needed … for any structural
  problems, I prefer a clean, coherent, longtermist refactor." This ADR therefore carries **R0, a
  one-time v1 reset** (see Work packages), and re-carves vocabulary that earlier drafts worked around:
  the realm axis, the Ref grammar, realm elision, the `standing`/`channel` split, and the idempotency
  vocabulary. Correctness invariants are untouched and were never in conflict. Two further revisions
  land here: the standing lattice is replaced by an **examination ledger** (decision 10), and the
  session seam is redesigned around a **two-plane encoding** after the effect bracket was found to be
  cadence-incompatible with chunk-grade durability (decision 4).
- **Revision (2026-08-22, ADR-031 — the gate policy):** Ren: *"the old guard guards the old
  architecture, but we need architecture upgrade … many places compromised design due to gate."*
  ADR-031 retires the closed-tree scanners and amends this ADR in four places, each marked inline:
  the freeze registry is no longer "regenerated and re-armed" but retired (its rejection in
  **Alternatives** is reversed on the record); D1's new families enter without ownership rows or
  freeze decisions; D2's gate drops the production-boundary `--check`; and D4's operation table is
  authored as TypeScript the carriers import rather than as a `--write`/`--check` JSON artifact —
  a table the carriers compile against is enforced by `tsc`, a table a checker compares against is a
  corpus that passes by construction. Decision 1's attestation observer is unchanged and is now the
  general answer rather than the mediation matrix's special case.
- **Execution (2026-08-22):** Ren: *"please finish adr 030"*. The remaining packages run as a
  parallel program of Opus implementers; the execution decisions the packages needed settled first
  are recorded in the **execution record** addendum at the end of this document. Status stays
  `proposed` until Ren signs the per-package acceptance notes.
- **Date:** 2026-08-21

**Context.** Ren's statement of intent, in three clauses: *our context system as a plugin, so not
only us — everyone in the ecosystem can install it* · *at the same time, a server where we have our
own UX and backend* · *the most elegant way to have a surface we can interact with, not only code
but conceptually.* Then, after reading `~/repos/deepseek-harness` and the deepseek-desktop pattern,
the sharpening: **everything is a plugin** — Cordis is more elegant and practical than building all
the wheels; adopt it as architecture; and the outer product should be a **multi-user web control
plane over isolated runtimes**, not another Harness UI wrapper. The convergence, in one line:
Cordis/DSH is the composition architecture of a runtime; the product is a separate control-plane
repository over a fleet of isolated runtimes, consuming pinned published upstreams — DSH *and*
context-runtime alike; and context-runtime is the truth layer under the fleet.

Two sentences govern everything below, unchanged from the original design and restated here because
every later reviewer must apply them: **this ADR relaxes policy refusals into recorded departures
read by a declared standing policy — nothing is silent, and nothing that used to be allowed becomes
refused.** And Ren's three archetypes — the pure writer, the working agents on a dirty shared
workspace, the free frontier — are **three policies over one mechanism, never three special cases**;
any clause that reintroduces a special case is a defect against this sentence.

Four findings made adoption the right call rather than a concession, each reversing an earlier
objection:

- **Mounting is trust in both worlds; Cordis makes the mounted set legible.** Our closure was always
  "a scan of code we chose to import" — in-process code is trusted code everywhere. A Cordis tree is
  *enumerable data* (`dsh --profile web --dump-config`), digestable at boot the way Σ is digested.
  The mediation claim survives with a better carrier: from a source scan to an **attested profile**.
- **HC6 already made the runtime plugin-shaped.** A purpose port is a service key; `inject`
  declarations are constructor dependencies; one-provider-per-service-key is one-active-writer-per-
  semantic, enforced by the framework's own composition. The HC6.1 dependency ledger is the
  mechanical input for conversion. Adoption is a re-mounting, not a rewrite.
- **"Even the agent loop is a plugin" is History Core's own conclusion.** Phases 5–7 demoted the
  loop to a non-authoritative scoped actor; a loop swappable from configuration is that demotion
  completed. And ADR-012 already ruled *composition as digestable data* — Cordis profiles are that
  rule realized at the host layer.
- **The deepest enforcement never lived in composition.** Append-only, one-open-turn-per-ref,
  `refs_guard`, `effect_observation_requires_intent`, RLS, the role split — Postgres holds them; no
  plugin tree repeals a trigger. Permits, budgets, attested egress live in gateway/kernel internals
  that become plugins with unchanged interiors. What relocates is only the *claim about the shipped
  composition*, and it relocates onto the profile digest.

What DSH does **not** have is equally load-bearing, verified in its own tree: the `/api`
browser-trust fence "is a reachability policy, not authentication; the Web carrier provides no
authentication layer" (`packages/client/connection/README.md:9`); the web server binds `127.0.0.1`
or `0.0.0.0` only (`packages/host/webserver/README.md:7`) and ships "No TLS, auth, or origin policy
… deliberately out of scope for the dev-facing v1" (`:21`); `SessionHeader`
carries no authenticated owner or tenant (`packages/core/session/src/types.ts:61`); `session.list`
merges every live and persisted session in the runtime
(`packages/host/apiproxy/src/api-proxy.ts:1720`); forwarded events have no per-user projection,
redaction, or scoped subscription (`packages/api/gateway/README.md:42`); identity is an anonymous
UUID per harness home (`packages/identity`); the bundled SQLite backend's synchronous writes are "a
throughput ceiling for busy multi-session servers"
(`packages/session/session-persistence-sqlite/README.md:58`); the session core has fork but no
merge, no OCC, no fencing (its docs name the concurrent-writer gap), no effect bracket, no
idempotency discipline, no erasure. A login page and a reverse proxy do not fix this; making two
users share one runtime with different permissions is a substantial capability seam (authenticated
principal through HTTP/WS, authorized lookups, filtered lists and event streams, partitioned
credentials and workspaces, actor attribution, per-user quotas), not an authentication plugin.

So the architecture is the one that lets DSH's global assumptions stay valid *and* lets our
guarantees do the work they were built for. The substrate is untouched: execution plan §1.1 — under
the accepted ADR-029 freeze — names what no phase may reopen or weaken, quoted: frozen canonical
bytes, StateId/NodeId and the digest vectors · existing migration bytes and
`frozen-migrations.json` · primary-basis/secondary-parent compatibility · Store-backed OCC, prefix
membership witness, race/branch semantics · durable effect intent, executor-class reconciliation,
fencing · availability ledger, namespace-aware erasure, restore reconciliation · replay
zero-provider guarantee · Postgres/Temporal semantic equivalence · tenancy/RLS, transactional
fan-out, host attribution · legacy readers and historical export/verify. Cordis composes runtimes;
canon holds truth; plugins are how the engine is *mounted*, never what it *is*.

**The architecture.**

```text
                          Browsers
                             │
                             ▼
              ┌──────────────────────────────┐
              │   Web control plane           │   login · organizations · membership
              │   (separate repository)       │   RBAC · billing/quotas · audit
              └──────────────┬───────────────┘   provisioning · updates
                             │
              ┌──────────────▼───────────────┐
              │  Authenticated runtime router │   HTTP + WebSocket auth — the seam
              └──────┬───────────────┬───────┘   DSH deliberately does not provide
                     │               │
        ┌────────────▼───┐   ┌───────▼────────┐
        │ Harness runtime │   │ Harness runtime │   one runtime = one security boundary
        │  (boundary A)   │   │  (boundary B)   │   = one DSH_HOME = one credential
        │  Cordis tree:   │   │  Cordis tree:   │     namespace = one session store
        │  loop · tools · │   │  loop · tools · │   = one sandbox = one mutually
        │  providers ·    │   │  providers ·    │     trusted group
        │  session log ·  │   │  session log ·  │
        │  OUR host +     │   │  OUR host +     │
        │  client plugins │   │  client plugins │
        └────────┬────────┘   └────────┬────────┘
                 │  SessionPersistence  │
                 ▼  (our provider)      ▼
        ┌───────────────────────────────────────┐
        │        context-runtime TRUTH LAYER     │   canon (append-only, OCC, fencing,
        │  Postgres: universes per boundary ·    │   effect bracket, erasure, replay
        │  RLS + per-runtime DB credentials ·    │   evidence, merge, export/verify)
        │  blob CAS · Temporal durable effects   │
        └───────────────────────────────────────┘
```

**Decisions.**

1. **Cordis is the composition architecture of a runtime — adopted, pinned, probe-gated.**
   Everything in a runtime is a plugin: the loop, tools, providers, the session log, our host and
   client extensions. We take the framework the way its biggest adopter does — DSH vendors Cordis
   4.0.0-rc.7 and its foundation, renamed into its own scope with a modification log, "so that the
   harness fully owns its framework layer" (`~/repos/deepseek-harness/vendor/README.md`; note the
   manifest table pins `4.0.0-rc.7` while `vendor/cordis/package.json` already reads `4.0.1` — the
   pin's source of truth is W0's to fix). W0 decides vendored-versus-published-pin for us with that
   precedent priced. Hard lines inside the adoption: **`packages/domain` stays zod-only** —
   schemastery is plugin-config vocabulary, never canonical schema; **production profiles disable
   HMR** and omit every dynamic-mount-shaped plugin — with the honest caveat that `ctx.plugin()` is
   a core `Context` method available to every mounted plugin
   (`~/repos/deepseek-harness/vendor/cordis/src/registry.ts:185, 316`) and Cordis has no seal, so
   "no dynamic mounts" is a property of what we mount, not a framework guarantee. For the same
   reason **attestation is a continuous runtime invariant, not a boot digest**: `--dump-config`
   composes patch layers without booting or evaluating `!!js`
   (`~/repos/deepseek-harness/apps/cli/src/dump-config.ts:1-5`), `disabled: !!js` re-evaluates at
   every mount decision, and waterfall listeners may `prepend` and short-circuit
   (`vendor/cordis/src/events.ts:114, 255`) — so the attestation record (decision 5) is written by
   an observer that watches post-boot mounts and listener registration on the mediated seams and
   **downgrades the recorded regime** the moment the composition changes. That is the mediation
   matrix's honest successor: a call-site scan proved a closed source tree; the observer records an
   open tree's actual state, and the record — not a static digest — is what a session's regime
   claim cites. One-provider-per-service-key carries the one-provider rule for *services*; which
   component is the writer of record for a *canonical fact* is decision 4's separate, stricter
   statement. The engine's inner packages (domain, store, kernel, compiler core, runtime services)
   remain framework-free libraries; bridge plugins mount them.

2. **The product is a separate repository: a control plane over pinned published upstreams — both
   upstreams.** Layout per the deepseek-desktop pattern:

   ```text
   <product>/
   ├── apps/
   │   ├── web/                  # browser product
   │   ├── control-plane/        # auth, orgs, RBAC, billing, routing, audit
   │   └── runtime-manager/      # provisions/starts/stops Harness runtimes
   ├── packages/
   │   ├── dsh-product-bundle/   # our Cordis profile/bundle
   │   ├── dsh-product-host/     # host plugins: truth-layer provider, gateways
   │   ├── dsh-product-client/   # Harness UI extensions: standing, DAG, approvals
   │   └── dsh-compat/           # narrow upstream-version adapter
   └── upstream/                 # optional read-only submodule, only while patching
   ```

   (*Execution record, 2026-08-22: `dsh-product-host` narrows to product-specific host plugins; the
   truth-layer provider and the gateways are the engine's published `@context-runtime/dsh-host` —
   see the addendum.*) The product consumes **pinned published packages** — `@deepseek-ai/*` and
   `@context-runtime/*` alike: our product trusts our engine exactly the way it trusts DSH, through published, pinned,
   semver-disciplined artifacts. That symmetry is the forcing function that makes the engine's
   publishing real (W1) and keeps this repo an *engine* repo. Publishing is **this ADR's own
   decision superseding ADR-011's ratified "packages private by default"** (`decisions.md:174`),
   named as such — it is not an HC9.3 trigger firing: ADR-029's reopening rows require "a real
   adopter outside this monorepo consumes History **without the runtime**" or "an external consumer
   needing an independently versioned artifact" (ADR-029 §HC9.3 table, rows quoted verbatim there),
   and a product repo we author ourselves is not that adopter. When a genuinely external adopter
   appears, the trigger fires on its own terms. Two channels — `stable` and `upstream-next` — test
   new upstream releases before promotion; the `dsh-compat` shim absorbs *renames and shapes*, and
   its real absorption budget is measured, not asserted — DSH's own vendor log records 18 local
   modifications including fiber-lifecycle and loader-semantics changes no shim can hide
   (`vendor/README.md`), so W0 replays the last N upstream bumps through the shim and records the
   actual diff size as the go/no-go input. This decision also **re-scopes two ratified ADRs by
   name**: ADR-015's "Stage 8 is the complete single-user Encounter product" (`decisions.md:275`)
   and ADR-014's thread-behavior-layer pricing, which declined a Beta-tier UI dependency precisely
   because of its "recurring migration tax" (`decisions.md:251-263`) — the answer this ADR gives to
   that priced objection *is* the channel discipline plus the shim plus the measured budget, and if
   W0's measurement shows the tax ADR-014 feared, the fallback stands. Not every part of the SaaS
   is a Cordis plugin: login, organizations, RBAC, billing, provisioning, routing, audit,
   deployment are the control plane's, in plain code — Cordis composes *runtimes*, and the control
   plane is not a runtime.

3. **One runtime per security boundary; sessions are refs; multi-user arrives in three stages.** The
   isolation arithmetic, extended by one term: one runtime = one `DSH_HOME` = one credential
   namespace = one session store = one filesystem/sandbox boundary = one mutually trusted group =
   **one `session/*` ref namespace in the boundary's universe** — a session id is boundary-local, and
   two boundaries reusing an id cannot collide because refs are universe-scoped. Stages are
   unchanged: **(1) multi-account MVP** — one isolated runtime per user; **(2) shared projects** —
   one runtime per project, gated on per-member attribution reaching canon, because host attribution
   is a §1.1 invariant and DSH's `SessionHeader` carries no owner
   (`~/repos/deepseek-harness/packages/core/session/src/types.ts:61`); **(3) fine-grained RBAC** —
   built only if projects need admin/member/viewer. Defense in depth is why this beats both parents:
   the process boundary (theirs) × per-runtime database credentials × RLS on every canonical row
   (ours) means even a compromised runtime reaches only its boundary's universes.

   Three review-forced corrections make that sentence true rather than aspirational, all retained.
   **Role provisioning is out-of-band:** migration 019 raises "owner roles violate the least-privilege
   contract" if the definer or DDL role holds CREATEROLE
   (`packages/store/migrations/019_stage9_security_hardening.cjs:13-25`) and migration 031's pattern
   is that privileged attributes are "externally provisioned … instead of granting the DDL owner
   CREATEROLE" (`031_gc_maintenance_bypass_rls.cjs:23-26`) — so the runtime manager draws from a
   fixed pool of boundary-class login roles and never mints one per signup; the one credential that
   performs role DDL is control-plane-held and out-of-band. **Ticket minting is a control-plane
   service:** `issuePrincipalContextTicket` accepts an arbitrary caller-supplied principal
   (`packages/store/src/principal-context.ts:21-57`) and principal-mode stores default the attestor
   pool to the same connection string (`postgres-store.ts:1557-1567`), which inside a runtime hosting
   foreign plugins is a cross-boundary key — so a runtime process never holds worker or attestor
   credentials, `attestorDatabaseUrl` points at the control plane, and W2's drill is an **in-process
   attacker**, not a stolen connection string. **The control plane writes the tenant's
   `policy/standing`** at provisioning: a policy that lets its subject discharge its own debts is the
   one thing the ledger must never permit silently (decision 10).

   One addition from the session projection. The **fleet-wide single-writer rule for session-bound
   refs** is part of the boundary contract: *at most one live writer per session id per fleet — the
   runtime holding the `session/<id>` lease; every fold, repair, and fork-seed publication is a fenced
   CAS at that lease's fence (`postgres-store.ts:2395-2406, 3572-3586`); an administrative fence
   supersession revokes the writer; the halt plugin converts any `race | fenced | authorization |
   policy` refusal into fiber disposal within one flush checkpoint.* It needs no new policy row — the
   ref class, `ops.leases`, and the fenced CAS already carry it, and DSH's own one-live-session-per-id
   store rule covers the intra-runtime half. The drill is two processes on one session id: exactly one
   fold wins per window, the loser halts, the projection stays linear.

4. **context-runtime is the truth layer: a `PersistenceBackend` under DSH's own coordinator, and
   everything a log alone cannot promise.** We do not implement the raw `SessionPersistence` service.
   `PersistenceCoordinator` is exported from the package root
   (`~/repos/deepseek-harness/packages/session/session-persistence/src/index.ts:44-58`) and the SQLite
   backend composes it exactly this way
   (`packages/session/session-persistence-sqlite/src/index.ts:99, 122, 134`), so we implement the
   eight-primitive `PersistenceBackend` — `loadStored`, `readStoredRevision`, `loadStoredFrom?`,
   `appendBatch`, `commitRepair`, `list`, `locate?`, `close?` — and inherit write-behind batching,
   per-session serialization, dispose quiescence, HMR live-prefix adoption, the prepared-session LRU,
   live-id guards, and repair sequencing. **`TornMarker` is vacuous for us**: a canon publication is
   atomic, so canon has no torn tails and the whole truncation arm of DSH's crash model disappears.
   Passing the vendored `runPersistenceContract` *and* our published kit is the gate, under six
   rulings.

   - **Writer of record, and one writer per session.** Canon is the writer of record for session
     truth; DSH's in-memory log is a derived operational projection (Law 3), never read back as
     authority — with one honest exception: during HMR adoption the live in-memory log is the recovery
     source for the listener-down window, which is adoption of *our own* uncommitted tail, not foreign
     authority. A session binds to exactly one ref, `session/<sessionId>` — a **ref class**, admitted
     by decision 8's uniform grammar. The single-writer rule is decision 3's.
   - **Two planes, because the bracket and chunk-grade durability cannot share one cadence.** This is
     the finding that invalidates one-publication-per-append-batch. DSH requires `append` to resolve
     only after durability (`session-persistence/src/index.ts:79-82, 133-143`), on a ≤200 ms
     write-behind window; our effect bracket holds a canon turn open across a whole tool execution,
     because the observation trigger requires intent and observation **in the same turn**
     (`packages/store/migrations/002_guards.cjs:20-38`), a ref has one open turn
     (`postgres-store.ts:2384-2418`), and `publish` refuses while an intent is unresolved
     (`postgres-store.ts:3559-3571`). A thirty-second tool would therefore stall every log append on
     that ref for thirty seconds. The resolution is already canon's own: **HC4.7's pending-writes
     journal**, which folds `ops.host_pending_writes` rows into the next canonical checkpoint inside
     the publication transaction (`postgres-store.ts:2760-2791`). So the provider appends into
     **`ops.session_log_staging`** — payload blobs to the CAS first, then rows, in one transaction;
     durable, turn-free, and with latency independent of tool duration and tree size — and **folds one
     canon node per DSH turn** (plus idle-flush and repair folds). Fold cleanup is by watermark and
     idempotent, so a crash between fold-commit and sweep is harmless, and the narrow `StageWriter`
     allowlist (`packages/store/src/stage-writer.ts:21-30`) does not widen. "Append ↔ records in
     turns" becomes literal rather than aspirational: one node per DSH turn, its patch naming exactly
     the events it folded.
   - **The log is a state domain with its own merge row.** Leaves live at
     `sessions/<id>/log/<pad12(seq0)>` with the header at `sessions/<id>/meta`; zero-padded
     fixed-width keys make the tree's bytewise-UTF-8 sort numeric (`packages/domain/src/tree.ts:33-43`)
     and the fixed-fanout trie absorbs wide nodes invisibly (`tree.ts:19`). Each leaf is one DSH
     `StorageRecord`: `packChunkRuns` / `decodeStorageRecord` are reused **verbatim**
     (`~/repos/deepseek-harness/packages/core/session/src/chunk-rows.ts:192, 339`; ~56× measured,
     `:7`), and anything they refuse to pack stores as-is, so a future chunk shape loses compression
     and never data. Around that record we add the split DSH has no reason to make: **envelope
     inline, content in a blob** — seq window, `time0`/`dt`, type, turn/step, `surfaceOp`,
     `sourceEventSeqs`, and structural keys (message id, provider/model, callId, usage) stay inline;
     content-bearing `data` becomes a `link` to a blob in namespace `dsh-session/<originSessionId>`,
     subject-overridable per policy (the ADR-018 pattern, universe-partitioned,
     `packages/store/src/blob-store.ts:75-101`), with `link` the only door for blob-shaped values
     (`packages/domain/src/patch.ts:43-53`). A new merge row — `sessions/**`, strategy `domain`,
     continuation `never` — **rejects** on any true conflict, because a `$contested` log leaf would
     poison the projection; one-sided subtrees still copy under the structural pass and are inert (the
     projection reads only the bound ref's own subtree), with `lint` reporting them. `forbidden` was
     rejected: it would refuse even one-sided copies, making any merge between two session-bound
     working refs impossible — which is exactly the dirty-workspace archetype. `sessions` joins the
     reserved-root list (`packages/session/src/domain.ts:180`).
   - **Fork is ref creation; departures are revisions, not events.** `ctx.sessions.fork(source,
     boundary?, childSessionId?)` already mints a child id and requires the boundary outside an open
     turn, so it maps to `RefPublicationMode` fork: a child ref at the node whose fold covers the
     boundary, seeded with the trimmed subtree plus `parentSession`/`seedLength`. Cost is near zero —
     identical leaves hash identically, so the prefix dedupes and the child cites the *same* payload
     blobs, which is what makes **erasure reach every fork** rather than stranding them. A merge's
     secondary parents, a `runtime.adopt`, or an administrative `advanceRef` on a session-bound ref
     surfaces DSH-visibly as a **`SessionPersistenceRevision` change of the whole stored log**: the
     live writer is fenced out and halts, and the next cold `prepare()` reads the new head. An in-log
     departure event is **rejected** for four reasons: it would claim a position inside the very
     sequence the departure rewrote; `ignorable`'s contract is that a reader "may safely skip" a
     record "whose loss cannot affect reconstruction"
     (`~/repos/deepseek-harness/packages/core/session/src/types.ts:412-422`), which any event a reader
     must understand violates; DSH validates seed contiguity and would refuse a log implying a gap;
     and there is no live consumer, because DSH never reloads a live session. The departure is
     recorded in canon with its envelope and explained by `lint`/`explain` — a **carrier-local
     absence with its reason**, which is precisely what decision 6's parity law provides for. Nothing
     is silent; the log is simply not the carrier.
   - **Crash repair: canon wins, mechanized; graceful dispose needs none of it.** Staged rows and the
     durable intent survive `kill -9`; the reconciliation scanner — **extended from its live-only pins
     (`packages/tools/src/execution-outbox.ts:140, 143-145, 259-261`) to `session/*` refs** — resolves
     the intent by executor class; `commitRepair` then publishes one `session.repair` transition
     folding the staged tail plus the coordinator-computed closers as log leaves marked
     `origin: "repair"`, so the returned log satisfies the foreign contract's shape while canon can
     always distinguish loop-written from repair-written events and never records a fabricated
     observation. An intent that cannot yet resolve makes `load()` refuse `transient` after a bounded
     wait — our one recorded contract deviation. **Graceful dispose is not this case**: the loop's own
     `finally` appends `turn/end` with `reason: {kind:"aborted", …}` on cancellation
     (`~/repos/deepseek-harness/packages/core/agent-loop/src/agent.ts:303-321`), so the log is already
     balanced; dispose is a bounded drain to staging, needing no open turn, no fence progress, and no
     tool quiescence, and the scanner releases the ref. None of the bad triad is taken — nothing
     fabricated, nothing permanently abandoned, disposal not blocked on quiescence.
   - **Erasure has a log representation — two forms, split by surface eligibility.** The earlier
     single-form ruling was wrong. `ignorable` licenses a reader to *skip*, and surface folding
     requires every seq a later `replace {start,end}` cites to exist as a surface node — so a redacted
     `user/message` turned into a skippable foreign-typed event would break folding and would lie
     about affecting reconstruction. Erase the payload blob under its namespace
     (`blob-store.ts:248-274`), keep the envelope leaf, and synthesize: **surface events** keep their
     type, envelope, `surfaceOp`, `sourceEventSeqs`, and structural keys, with content replaced by a
     typed-absence block — never `ignorable`; **log-only content events** become a
     `context-runtime/redacted` event with `ignorable: true`, honestly, because skipping a log-only
     record genuinely cannot change reconstruction. The state-object erasure lane
     (`packages/store/src/tree-codec.ts:225-237`) stays the wrong tool here: it removes the envelope
     too, leaving nothing to synthesize from.

   `materializeState` is demoted from correctness-gate to throughput work by the fold cadence: it
   re-hashes the whole tree per call today (`tree-codec.ts:159-197`) but now runs once per DSH turn,
   not per batch. The incremental implementation the frozen spec anticipates
   (`packages/domain/src/tree.ts:9-12`) must make fold cost proportional to the window and handle trie
   rebucketing; W2 carries it with a measured whole-tree ceiling as the recorded fallback.

   What canon adds that no other backend can is unchanged: OCC and fencing across processes (the
   "liveness signal beyond the log" DSH's own docs say concurrent writers need), branching **with
   merge** and contested values, erasure and availability with subject namespaces, replay evidence and
   export/verify, standing-labeled sharing (decision 15), and Temporal durability for effects. The
   semantic lens stays normative for the product with the opaque `HostCheckpointCodec` carrier as the
   ecosystem floor; universes-per-boundary granularity is a W2 recorded decision; and because
   `SESSION_FORMAT_VERSION = 0` ships with "no migration" upstream (`types.ts:34-56`), the truth layer
   owns a session-format upgrader and channel promotion is gated on format-version equality.

   `OPEN:` the session ref's creation base — fork from the anchor head (inherits workspace) or from
   genesis (pure log) — is a product-policy default, recorded in W2.

5. **Mediated contact ships as host plugins; coverage claims are per-profile; frozen guarantees are
   not.** The model gateway (permits, budgets, exact products, attempt ledger) mounts as the tree's
   `ctx.llm`-facing adapter; the effect bracket guards the
   `tools/pre-execute → execute → post-execute` waterfall; approvals and standing preconditions ride
   the same plugins. What varies by profile is **coverage** — said in the `IntegrationContract`
   vocabulary as an additive `composition-attestation` dimension defaulting `unsupported`. What does
   **not** vary, because §1.1 admits no scope qualifier: **replay's zero-provider guarantee and
   executor-class effect reconciliation fail closed rather than degrade** — replay refuses to run a
   composition in which any non-tape provider is reachable, and a tree that bypasses the bracket has
   *no* effect guarantee, not a weaker one. The regime a session ran under is recorded by the
   **composition attestation record**, written by decision 1's observer, and it is a ledger *input*
   (decision 10), not a parallel vocabulary.

   Three sharpenings from the integration design. **The bracket's turn is the session's turn**: the
   effect bracket asks the provider's session-canon-binding service for the open canon turn instead of
   minting its own, so a turn's intents, observations, and log fold share one node — decision 4's
   cadence, enforced rather than hoped for. **The ladder's residue is named precisely**: a DSH-loop
   composition stamps unmediated wall-clock at exactly three session-core sites
   (`~/repos/deepseek-harness/packages/core/session/src/index.ts:152, 630, 880`), while its two large
   nondeterminism sources — model streams and tool I/O — already route through seams we mount
   (`ctx.llm`; the bracketed waterfall). So such a composition reaches *auditable*/*reconstructable*,
   and the fleet's truth pitch is OCC + fencing + merge + erasure + Temporal, with replay as the
   engine verifying itself. **One upstream contribution is filed, and nothing gates on it**: **U1**, a
   Cordis `clock` service (default provider `Date.now`) consumed at those three sites and in the loop
   — independently attractive upstream because their own chunk-row tests already fight wall-clock
   (`chunk-rows.ts:34-36`). With `ctx.llm` mediated, the bracket on the waterfall, the clock through
   our seam, and HMR omitted, such a composition could claim *replayable-for-the-mediated-surface* —
   bounded permanently by the facts decision 1 records: `ctx.plugin` is reachable by every mounted
   plugin, Cordis has no seal, and un-bracketed plugin I/O is invisible. That bound is exactly why the
   attestation *record*, not the composition, carries the regime.
6. **The conceptual surface is the vocabulary, carried wherever a carrier exists.** The elegance
   clause lands as: one vocabulary — universe · ref · anchor · turn · record · claim · effect ·
   approval · departure · standing · examination · world · receipt — rendered by **client plugins** in
   the Harness UI (the standing badge, the DAG, approvals, `explain`/`lint` views), bound by **host
   plugins** as service keys and operation-table entries, spoken by the **control plane** as
   organizations/boundaries/universes, all projections of canon. `channel` — the admission axis
   renamed in decision 10 — is deliberately absent from this list: it is compiler-internal vocabulary,
   not a surface noun. The parity law survives translation: a verb on one carrier is a defect until it
   exists on the others **or is recorded carrier-local with its reason**; the checker walks profile
   trees and the control-plane API surface instead of a monorepo scan. Decision 4's departure-absence
   from the session log is the first deliberate use of that second clause.

   The code carrier is the **Mediated Runtime operation table**. The three wires that exist: `engine/1`
   (host; commands only, `packages/engine-wire/src/domain.ts:39-52, 151-160`), `encounter/1` (session),
   `scoped-rpc/v1` (actor; 8 methods; consumer B of the `activation-and-step-protocol` — a ninth
   method is a new protocol version). **Three write shapes**: `submit(proposal)` — the kinds; admitted
   ref publication — `RefPublicationMode` create/advance/fork, where ref creation decides an exact
   product and consumes a one-use permit (`packages/product/src/gateway/ref-creation.ts:38-125`);
   extension repository ops (`SpawnAgent`, `packages/agents/src/ports.ts:33-40`). **Reads are a third
   capability**: a principal-authenticated projection over `HistoryReader` narrowed by
   `VisibilityScope`, under the existing `context.read_state|query_index|read_artifact|hydrate` scopes
   (`packages/product/src/runtime.ts:161-166`; the same four reappear as raw strings at `:3425-3428` —
   the table names one constant), never the reducer-grade `ScopedHistoryView`; `explain(node)`
   re-bases `inspectNode` (`packages/session/src/projection.ts:511-573`) on the reader plus the
   compilation record, and for a session ref renders the turn's event window, its effects, and its
   evidence; `lint` per decision 9 — today an external actor has no read at all, the largest single
   gap between "integrable" and "usable". **Situation overlay**: a per-request `contextPolicy` on the
   existing continuation-request slot (`packages/domain/src/continuation/request.ts:97-101`); the
   product's two named-default pins (`chat-turn.ts:620`, `:604`) de-duplicate;
   `PRODUCT_COMPILER_IMPLEMENTATION` bumps and drops the policy from the implementation digest
   (`product/src/gateway/identity.ts:76-84`). **Receipts**: `ProposalReceipt`'s six arms verbatim
   (`packages/runtime/src/proposal-sink/receipt.ts:67-121`) plus additive
   `evidence: EnvelopeAddress[]` on the durable arms — the surface-visible "detected"; the closed
   `preimages` field is the precedent, and the receipt is a runtime API type outside the frozen
   canonical surface.

   Two clauses simplify under R0. **Idempotency is one vocabulary.** The census, verified at the mint
   sites, found three syntaxes for one concept — `commandId` (`packages/session/src/domain.ts:154`),
   `proposal/<digest>` (`packages/runtime/src/proposal-sink/index.ts:44`), and five `product/*` lanes
   (`canonical-command-reducer.ts:172`, `tool-publication.ts:96`, `promotion-publication.ts:111`,
   `conversation-bootstrap.ts:87`, `dialog-reducer.ts:131`), plus effect keys
   (`effect-gateway/evidence.ts:52`) and retry/step suffixes (`coordinator.ts:308, 527`). **After R0
   there is exactly one: `OperationKey`**, grammar `<lane>(/<segment>)*`. Derived lanes end in the
   product digest, so a resubmission is the same operation by construction; the session's
   client-minted lane is `session/<sessionId>/<commandId>` — client minting is legitimate, because a
   client must name its operation before it can compute any digest, but it is a *lane*, not a second
   vocabulary. No component may mint a dedupe identity outside it; recovery answers by key everywhere.
   **The per-step-kind prerequisite dissolves rather than defers.** Today the pushed
   `ProposalReduction` steps carry no kind field at all — absence is the perimeter placeholder
   (`packages/domain/src/history/publication.ts:332, 460, 499`) and the real kind rides only on the
   proposal input (`canonical-command-reducer.ts:156`). Post-R0, `kind` and `author` are **required
   fields** of `history.transition-write/1`, and the `history.batch_step` placeholder is deleted — so
   "every write is a kind" is a parse fact, not a promise, and D4's hardest prerequisite is work
   deleted rather than work moved.

   The table is not frozen and needs no registry row (ADR-031): it is frozen the day a published
   package exports it, and not before. Its front matter keeps the honesty sentence in a stronger form —
   the production-boundary register that once backed "every crossing is classified" had named syntactic
   blind spots (final review P2-3) and has now retired, because a source scan cannot see a dynamic
   mount at all; the claim rests on the capability not being injected, and on the attested profile; P2-5 (the `ForkContext`
   surface binding) and P2-7 (retries rate-charged before the idempotency lookup) remain adjacent
   hardening, cited not solved. All of this is **D4's work package**; none of it depends on Cordis.

7. **This repository remains the engine, and the reference host remains its acceptance surface.**
   The engine publishes (W1); the product repo consumes. `apps/web` (Encounter) is no longer the
   product's UI — the Harness client plus our client plugins is — but it remains the engine's
   reference host and the executable evidence for Stages 8/9/11 (thread projection, tenancy e2e,
   Temporal cutover), which signed acceptance still relies on — over R0's rewritten baseline, since
   those stages' artifacts are archived as pre-reset evidence. And D1's user-visible deliverable
   lands **here first**: the Live/Not-live pill — the sixth and most confusing meaning `live` carried
   (`packages/product/src/runtime.ts:766`) — splits into the three display facts it was conflating:
   the **standing badge** with its owed count, the **anchor chip**, and the **binding mode**
   (following/pinned), with `selectSibling` following a named ref instead of pinning
   (`apps/web/src/runtime/session-runtime.tsx:821`, pin/follow branch `:851-853`). Ren raised this
   whole program while testing that pill, and its first renderer does not wait for a repository
   that does not exist; W5's client plugin is the second carrier. Whether Encounter is eventually
   retired into the product's web app or kept permanently as the engine's walking skeleton remains
   an open question (see the OPEN block) — retiring signed-stage evidence is a deliberate act with
   its own drill, never a side effect (the ADR-029 category-6 lesson).

8. **Two axes and a ledger — Realm (binding authority) · Standing (the examination ledger).** The
   previous draft's third axis, *Convergence*, is **struck**: it named no schema, no mechanism, and no
   policy input anywhere in this ADR, and the three archetypes differ on it only through policies that
   already exist (promotion preconditions, standing gates). An axis with no referent is a defect
   against plan §34's closing rule, not a placeholder. If a declared per-ref destination ever earns
   bytes, it arrives then, as ref metadata, with its first consumer.

   **Realm is re-carved as what it always enforced: the binding's world authority.** Verified: the
   only thing `live` gates in the kernel is `authorizeEffect` (`packages/kernel/src/index.ts:366-369`
   and `:958-961`; the third site, `:1140-1141`, merely derives a realm from a ref). Three arms:

   ```text
   anchored        external-grade effects reachable
   world { W }     reversible-grade, inside W only
   detached        no world; effects none
   ```

   Today's `simulation` with an **optional** world (`packages/domain/src/ids.ts:75-79`) splits into its
   two honest cases: world present → `world`, absent → `detached`. A ref holding an exclusive worktree
   is not "simulating"; it is acting reversibly on something real, and the vocabulary now says so.
   **`replay` leaves the axis.** It was never a world-authority level:
   `packages/domain/src/evidence/replay.ts:4` already records that "replay is a mode the process is
   in", and the honest vocabulary already exists — `ReplayMode = verify | evidence-resume |
   re-execute | reconcile` with per-mode `ReplayContactAllowance` (`replay.ts:27-48`). Yet
   `GrantRealmKind` still reads `["live","simulation","replay"]`
   (`packages/domain/src/authority/grants.ts:61`), so today one can *grant authority "for replay"* —
   a category error the HC4.6 work already superseded. Grants become `anchored | world | detached`;
   replay's contact discipline is a mode invariant of the seam, and the zero-provider guarantee is
   unchanged and unscoped. `RealmKey` becomes `anchored | world | world:<id> | detached`, and
   `realmCovers` keeps exactly one covering pair — `world` covers `world:<id>`
   (`packages/domain/src/authority/ids.ts:132-135`, re-spelled).

   **The Ref grammar goes uniform, and the anchor is a class, not a token.** `Ref` becomes
   `<class>/<name>(/<name>)*` with classes `anchor | branch | session | agents | eval | archive`. The
   bare token `live` is deleted from the grammar (`ids.ts:52-55`), where it was the single privileged
   unprefixed name and the seed of six different meanings. `exp/` and `sim/` merge into `branch/`,
   because `refRealmClass` already treats them identically —
   `if (ref.startsWith("exp/") || ref.startsWith("sim/")) return RealmKey.parse("simulation")`
   (`authority/ids.ts:172`) — which is the tell that they were one class with two spellings.
   `session/` is the class decision 4 binds a DSH session to. **Anchoring is a class plus a genesis
   invariant**: exactly one ref under `anchor/` per universe, default `anchor/main`, created by the
   bootstrap's `RefAdmin.create`; `anchored(ref) ⇔ class(ref) = anchor`. This is deliberately the
   middle point between two worse extremes — anchor-ness stays grammar-visible, so the kernel, fences,
   and scanner check a prefix rather than reading policy on a hot path, while the bare-token privilege
   that bred the six meanings disappears, and multi-anchor becomes "relax the one-per-universe
   invariant", a data question rather than a grammar change.

   The binding realm is derived by **one total function** — `bindingRealm(ref, headState)`: `anchor/*`
   → anchored; otherwise `world` when head state holds `workspace/world`, else `detached` — replacing
   every hardcoded conditional (`packages/product/src/canonical-commands.ts:117`,
   `gateway/ref-creation.ts:75, 112`, `product/src/runtime.ts:766, 946`,
   `packages/agents/src/service.ts:1006, 1184`, `packages/product/src/tools.ts:216-223`). The fences
   and the scanner check the class prefix where they checked the token
   (`postgres-store.ts:4656, 4765`; `packages/tools/src/execution-outbox.ts:140, 259-261, 440`) — the
   invariant they enforce, fence equality plus lease margin adjacent to contact, does not move. And
   the UI pill that raised this whole program becomes
   `mode === "follow" && isAnchor(binding.ref)` (`product/src/runtime.ts:766`) beside the standing
   badge — three display facts where one overloaded word used to stand.

   **Realm elision is abolished.** Its entire justification was byte-compatibility: reading absence as
   `live` "changes no byte of any product already published"
   (`packages/domain/src/history/publication.ts:177-182`). Pre-launch that clause has no referent, and
   a token that means both a thing and the absence of its own field is exactly the cognitive load this
   decision exists to remove. Post-R0 every step and product carries its realm **explicitly**;
   `LIVE_REALM`, `declaredRealm`, `isLiveRealm`, and `sameDeclaredRealm` (`publication.ts:183-204`)
   are deleted with the bytes they were protecting.

   `OPEN:` multi-anchor universes — now spelled "relax the one-ref-under-`anchor/` genesis invariant".
   The blast radius is unchanged and enumerated: the kernel gate; `assertDispatchFence` /
   `assertRecoveryFence` including their TypeScript preconditions (`postgres-store.ts:4651, 4754` and
   `:4656, 4765`); the scanner (`execution-outbox.ts:140, 440`); the product's `assertLiveBinding`
   (`packages/product/src/tools.ts:216-223`); and the promotion target. The interface is named, not
   built.

9. **A departure is a transition; detection is its evidence; every departure accrues.** Every
   history-rewriting or purity-losing operation is a coordinator-lane transition — the
   `ProposalReducer` shape of `packages/product/src/gateway/canonical-command-reducer.ts`. Since
   ADR-029 category 10 the coordinator lane is the only lane: `packages/runtime/src/engine.ts` retains
   value types granting no publication capability, the HC6.5 facade and counter are deleted, rollout
   is active-only single-literal (`packages/runtime/src/rollout/bundle.ts:67, 92-97`), and the single
   live path is the `PublicationCoordinator` itself. **Amended 2026-08-22:** the inverted engine that
   used to compose it was retired under ADR-031 — nothing constructed it outside its own tests, and
   the History conformance kit proves its invariants against both drivers directly. With it went the
   ask below to delete the `legacy`/`legacy-engine`/`legacy-kernel` enum members: those classify
   *peer* frameworks in the integration contract (`CanonicalWriteOwnership`, `AuthorityMode`, exercised
   by the `vector-peer-legacy` golden vector), not our own code, and they stay.

   The departure step declares its `kind` — required of every step post-R0, per decision 6 — and
   **stages a `departure/1` evidence envelope** via `ProposalReduction.envelopes`/`evidenceRoots`
   (`packages/runtime/src/publication-coordinator/ports.ts:145-162`; the `rootAttestation` field at
   `:150-156` is the precedent — an envelope staged in `envelopes` whose exact recorded address is
   handed onward), registered in the retention registry
   (`packages/runtime/src/publication-coordinator/coordinator.ts:132-137`, staging `:646`), permanent,
   a GC root like `transition.citations/1` (`packages/domain/src/invocation/citations.ts:150-167`).
   The envelope carries small referents only — target/source node, realm of source, `refused[]`,
   `dropped[]`, world — never a diff (the commit path records the declared proposal input verbatim,
   `packages/store/src/history/postgres/commit.ts:305`, and a diff would embed bytes a tombstone must
   later excise). **What the envelope does not carry, the ledger computes**: a departure accrues an
   examination debt whose footprint is the transition's write set as logical paths, derived from canon
   by diffing parent state against result state — never stored, which is exactly what keeps accrual
   erasure-safe, because a state with erased payloads "can be read, diffed, and verified" but not
   re-materialized (`specs/decisions.md:184-190`). Structural citation is `causes` — secondary
   parents; the store checks only parents[0]=tip, uniqueness, same universe
   (`postgres-store.ts:3132-3144`). Explanation and index are the envelope's job
   (`canon.history_envelope_links` is indexed, migration 032:71-72; reverse lookup by parent is a seq
   scan, `packages/store/src/history/postgres/reader.ts:381-384`).

   The read side is `lint(ref | node) → Finding[]` — pure over canon: the primary walk, envelope
   citations, and the `ops.history_ref_heads` discontinuities left by administrative `advanceRef`
   (`postgres-store.ts:2583-2708`; fence ladder `:2665-2671`, admin CAS `:2681-2690`), which already
   moves refs non-linearly with no journal. Cached in `proj` and added to `rebuildAllProjections`
   (`packages/store/src/projection.ts:33-80`), bound to the caller's `VisibilityScope`
   (`packages/domain/src/history/reader.ts:100-121`), never a `GuardWitness`, never read by the
   coordinator (derived non-sovereignty). Lint has value on day one: it surfaces the departures that
   exist today, and its findings are the head-finding input to decision 10's badge.

10. **Standing is a per-ref examination ledger, not a scalar.** The previous draft's lattice —
    `guaranteed > examined > unexamined` — was a total order over two different subjects.
    `guaranteed` claimed something about a *line* (unbroken mediated custody, reachable only by
    construction); `examined` claimed something about a *node at a scope* (a recorded verification).
    So "never departed, never tested" outranked "departed once, then fully verified", and the middle
    value was launderable: any `runtime.examine{pass}` flipped the enum, because its `scope` was
    decoration unless a policy re-checked it by hand. This repository has already ruled against
    collapsed axes twice in code — the six independent admission axes where "no function derives any
    of them from any other" (`packages/domain/src/context/admission.ts`), and the coverage lattice,
    which is itself a **product** rather than a stored scalar:
    `effective = min(declared, max(observed, enforced))`, commented "min is the law: a claim never
    exceeds its evidence" (`packages/domain/src/integration/coverage.ts:287-303`). The replacement
    separates the two claims.

    **Custody** is a fact: a node whose transition was mediated, effect-bracketed, and recorded under
    a non-downgraded composition breaks no custody. **The ledger** is a per-node value over the
    primary line:

    ```text
    ledger(root)  = ∅
    ledger(N)     = discharge( ledger(basis(N)) ∪ accrue(N), examinations(N) )
    standing(ref) = badge( ledger(head) ∪ headFindings(head) )
    ```

    **Accrual is mechanism, fixed by format, never policy.** A transition accrues one debt —
    `{origin node, footprint, reason, author}` — exactly when it is (a) a departure (decision 9), (b)
    an effect performed while its world is shared (decision 14), or (c) recorded under a downgraded or
    recorded while the mounted composition's attestation observer reports a downgraded regime — and,
    where the profile *declares* the observer, recorded without a record at all. **Absence of the
    attestation family is "no claim", never guilt**: the observer arrives with W3 while the ledger
    lands in D1, so a bare "absent attestation accrues" would retroactively poison every line this
    engine has ever recorded, including the pure-writer archetype whose promised badge is `intact`.
    Scoped this way, arm (c) still guarantees what it exists for — under a declaring profile a
    foreign-profile session can never present a clean line — and decision 5's regime remains a ledger
    *input* rather than a parallel vocabulary. The same scoping governs "custody" above. The footprint is the write set as logical
    paths, computed from canon, never stored.

    **Discharge is selector-set subtraction.** An examination (decision 11) with scope `Selector[]`
    removes the covered parts of matching debts. The Selector grammar stays deliberately narrow —
    exact path, or a final `*`/`**` (`packages/domain/src/path.ts:63-80`) — and is **not** widened
    under R0: scope sets compose from selector *arrays* without grammar growth, while widening the
    grammar itself would widen a grammar that authority scopes share, where a parse ambiguity is an
    authority bug. **Anti-laundering is structural**: a principal's examination cannot discharge debt
    its own transitions accrued — the debt records its author, the examination records its author, and
    the subtraction refuses the pair.

    **The badge is format-fixed, never policy-variable**, so a badge and a shared-claim label mean the
    same thing in every universe and across fleet boundaries — which decision 15's cross-boundary
    sharing quietly depends on:

    ```text
    intact          no debt ever accrued on the primary line
    examined        debts accrued; all discharged
    unexamined(n)   n outstanding — the badge carries the count; the path bar enumerates the paths
    ```

    `guaranteed` is gone: **`intact` is a custody fact no policy can grant**, which also closes the
    old "may policy raise examined → guaranteed" question in the negative — there is nothing to
    restore, because custody is history and history never rewinds. `verified` was reconsidered once
    renaming became free and is still rejected on the merits: it overclaims totality an examination
    does not have, and it would blur the intact/examined distinction anti-laundering depends on.
    Decay needs no rule: later accruals are simply new outstanding items, so a badge moves from
    `examined` back to `unexamined(n)` only because new work arrived, never because old work was
    re-judged.

    **Policy consumes the ledger; it does not define it.** The standing policy is a versioned,
    digested rule value — the Σ model, where `COMPILER_CORE_POLICY_V1` is a value whose identity is
    recomputed from its own bytes and refused on mismatch
    (`packages/compiler/src/core/policy.ts:80-101`, `core/compile.ts:186-189`) — and it decides
    exactly two things: **preconditions** (what badge or debt state gates promotion, external effects,
    sharing) and **discharge authority** (which examiners may discharge which scopes with which
    verdicts). Three binding sites mirror Σ: build default (`DEFAULT_STANDING_POLICY`, equal to
    today's conservative behaviour — adopt-onto-anchor refused, promotion requiring no outstanding
    debt); universe — `policy/standing`, which finally means what it says, replacing the reader-less
    motto the genesis write stores today
    (`packages/product/src/gateway/conversation-bootstrap.ts:106-114`), with D1 adding the dedicated
    policy-set command kind (`CANONICAL_COMMAND_KINDS` is a closed four-member union,
    `canonical-command-reducer.ts:95-100`) and the `policy/**` merge row the static table lacks
    (`packages/runtime/src/merge.ts:157-168` falls to the `**` three-way default); and agent —
    `agents/<id>/psyche/standing`, which has no writer today, so the site is named, not built. Where a
    policy makes standing a **precondition**, the deciding reducer or guard reads the canonical inputs
    itself and records the ledger summary and policy digest it decided under (accountable
    conditioning) — the kernel stays pure and synchronous (`kernel/src/index.ts:881-890`).

    **The admission axis is renamed, so one word means one thing.** `standing` was already taken: the
    frozen candidate axis "which channel it enters — instruction | claim | observation | quarantined"
    (`packages/domain/src/context/admission.ts:19`), glossed in `specs/history-core/terminology.md`
    as cognition placement, and sitting in the very materialization pipeline decision 10 routes
    through — while that module's own docblock insists the axes are independent and
    `terminology.md`'s orthogonality table closes with "No row may be inferred merely from another
    row". Minting a second `standing` there would have manufactured, in a new word, the exact
    multi-meaning defect that `live` had. Under R0 the *frozen* axis renames instead:
    `CandidateStanding` → `CognitionChannel` with field `channel`
    (`packages/domain/src/context/ids.ts:147`, `admission.ts:307`); `standing-floor` →
    `channel-floor` and `standing-not-eligible` → `channel-not-eligible` (`admission.ts:216, 226`);
    `unclassifiedStanding` → `unclassifiedChannel`
    (`packages/runtime/src/candidate-admission/policy.ts:190-193`). This is the more honest name — the
    docblock already says "which channel it enters" — and it frees `standing` to mean what every
    reader of the badge expects, with no third coined term.

    Standing reaches cognition through additive fields on `TransitionAnswer` — `kind?`, `adoptedFrom?`,
    `debts?` (`packages/runtime/src/context-materializer/ports.ts:101-105`, a TypeScript port, not a
    canonical family) — and the source classifier's realm read
    (`packages/runtime/src/candidate-admission/admit.ts:203`) re-spells onto decision 8's arms. The
    ledger and badge are derived, `proj`-cacheable per `(node, policyDigest)`, recomputable from canon
    under any policy version, and never sovereign.

    `OPEN:` state-path blame for adopted values. The footprint gives path-exact *debt*; per-path
    *provenance* of an adopted subtree is separate work, and the precedent for answering it read-side
    is the claim-origin walk that already reports simulation-derived paths
    (`packages/tools/src/index.ts:928-952`).
    `OPEN:` the default discharge-authority table's contents — which examiner classes may discharge
    which scopes. D1 ships the conservative table; the worked universes exercise it.

11. **Examination is a transition that discharges scoped debts.**
    `runtime.examine {scope: Selector[], verdict, evidence}` — record-only, at head, produced by an
    examination actor: a test-runner effect plus reducer, a reviewer agent, or a human. Its effect on
    the ledger is subtraction (decision 10), under two structural rules and one policy rule.
    Structurally, a scope subtracts only from debts it covers, and an examiner cannot discharge debt
    accrued by its own principal's transitions. By policy, the discharge-authority table says which
    examiners may discharge which scopes — a test-runner may be granted `workspace/**` and nothing
    else. A `fail` verdict discharges nothing and is itself a head finding.

    A human examination is an **approval bound to the projection hash of the lint findings** — plan
    Law 16, approvals bind to what was seen; Target §9.1 relocates it into Laws 5/6 plus the approval
    protocol, as a special case of the exact product, over the existing `ApproveAction` machinery.
    What a given verdict *permits* afterward — promotion, external effects — is the policy's
    precondition table, not this record's business. The scope is now load-bearing rather than
    decorative, which is the whole point: a token examination cannot discharge a whole-tree adopt.

12. **One primitive for history rewriting: `state := target tree`, forward.** Three kinds, one
    mechanism — `patchFromTrees(headTree, targetTree)` (`merge.ts:261`, today module-private with one
    caller at `:502`, to be exported):

    - `runtime.adopt {target}` — state := T.state; `causes: [T]`.
    - `runtime.supersede {node, patch?}` — state := apply(patch?, parent(node).state); no cause
      needed, the basis suffices; revert is the empty patch.
    - `runtime.transplant {source}` — state := apply(source.patch, head.state); `causes: [S]`;
      non-applying ops become `contest`/refusal. This is **new behaviour**: today the canonical lane
      refuses the whole proposal with no contest path (`canonical-command-reducer.ts:283-295`,
      resolving at `:186`); the mechanism to build on is the `contest` patch op and `$contested`
      values (`merge.ts:250`).

    Namespace `runtime.*`, never `history.*` — the perimeter's kinds are `history.transition|publish`
    (`packages/product/src/runtime.ts:158-159`); not `replay` (a mode, `evidence/replay.ts:27`); not
    `amend` (Law 5 wording). Preconditions, all recorded: schema/encoding equal (StateId includes
    them, `domain/src/tree.ts:111-113`); the target-producing turn closed with no unresolved intent
    (reuse `advanceRef`'s subquery, `postgres-store.ts:2632-2656`); absent payloads → refuse or
    `dropped[]` (`postgres-store.ts:2027-2049, 1778-1792`); **path policy is honored on the whole-tree
    diff, mode-independent** — every path whose merge policy is `forbidden` (`runtime/**`, row at
    `merge.ts:164`) *or* `manual`/`continuation: never` (agent identity `merge.ts:163`,
    `env/config.json` `:166`) lands in `refused[]`; `simulation/effects/**` is refused
    **unconditionally**, because the existing guard at `merge.ts:425-428` is promotion-mode-gated and
    adopt never enters `DomainMerger.plan`, so the refusal is restated on the adopt path rather than
    inherited; `workspace/world` is refused by name, because a whole-tree adopt that retargets which
    world a live ref's holds address is a Law 5 vector; and `T.state == H.state` is refused up front,
    since the coordinator would answer noop (`publication.ts:921, 959`) or deferred (the deferral the
    retired engine used to answer with). Serial-per-ref and the fence are inherited from `open()`
    (`postgres-store.ts:2385-2393`) and `publish` (`:3522-3623`; unresolved-effect gate `:3559-3571`,
    fenced CAS `:3571-3586`) — **no `refs_guard` change**: `canon.guard_ref_cas`
    (`migrations/004_gc_role.cjs:59-81`) admits exactly `{fence+1}` and `{head≠, position+1, fence=}`,
    never rewind, never delete.

    Every kind is a departure and accrues its footprint (decision 10); the envelope carries the
    referents (decision 9). Under R0 the migration bookkeeping simplifies: the new command types'
    turn-origin allowlist entries land in the rewritten base chain
    (`024_transactional_attribution.cjs:1360-1370` is today's allowlist), and the reserved-number dance
    is deleted with the old chain — the manifest constants
    (`packages/store/src/migration-manifest.ts:13-17`) re-pin once, at R0.

13. **The anchor keeps its clean door and gains labeled ones; the ledger tells them apart; policy
    decides which a universe allows.** ADR-008 stays: promotion is re-execution, effect plans are
    never imported (`merge.ts:425-428`), the candidate is never a parent
    (`packages/tools/src/index.ts:1327-1360`; promotion routes through `#publication.promote` with a
    pre-allocated reconciliation node — the legacy lane is gone). Promotion gains
    `resolution: "theirs"`: conflicts resolved to the candidate wholesale, reported as
    `resolvedTheirs[]` in `PromotionReport` (`merge.ts:72-93`), **accruing one debt whose footprint is
    the theirs-resolved path set** — the report is the evidence, the ledger is the consequence, and
    the approval that authorized it discharges exactly those paths if it covers them. That is more
    honest than the previous draft's blanket "default standing *examined*": if the approval does not
    cover the paths, the debt stays. The conflicts-block-effects gate is unchanged
    (`packages/product/src/runtime.ts:2952-2957`; the `$contested` literal lives in `merge.ts:250`).

    `runtime.adopt` onto the anchor of a `world`- or `detached`-origin target is **allowed under a
    policy that permits it** and accrues its footprint as undischarged debt; the default policy
    refuses it — today's behaviour, preserved. This **re-scopes** `decisions.md:79` ("promotion as
    net-state-diff adoption — imports simulation-derived state *unexamined*"), and the argument is made
    from the recorded harm rather than by re-wording it: what the rejection protected against was
    import that history could not *attribute or answer for* — a net-state diff arrives with no cited
    cause, no realm provenance, no evidence envelope, and nothing downstream can tell it from anchor
    work; "unexamined" named the consequence of that silence. A `runtime.adopt` under this ADR imports
    the same bytes but **cannot be silent**: the target is a cited cause, the departure envelope
    carries the source realm, and the ledger carries a debt naming the exact written paths, which
    every consumer reads — compiler admission through the channel carrier, promotion preconditions,
    external-effect gates — until an examination discharges it. The word that was the rejection's
    consequence becomes the mechanism's recorded output, now with a path-exact footprint the old
    scalar never had. Two settled texts are amended **by name**: plan §16's "live ancestry contains
    only what live execution produced" and `decisions.md:108`'s promotion clause both narrow from
    *ancestry* to **primary line** — the anchor's primary line contains only transitions executed
    under the anchored binding; secondary parents may cite any lineage; each citation is a departure.
    Stated under Alternatives too, so the re-scope is explicit rather than silent.

14. **Worlds — a `world` binding may reversibly act on the world it holds.** A world is a
    **universe-scoped** slice of the external world — a descriptor under a universe-owned root, the
    ADR-018 pattern, so no cross-universe worlds by construction (`WorldId` replaces `SimulationId`,
    today a bare ULID, `packages/domain/src/ids.ts:20`). First kind: git worktree — and in the fleet
    architecture, a runtime's workspace/sandbox *is* a world its refs hold. The world a ref acts in is
    **canonical state** (`workspace/world`), and the binding realm is decision 8's one derivation;
    `world` is minted through the seam at checkout and placed in that turn's binding and action input,
    so replay never reads `ops`. Authority scopes cut the class key `world` to cover every world, or
    `world:<id>` for exactly one.

    **Holds, not leases** (`ops.leases` is the ref fence token; `ops.agent_control_leases` exists):
    `ops.world_holds (universe, world, kind, descriptor, ref, holder, shared, acquired_at, expires_at,
    released_at)`, landing in R0's genesis with §1.2's obligations **as amended by R0** — the
    fresh-chain test, the RLS/tenancy policy, the GC/retention role, and the manifest re-pin; the
    upgrade-test and downgrade obligations have no referent pre-launch and re-arm at the freeze. **The holder
    declares `shared`** — at acquisition or by a later `workspace.share` effect; an exclusive world
    refuses a second hold with a `policy` error naming the holder (Law 15 — the newcomer cannot widen
    the holder's exposure); expiry and renewal, with takeover of an expired hold a distinct recorded
    event; the anchor needs no hold. **Effects performed while a world is shared accrue a debt**
    (decision 10) whose footprint is the effect's canonical write set — Ren's dirty-workspace agents,
    path-exact.

    **Three tiers, one writer each.** Kernel — the gate at `kernel/src/index.ts:366-369, 958-961`
    today refuses **every** `authorizeEffect` outside `realm.kind === "live" && ref === "live"`, so
    this is a **named amendment to plan §16's realm gate**, and under R0 it is rewritten rather than
    relaxed: external-grade effects require `anchored`; `executorClass === "reversible"` under
    `world {W}` requires the hold on W, `grant.realms` covering `world:W`, and
    `scope.effects ≥ reversible` (`effectScopeAllows` applies after) — hold × grant × scope × the
    bracket. This is the explicit answer to Law 6's corollary that a simulation binding must not touch
    the live world without explicit realm promotion: a held world *is* the recorded, reversible-only,
    hold-fenced promotion analog, scoped to one world and never to the anchor. Store —
    `assertWorldHold` as a sibling of `assertCurrentEffectAuthority` on `ExecutorIntentPort`
    (`packages/tools/src/executor-ports.ts:72`), invoked inside `createStoreExecutionGuard`
    (`packages/tools/src/execution.ts:279-303`) so PG and Temporal share it — both callers verified
    (`durable-activity.ts:492` inside `#executeCore`, and `tools/src/index.ts:230`). World is derived
    Store-side from effect → `canon.effect_actions.node_id` → the transition's recorded world. The
    dispatch and recovery fences drop their anchor-only spelling — **the TypeScript precondition and
    the SQL together** (`postgres-store.ts:4656, 4765` in front of the SQL blocks at `:4659-4672,
    4768-4781`) — while the invariant that is actually frozen, fence equality plus lease margin
    adjacent to contact, keeps its exact SQL structure. **The reconciliation scanner is extended** to
    open effect turns with world-scoped reversible intents *and* to `session/*` refs (decision 4):
    `execution-outbox.ts:140, 259-261, 440` are anchor-only today, and the scanner is the only
    *unattended* caller of `beginEffectAbsorption` (`EffectRuntime.absorb`, `tools/src/index.ts:470-486`,
    is the manual second caller), with the outbox source generic over mediated envelopes, so the
    extension carries both envelope shapes. Without it, a worker killed between intent and observation
    strands the branch forever — a real crash-drill gate. Product — agent-work grants already mint
    conditionally (`runtime.ts:841-843`; the unconditional `"none"` mint is `:1416`); workspace grants
    add a `reversible` arm there; child derivation `effectAtMost`
    (`packages/agents/src/service.ts:339-344`, applied `:424`, widening check `:728-732`) then admits
    it. The world lane is `Level2ToolWrapper.execute` (`tools/src/index.ts:705-746`), never
    `ProposeTool`/`ApproveAction`.

    Lifecycle is ordinary reversible effects — `workspace.checkout|share|discard`; compensation stays
    declared-never-executed (`packages/runtime/src/effect-gateway/capability.ts:24-26`); discard is a
    fresh effect. A worktree is a **world — an effect target — not a Store**: nothing here reopens
    ADR-006/ADR-010's Git retirement (`decisions.md:20, 292`). **Merge-back is inside promotion**: the
    branch's terminal step plans `workspace.merge` as external-grade — merging into main *is* external
    — promotion refuses compensation-declaring sources (`product/src/promotion.ts:147-149`), with
    `requiresApproval` (`tools/src/index.ts:163` and the advance gate `:1139`) and
    `publish-or-branch`; the product's promotion driver registry becomes a real closed `Map`
    (`promotion.ts:141-146` is one constant today). Executed world effects are ordinary effects on the
    branch, never `simulation/effects/**` plans — else mislabeled and double-applied. `workspace/**`
    stays a **reference domain — observed, not merged** (plan §9's workspace rule): its merge row
    becomes `domain` with a `WorkspacePolicy` resolving to the anchor's value, and the anchor's
    `workspace/commit` is a witness refreshed by a `workspace.status` world-read. The claim-origin walk
    that flags simulation-derived memory (`tools/src/index.ts:928-952`) re-reads the explicit realm
    carrier and reports "produced in world W". Observability spans carry `world` beside `ref`
    (`tools/src/index.ts:381-394, 432-445`). Closes the `decisions.md:323` OPEN — "`SimulationId`
    semantics" — by replacing the identifier itself.

15. **Sharing across frontier refs carries the ledger, not trust.** Claim assimilation
    (`AssimilationRecord`, `packages/agents/src/domain.ts:40-68`, ADR-016 §4) and the union merge rows
    for `agents/*/memory/claims/**` (`domain.ts:228`) already move knowledge between refs with
    provenance; the record gains one additive field: the origin ref's **badge and outstanding-debt
    summary at the origin node**, computed from the origin's ledger at assimilation time and carried
    as a label on the claim — the generalization of the simulation-origin claim walk
    (`tools/src/index.ts:928-952`). The compiler's source-class lattice reads it through decision 10's
    channel carrier: a claim assimilated from an `unexamined(n)` line is admissible, and admissible
    *as that*. This is Ren's free-frontier universe: many `agents/*` refs, no convergence machinery,
    shared memory that says how much it was examined. In the fleet, the same mechanism is the
    **cross-boundary sharing story**: what moves between runtimes moves as claims with ledger labels,
    never as raw trust — which works only because the badge derivation is format-fixed rather than
    policy-variable (decision 10). The label is a **snapshot**, deliberately: re-deriving the origin's
    *current* standing would make a claim's admissibility mutate at a distance, so a consumer that
    wants freshness re-assimilates.

16. **Refs are archived, never deleted or renamed.** `runtime.archive_ref` is a record-only transition
    at head plus a registered `GuardWitness`, so later advances refuse until un-archived. It is a
    departure kind whose footprint is **empty** — archival rewrites no state — so archiving never
    dirties the badge. Archived refs stay GC roots (Law 19, corrected by Target §9.1 to governed
    availability); collection is retention policy (plan §22–23; `tools/src/retention.ts` adjacent),
    never an operation. Physical deletion stays impossible — the `refs_guard` DELETE arm
    (`004_gc_role.cjs:62-64`) and the foreign keys from `canon.agents`, `canon.agent_spawns`,
    `ops.command_subjects`, `ops.recovered_effect_settlements`.
**Four universes.** The worked examples, one per archetype — the fourth is this ADR's architecture
embodied. All four are rows over one mechanism, which is the sentence the whole program is held to:
three policies, never three special cases.

- **Writer (pure).** Policy row: `runtime.supersede` accrues nothing — rewriting a draft is proposed
  through the coordinator lane and fully attributable, so the `departure/1` envelope still lands
  (detection is evidence, decision 9) and nothing is silent, but nothing is owed. Everything else is
  mediated; anchor `anchor/main`; publishing is an external effect through the anchor. The badge reads
  **intact** on every frontier — and `intact` here means what it says: zero imports, nothing mystical.
- **Working agents, dirty shared workspace.** The first holder declares `shared: true`; every world
  effect while shared accrues that turn's write set. Mid-work the badge reads **unexamined(7)** with
  the owed paths enumerable in the path bar. A test-runner examination actor discharges with
  `scope: [workspace/**, tasks/**]` → **examined**. The promotion precondition is `outstanding = ∅`,
  which a token examination can no longer satisfy. Merge-back rides inside promotion as an approved
  `workspace.merge`.
- **Free frontier.** Each `agents/*` ref carries its own ledger; assimilated claims cross with
  `(badge, owed)` labels; a claim from an unexamined line is admissible *as that*, through the channel
  carrier. No convergence machinery anywhere — and the model no longer has an axis pretending
  otherwise. Irreversible effects go through the one anchor, or through the still-open multi-anchor
  question.
- **A product tenant.** The control plane provisions `policy/standing = DEFAULT_STANDING_POLICY` at
  genesis. Mediated work through our bundle accrues nothing; anything a foreign plugin injects, and
  any transition recorded while the composition attestation is downgraded, accrues its write set;
  policy-accepted examiners discharge; the tenant's own principal cannot discharge its own accruals,
  and no policy however corrupted can mint **intact**, because it is a fact about the line rather than
  a grantable level. Mechanically: a user signs in at the control plane; the runtime manager
  provisions their runtime — one Cordis tree, one `DSH_HOME`, one credential namespace, one universe
  under boundary-scoped DB credentials; our bundle mounts the truth-layer provider and the gateways;
  their sessions are `session/*` refs whose turns are canon nodes, their forks are child refs sharing
  payload blobs, their plugin-injected work is admitted as labeled departures, and the standing badge
  renders in the Harness client through our client plugin — and when their project adds a second
  member, the boundary widens to a project runtime (stage 2) without a byte of history changing
  identity.

**Alternatives considered.**

- **Patch one runtime into multi-user.** Rejected: the required seam is enumerated and large —
  authenticated principal through HTTP/WS, authorized lookups, filtered lists/searches/histories,
  projected event streams, partitioned credentials and workspaces, actor attribution, per-user
  quotas — a capability seam against a moving developer-preview upstream, versus an isolation
  arithmetic that keeps upstream's assumptions valid.
- **Expose the Harness Web profile behind a login page and reverse proxy.** Rejected: the trust
  fence explicitly provides no authentication, the server has no TLS/auth/origin policy by design,
  and `session.list`/events have no per-user projection — a proxy authenticates the socket, not the
  runtime's global state.
- **Fork DSH.** Rejected: pinned published upstream + the `dsh-compat` shim + `stable`/
  `upstream-next` channels; a fork is a permanent second writer on someone else's semantics. An
  `upstream/` submodule exists only while a temporary patch is in flight.
- **Build the product inside this repository.** Rejected: the engine publishes and the product
  consumes — the same discipline for both upstreams; a monorepo product would let the engine's
  internals leak into product coupling exactly where published semver should stand.
- **Cordis under canon.** Rejected — and scoped precisely: Cordis composes *runtimes*; the truth
  layer's packages stay framework-free libraries mounted by bridge plugins; `packages/domain` stays
  zod-only; Postgres enforcement is not composition and does not move.
- **Rebuild DSH's surface ourselves (the previous draft's Encounter-first path).** Superseded by
  this ADR: racing a mature plugin ecosystem's frontend for the single-user experience is the
  low-leverage half; the control plane and truth layer are the halves nobody else has.
- **Force-move or rewind of refs.** Rejected: breaks `refs_guard` and Law 5; a forward departure
  gives the same semantic with a self-explaining record.
- **`history.*` namespace for the adopter kinds.** Rejected: that namespace is the perimeter's.
- **Shipping the diff in the proposal input.** Rejected: erasure — the commit path records declared
  `proposalInput` verbatim, and a diff would embed bytes a tombstone must later excise.
- **Lint as a `GuardWitness`.** Rejected: derived non-sovereignty — a derived reading must never
  gate a commit.
- **A lease check in the kernel.** Rejected: the kernel's contract is pure and synchronous.
- **Newcomer-declared sharing.** Rejected: Law 15 — the newcomer cannot widen the holder's
  exposure; the holder declares.
- **Merge-back as a separate live tool after promotion.** Rejected: loses one report and one
  approval; recorded as the smaller fallback if the in-promotion form proves too heavy.
- **Standing as a stored bit on nodes or refs.** Rejected: sovereign derived data — the fold must be
  recomputable from canon under any policy version.
- **Standing policy as an injected callback.** Rejected: a Σ-style digested rule value plus `domain`
  module rows instead — a callback cannot be recorded, diffed, or replayed.
- **Bare adopt-onto-anchor as the default.** Rejected: the default policy preserves today's refusal —
  `decisions.md:79`'s rejection stands for *unlabeled* import; the label is what changed.

Rejected in the 2026-08-21 freeze-directive revision:

- **The `guaranteed > examined > unexamined` scalar.** Rejected: a total order over two different
  subjects — `guaranteed` claims a property of a *line*, `examined` a property of a *node at a scope*
  — so it ranks "never departed, never tested" above "departed once, then fully verified", and its
  middle value is launderable by any passing verdict. Replaced by the ledger (decision 10).
- **A bare (custody, verification) pair.** Right diagnosis, insufficient state: an unscoped
  verification coordinate re-opens the laundering hole, and "checked ⊇ departure write set" is not
  computable from the pair. The pair survives as the badge's corners, not as the stored value.
- **A policy-raisable top value.** Rejected: `intact` is a fact about a line, not a grade a policy may
  grant. Custody is history, and history never rewinds — there is nothing to restore.
- **A policy-variable badge derivation.** Rejected: it would break the fleet-wide label legibility
  decision 15's cross-boundary sharing depends on. Policy varies accrual and discharge, never the
  summary.
- **`verified` as the top badge word.** Rejected on the merits even once renaming became free: it
  overclaims a totality an examination does not have, and blurs the intact/examined distinction
  anti-laundering rests on. (It also collides with the derived `ProvenanceStrength`,
  `packages/domain/src/context/admission.ts:129`.)
- **Coining a third word ("assurance") to dodge the `standing` collision.** Rejected once the freeze
  lifted: a system should not carry three words for two concepts. The frozen admission axis renames to
  `channel` — which its own docblock already calls it — and `standing` means what a badge reader
  expects.
- **Value-level lineage as canonical data.** Rejected: propagation through cognition is unbounded and
  epistemically false, and conditioning evidence already records the influence. Per-path blame stays a
  `lint`/`explain` read, on the precedent of the existing claim-origin walk
  (`packages/tools/src/index.ts:928-952`).
- **Keeping `convergence` as an axis.** Rejected: no referent — no schema, no mechanism, no policy
  input. An expectation is a lint rule class, not an axis.
- **Widening the Selector grammar for discharge scopes.** Rejected: selector *arrays* compose sets
  without grammar growth, and the grammar is shared with authority scopes, where a parse ambiguity is
  an authority bug (`packages/domain/src/path.ts:63-80`).
- **Renaming the canonical `live` token in place, or minting an `anchor` namespace beside it.**
  Rejected in favour of the uniform class-prefixed grammar: the bare-token privilege *was* the defect,
  and anchor-as-class keeps the hot-path check a prefix test rather than a policy read.
- **One publication per DSH append batch** (what the W0 skeleton did). Rejected: the effect bracket
  holds a canon turn open across a whole tool execution, so a long tool would stall every log append
  on that ref. Replaced by the two-plane staging-and-fold encoding (decision 4), which is canon's own
  HC4.7 pattern.
- **A departure event inside the session log, riding `ignorable: true`.** Rejected on four grounds: it
  would claim a position inside the very sequence the departure rewrote; `ignorable` licenses a reader
  to *skip* a record whose loss cannot affect reconstruction, which a departure marker violates; DSH
  validates seed contiguity and would refuse a log implying a gap; and there is no live consumer,
  since DSH never reloads a live session. Departures surface as revision changes, recorded
  carrier-local with their reason under decision 6's parity law.
- **A single `ignorable` erasure placeholder for every event.** Rejected: it breaks surface folding
  whenever a later `replace` cites the erased seq, and it lies about affecting reconstruction. Two
  forms, split by surface eligibility (decision 4).
- **`forbidden` as the `sessions/**` merge policy.** Rejected: it would refuse even one-sided copies,
  making any merge between two session-bound working refs impossible — which is the dirty-workspace
  archetype. `domain` with rejection on true conflict instead.
- **Retiring the freeze registry outright.** Rejected here, then **reversed by ADR-031 on 2026-08-22
  and recorded as such.** The rejection said the register is not the constraint but the record of one.
  The reversal's answer: a record we author and grade ourselves is not evidence, and the day a user
  exists is exactly the day `exports` plus semver starts recording the same thing under enforcement we
  do not administer. So the register retires and publication carries the claim. The clause below that
  reads "regenerate the freeze registry, which re-arms on the reset" is retired with it.

**Consequences.** The engine repo's job sharpens: publish, conform, guarantee. The largest consequence
is **R0**, and it exists because Ren lifted the freeze for representational constraints on 2026-08-21:
pre-launch, with zero external users, a compatibility ladder protects nobody and buys permanent
structural debt, so the ladder is collapsed once rather than carried forever. What R0 breaks is
strictly representational — names, enums, grammars, wire versions, migration numbering, schema
families, elision rules. What it does not touch, and never conflicted with the new design, is the
correctness core: append-only canon and `refs_guard`'s two admissible mutations, OCC and the prefix
witness, per-lease fencing, the effect intent/observation bracket and the unresolved-intent
publication gate, the availability ledger and erasure semantics, RLS and tenancy, replay's
zero-provider guarantee, Postgres/Temporal equivalence, and one-active-writer-per-semantic. Those are
the product, not legacy requirements. **The additive-families rule is not deleted** — only its
application to dev-era bytes is; the freeze re-arms on the reset and becomes real the day a user
exists.

Five of the six `frozen-legacy-read-only` contracts die with the bytes they served; the sixth,
`authorization-decision-v1-formats`, has a **live writer and live readers** — the kernel constructs
`authority.static/v1` and `authority.attested/v1` today (`packages/kernel/src/index.ts:192-208,
800-812`) and the agents service reads the latter on a live path
(`packages/agents/src/service.ts:311, 1201, 1406`), so the registry's "nothing writes them" rationale
is stale — and it retires by supersession under decision 8's realm re-carve, writer and readers in
one change, never by reader deletion. The pre-reset
acceptance artifacts are archived as evidence of a superseded baseline with a recorded supersession
note — a deliberate retirement, never a side effect. Publishing flips `private: true` on the
plugin-facing subset with semver bound to family versions; the conformance kits publish beside them,
now including the **vendored** DSH persistence contract, and the cross-package test-tree debt retires.
A new product repository is scaffolded per decision 2. The runtime manager provisions per-boundary DB
roles over the existing RLS/definer machinery — defense in depth as a deployment property. The
embedded dialect is re-prioritized: the *product* mounts the Postgres provider from day one, so
PGlite/`node:sqlite` serves the pure-ecosystem audience and lands after W2 — and §34's
embedded-dialect deferral **has not fired**: its trigger is an embedded-only *host* demanding the
dialect, an audience is not a host, and DSH's embedded need is met by its own SQLite backend. No
second dialect may carry canon until it passes the Postgres semantic-equivalence and tenancy suites.
Encounter re-aims as the engine's reference host and D1's first badge carrier; the product UI is the
Harness client plus our client plugins.

Two new families enter: `departure` and `composition.attestation`. They enter by being written —
ADR-031 retired the schema-ownership ledger and the freeze registry, and neither family is frozen
because nothing is published yet. `specs/decisions.md` gains, on acceptance: the everything-is-a-plugin
adoption with its hard lines; the fleet/control-plane architecture; the truth-layer thesis with its
two-plane encoding; the R0 reset and its scope; the ADR-011 supersession; the plan §16 /
`decisions.md:79` / `decisions.md:108` re-scopes; and the ADR-014/015 re-aims. `terminology.md` gains
Anchor, Channel, Examination Ledger, Debt/Footprint, Examination, Departure, and Binding realm, and
its Standing entry is replaced. **CLAUDE.md rule 1 changes on acceptance**, because it currently says
the opposite of the directive: *frozen* means the correctness core plus whatever the re-armed registry
covers after R0; representational constraints are rewritable pre-launch, and policy refusals may be
relaxed by an ADR when the relaxation is a recorded departure read by a declared standing policy. Its
docs pointer refreshes to this ADR's current title.
**Work packages.** Ordered so nothing publishes before it is proven and nothing multi-user ships
before the truth layer holds it. Each gate is narrow. **R0 precedes everything**, because every other
package writes against the vocabulary it settles.

- **R0 — the v1 reset (the directive's package).** One clean re-baseline, executed once, pre-launch.
  **Migrations:** migrations `001..037`, both runner shims
  (`packages/store/src/migration-013-compatibility.ts`, `migration-030-compatibility.ts`), and the
  `targetOrdinal` seam are deleted; **one genesis migration** is authored carrying every enforcement
  the chain accreted — schemas, tables, triggers (`canon.guard_ref_cas`, `guard_insert_only`,
  `effect_observation_requires_intent`), definer functions, RLS policies, grants, and the guarded role
  bootstrap — with plain `CREATE INDEX`, because the concurrency ceremony served live upgrades that
  cannot exist on an empty base. A rewritten *chain* was the earlier hedge: there is no seam that
  needs a second file, since `CREATE ROLE` is transactional and the mid-chain special-casing existed
  only for migrations 013 and 030 (`migrate.ts:180-217`). `frozen-migrations.json` and the manifest
  constants (`packages/store/src/migration-manifest.ts:13-17`) re-pin to the one entry, gaps `[]`.
  **The genesis stays soft** — re-editable, with a trust-root re-pin per edit, so every change is a
  reviewed source change — until the first consumer Ren does not control exists (the earlier of a
  genuinely external adopter of the W1 packages, or W4's first provisioned tenant); at that moment the
  additive rule and §1.2's full obligations re-arm verbatim. Until then W2/D2/D3 schema lands *in* the
  genesis, which retires decision 12's reserved-number dance and dissolves the R0-precedes-D2
  allowlist tension in one move. **The safety invariant, stated as a check:** *no database outlives
  its genesis* — `migrate.ts` refuses any database whose `ops.migrations` ledger is not an exact
  prefix of the current manifest (the shims' `assertLedgerPrefix`,
  `migration-030-compatibility.ts:27-33`, promoted to a first-class guard as the shims die); an
  old-genesis database is dropped and recreated, never upgraded in place. §1.2 is amended **by name**:
  pre-launch the per-migration obligations are the fresh-chain test (every suite's `resetDatabase()`
  is one), the RLS/tenancy policy, the GC/retention role, and the manifest re-pin; "released-baseline
  upgrade test" and "downgrade/rollback statement" have no referent before a released baseline exists
  — `migration-upgrade.test.ts:11-16` says so itself, asserting that "a real installation in the field
  sits at ordinal 10" when none does — and both re-arm at the freeze. The sixteen
  `migration-*.test.ts` upgrade drills retire with the chain (`migration-manifest.test.ts` survives,
  retooled); the end-state invariants stay proven where they always were — behaviourally, in the
  store/history/authority suites, which test the migrated end state and do not care how many files
  produced it.

  **Vocabulary:** land the grammar and enum re-carves (decision 8) — **including the kernel gate
  re-spelled once to anchored-only** (`packages/kernel/src/index.ts:366-369, 958-961` is the same
  check spelled twice; fold the duplication while touching it, since D3 already promises "written
  once"), without which R0 would ship an enum the kernel does not speak; the `standing` → `channel`
  rename (decision 10); the one-`OperationKey` collapse and required step `kind`/`author`
  (decision 6); realm elision deleted with its helpers (`publication.ts:183-204`).

  > **Landed 2026-08-21 (parts 3a–3c).** Three things the plan did not anticipate, recorded because
  > each was a consequence rather than a choice:
  >
  > 1. **Deleting the realm elision forced the transition-write family to collapse.** "Absent is
  >    `live`" has no meaning once `live` is not a realm, and the v1/v2 pair existed *only* to keep
  >    already-published bytes stable — bytes R0 deletes. So the two families became one, with `step`
  >    and `realm` always present. The realm is a **required material**, not a defaulted one: the
  >    same default under the re-carve would have handed `anchored` — the realm that gates external
  >    effects — to a product that never named one. That is the one place the collapse had to fail
  >    closed rather than stay convenient.
  > 2. **The grammar was written twice.** `BranchNamespace`
  >    (`packages/domain/src/products/publication.ts:95`) carried its own copy of the namespace list,
  >    which is how `exp` and `sim` survived in it after `Ref` dropped them. A grammar written twice
  >    is a grammar with two answers; it now derives from the one class list.
  > 3. **Two words outlived the realm they were named after.** The compiler's authority rank and the
  >    admission source class both spelled their lowest value `simulation`, both *derived from the
  >    realm check* — so after the re-carve the label would have named a realm that no longer exists.
  >    Both are now `unanchored`, which is what they always meant: the claim arose off the anchor.
  >
  > `replay` left the axis with nothing to preserve: `resolveExecutionBinding`'s `replay?: boolean`
  > had **no caller anywhere in the tree**, so the arm was vestigial and its removal took no
  > protection with it. Replay's contact discipline was already a mode invariant of the seam.

  Renumber every
  family to `/1` — **with one carve-out**: `authority.static/v1` and `authority.attested/v1` are not
  dead readers. The kernel *writes* them today (`packages/kernel/src/index.ts:192-208, 800-812`) and
  the agents service *reads* them on a live path (`packages/agents/src/service.ts:311, 1201, 1406`);
  the freeze registry's "nothing writes them" rationale is stale. That pair retires **by supersession
  under decision 8's realm re-carve** — writer and readers changing together — never by reader
  deletion. The other five `frozen-legacy-read-only` contracts and their readers delete outright, plus
  the shadow, dual-path, and rollback surfaces the register never listed: `ingress-attestation`; the
  legacy continuation chain (domain envelope, store reader, runtime resolver); the compiler's legacy
  ordering, renderer, and selection half; `rollout/bundle.ts` and `rollbackToLegacy`/`drainToLegacy`;
  `dual-path.ts`; the retention v1 arms; the pre-Phase-7 read-both agent paths; the
  `authority-port/v2` family (v3 stays — it is the frozen protocol's remote-holder evidence); and the
  never-produced mediation/coverage enum members. Verified live despite legacy styling, and therefore
  **kept**: `packages/compiler/src/artifact-sink.ts` (constructed on the live chat path,
  `chat-turn.ts:708`), the `rollout/actors.ts` direct-path tripwire, the drain *barrier*, and the
  `legacy-hash` availability input.

  > **Legacy deletion — landed 2026-08-21, with two consequences and one stop.**
  >
  > Deleted: `ingress-attestation` (no consumer but a comment); the legacy
  > continuation chain (domain envelope, store reader, runtime resolver) and with
  > it `ResolutionMaterials`, which had one arm left and therefore carried no
  > information; the compiled-context renderer; and the rollout switchboard —
  > `bundle.ts`, `rollbackToLegacy`, `drainToLegacy`, and the `rollout` config
  > option — whose every component enum had exactly one legal member, so it could
  > only ever say "active". The drain *barrier* survives, without the rollback
  > verdict: what it rolled back to is gone.
  >
  > **One family lost its freeze, and the register says so.**
  > `continuation-resolution` was frozen on the rule of two, and its *second*
  > consumer was `packages/store/src/continuation/legacy-reader.ts` — the
  > migration-era reader this work deletes. That drops the family to one
  > producer. Rather than keep a dead reader alive to satisfy a count, the
  > candidate is marked `experimental`. It re-freezes when a second real producer
  > arrives; the D-series adapters are the expected one. The register refusing to
  > certify a freeze it can no longer back is the register working — but it *is*
  > a change to the accepted frozen surface, which is why it is stated here.
  >
  > Two `frozen-legacy-read-only` candidates go with the readers they described:
  > `compilation-record/v1..v5` and `compiled-context/v1`. Both named the deleted
  > legacy reader as their only consumer, and `compiled-context/v1`'s rationale —
  > "can never be deleted while a legacy frame is reachable" — stops holding when
  > no frame is reachable at all. The registry ends at 15 contracts: 8 `freeze`,
  > 4 `frozen-legacy-read-only`, 2 `experimental`, 1 `private-versioned`.
  >
  > **What was *not* affected, corrected after checking:** no render family lost a
  > freeze. `context-materialization-vocabulary` stays frozen — its two consumers
  > are the materializer and the compiler core, both live — and `context-ir` was
  > already `private-versioned` with the note "there is no second renderer", so
  > the legacy renderer never counted toward its rule of two either. What the
  > deletion did cost the render side is *untracked*: `renderer.test.ts`'s
  > cross-renderer comparison was the only place two independent renderers were
  > run over one record and compared, and the registry never cited it. That
  > evidence is gone until a second renderer exists, and no gate will say so.
  >
  > **Stopped, needing Ren:** the compiler's legacy *ordering* half.
  > `legacyUtf16Ordering` and the `pipeline.ts` selection stages it drives have
  > one consumer — `bench/mind-01.ts`, the chartered-but-dormant mind-layer eval
  > whose measured numbers are recorded in `specs/acceptance/mind-01.md`
  > (measured 2026-08-09, sign-off pending). Deleting them either breaks that
  > harness or silently invalidates its numbers, and the core compiler's
  > `codePointOrdering` breaks ties differently, so a port re-measures rather
  > than preserves. Three options, none of them mine to pick: port the harness to
  > the core compiler and re-measure; retire `mind-01` with the ordering; or keep
  > the comparator as the mind eval's own, renamed off "legacy". Everything else
  > on this list landed.

  **Gates and artifacts:** the phase-runner apparatus retires **whole** — runners, configs, artifact
  verifiers, `acceptance-core`, the frozen workspace-reporter trio, `census`, `retirement-drain`,
  `agent-state-ownership`, `adk-probe` (its JSON verdict stays as archived evidence),
  `phase-0-database`, and `stage-11-acceptance`. Not because it is merely unearned, but because R0
  **falsifies what it asserts**: `phase-9-artifact.ts:639-655` requires the migration inventory to end
  at 037, `:584` pins the frozen-legacy-reader count at exactly 6, `derivePhase9Statics` hard-codes
  `currentExceptions: 50`, and every phase artifact binds the exact pre-R0 tree through a chained
  ancestry — so the apparatus goes permanently red the day R0 lands, and a permanently red verifier
  guarding an archived baseline trains its only operator to ignore red. The drills those gates pointed
  at were always *in the suites* — no phase gate performs a crash drill itself; it pins vitest titles
  — and the suites keep running under `pnpm test`. The pieces that *execute* something no suite
  executes stay standalone (`egress-sandbox`, `process-group-supervisor`, `bench/stage-1.ts`'s WAL
  drill, `bench/stage-7-restore.ts`, `w0-probe`, `vector-coherence`). **The generators do not stay.**
  This clause originally retained six of them behind a relaxed `--write` cadence; ADR-031 retired every
  one, because relaxing the cadence treats the cost as the problem when the problem is that a scan of
  a closed tree stops meaning anything under plugin composition. The live consumer named here for
  `schema-inventory` illustrates it: `history-postgres.test.ts` was reading `schema-ownership.json`
  for relation ownership the corpus had attributed to migrations R0 itself deleted, and the suite
  passed anyway. It now walks the SQL live. Tag the pre-reset tree `pre-r0-baseline`; delete
  `bench/results/history-core/` (21MB) from the working tree; stamp
  `specs/acceptance/history-core/*.md` superseded — the human sign-off record stays — and record all of
  it in `specs/history-core/supersession.md`: the deliberate retirement drill, never a side effect.
  Regenerate `specs/vectors/*`; **delete** `census.json`, `retirement-drain.json`,
  `agent-state-ownership.json`, and `shadow-final-evidence.json`.

  **Byte pins are disarmed, and the finding that forced it (2026-08-21).** R0's vocabulary section
  originally said "regenerate every `specs/vectors/*` file", and the machinery to do that does not
  exist — the twelve vector files publish 1,300 digests and 116 canonical payloads with no generator,
  because under append-only-forever a golden vector is never regenerated, only added to. Lifting the
  freeze inverted that, and Ren's call followed: *pre-launch, with no stored data, no external
  consumer, and a data model still moving, byte pins buy nothing and cost a regeneration pass per
  iteration.* So the pins are **disarmed** behind a single documented flag (`BYTE_PINS_ARMED`, in each
  package's fixture module), re-armed at the same moment the soft genesis stops being editable — the
  first consumer Ren does not control. **One rule, three mechanisms:** the genesis, the additive
  families, and the byte pins all re-arm together.

  Disarming is safe rather than a hole, and the reason is specific: what actually guards the canonical
  encoding is `packages/domain/test/cjson.test.ts`, which pins the JCS output byte for byte
  (`{"A":3,"z":2,"！"​:1}` — the UTF-16 code-unit sort), determinism under key-insertion order, the
  single trailing LF, and the decode round-trip, under property testing. The primitive is covered. What
  is disarmed is only "these *particular records* hash to these *particular values*", and every
  assertion comparing two *computed* values still runs — refusal cases, admitted/refused verdicts, and
  each identity-sensitivity axis.

  **But disarming the assertions was not sufficient, and this is the part worth remembering:** the
  vectors embed derived values as *data*, not only as assertions. A compiler input's
  `value.materialization` **is** a MaterializationId, and each of its bindings carries the digest of
  that candidate's admission record, both schema-validated. So a canonical rename leaves the fixture
  internally incoherent even with every pin switched off — and it surfaces *behaviourally*
  (`refused` where the vector says `admitted`), not as a digest mismatch, which is exactly the shape a
  digest-only review would pass over. The answer is a **coherence pass**, not a generator:
  `bench/scripts/history-core/vector-coherence.ts` recomputes only the embedded cross-references —
  materialization ids and per-candidate admission digests — and is run after any change to a canonical
  context format. The remaining embedded digest-shaped fields (`policy.digest`, `resolution`, `frame`,
  `binding`) are literal test constants and do not move.

  With that in place the vocabulary work is unblocked: `standing` → `channel` landed under it, and the
  realm re-carve and Ref grammar follow the same path — rename, run the coherence pass, run the suite.
  `OPEN:` the vector generator proper is still owed at re-arm time, when the corpus is regenerated
  against the settled shape. Building it *then* is one pass against a stable model rather than a
  rebuild per iteration, which is why it is deferred rather than merely postponed.

  **Gate:** genesis migrate from empty · both-driver history/authority/attempt-ledger conformance kits
  green on the renumbered families · `liveThenReplay` byte-identical · `proj` drop-and-rebuild · the
  tenancy and in-process-attacker drills unchanged · required-field parses refuse an elided realm or
  an absent step kind · the **token gate**, identifier-precise (`LIVE_REALM`, `declaredRealm`,
  `isLiveRealm`, `sameDeclaredRealm`, `CandidateStanding`, `SimulationId`, `history.batch_step`, and
  the bare-`live` Ref/realm parse — never a bare `"live"` string grep, since the English word is
  everywhere) with a named exclusion set (`specs/acceptance/**`, `specs/reviews/**`,
  `supersession.md`, git history). A ~60-line script, not an apparatus. **R0 publishes no artifact**:
  the gate goes green, Ren signs the supersession note, and that is the record.
- **W0 — the Cordis/DSH probe (allowed to say no).** **Done, 2026-08-21: GO.** Pins resolved to the
  published artifacts; the compat budget measured; four gates PASS and the provider skeleton DEFER to
  W2. See `specs/acceptance/history-core/w0.md` and the addendum below.
- **W1 — Publish + the conformance kit.** The published-set decision — read from each package's
  `exports` map and the closure walker, since ADR-031 deleted the dependency inventory (execution
  record);
  `private: true` flipped with semver bound to family versions; the kit (actor attacks,
  execution-driver, history/authority, and the **vendored** persistence contract — DSH ships it only
  in `tests/`) published as a testkit; an out-of-tree fixture package building against only published
  artifacts passes it.
- **W2 — The truth-layer provider, whole.** Recorded decisions first: (1) the two-plane encoding —
  `ops.session_log_staging` plus the per-DSH-turn fold, chunk rows reused verbatim, the
  envelope/payload split; (2) the incremental `materializeState`, or its measured whole-tree ceiling
  as the recorded fallback; (3) universes-per-boundary granularity; (4) the session ref's creation
  base; (5) where the provider lives — `packages/dsh-host`, the engine's published plugin package
  (execution record). Then the work: the migration adding `ops.session_log_staging`, the `session/` ref class, the
  `sessions/**` merge row and reserved root, and the turn-origin allowlist entries for
  `session.append|repair|fork`; the backend under `PersistenceCoordinator`; the halt plugin and the
  session-canon-binding service; the scanner extension to `session/*` refs; the two-form erasure
  representation; the session-format upgrader; boundary-class role pools per decision 3. **Gate:**
  vendored `runPersistenceContract` green over Postgres canon, complete · projection round-trip
  `project(fold(events)) ≡ events` exactly, including packed runs split across batch and fold
  boundaries, with the window-partition invariant refusing a corrupted or foreign-adopted subtree as
  corruption rather than silently repairing · `kill -9` between staging and fold, and mid-tool with a
  durable intent: the scanner resolves on a `session/*` ref, `session.repair` folds closers marked
  `origin:"repair"`, **no observation row exists that the executor-class machinery did not produce**,
  and re-append continues at the balanced seq · graceful dispose mid-turn with a running tool: dispose
  bounded, next load balanced **without** synthetic closers, ref released by the scanner ·
  config-update restart mid-stream: adoption appends the missed suffix and the projection is
  byte-identical to an unrestarted control · halt: an administrative advance mid-session halts the loop
  within one flush checkpoint, post-fence folds are refused, `prepare()` serves the new head ·
  single-writer: two processes on one session id, one fold wins per window, the loser halts · erasure:
  a plain event, a packed run, and a surface event erased — the log still loads, surface placeholders
  keep type and surface structure and satisfy a later `replace` citing the seq, log-only placeholders
  are `ignorable`, a fork sharing the blobs shows the same placeholders, ledger evidence cited ·
  `liveThenReplay` byte-identical through the bridge composition with exact tape consumption ·
  **measured targets** for staged-append p95 and per-turn fold p95 at realistic chunk volume and a
  100k-event session, numbers named at gate time (the principal-mode pool is `max: 1` today) · the
  **in-process attacker** tenancy drill.
- **W3 — Mediated contact as host plugins.** The model-gateway plugin at the tree's provider seam; the
  effect bracket on the tool waterfall, taking its turn from the session-canon-binding service
  (decision 5); approvals; the attested-profile checker that makes decision 5's regime distinction
  durable. Gate: the negative fixtures — a tree with a foreign provider plugin yields the degraded
  contract row, never a false strong claim.
- **W4 — The product repository, stage 1 (multi-account MVP).** Scaffold per decision 2; control plane
  (login, orgs, membership, audit) reusing the Stage 9 identity machinery; the runtime manager
  (provision/start/stop/update, per-boundary credentials); the authenticated router (HTTP/WS). One
  runtime per user; our bundle mounted; `stable`/`upstream-next` channels running.
- **W5 — The client plugins.** Standing badge with its owed count, DAG/branch navigation, approvals,
  `explain`/`lint` surfaces as Harness UI extensions — the vocabulary's human carrier inside their
  client.
- **W6 — Stage 2: shared projects.** One runtime per project; attribution and collaboration rules;
  cross-boundary sharing as ledger-labeled claims (decision 15). RBAC (stage 3) only if projects
  demand admin/member/viewer.
- **U1 — Upstream clock service (non-gating).** A Cordis `clock` service consumed at DSH's three
  wall-clock session-core sites and in the loop, contributed upstream on its own merits (their
  chunk-row tests already fight wall-clock). Nothing in this ADR gates on it; it narrows decision 5's
  named residue without changing the pitch.
- **D1 — Detection and standing.** The `departure` family (no ownership row, no freeze decision —
  ADR-031); `lint`; the **ledger** — the fold, the selector-set algebra with absorption, the
  `proj` cache keyed `(node, policyDigest)`, registration in `rebuildAllProjections`, and the
  `VisibilityScope` binding; `DEFAULT_STANDING_POLICY` and the three binding sites, including the
  dedicated policy-set command kind and the `policy/**` merge row the current tree lacks; the
  admission additive fields and the `channel` rename's consumers; the badge data the client plugin
  renders, and its first carrier in Encounter. Zero new permissions. **Gate:** the ledger and badge
  reproduce from canon after a `proj` drop · the **anti-laundering drill** — a principal's examination
  refuses to discharge its own accrual · the **discharge-scope drill** — an examination discharges
  exactly its selector cover and no more · `VisibilityScope` leaks nothing · today's `advanceRef`
  moves appear as findings.
- **D2 — Departures.** `runtime.adopt|supersede|transplant|examine|archive_ref` (export
  `patchFromTrees`; build the transplant contest path — today's lane refuses whole-proposal only);
  promotion `resolution: "theirs"`; the command types and their allowlist rows in R0's chain. **Gate:**
  every departure has its envelope · **every departure's debt footprint equals the canon diff of its
  transition, asserted exactly** · adopt refuses on an open or effectful producing turn · replay
  identical. (The production-boundary register's `--check` was this gate's last clause; ADR-031
  retired the register, and what it claimed — no unmediated crossing — is structural under plugin
  composition: an actor not injected a capability cannot reach it.)
- **D3 — Worlds.** The holds table; the kernel branch written once in the new arithmetic rather than
  relaxed twice; `assertWorldHold` plus the fences (the TypeScript precondition and the SQL together)
  and the scanner (both envelope shapes); the product grants (a `reversible` arm in the existing
  conditional mint) and the tool lane; the `workspace.*` effects and driver registry; the
  `workspace/**` merge row. **Gate:** reversible + world + hold ok; no hold refused; no world refused;
  external under a world binding refused · a shared-world effect accrues · a crash drill — `kill -9`
  between intent and observation on a `branch/` ref reconciles through the extended scanner · PG and
  Temporal run the same guard, mediated and non-mediated activity paths both covered.
- **D4 — The operation surface (no Cordis dependency).** The operation table per decision 6, authored
  as **TypeScript the carriers import** — not a JSON artifact on a `--write`/`--check` pattern, which
  ADR-031 retired: a table the carriers compile against is enforced by `tsc`, while a table a checker
  compares against is a corpus that passes by construction. The parity checker, the per-wire
  conformance fixtures and the docs derive from it — carriers conform to the table rather than a
  checker walking carriers; reads-as-a-capability (`explain`, `lint`, the one scope constant); receipt
  `evidence[]`; the `contextPolicy` overlay and compiler identity bump. **Gate:** the parity check
  fails on an unlisted verb · every table row names its carriers or records why one is deliberately absent (the
  session log's departure absence is the first such row) · an `OperationKey` outside the lane grammar
  is refused at mint · an external read cannot reach reducer-grade state.
**OPEN.**

- `OPEN:` **vendored versus published-pin for Cordis** — decided by W0 with the DSH precedent
  (vendor at rc, own the framework layer) priced against our maintenance budget. **W0 result
  (2026-08-21): recommend the published pin** (`@deepseek-ai/cordis@4.0.1`; the manifest's
  `4.0.0-rc.7` is stale documentation, the published artifact is `4.0.1` and the DSH umbrella pins
  `^4.0.1`). The compat budget is measured small — the `SessionPersistence` seam is byte-stable
  across four releases, the session-event contract moved 7 additive lines once — so vendoring's
  audit/patch control is not yet worth the DSH precedent's 18-modification maintenance cost. Ren's
  call stands; see `specs/acceptance/history-core/w0.md`.
- ~~`OPEN:` **universe granularity per boundary**~~ — decided in W2 (recorded decision 3,
  `specs/acceptance/history-core/w2.md`): one universe per security boundary, argued from RLS being
  universe-scoped, blobs being universe-partitioned (fork dedupe → erasure reach) and the
  one-anchor-per-universe genesis invariant; a project surface is a ref, not a universe.
- ~~`OPEN:` **the session ref's creation base**~~ — decided in W2 (recorded decision 4): fork from
  the anchor head by default (`bindingRealm`, mergeability); `pure-log` stays a policy value on the
  composition config, read off a policy row by the product.
- `OPEN:` **Encounter's end state** — permanent reference host and acceptance surface, or eventual
  retirement into the product web app; retiring signed-stage evidence is its own deliberate drill
  (the ADR-029 category-6 lesson), never a side effect.
- `OPEN:` **event-stream projection and redaction at the router** — DSH forwards events with no
  per-user projection. *W6 (product `docs/acceptance/w6.md`, decision 5): moot for stage 2 — one
  project is one runtime and its members are mutually trusted by decision 3's arithmetic, so no
  per-member redaction exists to do; live only for a non-mutually-trusted runtime, which is stage 3's
  `viewer`, deliberately not built.* **Sharpened by W6's finding:** per-member attribution cannot reach
  canon through one runtime today, because no DSH seam hands a host plugin the acting principal —
  `ConnectionRpcHandler` is `(endpoint, payload, signal)` (`@deepseek-ai/dsh-client-connection`
  `lib/types/rpc.d.ts:11`; the `Request` with the injected headers never crosses). Authorization is
  per member and in canon; attribution is at project granularity with a per-member correlation trail
  at the router; a product gate goes red the day upstream widens the handler.
- ~~`OPEN:` **billing/quota enforcement point**~~ — decided in W6 (recorded decision 6): the router
  refuses request quota per boundary with `capacity`, charged after authorization; the kernel budget
  ledger is the only place that sees model spend; never the gateway plugin.
- `OPEN:` **the upstream channel policy** — how long `upstream-next` soaks, and what test surface
  promotes it (the compat shim's suite, at minimum). *W4 built the two channel directories and
  gated promotion on session-format-version equality; the soak length is still unset.*
- `OPEN:` **upstream's loopback-privileged methods on a shared runtime** (W6). Fifteen methods
  (`credentials.set`, `settings.replace`, `host.pickDirectory`, `llm.discoverModels`, …) are
  loopback-gated in `@deepseek-ai/dsh-client-connection` and the router presents a loopback `Host`,
  so any project `member` can call them on the project runtime — contained by the boundary, never
  cross-tenant, but the first place `member` must mean less than `admin`. The set is not exported
  upstream; the fix is an upstream export or `dsh-compat` restating it under a pin gate, and the
  router filtering it for non-admins.
- `OPEN:` **multi-anchor universes** — now spelled "relax the one-ref-under-`anchor/` genesis
  invariant"; blast radius enumerated in decision 8.
- `OPEN:` **state-path blame for adopted values** — footprints give path-exact *debt*; per-path
  *provenance* of an adopted subtree is separate work, answerable read-side.
- ~~`OPEN:` **the default discharge-authority table**~~ — D1 shipped the conservative table
  (`specs/acceptance/history-core/d1.md`): `test-runner → workspace/**, tasks/**` · `reviewer →
  artifacts/**, dialog/**` · `human → **`; no row grants `fail`; a scope must be covered, not merely
  intersect. A reviewer row for assimilated claims (decision 15's landing site) stays open.
- `OPEN:` **the session-free host projection, and `engine/1` additive versus `engine/2`.** DSH is the
  candidate second host, and the fleet makes the question *more* live, not less — but the fleet's
  runtimes reach canon through the provider, not the wire, so whether a session-free `engine/1`
  consumer materializes is genuinely open rather than scheduled. The deciding fixtures are pinned
  either way: the exact-catalog and schema byte-equality tests fail on an unversioned add
  (`packages/engine-wire/test/engine-wire.test.ts:147-160, 407-416`).
- `OPEN:` **the exact carrier for a transplant with more than one source** — the product caps `causes`
  at 8.
- **Decided, not open:** a departure does **not** surface as a forward-looking informational event on
  the session's next lifecycle line — not until a consumer for one exists. Decision 4 keeps departures
  out of the log entirely; a forward-only marker after re-preparation is the only honest in-log
  variant, and nothing needs it. Recorded in `decisions.md` on acceptance.

**Resolved and struck from this block.** *"Whether policy may raise examined → guaranteed"* —
`guaranteed` no longer exists; `intact` is a custody fact no policy can grant (decision 10).
*"`SimulationId` semantics"* (`decisions.md:323`) — closed by replacing the identifier with `WorldId`
(decision 14). *"Preimages versus `evidence[]`"* — answered by decision 6's own text: `evidence[]` is
the carrier, `preimages` stays closed; recorded with D2. *"Archived-ref TTLs"* — `packages/tools/src/
retention.ts` contains no archived-ref handling, so the answer is that a retention class is added; a
named task in D2, not a fork.

## Addendum — the DeepSeek Harness research record (2026-08-21)

Recorded from the directed research pass that preceded the convergence. DeepSeek open-sourced
**DeepSeek Harness** (`deepseek-ai/deepseek-harness`, npm `@deepseek-ai/dsh`) on 2026-08-13: a
TypeScript/Node agent harness on the Cordis plugin framework — the model adapter, tool registry,
session log, sandbox, and the agent loop itself are replaceable plugins mounted from configuration.
Developer preview; compatibility-breaking changes announced; Cordis and its foundation vendored at
4.0.0-rc.7 with a modification log.

**The session seam maps nearly 1:1.** DSH keeps an append-only `SessionEvent` log under the
invariant "model-visible means logged" (runtime-asserted), with monotonic contiguous `seq`,
source-citation fields (`sourceEventSeqs`), compaction as a surface `replace` shadowing its sources,
refuse-don't-drop on unrecognized required events, forks only at between-turn boundaries
(`ctx.sessions.fork(source, boundary?, childSessionId?)`), and a persistence seam —
`ctx.sessionPersistence`:
locate/create/append/prepare/load/inspect/readFrom/list/listSnapshots — whose backends pass a shared
`runPersistenceContract` suite and must close a crash-orphaned turn with a synthetic
`turn/end {interrupted}` on cold load. That is this repo's turn/publication-batch model with the
correctness layer missing, and DSH's own docs say so: tolerating concurrent writers "needs a
liveness signal beyond the log" — exactly the lease/fence discipline canon enforces.

**A future hosted/resident probe would meet named seams, not internals.** HC8.5's six interception
surfaces map to documented Cordis services: model = a `ctx.llm` adapter; effect = the
`tools/pre-execute → execute → post-execute` waterfall; services = profile/bundle composition with
rows withheld by patch; capture = `session/event` and `agent/*` events; commit = none of its own;
resident = the agent loop is itself a replaceable plugin behind the `Agent` interface, so "one
decide = one step" may be expressible as a runtime-owned loop plugin rather than a halted foreign
scheduler — the make-or-break where both existing residents lost something (ADR-028: LangGraph does
not run Pregel; AI SDK stops after one step).

**The model-provider axis needs none of this machinery**: DeepSeek *models* flow through
`AiSdkCoreProvider` (`packages/ai/src/index.ts:46-117`) plus `CONTEXT_RUNTIME_ALLOWED_MODELS`, with
no adapter, profile, or probe.

**Standing is what makes hosting Harness-shaped work honest.** A DSH session is plugin-injected
context, hook output, shared dirty worktrees, and forks — under the v0.9 reading, refused or
flattened to "simulation"; under this ADR, admitted as labeled departures folding to *unexamined*,
examinable upward by `runtime.examine`, with worlds (decision 14) fitting DSH's sandbox/worktree
plugins and holds. The fourth worked universe is this record made normative.

## Addendum — the W0 probe result (2026-08-21)

W0 ran and said **GO** for Cordis self-adoption. The probe
(`bench/scripts/history-core/w0-probe.ts`, artifact
`specs/history-core/integrations/w0-probe.json`, disposition `specs/acceptance/history-core/w0.md`)
mounts this engine behind bridge plugins in a minimal Cordis tree over the exact pins
`@deepseek-ai/cordis@4.0.1` + DSH seam `@0.1.0-rc.7`, and is DB-free and deterministic
(`--check` byte-compares). Five gates:

- **one-provider-per-service-key — PASS.** Cordis's registry throws on a second provider of a
  service key: decision 1's "one-provider-per-service-key carries the one-provider rule for
  *services*" is the framework's own behaviour, not an aspiration.
- **composition-attestation-observer — PASS.** An observer on `internal/plugin` and
  `internal/listener` enumerates the boot mounted-set and downgrades the recorded regime on a
  post-boot mount (→ reconstructable) or a mediated-seam `prepend` (→ auditable). Decision 5's
  continuous attestation record is buildable on Cordis's public event bus.
- **production-profile-hmr-omitted — PASS**, with decision 1's seal caveat recorded honestly
  (`ctx.plugin` stays available; "no dynamic mounts" is a property of the mounted set).
- **replay-seam-through-bridge — PASS.** `liveThenReplay` is byte-identical through the bridge
  composition and every event round-trips through the mounted `history` service — decision 5's
  "*replayable* is reached only by compositions whose every nondeterminism routes through the seam,"
  DSH loop excluded, shown rather than asserted.
- **truth-layer-provider-skeleton — DEFER → W2.** DSH's `SessionPersistence` backed by canon
  round-trips create→append→load, enforces contiguous `seq`, serves `readFrom`, and hides an empty
  session from `list()`. The full `runPersistenceContract` (crash precedence, erasure, chunk-packing,
  Postgres) is decision 4's W2 gate — and that suite is itself **unpublished** (DSH ships `lib/`
  only), so W2 must vendor it.

Two OPEN items are sharpened: the Cordis pin is recommended **published** at `4.0.1` (annotated in the
OPEN block), and the measured compat budget answers ADR-014's priced objection — the seam surfaces
the fleet binds to are byte-stable across four releases. The engine repo took ten dev-only pins and
the probe sources under `bench/`; nothing frozen, and no production boundary, moved.

## Addendum — the execution record (2026-08-22)

Ren's directive, 2026-08-22: *"please finish adr 030"*, with Opus implementers working the
remaining packages in parallel. This section records the execution decisions the packages needed
settled before they could start — the ones the text above left to "the dependency inventory" or to a
repository that did not yet exist. Each entry names the packages it binds. Nothing here changes a
decision's substance; where it changes a decision's *placement*, it says so and why.

- **Inputs ADR-031 deleted are replaced, not regenerated (W1).** The "published-set decision from the
  dependency inventory" reads from each package's `exports` map — a package's surface is what it
  exports — with `bench/scripts/history-core/lib/closure.ts` answering what an entry reaches. The
  published set is every `packages/*` package (`packages/execution-conformance`, a private test leaf,
  folds into the testkit); `apps/*` stay private. Version `0.1.0` for every package, lockstep —
  ADR-031 decision 3: the package's semver *is* the version, and there is no second live version. The
  registry push is Ren's deployment step; until it happens "published" means the `pnpm pack` tarball,
  byte-for-byte what a registry would serve, and the out-of-tree fixture consumes exactly that.

- **The host plugins are engine packages (W2, W3).** Decision 2's layout put the truth-layer provider
  and the gateways in the product repository (`dsh-product-host`). Executing W2 showed that
  placement to be wrong on this ADR's own first clause — *our context system as a plugin, so everyone
  in the ecosystem can install it*: a DSH user installs the provider with `dsh plugin add`, and the
  package they install must be published by the engine, not by a product they do not use. Its gates
  are engine drills besides — the vendored persistence contract over Postgres canon, `kill -9`
  between staging and fold, `liveThenReplay` through the bridge, the in-process attacker — and they
  live beside the engine's test infrastructure. So the provider, the session-canon-binding service,
  the halt plugin, the model-gateway adapter, the effect-bracket waterfall plugin, the attestation
  observer and the attested-profile checker land in **`packages/dsh-host`**
  (`@context-runtime/dsh-host`): the one package permitted to name the framework, named in
  `bench/architecture.test.ts`'s `FRAMEWORK_BRIDGES` as the deliberate act ADR-031 asks for, with
  ADR-031 decision 4's three rules binding it — no logic in a bridge, one service key one writer,
  framework types stop at the bridge. The product repository's `dsh-product-host` narrows to
  product-specific host plugins (ticket and credential plumbing to the control plane) and mounts the
  published `@context-runtime/dsh-host`. Decision 2's symmetry is intact: the product still trusts
  the engine only through published, pinned packages.

- **The product repository is `~/repos/context-runtime-product` (W4–W6).** A sibling checkout,
  consuming `@context-runtime/*` from the engine's `pnpm pack:all` tarballs by `file:` specifier
  until the registry publish, and `@deepseek-ai/dsh@0.1.1-rc.2` — the umbrella on npm; the seam
  packages the engine pins stay at `0.1.0-rc.7`, which W0 measured byte-stable across that range,
  and the `dsh-compat` shim absorbs the rest.

- **Acceptance is per package, unsigned until Ren signs.** Each package writes
  `specs/acceptance/history-core/<pkg>.md` on the `w0.md` model — gates as properties, each with the
  defect that made it fail first — and leaves the sign-off box empty. This ADR's status moves to
  *implemented — awaiting sign-off* when the last package lands; acceptance remains Ren's act.

- **U1 is not executed here.** Contributing a clock service upstream is an outward action on another
  project's repository; nothing gates on it, and it waits for Ren.

- **Closed 2026-08-23.** Nineteen packages landed in fifteen hours of parallel Opus work, each
  integrated onto `main` only after the full suite ran green there: W1, D4, D1, D3, D2, W2, the
  integration pass, W3, W3b, D15, W2b, W2c in the engine; W4, W5, W6, the W5/W6 union, W5c, W5d
  in the product. What a DSH user installs is `@context-runtime/dsh-host`: a runtime holding only
  its boundary login and a control-plane-minted ticket composes the truth layer, folds its session
  into canon one node per turn, brackets its tools with durable intents a `kill -9` cannot strand,
  and reports its standing through the Harness client. **Deliberately not done, each recorded where
  it was found:** U1 (an outward contribution); the publication kit's move into the testkit (a
  `tsc -b` cycle — Ren's call); stage 2's per-member attribution in canon (no upstream seam hands a
  host plugin the acting principal — a product gate goes red when one appears); the router's filter
  for upstream's loopback-privileged methods; a product tool that acts *inside* a world (DSH's tools
  act on the workspace root — a confinement fork, filed); the durable half of a bracketed effect
  failing after its intent is staged still strands that intent (measured in W2c); no default model
  policy (the fleet names no model until a key policy exists). The freeze-becomes-publication rule
  arms at the registry push, which is Ren's; until then every contract is still free to change.

