# Preliminary bounded-horizon checks for the renewal–closure target

6 October 2026 (UTC). AI-authored. These scripts support [the roadmap](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-ROADMAP.md). They check the conventions of the target theorem on tiny cases before any Lean work starts. **They prove nothing.** A finite horizon cannot certify endless renewal. Capping the reserve keeps the search finite; an "ends" verdict is trusted only when the cap was never reached.

| Script | Case | Output |
|---|---|---|
| `selfloop.py` | One kind that depends on itself and opens a channel (rate `a`, span `l`, formation demand `m`) | `selfloop-output.txt` |
| `twokind.py` | A non-channel kind P and a channel kind Q that depend on each other | `twokind-output.txt` |

Run with `python3 selfloop.py` and `python3 twokind.py`. Neither script needs any dependency. `twokind.py` runs for several minutes.

## What the runs show

**One self-dependent kind.**
- `a·l < m`: ends for every initial reserve tried, and the cap is never reached.
- `a·l = m`: persists through the horizon when the initial reserve is at least `a`, and ends from zero. That timing buffer must appear in the exact statement.
- `a·l > m`: persists through the horizon, even from a zero reserve.
- `l = 1`: never renews, because no token outlasts the tick in which it acts.

**P and Q depending on each other.**
- `aQ·lQ > mQ`: persists from every reserve tried.
- `aQ·lQ = mQ`: ends from reserves 0 and 5. From reserve 20 it is still running at tick 70 but has ended by tick 100.

This is what the target predicts: a balanced channel cannot also cover P, which brings nothing. So **closure plus openness to an unbounded flow is not sufficient**, and the renewal inequality must hold where the theorem places it. The exact outputs are in the two `-output.txt` files.
