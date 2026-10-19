"""Build and verify out/yi/entries.json (read-only on all inputs).
Usage: python3 -I build_entries.py ATLAS_DIR REPO_CLEAN_DIR DECLS_TSV RECORDS_DIR OUT_JSON
Checks: every fragment is an exact substring of ATLAS_DIR/text_path; every repo fragment is an exact
substring of the cleaned repo text; every declaration is in DECLS_TSV; every record file exists;
every atlas id is a node, relation or unit id of data/model.json.
"""
import json, os, sys

ATLAS, REPO, DECLS, RECORDS, OUT = sys.argv[1:6]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from entries_data import ENTRIES  # noqa: E402

decls = set(l.split('\t')[0] for l in open(DECLS, encoding='utf-8'))
model = json.load(open(os.path.join(ATLAS, 'data/model.json'), encoding='utf-8'))
ids = set(n['id'] for n in model['nodes']) | set(r['id'] for r in model['relations'])
for key in ('wing_units', 'transmission_units', 'classic_units'):
    ids |= set(u['id'] for u in model[key])


def repo_clean(path):
    # sources/zhouyi-yizhuan/<dir>/<name>.json -> REPO/<dir>__<name>.txt
    parts = path.split('/')
    return os.path.join(REPO, parts[-2] + '__' + parts[-1].replace('.json', '.txt'))


errors = []
seen = set()
for e in ENTRIES:
    i = e['id']
    if i in seen:
        errors.append(f'{i}: duplicate id')
    seen.add(i)
    if e['text_path']:
        t = open(os.path.join(ATLAS, e['text_path']), encoding='utf-8').read()
        for f in e['fragments']:
            if f not in t:
                errors.append(f'{i}: fragment not in {e["text_path"]}: {f}')
    else:
        if not e.get('needs_source'):
            errors.append(f'{i}: no text_path and no needs_source')
    for rf in e.get('repo_fragments', []):
        t = open(repo_clean(rf['path']), encoding='utf-8').read()
        if rf['text'] not in t:
            errors.append(f'{i}: repo fragment not in {rf["path"]}: {rf["text"]}')
    if not (1 <= len(e['declarations']) <= 8):
        errors.append(f'{i}: {len(e["declarations"])} declarations')
    for d in e['declarations']:
        if d not in decls:
            errors.append(f'{i}: missing declaration {d}')
    for r in e['records']:
        if not os.path.exists(os.path.join(RECORDS, r + '.json')):
            errors.append(f'{i}: missing record {r}')
    for a in e['atlas_ids']:
        if a not in ids:
            errors.append(f'{i}: missing atlas id {a}')
    if e['kind'] not in ('agreement', 'scope', 'divergence'):
        errors.append(f'{i}: kind {e["kind"]}')
    g = e.get('gap')
    if g:
        for d in g['nearest']:
            if d not in decls:
                errors.append(f'{i}: gap nearest missing {d}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

out = []
for e in ENTRIES:
    o = {
        'id': e['id'], 'tradition': e['tradition'], 'atlas': e['atlas'], 'atlas_ids': e['atlas_ids'],
        'source_id': e['source_id'], 'text_path': e['text_path'], 'locator': e['locator'],
        'fragments': e['fragments'],
    }
    if e.get('needs_source'):
        o['needs_source'] = e['needs_source']
    if e.get('repo_fragments'):
        paths = sorted(set(rf['path'] for rf in e['repo_fragments']))
        o['repo_text_path'] = paths[0] if len(paths) == 1 else paths
        o['repo_fragments'] = [rf['text'] if len(paths) == 1 else {'path': rf['path'], 'text': rf['text']}
                               for rf in e['repo_fragments']]
    for k in ('kind', 'declarations', 'records', 'relational', 'reading', 'reading_en', 'gap'):
        o[k] = e.get(k)
    out.append(o)
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
from collections import Counter
print(len(out), dict(Counter(e['kind'] for e in out)), 'gaps', sum(1 for e in out if e['gap']))
