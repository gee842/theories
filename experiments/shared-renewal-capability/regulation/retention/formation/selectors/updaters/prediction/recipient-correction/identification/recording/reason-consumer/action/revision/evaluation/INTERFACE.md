# Numerical serialization and event interface

6 October 2026. AI-authored implementation interface for the frozen [protocol](DRAFT-PROTOCOL.md). This document names representations and events; it adds no teaching, choice, resource or experimental case law. No outcomes are assumed.

`results.json.gz` decompresses to an object with `source_sha256`, `parent_catalog`, and `cases`. A case has its frozen `config` and `arms`; each arm has `producers`; each producer has aggregate `metrics` and `paths`. Each path has `predecessor_ref`, inherited `probability`, observer-only schedules, complete `runtime_trace`, final `state` and unweighted `metrics`.

Each unique catalog reference is `parent_case/producer/path_index/prefix_index`, including distinct ancestries even if states happen to agree. Its entry holds the exact saved parent prefix state, state hash, source indices, prefix event, old predecessor pointer, mass and observer law. It is a serialization of retained records and lineage, not a second active physical core.

Each live state has:

- `parent_ref` and one full `core` dictionary, replacing the catalog core.
- `physical`: `core_phase`, `core_target`, `core_action`, `acquired_record`, replacing those four old producer fields.
- `binding`: current `scope`, `permission`, `delivery`, replacing those old action-wrapper fields.
- `native`: `n`, `count`, `mode`, reusable `bit`, three isolated remaining `packets`, and `training_reserve`.
- `port`: `built`, `mode`, `generation`0/1, fixed recipe `route`, `opportunity_phase`, and paid `suppressed` control.
- `inventory`: `memory_cells`, `adapter`, held A/H counts/access, `retired_ports`, `omitted_pairs`.
- `reserves`: `later_fuel`, `later_source`, `idle_common`, `idle_source`, `saved_assembly`.
- `new_spent` by tariff, `new_waste`, immutable accounting offsets, status and descriptive outcome flags.

The lossless `parent_view` lens copies the catalog snapshot and replaces its core, the four physical fields, and three binding fields. It never appends another core. Every other inherited field, including old expenditure counters, cells, facts, publication, pointers, old source compartments and qualification history, stays equal to the actual saved prefix. Runtime command guards consult this overlaid current state. `accounting` and `outcomes` are audit instrumentation, not added decision memory. The exogenous intervention schedule may consult its fired-event marker solely to avoid applying an external intervention twice.

Every trace row has `event` and the entire live state after that event. Immutable parent content is resolved through its catalog reference. Read/write events do not store another numeric coefficient. Missing native read enters `read_missing` with inert bit0; only mode supplies missingness. `transfer_absent` yields assessed abstention with zero influence after the same factual read, rather than pretending evidence is absent.

Event vocabulary:

| Stage | Events |
|---|---|
| Entry | `extension.at_actual_parent_prefix`, `native.admission_blocked` |
| Native | `native.pay`, `native.return`, `native.read_known`, `native.read_missing`, `native.write`; corresponding `.pay_blocked`, `.return_blocked`, `.read_blocked`, `.write_blocked` |
| External controls | `suppression.paid`, `suppression.blocked`, `intervention.permission_loss`, `intervention.scope_loss` |
| Evaluation N | `evaluationN.read`, `.read_blocked`, `.write`, `.write_blocked` |
| Recipient N | `recipientN.initiate`, `.guard_blocked`, `.source_blocked`, `.surcharge`, `.surcharge_blocked`, `.miss`, `.rent`, `.continuation_blocked`, `.sense`, `.reserve`, `.work`, `.acquire`, `.write` |
| Opportunity N | `opportunityN.abstain`, `opportunityN.closed` |
| Replacement | `replacement.blocked`, `.assemble`, `.release_later_accounts` |
| End | `continuation.stopped`, `continuation.complete` |

N is1 or2. Blocked markers preserve the actual state apart from disclosed status/instrumentation or consumed opportunity. They do not manufacture a physical work, read, return or payment.

The explicit zero-cost opportunity-close event follows the scheduled evaluation/use attempt. It records first-closed/finished and can consume an idle unsuccessful opportunity; it never erases a pending read or an executing RI phase. Thus closing the schedule after a write shortage cannot satisfy replacement's consumed-port guard; an interrupted rent likewise cannot satisfy the ready-core guard. A scope cut does not itself close an idle opportunity. Missing initial hardware can close its first failed attempt, permitting the separately paid held-pair construction.

Native funding and pay2 form one atomic guarded event. In-progress return/read/write finish the already-paid private lesson even if scope later changes; a new native pay rechecks admission. Scope/permission interventions in frozen cases occur after native completion. The physical source-return guard requires only the actual0 or2 to be available; a missing return2 capacity blocks the paid prefix rather than changing its observed label. All configured native source packets contain2.

Aggregate metrics distinguish native acquisition, positive assessment, attempted/completed RI use, actual receipt, actor/recipient/source stocks, cost and unfinished escrow. The parent probabilities are retained coarse-history probabilities, not a new full M60 formation distribution. No ethical score or simulated equilibrium is reported.
