#!/usr/bin/env python3
"""P58c: the repoint spec and module counts, from the worktree's new receipts against HEAD's:
python3 -B p58c_spec.py ROOT OUTDIR
P58c names the rest family by strength: no module is added; Space gains two theorems (rests_unrefuted_iff,
not_recurring_of_rests_unrefuted; RestsFrom is a definition), Locality two (ceasing_steps_unrefuted,
Covers.ceasing_stops_unrefuted), Resolution one (restsFrom_of_after); no other module's count changes."""
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
ADDED = {'Becoming.Space': 2, 'Becoming.Locality': 2, 'Becoming.Resolution': 1}
assert changed == {m: (ocnt[m], ocnt[m] + k) for m, k in ADDED.items()}, changed
assert th == oth + 5 and au > oau, ((oth, oau), (th, au))
spec = {
    'old_run': OLD, 'new_run': RUN, 'old_totals': [oth, oau], 'new_totals': [th, au],
    'old_package': opk, 'new_package': pk, 'old_closure': ocl, 'new_closure': cl,
    'old_peri': OLDP, 'new_peri': PERI, 'old_peri_rest': orest, 'new_peri_rest': rest,
    'extra': [['外围回执 ' + OLDP, '外围回执 ' + PERI], ['periphery receipt ' + OLDP, 'periphery receipt ' + PERI],
              ['同一回执 ' + OLD, '同一回执 ' + RUN], ['same receipt ' + OLD, 'same receipt ' + RUN]],
    'skip': [],
    'history_zh': f'2026-10-12 P58c：验证范围重新指向合并检查器回执 {RUN} 与外围回执 {PERI}（静止一族按所证强度命名：从某步起静止'
                  f'不能被否证者名带 unrefuted，其陈述加强；只证不复现者名带 not_recurring；Space、Locality、Resolution 新增 5 项定理）。',
    'history_en': f'2026-10-12 P58c: validation scope re-pointed to consolidated receipt {RUN} and periphery receipt {PERI} '
                  f'(the rest family named by the strength proved: theorems proving that resting from some step on cannot be '
                  f'refuted are named with unrefuted, their statements strengthened; those proving only non-recurrence are named '
                  f'with not_recurring; Space, Locality and Resolution add five theorems).',
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'spec.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1))
(OUT / 'counts.json').write_text(json.dumps({'old': {m: a for m, (a, b) in changed.items()},
                                             'new': {m: b for m, (a, b) in changed.items()}}))
(OUT / 'values.json').write_text(json.dumps({
    'RUN': RUN, 'PERI': PERI, 'OLD_RUN': OLD, 'OLD_PERI': OLDP, 'TH': th, 'AU': au, 'OLD_TH': oth, 'OLD_AU': oau,
    'CL': cl, 'PK': pk, 'COUNT': cnt, 'OLD_COUNT': ocnt}))
print('run', RUN, 'periphery', PERI, 'totals', (oth, oau), '->', (th, au), 'package', pk, 'closure', cl, 'changed', changed)
