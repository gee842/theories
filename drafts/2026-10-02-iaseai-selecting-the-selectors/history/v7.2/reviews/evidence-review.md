# V7.2 evidence, provenance and editorial review

Date: 4 October 2026. Reviewer: fresh bounded Codex agent context. Scope: the supplied integration proposal; source CLAIMS (especially §11), EV19, Test N and §6.5, S13 and S16; opening, §1, §6 and relevant §10 joins; X1 and the four added or expanded prior-art references. README, LEDGER, CHANGELOG and RELEASE-REVIEW were being rebuilt and are not assessed as final. No manuscript was edited by this reviewer.

**Disposition:** no substantive evidence or provenance blocker found in this scope. The new institutional criterion remains an untested research target, and the reduced joint result is consistently conditional. Minor edition and locator defects below should be repaired before assembly and release. This is not an independent human review, a proof certification, or a complete literature/priority audit.

## Findings

### E1 — Minor: current-edition titles and executable references still name V7.1

At the inspected snapshot, `src/disc/01_X1.md:1,3` identifies the Discussion as V7.1 and omits its V7.2 revision. `src/supp/00_S0.md:1,3` does the same for the Supplement, and its overview stops at S15 despite the added S16. `src/reg/TESTS.md:217` also names only V7 and V7.1 as revisions by the later model family. These are current-edition descriptions, unlike the correctly retained historical V7.1 review narratives.

Several current instructions refer to absent local `checks_v71.py` rather than `checks_v72.py`: `src/core/10_s01.md:48`; `src/supp/00_S0.md:3,70,72`; `src/supp/06_S6.md:3,49`; `src/supp/10_S10.md:11,61`; and `src/supp/14_S14.md:148,167`. The numerical claims may be inherited, but the reader is directed to a script that does not exist in this edition. Update current invocation/reference text while retaining genuinely historical statements. Reassemble after repair.

### E2 — Minor: two inherited provenance locators no longer describe the edition correctly

- `src/reg/EVIDENCE.md:3` locates the V7.1 primary-source audit at local `planning/evidence-v71.md`. That file is absent in V7.2 and present at `../v7.1/planning/evidence-v71.md`. Point explicitly to the preserved earlier audit.
- `src/reg/CLAIMS.md:52` says that LEDGER records the V6.2–V7 comparison. The rebuilt current ledger is for V7.1–V7.2. Either name the current comparison or link the historical ledger directly.

Neither defect changes an empirical claim, but both obstruct tracing the review history. The root agent was notified of E1–E2 while this report was being prepared; later repair may supersede these snapshot findings.

## Claim and status consistency

**Conditional composition.** `src/supp/16_S16.md:15–40` states the incoming-field, liability, initial-state, equal-background, fixed-load and constant-speed replicator assumptions, excluding entry and mutation and restricting the host model. `src/reg/CLAIMS.md:179,214,219,350`, `src/supp/13_S13.md:22,26,57`, `src/core/00_head.md:9`, `src/core/10_s01.md:28,50`, and `src/core/a0_s10.md:79` preserve the distinction between this invariant subset and the unresolved implementation of the correction mechanism. The result is not represented as the full correctable kernel, a reachability guarantee, or resilience to arbitrary succession and institutional amendment.

**No institutional experiment claimed.** `src/reg/TESTS.md:132,179–185,197`, `src/reg/CLAIMS.md:351`, and `src/reg/EVIDENCE.md:301,313` explicitly mark Test N proposed and unrun. The S16 numerical trajectories are labelled model checks rather than institutional measurements (`src/supp/16_S16.md:47`).

**Test N can count against the candidate.** The protocol matches total resources and initial performance, permits costly obstruction, coalitions and successors, separates detection/authorization/execution, rejects suppression of legitimate appeals, and recognizes equal baseline performance as evidence against superiority. It expressly treats the held-out research scorer's independence as an experimental boundary. Positive findings remain confined to the registered envelope and do not establish C1. This is a coherent proposed comparison, not a completed preregistration: numerical margins, sample size, exact interventions and operational definitions still need to be specified for an actual study. The paper does not claim otherwise.

**Hazard and design boundaries.** EV19 (`src/reg/EVIDENCE.md:292,299–301`), S13 (`src/supp/13_S13.md:24–26,35–38`), Test N (`src/reg/TESTS.md:185`) and the revised inner-level discussion (`src/core/60_s6.md:105–107`) do not infer a residual-hazard floor or institutional design superiority from corrigibility, failed assurance, a barrier certificate or a local obstruction derivative. The distinction among function preservation, replaceable institutions, legitimate appeal and mere stability is maintained.

## Primary-source checks

All four source pages were retrieved directly on 4 October 2026. The checks support the bounded summaries actually made; none establishes the institutional proposal.

