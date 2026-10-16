# 接入变化与摘要必须保留什么 / Changing access and necessary information

2026-10-08，Asia/Bangkok。Ren 的“继续”见[来源](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md)。本轮形式化、比较及作者反审为 AI 工作。[当前理论第11节](../../../../theories/becoming/chapters/GENERATED-LOGIC.md)。

**完成结果：对当前接入相同的配置，保留未来允许接入范围内的全部占用区别，恰好足以保留所有允许有限历史的可行性。** 两步“改接—取得”给出必要方向。原生三步历史产生旧范围下完全等价、扩展范围下可区分的配置。只给旧摘要与改接事件，无法总能重建新摘要。

**Completed bounded result:** a fixed future access scope determines the occupancy distinctions required for exact finite-word behavior. Twenty-four new Lean theorems pass; 18 inherited core audits remain unchanged. This is a conditional representation result, not a derivation of the metalogic or a novelty claim.

## 1. Reuse completed work and fix the new target

Read and credit [EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md), with its 42 new theorems and 211-audit receipt. Its native formation, withdrawal, acquisition, release, exact certificate guards, recovery and progress-count results are already complete. Its infinite noncompletion history already separates readiness from scheduler progress. We do not recast any of these as this round's discovery.

The [previous logic continuation](CONTEXTUAL-LOGIC-INTEGRATION.md) established exact frozen-frame conditions and selective abstraction. Its one-bit representation explicitly excludes events concerning a hidden slot. The remaining connection studied here is **organizational access changes → newly relevant occupancy → adequacy of the representation used for logical judgments**. It provides an implementation requirement for descriptions of joint realization. It establishes no ethical priority and leaves the separately authorized G0/J and universal-grounding programmes intact.

The new model reuses `GenerativeCore`'s process and history interface. It supplies a different event alphabet and mutable route; no full-alphabet equivalence with the previous lease model is claimed. The parts of a configuration are analytic coordinates of one process. Shared occupancy and the activity's route remain related by the actual acquisition rule, rather than being independently constituted agent and environment.

## 2. Explicit law and theorem scope

Let `Configuration R` contain `route : R` and `busy : R → Bool`. The domain has decidable equality. A supplied predicate `K : R → Prop` specifies the permitted support scope.

| Native event | Enabled condition | Update |
|---|---|---|
| `redirect r` | `K r` | Set the route to `r`; keep occupancy. |
| `take` | The route belongs to `K` and its support is free. | Mark that support occupied; keep the route. |
| `release r` | `K r` and support `r` is occupied. | Clear that support; keep the route. |

The operations are atomic, identities are supplied, and every permitted slot can be reached by one redirect. Release has no ownership authentication. No cost, topology constraint, fabrication law or learned permission mechanism is encoded. `K` is fixed during a trace. Comparing two `K`s compares their allowed-operation contracts; it does not implement the formation or expansion of `K` itself. Reconfiguration of the current route is an actual native event.

`Agrees K s t` retains the current route and occupancy on `K`. `observe K` returns exactly those data. Step feasibility and the agreement relation are preserved under corresponding updates; `match_trace` lifts an arbitrary finite history with the same event word. Conversely `probe_exact` says that `[redirect r, take]` is feasible exactly when `K r` and `r` is free.

| Main claim | Checked declaration | Boundary |
|---|---|---|
| Equal retained observations preserve every finite word | `observation_iff`, `agrees_after`, `match_trace`, `observation_sufficient` | Current route is retained; permitted operations are precisely those above. |
| With equal current routes, all-word equivalence iff occupancy agrees on `K` | `probes_determine_occupancy`, `fixed_route_behavior_iff` | The necessary direction already follows from the two-event probes; no claim that routes themselves are minimally represented. |
| Any exact state reader must distinguish occupancy differences in `K` | `exact_reader_separates` | Quantifies over all supplied configurations and finite words; approximate or restricted-query readers are different contracts. |
| Unrestricted redirection forbids a lossy occupancy encoding | `unrestricted_reader_injective` | At a fixed route, the encoding of occupancy functions must be injective. It can still use a compact lossless encoding. |
| Native hidden occupancy defeats extension of the old abstraction | `Witness.hidden_formed`, `old_workload_exact`, `new_probe_separates` | The two states are linked by actual steps in the broader process, not a free flip of a readiness predicate. |
| Old active-slot view and destination cannot always determine the new view | `no_blind_redirect_update`, `no_old_view_future_reader` | Input excludes retained history, hidden state and fresh measurements. Additional information changes this premise. |
| Relation change alone can change readiness | `redirect_changes_readiness_only` | Occupancy is unchanged during redirect; the tested access relation changes. |

