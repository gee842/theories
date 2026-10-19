#!/usr/bin/env python3
"""R27 (20 October 2026), the stepwise classes and loss: advance the record significance-retained-within-margin
and re-point the records whose cited files R27 changed.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R27 was rebased on; RECEIPT_ID the passing core receipt of R27's checker run.
* The record gains one claim sentence, the six new declarations on its reference to Significance.lean, a
  next delta, the receipt and study section 217 as references, and a history note.
* Every proof binding to Significance.lean is rebound to the receipt after reading the change (the file gained
  a section and a theorem; nothing else in it changed).
* A reference to another file R27 changed follows it where it matched BASE, or where the render log reports
  drift in sections the record does not cite. A second pass adds to the first pass's note.
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
SIG = PKG + 'Becoming/Significance.lean'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
WHAT = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('§6.8 gains the bullet on the stepwise classes and loss; §9 counts and receipt follow R27',
                                       '§6.8 新增逐步类别与失去一条；§9 计数与回执随 R27'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the same bullet in the Chinese edition; §9 counts and receipt', '中文版同一条；§9 计数与回执'),
    STUDY: ('section 217 added', '新增第 217 节'),
    PKG + 'Becoming.lean': ("the module note of Significance", 'Significance 的模块说明'),
    PKG + 'becoming-verification.json': ("the current receipt is R27's run", '当前回执为 R27 之运行'),
    SIG: ('a section on the stepwise classes and loss and Preemption.within_renewal_yet_loses added; nothing else changed',
          '新增逐步类别与失去一节及 Preemption.within_renewal_yet_loses；其余不变'),
}
NEW = ['Becoming.Web.exceeded_of_below', 'Becoming.Web.UnderminingOn.exceeded', 'Becoming.Web.Includes.not_undermining',
       'Becoming.Web.UnderminingOn.not_retains', 'Becoming.Web.UnderminingOn.not_retains_unrestricted',
       'Becoming.Preemption.within_renewal_yet_loses']
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout).hexdigest() for p in WHAT}
mod = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Significance')
have = {x['name'] if isinstance(x, dict) else x for x in mod['declarations']}
assert not [n for n in NEW if n not in have], [n for n in NEW if n not in have]
assert receipt['source_sha256']['Becoming.Significance'] == h(SIG)

TAG = '20 October 2026, R27'
f = 'theories/becoming/results/records/significance-retained-within-margin.json'
d = json.load(open(f))
sigref = next(r for r in d['references'] if r['path'] == SIG)
if NEW[0] not in sigref['declarations']:
    sigref['declarations'] += NEW
    d['claim']['en'] += (' The stepwise classes read this order in one direction. Levels below a need are exceeded by every '
                         'level path admitting the formation there (Web.exceeded_of_below); so an undermining event, through '
                         'dependences on its condition holding across the step at no smaller need, leaves the levels exceeded by '
                         'every path meeting those dependences after the step (Web.UnderminingOn.exceeded), a path the levels '
                         'include admits no such undermining (Web.Includes.not_undermining), and from a standpoint at which those '
                         'continuations have significance nothing is retained along it (Web.UnderminingOn.not_retains; under the '
                         'continuation condition from every standpoint, Web.UnderminingOn.not_retains_unrestricted). The converse '
                         'fails: in Preemption the drawer\'s event is within renewal and not undermining, and the levels with its '
                         'part do not include those without it (Preemption.within_renewal_yet_loses).')
    d['claim']['zh'] += ('逐步类别在一个方向上读出这一序。水平低于一个所需时，每条在该处接纳这个形成的水平路径都超出它'
                         '（Web.exceeded_of_below）；所以一个侵蚀的事件，经由跨步持续、所需不减的对其条件的依存，使水平被每条在步后满足这些依存的路径超出'
                         '（Web.UnderminingOn.exceeded），水平所包含的路径不容这样的侵蚀（Web.Includes.not_undermining），'
                         '从这些延续有意义的立场，沿它什么也不保留（Web.UnderminingOn.not_retains；延续条件之下从每个立场，'
                         'Web.UnderminingOn.not_retains_unrestricted）。逆向不成立：Preemption 中汲取者的事件在更新之内且不侵蚀，'
                         '有其部分的水平却不包含无它的水平（Preemption.within_renewal_yet_loses）。')
    d['next_delta'] = {'en': 'A measure ordering mixed parts; comparison over several steps; the whole-run classes (consuming, '
                             'arising) related to the order on what can form.',
                       'zh': '为混合部分定序的度量；多步的比较；整段类别（消耗、生起）与能形成者之序的关系。'}
    if not any(r['path'] == RECEIPT for r in d['references']):
        d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    d['history'].append({
        'en': f'{TAG} (study section 217; twentieth review D2): six theorems relating undermining and renewal to the order on what '
              f'can form added to Significance.lean (core receipt {RID}); one paragraph added to the claim; next delta extended. '
              'The earlier claim is unchanged.',
        'zh': f'2026年10月20日，R27（研究第 217 节；第二十次审查 D2）：Significance.lean 新增六个定理，联系侵蚀与更新和能形成者之序'
              f'（核心回执 {RID}）；论断添一段；下一步扩展。原论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('advanced significance-retained-within-margin')

n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    touched, rebound = set(), False
    for b in d.get('proof_bindings', []):
        if b['source'] == SIG and b['receipt'] != RECEIPT:
            b['receipt'] = RECEIPT
            rebound = True
    refs = d.get('references', [])
    for r in refs:
        p = r['path']
        if p == SIG and rebound and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if rid == 'significance-retained-within-margin':
        for r in refs:
            if r['path'] in (STUDY, SIG) and r.get('sha256') != h(r['path']):
                r['sha256'] = h(r['path'])
                touched.add(r['path'])
    if rebound and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if not touched and not rebound:
        continue
    ps = sorted(touched)
    what_en = '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps)
    what_zh = '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps)
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith(f'{TAG} (the stepwise classes and loss)'):
        last['en'] = last['en'].replace(' The claim is unchanged.', f' Also re-pointed after reading the change: {what_en}. The claim is unchanged.')
        last['zh'] = last['zh'].replace('论断不变。', f'另读过改动后重新指向：{what_zh}。论断不变。')
    else:
        d['history'].append({
            'en': f'{TAG} (the stepwise classes and loss):'
                  + (f' proof binding to Significance.lean rebound to core receipt {RID}.' if rebound else '')
                  + (f' Re-pointed after reading the change: {what_en}.' if ps else '') + ' The claim is unchanged.',
            'zh': '2026年10月20日，R27（逐步类别与失去）：'
                  + (f'Significance.lean 的证明绑定改到核心回执 {RID}。' if rebound else '')
                  + (f'读过改动后重新指向：{what_zh}。' if ps else '') + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(ps), 'rebound' if rebound else '')
print(n, 'records changed')
