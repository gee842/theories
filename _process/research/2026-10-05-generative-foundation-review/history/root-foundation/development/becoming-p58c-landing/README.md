# P58c landing kit: the rest family named by strength

Ren, 12 October 2026, to the AI's analysis: “agree with you” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-rest-family-strengths.md)). Prepared by the integrator (Universal Metaethical Core). The study section of the landing gives the argument and the author's counterreview.

Three strengths of “it stops”, each stronger than the next: (a) from some step on nothing happens (`World.RestsFrom N` for a world); (b) that cannot be refuted (`¬¬∃N, RestsFrom N`); (c) it does not recur. (a) is not proved: for every finite world meeting the premises it gives LPO (`World.lpo_of_finite_ends`).

## Rename map

Read from the declarations of main and of the patched tree (`namemap_p58c.py`, output `namemap.json`). Statements marked (b) were strengthened from (c); statements marked (c) are unchanged.

| Module | Before | Now | Strength |
|---|---|---|---|
| Change | `falls_finitely_from_floor` | `falls_not_recurring_from_floor` | (c) does not recur |
| Dissipation | `Flow.taking_ceases_from` | `Flow.taking_not_recurring_from` | (c) does not recur |
| Dissipation | `Flow.Balances.taking_ceases` | `Flow.Balances.taking_not_recurring` | (c) does not recur |
| Dissipation | `Flow.taking_ceases_within` | `Flow.taking_not_recurring_within` | (c) does not recur |
| Dissipation | `Flow.Dissipative.finite_ceases` | `Flow.Dissipative.finite_taking_not_recurring` | (c) does not recur |
| Dissipation | `Flow.rising_ceases_from` | `Flow.rising_not_recurring_from` | (c) does not recur |
| Dissipation | `Flow.standing_ceases_from` | `Flow.standing_not_recurring_from` | (c) does not recur |
| Dissipation | `Flow.rising_ceases_on` | `Flow.rising_not_recurring_on` | (c) does not recur |
| Dissipation | `Flow.standing_ceases_on` | `Flow.standing_not_recurring_on` | (c) does not recur |
| Dissipation | `Flow.rising_ceases` | `Flow.rising_not_recurring` | (c) does not recur |
| Dissipation | `Flow.standing_ceases` | `Flow.standing_not_recurring` | (c) does not recur |
| Dissipation | `Flow.Dissipative.one_ceases` | `Flow.Dissipative.one_taking_not_recurring` | (c) does not recur |
| Generation | `Web.depletes_finitely` | `Web.depletion_not_recurring` | (c) does not recur |
| Generation | `Web.dissipation_ceases` | `Web.dissipation_generation_not_recurring` | (c) does not recur |
| Interdependence | `Flow.Balances.unfed_consumption_stops` | `Flow.Balances.unfed_consumption_not_continuing` | (c) does not recur |
| Listing | `World.Enumerated.rests` | `World.Enumerated.not_recurring` | (c) does not recur |
| Listing | `Flow.taking_stops_listing` | `Flow.taking_not_recurring_listing` | (c) does not recur |
| Listing | `Web.generation_ceases_listing` | `Web.generation_not_recurring_listing` | (c) does not recur |
| Listing | `Flow.Dissipative.finite_ceases_listing` | `Flow.Dissipative.finite_taking_not_recurring_listing` | (c) does not recur |
| Openness | `Flow.stills_from` | `Flow.change_not_recurring_from` | (c) does not recur |
| Openness | `Flow.stills` | `Flow.change_stops_unrefuted_around` | (b) cannot be refuted |
| Openness | `Flow.exchanges_finitely_from` | `Flow.exchange_not_recurring_from` | (c) does not recur |
| Openness | `Flow.exchanges_finitely` | `Flow.exchange_not_recurring_around` | (c) does not recur |
| Openness | `World.arising_stops_from` | `World.arising_not_recurring_from` | (c) does not recur |
| Openness | `World.arising_stops` | `World.arising_stops_unrefuted` | (b) cannot be refuted |
| Openness | `World.comes_to_rest_from` | `World.comes_to_rest_unrefuted_from` | (b) cannot be refuted |
| Openness | `World.comes_to_rest` | `World.comes_to_rest_unrefuted` | (b) cannot be refuted |
| Openness | `World.Finite.comes_to_rest` | `World.Finite.comes_to_rest_unrefuted` | (b) cannot be refuted |
| Openness | `World.rests_around` | `World.rests_unrefuted_around` | (b) cannot be refuted |
| Openness | `World.rests_enclosed` | `World.rests_unrefuted_enclosed` | (b) cannot be refuted |
| Openness | `Few.quiet` | `Few.coming_not_recurring` | (c) does not recur |
| Openness | `World.exchange_stops` | `World.exchange_not_recurring` | (c) does not recur |
| Openness | `World.hatch_rests` | `World.hatch_rests_unrefuted` | (b) cannot be refuted |
| Premises | `World.premised_rests` | `World.premised_rests_unrefuted` | (b) cannot be refuted |
| Recurrence | `Marks.change_stops` | `Marks.change_not_recurring` | (c) does not recur |
| Recurrence | `Run.change_stops` | `Run.change_not_recurring` | (c) does not recur |
| Renewal | `falls_finitely` | `falls_not_recurring` | (c) does not recur |
| Renewal | `Conditions.drawdown_finite` | `Conditions.drawdown_not_recurring` | (c) does not recur |
| Reserve | `Web.active_finitely_from` | `Web.active_not_recurring_from` | (c) does not recur |
| Reserve | `Web.Carries.active_finitely` | `Web.Carries.active_not_recurring` | (c) does not recur |
| Reserve | `Web.arising_finitely_from` | `Web.arising_not_recurring_from` | (c) does not recur |
| Reserve | `Web.Carries.arising_finitely` | `Web.Carries.arising_not_recurring` | (c) does not recur |
| Resolution | `Flow.taking_stops` | `Flow.taking_not_recurring` | (c) does not recur |
| Resolution | `World.rests_of_after` | `World.rests_unrefuted_of_after` | (b) cannot be refuted |
| Resolution | `World.rests_unrefined` | `World.rests_unrefuted_without_refinement` | (b) cannot be refuted |
| Resolution | `World.rests_refinement_counted` | `World.rests_unrefuted_refinement_counted` | (b) cannot be refuted |
| Resolution | `World.rests_at_resolution` | `World.not_recurring_at_resolution` | (c) does not recur |
| Resolution | `Trickle.exchange_stops` | `Trickle.exchange_not_recurring` | (c) does not recur |
| Roles | `Web.generation_ceases_from` | `Web.generation_not_recurring_from` | (c) does not recur |
| Roles | `Web.generation_ceases_on` | `Web.generation_not_recurring_on` | (c) does not recur |
| Roles | `Web.generation_ceases` | `Web.generation_not_recurring` | (c) does not recur |
| Sampling | `World.sample_rests` | `World.sample_rests_unrefuted` | (b) cannot be refuted |
| Space | `World.rests_covering` | `World.rests_unrefuted_covering` | (b) cannot be refuted |
| Space | `World.rests` | `World.rests_unrefuted` | (b) cannot be refuted |

