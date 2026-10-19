#!/usr/bin/env python3
"""R32: the pure forwarders the connectivity dump finds (fields `f`, `fk`), with their users.

usage: python3 -B fwstats.py DUMP.json [--json OUT]
DUMP.json is {"c": constants, "reg": registry} as written by the kit's dump runner."""
import collections
import json
import sys

d = json.load(open(sys.argv[1]))
c = d['c']
users = collections.defaultdict(set)
for n, x in c.items():
    for y in set(x['t']) | set(x['v']):
        if y != n:
            users[y].add(n)
fw = {n: x for n, x in c.items() if 'f' in x and x['m'].startswith('Becoming.')}
print('forwarders in Becoming.* modules:', len(fw), collections.Counter(x['fk'] for x in fw.values()))
same = sum(1 for n, x in fw.items() if c.get(x['f'], {}).get('m') == x['m'])
print('target in same module:', same, 'other tracked:', sum(1 for x in fw.values() if x['f'] in c) - same,
      'untracked target:', sum(1 for x in fw.values() if x['f'] not in c))
used = {n: sorted(users[n]) for n in fw}
print('used by another constant:', sum(1 for v in used.values() if v))
print('by module:', collections.Counter(x['m'] for x in fw.values()).most_common(40))
if '--json' in sys.argv:
    out = sys.argv[sys.argv.index('--json') + 1]
    json.dump({n: {'module': x['m'], 'target': x['f'], 'kind': x['fk'],
                   'target_module': c.get(x['f'], {}).get('m'), 'users': used[n]} for n, x in sorted(fw.items())},
              open(out, 'w'), indent=1, ensure_ascii=False)
