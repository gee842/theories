# Execution and preservation

The original [protocol](PROTOCOL.md) precedes producer execution. The first
source snapshot and its source/protocol hashes are preserved under
`development/attempt-01/`. This is an implementation of its fixed twenty cases;
no extra cases are added for other acknowledged limitations.

Before the first run, the following stopping convention was fixed. Lost
contact, interrupted commitment and interrupted reading stop immediately with
their actual pending, escrow and reader state. Conflicting completed records
finish all four reader operations, then undergo the same final leak/wear
sequence as ordinary cases and stop at `no_installed_command`. Later damage is
applied only after successful reconstruction. An unavailable repair attempt is
recorded without changing the physical state; it is not an admitted native
event.

The ninety-four-event ancestor is stored once with its complete state history.
Every case begins at that identical actual endpoint with total expenditure 80.
Its suffix contains complete before/after states and is joined to that ancestor
without resetting any quantity. Repeated prefixes across cases are experimental
alternatives, not multiple funded uses of one physical endowment.

The full post-assembly guard check also evaluates an intentionally incorrect
capacity-78 view without modifying the actual state. Its purpose is to expose
the material reuse error: the real native capacity is 72 because six parts
remain bound in memory/control. This diagnostic is neither an admitted copy
nor a second physical continuation.
