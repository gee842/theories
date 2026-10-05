# Unified theory reading bundle

Start with [the short guide](START-HERE.md), then read [the full theory](THEORY.md) and [formal core](FORMAL-CORE.md). The [claim register](CLAIMS.md) and [source map](SOURCE-MAP.md) identify what each conclusion rests on. The [synthesis record](SYNTHESIS-RECORD.md) explains integration, verification, and the remaining research frontier.

The theory and proof appendices are self-contained. This edition includes [Development 1](FORMATION.md), its [new proofs](FORMATION-MATH.md), the [ethical foundation](ETHICAL-FOUNDATION.md), and the full [formation study](formation-study/README.md) with code, data, and independent checks. It also includes the completed parallel [concern theory](concern-theory/START-HERE.md) and the [new concern–correction bridge](CONCERN-AND-CORRECTION.md). Source citations outside this package point to the preserved repository on this computer. The archive does not duplicate the 338 MB earlier source snapshot. These citation destinations may need adjustment if the reading bundle is moved to another computer; the manifest records the canonical source location and commit.

The [original formal review](reviews/formal-review-final.md), [original editorial review](reviews/editorial-review-final.md), and [original direction review](reviews/main-review-direction.md) cover the first synthesis. The [new proof review](reviews/development-01/formal-final-review.md), [integration review](reviews/development-01/integration-final-review.md), and [game audit](reviews/development-01/independent-game-review.md) cover Development 1. The [interface review](reviews/development-01/concern-interface-review.md) covers its connection to concern. Requested precision edits were applied before release. These are collaborating AI agents' reviews, distinct from external peer review and empirical validation.

From the unpacked package directory, these mathematical check programs run with Python's standard library:

```text
python3 verification/check_integration.py
python3 verification/check_mechanisms.py
python3 verification/check_formation_math.py
python3 verification/check_concern_interface.py
python3 verification/check_concern_interface_independent.py
python3 verification/check_release.py --local-only
```

The last command checks the exported documents and internal links without requiring the source repository. It replaces the local release-check result; the original canonical record is separately retained in [canonical-release-checks.json](verification/canonical-release-checks.json). [DELIVERY.json](DELIVERY.json) records package file hashes and provenance.

The concern branch's original release record refers to its canonical files before citation paths were adjusted for this bundle. Its mathematical check records are retained with their original provenance. The current delivery manifest hashes the exported versions; it does not count inherited results as new experiments.

The pre-synthesis checkpoints are `003cd2a` and `38f8022`; the original completed integration is `dd8ad7c`. The Development 1 protocol was committed as `1929eb5` before enumeration. This edition is committed as `04b75b32c809aab9c5c64afc6c89874688da5c49`. The repository was clean when this bundle was exported.
