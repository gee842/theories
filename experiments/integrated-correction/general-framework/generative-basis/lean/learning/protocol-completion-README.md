# Bounded completion of issued protocols

This additive study strengthens the existing completed-block interface with an explicit progress contract. The source definitions, report decoder, controller and resource laws remain supplied. It does not change any inherited transition law.

**Status:** accepted after a combined fresh build and separate internal AI review. The build passes 34 new theorem audits (13 general, eight paid examples, 13 predictor), including eight with no axiom dependencies, and 244 inherited audits across 15 source modules. Use the [canonical account](../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PROTOCOL-COMPLETION.md) for the accepted scope.

## Source roles

| Source | Contract or application |
|---|---|
| [ProtocolCompletion.lean](ProtocolCompletion.lean) | Command-dependent admitted states, actual next-event availability, preservation and strict internal rank; bounded first return, maximal-attempt and reported-history/account interfaces |
| [ProtocolCompletionExamples.lean](ProtocolCompletionExamples.lean) | Unchanged two-event paid example; refusal, paid deadlock, permitted stalling and depleted returned boundary |
| [PredictionProtocolCompletion.lean](PredictionProtocolCompletion.lean) | Remaining phase guards and retained command of the unchanged deterministic payable predictor trial |

The new contract strengthens [ProtocolComposition.lean](ProtocolComposition.lean); its earlier completed-history correspondence remains valid at its original scope. It does not silently add completion to every client or turn a failed paid prefix into a returned failure report.

For maximal discrete attempts, an unfinished finite endpoint must have no permitted next event. The new contract excludes such endpoints and infinite internal runs, and supplies a nonempty completing path. An external scheduler that stops taking enabled events is not made fair by this result. There is no wall-clock or probability claim.

Finite repetition is proved only under an explicit boundary domain whose members admit their next decoded command and whose actual completed successors remain in that domain. It preserves the returned physical state, reported history and reference memory. This reusable closure supports every finite operation count and is stronger than the horizon-specific conditions sufficient for a single funded finite job. The paid example's depleted returned boundary violates readmission; completing one command does not establish this closure or indefinite renewal. Each declared resource coordinate retains its own actual-prefix account.

The predictor's admitted domain is a finite list of actual remaining enabled-phase conditions. It is not defined by existence of a successful path. Its sharp guard uses the actual deterministic work outcome for later writing affordability; it is not an installed sensor for that future outcome. A separate sufficient admission theorem uses current fuel for rent, work and writing, together with the existing score, packet, lease and maintenance bound; accessible measurement and installed issuance remain additional implementation claims. Returned states need not admit another trial. The separately total stochastic exposure has different failed-write and packet-expiry behavior and retains its own correspondence boundary.

An admission guarantee based on incomplete observations must cover all compatible actual states. Selecting only hidden states where the sharp guard happens to hold is not a physically implemented admission decision.

## Reproduction and audit

From this directory run:

```sh
python3 check_protocol_completion.py
```

[The checker](check_protocol_completion.py) pins Lean 4.29.1, copies the canonical dependency sources into a fresh temporary build, audits each new theorem's dependencies and checks source identity across the build. It permits only the declared standard Lean axioms and rejects admissions, custom axiom declarations and unchecked native decision shortcuts. [The current audit](protocol-completion-audit.json) records exact source/compiler/checker hashes, compiler output and status. A passing build proves the displayed conditional propositions, not their empirical interpretation.

The allowed standard dependencies are `propext`, `Quot.sound` and `Classical.choice`. General completion existence and its corollaries use classical choice; this is declared in their individual audits. No custom axiom or unverified executable decision is used.

The uniquely named [development directory](protocol-completion-development/) preserves earlier attempts, source/checker versions and errors, including a preflight false positive caused by a forbidden-token scan reading an ordinary word in a Lean comment. The corrected scan excludes nested comments; no theorem changed for that correction. The [predictor development directory](prediction-protocol-completion-development/) separately preserves its application proof attempts. No inherited audit receipt is overwritten. Those failed or earlier snapshots are provenance, not separate confirmations of the final theorem.

The [mathematical specification](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-MATH.md), [application boundaries](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-APPLICATIONS.md), [independent internal review](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-REVIEW.md) and [integration](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROTOCOL-COMPLETION-INTEGRATION.md) remain separate from formal compilation. No new empirical experiment is performed.
