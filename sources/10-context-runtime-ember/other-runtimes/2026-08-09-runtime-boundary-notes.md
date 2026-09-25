# Boundary notes for the implementation agent

From Ren, drafted with the design session on 2026-08-09 and passed to you manually by Ren.

**Scope declaration, read first.** Nothing here changes the plan, the stage sequence, or any acceptance criterion. These are implementation-level choices *inside* §20 and §21, to be applied **only at the named stage boundaries**. Nothing below applies to Stages 1–2 — continue Stage 1 exactly as planned. If any item seems to conflict with plan text when you reach it, stop and ask Ren (CLAUDE.md rule 3).

**Housekeeping:** `specs/acceptance/stage-0.md` still reads "awaiting Ren" while Stage 1 is underway — confirm the sign-off status with Ren alongside this note.

**Background, one paragraph.** Ren is developing a mind-layer direction (GTC / composable context systems) that will run *on* the runtime as domains + compiler modules, after the §33 demo. Your engine work needs no change for it. The two items below are its only footprint in your lane: they keep future seams cheap without building any of them.

## At Stage 3 — when building the §20 v1 compiler

- Write the pipeline as internally explicit stages — gather → score → select → order → render — pure functions with a typed candidate object flowing between them. (The compile record already requires candidates / selected / rejected-with-reasons, §20; this is code shape, not new machinery.)
- Lift the §20 constants (category budget shares, priority weights) into one data object instead of inline literals, and fold that object's digest into `compilerDigest`, so memoization and the witness discipline are unchanged.
- Do **not** extract public interfaces, plugin points, or dynamic loading. The rule is: a second implementation extracts the interface. This item is deliberately just shape + data.

## At Stage 5 — when designing the memory domain

- `Claim.content`: beside free prose/blob, support an optional structured statement form — `{ predicate, args: { role: ref | value, … } }` as a CanonicalValue. The predicate vocabulary is **data, not schema** (no per-predicate zod kinds).
- `memory.contest` / `memory.supersede` transitions carry structured claim-to-claim references, so contradicts/supersedes edges are queryable rather than prose.
- Make bitemporality explicit in the claim schema: `observedAt` (when true of the world) vs record/topological time — §21 already draws this distinction conceptually.
- Compiler epistemic completion: when a selected claim has contested partners (§24 contested values, contradiction pairs), surface the disagreement in the same compilation — Law 12 applied at compile time.
- Note: structured statements make the open "domain comparator" item (decisions.md → Open) computable — same subject + predicate + scope with incompatible object ⇒ contradiction candidate. Sketch it there when you arrive; mark genuine forks `OPEN:`.

Everything else: the plan as written.
