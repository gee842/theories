# Landing package: how much difference arrives (P115)

差别到达多少的落地包。内容在分支 `p115-propagation`；本目录保存内容的文本与写入它们的脚本。

Six records left a measure of how much difference arrives, or of coupling, open: [counterfactual-is-the-course](../../../../../../theories/becoming/results/records/counterfactual-is-the-course.md) (P80; `Becoming.Counterfactual` lists “any measure of how much difference arrives” as not derived), [feedback-and-reach](../../../../../../theories/becoming/results/records/feedback-and-reach.md), [comparison-where-the-rest-responds](../../../../../../theories/becoming/results/records/comparison-where-the-rest-responds.md), [sensitivity-is-the-least-registration](../../../../../../theories/becoming/results/records/sensitivity-is-the-least-registration.md) (P113), [where-a-move-is-formed](../../../../../../theories/becoming/results/records/where-a-move-is-formed.md) (P109) and [levels-of-closure](../../../../../../theories/becoming/results/records/levels-of-closure.md); the theory chapter's §8 lists “a measure of coupling” among the further proofs under feedback and reach. Ren's goal of 12 October 2026: “move towards 100%, … pick the "What would move it most next" first” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), and “continue” on 15 October. Claimed on the work board as P115 by Current math core (fork 2) [6c0ec8].

## Content

One commit on branch `p115-propagation`, on main `416ff6b0` (after P114, I4a and P116). It changes no existing module.

- `Becoming/Propagation.lean`, a new core module (L4, imports `Becoming.Counterfactual` and `Becoming.TimedResponse`): 78 theorems, 97 declarations. `scratch_build.py` on `416ff6b0` gives every axiom report empty, with no warnings, and the root `Becoming` compiles with its 114-module closure, so no names clash. Both steps are stored in the shared cache. The module answers the question in five parts:
  - difference arrives as exchanged difference: in two balanced flows a condition's gap changes across a step by exactly the difference given less the difference taken (`levels_step_exact`, `gap_step`);
  - the coupling strength (`ExchangeLaw.RespondsWithin`, a coordinate-wise Lipschitz bound) is the measure of sensitivity: for a law of what has stood strength zero is insensitivity (`ExchangeLaw.insensitiveAt_iff_strength_zero`), strengths add up over levels changed one at a time (`ExchangeLaw.exchangeGap_le_strengths`), bounding a part's share of a move (`ExchangeLaw.exchangeGap_le_shares`), and a law giving the square of a level has no finite strength (`Propagation.Square.not_respondsWithin`);
  - every gap is at most the carried amount, the course the carrying law generates by Counterfactual's generation (`gap_le_carried`), and the carrying law attains it, so it is the most difference that can arrive (`most_difference_arrives`, an equivalence);
  - the carried amount is positive exactly along a route in time of positive strengths (`carried_pos_iff`), on routes of `TimedResponse.Spread` where the strengths are registered (`Conveyed.spread`); carried amounts add (`carried_add`);
  - witnesses: a unit relayed at twice its level arrives as 2t with no loop (`Propagation.Chain.keeps_arriving`), and a loop of strength one gives 2^t (`Propagation.Loop.runaway`).
- The name. The measure was first called "gain". P110's batch (P111) adds `Becoming.Gain`, where "gain/增益" means a family's stock rising, so the measure here is named "coupling strength / 耦合强度", the wording of levels-of-closure's scope ("does not measure the strength of coupling"). The module still mentions "incremental gains" once, as the systems-theory counterpart.
- `apply_docs.py` makes these edits, reading the bullet, rows, paragraphs and summaries from `docs.json` (written by `make_docs_json.py`):
  - `Becoming.lean`: the import at the end of the imports and the module bullet after the last;
  - `check_becoming.py`: `Becoming.Propagation` in the core list, before `Becoming.Relevance`, and a scope entry after Counterfactual's;
  - the Lean README: one L4 row after the last and the within-layer imports;
  - the theory chapter:
    - §2: a paragraph "How much difference arrives (Part I)" after that of the response as the dynamics give; in the paragraph of the comparison where the rest responds, "how much difference arrives" is no longer listed as not derived and points to `Becoming.Propagation`;
    - §6.10: the sentence that a common condition does not measure coupling gains what measures it (the AI's reading);
    - "Part I stated whole": one item after the response as the dynamics give;
    - §8: the status row of the response as the dynamics give (how much difference arrives moves out of the open items; a general theory of loops is added to them) and the further proofs under feedback and reach (how much difference arrives and a measure of coupling are given; a difference's routes in time noted; a general theory of loops stays open);
    - §9: one L4 row (78 theorems);
    - the glossary: rows "coupling strength" and "carried amount" after "reads finitely many conditions".
  
  New lines go at list ends, so modules landing first leave the anchors in place (P116 did, between the first draft and this commit).
- The study: a section, provisionally numbered 141, and its English paragraph (`study.md`, `study-en.md`; `apply_study.py`). Main holds §140 (P116); the integrator numbers the section at landing.
- `DECIDABILITY-INVENTORY.py` (`apply_inventory.py`):
  - `mixCells` mixes one history into another at listed levels, as `mixIn` does (`mix`); `mixCells_either`, `mixCells_listed` and `ExchangeLaw.exchangeGap_le_mixCells` name it in their statements;
  - nine theorems use the equality of conditions only in their proofs (`same`): the strength bounds, the carried bound and its attainment, and the two sensitivity equivalences.

  A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows. Its totals are: statements depending on decidedness 364 → 367; proof-only 214 → 223; decidability-taking definitions 96 → 97; the others unchanged.
- Records:
  - the new schema-2 record how-much-difference-arrives (`make_record.py`). Its proof references are hashed from the branch, `proof_bindings` is empty, and it reads "receipt bound at landing";
  - paired notes in the six records (`update_records.py`): each drops or narrows the answered item in next_delta, links the new record in related and adds one history note. Their scope items stay, because they still hold of those records' own theorems. In comparison-where-the-rest-responds the loop item's "gain" becomes "the strength around it"; in where-a-move-is-formed the item narrows to stating the part's share on that record's runs.

From `416ff6b0`, copy `Propagation.lean` in, then run `apply_docs.py`, `apply_study.py`, `apply_inventory.py`, `update_records.py` and `make_record.py` in that order to write the content commit. Each script asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. Renumber the study section: `python3 -B renumber_p115.py W N`. This changes the heading, the English paragraph, the record's scope and history, and the six paired notes.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Propagation` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to how-much-difference-arrives, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the seven records, run on the branch, reports two errors, both expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

Every other finding is chapter drift, scoped to the sections this changes (§2, §6, §8 and the glossary), in 12 records: comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision, sensitivity-is-the-least-registration and where-a-move-is-formed. Step 4 reconciles them.

The style lint finds nothing in the new record, nor in sensitivity-is-the-least-registration or where-a-move-is-formed. counterfactual-is-the-course, feedback-and-reach, comparison-where-the-rest-responds and levels-of-closure keep their earlier correspondence length warnings; this package does not touch correspondence.

Nothing here runs Lean, edits the board or commits.

## Coordination

P110 (`p110-frontier`, delegated readings, with P111 and P112) edits the chapter widely and the next_delta of counterfactual-is-the-course and sensitivity-is-the-least-registration. This package's replacements are disjoint substrings there, and its §6.10 sentence and §2 paragraph sit outside P110's rewrites of §8's list of Ren's choices. Whichever lands second reruns its scripts on the other's text.

## History

- 15 October 2026: claimed; module built in scratch on `56ccdc2a` (78 theorems).
- 16 October 2026: the measure renamed from "gain" to "coupling strength" after P111's `Becoming.Gain` was seen to use "gain" for a stock rising. The import narrowed from `Becoming.Sensitivity` to `Becoming.Counterfactual`, since nothing of Sensitivity is used. A docstring made constructively exact (sensitivity is that not every strength is zero). The package was prepared on P114's landing branch, then rebuilt on main `416ff6b0` after P114, I4a and P116 landed: module and root rebuilt, inventory rerun, numbers updated here.
