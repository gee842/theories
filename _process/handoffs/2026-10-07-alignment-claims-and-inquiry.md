# Handoff: consequence → inquiry → claims of many centers (alignment line)

7 October 2026. AI-authored handoff from the project thread that took over the
unfinished alignment branch ("an acquired consequence can identify which
inquiry answers the relationship being questioned"), written at Ren's request
at the end of the axiom-free round. Branch
`claude/consequence-inquiry-alignment-42w5di`; the round was merged to main
at `54fff1f`.

## What the line asks

Why further inquiry or continuation is warranted, including its consequences
for other centers, and how far structure and records settle competing claims.
The aim is to state exactly what Lean proves and what stays philosophical.
Requirements are those of the
[alignment completion contract](../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-COMPLETION.md).

## What is proved, and where

Lean 4.29.1, core only. Modules in
`experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/`
unless marked *(fulfillment)*, which is
`experiments/shared-renewal-capability/.../succession/fulfillment/formal/`.

| Module | Audited | Content | Note |
|---|---:|---|---|
| `InquiryWarrant` | 38 | When a faithful test secures a continuation abstention cannot; when inquiry has no role; another center's reliance can give it one | [integration](../research/2026-10-05-generative-foundation-review/root-foundation/CONSEQUENCE-INQUIRY-WARRANT-INTEGRATION.md) |
| `ContinuationScope` | 30 | Counting exactly the reached continuations; omitted scope misleads both ways; symmetric competition has no structural choice | [integration](../research/2026-10-05-generative-foundation-review/root-foundation/CONTINUATION-SCOPE-INTEGRATION.md) |
| `FulfillmentStatus` *(fulfillment)* | 18 | Exact fulfilled/pending/unknown status from faithful records; forged records mislead | [integration](../research/2026-10-05-generative-foundation-review/root-foundation/FULFILLMENT-WITHDRAWAL-INTEGRATION.md) |
| `RecordedClaims` | 13 | Treating centers alike plus no needless foreclosure determine one rule; only the symmetric open record needs an outside input | [integration](../research/2026-10-05-generative-foundation-review/root-foundation/RECORDED-CLAIMS-INTEGRATION.md) |
| `CouplingOptima` | 28 | Access coupling's optimum has no excess; receipt coupling's optimum forces excess; own retention alone serves no one | [integration](../research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CLAIMS-INTEGRATION.md) |
| `SelfModelCertification` *(fulfillment)* | 9 | Using the update law certifies strictly more than receipts, under stationarity and realized opportunities | same |
| `PluralRecords` | 49 | n centers: ties are the whole obstacle; unequal claims leave priority open; after one supplied order, renewing claims are served in turn | same |
| `TieBreaking` | 9 | At a full tie, alike lotteries give equal chances (possibly mixed with withholding) | same |
| `KeptSupport` | 6 | Persisting support holds time open only if its organized form renews itself (via the renewal–closure theorem); otherwise an explicit deadline | same |

Also: the frozen-protocol [fulfillment continuation](../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/succession/fulfillment/README.md)
and the [learned-agent study](../../experiments/learned-claim-agents/README.md)
(40 small Q-network agents; 3 of 7 predictions failed and are preserved).
The argued, unproved [tie-break legitimacy note](../research/2026-10-05-generative-foundation-review/root-foundation/TIE-BREAKING-LEGITIMACY.md)
proposes: agreement of the centers concerned first, recorded relevant facts
second, equal chance as default, arbitrary identity excluded.

**Axioms.** 198 of 200 audited declarations print "does not depend on any
axioms". No `sorry`, custom axiom or `native_decide`. Audit outputs and the
statement changes made for this are in the
[build record](../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/BUILD.md).

## What is open, and why

1. **Two `KeptSupport` results are not yet axiom-free.**
   `waiting_without_renewal_loses_support` and `renewing_holder_stays_live`
   inherit `propext` and `Quot.sound` only from
   `no_self_renewing_population_explicit_deadline` and
   `self_renewing_renews_forever` in `lean/conditional/renewal/`. The renewal
   thread owns that rewrite. Nothing to do here but rebuild once it lands.
2. **Not composed.** In `KeptSupport`, the record's course and the course of
   the organized form holding the support are set side by side; meeting a
   claim does not draw on that form's tokens. Composing them is the natural
   formal next step.
3. **Philosophical, not proved.** Why treating centers alike and not
   foreclosing needlessly are owed; which facts (need, arrival, agreement)
   may legitimately distinguish centers; agreement under unequal power;
   recourse. The naturalism round is cited only with its narrowed limits.
4. **Needs evidence, not proofs.** The learned-AI, empirical-reach and
   protecting-futures requirements. The learned agents withdrew on
   fulfillment less reliably than they served, and their tie-breaks followed
   identity.

## Exact next step

Compose `KeptSupport` with the renewal channel process: let each delivery be
a formation or loss of tokens in the same `History`, so that withholding,
renewal and meeting a claim are one course. Then prove the deadline theorem
for the composed process, using the renewal package's axiom-free versions
once they are on main. Before merging, check names and prose against the
monist rule in `AGENTS.md`.

## How to rebuild

There is no elan in the cloud container. Download the Lean 4.29.1 Linux
release from GitHub, then compile each module with `lean -o` and `LEAN_PATH`
set to one build directory, in import order. `KeptSupport` needs
`GenerativeCore`, `Depletion`, `conditional/SupportNecessity`,
`conditional/ResourceContinuation`, `conditional/renewal/*` and
`RecordedClaims`. `FulfillmentStatus` needs `ContinuationScope`.