## Added

| Module | Declaration |
|---|---|
| Locality | `ceasing_steps_unrefuted` |
| Locality | `Covers.ceasing_stops_unrefuted` |
| Resolution | `World.restsFrom_of_after` |
| Space | `World.RestsFrom` |
| Space | `World.rests_unrefuted_iff` |
| Space | `World.not_recurring_of_rests_unrefuted` |

`Covers.ceasing_not_recurring`, `Covers.not_not_coming_from` and `World.arising_unrefuted_covering` keep their names; the last two take the weaker hypothesis that ceasing after every step cannot be refuted.

## Order

1. After the preceding packages have landed, run `python3 -B apply_latest.py ROOT --check` from this directory, then the same command with `--apply`. The script merges each supplied module against its verification base `9a70ff1a`, preserving later changes and stopping on conflict before writing any source. It applies the identifier map to current modules and adapts P77's two uses of `World.rests` through `World.not_recurring_of_rests_unrefuted`. P77's `Enumerated.rests` statement is unchanged. Use `--output-tree TREE` to prepare a scratch overlay instead. None of these preparation modes is a proof check.
2. Run both consolidated checkers on the patched worktree, with no unrelated module addition in this run. Then use `LAND_WT=ROOT zsh land_p58c.sh`: spec, documents (`p58c_docs.py`), records (`p58c_records.py`), inventory, repoint, module counts, generators, guarded hash refresh (`p58c_refresh.py`), checks. The script uses the retained [P58b repoint helper](../becoming-p58b-landing/repoint.py) and [module-count helper](../becoming-p58b-landing/modcounts.py), and does not need the old temporary Claude workspace. The source preparation and landing steps commit nothing.