| Source and inspected location | Manuscript position | Assessment |
|---|---|---|
| [Soares et al., *Corrigibility*](https://intelligence.org/files/Corrigibility.pdf), PDF p. 2 §1.1 and p. 3 §2 desiderata | EV19 line 294; §6 line 107; X1 line 134 | The correction-preservation requirement covers self-modification and newly created agents. The paper presents failures and open problems rather than a general solution. Summary supported. EV19's broad “§1 and §1.2” locator could optionally be sharpened to “§1.1 and §2.” |
| [Carey and Everitt, *Human Control: Definitions and Algorithms*](https://proceedings.mlr.press/v216/carey23a.html), proceedings abstract and bibliographic record | EV19 line 295; §6 line 107; X1 line 134 | The abstract explicitly covers shutdown instructability, autonomy, user harm and non-obstruction. Manuscript does not claim these are institution-level guarantees. Summary supported at its declared abstract-only depth. |
| [Frank, *Mutual policing and repression of competition in the evolution of cooperative groups*](https://stevefrank.org/reprints-pdf/95Nature-Police.pdf), pp. 520–522, especially eqs. (2)–(4), Fig. 1 and discussion | EV19 line 296; X1 line 129 | The model jointly treats competitiveness and policing contributions. Its discussion distinguishes abstract theory from a testable empirical prediction. The manuscript correctly treats this as a theoretical predecessor, not AI evidence or a derivation of legitimate authority. |
| [Ames et al., *Control Barrier Function Based Quadratic Programs for Safety Critical Systems*](https://arxiv.org/abs/1609.06408), abstract | EV19 line 297; X1 line 130; S16 line 9 | The abstract supports the description of safety as forward invariance, control-input constraints and combination with performance objectives, including automotive illustrations. This review did not independently verify every condition of the paper's theorems or its journal pagination. The manuscript's institutional interpretation is explicitly its own extrapolation. |

The Frank 1995a/1995b distinction is present in the bibliography generation source and the displayed reference files. Soares and Carey are not made to support a claim of solved corrigibility. X1 (`src/disc/01_X1.md:129–134,158`) expressly inherits selection on regulation, calls the new result a modest composition, and leaves the larger contribution dependent on an implementable, tested arrangement. No priority over the general ideas in these four sources is asserted.

## Historical provenance preservation

The content of CLAIMS §§8–10 matches V7.1 in both the source and assembled registers. Comparison excluded only trailing whitespace separating the inherited ending from appended §11; it did not normalize text, punctuation or internal whitespace. SHA-256 of each extracted and trailing-trimmed historical span:

- Source span, both editions: `6134df4bc958e99107734c15590bca1766419f9e00838a00cea9e2cce16068d6`.
- Assembled span, both editions: `8dc3edf144503beb3c20356235e001c474320475e3bc077f9983652e310dc033`.

New §11 distinguishes integration authorization from authorship of new formulas, proof and protocol. The preserved `planning/USER-PROPOSAL.txt` supports the content lineage. This agent was not given the underlying user authorization turns, so it assessed the register's distinction and preserved record rather than independently authenticating those turns.

## Limits and remaining blockers

No substantive blocker is identified by this bounded evidence review. E1–E2 are release cleanup items. No experiment was run, no deployment evidence was added by this review, and no institutional or catastrophe probability was estimated. The reduced proof, numerical implementation, final assembly and final release metadata require their separate checks. No comprehensive prior-art search was performed; the conclusion is that these four citations support their exact bounded uses and that the draft's stated novelty is modest, not that novelty has been established exhaustively.

## Resolution check after root repairs

Rechecked on 4 October 2026 at the root agent's request. E2 is resolved: EVIDENCE now names `../v7.1/planning/evidence-v71.md`, and CLAIMS §4 explicitly links the V7 LEDGER while distinguishing the current V7.1 preservation baseline. Both referenced historical files exist.

E1 is resolved for the current script references, Supplement and Discussion edition titles, their revision provenance, and the S0 overview of S16. A source-wide search of the core, supplement, discussion and registers found no remaining `checks_v71` reference. One minor E1 fragment remains at this recheck: `src/reg/TESTS.md:219` still says “V7 and V7.1 are revised by another,” omitting V7.2. The root agent has been notified. This is an incomplete current review-history summary, not an evidence or scientific blocker.

The source and assembled CLAIMS §§8–10 still match V7.1 under the same trailing-separator-only comparison. Both hashes remain exactly as recorded above. The bounded evidence disposition is unchanged: no substantive blocker identified; no institutional experiment, design proof or hazard-floor validation claimed by these repairs. Final release metadata was not re-audited in this follow-up.

**Final closure of E1 (4 October 2026).** Verified `src/reg/TESTS.md:219` now reads “V7, V7.1 and V7.2 are revised by another.” The remaining fragment is repaired. E1 and E2 are both closed; this bounded evidence/provenance review has no remaining finding requiring repair. Final assembly and audit remain with the root agent.
