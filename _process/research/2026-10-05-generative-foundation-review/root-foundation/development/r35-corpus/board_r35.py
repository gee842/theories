#!/usr/bin/env python3
"""R35: the board at landing. The Queue and receipts lines, the R28-R36 row's state, the ZH row's rebase note,
an R35b row for the ring left open, and R35's sub-row in the board history file after R34's. Each replacement
must occur exactly once. usage (from the checkout root): python3 -B board_r35.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
HIST = ROOT / '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'

QUEUE_OLD = ('- **Queue:** R35 at the head (corpus and records: the two approved goal-scope proposals applied, moves to '
             'history, record histories compacted, supersession, families, ID redirects, banners, agreement grade, '
             'instance ring); R34 landed (core receipt `20261020T005554.047169Z`).')
QUEUE_NEW = ('- **Queue:** empty; R35 landed (corpus and records, no Lean and no checker run, study §226; the instance '
             'and applications ring left as R35b); R36 next.')

RECEIPT_OLD = "the latest core receipt is R34's `20261020T005554.047169Z` (20 October 2026)."
RECEIPT_NEW = "the latest core receipt is R34's `20261020T005554.047169Z` (20 October 2026); R35 changed no Lean."

ROW_OLD = '476 of 11,401 apart); R35 next |'
ROW_NEW = ('476 of 11,401 apart); R35 landed (corpus and records, no Lean and no checker run, study §226, sub-row in '
           'the history file; 1,035 files moved to history unchanged, B6 `foundation-assessment` declared evidence in '
           'place, 281 record histories compacted with every note kept in a snapshot, 57 records re-roled off '
           'superseded modules, five law families, 17 record ids renamed with redirects (the four the chain names '
           'left), 40 round banners to history, agreements split by law level; the instance and applications ring '
           'left as R35b with its blocker); R36 next |')

ZH_OLD = '| claimed 2026-10-20 on `c21c62712` |'
ZH_NEW = ('| claimed 2026-10-20 on `c21c62712`. **R35 (landed 20 October), what to rebase onto:** (1) the law level is '
          'computed by `verify_mapping.py` and `verify_ro.py` (`law_level`, `level_split`, `level_line`, `LEVEL_ZH`: '
          'encoding where every cited declaration is in `Becoming.Hexagram`, general where none is, mixed), never '
          'stored in `passages.json`; `--table` prints the column 律的层次 after 关系, and the tables of '
          'YI-ZHUAN-AND-BECOMING (1) and CHINESE-SOURCES-AND-BECOMING (9) are spliced from it, so a new passage '
          'needs no level field; (2) 17 record ids renamed (receipt `_process/architecture/renames/R35-E4-renames.json`, '
          'former ids kept with redirect pages): `build_passages.py` maps them by its rename step after FIXES, so '
          'rebuild `passages.json` rather than edit ids by hand; (3) moved paths in `_process/architecture/moves/R35-B*.json` '
          '(the passage-map kits did not move; `research.py move` rewrote links in live files); (4) no passage-map '
          'declaration was renamed: the ring that would rebind them is R35b, which waits for your map work or your '
          'agreement |')

R35B_AFTER = '| R24 → the whole theory |\n'
R35B_ROW = ('| **R35b: the instance and applications ring** (twentieth review G11, G13; left by R35, '
            '[study §226](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#226-corpus-and-records-r35)). '
            "Split `Becoming.Commuting`'s `namespace Hexagram` section (the waxing and waning law as its instance) into "
            'an instance module, so the Hexagram chain is importer-free; ring the instances (`Hexagrams`, '
            '`HexagramPlaces`, `HexagramLaws`, `HexagramSites`, `HexagramSequences`, `PlaceTransitionNets`, the split '
            'section) and the applications nothing imports (`Dispatch`, `GuardHorizon`, `ResponseLearning`, '
            '`Coverage`, `ScopedReach`, `SeedReach`); `INSTANCES` and `APPLICATIONS` in `check_becoming.py` (Init-only, '
            'empty axiom reports) with an import-direction check; the catalogue and connectivity classes; records and '
            'passage-map declarations rebound; chapter §9 (EN, ZH); one core checker run. '
            '| unclaimed | open; blocked by the Commuting split (new Lean with its own checker run) and by ZH\'s work on '
            'the two passage maps whose declarations the ring would rebind: take it after ZH\'s maps land or with ZH\'s '
            'agreement | — | R35\'s re-derived membership → chapter §9, R36 |\n')

SUB_ROW = ('| **R35: corpus and records** (twentieth review step 2 with the two goal-scope proposals: E1-E5, E7, E8, '
           'E10, E13, G12; G11/G13 left as R35b). **Step 0** both approved proposals applied (target 1\'s formal part '
           'restated in the goal and theory-of-becoming-foundation; K1-K7 adopted as the completion criterion). '
           '**Moves** 1,035 files unchanged in six batches with receipts `R35-B*.json` (B1 14 chapter files, B2 the '
           'reference edition, B3 5 snapshot pages, B4 37 study files, B5 the kits of 82 landed items, 967 files, B7 '
           '11 reading notes), hashes verified; B6 `foundation-assessment` declared evidence in place. **E3** 281 of '
           '282 record histories compacted (13,485 → 3,472 notes, 10,294 bookkeeping notes condensed; each record\'s '
           'bytes snapshotted under `_process/architecture/history/`), `research.py compact-history`. **E8** 57 '
           'records re-roled off superseded modules (154 references, 162 bindings, 53 aliases). **E7** five law '
           'families, 24 records (`law-families.json`). **E4** 17 record ids renamed off retired labels with '
           'redirects (`research.py rename-id`; the four the chain names left). **E5** the Lean README\'s '
           'registration rows (41 EN, 46 ZH phrases). **E13** 40 round banners from 12 chapter files to history. '
           '**G12** agreements split by law level (Y1 52 = 33 encoding, 9 general, 10 both; RO 95 = 84 general, 4 '
           'encoding, 7 both). Worktree audit classified in the kit (20 merged, 7 merged with uncommitted entries, 5 '
           'unmerged with content on main, 3 needing a salvage ref); nothing removed. '
           '| Claude Code session of 20 October (R28-R36 programme) '
           '| landed 2026-10-20 on `0dc5ec1ad`: no Lean changed, no checker run (latest core receipt R34\'s '
           '`20261020T005554.047169Z`); render, check, links and tests pass; 23 chain sources made pending, read, left '
           'with the 97 before for one chain reading; study §226 '
           '| worktree `.claude/worktrees/agent-a4f6be12e5f674fff`, kit `development/r35-corpus/` '
           '| a corpus of current files, compacted records, families and redirects → R36 (the chapter rewrite); R35b (the ring) |\n')


def replace_once(text, old, new):
    assert text.count(old) == 1, old[:80]
    return text.replace(old, new)


b = BOARD.read_text()
b = replace_once(b, QUEUE_OLD, QUEUE_NEW)
b = replace_once(b, RECEIPT_OLD, RECEIPT_NEW)
b = replace_once(b, ROW_OLD, ROW_NEW)
b = replace_once(b, ZH_OLD, ZH_NEW)
b = replace_once(b, R35B_AFTER, R35B_AFTER + R35B_ROW)
BOARD.write_text(b)

h = HIST.read_text()
lines = h.split('\n')
i = next(k for k, l in enumerate(lines) if l.startswith('| **R34: one evaluative chain**'))
assert not any(l.startswith('| **R35: corpus and records**') for l in lines)
lines.insert(i + 1, SUB_ROW.rstrip('\n'))
HIST.write_text('\n'.join(lines))
print('board and history updated')
