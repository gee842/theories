# Landing package: how a carried difference grows (P118)

所携带的差别怎样增长的落地包。内容在分支 `p118-loops`；本目录保存内容的文本与写入它们的脚本。

P115 left a general theory of loops open. [how-much-difference-arrives](../../../../../../theories/becoming/results/records/how-much-difference-arrives.md) lists “a general theory of loops (the strength around a loop and its runaway)” first in its next steps, and `Becoming.Propagation` lists it among what is not derived. [comparison-where-the-rest-responds](../../../../../../theories/becoming/results/records/comparison-where-the-rest-responds.md) and [runaway-distance-unregistered](../../../../../../theories/becoming/results/records/runaway-distance-unregistered.md) (P55) ask to define a loop in general and state a runaway as a theorem. The theory chapter's §8 lists the general theory of loops under feedback and reach. On 12 October 2026 Ren asked about patterns and loops: “there are so many patterns and loops but we can still find a way to to integrate so we can still calculate this effects but how how accurate can we do that uh what is the limitation do we have losses”. The goal that day was “move towards 100%” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). On 16 October Ren said “continue”. Current math core (fork 2) [6c0ec8] claimed this on the work board as P118.

## Content

One commit on branch `p118-loops`, on main `5f8f7726` (after I4b-2). It changes no existing module.

- `Becoming/Loops.lean` is a new core module. It sits in L4 and imports `Becoming.Propagation`. It has 113 theorems and 137 declarations. `scratch_build.py` on `5f8f7726` gives every axiom report empty, with no warnings. The root `Becoming` compiles with its 118-module closure, so no names clash. Both steps are stored in the shared cache. The module covers seven parts:
  - **Orders.** Order j (`carriedWithin`) is what routes of at most j responses carry, each order being the carried amount's own step taken on the order below (`carriedFrom`). The orders rise to the carried amount, and order j is exact up to step j (`carriedWithin_exact`).
  - **No loop upstream, a finite order is exact.** The module defines couplings (`Couples`), chains (`Coupled`), loops (`OnLoop`) and upstream (`Upstream`) on the positive strengths. Where no chain of j + 1 couplings ends at a condition, order j is exact there. With every condition listed, a chain as long as the list passes a loop: this is a pigeonhole argument through `revisits_within` (`loop_of_coupledInto`). So where no loop lies upstream, the order one less than the number of conditions is exact (`carriedWithin_exact_of_no_loop`).
  - **A loop upstream, every order misses.** This needs the couplings to hold at every step. A fed loop upstream then leaves every order inexact (`carriedWithin_lt_of_loop`). A finite order is exact from every start exactly where no loop lies upstream (`finite_order_iff_no_loop`). The hypothesis cannot be dropped: a loop coupled at the first step only leaves order one exact (`Loops.Once.not_always`).
  - **The strength around a loop.** Along a chain, what reaches the start arrives times the product of the strengths (`carried_along`). Around a loop, each time around multiplies it by at least one plus the product of the strengths (`carried_around`, `carried_runaway`).
  - **Accuracy of a cut.** Take starting gaps at most D and inflow at most M a step. Order j carries at most D·Σ_{i≤j} C(t,i)·M^i (`carriedWithin_le_withinBound`, `Loops.withinBound_eq`). The carried amount is at most D·(1+M)^t (`carried_le_geomBound`). A cut at order j misses at most the difference (`carried_le_carriedWithin_add`). A self-loop attains all three (`Loops.SelfLoop.attained`).
  - **Polynomial exactly where no loop lies upstream.** With no loop upstream the carried amount is at most a polynomial (`carried_le_polynomial`). Now take stationary strengths with the same formations at every step. Then every loop at least doubles what reaches it (`carried_doubles_around`, `carried_doubles_into`), and a doubling outgrows every polynomial (`Loops.not_poly_of_doubling`). So a polynomial bound holds exactly where no loop lies upstream (`polynomial_iff_no_loop`).
  - **For every law.** Through `most_difference_arrives` and `gap_le_carried` the results extend to every law with the strengths. The theorems are `most_difference_within`, `gap_le_polynomial` and `gap_polynomial_iff_no_loop`.
- `apply_docs.py` makes the following edits. It reads the bullet, rows, paragraphs and summaries from `docs.json`, which `make_docs_json.py` writes.
  - `Becoming.lean`: the import after `Becoming.Propagation`, and the module bullet after Propagation's.
  - `check_becoming.py`: `Becoming.Loops` in the core list after `Becoming.Propagation`, and a scope entry after Propagation's.
  - The Lean README: one L4 row after Propagation's, and the within-layer imports.
  - The theory chapter:
    - §2: Propagation's paragraph no longer lists a general theory of loops as not derived; it points to `Becoming.Loops`. A paragraph "How a carried difference grows (Part I)" follows it.
    - "Part I stated whole": one item after how much difference arrives.
    - §8, the status row of the response as the dynamics give: the general theory of loops leaves the open items, and loops whose couplings come and go join them. The row's last clause, on its readings, is left as it stands.
    - §8, the further proofs under feedback and reach: the general theory of loops is given; loops whose couplings come and go, and how fast a runaway is, stay open.
    - §9: one L4 row (113 theorems).
    - The glossary: rows "order (of the carried amount)" and "loop (of couplings)" after "carried amount".
