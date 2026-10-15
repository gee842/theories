# Landing package: what a cut loses, for every schedule of couplings (P120)

截断所失（任意耦合时程）的落地包。内容在分支 `p120-remainder`；本目录保存内容的文本与写入它们的脚本。

[how-a-carried-difference-grows](../../../../../../theories/becoming/results/records/how-a-carried-difference-grows.md) (P118) lists loops whose couplings come and go first in its next steps. `Becoming.Loops` lists the growth where couplings come and go among what is not derived. Its equivalence needs couplings at every step and every condition listed, and `Loops.Once.not_always` shows that the first premise cannot be dropped as it stands. On 12 October 2026 Ren asked: “how how accurate can we do that uh what is the limitation do we have losses” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). On 16 October, deciding P118's readings, Ren left couplings that hold only at some steps open ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md)). Current math core (fork 2) claimed this on the work board as P120.

## Content

Two commits on branch `p120-remainder`, on main `e47a1ede` (after the I4b-2 follow-up landed as study §153, `94fdd24e`, and a board commit).

1. `51dcf0dc`, Ren's P118 readings, regenerated from `929f66ab` (on `271ab66a`) as line for line the same change: `../becoming-p118-landing/apply_ren_readings.py` changes the readings in `Loops.lean`'s module docstring (comments only), the chapter's §2 paragraph, study §152 (a dated paragraph and an English bullet) and how-a-carried-difference-grows (correspondence, next_delta, the source as a provenance reference, one history note).
2. The P120 content, written by this package. It changes no existing module.

- `Becoming/Remainder.lean` is a new core module. It sits in L4 and imports `Becoming.Loops`. It has 58 theorems and 66 declarations. `scratch_build.py` on `51dcf0dc` gives every axiom report empty, with no warnings. The root `Becoming` compiles with its 119-module closure, so no names clash. Both steps are stored in the shared cache. The module covers seven parts:
  - **The exact remainder.** What one response carries (`responded`) and what j responses carry in turn (`responses`). Giving is additive in the levels read (`carriedGive_add`), so the carried amount is the orders below j plus what j responses carry from it (`carried_eq_orderBelow_add`). A cut at order j loses exactly what j + 1 responses carry (`carried_eq_carriedWithin_add`). The loss falls with the order (`responses_antitone`), is at most the bound of `Becoming.Loops` (`responses_le_missBound`) and is exactly that for the self-loop (`Loops.SelfLoop.responses_eq`).
  - **Where a cut loses.** One response carries something exactly where, at an earlier step, a positive level is coupled in (`CouplesAt`, `responded_pos_iff`). The orders below j miss something exactly where a gap is conveyed through j responses or more (`ConveyedThrough`, `orderBelow_lt_iff`, `carriedWithin_eq_iff`).
  - **From every start.** Order j is exact from every start exactly where no chain of j + 1 couplings in time order ends there (`CoupledIntoBy`, `exact_every_start_iff`). A finite order is exact exactly where those chains are bounded (`finite_order_iff_bounded`, `finite_order_uniform_iff`).
  - **Couplings that come and go.** A fed loop of recurring couplings (`CouplingRecurs`) upstream leaves every order inexact (`carriedWithin_lt_of_recurring_loop`, `unbounded_of_recurring_loop`). Where no coupling reads a level from step N on, order N is exact (`exact_of_reading_before`). A chain one longer than the list passes a loop with no listing of every condition (`loop_of_coupledInto_succ`, `no_chain_of_no_loop`); with couplings at every step, bounded chains are exactly no loop upstream (`bounded_iff_no_loop`).
  - **Where the schedule settles.** The strengths from step N on (`strengthsFrom`); the last j couplings of a chain in time order of N + j (`CoupledIntoBy.tail`). Where the schedule has settled by step N (`SettledFrom`), a finite order is exact exactly where no loop of the couplings from N on lies upstream (`bounded_iff_no_loop_from`, `finite_order_iff_no_loop_from`). Whatever the schedule, without such a loop the carried amount is at most a polynomial (`carried_le_polynomial_from`). `Loops.Once` reads the first step only and has settled from the second (`Loops.Once.reads_first`, `Loops.Once.no_chain_of_two`, `Loops.Once.settled`).
  - **`Becoming.Loops` as instances.** `Remainder.carriedWithin_exact`, `Remainder.carriedWithin_exact_of_no_loop`, `Remainder.finite_order_iff_no_loop` (without its listing of every condition) and `Remainder.Once.exact`.
  - **For every law.** `gap_within_order_iff`, through `most_difference_arrives`.
