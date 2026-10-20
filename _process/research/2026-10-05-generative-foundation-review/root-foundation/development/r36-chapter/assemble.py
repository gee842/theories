"""R36: assemble the restructured canonical chapter (EN) from its drafted parts.

Concatenates draft/EN-*.md in order, inserts the theorem map between its markers (written from the
records by `theorem_map`), the glossary's index of formal terms and its vocabulary tables (written
by glossary.py from the frozen edition), and writes the chapter.

Usage: python3 -B assemble.py ROOT FROZEN_EN OUT
  ROOT       repository root (records are read from theories/becoming/results/records)
  FROZEN_EN  the frozen edition, source of the glossary index and the vocabulary tables
  OUT        where to write the chapter
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import glossary  # noqa: E402

PARTS = ['EN-00-front', 'EN-01', 'EN-02', 'EN-03', 'EN-04', 'EN-05', 'EN-06', 'EN-07', 'MAP', 'EN-08',
         'EN-09', 'EN-10', 'EN-11']
REC = re.compile(r'results/records/([a-z0-9][a-z0-9-]*)\.md')

# Records no section of the body links: the section that states their content.
PLACE = {
    'acquired-binding-compositional-use': '3.5', 'binding-preserving-substitution': '3.5',
    'conditional-foundation-assessment': '8.1', 'constitutive-binding-assessment': '3.5',
    'naming-attention-coverage': '3.5', 'historical-source-binding': '3.5',
    'retrospective-source-binding': '3.5', 'enacted-scene-binding': '3.5',
}

# Premises of §0 blocks E–F (the condition, living significance, A, C, D, J1–J4, L) that a record's
# hypotheses take, read record by record from its hypotheses (R36, study §227): a mention there is often
# a negation ("uses no C"), a history ("G0 was folded") or another word ("the class C", "joining relation J").
ETHICS = {
    'acquired-revision-of-pending-task': ['living significance', 'J1–J4'],
    'becoming-spine-instances': ['A', 'C'],
    'classification-robust-generative-comparison': ['living significance', 'J1–J4'],
    'closure-verdict-meets-continuation-condition': ['the condition'],
    'comparison-within-reach': ['the condition (three witnesses)'],
    'continuation-condition-yields-living-significance': ['the condition', 'A'],
    'formed-goal-revision-continuation': ['living significance', 'J1–J4'],
    'open-form-realization-under-revision': ['living significance', 'the condition (one instance)'],
    'own-good-to-reachable-living-significance': ['monotonicity and supervenience'],
    'pending-task-context-applicability': ['living significance', 'J1–J4'],
    'positioned-positive-reason': ['living significance', 'D'],
    'positive-ground-open-futures': ['living significance', 'A'],
    'protection-priority-excludes-uniform-aggregation': ['living significance', 'C', 'J1–J4'],
    'ranking-under-readings': ['C', 'the condition (one theorem)'],
    'relational-generative-comparison': ['C'],
    'relational-reading-comparison': ['C', 'living significance (one theorem)'],
    'relative-position-is-zero-sum': ['the condition (one theorem)'],
    'renewing-consuming-formation': ['living significance', 'C'],
    'significance-retained-within-margin': ['the condition'],
    'whole-first-and-bounded-centers': ['the condition'],
}

# Premises of §0 block C and the supplied law of exchange, read off the Lean names in the hypotheses.
WORLD = [
    ('balance', r'Flow\.Balances(On)?\b|World\.Balanced|\bBalances\b|\bBalancesOn\b'),
    ('dissipation', r'\bDissipative(By)?\b|\bDissipatesOn\b|\bDissipatesBy\b'),
    ('embodiment', r'\bEmbodied\b'),
    ('activity needing support', r'\bDependent\b|\bCarries\b'),
    ('transmission', r'TransmitsWithin|\bTransmitting\b'),
    ('a supplied law of exchange', r'\bExchangeLaw\b|\bLocalLaw\b|Flow\.Follows'),
]


def premises_list(rec):
    if rec['kind'] != 'theorem' or rec['status'] == 'superseded':
        return None
    hyp = ' '.join(h.get('en', '') for h in rec.get('hypotheses', []))
    return ETHICS.get(rec['id'], []) + [n for n, p in WORLD if re.search(p, hyp)]


def standing(rec):
    kind, status = rec['kind'], rec['status']
    if status == 'superseded':
        return 'superseded'
    if kind == 'target':
        return 'open target'
    if kind in ('assessment', 'argument'):
        return kind
    core = '/lean/becoming/Becoming/' in (rec.get('canonical_source') or '')
    ps = premises_list(rec)
    if any(p.startswith('the condition') for p in ps):
        s = 'theorem, the condition among its hypotheses'
    elif ps:
        s = 'theorem under stated premises'
    else:
        s = 'theorem without premise'
    return s + ('' if core else ' (periphery)')


def premises(rec):
    ps = premises_list(rec)
    if ps is None:
        return 'in the record'
    return ', '.join(ps) if ps else '—'


def sections_of(text):
    """record id -> first section number (x.y, or x for a section without subsections) linking it."""
    out = {}
    cur = None
    for line in text.split('\n'):
        m = re.match(r'^#{2,3} (\d+(?:\.\d+)?)\.? ', line)
        if m:
            cur = m.group(1)
            continue
        if line.startswith('## ') and not m:
            cur = {'## Preface': 'preface', '## 0. Premise card': '0'}.get(line.strip(), cur)
        if cur is None:
            continue
        for rid in REC.findall(line):
            out.setdefault(rid, []).append(cur)
    return out


def best(secs):
    body = [s for s in secs if re.match(r'^[1-7]', s)]
    if body:
        return body[0]
    other = [s for s in secs if s not in ('preface',)]
    return other[0] if other else secs[0]


def theorem_map(root, text, zh=False):
    recs = {}
    for f in sorted((root / 'theories/becoming/results/records').glob('*.json')):
        d = json.loads(f.read_text())
        recs[d['id']] = d
    where = sections_of(text)
    rows, missing = [], []
    order = []
    for rid, d in recs.items():
        if rid in where:
            sec = best(where[rid])
        elif rid in PLACE:
            sec = PLACE[rid]
        else:
            missing.append(rid)
            sec = '—'
        key = [int(x) if x.isdigit() else 99 for x in re.split(r'\.', sec)] if sec[0].isdigit() else [99]
        order.append((key, rid, sec, d))
    order.sort(key=lambda x: (x[0], x[1]))
    for _k, rid, sec, d in order:
        title = d['title']['zh' if zh else 'en']
        link = f'[{title}](../results/records/{rid}.md)'
        anchor = sec.replace('.', '')
        sec_cell = sec if sec == '—' else f'§{sec}'
        rows.append(f'| {link} | {standing(d)} | {premises(d)} | {sec_cell} |')
    head = ['| Record | Standing | Premises of §0 in its hypotheses | Section |', '|---|---|---|---|']
    return '\n'.join(head + rows), missing


def main():
    root, frozen, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    parts = []
    for p in PARTS:
        if p == 'MAP':
            parts.append((HERE / 'draft' / 'MAP.md').read_text())
        else:
            parts.append((HERE / 'draft' / f'{p}.md').read_text())
    text = '\n'.join(s.rstrip('\n') + '\n' for s in parts)
    index, tail, _n = glossary.build(frozen.read_text())
    text = text.replace('<!-- glossary-index -->', '\n'.join(['| Term (Chinese name) | Meaning | Lean anchor |', '|---|---|---|'] + index) + '\n\n' + tail.strip('\n'))
    table, missing = theorem_map(root, text)
    text = re.sub(r'<!-- theorem-map:begin -->.*?<!-- theorem-map:end -->',
                  lambda _m: '<!-- theorem-map:begin -->\n' + table + '\n<!-- theorem-map:end -->', text, flags=re.S)
    out.write_text(text)
    print(f'wrote {out}: {len(text.encode())} bytes, {text.count(chr(10))} lines; records placed by no section: {missing}', file=sys.stderr)


if __name__ == '__main__':
    main()
