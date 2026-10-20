#!/usr/bin/env python3
"""CG2 landing text: chapter §2.3 (EN bullet, records line, theorem-map row; ZH theorem list, records line, map
row) and the coverage row (degeneration). From the checkout root: python3 -B apply_text.py"""
import json
from pathlib import Path

ROOT = Path.cwd()
EN = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
COV = ROOT / 'theories/becoming/results/completion/COVERAGE.json'
REC = '[the-rest-outruns-the-renewal](../results/records/the-rest-outruns-the-renewal.md)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


en = EN.read_text()
en = once(en, '''so the loss is the member's continuation [AI reading, D44].
''', '''so the loss is the member's continuation [AI reading, D44].
- `Flow.outrun_below`: where a part (the rest) takes jointly more than is given at each of `n` steps from a level below `n + m`, the level stays below `m` from then on and every formation depending at that need ends, whatever a member outside the part takes (`Flow.outrun_excess`, `Flow.outrun_ends`; full taking alongside another taker is the case of a part of two). With need one, every reading of the condition after the rest's end is alike under the member's acts (`Flow.outrun_reading_alike`), so no weight of such a reading selects its restraint. Tested on learners in a gated commons (CG2, `experiments/commons-outrun`, predictions frozen before any run): where the other members alone empty the patch, coupled learners empty it for every weight of an end reading; where they cannot, learners keep it, though the whole group at full draw would empty it.
''')
en = once(en, '[what-taking-all-excludes](../results/records/what-taking-all-excludes.md), [where-a-rising-take-ends]',
          '[what-taking-all-excludes](../results/records/what-taking-all-excludes.md), ' + REC + ', [where-a-rising-take-ends]')
en = once(en, '| [What taking all that is given excludes](../results/records/what-taking-all-excludes.md) | theorem without premise | — | §2.3 |\n',
          '| [What taking all that is given excludes](../results/records/what-taking-all-excludes.md) | theorem without premise | — | §2.3 |\n'
          '| [The rest outruns the renewal](../results/records/the-rest-outruns-the-renewal.md) | theorem under stated premises | activity needing support | §2.3 |\n')
EN.write_text(en)

zh = ZH.read_text()
zh = once(zh, '`Flow.continuing_excludes`、`Flow.seeking_ends`；', '`Flow.continuing_excludes`、`Flow.outrun_below`、`Flow.seeking_ends`；')
zh = once(zh, '[what-taking-all-excludes](../results/records/what-taking-all-excludes.md)、[where-a-rising-take-ends]',
          '[what-taking-all-excludes](../results/records/what-taking-all-excludes.md)、' + REC + '、[where-a-rising-take-ends]')
zh = once(zh, '| [取尽所给所排除的](../results/records/what-taking-all-excludes.md) | 不加前提的定理 | — | §2.3 |\n',
          '| [取尽所给所排除的](../results/records/what-taking-all-excludes.md) | 不加前提的定理 | — | §2.3 |\n'
          '| [其余者超出更新](../results/records/the-rest-outruns-the-renewal.md) | 在所述前提下的定理 | 活动需要支持 | §2.3 |\n')
ZH.write_text(zh)

text = COV.read_text()
cov = json.loads(text)
row = next(r for r in cov['rows'] if r['id'] == 'degeneration') if 'rows' in cov else None
assert row is not None, list(cov)[:5]
assert 'the-rest-outruns-the-renewal' not in row['records']
row['records'].insert(row['records'].index('what-taking-all-excludes') + 1, 'the-rest-outruns-the-renewal')
row['declarations'].insert(row['declarations'].index('Becoming.Flow.continuing_excludes') + 1, 'Becoming.Flow.outrun_below')
COV.write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('applied')
