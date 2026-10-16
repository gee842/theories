# Constructive dependency removal and finite inquiry: scoped review

6 October 2026. AI-authored review. The finite-classifier reviewer independently inspected that mechanism and its verification artifacts, but authored the repairs to `Depletion.lean` and `RootRealization.lean`. That reviewer's checks are therefore **not an independent review of those two repairs**. A separately attributed section below records the independent proof-source review by `current_scope`. No scientific simulation was rerun for this review.

The named connection remains **inquiry effects → acquired revision of which unresolved differences require inquiry**. The finite result closes one representation interface within that connection: construct the exact possibilities after an observation and derive the branch classification required by the existing bounded-policy characterization. It does not establish acquisition or revision of the criterion itself. This distinction follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md): the law and observation interface are local representations of related activity; supplying them here does not make them external to generative reality.

## Source review

The reviewed mechanism is [FiniteInquiryClassification.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/FiniteInquiryClassification.lean), with the meanings of `After`, `Completes`, `Sound`, `Within` and `ClassifiedThrough` taken from [InquirySufficiency.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/InquirySufficiency.lean). No material defect was found in the reviewed finite classifier.

| Question | Finding |
|---|---|
| Does the proof silently make every finite proposition decidable? | No. The generic interface explicitly takes `transition : ∀ s a t, Decidable (P.step s a t)` and decidable belief membership. `infer_instance` in `afterMembership` uses these decisions, constructive conjunction and equality on `Fin`; it does not supply arbitrary propositional decidability. |
| Are nondeterministic branches lost? | No. `afterMembership` searches every predecessor in the full declared carrier; `successors` then enumerates every endpoint. `mem_successors_iff` proves exactly `t ∈ successors … ↔ ∃ s, B s ∧ P.step s a t ∧ sense s a t = o`. Both directions matter: no unsupported endpoint is introduced and no compatible endpoint is omitted. |
| Is the actual continuation retained? | Yes, within this representation. `actual_successor_retained` inserts the actual predecessor, native step and resulting observation into that exact relation. No deterministic transition or favorable-successor selection is required. |
| Is branch classification merely renamed as an input? | No. `states_complete`, exact enumeration and `beliefDecision` construct it; `classifiedThrough` derives it recursively at every finite depth. The Boolean initial interface removes a separate membership-decision argument as well. |
| Is there a hidden finite action search? | No. `classifiedThrough` proves the property for each supplied action and observation. `Action` and `Response` need not be finite. This is why the policy characterization is not an executable policy-search algorithm. |
| Does empty belief produce a false success? | No. The final equivalence explicitly includes `InhabitedBelief B`. A zero-sized carrier has no inhabited initial belief. `abort` applies only to unreachable branches in the inherited semantics. |

The inherited `Completes` condition requires each prescribed action to be enabled and every admitted successor to preserve the local condition and complete the remaining word. The finite interface therefore retains the earlier protection against counting one favorable endpoint while overlooking an admitted deadlock or unsafe prefix. It does not add a scheduler or convert existence into an occurrence guarantee.

## What the representation preserves and omits

The enumeration retains all information already carried by each state. It does not reconstruct omitted history. If two earlier histories reach the same represented state, `After` forms their union at that state; a question about their different origins needs the relevant origin retained in the state representation. A finite truncation of an infinite native process also needs a separate faithful-representation argument. These are boundaries of the representation, not counterexamples to exact enumeration on its stated carrier.

The generic theorem itself introduces no classical decision oracle. An application could nevertheless instantiate its explicit `Decidable` parameter using a classical construction. Such an application would require its own dependency and executable-input audit. Empty reports for the generic theorem alone do not certify every possible instantiation.

`safe`, `goal`, response words, sensing and initial data remain explicit local inputs. Their relation to acquired significance, concern or criterion revision is not derived by eliminating an enumeration certificate. The result neither requires them to be fundamentally independent nor proves their generative formation. Nor does it prove that the mathematically sufficient policy exists for every configuration.

## Independent checks completed

The initial three-module receipt was independently reconciled against its current sources, immutable snapshots, logs, compiler, toolchain and checker: **12 hash comparisons passed**. A fresh temporary build of `GenerativeCore`, `InquirySufficiency` and `FiniteInquiryClassification`, with `LEAN_PATH` set to that build alone, reproduced all **48 empty dependency reports** and all three saved logs byte-for-byte. The finite module contributed 13 reports at this stage.

Five additional computational definitions were inspected through this supplemental source, compiled against that fresh closure:

```lean
import FiniteInquiryClassification
#print axioms Generative.InquirySufficiency.FiniteClassification.states
#print axioms Generative.InquirySufficiency.FiniteClassification.collect
#print axioms Generative.InquirySufficiency.FiniteClassification.decisionBit
#print axioms Generative.InquirySufficiency.FiniteClassification.enumerate
#print axioms Generative.InquirySufficiency.FiniteClassification.successors
```

All five reports were empty. These supplemental checks are not counted as additions to the public receipt's declared audit total.

The next public-closure stage was also independently rebuilt from frozen source bytes. Its [immutable 225-audit receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/finite-runs/1791274561004584000/receipt.json), dated `2026-10-06T08:16:06.948452+00:00`, has SHA-256 `406b2ae0c0c1ea83c09b40b86cb8d5701948371538e915b3a643c417fd9e0502`. The check established:

