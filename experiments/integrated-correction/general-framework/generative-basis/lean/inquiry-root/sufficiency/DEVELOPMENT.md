# Development scope and dependency correction

6 October 2026. The local proof was checked against a freshly compiled `GenerativeCore` in temporary scratch before the final public closure build. No ancestor source was edited, and no simulator was run.

The first narrow compile exposed two ordinary elaboration errors: an unknown depth prevented reduction of `Within n abort`, and a shadowed state name prevented elaboration of an execution case. Explicit depth cases and inference of the actual bound state corrected them. These attempts were not accepted verification results.

The first finite-choice proof used the standard `Fin.cases` helper. Its dependency report included `propext`. Direct finite-table construction removed that dependency from the helper, but the theorem still inherited `propext` through the instance used for overloaded numeric zero at type `Fin (n + 1)`. Supplying the explicit constructor `⟨0, Nat.zero_lt_succ n⟩` removed that implementation dependency. The final finite-choice argument uses induction on the finite branch count, direct constructors and native equality elimination; no choice axiom, excluded-middle call or altered policy semantics was introduced.

The final source-only run is preserved by [verification.json](verification.json) and its referenced `runs/` directory. It recompiles all eighteen modules and requires the original sixteen audit maps unchanged and all seventeen new audits empty. The narrow failed attempts motivated a proof implementation correction, not a change to the criterion, process or scientific claim.
