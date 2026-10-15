# Landing package: how often couplings act — settling, runaway and its rate (P123)

耦合多常作用（安定、失控与其速度）的落地包。内容在分支 `p123-frequency`；本目录保存内容的文本与写入它们的脚本。

[what-a-cut-loses](../../../../../../theories/becoming/results/records/what-a-cut-loses.md) (P120) lists three open items first in its next steps:
- whether every schedule of couplings settles, and the exact strength of that claim;
- whether every loop of recurring couplings makes the most difference that can arrive run away;
- how fast a runaway is (a spectral radius).

The chapter's §8 lists the same items under feedback and reach. On 12 October 2026 Ren asked of the loops: “how how accurate can we do that uh what is the limitation do we have losses” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). On 16 October Ren called the AI's reading of “only a loop makes a difference run away” right. That reading left couplings at only some steps open ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md)). Current math core (fork 2) claimed this on the work board as P123.

## Content

One commit on branch `p123-frequency`, on main `ed704543`, after P124 (`Becoming.Thresholds`, study §157) landed.

- `Becoming/Frequency.lean` is a new core module.
  - It sits in L4 and imports `Becoming.Closing`. It changes no existing module.
  - It has 83 theorems and 98 declarations.
  - `scratch_build.py` on `ed704543` gives every axiom report empty, with no warnings.
  - The root `Becoming` compiles with its 123-module closure, so no names clash.
  - Both steps are stored in the shared cache.

  The module covers six parts:
  - **The rate.**
    - The count of a schedule's marked steps (`Frequency.count`).
    - The carried amount is at most D·(1 + M)^a, where a is the number of marked steps (`carried_le_count`). It is at most D·A^M·(t + 1)^(nM) where 2^a ≤ A·(t + 1)^n (`carried_le_of_rare`).
    - With every condition listed, the steps at which anything couples are such a schedule (`Frequency.coupling`, `carried_le_coupling`).
    - The self-loop on any schedule couples exactly at the marked steps and carries exactly the bound. It is polynomial exactly where 2^a is (`Frequency.SelfLoop.couplesAt_iff`, `Frequency.SelfLoop.carried_eq`, `Frequency.SelfLoop.polynomial_iff`).
  - **Runaway needs frequent couplings, not strong ones.**
    - A coupling at a step adds at least what it reads (`carried_step_ge_at`).
    - Chains in time order (`ChainInTime`, `carried_along_in_time`).
    - Returns (`Returns`) at least double what has arrived (`carried_doubles_return`), and R returns multiply it by 2^R (`carried_returns`).
    - Frequent returns run away whatever the strengths (`runaway_of_returns`).
  - **A recurring loop need not run away.** The sparse schedule marks the steps 0, 1, 3, 7, … (`Frequency.Sparse`). Its bounds are `Frequency.Sparse.bounds` and `Frequency.Sparse.rare`. Its self-loop recurs, so every finite order is inexact, yet it stays polynomial (`Frequency.Sparse.inexact`, `Frequency.Sparse.polynomial`).
  - **Settling is local.** A coupling that stops (`StopsBy`) does not recur. With every condition listed, where each coupling recurs or stops, the schedule settles (`Frequency.bound_list`, `settled_of_each`).
  - **Settling for every schedule is a principle of reasoning, exactly.**
    - Whether a coupling reads late is decided (`Frequency.readsLate`).
    - The dichotomy `RecursOrStops` gives `LPO` (`RecursOrStops.lpo`) and gives settling (`recurs_or_stops`, `settled_of_recursOrStops`).
    - Two witnesses show the converse:
      - the first-true self-loop: once, not recurring, deciding its sequence (`Frequency.First`, `lpo_of_settled`);
      - the rows self-loop (`Frequency.Rows.recurs_iff`, `Frequency.Rows.decide_rows`).
    - Together these give the two equivalences, `settled_iff_recursOrStops` and `settled_every_iff`.
  - **Instances and every law.**
    - Loops' self-loop and Closing's onset (`Frequency.SelfLoop.always_carried`, `Frequency.SelfLoop.onset_amount`).
    - `gap_le_count`, through `gap_le_carried`.
- `apply_docs.py` makes the following edits. It reads the bullet, rows, paragraphs and summaries from `docs.json`, which `make_docs_json.py` writes.
  - `Becoming.lean`: the import after `Becoming.Thresholds`, and the module bullet after Thresholds'.
  - `check_becoming.py`: `Becoming.Frequency` in the core list after `Becoming.Thresholds`, and a scope entry after Thresholds'.
  - The Lean README: one L4 row after Thresholds', and the within-layer imports.
  - The theory chapter:
    - §2, the paragraph "What a cut loses": a dated parenthetical names the three of its not-derived items that `Becoming.Frequency` answers. P120's readings, pending Ren, are left as they stand.
    - §2: a paragraph pair "How often couplings act (Part I)" after the paragraphs on loops within what a law reads (P124).
    - "Part I stated whole": one item after loops within what a law reads.
    - §8, the status row of the response as the dynamics give: whether every schedule settles, and whether every loop of recurring couplings makes the most difference that can arrive run away, leave the open items. How fast a runaway of given strengths is (a spectral radius) joins them. The row's last clause, on its readings, is left as it stands.
    - §8, the further proofs under feedback and reach:
      - how often couplings act is now given, after the clause on loops within what a law reads;
      - the tail becomes how fast a runaway of given strengths is;
      - P124's open item, how a formation comes to observe a stock it depends on, is left as it stands.
    - §9: one L4 row (83 theorems).
    - The glossary: rows "return (around a loop)", "how often couplings act" and "recurs or stops" after "break (of a stock read only below a threshold)".
