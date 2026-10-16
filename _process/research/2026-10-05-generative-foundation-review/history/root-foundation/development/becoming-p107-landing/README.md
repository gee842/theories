# Landing package: the relation-first re-founding (P107)

从关系开始的重建的落地包。内容在分支 `p107-refounding`；本目录是写入内容与完成落地的脚本。

Ren, 14 October 2026: “why do we need "World"? … right now i think we are trapped by our speculative conditions”, then “please, finish all” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md)). The content commit `6a34f7b7` (on main `e678a801`) adds three core modules, `Becoming.Novelty`, `Becoming.Reading` and `Becoming.Readings` (66 theorems, 86 declarations, no existing module changed), the study section with its English paragraph, the chapter and plan text, the root imports and checker list, three schema-2 records and paired notes in four.

## Content, run once on `e678a801` in this order

These reproduce the content commit byte for byte (the three `.lean` files are copied in first).

1. `python3 -B apply_docs.py W`: the study section from `study-124.md` and `study-124-en.md`, the chapter, the zero-premise plan §1.4, the root module and the checker's core list.
2. `python3 -B update_records.py W`: the paired notes in imbalance-as-relatum, map-of-premises, process-and-frame-as-readings and contextual-registration.
3. `python3 -B make_records.py W`: returning-novelty-forgetting-on-levels, premises-read-off-the-exchange and unity-of-readings, each with “receipt bound at landing” until step 6 below.

## Landing, after the checker runs

`W` is the landing checkout, `N` P107's study section, `CORE` and `PERIPHERY` the run folders' `verification.json`, relative to `W`. Every replacement asserts the text it replaces, so a step run twice fails instead of applying twice.

1. `python3 -B renumber_p107.py W N`: integration I3a took study section 124 on main, so P107's own text (study heading and English paragraph, two citations in the chapter, two in the plan, its seven records) moves to `N`.
2. Claim the free checker slot on the board; `check_becoming.py`, then `check_correction_inquiry.py`, with `LEAN_TIMEOUT=3600`. The periphery run is needed because its last receipt predates `Becoming.Postponement` and P107 while chapter §9 says the core compiles there too.
3. `python3 -B land_p107_study.py W N CORE PERIPHERY`: the section's evidence lines name both runs; `DECIDABILITY-INVENTORY.py` classifies `upto_or_fails` (finitely many steps checked, a failing one found) as finding a step.
4. Regenerate `DECIDABILITY-INVENTORY.py` on the checked bytes, then the landing kit's `zero_count.py W`.
5. `python3 -B land_p107_docs.py W CORE PREV_UTC`: the chapter's §9 totals move from the receipt it names (`PREV_UTC`) to `CORE`, by pattern; the reading entry the-theory-of-becoming gains the re-founding and only then its source hash.
6. `python3 -B readme_p107.py W`: the Lean README rows for the three modules, the Imbalance row and the within-layer imports.
7. From `W`: `python3 -B bind_p107.py CORE N --list`, then `--write`. It binds every proof reference of the three new records to the run, rehashes references to the files this landing changed with a reason for each (the inventory's reason is read off the page before and after), and adds one paired note per changed record; any other drift is reported and left alone.
8. `research.py render`, the generativity-chain review of the changed sources, then the Lean and reading catalogues (last, since rendering changes what they index), and the checks: `research.py check`, the catalogue and chain checks, `make research-test`.

## History

- 14 October 2026: the first landing pass, on `6a34f7b7` with core receipt `20261014T150541.303546Z` (passed: 103 spine modules, 5444 theorems, 7625 declaration audits), is kept on branch `p107-landing-v1` (`9eb142c4`). It did not land: integration I3a took the checker slot next with the same study section number and the same shared files (root imports, checker list, §9 totals, inventory), so P107 lands after I3a with one combined run.
- 15 October 2026: the session's scratch copy of this kit was lost when `/private/tmp` was cleared at a restart. These files were rebuilt by replaying, in order, the session's recorded writes, edits and file-patching commands; the three content scripts were checked by reproducing `6a34f7b7` from `e678a801` byte for byte.

Nothing here runs Lean, edits the board or commits.
