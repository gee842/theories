# Independent oracle pre-execution amendments

6 October 2026. This records source work after checkpoint `98fd104`, before any independent or producer schedule outcomes. It is not a scientific validation receipt.

The exact checkpoint draft and its checkpoint-only status record remain in [review-history/checkpoint98fd104/](review-history/checkpoint98fd104/). That source was authored before protocol freeze and was explicitly unexecuted, unreviewed and not the promised frozen oracle. Its SHA-256 is `b9947d1fc0422cd11d6ff0cae603613183fff8087b9d90bfe8a7ee12f9a65923`.

The resumed changes are:

- Replace separate return and acquired-bit fields with exactly two physical `{value, mode}` latches. Each paid meter overwrites its own return bit. Empty/missing modes carry canonical false but cannot be read as acquired false. Past values survive only in the historical trace.
- Remove the numeric transmission value from the finite port. Compute it from the current graph and native n during the paid assessment, save it only in audit diagnostics, and never read that saved number for control.
- Choose four or six scheduled opportunities from the declared continuation mode, rather than the length of an analyst outcome word. The actual Y/X contents reach only their respective physical return events.
- Keep observer admission flags out of guards; the operational decision uses the independently computed actual-state predicate.
- Preserve the root-resolved inherited guards: factual read pays before content/applicability validation; scope loss consumes that paid read. With an offered ten-unit packet but insufficient service fuel, the final inherited miss loses the packet and deactivates the core without a service fee.
- Add the lossless catalog/live-parent projection in [SCHEMA.json](SCHEMA.json), plus a separate metadata freeze target. The checkpoint receipt is never overwritten. Any producer serialization adapter is a later declared layer and may not repair transitions.
- Add an expectations runner that operates only after matching the separately frozen source hashes. It retains all ancestor masses, all configured cases, every event/state and every metric. Its first output is marked independent expectations, not an accepted comparison.

The new plasticity producer has not been inspected or imported while these transition laws and this schema were authored. Accepted ancestor source was read as the reference contract; its operational functions are not imported by this oracle. Root's [protocol-freeze.json](protocol-freeze.json) authorizes the fixed protocol; the oracle source receives its own later freeze. Syntax checks are metadata-level validation and do not execute a plant or schedule.
