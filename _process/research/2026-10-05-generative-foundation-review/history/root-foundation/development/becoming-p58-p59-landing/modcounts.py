"""Update cited module theorem counts in every record's validation scope. Usage: modcounts.py COUNTS_JSON ROOT

Copied from the integrator's p46int/modcounts.py (10-11), with one more English pattern, “the N of Module”."""
import json
import re
import sys
from pathlib import Path
counts = json.loads(Path(sys.argv[1]).read_text())
OLD, NEW = counts['old'], counts['new']
REC = Path(sys.argv[2]) / 'theories/becoming/results/records'
for f in sorted(REC.glob('*.json')):
    r = json.loads(f.read_text())
    vs = r.get('validation_scope')
    if not vs:
        continue
    changed = False
    for lang in ('zh', 'en'):
        t = vs[lang]
        for mod in OLD:
            if OLD[mod] == NEW[mod]:
                continue
            m = re.escape(mod)
            t2 = re.sub(r'(%s(?: 的)? )%d( 项定理)' % (m, OLD[mod]), r'\g<1>%d\g<2>' % NEW[mod], t)
            t2 = re.sub(r'\b%d( theorems of %s\b)' % (OLD[mod], m), r'%d\g<1>' % NEW[mod], t2)
            t2 = re.sub(r'(\bthe )%d( of %s\b)' % (OLD[mod], m), r'\g<1>%d\g<2>' % NEW[mod], t2)
            if t2 != t:
                t, changed = t2, True
        vs[lang] = t
    if changed:
        f.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
        print('module counts in', r['id'])
