# 测得的反馈与实际对应 / Measured feedback and physical correspondence

8 October 2026. AI-authored continuation of the [connections audit](PROVED-CONNECTIONS.md), pursuing composition, explanation of supplied premises and real-world correspondence together. [Full evidence, derivation and limits](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/INQUIRY-JUDGMENT-EMPIRICAL.md). [Active completion audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/THREE-CONNECTIONS-COMPLETION-AUDIT.md).

**A concrete physical correspondence is now established for acquired measurements, retained feedback and issued action.** Three published temperature-controller runs contain 1,797 samples. All 1,794 subsequent commands can be reconstructed from the actual recorded readings, time differences and the stated controller. A separately implemented exact-rational check agrees within 7.43×10⁻¹⁴ percentage points. These are archived physical observations, not a newly conducted experiment.

**已有具体物理对应：** 取得读数、保留反馈与发出行动在已发表运行中逐项相连。模型里的读数与行为不再只是两个自由指定的成功标签。但观测与命令一致，不独自证明读数绝对准确、所有未来误差有界，或温控目标具有伦理根据。

The particular response mechanism explains an earlier supplied premise. A proportional-integral controller calculates its command from present error and retained integral, then clips it to the actuator's 0–100% range. Lean derives the command-error bound from measurement difference, memory difference, gains and elapsed time. The result directly supplies a term in the existing action-sensitive scale theorem and composes through its finite-horizon recurrence. **Thirteen new theorems / 26 new declaration audits pass; the five-module source closure has 147 audits.**

这里把原先给定的行动差异展开为同一实际过程中读数、积分、增益、时距与饱和的关系。物理响应敏感度和实际传感误差仍需各自的证据；局部前提被解释，不等于所有前提已被消去。温控装置也没有被冒充为此前玩具模型的同一物理过程。

The physical performance comparison reproduces the authors' rounded improvement: the initial engineering objective is 6.090828, versus 5.764581 in the first validation run, a 5.356% reduction. A second archived run gives 5.558066. Both changed-gain runs have more command movement; the first also has more integrated command exposure. Better tracking does not mean every relevant cost fell. Percent-seconds is an exposure proxy, not measured electrical energy.

The source assessment also changes what can be credited. The paper's stated objective uses absolute command movement; its archived search code sums signed changes. Lean proves that the latter telescopes to the final minus initial command and can ignore a bounded round trip's large movement. Thus the observed performance improvement is supported, while the claim that the archived search minimizes the stated objective is not certified. The original code and this discrepancy are preserved.

**反例和真实损失改变结论范围：** 较好的加权跟踪可以伴随更多动作与更高的命令暴露量；把有符号变化误当成总变化会改变方案排序。不能通过改掉指标含义来消除这些差别。

A separate held-out dataset tests model correspondence. Adding the second heater input improves the second temperature's free-run prediction in the fixed comparison, consistent with actual coupling. However, small one-step errors coexist with multi-degree rollout errors. The maximum training residual is exceeded twice in the held-out first-temperature data. A measured past maximum therefore cannot simply be reused as a guaranteed future uncertainty bound. No outlier was deleted to rescue it.

The current result is a checked mathematical composition, a mechanistic explanation of command discrepancy, and an evidenced physical feedback correspondence. **The overall three-part objective remains active.** The remaining work concerns justified uncertainty and generated alternatives, the actual tuning-source discrepancy, physical timing and response contracts, and their warranted use in practical comparison. The engineering weights and temperature setpoints do not supply G0, basic living claims or legitimate authority.

[Independent review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEASURED-FEEDBACK-REVIEW.md) rebuilt the five Lean modules, reconstructed all 1,794 commands with a separate rational implementation, and independently refitted all four regressions using Householder QR. It accepted this bounded addition and retained the wider completion limits.

[Preserved sources](../../../sources/tclab-benchmark/README.md) · [Numerical results](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-results.json) · [Rational cross-check](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-checks.json) · [Lean receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/measured-feedback-verification.json).

## 从初始误差到完整反馈历史 / From initial error to the whole feedback history

The [retained-memory continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/FEEDBACK-MEMORY-INTEGRATION.md) closes a remaining premise in the first result. **Later integral-memory error is now derived through the controller's actual recurrence**, from initial memory and casewise readout bounds with matched gains, targets and elapsed intervals. It is no longer independently assumed at each step. Branch margins distinguish rejection of both increments, retention of both, and uncertain switching. The resulting command radii directly feed the preceding plant-error theorem; physical response and readout warrant remain explicit inputs.

**从初始条件接通后续历史：** 在同一 PI 更新规则下，后续积分误差由初始误差、每步读数范围及实际饱和分支推得，不再每步重新给定。读数、保留、命令与后续响应是同一活动中的关系。真实热响应、读数校准和伦理比较仍有各自的对应要求。

The continuation adds **13 Lean theorems / 21 declarations; all 168 declarations in the six-module repository closure pass the fresh audit**. An exact boundary witness shows why the extra work matters: arbitrarily close readings can issue the same clipped command while retaining memories 50 units apart under specified illustrative gains. A later shared sample then produces a 50-point command difference. This preserves the earlier one-step result while blocking its use with an unjustified assumption of equal memory throughout.

Rational reconstruction evaluates 12 sequences, including three unchanged controls, across the same three archived runs: **7,176 updates**. Repeatedly using the preceding recorded reading gives maximum command differences of 3.43, 3.79 and 7.92 percentage points. Declared persistent ±1°C readout shifts yield differences up to 46.67 points. Every evaluated difference lies within the propagated bounds; some bounds nevertheless widen to the whole 0–100% command range. Both successful containment and lost precision are retained.

这些是固定历史读数上的完整控制器重算，并非重新观测的反事实温度。上一条读数与当前读数的差可由档案精确取得，但只有取得当前记录后才知道，因此不能凭它证明可以事先跳过测量。±1°C 是明确给出的敏感性范围，不是从档案学得的传感器真值保证。共同的记录时距也不等于完整执行延迟。

Additional checked results propagate command uncertainty into total absolute movement and interval-weighted commanded exposure, and state when separated cost intervals justify a comparison. The wider goal remains active: the recurrent-memory premise is now explained, while future uncertainty, the tuning model/objective contract, physical timing and warranted practical application remain to be joined. [Proof receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/feedback-memory-verification.json) · [Exact numerical certificates](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/memory-results.json).
