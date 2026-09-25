# Invocation and Occasion lifecycle

A client invocation is admitted through a typed port and its
schema/gate/Authority envelope. Durable work is recorded by one Domain-scoped
Occasion, which is the single commit spine.

## Invocation

The Runtime resolves the target Yi's committed binding revision, selects the
exact installed port/handler artifact, validates its schema, evaluates its gate
and Authority evidence, and executes with one `PortHandlerContext`.

Handlers may invoke nested commands. Nested commands join the active Occasion
rather than opening a second transaction or appending a side-channel audit
record.

## Occasion commit

The coordinator:

1. acquires the stable logical Domain lock/transaction;
2. supplies transaction-scoped narrow context repositories;
3. collects exact materialized effects;
4. computes the immutable commit;
5. binds every changed Yi root to the actual commit id;
6. persists commit and effect rows;
7. commits once.

An empty Occasion, an effect without materialized state, or an ordinary durable
write outside the coordinator fails closed. A materialization/finalization
failure rolls the whole transaction back.

## Observation and recovery

Callers observe success only after commit. Watches consume committed effects in
Occasion order. Checkpoints, retained tails, consumer positions, recovery,
restore, erasure propagation, and pruning all use the same commit source.
Checkpoint plus tail must reconstruct normalized state.

Authority causal reads and barriers derive their applied frontier from Domain
Occasion heads. First contact, current/barrier decisions, issuer revocation,
and irreversible operations therefore agree on one causal source.

Use async `dispose()` for Runtime lifecycle shutdown. It closes transports and
removes only scope-owned handler registrations.
