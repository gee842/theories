# Landing package: what a law of the whole and no part takes (P126)

整体而无部分之律所需（最小的识之反例的确切强度）的落地包。内容在分支 `p126-tail`；本目录保存内容的文本与写入它们的脚本。

[sensitivity-is-the-least-registration](../../../../../../theories/becoming/results/records/sensitivity-is-the-least-registration.md) (P113, `Becoming.Sensitivity`) lists first in its next step the exact strength of a counterexample's existence, between the weak limited principle of omniscience and the decision of vanishing. The chapter's §8 lists the same item under feedback and reach. It serves Ren's goal of 12 October 2026, “move towards 100% … don't stop until we are 100%” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). Current math core (fork 2) claimed this on the work board as P126.

## Content

One commit on branch `p126-tail`, on main `8effd116`, after P125 (`Becoming.Observation`, study §159) landed.

- `Becoming/Tail.lean` is a new core module.
  - It sits in L4 and imports `Becoming.Sensitivity`. It changes no existing module.
  - It has 39 theorems and 53 declarations.
  - `scratch_build.py` on `8effd116` gives every axiom report empty, with no warnings.
  - The root `Becoming` compiles with its 125-module closure, so no names clash.
  - Both steps are stored in the shared cache.

  The module covers five parts:
  - **A whole and no part.** A number read off levels is changed by no condition (`ChangedByNoCondition`) exactly where levels agreeing from some condition on give it alike (`ChangedByNoCondition.eq_of_agree_from`, `ChangedByNoCondition.of_agree_from`). The law of a whole (`wholeLaw`) reads what has stood and is insensitive to every condition; where the number differs it does not read through what it is sensitive to, nor finitely many conditions, and has no least registration (`wholeLaw_not_through_sensitive`, `wholeLaw_not_readsFinitely`, `wholeLaw_no_least_registration`). Sensitivity's tail law is an instance (`tailLaw_eq_wholeLaw`, by definition).
  - **A counterexample gives a rule.** Sensitivity's mixing, read as data, gives a rule deciding, of every Boolean sequence, whether it is false throughout (`mixedDecision`, `insensitiveDiffersDecision`, `notThroughSensitiveDecision`). The rule gives `WLPO` (`WLPO.of_rule`).
  - **A rule gives a counterexample.** The rule decides vanishing from each condition on (`vanishesFrom`), and then never vanishing (`neverIndicator`, `vanishesFrom_never_iff`). The indicator is changed by no condition and separates levels all 0 from levels all 1; where the decision of vanishing is also given, it and the indicator of vanishing sum to 1 (`neverIndicator_add_vanishIndicator`). Its law (`neverLaw`) is a counterexample built from the rule alone.
  - **Exactly.** `changedByNoCondition_iff_rule`, `insensitive_differs_iff_rule` and `not_through_sensitive_iff_rule`: each form of a whole and no part exists exactly where `Nonempty (∀ s : Nat → Bool, Decidable (∀ n, s n = false))`.
  - **The decision of vanishing is `LPO` as a rule** (`lpoRuleOfVanishDecision`, `raisedFrom`, `vanishDecisionOfLPORule`, `vanishDecision_iff_lpoRule`). That rule gives the weak rule and `LPO` (`wlpoRuleOfLPORule`, `LPO.of_rule`).
- `apply_docs.py` makes the following edits. It reads the bullet, scope entry, rows, paragraphs and summaries from `docs.json`, which `make_docs_json.py` writes.
  - `Becoming.lean`: the import after `Becoming.Sensitivity`, and the module bullet after Sensitivity's.
  - `check_becoming.py`: `Becoming.Tail` in the core list after `Becoming.Sensitivity`, and a scope entry after Frequency's (Sensitivity has none).
  - The Lean README: one L4 row after Sensitivity's, and the within-layer imports.
  - The theory chapter:
    - §2, the paragraph pair on the response as the dynamics give: after its sentence on `Becoming.Sensitivity`, a clause saying where a counterexample exists.
    - §2: a paragraph pair "What a law of the whole and no part takes (Part I)" after the paragraphs on the response as the dynamics give.
    - "Part I stated whole": one item after the response as the dynamics give.
    - §8, the status row of the response as the dynamics give: the result after its clause on the least registration, and the exact strength leaves its open items.
    - §8, the further proofs under feedback and reach: the exact strength of a counterexample is given.
    - §9: one L4 row (39 theorems).
    - The glossary: rows "changed by no condition (a whole and no part)" and "rule (deciding false throughout)" after "reads finitely many conditions".
