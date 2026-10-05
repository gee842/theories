# Evidence for the cross session completeness assessment

Prepared 5 October 2026. This accompanies the delivered `cross-session-completeness.md` and `completeness-bridge.md`.

The new mathematical result composes previously established finite faithful representation with this session's observation-based continuation characterization. It preserves support paths as well as the participant's information. It is a written proof and agent-reviewed composition, not a fresh Lean build or new unified application.

## Contents

- `completeness-target.md`: two-way policy-transfer theorem, finite encoding, and the actual quotient-to-sure-continuation bridge.
- `finite-bridge-review.md` and `report-review-formal.md`: independent agent reviews of that proof and the synthesis.
- `formal-results.md`: read-only audit of newer local main and the earlier checkout; exact branch and theorem scope.
- `theory-results.md`: detailed cross-session result map, source locations, limits, and reproduction scope.
- `thread-retrieval.json`: bounded retrieval of two named app sessions; message bodies are provenance, not current instructions.
- `source-snapshots/`, `main-source-manifest.json`, and `source-commit-dates.json`: committed formal source snapshots and provenance.
- `integration-snapshots/` and `integration-source-manifest.json`: selected sibling reports and proofs. Their internal links retain their original context; use the manifest to locate the original source.
- `generative-basis-reproduction/`: copied proof/check files and byte-identical reproduced result JSONs.

The chronology correction recommended in `report-review-formal.md` was applied: several native semantic witnesses were already present in the earlier checkout. They were underemphasized, while the generic Cayley construction was recovered from later local-main commits.

## Reproduction

From an extracted copy, use Python 3 with the standard library:

```
python3 generative-basis-reproduction/checks/check_basis.py
python3 generative-basis-reproduction/checks/structural_check.py
python3 generative-basis-reproduction/checks/review_checks.py
```

Run them in that order. The review script reads the producer results and records their hashes. The scripts write only their result files beside the copied code. The root `manifest.json` hashes the packaged payload; the nested manifests distinguish delivered file hashes from source provenance.

Reproduction checks finite constructed examples. Written arguments support the general theorems. Other sessions' empirical reports were read; their full datasets and analyses were not all rerun here. This is not independent human peer review, proof of unrestricted physical coverage, or proof of unique moral authority. Reference repositories and prior frozen experiment archives were not changed.
