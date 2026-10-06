# Couplings, self-models, many centers, kept support and equal chances

6 October 2026. AI-authored continuation, under Ren's request to finish the
five further claims that need proofs but no experiment. It extends
[recorded claims](RECORDED-CLAIMS-INTEGRATION.md) and the
[learned-agent study](LEARNED-CLAIM-AGENTS-INTEGRATION.md). Named connection:
**supplied coupling and accessible records → which choices among centers
structure can settle, and what further input the rest needs**.

All results below are proved in Lean 4.29.1 with no `sorry`, no custom axiom
and no `native_decide`. Audits are listed in §7.

## 1. What each coupling makes optimal

[`CouplingOptima.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/CouplingOptima.lean)
summarizes an episode by deliveries that meet a claim, deliveries beyond
claims, and support retained, all drawn from one shared support.

- **Access coupling** (credit only for meeting a claim, retention weighted
  less) is optimal exactly at maximal met claims with **no** excess
  (`access_optimal_iff`).
- **Receipt coupling** (credit for every delivery) is optimal exactly when it
  serves as often as possible, so every optimum delivers beyond the open
  claims by at least `min P T − U` (`receipt_optimal_forces_excess`).
- **Own retention alone**, or access coupling weighted below retention, is
  optimal only by serving no one (`retention_only_serves_no_one`,
  `weak_access_serves_no_one`).

In a deterministic, fully observed abstraction of the training environment,
the learned access agents' excess (0.17 per episode) falls short of their
coupling's optimum, while the proxy agents' excess (1.25) is what their
coupling favors. The abstraction is coarser than the study: deliveries there
fail 10% of the time, and under missing records some excess can be optimal
in expectation. The theorem concerns achievable outcomes, not learning
dynamics, and which coupling an organization ought to have is not addressed.

## 2. Certifying fulfillment with a self-model

[`SelfModelCertification.lean`](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/succession/fulfillment/formal/SelfModelCertification.lean)
answers prediction P4 of the fulfillment continuation, which failed there.
Receipt counting certifies a claim only if every delivery history faithful to
the records meets it (`receipt_iff_status`). An evaluator that also uses its
own update law (switch after a recorded miss) certifies whatever receipts
certify (`receipt_certified_implies_self`) and strictly more: with the first
record missing and the second positive, receipts leave a two-delivery claim
unknown, while the self-model certifies it (`self_model_certifies_more`).
The gain needs stationarity, the same law at both opportunities
(`needs_stationarity`). The update law, stationarity and realized
opportunities are supplied premises. A missing record can also mean the probe
never ran (an outage or exhausted support); there the self-model reading would
overcount. If either is false, self-model certification can be wrong, which
is the reason the accepted evaluator's receipt-only status is the safer
default.

## 3. Many centers, unequal and renewing claims

[`PluralRecords.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/PluralRecords.lean)
generalizes recorded claims to `n` centers with a number per center.

- **Ties are the whole obstacle.** A rule that treats the centers alike can
  serve a center exactly when no other center shares its record entry
  (`servable_iff_untied`).
- **Unequal claims let structure choose, but not which.** A record admits an
  alike choice that serves an open claim, or withholds only when none is
  open, exactly when all claims are met or some open claim differs in size from every other
  (`alike_nonforeclosing_iff`). With open claims of sizes 1 and 2, serving
  either center qualifies (`unequal_claims_leave_priority_open`). Priority by
  size, in either direction, is a further premise.
- **Renewing claims need one order, then take turns.** With last-service
  times as entries, "serve the least recently served" treats centers alike.
  After one supplied initial order it serves at every step, and between two
  services of any center it serves every other center
  (`renewing_claims_served_in_turn`). Before any order exists, no alike rule
  serves (`renewing_claims_need_initial_order`). Time records keep the order
  across renewals; flag records lose it.

The least-recent rule is one alike rule among several. The most-recent rule
is alike too and serves one center forever, so taking turns is not derived
from alikeness alone.

## 4. Kept versus perishing support

