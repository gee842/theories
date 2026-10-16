#!/usr/bin/env python3
"""P59 + P58: the repoint spec and module counts, from the worktree's new receipts against HEAD's:
python3 -B p5859_spec.py ROOT OUTDIR

Writes OUTDIR/spec.json (for shared/repoint.py), OUTDIR/counts.json (for shared/modcounts.py) and OUTDIR/values.json.
P59 + P58 adds two core modules (Becoming.Decidedness, Becoming.Imbalance), so the package and the core closure each
grow by two; the only existing modules whose theorem counts may change are Space and Openness (the settling lemmas);
Premises and Sampling change statements in place with their counts unchanged."""
import json
import subprocess
import sys
from pathlib import Path

ROOT, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
C = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json'
P = ('experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/'
     'correction-inquiry-verification.json')
core, peri = json.loads((ROOT / C).read_text()), json.loads((ROOT / P).read_text())
ocore = json.loads(subprocess.check_output(['git', '-C', str(ROOT), 'show', 'HEAD:' + C]))
operi = json.loads(subprocess.check_output(['git', '-C', str(ROOT), 'show', 'HEAD:' + P]))
assert core['status'] == 'passed' and peri['status'] == 'passed'
RUN, PERI, OLD, OLDP = core['utc'], peri['utc'], ocore['utc'], operi['utc']
assert RUN != OLD and PERI != OLDP, 'run both checkers first'


def stats(c):
    spine = [m for m in c['modules'] if m['spine']]
    return (sum(m['theorems'] for m in spine), sum(len(m['declarations']) for m in spine), len(spine),
            len(c['core_closure']), {m['module']: m['theorems'] for m in c['modules']})


th, au, pk, cl, cnt = stats(core)
oth, oau, opk, ocl, ocnt = stats(ocore)
NEW = {'Becoming.Decidedness', 'Becoming.Imbalance'}
assert set(cnt) - set(ocnt) == NEW and not set(ocnt) - set(cnt), (set(cnt) ^ set(ocnt))
assert (pk, cl) == (opk + 2, ocl + 2), ('P59 + P58 adds two modules', opk, pk, ocl, cl)
rest, orest = len(peri['compile_order']) - 1, len(operi['compile_order']) - 1
changed = {m: (ocnt[m], cnt[m]) for m in cnt if m in ocnt and ocnt[m] != cnt[m]}
assert set(changed) <= {'Becoming.Space', 'Becoming.Openness'}, changed
mods = '、'.join(f'{m.split(".")[-1]}（{a}→{b}）' for m, (a, b) in changed.items()) or '无'
mods_en = ', '.join(f'{m.split(".")[-1]} ({a} to {b})' for m, (a, b) in changed.items()) or 'none'
spec = {
    'old_run': OLD, 'new_run': RUN, 'old_totals': [oth, oau], 'new_totals': [th, au],
    'old_package': opk, 'new_package': pk, 'old_closure': ocl, 'new_closure': cl,
    'old_peri': OLDP, 'new_peri': PERI, 'old_peri_rest': orest, 'new_peri_rest': rest,
    'extra': [['外围回执 ' + OLDP, '外围回执 ' + PERI], ['periphery receipt ' + OLDP, 'periphery receipt ' + PERI],
              ['同一回执 ' + OLD, '同一回执 ' + RUN], ['same receipt ' + OLD, 'same receipt ' + RUN]],
    'skip': [],
    'history_zh': f'2026-10-12 P59+P58：验证范围重新指向合并检查器回执 {RUN} 与外围回执 {PERI}（新核心模块 Becoming.Decidedness '
                  f'与 Becoming.Imbalance，包与核心闭包各加两个模块；静止定理一族在原处去掉未用的判定程序，名称不变，平息的引理加在 '
                  f'Space 与 Openness；定理数改变的既有模块：{mods}）。断言不变。',
    'history_en': f'2026-10-12 P59+P58: validation scope re-pointed to consolidated receipt {RUN} and periphery receipt '
                  f'{PERI} (new core modules Becoming.Decidedness and Becoming.Imbalance, the package and the core closure '
                  f'each two modules larger; the rest theorems drop their unused decision procedure in place, names kept, '
                  f'with the settling lemmas added in Space and Openness; existing modules whose theorem count changed: '
                  f'{mods_en}). The claim is unchanged.',
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'spec.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1))
(OUT / 'counts.json').write_text(json.dumps({'old': {m: a for m, (a, b) in changed.items()},
                                             'new': {m: b for m, (a, b) in changed.items()}}))
(OUT / 'values.json').write_text(json.dumps({
    'RUN': RUN, 'PERI': PERI, 'OLD_RUN': OLD, 'OLD_PERI': OLDP, 'TH': th, 'AU': au, 'OLD_TH': oth, 'OLD_AU': oau,
    'CL': cl, 'PK': pk, 'OLD_CL': ocl, 'OLD_PK': opk, 'COUNT': cnt}))
print('run', RUN, 'periphery', PERI, 'totals', (oth, oau), '->', (th, au), 'package', opk, '->', pk, 'closure', ocl,
      '->', cl, 'changed', changed, 'new', {m: cnt[m] for m in NEW})