- The study gains a section and its English paragraph (`study.md`, `study-en.md`; `apply_study.py W [N]`).
  - The section is numbered 158 provisionally. Main holds §157 (P124).
  - `apply_study.py` renumbers the heading to N and refuses a number already taken.
- `apply_inventory.py` edits `DECIDABILITY-INVENTORY.py`.
  - One theorem uses the equality of conditions only in its proof (`same`): `gap_le_count`, through Propagation's `gap_le_carried`.
  - A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Its totals: proof-only 238 → 239 ("same" 186 → 187). The others are unchanged: 417 dependent statements, 109 decidability-taking definitions.
- Records:
  - `make_record.py ROOT [N]` writes the new schema-2 record how-often-couplings-act.
    - Ten laws cover all 98 declarations.
    - Its proof references are hashed from the branch.
    - `proof_bindings` is empty, and the record reads "receipt bound at landing".
  - `update_records.py ROOT [N]` writes the paired notes, one history note in each record.
    - **what-a-cut-loses.** Two items leave next_delta: whether every schedule settles, and whether every loop of recurring couplings makes the difference run away and how fast; the spectral radius of given strengths stays. Related adds the new record. The same note handles "joining what a cut loses to the losses of the sum over histories": orders-as-a-sum-over-histories (P121) answers it, and the P121 landing had left it in place. So it leaves next_delta, the related entry saying the two are not yet joined now says so, and related adds orders-as-a-sum-over-histories. Its readings stay the AI's, pending Ren.
    - **how-a-carried-difference-grows.** The first next_delta item becomes how fast a runaway of given strengths is, beyond the product of the strengths and the count of steps at which couplings act. Related adds the new record, which closes both ways the case Ren's decided readings leave open. Its correspondence keeps the readings Ren decided.
    - Statements, proofs and does_not_show are unchanged in both.

From main `ed704543`, copy `Frequency.lean` in. Then run `make_docs_json.py`, `apply_docs.py W`, `apply_study.py W N`, `apply_inventory.py W`, `update_records.py W N` and `make_record.py W N`, in that order, to write the content commit. Each script asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. If a landing before this one takes §158, rerun the kit on the new main with the next free N. `apply_study.py`, `update_records.py` and `make_record.py` take it as an argument.
2. Run the core checker, `check_becoming.py`. `Becoming.Frequency` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to how-often-couplings-act, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the three records, run on the branch, reports two errors. Both are expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

`make research-test` fails in the same two places before binding:
- `test_current_records_are_structurally_valid`;
- `test_drafts_validate_and_render`.

The other 99 tests pass.

Every other finding is chapter drift, which step 4 reconciles. It is scoped to the sections this changes (§2 and §8) and covers 21 records:
- comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, every-origin-passes-the-gate, how-a-carried-difference-grows, how-loops-form;
- how-much-difference-arrives, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, lifting-where-branching-is-finite, orders-as-a-sum-over-histories, recurrence-without-decidedness;
- recurrence-without-premise, recurring-reference-revision, selection-through-a-model-of-the-options, sensitivity-is-the-least-registration, what-a-cut-loses, what-a-finite-history-refutes, where-a-move-is-formed.

The lint finds nothing in how-often-couplings-act or what-a-cut-loses; their texts are within every cap. The nine length warnings in how-a-carried-difference-grows are those on main.

Nothing here runs the checker, edits the board or commits.

## History

- 16 October 2026: claimed on the work board (`f02f270a`) after P120, P121 and P122 had landed. The module was built in scratch while the integrator landed Ren's agreement with the P121/P122 readings. The branch was then moved to that landing (`c0fbc84b`) and the module rebuilt; the Loops and Closing steps were already in the shared cache.
- 16 October 2026, regenerated: P124 (`Becoming.Thresholds`) landed as study §157 while this was handed over. The first head, `512152b5` on `c0fbc84b`, is kept as branch `p123-frequency-c0fbc84b`. The branch was regenerated on main `ed704543`:
  - `Frequency.lean` copied in unchanged.
  - The kit's anchors moved after Thresholds' entries, and the section became 158.
  - The six scripts rerun.
  - Frequency was reused from the cache and the root rebuilt (123-module closure).
  - The inventory rerun gives the same one row.
  - A clean export of `ed704543` with the kit reproduces the branch bytes.
- Two sentences of the module's readings were corrected before the kit ran:
  - **Ren's 16 October words.** Ren called the AI's reading of “only a loop makes a difference run away” right. The qualifier about couplings at only some steps belongs to that reading, not to Ren.
  - **"How strong sets only the degree".** This is scoped to the self-loop, the only place it is proved.