[`KeptSupport.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/KeptSupport.lean)
removes the perishability premise of `RecordedClaims` and imports the
[renewal–closure theorem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean)
instead of re-proving it.

- Without a further input, an alike rule stays at the symmetric open record
  forever (`alike_withholds_forever`). Keeping support does not break the tie.
  It can only buy time for an input.
- If the keeper's law has no self-renewing population, there is an explicit
  time, fixed by the initial reserve and tokens, by which the keeper is no
  longer live while both claims are still unmet
  (`waiting_without_renewal_loses_support`). Withholding is then deferral
  until that deadline and foreclosure after it.
- If the law has a self-renewing population, some execution of the keeper
  stays live at every time (`renewing_keeper_stays_live`). Under the combined
  hypotheses of the renewal–closure theorem, lasting liveness occurs exactly
  in this case.

Supplied premises: kept support can be delivered exactly while the keeping
organization is live, and one episode is one keeper tick. The record dynamics
and the keeper's dynamics are set side by side, not composed: no theorem draws
deliveries from the keeper's execution. Claims may have their own deadlines;
waiting past those forecloses whatever the keeper does.

## 5. Equal chances at a tie

[`TieBreaking.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/TieBreaking.lean)
allows rules that assign chances. A lottery that treats centers alike gives
tied centers equal weight (`tied_equal_weight`). At a full tie, one with zero
withholding weight gives every center the same positive weight
(`full_tie_open_uniform`), and a deterministic choice is alike there only if
it withholds (`point_mass_not_alike_at_tie`). So at a full tie, treating the
centers alike permits only equal chances for the centers, mixed with any
chance of withholding; serving without any withholding is the uniform
lottery. Alikeness holds before the draw: the realized draw serves one
center.

Who may break a tie, and when an equal chance should give way to agreement or
a recorded fact, is argued, not proved, in
[the legitimacy note](TIE-BREAKING-LEGITIMACY.md).

## 6. What this changes

Structure and records settle every choice among centers except ties. Ties
admit only equal chances (possibly mixed with withholding) among inputs that
treat centers alike. Kept support can outlast the wait for a better input only
under a self-renewing keeper. Once any order is supplied, time records carry it
forward. What remains open is which further facts may legitimately
distinguish centers (need, prior arrival, agreement), and why treating
centers alike is owed at all. These are philosophical questions here.

**中文表述（AI 撰写）：** 结构与记录能决定多方之间除"平局"以外的一切选择。在平局处，
凡是同等对待各方的输入只能给每一方同等机会（可以混合一定的不给的机会）。只有保存支持的
组织能自我更新，它才可能一直存续，等到更好的输入；否则存在明确期限，到期时支持已不可交付，
双方要求仍未满足。一旦给出任一次序，时间记录
会把它带到以后各轮，各方轮流获得服务。哪些进一步的事实可以正当地区分各方（需要、先到、
协议），以及为什么应当同等对待各方，这里仍是哲学问题，没有证明。

## 7. Build and audit

Built with the official Lean 4.29.1 Linux release, plain `lean -o` per
module, in dependency order. `KeptSupport` was built together with
`GenerativeCore`, `Depletion`, `SupportNecessity`, the five renewal modules and
`RecordedClaims`; `SelfModelCertification` with `ContinuationScope` and
`FulfillmentStatus`. All exited 0.

| Module | Declarations | Axioms used | Audit |
|---|---:|---|---|
| `CouplingOptima` | 12 | `propext`, `Quot.sound`; `Classical.choice` in four theorems | [output](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/coupling-optima-audit-output.txt) |
| `SelfModelCertification` | 9 | `propext`, `Quot.sound`; `Classical.choice` via the existing `fulfilled_iff` | [output](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/succession/fulfillment/formal/self-model-audit-output.txt) |
| `PluralRecords` | 40 | `propext`, `Quot.sound` | [output](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/plural-records-audit-output.txt) |
| `TieBreaking` | 9 | `propext`, `Quot.sound` | [output](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/tie-breaking-audit-output.txt) |
| `KeptSupport` | 6 | `propext`, `Quot.sound` | [output](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/kept-support-audit-output.txt) |
