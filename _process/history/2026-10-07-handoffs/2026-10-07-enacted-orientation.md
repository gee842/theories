# Handoff: is the generative direction derived? (enacted-orientation study)

7 October 2026. AI-authored handoff from the project thread on whether the evaluative direction is generative, written at Ren's request at the end of the round. Branch `claude/generative-direction-g6wosf`; the work is merged into main at `5b10965`.

## What the study answers

Ren asked whether the direction of evaluation (generative rather than valuing loss) is already derived. The answer is **partly**. Read the [study note §11](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM.md#11-评价被实行时取向是否由延续导出) (Chinese) and [`EnactedOrientation.lean`](../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/EnactedOrientation.lean). The module has 27 results and the naturalism package 147. All audits are empty: no `propext`, `Quot.sound` or `Classical.choice`.

Before this round no file derived the direction. `PremiseNecessity` proves the orientation is a necessary input, and the self-undermining argument existed only as prose (§5.2). Every other text assumes the direction or leaves it open, including NONINSTRUMENTAL-CONCERN §15, YITI-REN, valuation §17–19, ContinuationScope, InquiryWarrant and FUTURE-GOOD-INTEGRAL.

## What is proved

The proofs are at the level of eventual realizability (`Can`), where persistence is defined. An evaluation is enacted when a marking `Q` picks out the actual transitions it endorses.

- **No transition gains** (`no_transition_gains`). So `converse CanLe` holds along every history and distinguishes nothing (`loss_order_along_every_history`). `CanLe` fails on every losing transition.
- **Loss is bounded.** With a complete finite list of states, every history has fewer losing transitions than there are states (`strict_loss_bounded`, `loss_endorsing_enactment_bounded`, `loss_marked_bound`). Neither result uses decidable equality.
- **Recurring enactment keeps.** A marking that recurs without bound has an enactment that does not lose (`recurring_enactment_not_all_loss`). With decidable equality, a reachable enactment lies on a return path and keeps everything (`recurring_enactment_keeps`). An activity enacted without bound persists (`unbounded_enactment_persists`).
- **Preserved counterexamples:**
  - Loss can come before persistence: `severing`, `loss_then_persistence`.
  - Finiteness is necessary: `ladder_loss_recurs`.
  - At immediate feasibility, failures of `ContinuationLe` recur without bound in `dip` (`dip_immediate_loss_recurs`), so `law_admits_opposite_recordings` stands at that level.

## Resume point

All of the above is complete and merged. The package checker passes from `experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/` with `python3 check.py`, which needs Lean 4.29.1. Elan's release host is blocked in the cloud container; in this session Lean was installed from the GitHub release tarball `lean-4.29.1-linux.tar.zst`.

## Next concrete step

Decide, from the process itself, which level is the right one for evaluation:

- eventual realizability, where the direction is derived;
- immediate feasibility, where it is not.

A candidate is to prove that immediate-level losses that recur are exactly those recovered on a return path. The whole-history comparison of loss against recovery (§5.4 item 2) would then reduce to the eventual level.

## Open items for Ren

1. Whether "can be enacted indefinitely" or persistence is the measure of good. It is not proved, and if it is introduced as a premise it must be proved necessary.
2. `recurring_enactment_keeps` and `unbounded_enactment_persists` take decidable equality of states as model data, as `persists_iff_regenerating_return` does. The bound theorems do not need it. Removing it from the positive forms seems to require deciding equality to locate the repeat; this was not attempted further.
3. Every exclusive commitment still counts as a loss at the eventual level; it is only bounded per history.

## Spawning a successor

Start a thread with this file as its brief: "Continue the enacted-orientation study from `_process/handoffs/2026-10-07-enacted-orientation.md`; do the next concrete step under the project rules: no axioms, monist framing, no market vocabulary, merge to main."