The spec checks both receipts against the current sources and requires exactly five added theorems and six added source
declarations, with no change to the module set. The landing applies only the identifier map to the current inventory
classifier (`inventory_names.py`, normally a no-op), preserves all newer categories, regenerates the inventory, and
updates the plan with the shared [generic count helper](../becoming-landing-kit/zero_count.py). The study section,
affected-record count and landing date are read from the current study, records and receipt; the authorization remains
dated 12 October. After the current queue and Entropy the section is expected to be 111, not hardcoded.

The original construction scripts are retained as provenance: `tokens_p58c.py`, `tokens2_p58c.py` (renames), `hand_p58c.py`, the three `openness` scripts, `docs_lean_p58c.py`, `resolution2_p58c.py`, and the two `wrap` scripts. Space and Locality were edited by hand; `lean/Becoming/` preserves the complete verified package. Do not replay the construction scripts over newer sources instead of reconciling with `apply_latest.py`.

The current map has 54 names: 15 strengthened statements and 39 unchanged non-recurrence statements. The original
package's 50 names / 35 pure renames are historical counts. P77 added four rest-family names after that package was
prepared; their statements are unchanged and now named for non-recurrence. Qualified-name resolution keeps
`World.rests` distinct from `World.Enumerated.rests`, and leaves Learning's unrelated rest names alone.

If the original P58c preparation has already been applied, run `python3 -B finish_listing.py ROOT` before checking
again. It applies only the four Listing names, their precise docstrings, the missed receiver call
`dissipative.finite_ceases` → `dissipative.finite_taking_not_recurring`, and the stale backticked `rests` reference in
Space. The latter docstring is also corrected in this package's Space source. Original source bytes remain in the
package's earlier Git revision; no theorem proposition changes in this finishing step. The first takeover check
found the missed receiver call; that failed run remains failed evidence, not a successful validation.

History, frozen packages, sources, reviews, record history and scopes of older receipts keep the names of their time;
this map translates them. Scopes citing the immediately preceding core receipt receive the current names before their
receipts are advanced. Changed documentary claims and names receive a current UTC review timestamp, without claiming
an independent proof review. The OPENING footnote cites `World.rests_enclosed` and is changed only with Ren.

## Package status

Verified in scratch on 12 October 2026 with `scratch_build.py` against main `9a70ff1a` (P69 in): 18 core modules, 1,466 theorems among them, every axiom report empty, no warnings. `lean/Becoming/` holds the patched modules. Documents and records were dry-run up to rendering on that main with stand-in receipts; rendering needs the real receipts. The package lands last in the current queue (work board), after rebasing the Lean onto whatever has landed by then.

13 October takeover preparation: the 18 current source modules still match the recorded base before P58c; the new merge preparation passes without touching them. The P73 `Learning` and P83 `Identification` rest names are distinct and kept. The retained package's old-name map is empty after preparation. This is preparation evidence only; the final integrated source requires the integrator's actual checker receipts. The Chinese term, informal heading, and substantive OPENING footnote wording retain their recorded decision scope.

Final preflight after P86–P88: every targeted chapter/Lean-README prose anchor and every record prose replacement still
matches the current source. The inventory classifier already uses no renamed identifier; the preparation leaves its
new categories intact. `Listing` needs the two consequence adapters, while Entropy's `falls_finitely` and two
`Marks.change_stops` uses are pure renames covered by `apply_latest.py`. This preflight runs no proof checker.

The subsequent Listing finishing step was exercised on copied current Listing and Space files and is idempotent.
Qualified dispatch distinguishes both renamed `rests` declarations and preserves unrelated names. A copied-record
rehearsal corrected all 19 current records, including Listing's explicit balance, dissipation and embodied-arising
premises; it renamed scopes bound to the current predecessor receipt while preserving a deliberately older scope and
every prior history entry. These are integration checks only; the integrator runs the actual proof check afterward.
