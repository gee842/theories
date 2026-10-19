"""R30 check: old names still standing in the given files after the renaming. A renamed declaration's last
component that no kept declaration shares is reported wherever it stands as a word; a shared one only where it
stands qualified by its old namespace. usage: python3 leftover.py FILE..."""
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(HERE + '/rename-draft.json'))
decls = json.load(open(HERE + '/decls.json'))['decls']
REN = {r['old_full_name']: r['new_full_name'] for r in t if r['kind'] == 'decl' and r['decision'].startswith('apply')}
by_last = defaultdict(set)
for d in decls:
    by_last[d['full'].rsplit('.', 1)[-1]].add(d['full'])
pats = []
for o, n in REN.items():
    last = o.rsplit('.', 1)[-1]
    if last == n.rsplit('.', 1)[-1]:
        p = o.split('.')[-2] + '.' + last  # a namespace move: the old qualified form
        pats.append((re.compile(r'(?<![\w.])' + re.escape(p) + r'(?![\w])'), o))
        continue
    kept = [f for f in by_last[last] if f not in REN]
    if not kept:
        pats.append((re.compile(r'(?<![\w.\'])' + re.escape(last) + r'(?![\w\'])'), o))
    elif o.count('.') >= 2:
        p = '.'.join(o.split('.')[-2:])
        pats.append((re.compile(r'(?<![\w.])' + re.escape(p) + r'(?![\w])'), o))
for f in sys.argv[1:]:
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        spans = ' '.join(re.findall(r'`([^`]+)`', line))
        for p, o in pats:
            bare = '.' not in p.pattern.replace('\\.', '').replace('[\\w.', '') and '\\.' not in p.pattern
            if p.search(spans) or (not bare and p.search(line)):
                print(f'{f}:{i}: [{o}] {line.strip()[:150]}')
