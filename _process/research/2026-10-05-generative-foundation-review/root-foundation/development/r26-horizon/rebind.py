#!/usr/bin/env python3
"""R26 (20 October 2026), Horizon's refutation laws derived from the laws of ideals: rebind the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R26 was rebased on; RECEIPT_ID the passing core receipt of R26's checker run.
* Declarations that moved from HistoryIdeals.lean to Horizon.lean with their full names (`stretchOrder`,
  `Run.stretches`, `refutable_iff_refutableBy`, `adheres_iff_adheresBy`) move to the record's reference to
  Horizon.lean (added, with a proof binding, where the record had none).
* The five `Stretches.*` restatements, removed, are replaced in every declaration list (references and laws)
  by Horizon's laws, which state the same on runs.
* Proof bindings to Horizon.lean and HistoryIdeals.lean are rebound to the receipt after reading the change;
  references to the other files R26 changed follow them where they matched BASE (or where the render log
  reports drift in sections the record does not cite).
* A history note says what moved; claims are unchanged.
"""
import glob, hashlib, json, subprocess, sys

BASE, RID = sys.argv[1], sys.argv[2]
DRIFT = {}
if len(sys.argv) > 3:
    _log = open(sys.argv[3]).read()
    _dec = json.JSONDecoder()
    for _k in range(len(_log)):
        if _log[_k] == '{':
            try:
                _o, _ = _dec.raw_decode(_log[_k:])
            except ValueError:
                continue
            if isinstance(_o, dict) and 'source_drift' in _o:
                for _x in _o['source_drift']:
                    DRIFT.setdefault(_x['path'], set()).add(_x['id'])
                break
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
HOR = PKG + 'Becoming/Horizon.lean'
HI = PKG + 'Becoming/HistoryIdeals.lean'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
MOVED = ['Becoming.stretchOrder', 'Becoming.Run.stretches', 'Becoming.refutable_iff_refutableBy',
         'Becoming.adheres_iff_adheresBy']
REMAP = {'Becoming.Stretches.not_not': 'Becoming.Refutable.not_not',
         'Becoming.Stretches.adheres_least': 'Becoming.Refutable.adheres_least',
         'Becoming.Stretches.adheres_iff': 'Becoming.Refutable.adheres_iff',
         'Becoming.Stretches.not_refutable_of_adheres': 'Becoming.not_refutable_of_adheres',
         'Becoming.Stretches.refutable_adheres_iff': 'Becoming.refutable_adheres_iff'}
home = {}
for m in receipt['modules']:
    for x in m.get('declarations', []):
        home.setdefault(x['name'] if isinstance(x, dict) else x, m['module'])
for n in MOVED + list(REMAP.values()):
    assert home.get(n) == 'Becoming.Horizon', n
for n in REMAP:
    assert n not in home, n
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
WHAT = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('the paragraph on what a finite stretch refutes cites Refutable.not_not, proved in Horizon from the law for points; §9 counts and receipt follow R26',
                                       '有限片段所否证者一段改引 Refutable.not_not（Horizon 由点的律证明）；§9 计数与回执随 R26'),
    CH + 'THE-THEORY-OF-BECOMING-REFERENCE.md': ('the HistoryIdeals row says Horizon proves its laws as the case of runs', 'HistoryIdeals 一行注明 Horizon 把其律作为运行情形证明'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('§9 counts and receipt follow R26', '§9 计数与回执随 R26'),
    STUDY: ('section 216 added', '新增第 216 节'),
    PKG + 'Becoming.lean': ('the module notes of Horizon and HistoryIdeals', 'Horizon 与 HistoryIdeals 的模块说明'),
    PKG + 'becoming-verification.json': ("the current receipt is R26's run", '当前回执为 R26 之运行'),
    HOR: ('imports Becoming.Ideals; stretchOrder, Run.stretches and the two equivalences moved in; six laws proved from the laws of points, statements unchanged',
          '导入 Becoming.Ideals；stretchOrder、Run.stretches 与两个等价移入；六条律由点的律证明，陈述不变'),
    HI: ('the four declarations moved to Horizon and the five Stretches restatements of Horizon\'s laws removed',
         '四个声明移到 Horizon，Horizon 之律的五个 Stretches 重述删去'),
}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout).hexdigest() for p in WHAT}


