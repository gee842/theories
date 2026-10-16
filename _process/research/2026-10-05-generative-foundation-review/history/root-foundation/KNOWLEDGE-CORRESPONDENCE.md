# Checked correspondence within the knowledge track

8 October 2026. AI-authored proof correspondence and dependency audit. This is a component of the [knowledge account](../../../../theories/becoming/chapters/KNOWLEDGE.md), not a definition of knowledge or a substitute for its philosophical grounding. The role being tested is **available differences → warranted discrimination**, conditional on the declared meanings, domain and access relationships.

## Source and actual validation

- [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/KnowledgeCorrespondence.lean).
- [Reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/check_knowledge_correspondence.py).
- [Current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/knowledge-correspondence-verification.json).
- [Frozen successful run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/knowledge-correspondence-checks/20261007T194225.244570Z/verification.json), containing source, checker, audit source and compiler output bindings.

Lean **4.29.1** freshly compiled the module in a temporary directory, using only `Std` and no cached project objects. **20 theorems and 34 explicit declarations** were audited. Three declarations (`decoder`, `resolution_admits_decoder`, `exact_possible_iff_resolves`) depend on standard `propext`, `Classical.choice` and `Quot.sound`; the other 31 explicit audits are empty. Hypotheses remain substantive even when the axiom list is empty. Generated structure declarations are kernel-checked, not separately counted as explicit audits. No `sorry`, user axiom, unsafe shortcut or `native_decide` occurs.

The initial direct compile found a reducible-function rewrite mismatch in the retention lemma. The proof was repaired by exposing the target expression; the recorded run checks the repaired source. This was a proof elaboration issue, not a counterexample or a change to the statement.

## Mathematical scope and correspondence

`H` represents complete local histories/configurations at the chosen level of description. `D : H → Prop` is the admitted domain. `evidence : H → E` and `target : H → Bool` are projections from the same histories. `answer : E → Option Bool` represents an answer or abstention using that evidence. This decomposition preserves the question's accessible distinctions and target values; it omits the formation of the channel, cognitive uptake, semantic interpretation, probabilities and a general theory of possible histories.

`SoundOn` requires every issued answer to be correct throughout D. `ExactOn` requires an answer, with the correct value, at every member of D. `Resolves` requires the target to be constant among histories with the same evidence. These are strong exact guarantees, deliberately distinct from fallible knowledge. There is no Lean predicate named `Knows` or a hidden ethical assumption supplied through its definition.

| Checked declarations | What they establish and what remains supplied |
|---|---|
| `exact_is_sound`, `exact_requires_resolution`, `resolution_admits_decoder`, `exact_possible_iff_resolves` | Exact answering implies soundness and requires resolution; resolution admits an abstract decoder. The converse uses classical choice, not a discovered or executable algorithm. The observation-factorization fact is familiar mathematics; no novelty claim is made. |
| `conflicting_fibre_forces_abstention` | A sound answer rule must abstain at evidence shared by admitted histories requiring opposite answers. It does not say all people in ordinary uncertain settings know nothing. |
| `sound_restricts_domain`, `refinement_preserves_resolution` | A soundness result remains on a smaller domain; adding an evidence component preserves resolution. Neither theorem warrants the choice of domain or the truth of the new reading. |
| `preserved_record_preserves_exactness` | An actual encoding/readback that recovers the evidence used by an exact rule preserves its exactness. Faithful recovery on D is a hypothesis. This is a sufficient retention condition, not a claim every raw datum must survive. |
| `calibrated_pair_exact`, `raw_signal_not_resolving`, `no_exact_raw_decoder`, `every_sound_raw_decoder_abstains` | A particular ambiguous channel cannot answer exactly from the raw reading; its specified reference supplies the needed distinction and a computable decoder. Calibration correspondence and stable orientation are local model inputs. |
| `direct_exact_on_normal`, `direct_fails_on_expanded_domain`, `lucky_actual_correct` | A direct reading works when reversal is excluded, fails on the wider family, and can nevertheless be right in a particular actual configuration. This is a genuine change of channel possibilities with fixed target meaning, not a freely toggled knowledge predicate. |
| `parity_record_exact`, `double_reversal_exact` | A sufficient compressed record and two specified inverse transformations preserve the actual answer. Intermediate symbols must be interpreted through their encoding; zero loss of all raw data and zero transformation are unnecessary. |
| `true_content_trivially_safe` | A supplied true proposition satisfies the explicitly weak fixed-content predicate regardless of the assertion route. This identifies that predicate's inability to assess competence; it does not refute richer safety accounts. |
| `abstention_sound`, `abstention_not_exact` | Always withholding an answer avoids false outputs, but fails the exact-answering requirement on a nonempty domain. Soundness must not be reported as successful discrimination. |

## The reference example reconstructed

Each `History` contains a target value and a Boolean channel orientation. `signal` applies exclusive-or. `reference` applies the same channel orientation to a stipulated known-false reference value. The paired decoder applies exclusive-or again. Both fields describe relations in one local configuration; they are not an ontological subject/world split. Sharing an orientation between the two readings represents a specific stability assumption.

Two configurations give the same raw `false` signal while their targets differ: value false with ordinary orientation; value true with reversed orientation. Corresponding ambiguity also occurs for raw `true`. These are the concrete witnesses used by the impossibility and abstention proofs. The reference separates them because it carries orientation information that the raw target reading lacked.

No organism, instrument or laboratory has been empirically shown here to satisfy these equations. The reference must be supported by a separate account of what it establishes; merely calling it calibrated cannot do that. Domain restriction also needs support: omitting the reversed cases makes a theorem easier but can misdescribe the intended application. This is the next epistemic question, not a missing line in the Lean proof.

## Limits relevant to completion

The model establishes a precise component of anti-accidental correspondence while leaving possession, competent grounding and admissible error possibilities visible. A thermostat or classifier can meet the formal conditions; this does not settle whether it knows. Conversely, ordinary fallible knowing may lack the model's absolute guarantee. The source contains no G0 parameter and proves no normative conclusion. Adding an unused G0 assumption would not connect the theorem to ethical grounding.

The knowledge track must therefore integrate these results with an explanation of cognitive uptake and of the actual error domain. Neither 20 successful theorems nor an audit with few logical dependencies proves the full task complete.
