# Changing the AI Trajectory — V7.1

*4 October 2026. Conditional working paper. Originally drafted by Claude from Ren's direction; revised by Codex after the V7 readiness review. The text is AI-drafted or drawn from the author's corpus. Model review and numerical checks are not independent human certification.*

Start with [START-HERE.md](START-HERE.md): the short argument, its central conditions, what would change the judgment, and where to read next. V7.1 corrects the formal, comparative and institutional scope findings in the [V7 readiness review](../v7/reviews/readiness/REVIEW-v7-readiness.md). [V7](../v7/README.md) is preserved.

## Reading the edition

| File | Purpose |
|---|---|
| [THEORY.md](THEORY.md) | Abstract, Chinese guide and core argument: mechanisms, diagnosis, alternatives, transition and judgment. |
| [SUPPLEMENT.md](SUPPLEMENT.md) | Full statements and proofs; S13 maps open interfaces, S14 counterexamples, S15 numerical checks. |
| [DISCUSSION.md](DISCUSSION.md) | Intellectual lineage, source comparisons, alternative paths and institutional design. |
| [CLAIMS.md](CLAIMS.md) | Stable result keys, claim status and dependencies; §10 records every V7 readiness finding's disposition. |
| [EVIDENCE.md](EVIDENCE.md) | Dated sources, contrary findings and empirical gaps. |
| [TESTS.md](TESTS.md) | Cruxes, model predictions, specified rival comparisons, research studies, and activation and withdrawal conditions. |
| [LEDGER.md](LEDGER.md) | Preservation, provenance and validation record. |
| [CHANGELOG.md](CHANGELOG.md) | V7.1 corrections and remaining limits. |
| [RELEASE-REVIEW.md](RELEASE-REVIEW.md) | Fresh review verdicts, validation and the limits of public working-paper readiness. |

For a **formal read**, follow §§2–6 with S2–S6, then the requirements in §9 and the model boundaries in S13–S15. For **alignment**, read §6/S6 with §§4.3–4.4 and 5.3. For **policy and design**, read §§7–12 with TESTS and Discussion X8–X11. Results, premises, observations and recommendations have distinct labels.

The revision restricts R1 to the selection dynamics that justify it, separates concentration from narrower objectives, and qualifies the effect of scope on correction. It preserves broad E1 as the author's preferred arrangement while applying independent hazard-coverage conditions on every branch. Withdrawal before and after capability construction, self-restraint versus a monopoly freeze, and durable verified containment now have distinct assessments. No institutional advantage is established merely by naming its intended fallback.

## Sources and rebuilding

Edit `src/core/`, `src/supp/`, `src/disc/` and `src/reg/`; the root Markdown documents are assembled outputs. Registers, including this README and START-HERE, are assembled from `src/reg/`.

Results use stable declarations such as `{{!Proposition:key}}`, references `{{key}}`, number-only references `{{#key}}`, and forward pointers `{{>key}}`. Equations use `{{!eq:key}}` and `{{eq:key}}`. The assembler assigns numbers in declaration order and writes `src/keymap.json`. V7.1 preserves all 128 declaration identities from V7.

Run from `v7.1/`:

```sh
python3 src/assemble_v71.py
python3 xref_v71.py
python3 checks_v71.py > checks_v71.log 2>&1
```

After adding or removing citations, run `python3 src/refs_v71.py` following assembly, then assemble again. The reference generator reads the assembled documents. The cross-reference check also assembles and checks declarations, citations and registered structural requirements.

The default numerical inventory retains V7's 43 blocks, including **RV**, and adds **RP** for the V7.1 readiness counterexamples and retained cases. `python3 checks_v71.py RP` selects the new checks; `--full` adds heavier grids and `--legacy` runs earlier suites. S15 distinguishes independent calculations, identities and derived checks. These computations test specified models, not the empirical diagnosis or the institutional design.

**Verification status:** the full default suite passes **239 counted checks across 44 blocks**, including eight V7.1 readiness groups. Assembly and cross-reference checks pass. All 128 declaration identities and the historical author record are preserved. Three fresh focused reviews found no remaining blocker for conditional public working-paper circulation; [RELEASE-REVIEW](RELEASE-REVIEW.md) states their scopes and limits. See [verification/summary.json](verification/summary.json), [checks_v71.log](checks_v71.log) and [LEDGER.md](LEDGER.md) for the record and limits. [CLAIMS §10](CLAIMS.md) records the repairs; implementation notes are in `planning/`.