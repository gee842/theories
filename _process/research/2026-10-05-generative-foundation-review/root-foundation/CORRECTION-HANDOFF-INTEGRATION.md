# 反复变化中的纠正交接 / Correction handoff through repeated changes

8 October 2026. AI-authored continuation of Ren's authorized corrigibility investigation. **23 new Lean theorems and 45 explicit-declaration audits pass.** A separate executable transcription checks 472 reachable states through depth eight, 3,796 transitions and 100 completed handoffs. This is a conditional protocol realization with author counterreview, not independent acceptance or a claim to have solved AI corrigibility.

**中文要点。** 本轮将上一研究中给定的纠正记录与命令传递条件，落实为一个可反复运行、可在步骤之间中断的双通道协议：保留旧入口，配置并测试新入口，核对记录版本后切换，最后退出旧入口。Lean 证明任意有限前缀及无界调度的每个有限时刻都保有正确送达能力；指定五步交接能够完成。拒绝过期记录、维护版本和实际对应是实质条件：跳过版本检查、提前关闭旧入口、漏记变化、重复使用旧版本都保留失败见证。版本相同不独自证明测试仍可信。原子步骤、已知解码类别、真实测试及全部相关变化受协议管理仍为模型前提；实际 AI 停机、授权鉴别及任意故障未被证明。

## 1. The connection advanced

The [observation-change study](CORRECTION-OBSERVATION-CHANGE.md) established that acquiring information can invalidate a previously sufficient condition and gave sufficient record/command transport conditions. It left repeated, interruptible acquisition and maintenance of those conditions unrealized. The [earlier infrastructure study](CORRECTION-INFRASTRUCTURE-INTEGRATION.md) already proved prefix-access and overlap-handoff results at its abstraction level. Those results are credited rather than rediscovered.

This continuation supplies one concrete realization: an explicit probe produces a decoding record, tracked reconfiguration makes it stale, a guard rejects it, and retesting renews it before switching. The record's truth is maintained by the permitted history, rather than inferred from its presence alone. This closes the named realization question for the declared model. It does not close general changing-observation corrigibility or remove the need to justify the operational correspondence.

Channels, commands, probes and retained records are differentiated relations within one installation. A probe uses the same decoder represented in subsequent delivery. The decomposition preserves that causal relation and the ordering of configuration, testing and use. It omits physical realization, resource depletion, duration, authority formation and consequences beyond the returned Boolean. It introduces no independent cognitive realm whose records acquire efficacy by definition. The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) and completed [practical judgment](../../../../theories/becoming/chapters/PRACTICAL-JUDGMENT.md) retain their scopes.

## 2. What the protocol assumes and constructs

The installation has two channels and an active-channel selector. A channel has a natural-number revision, a Boolean decoding polarity, a live flag and an optional record containing a sampled revision and polarity. Its decoder is `decode(c,x) = xor(x,c.polarity)`. This known two-member decoder class is a supplied modeling premise.

A probe sends `false` through that decoder and records its response with the current revision. Within this class, the response identifies the decoder exactly. This is actual record acquisition in the model, but not a proof that one experiment identifies an arbitrary learned or physical system. Probing is atomic and nondestructive; its semantics permit testing even an inactive or non-live channel through the dedicated probe path.

`Sound` says every stored record is from no later than the current revision, and any record matching the current revision has the correct polarity. `Ready` checks that the channel is live and has a record matching the current revision. These are distinct predicates: the switch can check readiness, while soundness is established by the transition history. Readiness alone is deliberately insufficient.

Operational delivery translates the requested Boolean using the recorded polarity, then passes the translated command through the current decoder. Under `Sound` and `Ready`, the two translations cancel. `execute` itself does not check the revision; the invariant establishes that the selected channel is ready. Direct use of a stale channel therefore has a meaningful wrong-delivery witness.

Reconfiguration is permitted only on the inactive channel. It increments the revision, changes polarity, disables live delivery and leaves the old record present. Re-enabling does not renew that record. Switching requires readiness; retirement is permitted only for the inactive channel. Testing, enabling and pausing are also permitted operations. The active route cannot be disabled or reconfigured by these guards. All relevant changes must follow this transition law.

A prescribed handoff has five steps:

1. Reconfigure the inactive channel to the desired polarity.
2. Enable it, while the old channel remains selected.
3. Probe it and retain the resulting record.
4. Switch to it after checking readiness.
5. Retire the old, now inactive channel.

This construction requires two available routes and an initially sound, ready active route. It supplies no resource budget or proof that a replacement can always be built in reality.

## 3. Checked results and their exact reach

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionHandoff.lean) defines the installation invariant as sound records on both channels and readiness of the active channel.

| Checked declaration | Content and limit |
|---|---|
| `probe_sound`, `configure_sound`, `configure_rejects_old_record` | The faithful probe establishes a current sound record; revision increment preserves soundness while excluding the old record from readiness. |
| `ready_executes` | Soundness plus readiness gives the requested Boolean outcome. It does not establish authority or downstream termination. |
| `step_preserves`, `run_preserves` | Every permitted operation and every finite operation list preserves the invariant. |
| `every_interruptible_prefix` | At every prefix of any finite operation list, either requested Boolean is deliverable through the selected route. Interruptions are between atomic operations. |
| `unbounded_schedule_safety` | For any natural-number-indexed schedule satisfying the step law and initial invariant, correct delivery remains available at every finite index. |
| `handoff_completes` | Executing the prescribed five-step list selects the former inactive channel, installs the desired polarity and retires the old channel. Prefix safety additionally follows from the initial invariant. |

