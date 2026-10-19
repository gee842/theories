import os
"""Build rename-draft.json from spec.py (read-only over the repository)."""
import glob, json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from parse import strip_comments
import spec

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *['..']*6))
CORE = os.environ.get('R30_CORE') or REPO + '/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
decls = json.load(open(HERE + '/decls.json'))['decls']
byfull = {x['full']: x for x in decls}
fulls = set(byfull)
shortcount = collections.Counter(x['name'].split('.')[-1] if '.' in x['name'] else x['name'] for x in decls)
lastcount = collections.Counter(x['full'].split('.')[-1] for x in decls)
nss = set()
for x in decls:
    p = x['full'].split('.')
    for i in range(1, len(p)):
        nss.add('.'.join(p[:i]))
mods = {x['module'] for x in decls}

core_files = {os.path.basename(f): open(f).read() for f in glob.glob(CORE + '/*.lean')}
core_code = {k: strip_comments(v) for k, v in core_files.items()}


def rd(p):
    try:
        return open(p, encoding='utf-8').read()
    except Exception:
        return ''

T = REPO + '/theories/becoming/'
DCP = REPO + '/_process/research/2026-10-05-generative-foundation-review/root-foundation/'
texts = {
    'chapter_en': {'ch': rd(T + 'chapters/THE-THEORY-OF-BECOMING.md')},
    'chapter_zh': {'zh': rd(T + 'chapters/THE-THEORY-OF-BECOMING.zh.md')},
    'opening': {'op': rd(T + 'OPENING.md')},
    'decisions_DC': {'dc': rd(DCP + 'DELEGATED-CHOICES.md'), 'dczh': rd(DCP + 'DELEGATED-CHOICES.zh.md')},
    'records_json': {os.path.basename(f): rd(f) for f in glob.glob(T + 'results/records/*.json')},
}
other = {}
for f in glob.glob(REPO + '/theories/**/*.md', recursive=True):
    if '/history/' in f or '/results/records/' in f or 'LEAN-INDEX' in f or 'lean-declarations' in f or 'LEAN-DECLARATIONS' in f:
        continue
    if f.endswith(('THE-THEORY-OF-BECOMING.md', 'THE-THEORY-OF-BECOMING.zh.md', 'OPENING.md')):
        continue
    other[f[len(REPO) + 1:]] = rd(f)
other['lean/becoming/README.md'] = rd(CORE + '/../README.md')
texts['other_live_md'] = other


def patterns(old):
    """(qualified, bare) regexes for a full declaration name."""
    p = old[len('Becoming.'):].split('.')
    last = p[-1]
    q = None
    if len(p) >= 2:
        q = re.compile(r'(?<![\w])' + re.escape(p[-2] + '.' + last) + r'(?![\w])')
    compound = ('_' in last) or bool(re.search(r'[a-z][A-Z]', last))
    bare = re.compile(r'(?<![\w])' + re.escape(last) + r'(?![\w\'])')
    return q, bare, compound, last


_big = {}
def count(pat, docs, files=False):
    key = id(docs)
    if key not in _big:
        _big[key] = '\x00'.join(docs.values())
    if not pat.search(_big[key]):
        return (0, 0) if files else 0
    n = 0; nf = 0
    for v in docs.values():
        k = len(pat.findall(v))
        n += k; nf += (k > 0)
    return (n, nf) if files else n


