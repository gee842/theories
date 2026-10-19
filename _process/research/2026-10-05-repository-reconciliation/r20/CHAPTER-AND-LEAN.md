# R20(b): the chapter and the Lean say exactly what the Lean shows

19 October 2026. This is board item R20(b), which follows up the [review of 19 October](../whole-repo-review-2026-10-19.md); R19 already applied that review's fixes. Each finding is answered by wording only. No statement, proof or claim changed, and no Lean was checked here.

## What changed

1. **Instantiation, not derivation.** `Unrestricted sig := Neutral (…)` and `Neutral rule := ∀ i, rule i`. The consequences under the condition are therefore instantiations of a universal statement, and the theorem counts measure uses of it, not further dependence. The condition gives significance to everything and orders no mixed part (`Transfer.unordered`). Every narrowing loses something, including predation, apoptosis and the ending of a cancer. Ranking comes from C (widening called better) and from the step of invariance. Where this is stated:
   - Chapter (en and zh): the status block, target 2, item 10, the premise card (continuation condition and living significance rows) and §5.
   - Chapter §6: the intro on counts, §6.1, §6.8, a new paragraph in §6.15 ("What the condition adds, exactly" / 条件确切加了什么), the whole statement IV, §7.5, §8.5 and the glossary.
   - AGENTS.md, Scope: the ethics may not be said to "derive" from the condition without this.
   - Records: one-axiom-yields-g0.
2. **`bounded_rival` and `Web.significance_undetermined`.** The rival being consistent with every law is meta-theoretic: significance is not a field of `World`, `Web` or `Flow`, and the theorem proves only its two parts. `significance_undetermined` evaluates only the two constants, true of everything and true of nothing. Where this is stated:
   - Chapter (en and zh): item 10, the premise card, §5, §6.8, §6.15 and the whole statement III.
   - Lean: the `Significance.lean` docstrings.
3. **Whole-number dependence.** The rest laws (`World.rests_unrefuted`, `World.rests_unrefuted_enclosed`, `World.comes_to_rest_unrefuted`) and `Flow.fed_from_beyond` use `Flow.DissipatesOn` with natural-number amounts. With real amounts, losses can shrink geometrically and the conclusions fail, and the second law gives no least loss per step. Where this is stated:
   - Chapter (en and zh): items 4 and 6, the premise card (a new zh row 表示 | 自然数的量), §1 Rest, §6.7, the whole statement II and §8.6.
   - Records: continuing-self-fed-from-beyond and continued-change-needs-openness.
4. **Definitional laws.** In the chapter (en and zh):
   - `change_readings` is proved by `Iff.rfl` (item 2).
   - `keep_pace` is an arithmetic fact (whole statement I).
   - `selects_alike_iff` and `selects_alike_all_iff` hold by construction (§3, §4 table, §7.1, glossary).
   - `aboveAll_unique` is immediate from the definition of a strict maximum (§3, §7.2).

   In the Lean, the `Selection.lean` docstring of `selects_alike_iff` and the `Significance.lean` docstrings of `paths_comparison_widens` now say this too.
5. **`law_iff_em` is a lemma.** The need for excluded middle comes from activity being a proposition: `World.undecided` makes an arbitrary proposition a relatum's activity at one step. So the equivalence is a lemma of the decided law and says nothing further about change. Where this is stated:
   - Chapter (en and zh): item 2, §1, "The deepest part" and §8.6.
   - Records: space-and-its-parts, counts-exist-where-decided and recurrence-without-decidedness.
6. **Witnesses.** `Pair.own_not_joint`, `Clearing.loses_beyond` and `Clearing.free_rider_loses` are marked as witnesses for "can" claims in one constructed world. Where (en and zh): §2 (two places), §6.7, §6.8 and §6.15.
7. **Pure core.**
   - What is now stated:
     - The core imports only Lean's `Init`.
     - An empty axiom report means no `propext`, `Quot.sound` or `Classical.choice`.
     - Constructivity needs only the absence of `Classical.choice`, so the core is stricter than constructive.
     - The report concerns logic only, not modelling choices (discrete steps, natural-number amounts, Prop-valued activity).
   - Where: AGENTS.md (the pure-core bullet, plus a revision line with a [before copy](../../../history/2026-10-19-instructions/AGENTS-before-pure-core-precision.md)), the chapter status block, the premise card, "What no axiom means", §8.6 and §9.
