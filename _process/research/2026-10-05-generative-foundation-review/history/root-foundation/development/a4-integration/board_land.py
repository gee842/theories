#!/usr/bin/env python3
"""A4 landed (19 October 2026): move A4's row from the live board to the history file (board rule 4), take A4 out of
the queue, and bring A4-L's row and queue place up to date. Links in the moved row are re-rooted for the history
file. Each edit must match exactly once. usage (from the repository root): python3 -B board_land.py LANDING_COMMIT"""
import sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
COMMIT = sys.argv[1]
board = Path(BOARD).read_text(encoding='utf-8')
history = Path(HISTORY).read_text(encoding='utf-8')


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


lines = board.split('\n')

# A4's row: its state cell records the landing; the row moves to the history file.
rows = [i for i, line in enumerate(lines)
        if line.startswith('| **A4: the readings and the open decisions, integrated into one account** ')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
decided = cells[2].split(' Chapter kit `apply_chapter.py`')[0]
assert decided.startswith('claimed 2026-10-19; decisions landed 2026-10-19 as docs'), decided[:80]
cells[2] = (decided + f' Chapter and records landed 19 October 2026 as `{COMMIT}` (docs and records, no checker run), '
            'rebuilt on main `421261da0` after N6, G5 and M4: the chapter, en + zh, by `apply_chapter.py` (M4\'s '
            'restatements matched as variants; in the zh, 静止 → 停息 in 113 places outside link targets and bare 生成 '
            'meaning becoming → 生成／变化); the records by `apply_records.py` (64 blocks in 26 records, 停息 in the live '
            'Chinese fields of 32, 54 records changed with one history note each); 122 records citing the chapter '
            're-pointed by `rehash_refs.py` after reading the change, none by rule (b). Rendered with 0 errors and 0 '
            'source drift; research-check, research-links, research-test and the lint ratchet pass; the Lean index '
            'pair kept at main\'s versions. N7 reapplies its blocks on this text; A4-L is its own row')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(last + 1, row)

# A4-L's row: state and workspace.
rows = [i for i, line in enumerate(lines) if line.startswith('| **A4-L: the family of ideals in the core** ')]
assert len(rows) == 1, rows
cells = lines[rows[0]].split(' | ')
assert len(cells) == 5, len(cells)
assert cells[2] == 'claimed 2026-10-19; reading the three originals', cells[2]
cells[2] = ('claimed 2026-10-19; core modules `Becoming.Ideals` (98 theorems: ideals of an order of stretches, refutable '
            'and closed classes with the two double-negation calibrations, the hull, avoidance, a lower set\'s order, '
            'the completion and its readings) and `Becoming.HistoryIdeals` (41: runs as the ideals of their stretches, '
            'with Horizon\'s laws as the case; words, histories and their order; settling ⇔ LPO on cut histories; '
            'classes of histories) scratch-built, every axiom report empty; the correspondence `IdealsCorrespondence` '
            '(92 theorems: W1, W2, W2a, A2, A2a, A3 and A4 from the core\'s laws, 41 declarations with empty reports, the '
            'rest naming their classical and extensionality steps) compiles clean under Lean 4.30.0-rc2 against them, '
            'with its checker `check_ideals_correspondence.py`; next: the kit, the record, a study section, chapter §2 '
            'and §9')
cells[3] = ('worktree `.claude/worktrees/a4l-ideals` (branch `a4l-ideals`); '
            '`_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a4l-ideals/`')
lines[rows[0]] = ' | '.join(cells)
board = '\n'.join(lines)

# The queue: A4 out, A4-L in before W2.
board = once(board, 'M4 landed, core receipt `20261019T004321.279483Z`): A4 (Claude Code session of 18 October, ',
             f'M4 landed, core receipt `20261019T004321.279483Z`; A4 landed as `{COMMIT}`, docs and records with no '
             'checker run): A4 (Claude Code session of 18 October, ')
start = board.index('): A4 (Claude Code session of 18 October, the readings in one account')
end = board.index('Then N7 (correction reading pass', start)
board = board[:start] + '): ' + board[end + len('Then '):]
board = once(board, ' Then W2 (this re-rooting\'s second batch',
             ' Then A4-L (Claude Code session of 18 October, the family of ideals in the core: two new core modules, '
             '`Becoming.Ideals` and `Becoming.HistoryIdeals`, with the CORE list, the scope text, the root import and '
             'the package README rows, and in the completion package the correspondence `IdealsCorrespondence` with '
             'its checker; scratch-built, core axiom reports empty; when its kit is ready it scratch-builds on main, '
             'runs the core checker and the correspondence checker, applies its record, study section and chapter '
             'text, re-points and renders; W2 may land ahead of it, and whichever lands second reruns its kit on the '
             'other\'s text). Then W2 (this re-rooting\'s second batch')
Path(BOARD).write_text(board, encoding='utf-8')
Path(HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('A4 row moved after history line', last + 1, '; queue and A4-L row updated')
