---
name: adr-030-assurance-model
description: "ADR-030's standing lattice was replaced by Custody + an Examination Ledger, committed 2026-08-21 (2ca9025); the ADR is still proposed."
metadata: 
  node_type: memory
  type: project
  originSessionId: c38e6a04-6315-4ec0-8cef-ba400c4b5d94
  modified: 2026-08-21T09:01:08.785Z
---

ADR-030's `guaranteed > examined > unexamined` lattice **was replaced** — rewritten and committed
2026-08-21 (`2ca9025`), after Ren questioned "what does guaranteed even mean?". The ADR remains
`proposed`; Ren agreed to the rewrite and to four calls: archive the pre-reset acceptance artifacts
as a superseded baseline, keep `intact` as the top badge word, keep departures out of the session
log (recorded carrier-local under decision 6's parity law), and leave CLAUDE.md rule 1 unedited
until the ADR it changes is accepted.

**Why the enum was wrong:** it is a total order over two different subjects. `guaranteed` is a claim
about a *line* (every transition mediated — provenance, reachable only by construction);
`examined` is a claim about a *node at a scope* (verification). So "never departed, never tested"
outranks "departed once, then fully verified", and the middle value is launderable — any
`runtime.examine{pass}` flips the enum because its `scope` field is decoration.

**The replacement:** `ledger(N) = discharge(ledger(basis(N)) ∪ accrue(N), examinations(N))`.
Accruals (departures, shared-world effects, transitions under downgraded composition attestation)
add a *footprint* — the write set as logical paths, computed from canon by diff, never stored.
Examinations discharge `scope ∩ outstanding`. Badge: `intact | examined | unexamined(n)`, a
format-fixed summary, never policy-variable.

**The decisive precedent** (verify before citing — it is the argument that convinced both Ren and
me): the coverage "lattice" is itself a *product*, not a stored scalar —
`effective = min(declared, max(observed, enforced))` in `packages/domain/src/integration/coverage.ts`,
commented "min is the law: a claim never exceeds its evidence".

**Also settled:** "standing" collides with the existing frozen `CandidateStanding`
(instruction|claim|observation|quarantined) in the same materialization pipeline; `live` carries at
least six distinct meanings including a UI binding mode; `convergence` has no referent and is
struck. Under [[freeze-liftable-pre-launch]] the re-carving may now rename either side.
