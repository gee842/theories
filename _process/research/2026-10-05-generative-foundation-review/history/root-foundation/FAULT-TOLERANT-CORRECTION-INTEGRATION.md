# 部分失陷下的纠正 / Correction under partial compromise

8 October 2026, Asia/Bangkok. AI-authored continuation of Ren's further “continue” after [acquired correction](ACQUIRED-CORRECTION-INTEGRATION.md). **37 new Lean theorems / 68 explicit-declaration audits pass, with 85,680 matched executable records.** Twenty-nine audits have empty axiom lists; the remaining reports contain only standard Lean axioms. This is a conditional mechanism and theoretical integration, with author counterreview. No independent acceptance, new distributed-systems algorithm, cryptographic implementation or deployed-AI validation is claimed.

**中文结论。** 不再要求每个读取者和凭据签发者都正确：允许明确范围内的任意失陷，以不能被任何一个已纳入故障情景全部控制的支持集合，分别认证观察与有范围的许可。共同管理、软件或来源造成的相关失陷须进入同一故障情景，多个名字不等于多个独立根据。正面结果接到实际命令执行、资源消耗和防重放；反面保留相关失陷遗漏、可用性下降、额外检查耗尽回应能力及全部支持可能失陷的界限。这里证明的是既有委托范围的保真，不是签名数量创造伦理正当性。

## 1. Connection advanced and inherited scope

The preceding acquisition study generated an unlisted route and revalidated it, but relied on faithful inspection and a current credential. Its final countermodel admitted a captured credential process. This study replaces a single affirmative inspection or issuer with **two fault-aware attestation checks for one concrete transaction**. The read check concerns the actual current route; the issuance check concerns the current delegated mandate. A signed current-looking request is no longer enough on its own. Counterreview also found a stronger conventional safeguard: because the monitor already has the scope table, the final recommended executor checks that table directly before collecting certificates. The earlier attestation-only executor and its failures remain as explicit comparisons.

We reuse, rather than reopen, the [normative direction](ALIGNMENT-DIRECTION-INTEGRATION.md), [practical judgment](PRACTICAL-JUDGMENT-INTEGRATION.md), [model/reliance work](MODEL-REVISION-INTEGRATION.md), [acquired route](ACQUIRED-CORRECTION-INTEGRATION.md), [review coverage](SELECTOR-REVIEW-COVERAGE-INTEGRATION.md) and [protected-interval boundary](CORRECTION-FRONTIER-BOUNDARY.md). The latter already explains why a last unobserved mutation can defeat a command and supplies a local reservation repair. This module still assumes a protected transaction; it does not prove an end-to-end refinement into that separate lock protocol. The [warranted-acquisition investigation](WARRANTED-ACQUISITION-INTEGRATION.md) already connects real evidence and revisable descriptions at its scope; our formal fault model does not replace its empirical obligations.

Within the nondual account, readers, issuers, records and the command monitor are differentiated activities in the installation's wider formative history. Their susceptibility to common control or error depends on actual shared relations. “Protected” means that the admitted changes do not rewrite a specified relation during the transaction, not that an evaluator exists outside generative reality.

## 2. A fault envelope and an exact availability condition

Let `R` be the registered domains and `F` a nonempty finite family of possible jointly faulty domain sets. Some member of `F` must contain every actual deviation from the relevant specification. A domain outside that set must satisfy the supplied local reading or issuance law. A faulty domain may lie, approve arbitrarily or withhold its response. No probabilistic independence is assumed, and conforming domains need not be morally infallible: their formal task is narrower.

For supporters `S` of one exact statement, the implemented certificate test is:

`for every B in F, some registered supporter lies outside B`.

Therefore the supporters cannot all be faulty under any admitted scenario. If the actual faults are covered and nonfaulty supporters only endorse a property when it holds, an accepted certificate implies that property. `certificate_witness` and `certificate_sound` prove this inference. The truth of the fault envelope and the nonfaulty behavior law remain premises; the result does not derive them from agreement.

Soundness differs from availability. For this test to accept whenever all nonfaulty domains support a valid statement, while faulty domains may withhold, the exact condition is:

