# Consumable material for a changing updater

[ConstructedUpdater.lean](ConstructedUpdater.lean) supplies a typed component refinement of the existing `UpdaterFormation` operational law. Every updater formation consumes one A and one H; a `false` selector consumes two A and a `true` selector two H. The events retain their original fuel, source, lease and response effects, including paid updater formation. Used parts remain in bound inventories and cannot be reused.

The principal `material_trace_lift_iff` states an exact criterion: a specified finite updater history and endpoint lift into this material process if and only if they are feasible under the existing law and both cumulative typed demands fit the inherited free stocks. The statement includes arbitrary finite event words, not only the concrete witness.

## Actual material and support entrance

The predecessor is the unchanged `FormedSelection` relation. The bridge requires an intact site, an actually captured local unit, sufficient adapter fuel, and one free A and H. Those two parts become adapter backing. The paid local-to-common conversion and source quotient/remainder agree with `UpdaterFormation.entrance`; the converted local unit is not stored twice. Resident material and any unused precursor capacity remain accounted for. Neither updater nor selector is active at entrance.

The joined witness starts with material capacity thirteen, common fuel twenty-nine and source energy ninety-seven. Five H formations, eight A formations, A association, repair and capture leave the actual handoff stock. It then executes the earlier `updaterWitness` event word with its coarse material field changed from two to thirteen. Both updater kinds are formed and actually govern selector reconstruction before a productive final response.

The closed ledger is `126 = 15 preparation + 1 adapter + 59 operation/waste + 51 remaining`. All thirteen material units remain present: one resident, seven bound A and five bound H. Final free stocks are zero despite nine fuel units and seven source packets remaining.

This is a restriction of the coarse updater law under supplied consumable-component recipes. It is not an equivalence with the earlier recyclable-slot material implementation. Its changed preparation and event restrictions do not inherit the old stochastic probabilities. Wiring, transduction, packet access, alternative updater repertoire and phase separation remain declared local inputs. Prediction acquisition, empirical chemistry, open-ended material renewal and concern are outside this package's claims.

## Verification

The fresh Lean 4.29.1 build passes **39 new theorem audits**, together with 107 inherited audits. One new theorem has an empty dependency list; the other 38 use only standard `propext` and/or `Quot.sound`. The inherited updater module also contains a `Classical.choice` dependency, reported separately. There are no proof holes, custom axioms or native proof shortcuts.

The independent model passes 1,248 enabled and 15,600 disabled handoffs; 299,584 short-word/inventory cases; 48 complete-witness stock pairs and 768 prefix/stock cases; seven boundary checks; and a complete 200-state, 522-edge graph from the smaller eight-fuel, three-packet initial state. The complete graph is not claimed for the sixteen-packet main witness. Both actual shortage preparations and the fully reached post-revision material obstruction are retained.

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/check.py
python3 experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/check_model.py
```

The formal checker pins Lean 4.29.1, freezes imported source bytes, recompiles in a fresh temporary directory, audits every new theorem and records source/compiler/checker/log hashes in [verification.json](verification.json). Inherited dependencies are reported separately from new declarations. The independent finite model records its coverage and source hashes in [model-verification.json](model-verification.json). Compiler objects and temporary dependency installations are not repository artifacts.

See the [canonical result](../../../../../../../../theories/becoming/history/MATERIAL-UPDATER-COMPOSITION.md), [mathematical companion](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/MATERIAL-UPDATER-MATH.md), and [internal review](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/MATERIAL-UPDATER-REVIEW.md). This package extends the [earlier selector construction](../README.md) by giving updater and selector formation a shared inventory; it does not revalidate that earlier package as new evidence.
