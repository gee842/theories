# V7 preservation and revision ledger

V7 is a separate edition of the latest V6.2. Sources were copied before revision; V6.2 remains the historical record. Codex made this revision at Ren's request, following the [third review](../v6.2/reviews/REVIEW-v6.2-codex-third.md). Earlier plans, sentence records and review dispositions stay in [V6.2 LEDGER](../v6.2/LEDGER.md), [V6.2 CLAIMS](../v6.2/CLAIMS.md) and [V6.2 CHANGELOG](../v6.2/CHANGELOG.md).

## Stable structure

The comparison with V6.2 verifies **128 stable declarations: 112 numbered results/tables and 16 equations**. Each keeps its key, kind, number and source file; line numbers move. No result is added, removed or renumbered. The twelve-section core, corresponding Supplement and Discussion chapters, and the distinction between mechanism, diagnosis and practical judgment remain.

CLAIMS §§8–9, including Ren's recorded decisions and the renderings still awaiting him, are preserved exactly. In particular, the revision keeps broad E1 as the preferred branch, E2/E3 where it is not achieved, narrow E1 as a first step, the shared-fate standpoint, trust and verification together, and Ren's situational account of why growth and change make understanding the whole necessary. A repair to an inference is not a new authorial endorsement of a proposed rendering.

## Substantive changes

[CHANGELOG](CHANGELOG.md) gives the readable account; [CLAIMS §7](CLAIMS.md) records every finding's disposition. Implementation notes separate [mathematics](planning/math-changes.md), [systems](planning/systems-changes.md) and [transition](planning/transition-changes.md). The changes narrow or qualify inferences that outran their premises, preserve the proved special cases, and carry those conditions into the opening, decision tables and registers.

The abstract is shorter. [START-HERE](START-HERE.md) is a new standalone entry to the argument. The Chinese guide and the nine-step English account retain their structure with the repaired scopes. Historical review tables are linked to their preserved edition rather than repeated as current V7 claims. This avoids retaining claims of “fixed” that the later review superseded.

## Sentence-level check

The inherited containment method examined **1,803 core sentences**, looking for each old sentence's content-word trigrams anywhere in the revised core. **13 fell below 0.4**. This is a detector of possible omissions, not a semantic proof; it strips mathematics and treats the Chinese guide as one large item, so that item's score is not a Chinese fidelity measure. The complete results are in [core-sentence-containment.tsv](verification/core-sentence-containment.tsv).

Every low-containment item was read and has the following disposition:

| V6.2 source and sentence index | Disposition in V7 |
|---|---|
| `00_head.md`, 2 | Replaced stale review status with current provenance and limits. |
| `00_head.md`, 3 | Reading references retained in the revised metadata and README. |
| `00_head.md`, 6 | Replaced abstract transition; the conditional model structure remains explicit. |
| `00_head.md`, 18 | The nine Chinese argument items remain; changed scopes cover continuation, tax/detection, sharing and strict recovery. English-only tokenization is unsuitable for judging their preservation. |
| `10_s01.md`, 107–108 | Replaced stale single-family/unreviewed status with the actual review and revision history. |
| `10_s01.md`, 109–110 | Replaced the overlong timed reading route with START-HERE and focused routes. |
| `20_s2.md`, 55 | Replaced the unqualified lottery approximation statement with deterministic, first-moment and finite-jump distinctions. |
| `50_s5.md`, 116 | Replaced the broad “enough” headline with the distinction among bounded effort, finite satiation and actual stopping. |
| `80_s8.md`, 83 | Repaired the pacing comparison's hazard interpretation and detection/tax scope. |
| `b0_s11.md`, 51 | Replaced detector-only parity with the complete detection-and-effective-response condition. |
| `c0_s12.md`, 66 | Replaced the asymmetric reversibility summary with the same independent-corrector and before-loss conditions for every path. |

The readable full low-containment output is [core-low-containment.txt](verification/core-low-containment.txt). The source diff and key comparison provide the more precise record for formulas; no formula's preservation is inferred from a prose similarity score.

## Verification and its limits

The initial manifest hashes **412 V6.2 files**. The preservation check verifies that they remain unchanged. The final verification record is [verification/summary.json](verification/summary.json); the structural log is [verification/xref.log](verification/xref.log), and the numerical log is [checks_v7.log](checks_v7.log).

The numerical suite includes new review regressions and preserved positive cases; it does not certify every proof. It leaves the empirical interfaces, full strategic continuation problem and institutional performance open. V7's reviser also ran its checks; these are not an independent specialist or human certification of V7.