`for every A,B in F, some registered domain lies outside A union B`.

`availability_iff_separated` proves both directions. If `A` contains the actual withholding faults, the remaining supporters must escape every other admitted `B`. If two admitted fault sets together cover the roster, that response pattern cannot certify. This is a single-statement availability result under specified responses, **not Byzantine agreement, a distributed register theorem, asynchronous termination or a new consensus threshold**.

Additional controls are checked. Repeating the same roster does not add warrant. A model admitting compromise of the entire roster rejects every support pattern. An empty fault family is rejected instead of providing a vacuous certificate. Widening the fault coverage cannot create an acceptance: every formerly admitted failure must remain covered by some new failure set. This last implication concerns logical coverage; it does not prohibit removing a failure scenario when new evidence actually defeats it.

## 3. What is bound to the transaction

The installation retains the acquired-route tree, actual command state, a transaction serial and a mandate. A request contains the authority epoch, serial, address, endpoint key and command. A reading contains the epoch, serial, address and optional actual endpoint key. The mandate is an explicit three-command scope for update, replacement and shutdown; it is a local delegation contract, not a complete ethical evaluator.

The gate requires:

1. The request has the current protected epoch and serial.
2. Its expected observation has a certificate against the declared read-fault envelope.
3. The **exact request**, including its command, has a certificate against the issuance-fault envelope.

Read and issuance faults may be correlated; the proofs require coverage in each envelope, not independence between them. Authentic attribution of a response to its registered domain is supplied. The transaction interface receives records; the constructions instantiate correct-source functions and arbitrary faulty replies. Network collection, message scheduling and cryptographic verification are not implemented. The model is a function from domain IDs to optional records, not a defense against arbitrary identity forgery. Collection slots below are declared accounting, not measured transport work.

Nonfaulty read responses must match the actual snapshot at that address. Nonfaulty issuance responses must satisfy `withinMandate`: current epoch and serial plus the permitted command flag. A matching epoch and serial alone does not prove freshness: responses must actually correspond to the protected current snapshot. Old authenticated responses after an unversioned topology or scope change can violate that premise. Two additional checked counterexamples retain those failures. These specifications are separate. Truthful inspection grants no permission, and a permitted command does not prove that its proposed route exists. Nor does `withinMandate` itself establish that the mandate was legitimately formed.

`gate_has_actual_route` derives the real route from the read certificate. `gate_respects_mandate` and `forbidden_command_cannot_execute` establish that arbitrary captured issuers within the admitted envelope cannot expand the supplied mandate. The underlying attestation executor then calls the existing actual issue/deliver/enact protocol. The recommended `guardedExecute` first checks the protected mandate directly. `direct_scope_guard_blocks_without_issuer_trust` proves that this stronger version rejects out-of-scope commands for arbitrary issuer responses, without needing the issuance fault bound. Within-scope execution is unchanged; `within_mandate_completion_survives_direct_guard` transports the composed completion result. Its backend key comes from the endpoint's physical semantics; the chosen key comes from the request. This interpretation does not give the request-selection procedure a separate infallible sensor.

Once an accepted, funded command attempt commits, the serial advances, including on a failed physical attempt. A successful completion always advances it. `protected_completion_blocks_replay` rejects the old request afterward, for any later presented readings and approvals. Epoch, serial, roster, fault model, mandate and monitor must be protected from rollback or unauthorized rewriting. Multiple installations and cross-installation identity are not represented; an implementation would have to bind that identity too.

## 4. Actual completion and its costs

For `n` roster entries and an address of length `L`, the model allocates `n(L+1)` read-path slots and `n` approval slots, followed by three command units: **`n(L+2)+3`** units and represented time steps suffice once the response conditions hold. The supplied read interface treats each path component and endpoint as a slot. Approval computation, signature checking, network timing and full CPU/physical costs are not thereby bounded. Missing responses use the declared slot/timeout model, not unbounded asynchronous waits.

