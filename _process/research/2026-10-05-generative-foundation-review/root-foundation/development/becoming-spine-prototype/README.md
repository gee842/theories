# Becoming spine prototype (development draft)

2026-10-09. AI-authored prototype written by an Opus subagent while surveying how to unify the repository into one theory ([plan](../../BECOMING-UNIFICATION-PLAN.md)). **This is not a registered result:** there is no checker, receipt or record, and nothing here is cited as evidence. It is preserved because the plan depends on what it showed.

| File | SHA-256 | Theorems |
|---|---|---|
| `BecomingBridge.lean` | `dae4ba05fb4e488d4ef95ed33e1bc01b9ec372782f864e15c601890ec6ac0125` | 17 bridge theorems and helpers |
| `BecomingRun.lean` | `6c42f8ad86ea07140ee34d7afcc3a65964d943607e5b3d190bff58b6ac3272e2` | `run_window`, `run_unique`, `unfolding_level_is_run_observable` |

## What it showed

- `Frame` = core `Generative.Process` + `realized : S → C → Prop` + `generative : C → Prop` instantiates `GenerativeComparison.Inventory` and `JointContinuationClassification.Continuations` from traces.
- `PracticalJudgment.Robust` ↔ `InquirySufficiency.CommonResponse` (`robust_iff_commonResponse`; the reverse direction uses an encoding process).
- `WholeGroundCoverage.Reached` ↔ core `Trace` (`reached_iff_trace`); history transport is `trace_map` / `trace_lift`.
- `StandardsBridge.revise` is `After` on a stuttering observation process (`revise_is_after`, an encoding rather than an identity).
- `normative_lift` (universe-polymorphic) and `sound_inquiry_gives_positioned_reason`: a visible scope defined as endpoints of executions of a sound policy, plus G0 and D, gives the positioned reason.
- `LiftBetter` lifts a comparison of outcomes to responses with nondeterministic outcomes; transitivity needs an enabled middle response. The choice of lifting rule is a normative premise hidden today by functional `Situation.realize`.
- `RelationalRenewal`'s unfolding is the unique run of a deterministic core process (`run_unique`).

## Reproduction

Copy into an empty directory together with these repository sources (hashes at the time of the run), compile in import order with `LEAN_PATH=<dir> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 -o X.olean X.lean`:

```text
e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8  lean/GenerativeCore.lean
116ea0aec116629103bc01b682510a2ac54b20ac37f41262ef8c14920e56374e  lean/NondualCore.lean
d4a95ca842f46ffa9c23eea92d04cdb45027dc6842148d3d0bdc17cd65ad18f2  lean/inquiry-root/sufficiency/InquirySufficiency.lean
e508683cc80832744a28f44c69f9c2561701cd099219448b75cfdb474c0786ee  lean/universal-ethics/JointContinuationClassification.lean
8ddf51311583755908ba843986f262f7a0b4071764031a6fa1a1bf2c0dbd512a  lean/universal-ethics/WholeGroundCoverage.lean
948d36b4cddc0b2289219604464bd38eb6e607183b157cee1075d50fb9797a03  lean/universal-ethics/generative-capacity/GenerativeComparison.lean
e3e5d866aa755650414eb85f8d3e8a1ba7166914dfc16d2e907f9fa9e0c451af  lean/universal-ethics/generative-capacity/PracticalJudgment.lean
f061dbc44da5cdf11ac5ff79b3f89558c7e177b23b9f121c1048c16ed353a42a  lean/universal-ethics/generative-capacity/StandardsBridge.lean
86ff096d42b7246b74242ba0e68ec90d3624392f14303b0dcd6e8a9c59e42fcd  lean/universal-ethics/generative-capacity/PositiveGroundUncertainty.lean
95cf5800f6827d1896cac186113cccf9561768693c6d6e867a3626cd04fc8408  lean/universal-ethics/generative-capacity/PositionedPositiveReason.lean
1b13fcc34fed86de83e6f09dae82b321422195f31fb97d37024d7143183d0e7b  lean/universal-ethics/generative-capacity/PracticalReach.lean
b97719c886e3dcd0f143a23db62fb7b8556dac35ec5c312fcdf7e14d47cee1d4  lean/deeper/RelationalRenewal.lean
```

(`lean/` abbreviates `experiments/integrated-correction/general-framework/generative-basis/lean/`.) Recompiled independently by the main session on 2026-10-09: all modules compile; `#print axioms` reports no axioms for all 20 prototype theorems.
