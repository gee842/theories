# ADR-012 — Composable context systems

- **Status:** accepted — ratified by Ren, 2026-08-09
- **Date:** 2026-08-09

**Context.** Stages 0–6 are complete; the engine exists. The mind layer above it (the GTC direction — persistent semantic structure, richer memory, attention policies) is the next axis of work, and it must be possible to build *many* context systems on one engine — iterated module by module, evaluated as trajectories — without a plugin framework arriving before its content. Stage 5/6 already landed the first absorptions (structured statement claims, typed contest/supersede edges, explicit bitemporality, compiler epistemic completion) through boundary notes rather than plan changes; this ADR records the discipline those instances followed and re-anchors one obligation Stage 6's ledger edit left implicit.

**Decision.** The runtime is an engine for many context systems, composed on two axes: **domain modules** (what a mind is made of — memory, goals, tools/affordances, self, world-model; §31's `DomainModule` is this axis) and **pipeline modules** (how it runs — the compiler's read path, the write path's interpret/resolve/classify/validate, background consolidation). Four rules govern growth:

1. **Boundary IR over plugin interfaces.** The leverage is the typed objects flowing between stages (the compiler's stage-tagged `Candidate` chain; a future write-side `CandidateOp`), not module registries. IRs are grown from working code, never designed a priori.
2. **Rule of two.** No stage interface is extracted and no registration surface is added until a second real implementation exists. First named instance: **per-domain object-incompatibility semantics** — the v1 exact-identity comparator stands until a domain supplies evidence for richer semantics; that domain's arrival extracts the comparator seam on `DomainModule`. This restores the obligation narrowed in `6c4872c` as an owned Open item and ratifies that narrowing as a decision.
3. **Composition as digestable data.** Which modules run, with what configuration, is a manifest whose digest folds into `compilerDigest` (precedent: `COMPILER_POLICY_V1` → `compilerPolicyDigest`). Determinism, memoization, the witness, and replay are therefore untouched by construction. GTC is a module catalog and, eventually, one reference composition — not a rival architecture and not one loadable monolith.
4. **Personality within the authority envelope.** A mind = composition (structure) + policy (config) + state (content). Per-agent policy later lives at `agents/<id>/psyche/**` as canonical data — manual merge, privileged writes, provenance-gated (external content may never propose psyche changes); the kernel floor (realm banners, approval contexts, standing policy) is non-droppable; fast salience is derived (`proj`), slow disposition is canonical. Capabilities bound what any composition may attend to; policy re-weights inside the envelope, never widens it.

**Alternatives considered.**

- One loadable "GTC bundle" as the mind layer — monoliths cannot be ablated; iteration needs stage-level swaps, and the signed-bundle/sandbox machinery stays §34-deferred (Stage 10+).
- A module/plugin framework now — interfaces frozen before a second implementation exists ossify wrong; the compiler already carries the rule in code.
- Retiring per-domain incompatibility by deletion — obligations end by decision, not deletion; the ledger keeps an owned Open item until the seam's first consumer arrives.

**Consequences.**

- Future mind-layer work (activation/salience as a derived module, goal-conditioned retrieval, topology routing, motif/structural analogy) enters as modules under these rules, evaluated by eval-as-branching (§29) with stage-level ablation as the default experiment shape.
- Commits us to keeping compiler internals policy-total (constants in the policy object — `stabilityRank` is the known residue) and to writing IRs down only as they stabilize.
- No new stages, no machinery now, no plan change: this ADR governs how post-demo mind-layer work arrives, not what ships next.
