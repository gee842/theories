# Changing the AI Trajectory — V7

*4 October 2026. Originally drafted by Claude from Ren's direction; revised by Codex after the V6.2 reviews. The text is AI-drafted or drawn from the author's corpus. Model review and numerical checks are not independent human certification.*

Start with [START-HERE.md](START-HERE.md): the short argument, its central conditions, what would change the judgment, and where to read next. V7 revises the latest V6.2 in a separate directory; [V6.2](../v6.2/README.md) remains preserved.

## Reading the edition

| File | Purpose |
|---|---|
| [THEORY.md](THEORY.md) | Abstract, Chinese guide and core argument: mechanisms, diagnosis, alternatives, transition and judgment. |
| [SUPPLEMENT.md](SUPPLEMENT.md) | Full statements and proofs; S13 maps interfaces and open assumptions, S14 counterexamples, S15 numerical checks. |
| [DISCUSSION.md](DISCUSSION.md) | Intellectual lineage, evidence-bearing comparisons, alternative paths, institutional design and transition. |
| [CLAIMS.md](CLAIMS.md) | Stable result keys, claim status, dependencies and disposition of the V6.2 review. |
| [EVIDENCE.md](EVIDENCE.md) | Dated sources, contrary findings and empirical gaps. |
| [TESTS.md](TESTS.md) | Cruxes, competing predictions, research studies, and activation and release conditions. |
| [LEDGER.md](LEDGER.md) | Preservation and provenance, including links to earlier version records. |
| [CHANGELOG.md](CHANGELOG.md) | V7 corrections and the remaining limits. |

For a **formal read**, follow §§2–6 with S2–S6, then S13–S15. For **alignment**, read §6/S6 with §§4.3–4.4 and 5.3. For **policy and design**, read §§7–12 with the cruxes in TESTS and the full alternatives and design in Discussion X8–X11. Results, premises, numerical illustrations and recommendations have distinct labels; the interfaces between models remain part of the argument's scope.

## Sources and rebuilding

Edit `src/core/`, `src/supp/`, `src/disc/` and `src/reg/`; the root Markdown documents are assembled outputs. Registers, including this README and START-HERE, are assembled from `src/reg/`.

Results use stable declarations such as `{{{{!Proposition:key}}}}`, references `{{{{key}}}}`, number-only references `{{{{#key}}}}`, and forward pointers `{{{{>key}}}}`. Equations use `{{{{!eq:key}}}}` and `{{{{eq:key}}}}`. The assembler assigns numbers in declaration order and writes `src/keymap.json`. The final comparison verifies that all 128 declarations retain V6.2's keys, kinds, numbers and source files.

Run from `v7/`:

```sh
python3 src/assemble_v7.py
python3 xref_v7.py
python3 checks_v7.py > checks_v7.log 2>&1
```

After adding or removing citations, regenerate the reference lists from `src/` with `python3 refs_v7.py`, then assemble again. The cross-reference check also assembles the edition and checks declarations, references, citations and registered structural requirements.

The default numerical inventory includes 43 blocks. New block **RV** runs the independent V7 checks in `verification/math_checks.py`, `verification/systems_checks.py` and `verification/transition_checks.py`; these can also run separately. `python3 checks_v7.py RV` selects the new block; `--full` adds heavier grids and `--legacy` runs earlier suites. S15 distinguishes independent calculations from identities and derived checks. These computations test specified models, not the empirical diagnosis or the institutional design.

**Verification status:** assembly and structural checks pass; the full default suite passes **231 counted checks across 43 blocks**, including 18 V7 regression groups. All 128 declaration identities are unchanged, CLAIMS §§8–9 preserve Ren's recorded decisions and pending renderings verbatim, and the 412-file V6.2 baseline is unchanged. See [checks_v7.log](checks_v7.log), [verification/summary.json](verification/summary.json) and [LEDGER.md](LEDGER.md) for the results and limits. Implementation notes are in `planning/`.