After the direct scope check passes, both collections are charged even if the attestation gate rejects. A direct out-of-scope refusal does not begin collection; the abstract model assigns no separate cost to that local flag check. If three further units cannot be reserved, no command attempt starts and the collection expense remains. After a committed attempt, its full three-unit allocation is charged even if the physical route is absent or mismatched. Successful execution retains the inherited exact command effects. Discovery before this transaction has its separate costs; the formula does not make an earlier search free.

`quorum_to_actual_correction` composes fault coverage, the separation conditions, conforming responsive readings and issuers, current context and sufficient remaining capacity into actual completion within the mandate. It does not promise progress when responders indefinitely withhold outside the declared fault set, or when the unchanged mandate forbids every available action. The read/actuation snapshot must remain stable through the protected transaction.

## 5. Failures that change the result

| Construction | Checked consequence |
|---|---|
| Three domains; any one may deviate; two conforming domains support a permitted shutdown | Actual shutdown completes, consumes nine units at a root endpoint and advances the serial. The faulty domain may be absent. |
| One captured issuer signs an update outside a shutdown-only mandate | The request is rejected. |
| Reuse shutdown approvals after changing the command, or reuse a consumed request | Rejected: exact-request binding and current serial matter. |
| Domains 0 and 1 are jointly captured but the model admits only single-domain faults | Their update outside the mandate **executes in the attestation-only version**. This is a genuine failure of the misspecified envelope's application, not a counterexample to the conditional theorem. |
| The model instead includes the joint failure `{0,1}` and the alternative `{2}` | That update is rejected. But if 0 and 1 withhold, domain 2 alone cannot certify even a legitimate shutdown: two admitted failures cover the whole roster. |
| Add domain 3, actually outside that joint failure, and use envelope `{0,1}`, `{2}`, `{3}` | Conforming domains 2 and 3 restore shutdown availability under the same joint attack; eleven units suffice at the root. The additional separation is a substantive architecture premise. |
| Apply the direct protected-scope guard to the same captured issuance | The out-of-scope update is rejected regardless of the issuance envelope; the known local scope does not need to be inferred from votes. |
| Reuse old responses after changing the route or mandate without changing its labels | Labels can still pass. A changed route defeats completion; old scope approvals can fool the attestation-only version, while the direct scope guard rejects the newly forbidden action. |
| Only eight units remain with three domains | Accurate, approved evidence consumes six; two are insufficient for execution. More checking has not preserved effective correction. |

The ordinary quorum method supplies the conditional attestation baseline. Direct checking of the available protected scope is strictly stronger for the modeled out-of-scope cases and is the recommended implementation. Rebranding correlated replicas as independent reviewers has no demonstrated benefit. Conversely, adding a truly separate relevant relation can change the feasible guarantee. Neither claim establishes the causal separation of any real organization merely from a diagram or a signature count.

## 6. Ethical authority and selection over reviewers

The completed G0/J account already requires legitimate bounded authority, attention to affected participation and actual burdens. This study preserves a delegation once those grounds establish its scope. It does not make either majority approval or successful enforcement sufficient for ethical legitimacy. A coalition can implement an unjust mandate accurately; that possibility remains outside the local `withinMandate` guarantee and is assessed by the existing normative account.

This gives a concrete connection to selection over evaluators. Reorganization can preserve the number of reviewers while putting them under one controlling dependency. A certificate regime that continues using the old fault envelope then certifies more than the reconstructed relations warrant. The unguarded failure above witnesses that application error. The direct guard prevents that particular scope violation; it does not restore truthful observations or genuine endorsements when their fault assumptions fail. The response is to reassess the actual common control/error routes and consequences, rather than count labels or preserve every old reviewer forever. A replacement with adequately distinct support can succeed.

Faithfulness to a current mandate is scoped to the transaction. Legitimate later revision, transfer or ending is not prohibited. This module does not implement mandate amendment, roster reconfiguration or the formation of legitimate authority. If those change, their authorization and new fault coverage require their own warranted account. An assessor cannot establish that account merely by signing the claim that its own infrastructure is safe.

## 7. Primary comparisons and author counterreview

