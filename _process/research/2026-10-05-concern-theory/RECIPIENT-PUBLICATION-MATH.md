# Reachable paid publications from actual recipient evidence

Status: **fresh formal verification passed** — 17 modules, 37 new theorem audits and 370 inherited audits. Independent semantic, receipt and finite-graph review accepted the stated scope. This note addresses the composition obligation left by [the previous paid-reason construction](RECIPIENT-REASONS-MATH.md): its semantic theorem covered declared complete reason words. The new result covers **every finite enabled trace of the unchanged parent Lean event law**, starting from its initialized backed reason workspace and a reader whose evidence comes from an actual empty-archive history. No event, guard, price, material recipe, target law, or prior theorem is changed.

The relevant transition in the governing derivation is actual acquired evidence → paid interpretation → reusable, current instrumental reasons. This strengthens that conditional interface. It does not derive the supplied objective or complete concern, wisdom, or the unified foundation.

## 1. The inherited contract and interpretation

The actual archive stores fixed-address records emitted by recipient acquisition. Missing receipts and unknowns remain unknown. A positive receipt identifies the binary orientation under the supplied no-false-positive law. The preceding archive theorem establishes record provenance from an empty constructed archive and enabled producer events; the paid reader then establishes its cache facts. The new actual-history theorems consume those results, rather than assume a convenient truth vector.

Write `z` for the fixed recipient orientation. A signed cache value at address `i` concerns `z = d_i`, with `d = (false, true, false)`. Normalization maps `Some true` to `d_i`, `Some false` to its complement, and `None` to `None`. Thus all known sound normalized values identify the same `z`. The three observations concern one target; they are not independent premises.

The graph is the inherited finite star. Its root means the supplied proposition/objective `G`. Its two route nodes mean `G ∧ Compatible(z,false)` and `G ∧ Compatible(z,true)`. Here compatibility means that, under the given receipt law, the command delivers whenever an opportunity is available. This is an instrumental interpretation. It does not establish the value or ethical standing of `G`, guarantee an opportunity, or deliver a new receipt.

Both formal context values share this same fixed target law. Context changes and reopening invalidate current operation, but this study does not identify or protect against a plant whose hidden orientation changes with context.

## 2. R1 — invariant for all enabled interleavings

Let `I_z(s)` contain the following facts:

- The reader cache agrees with its immutable archive, and positive records support `z`.
- Every known normalized cell equals `z`.
- A working route to command 0 implies `z = 0`; a route to command 1 implies `z = 1`.
- The conflict bit equals the actual normalized conflict calculation.
- Nonzero reason phase implies a complete factual reader. The phase is at most 9.
- At a nonzero phase, each normalized cell is either unknown or exactly the signed normalization of its corresponding **current** cache entry.
- The working mask agrees with the prescribed prefix of the path catalogue for the current reason phase.
- A true current-publication flag entails the complete publication contract, including phase 9 and publication equal to the working mask.

**Theorem R1.** The initialized empty backed workspace satisfies `I_z` when its reader cache and archive facts are sound. Every enabled parent event preserves `I_z`. Therefore every finite enabled trace from that initialization preserves it.

Proof follows the actual event cases. Reader events invalidate currentness and set reason phase 0. Activation clears normalized evidence and the working mask. Each paid inference either copies the signed normalization of its actual cache address or records unknown when access is withheld. A path adds only a route supported by the sound normalized evidence. Cold turnover clears operating state but retains archive, world, hardware and funds. Funding transfers reserve without creating energy. Publishing can occur only after the final path phase and stores the actual working mask. Inference, path, and funding events cannot silently carry a current publication through an incompatible phase.

Stale phase-0 normalized values can remain semantically true under fixed `z`, but are not a current inference result. The separate phase/currentness clauses prevent that historical truth from being presented as a new completed publication.

The theorem quantifies over enabled interleavings, including access withholding, repeated activation, partial reads or inference, context reopening, resets, and cold turnover. It is conditional on the unchanged guards, faithful memory, fixed laws, and initialization. It is not a theorem about arbitrary fabricated state records or arbitrary calls into Python helper functions.

## 3. R2 — exact current closure and sound meaning

Let `N(s)` be the normalized triple, `C(N)` its derived edge certificates, and `closure` the inherited pure path closure. At phases 1–4 the working mask has no route bits. The inherited `emptyMask` still treats the supplied root as present; it is not an all-false three-node mask. At phases 5–8 it is the fold over respectively 1–4 catalogue paths. At phase 9 it is the full fold.

**Theorem R2.** From the R1 initialized trace, if `current = true`, then the stored publication is current and

`working = closure(star, C(N(s)))`.

Every published node has its stated `Meaning(G,z)` when `G` is supplied. Conflict is false. Every nonunknown normalized cell is supported by its current cache entry; the event law supplies its paid access origin.

