# Build record: InquiryWarrant

6 October 2026. Fresh isolated build in a Linux cloud container, compiling each module with plain `lean -o` and `LEAN_PATH` set to the build directory (the same procedure as `check_consequence_inquiry.py`, whose pinned macOS binary path is not available here). The compiler is the official Lean 4.29.1 Linux release; its binary hash necessarily differs from the macOS hash pinned in the earlier verification.

```
Lean (version 4.29.1, x86_64-unknown-linux-gnu, commit f72c35b3f637c8c6571d353742168ab66cc22c00, Release)
lean binary sha256 3e0d0d3d801675359f2d4cf9815bfdb417b20b92fdd9d48b3b14c95bbae28bbf
GenerativeCore exit 0
RemainingDependency exit 0
ConsequenceInquiry exit 0
InquiryRelevance exit 0
InquiryWarrant exit 0
```

## Source identities

| Module | SHA-256 | Status |
|---|---|---|
| `GenerativeCore.lean` | `e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8` | unchanged |
| `RemainingDependency.lean` | `bacb8ebbdb38ea3367250f39f3dc5aace9a4e557256dc69cb00e70ccbe41af98` | unchanged |
| `ConsequenceInquiry.lean` | `862bb838eb7916e6f149cd38fd2673f1965585d775d422ca16e181bdbabf50be` | unchanged |
| `InquiryRelevance.lean` | `3ec8363e61404c1d23ecf5f562cb9bb880f6d136a0b936e725e2e4a98c9e4df1` | unchanged |
| `InquiryWarrant.lean` | `e7805809d157aa5e528e5085298a7f77dc6e033bc93578545eb9bbb3e1dfecb2` | new |

## Audit

[`audit-output.txt`](audit-output.txt) holds the complete `#print axioms` output for all 27 explicit new declarations. Dependencies are `propext` and `Quot.sound` only: no `sorryAx`, no `Classical.choice`, no custom axiom. The source contains no `sorry`, `axiom` or `native_decide`. The prerequisite modules rebuilt without error; their own audits are recorded in the earlier verification.