8. **§8.9 Objections not yet answered** (en §8.9, anchor `89-objections-not-yet-answered`; zh 尚未回答的反对). Each objection says what would answer it:
   - agent-relative reasons and partiality (Williams);
   - why "anything" has significance;
   - the externalism of A;
   - graded, prioritarian and deontic views are not modelled;
   - which learned function, misgeneralization and deception;
   - the internal-relations thesis is open;
   - every review so far is by AI.

   §6.2 points to the section.
9. **"Positively relevant" docstrings**, R19's open item, in seven files:
   - `Becoming.lean`, `ActiveReading.lean`, `Handoff.lean`, `Metaethics.lean`, `PositiveGround.lean`, `Relevance.lean` and `ScoreRepresentation.lean`.
   - `positive` stays as the name of G0's parameter, as in R19, and the docstrings say that the name carries no valence.
10. **NONDUAL-METHOD.md.** "Formation" now names any forming. "Generative" is the narrower term: generation and degeneration do not overlap.
    - The heading reads "Begin within the one unfolding".
    - The old anchor `begin-within-generative-unfolding` is kept, because the generativity chain links it.
11. **Record titles saying "registration".** None remain. The N5 and N6 passes had already given every title the adopted vocabulary, so nothing changed.

## Lean files whose bytes changed

All edits are comment or docstring only. The script `delims.py` (scratch) found the `/-` and `-/` counts unchanged in every file, and the code was identical after removing comments. The files are under `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/`:
- `Becoming.lean`
- `Becoming/ActiveReading.lean`
- `Becoming/Handoff.lean`
- `Becoming/Metaethics.lean`
- `Becoming/PositiveGround.lean`
- `Becoming/Relevance.lean`
- `Becoming/ScoreRepresentation.lean`
- `Becoming/Selection.lean`
- `Becoming/Significance.lean`

## Left alone, and why

- The Lean docstrings of `change_readings`, `keep_pace` and `aboveAll_unique` were already accurate; only the chapter overstated them.
- The chapter already called `paths_comparison_widens` definitional (premise card row C, §6.13).
- `Space.lean`'s docstring of `law_iff_em` is unchanged, which keeps one more receipt-bound file stable. The records and the chapter carry the lemma reading.
- These were left as they are:
  - "positive" where it is G0's parameter name, a numeric sign or A's parameter;
  - the analogy to `law_iff_em` in relata-counted-up-to-indiscernibility.

## Drift

- **Markdown, re-pointed.** [`rebind_r20b.py`](rebind_r20b.py) re-pointed 11 records whose cited lines in the chapter or the method changed:
  - bounded-census-keeps-pace, census-balance, counting-standing-and-dependence, identity-across-steps, laws-of-one-step, loss-beyond-a-region, recurring-reference-revision, seeking-boundary, significance-retained-within-margin, target-capture and whole-first-and-bounded-centers.

  Each was read against the changed lines with `../r19/drift_lines.py`, and no claim rests on wording that changed. Each got a dated note in English and Chinese.
- **Lean, left drifting on purpose.** 53 references in 40 records cite the nine Lean files above. Their records bind proof receipts, so they are re-pointed only after the integrator's checker run produces a receipt for the new bytes.
- **Generated files, restored.** The render also changed the following, and all were restored before commit:
  - the Lean index (`LEAN-INDEX.md`, `data/lean-index.json`, `lean-declarations/becoming-core.md`), which follows the Lean bytes;
  - `_process/research/README.md` (the counts for this folder);
  - `_process/architecture/generated-manifest.json`.

  The landing render regenerates them. The record pages (`.md`) of the changed records are committed so that each matches its JSON.
- **The generativity chain** fingerprints `NONDUAL-METHOD.md` and is not edited here. That fingerprint now differs, alongside many older ones that `generative_chain.py --changes` already lists. Reconciliation goes through the chain's maintenance record.
