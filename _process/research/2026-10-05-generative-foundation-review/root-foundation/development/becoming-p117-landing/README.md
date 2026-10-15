# Landing package: weights count situations (P117)

权重计数情境的落地说明。内容在分支 `p117-situations`（基于 main `987e8c20`，I4c 之后；`6c62e13e` 之后核心的 Lean 没有改动，所以在 `6c62e13e` 上的暂存构建与清单照旧有效）的一个提交中。

Ren, 16 October 2026: “we are describing what everything obeys, but at every moment, the actual change depends on the situation … just saying we are all one doesn't make it true, the situation makes it true”, answering the AI's two readings of P116, with “can you see what to do with my clarification above?” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-the-situation-makes-it-true.md)). Claimed on the work board as P117 by Current math core (fork) [8277f2].

## Content

One commit on branch `p117-situations`. No theorem or declaration of an existing module changes.

- One new core module, L4:
  - `Becoming/Situations.lean` imports `Becoming.Typicality`: 13 theorems, 19 declarations.
  - `scratch_build.py` on `6c62e13e`:
    - every axiom report is empty and there are no warnings;
    - the root `Becoming` compiles with its closure, so no names clash;
    - all steps are stored in the shared cache.
- `Becoming/Parting.lean` and `Becoming/Typicality.lean`: only the readings in their module headers change, following Ren's clarification. Their declarations are unchanged (18/27 and 32/44), and both were rebuilt and audited in scratch.
- `Becoming.lean`: the import and a module bullet, after `Becoming.Typicality`.
- `check_becoming.py`:
  - the module in the core list, after `Becoming.Typicality`;
  - one scope paragraph, after Typicality's.
- The Lean README: one L4 row, and the within-layer import in both languages.
- The theory chapter:
  - a new paragraph pair after the P116 pair, whose readings are rewritten with Ren's words;
  - "Knowing" in "Part I stated whole";
  - the theory stated in full: one bullet in each language, and the bound item;
  - §8: a new status row after P116's, the identification reading under Ren's choices, and the open item "When the course branches";
  - §9: one spine row (13 theorems);
  - the glossary: one row.
- The study: section 144, provisional, with its English paragraph. Main holds §142 (I4c), and I4b-1 is landing as §143. The English paragraph of section 140 now reads "Section 140 adds" (it said 138, a leftover of P116's renumbering).
- `DECIDABILITY-INVENTORY.py`: `Situations.mul_indicator` joins `ITE_STATEMENTS`, since its statement names Lean's own `if` with its condition decided and no core definition.
  - A scratch run on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Totals on `6c62e13e`: statements depending on decidedness 367 → 368; proof-only 223 unchanged; the other classes unchanged.
- Records:
  - new schema-2 record weights-count-situations. Its proof references are hashed from the branch, `proof_bindings` is empty, and it reads "receipt bound at landing";
  - identification-where-runs-part and typicality-by-counting:
    - the AI's first readings are withdrawn (the parting one) or replaced (the chance one), with Ren's words of 16 October;
    - correspondence, next_delta and, for typicality, the first does_not_show item rewritten;
    - related gains weights-count-situations, and the 16 October source joins the references;
    - the Parting.lean and Typicality.lean references are rehashed (header only), so their receipt bindings need the new receipt;
    - one history note each, keeping the former wording.

## Ren took the readings (second commit)

Ren, 16 October 2026: “yes, i take those readings”. A second commit on the branch records this. It is docs only, and no declaration changes:

- the source file gains the message, and the directive line says the readings were taken;
- "pending Ren" becomes "taken by Ren" for these readings in:
  - the headers of Situations, Parting and Typicality, rebuilt and audited in scratch;
  - the three Lean README rows;
  - the chapter's two paragraph pairs, the two status rows and the identification item under Ren's choices, where the finite-name reading stays for Ren;
  - the three records' correspondence, whose next_delta drops Ren's judgment, each with a history note;
- study §144 gains "Ren's judgment" in both languages;
- the references are rehashed.

## Landing

`W` is the landing checkout.

1. Renumber the study section if 144 is taken: the heading, the chapter's link (`#144-…`), the English paragraph, and the three records' validation_scope and history.
2. Run the core checker, `check_becoming.py`. `Becoming.Situations`, `Becoming.Parting`, `Becoming.Typicality` and the root are new steps, and all passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to weights-count-situations, one binding per proof reference, and rebind identification-where-runs-part (Parting) and typicality-by-counting (Typicality, Parting) to the new receipt.
5. Rehash the study and chapter references this landing changed, with one reconciliation note per changed record.
6. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

What `research.py check` reports on the branch:

- Five errors, all expected before binding:
  - "recorded-checked needs proof source and existing receipt" and "needs a source hash binding", for weights-count-situations;
  - "receipt does not bind the reviewed proof source": once for identification-where-runs-part (Parting) and twice for typicality-by-counting (Typicality, Parting).
- Drift:
  - chapter drift in nine records, scoped to §3, §8, "the theory stated in full" and "Part I stated whole": continuous-time-as-tower, counts-exist-where-decided, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision and where-a-move-is-formed;
  - study drift in how-much-difference-arrives, scoped to the English summary (the paragraph appended after P115's, and the "Section 140" fix in P116's).

  Step 5 reconciles both.

The style lint finds nothing in the three records. Nothing here edits the board.
