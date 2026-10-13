"""One consolidated P86–P88 landing, reusing the three source-preserving packages."""
from pathlib import Path
import runpy

BASE = Path(__file__).resolve().parent.parent
RUNS = ['becoming-p86-landing', 'becoming-p87-landing', 'becoming-p88-landing']
configs = [runpy.run_path(str(BASE / name / 'config.py')) for name in RUNS]
LABEL = 'P86 + P87 + P88'
PACKAGES = [p for c in configs for p in c['PACKAGES']]
assert len(PACKAGES) == 3
assert [p['module'] for p in PACKAGES] == ['Feeding', 'Persistence', 'OrderNormal']
assert len({p['key'] for p in PACKAGES}) == 3
PLAN_ZH = '\n'.join(c['PLAN_ZH'] for c in configs)
PLAN_EN = '\n'.join(c['PLAN_EN'] for c in configs)
CHAPTER_EDITS = [edit for c in configs for edit in c['CHAPTER_EDITS']]
RECORDS, HISTORY, VALUES = {}, {}, {}
for c in configs:
    for dest, key in [(RECORDS, 'RECORDS'), (HISTORY, 'HISTORY'), (VALUES, 'VALUES')]:
        for k, v in c.get(key, {}).items():
            assert k not in dest, ('duplicate configuration key', key, k)
            dest[k] = v
# One catalogue mutation for the combined run. The prose remains a concise argument
# summary; the chapter retains each package's own local insertion and scope.
READING = dict(
    after_en=configs[2]['READING']['after_en'],
    after_zh=configs[2]['READING']['after_zh'],
    en=('Earlier giving can meet later need through a condition carried across steps: the least feeding closure '
        'so extended contains the same-step closure, strictly through storage. Local balance exactly characterizes '
        'meeting a need; redundant feeders can stand in for one another. Possible carrying does not identify '
        'actual origin, and support is not sufficient for activity (P86). ' +
        configs[1]['READING']['en'] + configs[2]['READING']['en']),
    zh=('较早给予通过跨步携带的条件接到较晚所需，扩展后的最小供给闭包含同一步闭包，储存可使包含严格；局部平衡精确刻画需要满足，'
        '冗余供给者可以相互替代；可能携带未确定实际来源，支持不充分推出活动（P86）。' +
        configs[1]['READING']['zh'] + configs[2]['READING']['zh']),
    lean_after='Interdependence.lean',
)
DELTAS = ['record_deltas.py']
