# Ethical naturalism: formal counterparts of the four arguments

6 October 2026 (UTC). AI-assisted Lean development for the [ethical-naturalism study](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM.md), which answers [Ren's message on the four naturalist arguments](../../../../../../sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md). The study note (in Chinese) gives the interpretation, the comparison with utilitarian, Railton and Foot candidates, and what remains philosophical.

## What is proved

**`WholeQualityNaturalism.lean`: whole-history quality has the credentials the four arguments ask for.**

- Supervenience (Jackson): `supervenes_iff_factors`. A property supervenes on a base exactly when it is a function on the base-identity classes.
- The base is the whole history. `Run` keeps every intermediate state; `Along R r` holds when `R` relates the two states of every actual transition. It is a function of the visited states (`along_supervenes_on_states`). With `R = ContinuationLe`, it is not fixed by endpoints and action word (`quality_not_fixed_by_endpoints_and_word`, `quality_not_supervenient_on_word`).
- Structure, against the "shapeless disjunction" objection: composition through the shared boundary (`along_append`) and invariance under exact re-representation (`along_continuation_transport`).
- Explanation and knowledge: a damage-free history keeps every initially realizable activity realizable at every visited state (`preserved_throughout`); a single finite witness refutes preservation (`witness_refutes_preservation`); every loss occurs at an actual transition (`loss_localizes` under decidability, `loss_localizes_nn` without it). The explained fact is not fixed by endpoints and word (`availability_not_fixed_by_endpoints_and_word`).

**`NaturalismIdentity.lean`: which natural property.**

- The credentials are orientation-neutral: `naturalist_criteria_do_not_fix_orientation`. The order and its converse share them and rank an actual transition of `dip` oppositely.
- Under the stated non-undermining premise over the whole scope of activities, the admissible orientations are exactly the sub-relations of `ContinuationLe` (`generation_order_greatest`, `unprivileged_scope_is_whole_scope`, `guided_history_preserves`, `converse_undermines_in_dip`).
- Rival candidates: a scope fixed in advance admits removing an activity outside it (`fixed_scope_permits_loss`). Every complete ranking, including every scalar welfare ranking, removes a realizable activity in `incomparable` (`total_orders_undermine`, `scalar_ranking_undermines`), where `ContinuationLe` leaves the pair unranked (`generation_leaves_pair_unranked`).
- Preserved counterexample: counting every activity alike, preventing harm registers as a loss, as harm does, while leaving harm possible does not (`restraint_registers_as_damage`). The premise as stated is therefore not yet the ethical identity.

## What is not proved

The premise itself; property identity beyond necessary coextension; a principled derivation of the protected scope of activities; any verdict when every option removes something. Processes, scopes and rankings are supplied inputs. Nothing here says which history occurs or that any orientation is good.

## Verify

From this directory, with Lean 4.29.1 through elan or on `PATH`, run `python3 check.py`. The checker requires the inherited `GenerativeCore`, `DynamicUnderdetermination`, `DynamicSymmetry`, `DynamicConsequences` and `EthicalOrientation` to match the source hashes in the main [generative-basis receipt](../verification.json). It builds all seven modules fresh in a temporary directory, rejects `sorry`, custom axioms and warnings, and requires every new theorem to be audited.

The [receipt](verification.json) records **43 new audits**: 39 with empty axiom reports, and 4 that depend only on Lean's standard `propext` and `Quot.sound`.