中文解释：这里的必要性由同一组可检验的问题确定。未来可改接到某位置，就可以用“改接—取得”区分它是否空闲；只要要求对这些问题准确作答，摘要就不能丢掉相应区别。若不要求这些未来问题、只要求安全的近似、或另行保留历史，不能套用这个下界。

## 3. A generated witness and the repair boundary

Start with both Boolean slots free and route 0. Execute `redirect 1; take; redirect 0`. The resulting state differs by an occupied hidden slot. Both states have the same route and the same restriction to `K = {0}`. They therefore agree on **all** finite words of that restricted process. Under `K = {0,1}`, the probe `redirect 1; take` succeeds from the original state and fails from the reached one.

Thus the old projection was exact for the old contract; no earlier theorem was invalidated. Extending the contract exposes a previously omitted relation. At the reached state, redirecting to slot 1 preserves the entire occupancy function while changing immediate readiness. This distinguishes a relational change from changing a detached Boolean verdict.

The pure updater impossibility compares the same old active view and the same destination, with different required updated outputs. Its input cannot choose between them. `refreshed_view` checks that a current value of the newly relevant slot suffices to construct the new view. This is a definitional correspondence, counted as a supporting lemma; it does not verify a sensor, an atomic snapshot or a protocol under interference. A historical log may retain the missing information; this theorem does not deny that possibility.

## 4. Primary-source assessment

Primary sources inspected on 8 October 2026, with scope stated below. PDF fetches for the two abstract-interpretation papers timed out; the web index returned text from those exact author-hosted PDFs. We use only the returned abstract and specified extracts. No external proof artifact was run, and no exhaustive novelty search is claimed.

