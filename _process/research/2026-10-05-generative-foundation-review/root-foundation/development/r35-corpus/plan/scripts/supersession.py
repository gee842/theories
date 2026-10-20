#!/usr/bin/env python3
"""Read-only E8 audit (R35): records whose `proof` references bind superseded periphery modules
(development/bridge-fold/retire.json) or files under lean/history/, and the exact re-role edits.

Run from the repository root: python3 -B supersession.py OUT_DIR
Writes OUT_DIR/supersession.tsv and OUT_DIR/supersession.json. Writes nothing in the repository.
"""
import glob, json, os, sys
from collections import defaultdict

OUT = sys.argv[1]
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/bridge-fold/retire.json'
retire = json.load(open(RF))['modules']
CORE = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'

rows, out = [], []
for p in sorted(glob.glob('theories/becoming/results/records/*.json')):
    r = json.load(open(p))
    refs = r.get('references', [])
    cs = r.get('canonical_source')
    cs = cs.get('path') if isinstance(cs, dict) else cs
    bound = {b['source']: b for b in r.get('proof_bindings', []) or []}
    retired, core = [], []
    for ref in refs:
        path = ref.get('path', '')
        stem = os.path.splitext(os.path.basename(path))[0]
        if ref.get('role') != 'proof':
            continue
        if path.startswith(CORE) or path.endswith('/lean/becoming/Becoming.lean'):
            core.append(path)
            continue
        hist = '/lean/history/' in path
        if path.endswith('.lean') and (stem in retire or hist):
            retired.append({'path': path, 'module': stem, 'in_retire_json': stem in retire,
                            'lean_history': hist, 'stated_by': retire.get(stem, {}).get('stated_by', []),
                            'family': retire.get(stem, {}).get('family'), 'has_proof_binding': path in bound,
                            'receipt': bound.get(path, {}).get('receipt'), 'n_declarations': len(ref.get('declarations', []))})
    if not retired:
        continue
    canon_retired = any(cs == x['path'] for x in retired)
    remaining_bindings = [s for s in bound if s not in {x['path'] for x in retired}]
    stated_by_cited = sorted({m for x in retired for m in x['stated_by']
                              if any(c.endswith('/' + m.split('.')[-1] + '.lean') for c in core)})
    stated_by_missing = sorted({m for x in retired for m in x['stated_by']} - set(stated_by_cited))
    after_ok = (r['status'] != 'recorded-checked') or (core and remaining_bindings)
    out.append({'id': r['id'], 'status': r['status'], 'canonical_source_retired': canon_retired,
                'canonical_source': cs, 'retired_proof_refs': retired, 'core_proof_refs': len(core),
                'remaining_proof_bindings_after': len(remaining_bindings),
                'stated_by_cited_in_record': stated_by_cited, 'stated_by_not_cited': stated_by_missing,
                'still_valid_after_rerole': bool(after_ok)})
    rows.append((r['id'], r['status'], len(retired), sum(x['has_proof_binding'] for x in retired), len(core),
                 len(remaining_bindings), 'yes' if canon_retired else '', ' '.join(sorted({x['module'] for x in retired})),
                 ' '.join(stated_by_missing), 'ok' if after_ok else 'NEEDS-CORE-BINDING'))
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'supersession.tsv'), 'w') as f:
    f.write('id\tstatus\tretired_proof_refs\tof_which_bound\tcore_proof_refs\tbindings_left\tcanonical_retired\tretired_modules\tstated_by_not_cited\tafter_rerole\n')
    for row in rows:
        f.write('\t'.join(map(str, row)) + '\n')
json.dump(out, open(os.path.join(OUT, 'supersession.json'), 'w'), indent=1, ensure_ascii=False)
print(len(rows), 'records;', sum(r[2] for r in rows), 'retired proof refs;', sum(r[3] for r in rows), 'with proof bindings;',
      sum(1 for r in rows if r[9] != 'ok'), 'need a core binding;', sum(1 for r in rows if r[6]), 'canonical source retired')
