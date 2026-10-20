#!/usr/bin/env python3
"""A2: the board edits, as exact replacements on a board file. `queue` puts A2 at the end of the landing queue and marks
its row ready. `land` removes A2's row and its queue item from the board, notes the landing in the queue's
heading, and adds the landed row to the end of the
history file's table of rows landed after the board was rewritten (rule 4). Each replacement must match exactly once.

usage (from the repository root): python3 -B apply_board.py queue BOARD
                                  python3 -B apply_board.py land BOARD HISTORY
"""
import posixpath
import re
import sys
from pathlib import Path

DEV = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a2-chain/'
ROW_START = '| **A2: the generativity chain\'s change Ren took on 18 October**'
CLAIMED = ' | claimed 2026-10-18 | worktree `.claude/worktrees/a2-chain`'
READY = (' | claimed 2026-10-18; ready in its worktree (trial on `adab4a574`: render, check, links scoped to the changed '
         'files and tests passed), in the landing queue after F2 | worktree `.claude/worktrees/a2-chain`')
QUEUE_BEFORE = ' Hold commits that touch the package, the chapter or records'
QUEUE_ITEM = (' Then A2 (Claude Code session of 18 October, the generativity chain\'s change Ren took: docs and records '
              'only, no Lean and no checker run; its trial on `adab4a574` passed render, check, links and tests; it '
              'rebuilds on main with its scripts when its turn comes).')
HISTORY_AFTER = '## Landed after the board was rewritten (17 October 2026)\n'
LANDED = ('landed 2026-10-19 in the commit "A2 landing" (docs and records, no Lean: `Selection` in the chain\'s wisdom '
          'entry (M15), `Observation` and `Parting` in its learning entry (M26), each with its record\'s scope; the '
          'maintenance record\'s entry for the sources changed since 16 October, each change read before its '
          'fingerprint was refreshed and the rest left pending; chapter §8.4 and the brief\'s item 19; the references '
          'of records citing the changed files re-pointed)')
LANDED_NOTE = '; A2 landed in the commit "A2 landing", docs and records with no checker run'
FEEDS = ('D43, review P8 → `generativity-chain.json`, GENERATIVITY-CHAIN.md, its index record, chapter §8.4, the '
         'brief\'s item 19; the sources left pending, M21\'s wording and the chain\'s retired labels go to the next '
         'whole-chain review |')


def once(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f'the text to replace occurs {text.count(old)} times: {old[:80]}')
    return text.replace(old, new)


def row(text):
    rows = [line for line in text.splitlines(keepends=True) if line.startswith(ROW_START)]
    if len(rows) != 1:
        raise SystemExit(f'{len(rows)} A2 rows on the board')
    return rows[0]


def queue(board):
    text = board.read_text()
    line = row(text)
    text = once(text, line, once(line, CLAIMED, READY))
    board.write_text(once(text, QUEUE_BEFORE, QUEUE_ITEM + QUEUE_BEFORE))


def moved(line, board, history):
    """The row's relative links, rewritten for the history file's folder."""
    def target(match):
        path, mark, anchor = match.group(1).partition('#')
        if not path or re.match(r'[a-z]+:|/', path):
            return match.group(0)
        name = posixpath.normpath(posixpath.join(posixpath.dirname(board), path))
        return '](' + posixpath.relpath(name, posixpath.dirname(history)) + mark + anchor + ')'
    return re.sub(r'\]\(([^)\s]+)\)', target, line)


def land(board, history):
    text = board.read_text()
    line = row(text)
    text = once(text, line, '')
    item = QUEUE_ITEM[len(' Then '):]
    if QUEUE_ITEM in text:
        text = once(text, QUEUE_ITEM, '')
    elif item + ' Then ' in text:
        text = once(text, item + ' Then ', '')
    else:
        raise SystemExit('A2 queue item not found')
    head = re.search(r'^In the queue \((.*?)\): ', text, re.M)
    if not head:
        raise SystemExit('queue paragraph not found')
    text = text[:head.end(1)] + LANDED_NOTE + text[head.end(1):]
    board.write_text(text)
    cells = moved(line, str(board), str(history)).rstrip('\n').split(' | ')
    if len(cells) != 5:
        raise SystemExit(f'A2 row has {len(cells)} cells')
    cells[2:] = [LANDED, f'`{DEV}`', FEEDS]
    lines = history.read_text().splitlines(keepends=True)
    start = lines.index(HISTORY_AFTER)
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith('## ')), len(lines))
    last = max(i for i in range(start, end) if lines[i].startswith('| '))
    lines.insert(last + 1, ' | '.join(cells) + '\n')
    history.write_text(''.join(lines))


def main():
    if sys.argv[1:2] == ['queue'] and len(sys.argv) == 3:
        queue(Path(sys.argv[2]))
    elif sys.argv[1:2] == ['land'] and len(sys.argv) == 4:
        land(Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
