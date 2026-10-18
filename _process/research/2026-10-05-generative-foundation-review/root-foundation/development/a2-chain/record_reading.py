#!/usr/bin/env python3
"""A2: record the fingerprints of the chain sources A2 read, and the new pages it classified, at landing time.

READING (reading.json, next to this script) lists each source read with the sha256 of the version read. A source is
recorded where the file in the tree is still that version. A2's own landing re-points the references of records that
cite the chapter, and the regenerated page of such a record gains one history line; where a source's only change
since BASE is such lines and BASE holds the version read, that change is A2's note and the source is recorded too. Any
other source changed after A2 read it is reported, and the script stops before writing unless --allow-pending is
given: read the change with reread_at_landing.py first. The new pages A2 classified are added
to the inspected page inventory (`known_discovery_paths`), each only if it is still discovered; pages discovered later
are not added. This is `generative_chain.py --record-review` and `--record-discovery-review` restricted to what A2
read.

usage (from the repository root, after rehash_refs.py and the render):
    python3 -B record_reading.py BASE [--dry] [--allow-pending]
"""
import difflib
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, '.')
from tools.research import generative_chain as chain  # noqa: E402

READING = Path(__file__).resolve().parent / 'reading.json'
OWN = '- 19 October 2026, A2: '


def own_note_only(name, read, base):
    """Whether BASE holds the version read and the change since adds only A2's own history lines."""
    shown = subprocess.run(['git', 'show', f'{base}:{name}'], capture_output=True)
    if shown.returncode or hashlib.sha256(shown.stdout).hexdigest() != read:
        return False
    old, new = shown.stdout.decode().splitlines(), (chain.ROOT / name).read_text().splitlines()
    steps = difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes()
    return all(tag == 'equal' or (tag == 'insert' and all(line.startswith(OWN) for line in new[j1:j2]))
               for tag, _, _, j1, j2 in steps)


def main():
    base, dry = sys.argv[1], '--dry' in sys.argv
    reading = json.loads(READING.read_text())
    data = chain.read_data()
    recorded, own, moved_on, unchanged = [], [], [], []
    for name, item in sorted(reading['sources'].items()):
        current = hashlib.sha256((chain.ROOT / name).read_bytes()).hexdigest()
        if data['reviewed_sources'].get(name) == current:
            unchanged.append(name)
        elif current == item['sha256']:
            data['reviewed_sources'][name] = current
            recorded.append(name)
        elif own_note_only(name, item['sha256'], base):
            data['reviewed_sources'][name] = current
            own.append(name)
        else:
            moved_on.append(name)
    found = set(chain.discovery(data))
    known = set(data['known_discovery_paths'])
    added = sorted(p for p in reading['discovery'] if p in found and p not in known)
    data['known_discovery_paths'] = sorted(known | set(added))
    print(f'{len(recorded)} fingerprints recorded; {len(own)} recorded with A2\'s own history note; '
          f'{len(unchanged)} already current; {len(moved_on)} changed after A2 read them, left pending; '
          f'{len(added)} pages added to the inventory')
    for name in own:
        print('  with A2\'s note:', name)
    for name in moved_on:
        print('  changed since reading:', name)
    if moved_on and '--allow-pending' not in sys.argv:
        raise SystemExit('sources changed after A2 read them; read them with reread_at_landing.py first')
    if not dry:
        chain.write_data(data)


if __name__ == '__main__':
    main()
