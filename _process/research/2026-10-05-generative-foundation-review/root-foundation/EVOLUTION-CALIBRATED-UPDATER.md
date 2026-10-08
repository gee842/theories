# Acquired discrimination and a constructed updating relation

**Selected renewal continuation completed, 8 October 2026.** [The derivation and counterreview](EVOLUTION-CALIBRATION-RENEWAL.md) adds 34 checked theorems / 50 new audits. Actual fresh reference comparisons revise the reader and recover responsive updating across finite changed-channel blocks. It also derives the exact affine sign-transfer criterion and preserves late/mixed-reference and nonaffine failures. This predecessor’s 30/59 proof is unchanged; inspection support is separately declared. Within-block transfer and the checking schedule remain explicit.

8 October 2026. AI-authored continuation following Ren's “继续” and the [prospective protocol](EVOLUTION-CALIBRATED-UPDATER-PROTOCOL.md). **30 new Lean theorems / 59 new explicit declaration audits pass; 142 unchanged predecessor audits are separately rebuilt (201 total).**

**中文结论：**上一轮给定“当前反应是否成功”的正确答案和可用响应规则。这一轮把这个接口展开为实际参考接触、保留读数、局部比较及形成的抑制连接：在明示的稳定通道条件下，生成的报告确实对应当前网络反应，报告又实际控制下一次更新。连接形成前后的行为分别对应原先的持续更新与响应式更新，旧网络及运行支持不重置。这里完成的是这个特定网络的**取得读数 → 形成辨别 → 改变更新 → 进入支持与接续**的条件连接；参考关系、部件作用及构造次序仍有明确前提。

## 1. The explanatory advance

The [preceding study](EVOLUTION-UPDATER-CONSEQUENCES.md) already connects interference, response-dependent returns, updater expiry, replacement and later operation. Its control rule receives a correct success predicate and its replacement repertoire already includes a responsive rule. Neither premise is wrong as an abstraction. The present task is to recover that abstraction from more explicit local relations.

Start with the same matrix, tasks and response law. Three contacts and the inhibiting connection are initially absent; the six reference records are empty. Construction connects the contacts, acquires their actual readings and connects inhibition. The resulting controller reads the retained records and current signals. It does not read the channel parameters or a separately supplied truth value for success. Its effective rule is proved afterwards.

Responses, reference-producing contacts, records, control and support are differentiated roles within this one modeled history. The channel relation describes how a change reaches a contact; it is not a fundamentally independent observer or environment. This representation retains signal transmission, formation order and support consequences. It omits the microscopic production of reference states and component operations. Those omissions delimit this local derivation; they are not evidence that the wider relational theory lacks those relations in principle.

## 2. Two reference encounters acquire a usable sign relation

Retain a current task profile \(s\), the network response \(p=\tanh(Bs)\), and the previous success condition \(s_i p_i>0\) at every coordinate. For coordinate \(i\), the supplied local transmission law is

\[
r_i(x)=g_i x+b_i.
\]

The controller is not given \(g_i\), its polarity or \(b_i\). A reference encounter at zero stores \(z_i=r_i(0)\); an encounter at one stores \(o_i=r_i(1)\). Current contact supplies \(y_i=r_i(p_i)\). A local report is available only after connection and both records. Distinct records permit the comparison

\[
q_i=s_i(o_i-z_i)(y_i-z_i)>0.
\]

`reference_signal` derives the identity

\[
s_i(o_i-z_i)(y_i-z_i)=g_i^2 s_i p_i.
\]

Therefore, for nonzero gain, `acquired_local_exact` proves that the acquired comparison gives exactly the required sign result. Both positive and negative gains are admitted; an unknown bias cancels. This is a relation derived from encountered values, rather than a table assigning a success label to each network state.

The local result has three possibilities: success, failure or unresolved. A known failure suffices for a negative combined report; success requires all three local successes. Otherwise the result is unresolved. `report_requires_all` and `ready_report` establish the full correspondence for arbitrary real response and sign profiles in these three coordinates. Missing contact cannot certify success; constant gain leaves the reference pair indistinguishable and the local report unresolved.

The known zero/one reference states, their correct binding to record slots, the supplied task signs and stability of the channel between reference and use remain premises. This proof does not discover what the task ought to be or prove that an encounter advertised as a reference is trustworthy. Arithmetic, strict threshold comparison and record retention are idealized component laws. Noise and finite precision have not been analyzed here.

## 3. The update gate is assembled, then its effective rule is derived

The construction plan contains ten local events: connect the first contact and acquire its two references; repeat for the other two contacts; then connect inhibition. Each event requires one construction support unit. A contact connection also consumes one available part; the three sensing contacts and one inhibiting connection require four parts. A reference acquisition requires its contact already to exist. No construction event succeeds without its required support.

