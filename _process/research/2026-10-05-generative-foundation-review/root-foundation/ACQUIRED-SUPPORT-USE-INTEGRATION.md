# 取得读数与实际使用 / Acquired readings and actual use

2026-10-08，Asia/Bangkok。Ren 的本次“继续”见[来源](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md)。本轮形式化、整合、来源比较及作者反审为 AI 工作。[当前理论第12节](../../../../theories/becoming/chapters/GENERATED-LOGIC.md#acquired-support-use)。

**完成连接：实际读取留下的记录，在明确的逐位置版本维护和原子核对／使用条件下，支持原生取得规则；任意有限执行都可投影为前轮同一占用过程的合法历史。** 无关位置可以变化；相关变化使记录失效。正确拒绝旧记录仍可能耗尽全部读取预算。

**Completed bridge:** coherent acquisition → a maintained ticket invariant → validated use → the existing native acquisition law, with exact accounting and explicit interference controls. Twenty-eight new Lean theorems pass. This is a checked composition of established mechanisms, not a new concurrency logic or a derivation of trustworthy sensing from no premises.

## 1. Credit completed work and specify the remaining connection

The [previous logic study](RECONFIGURABLE-LOGIC-INTEGRATION.md) proves the exact occupancy distinctions needed for future permitted access. Its `refreshed_view` accepts a current bit; it does not obtain that bit. The present study connects obtained information to execution in that same `ReconfigurableSupportLogic` process, rather than introducing another unrelated success predicate.

The repository already has the following completed results. Their historical “next” wording is not a reason to repeat them:

| Existing work read | Result reused | What this continuation adds |
|---|---|---|
| [Correction handoff](CORRECTION-HANDOFF-INTEGRATION.md), 23 new theorems / 45 audits | Probe versions, guarded change, stale readings and bypass controls | A direct refinement into the prior logic study's native occupancy law, rather than a new generic stale-read claim |
| [Correction frontier boundary](CORRECTION-FRONTIER-BOUNDARY.md), 34 new theorems / 58 audits | Protection intervals, limitations of preflight tests, and faithful observation / full mediation premises | Per-slot validation allowing an unrelated slot to change, plus an exact paid retry history in this process |
| [Evidence-qualified correction](EVIDENCE-QUALIFIED-CORRECTION-INTEGRATION.md), 24 new theorems / 47 audits | Costed inspection and actual completion under stated evidence correspondence | A common trace proof that keeps read costs while projecting validated use to native access |

These studies are credited conceptually. They are not imported into the new Lean build or claimed to have a formally proved translation to it. The new closure imports `ReconfigurableSupportLogic` and `GenerativeCore` only. This supplies an implementation condition for valid descriptions of joint realization; it does not infer ethical authority, a duty to acquire, or actual motivation. The separately authorized G0/J and universal-grounding investigations retain their scope.

## 2. One process, with explicit observation and accounting coordinates

The previous configuration has a current route and a Boolean occupancy function. The extended configuration also records a natural-number revision at each slot, an optional ticket, and a remaining acquisition/use budget. These are coordinates of one changing organization, not independent subject and environment domains. The projection preserves the native route/occupancy effects and omits bookkeeping events; its theorem expressly limits that omission. It is not an identity between every physical aspect of the two descriptions.

Every admitted native `take` or `release r` increments the affected slot's revision. Redirecting changes the route but no revision. A primitive coherent read obtains `(current slot, its revision, its occupancy)` together. A ticket is `Valid` when its revision is no greater than the present revision and equality implies that its recorded occupancy agrees with the present value. An old ticket can remain valid in this conditional sense without being current or usable.

| Extended action | Guard and effect | Charge to the stated budget |
|---|---|---|
| `change e` | Prior native guard; perform that native event and maintain affected revisions | 0 |
| `read` | Current route permitted, positive budget; store its coherent sample | 1 |
| `use` | Route permitted, positive budget, stored ticket names the current route, matching revision, recorded free value; acquire and clear the ticket | 1 |
| `reject` | A stored ticket fails the admission check; clear it | 0 |

The use guard **does not additionally query actual occupancy**. `admitted_is_free` derives that fact from the preserved invariant and the recorded checks; `use_is_native` then derives the prior native step. Thus the substantive projection does not merely repeat the old guard as an extra premise of every use.

The unit charges are supplied accounting conventions for this allocated budget. Native changes and rejection cost zero in this account, not zero physical work. We do not derive energy, real time, fairness, replenishment, or the optimal policy. Permission `K`, support identities, coherent reads and atomic validation together with use remain supplied. Natural revisions do not wrap; no reclamation, address reuse, forged records or untracked writers are admitted. The previous release law still lacks ownership authentication.

中文要点：记录的来历与保持关系、当前位置、版本一致、读得空闲、还有执行预算，是不同条件。它们全都需要各自对应；“有一条正确的旧信息”不能省去后四项。版本的自然数模型明确排除回绕，不能直接冒充有限硬件计数器。

## 3. Checked correspondence and positive use

Write `Sound(s)` for validity of every stored ticket. An initially empty ticket satisfies it directly. Reads establish it; every admitted action preserves it. Let `nativeWord` keep `change e` as `e`, translate `use` to `take`, and erase `read` and `reject` from the physical event list.

For any finite extended history from a sound initial state, `trace_projects` proves a history of the old native process between the projected endpoints with exactly that translated event word. The theorem is one-way: it does not claim that every native history can be realized under an arbitrary reading budget. `trace_budget` separately proves

\[
\text{final budget}+\text{number of reads and uses}=\text{initial budget}.
\]

Erasing bookkeeping from the native projection therefore does not erase its charge from the extended account. For the immediately consecutive word `[read, use]`, `fresh_read_use_iff` proves feasibility **iff** the current route is permitted, currently free, and the initial budget is at least two. Intervening actions are excluded by that specified word, not assumed harmless.

| Claim | Checked declarations | Scope |
|---|---|---|
| A read produces a valid ticket; revisions preserve validity | `sample_valid`, `update_valid`, `next_sound`, `trace_sound` | Conditional accuracy is maintained; an invalidated ticket need not remain current |
| Admitted use meets native occupancy conditions | `admitted_is_free`, `use_is_native` | Requires `Sound`; the guard's version comparison and use are one atomic transition |
| Every extended history projects to a legal native history | `step_projects`, `trace_projects` | Arbitrary finite action words; no converse implementation theorem |
| Exact budget balance and quiet read/use condition | `step_budget`, `trace_budget`, `budget_necessary`, `fresh_read_use`, `fresh_read_use_iff` | This unit-charge account; no real-time estimate |
| Unrelated release preserves admission | `unrelated_release_admits`, `unrelated_change_then_use` | The released slot differs from the ticket's slot; a concrete legal three-step witness is included |

The positive two-slot witness starts with the current slot free and a different slot occupied. It reads the current slot, releases the other one, then successfully uses the record. Thus the proof does not require freezing the entire configuration. Related occupancy updates remain mediated by revisions.

## 4. Interference, conservative rejection and exact retry cost

The checked controls distinguish failures that a loose “trusted observation” premise could conceal:

- `stale_read_rejected`: after the read, a native acquisition occupies that slot and increments its revision; use is no longer enabled.
- `restored_value_still_rejected`: a subsequent native release restores the free value, but the old ticket is still rejected. Matching current truth is weaker than this protocol's freshness condition. The protocol is safe but deliberately conservative; validation is not proved necessary for every safe implementation.
- `wrong_route_rejected`: redirection to a different slot prevents using a ticket for the old route, even when revision numbers happen to agree.
- `bypass_breaks_correspondence`: changing occupancy without maintaining revisions creates a state whose operational use guard passes although the native take is disabled. That state violates `Sound` and lies outside the admitted transition law. This tests the full-mediation premise; it is not a counterexample to the law's proven invariant.

There is also a native interfering cycle: read a free slot; another admitted `change take` occupies it; `change release` restores it; reject the old ticket. This spends one read unit and returns to an empty-ticket, free-slot configuration with revision increased by two.

For exactly `n` repetitions of that cycle followed by the quiet word `[read, use]`, `retries_then_use_iff` proves

\[
\text{the specified history is feasible}\quad\Longleftrightarrow\quad n+2\leq B.
\]

`finite_budget_can_be_exhausted` gives, for every natural budget `B`, the history of `B` such cycles ending free but with zero budget and neither read nor use enabled. This is a constructive possibility for each finite budget, not a claim that every scheduler behaves that way. No stochastic lower bound, optimal retry theorem or inevitable starvation result is inferred.

The extended process still permits `change take` under the native guard, even at zero reading budget. It represents admitted native activity without attributing ownership or charging this ticket path. Thus the exhaustion theorem blocks further `read` and ticket-backed `use`, not all acquisitions or every possible route to an occupancy goal. The cost lower bound belongs to the specified word, not unrestricted native reachability.

中文结论：版本核对把“不能错用”接到了实际取得；它不独自给出“总能完成”。本轮给出的失败历史每次都恢复了支承，耗尽的是反复取得证据的预算。若要证明完成，必须另给有效的干扰限制、保护安排或可持续预算，并在同一执行规则中兑现。

## 5. Primary-source comparison and frontier assessment

Primary sources inspected on 8 October 2026:

- Kung and Robinson, *On Optimistic Methods for Concurrency Control* (1981), [author-hosted paper](https://www.eecs.harvard.edu/~htk/publication/1981-tods-kung-robinson.pdf), pp. 215, 219–222: read/validation/write phases, restarting and starvation, and an indivisible final validation/write interval already address these core issues. Our per-slot model is not a new optimistic concurrency method; no equivalence or superiority to the paper's serializability protocol was proved.
- Linux, [Sequence counters and sequential locks](https://cdn.kernel.org/doc/html/latest/locking/seqlock.html), introductory reader-retry and writer rules: consistency of a copied read requires the stated sequencing conditions. That is a reading contract, not by itself a future-use guarantee. Our code supplies an atomic coherent sample and atomic validate/use; it does not implement a Linux sequence counter or prove a hardware memory model.

**前沿判断：**本轮完成仓库内部的一个真实连接，前沿新颖性没有成立。已有文献与仓库研究已经覆盖版本、冲突、保护及重试。本轮价值是把它们接到前轮的同一原生过程，并使对应、无关变化和代价能够同时检查。继续把这些机制改名或增加相似例子，不会自动形成逻辑学突破。

The original question about derivable logic retains its distinctions: earlier rounds establish conditional object-calculus rules and applicability criteria; this continuation explains how one operational premise can be acquired and used under explicit laws. Neither proves the metatheory from nothing. A claim of frontier advance would need a distinct, precisely specified target beyond the credited results and a like-for-like comparison.

## 6. Substantive author counterreview and remaining bridge

1. **Does adding a perfect read solve sensing?** No. The primitive sample is faithful by definition. The proved contribution begins from that declared correspondence and carries it through interference to native use. A physical reader needs separate evidence.
2. **Is `Sound` an assumption silently reintroduced at each use?** No. It is assumed once for the arbitrary initial session and preserved by all actions; empty-ticket initial states satisfy it. A concrete read supplies the stored evidence. Unmediated changes are explicitly excluded and tested by the bypass control.
3. **Does validation leave an unmodelled check-to-use gap?** The model makes that interval atomic. An implementation that splits it does not inherit this theorem without an additional refinement argument. The older protected-interval study remains the relevant completed precedent.
4. **Does freshness guarantee budget or progress?** No. Route, permission and positive budget remain separate checks. The exact history and exhaustion witness expose the progress limit of the ticket-backed path. Other native acquisition events remain possible; no global impossibility of acquiring the support is claimed.
5. **Are the zero-cost changes free information or activity?** They are zero only against the designated reading/use budget. The theorem supplies no total resource economy. An interference account with its own costs would be a different model.
6. **Does the abstraction erase relevant history?** The physical projection erases read/reject events while the extended account retains their budget effects. No claim about the old process alone recording those costs is made. Projection soundness is not full behavioral equivalence.
7. **Does this derive an axiom or ethical duty from reality alone?** No. It is a conditional rule of correct operational application under supplied process laws and Lean's metatheory. No ethical premise is manufactured by the admission predicate.
8. **Is another toy protocol the next necessary step?** No. This local bridge is complete. Stronger application claims need a specified realization of coherent observation, full writer mediation and atomic validate/use, with actual implementation or experimental evidence. None is supplied by merely repeating the present formal construction.

This is an author counterreview, not independent-agent acceptance. No subagent was requested or used. The remaining correspondence concerns realization of the declared primitive observation and synchronization contract, plus a completion condition if eventual success is the target. These are identified limits of the representation and its application; they do not demonstrate failure of the whole generative theory or establish universal ethical grounding.

## 7. Verification and preservation

[AcquiredSupportUse.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/AcquiredSupportUse.lean) has 15 new theorems, four with empty named-axiom reports. [AcquiredSupportUseCases.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/AcquiredSupportUseCases.lean) has 13, four empty. The other 20 new reports use only `propext` and/or `Quot.sound`; none uses classical choice. The inherited 42 audits remain separate (30 empty). The four-module closure has **70 audits: 38 empty, 32 standard**, no custom postulate or proof hole. “Empty” does not erase parameters, type theory or the substantive correspondence premises.

The [frozen successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/acquired-support-use-checks/20261008T112000.799032Z/receipt.json) binds source bytes, compiler logs and checker to Lean 4.29.1. Earlier failed attempts remain recorded and were not reported as passing; fixes addressed proof elaboration, function equalities and unused simplifier arguments without disabling warnings.

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_acquired_support_use.py
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/ACQUIRED-SUPPORT-USE-CHECK.py
```

The [before-edition manifest](development/acquired-support-use-before/manifest.json) preserves the prior theory, previous study, exact messages and documentary evidence. Previous 38-, 37- and 24-theorem results keep their original frozen receipts and scopes. [Owned integration checks](ACQUIRED-SUPPORT-USE-CHECKS.json) and [index edits](ACQUIRED-SUPPORT-USE-INDEX-EDITS.json) validate this addition without certifying unrelated concurrent reviews or regenerating the separate full-results catalogue. No schedule or unlimited research goal was created.
