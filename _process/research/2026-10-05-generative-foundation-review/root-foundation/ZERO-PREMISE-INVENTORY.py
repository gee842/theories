"""Inventory for the zero-premise plan (ZERO-PREMISE-PLAN.md, section 1): for each Part I result
record whose canonical source is a Becoming core module, list the declarations it names whose
signatures use one of the eight premises, finiteness, enclosure or decidability. Usage:
python3 -B ZERO-PREMISE-INVENTORY.py. Where each use occurs in the proof is read by hand (plan 1.3);
this script only finds the candidates."""
import json, glob, re, sys
from pathlib import Path
R = Path(__file__).resolve().parents[4]
B = R / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
PART2 = {'Significance.lean','Metaethics.lean','Standpoints.lean','Ranking.lean','Renewal.lean','Bridge.lean','Correspondence.lean'}
# index declarations: full name -> (file, signature text)
decls = {}
for f in sorted(B.glob('*.lean')):
    lines = f.read_text().split('\n')
    ns = []
    i = 0
    while i < len(lines):
        l = lines[i]
        m = re.match(r'^namespace (\S+)', l)
        if m: ns.append(m.group(1)); i += 1; continue
        m = re.match(r'^end (\S+)', l)
        if m and ns and ns[-1] == m.group(1): ns.pop(); i += 1; continue
        m = re.match(r'^(theorem|lemma|def|abbrev|structure) (\S+)', l)
        if m:
            sig = [l]; j = i
            while j + 1 < len(lines) and ":=" not in lines[j] and " where" not in lines[j] and j < i + 25 \
                    and not re.match(r'^(namespace|end|theorem|def|lemma|abbrev|structure|instance|inductive|variable|/-)', lines[j + 1]):
                j += 1; sig.append(lines[j])
            i = j
            name = '.'.join(ns + [m.group(2)])
            decls[name] = (f.name, ' '.join(s.strip() for s in sig))
            i += 1; continue
        i += 1
KEYS = {'balance': r'Balances|Balanced', 'acting': r'\.Acting|Acting\b', 'taking': r'Taking', 'dissipative': r'Dissipat',
        'embodied': r'Embodied|ArisingEmbodied', 'dependent': r'Dependent\b', 'census': r'Census|Counted', 'transmitting': r'Transmit',
        'finite': r'Finite\b|\.Finite', 'enclosure': r'Enclosed|AroundStanding|ClosedAt|enclosed', 'decidable': r'Decidable|\(em :'}
for f in sorted(glob.glob(str(R / 'theories/becoming/results/records/*.json'))):
    r = json.load(open(f))
    cs = r.get('canonical_source', '')
    if '/lean/becoming/Becoming/' not in cs or cs.split('/')[-1] in PART2: continue
    print('##', r['id'], '(' + cs.split('/')[-1] + ')')
    for a in r.get('aliases', []):
        name = a if a.startswith('Becoming.') else 'Becoming.' + a
        d = decls.get(name)
        if not d:
            cands = [k for k in decls if k.endswith('.' + a.replace('Becoming.', ''))]
            d = decls[cands[0]] if len(cands) == 1 else None
        if not d:
            print('  ?', a); continue
        sig = d[1].split(':=')[0]
        hits = [k for k, p in KEYS.items() if re.search(p, sig)]
        print('  %-45s %s' % (a.replace('Becoming.', ''), ','.join(hits) if hits else '-'))