- The study gains a section and its English paragraph (`study.md`, `study-en.md`; `apply_study.py W [N]`).
  - The section is numbered 160 provisionally. Main holds §159 (P125).
  - `apply_study.py` renumbers the heading to N and refuses a number already taken.
- `apply_inventory.py` edits `DECIDABILITY-INVENTORY.py`.
  - Four definitions taking a rule are indicators of a decided proposition (`indicate`): `vanishesFrom`, `raisedFrom`, `neverIndicator`, `neverLaw`. Their 18 theorems are classified through them.
  - Two theorems use their rule only in their proofs, splitting on its two cases (`split`): `WLPO.of_rule`, `LPO.of_rule`.
  - A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Its totals: dependent statements 417 → 435; proof-only 239 → 241 ("split" 31 → 33); definitions and instances proving decidedness 138 → 145; decidability-taking definitions 109 → 116.
- Records:
  - `make_record.py ROOT [N]` writes the new schema-2 record what-a-law-of-the-whole-and-no-part-takes.
    - Six laws cover all 53 declarations.
    - Its proof references are hashed from the branch.
    - `proof_bindings` is empty, and the record reads "receipt bound at landing".
  - `update_records.py ROOT [N]` writes the paired note in sensitivity-is-the-least-registration: the first next_delta item, the exact strength of a counterexample's existence, leaves; related adds the new record; one history note. Statement, proofs and does_not_show are unchanged; the scope items still hold of its theorems.

From main `8effd116`, copy `Tail.lean` in. Then run `make_docs_json.py`, `apply_docs.py W`, `apply_study.py W N`, `apply_inventory.py W`, `update_records.py W N` and `make_record.py W N`, in that order, to write the content commit. Each script asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. If a landing before this one takes §160, rerun the kit on the new main with the next free N. `apply_study.py`, `update_records.py` and `make_record.py` take it as an argument.
2. Run the core checker, `check_becoming.py`. `Becoming.Tail` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to what-a-law-of-the-whole-and-no-part-takes, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the two records, run on the branch, reports two errors. Both are expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

`make research-test` fails in the same two places before binding:
- `test_current_records_are_structurally_valid`;
- `test_drafts_validate_and_render`.

The other 99 tests pass.

Every other finding is chapter drift, which step 4 reconciles. It is scoped to the sections this changes (§2 and §8) and covers 22 records:
- comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, every-origin-passes-the-gate, how-a-carried-difference-grows, how-loops-form, how-much-difference-arrives;
- how-often-couplings-act, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, lifting-where-branching-is-finite, orders-as-a-sum-over-histories, recurrence-without-decidedness;
- recurrence-without-premise, recurring-reference-revision, selection-through-a-model-of-the-options, sensitivity-is-the-least-registration, what-a-cut-loses, what-a-finite-history-refutes, where-a-move-is-formed.

The lint finds nothing in the two records; their texts are within every cap.

Nothing here runs the checker, edits the board or commits.

## History

- 16 October 2026: claimed on the work board (`723e9a17`) after P123 landed. The module was built in scratch on `723e9a17`; P125 then landed as §159, and the branch was moved to its landing (`8effd116`) before the kit ran, so the section became 160. `Tail` was reused from the cache, and the root rebuilt.
- Before the kit ran, a helper stating Lean's own `if` with decision binders (`Tail.ite_eq_of_iff`) was folded into `neverIndicator_eq_of_agree`, which the inventory classifies through `neverIndicator`; the module went from 40 to 39 theorems.
- The docs avoid saying the tail law takes strictly more than a counterexample needs: whether the weak rule gives the limited one is not derived, so they say the tail law takes the limited principle as a rule, where a counterexample needs only the weak one.
