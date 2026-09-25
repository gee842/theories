---
name: freeze-liftable-pre-launch
description: Ren lifted the freeze constraint on 2026-08-21 — breaking changes are preferred over compat layers because context-runtime is pre-launch with zero users.
metadata: 
  node_type: memory
  type: project
  originSessionId: c38e6a04-6315-4ec0-8cef-ba400c4b5d94
  modified: 2026-08-21T09:00:57.244Z
---

On 2026-08-21 Ren reversed the standing freeze constraint for the ADR-030 program:
"remove any frozen rules that is in conflict with our new design... do not have v1/v2 or code/data
model forcefully constrained by old requirement... prefer broken changes and since we are not
launched, no legacy compatibility is needed... for any structural problems, I prefer a clean,
coherent, longtermist refactor."

**Why:** context-runtime has no external users. Carrying a compat ladder (v1/v2 families, additive-
only schemas, append-only migration numbering) to protect nobody was buying permanent structural
debt. Ren would rather ship one coherent shape than a correct-but-encrusted one.

**How to apply:** two classes, and always say which one is being touched.
- *Representational* constraints — names, enums, grammars, wire versions, migration numbering,
  schema families, elision rules — may be rewritten. Rewrite a migration rather than append a
  compatibility one; a single clean v2 beats a shim.
- *Correctness* invariants — append-only canon, OCC, per-lease fencing, the effect
  intent/observation bracket, erasure + availability ledger, RLS/tenancy, replay determinism,
  one-active-writer-per-semantic, refs-never-rewind — are the product, not legacy. Never weaken
  them. If a design seems to require it, surface that as a finding instead.

This supersedes CLAUDE.md rule 1's "never weaken a frozen semantic" **for representational
constraints only**, and it applies to the ADR-030 program. CLAUDE.md itself still says otherwise —
it needs updating when ADR-030 lands. See [[adr-030-assurance-model]].