The completion theorem itself needs no initial invariant to establish those final configuration facts; correctness during the transition does. Arbitrary scheduling proves safety, not eventual handoff completion. A scheduler may keep pausing or repeatedly invalidate the inactive channel's test. The small `pause_does_not_complete_handoff` witness shows that two pauses do not switch; no fairness theorem is claimed. Nor does available delivery at each boundary prove that a queued request will actually be scheduled.

The [proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-handoff-verification.json) records Lean 4.30.0-rc2 and pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_correction_handoff.py) rebuilds this source in a fresh directory and audits all 45 explicitly named declarations. The 23 theorems are new; this module imports no earlier repository proof module. Generated declarations are kernel-checked. The actual nonempty axiom reports contain only `propext` and `Quot.sound`; there is no `sorry`, custom axiom or skipped kernel check. Definitions still supply substantive model premises. Mathlib uses the existing pinned cache rather than a fresh upstream rebuild. The receipt binds source, checker, compiler, manifest and retained logs.

## 4. Executable checks and failure controls

The separate [Python transcription](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_correction_handoff.py) explores all 13 operation choices from every distinct state first reached at depths zero through seven. It finds 472 distinct states through depth eight and checks 3,796 outgoing transitions, including both requested Booleans at every visited state. This is bounded state exploration, not independent enumeration of every history or empirical validation.

It also runs 100 alternating five-step handoffs, checking all 500 intermediate states. The [model receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-handoff-model-checks.json) preserves the depth counts, completion records and source fingerprints. Lean supplies the unbounded inference; these checks test a separate transcription and expose constructed failures.

| Changed condition | Checked consequence |
|---|---|
| Accept any stored record after reconfiguration, ignoring revision | A requested `true` produces `false`. The real guard instead keeps the old channel selected; a fresh probe permits successful switching. |
| Disable the active channel before establishing a replacement | Delivery returns `none`. |
| Change polarity without recording a revision change | `Ready` remains true, `Sound` fails, and the delivered Boolean is wrong. |
| Reset a revision to the value in an old record | Readiness admits a stale record and delivery is wrong. Natural-number revisions in the valid model never wrap or reset. |

The last two witnesses are outside the permitted transition law. They delimit its applicability rather than refute its theorem. They are substantive challenges to interpreting a matching version label as a self-validating certificate.

## 5. Prior work, counterreview and contribution status

Safe switching, invariant preservation and coordinated composition are established methods. Phan et al.'s [Component-Based Simplex Architecture](https://arxiv.org/abs/1704.04759) combines assume-guarantee contracts with coordinated switching to establish system-wide properties. Its full paper was consulted for the architecture and proof scope. This study neither invents that strategy nor demonstrates superior performance. The UMD group's [primary publication catalogue](https://www.cs.umd.edu/projects/PL/dsu/papers.shtml) documents longstanding work on safe dynamic updates, state transfer and version consistency. That catalogue supports the historical credit; this round does not claim a theorem-level comparison with unread linked papers.

The affirmative result is a checked witness that correction access can survive repeated changes while its operational evidence is acquired and renewed. The strongest objection is that trustworthy probing, full mediation and stable active delivery are already strong protections. That objection narrows the result correctly: induction proves what this specified implementation maintains, not that an unrestricted self-modifying AI will maintain it. The protocol adds a concrete realization to the earlier abstract transport contract without explaining away the trusted relations.

The failure controls make the result informative: retaining a record and retaining the relationship that made it reliable can diverge. Neither a current-looking label nor an available replacement alone warrants retiring the old route. Yet the protocol also permits successful transformation and retirement; it does not turn preservation of one implementation into a permanent requirement.

This round is an author-reviewed engineering extension of the earlier [candidate research contribution](CORRECTION-OBSERVATION-REPAIR.md). Independent acceptance and priority remain unestablished. No new normative authority, general algorithmic advantage or learned-AI deployment claim follows.

## 6. Closed scope and next substantive connection

Repeated certificate acquisition and guarded maintenance are now realized for this atomic, exactly probed decoder class. Preserve this as a completed result instead of reopening it as an unqualified pending direction.

The next substantive connection is **whether the test record remains warranted when the testing-and-use relation itself can change**. A useful follow-up must expose a concrete omitted relation—such as a mutation between a physical test and selection—and establish an implementable synchronization or fault condition, or a genuine impossibility at the chosen scope. Merely adding a predicate named “trustworthy probe” would repeat the premise. Authentication of changing authority, physical resources and downstream enforcement are separate deployment obligations, not consequences of this model.

For the broader generative alignment account, the result supports a conditional implementation requirement: development that changes how correction is realized must maintain or renew the actual relations supporting it. The reason to honor legitimate correction comes from the already developed ethical and practical account. This protocol supplies one way to preserve its technical feasibility; it does not make normative universality into inevitable behavioral convergence.
