# Unified theory reading bundle

Start with [the short guide](START-HERE.md), then read [the full theory](THEORY.md) and [formal core](FORMAL-CORE.md). The [claim register](CLAIMS.md) and [source map](SOURCE-MAP.md) identify what each conclusion rests on. The [synthesis record](SYNTHESIS-RECORD.md) explains integration, verification, and the remaining research frontier.

The theory and proof appendix are self-contained. Source citations outside this package point to the preserved repository on this computer. The archive does not duplicate the 338 MB source snapshot. These citation destinations may need adjustment if the reading bundle is moved to another computer; the manifest records the canonical source location and commit.

The [formal review](reviews/formal-review-final.md), [editorial review](reviews/editorial-review-final.md), and [direction review](reviews/main-review-direction.md) are collaborating AI agents' reviews. The precision edits requested in the editorial review were applied before release. Review is distinct from external peer review and empirical validation.

From the unpacked package directory, the two mathematical check programs run with Python's standard library:

```text
python3 verification/check_integration.py
python3 verification/check_mechanisms.py
python3 verification/check_release.py --local-only
```

The last command checks the exported documents and internal links without requiring the source repository. It replaces the local release-check result; the original canonical record is separately retained in [canonical-release-checks.json](verification/canonical-release-checks.json). [DELIVERY.json](DELIVERY.json) records package file hashes and provenance.

The pre-synthesis checkpoints are `003cd2a` and `38f8022`. The completed integration is committed as `dd8ad7cb8276935ed7025502e8cbf69a28a19a5f`. The repository was clean when this bundle was exported.