`acquired_assembly` proves that this sequence, starting with ten construction units, four parts and no records or connections, reaches the described reader and gate. `build_step_support` and `finite_build_support` conserve construction fuel plus recorded expenditure through every finite construction list. The ten units are consumed, not replenished by defining the apparatus to be ready. `three_unit_build_incomplete` preserves a lower-budget case: three units can connect and acquire the first coordinate but cannot form the full gate.

The operative update is now:

- if inhibition is connected and the acquired combined report is successful, retain \(B\);
- otherwise perform the earlier selected coefficient update for the current task.

This controller contains no `Route` label and no call to the native success predicate. `no_inhibitor_continual` proves that before formation it acts as the old continual updater. `formed_update_responsive` proves that after the acquired construction, with stable nonzero gains, it acts as the responsive updater. `formed_run_responsive` extends the equality to every finite sequence of the two supplied tasks, including both the actual matrices and the actual success count.

The formation changes an operative relation. Calling it “responsive” is a classification of its proved behavior. It is not the input that makes that behavior happen. Nevertheless, the local multiplication, conjunction, inhibition and coefficient-update components already have supplied functions. Their arrangement is given by this construction plan. This is conditional formation of the selected rule from local parts, not spontaneous invention of its plan or evolution over an unrestricted circuit repertoire.

## 4. The constructed gate enters the retained support history

The current operational state contains a matrix, active/inactive status and four support counters. It has no strategy enum. `native_cycle_projection` and `activation_projection` prove its correspondence with the preceding abstract carrier under the established behavior. The projection's route label is used only in that proof.

The declared entrance now contains **twelve operational source units, ten additional construction units and four construction parts**. The construction reserve has a specified access rule and is unavailable for ordinary updater renewal. It is present at the entrance, not created after failure. The earlier installed weight-update machinery and starting matrix remain part of that entrance; their formation is not retroactively included in these ten units.

| Event completed | Matrix | Operational stock | Operational source | Operational spent | Operational waste | Construction fuel / spent |
|---|---|---:|---:|---:|---:|---:|
| Entrance, gate absent | \(B(1,1)\) | 0 | 12 | 0 | 0 | 10 / 0 |
| Continual cycle fails to renew | \(B(2,4)\) | 3 | 8 | 0 | 1 | 10 / 0 |
| Contacts, records and inhibition formed | \(B(2,4)\) | 3 | 8 | 0 | 1 | 0 / 10 |
| Constructed apparatus activated | \(B(2,4)\) | 1 | 8 | 2 | 1 | 0 / 10 |
| First responsive cycle and renewal | \(B(2,4)\) | 1 | 4 | 6 | 1 | 0 / 10 |
| Second responsive cycle and renewal | \(B(2,4)\) | 1 | 0 | 10 | 1 | 0 / 10 |

`actual_unformed_failure` and `constructed_full_continuation` check this suffix. The first cycle really uses the unformed apparatus, and the formed apparatus actually controls the later updates. All four parts become the four specified connections. `complete_support_account` checks the final total of 22 support units across remaining stock, source, expenditure and waste. The general construction conservation result and inherited operational conservation account supply the separate event laws. Parts are counted separately; no equivalence between a part and an energy unit is asserted.

Formation is not affordable from the three retained operational units alone under the stated costs. The new reserve is an additional hypothesis, and the lower-budget failure prevents hiding that fact. Activation still costs two operational units. Ongoing sensing has no additional tariff beyond the inherited four-unit renewal law. This equal operating-cost assumption is declared, not measured; the preceding extra-cost threshold remains applicable. Source exhaustion still prevents indefinite continuation.

The physical return relation in `nativeRun` uses actual response success to determine transferred support. That is an explicit causal coupling retained from the earlier model; it is separate from what information the control gate receives. A richer account of this return-producing interaction remains possible, but the present construction does not mistake its own report for the actual return.

## 5. A real change can invalidate an acquired report

Calibrate on identity channels and then reverse the third channel during use. Keep the retained records, target and network unchanged. For a response with the \(C=(1,1,-1)\) signs, the changed transmitted values now have the \(A=(1,1,1)\) signs. `identity_reference_changed_use` proves that the formerly valid reader consequently declares success for \(A\).

At the earlier overwritten matrix \(B(1,4)\), the actual response to \(A\) has the \(C\) signs. `stale_channel_blocks_actual_repair` proves both that this response fails and that the acquired gate suppresses its needed update. This strengthens the preceding freely supplied false-report example: a concrete change in the transmission relation produces the false report.

This does not refute the stable-channel theorem, whose premise is violated. It refutes an unrestricted inference from “the reader was acquired correctly” to “its later report remains correct.” The target, actual response and changed signal relationship are all retained. Calling the report endogenous or historically grounded cannot remove this failure.

## 6. Reuse, primary comparison and substantive counterreview

