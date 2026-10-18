"""Print the live strings of records that hold core retired words, beyond the kept senses (N6)."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_dump import leaves
from reading_pass import RECORDS
from rec_count import core
for stem in sys.argv[1:]:
    d = json.load(open(RECORDS + stem + '.json'))
    print('########', stem)
    for p, s in leaves(d):
        if p[0] == 'validation_scope': continue
        if core(s): print('@', '/'.join(map(str, p)), '::', s)
