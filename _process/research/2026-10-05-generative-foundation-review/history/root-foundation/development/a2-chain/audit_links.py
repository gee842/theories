#!/usr/bin/env python3
"""A2: for the sources classify_pending.py found changed only in link targets (links-only, split+links), check that
every rewritten target still names the same file: the old and new targets, paired in order, differ only by the
file's directory (a move), by the anchor's spelling where the heading itself is unchanged, or by the edition
pointer of the language separation. Read-only on the repository.

usage (from the repository root): python3 -B audit_links.py CLASSIFICATION_JSON
prints, per source, the changed target pairs that are not a move of the same file, and a summary.
"""
import json
import re
import subprocess
import sys
from pathlib import PurePosixPath

sys.path.insert(0, '.')
from tools.research.split_languages import split  # noqa: E402

TARGET = re.compile(r'\]\(([^)\n]*)\)|href=["\']([^"\']*)["\']')


def targets(text):
    return [a or b for a, b in TARGET.findall(text)]


def file_of(target):
    return PurePosixPath(target.split('#', 1)[0]).name if target.split('#', 1)[0] else ''


def main():
    data = json.load(open(sys.argv[1]))
    odd, checked = {}, 0
    for name, item in data.items():
        if item.get('kind') not in ('links-only', 'split+links'):
            continue
        old = subprocess.run(['git', 'show', f"{item['recorded_commit']}:{item['recorded_path']}"],
                             capture_output=True, check=True).stdout.decode()
        if item['kind'] == 'split+links':
            old = '\n'.join(split(old, PurePosixPath(name).name).en)
        new = open(name).read()
        a, b = targets(old), targets(new)
        checked += 1
        if len(a) != len(b):
            odd[name] = [f'{len(a)} targets before, {len(b)} now']
            continue
        bad = [(x, y) for x, y in zip(a, b) if x != y and file_of(x) != file_of(y)]
        if bad:
            odd[name] = bad
    for name, bad in odd.items():
        print(name)
        for pair in bad:
            print('   ', pair)
    print(f'{checked} sources checked; {len(odd)} with a changed target that is not the same file moved')


if __name__ == '__main__':
    main()