- `apply_docs.py` makes the following edits. It reads the bullet, rows, paragraphs and summaries from `docs.json`, which `make_docs_json.py` writes.
  - `Becoming.lean`: the import after `Becoming.Loops`, and the module bullet after Loops'.
  - `check_becoming.py`: `Becoming.Remainder` in the core list after `Becoming.Loops`, and a scope entry after Loops'.
  - The Lean README: one L4 row after Loops', and the within-layer imports.
  - The theory chapter:
    - §2: the paragraph "How a carried difference grows" no longer lists couplings that come and go as not derived; it points to `Becoming.Remainder`. A paragraph "What a cut loses (Part I)" follows it.
    - "Part I stated whole": one item after how a carried difference grows.
    - §8, the status row of the response as the dynamics give: the loops on couplings that come and go leave the open items; whether every schedule settles, and whether every loop of recurring couplings makes the most difference that can arrive run away, join them. The row's last clause, on its readings, is left as it stands.
    - §8, the further proofs under feedback and reach: couplings that come and go are given; how fast a runaway is stays open.
    - §9: one L4 row (58 theorems).
    - The glossary: rows "what a cut loses", "chain of couplings in time order" and "settled (schedule of couplings)" after "loop (of couplings)".
- The study gains a section, numbered 154, and its English paragraph (`study.md`, `study-en.md`; `apply_study.py`). Main holds §152 (P118) and §153 (the I4b-2 follow-up). The integrator numbers the section at landing.
- `apply_inventory.py` edits `DECIDABILITY-INVENTORY.py`. One theorem uses the equality of conditions only in its proof (`same`): `gap_within_order_iff`, through Propagation's `most_difference_arrives`. A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows. Its totals: proof-only 237 → 238; the others unchanged (417 dependent statements, 109 decidability-taking definitions).
- Records:
  - `make_record.py` writes the new schema-2 record what-a-cut-loses. Its proof references are hashed from the branch. `proof_bindings` is empty, and the record reads "receipt bound at landing".
  - `update_records.py` writes a paired note in how-a-carried-difference-grows, with one history note: loops whose couplings come and go leave next_delta (the new record's next step carries on what stays open), and related adds the new record. Its scope item saying that its equivalences need couplings at every step stays, because it still holds of its theorems; its correspondence keeps the readings Ren decided.

From `51dcf0dc`, copy `Remainder.lean` in. Then run `make_docs_json.py`, `apply_docs.py`, `apply_study.py`, `apply_inventory.py`, `update_records.py` and `make_record.py`, in that order, to write the content commit. Each script asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. If the section is not 154, renumber it with `python3 -B renumber_p120.py W N`. This changes the heading, the English paragraph, the record's scope and history, and the paired note.
2. Run the core checker, `check_becoming.py`. `Becoming.Loops` (its docstring changed in `51dcf0dc`), `Becoming.Remainder` and the root are new steps; Remainder and the root passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to what-a-cut-loses, one binding per proof reference, and rebind how-a-carried-difference-grows (its Loops.lean source changed in `51dcf0dc`). Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the two records, run on the branch, reports two errors. Both are expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

Every other finding is drift in 18 records, which step 4 reconciles: how-a-carried-difference-grows (`Loops.lean`, and the chapter's §2 and §8), and chapter drift in 17 more, scoped to the sections this changes (§2 and §8):
- comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, every-origin-passes-the-gate, how-much-difference-arrives, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units;
- lifting-where-branching-is-finite, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision, selection-through-a-model-of-the-options, sensitivity-is-the-least-registration, what-a-finite-history-refutes, where-a-move-is-formed.

The lint finds nothing in what-a-cut-loses; its texts are within every cap.

Nothing here runs Lean, edits the board or commits.

## History

- 16 October 2026: claimed after P118 was handed over. The module was built in scratch on P118's branch, then on main `271ab66a` with Ren's P118 readings applied (`929f66ab`). The kit was written there, and its scripts reproduced the branch bytes from a clean export of `929f66ab`. That head is kept as branch `p120-remainder-271ab66a` (`2a72060f`).
- 16 October 2026, regenerated: the I4b-2 follow-up took §153, so this section is §154. The branch was regenerated on main `e47a1ede`: Ren's P118 readings by rerunning `apply_ren_readings.py` (`51dcf0dc`, line for line the change of `929f66ab`; the cherry-pick conflicted only in the record's history, where the I4b-2 landing had added its reconciliation note), then `Remainder.lean` copied in and the six scripts rerun, unchanged except for the section number and this base. The module and root were rebuilt (119-module closure, empty axiom reports), the inventory rerun (the same one row; proof-only 237 → 238), and a clean export of `51dcf0dc` with the kit reproduced the branch bytes.
