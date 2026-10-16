#!/usr/bin/env python3
"""P58b: the repoint spec and module counts, from the worktree's new receipts against HEAD's:
python3 -B p58b_spec.py ROOT OUTDIR
P58b renames six settling lemmas and adds stop_unrefuted_iff in Space: no module is added, Space's count rises by one
and no other module's count changes."""
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
    assert all(not v for m in spine for v in m['axiom_dependencies'].values())
    return (sum(m['theorems'] for m in spine), sum(len(m['declarations']) for m in spine), len(spine),
            len(c['core_closure']), {m['module']: m['theorems'] for m in c['modules']})


th, au, pk, cl, cnt = stats(core)
oth, oau, opk, ocl, ocnt = stats(ocore)
assert set(cnt) == set(ocnt) and (pk, cl) == (opk, ocl)
rest, orest = len(peri['compile_order']) - 1, len(operi['compile_order']) - 1
changed = {m: (ocnt[m], cnt[m]) for m in cnt if ocnt[m] != cnt[m]}
assert changed == {'Becoming.Space': (ocnt['Becoming.Space'], ocnt['Becoming.Space'] + 1)}, changed
assert (th, au) == (oth + 1, oau + 1), ((oth, oau), (th, au))
spec = {
    'old_run': OLD, 'new_run': RUN, 'old_totals': [oth, oau], 'new_totals': [th, au],
    'old_package': opk, 'new_package': pk, 'old_closure': ocl, 'new_closure': cl,
    'old_peri': OLDP, 'new_peri': PERI, 'old_peri_rest': orest, 'new_peri_rest': rest,
    'extra': [['外围回执 ' + OLDP, '外围回执 ' + PERI], ['periphery receipt ' + OLDP, 'periphery receipt ' + PERI],
              ['同一回执 ' + OLD, '同一回执 ' + RUN], ['same receipt ' + OLD, 'same receipt ' + RUN]],
    'skip': [],
    'history_zh': f'2026-10-12 P58b：验证范围重新指向合并检查器回执 {RUN} 与外围回执 {PERI}（P58 的六个平息引理改名，使名称恰是'
                  f'陈述所说：停止不能被否证；Space 加 stop_unrefuted_iff，{ocnt["Becoming.Space"]}→{cnt["Becoming.Space"]}；'
                  f'陈述与证明不变）。断言不变。',
    'history_en': f'2026-10-12 P58b: validation scope re-pointed to consolidated receipt {RUN} and periphery receipt '
                  f'{PERI} (P58\'s six settling lemmas renamed so each name says exactly what its statement says: '
                  f'stopping unrefuted; Space adds stop_unrefuted_iff, {ocnt["Becoming.Space"]} to {cnt["Becoming.Space"]}; '
                  f'statements and proofs unchanged). The claim is unchanged.',
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'spec.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1))
(OUT / 'counts.json').write_text(json.dumps({'old': {m: a for m, (a, b) in changed.items()},
                                             'new': {m: b for m, (a, b) in changed.items()}}))
(OUT / 'values.json').write_text(json.dumps({
    'RUN': RUN, 'PERI': PERI, 'OLD_RUN': OLD, 'OLD_PERI': OLDP, 'TH': th, 'AU': au, 'OLD_TH': oth, 'OLD_AU': oau,
    'CL': cl, 'PK': pk, 'COUNT': cnt, 'OLD_COUNT': ocnt}))
print('run', RUN, 'periphery', PERI, 'totals', (oth, oau), '->', (th, au), 'package', pk, 'closure', cl, 'changed', changed)