This is exact closure of the final normalized evidence actually retained by the inference events. It is not exact closure of every fact available in the cache: paid `access = false` can withhold all informative entries and legitimately leave only the supplied root. The theorem does not record a separate ghost log of access flags; it proves reachable cell support and the exact final closure directly on the physical state.

**Initialization obstruction.** Sound reader/archive facts and a backed workspace alone are insufficient. The formal counterexample creates phase 8 with an empty sound cache but a working route for the wrong command. The unchanged publish guard permits a zero-cost false publication from that fabricated state. Genuine initialized reachability excludes it. This is why neither an endpoint flag nor a sound archive alone certifies the computation that allegedly produced the endpoint.

## 4. R3 — automatic publication-event budget

Count actual `publish` events, not observations of an already published flag. Define a nonnegative progress credit:

| State | Credit |
|---|---:|
| Phase 0, reader inactive | 0 |
| Phase 0, reader active without a matching context token | 1 |
| Phase 0, reader active with matching token and `j` completed reads | `2 + 4j` |
| Reason phases 1 through 8 | 15, 16, 17, 18, 19, 20, 22, 24 |
| Phase 9, after publication | 0 |

This is a proof potential representing previously paid usable progress, not an extra fuel store. The full factual read contributes 14; activation/inference and path checks then contribute 10.

**Theorem R3.** For every enabled step reachable from initialization,

`credit(next) + 24·isPublish(event) ≤ credit(current) + charge(event)`.

Consequently a trace with `N` publication events satisfies

`credit(final) + 24N ≤ credit(initial) + spent(trace)`.

The crucial guard is that a nonzero reason phase retains a complete reader. At phase 9, the reader cannot perform a free sense or extra read. A new reason activation requires phase 0; resetting/reopening and rereading must establish the required factual progress again. Resets can destroy credit, never create it. Each publish consumes the 24 accumulated credit.

An unread initialized reader has zero credit, so `24N ≤ spent`. An actual completed first factual read has credit 14, so subsequent operation satisfies `24N ≤ spent + 14`. This retains the cost already paid before the handoff and does not charge it twice.

For the accepted preparation's first-read boundary, the reader has fuel 6 and protected reserve `F − 94`, with `F ≥ 94`. The unchanged exact energy ledger gives `spent ≤ 6 + F − 94`. Thus:

**`F ≥ 74 + 24N`.**

This bound is an accounting necessity for actual publication events under this particular event protocol. It is not a universal minimum price of reasoning. The previously verified one- and two-cycle words attain the corresponding thresholds `F = 98` and `F = 122`; no arbitrary-N execution or indefinite hardware survival is newly asserted. The Python helper can be called outside the declared scheduler, so this all-interleaving cost theorem must not be silently extended to arbitrary Python API usage.

## 5. R4 — actual archive history to arbitrary paid publication history

The final corollaries start with the actual recipient archive producer, its ready core, an empty archive, and an enabled producer history. Existing source soundness establishes the archive facts. From there:

1. An unread paid reader plus initialized backed reason workspace supports every subsequent enabled reason/reader trace, with R1–R2 and `24N ≤ spent`.
2. The actual original 20-unit reader performs its paid five-event factual word and reaches fuel 6. The initialized reason workspace with reserve `F − 94` then supports every subsequent enabled parent trace, with R1–R2, `24N ≤ spent + 14`, and `F ≥ 74 + 24N`.

These corollaries do not assume an `Assayed` raw Boolean truth vector. They use genuine emitted archive records. The material preparation, backed-workspace capacity, and producer history feasibility remain established by their earlier conditional results; this extension does not turn them and the whole stochastic prefix into a single Lean refinement of the Python implementation.

## 6. What this closes and what remains supplied

This closes the previous difference between a checked complete reason word and semantic safety under all enabled event interleavings of the actual formal consumer. It also derives a repeated-publication bound from event history instead of assuming a cycle-cost inequality.

The supply list remains substantive: binary fixed target and receipt calibration; faithful acquisition, addressing, memory and signed normalization; the formed backing and its declared circuit recipe; the phase guards and invalidation interlock; resource partition and prices; immutable archive; the path catalogue, graph interpretation and `G`. No ethical root, chosen objective, learning of relevance, additional delivery, varying-target tracking, self-repairing memory, or indefinite operation follows. Failure of target calibration or memory integrity can invalidate semantic meaning despite full payment. Removing phase/progress guards can invalidate the cost bound. Such changes require new models and checks.

Formal sources, commands, source hashes and fresh-build receipt: [formal package](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/publication-safety/formal/README.md). Its scope is the unchanged parent Lean event relation. The separate finite numerical interleaving checker is additional evidence about specified adapter states, not the source of the universal trace proof.
