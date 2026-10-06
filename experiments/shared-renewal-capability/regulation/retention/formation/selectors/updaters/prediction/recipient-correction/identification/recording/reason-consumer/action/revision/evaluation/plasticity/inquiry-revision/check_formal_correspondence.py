"""Compare selected compiled Lean milestones with saved numerical states.

This reads artifacts only: it does not execute the producer or claim complete
refinement of either transition system by the other.
"""
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
FORMAL = BASE/'formal/inquiry-revision'


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def vector(s):
    n, c, i, r = (s[k] for k in ('native', 'core', 'inventory', 'reserves'))
    energy = (s['accounting']['parent_fixed_retained']
              + sum(c[k] for k in ('fuel', 'recipient', 'source', 'escrow'))
              + sum(r.values()) + sum(s['packets']['own']) + sum(s['packets']['recipient']))
    occupied = [int(x is not None) for x in s['links']]
    pairs = (i['memory_cells'] + int(i['adapter']) + int(s['port']['built'])
             + i['omitted_pairs'] + sum(i['free_primary']) + int(i['replacement_free'])
             + len(s['retired']) + sum(occupied) + int(s['inquiry']['mode'] != 'absent'))
    phase = {'ready': 0, 'own_paid': 1, 'own_returned': 2, 'recipient_paid': 3,
             'recipient_returned': 4, 'own_acquired': 5, 'recipient_acquired': 6,
             'coupling_settled': 8}[n['phase']]
    # The existing Python law fuses explicit Lean close with the read boundary.
    if s['costs']['evaluation_read'] > 0:
        phase = 9
    return [n['n'], n['count'], c['fuel'], c['recipient'], c['source'],
            sum(s['packets']['own']), sum(s['packets']['recipient']),
            r['primary'], r['revision'], r['idle_common']+r['saved_assembly'], r['idle_source'],
            energy, *[x['sign'] if x is not None else 0 for x in s['links']], *occupied,
            sum(i['free_primary']), int(i['replacement_free']), len(s['retired']), i['omitted_pairs'],
            42+2*pairs, int(c['active']),
            {'ready':0,'rented':1,'sensed':2,'reserved':3,'worked':4,'acquired':5}[s['physical']['core_phase']],
            phase, {'idle':0,'read':1,'assessed_help':2,'assessed_abstain':3,'executing':4,'consumed':5}[s['port']['mode']],
            {'absent':0,'idle':1,'observed':2,'missing':3,'stale':4,'committed':5}[s['inquiry']['mode']],
            s['controls']['training_limit'], int(n['latches']['own']['value']),
            int(n['latches']['recipient']['value']), c['q']]


def main():
    proof = json.loads((FORMAL/'verification.json').read_text())
    assert proof['status'] == 'passed' and proof['fresh_build'] and proof['source_unchanged']
    for module in proof['modules']:
        assert digest(REPO/module['source']) == module['sha256']
    with gzip.open(HERE/'results.json.gz', 'rt') as f:
        result = json.load(f)
    for p, h in result['source_sha256'].items():
        assert digest(REPO/p) == h, p
    module = next(m for m in proof['modules'] if m['module']=='InquiryRevision')
    printed = {k:json.loads(v) for k,v in re.findall(r'^INQUIRY (\w+) (\[.*\])$',
               (REPO/module['log']).read_text(), re.M)}
    assert printed == proof['milestones']
    cases = result['histories']
    requests = {'entry':('faithful',0), 's4':('faithful',32),
                'assembled':('faithful','inquiry.assemble'),
                'observed':('faithful','inquiry.inspect:faithful'),
                'revised':('faithful','inquiry.commit'),
                'assessed':('faithful','evaluation.assess'),
                'final':('faithful','service.write'),
                'miss':('missing','inquiry.inspect:missing'),
                'zero':('zero','inquiry.inspect:zero'),
                'wrong':('wrongBinding','inquiry.inspect:wrongBinding'),
                'sham':('sham','inquiry.shamCommit'),
                'stale':('cut_noop','inherited.scope:true'),
                'noLoss':('zero_history',32)}
    assert set(requests) == set(printed)
    rows = []
    for name, (case, selector) in requests.items():
        trace = cases[case]['trace']
        index = selector if isinstance(selector, int) else next(j for j,x in enumerate(trace) if x['event']==selector)
        actual = vector(trace[index]['state'])
        assert len(actual) == 30
        assert actual == printed[name], (name, actual, printed[name])
        rows.append(dict(name=name, case=case, index=index, event=trace[index]['event'], vector=actual))
    receipt = dict(status='passed', milestones=len(rows), coordinates=30, parent_ref=result['parent_ref'],
        scope='Selected compiled milestones only; not a whole-program or arbitrary-interleaving refinement proof.',
        representation=['Formal packet counts are multiplied by ten for inherited source units.',
            'Explicit Lean close is mapped at the existing Python evaluation-read boundary.',
            'Ordered sockets and retained component counts are compared, not every numerical object identity.',
            'Material includes the converted pair; acquired bits, operative limit, mode and command register are compared.'],
        source_sha256={str(p.relative_to(REPO)):digest(p) for p in
            (Path(__file__), HERE/'results.json.gz', FORMAL/'verification.json', FORMAL/'InquiryRevision.lean')},
        rows=rows)
    (HERE/'formal-correspondence.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','milestones','coordinates','parent_ref')}))


if __name__ == '__main__':
    main()
