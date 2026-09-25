# ADR-013 — The GTC confluence: one project, two layers

- **Status:** accepted — ratified by Ren, 2026-08-09
- **Date:** 2026-08-09

**Context.** The GTC research branch — v0.1, two deep-research landscape reports, v0.2, archived in
`specs/reviews/gtc/` — evolved without sight of Stages 5–7 and converged on this repo's substrate: a
conservative semantic kernel under derived representations, module writes through a validated gate,
composition as versioned data, ablation as the arbiter. Its remaining novelty is the product shape of
the mind layer: named, versioned, selectable Context Systems; feature-carrying candidates; an explicit
eval program. ADR-012 set the entry rules for mind-layer work but deliberately made no plan change;
this ADR merges the branch and carries the plan bump (v0.6 → v0.7).

**Decision.**

1. **One project, two layers.** GTC is this repo's mind layer: the module catalog (entity/temporal/
   epistemic projections, consolidation workers, …) and, eventually, named reference compositions.
   The engine keeps its name and its plan; GTC names what runs on it. The research branch is closed
   by absorption — its stack recommendations (Python, polyglot stores) are branch incidentals, void.
2. **Σ — the Context System — is one object with three binding sites.** A named, versioned
   composition+policy value: bound at build (the default — `COMPILER_POLICY_V1` is Σ v0, digested as
   `compilerPolicyDigest`), at agent (`agents/<id>/psyche/**`, ADR-012 rule 4), and at situation
   (per-turn selection or overlay; the choice and its reason are recorded in the compilation record).
   All three reach the frame through `compilerDigest`, so memoization, the witness, and replay are
   untouched by construction. Mechanics are extracted when the second real Σ exists (rule of two) —
   the first mind-layer experiment is that trigger.
3. **Candidates record features, not only a collapsed priority.** The in-memory candidate already
   carries named components (recency, retrieval score, pin, chronology); at the next compiler touch
   they enter the compilation record beside `priority` (a `compilation-record` version bump). Recorded
   evidence then doubles as an offline experiment set — re-ranking and stage ablation replay from tape
   with zero providers. Rankers are Σ-owned weights over named features; module-local final scores are
   rejected (the one-global-score anti-pattern).
4. **The mind-layer eval program is the track's acceptance discipline**: the switching benchmark
   (state constant, Σ varies — the direct test of context-system plurality), the ablation ladder
   (vector → +recency → +temporal → +graph → +epistemics → full), leave-one-module-out, and two
   headline metrics — **ContextUtility** (useful evidence delivered / compile cost) and
   **WritePrecision** (useful durable writes / all durable writes). Deterministic modules evaluate
   offline on recorded frames (§29); external benchmarks (LoCoMo / LongMemEval class) are validity
   anchors, not the definition of done.
5. **Two dissolutions, recorded so they are not rebuilt.** Proposition identity is the statement
   value's canonical hash — two claims sharing a statement share its value object, and "same
   proposition?" is a hash comparison; a proposition table is void. ContextDiff is a derived tool over
   two compilation records (Stage 8's node inspector; `context compare` in the terminal) — never a
   stored object.
6. **Reference domains (Class B) are named.** Domains whose truth lives outside the runtime
   (repository, calendar, warehouse) enter as references + provenance + rebuildable derived views —
   §9's workspace rule generalized. Coding/project-context modules are this class; the runtime never
   copies ownership.
7. **Owned opens, each waiting for its first consumer** (decisions.md): claim `stance` (stance is
   claim content and may be authored — DENIES/HYPOTHESIZES are what the source did; origin trust stays
   provenance-derived); the causal-predicate admission policy (typed causal vocabulary —
   observed_correlation / stated_cause / inferred_cause / … — with stricter validation than ordinary
   predicates, in the world-model domain's `validate()`); WritePrecision instrumentation (lands with
   the first mind-layer module's acceptance).

**Rejected in the same pass** — do not re-propose: a polyglot mind-layer stack (Kafka/Neo4j/Redis
beside Postgres — the one-engine rule extends upward); a `context_runs` table (invocation records +
compilation evidence already carry it); a dynamic module planner before module plurality exists (the
plan-as-evidence object arrives with the planner); third-party module sandboxing now (§34's
signed-bundle machinery, Stage 10+); authored epistemic-status fields (an injected document must not
self-upgrade to "observed").

**Alternatives considered.**

- Keep GTC a separate project on its own stack — it would rebuild Stages 0–7 worse (no Becoming half:
  effects, realms, fencing, replay), and the branch's own v0.2 converged here anyway.
- Adopt v0.2's schema wholesale (Proposition table, `context_runs`, stance now) — each is either
  dissolved by content addressing, already carried by evidence, or waiting for a real consumer.
- Fold this into ADR-012 as an appendix — the confluence is its own decision event with its own review
  stream to archive; ADR-012 governs *how* modules arrive, ADR-013 records *what* merged.

**Consequences.**

- plan.md bumps to v0.7: the confluence changelog, the Σ landing shape (§20), the mind-layer track and
  its eval program (§32), two §34 additions. decisions.md records the settled/rejected/open deltas.
  CLAUDE.md opens the second track.
- First motions when mind-layer work begins, in order: features into the compilation record (next
  compiler touch) · Σ v0 extracted as data at the second Σ · the first catalog module measured against
  the ablation ladder. Stage 8 is untouched and un-gated by any of this.