rows = []
_seen = set()
for e in spec.build(decls):
    if e['kind'] == 'decl' and e['old'] in _seen:
        continue
    if e['kind'] == 'decl':
        _seen.add(e['old'])
    row = dict(old_full_name=e['old'], new_full_name=e['new'], kind=e['kind'], reason=e['reason'],
               confidence=e['confidence'], justified=e['justified'])
    old = e['old']
    x = byfull.get(old)
    if x:
        row['module'] = x['module']; row['line'] = x['line']; row['decl_kind'] = x['kind']
        body = ' '.join(strip_comments(x['text']).split())
        row['definition'] = body[:200]
    elif e['kind'] in ('module',):
        row['module'] = old
    elif e['kind'] == 'namespace':
        m = re.search(r'module=(\S+)', e['note'])
        row['module'] = m.group(1) if m else ''
    # occurrences
    if x or (e['kind'] in ('decl', 'keep', 'delete') and old.startswith('Becoming.')):
        q, bare, compound, last = patterns(old)
        ambiguous = lastcount[last] > 1
        occ = {'bare_token': count(bare, core_code, True)}
        occ['bare_token'] = {'count': occ['bare_token'][0], 'files': occ['bare_token'][1]}
        if q:
            c = count(q, core_files, True); occ['qualified'] = {'count': c[0], 'files': c[1]}
        occ['last_component_unique_in_core'] = not ambiguous
        row['occurrences_in_core'] = occ
        cites = {}
        for k, docs in texts.items():
            if compound and not ambiguous:
                c = count(bare, docs, True)
            elif q:
                c = count(q, docs, True)
            else:
                c = count(re.compile(r'`' + re.escape(last) + r'`'), docs, True)
            cites[k] = {'count': c[0], 'files': c[1]} if k in ('records_json', 'other_live_md', 'decisions_DC') else c[0]
        cites['_pattern'] = 'bare' if (compound and not ambiguous) else ('qualified ' + (old.split('.')[-2] + '.' + last) if q else 'backticked')
        row['cited_in'] = cites
    elif e['kind'] in ('module', 'namespace'):
        short = old.split(' ')[0][len('Becoming.'):]
        if e['kind'] == 'module':
            imp = re.compile(r'import Becoming\.' + re.escape(short) + r'(?![\w.])')
            ref = re.compile(r'Becoming\.' + re.escape(short) + r'(?![\w.])')
            row['occurrences_in_core'] = {'imports': count(imp, core_files, True), 'module_refs': count(ref, core_files, True),
                                          'declarations_in_namespace': sum(1 for d in decls if d['full'].startswith('Becoming.' + short + '.'))}
            row['cited_in'] = {k: (count(ref, v, True) if k in ('records_json', 'other_live_md', 'decisions_DC') else count(ref, v))
                               for k, v in texts.items()}
        else:
            mod = row.get('module')
            members = [d for d in decls if d['full'].startswith('Becoming.' + short + '.') and (not mod or d['module'] == mod)]
            ref = re.compile(r'(?<![\w.])' + re.escape(short.split('.')[-1]) + r'\.(' + '|'.join(re.escape(d['full'].split('.')[-1]) for d in members) + r')(?![\w])') if members else None
            row['occurrences_in_core'] = {'members': len(members),
                                          'qualified_member_refs': ({'count': count(ref, core_files, True)[0], 'files': count(ref, core_files, True)[1]} if ref else None)}
            if ref:
                row['cited_in'] = {k: count(ref, v) if not isinstance(v, dict) else count(ref, v) for k, v in texts.items()}
    # new-name check
    new = e['new']
    if e['kind'] in ('decl',) and new.startswith('Becoming.'):
        row['new_name_exists'] = new in fulls
        nl = new.split('.')[-1]
        row['new_last_component_elsewhere'] = sorted(d['full'] for d in decls if d['full'].split('.')[-1] == nl and d['full'] != old)[:5]
    elif e['kind'] in ('module', 'namespace') and new.startswith('Becoming.'):
        row['new_name_exists'] = {'namespace': new in nss, 'module': new in mods, 'decl': new in fulls}
    if e['note']:
        row['note'] = e['note']
    rows.append(row)

# collision of new names among themselves
newc = collections.Counter(r['new_full_name'] for r in rows if r['kind'] == 'decl')
for r in rows:
    if r['kind'] == 'decl' and newc[r['new_full_name']] > 1:
        r['new_name_clash_in_table'] = True

json.dump(rows, open(HERE + '/rename-draft.json', 'w'), indent=1, ensure_ascii=False)
k = collections.Counter((r['kind'], r['justified']) for r in rows)
print(len(rows), dict(k))
print('new exists:', [r['old_full_name'] + '->' + r['new_full_name'] for r in rows if r.get('new_name_exists') is True or (isinstance(r.get('new_name_exists'), dict) and any(r['new_name_exists'].values()))])
print('clash:', [r['new_full_name'] for r in rows if r.get('new_name_clash_in_table')])
print('missing old:', [r['old_full_name'] for r in rows if r['kind'] in ('decl', 'keep', 'delete') and r['old_full_name'] not in fulls])
