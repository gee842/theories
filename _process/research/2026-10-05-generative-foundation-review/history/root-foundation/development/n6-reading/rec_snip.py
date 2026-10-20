"""Print snippets around core retired words in records' live strings, beyond the kept senses (N6)."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_dump import leaves
from reading_pass import RECORDS
from rec_count import P, K
for stem in sys.argv[1:]:
    d = json.load(open(RECORDS + stem + '.json'))
    for p, s in leaves(d):
        if p[0] == 'validation_scope': continue
        t = K.sub(lambda m: '\0' * len(m.group()), s)
        for m in P.finditer(t):
            a = max(0, m.start() - 70); print(stem, '/'.join(map(str, p)), '::', s[a:m.end() + 50].replace('\n', ' '))
