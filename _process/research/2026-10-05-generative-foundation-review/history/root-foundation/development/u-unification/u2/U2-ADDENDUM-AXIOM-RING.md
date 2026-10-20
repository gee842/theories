# U2 addendum: periphery joins that inherit axioms

17 October 2026, the integrator. Batches P2 and P3 found that most general laws of the periphery modules have non-empty axiom reports (`propext`, `Quot.sound`, sometimes `Classical.choice`), from `simp`, `omega`, `decide` on propositions, `by_cases` and overlapping list matches in the periphery's own proofs and definitions. The repository's rules settle what may change: the core must be pure; the periphery may use any tool; a joined module's original file keeps its path and bytes (board rule 8). So the periphery files are not edited, and joins through such roots cannot sit on the pure bridge.

**New ring: periphery joins.** A join through an axiom-dependent root goes in a separate module, the **periphery-join** ring. It is compiled in the core checker's run after the bridge and imported by nothing in the core or bridge. Its audit reports every axiom exactly, and the only axioms allowed are those it inherits from the periphery theorems it uses (`propext`, `Quot.sound`, `Classical.choice`). It adds no axiom, `sorry` or `implemented_by` of its own. Every other point of the standard holds: the base object carries the law, the reading is exact, names are structural, there are no warnings, and proofs go through the root.

How to write them:
- Keep pure joins (empty reports) and periphery joins in **different modules**. Name a periphery-join module with the same structural word plus the suffix `Inherited`, for example `TreeSearchRunsInherited`, so its ring is visible in its name. It may import your pure join module and reuse its readings.
- Do not use `simp`, `omega` or `decide` in your own proofs even here. The only axioms should be the ones the periphery theorems bring in. Where it is no harder, prefer a proof that brings in fewer.
- Each periphery-join module's docstring ends by naming the axioms it inherits and from which periphery theorems, instead of "No … axiom occurs".
- In `classification.json`, keep `axiom-dependent` only for roots with no meaningful reading on the base at all; use `model-witness`, `periphery-scope` and so on as usual. A root joined in the periphery-join ring is joined, not classified.
- In your report, give the axioms each periphery-join module inherits, as `scratch_build.py` shows them under `with_axioms`. Expect them there; `"unclean": []` must still hold.
