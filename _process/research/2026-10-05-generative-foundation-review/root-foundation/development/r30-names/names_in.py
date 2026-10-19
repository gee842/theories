"""R30 check: which renamed declarations (short names) a file names. usage: python3 names_in.py FILE..."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(HERE + '/rename-draft.json'))
REN = {r['old_full_name']: r['new_full_name'] for r in t if r['kind'] == 'decl' and r['decision'].startswith('apply')}
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    hits = set()
    for o in REN:
        short = o[len('Becoming.'):]
        if '.' in short and re.search(r'(?<![\w.])' + re.escape(short) + r'(?![\w])', s):
            hits.add(short)
    print(f, sorted(hits))
