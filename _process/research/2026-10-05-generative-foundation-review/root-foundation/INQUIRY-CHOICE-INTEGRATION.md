# 查询与直接回应的比较 / Inquiry versus immediate response

8 October 2026. AI-authored continuation of [Ren's direction](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md). [Current account, §12](../../../../theories/becoming/chapters/RELATIONS-ACROSS-SCALES.md). The [prior revision study](SCALE-REVISION-INTEGRATION.md) supplies the reused probe, state and work charger. This is a new route-comparison law on that state, not a replay of its earlier event schedule.

## Transition and positive argument

The selected bridge is **acquired distinctions → task-relevant response possibilities → choice between further inquiry and existing response**. It supports identification and implementation of practical consequences in the generative derivation; it supplies no first ethical warrant. Records, source, condition, inquiry and intervention evolve together under one declared law. Loss, observation and action are analytical roles in that history, not independent ontological realms.

A distinction is useful here when it separates histories requiring incompatible interventions. The robust-response interval precisely identifies when present evidence already supports a common response. Inquiry can separate incompatible histories, but the response selected afterward must remain possible. This tests the inference from “more evidence” to “better actual outcome,” retaining both constructive and destructive cases.

**本轮结果：**同一证据下的各条可能历史若有共同可行回应，可直接回应；若没有，查询可能通过取得有关区别而恢复可选择性。查询本身属于实际变化，需同时检验途中条件、剩余工作与响应支持。目标的伦理根据和证据的现实校准仍分别说明。

## Mathematical scope and actual comparison

Write `terminal a H l u = a − H*l + u`, with one nonnegative additive intervention bounded by source `S`. `admissible` conjoins that implementation range with terminal interval `[lower,upper]`. Under `H≥0` and `lo≤hi`, a robust common intervention is equivalent to

`max(0,lower−a+H*hi) ≤ u ≤ min(S,upper−a+H*lo)`.

This is an exact characterization, with a least admissible dose when feasible. The action-class theorem separately characterizes observation-based policies by nonempty intersections of admissible actions on each observation class. It assumes a nonempty action type, uses classical choice and is an existence theorem. No sensor formation, probability law or algorithmic complexity guarantee is hidden in it.

The actual route witness reuses `ScaleRevision.State`, `drift`, `probeBody`, `paid` and `workTotal`, including the existing `RemainingDependency.charge`. A new event law permits sensing, a supplied dose, a response computed from the acquired decrement, and waiting. The initial condition is known; the actual constant loss is stored in the joint state but not read by the route selector. The acquired response reads the probe's retained loss. This represents differentiated access within one process. Sensing is exact and the loss stays constant; malformed arbitrary records are not certified by these witness results.

For `a=8,S=5,H=2`, terminal bounds `[7,8]` and prior loss interval `[1,3]`, loss 1 needs dose 1–2 while loss 3 needs dose 5–6 (source restricts the latter to 5). No common dose exists. The same supplied selector chooses inquiry for both histories. The actual probe consumes 1044 work and one stage; response consumes another 1044 work and one stage. Acquired doses 1 and 5 both reach 7; sources finish at 4 and 0. Intermediate levels 7 and 5 preserve the floor 0. These endpoints and work expenditures are checked by exact Lean normalization over the real-valued law.

The common horizon is essential. Immediate response occupies stage 1 and is followed by a free operating-work wait that still advances physical drift; inquiry occupies stage 1 and responds at stage 2. Immediate work is 1044 and inquiry work 2088. Same initial work and source are available to both. These are abstract inherited tariffs, not measured seconds, energy or finite-bit implementation costs. No overhead is charged for the route selector; this remains an explicit omission.

With terminal tolerance `[3,8]`, immediate dose 1 is robust over all losses in `[1,3]`. For the high-loss execution it reaches 3 and leaves work 1044. Under the additive constant-loss law, the same dose has the same stage-2 effect whether delivered early or late; earlier support is no worse before delayed delivery. Thus inquiry has no intrinsic advantage from timing or the name of a finer representation.

With initial 2 and actual loss 3, sensing first reaches −1. Immediate dose 5 reaches 1 at stage 2. The mathematical `waiting_floor` result covers every intermediate real time up to a declared duration for this constant nonnegative-loss law; this is an interpolation property of the model, not measured continuous biological protection. Source and work are separate quantities; the signed condition is not a conserved inventory.

## Failed and repaired route selection

`chooseRoute` first uses the robust interval, then checks only inquiry work and headroom. `selected_inquiry_can_lack_support` shows the omission: support 4 passes these checks but cannot provide the learned dose 5. The failed selector stays in the source and is not presented as a recommended general policy.

`guardedRoute` first checks nonnegative loss bounds, an ordered range, nonnegative initial and lower conditions, ordered tolerances, nonnegative source and work for an immediate operation. It chooses the robust least dose when feasible. Otherwise it requires inquiry work, headroom through the inquiry stage, an unassisted upper-condition bound and enough support for the largest adaptive correction. Under a true loss inside the stated interval, the checked general theorem certifies the selected inquiry's waiting floor and the admissibility of its exact-loss correction. Another theorem certifies every selected immediate dose as robust.

These are conditional planner certificates. A generic end-to-end execution theorem for every real parameter and every charged record is not asserted. The useful and adverse executions are checked concrete realizations. The selector returns an empty event list when neither route is certified; that means no certified route from this repertoire, not a safe or ethically permitted decision to do nothing. A third route could exist. Even a funded denial after an attempted delivery advances drift; a stopped controller subsequently stutters and does not freeze the world.

The repair retains the prior counterexample, rather than treating a failed supplied guard as a failure of the entire relational theory. Changing the loss during acquisition, biased readings, additional support interactions and novel interventions require corresponding bounds or a richer law. Earlier bias/context examples remain credited at their own scopes.

## Theorem map and verification

The [fresh receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/inquiry-choice-verification.json) passes **28 new theorem audits and 133 inherited audits**: core 18, exact organization 24, first scales 21, remaining-dependency 43, scale revision 27. The separate embodied-choice and organized-scales results are not replayed here. Lean `4.30.0-rc2`, Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`; all six local modules freshly compiled against the pinned installed libraries. New axiom dependencies are confined to standard `propext`, `Classical.choice`, `Quot.sound`, with some results needing none. Source, compiler, manifest, toolchain, checker, direct imports and audit logs are fingerprinted; no holes, custom axioms or unchecked decision procedure are admitted. Inputs remained unchanged during the successful run.

The initial compilation caught local syntax/proof errors and failed; they were repaired before the successful complete rebuild. No failed or incomplete proof is counted as verified. [Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/InquiryChoice.lean) · [reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_inquiry_choice.py).

| Result group | Exact theorem names |
|---|---|
| Common response interval | `robust_iff_interval`, `robust_exists_iff`, `minimal_robust_dose` |
| Observation classes | `indistinguishable_conflict`, `observed_class_policy_iff` |
| Timing | `waiting_floor`, `early_support_dominates_before_delivery`, `same_horizon_same_dose` |
| Joint histories and work | `run_is_core_trace`, `deliver_work_conserved`, `run_work_conserved` |
| Useful acquired distinction | `two_losses_have_no_common_immediate_dose`, `low_loss_inquiry`, `high_loss_inquiry`, `shared_evidence_selects_inquiry` |
| Immediate alternative | `wide_tolerance_selects_immediate`, `immediate_is_robust_with_wider_tolerance`, `immediate_uses_less_work` |
| Timing/work failure | `inquiry_can_cross_floor_before_response`, `early_response_keeps_floor`, `selector_rejects_unsafe_inquiry`, `selector_rejects_unfunded_inquiry` |
| Preserved failed guard | `selected_inquiry_can_lack_support` |
| Corrected sufficient guard | `adaptive_dose_admissible`, `guarded_inquiry_has_feasible_correction`, `guarded_immediate_is_robust`, `repaired_selection_retains_useful_inquiry`, `repaired_selection_rejects_insufficient_support` |

## Substantive self-counterreview

This review is by the same agent, not an independent-agent review.

- **Did inquiry receive extra time?** Both alternatives terminate at stage 2. Intermediate floor 0 and terminal target 7 are explicitly different requirements. The comparison would fail if the terminal target were silently imposed throughout the history.
- **Is the immediate rival artificially weak?** It may choose any source-bounded dose from the shared evidence, and the impossibility covers both true-loss endpoints. It is restricted to one irreversible intervention without later feedback. A richer conventional controller may match or improve inquiry; the study does not claim superiority over it.
- **Is the information gain merely a definition?** A general observation-class equivalence is a structural characterization, not explanatory evidence. The installed probe additionally acquires the actual decrement in checked executions, which changes the response. Its exactness and availability are supplied correspondences.
- **Does the upper bound hide an ethical weight?** It is an explicitly supplied outcome constraint, motivated here by excessive correction. No ethical priority or universal tolerance is derived. Different justified tolerances can change the selected route, as the wider-tolerance case shows.
- **Is the corrected selector globally optimal?** No. It selects sufficient routes from an installed repertoire and leaves uncertain cases uncertified. Work/time overhead of calculating these guards, probabilistic tradeoffs, sensor formation, split interventions and support renewal remain outside this result.
- **Has a stopped computation made a real loss disappear?** No. The negative intermediate condition and funded denied-response loss are preserved. Later stuttering is a representation convention, not an assertion of real safety.

## Primary comparison and reading limits

[Stuart Russell's author research account](https://people.eecs.berkeley.edu/~russell/research-bo.html), especially the discussion of metareasoning and bounded optimality, explicitly relates computation choice to later decision quality, resource limits and a joint computational/physical state. It also notes the complexity of metalevel optimization. This credits a conventional account of much of the present question; our use of one joint history is not a demonstrated exclusive advantage. We inspected that author overview, not all linked proofs or performance experiments.

The [CMU archival first page of Russell and Wefald, *Principles of Metareasoning*](https://iiif.library.cmu.edu/file/Newell_box00014_fld01011_doc0001/Newell_box00014_fld01011_doc0001.pdf) contains the abstract and opening introduction. It explicitly counts time/space costs and changed intended responses in assessing computation. The available PDF is one page, not the full paper. The author-linked full PostScript was inaccessible through the browser tool; no full-paper reading is claimed. Our interval feasibility comparison uses no probability or utility aggregation and neither implements nor refutes their expected-value method. Sources remain link-only; no new empirical evidence is claimed.

## Integration and remaining work

The continuation completes the selected conditional comparison: common response feasibility, acquired separation of conflicting histories, costs at a common horizon, early-action success and an explicit guard repair. It advances the theory by making task-relevant scale selection depend on actual response possibilities and their conditions. The next application must establish how observed biological or practical history warrants uncertainty bounds, sensing delay, outcome tolerances and the repertoire. The [organized-scales integration](ORGANIZED-SCALES-INTEGRATION.md) retains its stronger empirical correspondence obligations. No new declaration that all system theories or the unified foundation are complete follows.

[Document and source-binding checks](INQUIRY-CHOICE-CHECKS.json) verify the current edition separately from mathematical compilation. Prior 21- and 27-result source files and verification receipts retain their original validation scopes; older document row-snapshot checks are historical to their editions.