The existing [recipe-grounding integration](RECIPE-GROUNDING-INTEGRATION.md) already acquires an inverse binary decoder through bound reference encounters, with construction and adverse cases. Its 29 mathematical statements and 800 certificates retain their own receipt and toolchain; they are not counted as new here. The [formed-route monitor](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMED-ROUTE-MONITOR.md) already links acquired records to actual supported control. [Mechanism reconciliation](MECHANISM-STATUS-RECONCILIATION.md) prevents reclassifying these completed mechanisms as absent. This study adds their specific functional correspondence to the real-valued memory network; it does not claim a single chemical history with those models' different materials, budgets or component laws.

The JCGM vocabulary distinguishes establishing a reference-to-indication relation from subsequently using it, and also distinguishes calibration from verification or adjustment. Its calibration-curve entry notes that a curve alone lacks measurement uncertainty. These distinctions support our scope: the exact affine construction is an idealized acquired relation, not a complete metrological assurance. [VIM 2.39](https://jcgm.bipm.org/vim/en/2.39.html), [VIM 4.31](https://jcgm.bipm.org/vim/en/4.31.html).

Modulated learning also has established precedent. Frémaux and Gerstner's 2016 theoretical review treats additional factors that regulate pre/post-synaptic plasticity and examines the role of reward prediction and other modulatory signals. The present success-dependent gate is conceptually adjacent to that established family. It is neither a new discovery of gated plasticity nor a derivation of a spiking or molecular mechanism. Our added result is the checked correspondence among acquired records, a formed gate and this retained network/support history. [Primary authored review, especially §§4.5 and 5.1–5.2](https://www.frontiersin.org/journals/neural-circuits/articles/10.3389/fncir.2015.00085/full). The [reading record](../../../../sources/evolutionary-selection/comparative-direction/README.md#calibrated-updater-continuation) preserves inspected scope and link-only provenance.

**Has correctness only been moved into a definition?** The desired sign condition remains the declared task criterion. The controller's report is calculated from raw readings and acquired records. Their agreement is an algebraic theorem requiring a stable nonzero channel; the changed-channel witness separates them. Correct reference production/binding and exact component laws remain supplied. The theorem removes a success oracle at this control interface, not every premise of correctness.

**Does construction already prove evolutionary selection of the circuit?** No. The construction events and available parts are supplied. Actual later return determines the formed updater's renewal, but its occurrence, inheritance and population prevalence are not derived here. A proof of effective behavior should not be reported as evolution of the component grammar or spontaneous emergence of a comparator.

**Has the cost comparison silently changed?** It has been extended explicitly. The old operational twelve-unit account is unchanged. Ten construction units are added at the entrance, with distinct access conditions, and their complete expenditure is counted. The witness therefore cannot show that the new apparatus can be obtained from the original entrance alone, or that any construction cost is worth paying.

**Does success certify an ethical direction?** No. The native success and return laws supply causal conditions of this organization's maintenance. G0/J and the practical account retain their distinct justificatory work within the same relational theory. The result concerns an implementation requirement: a formed discriminator must keep adequate contact with the consequences that guide revision. It does not establish ethical discernment or inevitable alignment.

## 7. What is complete and what remains to connect

The selected correspondence is complete at this stated scope: a particular responsive rule and its sign-success access are derived from acquired local records and formed connections, and then operate in the retained finite history. The earlier generic mechanism achievements remain credited. No new empirical study is made a completion gate for this theoretical result.

The next explanatory pressure is **maintenance or revision of the correspondence between reference encounters and later use when the transmitting relationships themselves change**. The adverse case specifies what must be recovered: a controller can stop repairing exactly because its formerly valid evidence now reports success. Existing inquiry, monitoring and acquired-interpretation results may supply a response, but their trigger, reference binding and network/support interface must be shown. Merely adding another correct alarm would repeat the supplied premise at a higher level.

This is a localized transfer problem in the selected network representation, not an assertion that calibration or monitoring remains unexplained everywhere in the theory. Wider task spaces, noisy readings, microscopic reference production, discovery of construction plans and population inheritance each keep separate scopes. Standard connectionist/control theory can express this same construction. A generative interpretation and a machine-checked example do not establish field-wide novelty, universal favorable evolution or theoretical superiority.

## 8. Proof and documentary checks

[CalibratedUpdater.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/CalibratedUpdater.lean), its [fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/check_calibrated_updater.py) and [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/calibrated-updater-verification.json) bind the exact final claims. All 30 new theorems and 29 other explicit declarations pass (59 new audits; 201 total with predecessors). The three unchanged predecessors have 142 explicit declaration audits, separately rebuilt rather than attributed to this study.

The checker pins Lean 4.30.0-rc2 and Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`, rebuilds the repository import closure and audits every explicit declaration. Generated declarations are kernel-checked. The receipt records standard logical dependencies, source/compiler/import/manifest hashes and output logs. Proof holes, additional axioms, unsafe shortcuts and warnings are rejected. Development diagnostics remain preserved; compiler errors are not scientific counterexamples. [Documentary checks](EVOLUTION-CALIBRATED-UPDATER-CHECKS.json) separately cover owned integration, links and source bindings. No independent-agent acceptance, hardware experiment, population simulation or repository-wide audit is claimed.
