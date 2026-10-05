# Formation and differential return under one law

6 October 2026. AI-authored protocol saved before the full numerical implementation. The fixture and positive path were selected analytically, not fit to experimental data. This extends the [paid response law](../README.md) and the [local-access selection analysis](../../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md).

**Missing interface:** the earlier formation model supplied one response type, while the selection model supplied two existing seeds. This construction must form alternative types, associate them with a capture site, repair it and distribute the resulting support without installing a new contest preparation or resetting resources.

## Fixed law and preparations

One capture site has intact/damaged state, one resident position (empty/A/H), and capacity for one local fuel unit. Free A and H, resident type, common fuel F and incident source E are explicit state. Precursor P=M−A−H, with counts including the resident. Initially M=3, A=H=0, the site is damaged, vacant and locally empty, F=4 and E=1. An initially considered M=2,F=3 fixture permits useful clonal enrichment but exhausts precursor/fuel if both variants form before repair. Independent pre-run critique therefore required this larger primary fixture to include a genuinely mixed history; the smaller fixture is retained as a diagnostic, not counted as mixed competition.

Both untemplated formation channels have exactly the same propensity μDPF, spend one F and turn one P into free A or H. Either free type associates with a vacant site at propensity ξ free_i F, spending one F. Only resident A can repair at rate ρF, spending one F. An intact site captures E into local fuel at rate gE when its local store is empty. A resident of either type copies at rate βP times local fuel, spending that local unit and converting P into a free offspring. Symmetric bulk copying has propensity β₀ n_iPF and spends one F. Each molecule wears at rate δ and returns P; resident wear leaves site condition and stored fuel unchanged. Site damage has rate α; common and local fuel leak at rate ℓ per unit. Thus a later H resident can inherit an A-repaired site. Formation is not switched off by an external staging procedure.

Primary μ=ξ=ρ=g=β=1, α=δ=ℓ=β₀=1/1000000, H=12. Also compute the zero-loss, zero-bulk reference exactly. Do not sample or tune these rates after inspecting results.

## Prespecified comparisons and outputs

Main arms: active; no formation; no association; no repair; equally priced ineffective repair; no capture; burning captured incident fuel; no copying (both routes); shared return. Shared return routes captures into common F and makes the primary β copying reaction available per capita to both types from common F; paid association remains necessary for repair. No source refill, stored-state reset or free movement is allowed.

Record separate untemplated formation, local and bulk copies, wear, capture, binding and repair events. Report local copies made while the other variant is already present, endpoint A and H, their unconditional difference, total population, intact-site occupation and unconditional A fraction with value 1/2 when no variants are present. The last convention is only an observer statistic and must never enter an event rate. Do not condition on successful formation, surviving populations, useful founders or successful repair. Abundance enrichment is not automatically a relative-frequency or individual-learning theorem. In particular the earlier fixed-seed frequency martingale does not prove equal expected abundance in this model with ongoing formation.

Diagnostic preparations are F=0,1,2 (same otherwise) and E=0. For source-dependent work cost, split repair into a preserving branch (1−σ)ρF and an A-consuming branch σρF; both spend one F and restore the site, while the latter returns precursor and leaves the site vacant. Compare E=1 and E=0 at the same σ=1/10000 and α=δ=ℓ=β₀=1/1000000000. These loss rates were selected analytically after enlarging the fixture, before running the implementation, to preserve a strict source-dependent sign certificate. This extension is analytically chosen to distinguish productive access from catalytic expenditure; numerical results are not evidence for those rates in nature.

## Verification and next obligation

Enumerate all reachable states without truncation. Use exact rational terminal calculations and finite-time outward enclosures, reusing the previously reviewed arithmetic with its dependency hash. Independently reconstruct the law and calculations. Lean checks discrete-path costs, the minimum common-fuel requirement, formation and copy ancestry, and connection to the causal root; stochastic rates and Python refinement remain separate.

Success means that the same initially empty process produces actual alternative variants and a consequence-mediated differential copying/retention effect, with failures retained and supplied chemistry explicit. It does not mean that the variant repertoire, local-access chemistry or learning mechanism has itself been discovered. The next bridge is formation and revision of mechanisms controlling access, sensing and copying when old dependencies become misleading.
