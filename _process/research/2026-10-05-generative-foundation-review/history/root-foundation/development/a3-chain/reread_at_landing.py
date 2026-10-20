#!/usr/bin/env python3
"""A3: the sources A3 read that later landings changed before A3's turn. `--show` prints, for each, the change from
the version A3 read (found by its hash in BASE's history) to BASE's version: the items removed and added in each
changed field of a record JSON, and the diff of any other file. `--accept PATH ... --basis TEXT` records in
reading.json that BASE's version of each PATH was read, with the basis, so that record_reading.py records its
fingerprint. A source whose change was not read stays pending. Run on a branch at BASE before rehash_refs.py changes
anything.

usage (from the repository root): python3 -B reread_at_landing.py BASE --show
                                  python3 -B reread_at_landing.py BASE --accept PATH ... --basis TEXT
"""
import difflib
import hashlib
import json
import subprocess
import sys
from pathlib import Path

READING = Path(__file__).resolve().parent / 'reading.json'


def show(commit, name):
    done = subprocess.run(['git', 'show', f'{commit}:{name}'], capture_output=True)
    return None if done.returncode else done.stdout


def moved_on(reading, base):
    out = []
    for name, item in sorted(reading['sources'].items()):
        now = show(base, name)
        if now is None or hashlib.sha256(now).hexdigest() != item['sha256']:
            out.append(name)
    return out


def version(name, sha, base):
    """The committed bytes of `name` with the given sha256, searched in BASE's history."""
    commits = subprocess.run(['git', 'rev-list', base, '--', name], capture_output=True, text=True).stdout.split()
    for commit in commits:
        data = show(commit, name)
        if data is not None and hashlib.sha256(data).hexdigest() == sha:
            return data
    return None


def describe(name, base, item):
    old, new = version(name, item['sha256'], base), show(base, name)
    if old is None:
        return ['(no committed version has the hash read)']
    if new is None:
        return ['(missing at ' + base + ')']
    if name.endswith('.json'):
        a, b = json.loads(old), json.loads(new)
        lines = []
        for key in dict.fromkeys([*a, *b]):
            if a.get(key) == b.get(key):
                continue
            if isinstance(a.get(key), list) and isinstance(b.get(key), list):
                old_items = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in a[key]]
                new_items = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in b[key]]
                lines += [f'{key} removed: {x[:600]}' for x in old_items if x not in new_items]
                lines += [f'{key} added: {x[:600]}' for x in new_items if x not in old_items]
            else:
                lines.append(f'{key} changed: ' + json.dumps(b.get(key), ensure_ascii=False)[:1500])
        return lines
    return [line[:400] for line in difflib.unified_diff(old.decode().splitlines(), new.decode().splitlines(),
                                                       lineterm='', n=0)][2:]


def main():
    base = sys.argv[1]
    reading = json.loads(READING.read_text())
    if sys.argv[2] == '--show':
        for name in moved_on(reading, base):
            print('==', name, '(' + ', '.join(reading['sources'][name]['entries']) + ')')
            for line in describe(name, base, reading['sources'][name]):
                print('  ', line)
        return
    if sys.argv[2] != '--accept' or '--basis' not in sys.argv:
        raise SystemExit(__doc__)
    cut = sys.argv.index('--basis')
    names, basis = sys.argv[3:cut], ' '.join(sys.argv[cut + 1:])
    pending = set(moved_on(reading, base))
    for name in names:
        if name not in pending:
            raise SystemExit(f'{name} did not change after A3 read it')
        item = reading['sources'][name]
        item['sha256'] = hashlib.sha256(show(base, name)).hexdigest()
        item['basis'] = item['basis'].rstrip() + f' Read again at {base[:9]}: {basis}'
    READING.write_text(json.dumps(reading, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(names)} sources recorded as read at {base[:9]}')


if __name__ == '__main__':
    main()