- The study gains a section, numbered 152, and its English paragraph (`study.md`, `study-en.md`; `apply_study.py`). Main holds §146–§151 (I4b-4, P110–P112, P119 and I4b-2). The integrator numbers the section at landing.
- `apply_inventory.py` edits `DECIDABILITY-INVENTORY.py`. Three theorems use the equality of conditions only in their proofs (`same`): `most_difference_within`, `gap_le_polynomial` and `gap_polynomial_iff_no_loop`. They use it through Propagation's `gap_le_carried` and `most_difference_arrives`. A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows. Its totals: proof-only 234 → 237; the others unchanged (409 dependent statements, 109 decidability-taking definitions).
- Records:
  - `make_record.py` writes the new schema-2 record how-a-carried-difference-grows. Its proof references are hashed from the branch. `proof_bindings` is empty, and the record reads "receipt bound at landing".
  - `update_records.py` writes paired notes in three records, each with one history note:
    - how-much-difference-arrives: the general theory of loops leaves next_delta, and the related note on comparison-where-the-rest-responds now points to the new record.
    - comparison-where-the-rest-responds: the item narrows to loops under laws with no finite coupling strength.
    - runaway-distance-unregistered: the item becomes connecting its policies to loops.

    Their scope items stay, because they still hold of those records' own theorems.

From `5f8f7726`, copy `Loops.lean` in. Then run `make_docs_json.py`, `apply_docs.py`, `apply_study.py`, `apply_inventory.py`, `update_records.py` and `make_record.py`, in that order, to write the content commit. Each script asserts the text it replaces, so a second run fails.

The scripts apply unchanged on `5f8f7726`, after P110–P112, P119 and I4b-2 landed. Two anchors stop before the clause that follows them: P110 rewrote the last clause of the §8 status row (its readings) and removed the item after the loops item in comparison-where-the-rest-responds' next step.

## Landing

`W` is the landing checkout.

1. If the section is not 152, renumber it with `python3 -B renumber_p118.py W N`. This changes the heading, the English paragraph, the record's scope and history, and the three paired notes.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Loops` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to how-a-carried-difference-grows, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the four records, run on the branch, reports two errors. Both are expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

Every other finding is chapter drift in 17 records, scoped to the sections this changes (§2 and §8). Step 4 reconciles them. The records are:
- comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, every-origin-passes-the-gate, how-much-difference-arrives, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units;
- lifting-where-branching-is-finite, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision, selection-by-the-record-alone, sensitivity-is-the-least-registration, what-a-finite-history-refutes, where-a-move-is-formed.

Nothing here runs Lean, edits the board or commits.

## History

- 16 October 2026: claimed after P115 landed. The module was built in scratch, then rebuilt on main `064c8add` after P117 landed. The module and root were rebuilt, the inventory rerun, and the numbers updated here. The self-loop witness namespace is `Loops.SelfLoop`; it was first drafted as `Loops.Single`. `Loops.Once` was added so that the equivalences' need for couplings at every step is a theorem, not a remark.
- 16 October 2026, later: I4b-3 landed as study §145 while this waited, and P110–P112 were handed over with provisional §146–§148, so this section became provisional §149, and then §151 once I4b-4 took §146 and P119 asked for §150. The scripts were rerun on main `a5406334` (the module and root rebuilt, the inventory rerun: the same three rows and totals), and two anchors were narrowed so that the scripts also apply on `p110-frontier`.
- 16 October 2026, regenerated: I4b-2 took §151, so this section is §152. The package was regenerated on main `5f8f7726`, after P110–P112, P119 and I4b-2 landed: `Loops.lean` copied in and the six scripts rerun, unchanged except for the section number and this base. The module and root were rebuilt (118-module closure) and the inventory rerun (the same three rows; proof-only 234 → 237). The previous head, on `a5406334`, is kept as branch `p118-loops-a5406334`.
- 16 October 2026, after landing: Ren decided the three readings ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md)): the first in the AI's wording, the second as right with its qualifiers, the third in a refined form for now. `apply_ren_readings.py` applies them on main `271ab66a`. It changes the readings in `Loops.lean`'s module docstring (comments only), the chapter's §2 paragraph, and how-a-carried-difference-grows (correspondence, next_delta, the source as a provenance reference and one paired history note). It also adds a dated paragraph to study §152 and a bullet to its English paragraph. Hashes of the changed sources are reconciled at landing, with the core checker compiling `Becoming.Loops` again.
