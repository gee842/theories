# Migration map: generalization-through-lumping

Old record sha256 `92392615325d81b38a1f0d056fa2aff4cc44972286bedc0db71f961aed7a4f29`; snapshot `_process/architecture/history/92392615325d81b3/generalization-through-lumping.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Laws 1–9 were read against their declarations in `Becoming/Learning.lean` (with `GoAlike` in `Becoming/Mechanism.lean` and `Web.SelectsThrough` in `Becoming/Selection.lean`), laws 10–12 against `LearningCorrespondence.lean` in the periphery (bytes bound by the record's references). One law now carries a condition of its theorem that the old claim left to context: law 4 says “with decided equality on inputs”, which `every_determines_nothing` carries through `every_free` (`[DecidableEq I]`); the old hypotheses wrote it for `every_free` only. No law is wider than its theorem. The standard boundary no-ethical-premise is not cited: the periphery's network declarations report Mathlib's standard axioms (hypotheses[1]).

| Old text | Type | New place |
|---|---|---|
| T0 “Generalization through a lumping” | title | title (unchanged) |
| S0–S1 “A lumping generalizes exactly where it lumps and is right exactly where the world goes alike across it; structure and change are one lumping. Training selects through data; …; the acquisition chain and connectionist models are instances.” | statement | statement (unchanged) |
| C0–C3 “Let C be a class of functions I → V, D the data (a proposition on inputs) and x an input. Within C the data fix the value at x (Determines C D x) when …; g goes alike across a lumping π : I → K (Lumped π g) when …; C is free at x beyond the data (Free C D x) when ….” | definition | law 1 |
| C4 “With no premise: where an observed input is lumped with x by π, the class of functions going alike across π is determined at x by the data (lumped_determines);” | law | law 2 |
| C5 “given two values, data in a list and decided equality on K, this holds exactly where some observed input is lumped with x (determines_lumped_iff).” | law | law 2 (decideSeen among the declarations) |
| C6 “A member g going alike across π and fitting the world f on D is right at an x lumped with an observed d exactly where f d = f x (lumped_right_iff), and is right where f itself goes alike across π (lumped_world_right).” | law | law 3 |
| C7 “A free class is determined at x by the data exactly where its members all agree at x (free_determines_iff);” | law | law 4 |
| C8 “the class of every function is free at every input not observed (every_free), and with two values the data determine nothing there (every_determines_nothing).” | law (witness) | law 4 (“with decided equality on inputs” written in, see above); counterexamples[0] (unchanged) |
| C9 “Change: for a process P and a projection π of configurations, going alike under π (P66's GoAlike) is going alike by every move at every two configurations alike under π (GoAlikeAt, goAlike_iff_at);” | law | law 5 (“(GoAlike)”, declaration Becoming.GoAlike; P66 → the dependency projection-carrying-a-law, unchanged) |
| C10 “where P is determined and the outcome u₀ of a at s₀ is observed, the outcome read through π transfers to every step of a from s exactly where s₀ and s go alike under π by a (transfer_right_iff);” | law | law 5 |
| C11 “a determined law next goes alike under π exactly where π ∘ next goes alike across π (goAlike_iff_lumped).” | law | law 6 (with “Structure and change are one lumping”, from the statement) |
| C12 “Training: a selection through a relation alike (Training.Through) selects alike candidates alike;” | definition | law 7 |
| C13 “P64's selection through registration is exactly a selection through registering alike up to t (Training.web_selectsThrough_iff, by definition);” | law | law 7 (“selection through registration”, declaration Becoming.Web.SelectsThrough; P64 → the dependency selection-through-registration, unchanged) |
| C14 “a loss computed from the values on the data, and every choice made from it, select through agreeing on the data (Training.loss_through);” | law | law 7 |
| C15 “within a class free at x, every selection through the data has, for every selected member and every member's value at x, a selected member agreeing with the first on the data and taking that value at x (Training.unselected_beyond_data);” | law | law 8 |
| C16 “every member of C agreeing on the data with a world in C takes the world's value at x exactly where Determines C D x (Training.fit_right_iff).” | law | law 8 |
| C17 “Witness: in Shift (…) the lumping determines the untried input (Shift.determines), the class of every function does not (Shift.every_nothing), and the generalization is right where the world is the same at every position (Shift.right_same) and wrong where it differs (Shift.wrong_both).” | law (witness) | law 9; counterexamples[0] (unchanged) |
| C18 “Periphery (LearningCorrespondence, Lean 4.30.0-rc2 and Mathlib): within the uniform law family … determine every expression (uniform_determines, …, acquire_exact), and admitting its nonuniform law they determine nothing at the novel expression (nonuniform_not_determined);” | law (periphery) | law 10; “Lean 4.30.0-rc2 and Mathlib” → hypotheses[1] (unchanged) and validation_scope |
| C19 “a network's development under fixed weights is the orbit of its step (develop_orbit);” | law (periphery) | law 11 |
| C20 “Hebbian development is P66's adaptive system (hebbian, hebbian_determined), activity having a law of its own exactly where the weights make no difference to its step (hebbian_activity_law_iff), and in the three-unit memory they do (weights_matter), so activity alone has no law (hebbian_no_activity_law);” | law (periphery) | law 11 (“a system changing its own rule” for “P66's adaptive system”, the wording of the dependency's interface) |
| C21 “the network under a route of updating is again an adaptive system with the route as the rule (…), having a law of its own exactly where the route makes no difference (…), and at the starting network and first task the two routes differ (route_matters), so the network alone has no law (updating_no_network_law);” | law (periphery) | law 12 |
| C22 “the responsive route learns exactly where the task fails (responsive_kept, responsive_learns).” | law (periphery) | law 12 |
| H0 “The core part adds no axiom; the class C, the data D, the lumping π and the selection are supplied …; determines_lumped_iff further assumes …, and every_free decided equality on I.” | premise | hypotheses[0] (unchanged) |
| H1 “The periphery is checked with Lean 4.30.0-rc2 and Mathlib: …” | premise | hypotheses[1] (unchanged) |
| R0 “Ren, 12 October 2026: “我觉得理更像是对结构和变化的规律的建模”.” | Ren's words | correspondence (verbatim, unchanged) |
| R1 “On Ren's reading 理 is the modeling of the laws of structure and of change; the AI reads a model of structure as a lumping (Lumped) and a model of change as a lumping the step goes alike across (GoAlike), and goAlike_iff_lumped says the two are one notion.” | reading | correspondence (unchanged) |
| R2 “This replaces the AI's reading in P49, “a model answerable to registration”; on Ren's reading a model is still tested only through registration.” | reading | correspondence (“in testing-within-registration” for “in P49”) |
| R3 “Readings (the AI's, pending Ren): …; every_determines_nothing is a finite, determined form of “no free lunch”; …” | reading | correspondence (English unchanged; the Chinese “没有免费的午餐” became the theorem's English name “no free lunch”, as the English has it: 免费 is in the lint's list of market words, and the phrase names a known result, not a relation) |
| L0 “The class, the data and the lumping are supplied” | premise | hypotheses[0] (which says the same) |
| L1 “which class an actual formation or network holds or can reach, which lumping it imposes and its correspondence to the world are not derived” | non-implication | does_not_show[0] (“The laws do not derive …”) |
| L2 “optimization dynamics, implicit bias and probabilistic generalization bounds (PAC, VC dimension) are not stated” | scope | does_not_show[1] |
| L3 “the periphery's networks are three-unit models, not modern deep networks” | correspondence | does_not_show[2] |
| L4 “goAlike_iff_lumped is near-definitional, its content being that it gives Ren's 理 a formal referent” | scope | does_not_show[3] |
| L5 “the periphery instances re-read earlier results and give numerical witnesses, the delta being the connection” | scope | does_not_show[4] |
| L6 “the readings other than 理 (Ren's) are the AI's, pending Ren” | standard boundary | standard_boundaries: names-provisional; the correspondence says “Readings (the AI's, pending Ren)” and “On Ren's reading 理 …” |
| L7 “contains no ethical predicate” | standard boundary | standard_boundaries: no-evaluation |
| V0 “14 October 2026: the current bytes of Becoming.Mechanism, Becoming.Selection are bound to consolidated receipt 20261013T204910.042715Z (passed: …).” | evidence | validation_scope (the receipt and the two modules); the counts stay in the receipt and the snapshot |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence | validation_scope (“renamed since”); the renames are in the general-laws history note (unchanged) |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 75 theorems of Becoming.Learning all have empty axiom reports, among them …;” | evidence | validation_scope; the count and the list stay in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules …” | evidence (counts) | receipt + snapshot |
| V4–V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “Successful periphery learning-bridge check with Lean 4.30.0-rc2 and Mathlib ea11ccc0 (20261013T095759.980593Z): the 15 theorems/19 declaration audits of LearningCorrespondence, the 6 acquisition declarations with empty axiom reports and the rest reporting only Mathlib's standard axioms (propext, Classical.choice, Quot.sound);” | evidence | validation_scope (the receipt, the two axiom reports); the counts and the Mathlib version stay in the receipt and the snapshot; the axiom names are in hypotheses[1] |
| V7 “every other module in its import closure matches a passed receipt;” | evidence | receipt + snapshot |
| V8 “the core does not import it.” | evidence | validation_scope |
| V9 “The author's counterreview is in §92 of the integration note; there is no independent review yet.” | evidence | validation_scope; §92 stays in the snapshot |
| N0–N1 “Periphery instances of the lumping an actual architecture imposes (sharing across positions, invariance); generalization over undetermined processes;” | next step | next_delta (unchanged) |
| N2 “instance theorems with P69's Alike and P70's account of what a description keeps and loses;” | next step | next_delta (“Alike of Becoming.Unfolding and the account in Becoming.Description”) |
| N3 “Ren's judgment on the AI's formal reading of 理.” | next step | next_delta (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |
