# Landing package: identification where runs part, and typicality by counting (P116)

运行分开之处的辨识与计数中的典型的落地说明。内容在分支 `p116-separating`（基于 main `07b4316e`，I4a 之后；I4a 不改 Lean，所以对 `b34b8027` 的暂存构建与清单照旧有效）的一个提交中。

Ren, 15 October 2026: “"What this line doesn’t reach" is also worth doing”, with what Ren means by the core and the request to keep a note where earlier words are unreasonable ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-15-situational-and-the-whole-core.md)). Claimed on the work board as P116 by Current math core (fork) [8277f2].

## Content

One commit on branch `p116-separating`. No existing Lean module changes.

- Two new core modules, both L4:
  - `Becoming/Parting.lean` imports `Becoming.Distinguishing`: 18 theorems, 27 declarations;
  - `Becoming/Typicality.lean` imports `Becoming.Identification` and `Becoming.Weighted`: 32 theorems, 44 declarations.
  - `scratch_build.py` on `b34b8027` (after P114):
    - every axiom report is empty and there are no warnings;
    - the root `Becoming` compiles with its closure, `Becoming.Courses` included, so no names clash;
    - all steps are stored in the shared cache.
- `Becoming.lean`: the two imports and two module bullets, after `Becoming.Courses`.
- `check_becoming.py`:
  - both modules in the core list, after `Becoming.Courses`;
  - two scope paragraphs, after Learnable's.
- The Lean README: two L4 rows, and the within-layer imports in both languages.
- The theory chapter:
  - §6: a new paragraph pair after the learnable pair;
  - §6.10 "Knowing" in "Part I stated whole";
  - the theory stated in full: one bullet in each language, and the bound item qualified;
  - §8: a new status row after identification, the identification reading under Ren's choices, and the further proofs under "When the course branches";
  - §9: two spine rows (18 and 32 theorems);
  - the glossary: three rows.
- The study: section 140, with its English paragraph. Main holds §139 (I4a). If another section lands first, renumber the heading, the chapter's link, and the three records' scope and history.
- `DECIDABILITY-INVENTORY.py`: `Parting.unparted_iff` and `Parting.free_open` use decided values only in their proofs (`same`), with forms that need no decision.
  - A scratch run on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Totals on `b34b8027`: statements depending on decidedness 363 → 364 (`Parting.leastBound_right`, through `leastBound`); proof-only 212 → 214; the other classes unchanged.
- Records:
  - new schema-2 records identification-where-runs-part and typicality-by-counting. Their proof references are hashed from the branch, `proof_bindings` is empty, and each reads "receipt bound at landing";
  - identification-where-bounded:
    - next_delta now asks Ren about the finite-name reading, and about ‘situationally’ with its qualification;
    - correspondence notes that Ren did not take reading 1;
    - related gains identification-where-runs-part;
    - the sixteenth law's ‘costing a whole turn’ now reads ‘taking a whole turn’;
    - one history note.

## Landing

`W` is the landing checkout.

1. Renumber the study section if 140 is taken.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Parting`, `Becoming.Typicality` and the root are new steps, and all passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to the two new records, one binding per proof reference.
5. Rehash the study and chapter references this landing changed, with one reconciliation note per changed record.
6. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

What `research.py check` reports on the branch:

- Four errors, all expected before binding:
  - "recorded-checked needs proof source and existing receipt", once for each new record;
  - "needs a source hash binding", once for each new record.
- Chapter drift in nine records: continuous-time-as-tower, counts-exist-where-decided, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision and where-a-move-is-formed. The drift is scoped to §8, "the theory stated in full" and "Part I stated whole", and step 5 reconciles it.

`make research-test` fails only on those four expected errors. The style lint finds nothing in the two new records. Nothing here edits the board.