| Source and inspected scope | Precedent and consequence |
|---|---|
| Xinyu Feng, *Local Rely-Guarantee Reasoning*, POPL 2009, [author PDF](https://home.ttic.edu/~feng/research/publications/LRG.pdf), abstract, §§2.1 and 5 stability definitions and returned portions on hiding | Already treats local reasoning, dynamic sharing and changing rely/guarantee conditions. Stability retains a predicate across the admitted interference relation; the source also exhibits failures of insufficient composition conditions. Dynamic resource scope alone cannot distinguish our work as new. Its analytic resource partitions are not evidence of ontological dualism. |
| Giacobazzi, Ranzato and Scozzari, *Making Abstract Interpretations Complete*, JACM 2000, [author PDF](https://www.sci.unich.it/~scozzari/paper/JACM00.pdf), returned abstract and Theorem 5.3 extract | Already investigates complete extensions/restrictions of abstract domains and gives constructive characterizations under stated continuity conditions. Our direct state-observation criterion is not a new general completeness theory; no lattice-level translation or superiority theorem has been proved. |
| Bruni, Giacobazzi, Gori and Ranzato, *Abstract Interpretation Repair*, PLDI 2022, [author PDF](https://www.math.unipd.it/~ranzato/papers/pldi22.pdf), returned abstract and §7.1–7.2 extract | Already studies local-completeness repair, optimal refinements and forward/backward strategies. The inspected forward strategy assumes a way to find failed completeness obligations. Our fresh-observation boundary is a concrete model premise, not a demonstrated limitation of AIR's full framework. |

**判断：本轮有理论内容，前沿新颖性尚未建立。** 结果把“新的接入关系使旧摘要不够”收紧为有范围的充分必要条件，纠正了以“动态”作为新颖性根据的想法。现有文献已包含大量相邻方法；下一研究必须给出同目标的额外贡献，不能仅把抽象修复改称为生成修订。

## 5. Substantive author counterreview

1. **Has the claimed interleaving frontier already been solved here?** The repository has a completed changing-support protocol, and the literature has richer concurrent logics. Both are credited. The remaining test is representation under mutable access, not a second proof of ordinary interference preservation.
2. **Is the information bound hidden in the definition of correctness?** Correctness requests actual feasibility of independently specified event words. The lower bound uses native probes. It is nevertheless conditional on exact answers for those probes and the stipulated freedom to redirect.
3. **Does the theorem derive permission, support identities or a growing universe?** No. `K`, identities and atomic laws are supplied. Route changes are generated inside that fixed domain; expansion of the permission predicate is a comparison between contracts.
4. **Is the negative witness reachable?** Yes: a three-event native trace joins the two compared configurations in the broader law. Their equivalence for the narrower law is separately proved. The narrower law is not falsely said to generate the hidden acquisition.
5. **Does any change in the future scope invalidate any old summary?** No. The sufficient direction states exactly when retained information is enough. A richer old summary or a smaller target can survive. The counterexample defeats an unrestricted claim, not every extension.
6. **Does injectivity forbid compact encodings?** No. It forbids identifying distinct occupancy functions under the specified exact contract. Lossless encodings, auxiliary history and approximate analysis remain possible.
7. **Does this solve sensing and concurrency during repair?** No. `refreshed_view` consumes the actual current bit. Its identity does not establish how that bit is obtained or remains valid until use. No empirical deployment is claimed.
8. **Are all minimal-state claims proved?** No. The iff fixes the current route; the representation's route component is not claimed minimal. The bound concerns occupancy distinctions, without a cardinality or asymptotic-memory theorem.
9. **Do new relations make old logical theorems false?** No. A theorem keeps its hypotheses. What changes is applicability of an unqualified summary or operational readiness at a changed configuration. Lean and the given object-level law remain explicit premises.
10. **Is this a frontier breakthrough or ethical conclusion?** Neither has been established. The result is useful integration and a concrete boundary for future work. It proves no moral duty to preserve a particular route, target or resource.

This is author counterreview, not independent-agent acceptance. No subagent was requested or used.

## 6. Verification, history and completion

[ReconfigurableSupportLogic.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ReconfigurableSupportLogic.lean) adds 24 theorems, including supporting lemmas: 12 have empty named-axiom reports, 12 use only `propext` and/or `Quot.sound`. The inherited `GenerativeCore` contributes 18 empty reports. The two-module closure has 42 audits, 30 empty, with no choice dependency, proof holes or custom postulates. Empty reports do not remove the theorem parameters or Lean's type theory.

The [successful frozen receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/reconfigurable-logic-checks/20261008T105809.742208Z/receipt.json) binds the two source snapshots, compiler logs and checker to Lean 4.29.1. The first attempted run was rejected for three unused-variable warnings; those were removed explicitly without disabling the linter. No mathematical error is presented as a passed result.

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_reconfigurable_logic.py
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/RECONFIGURABLE-LOGIC-CHECK.py
```

The [before-edition manifest](development/reconfigurable-logic-before/manifest.json) preserves the previous theory, integration, exact source messages and documentary check/edit records. Earlier 38- and 37-theorem proof packages retain their frozen receipts and are not re-counted as new here. Their old documentary certifications remain tied to historical versions. [Current scoped checks](RECONFIGURABLE-LOGIC-CHECKS.json) and [owned index edits](RECONFIGURABLE-LOGIC-INDEX-EDITS.json) cover this continuation, not all concurrent source changes or the separate results catalogue.

**Completed bridge:** mutable access → exact required occupancy distinctions → a native failure of old-view reuse → a precise boundary on blind updating. Reuse these results. The next unresolved connection is how newly relevant information is acquired and used with explicit cost, authority and interference guarantees, and whether that delivers a contribution beyond existing abstraction-repair methods on the same target. No autonomous schedule or unlimited research goal was created.

**后续接通 / Successor, 2026-10-08:** [Acquired readings and actual use](ACQUIRED-SUPPORT-USE-INTEGRATION.md) now completes a conditional execution bridge into this same native process, with 28 new checked theorems, per-slot validation and exact retry accounting. It credits existing handoff, protection and evidence-cost results. Coherent sensing, full writer mediation and atomic validate/use remain supplied realization conditions; permission authority and frontier novelty have not been derived. The local bridge is no longer a pending task. This study's prior documentary edition and check records are preserved in the [successor manifest](development/acquired-support-use-before/manifest.json).
