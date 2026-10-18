#!/usr/bin/env python3
"""Move landed rows from the live board to the history file (board rule 4), apply exact replacements to the board
(for instance the queue line), and commit only these changes.

usage (from the repository root): python3 -B board_landed.py SPEC_JSON MESSAGE_FILE
  SPEC_JSON     {"rows": [[PREFIX, STATE], ...], "replace": [[OLD, NEW], ...]}
                PREFIX is the start of a row's first cell, e.g. "| **L2: "; STATE its new state cell; each OLD must
                occur exactly once in the board
  MESSAGE_FILE  the commit message

Another session may hold uncommitted edits to the same two files (18 October 2026: the board restructure of the
session "Constraints as roadblocks"). The commit is made from HEAD's versions with only these changes; the
working-tree versions get the same changes, so their remaining diff is the other session's alone. The files are
checked unchanged between reading and writing back."""
import hashlib, json, subprocess, sys
from pathlib import Path

BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
spec = json.load(open(sys.argv[1]))
message = sys.argv[2]


def git(*args):
    return subprocess.run(['git', *args], check=True, capture_output=True, text=True).stdout


def change(board, history):
    for prefix, state in spec['rows']:
        lines = board.split('\n')
        rows = [i for i, line in enumerate(lines) if line.startswith(prefix)]
        assert len(rows) == 1, (prefix, len(rows))
        row = lines.pop(rows[0])
        cells = row.split(' | ')
        assert len(cells) == 5, len(cells)
        cells[2] = state
        row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
        hist = history.split('\n')
        stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
        last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
        hist.insert(last + 1, row)
        board, history = '\n'.join(lines), '\n'.join(hist)
    for old, new in spec.get('replace', []):
        assert board.count(old) == 1, (old[:80], board.count(old))
        board = board.replace(old, new)
    return board, history


assert subprocess.run(['git', 'rev-parse', '-q', '--verify', 'MERGE_HEAD'], capture_output=True).returncode != 0, \
    'mid-merge: no commit'
head = {p: git('show', f'HEAD:{p}') for p in (BOARD, HISTORY)}
work = {p: Path(p).read_text(encoding='utf-8') for p in (BOARD, HISTORY)}
seen = {p: hashlib.sha256(work[p].encode()).hexdigest() for p in work}
mine = dict(zip((BOARD, HISTORY), change(head[BOARD], head[HISTORY])))
theirs = dict(zip((BOARD, HISTORY), change(work[BOARD], work[HISTORY])))
for p in (BOARD, HISTORY):
    assert hashlib.sha256(Path(p).read_text(encoding='utf-8').encode()).hexdigest() == seen[p], f'{p} changed meanwhile'
    Path(p).write_text(mine[p], encoding='utf-8')
try:
    print(git('commit', '-F', message, '--', BOARD, HISTORY))
finally:
    for p in (BOARD, HISTORY):
        Path(p).write_text(theirs[p], encoding='utf-8')
print(git('show', '--stat', '--format=%h %s', 'HEAD'))
print(git('diff', '--stat'))
