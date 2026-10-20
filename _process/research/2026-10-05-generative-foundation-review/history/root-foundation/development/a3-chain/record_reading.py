#!/usr/bin/env python3
"""A3: record the fingerprints of the sources A3 read, and the discovery pages it classified.

READING (reading.json, next to this script) lists each pending source read, with the sha256 of the version read, the
entries that link it and the basis of the reading. A source's fingerprint is recorded only where the file in the tree
is still the version read; any source changed since is reported and the script stops before writing, unless
--allow-pending is given: read the change, then update its sha256 and basis in reading.json. The classified pages of
`discovery` are added to the inspected page inventory, each only if it is discovered; pages discovered later are not
added. This is `generative_chain.py --record-review` and `--record-discovery-review` restricted to what A3 read.

usage (from the repository root, after apply_entries.py): python3 -B record_reading.py [--dry] [--allow-pending]
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, '.')
from tools.research import generative_chain as chain  # noqa: E402

READING = Path(__file__).resolve().parent / 'reading.json'


def main():
    dry = '--dry' in sys.argv
    reading = json.loads(READING.read_text())
    data = chain.read_data()
    recorded, unchanged, moved_on = [], [], []
    for name, item in sorted(reading['sources'].items()):
        if item['decision'] != 'refresh':
            continue
        current = hashlib.sha256((chain.ROOT / name).read_bytes()).hexdigest()
        if data['reviewed_sources'].get(name) == current:
            unchanged.append(name)
        elif current == item['sha256']:
            data['reviewed_sources'][name] = current
            recorded.append(name)
        else:
            moved_on.append(name)
    found = set(chain.discovery(data))
    known = set(data['known_discovery_paths'])
    added = sorted(p for p in reading['discovery'] if p in found and p not in known)
    data['known_discovery_paths'] = sorted(known | set(added))
    print(f'{len(recorded)} fingerprints recorded; {len(unchanged)} already current; '
          f'{len(moved_on)} changed after A3 read them, left pending; {len(added)} pages added to the inventory')
    for name in moved_on:
        print('  changed since reading:', name)
    if moved_on and '--allow-pending' not in sys.argv:
        raise SystemExit('sources changed after A3 read them; read each change and update reading.json first')
    if not dry:
        chain.write_data(data)


if __name__ == '__main__':
    main()
