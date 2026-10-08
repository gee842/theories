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

The result at this stage is a checked mathematical composition, a mechanistic explanation of command discrepancy, and an evidenced physical feedback correspondence. **The overall three-part objective remains active.** The continuations below address retained memory and actual candidate generation; justified future uncertainty, physical timing and response contracts, and their warranted use in practical comparison remain open. The engineering weights and temperature setpoints do not supply G0, basic living claims or legitimate authority.

[Independent review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEASURED-FEEDBACK-REVIEW.md) rebuilt the five Lean modules, reconstructed all 1,794 commands with a separate rational implementation, and independently refitted all four regressions using Householder QR. It accepted this bounded addition and retained the wider completion limits.

[Preserved sources](../../../sources/tclab-benchmark/README.md) · [Numerical results](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-results.json) · [Rational cross-check](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-checks.json) · [Lean receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/measured-feedback-verification.json).

## 从初始误差到完整反馈历史 / From initial error to the whole feedback history

The [retained-memory continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/FEEDBACK-MEMORY-INTEGRATION.md) closes a remaining premise in the first result. **Later integral-memory error is now derived through the controller's actual recurrence**, from initial memory and casewise readout bounds with matched gains, targets and elapsed intervals. It is no longer independently assumed at each step. Branch margins distinguish rejection of both increments, retention of both, and uncertain switching. The resulting command radii directly feed the preceding plant-error theorem; physical response and readout warrant remain explicit inputs.

**从初始条件接通后续历史：** 在同一 PI 更新规则下，后续积分误差由初始误差、每步读数范围及实际饱和分支推得，不再每步重新给定。读数、保留、命令与后续响应是同一活动中的关系。真实热响应、读数校准和伦理比较仍有各自的对应要求。

The continuation adds **13 Lean theorems / 21 declarations; all 168 declarations in the six-module repository closure pass the fresh audit**. An exact boundary witness shows why the extra work matters: arbitrarily close readings can issue the same clipped command while retaining memories 50 units apart under specified illustrative gains. A later shared sample then produces a 50-point command difference. This preserves the earlier one-step result while blocking its use with an unjustified assumption of equal memory throughout.

Rational reconstruction evaluates 12 sequences, including three unchanged controls, across the same three archived runs: **7,176 updates**. Repeatedly using the preceding recorded reading gives maximum command differences of 3.43, 3.79 and 7.92 percentage points. Declared persistent ±1°C readout shifts yield differences up to 46.67 points. Every evaluated difference lies within the propagated bounds; some bounds nevertheless widen to the whole 0–100% command range. Both successful containment and lost precision are retained.

这些是固定历史读数上的完整控制器重算，并非重新观测的反事实温度。上一条读数与当前读数的差可由档案精确取得，但只有取得当前记录后才知道，因此不能凭它证明可以事先跳过测量。±1°C 是明确给出的敏感性范围，不是从档案学得的传感器真值保证。共同的记录时距也不等于完整执行延迟。

Additional checked results propagate command uncertainty into total absolute movement and interval-weighted commanded exposure, and state when separated cost intervals justify a comparison. The wider goal remains active: the recurrent-memory premise is now explained, while future uncertainty, the tuning model/objective contract, physical timing and warranted practical application remain to be joined. [Proof receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/feedback-memory-verification.json) · [Exact numerical certificates](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/memory-results.json).

## 实际候选生成与迁移限制 / Actual candidate generation and transfer limits

The [tuning continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/TUNING-CORRESPONDENCE-INTEGRATION.md) now reconstructs the source's actual finite candidate procedure. A pinned modern local fit, the archived 256-gain grid and its disclosed recurrence recover **the same winning gains `(10,55)` under both the signed and corrected absolute objectives**. The metric error nonetheless reverses 8,454 of 32,640 pairwise rankings. The earlier claim that the source minimizes the stated objective was uncertified; the present reconstruction answers its effect in this case without rewriting the archived code or certifying physical/global optimality.

**候选形成已有实际过程：** 由记录拟合、有限增益枚举和指定工程指标产生比较。修正指标后本例胜出参数不变，但大量排序改变；“有错误”不能代替对错误后果的实查。网格、权重和模型种类仍是给定的工程选择，不能暗中充当伦理起点。

Across six disclosed model/timing contracts, all **1,536 numerical candidate simulations** are retained. The direct recurrence is also compared with the actual GEKKO ARX runtime for four leading candidates and all 599 iterations each; both objective winners agree there, with maximum command difference below 0.0000569 percentage points. This is numerical implementation evidence. It does not assert an unknown historical software environment or a checked refinement of every floating operation.

The stronger limitation is residual transfer. A coherent two-lag family, each paired with its original-record correction, fits that original record equally while disagreeing on changed-input responses. Lean proves this through the recurrence, rather than freely toggling a success predicate. The illustrative ±20% gain range is not an empirically justified domain. Separate recorded validation raises RMSE when the original residual is transferred in both inspected runs; a post-hoc initial-reference adjustment helps one run and harms the other. These failures and mixed metrics remain in the account.

**对应限制也得到解释：** 拟合残差随模型共同形成；把它原样移到不同输入下，额外假定了迁移关系。共同拟合原记录不能独自证明这个关系。验证记录可以限制模型，却不能把过去最大误差直接变成未来保证；修补只在一个记录成功，也不能宣布普遍修复。

**Ten new Lean theorems / fourteen declarations pass; the eight-module closure has 228 audits.** They carry trajectory error into the complete objective, reuse the established finite-frontier and interval-comparison results, prove the residual-transfer nonidentification, and combine calibrated margins with actual-case inclusion. The final protection implication remains conditional on the warranted domain and all relevant calibrations. Engineering tracking cost is not a proof of living protection. [Lean receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/tuning-correspondence-verification.json).

The supplied candidate procedure and source objective effect are now explained at their actual offline scope. The next inference remains **justified measurement/model domains and actual timed feasibility → warranted common response**. The fit's observed runtime, retrospective residuals and hardware command limits do not alone establish these premises; neither do they erase the completed physical and mathematical connections.


[Independent tuning review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/TUNING-CORRESPONDENCE-REVIEW.md) freshly rebuilt all 228 declaration audits, separately reproduced all finite comparisons and validation metrics, refitted identical model coefficients, and checked one complete runtime candidate. No required repair was identified; the same correspondence limits remain.
