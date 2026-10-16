# Continuation-grounding sketch (development draft)

2026-10-10. AI-authored feasibility sketch for the [continuation-grounding plan](../../CONTINUATION-GROUNDING-PLAN.md), following Ren's proposal and instruction “please write these down, and get ready for implementation” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)). **This is not a registered result:** it is not in the Becoming package, has no checker receipt or record, and nothing here is cited as evidence. It is preserved because the plan's statements were checked against it.

| File | SHA-256 | Content |
|---|---|---|
| `Continuation.lean` | `60d7dbb27c1db0552963d07d3760c9a724339ec5b41b8ca59a234d49955e033e` | 15 definitions, 15 theorems |
| `Audit.lean` | `0a8b11330918d5f7c46abecabe755fda6f8a72255a0bee54aa907b5d6f401bae` | `#print axioms` for all 30 declarations |
| `build_core.py` | `6a8b40406e7a1b486b905f299cf295b5e972e7412375bdf5254c742485d8f507` | compiles the core from the bytes of commit `e448c56b` |

`audit.log` (SHA-256 `b0dd6d340f061d7779c6ab8917daaf6f5d7d45c7fa0d52a4e4fca0a14813ef25`) holds the output: all 30 declarations report no axioms. `lean-version.log` and `core-commit.txt` record the toolchain (Lean 4.29.1) and the core commit (`e448c56b180a62e51c35cd5cc1e42deb5b455377`). The core was compiled from committed bytes, so another session's uncommitted edits were not part of the run. Prelude-only compilation and the checker's audit of generated constants were not run.

## What it showed

- **Held lives (plan W5).** Where every living claim lies in some position's own region (`Valuation.Held`), G0 at claim level is exactly S0 at every position with standpoint neutrality (`Valuation.significant_iff_held`); neither connection nor relational neutrality is used. Two countermodels: standpoint neutrality is needed (`OwnStandpoints.standpoint_neutrality_is_needed`), and a life held by no standpoint gets no significance from S0 and standpoint neutrality alone (`Unheld.held_is_needed`). More generally, with holding decided, where every living claim is reached through formed relations from a held one, G0 is S0 at every position, standpoint neutrality, and relational neutrality only into claims no position holds (`Valuation.Unheld`, `Valuation.significant_iff_reached`); the last is needed (`Reached.transmission_is_needed`).
- **Fed from beyond (plan W1).** With equality of conditions decided, a step at which nothing beyond a family is conveyed into it is inward (`Flow.inward_of_not_fed`), so `Flow.taking_draws_in` gives `Flow.fed_from_beyond`: under balance and dissipation, a finite family without repetition from which formations take at arbitrarily late steps, enclosed around from some step on, cannot from some step on be fed from nothing beyond it (`Flow.Conveys`, `Flow.FedFromBeyond`). Constructively this is stated for each step `N`: it is refuted that at every step from `N` nothing beyond the family is conveyed into it.
- **Crossing (plan W2).** Read with one kind of relatum, conveyance relates two events at a common step when something is conveyed between their relata (`Flow.conveyance`). The boundary of such a continuing family is crossed at arbitrarily late steps (`Flow.boundary_crossed`), so its region is not a cut in the relations (`Flow.Cut`, `Flow.region_not_a_cut`); under N_rel, valuing a relatum's event reaches the living event of what is conveyed into it (`Flow.valuing_reaches_source`).
- **Joint counting (plan W3).** Taking jointly within what a step gives keeps the level (`Flow.joint_keeps`); a step of joint excess lowers it by at least one (`Flow.excess_lowers`), so `n` consecutive steps of joint excess need a level of at least `n` at the start (`Flow.excess_bounded`). Two formations each taking within what the step gives can together take more (`Pair.own_not_joint`), and then no web balances the flow (`Pair.no_web`).

## Reproduction

```sh
python3 -I build_core.py <empty work dir>
mkdir -p <work>/Sketch && cp Continuation.lean Audit.lean <work>/Sketch/
cd <work> && LEAN_PATH=$PWD ~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean -o Sketch/Continuation.olean Sketch/Continuation.lean
LEAN_PATH=$PWD ~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean Sketch/Audit.lean
```