def binding(src, module):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module,
            'success_pointer': '/status', 'success_value': 'passed'}


def remap(names):
    out = []
    for n in names:
        n = REMAP.get(n, n)
        if n not in out:
            out.append(n)
    return out


n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by = {r['path']: r for r in refs}
    moved, remapped = [], []
    hi = by.get(HI)
    if hi and hi.get('declarations'):
        keep = []
        for x in hi['declarations']:
            if x in MOVED or x in REMAP:
                if HOR not in by:
                    by[HOR] = {'path': HOR, 'role': 'proof', 'sha256': h(HOR), 'declarations': []}
                    refs.insert(refs.index(hi) + 1, by[HOR])
                y = REMAP.get(x, x)
                if y not in by[HOR]['declarations']:
                    by[HOR]['declarations'].append(y)
                (remapped if x in REMAP else moved).append(x)
            else:
                keep.append(x)
        hi['declarations'] = keep
    for law in d.get('laws', []) or []:
        if isinstance(law, dict) and law.get('declarations'):
            new = remap(law['declarations'])
            if new != law['declarations']:
                remapped += [x for x in law['declarations'] if x in REMAP]
                law['declarations'] = new
    for r in refs:
        if r.get('declarations'):
            r['declarations'] = remap(r['declarations'])
    for k in ('aliases',):
        if isinstance(d.get(k), list):
            d[k] = remap(d[k])
    if rid == 'a-history-read-off-its-finite-stretches':
        for dep in d.get('dependencies', []):
            if dep.get('id') == 'what-a-finite-history-refutes':
                dep['detail']['en'] = dep['detail']['en'].replace(
                    "and Horizon's laws are derived here as the case of runs.",
                    "and Horizon's laws are the case of runs of the laws of points, which Becoming.Horizon proves them from (R26).")
                dep['detail']['zh'] = dep['detail']['zh'].replace(
                    'Horizon 的律在此作为运行情形推出。', 'Horizon 的律是点的律的运行情形，Becoming.Horizon 由之证明（R26）。')
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if HOR in by and HOR not in bound and (moved or remapped) and d.get('proof_bindings'):
        d['proof_bindings'].append(binding(HOR, 'Becoming.Horizon'))
    rebound, touched = [], set()
    module_of = {HOR: 'Becoming.Horizon', HI: 'Becoming.HistoryIdeals'}
    for b in d.get('proof_bindings', []):
        if b['source'] in module_of and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
            b['receipt'] = RECEIPT
            rebound.append(b['source'].rsplit('/', 1)[-1])
    for r in refs:
        p = r['path']
        if p in module_of and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    ps = sorted(touched)
    en = '20 October 2026, R26 (Horizon\'s refutation laws derived from the laws of ideals; board rule 9):'
    zh = '2026年10月20日，R26（Horizon 的否证律由理想之律推出；看板规则 9）：'
    if moved:
        en += ' ' + ', '.join(x.split('Becoming.', 1)[1] for x in moved) + ' moved from HistoryIdeals.lean to Horizon.lean with their full names and proofs.'
        zh += '、'.join(x.split('Becoming.', 1)[1] for x in moved) + ' 连同完整名称与证明从 HistoryIdeals.lean 移到 Horizon.lean。'
    if remapped:
        en += (' The removed restatements ' + ', '.join(sorted(set(x.split('Becoming.', 1)[1] for x in remapped)))
               + ' are replaced by Horizon\'s laws, which state the same on runs and are now proved from the laws of points.')
        zh += '删去的重述 ' + '、'.join(sorted(set(x.split('Becoming.', 1)[1] for x in remapped))) + ' 改为 Horizon 的律，它们在运行上陈述相同，现由点的律证明。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    if ps:
        en += (' Re-pointed after reading the change: ' + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '.')
        zh += '读过改动后重新指向：' + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。'
    en += ' The claim is unchanged.'
    zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R26'):
        # A second pass (with a render log) adds what it re-pointed to the first pass's note.
        if ps:
            last['en'] = last['en'].replace(' The claim is unchanged.', ' Also re-pointed after reading the change: '
                                            + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '. The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', '另读过改动后重新指向：'
                                            + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。论断不变。')
    else:
        d['history'].append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(moved), len(set(remapped)), sorted(set(rebound)), len(ps))
print(n, 'records changed')
