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

## Addendum: ContinuationScope

Same compiler and procedure. `ContinuationScope.lean` (SHA-256 `89aa3c118c08d28a4653b4b90bc258d022c55eb087e4e429c779810220ceec0a`) imports only the Lean prelude. It compiled with exit 0. [`continuation-scope-audit-output.txt`](continuation-scope-audit-output.txt) holds the `#print axioms` output for its 22 declarations: `propext` and `Quot.sound` only.

## Addendum: RecordedClaims

Same compiler and procedure. `RecordedClaims.lean` (SHA-256 `71b42b8bc11f63cbb853174e6bf83210416bf9e18d44cfaafa838a86b960b4a7`) imports only the Lean prelude and compiled with exit 0. [`recorded-claims-audit-output.txt`](recorded-claims-audit-output.txt) holds the audit for its 13 declarations; the only axiom dependency is `propext`.

## Addendum: CouplingOptima, PluralRecords, TieBreaking, KeptSupport

Same compiler and procedure. `KeptSupport.lean` imports `RecordedClaims` and the renewal package (`lean/conditional/renewal/*`, with `GenerativeCore`, `Depletion` and `conditional/SupportNecessity`), and was built together with them; all exited 0. The other three import only the prelude or `PluralRecords`.

| Module | SHA-256 | Declarations | Audit |
|---|---|---:|---|
| `CouplingOptima.lean` | `81646a8870f4b14a2a06b85ec256f5870e63ae9556b91335b83e421f77da6752` | 12 | [coupling-optima-audit-output.txt](coupling-optima-audit-output.txt): `propext`, `Quot.sound`; `Classical.choice` in four theorems |
| `PluralRecords.lean` | `d64667360b7ff1e0b90ce1e664fbc2308a1d0396948073258afc8a9852d83148` | 40 | [plural-records-audit-output.txt](plural-records-audit-output.txt): `propext`, `Quot.sound` |
| `TieBreaking.lean` | `170f3879af9de33ec1e238b737ce9c8c9760aefd87d7799abaf4548a618696c1` | 9 | [tie-breaking-audit-output.txt](tie-breaking-audit-output.txt): `propext`, `Quot.sound` |
| `KeptSupport.lean` | `65ef65642e05e9d75d4feab0f3ba6ba73b03288c73af30c9bdaa29dd4dc08b3b` | 6 | [kept-support-audit-output.txt](kept-support-audit-output.txt): `propext`, `Quot.sound` |

No source contains `sorry`, `axiom` or `native_decide`.

`SelfModelCertification.lean` (fulfillment `formal/`, SHA-256 `7b839a96c4e1353e6e96c6273cf195f488461e2009b5c730887932ee07b4baa7`) was built with `ContinuationScope` and `FulfillmentStatus`; its audit is in that directory's `self-model-audit-output.txt`.

An independent AI review rebuilt all five modules and found no proof error. It found three overclaims in the prose (the tie-break "exactly two courses", the uncomposed kept-support conjunction, and the self-model's reading of a missing record) and several scope notes. All were corrected before this build.

## Addendum, 7 October 2026: empty axiom reports

Under Ren's rule that the generative model needs no axioms, the proofs of `InquiryWarrant`, `ContinuationScope`, `RecordedClaims`, `CouplingOptima`, `PluralRecords`, `TieBreaking`, `KeptSupport`, `FulfillmentStatus` and `SelfModelCertification` were rewritten without `simp`, `omega`, `funext` or classical reasoning. Local helper lemmas, proved by structural recursion, replace core lemmas that carry `propext`; each has its own audit line. All modules were rebuilt together with the renewal, valuation-development, naturalism and sufficiency packages on the merged branch; every module exited 0.

Result: 198 of 200 audited declarations print "does not depend on any axioms". The two exceptions, `KeptSupport.waiting_without_renewal_loses_support` and `KeptSupport.renewing_holder_stays_live`, inherit `propext` and `Quot.sound` only from `no_self_renewing_population_explicit_deadline` and `self_renewing_renews_forever` in `lean/conditional/renewal/`, which the renewal thread is rewriting; their own proof steps add none.

Statement changes made for this, all recorded in the module comments:
- `PluralRecords.TreatsAlike` and `TieBreaking.LotteryAlike` are stated pointwise (any record whose entries are another's relabeled), so no equality of functions is needed; `relabel_of_tie` is now pointwise.
- `unequal_claims_leave_priority_open` names the two centers as `⟨0, _⟩` and `⟨1, _⟩`, since the numerals for `Fin 2` carry `propext`.
- `FulfillmentStatus.certified`, `unknownCount` and `Faithful` use exhaustive non-overlapping patterns; their equations are unchanged.
- `KeptSupport` follows the renewal package's current interface (`History`, bounds read off the kinds).
- `SelfModelCertification.World` is renamed `Course`, under the monist naming rule.

Audit outputs in this directory and in the fulfillment `formal/` directory were regenerated from this build.