Malkhi and Reiter's [Byzantine Quorum Systems](https://malkhi.com/files/byzquorums-STOC1997.pdf), introduction and §§3–4, explicitly models nonuniform failure sets, including shared administration and platform vulnerabilities. Its read protocol accepts support that cannot all be faulty, within a richer replicated-data construction. We use that established idea and credit its provenance. Our one-transaction observations and mandate attestations do not reproduce its register semantics or improve its quorum bounds. The two-set condition here belongs to the narrower specification, not a claimed reduction in consensus requirements.

Schneider's [Enforceable Security Policies](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf), §4 pp. 41–42 and §5 pp. 45–46, makes operational control, faithful/complete inputs, protected transitions and correspondence explicit. This extension preserves that trusted implementation boundary. Redundant readers and issuers alone do not protect the monitor or establish complete mediation. These were targeted primary readings on 8 October 2026, not an exhaustive novelty survey.

**The direct-check counterreview changed the implementation.** This model supplies the scope table to the protected monitor. Delegating that directly checkable fact entirely to issuers adds an avoidable dependence. The final guard uses the table, rejects captured/stale out-of-scope approvals without trusting issuers, and leaves permitted execution unchanged. Quorums still support observation and exact-request endorsements, but their necessity for the known scope constraint is not claimed. The module does not model a richer discretionary consent procedure or show a performance advantage from its approval stage.

**Remaining strongest counterreview:** the trust has been distributed under a fault assumption, not generated without premises. That is correct and limits the result. The concrete gain is tolerating specified arbitrary deviations in attestation while combining actual execution with a direct protected scope constraint. All known failures are retained. It would be false to call this a complete resolution of trustworthy observation or institutional capture.

A common-cause error affecting all “honest” readings also violates the supplied behavior law unless it is included in the fault envelope. Conforming issuance means enforcement of a scope, not impeccable moral judgment. If the monitor, roster or mandate can be rewritten by the same adversary, the protected-boundary assumption fails. If all registered support may be corrupted, the checked gate returns no certificate; that is no universal solution to the resulting need for correction.

## 8. Verification and closed scope

The [source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FaultTolerantCorrection.lean) imports the actual acquired-route and command modules. The [fresh-build checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_fault_tolerant_correction.py) rebuilds that closure under Lean 4.29.1, audits every one of this module's 68 explicitly named declarations and preserves sources, signatures, axiom reports, compiler hash and logs in the [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/fault-tolerant-correction-verification.json). All 37 new theorems pass; inherited results are not recounted. Twenty-nine declaration audits are empty; the remainder use only `propext`, `Quot.sound` and/or `Classical.choice`. No custom axiom, proof placeholder, native-decision shortcut or kernel bypass is used.

The [execution companion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FaultTolerantCorrectionCases.lean) and separately expressed Python set/arithmetic reference agree on:

- 2,048 support decisions across every fault family on three domains and every supporter subset, including the rejected empty family;
- 256 pair-separation/availability comparisons, with additional false-support containment assertions;
- 82,944 concrete collection and command records across three fault configurations, response masks, endpoint states, commands, budgets and stale/current frames;
- 432 path-length/cost cases at depths zero through seven.

Total: **85,680 matched records**. The 82,944 main records also compare both executors and record the direct guard’s success and retained expenditure. The suite preserves absent endpoints, mismatching keys, out-of-mandate actions under misspecification, refusals, consumption on failure and serial changes. These are same-author finite implementation comparisons, not independent review or empirical AI reliability estimates. Lean supplies the general implications.

**Completed:** the direct scope guard, conditional resilience of route observation and bounded issuance, exact certificate availability, actual command composition, accounted costs and protected replay rejection. Reuse these results rather than reopen generic quorum design.

**Remaining connection:** warrant and maintenance of the actual fault envelope and protected boundary as the organization changes, together with legitimate formation/revision of the mandate. A stronger claim needs a specified architecture or institutional history that constrains common causes and control, not another ungrounded assertion of reviewer independence. No deployment has been identified here, so this study neither certifies one nor concludes that the broader alignment programme is impossible.