- All 20 modules compiled afresh, with 225 empty reports and no warnings; every new log matched the saved log byte-for-byte.
- All 212 inherited declaration/dependency maps were retained exactly.
- All 126 hash comparisons passed: 20 current sources, 20 source snapshots, 20 logs, compiler, toolchain, checker, baseline receipt, baseline snapshot, archive manifest and all 60 archive files.
- Sources and the receipt remained unchanged during the independent build. Existing local `.olean` files were not used.

These checks validate the reported declarations and their dependency reports under the recorded Lean compiler. They are not a proof that every possible declaration in the imported library is axiom-free, and they do not eliminate the local model's parameters or establish a completed foundation. The stricter migration checker's preservation and body-equivalence tests are separate from this independent finite-module review.

## Final Boolean interface and 227-audit receipt

The final addition is `tableProcess table`, defined by the relation `table s a t = true`, and `boolean_model_iff_bounded_policy`. Inspection of the fully elaborated theorem signature confirmed that it has **no generic `P` or transition-decision parameter**. Its inputs are the Boolean transition function, Boolean initial membership, sensing, the local condition and endpoint requirement, response words and depth. Boolean equality supplies transition decidability internally. This is a generic representation adapter, not an asserted physical law or a proof that an arbitrary native process has that finite representation. The generic native-process interface remains available.

The final source hashes are `1a0613f734ccdd432656770d6d73d7ee7db4b119f57b379ebe8ff7f623054375` for the mechanism and `23a987f6c021df07456bd8b9bb0b5a5a99855144b54cfee06ce8207be33a0b20` for the [public entry](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeFiniteInquiryModel.lean). Both changed modules were independently recompiled against the unchanged 18-module closure already built afresh above. The mechanism's **15 dependency reports were empty**; the public entry contains imports only. The complete elaborated signature was also checked directly with `#check @Generative.InquirySufficiency.FiniteClassification.boolean_model_iff_bounded_policy`.

The [final immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/finite-runs/1791274808194068000/receipt.json), dated `2026-10-06T08:20:15.016253+00:00`, has SHA-256 `b7cd95e327f86e712c3367f3458a3b8e8d3eadc042e0c59a48ef74a8f9a66450`. It records a fresh **20-module, 227-audit** build, all empty, with the exact 212 inherited audit maps retained. Independent reconciliation again passed all 126 source/snapshot/log/compiler/baseline/archive hash comparisons. Receipt, checker and toolchain copies also matched byte-for-byte. All 20 final source snapshots and logs match the independent build, with only the two changed modules recompiled at this final stage.

The [final checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_finite.py) pins the immutable sufficiency baseline `runs/1791274724854453000/receipt.json`, SHA-256 `5b95908a98c1b33ad9cbfaab5dbc00788c5c92e40ef8e778a3c0a2af0ff419bd`; it does not depend on the mutable convenience receipt remaining unchanged. The checker itself has SHA-256 `575efdbc59a2e2c9c5a7e76aef8a1c1413b4f7b192d80829d6b0cd59160c9b6e`. No material source, dependency or receipt discrepancy was found. The limits stated above still apply: classification is derived for the declared finite representation; criterion formation, native correspondence and a policy-search procedure are not thereby derived.

## Independent review of the canonical proof repairs — current_scope

This reviewer authored the migration checker, but did **not** author the repairs to [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) or [RootRealization.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/RootRealization.lean). This section independently reviews those two proof sources against the [preserved originals](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification-history/2026-10-06-before-axiom-removal/manifest.json); it is not an independent review of this reviewer's checker. Reviewed source hashes are `324021e3f315d7f06f2ae28624aa4468f1029a77347a6f3952c5313c2641aa3e` and `584af3a49ae9b9ce8e5a0b184eab9412376628e2346fd36f45f672a71794b524`, respectively. No blocking issue was found. Completed build evidence was inspected; no duplicate build was run for this source review.

The depletion repair preserves all five original quantified statements, including strict decrease on **every** permitted step. The trace induction adds one to the tail bound and composes it with the strict decrease. For a nonempty cycle this would put the starting reserve plus one below the starting reserve. For an alleged infinite execution, the bound at time `reserve (states 0) + 1` gives the same contradiction. No finite-state condition, constant decrement, probability, replenishment exclusion beyond the existing premise, or selected-successor restriction was added.

The realization preserves its constructors, namespaces and signature contexts, and all original declaration types. Its only model-definition rewrites are exhaustive presentations of `supported` and `law`. The five possible edge patterns remain identical, including restoration being controlled by the original `supplied` Boolean and terminal states having no action. The 200 closed law comparisons cover the full `Bool × Phase × Event × Phase` domain; the five support and five selector comparisons likewise exhaust their domains. `selector`, `process`, `cycleState`, `cycleEvent` and `decoratedProcess` retain their original definition bodies. This correspondence preserves the alternative terminal history as well as the renewable cycle.

The six added private arithmetic helpers establish independence of the remainder routine's sufficient recursion bound, relate its unfolding to standard natural-number remainder, derive period two, and prove adjacent parity by induction. The recursion-bound argument retains both required bounds and the positive-divisor condition where the internal routine needs them; the general unfolding handles a zero divisor separately. The cycle theorem then uses the two proved parity alternatives to establish the original native step at every natural-number index. The modulo definitions of the trajectory were not replaced with another process or assumed parity law.

Accordingly, the dependency removal preserves the prior semantic scope: a conditional strict-depletion obstruction and a finite satisfiability witness under its supplied event law. It does not derive that law, imply that every history renews, or establish the formation of concern, an inquiry criterion or an assumption-free ontology. The changed implementation and proof terms discharge the recorded named dependencies at the checked scope; they do not erase the documented explanatory inputs.
